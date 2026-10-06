# Event 24 Exact-State Probability Baseline

Audit date: 2026-10-03.

Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

Status: prepatch source audit complete, required MCP probability baseline blocked by repeated 600-second tool timeouts, all probability rankings and normalized selection results unresolved.

This is a read-only audit for the narrow exact-state comparator repair and the `chaosx.nr24.50.c` affordability gate. No gameplay source was edited, no balance target was selected, no after-comparison was run, no game was launched, and no other task was contacted.

## Scope and accepted scenarios

The accepted design source is `docs/specs/024_video_game_in_sweden_specs/024_video_game_in_sweden_ai_probability_scenarios.md`, read with `024_video_game_in_sweden_decision_map.md` and specification parts 1 through 3. The named scenario IDs used below are read directly from that accepted matrix and prior Event24 handoffs. No new scenario IDs are proposed.

The analyzed weighted surfaces are event options in `chaosx.nr24.20`, `chaosx.nr24.30`, and `chaosx.nr24.50`. The opening option pool in `chaosx.nr24.2` uses the existing opening matrix. The incident selector in `video_game_in_sweden_roll_incident` has seven `random_list` candidates. The decision category `video_game_in_sweden_program_category` has 18 decision `ai_will_do` blocks.

The preserved opening scenario set is `P24_FINAL_OPENING_MATRIX` with `P24-O1` through `P24-O4`. The other preserved scenario IDs are `P24-C1` through `P24-C7`, `P24-D1` through `P24-D5`, and `P24-I1` through `P24-I5`. The `P24-F1` through `P24-F5` foreign-response surface and `P24-E1A` through `P24-E3B` timing scenarios were not re-audited in this pass.

## Immutable BEFORE source identities

All listed immutable copies were SHA-256 checked against the live source at audit start and again before writing this handoff. Every pair still matches. These hashes are the prepatch baseline identities and the parent must preserve these copies for any later compare.

| Live source | Immutable BEFORE copy | SHA-256 |
| --- | --- | --- |
| `events/024_hearts_of_iron.txt` | `docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_hearts_of_iron.txt` | `5F628F1C1718FEA7FC9171E46C3A2530101A3749ECFEDC9CA288E3212F862420` |
| `common/decisions/024_video_game_in_sweden_decisions.txt` | `docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden_decisions.txt` | `DC1EA5273D6F22CFE8361C8D8BA176D344FC4BA98865F62A2145455D694F7F30` |
| `common/scripted_effects/024_video_game_in_sweden_effects.txt` | `docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden_effects.txt` | `9336E28C7ECA010C16B24242926A85E633A5083A2F8C049269AEEC587C4C9622` |
| `common/scripted_triggers/024_video_game_in_sweden_triggers.txt` | `docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden_triggers.txt` | `875B061004F7122C0599825409D9345B532EA38B38AC1ADDCC19C11965BF58E5` |
| `common/script_constants/024_video_game_in_sweden_constants.txt` | `docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden_constants.txt` | `622621C00D24CF036CF3FEC3F1F82949DB6D92B3AF4701AF396BEF4E132D632C` |
| `common/ideas/024_hearts_of_iron_ideas.txt` | `docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_hearts_of_iron_ideas.txt` | `04E14B1B74D5EC5FD862F45D9EAA16524C6316D6E986856618B9EB603E7AF97C` |
| `common/scripted_localisation/024_video_game_in_sweden.txt` | `docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden.txt` | `5844548F94A997A80DB45D8950A3848DD6B589A73037E137F9DCEF5CBEB0ACBF` |

The accepted BEFORE copies are unchanged. The idea and scripted-localisation copies are identity cross-checks, not weighted candidates in this audit.

At the final scoped Git-status check, the five live weighted gameplay source files above were marked modified relative to `HEAD`, while their bytes still matched these immutable BEFORE copies. Those worktree changes predate this audit baseline and were not edited here. The only file added by this audit is this handoff.

## MCP calls and reference evidence

Connected workspace ID: `mod_chaos_redux_ea3b2d67c2c0`.

| Tool | Request | Result |
| --- | --- | --- |
| `hoi4.probability_inspect` | `event_option_ai_chance`, source `events/024_hearts_of_iron.txt`, candidates `chaosx.nr24.20.a`, `.20.b`, `.20.c`, refresh enabled | Tool error: `timed out awaiting tools/call after 600s`. No `sourceRevision`, candidate rows, `poolComplete`, unresolved fields, artifact URI, or scenario hash returned. |
| `hoi4.probability_inspect` | Same adapter and three candidates against the immutable BEFORE event snapshot path | Tool error: `timed out awaiting tools/call after 600s`. No inspect evidence returned. |
| `hoi4.event_inspect` | `trace` for `chaosx.nr24.20`, both directions, depth 3, 100-node cap | Tool error: `timed out awaiting tools/call after 600s`. No structural artifact or source revision returned. |
| `hoi4.event_render` | `options` view for `chaosx.nr24.20` | Tool error: `timed out awaiting tools/call after 600s`. No render URI returned. |
| `hoi4.reference_context` | Event surface | Succeeded with workspace ID above and source paths for installed Effects and Triggers documentation plus offline Event modding, Data structures, Effects, Triggers, Scopes, and related wiki pages. `artifactCount = 0`. |
| `hoi4.reference_context` | AI surface | Succeeded with the same workspace ID and source paths for installed AI strategy documentation, offline AI modding, Triggers, Scopes, and Data structures. `artifactCount = 0`. |
| `hoi4.reference_context` | Decision surface | Tool error: `timed out awaiting tools/call after 600s`. |
| `hoi4.reference_search` | `check_variable compare default omitted compare equals greater_than_or_equals` across game docs, wiki, and script docs | Tool error: `timed out awaiting tools/call after 600s`. |
| `hoi4.reference_read` | Installed `triggers_documentation.md`, source ID `c0376eecba6ff9d269543661538e9ab9bb76503c7cef06e217169e85e36f0f5b`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, requested lines 2110 onward | Tool error: `timed out awaiting tools/call after 600s`. |
| `hoi4.reference_read` | Offline Data structures page, source ID `de4ff54ddb45a49b5228c82da5bd6f8098bca7eed04520d50a20db30304b169a`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, requested line 566 onward | Tool error: `timed out awaiting tools/call after 600s`. |
| `hoi4.reference_read` | Offline Triggers page, source ID `3bfd60ebbf3fca651f93d5c870c77046f7fb9085303b5fb16a958ce121bbae67`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, requested line 571 onward | Tool error: `timed out awaiting tools/call after 600s`. |
| `hoi4.source_lookup` | Symbol `video_game_in_sweden_phase`, references enabled | Tool error: `timed out awaiting tools/call after 600s`. No source revision, indexed references, or artifact URI returned. |

The successful reference-context calls identify the relevant current source revisions, but their excerpts only identified document headings. The local offline wiki fallback was read directly at `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:566` and `:598-609`, and `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:571-586`. The installed fallback was read directly at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:2110-2131`.

The installed Triggers documentation lists `equals`, `not_equals`, the strict inequalities, and their syntax, but it does not state the default when `compare` is omitted. The offline Data structures page explicitly states that the default is `greater_than_or_equals`. This supports bounded source reasoning from the configured offline reference, but the failed reference reads and absent game run leave engine behavior unverified in this task.

Reference source identities from the successful context calls are `triggers_documentation.md` revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, offline Data structures revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, and offline Triggers revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`. No MCP reference-read artifact URIs were returned.

No probability evaluation, sweep, simulation, sequence, render, or comparison completed. Their dependent `analysisId`, `scenarioHash`, `comparisonId`, source revisions, unresolved-field rows, and rendered artifact URIs are unavailable. The mandatory fresh probability baseline is therefore blocked, and every normalized probability, rank, sensitivity, or timing conclusion below is unresolved.

Historical MCP artifacts retained for context only are the opening evaluation in `subagent_handoffs/06_ai_probability_audit.md`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f67017802db38f3033f13c7da9155822c60531c6a14b23fded978d1f2370fda7/2c77c3ee1582b4997563595f327f82e7b135bd12bbad5dfe8fcacd85f7952c09/probability-cb60cb3ec67ba407e5c9dec4.json`, and the prior decision inspect at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6586c8819613196ac2c29345e39353cb6799c6a626201fdca2f87539c95a189/b9c23bef38b88d6c6e6ef6cf9f5bd97e7326017f85e1b5f22e31c91dee24ce13/probability-inspect-d07e33ab2f93.json`. The opening result was reported as 12 rows with 12 bounded unresolved inputs and one diagnostic. The decision inspect was reported as one projected decision, zero candidate-pool matches, and 12 unresolved inputs. Neither artifact has a source revision in those handoffs that binds it to these 2026-10-03 immutable snapshots, so neither is accepted as this fresh baseline.

## Source constants and candidate-pool inventory

The exact numeric enums are in `common/script_constants/024_video_game_in_sweden_constants.txt:13-40,49-95`.

| Value group | Exact source values |
| --- | --- |
| Phase | `phase_baseline = 1`, `phase_evolution_i = 2`, `phase_evolution_ii = 3`, `phase_evolution_iii = 4`, `phase_recovery = 5`, `phase_closed = 6` |
| Route | `route_controlled = 1`, `route_commercial = 2`, `route_officer = 3` |
| Incident | `zero = 0`, `incident_terrain = 1`, `incident_supply = 2`, `incident_enemy = 3`, `incident_template = 4`, `incident_diplomatic = 5`, `incident_workplace = 6`, `incident_party = 7` |
| Exact country-state targets | `stockholm_state = 141`, `southern_front_state = 138`, `central_front_state = 141`, `northern_front_state = 666` |

The state IDs are consumed by direct `owns_state` and `controls_state` triggers, including `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:18-22,199-200,583-599,630-631,741-767`. No `check_variable` comparison against a stored state ID was found in the audited source files, so no state-ID comparator defect is claimed.

| Surface | Complete definition-level pool | Raw source weights and modifiers | Pool and factor completeness |
| --- | --- | --- | --- |
| Opening `chaosx.nr24.2` | `.2.a`, `.2.b`, `.2.c` | Base constants 4.0, 3.0, 2.0. Modifiers use peace 1.8, low-stability 0.5, commercial-stability 1.5, wartime-commercial 0.4, wartime-officer 2.0, low-experience 1.4, supply-crisis 0.25, and severe-crisis factors 8.0, 0.0, 0.25 respectively. | Three options are present in source. MCP did not return `poolComplete` or external-factor coverage. |
| Route report `chaosx.nr24.20` | `.20.a`, `.20.b`, `.20.c` | Each has `ai_chance` base 1. | Three source options are present. Route-trigger resolution and host/event-target gates were not MCP-verified. |
| Incident response `chaosx.nr24.30` | `.30.terrain_a`, `.30.terrain_b`, `.30.supply_a`, `.30.supply_b`, `.30.enemy_a`, `.30.enemy_b`, `.30.template_a`, `.30.template_b`, `.30.diplomatic_a`, `.30.diplomatic_b`, `.30.workplace_a`, `.30.workplace_b`, `.30.party_a`, `.30.party_b` | All bases are 1. Conditional factors are 0.25 for supply-crisis overconfidence, 2.0 and 0.2 for enemy/red-team and enemy/supply, 1.8 and 0.25 for template/separate-policy and template/supply, 1.8 and 0.2 for workplace/protection and workplace/war, and 1.7 and 0.2 for party/democratic and party/supply. | Fourteen source options are present. Their trigger eligibility is affected by the missing exact comparators and is unresolved in MCP. |
| Mandatory reassessment `chaosx.nr24.50` | `.50.a`, `.50.b`, `.50.c` | `.50.a` base 3.5, `.50.b` base 2.0, `.50.c` base 4.0. Raw modifiers include supply factor 2.0, Dual-Track stability factor 1.6, and route factors in the constants group. | Three source options are present. `.50.c` lacks the full affordability predicate described below. MCP option availability was not returned. |
| Incident selection `video_game_in_sweden_roll_incident` | `video_game_in_sweden_incident_{terrain,supply,enemy,template,diplomatic,workplace,party}_weight` | Base random-list weights are 2.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0 in that order. | Seven random-list entries are present. Runtime candidate eligibility depends on scripted triggers, variables, flags, cooldown, and current host state. MCP pool completeness is unknown. |
| Decision category `video_game_in_sweden_program_category` | 18 decisions: `video_game_controlled_exercise`, `video_game_logistics_module`, `video_game_expand_access`, `video_game_conclude_trial`, `video_game_rules_revision`, `video_game_field_validation`, `video_game_red_team`, `video_game_officer_league`, `video_game_national_league`, `video_game_protect_shifts`, `video_game_preparedness_clubs`, `video_game_foreign_licenses`, `video_game_separate_policy`, `video_game_begin_reality_audit`, `video_game_narrow_reality_audit`, `video_game_dual_track`, `video_game_restrict_use`, `video_game_trust_model` | These are `ai_will_do` willingness scores, not click probabilities. Relevant source constants include Logistics base 2.0, Validation Caution 2.5, Audit Crisis 3.5, Restrict Crisis 4.0, Trust Safe 1.5, and Trust Crisis / Trust Low Stability factors 0.0. | All 18 weighted decision definitions are present in the file. Phase-specific eligibility is not complete because the helper comparators are defective and the adapter did not return a decision pool. |

The raw constants above are source values, not evaluated scores or normalized probabilities. No hand arithmetic is used to infer an ordering or share.

The source bases for the 18 decision score candidates, in the order listed above, are `1`, `2`, `1`, `conclude_low_value = 4`, `1`, `validation_caution = 2.5`, `red_team_caution = 2`, `1`, `1`, `1`, `1`, `foreign_interest = 2`, `2`, `audit_crisis = 3.5`, `audit_crisis = 3.5`, `2`, `restrict_crisis = 4`, and `trust_safe = 1.5`. These are the `base` values only. Relevant named modifiers from `common/script_constants/024_video_game_in_sweden_constants.txt:351-458` are listed here without multiplying them into hand-calculated scores.

| Named scenario | Source modifier traces to inspect |
| --- | --- |
| `P24-D1` | Logistics uses supply factor 2.0 and peace factor 0.3, with route factors. |
| `P24-D2` | Field Validation uses supply factor 0.0, low-stability factor 0.5, and mismatch factor 3.0. |
| `P24-D3` | National League uses war factor 2.5, low-war-support factor 2.0, and supply factor 0.35. Protect Shifts uses war factor 3.0 and distraction factor 2.0. |
| `P24-D4` | Foreign Licensing has foreign-interest base 2.0 and war factor 0.2, with route factors. The source decision has no direct blockade / usable-convoy-route trigger. |
| `P24-D5` | Conclude Trial uses peace factor 1.8 and war factor 0.4. |
| `P24-C5`, `P24-C7` | Reality Audit uses supply factor 2.0 and low-stability factor 0.5. Dual-Track uses stable factor 1.8, red-team factor 1.5, and supply factor 0.5. Restriction uses crisis factor 2.0 and peace factor 0.1. Trust the Model uses crisis and low-stability factors 0.0, plus war factor 1.5. Availability gates still determine which candidates exist. |

## Scenario fixture points and completeness

The adapter calls returned no nested scenario schema, so no new adapter JSON fixture was written and no unverified fixture keys were introduced. The numeric enum map above is the source of truth for any later fixture. The route values assigned below are explicit audit assumptions only where the accepted scenario matrix leaves a route unspecified. Keep each named ID and each chosen numeric value unchanged between any future before and after run.

| Named set and scenarios | Phase / route / current incident / last incident fixture point | Additional scenario assumptions and unresolved factors |
| --- | --- | --- |
| `P24_FINAL_OPENING_MATRIX`: `P24-O1` through `P24-O4` | Before route choice: `1 / 0 / 0 / 0`. | The accepted matrix gives qualitative war, stability, experience, supply, and crisis conditions. It does not supply exact numeric values or the full host/event-target binding. Use explicit values from the source gates if fixtures are later built. The prior opening audit is context only, not this fresh baseline. |
| `P24-C1` stable democratic Evolution I | `2 / 1 / 0 / 0` (route 1 is an audit assumption). | Stability, active host binding, affordability, and field / red-team flags need explicit values. |
| `P24-C2` militarized wartime Evolution I | `2 / 3 / 0 / 0` (route 3 is an audit assumption). | War, army experience, supply, validation, and all eligible option triggers need explicit values. |
| `P24-C3` strong-industry, high-tension Evolution II | `3 / 2 / 0 / 0` (commercial route is an audit assumption). | Industry, public reach, stability, policy separation, and route flags need explicit values. |
| `P24-C4` factory and stability crisis | `3 / 2 / 0 / 0` (commercial route is an audit assumption). | The matrix has no numeric stability point. Source crisis and maximum-risk boundaries are 0.20, 0.35, and 0.50 in `constants.txt:336-343`. The exact point must be recorded before evaluation. |
| `P24-C5` Evolution III after supply failure | `4 / 1 / 0 / 2` (route 1 and recent supply incident 2 are audit assumptions). | The matrix says severe supply shortage, core loss, and low fuel or trains, but does not distinguish the persistent `video_game_in_sweden_supply_crisis` flag from the current supply-gap trigger. The latter uses train 3, truck 20, and fuel 100 thresholds at `constants.txt:29-40` and `triggers.txt:223-234`. A current gap blocks Reality Audit start, so the expected Audit-first ordering is unresolved until this state distinction is explicit. |
| `P24-C6` stable, high-Chaos militarized Evolution III | `4 / 3 / 0 / 0` (officer route is an audit assumption). | Stability, supply reserves, active war goal, chaos tier, and all route flags need explicit values. |
| `P24-C7` near capitulation | `4 / 1 / 0 / 0` (route 1 is an audit assumption). | The accepted matrix does not provide surrender progress. The maximum-risk cutoff is strict `< 0.75` at `constants.txt:340` and `triggers.txt:396`. Use a declared value at or above 0.75 to test the invalid branch. |
| `P24-D1` Logistics under train shortage | `1 / 1 / 0 / 0` (baseline controlled route is an audit assumption). | The matrix requires the Logistics action to remain affordable. A live shortage below the 3-train gap threshold conflicts with the 4-train Logistics cost. The scenario must separate a prior crisis flag from current train stock or remain unresolved. |
| `P24-D2` Field Validation after mismatch | `2 / 1 / 0 / 1` (route and recent terrain incident are audit assumptions). | Available divisions, supplied field package, equipment, fuel, trains, and mismatch flags must be explicit. |
| `P24-D3` National League during total mobilization | `3 / 2 / 0 / 0` (commercial route is an audit assumption). | The matrix does not provide numeric factory output or full decision availability inputs. |
| `P24-D4` Foreign Licensing while blockaded | `3 / 2 / 0 / 0` (commercial route is an audit assumption). | Convoy stock, usable convoy access, partner validity, autonomy, and recipient scope must be declared. Source review found no direct blockade or usable-route predicate in the decision gate. |
| `P24-D5` Conclude ignored baseline | `1 / 1 / 0 / 0` (controlled route is an audit assumption). | Program days must be at least the 120-day review threshold, Reliance below 50, and no active mission. The full category pool still needs exact phase filtering. |
| `P24-I1` terrain mismatch | Random-list state before selection: `2 / 1 / 0 / 0`. Conditional `.30` response trace uses `current_incident = 1`. | Declare war or a field exercise, no recent terrain validation, valid host, and any scheduled cooldown change. |
| `P24-I2` train and fuel shortage | Random-list state before selection: `2 / 1 / 0 / 0`. Conditional `.30` response trace uses `current_incident = 2`. | Declare current stockpiles and `has_war`. The source supply-gap trigger requires war plus a train, truck, or fuel threshold breach. |
| `P24-I3` Evolution II public league | Random-list state before selection: `3 / 2 / 0 / 0`. Conditional `.30` response can use `current_incident = 6` for workplace. | Workplace validity needs public reach and Evolution II. The accepted scenario also mentions party appropriation, which is incident 7 and requires its own conditional response trace. |
| `P24-I4` Evolution III diplomacy | Random-list state before selection: `4 / 1 / 0 / 0`. Conditional `.30` response uses `current_incident = 5`. | A meaningful live diplomacy target and active diplomacy flag are required. The matrix does not define the target scope. |
| `P24-I5` repetition control | Random-list state before selection: `2 / 1 / 0 / 2` (incident 2 as the recent-family assumption). | The matrix says one family fired recently but does not name it. The chosen previous family is an explicit audit assumption, not an accepted numeric value. |

The same accepted scenario ID can represent a before-selection random-list state and a conditional response event state only when the report declares the transition explicitly. Do not silently treat these as one identical point in a comparison. Scenario dates, flags, scope bindings, state control, external factors, and scheduled changes were not MCP-validated.

## Comparator findings from the frozen source

The offline wiki's documented default means an omitted `compare` acts as `greater_than_or_equals`. Every finding below is source-level and bounded by that local reference. The MCP could not verify the constructs or the candidate eligibility.

### Phase and route identities

`common/scripted_triggers/024_video_game_in_sweden_triggers.txt:459-499` uses phase constants as enum identities in `video_game_in_sweden_is_baseline`, `video_game_in_sweden_is_baseline_or_evolution_i`, and `video_game_in_sweden_is_baseline_or_early_evolution`, but omits `compare` in each check. Under the documented default, the phase-1 check remains true at phases 2 through 6, and the OR helpers accept every phase from 1 onward instead of only their named phases.

`common/scripted_triggers/024_video_game_in_sweden_triggers.txt:502-524` repeats the omitted comparator in `video_game_in_sweden_next_evolution_disabled`. These are exact phase-state tests, not thresholds.

`events/024_hearts_of_iron.txt:231-255` uses omitted-comparator route tests for `.20.a`, `.20.b`, and `.20.c`. The intended identities are route 1, 2, and 3. The resulting overlap admits lower-numbered route options at later route values, so the candidate denominator and possible close result can be wrong.

`common/scripted_effects/024_video_game_in_sweden_effects.txt:337-385,392-393,933,976,1057,1131,1161,1874-1884` contains additional exact phase or route identity checks without explicit comparators. In particular, `video_game_in_sweden_refresh_stage_idea` checks baseline first at line 340 and then uses `else_if` for later phases. A positive phase value can satisfy the first test, so the source branch order can keep applying the baseline idea rather than the matching evolution idea. Phase-gated evolution entry, commercial-route detection, ordinary aftermath, conclusion, and cleanup paths are also affected.

### Incident identity and repeat control

`events/024_hearts_of_iron.txt:294-407` contains 14 incident response options. Each option tests `video_game_in_sweden_current_incident` against one of the constants 1 through 7 without `compare = equals`. The event trigger itself checks current incident `> 0` explicitly at lines 286-292. The option triggers therefore use threshold semantics where each later incident value can admit earlier incident families. No exact option share or ranking is claimed.

`common/scripted_effects/024_video_game_in_sweden_effects.txt:1905-1929` uses the same omitted exact comparator in `video_game_in_sweden_mark_incident`. The first terrain test accepts any positive incident ID, so later `else_if` marker branches are not reached for those positive values. The family-seen state can therefore diverge from the actual incident identity.

`common/scripted_effects/024_video_game_in_sweden_effects.txt:1950-1955` intends `current_incident = 0` to gate `video_game_in_sweden_roll_incident`. With the documented default, any nonnegative current incident passes this check. If the effect is invoked again before the pending incident is resolved, a new draw can overwrite the pending incident. Whether the maintenance cadence produces that overlap is unresolved without MCP or runtime evidence.

`common/scripted_effects/024_video_game_in_sweden_effects.txt:1991-2051` checks `video_game_in_sweden_incident_alternative_available = 0` inside an OR without an explicit comparator. This variable is initialized and assigned as 0 or 1. The default `>= 0` condition is true for both values, so the OR bypasses the intended last-family exclusion. The seven `last_incident` checks in the same block also omit `compare = equals`. Because they are nested under `NOT`, the documented default makes them directional `<` tests rather than identity exclusions. Both parts need exact semantics for the accepted repetition-control intent.

`common/scripted_effects/024_video_game_in_sweden_effects.txt:2058-2081` checks the 0/1 `incident_pool_available` variable against 1 without an explicit comparator. Given its current 0/1 assignment domain, `>= 1` is equivalent today, so no separate defect is claimed. Explicit equality would make its boolean state contract clear.

### Reassessment affordability and maximum-risk safety

`events/024_hearts_of_iron.txt:647-688` shows `.50.a` requiring both `can_begin_reality_audit` and `can_pay_reality_audit`, and `.50.b` requiring both `can_use_dual_track` and `can_pay_dual_track`. `.50.c` only requires `can_restrict_use` at line 680. `video_game_in_sweden_can_pay_restriction` is a separate trigger at `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:145-149`. It requires at least 30 political power and stability and war support at or above 0.04. The restriction decision includes this payment trigger at `common/decisions/024_video_game_in_sweden_decisions.txt:601-611`, but `.50.c` does not.

The effect `video_game_in_sweden_pay_restriction` at `common/scripted_effects/024_video_game_in_sweden_effects.txt:754-768` conditionally subtracts each resource only when individually affordable, then `video_game_in_sweden_start_restriction` proceeds at lines 1270-1286. Thus `.50.c` can start the route while omitting unaffordable payment components. Add the same affordability predicate to the event option trigger if the owner accepts this narrow repair. No numeric weight change is proposed.

The maximum-risk route source gate is directionally protective. `video_game_in_sweden_is_severe_campaign_crisis` at `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:263-270` catches capitulation, the supply-crisis flag, core-loss crisis, capital threat, or stability below 0.20. `video_game_in_sweden_can_use_maximum_risk_route` at lines 389-405 additionally requires affordability, no current supply gap, no reality-check disqualification, surrender progress below 0.75, and stability above 0.35 at war or above 0.50 at peace. This source gate appears consistent with the accepted requirement that broken supply, severe instability, and near capitulation not favor Trust the Model. The MCP did not confirm scenario eligibility or AI rankings.

## Results classification and risks

| Conclusion | Classification | Evidence limit |
| --- | --- | --- |
| Raw constants, option IDs, random-list entries, and decision IDs | `score-only` source inventory | Read from the frozen BEFORE copies that matched live source hashes. |
| Omitted-comparator effects on enum and sentinel conditions | `bounded` source analysis | Depends on the offline wiki's default-comparator documentation. No installed-doc default or live-engine result was obtained. |
| Conditional `ai_chance` shares for `.20`, `.30`, `.50`, or `.2` | `unresolved` | Required probability inspect and evaluate calls timed out. No candidate eligibility trace, poolComplete value, external-factor resolution, or normalized result returned. |
| Incident random-list probabilities, repetition rate, dominance, and starvation | `unresolved` | The seven source entries are identified, but the dynamic trigger pool and variable values were not evaluated. |
| Decision rankings, rank reversals, or phase-specific starvation | `unresolved` | Decision `ai_will_do` remains a score race. No current decision adapter result returned. |
| Trust the Model validity in P24-C4, C5, C7, or P24-O4 | `bounded` source gate plus `unresolved` scenario result | The source has crisis, supply, surrender, and stability gates. The scenario matrix does not supply all numeric values or target-state bindings. |
| Evolution timing distributions | `unresolved / not applicable to these files` | No `mtth:` or `mean_time_to_happen` construct was found in the audited Event24 event, decision, effect, or trigger files. The current timing path uses day counters and explicit comparisons. |

No exact selection probability, complete MCP candidate pool, dominant option, starvation claim, measured rank reversal, repetition rate, or timing distribution is reported. Raw `ai_will_do` values are not click probabilities. Conditional option shares, if later resolved, remain conditional on the event firing and its complete local option pool.

## Skipped analyses and blockers

`hoi4.probability_evaluate` and `hoi4.probability_sweep` were not called after the required inspect timed out. There is no retained analysis ID or candidate trace to evaluate, sweep, or render.

`hoi4.probability_render` was not called because there is no retained analysis ID. `hoi4.probability_sequence` was not applicable because the incident selector is a native `random_list`, not a declared custom weighted-pool manifest with cadence, transitions, recovery, caps, cooldowns, removals, resets, timers, and terminal states. `hoi4.probability_simulate` was not run because the accepted scenarios declare no distributions, correlations, or seed contract.

`hoi4.probability_compare` was intentionally not run. This is the prepatch baseline pass, no owner patch is present, and comparing the current source to itself would be a fake after-comparison.

No new JSON scenario fixture was created because the exact-state probability inspect timed out before the connected route could return candidate, scope, and nested scenario-field coverage. The report records the exact accepted IDs and source enum values without inventing unsupported fixture keys. The existing foreign-response JSON is a separate surface and is not reused as Event24 C, D, I, or O evidence.

The structural event trace and options render were attempted for `.20`. Both timed out after 600 seconds. The parent-reported root-event lint timeout is not substituted for a returned artifact. No event structural artifact URI or revision is claimed.

## Recommended owner follow-up, without applying changes

1. Add `compare = equals` to checks intended to identify exact phase, route, or incident enum states in `events/024_hearts_of_iron.txt`, `common/scripted_effects/024_video_game_in_sweden_effects.txt`, and `common/scripted_triggers/024_video_game_in_sweden_triggers.txt`. Keep deliberate numeric thresholds such as Reliance, Chaos, elapsed days, stability, and surrender progress on their existing strict or inclusive comparators.
2. Add exact-zero comparisons to the current-incident sentinel and `incident_alternative_available` checks in `video_game_in_sweden_roll_incident`. Add exact identity comparisons to the seven `last_incident` exclusions and the incident family markers.
3. Add `video_game_in_sweden_can_pay_restriction = yes` to `chaosx.nr24.50.c` if the owner accepts consistency with the Restrict decision's existing affordability gate.
4. Clarify whether P24-C5 means a historical supply-crisis flag with the field package recovered, or a current `has_campaign_supply_gap`. The latter blocks `can_begin_reality_audit`, which can conflict with the expected Audit-first ordering. Keep that distinction explicit in the accepted scenario input.

## Compare readiness for the owner-applied patch

Source readiness: the immutable BEFORE source copies are verified and the source-level exact-state findings are complete. Probability readiness: blocked until the connected `hoi4.probability_inspect` route returns. Do not treat this handoff as the required numeric baseline or as balance signoff.

After the owner patch, the auditor should rerun inspect and compare using the same named scenarios and the immutable BEFORE paths in the table above. For each changed weighted surface, use the matching snapshot as `before.path` and the owner-patched current source as `after.path`, with the identical saved scenario set and complete candidate pool. The parent skill notes that compare source objects must use nonempty `path` values without adding `sourceRevision` or `sourceHash` fields. Do not compare current source to itself or substitute an analysis artifact for the BEFORE source.

Preserve the three opening options `.2.a/.2.b/.2.c` with `P24_FINAL_OPENING_MATRIX` and `P24-O1` through `P24-O4`. Preserve all three `.20` route-report options with explicit route enum values 1, 2, and 3, all fourteen `.30` incident response options, and all three `.50` reassessment options including `.50.c`. Preserve all seven incident random-list families with `P24-I1` through `P24-I5` and all 18 decision candidates with `P24-D1` through `P24-D5` plus the applicable crisis choices `P24-C1` through `P24-C7`.

Before claiming exact normalized results, require returned `poolComplete = true`, inspect every `unresolved` input, and declare host scope, valid Swedish state control, affordability, current supply, event flags, and any diplomacy target. For the crisis checks, preserve the source thresholds and state whether `P24-C5` has a current supply gap, whether `P24-C7` has surrender progress at or above 0.75, and whether restriction resources satisfy the 30 political-power and 0.04 stability / war-support floors. If any field remains unsupported, report bounded or unresolved results only.

No numerical balance targets are recommended. The suggested repairs are comparator and availability-consistency repairs only.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, and `chaos-redux-decisions-missions`. No skill was created or updated. No gameplay file was changed and no commit was made.
