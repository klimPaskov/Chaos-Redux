# Holy Realm Focus Tree Non-Soviet Audit Patch Handoff

Date: 2026-05-29

## Scope

Focus-tree-only audit and bounded patch for `common/national_focus/003_holy_realm.txt` against the non-Soviet Holy Realm focus requirements in `tmp/chaos_redux_multi_system_fix_spec.md`.

The worktree was already dirty before this audit, including `common/national_focus/003_holy_realm.txt`. This handoff only describes the bounded focus-file edits made in this pass.

## Files Changed

- `common/national_focus/003_holy_realm.txt`
- `docs/plans/003_holy_realm_plans/subagent_handoffs/2026-05-29_focus_tree_non_soviet_audit_patch.md`

No localisation keys were changed.

## Changed Focus IDs

- `THR_mandala_bureau`
- `THR_lamps_remain_lit`
- `THR_white_flags_foreign_roads`
- `THR_vow_against_annihilation`
- `THR_no_one_leaves_mandala`
- `THR_final_silence`
- `THR_permit_foreign_pilgrimage`
- `THR_letters_to_war_tired`
- `THR_shelter_exiles`
- `THR_mandala_of_nations`
- `THR_last_human_signature`
- `THR_sermon_without_translation`
- `THR_compassion_of_non_return`
- `THR_ministry_of_release`

## Route Coverage

| Required route or correction | Implemented branch or focus | Status | Notes |
| --- | --- | --- | --- |
| Focus filter cleanup | Peace, Final Silence, Mandala/intelligence focuses | Patched | Added custom filters to key peace/final/Mandala focuses and vanilla research filter to `THR_mandala_bureau`. |
| Vow Against Annihilation should unlock Lamps branch | `THR_vow_against_annihilation`, `THR_lamps_remain_lit` | Partially patched | Focus completion now sets clear peace route flags and autocompletes `THR_lamps_remain_lit` if missing. Event-option wiring in `chaosx.nr3.70.b` remains outside this focus-only scope. |
| Ministry of Silence AND prerequisites | `THR_ministry_of_release` | Already satisfied | Internal ID remains stable, localisation displays Ministry of Silence. It has separate prerequisites for `THR_sermon_without_translation`, `THR_last_human_signature`, and `THR_compassion_of_non_return`, which is AND semantics. |
| Last Authorization final focus requiring Ministry | `THR_final_silence` | Patched | `THR_final_silence` is localised as The Last Authorization, requires `THR_ministry_of_release`, and was moved down to `y = 14` so it reads as the final endpoint. |
| Three 14-day prerequisite focuses with real effects | `THR_last_human_signature`, `THR_sermon_without_translation`, `THR_compassion_of_non_return` | Already satisfied, filters patched | They use `@thr_focus_cost_two_weeks` and set existing decision-unlock flags for audits, warnings, and shelters. |
| White Flags should unlock intervention/letters/observers/peacekeeping | `THR_white_flags_foreign_roads` | Partially patched | Added existing unlock/memory flags for peacekeeping, mediation, foreign-road memory, and peace letters. Full observer/volunteer/intervention decision families are broader decision work. |
| Mandala of Nations super-event trigger | `THR_mandala_of_nations` | Already satisfied, filters patched | Focus sets `holy_realm_super_event_id = constant:holy_realm_super_event.mandala_of_nations` and calls `holy_realm_show_super_event = yes`. |
| Peace focuses unlock mechanics rather than repeated flat rewards | Peace branch | Partial | Added/confirmed unlock flags for the main White Flags pivot. Several later peace focuses still mostly grant stats/reach and need broader decision/mechanic work. |

## Before And After

Before:

- Some key peace focuses were not tagged with `FOCUS_FILTER_THR_PEACE`.
- Final Silence prep and terminal focuses were not consistently tagged with `FOCUS_FILTER_THR_FINAL_SILENCE_PRESSURE`.
- `THR_mandala_bureau` was not filterable through research/Mandala-oriented filters despite being the intelligence agency pivot.
- `THR_white_flags_foreign_roads` set peacekeeping doctrine but did not set the existing peace-letter and mediation unlock/memory flags.
- `THR_vow_against_annihilation` renounced Final Silence but did not defensively set peace-route flags or autocomplete `THR_lamps_remain_lit` if reached through an alternate route.
- `THR_final_silence` sat on the same row as late preparation focuses, weakening its final-branch endpoint presentation.

After:

- Peace branch anchors and follow-ups have `FOCUS_FILTER_THR_PEACE`.
- Final Silence prep, `THR_no_one_leaves_mandala`, `THR_ministry_of_release`, and `THR_final_silence` have `FOCUS_FILTER_THR_FINAL_SILENCE_PRESSURE`.
- `THR_mandala_bureau` has `FOCUS_FILTER_RESEARCH` and `FOCUS_FILTER_THR_MANDALA_INTEGRATION`.
- `THR_white_flags_foreign_roads` sets `holy_realm_memory_white_flags_foreign_roads`, `holy_realm_memory_mediation_offered`, `holy_realm_expansion_letters_unlocked`, and `holy_realm_peace_letter_minor_unlocked`.
- `THR_vow_against_annihilation` sets `holy_realm_peace_route_opened`, restraint doctrine flags, and completes `THR_lamps_remain_lit` if it is not already completed.
- `THR_final_silence` has the Final Silence custom filter and is placed at `y = 14`.

## Localisation And Icon Changes

Localisation keys changed: none.

Icon IDs changed: none.

Icon coverage remains mixed: the tree uses existing custom Holy Realm icons and vanilla/generic focus icons. No missing icon references were patched in this pass.

## Validation

Ran local text validation:

- `common/national_focus/003_holy_realm.txt` brace balance: OK.
- Unsupported operators `<=` or `>=` in the touched focus file: none.
- Focus prerequisite and mutual-exclusion references inside `003_holy_realm.txt`: no missing focus IDs.
- Holy Realm focus name/description localisation coverage in `003_the_holy_realm_l_english.yml`: no missing focus name or description keys.
- Custom focus filter localisation for `FOCUS_FILTER_THR_PEACE`, `FOCUS_FILTER_THR_FINAL_SILENCE_PRESSURE`, and `FOCUS_FILTER_THR_MANDALA_INTEGRATION`: present.

Skipped validation:

- No full HOI4 load test or in-game focus UI validation was run from this environment.
- No decision/event validation was run because the task scope forbids editing those systems.

## Remaining Gaps And Risks

- The event option in `chaosx.nr3.70.b` still only calls `holy_realm_renounce_final_silence = yes`; making that option directly autocomplete `THR_lamps_remain_lit` is event-file work and was left untouched by scope.
- White Flags now unlock existing peace-letter and mediation/peacekeeping hooks, but dedicated observer, volunteer, and intervention decision families are not fully implemented in the focus file. That is broader decision content.
- Several peace branch focuses still rely on manpower, stability, political power, Mandala Reach, or infrastructure-style rewards. A full rework into arbitration, development, peacekeeping, and faction-member protection missions belongs in decision/mechanic implementation rather than this bounded focus patch.
- Many Holy Realm focuses still lack route-specific `ai_will_do`. The high-impact route anchors have some AI behavior, but a full AI route pass remains open.
- The focus tree file had pre-existing formatting and indentation irregularities. This pass did not reformat unrelated blocks.
