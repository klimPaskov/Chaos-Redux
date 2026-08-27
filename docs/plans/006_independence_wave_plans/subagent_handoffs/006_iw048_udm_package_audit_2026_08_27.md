# IW-048 UDM package audit

Date: 2026-08-27.

Auditor: bounded country-package audit subagent.

Status: HOLD / fail-closed. IW-048 remains package-local and must not be promoted to central Event 006 admission, and no gameplay, map, asset, registry, or central files were changed by this audit.

## Accepted package contract

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:49` identifies IW-048 as Udmurtia, registered tag `UDM`, reservation group `RG-399`, anchor state `399` (Izhevsk), Layer B, and a compact industrial-forest republic.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:49` requires a dormant registered-tag release, state-399 anchor, former-host retention, sourced real male period leader or authentic institution, and explicit final asset provenance.
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:34` reserves state 399 only when the tag is not living and the host remnant test succeeds, with the host protected first.
- `docs/events/006_independence_wave/udmurtia_package.md:3-41` correctly describes a package-local implementation and explicitly withholds central admission, identity clearance, and fallback assets.

## Country package coverage checklist

- Identity and tag: covered only by the vanilla `UDM` carrier; no Chaos Redux country tag, country definition, history override, character override, or flag override exists.
- Anchor and state: package references state 399 and capital 399 consistently, but dynamic host retention and installed-map proof remain unresolved.
- Politics and parties: covered by package-local baseline and four route governments in `common/scripted_effects/006_independence_wave_udm_package_effects.txt:137-216`, with matching keys in `localisation/english/006_independence_wave_udm_l_english.yml:60-67`.
- Leader and roster: package references vanilla `UDM_boris`, but `has_independence_wave_udm_command_roster` requires the parent-owned `independence_wave_iw_048_identity_rights_cleared` flag in `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:90-95`.
- Portrait and rights: blocked because vanilla `UDM_boris` resolves to the existing `GFX_portrait_Boris_Berman` token while the installed token uses a generic Europe portrait texture; no rights-cleared period image or approved institution portrait is present.
- Flags: the vanilla normal, medium, and small ideology ladder is present and reused; no alternate IW-048 flag is proven or wired.
- Advisors and command: no IW-048-specific advisor, high-command, commander, or additional character roster is claimed; the package remains dependent on the unresolved vanilla leader identity.
- Forces and equipment: package-local mapping uses force profile `industrial_security`, profile p48, tradition 54, five reinforcement pathways, and no navy or air inheritance; the separate archetype contract is unresolved.
- Ideas and lifecycle: seven UDM ideas are defined and cleaned up generation-safely.
- Decisions and mission: one 420-day founding mission and ten timed projects are defined and localised.
- Focus callbacks: five guarded callbacks use the shared Event 006 focus tree; no dedicated UDM focus tree is claimed.
- AI: four UDM strategy blocks are present, but current typed probability evidence is unavailable.
- Network and formables: package completion checks shared network arrays; existing formable membership checks reference UDM outside the package, while IW-048 itself registers no formable family.
- Setup, validation, cleanup: package-local setup, final validation, dispatch helpers, and generation-safe cleanup exist, but central adapter, attestation, preflight, scenario, and deterministic Join ownership is intentionally absent.

## File surface checklist

- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:9-202` covers origin, tag, state, host, costs, roster, routes, force mapping, setup, readiness, and cleanup gates.
- `common/scripted_effects/006_independence_wave_udm_package_effects.txt:9-373` covers idea lifecycle, compact values, route politics, focus callbacks, package setup, final validation, and cleanup, and its header records the absent central wiring.
- `common/decisions/categories/006_independence_wave_categories.txt:464-467` defines `independence_wave_udm_industrial_forest_category`.
- `common/decisions/006_independence_wave_siberian_decisions.txt:2317-2511` contains `independence_wave_udm_hold_workshop_congress` and the ten UDM projects with activation, availability, cost, timeout/cancel, effects, AI, and icon references.
- `common/ideas/006_independence_wave_ideas_registry.txt:4282-4359` defines the seven UDM ideas and uses shared registered Event 006 idea sprites.
- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3385-3458` defines the four UDM strategy blocks and package/setup gates.
- `common/national_focus/006_independence_wave_focus.txt:129,182,216,1447,1718` contains the five UDM-specific shared-tree callback branches.
- `localisation/english/006_independence_wave_udm_l_english.yml:1-67` covers the category, founding mission, ten projects, costs, tooltips, seven ideas, and four route party names.
- `common/script_constants/006_independence_wave_constants_registry.txt:1873-1888,2149,2363,2577,6809-6822,7621,9262-9331` provides the force profile, p48 mapping, tradition, pathway mask, archetype table, package id, and UDM tuning values.

## Missing or stale package surfaces

- No UDM entry is present in the central adapter, content-attestation registry, normal or SCN-008 preflight, scenario admission, or deterministic Join surfaces; this is an admission blocker, not a safe package-local patch.
- The package still maps `industrial_security` force profile to the shared `industrial_breakaway` archetype because no `industrial_security` archetype token exists in `common/script_constants/006_independence_wave_constants_registry.txt:6809-6822`; the owner must explicitly accept that mapping or redesign the shared contract.
- The current authority docs still point at older 2026-08-14 UDM handoffs in `docs/specs/006_independence_wave_specs/quality/package_manifest.md:49` and `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md:59`; this audit records the newer status but did not rewrite shared authority files while other agents' work is present.

## Map and state setup

- Vanilla `history/states/399-Izhevsk.txt:2-29` confirms id 399, `STATE_399`, owner SOV, SOV and UDM cores, capital/VP province 6278, infrastructure 2, chromium 18, and the expected province list.
- Vanilla `history/countries/UDM - Udmurtia.txt:1-101` confirms capital 399, three research slots, vanilla starting technology, and `recruit_character = UDM_boris`.
- Package planning and reservation use state 399 consistently in `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:421-428` and `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1060-1071,1213`.
- Fresh `hoi4.map_inspect` and `hoi4.map_render` attempts reached the installed MCP but returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` for workspace `mod_chaos_redux_ea3b2d67c2c0` before scanning or producing artifacts, so no current MCP map evidence is claimed.
- The prior 2026-08-26 map receipt in `006_iw048_udm_current_admission_audit_2026_08_26.md:67-69` found no UDM-specific state-399 error but reported unrelated workspace map diagnostics; it is historical context, not a refreshed proof of current state/host behavior.

## Politics, leader, portrait, flag, advisor, and party issues

- Vanilla `common/characters/UDM.txt:1-15` defines `UDM_boris` as Boris Berman with civilian portrait token `GFX_portrait_Boris_Berman` and a stalinism leader record, while vanilla history recruits that character.
- The package's parent-owned identity-rights gate has no local setter, and the exact-name portrait research remains fail-closed; no generic texture, wrong-person portrait, or generated fallback was introduced.
- The package initializes democratic, cultural/neutrality, worker/communist, and emergency route politics in `common/scripted_effects/006_independence_wave_udm_package_effects.txt:143-216`, and cleanup restores the vanilla democratic baseline at `:320-370`.
- Vanilla flags exist at `gfx/flags/UDM_{communism,democratic,fascism,neutrality}.tga` in the installed game, but no mod-side rights/provenance manifest or alternate flag is present.
- No custom advisors or command characters are present, so the package cannot claim a complete bespoke leadership roster until the identity owner resolves the source or institution decision.

## Focus, decision, idea, and asset issues

- The UDM focus callbacks are guarded and routed through the shared focus tree, but fresh `hoi4.focus_inspect` and `hoi4.focus_render` attempts failed with the same workspace artifact-manifest blocker; the prior shared-tree receipt is recorded in `006_iw048_udm_current_admission_audit_2026_08_26.md:80-83`.
- The decision category, founding mission, and ten projects are source-complete at the package level, including visible text, costs, cancellation, timeout failure, and route guards in `common/decisions/006_independence_wave_siberian_decisions.txt:2328-2511`.
- Shared Event 006 idea and decision sprites resolve through `interface/006_independence_wave.gfx:33-54`; no UDM-specific icon gap was found.
- The current worktree has an unrelated AI-registry whitespace edit and a concurrent removal of the UDM strategic cost's war-support guard in `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:50-54`; this audit did not modify or adjudicate that concurrent change.

## Starting military, technology, industry, supply, and production

- IW-048 reuses vanilla UDM history rather than adding an independent country history, army, navy, air force, equipment stockpile, or technology baseline.
- The shared force mapping provides p48, tradition 54, industrial-security profile, and five selected reinforcement pathways, but the force-profile/archetype mismatch remains unresolved at `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:168-186`.
- State 399 retains its vanilla rural, infrastructure, chromium, and province setup; package project costs use guarded civilian-factory modifiers and do not add an unplanned production or map fallback.
- No UDM-specific technology or doctrine tree is declared; fresh `hoi4.tech_inspect` and `hoi4.tech_render` attempts failed before scanning, and the installed package exposes no Technology Tree Viewer, which remains an unresolved tooling limitation.

## AI and playability issues

- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3406-3458` provides industrial survival, former-host restraint, settled compact, and emergency guard behavior with package/setup gates.
- The required fresh `hoi4.probability_inspect` attempt for the AI source failed with `ARTIFACT_MANIFEST_INTEGRITY_FAILED`; the prior 2026-08-26 receipt reported `no_weighted_surfaces` and zero candidates, but that receipt predates current worktree state.
- The required fresh decision probability inspection also failed before scanning; the prior receipt reported 88 candidates, zero available candidates, 16 required inputs, and no unresolved source diagnostics, so no normalized decision probability or balance claim is valid.
- The callable tool set exposes no direct `chaosx_ai_probability_auditor` subagent route, and no owner patch occurred in this audit, so no `hoi4.probability_compare` is claimed.
- No live HOI4 session, save-load test, or long-horizon AI run was performed.

## Event and central integration evidence

- IW-048 has no dedicated Event 006 branch and relies on a future owner-approved dispatcher, as documented in `docs/events/006_independence_wave/udmurtia_package.md:25-37`.
- Fresh `hoi4.event_inspect` and `hoi4.event_render` attempts for `chaosx.nr6.350` failed before graph creation with `ARTIFACT_MANIFEST_INTEGRITY_FAILED`; the historical partial receipt and artifact references remain in `006_iw048_udm_current_admission_audit_2026_08_26.md:99-103`.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt:192` includes `iw_048` in the ranked package-id array, but ranking is not equivalent to central admission or runtime Join readiness.
- Existing formable references in `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt:316,323` treat UDM as a possible member candidate for later formables, while the UDM package itself keeps `independence_wave_formable_family_registered` false.

## Disposition and next authorized action

IW-048 is not admissible. The immediate owner queue is: clear Boris/institution identity and portrait rights through `chaosx_portrait_creator`; resolve or explicitly approve the `industrial_security` versus `industrial_breakaway` contract; prove state-399 host retention and reservation behavior in named scenarios; repair the MCP artifact-manifest blocker; obtain typed probability fixtures and same-scenario comparison; then prepare a parent-reviewed central admission patch. No package gameplay patch is authorized by this audit, and no simplification or fallback was made.

## Validation and skipped checks

- Completed source review against the offline Paradox wiki country, character, portrait, flag, focus, decision, idea, AI, map, event, localisation, triggers, effects, and scopes pages, plus the relevant vanilla documentation files.
- Completed direct vanilla and repository collision/source checks for `UDM`, state 399, `UDM_boris`, the portrait token, and ideology flags; no mod-side UDM override or unrelated workshop hit was found.
- Attempted all applicable read-only MCP routes: map inspect/render, Event 006 inspect/render, shared focus inspect/render, AI/decision probability inspect, and technology inspect/render; every current call was blocked before artifact creation by `ARTIFACT_MANIFEST_INTEGRITY_FAILED`.
- Skipped map/focus/event/technology rewrites, live HOI4 execution, RunPod, asset generation, central admission, and probability compare because they are outside this read-only audit or blocked by the exact limitations above.

Changed files: this handoff only.

Changed tags, states, leaders, parties, focus ids, localisation keys, formables: none.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw048_udm_package_audit_2026_08_27.md`.
