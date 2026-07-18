# Event 019 Regional Flag Flatness Rescue — Bounded ImageGen Experiment

> **Historical experiment, superseded 2026-07-18:** This bounded 7/16/7/17
> ImageGen rescue experiment is retained as rejected-method evidence. It is not
> the current regional flag pipeline and does not describe the live blocker.
> The current owner-approved chain is 91 independent full-flag raws -> 91
> deterministic 820x520 spot-colour masters -> 273 native PNGs -> 273 runtime
> TGAs. Visual/runtime rows pass, while independent remediation re-audit,
> workbook export, and final completion audit remain pending.

Date performed: 2026-07-17  
Filename date: retained exactly as requested by the parent task (`2026_07_16`).

## Outcome

No technique produced an acceptable full-color, flat, orthographic regional flag source. All three allowed ImageGen calls are exhausted. No fourth call was made, no candidate was promoted, and no pass contact sheet was produced.

The decisive defect in every candidate is visible broad-area tonal falloff inside areas that must be constant ink fields. The unique-RGB counts below include edge antialiasing, so they are supporting evidence rather than the acceptance test by themselves; the plainly visible interior gradients are the acceptance failure.

This is a read-only recommendation handoff. It does not select or implement a fallback. No final DDS, processor, manifest, GFX, gameplay, localisation, spec, or fixed 27-identity-scene file was changed.

## References reviewed before generation

- Repository `AGENTS.md`, including required offline-wiki and vanilla-reference rules.
- Offline Paradox wiki core pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Relevant offline wiki pages: Graphical asset modding, Country creation (flag section), and Interface modding.
- Vanilla documentation directory. No flag- or raster-asset-specific official documentation was present for this narrow source-authoring question.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`, especially section 20, Flags.
- `C:/Users/klimp/.codex/skills/.system/imagegen/SKILL.md` and its prompting reference.
- Canonical flat references and their provenance: `assets/vanilla_reference/README.md`, `assets/vanilla_reference/CATALOG.md`, the normal/medium/small flag ladders, and `assets/vanilla_reference/flags/contact_sheet.png`. ARG, ARM_UK, and ANU were inspected individually as representative flat-ink references.
- Event 019 requirements in `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_6_derivative_countries.md` and `docs/specs/019_infantry_spawn_specs/prompts/019_infantry_spawn_asset_prompt.md`.
- The Regional Flag Matrix in `docs/assets/019_infantry_spawn/manifest.md`.
- The rejected pilot set at `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/` and the existing blocker report at `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_flag_flat_source_blocker_options_2026_07_17.md`.

The task named `regional_imagegen_raw_flat_test`, but that directory was absent. The rejected-generation evidence above is the live successor and contains the binary, flat, flat-edit, indexed, two-ink, colored-print, dual-reference, and cel-color-key pilots. All 14 pilot images were visually inspected. The full-color pilots retain field or emblem falloff; only the monochrome binary source is genuinely flat.

## Attempt 1 — ImageGen-only palette edit of a flat binary source

Technique: give ImageGen an already-flat black/white source and request a geometry-locked, color-only conversion to two exact spot inks. This tests whether the model can preserve spatial flatness when it need not invent geometry.

Edit target:

`docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_GHOST_BASE_EUROPE_binary_test.png`

Exact prompt:

```text
Use case: precise-object-edit
Asset type: Hearts of Iron IV fictional country flag source master
Input image: Image 1 is the edit target and its exact flat orthographic geometry is locked.
Primary request: recolor the existing binary flag into a genuinely flat two-ink full-color flag without redrawing anything. Map every pure black filled region in Image 1 to one single exact uniform deep navy-blue ink (#08233F). Map every pure white filled region in Image 1 to one single exact uniform pale spectral-cyan ink (#CFF7F4). Keep the exact anchors, three procession figures, winged crest, crossing lower chevrons, outlines, proportions, boundaries, and full-bleed rectangular framing unchanged.
Style/medium: raw digital spot-color separation; two opaque unmodulated RGB fills only; a flat raster flag design, not an illustration or mockup.
Composition/framing: straight-on orthographic full-bleed flag rectangle; no border outside the flag; no margin; no background scene.
Critical pixel behavior: within each navy field, every interior pixel must have the same RGB value; within each cyan field, every interior pixel must have the same RGB value. Boundary antialiasing may blend only across the one-pixel edge. Do not introduce any third ink, highlight, darker shade, lighter shade, glow, lighting, radial falloff, vignette, shadow, texture, grain, fabric, folds, perspective, depth, bevel, translucency, weathering, or local tonal variation.
Constraints: change colors only; preserve all authored emblem detail; no text, watermark, labels, flagpole, sky, scene, paper, swatches, registration marks, or presentation board. The output itself is the flag.
```

Provenance and evidence:

- ImageGen output: `C:/Users/klimp/.codex/generated_images/019f6ce5-2094-7582-b173-bafb2c08d093/exec-4378986b-1735-4414-88b2-6548db514cc2.png`
- Isolated copy: `docs/assets/019_infantry_spawn/source_png/flags/regional_imagegen_rescue_test/attempt_01_binary_palette_edit.png`
- Dimensions: 1536×1024; size: 1,280,941 bytes.
- SHA-256: `aff4cfba96083fa003a3411c80273995e48c50cdcf8b8a11ae1978f6fb8d9b00`.
- RGB evidence: 14,126 unique colors. Dominant values include `(4,37,74)` and `(197,240,241)`, rather than the requested exact inks.
- Verdict: **fail**. Both navy and cyan regions have visible center-to-edge tonal falloff. ImageGen treated recoloring as a relit render instead of a constant-ink mapping.

## Attempt 2 — Literal RGB channel-occupancy mask

Technique: request a newly authored Event 019 regional design in only the three extreme RGB-cube colors. Any shading necessarily introduces conspicuous mixed-channel pixels, making the flatness requirement semantically and visually explicit.

Exact prompt:

```text
Use case: logo-brand
Asset type: Hearts of Iron IV fictional country flag source master for Event 019, identity GOLEM_COLLECTIVE_AUSTRALIA
Primary request: create one original full-color flag as a raw digital RGB channel-mask design. The flag represents a collective golem host from Australia. Its principal emblem is a bold assembled stone hand made from interlocking block segments, enclosing a broken ring; a smaller eight-point navigation star joined to one clean wave-chevron is the regional secondary motif. Keep a strong authored heraldic silhouette and only large details that remain recognizable at 82x52 and 10x7.
Style/medium: literal digital channel-occupancy map, not painted art. Use exactly three opaque palette entries and no others: pure blue RGB(0,0,255) for the full field; pure yellow RGB(255,255,0) for the assembled-hand and broken-ring identity emblem; pure red RGB(255,0,0) for the navigation-star and wave-chevron regional accent. Every connected interior region must be a bucket-filled constant RGB value. Hard clean boundaries; no boundary softness except minimal one-pixel antialiasing.
Composition/framing: full-bleed 82:52 flag ratio, straight-on orthographic rectangle filling the entire image. Central emblem occupies about half the flag height; regional accent is large enough to survive at 10x7; balanced negative space.
Critical pixel behavior: there are only three spatially constant inks. Do not create darker blue, lighter blue, orange, gold, cream, pink, purple, black, white, gray, highlights, rim lights, shadows, glow, gradients, radial falloff, vignette, texture, grain, fabric, folds, depth, bevel, translucency, weathering, or any local tonal variation. This is a raw color-mask bitmap, not a presentation render.
Avoid: text, letters, numbers, watermark, flagpole, sky, room, scene, paper, border outside the flag, swatches, legend, labels, registration marks, mockup, perspective, lighting.
```

Provenance and evidence:

- ImageGen output: `C:/Users/klimp/.codex/generated_images/019f6ce5-2094-7582-b173-bafb2c08d093/exec-1f20678f-c7ac-4e9d-a33f-679ac89ceaf0.png`
- Isolated copy: `docs/assets/019_infantry_spawn/source_png/flags/regional_imagegen_rescue_test/attempt_02_rgb_cube_channel_mask.png`
- Dimensions: 1575×998; size: 1,068,400 bytes.
- SHA-256: `389a84aea51f662c905692a80a4731ebbeab37ac1fcf728b6b535a4f7b05c1d7`.
- RGB evidence: 27,287 unique colors. The most common blue is `(0,6,212)`, not `(0,0,255)`; the yellow emblem also contains broad shade changes.
- Verdict: **fail**. The blue field visibly brightens toward the emblem and the yellow emblem is shaded. The channel-mask framing did not suppress the model's lighting prior.

## Attempt 3 — Retained chroma field with binary emblem inks

Technique: exploit the model's background-extraction vocabulary but explicitly retain the chroma plane as the finished flag field, while limiting the authored emblem to black and white. This tests whether the strongest available “uniform backdrop” concept can coexist with a full-color flag.

Exact prompt:

```text
Use case: background-extraction
Asset type: Hearts of Iron IV fictional country flag source master for Event 019, identity ZOMBIE_SPECIES_AFRICA
Primary request: create one original flag as a black-and-white heraldic cutout on a perfectly flat solid #00FF00 chroma-key background. IMPORTANT: do not remove the chroma background; the #00FF00 backdrop is intentionally retained as the full-bleed green field of the finished flag. The main identity emblem is a bold black fragmented vertebral spiral forming a broken ring around a central black spearhead. The Africa regional secondary motif is a compact pure-white stepped sun joined to a small pure-white spearhead at the fly side. Use a strong authored outer silhouette and only large internal separations that remain readable at 82x52 and 10x7.
Scene/backdrop: one perfectly uniform, opaque, full-bleed #00FF00 chroma-key plane with no border and no surrounding scene.
Style/medium: raw chroma extraction plate; flat opaque silhouette artwork; exactly three unmodulated RGB fills: #00FF00 green background, #000000 black principal emblem, #FFFFFF white regional motif. No other colors.
Composition/framing: straight-on orthographic full-bleed 82:52 flag rectangle; central black emblem about half the flag height; white regional badge large enough to remain a distinct light mark at 10x7; generous clear separation between motifs.
Critical pixel behavior: the green background must be one uniform color with no shadows, gradients, texture, reflections, floor plane, lighting variation, vignette, or falloff. The black and white artwork must also be spatially constant solid fills with no gray, tint, highlight, internal shading, glow, depth, bevel, or translucency. Boundary antialiasing may occur only on the immediate silhouette edge.
Avoid: cast shadow, contact shadow, reflection, fabric, folds, flagpole, sky, room, paper, mockup, perspective, grain, weathering, text, letters, numbers, watermark, labels, swatches, checkerboard, registration marks, presentation board, extra colors.
```

Provenance and evidence:

- ImageGen output: `C:/Users/klimp/.codex/generated_images/019f6ce5-2094-7582-b173-bafb2c08d093/exec-cc97b633-43ec-4e46-80ed-9854413425ba.png`
- Isolated copy: `docs/assets/019_infantry_spawn/source_png/flags/regional_imagegen_rescue_test/attempt_03_retained_chroma_field.png`
- Dimensions: 1575×999; size: 1,031,973 bytes.
- SHA-256: `3016af6900a6de339e80367d0b2f44a8b73963b683189c43492b57d8cf74d80d`.
- RGB evidence: 21,639 unique colors; zero pixels equal the required `(0,255,0)`. Dominant field values include `(14,240,21)` and `(13,239,20)`. Corner samples range around `(30–33,231–236,28–33)` while upper and side-center samples range around `(15–17,239–240,14–22)`.
- Verdict: **fail**. The green field has an unmistakable center-bright/edge-dark falloff. Even chroma-key language did not produce a uniform retained field.

## Blocker and approval boundary

The bounded experiment establishes that prompt-only ImageGen does not reliably output spatially constant full-color inks for this flag family. The generated geometry can be strong, but accepting any of these shaded raw sources would violate the flat-flag requirement. No such acceptance is recommended or implemented.

Only the following two approval-requiring directions remain in scope:

### Option A — Independently generated monochrome flags

Generate each of the 91 identity-region designs independently as a black/white binary flag, with no shared source reuse. This preserves separate ImageGen authorship and has already shown that ImageGen can produce genuinely flat monochrome fields. It would, however, change the Event 019 regional flag direction from full color to monochrome, reduce palette-based regional differentiation, and require explicit user approval before production.

### Option B — User-approved deterministic flattening of independently generated full-color flags

Generate each of the 91 identity-region sources independently in full color, then apply a deterministic flat-ink conversion to each approved source. This retains source-authored geometry, full-color regional distinction, and richer emblem detail, but it requires explicit user approval to relax the current prohibition on solid-fill normalization, quantization, and local recoloring. If approved, raw and flattened masters, exact processor arguments, and hashes should all be retained; independent ImageGen provenance remains mandatory for every design.

No preference between Option A and Option B is asserted here. Neither was implemented.

## Files created

- `docs/assets/019_infantry_spawn/source_png/flags/regional_imagegen_rescue_test/attempt_01_binary_palette_edit.png`
- `docs/assets/019_infantry_spawn/source_png/flags/regional_imagegen_rescue_test/attempt_02_rgb_cube_channel_mask.png`
- `docs/assets/019_infantry_spawn/source_png/flags/regional_imagegen_rescue_test/attempt_03_retained_chroma_field.png`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_flag_flatness_rescue_2026_07_16.md`

No contact sheet was created because no candidate passed. No simplification or fallback was used.
