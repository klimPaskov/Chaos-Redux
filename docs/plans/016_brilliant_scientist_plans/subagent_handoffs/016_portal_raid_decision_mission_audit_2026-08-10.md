# Event 016 Portal Warfare decision and mission audit

Date: 2026-08-10

Owner: `event16_portal_raid_decision_audit`

Scope: native Portal Warfare raids, their category and scripted triggers/effects, Kruger portal-transit fabrication and terminal decisions, Black Plague access coupling, localisation/GFX references, and weighted AI evidence.

## Changes applied

- `common/raids/016_brilliant_scientist_portal_raids.txt`: replaced four invalid `destroy_unit = THIS` division effects with the native scalar `destroy_unit = yes` in success and critical outcomes for both raids. The selected six-battalion formation is therefore consumed once before the beachhead reconstruction and cannot be retained as a free duplicate.
- `common/raids/016_brilliant_scientist_portal_raids.txt`: added exact-facility `damage_building = { tags = facility ... province = var:ROOT.target_province }` effects to limited, success, and critical outcomes. The state-targeted raid keeps the state-level damage helper.
- `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`: special-project extraction branches now require the selected `var:ROOT.target_province` to contain the matching facility family before removal. Facility, reactor, and rocket destinations use `random_owned_controlled_state`; destination checks require actor control, so an occupied-owned state cannot consume a source without a valid reconstruction location.
- `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt`: added the exact province facility check and matched all reactor, rocket, and special-facility destination checks to controlled actor states. This keeps availability and effect-time destination gates aligned.

No model, entity, action, sound, fallback, or new scripted-GUI wiring was added.

## Severity-sorted findings

### Critical, fixed

The previous `destroy_unit = THIS` was not the scalar native division-effect form used by vanilla raids. It could leave the assigned division alive while `brilliant_scientist_portal_raid_establish_beachhead` created a reconstructed cadre, producing a repeatable free-unit, manpower, and equipment loop. The four outcome blocks now use `destroy_unit = yes`.

### High, fixed

The exact building raid selected a province but the extraction resolver could branch from aggregate state building counts and remove a different facility family, or remove no selected source while still recording a transfer. Matching source-province guards now require the selected province to contain the family being removed.

The effect-time destination scopes previously used random owned states while the availability gates could pass occupied-owned states. Reactor, rocket, and facility reconstruction now use controlled-state checks and `random_owned_controlled_state`; the trigger gates were updated to the same rule.

Exact-facility limited/success/critical outcomes previously called only the state-level damage helper. Direct province-targeted facility damage is now present in all three exact-facility outcomes. If the facility was successfully extracted first, the direct damage is naturally a no-op and the existing state-level damage remains the secondary consequence.

### Medium, remaining

The exact-facility destination rule requires a controlled actor state with all four special-facility families below one, not merely the requested family. This can hide valid raids when a family-specific destination exists beside another special facility. It is conservative and prevents invalid construction, but should be reconsidered as a balance/usability decision rather than silently broadened here.

Both raids declare `portal_raider = { min = 6 }` without a native maximum. The locked `Quantum Transit Raiders` template contains exactly six battalions, and the rebuild is exactly that template, but a custom formation containing more than six qualifying battalions could pass the native requirement. No vanilla exact-max precedent was found; this remains an engine-contract risk for parent review.

Beachhead creation changes the selected province controller and creates a full-factor `Quantum Transit Raiders` cadre. The source division is destroyed by the native outcome block, but `start_equipment_factor = 1.00` and `start_manpower_factor = 1.00` can still grant a substantial reconstruction payload. This is part of the accepted Portal Warfare design, but is a balance surface to test in a live save.

`brilliant_scientist_portal_beachhead_active`, `brilliant_scientist_portal_raid_breach_recorded`, `brilliant_scientist_portal_raid_targeted`, and extraction state flags are persistent. A repository search found no Event 016 cleanup or expiry consumer for these flags; later containment/spread work must clear stale state if that lifecycle is intended.

Heavy target damage intentionally calls the light helper and then a heavy pass, so the same highest-priority surviving state building can receive both applications. This is not a duplicate reward, but it should be documented if the intended meaning is damage to distinct facilities.

### Low

Native raid cancellation and cooldown are engine-owned. The source uses seven preparation days, thirty re-enable days, `fire_only_once = no`, reservation of sixty Teleportation Equipment, and explicit cancellation when actor readiness or target validity is lost. The exact-facility target helper now also rejects a stale target province with no facility.

## Decision category and native raid lifecycle

`brilliant_scientist_raids` is registered in `common/raids/categories/chaosx_raid_categories.txt` with army intelligence and `free_targeting = yes`; the category gate requires the portal weaponization technology and ready Portal Raider template. Both raid types are visible through the technology gate, show a custom target tooltip, require a valid hostile target and ready actor, require an existing war at launch, and cancel if either side becomes invalid. The state raid targets a hostile controlled state containing factories, reactors, or rocket sites. The companion raid uses native `building = { tags = facility }` exact targeting. Native preparation, equipment reservation/collection, cancellation, expiry, outcome selection, cooldown, and `add_raid_history_entry = yes` remain engine-owned.

## Mission quality and adjacent Kruger decisions

These are decisions and native raid surfaces rather than timed missions for the Portal Warfare launch itself.

| Surface | Owner and category | Region/target | Requirement and cost | Duration and outcome | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `brilliant_scientist_portal_facility_raid` | Any actor holding the weaponization technology and locked template; `brilliant_scientist_raids` | Hostile controlled state | Six `portal_raider` battalions and 60 Teleportation Equipment; 10 Command Power | 7-day preparation, 30-day re-enable; failure, limited, success, and critical native outcomes | Formation is destroyed on success/critical; state critical intentionally performs up to two bounded extraction calls |
| `brilliant_scientist_portal_special_project_facility_raid` | Same owner/category | Exact hostile provincial facility | Same six-battalion, 60-equipment, and Command Power contract | Same lifecycle; exact facility success and critical can extract the selected facility, with critical optionally extracting one state installation | Source guards and destination gates prevent extraction-without-rebuild; no second independent formation |
| `brilliant_scientist_krg_fabricate_portal_transit_batch` | KRG decision layer | Country stockpile | Portal operation, bounded recruitment unlock, raid AI or linked terminal network, support >149, motorized >49, fuel >999, manpower >999, heavy factory capacity, 65 PP | 90-day decision, 30-day re-enable, cancellation when KRG layer or teleportation operation closes; pays -150 support, -50 motorized, -1000 fuel, -1000 manpower, then grants 180 Teleportation Equipment | Maximum four batches; each batch is one bounded stockpile increment |

The locked template contains six `portal_raider` battalions, each requiring ten Teleportation Equipment, so the sixty-equipment raid reservation aligns with the six-battalion contract. The fabrication decision can produce at most 720 equipment across four batches.

## AI and probability evidence

Raid `ai_will_do` uses base `1`, zero factors for readiness/target invalidity, Kruger-state factor `5`, Kruger factor `2`, major-target factor `1.75`, capital factor `1.50`, and facility factor `1.35`, with an AI minimum success chance of `0.25`. Mandatory MCP inspection of `common/raids/016_brilliant_scientist_portal_raids.txt` through `decision_ai_will_do` returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`, zero candidates, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6131eb6eb7ad36e79af838d551929380aa6dbfae13611431cc8a1a7b1c507425/9a4182c318047e5f5ffa85a0d1603f47f065e977c175b6924c9ae810df765b1c/probability-inspect-9e9deaa70223.json`. Raid evaluate, sweep, and compare for READY state, READY KRG host, NOT READY, and INVALID TARGET scenarios returned `PROBABILITY_SURFACE_EMPTY` (`No weighted blocks matched this request`) with no artifacts. The `ai_strategy_factor` route returned `INTERNAL_ERROR` / `Unexpected internal error`.

The native raid AI route therefore has an explicit MCP coverage blocker; source arithmetic is recorded, but no selection-probability claim is made.

The adjacent mission adapter inspected all three KRG portal decisions with current source revision `3021d3fe6042018e5ff876d368dae89fb4b13ad7f4b209a64c5f26152015ee58`, source hash `7213985c2bf7030339ca9e3430c3eeac960c224466931321c2748ad12aa784ce`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32f03c81ceff6a52abc2ddfef3367e4c87ebb87f1498230b7554f1d96fb02d96/bf5339837b1dd9df5743d036e500e64b287b438ce1866a43a01b61b088d4fe6a/probability-inspect-7213985c2bf7.json`. Current evaluation produced `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-b29573a754a05d6ad480410b`, nine candidates, twenty-one unresolved diagnostics, and `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for `brilliant_scientist_krg_fabricate_portal_transit_batch` across READY_KRG, READY_NETWORK, and CAP_REACHED scenarios. Mission AI is classified score-only; normalized selection probability and timing are not available. Ranking, matrix, and unresolved render artifacts are recorded in the probability auditor mailbox.

## Localisation, assets, and Black Plague coupling

Portal category, raid names, target names, preparation/launch tooltips, and all outcome tooltips are present in `localisation/english/chaosx_raids_l_english.yml`. The category and raid icons resolve through `interface/chaosx_raids.gfx`, `interface/cbrn_protection.gfx`, and vanilla `GFX_facility_icon`/`GFX_other_target_icon`. No active raid file references a portal model, entity preview, action, or sound beyond vanilla raid entities and sounds; the model/entity/audio task remains explicitly rejected and unwired.

The Black Plague decision files contain no Kruger, Mengele, Portal Warfare, or Teleportation Equipment references. No invalid Black Plague access path was found for the scoped coupling question.

## Validation and remaining work

Targeted source checks covered vanilla raid syntax, native raid documentation, exact-facility target syntax, division-effect scalar form, state/province scopes, destination control gates, KRG fabrication arithmetic, template battalion count, localisation/GFX key presence, and persistent-flag consumers. The installed HOI4 MCP exposes no native raid-inspection/render route, and the raid probability surface is empty; these are recorded blockers rather than substituted with source-only engine claims. No game launch or live-save validation was performed.

Parent review remains needed for the all-family special-facility destination restriction, six-battalion maximum contract, full-factor reconstructed cadre balance, and beachhead flag cleanup lifecycle. No broad mechanic or fallback was introduced.
