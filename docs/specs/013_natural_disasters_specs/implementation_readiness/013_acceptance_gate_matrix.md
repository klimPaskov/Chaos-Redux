# Event 013 Natural Disasters, acceptance gate matrix

This matrix turns the expanded specs into implementation gates. A coding agent should not claim completion while any required gate is missing, simplified, or replaced by a placeholder.

## Core system gates

| Gate | Must be true | Failure signal | Evidence expected |
| --- | --- | --- | --- |
| Fresh system | Event 013 logic is created from the new specs. | Any old Natural Disasters logic is retained as the functional base. | File diff and completion notes identify fresh controller files and no preserved legacy branch. |
| One-row history | One Event 013 firing creates one Event 013 history row. | Warning, impact, aftermath, or follow-up subevents add extra Event 013 rows. | Targeted test or script review shows history recording only at sequence start. |
| Reusable call contract | Other events can request family, target mode, target country, target state or region, severity, news policy, report policy, aftermath policy, chain policy, and scaling overrides. | Callers copy damage logic or must fire one bespoke family event. | Scripted effect or equivalent helper docs show inputs, defaults, side effects, cleanup, and example calls. |
| Individual family trigger | Every implemented family can be called directly. | Only random disasters work. | Debug or scenario helper can call each family without manual event edits. |
| Target validity | Invalid country, state, region, heat-stack, sea-only, dead-tag, and impossible target cases resolve safely. | Disaster tries to damage invalid scopes or silently does nothing after consuming sequence state. | Target triggers and fallback resolution are documented with blocked reasons. |
| Delayed sequence | Multiple subevents do not land on the same day under normal sequence rules. | Baseline feels like one popup burst. | Delay controls and sequence queue are visible in script and test notes. |
| Event 051 separation | Event 013 heat calls detect active Heat Wave state and avoid stacking. | Heat family stacks with Event 051 effects. | Heat family trigger and blocked report path show the separation rule. |
| Event 046 placeholder | Event 046 remains inactive and unknown. | Old Earth Earthquake logic survives outside Event 013. | Event 046 file or catalog points to placeholder state only. |
| Event 099 bridge | Sandstorm does not keep a separate competing disaster system. | Event 099 duplicates sandstorm logic. | Event 099 is placeholder or bridges narrowly into Event 013 dust calls. |

## Damage and deaths gates

| Gate | Must be true | Failure signal | Evidence expected |
| --- | --- | --- | --- |
| Baseline impact | Baseline disasters damage buildings and population enough to matter. | Baseline deaths are tiny flavor numbers or buildings barely change. | Tuning table shows family-specific baseline bands and Deaths-system calls. |
| Evolution II scaling | Evolution II scales deaths and destruction harder through density, infrastructure, supply, devastation, stability, recovery weakness, and follow-up pressure. | Evolution II is only more frequent, not more dangerous. | Dynamic factors are visible in constants, helpers, and family calls. |
| Evolution III devastation | Abnormal disasters can devastate regions when family identity supports it. | Evolution III only adds stronger modifiers. | Abnormal family handlers can destroy large building amounts and cause large population losses under severe conditions. |
| Deaths-system visibility | Population losses feed the shared Deaths system clearly. | Population changes happen without Deaths tracking. | Deaths log integration and source types are documented. |
| Building specificity | Families damage relevant building types. | Every family applies the same generic damage package. | Family mini-spec mapping is preserved in effects or helper branches. |
| Aftermath pressure | Unresolved aftermath can worsen chain risk, refugee pressure, famine, disease, supply, stability, or war support where designed. | Aftermath is only a cleanup cost. | Aftermath ledger values influence follow-up checks and decision urgency. |

## Report, news, and notification gates

| Gate | Must be true | Failure signal | Evidence expected |
| --- | --- | --- | --- |
| Affected-country report | Hit countries receive a report after the specified delay. | Player must infer damage from map changes. | Report event or report path is called for serious impacts and direct helper calls. |
| Visible aftermath notification | Serious impacts open or refresh the aftermath category with a visible notification. | Category appears silently. | Notification effect is tied to impact resolution and direct helper calls. |
| Family-specific reports | Reports identify family and place with distinct direction. | Same generic report with swapped state name. | Localisation plan or keys map family, place, severity, and aftermath type. |
| News throttling | Early meaningful disasters can produce news, later small disasters are throttled. | Evolution II floods the player with news. | News policy, family priority, global throttles, and severity thresholds exist. |
| Direction-only spec compliance | Planning directions are not pasted as final player text. | Prompt fragments or research gates appear in localisation. | Localisation audit confirms no planning labels in final text. |

## Decision and mission gates

| Gate | Must be true | Failure signal | Evidence expected |
| --- | --- | --- | --- |
| Category lifecycle | Aftermath category opens, updates, and closes cleanly. | Stale disaster cards remain after cleanup or annexation. | Cleanup hooks cover recovery completion, invalid target, tag change, annexation, and disaster expiry. |
| Staged recovery | Early rescue, middle stabilization, and late reconstruction exist. | All recovery actions unlock at once. | Phase triggers, card state, and mission pools exist. |
| Active caps | Active missions are capped and prioritized. | Player sees a wall of nearly identical missions. | Active cap logic and priority scoring are documented. |
| Partial success | Missions can produce partial success where designed. | Every mission is binary. | Mission outcomes show success, partial success, failure, and follow-up paths. |
| Varied costs | Recovery uses equipment, manpower, fuel, trains, convoys, XP, stability, supply, local support, or other concrete costs where fitting. | Decisions default to political power purchases. | Cost localisation and decision effects show nonstandard costs. |
| Foreign relief variants | Foreign relief can help and create tradeoffs. | Relief is only a free positive button. | Relief variants include dependency, convoy, ideology, distance, war, and AI willingness factors. |
| AI equivalents | AI countries can recover and use relief logic. | Human-only GUI or decisions leave AI countries trapped. | AI decisions or scripted pulses perform equivalent actions. |

## Evolution, cluster, and scenario gates

| Gate | Must be true | Failure signal | Evidence expected |
| --- | --- | --- | --- |
| Baseline | Baseline sequence works with a narrow pool and meaningful local impact. | Baseline has all families at once or trivial effects. | Baseline controller settings are separate from evolved pools. |
| Evolution I | Evolution I widens variety and activity without major severity jumps. | Evolution I duplicates Evolution II scale. | Family pool and sequence count differ from impact severity. |
| Evolution II | Evolution II enables regional spread and chained aftermath. | Evolution II only changes news or family availability. | Regional state resolution and chain ledger exist. |
| Evolution III | Evolution III enables abnormal meteor, rupture, volcanic, tsunami, and moving corridor disasters. | Abnormal concepts only appear in text. | Abnormal controller, GUI state, and super-event eligibility exist. |
| Natural Disasters cluster | Cluster behavior can include multiple Event 013 entries with tiered severity. | Cluster treats one Event 013 as a normal single-slot member only. | Cluster member entries or cluster runtime context preserve repeated sequence behavior. |
| Disaster Barrage | Manual scenario uses the same controller and intensity model. | Scenario has separate disaster scripts. | Scenario launch effect passes type and intensity into Event 013 helpers. |

## Presentation, asset, and super-event gates

| Gate | Must be true | Failure signal | Evidence expected |
| --- | --- | --- | --- |
| Normal assets | Report, news, decision, category, idea, achievement, and aftermath assets are produced or honestly marked blocked. | Missing assets are hidden in completion notes. | Asset manifest lists every required asset and status. |
| Animation package | Abnormal moving-disaster UI uses frame-sheet animation with static fallback. | GIF, transform-only loop, or single shifted still is treated as final art. | Frame plan, source frames, sheet DDS, static fallback, and GFX handoff exist. |
| Static fallback | Every animated GUI element has a static fallback. | GUI breaks or shows nothing if animation is disabled or unavailable. | GFX handoff lists fallback sprite and animated sprite. |
| Super-event research | Super-event quotes, remarks, and audio are researched before final localisation or wiring. | Working labels become final titles or quotes. | Text and audio research notes include sources, confidence, license, and blockers. |
| Unique audio | Completed super-events do not use placeholder or undocumented audio. | Default, test-tone, or undocumented reuse remains. | Audio documentation records title, creator, source, license, duration, and final path. |
| Achievements | Achievements are difficult, tracked, localised, and have icons. | Achievements unlock automatically or lack assets. | Achievement registry, triggers, localisation, icon triplets, and docs align. |

## Documentation and audit gates

| Gate | Must be true | Failure signal | Evidence expected |
| --- | --- | --- | --- |
| Event docs | Event doc describes actual implemented behavior. | Docs repeat old deleted behavior or planning-only text. | `docs/events/013_natural_disasters/overview.md` aligns with implementation. |
| Spreadsheet | Catalog fields match final in-game wording after localisation exists. | Spreadsheet uses spec directions as final copy. | Spreadsheet worker handoff records changed rows and fields. |
| Localisation audit | Visible text is complete and follows style rules. | Missing keys, duplicate keys, process notes, or raw triggers remain. | Localisation auditor handoff lists key checks and changes. |
| Completion audit | A completion auditor checks spec versus implementation. | Main agent claims completion without independent audit. | Completion audit lists finished, partial, blocked, and missing surfaces. |
| Simplification report | Any missing item is reported clearly. | Placeholders or skipped systems are presented as complete. | Final report has a simplification, omission, and blocker section. |
