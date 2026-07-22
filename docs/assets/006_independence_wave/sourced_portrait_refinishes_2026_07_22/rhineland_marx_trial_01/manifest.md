# Wilhelm Marx source-locked portrait trial

Status: **candidate awaiting independent visual and provenance audit; not approved for runtime wiring**

This package contains one sourced real-male Rhineland civic-leader portrait candidate. It creates no advisor, dossier, `_small`, female, fictional, flag, focus, decision, localisation, gameplay, interface, or runtime asset.

## Subject and role

- Event 006 package: IW-008, Rhineland (`RHI` carrier).
- Stable role and consumer: `RHI_independence_wave_provisional_directorate`, opening civic leader.
- Subject: Wilhelm Marx (1863–1946), Cologne-born lawyer, Centre Party chairman, and former Weimar Chancellor.
- Role basis: a living Rhenish constitutional and civic figure in 1936, used as the real-person replacement for the rejected Karl Jarres likeness trial.
- Ownership gate: the Event 006 source-research handoff reports no active vanilla or current Chaos Redux character ownership hit. Same-person use in another mutually exclusive mod is disclosure-only and grants no permission to copy its art or source.

## Archival source and rights

- Commons page: <https://commons.wikimedia.org/wiki/File:Reichskanzler_Wilhelm_Marx.jpg>
- Library of Congress catalog: <https://www.loc.gov/pictures/item/2014716800/>
- Library of Congress digital ID: <https://hdl.loc.gov/loc.pnp/ggbain.36651>
- Direct Commons upload: <https://upload.wikimedia.org/wikipedia/commons/9/94/Reichskanzler_Wilhelm_Marx.jpg>
- Credit: Library of Congress, George Grantham Bain Collection, Bain News Service, digital ID `ggbain.36651`.
- Date: LOC records no date; Commons gives circa 1920. The uncertainty remains disclosed.
- Rights basis: Library of Congress and Commons state no known copyright restrictions/public-domain basis for the Bain image.
- Unchanged master: `source_masters/RHI_wilhelm_marx_loc_undated_c1920.jpg`.
- Unchanged master: `749x1024`, SHA-256 `DF60E8B2F335D1FE6B399D258A4B4FD52D3186AE6B0FCD323BAAF504E5079661`.
- Explicit head-and-shoulders crop: `(10, 54, 730, 1024)` from the unchanged master.
- Crop: `720x970`, SHA-256 `0E70BFD8B55BA0876E8661FD33AEB4892551304F3EEF56259F6F7AB4CBB3B200`.

## Source-locked repaint

- Identity source: the explicit Wilhelm Marx crop above; no other person is an identity input.
- Style-only reference: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/den_thorvald_stauning.png`.
- Prompt: `prompts/RHI_wilhelm_marx_identity_preserve_trial_01.txt`.
- ImageGen source result: `imagegen_results/RHI_wilhelm_marx_identity_preserve_trial_01.png`, `1086x1448`, SHA-256 `7FE508AE31CD7D2CC0AC79768222FAFDBC4925BFB85AD818BCDF31296FDB1E69`.
- Finish command: skill-local `advisor_icon_processing.py leader`, source kind `real`, explicit full-result crop `(0, 0, 1086, 1448)`, canonical vanilla leader reference directory.
- Processed `156x210` PNG: `processed_png/portrait_RHI_independence_wave_provisional_directorate.png`, SHA-256 `757A0DEAFF0A57595C6A87E3BFBC84E39D1187FA23871DA4EA85CEA6CD736839`.
- Review sheet: `contact_sheets/RHI_wilhelm_marx_source_result_reference.png`, SHA-256 `66C3BBC688C1F1A679E691CA6173A163C394E16B8489648F8D9815D2EF836056`.
- Processor metadata: `metadata/RHI_wilhelm_marx_processing.json`.

The refinish preserves Marx's bald crown and side hair, round spectacles, small pale moustache, long nose, cheeks and jowls, three-quarter gaze, expression, civilian suit, collar, and tie. Independent review must reject it if the tiny portrait loses his identity, reads as ordinary photography instead of HOI4 painted art, invents anatomy or attire, or fails the source/rights/ownership gates.

## Runtime gate

Do not copy this candidate into `gfx/leaders/006_independence_wave/`, convert it to DDS, register or change a sprite, rename the character in localisation/docs, or reopen IW-008 on this package alone. IW-008 also needs a separately approved sourced Josef Harpe commander portrait, exact runtime wiring, protected Josef Friedrich Matthes hash verification, and a fresh full country-package audit.
