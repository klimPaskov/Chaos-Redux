# Event 81 asset production prompt

Use `chaos-redux-event-assets` and read AGENTS.md, the full Event 81 spec package, and the applicable report, news, idea, decision, category-picture, achievement, and super-event references before producing assets. All identifiers in the source specs are working labels, not final localisation. This prompt authorises the specified asset production when it is invoked in a capable implementation environment. It does not claim that production has already occurred.

## Scope and source of truth

Source folder: `docs/specs/081_british_tax_specs/`. Read Parts 1, 2, 5, 7, and 9 in full, then the remaining parts for context. Part 7 owns the 61-image consumer inventory. The separate achievement prompt owns achievement tracking and icon subjects. The super-event prompt owns final quote and audio research.

Produce twelve report images, four news images, one super-event image, seven idea icons, eleven decision icons, two static category pictures, and twenty-four achievement state images. Do not turn the eleven decision icons into eleven permanently visible actions. They support mutually exclusive action families and role-specific categories.

Before adding anything, inspect actual repository consumers, existing Event 81 assets, shared registrations, and family templates. Reuse an existing correct consumer where suitable, but do not mislabel an unrelated existing picture as new approved artwork. Never add icons that have no named consumer.

## Required reference gate

Canonical reference root in the supplied project instructions:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

Resolve the corresponding checkout-relative `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/` path in the active environment. Read its README and CATALOG. Inspect the matching family's contact sheet and native examples. If a category-picture contact sheet is missing, build and label it from actual references, then update the reference README and CATALOG before producing category pictures. Do not infer approval from a plan or from an inaccessible reference path.

The supplied planning archive lacked those visual references. Record an honest blocker if they remain unavailable. A description of the expected style is not evidence of visual comparison.

## Family production

Reports R01 to R12 follow the individual scene directions in Part 7. Generate original fictional period documentary scenes rather than misrepresenting them as archival photographs. Prepare the approved source into the prescribed 210 x 176 tilted photograph card, preserving the intended transparent corners and family tone.

News N01 to N04 use monochrome wide 397 x 153 framing. The scene must remain clear at that size. Avoid readable generated invoices, newspaper headlines, numbers, signatures, and tiny labelled maps.

SE01 uses 457 x 328 and presents the mature international revenue order. Coordinate image timing and thematic emphasis with the super-event researcher. The image can be completed independently of final quotation selection, but final package acceptance requires both to fit.

Seven idea icons are separate original subjects: three taxpayer regime states, three British revenue regime states, and one temporary pressure or emergency state. Final size is 64 x 64. The persistent taxpayer idea changes effects and tier art without accumulating a national spirit per tax channel.

Eleven decision subjects are industrial recovery, consumer assessment, external reform, consolidation, hostile exit, petition, pressure, emergency assessment, enforcement, settlement, and partner assistance. Final size is 32 x 32. Generate and compose for the decision family. Do not resize idea art into these consumers.

Both category pictures are static. Confirm the exact native consumer and final dimensions from the matching reference family, using 114 x 101 only as the planning reference anchor. The resistance category depicts domestic economic authority being recovered. British administration depicts central collection. Do not create an interactive GUI or a GUI asset set under this prompt.

## Achievement assets

Use one new original subject for each of the eight proposed achievement IDs in Part 9. Produce the completed, grey, and not-eligible states through the current achievement pipeline. Inspect the current immutable templates under the skill's `icons/achievements/template/` family and the actual processing script instead of relying on older overlay-path references elsewhere.

Use `process_achievement_icons.py` according to the current skill. Final files are placed directly under `gfx/achievements/` as `<achievement_id>.dds`, `<achievement_id>_grey.dds`, and `<achievement_id>_not_eligible.dds`. Do not hand-paint different subjects for the three status variants or distribute them into undocumented subfolders.

## Workspace and runtime handoff

Use `docs/assets/081_british_tax/` for provider originals, working crops, manifests, source-rights notes, and review comparisons while the work is incomplete. Preserve blocked evidence rather than deleting it to look finished. Before complete delivery, promote approved runtime assets and durable provenance, verify that no runtime consumer references the temporary workspace, and clean the workspace as required by the skill.

Use `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` for the required conversion workflow. Validate dimensions, alpha, compression, filename consistency, and final-size readability. Create a contact sheet of every final consumer, including all achievement states, and inspect it visually. A successful conversion process alone is not visual acceptance.

For each asset, provide its source mode, actual source or generation record, matching reference family, intended consumer, final path, native dimensions, alpha treatment, rights status where relevant, and approval state. Hash-aware promotion must prevent an older source or unapproved revision from replacing the accepted runtime candidate.

The main implementation agent owns final `.gfx` wiring and consumer integration unless explicitly delegated. Asset workers must stay within bounded production paths. Do not edit the event framework, event history, settings, shared super-event registry, or unrelated UI.

## Completion conditions

Every planned visible consumer must have correct art and a documented source mode. All icons must be legible at native size and visually belong to their family. Missing references, unresolved rights, incomplete achievement variants, missing consumer wiring, and an unreviewed final contact sheet are blockers. Report them plainly instead of supplying placeholder art or claiming a complete asset package.
