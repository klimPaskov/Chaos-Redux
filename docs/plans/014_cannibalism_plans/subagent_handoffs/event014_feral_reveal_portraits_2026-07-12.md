# Event 014 Feral Reveal Portrait Handoff

## Scope and outcome

This subagent owned only the two reveal portrait animation packages, their four registered runtime DDS files, and this handoff.

The ordinary and Wendigo Hannibal packages are complete at the asset layer:

- Ordinary Hannibal: 12 independent generated frames of a progressive skull-licking action, with a gaunt pallid asymmetric face, severe dark-crimson staining, bloodshot wide eyes, irregular teeth, ecstatic feral expression, and invented torn 1936-1945 scavenged command clothing.
- Wendigo Hannibal: 16 independent generated frames of a separate crooked crouch, claw/jaw unfurl, diagonal lunge, inhuman apex, ice-shedding recoil, S-neck whip, swallow spasm, and re-crouch. The anatomy is dramatically inhuman and asymmetric.
- Both stale source starts were replaced: ordinary 000/001 and Wendigo 000.
- No actor or real-person likeness is used.
- No ancient-general, Carthaginian, Punic, elephant, classical, laurel, toga, or legionary framing is used.
- No Wendigo frame contains antlers, horns, deer traits, animal skull headdress, totem, runes, dreamcatcher, feathers, beadwork, tribal/Indigenous/sacred/ceremonial motifs, or a cultural-authenticity claim.
- The protected legacy `hannibal.dds` and `hannibal_wendigo.dds` files were not modified.

## Files changed

### Ordinary package

- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/brief.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/frame_plan.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/manifest.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/validation.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/gfx_handoff.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/hashes.sha256`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/notes/source_prompts.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/notes/leader_CBL_hannibal_identity_reference.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/source_frames/leader_CBL_hannibal_000_source.png` through `_011_source.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/processed_frames/leader_CBL_hannibal_000.png` through `_011.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/sheets/leader_CBL_hannibal_static.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/sheets/leader_CBL_hannibal_sheet.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/previews/leader_CBL_hannibal_source_contact.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/previews/leader_CBL_hannibal_contact.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/previews/leader_CBL_hannibal_preview.gif`

### Wendigo package

- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/brief.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/frame_plan.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/manifest.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/validation.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/gfx_handoff.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/hashes.sha256`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/notes/source_prompts.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/source_frames/leader_ZZZ_hannibal_wendigo_000_source.png` through `_015_source.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/processed_frames/leader_ZZZ_hannibal_wendigo_000.png` through `_015.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/sheets/leader_ZZZ_hannibal_wendigo_static.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/sheets/leader_ZZZ_hannibal_wendigo_sheet.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/previews/leader_ZZZ_hannibal_wendigo_source_contact.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/previews/leader_ZZZ_hannibal_wendigo_contact.png`
- `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/previews/leader_ZZZ_hannibal_wendigo_preview.gif`

### Registered runtime assets

- `gfx/leaders/014_cannibalism/leader_CBL_hannibal_static.dds`
- `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`
- `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static.dds`
- `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds`

### Handoff

- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_feral_reveal_portraits_2026-07-12.md`

## Existing identifiers and wiring verified

- Ordinary character: `CBL_hannibal`
- Wendigo character: `ZZZ_hannibal_wendigo`
- Ordinary character portrait: `GFX_portrait_CBL_hannibal`
- Ordinary GUI static: `GFX_cannibalism_revealed_portrait_static`
- Ordinary GUI animated: `GFX_cannibalism_revealed_portrait_animated`, 12 frames at 6 FPS
- Wendigo character portrait: `GFX_portrait_ZZZ_hannibal_wendigo`
- Wendigo GUI static: `GFX_cannibalism_wendigo_portrait_static`
- Wendigo GUI animated: `GFX_cannibalism_wendigo_portrait_animated`, 16 frames at 6 FPS
- Registered GFX: `interface/014_cannibalism.gfx`
- GUI consumer: `interface/014_cannibalism_frontline_hunger.gui`
- Scripted-GUI gate: `common/scripted_guis/014_cannibalism_scripted_gui.txt`

No GFX or GUI file was edited because all required final paths and frame counts were already registered.

## Before and after

Before:

- The ordinary package contained only two calm, tailored-looking source starts and no completed frame sequence or registered runtime output files.
- The Wendigo package contained only one calm, mostly human ice-skinned source start and no completed frame sequence or registered runtime output files.

After:

- Ordinary: 12 real source frames, 12 processed frames, static fallback, horizontal sheet, runtime DDS pair, source/final contact sheets, GIF, prompt record, manifest, hash ledger, validation, and GFX handoff.
- Wendigo: 16 real source frames, 16 processed frames, static fallback, horizontal sheet, runtime DDS pair, source/final contact sheets, GIF, prompt record, manifest, hash ledger, validation, and GFX handoff.

## Meaningful validation

- All 12 ordinary source frames and all 16 Wendigo source frames have distinct SHA-256 hashes. All 28 processed frames are also hash-distinct.
- All processed frames are exactly 156x210.
- Static fallbacks are byte-identical to their processed frame 000.
- Sheets are exactly 1872x210 and 2496x210.
- GIFs have exactly 12 and 16 frames at 170 ms per review frame and loop indefinitely. They are not referenced by GFX.
- Ordinary adjacent changed-pixel ratios range from 29.20% to 52.55%; Wendigo ratios range from 47.70% to 63.30%. These support the visual review that frames are full redraws rather than one-still transforms.
- The final Wendigo frame was regenerated to improve the last-to-first loop. Its processed last-to-first mean absolute difference is 7.93 with 14.27% changed pixels, while remaining a separate imagegen render and hash-distinct.
- Runtime DDS files use the required 32-bit BGRA masks and decode pixel-identically to the PNG static/sheets.
- Reveal secrecy is preserved: the ordinary command window requires `cannibalism_reveal_complete`; the transformation window also requires `cannibalism_wendigo_route_active` and the transformed Hannibal country trigger. The reveal effect sets the public flag before recruiting `CBL_hannibal`.
- Source and final contact sheets were visually reviewed at original resolution. Ordinary action, Wendigo identity continuity, inhuman anatomy, and motif exclusions survive the 156x210 crop.

## Moderation handling

The built-in image generator rejected four early ordinary calls whose prompts used explicit blood/gore wording. No images were returned. The accepted full imagegen redraws use dark-crimson wet/frozen stage-glaze wording, no victims, and no wounds, while visually retaining the severe blood-smeared and icy-gore presentation requested. The rejected attempts and retained edit lineage are documented in the per-package prompt records.

This did not introduce a static, sourced, composited, transform-only, or alternate-tool fallback.

## Parent follow-up

- Review the two final-size contact sheets and GIFs linked in the package manifests.
- Reconcile the shared/root Event 014 asset manifest and shared handoff only if that broader task surface requires it; those files were explicitly outside this subagent's scope.
- Include these files in the parent plan commit after final integration review.

## Skipped validation and why

- No gameplay or live UI files changed, so this subagent did not run an in-game session. Runtime paths, GFX registrations, frame counts, reveal gates, file formats, and decoded pixels were verified directly.

## Simplifications, omissions, and blockers

None. Both requested loops, all source/processed/final artifacts, both static fallbacks, both runtime sheet DDS files, both runtime static DDS files, manifests, prompt lineage, hashes, validation, contact sheets, GIF previews, and GFX handoffs are present. There are no remaining asset blockers.

## Skills and references used

- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-subagents`
- system `imagegen`
- Required offline core wiki pages plus `Graphical asset modding`, `Interface modding`, and `Scripted GUI modding`
- Vanilla `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, `interface/_leader_portraits.gfx`, and `common/characters/ABK.txt`
- Official vanilla `documentation/effects_documentation.md` portrait effects and `documentation/console_commands_documentation.md` portrait sanity reference
