# Event 008 localisation audit, 2026-10-05

Disposition: implemented text patch, pending parent review and MCP visual validation.
Acceptance basis: bounded parent assignment for plain report text, concrete prose and mechanics-aligned tooltips.

## Changed files

- `localisation/english/008_world_tension_rises_l_english.yml`
- `common/scripted_localisation/008_tensions_rising_scripted_localisation.txt`

## Key-level changes

### `chaosx.nr8.baseline.d`

Before: A chain of public accusations, military communiques, and unattributed leaks has unsettled diplomatic circles. Border offices, newspapers, and staff rooms now behave as if a crisis is already near.

After: Public accusations and leaked military cables have strained relations between capitals. Newspapers carry rumours of war, and border commanders put their patrols on alert.

### `chaosx.nr8.stage_1.d`

Before: The cables are moving faster than the diplomats. Every denial is copied, every correction is reprinted, and every quiet military note seems to reach a foreign desk before dawn.

After: Embassy telegraph rooms work through the night. Leaked military cables fill the morning papers, spreading rumours of mobilisation across the border.

### `chaosx.nr8.stage_2.d`

Before: Rumour has become a commodity. Newspapers sell it, ministries launder it, border officers fear it, and foreign rivals repeat it with just enough distance to deny authorship.

After: Newspapers sell rumours of mobilisation, and rival governments use them to accuse their neighbours. Border officers tighten patrols as each accusation spreads.

### `chaosx.nr8.stage_3.d`

Before: Staff offices remain lit long after the public briefings end. Maps are checked, train schedules copied, and commanders prepare for a crisis that official orders refuse to name.

After: Commanders keep their staffs at work through the night, checking railway timetables and preparing troops for mobilisation. Exhausted officers face another day of rumours along the frontier.

### `chaosx.nr8.stage_4.d`

Before: The latest round of warnings has become routine across foreign offices. Capitals compare statements, watch railway notices, and prepare contingency files as the situation slips beyond easy control.

After: Troops remain on alert along the frontier. Commanders delay leave, patrols challenge unfamiliar movements, and fresh accusations deepen distrust between neighbouring capitals.

### `chaosx.nr8.stage_4.a`

Before: Log the latest alerts.

After: Keep the patrols on alert.

### `chaosx.nr8.report.a`

Before: Record the incident.

After: A troubling development.

### `chaosx.nr8.2.d`

Before: A message circulated through several foreign ministries today. Every government named in the document disowns it, yet each ministry has read the text and another diplomatic exchange has already soured.

After: An unsigned telegram accusing several governments of secret mobilisation has reached foreign ministries. Its circulation has provoked angry exchanges between the capitals named in it.

### `chaosx.nr8.3.d`

Before: Reporters have noticed embassy staff abandoning front entrances in several capitals. Guards at the front gates have doubled, and several governments are answering with readiness orders as staff move through side doors.

After: Embassy staff use side entrances under armed guard. Reporters gather at the deserted front gates, and rumours of an imminent rupture spread through the surrounding streets.

### `chaosx.nr8.4.t`

Before: The Calm Map Says Nothing

After: Unease Along the Frontier

### `chaosx.nr8.4.d`

Before: Public measures say the world can grow no more tense, yet clerks still copy new warnings, commanders ask for clearer orders, and newspapers find darker words that make restraint harder.

After: Patrols challenge travellers along the frontier, and commanders demand clearer orders. Newspapers carry fresh accusations each morning, deepening the fear of war.

### `chaosx.nr8.5.d`

Before: Neutral shipping firms have begun rewriting their rates as merchants hear war in every delayed cargo and several ministries take the invoices personally.

After: Insurers in neutral ports have raised their premiums against the risk of war. Merchants face dearer voyages, and the increases have stirred fresh distrust between trading partners.

### `chaosx.nr8.6.d`

Before: Two capitals received the same rumour through different channels, with the same phrasing, the same missing signature, and the same urgent warning. The matching message has turned suspicion on every office that handled it.

After: Two capitals received the same rumour of mobilisation through separate channels. The identical wording and missing signature have cast suspicion on the embassies that passed it along.

### `chaosx.nr8.7.d`

Before: Staff cars were seen outside several ministries long after midnight. The meetings require blackout curtains, extra guards, and sealed orders, and the streets around the buildings have emptied.

After: Military staff cars line the streets outside several ministries after midnight. Armed guards keep passers-by away from the shuttered buildings, and rumours of mobilisation spread across the capital.

### `chaosx.nr8.8.d`

Before: A naval movement passed without public explanation today. Harbour offices withheld ship names, and foreign staffs are already planning around the silence.

After: Warships left harbour under radio silence. The secrecy has alarmed neighbouring naval commands, which are drawing up plans for a possible confrontation at sea.

### `chaosx.nr8.9.d`

Before: Lamps stayed lit along a quiet border through the night. Weather, training, and paperwork failed to explain the activity, and patrols are no longer waiting for diplomats.

After: Lamps burned through the night at frontier posts. Reinforced patrols challenge traffic on the border roads, and nearby residents fear that a mistaken shot could start a clash.

### `chaosx.nr8.10.d`

Before: The third denial came faster than the first accusation. By the time it reached the morning papers, several foreign editors treated its speed as evidence, and several staffs filed the article beside their readiness orders.

After: A third denial of mobilisation has reached the morning papers. Foreign editors call it evidence of concealed preparations, and commanders in neighbouring countries put their troops on alert.

### `chaosx.nr8.12.d`

Before: The briefing began with ordinary phrasing and ended with several border districts receiving instructions nobody wanted to sign. By evening, no one expected the day to remain ordinary.

After: Several frontier districts received mobilisation instructions after the morning briefing. Officers hesitate over the unsigned orders, and troops wait beside the roads for word to move.

### `tensions_rising_alarmist_rearmament_desc`

Before: Staff rooms, newspapers, and ministries are pressing for visible readiness as the reason for it becomes harder to hide.

After: Newspapers and military commanders press the government to prepare its forces for war.

### `tensions_rising_general_staff_fever_desc`

Before: Military offices are preparing around rumours that circulate through every diplomatic channel.

After: The general staff prepares for mobilisation as rumours spread through the embassies.

### `tensions_rising_permanent_alert_desc`

Before: The state treats every denial as a possible order to prepare.

After: Troops remain on alert as fresh accusations deepen distrust of neighbouring countries.

### `chaosx.events_log.window.event_details.tensions_rising`

Before: Public accusations, leaked cables, and military bulletins unsettle foreign offices. Rumours travel faster, relations sour, and frontier commands prepare for a clash that no capital can explain away.

After: Public accusations and leaked military cables spread rumours of war. Embassies guard their entrances, shipping grows dearer, and frontier commanders put their patrols on alert.

### `chaosx.events_log.window.evolution_details.tensions_rising.body.event_detail`

Before: Diplomatic Fever marks the world learning to panic faster. Each milestone carries the same alarming headline farther: from crowded cable rooms and public accusations to sleepless general staffs, permanent alert, and the risk of a limited frontier clash.

After: Rumours of mobilisation spread from embassies to newspapers and frontier posts. General staffs work through the night, troops remain on alert, and exhausted patrols grow quicker to challenge movements across the border.

### `chaosx.events_log.window.evolution_details.tensions_rising.body.stage_1`

Before: Cable traffic swells as embassies answer rumours with denials. Relations begin to fray, and each new dispatch makes the next alarm easier to believe.

After: Embassy telegraph rooms work through the night as leaked cables fill the papers. Rumours of mobilisation deepen distrust between neighbouring capitals.

### `chaosx.events_log.window.evolution_details.tensions_rising.body.stage_2`

Before: Competing accusations spread through more capitals. Delayed reports keep old suspicions alive, while cautious governments quietly raise their readiness.

After: Rival governments accuse their neighbours of preparing for war. Newspapers repeat the accusations, and border commanders tighten their patrols.

### `chaosx.events_log.window.evolution_details.tensions_rising.body.stage_3`

Before: General staffs begin treating rumour as operational guidance. Diplomatic shocks linger, frontier incidents become harder to contain, and governments watch the Thin Wire with growing unease.

After: General staffs work through the night preparing troops for mobilisation. Exhausted officers weigh fresh rumours, and frontier patrols grow quicker to challenge unfamiliar movements.

### `chaosx.events_log.window.evolution_details.tensions_rising.body.stage_4`

Before: Extended alert becomes the normal condition. Heavier accusations and exhausted border commands make a limited frontier clash more likely as the border grows harder to control.

After: Troops remain on alert along the frontier as commanders delay leave. Fresh accusations deepen distrust, and exhausted patrols risk turning a confrontation into a clash.

### `chaosx.nr8.2.a.tt`

Before: Additional world tension, chaos, and a timed opinion shock are applied.

After: World tension and chaos increase. Diplomatic relations temporarily worsen.

### `chaosx.nr8.3.a.tt`

Before: Additional world tension, chaos, a timed opinion shock, and a small AI readiness push are applied.

After: World tension and chaos increase. Diplomatic relations temporarily worsen, and some foreign governments adopt a more guarded military posture.

### `chaosx.nr8.4.a.tt`

Before: Additional world tension, chaos, and a timed opinion shock are applied.

After: World tension and chaos increase. Diplomatic relations temporarily worsen.

### `chaosx.nr8.5.a.tt`

Before: Additional world tension, chaos, and a timed opinion shock are applied.

After: World tension and chaos increase. Diplomatic relations temporarily worsen.

### `chaosx.nr8.6.a.tt`

Before: Additional world tension, chaos, and two timed opinion shocks are applied.

After: World tension and chaos increase. Diplomatic relations temporarily worsen between several countries.

### `chaosx.nr8.7.a.tt`

Before: Additional world tension, chaos, a timed opinion shock, and AI readiness pressure are applied.

After: World tension and chaos increase. Diplomatic relations temporarily worsen, and some foreign governments adopt a more guarded military posture.

### `chaosx.nr8.8.a.tt`

Before: Additional world tension, chaos, a timed opinion shock, and AI readiness pressure are applied.

After: World tension and chaos increase. Diplomatic relations temporarily worsen, and some foreign governments adopt a more guarded military posture.

### `chaosx.nr8.9.a.tt`

Before: Additional world tension, chaos, and heavier timed opinion shocks are applied. At higher chaos levels, a safe adjacent pair can be pulled into a non-transfer border war.

After: World tension and chaos increase. Diplomatic relations temporarily worsen between several countries. At higher chaos levels, neighbouring countries may fight a border clash without exchanging territory.

### `chaosx.nr8.10.a.tt`

Before: Additional world tension, chaos, and heavier timed opinion shocks are applied. At higher chaos levels, a safe adjacent pair can be pulled into a non-transfer border war.

After: World tension and chaos increase. Diplomatic relations temporarily worsen between several countries. At higher chaos levels, neighbouring countries may fight a border clash without exchanging territory.

### `chaosx.nr8.12.a.tt`

Before: Additional world tension, chaos, multiple timed opinion shocks, and AI readiness pressure are applied. At higher chaos levels, this incident has the strongest chance to start a safe non-transfer border war.

After: World tension and chaos increase. Diplomatic relations temporarily worsen between several countries, and some foreign governments adopt a more guarded military posture. At higher chaos levels, the risk of a border clash is greater. No territory changes hands.

### `chaosx.nr8.baseline.effect`

Before: World tension increases by 100.

After: World tension increases by [?tensions_rising_display_world_tension|0].

### `chaosx.nr8.stage_1.effect`

Before: World tension increases by 100. Chaos increases by 10.

After: World tension increases by [?tensions_rising_display_world_tension|0]. Chaos increases by [?tensions_rising_display_chaos|0].

### `chaosx.nr8.stage_2.effect`

Before: World tension increases by 200. Chaos increases by 15.

After: World tension increases by [?tensions_rising_display_world_tension|0]. Chaos increases by [?tensions_rising_display_chaos|0].

### `chaosx.nr8.stage_3.effect`

Before: World tension increases by 500. Chaos increases by 25.

After: World tension increases by [?tensions_rising_display_world_tension|0]. Chaos increases by [?tensions_rising_display_chaos|0].

### `chaosx.nr8.stage_4.effect`

Before: World tension increases by 1000. Chaos increases by 50.

After: World tension increases by [?tensions_rising_display_world_tension|0]. Chaos increases by [?tensions_rising_display_chaos|0].

## Audit results and rationale

Missing keys: none among the assigned event references and all 15 scripted output branches.
Duplicate keys: none in the assigned localisation file.
Scripted localisation: all three getters have valid literal output keys and fallback branches.
`GetTensionsRisingEffectText` now assigns display-only temporary variables directly in each branch from the same constants used by gameplay, with `|0` integer formatting.
These assignments invoke no helpers and introduce no saved variables.
The baseline displays 100 world tension, and stages I-IV display 100/10, 200/15, 500/25 and 1000/50 world tension/chaos at current tuning.
Every dynamic call already present was preserved.
The only new tokens are the two constant-backed display values.

`python .tools/report_colour_audit.py --event 008` returned `total keys with colour: 0` both before and after the patch.
Direct report titles/descriptions and every scripted output branch are plain text.
The coloured evolution-type key remains in its dark GUI consumer and is not referenced by a report description.
No em dashes, semicolons, update-history phrasing or banned process terms were introduced.
No sourced or attributed quotation occurs in the inspected assigned surfaces, so there was no quotation to alter.
The localisation UTF-8 BOM and single-line entries are preserved, and scripted localisation retains its original encoding.

### Prose quality

Vagueness: replace unnamed pressure, signals, and preparation around silence with patrols, troops, premiums, and concrete accusations of mobilisation.
Bloat: remove repeated lists of identical phrasing and claims that an ordinary day will cease to be ordinary.
Obvious explanation: remove applied-effect narration from incident tooltips.
Repetition: give each report a concrete incident, and remove the repeated frontier-control clause in Stage IV details.
Overcomplication: replace safe adjacent pairs, timed opinion shocks, non-transfer wars and AI posture pressure with readable diplomatic and military consequences.
Style repair: remove official-denial contrast structures and description of visible UI measures from the calm-map report.
Its title is now `Unease Along the Frontier`.
No gameplay actions, tuning values, chance targets or eligibility checks were changed.

### Cross-surface handoff

Spreadsheet owner must mirror the final strings for `chaosx.events_log.window.event_details.tensions_rising`, `chaosx.events_log.window.evolution_details.tensions_rising.body.event_detail`, and all four `chaosx.events_log.window.evolution_details.tensions_rising.body.stage_*` keys.
Their exact final wording appears above.
The workbook was not inspected or edited, so whether it currently differs is unresolved.
Shared GUI and Event Log/Details source files were not edited.
Existing evolution stage titles remain unchanged.
Historical suggested prose in the source spec differs from this finished text and remains design direction rather than final YAML.

### Dynamic opportunities and remaining decisions

Incident tooltips still use qualitative consequences because affected country pairs and posture recipients are selected within immediate effect chains without stored popup-bound actors.
Names should not be invented or drawn from stale targets.
Exact incident numbers could be exposed through additional constant getters, but the accepted ordinary-popup promise keeps hidden pair-selection mathematics and timer pressure out of view.
The existing main-stage effect summary remains intentionally limited to world tension and chaos.

## Validation limits and route blockers

Connected discovery advertised `hoi4.reference_context`, `hoi4.reference_search`, and `hoi4.event_inspect`, but each live call returned `MCP tool ... is not available to the model`.
The advertised `hoi4.event_render` route was absent from the callable tools object and raised `TypeError: tools.mcp__hoi4_agent_tools__hoi4_event_render is not a function`.
No event or GUI artifact URI was produced.
Parent must carry this blocker and review final Event Details text through the mandatory GUI render route when callable.
Source checks do not establish rendered wrapping, overflow, clipping or runtime branch evaluation.
No standalone Technology Tree Viewer tool was discovered separately from technology routes, recorded as an exposed-package gap.
Event 008 does not own a technology surface.

## Offline reference evidence

References were read directly after the MCP route failures.
Line spans are one-based.

- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, lines 65-80, 184-210, 656-691, 731-752, SHA-256 `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, lines 12-46, 216-245, SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, lines 7820-7844, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`, lines 1-35, SHA-256 `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/00_scripted_localisation.txt`, lines 1-35, SHA-256 `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587`.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill files changed.
No new design plan or mechanics handoff was needed.
No staging or commit performed, per parent ownership instructions.
