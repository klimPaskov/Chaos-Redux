#!/usr/bin/env python3
"""WSL-only Clausewitz entry point; see docs/testing/clausewitz_mcp_linux.md.

Inputs: command, job name, fixed reviewed checkout and Linux game paths.
Outputs: stdio MCP, preflight JSON, or exec of the opt-in Linux game.
No listeners, Windows fallback, global ptrace change, or game-file patch.
"""
from __future__ import annotations

import argparse
import ctypes
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time

UPSTREAM = Path('/home/klim/tools/Clausewitz-MCP')
GAME = Path('/home/klim/games/hoi4/hoi4')
RUNTIME = Path('/home/klim/.local/share/chaosx-live')
LOCK = Path('/tmp/hoi4_wsl.lock')
PIN = '97c85437081904d5ad07bae1623ec58d1c0a5b9e'
PINNED_BUILD = '2a79e51358b8b71c09cfb5ddefa0c03649067a4b'
TARGET_BUILD = 'a4971c9e8ac9a6f2487dea109e01f9839ee59db7'
PORT = Path('/home/klim/tools/Clausewitz-MCP-ports/1.19.3')
TARGET_TABLE = PORT / 'runtime_table_1193.json'
RECOVERY_LOG = PORT / 'live_call_recovery_1193.jsonl'
DISPLAY = ':91'


def load_target_table():
    if not TARGET_TABLE.is_file():
        raise RuntimeError(f'Missing reviewed 1.19.3 table: {TARGET_TABLE}')
    table = json.loads(TARGET_TABLE.read_text(encoding='utf-8'))
    if table.get('build_id') != TARGET_BUILD or table.get('version') != '1.19.3':
        raise RuntimeError('1.19.3 table identity does not match its selector')
    return table


def build_profile(actual):
    if actual == PINNED_BUILD:
        return {'build_id': PINNED_BUILD, 'version': '1.19.2', 'status': 'upstream-pinned', 'table': None}
    if actual == TARGET_BUILD:
        table = load_target_table()
        return {'build_id': TARGET_BUILD, 'version': '1.19.3', 'status': table.get('status', 'partial'), 'table': table}
    return None


def command_output(*args):
    return subprocess.check_output(args, text=True, timeout=20).strip()


def build_id(path):
    text = command_output('readelf', '-n', str(path))
    match = re.search(r'Build ID: ([0-9a-f]+)', text)
    if not match:
        raise RuntimeError('ELF build ID is missing; attachment refused')
    return match[1]


def check_checkout():
    if command_output('git', '-C', str(UPSTREAM), 'rev-parse', 'HEAD') != PIN:
        raise RuntimeError('Clausewitz checkout is not the reviewed commit')
    if command_output('git', '-C', str(UPSTREAM), 'status', '--porcelain', '--untracked-files=no'):
        raise RuntimeError('Reviewed upstream tracked files have changed')
    if not GAME.is_file() or GAME.is_symlink():
        raise RuntimeError('Expected a regular executable in the isolated Linux install')


def require_build(path=GAME):
    actual = build_id(path)
    profile = build_profile(actual)
    if profile is None:
        raise RuntimeError(f'Unsupported HOI4 ELF build {actual}; reviewed entries cover only {PINNED_BUILD} (1.19.2) and {TARGET_BUILD} (1.19.3). No memory access or injection attempted.')
    return profile


def require_lease(job):
    if not re.fullmatch(r'[a-zA-Z0-9_-]+', job):
        raise RuntimeError('Invalid job name')
    owner = LOCK.read_text().strip() if LOCK.is_file() else None
    if owner != job:
        raise RuntimeError(f'WSL game lease belongs to {owner!r}, not {job!r}; live operation refused')


def owned_pid(job):
    require_lease(job)
    pid_text = (RUNTIME / 'hoi4.pid').read_text().strip()
    if not pid_text.isdigit():
        raise RuntimeError('Invalid recorded Linux game PID')
    pid = int(pid_text)
    proc = Path(f'/proc/{pid}')
    if (proc / 'exe').resolve(strict=True) != GAME:
        raise RuntimeError('Recorded process is not the isolated Linux game')
    if (proc / 'status').stat().st_uid != os.getuid():
        raise RuntimeError('Game must run as the same unprivileged Linux user')
    env = (proc / 'environ').read_bytes().split(b'\0')
    if b'DISPLAY=:91' not in env:
        raise RuntimeError('Game is not on the private display :91')
    return pid


def preflight(job):
    check_checkout()
    actual = build_id(GAME)
    profile = build_profile(actual)
    table = profile.get('table') if profile else None
    return {
        'upstream_commit': PIN, 'game_executable': str(GAME),
        'reviewed_elf_builds': [PINNED_BUILD, TARGET_BUILD], 'installed_elf_build': actual,
        'compatible': profile is not None, 'table_status': profile.get('status') if profile else 'unknown-build-refused',
        'version': profile.get('version') if profile else None,
        'target_test_tools': table.get('test_eligible_tools', []) if table else 'upstream tool set',
        'display': DISPLAY, 'job': job,
        'lease_owner': LOCK.read_text().strip() if LOCK.is_file() else None,
        'ptrace_scope': Path('/proc/sys/kernel/yama/ptrace_scope').read_text().strip(),
        'transport': 'stdio', 'network_listeners': False,
    }


def screenshot(job, crop=None, focus=False):
    if focus:
        raise RuntimeError('Desktop focusing is disabled; capture the private game window')
    require_build()
    if crop and not re.fullmatch(r'\d+x\d+[+-]\d+[+-]\d+', crop):
        raise ValueError('Crop must be WIDTHxHEIGHT+X+Y')
    pid = owned_pid(job)
    env = dict(os.environ, DISPLAY=DISPLAY)
    windows = subprocess.check_output(
        ['xdotool', 'search', '--onlyvisible', '--pid', str(pid)],
        env=env, text=True, timeout=10).splitlines()
    if not windows:
        raise RuntimeError('Owned game has no visible X11 window')
    with tempfile.TemporaryDirectory(prefix='clausewitz-shot-') as temp:
        output = Path(temp) / 'game.png'
        subprocess.run(['import', '-silent', '-display', DISPLAY, '-window', windows[-1], str(output)],
                       env=env, capture_output=True, check=True, timeout=45)
        if crop:
            subprocess.run(['convert', str(output), '-crop', crop, '+repage', str(output)],
                           env=env, capture_output=True, check=True, timeout=20)
        return output.read_bytes()


def serve(job):
    check_checkout()
    profile = require_build()
    os.environ['HOI4_PATH'] = str(GAME.parent)
    sys.path.insert(0, str(UPSTREAM / 'calling'))
    import mem
    import process

    original_init = process.Backend.__init__

    def guarded_init(self, pid=None, exe_name='hoi4'):
        require_build()
        target = owned_pid(job)
        require_build(Path(f'/proc/{target}/exe'))
        if pid is not None and pid != target:
            raise RuntimeError('Explicit PID differs from the owned Linux game')
        original_init(self, target, 'hoi4')

    process.Backend.__init__ = guarded_init
    # Restore the backend delegation hidden by upstream's duplicate broken method.
    mem.Proc.write = lambda self, addr, data: self.be.write(addr, data)
    spec = importlib.util.spec_from_file_location('clausewitz_upstream_server', UPSTREAM / 'mcp/server.py')
    server = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(server)

    target_build = profile['build_id'] == TARGET_BUILD
    target_table = profile.get('table') if target_build else None
    if target_build:
        apply_target_table(target_table)
        install_target_command_catalog(target_table)
        install_target_safe_stack_call(process)
        install_call_recovery_monitor(process)
        import api
        api.multiplayer_detected = lambda game: target_singleplayer_guard(job)

    server.GAME_DIR = str(GAME.parent)
    server.DOC_MD = str(GAME.parent / 'documentation/console_commands_documentation.md')
    server.screenshot = lambda crop=None, focus=False: screenshot(job, crop, focus)
    if target_build:
        server.HANDLERS['hoi4_status'] = lambda args: status_1193(server)
        server.tool('clausewitz_linux_tool_status', 'Per-tool 1.19.3 verification state; unverified tools are blocked.')(lambda args: target_table.get('tool_status', {}))
    for tool in server.TOOLS:
        if target_build and tool['name'] == 'hoi4_status':
            tool['description'] = 'Connection and live state-root status: process, 1.19.3 build, country count, player tag index, and mapped country pointer.'
        if tool['name'] == 'hoi4_screenshot':
            tool['description'] = 'Capture only the owned Linux game window on private display :91. Requires this job\'s WSL lease. Desktop fallback and focus=true are disabled.'
    server.tool('clausewitz_linux_preflight', 'Read installation/build/lease metadata without attaching to the game.')(lambda args: preflight(job))
    upstream_handle = server.handle

    def handle(message):
        if message.get('method') == 'tools/call':
            name = (message.get('params') or {}).get('name')
            try:
                if name not in ('clausewitz_linux_preflight', 'clausewitz_linux_tool_status'):
                    active = require_build()
                    active_table = active.get('table')
                    if active['build_id'] == TARGET_BUILD:
                        allowed = set(active_table.get('test_eligible_tools', []))
                        allowed.update({'clausewitz_linux_tool_status', 'clausewitz_linux_preflight'})
                        if name not in allowed:
                            return server.rpc_result(message.get('id'), {
                                'isError': True,
                                'content': [{'type': 'text', 'text': f'{name} is unverified on 1.19.3 and was blocked before attaching to the game.'}]})
                    # Check the executable again before every target call.
                    target = owned_pid(job)
                    require_build(Path(f'/proc/{target}/exe'))
                    if server._g is not None and server._g.p.pid != target:
                        server._g = None
                    if name == 'hoi4_debug_console':
                        import offsets as O
                        game = server.game()
                        if not game.p.u64(game.va(O.G_IDLER)):
                            return server.rpc_result(message.get('id'), {
                                'isError': True,
                                'content': [{'type': 'text', 'text': 'Console commands are blocked until an active single-player campaign is loaded.'}]})
            except (OSError, RuntimeError, ValueError) as exc:
                return server.rpc_result(message.get('id'), {
                    'isError': True, 'content': [{'type': 'text', 'text': str(exc)}]})
        return upstream_handle(message)

    server.handle = handle
    server.main()


def launch(job, args):
    check_checkout()
    require_build()
    require_lease(job)
    if os.environ.get('DISPLAY') != DISPLAY:
        raise RuntimeError('Opt-in game launch must use private display :91')
    libc = ctypes.CDLL('libc.so.6', use_errno=True)
    libc.prctl.argtypes = [ctypes.c_int, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong]
    libc.prctl.restype = ctypes.c_int
    # PR_SET_PTRACER_ANY applies only to this process and survives exec.
    # Yama/global settings stay unchanged; ordinary same-UID checks still apply.
    if libc.prctl(0x59616D61, ctypes.c_ulong(-1).value, 0, 0, 0) != 0:
        raise OSError(ctypes.get_errno(), 'PR_SET_PTRACER failed')
    os.execv(str(GAME), [str(GAME), *args])


def main():
    if sys.platform != 'linux' or os.getuid() == 0:
        raise RuntimeError('Run only as unprivileged klim in WSL Ubuntu-24.04')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--job', default='clausewitz_linux')
    parser.add_argument('command', choices=['serve', 'preflight', 'check-build', 'launch'])
    parser.add_argument('game_args', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.command == 'serve':
        serve(args.job)
    elif args.command == 'launch':
        launch(args.job, [arg for arg in args.game_args if arg != '--'])
    else:
        info = preflight(args.job)
        print(json.dumps(info, indent=2))
        if args.command == 'check-build':
            require_build()


def apply_target_table(table):
    import api
    import offsets as O
    import session

    for key, value in table.get('globals', {}).items():
        setattr(O, key, int(value, 0))
    O.VERSION = table['version']
    O.BUILD_ID = table['build_id']
    for key, value in table.get('functions', {}).items():
        setattr(O, key, int(value, 0))
    structure_aliases = {
        'PDXARRAY_SIZE_BYTES': 'PDXARRAY_SZ',
        'STDSTRING_SIZE': 'STDSTRING_SZ',
        'SRESULT_SIZE': 'SRESULT_SZ',
    }
    for key, value in table.get('structures', {}).items():
        attr = structure_aliases.get(key, key)
        if hasattr(O, attr):
            setattr(O, attr, int(value, 0))
    for key, value in table.get('country_fields_verified_by_serializer', {}).items():
        attr = 'CO_' + key.upper()
        if hasattr(O, attr):
            setattr(O, attr, int(value, 0))
    for name in ('G_IDLER', 'G_GAMESTATE', 'IDLER_COUNTRY_NAME', 'IDLER_LOCAL_PLAYER'):
        value = table.get('globals', {}).get(name) or table.get('structures', {}).get(name)
        if value is not None and hasattr(session, name):
            setattr(session, name, int(value, 0))
    api.VERIFIED_CALLS = {int(value, 0) for value in table.get('verified_native_calls', [])}
    api.MP_SAFE_CALLS = {int(table['functions'][key], 0) for key in ('FN_OPERATOR_NEW', 'FN_OPERATOR_DELETE') if key in table.get('functions', {})}


def install_target_command_catalog(table):
    import api
    import offsets as O

    ro_lo = int(table['sections']['RODATA_LO'], 0)
    ro_hi = int(table['sections']['RODATA_HI'], 0)

    def command_catalog(self):
        if self._cmds is not None:
            return self._cmds
        manager = self.p.u64(self.va(O.G_CONSOLE_MANAGER))
        if not manager:
            raise RuntimeError('console manager not found')
        data = self.p.u64(manager + O.PDXARRAY_DATA)
        count = self.p.i32(manager + O.PDXARRAY_SIZE)
        if count < 0 or count > 10000:
            raise RuntimeError(f'console command count is invalid: {count}')
        low, high = self.va(ro_lo), self.va(ro_hi)
        commands = {}
        for index in range(count):
            entry = data + index * O.CMD_STRIDE
            name = self.p.stdstring(entry + O.CMD_NAME)
            if not name:
                continue
            alias_count = self.p.i32(entry + O.CMD_ALIAS_COUNT)
            aliases = []
            if 0 < alias_count <= 3:
                for alias_index in range(alias_count):
                    address = self.p.u64(entry + O.CMD_ALIASES + alias_index * 8)
                    if low <= address < high:
                        alias = self.p.cstr(address, 64)
                        if alias:
                            aliases.append(alias)
            function = self.p.u64(entry + O.CMD_FUNC)
            commands[name] = {'aliases': aliases, 'func': 'img+%#x' % (function - self.base) if function else None}
        self._cmds = commands
        return commands

    api.HOI4.command_catalog = command_catalog


def _reg_values(regs):
    return tuple(int(getattr(regs, field)) for field, _ in regs._fields_)


def _thread_state(pid, tid):
    try:
        for line in Path(f'/proc/{pid}/task/{tid}/status').read_text().splitlines():
            if line.startswith('State:'):
                return line.split()[1]
    except OSError:
        return 'missing'
    return 'unknown'


def install_call_recovery_monitor(process):
    original_call = process.Injector.call
    original_detach = process.Injector.detach

    def append_recovery(record):
        PORT.mkdir(parents=True, exist_ok=True)
        with RECOVERY_LOG.open('a', encoding='utf-8') as stream:
            stream.write(json.dumps(record, sort_keys=True) + '\n')

    def monitored_call(self, func_addr, *args, **kwargs):
        expected_tids = sorted(int(tid) for tid in os.listdir(f'/proc/{self.pid}/task'))
        attached_tids = sorted(self.tids)
        if attached_tids != expected_tids:
            raise process.CallError(f'ptrace call refused: attached thread set {attached_tids} differs from process thread set {expected_tids}')
        states_before = {tid: _thread_state(self.pid, tid) for tid in attached_tids}
        if any(state not in ('t', 'T') for state in states_before.values()):
            raise process.CallError(f'ptrace call refused: not every attached thread is stopped: {states_before}')
        before = {tid: _reg_values(self.getregs(tid)) for tid in attached_tids}
        outcome, error = 'returned', None
        try:
            result = original_call(self, func_addr, *args, **kwargs)
        except BaseException as exc:
            outcome, error = 'error', f'{type(exc).__name__}: {exc}'
            result = None
        after, states_after = {}, {}
        recovery_error = None
        try:
            current_tids = sorted(int(tid) for tid in os.listdir(f'/proc/{self.pid}/task'))
            states_after = {tid: _thread_state(self.pid, tid) for tid in attached_tids}
            after = {tid: _reg_values(self.getregs(tid)) for tid in attached_tids}
        except BaseException as exc:
            current_tids = []
            recovery_error = f'{type(exc).__name__}: {exc}'
        comparisons = {tid: before.get(tid) == after.get(tid) for tid in attached_tids}
        all_restored = (not recovery_error and expected_tids == current_tids and all(comparisons.values())
                        and all(state in ('t', 'T') for state in states_after.values()))
        record = {
            'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'pid': self.pid, 'function': hex(func_addr - self.p.base), 'outcome': outcome,
            'error': error, 'recovery_error': recovery_error, 'threads_before': expected_tids,
            'scratch_layout': getattr(self, '_last_scratch_evidence', None),
            'threads_attached': attached_tids, 'threads_after': current_tids,
            'states_before': {str(k): v for k, v in states_before.items()},
            'states_after': {str(k): v for k, v in states_after.items()},
            'registers_restored_by_thread': {str(k): v for k, v in comparisons.items()},
            'registers_restored': bool(all_restored),
        }
        append_recovery(record)
        if error:
            raise process.CallError(error)
        if not all_restored:
            raise process.CallError(f'ptrace call return-state recovery check failed; evidence: {RECOVERY_LOG}')
        return result

    def monitored_detach(self):
        tids = sorted(self.tids)
        pid = self.pid
        result = original_detach(self)
        states = {tid: _thread_state(pid, tid) for tid in tids}
        resumed = all(state not in ('t', 'T', 'missing') for state in states.values())
        append_recovery({
            'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'phase': 'detach', 'pid': pid, 'threads_detached': tids,
            'states_after_detach': {str(k): v for k, v in states.items()},
            'threads_resumed': bool(resumed),
        })
        if not resumed:
            raise process.CallError(f'ptrace detach recovery check failed; evidence: {RECOVERY_LOG}')
        return result

    process.Injector.call = monitored_call
    process.Injector.detach = monitored_detach


def install_target_safe_stack_call(process):
    """Keep the injected return frame and scratch buffer inside the mapped main stack."""
    import signal
    import struct

    backend = process.backend
    regs_type = backend.Regs

    def safe_call(self, func_addr, args=(), scratch_writer=None, timeout=5.0, xmm_zero=True):
        main = self.pid
        old = self.getregs(main)
        saved = regs_type.from_buffer_copy(old)
        stack = next((m for m in self.p.maps
                      if m['start'] <= old.rsp < m['end'] and 'w' in m['perms'] and m.get('path') == '[stack]'), None)
        if stack is None:
            raise process.CallError('ptrace call refused: main-thread writable stack mapping was not found')
        reserve = max(int(self.scratch_size), 0x40000)
        upper_guard = 0x10000
        lower_guard = 0x2000
        scratch = (old.rsp - reserve - upper_guard) & ~0xFFF
        if scratch - lower_guard < stack['start'] or scratch + reserve > old.rsp - 0x8000:
            raise process.CallError('ptrace call refused: stack has insufficient mapped scratch space')
        self._last_scratch_evidence = {
            'stack_start': hex(stack['start']), 'stack_end': hex(stack['end']),
            'saved_rsp': hex(old.rsp), 'scratch': hex(scratch),
            'scratch_size': hex(reserve), 'gap_below_saved_rsp': hex(old.rsp - (scratch + reserve)),
        }
        if scratch_writer:
            args = scratch_writer(scratch) or args

        new = regs_type.from_buffer_copy(old)
        argregs = ['rdi', 'rsi', 'rdx', 'rcx', 'r8', 'r9']
        for index, value in enumerate(args[:6]):
            setattr(new, argregs[index], ctypes.c_ulonglong(value & 0xFFFFFFFFFFFFFFFF).value)
        new.rax = 0
        stack_args = list(args[6:])
        sp = (scratch - lower_guard) & ~0xF
        if len(stack_args) % 2:
            sp -= 8
        sp -= 8 * len(stack_args)
        sp -= 8
        if sp < stack['start'] or scratch + reserve > old.rsp:
            raise process.CallError('ptrace call refused: computed scratch frame falls outside the mapped stack')
        payload = struct.pack('<Q', 0) + b''.join(
            struct.pack('<Q', value & 0xFFFFFFFFFFFFFFFF) for value in stack_args)
        self.p.write(sp, payload)
        new.rsp = sp
        new.rip = func_addr
        self.setregs(new, main)
        backend._ptrace(backend.PTRACE_CONT, main, 0, 0)
        started = time.time()
        status = None
        while True:
            try:
                waited, status = os.waitpid(main, os.WNOHANG | 0x40000000)
            except ChildProcessError:
                waited, status = 0, None
            if waited == main:
                break
            if time.time() - started > timeout:
                self.setregs(saved, main)
                raise process.CallError('call timed out (function %#x)' % func_addr)
            time.sleep(0.001)
        result_regs = self.getregs(main)
        sig = os.WSTOPSIG(status) if os.WIFSTOPPED(status) else None
        result = result_regs.rax
        rip = result_regs.rip
        self.setregs(saved, main)
        if sig != signal.SIGSEGV or rip != 0:
            raise process.CallError('unexpected state: sig=%s rip=%#x (rax=%#x)' % (sig, rip, result))
        return result

    process.Injector.call = safe_call


def status_1193(server):
    import offsets as O
    game = server.game()
    p = game.p
    state = p.u64(game.va(O.G_GAMESTATE))
    if not state:
        raise RuntimeError('game-state root is null; load the test game before reading state')
    country_count = p.i32(state + O.GS_COUNTRIES + O.PDXARRAY_SIZE)
    tag_index = p.i32(state + O.GS_PLAYER_TAG)
    tag_count = p.i32(state + O.GS_TAG2INDEX + O.PDXARRAY_SIZE)
    tag_map = p.u64(state + O.GS_TAG2INDEX + O.PDXARRAY_DATA)
    if country_count < 1 or country_count > 1000 or tag_index < 0 or tag_index >= tag_count or not tag_map:
        raise RuntimeError(f'game-state layout check failed: countries={country_count}, tag_index={tag_index}, tag_count={tag_count}')
    country_index = p.i32(tag_map + tag_index * 4)
    country_array = p.u64(state + O.GS_COUNTRIES + O.PDXARRAY_DATA)
    if not country_array or country_index < 0 or country_index >= country_count:
        raise RuntimeError(f'player country index is invalid: {country_index}/{country_count}')
    country_ptr = p.u64(country_array + country_index * 8)
    idler = p.u64(game.va(O.G_IDLER))
    return {
        'pid': p.pid, 'image_base': hex(p.base), 'version': '1.19.3',
        'countries': country_count,
        'active_campaign': bool(idler),
        'player_tag_index': tag_index, 'player_country_index': country_index,
        'player_country_pointer': hex(country_ptr),
    }


def target_singleplayer_guard(job):
    """Allow target calls only for this adapter-launched, single-player test process."""
    pid = owned_pid(job)
    proc = Path(f'/proc/{pid}')
    environment = (proc / 'environ').read_bytes().split(b'\0')
    command_line = (proc / 'cmdline').read_bytes().split(b'\0')
    if b'HOI4_CLAUSEWITZ=1' not in environment or f'HOI4_WSL_JOB={job}'.encode() not in environment:
        return True
    forbidden = {b'-server', b'--server', b'-multiplayer', b'--multiplayer'}
    if any(argument.lower() in forbidden for argument in command_line if argument):
        return True
    return False


if __name__ == '__main__':
    try:
        main()
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
