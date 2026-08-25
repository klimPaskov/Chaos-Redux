# Event 016 current MCP audit receipt

Date: 2026-08-26

Scope: current read-only MCP evidence after the country-owned Alien Infantry landing-registry correction and the player-facing localisation tranche. No gameplay source was changed by this audit.

## Event and Event 019 state flow

`hoi4.event_inspect` inspected `chaosx.nr16.47` in both directions with helper expansion, bounded depth six, and bounded nodes and edges. It returned `EVENT_INSPECTED_PARTIAL`, status `ok`, revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5`, zero blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94eaa4862016956958bae29a2fba697a0e3f1efd857ff96c4fbb3381c76ccb38/cf509287edc5293ffdfebfa2f78ddcd1972b2ee23764f5d60435b01fa7a2b23b/event-state_flow-f588a2607444.json`. The matching lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/678bfabc6eb84fdbff224e0d7fae1f62e48aee85d4d7780a78e2c8043c716038/5afba29c4a86076360b6e191bb05a6ed5a52ef004fef10ceccdc53cd956ad19b/event-lint-f588a2607444.json`.

The read-only Event `.47` state render produced the manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd81c30903ef30ef048a6478c0c9e6795e0e6371e82631f253c3e17581525cda/ca626de89826dfcdd32e35b58609f9f2491151a02727e318add020b45e91049e/event-state-f588a2607444-manifest.json` and linked JSON, SVG, and PNG artifacts. The renderer reports no blocking diagnostics but defers workspace-wide helper projections because the workspace is large.

`hoi4.event_inspect` also inspected `chaosx.nr19.1` in both directions with bounded helper expansion and returned `EVENT_INSPECTED_PARTIAL`, status `ok`, the same current revision, zero blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0676ae7909104fca3360c55205ebbb4cb452f62d4b8be7a19aa28648c2613095/701a8468b6893f1b27cb6829ae2478ce65997462e0eee17b947da8b454a9aaad/event-state_flow-f588a2607444.json`. This is structural provider-chain evidence only; it is not a live one-cohort or 2,000-gun conservation proof.

## Rebellion weighting

`hoi4.probability_inspect` first listed the installed adapters, then inspected `common/scripted_effects/016_dhrondan_contact_effects.txt` with `custom_weighted_pool` and `direct_random`. The custom-pool route returned `PROBABILITY_SOURCE_INSPECTED` with no declared custom-pool candidates. The direct-random route discovered the supported `random_list` adapter and the two revolt/no-revolt branches.

A bounded `hoi4.probability_evaluate` run used the two branch candidates and named LOW, MEDIUM, and HIGH scenarios with revolt/no-revolt weights of 10/90, 20/80, and 40/60. It returned `PROBABILITY_ANALYZED`, zero unresolved inputs, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e6b12c1c58d429149c8cfd862db1eb27fa2828abe9b019d28f7742f5b3bc5d5/4f8da02cda90ddb1005a32456c01c0b3f80491073478574d0c2381ef2d085338/probability-ce533f32be4dd0efbce3f9f8.json`. The only diagnostic is the intentional 90% no-revolt dominance in the low tier. This proves conditional branch arithmetic, not cumulative 90-day campaign timing.

## D’Rhondan focus tree

`hoi4.focus_inspect` inspected `common/national_focus/016_dhrondan_focus_tree.txt` as `dhrondan_focus_tree`. It returned `FOCUS_INSPECTED`, 88 focuses, 102 connectors, zero crossings, zero node intersections, zero long connectors, exact title resolution for all 88 focuses, and no DHR-specific diagnostics. The current artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ab31f7f3b3db75186edae4832c433bb17d3cf8ac4a1c40a5a771b4b80d13ead/c36e3b3ed4f8b3dfe32fffe86a965bb1e0d1cbe54c7519a86ec48824f5dec0da/focus-inspect.cffdde6def51b0c0.json`.

`hoi4.focus_render` produced HTML, SVG, JSON, source-map, and plan artifacts for the same tree at 6992 by 2788 pixels. The render returned `FOCUS_RENDERED` with no blocking diagnostics. The only warning is the inherited vanilla `continuous_restrict_freedom_desc` localisation reference, outside the DHR tree.

## Directorate scripted GUI

`hoi4.gui_inspect` inspected `kruger_directorate_container` under scenario `event016_directorate_compact_current` and returned `GUI_INSPECTED` with 22 exact Event 016 elements. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a755b7324445bb88434e9613711b92daefcddd410e50124c56969d43225a3710/316ed573267e20625432412e0b8f9277b772a6022745f36dd9ef95f4c0ea4fa1/gui-inspect.ab24df94636a45c9.json`. The global GUI graph still reports thousands of unrelated symbol-collision and overlap diagnostics, so this is not a clean workspace-wide GUI certification; the exact Directorate surface is present and inspectable.

`hoi4.gui_render` returned `GUI_RENDERED` for the same window with normal, hover, disabled, warning, active, long-text, and missing-localisation states at 1366x768 and 1920x1080. The current linked SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce/eb45207d69a6d48fb59949eb762a10a3b52bbe29908a3cd9dc294bfe54351b64/kruger_directorate_container-full.svg`. The response was truncated on the wire, but the artifact itself is retained by MCP. No GUI rewrite was justified in this pass because the source already matches the accepted compact layout and the graph diagnostics are dominated by unrelated active definitions.

## Alien Infantry technology

`hoi4.tech_inspect` linted `brilliant_scientist_alien_infantry_tech` with bounded dependency expansion and returned `TECH_INSPECTED_PARTIAL`, source-linked revision `3793d2e9b80ba12de1803e1ff84dde8d38933522368ceadebdc52e938d17d6c6`, and linked lint artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c593b1abca1ef9b2a2fa9d0b815e56b9ffbee40ec6c0f1ca53acec9f3fdc0529/54e9ffc10845a147e6f7687ac031f8c57eb55b5b3e10ed7c5333823fefe2f72c/technology-lint-3793d2e9b80b.json`. Workspace-wide helper projections were deferred by the large index.

`hoi4.tech_render` rendered the same technology as a source-linked JSON, SVG, PNG, and manifest package under `technology-3793d2e9b80b`. The render is partial because the shared technology index defers helper projections; it is not a claim that every 672-technology workspace issue is resolved.

## Map and state records

`hoi4.map_inspect` completed a full map catalog and a targeted state query for states 1, 12, and 77. The targeted artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f2154f813f3d5da9ee50018c48f0c2b3bd5a174db50a400d1ca27f94fd182a7/dd579f7183317c4cc091189d040fe844385a4701ca7bbb3091c6bddc2ca93773/map-inspect.1bbbbf9bcba2fc25.json`. State membership, province geometry, networks, and adjacency checks passed. The map workspace retains pre-existing `map/buildings.txt` position and floating-harbor errors (2,654 omitted diagnostics after truncation), so no clean map-wide validation claim is made and no Event 016 map file was changed.

## Remaining validation boundary

These MCP artifacts do not replace user-owned in-game acceptance. They also do not close the two custom-unit runtime blockers: Alien Infantry still lacks an accepted stable muzzle locator and all required verified defend, support-attack, retreat, and death action consumers with synchronized particle/audio binding, and Portal Raider remains without an accepted firearm-bearing model/entity package. The Portal beachhead state-marker lifecycle and five D’Rhondan support-route consumers remain queued because no accepted lifecycle owner exists. The custom `chaosx_ai_probability_auditor` route and same-scenario `hoi4.probability_compare` remain unavailable in this runtime.

No gameplay source was changed by this audit. The country-owned registry correction is committed in `d77afae7e`; the wording tranche is committed in `89f80a2a2`.
