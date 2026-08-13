# Event 019 country-package independent audit

> **Parent closure update (2026-07-16):** The two follow-ups identified by this
> dated audit are implemented. The normal region contract now prefers mainland
> states and permits a controlled, passable, non-capital island only when the
> parent has no viable mainland base; an exact loyal origin replaces an unsafe
> claimant-headquarters anchor without transferring the parent capital. The
> dedicated neutral unassigned muster scene also replaces all three generic
> portrait fallthroughs. A newer registry/scenario specialist audit owns the
> independent recheck of these changes; the historical body below is retained
> unchanged as discovery evidence.

**Date:** 2026-07-16  
**Mode:** independent live-source audit; no gameplay, localisation, workbook, or asset edits  
**Scope:** claimant takeover/failed coup/revolt, the three natural-release modes, exact recorded-formation transfer, dynamic derivative identity and content, one-state and microstate safety, parent isolation, defeat and annex cleanup, and the latest army/host portrait requirement

## Disposition

- The live country package is structurally complete across claimant and zombie/ghost/golem derivative identity, leaders, ideas, focus content, decisions, AI, diplomacy, wars, expansion, defeat, and proof-gated annex cleanup.
- The exact-transfer P0 found during this audit is closed in the live source. `infantry_spawn_prove_natural_derivative_source_commit_ready` had required an active claimant in claimant-independent family mode; the exact-transfer owner corrected the guard so the claimant count is required only for ordinary or anomalous claimant releases.
- One gameplay P1 remains deliberately unpatched: every natural multi-state release rejects island states, so an all-island multi-state country cannot use the specification's permitted "only viable base" exception. Repository policy requires fallback design to be discussed with the user; the parent explicitly directed this auditor not to patch that path.
- One latest-portrait-requirement follow-up remains outside this country-package edit boundary: two claimant portrait selector fallthroughs and the Muster Board's initial sprite still use `GFX_portrait_unknown`. The parent is reserving a separate agent slot for a dedicated neutral Event 19 army/muster asset and wiring pass. No false claimant or improvised raster substitution was made here.
- Open severity after the live exact-transfer correction: zero P0, one gameplay P1, zero country-package P2. The neutral portrait work is a separate user-override compliance item owned by the parent.

The country package should not receive a full completion claim until the island-only natural-release behavior is approved and resolved. No other country-package blocker was found.

## Finding: island-only natural release remains unavailable

The relevant live gates are in `common/scripted_triggers/019_infantry_spawn_triggers.txt`:

- `infantry_spawn_natural_claimant_release_base_is_safe` requires a controlled, non-capital, non-island owned state.
- `infantry_spawn_natural_family_dynamic_release_base_is_safe` repeats the same requirement.
- `infantry_spawn_natural_derivative_revolt_state_is_safe` categorically rejects `is_island_state = yes`, so the region builder cannot use an island even when no mainland state exists.

Consequences:

- A mature claimant crisis in an all-island multi-state host reaches the natural transaction, fails region preflight, and resolves through the existing visible failed-coup branch.
- A claimant-independent family breach in the same geography fails preflight and receives the visible deferred-containment outcome (`chaosx.nr19.206`).
- No zero-state actor, unproved deletion, or silent transaction residue is created.

This is safe but does not implement the specification in `019_infantry_spawn_spec_part_6_derivative_countries.md`, which says isolated islands should be avoided **unless geography or scenario setup makes them the only viable base**. The narrow remediation would be a two-tier geography contract: prefer the current non-island set, then permit a coherent island base only when the parent has no eligible non-island release state. That is explicitly a fallback and was not authorized in this tranche.

## Exact recorded-formation transfer

### Three release modes

The live router freezes and proves three distinct modes:

1. **Ordinary claimant:** Evolution III; a valid claimant; exact claimant-loyal Event 19 rows; no family requirement.
2. **Anomalous claimant:** Evolution IV; a valid claimant plus a complete provider row; exact union of claimant-loyal and selected-family rows.
3. **Independent family:** Evolution IV; no claimant requirement; exact claimant-free rows of one selected family. A one-controlled-state source uses the verified same-tag provider takeover when its entire live army is exactly that frozen family set.

All multi-state paths use `create_dynamic_country = { original_tag = THIS }`. There is no fixed derivative output tag. Provider checks such as `tag = KMB` are input eligibility context only.

### Destination proof precedes source deletion

`infantry_spawn_run_natural_derivative_exact_transaction` performs this live order:

1. Freeze mode, claimant/provider identity, connected region, selected state array, unit UIDs, delete cohorts, generation/lot/template manifests, obligations, auxiliary membership, and global accounting.
2. Stage source rows without deleting divisions or committing accounting.
3. Create the dynamic actor, transfer only the frozen region, build its private ledger and replacement army, and prove territory, capital, cores, exact UID/cohort cardinality, template/lot/generation identity, obligations, claimant/provider identity, and aligned ledgers.
4. Re-prove unchanged global Event 19 accounting.
5. Only after actor and global proofs pass, call `infantry_spawn_delete_and_prove_natural_derivative_source_set`.
6. Prove zero matching source UIDs/cohorts and the exact source division-count delta.
7. Prove commit readiness, snapshot expected accounting, commit source ledger history once, prove it, install public identity and former-parent war, then repeat final actor/source/territory/global proofs before unlocking.

The source deletion is exact frozen cohort deletion with `disband = no`; it is not a ratio, blanket troop transfer, ordinary-army scan, or random replacement. A post-accounting mismatch locks both sides and never enters the pre-commit rollback.

### Recovery

Pre-commit recovery removes and proves absent the provisional actor's exact replacements, removes provisional cores, annexes the unpublished actor with troop transfer disabled under a narrow listener bypass, proves all selected territory returned, and recreates only missing frozen source UIDs before rebinding and proving their original rows. Locks clear only after the complete source set and global accounting snapshot are restored and proved.

The independent-family commit guard now correctly reads: active divisions must cover the frozen transfer set in every mode, while active-claimant cardinality is required only when the frozen mode is not `independent_family`.

## Claimants, leaders, and government identity

- Non-microstate claimant crises route into the exact natural revolt transaction.
- Microstates route to claimant takeover or failed coup and never create a zero-state country.
- A living Event 67 Generalissimo conflict forces the failed-coup branch instead of silently displacing that leader.
- All generated claimant commanders explicitly use `female = no`; destination claimant proof also requires exactly one matching leader with `is_female = no`.
- All three one-person family leaders explicitly use `female = no`.
- The 20 claimant profiles expose four reviewed regional male name variants each. The player-facing 80-name set is male.
- Zombie, ghost, and golem councils use institutional names and collective host-scene sprites. HOI4's documented country-leader surface has no neutral gender value; omission of `female` is therefore the package's genderless presentation contract rather than a claim that the engine stores a third sex.

An anomalous claimant is intentionally classified as a nonhuman family derivative with the claimant UID preserved for the ruler and claimant route. Ordinary claimant breakaways retain claimant classification and family `none`.

## Regional and species identities

The public identity contract is complete and fail-closed:

- seven regions: Europe, Middle East, Africa, Asia, Australia, North America, and South America;
- thirteen identity stems: claimant breakaway plus base, claimant, collective, and species identities for zombie, ghost, and golem families;
- 91 reachable regional cosmetic tags (`13 x 7`);
- 1,365 required regional base/DEF/ADJ plus four-ideology localisation keys, with zero missing;
- 104 normal, 104 medium, and 104 small TGA flags: the 91 regional identities plus 13 base identities, with exact filename parity across all three sizes.

`infantry_spawn_derivative_classify_origin_region` fails closed when the capital has no supported continent, and `infantry_spawn_derivative_apply_cosmetic_identity` executes only for valid region and identity enums. There is no generic cosmetic-tag fallback.

## Package content and lifecycle

### Content surface

- **Focus tree:** 45 focus definitions: 30 shared and five each for zombie, ghost, and golem overlays. Each family sees a 35-focus surface before route/doctrine exclusions. Claimant, collective, and species roots are mutually exclusive; downstream availability accepts the intended alternatives.
- **Decisions and missions:** 26 definitions covering governance, depots and sustainment sites, claimant guard, zombie training/rally, paid ghost/golem formations, family sustainment, family diplomacy, district integration, fragmentation, former-parent operations, submission, claimant continuity, and opening survival.
- **Ideas:** 42 definitions covering starting weakness, route/doctrine replacements, sustainment and outward growth, and defeated remnants.
- **AI:** self-removing derivative-only profiles adapt to family, route, governance, opening restraint, production, construction, garrison, diplomacy, and regional aggression. No fixed tag selects a derivative AI profile.

Every focus, decision/mission, and idea definition has both name and description localisation. All 58 unique focus/decision icon references resolve in the mod interface.

### Wars and expansion

- A proved multi-state derivative declares war on its stored former parent as the final locked setup step.
- A verified one-state family takeover clears former-parent surfaces and does not declare war on itself.
- Expansion targets exclude Event 19 derivatives, special Chaos countries, actual nonhuman countries, capitulated countries, existing war/NAP/wargoal conflicts, and targets outside the configured controlled-state band.
- Regional Predator and outward-muster progression require the package's own route, sustainment, integration, and war-win evidence rather than parent-event progress.

### Starting weakness and parent isolation

- Zombie derivatives expose only the base zombie battalion and begin with fragmented command; no mutation, league, global outbreak, super-event, or world-end surface is called.
- Ghost derivatives expose only `death_weak_ghost_host`, retain spawn-only recruitment, and use slow local decline rather than Death's soul, rapid-consumption, continent, super-event, or world-end systems.
- Golem derivatives expose only the two-battalion coal-golem template, remain spawn-only, and never call Kuznetsk Mining Board country setup, progression, endgame, or super-events.
- `is_infantry_spawn_derivative_country` is registered into `is_special_chaos_country`; nonhuman derivatives are registered into `is_actual_nonhuman_country`, which also excludes them from normal civilian systems.
- `infantry_spawn_derivative_clear_parent_runtime_surface` removes ordinary Event 19 evolution, claimant-management, scenario, and Muster Board state before private package setup. Derivatives do not receive `infantry_spawn_participant` and do not advance ordinary Event 19 history.
- The derivative package, focus, decision, and AI surfaces contain no `world_end` reference.

## Defeat and cleanup

- `on_capitulation` records the winner and applies defeat once. It disables the active package and decisions, cancels missions/projects, removes active route/family ideas, installs family-appropriate remnant penalties, and dispatches one claimant or family defeat report.
- `on_annex` migrates any cleanup queue owned by the defeated country before invoking final cleanup.
- Final cleanup first freezes the exact tracked UID/cohort/template set. It destroys only proven tracked formations, proves all target UIDs absent, deletes and proves the tracked templates absent, and only then clears private ledgers, state markers, claimant roles, ideas, missions, flags, variables, cosmetic identity, and package classification.
- State-marker removal is bounded by the package-owned state array and matching package-owner UID.
- Failure retains the identity and frozen set, marks the invariant, and queues the exact annexed country scope on the annexer. The persistent queue retries one country at a time, removes no entry without the real completion flag, and migrates again if its current annexer is annexed.
- No daily, weekly, monthly, world-country, or recurring global cleanup scan was introduced.

## Scenario SCN-013 authority portrait audit

The parent's live `GetInfantrySpawnScenarioActorArmyScene` selector and `infantry_spawn_scenario_install_actor_government` wiring are correct for the latest government-leader replacement:

- zombie, ghost, and golem governments select their family council host scenes;
- Arsenal Lottery and General Mutiny select Event 19 army/muster scenes;
- Anomalous Rising selects a ghost host scene;
- the current default selects claimant slot 01, which is an army/muster scene;
- completed nonhuman derivatives and General Mutiny claimant identity are excluded from generic government overwrite where their own identity must survive.

Every referenced sprite in that selector points to one of the reviewed Event 19 army/host scenes. No asset was edited in this audit.

The broader latest override is not fully closed because these older neutral fallthroughs remain live pending the parent's dedicated neutral asset pass:

- `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`: `GetInfantrySpawnClaimantPortraitSprite` default;
- the same file: `GetInfantrySpawnSelectedClaimantPortraitSprite` default;
- `interface/019_infantry_spawn_muster_board.gui`: initial `infantry_spawn_muster_claimant_portrait` sprite.

All three currently use `GFX_portrait_unknown`. Replacing them with a false claimant/profile scene would satisfy the visual category while misrepresenting identity, so this auditor left them untouched for the dedicated neutral army/muster asset.

## Structural evidence

- 45 focuses, 26 decisions/missions, and 42 ideas: zero missing name/description localisation.
- 58 unique focus/decision icon tokens: zero missing from mod interface definitions.
- 91 regional cosmetic tags: zero missing among 1,365 required localisation variants.
- 312 Event 19 derivative flag files: 104 per size with exact filename parity.
- 983 Event 19 `infantry_spawn_*` scripted-effect definitions across the live effect set: zero duplicate definition names.
- 329 `infantry_spawn_*` and six `is_infantry_spawn_*` scripted-trigger definitions: zero duplicate definition names.
- 2,873 keys in the Event 19 English localisation file: zero duplicate keys.
- 48 `chaosx.nr19.*` event IDs: zero duplicate IDs.
- Fixed-output scan found only dynamic actor creation with `original_tag = THIS`; fixed tags occur only in provider/parent isolation eligibility context.
- Package-surface scan found no `world_end` reference.

Both `hoi4.focus_inspect` and narrow `hoi4.event_inspect` lint were attempted. The shared HOI4 MCP server returned `ARTIFACT_STORAGE_LIMIT` before scanning, so no MCP diagnostic result is claimed.

## Files changed by this auditor

- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_country_package_independent_audit_2026_07_16.md`

The exact-transfer owner separately changed the live commit-readiness guard described above. This auditor reviewed that result but did not edit the shared gameplay file.

## Skills and references used

- `chaos-redux-subagents` for independent ownership, coordination, severity reporting, and handoff placement.
- `chaos-redux-events` for Event 19 integration, identity, logs, evolution, documentation, and completion standards.
- `chaos-redux-focus-trees` for focus route, reachability, AI, reward, and lifecycle review.
- `chaos-redux-decisions-missions` for decision/mission visibility, target, cancellation, cost, AI, and cleanup review.
- Required offline Paradox wiki pages, including the core scripting pages plus country creation, national focus, and division references.
- Current vanilla HOI4 effects, triggers, script concepts, script constants, dynamic variables, and AI documentation, plus dynamic-country/unit-transfer/civil-war precedents.

## Simplifications, omissions, and blockers

- No fallback, simplification, fixed-tag substitute, random formation, unproved source deletion, or silent content omission was introduced.
- The approved exact recreate/prove/delete transaction necessarily preserves recorded Event 19 identity, issue manifest, starting factors, and obligations rather than unsupported live organization, veterancy, decorations, army assignment, exact current manpower fill, or exact per-equipment composition. That engine-constrained contract is already documented in the exact-transfer handoff.
- The island-only natural-release exception remains unimplemented pending explicit approval of its fallback semantics.
- Neutral Event 19 authority art remains a separate parent-owned asset/wiring follow-up; this audit produced no raster or sprite fallback.
- The HOI4 MCP artifact-retention limit prevented focus/event inspector output.
