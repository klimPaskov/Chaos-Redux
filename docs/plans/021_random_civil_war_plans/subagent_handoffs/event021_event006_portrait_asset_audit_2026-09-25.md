# Event 021 / Event 006 portrait asset audit

Date: 2026-09-25 (Europe/Kyiv).

Disposition: bounded visual/provenance audit; no portrait art, runtime DDS, character, GFX, localisation, gameplay, or existing crosswalk file was changed.

Scope: the 32 Event 021-admitted Event 006 packages listed in the accompanying JSON, their current portrait consumers, the installed vanilla portraits those consumers actually use, and the specified canonical leader reference family. This is not a whole Event 006 asset audit or a whole Event 021 asset audit.

## Findings

The package-by-package trace resolves 46 active Event 006 mod portrait sprite/runtime rows and 19 additional vanilla large-portrait consumer rows. Eighteen of those vanilla portrait rows have readable backing DDS files; Kuban's declared Ivanis large portrait texture is absent from the installed No Step Back DLC tree. The 65-row crosswalk therefore records 64 present textures and one missing runtime texture, with shared vanilla generic textures retained as separate consumer rows.

The 46 mod rows comprise 15 legacy generated grounded-polity portraits whose identity status remains unverified, 28 source-recorded real-person rows (25 pending the user's HOI4-style final and three separately flagged for source/visual review), one ARX row where live character token Gavino Piras consumes a portrait of Vittorio Vernè, and two current DDS files whose decoded pixels match archived ImageGen identity-preservation repaint candidates for real people. Those two rows are HAW Samuel Wilder King and HBX William D. Stephens; under the current portrait boundary they require user review and are not accepted as unchanged source placeholders or user-supplied RunPod finals.

The 19 vanilla rows comprise eight named, subject-specific vanilla portraits, ten name-keyed portraits backed by generic vanilla art rather than the named person's likeness, and the missing Kuban Ivanis texture. The generic-art rows are recorded as inherited vanilla mappings and `needs_user_review`; no replacement, genericization, or fallback was performed.

The two additional RHI/BAY sourced-person aliases are live, portrait-specific DDS/GFX consumers: Josef Friedrich Matthes and Rupprecht of Bavaria. Current consumers and cleanup/override paths are traced in the JSON, separately from the generated RHI/BAY council and commandant rows.

## Visual and provenance review

Every available in-scope DDS was decoded and inspected at native 156x210 and in nearest-neighbour 4x views against the canonical leader references. Available textures generally retain readable head-and-shoulders framing without clipping, borders, alpha seams, or path-induced wrong images. Three visual-quality notes remain distinct from identity/provenance: AFX's provisional-assembly face is a tight left-facing profile near the left edge; KOS Shaban Polluzha is unusually grainy and high-contrast; and ASX Vincenzo Di Benedetto is low-contrast/grayscale. None was repainted or adjusted.

The 15 legacy generated portraits may look technically well framed, but visual quality does not validate the depicted identity. The HAW and HBX runtime DDS pixels exactly match archived 156x210 PNGs produced by ImageGen identity-preservation workflows, not the unchanged source crops. HAW's source-clearance handoff explicitly says its crop was not runtime-promoted at that stage; HBX's older audit records an ImageGen repaint candidate. Both current-runtime matches therefore remain policy/provenance blockers pending user review.

The JSON records current runtime dimensions, byte counts, SHA-256 hashes, sprite/GFX registrations, consuming character IDs or history names, source and crop evidence paths, rights status as recorded in the local source files, review status, and unresolved action for each row. An exact decoded-pixel scan of 247 archived 156x210 PNGs was also performed; per-row matches are listed. A non-match means no exact PNG pixel match was found in that archive scan, not that the person's identity is disproved. The audit does not upgrade historical attribution or rights notes into a new licence or legal clearance.

No PNG or DDS output was created by this audit. Existing runtime DDS files were not converted again. No portrait-specific wiring was edited.

## Source revision and preserved work

The repository base revision read was `5206d465c1f37ef4371b78f42d0f163a8380a164`. Of the requested/current source surfaces, the worktree already contained user edits in `docs/events/021_random_civil_war/owned_asset_crosswalk.md` and `interface/006_independence_wave.gfx`; their current SHA-1 blob IDs are `5fb66948ecfe32f2aa18097556b47b648a18dc50` and `d56635315522bf05d6929393cb479907e86b57f4`, respectively. Their HEAD blob IDs are `b166f46f805fa1d4125006650533b1d635e62924` and `2ca06d53f8f26d13fb7e04a17e6a34ff481edc7b`. Both were read as current source and left untouched. The other specified repository sources were clean against HEAD at audit time.

Primary current source and status authorities include the Event 021 admission registry, the current Event 006 character and portrait GFX files, the Event 021 spec part 7, the supplied 2026-09-02 partial crosswalk, the 2026-09-13 Event 006 portrait asset audit, the 2026-09-19 Event 006 visual refresh, and the cited dated per-identity source packages. The partial crosswalk's 46-row/pending and no-row counts were treated as leads and were independently traced.

Temporary visual review sheets are outside the repository at `C:/Users/klimp/AppData/Local/Temp/cr_event021_portrait_audit_20260925_zph49f02/` (`native_01.png`–`native_03.png`, `nearest4x_01.png`–`nearest4x_15.png`) and `C:/Users/klimp/AppData/Local/Temp/cr_event021_portrait_audit_extra_pc9161qa/` (`native.png`, `nearest4x.png`). The canonical references used were `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`, and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png`.

## Limitations, blocked rows, and skipped checks

- The 15 superseded generated grounded-polity rows need a user-owned identity/source decision and, if still required, a user-supplied identity-correct HOI4-style final. No real person was invented, repainted, or substituted during this audit.
- HAW and HBX need user review because each current runtime DDS is pixel-identical to a retained ImageGen repaint output for a grounded real person. Their source and crop dossiers are recorded, but the current DDS provenance is not accepted as the required unchanged source placeholder or a user-supplied RunPod final.
- Ten vanilla generic-art rows need a user decision if subject-specific identity is required. The audit leaves their installed vanilla sprite mappings unchanged.
- KUB's missing large portrait needs a user/package decision or a restored vanilla texture. No substitute was selected.
- ARX `ARX_gavino_piras` currently consumes the Vittorio Vernè portrait sprite. The JSON records the character/depicted-person discrepancy for user review; the portrait was not relabelled.
- AXX Otto Roth, BBX Spyros Spyromilios, KOS Ferhat Draga/Miladin Popović, MAC Metodija Andonov-Cento, and several other source-placeholder rows lack an exact current-runtime-to-archived-156x210-PNG pixel match in the scanned archive. Their individual archived source/crop records and the prior supplied-DDS/runtime mapping are linked per row; the missing exact match is not silently promoted to identity/equality proof.
- The source-site attribution and licence state were read from the retained dated research records; live external source-page/licence terms were not re-fetched for this bounded audit. Rights are reported as locally recorded, not independently renewed or legally cleared.
- No RunPod page, workflow, configuration, queue, or output was opened or monitored. No native ImageGen was invoked. No game launch, HOI4 MCP render, or live runtime test was performed. Small-portrait/idea surfaces were not reviewed as substitutes for the 156x210 large-portrait family.
- The Event 021-owned asset crosswalk contains no portrait rows. This pass does not certify unrelated visual assets, whole-event asset coverage, or Event 006 completion.

Changed files are only this Markdown handoff and `event021_event006_portrait_asset_audit_2026-09-25.json`. Existing user changes were preserved.
