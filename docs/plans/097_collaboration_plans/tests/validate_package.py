"""Check the delivered documentation package. This does not validate HOI4 code."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[4]
SPECS=ROOT/'docs/specs/097_collaboration_specs'
PLANS=ROOT/'docs/plans/097_collaboration_plans'

def main() -> None:
    failures=[]
    checks={}
    parts=sorted(SPECS.glob('*spec_part_*.md'),key=lambda p:int(re.search(r'part_(\d+)_',p.name).group(1)))
    checks['numbered_parts']=[int(re.search(r'part_(\d+)_',p.name).group(1)) for p in parts]
    if checks['numbered_parts'] != list(range(1,11)):
        failures.append('Expected exactly parts 1 through 10.')
    checks['numbered_part_words']=sum(len(p.read_text(encoding='utf-8').split()) for p in parts)
    goal=(SPECS/'097_collaboration_goal_prompt.md').read_text(encoding='utf-8')
    checks['goal_characters_including_final_newline']=len(goal)
    if not 3500 <= len(goal) <= 4000:
        failures.append('Goal prompt must be 3500-4000 characters.')
    for name in ['coding','asset','achievement','goal']:
        if not (SPECS/f'097_collaboration_{name}_prompt.md').is_file():
            failures.append(f'Missing {name} prompt.')
    missing_links=[]
    for p in ROOT.rglob('*.md'):
        text=p.read_text(encoding='utf-8')
        for raw in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',text):
            dest=raw.split('#')[0]
            if not dest or '://' in dest or dest.startswith('mailto:'):
                continue
            target=(p.parent/unquote(dest)).resolve()
            if not target.exists(): missing_links.append({'from':str(p.relative_to(ROOT)),'link':raw})
    checks['broken_local_markdown_links']=missing_links
    if missing_links: failures.append('Broken local Markdown links.')
    style=[]
    for p in parts:
        t=p.read_text(encoding='utf-8')
        if '\u2014' in t:style.append(f'{p.name}: em dash')
        if ';' in t:style.append(f'{p.name}: semicolon')
        if len(t.split()) < 800:style.append(f'{p.name}: suspiciously short part')
    checks['spec_style_flags']=style
    if style: failures.append('Specification style or length issue.')
    sources=json.loads((PLANS/'097_collaboration_source_manifest.json').read_text())
    ranges=json.loads((PLANS/'097_collaboration_read_coverage.json').read_text())
    checks['supplied_text_files']=len(sources)
    checks['subagent_profiles_read']=sum(x['path'].startswith('subagents/') for x in sources)
    checks['recorded_read_chunks']=len(ranges)
    gaps=[]
    for source in sources:
        covered=set()
        for c in ranges:
            if c['path']==source['path']:
                covered.update(range(c['start'],c['end']+1))
        if covered != set(range(1,source['lines']+1)):
            gaps.append(source['path'])
    checks['recorded_line_coverage_gaps']=gaps
    if len(sources)!=46 or len(ranges)!=104 or gaps:
        failures.append('Source-reading manifest or range coverage mismatch.')
    assets=json.loads((PLANS/'097_collaboration_planned_asset_manifest.json').read_text())
    checks['planned_runtime_images']=len(assets)
    checks['asset_statuses']=sorted({a['status'] for a in assets})
    if len(assets)!=23 or any(a['status']!='planned, not produced' for a in assets):
        failures.append('Planned asset count or status mismatch.')
    ids=set(re.findall(r'\*\*Identifier:\*\* `(chaosx_097_[^`]+)`',(SPECS/'097_collaboration_spec_part_9_achievements.md').read_text()))
    checks['achievement_ids']=sorted(ids)
    if len(ids)!=6:failures.append('Expected six unique achievement IDs.')
    for aid in ids:
        paths={a['path'] for a in assets if a['consumer']==aid}
        expected={f'gfx/achievements/{aid}{variant}.dds' for variant in ['','_grey','_not_eligible']}
        if paths != expected:failures.append(f'Achievement triplet mismatch: {aid}')
    prompt=(SPECS/'097_collaboration_achievement_prompt.md').read_text()
    copied=prompt.split('## Full achievement design\n\n',1)[1]
    if copied!=(SPECS/'097_collaboration_spec_part_9_achievements.md').read_text():
        failures.append('Achievement prompt reproduction is out of sync.')
    checks['prepared_relevant_subagent_handoffs']=len(list((PLANS/'handoffs').glob('*.md')))
    execution=(PLANS/'097_collaboration_subagent_execution_map.md').read_text()
    for source in sources:
        if source['path'].startswith('subagents/'):
            if f'`{Path(source["path"]).stem}`' not in execution:
                failures.append(f'Unaccounted supplied role: {source["path"]}')
    for p in (PLANS/'handoffs').glob('*.md'):
        t=p.read_text()
        if 'Prepared, not executed.' not in t or 'fork_turns="none"' not in t:
            failures.append(f'Agent status or isolation omitted: {p.name}')
    checks['gameplay_or_produced_asset_files']=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
        if p.is_file() and p.suffix.lower() in {'.dds','.png','.gfx','.gui','.yml','.asset','.mesh','.anim'}]
    if checks['gameplay_or_produced_asset_files']:
        failures.append('Unexpected gameplay or produced asset files.')
    model=json.loads((PLANS/'tests/model_results.json').read_text())
    checks['model_tests_passed']=model['tests_run'] if model['successful'] else 0
    if not model['successful'] or model['tests_run']!=44:
        failures.append('Reference model result not passing or wrong count.')
    if model['native_engine_validation'] or model['independent_subagent_review']:
        failures.append('Model evidence overclaims execution.')
    for p in ROOT.rglob('*.json'):
        json.loads(p.read_text(encoding='utf-8'))
    for p in ROOT.rglob('*.py'):
        compile(p.read_text(encoding='utf-8'),str(p),'exec')
    result={'scope':'Documentation package consistency only',
            'successful':not failures,'failures':failures,'checks':checks,
            'native_engine_validation':False,'independent_agent_execution':False}
    out=PLANS/'097_collaboration_package_validation.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if failures:raise SystemExit(1)

if __name__=='__main__':main()
