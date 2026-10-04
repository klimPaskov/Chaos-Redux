# Acid Rain small-marker parent review

Disposition: source/package artwork reviewed; provenance recovery, timed playback, static selection, and consumer-render acceptance remain open.
Scope: the front, warning, and severe animated families and their six sheet/static DDS files.
This is not complete GUI or Event 033 acceptance.

Each row below was opened individually as its selected source master, processed 128x128 PNG, and independently decoded DDS frame.
All three complete processed sheets and decoded sheets, all three static PNG/DDS pairs, and all three configured 48px map/38px card footprint boards were also opened.
The source, processed, and decoded artifacts are recorded by frame and hash in the producer's family manifests under the temporary `docs/assets/033_acid_rain/icon_artist/animations/acid_rain_gui/` workspace.

| Family/frame | Individual parent observation |
| --- | --- |
| Front 000 | Circular rim, lower anchor and compact cloud remain complete; rain reads at native size. |
| Front 001 | Selected native-alpha v2 repair retains the cloud, rim and long rain; the opaque checkerboard original is rejected. |
| Front 002 | Distinct billow and lower rain-impact state; no native-size clipping or matte square. |
| Front 003 | Dense crest and separate rain streaks remain readable inside the same rim. |
| Front 004 | Rightward cloud curl and visible inner opening preserve the fixed anchor. |
| Front 005 | Layered shelf and runoff changes retain the front identity. |
| Front 006 | Selected native-alpha v1 repair has the intended sparse rainfall and complete lower anchor; the opaque checkerboard original is rejected. |
| Front 007 | Compact return state is visually related to 000 without duplicate pixels. |
| Warning 000 | Triangular amber sign and fixed bottom tab distinguish it from a front. |
| Warning 001 | Different compact cloud/rain state with complete sign edges. |
| Warning 002 | Peak rain/drop state remains legible at both review footprints. |
| Warning 003 | Two-lobed cloud and darker wet sign preserve triangular geometry. |
| Warning 004 | Right-side rain/runoff variation stays within the native canvas. |
| Warning 005 | Tight loop-return cloud remains coherent with 000. |
| Severe 000 | Large cloud, lightning and splash read as stronger than the ordinary front. |
| Severe 001 | Central lightning and expanded impact state remain complete. |
| Severe 002 | Rightward lightning/impact variation does not move the rim anchor. |
| Severe 003 | Bright central crest and distinct droplets preserve the same severe-cell identity. |
| Severe 004 | Right-side core and spread splash remain inside the shared inset. |
| Severe 005 | Dense rain and broad lower splash retain complete edges. |
| Severe 006 | Broken cloud lobes and left impact remain readable at native size. |
| Severe 007 | Compressed return state is coherent with the opening frame. |

No final matte/checkerboard, clipped silhouette, or visible colored halo was found in these native-size marker views.
The producer's fixed-rim registration reports zero integer offset for every frame; no correction transform was applied to manufacture motion.
The producer's strict BGRA/Pillow roundtrips report exact RGBA equality, and static representatives are frame 000.
The accepted asset prompt permits front 8–12, warning 6–8, and severe 8 authored frames, so the delivered 8/6/8 counts are inside those ranges rather than a frame-count simplification.

| Runtime sheet/static pair under `gfx/interface/033_acid_rain/animation/` | Native contract | Parent package disposition |
| --- | --- | --- |
| `acid_rain_front_sheet.dds` / `acid_rain_front_static.dds` | 8 × 128x128, 6 FPS; static 128x128 | Artwork reviewed; final motion/consumer gate open. |
| `acid_rain_warning_sheet.dds` / `acid_rain_warning_static.dds` | 6 × 128x128, 5 FPS; static 128x128 | Artwork reviewed; final motion/consumer gate open. |
| `acid_rain_severe_sheet.dds` / `acid_rain_severe_static.dds` | 8 × 128x128, 6 FPS; static 128x128 | Artwork reviewed; final motion/consumer gate open. |

The existing GFX registry and named map/card consumers remain the runtime authority.
The event-owned GUI worker is implementing the accepted presentation-only motion toggle and mutually exclusive animated/static consumers.
Still images, strip inspection, numeric loop deltas, and GIF/APNG timing metadata do not establish timed visual playback or a current-source MCP render.
Original September generation prompts are being recovered; exact missing prompts are not reconstructed or asserted.

The global animation and the two static veils are outside this small-marker approval.
The parent individually opened all eight global repaired masters, processed frames and decoded DDS frames, and both static selected masters/processed/decoded files with dark/light composites.
The continuous global curtain is not accepted against the separated-cloud plan and is undergoing native repair.
Static-opacity changes require actual map-composite review.
No local opacity/matte workaround or unapproved fallback is accepted.
