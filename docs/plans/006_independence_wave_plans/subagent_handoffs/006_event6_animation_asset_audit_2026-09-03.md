# Event 006 animation asset audit

Audit date: 2026-09-03. Scope: ASSET-040 recognition seal, ASSET-041 dependency warning, ASSET-042 league charter activation, and ASSET-043 formable eligibility seal under `gfx/interface/006_independence_wave/animations`, their registrations in `interface/006_independence_wave.gfx`, and their consumers in `interface/006_independence_wave.gui`.

## Result

All four accepted animation packages are complete and usable from the asset side. Every package retains independent source masters, processed 64x64 RGBA frames, a horizontal sheet PNG, a horizontal runtime DDS sheet, a 64x64 static PNG/DDS fallback, a GIF review preview, contact-sheet evidence, and manifest/build-report entries.

No source frame, processed frame, sheet PNG, runtime DDS, GFX definition, or GUI layout required repair. The only safe drift found was documentation metadata: the four briefs, manifest, and build report said `play_on_show = no`, while the live animated sprite definitions intentionally use `play_on_show = yes` for the explicit Animate toggle. Those documentation values were aligned to the live definition and the manifest's report hash was refreshed.

## Required reference review

The canonical reference root used was `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`.

The matching family was `icons/decision_categories/`. I inspected `icons/decision_categories/contact_sheet.png` first, then `decision_category_generic.png` (51x40 RGBA), `decision_category_generic_crisis.png` (52x39 RGBA), `decision_category_border_conflicts.png` (52x40 RGBA), and `decision_category_generic_democracy.png` (52x40 RGBA) individually at native size. The family establishes compact, centered, transparent-corner category icon treatment; the accepted Event 006 brief target remains the parent-provided 64x64 canvas.

The installed vanilla animation precedent was also checked in `interface/alerts.gfx` and `interface/countryconstructionsview.gfx`. The Event 006 definitions use the same horizontal `frameAnimatedSpriteType`, `noOfFrames`, `animation_rate_fps`, `looping`, `play_on_show`, `alwaystransparent`, and `buttonstate_blendframes.lua` conventions.

## Runtime definition and consumer trace

`interface/006_independence_wave.gfx:66-77` contains exactly one state-strip sprite, one animated sprite, and one static sprite for each accepted package. Every targeted GFX name has exactly one definition across `interface/**/*.gfx`; every referenced texture path exists with matching case.

| Asset | State order and frame map | State-strip sprite | Animated sprite | Static fallback sprite | Runtime sheet | Frames/FPS |
| --- | --- | --- | --- | --- | --- | --- |
| ASSET-040 recognition seal | `hidden=1`, `weak=2`, `rising=3`, `strong=4`, `entrenched=5` | `GFX_independence_wave_recognition_seal_states` | `GFX_independence_wave_recognition_seal_animated` | `GFX_independence_wave_recognition_seal_static` | `independence_wave_recognition_seal_sheet.dds` | 5 / 5 |
| ASSET-041 dependency warning | `calm=1`, `watch=2`, `danger=3` | `GFX_independence_wave_dependency_warning_states` | `GFX_independence_wave_dependency_warning_animated` | `GFX_independence_wave_dependency_warning_static` | `independence_wave_dependency_warning_sheet.dds` | 3 / 5 |
| ASSET-042 league charter activation | `rest=1`, `drafting=2`, `vote=3`, `activated=4` | `GFX_independence_wave_league_charter_activation_states` | `GFX_independence_wave_league_charter_activation_animated` | `GFX_independence_wave_league_charter_activation_static` | `independence_wave_league_charter_activation_sheet.dds` | 4 / 5 |
| ASSET-043 formable eligibility seal | `hidden=1`, `discovered=2`, `eligible=3`, `proclaimed=4` | `GFX_independence_wave_formable_eligibility_seal_states` | `GFX_independence_wave_formable_eligibility_seal_animated` | `GFX_independence_wave_formable_eligibility_seal_static` | `independence_wave_formable_eligibility_seal_sheet.dds` | 4 / 5 |

`interface/006_independence_wave.gui:23-31` places the four state strips and four animated siblings at matching coordinates and `scale = 0.72`; the animated siblings are not independently offset. `common/scripted_guis/006_independence_wave_scripted_gui.txt:89-104` makes the four state strips visible when `independence_wave_status_gui_show_animation` is absent, makes the four animated siblings visible when that flag is present, and supplies the four state-strip frame properties from the parent-owned state variables. The first frame is therefore the package fallback and the strip state is deterministic when animation is disabled.

## Pixel and frame evidence

All source masters are `1254x1254 RGB` inherited opaque ImageGen outputs. All processed frames are `64x64 RGBA`. The source masters are retained untouched. Frame-order lists below are left-to-right sheet order.

### ASSET-040 recognition seal

Frame order is `hidden`, `weak`, `rising`, `strong`, `entrenched`; frame math is `5 * 64 = 320`, so the sheet is exactly `320x64` and the static fallback is the hidden frame.

Processed frame SHA-256 values in order are `9ea1587bb5f5e4352747811c9822b3480f9a24d3a2a657ad7cde3fbadad6c145`, `c88c04126008a7abd799dfff8f26fcbe3b4e642778bf37b41798520328d75a1a`, `176bbcc8b63695d120a2132e733a2d6b27220fa711fa4d2ba2c98eb440a34f8d`, `7f160a55fba49653a219e7af2e89912f4514e0b677c5e3603eda0eaff41ed72a`, and `e28aeed2220eae17054a189d62f17897c2c01cb6c0bd520104d44d63b48b1e29`.

The source-master SHA-256 values in the same order are `5e8227076f165d0bd760c9fc423dc7d362dad35bbbd61a742843ca39b0963bf5`, `af96d1211bc00abac72258824d8382f1ab4b5302c87cdbc5a9d6df7557b27a8e`, `6a93a9a7b949c81965e3c0767c1b87892462b4cfc45940498b200796fc318559`, `0bd9bae4c8f68976e680841b50908c97efdbc991d9d0397b6eef3f8de8f09209`, and `d662706c0d19569cd682117cced803482c5b00010ad85f1c8e62484db27c16d5`.


The sheet PNG SHA-256 is `509d53dee0d25b715f6854a3c8c16b5a4d6e86567a6782b2b4cc149fe49551c2`. The runtime sheet DDS is 82048 bytes, `320x64`, SHA-256 `b6572f49f85660e64842a9a4b5cc56a16076a0c12c1d00a875ba8708603fe9fd`. The static PNG is the hidden processed frame with SHA-256 `9ea1587bb5f5e4352747811c9822b3480f9a24d3a2a657ad7cde3fbadad6c145`; the runtime static DDS is 16512 bytes, `64x64`, SHA-256 `c1871b031ccb2c264c6508e6a02482231020ab81c63cabe4efaa2f0e794c41cc`.

Visual review at native 64x64 shows the intended progression from unlit navy star, through weak/rising/strong illumination, to the entrenched gold wreath. Every pair of frames differs in at least 2777 of 4096 pixel tuples, proving independent authored state art rather than transform-only motion. Alpha bboxes are end-exclusive `(3,3)-(60,61)`, `(3,3)-(61,61)`, `(3,3)-(61,61)`, `(3,3)-(61,61)`, and `(3,3)-(60,61)` in order; all four canvas edges have zero nontransparent pixels in every frame. The decoded DDS sheet, all five decoded DDS frame crops, and static fallback match the processed PNG pixels exactly.

### ASSET-041 dependency warning

Frame order is `calm`, `watch`, `danger`; frame math is `3 * 64 = 192`, so the sheet is exactly `192x64` and the static fallback is calm.

Processed frame SHA-256 values in order are `1f9b411fa44f47b1a20fb00ac86e5e8399bbae7c9e316db98dd6496572eb03f8`, `18fac2ec2ecf4decfc43e85fefae4e6bd933dcb079026fce0bf57ca10b7176ad`, and `ccc61e9d7160e2baa4c0526f1ca21a46b1abcb1dab5cf9b58892797d56c86c31`.

The source-master SHA-256 values in the same order are `5c9152db712de93915c3beb6f33b8552402755ab7a782ccec3059f4dc61319b5`, `8d1db1072e57c2a2b2242a34af9fe10b2fc27e2e02dbbd5cf80decb6ce6bedec`, and `c728754a3ae2ef2da187e4a19d61dbae3683c7c951b775fadc5671433bedfa0e`.

The sheet PNG SHA-256 is `143dd67da034ca2fcd8568e1c907bf8cc4a5ba1f93a006ab744a46672a58e4c3`. The runtime sheet DDS is 49280 bytes, `192x64`, SHA-256 `2ed53c2f6ae1a55ebd89f5ede4795885de1b16d5fdd51741d0936fe192162fe6`. The static PNG is the calm processed frame with SHA-256 `1f9b411fa44f47b1a20fb00ac86e5e8399bbae7c9e316db98dd6496572eb03f8`; the runtime static DDS is 16512 bytes, `64x64`, SHA-256 `c52d3a2d17dbd594c9ceac36778cab4eb6dfe525efb26d424211282a53bcd1c4`.

Visual review at native 64x64 shows the intact chain and blue/green shield in calm, loose chain and amber warning in watch, and snapped chain, crimson jewel, and red rays in danger. Every pair of frames differs in at least 2050 of 4096 pixel tuples. Alpha bboxes are end-exclusive `(9,3)-(54,61)`, `(9,3)-(54,61)`, and `(11,3)-(53,61)`; all four canvas edges have zero nontransparent pixels in every frame. The decoded DDS sheet, all three decoded DDS frame crops, and static fallback match the processed PNG pixels exactly.

### ASSET-042 league charter activation

Frame order is `rest`, `drafting`, `vote`, `activated`; frame math is `4 * 64 = 256`, so the sheet is exactly `256x64` and the static fallback is rest.

Processed frame SHA-256 values in order are `3d8f22e7281a2acb83d4fca7868e8b1b515dc0fcaa04374187a9807dee3fee2b`, `09318e3940dbd3f45a7f3723f3701a1f849ce54f1ce2fcbc0adaa81921cc5d93`, `dcb8888156fff8de46e5be5b3f13a3a151a2600807547627a32b3ad5f43a0608`, and `b2d6468425fa1ae740392652e16dcb2a2acb3cd1eb3e638637ff3d253f08feb3`.

The source-master SHA-256 values in the same order are `fa0dc1f83f5bf0c6fcbd7e31bbf629f9995e9647f0af2aba6f8695c67b7af2c6`, `f86fcea89a74cb4b58b22547ac1538644a3a7a050c4a122b122183d6a5b62b76`, `d1f78da691029ee9f3c8e5747b5f70fa02f0916a13c33c4d3f7b45a21496153d`, and `e35ec4910d1e70d405eb3ab00b13420f3a89a2f8ea64aa1e6500ca7613cd66cd`.

The sheet PNG SHA-256 is `06424131427b6eb7a1897540437c8f30875a14fd5ff0a6eafdf3e06a6d1df8aa`. The runtime sheet DDS is 65664 bytes, `256x64`, SHA-256 `fe4d108d4a085f719eaacf57352bb3f85b69bba1fec88360c0c41ef28734858b`. The static PNG is the rest processed frame with SHA-256 `3d8f22e7281a2acb83d4fca7868e8b1b515dc0fcaa04374187a9807dee3fee2b`; the runtime static DDS is 16512 bytes, `64x64`, SHA-256 `08f021545bae25aa875a557e54275058bacaf0156ee6617d297d3724643457af`.

Visual review at native 64x64 shows the closed charter in rest, lifted parchment and quill in drafting, open parchment and vote stars in vote, and sealed charter with joined pennants and cyan-gold activation halo in activated. Every pair of frames differs in at least 2386 of 4096 pixel tuples. Alpha bboxes are end-exclusive `(3,3)-(61,61)`, `(8,3)-(55,61)`, `(3,3)-(60,61)`, and `(3,3)-(61,60)`; all four canvas edges have zero nontransparent pixels in every frame. The drafting centroid shifts down because the authored parchment extends lower; the canvas placement and silhouette remain centered and unclipped. The decoded DDS sheet, all four decoded DDS frame crops, and static fallback match the processed PNG pixels exactly.

### ASSET-043 formable eligibility seal

Frame order is `hidden`, `discovered`, `eligible`, `proclaimed`; frame math is `4 * 64 = 256`, so the sheet is exactly `256x64` and the static fallback is hidden.

Processed frame SHA-256 values in order are `38242fdff1565e2403b2a8d1660980869bfb657d054c8d1e90439df581bededa`, `505113157083d48471fb174812eefd333fda08d5657e1f63acbe76d502fb4e32`, `20a258f4ee9363e5941cfb0f1389c4ed4e1d6336bc2106b577b3cd31dfccfb23`, and `89be6faf7148fb05f17e36014aa069727793d3763fd9fcd7f76a9276e827a125`.

The source-master SHA-256 values in the same order are `1b0d2abff442df6a9f92f3cf04e3c7aa8b45eca32a2a006e7270a2c2ac371487`, `82c44f59ac5b4ff5b46ba27302939ee6b97ad1592701650036f7905cd1548f63`, `f1f9d2a29931a2a825566f8556f8d8a582797c4f12e52fec28f495878d9d3142`, and `848057cdf9cc47951e70929944c0c00d74b1730fe67ae53b62a160fb121fe1f7`.

The sheet PNG SHA-256 is `bff59c72658dbee5f8baa10c5732437b36bdbf91f8b23280f138e76bca41e105`. The runtime sheet DDS is 65664 bytes, `256x64`, SHA-256 `db8ca4e24c7ce343a354b9a768dc5b2533666bf5779ddf4a9f5a9282b4f64271`. The static PNG is the hidden processed frame with SHA-256 `38242fdff1565e2403b2a8d1660980869bfb657d054c8d1e90439df581bededa`; the runtime static DDS is 16512 bytes, `64x64`, SHA-256 `de2f835fb3e60bd6fa906884af572f9a588fc614b1b409d91411c6867ebb6a8a`.

Visual review at native 64x64 shows the dark hidden seal, discovered compass-star shield, eligible joined stars with green-gold inset, and proclaimed civic crown with ribbon tabs and full cyan-gold halo. Every pair of frames differs in at least 2676 of 4096 pixel tuples. Alpha bboxes are end-exclusive `(3,3)-(60,61)`, `(4,3)-(59,61)`, `(4,3)-(60,61)`, and `(3,3)-(61,61)`; all four canvas edges have zero nontransparent pixels in every frame. The decoded DDS sheet, all four decoded DDS frame crops, and static fallback match the processed PNG pixels exactly.

## Alpha, bleed, and DDS checks

Every processed frame has transparent corners and zero nontransparent pixels on all four canvas edges. Alpha values are preserved as antialiased RGBA rather than flattened; each frame has 137-242 distinct alpha levels and 460-1041 semi-transparent pixels. Every fully transparent pixel is RGB `(0,0,0)`, with no retained green chroma in the transparent canvas. Native-size visual inspection found no clipped outline, shadow, glow, coloured spill, fake checkerboard, unintended transparent hole, or cross-frame bleed. The frame boundary columns are transparent in each source frame, and the reconstructed horizontal sheets were pixel-equal to the concatenation of their ordered processed frames.

All eight runtime DDS files were decoded from their actual bytes. Each uses the strict uncompressed 32-bit BGRA layout (`DDS ` magic, header size 124, pixel-format size 32, RGB+A masks, zero mipmaps, caps `0x1000`) and exact byte length `128 + width * height * 4`. Every decoded sheet is pixel-equal to its sheet PNG, and every decoded static fallback is pixel-equal to both its static PNG and its first processed frame.

The historical package source route is documented in each `notes/source_prompts.md`: inherited opaque `#00ff00` ImageGen masters were preserved, then the verified official helper `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py` was used as the fallback with its default key-removal settings (`#00ff00`, tolerance 12, soft matte, transparent threshold 12, opaque threshold 96, no edge feather, no edge contract, despill/spill cleanup). This is an inherited-source fallback, not a newly generated opaque-background route. The repaired outputs pass the native alpha and edge checks above.

## MCP evidence

The read-only `mcp__hoi4_agent_tools__hoi4_gui_inspect` call for `independence_wave_status_window` under scenario `event006_animation_asset_audit_2026_09_03` returned `GUI_INSPECTED`, status `ok`, complete source graph, zero skipped sources, and 48 inspected Event 006 elements. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/693c2a44394ebb80b15caa5889aeae1e9a86b3233124046b4eb914723af9cc00/9a4fd176f7e8c378143bf2ee0a31620008efaa208c43381c25b3f67d53ada186/gui-inspect.08bc00343bf70b92.json`.

The read-only `mcp__hoi4_agent_tools__hoi4_gui_render` call for the same window and scenario returned `GUI_RENDERED` for 1920x1080 and 1366x768, normal/active/warning requested states, and 27 artifacts including full, cropped, annotated, click-region, source-map, hierarchy, state-matrix, resolution-scale, and comparison outputs. Full render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0682fbd89fe2ffad5c6d772325ae581172213fb4eb67e281c7257ea3dae2f38e/55fb3e6ab650fc56e363063942600c01961422ae53568933da49186a44176260/independence_wave_status_window-full.svg`.

The GUI MCP does not execute `buttonstate_blendframes.lua`, so it cannot prove live frame playback; the actual frame playback contract was checked through the GFX definition and direct per-frame/sheet DDS decode. The MCP produced four non-blocking `GUI_ANIMATION_STATIC_FALLBACK_MISSING` warnings because it cannot infer the separate static sprite association from a `frameAnimatedSpriteType`. The four static sprites are explicitly registered and the GUI uses the four state-strip sprites as the default readout, so this is an adapter limitation rather than a missing runtime texture. The render also reported unrelated existing Event 006 GUI tab-state, overlap, and fractional clipping diagnostics; no layout or gameplay changes were authorized in this asset audit.

## Review-only timing note

Runtime metadata is consistently 5 FPS, 200 ms per frame, looping, and `play_on_show = yes` on all four animated GFX definitions. The review GIFs contain the correct frame counts and state order but encode 180 ms per frame. GIFs are review-only and do not ship to the runtime consumer; this cadence difference is recorded as `needs_user_review` if exact preview/runtime timing parity is desired, but it does not affect the DDS consumer and was not changed in this audit.

## Exact files changed

The following documentation files were changed or added by this audit:

- `docs/assets/006_independence_wave/animations/manifest.md` corrected `play_on_show` semantics and refreshed the build-report hash.
- `docs/assets/006_independence_wave/animations/animation_build_report.json` corrected all four `play_on_show` values to `true`.
- `docs/assets/006_independence_wave/animations/independence_wave_recognition_seal/brief.md` corrected the runtime animation-mode description.
- `docs/assets/006_independence_wave/animations/independence_wave_dependency_warning/brief.md` corrected the runtime animation-mode description.
- `docs/assets/006_independence_wave/animations/independence_wave_league_charter_activation/brief.md` corrected the runtime animation-mode description.
- `docs/assets/006_independence_wave/animations/independence_wave_formable_eligibility_seal/brief.md` corrected the runtime animation-mode description.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_animation_asset_audit_2026-09-03.md` records this audit.

No GFX, GUI, scripted-GUI, gameplay, localisation, source-art, processed-art, sheet, or DDS file was changed. No staging or commit was performed.

## Status and handoff

Completed: ASSET-040, ASSET-041, ASSET-042, and ASSET-043 static/animated packages, runtime path and case checks, frame-count and frame-rate checks, alpha/anchor/bleed checks, state semantics trace, and native-size visual review.

Needs user review: optional exact GIF preview cadence parity, because the existing review GIFs use 180 ms while the runtime contract is 200 ms; no runtime defect is implied.

Blocked: none.

Orphaned accepted items: none. All four accepted packages have complete source/processed/runtime/fallback/review evidence and all twelve targeted sprite names resolve uniquely.
