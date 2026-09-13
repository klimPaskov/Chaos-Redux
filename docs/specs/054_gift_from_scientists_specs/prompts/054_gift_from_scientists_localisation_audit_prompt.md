# Event 54 Localization Audit Prompt

Use `chaosx_localisation_auditor` after Event 54 implementation has final gameplay behavior.

Read the complete Event 54 specification, all implemented Event 54 localization and scripted localization, the Event Details and event-log selectors, Scientific Research cluster text, achievement text, technology owner localization, and the catalog handoff.

## Audit surfaces

- event name mapping and debug name mapping
- initial global incident report
- consolidated country grant report
- full grant-list tooltip
- partial grant and pool-exhaustion state
- evolution names, descriptions, and history rows
- Event History and Event Details
- Scientific Research cluster title, premise, member lines, severity, and skip reasons
- registered custom-technology names
- both achievement titles, descriptions, eligibility, and locked state
- asset tooltips and any report-image reference
- documentation and workbook-facing text that mirrors in-game wording

## Required wording behavior

The report should describe unexplained completed discoveries appearing across unrelated institutions and fields. It should name each granted technology through its authoritative localization. It should explain a shortfall only as the absence of further usable discoveries for that country.

Keep the cause unresolved. Avoid aliens, time travel, Antarctica, a named mastermind, or an implied central conspiracy unless a later accepted design changes the event.

The acknowledgement should accept the result after the grant has already occurred. It should never imply that declining the option can reverse the technologies.

Evolution text should describe one breakthrough, several simultaneous breakthroughs, discoveries resembling hidden programs, and a final breakdown of normal research order. It should not expose exact grant counts as tuning or use terms such as pool, registry, callback, candidate, owner API, fail closed, reroll, safety profile, or provider.

Cluster text should present sudden discoveries, military simulation, doctrine leaps, singular researchers, and institutional setbacks as one unstable research wave. It should not present the cluster as a guaranteed reward bundle.

## Technical checks

- use UTF-8 with BOM for localization files
- use the repository key format without `:0`
- verify every dynamic technology name resolves for ordinary and registered candidates
- verify long grant lists wrap cleanly and retain readable ordering
- verify zero, one, partial, five, and ten-result forms
- verify country and actor scopes never leak another country's name or wording
- remove raw keys, raw variables, debug labels, update-history language, and implementation terminology
- preserve owner technology names unchanged inside Event 54
- keep Event Details and workbook-facing premise text aligned with final in-game wording

Apply only bounded localization fixes. Record changed keys, before and after behavior, remaining blockers, and any text that cannot be verified without the final gameplay or asset consumer.
