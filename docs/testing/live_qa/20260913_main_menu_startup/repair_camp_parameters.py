from pathlib import Path
import re, shutil, json, hashlib

root = Path.cwd()
artifact = root / 'docs/testing/live_qa/20260913_main_menu_startup'
files = list((root/'common/scripted_effects').glob('camp*.txt')) + list((root/'common/scripted_triggers').glob('camp*.txt'))
source = {p: p.read_text(encoding='utf-8-sig') for p in files}
texts = source.copy()
proof = {'specializations': [], 'numeric_calls': [], 'files': []}

def block(text, name):
    m = re.search(r'(?m)^'+re.escape(name)+r'\s*=\s*\{', text)
    assert m, name
    depth=1; i=m.end()
    while depth:
        if text[i]=='{': depth+=1
        if text[i]=='}': depth-=1
        i+=1
    return m.start(),i,text[m.start():i]

# Numeric arguments retain one implementation and are initialized immediately at every call.
numeric = {
    'camp_admin_country_start_program': ('PROGRAM', 'camp_admin_start_program_input', '$PROGRAM$'),
    'camp_admin_integration_record_site_history': ('KIND', 'camp_admin_history_kind_input', '$KIND$'),
    'camp_occ_seed_origin': ('ORIGIN', 'camp_occ_origin_ceiling_input_k', 'constant:camp_occ_origin_k.$ORIGIN$'),
}
for name,(arg,var,token) in numeric.items():
    pat=re.compile(re.escape(name)+r'\s*=\s*\{\s*'+arg+r'\s*=\s*([^\s{}]+)\s*\}')
    for p,t in list(texts.items()):
        def sub(m):
            value=m[1] if arg!='ORIGIN' else 'constant:camp_occ_origin_k.'+m[1]
            proof['numeric_calls'].append({'file':str(p.relative_to(root)), 'helper':name,'input':var,'value':value})
            return f'set_temp_variable = {{ {var} = {value} }} {name} = yes'
        t=pat.sub(sub,t)
        if re.search(r'(?m)^'+name+r'\s*=',t):
            a,z,b=block(t,name)
            t=t[:a]+b.replace(token,var)+t[z:]
        texts[p]=t

# Literal keys must remain static. Each variant is an exact expansion of its original body.
names=['camp_admin_initialize_cause_records','camp_admin_record_cause','camp_admin_country_apportion_census','camp_admin_country_admit_census_host','camp_admin_country_award_program']
variants={}
for name in names:
    owner=next(p for p,t in texts.items() if re.search(r'(?m)^'+name+r'\s*=',t))
    _,_,body=block(texts[owner],name)
    params=set(re.findall(r'\$([A-Z_]+)\$',body))
    calls=[]
    pat=re.compile(re.escape(name)+r'\s*=\s*\{([^{}]*)\}')
    for p,t in texts.items():
        for m in pat.finditer(t):
            args=dict(re.findall(r'([A-Z_]+)\s*=\s*([^\s{}]+)',m[1]))
            if args and not any('$' in v for v in args.values()): calls.append(args)
    if name=='camp_admin_country_admit_census_host': calls=[v[1] for v in variants['camp_admin_country_apportion_census']]
    unique=[]
    for args in calls:
        assert params<=args.keys(),(name,params,args)
        if args not in unique: unique.append(args)
    variants[name]=[(name+'_'+args.get('GROUP',args.get('CAUSE',args.get('PROGRAM',''))),args) for args in unique]
    expanded=[]
    for new,args in variants[name]:
        b=body.replace(name+' =',new+' =',1)
        for k,v in args.items(): b=b.replace('$'+k+'$',v)
        assert '$' not in b,(new,b)
        expanded.append(b)
        proof['specializations'].append({'original':name,'helper':new,'args':args,'body_sha256':hashlib.sha256(b.encode()).hexdigest()})
    a,z,_=block(texts[owner],name)
    texts[owner]=texts[owner][:a]+'\n\n'.join(expanded)+texts[owner][z:]

for name,vs in variants.items():
    pat=re.compile(re.escape(name)+r'\s*=\s*\{([^{}]*)\}')
    for p,t in list(texts.items()):
        def sub(m):
            args=dict(re.findall(r'([A-Z_]+)\s*=\s*([^\s{}]+)',m[1]))
            assert args,(name,m[0])
            new=next(n for n,a in vs if a==args)
            return new+' = yes'
        texts[p]=pat.sub(sub,t)

for p,t in list(texts.items()):
    if p.parent.name=='scripted_triggers': t=re.sub(r'(?<![\w])political_power(?=\s*[><=])','has_political_power',t)
    assert not re.search(r'\$[A-Z_]+\$',t),p
    if t==source[p]: continue
    backup=artifact/'baseline/camp'/p.relative_to(root)
    backup.parent.mkdir(parents=True,exist_ok=True)
    assert not backup.exists(),backup
    shutil.copy2(p,backup)
    before=p.read_bytes()
    bom=before.startswith(b'\xef\xbb\xbf')
    newline='\r\n' if b'\r\n' in before else '\n'
    after=t.replace('\n',newline).encode('utf-8')
    if bom: after=b'\xef\xbb\xbf'+after
    p.write_bytes(after)
    proof['files'].append({'file':str(p.relative_to(root)),'before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(after).hexdigest()})
(artifact/'camp_parameter_contract.json').write_text(json.dumps(proof,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'files':len(proof['files']),'specializations':len(proof['specializations']),'numeric_calls':len(proof['numeric_calls'])}))
