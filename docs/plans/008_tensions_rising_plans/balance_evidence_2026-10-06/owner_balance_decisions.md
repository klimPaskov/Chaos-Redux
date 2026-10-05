# Tensions Rising balance and actual-result reporting

Disposition: implemented source correction; native and probability acceptance remain incomplete.
Acceptance basis: the user's G4/G6 direction authorises proportionate balance and weak-design corrections.
The parent accepted this tranche after reviewing the supplied `evt008_pop00.png`: it shows 99 percent world tension on 1 January 1936 while the baseline report is open.

## Accepted tuning

| Packet | Previous requested threat | Accepted requested threat |
| --- | ---: | ---: |
| Baseline | 100 | 2 |
| Stage I | 100 | 3 |
| Stage II | 200 | 5 |
| Stage III | 500 | 8 |
| Stage IV | 1000 | 12 |

Vanilla Rhineland adds 5 named threat.
A newspaper/embassy alarm should not by itself force the opening world's mobilisation threshold to the ceiling.
The upper stages retain increasing pressure, while their pulse, relations, posture, Chaos, and border-clash effects remain separately gated.
An automatic shock has a thirty-day global cooldown, preventing smaller packets from creating a new stream of repeated reports.
Manual forces bypass that cadence and retain the pending-country report coalescing contract.
Each effective manual shock also refreshes the thirty-day recent-alarm flag, preventing a new automatic alarm immediately afterward.
No new world-iterating daily action was added.

## Dynamic country distribution

The helper derives its recipient cap by flooring `packet / minimum_country_slice`, with a minimum count of one.
The chosen count is the lesser of that cap and the actual eligible source count.
Each selected source receives `packet / chosen_count`.
The existing minimum slice is 0.1, so the accepted full-pool caps are 20/30/50/80/120.
There are no duplicated hardcoded cap ladders to keep in sync.
The native static `random_select_amount` is injected through the existing documented meta-effect mechanism as an integer.
For below-minimum future packets, the one-source slice remains the requested amount rather than overshooting it.
Zero sources or a nonpositive packet adds no named threat.

## Actual report values

The distribution helper returns the observed `global.threat` change multiplied by 100, not the requested packet.
Only its root/stage callers add that returned value to the pending main report; incident callers ignore it and cannot repopulate an acknowledged main report.
Root and stage callers initialise the output before the helper call.
The root also records the overall observed change in `global.chaos_meter_value`, including the shared world-tension updater and any ceiling.
Negative net Chaos selects a colour-free decrease branch with an absolute displayed amount.
One decimal place preserves sub-point results.
The first-effective-stage marker is a flag rather than a test of positive numeric totals, because pulse/opinion/posture effects may still matter at both meter ceilings.
New report batches and acknowledgement clear that flag.

## Required evidence

The read-only auditor preserved immutable pre-tranche source from commit `e99130b84519be8026068502e594507b3979f73d` before the owner patch.
Its named scenarios are retained under `auditor/`; a stopped pending inspection is a route gap and does not establish probabilities.
The mandatory same-scenario comparison must bind before/after constants and dependencies explicitly or remain unresolved.
The source model in `source_model/` tests arithmetic, helper-frame return, clipping, and source-level cadence/report contracts with native stubs.
It cannot certify engine RNG, native threat caching, helper meta expansion, on-actions, or rendered popup refresh.

## Local references and route gaps

The parent used direct local reads after the resource reader returned Transport closed.
Source revisions below are SHA-256 file hashes, not proof of live execution.

| Source | Read section |
| --- | --- |
| Installed `documentation/effects_documentation.md` | `add_named_threat`, 1762–1769; `round_temp_variable`, 6476–6484; `set_global_flag`, 7085–7092; existing meta-effect and arithmetic sections cited in the earlier handoffs |
| Installed `documentation/dynamic_variables_documentation.md` | `threat`, 1051–1053: global world tension is a 0–1 value |
| Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | named threat, 1502–1503, and the meta-effect section cited by the event skill |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | global/country flag equivalence and timed flags, 119–129; variable lifetime, 435–449 |
| Vanilla `common/national_focus/germany.txt` | Rhineland's `add_named_threat = 5`, 8188 |
| Mod `common/scripted_effects/chaos_meter_effects.txt` | existing `global.threat * 100` conversion and derived Chaos update, 6501–6522 |

Exact current source and model hashes accompany the retained evidence.
The colour audit and source coverage are required after the final model review.
No native balance or numeric probability conclusion is claimed from a failed route.

## Orchestrator additions to the live cases

Start a fresh USA 1936 case with world tension below full and the normal event system initialised.
Force a baseline Event 8: it should add about two meter points, not jump to 99 percent; the hover must show the observed change.
Repeat separately at 99 percent: the hover should show the remaining increase to the ceiling rather than the whole requested packet.
At full tension with an enabled evolved stage, the WT increase should be zero while real Chaos/pulse/opinion effects and first-stage presentation remain correct.
Test each stage and compare the 2/3/5/8/12 requested ladder against observed world tension, recognising the ceiling.
After an effective shock, automatic selection should stay unavailable for thirty days; a manual force still applies and reports/coalesces immediately.
At both meter ceilings, keep the report open and change the tier: its first meaningful stage must remain stable even when numeric totals are zero.
Check negative net Chaos in a controlled world-tension reconciliation case: the hover must say decreases and display its absolute amount.
The prior Thin Wire, One Denial, expiry, delayed-follow-up, and report-count cases remain required.

Final Event inspect and script-validation calls returned the exact error `Transport closed`.
Neither returned a domain report, source revision, or artifact for the balance patch.

The completed read-only auditor preserves sixty unique source-model scenario IDs with identical before/after inputs.
Both baseline inspections and the one comparison remained pending and were stopped, returning no artifact or numeric result.
Its effect-only comparison leaves before constants/other dependencies unbound; this is an explicit coverage gap.
The parent reran the retained source-derived model successfully: 168 distribution cases, four caller-report examples, and three signed Chaos examples.
These arithmetic/static-contract results remain separate from native execution.
