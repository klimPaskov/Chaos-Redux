# Event 016 biological native raid migration handoff

Disposition: implemented in source under the user's approved CBRN native-raid simplification, with the engine and MCP limits below still unresolved.
The approved instruction removes the human-facing agent selection, Event 016 payload production, staging decision, and decision-based biological attacks in favor of ordinary equipment production and native raid reservation.
This instruction supersedes older Event 016 documents that required a separate decision deployment receipt.

## Changed surfaces

- `common/raids/016_brilliant_scientist_biological_raids.txt`: eighteen native raids, one per agent and battlefield, Portal battlefield, or covert method.
- `events/016_brilliant_scientist_biological_raid_events.txt`: seventy-two hidden immediate outcome events that restore actor-country `ROOT` before any inherited consequence helper runs.
- `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt`: one guarded outcome dispatcher plus existing ordinary, Zombie, and Black Plague consequence routes.
- `common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt`: six unlock predicates and exact native target guards.
- `common/decisions/016_brilliant_scientist_biological_operations.txt`: removed obsolete selection, production, staging, and attack decisions.
- `common/decisions/categories/016_brilliant_scientist_raid_lifecycle_categories.txt`: removed the now-empty biological decision category while retaining Portal containment.
- `common/on_actions/016_brilliant_scientist_raid_lifecycle_on_actions.txt`: removed decision-receipt capitulation and annexation callbacks while retaining Portal beachhead callbacks.
- `common/script_constants/016_brilliant_scientist_raid_lifecycle_constants.txt`: retained native outcome and agent tuning, removed unused production and staging constants.
- `common/ai_strategy/biological_warfare_production.txt`: added Zombie Disease Bomb demand after its delivery technology unlock and a narrow two-bomb Black Plague reserve after offensive Event 020 completion under safe stockpile conditions.
- `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt`: removed debug auto-selection of Anthrax.
- `common/raids/zombie_weaponized_raids.txt`, `common/raids/zombie_weaponized_friendly_raids.txt`: removed obsolete staging bonus definitions and modifiers.
- `common/scripted_localisation/016_brilliant_scientist_biological_operations_scripted_localisation.txt`: removed unused selected-agent text.
- `localisation/english/016_brilliant_scientist_projects_l_english.yml`, `localisation/english/chaosx_raids_l_english.yml`: removed obsolete decision and staging copy.
- `localisation/english/016_brilliant_scientist_biological_raids_l_english.yml`: names, descriptions, target conditions, and outcome text for the eighteen raids.
- `interface/016_brilliant_scientist_biological_raids.gfx`: stable Black Plague map sprite using existing Event 020 delivery art.
- `docs/events/016_brilliant_scientist/systems/biological_operations.md`: current mechanic, asset, rebalance, and extension contract.

The generic `biological_raids` category is owned by the native-raids worker; it now accepts Event 016 agent unlocks, including tech-only and Black Plague-only access.
The native-raids worker owns removal of matching staging modifiers from `biological_raids.txt` and `biological_battlefield_raids.txt`.
The shared lifecycle worker owns the guard that skips duplicate integrated-doctrine Command Power recovery when `bio_native_raid_dispatch_in_progress` is set.

## Cost and outcome comparison

| Method | Previous decision reservation | Native raid reservation | Previous result weights | Native result mapping |
| --- | --- | --- | --- | --- |
| Battlefield | 25 Command Power plus one agent lot at decision start, seven-day timer | 25 Command Power plus the same fixed agent lot in `essential_equipment`, seven-day raid preparation | 70 success / 25 failed release / 5 home accident | Success or critical success releases; limited success fails; failure is home accident, using success base 0.70 and disaster base 0.05 |
| Portal battlefield | Same battlefield spend plus 10 Teleportation Equipment for rear access | Same payload and Command Power plus 10 Teleportation Equipment in `essential_equipment` | Same battlefield weights | Same battlefield mapping and original target history |
| Strategic covert | 50 Command Power plus two agent lots at decision start, fourteen-day timer | 50 Command Power plus the same fixed two lots in `essential_equipment`, fourteen-day raid preparation | 55 success / 30 failed release / 15 home accident | Success or critical success releases; limited success fails; failure is home accident, using success base 0.55 and disaster base 0.15 |

| Agent identity | Battlefield and Portal items | Covert items | Concrete equipment and unlock |
| --- | ---: | ---: | --- |
| Anthrax | 200 | 400 | `anthrax_bomb_1`, Anthrax project or technology |
| Plague | 100 | 200 | `plague_bomb_1`, Plague project or technology |
| Tularemia | 100 | 200 | `tularemia_bomb_1`, Tularemia project or technology |
| Smallpox | 50 | 100 | `smallpox_bomb_1`, Smallpox project or technology |
| Weaponized Zombies | 125 | 250 | `zombie_disease_bomb_1`, Zombie project, flag, or technology |
| Engineered Black Plague | 1 | 2 | `plague_bomb_1`, Event 020 weaponization or Kruger authorization |

Black Plague and ordinary Plague deliberately share Plague Bomb hardware but have distinct raid IDs, names, map sprites, authorization, and consequence callbacks.
The retired one-lot and three-lot production decisions formerly occupied two or four civilian factories for 30 or 60 days and spent 80 or 240 Support Equipment and 250 or 750 manpower.
Their removal is an explicit balance change to ordinary equipment production, not a hidden rebate.
The retired staging decision occupied one civilian factory for 90 days, then gave 180 days of native-raid success, critical, disaster, and AI bonuses.
The Black Plague completion grant supplies one `plague_bomb_1`; its separate ordinary-production AI strategy requests only the second bomb needed for a covert Event 016 raid when generic safe, desperate, and Japan Plague strategies are inactive.
The Zombie delivery technology directly enables its buildable concrete bomb, so a tech-only AI actor receives production demand under the existing safe or desperate biological production posture without needing the project completion flag.

## Evidence and limits

The offline core Paradox wiki pages, installed vanilla raid documentation, and vanilla land raid precedent were consulted before editing.
Source checks found eighteen unique native raid IDs, all in `biological_raids`, eighteen explicit equipment and Command Power reservations, four outcome levels per ID, matching localisation names and descriptions, and balanced braces in touched script.
The final static crosswalk found seventy-two distinct block-form `country_event` callback IDs exactly matching seventy-two hidden event definitions (`chaosx.nr16.950` through `.1021`), with actor, selected-state, and victim event targets saved in every callback before dispatch.
The current SHA-256 values are `D6D3C18B2D8B44F65DCC59E277138F036750246C3E3963DCACEDCF5768EE76A0` for the native raid file, `68CB54564F64F6956D136B9BC2A48DF2A9E28EA9309CF6BF20D11C7EA716C994` for the hidden event file, and `74411B39EE2FF4E115115C457BD89A0831BEE35C90A1C9E0B53318F4994A1B81` for the AI production file.
Vanilla raid documentation distinguishes actor-country scope for `visible`, `show_target`, `available`, and `launchable` from raid-instance scope for outcome effects.
The Event 016 pre-raid target predicates keep actor-country `ROOT`; completed-raid callbacks begin in raid-instance `ROOT` and save exact actor, target-state, and victim pointers as regular chain-local event targets before firing a hidden immediate actor-country event.
Each hidden event ID encodes its agent, method, and result, reconstructs all temporary input values, and dispatches with actor-country `ROOT`; no country or global pending scalar can be overwritten by another raid.
All seventy-two immediate callbacks use the vanilla-documented `country_event = { id = ... }` effect form.
The dispatcher validates the live actor, authorized agent, war, selected state, original victim, and method-specific target before applying consequences; missing or invalid targets fail closed after the native payment and still retain native raid history.
The capital accident stores the capital state through the actor scope, and Black Plague exposure reads its route as an unscoped temporary variable.
The native `target_type` lists the eligible state set; `show_target`, `available`, and `launchable` enforce the precise enemy and method predicates.
The four ordinary bomb models and Zombie Disease Bomb model are concrete buildable equipment, their delivery technologies enable them, and the Zombie project completion grants its delivery technology and initial stock.
CXT's player-triggered debug stockpile currently grants all five concrete IDs; that refill is intentionally repeatable and is not a package-owned idempotent setup grant.

An earlier namespace `hoi4.event_inspect` and narrower Event 016 root inspection timed out after 180 seconds before the country-event bridge was added.
The post-bridge focused `hoi4.event_inspect` lint for `chaosx.nr16.950` returned `EVENT_INSPECTED_PARTIAL` at revision `c126a00aad731c2193c022096c51891c4529c750b0f9a73eb523428d37775d73`, with no blocking diagnostics, zero skipped sources, and deferred workspace-wide helper and lifecycle projections.
The post-bridge `hoi4.event_render` scope view returned `EVENT_RENDERED_PARTIAL` at revision `4ce0bad5115f1a26a5d1b5383413a47a59965b13fdfd02f50af1d57a6da57b2f`; this is structural event evidence and does not prove the native raid parser or live outcome behavior.
The `hoi4.event_compare` attempt between those two revisions returned `EVENT_REVISION_NOT_CACHED` and no artifact, so there is no MCP before-and-after graph comparison.
After converting all raid callbacks to the vanilla-documented block form, a refreshed focused Event 016 `hoi4.event_inspect` lint and `hoi4.event_render` scope view both indexed revision `53cfc668c05d032d7d279e9e9b3ddd7bfd6852cc288bbd5c857f7600bc679964` with zero blocking diagnostics and zero skipped sources, but returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` because workspace-wide helper and lifecycle projections were deferred.
The scope render reported `selectedNodes: 0`, so it is not proof of the selected bridge event's visualized chain; a same-selector `trace` remained partial as well.
The final comparison of revision `4ce0bad5115f1a26a5d1b5383413a47a59965b13fdfd02f50af1d57a6da57b2f` against `53cfc668c05d032d7d279e9e9b3ddd7bfd6852cc288bbd5c857f7600bc679964` again returned `EVENT_REVISION_NOT_CACHED` with no artifact.
Final lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7cc83384ae8195211cbf2e749a05317061ca1ca4c937a68727ac0d0e51e91980/55f52d4c842dff83f5e9a9933feb45f8f12729b5237f291b53a742aea1daa618/event-lint-53cfc668c05d.json`.
Final scope manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc32587db471310367b1a7c8934a9b4259a5a2b3ce10ebb7d68c3407963cf8c5/320e387a5bd804b3eab50d28a11faf0fffbbb06ab54400fac251ec13219f26c3/event-scope-53cfc668c05d-manifest.json`.
For the named `E016_BLACK_PLAGUE_ORDINARY_PRODUCTION_1936` AI scenario, mandatory `hoi4.probability_inspect` found the source but reported `no_weighted_surfaces`, zero candidates, and no available adapters for `equipment_production_surplus_management` (baseline source hash `ef626c63c4f687c96c95fbc2b03de2f6da78ea7d0164ca2a3e62b94a88aacd40`; post-patch source hash `e915664bcce31ad478d5d3ee2ba0276450edcd87beb27b1bb291ca856f1eeb0e`).
The mandatory same-scenario `hoi4.probability_compare` attempt with scenario set `cbrn_bio_production_black_plague_20260920` returned `PROBABILITY_SURFACE_EMPTY`, zero artifacts, and no analysis ID; no weighted or runtime production probability is claimed.
The Zombie tech-only production gate change was made after the baseline biological AI source discovery at hash `e915664bcce31ad478d5d3ee2ba0276450edcd87beb27b1bb291ca856f1eeb0e`, which also reported `no_weighted_surfaces` and no adapter; the named `E016_ZOMBIE_TECH_ONLY_PRODUCTION_1936` postpatch comparison is delegated to the probability auditor and remains outstanding in this handoff.
Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67d6ff20bbd5966cf9317ba8a40bffe882d77fe366c4aca678426e1e74e573f4/671c45d57429691f7eb6e205bb806dfb777e73a07f71bb47adaf2657f2e19c72/event-lint-c126a00aad73.json`.
Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a8ad21281d261f3b41587346fc03f915b1490e6e29d60be34fdf0ccab52ab14/ec400414ff6c266a7417d11bf241ca9be23fe1d047cac75c2c9875760ba997de/event-scope-4ce0bad5115f-manifest.json`.
No Hearts of Iron IV process or save was launched.

The native land path solver has not been proven to reach every disconnected Portal rear target that the former state-targeted decision could select.
The native raid success/disaster formulas are source-level parity with the former weights, but the engine may apply raid unit and preparation modifiers.
The raid system requires a qualifying land formation and supply-node start where the former decision did not.
The 32-by-33 Event 020 Black Plague delivery art is reused as a distinct map sprite key; the ordinary raid icon reference canvas is 32-by-32.
Those three differences are explicit validation and visual follow-up items, not claimed parity.
The older Event 016 spec, plan, and wonder-technology action documents still describe the superseded decision deployment and need parent-owned reconciliation.
