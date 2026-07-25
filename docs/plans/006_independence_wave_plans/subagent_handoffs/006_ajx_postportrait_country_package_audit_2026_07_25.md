# IW-010 Saar (`AJX`) post-portrait country-package audit

Audit date: 2026-07-25.

Scope: independent country-package audit after promotion of the sourced Walter Simons civic portrait and sourced Friedrich von Rabenau commander portrait.

## Decision

**Static country-package decision: PASS.** The tag, dormant setup, state binding, politics, roster, portrait consumers, flag, localisation, ideas, focus assignment, decisions, force mapping, AI, FORM-04 hooks, host/patron/network/league surfaces, cleanup, and Event-005 collision protections are present and internally coherent.

**Runtime admission: CLOSED.** `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` does not include `constant:independence_wave_package_id.iw_010` in `has_independence_wave_runtime_package_content_attestation_for_execution_id` (the exact list currently ends at `iw_184`). The automatic wrapper, SCN-008 preflight branch, capacity witness, and region-one planner branch are registered, but the central attestation gate correctly prevents execution until the parent promotes this exact package ID.

**Compile-time admission recommendation: JUSTIFIED after parent review.** The complete static package and both sourced full-size portrait consumers now have independent PASS evidence, so adding one exact `iw_010` branch to the central attestation list is supported by the available evidence. This subagent did not make that central runtime edit and does not claim live execution or allocator proof.

No Hearts of Iron IV process was launched. No map mutation was attempted.

## Required references consulted

- `AGENTS.md`.
- `.agents/skills/chaos-redux-subagents/SKILL.md`.
- `.agents/skills/chaos-redux-events/SKILL.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- `.agents/skills/hoi4-focus-trees/SKILL.md`.
- `.agents/skills/hoi4-decisions-missions/SKILL.md`.
- Offline wiki pages in `paradox_wiki/` for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, country creation, national focuses, state, character, portrait, graphical assets, technology, division, and unit syntax.
- Vanilla documentation in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including effects, triggers, script concepts, modifiers, dynamic variables, decisions, focuses, characters, and AI references.

## Country package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Candidate identity and registry | PASS | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` row `IW-010`; resolved tag `AJX`; Level 1; anchor state `42`; reservation group `RG-RHINE-SAAR`; automatic disposition `automatic_pool_ready_if_unique_state_exists`. |
| Research boundary | PASS | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` row `IW-010`; unique current-map state and surviving former host are required; sourced interwar symbols and real-person roles are required. |
| Tag registration | PASS | `common/country_tags/006_independence_wave_countries.txt:18` maps `AJX` to `countries/006_independence_wave_AJX.txt`. |
| Country definition | PASS | `common/countries/006_independence_wave_AJX.txt` provides the western-European graphical cultures and Saar colour. |
| Dormant history | PASS | `history/countries/AJX - Saar.txt` is dormant at game start, sets civilian economy/export focus/volunteer-only, and recruits the complete AJX roster through setup. |
| Setup and validation | PASS | `common/scripted_triggers/006_independence_wave_saar_package_triggers.txt` and `common/scripted_effects/006_independence_wave_saar_package_effects.txt` enforce exact package, host, anchor, roster, route, formable, force, lifecycle, and completion flags. |
| Final setup and cleanup | PASS | `independence_wave_setup_iw_010_saar`, `independence_wave_validate_iw_010_saar`, and `independence_wave_cleanup_iw_010_saar` are wired, with package ideas, mission, decisions, variables, and all AJX flags removed during cleanup. |
| State and host contract | PASS | State `42` (`Moselland`) is the fixed compact anchor; former host is dynamic; the host must retain a protected state and may not equal AJX. |
| Politics and routes | PASS | Constitutional, labour, patron-client, and neutral-commission routes are initialized by the AJX effects; traditional, emergency-military, and radical-sovereignty routes are explicitly excluded for this package. |
| Characters and leadership | PASS | `common/characters/006_independence_wave_saar_characters.txt` defines `AJX_friedrich_hoffmann` as the male civilian leader consumer and `AJX_karl_becker` as the male corps commander, plus three male advisor offices. No commander is promoted as a country leader. |
| Portrait provenance and runtime | PASS | Both promoted sourced portraits have independent audit handoffs, exact crop evidence, deterministic `156x210` candidates, package/runtime DDS byte equality, and stable existing consumers. See the portrait evidence section below. |
| Flags and visual assets | PASS | `gfx/flags/AJX.tga`, `gfx/flags/medium/AJX.tga`, `gfx/flags/small/AJX.tga`, the neutral-commission focus icon, and the asset manifest are present and documented. |
| Localisation | PASS | `localisation/english/006_independence_wave_saar_l_english.yml` covers promoted leader names, party names, advisors, ideas, category, mission, decisions, focuses, tooltips, and descriptions; `006_independence_wave_countries_l_english.yml` covers `AJX`, `_DEF`, `_ADJ`, and ideology variants. |
| Ideas and lifecycle | PASS | `common/ideas/006_independence_wave_saar_ideas.txt` contains exposed/balanced lifecycle and route ideas scoped to `AJX`. Setup initializes continuity and neutrality values and the 480-day founding mission. |
| Focus assignment and tree | PASS | `independence_wave_focus_tree` is assigned by `independence_wave_assign_focus_framework`; AJX has the neutral commission route and six package nodes with prerequisites, rewards, icons, and localisation. |
| Decisions and mission | PASS | `common/decisions/006_independence_wave_saar_decisions.txt` contains the founding mission and twelve AJX decisions with costs, serialization, cancellation, AI weights, trigger tooltips, and effect localisation. |
| Starting force and equipment | PASS | P10 `industrial_security` mapping, tradition `50`, reinforcement mask `1349`, dynamic starting-force application, technology/slot inheritance, and no navy/air inheritance are wired. |
| AI and playability | PASS | `common/ai_strategy/006_independence_wave_saar.txt` uses exact origin/setup/profile checks, dynamic former-host threat, industrial survival, founding restraint, and route-specific policy weights without a static host assumption. |
| Formable and diplomacy | PASS | FORM-04 Rhenish Federation eligibility includes AJX state `42`, living RHI partner state `51`, connected capitals, undominated corridor, consent, integration, autonomous-member, rollback, and cleanup adapters. |
| Host/patron/network/league | PASS | AJX setup registers all four host routes, patron/client route, network/coal transit route, Rhenish league ambition, host-account decisions, and the Rhine family selection. |
| Event-005 collision safety | PASS | Event-005-first frozen metadata and Event-006 capacity checks protect AJX, state `42`, and the dynamic host; `RG-RHINE-SAAR` permits at most one automatic claimant per frozen wave. |
| Runtime dispatch boundary | BLOCKED BY INTENT | Exact adapter/preflight/scenario branches and automatic wrapper exist, but central compile-time content attestation excludes `iw_010`. Parent review is required before admission. |

## File surface checklist

| File or surface | Identifier(s) | Finding |
| --- | --- | --- |
| `common/country_tags/006_independence_wave_countries.txt` | `AJX` | Registered correctly. |
| `common/countries/006_independence_wave_AJX.txt` | `AJX` | Definition and graphical cultures present. |
| `history/countries/AJX - Saar.txt` | `AJX` | Dormant history and starting ideas are coherent. |
| `common/characters/006_independence_wave_saar_characters.txt` | `AJX_friedrich_hoffmann`, `AJX_karl_becker`, three advisor IDs | Male metadata matches male portrait/name roles; advisor offices intentionally have no custom portrait handles. |
| `interface/006_independence_wave_region_01_portraits.gfx` | `GFX_portrait_AJX_friedrich_hoffmann`, `GFX_portrait_AJX_karl_becker` | Existing stable sprites already target the promoted runtime DDS paths; no duplicate `.gfx` registration is needed. |
| `common/scripted_triggers/006_independence_wave_saar_package_triggers.txt` | AJX package/setup/roster/complete triggers | Exact tag, state, host, roster, route, force, formable, lifecycle, and cleanup preconditions pass inspection. |
| `common/scripted_effects/006_independence_wave_saar_package_effects.txt` | `independence_wave_setup_iw_010_saar`, `independence_wave_cleanup_iw_010_saar` | Setup recruits the three offices, initializes politics and force, and cleanup removes all package state. |
| `events/006_independence_wave.txt` | `chaosx.nr6.10` | Hidden setup event recruits the three AJX advisors only under the exact AJX package trigger. |
| `common/ideas/006_independence_wave_saar_ideas.txt` | AJX ideas | Lifecycle and route idea lifecycle is complete. |
| `common/national_focus/006_independence_wave_focus.txt` | `independence_wave_focus_tree`, AJX focus IDs | Neutral-commission root and six AJX package nodes are present with route locks and rewards. |
| `common/decisions/006_independence_wave_saar_decisions.txt` | AJX mission plus twelve decisions | Costs, project serialization, cancellation, AI weights, trigger tooltips, and cleanup coverage are present. |
| `common/ai_strategy/006_independence_wave_saar.txt` | Four AJX strategy blocks | Origin-gated dynamic-host AI is present and does not hardcode GER. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | `iw_010` adapter/preflight/scenario branches | Adapter and preflight are registered; exact content attestation omits `iw_010`. |
| `common/scripted_triggers/006_independence_wave_triggers.txt` | `is_independence_wave_runtime_automatic_package_iw_010_ready`, `independence_wave_liberations_capacity_try_iw_010` | Automatic readiness and Event-005-aware capacity witness are registered. |
| `common/script_constants/006_independence_wave_package_constants.txt` | `iw_010 = 10` | Package ID constant is present. |
| `common/script_constants/006_independence_wave_force_package_constants.txt` | P10 profile/tradition/mask | P10 maps to industrial security, tradition 50, mask 1349. |
| `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt` | `is_independence_wave_form04_eligible_member`, connected-capital gates | AJX state-42 membership and RHI/AJX corridor requirements are explicit. |
| `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt` | FORM-04 transfer/autonomous/cleanup adapters | AJX state 42 is transferred only after strict consent and commit proof; no fallback annexation is used. |
| `005_006` collision triggers/effects | Event-005 frozen footprint and host reservation | Event-005-first ordering and same-wave state/host protection are present. |
| `localisation/english/006_independence_wave_saar_l_english.yml` | AJX player-facing keys | Promoted names and package text are localized. |
| `gfx/flags/AJX.tga`, `medium/AJX.tga`, `small/AJX.tga` | AJX flag family | Historical Saar flag family is present and manifest-hashed. |

## Portrait provenance and runtime evidence

### Walter Simons civic consumer

- Stable internal token: `AJX_friedrich_hoffmann`.
- Stable sprite: `GFX_portrait_AJX_friedrich_hoffmann`.
- Runtime path: `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds`.
- Role: full-size civilian country leader only; male metadata and male name are aligned.
- Source: Bundesarchiv Bild 102-12279, September 1931, CC-BY-SA 3.0.
- Master SHA-256: `789961BC6505993F4A6441979CA4D1F247609531D23CFB8D7088CCC2D4A170B3`.
- Exact crop SHA-256: `2B1C394DA30F31F0E81B35CD6740CC0E0235A71326FDC976CCE9F0217688EFD7`.
- Processed `156x210` PNG SHA-256: `A7DE632090AD42ECDAD19583A7B76DE3B3231E75D597E1EFED06486A801A9E04`.
- Package/runtime DDS SHA-256: `07EFF6959101BED7629F722276DBD46EC6D91D3E5E58F5D3462057C131BED426`.
- Audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_saar_walter_simons_trial01_independent_portrait_audit_2026_07_25.md` reports PASS and `approved_for_parent_promotion`.

### Friedrich von Rabenau commander consumer

- Stable internal token: `AJX_karl_becker`.
- Stable sprite: `GFX_portrait_AJX_karl_becker`.
- Runtime path: `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds`.
- Role: full-size army commander with existing `civilian.large` and `army.large` consumers; male metadata and male name are aligned.
- Source: Bundesarchiv Bild 183-C05190, 13 April 1937, Dorneth/Scherl, CC BY-SA 3.0 DE.
- Master SHA-256: `F6B51E6B3A39E35734D67FA4DB4081C6DA26AEB40084569FF6747CD9ACA0480B`.
- Exact crop SHA-256: `B153E0310340D1EC5ED02484A52049C5D018767FEC6C5C525BA237B5803161E1`.
- Processed `156x210` PNG SHA-256: `FEC2653228598C9E5A9F18292ECAA07528469AA9477DCB2FFF800F73E6E55627`.
- Package/runtime DDS SHA-256: `6595D33FC6A08B840EB51DEBE3E05BDE56BDAD38009CB22EEF0019720A1EABFD`.
- Audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_saar_rabenau_trial01_independent_portrait_audit_2026_07_25.md` reports PASS and `approved_for_parent_promotion`.

Both portrait manifests explicitly forbid advisor, dossier, operative, commander-small, `_small`, female, generic, and fallback derivatives.

The role boundary is deliberate: Simons is an alternate-history constitutional civic figure with no claim that he chaired an independent Saar commission, while von Rabenau is an alternate-history German corps-command figure with no claim of a historical Saarbrücken or industrial-security posting.

## Map and state setup

The accepted current-map binding is state `42`, localized as `Moselland`, with `GER` as the vanilla owner in the 1936 map and a protected host-survival requirement.

`docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` records `IW-010`, `AJX`, anchor `42`, compact `42`, former host `GER`, and `automatic_pool_ready_if_unique_state_exists`.

`docs/plans/006_independence_wave_plans/package_bindings/006_current_map_state_collisions.csv` records state `42` as a shared `IW-008` extension and `IW-010` anchor/compact claim in `RG-RHINE-SAAR`, resolved by a maximum-one-automatic-package-per-wave rule.

The runtime package trigger requires a unique anchor owner/controller, dynamic former host, host survival, capital state `42`, and state/event-target coherence before setup mutates the country.

No map write was made, and no state history override is required for this package.

## Politics, leader, advisor, party, and diplomacy issues

The setup effect initializes democratic/election state and route-specific party names, then promotes `AJX_friedrich_hoffmann` under the constitutional, labour, patron, or neutral-commission ideology selected by the route.

All four route installers preserve the same stable civilian leader token and never promote `AJX_karl_becker` as a country leader.

The mine/rail dispatch superintendent, cross-border accounts comptroller, and factory-security inspector are separate advisor offices with localized names and descriptions and intentionally no custom portrait blocks.

The AJX party names, long names, adjectives, route descriptions, and ideology variants are localized, and no stale fictional player-facing leader names remain in current package localisation.

The host relationship is dynamic through saved former-host targets, and patron influence, network membership, host ledgers, and Rhenish league actions have explicit setup and cleanup flags.

## Focus, decision, idea, and asset issues

The full shared `independence_wave_focus_tree` is assigned during package setup.

AJX's bespoke focus surface contains the neutral-commission root and the package branch `keep_mines_breathing`, `charter_coal_rail_authority`, `screen_industrial_security_companies`, `open_cross_border_trade_desk`, `settle_saar_accounts`, and `send_rhenish_league_delegation`, with prerequisites, route locks, effects, icons, tooltips, and localisation.

The AJX decision category contains the founding mission plus twelve serialized projects covering mine/rail administration, factory security, trade, host ledgers, government routes, durable independence, patron balancing, and Rhenish league work.

The exposed/balanced lifecycle ideas and route ideas are scoped to `AJX`, have an explicit cleanup path, and are represented in localisation.

The Saar flag family and neutral-commission focus icon are present; no Event 006 custom advisor cards or portrait derivatives are authorized.

## Starting military, technology, industry, supply, and production

P10 uses `industrial_security`, tradition `50`, and reinforcement mask `1349`.

Mask `1349` resolves to the five intended paths: `integrate_militias`, `secure_depots`, `factory_rail_guards`, `foreign_arms`, and `capital_border_defense`.

The dynamic force effect validates the roster and setup event targets, loads the mapping, inherits applicable technology/research slots, generates the industrial-security infantry/support template, creates the bounded opening force, and marks the package applied.

The P10 inheritance mask is zero for navy/air inheritance, so no unsupported navy or air opening is silently created.

The dormant history's civilian economy, export focus, volunteer-only law, state-42 industrial facilities, and dynamic equipment/force setup provide the intended small industrial anchor without an unrelated balance expansion.

## AI and playability

The AI blocks are exact-origin and setup gated, use the package's dynamic former host, and prefer industrial survival, equipment production, infantry/support/artillery, infrastructure, and arms factories.

Founding-restraint and civic/patron industrial policies discourage opportunistic wars while the host threat remains non-severe, and route-specific policies do not assume a fixed GER host.

The package can pursue constitutional, labour, patron-client, or neutral-commission routes and can reach FORM-04 only through the explicit RHI/AJX connected-capital and consent contract.

## Event-005 collision and allocator/runtime boundary

`independence_wave_liberations_capacity_try_iw_010` checks the exact AJX tag, state-42 anchor, dynamic host, Event-005 country/anchor/host clearance, selected arrays, chaos-band threshold, and `RG-RHINE-SAAR` reservation before adding the package to a wave.

The shared Event-005/Event-006 transaction freezes Event-005 first, trims or rejects overlapping Event-006 claims, preserves host survival, and rolls back rejected reservations without leaving stale package state.

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` has an adapter branch at the AJX exact tag and scenario branch for `iw_010`, but the compile-time content-attestation OR block omits `iw_010`.

This omission is the only current package-level admission blocker found after the sourced portrait promotion.

## Missing or stale surfaces

1. **Central runtime attestation is intentionally not promoted in this handoff.** The parent should review this file and add the exact `iw_010` branch to `has_independence_wave_runtime_package_content_attestation_for_execution_id` if the parent accepts the compile-time recommendation.
2. **No live execution evidence exists.** The exact wrapper and capacity witness are statically present, but this audit did not launch HOI4 or execute SCN-008/allocator runtime.
3. **Superseded historical asset notes remain in the repository.** Rejected 2026-07-22 Schmelcher trial notes and 2026-07-24 pre-promotion two-role clearance notes are retained as provenance history and are not player-facing runtime authority. The current 2026-07-25 portrait manifests and independent audit handoffs supersede them.
4. **No gameplay omission was found.** The remaining closure is the deliberate exact-attestation gate, not a fallback package or a missing country mechanic.

## Changes made by this audit

- Updated `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` so IW-010 records the passing post-portrait package audit while remaining outside exact runtime attestation.
- Updated `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` with the same runtime-closure and parent-review rule.
- Updated `docs/events/006_independence_wave/northern_western_europe_packages.md` so the portrait authority, asset section, and readiness paragraph no longer claim unresolved portraits or active runtime attestation.
- Updated `docs/assets/006_independence_wave/manifest.md` to distinguish passing static portrait/package evidence from the still-closed runtime gate.
- Added this audit handoff.

No gameplay, map, portrait, `.gfx`, localisation, focus, decision, AI, or runtime attestation file was changed by this audit.

## Meaningful validation

- Read-only source inspection covered the complete AJX package files, current Event-005/Event-006 collision contracts, current-map bindings, FORM-04 adapters, focus and decision surfaces, AI strategy, localisation, flags, characters, ideas, force constants, and central dispatch gate.
- A read-only DDS parser checked both promoted package/runtime files as legacy uncompressed BGRA textures with exact `156x210` dimensions, opaque alpha, valid headers, exact package/runtime byte equality, and decoded-pixel equality with the corresponding approved PNG.
- The independent portrait source/crop SHA-256 values in both promoted manifests were rechecked against their archived source evidence.
- A repository search found no current player-facing AJX localisation using the retired fictional display names; stable internal tokens remain intentionally unchanged.
- No in-game validation was run because AGENTS.md assigns live consumer testing to the user and forbids this agent from launching Hearts of Iron IV.

## Simplifications, omissions, and blockers

No gameplay simplification or fallback was introduced.

The only blocker is the deliberate central compile-time runtime-attestation omission for `iw_010`; the static package and portrait evidence support promotion, but live allocator and in-game behavior remain unproved until the parent makes that exact admission edit and performs its own final review.

The two sourced roles retain their documented alternate-history office boundaries and do not assert unsupported historical Saar postings.

## Parent handoff

Review this handoff, then either promote `iw_010` in the central attestation OR block and perform the parent-owned final dispatch review, or leave the package fail-closed with this static PASS as the recorded readiness state.
