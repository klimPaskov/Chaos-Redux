# Event 021 Random Civil War — AI and probability audit

> **Historical baseline notice.** This is the 2026-08-29 pre-change read-only audit. Its minimal-implementation assessment and unavailable-route statements are retained for provenance and are not the current Event 021 status. Current targeted probability evidence and the remaining named-matrix gate are recorded in `docs/events/021_random_civil_war/acceptance_evidence.md` and `docs/plans/021_random_civil_war_plans/post_fix_improvement_loop_closure_addendum_2026-08-31.md`.

Audit timestamp: 2026-08-29 20:34:20 +03:00 (Europe/Kyiv). This is a read-only pre-change audit. No gameplay, AI, event, focus, decision, mission, localisation, or runtime file was edited.

## Scope and evidence status

Audited surface: Event 021 `chaosx.nr21.1`, its random-event registration and dispatch, the intended Wars cluster relationship with Events 004 and 007, Event 006 package/AI surfaces, target validity and pressure requirements, severity and evolution timing, neighbor exposure, queue/cooldown behavior, scenario intensity, decisions/missions, sponsor/settlement/recurrence roles, and the Event 021 probability scenario matrix.

The current implementation is a minimal hidden, triggered-only event. It does not implement the Event 021 design described by the specification package. Numerical conclusions about the live game are therefore either `score-only` (a literal source weight) or `unresolved` (engine probability/timing not proven).

## HOI4 MCP availability

The mandatory first call was attempted before treating source inspection as evidence:

```text
tool: mcp__hoi4_agent_tools__hoi4_probability_inspect
adapter: event_mean_time_to_happen
refresh: true
result: MCP tool `hoi4_agent_tools/hoi4.probability_inspect` is not available to the model
```

The tool catalogue exposed the probability route names, but the callable route returned the exact availability error above after the baseline attempt. No MCP artifact URI, revision, scenario hash, analysis ID, comparison ID, or rendered evidence path was produced.

Per the audit contract, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, `hoi4.probability_compare`, and `hoi4.probability_render` were not substituted with hand calculations. They remain unavailable engine evidence for this audit. The required event structural inspect/render evidence was likewise not available through the exposed model route at this checkpoint. The parent must rerun the full probability and event structural passes when those routes are callable.

## Files and references reviewed

The repository instructions and the Chaos Redux subagent, events, MTTH, and event-planning skills were read before the audit. The complete `docs/specs/021_random_civil_war_specs/` package was reviewed, including `README.md`, `MANIFEST.sha256`, the master spec, parts 1–10, the probability scenario matrix, country package matrix, research notes, source-read ledger, role review, revision notes, overlap/catalog reconciliation, package manifest, goal/coding/decision-mission/asset/achievement prompts, and implementation handoff material.

Relevant current source surfaces reviewed:

- `events/021_random_civil_war.txt::chaosx.nr21.1`.
- `common/scripted_effects/chaosx_logic_effects.txt::initialize_all_events_array`, `::initialize_default_disabled_events_for_rework_queue`, `::initialize_event_weights`, `::evaluate_event_pool_candidate_unavailability`, `::evaluate_random_event_active_pool_candidate`, `::update_repeatable_event_weights`, and `::get_event_weight`.
- `common/scripted_effects/chaosx_settings_effects.txt::evaluate_random_event_selection_candidate`, `::select_weighted_random_event_id`, `::fire_event_by_temp_id`, `::random_war_setup_context`, and `::fury_prepare_random_event_fire`.
- `common/on_actions/chaosx_on_actions_system.txt` daily timer and weighted event dispatch.
- `events/004_random_war.txt`, `common/scripted_effects/004_random_war_effects.txt`, `common/scripted_triggers/004_random_war_triggers.txt`, and `common/script_constants/004_random_war_constants.txt`.
- `events/007_fury.txt`, `common/scripted_effects/007_fury_effects.txt`, `common/scripted_triggers/007_fury_triggers.txt`, `common/decisions/007_fury_decisions.txt`, and `common/script_constants/007_fury_constants.txt`.
- `events/006_independence_wave.txt`, `events/006_independence_wave_support_events.txt`, `common/scripted_effects/006_independence_wave_effects.txt`, the `common/scripted_effects/006_*` and `common/scripted_triggers/006_*` helpers, `common/decisions/006_independence_wave_decisions.txt`, `common/decisions/006_independence_wave_shared_decisions.txt`, `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, `common/on_actions/006_*`, `common/mtth/006_independence_wave_evolution_mtth.txt`, and `common/script_constants/006_independence_wave_constants_registry.txt`.
- `events/chaosx_event_clusters.txt`, `common/scripted_effects/chaosx_event_cluster_effects.txt`, and `common/script_constants/event_cluster_constants.txt`.
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`, `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`, and `common/script_constants/chaosx_triggerable_scenarios_constants.txt`.
- `common/mtth/chaosx_mtth_variables.txt` and the current Event 021 localisation/event-log references.

Required offline references reviewed:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`.
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`.

Relevant installed vanilla documentation reviewed:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_math_functions.md`.

The references establish the distinctions used below: `ai_will_do` and `ai_chance` are weighting scores for a valid competition; MTTH is a timing distribution; a `random_list` is proportional only over the positive entries in the actual evaluated list; and the event-system selector is a probability-proportional draw only after the complete active candidate pool and all modifiers are known.

## Pre-change source findings

### Event 021 itself

`events/021_random_civil_war.txt::chaosx.nr21.1` calls `random_country` and then evaluates four literal `random_list` entries, each with base weight `25` and `start_civil_war = { size = 0.5 }` for fascism, democracy, communism, or neutrality.

Each branch has only one zeroing modifier tied to the selected country's current government. The communism branch additionally requires `has_global_flag = communism_spread` together with `has_government = communism`. No branch checks opposition, territory, leadership, army access, safe capital, package completeness, civil-war collision, cooldown, recent victory, successor grace, actual-nonhuman status, or terminal state.

The four `25` values are a literal branch score, not an Event 021 target probability. Conditional on a fully known target and all four positive branches, the local list would be proportional to those four values; however, the source does not establish that the selected country is valid or that each `start_civil_war` call succeeds. The branch result is therefore `score-only`, and every target/archetype probability is `unresolved`.

There is no Event 021 `ai_chance`, `ai_will_do`, MTTH entry, severity weight, Fracture Pressure score, role-specific AI, decision, mission, sponsor score, settlement score, recurrence score, evolution resolver, or neighbor exposure resolver in the current source.

### Shared random-event queue

`chaosx_logic_effects.txt::initialize_all_events_array` combines major, fire-once, and repeatable event arrays. Event 021 is listed as repeatable in the current event-category registration, but no Event 021-specific availability branch or target-preparation branch was found in `evaluate_event_pool_candidate_unavailability` or `fire_event_by_temp_id`.

`initialize_default_disabled_events_for_rework_queue` disables any event that is not accepted by `event_log_event_is_reworked_default_enabled`. No Event 021 allowlist mapping was found in the current helper surface, so automatic participation is expected to remain disabled until explicit registration is added. This is a source-level registration finding, not a live-state claim.

`chaosx_settings_effects.txt::evaluate_random_event_selection_candidate` checks the active event pool, repeatability, disabled state, and `get_event_weight`. `select_weighted_random_event_id` then scans the complete valid `global.all_events` array, sums scaled weights, rolls once, and selects by cumulative weight. This is a probability-proportional event draw, not a comparison of Event 021's isolated weight with a click probability.

`chaosx_on_actions_system.txt` invokes that selector when the event timer expires. Because the generic dispatcher has no Event 021 prefire validator, a forced or otherwise directly dispatched `chaosx.nr21.1` can reach the broad `random_country` implementation without the target and route gates required by the spec.

Repeatable weights recover toward their per-event cap through `update_repeatable_event_weights`, while cluster pacing, cooldown flags, disabled events, and fired-state handling alter the live pool. The MCP adapter was unavailable, so no baseline Event 021 weight, cap, timer, conditional launch chance, cumulative chance, or timing distribution can be reported.

### Event 004 comparison

`events/004_random_war.txt` contains option `ai_chance` bases `80` and `20` for the aggressor response and `70` and `30` for the target response. These are option weights after validity, not direct player-click probabilities.

`004_random_war_effects.txt::random_war_select_pair` first makes a 1–100 special roll using stage-dependent chances and then tries special, major, neighbor, and global selectors in sequence. `004_random_war_triggers.txt` checks sovereign status, capitulation, recent flags, wars, alliances, subjects, declaration legality, scale, and cooldown-related flags. The pair selector is a priority/fallback process over nested `random_country` and `random_other_country` calls, not one normalized pair pool. Exact pair probabilities and timing are unresolved without the adapter and a complete live country pool.

### Event 007 comparison

`007_fury_triggers.txt::fury_can_be_selected` and `::fury_is_valid_target` provide explicit actor, nonhuman, recent-actor, player-link, state-count, and target validity gates. `007_fury_effects.txt::fury_select_weighted_actor_candidate` and `::fury_target_score` provide a weighted candidate stage. Current target-score constants include `base_neighbor = 10`, `one_state_bonus = 8`, `two_state_bonus = 4`, `weak_industry_bonus = 5`, `target_at_war_bonus = 3`, `faction_penalty = 9`, `major_penalty = 20`, `momentum_bonus = 1`, `preparation_bonus = 2`, `evolution_i_bonus = 2`, and `evolution_iii_bonus = 4`, with further pressure, equipment, overextension, churn, and rival modifiers in the same constant group.

Fury decisions use file-scoped bases `low = 2`, `medium = 5`, and `high = 10`, with context multipliers such as `factor = 2` and route/pressure zeroing. Those are decision willingness scores and do not establish Event 021 probabilities. No Event 021 target or role uses these Fury selectors today.

### Event 006 comparison

Event 006 has a much more complete package gate and role/route surface. Its decision AI constants are `blocked = 0`, `very_low = 2`, `low = 5`, `standard = 10`, `high = 25`, `urgent = 100`, with `modifier_half = 0.5`, `modifier_double = 2`, and `modifier_major = 5` in `006_independence_wave_constants_registry.txt`. Current decision files apply these scores with route, host-threat, legitimacy, pressure, major-owner, capacity, and war-state modifiers.

Event 006 also has a dedicated evolution MTTH entry in `common/mtth/chaosx_mtth_variables.txt` and package/anchor/territory/leader/capacity checks across its scripted triggers and effects. This is a useful structural precedent, not evidence that Event 021 currently inherits those weights. Event 006 option and decision weights remain `score-only` without a complete competing-option pool and live trigger state.

### Cluster and scenario surfaces

`chaosx_event_cluster_effects.txt::event_belongs_to_cluster` currently maps Event IDs `4` and `7` to `constant:event_cluster_id.wars`. `load_event_cluster_members` currently defines the Wars rows for Event 004 (`wars_random_war`, required, low danger) and Event 007 (`wars_fury`, optional, medium danger). Event 021 is not mapped into this live cluster member definition, despite the specification's intended three-member Wars cluster.

The current cluster layer has global cooldown/pacing, required-versus-optional member status, eligibility, danger, base/final chance, roll, skipped status, and pending queue metadata. Since Event 021 has no row, no cluster participation, optional roll, collision reservation, or cluster-specific target chance can be measured.

The triggerable-scenario registry contains the existing scenario families and does not expose a verified Event 021 `The Fracture Cascade` / `SCN-014` entry in the reviewed current source. The spec itself says that identifier must be verified against the live registry/export. All Event 021 intensity values are therefore design targets only.

## Required scenario matrix and pre-change result

Pool codes: `P1` means no Event 021 candidate pool or resolver exists in source; `P2` means a related shared surface exists but the complete live pool and external factors are unavailable; `P3` means the specification requires an exact-zero gate that current source does not implement. `U` means unresolved engine result. `S` means score-only source evidence.

All rows below require MCP scenario hashes and complete candidate pools before an exact or bounded probability claim. No row received a probability, ranking, timing, sensitivity, simulation, sequence, comparison, or render artifact in this audit.

### Target selection (`TGT`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| TGT-01 | Stable minor without organized opposition versus unstable minor with valid opposition; valid opposition should materially outweigh stable minor. | No target or opposition resolver; `random_country` is broad. | P1 / U |
| TGT-02 | Unstable minor versus stable major after Evolution I; minor remains favored unless major pressure is extreme. | No pressure, major allowance, or Evolution I target modifier. | P1 / U |
| TGT-03 | Stable minor versus unstable major after Evolution I; major is a real candidate but does not automatically dominate. | No major candidate policy or pressure score. | P1 / U |
| TGT-04 | Recent Event 021 target versus comparable fresh country; fresh country strongly favored. | No recent-target flag, cooldown, or successor grace. | P3 / U |
| TGT-05 | Player versus comparable AI after valid player/AI factors; neither receives an artificial boost. | No Event 021 player/AI factor surface. | P1 / U |
| TGT-06 | One complete actor versus three complete actors at similar pressure; multi-actor case moderately favored after Evolution I. | No actor completeness or actor-count scoring. | P1 / U |
| TGT-07 | Country near an active Event 021 war versus distant country during Evolution II; neighbor favored. | No active-war neighbor exposure. | P1 / U |
| TGT-08 | Actual nonhuman versus normal human; nonhuman exactly zero. | No nonhuman exclusion in Event 021. | P3 / U; positive-route risk |
| TGT-09 | Human Event 006 after grace versus ordinary human; both valid. | No Event 006 grace or Event 021 target validation. | P1 / U |
| TGT-10 | Country inside incompatible bespoke civil war versus valid country; incompatible target exactly zero. | No incompatible-civil-war gate. | P3 / U; positive-route risk |

### Archetype selection (`ARC`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| ARC-01 | Strong excluded ideology yields ideological uprising. | Only ideology branches exist; no exclusion/organization test. | P1 / U; branch S |
| ARC-02 | Disputed succession and two legal institutions yield rival legal route. | Rival legal route absent. | P1 / U |
| ARC-03 | Low command loyalty and several districts yield broad command schism. | Command-schism route absent. | P1 / U |
| ARC-04 | Complete Event 006 package and strong region yield Event 006 independence. | Event 006 route dispatch absent from Event 021. | P1 / U |
| ARC-05 | Coherent region without package/autonomy yields temporary secession. | Temporary-secession route absent. | P1 / U |
| ARC-06 | One-state target yields same-tag takeover. | One-state routing absent. | P1 / U |
| ARC-07 | Equal blocs after Evolution I yield a multi-front mix without actor starvation. | Multi-front and actor-cap logic absent. | P1 / U |
| ARC-08 | Incomplete Event 006 package has exactly zero Event 006 route weight. | No Event 006 package-completeness gate. | P3 / U; positive-route risk |

### Severity (`SEV`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| SEV-01 | High stability, intact administration, and no war yield Limited. | No severity score or stability/war input. | P1 / U |
| SEV-02 | Moderate instability and valid opposition yield Serious. | No severity layer. | P1 / U |
| SEV-03 | Low stability, long external war, and occupied cores yield Severe. | No severity layer or occupied-core input. | P1 / U |
| SEV-04 | Several actors and low authority after Evolution I permit Critical multi-front. | No authority, actor count, or front layer. | P1 / U |
| SEV-05 | Stable one-state target yields Limited same-tag crisis. | Same-tag route and severity absent. | P1 / U |
| SEV-06 | Extreme major pressure yields Severe/Critical, not automatic destruction. | No major pressure or non-destruction cap. | P1 / U |

### Evolution timing (`EVO`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| EVO1-01 | Large stalemated war, low authority, and an extra actor accelerate Evolution I. | No Event 021 evolution timer or MTTH entry. | P1 / U |
| EVO1-02 | Near defeat with no extra region gives slow or unresolved Evolution I. | No Event 021 evolution timer. | P1 / U |
| EVO2-01 | Long border, sponsors, and surviving independence accelerate Evolution II. | No Event 021 neighbor/sponsor MTTH. | P1 / U |
| EVO2-02 | Early settlement and strong neighbors slow or suppress active spread. | No settlement/neighborhood timing layer. | P1 / U |
| EVO3-01 | Evolution III is normally available during a live severe war. | No Event 021 Evolution III gate or timer. | P1 / U |
| EVO3-02 | Evolution III already active before first Event 021 follows prefire global rules without duplicate history. | No prefire/global Event 021 state handling. | P3 / U |

### Front and actor count (`FRT`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| FRT-01 | Small coherent region yields two belligerents. | Fixed ideological split only; no regional actor count. | P1 / U |
| FRT-02 | Medium case with two valid regions yields three actors after Evolution I. | No region or actor-count resolver. | P1 / U |
| FRT-03 | Major with four actors and capacity yields three to five actors within cap. | No actor cap or major capacity logic. | P1 / U |
| FRT-04 | Large map with one valid leader does not create a fake actor. | No leader/territory validity. | P3 / U; fake-actor risk |
| FRT-05 | Two overlapping Event 006 packages select one valid package or another archetype without collision. | No Event 006 package collision handling. | P3 / U |

### Sponsor and external support (`SPN`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| SPN-01 | Rich neutral major with one aligned viable side gives moderate support. | Sponsor role and support score absent. | P1 / U |
| SPN-02 | Desperate war and low equipment give little or no support. | Sponsor capacity inputs absent. | P1 / U |
| SPN-03 | Rival sponsors and two viable sides produce competitive support within caps. | No sponsor competition or cap. | P1 / U |
| SPN-04 | Side without administration or survival is suppressed for recognition and large aid. | No recognition/administration/survival gate. | P3 / U |
| SPN-05 | Neutral mediator suppresses military support and favors mediation. | Mediator role absent. | P1 / U |

### Strange-event timing and selection (`STR`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| STR-01 | New baseline side Rising is very low. | No strange-event surface exists for Event 021. | P1 / U |
| STR-02 | Long-lived, low-authority, high-chaos state is higher but bounded. | No strange-event weight or cap. | P1 / U |
| STR-03 | Active incident is exactly zero. | No active-incident exclusion. | P3 / U; repetition risk |
| STR-04 | Cooldown is exactly zero. | No Event 021 cooldown. | P3 / U; repetition risk |
| STR-05 | Disabled evolution is exactly zero. | No evolution-disabled gate. | P3 / U |

### Settlement (`SET`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| SET-01 | Dominant government and high authority favor military or firm negotiated settlement. | No settlement options or role AI. | P1 / U |
| SET-02 | Independence controls homeland and is recognized; independence/autonomy favored. | No settlement route. | P1 / U |
| SET-03 | Equal fronts and exhaustion favor coalition, partition, or separate peace. | No front/exhaustion settlement score. | P1 / U |
| SET-04 | Hardliner with low legitimacy can repress, with recurrence cost. | No hardliner or recurrence coupling. | P1 / U |
| SET-05 | Negotiator with enforceable guarantee favors durable agreement. | No negotiator/guarantee validity. | P1 / U |
| SET-06 | No viable state makes settlement route invalid. | No viable-state gate. | P3 / U |

### Recurrence (`REC`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| REC-01 | Negotiated/disarmed settlement with high authority gives very low recurrence. | No recurrence score or settlement memory. | P1 / U |
| REC-02 | Harsh settlement, surviving underground network, and low authority give high recurrence after cooldown. | No network, authority, or cooldown model. | P1 / U |
| REC-03 | Recent victory or successor grace makes recurrence exactly zero. | No grace or victory exclusion. | P3 / U; repetition risk |
| REC-04 | Resolved partition/armistice gives low to moderate recurrence based on violations. | No partition/violation state. | P1 / U |
| REC-05 | Broken guarantee strongly increases recurrence. | No guarantee state. | P1 / U |
| REC-06 | Actual nonhuman recurrence is exactly zero. | No nonhuman exclusion. | P3 / U |

### Global queue (`GLB`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| GLB-01 | Critical valid major enters the queue early. | Event 021 has no valid-target or critical queue adapter. | P1 / U |
| GLB-02 | Fractured country with no actor cannot enter the queue. | No actor gate; generic event-level selector has no Event 021 prefire check. | P3 / U; positive-route risk |
| GLB-03 | Stable country waits through review and does not launch immediately. | No Fracture Pressure or review timer. | P1 / U |
| GLB-04 | Critical but theater-cap-blocked country stays Critical and launches after capacity. | No theater-cap state or deferred Event 021 context. | P1 / U |
| GLB-05 | Annexed queued country is removed. | No Event 021 queue state or annexation cleanup. | P3 / U |
| GLB-06 | Human Event 006 after grace remains valid. | No Event 006 grace integration. | P1 / U |
| GLB-07 | Nonhuman is excluded. | No nonhuman gate. | P3 / U; positive-route risk |

### Cluster participation (`CLU`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| CLU-01 | Calm world can produce separated Events 004, 007, and 021 targets. | Live Wars cluster contains only 004 and 007; 021 has no row. | P1 / U |
| CLU-02 | Rising/high-pressure external target permits intentional overlap. | No Event 021 cluster participation or overlap rule. | P1 / U |
| CLU-03 | New Fury actor cannot be an Event 021 target in the same transaction. | No cross-member reservation for Event 021. | P3 / U |
| CLU-04 | Event 006 tag reservation causes reroll/skip. | No Event 021 cluster/package collision check. | P3 / U |
| CLU-05 | No valid Event 021 target skips with a reason while the cluster continues. | No Event 021 member, skip reason, or prefire resolver. | P1 / U |

### Scenario intensity (`SCN`)

| ID | Spec case | Pre-change source assessment | Pool / result |
|---|---|---|---|
| SCN-01 | Political Fracture Low, approximately 10%, mostly minors and one opponent. | Scenario registry/launch and Event 021 intensity are absent. | P1 / U |
| SCN-02 | Independence Cascade Medium, approximately 25%, with regular Event 006 participation. | No Event 021 scenario adapter or Event 006 insertion. | P1 / U |
| SCN-03 | Command Collapse High, approximately 50%, with majors and multi-front behavior. | No Event 021 intensity, command route, or multi-front layer. | P1 / U |
| SCN-04 | Universal Fragmentation Maximum commits every eligible normal human. | No maximum scenario or complete eligible-human pool. | P1 / U |
| SCN-05 | Any scenario type excludes actual nonhumans. | No nonhuman exclusion. | P3 / U; positive-route risk |
| SCN-06 | Any scenario with one-state target uses same-tag crisis. | No one-state route. | P1 / U |
| SCN-07 | Maximum measured stall locks deterministic batches of no more than seven days. | No Event 021 plan lock, batch cadence, or terminal-state sequence. | P1 / U |

## Findings for parent review

1. The current Event 021 target selection is not a weighted target competition. It is `random_country` followed by a four-entry ideology list. It can select a country without valid opposition and can attempt a route that the specification requires to be exactly zero.

2. Event 021 has no current AI decision or mission surface. The Event 004 option weights, Event 006 decision constants, and Event 007 Fury score/decision constants are comparison evidence only and must not be copied as Event 021 probabilities without a declared candidate pool and role-specific validity.

3. The global random-event selector is a complete-pool probability-proportional sampler in source, but Event 021 is not visibly enabled or specially prepared in the current registry/dispatcher. Its isolated default event weight cannot be converted into launch probability without live caps, disabled state, timer, cluster pacing, and all other event candidates.

4. Event 021 is absent from the current Wars cluster member mapping. The intended cluster behavior, required/optional status, base chance, collision reservations, skip reasons, and queue cadence cannot occur until the member row and event mapping exist.

5. No Event 021 MTTH or custom weighted-pool manifest exists. Evolution timing, recurrence timing, neighbor exposure, and global queue behavior are all unresolved rather than zero or balanced.

6. Main exploit and balance risks are invalid positive targets, nonhuman participation, same-transaction Fury/Event 021 collision, Event 006 package collision, no-actor launch, target repetition, target starvation caused by broad uniform country selection, and a misleading assumption that literal `25`, `80`, `70`, `10`, `25`, or `100` values are campaign probabilities.

## Concrete recommended fixes, not applied

- Add an Event 021 target-validity and route-validity layer in new or designated `common/scripted_triggers/021_random_civil_war_triggers.txt` and `common/scripted_effects/021_random_civil_war_effects.txt`. It should make actual nonhumans, terminal countries, incompatible bespoke wars, missing opposition, missing territory/leader/force, active incidents, cooldowns, successor grace, and incomplete Event 006 packages zero before any positive score enters the pool.
- Centralize Event 021 pressure, severity, archetype, actor-cap, neighbor, sponsor, recurrence, cooldown, recovery, and scenario-intensity values in `common/script_constants/021_random_civil_war_constants.txt`. Add explicit MTTH entries to the appropriate `common/mtth/` source only for declared timing distributions, with cadence, reset, cap, removal, and terminal behavior documented.
- Add an Event 021 prefire resolver to `common/scripted_effects/chaosx_settings_effects.txt::fire_event_by_temp_id` or its designated helper so automatic and forced dispatch share the same valid target/context contract. Do not let the generic dispatcher fall through to an unvalidated `random_country` call.
- Register Event 021 deliberately in `common/scripted_effects/chaosx_logic_effects.txt`, including default availability, event weight/cap behavior, target context, fired/recovery state, and cleanup. Verify the registration with the live probability adapter before making a launch claim.
- Extend `common/scripted_effects/chaosx_event_cluster_effects.txt::event_belongs_to_cluster` and `::load_event_cluster_members`, plus `common/script_constants/event_cluster_constants.txt`, with the accepted Event 021 Wars row, required/optional role, danger, base chance, cooldown, collision reservation, and explicit skip reason. Preserve the single global pacing update for the cluster.
- Add Event 021's role-specific decision/mission AI with centralized constants and validity gates for consolidator, hardliner, negotiator, revolutionary, constitutional, independence, command, sponsor, containment, neutral mediator, and survivalist successor. Keep willingness-score evidence separate from target-selection and event-launch probability evidence.
- Register and verify the accepted Event 021 triggerable scenario identifier, including Low/Medium/High/Maximum intensity, normal-human eligibility, one-state routing, actor/front caps, and the measured-stall batch lock. The spec's possible `SCN-014` identifier must not be assumed until the live registry/export confirms it.
- After implementation, rerun the baseline and the exact same IDs above through `hoi4.probability_inspect`, `probability_evaluate`, threshold/rank `probability_sweep`, and rendered evidence. Use `probability_simulate` only for explicitly declared uncertain inputs, `probability_sequence` only after the complete cadence/state manifest exists, and `probability_compare` for the owner-applied before/after patch.

## Skipped analyses, blockers, and remaining uncertainty

- Skipped all numerical probability, timing, sensitivity, rank-reversal, sampled, sequence, comparison, and render claims because the mandatory baseline `hoi4.probability_inspect` route returned `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`.
- No exact candidate pool was available for countries, ideology/archetype routes, event IDs, decisions, missions, cluster members, sponsors, neighbors, settlement options, recurrence options, or scenario intensity. The source snippets cannot supply missing runtime state.
- No seed, scheduled state transition, active-war snapshot, pressure values, authority values, cooldown values, caps, queue contents, cluster roll, or terminal-state sequence was available.
- The Event 021 source itself has no implementation for most named surfaces, so “unresolved” means both engine evidence is missing and the pre-change code does not express the requested behavior. It must not be read as a balance pass or as evidence that the desired zeroes/ratios already hold.
- Parent follow-up remains required after implementation: obtain callable MCP probability and event structural adapters, preserve their artifact URIs/revisions/scenario hashes, and compare the same named scenario IDs before accepting any balance conclusion.

## Current-revision read-only audit — 2026-08-31 (Europe/Kyiv)

This append-only section records a fresh probability and structural MCP pass and preserves the historical provenance above.

This audit used only the current fork context with no inferred parent history and no subagent context.

No gameplay, localisation, asset, GFX, GUI, focus, country, event, decision, mission, or spreadsheet file was edited.

The only file changed by this audit is this handoff, as explicitly authorized by the parent request.

This section is not a gameplay-completion or release-certification claim.

### Audited surfaces and source snapshot

The Event 021 root is `events/021_random_civil_war.txt::chaosx.nr21.1`.

The decision and mission source is `common/decisions/021_random_civil_war_decisions.txt`.

The rare strange-incident source is `common/scripted_effects/021_random_civil_war_parent_effects.txt::event021_parent_roll_strange_incident`.

The decision and mission tuning source is `common/script_constants/021_random_civil_war_constants.txt::event021_ai` and `::event021_mission_tuning`.

The strange-incident tuning source is `common/script_constants/021_random_civil_war_constants.txt::event021_parent_tuning`.

The related strategy source inspected for external weighted factors is `common/ai_strategy/021_random_civil_war_ai_strategy.txt`.

The current source-level file hashes observed locally were `64E0FF657E511B1008665963FF6AC1D29921395FF6783FB779FEAC9662BEC995` for the decision/mission file, `138E276E8A0642F401CF46C03D7189F4664C6734FE617A55B807461D4DB127FF` for parent effects, `6ADBB93B2CD17665C4BD967368F08BC953738D81DB7A2069171241F45C309DCA` for the strategy file, and `C42496D5691D04C956BFC118E282CFBBCFEBCA02843F9A1C4DC0C62AB9493AA0` for constants.

These local SHA-256 values are not interchangeable with MCP source revisions or source hashes.

The source files were dirty or untracked in the shared workspace before this append, and MCP source revisions changed during the audit.

Therefore the successful analysis artifacts below are immutable evidence for their recorded source revisions, while the later refresh failures prevent a stable final-current certification.

The source scan at the end of the pass still found exactly 18 decision `ai_will_do` blocks and 3 mission `ai_will_do` blocks.

### Exact candidate pools

The complete source-discovered decision pool supplied to the decision adapter was:

```text
event021_secure_arsenals
event021_defend_capital
event021_review_loyalty
event021_seize_depot
event021_open_relief_corridor
event021_offer_emergency_settlement
event021_reconstruct_administration
event021_integrate_formations
event021_set_priority_front
event021_monitor_border
event021_support_government
event021_support_opposition
event021_offer_mediation
event021_end_sponsor_commitment
event021_complete_disarmament
event021_complete_coalition_governance
event021_protect_communications
event021_review_regional_administration
```

The complete source-discovered mission pool supplied to the mission adapter was:

```text
event021_hold_the_capital_mission
event021_secure_rail_spine_mission
event021_hold_settlement_terms_mission
```

The complete narrowed strange-incident random-list pool was:

```text
common/scripted_effects/021_random_civil_war_parent_effects.txt:4378.entry.1
common/scripted_effects/021_random_civil_war_parent_effects.txt:4378.entry.2
```

The first random-list inspection against the whole parent-effects source found eight entries from multiple categorical pools and explicitly refused to normalize them without selecting one pool.

The narrowed two-entry inspection reported `poolComplete=true` at the source-pool level.

The decision and mission inspections reported `poolComplete=false` and `availableCandidates=0` because no runtime country, target, resource, flag, or state fixture was active.

An explicit 18-entry or 3-entry list therefore proves source-pool enumeration, not the complete currently eligible runtime pool.

### Mandatory probability inspect calls and receipts

The initial adapter-only probe was:

```text
mcp__hoi4_agent_tools__hoi4_probability_inspect({
  adapter: "decision_ai_will_do",
  refresh: true,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

It returned the exact input blocker `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: An adapter requires a source; provide a source alone to discover compatible adapters`.

The corrected decision inspection was:

```text
mcp__hoi4_agent_tools__hoi4_probability_inspect({
  adapter: "decision_ai_will_do",
  source: { path: "common/decisions/021_random_civil_war_decisions.txt" },
  refresh: true,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

It returned `PROBABILITY_SOURCE_INSPECTED` with source revision `fcd299cd0c791f263428acb1084e4b633aa12caadd3f630ad229a4bf030f8215`, source hash `b012bf7ee5789568875a8e9eb6c1fdb57ad206b1a9e04348eea9523070aa4b6d`, 18 candidates, 5 required input families, zero inspect-time unresolved items, `poolComplete=false`, `availableCandidates=0`, `selectionRule=score_only`, `rawScore=true`, and `normalizedProbability=false`.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5f6af0ac32d346161acbce2375ae6fdf9d05896a7f5230dc83714ab9b6f114f/e1ba6dfc912a71c13734def06ddd54674e76d4da391657a06e703a700cb3f5fc/probability-inspect-b012bf7ee578.json`.

The required input union was `capital_scope`, `custom_trigger_tooltip`, `has_variable`, `hidden_trigger`, and `var:random_civil_war_priority_front_state`.

The corrected mission inspection was:

```text
mcp__hoi4_agent_tools__hoi4_probability_inspect({
  adapter: "mission_ai_will_do",
  source: { path: "common/decisions/021_random_civil_war_decisions.txt" },
  refresh: true,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

It returned `PROBABILITY_SOURCE_INSPECTED` with the same source revision and source hash, 3 candidates, 2 required input families, zero inspect-time unresolved items, `poolComplete=false`, `availableCandidates=0`, `selectionRule=score_only`, `rawScore=true`, and `normalizedProbability=false`.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d001352e3ee3645e766c151ba09a255c7b699aea13c3d453e097f7ec067223fb/70947f626da53e4dc8f3e87cd0b785bf8bebd1f74099f587a4e88259ea8fdc6d/probability-inspect-b012bf7ee578.json`.

The required input union was `custom_trigger_tooltip` and `has_variable`.

The whole-source strange-list inspection was:

```text
mcp__hoi4_agent_tools__hoi4_probability_inspect({
  adapter: "random_list",
  source: { path: "common/scripted_effects/021_random_civil_war_parent_effects.txt" },
  refresh: true,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

It returned `PROBABILITY_SOURCE_INSPECTED` with source revision `dae889e52c68a7fdbf2733bf2b3096bc47b1d55dff6bddfb2b077f4ba4462512`, source hash `7279c1eabc4339d4a20e0a02cbdb44f874af7f329e124053367046789729e4aa`, 8 aggregate entries, `poolComplete=false`, 8 required input families, 1 unresolved item, and the unsupported diagnostic `MULTIPLE_CATEGORICAL_POOLS: Select one event-option or random-list pool before requesting normalized probabilities`.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a1532d26484e7564fc4969694447c8f00409681c6cd0764cd45fc43df3c8474/5c8c6711d75fcad3bc69c34010c1c4861bf0ed70e69e7e03ee070c43053fa113/probability-inspect-7279c1eabc43.json`.

The narrowed strange-list inspection was:

```text
mcp__hoi4_agent_tools__hoi4_probability_inspect({
  adapter: "random_list",
  source: { path: "common/scripted_effects/021_random_civil_war_parent_effects.txt" },
  candidatePool: [
    "common/scripted_effects/021_random_civil_war_parent_effects.txt:4378.entry.1",
    "common/scripted_effects/021_random_civil_war_parent_effects.txt:4378.entry.2"
  ],
  refresh: true,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

It returned `PROBABILITY_SOURCE_INSPECTED` with the same source revision and source hash, 2 candidates, `poolComplete=true`, 2 required variable inputs, zero unresolved items, and `selectionRule=proportional_categorical`.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c4d373c7108966204ebe3b251dcdc641e24e2b59808edfb1c673107c19d9ed9/e42fd2134577f563b5531a0fe16b2c21f48ffcfc5d716facdb81afaa00f9df7a/probability-inspect-7279c1eabc43.json`.

The related strategy-factor inspection was:

```text
mcp__hoi4_agent_tools__hoi4_probability_inspect({
  adapter: "ai_strategy_factor",
  source: { path: "common/ai_strategy/021_random_civil_war_ai_strategy.txt" },
  refresh: true,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

The first result was `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, zero required inputs, source revision `df88cb5f946e5c19c34bf2c8aba0f8453f367ff9bf0b164bda4f09fe4d1101e0`, source hash `74d73084d977d42abe822021d859cb7b7a075aa89565a9c9dd861c9261b37db9`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f17e34dd9bdc904e5dbe41222d13797c877377eba38b4effa0df36756eb70a2/5903e6e784f91d683d1742935b24d0176bfa382bbfad5d0f0ed0c9fd9f1ddccb/probability-inspect-74d73084d977.json`.

### Named probability evaluations

The decision smoke evaluation used scenario set `EVENT021_DECISION_SCORE_SMOKE_2026_08_31` and scenario id `E021-DECISION-EMPTY-FIXTURE-2026-08-31` with `state={}`, the exact 18-entry pool above, horizon 365 days, metric `raw_value`, and outputs `json`, `ranking`, `matrix`, and `unresolved`.

It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-4b1db080c305dc3a3d48e6e8`, source revision `fcd299cd0c791f263428acb1084e4b633aa12caadd3f630ad229a4bf030f8215`, source hash `b012bf7ee5789568875a8e9eb6c1fdb57ad206b1a9e04348eea9523070aa4b6d`, scenario hash `c5b609c5bf253da7fc574432b68a5d9928f0abd2a7c66aec3db68db5b2a3619c`, 18 candidates, 22 unresolved items, 23 diagnostics, and no normalized candidate probabilities.

Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b04ee13b5b7461c3044f1d94c34b7d5c85cef73de77caf57796a6fd6c4f2615/4e0af5f38b6a82c1b2fc90b0b8b3b802838e38fd09a083f35f2a4535d02aec0c/probability-4b1db080c305dc3a3d48e6e8.json`.

The unresolved trace was dominated by missing `hidden_trigger` state, with additional unresolved `capital_scope`, `custom_trigger_tooltip`, `has_variable`, and `var:random_civil_war_priority_front_state` requirements on the affected candidates.

The mission smoke evaluation used scenario set `EVENT021_MISSION_SCORE_SMOKE_2026_08_31` and scenario id `E021-MISSION-EMPTY-FIXTURE-2026-08-31` with `state={}`, the exact 3-entry pool above, horizon 365 days, metric `raw_value`, and outputs `json`, `ranking`, `matrix`, and `unresolved`.

It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-57848d7f8d538bd52552b9f8`, source revision `cea48bec5f1562f9496601f4944e5d52a40e6ca7e4c36280e2fd2352583d9fe7`, source hash `b012bf7ee5789568875a8e9eb6c1fdb57ad206b1a9e04348eea9523070aa4b6d`, scenario hash `d2c37df9afdf63b684dae6baa3d77619b7f9ec771d0dfce1c5108b0d64bdfad4`, 3 candidates, 5 unresolved items, 4 diagnostics, and `selectionRule=score_only`.

Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5d552e7665d6132c522632ebf74d496b70ea462f456f0b9d0ca875bd1577fa7/035ef0b22dff1cd6a8f22c8d3330b0de623725611568202174e9cc5a0b7954f0/probability-57848d7f8d538bd52552b9f8.json`.

The empty fixture produced raw values of 1 for `event021_hold_settlement_terms_mission` and `event021_secure_rail_spine_mission`, and raw value 0 with `eligibility=false` for `event021_hold_the_capital_mission`.

Those values are not a live mission ranking because the settlement and rail rows retained unresolved `has_variable` and `custom_trigger_tooltip` inputs, while the capital row was evaluated under an intentionally empty fixture.

The strange-incident evaluation used scenario set `EVENT021_STRANGE_INCIDENT_CURRENT_2026_08_31` and scenario id `STR-BASELINE-EVOL-II-ELIGIBLE-VARKEYS-2026-08-31` with the exact two-entry pool, flat state keys `var:event021_parent_strange_incident_weight=0.08` and `var:event021_parent_no_strange_incident_weight=0.92`, horizon 1 day, metrics `conditional_probability` and `raw_value`, and outputs `json`, `ranking`, `matrix`, and `unresolved`.

It returned `PROBABILITY_ANALYZED` with analysis id `probability-8f447805680e8f4d5342a8e6`, analysis status `complete`, source revision `ebdc4982d2194cb2a1803af265661f9568b873abf23bd2ef6b397e9aea13fee6`, source hash `7279c1eabc4339d4a20e0a02cbdb44f874af7f329e124053367046789729e4aa`, scenario hash `98ec6320dd0d1cff201167a1d28a2f0e20ac1cf929a54c0b8fb7996caaeb0851`, 2 candidates, zero unresolved items, and 1 dominance diagnostic.

The exact conditional random-list outcomes were `0.08` for `common/scripted_effects/021_random_civil_war_parent_effects.txt:4378.entry.1` and `0.92` for `common/scripted_effects/021_random_civil_war_parent_effects.txt:4378.entry.2`.

The `0.92` no-incident outcome ranked first and emitted `PROBABILITY_DOMINANT_OUTCOME` at the configured dominance threshold.

The strange JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7030716bb856042da760a88cfaaf32569fec975ee95501709247833f13525173/ef903a5a8048a54dd3ded95570c930233ca34d272298d6cec0bed9c2ddfe8221/probability-8f447805680e8f4d5342a8e6.json`.

The emitted strange ranking, matrix, and unresolved resources were respectively `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/954c315da441f05da8e71f7cb5173ba4e561c508ceca034c083088d576c0ad7a/3333e2f9f2077c524f3307d84155ae78b8ecc0b0921bef6afdb4a7c8979f745f/probability-probability-8f447805680e8f4d5342a8e6-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/baf6b0253d25a60650473aca0380a2ab9730854b0c5b9b1ebc2f2dd66bf3c5b1/1d74df6ad05bea020faf398d2796687f6398ecfe92295f810f7edd7c57ace9da/probability-probability-8f447805680e8f4d5342a8e6-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/1258a887821734981bb5f5bd4fef83a175b39eb30032dc3c16d21835f44c1c62/probability-probability-8f447805680e8f4d5342a8e6-unresolved.svg`.

This exact result is conditional on the enclosing effect reaching this complete two-entry list with both weights supplied.

It does not certify the outer Evolution II gate, active-side enumeration, invocation cadence, recent-incident cooldown, long-run incidence, terminal state, or campaign timing.

The parent-supplied strange evidence remains historical provenance: analysis `probability-6238523a08ebef03f0a38e07`, scenario hash `dfc486d2c35bd1237686439b22e74de17dbed503085b3e52346d81252640e284`, and its supplied artifact remain distinct from this fresh analysis and must not be rewritten as the same revision.

The fresh result semantically reconciles to the supplied 8%/92% result, but the two analysis ids, scenario hashes, and source revisions are different.

### Render and source-stability receipts

The explicit render call for the fresh strange analysis was:

```text
mcp__hoi4_agent_tools__hoi4_probability_render({
  analysisId: "probability-8f447805680e8f4d5342a8e6",
  expectedScenarioHash: "98ec6320dd0d1cff201167a1d28a2f0e20ac1cf929a54c0b8fb7996caaeb0851",
  outputs: ["ranking", "matrix", "unresolved"],
  includeHtml: false,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

It returned `PROBABILITY_ANALYSIS_STALE` with analysis revision `ebdc4982d2194cb2a1803af265661f9568b873abf23bd2ef6b397e9aea13fee6` and current workspace revision `2c5d0bfe19bf65863746f4a4740cd1e4641ec690d8d17d7e83c9a66f1049ebbc`.

The stale render receipt is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f89717abeebcacc48538d0883f65bfbe5b0d4f05bd1250eba092aa3c05275d78/fd4a3c96fa476de2e89c4daa67ced13c9623386d53ad1d6232d2cf36cec31105/probability-8f447805680e8f4d5342a8e6.json` and reported `visualResources=0`.

A final refresh inspect after the workspace revision moved returned `INTERNAL_ERROR` with `Unexpected internal error` and no artifact for each of `decision_ai_will_do` on the decision source, `mission_ai_will_do` on the decision source, and `random_list` on the parent-effects source.

The final strategy refresh did succeed as `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`, zero candidates, source revision `841a5a87ae56ecea148c1ee6a23c2f46fdff00f1353e1342c27c0a758ba902b1`, the same source hash `74d73084d977d42abe822021d859cb7b7a075aa89565a9c9dd861c9261b37db9`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1379141127b0b9ba36d4aa8e725e3e7295efe608f3a2d1c435f1c3a5cc48104/9481a3283ae11a2a207f496987cf4f8c76eb546a1efec893f5d5405f7eb3e483/probability-inspect-74d73084d977.json`.

The stale render and final refresh errors mean no stable post-movement visual or current-source probability certification is claimed.

### Required sweep calls and exact blockers

The decision sweep used the full 18-entry pool, scenario set `EVENT021_DECISION_SWEEP_PENDING_2026_08_31`, scenario `E021-DECISION-EMPTY-FIXTURE-2026-08-31`, empty state, paths `hidden_trigger`, `capital_scope`, `has_variable`, and `var:random_civil_war_priority_front_state`, 5 steps, pairwise sensitivity, and `findRankReversals=true`.

It returned `INTERNAL_ERROR` with `Unexpected internal error`, zero artifacts, and no analysis id.

The mission sweep used the full 3-entry pool, scenario set `EVENT021_MISSION_SWEEP_PENDING_2026_08_31`, scenario `E021-MISSION-EMPTY-FIXTURE-2026-08-31`, empty state, paths `has_variable` and `custom_trigger_tooltip`, 5 steps, pairwise sensitivity, and `findRankReversals=true`.

It returned `INTERNAL_ERROR` with `Unexpected internal error`, zero artifacts, and no analysis id.

The strange sweep used scenario set `EVENT021_STRANGE_SWEEP_PENDING_2026_08_31`, scenario `STR-BASELINE-EVOL-II-ELIGIBLE-VARKEYS-2026-08-31`, the two-entry pool, supplied variable weights `0.08` and `0.92`, paths `var:event021_parent_strange_incident_weight` and `var:event021_parent_no_strange_incident_weight`, 5 steps, pairwise sensitivity, and `findRankReversals=true`.

It returned `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request`, zero artifacts, and no analysis id.

A retry using plain paths `event021_parent_strange_incident_weight` and `event021_parent_no_strange_incident_weight` returned the same `PROBABILITY_SURFACE_EMPTY` blocker.

No sensitivity, threshold, or rank-reversal result is claimed for any scoped surface.

### Structural MCP evidence

The required event structural call was:

```text
mcp__hoi4_agent_tools__hoi4_event_inspect({
  mode: "trace",
  direction: "both",
  expandHelpers: true,
  maxDepth: 3,
  maxNodes: 200,
  maxEdges: 400,
  selector: { kind: "event", eventId: "chaosx.nr21.1" },
  refresh: true,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

It returned `EVENT_INSPECTED_PARTIAL` at graph revision `cfdc65be2a281cc4ef468a2feb63ec37cf7111f783c5e240480e4ef2b0351a3b`, graph hash `94718112adcec4bf4f89412207856442507d6b9bbbe753508b64591ebf2285cd`, and with a focused root-to-helper boundary that marked `event021_parent_dispatch_opening` as `EVENT_HELPER_UNRESOLVED` because it was absent from the active MCP catalog.

The local source defines that helper at `common/scripted_effects/021_random_civil_war_parent_effects.txt:4219`, so this is an MCP catalog/deferred-projection blocker, not evidence that the helper is absent from the source.

The event trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d664d8ae162737ab83adaa9f28447261a7645cca5437f8bff458ce66fc4ec172/02b78f1cea2eab0a21a7e3c786ed47d297fa383b2bc79603082fc8a6f184fd0d/event-trace-cfdc65be2a28.json`.

The matching overview render call used `view=overview`, selector `{kind:event,eventId:chaosx.nr21.1}`, `expandHelpers=true`, `maxDepth=3`, `maxNodes=200`, `includeHtml=true`, and the same workspace.

It returned `EVENT_RENDERED_PARTIAL` and selected the event root plus the unresolved `event021_parent_dispatch_opening` helper.

The render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7933af159120092eeae758b885d0dbde25537b46d755554290842d3f87bee401/4ac58c8f556ed75d72df3eb52917b8c51968bb0dcad308962a80be9bb994885c/event-overview-cfdc65be2a28-manifest.json`.

The rendered JSON, SVG, PNG, and HTML are respectively `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ae814a62ebf42868f4df05ead4cf9e228e0a20e63bac88d0bcee59ea9b9b6e9/74c9e127f1aae48562112e83ffce63fe721fe891ed1d27fbb86abce3d0c0f586/event-overview-cfdc65be2a28.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/829d497756b9c3a9ca0410fb960ca3432ed0228e1a1593bca3aaec4386516cea/f749b76c224d5dc8b5fdbc2c9327fa94ce605724426af9afaca42e79ef034cbf/event-overview-cfdc65be2a28.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca00ef1d2c23589586e6fbc60db6c4175ab13e4093e4a3e430e75769ec2759b9/e9ba0a576852a92f99741961ff4ef73f23d27e525c64a8eede3750bd09ffc586/event-overview-cfdc65be2a28.png`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ccbcca7f7b895c5314a0bf877bd20ec75875ce29bd9ba38c5d7fff659499e72d/ce5416b1a8cd09e2b4cbde833f6acf62c2d9449fcbd65b40049f9de92da99ac8/event-overview-cfdc65be2a28.html`.

### Source base values and modifier trace

Every one of the 18 decision blocks has base willingness `constant:event021_ai.base_action = 1`.

The 3 mission blocks have base willingness `constant:event021_ai.base_mission = 1`.

The centralized AI constants are `priority_major = 1.5`, `discourage_concession = 0.75`, `discourage_repression = 0.75`, and `exposure_mediator_stability = 0.65`.

The current decision modifiers are:

| Candidate | Positive factors | Reduction or hard-zero factor |
| --- | --- | --- |
| `event021_secure_arsenals` | government side `1.5` | settlement pending `0` |
| `event021_defend_capital` | capital controlled by ROOT `1.5`; government side `1.5` | none |
| `event021_review_loyalty` | command claimant `1.5`; government side `1.5` | low authority `0.75` |
| `event021_seize_depot` | opposition side `1.5` | invalid priority-front depot `0` |
| `event021_open_relief_corridor` | neighbor exposure `1.5`; humanitarian pressure `1.5` | none |
| `event021_offer_emergency_settlement` | negotiator profile `1.5`; low authority `1.5` | hardliner profile `0.75` |
| `event021_reconstruct_administration` | successor side `1.5` | none |
| `event021_integrate_formations` | multifront active `1.5`; command claimant `1.5` | none |
| `event021_set_priority_front` | multifront active `1.5` | none |
| `event021_monitor_border` | containment profile `1.5` | none |
| `event021_support_government` | opportunistic sponsor `1.5` | mediator profile `0.75` |
| `event021_support_opposition` | opportunistic sponsor `1.5` | mediator profile `0.75` |
| `event021_offer_mediation` | mediator profile `1.5` | opportunistic sponsor `0.75` |
| `event021_end_sponsor_commitment` | negotiator profile `1.5` | none |
| `event021_complete_disarmament` | government side `1.5` | none |
| `event021_complete_coalition_governance` | negotiator profile `1.5` | none |
| `event021_protect_communications` | capital supply risk `1.5` | none |
| `event021_review_regional_administration` | low authority `1.5` | none |
```

The mission modifiers are `event021_hold_the_capital_mission` government side `1.5`, `event021_secure_rail_spine_mission` reconstruction phase `1.5`, and `event021_hold_settlement_terms_mission` settlement phase `1.5`.

The decision source also carries resource, cooldown, visibility, availability, and target gates outside the score blocks.

`event021_seize_depot` requires `event021_priority_front_depot_target_valid = yes` for availability and explicitly gives its AI score factor `0` when that target is invalid.

The government and opposition support decisions require their corresponding exposure target-valid triggers.

The capital mission requires a ROOT-controlled capital with positive infrastructure and supply-node values, plus an active defense or held-capital flag.

The rail mission requires `random_civil_war_rail_mission_state`, ROOT ownership and control of that target, membership in `ROOT.random_civil_war_opening_core_states`, and positive supply-node or infrastructure state.

The settlement mission requires `random_civil_war_settlement_terms_hold_until`, an active settlement obligation, and no settlement-obligation failure flag.

The strange-list weights are `constant:event021_parent_tuning.strange_incident_probability = 0.08` and `constant:event021_parent_tuning.strange_incident_no_probability = 0.92`.

The incident branch records a recent-incident flag, applies authority delta `-3`, applies pressure delta `+4`, and writes `random_civil_war_strange_incident_until` using the exposure cooldown constant.

The outer incident gate requires Evolution II active, the Evolution II log not disabled, an active civil war, and no recent incident.

The caller `event021_parent_apply_evolution_ii` runs the active-theater loop and invokes at most one local strange-incident roll per active side in that recorded Evolution II invocation.

That caller cadence, the outer gate frequency, cooldown expiry, and terminal cleanup were not part of the two-entry random-list adapter result.

### Result classification and findings

The decision result is `score-only` and `MCP partial`.

The source-parsed base value of 1 is exact source evidence, not a click probability.

The empty decision fixture did not resolve the hidden availability/cost/target inputs and therefore proves no live ranking, dominance, starvation, or rank reversal.

The mission result is `score-only` and `MCP partial`.

The empty fixture's raw values are diagnostic of that fixture only and cannot be treated as a live mission-selection probability or ranking.

The strange result is `exact conditional` for the complete two-entry categorical random list, with 8% incident and 92% no incident and zero unresolved items in that list.

The strange result is not an exact overall occurrence rate for a day, campaign, side, or event chain because the enclosing gates and cadence were not evaluated.

AI validity is source-bounded rather than engine-certified: explicit zeroing exists for an invalid depot target, and the other decisions and missions have availability/activation gates, but the adapter could not resolve the live target, resource, flag, scope, and custom-trigger state.

Conditional no-incident dominance is proven at 92% for the strange two-entry pool and was reported by MCP as a dominance warning.

No decision or mission dominance claim is supportable from the empty score-only fixtures.

No starvation claim is supportable for the decision or mission pool because no complete eligible runtime pool was available.

The explicit hard-zero gates are intended fail-closed behavior, but stale or incorrectly populated target state remains an untested runtime risk.

No rank reversal, threshold, or sensitivity result was produced because all sweep calls were blocked.

No repetition rate or long-run strange-incident frequency was produced because `probability_sequence` was not justified without a complete cadence/state-transition manifest.

The source-level recent-incident guard and cooldown variable reduce repeat risk, but their runtime reset and terminal behavior remain unverified.

No exploit is proven.

Unresolved exploit-risk surfaces are target validity, resource affordability, cooldown/cap interaction, repeated mission activation, and outer strange-incident cadence because those require populated runtime fixtures or sequence evidence.

### Pending matrix, comparisons, and skipped analyses

The broad named probability matrix for target, archetype, severity, decision, mission, exposure, sponsor, strange incident, settlement, recurrence, cluster, and scenario systems remains pending.

The accepted `TGT-01` through `SCN-07` matrix and runtime acceptance fixtures were not closed by the empty smoke evaluations.

`hoi4.probability_compare` was not called because no owner-applied before/after patch and no immutable same-scenario pre-change baseline were supplied.

No comparison id exists.

`hoi4.probability_simulate` was skipped because no uncertain input distribution and seed contract was declared.

`hoi4.probability_sequence` was skipped because no complete custom pool manifest declared cadence, cooldown, recovery, cap, removal, reset, timer changes, and terminal states.

The explicit `probability_sweep` attempts and their exact blockers are recorded above, so no threshold, sensitivity, or rank-reversal result is inferred from source arithmetic.

Live HOI4 runtime acceptance was not performed.

### Recommended owner follow-up, not applied

1. Provide typed country, target, state, resource, flag, scope, cooldown, and route fixtures for all 18 decisions, including `hidden_trigger`, `capital_scope`, `custom_cost_trigger`, target-validity, and `random_civil_war_priority_front_state` inputs.

2. Provide typed mission fixtures for capital control/infrastructure/supply, opening-core membership, rail target ownership/control, settlement hold-until, settlement obligation, reconstruction phase, government side, and mission-active/success/failure flags.

3. Re-run the same named decision and mission scenario ids with the full 18-entry and 3-entry pools and classify the results as score-only unless the adapter changes its verified selection rule.

4. Declare numeric alternatives or ranges for accepted scenario state paths before rerunning `probability_sweep`, retaining pairwise sensitivity and rank-reversal search.

5. Declare an Evolution II sequence manifest for `event021_parent_apply_evolution_ii` and `event021_parent_roll_strange_incident`, including active-side pool, invocation cadence, recent-incident cooldown, reset, recovery, and terminal state before using `probability_sequence` or claiming a long-run incidence rate.

6. Capture a real pre-change artifact and run `probability_compare` against an owner-applied after state using identical scenario ids, hashes, pools, and external factors.

7. Re-run the structural inspect/render after the source revision stabilizes or the MCP catalog resolves `event021_parent_dispatch_opening` from `common/scripted_effects/021_random_civil_war_parent_effects.txt:4219`.

8. Keep all balance targets, gameplay edits, and any source fixes with the owning implementation agent; this auditor applied none.

### Current disposition

The handoff path `docs/plans/021_random_civil_war_plans/subagent_handoffs/ai_probability_audit.md` was writable and this dated section was appended without deleting historical provenance.

The decision and mission source parses are reconciled to the supplied 18/3 candidate counts, but their current runtime eligibility and score races remain unresolved.

The strange two-entry conditional list is exactly 8%/92% for the recorded analysis snapshot, but overall strange-incident timing and frequency remain unresolved.

The audit is therefore `MCP partial / score-only for decisions and missions / exact conditional for the narrowed strange list / not gameplay complete`.
