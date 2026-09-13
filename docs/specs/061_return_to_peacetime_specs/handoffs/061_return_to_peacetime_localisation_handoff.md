# Event 061 localisation handoff

## Rule

Write final in-world localisation during implementation.

This handoff defines surfaces, viewpoint, dynamic information, and tone. It does not provide paste-ready text.

The fixed user-facing names are:

- Return to Peacetime
- Swords into Ploughshares
- The Great Demobilization
- Permanent Peace
- Peacetime Economy
- No Army

Other names in the source package are working labels and may be refined while preserving their role.

## Required key groups

Use the repository's current naming and file conventions.

Required groups:

- canonical event name and debug name
- baseline national report title, description, option, and tooltip
- AI-hidden national handler where text is technically required
- Evolution I warning, result, option, and dynamic result lines
- Evolution II warning, result, option, and dynamic result lines
- Evolution III settlement, exemption, deferral, forced result, voluntary result, and recovery milestone
- Return to Rearmament category title and description
- Rearmament Readiness name, value, bands, and qualitative pillar states
- every decision and mission
- every idea and stage
- Peacetime Economy and No Army
- Event Logs history and evolution entries
- Event Details event and evolution catalog text
- Peace cluster title, details, member roles, and skip result
- three achievements and requirement tooltips
- blocked-reason tooltips
- confirmation dialogs
- cost texticons and dynamic cost lines

## Baseline dynamic data

The national baseline report should support:

- country name
- eligible military factories before conversion
- military factories converted
- civilian factories added
- War Support before and after
- Stability before and after
- transfer lost to Stability ceiling
- economy law before and after
- conscription law before and after
- reconversion phase and expected duration
- current unresolved factory ledger
- Return to Rearmament category availability
- next active evolution warning when public

Use conditional lines so zero-result components are described accurately.

Examples of conditions that require different wording direction:

- zero military factories converted
- law already at ordinary floor
- incompatible custom law group
- country at war
- country is a large industrial major
- country is a small concentrated economy

Do not expose variable names.

## Readiness text

Display:

- total Readiness value
- current band
- broad meaning of the band
- qualitative industrial status
- qualitative economy-law status
- qualitative conscription status
- qualitative defence-institution status
- qualitative public and material status
- whether meaningful rearmament exists
- whether the current settlement requires a stricter last-chance condition

The five pillars should not look like five independent numeric currencies.

## Decision text requirements

Every decision needs:

- concise name
- in-world description
- visible cost
- duration
- target state when relevant
- exact result direction
- blocked reason
- cancellation or invalidation consequence when non-obvious
- structural-action credit when relevant
- emergency aftermath when relevant

### Arms contracts

Viewpoint:

Procurement offices, industrial planners, and suppliers.

Mention that contracts and tooling plans must be restored before broad factory reopening.

### State arsenal reopening

Mention the target state, exact batch, factory commitment, and one-for-one physical conversion.

Do not say that factories are being created.

### General Staff

Use institutional and planning language. Do not frame it as free army experience.

### Public defence campaign

Make the political tradeoff clear. Public confidence is being redirected toward military preparedness.

### Law restoration

Show current law and proposed next law.

Do not claim a higher final law than the project grants.

### Emergency actions

Use urgent official language.

Show the immediate survival result and the severe later disruption.

### Permanent civilian conversion

State that civilian factory levels remain and Event 61 restoration rights are abandoned.

Show exact units and states in the confirmation.

## Mission text requirements

### Inventory Liquidation

Show:

- deadline
- broad eligible stockpile families
- current protected families
- estimated loss range when safe to calculate
- selected civilian disposition

Do not promise an exact quantity at mission start when the final stockpile can change.

### Mustering Out

Show:

- deadline
- approximate eligible division target
- protected cadres or border regions
- current war-state effect
- that safe disband returns manpower and equipment

### National Defence Settlement

Show:

- deadline
- current Readiness and band
- immediate exemption status
- last-chance action progress
- active-war deferral status
- broad Peacetime Economy and No Army consequences

## Evolution result data

### Evolution I

- actual equipment removed by broad family
- protected families
- chosen disposition
- Reconstruction Materials tier and duration
- skipped unsupported families only when the skip is player-relevant

### Evolution II

- actual divisions demobilized
- manpower returned when measurable
- equipment returned by broad family when measurable
- protected formations or regions
- Veteran Reintegration tier and duration

### Evolution III

- exemption, deferral, voluntary adoption, or forced adoption
- additional factories converted
- conventional divisions demobilized
- current extreme laws
- Peace Dividend state
- recovery route availability

## Idea text

### Industrial Reconversion Shock

Write three stage descriptions that explain the changing industrial condition.

Do not create three unrelated national crises.

### Reconstruction Materials

Describe recovered material and machinery entering civilian projects.

### Veteran Reintegration

Describe skills returning to the economy and the short-term pressure on jobs, housing, and administration.

### Peace Dividend

Describe civilian capacity released by sustained disarmament.

### Improvised Rearmament

Describe rushed procurement, weak training, and disrupted production.

## Law text

### Peacetime Economy

State that military production institutions have been dismantled and civilian recovery receives priority.

Show severe military and conversion restrictions in the law tooltip.

### No Army

State that the conventional standing army has been legally abolished.

Show recruitment and training restrictions.

Do not imply that every special event-owned unit is deleted when owner rules exclude it.

## Event Logs and Event Details

### History

Use the real date and repeat count.

Summarize global affected-country and factory totals without listing every country.

### Evolution history

Use actual activation metadata.

Do not copy event catalog stage or tier into every historical row unless the log contract requires it.

### Catalog

Use stable public premises.

Do not expose hidden thresholds, code identifiers, or anti-exploit state.

## Peace cluster text

Explain the two-stage de-escalation.

Event 9 can end eligible wars.

Event 61 can then unwind wartime institutions.

Provide a concise skip description when White Peace finds no valid war without presenting the cluster as failed.

## Achievement text

### The Arsenal Returns

Describe the forced extreme-law recovery challenge and visible banned shortcuts.

### Swords, Ploughshares, Swords

Describe the required reconstruction, rearmament, and defensive victory.

### The Arsenal Sleeps

Describe the five-year high-Chaos survival under both extreme laws.

Do not expose internal bit masks, cycle variables, or debug exclusions.

## Audit checks

`chaosx_localisation_auditor` must verify:

- every referenced key exists
- no raw key appears in game
- no working label or prompt language leaked into final text
- dynamic numbers match implemented effects
- state and country names scope correctly
- pluralization works for 0, 1, and many
- law before and after values are correct
- mission deadlines are accurate
- blocked reasons identify the real missing condition
- Event Details metadata does not leak into normal history rows
- no unsourced quote or cultural reference appears
- serious demobilization surfaces avoid cheap jokes
