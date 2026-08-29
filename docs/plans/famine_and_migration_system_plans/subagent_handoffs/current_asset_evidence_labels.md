# Current Asset Evidence Label Refresh

Status: complete.

The eight stale-label evidence sheets were regenerated from the current split `famine_*` and `migration_*` source, processed, and DDS-roundtrip PNG inputs. Runtime DDS files, `.gfx` files, gameplay files, manifests, and the category/mapmode evidence sheets were not changed.

## Regenerated files

- `docs/assets/famine_and_migration_system/contact_sheets/achievements_source_processed_roundtrip.png` — 1200x1520 RGB; current achievement source, processed, and decoded-roundtrip triplets with `famine_*` or `migration_*` state labels.
- `docs/assets/famine_and_migration_system/report_art/contact_sheets/report_art_contact_sheet.png` — 1080x870 RGB; current processed 210x176 report art in the existing three-column layout with split report names.
- `docs/assets/famine_and_migration_system/contact_sheets/state_modifiers_source_processed_roundtrip.png` — 1200x570 RGB; current state-modifier source, processed, and decoded-roundtrip triplets with split names.
- `docs/assets/famine_and_migration_system/contact_sheets/decisions_source_processed_roundtrip.png` — 1200x760 RGB; current decision source, processed, and decoded-roundtrip triplets with split names.
- `docs/assets/famine_and_migration_system/contact_sheets/state_modifiers_processed_4x.png` — 2208x1686 RGB; current 32x32 processed state modifiers enlarged with nearest-neighbour 4x previews and split labels.
- `docs/assets/famine_and_migration_system/contact_sheets/decisions_processed_4x.png` — 2208x1686 RGB; current 32x32 processed decisions enlarged with nearest-neighbour 4x previews and split labels.
- `docs/assets/famine_and_migration_system/contact_sheets/deaths/native_4x.png` — 520x230 RGBA; current native source death icons with alpha evidence and split labels.
- `docs/assets/famine_and_migration_system/contact_sheets/deaths/dds_roundtrip_4x.png` — 440x210 RGBA; current decoded DDS death icons with roundtrip evidence and split labels.

## Method and evidence

The source/processed/roundtrip sheets retain the prior card order, three-way comparison layout, checkerboard transparency treatment, native-size dimensions, and footer evidence text while replacing the retired combined labels.

The report sheet retains the prior 320x268 card presentation, 210x176 dimensions, period-art content, and checkerboard margins while reading current processed report-art inputs.

The 4x sheets read current processed PNGs, preserve their solid review panels, and use nearest-neighbour enlargement so the 32x32 evidence remains visibly pixel-faithful.

The death sheets read the current source and DDS-roundtrip PNGs, preserve the bordered dark review cards, and retain the alpha and DDS roundtrip captions.

All eight outputs were visually inspected after regeneration. The visible labels now use `famine_*`, `migration_*`, `report_event_famine_*`, or `report_event_migration_*` names, and no `fm_*` or `famine_migration_*` label remains in the refreshed sheets.

The authoritative asset manifest currently has 50 rows, all source, processed, and final DDS paths exist, and it contains no `fm_*` or `famine_migration_*` identifiers. No concrete manifest mismatch was found.

## Output hashes

| File | SHA-256 |
| --- | --- |
| `contact_sheets/achievements_source_processed_roundtrip.png` | `4be1578f4e595c43cfbe82883f269079bd4826120fa184310db30bf31920d0d9` |
| `report_art/contact_sheets/report_art_contact_sheet.png` | `bbf9e8a58933fcfac7d6f68551379972898712e026ab3c630adc053617cdf195` |
| `contact_sheets/state_modifiers_source_processed_roundtrip.png` | `76809dda7f04e4cccbb649704d1e26e9d52160e5f2b1826b306aad501ab05f07` |
| `contact_sheets/decisions_source_processed_roundtrip.png` | `bdc13bf780bd73fef5f3ef901763497af182a99a79cc24fa66548a654a56c0f8` |
| `contact_sheets/state_modifiers_processed_4x.png` | `4bf7504d35f0548789480d547daa16b44872c801de9a32bed59bfc3b03cd9256` |
| `contact_sheets/decisions_processed_4x.png` | `adc54ec279370b0c8981c9d6533324647027e448231a83e348c26b201edbe1ea` |
| `contact_sheets/deaths/native_4x.png` | `4a4513eb204373b540a485744afdc5f02d1afbc246f788ab4e437f5b84f4a233` |
| `contact_sheets/deaths/dds_roundtrip_4x.png` | `bcc2c7635359d609db62b8bcb399893d09bd36bc0f102389372caafdd32bb7f4` |

No blocker or needs-user-review item remains for this evidence-label cleanup.
