# Event 006 IW-013 NAV / IW-015 GLC country-package audit after source placeholders

Date: `2026-08-06`.

Scope: current-file audit of the vanilla `NAV` and `GLC` carriers after the source-placeholder portrait tranche and ordinary super-event normalization. The review covers tag registration, setup and map anchors, politics, leaders and command roster, portraits and flags, forces, technology and production references, ideas, decisions and missions, AI, diplomacy and former-host hooks, regional and formable hooks, shared focus admission, cleanup, and central dispatch. No gameplay file was changed in this audit.

Verdict: **SOURCE-WIRED / HOLD / FAIL-CLOSED**.

The package adapters are present and internally cross-referenced, but the source-placeholder portraits are not final HOI4-style replacements, the proposed portrait subjects are not wired to the current ruling-leader consumers, command-roster readiness only proves a country leader, and central runtime content attestation still excludes execution IDs `iw_013` and `iw_015`. These gates must remain closed.

## Country package coverage checklist

| Surface | IW-013 NAV | IW-015 GLC | Current result |
| --- | --- | --- | --- |
| Tag and package identity | `original_tag = NAV`, package `constant:independence_wave_package_id.iw_013` | `original_tag = GLC`, package `constant:independence_wave_package_id.iw_015` | PASS source crosswalk |
| Setup archetype and region | Mediterranean-Iberia, regional depth, industrial-breakaway | Mediterranean-Iberia, standard depth, agrarian-regional | PASS source crosswalk |
| Anchor and capital | State `792` for both anchor and capital | State `171` for both anchor and capital | PASS package contract; map evidence has unrelated global diagnostics |
| Former host and ownership | Living former host, liberated state owned and controlled by carrier | Same | PASS guarded source predicates |
| Leader identity gate | `Ramón Ormazábal Tife` | `Fuco Gómez` | PASS current vanilla carrier predicate |
| Command roster | Country-leader check only | Country-leader check only | PARTIAL; no army commander proof |
| Focus admission | Shared `independence_wave_focus_tree` full framework | Shared `independence_wave_focus_tree` full framework | PASS source contract; shared-tree MCP warnings remain |
| Decisions and founding mission | Local category, crisis mission, eleven serialized projects, route, host, Network, sovereignty | Same | PASS source wiring |
| Ideas and ledgers | Contested/mature pair and five route ideas; two compact ledgers | Same | PASS source wiring |
| Forces, technology, industry | `mountain_frontier` profile `p13 = 709`; no package-local navy/air inheritance | `territorial_defense` profile `p15 = 1047`; no package-local navy/air inheritance | PASS source references; no new technology surface |
| AI | Mountain survival, host restraint, settled industry, emergency command | Territorial survival, host restraint, settled port, emergency command | PASS source references; named-scenario probability evidence remains outside this bounded handoff |
| Portraits and flags | Aguirre source placeholder exists, no gameplay consumer changed | Castelao source placeholder exists, no gameplay consumer changed | HOLD; replacement, identity, rights, and wiring review open |
| Runtime attestation | Adapter registered, content attestation absent | Adapter registered, content attestation absent | BLOCKED by design |

## File surface checklist

Current package source surfaces reviewed:

- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt` lines 9-18, 21-57, 59-66, 131-252.
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` lines 418-520 and 522-600.
- `common/script_constants/006_independence_wave_iberian_constants.txt` lines 10-122.
- `common/ideas/006_independence_wave_iberian_ideas.txt` lines 16-120.
- `common/decisions/006_independence_wave_iberian_decisions.txt` lines 1-397.
- `common/ai_strategy/006_independence_wave_iberian.txt` lines 1-93.
- `common/national_focus/006_independence_wave_focus.txt`, shared tree `independence_wave_focus_tree`.
- `common/scripted_effects/006_independence_wave_focus_effects.txt` and `common/scripted_triggers/006_independence_wave_focus_triggers.txt` for full-framework loading and generic contract.
- `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt` and `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt` for reservation and package loading.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` for adapter and attestation gates.
- `localisation/english/006_independence_wave_iberian_l_english.yml` for category, project, party, idea, and tooltip coverage.
- `interface/006_independence_wave_iberian_portraits.gfx` and the two runtime DDS files under `gfx/leaders/006_independence_wave/`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_iberian_portrait_source_placeholder_2026-08-05.md` for source-placeholder provenance and replacement state.
- Vanilla precedents `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/NAV - Navarra.txt` and `GLC - Galicia.txt`.

No custom country-definition file exists for `NAV` or `GLC`; both are intentional vanilla carriers. Existing dirty-worktree edits belong to the parent or other scoped agents and were not reverted.

## Missing or stale country-package surfaces

The dispatch adapter trigger includes `iw_013` and `iw_015` in `has_independence_wave_runtime_package_adapter_for_execution_id` at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:42-43`.

The content-attestation trigger at the same file, lines 88-119, does not include either execution ID. The preflight therefore remains false for both carriers even though their adapter branches and scenario tag proofs exist at lines 243-248 and 370-375.

The package-local exact-runtime predicates are deliberately not content attestations. `is_independence_wave_exact_package_iw_013_runtime_ready` and `_iw_015_runtime_ready` only compose setup and lifecycle state at lines 244-252; they must not be used to bypass central admission.

The FORM-07 identity/member/flag gate remains separate and fail-closed. No stale old four-digit ordinary super-event identifier was found in the current Event 006 package surfaces; the active ordinary super-event consumers remain `chaosx.nr23` and `chaosx.nr24` in `events/023_soviet_nukes.txt` and `events/024_hearts_of_iron.txt`.

## Map and state setup issues

`NAV` state `792` is the package anchor and capital. The vanilla state is SPR-owned with a NAV core, port, airbase, one arms factory, and one civilian factory, matching the package contract. Region-02 reservation also permits the documented optional states `172` and `806`.

`GLC` state `171` is the package anchor and capital. The vanilla state is SPR-owned with a GLC core, port, airbase, one arms factory, and two dockyards, matching the package contract.

The current package triggers require the anchor state to be owned and controlled by the carrier and require the former-host liberated state to be owned by the carrier. The source does not silently transfer an anchor, so an occupied or conflicting state fails initialization.

The prior bounded map inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56cdd14e21f9ac1bf86f60e1c6fa898ae396f74ac2414b483735e90c08fe1f84/4e6136fbe334a509ec59ed0471d02ad55ad2f653a46fd8096bcca95f3ec18b64/map-inspect.2c1cde840ea0e249.json`. It confirmed the relevant state membership and network anchors but reported unrelated invalid building positions and floating-harbor diagnostics in global map data. No map rewrite is justified in this country-local scope.

## Politics, leaders, portraits, flags, advisors, and parties

The package setup effects at `006_independence_wave_iberian_package_effects.txt:418-502` set democratic provisional politics, apply authored starting popularity, and initialize all twenty-four short/long institutional party keys before route selection. The authored start profiles are NAV `44/29/22/5` and GLC `48/25/22/5` for democratic, communist, neutrality, and fascist popularity and each sums to 100.

The setup predicates require vanilla `Ramón Ormazábal Tife` for NAV and `Fuco Gómez` for GLC at `006_independence_wave_iberian_package_triggers.txt:21-57`. The command-roster helpers at lines 59-66 repeat only the country-leader check. They do not create, identify, or attest an army commander. This remains a roster/source risk and a blocker for any claim that the package has a complete command staff.

The placeholder tranche added stable sprite names `GFX_portrait_NAV_jose_antonio_aguirre` and `GFX_portrait_GLC_alfonso_daniel_castelao` in `interface/006_independence_wave_iberian_portraits.gfx`, plus runtime DDS files at `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds` and `portrait_GLC_alfonso_daniel_castelao.dds`.

Those textures are exact source-crop placeholders with `source_placeholder` and `replacement_pending` status, not final HOI4-style replacements. No `common/characters`, country history, or current leader consumer was changed. Vanilla GLC already has Castelao as a non-primary roster entry, while current package setup still requires Fuco Gómez; vanilla NAV has no Aguirre consumer. Wiring either proposed subject to a ruling or additive role requires a separate identity and roster decision.

The Aguirre source carries a Commons CC BY-SA 3.0/4.0 metadata discrepancy. The Castelao scan is marked public domain/PD-old but has an unknown original author and scan-chain caveat. Both require independent rights and identity review before promotion.

Vanilla NAV/GLC flags remain the carrier flags. No replacement flag was added or promoted, and no independent flag provenance review is complete. No advisor icon or advisor consumer was added.

## Focus, decision, idea, and asset issues

Both setup effects call `independence_wave_assign_focus_framework`, which loads the shared `independence_wave_focus_tree` and marks the full generic contract. No country-specific focus tree is missing from the current adapter design.

Fresh read-only `hoi4.focus_inspect` used workspace `mod_chaos_redux_ea3b2d67c2c0` and produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b66f915c70daba96cad7779bd850e3f4c1514f1b27827902498c16d5e1cc97f4/2ec0a22abe9984f05c305f5d99bf8a81242d35ffa24ea1770303cf2c68221e38/focus-inspect.20b8e3a8ecb68ee7.json`. It recognized 184 focuses and 193 connectors with zero crossings, zero node intersections, one long connector, and five tree-local layout diagnostics. The same inspection reported 14 global missing continuous-focus icon references inherited from the installed generic palette.

Fresh read-only `hoi4.focus_render` produced HTML, SVG, JSON, source-map, and plan artifacts under `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/573f3f22303bfbda7edb38e13a803993cbf0b9d7a47aa9dbef0d975e6e0eccda/`. The render is evidence of the shared framework only and does not justify a country-local focus rewrite.

The two local decision categories, founding missions, route projects, former-host work, Network actions, sovereignty action, cost text, AI blocks, and cleanup lists are present. The separate decision audit already corrected ten dead government-route predicates and prevented founding-mission rearming after terminal success/failure. Four package duration constants remain unused and the local compact crisis is intentionally outside the shared global founding-mission concurrency list; neither is patched here because each is a broader balance or cross-package policy decision.

The ideas file provides one contested idea, one mature idea, and five mutually exclusive route ideas per carrier. All fourteen idea names and descriptions resolve in the Iberian localisation file and reuse existing Event 006 icon families.

## Starting military, technology, industry, supply, and production

The force mapping table maps IW-013 to `mountain_frontier`, profile `p13 = 709`, and IW-015 to `territorial_defense`, profile `p15 = 1047`. The source mapping includes role masks, terrain/tradition inputs, depots or militia roles, stockpiles, technology grants, and research-slot adjustments through the shared force loader.

The package intentionally does not inherit a package-specific navy or air force. No missing technology, production-line, convoy, train, fuel, supply-capacity, or resource identifier was found in the reviewed package source. The force loader still creates formations without army commanders, which is the same unresolved roster limitation.

No technology tree was edited. The installed package exposes no Technology Tree Viewer, so no viewer artifact exists; this is an unresolved tooling limitation rather than a technology-pass claim.

## AI, diplomacy, host, regional, and formable hooks

`common/ai_strategy/006_independence_wave_iberian.txt` contains separate guarded NAV and GLC profiles. Each profile is restricted by original tag, active package/setup/profile flags, and abort conditions. The profiles prioritize survival, production or port/industry repair, host restraint, and emergency command while avoiding unrelated wars.

The package loaders register the former-host route, regional ambition family, League route, host settlement, Network membership, and the `iberian_federation` formable family. Route, host, Network, and formable checks are tied to the package ID, anchor ownership, living former host, and stable-ledger requirements.

No package-local AI or random-selection source was changed. The bounded MCP probability adapter-list call completed with `PROBABILITY_ADAPTERS_LISTED`, but no named world-state scenario was supplied and no probability comparison is claimed here. A named-scenario AI/probability pass remains parent-owned before any weighted balance or attestation decision.

## Cleanup and lifecycle

`independence_wave_cleanup_iw_013_basque` and `independence_wave_cleanup_iw_015_galicia` remove the local mission and eleven decisions, remove local ideas, clear lifecycle/setup/ledger/project variables, clear route/host/Network/formable progress flags, and clear the compact-crisis terminal flags. The dispatch cleanup calls both carrier helpers at lines 599-600.

The cleanup source does not create a global event target and does not use a world iteration. It preserves the vanilla carrier tag and leader history rather than attempting to delete or replace the carrier.

## Validation evidence and skipped checks

- Offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, ideas, AI, country creation, focus modding, character/portrait modding, and state modding were consulted.
- Vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` was consulted for effects, triggers, modifiers, script concepts, localisation formatting, and dynamic variables.
- Current static crosswalks found no missing Iberian party, idea, decision, project, focus-contract, AI-profile, force-profile, or constant identifiers.
- Fresh Event Chain Viewer lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/89f46f6286af86f23bd0c8b15d9f6d804bf736ae70b5d3a5f7ca325de3f74a60/393fbfac6ae22576949f4bb98c21a4ea8f48160ac857345d808b38421e655a0b/event-lint-04e76dcf50ae.json`. The large-workspace helper/lifecycle projection was deferred by MCP.
- Fresh shared-focus inspection and rendering were read-only and produced the artifacts recorded above.
- No live game, save, runtime consumer test, final provider portrait operation, independent rights/style review, or final flag audit was run. These are user/parent-owned acceptance gates.

## Findings requiring parent action

1. Keep `has_independence_wave_runtime_package_content_attestation_for_execution_id` closed for `iw_013` and `iw_015` until the final portrait replacement, leader/roster consumer decision, flag provenance review, and independent country-package audit are complete.
2. Decide whether Aguirre and Castelao are additive non-ruling consumers or replacements for current leaders. Do not infer this from the source placeholders; current setup predicates intentionally remain Ormazábal and Fuco.
3. Add or attest army commanders only in a separately scoped roster/source pass if the package design requires command-roster completeness. Do not mark the current country-leader-only helper as a complete command roster.
4. Preserve the separate FORM-07 identity, member, flag, territory, and attestation gates. Do not use the exact package runtime predicates as a substitute for central attestation.

## Simplifications, omissions, and blockers

No gameplay patch, identity redesign, focus rewrite, map rewrite, advisor icon, flag replacement, leader replacement, or central attestation promotion was made.

The runtime portrait DDS files are source placeholders only and remain replacement-pending. The shared focus tree retains one long connector, five tree-local layout warnings, and fourteen unrelated generic continuous-icon diagnostics. The map inspector retains unrelated global map diagnostics. Technology Tree Viewer evidence is unavailable in the installed package. Named-scenario AI probability evaluation, live gameplay, final portrait/style/rights review, and final flag review remain unresolved.

## Skills used

`chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-comfyui` guided this audit boundary and handoff.
