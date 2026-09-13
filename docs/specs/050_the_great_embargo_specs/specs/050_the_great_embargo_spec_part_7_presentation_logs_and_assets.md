# Event 050: The Great Embargo

## Part 7: Presentation, event logs, localisation direction, and visual assets

This file gives presentation direction. It does not provide pasteable player-facing localisation.

## Presentation purpose

The event should make economic isolation visible through halted shipments, empty loading areas, rerouted cargo, rationing, port inspections, missing foreign representatives, and hurried domestic substitution.

The event should avoid treating the crisis as a spreadsheet presented through popups. Numbers belong in the Pressure display and concise tooltips. Reports should focus on consequences that people, factories, armies, shipping firms, and governments can observe.

## Event surface map

### Entry and target opening

The canonical entry event begins the target and coalition transaction. The target receives the first player-facing report after the selected scope and coalition are valid.

The opening report should communicate:

- which country is targeted
- the public reason or accusation
- the convenor
- the most important participating powers
- the first visible trade or supply disruption
- the fact that a response category is available

It should not expose hidden dependence values, coalition coefficients, or future evolution conditions.

### Coalition opening reports

Core enforcers receive compact commitment events. Human-controlled countries receive direct choices. AI-only minor compliance partners can be handled without visible popups.

The report viewpoint should match the country receiving it. A core enforcer sees enforcement costs and strategic aims. A neutral sees commercial opportunity and risk. A faction partner of the target sees pressure to choose sides.

### Target threshold reports

A report can fire when Pressure first enters:

- porous embargo
- severe isolation
- near-total isolation
- collapsing coalition

Do not repeat the same threshold report after every later fluctuation. Each first-entry report should have a one-shot marker within that crisis.

### Decision outcome reports

Use reports for outcomes that change the crisis identity:

- first replacement route opens
- major smuggling network exposed
- core enforcer defects
- coalition-wide concession vote begins
- target commits to defiance
- resource-seizure preparation becomes public
- first secondary sanction is imposed
- several embargoed targets form a cooperation network

Routine cost payments and small Pressure changes should remain in decision feedback and tooltips.

### Coalition review reports

A normal monthly review can resolve silently when nothing important changes. A report appears when the review renews enforcement, replaces the convenor, triggers a defection cascade, starts terminal fatigue, or changes the stage.

### Resolution reports

Each resolution family needs a distinct target report and a compact foreign reaction package.

The report should identify:

- why the embargo ended
- what the target kept or conceded
- which relationships changed
- what temporary aftermath remains

The text should not describe cleanup or internal state removal.

## Event Details

Event Details should explain the premise of a sudden multinational embargo, the role of Embargo Pressure, the target's main response families, and the way higher evolutions pressure neutral traders or spread several embargoes across the world.

The details surface should remain a premise and play overview. It should not list precise penalties, hidden formulas, future surprise events, achievement conditions, or implementation status.

### Evolution previews

Evolution I preview direction:

- neutral states and firms face pressure for helping the target
- intermediary routes become more dangerous
- coalition disputes over enforcement intensify

Evolution II preview direction:

- several targets can be isolated at once
- coalitions overlap
- embargoed countries begin building alternative trade arrangements
- wider world trade becomes fragmented

The Event Details evolution catalog is not a history log. It should not display fake dates or sequence numbers.

## Event log integration

Every firing records one normal Event 50 history entry with the selected primary target as actor.

Evolution II still counts as one event-system firing even when it creates several target ledgers. The history detail can list additional targets through event-specific detail text or related reports.

Each target crisis can record its own resolution outcome for event-specific history detail without advancing the global event timer again.

### Actor handling

The primary target should be the normal event actor. When an evolution milestone belongs to a specific target, save that country as the evolution actor before recording the entry.

When Evolution II unlocks as a global rule without one meaningful actor, use the shared no-actor behavior so an earlier event target cannot leak into the record.

### Evolution logs

Evolution I and Evolution II each record once when their evolved behavior becomes active.

The main Evolutions tab and selected History detail should show:

- Event 50 identity
- evolution name
- tier
- stage where used by the shared system
- date
- actor where meaningful
- enable state

## Decision category presentation

### Header

The header should show:

- current Embargo Pressure
- stage label
- upward, stable, or downward trend
- one short line naming the most urgent exposure
- convenor and leading enforcers in a tooltip

The category must not print a long pipe-separated ledger or raw variable list.

### Static category picture

The category should use one static picture showing a period port, freight yard, or customs point after international shipments have stopped. The strongest visual is a practical absence of trade, such as idle cranes, sealed cargo, inspectors, and waiting railcars.

The picture is presentation only. It should contain no painted buttons, fake meter, labels, map diagram, or readable generated text.

### Action visibility

Three to five primary actions should be visible in one phase. One active mission can appear beside them. Selected-target decisions should show only the currently chosen coalition member or intermediary to the human player.

## Player-facing value treatment

Embargo Pressure should have one consistent colour identity, icon, range, and threshold vocabulary across:

- decision category
- target national spirit or dynamic modifier tooltip
- reports
- Event Details
- event history detail

The player should be able to answer:

- what Pressure represents
- what changed it recently
- what happens at the next stage
- which response can affect it

Dependence remains qualitative. Useful status labels can identify the most exposed area, such as fuel, imported metals, rubber, shipping, or foreign military supply. The implementation should not invent exact trade percentages it cannot support.

## Localisation direction

### Target-country voice

The target reports should focus on commercial disruption, missing cargo, factory substitutions, military stockpiles, cabinet disagreement, and the pressure to choose a national response.

The tone can range from alarm to controlled anger according to Pressure, ideology, and chosen strategy. It should remain concrete.

### Coalition voice

Coalition reports should focus on enforcement, cost, strategic purpose, pressure from allies, and the risk that neutral trade makes the campaign ineffective.

Hardliner wording can be severe. Commercial members should sound concerned with routes, contracts, and domestic shortages.

### Neutral voice

Neutral reports should show profit, risk, inspection, insurance, port capacity, and pressure from larger markets. The country should feel that a real commercial choice exists.

### Defiance voice

Defiance text should let the government turn isolation into mobilization without assuming the public believes every claim. Strong regimes can sound confident. Fragile regimes can rely on rationing, coercion, or emergency appeals.

### Concession voice

Concession text should make the public price clear. It should avoid abstract lines about compromise and name the actual policy, access, guarantee, withdrawal, inspection, or contract being offered.

### Resource-seizure voice

Resource Seizure should use military and economic urgency. It must identify the resource region and strategic need without promising easy victory.

### Humor and irony

The event can use restrained irony around governments calling an embargo universal while cargo keeps moving through neutral ports, or around coalition members condemning trade that they secretly profit from.

Humor should target hypocrisy and administrative evasions. It should not treat civilian shortages or famine as a joke.

### Avoided writing patterns

Final text should avoid:

- generic diplomatic communiques as the main emotional image
- repeated claims that the world will never be the same
- unexplained dramatic filler
- raw effect lists
- hidden formula language
- implementation and rework history
- invented proof of accusations
- unsourced cultural quotations
- repeated contrast formulas built around official denial

## Visual asset package

### Report images

Three event-owned report images are required at `210x176`.

#### Opening isolation

A period documentary scene at a major port or freight terminal. Cargo is halted, cranes or railcars stand idle, customs officers inspect manifests, and crews wait beside sealed shipments. The image should communicate a sudden loss of access.

#### Secondary sanctions

A neutral port, warehouse, insurer, or customs office under intensified inspection. Cargo identities, seals, or certificates are being checked. The scene should emphasize pressure on intermediaries without readable generated documents.

#### Fragmented world trade

A period freight or shipping scene where cargo is being redirected through several systems. Different markings, guarded transfer points, crowded neutral docks, and delayed trains should communicate overlapping embargoes.

Generated documentary-style art is suitable because the event is dynamic and does not depict one fixed historical incident. The art must remain period-authentic to the 1936 to 1945 visual world.

### Decision category picture

One static category picture is required. The asset worker must inspect the canonical decision-category-picture reference family and active consumer before fixing the final dimensions. The existing reference family uses a `114x101` canvas. Treat that size as reference guidance and verify the active consumer.

Visual direction:

- idle port or freight yard
- sealed crates and stopped movement
- strong readable composition at small size
- no text
- no map
- no fake controls

### Category icon

One `32x32` category icon with native transparency. Suggested motif is a cargo crate, globe, or merchant ship enclosed by a broken trade ring or customs seal. It needs a clear silhouette, dark outline, and subtle shadow.

### Response decision icons

Six separate `32x32` decision icons are required:

- Self-Sufficiency: mine, refinery, factory, or domestic resource motif
- Smuggling Networks: concealed cargo route or false crate marking
- Neutral Intermediaries: merchant ship or handshake through a neutral gate
- Diplomatic Concessions: signed compact, key, or opened barrier
- Defy the World: isolated national emblem behind rationing or industrial defenses
- Resource Seizure: resource field or mine under military targeting

Each icon must be designed for the decision surface. It cannot be a resized focus or idea icon.

### Mission icon

One separate `32x32` mission icon for the replacement-supply objective. Suggested motif is a cargo route reaching a factory before a closing barrier.

### National spirit icon

One `64x64` target national-spirit or crisis-state icon. Suggested motif is an isolated industrial nation surrounded by closed shipping lanes and stamped cargo. It should communicate broad economic isolation, including land, maritime, commercial, and diplomatic pressure.

### Achievement icons

Each accepted achievement requires a `64x64` completed icon and the normal grey and not-eligible variants. The completed source art must be designed for the achievement surface.

### Source and processing mode

- report images and category picture use generated period documentary art with full-canvas treatment
- icons use generated native-transparent art
- all generated assets preserve source PNGs, prompt records, processed previews, final DDS files, manifests, and contact sheets during active implementation
- final assets move to event-scoped runtime folders
- durable provenance and wiring facts move into permanent event documentation before temporary asset workspaces are removed

## Sound direction

Event 50 should use normal report-event sound treatment or an existing fitting interface cue. It does not need a separate musical presentation layer.

The sound should support halted commerce, inspection, or cabinet urgency through a suitable normal report cue.

## Documentation and catalog wording

The event document should explain:

- target selection
- Pressure stages
- dependence scaling
- response families
- coalition roles
- evolutions
- AI
- outcomes
- interactions
- assets
- validation state

The authoritative event catalog workbook should be updated only after final in-game wording exists. Event Details and workbook details must match the same player-facing premise.
