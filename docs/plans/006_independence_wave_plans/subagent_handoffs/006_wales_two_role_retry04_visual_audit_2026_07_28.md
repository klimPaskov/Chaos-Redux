# Event 006 Wales two-role portrait audit (retry 04)

Reviewer: Codex independent asset-audit agent `/root/wls_retry04_portrait_audit`.
Review date: 2026-07-28 (Europe/Kyiv).
The reviewer did not produce the source, ImageGen, or processor artifacts. The recorded ImageGen handles belong to the producing run and are distinct from this audit task. No gameplay, GFX, DDS, advisor icon, or portrait file was created or edited by this audit.

## Scope and method

The review covered the immutable archival masters and exact crops in `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/`, the retry-04 raw ImageGen results, deterministic `156x210` candidates, metadata, review sheets, and the canonical role references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/`.

Each candidate was compared against its unchanged source master, exact crop, raw repaint, processed `156x210` PNG, and role-specific references at native size and at a 4x nearest-neighbour enlargement. The review sheet was treated as evidence only; it does not replace the separate source/crop comparison. Male-only compliance, source identity, portrait-family style, crop/provenance chain, and runtime-surface constraints were checked independently.

The later retry-05 David package was also inspected at the parent agent's request as an alternate only. It is not promoted by this record.

## Gate summary

| Subject / package | Role family | Likeness | HOI4 style | Provenance | Overall gate | Runtime disposition |
| --- | --- | --- | --- | --- | --- | --- |
| David Rhys Grenfell, retry 04 | leader | `NEEDS_REVIEW` | `PASS` | `PASS` | `NEEDS_REVIEW` | Do not convert, wire, or shelf-promote. |
| David Rhys Grenfell, retry 05 alternate | leader | `NEEDS_REVIEW` | `PASS` | `NEEDS_REVIEW` | `NEEDS_REVIEW` | Alternate evidence only; do not promote. |
| Major George Frederick Myddleton Cornwallis-West, retry 04 | commander | `PASS` | `PASS` | `PASS` | `PASS` | Parent may proceed to DDS/wiring and flat-shelf promotion. |

Identity is a non-compensable gate. David's good style and complete retry-04 source chain cannot compensate for the remaining likeness uncertainty. George's visual likeness is clear enough to pass, and the package-level `provenance.json`, `PROMPTS.md`, exact-crop metadata, raw hashes, and processor metadata provide the required source-to-raw record.

## David Rhys Grenfell — civic/national-council leader

### Source and artifact evidence

- Identity and role: David Rhys Grenfell (1881–1968), Welsh Labour MP for Gower and Welsh Parliamentary Labour Party chair; plausible Welsh civic/national-council figure for the 1936 setting.
- Archival source: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/source_png/david_grenfell_civic_candidate.jpg` (`620x800`, SHA-256 `5bf5bfe500c724961acd4f56e3057f5a53981fcb779060bf9a79e901a7515749`).
- Decoded immutable master: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/source_master_png/david_grenfell_civic_master.png` (`620x800`, SHA-256 `7b613faad429e155133b60fb9e4c403639281e7054df47f07d5cdd6ea3e10e70`).
- Exact source crop: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/exact_crops/david_grenfell_civic_crop.png` (`530x725`, SHA-256 `55f5cd025f7bfc070f3b821e90bcfabba0ba6daafffcb6d4a161a1a7db73392f`). Its JSON evidence at `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/exact_crops/david_grenfell_civic_crop.json` records crop `(70,65,600,790)`, Pillow decoding, and `decoded_pixels_equal: true`.
- Retry-04 raw ImageGen result: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/imagegen_results/WLS_david_grenfell_identity_preserve_retry_04.png` (`1072x1467`, SHA-256 `ab194a2f47d24c10c14073288d5da20ebbfd3f546e32e5c366daf14c97d1d8c5`).
- Retry-04 processed candidate: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/processed_png/WLS_david_grenfell_identity_preserve_retry_04_156x210.png` (`156x210` RGBA, SHA-256 `41acbe09a7c13450d2de8beee6d7700ec171aeaa552048277230b12ae98778af`).
- Retry-04 processor sheet: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/review/WLS_david_grenfell_identity_preserve_retry_04_review.png` (`1344x464`, SHA-256 `0576912e8c515c455160402adfd162db86b2aa81ecad63334fcea00eb96aa414`).
- Retry-04 metadata: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/metadata/WLS_david_grenfell_identity_preserve_retry_04.json`; processor `the retired portrait-processing utility` v5.0, `role_family: leader`, deterministic output `156x210`, selected references `den_thorvald_stauning.png` and `fin_carl_mannerheim.png`.
- Source-to-raw provenance: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/provenance.json` records the immutable master/crop hashes and rectangle, raw and candidate hashes, ImageGen handle `exec-2cf2eba6-30be-4343-9b21-471431229772`, runtime consumer `GFX_portrait_WLS_independence_wave_national_council`, and the flat-shelf rule. `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/PROMPTS.md` records the single exact-crop ImageGen input and identity-preserving leader prompt.
- Subject ownership: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/ownership_scan.md` reports no David Grenfell owner in installed vanilla, approved reference mods, or Chaos Redux.

Source attribution is Bassano Ltd, National Portrait Gallery record MW64853, dated 1922. The source snapshot records Wikimedia Commons public-domain status; retain the Bassano/NPG credit in durable provenance.

### Visual findings

At native and enlarged views, retry 04 preserves the high side-part/receding hairline, visible right ear, formal bow tie and dark suit, long straight nose, and prominent moustache. The output is clearly a male period portrait and does not introduce text, insignia, modern props, or a second person.

The remaining identity concern is non-compensable: the raw repaint broadens and shortens the source face, enlarges and regularizes the eyes, changes the source gaze/three-quarter geometry toward a more frontal pose, and makes the moustache fuller and more generic. At `156x210` the hairline and moustache are readable, but the face can still read as a generic narrow-moustached official rather than an unambiguous Grenfell likeness. This is why likeness is `NEEDS_REVIEW`, not `PASS`.

Style is `PASS`. The muted charcoal/brown palette, restrained oil/gouache texture, head-and-shoulders framing, clean warm-gray vignette, and readable leader portrait scale fit the selected Stauning/Mannerheim leader family. Style quality does not override the likeness hold.

### Retry-05 alternate

The parent supplied a tighter retry-05 alternate for comparison:

- Raw: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_05/imagegen_results/WLS_david_grenfell_identity_preserve_retry_05.png` (`1074x1465`, SHA-256 `78b5ce9ec06efd96e739097df8f531c5cae2bd3e989fb1e0f0a0397702b93d6`).
- Candidate: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_05/processed_png/WLS_david_grenfell_identity_preserve_retry_05_156x210.png` (`156x210`, SHA-256 `569d5bc458b87b846ada390426f2604885158f5f5905fd313b66c0faf8beca8d`).
- Review sheet: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_05/review/WLS_david_grenfell_identity_preserve_retry_05_review.png` (SHA-256 `d33931fc1f7aaef48692f62145e6e9bda9a473802fba69e53df48881aa00001e`).
- Metadata: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_05/metadata/WLS_david_grenfell_identity_preserve_retry_05.json` (`role_family: leader`, selected refs Stauning/Mannerheim).

Retry 05 is the stronger alternate for source pose and long-nose/side-part geometry, but enlarged inspection still shows eye-size/asymmetry drift and a genericized lower face. It remains `NEEDS_REVIEW`. The retry-05 package has no `provenance.json` or `PROMPTS.md` source-to-raw record, so provenance is also `NEEDS_REVIEW`; it cannot be promoted or wired from this audit.

## Major George Frederick Myddleton Cornwallis-West — mountain commandant

### Source and artifact evidence

- Identity and role: Major George Frederick Myddleton Cornwallis-West (1874–1951), Welsh-born Scots Guards officer; a defensible real Welsh-born military-commandant fit for the existing WLS mountain-commandant token. The source does not prove a specialist Welsh mountain command, so this audit makes no such claim.
- Archival source: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/source_png/george_cornwallis_west_original.jpg` (`1080x1371`, SHA-256 `95068427782c799d86644133e1654b995569aebd51267da10f1d1e1baf16e3e8`).
- Decoded immutable master: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/source_master_png/george_cornwallis_west_commander_master.png` (`1080x1371`, SHA-256 `dba6c6bc4b5a261c4e761323944bc2d504b0f3de992f0d8301f2d28535e5ed2c`).
- Exact source crop: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/exact_crops/george_cornwallis_west_commander_crop.png` (`1000x1280`, SHA-256 `3483095e908cd993d46469d4033aaba4ad8cf7009e3bd7d8ba69f890cea066c4`). Its JSON evidence at `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/exact_crops/george_cornwallis_west_commander_crop.json` records crop `(40,40,1040,1320)`, Pillow decoding, and `decoded_pixels_equal: true`.
- Retry-04 raw ImageGen result: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/imagegen_results/WLS_george_cornwallis_west_identity_preserve_retry_04.png` (`1122x1402`, SHA-256 `23f39f714510df4707d81677ed549420e1d9687a70270c946396e1e6b45bf9c0`).
- Retry-04 processed candidate: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/processed_png/WLS_george_cornwallis_west_identity_preserve_retry_04_156x210.png` (`156x210` RGBA, SHA-256 `9b58faa2262f3182f0e89ac3d8985effd1f76864eb63b25edb498ed7f8a6d04d`).
- Retry-04 processor sheet: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/review/WLS_george_cornwallis_west_identity_preserve_retry_04_review.png` (`1344x464`, SHA-256 `4738cacb12102ef575bb37ba175633bb80f14c0d195ff5b74998134d9489d0a4`).
- Retry-04 metadata: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/metadata/WLS_george_cornwallis_west_identity_preserve_retry_04.json`; processor `the retired portrait-processing utility` v5.0, `role_family: commander`, deterministic output `156x210`, selected references `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png`.
- Source-to-raw provenance: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/provenance.json` records the immutable master/crop hashes and rectangle, raw and candidate hashes, ImageGen handle `exec-2e50c238-d052-4fa7-bc21-35a981f4a840`, runtime consumer `GFX_portrait_WLS_independence_wave_mountain_commandant`, and the flat-shelf rule. `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/PROMPTS.md` records the single exact-crop ImageGen input and identity-preserving commander prompt.
- Subject ownership: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/ownership_scan.md` reports no George Cornwallis-West owner in installed vanilla, approved reference mods, or Chaos Redux.

Source attribution is Henry Walter Barnett, National Portrait Gallery image as recorded in the Commons snapshot, dated between 1900 and 1910. Commons labels the image public domain but carries a PD-Art jurisdiction caution; preserve that uncertainty and the photographer credit in durable provenance.

### Visual findings

At native and enlarged views, retry 04 preserves the unusually high forehead, swept side-part, narrow eyes, long nose, ear shape, jawline, direct gaze, and distinctive curled handlebar moustache. The repaint ages and colours the early-century source without substituting a different face. The collar, shoulder braid, buttons, ribbon bars, and two medal discs remain in the source-visible arrangement; no unsupported modern insignia, text, or extra subject appears.

Likeness is `PASS`: the face remains unambiguously the same man at native `156x210` and at 4x inspection. Style is `PASS`: the full `156x210` commander framing, restrained dark olive uniform, muted painted background, crisp facial planes, and controlled painterly texture fit the Montgomery/Witzleben commander family while keeping the source identity dominant.

## Role-reference evidence

The processor sheets and independent comparisons used only the role-specific canonical references as style controls, never as identity inputs.

### Leader references

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png` (`156x210`, SHA-256 `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`).
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png` (`156x210`, SHA-256 `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`).

### Commander references

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/eng_bernard_montgomery.png` (`156x210`, SHA-256 `39b03871d7451ca96712a5ccf3c056528693f82642776e6c5e297e041943944e`).
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/ger_erwin_von_witzleben.png` (`156x210`, SHA-256 `10f4a1108f9d440213f70fb5802349a2291f298f9d132644241119561577d5b6`).

## Handoff and shelf rules

### George — approved next step

Because George is `PASS` on likeness, style, and provenance, the parent may convert the approved processed PNG with the repository-standard DDS converter and wire only the existing reserved sprite/texture contract:

- sprite: `GFX_portrait_WLS_independence_wave_mountain_commandant`
- DDS path: `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds`
- processed PNG input: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/processed_png/WLS_george_cornwallis_west_identity_preserve_retry_04_156x210.png`

Under the explicit flat-shelf rule, copy the original-size retry-04 repaint master `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/imagegen_results/WLS_george_cornwallis_west_identity_preserve_retry_04.png` directly into `docs/assets/006_independence_wave/portraits_generated_png/` with a unique basename. Do not create a subfolder and do not place the normalized `156x210` PNG in that shelf. The shelf remains evidence-only and does not replace the DDS runtime path.

### David — hold

Do not convert or wire retry 04 or retry 05. Do not copy either repaint master to the flat shelf until a fresh independent likeness review reaches `PASS`. No advisor/high-command/dossier portrait was requested or created for Event 006.

## Remaining risk

The only open gate is David Grenfell likeness. A future candidate must preserve the source eye geometry/asymmetry, narrow facial proportions, gaze, and three-quarter pose more faithfully before promotion. The accepted George portrait still carries the Commons PD-Art jurisdiction caution in its provenance; this audit does not broaden the license claim.

## Parent evidence-shelf disposition

After this audit, the parent retained the retry-04 and retry-05 David raw masters as user-requested original-size evidence copies in the single flat shelf `docs/assets/006_independence_wave/portraits_generated_png/`. This is a shelf-layout exception only: both remain `NEEDS_REVIEW`, neither processed `156x210` candidate is on the shelf, and neither candidate is converted, wired, or admitted to a runtime consumer. The audit's likeness hold and no-DDS/no-wiring disposition remain unchanged.
