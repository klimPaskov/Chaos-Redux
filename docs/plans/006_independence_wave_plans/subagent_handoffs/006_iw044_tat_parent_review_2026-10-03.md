# IW-044 Tatarstan parent review (2026-10-03)

## Scope and acceptance

This review covers the accepted TAT founding-government gate, five shared focuses, localization, and a narrow affordability/deadline correction.
TAT's anchor is state 249 Kazan; IW-039's Millerovo/state 245 contract is unrelated.
The user directed continuation without waiting for input and selection of recommended choices on 2026-10-03.
Within that authorization, the parent accepted preserving project costs and durations, setting the founding deadline to 720 days, and giving the existing assembly reward a deficit-only four-civilian-factory target in Kazan.

## Source findings and correction

The ordinary project gate requires founding-mission resolution, while the four government projects use the active-mission gate and their own serialization check.
The generic founding-mission serialization list excludes the TAT package mission, so it does not prevent DM-04/DM-05 from supplying their route flags.
DM-04 and DM-05 set those flags in `complete_effect` when selected; their active factory reservations may still delay the subsequent TAT administration project.
Cancellation of the package mission requires an installed government, stable ledgers, and retained anchor/capital control for success; otherwise loss or timeout records failure and closes the route projects.

The source assigns the full tree before publishing TAT setup completion and origin/network activation receipts.
Because `allow_branch` is checked at tree loading, the full package gate is false at that early assignment.
The origin-activation helper now includes IW-044 alongside the existing IW-039 refresh guard and calls `mark_focus_tree_layout_dirty` only after the current country's setup and aligned network/active-country receipts are ready.
This preserves the package gate, adds no world iteration, and retains the loaded tree and focus progress.

Installed vanilla `history/states/249-Kazan.txt` has one military factory and no civilian factories at the 1936 start.
The previous source offered no local factory reserve before the government project's factory requirements.
The assembly/depot hook adds only `target - building_level@industrial_complex` when positive, in owned and controlled state 249, and adds matching shared slots.
The existing depot-completion flag guards the whole hook, so a repeat call cannot grant factories or pressure rewards again.
Inputs with zero, one, three, four, or five existing civilian factories produce totals of four, four, four, four, or five respectively; military factories and prior civilian industry remain intact.

## Four-route source arithmetic

The starting Civic Concord/River Security values are 38/44.
Assembly, communities, and guards add 15/5, 15/10, and 5/15, reaching 73/74.
The stable threshold is 60 in each ledger.

| Government | Values after three common focuses and government | Project duration |
| --- | --- | --- |
| Constitutional | 88 / 79 | 75 days |
| Agrarian | 88 / 84 | 180 days |
| Socialist | 78 / 89 | 75 days |
| Emergency | 68 / 94 | 120 days |

The generic founding-focus requirements total 336 nominal days: four five-point focuses and four seven-point focuses at the default seven days per point.
Constitutional and traditional route preparation/locking add 84 days; popular and emergency route locking add 49.
The three common TAT focuses take 105 nominal days and can run while a government project is active.

| Government | Nominal earliest joint completion with costs already affordable | Margin to 720-day deadline |
| --- | --- | --- |
| Constitutional | 525 days | 195 days |
| Agrarian | 600 days | 120 days |
| Socialist | 490 days | 230 days |
| Emergency | 505 days | 215 days |

For the constitutional route, an active DM-04 factory reservation can postpone the TAT project despite its route flag already being set.
If the only available factory capacity is occupied until the nominal day-551 reservation expiry, the 75-day TAT project completes at day 626, leaving 94 days before the deadline while the common TAT focuses finish earlier.
These are explicit source witnesses under retained capital/anchor control, normal focus speed, affordable manpower/command/equipment/transport, completed generic founding missions and capstone value requirements by the listed dates, and no unrelated project reservations; they are not executed campaign or AI evidence.
The installed civilian-economy law specifies `consumer_goods_expected_value = 0.35`; the four-factory target also leaves a construction base for later growth, but live availability and other country modifiers remain engine-dependent checks.

## References and evidence limits

Offline `National focus modding - Hearts of Iron 4 Wiki.md`, lines 297–301, documents the default cost-to-days conversion; its prior revision is `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`.
Offline `Decision modding - Hearts of Iron 4 Wiki.md`, lines 268–276 and 338–343, documents immediate `complete_effect`, delayed `remove_effect`, and active modifiers.
Offline `Effects - Hearts of Iron 4 Wiki.md`, lines 3613–3615, documents variable-backed building levels and shared-slot grants.
Installed `documentation/effects_documentation.md`, lines 839–847 and 1267–1275, identifies both building effects as state-scoped; revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Installed `common/decisions/_documentation.md`, lines 1–46, describes visibility and availability requirements; prior revision `5e7e686b5582f32c38d898d805e17171e88f3bfeeea4a030deb1884f9726de019`.
Installed `common/national_focus/baltic_shared.txt`, lines 379–385, provides the shared-slot/instant-civilian-building precedent.
Installed `common/ideas/_economic.txt`, lines 101–116, provides the civilian-economy modifiers.
Offline focus-modding lines 419–420 describe the load-time `allow_branch` check and layout-refresh effect; installed `documentation/effects_documentation.md`, lines 4811–4820, documents the country-scoped refresh, and vanilla `common/national_focus/afghanistan.txt`, line 2972, supplies a precedent.

The parent crosswalk found each of the five new focus IDs once as a definition and once as an import, with both its name and description localization present.
All five reused sprites resolve in `interface/006_independence_wave.gfx` to existing DDS files under `gfx/interface/goals/006_independence_wave/`.
No new visual assets were created or substituted.

Four project audit agents failed before initialization with `workspace routing discovery timed out` and produced no review or patch.
Their failures are recorded rather than treated as completed audits.
A subsequent country-package audit has been requested with an explicit absolute workspace and a narrower scope; its outcome remains separate from this parent source review.
Current focus inspection and a render cropped to the assembly node have also been requested against the single source file; no final result is claimed before those requests return.
Imported shared-focus MCP layout and typed route AI evidence remain open under the accepted shared architecture.
No numeric AI weights changed, and no live game was launched by the parent.
The full Event 006 goal remains **HOLD / PARTIAL**.
