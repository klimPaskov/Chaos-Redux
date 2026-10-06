# Shared unit pipeline decisions

Execution date: 6 October 2026.
Acceptance basis: the user's explicit section 3 assignment, common-ticket rules, no paid provider tasks, existing-recording-only audio, and source-safe global fixes.

| Decision | Reason and evidence | Disposition |
|---|---|---|
| Use a repository native BC1/BC3 encoder rather than requiring texconv | No installed texconv was found; endpoint fitting, full mip payloads and independent decoded-pixel QA were implemented and tested against installed vanilla maps. | implemented; `texture_tools_handoff.md` |
| Preserve existing normal G/A where handedness is not proven | The installed shader and exporter flip conventions require actual source evidence; blanket Y inversion could introduce another defect. R mirrors G, unused B is zero and padding is flat. | implemented; texture delivery manifest |
| Require material/UV masks before changing specular classes | Skin, cloth, fur, stone and metal cannot be reliably inferred from a dark atlas; explicit class masks remove metal leakage and select the requested G/A ranges. | implemented tools; package masks remain required |
| Treat material streams as one logical surface | Independent stream topology would count export partition seams as holes. | implemented; geometry delivery tests and installed audit |
| Keep winding diagnostics when non-manifold islands exist | Ambiguous orientation cannot be repaired blindly, but the rest of the mesh still needs evidence. | implemented; winding inspector and 34 blocked mesh registrations |
| Make action and mesh gates refuse invalid candidates | Existing signs may be negated without changing key orientations; real pose, root, weight and component corrections remain live Blender authoring. | implemented; actual gorilla export refusal and native reimport proof |
| Measure evaluated sole geometry for footstep placement | An ankle coordinate or a guessed cycle peak does not establish contact. | implemented; delivery policy helper and hash-bound event proposals |
| Preserve separate authored item materials and UVs | The shared quarter-height prop strip discarded canvas space and the old helper generated skin/aim/floor changes; the production entry now reviews an existing authored assembly. | implemented; `review/lab_items.py` |
| Separate mastering acceptance from sound-package acceptance | Format and levels can be corrected safely while source sharing, missing takes, role identity and state timing still need package work. | implemented; source/duplicate/cue reports |
| Accept inherited per-file licensed recording attribution with captured input SHA | Remastering uses the exact existing runtime recording; an absent untouched-original archive is disclosed and never invented. Ambiguous source/license mappings are held. | implemented review policy; provenance review |
| Use recorded-sample crossfades and bounded limiting | They are ordinary authorized editing of existing recordings and meet the requested loop/true-peak gates without generated tones or noise. | implemented; recovery reports |
| Archive and remove only globally unused binaries | Per-model directory scans incorrectly treated assassin variants' shared maps as unused; active consumers and embedded references were combined first. | implemented; nine archived maps, 37,749,888 bytes |
| Correct winding face counts without changing acceptance | Empty map lookups had counted every face; exact-position rereads correct all 48 objects while preserving edge counts and intake/manifold decisions. | implemented; geometry_counts_corrected.json and eleven focused winding tests |
| Preserve geometry-only reimport limits | A matching checkpoint proves native import of installed bytes, while material appearance, deformation and live consumer validation are separate. | implemented; all 38 registrations have matching native proof |
| Reject zero channels as motion-peak evidence | Static translation must not admit every rotation frame into the timing peak set; static poses provide no contact proof. | implemented; eight focused entity-lint tests |
| Specify source briefs for the two licensed held cues | Island-reavers death is clipped; march idle fails recorded-edge loop checks. Existing licensed archives are checked first, with about 2.2 s death and about 6 s idle targets; new sourcing remains orchestrator work. | accepted and queued under explicit audio-needs mandate; WP2/WP6 needs reports |
| Leave showcase capture to the orchestrator | Empty attack tiles and distant-unit crop locks require capture changes rather than model transformations. | accepted and queued; exact capture protocol in pipeline report |

No source substitutions, paid provider attempts, new recordings, generated sounds, or generated production rigs/weights/keys were used.
No gameplay, entity, sound-definition, focus, GUI, country, equipment or spreadsheet content was added by this tranche.
