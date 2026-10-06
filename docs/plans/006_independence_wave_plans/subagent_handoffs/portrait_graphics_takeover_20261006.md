# Event 006 portrait graphics takeover

Date: 2026-10-06.

Disposition: `implemented` for the twelve-source audit, four source-placeholder DDS corrections, four new durable portrait source packages, and this handoff; `blocked` for cleaner-source repairs to Shaban Polluzha and Gayaz Ishaki; `pending` for user-supplied HOI4-style finals.

The task's grounded source-mode gate remains unchanged. All twelve identities remain attributed `source_placeholder` portraits. `styled_final=not_requested` and `replacement_pending=false`; the user alone creates and supplies any RunPod final after an explicit request. No real-person repaint, fictional substitute, generic face, ImageGen portrait, or RunPod operation was used.

## Files changed

| Surface | Changes |
| --- | --- |
| Runtime DDS | Re-exported `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds`, `portrait_ASY_independence_wave_provisional_national_council.dds`, `portrait_ASX_independence_wave_vincenzo_di_benedetto.dds`, and `portrait_SCO_independence_wave_civic_convention.dds` from their attributed source-placeholder PNGs through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. |
| Existing portrait contracts | Updated the BRI Henri-Leon Devin and SCO R. B. Cunninghame Graham `.txt` provenance contracts to record the installed source-placeholder state, source rights terms, and runtime mapping. |
| New durable source packages | Added complete original/crop/crop-JSON/156x210-PNG/provenance packages for KOS Shaban Polluzha, ASY Gallo Shabo, ARX Luigi Mella di Sant'Elia, and ASX Vincenzo Di Benedetto under `docs/assets/portraits/006_independence_wave/portrait_graphics_takeover_20261006/`. Each includes nearest-neighbor 4x review output. |
| Evidence | Added the twelve-row source/runtime audit JSON, before and after native-plus-4x runtime contact sheets, the manifest, and the user-output candidate audit/contact sheets in the same portrait evidence folder. |
| Handoff | Added this file at `docs/plans/006_independence_wave_plans/subagent_handoffs/portrait_graphics_takeover_20261006.md`. |

No `.gfx`, character, gameplay, localisation, event, focus, decision, country, or shared UI file changed. The existing sprite names, texture paths, and character portrait references were re-read immediately before the DDS writes and remain unchanged.

Version-control note: root `.gitignore:80` ignores all of `docs/assets/`, so the source archives, contact sheets, audit JSON, manifest, and updated BRI/SCO provenance contracts remain in the shared worktree but do not appear in normal `git status`. I did not force-stage them; the parent can choose whether to stage exact evidence paths. The four DDS changes and this handoff are visible to Git.

## Runtime and source evidence

All twelve runtime DDS files are 156x210, 131,168 bytes, uncompressed 32-bit BGRA textures with opaque alpha. `docs/assets/portraits/006_independence_wave/portrait_graphics_takeover_20261006/source_runtime_audit_20261006.json` records each exact runtime path and SHA-256, selected source PNG SHA-256, source original SHA-256, lossless crop SHA-256, crop rectangle, decoded-pixel hashes, and the per-pixel runtime-to-source comparison. All twelve decoded runtime DDS images equal their selected 156x210 source-placeholder PNGs pixel-for-pixel.

The four corrected runtime outputs now match these source-placeholder PNG hashes exactly: BRI `1397ef6790efc600809af2215f4b2b3364e67eddc9749d8c61b37655963952fc` to DDS `01baa0e04b1ed2a4d31422968ce60cdde9c1e1bc5286bfe03df02a608e1f17c5`; ASY Gallo Shabo `0b0d30f6e485fe523b01812dc414c1e5c2652b730ff5e9e4aabd5bb5d8dd3e6a` to DDS `22aa0a83a4fcaf918e90acf2741cb45feaa1061c741a85db58af7ceb204cf530`; ASX Vincenzo Di Benedetto `6869d1ca9b5201b26ac41cfc760a0f7e0a7cc5aba6b9fb8f1c377a8a5cb1330e` to DDS `c98c00633be19430065076fc41b29e2108ea382388c4f87f5f498c418156362e`; and SCO Cunninghame Graham `d1a9598fae497ba6cc85d3a2dab0129dcab18a55913decf80725fc56809fb82b` to DDS `930b2f7278635b7de3a21349afeb04e502327165a79c7313e1ec5320592c4e94`.

The other eight runtime DDS files already matched their selected source PNGs and were left byte-for-byte unchanged: Shaban Polluzha, the four CHU identities, Ignatius Afram I Barsoum, Luigi Mella di Sant'Elia, and Hasan dan Mu'azu.

The complete identity, attribution, rights, source date, crop/framing verdict, and replacement-state crosswalk is in `docs/assets/portraits/006_independence_wave/portrait_graphics_takeover_20261006/manifest.md`. The original/crop/processed PNG contracts remain co-located with their subject packages under the durable portrait archive.

## Identity, attribution, and rights findings

D13's accepted CHU identities were preserved: Gayaz Ishaki for the federal presidium, Mirsaid Sultan-Galiev for the Middle Volga Congress, Karim Tinchurin for the Bolgar civic presidium, and Luka Spasov for the river security directorate. D13's ASY identities were preserved: existing Gallo Shabo for the provisional national council and Ignatius Afram I Barsoum for the concordat council. The remaining targets use their exact named source identities: Shaban Polluzha, Henri-Leon Devin, Luigi Arborio Mella di Sant'Elia, Vincenzo Di Benedetto, Robert Bontine Cunninghame Graham, and Hasan dan Mu'azu Ahmadu.

The source packages retain their attributed rights bases: Commons Public Domain Mark for Polluzha; PD-old-70-1923 for the Ishaki book plate and Sultan-Galiev image; the Commons public-domain record for Tinchurin; PD-Russia-1996 for Spasov; CC BY-SA 4.0 for the Aramean Archive Gallo Shabo source; PD-Syria for Barsoum; the Gallica/BnF Agence Rol Devin source; CC BY 3.0 IT and senato.it attribution for Mella; PD Italy and PD-1996/US for Di Benedetto; the Rijksmuseum public-domain record for Cunninghame Graham; and the Commons Public Domain Mark for Hasan dan Mu'azu's 1934 London photograph.

For the BRI portrait, the source dossier records the historic photo as public domain in France and the United States. BnF's official policy allows non-commercial reuse with source acknowledgement and requires a separate licence for commercial use; this source is recorded for the free non-commercial mod only. Commercial reuse remains uncleared. The existing contract cites [BnF reuse terms](https://www.bnf.fr/en/reproduction-documents).

The SCO source is the Rijksmuseum photomechanical print RP-F-2001-7-67-30, dated circa 1881 to in or before 1891 and explicitly marked public domain by the museum. This date is an age-context caveat for the 1936 leader image. The [Rijksmuseum record](https://www.rijksmuseum.nl/en/collection/object/Portret-van-Robert-Bontine-Cunninghame-Graham--58d50c7b9bd272d04b216d7494101918) names the subject, maker, date range, technique, and public-domain status.

The Mella source is a 153x193 Senate GIF and is low resolution. Its exact crop was made 143x193 to fit the 156:210 leader ratio without distorting the source. The source dossier records CC BY 3.0 IT and requires credit to senato.it; it also notes the image date is unknown and only bounded as before 1955. The existing character role remains the Sardinian crown consultative council.

## User-supplied final candidates

The manifest-declared user output folder was inspected at `C:/Users/klimp/Documents/ComfyUI Workflows/HOI4/hoi4_portraits_output/output/156x210/iw/`. It contains eight CHU PNG candidates and two Shaban Polluzha candidates for this target set; the exact dimensions, hashes, embedded prompt/workflow fields, and visual sheets are recorded in `user_candidate_audit_20261006.json` and `user_candidates_*_native_4x.png`.

The prior Event 006 consumer audit records no provider/job receipt for this output batch and keeps the CHU images as candidates only. Their portraits predate D13's corrected source identities, so no file has an approved matching final mapping for the current subjects. Both Shaban outputs were reviewed again: `_00001` is malformed and `_00002` is effectively background-only. None was installed. No exact supplied final for BRI, ARX, ASX, SCO, or SOK appeared in the manifest-declared folder.

## Crop and visual review

The final installed portraits were reviewed at native 156x210 and nearest-neighbor 4x in `portrait_takeover_native_4x_group_1.png`, `portrait_takeover_native_4x_group_2.png`, and `portrait_takeover_native_4x_group_3.png`. The corresponding `*_before_20261006.png` sheets show the runtime state before this tranche. User-output candidates were reviewed separately and were not confused with source placeholders.

The vanilla leader contact sheet at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/portraits/leaders/contact_sheet.png` was inspected before the reference-only `portrait_backdrops` family. The installed vanilla `interface/_leader_portraits.gfx` declarations for Sveinn Bjornsson, Carl Mannerheim, and Haile Selassie and their DDS files confirm the full 156x210 leader canvas. The backdrop examples were used only to consider background composition and supplied no identity, crop, or runtime pixels.

## Blocked and pending work

The Shaban Polluzha severity-1 quality issue remains blocked. The accepted 3,769x6,000 individual Commons scan itself is heavily overexposed; a cleaner, rights-cleared individual image was not found. The earlier group image's front-right fighter crop remains rejected because the caption does not identify that person, and no contrast repair or face substitution was attempted.

The Gayaz Ishaki federal-presidium severity-1 quality issue remains blocked. The D13-accepted book plate has already been cropped as a head-and-shoulders source placeholder; no source-only crop or contrast operation can add detail to its blurred scan. A local 1911 Commons image is clearer but about 25 years earlier than the 1936 start, so it was not selected. A much closer-era Commons candidate, [Ayaz Ishaki 1938 (cropped)](https://commons.wikimedia.org/wiki/File:Ayaz_Ishaki_1938_(cropped).jpg), is identified as a 430x657 Warsaw portrait with public-domain metadata, but the direct file download returned HTTP 429. No bytes were archived or substituted. The current book-plate source remains installed.

All twelve remain source placeholders pending the user's possible style-final request. This leaves the cross-cutting raw-photo-versus-painted-set mismatch recorded in the GFX review plan intentionally open under the user's source-mode gate. No real person was repainted or replaced by a fictional figure.

## Wiring, checks, and scope

All twelve existing `GFX_portrait_*` keys and stable `gfx/leaders/006_independence_wave/*.dds` paths remain unchanged. The existing character identities and portrait references were not edited. The four DDS corrections used the repository converter, and the final audit proves every runtime DDS is 156x210 and pixel-equal to its selected source PNG.

No HOI4 process, desktop game window, RunPod page, provider queue, or ImageGen was opened or used. No in-game check was run; live-game validation remains with the user. No focus, event, decision, country, localisation, gameplay, spreadsheet, or shared UI checks were in this portrait-only scope. No commit was made.
