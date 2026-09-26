# GUI source-fixture qualification

Disposition: implemented for the supported source-render and primary hit-region matrix; unsupported interaction and engine evidence remains unresolved.
Acceptance basis: the user's request to fix the MCP scenario contract and replace unproved visual claims with source-backed evidence.
The parent completed the closing checks after the audit worker produced the requests and artifacts.
No gameplay, GUI, or localisation source was changed by this qualification.

## Evidence

The current run uses canonical MCP commit `d04d7eb51011461b3bb646946805a13bf5c73d2f`, server version `3.5.0`.
[The run manifest](current_source_6c3a2036_4c937887/run_manifest.json) records the actual initialization, requests, scenario identities, diagnostics, source revisions, and artifact reads.
The twelve render calls cover fifteen declared cases at 1280×720/1.0, 1920×1080/1.0, and 1920×1080/1.25, producing 45 scenario images.
Every call returned `GUI_RENDERED`; all 85 MCP artifact reads passed their expected byte count and SHA-256 checks.
[Parent verification](parent_final_review/verification.json) independently verifies the saved image hashes, output dimensions, window containment, requested primary resolution/scale, and primary hit-region bounds.
The parent visually reviewed the normal, hover, unavailable, empty-list, long-value, closed-site, and Records views at native and 125% scale.
No clipping, overflow, or misplaced control was found in those reviewed images.
[Cross-resolution comparison](parent_final_review/cross_resolution_pixels.json) confirms all fifteen window crops at scale 1 have identical pixels across the two viewport sizes.
The contact sheets are browsing aids; original full and cropped images remain in the run directory.

The GUI, scripted-GUI, and UI-localisation files remained unchanged before and after every render:

| Source | SHA-256 |
| --- | --- |
| `interface/camp_repression_ledger.gui` | `6c3a20368b6e2175aa0d2024098288a0bc2a97ec549c90a73058619e99946d33` |
| `common/scripted_guis/camp_repression_ledger_scripted_gui.txt` | `4c937887e349decd955e632c59bd119873cd1cced761f5995f5b698fee176dc2` |
| `localisation/english/camp_administration_ui_l_english.yml` | `4aac46621cd516cdbfa6ed7b45754459a4dc80a8130868bad4e515be859cc445` |

Aggregate source revisions differ because the shared workspace changed outside those three files.
Each call retains its own revision; this is not a frozen whole-workspace or before/after gameplay comparison.
The first run in the parent directory mixed GUI revisions and is retained as historical provenance, not current-source acceptance.

## Click geometry and state evidence

The active picker control `camp_admin_option_role_killing` is clickable, visible, unclipped, and in hover state at all three targets.
Its rectangles are `(648,421,398,48)`, `(968,601,398,48)`, and `(970,616.25,497.5,60)` respectively.
Those bounds match the visible control face and scale with the interface.
All primary clickable controls have positive viewport-contained rectangles and no disabled reason or click-through flag.
The twelve primary overlays also distinguish disabled controls from active hit regions.
Related-case images establish visible appearance; they are not independent click-execution receipts.

The custody and labor picker controls can look nearly unchanged when disabled because their native shader only desaturates an already grey texture.
Their saved layout correctly records `state=disabled`, `clickable=false`, and the source `Disable` shader.
No invented darkening was applied to make the example look different.

## Unresolved coverage and limits

- The source binds `pdx_tooltip`, but the renderer does not draw native tooltip popups.
- `click_to_front` is preserved but not rendered; actual window raising is unproved.
- Two `attached_scrollbar` consumers report no active clipped background boundary; native thumb/drag behavior remains unproved.
- Selected-location fixtures do not declare numeric state-controller facts, so their site work/purpose actions remain disabled in the model; active contextual-action behavior is not passed.
- Primary hit regions are covered at all targets, but every related state does not have a separately reviewed click-region overlay.
- The MCP does not execute engine clicks. Actual availability, costs paid, transfers, delayed callbacks, and timer receipts require runtime evidence.
- The user reported no saves available. No game launch, save search, or game-log request was performed.

These limits prevent a complete engine interaction or 99.9% visual-equivalence claim.
They are explicit capability/evidence boundaries, not fabricated successful cases.
The qualification found no new confirmed renderer defect in the supported source-fixture views.
