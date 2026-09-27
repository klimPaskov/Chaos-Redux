# CBRN Defensive Advisor Card Production Handoff

Date: 2026-09-27.

## Outcome

Produced and wired three `65x67` CBRN advisor cards from their existing approved `156x210` in-mod scientist portraits: `SOV_nikolay_zelinsky`, `ENG_norman_heatley`, and `USA_stanhope_bayne_jones`. The initial fourth candidate, `USA_james_stevens_simmons`, was excluded by the parent because no distinct accepted gameplay effect was assigned to him.

## Durable source/runtime manifest

The tracked manifest at `docs/systems/cbrn_warfare/cbrn_defensive_advisor_cards_manifest_2026-09-27.md` records the approved source decision, exact source and output hashes, stable sprite/runtime mapping, DDS properties, review state, and parent integration requirement. The detailed contact sheet and per-card processor metadata remain in the ignored `docs/assets/chaos_warfare_historical_advisors_v4/` review package.

## Files changed

- `interface/cbrn_historical_advisors.gfx`
- `docs/systems/cbrn_warfare/cbrn_defensive_advisor_cards_manifest_2026-09-27.md`
- `gfx/interface/advisors/cbrn/SOV_nikolay_zelinsky.dds`
- `gfx/interface/advisors/cbrn/ENG_norman_heatley.dds`
- `gfx/interface/advisors/cbrn/USA_stanhope_bayne_jones.dds`
- `docs/assets/chaos_warfare_historical_advisors_v4/review_contact_sheet.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/validation_report.json`
- `docs/assets/chaos_warfare_historical_advisors_v4/SOV_nikolay_zelinsky/SOV_nikolay_zelinsky_4x.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/SOV_nikolay_zelinsky/SOV_nikolay_zelinsky_65x67.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/SOV_nikolay_zelinsky/SOV_nikolay_zelinsky_alignment_8x.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/SOV_nikolay_zelinsky/SOV_nikolay_zelinsky_metadata.json`
- `docs/assets/chaos_warfare_historical_advisors_v4/SOV_nikolay_zelinsky/SOV_nikolay_zelinsky_placement_study.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/SOV_nikolay_zelinsky/SOV_nikolay_zelinsky_processor.dds`
- `docs/assets/chaos_warfare_historical_advisors_v4/ENG_norman_heatley/ENG_norman_heatley_4x.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/ENG_norman_heatley/ENG_norman_heatley_65x67.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/ENG_norman_heatley/ENG_norman_heatley_alignment_8x.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/ENG_norman_heatley/ENG_norman_heatley_metadata.json`
- `docs/assets/chaos_warfare_historical_advisors_v4/ENG_norman_heatley/ENG_norman_heatley_placement_study.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/ENG_norman_heatley/ENG_norman_heatley_processor.dds`
- `docs/assets/chaos_warfare_historical_advisors_v4/USA_stanhope_bayne_jones/USA_stanhope_bayne_jones_4x.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/USA_stanhope_bayne_jones/USA_stanhope_bayne_jones_65x67.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/USA_stanhope_bayne_jones/USA_stanhope_bayne_jones_alignment_8x.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/USA_stanhope_bayne_jones/USA_stanhope_bayne_jones_metadata.json`
- `docs/assets/chaos_warfare_historical_advisors_v4/USA_stanhope_bayne_jones/USA_stanhope_bayne_jones_placement_study.png`
- `docs/assets/chaos_warfare_historical_advisors_v4/USA_stanhope_bayne_jones/USA_stanhope_bayne_jones_processor.dds`
- `docs/assets/chaos_warfare_historical_advisors_v4/manifest.md`
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-27_cbrn_defensive_advisor_cards_handoff.md`

## Portrait and runtime crosswalk

| Subject | Source DDS SHA-256 | Runtime DDS SHA-256 | Sprite | Runtime texture |
|---|---|---|---|---|
| `SOV_nikolay_zelinsky` | `953b502bdc71ad4887963b69e82adb00f1d67d0bb77c0ff5424efe181ab5e597` | `fc5f3cd74ec1523fd931f46cf9749e5b7e8c31a736158ae74968d5d1efb3633f` | `GFX_idea_SOV_nikolay_zelinsky` | `gfx/interface/advisors/cbrn/SOV_nikolay_zelinsky.dds` |
| `ENG_norman_heatley` | `c6a6cda2ac310f17d891cc69093c9255bb881fb0c347164ac3ea1a44803b6367` | `b63353dd81291e7f23928fd9c088442be2b285113b1b6fd549a0e4c26805ceca` | `GFX_idea_ENG_norman_heatley` | `gfx/interface/advisors/cbrn/ENG_norman_heatley.dds` |
| `USA_stanhope_bayne_jones` | `9969c617aaf5d9e315a8c47a69a578d31012828fbdd025cb796a996f372a1f5d` | `05870d7622e3b30fc6bb5e25a9341c755e711589c059af8174b43cc8d563e8e2` | `GFX_idea_USA_stanhope_bayne_jones` | `gfx/interface/advisors/cbrn/USA_stanhope_bayne_jones.dds` |

`interface/cbrn_historical_advisors.gfx` registers each sprite once and each texture path exists. The parent has added `small = GFX_idea_<ID>` in `portraits.civilian` for all three dual-role character definitions; vanilla `GER_erwin_rommel` uses the same small-card field under `portraits.army` for a high-command advisor. Character definitions and advisor gameplay blocks were left to the parent.

## Source, processing, and review evidence

The cards reuse the parent-approved local masters in `gfx/leaders/scientists/portrait_<ID>.dds`. The user-approved scope did not require restoring the Internet source archive; the manifest records hashes and processing provenance without asserting new source attribution or licensing. No external image, ImageGen output, or RunPod result was used.

The canonical vanilla advisor family and installed `GFX_idea` texture consumer were inspected before production. Each input remained an opaque `156x210` image. The canonical dossier processor composed the full source canvas under the unchanged template using centered placement, `-4.76` degrees, aspect-preserving cover, `2` px bleed, and `1` px edge guard. Because the exact opening dimensions hit the processor's strict floating-point boundary, `30.47x45.09` px was used within its `0.01` px tolerance; no crop, stretch, identity change, or substitute was introduced.

Each processed PNG was converted through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. All final DDS files are `65x67`, one-level 32-bit BGRA, alpha `0..255`, exactly `17,548` bytes, and pixel-identical to both the processed PNG and the processor DDS. The processor reports zero opening, inner-edge, and exterior alpha gaps for each card.

Parent independent visual review passed on 2026-09-27. The parent reported that all three faces remain recognizable at native card scale and that framing and alpha match the advisor family on light, dark, and checker backgrounds. Producer inspection also passed at native and `4x` sizes against the approved masters and canonical reference family.

## Skipped checks and blockers

Live Hearts of Iron IV consumer validation was not performed; the user owns in-game validation. No task blocker remains for these three portrait assets. No unapproved fallback or simplification was used. The source archive and external licensing details were not re-audited because the parent supplied the user's explicit approval and said archive recovery was unnecessary; this handoff makes no new rights claim.
