# Event 064 Catalog and Repository Reconciliation

## Accepted design source

The user's current brief is authoritative for Event 064 identity. Project-facing package paths and identifiers use the zero-padded form `064`, while the established runtime namespace remains `chaosx.nr64.*`.

- Event ID 064
- Border Fortifications
- Minor Repeatable
- To Be Reworked
- Chaos Level 1
- Sudden Abundance, Medium
- Military Preparation, Medium
- Defense in Depth at 200 or more Chaos
- Fortress States at 400 or more Chaos
- Fortress World at 600 or more Chaos

## Current exported event-catalog problem

The supplied event CSV contains this stale Event 064 state:

- event name uses a lower-case second word
- details describe country leaders developing unexpected talents
- evolution fields are empty
- cluster fields are empty
- type and Chaos level are otherwise correct
- status is To Be Reworked

The leader-trait detail belongs to another idea and must be removed from Event 064.

Do not patch the CSV directly. Update the authoritative workbook and regenerate all catalog exports.

## Current exported cluster-catalog problem

The supplied cluster CSV contains the older implemented cluster set and several placeholder cluster rows. It does not yet contain accepted Sudden Abundance or Military Preparation definitions and does not express Event 064's two memberships.

The user supplied a newer accepted cluster map through Events 001 to 064. That map is the design input for this package.

Implementation must reconcile:

- stable cluster identifiers
- cluster names and descriptions
- unlock level and type
- Event 064 membership in both clusters
- Medium severity in both
- settings and details views
- automatic arbitration for multi-cluster members
- manual cluster trigger behavior
- event and cluster history
- workbook and CSV exports

Do not assign numeric cluster IDs in Event 064 files before the authoritative registry collision check.

## Current repository Event 064 shell

The connected repository contains `events/064_border_forts.txt` with:

- namespace `chaosx.nr64`
- hidden entry `chaosx.nr64.1`
- a global `every_country` report dispatch
- report event `chaosx.nr64.2`
- report sprite `GFX_report_event_border_fortifications`
- one option that adds two bunker levels instantly in every controlled state's border provinces

This shell proves the existing namespace and report-art identity. It does not satisfy the current design.

Missing current surfaces include:

- coherent one-token transaction
- fixed firing-time snapshot
- duplicate protection
- per-country result counts
- one-level gradual repeat design and caps
- evolution lifecycle
- strategic anchor and depth selection
- Fortress State support packages
- internal redoubts
- player response postures
- decisions and missions
- AI strategy and probability evidence
- direct Chaos impact map
- two cluster memberships
- Event Details and modern history integration
- achievements
- complete asset family
- catalog correction
- comprehensive validation

The new implementation should replace the shell. It should not create a second Event 064 namespace or leave the old two-level option as a hidden duplicate.

## Current localisation problem

The connected repository contains `localisation/english/064_border_forts_l_english.yml` with a short report that says the government ordered the fortifications and engineers are building them.

That explanation conflicts with the accepted sudden global abundance premise. Final text should describe completed defenses appearing across the world's current frontiers, then ask the receiving country how to respond.

The current file also contains a duplicate-looking second option key even though the event shell uses one option. The localisation audit must remove obsolete keys after the new report options are finalized.

## Current report sprite

The repository maps:

- `GFX_report_event_border_fortifications`
- `gfx/event_pictures/064_border_forts/report_event_border_fortifications.dds`

Preserve this sprite identity and path family when the current asset can be replaced in place safely. A migration is acceptable only when the asset handoff documents every reference and no stale sprite remains.

## Current cluster runtime gap

The repository's current event-cluster documentation describes the older implemented cluster set. Sudden Abundance and Military Preparation are not yet runtime definitions in that source.

Event 064 cannot claim both cluster memberships through documentation alone. The shared runtime must support:

- both new cluster definitions
- one event belonging to more than one cluster
- one automatic cluster context per selected event incident
- exact manual cluster selection
- one member execution per cluster incident
- member and normal history
- settings and event-log views

If this shared work cannot land with Event 064, record it as a blocker and keep the event's standalone route valid.

## Registry and integration areas to inspect

The implementation worker should inspect current repository ownership before editing. Likely areas include:

- `events/064_border_forts.txt`
- `localisation/english/064_border_forts_l_english.yml`
- Event 064 specific scripted triggers, effects, constants, decisions, and modifiers
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- event-log effects and scripted localisation
- evolution registration and history
- Event Details data and scripted localisation
- cluster constants, effects, events, GUI, settings, and documentation
- achievements registration, tracking, localisation, and icons
- `interface/chaosx_pictures.gfx` or the current Event 064 asset owner
- authoritative event and cluster workbook
- `.tools/export_event_catalog_csv.py`
- permanent event overview documentation

The coding prompt gives the implementation agent the full integration contract. It does not require blind creation of every listed path when a current shared owner already exists.

## Proposed catalog content direction

### Event row

| Field | Direction |
| --- | --- |
| Event Name | Border Fortifications |
| Details | Synchronized defenses appear along every valid current foreign land frontier worldwide. Each affected country then decides how to use, supply, or overcome the new lines. |
| Evo I | Defense in Depth strengthens selected frontier anchors and creates bounded secondary positions near major routes and objectives. |
| Evo II | Fortress States turns selected border states into integrated sectors with stronger forts, anti-air, radar, supply work, and selective coastal defenses. |
| Evo III | Fortress World creates bounded internal redoubts around capitals, major victory points, supply hubs, and critical approaches. |
| Type | Minor Repeatable |
| Chaos level | 1 |
| Primary cluster | Sudden Abundance |
| Additional cluster | Military Preparation |
| Severity | Medium in each cluster |
| Status | To Be Reworked during planning, then Needs Testing after complete implementation wiring |

These are spreadsheet content directions. The final workbook wording should receive the normal localisation and documentation review.

## Export procedure

After authoritative workbook edits:

```text
python .tools/export_event_catalog_csv.py
```

Then inspect all three exports for:

- stable schema
- Event 064 identity
- complete evolution fields
- both cluster memberships through the accepted catalog model
- no unrelated leader-trait text
- no hand-edited divergence from workbook output

## Reconciliation acceptance

Repository reconciliation is complete only when:

- one canonical Event 064 implementation exists
- namespace and entry id remain stable
- obsolete two-level option logic is gone
- obsolete localisation keys are gone
- report sprite resolves
- Event 064 is registered as Minor Repeatable
- Event Details and history are aligned
- all three evolutions are registered and logged correctly
- both clusters are real runtime memberships
- multi-cluster arbitration is proven
- achievements and decisions are registered
- permanent docs describe current implementation
- authoritative workbook is corrected
- generated CSVs match the workbook
