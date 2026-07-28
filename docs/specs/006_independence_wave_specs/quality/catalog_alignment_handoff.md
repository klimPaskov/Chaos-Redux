# Catalog alignment handoff

> Historical design handoff note (2026-07-28): the uploaded-row wording and
> `To Be Reworked` status below predate the doubled 6/8/10/14/20 ladder and the
> host-facing pre-wave crisis. Keep this file as accepted catalog direction,
> but use `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
> and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_pre_wave_crisis_and_doubled_ladder_2026_07_28.md`
> for current implementation status. This documentation reconciliation does
> not edit or export the workbook.

## Current catalog state

The uploaded Event 6 row is marked `To Be Reworked`. It currently describes evolution wave ranges of 4 to 6, 5 to 7, 6 to 9, 8 to 12, and 10 to 16. Those ranges are stale against the accepted doubled automatic wave ladder.

The catalog currently records:

- ID 6
- Independence Wave
- Minor Repeatable
- Cluster ID 2
- Member Severity Medium
- Status To Be Reworked

The Liberations cluster contains Events 5 and 6, uses Minor Repeatable classification, and has cluster chaos level 1.

## Source design that should drive the eventual update

### Event details direction

The final Event Details text should describe a synchronized wave of provisional states appearing from viable local claims, prepared institutions, regional identities, and historical polities. It should communicate that hosts retain a remnant and that the new countries face recognition, government, security, border, and patron problems.

It should not list exact modifiers, variable changes, rewards, candidate IDs, tag rules, internal rarity layers, or hidden high-chaos routes.

### Exact automatic wave ladder

The implementation and catalog must agree on these counts:

| Chaos band | Countries released by an automatic wave |
| --- | ---: |
| Calm World | 6 |
| Gathering Storm | 8 |
| Rising Chaos | 10 |
| Chaos Tier | 14 |
| Totalen Chaos | 20 |
| World Collapse | 20 |

The wave count is baseline chaos behavior. It must not be confused with the five evolution descriptions. World Collapse retains the 20-country count of Totalen Chaos and raises strength, instability, rarity, and ambition instead of replacing count with intensity.

### Pre-wave crisis surface

The current source implementation adds a host-facing, costed crisis before an ordinary wave. It is visible below 35% stability, when an enemy controls an owned state with resistance above 50, or when a country controls a foreign-owned state above 50 resistance. The 120-day mission spends the standard security commitment and, when pressure persists, queues the ordinary Event 006 entry through `chaosx.nr6.3`; a busy coordinator receives a bounded retry window before a blocked outcome. Invalid, cancelled, or exhausted resolution applies the documented pressure and cooldown consequences without changing ownership. The crisis never creates a country directly, bypasses host survival, or opens a second transaction. The implementation handoff records source-level validation; a fresh spreadsheet-worker cell comparison and live mission/queue evidence remain required.

### Evolution fields

The source design contains five genuine evolution tracks. The labels below are working labels and need final player-facing wording during implementation.

| Catalog field | Working evolution | Player-facing direction |
| --- | --- | --- |
| Evo I | Replicable Independence | Earlier released states help later claimants prepare institutions, exchange civil servants, and build recognition networks |
| Evo II | Dormant Nations | Historical states, local polities, indigenous nations, island identities, and regional overlays enter the viable pool |
| Evo III | Armed Birth | Some new states begin with defecting units, depots, volunteers, military factions, and immediate border pressure |
| Evo IV | Sovereign Congress | Released states prepare a common congress, shared recognition, arbitration, aid, and collective defense |
| Evo V | Open Sovereignty | High-chaos governments coordinate revisionism, radical blocs, unusual formables, and sponsorship of further breakaways |

Each evolution must support active Event 6 countries and a pre-fire evolved opening.

### Terminal field

Leave the terminal-scenario catalog field empty for Event 6.

### Super-event documentation

The event has two threshold-based super-event roles:

- formation of a meaningful league or coalition among Event 6 states
- emergence of a dangerous coordinated bloc, extreme high-chaos wave, or similarly global milestone

Ordinary waves do not receive super-events. The two milestone titles, text, buttons, quotes, and musical selections are approved in the research files. The dangerous milestone's image, cleared `6002` audio, five trigger predicates, history row, and settings-aware queued playback are implemented. Four predicates have reachable producers; the hidden-formable predicate remains dormant until FORM-42 or FORM-48 and its carrier are fully implemented and promoted. The exact `6001` recording is blocked for United States redistribution and remains absent until permission or a waiver clears it.

### Triggerable scenario proposal

The next free scenario slot in the uploaded scenario catalog is `SCN-008`. The working scenario label is `Every Flag`, not final localisation.

The scenario should state that every intensity attempts every viable candidate. Intensity changes starting territory, units, equipment, institution strength, and pressure. It does not reduce the candidate set.

The implementation uses six numeric type families:

- Sovereign Scatter
- Common Congress
- Wars of Separation
- Universal Belligerence
- Patron Worlds
- Great Partition

Universal Belligerence has three independently selectable rules: Former Hosts, Neighboring Releases, and Nearby Nonleague States.

The player-facing catalog therefore exposes eight selectable modes backed by the six numeric families. The runtime acceptance matrix is eight selectable modes by four intensities, or 32 cells. The three Universal Belligerence rules require separate acceptance rows and are not interchangeable proxies.

Final scenario detail text, type names, and intensity text must be written in game first and then mirrored into the catalog workbook.

## Cluster alignment

Keep Event 6 in Cluster ID 2, Liberations. The event can share candidate tags or regions with Event 5, but the cluster runtime must reserve tags and states before either member executes. A country released by Event 6 remains an Event 6 origin country and does not enter Soviet Collapse systems.

The user describes Event 6 cluster participation as Low. This is a participation or cluster-member intensity direction. It does not require changing the existing player-facing Member Severity value of Medium unless implementation and final localisation choose to do so.

## Workbook update order

1. Implement Event 6 and write final in-game Event Details and evolution wording.
2. Register and localize the triggerable scenario.
3. Finalize super-event roles and research packages.
4. Confirm cluster wording and member severity.
5. Run localisation and completion audits.
6. Send exact localisation keys and final wording to `chaosx_spreadsheet_doc_worker`.
7. Update the catalog workbook without paraphrasing mirror fields.

The `To Be Reworked` status at the top of this historical handoff is not a current workbook claim. The current workbook status and any changed Event Details/crisis-queue fields must be confirmed by the spreadsheet worker after the doubled-ladder/crisis wording is re-audited; no status promotion is implied here.
