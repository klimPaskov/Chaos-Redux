# Japan-China Chemical Campaign Raids

## Acceptance and current source

The user's 2026-09-20 CBRN implementation request accepted exactly two shared raid categories and native land delivery. `common/raids/japan_cbrn_campaign_raids.txt` defines Japan's chemical campaign inside `chemical_raids`; the old Japan decision category, agent selector, attack decision, and decision-side cost helpers are retired. This source account awaits parent integration and live-game validation.

The 24 raid IDs follow `japan_china_chemical_<chlorine|phosgene|mustard|lewisite>_<normal|sale|evolution>[_optimized]_raid`. A raid selects one enemy-controlled Chinese state, starts from a supply node, uses an assigned division and army-intelligence category, and has five days of native preparation. It reserves only the matching `<agent>_agent_payload` archetype and native Command Power for the selected variant. Human and AI users enter through the same native path; the campaign outcome adapter is `japan_resolve_chemical_campaign_raid_outcome` in `common/scripted_effects/JAP_chemical_campaign_effects.txt`.

## Reservation and cost matrix

| Variant | Exact agent lot | Ordinary Command Power | Optimized Command Power |
| --- | ---: | ---: | ---: |
| Normal | 40 | 20 | 16 |
| Sale | 20 | 10 | 8 |
| Evolution | 10 | 5 | 4 |

The selected tier is fixed at raid creation. Native `essential_equipment` supplies the material reservation and debit; the outcome callback must not debit the same lot again. The prior Political Power charge and standalone cylinder-selector economy are removed under the parent-approved native-raid simplification. Sale and evolution variants are separate raid types within the same Chemical Raids category, not additional categories. Eligibility, authority, exact-state validation, cooldown, exposure, evidence, and Condemnation still depend on their current trigger and effect sources; a failed context cannot be replaced with an inferred target.

## Presentation and validation boundary

The raid file and shared category are the active UI contract. The native chemical raid reuses `GFX_decision_japan_chemical_campaign_attack` from `interface/chaosx_gfx_cleanup.gfx`; the old category and cycle-selector sprites are retired decision art. Final raid GFX and DDS consumer review belongs to the asset owner and parent.

The raid file's probability adapter reported no weighted surfaces and cross-adapter comparison returned `PROBABILITY_SURFACE_EMPTY`, so no raid success or AI weight comparison is established by that result. Static sale tiers cover the source-defined 50% and 75% price variants but do not include other composed Black Friday modifiers from the old universal quote. Source ID and cost checks remain separate from in-game reservation, cancellation, target, and AI behavior. The native cancellation treatment of reserved equipment is not proven by installed documentation and remains a live-game evidence gap.

## Future depth

Historical campaign incidents can receive clearer forensic summaries after the native exact-state outcome, AI selection, and final art are validated; they must continue to use the shared consequence dispatcher.
