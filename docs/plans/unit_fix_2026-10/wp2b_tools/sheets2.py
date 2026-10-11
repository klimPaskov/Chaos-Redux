"""python sheets2.py <job> <blend|-> <tag> <body_diffuse> <items name:tex ...> -- role:f1,f2,... [--views front,right] [--size 9] [--center 0,0,3.6]
Renders contact sheets (rows = views, columns = frames) through the Lab preview2 script. blend '-' uses the open scene."""
import sys, json, subprocess, os
a=sys.argv[1:]; job,blend,tag,body=a[0],a[1],a[2],a[3]
rest=a[4:]; i=rest.index('--'); items=rest[:i]; roles=[r for r in rest[i+1:] if not r.startswith('--')]
opts=rest[i+1:]
views=['front','right']; size=9.0; center=[0,0,3.6]
for k,o in enumerate(opts):
    if o=='--views': views=opts[k+1].split(',')
    if o=='--size': size=float(opts[k+1])
    if o=='--center': center=[float(x) for x in opts[k+2-1].split(',')]
roles=[r for r in roles if ':' in r]
tex={'char1.001':body}
for it in items:
    n,t=it.split(':',1); tex['ITEM_'+n]=t
port=os.environ.get('LABPORT','9877')
for spec in roles:
    role,frames=spec.split(':'); frames=[int(x) for x in frames.split(',')]
    shots=[{'action':f'{job}_{role}','frame':f,'view':v,'center':center,'size':size} for v in views for f in frames]
    cfg={'job':job,'tex':tex,'shots':shots,'out':f'.tmp/wp2b/pv/{tag}_{role}.png','cols':len(frames),'res':[300,375]}
    if blend=='-': cfg['open']=False
    else: cfg['blend']=blend
    code=f"CFG={json.dumps(cfg)}\nimport json\n"
    sys.path.insert(0,r"<mod root>/.tmp/wp2b")
    import lab
    r=lab.run("import json\nCFG=json.loads(%r)\n"%json.dumps(cfg)+open(r"<mod root>/.tmp/wp2b/preview2.py",encoding='utf-8').read())
    print(role, r.get('status'), r.get('message','')[:300] if r.get('status')!='ok' else '')
    blend='-'
    cfg['open']=False
