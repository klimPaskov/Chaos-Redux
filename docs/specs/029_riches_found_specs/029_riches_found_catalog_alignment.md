# Event 029 catalog and Event Details alignment

## Current source discrepancy

The supplied CSV export lists Event 029 as follows:

| Field | Supplied CSV value |
| --- | --- |
| ID | `29` |
| Event Name | Riches Found |
| Details | A chance discovery brings a country a large political windfall and turns one state into a source of continuing income. |
| Evolution fields | Blank |
| World-End Scenario | Blank |
| Type | Minor Repeatable |
| Cluster ID | Blank |
| Member Severity | Blank |
| Status | Unavailable |

The user-provided catalog entry in this task identifies the status as `To Be Reworked`.

The authoritative XLSX workbook was not supplied, so this package does not decide which status label is current in the repository.

Implementation must inspect `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, preserve its active status vocabulary, and update that workbook only after the event implementation facts are verified.

The three CSV files remain export-only snapshots and must not be edited directly.

## Stable catalog identity

The following fields do not change:

| Field | Required value |
| --- | --- |
| ID | `29` |
| Event Name | Riches Found |
| Type | Minor Repeatable |
| Cluster ID | Blank |
| Member Severity | Blank |
| World-End Scenario | Blank |

Event 029 remains outside every event cluster.

It does not receive a manual triggerable scenario through this specification.

It does not receive a public or hidden world-end branch through this specification.

## Status transition direction

Before implementation, preserve the workbook's current unreworked or unavailable state.

After the complete event has been implemented and the source checks have passed, move it to the repository's status for content awaiting live testing if that status exists.

After live testing and catalog verification, move it to the repository's fully playable or implemented status according to current catalog practice.

Do not mark the event playable merely because the specification package exists.

Do not mark it implemented while required decisions, AI, assets, localisation, Event Details, evolution logs, documentation, or catalog fields remain missing.

## Event Details premise direction

Event Details should explain the public premise without exposing exact reward values, hidden pressure formulas, future supernatural outcomes, or implementation structure.

The entry should communicate these facts:

- One country discovers exceptional mineral wealth in one state.
- A rush of labor, capital, criminals, guards, officials, and foreign interests develops around the site.
- The mine remains tied to the state and can enrich whoever controls it.
- Development, public revenue, security, concessions, and extraction policy shape what the site becomes.
- The discovery can remain productive or create deeper political and human costs.

The entry should not name Gold Disease, demons, hidden bargains, late crisis outcomes, exact thresholds, Event 18 separation rules, or controller aggregate formulas.

The text should focus on the state, the people arriving, the struggle over access, and the political choices created by the discovery.

It should avoid a technical reward list, generic administrative reports, and direct statements that the event is a warning.

## Catalog Details field direction

The catalog Details field should remain compact and player-facing.

It should cover:

- the random recipient and selected state
- the immediate political windfall
- persistent controller-linked income and industrial value
- the mining rush and conflict over claims, revenue, concessions, security, and control
- the fact that the mine follows state control

It should not list every decision, every modifier, exact scaling, evolution gates, hidden variables, or late supernatural outcomes.

The current one-sentence CSV summary is accurate at a high level but too narrow for the complete event.

The implementation workbook update should expand it enough to distinguish Event 029 from Event 18 while remaining shorter than the event documentation.

## Evolution field alignment

Only three catalog evolution rows are populated.

The project planning rule allows one evolution stage per chaos tier.

The user fixed Evolution I at 600+, leaving the next two higher tiers for Evolution II and Evolution III.

### Evolution I field

Working identity: The Resource Curse.

The catalog field should communicate that the mine's wealth starts capturing the state, government, companies, security services, and public spending.

It should mention the choice between public revenue, national control, private domination, concession dependence, and tolerated corruption.

It should explain that harder extraction improves the mine while worsening dependence and capture.

It should not reveal exact corruption values or the late Gilded Sovereignty outcome.

### Evolution II field

Working identity: Gold Disease.

The catalog field should communicate that obsessive possession spreads among workers, officials, guards, soldiers, and administrators connected to the mine.

It should describe theft, hoarding, barricaded workings, violent disputes, and the choice between revenue sharing, replacement, intervention, quarantine-style isolation, closure, or sealing deeper sections.

It should make clear that continued extraction raises output and crisis severity.

It should not describe the crisis as an ordinary biological pathogen or connect it to the biological warfare system.

### Evolution III field

Working identity: Demons Beneath the Mine.

The catalog field should communicate that deep excavation reaches a fictional corrupting underground force.

It should mention disappearances, altered workers, impossible accidents, mass violence, military breakdown, and severe state pressure.

It should communicate the core choice between sealing, evacuation, religious or occult assistance, controlled exploitation, purges, and agreement.

It should not reveal the exact terms of The Bottomless Account or identify the force as any existing Chaos Redux underground actor.

### Evolution IV and Evolution V fields

Leave both blank.

The Gilded Sovereignty and The Bottomless Account are late outcomes inside existing evolution tracks.

They are not registered evolution stages and must not receive separate evolution log rows or catalog evolution fields.

This preserves all planned late-game content while following the one-evolution-per-tier rule.

## Evolution Details catalog direction

The Event Details evolution catalog should show three independently controlled entries.

Each entry should have:

- one stable event ID link to Event 029
- one stable evolution type ID
- one display stage
- one chaos tier
- a premise that describes the new public situation
- enabled or disabled state

The preview surface must not show fake history dates, fake sequence numbers, or an actor before the evolution has actually been logged.

When an evolution is disabled, baseline mine progression must remain playable and later enabled sibling content must not be corrupted by disabled-stage flags.

## Event history direction

A normal Event 029 firing creates one event history entry with the receiving country as actor.

The history detail should identify the selected mine state through dynamic text when the repository's current history surface supports it.

Normal baseline phases, decisions, missions, claims, contracts, raids, and closures do not create evolution log rows.

Actual evolution milestones create evolution log entries with the current controller as actor.

If the mine changes controller after an evolution, the existing log actor remains historical.

Future evolution incidents use the current controller as the active event actor.

## Event list availability direction

The Events tab should show a live weight only when at least one valid country and state pair exists.

It should show `N/A` when no valid pair exists.

Reasons include:

- no ordinary eligible country exists
- every otherwise valid country lacks an eligible state
- every suitable state already carries an Event 029 mine or a conflicting persistent site
- only excluded special or nonhuman actors remain

A temporary shortage of perfect high-value targets should not make the event unavailable when a lower-weight valid state still exists.

## Event 18 separation in catalog text

Event 029 catalog wording must not reuse Event 18 language about deposits beneath deposits, caves, fossils, attacks from existing underground actors, Oth-Kesh, or The World Opens Below.

Event 18 remains the resource-deposit and underground-breach event.

Event 29 remains the wealth-governance, ownership, corruption, obsession, and fictional bargain event.

A player reading both rows should understand that they create different campaign systems.

## Workbook update checklist

When implementation facts exist, the spreadsheet worker should:

1. Read the authoritative workbook and current Event 029 row.
2. Confirm the workbook's current status vocabulary.
3. Update Details and Evolution I through III to match final in-game Event Details wording.
4. Keep Evolution IV, Evolution V, World-End Scenario, Cluster ID, and Member Severity blank.
5. Keep Type as Minor Repeatable.
6. Set status according to the verified implementation and testing state.
7. Preserve workbook structure, formulas, filters, validation, and formatting.
8. Run `python .tools/export_event_catalog_csv.py` from the mod root.
9. Confirm that all three generated CSV snapshots were refreshed from the workbook.
10. Report any source discrepancy instead of editing the CSV by hand.
