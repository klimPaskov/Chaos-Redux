# Event 014 Asset Source Research Handoff

Date: 2026-07-11

Subagent mode: read-only asset/source audit. The only writes are this handoff and docs/plans/014_cannibalism_plans/014_live_asset_gap_map.md.

## Completed scope

- Read AGENTS.md and the complete chaos-redux-subagents, chaos-redux-event-assets, and chaos-redux-frame-animation skills.
- Consulted the required offline HOI4 wiki snapshot, including graphical asset, interface, scripted-GUI, achievement, focus, and technology guidance, plus relevant vanilla documentation and live vanilla/repo format precedents.
- Read the complete Event 014 specification package and the current docs/assets/014_cannibalism/manifest.md.
- Audited current runtime files, source packages, image dimensions and compression, sprite registries, flags, portraits, achievements, ideas, report/news images, animation packages, dirty-worktree deletions, and relevant Git history.
- Produced an authoritative requirement-to-file map with stable filenames, dimensions, formats, generation batches, dependency gates, spoiler constraints, and runtime owners.

## Files written

- docs/plans/014_cannibalism_plans/014_live_asset_gap_map.md
- docs/plans/014_cannibalism_plans/subagent_handoffs/event014_asset_source_research_2026-07-11.md

No gameplay, GFX, GUI, localisation, spreadsheet, asset binary, or manifest file was edited. No file was generated, converted, renamed, restored, deleted, or staged.

## Principal findings

1. No Event 014 visual family is currently complete and wired under the current specification.
2. Eleven old report DDS and one old news DDS survive in the runtime folder, but none is accepted against the current exact report/news directions. The two original_unused files are compressed DXT and cannot be finals.
3. The Event 014 super-event folder is absent. gfx/super_events/002_zombie_outbreak/super_event_wendigo_hannibal.dds is misplaced and visually wrong for the current transformed-leader brief.
4. The protected gfx/leaders/014_cannibalism/hannibal.dds is present and its SHA256 exactly matches 5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88. It must remain untouched. It is not current-spec completion proof.
5. The retained hannibal_wendigo.dds lacks facial continuity and the required cold body-horror treatment. Both current static portraits lack their required distinct-frame animation packages.
6. No CBA-CBH portrait or flag package exists. The 24 surviving CBL/CBL_LAST_TABLE TGA files are format-valid but partial and based on an obsolete route identity.
7. The focus runtime folder is empty because 37 tracked old DDS files are deleted in the shared worktree. They were not restored or counted. The current 180-to-224 focus icon pass is blocked on final focus IDs.
8. Eighteen old idea DDS and thirteen old achievement triplets survive, but they belong to the old gameplay contract and are unwired. The current target is a 24-icon idea baseline and 18 exact achievement triplets.
9. The decision and animated runtime folders are absent. No Event 014 unit, technology, or GUI static art exists.
10. All six retained animation source packages have distinct source frames, processed frames, static PNGs, sheets, GIFs, contact sheets, briefs, and frame plans. They are source-complete only. Their twelve listed runtime DDS files, sprite aliases, GUI layout, and scripted-GUI wiring are missing.
11. The six custom animation packages do not satisfy the full fourteen-row Part 10 animation ledger. Three are plausible matches for the early warning, Cult Cohesion warning, and island alert rows; the other three are useful adjacent custom art. Eleven exact Part 10 rows remain absent unless the plausible mappings are accepted.
12. Current shared registries contain no live Event 014 report, super-event, achievement, hidden-leader, unit, GUI, or animation wiring.

## Historical evidence boundary

- Commit f2d7e448db94312955200d5ba7b0bd50228ae2b0 deleted the previous Event 014 implementation, including GFX/GUI/scripted GUI, twelve animation DDS files, decisions, super-event files, portraits, and gameplay surfaces.
- Commit 1fb0617a4aa790301b0fd8ef6958ec44cc8e9961 deleted six root-size CBL/CBL_LAST_TABLE flags.
- These files are historical syntax and dimension evidence only. The gap map does not recommend wholesale restoration or counting them as current.

## Production decisions recorded

- Final DDS standard: uncompressed 32-bit BGRA/B8G8R8A8. Final Event 014 TGA flags: 32-bit BGRA, bottom-origin.
- Stable new report, news, super-event, portrait, flag-family, idea, decision, achievement, animation, and GUI logical names are recorded in the gap map.
- The protected portrait receives new sibling current-spec filenames rather than being overwritten.
- The minimum flag baseline is eight warlord families, unified base, three unified route families, and one deliberate transformed cosmetic identity, across base plus four ideology variants and all three sizes.
- The current Part 10 three-route unified flag contract conflicts with the scripted architecture's older CBL_LAST_TABLE cosmetic, while origin-route cosmetic tokens are still unspecified. Flag generation is blocked until the parent freezes that ledger.
- Focus icons are intentionally not batch-named beyond goal_[final_focus_id].dds until final IDs exist.
- Unit/technology files are intentionally blocked until implementation proves actual subunit, technology, or equipment IDs.
- UI-dependent art is intentionally blocked until the GUI owner supplies final rectangles.
- No focus/idea/decision/achievement/unit/technology/GUI cross-reuse is permitted.

## Parallel-work note

During the audit, the untracked docs/assets/014_cannibalism/static_event_art_imagegen directory appeared. At the audit snapshot it contained only five reference-inspection PNGs and no manifest, generated source art, processed deliverables, or final DDS. It was not counted. The parent should re-audit that directory before dispatching E14-RPT-01, E14-NEWS-01, E14-SUPER-01, or portrait generation so parallel output can be reviewed rather than duplicated.

## Remaining blockers and risks

- Final focus, idea, decision, unit, and technology IDs are not all implemented or frozen.
- GUI rectangles and therefore several static and animated sheet dimensions are not frozen.
- The exact acceptance or regeneration decision for the three plausible specification-animation mappings still belongs to the parent/GUI owner.
- Cosmetic tag availability must be confirmed before writing the full flag family.
- The top-level asset manifest is stale and should be rebuilt only after final asset production and wiring.
- Anti-spoiler gating must be verified at event-picture defaults, GUI defaults, focus search, achievements, flags, portrait resolution, and super-event slots, not only at event triggers.

## Validation evidence

- Verified protected portrait hash directly from the live file.
- Verified the report/news, portrait, idea, achievement, and stale super-event DDS headers and dimensions; active survivors use raw 32-bit BGRA, while the two original_unused images use DXT.
- Verified all surviving Event 014-related flags have the correct three dimensions, bottom-origin descriptor, and BGRA pixel format.
- Verified all six animation source packages contain eight distinct source hashes and complete PNG/GIF/contact-sheet support files.
- Verified all listed Event 014 runtime wiring files and folders against the live filesystem and registries.
- Rechecked scoped Git status before writing; this subagent did not touch the 37 focus deletions or other concurrent changes.

No fallback or simplification was used in the audit. The gap map reports every observed absence and contract drift explicitly.
