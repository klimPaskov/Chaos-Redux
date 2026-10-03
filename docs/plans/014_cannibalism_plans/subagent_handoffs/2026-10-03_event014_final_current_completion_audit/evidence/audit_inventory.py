"""Read-only lexical inventory; writes only this audit evidence directory.
Not an engine parser, gameplay test, visual approval, or probability analysis.
"""
from pathlib import Path
import re, json, hashlib, datetime, subprocess, zipfile, xml.etree.ElementTree as ET
ROOT = Path.cwd()
GAME = Path(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV')
OUT = ROOT / 'docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_final_current_completion_audit/evidence'
def read(p): return Path(p).read_text(encoding='utf-8-sig')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def blocks(s):
    # Preserve character offsets while excluding quoted values and comments.
    clean = re.sub(r'"(?:\\.|[^"\\])*"|#[^\n]*', lambda m:' ' * len(m.group()), s)
    stack=[]; result=[]
    for m in re.finditer(r'([\w.@:]+)\s*=\s*\{|[{}]',clean):
        if m.group().endswith('{'):
            n={'key':m.group(1), 'start':m.start(), 'open':m.end()-1, 'depth':len(stack), 'parent':stack[-1]['start'] if stack else None}
            stack.append(n)
        elif m.group()=='{': stack.append({'key':'<bare>','start':m.start(),'open':m.start(),'depth':len(stack),'parent':stack[-1]['start'] if stack else None})
        elif stack:
            n=stack.pop(); n['end']=m.end(); n['line']=s.count('\n',0,n['start'])+1; n['endLine']=s.count('\n',0,n['end'])+1; result.append(n)
    return sorted(result,key=lambda n:n['start'])
def ident(s,n,key='id'):
    m=re.search(r'\b'+re.escape(key)+r'\s*=\s*("[^"]*"|[^\s{}#]+)',s[n['open']+1:n['end']]); return m.group(1).strip('"') if m else None
def brief(s,n): return {'key':n['key'],'id':ident(s,n),'line':n['line'],'endLine':n['endLine']}
paths=[]
for base in ['events','common','interface','gfx/entities','history/countries','common/countries','docs/specs/014_cannibalism_specs','docs/plans/014_cannibalism_plans/subagent_handoffs']:
    for p in (ROOT/base).rglob('*'):
        if p.is_file() and p.suffix in ['.txt','.md','.yml','.gui','.gfx','.asset','.json'] and ('014_cannibalism' in str(p.relative_to(ROOT)) or re.search(r'[/\\](CB[A-HL])\s',str(p))):
            if OUT not in p.parents: paths.append(p)
files={str(p.relative_to(ROOT)).replace('\\','/'):{'sha256':sha(p),'bytes':p.stat().st_size,'lines':len(read(p).splitlines())} for p in paths}
loc={}; dup=[]
for p in (ROOT/'localisation/english').rglob('*.yml'):
    for i,line in enumerate(read(p).splitlines(),1):
        m=re.match(r'^\s*([\w.]+):(?:\d+)?\s*"',line)
        if m:
            if m.group(1) in loc and ('cannibal' in m.group(1) or 'nr14' in m.group(1)): dup.append(m.group(1))
            loc[m.group(1)]={'path':str(p.relative_to(ROOT)).replace('\\','/'),'line':i}
sprites={}; textures=[]
for p in (ROOT/'interface').rglob('*.gfx'):
    s=read(p)
    for n in blocks(s):
        if n['key'] not in ['spriteType','frameAnimatedSpriteType']: continue
        name=ident(s,n,'name'); tex=ident(s,n,'texturefile')
        if name: sprites[name]={'path':str(p.relative_to(ROOT)).replace('\\','/'),'line':n['line'],'texture':tex}
        if tex and ('014_cannibalism' in tex or (name and 'cannibal' in name.lower())):
            q=ROOT/tex
            if not q.exists(): q=GAME/tex
            textures.append({'sprite':name,'texture':tex,'resolvedPath':str(q),'exists':q.exists(),'sha256':sha(q) if q.exists() else None})
focusPath='common/national_focus/014_cannibalism_focus.txt'; s=read(ROOT/focusPath); bs=blocks(s)
trees=[]; foci=[]
for tree in [n for n in bs if n['key']=='focus_tree']:
    fs=[n for n in bs if n['key']=='focus' and n['parent']==tree['start']]
    trees.append({**brief(s,tree),'focusCount':len(fs)})
    for f in fs:
        fid=ident(s,f); body=s[f['start']:f['end']]
        icon=ident(s,f,'icon'); prereqs=re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*(\w+)',body)
        foci.append({**brief(s,f),'tree':ident(s,tree),'icon':icon,'localised':fid in loc and fid+'_desc' in loc,'registeredIcon':icon in sprites if icon and icon.startswith('GFX_') else None,'prerequisites':prereqs,'hasReward':bool(re.search(r'completion_reward\s*=\s*\{',body)),'hasAI':bool(re.search(r'ai_will_do\s*=\s*\{',body))})
decPath='common/decisions/014_cannibalism_decisions.txt'; s=read(ROOT/decPath); bs=blocks(s); decisions=[]
for cat in [n for n in bs if n['depth']==0]:
    for n in [x for x in bs if x['parent']==cat['start']]:
        body=s[n['start']:n['end']]
        decisions.append({**brief(s,n),'category':cat['key'],'mission':bool(re.search(r'\bdays_mission_timeout\s*=',body)),'tracker': 'achievement_tracker' in cat['key'],'localised':n['key'] in loc and n['key']+'_desc' in loc,'AI':bool(re.search(r'\bai_will_do\s*=',body)),'lifecycleKeys':sorted(set(re.findall(r'\b([\w]*(?:effect|trigger|timeout|complete)[\w]*)\s*=',body)))})
s=read(ROOT/'common/units/014_cannibalism_irregular_infantry.txt'); units=[]
for n in blocks(s):
    if n['key'].startswith('cannibal_') and n['depth']==1: units.append({**brief(s,n),'sprite':ident(s,n,'sprite'),'localised':n['key'] in loc})
s=read(ROOT/'events/014_cannibalism.txt'); events=[]
for n in blocks(s):
    if n['depth']==0 and n['key'].endswith('_event'): events.append(brief(s,n))
s=read(ROOT/'common/achievements/chaos_redux_achievements.txt')
achievements=[brief(s,n) for n in blocks(s) if n['depth']==0 and n['key'].startswith('014_cannibalism_')]
literalDefs=set(); helperCalls=set()
for base in ['common','events']:
    for p in (ROOT/base).rglob('*.txt'):
        text=read(p); literalDefs.update(re.findall(r'^([\w]+)\s*=\s*\{',text,re.M))
        if '014_cannibalism' in p.name: helperCalls.update(re.findall(r'\b(cannibalism_\w+)\s*=\s*(?:yes|no)\b',re.sub(r'#[^\n]*','',text)))
portraitAliases=[dict(name=k,**v) for k,v in sprites.items() if re.match(r'GFX_portrait_CB[A-H]_warlord',k)]
modelLedger=json.loads(read(ROOT/'docs/assets/014_cannibalism/models_3d/family_jobs.json'))
workbook=ROOT/'docs/spreadsheets/chaos_redux_events_catalog.xlsx'; catalog={}
try:
    import openpyxl
    w=openpyxl.load_workbook(workbook,read_only=True,data_only=False)
    for sheet,cell in [('Events','A15:N15'),('Scenarios','A10:F10')]:
        catalog[sheet]=[[x.value for x in row] for row in w[sheet][cell]]
    catalog['EventsHeaders']=[[x.coordinate,x.value] for x in w['Events'][1]]
    catalog['StatusCells']={k:w[sn][c].value for k,sn,c in [('EventsM15','Events','M15'),('EventsN15','Events','N15'),('ScenariosF10','Scenarios','F10')]}
    w.close()
except Exception as e: catalog={'readError':str(e)}
result={'timestampUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'limits':'Lexical presence/crosswalk only; no engine, balance, visual or live claim. Shared tree changes may continue after this snapshot.','files':files,'focusTrees':trees,'foci':foci,'focusMissingLocalisation':[x for x in foci if not x['localised']],'focusMissingIcons':[x for x in foci if x['registeredIcon'] is False],'decisions':decisions,'units':units,'events':events,'achievements':achievements,'undefinedLiteralHelpers':sorted(helperCalls-literalDefs),'duplicateLocalisationKeys':sorted(set(dup)),'textureReferences':textures,'missingTextures':[x for x in textures if not x['exists']],'portraitAliases':portraitAliases,'portraitUniqueTextureCount':len(set(x['texture'] for x in portraitAliases)),'modelLedger':modelLedger,'catalogReadOnly':catalog,'workbookSha256':sha(workbook),'gitHead':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()}
(OUT/'current_inventory.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'focusTrees':trees,'decisions':len(decisions),'missions':[x['key'] for x in decisions if x['mission']],'trackerEntries':sum(x['tracker'] for x in decisions),'units':units,'events':len(events),'achievements':len(achievements),'undefinedLiteralHelpers':result['undefinedLiteralHelpers'],'missingTextures':result['missingTextures'],'focusMissingLocalisation':result['focusMissingLocalisation'],'focusMissingIcons':result['focusMissingIcons'],'portraitAliases':len(portraitAliases),'portraitTextures':result['portraitUniqueTextureCount'],'catalog':catalog},indent=2,ensure_ascii=False))
