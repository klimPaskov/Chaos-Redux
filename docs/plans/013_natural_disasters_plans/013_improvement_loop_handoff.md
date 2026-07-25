# Event 013 improvement-loop handoff

> Parent disposition, 2026-07-10: implemented and folded into the live Event 013 package. The blockers and prioritized work below describe the pre-closure audit snapshot; `013_implementation_validation_notes.md` and the final specialist audits contain the current closure evidence. This handoff remains as the improvement-loop provenance record.

> Historical snapshot: the incomplete verdicts and blocker lists below are retained for provenance and are not current implementation instructions. Use `013_event_completion_final_audit.md` and `013_implementation_validation_notes.md` for the current disposition.

Date: 2026-07-10
Mode: plan-only audit
Parent owner: main Event 013 implementation agent
Historical completion verdict at snapshot: incomplete

## Historical outcome

The Event 013 implementation has a strong reusable engine, but the accepted source pack is not complete. The detailed closure plan is `docs/plans/013_natural_disasters_plans/013_implementation_depth_addendum.md`.

This pass changed documentation only. It did not edit gameplay, localisation, UI, assets, the workbook, or skills, and it did not create a commit.

## Preserve before changing anything

- `chaosx.nr13.1` remains the repeatable, non-terminal root.
- `call_natural_disaster` remains the sole reusable public entry point.
- Delayed jobs remain persistent, exact-state, and future-dated.
- History remains call-owned: one Event 013 row per logical Event 013 call, never one row per delayed job.
- The existing 25 family ids, four evolution stages, Natural Disasters cluster, Disaster Barrage, six super-event roles, ten achievement routes, and abnormal-GUI access gate remain in scope.
- Event 046 remains inert, Event 051 remains separate with no heat stacking, and Event 099 remains a placeholder unless the user explicitly accepts the narrow dust bridge.

## Prioritized accepted blockers

### P0 - contract and state safety

1. Finish caller validation and behavior: family groups, weaponized `caller_cost_checked`, supply scale, consumed recovery scale, real aftermath-policy differences, exact-count caps, enum rejection, strict selected-target legitimacy, and defined global-report behavior.
2. Add bounded family suitability weighting. Current targeting is mostly random outside coast and Event 051 heat gates.
3. Handle repeated impacts and owner/controller changes without skipped damage or stranded country queues, cards, missions, abnormal-card entries, reports, modifiers, or achievement state.
4. Consume the existing capacity constants. Live rescue/stabilization/reconstruction caps are fixed at 3/2/2.

Primary files:

- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `common/scripted_effects/chaosx_dynamic_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `common/on_actions/013_natural_disasters_on_actions.txt`

### P0 - 25-family depth

1. Add the 50 missing warning directions. Live coverage is 25 decisions against 75 accepted directions.
2. Turn each family route set into conditional alternatives. Live profiles generally choose one generic default chain.
3. Give each family a real state-modifier profile. Current state modifiers use the same severity-driven supply/movement/attrition/repair/resource fields regardless of family flags.
4. Persist/display the full Part 8 card identity, especially warning result, known deaths or honest direction, linked states, active modifier, and failure date.
5. Give AI the same three warning choices and family-specific costs/route protection as the player.
6. Audit warning cost text against actual affordability and deduction effects.

Primary files:

- `common/decisions/013_natural_disasters_decisions.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `localisation/english/013_natural_disasters_l_english.yml`

### P0 - visible presentation

1. Register every live report/news sprite basename. The event script references 14 report and 24 news sprite basenames; `interface/013_natural_disasters.gfx` currently registers zero of either type.
2. Inventory and register all accepted Event 013 decision/category and idea sprites.
3. Produce, install, register, and manifest the eight missing static abnormal-GUI sprites.
4. Produce the missing abnormal-age and delayed-tsunami super-event images. Only four of six final Event 013 super-event DDS files exist.
5. Produce the exact completed/grey/not-eligible triplets for all ten accepted achievements. None of the 30 accepted final basenames exists; the current eight-id set is obsolete.
6. Reconcile DDS format/provenance and live sprite paths with the asset manifest and GFX handoff. No placeholder or filename fallback is acceptable.

Primary files and folders:

- `interface/013_natural_disasters.gfx`
- `interface/chaosx_super_events.gfx`
- `interface/chaosx_achievements.gfx`
- `gfx/event_pictures/013_natural_disasters/`
- `gfx/interface/013_natural_disasters/`
- `gfx/interface/decisions/013_natural_disasters/`
- `gfx/interface/ideas/013_natural_disasters/`
- `gfx/super_events/013_natural_disasters/`
- `gfx/achievements/`
- `docs/assets/013_natural_disasters/`

### P1 - evolution and abnormal-path fidelity

1. Stop broad Evolution I calls from becoming universally severe. Retain the accepted 3-6 activity range with a mixed local/severe profile.
2. Persist chronological path segments and forecast state when abnormal jobs are scheduled.
3. Render physical arrival order and next-hit prediction in the GUI. The current five-card list is urgency-sorted and must not be labelled as route order.
4. Tighten the delayed-tsunami super-event gate to require separated coastal groups/regions and a delayed independent major arrival, not merely tsunami family plus enough planned hits.

Primary files:

- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_guis/013_natural_disasters_scripted_gui.txt`
- `interface/013_natural_disasters.gui`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `events/013_natural_disasters.txt`

### P1 - achievement route proof

The registry and runtime hooks exist, so do not reimplement them from the stale registry handoff. Instead, prove all ten exact routes and disqualifiers end to end. Pay particular attention to:

- capital and primary-supply-route continuity;
- the required airfield network;
- second-wave and refugee death thresholds;
- partial/abandoned cards not counting as full reconstruction;
- exact-sequence closure under overlapping seasons;
- Maximum Barrage capitulation, corridor, recovery-card, and deadline gates;
- normal-family catalogue groups excluding abnormal substitutions.

The live numeric thresholds are now balance-validation gates rather than missing design decisions.

### P2 - integration, documentation, and final audits

1. Trace normal, cluster, scenario, and external calls to prove one logical history row and correct affected-country reports.
2. Exercise overlapping sequences, all 25 families, all evolutions, all five Barrage types, and all four Barrage intensities.
3. Keep Cluster 5 and SCN-007 statuses incomplete until those scenarios pass.
4. Correct `docs/events/013_natural_disasters.md`; it currently overclaims API validation/scaling, family target priorities, path order, six installed super-event images, achievement icon files, and sprite registration.
5. Mark stale plans/handoffs as superseded or partially resolved instead of using them as current evidence.
6. Align the workbook only after implementation facts stabilize.
7. Run the event-completion, decision/mission, localisation, and asset audit routes before a completion claim.

## Static evidence already established

- 25 accepted family ids are implemented.
- Sequence ranges are baseline 1-3/5-10 days, Evolution I 3-6/4-8, Evolution II 8-18/2-5, and Evolution III abnormal 5-12/1-4.
- Reports are scheduled after impact and delayed jobs do not own Event 013 history writes.
- Affected-country, caller, and scenario integrations route through the public wrapper.
- Event 046 is inert, Event 051 is separate and clears Event 013 heat overlap, and Event 099 is inert.
- Cluster 5 uses five logical Event 013 slots; Disaster Barrage uses five types and four intensities and remains non-terminal.
- Eight abnormal animation pairs have real frame sheets and static fallbacks and are wired.
- Six researched super-event script/audio roles and ten achievement registry routes exist.

These facts should be preserved, but they do not remove the validation gates below.

## Validation gates, not new design blockers

- Runtime trace of exactly one Event 013 history row for normal, cluster, external, and follow-up-heavy calls.
- Reliable affected-country delayed report when the caller is another country.
- No same-day job collision or payload overwrite in two overlapping sequences.
- Plausible baseline, Evolution I, Evolution II, and Evolution III death/damage/recovery bands.
- AI purchase and recovery behavior for strong, weak, wartime, capital, transport, coastal, and dense-state cases.
- All ten achievement successes and all disqualifiers.
- Six super-event once-only, same-sequence, image, and settings-aware audio cases.
- Ownership/control-change cleanup.

If runtime state is ambiguous, add narrow temporary debug lines for the exact sequence/card values and remove all of them before completion. Do not replace scenario evidence with generic brace, operator, or encoding checks in the user-facing completion report.

## Optional work that must not block closure

- Event 099 dust bridge;
- Event 046 activation;
- memorial or long-term rebuilding flavor;
- new disaster families, super-events, achievements, countries, focus trees, generic agencies, or a second GUI;
- architecture rewrites whose only purpose is to match an older planning diagram.

## Documentation disposition warnings

- `013_repo_explorer_map.md` predates the live implementation.
- `013_scripted_system_architecture.md` is a proposed architecture, not a mandate to recreate every ledger when the accepted behavior can be proven in the current queue engine.
- `013_cluster_scenario_handoff.md` contains API gaps that are already resolved in the live call path.
- `013_decision_mission_handoff.md` contains stale hook and variable claims.
- `subagent_handoffs/013_achievement_registry_handoff.md` correctly identifies icon/route requirements but its claim that runtime hooks do not exist is stale.
- `013_asset_audit.md` predates live animation GFX/GUI wiring; retain its missing-static, accepted-icon, missing-super-image, DDS-format, and provenance findings.
- `docs/super_events/013_natural_disasters_super_event_research_addendum.md` controls the accepted six-role package over the earlier four-role research recommendation.

## Files added by this planning pass

- `docs/plans/013_natural_disasters_plans/013_implementation_depth_addendum.md`
- `docs/plans/013_natural_disasters_plans/013_improvement_loop_handoff.md`

No simplification or fallback is proposed. The plan is deliberately bounded to closing accepted source-pack behavior.
