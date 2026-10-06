import {execFileSync} from 'node:child_process';
import {writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const repo='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const evidence=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/takeover_2026-10-06';
const files=['common/scripted_triggers/camp_administration_occupation_triggers.txt','common/scripted_triggers/camp_administration_country_triggers.txt','common/decisions/camp_administration_country_decisions.txt'];
const rows=[];
for(const path of files){const bytes=execFileSync('git',['show','HEAD:'+path],{cwd:repo,encoding:null});const out=evidence+'/HEAD__'+path.replaceAll('/','__');await writeFile(out,bytes);rows.push({sourcePath:path,snapshotPath:out,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex')});}
const head=execFileSync('git',['rev-parse','HEAD'],{cwd:repo,encoding:'utf8'}).trim();
console.log(JSON.stringify({head,files:rows}));
