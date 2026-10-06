# Event 015 Advisor Portrait Framing Handoff

Date: 2026-10-06.

Status: parent accepted all sixteen portraits on 2026-10-06; the approved candidates are installed and hash-verified at the existing runtime paths.

## Authorized Scope

The cross-cutting plan at C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md records that the sixteen 65×67 Event 015 advisor cards have undersized faces and pseudo-writing on a paper note.

The authorized target is a plain framed head-and-shoulders portrait with a larger readable face and no lettering, while preserving the existing advisor IDs, sprite aliases, character references, and runtime texture basenames.

No character identity, traits, gameplay, localisation, event, focus, decision, country, or unrelated interface files were edited.

## Source Mode and Provenance

Historical Event 015 portrait handoffs describe sixteen independent fictional ImageGen subjects, but the original high-resolution package at docs/assets/015_utopia_manifesto/route_identity_2026_07_14/ is absent from the current worktree.

The original 65×67 source PNG and DDS files are preserved under docs/assets/gfx_fix_portraits_2026-10/source_png/ and source_dds/ and were used as each subject’s identity anchor for fresh native ImageGen work.

Before promotion, all sixteen archived source DDS hashes matched the July-migration runtime files; those source files are retained as original lineage, and the current runtime DDS hashes now match the parent-approved candidates.

The previous full-resolution test at docs/assets/gfx_fix_portraits_2026-10/imagegen_master_png/advisor_utopia_manifesto_interpreter.png remains untouched and unselected because it changed the interpreter’s hairstyle.

The new candidate masters were produced through native ImageGen using each portrait’s own source card; the full prompt templates, input mapping, candidate lineage, correction notes, and generated output identifiers are in docs/assets/gfx_fix_portraits_2026-10/metadata/imagegen_prompts.md.

The result masters are fresh fictional ImageGen edits, are not represented as the missing July masters, and were accepted by the parent on 2026-10-06.

## Installed Vanilla References Inspected

The installed vanilla sprite GFX_idea_generic_political_advisor_europe_1 is registered in interface/ideas.gfx at lines 961–963 and uses gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds, a 65×67 advisor card.

The installed vanilla sprite GFX_idea_generic_political_advisor_female_europe is registered in interface/ideas.gfx at lines 4542–4544 and uses gfx/interface/ideas/idea_generic_political_advisor_female_europe.dds, also 65×67.

Both installed DDS images were decoded and viewed directly; their decoded RGBA pixels exactly match the corresponding skill reference PNGs in .agents/skills/chaos-redux-event-assets/assets/gfx_references/portraits/advisors/.

The canonical advisor template and minister portrait base include the note overlay, while the inherited Event 015 cards bake the note and portrait together; no clean separable frame remains in the current package.

The minister portrait background reference was consulted only after the vanilla card inspection and informed the frame shape and transparent outer corners; no reference-shelf artwork was copied or shipped.

## Candidate Outputs

Sixteen high-resolution framed master PNGs are archived in docs/assets/gfx_fix_portraits_2026-10/imagegen_master_candidates/.

Sixteen aspect-preserving 65×67 RGBA PNG candidates are in docs/assets/gfx_fix_portraits_2026-10/processed_png/.

Sixteen 65×67 DDS review candidates are in docs/assets/gfx_fix_portraits_2026-10/candidate_dds/, with decoded DDS PNGs in candidate_decoded_png/.

The native-size old/new comparison sheet is docs/assets/gfx_fix_portraits_2026-10/contact_sheets/parent_review_native_old_new.png.

The nearest-neighbour 4× old/new comparison sheet is docs/assets/gfx_fix_portraits_2026-10/contact_sheets/parent_review_4x_old_new.png.

Per-portrait image paths, dimensions, crop rectangles, alpha-corner values, source/runtime hashes, candidate hashes, and review state are in docs/assets/gfx_fix_portraits_2026-10/metadata/portrait_candidate_manifest.json.

## Processing and DDS Evidence

Every generated master was center-cropped without aspect distortion to the 65:67 consumer ratio, then resized to 65×67 with Pillow LANCZOS while preserving alpha.

All processed PNGs are RGBA at exactly 65×67 and have alpha 0 in all four canvas corners.

All candidate DDS files were produced with .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py at 65×67.

The converter used its FFmpeg BGRA fallback because DirectXTex texconv was not present on PATH; output is one-mip BGRA/B8G8R8A8_UNORM with a 17,548-byte DDS per portrait.

All sixteen v1 DDS candidates were decoded with Pillow and their decoded RGBA pixel arrays exactly matched their processed PNG inputs; the two v2 DDS replacements passed the same round-trip check.

The post-copy runtime hashes, DDS round-trips, stable .gfx aliases, and character consumers are recorded in docs/assets/gfx_fix_portraits_2026-10/metadata/runtime_install_validation.json.

## Portrait Wiring

The existing sixteen GFX_portrait_utopia_manifesto_<advisor>_small sprite definitions remain in interface/015_utopia_manifesto.gfx and continue to point at gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_<advisor>.dds.

The existing sixteen civilian small-portrait references remain in common/characters/015_utopia_manifesto_characters.txt and match those sprite aliases.

No .gfx or character wiring was changed; all sixteen approved DDS candidates now replace the previous runtime portraits at the same stable paths.

## Independent Review and Replacement State

The two contact sheets show the old installed cards beside the processed new candidates at both native size and 4×.

The parent reviewed the v1 and v2 sheets and accepted all sixteen candidate likenesses after the requested Interpreter and Contract Broker corrections.

The Constitutional Jurist first generated candidate introduced round glasses that were not clear in the source, so a focused edit removed the glasses before framing.

The Steward of Service first generated candidate changed the older fair-skinned man’s presentation, so a focused edit restored the source-visible age, receding hair, glasses, and green sweater before framing.

The parent reviewed the 4x sheet and accepted the painted frame family as coherent.

The parent accepted all sixteen rows; per-card identity, style, and framing verdicts are recorded in the v2 manifest.

## Skipped Checks and Blockers

No HOI4 runtime or desktop session was launched; live-game validation remains with the user under repository policy.

No portrait wiring edit was required because the existing sprite aliases and character references already point to the stable runtime basenames.

The missing historical high-resolution masters limited direct likeness comparison, but the parent reviewed both source/candidate sheets and accepted all sixteen current portraits.

No commit was created because the parent owns the commit.

## Reference Evidence

Direct installed-vanilla DDS paths, sprite definitions, dimensions, decoded-pixel equality, and hashes are recorded in docs/assets/gfx_fix_portraits_2026-10/metadata/vanilla_reference_evidence.json.

The candidates are fictional native ImageGen outputs; no Internet source, archival likeness, or real-person attribution applies.

## Parent Review and v2 Candidate Update

On 2026-10-06 the parent reviewed the v1 sheets and accepted the painted family style, plain framing, 65×67 composition, and removal of all note writing.

The parent requested a pulled-back hairstyle and warmer source complexion for the Public Interpreter, a rounder warmer face for the Contract Broker, and a source-eye inspection for the Chief Surveyor before deciding whether eyewear is present.

The parent-approved current set selects the v2 Public Interpreter master, processed PNG, and DDS with corrected pulled-back hair and warmer complexion; its v1 candidate remains archived.

The parent-approved current set selects the v2 Contract Broker master, processed PNG, and DDS with the corrected rounder warmer face; its v1 candidate remains archived.

The Chief Surveyor's 65x67 source crop does not establish eyewear with confidence, so no glasses were added; the nearest-neighbour detail at docs/assets/gfx_fix_portraits_2026-10/evidence/source_details/chief_surveyor_eyes_nearest_20x.png and its crop coordinates are recorded in the v2 manifest.

The v2 native and nearest-neighbour sheets are docs/assets/gfx_fix_portraits_2026-10/contact_sheets/parent_review_native_old_new_v2.png and parent_review_4x_old_new_v2.png.

The v2 per-card identity, style, framing, source-trait, and DDS status records are in docs/assets/gfx_fix_portraits_2026-10/metadata/portrait_candidate_manifest_review_v2.json.

The two v2 DDS files decode pixel-for-pixel to their 65x67 PNG candidates and are installed at their stable runtime basenames. All sixteen installed runtime DDS files match the approved candidate hashes and decode pixel-for-pixel to the corresponding PNG.

The parent accepted the v2 set on 2026-10-06. Chief Surveyor eyewear remains indeterminate from the source card, and no uncertain trait was added.

## Workspace Tracking Note

The docs/assets tree is ignored by .gitignore at line 80, so the prompt, source, candidate, and review evidence remains in the shared workspace but is not included in normal Git status. The parent decides which ignored evidence to force-add during the commit.
