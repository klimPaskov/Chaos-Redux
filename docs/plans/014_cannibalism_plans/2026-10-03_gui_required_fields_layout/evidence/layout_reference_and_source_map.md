# Event014 Required Fields: Reference and Source Map

Date: 2026-10-03.

Disposition: accepted requirements, proposed placements pending parent selection and accepted data API contract.

Acceptance basis: the current user assignment explicitly accepts E014-FINAL-02/03 completion against `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md`, lines 570-613, and authorizes only the three named Event014 windows and their matching presentation bindings.

The specification requires four additional per-node fields in the Network window, controlled-state identity cards and a raid-target card in the Warlord command window, and a warlord loyalty list plus continental-target cards in the revealed command window.

The current audit `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_final_current_completion_audit.md` classifies these as E014-FINAL-02 and E014-FINAL-03 presentation omissions.

The three reference proposals below use the existing accepted Event014 background and registered card artwork.

They show field names and source bounds only and contain no invented campaign values, persistent facts, new binding identifiers, or new button effects.

## Event ownership and exact surfaces

Event id and slug: `014_cannibalism`.

The event root is `chaosx.nr14.1` in `events/014_cannibalism.txt:18-20`.

The early Event014 header exposes the `cannibalism_network_open` button in `interface/014_cannibalism_frontline_hunger.gui:48`.

`cannibalism_early_header_scripted_gui` in `common/scripted_guis/014_cannibalism_scripted_gui.txt:14-56` binds that control, and its click effect calls `cannibalism_gui_open_network_view` at line 29.

The Network window is `cannibalism_network_window`, bound by `cannibalism_network_scripted_gui` with `player_context` and parent `top_bar` at lines 58-71.

The Warlord window is `cannibalism_warlord_command_window`, bound by `cannibalism_warlord_command_scripted_gui` with `decision_category` context and the unrevealed-warlord visibility gates at lines 155-163.

The revealed window is `cannibalism_revealed_command_window`, bound by `cannibalism_revealed_command_scripted_gui` with `decision_category` context and the post-reveal, non-Wendigo visibility gates at lines 185-193.

The category entries are `cannibalism_containment_category` and `cannibalism_network_alerts_category` for the early header, `cannibalism_warlord_command_category` for the Warlord panel, and `cannibalism_unified_command_category` for the revealed panel in `common/decisions/categories/014_cannibalism_categories.txt`.

These identifiers and gates establish Event014 ownership. The shared event log, Event Details, settings, super-event framework, shared registries, Wendigo window, and unrelated interfaces remain excluded.

## Current source identities and read-only boundary

`interface/014_cannibalism_frontline_hunger.gui` SHA-256: `1c7b33ab8bad6bf26d3505705754ff1d8e10b3edf598a8fb879478fe70fdb591`.

`common/scripted_guis/014_cannibalism_scripted_gui.txt` SHA-256: `70699e7db5e95af1787fef459d077240270f2c4a9bcf324d448c9e5e6e475664`.

Current `interface/014_cannibalism.gfx` SHA-256: `f28d0ca3fffba23effa0b4aafd1d3c41d035407a002e99d5e77883bcf6099b4c`.

The GFX file was already modified in the shared worktree by the parent. The parent instruction says only its portrait comment changed and aliases remain stable. This worker read the current file and did not edit it.

`common/decisions/categories/014_cannibalism_categories.txt` SHA-256: `11b87433cc95344a96b6bfbf9612e751f28912fb9030613e3cc3f583cd56a9c6`.

`common/decisions/014_cannibalism_decisions.txt` SHA-256: `ad356db7875965262a049bcdc858499193ee5c2163dc1c736aa066c063d279d3`.

The decision file was read to identify entry surfaces only. No decision trigger, target, payment, effect, AI rule, or localisation was changed.

## Reference images and native mapping

`network_required_fields_reference.png` uses the retained 860x620 network background and registered 374x64 country/state card artwork.

The left row is at local window position `(22,290)` with size `374x64`; its existing text region begins at `(58,8)` and is bounded by `304x56`.

The right row is at `(435,290)` with size `374x64`; its existing text region begins at `(14,8)` and is bounded by `346x56`.

The reference proposes three compact native text lines inside the existing row: identity/type/strength, known route/last incident, and selected counteraction/uncertainty.

The row's existing full-width selection control remains informational and the selected-target footer remains a read-only evidence card.

The three-line fit is a reference proposal only. It must be checked against the accepted data API's longest real labels and production renders before any source patch.

`warlord_required_fields_reference.png` uses the existing 470x340 warlord background and overlays the registered 278x72 `GFX_cannibalism_controlled_state_card` at `(20,204)`.

The existing Larder, Frenzy, and post-Evolution-II Alignment values remain at their current source positions, while recruitment capacity remains represented by `cannibalism_warlord_capacity` in the existing card at `(34,214)` with a `244x52` text box.

The right side contains the existing animated route emblem, critical-Larder glow, and Frenzy border regions.

The accepted controlled-state identity list and raid-target card have no current data-bound element, and the visible background has no unassigned card-sized region that can hold both while preserving the existing capacity value and animated regions.

The lower decorative frame strip is marked as a constraint because it has no current native state or target rows and its usable bounds have not been approved for names.

The reference therefore requests a parent selection of a bounded reflow or a separately routed background-art change before a source placement is chosen.

`revealed_required_fields_reference.png` uses the existing 470x380 background, current 278x72 loyalty card at `(184,158)`, the registered 278x72 continental-target card as a placement candidate at `(184,232)`, the current animated unification-seal placement at `(356,234)` scaled to 0.75, and the current conditional terminal-progress text region at `(26,315)`.

The candidate target card intersects the seal footprint and ends at the terminal-progress panel boundary.

The present loyalty card shows an aggregate count in one text box rather than a list. The existing `GFX_cannibalism_continental_target_card` is registered but has no current GUI consumer.

These bounds are candidate annotations, not accepted placements. Parent selection must resolve list height, scroll or paging behavior, card count, order, seal clearance, and the terminal-progress relationship.

The source PNGs under `evidence/reference_inputs/` are unmodified copies or mechanical DDS decodes for reference inspection. The three final reference PNGs are annotated source-background maps, not runtime art, MCP production renders, or accepted final layout screenshots.

## Linked assets and current states

Network background and rows use `GFX_cannibalism_network_window_background`, `GFX_cannibalism_network_country_card`, `GFX_cannibalism_network_state_card`, and `GFX_cannibalism_network_target_frame`.

The Network scripted-GUI binding already maps `cannibalism_network_gui_country_entries` and `cannibalism_network_gui_state_entries` to the existing country and state row containers with scoped values, indices, and `change_scope = yes`.

The current row localization keys are `cannibalism.gui.network.country_entry` and `cannibalism.gui.network.state_entry`. They show identity, current type/stage, and strength only.

The current Warlord background and card assets are `GFX_cannibalism_warlord_command_background` and `GFX_cannibalism_controlled_state_card`.

The current Warlord window shows Larder, Frenzy, recruitment capacity, and Network Alignment after Evolution II. The latter makes four simultaneous mechanic values, so the new state and raid entries must remain information records and add no meter.

The current Warlord animated families are the route emblem, critical-Larder glow, and Frenzy border. Their existing scripted visibility conditions remain untouched.

The current revealed assets are `GFX_cannibalism_revealed_command_background`, `GFX_cannibalism_warlord_loyalty_card`, `GFX_cannibalism_continental_target_card`, the reveal-gated portrait sprites, the unification-seal sprites, and ordinary terminal-frame sprites.

The revealed window remains hidden for the Wendigo route. Its portrait and seal are currently always visible within the revealed command state, and its terminal-progress text is gated by `cannibalism_terminal_route_ready`.

No new asset or GFX registration is proposed. If the parent selects a background redesign, that work requires a separate explicit asset handoff and must preserve the accepted Event014 visual identity and existing animations.

## Decision entry surfaces and ownership

The Warlord category's state-target decisions include `cannibalism_consume_controlled_state`, `cannibalism_raise_scavenger_warband`, `cannibalism_raise_feast_cohort`, `cannibalism_raise_origin_specialist`, and `cannibalism_raise_bone_guard` in `common/decisions/014_cannibalism_decisions.txt`.

The revealed category includes the country-target `cannibalism_unified_absorb_warlord` and `cannibalism_unified_issue_continental_command` entries.

These definitions were consulted as entry-surface context only. They do not establish which current target pointer or existing decision selection the new cards should display.

The worker's bounded search found no literal `raid` identifier in the Event014 decision file. The exact decision or owner record that populates the accepted “raid target card” remains for the parent data API handoff to identify.

No GUI control, click effect, payment path, target selection, or gameplay action is added by these references.

## Engine and vanilla references

Offline `Interface modding - Hearts of Iron 4 Wiki.md` was read at lines 83-95 for container bounds, backgrounds, clipping, and relative geometry, and lines 110-128 for scroll-container requirements.

Offline `Scripted GUI modding - Hearts of Iron 4 Wiki.md` was read at lines 44-60 for independent window binding, lines 71-114 for parent context, lines 179-208 for click effects and temporary GUI values, and lines 241-300 for dynamic lists and their native grid-box relationship.

Installed vanilla `common/scripted_guis/_documentation.md` was read at lines 78-90 for array, value, index, `change_scope`, and entry-container fields.

The `army_units` scroll container in installed vanilla `interface/countryarmyview.gui`, lines 388-410, is the exact vanilla grid-box and scroll precedent reviewed for bounded repeated rows.

Installed vanilla `interface/RAJ_famine.gui`, lines 1-44, and `common/scripted_guis/RAJ_famine_scripted_gui.txt`, lines 1-15, were also reviewed for a decision-category window attachment precedent.

The installed vanilla `common/scripted_guis/` search found only `_documentation.md` using the literal `dynamic_lists =` syntax, so no vanilla runtime dynamic-list binding precedent was available. The live Event014 Network lists and vanilla grid-box scrolling remain the closest paired sources for a future accepted list layout.

SHA-256 revisions are recorded here: offline Interface wiki `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, offline Scripted GUI wiki `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`, installed scripted-GUI documentation `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, vanilla `countryarmyview.gui` `9c37dc7f856e792a5a2a56493c2c54de9509e209ee9d5ed117e7fd3eeff5c950`, vanilla RAJ GUI `9f5e2b81792460c7982b202c1feab7805895140052b7d27e1e759882bdc1979`, and vanilla RAJ scripted-GUI source `87814f78c90955fa00a6449521fdca0183a86e46c629e68baeafe90dffe14e2f`.

The connected `hoi4_agent_tools` exposed GUI and reference tool schemas, but no health, version, or task-negotiation route was exposed. This pass did not use helper expansion, jobs, native tasks, or GUI rewrite.
