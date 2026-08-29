# Great Depression 2.0 specification, part 10: Presentation, assets, and writing direction

## Presentation hierarchy

The event should be readable from the normal decision interface.

Primary presentation:

1. Opening report event.
2. One Great Depression 2.0 decision category.
3. Depression Severity display.
4. Trend and next threshold.
5. One selected Depression Center at a time.
6. One main objective and up to two supporting missions.
7. State modifiers and map highlighting for registered centers.
8. Event Details and evolution history.

Evolution III adds one global super-event and one qualitative world-stage line. It does not require a separate permanent scripted GUI.

## Category layout

The category header should answer five questions quickly:

- How severe is the crisis?
- Is it improving or worsening?
- What threshold matters next?
- Which recovery doctrine is active?
- What can the player do now?

Recommended order:

```text
Category picture
Depression Severity meter or compact progress display
Severity band and trend
Current phase and recovery doctrine
Next threshold
Top material causes
Selected Depression Center and local condition
Active objective
Current primary decisions
```

Do not place a paragraph above the actions. Use a concise summary and tooltips.

## Severity display

The display needs:

- Value from `0` to `100`.
- Named band.
- Qualitative trend.
- Threshold marker.
- Distinct Economic Paralysis state.
- Label and icon support in addition to color.

Suggested color direction:

- Recovery and stabilization use restrained green or blue.
- Fragile Economy uses yellow.
- Depression and Deep Depression use orange.
- Systemic Breakdown and Economic Paralysis use red and dark red.

The exact colors should follow existing Chaos Redux and vanilla UI contrast. Color must not carry the meaning alone.

## Category picture

Use one static decision category picture as the baseline. It should establish the event's identity without drawing fake controls.

Visual direction:

- Period industrial district during a shutdown.
- Idle factory gate, dark windows, quiet rail sidings, and a line of unemployed workers or families.
- Country-neutral 1936 to 1945 setting.
- Documentary or period press photography treatment.
- Strong readable industrial subject at the category picture's actual size.
- No readable generated text.
- No stock-market graph, modern skyline, computer display, or modern clothing.
- No map as the main subject.

The asset worker must inspect the active category-picture consumer and the canonical reference family before fixing size. The current reference family uses `114x101`, but that is not a universal assumption.

A phase-variant or animated category picture is not required. The Severity display already communicates changing state. Additional motion would add production cost without improving the main decision.

## Opening report image

The current repository uses `GFX_report_event_great_depression`. Treat that sprite as a stable migration anchor until inspection proves a reason to rename it.

Source mode direction:

- Generated period documentary scene is preferred because Event 35 can affect any country and needs a country-neutral composition.
- Sourced archival photography is acceptable when rights, date, and geographic implication fit the final event.
- Do not reuse a modern recession photograph.

Composition direction:

- Foreground workers, closed plant, empty construction site, or idle freight yard.
- Visible human and industrial consequences.
- Strong horizontal event-picture crop.
- Serious treatment without theatrical destruction.

The opening image should communicate halted work. It should not show the final political or global evolutions.

## News image

The ordinary news event may reuse the opening report family when the existing news surface and crop support it. A separate news image is justified if the news event uses a different canvas or if the opening art is too local to read as an international report.

News direction:

- Broad industrial slowdown.
- Closed exchanges, idle docks, or silent factories.
- No national flag that would make the image wrong for other target countries.
- No readable newspaper headline generated inside the art.

## Evolution I visual direction

Financial Contagion needs a report image or event-art variant only for its first major activation and important international incidents.

Subject direction:

- Crowded banking hall, closed bank doors, queues, brokers or clerks handling failed payment notices, or freight documents that no longer clear.
- Several countries implied through travelers, shipping, or correspondence without using a map as the main composition.
- Period clothing and architecture.
- Anxiety shown through action and queues, not abstract red arrows.

## Evolution II visual direction

Social Collapse needs one report image family for national unrest.

Subject direction:

- Factory occupation, organized strike line, relief march, or guarded industrial gate.
- Show the political and labor conflict created by prolonged unemployment.
- Keep violence restrained unless the exact incident is violent.
- Avoid cheap comedy or spectacle.
- Avoid using a specific real political symbol unless the country and movement justify it.

Country-specific political events may reuse existing valid leader or party assets. New grounded portraits are not inferred by this spec.

## Evolution III super-event image

The worldwide escalation needs one unique super-event image.

Source mode:

- Generated period documentary or symbolic scene.

Subject direction:

- A major international port, freight exchange, or industrial city brought to a halt.
- Idle cranes, silent locomotives, dark factory districts, and crowds seeking work.
- Several regions of the world implied through shipping, uniforms, cargo, or architecture while keeping one coherent scene.
- Global scale communicated through the collapse of exchange and movement.
- No map collage.
- No readable text.
- No modern financial screens.
- No apocalyptic ruins because the event is an economic world crisis, not physical annihilation.

The image should support the global-contraction super-event role through grounded economic shutdown and human hardship, without apocalyptic framing.

## Icon inventory

Every generated alpha-backed icon requests native transparency and preserves it through DDS conversion.

### Category and doctrine icons

| Working asset | Type | Visual direction | Proposed runtime folder |
| --- | --- | --- | --- |
| Great Depression category | Decision category icon | Dark factory gate, idle gear, or closed plant symbol | `gfx/interface/decisions/035_great_depression/` |
| Emergency Public Works | Decision icon | Worker, shovel, rail, and public structure in one simple silhouette | Same event folder |
| Rescue Strategic Industry | Decision icon | Protected factory or shielded gear | Same event folder |
| Stabilize Finance and Trade | Decision icon | Bank ledger, secure coin, ship, or linked trade document | Same event folder |
| Austerity and Retrenchment | Decision icon | Cut ledger, tied budget, or narrowed scale | Same event folder |
| Direct State Planning | Decision icon | Planning board, factory grid, or state allocation emblem | Same event folder |
| Let the Market Clear | Decision icon | Auction hammer, reopened shopfront, or broken chain with surviving gear | Same event folder |
| Cabinet Review | Decision icon | Cabinet table, policy folder, or rotating doctrine symbol | Same event folder |

The icons should be distinct at `32x32`. They should not be resized focus icons or one shared icon with recolors.

### Mission icons

| Working asset | Type | Visual direction |
| --- | --- | --- |
| Halt the Panic | Mission icon | Closed bank and stabilizing barrier |
| Keep Essential Freight Moving | Mission icon | Locomotive, rail switch, or freight crate |
| Reopen Depression Center | Mission icon | Factory lights returning or gate reopening |
| Prevent a Relapse | Mission icon | Fragile upward line supported by brace, without modern chart styling |
| Maximum-Severity Emergency | Mission icon | Dark factory and emergency beacon |
| Contain Financial Contagion | Mission icon | Linked institutions separated by a firebreak |
| Prevent a General Strike | Mission icon | Factory gate and negotiation table |
| International Reconstruction | Mission icon | Crane, rail, ship, and cooperative emblem |

Mission icons need the exact mission reference family. They are not decision icons with different filenames.

### Idea and national-condition icons

| Working asset | Surface | Direction |
| --- | --- | --- |
| Opening Economic Shock | Timed idea | Sudden factory shutdown and falling order book |
| Active Great Depression | Dynamic national condition | Idle factory and unemployment queue |
| Economic Contagion | Secondary-country condition | Linked banks or markets under strain |
| Global Contraction | Evolution III condition | World shipping and factory exchange halted |
| Post-Depression Recovery | Timed recovery safeguard | Reopened gate, workers returning, and repaired rail |
| Recovery doctrine legacies | Route-specific idea family | One unique symbol for each durable institution |
| Recovery scars | Country or state idea family | Broken rail, hollow plant, debt ledger, or emergency control symbol |

Prefer one staged active-depression icon family. Avoid many near-identical national spirits.

### State modifier icons

| Working state | Direction |
| --- | --- |
| Distressed Center | Factory with partial shutdown |
| Idled Center | Dark gear or stopped conveyor |
| Shuttered Center | Closed gate and chain |
| Abandoned Works | Unfinished structure and idle crane |
| Protected Center | Factory under shield |
| Public Works Active | Worker and rail or road |
| Reopened Center | Lit factory and open gate |
| Hollowed Industrial District | Empty factory shell |

State icons must remain readable in the state-view consumer. They should use the state-modifier reference family, not decision art.

### Evolution icons

Each evolution needs one Event Details and history icon if the shared interface supports event-specific evolution art.

- Financial Contagion: linked banks or contracts transmitting failure.
- Social Collapse: occupied factory or broken civic order.
- The Second Great Depression: halted global shipping and industry.

## Achievement icons

Every accepted achievement needs a complete root-level achievement triplet:

- Eligible color asset.
- Grey locked asset.
- Not-eligible asset using the verified overlay workflow.

Filenames must match final achievement IDs. Achievement assets stay directly under `gfx/achievements/` unless current engine inspection proves another requirement.

## Asset production routing

Use:

- `chaosx_generated_event_art` for generated report, news, category-picture, and super-event scenes.
- `chaosx_asset_source_researcher` when the final choice requires real archival Great Depression material.
- `chaosx_icon_artist` for decisions, missions, ideas, state modifiers, evolution icons, and achievements.
- `chaosx_super_event_audio_researcher` for the Evolution III musical cue.
- `chaosx_super_event_text_researcher` for quote and cultural-reaction research.

There are no character portraits, flags, faction emblems, 3D models, unit counters, or skeletal animations required by the baseline specification.

Social Collapse can create a leader or country identity only when a valid existing political route supports it. Any resulting portrait, flag, country, or unit asset becomes a separate accepted requirement and follows the full source, tag, portrait, flag, country, and force-package workflow.

## Temporary asset workspace

During implementation, use:

```text
docs/assets/035_great_depression/
```

for sources, prompts, previews, provenance, contact sheets, and handoffs.

Final runtime assets belong in engine-facing event folders. Before completion, promote durable evidence into permanent Event 35 documentation, verify that no runtime reference points into `docs/assets/`, and delete the temporary event workspace.

## Asset QA

For every asset:

- Inspect the exact vanilla or Chaos Redux reference family.
- Confirm canvas and consumer.
- Preserve native transparency for alpha-backed icons.
- Verify no white halo, fake checkerboard, opaque square, or clipped silhouette.
- Review at native size and enlarged nearest-neighbor size.
- Confirm sprite name and path before final wiring.
- Create contact sheets for each asset family.
- Record source mode, prompt or source, rights, dimensions, checksums, and final status.

Generated event scenes must be checked for modern props, readable false text, wrong era clothing, and country-specific symbols that break reuse.

## Player-facing writing standard

The planning package defines direction. It does not provide pasteable localisation.

All final text must:

- Use concrete in-world observations.
- Describe idle plants, failed orders, lost work, freight disruption, bank queues, and policy action.
- Explain visible costs and requirements clearly.
- Name dynamic countries and states where relevant.
- Keep hidden formulas, incident pools, and future evolutions secret.
- Avoid process history and rework language.
- Avoid em dashes and semicolons.
- Avoid staccato sentence chains.
- Avoid contrast formulas and generic dramatic templates.
- Avoid cheap humor around mass unemployment, hunger, repression, or civil conflict.

## Opening event text direction

### Viewpoint

National government receiving evidence from factories, banks, local administrations, and transport authorities.

### Driving force

Orders are cancelled, credit stops circulating, construction closes, and unemployment spreads through the industrial regions.

### Information shown

- The country has entered a severe economic contraction.
- Production and construction will fall sharply.
- A decision category has opened.
- The first Depression Centers are visible.
- The government must choose a recovery direction.

### Information withheld

- Exact hidden component formula.
- Future evolution branches.
- Exact incident probabilities.
- Achievement conditions.
- Whether a civil war or worldwide depression will occur.

### Tone

Serious, specific, and administrative without becoming paperwork-centered. The human effect should be visible through lost work and halted industry.

### Option direction

The opening option acknowledges the need for immediate economic action. It can use restrained official confidence or grim administrative understatement. It should not joke about unemployment or use a generic statement that the world will never be the same.

## Independent news text direction

### Viewpoint

Foreign press and governments observing the target country's industrial contraction.

### Information shown

- Major plants and construction are slowing.
- Unemployment and financial stress are spreading inside the named country.
- Foreign partners are reconsidering exposure.

### Information withheld

- Hidden Severity.
- Future contagion target.
- Event 34 inheritance details unless the source was publicly known.

### Tone

Period news report with concrete economic observations. Avoid broad claims that every market is already collapsing.

## Event 34 collapse text direction

### Viewpoint

The boom country witnesses the reversal of its own expansion.

### Driving force

Orders, credit, transport, and investment built for extraordinary growth fail together. Protected and unfinished Industrial Regions should be named where possible.

### Information shown

- The boom has ended.
- Event 35 has begun or deepened.
- The starting crisis reflects the failed boom.
- The player must manage inherited centers.

### Information withheld

- Raw Overheating formula.
- Snapshot fields.
- Direct code mapping.

### Tone

Abrupt reversal and material failure. Avoid moralizing that the boom was always doomed.

## Severity and category text direction

The category summary should use one or two short paragraphs at most.

It should dynamically mention:

- Current band.
- Trend.
- Main cause.
- Next threshold.
- Selected center.
- Active doctrine.

Tooltips explain:

- What changes Severity.
- What the next threshold does.
- Why the current action is blocked.
- Which cost is committed.
- What happens on success or failure.

Do not expose a long hidden contributor ledger.

## Doctrine text direction

### Emergency Public Works

Speaker and stance:

- Government presenting employment and construction as a national recovery program.

Tone:

- Practical, mobilizing, and public-facing.

Visible promise:

- Jobs, transport, and state reconstruction at a large immediate cost.

Avoid:

- Claiming projects are free.
- Generic praise of infrastructure.

### Rescue Strategic Industry

Speaker and stance:

- War ministry, industrial board, or cabinet choosing which plants must survive.

Tone:

- Hard prioritization and strategic necessity.

Visible promise:

- Preserve essential production while other sectors bear more pressure.

Avoid:

- Treating all factories as equally strategic.

### Stabilize Finance and Trade

Speaker and stance:

- Treasury, central bank equivalent, commercial ministry, and foreign partners.

Tone:

- Controlled confidence and concrete institutional action.

Visible promise:

- Reopen viable finance and preserve essential exchange.

Avoid:

- Modern central-bank jargon.
- Claiming exact exchange rates that the game does not model.

### Austerity and Retrenchment

Speaker and stance:

- Treasury or cabinet arguing that the state cannot sustain every commitment.

Tone:

- Severe, sober, and politically contested.

Visible promise:

- Lower fiscal pressure with an explicit unemployment and stability risk.

Avoid:

- Presenting austerity as automatically wise or evil.

### Direct State Planning

Speaker and stance:

- Emergency planning authority coordinating production, transport, and distribution.

Tone:

- Directive and organized.

Visible promise:

- Lower volatility and protect essential sectors at political and flexibility cost.

Avoid:

- Generic ideological slogans unless the country route supports them.

### Let the Market Clear

Speaker and stance:

- Government or commercial coalition accepting closure and repricing.

Tone:

- Cold confidence, resignation, or commercial pragmatism according to country.

Visible promise:

- Lower state commitment and a possible later recovery with high short-term risk.

Avoid:

- Hidden promise that the route will succeed.

## Depression Center text direction

State text should name:

- The state.
- Its current local condition.
- The industry, transport, port, or project that makes it important.
- Current treatment.
- What will happen if the mission succeeds or fails.

Avoid a generic sentence used for every state.

## Financial Contagion text direction

### Origin report

Show:

- Foreign credit and contracts are reacting to the national crisis.
- Specific partners are exposed when valid.
- New international actions are available.

Keep uncertain:

- Which country will enter a full depression.
- Exact conversion chance.

Tone:

- International economic fear shown through banks, shipping, and contracts.

### Exposed-country report

Show:

- The named origin and relationship.
- Local banking, trade, or contract pressure.
- Ring-fence, aid, diversification, or abandonment choices.

Do not say the country has Event 35 until conversion actually occurs.

## Social Collapse text direction

### Viewpoint

Workers, local authorities, movements, employers, government, and security institutions according to incident.

### Information shown

- Exact strike, occupation, riot, or government crisis.
- Named state or sector.
- Visible movement and demand.
- Available response and cost.

### Information withheld

- Hidden Social Strain.
- Future coup or civil-war roll.
- Secret support values.

### Tone

Serious and political. Official euphemism, propaganda, or bitter understatement can be used when it exposes the speaker's position. Cheap jokes are forbidden.

## Evolution III super-event text direction

### Role

First concrete worldwide economic contraction.

### Title direction

Short and specific to a second global depression. Research period economic, literary, or political references before final choice. Do not use generic titles about darkness, flames, or the end.

### Description direction

Show the simultaneous slowing of factories, ports, trade credit, and construction across several countries. State that the crisis is worldwide. Do not list modifiers or claim that every country is equally affected.

### Reaction direction

Brief, grim, and suitable for a global economic crisis. A sourced cultural allusion may be used only after verification. Do not use an unsourced quotation or lyric.

### Quote direction

Research public-domain or otherwise suitable historical, economic, political, literary, or religious text about unemployment, credit, hunger, work, or international collapse. Verify exact wording and attribution. The planning package selects no final quote.

### Audio direction

Use an intentional musical recording with a restrained, period-suitable, mournful or processional character. Research composition and recording rights separately. Do not use drones, test tones, abstract noise, or another super-event's track.

## Recovery text direction

Recovery reports should distinguish:

- Strong recovery.
- Uneven recovery.
- Hollow recovery.
- End of worldwide depression.

They should name what reopened, what institution remains, and what cost persists. Avoid a generic celebration that ignores scars.

## Event Details direction

The Event Details premise should explain:

- A major or player country can enter a long depression.
- One Severity value is managed.
- The event can start independently or from Event 34 collapse.
- Recovery doctrine and Depression Centers shape the result.

Evolution details explain the visible premise of each stage without listing raw effects or hidden conditions.

The cluster detail identifies Event 35 as a Low member of Negative Economy after the authoritative cluster registry is completed.

## Spreadsheet direction

After implementation, the workbook row should use final in-game wording for:

- Event Details.
- Evolution I details.
- Evolution II details.
- Evolution III details.
- Cluster name and Low danger.
- Cross-event Event 34 relation.
- Super-event presence for Evolution III.

The workbook is authoritative. Regenerate all three CSV exports through the repository exporter.
