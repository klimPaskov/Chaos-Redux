# Asset Prompt for Event 007 Fury

Create the final visual asset package for Chaos Redux Event 007, Fury.

Read and follow:

- AGENTS.md
- chaos-redux-event-assets
- chaos-redux-frame-animation if any animated asset is approved
- docs/specs/007_fury_specs/007_fury_asset_plan.md
- docs/specs/007_fury_specs/007_fury_spec.md

Event identity:

- Event ID: 7
- Slug: fury
- Type: minor repeatable
- Cluster: Wars
- Source mode: generated for fictional symbolic assets, no real leader portrait generation

Required assets:

1. `idea_fury_impetus`, idea icon, 64x64, generated.
2. `idea_fury_veteran_impetus`, idea icon, 64x64, generated.
3. `idea_fury_joint_command`, idea icon, 64x64, generated.
4. `idea_fury_all_front_command`, idea icon, 64x64, generated.
5. `idea_fury_continental_mandate`, idea icon, 64x64, generated.
6. `decision_category_fury_campaign`, decision category icon, repo pattern or 32x32, generated.
7. `decision_fury_next_war`, decision icon, 32x32, generated.
8. `decision_fury_depot`, decision icon, 32x32, generated.
9. `decision_fury_administration`, decision icon, 32x32, generated.
10. `decision_fury_core`, decision icon, 32x32, generated.
11. `decision_fury_coordination`, decision icon, 32x32, generated.
12. `decision_fury_world_end`, decision icon, 32x32, generated.
13. `faction_fury_pact`, faction emblem, repo pattern, generated.
14. `news_event_fury_first_victory`, news image, 397x153, black and white, generated.
15. `super_event_fury_major`, super-event image, 457x328, generated.
16. `super_event_fury_world_end`, super-event image, 457x328, generated.
17. Optional `leader_fury_staff_council`, fictional leader or council portrait, 156x210, generated only if the implementation uses the high-chaos council identity.

Focus icon family:

Create or assign HOI4-style 94x86 focus icons for these motifs:

- border mobilization
- surprise orders
- military staff takeover
- civil administration
- depot seizure
- captured industry
- rail and supply expansion
- occupation integration
- partner coordination
- all-front assault
- no-neighbor consolidation
- world-end export branch

Rules:

- Preserve existing country base flags.
- Do not create bespoke flags for every possible Fury candidate.
- Do not generate portraits for real existing country leaders.
- Generated news and super-event images must avoid readable text.
- Inspect relevant reference folders before generation.
- Save source PNGs, processed PNGs, DDS files, manifests, and gfx handoff notes.
- Final DDS files must be in the correct mod folders, not only under docs.
- Create `docs/assets/007_fury/manifest.md` and `docs/assets/007_fury/gfx_handoff.md`.

Animation:

No baseline animation is required. If an animated Fury emblem is requested later, create real source frames, a horizontal sheet DDS, a static fallback DDS, a GIF preview only for review, and frame metadata.
