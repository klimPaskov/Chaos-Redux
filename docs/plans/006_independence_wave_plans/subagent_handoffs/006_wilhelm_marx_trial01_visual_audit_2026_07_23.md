# Event 006 IW-008 Rhineland Wilhelm Marx portrait audit

Audit date: `2026-07-23`.

Audited package commit: `e84360a912b0431cd7cdd6f4e7d3cb3604cd300d` (`Add sourced Wilhelm Marx portrait trial`).

The shared branch was rechecked at current HEAD `0d2fed7cd849b37adba7d845195fa24fd3bf3e02`.

Scope was the real-person source, provenance, visual identity, role fit, ownership, hashes, metadata, handoff, and protected Matthes check only; this audit changed no source, runtime, DDS, `.gfx`, gameplay, character, localisation, or manifest file.

## Verdict

**PASS for independent sourced-portrait visual/provenance admission; runtime promotion remains deferred.**

The unchanged Bain/Library of Congress source, explicit crop, identity-preserving repaint, and native `156x210` result all identify the same Wilhelm Marx with a readable HOI4 country-leader finish.

The candidate is not runtime-complete because the trial intentionally contains no final DDS and remains unapproved in its own metadata.

## Source, identity, rights, and role

- The source is `source_masters/RHI_wilhelm_marx_loc_undated_c1920.jpg`, `749x1024`, unchanged indexed-grayscale JPEG, SHA-256 `DF60E8B2F335D1FE6B399D258A4B4FD52D3186AE6B0FCD323BAAF504E5079661`.
- The source record is [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Reichskanzler_Wilhelm_Marx.jpg), [Library of Congress item 2014716800](https://www.loc.gov/pictures/item/2014716800/), [LOC digital ID ggbain.36651](https://hdl.loc.gov/loc.pnp/ggbain.36651), and the [direct Commons upload](https://upload.wikimedia.org/wikipedia/commons/9/94/Reichskanzler_Wilhelm_Marx.jpg).
- Commons identifies the subject as German Chancellor Wilhelm Marx, credits Bain News Service and the Library of Congress George Grantham Bain Collection, and records public-domain/no-known-copyright-restrictions status.
- The Commons date field says `1920`, while the LOC caption-date uncertainty and Commons file history say the date is unverified, so the package correctly retains `undated/early twentieth-century (Commons circa 1920)` uncertainty.
- The role is defensible for a living Rhenish constitutional/civic elder in 1936 because authoritative [DHM LeMO biography](https://www.dhm.de/lemo/biografie/wilhelm-marx) and [Bundesarchiv overview](https://weimar.bundesarchiv.de/WEIMAR/DE/Content/Virtuelle-Ausstellungen/die-reichskanzler-der-weimarer-republik.html) identify Marx as Cologne-born jurist, Centre Party leader, and Weimar Reich Chancellor who lived until 1946.
- DHM records that Marx withdrew into private life in 1932, so the route should present him as a revived civic/constitutional elder or provisional-directorate figure rather than imply that he held an active historical office in 1936.
- Same-person use in a mutually exclusive reference mod is disclosure only and is not a blocker; Kaiserreich `1521695605` has narrative Wilhelm Marx mentions but no character, recruitment, portrait, or `.gfx` owner, while `2265420196` and `1458561226` returned no exact identity owner.
- No reference-mod art or source was copied, and the den Thorvald Stauning image is style-only.

## Crop, repaint, and visual review

- `source_crops/RHI_wilhelm_marx_head_shoulders.png` is `720x970`, SHA-256 `0E70BFD8B55BA0876E8661FD33AEB4892551304F3EEF56259F6F7AB4CBB3B200`, and its `(10,54)-(730,1024)` pixels match the unchanged source master exactly across all `698400` pixels.
- The full `imagegen_results/RHI_wilhelm_marx_identity_preserve_trial_01.png` is `1086x1448` RGB, SHA-256 `7FE508AE31CD7D2CC0AC79768222FAFDBC4925BFB85AD818BCDF31296FDB1E69`.
- Full-size source-versus-result review preserves the high rounded balding crown, sparse side hair, narrow round spectacles, heavy eyelids, long nose, pale moustache, cheek and jowl volume, rightward three-quarter gaze, closed mouth, facial asymmetry, dark civilian suit, white shirt, patterned tie, and head-and-shoulders pose.
- The repaint slightly cleans the moustache and glasses edges and smooths photographic damage, but it does not materially change facial proportions, apparent source age, expression, clothing, pose, or recognisable identity.
- The processed `processed_png/portrait_RHI_independence_wave_provisional_directorate.png` is an opaque `156x210` ARGB PNG, SHA-256 `757A0DEAFF0A57595C6A87E3BFBC84E39D1187FA23871DA4EA85CEA6CD736839`, with alpha `255..255`.
- At native `156x210`, the bald crown, round glasses, long nose, small moustache, full cheeks/jowls, three-quarter gaze, suit, collar, and tie remain readable enough to identify Marx rather than a generic middle-aged civic face.
- The result uses visible hand-painted planes, restrained brush texture, muted desaturated interwar values, a quiet neutral backdrop, and a readable opaque silhouette compatible with the canonical leader family rather than a raw photograph, sepia conversion, or generic oil filter.
- No uniform, medals, insignia, hat, props, text, watermark, border, second person, female presentation, advisor card, dossier frame, or invented institutional symbol is visible.
- The contact sheet `contact_sheets/RHI_wilhelm_marx_source_result_reference.png` is present at `1344x464`, SHA-256 `66C3BBC688C1F1A679E691CA6173A163C394E16B8489648F8D9815D2EF836056`, and shows the source crop, native candidate, and canonical leader references.

## Ownership, runtime boundary, and integrity

- Exact and variant forms (`Wilhelm Marx`, `Wilhelm_Marx`, `wilhelm_marx`, `Marx, Wilhelm`, and name-order variants) returned no active vanilla or current Chaos Redux character, recruitment, portrait, `.gfx`, or localisation owner in `common/characters`, `history/countries`, `common/country_leader`, `interface`, `gfx/leaders`, or `localisation/english`.
- Current Chaos Redux does own the stable role slot `RHI_independence_wave_provisional_directorate`, its sprite `GFX_portrait_RHI_independence_wave_provisional_directorate`, and an older runtime DDS currently localised as Karl Jarres; that generated role slot is not an existing Wilhelm Marx identity owner and must be renamed only during parent-approved admission.
- No package or current Event 006 runtime file provides an RHI `_small`, advisor, dossier, high-command, or theorist portrait or consumer, and no such derivative is authorized by this trial.
- The package metadata records processor SHA-256 `C6E78C01C025AD57FEF8DC25EB79BD216FF9809DF27E4C758EB9EC72594A3963`, source/result/review hashes matching the files above, canonical reference directory `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders`, and status `candidate_requires_visual_approval`.
- `gfx_handoff.md` reserves `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds`, sprite `GFX_portrait_RHI_independence_wave_provisional_directorate`, interface `interface/006_independence_wave_region_01_portraits.gfx`, consumer `RHI_independence_wave_provisional_directorate`, and player-facing identity Wilhelm Marx.
- No final DDS exists in the trial and no DDS conversion was run in this bounded audit; the parent must use the repository converter only after visual approval and then perform the full IW-008 package audit.
- The protected runtime file `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` remains byte-identical at `131168` bytes with SHA-256 `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`.

## Parent handoff

Admit the Marx candidate as a sourced real-male leader portrait for the visual/source gate, preserve the source URLs, date uncertainty, hashes, and style-only reference boundary, and keep runtime wiring deferred until the standard DDS conversion, Wilhelm Marx localisation update, protected Matthes verification, and complete IW-008 country-package audit are finished.

Simplifications, omissions, and blockers: no visual or provenance blocker was found, but the trial has no final DDS by design and is not itself runtime approval.
