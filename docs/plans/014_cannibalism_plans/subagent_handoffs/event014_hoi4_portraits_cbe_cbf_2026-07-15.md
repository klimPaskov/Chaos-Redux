# Event 014 CBE/CBF HOI4 Portrait Repaint Handoff

Date: 2026-07-15
Owner: `event014_portraits_cbe_cbf_hoi4`
Scope: the 14 static CBE and CBF warlord leader portraits only. No gameplay, interface, localisation, shared manifest, aggregate hash, or prompt-matrix files were edited.

## Delivered package

All fourteen portraits were regenerated as original fictional male warlords with the requested prop action preserved in the final 156x210 leader crop. The masters use the classic HOI4 country-leader visual language requested for this pass: opaque oil/gouache handling, simplified facial planes, firm painted edges, low photographic microdetail, muted olive/umber/gray colour, and quiet brushed backdrops.

ImageGen used these three vanilla-style references for style, framing, value range, and paint finish only:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ire_eamon_de_valera.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`

No referenced identity, face, clothing, pose, or insignia was copied.

## Portrait matrix

| Stem | Required action preserved in source and leader crop |
| --- | --- |
| `leader_CBE_warlord` | Licks the brow of a weathered skull held against his cheek. |
| `leader_CBE_warlord_africa` | Bites a cracked brass compass and twists the exposed needle with a finger. |
| `leader_CBE_warlord_asia` | Chews the cracked corner of an old leather map case. |
| `leader_CBE_warlord_middle_east` | Threads a plain tooth-and-bone charm onto wire at his open collar. |
| `leader_CBE_warlord_north_america` | Presses a secular carved feast mask to his cheek and peers through its eyehole. |
| `leader_CBE_warlord_south_america` | Holds one conventional tarnished spoon by its handle between filed teeth and taps the single bowl. |
| `leader_CBE_warlord_oceania` | Nibbles the blackened corner of a scorched ration biscuit while staring at the viewer. |
| `leader_CBF_warlord` | Kisses the circular face of a detached cracked 1930s gas-mask filter. |
| `leader_CBF_warlord_africa` | Balances a blunt rounded table knife across an extended tongue. |
| `leader_CBF_warlord_asia` | Inhales from the open cuff of an old empty leather field glove. |
| `leader_CBF_warlord_middle_east` | Manically plays a crude harmonica folded from a flattened ration tin. |
| `leader_CBF_warlord_north_america` | Offers a plain tooth charm to a rat perched on his shoulder. |
| `leader_CBF_warlord_south_america` | Uses a weathered lower jawbone relic as a telephone handset between ear and mouth. |
| `leader_CBF_warlord_oceania` | Holds a cracked glass false eye beside his real eye for comparison. |

Each face, cranial silhouette, expression, build, garment arrangement, and prop interaction is distinct. None uses a real-person identity, modern equipment, prison imagery, graphic injury, or living Indigenous sacred motifs.

## Files and locations

- Approved ImageGen masters: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/source_png/leader_CBE_warlord*_source.png` and `leader_CBF_warlord*_source.png`
- Exact accepted prompts: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/prompts/generated/leader_CBE_warlord*.txt` and `leader_CBF_warlord*.txt`
- Finished leader PNGs: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/processed_png/leader_CBE_warlord*.png` and `leader_CBF_warlord*.png`
- Processor metadata: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/metadata/leader_CBE_warlord*.json` and `leader_CBF_warlord*.json`
- Per-portrait review sheets: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/contact_sheets/reviews/leader_CBE_warlord*_review.png` and `leader_CBF_warlord*_review.png`
- Combined visual review: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/contact_sheets/cbe_cbf_hoi4_repaint_contact_sheet.png`
- Final game DDS files: `gfx/leaders/014_cannibalism/leader_CBE_warlord*.dds` and `leader_CBF_warlord*.dds`

## Deterministic finishing

All portraits were processed with `.tools/process_hoi4_portrait.py leader`, `--source-kind fictional`, the leader reference directory above, an explicit crop, a metadata JSON, and a per-portrait review sheet.

- Thirteen 1080x1456 masters use crop `0 1 1080 1455`.
- `leader_CBF_warlord_south_america_source.png` is 1079x1457 and uses crop `0 2 1079 1455`.
- Every processed PNG is 156x210.
- Every DDS was produced with `.tools/convert_to_dds.py --width 156 --height 210`.

The generated metadata retains the processor's machine status `candidate_requires_visual_approval`. Manual visual approval is recorded here: every source master was inspected at generation time, and all fourteen processed crops were inspected together in the combined contact sheet. The requested gestures remain readable after finishing, facial silhouettes remain unique, and the set is visually coherent with the three style references.

## Wiring and validation evidence

Existing sprite definitions in `interface/014_cannibalism.gfx` lines 199-214 already point to the exact fourteen DDS filenames, including the default files reused for each European sprite. No interface edit was required.

- 14/14 source files, processed PNGs, metadata files, prompt files, review sheets, and DDS files are present.
- Source SHA-256 hashes are unique across all fourteen masters; processed PNG SHA-256 hashes are also unique across all fourteen finals.
- All processed PNGs report 156x210.
- All DDS headers report 156x210 and the expected `DDS ` magic; each file is 131,168 bytes.
- Saved prompt files were compared against the accepted ImageGen call prompts from the generation session.
- The combined contact sheet was inspected at original resolution after processing.

Shared `manifest.md`, `hashes.sha256`, `source_generation_metadata.md`, `validation.md`, and `prompts/prompt_matrix.md` were intentionally left untouched under the parent-granted ownership boundary. The parent can refresh aggregate records after all portrait batches are assembled.

## Simplifications, omissions, and blockers

None within the assigned fourteen-portrait scope. No fallback art, transform-only substitute, placeholder, missing action, missing regional variant, or unwired filename was accepted. No commit was created, as requested.
