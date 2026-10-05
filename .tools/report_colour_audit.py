"""Report and news event text on light parchment must carry no § colour codes.

python report_colour_audit.py [--json out.json] [--event NNN]

Walks every country_event and news_event (and super-event report windows defined as events) in events/*.txt, collects
their title/desc localisation keys (plain, triggered desc blocks and option names are excluded: option buttons are
dark), follows [This.GetX] / [Root.GetX] scripted localisation recursively, and prints every reached key whose text
contains a § code, grouped by event file.
"""
import glob
import json
import os
import re
import sys

from pathlib import Path

REPO = str(Path(__file__).resolve().parent.parent)


def load_loc():
    loc = {}
    for p in glob.glob(os.path.join(REPO, 'localisation', 'english', '*.yml')):
        for n, l in enumerate(open(p, encoding='utf-8-sig', errors='replace'), 1):
            m = re.match(r'\s*([\w.\-]+):\d*\s*"(.*)"\s*$', l.rstrip('\r\n'))
            if m:
                loc[m.group(1)] = (os.path.basename(p), n, m.group(2))
    return loc


def load_defined_texts():
    blocks = {}
    for p in glob.glob(os.path.join(REPO, 'common', 'scripted_localisation', '*.txt')):
        s = open(p, encoding='utf-8-sig', errors='replace').read()
        s = re.sub(r'#[^\n]*', '', s)
        for m in re.finditer(r'defined_text\s*=\s*\{\s*name\s*=\s*([\w.]+)', s):
            i, d = s.index('{', m.start()) + 1, 1
            while d and i < len(s):
                if s[i] == '{':
                    d += 1
                elif s[i] == '}':
                    d -= 1
                i += 1
            blocks.setdefault(m.group(1), []).extend(re.findall(r'localization_key\s*=\s*"?([\w.\-]+)', s[m.start():i]))
    return blocks


def event_blocks(s):
    for m in re.finditer(r'\b(country_event|news_event|state_event|unit_leader_event|operative_leader_event)\s*=\s*\{', s):
        i, d = m.end(), 1
        while d and i < len(s):
            if s[i] == '{':
                d += 1
            elif s[i] == '}':
                d -= 1
            i += 1
        yield m.group(1), s[m.start():i]


def strip_options(body):
    out, i = [], 0
    for m in re.finditer(r'\boption\s*=\s*\{', body):
        if m.start() < i:
            continue
        out.append(body[i:m.start()])
        j, d = m.end(), 1
        while d and j < len(body):
            if body[j] == '{':
                d += 1
            elif body[j] == '}':
                d -= 1
            j += 1
        i = j
    out.append(body[i:])
    return ''.join(out)


def main():
    only = None
    out_json = None
    a = sys.argv[1:]
    if '--event' in a:
        only = a[a.index('--event') + 1]
    if '--json' in a:
        out_json = a[a.index('--json') + 1]
    loc, dt = load_loc(), load_defined_texts()
    result = {}
    for p in sorted(glob.glob(os.path.join(REPO, 'events', '*.txt'))):
        base = os.path.basename(p)
        if only and not base.startswith(only):
            continue
        s = re.sub(r'#[^\n]*', '', open(p, encoding='utf-8-sig', errors='replace').read())
        roots = set()
        for kind, body in event_blocks(s):
            if re.search(r'\bhidden\s*=\s*yes', body):
                continue
            head = strip_options(body)
            for k in re.findall(r'\b(?:title|desc)\s*=\s*"?([\w.\-]+)"?\s*(?:\n|\})', head):
                roots.add(k)
            for k in re.findall(r'\btext\s*=\s*"?([\w.\-]+)', head):
                roots.add(k)
        seen, todo_k, todo_n = set(), list(roots), []
        seen_n = set()
        while todo_k or todo_n:
            while todo_n:
                n = todo_n.pop()
                if n in seen_n:
                    continue
                seen_n.add(n)
                todo_k += dt.get(n, [])
            while todo_k:
                k = todo_k.pop()
                if k in seen or k not in loc:
                    continue
                seen.add(k)
                todo_n += re.findall(r'\.(Get\w+)\]', loc[k][2])
                todo_n += re.findall(r'\[(Get\w+)\]', loc[k][2])
        hits = sorted((loc[k][0], loc[k][1], k) for k in seen if '§' in loc[k][2])
        if hits:
            result[base] = [{'file': f, 'line': n, 'key': k} for f, n, k in hits]
    total = sum(len(v) for v in result.values())
    for ev, hs in result.items():
        print(f'{ev}: {len(hs)}')
    print('total keys with colour:', total)
    if out_json:
        json.dump(result, open(out_json, 'w', encoding='utf-8'), indent=1)


if __name__ == '__main__':
    main()
