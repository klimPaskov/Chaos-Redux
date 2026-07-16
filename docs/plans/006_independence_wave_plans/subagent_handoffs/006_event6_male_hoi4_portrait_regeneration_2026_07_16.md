# Event 6 male HOI4 portrait regeneration handoff

Date: 2026-07-16

Status: complete; no further portrait writes are pending.

## Outcome

Every non-approved large Event 006 portrait was regenerated as an independent fictional male subject in a restrained painted Hearts of Iron IV style. The final runtime package contains twenty regenerated 156x210 large portraits and ten matching 65x67 commander-small dossier textures derived from the corresponding new commander masters.

The two user-approved historical runtime portraits remain byte-identical:

- `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`: `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`
- `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`: `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`

No advisor icon was created, edited, installed, renamed, or wired.

## Installed runtime inventory

| Region | Civil/institutional large | Commander large | Commander-small |
| --- | --- | --- | --- |
| ACX | `portrait_ACX_cornish_port_and_mines_committee.dds` | `portrait_ACX_cornish_coastal_commander.dds` | `portrait_ACX_cornish_coastal_commander_small.dds` |
| AEX | `portrait_AEX_flemish_civil_industrial_board.dds` | `portrait_AEX_flemish_industrial_security_commander.dds` | `portrait_AEX_flemish_industrial_security_commander_small.dds` |
| AFX | `portrait_AFX_walloon_provisional_assembly.dds` | `portrait_AFX_walloon_reserve_commander.dds` | `portrait_AFX_walloon_reserve_commander_small.dds` |
| AGX | `portrait_AGX_friesland_coastal_council.dds` | `portrait_AGX_friesland_coastal_commander.dds` | `portrait_AGX_friesland_coastal_commander_small.dds` |
| AJX | `portrait_AJX_saar_municipal_neutral_commission.dds` | `portrait_AJX_saar_industrial_security_commissioner.dds` | `portrait_AJX_saar_industrial_security_commissioner_small.dds` |
| BAY | `portrait_BAY_independence_wave_state_council.dds` | `portrait_BAY_independence_wave_mountain_commandant.dds` | `portrait_BAY_independence_wave_mountain_commandant_small.dds` |
| BRI | `portrait_BRI_independence_wave_civic_commission.dds` | `portrait_BRI_independence_wave_coastal_commandant.dds` | `portrait_BRI_independence_wave_coastal_commandant_small.dds` |
| RHI | `portrait_RHI_independence_wave_provisional_directorate.dds` | `portrait_RHI_independence_wave_river_commandant.dds` | `portrait_RHI_independence_wave_river_commandant_small.dds` |
| SCO | `portrait_SCO_independence_wave_civic_convention.dds` | `portrait_SCO_independence_wave_territorial_commandant.dds` | `portrait_SCO_independence_wave_territorial_commandant_small.dds` |
| WLS | `portrait_WLS_independence_wave_national_council.dds` | `portrait_WLS_independence_wave_mountain_commandant.dds` | `portrait_WLS_independence_wave_mountain_commandant_small.dds` |

All files live under `gfx/leaders/006_independence_wave/`. Existing filenames were retained, so no `.gfx`, character, focus, decision, event, localisation, or other gameplay wiring edit was required for this portrait pass.

## Evidence package

Source of truth:

`docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/`

Key evidence:

- `manifest.md`: complete package inventory, production chain, protected assets, and scope boundaries.
- `prompts/`: twenty frozen male/role/style prompts.
- `raw_outputs/`: twenty retained independent built-in ImageGen masters.
- `processed_png/`: twenty target-size large PNGs.
- `small_processed_png/`: ten matching-master commander dossiers.
- `dds_decoded_png/`: twenty actual runtime large DDS decodes.
- `small_dds_decoded_png/`: ten actual runtime small DDS decodes.
- `metadata/`, `review_sheets/`, and `tranche_bay_bri_rhi_sco_wls/`: all thirty metadata records and all thirty individual review sheets.
- `hashes/raw_master_sha256.sha256`: twenty unique raw-master hashes.
- `hashes/runtime_sha256_inventory.sha256`: hashes for all thirty regenerated runtime files and both immutable historical files.
- `validation/full_package_validation_report.json`: complete-machine validation summary.
- `validation/full_package_visual_review.md`: final visual acceptance record.
- `tranche_bay_bri_rhi_sco_wls/manifest.md` and `tranche_bay_bri_rhi_sco_wls/validation/validation_report.json`: detailed second-tranche per-file provenance, processor/overlay pins, face placement, alpha, and guard evidence.

Merged decisive contact sheets:

- `contact_sheets/all_runtime_large_156x210_contact_sheet.png`
- `contact_sheets/all_runtime_large_canonical_comparison.png`
- `contact_sheets/all_runtime_commander_small_65x67_contact_sheet.png`

## Generation and processing notes

- Source mode was the built-in ImageGen tool. Each retained large portrait has its own independent generated master and prompt.
- All twenty selected subjects are adult men. Institutional offices use one male delegate rather than a group image.
- One RHI river-commandant attempt was rejected during output moderation and produced no image. The unchanged prompt was retried once; no fallback, substitute source, or weaker design was used.
- All thirty retained processing metadata records pin portrait processor version `4.3` and processor SHA-256 `c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`.
- The commander-small bundle additionally pins overlay manifest `be1ff82d3f460ca1e0572ff3cb23853fdd87d2a0a8444f20cdad6565cacd2d2f`, frame source/overlay `77857264f8f6e36c75c675969f73e5ba5ee936f38599c6d843e2e07c527c0740` / `950596dd88da0b58861af9e58cacdaa80b2e6308af9168dd98ad390ae42aea79`, and paper source/overlay `5d5f5c76e0a290c848cc71e8ff8f102a87e47227d32c9902350bc7f1eb00d491` / `e5db0602b4b5d82ba148552bfa2a6c7b6e00c6a91137de2b3baec404535210a0`. The exact seventeen-file v4.3 processor/input set is retained package-locally as Git blob bytes from commit `6729ad0cd74e0ed294a0b603a0eb677a0533099c`; all metadata paths resolve there.
- The final merged `merge-evidence` stage is processor-free. It only decodes installed DDS files, performs pixel comparisons, and assembles contact sheets.
- The unrelated working-tree v4.4 processor change was neither invoked nor edited by the merged evidence pass.

## Validation evidence

- Twenty raw masters exist and have twenty unique SHA-256 values.
- All twenty installed large DDS files are exactly 156x210, legacy uncompressed BGRA32, and 131,168 bytes.
- All ten installed commander-small DDS files are exactly 65x67, legacy uncompressed BGRA32, and 17,548 bytes.
- Every installed large and small DDS decodes pixel-identically to its retained processed PNG.
- Every saved decode is pixel-identical to the installed DDS it represents.
- All ten small textures have alpha extrema 0/255 and transparent dossier corners.
- All thirty generated runtime hashes are distinct.
- Both protected historical hashes match their approved values after the complete merged pass.
- The merged visual review accepted male presentation, distinct identities, painterly HOI4 treatment, period clothing, restrained backgrounds, target-size legibility, and canonical commander-small dossier treatment.

## Files changed by the portrait task

- Thirty existing runtime DDS files under `gfx/leaders/006_independence_wave/` were replaced in place: the twenty non-approved large portraits and ten corresponding `_small` commander textures listed above.
- The complete evidence package was added under `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/`.
- This handoff file was added.

No portrait-task files were staged or committed.

## Worktree boundary

This handoff covers portrait work only. Before the portrait task preempted earlier work, this agent had begun unrelated Mediterranean package edits in the following files; they remain paused and incomplete and are not part of this completion claim:

- `common/script_constants/006_independence_wave_mediterranean_constants.txt`
- `common/characters/006_independence_wave_mediterranean_characters.txt`
- `common/ideas/006_independence_wave_mediterranean_ideas.txt`
- `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`
- `history/countries/ARX - Event 006 Country Shell.txt`
- `history/countries/ASX - Event 006 Country Shell.txt`

They were not resumed after the portrait directive.

## Skills used

- `chaos-redux-event-assets`
- `imagegen`

The offline Portrait Modding and Graphical Asset Modding wiki references, required core wiki pages, canonical vanilla portrait catalog, and retained vanilla leader/commander/advisor comparison assets were consulted before production.

## Simplifications, omissions, and blockers

None for the portrait task. All twenty non-approved large portraits and all ten matching commander-small textures were regenerated, installed, evidenced, and validated. The two approved historical portraits remain byte-identical, and no advisor-icon work entered the package.
