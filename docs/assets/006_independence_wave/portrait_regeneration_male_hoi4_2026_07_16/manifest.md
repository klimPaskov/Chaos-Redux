# Event 006 male HOI4 portrait regeneration manifest

## Scope and completion state

This package replaces every non-approved large Event 006 regional portrait with a distinct male fictional subject in a restrained painted Hearts of Iron IV style. The completed inventory is twenty independently generated 156x210 large portraits plus ten 65x67 commander-small derivatives made from the matching new commander masters.

- Source mode: OpenAI built-in ImageGen, one independent successful generation per large master. One RHI river-commandant attempt was rejected during output moderation and produced no image; the unchanged prompt was retried once. No fallback or substitution was used.
- Identity mode: fictional adult men designed for the exact regional civil or military office named by each runtime token.
- Style references: canonical vanilla leader and commander portraits were used only as visual direction for framing, value structure, period treatment, and painterly finish; they were not identity inputs.
- Runtime large format: 156x210, legacy uncompressed 32-bit BGRA DDS.
- Runtime commander-small format: 65x67, legacy uncompressed 32-bit BGRA DDS with canonical dossier-card transparency.
- Immutable exceptions: the approved historical Rupprecht of Bavaria and Josef Friedrich Matthes DDS files were not generated, processed, or overwritten.
- Advisor boundary: no advisor icon was generated, processed, installed, renamed, or wired.

## Completed inventory

| Region | Civil or institutional large portrait | Commander large portrait | Matching commander-small | Runtime state |
| --- | --- | --- | --- | --- |
| ACX | `portrait_ACX_cornish_port_and_mines_committee` | `portrait_ACX_cornish_coastal_commander` | `portrait_ACX_cornish_coastal_commander_small` | Installed readiness-pool art; intentionally unregistered until IW-003 admission |
| AEX | `portrait_AEX_flemish_civil_industrial_board` | `portrait_AEX_flemish_industrial_security_commander` | `portrait_AEX_flemish_industrial_security_commander_small` | Installed readiness-pool art; intentionally unregistered until IW-005 admission |
| AFX | `portrait_AFX_walloon_provisional_assembly` | `portrait_AFX_walloon_reserve_commander` | `portrait_AFX_walloon_reserve_commander_small` | Installed |
| AGX | `portrait_AGX_friesland_coastal_council` | `portrait_AGX_friesland_coastal_commander` | `portrait_AGX_friesland_coastal_commander_small` | Installed |
| AJX | `portrait_AJX_saar_municipal_neutral_commission` | `portrait_AJX_saar_industrial_security_commissioner` | `portrait_AJX_saar_industrial_security_commissioner_small` | Installed |
| BAY | `portrait_BAY_independence_wave_state_council` | `portrait_BAY_independence_wave_mountain_commandant` | `portrait_BAY_independence_wave_mountain_commandant_small` | Installed |
| BRI | `portrait_BRI_independence_wave_civic_commission` | `portrait_BRI_independence_wave_coastal_commandant` | `portrait_BRI_independence_wave_coastal_commandant_small` | Installed |
| RHI | `portrait_RHI_independence_wave_provisional_directorate` | `portrait_RHI_independence_wave_river_commandant` | `portrait_RHI_independence_wave_river_commandant_small` | Installed |
| SCO | `portrait_SCO_independence_wave_civic_convention` | `portrait_SCO_independence_wave_territorial_commandant` | `portrait_SCO_independence_wave_territorial_commandant_small` | Installed |
| WLS | `portrait_WLS_independence_wave_national_council` | `portrait_WLS_independence_wave_mountain_commandant` | `portrait_WLS_independence_wave_mountain_commandant_small` | Installed |

The twenty large textures and ten small textures retain their existing runtime filenames under `gfx/leaders/006_independence_wave/`. The twenty-four textures owned by admitted packages retain their existing sprite and character consumers without `.gfx`, character, focus, decision, event, or localisation edits from this package. The six ACX/AEX textures remain readiness-pool art and deliberately have no live sprite or character consumer until their exact package admission gates pass.

## Production chain and retained evidence

1. `prompts/` contains one complete generation prompt for every large master. Each prompt explicitly requires a male subject, the regional role, period clothing, restrained background, and matte HOI4 painted treatment.
2. `raw_outputs/` contains all twenty untouched built-in ImageGen results. `hashes/raw_master_sha256.sha256` records twenty distinct hashes, confirming twenty independent retained masters.
3. `processed_png/` contains the deterministic 156x210 large candidates.
4. `small_processed_png/` contains the ten 65x67 commander-small cards derived from the matching new raw commander master. The canonical v3 frame and paper overlay pair is recorded in each small metadata file.
5. `metadata/` and `review_sheets/` contain the ACX/AEX/AFX/AGX/AJX processing records and individual review sheets. `tranche_bay_bri_rhi_sco_wls/metadata/` and `tranche_bay_bri_rhi_sco_wls/review_sheets/` contain the corresponding BAY/BRI/RHI/SCO/WLS records.
6. All thirty metadata records pin portrait processor version `4.3` and SHA-256 `c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`.
7. `_tooling/v4_3_frozen_inputs/` retains the exact seventeen-file processor, dossier-overlay, prompt, and canonical-reference bundle used for the commander-small renders. The files are exact Git blob bytes from commit `6729ad0cd74e0ed294a0b603a0eb677a0533099c`; every processor and embedded small-metadata path resolves inside this immutable evidence bundle. `hashes/frozen_v4_3_inputs_sha256.sha256` records it.
8. `dds_decoded_png/` and `small_dds_decoded_png/` contain decodes of the actual installed runtime DDS files. Every decode is pixel-identical to its matching processed PNG, including alpha.
9. `hashes/runtime_sha256_inventory.sha256` records the twenty large runtime textures, ten small runtime textures, and two protected historical textures.
10. `validation/full_package_validation_report.json` records counts, DDS header and byte-length checks, pixel-equivalence checks, metadata pins, and protected hashes. `validation/frozen_v4_3_input_resolution.md` records the post-audit provenance-path repair.
11. `tranche_bay_bri_rhi_sco_wls/manifest.md` and `tranche_bay_bri_rhi_sco_wls/validation/validation_report.json` retain detailed provenance, per-file hashes, overlay pins, face-placement evidence, and shared-file guards for the second production tranche.
12. `_tooling/build_nwe_portraits.py` retains the ACX/AEX/AFX/AGX/AJX production geometry and a processor-free `merge-evidence` stage for complete-package DDS decoding, pixel comparison, and contact-sheet assembly.

## Merged visual evidence

- `contact_sheets/all_runtime_large_156x210_contact_sheet.png`: all twenty installed large DDS decodes.
- `contact_sheets/all_runtime_large_canonical_comparison.png`: all twenty installed large decodes together with canonical vanilla and immutable approved Event 006 comparisons.
- `contact_sheets/all_runtime_commander_small_65x67_contact_sheet.png`: all ten installed commander-small DDS decodes with canonical vanilla dossier comparisons.
- `validation/full_package_visual_review.md`: final acceptance record for male presentation, identity distinction, HOI4 painted treatment, period clothing, restrained backgrounds, and target-size legibility.

## Protected historical portraits

The following runtime DDS files remain byte-identical to their approved state:

- `portrait_BAY_rupprecht_of_bavaria.dds`: `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`
- `portrait_RHI_josef_friedrich_matthes.dds`: `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`

The package builder checks both hashes before and after every supported production or merged-evidence stage.

## Simplifications, omissions, and blockers

None. All twenty non-approved large portraits and all ten matching commander-small textures were regenerated, reviewed, validated, and installed. Both approved historical portraits remain byte-identical, and no advisor-icon work entered the package.
