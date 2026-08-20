# Event 016 Directorate color integration post-audit

Date: 2026-08-20

## Result

The post-color Event 016 Directorate surface remains the accepted compact 500x360 decision-category display. No GUI geometry, scripted-GUI presentation logic, gameplay, costs, effects, or AI was changed. The only file created by this audit is this handoff.

The composed render was reviewed as a compact four-row composition. The cyan Mandate, amber Dependence, crimson Exposure, and emerald Capacity rows align with their matching tinted background bands. The title, portrait, profile label, status line, footer, meter labels, and mutually exclusive open/close controls do not overlap in the reviewed composition. The four colors are reinforced by stable row labels, separate meter sprites, and fixed vertical positions, so color is not the only cue.

## Event ownership and entry point

The accepted Event 016 spec at `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_2_host_directorate_and_decisions.md` requires the Directorate to expose exactly Mandate, Dependence, Exposure, and Project Capacity. The implementation handoff at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_directorate_implementation_handoff.md` identifies `brilliant_scientist_directorate_category` as the Event 016 host-Directorate category.

The event-owned attachment chain is:

- decision category and entry point: `brilliant_scientist_directorate_category` in `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`
- attachment: `scripted_gui = brilliant_scientist_directorate_scripted_gui`
- scripted GUI: `brilliant_scientist_directorate_scripted_gui` in `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`
- exact window: `kruger_directorate_container` in `interface/016_brilliant_scientist_directorate.gui`
- GFX registration: `interface/016_brilliant_scientist_directorate.gfx`
- GUI localisation: `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`

The surface is not part of the shared event log, event-details framework, settings UI, super-event framework, or another shared interface.

## Source and precedent review

Required offline wiki pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding. Installed vanilla `common/scripted_guis/_documentation.md` was consulted for the decision-category attachment and element trigger contract. The exact vanilla precedent inspected was `common/scripted_guis/RAJ_famine_scripted_gui.txt` with `interface/RAJ_famine.gui`, which uses a bounded decision-category scripted GUI and a dedicated independent window.

## Layout hierarchy and budgets

- root: `kruger_directorate_container`, 500x360, clipped
- collapsed branch: `kruger_directorate_compact_panel`, 500x58, background, short title, open control
- expanded branch: `kruger_directorate_full_panel`, 500x360, full background, title at y=22, close control, portrait/profile region, four metric rows, one status line, and footer
- metric rows: meter y=82/126/170/214 and value text y=89/133/177/221
- visible mechanic values: four, exactly at the hard ceiling and exactly matching the accepted spec
- primary/supporting hierarchy: Mandate is the authority lead, with Dependence, Exposure, and Capacity as distinct pressures with separate causes, consequences, and responses
- GUI action budget: zero gameplay-changing actions; two mutually exclusive presentation controls, open and close
- active mission/target controls: zero inside this display
- cost-count audit: zero GUI costs and zero spendable cost types
- texticon coverage: not applicable because the display has no costs
- text-density audit: one title, four single-line metric labels, one compact status line, one footer, and concise two-line metric tooltips; no subtitle, tabs, cards, panels, paragraph ledger, or extra control is instantiated by the current `.gui`

## Background coverage map

| Background region | Intended content | GUI elements | Status |
| --- | --- | --- | --- |
| top title band | Directorate identity and collapse control | `kruger_directorate_title`, `kruger_directorate_close_button` | aligned |
| left portrait field | Kruger portrait, frame, and name | `kruger_directorate_profile_frame`, `kruger_directorate_portrait`, `kruger_directorate_profile_name` | aligned, no control overlap |
| cyan row | Mandate meter and value | `kruger_directorate_mandate_meter`, `kruger_directorate_mandate_value` | aligned |
| amber row | Dependence meter and value | `kruger_directorate_dependence_meter`, `kruger_directorate_dependence_value` | aligned |
| crimson row | Exposure meter and value | `kruger_directorate_exposure_meter`, `kruger_directorate_exposure_value` | aligned |
| emerald row | Capacity meter and value | `kruger_directorate_capacity_meter`, `kruger_directorate_capacity_value` | aligned |
| lower status field | role and government-control summary | `kruger_directorate_role_control` | aligned |
| footer strip | points the player to ordinary decisions | `kruger_directorate_footer` | aligned |

## State and click-region matrix

The MCP render request covered normal, hover, selected, active, disabled, warning, completed, empty-list, full-list, and long-text at 1366x768 and 1920x1080, with full and collapsed related scenarios. The route emits full-window, cropped, annotated, hierarchy, click-region, state, resolution, fidelity, and comparison evidence as one linked evidence package; the wire response exposed only the primary full SVG URI.

The scripted-GUI state contract keeps the collapsed and expanded children mutually exclusive through `brilliant_scientist_directorate_gui_collapsed`. The only click regions belong to `kruger_directorate_open_button` and `kruger_directorate_close_button`. Their visible bounds and scripted effects correspond directly, and all meter, portrait, text, and background elements remain informational.

Generic selected, active, disabled, warning, completed, empty-list, and full-list probes do not add event-owned controls or values. They are retained as renderer stress states. Long-text remains an offline approximation because the current English strings are short and the renderer substitutes deterministic font metrics.

## Localisation keys in the compact surface

- `brilliant_scientist_directorate_gui_compact_title`
- `brilliant_scientist_directorate_gui_open_tt`
- `brilliant_scientist_directorate_gui_title`
- `brilliant_scientist_directorate_gui_close_tt`
- `brilliant_scientist_directorate_gui_profile_name`
- `brilliant_scientist_directorate_gui_role_control`
- `brilliant_scientist_directorate_gui_mandate`
- `brilliant_scientist_directorate_gui_dependence`
- `brilliant_scientist_directorate_gui_exposure`
- `brilliant_scientist_directorate_gui_capacity`
- `brilliant_scientist_directorate_gui_mandate_tt`
- `brilliant_scientist_directorate_gui_dependence_tt`
- `brilliant_scientist_directorate_gui_exposure_tt`
- `brilliant_scientist_directorate_gui_capacity_tt`
- `brilliant_scientist_directorate_gui_control_tt`
- `brilliant_scientist_directorate_gui_footer`
- `brilliant_scientist_directorate_gui_footer_host`
- `brilliant_scientist_directorate_gui_footer_sovereign`

The value strings and tooltip headings use Mandate `§C`, Dependence `§Y`, Exposure `§R`, and Capacity `§G`, matching the four asset families.

## Runtime asset hashes

These current hashes match `016_directorate_color_art_2026-08-20.md`:

- `directorate_background.dds`: `380F0AF0B9A77D19A692B2A86B8D31D12BC14DA3B297F996A80B61A0F7563534`
- `meter_mandate_low.dds`: `D26841549965D96FDE6B7BE4BF950CA515041DFD6916F42941D04045B2A3A56F`
- `meter_mandate_moderate.dds`: `B9D9B5BFAE8C620D867D6B7F21D7CB17C804F85434CC3A3754B0B103557DF165`
- `meter_mandate_high.dds`: `B9C41B2A327A6C507A0D4F650FECC91AAA98AC03FF40DFB625CADFD563FCE49A`
- `meter_mandate_extreme.dds`: `6CC3FB039FAD8D88D414BD90805F16317871A9292B48AD641F19E9EFA2E1A70A`
- `meter_dependence_low.dds`: `B408EEFA0F114F897CCB1E669540D8BC3829EC2C45B8A10D9182350D11ED1BDD`
- `meter_dependence_moderate.dds`: `50E789CF5EBB9EEBA1D64F3104E0CB127C63E0F97FA8BE266F8C439215C61CAA`
- `meter_dependence_high.dds`: `6B5313AF07BBBD87936B29A685465EFCA029626B20E9044BFF2F74918A2AA1EF`
- `meter_dependence_extreme.dds`: `1A668C1F912E0D109232B265B459B554FE90B493AE3B29FB5DDE8B04C9E6F6FE`
- `meter_exposure_low.dds`: `5B3B25088617C01659022B33566C036E49769BB21A2F1884CFF88203203C7A92`
- `meter_exposure_moderate.dds`: `2AAF8A3085BE6D1FF41FD511816C24A236060BA6BC037D6FB1DD07BCDC82AFB9`
- `meter_exposure_high.dds`: `72AC178168EBCE30D0A52A041406344B6508BD63FB8F700E2E6E77827316E478`
- `meter_exposure_extreme.dds`: `EB6381B506C2A770B5D7B7816CA630D1568BA70E92E5C52E588F90432D66310F`
- `meter_capacity_low.dds`: `C2CEB3A47BDCA82954CA7E69B6FF234FA5E53202378F85DD996CBD57EC7994EE`
- `meter_capacity_moderate.dds`: `A16DF1F26952B14512DD6B3494C09F109E6A0DA57B38EEFBF6DA9AE1FD6CF2BC`
- `meter_capacity_high.dds`: `A1F0F5B12DD0300B1DC797CEC6C7BF83FA7F3E7C711451A59D4E17A0826E924D`
- `meter_capacity_extreme.dds`: `C0919D6767EBE35E4B53079394351134BE6F6290A52BECEC301BA75DEFF62C4A`

The corresponding stable sprites are `GFX_kruger_directorate_background` and `GFX_kruger_directorate_{mandate,dependence,exposure,capacity}_{low,moderate,high,extreme}`.

## MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`

Shared source revision before and after the identity rewrite attempt: `44699c01cb2e4a5e7a76c27a3cce6e20dfb0c99329a5e378d6c155da8e340a85`.

Pre-attempt inspect:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d1fa3be5896d2e6b741a6b37c50401ce7a749366997c21cc3ae612fa404ac6e/b5751faa4be57a8d14a527bf0301542ef717fad8f2668f70b8e2eaf699848e70/gui-inspect.44699c01cb2e4a5e.json`

Pre-attempt render matrix primary artifact:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37ff77d27cefc33ffbf1da50bb2e953003a4841dd3f75a7a8e0cc8a96ee4d085/be4d0026b9c0f392e9184717627eafaa318109782f4e033c84b1377356d1d4aa/kruger_directorate_container-full.svg`

Identity-preservation `hoi4.gui_rewrite` attempt:

- route status: `blocked`, code `GUI_CHANGES_BLOCKED`
- reason: the rewrite validator consumes the repository-wide GUI graph and hit `GUI_GRAPH_DIAGNOSTICS_TRUNCATED` plus unrelated active symbol collisions before it could accept even identical source
- `changedFiles` was empty and the Event 016 source was not rewritten
- before PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e1e4f1a8d81affcfa4f8c9de9a5eb3510639ba2353e313b9b466089421b3ecd/91503db88b03733138173983a8012543e77802a13a2cc5eebf5b8997a6fb7c0e/kruger_directorate_container-before.png`
- proposed PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e1e4f1a8d81affcfa4f8c9de9a5eb3510639ba2353e313b9b466089421b3ecd/b702d09b3ab442eb6442d3014232ddac8555e7000c5ae3fcd3b6081e77854b45/kruger_directorate_container-proposed.png`
- exact visual comparison: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/86a3645cb46f1398dfe8761b23cfa1c05e2552c27c2598e6bd45e75ec7e2b797/kruger_directorate_container-visual-diff.json`
- comparison result: `changedPixels = 0`, `changedRatio = 0`, 1920x1080, offline threshold 8
- rewrite validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae35b0bb47c6c0395a59a27ce26ccd8b03a0abbc7f00271ab79fe45a1d072259/30d7ff52f3edb11d2d767bc0d1c7d58d6493e1c4ab8c242665f11f6656321c5e/kruger_directorate_container-rewrite-validation.json`

Post-attempt inspect:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f0b95de351346900c6d531d1566e2596cb61f25d695713e86bb4164bd7ca6f24/fd918e6f4534c403b9287c04d68746e0c2fea5d05d366b2bcbe6722c1c535965/gui-inspect.44699c01cb2e4a5e.json`

Post-attempt render and comparison matrix primary artifact:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37ff77d27cefc33ffbf1da50bb2e953003a4841dd3f75a7a8e0cc8a96ee4d085/b4b7b0407a6d9f527437d4dfb9690dd969e82ddf84f06f4fef9424ba50cc4cb8/kruger_directorate_container-full.svg`

Both inspect passes found 22 elements with the same shared revision and fidelity counts. Both render matrices produced the same primary SVG SHA-256 `37ff77d27cefc33ffbf1da50bb2e953003a4841dd3f75a7a8e0cc8a96ee4d085`.

## Limitations and remaining parent-owned validation

- The MCP global graph retains thousands of unrelated repository-wide symbol collisions and truncates its aggregate diagnostic list. Those aggregate diagnostics prevent the rewrite route from accepting identical source and cannot be interpreted as an Event 016-local defect.
- The render response was wire-truncated, and direct resource retrieval of the large SVG was byte-truncated. The parent separately raster-reviewed the fresh composed post-color render and reported the compact 500x360 composition clean. The rewrite route's complete before/proposed PNGs also have identical SHA-256 values and its complete JSON comparison reports zero changed pixels.
- The named collapsed scenario is retained as linked MCP evidence, but the offline scenario route does not prove live flag mutation semantics by itself.
- Live consumer behavior, in-game font rasterization, actual decision-tab anchoring, hover/pressed frame behavior, and gameplay/runtime acceptance remain parent and user owned.
- No missing asset, fallback, placeholder, geometry simplification, gameplay simplification, or unapproved substitute was introduced by this audit.

