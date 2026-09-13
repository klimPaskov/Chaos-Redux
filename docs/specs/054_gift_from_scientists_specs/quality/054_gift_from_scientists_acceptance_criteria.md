# Event 54 Acceptance Criteria

## Event identity

- Event ID `54` remains Gift from Scientists.
- The canonical entry remains `chaosx.nr54.1`.
- The event is Minor Repeatable with Chaos level 1.
- The event is registered and enabled only after the rework is complete.
- The event belongs to Scientific Research at Medium severity.

## Baseline result

- One bounded global transaction runs per firing.
- Every valid research-capable country is considered once.
- Every included country draws independently from its own safe missing pool.
- Baseline grants one ordinary technology.
- Strategy, country size, ideology, player status, and research slots do not weight the draw.
- Ahead-of-time technology is allowed when direct grant is safe.
- The event grants no research slots, research speed, equipment, factories, or doctrine.

## Evolution results

- Evolution I activates at 200+ when enabled and targets three ordinary technologies.
- Evolution II activates at 400+ when enabled and targets five technologies from the ordinary and registered pools.
- Evolution III activates at 600+ when enabled and targets ten technologies from the ordinary and registered pools.
- The highest eligible enabled stage is used.
- Disabled stages set no history, used flag, expanded-pool state, or Chaos milestone.
- A campaign can begin Event 54 at a higher evolved opening without prior lower-stage history.

## Technology integrity

- Already researched technologies never enter a recipient pool.
- One country receives no duplicate technology in one firing.
- Package-granted technologies also leave the pool.
- Every draw after the first rechecks branch compatibility.
- Opposing industry and production branches cannot both be granted.
- Every other exclusive family is inventoried and protected.
- Doctrines remain excluded.
- Special projects and hidden setup technologies remain excluded.
- No-DLC graphs work without substitution.
- Pool exhaustion ends safely and never selects an excluded fallback.

## Registered technology integrity

- Custom technologies are excluded before Evolution II.
- Every registered candidate has a stable owner and safety profile.
- A registered grant does not mark its owner event fired.
- A registered grant does not complete its owner project or route.
- A registered grant does not consume a normal unique reward.
- A registered grant does not create the owner character, institution, country, facility, or faction.
- Owner callbacks are narrow, idempotent, recipient-only, and fail closed.
- A later normal owner event can still fire and has duplicate-reward handling.
- Malformed providers affect only their candidates and do not stop the world transaction.

## Recipient integrity

- Human and AI countries use the same rules.
- Majors, minors, subjects, exiles, and capitulated research states are handled correctly.
- Research-capable special and nonhuman countries are not excluded by a blanket classifier.
- Reserved, observer, dummy, invalid, and protected-transaction countries are excluded.
- Recipient list is fixed at transaction start.
- Countries created during the transaction wait until a later repeat.

## Reports and logs

- Normal grant popups are suppressed.
- Every affected human country receives one consolidated report.
- AI countries receive no report spam.
- Reports show intended and actual grant counts.
- Reports provide every granted technology's real localized name.
- Partial and zero-grant reports explain safe pool exhaustion.
- Registered grants are identifiable without exposing owner internals.
- Each firing creates one Event History row.
- Human report events create no pacing or duplicate history.
- Evolution history records only stages actually used.
- Event Details stays premise-focused and hides registry internals.

## Chaos feedback

- The first completed world transaction can add +2 Chaos only once.
- The first qualifying Multiple Breakthroughs wave can add +1 only once.
- The first external registered grant can add +1 only once.
- The first qualifying Scientific Deluge can add +2 only once.
- Every milestone applies only after its concrete grant threshold is met.
- Evolution eligibility and logging add zero Chaos.
- Later technology use relies on existing owner or shared Chaos sources.
- Wars, deaths, contamination, nuclear use, and world tension are not double counted.

## Multiplayer and persistence

- Results are synchronized across clients.
- All random results are committed before human reports open.
- Report acknowledgement cannot reroll or regrant.
- Save and reload preserves results and prevents duplicate grants.
- Tag switching cannot create a second receipt.
- A transaction or report sequence is consumed once.
- One global firing produces one pacing transaction.

## Scientific Research cluster

- The stable Scientific Research cluster ID is confirmed before implementation.
- The cluster is Minor Repeatable and unlocks at 200+.
- Members are 16, 24, 27, 54, and 60.
- Severities are Severe, High, Medium, Medium, and High.
- Event 27 also retains Military Preparation membership at Medium severity.
- Many-to-many membership survives catalog, runtime, logs, details, and settings.
- The selected anchor fires when valid.
- Optional members show accurate fired or skipped reasons.
- The cluster remains available after fire-once members have fired.
- The cluster counts as one pacing event.
- Gift from Scientists and Research Failure can coexist without overwriting each other.

## Assets and achievements

- One final 210x176 report-event image is generated and processed through the standard report-card workflow.
- The report image has period-appropriate content, black-and-white sepia treatment, transparent corners, and no readable generated text.
- Achievement `chaosx_achievement_054_complete_the_chain` has full tracking, disqualifiers, localization, and icon states.
- Achievement `chaosx_achievement_054_borrowed_future` remains blocked until at least two owner providers can satisfy its full use contract.
- Every implemented achievement has its 64x64 state package and correct root filenames.
- No placeholder image or icon is accepted as final.

## Required evidence before completion

- Full source review and one vanilla precedent for direct technology grants.
- `hoi4.event_inspect`, event render, and post-change comparison for the Event 54 chain.
- `hoi4.tech_inspect`, technology render, and technology compare for candidate and registry behavior.
- `hoi4.probability_inspect` plus the named scenario matrix.
- Probability evaluation, sweeps, and before-and-after comparison where required.
- Event log and cluster details evidence.
- Save and reload evidence when the user performs live validation.
- Localization audit.
- Asset handoffs and final wiring evidence.
- Catalog workbook update followed by CSV export.
- Improvement-loop closure handoff.
- Final event completion audit.

## Completion blockers

Any of these conditions blocks completion:

- a candidate can break an exclusive branch
- custom technology grants alter owner lifecycle
- doctrines enter the pool
- a country can receive duplicate grants
- a failed candidate consumes a slot or loops forever
- normal technology popups create report spam
- human reports omit exact results
- save and reload can reroll or duplicate grants
- the cluster loses Event 27's second membership
- direct Chaos can be farmed by repeat firings
- required assets or achievements use placeholders
- the workbook and export remain stale
- required MCP evidence is unavailable and the affected result is still claimed as proven
- an accepted spec rule is simplified without explicit disclosure
