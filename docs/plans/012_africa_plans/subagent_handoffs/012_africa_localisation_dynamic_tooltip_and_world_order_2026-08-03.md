# Event 012 localisation dynamic-tooltip audit — 2026-08-03

## Scope

This bounded pass audited the current Event 012 English localisation surface at shared-worktree HEAD `2a04c10a2e47476ae5b1510521e81cdc8c23cfaf`.

The audit covered 18 Event 012 English localisation files, four Event 012 scripted-localisation files, six external continent package surfaces, the 16 priority-member package names, terminal/world-order text, and action contracts 85–92.

No gameplay, portrait, GFX, or scripted-localisation source was changed by this pass.

## Changed files and keys

- `localisation/english/012_africa_world_sponsorship_l_english.yml` now resolves all 12 sponsorship-duration displays through `africa_world_order.sponsorship_obligation_days`, all five offer/counterterm costs through `africa_world_sponsorship_mode` constants, and the material delivery quantities through `africa_world_order` constants.
- `localisation/english/012_african_union_l_english.yml` now resolves natural-disaster caller reserve, cooldown, and backfire values through constants, replaces raw unmapped host and nature labels with player-facing wording, and rewrites action 85–92 descriptions/results to remove implementation terms and describe the actual full, partial, and failure outcomes.
- `localisation/english/012_africa_world_order_l_english.yml` now uses `africa_world_order.required_package_count` instead of repeating a static six-package gate in three player-facing strings.
- `localisation/english/012_africa_priority_member_focus_l_english.yml` now presents the scripted-localisation fallback as `Priority package awaiting recognition` rather than `Unmapped priority package`.
- `localisation/english/012_africa_priority_member_l_english.yml` now presents the unresolved requalification fallback as an unresolved compact-settlement question rather than an unrecorded implementation state.

## Before and after display behavior

- Sponsorship duration and costs previously repeated literal numbers and now track the live script constants, so future tuning cannot leave stale player-facing values behind.
- Natural-disaster reserve and recovery text previously repeated literal costs and omitted the actual cooldown/backfire values; it now shows the configured reserve, cooldown, and backfire chance.
- World-order gate text previously said six packages in three places and now shows the configured required package count.
- Action 85–92 result text previously exposed `unique unifier package`, `puppet continent`, `super-event fires`, `not applicable`, and `world victory`; it now describes settlements, armistices, ceremonies, and continuing disasters in-world.

## Audit evidence

- Missing localisation key list: none found in the 18 Event 012 English files.
- Duplicate localisation key list: none found in the 18 Event 012 English files.
- Scripted-localisation issue list: four Event 012 scripted-localisation files contain 1,214 literal `localization_key` references and every reference resolves to an English key; repeated branch references are intentional selection branches, not duplicate localisation definitions.
- Dynamic text opportunities completed: sponsorship durations and costs, material delivery quantities, natural-disaster reserve/cooldown/backfire values, and the world-order required-package count.
- Action matrix coverage: action 85, 86, 87, 88, 89, 90, 91, and 92 each retain name, selection, description, and full/partial/failure result keys.
- Public package-name coverage: all 16 direct names remain present through `GetAfricaPriorityPackageName`, including Asante, Oyo, Sokoto, Kanem-Bornu, Manden, Kongo, Buganda, Aksum, Harar, Kilwa, Nubia, Luba, Lunda, Great Zimbabwe, Merina, and Zulu.
- Raw tag check: no `GetTag`, `GetTagDef`, or `.GetTag` token remains in the Event 012 English localisation files.
- Encoding check: all 18 Event 012 English localisation files begin with UTF-8 BOM bytes `EF BB BF`.
- Afaan Oromoo preservation check: `qaama saalaa koo xuuxaa` and `haadha kee waliin wal qunnamtii saalaa raawwadhe` each occur exactly once in the runtime character localisation, and no additional source-language name was introduced.

## Cross-surface mismatch notes

- Older localisation audit documents still say there are 17 Event 012 English files and that the two Afaan Oromoo strings are absent; the runtime now contains 18 English files and preserves those two exact strings, so those documents are stale and should be reconciled by the documentation owner.
- `africa_world_order_terminal_presentation_not_ready_tt` in `localisation/english/012_africa_world_order_l_english.yml` remains an apparently unreferenced readiness string; the owner should either wire it to a real status surface or retire it without changing terminal gameplay.
- Action 85, 87, and 92 descriptions still use broad threshold phrases such as `global chaos high enough`, `world chaos threshold`, and `special countermeasures`; these are acceptable public summaries but could expose configured threshold values through dynamic localisation if the owning decision pass wants that clarity.
- The country-package handoff reports male metadata for all 16 sovereign leaders, but Aksum, Nubia, and Merina runtime DDS portraits remain visibly female-presenting; portrait replacement is an asset-owner blocker outside this localisation pass.
- The current untracked `012_africa_super_events_l_english.yml` and its scripted-localisation companion are BOM-clean and fully covered by the reference scan, but their addition is not represented in older audit counts.

## Recommended follow-up

- Update stale Event 012 localisation audit documents to 18 English files and the current two-string preservation state.
- Decide whether to wire or retire `africa_world_order_terminal_presentation_not_ready_tt`.
- If the decision owner wants explicit threshold transparency, add dynamic constant displays to action 85, 87, and 92 through a connected tooltip review rather than hardcoding new numbers.
- Replace the three female-presenting grounded leader DDS assets before claiming final male portrait parity.

## Validation and skipped checks

The task-specific scans above were run after the final namespace correction, including key extraction, duplicate-key detection, scripted-localisation reference resolution, action 85–92 matrix coverage, raw-tag search, BOM checks, exact Afaan Oromoo occurrence checks, and constant-name verification against `common/script_constants/012_africa_world_order_constants.txt` and `common/script_constants/012_africa_action_constants.txt`.

Live Hearts of Iron IV launch, save loading, and in-game visual validation were skipped because repository instructions assign those checks to the user and prohibit agents from launching the game.

No fallback mechanic or gameplay simplification was introduced by this pass.
