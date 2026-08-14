# IW-031 Kosovo weighted-logic audit - current source - 2026-08-09

## Scope and verdict

This is a read-only weighted-logic audit for Event 006 IW-031 Kosovo (KOS).
The audited gameplay surfaces are `common/decisions/006_independence_wave_kosovo_decisions.txt`, `common/ai_strategy/006_independence_wave_kosovo.txt`, and the KOS hooks in the shared `independence_wave_focus_tree` from `common/national_focus/006_independence_wave_focus.txt`.
The supporting eligibility and state-transition sources are `common/scripted_triggers/006_independence_wave_kosovo_package_triggers.txt`, `common/scripted_effects/006_independence_wave_kosovo_package_effects.txt`, `common/script_constants/006_independence_wave_decision_constants.txt`, and `common/script_constants/006_independence_wave_kosovo_constants.txt`.

The mandatory decision `hoi4.probability_inspect` succeeded and proved one ordinary decision candidate, ten required inputs, zero source diagnostics, and an incomplete runtime pool.
The mission, `ai_strategy_factor`, and national-focus probability inspections were attempted after the required inspect-first call, but the MCP transport closed; the strategy attempt also timed out after an internal-error retry.
The matching structural `hoi4.focus_inspect` and `hoi4.focus_render` calls also hit the same transport blocker.

No typed evaluation, ranking, timing, sensitivity, rank-reversal, probability, or rendered evidence is available for the blocked surfaces.
The decision evaluate and sweep were attempted with named empty-state scenarios and then failed with `Transport closed`.
All score statements below are source-declared score traces only; an `ai_will_do` score is a willingness score in a score race, not a click or selection probability.

There is no pre-change source baseline for IW-031, so no `hoi4.probability_compare` was fabricated or run.
No gameplay, AI, decision, mission, focus, strategy, effect, trigger, localisation, or runtime file was changed.

## Source identity

The MCP workspace was `mod_chaos_redux_ea3b2d67c2c0`.
The local repository HEAD observed during the audit was `c369e432e07d0b2181702630863ffce22f51d680`.
Local raw hashes tie this receipt to the current worktree; the MCP revision and hash are authoritative for the one successful MCP receipt.

| Source | Local raw SHA-256 | MCP source revision | MCP source hash |
| --- | --- | --- | --- |
| `common/decisions/006_independence_wave_kosovo_decisions.txt` | `A4A9E251A477DB0CDF16158C3644B2899411D194E160DF2FBE185F4C7C418D51` | `b379748b74ae53455a27bcc85db8371ac4a848235476c2081e4ec9b214512150` | `61b11f4c4102a43c755f473413a5bce2cd8fce4ff37f8eb03fef30d38a735919` |
| `common/ai_strategy/006_independence_wave_kosovo.txt` | `B488AFCD23F245147588880233A098899ED24BA1B8A03D2A3F3B9F86241B106D` | unavailable because the adapter transport closed | unavailable |
| `common/national_focus/006_independence_wave_focus.txt` | `9ACF294ADB8AECAED18B14F16177E1330824F9F8E292A304BDA609645913DC1E` | unavailable because the adapter transport closed | unavailable |
| `common/scripted_triggers/006_independence_wave_kosovo_package_triggers.txt` | `2D5EBDD413F437E9473F78CDBA092A631FC8B0B772A8800B78DEEF23BDED36A8` | supporting source only | not inspected by probability adapter |
| `common/scripted_effects/006_independence_wave_kosovo_package_effects.txt` | `7E85EB35FB437299D8D095A6509312F68EDC7364E2B8DFE54E62E8BCFA8CB5AE` | supporting source only | not inspected by probability adapter |
| `common/script_constants/006_independence_wave_decision_constants.txt` | `D0273EC935B60BD96A73A5A149E910E18AB8CE9EB10703288ABD85583F48A48B` | supporting source only | not inspected by probability adapter |
| `common/script_constants/006_independence_wave_kosovo_constants.txt` | `2699ABD4063D4CC874B2CB7F26BE439B02CCD754A08D6560BC818B5EC53AA2E8` | supporting source only | not inspected by probability adapter |

## MCP inspection receipts and blockers

### Ordinary decision AI

The mandatory call was `hoi4.probability_inspect` with adapter `decision_ai_will_do` and source `{ "path": "common/decisions/006_independence_wave_kosovo_decisions.txt" }`.

- Result code: `PROBABILITY_SOURCE_INSPECTED`.
- Status: `ok`.
- Files scanned: `mod:common/decisions/006_independence_wave_kosovo_decisions.txt`.
- Discovered candidates: `1`.
- Required inputs: `10`.
- Unresolved source diagnostics: `0`.
- `poolComplete`: `false` because eligibility depends on live package, route, capital, resource, and project state.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c1135ed76ada2a5bb6c4f7e302334249b8cabdb8a58f2143cceea9b7eaa4d93/33ea3dd2375368a6419529a4e31eb3aa13a1c205362db1b91d14c1dfb0988960/probability-inspect-61b11f4c4102.json`.

The one ordinary candidate is `independence_wave_kos_codify_durable_sovereignty`.
The other ten project actions have `days_remove` and are therefore listed in the mission pool below; the founding-crisis action is also a mission.

The required decision evaluation was attempted with candidate pool `[independence_wave_kos_codify_durable_sovereignty]` and the named set `E6_IW031_KOS_DECISION_SCENARIOS_CURRENT_2026_08_09_AUDIT` using `state = {}` for each scenario.
The exact result was `tool call error: hoi4_agent_tools/hoi4.probability_evaluate ... Transport closed`.
The matching sweep over `state.has_war` with three steps, pairwise comparison, and rank-reversal detection returned the same exact `Transport closed` error.

### Mission AI

The mandatory `hoi4.probability_inspect` call used adapter `mission_ai_will_do` and the same source path.
The first attempt timed out after the MCP wait window; subsequent retries returned the exact error `tool call error: hoi4_agent_tools/hoi4.probability_inspect ... Transport closed`.
No mission source revision, candidate count, required-input count, scenario hash, analysis id, or artifact was produced by MCP.

The complete source-declared mission pool is:

`independence_wave_kos_hold_cantonal_compact_together`, `independence_wave_kos_secure_mitrovica_depots`, `independence_wave_kos_integrate_territorial_guards`, `independence_wave_kos_register_municipal_compacts`, `independence_wave_kos_settle_former_host_ledgers`, `independence_wave_kos_ratify_agrarian_civic_charter`, `independence_wave_kos_convene_workers_council`, `independence_wave_kos_adopt_federal_cantonal_charter`, `independence_wave_kos_establish_territorial_command`, `independence_wave_kos_codify_durable_sovereignty`, and `independence_wave_kos_open_balkan_network_corridor`.

This eleven-entry list is complete for the declarations in the source file, but its engine candidate pool remains unresolved because the required mission inspect did not return.
The active-project trigger independently enumerates the ten project IDs at `common/scripted_triggers/006_independence_wave_kosovo_package_triggers.txt:95-107`.

### AI strategy factors

The mandatory `hoi4.probability_inspect` call used adapter `ai_strategy_factor` and source `{ "path": "common/ai_strategy/006_independence_wave_kosovo.txt" }`.
An initial attempt returned `INTERNAL_ERROR`; a retry timed out while waiting for the MCP host, and later retries returned the exact `Transport closed` error.
No strategy artifact, factor ranking, scenario hash, or render exists.
This is an adapter-transport/discovery failure, not evidence that the four source-declared strategy blocks are empty.

The four source blocks are `independence_wave_kos_municipal_survival`, `independence_wave_kos_host_restraint`, `independence_wave_kos_settled_compact`, and `independence_wave_kos_emergency_guard`.

### Shared generic focus AI

The probability inspect for adapter `national_focus_ai_will_do` and source `{ "path": "common/national_focus/006_independence_wave_focus.txt" }` first returned `INTERNAL_ERROR` and then returned the exact `Transport closed` error.
The required structural `hoi4.focus_inspect` call for tree `independence_wave_focus_tree` and the matching `hoi4.focus_render` call both returned `Transport closed`.
No focus candidate pool, focus analysis id, scenario hash, layout artifact, or render is available from this turn.

Source review found no ordinary KOS-specific focus IDs.
IW-031 is wired through five shared generic nodes: `independence_wave_prepare_capital_administration` (line 100, KOS assembly hook at line 114), `independence_wave_inventory_the_state` (line 140, KOS community hook at line 155), `independence_wave_bind_the_first_oath` (line 162, KOS guards hook at line 177), `independence_wave_define_former_host_policy` (line 1400, KOS ledger hook at line 1407), and `independence_wave_recognize_fellow_new_states` (line 1670, KOS corridor hook at line 1677).
The country assignment score for the shared tree is urgent when `independence_wave_full_focus_framework` and `is_independence_wave_active_country` are both true (`common/national_focus/006_independence_wave_focus.txt:37-46`).
The focus candidate pool is consequently the large shared generic tree, not a five-node KOS-only pool; it is incomplete and uninspected by MCP in this turn.

## Source-declared candidate scores

The following values are direct source traces using `independence_wave_decision_ai` (`standard = 10`, `high = 25`, `urgent = 100`, `modifier_double = 2`) from `common/script_constants/006_independence_wave_decision_constants.txt:244-259`.
They are nominal willingness scores only.

| Surface and identifier | Base | Declared modifier | Nominal score when modifier condition is true | Eligibility notes |
| --- | ---: | --- | ---: | --- |
| Mission `independence_wave_kos_hold_cantonal_compact_together` | 100 | none | 100 | Activation-backed founding crisis; `available = { always = no }` is intentional and its timeout is 570 days. |
| Mission `independence_wave_kos_secure_mitrovica_depots` | 25 | none | 25 | Project ready, administration-light cost, capital controlled, and no active project. |
| Mission `independence_wave_kos_integrate_territorial_guards` | 25 | x2 when `has_war = yes` | 50 | Project ready, security-standard cost, capital controlled, and no active project. |
| Mission `independence_wave_kos_register_municipal_compacts` | 25 | none | 25 | Project ready, administration-standard cost, capital controlled, and no active project. |
| Mission `independence_wave_kos_settle_former_host_ledgers` | 10 | x2 when `NOT = { has_independence_wave_severe_host_threat = yes }` | 20 calm / 10 severe-host state | Former-host/assembly and unsettled-host branches are mutually state-dependent; living-host war is a cancellation input. |
| Mission `independence_wave_kos_ratify_agrarian_civic_charter` | 25 | none | 25 | Constitutional route available and no route government. |
| Mission `independence_wave_kos_convene_workers_council` | 25 | none | 25 | Popular-council route available and no route government. |
| Mission `independence_wave_kos_adopt_federal_cantonal_charter` | 10 | none | 10 | Traditional route available and no route government. |
| Mission `independence_wave_kos_establish_territorial_command` | 100 | x2 when `has_war = yes` | 200 | Emergency-military route available and no route government. |
| Decision `independence_wave_kos_codify_durable_sovereignty` | 25 | none | 25 | Requires stable compact, founding settlement complete, route government, strategic cost, capital control, and no active project; `fire_only_once = yes`. |
| Mission `independence_wave_kos_open_balkan_network_corridor` | 10 | none | 10 | Stable compact, network member, league route available, diplomatic-standard cost, capital control, and no active project. |

The five shared focus-hook traces use `independence_wave_focus_ai` (`high = 25`, `urgent = 100`, `preferred_factor = 2`, `strong_preference_factor = 4`, and `prerequisite_boost = 1.5`) from `common/script_constants/006_independence_wave_focus_constants.txt:62-80`.

| Shared focus hook | Base | Declared modifier | Nominal score when modifier condition is true | KOS effect |
| --- | ---: | --- | ---: | --- |
| `independence_wave_prepare_capital_administration` | 100 | x4 under severe instability | 400 | Calls `independence_wave_kos_focus_convene_assembly`. |
| `independence_wave_inventory_the_state` | 100 | none | 100 | Calls `independence_wave_kos_focus_guarantee_communities`. |
| `independence_wave_bind_the_first_oath` | 100 | x2 during war | 200 | Calls `independence_wave_kos_focus_integrate_territorial_guards`. |
| `independence_wave_define_former_host_policy` | 25 | x1.5 after `independence_wave_complete_founding_settlement` | 37.5 | Calls `independence_wave_kos_focus_settle_yugoslav_ledgers`. |
| `independence_wave_recognize_fellow_new_states` | 25 | x1.5 after `independence_wave_complete_founding_settlement` | 37.5 | Calls `independence_wave_kos_focus_open_balkan_corridor`. |

The source-declared AI strategy priorities are not a normalized candidate pool.
`independence_wave_kos_municipal_survival` sets build-army 80, infantry production 38, artillery production 20, support production 48, infrastructure construction 72, and bunker construction 68.
`independence_wave_kos_host_restraint` sets `avoid_starting_wars = -240` while a living former host remains unsettled.
`independence_wave_kos_settled_compact` sets build-army 80 and `avoid_starting_wars = -400` after compact stabilization.
`independence_wave_kos_emergency_guard` sets build-army 112 and bunker construction 68 under the emergency-government flag.
The shared KOS constants also declare `corridor_priority = 78` at `common/script_constants/006_independence_wave_kosovo_constants.txt:74-90`, but the current KOS strategy source does not consume that constant.

## Named scenarios and completeness contract

The scenario ids below are deliberately named and use only source-declared triggers, variables, flags, and costs.
The only scenario payload actually submitted in this turn was the decision set with `state = {}` for every row because the adapter did not accept a typed fixture after transport failure.
The empty state does not assert any package, setup, capital, host, route, resource, ledger, active-project, war, network, or focus prerequisite.
The prose contracts therefore document intended test inputs, not successful engine evaluations.

| Scenario id | Source-declared contract | Decision submitted | Mission submitted | Strategy submitted | Focus submitted | External-factor completeness |
| --- | --- | --- | --- | --- | --- | --- |
| `KOS_FOUNDING_CALM` | KOS package and IW-031 setup complete; project-ready; initial civic concord 30 and municipal reach 27; compact not stable; capital controlled; no active project; no war; route-government state not selected. | Yes, empty state only | No, inspect transport blocker | No, inspect transport blocker | No, inspect transport blocker | No, inspect/render transport blocker | Incomplete; all live scopes and affordability values are unasserted. |
| `KOS_HOST_CRISIS` | Package/setup/project-ready; capital controlled; living former host exists and `var:independence_wave_former_host = { has_war_with = ROOT }`; host ledgers unsettled; severe host threat; no active project. | Yes, empty state only | No, inspect transport blocker | No, inspect transport blocker | No, inspect/render transport blocker | Incomplete; host scope and war relation are unasserted. |
| `KOS_ROUTE_LOCKED` | Package/setup/project-ready; stable compact means both concord and municipal reach are at least the declared stable threshold 60; one declared route-government flag matches its route; founding settlement complete; no active project; capital controlled. | Yes, empty state only | No, inspect transport blocker | No, inspect transport blocker | No, inspect/render transport blocker | Incomplete; route flags, settlement completion, and affordability are unasserted. |
| `KOS_NO_VALID_TARGET` | A concrete no-target branch with package/setup absent, which fails `is_independence_wave_kos_project_ready`; other source-declared no-target branches include lost capital, an active project, missing route, failed cost, or missing network phase. | Yes, empty state only | No, inspect transport blocker | No, inspect transport blocker | No, inspect/render transport blocker | Incomplete; the alternative branches were not mixed into one contradictory fixture. |

The intended mission scenario set is `E6_IW031_KOS_MISSION_SCENARIOS_CURRENT_2026_08_09_AUDIT` with the four ids above and the eleven-entry pool listed in this handoff.
The intended strategy scenario set is `E6_IW031_KOS_STRATEGY_SCENARIOS_CURRENT_2026_08_09_AUDIT` with the same four ids and no normalized candidate pool.
The intended focus scenario set is `E6_IW031_KOS_FOCUS_SCENARIOS_CURRENT_2026_08_09_AUDIT` with the same four ids and the complete shared-tree pool to be recovered from a successful focus inspection.
No scenario hash exists for these sets because no successful evaluation completed.

## Validity, dominance, starvation, and exploit-risk findings

The source has an explicit one-active-project lock through `has_independence_wave_kos_active_package_project`, which enumerates all ten project decisions.
That lock prevents simultaneous project starts but also makes the mission race highly state-dependent.
Candidate visibility and availability additionally depend on package identity, IW-031 setup, compact-crisis failure, capital control, route availability, route-government status, host scope and war relation, network membership, stable ledgers, founding-settlement completion, project resources, and the active-project lock.

The activation-backed founding mission has `available = { always = no }` and is not a dead choice by itself; it is started by activation and removed by timeout or cancel effects.
An empty-state evaluation would therefore be expected to report it as never eligible, but that would be an artifact of missing setup state rather than proof of starvation.

The former-host ledger project has a source-level cancellation/availability interaction that needs a typed test.
Its availability permits the assembly-plus-unsettled-host branch, while its cancellation trigger ends the mission when the living former host is at war with KOS; its cancel effect then applies either host-loss settlement or project failure depending on the remaining state.
No probability or exploit conclusion is justified until that branch is evaluated with an actual former-host scope.

The emergency territorial-command score reaches nominal 200 during war and the guards integration score reaches nominal 50 during war, but their route, cost, project-lock, and capital gates can remove them from the race.
The ordinary sovereignty decision has a positive nominal score of 25 despite strict stable-compact, founding-settlement, route-government, strategic-cost, and one-shot gates; positive source score is not proof of a valid candidate.

The four AI strategy blocks have independent enable conditions.
Municipal survival and host restraint can overlap during founding, and settled compact can coexist with emergency guard if their flags are simultaneously present; the strategy adapter did not return, so no rank or factor-composition claim is made.
The declared `corridor_priority = 78` constant is not consumed by the current KOS strategy source and should be reviewed for dead tuning or an intentionally deferred network factor.

Because the ordinary decision adapter exposed one candidate, there is no ordinary-decision rank race to analyze.
Mission dominance, mission starvation, focus rank reversal, strategy dominance, repetition, and snowball/exploit risk are unresolved rather than disproven.

## Analyses run, skipped, and exact blockers

- `hoi4.probability_inspect` for `decision_ai_will_do`: completed successfully with the artifact and source identity recorded above.
- `hoi4.probability_inspect` for `mission_ai_will_do`: first call timed out; retries returned `Transport closed`.
- `hoi4.probability_inspect` for `ai_strategy_factor`: initial call returned `INTERNAL_ERROR`; retry timed out; later calls returned `Transport closed`.
- `hoi4.probability_inspect` for `national_focus_ai_will_do`: initial call returned `INTERNAL_ERROR`; retry returned `Transport closed`.
- `hoi4.probability_evaluate` for the named decision scenarios: attempted after inspection and returned `Transport closed`.
- `hoi4.probability_sweep` for the decision war-state path with three steps, pairwise, and rank-reversal detection: attempted and returned `Transport closed`.
- `hoi4.focus_inspect`: attempted for `independence_wave_focus_tree` and returned `Transport closed`.
- `hoi4.focus_render`: attempted for the same tree and returned `Transport closed`.
- `hoi4.probability_render`: skipped because no evaluation analysis id or scenario hash exists.
- `hoi4.probability_compare`: intentionally skipped because IW-031 is a new source with no before baseline; fabricating a baseline is forbidden.
- `hoi4.probability_simulate`: skipped because no uncertain-input distributions, seed, or typed state fixture were declared.
- `hoi4.probability_sequence`: skipped because the scoped files do not declare a complete custom weighted pool with cadence, cooldown/recovery, removal/reset, cap, timer, and terminal-state manifest.
- Event, GUI, technology, doctrine, and random-list adapters: out of scope; no such weighted surface is declared by the named IW-031 files.

## Recommended owner follow-up

1. Restore the HOI4 MCP probability and focus transports, then rerun the exact inspect-first workflow against the three named source files and preserve the returned revisions, artifacts, scenario hashes, and rendered unresolved/ranking evidence.
2. Supply a typed KOS fixture for package identity, IW-031 setup, state 802 ownership/control and capital scope, former-host event target and war relation, concord and municipal ledgers, route flags and installed government, league/network phase, resource affordability, active-project flags, one-shot flags, focus prerequisites, and strategy-enable flags.
3. Re-run the four named scenario ids with the complete eleven-entry mission pool and the complete shared-focus pool recovered from MCP; classify output as score-only or bounded until all external factors resolve.
4. Add a sensitivity path for `has_war`, severe host threat, capital control, and active-project/route gates once typed scenarios are available, then render ranking and unresolved views.
5. Review `common/script_constants/006_independence_wave_kosovo_constants.txt:89` (`corridor_priority = 78`) against `common/ai_strategy/006_independence_wave_kosovo.txt`; either wire an owner-approved network strategy factor or document the constant as intentionally unused.
6. Test the former-host living/war and assembly/unsettled branches as separate typed scenarios so cancellation and host-loss settlement cannot silently starve or prematurely fail the project.
7. After an owner-applied AI change creates a real before revision, run `hoi4.probability_compare` with the same scenario ids and candidate pools; do not compare this new source to an invented baseline.

## References consulted

The required offline Paradox wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, and national-focus modding.
The required vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` was consulted for triggers, effects, modifiers, script concepts, dynamic variables, decisions/missions, and national-focus/AI behavior.
The repository skills `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-focus-trees/SKILL.md` were read before the audit.
