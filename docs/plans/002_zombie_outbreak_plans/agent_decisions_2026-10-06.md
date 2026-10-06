# Event 002 release cleanup decisions, 2026-10-06

## Authority and current disposition

The parent accepted the bounded Event 002 category consolidation under the user's G6 release-QA authorization. The consolidation is implemented in the current Event 002 source and its source-driven checks; live map selection and numeric AI comparison remain unresolved. This record does not assert approval beyond that bounded cleanup or claim live-game validation.

## Accepted consolidation design

The weaponized outbreak category previously defined eight separate zero-cost profile-review decisions and eight separate counterstrain research decisions. The current source has one profile-review action and one targeted counterstrain action, preserving selection of each live strain, the existing Political Power cost, the existing research duration, the 34-point progress amount, the 240-day exposure effect, the shared-progress behavior, and the receipt-aware cancellation refund.

The two actions will target each eligible profile's capital state and use `on_map_mode = map_only`. The review marker and research marker will use distinct native decision icons and separate actions. Their markers refer to the exact selected profile; the research action stores that profile's single type at purchase. A malformed profile with zero or multiple type flags remains inspectable but its research action reports why it cannot be selected. If the selected profile ceases to be a live profile or its type changes while research is active, the action cancels, clears its selected-target state, and returns the paid PP and applicable sale credit.

The native target-mode evidence says `state_target` decisions use `FROM` as the selected state and their icons appear over that state; `on_map_mode = map_only` leaves the targeted action on the map and out of the decision menu. Vanilla `AFG.txt:1901-1929` uses `state_target = any_controlled_state`, `on_map_mode = map_only`, and a timed completion effect against the same `FROM` state. Two actions at one capital will use separate icons and labels. No retrieved documentation establishes how overlapping same-state decision icons stack or offset, so the separate-click behavior remains a live acceptance check.

The profile type constructors normally enforce a single type: `weaponized_zombie_set_type_*` clears the eight type flags before setting one, and triggerable profiles clear them before applying their selected type. The profile-copy path copies source flags verbatim, so the target gate still needs an explicit exactly-one-type check; the design does not rely on branch order.

Standalone weaponized profiles are valid research targets. The owning category currently requires the standard outbreak global flag, however, which can hide counterstrain research after that flag is cleared even while a live weaponized horde remains. The accepted source patch must make category visibility follow the same standard-outbreak-or-live-weaponized condition as the generic research action.

## Baseline and evidence limits

The frozen pre-change sources are in `source_snapshots/pre_clutter_20261006/`, with SHA-256 values in that folder's manifest. The current typed decision source at the freeze was `801E222166733AA43D43A523F6D3B950BCC54EBB36ED9539731AD4D47487CDD3`.

The source-inspector discovery returned 13 `decision_ai_will_do` candidates in the file and confirmed source factors of 0 for profile reviews and 1 for each typed research action. These are score inputs, not normalized probabilities. The targeted probability scenario/evaluation request is still unresolved; no numeric compare may be inferred from candidate counts or source factors.

The first-anniversary memorial remains a single opt-in report per participant, with the existing 10 PP reward once. All eight per-type branches in `apply_weaponized_zombie_counterstrain_research` remain the output contract for type-specific local/shared progress and the corresponding readiness/exposure effects. The current tuning is confirmed by `common/script_constants/chaosx_triggerable_scenarios_constants.txt:295-298`: 45 Political Power base cost, 55-day research, 34 progress, and 240-day exposure. These values are preserved, not retuned.
