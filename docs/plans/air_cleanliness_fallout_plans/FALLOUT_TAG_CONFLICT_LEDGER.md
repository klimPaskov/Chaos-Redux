# Fallout Live Tag Conflict Ledger

Status: required allocation ledger. This file records live ownership before any successor tag is assigned.

## Allocation rules

1. Preserve the human player country and its continuation candidates before general allocation.
2. Record every tag that is alive, releasable, dynamically reserved, or owned by another event package.
3. Reserve Fallout tags only after the live scan.
4. Treat the 99-successor matrix as a candidate pool rather than an instruction to spawn every candidate.
5. Never overwrite a live country or an event-owned dynamic country.
6. If a requested successor tag conflicts, choose another reviewed candidate from the same regional and identity package. Do not silently reuse a zombie tag.

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

The implementation ledger must record:

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

## Player reservation order

1. Store the player country scope.
2. Store its surviving core clusters and continuity memories.
3. Reserve the strongest valid continuation candidates.
4. Exclude those candidates from general successor allocation.
5. Run the general conflict ledger.
6. Present continuation only after all offered targets are confirmed live and playable.

## Audit status

The repository-level ownership families above are identified. The runtime tag-by-tag population remains an implementation obligation for the rewrite tranche. No successor allocation may be called complete until that live scan and player-first reservation are wired and audited.
