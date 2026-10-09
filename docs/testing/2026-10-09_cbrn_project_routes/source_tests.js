// Bounded production-AST tests. Run: node docs/testing/2026-10-09_cbrn_project_routes/source_tests.js
// Reuses VM.run unchanged, including conservative helper temporary cleanup.
// Native inputs and complex owner calls are explicit boundaries, not engine proof.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');
const assert = require('node:assert/strict');
const base = require('../../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const { VM, ticks, parse, root, definitions, constants } = base;
const vmRun = VM.prototype.run;
const sources = [
  'common/scripted_effects/cbrn_special_project_effects.txt',
  'common/scripted_triggers/cbrn_special_project_triggers.txt',
  'common/scripted_effects/016_conventional_technology_api_effects.txt',
  'common/scripted_triggers/016_conventional_technology_api_triggers.txt',
  'common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt',
  'common/scripted_triggers/016_brilliant_scientist_triggers.txt',
];
const tuning = [
  'common/script_constants/cbrn_special_project_constants.txt',
  'common/script_constants/016_brilliant_scientist_constants.txt',
  'common/script_constants/016_brilliant_scientist_custom_technology_constants.txt',
];
for (const file of sources) for (const n of parse(fs.readFileSync(path.join(root, file), 'utf8'))) definitions.set(n.key, n.value);
function walkConstants(nodes, prefix = []) {
  for (const n of nodes) {
    if (n.key === 'schema') continue;
    if (Array.isArray(n.value)) walkConstants(n.value, [...prefix, n.key]);
    else if (/^-?\d+(\.\d+)?$/.test(n.value)) constants.set(`constant:${[...prefix, n.key].join('.')}`, ticks(n.value));
  }
}
for (const file of tuning) walkConstants(parse(fs.readFileSync(path.join(root, file), 'utf8')));
const boundaryCalls = new Set(['brilliant_scientist_record_new_project_prototype', 'chaosx_grant_custom_operational_technology']);
class ProjectVM extends VM {
  constructor() {
    super(); this.tech = new Set(); this.completed = new Set(); this.dlc = new Set(); this.characters = new Set();
    this.ideas = new Set(); this.modifiers = new Set(); this.ideaAdds = []; this.modifierAdds = []; this.technologyWrites = [];
    this.trace = []; this.ownerCalls = []; this.extremePolicy = false; this.validMengele = false; this.nativeRefreshes = 0;
  }
  run(name, allow = false) {
    this.trace.push(name);
    if (name === 'cbrn_policy_allows_extreme_use') return this.extremePolicy;
    if (name === 'brilliant_scientist_mengele_project_stage_provider_is_valid') return this.validMengele;
    if (boundaryCalls.has(name)) {
      this.ownerCalls.push({ name, storyFamily: String(this.value('brilliant_scientist_project_family')), customFamily: String(this.value('chaosx_custom_technology_family')), source: String(this.value('chaosx_custom_technology_source')) });
      return true; // Only call entry and selectors are observed. No owner outcome is fabricated.
    }
    return super.run(name, allow);
  }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i], k = n.key, v = n.value;
      if (k === 'if') {
        const chain = [n]; while (nodes[i + 1] && ['else', 'else_if'].includes(nodes[i + 1].key)) chain.push(nodes[++i]);
        if (!super.eval(chain)) return false;
      } else if (k === 'has_tech') { if (!this.tech.has(v)) return false; }
      else if (k === 'is_special_project_completed') { if (!this.completed.has(v)) return false; }
      else if (k === 'has_dlc') { if (!this.dlc.has(v.replace(/^"|"$/g, ''))) return false; }
      else if (k === 'has_character') { if (!this.characters.has(v)) return false; }
      else if (k === 'has_country_flag') { if (!this.flags.has(v)) return false; }
      else if (k === 'set_country_flag') this.flags.add(v);
      else if (k === 'clr_country_flag') this.flags.delete(v);
      else if (k === 'has_idea') { if (!this.ideas.has(v)) return false; }
      else if (k === 'add_ideas') { this.ideas.add(v); this.ideaAdds.push(v); }
      else if (k === 'has_dynamic_modifier') { if (!this.modifiers.has(v)) return false; }
      else if (k === 'add_dynamic_modifier') { const id = this.field(v, 'modifier'); this.modifiers.add(id); this.modifierAdds.push(id); }
      else if (k === 'force_update_dynamic_modifier') this.nativeRefreshes++;
      else if (k === 'set_technology') {
        for (const t of v.filter(t => t.key !== 'popup')) { assert.equal(t.value, '1'); this.tech.add(t.key); this.technologyWrites.push(t.key); }
      } else if (boundaryCalls.has(k) || ['cbrn_policy_allows_extreme_use', 'brilliant_scientist_mengele_project_stage_provider_is_valid'].includes(k)) {
        const yes = this.run(k); if ((v === 'no' && yes) || (v !== 'no' && !yes)) return false;
      } else if (!super.eval([n])) return false;
    }
    return true;
  }
}
const report = { model: 'Actual production AST, reused fixed-point VM with unchanged helper temporary cleanup; country native inputs and named complex owner boundaries are explicit fixtures', cases: [], limits: [
  'Native equipment/sub-unit bonus application and project callback timing are not executed.',
  'Story settlement, Capacity/control lifecycle, custom force reconstruction, templates and provider rebuild stop at named call boundaries.',
  'Mengele live-provider validity and extreme-use policy are fixture inputs, not simulated lifecycle proofs.',
  'Dynamic-modifier presence and add-call cardinality are tested. Effective modifier aggregation in HOI4 is not modeled.',
] };
function check(id, fn) { const evidence = fn(); report.cases.push({ id, passed: true, ...evidence }); }
function fixture({ tech = [], completed = [], extreme = false } = {}) { const v = new ProjectVM(); tech.forEach(x => v.tech.add(x)); completed.forEach(x => v.completed.add(x)); v.extremePolicy = extreme; return v; }
const requirements = [
  ['smoke', ['basic_gas_masks', 'motorised_infantry'], []],
  ['collective_protection', ['improved_gas_masks', 'sealed_containment_laboratories'], []],
  ['renewing_filters', ['advanced_gas_masks'], ['sp:sp_cbrn_collective_protection_systems']],
  ['vaccines', ['bio_surveillance_networks', 'pathogen_handling_protocols'], []],
  ['field_antibiotics', ['rapid_outbreak_response', 'pathogen_handling_protocols'], []],
  ['regenerative_serum', ['fail_safe_containment_facilities'], ['sp:sp_cbrn_field_antibiotics']],
  ['antiserum', ['integrated_epidemic_control'], ['sp:sp_cbrn_mass_vaccine_production', 'sp:sp_cbrn_field_antibiotics']],
];
for (const [name, tech, completed] of requirements) {
  const helper = `cbrn_project_can_research_${name}`;
  check(`admission-${name}-positive`, () => { assert(fixture({ tech, completed }).run(helper)); });
  for (const token of [...tech, ...completed]) check(`admission-${name}-missing-${token}`, () => {
    assert.equal(fixture({ tech: tech.filter(x => x !== token), completed: completed.filter(x => x !== token) }).run(helper), false);
  });
}
for (const medical of ['sp:sp_cbrn_mass_vaccine_production', 'sp:sp_cbrn_field_antibiotics']) check(`discovery-biomedical-${medical}`, () => {
  assert(fixture({ tech: ['fail_safe_containment_facilities'], completed: [medical] }).run('cbrn_project_can_discover_biomedical_acceleration'));
});
check('discovery-biomedical-missing-containment', () => assert.equal(fixture({ completed: ['sp:sp_cbrn_field_antibiotics'] }).run('cbrn_project_can_discover_biomedical_acceleration'), false));
check('discovery-biomedical-missing-foundation', () => assert.equal(fixture({ tech: ['fail_safe_containment_facilities'] }).run('cbrn_project_can_discover_biomedical_acceleration'), false));
const clonePrerequisites = ['sp:sp_brilliant_scientist_biomedical_acceleration', 'sp:sp_cbrn_regenerative_serum'];
check('discovery-cloning-positive', () => assert(fixture({ completed: clonePrerequisites }).run('cbrn_project_can_discover_cloning')));
for (const missing of clonePrerequisites) check(`discovery-cloning-missing-${missing}`, () => assert.equal(fixture({ completed: clonePrerequisites.filter(x => x !== missing) }).run('cbrn_project_can_discover_cloning'), false));
const exoticInputs = { tech: ['fail_safe_containment_facilities'], completed: ['sp:sp_cw_sarin_program'], extreme: true };
check('discovery-exotic-positive', () => assert(fixture(exoticInputs).run('cbrn_project_can_discover_exotic_biological')));
for (const missing of ['tech', 'completed', 'extreme']) check(`discovery-exotic-missing-${missing}`, () => assert.equal(fixture({ ...exoticInputs, [missing]: missing === 'extreme' ? false : [] }).run('cbrn_project_can_discover_exotic_biological'), false));
check('phantom-visible-but-not-researchable-without-tabun', () => { const v = fixture(exoticInputs); assert(v.run('cbrn_project_can_discover_phantom_mist')); assert.equal(v.run('cbrn_project_can_research_phantom_mist'), false); v.tech.add('tabun'); assert(v.run('cbrn_project_can_research_phantom_mist')); });
for (const missing of ['tech', 'completed', 'extreme']) check(`phantom-discovery-missing-${missing}`, () => assert.equal(fixture({ ...exoticInputs, [missing]: missing === 'extreme' ? false : [] }).run('cbrn_project_can_discover_phantom_mist'), false));
const firstTier = [
  ['mechanized_smoke', 'mechanized_smoke_screens'], ['collective_protection', 'collective_protection_systems'],
  ['renewing_filters', 'self_renewing_filters'], ['phantom_mist', 'phantom_mist'], ['mass_vaccine', 'mass_vaccine_production'],
  ['field_antibiotics', 'field_antibiotics'], ['regenerative_serum', 'regenerative_serum'], ['antiserum', 'broad_spectrum_antiserum'],
];
check('eight-first-tier-adapters-repeated', () => {
  const v = new ProjectVM(); for (let repeat = 0; repeat < 2; repeat++) for (const [name] of firstTier) assert(v.run(`cbrn_complete_${name}_project`));
  assert.deepEqual([...v.flags].sort(), firstTier.map(([, flag]) => `cbrn_project_${flag}`).sort());
  assert.deepEqual(v.ideaAdds, ['cbrn_project_regenerative_serum_idea']); assert.equal(v.technologyWrites.length, 0);
  return { durableFlags: [...v.flags], serumIdeaAddCalls: v.ideaAdds.length };
});
for (const family of ['flamethrower', 'engineering']) {
  const project = family === 'flamethrower' ? 'sp:sp_land_flamethrower_tank' : 'sp:sp_land_military_engineering_vehicles';
  const tech = family === 'flamethrower' ? 'sealed_tank_crews' : 'mobile_wash_columns';
  const output = family === 'flamethrower' ? 'cbrn_sealed_flamethrower_crew_integration' : 'cbrn_armored_engineer_decontamination_integration';
  for (const order of [['project', 'collective', 'tech'], ['collective', 'tech', 'project'], ['tech', 'project', 'collective']]) check(`integration-${family}-${order.join('-')}`, () => {
    const v = new ProjectVM(); v.dlc.add('No Step Back');
    order.forEach((step, i) => { if (step === 'project') v.completed.add(project); if (step === 'collective') v.completed.add('sp:sp_cbrn_collective_protection_systems'); if (step === 'tech') v.tech.add(tech); assert(v.run('cbrn_sync_vanilla_project_integrations')); assert.equal(v.tech.has(output), i === 2); });
    assert(v.run('cbrn_sync_vanilla_project_integrations')); assert(v.run('cbrn_sync_vanilla_project_integrations'));
    assert.deepEqual(v.technologyWrites, [output]); return { technologyWrites: v.technologyWrites };
  });
}
check('flamethrower-integration-requires-dlc', () => { const v = fixture({ tech: ['sealed_tank_crews'], completed: ['sp:sp_land_flamethrower_tank', 'sp:sp_cbrn_collective_protection_systems'] }); assert(v.run('cbrn_sync_vanilla_project_integrations')); assert.equal(v.tech.size, 1); });
check('engineering-integration-does-not-require-tank-dlc', () => { const v = fixture({ tech: ['mobile_wash_columns'], completed: ['sp:sp_land_military_engineering_vehicles', 'sp:sp_cbrn_collective_protection_systems'] }); assert(v.run('cbrn_sync_vanilla_project_integrations')); assert.deepEqual(v.technologyWrites, ['cbrn_armored_engineer_decontamination_integration']); });
check('collective-adapter-flag-cannot-replace-native-completion', () => {
  const v = fixture({ tech: ['mobile_wash_columns'], completed: ['sp:sp_land_military_engineering_vehicles'] }); assert(v.run('cbrn_complete_collective_protection_project'));
  assert(v.flags.has('cbrn_project_collective_protection_systems')); assert.equal(v.technologyWrites.length, 0);
  v.completed.add('sp:sp_cbrn_collective_protection_systems'); assert(v.run('cbrn_sync_vanilla_project_integrations')); assert.deepEqual(v.technologyWrites, ['cbrn_armored_engineer_decontamination_integration']);
});
const biomedicalModifiers = ['theory', 'prototype', 'deployment'].map(x => `brilliant_scientist_biomedical_${x}`);
function biomedical(source = 0, tier = 'deployment') { return new ProjectVM().set('chaosx_conventional_technology_family', 6).set('chaosx_conventional_technology_tier', tier === 'deployment' ? 3 : 4).set('chaosx_custom_technology_source', source); }
check('biomedical-core-repeat-and-reconcile-preserve-full-package', () => {
  const v = biomedical(); assert(v.run('chaosx_grant_conventional_technology_package_core')); assert(v.run('chaosx_grant_conventional_technology_package_core'));
  assert(v.flags.has('conventional_technology_biomedical_operational')); assert.deepEqual(v.modifierAdds, biomedicalModifiers); assert.equal(v.arrays.size, 0);
  v.modifiers.delete(biomedicalModifiers[1]); assert(v.run('chaosx_reconcile_conventional_technology_runtime'));
  assert.deepEqual(v.modifierAdds, [...biomedicalModifiers, biomedicalModifiers[1]]); return { modifierAddCalls: v.modifierAdds };
});
check('biomedical-source-zero-no-provenance-duplicates', () => { const v = biomedical(); for (let i = 0; i < 3; i++) assert(v.run('chaosx_grant_conventional_technology_package')); assert.equal(v.array('conventional_technology_operational_provenance').length, 0); assert.deepEqual(v.modifierAdds, biomedicalModifiers); return { provenanceEntries: 0, modifierAddCalls: v.modifierAdds }; });
check('biomedical-positive-sources-dedupe-family-and-source', () => {
  const v = biomedical(16); for (let i = 0; i < 3; i++) assert(v.run('chaosx_grant_conventional_technology_package'));
  v.set('chaosx_custom_technology_source', 25); assert(v.run('chaosx_grant_conventional_technology_package')); assert(v.run('chaosx_grant_conventional_technology_package'));
  const expected = [ticks(6000016), ticks(6000025)]; assert.deepEqual(v.array('conventional_technology_operational_provenance'), expected);
  assert.deepEqual(v.modifierAdds, biomedicalModifiers); return { receiptTicks: expected.map(String) };
});
check('conventional-provenance-same-source-distinct-family', () => {
  const v = biomedical(16); assert(v.run('chaosx_record_conventional_technology_operational_provenance')); assert(v.run('chaosx_record_conventional_technology_operational_provenance'));
  v.set('chaosx_conventional_technology_family', 3); assert(v.run('chaosx_record_conventional_technology_operational_provenance')); assert(v.run('chaosx_record_conventional_technology_operational_provenance'));
  assert.deepEqual(v.array('conventional_technology_operational_provenance'), [ticks(6000016), ticks(3000016)]); assert.equal(v.modifierAdds.length, 0);
  return { receiptTicks: v.array('conventional_technology_operational_provenance').map(String), grants: 0 };
});
check('biomedical-weaponization-repeat-is-one-fourth-modifier', () => { const v = biomedical(16, 'weaponization'); for (let i = 0; i < 2; i++) assert(v.run('chaosx_grant_conventional_technology_package')); assert.deepEqual(v.modifierAdds, [...biomedicalModifiers, 'brilliant_scientist_biomedical_weaponization']); assert.equal(v.array('conventional_technology_operational_provenance').length, 1); assert.equal(v.array('conventional_technology_weaponization_provenance').length, 1); return { modifierAddCalls: v.modifierAdds }; });
check('invalid-biomedical-tier-no-grant', () => { const v = biomedical(16).set('chaosx_conventional_technology_tier', 1); assert(v.run('chaosx_grant_conventional_technology_package')); assert.equal(v.flags.size, 0); assert.equal(v.modifierAdds.length, 0); assert.equal(v.arrays.size, 0); });
const advanced = [
  ['biomedical_acceleration', 'biomedical', 5, 'biomedical', 6, null],
  ['cloning', 'cloning', 7, 'cloning', 8, 'clone'],
  ['paleogenetics', 'paleogenetics', 9, 'paleogenetics', 10, 'paleogenetic'],
  ['xenobiological', 'xenobiological', 10, 'xenobiological_synthesis', 11, 'xenobiological'],
];
for (const [adapter, route, index, storyName, storyId, customName] of advanced) for (const owner of ['ordinary', 'kruger-theory', 'mengele-theory', 'invalid-mengele', 'kruger-no-theory']) check(`adapter-${adapter}-${owner}`, () => {
  const v = new ProjectVM(); const stages = Array(15).fill(ticks(0));
  v.completed.add(`sp:sp_brilliant_scientist_${adapter === 'xenobiological' ? 'xenobiological_synthesis' : adapter}`); // Completion callback state, not research admission.
  if (owner.startsWith('kruger')) { v.flags.add('brilliant_scientist_current_host'); v.characters.add('KRG_warren_kruger'); if (owner === 'kruger-theory') stages[index] = ticks(1); }
  v.arrays.set('brilliant_scientist_project_stage_entries', stages);
  if (owner.includes('mengele')) { v.flags.add(`mengele_event016_${storyName}_theory_completed`); v.validMengele = owner === 'mengele-theory'; }
  const story = ['kruger-theory', 'mengele-theory'].includes(owner);
  assert.equal(v.run(`cbrn_project_${route}_uses_event016_story`), story);
  for (let i = 0; i < 2; i++) assert(v.run(`cbrn_complete_${adapter}_project`));
  if (story) { assert.equal(v.ownerCalls.length, 2); assert(v.ownerCalls.every(x => x.name === 'brilliant_scientist_record_new_project_prototype' && x.storyFamily === String(ticks(storyId)))); assert.equal(v.modifierAdds.length, 0); }
  else if (customName) { assert.equal(v.ownerCalls.length, 2); assert(v.ownerCalls.every(x => x.name === 'chaosx_grant_custom_operational_technology' && x.customFamily === String(constants.get(`constant:chaosx_custom_technology_family.${customName}`)) && x.source === '0')); }
  else { assert.equal(v.ownerCalls.length, 0); assert(v.flags.has('conventional_technology_biomedical_operational')); assert.deepEqual(v.modifierAdds, biomedicalModifiers); assert.equal(v.array('conventional_technology_operational_provenance').length, 0); }
  assert(!v.trace.some(x => x.startsWith('brilliant_scientist_can_research_')), 'completion must not reuse admission gate');
  return { story, boundaryCalls: v.ownerCalls, modifierAddCalls: v.modifierAdds };
});
check('temporary-cleanup-remains-conservative', () => {
  const v = new ProjectVM(); assert(v.run('cbrn_complete_biomedical_acceleration_project')); assert.equal(v.vars.has('chaosx_conventional_technology_family'), false); assert.equal(v.vars.has('chaosx_conventional_technology_tier'), false); assert.equal(v.vars.has('chaosx_custom_technology_source'), false);
  assert(v.flags.has('conventional_technology_biomedical_operational')); assert.equal(VM.prototype.run, vmRun); return { droppedTemps: v.droppedTemps, unchangedRun: true };
});
const dependencyPaths = [...new Set([...sources, ...tuning, ...base.files, 'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js'])];
report.sourceHashes = dependencyPaths.map(file => ({ path: file, sha256: crypto.createHash('sha256').update(fs.readFileSync(path.join(root, file))).digest('hex') }));
report.dirtySharedDependencies = execFileSync('git', ['status', '--porcelain', '--', ...dependencyPaths], { cwd: root, encoding: 'utf8' }).trim().split(/\r?\n/).filter(Boolean);
report.caseCount = report.cases.length;
report.testRunnerSha256 = crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex');
fs.writeFileSync(path.join(__dirname, 'source_test_results.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ caseCount: report.caseCount, passed: true, dirtySharedDependencies: report.dirtySharedDependencies, result: path.join(__dirname, 'source_test_results.json'), limits: report.limits }, null, 2));
