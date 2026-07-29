# Event 006 real-person deterministic leader finish blocker — 2026-07-22

## Verdict

Blocked. The experiment preserves the recognisable source geometry and facial
identity, but it does not produce a genuinely HOI4-painted leader portrait.
Both candidates still read as colourized archival photographs beside the
protected Rupprecht/Matthes targets and canonical vanilla leaders. Josef
Harpe additionally shows unacceptable semantic-mask boundaries around the
cap, face, neck, and collar.

No candidate was approved, converted to DDS, copied into `gfx/leaders/`, or
wired. All processor metadata remains `candidate_requires_visual_approval`.
This handoff authorizes no DDS conversion, runtime wiring, or skill/workflow
recommendation.

## Scope and isolation

The experiment created one separate leader-only processor and an event-scoped
trial workspace. It did not modify:

- `the retired portrait-processing utility`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- gameplay, `.gfx`, DDS, localisation, specs, existing manifests, or protected
  runtime portraits

The frozen advisor processor remained byte-identical at SHA-256
`e248979f21784c016e69c5458b9925c32177d6af29f2cca1a82bfaaffbe1f23c`.

## Experimental method

The separate processor at
`.agents/skills/chaos-redux-event-assets/tools/leader_portrait_finish.py`
uses only source-derived and deterministic operations:

1. one explicit source-pixel crop;
2. a fixed `156x210` Lanczos fit;
3. manual output-space subject, face, clothing, cap, shirt, and tie masks;
4. manually recorded shadow/midtone/highlight palette ramps;
5. bounded bilateral value smoothing with face-specific strength;
6. low-amplitude deterministic directional brush texture;
7. restrained value-plane quantization, edge darkening, and vignette;
8. face luminance, gradient-magnitude, and gradient-direction correlations.

There is no ImageGen, face model, synthesis, reconstruction, inpainting,
content-aware fill, face warp, external model, downloaded weight, or invented
insignia. All manual parameters are in the JSON configs and embedded verbatim
in the metadata.

These controls were sufficient to preserve identity but insufficient to
replace photographic lighting and continuous photographic surface cues with
the authored planes, selective brushwork, edge decisions, and locally
reinterpreted colour found in genuine HOI4 painted portraits. Increasing the
deterministic smoothing/quantization further would remove identity-bearing
detail or become a generic filter, which violates the task constraints.

## Rejected trial evidence

### Gioacchino Solinas

- source master:
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/sardinia_crown_command_retry/source_masters/sardinia/arx_gioacchino_solinas_1943_original.png`
- source SHA-256:
  `af9d453444a7c8ee3f4f75089eec9104748e19d4c8adbb0f2f2bf150e1a0ea15`
- config:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/configs/arx_gioacchino_solinas.json`
- config SHA-256:
  `b665ed7cae02a04214314ff7959dcb8487ada44e385e4790fcb7019edd4927e0`
- rejected candidate:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/candidates/arx_gioacchino_solinas.png`
- candidate SHA-256:
  `ce9bf8b93a2155859fc1d5f98de07f43cdb7a464d6be7f3f6f24a9cdb956062a`
- native/4x comparison:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/review_sheets/arx_gioacchino_solinas_review.png`
- review SHA-256:
  `31bf77d0a24c5527d1414489d37d6ce3f03987b031b2aa19fb2ee19921a80a17`
- mask sheet:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/mask_sheets/arx_gioacchino_solinas_masks.png`
- metadata:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/metadata/arx_gioacchino_solinas.json`
- recorded face metrics: luminance correlation `0.996544`, gradient-magnitude
  correlation `0.987542`, gradient-direction cosine `0.990530`
- visual rejection: strong likeness, but the result remains visibly a tinted
  and softened black-and-white photograph rather than a painted HOI4 portrait

### Josef Harpe

- source master:
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/western_gap_retry/source_masters/RHI/RHI_josef_harpe_bundesarchiv_original.jpg`
- source SHA-256:
  `5353200abd3584c52a4938f2a79bf62c15d1be6aad22d70e0c45f1a4181c1384`
- config:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/configs/rhi_josef_harpe.json`
- config SHA-256:
  `ee290ff7c9878d7e95fbbcae596f652743b7e82c913e5a33dd8f6c85adb1a5ba`
- rejected candidate:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/candidates/rhi_josef_harpe.png`
- candidate SHA-256:
  `2b54790b783ba1f6de220c54a99f79a8f6e278be8b925bfc7f16df8087bb8b52`
- native/4x comparison:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/review_sheets/rhi_josef_harpe_review.png`
- review SHA-256:
  `880d8c26cccc29bf2db7791ea9690287a2c780f2d0912b8fd0efaea5ed1f8c91`
- mask sheet:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/mask_sheets/rhi_josef_harpe_masks.png`
- metadata:
  `docs/assets/006_independence_wave/leader_finish_tool_trials_2026_07_22/metadata/rhi_josef_harpe.json`
- recorded face metrics: luminance correlation `0.996753`, gradient-magnitude
  correlation `0.989058`, gradient-direction cosine `0.982338`
- visual rejection: still photographic, with conspicuous cap/skin/collar mask
  transitions and washed facial planes

The high correlations prove that the source identity survived. They do not
prove painted style, and they did not override the visual rejection.

## Comparison set

Each review sheet includes the source crop, candidate, protected Chaos Redux
targets, and canonical skill-local vanilla leaders at native `156x210` and 4x
nearest-neighbour scale:

- `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`
- `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`
- `den_thorvald_stauning.png`
- `fin_carl_mannerheim.png`
- `afg_mohammed_zahir_shah.png`
- `ice_sveinn_bjornsson.png`

The canonical PNGs come from
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.

## Recommendation

Do not promote or document `leader_portrait_finish.py` as an approved
`chaos-redux-event-assets` workflow. Omit the tool from the production merge to
prevent future agents from treating a mechanically valid but visually failed
pipeline as production-capable. Retain the trial workspace and this handoff as
rejection evidence if the project wants a durable record of the non-generative
deterministic ceiling; otherwise the entire experimental package may be
discarded together.

Under the current prohibition on ImageGen, face synthesis, generative
reconstruction, and authored manual repainting, no acceptable replacement path
was found. A future attempt needs explicit authorization for a human-authored
manual digital repaint over the sourced likeness, with the source photo kept
visible during review and the painted result independently checked for identity.

## Simplifications, omissions, and blockers

- No production-capable HOI4 painted finish was achieved.
- No third portrait was needed after both required sources independently
  demonstrated the same deterministic ceiling.
- No candidate was approved or converted.
- No DDS, runtime portrait, GFX, gameplay, localisation, spec, manifest, or
  skill text was changed.
- The blocker is visual-authorship capability under the non-generative,
  no-reconstruction, no-generic-filter constraint; it is not a missing source,
  runtime error, or identity-preservation failure.
