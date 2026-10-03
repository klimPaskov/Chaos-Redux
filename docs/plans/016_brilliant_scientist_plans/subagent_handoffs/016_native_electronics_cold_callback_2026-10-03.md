# Event016 cold native callback storage review

Disposition: implemented source correction with targeted source-contract validation.
Acceptance basis: the existing exact provider receipt contract requires correct source provenance without relying on unrelated temporary fields in an outer caller.
This is a related correction within the accepted Electronics native ownership tranche.

The shared exact later-stage core initializes its own project index, output-applied and stage-package output slots before nested mapping and output helpers.
Its caller-supplied family, requested stage and exact source remain intact.
The caller initializes native_later_stage_settled before the call when it consumes that temporary result after return.
No native project cost, clock, progress, reward, paid receipt, or model changes.

The parent reran the retained 6,590-case actual-source driver after this correction.
The additional driver below passes 160 cold-entry cases with every root temporary removed, conservative helper-return cleanup, both radio technology states, both selected/Theory/provider states, all five paid-stage states, and both existing-Prototype states.
It executes the actual Radar country output and the separately named radio_detection completion boundary.
Successful eligible Deployment records exact source 1 at Electronics family index 1 and preserves index 0 and every paid receipt row.
Two counterexamples substitute only the real previous HEAD later-stage helper while retaining the corrected Prototype core.
Both old-helper cases leave Deployment and its source receipt unrecorded in this conservative source model.
The combined source checks total 6,752.

Engine queries and provider state are fixture inputs; availability/modifier refresh and operational package payloads retain the core driver's declared stubs.
The named technology callback is invoked as a separate source boundary and does not establish observed engine notification order.
No native payment, research clock, cancellation, callback-generation isolation, rendered UI, balance, or live-log acceptance is established.
Native cancellation/reselection and the full Event016 completion contract remain unresolved.

The reference rule is offline Data structures:425-445, especially temporary variables across scripted helper returns, SHA-256 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4.
Installed effects_documentation.md:7820-7840 documents set_temp_variable in any scope, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.
No simplification, new project/technology, periodic world iteration, or extra asset is introduced.

## Executable source driver

Run from the mod root with Python.
It reads the retained core driver and current source, uses Git only to read the real before helper, and writes no gameplay files.

```python
from pathlib import Path
import re, itertools, copy, subprocess, json
handoff = Path('docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_electronics_core_2026-10-03.md')
block = re.findall(r'```python\n(.*?)\n```', handoff.read_text(encoding='utf-8'), re.S)
assert len(block) == 1
g = {'__name__': '__main__'}
exec(compile(block[0], str(handoff) + ':driver', 'exec'), g)
prefix, base, defs, const = (g[k] for k in ['prefix', 'base', 'defs', 'const'])
fixture, run, parse, Model = (g[k] for k in ['fixture', 'run', 'parse', 'Model'])
radar = parse(Path('common/special_projects/projects/radar_projects.txt').read_text(encoding='utf-8-sig'))
def child(body, key):
    return next(v for k, op, v in body if k == key)
country = child(child(child(radar, 'sp_air_radar'), 'project_output'), 'country_effects')
expected_source = const['mengele_event016_native_later_stage_source.electronics_radar_pair']
passed = 0
for selected, theory, provider, active, radio, pre_proto in itertools.product([False, True], [False, True], [False, True], range(5), [False, True], [False, True]):
    m = fixture()
    m.conservative = True
    m.provider = provider
    m.temp.clear()
    if selected: m.flags.add(base + 'native_selected_electronics_radar')
    if theory: m.flags.add(base + 'electronics_theory_completed')
    if pre_proto: m.flags.add(base + 'electronics_prototype_completed')
    if radio: m.tech.add('radio_detection')
    m.arr[base + 'active_project_stage_entries'][1] = active
    for key, values in m.arr.items():
        if key.startswith(base + 'active_cost_'):
            values[0] = 66
            values[1] = 77
    paid_before = {k: copy.deepcopy(v) for k, v in m.arr.items() if k.startswith(base + 'active_')}
    # Direct native country effects start with no provider scratch temporaries.
    m.effect(country)
    if not radio:
        m.temp.clear()
        run(m, 'native_completion_radio_detection')
    fresh = selected and theory and provider and active == 0 and not pre_proto
    deployed = provider and active == 0 and (pre_proto or fresh)
    assert (base + 'electronics_deployment_completed' in m.flags) == deployed
    assert m.arr[base + 'native_later_stage_deployment_source_entries'][1] == (expected_source if deployed else 0)
    assert m.arr[base + 'native_later_stage_deployment_source_entries'][0] == 0
    assert all(m.arr[k] == v for k, v in paid_before.items())
    passed += 1

# Isolate the old later-stage helper while retaining the corrected Prototype core.
old_defs = copy.deepcopy(defs)
old_body = dict((k, v) for k, op, v in parse(subprocess.check_output(['git', 'show', '9f94f7c2a19dd97a0ffb8bfab5c9ceab977bca9a:common/scripted_effects/016_mengele_project_stage_effects.txt']).decode('utf-8-sig')) if isinstance(v, list))
old_defs[prefix + 'settle_exact_native_later_stage'] = old_body[prefix + 'settle_exact_native_later_stage']
old_failures = 0
old_completion_flags = []
for radio in [False, True]:
    m = fixture()
    m.defs = old_defs
    m.conservative = True
    m.temp.clear()
    m.flags.update([base + 'electronics_theory_completed', base + 'native_selected_electronics_radar'])
    if radio: m.tech.add('radio_detection')
    m.effect(country)
    if not radio:
        m.temp.clear()
        run(m, 'native_completion_radio_detection')
    old_completion_flags.append(base + 'electronics_deployment_completed' in m.flags)
    assert m.arr[base + 'native_later_stage_deployment_source_entries'][1] == 0
    old_failures += 1
print(json.dumps({'coldRadarCasesPassed': passed, 'oldLaterStageMissingProvenanceCounterexamples': old_failures, 'oldDeploymentCompletionFlags': old_completion_flags, 'expectedRadarSource': expected_source, 'limits': ['Actual source executed in conservative helper-frame model', 'Engine/provider/technology callback inputs supplied as fixture state', 'No native timing, payment or engine acceptance proof']}, indent=2))

```

Current stage source SHA-256: d129df615665c665b2bffca00bbe36cf436c2b425b86b7d6fb13af2ca7cb9989.
Before helper checkpoint: 9f94f7c2a19dd97a0ffb8bfab5c9ceab977bca9a.
