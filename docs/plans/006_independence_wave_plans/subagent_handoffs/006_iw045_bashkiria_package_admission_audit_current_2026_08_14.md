# IW-045 Bashkiria package admission audit (current source, 2026-08-14)

> Superseded for central routing by the parent promotion receipt `006_iw045_bashkiria_promotion_current_2026_08_14.md`. This audit remains package-local evidence and preserves the earlier fail-closed review boundary.

## Superseding lifecycle addendum (parent follow-up, 2026-08-14)

The previously identified `bsk_oilfield_council` lifecycle gap is resolved in `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt`: the idempotent oilfield-communities reward adds the idea, while package setup and both package-idea cleanup paths remove it. The static allocator and SCN-008 matrix audits still pass at 40 adapters, 31 attestations, 28 compatible groups, and 162 unattested rows. A fresh `.350` event inspect/render remains `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` with zero blocking diagnostics (revision `d21fdfa2723e4a624054076fb1104ba638c4fbb1f733358a99b24aac1839ace2`); BSK strategy inspection remains `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`. The central admission verdict is unchanged: IW-045 remains outside content attestation, normal/scenario preflight execution, and deterministic Join pending a fresh independent re-audit of the complete package and typed evidence.

## Verdict

IW-045 (`iw_045`, vanilla carrier `BSK`) remains **PACKAGE-LOCAL COMPLETE / CENTRAL ADMISSION FAIL-CLOSED**. Content attestation, normal preflight, scenario preflight, and deterministic Join must not be widened from this audit. No central file was edited.

The package-local adapter is present and the exact BSK/state-651 proof is coherent, but the central content-attestation allowlist does not contain `iw_045`. Both preflight predicates require that allowlist, so their existing IW-045 branches cannot pass. The deterministic Join candidate sequence also has no `iw_045` entry. Adding any of those central entries would be an admission change, not a package-local repair, and is outside this audit's authority.

## Required source and reference review

Before reviewing source I read `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-comfyui`, and `chaos-redux-improvement-loop`. I consulted the offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, country creation, national focuses, characters, portraits, states, divisions, units, maps, cosmetic tags, and graphical assets. I also read the relevant installed-vanilla documentation files under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including effects, triggers, script concepts/constants, modifiers, and localisation formatter/object references. Vanilla BSK history and character files were checked directly.

## Country-package coverage checklist

| Surface | Current evidence | Result |
| --- | --- | --- |
| Carrier/origin | `common/scripted_triggers/006_independence_wave_bashkiria_package_triggers.txt:8-14` requires `original_tag = BSK`, package id `iw_045`, active-country scope, and rejects both Soviet-collapse origin forms | Pass |
| Map anchor | `common/scripted_triggers/006_independence_wave_bashkiria_package_triggers.txt:61-93,99-110` binds capital/owned-and-controlled anchor to state `651`; vanilla `history/countries/BSK - Bashkortostan.txt:1` is `capital = 651` | Pass (MCP caveat below) |
| Former host | Package setup/runtime gates require the actual planner-captured living former host and protected-state owner relation (`...bashkiria_package_triggers.txt:68-90,156-164`) | Pass |
| Vanilla roster | Vanilla `common/characters/BSK.txt` defines male `BSK_yakov_bykin` / Yakov Borisovich Bykin; vanilla history recruits it at line 101; package roster trigger is `...bashkiria_package_triggers.txt:95-97` | Pass |
| Portrait runtime | `events/006_independence_wave.txt:306-324` applies only `GFX_portrait_BSK_independence_wave_yakov_bykin` to `BSK_yakov_bykin`; cleanup restores `GFX_portrait_Yakov_Borisovich_Bykin` at `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt:430-442`; no global vanilla override | Pass |
| Portrait asset/GFX | `interface/006_independence_wave_iw045_bashkiria_portraits.gfx` points to `gfx/leaders/006_independence_wave/portrait_BSK_independence_wave_yakov_bykin.dds`; grounded source/manifest/review are in `docs/assets/portraits/006_independence_wave/` | Pass |
| Route flags/cosmetics | Four route ladders exist in `gfx/flags/`, `medium/`, and `small/`; route effects set `BSK_INDEPENDENCE_WAVE_CIVICX`, `AGRARIANX`, `SOCIALISTX`, and `EMERGENCYX` at `...bashkiria_package_effects.txt:164,177,196,215,234`, with `drop_cosmetic_tag` cleanup at line 443 | Pass |
| Constants/triggers/effects | `common/script_constants/006_independence_wave_bashkiria_constants.txt`, package triggers, and package effects provide ledgers, costs, lifecycle, setup, final validation, and generation guards | Pass |
| Ideas | Seven definitions exist in `common/ideas/006_independence_wave_bashkiria_ideas.txt:7-47`, with route and compact lifecycle consumers | Pass after lifecycle patch; see re-audit addendum below |
| Decisions/projects | `common/decisions/006_independence_wave_bashkiria_decisions.txt:15-570` contains the founding mission `independence_wave_bsk_hold_frontier_congress` plus the ten canonical serialized projects, costs, timeouts, cancellation, failure, and AI blocks | Pass |
| Shared focus hooks | Package effects expose the five BSK helper hooks and setup assigns the shared full framework (`...bashkiria_package_effects.txt:244-325,366-381`); no separate BSK tree is required by this carrier design | Pass, subject to shared-tree MCP diagnostics |
| Forces | Prepared setup requires `independence_wave_force_mapping_package_id = iw_045`, `mounted_mobile`, p45 tradition, five allowed reinforcement pathways, seven forbidden pathways, and no navy/air inheritance (`...bashkiria_package_triggers.txt:187-206`) | Pass |
| AI | `common/ai_strategy/006_independence_wave_bashkiria.txt` provides package/setup-gated army, production, infrastructure, bunker, and host-restraint layers | Source pass; no quantitative balance claim |
| Localisation | `localisation/english/006_independence_wave_bashkiria_l_english.yml` covers BSK names, four cosmetic ladders, parties, ideas, mission, ten projects, costs, and tooltips; canonical `bsk_congress_charter` keys are present | Pass |
| Cleanup | `...bashkiria_package_effects.txt:415-455` removes the mission/ten decisions, package ideas, portrait override, cosmetic tag, ledgers, flags, and package setup state | Pass |

## Central admission gate evidence

- The package dispatcher has an IW-045 adapter call for setup/final/cleanup (`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:37-78`), and the normal preflight has an exact dormant BSK/state-651 branch (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:300-306`). These prove only that the package adapter and identity proof exist.
- The separate content-attestation predicate is `has_independence_wave_runtime_package_content_attestation_for_execution_id` (`...package_dispatch_triggers.txt:159-201`). Its OR list ends without `iw_045`; the source comment at lines 44-46 explicitly says IW-045 remains absent from that allowlist.
- Normal preflight requires both adapter and content attestation (`...package_dispatch_triggers.txt:206-212`). Therefore the IW-045 normal branch cannot pass while the attestation list remains unchanged.
- Scenario preflight also begins with the same content-attestation requirement (`...package_dispatch_triggers.txt:410-412`). Its IW-045 dormant branch exists at lines 511-515, but it is unreachable without attestation.
- The deterministic Join probe iterates a fixed candidate order in `common/scripted_effects/006_independence_wave_join_effects.txt:210-245`; it contains `iw_044`, then `iw_033`, `iw_041`, and later IDs, but no `iw_045` entry. Join must remain closed.

## Mandatory MCP evidence and limitations

- `hoi4.map_inspect({stateIds:[651]})` returned `MAP_INSPECTED`, workspace `mod_chaos_redux_ea3b2d67c2c0`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2eac81b3ea870153528ba3842195f9f82e6edf6d5d9add2e1718c6079c288223/c9dc53134b77913cd1c2ba7d196f213e65ff4156817863db857b273bf6f8cb7f/map-inspect.cb427d91802129c8.json`. State/region/network checks passed, but global validation is false because unrelated workspace diagnostics report 1,323 `MAP_BUILDING_POSITION_INVALID` and 1,331 `MAP_PORT_ADJACENT_SEA_INVALID` errors in `mod:map/buildings.txt`; no BSK/state-651-specific error was exposed in the bounded result. `hoi4.map_render` produced the state artifact `map-state.png` with no blockers.
- `hoi4.focus_inspect` and `hoi4.focus_render` on `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, returned 184 focuses and 196 connectors. Current inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1521f7c88b6dd0eaf644e9e48c8a2c85fb9c04f634855fd460048313f73918ba/5d2867a30e4c9229213b4f1efafdb583b9096fbc8d7572a0b9d41616a6e1a292/focus-inspect.5c5a041f77ec68e1.json`. The earlier render artifact remains `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d77d09877e1b590360efa25ab41318842ab937b401e728e6f8b9999a2389bef/cde7f0abed0d936abd5e4db1df2dd7dbc0c257ef44e2e6ec53403501df21a431/independence_wave_focus_tree.focus.html`. Validation is false only for 14 shared-workspace missing continuous-focus icon references and layout warnings; no IW-045-specific missing focus surface was reported.
- `hoi4.event_inspect` and `hoi4.event_render` for `chaosx.nr6.350` used `selector.kind = event` and returned partial focused evidence with zero blocking diagnostics. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f45d027565568c1eed29cefcb9a688e617613629b43f6ae95ae11e66fb8cd9b/5814cd1334aed180a28defe92b053846e882dc94bd12c3f711f4dd3cad41c778/event-state_flow-d21fdfa2723e.json`. The viewer deferred large-workspace helper/lifecycle projections; no complete global event claim is made.
- Mandatory probability inspection found `ai_strategy_factor` has `discoveryReason = no_weighted_surfaces` for `common/ai_strategy/006_independence_wave_bashkiria.txt` (artifact `probability-inspect-38b83abe93f1.json`). `mission_ai_will_do` discovered 11 candidates but `poolComplete = false`, `availableCandidates = 0`, and 15 required inputs (artifact `probability-inspect-b7b031d727e0.json`). The decision adapter redirected to mission discovery. No numeric AI balance or ranking claim is justified without typed scenarios; no probability-bearing source patch was made.
- The installed MCP package exposes no Technology Tree Viewer. No technology/doctrine admission claim is made.

## Portrait archive preservation check

The IW-045 originals and metadata are flat under `docs/assets/portraits/006_independence_wave/` with names beginning `iw045_bsk_yakov_bykin...` or `metadata__iw045...`. BSK processed crops/master files are confined to `docs/assets/portraits/006_independence_wave/processed/`. A recursive check found no archive filename containing `156x210`. The runtime DDS remains only under `gfx/leaders/006_independence_wave/`; no portrait archive was moved or overwritten.

## Lifecycle re-audit addendum

The parent’s current package-local patch closes the only idea-lifecycle gap identified above. `independence_wave_bsk_focus_secure_oilfield_communities` now adds `bsk_oilfield_council` at `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt:264-273`; `independence_wave_remove_bsk_package_ideas` removes it at lines 12-21; and `independence_wave_remove_bsk_route_ideas` removes it at lines 25-31. The seven defined BSK ideas therefore have an explicit add/remove lifecycle, including cleanup and route transitions. This re-audit finds no remaining package-local idea-contract blocker.

The parent’s current static allocator/scenario receipts and fresh `chaosx.nr6.350` event inspect/render remain partial where the MCP workspace defers large projections but report zero blocking event diagnostics; the BSK strategy inspection still reports `no_weighted_surfaces`. Those receipts do not change admission status: the central content-attestation OR list still omits `iw_045`, both preflights still require that attestation, and deterministic Join still has no `iw_045` candidate. Typed mission scenarios remain the outstanding probability evidence limitation, so central attestation and Join must remain fail-closed.

## Recommendation and remaining work

Keep IW-045 absent from central content attestation, normal/scenario preflight admission, and deterministic Join. The `bsk_oilfield_council` lifecycle is now resolved and documented above. Before any future central promotion, preserve the source-placeholder/flag evidence, obtain typed probability scenarios (or record the adapter limitation without a balance claim), and run a fresh package attestation/preflight/Join review. No package-local gameplay or central registry files were changed in this audit.
