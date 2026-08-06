# Event 006 Karelia and Crimean Tatar State packages

## Scope

This document records the IW-033 Karelia and IW-041 Crimean Tatar State package adapters. Both use the registered vanilla carriers `KAR` and `CRI`; the event never creates a replacement tag or overwrites vanilla history. A release must first reserve the anchor and former-host state, then run the package setup inside the synchronized Event 006 transaction.

## Current source status (2026-08-06)

The owner-patch reconciliation is recorded in `../../plans/006_independence_wave_plans/subagent_handoffs/006_documentation_curator_iw033_iw041_owner_patch_reconciliation_current_2026_08_05.md`, the prior promotion/count reconciliation is recorded in `../../plans/006_independence_wave_plans/subagent_handoffs/006_documentation_curator_iw033_iw041_post_promotion_reconciliation_current_2026_08_05.md`, and the current parent admission receipt is `../../plans/006_independence_wave_plans/subagent_handoffs/006_iw033_iw041_source_admission_current_2026_08_06.md`. The package source now excludes passive founding missions from the active-project lock, requires a route government before stable-ledger mission success, cancels government routes on capital loss, makes former-host settlement idempotent, clears its decision and settlement flag during cleanup, waits for a live League phase before consuming the network action, and uses the shared reserve/member-confidence helper inputs. Package localisation exposes dynamic ledger values and normal, blocked, and hover cost variants. IW-033 and IW-041 are centrally content-attested inside the current 23-package / 22-compatible-group boundary, with a 20-package static standalone witness that excludes only self-hosting IW-012 ICE. The parent-waived Level 2 country-specific-focus expectation remains a documented shared-tree breadth limitation, and package-specific probability/runtime evidence remains bounded. Event 006's active super-event identifiers remain ordinary `23` for The League of New States and `24` for Every Border a Casus Belli; dated four-digit research identifiers are not runtime package identifiers.

The later owner-AI handoff `../../plans/006_independence_wave_plans/subagent_handoffs/006_iw033_iw041_owner_ai_reserve_floor_patch_2026_08_05.md` records executable decision selection for both packages: regular actions wait for foundation settlement, prefer the lower regional ledger, and receive zero-weight post-spend gates for command power, manpower, equipment, trains, convoys, fuel, and major security reserves. The thresholds are centralized in `independence_wave_karelia_crimea_ai_floor`; the source behavior is current, while the required same-scenario MCP probability comparison and live runtime evidence remain pending.

| Package | Carrier | Region | Anchor | Optional territory | Force profile |
| --- | --- | --- | --- | --- | --- |
| IW-033 | `KAR` Karelia | Eastern Europe / western Russia | state 146 Karelia | state 147 Salla; states 215 and 216 only when the locked extended plan admits them | `mountain_frontier`, p33 |
| IW-041 | `CRI` Crimea | Eastern Europe / western Russia | state 137 Crimea | none in the compact package | `mounted_mobile`, p41 with approved navy/air inheritance |

The frozen anchor is also the runtime capital. Karelia prefers the Finnish former host and preserves a FIN-owned anchor; the Crimean package preserves a SOV-owned anchor. Origin guards keep Soviet Collapse and Event 006 separate. If either carrier is already living, the exact candidate wrapper fails closed and the allocator rerolls before the plan is locked.

## Shared playable contract

Each package receives the shared Event 006 generic focus framework, all four government lanes (constitutional, popular council, traditional, and emergency military), the four host-negotiation lanes, an internal power struggle, a regional ambition family, the league route, dynamic force mapping, AI strategy, and package-specific ideas and decisions. Existing vanilla characters are reused. Karelia keeps Peteris Irklis, Ukki Vainamoinen, and Jalmari Takkinen; the setup promotes Jalmari's existing character to corps commander. Crimea keeps Ilyas Tarkhan and adds a corps-commander role at runtime without adding a new portrait or history entry. The p41 force mapping also enables the accepted conditional navy and air transfer from the saved former host; Karelia's p33 mapping explicitly keeps both inheritance paths off.

The founding mission lasts 210 days. It succeeds only when both package ledgers reach 65, the anchor is owned, controlled, and the capital, the force, focus, host, league, and route receipts are present, and the sovereign is living. A timeout or cancellation lowers the package ledgers, lowers shared recognition/security/capacity, raises instability, and advances a bounded package crisis tier. The former-host settlement and regional-network actions are paid, reversible projects rather than free rewards.

The founding mission is a passive deadline and does not count as an active project. One paid project or government route may run at a time, and each government route cancels into the shared failure bundle if the capital falls while it is underway. Stabilising both ledgers without a government leaves the mission active until the route is chosen. A failed foundation blocks the remaining package actions until the origin cleanup resets the carrier.

The former-host settlement receipt is idempotent. If the paid settlement runs before foundation resolution, the later foundation success does not apply the same relationship bundle a second time. The network corridor also waits for a live league phase so its cohesion, common-cause, reserve, confidence, and network-standing changes are delivered rather than consumed early.

## Package ledgers and actions

Karelia begins with forest supply integrity 36 and civic mandate 42. Its four projects are 30-day railhead reopening (20 command power and 5 trains), 45-day ski guard formation (25 command power, 350 infantry equipment, and 80 support equipment), 45-day language commission (45 command power and 2,500 manpower), and 30-day border transit (35 command power and 8 trains).

Crimea begins with return capacity 34 and land settlement 40. Its four projects are 45-day land survey (45 command power and 2,500 manpower), 30-day return commission (20 command power and 2,500 manpower), 45-day service screen (25 command power, 350 infantry equipment, and 80 support equipment), and 60-day Black Sea customs (30 command power, 15 convoys, and 500 fuel).

Every project changes the package ledgers and the shared country, host, network, or league values. The package cleanup removes missions, decisions, ideas, flags, and variables when the synchronized release transaction ends.

AI decision selection is state-aware rather than comment-only. A valid completed package setup permits the AI to take the ledger and government actions needed to settle its 210-day foundation, while a foundation failure suppresses those actions. The package-specific lower ledger receives a priority multiplier, and every project has an explicit post-spend reserve-floor gate. Karelia uses command-power, manpower, infantry-equipment, support-equipment, and train reserves; Crimea uses the same land reserves plus a convoy-and-fuel floor for Black Sea customs. Major emergency-government actions use separate higher manpower and equipment floors. These thresholds are centralized in `independence_wave_karelia_crimea_ai_floor`, and the reusable predicates live in `006_independence_wave_karelia_crimea_package_triggers.txt`.

## Runtime files and identifiers

The package constants are in `common/script_constants/006_independence_wave_karelia_crimea_constants.txt`. Triggers and effects are split between the matching `common/scripted_triggers` and `common/scripted_effects` files. Decisions and missions are registered in `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`, the category in `common/decisions/categories/006_independence_wave_karelia_crimea_categories.txt`, ideas in `common/ideas/006_independence_wave_karelia_crimea_ideas.txt`, and AI layers in `common/ai_strategy/006_independence_wave_karelia_crimea.txt`. The central dispatcher admits IDs IW-033 and IW-041 in the content-attestation OR-list after the owner promotion. The current allocator audit reports 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 23 attested packages, 22 compatible reservation groups, and 170 unattested selectable rows. Exact host, anchor, reservation, force, scenario, probability, and runtime checks remain required for a live release; central attestation is not a whole-event completion claim.

## Icons and assets

No new leader, advisor, flag, or country-history asset is required for these vanilla carriers. Decisions reuse the registered Event 006 icon families: `GFX_decision_independence_wave_integration_missions`, `GFX_decision_independence_wave_government_actions`, `GFX_decision_independence_wave_army_integration_actions`, `GFX_decision_independence_wave_former_host_negotiations`, and `GFX_decision_independence_wave_league_votes`. If a later visual pass replaces one of those families, the replacement belongs under `docs/assets/006_independence_wave/`, must be listed in its manifest, and must be wired in the relevant interface `.gfx` file before promotion.

## Readiness and future work

The central content-attestation rows are promoted, but each adapter remains bounded by the independent exact-tag, host-survival, allocator, scenario, probability, and runtime checks that decide a live release. No bespoke focus tree is introduced: the accepted design is the one shared generic tree with regional package overlays, and the parent-waived Level 2 expectation leaves a documented breadth limitation. FORM-10 remains a separate registry decision and is not silently enabled by either package.
