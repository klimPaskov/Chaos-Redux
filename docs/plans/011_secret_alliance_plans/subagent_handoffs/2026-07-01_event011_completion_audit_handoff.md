# Event 011 Secret Alliance Completion Audit Handoff

Date: 2026-07-01
Role: read-only completion auditor

## Scope And Reading

Audited current repo files only. No gameplay, localisation, asset, docs, or spreadsheet files were patched except this audit handoff.

Required reading completed:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/xlsx/SKILL.md` for read-only spreadsheet inspection
- Offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, graphical assets, interface modding, and scripted GUI context
- Vanilla docs for effects, triggers, script concepts, script constants, and localisation objects/formatting as needed
- Full Event 011 source package under `docs/specs/011_secret_alliance_specs/`
- Current Event 011 implementation files and handoffs under `docs/plans/011_secret_alliance_plans/subagent_handoffs/`

## Overall Status

Event 011 is not completion-ready against the requested pass/fail requirements.

The hidden formation, evolved opening, war-trigger reveal hook, localisation concealment, event log routing, asset registration, and spreadsheet row are substantially present. The main blockers are decision/mission depth, route-aware AI, incomplete idea implementation, simplified achievement tracking, stale documentation claims, and unresolved handoff risks.

## Completion Status By Surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Hidden baseline compact | Proven for baseline; weak for all evolved profiles | Baseline target availability requires three valid minor candidates in `common/scripted_triggers/011_secret_alliance_triggers.txt:47-76`; candidate trigger excludes major, faction member, subject, capitulated, target, and war-with-target countries at `common/scripted_triggers/011_secret_alliance_triggers.txt:28-45`; baseline constant is 3 in `common/script_constants/011_secret_alliance_constants.txt:44`; hidden start does not create a faction in `common/scripted_effects/011_secret_alliance_effects.txt:377-396`. |
| War-trigger reveal | Proven with edge risk | `on_war_relation_added` calls Event 011 at `common/on_actions/chaosx_on_actions.txt:171-174`; reveal trigger checks ROOT/FROM target/core-member directions at `common/scripted_effects/011_secret_alliance_effects.txt:1653-1672`; reveal exposes members, attempts public faction creation, and declares war for valid core members at `common/scripted_effects/011_secret_alliance_effects.txt:1540-1620`. Edge risk: public faction creation only succeeds if the selected leader is not already in a faction at `common/scripted_effects/011_secret_alliance_effects.txt:1508-1523`; runtime handoff also flags this risk. |
| Evolutions I/II/III | Partial | Active evolution effects exist at `common/scripted_effects/011_secret_alliance_effects.txt:1277-1353`; pre-fire opening supports wider minors and major-patron opening at `common/scripted_effects/011_secret_alliance_effects.txt:121-195` and `246-273`. Evolution III can start public crisis, second major selection, and final crisis scheduling. Depth remains simplified around second-major behavior and final crisis ownership. |
| Evolution II decision system | Partial | Category opens through `secret_alliance_can_open_counter_pact_category` at `common/scripted_triggers/011_secret_alliance_triggers.txt:174-197`, and the category description shows suspicion/evidence/preparedness/counter-network/known links at `localisation/english/011_secret_alliance_l_english.yml:75`. Most mapped decisions exist, but key spec missions are still instant cooldown decisions and map/unit/supply objectives are missing. |
| Evolution III confrontation | Partial | Public confrontation decisions exist at `common/decisions/011_secret_alliance_decisions.txt:599-683`; second major selection exists at `common/scripted_effects/011_secret_alliance_effects.txt:1357-1369`; final crisis mission/window exists at `common/decisions/011_secret_alliance_decisions.txt:753-787` and `common/scripted_effects/011_secret_alliance_effects.txt:1642-1650`. The second major is random among broad candidates, and the hidden event plus visible mission duplicate final-crisis lifecycle ownership. |
| Operations | Mostly present but simplified | Baseline and evolved operation families exist at `common/scripted_effects/011_secret_alliance_effects.txt:1107-1257`. Effects are mostly variable/event pulses rather than map-state outcomes. |
| Ideas | Incomplete | Spec requires Prepared Security Network, Compromised Ministries, and Exposed Pact Government in `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_3_counter_pact_decisions.md:158-161`; implementation defines six ideas only at `common/ideas/011_secret_alliance_ideas.txt:10-78` and lacks those distinct spirits. |
| AI behavior | Incomplete | Spec requires role-aware behavior for cautious minors, aggrieved neighbors, major patron, second major, target AI, and neutrals at `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_4_ai_assets_achievements.md:11-18` and acceptance at line 153. Current implementation uses generic random member/patron selection and broad strategies at `common/scripted_effects/011_secret_alliance_effects.txt:313-316`, `1041-1048`, `1053-1068`, and `1357-1369`, plus shallow decision `ai_will_do` blocks. |
| Localisation concealment | Mostly proven | The first popup avoids revealing the pact at `localisation/english/011_secret_alliance_l_english.yml:2-5`, matching the spec line at `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_1_core.md:125`. The category exposes values, not hidden names, at `localisation/english/011_secret_alliance_l_english.yml:75`. Event details intentionally describe the premise in catalog/detail context at `localisation/english/011_secret_alliance_l_english.yml:262-270`; localisation audit handoff records this as an accepted wording decision. |
| Assets and animation | Mostly proven, with one disclosed simplification and unused GUI assets | Sprites and frame animations are registered in `interface/011_secret_alliance.gfx:1-128`; asset manifest marks final DDS and animated packages complete in `docs/assets/011_secret_alliance/manifest.md:23-98`. The evidence-meter highlight is explicitly simplified due missing GUI geometry at `docs/assets/011_secret_alliance/manifest.md:95`, and no Event 011 scripted GUI is implemented, so board/meter/card assets are not used by a scripted GUI surface. |
| Achievements | Partial | All eight achievement definitions exist at `common/achievements/chaos_redux_achievements.txt:1845-1923`, but tracking is simplified. Spec requires disqualifier tracking and mastery conditions at `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_4_ai_assets_achievements.md:123-132` and acceptance at line 157. Current completion checks set `no_factory_lost`, `prepared_border`, and `ten_signatures` from broad flags/variables at `common/scripted_effects/011_secret_alliance_effects.txt:1739-1813`. |
| Event logs/details | Mostly proven | Event name mapping exists at `localisation/english/chaosx_event_names_l_english.yml:13`; Event Details routing exists at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4626-4627`; evolution title/body routing exists at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:9753-9796`; Event 011 records evolution entries at `common/scripted_effects/011_secret_alliance_effects.txt:1394-1437`. |
| Documentation | Partial/stale | `docs/events/011_secret_alliance.md` exists and lists surfaces, assets, achievements, and flow. It incorrectly claims timed missions are used for rail protection, officer protection, factory repairs, allied observers, border searches, crossing closures, patrols, and consultations at `docs/events/011_secret_alliance.md:52`, while those are mostly instant decisions in `common/decisions/011_secret_alliance_decisions.txt:116-250` and `392-595`. |
| Spreadsheet | Present but not validated complete | Event row exists in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Events` row 12, with details and three evolution columns populated. Current row status is `Needs Testing`, so spreadsheet alignment is not a completion claim. |
| Cleanup | Partial | Cleanup helpers clear flags/ideas/event targets/arrays at `common/scripted_effects/011_secret_alliance_effects.txt:23-119`; peace/capitulation cleanup hooks exist at `common/on_actions/chaosx_on_actions.txt:201-203` and `911-913`. Runtime handoff flags residual array-mutation risk in `secret_alliance_recalculate_member_counts` at `common/scripted_effects/011_secret_alliance_effects.txt:454-497`. |

## Findings

### High: Counter-pact missions are not implemented to spec depth

Requirement 4 is incomplete.

The spec maps `Guard the rail offices`, `Secure industrial districts`, and `Watch the suspected frontier` to timed missions with supplied divisions, named rail/industrial/border states, and failure consequences at `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_3_counter_pact_decisions.md:71-72` and `102`. The implementation keeps these as instant cooldown decisions: `secret_alliance_guard_rail_offices` at `common/decisions/011_secret_alliance_decisions.txt:116-134`, `secret_alliance_secure_industrial_districts` at `136-154`, `secret_alliance_harden_ports_and_cables` at `196-214`, and `secret_alliance_frontier_watch` at `392-410`.

Only three actual missions exist at `common/decisions/011_secret_alliance_decisions.txt:685-789`, and they check national variables rather than named states, supplied divisions, border-state coverage, port control, or supply. This also contradicts the event doc claim at `docs/events/011_secret_alliance.md:52`.

### High: AI behavior is generic compared with the required role matrix

Requirement 6 and focused AI coverage are incomplete.

The spec calls for role-aware behavior for cautious minors, aggrieved neighbors, ideological actors, opportunists, major patron, second major, target AI, and neutrals at `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_4_ai_assets_achievements.md:11-18`. The current code mostly selects random eligible members or majors and applies broad `antagonize`, `prepare_for_war`, `building_target`, and direct target-AI progress. Evidence:

- Random core-member selection: `common/scripted_effects/011_secret_alliance_effects.txt:313-316`
- Generic member AI strategy: `common/scripted_effects/011_secret_alliance_effects.txt:1041-1048`
- Target AI equivalent pulse grants values directly: `common/scripted_effects/011_secret_alliance_effects.txt:1053-1068`
- Second major selection is any broad candidate, not conditioned on exposure, preparedness, faction backing, split members, or target isolation: `common/scripted_effects/011_secret_alliance_effects.txt:1357-1369`

The decision/mission audit handoff already records the same unresolved AI-equivalent gap.

### High: Achievement tracking exists but does not prove the specified mastery conditions

Requirement 6 is partial, not complete.

The eight achievements are registered at `common/achievements/chaos_redux_achievements.txt:1845-1923`, but several flags are set from broad route state rather than the exact spec predicates and disqualifiers:

- `sa_prepared_for_every_border` requires all exposed member borders covered by supplied divisions and disqualification on any failed border mission in `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_4_ai_assets_achievements.md:126`. The code only checks `secret_alliance_prepared_border_eligible`, known neighbor count >= 1, and preparedness threshold at `common/scripted_effects/011_secret_alliance_effects.txt:1795-1809`.
- `sa_ten_signatures` requires defeat/dissolve/split after a pact reaches at least ten members at spec line 128. The code sets eligibility when count reaches ten at `common/scripted_effects/011_secret_alliance_effects.txt:498-517`, then awards from the eligibility flag at `1811-1813` without rechecking route completion quality.
- `sa_no_factory_lost` requires completing the chain after Evolution II without successful major industrial sabotage at spec line 130. The code awards when stage is at least major patron and factory loss is zero at `common/scripted_effects/011_secret_alliance_effects.txt:1783-1793`, which does not itself prove chain completion.
- The spec requires disqualifier flags to be tracked when they happen at line 132. Current tracking is mixed and does not cover all stated disqualifiers with explicit flags.

### High: Required ideas are missing as gameplay spirits

Requirement 6 is incomplete for ideas.

The spec requires `Prepared Security Network`, `Compromised Ministries`, and `Exposed Pact Government` with roles and lifecycle at `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_3_counter_pact_decisions.md:158-161`. The implemented idea file defines `secret_alliance_unexplained_friction`, `secret_alliance_counter_pact_bureau`, `secret_alliance_hidden_compact_discipline`, `secret_alliance_patron_shield`, `secret_alliance_revealed_compact`, and `secret_alliance_public_war_command` at `common/ideas/011_secret_alliance_ideas.txt:10-78`.

Asset sprites for prepared/exposed idea concepts exist in `interface/011_secret_alliance.gfx:49-57`, but the corresponding gameplay ideas are not implemented.

### Medium: Second major and final crisis behavior are too broad

Requirement 5 is partial.

Evolution III does unlock public confrontation, war options, possible second major, and a final crisis window, but not with the spec's conditional depth. The spec says a second major should be less likely or refuse after exposure/split/faction backing and more likely when the target ignored investigations or is isolated at `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_2_evolutions_and_reveal.md:133-141`. Current `secret_alliance_force_public_crisis` always calls second-major selection at `common/scripted_effects/011_secret_alliance_effects.txt:1343-1353`, and selection chooses any broad candidate at `1357-1369`.

Final crisis lifecycle is also duplicated: `secret_alliance_force_public_crisis` schedules hidden event `chaosx.nr11.60` at `common/scripted_effects/011_secret_alliance_effects.txt:1353`, while `secret_alliance_final_crisis_mission` runs a visible mission with the same timeout at `common/decisions/011_secret_alliance_decisions.txt:753-787`.

### Medium: Public reveal is one-size-fits-all and always declares war

Requirement 5 is weakly evidenced for non-war reveal types.

The war-trigger reveal must immediately join valid core members against the target, and that path is implemented. However, public-crisis and preemptive-strike reveal helpers also call the same `secret_alliance_reveal_compact` helper at `common/scripted_effects/011_secret_alliance_effects.txt:1525-1538`, and that helper declares war for every valid core member at `1571-1577` plus major patron and second major at `1591-1614`.

The spec distinguishes war-trigger reveal from pact public reveal, which may be war countdown, ultimatum, or immediate war only if readiness is extreme at `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_2_evolutions_and_reveal.md:155-165`. The implementation has public crisis timing, but once reveal fires it always becomes war.

### Medium: Scripted GUI assets are produced but no Event 011 scripted GUI uses them

Requirement 6 is partial for GUI/assets.

The spec allows a decision-localisation fallback if the custom board is not implemented at `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_3_counter_pact_decisions.md:26`. That fallback is present in `localisation/english/011_secret_alliance_l_english.yml:75`.

However, board, suspect-card, meter, and animated assets are produced and registered at `interface/011_secret_alliance.gfx:59-102`, but no Event 011 scripted GUI exists under `common/scripted_guis/` or the interface files. The asset manifest also discloses a placement simplification for `secret_alliance_evidence_meter_highlight` at `docs/assets/011_secret_alliance/manifest.md:95`.

### Medium: Documentation overstates implemented decision/mission behavior

Requirement 6 is incomplete for docs.

`docs/events/011_secret_alliance.md:52` says timed missions are used for rail protection, officer protection, factory repairs, allied observers, border searches, crossing closures, patrols, consultations, and the crisis countdown. Current implementation has only three actual missions at `common/decisions/011_secret_alliance_decisions.txt:685-789`; most named items are instant decisions with cooldowns in `common/decisions/011_secret_alliance_decisions.txt:116-250` and `392-595`.

### Low: Completion validation is still static and marked as needing testing

The spreadsheet row has status `Needs Testing`, and subagent handoffs repeatedly state no in-game validation was run. This is not a boilerplate syntax issue; it affects confidence in event-chain behavior, reveal timing, final crisis ownership, achievement predicates, and AI pacing.

## Accepted Plans And Handoff Disposition

No unresolved improvement-loop addendum exists under `docs/plans/011_secret_alliance_plans/`. Current handoffs are:

- `2026-06-30_event011_generated_event_art_handoff.md`: static report/news/UI art completed; no animated assets in that handoff because scope was static.
- `2026-06-30_icon_artist_asset_package.md`: icon, achievement, and animated sprite package completed; disclosed simplification that `secret_alliance_evidence_meter_highlight` is a compact marker due missing final meter geometry.
- `2026-06-30_event011_spreadsheet_handoff.md`: spreadsheet row updated; current workbook row still says `Needs Testing`.
- `2026-07-01_event011_scripted_runtime_handoff.md`: runtime patch applied; residual risks remain for array mutation during cleanup, public coalition creation when members are faction-locked, and delayed paper-collapse cleanup.
- `2026-07-01_event011_decision_mission_audit_handoff.md`: decision/localisation patch applied; unresolved high/medium gaps remain for missions as instant decisions, final crisis duplicate lifecycle, broad second-major selection, abstract border readiness, generic AI equivalents, and non-target-specific diplomacy.
- `2026-07-01_event011_localisation_audit_handoff.md`: localisation concealment and missing-key issues patched; no blocking localisation issue remains from that pass. It leaves event-log/detail hidden-compact wording as an intentional catalog/detail decision.

## Meaningful Validation Performed

Static audit checks only:

- Compared Event 011 spec files and matrices against current implementation files.
- Inspected current event script, effects, triggers, constants, decisions, ideas, achievements, on-actions, localisation, interface sprites, docs, asset manifests, plan handoffs, and spreadsheet workbook row.
- Confirmed the workbook `Events` row 12 for event id 11/011 is present and currently marked `Needs Testing`.
- Confirmed no Event 011 scripted GUI is present by searching `common/scripted_guis`, `common/scripted_gui`, and `interface`.

Missing validation affecting confidence:

- No in-game chain validation is evidenced for hidden formation, reveal timing, public faction edge cases, final crisis double owner behavior, or achievement unlock/disqualifier routes.
- No AI scenario validation is evidenced for target AI choices, pact recruitment, second major behavior, or suicidal preemptive-war avoidance.
- No mission route validation is evidenced because the main spec missions are not implemented as concrete map/unit/supply missions.

## Asset And Documentation Gaps

- Asset package is mostly complete and well documented, including source, processed, DDS, contact sheets, and `.gfx` handoff.
- One disclosed asset simplification remains: evidence-meter highlight geometry.
- Scripted GUI board is not implemented; related board/meter/card assets are unused by Event 011 gameplay UI.
- Documentation exists but overstates mission implementation and achievement fidelity.
- Spreadsheet alignment exists but status remains `Needs Testing`.

## Remaining Blockers

- Convert security/border/capital/port items that the spec maps as timed missions into real missions with named regions, supplied divisions, supply/port/rail conditions, failure outcomes, and active mission caps.
- Add route-aware AI for member recruitment, target response, patron behavior, second major selection, neutral courting, and preemptive-war avoidance.
- Implement missing staged ideas or explicitly reject/promote a spec change explaining their replacement.
- Rework achievement tracking to match exact unlock conditions and disqualifiers.
- Choose one final-crisis lifecycle owner.
- Resolve public-faction edge behavior or document coalition fallback explicitly.
- Update docs and spreadsheet after implementation facts change; remove stale timed-mission claims.

## Recommended Next Actions

1. Implement the unresolved findings from `2026-07-01_event011_decision_mission_audit_handoff.md` before claiming completion.
2. Add or reject the missing idea spirits with a documented reason.
3. Rework achievement predicates and disqualifier flags against the spec table.
4. Add targeted/static validation notes for at least baseline fire, Evolution II decision opening, war-trigger reveal, public crisis timeout, paper collapse, and two achievement paths.
5. Update `docs/events/011_secret_alliance.md` and the spreadsheet row after the implementation matches reality.

## Improvement Loop Recommendation

Use `chaosx_improvement_loop_planner` if the parent wants Event 011 to reach the intended depth rather than only patching obvious defects. There is no unresolved planner addendum for Event 011, and the current implementation technically has the core event loop but falls short on mission design, AI role behavior, second-major consequences, achievement mastery routes, and post-reveal depth.
