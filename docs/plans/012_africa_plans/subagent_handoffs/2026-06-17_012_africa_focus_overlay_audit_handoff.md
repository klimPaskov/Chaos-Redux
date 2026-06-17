# Event 012 Africa Focus Overlay Audit Handoff

Date: 2026-06-17

Scope audited:
- `common/national_focus/012_africa_focus.txt`
- `common/national_focus/012_africa_authority_focus.txt`
- `localisation/english/012_african_union_l_english.yml`
- Direct focus-decision hook checks in `common/decisions/012_africa_decisions.txt`, `common/scripted_triggers/012_africa_triggers.txt`, and `common/scripted_effects/012_africa_effects.txt`

References consulted before editing:
- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline Paradox wiki pages for national focuses, data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding.
- Vanilla HOI4 documentation and focus examples under `/home/klim/projects/Hearts of Iron IV/`.

## High-Priority Fix Applied

| Priority | File and identifiers | Finding | Action |
| --- | --- | --- | --- |
| High | `common/national_focus/012_africa_focus.txt`: `AFR_respect_the_old_seats`, `AFR_documents_before_consent`, `AFR_seal_them_under_one_archive` | The Archive policy fork was intended as a three-way policy split. `AFR_respect_the_old_seats` and `AFR_documents_before_consent` were each exclusive with `AFR_seal_them_under_one_archive`, but not with each other, allowing two policy settlements to stack. | Added the missing pairwise mutual exclusions so all three choices are mutually exclusive. |

## Changed Files

| File | Change |
| --- | --- |
| `common/national_focus/012_africa_focus.txt` | Added missing mutual exclusions between `AFR_respect_the_old_seats` and `AFR_documents_before_consent`. |
| `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_focus_overlay_audit_handoff.md` | This handoff. |

Changed focus ids:
- `AFR_respect_the_old_seats`
- `AFR_documents_before_consent`

Route behavior before:
- `AFR_respect_the_old_seats` excluded only `AFR_seal_them_under_one_archive`.
- `AFR_documents_before_consent` excluded only `AFR_seal_them_under_one_archive`.
- A country could take both the Respect and Documents policy outcomes.

Route behavior after:
- `AFR_respect_the_old_seats`, `AFR_documents_before_consent`, and `AFR_seal_them_under_one_archive` are pairwise exclusive.
- The Archive settlement fork now matches the three-way policy split described by the focus architecture.

Localisation keys changed:
- None.

Icon ids changed:
- None.

## Route Coverage Table

| Goal route/surface | Implemented focus ids or surfaces | Audit status |
| --- | --- | --- |
| Opening trunk and continental claim | `AFR_the_charter_mandate`, `AFR_continental_congress`, `AFR_liberation_war_office`, `AFR_authority_atlas` | Present. Trunk provides political, military, and Authority Atlas entry points. |
| Political identity routes | `AFR_federal_charter_path`, `AFR_sovereign_seats_path`, `AFR_peoples_liberation_front`, `AFR_general_staff_above_parliament`, `AFR_crown_congress` | Present with mutual exclusions among the five visible central identity paths. |
| High-chaos hidden route | `AFR_high_chaos_door`, `AFR_forest_parliament`, `AFR_archive_bestiary_clause`, `AFR_treaty_of_teeth_and_roots`, `AFR_world_root_mandate` | Present, but behaves as an overlay/late hidden path rather than a mutually exclusive political identity route. This may be intended, but it remains a design risk against the goal wording. |
| Industry and logistics | `AFR_industrial_convergence`, `AFR_lake_and_rail_agreements`, `AFR_mandate_foundries`, regional Archive infrastructure focuses | Present, but much of the reward language is broad state construction and variable movement rather than deeply regional industrial programs. |
| Military branch | `AFR_charter_general_staff`, `AFR_liberation_columns`, route-linked military focuses under PLF and General Staff | Present. The military surface is meaningful but not as large as the political/Archive overlay. |
| Diplomacy and Charter League | Charter/RSA/diaspora focuses and decision hooks from focus flags | Present, with decision integration for several flags. Needs broader route-aware AI in support focuses. |
| Authority Atlas and Archive of Old Seats | `AFR_archive_of_old_seats`, `AFR_authority_register`, `AFR_dossier_selection_office`, `AFR_integration_temperature_board`, `AFR_old_seat_mission_calendar`, regional dossier lanes | Present and large. `AFR_integration_temperature_board` currently sets a flag with no direct hook found in decisions/triggers/effects. |
| Expansion and integration | `AFR_dossier_kush_to_kilwa`, `AFR_dossier_manden_to_benin`, `AFR_dossier_kongo_to_merina`, `AFR_scramble_reverse_claims`, `AFR_integrated_regions`, `AFR_autonomous_regions`, `AFR_continental_register` | Present. Some conquest/integration outcomes are represented abstractly through variables, flags, and decisions rather than route-specific focus consequences. |
| Regional authority companion overlay | `common/national_focus/012_africa_authority_focus.txt` regional and Bestiary companion trees | Present with branch visibility gates and full AI blocks on all companion focuses. |
| Post-unification/world order | `AFR_continent_sponsor_office`, `AFR_africa_is_one`, `AFR_continental_export_office`, `AFR_the_world_is_one` chain | Present. `AFR_africa_is_one` is gated through high-chaos/Bestiary route requirements, which may over-constrain non-high-chaos unification if that path is intended. |

## Missing or Simplified Content

| File and identifiers | Gap |
| --- | --- |
| `common/national_focus/012_africa_focus.txt`: `AFR_high_chaos_door` and downstream high-chaos focuses | High-chaos is a hidden overlay gated by Archive/Bestiary state, not a fully exclusive top-level political route. I did not patch this because it is route design, not a narrow local fix. |
| `common/national_focus/012_africa_focus.txt`: `AFR_africa_is_one`, `AFR_world_root_mandate`, `AFR_forest_parliament`, `AFR_archive_bestiary_clause` | Continental unification capstone requires high-chaos/Bestiary progression. If a normal political-route Africa unification endpoint is expected, this remains a route design blocker. |
| `common/national_focus/012_africa_focus.txt`: regional Archive infrastructure and dossier focuses | Rewards are often variable deltas and broad `random_owned_controlled_state` / `every_owned_state` effects. They are functional, but several branches still feel mechanically similar. |
| `common/national_focus/012_africa_focus.txt`: `AFR_integration_temperature_board` | Focus sets `africa_integration_temperature_board_open`, but no direct reference to that flag was found in the checked Event 012 decisions, triggers, or effects. This may be a dormant UI/decision hook. |
| `common/national_focus/012_africa_focus.txt`: failure states generally | Some Archive/World order systems have mission and gate state hooks, but the focus tree itself has limited visible failed-path routing. Broader failure-state content would be a design expansion. |

## Icon Coverage Table

| Surface | Result |
| --- | --- |
| Main Event 012 focus tree icons | All checked focus icon ids resolve against local or vanilla interface definitions. |
| Companion authority focus tree icons | All checked focus icon ids resolve against local or vanilla interface definitions. |
| Missing `icon =` fields | None found. |
| Repeated icon concern | Reuse exists on generic support focuses, but no broken icon reference was found. I did not change icon choices. |

## Localisation and Reward Mismatch List

| File and identifiers | Result |
| --- | --- |
| `localisation/english/012_african_union_l_english.yml`; all 150 Event 012 focus ids and `_desc` keys | No missing focus localisation keys found. |
| `AFR_respect_the_old_seats`, `AFR_documents_before_consent`, `AFR_seal_them_under_one_archive` | Localisation already describes distinct policy outcomes; no text change needed for the mutual-exclusion fix. |
| `AFR_integration_temperature_board` | Description says it tracks integration tension, but the focus flag currently has no direct checked hook in decisions/triggers/effects. Reward-to-system connection is uncertain. |
| Regional infrastructure/dossier focuses | Text is more specific than several rewards, which are often broad state construction or variable changes. This is a reward-depth simplification rather than a broken localisation key. |

## AI Behavior Gaps

| File and identifiers | Finding |
| --- | --- |
| `common/national_focus/012_africa_focus.txt` | 108 main-tree focus ids checked; 66 `ai_will_do` blocks found. Missing `ai_will_do` blocks are concentrated in industry/Archive regional support lanes and several convergence focuses. |
| `common/national_focus/012_africa_focus.txt`: `AFR_sovereign_seats_path`, `AFR_high_chaos_door`, `AFR_integrated_regions`, `AFR_autonomous_regions`, `AFR_continent_sponsor_office` | These notable route/convergence focuses have no direct `ai_will_do` block. Some may rely on default AI behavior or availability gates, but route-aware weighting is incomplete. |
| `common/national_focus/012_africa_authority_focus.txt` | 42 companion focus ids checked; 42 `ai_will_do` blocks found. Companion route AI is complete at the focus-block level. |

## Focus-Decision Integration Notes

| Focus flag or route hook | Direct hook result |
| --- | --- |
| `africa_dossier_selection_office_open` | Found in Event 012 decisions, triggers, and effects. |
| `africa_old_seat_mission_calendar_open` | Found in Event 012 decisions. |
| `africa_world_root_mandate_open` | Found in Event 012 decisions, triggers, and effects. |
| `africa_continent_sponsor_office_open` | Found in Event 012 decisions, triggers, and effects. |
| `africa_integration_temperature_board_open` | No direct hook found in the checked Event 012 decisions, triggers, or effects. |
| `africa_the_world_is_one_complete` | No direct hook found under that exact flag name; the world-order chain appears to use other global gate flags and scripted effects. |

## Validation

Meaningful task-specific checks run:
- Parsed `common/national_focus/012_africa_focus.txt` and `common/national_focus/012_africa_authority_focus.txt`: 150 focus ids, 0 duplicate ids.
- Checked Event 012 focus blocks: 0 missing `search_filters`, 0 missing `icon =` fields.
- Checked focus icon ids against local and vanilla interface definitions: 0 missing icon definitions.
- Checked focus ids and `_desc` keys against `localisation/english/012_african_union_l_english.yml`: 0 missing focus localisation keys.
- Checked Archive policy fork topology after patch: all three pairs are mutually exclusive.
- Checked direct focus-decision hooks for representative Event 012 focus flags; noted the `africa_integration_temperature_board_open` gap above.
- Ran `git diff --check -- common/national_focus/012_africa_focus.txt`; no whitespace errors reported.

Skipped validation:
- No full game launch or live HOI4 parse was run in this subagent pass.
- No decision system rewrite or deep mission balance validation was run because the requested write scope excludes decision rewrites.
- No country history, assets, achievements, spreadsheets, super-event, or audio validation was run because those surfaces are outside scope.

## Remaining Route Risks

| Risk | Recommended owner/action |
| --- | --- |
| High-chaos route may not satisfy the goal if it is expected to be a primary route family rather than a hidden overlay. | Main agent or improvement planner should decide whether hidden overlay behavior is intentional. |
| Normal political routes may lack a non-high-chaos `Africa Is One` endpoint due to `AFR_africa_is_one` requiring `AFR_world_root_mandate`. | Main agent should compare against accepted Event 012 design before changing capstone gates. |
| `AFR_integration_temperature_board` may be a dead focus-decision unlock hook. | Decision/mission audit should confirm whether this flag is intentionally future-facing or should gate an existing decision. |
| Main-tree AI is incomplete at the focus-block level for several support and convergence focuses. | Safe follow-up could add narrow `ai_will_do` guards, but broader route-aware AI should be planned deliberately. |
| Several regional rewards remain mechanically similar. | Improvement-loop plan is appropriate if deeper regional reward design is desired. |

## Simplifications and Blockers

No fallback implementation was used.

This pass did not redesign route families, add new focuses, or rewrite decision systems. The only gameplay patch was the narrow three-way Archive fork mutual-exclusion fix. Broader gaps are documented above as remaining route risks because changing them would exceed the requested safe patch scope.
