# Death Icon Scratch Source Cleanup Handoff

Date: `2026-06-21`

Parent task:

- Correct the Death icon asset trail after the user clarified that the needed Death icons must be regenerated from scratch, not modified from existing icon art.

Files changed:

- `docs/assets/010_death/generated_art_manifest.md`
- `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/gfx_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_012_africa_asset_qa_handoff.md`
- Removed tracked superseded folders:
  - `docs/assets/010_death/focus_icon_regen_white_artifact_2026_06_21/`
  - `docs/assets/010_death/focus_icon_fresh_regen_2026_06_21/`
- Removed untracked stale folder:
  - `docs/assets/010_death/focus_icon_regeneration/`

Changed asset evidence:

- The active Death icon source of truth is now only `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/`.
- The deleted `focus_icon_regen_white_artifact_2026_06_21` package was a modified-art repair pass and is no longer present as a tracked package.
- The deleted `focus_icon_fresh_regen_2026_06_21` package was an intermediate focus-only package and is no longer present as a tracked package.
- The deleted untracked `focus_icon_regeneration` folder was stale local output and is not part of the accepted asset trail.

Validation evidence:

- The eight live Death focus DDS files match the scratch package DDS files byte-for-byte.
- The scratch package validation records fresh generated source PNGs, processed PNGs, package DDS files, live DDS files, transparent `94x86` focus icons with zero opaque-white pixels, and separate `64x64` Death achievement triplets.
- The scratch package validation records source PNG byte comparisons against the older modified/fresh packages as non-identical.

Remaining issues:

- None for the Death icon provenance correction.
- This handoff does not cover unrelated Event 012 Africa icon/audio work or Soviet Collapse icon QA.
