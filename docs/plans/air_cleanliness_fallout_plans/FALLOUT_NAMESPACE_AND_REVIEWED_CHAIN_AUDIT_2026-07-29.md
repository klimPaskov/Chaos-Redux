# Fallout namespace and reviewed chain audit

This audit records the source-level review completed after the Fallout consequence boundary was reconciled with the retired Final Silence route.

## Dedicated ownership

`events/fallout_world_end_events.txt` begins with `add_namespace = chaosx.fallout`.

The file contains 721 unique top-level `country_event` definitions with ids from the dedicated namespace.

A repository scan found no `chaosx.fallout.*` event id in another event-definition file.

The visible event blocks have titles, descriptions, and either a player option or an immediate effect.

The hidden blocks are callback, hidden-AI, delayed-result, or cleanup surfaces and are not presented as the Fallout consequence itself.

The file contains 323 visible blocks. The 30 direct title, description, option, and tooltip references used by events `677`, `679`, and `681` resolve to the dedicated English localisation file with zero missing references.

No Fallout-owned effect uses `delete_country`, `delete_tag`, `annex_country`, or `release_country`.

## Consequence boundary

The Fallout consequence has no ordinary country Event Log row and no evolution entry.

Post-consequence survivor stories use ordinary country events and typed `fallout_country_memory` history rows. Those rows describe survivor chains and do not register the world rewrite as an ordinary event.

The world-end selector replaces the retired Final Silence selector row with Fallout id `13`.

The separate manual sandbox launch surface uses triggerable-scenario id `14`, the next live id after the existing maximum. It remains launch-gated by the exact native province-sweep proof and is not an ordinary Event Log row, evolution, Event Details card, or ordinary super-event.

The live Fallout scenario window no longer initializes or advances a Final Silence type variable. The retired id, selector wrapper, and trigger wrapper remain only as save and scripted-caller compatibility paths, while Fallout's visible name, type, description, and impact are selected directly from id `14`.

The settings export no longer emits a Final Silence type row. The retired type constant remains only for compatibility with older serialized settings.

The Final Silence runtime migration has no active setter in the current Fallout-owned path. A stale base or thermonuclear Final Silence flag queues the Fallout request coordinator, while the completed cause-memory flag remains historical. The retirement helper clears the old base, thermonuclear, and interrupted runtime markers before Fallout takes ownership.

The locked Fallout admission calls the generation-bound `fallout_stop_old_world_wars_at_admission` receipt before blackout presentation. Its source path ends active wars, exiles, volunteers, and civil-war targets. Subjects, access, markets, trade, intelligence, and exhaustive diplomatic readback remain owned by the later reset transaction.

The permanent Air boundary writes `9,900` basis points through one idempotent effect. Wildfire, volcanic eruption, ashfall, and settled-ash inputs use the low shared reservoir cap before Fallout and return zero after the permanent lock.

## The Battalion's Bread List reviewed chain

The latest reviewed ordinary chain uses ids `chaosx.fallout.677` through `chaosx.fallout.683`.

The human opening offers protected issue, equal measure, field requisition, and rear-echelon stand-down choices with complete resource, military, state, owner, and generation checks.

The hidden opening selects an AI branch through the same branch ledger instead of showing a player event to an AI country.

The result pair resolves after `28` days and carries success, partial, and failure prose for each branch.

The callback pair performs a later ration review after `210` days and preserves branch-specific delayed consequences.

The cleanup event is hidden, generation-bound, and called only after the callback receipt is current.

Dedicated localisation covers the opening, government-aware ration authority, four choices, branch-specific result text, callback outcomes, tooltips, survivor-memory Event Log wording, and modifiers in `localisation/english/fallout_consolidated_l_english.yml`.

The prerequisite Work for Rations chain now writes a durable policy generation and owner receipt for every branch. Candidate 677 rejects stale branch flags without that receipt.

The chain remains dormant until the Fallout-owned scheduler, host authority, save recovery, delayed delivery, Event Log delivery, Deaths readback, and runtime presentation gates are accepted.

## Static checks

The dedicated Fallout event file and the reviewed transition scripts are brace-balanced.

No unsupported `<=` or `>=` operator appears in the reviewed Fallout event or transition scripts.

The source-level audit does not prove engine callback timing, native province acceptance, dynamic-country creation, blackout input capture, or multiplayer host authority.
