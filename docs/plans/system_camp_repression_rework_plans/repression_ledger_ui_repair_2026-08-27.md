# Repression Ledger UI Repair, 2026-08-27

## Outcome

The attached decision-category surface and `repression_ledger_window` were rebuilt after the prior pass remained visually rough and exposed implementation-style text.

The category now uses a purpose-built 52x40 decision-category medallion depicting a sealed state dossier, a short country-scoped heading, a bounded three-line status, and one `Review Records` action.

The popup now uses one horizontal five-tab rail: Summary, Territories, Sites, Authority, and Records.

The previous invisible list rows were replaced by visible two-column card grids with six bounded entries for Territories and Sites.

The Summary tab uses four consequence-led cards and a conditional, written warning when guards and transport cannot sustain the administration.

The selected-state frame and contextual orders occupy their own lower region, outside the tab panels.

## Player-facing text

Separator bars, zero-heavy telemetry, developer explanations, and implementation terms were removed from the category and popup.

Active, dormant, and reforming administrations receive different summary sentences, so a dormant German or Japanese administration no longer reads as an active zero-site debug record.

The live Germany, Japan, and Soviet Authority strings were traced through `camp_repression_country_kits_l_english.yml` and rewritten there rather than only in the general ledger file.

Every country-specific action name and description now requires both its action id and the matching original country tag. A stale action id therefore falls back to no available directive instead of exposing another country's wording.

The Soviet branch identifies the Gulag, NKVD authority, state paranoia, grain seizures, and famine aftermath. It contains no Japanese institution, name, site, or fallback string.

## Layout bounds

The 900x560 popup uses these non-overlapping authored regions:

- Summary strip: `x=18..882`, `y=48..100`.
- Horizontal tabs: `x=18..846`, `y=102..144`.
- Tab panels: `x=28..872`, `y=154..428`.
- Selected-state frame: `x=95..805`, `y=432..470`.
- Contextual orders: `y=474..554`, leaving six pixels inside the window.

Panel and action overlap is permitted only where scripted visibility makes the consumers mutually exclusive, such as site orders versus national guard and quota orders.

All six Territory cards and all six Site cards resolve their detailed tooltip keys; they no longer resolve to the one-word `Select` button labels.

## Icon package

Runtime sprite: `GFX_decision_category_repression_ledger`.

Runtime DDS: `gfx/interface/camp_repression/decision_category_repression_ledger.dds`.

The DDS is a one-level 52x40 legacy BGRA texture with preserved transparency and a pixel-identical decoded round trip.

The former 53x53 crate-and-optics texture was removed after its only sprite consumer was rewired.

Source, processing evidence, prompt, previews, and the manifest are retained under `docs/assets/system_camp_repression_rework_ui_repair/`.

## Documentation alignment

The scripted-GUI specification now describes the live horizontal rail, four-card Summary panel, two-column list cards, concise category attachment, and prohibition on invisible debug rows and separator telemetry.

## Validation evidence

Source validation found no missing GUI elements for Repression Ledger visibility triggers, no duplicate GUI element names, no unresolved sprite registrations, and balanced GUI braces.

The localisation files retain UTF-8 BOM encoding and the edited localisation set has no duplicate keys.

The mandatory HOI4 GUI MCP inspect, rewrite, and render routes were attempted after the repair, including 1920x1080 and 1280x720 long-text, empty-list, full-list, selected, and warning scenarios.

All current post-change calls were blocked before scanning with `SCAN_BYTE_LIMIT: Scan exceeds the configured byte limit` in workspace `mod_chaos_redux_ea3b2d67c2c0`, so no post-change engine-render artifact exists and source validation is not presented as equivalent visual proof.

## Simplifications, omissions, and blockers

No fake layout, placeholder art, or alternate three-tab simplification was used.

Post-change MCP visual evidence remains blocked by the workspace scan-byte limit. In-game consumer validation remains with the user under the repository testing boundary.
