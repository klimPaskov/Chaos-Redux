# Event 014 European Warlord Portrait Candidate Handoff

Disposition: implemented for the bounded Europe source, native PNG, DDS, and runtime-install tranche. Parent final approval is recorded and the eight existing Europe DDS paths now contain the approved bytes. The full 56-portrait requirement is not complete because the other 48 region-slot portraits remain queued; this is not full-event or live-game acceptance.

## Authorization and selected route

The user authorized full implementation of accepted Event 014 with no simplifications. The accepted Event 014 specification and parent brief classify CBA-CBH as invented Cannibal Warlord identities, not grounded real offices or people, so the accepted source-mode gate routes them through built-in native ImageGen. The user's latest instruction authorized only the eight existing Europe DDS paths after the parent recorded final approval.

The accepted design is the 56-entry generic warlord portrait matrix in `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_10_assets_animation_and_localisation.md` lines 116-155 and the matching acceptance criteria in `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_12_acceptance_criteria.md` lines 73 and 193.

On 2026-10-03 the parent reviewed the seven other full-resolution masters and native 156x210 contact sheet, plus the CBA-v02 master, approved the source art and framing, and selected CBA-v02 for the skull-and-blood action. The parent then reviewed the decoded eight-DDS native contact sheet and verified exact selected PNG/DDS RGBA equality, opacity, native dimensions, and distinct decoded buffers for all eight. This parent selection is within the user's authorized scope, not a new explicit user art decision. The approval record is `docs/plans/014_cannibalism_plans/evidence/2026-10-03_europe_portrait_parent_review.json`.

## Produced candidates

Eight selected opaque RGB source PNGs, eight processed 156x210 PNGs, and eight approved candidate DDS files are retained under `docs/assets/014_cannibalism/portrait_finals_2026-10-03/europe/`; exact copies of those DDS files are installed at the existing Europe runtime paths.

| Slot | Distinct approved behavior | Selected native source | Processed PNG | Candidate DDS |
|---|---|---|---|---|
| CBA | Licks the blood mark on a held human skull | `source_png/leader_CBA_warlord_europe_candidate_v02.png` | `processed_png/leader_CBA_warlord_europe_v02_156x210.png` | `candidate_dds/leader_CBA_warlord_europe.dds` |
| CBB | Gnaws a stripped bloodied bone | `source_png/leader_CBB_warlord_europe_source.png` | `processed_png/leader_CBB_warlord_europe_156x210.png` | `candidate_dds/leader_CBB_warlord_europe.dds` |
| CBC | Bites a bloodied glove | `source_png/leader_CBC_warlord_source.png` | `processed_png/leader_CBC_warlord_156x210.png` | `candidate_dds/leader_CBC_warlord.dds` |
| CBD | Laughs through a scarred damaged jaw | `source_png/leader_CBD_warlord_europe_source.png` | `processed_png/leader_CBD_warlord_europe_156x210.png` | `candidate_dds/leader_CBD_warlord_europe.dds` |
| CBE | Grips a stained ration cleaver | `source_png/leader_CBE_warlord_source.png` | `processed_png/leader_CBE_warlord_156x210.png` | `candidate_dds/leader_CBE_warlord.dds` |
| CBF | Clutches stolen blank dog tags | `source_png/leader_CBF_warlord_source.png` | `processed_png/leader_CBF_warlord_156x210.png` | `candidate_dds/leader_CBF_warlord.dds` |
| CBG | Drags a torn ration sack across his shoulder | `source_png/leader_CBG_warlord_europe_source.png` | `processed_png/leader_CBG_warlord_europe_156x210.png` | `candidate_dds/leader_CBG_warlord_europe.dds` |
| CBH | Leans toward the viewer holding a broken burial shovel shaft | `source_png/leader_CBH_warlord_source.png` | `processed_png/leader_CBH_warlord_156x210.png` | `candidate_dds/leader_CBH_warlord.dds` |

The producer inspected all eight selected source masters at full resolution and every processed PNG at 156x210. Faces, poses, clothing silhouettes, props, crops, and restrained painted backgrounds read as distinct across the contact sheet; all assigned behaviors remain legible at native size. The parent-approved style and framing verdict is pass for this bounded set.

The selected native-size and 4x nearest-neighbour PNG sheets are `review/europe_native_4x2_contact_sheet_v03.png` and `review/europe_nearest4_4x2_contact_sheet_v03.png`. The DDS-decoded contact sheets are `review/europe_dds_decoded_native_4x2_contact_sheet.png` and `review/europe_dds_decoded_nearest4_4x2_contact_sheet.png`.

## CBA ImageGen lineage and failure record

The first CBA native ImageGen call returned HTTP 400, `image_generation_user_error`, `moderation_blocked`, at the output stage with category `violence` and request ID `be00ff3e-d7eb-4fdc-88db-b821139a4262`. Its exact prompt and response are retained in `evidence/prompts.json` and `evidence/imagegen_call_log.json`.

A narrowed native prompt then generated CBA-v02 with the skull and tongue-to-bloodstained-human-skull action. The parent reviewed and selected v02 for crop and contact-sheet use.

A subsequent focused native edit generated CBA-v03 with a clearer small mark. It is preserved at `source_png/leader_CBA_warlord_europe_source.png` with its processed alternate, but is unselected and excluded from the chosen PNG sheet and DDS output.

The first rejected call did not leave CBA blocked, and no required CBA behavior was omitted. No CLI/API image generation or other image-generation fallback was used.

## Provenance, reference rights, and framing gate

The selected portraits are original native ImageGen outputs. No Internet photographs, user-supplied raster sources, or real-person identities were used.

The installed-vanilla leader contact sheet and three individual 156x210 samples were inspected as style and framing references only. No reference image was attached to generation calls, no source face was copied, and proprietary vanilla artwork was not included in the candidate files.

The selected outputs are opaque full-canvas painted leader busts. No fake transparency or background-removal step was used. Rights status for references and generated outputs is recorded separately in `docs/assets/014_cannibalism/portrait_finals_2026-10-03/europe/manifest.md` and `evidence/output_inventory.json`.

## PNG and DDS checks

Every selected processed PNG is RGB 156x210, and all eight decoded processed-pixel buffers are unique. Exact source dimensions, crop boxes, source hashes, crop hashes, and processed PNG hashes are recorded in `evidence/png_review_audit.json`, `evidence/*_crop.json`, and `evidence/output_inventory.json`.

The required `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` produced eight 156x210 uncompressed BGRA32 candidates at 131168 bytes each. Its built-in FFmpeg BGRA32 fallback was selected because `texconv` was not present on PATH.

All eight DDS headers have a 128-byte header, the expected BGRA masks and texture caps, one image level with no mip chain, and alpha fixed at 255. DDS decoding exactly matches each selected processed PNG, the eight decoded DDS pixel buffers are unique, and each existing runtime DDS hash is unchanged from the pre-conversion baseline.

Candidate DDS SHA-256 values and full header/round-trip evidence are in `evidence/dds_roundtrip_audit.json` and the manifest's DDS table. The combined dimensions and hash inventory is `evidence/output_inventory.json`.

## Runtime crosswalk and replacement state

The exact existing base-alias and Europe sprite registrations, GFX line numbers, current runtime DDS paths, and pre-conversion hashes are recorded in `docs/assets/014_cannibalism/portrait_finals_2026-10-03/europe/manifest.md` and `evidence/output_inventory.json`.

Exactly the eight parent-approved Europe DDS files were copied into their existing runtime paths. No `.gfx` or character-definition changes were made. A bounded search found no literal CBA-CBH portrait sprite references in `common/characters/` or `history/countries/`; the Event 014 character file's literal portrait reference is Hannibal's separate `GFX_portrait_CBL_hannibal` at line 14.

The eight candidate DDS files remain in `candidate_dds/` as provenance copies, and their SHA-256 values match the installed runtime bytes. The eight old runtime DDS files are backed up in `evidence/runtime_before/` with hashes matching the recorded baseline.

All other 52 DDS files in `gfx/leaders/014_cannibalism/` match the pre-install snapshot, including the 48 non-Europe warlord portraits and canonical `hannibal.dds`, `hannibal_wendigo.dds`, and both animated sheets. `interface/014_cannibalism.gfx` and `common/characters/014_cannibalism_characters.txt` also match their pre-install hashes. These checks are recorded in `evidence/runtime_install_receipt.json` and `evidence/runtime_preinstall_snapshot.json`.

No HOI4 process was launched and no live-game consumer check was performed.

## Changed files and evidence

The writes for this tranche are limited to the eight Europe runtime DDS paths, their eight exact pre-install backups, the Europe candidate workspace and evidence, and this handoff. The workspace contains selected and alternate source PNGs, processed/crop PNGs, candidate DDS files, exact prompts, ImageGen call and CBA lineage records, processing and QA scripts, native and 4x review sheets, and machine-readable crop, PNG, DDS, and output-inventory reports.

The eight Europe portraits are installed. The other 48 regional portraits remain queued across Asia, Africa, Middle East, North America, South America, and Oceania; the full Event 014 portrait goal is not complete.

No simplification was made. No RunPod, Meshy, Blender, HOI4 launch, unrelated gameplay edit, localisation edit, character identity edit, or runtime GFX edit occurred. No commit was made.
