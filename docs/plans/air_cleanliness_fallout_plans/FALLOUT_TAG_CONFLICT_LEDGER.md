# Fallout Live Tag Conflict Ledger

Status: required allocation ledger. This file records live ownership before any successor tag is assigned.

## Allocation rules

1. Preserve the human player country and its continuation candidates before general allocation.
2. Record every tag that is alive, releasable, dynamically reserved, or owned by another event package.
3. Reserve Fallout tags only after the live scan.
4. Treat the 99-successor matrix as a candidate pool rather than an instruction to spawn every candidate.
5. Never overwrite a live country or an event-owned dynamic country.
6. If a requested successor tag conflicts, stop allocation for that package and report the conflict. An alternate reviewed candidate may be used only after explicit approval. Never silently reuse a zombie tag.

## Current repository reservations

| Reservation family | Evidence surface | Fallout rule |
| --- | --- | --- |
| Zombie outbreak | `ZZZ`, zombie dynamic-country flags, zombie scripted effects and assets | Never reuse ids, tags, files, sprites, audio, or asset paths |
| Mengele clone scenario | Global target `mengele_clone_army_scenario_country` and clone scenario country flag | Treat its live dynamic country as occupied |
| Soviet collapse packages | Existing country and releasable assignments in Event 005 | Re-scan active tags before successor allocation |
| Final Silence | Event 003 terminal-country and strike ownership | Preserve cause memory, do not inherit its actor tags |
| Cannibalism | Host-country flags and Event 014 country packages | Treat every live host country as occupied |
| Other dynamic event countries | Any country with an event-package ownership flag | Treat as occupied until the package explicitly releases it |

## Runtime ledger fields

The complete allocation ledger must record:

- tag token or dynamic country scope
- original tag
- current controller and capital state
- human ownership
- event-package ownership
- alive and land-holding state
- reserved continuation priority
- selected Fallout package
- selected regional package
- selected archetype
- conflict result
- cleanup owner
- resolution generation
- cleanup generation
- resolution-specific provenance receipt

The first seven fields describe the pre-allocation inventory. The selected Fallout package, regional package, selected archetype, conflict result, and cleanup owner are allocation outputs. They must not be inferred by the inventory builder.

## Player reservation order

1. Store every human source scope before any mutation.
2. Store every snapshot-origin state and continuity memory for that source.
3. Reserve every origin state, then reserve the strongest hostable capital when one exists.
4. Record an explicit fragmented, refuge, altered, or emergency materialization row when no in-place target is ready. A landless source remains valid and receives the emergency row.
5. Freeze the general conflict inventory only after every player source passes the reservation-row proof.
6. Materialize and package missing player targets before general output finalization.
7. Present continuation only after all offered targets are confirmed live, unique, and playable.
8. Treat player reservations as immutable after allocation initialization. Any later drift owns a fail-closed error and cannot rebuild consumed rows.

## Audit status

### Generation-bound pre-allocation inventory is implemented

`fallout_build_successor_conflict_ledger` builds derived inventory schema 1 for the active transition generation. The builder does not assign a tag or transfer a state.

- Every member of `game:all_countries` receives a row with country identity, original tag, owned-state count, land-holding status, human status, player reservation status, capital state, capital controller, and overlapping known event-package ownership flags.
- Every member of `game:all_possible_countries` is copied into a separate possible-scope array. A possible scope is not treated as a materialized country or an available tag merely because it appears in that collection.
- Every state receives a generation-bound row with frozen owner, frozen controller, hostability, human ownership and control, player reservation, and known event-package ownership.
- A state enters the successor candidate array only when it can host a government, has no current player reservation, has AI ownership and control, and neither country has known live event-package ownership.
- Event-package-owned land remains outside the ordinary candidate array. A separate protected-event origin proof permits only a preserved package to use its own rewritten land.
- Header and row validators compare the local schema, transition generation, exact collection sizes, array counts, current country rows, current state rows, candidate membership, reservation membership, and candidate-reservation separation.
- A land-holding country without exactly one owned capital makes the inventory invalid. A landless country may have no capital row.
- The builder records overlapping package families independently. It does not collapse them into one cleanup owner.
- Inventory failure uses its own error code and preserves any earlier transition error.

The ownership helper covers the current known Zombie, Mengele, Soviet collapse, Independence Wave, liberation reservation, Holy Realm, Final Silence, Cannibalism, special Chaos country, and Fallout request-actor surfaces. This is not a permanent repository-wide registry. It must be re-audited against live package producers before any allocator is allowed to change ownership or materialize a tag.

Static source inspection supports the structure, but several engine properties remain runtime-sensitive. These include dynamic-country membership in `game:all_possible_countries`, absent possible-country scope behavior, persistent storage of `original_tag`, capitals on unusual dynamic or exile countries, and save behavior for scope-valued rows.

### Deterministic pre-allocation classification is implemented

Government classifier schema 2 assigns a provisional origin archetype to every surviving live country before ownership changes. It aggregates frozen state inputs into the frozen original owner scope, uses a fixed specificity order, and stops the transition with error 16 when a surviving country has no valid identity.

- Eleven archetypes have live predicates: mutant polity, religious refuge, quarantine state, bunker authority, warlord command, technate, food compact, maritime remnant, scavenger syndicate, nomad convoy, and continuity government.
- Machine Protocol is future-only. It requires a Brilliant Scientist machine-continuity memory, a live command network, a separately verified EMP-survival flag, a technical state, and a remote refuge. The live command network and EMP-survival requirements have no complete producer, so any partial machine claim remains unresolved rather than falling into another archetype.
- Mutant Polity requires Chaos at the final tier, a biological or mixed cause, an owned altered-biosphere state, and separate hostable territory. This is fictional high-chaos content and does not gate the Fallout request.
- Continuity Government requires a surviving pretransition capital. The stored government or exile flags preserve old-state memory but do not add meaningful discrimination because every snapshotted country records one government family.
- Air Winter category memory is copied into `fallout_pretransition_air_winter_original_category` during the Fallout snapshot. Later Air Winter cleanup cannot change bunker, food, or maritime origin classification.
- The classifier stores the result in `fallout_government_origin_archetype`. The final applied package uses the separate `fallout_government_archetype` variable, so reviewed package selection can preserve origin memory without overwriting it.
- The classifier does not change visible politics, select a country package, transfer territory, load a focus tree, or initialize AI.

The fixed order is Machine Protocol, partial machine claim, Mutant Polity, Religious Refuge, Quarantine State, Bunker Authority, Warlord Command, Technate, Food Compact, Maritime Remnant, Scavenger Syndicate, Nomad Convoy, and Continuity Government. It is a deterministic pre-allocation identity rule. It is not a substitute for reviewed package selection.

### Post-allocation proof contract is implemented, allocator remains absent

Successor allocation schema 2 separates the frozen input ledger from the mutated output world.

- `fallout_begin_successor_allocation_transaction` may consume only a fully current inventory generation after the player reservation ledger passes, and records the source generation and schema.
- Every frozen live-country conflict needs a current resolution and cleanup owner. The source row must remain recorded and resolved, must no longer be allocation-pending, and must retain the frozen inventory generation. Resolution and cleanup generations must match the active transition. A player source must use `player_reserved`. A non-player event-package owner or request actor must use `preserved_event_package`. An ordinary source may use neither protected result. A non-retired source must name one output country. That output must link back to the same source with the same result, generation, and cleanup owner.
- Continued-in-place and protected-package outputs must be the frozen source country. Converted outputs require a current conversion-commit receipt. A releasable must be absent from the frozen live-country array, present in the frozen possible-country array, and own a current release-commit receipt. Possible-country membership alone is not release proof. Dynamic outputs must be absent from both frozen arrays and own a current materialization receipt. Retirement requires no output.
- A player source's `player_reserved` conflict output must equal its player continuation primary target before allocation can finalize.
- `retired_landless` is valid only when the source owns no state, has no committed assignment, and names no output.
- Every surviving landholder needs one committed country row, one unique capital row, a preserved origin archetype, a separate final archetype, current country, focus, archetype, regional, and country-memory package generations, and current conflict and cleanup receipts.
- Array counts must equal the number of unique live country scopes, unique capital states, and exact live landholders.
- Conflict results must use the registered resolution enum, final regions must use one of the nine regional ids, and country-memory ids must be positive. A surviving assignment cannot claim the landless-retirement result.
- `fallout_finalize_successor_allocation_transaction` is the only setter for `fallout_successor_allocation_complete`, and it writes the flag only after the complete output proof passes.

No active allocator calls the begin or finalize effect. No active producer creates assignment rows, writes conversion, release, or materialization provenance receipts, or applies the required package layers. Map return therefore remains blocked.

The future allocator must use a persistent generation-bound plan, cursor, and per-row committed stage because Clausewitz exposes no atomic rollback. The current initializer is only the transaction boundary and does not yet supply that resumable allocator. The allocator must reserve humans and event packages first, prove every target, state, and capital unique before mutation, capture or materialize the target, transfer exact planned states, validate ownership and control, set the capital, apply identity and gameplay packages, write the resolution-specific provenance and reciprocal conflict receipts, then call the guarded finalizer. Static existing tags and approved releasables may be used only after the live conflict proof. Dynamic creation remains disabled until capacity, reservation, recycling, save, and multiplayer behavior are proven.

- The inventory does not select a Fallout country package, regional package, final successor archetype, conflict result, or cleanup owner.
- No Fallout successor focus, character, idea, decision, AI, country localisation, or flag package is present.
- The accepted 99-successor matrix remains a design catalogue. It does not provide approved exact state packages, ordered capital choices, source-tag conflict dispositions, or complete package assignments for allocation.

The accepted matrix rows now have stable script ids 1 through 99 in `constant:fallout_country_memory.*`. Those ids preserve matrix identity only. They do not approve a pilot roster, activate a tag, or fill the missing state, capital, package, and asset decisions.

No successor allocation may be called complete until the live ledger is fully populated, player-first reservation is enforced, package conflicts are resolved, and all required country surfaces are implemented.

## Conditional existing-tag pilot candidates

The following entries are conditional planning candidates. They do not approve activation, state transfer, focus loading, or a reduced package. All eleven use registered vanilla country tags, so they do not consume dynamic-country pool capacity. Runtime allocation must still reject any tag or state scope that is alive, human-reserved, or owned by another event package.

The primary state package is the reviewed proposal. Every reduced package below is explicitly unapproved. A reduced package is not an automatic fallback and cannot be selected without a separate design approval.

| Archetype | Candidate and tag | Proposed primary states | Ordered capital proposal | Unapproved reduced package | Compatibility evidence and unresolved condition |
| --- | --- | --- | --- | --- | --- |
| Continuity government | South African Continuity Mines, `SAF` | `{ 275, 719 }` | `275 -> 719` | `{ 275 }`, unapproved | Existing vanilla country with a South Africa focus tree, SAF characters, ideas, and decisions. Chaos Redux references are generic CBRN and startup hooks. |
| Bunker authority | Alpine Redoubt, `SWI` | `{ 3, 151, 845, 846, 847 }` | `3 -> 151` | `{ 3, 151 }`, unapproved | Existing vanilla country with bespoke focus, character, idea, decision, and AI content. Chaos Redux has one generic communism trigger reference. |
| Warlord command | Venezuelan Fuel Remnant, `VEN` | `{ 307, 488, 489 }` | `307 -> 489` | `{ 307, 489 }`, unapproved | Existing vanilla country with a generic focus tree and unique characters, ideas, and decisions. Chaos Redux has one generic communism trigger reference. |
| Food compact | Australian Grain Shield, `AST` | `{ 285, 517, 519, 521, 522 }` | `285 -> 517` | `{ 285, 517, 519 }`, unapproved | Existing vanilla country with a bespoke package. Chaos Redux references are generic CBRN and startup hooks. |
| Scavenger syndicate | Rhine Dead Cities, `HOL` | `{ 7, 35, 36 }` | `7 -> 35` | `{ 7 }`, unapproved | Existing vanilla country with a bespoke package. Chaos Redux references include the Mengele scenario and generic CBRN and startup hooks. Terminal coexistence requires explicit review. |
| Technate | Atacama Observatory State, `CHL` | `{ 952, 951, 506 }` | `952 -> 506` | `{ 952, 506 }`, unapproved | Existing vanilla country with a bespoke package. Chaos Redux owns `history/units/CHL_1936.txt`, `interface/countrystateview.gfx`, and a generic communism trigger reference. Fallout activation cannot reuse starting-history setup. |
| Mutant polity | Amazon Altered Basin, `BRA` | `{ 495, 496, 938, 939, 940, 942 }` | `495 -> 496` | `{ 495, 496, 938 }`, unapproved | Existing vanilla country with a bespoke package. Chaos Redux references `interface/countrystateview.gfx` and a generic communism trigger. Altered-biosphere eligibility must be proven at runtime. |
| Religious refuge | Ethiopian Highland Refuge, `ETH` | `{ 271, 840, 841, 842, 843 }` | `271 -> 842` | `{ 271, 840, 841 }`, unapproved | Existing vanilla country with a bespoke package. Chaos Redux has a camp-repression trigger reference. Archetype assignment must explicitly select the church-relief route. |
| Quarantine state | Levant Quarantine Cities, `SYR` | `{ 554, 677, 680 }` | `554 -> 677` | `{ 554, 677 }`, unapproved | Existing vanilla tag with country history and characters. It uses the generic focus tree and has no bespoke vanilla idea, decision, or AI package. No Chaos Redux ownership reference was found. |
| Maritime remnant | New Zealand Lifeboat State, `NZL` | `{ 284, 1079, 723, 1080, 1081 }` | `284 -> 1079` | `{ 284, 1079, 723 }`, unapproved | Existing vanilla country with bespoke focus, character, idea, and decision content. Chaos Redux references are generic CBRN and startup hooks. |
| Nomad convoy | Sahel Caravan Wards, `MLI` | `{ 556, 782, 898, 899 }` | `556 -> 782` | `{ 556, 782 }`, unapproved | Registered vanilla releasable with capital state 556. All proposed states are MLI cores and begin under French ownership. Allocation requires release or transfer review plus French and player reservation checks. No Chaos Redux ownership reference was found. |

## Machine protocol blocker

No safe machine-protocol candidate has been proven.

- Antarctic Listening Government has no mapped state package and no exact source tag.
- Arctic Listening Posts requires a northern Soviet or Russian clone package that does not exist.
- `KAR` is the nearest concrete vanilla releasable candidate. Its capital is state 216, its cores are `{ 146, 147, 215, 216 }`, and those states begin divided between Finland and the Soviet Union.
- Event 005 and Event 006 already own the Karelian lifecycle through `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/national_focus/005_soviet_collapse_republics.txt`, and `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt`, with related scripted triggers.
- Reusing `KAR`, `ARD`, or another Soviet-collapse tag without an explicit coexistence or exclusivity contract would violate this ledger.
- The live classifier also requires `brilliant_scientist_singularity_live_command_network` and `fallout_machine_emp_survival_verified`. Neither requirement has a complete live producer.

No free tag, dynamic slot, clone identity, or replacement candidate is reserved by this note. Machine protocol remains blocked pending an approved identity, exact state package, source-tag ownership rule, and event-package coexistence contract.

## Smallest dormant package candidate

`NZL` is the smallest reviewed dormant-package candidate. This finding does not establish activation readiness.

The candidate is narrow because it uses an existing tag, five exact NZL-owned core states, current capital 284, reviewed second capital 1079, existing vanilla country content, an already implemented maritime archetype classifier, and accepted country-memory direction. No bespoke Chaos Redux event package currently owns NZL. A dormant implementation would not require a new `common/country_tags` entry or a replacement `history/countries` file.

The dormancy contract is:

1. Give the Fallout focus tree `factor = 0` and `default = no`.
2. Gate the tree, decisions, events, ideas, starting forces, and AI behind one package-active country flag.
3. Do not set that flag and do not call `load_focus_tree` from successor allocation until every package surface is complete.
4. Skip the candidate if NZL or any required state fails grade, ownership, player reservation, or event-package reservation checks. Do not select a substitute.

Activation review still requires all of these surfaces:

- shared constants, triggers, effects, and a populated conflict-ledger row
- a maritime skeleton, an Oceania regional layer, and an NZL overlay
- decisions, missions, staged ideas, and complete idea lifecycles
- leader or council content, portraits, and cosmetic identity
- one-shot starting forces plus a reinforcement path
- route-specific AI
- country-memory events
- base and ideology-specific localisation
- flags, icons, sprite definitions, and an asset manifest
- event documentation, event-log and Event Details alignment, and spreadsheet alignment

All new cosmetic identifiers remain unassigned. This note does not reserve or claim any free identifier.

## Source-of-truth boundary

The accepted specifications under `docs/specs/air_cleanliness_fallout_specs/` remain unchanged. This ledger records reconnaissance for a later implementation decision. It does not accept a pilot candidate, approve a reduced package, authorize state transfer, or declare any country package ready for activation.
