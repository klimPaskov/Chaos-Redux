# Air Cleanliness and Fallout World-End Source Spec, Part 12 Documentation, Catalog, and Acceptance Criteria

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

Current consequence correction: `specs/68_fallout_consequence_boundary.md` supersedes any baseline wording that treats Fallout itself as an Event Details row, evolution, ordinary super-event, or ordinary public catalog entry. Fallout is a consequence transition. A Fallout-owned triggerable-scenario sandbox row may expose the reserved manual launch surface without turning the consequence into an ordinary catalog event. Post-consequence survivor events may keep their own event history.

## Documentation surfaces

| Surface | Required update |
| --- | --- |
| Air Cleanliness mechanic doc | Replace simple threshold future plans with winter phase mapmode, state effects, treaty operations, and Fallout trigger rules. |
| Fallout world-end doc | New canonical source doc for black-screen transition and post-Fallout overhaul. |
| Triggerable scenarios doc | Document active raw id 14, the exact 10,154-target sweep, 41 batches, completion receipts, and seven-day barrier. |
| Chaos mechanics guide | Update Air Cleanliness, world-end rules, Deaths integration, and triggerable scenario list. |
| Event catalog spreadsheet | Do not add Fallout scenarios, survivor events, fields, or bridge notes. Fallout is outside the catalog system. |
| Asset manifests | Add mapmode, UI, icon, flag, portrait, report, news, and animated asset packages. |
| Music and super-event docs | Mark Fallout as not a normal super-event. If blackout audio is later added, document outside super-event pattern. |
| Subagent handoffs | Record every subagent patch or blocked report. |

## Spreadsheet direction

The event workbook and all exported catalogs contain no Fallout rows or Fallout-specific fields. Fallout mechanics, manual-launch details, internal survivor identities, and dormant content remain documented only in Fallout-owned specs, proofs, and system docs.

## Event details direction

Event Details should describe the premise, not raw effects. For Air Cleanliness, describe atmospheric contamination and visible winter spread. Fallout itself has no Event Details row. Post-consequence survivor cards may describe their own survival premise without registering the consequence as an event. Do not expose secret route requirements.

## Catalog additions

| Catalog | Row direction |
| --- | --- |
| Scenario catalog | Do not add Fallout. Keep raw id 14 and its proof status in Fallout-owned implementation docs. |
| Event catalog | Do not add Fallout consequences, survivor content, or Air Cleanliness bridge fields. |
| Cluster catalog | No cluster required unless later implementation creates a Fallout precursor cluster. |

## Implementation acceptance criteria

### Air Cleanliness

- New mapmode exists and is state-based.
- Winter phase appears on mapmode and in state tooltip.
- Winter phases create actual state effects.
- State population loss uses the Deaths system.
- Buildings and infrastructure can be damaged by severe phases.
- State categories can degrade after sustained severe phases.
- Treaty decisions interact with map states.
- AI uses air responses and does not ignore severe winter.
- Flavour events have real gameplay effects.

### Fallout transition

- Fallout can trigger above 100 percent contamination, from scripted terminal events, and from manual scenario.
- No 1000-percent contamination or 1000-Chaos requirement is used. Higher contamination may change urgency and severity.
- Fallout does not use normal super-event presentation.
- Black screen overlay blocks UI and shows timed text beats.
- Heavy world rewrite runs during blackout.
- Player continuation is handled when old tag dies or fragments.

### Manual scenario

- The manual Fallout id is raw id 14, one above the previous live maximum. Its exact 10,154-target sweep, 41 batches, completion receipts, and seven-day barrier are implemented and wired to the active launch path.
- Every valid province receives thermonuclear strike effects.
- There is a one-week delay before Fallout rewrite.
- If province-level strike is blocked, implementation reports blocker and does not silently downgrade.

### Post-Fallout overhaul

- State classes replace normal map identity.
- Old factions, normal trade, and incompatible events are disabled or transformed.
- Survival resources exist and are visible.
- The current static core gives every survivor the universal Fallout focus and decision package. Bespoke country trees and non-generic country packages remain a deferred expansion boundary and are not claimed by this tranche.
- Regional successors and mutant polities can appear with cosmetic identities.
- Decisions, missions, AI, assets, achievements, and docs are aligned.
- Gameplay remains interesting for ten more years.

## Required validation and audits

| Audit | Must check |
| --- | --- |
| Scripted system architect | Helpers, constants, state class assignment, cleanup, selected-state logic. |
| Decision mission auditor | Costs, tooltips, AI, clutter, exploit loops, cleanup. |
| Focus tree auditor | Route coverage, branch depth, icons, rewards, AI. |
| Country package auditor | Tags, cosmetics, leaders, flags, starting states, armies, AI, focus loading. |
| Localisation auditor | Missing keys, bad copied spec text, dynamic value formatting, blackout text quality. |
| Documentation curator | Source-of-truth map, stale plans, docs consistency. |
| Spreadsheet worker | Verify that Fallout rows and Fallout-specific fields remain absent. |
| Completion auditor | Spec versus implementation and missing depth. |

## Known remaining boundary

- Live HOI4 observation belongs to the user and is not a source gate.
- Bespoke country focus trees are future content.
- The ordinary 660-event living-world scheduler remains dormant at zero released blocks until its reviewed producers, release receipts, and activation setters exist.
- Field-level `copy_tag = THIS` behavior and same-chain human-control visibility remain engine-conditional observations with fail-closed receipts.

## Final quality bar

The core is incomplete if it only adds a mapmode, black screen, state damage, or generic countries without the connected Air, Air Winter, population, Deaths, buildings, state categories, governments, allocation, player continuation, focus, decisions, AI, assets, and documentation surfaces. Fallout is deliberately absent from catalog rows.
