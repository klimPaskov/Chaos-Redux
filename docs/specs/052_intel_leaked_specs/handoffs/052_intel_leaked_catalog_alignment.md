# Event 052 Catalog Alignment Handoff

The authoritative catalog source is:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

The three CSV files are export-only snapshots. Do not edit them directly.

After workbook changes, run:

```text
python .tools/export_event_catalog_csv.py
```

## Event 52 row

Update the Event 52 row after implementation facts and final in-game localisation are available.

Required identity fields:

- ID: `52`
- Name: Intel Leaked
- Type: Minor Repeatable
- Chaos level: `1`
- Cluster ID: `10`
- Cluster severity: Low
- Status after complete source implementation but before live verification: Needs Testing

The Details field should describe the player-facing premise:

- one player-controlled country or major power suffers a massive classified leak
- foreign governments temporarily gain broad knowledge
- the target races to make the files obsolete
- damage control, network protection, and deception shape the outcome
- the source remains unresolved

Do not list raw Exposure numbers, hidden Reliance, exact costs, file names, or implementation history.

## Evolution I field

Name direction: Deep Files.

Summary direction:

- available from 400 Chaos
- later incidents contain current plans, active operations, identities, contacts, shortages, research priorities, commander information, and mobilization details
- an incident already in progress can receive a delayed deeper tranche
- recovery becomes more expensive and personnel danger rises

Use final in-game evolution wording.

## Evolution II field

Name direction: Total Compromise.

Summary direction:

- available from 800 Chaos
- one firing can expose several countries at once or produce one exceptionally severe target
- every target has separate archive and recovery state
- wartime enemies can hold exceptional information about each other

Use final in-game evolution wording.

## Intelligence cluster row

Update Cluster 10 member IDs from the current Event 039-only state to:

```text
39, 52
```

Preserve Event 039 as the Medium-severity fire-once member.

Add Event 52 as the Low-severity repeatable member.

Review the cluster Type field because the members have different event types. Use the established workbook convention for mixed-type clusters. Do not assign one member's type to the other.

The cluster detail should remain player-facing and can mention:

- leadership shocks
- leaked archives
- endangered networks
- investigations
- counterintelligence
- deception

Do not expose member selection weights, internal adapters, or skip-code names.

## Alignment checks

- Event Details premise and workbook Details wording agree.
- Evolution preview wording and workbook evolution fields agree.
- Event name spelling is consistent across event names, debug names, localisation, docs, and workbook.
- Cluster row identifies both members and their correct severities.
- Status changes only when implementation evidence supports it.
- Exported CSVs are regenerated from the workbook and not hand-edited.
