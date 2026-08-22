# Chaos Warfare package country-profile audit

Status: actionable AI migration finding fixed; two findings rejected against accepted authority; one MIO engine boundary retained

## Audit scope

The mapped `chaosx_country_package_auditor` reviewed starting protective reserves, gas-mask progression, the seven major and secondary country profiles, route-aware research and production, regimental and Headquarters preferences, and CBRN Military Industrial Organizations.

This report records the parent review of every returned finding. It is not a completion claim for the overall package.

## Confirmed coverage

- `cbrn_starting_masks` and `chaosx_apply_starting_cbrn_mask_profiles` cover every country named by the starting-stockpile matrix plus additional secondary profiles.
- Britain receives 45,000 tuned starting crates and the strongest starting civilian distribution share.
- Gas-mask model progression is `gas_mask_equipment_1` through `gas_mask_equipment_4`, with matching technology, production, sprite, and localisation surfaces.
- Seven major selectors and multiple secondary selectors exist in `common/scripted_triggers/cbrn_ai_profile_triggers.txt`.
- Country profiles affect research, production, Headquarters, regimental roles, protection, containment, sanctions, and route preference without granting payload, policy, target, condition, or success authorization.
- Six distinct generic CBRN MIO families, trait trees, exact equipment scopes, assets, localisation, and differentiated AI weights exist.

## Actionable finding fixed

The retained Livens and armored-delivery AI files could compete with ordinary army production without the shared protection and conventional-stock gates.

The parent changed:

- `common/ai_strategy/chemical_warfare_livens.txt`
- `common/ai_strategy/chemical_warfare_tank_shells.txt`
- `docs/systems/cbrn_warfare/chemical_warfare/cbrn_regimental_support.md`

Every Livens research, production, and template-pressure block and every armored-delivery production or template-pressure block now requires `cbrn_ai_can_expand_offensive_cbrn_production`.

Armored-delivery pressure was also corrected from ordinary `light_tank_chassis`, `medium_tank_chassis`, and `heavy_tank_chassis` minimum-factory pressure to the exact `light_tank_flame_chassis`, `medium_tank_flame_chassis`, and `heavy_tank_flame_chassis` variant-production pattern used by the consolidated detachments. The installed vanilla German AI file supplies the same `equipment_variant_production_factor` precedent for flame-role chassis.

The weighted-surface inspector found eight Livens strategy-factor consumers, no unresolved input, and no diagnostic after the change. Its adapter does not model `equipment_variant_production_factor`, so the armored correction is source- and vanilla-precedent evidence rather than a weighted-tool result.

## Findings rejected against accepted authority

### Starting totals

The auditor requested runtime population/OOB-derived starting stock.

That finding is rejected because the user explicitly required the exact totals to be recorded as gameplay tuning with honest historical confidence. The accepted Stage 2 design records the tuned totals inside the matrix bands, keeps military issue and civilian distribution separate, uses real fielded need and real state population when issuing the finite stock, and identifies exact-total confidence as lower than the relative historical profile.

This does not turn a technology grant into free coverage. A country can issue only the tuned crates it actually receives, and civilian distribution receives only stock left after military issue.

### Missing AI profile matrix

The auditor named `matrices/ai_country_profile_matrix.md`.

That file is not part of the accepted package. The authoritative matrix set contains `ai_behavior_matrix.md` and `country_program_and_designer_matrix.md`, and both were implemented and audited. No new source-of-truth matrix is invented during implementation.

## Supported AI production mapping

The engine's AI-strategy database exposes static strategy values rather than a runtime percentage-allocation field. `common/ai_strategy/cbrn_protection_production.txt` uses supported mask equipment-production factors, real shortage/target stop conditions, and non-overlapping military-factory bands to realize the matrix's suggested 4–10 percent emergency priority “if possible.”

This is recorded as a discrete supported AI realization, not an exact percentage claim. The package does not claim that the engine guarantees a precise share of total military output.

## MIO country-identity boundary

The six CBRN organizations use program and technology visibility/availability plus country- and posture-specific `ai_will_do` factors. Each major profile therefore receives protective and offensive or medical organization preference without creating free access or assigning a designer through an invented effect.

The organization database's `allowed` block is evaluated at game start. It can statically partition organizations by a known starting tag, but it cannot supply the requested dynamic country-program assignment after tag changes, generated-country setup, doctrine adoption, or later program establishment. The current generic names are permitted by numbered specification 10, and the differentiated selection weights are implemented; no dynamic static-assignment substitute is claimed.

Historically sourced unique national firm identities remain absent. Because the accepted spec says to use existing firms where available, that absence remains an explicit documentation and completion-audit item rather than an implied pass.

## Remaining disposition

- Exact live production shares and long-run AI pacing remain user-owned consumer validation.
- The technology progression review was textual because no Technology Tree Viewer was exposed.
- Exact country-specific historical MIO identities remain unresolved; no invented firm or dynamic assignment fallback is authorized.
