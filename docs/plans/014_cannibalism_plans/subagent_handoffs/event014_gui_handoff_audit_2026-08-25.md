# Event 014 scripted GUI handoff audit

Audit date: 2026-08-25.

## Result

The five audited windows are dedicated Event 014 Cannibalism presentation surfaces, but the mandatory MCP evidence does not support an attributable source patch in this pass.

No runtime GUI, scripted-GUI, GFX, localisation, gameplay, decision, AI, balance, shared interface, or asset file was changed.

The MCP inspection route resolved every exact window and produced one linked inspection artifact per window. Its validation diagnostics were globally truncated, and the retained inline diagnostics did not name an Event 014 overlap, click-region, or text-overflow element. The network inspection reported one dropped `GUI_CLICK_BOUNDS_MISMATCH`, but the response did not retain its element or source path. Attempting to reopen that linked artifact through the MCP resource route failed with `Artifact provenance manifest is unavailable`. That unattributed diagnostic is therefore a blocker, not grounds for changing Event 014 source.

The MCP renderer accepted the requested states, resolutions, and comparisons, but exposed only one full-window SVG per request. For each window, the state, four-resolution, and comparison requests returned the same artifact SHA-256. Distinct cropped, annotated, hierarchy, click-region, per-state, per-resolution, and comparison images are not proven.

## Event ownership proof

Event ID and slug: `014_cannibalism`.

The accepted design source is `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md`. It defines the early attached header, organized-network window, Cannibal command window, revealed command window, and Wendigo transformation window as Event 014 mechanic surfaces.

The exact implementation is confined to:

- `common/scripted_guis/014_cannibalism_scripted_gui.txt`
- `interface/014_cannibalism_frontline_hunger.gui`
- `interface/014_cannibalism.gfx`
- `localisation/english/014_cannibalism_l_english.yml`

Decision-category entry points are Event 014-owned entries in `common/decisions/categories/014_cannibalism_categories.txt`:

- `cannibalism_containment_category` and `cannibalism_network_alerts_category` attach `cannibalism_early_header_scripted_gui`.
- `cannibalism_warlord_command_category` attaches `cannibalism_warlord_command_scripted_gui`.
- `cannibalism_unified_command_category` attaches `cannibalism_revealed_command_scripted_gui`.
- `cannibalism_wendigo_command_category` attaches `cannibalism_wendigo_command_scripted_gui`.

The early header opens the separate player-context network window through `cannibalism_network_open`, `cannibalism_network_open_click`, and `cannibalism_gui_open_network_view`. The network block uses `parent_window_token = top_bar`, a dirty token, and Event 014 country/state arrays.

No shared event log, Event Details, settings, super-event, shared registry, generic debug window, or unrelated GUI was inspected or edited as an owned surface.

## Exact identifiers

| Window | Scripted GUI | Context and entry |
| --- | --- | --- |
| `cannibalism_early_header_window` | `cannibalism_early_header_scripted_gui` | `decision_category`; containment and network-alert categories |
| `cannibalism_network_window` | `cannibalism_network_scripted_gui` | `player_context`; `top_bar`; opened by `cannibalism_network_open` |
| `cannibalism_warlord_command_window` | `cannibalism_warlord_command_scripted_gui` | `decision_category`; warlord command category |
| `cannibalism_revealed_command_window` | `cannibalism_revealed_command_scripted_gui` | `decision_category`; unified command category |
| `cannibalism_wendigo_command_window` | `cannibalism_wendigo_command_scripted_gui` | `decision_category`; Wendigo command category |

Network interaction identifiers:

- Buttons: `cannibalism_network_open`, `cannibalism_network_close`, `cannibalism_network_refresh`, `cannibalism_network_sort`, five `cannibalism_network_tab_*` controls, `cannibalism_network_country_entry_select`, and `cannibalism_network_state_entry_select`.
- Dynamic lists and entries: `cannibalism_network_country_dynamic_list`, `cannibalism_network_state_dynamic_list`, `cannibalism_network_country_entry`, and `cannibalism_network_state_entry`.
- Selection effects: `cannibalism_gui_select_country_entry` and `cannibalism_gui_select_state_entry`.
- View lifecycle effects: `cannibalism_gui_open_network_view`, `cannibalism_gui_close_network_view`, `cannibalism_gui_rebuild_network_view`, and `cannibalism_gui_toggle_network_sort`.

Principal background and card sprites:

- `GFX_cannibalism_early_category_background`
- `GFX_cannibalism_network_window_background`
- `GFX_cannibalism_network_country_card`
- `GFX_cannibalism_network_state_card`
- `GFX_cannibalism_network_target_frame`
- `GFX_cannibalism_warlord_command_background`
- `GFX_cannibalism_revealed_command_background`
- `GFX_cannibalism_wendigo_command_background`

State and animation sprite families include the Field Hunger, Command Integrity, Cult Cohesion, Larder, Frenzy, Network Alignment, global Larder, global Network Reach, countdown, capacity, portrait, warning-seal, network-thread, island-alert, selected-target, route-emblem, terminal-frame, unification-seal, and Wendigo anchor-pulse identifiers registered in `interface/014_cannibalism.gfx`.

The Event 014 GUI localisation family is `cannibalism.gui.*`, including the early, network, warlord, revealed, and Wendigo keys around lines 1843 through 1943 of the owning localisation file.

## Sources and precedents inspected

Repository guidance:

- `AGENTS.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`

Accepted Event 014 design and prior evidence:

- Part 6 decisions, missions, and GUI spec
- Part 10 assets, animation, and localisation spec
- Part 12 acceptance criteria
- Event 014 package manifest
- `event014_gui_final_audit_v4.md`
- `event014_gui_parser_final_2026-08-25.md`
- `event014_network_gui_repair_evidence_2026-08-24.md`

Offline wiki pages consulted include the required core pages plus `Interface modding` and `Scripted GUI modding`.

Installed vanilla references:

- `common/scripted_guis/_documentation.md` for `decision_category`, `player_context`, parent tokens, effects, triggers, properties, dynamic lists, dirty refresh, and AI behavior.
- `common/scripted_guis/RAJ_famine_scripted_gui.txt` and `interface/RAJ_famine.gui` as an exact compact decision-category scripted-GUI precedent.
- `interface/countryarmyview.gui` and the prior Event 014 parser handoffs were reviewed for transparent full-row button behavior.

## Layout hierarchy

```text
cannibalism_early_header_window (470x304)
|-- full-canvas background and title
|-- Field Hunger, Command Integrity, and conditional Cult Cohesion meters
|-- primary-state card
|-- warning and cohesion animated/static presentation pairs
|-- active-mission summary
`-- Network Ledger view-control button

cannibalism_network_window (860x620, movable)
|-- full-canvas background, title, summary, and close control
|-- five filter tabs, sort, and refresh
|-- network-thread and island-alert presentation
|-- country list well (394x222)
|   `-- 374x64 country entries and full-row selectors
|-- state list well (394x222)
|   `-- 374x64 state entries and full-row selectors
`-- 374x64 selected-target evidence card

cannibalism_warlord_command_window (470x340)
|-- full-canvas background and title
|-- Larder, Frenzy, and conditional Network Alignment meters
|-- controlled-state/capacity card
`-- route, critical-Larder, and Frenzy animated/static presentation pairs

cannibalism_revealed_command_window (470x380)
|-- full-canvas background and title
|-- portrait bay and frame
|-- global Larder and global Network Reach meters
|-- warlord-loyalty card
|-- unification seal
`-- conditional terminal frame and progress text

cannibalism_wendigo_command_window (470x400)
|-- full-canvas background and title
|-- transformed portrait bay and frame
|-- anchor card, countdown, and Pack-capacity field
|-- anchor pulse
`-- conditional terminal frame and lock text
```

## Background coverage map

The source PNG canvases exactly match their window dimensions: 470x304, 860x620, 470x340, 470x380, and 470x400. Network country, state, and target cards are each exactly 374x64.

| Background region | Intended content | GUI use | Status |
| --- | --- | --- | --- |
| Early title and left meter stack | Crisis identity and three-stage pressure hierarchy | title, three meters, primary-state card | Mapped |
| Early right presentation column | warning, ritual state, current objective, network entry | warning seal, cohesion emblem, mission text, ledger button | Mapped |
| Network header and control band | identity, totals, filters, refresh, close | title, summary, five tabs, sort, refresh, close | Mapped |
| Network central art band | changing network activity and island alert | thread and alert sprites | Mapped |
| Network twin list wells | country actors and state nodes | clipped dynamic lists and 374x64 cards | Mapped |
| Network lower evidence frame | selected actor or node | target frame, overlay, flag, text | Mapped |
| Warlord left command field | three pressures and capacity | meters and controlled-state card | Mapped |
| Warlord right identity field | route and critical-state signals | route emblem, Larder glow, Frenzy border | Mapped |
| Revealed portrait bay | Hannibal identity | animated/static portrait and frame | Mapped |
| Revealed command field | Larder, Reach, loyalty, terminal state | two meters, loyalty card, seal, terminal frame | Mapped |
| Wendigo portrait bay | transformed identity | animated/static portrait and frame | Mapped |
| Wendigo command field | anchors, countdown, capacity, terminal state | anchor card, countdown field, capacity field, pulse, terminal frame | Mapped |

## Value, action, cost, and text-density audits

| Surface | Visible value budget | Gameplay-changing GUI actions | View controls | Audit result |
| --- | --- | ---: | ---: | --- |
| Early | Field Hunger, Command Integrity, Cult Cohesion; state and mission are contextual summaries | 0 | 1 | Three mechanic values; within budget |
| Network | actor count, node count, Network Reach; per-row stage/strength and selected target are list context | 0 | five tabs, sort, refresh, close, row selectors | No gameplay action; accepted data-ledger design, but crowded-state visual proof is unresolved |
| Warlord | Larder, Frenzy, Alignment, formation capacity | 0 | 0 | Four mechanic values; at hard ceiling |
| Revealed | global Larder, global Reach, integrated warlords, conditional terminal progress | 0 | 0 | Four mechanic values; at hard ceiling |
| Wendigo | anchor state, transformation countdown, Pack capacity, conditional terminal state | 0 | 0 | Four conceptual values; at hard ceiling |

Spendable-cost count is zero for every audited GUI control. All gameplay costs and outcomes remain in Event 014 decisions, so GUI cost texticon coverage is not applicable.

All button-shaped elements in the source have matching scripted effects and enablement triggers where applicable. The network row selectors are transparent full-card selectors over 374x64 cards, but the MCP's single dropped click-bounds diagnostic could not be attributed to them or cleared.

Main titles are one line. The network summary is two short lines. Card text is one or two lines. Tooltips are generally one or two concise sentences and place cause or use next to the related value. The MCP reported dropped text-overflow diagnostics without retained Event 014 paths, so long-text and localisation-expansion safety remain visually unresolved.

## MCP inspection evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

| Window | Elements | Inspect artifact |
| --- | ---: | --- |
| Early | 17 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30e6c35e08d309b5a89e66c09479fcd00edee5ec5653b573c47b0ec55de1d230/8d672ac06397f4405f6ef383b04b4e73f8894c27b73114d10b1a59e532c45170/gui-inspect.1cbc143519aa5b63.json` |
| Network | 27 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba4c7ebdebe950b390fe34cebb619a25f4c563e742dff4934df8ac28a6637ceb/7f773a7d6200398978495f683cf49b86bab951c3e3b810f1b0ab2b0af9cef31c/gui-inspect.e6d953a7df8542a6.json` |
| Warlord | 17 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7739bb03597208d0286fa340d1b80e8ad329037ebc7b4d61568c36e21e7fd450/c8525b48716706f592abd8ee0d2c96effb4cfd5676551ae2b457cc2e0037807e/gui-inspect.531fb1d00d68c8e2.json` |
| Revealed | 17 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16e2cd9e1a955a9e75571b8aecf591e1376f2a7622dd5477119191b058798890/6320c2d0cbd1dbfca73e0fcc633c729b30860bff9e75cc3097427a34d20a6736/gui-inspect.4869d68c649d039f.json` |
| Wendigo | 17 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1562e62da5f603e051ae9071071c95a7bd4cd6158d19a42d0e988d0901466d01/60ea9a6edf33665c2532c2b93ab9bfa9e7d56120d5c7b0fbe528aee6f170b5b7/gui-inspect.51244b118a282fd3.json` |

Every inspect returned `GUI_INSPECTED` and `status = ok`. Every inspect also returned `GUI_GRAPH_DIAGNOSTICS_TRUNCATED` and `GUI_VALIDATION_DIAGNOSTICS_TRUNCATED` against the repository-wide graph. Retained inline collisions point to Event 003 and Event 005 assets and are outside this worker's scope.

The per-window validation summaries reported visible-overlap totals of 21 early, 11 network, 22 warlord, 25 revealed, and 25 Wendigo. The detailed paths were dropped. The layouts intentionally co-locate animated and static fallback pairs, so overlap counts cannot be treated as defects without element-level attribution.

## MCP render, state, resolution, hierarchy, click-region, and comparison evidence

Requested state set at 1920x1080 for every window:

- normal
- hover
- selected
- active
- disabled
- warning
- completed
- empty list
- crowded/full list
- minimum value
- maximum value
- long text
- missing localisation

Requested normal-state resolutions for every window:

- 1366x768
- 1600x900
- 1920x1080
- 2560x1440

Requested comparisons:

- Early: normal versus warning
- Network: normal versus full list
- Warlord: normal versus warning
- Revealed: normal versus completed
- Wendigo: normal versus warning

| Window | Full render SHA-256 | State artifact | Resolution artifact | Comparison artifact |
| --- | --- | --- | --- | --- |
| Early | `fcfae968916de2c03f1a02f42bf5dc720fcc83c255414d77af125652efc1ea15` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fcfae968916de2c03f1a02f42bf5dc720fcc83c255414d77af125652efc1ea15/ced316f198e0c5042d85ce074ab446bfc38265c18a0eaa8439f4c260f8b9ee5b/cannibalism_early_header_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fcfae968916de2c03f1a02f42bf5dc720fcc83c255414d77af125652efc1ea15/6e3e76d752a7d3c2bfbff799a660978eab2fc512133122d8077223e454811578/cannibalism_early_header_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fcfae968916de2c03f1a02f42bf5dc720fcc83c255414d77af125652efc1ea15/63cbcf0c8a2cc66e6e53f9220ad99dbfc60b2a984e01fb9515a9b2303f647a2a/cannibalism_early_header_window-full.svg` |
| Network | `40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/7b99509de070614dcc051c84215e2e5a0a4622b635c0927211a60e4a4232a649/cannibalism_network_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/cd32e3cfb94214e76e2fb6f4adebaa1d2a4a295a5da1472236ea2de732a625c4/cannibalism_network_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/b9a9541b25ae7b3d91badf7e85592c2c67bf9785698daf9095ff93eb8e161fe4/cannibalism_network_window-full.svg` |
| Warlord | `356eda9a5565ef7475fbeca05d9002dcef5a8fbdc5f659787da7ef3a485f6ca7` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/356eda9a5565ef7475fbeca05d9002dcef5a8fbdc5f659787da7ef3a485f6ca7/9ba64f6e7466b54fdc79e8b8afe3e053bbbaae856e0390184370712a025ef040/cannibalism_warlord_command_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/356eda9a5565ef7475fbeca05d9002dcef5a8fbdc5f659787da7ef3a485f6ca7/8c4f1f8454ca3af810274ba22e30c818a019f9630736b6c5b9a6720052ca4b42/cannibalism_warlord_command_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/356eda9a5565ef7475fbeca05d9002dcef5a8fbdc5f659787da7ef3a485f6ca7/1bcbd85b06f75e81ac5ca4477dc475b6567133072ab19ff1a52f02d3586c5afd/cannibalism_warlord_command_window-full.svg` |
| Revealed | `7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9/6d227abe33d210fbc2de8669370fa37fb7c8b8998d5f3359f322a8cbe931c27f/cannibalism_revealed_command_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9/da5f96b15616ff2948951e7a327f2652ad5117143281ed1c3aa3ee6ea3945a18/cannibalism_revealed_command_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9/b1b8b7ca005e952dd0056eacded859b37c3f819fc56377f1f13a6ab529fbae69/cannibalism_revealed_command_window-full.svg` |
| Wendigo | `5dca062f0ceea5b6be78543b2af1390a739f0896c5517587b74aaa42190738c7` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5dca062f0ceea5b6be78543b2af1390a739f0896c5517587b74aaa42190738c7/1725dfcc37e16a232c2aa27b8f99c616482ee86d674e817145795c3b90a95923/cannibalism_wendigo_command_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5dca062f0ceea5b6be78543b2af1390a739f0896c5517587b74aaa42190738c7/2727b5fd9dd2ec1a1336e9f826988b005b85fe33f5a91bea2d3aeb8074b8d49b/cannibalism_wendigo_command_window-full.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5dca062f0ceea5b6be78543b2af1390a739f0896c5517587b74aaa42190738c7/307f981c507d21e17b50e98dcb99d52c3a73f0e80f98f43b09bccd6b42ed3015/cannibalism_wendigo_command_window-full.svg` |

Every render returned `GUI_RENDERED`, `status = ok`, and `MCP_RESPONSE_TRUNCATED`. The identical full-render hash across each window's state, resolution, and comparison groups proves that no distinct variant image was exposed. The route did not return separate crop, annotation, hierarchy, or click-region artifacts.

## Before, after, and rewrite disposition

No source change was justified, so there is no behavioral or visual before/after delta.

`hoi4.gui_rewrite` was not called. The retained MCP output did not identify an exact Event 014 defect to rewrite, and global or dropped diagnostics are not sufficient authority for a speculative patch.

The current worktree already contained unrelated concurrent changes to the network tab, sort, and refresh positions in `interface/014_cannibalism_frontline_hunger.gui`. This worker preserved those changes and did not stage, revert, or amend them.

## Missing assets and routed handoffs

No missing Event 014 asset was proven in this bounded audit.

All five background PNGs and DDS registrations exist. The inspected source PNG dimensions exactly match their window canvases, and the three network card PNGs exactly match their 374x64 consumers.

No new art, asset correction, animation request, or asset-subagent route was opened.

## Remaining blockers and parent-owned validation

- The GUI inspect graph is globally truncated, with unrelated Event 003 and Event 005 symbol collisions dominating retained diagnostics.
- The network inspect reports one dropped `GUI_CLICK_BOUNDS_MISMATCH` without an element or path. The linked artifact cannot currently be reopened because the MCP resource route reports `Artifact provenance manifest is unavailable`.
- Visible-overlap and text-overflow totals are not attributable to exact Event 014 elements because their detailed diagnostics were dropped.
- The renderer collapsed all requested states, resolutions, and comparisons into one full-window SVG per window.
- Distinct annotated, cropped, hierarchy, click-region, hover, selected, active, disabled, warning, completed, empty, crowded, minimum, maximum, long-text, missing-localisation, and per-resolution views remain unresolved.
- Live consumer and in-game validation remain parent-owned.

The audit is complete as a bounded evidence pass. Visual completion of the five windows remains blocked by missing distinct MCP state, resolution, hierarchy, click-region, and comparison artifacts.

## Simplifications and omissions

No source simplification, fallback UI, placeholder, guessed click region, or gameplay substitution was introduced.

The only omission is evidence imposed by the MCP route: it did not expose the requested distinct visual variants, so this handoff does not claim visual completion.
