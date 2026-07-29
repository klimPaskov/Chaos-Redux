# Event 12 Africa localisation deep audit

Date: 2026-07-30

Scope: Read-only localisation and player-facing text audit for Event 12 Africa across source scripts, English localisation, scripted localisation, Charter GUI, achievements, shared event-log surfaces, and the related specification and handoff documents.

Status: The audit is complete. No gameplay files or localisation files were changed for this handoff, and no commit was created.

## Source-of-truth and method

The audit followed AGENTS.md, the Event, Decision, Focus, Localisation, Data Structures, Triggers, Effects, Modifiers, Scopes, On Actions, AI Modding, Interface Modding, and Scripted GUI Modding pages in the offline Paradox wiki snapshot, the applicable Chaos Redux skills, and the matching vanilla documentation files.

The checked runtime surfaces were `events/012_*.txt`, `common/decisions/012_*.txt`, `common/national_focus/012_*.txt`, `common/ideas/012_*.txt`, `common/achievements/chaos_redux_achievements.txt`, `common/scripted_localisation/012_*.txt`, `common/scripted_guis/012_*.txt`, `interface/012_africa_charter.gui`, and the ten Event 12 English localisation files.

## Coverage evidence

- The ten Event 12 English localisation files contain 3,299 unique keys.
- The whole English localisation tree contains 46,544 keys with zero duplicate keys.
- The source scan found 1,247 literal Event 12 localisation assignments and all 1,247 resolve.
- Filtered unresolved Event 12-shaped references: 0.
- The three Event 12 scripted-localisation files contain 35 unique `defined_text` definitions and 1,138 resolved `localization_key` branches.
- Old `localisation_key` spellings remaining in those files: 0.
- GUI localisation attributes: 67 occurrences and 59 unique keys, all resolving.
- Focus IDs checked: 402, with zero missing generated name or description keys.
- Decision IDs checked: 213, with zero missing generated name or description keys.
- Decision category IDs checked: 17, with zero missing generated name or description keys.
- Event 12 idea IDs checked: 80, with zero missing generated name or description keys.
- Event 12 achievement IDs checked: 44, with zero missing name, description, or tooltip keys.

## Missing key list

There are no confirmed missing Event 12 localisation keys in the scanned runtime surfaces.

The exact Afaan Oromoo strings `qaama saalaa koo xuuxaa` and `haadha kee waliin wal qunnamtii saalaa raawwadhe` are absent from localisation and identifiers, which is correct while native verification and approved flavour placement remain unresolved.

## Duplicate key list

There are no duplicate keys inside the ten Event 12 English files and no collisions with the complete English localisation tree.

## Scripted localisation issue list

No unresolved scripted-localisation branches were found.

All 1,138 branches use the current `localization_key` spelling, and all literal branch keys resolve.

The 35 custom definitions are unique and all custom methods used by Event 12 English values resolve to a definition.

Three force-name methods are used by scripted effects rather than player-facing English localisation, so they are not orphaned text methods.

## Candidate orphan or unreferenced keys

Runtime missing-reference count is zero, but fifteen source-unreferenced candidates require owner review because some may be optional blocked or tooltip surfaces.

- `localisation/english/012_africa_rsa_l_english.yml`: `africa_rsa_relief_cost_blocked`, `africa_rsa_relief_cost_tooltip`, `africa_rsa_regional_request_cost_blocked`, `africa_rsa_regional_request_cost_tooltip`, `africa_rsa_citizenship_cost_blocked`, `africa_rsa_citizenship_cost_tooltip`, `africa_rsa_sovereignty_guarantee_cost_blocked`, `africa_rsa_sovereignty_guarantee_cost_tooltip`, `africa_rsa_exile_recovery_cost_blocked`, and `africa_rsa_exile_recovery_cost_tooltip`.
- `localisation/english/012_african_union_l_english.yml`: `africa_selected_action_dynamic_cost_blocked` and `africa_selected_action_dynamic_cost_tooltip`.
- `localisation/english/012_africa_rsa_l_english.yml`: `africa_rsa_allied_branch_can_start_tt` and `africa_rsa_start_allied_civil_war_tt`.
- `localisation/english/012_africa_world_order_l_english.yml`: `africa_world_order_terminal_presentation_not_ready_tt`.

The twelve cost variants may be intended for optional custom cost UI, so they should be wired or explicitly marked as intentionally unused before deletion.

The two RSA branch tooltips should be wired to their start controls if those controls still exist, or removed after owner confirmation.

The terminal presentation readiness key is both unreferenced and implementation-facing, so it should be wired to the terminal gate or retired after the world-order owner confirms the intended surface.

## Dynamic text opportunities

- `localisation/english/012_africa_charter_gui_l_english.yml:9-13` exposes each selected member's raw `GetTag` beside `GetName`; show the direct public name only.
- Existing dynamic values such as the selected action cost, selected member detail, actor names, route methods, relationship methods, and state names should be retained.
- Rewrite implementation-oriented action and mission descriptions around the visible actor, action, target, commitment, and result while preserving their dynamic tokens.
- Mission timers are already presented by the mission UI and do not need a new hard-coded timer sentence.

## Player-facing wording blockers

The following keys expose implementation history, internal state-machine terms, technical identifiers, or debug language and should be rewritten without changing mechanics.

| File and key | Current issue | Recommended direction |
| --- | --- | --- |
| `localisation/english/012_african_union_l_english.yml:88`, `africa_execute_selected_country_action_desc` | Says “recompute,” “verify every gate,” “spend once,” and “generation-safe action record.” | Describe the current action, cost, commitment, and visible outcome in-world. |
| `localisation/english/012_african_union_l_english.yml:90`, `africa_execute_selected_host_action_desc` | Uses the same implementation contract wording. | Describe the host action and its resulting commitment or settlement. |
| `localisation/english/012_african_union_l_english.yml:95`, `mission_africa_action_short_desc` | Says “quoted action generation,” “invalidation,” and “cleanup contract.” | Refer to the named actor's current action and the mission's success or cancellation result. |
| `localisation/english/012_african_union_l_english.yml:97`, `mission_africa_action_medium_desc` | Same action-generation and cleanup terminology. | Use the visible action and target. |
| `localisation/english/012_african_union_l_english.yml:99`, `mission_africa_action_long_desc` | Same action-generation and cleanup terminology. | Use the visible action and target. |
| `localisation/english/012_african_union_l_english.yml:101`, `mission_africa_action_epic_desc` | Same action-generation and cleanup terminology. | Use the visible action and target. |
| `localisation/english/012_african_union_l_english.yml:447`, `africa_action_result_declare_the_world_is_one_failure` | Says “invalid state” and “fallback.” | Say that the declaration cannot proceed until all required conditions are satisfied. |
| `localisation/english/012_african_union_l_english.yml:755`, `africa_select_declare_the_world_is_one_desc` | Repeats “invalid state,” “fallback,” and raw `world_end`. | Refer to the final world settlement in player-facing terms. |
| `localisation/english/012_african_union_l_english.yml:767`, `africa_select_conduct_first_continental_election_desc` | Exposes raw `world_end`. | Refer to whether the final world settlement has already been declared. |
| `localisation/english/012_african_union_l_english.yml:785`, `africa_select_hold_postwar_constitutional_review_desc` | Exposes raw `world_end`. | Use a player-facing final-settlement phrase. |
| `localisation/english/012_africa_priority_member_focus_l_english.yml:18`, `africa_priority_negotiate_league_role_desc` | Says “Charter state machine.” | Say “Charter relationship rules” or equivalent. |
| `localisation/english/012_africa_priority_member_l_english.yml:8-9`, `africa_resolve_priority_member_requalification_desc` and `_tt` | Expose “Action 102 attempt” and “Action 102 result.” | Say “full promotion action” and “full promotion result.” |
| `localisation/english/012_africa_priority_member_l_english.yml:250`, `africa_priority_member.1220.c.tt` | Says “Charter state machine.” | Say “Charter relationship rules.” |
| `localisation/english/012_africa_achievements_l_english.yml:2`, `africa_achievement_eligible_tooltip` | Says “normal Event 12 play” and “forced scenario launches.” | Say “Available through normal play” or equivalent. |
| `localisation/english/012_africa_achievements_l_english.yml:132`, `africa_war_between_worlds_tooltip` | Says “debug surrender.” | Describe the gameplay disqualifier without debug terminology. |
| `localisation/english/012_africa_world_order_l_english.yml:100`, `africa_world_order_terminal_presentation_not_ready_tt` | Exposes “unique audio ID” and “final scenario package” and is source-unreferenced. | Wire or retire it, then describe only the final title, quotation, image, and music readiness. |
| `localisation/english/012_african_union_l_english.yml:18`, `africa_charter_council_category_desc` | Contains one em dash. | Use a colon, comma, or separate sentence. |

The audit found no coercive forced-return language. Existing diaspora wording explicitly uses voluntary or anti-coercion phrasing, including the `africa_return_without_compulsion_*` and `africa_four_oceans_homeward_*` surfaces.

## Semicolon and punctuation review

The event writing style disallows semicolons and em dashes in player-facing sentences.

There is one em dash in `africa_charter_council_category_desc`.

There are 64 semicolon-bearing player-facing values, including one Charter GUI tooltip, three priority-member focus or package values, one candidate survey value, one requalification tooltip, and 59 values in `012_african_union_l_english.yml`.

The 53 `africa_host_leverage_*` values use semicolons as list-fragment separators and should be changed to commas or explicit line breaks without changing the listed leverage effects.

## Sovereign titles, councils, and cultural strings

The priority-member character file contains sixteen direct public royal office titles, including the Asantehene, Alaafin of Oyo, Sultan of Sokoto, Mai of Kanem-Bornu, Mansa of Manden, Manikongo, Kabaka of Buganda, Queen of Aksum, Emir of Harar, Sultan of Kilwa, Kandake of Nubia, Mulopwe of Luba, Mwaant Yaav of Lunda, King of Great Zimbabwe, Queen of Merina, and King of the Zulu.

The character source keeps constitutional councils separate from sovereigns, and the current localisation follows that separation.

“The King of the Zulu” sounds less idiomatic than the other public titles, but changing it would be a wording decision for the country-package owner rather than a safe mechanical fix.

The plain-background requirement for decorated sovereign portraits is an asset acceptance check and cannot be proven by localisation scanning.

The two exact Afaan Oromoo strings remain absent from all localisation and identifiers as required. They must not be added until native verification and an approved fictional flavour surface exist.

## Cross-surface mismatch notes

- `docs/plans/012_africa_plans/012_africa_priority_member_packages_handoff.md` still describes “16 registered 156x210 council portrait paths,” while the source and current package contract distinguish sixteen sovereign portraits from institutional council portraits. This is historical or superseded handoff wording, not a runtime localisation blocker.
- The same older handoff describes the sixteen sovereign portraits as unresolved even though the current package audit records them as installed. Mark that section historical or update it after the owning asset audit.
- `docs/specs/012_africa_specs/specs/012_africa_spec_part_9_priority_member_country_packages.md` agrees with current localisation by requiring direct public country names and one decorated sovereign portrait on a plain background.
- `docs/specs/012_africa_specs/specs/012_africa_spec_part_4_country_packages_formables.md` agrees that councils use institutional names and collective portraits rather than public country names, and it preserves the two exact Afaan Oromoo flavour strings as untranslated non-identifier text.

## Encoding concerns

All ten Event 12 English localisation files are UTF-8 with BOM.

The three Event 12 scripted-localisation `.txt` files are UTF-8 without BOM, matching the repository's existing scripted-localisation convention. They should not be converted during wording patches.

No `:0` localisation syntax was found.

## Recommended fix queue

1. Remove raw `GetTag` from `africa_charter_gui_member_slot_1` through `africa_charter_gui_member_slot_5` in `localisation/english/012_africa_charter_gui_l_english.yml`.
2. Rewrite the six action and mission descriptions in `012_african_union_l_english.yml` to describe current visible commitments and outcomes rather than generation, gates, invalidation, or cleanup contracts.
3. Replace fallback and invalid-state wording in `africa_action_result_declare_the_world_is_one_failure` and `africa_select_declare_the_world_is_one_desc`.
4. Replace raw `world_end` tokens in the three selection descriptions with final-settlement wording.
5. Replace “Charter state machine” and “Action 102” in the priority-member focus, package, and event option text.
6. Remove “forced scenario launches” and “debug surrender” from achievement text while preserving the actual eligibility conditions.
7. Wire or retire the fifteen candidate orphan keys after their owning GUI or decision surfaces are confirmed.
8. Replace the single em dash and all 64 semicolons with commas, colons, or line breaks that preserve the same player-facing lists and dynamic values.
9. Correct the historical council-portrait wording in `docs/plans/012_africa_plans/012_africa_priority_member_packages_handoff.md` after the owner confirms the package audit status.
10. Keep the direct public sovereign titles, plain-background portrait requirement, and the two untranslated Afaan Oromoo strings unchanged unless the country-package owner supplies a reviewed wording decision.

## Validation and handoff

The checks above were static key-resolution, duplicate-key, scripted-localisation branch, GUI localisation-reference, generated-key, source-reference, and encoding scans.

Live game validation was skipped because agents must not launch Hearts of Iron IV and the user owns in-game validation.

No localisation files, gameplay files, assets, or specs were changed by this audit.

No commit was created.

The next implementation tranche may use this handoff as the review checklist: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_localisation_deep_audit_2026-07-30.md`.
