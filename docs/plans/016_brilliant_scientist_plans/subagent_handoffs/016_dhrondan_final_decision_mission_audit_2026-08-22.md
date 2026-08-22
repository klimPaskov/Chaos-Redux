# Event 016 D’Rhondan Final Decision and Mission Acceptance Audit

Date: 2026-08-22

Scope: the reusable Alien Infantry landing reservation, the Event 016 D’Rhondan contact decisions and missions, DHR focus-derived landing recovery, rebellion pulse probabilities, decision AI, player-facing decision text, and regressions to the existing Directorate scripted GUI.

Authority: `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`, `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`, the current source files, the accepted Event 016 handoffs, the offline Paradox wiki decision/mission and GUI pages, and the installed vanilla documentation and precedents.

## Acceptance result

The scoped source is accepted for decision and mission behavior with no P0 or P1 gameplay defect found and no source patch required in this audit.

The UFO landing reservation, contact header, Honor Accord, Kruger expedition, Mengele expedition, and country-scoped rebellion pulse match the accepted addendum in source review and in the supported MCP probability scenarios.

The unresolved items are evidence limitations rather than accepted gameplay defects: the required `chaosx_ai_probability_auditor` is not present in the callable tool inventory, the standard decision/category inspector is not exposed, ordinary decisions have no GUI window identifier, the existing Directorate GUI inspect was blocked by artifact storage, and no in-game consumer run is permitted for this agent.

No gameplay, localisation, GUI, focus, event, or constant file was changed by this audit. The only new file is this handoff.

## Severity-sorted issue list

### P0 — none

No acceptance-contract blocker was found in the scoped landing, contact, mission, AI, or cleanup source.

### P1 — none

No route can currently bypass the landing reserve, create a second pending landing, grant a duplicate Kruger return, or activate a world-iterating rebellion scheduler in the audited source.

### P2 — unresolved MCP probability-owner route

The project-required `chaosx_ai_probability_auditor` is absent from `ALL_TOOLS`; no callable custom auditor route exists for the mandatory owner-routed probability pass.

The direct `hoi4.probability_inspect` source pass discovered the rebellion `random_list`, but the `decision_ai_will_do` adapter discovered only the unavailable status row and the `mission_ai_will_do` adapter discovered no weighted blocks because the route decisions and hidden missions do not expose adapter-recognized weighted pools.

Forced route evaluation for `dhrondan_send_kruger_to_dhronda`, `dhrondan_send_mengele_to_dhronda`, `dhrondan_honor_accord`, `dhrondan_kruger_expedition_mission`, `dhrondan_mengele_expedition_mission`, and `dhrondan_rebellion_pulse_mission` returned `PROBABILITY_SURFACE_EMPTY` with no artifact.

This is recorded as an MCP fidelity blocker and is not treated as equivalent to the required custom auditor or live AI acceptance.

### P2 — decision and GUI MCP limitations

The installed server exposes no standard `hoi4.decision_inspect` or decision-category render route, and the two scoped categories use the normal decisions surface rather than a scripted GUI window.

The mandatory regression-only `hoi4.gui_inspect` attempt for `kruger_directorate_container` returned `ARTIFACT_STORAGE_LIMIT` with the exact message `Artifact batch cannot fit after reclaiming expired artifacts` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The corresponding read-only `hoi4.gui_render` did complete and returned a full SVG artifact, but the inline response was truncated; no GUI rewrite was justified because the existing Directorate panel has no Event 016 contact or landing controls and source review found no regression.

### P3 — inherited focus-layout warnings

`hoi4.focus_inspect` confirmed 88 DHR focuses and returned seven DHR layout warnings consisting of two linear detours and five same-row spacing warnings, plus unrelated vanilla continuous-focus icon diagnostics.

Those are owned by the focus-tree audit and do not block this decision or mission acceptance because the landing API consumes already-defined DHR flags without changing focus layout.

### P3 — live consumer validation

No Hearts of Iron IV process was launched and no save was exercised, as required by the repository instructions; live decision rendering, mission countdown behavior, AI selection, equipment consumption, and popup consumer acceptance remain user-owned evidence.

## Audited source and identifiers

- Landing decision and mission: `common/decisions/016_alien_infantry_landing_decisions.txt`, `alien_infantry_call_landing`, `alien_infantry_landing_mission`.
- Landing trigger API: `common/scripted_triggers/016_alien_infantry_api_triggers.txt`, `alien_infantry_landing_state_is_valid`, `alien_infantry_landing_target_is_valid`, `alien_infantry_landing_reservation_is_valid`, `alien_infantry_can_call_landing`.
- Landing effect API: `common/scripted_effects/016_alien_infantry_api_effects.txt`, `alien_infantry_begin_landing_reservation`, `alien_infantry_cancel_landing_reservation`, `alien_infantry_apply_landing_cooldown`, `alien_infantry_spawn_landing_cohort`.
- Landing constants: `common/script_constants/016_alien_infantry_api_constants.txt`.
- Contact decisions and missions: `common/decisions/016_dhrondan_contact_decisions.txt`, `dhrondan_contact_status_header`, `dhrondan_send_kruger_to_dhronda`, `dhrondan_send_mengele_to_dhronda`, `dhrondan_honor_accord`, `dhrondan_kruger_expedition_mission`, `dhrondan_mengele_expedition_mission`, `dhrondan_rebellion_pulse_mission`.
- Contact triggers: `common/scripted_triggers/016_dhrondan_contact_triggers.txt`, route availability and validity readers, Honor gate, pulse gate, and high/medium tier readers.
- Contact effects: `common/scripted_effects/016_dhrondan_contact_effects.txt`, Kruger suspension and restoration, exact Directorate deltas, expedition start and AI helper, success/failure cleanup, Honor Accord, pulse refresh and resolution, and revolt bridge.
- Contact constants: `common/script_constants/016_dhrondan_contact_constants.txt`.
- Decision categories: `common/decisions/categories/016_alien_infantry_landing_category.txt` and `common/decisions/categories/016_dhrondan_contact_category.txt`.
- Player text: `localisation/english/016_alien_infantry_api_l_english.yml` and `localisation/english/016_dhrondan_contact_l_english.yml`.
- DHR focus consumers: `common/scripted_effects/016_dhrondan_focus_effects.txt`, `common/scripted_triggers/016_dhrondan_focus_triggers.txt`, and `common/national_focus/016_dhrondan_focus_tree.txt`.
- Follow-up events: `events/016_brilliant_scientist_dhrondan_contact_events.txt`, `chaosx.nr16.40` through `.47`.
- Existing GUI regression surface: `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt` and `interface/016_brilliant_scientist_directorate.gui`.

## Landing reservation acceptance

`alien_infantry_call_landing` is a state-targeted decision using `state_target = yes`, `target_root_trigger`, `target_trigger`, `on_map_mode = map_and_decisions_view`, and `FROM` state scoping consistent with vanilla state-targeted decisions such as the AFG decisions around `AFG.txt:477` and `AFG.txt:1069`.

The selected state must be passable, owned by, and controlled by the calling country; the same state ID is stored in `dhrondan_landing_state_id` before the reservation effect runs.

The country gate requires an independent positive contact receipt, no pending reservation, no recovery flag, no world-end flag, at least `2,000` `alien_laser_weapon_equipment_1`, and at least one valid controlled state.

The reservation effect subtracts exactly `constant:alien_infantry_landing.reserve_equipment` (`2,000`) once, sets `alien_infantry_landing_pending`, stores `constant:alien_infantry_landing.reservation_days` (`7`), and activates exactly one hidden landing mission.

The pending flag blocks a second landing even when another state is valid, and the country-level reservation target prevents a second concurrent reservation.

The mission timeout is `var:alien_infantry_landing_reservation_days` and its timeout effect calls `alien_infantry_spawn_landing_cohort`; it does not refund on success.

The mission cancellation trigger revalidates contact, the selected state, control, ownership, passability, and world-end safety; `alien_infantry_cancel_landing_reservation` clears the pending flag before refunding exactly `2,000`, removes the mission, and clears the reservation-day and target variables, making repeated cancellation idempotent.

Successful materialization creates one locked, non-recruitable ten-battalion `D’Rhondan Landing Cohort`, marks the selected state, records history, increases Alien Presence by `1`, increases Pact Strain by `5`, and applies the recovery cooldown.

The ordinary recovery ladder is `30` days by default, `24` with `dhrondan_landing_network_enabled`, `18` with `dhrondan_descent_windows_guarded`, and `12` with `dhrondan_near_space_secured`; the tag guard requires `DHR` and the highest earned tier wins because the later checks override the earlier temporary value.

The seven-day reservation and exact `2,000` reserve remain unchanged by the focus-derived recovery tiers.

The DHR sovereignty bootstrap branch is explicitly batch-only, requires a positive DHR sovereignty receipt, consumes its own `2,000` per cohort, and intentionally suppresses ordinary host telemetry and immediate cooldown; it is a separate accepted country-formation input and is not an ordinary landing decision bypass.

## Contact header, decision lifecycle, and cognitive load

`dhrondan_contact_status_header` is a compact unavailable status row visible after `dhrondan_pact_established`; its localisation exposes live `dhrondan_alien_presence` and `dhrondan_pact_strain` values and the description explains what each value means and why high strain matters.

The D’Rhondan contact category is visible after craft completion, pact establishment, or an active expedition and is marked `visible_when_empty = yes`.

Before the pact, the category presents the eligible Kruger or Mengele route and no unrelated management wall; the route predicates are mutually exclusive in the intended country identities.

After the pact, the status header and Honor Accord are visible, and the landing callback may activate the single country-scoped rebellion pulse mission.

During an expedition, the active route decision remains a disabled presentation row while the hidden mission owns the clock; the route gate prevents a second expedition.

The contact category has at most two route rows, one Honor row, one status row, and one active contact mission in normal valid states, staying below the six-primary-action ceiling; the landing category has one call row and one active mission row.

The Kruger and Mengele missions cannot overlap because both route gates reject `dhrondan_expedition_in_progress`; the rebellion pulse cannot overlap an expedition because pact establishment occurs only after the expedition returns.

No raw wall of dynamic values is exposed: the only persistent contact values are the two header counters, and their cause, threshold, consequence, and player response are explained in the adjacent header/category/mission text.

All visible action descriptions are concise enough to identify the actual cost, duration, threshold, consequence, or blocked condition without requiring the player to remember an unrelated counter.

## Mission quality notes

| Mission | Owner and category | Region or target | Requirement and duration | Success | Failure and cleanup | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| `alien_infantry_landing_mission` | Alien Infantry API, `alien_infantry_landing_category` | One saved passable state owned and controlled by the host | Positive contact, one pending flag, valid target, and `7` days | One locked ten-battalion cohort, state marker, history, Presence `+1`, Strain `+5`, cooldown | State/contact/world-end invalidation refunds exactly `2,000` once and clears reservation state | Country pending flag and idempotent cancel block duplicate reservations or refunds |
| `dhrondan_kruger_expedition_mission` | D’Rhondan contact owner, `dhrondan_contact_category` | Country-scoped expedition; no map target | Current Kruger host, completed craft, active canonical Kruger, no injury/confined/obligation/pact, `50` PP plus `500` fuel, `180` days | Valid timeout opens the planetary audience; accepted return applies pact and one-time Directorate return deltas | Character death/injury/confined state, host invalidation, or world end calls failure cleanup and restores only a valid canonical host role state | Route flag, shared expedition flag, character obligation, and idempotent reward flags prevent duplicate mission/award |
| `dhrondan_mengele_expedition_mission` | D’Rhondan contact owner, `dhrondan_contact_category` | Country-scoped expedition; no map target | Eligible Mengele route, completed craft, no pact/other expedition, `50` PP plus `500` fuel, `180` days | Valid timeout opens the same audience with Mengele-specific text; accepted return grants only Mengele contact | Route invalidation or world end calls the common failure cleanup without Kruger changes | Dedicated Mengele progress/receipt/report flags prevent a second award and never call Kruger Directorate helpers |
| `dhrondan_rebellion_pulse_mission` | D’Rhondan contact owner, `dhrondan_contact_category` | Country-scoped pact host; no world scan | Pact, at least `6` arrivals, Strain at least `30`, chaos at least `600`, `90` days | One random-list resolution at the current tier; revolt warning/event bridge on the revolt branch | If the gate falls below threshold, mission cancellation removes it; no-revolt reactivates only while still eligible | `has_active_mission` guard prevents duplicate pulses, and `dhrondan_rebellion_triggered` stops post-revolt reactivation |

## Cost and requirement clarity

The landing action has one spendable type: exactly `2,000` alien laser weapons, displayed with `£GFX_alien_laser_weapon_equipment_medium` in the decision description, custom cost text, and effect tooltip.

Each expedition action has exactly two spendable types: `£pol_power 50` through the native decision cost and `£fuel_texticon 500` through the custom fuel gate and tooltip; both values also appear in the visible route descriptions and Event `.40` tooltip.

The Honor Accord has one spendable type: `£pol_power 75`; its separate effect text states Strain `-10` and the `180`-day cooldown.

The rebellion pulse has no spendable cost and instead presents the country-scoped thresholds and tier chances.

Every gameplay-changing GUI/decision action in this scope is at or below four distinct spendable cost types, and no fifth cost is hidden in a confirmation window, scripted effect, or secondary panel.

Non-consumed requirements remain separate from spendable costs: contact receipts, state ownership/control, project completion, current host identity, character health and obligation flags, pact state, cooldown flags, arrival count, Pact Strain, chaos, and world-end safety are triggers or custom trigger tooltips rather than cost prose.

The audited player-facing cost strings use texticons for every spendable resource; no literal-only Political Power, fuel, or laser-equipment payment row remains.

## AI validity and route-lock notes

The landing decision uses a valid target trigger and a country-level gate, so AI cannot select a dead, impassable, uncontrolled, unowned, contactless, under-equipped, pending, recovery-locked, or world-ended target.

Landing AI starts at `constant:alien_infantry_landing_ai.standard` and applies only DHR focus/reserve-priority factors; it does not bypass the equipment or state gates.

Kruger and Mengele route decisions use `constant:dhrondan_contact_ai.dominant` (`10000`) and are revalidated in their complete effects before fuel debit or mission activation.

`dhrondan_ai_try_authorize_expedition` is called by Event `.40`; it requires `is_ai`, at least `50` political power, at least `500` fuel, and one valid route, debits the exact political-power amount once, then prefers the Kruger route and falls back to Mengele.

The Honor Accord starts at `constant:dhrondan_contact_ai.low` (`25`) and receives a factor of `4` at Strain `50` or higher; its availability still blocks missing pact, zero Strain, cooldown, active rebellion, and world end.

The hidden missions are not selectable AI decisions and therefore have no separate mission score; they activate only through the guarded source effects and resolve or cancel through their lifecycle triggers.

No route targets a dead country, impossible border, closed project, disabled evolution, or invalid current host in the audited source.

## Rebellion pulse probability acceptance

The eligibility gate is country-scoped and requires pact, arrivals at least `6`, Pact Strain at least `30`, and `global.chaos_meter_value` at least `600`; there is no `every_country`, `every_state`, `on_daily`, `on_weekly`, or `on_monthly` world iteration in the scoped decision, trigger, effect, or event files.

The high tier is checked first and requires arrivals at least `10` and chaos at least `800`, producing a `40%` revolt weight.

The medium tier produces `20%` when arrivals are `8–9`, Strain is at least `50`, or chaos is at least `800` without the high-tier combination.

The qualifying base tier produces `10%` for the remaining eligible states, including six or seven arrivals at chaos `600–799`.

The resolver calculates a complementary no-revolt weight from the constant total `100`, so the declared rows are `10/90`, `20/80`, and `40/60` rather than independent additive chances.

Named acceptance scenarios and expected probabilities:

| Scenario | Arrivals | Strain | Chaos | Revolt weight | Expected revolt |
| --- | ---: | ---: | ---: | ---: | ---: |
| `DHR_LOW_6_30_600` | 6 | 30 | 600 | 10/90 | 10% |
| `DHR_LOW_7_30_799` | 7 | 30 | 799 | 10/90 | 10% |
| `DHR_MEDIUM_8_30_600` | 8 | 30 | 600 | 20/80 | 20% |
| `DHR_MEDIUM_9_30_600` | 9 | 30 | 600 | 20/80 | 20% |
| `DHR_MEDIUM_6_50_600` | 6 | 50 | 600 | 20/80 | 20% |
| `DHR_MEDIUM_6_30_800` | 6 | 30 | 800 | 20/80 | 20% |
| `DHR_LOW_10_30_799` | 10 | 30 | 799 | 10/90 | 10% |
| `DHR_HIGH_10_30_800` | 10 | 30 | 800 | 40/60 | 40% |

The typed MCP scenario inputs supplied the declared temporary weights because the adapter cannot execute the source trigger/helper chain; the resulting probability arithmetic is exact for those declared weights, while tier classification remains source-reviewed rather than claimed as full engine evaluation.

## Kruger Directorate and Mengele separation

Kruger authorization uses the canonical character receipt `dhrondan_kruger_authorization_reward_received` and applies Mandate `+10`, Dependence `+10`, Exposure `+5`, Independent Capacity `+10`, and Grievance `-5` exactly once.

The expedition sets the character obligation flag, removes Kruger roles through the existing role helper, sets the shared and route-specific progress flags, and clears the transaction lock before the mission starts.

Successful Kruger return uses a separate one-time character receipt and applies Mandate `+5`, Dependence `+5`, and Independent Capacity `+5` exactly once before granting the Kruger contact receipt and pact.

Failure or cancellation clears the expedition, audience, route, and duration state and restores the obligation ledger; roles are re-added only when the canonical Kruger remains the valid active, uninjured, and unconfined host.

Mengele uses its own route, progress, contact, report, and failure flags, shares only the expedition cost and duration contract, and does not call either Kruger Directorate mutation helper or write Kruger obligation/pact variables.

Audience authorization revalidates the route immediately before applying the pact, so death, invalid host, injury, confinement, or a late world-end transition cannot produce a stale success or duplicate award.

## Localisation, tooltip, and GUI findings

The contact header text explicitly names Alien Presence and Pact Strain and its description explains their significance and the rebellion response.

The landing text states the exact `2,000` reserve, seven-day reservation, one pending reservation rule, exact refund condition, successful Presence and Strain changes, and the `30/24/18/12` recovery ladder.

Kruger and Mengele descriptions state `180` days, `50` PP, `500` fuel, and their route-specific Directorate behavior; the separate fuel custom tooltip states the exact fuel requirement.

Honor text states `75` PP, Strain `-10`, and the `180`-day cooldown.

The pulse mission text states the `90`-day clock, gate, and `10/20/40%` tiers with their boundaries.

No missing scoped localisation key, literal-only spendable cost, long raw trigger exposed to the player, or vague route tooltip was found in the current Event 016 package; the preceding localisation audit records zero missing keys and zero duplicate scoped definitions.

The normal decision categories have no dedicated scripted GUI. The existing Directorate GUI contains its original profile, meters, and buttons and has no contact or landing controls, so no Event 016 regression or GUI rewrite is indicated.

## Cleanup and exploit-risk notes

Landing cancellation clears the pending flag before refunding and removes the mission and target variables, preventing repeated refund loops.

Landing success clears the pending reservation and does not refund the consumed reserve; the spawn path measures division-count delta and only records telemetry after one cohort materializes.

The single shared expedition flag, route-specific flags, character obligation, one-time authorization/return receipts, and common cleanup prevent repeated Kruger awards, stale audience success, free repeated fuel use, or parallel route activation.

Mengele failure does not restore or mutate Kruger variables unless a pre-existing Kruger obligation is present in the common cleanup, and normal route guards make that state unreachable.

Honor Accord uses a timed `180`-day country flag and clamps Strain at zero, preventing negative-strain farming or cooldown bypass.

The pulse mission refresh is country-scoped, does not reset an active ninety-day timer, removes itself when the gate falls below threshold, and stops after the revolt bridge marks the country as triggered.

No new exploit, free unit loop, equipment farming loop, war-goal spam, core spam, or cooldown abuse was found in this tranche.

## MCP evidence and fidelity

### Probability inspection and evaluation

- Rebellion pool inspection used `hoi4.probability_inspect` with adapter `random_list` on `common/scripted_effects/016_dhrondan_contact_effects.txt`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/478d94f9338c70655191b76629c718c520c6a7781967926b657ac9f4b7063c7a/dae4ac98505c07d079008bb33b6670353398f6a5b8dfdf983db85909c05ef926/probability-inspect-ed0e8caeac0d.json` reported a complete two-candidate pool with no unresolved source inputs.
- Empty-state rebellion evaluation artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/470de8e190b1fbac33cf3bc140b9e2a63ce553af545a75eb40265c58d9b5efc3/b93b9c9b487bc16de8d76bb15533432aec25956529a5f162764dbb357063aa75/probability-d9de218bcf8b904ae4e34a60.json` returned partial analysis with two unresolved dynamic temporary weights, which is recorded rather than treated as a pass.
- Named tier evaluation used scenario set `E016_DHR_REBELLION_TIERS_2026_08_22`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d115007a2b5ef9c85bb46246e44a1db2be38ceb54c4b91347323fa5ee8dbb877/d6e73b2b19b67b8a6da3ae1dfb870a515077b7ada0414f9e8aeb39ed8e51f2ed/probability-c05f0b1b21f6ca9b8c4f24b1.json` returned complete exact `10%`, `20%`, and `40%` rows with no unresolved inputs.
- Tier sweep artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4122e738526d10b8fddbcb5ce9755d38c59e496d1865c9267b1c039f946f5669/dbd095a92915419cb23aaa7f9c771b5ce5d1c5587f2ebddc24800f75b3dc485f/probability-2a8536417c4fa661452024ea.json` completed three sweep points with the expected low-tier dominance warning.
- Boundary evaluation used scenario set `E016_DHR_REBELLION_ACCEPTANCE_BOUNDARIES_2026_08_22`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3ac57570383b04f652280e54c3f24e49b32e1fe853e70ba57dda5431273dfdfb/1d1096cfa2e178df7c0289a985f9dd295fddb55b872549e38520eb878f625aa8/probability-a8179bdcf492527537ea3ccf.json` returned eight scenarios, sixteen candidate rows, zero unresolved inputs, and exact expected boundaries.
- Decision adapter inspection artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36577435a19f5b9cf0c251d88394374594d2d7f6035c1d09f4ec6e2d53da6d1b/4754f057cbfd0465c3b0673db1f01eadd8ccb9017c3f92476896229451380ef3/probability-inspect-4a370bea603b.json` discovered only the status row and did not discover route decisions.
- Mission adapter inspection artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94dade18158d4c477625532767923b82cd75d7ef24e760f8aeab56e9fb92973e/88b326136dc208f94f33740af41b1529a75bd2dd6ceee84095309cb0d24fcce1/probability-inspect-4a370bea603b.json` found no mission AI-weight blocks; forced route evaluations returned `PROBABILITY_SURFACE_EMPTY`.

### Event and focus structure

Focused `hoi4.event_inspect` lint for `{ kind: event, eventId: chaosx.nr16.40 }` returned `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, and no skipped sources; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1097c38c958c9f0e61f15df65b58f81f0152464be83e0ae946beeac170b6d7de/9ff80875117ccc5554d30a784fff7cc418eff90a3b0ab01ffe3e1a730d134f6f/event-lint-2af1fa63424e.json`.

The event report is partial because the large workspace deferred helper and lifecycle projections; its `MCP_INLINE_FILES_TRUNCATED` diagnostic is not treated as complete event-runtime evidence.

Focused `hoi4.focus_inspect` confirmed the DHR focus tree and supplied the landing-network, guarded-descent, and near-space flag consumers; the DHR focus artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6db49791c9e45a3ed40fe480d1699ee9ce5bf04b35976f47848927d6e8184bb2/15cf21453f74d3d661715fce5126c17b6a0286225f1d107a7526601f2b9c1836/focus-inspect.79481ef6da4647c9.json`.

### GUI regression evidence

`hoi4.gui_inspect` for `kruger_directorate_container` was attempted as mandatory read-only regression evidence and failed at artifact allocation with `ARTIFACT_STORAGE_LIMIT`.

`hoi4.gui_render` for `kruger_directorate_container` completed for normal, active, warning, disabled, long-text, and missing-localisation states at 1280x720 and 1920x1080; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3ce9c692f6a8442cd4e7aa62421e8e1f42b42003334e4295784ebc359fb17ea7/498d4208f65c131d6fb83a591040e031deb44cba2c373982d0ee58993b76ae1/kruger_directorate_container-full.svg` was returned with no blocking diagnostics and one inline truncation warning.

No `hoi4.gui_rewrite` was run because no existing Directorate GUI regression was found and no dedicated Event 016 scripted GUI belongs to this scope.

## Meaningful validation completed

- Read and applied the repository, decisions/missions, events, focus-tree, and subagent skills, the required offline Paradox wiki pages, and the relevant vanilla documentation and precedents.
- Reviewed the accepted addendum, acceptance scenarios, prior decision/mission and contact-chain handoffs, current decision/category/trigger/effect/constants/localisation/event/focus sources, and the existing Directorate GUI source.
- Verified exact source constants for `2,000`, `7`, `30/24/18/12`, `50`, `500`, `180`, `75`, `-10`, `90`, arrival/strain/chaos gates, and `10/20/40` pulse weights.
- Verified the touched source has no prohibited `<=` or `>=` operators and no prohibited global `every_country`, `every_state`, `on_daily`, `on_weekly`, or `on_monthly` iteration.
- Compared state-targeted decision structure with vanilla `AFG.txt` and mission lifecycle structure with vanilla `AST.txt`.
- Audited all scoped visible action counts, active missions, cost types, texticons, requirement separation, route locks, cleanup paths, duplicate guards, and player-facing significance.
- Ran the named rebellion probability scenarios and boundary sweep through the installed read-only MCP probability tools.

## Skipped meaningful validation and why

- The custom `chaosx_ai_probability_auditor` pass was unavailable because no callable custom auditor tool was exposed; direct MCP probability evidence is recorded with its fidelity limits and is not claimed as an equivalent replacement.
- A standard decision/category inspector or render was unavailable; ordinary decisions use the normal game decision surface and expose no `windowName` to `hoi4.gui_inspect`.
- The Directorate GUI inspect was blocked by shared artifact storage, although the render route produced a read-only SVG artifact.
- `hoi4.probability_compare` was not run because this audit applied no weighted source patch; there was no before/after source change to compare.
- No `hoi4.gui_rewrite` was run because no GUI patch was justified and the ordinary contact/landing categories do not own a dedicated scripted GUI.
- No in-game run was performed because live consumer validation belongs to the user under the repository instructions.

## Changes and before/after behavior

No gameplay or localisation source changed, so there is no behavior delta to review.

Before this handoff, the source already implemented the accepted landing reservation, contact, route, mission, pulse, AI, cleanup, and tooltip contracts.

After this handoff, the parent has a consolidated acceptance result, line-level source map, named scenarios, probability artifacts, GUI/event/focus MCP evidence, exact unsupported routes, and remaining user-owned validation boundaries without needing to rediscover the audit.

## Concrete recommended fixes

No immediate local gameplay fix is recommended.

The parent should retain the `chaosx_ai_probability_auditor` and standard decision/category MCP blockers in the final completion report, preserve the seven DHR focus layout warnings for the focus owner, and obtain user-owned live acceptance for the ordinary decision UI and mission countdowns.

If the MCP artifact store is repaired, rerun `hoi4.gui_inspect` for `kruger_directorate_container`, rerun the standard decision surface if a route is added, and rerun the same named AI scenarios through `chaosx_ai_probability_auditor` before claiming engine-level AI proof.

## Remaining issues and simplifications

No gameplay simplification, fallback, hidden route, omitted mission, missing localisation, or unapproved GUI redesign was introduced by this audit.

The acceptance claim is source-level plus supported read-only MCP evidence only; it does not claim live game behavior, complete large-workspace event/helper projection, complete decision GUI rendering, or custom-auditor probability evidence.

Plan handoff path: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_final_decision_mission_audit_2026-08-22.md`.
