# `_scientists_portraits` portrait repair report

Date: 2026-10-06. The source-of-truth finding set is `_scientists_portraits` in `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` and the matching entries in `gfx_issues.json`.

The group contained five findings: zero severity 1, two severity 2, and three severity 3. Exactly two runtime DDS files changed in this group: the approved fictional portrait was repaired, and Otto Ambros's caption slab was removed from an authentic-source placeholder. Bounded source research was completed for the other historical subjects. The group is not fully closed because Rascher, Weigl, and Dufraisse remain blocked, and Otto still needs the user's painted HOI4-style final.

## Findings, in severity order

| Severity | Sprite | Original finding | Disposition and evidence |
|---:|---|---|---|
| 2 | `GFX_portrait_GER_otto_ambros` | Flat grey caption slab occupied the lower fifth of the 156×210 portrait. | The slab is removed by replacing the old art with a crop of an attributed U.S. Army Nuremberg photograph; parent approved identity, provenance, and framing on 2026-10-06. The runtime is a raw monochrome source placeholder, not a painted final, so this finding remains open for user-provided HOI4-style art. |
| 2 | `GFX_portrait_GER_sigmund_rascher` | Existing bust included a second figure and cut-off infant. | No free-licensed standalone bust was found. The sole standalone likeness is explicitly non-free; public-domain Commons/USHMM/HLS materials reviewed are experiment scenes or prisoners. Cropping above the infant cannot resolve the standalone source's reuse restriction. Existing runtime is unchanged; bounded source evidence is in `docs/assets/portraits/shared_scientists_portraits/GER_sigmund_rascher/blocked_research.md`. |
| 3 | `GFX_portrait_POL_rudolf_weigl` | Existing portrait is a strict downward profile rather than frontal or three-quarter. | The genuine, public-domain NAC profile candidate passed identity/provenance but failed the parent framing gate; it remains study-only and is not promoted. Existing runtime is unchanged. Bounded research and reviewer evidence are in `docs/assets/portraits/shared_scientists_portraits/POL_rudolf_weigl/pose_source_gap.md`. |
| 3 | `GFX_portrait_FRA_charles_dufraisse` | Existing full profile, beret, and large beard obscure the face and conflict with the scientist-bust direction. | The bounded search found a Commons public-domain laboratory group photo that identifies Dufraisse but shows him capped, bearded, and looking down; it fails framing. The official Collège de France photo is watermarked and has no reuse license. No candidate was copied or promoted; current runtime is unchanged. Evidence is in `docs/assets/portraits/shared_scientists_portraits/FRA_charles_dufraisse/blocked_research.md`. |
| 3 | `GFX_portrait_GER_perfect_aryan` | Existing fictional render was flatter, cooler, and more photo-like than the warm, textured scientist set. | Fixed with native ImageGen v2, parent-approved on 2026-10-06 for fictional identity, HOI4 painted style, complete bust framing, and subtle constructed temple join; standard DDS conversion and runtime promotion are complete. |

## Changed files and installed assets

Runtime DDS files changed in this group:

| Runtime path | Dimensions / bytes | SHA-256 | Processed PNG |
|---|---:|---|---|
| `gfx/leaders/scientists/portrait_GER_otto_ambros.dds` | 156×210 / 131,168 | `74c849c1da409c7724f25435d0a46710c417c691ef7cb98df7dcff7c5cfd298c` | `docs/assets/portraits/shared_scientists_portraits/GER_otto_ambros/portrait_GER_otto_ambros_156x210.png`, 156×210, SHA-256 `e124d8cd46a5e9ff3a0b164c24a79d0c37662662e336c07ff297c42e7f5bd635`. |
| `gfx/leaders/scientists/portrait_GER_perfect_aryan.dds` | 156×210 / 131,168 | `2d2106356382023a252c1eb03a03f53f58dd41414d0c0ca7f84be82f0ab75e0c` | `docs/assets/portraits/shared_scientists_portraits/GER_perfect_aryan/processed_png/portrait_GER_perfect_aryan_v2_156x210.png`, 156×210 RGBA, SHA-256 `5fd5b15a8ab92659b1a3bd02b3c76b939428645d5fabb463bdf1c407f7a94f86`. |

The Otto original source, exact crop, source/crop metadata, pending-final provenance contract, review sheet, and pre-fix runtime are in `docs/assets/portraits/shared_scientists_portraits/GER_otto_ambros/`. Its 253×340 source JPEG SHA-256 is `d9b7cf01e00986c33b54190dc33d59584277064139dee4bf14d18a6bf84b8a13`; the exact 197×265 crop SHA-256 is `89c3b3f85e95a43e9c5e80e8deb4a9b07c9ad9a10259e009f75afdb13dcfb6ff`. The parent-reviewed source crop sheet `review/portrait_GER_otto_ambros_source_crop_review.png` has SHA-256 `81934e42a866eafac5c7b9e0c6ee6a8ad63705e00bf69e86ac7c3f3b53b2a93b`.

The Otto source is [Commons File:Otto Ambros.jpg](https://commons.wikimedia.org/wiki/File:Otto_Ambros.jpg), attributed to U.S. Army photographers for OUSCCPAC/OCCWC and marked public domain in the United States; the 1945–49 trial-era date is a documented role-date limitation.

The fictional `perfect_aryan` v2 native ImageGen source is 1082×1454 RGB, SHA-256 `a540781f7ffef642971c9ab706becbab200f04ba2c6c279fb38d56cb5f8de15b`; exact v1 and v2 prompts are retained under `docs/assets/portraits/shared_scientists_portraits/GER_perfect_aryan/prompts/`. The earlier v1 remains preserved as a superseded candidate. Parent-reviewed candidate comparisons are `review/portrait_GER_perfect_aryan_native_comparison.png` (SHA-256 `bfab42ea2377cb9a5f476deb8073dbe90a00094ee981bf1056a5075984564657`) and `review/portrait_GER_perfect_aryan_4x_comparison.png` (SHA-256 `ea7a475987552d8d6ba5240116cf12847f43201131e899a60e655b00fd65f8b3`); before/after sheets are `review/portrait_GER_perfect_aryan_before_after_native.png` (SHA-256 `8f3472399e1944c4de83982b63886a400d3d206bb44643ba8702f2f245fa092c`) and `review/portrait_GER_perfect_aryan_before_after_4x.png` (SHA-256 `a859fa7857b7c0d10c231fdc80d643f5bb8d65c1f6d5f1aeb2b7f6e168865c33`).

The prior runtime DDS files were retained byte-for-byte before promotion: Otto SHA-256 `091b35b0a80e6e223e9e62e92c3764d4fb6b85eda6d10c7bb5b5a5230560b73f`, `perfect_aryan` SHA-256 `992fd164fd779b10388e3019ff930a9fc3f6b63794df1997709528ffec1a9cdc`.

Additional asset documentation changed or added: `docs/assets/portraits/shared_scientists_portraits/manifest.md`, `GER_sigmund_rascher/blocked_research.md`, `FRA_charles_dufraisse/blocked_research.md`, `POL_rudolf_weigl/pose_source_gap.md`, and `POL_rudolf_weigl/portrait_POL_rudolf_weigl.txt` plus its source-crop JSON to reconcile the completed parent review and unchanged runtime state.

The Weigl study sheet `review/portrait_POL_rudolf_weigl_source_crop_review.png` has SHA-256 `b3712fdb9f0e503469784fbb32b4d16292508d50d0ecf7f1e0e1770aaec9deaa`; parent explicitly rejected its pose for promotion. Its source/crop/processed hashes and parent finding remain in the adjacent contract and crop JSON.

The report and manifests preserve the source attribution, rights note, candidate status, review evidence, and the user-final boundary for each historical subject.

## Processing, wiring, and review

The installed vanilla leader portrait references and the local canonical reference `.agents/skills/chaos-redux-event-assets/assets/gfx_references/portraits/leaders/den_thorvald_stauning.png` were inspected before generation; the native leader portrait target is 156×210. The matching advisor dossier template was inspected for the sibling 65×67 work.

The Otto and `perfect_aryan` DDS files were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, validated as 156×210 DDS textures, and decoded pixel-for-pixel against their processed PNGs. The updated `perfect_aryan` before/after evidence is `review/portrait_GER_perfect_aryan_before_after_native.png` and `review/portrait_GER_perfect_aryan_before_after_4x.png` beneath its asset package; parent approved both native and 4× comparison evidence.

The full group contact sheets were generated with the documented filtered command `python .tools/gfx/gfx.py sheet --groups _scientists_portraits shared_chaosx_characters --out docs/plans/gfx_fix_2026-10/portrait_group_sheets_20261006 --label after`. For the before view, a temporary snapshot root copied the current registry and referenced textures, then restored the six exact pre-fix DDS files from their preserved backups; its root was `C:\Users\klimp\AppData\Local\Temp\chaosx_gfx_portrait_before_ecbf79b699ba42bd818f4707e551c029`. The before sheets were generated with `python .tools/gfx/gfx.py sheet --root C:\Users\klimp\AppData\Local\Temp\chaosx_gfx_portrait_before_ecbf79b699ba42bd818f4707e551c029 --groups _scientists_portraits shared_chaosx_characters --out docs/plans/gfx_fix_2026-10/portrait_group_sheets_20261006 --label before_snapshot`.

The scientist group sheets are:

| Snapshot | File | SHA-256 |
|---|---|---|
| Before | `portrait_group_sheets_20261006/_scientists_portraits_before_snapshot_1.png` | `aef129335bfc6fc187bf677bd523dc685aaca2acef53820d64ded2518e8ca1cd` |
| Before | `portrait_group_sheets_20261006/_scientists_portraits_before_snapshot_2.png` | `bb7c6487d2c4715233a9e852b0edcd863edb4d0b15365aa6c19cdef5f3f66edb` |
| Before | `portrait_group_sheets_20261006/_scientists_portraits_before_snapshot_3.png` | `f336c2103d5a8413de7aa62294591be2e874a84750421471c8ba77902ca5e80d` |
| After | `portrait_group_sheets_20261006/_scientists_portraits_after_1.png` | `61089add19edde6eee0cbca37eac1ad07a8b5a7bb704839cf807a469a4fa21a3` |
| After | `portrait_group_sheets_20261006/_scientists_portraits_after_2.png` | `596f8a30af5685f18c00e4eb38fcf7f7688a75cb39c1f758334a109764f3f6de` |
| After | `portrait_group_sheets_20261006/_scientists_portraits_after_3.png` | `f336c2103d5a8413de7aa62294591be2e874a84750421471c8ba77902ca5e80d` |

Visual comparison confirms `perfect_aryan` changed from its flatter capped image to the accepted warm painted fictional bust, Otto lost the slab but remains a raw historical source placeholder, and Weigl/Rascher/Dufraisse remain unchanged with the documented framing or source gaps.

The existing `GFX_portrait_*` sprite names and texture paths in `interface/_scientists_portraits.gfx` were checked and remain unchanged. No character definition, identity, role, portrait reference, or gameplay file changed.

No dedicated portrait inspection route was found; the exposed GUI/source routes are separate capabilities. The parent GUI requests stalled without artifacts, so no successful engine-context portrait preview is claimed. No game or desktop window was opened.

An earlier attempted command `python C:\Users\klimp\Videos\chaos_redux_trailer\tools\gfx_sheets.py --help` on 2026-10-06 at 10:12:47 Europe/Kyiv had no CLI parser and produced no captured output; its exact Python process (PID 12272) was stopped. At final audit the external scientist-sheet timestamps still read 08:54:03 and 08:54:04 local, before the runtime promotion tranche. Per parent direction, external originals are treated as unreliable and were neither restored nor used as the before baseline; the documented in-repository snapshot sheets are the comparison evidence.

## Replacement state and blockers

`GER_perfect_aryan` is fully replaced by its parent-approved fictional final.

Otto Ambros is an explicitly pending source placeholder; the user alone supplies the HOI4-style final.

Rascher is blocked by the only standalone photo being explicitly non-free and no rights-cleared single-bust crop being found.

Weigl is blocked by the accepted source pose being a downward profile; the study is preserved but not installed.

Dufraisse is blocked because the public-domain photo is not a qualifying frontal bust, and the official portrait-library photograph has unresolved reuse rights.

No historical portrait was generated, reconstructed, or genericized, and no RunPod provider was operated by the agent.

## Skipped checks and simplifications

No successful MCP GUI portrait preview or live game-state check was obtained; the source/native comparison evidence does not replace those gates.

No `.gfx` entry changed, so there is no source diff to review there; the unchanged references were checked against the current sprite keys and runtime paths.

The requested HOI4-style historical finals for the other four historical portraits remain user/source-gated or blocked, as enumerated above.

## Parent current-family review

The parent independently reviewed the current Rabid v2 and Godly Figure runtime portraits at native156x210, alongside the complete Holy Realm progression family.
Their painted finish, framing, and family consistency pass this task review; the Holy Realm family uses a quiet temple interior for the human seed and ornate interiors for later stages.
This current direct acceptance within the user-authorized graphics review is separate from the contradictory earlier release-manifest status labels, which are left for their owner to reconcile.

## Bounded second source pass, 6 October 2026

The portrait worker completed six additional targeted searches per blocked scientist and made no runtime changes.
No candidate met identity, usable crop, pose and reuse requirements together.

For Weigl, Commons marks the [UJK photograph from Wschód 131/1939](https://commons.wikimedia.org/wiki/File:Rudolf_Weigl_in_UJK_(-1939).jpg) as public domain, linking to the [Jagiellonian Digital Library publication](https://jbc.bj.uj.edu.pl/publication/922356); its 439×566 image remains a laboratory profile rather than a frontal bust.
Its inspected download SHA-256 is `2d26d9d5aefd827816d01bc70c52e39d5779bde15a817ba75506bdfc5a4f4c23`.
The NAC `1-N-541a` portrait hit identifies Marian Sokołowski, so it was rejected as the wrong person.

For Rascher, the [Lombardy Cultural Heritage record IMM-o9010-0000065](https://www.lombardiabeniculturali.it/fotografie/schede/IMM-o9010-0000065/) concerns a multi-person experiment scene; its page timed out and reuse terms could not be verified.
The related [Bridgeman photograph](https://www.bridgemanimages.com/en/noartistknown/nazi-physicians-performing-freezing-experiments-on-an-internee-at-dachau-concentration-camp-c-1942-b/black-and-white-photograph/asset/343409) is rights-managed and also fails the bust requirement.
The public-domain [pressurization-experiment image](https://commons.wikimedia.org/wiki/File:Pressurization_experiments_(Nazi_human_experimentation).jpg) depicts the prisoner/chamber rather than providing a Rascher portrait.

For Dufraisse, the official Collège de France records [000956_001, 21 June 1942](https://phototheque.college-de-france.fr/tl/image/info/5748/000956_001.html) and [001075_001, 24 June 1951](https://phototheque.college-de-france.fr/tl/image/info/6199/001075_001.html) identify him within large groups.
Their watermarked previews provide insufficient face detail and no stated reuse license.
The [Académie des sciences obituary](https://www.academie-sciences.fr/pdf/eloges/dufraisse_cr1969.pdf) is text only.

These findings reinforce the existing source blockers without substituting an unrelated person, an unlicensed photograph or generated historical face.
The six user-supplied painted portrait finals remain pending as recorded in the two portrait-group reports.
