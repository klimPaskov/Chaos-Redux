# Event 006 ARX Sardinian portrait source handoff v15

Date: 2026-07-29.

Owner: sourced visual-asset research subagent.

Scope: archival source research, source-master preservation, exact source crops, provenance, rights, role-fit notes, and cross-mod ownership checks for the three existing ARX full-size portrait consumers.

No gameplay, character, localisation, GFX, DDS, generated repaint, resized finish, advisor icon, dossier art, or small portrait was created or edited.

## Package

All bounded outputs live under [`docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/).

The package manifest is [`manifest.md`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/manifest.md).

The ownership evidence is [`research/ownership_audit.md`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/research/ownership_audit.md).

The role evidence is [`research/role_evidence.md`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/research/role_evidence.md).

The source-only GFX boundary is [`gfx_handoff.md`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/gfx_handoff.md).

## Conclusive role dispositions

### Civic leader: Emilio Lussu

`ARX_sardinian_provisional_assembly` remains the current Chaos Redux owner.

The new [Senate-sourced headshot](https://commons.wikimedia.org/wiki/File:Emilio_Lussu.jpg) is `source_ready_for_parent_review` because the unchanged 180x253 source is clear, male, directly attributed to senato.it, and licensed through the Commons `{{Senato.it}}` template as `CC BY 3.0 IT`.

The exact crop is `(0,0,180,253)` with paired equality JSON.

Roster admission remains `needs_user_review` because the source record only says `before 1958`, the 1936-era capture is not proved, and the previous 1916 repaint failed the likeness gate.

The 1945 De Gasperi group photo is rights-valid but rejected because Lussu is a small side-profile figure with no defensible head-and-shoulders crop.

### Crown/council representative: Luigi Arborio Mella di Sant'Elia

Mella is the strongest collision-free crown-route source found in this pass.

The [Senate portrait](https://commons.wikimedia.org/wiki/File:Mella_di_Sant%27Elia.gif) is `source_ready_for_parent_review`: born in Sassari, Grand Master of Court Ceremonies for Vittorio Emanuele III, confidant of Queen Margherita, alive in 1936, and source-licensed `CC BY 3.0 IT` through senato.it.

The exact crop is the complete decoded 153x193 frame `(0,0,153,193)` with paired equality JSON.

Roster admission remains `needs_user_review` because Commons gives only a `before 1955-06-26` death-date bound and the source is small; do not describe him as a 1936 senator because the biography dates his Senate appointment to 1939.

No exact Mella owner was found in current Chaos Redux, vanilla, or approved references.

### Commander: Vittorio Vernè, with Sardinian-born alternatives closed

The collision-free command package is [Vittorio Vernè](https://commons.wikimedia.org/wiki/File:Vittorio_Vern%C3%A8.jpg), not Giuseppe Valle.

Vernè is `source_ready_for_parent_review` if the route accepts a Sardinia-linked rather than Sardinian-born commander: Commons records an anonymous 1930s photograph with `PD-Italy` plus `PD-1996`, the prior ARX role audit documents his 1936 major-general command and Sardinia-linked formation, and no current/vanilla/Kaiserreich/approved-reference owner was found.

The exact crop is `(7,0,193,250)` with paired equality JSON.

If Sardinian birth is a hard requirement, the command role is `blocked_strict_birth_requirement`; Vernè was born in Rome.

Giuseppe Valle is not admissible despite ideal birth/era fit because Kaiserreich owns the exact person as `SRD_giuseppe_valle` with character, history, localisation, and large/small portrait consumers.

Giuseppe Pizzorno is Sardinian-born and role-plausible but `blocked_source_quality`: the only rights-valid portrait is a 145x160 side-profile thumbnail with insufficient detail for a defensible identity-preserving repaint.

## Ownership evidence

The exact collision records and paths are in `research/ownership_audit.md`.

The important hard collision is Kaiserreich `SRD_giuseppe_valle` in `common/characters/SRD characters.txt:129-148`, history recruitment at `history/countries/SRD - Sardinia.txt:173`, localisation at `localisation/english/KR_country_specific/SRD - Sardinia l_english.yml:598-599`, and portrait GFX at `interface/kaiserreich/portraits/SRD_portraits.gfx:27-32`.

Kaiserreich also owns `SRI_emilio_lussu`, but that is a disclosure-only cross-mod duplicate because the ARX target is already the same real person and current ARX remains the target owner.

No exact Mella, Vernè, or Pizzorno owner was found in the checked roots.

## Validation evidence

All five retained crop PNGs were generated with the repository exact-crop utility and paired JSON evidence reports `exact_source_crop_verified` with decoded pixel equality.

Retained crop hashes are recorded in the package manifest and source records.

Source masters were not rewritten after download or copy; SHA-256 values are recorded for every master.

## Remaining risks and parent actions

The package is not runtime-admissible by itself.

Parent must choose whether a late/undated Senate portrait is acceptable for Lussu and Mella, decide whether “Sardinia-linked” is sufficient for Vernè, then route only accepted sources through the separate source-locked repaint and independent likeness/style audit workflow.

No fallback, fictional identity, vanilla-owned face, or unlicensed substitute was introduced.
