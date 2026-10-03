# Participant scope skill rule correction and owned patch

Disposition: implemented for the bounded reusable skill correction; parent review and isolated commit remain parent-owned.
Acceptance basis: the explicit assignment authorizes replacing only the existing four-line participant-scope paragraph, this review handoff, and the requested temporary owned patch.
No gameplay completion or runtime behavior is claimed.

## Owned files and behavior

- `.agents/skills/chaos-redux-events/SKILL.md`, lines 510-513 at edit time: replaced exactly four existing physical lines in `Country activation and ROOT`.
- `docs/plans/012_africa_plans/subagent_handoffs/012_participant_scope_skill_rule_review_2026-10-03.md`: this new handoff.
- `C:\Users\klimp\AppData\Local\Temp\gods_participant_scope_skill_owned_20261003.patch`: isolated owned skill patch, outside the repository.

The previous paragraph grouped country events and targeted decisions under an assumed initiating-owner ROOT.
The correction retains the original country-event recipient through participant-country and state iterators, explicitly verifies the actual targeted-decision ROOT/FROM callback contract, captures the intended current participant before entering state scope, and uses that participant target for helper country inputs and participant receipts.
The standard targeted-decision context has the deciding country as ROOT and the target country or state as FROM.
ROOT remains valid wherever the documented callback or helper contract requires it.
The skill contains no event-specific identifiers, names, implementation history, or private tokens from the source lesson.

The following frozen transaction-frame guidance, existing `$PARAMETER$` prohibition, parchment guidance, probability guidance, and every other byte outside the four-line replacement were preserved at write time.
No other skill, AGENTS.md, gameplay file, original participant-scope handoff, or routing definition was edited.
No new skill or AGENTS.md/subagent routing update is needed.

## Actual source lesson and authority

Installed documentation is the primary engine syntax authority; the offline wiki supplies parallel scope and target-lifetime rules.
Native source is a concrete structural precedent rather than a live engine test.
Repository source demonstrates the reusable capture-and-receipt pattern without establishing a full feature audit.
The paths below are exact local files; hashes are SHA-256 of the complete file bytes when read.

1. `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md`, lines 12-35 and 39-46, hash `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
   Installed authority explicitly distinguishes current country scope from FROM target country/state, identifies the acting-country precheck, and uses ROOT as owner/controller in state-target filtering.
2. `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md`, lines 260-269, hash `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`.
   Offline authority defines event ROOT as the country receiving the event, THIS as current scope, PREV by nesting, FROM by the native context, and event targets as stored scope pointers.
3. `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md`, lines 511-518 and 531-536, hash `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
   Offline authority states that the decision recipient is ROOT and the targeted country is FROM, and distinguishes target-root, target, visibility, and availability checks.
4. `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\AST.txt`, lines 114-149 and 712-771, hash `aad50da745f5a93c5f7470e06ed990a49a5416c81810849c8a2312600e81f4f2`.
   Native `AST_seize_local_leadership_in_state_major` checks the FROM state against ROOT ownership and enters FROM in its remove callback.
   Native `AST_supply_arms_to_nation` selects target countries and sends equipment to FROM in `complete_effect`, confirming the target contract in a concrete effect callback.
5. `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 6496-6503, hash `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
   Installed authority permits `save_event_target_as` in any scope.
6. `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, lines 263-266 and 303-305, hash `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
   Offline authority explains pointer identity and regular-target lifetime through the originating effect chain and events fired within it.
7. `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\012_africa_gods_effects.txt`, lines 116-154 and 2671-2700, hash `7def8a688e56dd54571cbca0356f3d5ad487d9bbf4a95e9f07be465b59bb26f8` at inspection.
   The owner tick iterates participant-country scopes.
   `gods_of_africa_apply_population_wave` captures the current participant at line 2679 before `random_owned_controlled_state` at line 2680, supplies that target to the shared exact-loss helper at line 2685, then writes participant flags and receipts through the same target at lines 2693-2696.
   This is independently read current source evidence for the reusable attribution lesson; it is not a claim that all call chains or engine accounting were validated.

## MCP reference evidence and limits

Connected schemas for `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` were discovered before use.
All requested reference routes returned successfully with workspace `mod_chaos_redux_ea3b2d67c2c0`; no local reference route gap remains for this correction.
Local direct reads supplied the exact Scopes section, additional Decision modding sections, native state-target precedent, event-target syntax/lifetime sections, and repository lesson.
The context bundle was discovery only; detailed coverage rests on the listed actual section reads.
No whole-context or whole-tree coverage is claimed.

- `reference_context`: surface `decision`, limit 4, question about targeted-decision ROOT/FROM and country-event iterators; returned installed decision documentation id `c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
- `reference_read`: that id and revision, startLine 12, maxLines 35; returned lines 12-46 with `nextLine = null`.
- `reference_search`: query `Targeted decisions`, sources `[wiki]`, limit 2; returned the targeted-decisions section and a state-targeted section, with `skipped = 0`.
- `reference_read`: targeted-decisions id `09d5949e5fe45735721cecc1a56ee07a277873591c4a5289b66d184e7658ce96`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, startLine 511, maxLines 8; returned lines 511-518 with `nextLine = null`.
- `source_lookup`: symbol `AST_supply_arms_to_nation`, kind `decision`, maxDefinitions 1, maxLines 65, includeReferences false; returned `game:common/decisions/AST.txt`, definition lines 712-784, inspected excerpt 712-776, nextLine 777, source revision `ebec921a860da56bb9a19b1887c83b0ba13324c0553b56b1de4a341980fda3de`, unshadowed/unoverridden, skippedSourceCount 0.
  The relevant target selection and complete-effect block are fully inside the returned excerpt; later AI modifiers and consumers were outside this bounded scope.
  The source-lookup revision is a service revision, distinct from the full AST file-byte hash above.

No MCP GUI, native tasks, HOI4 launch, or live game validation was used.
Reference reads and source inspection validate the skill wording, not native runtime behavior.

## Owned patch and preservation proof

Recorded HEAD at patch generation: `91dc29cfff8b5438eee5f3b0c1b12d353cd95e2e`.
HEAD skill-byte SHA-256: `b5e04deaaf0e716fcd8b166ec5c5113cf1ef2e5b1365c57cfb326556cce5cb05`.
Working-file SHA-256 before correction: `2fc50ca6b63cfd6242ae85bae3a6b60c838031770d55d4229bfebf1e4db13d0f`.
Working-file SHA-256 after correction: `e9e6ee4c875ffd6a92ee91885a8a4a40d35801e651228e9604e8a1e603b2789b`.
Untouched byte-prefix SHA-256: `d743bceec863b3678ea148576d458a1635d7cddbabe86f7e13d667c1aa811df0`.
Untouched byte-suffix SHA-256: `5ba0eb2669c5e86449608c094c96aab275e16db4fd96c7cae0f0b39a84ed0159`.
Patch SHA-256: `3d63963b5842a14ce3ac32a76778af9f98b38174c4fd9a98e1c34bfea8b145d3`.

The shared-tree edit replaces four lines and preserves their original line endings and every surrounding byte.
The owned HEAD patch adds only the corrected four-line paragraph and its separating blank line because the earlier uncommitted paragraph is absent from that HEAD.
It excludes all other owners' uncommitted changes and excludes this handoff.
Its single hunk is `@@ -505,6 +505,11 @@`; both old and new offsets/counts are explicit, and blank context lines retain their leading context space.
The following frozen-frame lines occur only as unchanged patch context.
The entire patch was manually reviewed, and an in-memory unified-hunk reconstruction matched the synthetic HEAD-plus-owned-paragraph result exactly.

Read-only `git rev-parse HEAD` and `git show <recorded-HEAD>:<skill-path>` were used solely to produce the explicitly requested HEAD-relative patch.
No Git mutation, index access or update, staging, commit, reset, checkout, or worktree operation was performed.
The parent should apply the patch only to its isolated checkout of the recorded base, review the handoff separately, and own the final commit.
Do not apply the insertion patch to the shared working skill, which already contains the corrected paragraph.
If the parent base advances, review/rebase this owned paragraph without taking unrelated hunks.

## Validation and disposition

The official `skill-creator` quick validator accepted the updated events skill.
The four-line rule was reviewed against the exact scope/decision contracts and the concrete participant capture/receipt source pattern.
Byte-preservation checks establish the worker's ownership boundary at write time; they do not assert that concurrent owners cannot subsequently edit the shared file.
No design simplification, omitted requested output, or remaining reference blocker.
The bounded maintenance work is implemented; parent source integration and final commit remain pending by assignment.
No claim is made about the completion of the parent feature.

Skills used: official `skill-creator`, `chaos-redux-events`, and `chaos-redux-subagents`, operating in the canonical `chaosx_skill_maintainer` role.
Updated skill: `chaos-redux-events` only.
Created skills: none.
Left unchanged: `chaos-redux-subagents`, official `skill-creator`, and all other skills.
User review needed: none for the authorized correction; parent review of the owned patch and isolated commit is the requested handoff.
