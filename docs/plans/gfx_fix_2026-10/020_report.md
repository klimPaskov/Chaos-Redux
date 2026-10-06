# Event 020 Black Plague Graphics Report

The six Event 020 asset repairs are tracked in the named event-asset package at `docs/assets/gfx_fix_plague_2026-10/`; the package contact sheet is `contact_sheet.png`, and the animation frame proof is `previews/020_animation_frame_proof.png`.

| Finding | Status | Result | Runtime destination |
|---|---|---|---|
| `GFX_black_plague_crisis_seal_animated` | Complete | Eight consistent 64×64 frames use the unchanged static seed plus seven individually generated native-alpha glint layers; frame 000 equals the static fallback and the 512×64 sheet is installed. | `gfx/interface/animated/020_black_plague/crisis_seal/` |
| `GFX_black_plague_rat_king_terminal_readiness_animated` | Complete | Eight 64×64 authored master frames are retained; the parent accepted the 34×34 static and 272×34 runtime sheet for the sole 41px decision-row consumer, and frame 000 equals the resized static seed. | `gfx/interface/animated/020_black_plague/world_end_readiness_seal/` |
| `GFX_black_plague_response_progress_fill` | Implemented and reviewed | The 96x27 brass/parchment tile preserves source alpha; a matching 60% MCP before/after pair and coherent 0%/100% post-change renders show clean empty, three-band and five-band states. | `gfx/interface/020_black_plague_response/response_progress_fill.dds` |
| `GFX_decision_black_plague_clean_city_rats` | Complete | The 33×32 processed PNG rebuilds opaque trap interiors from a mask and retains a soft exterior edge; its DDS was converted and round-trip checked. | `gfx/interface/decisions/020_black_plague/decision_clean_city_rats.dds` |
| `GFX_goal_black_plague_rat_brood_signal` | Complete | The 94×86 processed PNG fills the enclosed badge interior, retains a soft exterior edge, and serves both existing base and shine aliases; its DDS was converted and round-trip checked. | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_brood_signal.dds` |
| `GFX_goal_black_plague_rat_king_the_royal_basin` | Complete | The 94×86 processed PNG rebuilds the opaque badge silhouette and retains a soft exterior edge; its DDS was converted and round-trip checked. | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_king_the_royal_basin.dds` |

The crisis-seal animation retains eight source frames, an eight-frame 512×64 PNG and DDS sheet, a 64×64 static PNG and DDS fallback, an 8-frame contact sheet, and a review-only GIF preview.

The readiness animation retains the 64×64 authored master package and uses a reviewed 34×34 runtime package because its only literal consumer is the 41-pixel decision row; no other readiness-static or sheet-path consumer was found.

The progress meter is a read-only 520x282 decision-category attachment with five 96x27 bands in a 480x27 meter and 20-point visibility thresholds.
The matching 60% before/after comparison preserves flags, values and 1920x1080 scale-1 geometry; the post-change 0% and 100% scenarios provide supplemental state coverage, not falsely matched pre-change comparisons.
The 0% status reads Not established, the 60% status reads Active research programme, and the 100% status reads Complete: cure-capable cleanup unlocked.
MCP validation found no visible overlap, text overflow, missing texture or missing sprite in these requested states; hidden zero-size fields and generic unvisited-state notices remain documented in `020_gui_handoff.md`.

The crisis-seal consumer is correctly placed at 28.8px display size in the shared containment board.
Its frame-shader preview is partial: the open scenario schema does not declare a frame/time selector, and the attempted 0.5s request returns an empty selectedFrames object.
The source/native eight-frame proof establishes consistent authored frames, but does not prove in-game motion or a pre-rebuild/current shared-board comparison.
That capability limit is retained explicitly for the orchestrator.

The reviewed visual references were limited to the matching canonical decision-icon, medal, and institutional-board families in `.agents/skills/chaos-redux-event-assets/assets/gfx_references`; no matching progress-fill texture family exists in that reference root.

The completed DDS files use only `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and passed uncompressed BGRA header, native dimensions, exact byte length, alpha-range, and decoded-pixel round-trip comparisons against their processed PNGs.

The inherited crisis frame-001 glint source was superseded at the parent’s request; a fresh replacement prompt was saved before generation, and the older PNG and composite are retained outside the final sheet.

The exact prompts for resumed ImageGen frames 002–007 were recovered from this turn and archived after generation; the replacement frame-001 prompt was archived before generation, while the superseded carry-forward and rejected full-seal request records remain unavailable.

The asset producer did not edit `.gfx`, `.gui`, gameplay, localisation, event, history, focus, decision, or spreadsheet files; parent-owned runtime review and wiring remain outside this report's asset production scope.
