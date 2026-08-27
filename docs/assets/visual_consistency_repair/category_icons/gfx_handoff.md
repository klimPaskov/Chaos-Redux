# GFX handoff: decision-category icon repair

The parent worker owns all `.gfx`, decision, GUI, localisation, and gameplay wiring.

No `.gfx` file was edited by this worker.

The exact runtime texture paths are the eight DDS paths in `manifest.md` under `gfx/interface/decisions/visual_consistency_repair/categories/`.

The parent did not provide exact sprite identifiers or a target `.gfx` filename in the isolated asset brief, so the following are proposed stable sprite names for parent confirmation rather than completed registrations.

| Proposed sprite name | Exact texture path | Suggested target `.gfx` file |
| --- | --- | --- |
| `GFX_decision_category_independence_wave_integration` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_integration.dds` | Parent-selected existing decision-category registry |
| `GFX_decision_category_independence_wave_government` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_government.dds` | Parent-selected existing decision-category registry |
| `GFX_decision_category_independence_wave_diplomacy` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_diplomacy.dds` | Parent-selected existing decision-category registry |
| `GFX_decision_category_independence_wave_network` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_network.dds` | Parent-selected existing decision-category registry |
| `GFX_decision_category_independence_wave_borders` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_borders.dds` | Parent-selected existing decision-category registry |
| `GFX_decision_category_independence_wave_death_survey` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_death_survey.dds` | Parent-selected existing decision-category registry |
| `GFX_decision_category_012_africa_charter_ledger` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_012_africa_charter_ledger.dds` | Parent-selected existing decision-category registry |
| `GFX_decision_category_fallout_food_security` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_fallout_food_security.dds` | Parent-selected existing decision-category registry |

Ready-to-copy sprite pattern after parent confirms the identifier and owning registry:

```text
spriteType = { name = "GFX_decision_category_independence_wave_integration" texturefile = "gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_integration.dds" }
```

The same one-line structure applies to the other seven exact texture paths.

The parent should visually review `contact_sheet_review.png` before runtime promotion.

All eight assets passed source alpha, processed alpha, 52x40 dimension, strict DDS legacy-header, exact-length, and decoded pixel round-trip checks, but remain `needs_user_review` because this worker cannot perform parent wiring or in-game consumer validation.

No animation, fallback background removal, opaque backdrop, generated text, fake UI, fake meters, or existing decision art substitution was used.
