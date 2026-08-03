# Event 006 IW-025 — current Vojvodina overlay country-package audit

Date: 2026-08-03.

Scope: current-source audit of the IW-025 Vojvodina vanilla-route overlay adapter. Obsolete pasted flag-log claims were excluded.

Disposition: SOURCE PASS for the bounded HUN-origin `vojvodina` adapter, but NOT ADMITTED as a selectable Event 006 country package. No gameplay source edit was made in this audit.

This handoff supersedes the current-status portions of `subagent_handoffs/006_iw025_vojvodina_overlay_adapter_2026_07_28.md`. The older handoff remains implementation history, while this receipt records the current source and blocker state.

## Source contract

Vanilla `common/national_focus/yugoslavia.txt` creates the carrier in the release focus around the `create_dynamic_country` block at lines 1558-1576. The block uses `original_tag = HUN`, cores and transfers state `45`, assigns cosmetic tag `vojvodina`, puppets the carrier, and prepares a `Yugoslavian Division` template. The current Chaos Redux adapter observes that carrier and never creates a country, transfers a state, changes autonomy, replaces the carrier focus tree, or creates a new identity asset.

The accepted map anchor is state `45`, the installed vanilla `history/states/45-Yugoslavia.txt` state with victory point `619`, owner `YUG`, cores `YUG` and `SER`, infrastructure `3`, and no IW-025 state-history override. The reservation ledger keeps state `45` in `RG-DANUBE-BORDERLAND` alongside the separate IW-023, IW-024, IW-031, and IW-032 anchors.

## Country package coverage checklist

| Surface | Current result | Evidence and identifiers |
| --- | --- | --- |
| Carrier identity | PASS | `is_independence_wave_iw025_vojvodina_route_active` in `common/scripted_triggers/006_independence_wave_iw025_vojvodina_triggers.txt:12-18` requires `exists = yes`, `is_dynamic_country = yes`, `original_tag = HUN`, `has_cosmetic_tag = vojvodina`, and rejects `independence_wave_iw025_vojvodina_permanent_identity_loss`. |
| Vanilla route ownership | PASS | Vanilla `common/national_focus/yugoslavia.txt:1558-1576` is the authoritative creation and puppet route. The adapter does not shadow the route or alter its dynamic-country contract. |
| State and host preservation | PASS | `has_independence_wave_iw025_vojvodina_anchor_control` requires both `owns_state = 45` and `controls_state = 45` in `...iw025_vojvodina_triggers.txt:32-35`; the watch objective adds `divisions_in_state = { state = 45 size > 0 }` at lines 37-47. No map or state-history write is present. |
| Narrow runtime hooks | PASS | `common/on_actions/006_independence_wave_iw022_dalmatia_on_actions.txt:9-59` calls `independence_wave_iw025_vojvodina_refresh_overlay` exactly once in each `on_daily_D01` through `on_daily_D50` hook. No global `on_daily`, weekly, or monthly iterator is used. |
| Paid decisions | PASS | `common/decisions/006_independence_wave_iw025_vojvodina_decisions.txt` defines five costed actions: `independence_wave_iw025_compile_danube_depot_survey`, `independence_wave_iw025_establish_mounted_frontier_reserve`, `independence_wave_iw025_mobilize_border_watch`, `independence_wave_iw025_charter_municipal_minority_guarantees`, and `independence_wave_iw025_establish_federal_agrarian_compact`. Each has route visibility, an availability gate, a custom cost trigger/text pair, a payment effect, and an effect tooltip. |
| Timed mission | PASS | `independence_wave_iw025_hold_vojvodina_border_watch` in `...iw025_vojvodina_decisions.txt:92-118` is activated by the paid mobilisation action, requires 45 continuous objective days, has a 135-day timeout, and defines completion, cancellation, timeout, AI, and anchor-garrison behavior. |
| Value and idea lifecycle | PASS | `common/script_constants/006_independence_wave_iw025_vojvodina_constants.txt` centralizes the three values, caps, gains/losses, costs, AI weights, and 30-day suspension timing. `common/scripted_effects/006_independence_wave_iw025_vojvodina_effects.txt:19-75` refreshes the four lifecycle ideas from route and settlement state. |
| Route-loss lifecycle | SOURCE PASS | `...iw025_vojvodina_effects.txt:275-332` suspends and resumes before the grace limit; lines 292-317 extend the active mission by one day per inactive hook; lines 186-201 remove the mission, ideas, runtime flags, and hold progress at permanent identity loss. The old P3 claim that hold progress remained stale is superseded by the live reset at line 199. Exact engine ordering between a mission timeout and the daily hook remains a runtime boundary. |
| Localisation and UI | PASS with a P3 wording note | `localisation/english/006_independence_wave_iw025_vojvodina_l_english.yml` is UTF-8 with BOM and covers the category, five actions, mission, costs, blocked costs, tooltips, and four ideas. Three effect strings display negative loss constants after wording such as “lose” (`lines 17, 36, and 43`), yielding text such as “lose -5”; this is a player-facing clarity issue shared with sibling overlays and was not changed under the no-gameplay-edit scope. |
| Focus ownership | PRESERVED, admission closed | Vanilla HUN uses `hungarian_focus` in `common/national_focus/hungary.txt:9-10`, but the dynamic Dxx carrier's final owner is not source-registered. IW-025 has no `shared_focus`, `load_focus_tree`, `independence_wave_assign_focus_framework`, or carrier receipt. The accepted generic-focus audit therefore correctly keeps this route overlay-only. |
| Ideas and assets | PASS for overlay scope | `common/ideas/006_independence_wave_iw025_vojvodina_ideas.txt` defines the four route-gated ideas and reuses registered shared idea pictures. Decision and mission icons resolve to registered `GFX_decision_independence_wave_government_actions`, `GFX_decision_independence_wave_army_integration_actions`, and `GFX_decision_independence_wave_integration_missions` sprites in `interface/006_independence_wave.gfx`. No new flag, portrait, focus icon, or advisor art is required for the overlay. |
| Politics, leaders, parties, and advisors | Carrier-preserved | The route uses the vanilla dynamic HUN-origin carrier and the vanilla Yugoslav release's party setup. No IW-025 character, leader, portrait, advisor, party, country-name, or country-history file exists. Live leader continuity and post-release political behavior remain unverified and are not replaced by an invented identity. |
| Military, technology, industry, supply, and production | Carrier-preserved | No IW-025 OOB, division, technology, research-slot, factory, railway, port, resource, fuel, train, convoy, or production override exists. The route consumes the centralized command power, manpower, train, infantry equipment, support equipment, and army experience costs and requires a real garrison in state `45`; no free formation effect is added. |
| AI and playability | SOURCE PASS, runtime evidence open | All five actions and the mission have AI weights in `...iw025_vojvodina_decisions.txt:26-170`. Mobilisation is AI-disabled without a qualifying garrison, preparation is weighted high, settlement weights respond to war status, and the mission is urgent. No live AI survival, weighted-selection, save/load, or mission-order evidence is claimed. |
| Network, League, formable, and package admission | NOT ADMITTED | No IW-025 source registers Network, League, formable, central package dispatch, scenario admission, or full Event 006 focus validation. `common/scripted_triggers/006_independence_wave_form08_triggers.txt:4-9` explicitly excludes the Vojvodina overlay as a new country. |

## File surface checklist

The live IW-025 source surfaces are:

- `common/script_constants/006_independence_wave_iw025_vojvodina_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw025_vojvodina_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw025_vojvodina_effects.txt`
- `common/ideas/006_independence_wave_iw025_vojvodina_ideas.txt`
- `common/decisions/categories/006_independence_wave_iw025_vojvodina_categories.txt`
- `common/decisions/006_independence_wave_iw025_vojvodina_decisions.txt`
- `common/on_actions/006_independence_wave_iw022_dalmatia_on_actions.txt` for the shared D01-D50 hook table
- `localisation/english/006_independence_wave_iw025_vojvodina_l_english.yml`

The current contract and admission surfaces checked were:

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` row `IW-025`, whose provisional token `AYX` is not a runtime tag and whose resolved tag is empty under `reuse_vanilla_route_overlay`.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` row `IW-025`, which requires the HUN-origin `vojvodina` identity and preserves the vanilla Yugoslav creation route.
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv` row `RG-DANUBE-BORDERLAND`, which includes anchor `45`.
- `common/country_tags/006_independence_wave_countries.txt`, whose header explicitly excludes vanilla route/cosmetic overlays from standalone Event 006 tag registration.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`, which contains no IW-025 package adapter and applies the generic focus-contract barrier only to admitted packages.
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt`, `common/scripted_effects/006_independence_wave_focus_effects.txt`, and `common/national_focus/006_independence_wave_focus.txt` for the reviewed full/additive focus contract.
- `common/scripted_triggers/006_independence_wave_form08_triggers.txt` and `docs/events/006_independence_wave/systems/formable_registry.md` for the fail-closed Danubian formable boundary.
- Vanilla `common/national_focus/yugoslavia.txt`, `common/national_focus/hungary.txt`, `history/states/45-Yugoslavia.txt`, and the relevant vanilla documentation for effects, triggers, decisions, missions, and focuses.

## Missing or stale country-package surfaces

The route remains intentionally `vanilla_route_overlay_only` and `overlay_nonselectable`. Its registry provisional token `AYX` must not be promoted to a country tag without a new identity and asset review.

No static HUN owner-tree copy imports the shared Event 006 overlay root, no route-specific additive carrier receipt exists, and no safe dynamic `load_focus_tree` operation can be added without replacing the living carrier tree. This is the principal focus and package-admission blocker.

No IW-025 source writes Network membership, League availability, formable membership, patron relations, central package dispatch, scenario ranking, host-survival setup, save/load cleanup, or runtime carrier evidence. These are package-promotion blockers rather than defects in the accepted overlay-only source contract.

No IW-025 country tag, history, state override, leader, portrait, flag, advisor, party, OOB, technology, industry, supply, or production surface is present. That omission is correct for the non-selectable vanilla-route overlay and would become a blocker only if the route is promoted to a standalone package.

The old lifecycle re-audit `006_overlay_watch_permanent_identity_loss_reaudit_2026_08_03.md` still describes the pre-reset P3 hold residue. The current source at `...iw025_vojvodina_effects.txt:199` resets the hold variable, so that paragraph is historical and superseded rather than an open source defect.

## Map and state setup issues

State `45` is a valid installed vanilla state and the source route transfers it to the dynamic carrier. The local trigger's owns-and-controls check and the watch garrison check make current state control authoritative. No map rewrite, railway, port, resource, building, supply, or victory-point adjustment is needed for the overlay contract.

The reservation group `RG-DANUBE-BORDERLAND` contains several distinct package anchors. IW-025 uses only state `45`, while FORM-08 uses separate TRA/AXX/MAC anchors and does not admit this dynamic overlay as a member.

## Politics, leader, portrait, flag, advisor, and party issues

The adapter preserves the vanilla dynamic carrier's existing politics and route identity. It does not invent a Vojvodina leader, portrait, flag, advisor, party, or council. Any future standalone promotion would require researched identity, sourced leader/portrait, flag, party, advisor, and focus-owner decisions before admission.

## Focus, decision, idea, and asset issues

The five visible decisions, one timed mission, four route ideas, and category are fully localized and use existing registered icons. The watch threshold closes through the current centralized chain: Provincial Legitimacy starts at `28`, depot survey adds `8`, mounted reserve costs `5`, and successful watch adds `34`, reaching `65`; River Logistics and Border Mobility also reach their respective settlement gates through the same paid chain.

No focus node, focus localisation, focus icon, decision icon, idea icon, flag, portrait, or advisor asset was added by this audit. The only noted local wording issue is the negative loss-value display described in the coverage table.

## Starting military, technology, industry, supply, and production issues

The vanilla dynamic route owns the starting setup, including its `Yugoslavian Division` template and the route-created Vojvodinian division. The overlay adds no starting force, technology, factory, supply, rail, port, resource, fuel, train, convoy, or production changes. Its costs are paid from the carrier's actual stocks and its border-watch requirement uses a real state `45` division.

## AI and playability issues

Source-level AI weights are present for each action and the mission, with garrison gating and war/peace modifiers. The route still has no generic focus AI, package admission, Network/League/formable behavior, or live runtime proof. Save/load continuity, mission timeout ordering, temporary route loss, permanent route loss, and dynamic carrier leader behavior remain user-side runtime validation boundaries.

## Validation performed

- Required offline Paradox wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, national focuses, and country creation.
- Relevant vanilla documentation was read for effect, trigger, decision, mission, focus, script-constant, and variable behavior.
- `python -B .tools/audit_event6_allocator.py` passed with the current repository publisher, reservation, scenario, and ordering counts.
- `python -B .tools/audit_event6_flags.py` passed with `102` complete Event 006 flag families and `0` incomplete families.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` reported `0` external country-definition collisions and `0` external identity-surface collisions.
- A bounded source check passed the exact HUN/`vojvodina` identity, state `45` ownership/control/garrison checks, 50 D01-D50 refresh calls, no focus-load or country-creation effects, permanent hold reset, balanced touched script blocks, decision localisation coverage, shared GFX references, and UTF-8 BOM localisation encoding.
- Vanilla Yugoslav and Hungarian focus sources and vanilla state `45` were inspected as route and map precedents.

Hearts of Iron IV was not launched. No live, save/load, weighted-AI, mission-order, focus-render, or map-write evidence is claimed.

## Changed files and patch disposition

Changed by this audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw025_vojvodina_overlay_audit_current_2026_08_03.md` only.

No gameplay source, tag, state, leader, party, focus, decision, mission, idea, localisation, asset, map, or registry admission patch was made. A concurrent parent edit in `common/ideas/006_independence_wave_iw025_vojvodina_ideas.txt` mirrors static modifier values into file-scoped constants; this audit did not touch or claim that edit.

## Remaining blockers and next actions

- Keep IW-025 non-selectable and keep its provisional registry token `AYX` out of runtime tag registration.
- Select and document a reviewed HUN-origin focus-owner contract before adding any shared-focus import or carrier receipt.
- Keep Network, League, formable, package dispatch, scenario, and runtime admission fail-closed until their separate source contracts exist.
- Correct the three negative loss-value localisation strings in a coordinated sibling-overlay localisation pass if the parent authorizes that player-facing edit.
- Perform live dynamic-carrier, mission-timeout, temporary-loss, permanent-loss, save/load, leader, and AI validation only in a separately authorized runtime pass.

No fallback, placeholder country, new tag, identity redesign, or gameplay simplification was introduced by this audit.
