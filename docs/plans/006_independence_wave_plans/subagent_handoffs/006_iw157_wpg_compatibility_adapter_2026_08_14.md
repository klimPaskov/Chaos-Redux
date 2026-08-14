# IW-157 WPG compatibility adapter handoff (2026-08-14)

## Disposition

IW-157 remains a `specific_community_variant_only` research HOLD and has no authoritative current-map binding. This tranche adds only dormant, package-local preservation predicates and a selector cleanup wrapper for the registered vanilla `WPG` carrier. The future selector `independence_wave_iw_157_named_community_selected` is deliberately never set here, so the adapter has no current gameplay effect.

No central admission, Join, preflight, attestation, dispatcher, scenario allowlist, FORM-39 writer, event, decision, focus, force, asset, localisation, workbook, or vanilla-file change was made. No map write was attempted, and no country identity or generic West Papua substitute was introduced.

## Changed files and identifiers

| File | Added surface | Runtime behavior |
| --- | --- | --- |
| `common/scripted_triggers/006_independence_wave_iw157_wpg_compatibility_triggers.txt` | `is_independence_wave_iw_157_wpg_compatibility_context`; `has_independence_wave_iw_157_wpg_anchor_surface`; `has_independence_wave_iw_157_wpg_vanilla_surface`; `has_independence_wave_iw_157_wpg_compatibility_contract` | Read-only, fail-closed witnesses for living `original_tag = WPG`, Event 006 origin, package `iw_157`, future named-community selection, anchor state `669`, secondary core state `1057`, and `INS_releasables` membership. |
| `common/scripted_effects/006_independence_wave_iw157_wpg_compatibility_effects.txt` | `independence_wave_iw_157_wpg_compatibility_clear_named_selection`; `independence_wave_cleanup_iw_157_wpg_compatibility` | Clears only the future named-community selector after the complete contract passes. It never sets the selector or changes WPG, states, cores, leaders, assets, or origin state. |

## Country package coverage checklist

| Surface | Result | Evidence / gap |
| --- | --- | --- |
| Tag registration and consistency | Preserved | Vanilla `common/country_tags/00_countries.txt:355` registers `WPG = "countries/West Papua.txt"`; no tag or alias was changed. Chaos Redux registry/constants already list IW-157/WPG. |
| Country definition and history | Source-only HOLD | Vanilla `common/countries/West Papua.txt` has graphics/color only; no vanilla `history/countries/West Papua.txt` exists. No replacement history or leader was invented. |
| Anchor state/core/capital | Bounded witness added | Vanilla `history/states/669-Dutch New Guinea.txt` and `1057-Dutch Southern New Guinea.txt` core WPG; the adapter requires ownership/control/capital on exact anchor state `669` and witnesses core `1057`. |
| Japanese interaction | Preserved by non-interference | Vanilla `common/national_focus/japan.txt` focus `JAP_strike_the_southern_road` leads to war with WPG and can create an annexation wargoal; no Japan source was edited. |
| Indonesian interaction | Preserved and witnessed | Vanilla `history/countries/INS - Indonesia.txt` includes WPG in `INS_releasables`; the adapter checks that row. Existing Indonesian decision targets and release behavior were not edited. |
| Indonesian transfer/leader surface | Explicit gap | Vanilla has no `indonesia_transfer_WPG` effect and no WPG country history/leader surface. The adapter therefore has no character predicate and does not invent a transfer role. |
| Named-community gate | Fail-closed | The future selector flag is required by every predicate and has no writer in this tranche. Research still requires an exact named people-and-district package contained by state 669. |
| Living-tag/origin guard | Bounded witness added | Every contract path requires `exists = yes`, `original_tag = WPG`, active Event 006 origin, exact package id `iw_157`, and the selector; the shared active trigger also rejects ended origins. |
| Release/spawn/cleanup | Cleanup only | No release, spawn, transfer, annexation, puppet, or cosmetic-tag logic was added. The cleanup wrapper clears only the future selector after full proof. |

## File surface checklist

| Surface | Result |
| --- | --- |
| Local scripted triggers/effects | Added the two package-local files above; they auto-load from existing folders and have no central caller. |
| Events and event details | No WPG-owned event exists in this tranche; Event 006 root `chaosx.nr6.1` was inspected read-only. |
| Focus tree | WPG has no own tree; Japanese `japan_wtt_focus` dependency was inspected read-only and left untouched. |
| Decisions/missions | No WPG-owned decision or mission was added; existing Indonesian WPG interactions were source-reviewed and left untouched. |
| Technology | No WPG-owned technology or doctrine dependency was identified; no technology claim is made. |
| AI/weighted surfaces | No AI weight, strategy factor, probability, or MTTH surface was changed; the mandatory probability audit route was therefore not applicable. |
| GUI/map/assets/localisation/workbook | No surface changed. No asset, flag, portrait, advisor, party, localisation, map, or spreadsheet write was made. |

## Politics, leader, portrait, flag, advisor, and party issues

WPG's vanilla country file has no leader/history setup and no package-specific character, advisor, party, portrait, or flag surface. The current IW-157 research handoff requires a sourced real male period leader or authentic archival institutional evidence for the exact named community, and rejects generic or generated identity substitution. Existing vanilla color/flag/localisation and Japanese/Indonesian behavior remain preserved. These identity inputs remain unresolved and block admission.

## Focus, decision, idea, and asset issues

There is no WPG-owned focus or decision package to patch safely. The Japanese focus `JAP_strike_the_southern_road` and Indonesian decision/release interactions remain vanilla-owned. No ideas, icons, portraits, flags, or other assets were promoted because the named community, source date/role, and symbol/flag evidence remain unresolved.

## Starting military, technology, industry, supply, and production issues

No WPG history or Event 006 starting setup exists to audit or change. Military, technology, industry, supply, production, and force-profile content remains an unimplemented package surface and is intentionally outside this compatibility-only tranche.

## AI and playability issues

No WPG AI strategy or playability setup exists in this tranche. The adapter cannot admit a country, release a generic carrier, or make IW-157 selectable. The package remains unbound and fail-closed until named-community research, current-map containment, identity/asset evidence, setup, and runtime admission proof are separately accepted.

## Source and engine-backed evidence

- Offline wiki pages consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, country creation, state modding, and map modding.
- Vanilla documentation consulted: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, and `documentation/modifiers_documentation.md`.
- Chaos Redux source/spec authority: `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` IW-157 row; `docs/specs/006_independence_wave_specs/research/006_sensitive_package_resolution.md`; `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv` RG-NEW-GUINEA row; `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` IW-157 row; `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw157_iw178_new_guinea_source_research_current_2026_08_03.md`; and `docs/events/006_independence_wave/form39_melanesian_federation.md`.
- Read-only HOI4 map inspect covered states `669` and `1057`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/831b85e1c60e027d196f2d4d536bf85d481b65d36492051433d22971fa2dbf5a/2f12d1731ea7566b2fefe1b953c5d3986234ff69d36809cdf726a31fdf0776f9/map-inspect.24bebf72ae84437c.json`. Selected state membership/geometry was available; aggregate validation also reported unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics elsewhere in the workspace.
- Read-only state render evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c8a38f2a0c09e2af8e7995c5a27803696c79c642b4d19a9fb7e001d8d2e9ae9/f687ba682d4cab3e3fb8ddb7a751b9f1c27af1bc14ad3b89e2d92305cb8aec54/map-state.png`.
- Read-only Event 006 inspect evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62668c98ccd7f4279878b93e75a83e36295e7c77154c18d06d9f1bfda9fdc821/c28a9c369729ae8da2315040bc00ff4ca00993e11d7abb603d8f3d8523e38429/event-state_flow-741883f50501.json`. The inspector returned partial validation because large-workspace helper/lifecycle projections were deferred; no selected WPG blocker was reported.
- Read-only Event 006 render evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fa0175af9c12eb9eec117b596be4f77755cc0e435036e3025619b83817fa8d2/cdec27f4dcf49f87654974db0f817a232f0d141caea0523c68a8a102a4381ce4/event-overview-741883f50501.png`. Render was partial for the same deferred large-workspace projections.
- Read-only Japan focus inspect evidence for `japan_wtt_focus`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85fee8b028fdb2bbeded390df721cd7b205639e456fc7e243e5d9bd4564b73aa/ec22d69da7e3a87965b062149191c23c4687452c06488d539880aae167148e17/focus-inspect.5bb17398adee2259.json`.
- Read-only Japan focus render evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9dd651c9f4a2449a3b08b84d28a7f603f1eb2d6eb4b89af50046ac5a50a032df/08cb6113449fb2b3e0636684686befcddf79597d0800966c424d76d7fd018788/japan_wtt_focus.focus.svg`. The focus inspector/render reported existing broad-tree diagnostics, not a WPG-specific change; no Japan source was rewritten.

## Validation and remaining risks

Task-specific static review confirmed the three new files contain only the identifiers listed above, balanced Clausewitz blocks, and no unsupported comparison operators. A targeted source scan confirmed no new central admission/preflight/attestation/Join/dispatcher call, no WPG leader/asset/localisation writer, and no vanilla file edit. No live game run was performed; live consumer validation belongs to the parent/user workflow.

Remaining blockers are the unresolved named-community/district containment proof inside state 669, period-valid role/source and portrait rights, community-specific symbol/flag evidence, complete WPG setup/force/AI/playability package, and the existing FORM-39 member/consent/identity gates. Keep the selector unset and do not promote IW-157 or set `independence_wave_wpg_melanesian_member_research_complete` from this handoff.
