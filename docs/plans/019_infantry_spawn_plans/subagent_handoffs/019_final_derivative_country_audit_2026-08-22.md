# Event 19 derivative country package final audit — 2026-08-22

## Verdict

The Event 19 derivative-country package is **not source-complete for sign-off**.

No P0 defect was confirmed in the read-only audit.

The concrete P1 blockers are missing asset provenance/manifests, an unavailable mandatory probability-auditor route, missing explicit starting economy and country-level logistics reconciliation, and a strict weaker-than-parent gap for the Event 19 ghost starting template.

The runtime country, transfer, leader, unit-provider, focus, decision, AI, isolation, decline, expansion, and defeat-cleanup implementations are substantially present, but the unresolved surfaces prevent a completion claim.

This audit made no gameplay, localisation, focus, asset, map, or documentation-source edits; only this handoff was added.

## Scope and required evidence

The audit covered the dynamic derivative package for `chaosx.nr19.1`, including ordinary claimant breakaways, anomalous claimant breakaways, independent zombie/ghost/golem families, shared classifiers, country creation and state transfer, leaders and visual identity, starting ideas, provider units and reinforcement, focus and decision routes, AI strategy, expansion, ghost decline, parent isolation, defeat/annex cleanup, flags, localisation, and Event 19 specifications and handoffs.

The required offline Paradox wiki core pages and the country-creation, division, and national-focus pages were read, along with the relevant vanilla documentation and precedents.

The required country/event/focus/decision/assets/comfyui/subagent skills were read before the source audit.

## Severity-ranked findings

### P0 — none confirmed

No confirmed P0 country-package defect was found in the reviewed source or the available read-only MCP evidence.

### P1 — missing asset provenance and manifests, confirmed

The current repository has runtime Event 19 assets but no `docs/assets/019_infantry_spawn/` tree.

The missing tree includes the required source/master/runtime provenance records such as `manifest.md`, `gfx_handoff.md`, source PNGs, processed PNGs, checksum/crosswalk tables, contact sheets, provider/source-mode records, and portrait-specific wiring evidence.

The planning requirement is explicit in `docs/specs/019_infantry_spawn_specs/matrices/019_asset_inventory.md`, which requires source PNG, processed PNG, DDS/TGA runtime output, manifest, sprite wiring, contact sheet, and source-mode or prompt provenance for completion.

The stale historical claims in `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026-07-18.md` and `019_full_portrait_regeneration_handoff_2026-07-16.md` refer to that missing directory and cannot substitute for files that are absent from the current tree.

This is a confirmed package-evidence defect rather than a confirmed runtime-load defect because the runtime files remain present under `gfx/leaders/019_infantry_spawn/`, `gfx/flags/`, `gfx/interface/goals/019_infantry_spawn/`, `gfx/interface/decisions/019_infantry_spawn/`, `gfx/interface/ideas/019_infantry_spawn/`, and `gfx/event_pictures/019_infantry_spawn/`.

### P1 — mandatory probability audit unavailable, confirmed limitation

The required named `chaosx_ai_probability_auditor` route is not exposed as a callable tool in this runtime, so the mandatory auditor-owned probability pass cannot be completed.

Direct read-only MCP inspection found the derivative focus source at `common/national_focus/019_infantry_spawn_derivative_focus.txt` with 45 candidates but `poolComplete=false` and 11 required inputs.

Direct decision inspection found `common/decisions/019_infantry_spawn_derivative_decisions.txt` with `poolComplete=false` and seven required inputs, and claimant decisions at `common/decisions/019_infantry_spawn_claimant_decisions.txt` with `poolComplete=false` and four required inputs.

The derivative AI strategy source `common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces` because the adapter does not normalize the profile-based `ai_strategy` blocks.

The provider callbacks are meta-dispatched by provider id, and the available probability adapter does not normalize that provider pool into scenario-level candidates.

These are MCP/auditor limitations, not proof that the source weights are invalid, but they block the required scenario-specific balance certification and any final source-complete claim.

### P1 — starting country economy and logistics reconciliation is not explicit, confirmed source gap

The derivative setup in `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:520-593` initializes private ledgers, ideas, politics, dynamic focus loading, region metadata, the opening mission, and the pulse, but does not explicitly reconcile starting factories, production lines, research slots or technologies, fuel, convoys, supply capacity, supply hubs, railways, ports, resources, or captured stockpiles.

The Event 19 derivative specification requires those inputs to be evaluated in `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_6_derivative_countries.md:261-275`.

The file contains later decision/reinforcement costs and a golem infrastructure action at approximately line 6944, but those effects are not a starting-country reconciliation.

`create_dynamic_country` may inherit engine state from `original_tag = ROOT`, but the available documentation and MCP routes do not prove which country-level economy and logistics state is copied, so this remains an acceptance blocker rather than a proven runtime outcome.

### P1 — strict weaker-than-parent proof is missing for the ghost starting template, confirmed source comparison

`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4493-4505` builds the Event 19 ghost template from four `death_weak_ghost_host` battalions.

`history/units/DTH_1936.txt:1-10` gives the Death parent’s `Death Passive Host` the same four `death_weak_ghost_host` battalions.

Therefore the ghost derivative is not strictly weaker at the raw starting-template row level, even though the package is isolated from Death’s soul economy and world-end route, has slow decline, and has bounded expansion and provider costs.

The zombie provider is materially bounded to four base `zombies` battalions in `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4239-4251`, with no mutation or weaponized variants, and the golem provider uses two `coal_golem` battalions at `:4740-4750` versus the parent KMB four-row template at `common/scripted_effects/005_soviet_collapse_effects.txt:22189-22201`.

The package-level weakness contract is therefore strong for zombie and golem but not strictly demonstrated for ghost, and the parent should either accept the bounded-route interpretation or tune and re-audit the ghost starting strength.

### P2 — focus layout warnings, confirmed non-blocking MCP diagnostics

The fresh `hoi4_focus_inspect` result for `infantry_spawn_derivative_focus_tree` reported 45 focuses, 54 connectors, zero crossings, zero node intersections, and zero long connectors, with seven non-blocking warnings/information diagnostics.

The warnings identify two linear detours (`infantry_spawn_derivative_inventory_the_seized_districts` to `infantry_spawn_derivative_restore_a_chain_of_orders`, and `infantry_spawn_derivative_quiet_the_fragmented_columns` to `infantry_spawn_derivative_outlast_the_former_state`) plus sibling-anchor asymmetry in family cohorts.

The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0892ecbe73218dfd6e9764500f4f5db739e99f61f1d1ae99a2c61512334bb2e5/ad632148fbe464c0a372e918abe5b4ff1c3949cf44179ca3373c94b6009a2cfe/focus-inspect.6d1053f86f5afcee.json`.

The warnings do not block focus loading or route availability, but the presentation is not warning-free.

### P2 — Event 19 route-count wording is stale or ambiguous, confirmed documentation drift

`docs/events/019_infantry_spawn/overview.md:591-593` says “thirty common focuses plus five family-gated focuses,” while the current source and MCP inspection contain 45 total focus nodes, consisting of 30 common nodes plus five nodes in each of the three family cohorts.

This may describe 35 focuses visible to one family or may be stale wording, but it should be clarified before a documentation-complete claim.

### P2 — dynamic state/map projection and technology viewer remain unresolved, confirmed MCP limitations

`hoi4_map_inspect` validated the canonical map sample but cannot project Event 19’s runtime state arrays and event-target-selected regions into a fixed state-id country view.

The map artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a25e1973a846bc80d560a2988596b71210cdd26a3e319a7da683db903454b9ab/9a5185a3bc3c3f72a88b559f6f18d7e17d08c50f3c26ece3fef6870c3414684a/map-inspect.1746207909525d1f.json`.

The map result also contains unrelated global `map/buildings.txt` invalid-position and port-adjacency diagnostics, which cannot be attributed to Event 19.

No Event 19 derivative-owned technology node was found, but the installed package exposes no Technology Tree Viewer, so technology evidence remains unresolved by tool limitation.

### P3 — localisation filename typo, confirmed hygiene issue

The Event 19 localisation file is named `localisation/english/019_infrantry_spawn_l_english.yml` with `infrantry` rather than `infantry`.

The file is still likely loaded by the engine’s localisation glob, and the current census reports 3025 unique keys with no duplicate keys, so this is a maintainability issue rather than a confirmed missing-localisation defect.

## Country-package coverage checklist

### Dynamic tags, state ownership, and isolation

Dynamic creation is implemented at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:5228-5237` with `create_dynamic_country`, `original_tag = ROOT`, a saved actor target, and no fixed-tag fallback.

The source search found no Event 19 derivative `tag =`, `release =`, or `change_tag` creation path; parent `KMB` references in provider eligibility are parent-provider checks, not fallback actor creation.

State transfer is implemented by `infantry_spawn_transfer_natural_derivative_region_to_actor` at `:1698-1717`, with state transfer, cores, and a saved capital anchor.

The transaction stages source rows, creates and proves the dynamic actor, transfers the selected states, recreates recorded units, verifies ownership/control/core/capital counts, deletes and proves the source set, and commits accounting only after proof.

The three mode filters in the transfer preflight distinguish ordinary claimant UID, anomalous claimant family or UID, and independent family id, and require recorded Event 19 unit rows with status above `untracked` and below `transferred_out`.

The identity proof at `:1276-1335` checks generated identity, unit UID, generation UID, lot UID, template UID, family, claimant, origin, and live division scope before transfer.

Claimant source snapshots at `:4085-4095` and `:4495-4512` explicitly require `infantry_spawn_unit_status.claimant_loyal` for claimant-specific remaining rows; independent family transfers are family-scoped recorded rows without a claimant UID by design.

One-state independent-family handling is implemented by `infantry_spawn_prove_natural_family_same_tag_takeover` at `:5395-5495`, which requires exactly one controlled state and exact family-only live formations, and `infantry_spawn_execute_natural_family_same_tag_takeover` at `:5497-5584` applies the same-tag takeover.

Failed transaction handling is implemented by `infantry_spawn_apply_natural_derivative_precommit_failure` at approximately `:5129-5187`, which dispatches the claimant failed-coup path or defers a family breach and restores the precommit source state.

`is_infantry_spawn_derivative_country` and `infantry_spawn_parent_event_identity_is_absent` in `common/scripted_triggers/019_infantry_spawn_triggers.txt:1140-1190` enforce derivative subtypes and reject parent identities.

The shared `is_special_chaos_country`, `is_actual_nonhuman_country`, and `uses_normal_civilian_systems` classifiers include the derivative and nonhuman triggers in `common/scripted_triggers/chaosx_dynamic_triggers.txt`.

The ordinary Event 19 event excludes derivative countries at `events/019_infantry_spawn.txt:177`, and the derivative pulse uses the country-local pulse rather than a world-wide recurring scan.

### Leaders and visual identity

The current Event 19 GFX wiring exposes 20 claimant portraits, six derivative host/council portraits, and one neutral muster portrait in `interface/019_infantry_spawn.gfx:52-156`.

All 20 claimant and all six zombie, ghost, and golem runtime DDS outputs were converted only in a temporary directory and reviewed as a contact sheet; every image depicts an army, procession, formation, camp, host, or massed horde, with no individual focal person.

All discovered Event 19 leader-creation paths are male-only: six derivative commander/council paths at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:390-448`, two scenario assembly/council paths at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:211-227`, the claimant corps commander at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:196-200`, and the external Event 19 provider leader at `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:1686-1689` all set `female = no` or `is_female = no`.

The claimant lookup also filters `is_female = no` at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:319-333`.

No `common/characters/019_infantry_spawn_characters.txt` exists, which is consistent with the package’s dynamic leader creation and is not itself a defect.

Runtime art wiring is present, but the missing asset provenance tree prevents verification of portrait-worker provenance, source-mode records, master outputs, crosswalks, and final-versus-placeholder status.

### Politics, ideas, localisation, decisions, and focus

`common/ideas/019_infantry_spawn_derivative_ideas.txt` contains the derivative starting burdens and family-specific lifecycle ideas, including command confusion, seized districts, former-parent pursuit, claimant dispute, zombie fragmentation, ghost instability, and golem broken pattern.

`common/national_focus/019_infantry_spawn_derivative_focus.txt:18-29` assigns `infantry_spawn_derivative_focus_tree` only to derivative countries, and the source contains 45 focus nodes with AI weights on all focus blocks.

The fresh focus MCP inspection found a valid 45-node graph with 54 connectors and no blocking layout diagnostics.

`common/decisions/019_infantry_spawn_derivative_decisions.txt` contains 26 derivative decisions/missions covering training, family binding, sustainment, claimant preservation/replacement, local submission, integration, expansion, and defeat pressure.

Decision and focus localisation coverage is present in `localisation/english/019_infrantry_spawn_l_english.yml`, and the latest localisation handoff reports 3025 unique keys with no duplicates.

The dynamic provider localisation handoff reports 57 provider presentation and cost tokens resolved after provider migration.

No dedicated Event 19 scripted GUI is required by the current package; the routes are ordinary decision categories and focus rewards.

### Actual units, reinforcement, and family distinctions

`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:2337-2349` recreates recorded formations with `create_unit`, frozen experience/equipment/manpower factors, recorded UIDs, templates, and the dynamic derivative owner.

Provider 501 in `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4206-4427` exposes only base `zombies`, with training, sustainment, management, derivative setup, and cleanup callbacks.

Provider 502 at `:4427-4675` exposes only the weak ghost host, with manifestation, sustainment, no ordinary queue, derivative setup, and cleanup callbacks.

Provider 503 at `:4675-4915` exposes coal golem formations, industrial/material gates, sustainment, derivative setup, and cleanup callbacks.

The derivative pulse and provider callbacks maintain family-specific reinforcement and ledger state, and `infantry_spawn_derivative_apply_ghost_decline` at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:7024-7053` applies a 180-day cooldown with anchored and managed reductions rather than a fast decline.

### Expansion, AI, isolation, and cleanup

`infantry_spawn_derivative_can_expand` and the derivative decisions provide bounded neighboring-state expansion and integration checks.

`common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt` contains route-specific profiles for opening, claimant, collective, zombie, ghost, golem, sustainment, and expansion behavior, with flag-gated activation and abort conditions.

The required direct probability inspection was performed, but the unavailable named auditor and incomplete adapters prevent normalized strategy and provider-pool balance evidence.

`common/on_actions/019_infantry_spawn_derivative_on_actions.txt:65-116` handles derivative capitulation, annexation, evolution-membership unregistering, defeat processing, retry-queue migration, and final cleanup.

`infantry_spawn_derivative_final_cleanup` at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:7604-7628` locks and removes tracked formations, dispatches provider cleanup, requires cleanup proof, retries on invariant failure, and only then finalizes the derivative identity.

No derivative-owned world-end or super-event route was found, and the Event 19 overview explicitly describes derivatives as isolated from parent progression, parent counts, evolutions, deaths, wars, and world-end progression.

## MCP artifacts and limitations

The Event 19 lint inspection returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics, but deferred workspace expansion produced 8282 unresolved references and 367 truncated inline paths, so it is not a complete whole-event proof.

The event artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cee24747dde6fefdf7c21c77f25f75ac1b55ac8229787984f13acecdfb5d255a/ae31e2b4cc8786a878b249e9c3b382ceafd500306392f6b2ccccf557c1494026/event-lint-43f28961e452.json`.

The event neighborhood render returned `EVENT_RENDERED_PARTIAL` with no blocking selected-node diagnostic because full workspace analysis was deferred.

The map inspection was read-only and package-specific dynamic state projection was unavailable; unrelated global map diagnostics were not attributed to Event 19.

No Technology Tree Viewer is exposed by the installed package, and no Event 19 derivative-owned technology node was found to render.

No probability compare was run because this audit made no weighted-source patch, the named probability auditor is unavailable, and the direct adapters do not produce a complete normalized candidate pool.

## Missing or stale surfaces to resolve before completion

- Restore or regenerate the complete `docs/assets/019_infantry_spawn/` source/master/runtime provenance tree and crosswalks for portraits, flags, focus icons, decision icons, idea icons, and report art.
- Complete the required `chaosx_ai_probability_auditor` scenario pass for all derivative focus, decision, strategy-factor, and provider-weight surfaces, including normalized provider callbacks and named zombie, ghost, golem, claimant, and one-state scenarios.
- Add or prove explicit starting economy, industry, research, production, stockpile, fuel, convoy, supply-hub, railway, port, resource, and population reconciliation against the derivative-country specification.
- Resolve whether the ghost derivative must be strictly weaker than `Death Passive Host` at starting-template strength and, if so, adjust the provider or document an accepted package-level weakness rule before re-auditing.
- Clarify the 35-versus-45 focus-count wording in `docs/events/019_infantry_spawn/overview.md`.
- If final review requires advisors or high-command roles, none are present in the Event 19 derivative-specific sources; the current specification explicitly covers leaders and councils but does not require those extra roles.

## Handoff status

The source evidence supports dynamic-only country creation, state and capital safety, recorded Event 19 formation transfer, one-state takeover/failed-coup handling, male-only army/massed-host leader identity, family-specific actual units and reinforcement, slow ghost decline, shared special/nonhuman classifiers, bounded focus-scale routes, decisions, AI profiles, parent isolation, no-world-end behavior, and proof-gated annex cleanup.

The package remains **not source-complete** because the P1 surfaces above are unresolved.

No live game launch or in-game validation was performed, as required by repository policy.
