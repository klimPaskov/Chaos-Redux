# Event 037: Mysterious People

## Part 2: Population creation and the newcomer ledger

## Real population is authoritative

Every person created by Event 037 is real state population.
The event never represents the newcomers through recruitable manpower alone, a national spirit, or an abstract country total.
Every system that reads state population, including recruitment, Deaths, Famine, Migration, bombing, nuclear and disease mortality, and occupation, sees the larger population through its ordinary rules.

The ledger below records provenance and settlement only.
It never replaces real population as the gameplay source of truth.

## Positive population helper

**Implemented.** The repository had a neutral loss helper, `apply_state_population_loss_without_recruitable_manpower_gain` in `common/scripted_effects/chaosx_dynamic_effects.txt`, and Event 037 added the neutral gain helper beside it.
The positive credit pattern exists twice in owner-specific form: `camp_occ_apply_population_credit` and `civilian_transfer_apply_destination_credit`.
Both apply state `add_manpower`, measure the real population change, and remove the recruitable manpower the engine grants the owner and controller at the same moment.

Event 037 adds the neutral counterpart, planned as `apply_state_population_gain_without_recruitable_manpower_gain`, with the same measured-result contract, and documents it in `common/scripted_effects/chaosx_dynamic_effects.md`.
The grant uses the measured applied amount for every later step.

Removing the instant recruitable gain is how newcomers settle into the army: they become recruitable through the engine's ordinary recruitable-population growth instead of all at once.
Whether that growth is gradual enough is an engine-proof gate for implementation.
Installed documentation cannot prove the growth rate, so the Newcomers modifier carries the closest faithful mechanism: a `conscription_factor` equal to minus the unsettled share, which keeps unsettled newcomers out of the recruitable target until they settle. Accepted by the release orchestrator on 2026-10-10 under the brief's instruction to implement the closest faithful mechanism and record the deviation; live confirmation is user-owned.

## Grant model

Each state uses its own pre-fire population `P`.
Previous newcomers count in `P`, so repeated firings compound naturally.

```text
practical floor = minimum of (nominal floor, P x small-state ceiling)
grant = minimum of (stage cap, maximum of (P x stage ratio, practical floor))
```

| Stage | Ratio | Nominal floor | Per-state cap | Small-state ceiling |
| --- | ---: | ---: | ---: | ---: |
| Baseline | `2.5%` | `1,000` | `1,500,000` | `5%` |
| Evolution I | `6%` | `2,500` | `3,000,000` | `10%` |
| Evolution II | `12%` | `5,000` | `7,500,000` | `20%` |
| Evolution III | `25%` | `10,000` | `20,000,000` | `40%` |

The values are planning anchors held in `common/script_constants/` and tuned against the installed state-population distribution.
Worked examples are in the [balance matrix](../quality/037_mysterious_people_balance_matrix.md).

Rules:

- one grant per state per firing
- the grant is rounded to whole people
- the ledger records the measured applied amount, never the requested amount
- a state that becomes invalid during the pass receives nothing and keeps its ledger unchanged
- the grant does not shrink because a state already holds many newcomers

## State ledger

Each state stores three values.

| Value | Meaning | Changed by |
| --- | --- | --- |
| Newcomer share | The fraction of the state's living population that arrived through Event 037 | Grants, and arrivals through the civilian transfer primitive |
| Unsettled newcomers | People from recent grants who have no settled home and work yet | Grants add, monthly settlement and projects remove, Breakdown flight removes |
| Settlement rate | People settled per month | Recomputed at firings, project completion, stance change, and hotspot refresh |

The newcomer count is derived as share times live population.
Storing a share instead of a count means every ordinary population loss and every proportional move already keeps the ledger correct.
Famine, bombing, nuclear attack, disease, disasters, cannibalism, camps, and war kill newcomers in proportion to their share without any Event 037 callback, and the count can never exceed real population or fall below zero.

The share is stored as a scaled fixed-point value (for example parts per hundred thousand) so small shares keep their precision.

Unsettled newcomers are clamped to the derived newcomer count after any read, so losses that shrink the state also shrink its unsettled backlog.

### Share changes

A grant `G` into a state with live population `P` and share `s` sets the new share to `(s x P + G) / (P + G)`.

An arrival through the civilian transfer primitive blends the destination share with the origin share for the measured survivors.
This is one Event 037 call in the primitive's finalization, and it is the only shared-system hook the ledger needs.
Population credited by other owners outside that primitive is treated as having the destination's share, which keeps the ledger inside real population.

### Settlement

Each month a state settles unsettled newcomers equal to its population times the base settlement rate, adjusted by:

| Factor | Planning effect |
| --- | --- |
| Infrastructure level `L` | multiplier `0.6 + 0.08 x L` |
| Open Integration stance | `x 1.25` |
| Restricted Registration stance | `x 0.75` |
| Registration Drive active | `x 1.5` |
| Origin register adopted (Event Option 24.b) | `x 0.667` for a year |
| Completed Emergency Housing | `+25%` of the base, once per state |
| Completed Roads and Water | `+25%` of the base, once per state |
| Completed New City | `+50%` of the base, once per state |
| Famine stage acute shortage or worse | `x 0.5` |
| Occupied (controller is not owner) | `x 0.5` |

The planned base rate is `1%` of state population per month.
A baseline grant of `2.5%` therefore settles in about two and a half months, and an Evolution III grant of `25%` needs two years without help.

## Country and world counts

| Count | Shown to | Updated |
| --- | --- | --- |
| Newcomers living in the country | Player, in the category header | At every firing from the world pass, and on state ownership change |
| Unsettled newcomers in the country | Player, in the pressure tooltip | At firings, on the monthly pulse, and when projects or flight remove people |
| Living newcomers in the world | Event Log detail and milestones | At every firing from the world pass |
| People created by the latest firing and in total | Event Log detail | At every firing |

The country count is labelled as the figure from the latest count, because ordinary deaths between firings lower it without a recount.
The world pass at each firing refreshes it exactly.
Lifetime newcomer deaths and lifetime transfers are not tracked, since no decision uses them.

## Ownership and control

The ledger belongs to the state.
When ownership changes, the state's newcomers and unsettled backlog move with it, the old owner's counts fall, and the new owner's rise through the existing `on_state_control_changed` path.
Annexation and liberation cannot duplicate or erase newcomers.

## Runtime cadence

### At firing

One world pass applies grants, refreshes every state's settlement from the months elapsed since its last update, rebuilds country and world counts, and picks each country's hotspots.

### Between firings

A self-rescheduling hidden host event runs every 30 days.
It processes only countries with unsettled newcomers.
For each, it settles its hotspot states exactly, reduces the rest of the country's unsettled backlog by its stored national settlement rate, recomputes pressure, and calls the Famine and Migration adapters for qualifying hotspots (Part 3).

A **hotspot** is one of a country's states with the highest state pressure, up to `3` per country.
Hotspots are the only states the monthly pulse reads one by one, and the only targets for state decisions.
Unsettled newcomers can only grow at a firing, so the hotspot list changes only at firings, ownership changes, and when a hotspot falls to zero.

A country with no unsettled newcomers leaves the registry.
There is no daily, weekly, or monthly scan of every state.

## Integrity rules

- A transaction with missing proof applies no guessed population change.
- A repeated firing identity cannot apply a second grant after reload or from a delayed report.
- All ledgers, counts, milestone flags, stances, projects, and the host pulse survive save and reload.
- A debug action can rebuild counts from state data, and that repair is never part of normal runtime.
