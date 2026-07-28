# Wales two-role portrait repaint retry 04

This package contains two source-locked HOI4 portrait repaints for the existing WLS national-council and mountain-commandant consumers.

The immutable archival masters and exact equality-proven crops remain in `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/`. The raw ImageGen outputs are retained under `imagegen_results/`. The deterministic processor outputs are under `processed_png/`, and the processor review sheets are under `review/`.

The raw masters are original-size RGB PNGs. The processed candidates are deterministic 156x210 RGBA exports and are not copied to the flat pre-resize shelf. The flat shelf rule is one directory only: `docs/assets/006_independence_wave/portraits_generated_png/`, with original-size masters directly in that directory and no child folders.

## Current gate status

The processor runs completed as `candidate_requires_visual_approval`. The independent audit `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wales_two_role_retry04_visual_audit_2026_07_28.md` passes George Cornwallis-West for likeness, HOI4 commander style, and provenance. His original-size raw master is promoted to the flat shelf and his normalized candidate is wired to the existing WLS commander DDS consumer. David Grenfell remains `NEEDS_REVIEW` for likeness; his raw retry-04 master is retained in the flat shelf as an evidence copy, but it is not converted or wired. No Event 006 advisor icon or dossier derivative is part of this package.

## Candidates

| Consumer role | Raw ImageGen result | Raw dimensions / SHA-256 | Processed candidate | Candidate SHA-256 |
| --- | --- | --- | --- | --- |
| David Rhys Grenfell, civic national council | `imagegen_results/WLS_david_grenfell_identity_preserve_retry_04.png` | `1072x1467` RGB / `ab194a2f47d24c10c14073288d5da20ebbfd3f546e32e5c366daf14c97d1d8c5` | `processed_png/WLS_david_grenfell_identity_preserve_retry_04_156x210.png` | `41acbe09a7c13450d2de8beee6d7700ec171aeaa552048277230b12ae98778af` |
| Major George Frederick Myddleton Cornwallis-West, mountain commandant | `imagegen_results/WLS_george_cornwallis_west_identity_preserve_retry_04.png` | `1122x1402` RGB / `23f39f714510df4707d81677ed549420e1d9687a70270c946396e1e6b45bf9c0` | `processed_png/WLS_george_cornwallis_west_identity_preserve_retry_04_156x210.png` | `9b58faa2262f3182f0e89ac3d8985effd1f76864eb63b25edb498ed7f8a6d04d`; final DDS `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` SHA-256 `63e974a6d95117e3c37efca01884a3bdfec1da190b25617164ad177934c0cd94` |

## Prompt and source lock

The exact prompts used for the two source-locked edits are recorded in `PROMPTS.md`. Image 1 in each edit was the corresponding immutable exact crop, not a generated substitute. The edits preserve the named man's identity, pose, facial hair, age, and source-visible clothing while applying the HOI4 painted leader or commander treatment. Canonical vanilla portraits were used only for style-family comparison by the deterministic processor.
