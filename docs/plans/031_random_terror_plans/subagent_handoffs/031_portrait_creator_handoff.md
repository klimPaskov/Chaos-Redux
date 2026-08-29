# Event 31 Random Terror portrait creator handoff

Producer: `chaosx_portrait_creator`.

Scope: complete fictional and institutional static portrait package for Event 31 Random Terror.

Generation date: `2026-08-29`.

Generation mode: native built-in ImageGen with the Event 31 `fictional_high_chaos` portrait brief.

RunPod status: not opened, operated, configured, queued, or monitored.

## Delivered package

The package contains the full minimum `45/45` requested static rows: six military-command portraits, six clandestine-coordinator portraits, six revolutionary portraits, six criminal-political portraits, six millenarian portraits, eight jihadist-route portraits, six institutional council portraits, and one static False Revelation entity portrait.

The named one-person rows use fictional metadata only and were not based on real people. The council rows are people-free institutional compositions, as authorized by the brief. The entity is an impossible, ambiguous presence without a deity, demon, alien, or real-person identity.

The portrait-specific manifest with every row, proposed fictional metadata, exact source/processed/runtime paths, sprite proposals, state, consumer boundary, and coverage is `docs/assets/031_random_terror/portraits/manifest.md`.

The portrait-only sprite proposal is `docs/assets/031_random_terror/portraits/gfx_handoff.md`; it deliberately contains no shipped `.gfx` edit.

## Changed files and asset locations

- `docs/assets/031_random_terror/portraits/` contains 45 native ImageGen source subfolders, each retaining `<basename>_source.png`, plus the prompt record, contact sheets, round-trip PNGs, and processing evidence.
- `docs/assets/031_random_terror/portraits/prompts/prompt_record.md` retains the native ImageGen output IDs and per-row prompt records.
- `docs/assets/031_random_terror/portraits/processing_evidence.json` is the authoritative machine-readable dimension, crop, SHA-256, DDS-header, alpha, and round-trip evidence for all 45 rows.
- `docs/assets/031_random_terror/portraits/source_contact_sheet.png` is the native-source review sheet.
- `docs/assets/031_random_terror/portraits/final_contact_sheet.png` is the 156x210 processed review sheet.
- `docs/assets/031_random_terror/portraits/gfx_handoff.md` contains the proposed portrait-only sprite definitions and the explicit no-GFX-edit boundary.
- `docs/assets/031_random_terror/portraits/roundtrip/` contains the decoded DDS PNG for every row.
- `docs/assets/031_random_terror/processed_png/portraits/` contains the 45 deterministic processed PNGs.
- `gfx/leaders/031_random_terror/` contains the 45 final runtime DDS files using the stable basenames in the manifest.
- This handoff is `docs/plans/031_random_terror_plans/subagent_handoffs/031_portrait_creator_handoff.md`.

No `.gfx`, character, gameplay, localisation, event, focus, decision, country setup, sound, workbook, or unrelated UI file was changed.

## Source and rights evidence

This is a fictional/impossible source package, so no Internet attribution, real-person provenance, or external license was required. The native ImageGen output directory was `C:\Users\klimp\.codex\generated_images\01a04eee-7cf5-7053-baf7-6343032bd8eb`; every output was copied into the repository before processing.

The 45 native output IDs and prompt evidence are retained in `docs/assets/031_random_terror/portraits/prompts/prompt_record.md`. The copied native source PNGs are the durable source evidence for this fictional package.

The prompts explicitly excluded real persons, real extremist symbols, sacred branding, depictions of deities, national flags, readable text, modern gear, gore, stereotypes, and caricatures. No generated source was used as a proxy for a grounded historical identity.

The installed-reference review used `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/contact_sheet.png`, and the corresponding portrait rows in `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`.

## Processing, dimensions, and hashes

Native source canvases were RGB and varied slightly around the ImageGen portrait aspect ratio, with dimensions recorded per row in `processing_evidence.json`.

Every processed PNG is opaque RGB `156x210` and was produced with Pillow `ImageOps.fit`, LANCZOS resampling, and `centering=(0.50,0.46)`; the source crop box is recorded per row.

Every DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 156 --height 210`.

Every DDS passed the expected legacy uncompressed BGRA header: `DDS ` magic, header size `124`, width `156`, height `210`, pitch `624`, no mipmap payload, 32-bit RGB plus alpha masks `0x00ff0000/0x0000ff00/0x000000ff/0xff000000`, and exact file length `131168` bytes.

Every DDS alpha byte is `255`, and all 45 decoded DDS payloads are pixel-equal to their processed PNGs.

Full per-file SHA-256 values are not abbreviated or retyped here; `processing_evidence.json` records `source_sha256`, `processed_sha256`, `dds_sha256`, and `roundtrip_sha256` for each stable basename, alongside dimensions and validation fields.

## Runtime wiring handoff

The runtime directory is `gfx/leaders/031_random_terror/`.

The proposed portrait sprite names are `GFX_Portrait_Random_Terror_<family>_<index>` and the texture path is `gfx/leaders/031_random_terror/leader_random_terror_<family>_<index>.dds`, as listed row-by-row in the manifest.

The parent must confirm final Event 31 character, council, and entity consumers before installing portrait-specific `.gfx` entries or attaching fictional metadata to gameplay objects. The live repository search found no Event 31 portrait consumers in `common/characters/`, `history/countries/`, `gfx/leaders/`, or `interface/` for the requested route identifiers, so this worker intentionally did not guess a registry or fabricate character references.

No 65x67 advisor/high-command dossier cards were created. The accepted brief does not authorize blanket advisor portraits, and no final Event 31 roster proves up to twelve exact route-critical dossier consumers.

## Review result and replacement state

The native-source and processed contact sheets were reviewed for vanilla portrait framing, readable face/subject separation, role-specific visual motifs, period treatment, no modern objects, no readable generated text, no watermark, no real extremist or sacred branding, no flags, no gore, no stereotype or caricature, and no apparent real-person likeness.

The review result is `producer_review_pass; needs_parent_consumer_review` for all 45 rows.

All rows are native fictional ImageGen outputs and therefore have no grounded source-placeholder replacement cycle. Their manifest state is `styled_final` for this native fictional generation branch; none is a source placeholder, and none is awaiting a user-supplied RunPod replacement.

## Skipped checks and blockers

- Grounded Internet research, source attribution, and licensing checks were skipped because the brief classifies every row as fictional, institutional, or impossible.
- User-supplied HOI4-style final validation was not applicable to fictional native ImageGen rows; the user-only RunPod boundary was respected.
- Entity animation was skipped because no verified animated consumer, exact sprite path, frame count, timing, or animation brief was supplied.
- Advisor/high-command dossier portraits were skipped because no exact final character manifest or consumer authorization was supplied.
- `.gfx` and existing character portrait references were not installed because the user explicitly forbade GFX/gameplay wiring and the live consumer search returned no Event 31 portrait IDs to wire safely.
- In-game consumer validation was not performed; no agent may launch Hearts of Iron IV for this workflow.

No placeholder, generic face, repaint, real-person substitute, or unapproved fallback was used.
