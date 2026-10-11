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

UPSTREAM = Path('/home/klim/tools/Clausewitz-MCP')
GAME = Path('/home/klim/games/hoi4/hoi4')
RUNTIME = Path('/home/klim/.local/share/chaosx-live')
LOCK = Path('/tmp/hoi4_wsl.lock')
PIN = '97c85437081904d5ad07bae1623ec58d1c0a5b9e'
BUILD = '2a79e51358b8b71c09cfb5ddefa0c03649067a4b'
DISPLAY = ':91'


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
    if actual != BUILD:
        raise RuntimeError(f'Unsupported HOI4 ELF build {actual}; reviewed offsets require {BUILD} (1.19.2). No memory access or injection attempted.')


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
    return {
        'upstream_commit': PIN, 'game_executable': str(GAME),
        'expected_elf_build': BUILD, 'installed_elf_build': actual,
        'compatible': actual == BUILD, 'display': DISPLAY, 'job': job,
        'lease_owner': LOCK.read_text().strip() if LOCK.is_file() else None,
        'ptrace_scope': Path('/proc/sys/kernel/yama/ptrace_scope').read_text().strip(),
        'transport': 'stdio', 'network_listeners': False,
    }


def screenshot(job, crop=None, focus=False):
    if focus:
        raise RuntimeError('Desktop focusing is disabled; capture the private game window')
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
    server.GAME_DIR = str(GAME.parent)
    server.DOC_MD = str(GAME.parent / 'documentation/console_commands_documentation.md')
    server.screenshot = lambda crop=None, focus=False: screenshot(job, crop, focus)
    for tool in server.TOOLS:
        if tool['name'] == 'hoi4_screenshot':
            tool['description'] = 'Capture only the owned Linux game window on private display :91. Requires this job\'s WSL lease. Desktop fallback and focus=true are disabled.'
    server.tool('clausewitz_linux_preflight', 'Read installation/build/lease metadata without attaching to the game.')(lambda args: preflight(job))
    upstream_handle = server.handle

    def handle(message):
        if message.get('method') == 'tools/call':
            name = (message.get('params') or {}).get('name')
            try:
                if name != 'clausewitz_linux_preflight':
                    # Check compatibility before even a state getter: some inject calls.
                    if name != 'hoi4_screenshot':
                        require_build()
                    target = owned_pid(job)
                    if name != 'hoi4_screenshot':
                        require_build(Path(f'/proc/{target}/exe'))
                    if server._g is not None and server._g.p.pid != target:
                        server._g = None
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


if __name__ == '__main__':
    try:
        main()
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
