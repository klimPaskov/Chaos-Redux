# Event 014 direct GUI MCP reaudit

Audit date: 2026-08-24.

## Scope and result

This pass covered only the five direct scripted GUI windows owned by Event 014 Cannibalism.

The windows are `cannibalism_early_header_window`, `cannibalism_network_window`, `cannibalism_warlord_command_window`, `cannibalism_revealed_command_window`, and `cannibalism_wendigo_command_window`.

Their Event 014 bindings are `cannibalism_early_header_scripted_gui`, `cannibalism_network_scripted_gui`, `cannibalism_warlord_command_scripted_gui`, `cannibalism_revealed_command_scripted_gui`, and `cannibalism_wendigo_command_scripted_gui`.

The network window uses player context with the top bar parent.

The other four windows use decision-category context.

No shared event log, Event Details, settings, super-event, registry, unrelated GUI, gameplay cost, or gameplay effect surface was inspected or changed.

No narrow Event 014 source defect was proven by attributable MCP evidence.

No source rewrite was applied and no commit was created.

## Required references

`AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-events/SKILL.md` were reread for this resumed pass.

The offline Interface Modding and Scripted GUI Modding pages were reread.

Installed vanilla scripted-GUI documentation and script-concept documentation were reread.

The existing Event 014 layout follows the installed vanilla container, button, decision-category context, and player-context patterns.

## Current layout inventory

| Window | Size | Main visible values | Controls | Entry or context |
| --- | ---: | --- | --- | --- |
| Early header | 470x304 | Field hunger, command integrity, cult cohesion, primary theater, active mission | Network open | Decision category |
| Network | 860x620 | Current network summary and selected target | Close, five filters, sort, refresh, country and state target selection | Player context, top bar |
| Warlord command | 470x340 | Larder, frenzy, alignment, controlled-state capacity | Informational surface | Decision category |
| Revealed command | 470x380 | Global larder, global network, loyalty, terminal progress | Informational surface | Decision category |
| Wendigo command | 470x400 | Anchors, countdown, capacity, terminal progress | Informational surface | Decision category |

The early header reaches the four-visible-mechanic-value hard ceiling before its mission summary.

The network surface has no spendable controls and its country and state selector hitboxes use the verified full-row 374x64 `x`,`y` vector form.

The three command windows have no direct gameplay-changing buttons, so the cost and texticon budget is not engaged on these direct GUI surfaces.

The frame-sequence sprites are selected by scripted visibility and are active without a player-facing control.

Static sibling sprites remain wired as technical fallbacks.

## Fresh inspect evidence

All five fresh `hoi4.gui_inspect` calls completed with `GUI_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

| Window | Inspected elements | Artifact |
| --- | ---: | --- |
| Early header | 17 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cee45f33bc8737dab16bd1f37d9f0e1d8ca65842ad8fe206a0b5b48351fa5ad5/c2cf802f3b650562f4cab342bc996033b46e9ea6e23584e23777591dd7e56265/gui-inspect.9b7544e664d4fcd6.json` |
| Network | 27 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c74dce387b23cdd2d5948563a31e75316f960d7b795bb453a68813b269609e02/390aa940b5a8c3370c35f5df568021f4b315e700f89207af2bb6ac66725b9b09/gui-inspect.85257fea3951b406.json` |
| Warlord command | 17 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9e0498d89413eb187ee66ec4e3827ac4d20e032b49a87a1efcd21414fe2f3629/582a6dd7c9ecce873f37c247294801895282f05ea25a41775b48f081c4bd54c3/gui-inspect.7f08a1b3a1adc504.json` |
| Revealed command | 17 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6512884a12668aa1c94d0f3c519d0cff54f3b286109176a2eb15237eb3ec0313/04c0aaab2a1d81008a6b1f28cca1ae78eee03f757eef82f62ed048d11dea36c3/gui-inspect.0651d33ac6818cf7.json` |
| Wendigo command | 17 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4517cc0953659a164a39a489a62052aa8eca4d5f501839c849168ce422093818/bb0f44b0f423288825baede961ec7e6bcc585af3c3282543fe801e4d160b3f14/gui-inspect.a382d291438b4717.json` |

Every inspection was blocked as acceptance evidence by the global 2000-diagnostic ceiling.

The returned summary omitted the paths and exact elements for most layout findings.

The inline counts reported visible-overlap findings of 21 for the early header, 11 for the network window, 22 for the Warlord window, and 25 each for the revealed and Wendigo windows.

Those counts include intentional layered backgrounds, frames, portraits, meters, and overlays and cannot support a source rewrite without element attribution.

The network inspect also omitted one click-bounds mismatch from the returned diagnostic body, so it cannot be assigned to either target selector.

## Fresh render evidence

Each render call requested normal, hover, selected, locked, disabled, warning, minimum-value, maximum-value, long-text, and missing-localisation states where applicable.

The network request also included empty-list and full-list states.

Each call requested 1366x768, 1600x900, 1920x1080, 2560x1440, and 3840x2160.

| Window | Returned artifact |
| --- | --- |
| Early header | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fcfae968916de2c03f1a02f42bf5dc720fcc83c255414d77af125652efc1ea15/83e7f9966c0e714e49046906ef8f382458a0b666db9ecea6f2c2cb9ea19a727d/cannibalism_early_header_window-full.svg` |
| Network | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/2e59e66223916132300144646a44ecbe55a027a0a61834280097a513bebbd46c/cannibalism_network_window-full.svg` |
| Warlord command | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/356eda9a5565ef7475fbeca05d9002dcef5a8fbdc5f659787da7ef3a485f6ca7/1916c03fe61b063731e6c328cdff6b8221639f6b1ef7740ebdca8b1d22d95314/cannibalism_warlord_command_window-full.svg` |
| Revealed command | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9/ab8b643bb3414151f7c8f419aec16829e1d5a947a6fd04c3572fb1f9d80a64d1/cannibalism_revealed_command_window-full.svg` |
| Wendigo command | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5dca062f0ceea5b6be78543b2af1390a739f0896c5517587b74aaa42190738c7/94ae404ca5c7fab32ca03590fb26e796d948ac492efc895d957be2936e4db150/cannibalism_wendigo_command_window-full.svg` |

Every call returned one artifact and `MCP_RESPONSE_TRUNCATED` with no validation checks.

Readable artifacts identify themselves as 1920x1080 with UI scale 1 regardless of the requested resolution matrix.

The renderer records substituted project font metrics and only the primary frame for frame-sequence sprites.

It omits tooltip presentation from the offline scene.

An isolated `cannibalism_revealed_command_window` retry requested only normal state at 3840x2160.

It returned the same content hash as the 1920x1080 artifact.

Its SVG root is explicitly `<svg width="1920" height="1080" viewBox="0 0 1920 1080">`.

Isolated 3840 retry artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9/527f4815de46760e9551eac022f9a3213bf5ce1700f1ccfb6b0c7892be0178b7/cannibalism_revealed_command_window-full.svg`.

This proves that the route did not honor the isolated resolution request.

Repeating identical resolution calls would not add evidence, so no further identical retries were made.

## State and resolution coverage

| Requested coverage | Result |
| --- | --- |
| Normal | One 1920x1080 full-window artifact per window |
| Hover and selected | Requested, no distinct artifacts returned |
| Locked and disabled | Requested, no distinct artifacts returned |
| Warning | Requested, no distinct artifacts returned |
| Empty and full network lists | Requested, no distinct artifacts returned |
| Minimum and maximum values | Requested, no distinct artifacts returned |
| Long text | Requested, no distinct artifacts returned |
| Missing localisation | Requested, no distinct artifacts returned |
| 1366x768 | Requested, no artifact at this resolution returned |
| 1600x900 | Requested, no artifact at this resolution returned |
| 1920x1080 | One full-window artifact per window returned |
| 2560x1440 | Requested, no artifact at this resolution returned |
| 3840x2160 | Requested and isolated retry performed, but the route returned 1920x1080 |

The mandatory state, hierarchy, click-region, clipping, scale, and resolution comparison matrix therefore remains unresolved.

## Source and rewrite disposition

`interface/014_cannibalism_frontline_hunger.gui` already had concurrent changes to the network counter tab, sort, and refresh positions before this worker resumed.

Those changes were preserved and were not staged or reverted.

The fresh inspect results do not retain exact Event 014 element attribution for their overlap, clipping, text, or click-bounds counts.

The fresh render results do not expose distinct requested states or resolutions.

Using `hoi4.gui_rewrite` under these conditions would require guessing which intentional layered elements should move or resize.

No rewrite was attempted.

No Event 014 GUI source, scripted GUI helper, GFX file, asset, or localisation file was changed.

## Completion status and remaining blockers

This audit is incomplete as visual acceptance evidence.

The exact blockers are `GUI_GRAPH_DIAGNOSTICS_TRUNCATED`, `GUI_VALIDATION_DIAGNOSTICS_TRUNCATED`, `MCP_RESPONSE_TRUNCATED`, missing per-state artifacts, and the renderer returning 1920x1080 for an isolated 3840x2160 request.

The next useful MCP pass requires the server to honor one requested state and resolution per artifact and retain Event 014 element attribution for bounds, overlap, clipping, and click-region findings.

No simplification, fallback, or speculative source change was made.
