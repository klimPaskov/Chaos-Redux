# Manual Improvement Loop Closure Review

## Disclosure

The `chaosx_improvement_loop_planner` contract was read in full. This environment did not expose a custom subagent spawning tool, so this is a manual parent-agent review using the same planning and anti-bloat standard. It is not represented as a spawned subagent output.

## Feature promise reviewed

Event 20 promises:

- a severe state-based disease rather than a temporary continent modifier
- escalating real population loss
- meaningful containment, treatment, sanitation, and rat-control choices
- Black Plague-specific actions inside the shared disease category
- black rendering for established Black Plague states in the existing disease mapmode
- shared disease and biowarfare integration
- long weaponization research
- five evolutions
- Rat Nations with growing nonhuman armies
- a separate sentient Rat King country
- an instant-chaos triggerable scenario
- an earned focus-driven terminal world takeover

## Gaps found and resolved

### Rat supply and counterplay

The design now includes plague-state sustenance, burrow nodes, clean-territory strain, armor and air counterplay, engineer clearance, and royal node objectives.

### Black Plague-specific crisis actions

A shared category alone was too generic. The final spec adds selected-state Black Plague actions for clearing city rats, sealing food stores, clearing sewers and burrows, controlling fleas and bedding, purging rail yards and docks, and demolishing irrecoverable blocks. These remain separate decisions inside the general disease category.

### Mapmode identity

A normal disease colour would make the event visually indistinct. The final resolver gives every established Black Plague state a black base colour. Borders, patterns, icons, and tooltips carry phase and containment information. Other diseases retain their existing colours.

### Triggerable instant-chaos setup

The original closure pass rejected a manual scenario because it was not in the first request. The user later explicitly required one. Part 9 now defines a data-driven scenario with four intensities, multi-continent disease seeding, forced Evolutions I through IV, multiple independent Rat Nations, a separate Rat King Royal Basin, a coexistence grace period, idempotent setup, achievement disqualification, and a full mapmode refresh. It never grants Evolution V or terminal victory.

### Liberated states

Liberated rat territory remains plagued. Human owners must quarantine, clear burrows, reduce infestation, and complete ordinary disease cleanup.

### Human last-response play

The world-end approach includes human capital, port, cure-sharing, relief-corridor, royal-node, and crown-strike objectives that can interrupt Rat King readiness.

### Rat political depth

The Rat King receives three government routes, visible mechanics, human population policy, captured knowledge, administration, internal crises, and route-specific AI.

### World-end certainty

After the difficult terminal conditions are met, a deterministic takeover resolves surviving resistance and prevents an indefinite half-ended campaign.

### Performance and tag limits

The final design uses a finite tag pool, basin cooldowns, pulse caps, active registries, intensity caps, consolidation rules, and map-size-aware thresholds.

### Super-event distinction

Coronation and world end have separate campaign roles and require unique image, quote, and audio research. Scenario coronation wording must work while independent broods still exist.

## Anti-bloat findings

The following additions remain rejected because they duplicate or weaken the event:

- a dedicated Black Plague decision category
- a second disease mapmode
- a duplicate contamination or death meter
- a Black Plague-only doomsday button outside the shared biowarfare structure
- one bespoke focus tree for every base Rat Nation tag
- ordinary diplomatic routes between Rat Nations and human countries
- a super-event for every brood emergence
- a new ideology family without live-repository need
- dozens of permanent national spirits
- conventional rat manpower, factories, equipment, navy, or air production
- automatic Evolution V or world-end completion from the triggerable scenario

## Closure recommendation

Broad expansion should stop at this revised specification. The event has a complete disease loop, specific sanitation decisions, a distinct black mapmode identity, medical and military tradeoffs, dynamic AI, country packages, focus architectures, an instant-chaos scenario, an earned world-end route, assets, achievements, and implementation acceptance criteria.

Remaining work is implementation, live-source verification, asset and audio production, final localisation, scenario registration, performance testing, workbook alignment, and completion audits. Another broad planning pass would add duplication unless implementation uncovers a concrete engine or compatibility gap.
