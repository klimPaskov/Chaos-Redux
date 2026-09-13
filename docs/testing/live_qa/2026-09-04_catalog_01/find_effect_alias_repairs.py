from pathlib import Path
import re, json, collections
root=Path.cwd()
qa=root/'docs/testing/live_qa/2026-09-04_catalog_01'
aliases={'clear_country_flag':'clr_country_flag','clear_global_flag':'clr_global_flag','add_army_experience':'army_experience','remove_idea':'remove_ideas','add_idea':'add_ideas'}
records={}
for match in re.finditer(r"Invalid effect '([^']+)' in (\S+) line : (\d+)", (qa/'logs/launch_07/logs/error.log').read_text(encoding='utf-8-sig')):
    old,path,line=match.groups(); line=int(line)
    if old not in aliases or not path.startswith('common/scripted_effects/') or path.startswith('common/scripted_effects/023_'): continue
    text=(root/path).read_text(encoding='utf-8-sig').splitlines()
    actual=text[line-1] if line<=len(text) else ''
    if re.search(r'(?<!\w)'+re.escape(old)+r'\s*=',actual): records[(path,line,old)]={'path':path,'line':line,'old':old,'new':aliases[old],'source':actual}
result=list(records.values())
(qa/'effect_alias_candidates.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'changes':len(result),'files':dict(collections.Counter(r['path'] for r in result)),'aliases':dict(collections.Counter(r['old'] for r in result))},indent=2))
