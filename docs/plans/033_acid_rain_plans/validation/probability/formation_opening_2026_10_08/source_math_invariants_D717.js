// Read-only frozen-source equality checks, not a Clausewitz or native replay.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = __dirname;
const sha = x => crypto.createHash('sha256').update(x).digest('hex');
const read = (role, logical) => fs.readFileSync(path.join(root, role, logical));
function end(text, open) {
  let depth=0, quoted=false, escape=false, comment=false;
  for(let i=open;i<text.length;i++) {
    const c=text[i];
    if(comment){if(c==='\n')comment=false;continue;}
    if(quoted){if(!escape&&c==='"')quoted=false;escape=!escape&&c==='\\';continue;}
    if(c==='#'){comment=true;continue;}
    if(c==='"'){quoted=true;continue;}
    if(c==='{')depth++;
    if(c==='}'&&--depth===0)return i+1;
  }
  throw Error('Unclosed source block');
}
function helper(text,id){const start=text.indexOf('\n'+id+' = {');if(start<0)throw Error('Missing helper '+id);const open=text.indexOf('{',start);return text.slice(start+1,end(text,open));}
function randomArgs(text){return [...text.matchAll(/\bset_(?:temp_)?variable_to_random\s*=\s*\{/g)].map(m=>text.slice(m.index,end(text,text.indexOf('{',m.index))).replace(/\s+/g,' '));}
function footprintMath(text){const h=helper(text,'acid_rain_commit_front_region');const start=h.indexOf('set_temp_variable_to_random = {');const finish=h.indexOf('set_variable = { global.acid_rain_front_active_state_count_entries^');if(start<0||finish<0)throw Error('Footprint math segment missing');return h.slice(start,finish);}
const before=read('before-source','common/scripted_effects/033_acid_rain_effects.txt');
const after=read('after_d717bf91','common/scripted_effects/033_acid_rain_effects.txt');
const a=before.toString('utf8'),b=after.toString('utf8');
const names=['acid_rain_compute_region_candidate_weight','acid_rain_select_weighted_region','acid_rain_calculate_front_goal','acid_rain_initialize_front_visit_timing','acid_rain_activate_front','acid_rain_process_front','acid_rain_touch_state_for_front','acid_rain_prepare_front_warning','acid_rain_execute_front_move','acid_rain_retire_front_footprint_states','acid_rain_pulse_front_states'];
const helpers=names.map(name=>{const x=helper(a,name),y=helper(b,name);return {name,beforeSha256:sha(x),afterSha256:sha(y),exactEqual:x===y};});
const oldMath=footprintMath(a),newMath=footprintMath(b);
const c1=read('before-source','common/script_constants/033_acid_rain_constants.txt'),c2=read('after_d717bf91','common/script_constants/033_acid_rain_constants.txt');
const e1=read('before-source','events/033_acid_rain.txt'),e2=read('after_d717bf91','events/033_acid_rain.txt');
const result={scope:'Authored source math/body equality only. Actual draw order/admission/first-entry timing intentionally change and are NOT invariant.',runtime:{beforeSha256:sha(before),afterSha256:sha(after)},constants:{beforeSha256:sha(c1),afterSha256:sha(c2),exactEqual:c1.equals(c2)},rootEvents:{beforeSha256:sha(e1),afterSha256:sha(e2),exactEqual:e1.equals(e2)},helpers,firstFootprintMath:{beforeSha256:sha(oldMath),afterSha256:sha(newMath),exactEqual:oldMath===newMath},randomCommandArguments:{before:randomArgs(a).length,after:randomArgs(b).length,textualCommandArgumentsEqual:JSON.stringify(randomArgs(a))===JSON.stringify(randomArgs(b)),executedDrawOrderingEqualClaim:false},nativeFrameReplay:false};
if(!result.constants.exactEqual||!result.rootEvents.exactEqual||!helpers.every(x=>x.exactEqual)||!result.firstFootprintMath.exactEqual||!result.randomCommandArguments.textualCommandArgumentsEqual)throw Error(JSON.stringify(result));
console.log(JSON.stringify(result,null,2));
