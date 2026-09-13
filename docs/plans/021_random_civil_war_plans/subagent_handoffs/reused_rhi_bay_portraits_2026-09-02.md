# Event021 RHI/BAY reused portrait audit handoff

Audit date: 2026-09-02.

Owner: Chaos Redux portrait-production subagent.

Scope: exactly six existing GFX rows from docs/plans/021_random_civil_war_plans/subagent_handoffs/event006_reused_asset_crosswalk_2026-09-02.json, covering iw008/RHI and iw009/BAY.

## Handoff result

The bounded audit is complete.

No safe candidate repair or promotion was made.

The complete six-row evidence crosswalk, source provenance, rights notes, consumer tracing, visual review paths, exact hashes, DDS metadata, and independent audit caveats are in docs/assets/021_random_civil_war/validation/reused_rhi_bay_portraits_2026-09-02/crosswalk.md.

The four generated grounded-person runtime rows are blocked under the current portrait policy.

The two named vanilla reuse rows remain source_placeholder by the existing authority and are blocked for promotion because the selected external _00002 outputs differ from the retained local deterministic processed PNGs and their mode authority is unresolved.

The current no-final-placeholder requirement is not satisfied by any of the six rows.

## Six-row status

| # | Package, actual consumer, and role | Current runtime file SHA-256 | Decoded native SHA-256 | Status |
| --- | --- | --- | --- | --- |
| 1 | iw008/RHI; generated male RHI_independence_wave_provisional_directorate, displayed as Wilhelm Marx; civilian.large | 080a1c3b3f6c7c3f01f7e380c8c6bfc064c238fcc44db084f2c559f1c3436bcb | f3e6d37612fee163ae64f527fd9ac9f0ba68c78f770149425f3a782dfef38164 | BLOCKED_GENERATED_GROUNDED_REPAINT |
| 2 | iw008/RHI; generated male RHI_independence_wave_river_commandant, displayed as Gustav-Adolf von Zangen; civilian.large and army.large | f8f99f0d3ef38601da687b9a2cea63edbde629017076e26e46b26b4b762e0df2 | fc1c0074e98f87819e3217981fd1982f04b03f10456febb9a2a2908cfb6f0400 | BLOCKED_GENERATED_GROUNDED_REPAINT |
| 3 | iw008/RHI; existing vanilla male RHI_josef_friedrich_matthes, displayed as Josef Friedrich Matthes; civilian.large | fb43deb0b8708e7f5d1000b1f67ab63aca43d54efcb75618fb9097112a7699aa | 045143232876d8095ae532f2dd7c291b53954941a920978720fa4315b6476aa0 | BLOCKED_FOR_PROMOTION |
| 4 | iw009/BAY; generated male BAY_independence_wave_state_council, displayed as Heinrich Held; civilian.large | 999857d191f7b088e11daa78fb29eadd0b514dc6da494a0102423c635e736e95 | 02c73fb07a93c5b261f86fe221706a7fb8cfe644cc3d99e18cdbd50c3c49b551 | BLOCKED_GENERATED_GROUNDED_REPAINT |
| 5 | iw009/BAY; generated male BAY_independence_wave_mountain_commandant, displayed as Friedrich Dollmann; civilian.large and army.large | 332d8578f4bdede1a9fead234b361aa8c9fd786d5261cb45dbea56475754dbab | f90ff7139c6861fae18f6cfd8cd824b8d2f5b88c8f75d5609653b27c6dcd8f91 | BLOCKED_GENERATED_GROUNDED_REPAINT |
| 6 | iw009/BAY; existing vanilla male BAY_rupprecht_of_bavaria, displayed as Rupprecht von Bayern; civilian.large | fb7bce1d8316f52d728e82e299eaf9675fa0dabe57f2f7c9aff154c1012478b7 | c16ce49fa05e45da8fd3bba0c84c3c44754b6adc893472497ea1f74242d974db | BLOCKED_FOR_PROMOTION |

All six runtime files are 131168-byte 156x210 one-level uncompressed BGRA DDS files with opaque alpha and valid headers.

## Consumer and wiring findings

All six rows are live in the bounded setup trace and are not orphan GFX rows.

The generated RHI/BAY helper is common/scripted_effects/006_independence_wave_rhineland_bavaria_saar_package_effects.txt.

The RHI preparation helper creates or updates the Marx and von Zangen tokens at lines 215-267 and iw008 invokes it at lines 900-905.

The BAY preparation helper creates or updates the Held and Dollmann tokens at lines 269-312 and iw009 invokes it at lines 954-959.

The same helper conditionally overrides the existing vanilla Matthes and Rupprecht large portraits at lines 260-266 and 313-323 and restores their vanilla portraits at lines 327-338.

The four institutional-sounding sprite names are actual named-person consumers, not people-free institutional portraits: the current displayed names are Wilhelm Marx, Gustav-Adolf von Zangen, Heinrich Held, and Friedrich Dollmann, and the generated tokens explicitly use gender = male.

The stable GFX rows remain unchanged at interface/006_independence_wave_portraits_registry.gfx:259-272 for the four generated rows and interface/006_independence_wave.gfx:58-59 for the two vanilla reuse rows.

## Source, rights, and ImageGen evidence

Wilhelm Marx: [Wikimedia Commons source page](https://commons.wikimedia.org/wiki/File:Reichskanzler_Wilhelm_Marx.jpg) and [LOC item 2014716800](https://www.loc.gov/pictures/item/2014716800/), circa 1920, LOC/Bain no-known-restrictions/public-domain basis.

Gustav-Adolf von Zangen: [Wikimedia Commons Bundesarchiv source page](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-H28061,_Westfront,_Gustav_v._Zangen,_Albert_Speer.jpg), November 1944, [CC BY-SA 3.0 Germany](https://creativecommons.org/licenses/by-sa/3.0/de/deed.en), Bundesarchiv credit required.

Josef Friedrich Matthes: [LOC item 2014695969](https://www.loc.gov/pictures/item/2014695969/) and [LOC persistent handle](https://hdl.loc.gov/loc.pnp/ggbain.15992), 22 November 1923, LOC no-known-restrictions advisory.

Heinrich Held: [Wikimedia Commons source page](https://commons.wikimedia.org/wiki/File:Heinrich_Held,_1933.jpg) and [NAC object record](https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6270998/obiekty/473188), circa 1933, Commons CC0 1.0 source record.

Friedrich Dollmann: [Wikimedia Commons Bundesarchiv source page](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_101I-052-1435-20,_Oberrhein,_Befestigung_am_Isteiner_Klotz.jpg), 1940, [CC BY-SA 3.0 Germany](https://creativecommons.org/licenses/by-sa/3.0/de/deed.en), Bundesarchiv credit required.

Rupprecht von Bayern: [Wikimedia Commons source page](https://commons.wikimedia.org/wiki/File:Rupprecht_von_Bayern_01.jpg), circa 1916, underlying work marked public domain/PD-Art on Commons, with a museum-digital/Historisches Museum der Pfalz credit and CC BY-NC-SA metadata caveat.

The existing Marx, von Zangen, Held, and Dollmann packages contain raw ImageGen result evidence and processed PNGs, and their historical metadata identifies the source kind as real and the processing as an identity-preserving ImageGen edit.

The current Matthes and Rupprecht selected outputs are read-only external _00002 PNG/DDS files in C:/Users/klimp/Documents/ComfyUI Workflows/HOI4/hoi4_portraits_output/output/156x210/iw and its dds subdirectory.

RunPod was not opened, operated, configured, queued, or monitored.

## Visual and processing review

All six source crops were individually reviewed at native size and nearest-neighbor 4x.

All six retained processed or selected external PNGs were individually reviewed at native size and nearest-neighbor 4x.

All six current DDS files were decoded and individually reviewed at native size and nearest-neighbor 4x.

Rows 1, 3, 4, and 6 were compared with the canonical vanilla leader reference den_thorvald_stauning.png.

Rows 2 and 5 were compared with the canonical vanilla commander reference ger_erwin_von_witzleben.png.

The source crops all equal their recorded master rectangles.

The four generated-repaint runtime decodes equal their retained processed PNG pixels.

The Matthes and Rupprecht selected external PNG/DDS/runtime triples are internally exact, but each differs from its retained local deterministic source-placeholder PNG.

No crop, alpha, dimension, or DDS encoding defect was found.

## Evidence files and changed scope

Only the following requested report path and evidence path were written:

docs/assets/021_random_civil_war/validation/reused_rhi_bay_portraits_2026-09-02/crosswalk.md.

docs/plans/021_random_civil_war_plans/subagent_handoffs/reused_rhi_bay_portraits_2026-09-02.md.

The evidence directory also contains 54 review binaries: six exact source-crop copies, two selected external PNG copies, two vanilla role-reference copies, six decoded-native runtime PNGs, six native comparison sheets, and 32 nearest-neighbor 4x comparison assets and sheets.

The existing Event006 source masters were referenced in place and not moved or duplicated into the Event021 evidence directory because the user restricted initial writes to the evidence directory and this handoff.

No live runtime DDS, source master, processed PNG, external selected output, GFX file, character file, advisor file, small portrait, animation, or gameplay file was changed.

## Parent action and blockers

Rows 1, 2, 4, and 5 require removal from the live promotion set or a parent-approved replacement path that does not repaint or substitute a grounded named person; this subagent did not create or install one.

Rows 3 and 6 require a mode-authority decision before promotion: the dated authority says source_placeholder, while the selected external outputs are a different processed chain and are not independently relabelled styled_final here.

The Rupprecht rights record also requires parent review of the Commons public-domain/PD-Art basis against the museum-digital/Historisches Museum der Pfalz metadata terms before promotion.

No candidate repair was created because the observed defects are provenance, mode, policy, and rights-gate defects rather than crop or encoding defects.

The mandated converter .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py was inspected but not rerun because no candidate was admitted and all current runtime DDS files already pass the contract.

No HOI4 MCP event workspace scan, in-game test, live consumer validation, or broad Event006 discovery was performed.

No commit was created because the user explicitly prohibited committing.

This handoff does not claim Event021 portrait completion.
