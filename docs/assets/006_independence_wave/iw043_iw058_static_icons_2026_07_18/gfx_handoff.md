# GFX handoff — IW-043 / IW-058 static icons

No `.gfx` file was edited by the asset producer. The parent implementation agent should register the category and decision sprites in the Event 006 interface GFX file, then point the live decision/category definitions at these exact sprite names. The existing idea GFX registration already uses the idea sprite names and texture family listed below.

Suggested registration file: `interface/006_independence_wave_iw043_iw058_decision_icons.gfx` (or the parent agent's existing Event 006 decision-icon GFX file if one is already the source of truth).

## Decision categories — proposed sprite registrations

These sprite names are required by `common/decisions/categories/006_independence_wave_iw043_iw058_categories.txt`:

| Sprite name | Texture path | Target |
|---|---|---:|
| `GFX_decision_category_independence_wave_iw043_middle_volga_congress` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_category_independence_wave_iw043_middle_volga_congress.dds` | 52x40 |
| `GFX_decision_category_independence_wave_iw058_council_of_communities` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_category_independence_wave_iw058_council_of_communities.dds` | 52x40 |

The category source art is transparent after chroma-key removal and carries the requested institutional seal treatment. The 52x40 size follows the canonical decision-category reference family; it is not a fallback or a resized decision icon.

## Decisions — proposed sprite registrations

These sprite names are required by `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`:

| Sprite name | Texture path | Target |
|---|---|---:|
| `GFX_decision_independence_wave_iw043_congress` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw043_congress.dds` | 32x32 |
| `GFX_decision_independence_wave_iw043_diplomacy` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw043_diplomacy.dds` | 32x32 |
| `GFX_decision_independence_wave_iw043_formable` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw043_formable.dds` | 32x32 |
| `GFX_decision_independence_wave_iw043_guard` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw043_guard.dds` | 32x32 |
| `GFX_decision_independence_wave_iw043_rights` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw043_rights.dds` | 32x32 |
| `GFX_decision_independence_wave_iw043_river` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw043_river.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_aramean_guarantee` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_aramean_guarantee.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_assyrian_guarantee` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_assyrian_guarantee.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_chaldean_guarantee` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_chaldean_guarantee.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_council` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_council.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_diplomacy` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_diplomacy.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_formable` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_formable.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_guarantees` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_guarantees.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_security` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_security.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_settlement` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_settlement.dds` | 32x32 |
| `GFX_decision_independence_wave_iw058_syriac_guarantee` | `gfx/interface/decisions/006_independence_wave/volga_assyria/decision_independence_wave_iw058_syriac_guarantee.dds` | 32x32 |

## Ideas / national spirits — existing sprite names

`interface/006_independence_wave_iw043_iw058_idea_icons.gfx` already registers these exact names and texture paths:

| Sprite name | Texture path | Target |
|---|---|---:|
| `GFX_idea_independence_wave_iw043_congress` | `gfx/interface/ideas/006_independence_wave/volga_assyria/idea_independence_wave_iw043_congress.dds` | 64x64 |
| `GFX_idea_independence_wave_iw043_river_economy` | `gfx/interface/ideas/006_independence_wave/volga_assyria/idea_independence_wave_iw043_river_economy.dds` | 64x64 |
| `GFX_idea_independence_wave_iw043_river_guard` | `gfx/interface/ideas/006_independence_wave/volga_assyria/idea_independence_wave_iw043_river_guard.dds` | 64x64 |
| `GFX_idea_independence_wave_iw058_corridor` | `gfx/interface/ideas/006_independence_wave/volga_assyria/idea_independence_wave_iw058_corridor.dds` | 64x64 |
| `GFX_idea_independence_wave_iw058_council` | `gfx/interface/ideas/006_independence_wave/volga_assyria/idea_independence_wave_iw058_council.dds` | 64x64 |
| `GFX_idea_independence_wave_iw058_diaspora` | `gfx/interface/ideas/006_independence_wave/volga_assyria/idea_independence_wave_iw058_diaspora.dds` | 64x64 |

## Achievement variants

The three final achievement DDS files are installed at the root runtime paths expected by the achievement definition. The Volga triplet is not touched.

| Variant | Runtime texture |
|---|---|
| completed | `gfx/achievements/chaosx_006_assyria_survives.dds` |
| grey | `gfx/achievements/chaosx_006_assyria_survives_grey.dds` |
| not eligible | `gfx/achievements/chaosx_006_assyria_survives_not_eligible.dds` |

Achievement art is opaque 64x64 full-pixel art. The grey and not-eligible variants are derived from the same approved source with the canonical vanilla overlay treatment; they are not separate unrelated compositions.

## Explicit exclusions

Zero advisor/adviser, dossier-card, portrait, small/commander, military-high-command, theorist, or character assets are present or requested in this handoff. No advisor GFX path, sprite name, or placeholder is supplied.
