import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {existsSync} from 'node:fs';
import {writeFile} from 'node:fs/promises';
const repo='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const evidence=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/takeover_2026-10-06';
const path='common/scripted_triggers/camp_administration_occupation_triggers.txt';
const target='22ef0a87f816de698c5d11d9368a5dccb4ff9148e67f2e781f38c30ffc9f5e6e';
const commits=execFileSync('git',['log','--all','--format=%H','--',path],{cwd:repo,encoding:'utf8'}).trim().split(/\r?\n/).filter(Boolean);
const matches=[],tested=[];
for(const commit of commits){try{const bytes=execFileSync('git',['show',commit+':'+path],{cwd:repo,encoding:null});const sha=createHash('sha256').update(bytes).digest('hex');tested.push({commit,sha,bytes:bytes.length});if(sha===target){const out=evidence+'/recovered__'+path.replaceAll('/','__');await writeFile(out,bytes);matches.push({commit,sha,snapshotPath:out,bytes:bytes.length});}}catch{}}
const record={targetHash:target,commitsTested:tested.length,matches,tested};
await writeFile(evidence+'/occupation_trigger_baseline_recovery.json',JSON.stringify(record,null,2));
console.log(JSON.stringify({targetHash:target,commitsTested:tested.length,matches}));
