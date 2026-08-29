# Event 34 Industrial Boom repository cross-check

## Review scope

The public `klimPaskov/Chaos-Redux` repository was inspected on 2026-08-27 after the supplied project-source pass. The repository default branch is `master`. GitHub code search returned revision `2d1653381c8f495bb587cc22941e428db810bc09` for the relevant indexed files.

The cross-check focused on the current Event 34 and Event 35 entry files, their localisation, the Event 34 idea, and repeatable-event registration. The purpose was to preserve live identifiers and identify legacy behavior that the rework must replace deliberately.

## Current Event 34 entry

Source: [`events/034_industrial_boom.txt`](https://github.com/klimPaskov/Chaos-Redux/blob/master/events/034_industrial_boom.txt)

The current entry already uses namespace `chaosx.nr34` and canonical entry ID `chaosx.nr34.1`. The hidden entry selects a random major or human-controlled country, schedules `chaosx.nr34.2`, and grants the timed `industrial_boom` idea for 180 days. The visible event uses `GFX_report_event_airplane_factory` and schedules `chaosx.news.39`.

Design consequences:

- Preserve `chaosx.nr34.1` and the existing namespace.
- Preserve `chaosx.nr34.2` or migrate it only through a complete reference update.
- Treat the 180-day idea as legacy stub behavior. The accepted design uses a dynamic lifecycle and cannot retain a fixed expiry as its resolution rule.
- Preserve `chaosx.news.39` when it remains the opening news slot, or migrate the slot and every reference together.
- Replace the generic opening picture through the accepted event-owned asset workflow.
- Keep the current major-or-human eligibility principle while adding the full valid-target contract from the specification.

## Current Event 34 idea

Source: [`common/ideas/034_industrial_boom_ideas.txt`](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/ideas/034_industrial_boom_ideas.txt)

The current `industrial_boom` idea grants large static bonuses to consumer goods, production-efficiency ceiling, building speed, production-efficiency growth, factory output, local resources, and research speed. It also blocks ordinary civil-war inheritance through `allowed_civil_war = { always = no }`.

Design consequences:

- Keep the stable `industrial_boom` identifier when it remains useful as the opening lifecycle carrier.
- Do not treat the current modifier bundle as the final balance precedent. The rework must tune practical output across country conditions and use staged or dynamic effects.
- Research speed and broad local resource growth are legacy effects, not mandatory parts of the accepted baseline promise.
- Civil-war behavior must follow the explicit active-boom and state-project transfer contract. The existing idea inheritance rule cannot substitute for full cleanup and split handling.
- Avoid stacking the legacy idea with new dynamic modifiers in a way that doubles the intended bonus.

## Current Event 34 localisation

Source: [`localisation/english/034_industrial_boom_l_english.yml`](https://github.com/klimPaskov/Chaos-Redux/blob/master/localisation/english/034_industrial_boom_l_english.yml)

The existing localisation defines the entry title, visible event, option, and `chaosx.news.39` text. Its baseline vocabulary already centers factories, workers, investment, transport, construction, trade, exports, and jobs.

Design consequences:

- Preserve valid key identities when the final event surface still uses them.
- Rewrite the text from the full tone and information directions in specification part 9.
- Keep the concrete industrial vocabulary, then add dynamic actor, state, phase, threshold, and consequence references where the final surface needs them.
- Do not expose planning labels, hidden formulas, or evolution outcomes in the opening text.

## Current Event 35 entry

Source: [`events/035_great_depression.txt`](https://github.com/klimPaskov/Chaos-Redux/blob/master/events/035_great_depression.txt)

The current Event 35 entry uses namespace `chaosx.nr35`, canonical entry `chaosx.nr35.1`, visible event `chaosx.nr35.2`, a fixed 365-day `great_depression` idea, and `chaosx.news.40`. It independently selects a random major or human-controlled country.

Design consequences:

- Preserve the Event 35 namespace, entry IDs, and news slot unless every reference is migrated together.
- Replace the fixed one-year crisis with Event 35's own dynamic severity and recovery lifecycle when that event is implemented.
- Add one reusable fail-closed start and deepen API owned by Event 35.
- Event 34 must call that API for the exact boom country and cannot imitate the current independent random-target entry.
- Existing Event 35 activity must be deepened in place without duplicate ideas, categories, or history rows.

## Current Event 35 localisation

Source: [`localisation/english/035_great_depression_l_english.yml`](https://github.com/klimPaskov/Chaos-Redux/blob/master/localisation/english/035_great_depression_l_english.yml)

The existing keys cover the independent opening and `chaosx.news.40`. They describe market collapse, unemployment, idle factories, business closure, and family hardship.

Design consequences:

- Preserve key identities where the final surface still uses them.
- Add source-aware text for a depression inherited from Event 34.
- Keep independent and inherited entry wording distinct while sharing the same Event 35 mechanics.
- The inherited text should use the frozen Event 34 history and avoid displaying raw inheritance variables.

## Event-system registration

Source: [`common/scripted_effects/chaosx_logic_effects.txt`](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_effects/chaosx_logic_effects.txt)

The current category initializer registers both Event 34 and Event 35 in `global.repeatable_events`. This matches the accepted catalog identity.

Design consequences:

- Keep Event 34 and Event 35 registered as repeatable events.
- The direct Event 34 crash call must bypass a second global pacing transaction while retaining Event 35's country crisis history.
- The implementation must update the reworked-event default enable state, event details, actor mapping, evolution catalog, and event history in the same change.

## Cross-check result

The repository confirms that Event 34 and Event 35 currently exist as small legacy implementations. The accepted package is a rework specification, not a new event reservation. Stable namespaces, entry IDs, idea identity, news slots, and repeatable classification need deliberate migration. The current fixed-duration ideas and static modifier packages do not satisfy the accepted design and should not survive accidentally beside the new lifecycle.
