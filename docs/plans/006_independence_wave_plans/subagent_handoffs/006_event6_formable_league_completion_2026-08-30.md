# Event 006 formable, League, evolution, and achievement completion audit handoff — 2026-08-30

## Disposition

This bounded audit found no safe, source-backed gameplay defect in the Event 006 formable, League, evolution/re-entry, or achievement wiring that can be repaired without changing the accepted design.

No gameplay, localisation, GUI, country, formable, achievement, weighted-logic, or map files were changed in this tranche.

The existing 2026-08-29 audit handoffs already contain the earlier safe formable cost-localisation correction and the evolution/League/achievement source review; this receipt does not duplicate or revert that work.

The remaining registry gap is explicit scope rather than an accidental missing branch: the 48-row formable family registry is defined, while 14 state-puzzle families have reviewed identity and integration adapters and the other 34 families remain fail-closed until their source package, territorial proof, tag, flag, and integration contracts are admitted.

## Reviewed authority

The review used `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`, `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv`, and `docs/specs/006_independence_wave_specs/matrices/006_achievement_matrix.csv`.

The current source review covered `events/006_independence_wave.txt`, the Event 006 scripted effects and triggers, the shared formable state-puzzle GUI, the Event 006 decision categories and decisions, the evolution and League on-actions, the achievement definitions/triggers/effects, and the Event 006 localisation and achievement icon surfaces.

The prior dated handoffs and resume packet were checked for superseded work, provisional join changes, admitted-family counts, cleanup boundaries, and unresolved runtime evidence instead of reimplementing completed work.

The required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, and the relevant scripted GUI/country-creation pages were consulted alongside the vanilla documentation for effects, triggers, script constants, localisation formatting, and dynamic variables.

## Source findings

### Event entry and pre-event isolation

`chaosx.nr6.1` remains a hidden committed-plan entry point, and the public `chaosx.nr6.2` report is the first public Event 006 surface.

The retired `chaosx.nr6.3` callback only clears stale legacy crisis state; it cannot open an Event 006 pressure category, mission, cost, queue, or pre-event history surface.

The active-origin predicate requires the committed Event 006 origin flag and the Event 006 liberation-origin value, while the root event writes the runtime-unlock receipt only when the joint or standalone package has actually committed.

Overlay categories additionally require `is_independence_wave_overlay_runtime_unlocked`, so a stale package flag cannot expose an overlay before the public runtime gate.

### Formable registry and state-puzzle families

`independence_wave_formable_load_selected_family_profile` loads one of all 48 reviewed registry profiles into scoped variables, derives method support, and sets the profile-loaded flag; it does not fabricate a family or a country tag.

`independence_wave_formable_build_member_and_anchor_ledgers` clears and rebuilds generation-aligned member, anchor, consent, and integration ledgers from the bounded active-country registry, with no all-country or periodic world scan.

`independence_wave_formable_commit_selected_family` requires the shared readiness and congress-proof contract, dispatches the family identity and integration adapters, sets the committed transaction only after both adapters succeed, and starts the family-owned post-formation progression where one exists.

The reviewed state-puzzle adapter pairs are FORM-01, FORM-02, FORM-03, FORM-04, FORM-07, FORM-08, FORM-09, FORM-12, FORM-13, FORM-16, FORM-18, FORM-39, and FORM-48.

The 14 state-puzzle directories under `docs/formables/state_puzzles/` match that admitted set, and the adapter IDs are exactly `1`, `2`, `3`, `4`, `7`, `8`, `9`, `12`, `13`, `16`, `18`, `39`, and `48` for both identity and integration dispatch.

FORM-01, FORM-02, and FORM-04 intentionally use the dedicated `006_independence_wave_form01_02_04_effects.txt` integration adapters rather than the generic member-ledger branch.

FORM-03 retains its dedicated Low Countries charter and sovereign-associate path, including the Belgian delegation exception, instead of being weakened into the generic transaction lane.

FORM-05 retains its dedicated maritime charter category and readiness contract; generic discovery intentionally excludes it because its authoritative charter surface owns the route.

FORM-08 and FORM-09 retain their post-formation progression categories and fail-closed territory/readiness checks.

FORM-12 and FORM-13 retain the distinct IW-043 route surfaces, three external consenting-member requirement, and distinct anchor proof.

FORM-18 retains the IW-058 route surface, former-host requirement, sovereign anchor, corridor receipts, and defensive-only military proof.

The generic registry trigger and effect dispatch leave all unreviewed family rows fail-closed; no fallback country, state, X-ending tag, annexation, or copied integration route is introduced.

The shared scripted GUI remains attached to 17 Event 006 formable categories, including the generic formable category, membership and transaction categories, the dedicated FORM-01/02/03/04/05/08/09/39/48 surfaces, and the IW-043/IW-058 surfaces.

### League state machine and re-entry

The canonical League effects implement generation-aligned founder and member arrays, regional rebuilding, contribution/confidence values, and the phase sequence from informal network through regional conferences, congress preparation, charter vote, consultative/formal League, durable League, crisis, reform, rival Leagues, dissolution, and restart.

The League gates require the accepted live-origin, founder, recognition/network, congress-preparation, strategic-problem, cohesion, common-cause, and non-patron-domination conditions before formal formation.

`independence_wave_reconcile_registries`, `independence_wave_reconcile_league_founder_registry`, and `independence_wave_reconcile_league_member_registry` prune stale generations and rebuild only from aligned active entries.

`independence_wave_rival_bloc_reunify_into_league` copies the rival member array before unregistering and re-registering active non-client members, preserving generation safety on re-entry.

`independence_wave_dissolve_league_to_network` clears member and founder arrays, discredits former members, clears the leader and member phase state, and returns the shared phase to a restartable network state through `independence_wave_restart_informal_network`.

`independence_wave_formable_cleanup_runtime`, the generation reset, and `independence_wave_end_active_origin` clear transaction flags, missions, ledgers, family-owned progression state, active-origin records, and global League targets at their respective ownership boundaries.

### Evolution activation and re-entry

The five canonical stages are Replicable Independence, Dormant Nations, Armed Birth, Sovereign Congress, and Open Sovereignty, represented by their existing Event 006 evolution flags, country application helpers, and dynamic evolution log context.

`independence_wave_prepare_evolution_for_incident` reconciles the active registry, applies the pre-fire plan only before the first active origin, synchronizes already-active stages to later-born countries, and schedules the next check through the existing Event 006 MTTH contract.

`independence_wave_try_next_active_evolution` activates at most one missing enabled and tier-eligible stage per due Event 006 invocation, while disabled stages are skipped independently rather than blocking later stages.

Evolution delivery is idempotent over the aligned active-country array, and pending log flags preserve the evolution row when a stage fires before an actor exists.

Generation reset and active-origin cleanup remove per-generation evolution feedback and application flags without creating a second origin or a periodic world iteration.

### Achievement wiring

All 16 matrix IDs have exactly one definition in `common/achievements/chaos_redux_achievements.txt`, one corresponding final proof trigger in `common/scripted_triggers/006_independence_wave_achievement_triggers.txt`, matching English name/description/possible/completion localisation, and complete/grey/not-eligible DDS triplets.

The proof triggers preserve the shared sovereign actor gate and the row-specific host, League, formable, route, scenario, patron, arbitration, rescue, and remnant disqualifiers from the matrix.

The achievement effects and narrow engine callbacks cover country reset, recognition/capacity, patron history, host settlement, reconquest loss/recovery, League founding and cross-regional clocks, rescue, radical containment, scenario survival, arbitration, coercion/expulsion, and host-remnant survival without a daily, weekly, monthly, or all-country scan.

## Reusable helper map

The existing helpers are sufficient for this tranche, so no new helper was created.

- `independence_wave_formable_load_selected_family_profile` — country scope; input is the selected registry family; outputs profile region, method mask, discovery mode, minimum member/consent/anchor counts, AI willingness, risk tier, and derived method flags; side effects clear the previous profile and set the loaded-profile flag; call sites are registry selection, discovery/preparation gates, transaction categories, and commit readiness.
- `independence_wave_formable_build_member_and_anchor_ledgers` — country scope; input is the active generation registry and loaded profile; outputs aligned member, generation, region, anchor, contribution, confidence, and consent arrays; side effects clear and rebuild the temporary/frozen ledgers; call sites are invitation, signature, preparation, and commit flows.
- `independence_wave_formable_commit_selected_family` — country scope; input is a fully validated selected family and congress transaction; outputs committed transaction state, family identity, territory integration, and post-formation progression; side effects reserve the proposer target, invoke meta-dispatched identity/integration adapters, remove the formation mission, and clear pending flags; call sites are the shared transaction decisions and AI/human commit paths.
- `independence_wave_formable_cleanup_runtime` — country scope; input is the current generation/family state; outputs no persistent transaction state; side effects remove the formation mission, call family-specific cleanup, clear ledgers/profile/flags/variables, and preserve intentional historical first-stage receipts; call sites are transaction failure, generation reset, and active-origin end cleanup.
- `independence_wave_open_regional_conference`, `independence_wave_complete_congress_preparation`, `independence_wave_open_charter_vote`, `independence_wave_proclaim_consultative_league`, `independence_wave_proclaim_formal_league`, `independence_wave_upgrade_consultative_league`, `independence_wave_mark_league_durable`, `independence_wave_enter_league_crisis`, `independence_wave_reform_league`, `independence_wave_split_league`, `independence_wave_normalize_reformed_league`, `independence_wave_reunify_rival_leagues`, `independence_wave_dissolve_league_to_network`, and `independence_wave_restart_informal_network` — global phase scope with country-owned entry calls; inputs are validated phase, founder/member arrays, route input, and League values; outputs are the next phase, dates, flags, leader, and member arrays; side effects clear conflicting phase flags, reconcile arrays, update event targets, refresh ideas, and write achievement milestones.
- `independence_wave_try_next_active_evolution` and `independence_wave_prepare_evolution_for_incident` — global/Event 006 invocation scope; inputs are the current evolution date, tier, enabled-stage settings, and aligned active registry; outputs one activated stage or a scheduled next check; side effects deliver idempotent country transitions, defer actor-less log rows, seed League values where required, and avoid periodic world scans.
- `independence_wave_achievement_refresh_country_state`, `independence_wave_achievement_mark_formal_league_founders`, `independence_wave_achievement_record_rescue`, `independence_wave_achievement_record_arbitration`, `independence_wave_achievement_refresh_host_remnant_peace`, and the related achievement on-actions — country or narrow engine-callback scope; inputs are transaction, war, peace, state-control, subject, rescue, arbitration, or survival facts; outputs row-specific proof flags, dates, counters, and disqualifiers; side effects are idempotent tracker writes and bounded cleanup.

## Constants and tuning plan

The shared tuning source remains `common/script_constants/006_independence_wave_constants_registry.txt`.

It centralizes formable profile metadata, method bits, member/consent/anchor thresholds, transaction costs and risk bands, League phase/value thresholds, evolution tiers and MTTH bounds, evolution feedback deltas, achievement durations, and survival thresholds.

No new constants or magic values were added, and no constant was duplicated across a formable, League, evolution, achievement, decision, or localisation file.

The previous civic command-power localisation correction already exposes the existing `constant:independence_wave_formable_cost.civic_command_power` value and was not repeated here.

## Event-target and cleanup plan

Formable transaction targets are generation-scoped and include `independence_wave_formable_proposer`, `independence_wave_formable_candidate_country`, `independence_wave_formable_invited_candidate`, the Belgian delegation candidate, frozen consent snapshots, and family-owned cleanup targets.

League targets include the main League leader and rival-bloc leader or invitation targets; global targets are explicitly cleared by League initialization, dissolution, rival-bloc cleanup, and active-origin end paths.

Evolution actor targets are short-lived event targets used to write the Event Log row and pending flags; they do not become a second persistent origin pointer.

The existing cleanup boundary is retained: family adapters clear family-owned state, the generic formable cleanup clears transaction state and ledgers, League cleanup clears phase/member/leader state, and `independence_wave_end_active_origin` clears the active-generation records and achievement lifecycle state.

No new event target, global event target, flag, variable, or cleanup helper was needed.

## Migration plan

No migration is required because the shared registry already routes all admitted formable families through one profile/ledger/readiness/commit/cleanup contract.

The dedicated FORM-01/02/04, FORM-03, FORM-05, FORM-08/09, FORM-16, FORM-39, FORM-48, IW-043, and IW-058 adapters remain the owning implementations for their reviewed family behavior.

The 34 unadmitted rows remain fail-closed and must not be promoted by this audit; a future admission tranche needs source-backed country, territory, flag, identity, integration, GUI, and validation evidence before adding adapters.

## Validation evidence

`python .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, 40 total runtime adapters, 32 attested packages, and 29 compatible reservation groups; it also confirmed the retired pre-event crisis surface and the accepted all-anchors -> compact -> extended -> lock order.

`python .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 mode/intensity cells and eight documented edge cases.

`python .tools/audit_event6_flags.py --strict` passed with 102 registered Event 006 tags, 102 complete flag families, and zero incomplete families.

`python .tools/audit_event6_country_api.py` passed with 242 broad API tags, 191 resolved carriers, zero missing/duplicate bindings, and the IW-031 Kosovo crosswalk intact.

`python .tools/audit_event6_form16.py` passed the admitted ARM/GEO/AZR FORM-16 contract, including exact states 229/230/231, consent/refusal, mutation, generation, vote, and rollback/cleanup checks.

`python .tools/audit_event6_gui_matrix.py` passed the 17-category semantic matrix, including five recognition frames, three dependency frames, four League frames, four formable frames, and cleanup of all four frame variables plus the animation flag.

A read-only mechanical crosswalk found 48 formable matrix rows, 48 profile-family constants, the exact 14 identity/integration adapter IDs listed above, 16 achievement matrix rows, zero missing achievement definitions/triggers/localisation keys, and all 16 complete/grey/not-eligible achievement icon triplets.

The read-only `hoi4.gui_inspect` result for `chaosx_independence_wave_formable_state_puzzle_window` was complete with 93 inspected elements, zero missing or unsupported elements, and no visible overlap. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2e0149b541dc6d902dadf6be686f5887dd6d7c31d185e827ba405eeb3893937/6438a47a96cbd334f0a369354d6da388efa1c5018ac8042fedb04df25521f9a2/gui-inspect.9731b1c6ba569ce2.json`; revision `9731b1c6ba569ce267cac699f2fbe85189d87ff509df390e0e29b88dc7bed8ec`.

The read-only `hoi4.map_inspect` result covered all 43 unique state-puzzle state IDs, found no unknown or missing IDs, and reported valid selected-state membership and networks. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee5ac5bb15ed9835c8f6411788ce252f63c1ab89e202bf318ca1ddb66695f2d9/9e2e85ed287d800632b9440955fef1db2dcffeec039bd0ebbb00b91ebb6dfd50/map-inspect.2f75eed17d86e3ed.json`; revision prefix `2f75eed17d86e3ed`.

The Event 006 trace inspection completed only as a whole-workspace partial graph with 9,643 events, 15,012 options, 37,953 edges, 8,537 unresolved nodes, 23 blocking diagnostics, and 24,647 issues. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c84b6ced12d8642122c951bb3f55ffb0533a0c5faaca07841b6e1287cbc4af7/6bf2bfcaaa43f84d9faf584b83e2905bac85c7a99b5069f2cd65f903f3ff2fdd/event-trace-55c38793c7fb.json`.

The Event 006 lint inspection likewise completed as a whole-workspace partial result with 9,643 events, 15,012 options, 37,959 edges, 8,543 unresolved nodes, 8 blocking diagnostics, and 2,180 issues. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/294acda215cfb704e98ae8a7843c77b270a72a4ee484e28276d0e28e0e540629/5e44ceb0c0d76ac6d2af61643e54266fc9a0e9c72149a499a2a19555b983fab9/event-lint-903a0ec1e1c7.json`; revision `903a0ec1e1c79d4d289cdfc3a91862032b64986b4a47ff563fda9057305390cb`.

## Evidence blockers and limitations

Reading the Event trace/lint artifact through `read_mcp_resource` was blocked because the server returned `Artifact provenance manifest is unavailable`; the partial MCP counts above are recorded, but they are not treated as a complete Event 006 engine proof.

The map inspection overall validation was false because the global map diagnostic budget retained 1,999 and omitted 2,655 unrelated `MAP_PORT_ADJACENT_SEA_INVALID` and `MAP_BUILDING_POSITION_INVALID` diagnostics; the selected Event 006 state membership and network checks were valid, and no unrelated map positions were changed.

The GUI inspection was read-only and clean, so no GUI rewrite or before/after comparison was warranted.

No weighted AI, MTTH score, random list, or probability-bearing helper was changed; therefore no probability patch or probability comparison was required for this tranche.

Live Hearts of Iron IV execution, save/load, achievement-award, and in-game formable mutation validation remain outside this worker's permitted surface.

## Simplifications, omissions, and follow-up

No gameplay simplification, fallback country, invented route, duplicate helper, localisation omission, weighted-logic adjustment, or unrelated-file edit was made.

This handoff does not claim that all 48 formable families are playable; it records the accepted 14-family runtime admission and the intentional fail-closed boundary for the remaining 34 rows.

Parent follow-up is to rerun the Event 006 MCP event trace/lint and any live consumer/save-load scenarios when the artifact provenance route is repaired, and to open a separate source-backed admission tranche before promoting any additional formable family.
