# Historical CBRN Advisors Implementation Handoff

Date: 2026-08-04.

## Supersession notice

The advisor-card production and review claims in this handoff are superseded by the actual-workflow re-audit under `docs/assets/chaos_warfare_historical_advisors/v2_actual_workflow/` and its follow-up handoff. Keep this file as the historical implementation record, but use the v2 package for current asset provenance, conversion, and review status.

The current correction also assigns political-advisor cards through `portraits.civilian.small` and theorist cards through `portraits.army.small`; all twelve cards retain their existing `portraits.army.large` scientist consumers.

## Implemented scope

- Converted twelve existing startup-generated scientists into static dual-role scientist/advisor characters without creating duplicate identities.
- Preserved every existing scientist skill, trait, portrait, and identity flag consumer.
- Added five theorist appointments and seven political-advisor appointments across AST, ENG, GER, JAP, POL, SOV, and USA.
- Kept Howard Florey and Alexander Fleming ungated as medical countermeasure specialists.
- Required Chaos Warfare for the ten appointments tied to offensive, retaliatory, clandestine, or dual-use weaponization programs.
- Added route-aware AI weights for prepared, battlefield, defensive, and active-outbreak profiles.
- Added strong static advisor benefits and operational effects for chemical potency, contamination, deaths, readiness efficiency, biological potency, growth, spread, deaths, medical saturation, detection, and Condemnation.
- Routed all operational effects through the existing shared chemical exposure, Chemical Readiness, and biological lifecycle systems.
- Preserved payload debit, evidence, attribution, and recorded deaths.
- Corrected Franciszek Witaszek's unsupported exact typhus wording and represented his documented resistance CBW sabotage role.

## Gameplay files

- `common/characters/cbrn_historical_specialists.txt`
- `common/country_leader/cbrn_historical_advisor_traits.txt`
- `common/script_constants/cbrn_historical_advisor_constants.txt`
- `common/scripted_effects/cbrn_historical_advisor_effects.txt`
- `common/scripted_effects/cbrn_exposure_effects.txt`
- `common/scripted_effects/biological_lifecycle_effects.txt`
- `common/scripted_effects/cbrn_protection_effects.txt`
- `common/scripted_effects/chaosx_startup_history_effects.txt`
- `localisation/english/chaosx_characters_l_english.yml`

## Asset files

- `gfx/interface/advisors/cbrn/*.dds`
- `interface/cbrn_historical_advisors.gfx`
- `docs/assets/chaos_warfare_historical_advisors/processed/*.png`
- `docs/assets/chaos_warfare_historical_advisors/review_4x/*.png`
- `docs/assets/chaos_warfare_historical_advisors/asset_manifest.md`
- `docs/assets/chaos_warfare_historical_advisors/gfx_handoff.md`

No existing Chaos Redux icon was overwritten.
No generic icon, placeholder, cross-type substitute, or direct resized leader portrait was wired as an advisor card.

## Workflow maintenance

The required advisor compositor exposed a Pillow-version incompatibility in its DDS pixel iterator.
The tool and its regression test now use a version-safe iterator, and the tool optionally writes a nearest-neighbour 4x review PNG.
The three compositor regression tests pass.

## Historical and visual audits

The historical source audit is recorded in `2026-08-04_chaos_warfare_named_scientists_source_audit.md` and includes identity hashes, role-fit evidence, confidence, and sensitive-history constraints.

Independent reviewer `019fcc70-9914-7db0-ab65-a45c1e2577c1` inspected all twelve native cards and all twelve 4x review images.
Every card passed canonical-template integrity, readable identity, vanilla dossier framing, no portrait spill, native 65x67 dimensions, and 4x 260x268 dimensions.

## Meaningful validation

- Exactly twelve static character IDs exist and exactly twelve startup recruitment calls replace the former generators.
- Exactly ten aggressive or dual-use appointments require Chaos Warfare; Florey and Fleming remain ungated.
- Every trait name, description, and operational tooltip resolves once in English localisation.
- Every small portrait sprite resolves to an installed 65x67 DDS.
- Every referenced historical-advisor script constant exists in the centralized tuning table.
- Shared chemical and biological consequence floors remain downstream of the new Condemnation multipliers.
- Advisor effect helpers contain no evidence or attribution writes.

## Simplifications, omissions, and blockers

No simplification, fallback, placeholder, or omitted roster member remains in this implementation tranche.
