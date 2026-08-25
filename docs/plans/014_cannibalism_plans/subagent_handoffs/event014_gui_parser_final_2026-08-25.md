# Event 014 Cannibalism GUI Parser Final Handoff

## Scope and ownership proof

Event ID and slug: `014_cannibalism`.

The accepted Event 014 specification in `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md` defines the early frontline header, organized network, cannibal command, revealed command, and Wendigo transformation presentation surfaces.

`docs/plans/014_cannibalism_plans/014_gui_dimension_ledger.md` freezes those five Event 014 window dimensions and identifies `interface/014_cannibalism_frontline_hunger.gui` as their implementation-owned layout file.

`common/scripted_guis/014_cannibalism_scripted_gui.txt` binds the five windows only through `cannibalism_early_header_scripted_gui`, `cannibalism_network_scripted_gui`, `cannibalism_warlord_command_scripted_gui`, `cannibalism_revealed_command_scripted_gui`, and `cannibalism_wendigo_command_scripted_gui`.

The decision entry points are `cannibalism_containment_category` and `cannibalism_network_alerts_category` for the early header, `cannibalism_warlord_command_category` for Warlord command, `cannibalism_unified_command_category` for revealed command, and `cannibalism_wendigo_command_category` for Wendigo command.

The separate network window is opened by `cannibalism_network_open` and is attached through `context_type = player_context`, `parent_window_token = top_bar`, and `window_name = "cannibalism_network_window"`.

No shared event log, event-details, settings, super-event, registry, or unrelated GUI file was changed.

## Identifiers and linked files

| Surface | Window | Scripted GUI | Context or entry | Main background sprite |
| --- | --- | --- | --- | --- |
| Early header | `cannibalism_early_header_window` | `cannibalism_early_header_scripted_gui` | decision categories | `GFX_cannibalism_early_category_background` |
| Network | `cannibalism_network_window` | `cannibalism_network_scripted_gui` | `cannibalism_network_open`, `top_bar` | `GFX_cannibalism_network_window_background` |
| Warlord command | `cannibalism_warlord_command_window` | `cannibalism_warlord_command_scripted_gui` | `cannibalism_warlord_command_category` | `GFX_cannibalism_warlord_command_background` |
| Revealed command | `cannibalism_revealed_command_window` | `cannibalism_revealed_command_scripted_gui` | `cannibalism_unified_command_category` | `GFX_cannibalism_revealed_command_background` |
| Wendigo command | `cannibalism_wendigo_command_window` | `cannibalism_wendigo_command_scripted_gui` | `cannibalism_wendigo_command_category` | `GFX_cannibalism_wendigo_command_background` |

The network list identifiers are `cannibalism_network_country_dynamic_list`, `cannibalism_network_state_dynamic_list`, `cannibalism_network_country_entry`, `cannibalism_network_state_entry`, `cannibalism_network_country_entry_select`, and `cannibalism_network_state_entry_select`.

The row sprites are `GFX_cannibalism_network_country_card` and `GFX_cannibalism_network_state_card`, both frozen at 374 by 64 pixels.

The relevant localisation keys include `cannibalism.gui.early.title`, `cannibalism.gui.network.title`, `cannibalism.gui.warlord.title`, `cannibalism.gui.revealed.title`, `cannibalism.gui.wendigo.title`, and `cannibalism.gui.network.entry.select.tt`.

## Files changed

- `interface/014_cannibalism_frontline_hunger.gui`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_gui_parser_final_2026-08-25.md`

The source change is exactly two token-pair corrections.

`cannibalism_network_country_entry_select` changed from `size = { x = @CANNIBALISM_NETWORK_ENTRY_WIDTH y = @CANNIBALISM_NETWORK_ENTRY_HEIGHT }` to `size = { width = @CANNIBALISM_NETWORK_ENTRY_WIDTH height = @CANNIBALISM_NETWORK_ENTRY_HEIGHT }`.

`cannibalism_network_state_entry_select` received the identical correction.

The resulting click bounds remain exactly 374 by 64 pixels and continue to match the row containers, grid slots, and card sprites.

Three pre-existing concurrent network control position changes remain in the worktree and were deliberately excluded from this worker's staged patch and commit.

## References inspected

The required offline wiki pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding.

The complete `chaos-redux-decisions-missions` and `chaos-redux-events` skills were read.

The installed vanilla scripted-GUI documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md` was read.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/airwingreorganization.gui` was inspected as the exact vanilla list, grid, slot-size, container-size, and button-layout precedent.

The accepted Event 014 specification, acceptance criteria, GUI dimension ledger, prior GUI audit evidence, exact Event 014 GUI source, scripted-GUI binding, GFX registrations, category attachments, and linked localisation were inspected.

## Pre-change MCP evidence

All five exact windows returned `GUI_INSPECTED` with `status = ok` before the source edit.

| Window | Inspect artifact |
| --- | --- |
| Early header | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2654f5cefe6eb3ef0d73735dbb526b278271d40c6e5fac68550932a78aa82611/743b9249249224d2da8e1fc54dc5cd2315ae980641a8d4eeccd7393721340915/gui-inspect.c1461b310b7d2522.json` |
| Network | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11c147025f931d7b90cde3b1372f2d94215284c2143bbbc29111a1f76d709baa/b38914a5e2d69ce0448691ba25d925a6155c12278e787e0291d423bc38a126f3/gui-inspect.a3317582ad124ba7.json` |
| Warlord | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f9789d2768cb43b7598ed56a7fdee597cba9b57f1b906e80ba22c509df62ceb/107952d2731c1f71953ba4fadd446d89bfdf21d6b96f339e2d2d2aec3c951a63/gui-inspect.7ad7f974db9e693a.json` |
| Revealed | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05c338d8cb34fd538f4617c15e604d78c6f40190eb3dc843ca96d4e3f2a58815/571eba3dc5871b535192af7095999f10f52a600a29f352bd460d901c6e4fbbd7/gui-inspect.384180d305be4469.json` |
| Wendigo | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ffb47feace8da6119fe21b0972c751efe585475535dfea8638a44dd1a6e3c5e5/7ac5f665f8c911b23eb319caad9ad112985f8198a683053b450be9e7a7be333d/gui-inspect.5c0b04330d383924.json` |

The pre-change render request asked for normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states at 1280 by 720, 1920 by 1080, 2560 by 1440, and 3840 by 2160.

The route emitted one full-window SVG per successful request and returned `MCP_RESPONSE_TRUNCATED`, so the linked artifact does not prove that every requested state and resolution was emitted as a distinct view.

| Window | Pre-change render artifact |
| --- | --- |
| Early header | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fcfae968916de2c03f1a02f42bf5dc720fcc83c255414d77af125652efc1ea15/a0c75620a0a06cb8ffce543bf733f91b83c4e062a4b2f7e7ebaf5c0d8a547f72/cannibalism_early_header_window-full.svg` |
| Network state batch | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/658d6c530db34be74d2a872fad8610483a7038e9670acc3ba9e7794457cab19d/cannibalism_network_window-full.svg` |
| Network resolution batch | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/d652e1a36e31416b59e5cd27100edd80f39b98a0eae9e414c053ae9000f1365b/cannibalism_network_window-full.svg` |
| Warlord | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/356eda9a5565ef7475fbeca05d9002dcef5a8fbdc5f659787da7ef3a485f6ca7/043acb55ae9da41d47458a7ceeaf8d4b566609351960d397eda1bbd5e2362abf/cannibalism_warlord_command_window-full.svg` |
| Revealed | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9/b6b24e036058b7dd74df56a382a3628c41ebdcf748bb3ec34cf1f443c25d7fb8/cannibalism_revealed_command_window-full.svg` |
| Wendigo | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5dca062f0ceea5b6be78543b2af1390a739f0896c5517587b74aaa42190738c7/cd8b1492ff0465e1471b9bb8c43f776c3b3a7d2aa5e9e6883124a9a9e086f2df/cannibalism_wendigo_command_window-full.svg` |

The first broad network render returned `RENDER_AGGREGATE_BLOCKED` because its comparison diff plane would exceed the fixed aggregate limit of 67,108,864 pixels.

Splitting the network state and resolution requests produced the two successful artifacts listed above.

## Rewrite review

`hoi4.gui_rewrite` reviewed the complete proposed source for `interface/014_cannibalism_frontline_hunger.gui`, exact selector `cannibalism_network_window`, and scenario `event014_parser_final_network_size_rewrite_review_20260825`.

The proposed layout preserved the 374 by 64 geometry and generated before, proposed, visual-diff, fidelity, validation, and source-diff artifacts.

| Artifact | URI |
| --- | --- |
| Before PNG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10c10d254061df247f0b9ec9fb00a1efdc1678b401514c18b38d5b7717bfc4fc/7465a9fb6c6efb26e0a251e49ea0a916cd311bc29489c25ff47e2e87f24e6bc8/cannibalism_network_window-before.png` |
| Proposed PNG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10c10d254061df247f0b9ec9fb00a1efdc1678b401514c18b38d5b7717bfc4fc/8cd5af403b387f299b3a014c41d3d3321cb65486a98e3f76f03a4b60cf0c0b92/cannibalism_network_window-proposed.png` |
| Visual diff PNG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/600d8224ddfff7a812166f600e16c809a5fe89e36ca3eff06f68b469698f2a86/509f45fdfc06ac8c388ec6324661299048a3a430d2ab8b9b96057ce67c4b91db/cannibalism_network_window-visual-diff.png` |
| Visual diff JSON | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/5ecb221fb5fddc2a1e58f61695125562ee2afa2b092e32aefac95d7680fe6e75/cannibalism_network_window-visual-diff.json` |
| Proposed fidelity | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28bbff69eca512f3eda620a829a70848a887800fc103fe2fa84854a6883ee9a2/254d5ac8eeb329a76a9d595e7c4e102d83d09951e5ded1f5750182bf18d0f42d/cannibalism_network_window-proposed-fidelity.json` |
| Rewrite validation | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25cacf89dc9854a0678bdd137760c4c03fa5078ff62e9f3e7f4befed39a58e82/0f4b33d0cfce3ac7492ecd034e080132af5da8f60f91c022d4c7330ea0277da9/cannibalism_network_window-rewrite-validation.json` |
| Source diff | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/baddfa57ae5b31df487abd71c94e1f0a8581d0ba5c9ba61da017e619efbd7145/14dc2cf4030e50252eb347fb30a0f625e4ffc7f66d6860996d0ba97689b9db23/014_cannibalism_frontline_hunger.gui.diff` |

The rewrite route returned `GUI_CHANGES_BLOCKED` and made no source write because repository-wide GUI graph diagnostics were truncated and unrelated Event 003 and Event 005 sprite collisions remained active.

The reviewed two-line correction was therefore applied through the normal patch workflow.

## Layout hierarchy and background coverage

| Background region | Intended content | GUI elements | Interaction or state | Status |
| --- | --- | --- | --- | --- |
| Early left meter column | Field Hunger, command integrity, Cult Cohesion, primary-state context | three meter sprites, three value labels, one state card | read-only live state | unchanged |
| Early right column | warning emblem, cult emblem, mission summary, network entry | icons, summary, `cannibalism_network_open` | one view-opening control | unchanged |
| Network header | title, summary, close | title and summary text, close control | movable-window control | unchanged |
| Network tab strip | five filters, sort, refresh | seven view controls | filter and rebuild only | unchanged |
| Network center | thread field and two list panels | country and state dynamic grids | hover and row selection | corrected 374 by 64 row hitboxes |
| Network footer | selected target | target frame, flag, summary | selected-state feedback | unchanged |
| Warlord left column | Larder, Frenzy, Network Alignment, capacity | three meters and one card | read-only live state | unchanged |
| Warlord right column | route, critical state, frenzy state | event-owned icons and frames | state feedback | unchanged |
| Revealed portrait bay | revealed portrait and frame | portrait sprites and frame | reveal-gated state | unchanged |
| Revealed command field | global Larder, global Network Reach, loyalty, terminal progress | two meters, loyalty card, terminal frame | read-only live state | unchanged |
| Wendigo portrait bay | transformed portrait and frame | portrait sprites and frame | route-gated state | unchanged |
| Wendigo command field | anchors, countdown, capacity, terminal progress | anchor card, two meters, terminal frame | read-only live state | unchanged |

## Value, action, cost, and text-density audits

| Surface | Visible mechanic-value budget | Gameplay-changing GUI actions | View controls | Result |
| --- | --- | ---: | ---: | --- |
| Early | three meters plus one context card | 0 | 1 | within the four-value ceiling |
| Network | node cards and one selected-target summary | 0 | five tabs, sort, refresh, close, row selectors | no decision costs or outcomes live in this window |
| Warlord | three meters plus one capacity card | 0 | 0 | within the four-value ceiling |
| Revealed | two meters, one loyalty card, one terminal state | 0 | 0 | at the four-value ceiling |
| Wendigo | anchors, countdown, capacity, terminal state | 0 | 0 | at the four-value ceiling |

The GUI source contains no spendable gameplay action, so the spendable-cost count is zero and texticon coverage is not applicable to this layout patch.

The network row hitboxes now match the visible 374 by 64 cards and their 374 by 64 grid slots exactly.

Text boxes use fixed widths and heights inside their intended painted regions.

The source change does not alter text bounds, fonts, labels, localisation, wrapping, hover wording, or missing-localisation behavior.

The MCP route returned full-window artifacts but did not expose distinct annotated, hierarchy, click-region, crop, state, long-text, and missing-localisation images as separate linked files, so visual claims for those requested variants remain unresolved.

## State and resolution matrix

| Evidence group | Requested | Emitted | Limitation |
| --- | --- | --- | --- |
| Pre inspect | all five exact windows | five inspect JSON artifacts | repository-wide graph and validation diagnostics truncated |
| Pre render | fourteen states and four resolutions per window | one full SVG per successful request | response collapsed or omitted distinct variants |
| Pre network broad render | fourteen states and four resolutions | none | aggregate render cap exceeded |
| Pre network split renders | fourteen states at 1920 by 1080, plus normal at four resolutions | two full SVG artifacts | distinct variants not separately exposed |
| Post inspect aggregate | all five exact windows | none | batch remained active without output and was terminated after an extended bounded wait |
| Post network inspect | exact changed network window | one inspect JSON artifact | global diagnostics still truncated |
| Post render aggregate | network state and resolution batches plus normal comparison for four unchanged windows | none | batch remained active without output and was terminated after an extended bounded wait |
| Post network render | normal at 1920 by 1080 | one full SVG artifact | response truncated, no separate annotated or click-region artifact exposed |

## Post-change evidence

The bounded post-change inspect of the changed surface returned `GUI_INSPECTED` with `status = ok`.

Post network inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f4492da13165aa5f1e984069ad409d5f30fd95abfddb24192e37fbaa47e2881/1038db276a55db89e99e070301d54eea78117b8bcf4a49568064f6033596ed28/gui-inspect.f736164a907df8c5.json`.

The bounded post-change network render returned `GUI_RENDERED` with `status = ok`.

Post network render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/e0d601666300447b2bed0d897ba18120417a134c573c0b5b6f5ab182ac1ead8e/cannibalism_network_window-full.svg`.

The before and proposed rewrite PNGs have identical dimensions and the correction intentionally produces no visual movement.

The behavioral change is parser and hitbox integrity: the two transparent row selectors now declare valid width and height fields that agree with the 374 by 64 cards, entry containers, and grid slots.

## Blockers and unresolved states

- Repository-wide `GUI_GRAPH_DIAGNOSTICS_TRUNCATED` and `GUI_VALIDATION_DIAGNOSTICS_TRUNCATED` prevent a clean global GUI validation claim.
- Unrelated active sprite collisions in Event 003 and Event 005 blocked `hoi4.gui_rewrite` from writing the reviewed proposal.
- The broad network render exceeded the fixed 67,108,864-pixel aggregate budget and required split requests.
- Render responses exposed one full SVG per successful request and returned `MCP_RESPONSE_TRUNCATED`, so distinct hover, selected, active, completed, disabled, warning, empty, crowded, long-text, missing-localisation, hierarchy, click-region, annotated, crop, and per-resolution artifacts are not proven.
- The post-change five-window inspect batch and the bounded multi-window render/comparison batch remained active without output and were terminated after extended waits.
- Only the changed network surface has successful bounded post-change inspect and render artifacts.
- No final in-game or live-consumer completion claim is made.

## Parent-owned follow-up

The parent retains runtime and live-consumer validation.

If the GUI MCP later exposes isolated state, hierarchy, click-region, annotated, crop, and per-resolution artifacts without stalling or collapsing them, the five-window post-change visual matrix should be completed against this commit.

No gameplay, localisation, asset, AI, decision, cost, balance, or shared-UI change was made.

No simplification was made to the requested source correction.

Visual completion remains explicitly unresolved only where the renderer did not return the requested distinct evidence.
