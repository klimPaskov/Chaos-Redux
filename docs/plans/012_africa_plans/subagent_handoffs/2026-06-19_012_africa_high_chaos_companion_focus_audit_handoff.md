# Event 012 Africa High-Chaos Companion Focus Audit Handoff

Date: 2026-06-19

## Scope

- Primary file audited: `common/national_focus/012_africa_authority_focus.txt`
- Tree audited: `africa_high_chaos_actor_focus_tree`
- Patch surface audited:
  - `AFR_BEST_kinship_boundary_pacts`
  - `AFR_BEST_night_signal_omens`
  - `AFR_BEST_terracotta_citadel_terms`
  - `AFR_BEST_bon_gentle_veto_court`
  - `AFR_BEST_hyr_night_broadcasts`
  - `AFR_BEST_bir_verified_wall_warnings`
  - `AFR_BEST_sao_terracotta_line`
  - `AFR_BEST_world_witness`

## Files Changed

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-19_012_africa_high_chaos_companion_focus_audit_handoff.md`

No gameplay file was changed. The current focus patch did not show a concrete local issue inside the allowed patch scope.

## Route Coverage

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| BON shared start to Mutual Defense to Bonobo route to World Witness to BON capstone | `AFR_BEST_bestiary_seat` -> `AFR_BEST_habitat_terms` plus `AFR_BEST_charter_limits`/`AFR_BEST_warning_network` -> `AFR_BEST_mutual_defense`; BON route `AFR_BEST_kinship_boundary_pacts`; convergence `AFR_BEST_world_witness`; capstone `AFR_BEST_bon_gentle_veto_court` | Covered | `AFR_BEST_world_witness` includes `AFR_BEST_kinship_boundary_pacts` in its route OR block, and the capstone AND-gates World Witness plus the BON route focus. |
| HYR shared start to Mutual Defense to Hyena route to World Witness to HYR capstone | Shared start and `AFR_BEST_mutual_defense`; HYR/BIR route `AFR_BEST_night_signal_omens`; convergence `AFR_BEST_world_witness`; capstone `AFR_BEST_hyr_night_broadcasts` | Covered | `AFR_BEST_night_signal_omens` is available to HYR or BIR, so HYR does not need another actor branch. HYR capstone is tag-gated to HYR. |
| BIR shared start to Mutual Defense to Bird route to World Witness to BIR capstone | Shared start and `AFR_BEST_mutual_defense`; HYR/BIR route `AFR_BEST_night_signal_omens`; convergence `AFR_BEST_world_witness`; capstone `AFR_BEST_bir_verified_wall_warnings` | Covered | BIR uses the shared signal-omen route focus without relying on HYR's capstone. BIR capstone is tag-gated to BIR. |
| SAO shared start to Mutual Defense to Sao route to World Witness to SAO capstone | Shared start and `AFR_BEST_mutual_defense`; SAO route `AFR_BEST_terracotta_citadel_terms`; convergence `AFR_BEST_world_witness`; capstone `AFR_BEST_sao_terracotta_line` | Covered | `AFR_BEST_world_witness` includes the Sao route focus in its route OR block, and the capstone AND-gates World Witness plus the Sao route focus. |

## High-Priority Findings

None requiring a gameplay patch in the scoped focus file.

The important prerequisite semantics are correct: `AFR_BEST_world_witness` uses separate prerequisite blocks for `AFR_BEST_habitat_terms` and `AFR_BEST_mutual_defense`, making those mandatory, then uses one prerequisite block containing the route focuses, making the route branch an OR. The four new capstones use separate prerequisite blocks for `AFR_BEST_world_witness` and their route focus, making both mandatory.

## Missing or Simplified Content

- No missing BON/HYR/BIR/SAO route or capstone content found in `africa_high_chaos_actor_focus_tree`.
- The tree remains a shared companion tree, not bespoke country trees. That is consistent with the current Event 012 documentation and source-of-truth note, which state that role branches, tag capstones, and tag AI are the intended adaptation layer.
- No broad improvement plan was written because this audit did not find a shallow-route issue specific to the parent patch.

## Icon Coverage

| Focus id | Icon | Coverage | Notes |
| --- | --- | --- | --- |
| `AFR_BEST_kinship_boundary_pacts` | `GFX_goal_africa_charter_league_diplomacy` | Covered | Sprite and `_shine` definitions exist in `interface/012_africa.gfx`; DDS is present at 94x86. |
| `AFR_BEST_night_signal_omens` | `GFX_goal_africa_authority_atlas` | Covered | Sprite and `_shine` definitions exist in `interface/012_africa.gfx`; DDS is present at 94x86. |
| `AFR_BEST_terracotta_citadel_terms` | `GFX_goal_africa_industry_logistics` | Covered | Sprite and `_shine` definitions exist in `interface/012_africa.gfx`; DDS is present at 94x86. |
| `AFR_BEST_bon_gentle_veto_court` | `GFX_goal_africa_charter_league_diplomacy` | Covered | Reuses an existing diplomacy focus icon; acceptable for a small companion capstone. |
| `AFR_BEST_hyr_night_broadcasts` | `GFX_focus_research` | Covered | Vanilla sprite and `_shine` definition exist. |
| `AFR_BEST_bir_verified_wall_warnings` | `GFX_goal_africa_authority_atlas` | Covered | Sprite and `_shine` definitions exist in `interface/012_africa.gfx`; DDS is present at 94x86. |
| `AFR_BEST_sao_terracotta_line` | `GFX_goal_africa_military_forces` | Covered | Sprite and `_shine` definitions exist in `interface/012_africa.gfx`; DDS is present at 94x86. |
| `AFR_BEST_world_witness` | `GFX_goal_africa_world_order_route` | Covered | Sprite and `_shine` definitions exist in `interface/012_africa.gfx`; DDS is present at 94x86. |

## Localisation and Reward Mismatch

- Missing localisation: none found for the seven new focus IDs; each has title and `_desc` keys in `localisation/english/012_african_union_l_english.yml`.
- Reward mismatch: none found in the focus file. Rewards match the route themes closely enough for this companion tree:
  - BON moves habitat trust, league cohesion, alarm relief, and covenant relief.
  - HYR moves liberation momentum, alarm, and covenant pressure.
  - BIR moves archive mandate, alarm relief, and volatility relief.
  - SAO moves authority, old-seat legitimacy, volatility, manpower/equipment, and a bunker.
- Reward tuning uses `constant:africa_focus_reward.*`, `constant:africa_value_delta.*`, and `constant:africa_ai.*`; no literal reward tuning values were found in the audited focuses.

## AI Behavior Gaps

- Focus-local AI: no blocking gap. The new route focuses use `constant:africa_ai.normal` with tag-preferred modifiers where shared, and the new capstones use `constant:africa_ai.strong`, matching nearby Event 012 companion capstones.
- External AI strategy: no blocking gap. `common/ai_strategy/012_africa.txt` contains separate BON, HYR, BIR, and SAO high-chaos actor strategy blocks.
- Remaining risk: focus-local `ai_will_do` is intentionally simple. Deeper campaign-state focus ordering would require broader AI strategy work outside this audit's patch scope.

## Validation Performed

- Consulted required offline Paradox wiki pages, including National focus modding, AI modding, AI focuses, Triggers, Effects, Localisation, Scopes, Data structures, Decision modding, Event modding, Idea modding, Modifiers, and On actions.
- Consulted vanilla documentation under `~/projects/Hearts of Iron IV/documentation/`, including script concepts, effects, triggers, and script constants documentation.
- Inspected vanilla focus precedents for OR prerequisites, search filters, icon definitions, and AI focus weighting.
- Parsed `africa_high_chaos_actor_focus_tree`: 27 focuses; no duplicate IDs; no duplicate x/y coordinates; no missing same-tree `AFR_BEST_*` prerequisite references.
- Checked the seven new focus IDs across `common/national_focus/`: each appears once.
- Checked all `constant:africa_ai.*`, `constant:africa_focus_reward.*`, and `constant:africa_value_delta.*` references used by `012_africa_authority_focus.txt`: no missing keys in `common/script_constants/012_africa_constants.txt`.
- Checked custom focus icons referenced by the new patch: required sprite and `_shine` entries exist and referenced DDS files are present at 94x86.

## Skipped Validation

- No in-game validation was run.
- No localisation or documentation patch was made because the user limited direct edits to the focus file plus this handoff.
- No broader Event 012 completion audit was attempted; the scope was only the BON/HYR/BIR/SAO companion focus patch.

## Residual Risk

- `allow_branch` is load-time visibility. The audited focuses use exact tag gates and match the surrounding shared-tree pattern, but any future dynamic tag/cosmetic transformation would need `mark_focus_tree_layout_dirty` or different gates.
- Several capstones are spread far right on the y=4 capstone row. There are no coordinate collisions and this follows the current one-row capstone pattern, but the parent may still want a visual screenshot pass if focus-line readability is being polished.
- The focus rewards use existing constants rather than bespoke per-tag constants. This keeps the patch small and consistent, but it means some BON/HYR/BIR/SAO values reuse package or actor tuning bands instead of unique tuning entries.
