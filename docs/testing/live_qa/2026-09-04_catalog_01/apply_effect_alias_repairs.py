from pathlib import Path
import json, re, collections, hashlib
root=Path.cwd(); qa=root/'docs/testing/live_qa/2026-09-04_catalog_01'
records=json.loads((qa/'effect_alias_candidates.json').read_text(encoding='utf-8'))
groups=collections.defaultdict(list)
for record in records: groups[record['path']].append(record)
prepared=[]
for relative,changes in groups.items():
    path=root/relative; original=path.read_bytes(); bom=original.startswith(b'\xef\xbb\xbf')
    lines=original.decode('utf-8-sig').splitlines(keepends=True)
    for change in changes:
        index=change['line']-1
        if lines[index].rstrip('\r\n')!=change['source']: raise RuntimeError(f'Concurrent source change: {relative}:{index+1}')
        pattern=r'(?<!\w)'+re.escape(change['old'])+r'(?=\s*=)'
        lines[index],count=re.subn(pattern,change['new'],lines[index])
        if count!=1: raise RuntimeError(f'Ambiguous keyword: {relative}:{index+1}')
    repaired=(''.join(lines)).encode('utf-8')
    if bom: repaired=b'\xef\xbb\xbf'+repaired
    prepared.append((relative,original,repaired))
for relative,original,repaired in prepared:
    path=root/relative
    if path.read_bytes()!=original: raise RuntimeError(f'Concurrent write: {relative}')
    backup=qa/'pre_patch_effect_aliases'/relative
    if backup.exists(): raise RuntimeError(f'Backup already exists: {relative}')
    backup.parent.mkdir(parents=True,exist_ok=True); backup.write_bytes(original)
    path.write_bytes(repaired)
print(json.dumps({'changed_files':len(prepared),'repaired_keywords':len(records),'numeric_and_identifier_arguments':'unchanged'},indent=2))
