# Event 006 Pacific Focus-Tree Re-audit

Date: 2026-07-18
Auditor and implementer: `chaosx_focus_tree_auditor`
Scope: IW-173 HAW, IW-179 FSM, IW-184 HBX, and their preformation FORM-48 focus seams
Current result: **PASS for the resolved Pacific focus tranche; package attestation and FORM-48 readiness remain fail-closed**

## Readiness recommendation

The focus-side P1 findings from the first pass are resolved. Do not infer a
package-admission or FORM-48-readiness promotion from this bounded result.
IW-173, IW-179, and IW-184 must remain absent from runtime content attestation,
and `independence_wave_form48_readiness_attested` must remain unset, until the
parent completes the coordinated country-package, registry, preformation, and
postformation audits. This tranche did not change either gate.

## Required references consulted

- repository `AGENTS.md`;
- repo skills `chaos-redux-subagents`, `chaos-redux-events`,
  `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, and
  `chaos-redux-event-assets`;
- offline wiki snapshot pages for Data structures, Triggers, Effects,
  Modifiers, Localisation, Scopes, On actions, Event modding, Decision
  modding, Idea modding, AI modding, National focus modding, and Interface
  modding;
- official vanilla documentation for script concepts/constants, triggers,
  effects, decisions, and focus inlays;
- vanilla `generic.txt`, `baltic_shared.txt`, Bulgarian `focus_progress`
  precedents, and the HAW/FSM country histories; and
- accepted Event 006 specs, candidate rows IW-173/IW-179/IW-184, FORM-48 plan,
  the Pacific country-package re-audit, and the Pacific icon-family handoff.

## Changed files

- `common/national_focus/006_independence_wave_pacific_focus.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_pacific_decisions.txt`
- `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`
- `localisation/english/006_independence_wave_pacific_l_english.yml`
- `interface/006_independence_wave_pacific_focus_icons.gfx`
- `docs/events/006_independence_wave/pacific_country_packages.md`
- `docs/plans/006_independence_wave_plans/006_form48_pacific_federation_implementation_plan_2026_07_16.md`
- this re-audit handoff

The separate icon-production lane supplied the fourteen final DDS files and
their source/processed/validation package under
`docs/assets/006_independence_wave/pacific_focus_icons_2026_07_18/`.

## Current criterion results

| Criterion | Result | Evidence |
| --- | --- | --- |
| Exact HAW tree isolation | **PASS** | Only exact active IW-173 HAW with `generic_focus` can initialize. Setup assigns `full_framework`; prepared proof requires `independence_wave_focus_tree`, the full-framework flag and variable, and absence of the additive flag. Living, non-Event-6, Soviet-collapse, and meaningful non-generic HAW therefore fail closed. |
| HAW guarded cleanup | **PASS** | Cleanup is scoped to `original_tag = HAW` plus package ID IW-173 and restores `generic_focus` only if the current tree is still `independence_wave_focus_tree`. It does not overwrite a later third-party or owning tree. |
| HAW leadership preservation | **PASS** | Setup proof requires the preserved vanilla ruling leader. No HAW character is recruited, promoted, retired, replaced, or given an adviser role. Vanilla identity, history, flags, and leader portraits remain the owning surfaces. |
| HAW government routes | **PASS** | The full framework owns constitutional, popular-council as labor, traditional, and patron-client routes. Emergency-military and radical-sovereignty are explicitly excluded. Route flags are published before `mark_focus_tree_layout_dirty`, and setup proof checks the positive and negative route contract. |
| HAW Level-2 focus depth | **PASS** | Seven material, country-specific shared focuses form a 35/49/70-day fork-and-rejoin branch and are imported through the final shared focus. Rewards change Shipping Security, Event 6 state, former-host relations when a living host exists, network cooperation, ambition, and FORM-48 delegation state. |
| FSM owning-tree safety and routes | **PASS** | FSM remains additive and never loads a tree. Its adjacent country-package surface provides four mutually exclusive timed settlements: federal council through popular-council, traditional leaders, constitutional government, and patron client; emergency and radical routes are excluded. |
| HBX focus depth and pacing | **PASS** | The existing seven-node 35/49/70-day branch remains attached to the full framework. From 26 Coastal Command, Screen (+10), both early institutions (+10 each), and Bind (+15) reach 71 against the stable threshold of 68. Including Prepare Capital Administration, this is 217 focus days within the 240-day founding mission. |
| Focus/project concurrency | **PASS** | Five HBX and four HAW result-sharing pairs are bidirectionally exclusive. A focus cannot start while its paid project is active; a project cannot start after the matching focus completes or once vanilla `focus_progress` is above zero. One-shot adapters and authoritative bypass flags remain the single result source. |
| Layout and reference integrity | **PASS with MCP render limitation** | All national-focus definitions are unique and all parsed target references resolve. HBX occupies x 89-91/y 1-5 and HAW x 97-99/y 1-5. Same-coordinate RHI/BAY peers are hidden by mutually exclusive exact-package `allow_branch` gates; neither Pacific group has an internal collision. |
| AI behavior | **PASS** | Institution and security focuses have urgent/high weights; living-host work is preferred when relevant; final FORM-48 work is suppressed without host collapse and strongly preferred on the accepted collapse/signature conditions. FSM route projects have their own exact-package AI selection. |
| Localisation | **PASS** | All fourteen Pacific focuses have title, description, and effect-tooltip keys. HAW wording describes material shipping, coastwatch, government, host-account, mandate, and delegation outcomes without implementation-history language. |
| Focus icon wiring | **PASS** | Fourteen unique base sprites and fourteen matching `_shine` sprites are registered once. All fourteen focus icon references resolve exactly, all fourteen 94x86 BGRA DDS textures exist, and there are no orphan base sprites. No ID has a trailing `_focus`. |
| Adviser-asset boundary | **PASS** | The tranche creates no adviser icon, adviser DDS, small portrait, placeholder, or fallback. The Pacific icon package contains national-focus art only. |

## HAW branch proof

| Focus | Required predecessor(s) | Duration | Material result |
| --- | --- | ---: | --- |
| `independence_wave_haw_reconcile_shipping_registers_focus` | Prepare Capital Administration | 35 days | +15 Shipping Security and administration progress |
| `independence_wave_haw_organize_island_coastwatch_focus` | Reconcile Shipping Registers | 49 days | +15 Shipping Security and security reform |
| `independence_wave_haw_seat_island_government_compact_focus` | Reconcile Shipping Registers | 49 days | +10 Shipping Security and public settlement |
| `independence_wave_haw_bind_shipping_supply_and_coastwatch_focus` | both early branches | 49 days | +15 Shipping Security and stabilization |
| `independence_wave_haw_settle_base_and_property_accounts_focus` | binding focus | 49 days | +10 Shipping Security, living-host account settlement when applicable, and diplomatic progress |
| `independence_wave_haw_ratify_autonomous_pacific_mandate_focus` | binding focus, network membership, recognized status | 49 days | ambition and network cooperation |
| `independence_wave_haw_dispatch_pacific_delegation_focus` | both late branches, stable Shipping Security, recognized status | 70 days | diplomatic progress and FORM-48 delegation readiness |

Starting Shipping Security is 34. Reconcile and Coastwatch reach the stable
threshold of 64 after 119 focus days when the 35-day shared prerequisite is
included. The full pressure-producing branch reaches 99 and remains inside the
shared 0-100 clamp. The branch has no free-unit dump, repeatable reward, or
hardcoded tuning value.

## Concurrency pairs

The five preserved HBX authoritative bypass/project pairs are Screen Federal
Arsenals, Reopen Coastal Supply Bureaus, Seat Sacramento Civic Convention,
Settle Federal Asset Ledger, and Charter Pacific Procurement Board. The four
HAW focus/project pairs are Reconcile Shipping Registers, Organize Island
Coastwatch, Settle Base and Property Accounts, and Dispatch/Authorize Pacific
Delegation. Each pair uses the same guarded scripted adapter regardless of
entry surface.

## Icon evidence

`interface/006_independence_wave_pacific_focus_icons.gfx` contains exactly 28
sprite blocks: fourteen base IDs and fourteen `_shine` IDs. They point to
fourteen distinct files under `gfx/interface/goals/006_independence_wave/`.
The asset validation ledger records 94x86, one-level, 32-bit BGRA8888 DDS
headers, alpha range 0-255, and source/runtime hashes for every row. Native and
3x contact sheets were visually reviewed by the parent and passed for
distinctness, readability, and HOI4 focus-icon coherence.

## HOI4 MCP limitation

The required MCP routes were attempted but could not produce a deterministic
render:

1. inspecting `independence_wave_focus_tree` returned
   `ARTIFACT_STORAGE_LIMIT` with zero artifacts;
2. rendering `common/national_focus/006_independence_wave_focus.txt` returned
   `RENDER_DIMENSIONS_BLOCKED` with zero artifacts; and
3. inspecting the shared-focus-only Pacific file returned
   `FOCUS_TREE_NOT_FOUND`, as it contains no standalone `focus_tree` block.

No rewrite was requested. Source-level definition/reference, prerequisite,
coordinate, route, reward, localisation, decision-concurrency, sprite, texture,
and DDS validation supplied the available evidence. The MCP storage/render
condition is a tooling limitation, not a gameplay fallback.

## Simplifications, omissions, and blockers

No fallback, placeholder, route omission, missing focus, missing localisation,
missing AI behavior, or missing focus asset remains inside this focus tranche.
Deterministic MCP rendering remains unavailable for the reasons above. Package
content attestation and FORM-48 readiness remain deliberately unpromoted until
the parent completes the wider coordinated admission audit. No commit was
created by this subagent.
