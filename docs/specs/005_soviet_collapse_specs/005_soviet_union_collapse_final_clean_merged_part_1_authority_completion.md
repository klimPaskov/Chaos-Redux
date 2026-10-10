# Soviet Union Collapse Final Clean Merged Specification, Part 1
# Implementation Authority, Contradiction Cleanup, and Completion Contract

## Core contract

This package is the clean source of truth for continuing Soviet Union Collapse event 005. It merges the Markdown files in the supplied zip into a cleaner sequence of specifications. The older files are treated as design sources, correction sources, and skill guidance. They should no longer be used as competing instructions after this package is copied into the repo.

The implementation goal is not to add a few more fixes. The goal is to prove that every requested system has been implemented without hidden simplifications, filler content, shallow focus trees, missing high-chaos splinters, missing focus icons, broken mission clarity, weak balance, or fallback country packages.

This event is a major Chaos Redux crisis. It must feel like a full system, not a release effect with focus trees attached.

## Required working stance

The agent must implement cleanly and report honestly.

The agent must not claim completion unless the implementation satisfies this package and the final report proves it. If any requested item is not implemented to the fullest extent, that item must be listed as a simplification, omission, deviation, or blocker. Even a small shortcut must be reported.

Examples of reportable deviations:

- a requested tag exists but has no focus tree
- a country has flags but no history setup
- a focus tree exists but has no real expansion branch
- a focus tree mostly grants ideas or flat factory rewards
- focuses have generic icons or duplicated icons
- focus names and descriptions do not match rewards
- decisions contain vague requirements such as required states
- missions only check passive stockpiles, manpower, stability, or war support
- a local league forms with one member
- Union Unmade releases only some republics
- a high-chaos splinter such as the Northern Revenant Fleet is missing
- a super-event is used for a minor regional league formation
- repeated remove-idea effects appear in focus tooltips
- any asset, localisation, AI behavior, event log, evolution log, or docs are missing

If no simplifications were made, the final report must explicitly state:

`No simplifications, omissions, approximations, or weaker substitutes were used.`

That statement is valid only when the implementation ledger supports it.

## Conflict resolution

The source files contained several older instructions that conflict with later corrections. Resolve them this way.

### Focus tree mapping

Earlier drafts mapped or implied exact focus-by-focus structures. Later skill guidance changed this to path-level design. The final instruction is path-level design.

The spec defines routes, branch families, required mechanics, reward styles, route locks, AI behavior, localisation tone, and completion gates. The implementation agent owns final focus count, final focus names, coordinates, and detailed prerequisites. The final in-game layout must still be non-linear, readable, replayable, and faithful to the route architecture.

### Focus tree size

Older drafts sometimes emphasized large focus counts. The final instruction is depth over count.

Large countries can justify very large trees, but size is not proof of quality. A focus tree is unacceptable if it is just a large vertical checklist. A smaller tree with meaningful branches, mechanics, decisions, tradeoffs, and route payoffs is better than a huge tree with repeated rewards.

### Super-event scope

Older drafts suggested super-events for several dramatic developments. Later corrections narrowed super-event use. The final instruction is strict super-event scope.

Do not use super-events for local league formation, ordinary republic release, internal republic release, normal regional cascades, ordinary recognition conferences, or local league war votes. Use news events, report events, event-log entries, or decision notifications.

Allowed Soviet Collapse super-events are:

- Union Unmade
- Black Banner Returns, only when Black Banner becomes a major state actor
- The Dead Are Citizens, only when death-state mechanics become major
- The World as One Factory, only when factory-state mechanics become major
- Every Port a Council, only when sailor or naval council mechanics become major
- other rare major high-chaos transformations explicitly implemented as campaign-defining states

### Kazakhstan and Central Asia

Kazakhstan should not be the ordinary first southern domino. The first southern pressure should more often begin through Uzbekistan, Turkmenistan, Tajikistan, Kyrgyzstan, local committees, mountain pressure, or border events. Kazakhstan becomes more likely after southern cascade pressure, other southern republics are free, command obedience is weak, foreign influence reaches Central Asia, or chaos is high.

### Union Unmade

Union Unmade is not a first-month consequence in a calm strong Soviet game. It is a terminal collapse state caused by sustained severe failure, high threat, low Moscow authority, multiple republics, failed containment, foreign intervention, league coordination, and major rail, depot, or command failures.

When Union Unmade fires, all ordinary and internal Soviet republics must be released, Soviet republican puppets and subjects must be freed, released republics must receive dynamically scaled units, local leagues must form where valid, the Free Republics' League must form or expand, and released republics must enter the anti-Soviet war.

### Assets

Older asset notes allowed reuse when assets survived prior implementation. The final rule is reuse only if suitable. Reuse existing assets when they are valid, correctly sized, correctly wired, documented, and visually appropriate for the exact route identity. Every focus must have a unique icon assignment. Do not reuse one generic icon across many focuses unless the icon is intentionally part of a staged visual family and the variants are distinct enough to read as separate focuses.

Historical flags, real historical symbols, and real leader portraits require attributed source evidence.
Current production follows [chaos-redux-event-assets](../../../.claude/skills/chaos-redux-event-assets/SKILL.md) and the specialist ownership in Part 7.
A symbolic, high-chaos, council, factory, or cult label does not independently authorize a generated portrait for a grounded person or institution.

### Remove-idea tooltip spam

The current implementation problem where many focus hovers show repeated remove-idea effects must be fixed.

Focuses may replace or upgrade ideas, but the tooltip should show clean player-facing text, not a long mechanical stack of remove-idea effects. Use hidden effects, custom effect tooltips, scripted effects, or idea-upgrade helper patterns so the player sees a concise statement such as:

- `Replaces Broken Ministries with Emergency Ministries.`
- `Mitigates Improvised Command.`
- `Upgrades Foreign Volunteer Cadres.`
- `Removes Supply Confusion after the rail mission succeeds.`

Do not put exposed remove-ideas on every focus hover.

## Required ledger and reporting

The separate full-ledger, focus-tree, balance, mission and validation report files that earlier drafts required are superseded: the repository keeps one current report per event instead of a family of parallel status files.

Two documents carry the coverage obligation:

- `docs/events/005_soviet_collapse_implementation_audit.md` is the single current implementation, coverage and validation-status report.
- `docs/assets/005_soviet_collapse/manifest.md` is the asset manifest.
  It is absent in the current checkout, so asset provenance remains `unresolved`.

The coverage table inside the implementation audit uses these columns:

| Requirement | Source section | Required implementation | Implemented files | Evidence | Status | Deviation or blocker |
| --- | --- | --- | --- | --- | --- | --- |

Allowed statuses:

- `complete`
- `partially_complete`
- `simplified`
- `blocked`
- `not_started`
- `not_applicable_by_source_rule`

A missing feature with no coverage row is a failed goal.
The focus-tree, mission, balance and validation findings are sections of that one report, not separate files.

## Required source reading

The repository rules in `CLAUDE.md` already define the reference, wiki, vanilla, skill and documentation reading duties; they apply here without restatement.

Read in addition, because they are specific to this event:

- every part of this package, plus the UWR and KMB companion documents
- the current implementation audit and the working ledgers in `docs/plans/005_soviet_collapse_plans/`
- the existing Event 005 event, decision, focus, idea, AI, localisation and asset sources before changing any of them
- the Event 006 IW-039 contract referenced in Part 6, before touching the Don foothold

If a named file is missing, report the blocker with exact path evidence.

## Completion gate

The goal is incomplete unless all of these are true:

- every required actor, republic, internal republic and high-chaos splinter has a coverage row
- the focus-tree, mission, balance and validation sections of the implementation audit are current
- the asset manifest exists and records every visible element
- repeated remove-idea tooltip spam is removed
- every focus has a unique icon assignment
- every simplification is reported and every blocker is reproducible

A short completion note is not acceptable.
Live-game confirmation is the user's, so a documented source-derived check is the agent's completion evidence and an unavailable tool limits a claim instead of blocking the work.
