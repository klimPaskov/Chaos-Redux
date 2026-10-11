import sys,json
for l in sys.stdin:
    l=l.rstrip()
    if l.startswith('##') or l.startswith('FINAL'): print(l); continue
    try: d=json.loads(l)
    except Exception: print(l[:200]); continue
    for k,v in d.items():
        if isinstance(v,dict) and any(x in v for x in ('reach_resid_max','before','final')): print(' ',k,{x:y for x,y in v.items() if x not in ('log','seam_log')})
        elif isinstance(v,dict):
            for k2,v2 in v.items():
                if isinstance(v2,dict) and 'final_floor_fixed' in v2: print('   ',k,k2,{x:y for x,y in v2.items() if x!='log'})
