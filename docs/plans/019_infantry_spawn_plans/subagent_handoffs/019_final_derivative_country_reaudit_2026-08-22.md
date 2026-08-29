# Event 019 derivative and claimant country-package final re-audit — 2026-08-22

Status: read-only country-package audit complete. No gameplay, focus, decision, AI, asset, map, localisation, or registry file was edited by this audit. No commit was created.

The audited package is the current Event 019 claimant and zombie/ghost/golem derivative surface. The parent’s concurrent changes were preserved. The package has no fixed output tag or fixed-tag fallback path.

## Executive verdict

The current derivative country package is structurally coherent after the parent’s latest corrections. Dynamic country creation, one-state family takeover, recorded-unit transfer, local asset reconciliation, male-only claimant identities, family council identities, derivative focus loading, paid formation operations, and defeat/annex cleanup are all present in the current source.

The parent corrections are visible in the audited source: the ghost derivative template has three weak ghost battalions versus Death’s four, the provider 523 census is nine bodies with 7,350 manpower, 990 infantry equipment, and 35 motorized equipment, and opening assets are reconciled rather than granted.

Two evidence boundaries remain unresolved. The mandatory `chaosx_ai_probability_auditor` callable route is not exposed in this runtime, and direct current probability calls for the derivative and claimant decision files/provider registry returned `INTERNAL_ERROR`. The installed MCP package also exposes no Technology Tree Viewer. These are reported as evidence blockers, not replaced with source-only probability or technology claims.

One low-risk source hygiene finding remains: `minimum_population_fraction = 0.001` is declared only in `common/script_constants/019_infantry_spawn_derivative_package_constants.txt:247` and is not consumed by `infantry_spawn_derivative_apply_ghost_decline`. The active decline uses the base, anchored, managed, maximum, and hard-cap values. This may be an intentionally unused tuning floor, but it should be resolved by the package owner before claiming that every declared decline constant is live.

## Country-package coverage checklist

| Surface | Current evidence | Verdict |
| --- | --- | --- |
| Dynamic safe creation | `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:5410-5588`, `create_dynamic_country = { original_tag = ROOT }` at `:5422` | Pass; no fixed tag or fallback creation path |
| State transfer and capital | `:1892-1910`; selected owned states transfer and core to the dynamic actor, then the actor receives the frozen anchor capital | Pass for the one-state and exact-transaction paths; dynamic state arrays remain outside map-render projection |
| Recorded formations | `:2531-2543`, `:3625-3637`; `create_unit` is called with recorded cohort/template UIDs and a dynamic owner target | Pass; no unrecorded free grant observed |
| One-state family takeover | `:5589-5691`; requires independent-family mode, exactly one controlled state, claimant-free family rows, aligned ledgers, and exact live division count | Pass; failed proof routes to recovery or exact transaction |
| Claimant identity pool | `common/script_constants/019_infantry_spawn_claimant_constants.txt`, `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:27-108`, claimant identity effects `:190-223` | Pass; 20 region-gated profiles, male names, and `female = no` |
| Derivative identity and flags | `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:417`, `:668-914` | Pass; claimant, zombie, ghost, and golem identities resolve through validated identity/region tokens |
| Leaders and councils | `:512-656`, `:6588-6730`; dynamic claimant promotion and family commander/council creation | Pass; councils use institutional names and all current leaders are male-only |
| Local opening assets | `:46-228`, `:770`; state, economy, population, infrastructure, rail, port, supply, resource, research, fuel, standard stock, custom provider stock, debt, and formation snapshots | Pass; fragile/strained/viable classification does not grant free assets |
| Parent runtime isolation | `:274-333`, `:736-771`; parent ideas/missions/flags/evolution memberships are cleared before the derivative tree loads | Pass; derivative private ledgers remain owned by the derivative package |
| Focus tree | `common/national_focus/019_infantry_spawn_derivative_focus.txt`, tree `infantry_spawn_derivative_focus_tree` | Pass structurally; 45 source nodes and 35 visible per active family, with two nonblocking sibling-anchor warnings |
| Adapted decisions and missions | `common/decisions/019_infantry_spawn_derivative_decisions.txt`, 26 top-level blocks including three missions; claimant decisions contain seven blocks | Pass source-level; targets, costs, cooldowns, route gates, icons, and effect tooltips are present |
| AI strategy | `common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt` | Source pass; probability evidence remains unresolved because the auditor route is unavailable |
| Provider families 501/502/503/523 | `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4047-4929`, `common/scripted_effects/014_cannibalism_effects.txt`, Event 014 constants | Pass for family ownership, paid management, and cleanup boundaries; custom pool odds remain unresolved |
| Ghost decline | Package effect `:7218-7249`; derivative constants `:237-248` | Pass for 180-day slow decline and hard cap; unused minimum-floor constant is a hygiene follow-up |
| Defeat and annex cleanup | `common/on_actions/019_infantry_spawn_derivative_on_actions.txt:67-116`, package effects `:7402-7854` | Pass; tracked formations and provider additions are proof-gated and retry on invariant failure |
| Flags, portraits, focus/idea/decision art | `docs/assets/019_infantry_spawn/manifest.md`, `interface/019_infantry_spawn.gfx`, `gfx/flags`, `gfx/leaders/019_infantry_spawn` | Pass for the current claimant and six derivative scene package; historical/provider-extension asset gate remains separate |
| Technology tree | No Event 019 derivative technology source; no installed Technology Tree Viewer | Unresolved limitation, not an invented pass |
| Map write/validation | No map rewrite was performed; dynamic selected-state arrays are runtime data | Parent-scope follow-up; no map mutation by this audit |

## File-surface checklist

The primary country-package files audited were:

- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt`
- `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- `common/national_focus/019_infantry_spawn_derivative_focus.txt`
- `common/decisions/019_infantry_spawn_derivative_decisions.txt`
- `common/decisions/019_infantry_spawn_claimant_decisions.txt`
- `common/ideas/019_infantry_spawn_derivative_ideas.txt`
- `common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt`
- `common/on_actions/019_infantry_spawn_derivative_on_actions.txt`
- `events/019_infantry_spawn.txt`
- `events/019_infantry_spawn_scenario.txt`
- `common/script_constants/019_infantry_spawn_constants.txt`
- `common/script_constants/019_infantry_spawn_derivative_constants.txt`
- `common/script_constants/019_infantry_spawn_derivative_package_constants.txt`
- `common/script_constants/019_infantry_spawn_claimant_constants.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `common/script_constants/014_cannibalism_constants.txt`
- `interface/019_infantry_spawn.gfx`
- `localisation/english/019_infrantry_spawn_l_english.yml`
- `docs/assets/019_infantry_spawn/manifest.md`
- `docs/events/019_infantry_spawn/overview.md`
- `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`
- `docs/events/019_infantry_spawn/systems/triggerable_scenario.md`

The localisation filename contains the historical `infrantry` spelling. It is currently glob-loadable, but the filename is a P3 repository-hygiene risk and should be renamed only in an owner-approved localisation maintenance change.

## Dynamic creation, transfer, and recovery findings

`infantry_spawn_run_natural_derivative_exact_transaction` freezes the release mode, saves the parent event target, allocates a dynamic nonce, snapshots global accounting, stages only recorded unit rows, and calls `create_dynamic_country` with `original_tag = ROOT`. It does not call a fixed `release`, `change_tag`, or hard-coded derivative tag. Identity, claimant UID, family/provider, generation, region, and presentation tokens are set only after the dynamic actor exists and validates.

Selected owned states are transferred with `transfer_state = PREV` and `add_state_core = PREV`. The actor receives the frozen anchor state as capital. The source set is deleted and proved empty before commit; ledgers, debt, manpower, equipment, formation rows, and global accounting are rechecked before finalization. Failure paths restore source rows or annex a provisional carrier only inside the explicitly marked recovery transaction, then prove zero live divisions before cleanup.

The same-tag family route is not a hidden multi-state civil war. `infantry_spawn_prove_natural_family_same_tag_takeover` requires independent-family mode, a valid family/provider/generation, exactly one controlled state, no claimant rows, aligned ledgers, claimant-free family rows, and exactly one live division for each recorded source row. If the one-state proof fails, the route uses the exact transaction rather than a fixed fallback.

The actual unit calls use `Unbidden Formation [UNIT_UID]`, a dynamic owner event target, a dynamic template UID, recorded source cohort IDs, and preserved start experience/equipment/manpower factors. No derivative setup effect grants an unrelated army, manpower, stockpile, or factory bundle.

## Formation providers and weaker-than-parent proof

| Provider | Runtime family | Mode and current derivative template | Parent comparison and package boundary |
| --- | --- | --- | --- |
| 501 | Zombie | `trainable_and_spawnable`; `Unbidden Muster [TEMPLATE_UID]` contains four `zombies` rows at `:4253-4265`; management is paid and base-zombie-only | Vanilla `history/units/ZZZ_1936.txt` has 16 `zombies` rows in its base template, so the derivative is weaker and does not import the parent’s broader progression |
| 502 | Ghost | `spawn_only`; `Unbidden Muster [TEMPLATE_UID]` contains exactly three `death_weak_ghost_host` rows at `:4507-4517`; no training, Death-country setup, soul pool, rapid wasteland, evolution, super-event, or world-end callback | Vanilla `history/units/DTH_1936.txt` has four weak ghost-host rows; the Event 19 derivative is strictly weaker at raw battalion count and retains paid manifestation plus slow decline |
| 503 | Golem | `spawn_only`; derivative template uses two `coal_golem` rows and no engineer support; paid coal-golem equipment, factory, political-power, and command-power gates | `common/scripted_effects/005_soviet_collapse_effects.txt:22189` and KMB precedent use four golem rows plus support; the derivative uses the weaker two-row host and does not invoke KMB progression |
| 523 | Cannibal irregulars | Event 014-owned `spawn_only`, family-only provider; nine recorded combat rows (`cannibal_scavenger_warband`, `cannibal_feast_guard`, `cannibal_feast_cohort`, `cannibal_bone_guard`, `cannibal_bone_riders`, `cannibal_island_reavers`, `cannibal_siege_eaters`, `cannibal_march_predation_column`, `cannibal_network_cadre`) | Current owner constants are exactly nine bodies, 7,350 manpower, 990 infantry equipment, and 35 motorized equipment. Event 19 does not install Event 014 identity, stage, count, or world-end state for this provider; its callbacks are bounded no-op setup/removal with provider-owned accounting |

Provider 501, 502, and 503 setup callbacks first require `infantry_spawn_parent_event_identity_is_absent`, then install only the derivative provider identity. Cleanup locks recorded family templates, removes provider public additions, retires the dynamic provider leader/cosmetic identity, and proves the provider package absent. Provider 503 has a `tag = KMB` eligibility branch for native KMB ownership, but the derivative creation path uses the derivative flag and dynamic provider selection; this is not a fixed-tag creation fallback.

## Claimant and derivative identity findings

The 20 claimant profiles are defined in `common/script_constants/019_infantry_spawn_claimant_constants.txt`, region-gated in `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:27-108`, and selected by `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:190-223`. Each profile has a regional male-coded name pool and a male commander with `female = no`. The current source contains no opposite-gender name pool, no female leader metadata, and no female portrait wiring. The profile enum labels that look feminine are not used as the rendered name strings.

The claimant leader path finds the recorded claimant character by UID and promotes that male character with an archetype-specific ideology. The zombie, ghost, and golem paths create male family commanders and male councils. Current institutional names are `Council of Numbered Bands`, `Chorus of Anchors`, and `Council of Living Patterns`; the commander names are `First Hunger`, `The First Anchor`, and `Master Builder Khel`. Council portraits are institutional massed-host scenes rather than personal random-name portraits.

The cosmetic identity path uses one validated dynamic `meta_effect` call at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:417` to build `INFANTRY_SPAWN_[IDENTITY]_[REGION]`. Identity and region enums fail closed before the cosmetic tag is applied. The dynamic path has 13 identity stems across seven regions, with the extra unregional base flag files retained as harmless package assets rather than selected fallback tags.

## Portrait, flag, and asset findings

`docs/assets/019_infantry_spawn/manifest.md` records 20 regional claimant army/muster scenes and six derivative zombie/ghost/golem host/council scenes as fictional built-in ImageGen originals, processed to runtime PNG/DDS outputs. The reviewed contact sheets were:

- `docs/assets/019_infantry_spawn/contact_sheets/event_019_claimant_processed_contact_sheet.png`
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_derivative_portrait_processed_contact_sheet.png`

Visual review found no focal human identity in the claimant army scenes and no focal personal identity in the six host/council scenes. This is consistent with the current institutional/host portrait contract. The runtime directory contains 20 `portrait_019_claimant_01.dds` through `portrait_019_claimant_20.dds` and six named derivative runtime portraits (`portrait_019_zombie_host_commander.dds`, `portrait_019_zombie_host_council.dds`, `portrait_019_ghost_host_commander.dds`, `portrait_019_ghost_host_council.dds`, `portrait_019_golem_master_builder.dds`, and `portrait_019_golem_pattern_council.dds`), plus the neutral unassigned muster asset. `interface/019_infantry_spawn.gfx` wires all claimant and derivative portrait sprites.

The normal, medium, and small flag tiers each contain 104 `INFANTRY_SPAWN_*.tga` files. The current dynamic cosmetic path resolves the 91 regional identity combinations required by the 13 identity stems and seven regions. No runtime source or archive path under `docs/assets/019_infantry_spawn` is referenced from gameplay, interface, localisation, or `gfx` source.

The manifest still carries a separate historical/provider-extension gate. This audit does not promote that broader Event 019 asset tranche to complete and does not count the neutral muster asset as a claimant identity.

## Opening assets, economy, equipment, and supply

`infantry_spawn_derivative_reconcile_starting_local_assets` snapshots owned-state count, civilian/military/naval factories, population, infrastructure, naval bases, supply nodes, all listed resources, railway states, research slots, fuel ratio, standard infantry/support/motorized/train/convoy stockpiles, recorded debts, and active formations. It calls the provider-owned custom-equipment publisher for dynamic provider tokens and amounts, then classifies the opening as fragile, strained, or viable through package constants.

Only the fragile classification adds `infantry_spawn_derivative_local_asset_shortfall`. The inventory focus invokes `infantry_spawn_derivative_resolve_opening_local_asset_shortfall`, which removes that temporary idea and sets the resolved flag. No free factory, manpower, equipment, fuel, resource, rail, port, supply, or research grant was found in the opening reconciliation path. Provider custom equipment and obligations remain local ledger/debt entries and are not silently converted into parent stockpile grants.

Starting ideas include `infantry_spawn_derivative_unrecognized_host`, `infantry_spawn_derivative_seized_muster_districts`, `infantry_spawn_derivative_pursued_by_former_state`, and one family/claimant-specific weakness (`infantry_spawn_derivative_claimant_disputed_command`, `infantry_spawn_derivative_zombie_fragmented_command`, `infantry_spawn_derivative_ghost_unstable_manifestation`, or `infantry_spawn_derivative_golem_broken_pattern`). Lifecycle effects remove these ideas on the corresponding route completion and on defeat/final cleanup.

The provider 523 owner census remains exact in `common/script_constants/014_cannibalism_constants.txt` and its provider callback: nine bodies, 7,350 manpower, 990 infantry equipment, and 35 motorized equipment. Its Event 19 use is an owner/provider obligation surface, not a free derivative opening grant.

## Politics, parties, leaders, ideas, focus, and decisions

Derivative setup clears the parent Event 019 participant/evolution runtime, selects neutral politics with elections disabled, applies the validated cosmetic identity, adds the derivative opening ideas, reconciles local assets, and loads `infantry_spawn_derivative_focus_tree`. Claimant archetypes can promote their recorded commander under the archetype ideology; family derivatives use the male commander or institutional council. No separate advisor, high-command, or historical-leader fabrication was found in the dynamic package; this is consistent with the package’s commander/council identity model.

The focus tree source is `infantry_spawn_derivative_focus_tree` in `common/national_focus/019_infantry_spawn_derivative_focus.txt`. The read-only MCP inspect/render/raster pass reports 45 nodes, 54 connectors, zero crossing/connector/intersection blockers, 45 resolved focus titles, and no Event 19-specific missing localisation diagnostic. The only Event 19 diagnostics are nonblocking sibling-anchor deviations for the three ghost family nodes and three golem family nodes. The unrelated `continuous_restrict_freedom_desc` warning belongs to vanilla content. The current file SHA-256 is `e4df35d68962bbc5bd993b96563f7c1a90fb9e2c199608f33bf0b278dbdd01d0`, matching the completed focus audit and its sidecar source hash; the focus source was not modified in this audit.

The 26 derivative decision/mission blocks in `common/decisions/019_infantry_spawn_derivative_decisions.txt` cover collective command, local asset operations, family training/manifestation/binding, paid sustainment, claimant guard, diplomacy, conquered-district missions, former-parent pressure, submission, and claimant preservation/replacement. The seven claimant decisions in `common/decisions/019_infantry_spawn_claimant_decisions.txt` remain separate. Decision costs are either explicit political-power costs or custom cost triggers that debit the relevant manpower, equipment, coal, trains, command power, or ledger resource. State and neighbor targets have target-root and target-trigger guards. GFX, localisation, custom cost text, trigger tooltip, and effect tooltip references are present.

## AI and probability evidence

`common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt` contains self-removing profiles for opening survival, claimant, collective, species, zombie, ghost, and golem route states. The profiles bias defence, supply, garrison, equipment, infrastructure, resource recovery, and preservation without selecting a fixed derivative tag. Decision AI uses the shared derivative AI constants and route-state modifiers.

The mandatory probability route was attempted only as read-only evidence. A successful current focus-source `hoi4.probability_inspect` using `national_focus_ai_will_do` returned 45 candidates, 11 required inputs, zero unresolved inspect inputs, and `poolComplete = false`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01b1a163b6417c6b7e263872a9dbccb54ce4382975c1eb833fc5b1ae42b8dae8/863d1a09245a0dca5371ed0d680736417dcf9b26c6f547945dbe2866ed760819/probability-inspect-2f7d308ed06e.json`. The direct `ai_strategy_factor` inspect discovered no weighted surfaces in the strategy-plan adapter and returned artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a009d754400c897434c58a5195faacc3173b8f216961fa9932621e43dcdb894f/9c189e040c3232798f4fdc0b5e6ea32f3a0c01eaf0aacd17e031fae64cf46309/probability-inspect-5c4de8bd863f.json`.

The current parallel inspect for derivative decisions, claimant decisions, and the custom provider registry returned `INTERNAL_ERROR` from the MCP adapter. The prior Event 019 provider probability handoff records the exact custom-pool limitation: `custom_weighted_pool` cannot discover dynamic provider rows or meta-dispatched callbacks, direct random-list inspection cannot resolve effect-derived temporary weights, and no normalized provider odds, dominance, starvation, or rank-reversal claim is valid. The named `chaosx_ai_probability_auditor` route is not callable in this runtime. No AI weight or probability-bearing source was changed, so no probability compare is claimed.

## Expansion, decline, defeat, annexation, and leakage boundaries

Claimant expansion and family expansion are local to derivative package flags, state targets, paid costs, cooldowns, route prerequisites, and the derivative focus/decision surface. No fixed country tag is created by expansion. Family templates are locked or spawn-only where the provider contract requires it, and zombie, ghost, and golem reinforcement operations charge package resources rather than granting parent-system armies.

Ghost decline runs through `infantry_spawn_derivative_apply_ghost_decline` every 180 days when the cooldown is clear. It chooses an eligible controlled state, applies the base 0.25 percent population fraction, the anchored 0.20 percent fraction, or the managed 0.15 percent fraction, and enforces the 0.50 percent maximum fraction plus hard cap of 5,000 deaths. The ghost provider removes decline flags on cleanup. The unused minimum-floor constant is recorded above as a follow-up; no decline-rate patch was made.

`on_capitulation` records derivative victory/defeat and invokes the local defeat handler. `on_annex` records the winner, migrates retry state, handles defeat if needed, runs proof-gated provider cleanup, and reconciles Event 019 evolution memberships for the remaining parent participants. The final cleanup path proves recorded units, templates, provider additions, and country identity absent; invariant failure sets `infantry_spawn_annex_cleanup_invariant_failure` and queues a retry. `on_subject_annexed` removes evolution memberships without reintroducing derivative identity.

Derivative setup explicitly unregisters Event 019 evolution memberships and clears parent participant flags, ordinary ideas, ordinary missions, and ordinary runtime variables. Shared `on_war`, `on_peace`, release, government-change, and annex reconciliation hooks remain bounded to the parent system’s global participant maintenance; they do not add derivative rows or resurrect a derivative into parent evolution counts. Provider 502 explicitly avoids Death country/soul/evolution/super-event/world-end callbacks, and provider 503 avoids KMB setup/progression. No Event 019 derivative path calls a world-end route, super-event, parent count/stage setter, or evolution stage advancement.

The shared classifiers in `common/scripted_triggers/019_infantry_spawn_triggers.txt` and `common/scripted_triggers/chaosx_dynamic_triggers.txt` distinguish `is_infantry_spawn_derivative_country` from the nonhuman derivative classifier. Claimants clear the nonhuman marker; zombie, ghost, and golem set it only after family validation. The provider setup isolation proof uses `infantry_spawn_parent_event_identity_is_absent` before public derivative additions.

## MCP and source evidence

The current read-only Event Chain Viewer calls used selector `{ kind = event, eventId = chaosx.nr19.1 }` and returned bounded partial analyses because the workspace is large. Useful artifacts are:

- Event lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0a2b5f8bb8a86623d9f7bc7d02c7b8dbad9fe9e40e46f2b5009536412f31ffb/b320a9a6de59ec0ea6c42b1214ac083726a5951fe786f5b21d74fdd7368f1799/event-lint-e8ab707dc24e.json`
- Event overview render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9a87076b79cd41e83cafc50418351f92154c6eb2216f8a9e488227398cda6541/c0ad8ed6de79d7c87b5ecd228e571dc67db36636427ead8a412a3d9dcf9cf00d/event-overview-e8ab707dc24e-manifest.json`
- Event state-flow report: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2260a8683942f74b754c5eec64aa6587a7cd1dc3e31b84c511052febb8266ac5/cbda57c4ab182144f4aa2ea5831a5cb859ad6b93b4ba1e723271f04d5b4724b4/event-state_flow-e8ab707dc24e.json`
- Event trace report: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9b6d9e12e18b62f5158f99f5ec46a0384aa7ce3ba99b0910ec138e9d3db6810/3a3272c38cae6a33dab257469bdd99e6188c1d3aefef4dd15d5f8e9f8b9834f9/event-trace-e8ab707dc24e.json`
- Focus render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/438c566f51ad1667944129ec4a9bd113e5870b15148fcc35619fd0f6bcaa99ac/1b54c77093ca8f088e7f945191a24cab0520b147fe045a214ab01c4900cf83fd/infantry_spawn_derivative_focus_tree.focus.svg`
- Focus raster PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b73666a3eda6c67ec83c7fc4f2f7761af2c22c8046195364f07dcac70cde0b9/ae4811ff03d49c9b3318cb3f896a2ace0a0271feb300e07acb6b16963aca9d08/infantry_spawn_derivative_focus_tree.focus.png`

The Event Viewer reports `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` with deferred workspace-wide helper/lifecycle projections but zero blocking diagnostics in the bounded result. The focus Viewer reports validation passed with only the two nonblocking sibling-anchor warning groups described above. No Event Viewer or focus rewrite was used.

Before source review, the required offline wiki pages were consulted from `paradox_wiki/`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding, Equipment modding, Division modding, Character modding, and Map modding. Vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation` was consulted for dynamic country, event, effects, triggers, script constants, divisions, and AI precedent. Vanilla comparisons used `history/units/DTH_1936.txt`, `history/units/ZZZ_1936.txt`, and the KMB setup in `common/scripted_effects/005_soviet_collapse_effects.txt:22189`.

## Remaining blockers, simplifications, and skipped validation

- The mandatory `chaosx_ai_probability_auditor` route is unavailable as a callable subagent/tool in this runtime. Direct MCP source inspection is retained as evidence only; no normalized AI decision, focus-selection, provider-family, random-list, dominance, starvation, or timing claim is made.
- Current direct probability inspection of derivative decisions, claimant decisions, and the custom provider registry returned `INTERNAL_ERROR`; the prior Event 019 probability handoff’s incomplete-pool artifacts remain the authoritative limitation record.
- The installed package exposes no Technology Tree Viewer. Event 019 has no derivative technology tree source in the audited package, so no technology completion claim is made.
- No map rewrite was requested or performed. Dynamic state ownership/control arrays and runtime capital selection remain parent-scope map validation; no fixed state or fallback tag was introduced by this audit.
- Event lint/render are bounded partial workspace analyses with deferred helper/lifecycle projections. Their linked artifacts are useful structural evidence but are not a live HOI4 launch or consumer-validation result.
- Live HOI4 execution was skipped per repository instructions; the user owns live in-game validation.
- The only source-level follow-up found in this package is the unused ghost decline minimum-floor constant at `common/script_constants/019_infantry_spawn_derivative_package_constants.txt:247`. The localisation filename spelling and historical/provider-extension manifest gate are hygiene/documentation follow-ups, not runtime fallbacks.

No fixed country tag, fixed-tag fallback, free derivative army, free equipment grant, opposite-gender claimant pairing, parent evolution count increment, parent stage advancement, Death/KMB progression import, world-end route, super-event route, or map mutation was introduced or accepted by this audit.
