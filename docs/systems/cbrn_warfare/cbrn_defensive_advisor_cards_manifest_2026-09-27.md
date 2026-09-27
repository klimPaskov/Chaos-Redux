# CBRN Defensive Advisor Portrait Asset Manifest

Date: 2026-09-27.

Status: Three native advisor-card DDS assets are installed, sprite-registered, and independently reviewed by the parent agent.

## Authorization and provenance

The parent authorized advisor cards for `SOV_nikolay_zelinsky`, `ENG_norman_heatley`, and `USA_stanhope_bayne_jones` using their existing approved scientist portrait masters. The user-approved source decision, relayed by the parent, says the approved in-mod scientist portraits may be reused and their external source archive does not need recovery. The masters were not edited or moved.

This manifest records source bytes and asset processing. It does not claim new image attribution, license, or redistribution rights; those remain inherited from the existing approved in-mod portraits and were not re-audited here. No Internet image, ImageGen output, or RunPod session was used. No styled-final replacement was requested or supplied, and the main `156x210` portrait files and their replacement states remain unchanged.

The initial four-person proposal was narrowed by the parent to these three appointments because `USA_james_stevens_simmons` had no distinct accepted gameplay effect. No Simmons card was generated or registered.

## Source and runtime crosswalk

| Subject | Source master | Source SHA-256 | Source size | Processed PNG | PNG SHA-256 | Runtime DDS | DDS SHA-256 | Sprite |
|---|---|---|---|---|---|---|---|---|
| `SOV_nikolay_zelinsky` | `gfx/leaders/scientists/portrait_SOV_nikolay_zelinsky.dds` | `953b502bdc71ad4887963b69e82adb00f1d67d0bb77c0ff5424efe181ab5e597` | 156x210 | `docs/assets/chaos_warfare_historical_advisors_v4/SOV_nikolay_zelinsky/SOV_nikolay_zelinsky_65x67.png` | `5eed366d4f92dc9ead90ac03a426abe4cd3666112dc6f12161e2e11b6d0e850b` | `gfx/interface/advisors/cbrn/SOV_nikolay_zelinsky.dds` | `fc5f3cd74ec1523fd931f46cf9749e5b7e8c31a736158ae74968d5d1efb3633f` | `GFX_idea_SOV_nikolay_zelinsky` |
| `ENG_norman_heatley` | `gfx/leaders/scientists/portrait_ENG_norman_heatley.dds` | `c6a6cda2ac310f17d891cc69093c9255bb881fb0c347164ac3ea1a44803b6367` | 156x210 | `docs/assets/chaos_warfare_historical_advisors_v4/ENG_norman_heatley/ENG_norman_heatley_65x67.png` | `edb1bb61249e010f0ac4d36da71c9de7fbfd6015c6c899c2b9671dafeeb1049d` | `gfx/interface/advisors/cbrn/ENG_norman_heatley.dds` | `b63353dd81291e7f23928fd9c088442be2b285113b1b6fd549a0e4c26805ceca` | `GFX_idea_ENG_norman_heatley` |
| `USA_stanhope_bayne_jones` | `gfx/leaders/scientists/portrait_USA_stanhope_bayne_jones.dds` | `9969c617aaf5d9e315a8c47a69a578d31012828fbdd025cb796a996f372a1f5d` | 156x210 | `docs/assets/chaos_warfare_historical_advisors_v4/USA_stanhope_bayne_jones/USA_stanhope_bayne_jones_65x67.png` | `17a66ffd2e415f464c45271f3b6ea94523e1aae390eb2167e27800437f8a7f5a` | `gfx/interface/advisors/cbrn/USA_stanhope_bayne_jones.dds` | `05870d7622e3b30fc6bb5e25a9341c755e711589c059af8174b43cc8d563e8e2` | `GFX_idea_USA_stanhope_bayne_jones` |

Each source DDS remains in `gfx/leaders/scientists/` and decodes as opaque RGBA `156x210` (`A=255`). Each processed PNG and runtime DDS is `65x67`, with alpha `0..255`; the PNG, processor DDS, and runtime DDS decode to identical pixels. The runtime DDS is one-level uncompressed BGRA, has texture caps and the standard 128-byte header, and is exactly `17,548` bytes.

## Reference and portrait treatment

The installed vanilla advisor reference was checked against `interface/ideas.gfx:3384-3385`, which registers `GFX_idea_generic_political_advisor_african_1` to the `65x67` texture `gfx/interface/ideas/idea_generic_political_advisor_africa_1.dds`. Vanilla `common/characters/GER.txt:524-535` uses `small = GFX_idea_erwin_rommel` in the portrait block for a high-command advisor. The canonical 65x67 advisor reference family and `advisor_template.png` were inspected before production.

The cards use the approved full portrait canvases under the unchanged canonical advisor dossier template. The frame is the top layer; the source was not pre-cropped, stretched, or replaced. The centered transform uses `-4.76` degrees, aspect-preserving cover, `2` px under-frame bleed, and `1` px resampling edge guard. The template SHA-256 is `8f594ef62afba6fdec58de66a80609350dcfe884320b11e6cb6220f1a0e19f58`.

The tool measured an opening-fill plane of approximately `30.477406 x 45.094508` px. Its exact boundary coordinates tripped a strict floating-point containment check, so the generated candidates use `30.47 x 45.09` px within the processor’s `0.01` px geometry tolerance. Center and angle remain unchanged, leaving a sub-pixel inset. The existing processor default `0.18` sepia blend was used for all three cards.

The processed PNGs were converted to the runtime paths with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. The standard converter output is byte-identical to the processor DDS for all three cards.

## Wiring and review

`interface/cbrn_historical_advisors.gfx` registers each stable sprite exactly once and points to the runtime DDS shown above. The parent placed all three single-definition dual-role characters in `common/characters/cbrn_historical_specialists.txt` and assigned their `GFX_idea_<ID>` sprites through `portraits.civilian.small`. The vanilla high-command example places its small field under `portraits.army`; either category supports an advisor small portrait. The portrait worker did not change character definitions or advisor gameplay.

The parent agent reviewed the native-scale contact sheet on 2026-09-27 and passed face recognizability, frame consistency, and alpha presentation on light, dark, and checker backgrounds. The review sheet is `docs/assets/chaos_warfare_historical_advisors_v4/review_contact_sheet.png`. The detailed per-card validation record is `docs/assets/chaos_warfare_historical_advisors_v4/validation_report.json`; both live in the ignored working evidence package.

Each card reports `opening_alpha_gap_pixels=0`, `inner_edge_alpha_gap_pixels=0`, and `exterior_alpha_leak_pixels=0`. Live-game consumer validation was not performed; the user owns that check. No fallback, face substitution, or unapproved source was used.
