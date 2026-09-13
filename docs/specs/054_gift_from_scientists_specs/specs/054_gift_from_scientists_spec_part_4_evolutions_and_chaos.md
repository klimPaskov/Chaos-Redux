# Event 54: Evolutions and Chaos Feedback

## Evolution model

Event 54 uses pre-fire evolved openings. The event has no persistent active crisis to upgrade between firings.

Every firing checks the current Chaos value and the enabled state of all three evolutions. It uses the highest eligible enabled stage. A disabled higher stage falls back to the next eligible enabled stage, then to the baseline.

The event does not require a previous lower stage to have fired. A campaign that first receives Event 54 at 600 Chaos can begin with Scientific Deluge when that evolution is enabled.

Each evolution changes the current firing only. Technologies granted during an earlier stage remain part of the country's normal researched state.

## Baseline: One Breakthrough

Every valid country receives one eligible ordinary technology.

The baseline uses the ordinary pool. Registered Chaos technologies are unavailable.

The baseline should feel uneven across countries. Some gains will be decisive and others will have little immediate value.

## Evolution I: Multiple Breakthroughs

- Chaos requirement: 200+
- Grant target: three technologies per valid country
- Eligible source: ordinary technology pool

Every country receives up to three distinct eligible ordinary technologies.

Selection remains independent and without replacement. The second and third draws recheck branch compatibility after every grant.

This stage represents a broad research surge. It does not expose event-owned technologies and does not grant research speed or slots.

### Entry and history

The first firing that actually uses this stage may record Evolution I in the evolution history.

Crossing 200 Chaos alone does not record the evolution. A disabled Evolution I does not set its used flag.

## Evolution II: Accelerated Discovery

- Chaos requirement: 400+
- Grant target: five technologies per valid country
- Eligible source: ordinary pool plus explicitly registered Chaos technologies

Every country receives up to five distinct technologies.

This is the first stage that can select individual custom technologies published through the eligibility registry. A registered technology competes with ordinary candidates under the same random selection rule.

The owner event does not count as fired. The owner route remains available. Only the selected technology and its approved grant profile are applied.

### Entry and history

The first firing that actually uses this stage may record Evolution II in the evolution history.

If the campaign reaches this stage before Event 54 has ever fired, the first Event 54 firing starts with five grants and the expanded pool.

## Evolution III: Scientific Deluge

- Chaos requirement: 600+
- Grant target: ten technologies per valid country
- Eligible source: ordinary pool plus explicitly registered Chaos technologies

Every country receives up to ten distinct technologies.

Scientific Deluge can produce large jumps in military, industrial, engineering, and experimental capability. It still respects recipient safety, branch exclusivity, owner boundaries, and pool exhaustion.

The event should not soften the result through category balancing. A country may receive several technologies from one field when the independent random sequence produces them.

### Entry and history

The first firing that actually uses this stage may record Evolution III in the evolution history.

A first firing at 600 or more Chaos does not need to create artificial history entries for Evolutions I and II. The history should record the evolved opening that actually occurred.

## Evolution disable behavior

Evolution toggles are independent.

Examples:

- At 650 Chaos with Evolution III disabled and Evolution II enabled, the event grants five technologies from the expanded pool.
- At 650 Chaos with Evolutions II and III disabled and Evolution I enabled, the event grants three ordinary technologies.
- At 650 Chaos with all evolutions disabled, the event grants one ordinary technology.
- At 450 Chaos with Evolution II enabled and Evolution I disabled, the event grants five technologies from the expanded pool.

A disabled evolution cannot record history, unlock the expanded pool, set a used milestone, or contribute its Chaos milestone.

## Chaos impact map

The event is beneficial in immediate terms, but the simultaneous worldwide origin is abnormal. Chaos comes from the scale and impossibility of the research wave, not from ordinary research success.

| Milestone or outcome | Why global Chaos changes | Direction | Starting magnitude | Dynamic factors | Repeat guard | Shared-source overlap | Reversal counterpart |
| --- | --- | --- | --- | --- | --- | --- | --- |
| First completed Event 54 world transaction | Unrelated countries receive verified breakthroughs in the same short period with no shared source | Increase | +2 | Requires at least half of valid recipients to receive one technology | Once per campaign | Does not count later wars, weapons use, deaths, contamination, or tension | None, because the knowledge remains |
| First completed Multiple Breakthroughs wave | A majority of research-capable countries receive three discoveries in one incident | Increase | +1 | Requires at least half of valid recipients to receive the full three grants | Once per campaign | Does not duplicate generic military or industrial growth sources | None |
| First registered technology granted outside its owner route | A technology reserved by another Chaos system appears without that event delivering it | Increase | +1 | Requires a successful registered grant and an unchanged owner-event lifecycle | Once per campaign | The later use of the technology follows the owner's normal Chaos rules | None |
| First completed Scientific Deluge | A majority of valid countries receive ten discoveries during one firing | Increase | +2 | Requires at least half of valid recipients to receive all ten grants | Once per campaign | Does not duplicate consequences caused later by these technologies | None |

These are initial balance values. They should live in event-owned tuning constants and be reviewed with the wider Chaos pacing model.

## Chaos guard rules

Event 54 does not add Chaos merely because the random picker selected it.

A milestone applies only after the relevant grants have completed. A transaction in which too few countries receive technology does not qualify.

Later repeats of the same milestone add no direct Chaos. This prevents a repeatable beneficial event from becoming a reliable path to World Collapse.

Evolution eligibility, evolution logging, registry expansion, and stage selection add zero Chaos by themselves.

## Shared-source separation

Technologies granted by Event 54 may later enable actions that already generate Chaos through other systems.

Examples include war, annexation, nuclear use, chemical or biological use, deaths, contamination, world tension, and event-owned weapon milestones. Those consequences keep their existing sources.

Event 54 does not pre-charge Chaos for possible future use and does not duplicate the later source.

A registered technology's owner can add a concrete Chaos source when the recipient first uses the capability. The grant callback itself should remain neutral unless the owner has documented that possession alone changes the world.

## Irreversibility

There is no generic containment route for Event 54. The technology has already spread into state institutions and cannot be removed cleanly without damaging unrelated research state.

Research Failure may reduce research capacity after a gift, but it does not erase the technologies already received and therefore does not reverse Event 54's anomaly milestones.

This lack of reversal is acceptable because the event's direct Chaos contribution is small, one-time, and capped across the whole campaign.

## Evolution presentation direction

Evolution text should describe changes in the observed scale of discovery.

Multiple Breakthroughs should focus on several independent breakthroughs appearing inside each country.

Accelerated Discovery should introduce the first reports of technologies that seem to belong to secret projects or unfamiliar institutions.

Scientific Deluge should show research systems losing any normal sense of sequence as whole fields leap forward together.

The text should not mention candidate pools, registry entries, callbacks, safety profiles, stage constants, or exact code thresholds outside the normal evolution requirement display.
