# Event 010 Death Completion Audit Handoff

Audit role: `chaosx_event_completion_auditor`

Scope: final read-only completion audit for Event 010 Death replacing the obsolete Spirit of War/Peace event.

## Verdict

Event 010 Death is broadly implemented and the old Spirit of War/Peace active surfaces appear removed, but at audit time the implementation should not be claimed fully complete yet. There were unresolved spec and accepted-plan gaps that were not merely optional future depth.

Audit-time completion status: incomplete until the blockers below are patched, explicitly queued with reasons, or consciously rejected by the parent. The blocker and queue sections below are retained as audit history; `Parent Resolution` records the fixes applied after this audit, including the later route, Black Atlas, achievement, and world-end portrait implementation.

## Completed Surfaces

- Old Spirit of War/Peace cleanup: active references to `Spirit of War`, `Spirit of Peace`, `War or Peace`, `war_or_peace`, and old symbol/event ids were not found outside historical specs/handoffs/XLSX after excluding the Event 010 spec and audit history surfaces. The old event file and old event pictures/localisation are deleted in the current worktree.
- Core event chain: `events/010_death.txt` keeps `chaosx.nr10.1` as the hidden root. `death_consume_current_state` in `common/scripted_effects/010_death_effects.txt` is the shared consumption path for origin, island spread, wither, coastal jumps, triggerable scenarios, and world-end footholds.
- Reveal/world-end/final branches: reveal uses `death_reveal_from_current_state`; world-end uses `death_can_start_world_end` and `death_try_start_world_end`; final world-consumed handling uses `death_whole_world_consumed` and super-event 65. The world-end trigger correctly checks consumed continent plus Chaos threshold in `common/scripted_triggers/010_death_triggers.txt:207`.
- Country package: `DTH` is registered in `common/country_tags/chaosx_countries.txt`, Death has black country color in `common/countries/Death.txt`, Zol is defined in `common/characters/DTH.txt`, and `history/units/DTH_1936.txt` contains templates without deployed starting divisions.
- Decisions and missions: public/compact decisions are gated after reveal and defeat, the compact war declaration is leader-only, custom cost localisation variants exist, pre-reveal decision text no longer names Death, quarantine-line hold is implemented as a timed mission, and post-defeat wasteland outposts count only after `death_defeated`.
- Focus tree: `common/national_focus/010_death_focus_tree.txt` contains 26 focus nodes. `interface/010_death.gfx` registers the matching 26 base focus sprites plus shine variants. The tree has a fixed-purpose lane structure and keeps Dark Methods, Black Oath, Herald, and Black Apostolate as living-country decisions rather than DTH focus ids.
- Triggerable scenario: SCN id is `#006` in `localisation/english/chaosx_gui_l_english.yml:76`, and the scenario selection gate dispatches Death variants from `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt:47`.
- Super-events and audio: Death super-event ids 62-65 are wired through scripted localisation, `interface/chaosx_super_events.gfx`, `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset`. Audio files exist and `ffprobe` reports valid 44.1 kHz OGG streams for the four Death super-event tracks.
- Achievements: Death achievements, including Dark Methods, Black Oath, and Black Apostolate achievements, are registered in `common/achievements/chaos_redux_achievements.txt`, documented in `docs/systems/custom_achievements.md`, localised in `localisation/english/chaosx_achievements_l_english.yml`, and wired in `interface/chaosx_achievements.gfx`.
- Documentation: `docs/events/010_death/overview.md`, asset manifests, super-event research docs, and the spreadsheet handoff describe the current implementation, SCN-006, implemented route surfaces, and completed asset package.

## Resolved Audit-Time Blockers

1. Triggerable scenario launch context cleanup from the accepted scripted-system plan was missing at audit time.
   - Parent resolution: `death_cleanup_triggerable_scenario_context` now clears the Death scenario bypass context after SCN-006 finishes. The current SCN-006 path uses one Instant Outbreak type and no longer has a Last Shores scenario type or ghost-tier shortcut.

2. Defeat aftermath super-event 64 is less gated than the source spec requires.
   - Spec evidence: `docs/specs/010_death_specs/specs/010_death_spec_part_1_core_flow.md:210` says the defeat aftermath super-event should fire only after reveal and after a large population/crisis threshold, such as more than 10 million consumed population, a mainland foothold, or a world-end attempt.
   - Implementation evidence: `common/scripted_effects/010_death_effects.txt:1148` fires `death_emit_defeat_super_event` whenever `death_publicly_revealed` is set. There is no large-consumption, mainland-foothold, or world-end-attempt threshold in that gate.
   - Impact: this is an undisclosed simplification against the super-event spec.

3. Zol's unique non-political leader trait direction is not implemented or queued.
   - Spec evidence: `docs/specs/010_death_specs/specs/010_death_country_package_and_focus_tree.md:45` asks for a unique leader trait direction such as `God of Death` that clarifies Death does not use normal politics/manpower.
   - Implementation evidence: `common/characters/DTH.txt:9` defines Zol as a country leader with ideology only; no trait is assigned, and no corresponding active trait/localisation surface was found.
   - Impact: country identity is slightly shallower than the accepted country package spec.

4. Death receives starting manpower and stockpile equipment during setup despite the country package spec saying no recruitable manpower or starting equipment.
   - Spec evidence: `docs/specs/010_death_specs/specs/010_death_country_package_and_focus_tree.md:64` through `:72` says Death starts with no units, no recruitable manpower, and no starting equipment.
   - Implementation evidence: `common/scripted_effects/010_death_effects.txt:97` adds 20,000 manpower and `:98` through `:101` adds 5,000 infantry equipment inside `death_setup_country`.
   - Impact: this may be an intentional implementation support pool for later host spawning, but it is not disclosed in the docs or queued as a spec deviation.

## Superseded Audit-Time Queue

These items were considered non-blocking at audit time only because they were then hidden/unwired. The later parent implementation resolved them instead of leaving them queued:

- Dark Methods and Black Oath gameplay routes are implemented as living-country decisions.
- Herald of Zol and Black Apostolate route flags/art are implemented and wired.
- Black Atlas scripted GUI assets are implemented with stable sizes, final paths, and target GUI surfaces.
- The animated Zol/world-end portrait package is implemented as an eight-frame source-frame sheet with static fallback.
- Expanded focus-lane icons have dedicated generated DDS files under stable filenames.
- `death_friend_of_zol` and `death_book_burner` achievement art is wired because Black Oath and Dark Methods are implemented.

## Accepted Plans and Disposition

- `focus_tree_depth_followup_plan.md`: implemented. The file marks the plan as implemented by parent, and the active tree is a 26-node lane tree.
- `decision_mission_audit_handoff.md`: mostly implemented/superseded. The specific high-risk findings around cost localisation, defeat gates, compact leader-only declaration, timed mission, recaptured modifier stacking, and post-defeat outpost achievement counting are fixed in the current surfaces.
- `country_package_audit_handoff.md`: partially implemented/superseded. DTH tag/history/parties/no deployed units are handled, but Zol's unique trait and the starting stockpile/manpower deviation remain unresolved.
- `localisation_audit_handoff.md`: mostly implemented/superseded for pre-reveal decision text and missing keys. One visibility uncertainty remains: the previous audit warned to verify whether Event Details can expose Death before reveal. Current code still registers Death event detail previews in `common/scripted_effects/chaosx_events_log_effects.txt:1434`, but this static audit did not prove whether the Event Details catalog entry is visible before discovery.
- `scripted_system_architect_handoff.md`: not fully implemented. The triggerable scenario cleanup helper/call is missing.
- `spreadsheet_doc_handoff.md`: documented as updated. This audit did not reopen the workbook; the handoff says row 10 and SCN-006 were updated and reopened successfully.

## Task-Specific Validation Performed

- Checked obsolete Spirit of War/Peace strings and old asset ids outside historical/spec/handoff surfaces; no active hits found.
- Verified focus count is 26 in `common/national_focus/010_death_focus_tree.txt` and matching focus sprites are registered in `interface/010_death.gfx`.
- Verified Death world-end gate uses consumed-continent plus Chaos threshold, not a mainland count shortcut.
- Verified Death super-event audio file paths are wired and all four OGG files report valid 44.1 kHz streams through `ffprobe`.
- Verified SCN-006 UI id text is `#006`, not `#010`.

## Validation Gaps Before Final Commit

- Run a task-specific parser/load check for Event 010 plus SCN-006 after fixing or accepting the cleanup gap. In particular, verify that repeated SCN-006 launches do not leave stale launcher/global context.
- Smoke the defeat aftermath branch with a low-post-reveal defeat and a high-crisis defeat to confirm whether super-event 64 should be threshold-gated.
- Verify Event Details visibility in the actual UI path: if Event 010 details can be opened before reveal, the Death name/evolution previews need either gating or intentionally accepted spoiler behavior.
- If the manpower/equipment pool is intentional for host spawning, document that it is a hidden implementation pool, not normal starting capability; otherwise remove or defer it into host-spawn effects.

## Remaining Blockers At Audit Time

- Missing `death_cleanup_triggerable_scenario_context` implementation/call or an explicit rejection/queue decision.
- Missing defeat-after-reveal crisis threshold for super-event 64 or an explicit accepted simplification.
- Missing Zol leader trait or an explicit accepted simplification.
- Undocumented starting manpower/equipment pool deviation.

## Recommended Next Actions At Audit Time

1. Patch or explicitly queue the triggerable scenario cleanup helper from the accepted scripted-system plan.
2. Add the defeat super-event threshold gate, or update the spec/docs to say public reveal alone is sufficient.
3. Add Zol's non-political trait and localisation, or document why it is deferred.
4. Resolve the Death setup manpower/equipment mismatch by moving the support pool into host-spawn effects or documenting the hidden pool.
5. Verify Event Details pre-reveal visibility before final completion claim.

## Improvement Loop Recommendation

Do not spawn `chaosx_improvement_loop_planner` for this audit finding set. The remaining issues are implementation/spec-disposition gaps, and the broader depth items already have queued plans or future-work entries.

## Parent Resolution

Resolved after this audit:

- `death_cleanup_triggerable_scenario_context` was added in `common/scripted_effects/010_death_effects.txt` and called at the end of `trigger_death_scenario` in `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`.
- Defeat aftermath super-event `64` now uses `death_should_emit_defeat_super_event`, requiring public reveal plus world-end, at least 10 million consumed population, or at least three mainland states consumed.
- Zol now has the non-political `death_god_of_death` country leader trait, with localisation in `localisation/english/010_death_l_english.yml`.
- The hidden setup manpower/equipment pool was removed from `death_setup_country`; scripted host effects still provide only per-host dummy manpower/equipment when a host is created.
