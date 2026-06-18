# Event 012 Missing High-Chaos Actor Parent Handoff

Date: `2026-06-18`

## Scope

Implemented the four prompt-named Event 012 high-chaos actor packages that were previously queued:

- `BON` Bonobo Kinship Congress
- `HYR` Hyena Radio Dominion
- `BIR` Bird of the Walls
- `SAO` Sao Terracotta Host

## Gameplay Surfaces

- Added country tags, country files, history files, static OOBs, capitals, politics, leaders, role ideas, role setup packages, generated advisor/commander hooks, AI strategies, and Charter/high-chaos binding.
- Expanded the Authority Atlas high-chaos catalog from 11 to 15 packages and registered package IDs `212` through `215`.
- Added package outcomes, selected-package localisation, habitat-seat handling, actor setup, cleanup, and reset coverage.
- Added four one-time targeted Bestiary decisions with concrete non-PP requirements and spends:
  - Bonobo Kinship gentle veto
  - Hyena Radio misdirection broadcast
  - Bird of the Walls verified warning
  - Sao Terracotta defensive line
- Added report events `chaosx.nr12.45` through `chaosx.nr12.48`.
- Added achievements and localisation for the four prompt-named rows, and extended `ACH_AFR_CHARTER_HAS_TOO_MANY_SIGNATURES` to require all 15 Bestiary package outcome flags.

## Asset Surfaces

- Integrated source art from the asset subagent under `docs/assets/012_africa/missing_high_chaos_actor_assets/`.
- Produced final portrait DDS files under `gfx/leaders/012_africa/`.
- Produced base and ideology variant flag TGA families under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- Produced normal, grey, and not-eligible achievement DDS icons under `gfx/achievements/`.
- Registered portrait sprites in `interface/012_africa.gfx` and achievement sprites in `interface/chaosx_achievements.gfx`.
- Documented the package in `manifest.md`, `gfx_handoff.md`, and `prompts/generated_prompts.md`.

## Validation

- Confirmed touched script files have balanced braces.
- Confirmed no unsupported `<=` or `>=` operators were introduced in the touched script set.
- Confirmed localisation files touched in this tranche keep UTF-8 BOM.
- Confirmed new portrait DDS files are `156x210`, achievement DDS files are `64x64`, and flag TGAs are `82x52`, `41x26`, and `10x7`.
- Visually reviewed processed contact sheets for the four portraits, twenty flag variants, and twelve achievement icon variants.

## Remaining Risks

- The exact image-generation prompt strings were not returned by the asset subagent. The package records production briefs and source files instead of a verbatim prompt transcript.
- Small flag variants compress fine details at `10x7`; this matches the documented risk for earlier Bestiary flag packages.
- This tranche resolves the queued BON/HYR/BIR/SAO actor and achievement packages. It does not claim full Event 012 completion; the broader completion audit still has unresolved UI/animation/depth and scenario-validation findings.
