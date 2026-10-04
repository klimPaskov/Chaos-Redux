"""Task-specific source-form checks and declared arithmetic. No engine emulator."""
from pathlib import Path
from decimal import Decimal as D
import re,json,hashlib,difflib,importlib.util
R=Path.cwd();V=R/'docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-04_larder_logistics_implementation/evidence'
manifest=json.loads((V/'source_manifest.json').read_text(encoding='utf-8'));patch=[]
for row in manifest:
 p=R/row['relativePath'];raw=p.read_bytes();row['afterSha256']=hashlib.sha256(raw).hexdigest();(V/'after'/row['relativePath']).write_bytes(raw)
 old=(V/'before'/row['relativePath']).read_bytes();owned=raw
 if row['relativePath']=='common/scripted_effects/chaosx_dynamic_effects.md':
  line=next(x.rstrip('\r\n') for x in raw.decode('utf-8').splitlines(keepends=True) if x.startswith('The Event014 owner API [Larder logistics]'))
  owned=old+b'\r\n'+line.encode('utf-8')+b'\r\n'
  row['ownedAfterSha256']=hashlib.sha256(owned).hexdigest()
  row['concurrentChangesPreserved']=['Independent Event012 recovery/epoch owner API index addition.']
 patch.extend(difflib.unified_diff(old.decode('utf-8-sig').splitlines(keepends=True),owned.decode('utf-8-sig').splitlines(keepends=True),fromfile='before/'+row['relativePath'],tofile='after/'+row['relativePath']))
(V/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8');(V/'owned_source.patch').write_bytes(''.join(patch).encode('utf-8'))
E=(R/'common/scripted_effects/014_cannibalism_effects.txt').read_text(encoding='utf-8-sig');B=(V/'before/common/scripted_effects/014_cannibalism_effects.txt').read_text(encoding='utf-8-sig');T=(R/'common/scripted_triggers/014_cannibalism_triggers.txt').read_text(encoding='utf-8-sig')
def body(s,n):
 m=re.search(r'(?ms)^'+re.escape(n)+r' = \{.*?^\}',s);assert m,n
 return m.group()
checks={}
C=(R/'common/script_constants/014_cannibalism_constants.txt').read_text(encoding='utf-8-sig')
checks['accepted_tuning_and_existing_ceiling_local_bound']=all(re.search(r'(?m)^\t'+k+r' = '+re.escape(v)+r'$',body(C,'cannibalism_larder_logistics')) for k,v in {'capacity_base':'1200','capacity_per_controlled_state':'100','capacity_per_development_point':'50','distance_loss_divisor':'10000','distance_loss_maximum':'0.60'}.items()) and 'global_larder_maximum = 5000' in C and 'larder_max = 2000' in C
checks['fifty_flag_original_score_unchanged']=body(E,'cannibalism_unified_refresh_contract_capacities')==body(B,'cannibalism_unified_refresh_contract_capacities')
checks['exact_static_meta_distance']='distance_to@[DESTINATION]' in E and 'SOURCE = "[cannibalism_larder_source_capital.GetID]"' in E and 'DESTINATION = "[cannibalism_larder_destination_capital.GetID]"' in E
checks['no_composite_distance_target']='distance_to@var:' not in E
checks['old_direct_global_store_clamps_removed']=not re.search(r'clamp_variable = \{[^}]*var = cannibalism_larder\s[^}]*global_larder_maximum',E)
for n in ['cannibalism_create_unified_country_from_selected_host','cannibalism_create_wendigo_unification_from_selected_hosts','cannibalism_absorb_current_warlord_into_unified_host','cannibalism_bargain_current_warlord_autonomy']:
 b=body(E,n);fields=['cannibalism_transfer_distance','cannibalism_transfer_dispatch','cannibalism_transfer_received','cannibalism_transfer_result','cannibalism_transfer_committed','cannibalism_transfer_source_generation','cannibalism_larder_source_capital_captured','cannibalism_larder_destination_capital_captured']
 work=min(x for x in [b.find('cannibalism_validate_spread_queue = yes'),b.find('\n\tif = {')] if x>=0)
 checks[n+'_owns_outputs_first']=all(0<=b.find('set_temp_variable = { '+v+' =')<work for v in fields)
checks['snapshot_capture_unchanged']=body(E,'cannibalism_capture_current_warlord_inheritance')==body(B,'cannibalism_capture_current_warlord_inheritance')
checks['warlord_population_contract_unchanged']=body(E,'cannibalism_apply_warlord_consumption_contracts')==body(B,'cannibalism_apply_warlord_consumption_contracts')
x=body(E,'cannibalism_add_current_warlord_larder_to_unified_host')
checks['single_debit_credit']=x.count('subtract_from_variable = { cannibalism_larder = cannibalism_transfer_dispatch }')==1 and x.count('add_to_variable = { cannibalism_larder = cannibalism_transfer_received }')==1
checks['consume_success_before_debit']=x.index('cannibalism_transfer_result = constant:cannibalism_larder_logistics.zero')<x.index('subtract_from_variable')
checks['identity_has_no_early_larder_mutation']='cannibalism_larder =' not in body(E,'cannibalism_apply_inherited_host_identity_to_cbl')
x=body(E,'cannibalism_bargain_current_warlord_autonomy')
checks['autonomy_explicit_source_no_annex']='puppet = event_target:cannibalism_larder_source_country' in x and 'annex_country' not in x
for n in ['cannibalism_absorb_current_warlord_into_unified_host','cannibalism_absorb_primary_warlord_donor_into_wendigo','cannibalism_create_unified_country_from_selected_host']:
 x=body(E,n);checks[n+'_post_annex_clamp']=x.index('cannibalism_clamp_and_publish_current_larder = yes')>x.index('annex_country = {')
x=body(T,'cannibalism_has_valid_unification_destination')
checks['positive_expected_generation_equality']='global.cannibalism_unification_host_generation > constant:cannibalism_larder_logistics.zero' in x and 'compare = equals' in x
checks['both_human_zero_retained']='set_temp_variable = { cannibalism_inherited_larder = 0 }' in body(E,'cannibalism_create_wendigo_unification_from_selected_hosts')
checks['opening_last_state_provenance']='cannibalism_runtime_migration_source_is_valid = yes' in body(E,'cannibalism_migrate_spread_entries_between_countries') and 'is_owned_and_controlled_by = CBL' in body(T,'cannibalism_runtime_migration_source_is_valid') and body(E,'cannibalism_create_unified_country_from_selected_host').count('cannibalism_initial_cbl_source_validated = constant:cannibalism_larder_logistics.zero')==2
checks['no_profile_recursion']='cannibalism_unified_refresh_operational_profiles' not in body(E,'cannibalism_refresh_larder_effective_capacity') and 'cannibalism_refresh_larder_effective_capacity = yes' in body(E,'cannibalism_unified_refresh_operational_profiles')
checks['mixed_pulse_seed_finalized']=all('cannibalism_clamp_and_publish_current_larder = yes' in body(E,n) for n in ['cannibalism_process_current_actor_pulse','cannibalism_execute_deliberate_foreign_seed'])
L=(R/'localisation/english/014_cannibalism_l_english.yml').read_text(encoding='utf-8-sig');LB=(V/'before/localisation/english/014_cannibalism_l_english.yml').read_text(encoding='utf-8-sig')
checks['only_authorized_tooltips_changed']={l.split(':',1)[0] for l in L.splitlines() if l not in LB.splitlines()}=={'cannibalism.gui.larder.tt','cannibalism.gui.global_larder.tt'}
for k in ['chaosx.nr14.60.d','chaosx.nr14.62.d']:checks[k+'_protected_plain_text']=re.search(r'(?m)^'+re.escape(k)+':.*$',L).group()==re.search(r'(?m)^'+re.escape(k)+':.*$',LB).group()
spec=importlib.util.spec_from_file_location('existing_indentation_checker',R/'.tools/check_structural_indentation.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
structure=[]
for row in manifest[:3]:
 f=row['relativePath'];old=m.measure(V/'before'/f);new=m.measure(R/f);introduced=[x for x in new if x[2].strip() not in [o[2].strip() for o in old]];depth=0
 for n,l in enumerate((R/f).read_text(encoding='utf-8-sig').splitlines(),1):_,depth=m.scan_line(l,depth);assert depth>=0,(f,n)
 assert depth==0,(f,depth)
 structure.append(dict(file=f,introducedFindings=introduced));checks[f+'_scoped_structure']=not introduced
assert all(checks.values()),[k for k,v in checks.items() if not v]
cap=lambda s,k:min(D(5000),D(1200)+D(100)*D(s)+D(50)*D(k))
def later(name,donor,host,states,index,distance,factor,valid=True,migration=True,autonomy=False):
 dispatch=D(str(donor))*D(str(factor)) if valid and migration else D(0);received=dispatch*(1-min(D('.6'),D(distance)/D(10000)));limit=cap(states,index)
 stock=min(limit,D(host)+received) if valid and migration else D(host)
 return dict(id=name,validContext=valid,migrationSucceeded=migration,dispatch=str(dispatch),received=str(received),transitLoss=str(dispatch-received),donorRemainderBeforeAnnexOrSubject=str(D(donor)-dispatch),hostAfter=str(stock),capacity=str(limit),overflowLoss=str(max(D(0),D(host)+received-limit)) if valid and migration else '0',territory='actual recipient controlled states, no donor projection',autonomy=autonomy)
rows=[later('locality_submission',1000,300,1,0,0,.85),later('regional_submission',1000,1000,5,10,1000,.85),later('distant_surrender',2000,2500,20,20,3000,.65),later('remote_autonomy',1000,4800,40,40,6000,.20,autonomy=True),dict(id='cap_loss',stockBefore='3000',statesAfterLoss=1,index=0,capacity=str(cap(1,0)),stockAfter='1300',lost='1700',boundary='next existing actor pulse or operation finalization'),dict(id='both_human_preservation',donorBefore='1000',donorAfter='1000',donorTransfer='0',snapshot='0 retained',host='original zero-snapshot bootstrap and route bonuses, own territory only'),dict(id='insufficient_larder_terminal_gate',stores=800,lockReserve800=True,reserveAfterCost400=False,strictBonusAbove1200=False),later('stale_generation_no_transfer',1000,300,1,0,3000,.85,valid=False),dict(id='opening_post_annex_capacity',donorStore='2000',bootstrap='300',managedBonus='100',temporaryRecipientStates=1,actualPostAnnexStates=12,index=0,capacity=str(cap(12,0)),stockAfter='2400',prematureClampDiscardPrevented='1100'),dict(id='opening_one_state_source_provenance',sourceLiveBeforeQuote=True,sourceLiveAfterCapitalTransfer=False,positiveValidatedQuote=True,actualFrozenCapitalOwnedAndControlledByCBL=True,positiveRecipientGeneration=True,allowedOpeningProvenance=True,statesAfterAnnex=1,donorStore='1000',stockAfter='1300'),later('failed_migration_no_commit',1000,300,1,0,1000,.85,migration=False),dict(id='missing_capital_or_unwritten_distance',quoteResult=0,dispatch=0,received=0,annex=False,subject=False),dict(id='reserve_strict_bonus_boundaries',capacity=str(cap(1,0)),points=[dict(stores=n,reserve1200=n>=1200,bonusAbove1200=n>1200) for n in [1199,1200,1201,1300]]),dict(id='ceiling_saturation',states=38,index=0,capacity=str(cap(38,0)),veryLargeCapacity=str(cap(100,250)),ordinaryCap='2000'),dict(id='repeated_quote_commit',firstCommit='consumes result before debit',secondDispatch='0',secondReceived='0')]
(V/'source_validation_and_math_receipts.json').write_text(json.dumps(dict(authority='Task-specific source assertions and declared arithmetic, not engine execution or AI probability acceptance.',sourceChecks=checks,structuralChecker=structure,scenarios=rows,comparisonFixtureIds=[r['id'] for r in rows[:8]],limitations=['Probability compare remains auditor/parent-owned.','Existing native constructor tag/leader/capital preparation has no engine rollback proof.','Native GetID/distance/annex behavior unobserved.','Eight frozen auditor fixtures contain unbound inputs, preserved rather than silently filled.']),indent=2)+'\n',encoding='utf-8')
print('Quote ownership, one-shot debit/receipt, post-annex placement, generation proof, both-human zero and last-state provenance source checks passed.')
print('15 declared source-arithmetic scenarios retained with the eight comparison IDs. No engine or AI acceptance claim.')
