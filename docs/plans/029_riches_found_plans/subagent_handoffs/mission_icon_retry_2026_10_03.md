# Event 029 mission icon audit and retry — 2026-10-03

Scope is limited to the nine Riches Found mission icons. This handoff is not an Event 029 package-completion claim.

Eight pre-existing mission icons pass the individual visual, alpha, dimensions, wiring, and DDS roundtrip audit. Parent accepted evacuation candidate 02 and copied its final DDS to the existing runtime path; the current runtime and evidence DDS are byte-identical and the icon status is wired.

## Consumer and references

The current source roots are docs/assets/029_riches_found/source_png/, docs/assets/029_riches_found/processed_png/missions/, and docs/assets/029_riches_found/final_dds/gfx/interface/decisions/029_riches_found/. The runtime directory is gfx/interface/decisions/029_riches_found/. The asset subagent made no runtime writes; the parent subsequently synchronized the accepted DDS and archived the previous runtime file.

The active consumer is common/decisions/029_riches_found_decisions.txt. The nine mission IDs and their current icon assignments are recorded in the status table below. The sprite registrations remain in interface/029_riches_found.gfx; the evacuation sprite at line 267 still points to gfx/interface/decisions/029_riches_found/mission_riches_found_evacuate_workforce.dds.

The canonical reference root was .agents/skills/chaos-redux-event-assets/assets/gfx_references/. I inspected its README.md and CATALOG.md, then opened icons/missions/contact_sheet.png before opening all five canonical mission reference PNGs individually. The catalog identifies the Mapuche mission symbol and four counter-infiltration mission-state references as Vanilla HOI4, each 33x32, with their installed DDS source paths.

The installed interface/decisions.gfx defines GFX_decision_CHL_ibanez_cracking_down_on_mapuche_organizations_mission and the four generic counter-infiltration mission-state sprites. The four installed counter-infiltration DDS files were header-checked at 33x32. Event 029's existing mission textures are 32x32, which is the exact retained consumer size for this handoff.

## Individual nine-row status and hashes

Every source PNG, processed PNG, and decoded runtime DDS image was opened individually. The refreshed contact sheet adds a source thumbnail, native-size processed image, dark/light alpha contrast view, 4x smooth enlargement, and DDS decode for each row; it is review evidence, not final art.

All nine source PNGs are RGBA with RGB channel extrema 0–255 and alpha extrema 0–255. Alpha counts below are transparent / partial / fully opaque pixels. The eight pre-existing sources have one bottom-left alpha=1 pixel and zero alpha in their other three corners; the saved provenance records no background-removal fallback, but their original prompts were not retained, so the original native-transparency request cannot be independently verified. The selected evacuation source has four zero-alpha corners and one isolated alpha=1 pixel at (0,809); the processed crop excludes that stray edge pixel without changing the retained source.

Source filenames are docs/assets/029_riches_found/source_png/<asset>.png. Processed filenames are docs/assets/029_riches_found/processed_png/missions/<asset>.png. Final DDS filenames are docs/assets/029_riches_found/final_dds/gfx/interface/decisions/029_riches_found/<asset>.dds. Runtime filenames are gfx/interface/decisions/029_riches_found/<asset>.dds. The current parent audit confirms all nine runtime DDS files are byte-identical to their evidence DDS files and their decoded pixels equal the processed PNGs.

| Asset | Mission consumer line | Source alpha transparent / partial / opaque | Source PNG SHA-256 | Processed PNG SHA-256 | Evidence DDS SHA-256 | Runtime DDS SHA-256 | Status |
|---|---:|---:|---|---|---|---|---|
| mission_riches_found_secure_rush | 7184 | 643890 / 927931 / 695 | 692a54ba0d102a1302a6de9be9c8fbcd92a9807cab093ae447ae03c736c8210d | 0a11b8863185a2463e92a725b18786253b4b4f30089540ff8980e4f2039e88e1 | 21095d5a8b10cddf59dfffad4f76d76d8b7d540996029c56d9e52a2a43a259d7 | same as evidence | pass |
| mission_riches_found_open_railhead | 7288 | 698685 / 872861 / 970 | 36812df934908bb3fa40d26208f6c57f2e6bcca7bbb2a29d00d8a93c159de820 | 4c637352538828c030372fa35ac74cf7bc1801ccd771611f5966912ae2d10ec7 | 8b60e7d7e4ecbd87b2a5dfdb664dbe63052572f05b115040018e32a99a43d5a7 | same as evidence | pass |
| mission_riches_found_protect_pay_train | 7388 | 522790 / 1049586 / 140 | dc80cae974ac406950efdb5a7dfcc6228e7436f9b3240d55633bba62f0d508f4 | 1d97205f397647b5f2e61639dd6c059eccac5847e8e635adfd64e1662fa76c05 | 392c1de8c9d62ffcbbd177fd351446637796f789f55fa6da86e4454629495702 | same as evidence | pass |
| mission_riches_found_break_claim_war | 7510 | 796026 / 775821 / 669 | 3b5997101a43f21010da0724e47c6dfdda59d3accd478a6b7decb0e5c0dc6869 | 43ee8d343bc4d983d295c1c0c4928fe8caf1bd3078071520007e09828cc54464 | 625582b3a9de039a79a5195f387f833ce0f76dc55cd4c906a8f98aba54a14958 | same as evidence | pass |
| mission_riches_found_restore_shaft | 7611 | 476170 / 1096099 / 247 | b67c0a11105db77fa59ca6781cbd787b9029d548117a480dd35f91d9cc306e40 | 046c55ca7e6a7f661e3907864ba6d52af1601bf98e611910d0ebeb8c96c30644 | 8e49b1a9deecd94b003629cfeb1d1debc37952f7a465402e8ae9d25aed4d040c | same as evidence | pass |
| mission_riches_found_hold_mine | 7717 | 600952 / 970785 / 779 | 1434e1e9cd1e888b25b59016d8afe54a750350b8f25dbe95249c6ad4c3c84042 | 0ecf9362f4d198fcde5893d102bca2ec715033f6ce59cb5fa80786df72f11113 | 3e9fcb9ac478e25f27611bc55e1b9ffa8cf157f7ab3ec2fdbfbc268882fc445a | same as evidence | pass |
| mission_riches_found_public_settlement | 7817 | 643800 / 928176 / 540 | 2aa7530efdf9914ffabb39397a50e38f83273b18f780504d4ae39414a73f32c7 | c1fc2f0f8ebced3a93577ebfe7e97841efa23616a06f87b6d1e98d339d06ef19 | 2c61dfad79035d84b0d4b811152d7369f76e5fb0ad10629ef27e9a32608de50d | same as evidence | pass |
| mission_riches_found_audit_concession | 7922 | 562334 / 1009358 / 824 | ab604f24518038ae45c19bcfcf3358d6ee090ec8f66e48d2b3edd7a62b6c9926 | a28f2b2299a63dd3398f963e92cd3345febb59cb00d77937264e14ad9c1ef8b8 | e02dda20136460dc67eee0e652532c8b386e6e28c1025958d88a519897f22c0b | same as evidence | pass |
| mission_riches_found_evacuate_workforce | 8026 | 809436 / 763009 / 71 | 5f74115a60cff9dc5391deaf2b6a0fc88b2176d07666269867a66257fff443cd | bf09570c7b647a99e93c42593aba92f31fe716338025f9e5b6a6f79b6ab2c5a1 | c30eb96b9ed44838e4db5a118a61a6a49d8432400d94499e4a66709ae98df1e2 | c30eb96b9ed44838e4db5a118a61a6a49d8432400d94499e4a66709ae98df1e2 | wired; parent accepted |

Every evidence DDS strictly decodes as one-level uncompressed BGRA, 32x32, 4,224 bytes, with preserved transparency. All nine evidence DDS decodes are pixel-identical to their processed PNGs and byte-identical to the current runtime DDS files. The parent's current audit confirms all nine runtime DDS roundtrips match their decoded PNGs individually. The updated icon audit summary has duplicate_groups = [] and cross_family_consumer_reuse_flags = [].

The accepted DDS decode is docs/assets/029_riches_found/notes/decoded_icon_dds/mission/mission_riches_found_evacuate_workforce.png. The earlier candidate decode remains at docs/assets/029_riches_found/notes/decoded_candidate_dds/mission/mission_riches_found_evacuate_workforce.png; both match the processed PNG and synchronized runtime DDS.

## Evacuation candidate lineage

The September 1 notes/icon_artist_audit.json and September 4 notes/icon_validation_report.json recorded pixel-identical decision-to-mission reuse. Those dated reuse claims are historical and superseded. The current notes/icon_audit_summary.json is dated October 3 and records no duplicate groups or cross-family consumer reuse flags. The October 3 user brief required separate original mission-family artwork; parent accepted the new art, copied it to the mission runtime path, and archived the former runtime DDS at docs/assets/029_riches_found/rejected_pre_audit/mission_evacuation_runtime/mission_riches_found_evacuate_workforce_old_decision_reuse.dds with SHA-256 6e836c5356794138ac46458f9fa5aa8317637827fbf27956ef45f556720c40d8. The decision source, preview, DDS, and runtime decision icon remain unchanged.

Candidate 01 was generated with built-in ImageGen and requested native transparency. Its source is preserved as docs/assets/029_riches_found/source_png/mission_riches_found_evacuate_workforce_candidate_01_rejected.png with SHA-256 9df9b2c783807d5f861b25eb111783c6a7a93bb3d0f562b94ec9240f65182e37. Its 32x32 trial preview SHA-256 was 3832e691475d063f5929ba339ed7894a40781a97569ad5365cbb3bf1aa50c1dc and its trial DDS SHA-256 was b5c44060c10c5d6768cb63f5761df9349382ed2ffd549b6717ca31b9a32c1213. I rejected it after opening its 32x32 preview and decode because the dark details merged into an indistinct mark.

Candidate 01 was saved by built-in ImageGen as C:/Users/klimp/.codex/generated_images/01a10134-2858-7400-b764-1e2281255b39/exec-c41d5a00-85ac-4f37-868e-fe40e54fdad7.png. Its retained source is 1254x1254 RGBA with 1086089 alpha-zero / 486170 partial / 257 fully opaque pixels, four zero-alpha corners, and one detached alpha=1 pixel on the left edge. The initial call set transparent_background=true; no background-removal fallback was used.

The exact Candidate 01 prompt was:

~~~text
Use case: stylized-concept
Asset type: Original Hearts of Iron IV mission icon, processed to a 32x32 transparent DDS
Primary request: Create a compact, clearly readable symbol for evacuating a workforce from a dangerous mine. Center one small period mine cart carrying two simplified helmeted worker silhouettes, rolling outward from a timber-braced mine exit; place one small hanging lamp above the exit. The outward cart and mine exit must communicate evacuation at a glance.
Input images: Image 1: style/reference-family anchor only, canonical vanilla mission icon; transfer only its compact aged HOI4 texture, dark edge treatment, muted historical palette, and small-icon visual density. Do not reproduce its subject, exact shapes, arrangement, or any copied detail.
Style/medium: Aged HOI4 military-artifact icon, painterly but silhouette-led, weathered dark iron and timber with restrained warm lamp light, subtle shadow.
Composition/framing: Single centered compact emblem-like object group, nearly square footprint with clear transparent breathing room; designed to remain legible at 32x32. Keep the cart, exit, and lamp as three simple connected masses, with strong contrast and no fine interior detail.
Scene/backdrop: No scene canvas. The unused canvas must be genuinely transparent.
Constraints: Original mission-family artwork, independent from every decision icon. Preserve a clean, complete silhouette and real transparent pixels around it. No text, lettering, numbers, portrait or readable face, border, badge frame, full background, square backing, fake checkerboard, chroma key, smoke cloud, extra tools, flags, modern equipment, or unrelated objects.
~~~

Candidate 02 is the parent-accepted source. Built-in ImageGen returned C:/Users/klimp/.codex/generated_images/01a10134-2858-7400-b764-1e2281255b39/exec-b788dd5b-7839-4a49-9289-3a75a1482105.png; the retained workspace copy is docs/assets/029_riches_found/source_png/mission_riches_found_evacuate_workforce.png. Both have SHA-256 5f74115a60cff9dc5391deaf2b6a0fc88b2176d07666269867a66257fff443cd.

The selected mission source, processed preview, and decoded candidate DDS were each pixel-compared with the corresponding evacuation decision image; all three comparisons are different.

The initial ImageGen call set transparent_background=true and used the canonical Mapuche mission icon only as a style-family anchor. The full submitted prompt was:

~~~text
Use case: stylized-concept
Asset type: One original Hearts of Iron IV mission icon, to be processed to a 32x32 transparent DDS
Primary request: Create a bold, immediately readable symbol for evacuating mine workers from a dangerous mine. Make one small iron mine cart with two simple cream-colored helmet silhouettes inside roll out of one dark timber mine exit, with one bright amber lamp above the exit. The cart is the dominant shape and the open exit is clearly behind it.
Input images: Image 1: style/reference-family anchor only, canonical vanilla mission icon; use only its compact aged HOI4 finish, muted historic palette, dark edge treatment, and native icon density. Do not copy its symbol, shape, subject, or composition.
Style/medium: Painterly HOI4 military-artifact icon with broad color masses, a dark charcoal outline, muted iron and timber, cream highlights, and one amber lamp. Simple enough to read at 32x32; polished illustration rather than a diagram or primitive vector.
Composition/framing: Centered square emblem footprint occupying most of the canvas with a small transparent margin. Use only four bold visual masses: mine opening, cart body, two helmet shapes, lamp. Keep forms thick, separated, and high contrast. No tiny detail.
Scene/backdrop: No scene canvas; genuinely transparent unused canvas.
Constraints: Original mission-family artwork, independent from all decision icons. No portrait or face detail; the workers are only simple helmeted silhouettes. No surrounding rock pile, foreground track network, smoke, extra props, words, letters, numbers, frame, badge, opaque square, checkerboard, or chroma background. Preserve complete edges and true alpha.
~~~

The candidate source is 1254x1254 RGBA. Its RGB channels each span 0–255; alpha has 809436 zero, 763009 partial, and 71 fully opaque pixels, with all four canvas corners at alpha zero. It has one detached alpha=1 pixel at x=0,y=809; no chroma background, checkerboard, matte, or background-removal step was used.

Processing retained the source unchanged. A threshold-4 alpha crop used bounds (157,116,1100,1153), then Lanczos scaling fit the 943x1037 crop into 27x30 and placed it at (2,1) on a transparent 32x32 canvas. The crop excludes only the detached alpha=1 edge speck; it does not remove or repaint the subject.

The selected processed PNG has alpha counts 304 zero / 645 partial / 75 fully opaque and SHA-256 bf09570c7b647a99e93c42593aba92f31fe716338025f9e5b6a6f79b6ab2c5a1. The candidate DDS was created with .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py and has SHA-256 c30eb96b9ed44838e4db5a118a61a6a49d8432400d94499e4a66709ae98df1e2. Its decoded PNG hash equals the processed PNG hash, proving pixel-exact roundtrip.

## Files changed and parent handoff

The parent accepted Candidate 02 and synchronized its final DDS to runtime after the subagent staged the source, processed PNG, evidence DDS, decode, and refreshed mission contact sheet. The previous runtime DDS is retained at the rejected-pre-audit archive path listed above.

This documentation closeout changed no runtime GFX/DDS, gameplay, decision, mission, or localization file. No other event asset family was touched, and Hearts of Iron IV was not launched.

The parent has visually accepted the selected source, native 32x32 preview, and decoded DDS, copied the accepted DDS to the existing runtime path, and archived the replaced DDS. No sprite-name or GFX path change was needed; the evacuation icon is wired.

## Limitations

The original ImageGen prompts for the eight pre-existing mission sources were not retained in their prior provenance records. Their source PNGs are RGBA with transparent unused canvas, the prior record documents no fallback, and their visual, alpha, dimensions, consumer wiring, and DDS roundtrip were checked here, but their initial transparency-request prompts cannot be independently verified. The broader Event 029 visual asset package remains incomplete; this mission-only handoff is not a package-completion claim.

The prior icon_provenance.md mission row and contact sheet were not part of the user-specified documentation edit list and remain pre-synchronization records. The current wired status is recorded in this handoff, icon_manifest.md, manifest.md, gfx_handoff.md, and icon_audit_summary.json.

No background-removal, chroma-key, or opaque-canvas fallback was used.
