# IW-007 Frisia retry 02 portrait-refinish producer handoff

Producer: `chaosx_generated_event_art` (identity-preserving real-person edit)
Date: 2026-07-22
Scope: only the new `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/frisia_retry_02/` package. No prior rejected package, source package, gameplay, interface, localisation, registry, runtime DDS, skill, or unrelated manifest was edited.

## Deliverables

- Exact selected source copies:
  - `source_masters/AGX_douwe_kalma_1917.jpg` — SHA-256 `38dafcbff7c3a67b6b29b9b637e69ff4c2f9d8caae076361200919a6bb36dbdf`, native `691x1013` RGB.
  - `source_masters/AGX_pieter_reenalda_1919_uniform.jpg` — SHA-256 `8f93840b12ecdcb313279c6f0fd4027863f8c1c4c9232e699aa7a0a9d46668ce`, native `1206x1765` grayscale `L`.
- Official built-in ImageGen edit prompts:
  - `prompts/leader_douwe_kalma_identity_preserve.txt`
  - `prompts/commander_pieter_reenalda_identity_preserve_candidate_01.txt`
  - `prompts/commander_pieter_reenalda_identity_preserve_candidate_02.txt`
- Raw ImageGen masters:
  - Kalma: `raw_masters/leader_douwe_kalma_imagegen_2026-07-22.png`, `1069x1472` RGB, SHA-256 `222c7f75bbf24a4167151bb96aa3f256b4f50938f14dc4739de7df6fa2f53238`.
  - Reenalda candidate 01: `raw_masters/commander_pieter_reenalda_imagegen_candidate_01_2026-07-22.png`, `1081x1455` RGB, SHA-256 `cdc0c7fb893ee980ec5be0e94cfb8df0aabcf455252c90aee4c62e2cd58ef2d1`.
  - Reenalda candidate 02: `raw_masters/commander_pieter_reenalda_imagegen_candidate_02_2026-07-22.png`, `1080x1456` RGB, SHA-256 `eb5d9e6ee35ba6a44ddf9b2e307c42da1b0f5bdaf7df273487350e5c6ad5a8b3`.
- Processed 156x210 PNG previews:
  - `processed_png/AGX_friesland_coastal_council.png`, RGBA opaque, SHA-256 `644e37c3ffbcfa871af22bcb6cf9e575cbfa16bdd2cc30b253e2f65c440277a8`.
  - `processed_png/AGX_friesland_coastal_commander.png` (Reenalda candidate 02), RGBA opaque, SHA-256 `25a3c29b6b9deeda87d0e96699beb44d2d2d7051a5335af61f630cb5d918c968`.
  - `processed_png/AGX_friesland_coastal_commander_candidate_01.png` is retained for comparison and is blocked; SHA-256 `e6e2e20791823f4f21edf5cf295fbfbbde68382619111c2431ab91e093df9647`.
- Native review evidence: `contact_sheets/native_source_result_style_comparison.png`.
- Hash ledger: `hashes.sha256`.
- Package manifest: `manifest.md`.
- GFX handoff: package-local `gfx_handoff.md`.

## Identity and style inputs

Each edit used the exact selected source master as the sole identity-bearing
input. Style-only inputs were male vanilla HOI4 references from the canonical
curated pack:

- Kalma leader: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/den_thorvald_stauning.png`.
- Reenalda candidate 01: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/generic_africa_navy_2.png`.
- Reenalda candidate 02: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/generic_africa_navy_1.png`.

The 1915 garden and 1911 uniform Reenalda images were comparison/context only;
they were not supplied to ImageGen and are not runtime identities. The prior
drifted ImageGen portraits were not reused.

## Crop and likeness review

- Kalma source crop: `(48, 62, 643, 864)`; raw-result crop: `(34, 58, 1035, 1405)`.
- Reenalda source crop: `(0, 48, 1206, 1672)`; candidate 01 raw crop: `(0, 0, 1081, 1455)`; candidate 02 raw crop: `(0, 0, 1080, 1454)`.
- Kalma self-review: direct gaze, center pose, swept hair, forehead source mark, collar, patterned tie, jacket and shoulder silhouette remain recognizable; subtle eye/jaw symmetry drift cannot be ruled out. Status: `needs_independent_visual_audit`.
- Reenalda candidate 02 self-review: broad face, hair part, broad handlebar moustache, centered head, high-collared maritime uniform, buttons, pocket chain and shoulder-board silhouette remain recognizable; eye/cheek and fine moustache geometry may drift. Status: `needs_independent_visual_audit`.
- Reenalda candidate 01 self-review: visible eye/cheek drift and more assertive invented shoulder-board color. Status: `blocked`; never wire it.

## Runtime handoff and blockers

Stable sprite names and intended runtime paths are preserved in
`gfx_handoff.md`:

- `GFX_portrait_AGX_friesland_coastal_council` → `gfx/leaders/AGX_friesland_coastal_council.dds`.
- `GFX_portrait_AGX_friesland_coastal_commander` → `gfx/leaders/AGX_friesland_coastal_commander.dds` (candidate 02 only).

DDS/runtime conversion is explicitly deferred by the parent. No DDS, `.gfx`,
gameplay, localisation, or registry file was created or edited. The parent must
perform an independent visual audit; if either likeness materially drifts, fail
closed and mark that subject blocked rather than selecting a generic or prior
portrait. Only after approval should the main agent run the repository-standard
DDS converter and wire the existing stable sprites.
