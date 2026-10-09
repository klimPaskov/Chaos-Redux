#!/usr/bin/env python3
"""Apply shared read budgets to supported runtime settings; preserve other settings.

Default: project Codex, Claude and OpenCode settings. --user-defaults also updates
their user defaults. --dsh-profile names an existing profile patch explicitly.
Cursor/Qoder have no verified equivalent setting; AGENTS.md carries the policy.
Byte-based caps are explicit byte budgets, not exact tokenizer conversions.
"""
import argparse
import json
import os
from pathlib import Path
import re
import tempfile

try:
    import tomllib
except ImportError:
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[2]
CONFIG = Path(__file__).with_name('read_limits.json')


def read(path):
    return path.read_text(encoding='utf-8-sig') if path.exists() else ''


def write(path, text, check):
    old = path.read_bytes() if path.exists() else b''
    newline = '\r\n' if old.count(b'\r\n') > old.count(b'\n') / 2 else '\n'
    data = text.replace('\r\n', '\n').replace('\n', newline).encode('utf-8')
    if old == data:
        return False
    if not check:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, temporary = tempfile.mkstemp(prefix=path.name + '.', dir=path.parent)
        try:
            with os.fdopen(fd, 'wb') as output:
                output.write(data)
            os.replace(temporary, path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    print(('Would update ' if check else 'Updated ') + str(path))
    return True


def codex(path, tokens, check):
    text = read(path)
    before = tomllib.loads(text)
    # Only top-level assignment; leave agent/provider table fields alone.
    end = next((m.start() for m in re.finditer(r'^\s*\[', text, re.M)), len(text))
    header, rest = text[:end], text[end:]
    replacement = 'tool_output_token_limit = ' + str(tokens)
    pattern = r'^tool_output_token_limit\s*=.*$'
    if re.search(pattern, header, re.M):
        header = re.sub(pattern, replacement, header, flags=re.M)
    else:
        header = header.rstrip() + ('\n' if header.strip() else '') + replacement + '\n\n'
    updated = header + rest
    expected = dict(before, tool_output_token_limit=tokens)
    assert tomllib.loads(updated) == expected, 'Unexpected Codex settings change'
    return write(path, updated, check)


def json_settings(path, group, values, check):
    text = read(path)
    data = json.loads(text) if text.strip() else {}
    current = data.setdefault(group, {})
    if not isinstance(current, dict):
        raise ValueError(str(path) + ': ' + group + ' must be an object')
    current.update(values)
    return write(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n', check)


def dsh(path, limits, byte_limit, check):
    import yaml  # Required only when updating an explicitly named DSH profile.
    if not path.is_file():
        raise FileNotFoundError('DSH profile patch must already exist: ' + str(path))
    text = read(path)
    data = yaml.safe_load(text) or []
    if not isinstance(data, list):
        raise ValueError('DSH profile patch must be a loader-entry array')
    matches = [entry for entry in data if isinstance(entry, dict) and entry.get('id') == 'tool-fs']
    if len(matches) > 1:
        raise ValueError('Duplicate tool-fs profile overrides')
    entry = matches[0] if matches else {'id': 'tool-fs'}
    entry.setdefault('config', {}).update({
        'readLimit': limits['line_limit'],
        'readMaxBytes': byte_limit,
        'readMaxLineLength': byte_limit,
    })
    rendered = yaml.safe_dump([entry], sort_keys=False, allow_unicode=True)
    if matches:
        pattern = r'^- id: [\'\"]?tool-fs[\'\"]?\s*\n.*?(?=^- |\Z)'
        updated, count = re.subn(pattern, lambda _: rendered, text, flags=re.M | re.S)
        if count != 1:
            raise ValueError('Cannot isolate the existing tool-fs override safely')
    else:
        data.append(entry)
        updated = text.rstrip() + '\n' + rendered
    assert yaml.safe_load(updated) == data, 'Unexpected DSH profile change'
    return write(path, updated, check)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Report drift without writing; exit 1 for drift')
    parser.add_argument('--user-defaults', action='store_true', help='Also apply supported defaults to this user')
    parser.add_argument('--dsh-profile', type=Path, help='Existing cordis.patch.yml to update, without starting DSH')
    args = parser.parse_args()
    limits = json.loads(CONFIG.read_text(encoding='utf-8'))
    for key, value in limits.items():
        if type(value) is not int or value <= 0:
            raise ValueError(key + ' must be a positive integer')
    if limits['guidance_file_tokens'] >= limits['read_output_tokens']:
        raise ValueError('The file budget must leave reader headroom')
    tokens = limits['read_output_tokens']
    byte_limit = tokens * limits['estimated_bytes_per_token']
    homes = [(ROOT / '.codex/config.toml', ROOT / '.claude/settings.json', ROOT / '.opencode/opencode.json')]
    if args.user_defaults:
        user = Path.home()
        homes.append((user / '.codex/config.toml', user / '.claude/settings.json', user / '.config/opencode/opencode.json'))
    changed = 0
    for codex_path, claude_path, opencode_path in homes:
        changed += codex(codex_path, tokens, args.check)
        changed += json_settings(claude_path, 'env', {
            'CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS': str(tokens),
            'MAX_MCP_OUTPUT_TOKENS': str(tokens),
        }, args.check)
        changed += json_settings(opencode_path, 'tool_output', {
            'max_bytes': byte_limit,
            'max_lines': limits['line_limit'],
        }, args.check)
    if args.dsh_profile:
        changed += dsh(args.dsh_profile.resolve(), limits, byte_limit, args.check)
    print('Read target: %d tokens; guidance ceiling: %d tokens.' % (tokens, limits['guidance_file_tokens']))
    print('OpenCode/DSH use byte/line caps; Cursor/Qoder inherit the guidance policy, not an invented native setting.')
    return 1 if args.check and changed else 0


if __name__ == '__main__':
    raise SystemExit(main())
