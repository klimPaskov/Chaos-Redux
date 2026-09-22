# CBRN MIO and industrial concern redesign handoff

Disposition: implemented in source; final asset and engine evidence remain pending.
Acceptance basis: the parent task authorized three functional MIO families, six historical national identities, two advanced project institutions, broad nonduplicative industrial concerns, twelve-node trees, bounded bonuses, and exact equipment badges.

## Organization design

The generic families are `cbrn_chemical_protection_consortium`, `cbrn_biomedical_industry_directorate`, and `cbrn_delivery_engineering_bureau`.
Each family has three foundation traits, two mutually exclusive four-trait specializations, and one capstone, with twelve unique grid positions.
The national variants are `cbrn_ici_organization` for ENG, `cbrn_ig_farben_organization` for GER, `cbrn_dupont_organization` for USA, `cbrn_rhone_poulenc_organization` for FRA, `cbrn_montecatini_organization` for ITA, and `cbrn_showa_denko_organization` for JAP.
Five national variants and their paired concerns are visible in January 1936; Showa Denko's MIO and concern require a date after 1939-05-31.
The fictional `cbrn_advanced_containment_institute` requires sealed-containment research and a completed biological agent project, while `cbrn_strategic_delivery_authority` requires chemical-air research, strategic-use policy, and one of two chemical-air special projects.
Both advanced organizations inherit exactly twelve nodes and have one costed signature trait override.
The six broad paired industrial concerns modify industry, synthetic-resource, or electronics research rather than duplicate MIO CBRN equipment or research bonuses.

## Compatibility and balance

The 32 existing designer trait hooks remain as country-scope triggers and resolve through three reusable MIO-family predicates; the burn-treatment hook deliberately shares the respiratory-care foundation trait.
The nine agent-specific chemical payload archetypes are enumerated directly in delivery matching because the retired generic archetype no longer owns their concrete lots.
Native MIO bonuses add no attack statistic; the highest dedicated reliability stack is DuPont sealed gas masks at +31%, the highest dedicated production-capacity stack is Showa chemical artillery ammunition at +34%, and the highest MIO research stack is delivery engineering at +32%.
The initial seven designer constants changed for combined CBRN budget are choking dose 1.03, persistent contamination 1.02, persistent duration 1.15, low-water cleanup 1.15, rapid-route cleanup 1.15, biological strategic dissemination delivery 1.02, and sealed-assault armored friendly-risk 0.90.
The subsequent same-metric treatment pass set respiratory choking deaths, continuing blister deaths, nerve antidote deaths, mobile casualty sorting, smallpox vaccine scale, and captured-facility mobile containment spread to 0.85 each; distributed-surveillance detection became 1.30.
After the doctrine owner's advisor and hospital retunes, the added chemical-death reductions are 0.85 generic × 0.85 MIO × 0.85 advisor = 0.614125 residual, and the Dimercaprol/advisor/hospital/MIO medical-saturation path is 0.85^4 = 0.52200625 residual.
The active smallpox vaccination program remains a stronger pathogen-specific baseline: its death multiplier 0.45 combines with MIO vaccine scale 0.85 to make 0.3825 total residual before other additional treatment, while a separate biological lifecycle floor caps added project/advisor/MIO benefits against that baseline.
For smallpox captured-facility spread, the vaccination baseline 0.65 × MIO vaccine scale 0.85 × MIO mobile containment 0.85 = 0.469625 total residual; the two additional MIO multipliers alone make 0.7225 relative to that accepted baseline.
Sealed-sample capture release amount still uses its separate 0.50 multiplier, which was outside the authorized same-metric treatment retune and needs consideration in any final captured-facility harm assessment.
The doctrine owner calculated biological potency at 1.4863 including the 1.02 MIO multiplier; the exposure owner is adding a final composite floor for protection stacks.
Chemical shell high output can be reached without a mustard/lewisite technology, while persistent formulation remains a separate optional sibling.
Air precision can be reached without strategic-use policy, while the long-range payload trait requires it.

## Asset contract

`interface/cbrn_mio_industry.gfx` registers eight MIO logos under `gfx/interface/ideas/cbrn_designers/`, six concern idea cards under `gfx/interface/ideas/cbrn_industrial_concerns/`, and 21 exact equipment badge tokens under `gfx/interface/military_industrial_organization/cbrn_badges/`.
Every badge sprite is named `GFX_military_industrial_organization_<matched equipment archetype>`.
Nine chemical agent archetypes share the purpose-made `chemical_agent_payload.dds` texture through nine distinct GFX aliases; chemical artillery, four chemical-air payloads, gas masks, decontamination equipment, CBRN instruments, and four biological bombs each use their own DDS.
The binary DDS package is owned by the icon artist and must be verified against every registered texture path before visual completion is claimed.
The eight organization logo filenames under `gfx/interface/ideas/cbrn_designers/` are `cbrn_ici_organization.dds`, `cbrn_ig_farben_organization.dds`, `cbrn_dupont_organization.dds`, `cbrn_rhone_poulenc_organization.dds`, `cbrn_montecatini_organization.dds`, `cbrn_showa_denko_organization.dds`, `cbrn_advanced_containment_institute.dds`, and `cbrn_strategic_delivery_authority.dds`; their code icon names have the matching `GFX_` prefix.
The six idea-card filenames under `gfx/interface/ideas/cbrn_industrial_concerns/` are `idea_cbrn_ici_concern.dds`, `idea_cbrn_ig_farben_concern.dds`, `idea_cbrn_dupont_concern.dds`, `idea_cbrn_rhone_poulenc_concern.dds`, `idea_cbrn_montecatini_concern.dds`, and `idea_cbrn_showa_denko_concern.dds`; their code picture sprites are `GFX_idea_cbrn_<identity>_concern`.
The thirteen badge filenames under `gfx/interface/military_industrial_organization/cbrn_badges/` are `chemical_agent_payload.dds`, `chemical_artillery_ammunition.dds`, `choking_chemical_air_payload.dds`, `blister_chemical_air_payload.dds`, `nerve_chemical_air_payload.dds`, `incapacitating_chemical_air_payload.dds`, `gas_mask_equipment.dds`, `decontamination_equipment.dds`, `cbrn_instrument_equipment.dds`, `anthrax_bomb_equipment.dds`, `plague_bomb_equipment.dds`, `tularemia_bomb_equipment.dds`, and `smallpox_bomb_equipment.dds`.
The shared chemical-agent badge is registered under nine exact sprite names ending in `chlorine_agent_payload`, `phosgene_agent_payload`, `mustard_agent_payload`, `lewisite_agent_payload`, `tabun_agent_payload`, `sarin_agent_payload`, `soman_agent_payload`, `malodor_agent_payload`, and `behavioral_agent_payload`.

## Files and validation

Organization source: `common/military_industrial_organization/organizations/cbrn_chemical_protection_organizations.txt`, `cbrn_biomedical_organizations.txt`, `cbrn_delivery_organizations.txt`, and `cbrn_national_organizations.txt`, replacing the six-family `cbrn_organizations.txt` and `cbrn_protection_biological_organizations.txt`.
Other source: `common/ideas/cbrn_industrial_concerns.txt`, `common/scripted_triggers/cbrn_designer_triggers.txt`, `common/script_constants/cbrn_designer_constants.txt`, `interface/cbrn_mio_industry.gfx`, `localisation/english/cbrn_mio_redesign_l_english.yml`, and `localisation/english/cbrn_designers_l_english.yml`.
Source checks confirmed twelve named traits and unique positions in each family, valid parent and exclusion links, all national override targets, all MIO names and concern names localized, all 21 matched archetypes present in the equipment bonus enum, and the exact designer constant values.
No Hearts of Iron IV game session was launched.

## Remaining evidence

The icon artist must deliver the registered DDS paths, after which the GFX file must be checked against the actual binary files and image dimensions.
The HOI4 probability adapter returned `INTERNAL_ERROR: Unexpected internal error` for the retired MIO source files and for two replacement family files in the baseline audit, while the biomedical file returned `no_weighted_surfaces`; the AI auditor should try a final exact-file inspection and record the service result without treating source weights as engine probabilities.
The biological integration owner is adding a final 0.50 floor against foundational pathogen-specific treatment for additional project/advisor/MIO lifecycle reductions, and the exposure owner is adding its final chemical treatment/protection composite floor; these consumer changes are outside this MIO handoff's file ownership.
Final documentation reconciliation and any parent integration checks remain with the parent and documentation curator.
