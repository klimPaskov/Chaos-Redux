# Event logs, Event Details, catalog, cluster, and localisation

## Registration surfaces

Implementation must align these surfaces in one change:

- Event 38 script and namespace
- Fire-Once category registration
- minimum Chaos level 1
- event enable and disable state
- default reworked-event allowlist
- event name mappings
- event log actor mapping
- Event Details content
- evolution catalog and history
- public world-end row
- Formables cluster membership
- triggerable scenario registry
- documentation
- authoritative workbook
- generated CSV exports

The event remains default disabled while its status is `To Be Reworked`. Add it to the normal default-enabled allowlist only after the event is complete.

## Normal History row

The initial Event 38 firing creates one History row with:

- Event 38
- firing date
- Malta Crusader actor
- Minor Fire-Once type
- relevant origin or target flag according to current row design

Internal follow-up events do not create new random-event History rows.

If Event 38 fires through a cluster, the event still creates its normal member History entry while the cluster creates one global pacing record.

## Evolution log

Only these milestones enter the Evolutions history:

1. The Orders Return
2. The Crusader Principalities
3. The Age of Holy War

Each row needs:

- sequence
- date
- Event 38 source
- evolution title
- tier
- stage
- Malta or successor actor
- enabled state where the current UI displays it

Ordinary order incidents, principalities, relics, Holy See formation, Kingdom of God, Teutonic Order, Atlantis, and Holy World readiness are not Event 38 evolution rows.

### Event Details evolution catalog

The catalog preview describes the three public evolution premises. It does not print fake dates, fake sequence numbers, or actor history.

### Disabled evolutions

Disabled evolutions do not set recorded flags, unlock content, or appear as completed.

## Event Details premise

The public Event Details text should explain:

- Malta is released as a crusader state with occupied footholds and immediate regional wars
- the army uses unusual medieval-modern formations
- the campaign can create military-order governments, principalities, the Holy See, and the Kingdom of God
- defeat can open an Eleventh Crusade recovery
- higher Chaos can add more orders, principalities, foreign religious support, relics, and Blessed formations

It should not reveal:

- Teutonic Order
- Blessed Hitler or transformed hidden leaders
- Operation The Final Crusade
- Atlantis
- the two-year betrayal timer
- the 90 percent AI choice
- Atlantean claims or extermination
- exact hidden values
- exact evolution MTTH
- implementation file names or variables

## Public world-end row

Event 38 has one public world-end row:

### The Holy World

The detail should explain:

- a Papal crusader state can build a worldwide believer bloc at extreme Chaos
- the Pope must first control one complete continent directly or through approved Papal subjects
- at 1000 or more Chaos the final crusade divides governments between submission and resistance
- normal automatic event firing stops under the shared world-end state

The row has its own persistent checkbox. Toggling it does not toggle Event 38 or hidden routes.

## Hidden route visibility

The Teutonic Order and Atlantis:

- do not appear as public world-end rows
- do not appear in public evolution previews
- do not appear in public catalog detail fields
- do not appear in normal scenario controls
- can use internal stable identities and hidden flags
- become visible through their own events only after reveal

## Formables cluster

The accepted membership is:

- Event 38 Malta Crusaders
- Formables cluster
- Cluster ID 6
- High member severity

The supplied current cluster CSV does not yet reflect this final membership. Implementation must update the authoritative XLSX and regenerate exports.

Cluster behavior:

- Event 38 minimum Chaos level is checked before cluster logic
- the Formables cluster uses its own unlock and member gates
- Event 38 can fire as the selected member or through valid cluster participation
- member effects apply once
- one cluster firing counts as one global pacing event
- Event 38's Fire-Once weight and history update normally
- cluster history records actor, tier, fired or skipped result, and reason

Do not edit the export CSV directly.

## Manual scenario catalog

The scenario working ID is SCN-015. The final ID requires a workbook collision check.

Workbook fields need:

- stable ID
- name
- player-facing details
- optional type options
- intensity scaling summary
- implementation status

The scenario text should explain immediate Papal actor setup, world division, intensity, and terminal war without listing internal bypass flags.

## Catalog event row

Suggested player-facing field direction:

### Details

Describe Malta's immediate release, occupied footholds, regional wars, custom medieval-modern army, order politics, and possible state formation.

### Evolution I

Describe the return of additional orders, foreign volunteers, specialized formations, and deeper rivalry.

### Evolution II

Describe the creation of principalities, local governments, church disputes, and subject obligations.

### Evolution III

Describe wider religious support, relic claims, Blessed formations, and foreign movements.

### World-End Scenario

Describe The Holy World only. Hidden routes stay absent.

### Type and classification

- Minor Fire-Once
- Chaos level 1
- Cluster ID 6
- High severity

The event status changes to the accepted implementation status only after completion evidence.

## Player-facing prose rules

Every Event 38 prose surface follows these rules:

- no em dash
- no semicolon in sentences
- no thesis, antithesis, synthesis framing
- no staccato drama
- no stock contrast formulas that split one thought into a forced reversal
- no raw update history
- no developer-facing terms such as reworked, hardcoded, capped, fallback, setup transaction, or bypass in player text
- no secret-route spoilers
- no invented quotes
- no text copied from implementation prompts
- no whole-population religious stereotypes

## Tone by surface

### Malta event text

Use direct military and political detail. Mention forts, ports, banners, orders, civilians, supply, and sacred centers.

### Order events

Give each order a distinct institutional voice. Hospitallers speak through care and fortification. Templars use finance and command. Teutonic chapters emphasize discipline and heavy armour. Naval Orders focus on ports and sea routes. Siege Brotherhoods focus on engineering and walls.

### Principalities

Use local government, charter, church, succession, and military obligations. Avoid generic puppet language.

### Relics

Maintain uncertainty. Describe custody, witnesses, traditions, tests, disputes, and public belief. Do not confirm supernatural truth.

### Papal route

Use religious authority, law, pilgrimage, Rome, Jerusalem, and international submission. Avoid empty apocalyptic filler.

### Nazi and Atlantis routes

Call racial ideas regime claims, pseudo-science, mythology, or propaganda. Do not present them as factual ancestry.

### Atrocity text

Use serious in-world language and exact public consequences. Avoid cheap humour, spectacle, and graphic detail.

## Option direction

Important options need:

- speaker or institution
- public action
- visible consequence
- serious, ironic, bureaucratic, frightened, or arrogant tone as appropriate
- researched cultural reference direction when used

Do not draft final option text in specs. The implementation agent writes finished wording after research.

## Dynamic localisation

Dynamic text should support:

- Malta or successor name
- Grand Master, Pope, or council leader
- selected order
- selected state or region
- principality name
- active demand
- current value band
- selected continent
- selected Holy World side
- current route and government

Fallback branches must be neutral and cannot leak another country's wording.

## Event-detail actor handling

The event actor can transform from Malta into the Holy See or Kingdom of God. Event Details should preserve the Event 38 identity and show the current valid actor where supported.

If no Event 38 actor survives, the detail view should show a clear historical or defeated state without invalid scope text.

## Workbook workflow

1. inspect the authoritative workbook
2. update Events, Clusters, and Scenarios sheets as required
3. preserve formatting, filters, formulas, and validation
4. save the workbook
5. run `python .tools/export_event_catalog_csv.py`
6. review all three generated exports
7. confirm in-game wording and workbook wording match

The spreadsheet worker should run only after implementation facts and localisation are final.

## Localisation audit

Before completion, audit:

- missing keys
- duplicate keys
- BOM encoding
- raw variables or debug prose
- key namespaces
- dynamic fallbacks
- cost texticons
- state and country names
- Event Details and workbook text alignment
- hidden route leaks
- super-event text and quote attribution
- all route, focus, decision, idea, unit, equipment, achievement, and scenario keys
