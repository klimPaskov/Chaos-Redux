# Fallout Diplomacy, Trade, and Intelligence Reset Matrix

## Purpose

This proof separates exact old-world reset surfaces from observable but non-resettable state. It covers ordinary resource imports, lend lease, expeditionary forces, and the intelligence system. The live transition remains fail closed wherever the installed engine documentation does not provide both a complete coverage route and an exact inverse.

This review adds the proven truce inverse and readback. It does not relax the unresolved trade or intelligence contract. `fallout_reset_old_world_diplomacy` still records those blockers. `fallout_old_world_diplomacy_full_reset_is_verified` still requires every required surface before map return.

## Verdict

Ordinary imports have a documented aggregate positive-flow detector, but no documented route enumerator and no documented cancellation effect. A country can be tested for a positive imported amount of each installed resource. A zero result across every resource does not prove that no trade route exists.

Intelligence has several documented detectors and a few narrow mutations. The documented surface cannot remove an intelligence agency, reverse its upgrades, clear every network, cancel every operation, erase completed-operation history, reset decryption state, reset static intel, empty the operative candidate pool, or clear death and turned-operative slot locks. Killing or turning operatives creates additional persistent state and is not a reset.

The exact full reset requested by the transition is therefore not proven for either surface. The live blocker flags are correct and must remain part of the map-return barrier.

## Live fail-closed ownership

The coordinator clears stale receipts at the start of each reset attempt. After all proven diplomacy work finishes, it:

- clears every old-world truce after white peace and validates every ordered country pair
- verifies an empty lend-lease surface through every ordered country pair
- verifies an empty expeditionary surface through every ordered country pair
- sets `fallout_transition_trade_routes_reset_blocked`
- sets `fallout_transition_intelligence_reset_blocked`
- registers `unprovable_diplomacy_surface`

The full-reset trigger requires the corresponding blocked flags to be absent and the trade and intelligence verified flags to exist. No live effect sets those verified flags. This makes the missing engine surfaces a hard barrier rather than a silent cleanup omission.

## Diplomacy, trade, and force-transfer matrix

| Surface | Documented readback | Documented inverse | Exact Fallout status |
| --- | --- | --- | --- |
| Wars and civil-war links | War and civil-war predicates expose the live relations | `white_peace` and `remove_civil_war_target` clear the supported relations | Implemented with global absence checks and an active peace-conference barrier |
| Factions, subjects, and exiles | Faction, subject, and exile predicates expose the live structures | `dismantle_faction`, `end_puppet`, and `end_exile` clear them | Implemented and validated |
| Guarantees, military access, non-aggression pacts, and embargoes | Official bilateral predicates expose each relation | `diplomatic_relation` with `active = no` cancels each relation | Implemented and validated across ordered country pairs |
| Docking rights | No documented readback trigger was found | `diplomatic_relation` with `docking_rights` and `active = no` has vanilla cancellation precedents | Implemented through exhaustive ordered-pair inverse coverage and a generation-bound application receipt. No runtime readback is claimed |
| Market access | `has_market_access_with` identifies the relation | `diplomatic_relation` with `market_access_rights` and `active = no` has an approved live-mod precedent | Implemented with exhaustive ordered-pair application and global readback |
| Resource rights | `has_resources_rights` reads observable country-state grants but returns false for resource-free states | `remove_resource_rights` removes a country-scoped state grant | Implemented with an exhaustive country-state inverse sweep and global readback for every observable grant. Blind resource-free states still receive the inverse |
| Purchase contracts | `any_purchase_contract` enumerates live contracts | `cancel_purchase_contract` cancels the scoped contract | Implemented and validated |
| Truces | `has_truce_with` reads the bilateral relation | `set_truce` with zero days clears an existing truce in vanilla | Implemented after white peace with exhaustive ordered-pair readback |
| Active lend lease | `is_lend_leasing` reads the outgoing relation against a specified country | No documented cancellation effect | An empty world can be proven. Any active lease remains blocked |
| Expeditionary forces | `received_expeditionary_forces` reads the amount received from a specified sender | No documented return-to-sender effect | An empty world can be proven. Any received force remains blocked |
| Positive ordinary imports | `has_resources_in_country` with `only_imported = yes` reads aggregate imported amount for one resource | No documented cancellation effect | Positive flow can be detected. Route identity and exact cleanup are unavailable |
| Ordinary route existence | No documented route iterator or bilateral route-existence trigger was found | No documented cancellation effect | Absence cannot be proven and cleanup cannot be performed |
| Active peace conference | `is_in_peace_conference` identifies the blocked world state | No documented exact termination effect | The reset waits and cannot advance while any conference is active |

Resource rights and market access are separate diplomatic surfaces. Clearing either one does not cancel ordinary factory-for-resource imports.

## Ordinary import detector boundary

Official `triggers_documentation.md` defines country-scoped `has_resources_in_country`. With `only_imported = yes`, the trigger checks imported resource amount instead of the country's resource balance. The installed vanilla resource registry contains exactly these seven resource ids:

1. `oil`
2. `aluminium`
3. `rubber`
4. `tungsten`
5. `steel`
6. `chromium`
7. `coal`

The mod has no `common/resources` directory, so this installed registry is the complete static resource-id set for the current project.

An exhaustive seven-resource check has one safe positive conclusion. If any resource reports an imported amount above zero, then the country has positive imported flow for that resource at that moment.

It does not support these conclusions:

- which exporter supplies the amount
- how many trade routes contribute to the amount
- whether a route exists while current delivery is zero
- whether a route exists for a resource whose aggregate imported amount is zero
- whether every route can be cancelled
- whether a zero aggregate is a durable postcondition

The route-existence limitations are an inference from the documented aggregate contract. The trigger reports an amount, not a route object or bilateral relation. Therefore a seven-resource zero result is not accepted as proof of an empty trade surface.

Official `effects_documentation.md` exposes `create_import`, described only as creating trade between two countries. It provides no documented inverse. No `cancel_imports` effect appears in the installed official effect reference. No live use of that token was found in vanilla, Chaos Redux, or the three approved reference mods. An executable-looking but undocumented token is not an accepted engine surface.

## Intelligence matrix

| Surface | Documented observation | Documented mutation | Exact reset result |
| --- | --- | --- | --- |
| Agency existence | `has_intelligence_agency` | `create_intelligence_agency` only creates | No removal route |
| Agency upgrades | `agency_upgrade_number` and `has_done_agency_upgrade` | `upgrade_intelligence_agency` only adds | No downgrade or clear route |
| Controlled operatives | `num_of_operatives`, `any_operative_leader`, and `all_operative_leader` | `every_operative` plus `kill_operative` can destroy the currently controlled roster | Partial destructive teardown with a count postcondition. Killing explicitly creates temporary slot locks and does not clear history or candidates |
| Captured operatives | `has_captured_operative` and `is_operative_captured` | `free_operative` and `free_random_operative` can release captured operatives | Exact captivity inverse under an exhaustive owner-captor sweep. Releasing agents does not reset the operative roster or agency |
| Operative slots | `num_operative_slots` and `num_free_operative_slots` | No documented slot-state reset | Death and turned-operative locks cannot be cleared exactly |
| Dead and turned operative state | Only aggregate slot-capacity observations are documented | Kill and turn create death or slot-lock state. Nationality transfer also locks the origin slot | No unturn, resurrection, death-counter reset, slot-lock reset, or exact detector |
| Operative candidate pool | No documented candidate iterator, count, or empty-pool trigger | `create_operative_leader` can add a candidate | No candidate removal or pool reset route |
| Networks | `network_strength` and `network_national_coverage` | No documented network removal effect | No reset route |
| Preparing operations | `is_preparing_operation` | No documented cancellation effect | Detectable in bounded target and known-operation checks, not resettable |
| Running operations | `is_running_operation` | No documented cancellation effect | Detectable in bounded target checks and the operation token may be omitted, not resettable |
| Completed operation history | `num_finished_operations` | No documented history reset | No reset route |
| Operation tokens | `has_operation_token` reads a named token against a named country | `remove_operation_token` removes one named token | Exact only for a finite token known in advance. No complete token enumerator was found |
| Decryption progress | `decryption_progress` | `add_decryption` only adds | No set-to-zero route |
| Active decryption bonus | `is_active_decryption_bonuses_enabled` | No documented disable or clear effect | No reset route |
| Decryption department and active target | Department-active, currently-decrypting, and fully-decrypted triggers expose partial state | No documented stop, disable, or clear effect | No reset route |
| Static intel | `compare_intel_with`, `intel_level_over`, and four documented intel variables expose partial or aggregate values | `add_intel` only adds named intel categories | No scripted set-to-zero route. `clear_intel_pools` is a console command, not a scripted effect |
| Fake intelligence divisions | `num_fake_intel_divisions` reads the aggregate count | `delete_unit` can remove a known creation id and template effects can remove a known named template | Exact only for units already covered by a complete id ledger or one known template. No generic fake-intel iterator or filter was found |
| Faction spymaster | `is_spymaster` | `set_faction_spymaster` assigns a spymaster | Faction teardown removes the surrounding context. It is not a standalone documented spymaster inverse and still requires `is_spymaster = no` observation |

## Narrow exact actions that do not satisfy the full contract

The documented effects support a few exact local changes:

- `free_random_operative = { all = yes captured_by = TAG }` releases every operative of the scoped country captured by the specified country. An exhaustive owner-captor sweep can clear captivity exactly
- `free_operative` releases one specified captured operative
- `remove_operation_token` removes one specified token against one specified country
- `delete_unit` removes a fake-intel unit whose exact creation id was recorded, matching the vanilla fake-intel cleanup pattern
- named-template deletion can remove one known fake-intel template and its units
- faction teardown removes the faction context in which a spymaster relation exists, subject to a negative `is_spymaster` observation

These actions cannot be combined into a complete intelligence reset. Releasing captured operatives preserves or restores active operatives. Removing a finite known token list does not enumerate tokens introduced by the base game, downloadable content, another mod, or saved state. Fake-intel deletion covers only ids or templates known before the cleanup. Faction teardown does not remove agencies, upgrades, networks, operations, decryption, intel, candidates, or operative-slot locks.

## Rejected substitutes

The following substitutions are not accepted:

- treating zero positive imports across seven resources as proof that no route exists
- calling undocumented `cancel_imports`
- recreating or overwriting imports with zero values
- deleting divisions to approximate expeditionary return
- transferring broad force categories to approximate expeditionary return
- killing every operative
- turning every operative
- freeing captured operatives and declaring the intelligence surface clean
- removing only a hand-maintained operation-token list
- dismantling factions and declaring every intelligence agency clean
- adding negative decryption or intel values when no reset contract is documented

Each substitute either leaves required state behind, destroys the wrong owner state, creates new persistent state, or depends on an undocumented behavior.

## Release effect

No trade or intelligence verified receipt may be written from the evidence available here. `fallout_transition_trade_routes_reset_blocked` and `fallout_transition_intelligence_reset_blocked` must continue to prevent `fallout_old_world_diplomacy_full_reset_is_verified` from passing. Because map return requires that trigger, blackout recovery must remain closed on any transition that reaches this proof boundary.

This is an exact engine blocker. It is not permission to weaken the transition contract. Any proposed simplification requires explicit user approval before gameplay code changes.

## Source record

Primary official engine sources:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/console_commands_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/resources/00_resources.txt`

Relevant offline wiki sources were reviewed in parallel:

- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`

Precedent search roots:

- installed vanilla Hearts of Iron IV files
- vanilla `events/GOE_Raj.txt` lines 1706 through 1711 for zero-day truce cancellation
- vanilla `events/AAT_Finland.txt` for docking-rights cancellation
- vanilla `common/on_actions/07_nsb_on_actions.txt` for state-scoped resource-rights removal
- vanilla `common/operations/00_operations.txt` for captured-operative release, operation-token use, decryption, intel, and fake-intel creation ledgers
- vanilla `events/LaR_espionage_operations.txt` for ledger-backed fake-intel deletion
- Chaos Redux
- Kaiserreich workshop id `1521695605`, especially `common/scripted_effects/00_economic_sphere_scripted_effects.txt` for market-access cancellation
- approved workshop ids `2265420196` and `1458561226`

No Hearts of Iron IV session was run. This proof records the static engine surface and its exact limitations.
