# Event 006 focus-tree read-only handoff — 2026-07-26

> Supersession notice (2026-07-26): This pre-reflow baseline is retained for its original MCP diagnostics. Commit `f8ca54d24` and `006_shared_focus_geometry_repair_2026_07_26.md` supersede its coordinate state, while `006_agx_focus_overlay_handoff_2026_07_26.md` supersedes the AGX-missing-module wording. Post-edit `hoi4.focus_inspect` and `hoi4.focus_render` returned `Transport closed`, so the shared layout remains **HOLD** and no post-edit engine metric is claimed.

## Scope and verdict

This is a bounded, pre-reflow read-only audit of the shared Event 006 focus tree and the admitted IW-007 Frisia/AGX package. No focus source, localisation, icon, AI, or runtime-attestation file was changed in this pass. Its historical verdict remains **HOLD** for the fourteen-blocker baseline; the AGX package-module absence statement is superseded by `006_agx_focus_overlay_handoff_2026_07_26.md`.

The evidence below is carried forward from the latest completion and layout audits, especially `006_event_completion_audit_v6_2026_07_26.md`, `006_focus_tree_completion_audit_2026_07_25.md`, and `006_focus_layout_repair_v3_2026_07_25.md`.

## Current diagnostics

The recorded `hoi4.focus_inspect` baseline for `independence_wave_focus_tree` is:

| Measure | Recorded value |
| --- | ---: |
| Regular focuses | 176 |
| Connectors | 214 |
| Crossings | 49 |
| Intersections | 18 |
| Long connectors | 26 |
| Blocking diagnostics | 14 |
| Layout hash | `3e5996acbdbed97ab085d52cd058861f2fbd21acc896f859268b204a9c81a5a2` |

No parser, unresolved focus-reference, icon-existence, or localisation-key blocker was recorded in the source audit. The old economy-capstone finding is superseded: `independence_wave_independent_treasury` now exposes the continuing `independence_wave_treasury_backed_public_works` decision in `common/decisions/006_independence_wave_decisions.txt`.

## Route coverage

| Required route | Current coverage | Evidence / limitation |
| --- | --- | --- |
| Survival and founding settlement | Present | `independence_wave_complete_founding_settlement`, `independence_wave_bind_the_first_oath`, `independence_wave_integrate_provinces_and_councils`, `independence_wave_map_internal_power_centers`. |
| Economy and treasury | Present | `independence_wave_inventory_the_state`, `independence_wave_establish_emergency_revenue`, `independence_wave_secure_food_and_fuel`, `independence_wave_build_regional_transport_authority`, `independence_wave_create_independent_treasury`, `independence_wave_independent_treasury`; continuing decision hook is wired. |
| Military and command | Present | `independence_wave_integrate_militia_commands`, `independence_wave_secure_national_depots`, `independence_wave_adopt_military_archetype_program`, `independence_wave_confirm_civilian_control`, `independence_wave_grant_military_autonomy`, `independence_wave_build_professional_core`, `independence_wave_adopt_border_defense`, `independence_wave_adopt_reclamation_doctrine`, `independence_wave_preserve_independent_command`, `independence_wave_standardize_with_league`, `independence_wave_found_professional_defense_institution`. |
| Government / former host / regional overlay | Present | Shared framework and overlay focuses are loaded in `common/national_focus/006_independence_wave_focus.txt`; route naming is still largely generic. |
| League, high-chaos, formables | Present | Existing generic and bounded package/formable modules provide the route families. |
| IW-007 Frisia (AGX) package ambition | **Missing** | AGX reaches the shared framework, overlay, and package decision surfaces, but no `AGX`-/`Frisia`-named focus identifier or accepted narrow module exists. The registry row is Level 1, while the latest Event 006 completion authority explicitly requires the admitted narrow module. |

## Missing, simplified, or blocked content

### Layout blockers (14)

The latest layout repair audit groups the blockers as follows:

1. The `independence_wave_bind_the_first_oath` → `independence_wave_integrate_provinces_and_councils` connector crosses the `independence_wave_inventory_the_state` → `independence_wave_establish_emergency_revenue` connector (two diagnostics).
2. The `independence_wave_complete_founding_settlement` connectors to `independence_wave_ajx_appoint_neutral_commission_focus`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states` each cross `independence_wave_secure_food_and_fuel` → `independence_wave_build_regional_transport_authority`, and each also crosses `independence_wave_secure_national_depots` → `independence_wave_recall_and_vet_officers` (six diagnostics).
3. The professional-defence convergence around `independence_wave_adopt_military_archetype_program`, `independence_wave_confirm_civilian_control`, `independence_wave_grant_military_autonomy`, `independence_wave_build_professional_core`, and `independence_wave_found_professional_defense_institution` produces the remaining six crossings.

Non-blocking geometry warnings include the long connectors `independence_wave_complete_founding_settlement` → `independence_wave_map_internal_power_centers`, `independence_wave_inventory_the_state` → `independence_wave_establish_emergency_revenue`, and `independence_wave_bind_the_first_oath` → `independence_wave_integrate_militia_commands`, plus a through-node warning from `independence_wave_complete_founding_settlement` → `independence_wave_survey_regional_ambition`.

These are a coupled layout problem. The prior single-node probes and a broader attempted reflow were reverted because they left blockers unchanged or increased crossings/intersections.

### AGX/Frisia module gap

`common/national_focus/006_independence_wave_focus.txt` contains no accepted `AGX`-/`Frisia`-named focus module. The package handoff (`006_wallonia_frisia_package_handoff.md`) supplies the intended bounded identity: constitutional/cultural-council/patron-client choices, host negotiation and guarded-frontier/association routes, coastal-maritime opening force, labor-council versus ministry tension, and a North Sea coastal league / Low Countries Federation hook. This should be attached to the existing framework without adding a new route family or inventing a new formable chain.

## Icon coverage

| Surface | Status | Note |
| --- | --- | --- |
| Existing focus blocks | Pass for reference wiring | The source audit found an icon reference for every parsed focus/shared block. |
| Route-family distinctness | Partial | Generic icon families repeat across government, host, and ambition routes; this is a readability concern, not an unresolved asset reference. |
| AGX module | Not applicable yet | No AGX focus IDs exist, so there is no AGX icon coverage to verify. Any module patch must select existing registered focus sprites or provide an explicitly reviewed icon handoff. |

## Localisation and reward alignment

- Existing parsed focuses have title/description localisation coverage; no unresolved key blocker was recorded.
- Dynamic country/package naming is incomplete: government, patron, and former-host route labels remain generic in places, contrary to the shared-adaptation guidance.
- The treasury capstone mismatch is closed by the continuing decision hook noted above; do not regress it while reflowing or adding AGX content.
- AGX has no focus localisation or focus reward surface because its package-named module is absent. A future narrow module must add matching title/description keys and make each reward point to existing AGX decision/effect/formable hooks rather than a passive placeholder.

## AI behavior gaps

- Every audited focus block has an `ai_will_do` block.
- Existing strategy files cover a bounded set of package tags, but there is no complete 206-row package sweep.
- AGX has no package-specific focus route weights or module-level route invalidation because the module is absent. The future patch must keep patron, league, and former-host choices invalid when their package triggers disallow them, and should align with `common/ai_strategy/006_independence_wave_wallonia_frisia.txt`.

## Queued actions for the parent

1. Use `hoi4.focus_inspect` and `hoi4.focus_render` for one coordinated reflow of the founding/economy, founding/regional/officer, and professional-defence convergence clusters. Do not suppress connectors by changing prerequisites, and do not repeat isolated one-node nudges without measuring all four geometry metrics.
2. Add a narrow AGX/Frisia package module in the existing Event 006 focus scope, anchored to the shared framework and existing package decision/effect hooks. Keep it package-named, coastal/North-Sea in identity, and limited in scope; do not add a route family or new formable chain.
3. Add and verify the module's localisation, icon references, AI weights, prerequisites/bypasses, mutual exclusions, and reward-to-decision/formable hooks in the same implementation tranche.
4. Re-run focus inspection/render and source-level loc/icon/AI/reference checks after both changes. Parent-owned runtime attestation remains outside this handoff.

## Validation and limits

This handoff records the latest source and MCP audit evidence; no new gameplay edit was made and no fresh runtime launch was attempted. The referenced audits document the inspect baseline and the reverted layout probes. Because the parent requested immediate handoff, the coupled reflow and AGX implementation remain queued rather than guessed.
