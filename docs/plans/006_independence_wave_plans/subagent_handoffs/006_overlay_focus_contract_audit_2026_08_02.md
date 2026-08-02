# Event 006 overlay focus-contract audit

Status: **blocked; no safe source-level patch in the scoped overlay files**.

Audit date: 2026-08-02.

This handoff covers IW-022, IW-025, IW-035, IW-059, IW-085, IW-101, IW-102, IW-105, IW-156, IW-196, IW-197, and IW-204.

## Decision

The scoped overlays must not call `load_focus_tree` and must not be admitted as additive carriers by flag alone.

`shared_focus` is a static import on the owning `focus_tree` definition, as documented by `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md` and the vanilla focus-tree files.

`common/scripted_effects/006_independence_wave_focus_effects.txt` explicitly uses `load_focus_tree` only for the full framework and never for additive overlays.

Vanilla `effects_documentation.md` documents `load_focus_tree` as changing the country's current tree, with `keep_completed` retaining only completed IDs that also exist in the replacement tree.

The only reviewed additive owner is the mod-owned `iceland_tree` in `common/national_focus/iceland.txt`.

None of the scoped route adapters imports `independence_wave_overlay_take_stock_of_independence`, registers `independence_wave_focus_carrier_registered`, or calls `independence_wave_assign_focus_framework`.

Adding those flags without a static import would satisfy a validator while exposing no Event 006 focus nodes to the player.

Adding `load_focus_tree = { tree = independence_wave_focus_tree ... }` would erase or replace a living carrier tree and violates `docs/events/006_independence_wave/systems/generic_focus_tree.md` and the accepted closure in `docs/plans/006_independence_wave_plans/006_generic_focus_contract_closure_handoff_2026_08_02.md`.

Therefore no gameplay file was patched in this audit.

## Contract evidence

- `common/national_focus/006_independence_wave_focus.txt:27` defines the single generic `independence_wave_focus_tree`.
- `common/national_focus/006_independence_wave_focus.txt:46` statically imports `independence_wave_overlay_take_stock_of_independence` into that tree.
- `common/national_focus/006_independence_wave_focus.txt:3177-3424` defines the overlay root and its dependent shared focuses.
- `common/scripted_effects/006_independence_wave_focus_effects.txt:29-78` implements the full/additive assignment split; the additive branch only records flags after a reviewed carrier trigger succeeds.
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-77` accepts either a loaded full tree or an additive carrier proved by `can_attach_independence_wave_additive_focus_carrier`.
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt:70-77` currently proves only the `independence_wave_focus_carrier_registered` plus `independence_wave_ice_lifecycle_initialized` and `has_focus_tree = iceland_tree` combination.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:52` rejects a package without the common focus contract.
- `rg` over all seven scoped effect files found zero focus-contract tokens in executable source.
- Repository-wide `rg` found the generic overlay root imported only by `006_independence_wave_focus.txt` and `common/national_focus/iceland.txt`.

## Country-package coverage checklist

| Package | Route identity and focus-owner surface | Map and state contract | Focus disposition |
| --- | --- | --- | --- |
| IW-022 | `is_independence_wave_iw022_dalmatia_route_active`; dynamic country, `original_tag = CRO`, `has_cosmetic_tag = dalmatia`; possible runtime owner is the carrier's vanilla/default tree, not a mod-owned tree | State 103 anchor, optional Zara state 163, state 103 guard; D01-D50 daily hooks | No static import or carrier receipt; retain the current overlay-only route |
| IW-025 | `is_independence_wave_iw025_vojvodina_route_active`; dynamic country, `original_tag = HUN`, `has_cosmetic_tag = vojvodina`; HUN's source precedent is `common/national_focus/hungary.txt` `hungarian_focus`, but the Dxx runtime owner is not source-registered | State 45 anchor and guard; D01-D50 daily hooks | No static import or carrier receipt; retain the current overlay-only route |
| IW-035 | `is_independence_wave_iw035_livonia_route_active`; `tag = LIT`, `has_cosmetic_tag = LIVONIA`; vanilla owner is `common/national_focus/lithuania.txt` `lithuania_tree` | State 12 or 191 anchor; state 12/191 ownership and control checks | Meaningful Lithuanian tree remains authoritative; no safe additive import exists yet |
| IW-059 | `is_independence_wave_iw059_mesopotamia_route_active`; `has_cosmetic_tag = neo_mesopotamia`, `neo_mesopotamia_formed_flag`, originals `KUR IRQ SYR PAL EGY KUW LEB ASY`; formable source is vanilla `neo_mesopotamia_decision` | State 291 anchor and guard | Multiple possible original-tree owners and post-formation identity; no single reviewed carrier contract |
| IW-085 | `is_independence_wave_iw085_cyrenaica_route_active`; `original_tag = LBA`, subject of ITA, fascist, satellite/dominion | Adapter anchor/guard is state 663; existing planner reservation metadata still mentions states 450/451/663 | Research-gated overlay; no carrier registration or focus import |
| IW-101 | `is_independence_wave_iw101_kongo_route_active`; `original_tag = COG`, `COG_kingdom_of_kongo` cosmetic, `COG_kingdom_of_kongo_flag` | State 538 anchor and guard | Vanilla `common/national_focus/congo.txt` `congo_focus` must remain intact |
| IW-102 | `is_independence_wave_iw102_kuba_route_active`; `original_tag = COG`, `COG_kingdom_of_kuba`, `COG_kingdom_of_kuba_flag` | State 538 anchor and guard | Same meaningful `congo_focus` owner; no additive import |
| IW-105 | `is_independence_wave_iw105_loango_route_active`; `original_tag = COG`, `COG_kingdom_of_loango`, `COG_kingdom_of_loango_flag` | State 538 anchor and guard | Same meaningful `congo_focus` owner; no additive import |
| IW-156 | `is_independence_wave_iw156_tne_route_active`; `original_tag = TNE`, democratic, non-subject, owns/controls state 668 | State 668 anchor and guard | TNE has no Event 006-owned focus source; preserve its installed/default tree until a carrier owner is explicitly reviewed |
| IW-196 | `is_independence_wave_iw196_antilles_route_active`; originals `HAI DOM PUE CUB JAM BAH GDL BAS`, `antilles` cosmetic, `antilles_formed_flag` | One of states 689, 691, 692, 694 as owned/controlled anchor | Formable can retain different original trees; no single static additive owner |
| IW-197 | `is_independence_wave_iw197_mapuche_route_active`; `original_tag = CHL`, `CHL_mapuche_state` cosmetic | State 950 anchor and guard | Vanilla `common/national_focus/chile.txt` `chilean_focus_tree` remains authoritative |
| IW-204 | `is_independence_wave_iw204_araucania_route_active`; `original_tag = CHL`, `kingdom_of_araucania_and_patagonia` cosmetic, `CHL_chile_is_a_monarchy` flag | State 512 first, state 507 second, ownership/control guard | Same meaningful `chilean_focus_tree` owner; no additive import |

## File-surface checklist

### Reviewed route source files

- `common/scripted_effects/006_independence_wave_iw022_dalmatia_effects.txt` and `common/scripted_triggers/006_independence_wave_iw022_dalmatia_triggers.txt`.
- `common/scripted_effects/006_independence_wave_iw025_vojvodina_effects.txt` and `common/scripted_triggers/006_independence_wave_iw025_vojvodina_triggers.txt`.
- `common/scripted_effects/006_independence_wave_iw035_livonia_effects.txt` and `common/scripted_triggers/006_independence_wave_iw035_livonia_triggers.txt`.
- `common/scripted_effects/006_independence_wave_iw059_mesopotamia_effects.txt` and `common/scripted_triggers/006_independence_wave_iw059_mesopotamia_triggers.txt`.
- `common/scripted_effects/006_independence_wave_iw085_cyrenaica_effects.txt` and `common/scripted_triggers/006_independence_wave_iw085_cyrenaica_triggers.txt`.
- `common/scripted_effects/006_independence_wave_iw101_iw102_iw105_cog_overlays_effects.txt` and `common/scripted_triggers/006_independence_wave_iw101_iw102_iw105_cog_overlays_triggers.txt`.
- `common/scripted_effects/006_independence_wave_iw156_iw196_iw197_iw204_overlays_effects.txt` and `common/scripted_triggers/006_independence_wave_iw156_iw196_iw197_iw204_overlays_triggers.txt`.

### Related consumers checked

- Route-specific `common/on_actions/006_independence_wave_*_on_actions.txt` files run narrow carrier hooks and do not assign a focus framework.
- Route-specific decisions and decision categories provide the visible overlay surfaces and missions.
- Route-specific ideas provide lifecycle state; IW-059 and IW-085 use broad `allowed = { always = yes }` idea gates pending stronger package admission.
- Route-specific localisation covers current decisions, missions, ideas, and tooltips; no focus localisation or icon addition was required because no focus node was added.
- `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/iceland.txt`, the central assignment effects/triggers, and the package-dispatch validator are the only relevant focus-contract surfaces.

## Missing or stale surfaces

- No scoped owner tree contains `shared_focus = independence_wave_overlay_take_stock_of_independence`.
- No scoped route calls `independence_wave_assign_focus_framework`.
- No scoped route sets `independence_wave_focus_carrier_registered`.
- `can_attach_independence_wave_additive_focus_carrier` has no reviewed branch for any scoped route.
- There is no dynamic `add_shared_focus` effect that could safely inject the generic nodes into an already-loaded tree.
- A flag-only extension would be a false contract because `has_independence_wave_generic_focus_contract` would pass while the player still sees no generic overlay branch.
- A runtime `load_focus_tree` extension would be a tree replacement, not an overlay, and is rejected by the accepted generic-tree contract.

## Map and state setup issues

- IW-022 uses state 103 as its anchor and guard, with optional Zara state 163; the dynamic Dxx ownership/control proof remains the route's safety boundary.
- IW-025 uses state 45 as its anchor and guard.
- IW-035 accepts state 12 or 191 for the Livonia anchor.
- IW-059 uses state 291 as its anchor and guard.
- IW-085's adapter uses state 663, while prior reservation/planner metadata still mentions states 450/451/663; this mismatch must be reconciled before admission or a focus carrier review.
- IW-101, IW-102, and IW-105 share state 538 as their Kongo-region anchor and guard.
- IW-156 uses state 668, IW-196 uses one of 689/691/692/694, IW-197 uses state 950, and IW-204 uses states 512/507.
- No map rewrite was attempted because focus ownership is unresolved and the parent scope owns any map write with dry-run/review/apply/post-validation evidence.

## Politics, leaders, portraits, flags, advisors, and parties

- These adapters preserve existing carrier politics, leaders, portraits, party setup, and advisor surfaces.
- IW-022, IW-025, IW-035, IW-059, IW-085, and IW-101/102/105 are identity- or host-gated overlays rather than new tags.
- IW-156 relies on the installed TNE identity contract (`original_tag = TNE`, democratic, non-subject, state 668); no unverified cosmetic name was invented.
- IW-196 relies on the vanilla Antilles formable identity and original-tag allowlist; no new flag or leader was created.
- IW-197 and IW-204 reuse Chile's existing identity, leaders, flags, and `chilean_focus_tree`.
- No new portrait, flag, advisor icon, party, leader, or council asset is needed for this focus-contract audit.
- IW-085 remains research-gated and should not be treated as a fully sourced historical identity until the existing source and state-anchor blockers close.

## Focus, decision, idea, and asset issues

- The generic focus root and overlay chain exist in `common/national_focus/006_independence_wave_focus.txt`, but those nodes are only visible to trees that statically import the root.
- The current route decisions, missions, and lifecycle ideas remain valid overlay surfaces and are not replaced by a focus tree.
- No focus IDs, focus localisation keys, focus icons, decision icons, idea icons, or `.gfx` registrations were added or changed.
- The required next focus work is owner-tree integration review, not another generic-tree definition and not a country-specific tree.
- For each future carrier, a safe implementation must add a static shared-focus import to a mod-owned copy/override of the owner tree, prove layout coordinates, register a carrier receipt, and bind the receipt to the exact route identity.

## Starting military, technology, industry, supply, and production

- No starting army, navy, air force, template, equipment, manpower, technology, research slot, production line, convoy, train, fuel, supply, rail, port, resource, or building setup was changed.
- These overlays intentionally operate on the existing carrier setup and use route costs, ideas, and missions instead of standalone country starts.
- Any future generic-focus assignment must preserve the carrier's current starting setup and completed focus IDs; a replacement tree cannot be accepted merely because it keeps some completed IDs.

## AI and playability

- The inspected adapters expose route decisions, timed guard missions, narrow daily refresh hooks, suspension/resumption, and lifecycle idea changes.
- They do not provide focus-selection AI for the generic Event 006 tree because no generic focus tree is assigned.
- AI survival, focus completion, save/load continuity, post-formation ownership, and scenario coverage remain unproven in live play and are outside this source-only audit.
- Treating these routes as admitted full-framework packages before a focus disposition is selected would overstate playability.

## Validation evidence

- `python -B .tools/audit_event6_allocator.py` completed successfully with `Event 006 allocator audit passed` and the repository's current publisher, reservation, scenario, and ordering counts.
- A source scan over all seven scoped effect files found zero executable focus-contract tokens.
- A repository scan found the generic overlay root imported only by `006_independence_wave_focus.txt` and the mod-owned `iceland.txt` tree.
- Vanilla precedents inspected include `yugoslavia.txt`, `hungary.txt`, `lithuania.txt`, `iraq.txt`, `congo.txt`, `chile.txt`, `generic.txt`, and `iceland.txt`.
- Required offline wiki pages and vanilla documentation for focus trees, effects, triggers, data structures, and localisation were consulted before this audit.
- Hearts of Iron IV was not launched, and no in-game, save/load, AI, MCP geometry, or live consumer validation is claimed.

## Recommended next implementation tranche

Choose one of the following explicitly before changing the central carrier trigger.

1. **Decisions-only disposition.** Keep these route overlays fail-closed for the generic focus contract and document that their decisions, missions, ideas, and identity surfaces are the complete Event 006 interaction for the current release.
2. **One-carrier owner-tree tranche.** Select one route with a stable owner tree, copy/override that vanilla tree under the mod's ownership, add the static generic overlay import at a reviewed coordinate region, register a route-specific carrier receipt, bind the additive assignment to that receipt, and run source plus focus geometry validation before considering another carrier.

The first candidate should be selected only after resolving whether the carrier is a stable tag or a dynamic/formable identity.

IW-035 (`LIT`/`lithuania_tree`), IW-101/102/105 (`COG`/`congo_focus`), and IW-197/204 (`CHL`/`chilean_focus_tree`) have clear owner-tree precedents but still require mod-owned static import and geometry review.

IW-022, IW-025, IW-059, IW-085, IW-156, and IW-196 require identity, formable, host, or runtime-owner review before they can be carrier candidates.

Do not extend `can_attach_independence_wave_additive_focus_carrier` to any of these routes until the owner-tree import exists and a source-level carrier receipt proves it.

## Simplifications, omissions, and blockers

- No source gameplay patch was made because every apparent patch either flag-gates nodes that are not statically imported or replaces a meaningful/current carrier tree.
- No new tags, histories, focus trees, leaders, portraits, flags, advisors, focus icons, decision icons, or idea icons were created.
- No map changes were made.
- The generic Event 006 tree remains complete only for its existing full-framework assignments and the reviewed ICE additive carrier.
- This handoff does not claim package admission, live playability, AI completion, save/load continuity, or formable completion for the twelve scoped overlays.

