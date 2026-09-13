from pathlib import Path
import re,json
root=Path.cwd()
art=root/'docs/testing/live_qa/20260913_main_menu_startup'
manifest=json.loads((art/'camp_parameter_contract.json').read_text())
def block(t,n):
 m=re.search(r'(?m)^'+re.escape(n)+r'\s*=\s*\{',t); assert m,n
 d=1;i=m.end()
 while d:
  d+=(t[i]=='{')-(t[i]=='}');i+=1
 return t[m.start():i]
def nested(t):
 for v in manifest['specializations']:
  name=v['original']
  def replace(m):
   args=dict(re.findall(r'([A-Z_]+)\s*=\s*([^\s{}]+)',m[1]))
   return v['helper']+' = yes' if args==v['args'] else m[0]
  t=re.sub(re.escape(name)+r'\s*=\s*\{([^{}]*)\}',replace,t)
 return t
checks=[]
for v in manifest['specializations']:
 for f in manifest['files']:
  p=Path(f['file']); old=(art/'baseline/camp'/p).read_text(encoding='utf-8-sig')
  if not re.search(r'(?m)^'+v['original']+r'\s*=',old):continue
  expected=block(old,v['original']).replace(v['original']+' =',v['helper']+' =',1)
  for k,x in v['args'].items():expected=expected.replace('$'+k+'$',x)
  expected=nested(expected)
  actual=block((root/p).read_text(encoding='utf-8-sig'),v['helper'])
  assert actual==expected,v['helper']
  checks.append(v['helper'])
call_checks=[]
for c in manifest['numeric_calls']:
 text=(root/c['file']).read_text(encoding='utf-8-sig')
 expected='set_temp_variable = { '+c['input']+' = '+c['value']+' } '+c['helper']+' = yes'
 assert expected in text,c
 call_checks.append(c)
result={'specialization_body_equivalence':checks,'numeric_call_contracts_verified':len(call_checks),'limits':'Source equivalence of intended literal substitution, not engine execution or balance simulation.'}
(art/'camp_parameter_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
