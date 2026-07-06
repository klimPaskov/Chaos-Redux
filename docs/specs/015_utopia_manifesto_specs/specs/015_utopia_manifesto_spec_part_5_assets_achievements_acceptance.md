# Event 015 Utopia Manifesto, part 5 assets, achievements, super-events, and acceptance criteria

## Asset direction

The asset package should make the event feel like a recovered manifesto becoming a state machine. Use parchment, early printed pages, island maps, common shelves, plain halls, survey instruments, household tables, railway corridors, coastal pilot marks, daughter commonwealth seals, and geometric no-place symbols. Avoid generic maps as the main visual unless the asset is a land dossier or focus icon. The visual center should be the book, the household, the shelf, the worker, the survey, the ward, or the subject network.

## Core visual assets

| Asset family | Type | Source mode | Direction |
| --- | --- | --- | --- |
| opening report image | report event image | sourced or generated | old Utopia-like book or manifesto being read in a small capital, period documentary treatment |
| Need Ledger category icon | decision category icon | generated icon | open book with measuring compass and shelf marks |
| Common Stores idea | national spirit icon | generated icon | public shelf, plain loaf, tools, and ledger tabs |
| Vocational Freedom idea | national spirit icon | generated icon | hands choosing between tools, no readable text |
| Land Need idea | national spirit icon | generated icon | compass over fields and houses, not a conquest map |
| Outopia Fracture idea | hidden or warning icon | generated icon | cracked seal or impossible island shape |
| subject value icons | idea or GUI icons | generated icons | Local Stores, Local Consent, Vocational Acceptance, Dependence, Autonomy, and Fracture Import |
| Utopian Commonwealth flag variants | flags | generated fictional | clean emblem, readable at all HOI4 sizes |
| Eutopian League emblem | faction emblem | generated fictional | table, island, or shared shelf motif |
| subject cosmetic flags | flags | generated fictional | Charter, Surveyor, Mandate, Daughter Commonwealth, and No-Place variants when visible |
| Surveyor State portrait | leader or council portrait | generated fictional when needed | institutional survey council or planner portrait |
| Household Compact council | leader or council portrait | generated fictional when needed | pluralist council, not crowd clutter |
| No-Place branch portrait | symbolic leader portrait | generated fictional, animated optional | ledger council or impossible bureaucratic icon |
| focus icon family | focus icons | generated icons | book, shelf, compass, home, rail, harbor, council, guard, charter, ward, subject, ultimate pillar |
| decision icon family | decision icons | generated icons | store convoy, ward magistrate, charter plebiscite, false dossier, settlement congress, precinct conversion |
| achievement icons | achievements | generated icons | route-specific completed icons plus required variants |

Historical or early printed Utopia imagery can be sourced for the opening report if license and source allow. Do not generate real Thomas More or real historical figures as leader portraits.

## Animated assets

Animation should clarify mechanic states. It is not required for every icon. It is strongly recommended for the Need Ledger board, hidden branch reveal, subject warning states, and Ultimate Utopia convergence.

| Animated asset working label | Surface | State | Size direction | Source mode |
| --- | --- | --- | --- | --- |
| need ledger seal | decision category or GUI header | balanced, shortage, crisis | category specific, likely larger than 32x32 | generated frame set through icon or art subagent |
| outopia fracture seal | hidden warning panel | dormant, cracked, revealed | GUI icon or route seal | generated frame set |
| subject warning frame | selected subject card | stable, empty stores, unrest, settlement ready | GUI card overlay | generated frame set if subject GUI exists |
| ultimate pillar seal | final convergence branch or GUI | locked, ready, completed | route emblem or focus-adjacent sprite | generated frame set |
| common table league emblem | faction or GUI panel | inactive, active, crisis | GUI emblem | generated frame set if league GUI exists |
| no-place portrait overlay | leader or GUI portrait | hidden route revealed | 156x210 overlay or portrait package | generated symbolic frames |

Every animated package needs source frames, processed frames, sheet PNG, sheet DDS, static fallback DDS, preview GIF, manifest, and gfx handoff.

## Super-event package directions

The event has two late super-event candidates. A third subject-network super-event can be considered if the implementation makes daughter commonwealths a major regional order change.

| Working label | Role | Trigger direction | Tone | Image direction | Research gates |
| --- | --- | --- | --- | --- | --- |
| commonwealth reveal super-event | ideological transformation and regional order | form Utopian Commonwealth, lead Eutopian League, or reach a peaceful Ultimate Utopia ending | hopeful, strange, controlled, public | public halls, island map, shelves, delegates, period documentary or symbolic scene | final title, quote, button remark, and audio require research |
| no-place mandate super-event | coercive world-order announcement | high Fracture, Needful War success chain, hidden branch finisher | alarming, bureaucratic, righteous in its own voice | measuring instruments over occupied wards, no generic apocalypse | final title, quote, button remark, and audio require research |
| daughter commonwealth super-event | subject network announcement | several stable utopian subjects or League members support the World Household Congress | civic, formal, uneasy if subjects are mixed | parent common table surrounded by subject seals and store convoys | final title, quote, button remark, and audio require research |

The super-event text researcher should consider public domain or historical quotes about commonwealth, need, measure, law, and the danger of perfect states. The audio researcher should find licensed or public domain music with formal, ceremonial, or uneasy civic tone. No default or placeholder audio should be accepted as final.

## Achievement set

Achievements are required because the event creates a deep focus tree, mechanics, rare variants, formable outcomes, subject systems, and late enforcement goals. Use the full achievement matrix as the source list.

Additional achievement coverage beyond the first package must include:

| Achievement working id | Working label, not final localisation | Route coverage |
| --- | --- | --- |
| utopia_manifesto_ring_of_full_shelves | Ring of full shelves | subject stores and late network mastery |
| utopia_manifesto_no_ward_without_voice | No ward without voice | peaceful ward conversion and consent mastery |
| utopia_manifesto_measured_without_breaking | Measured without breaking | Surveyor protectorate management |
| utopia_manifesto_mandate_holds | The mandate holds | coercive subject management under pressure |
| utopia_manifesto_false_claims_buried | Bury the false claims | renunciation and restraint route |
| utopia_manifesto_daughter_commonwealths | Daughter commonwealths | final subject fate and convergence route |

Achievement titles and descriptions need final localisation written later. The working labels are not final copy.

## Documentation expectations

Implementation should create or update the canonical event doc for Event 15. It should explain the event premise, host eligibility, focus tree, Need Ledger values, decisions, integration rules, late enforcement, utopian subject forms, AI behavior, evolutions, super-event thresholds if implemented, assets, and limitations.

The spreadsheet row should be updated after implementation using final in-game event detail wording. The row should classify Event 15 as Minor Fire-Once and should not preserve World Tension Subsides wording.

## Localisation handoff

The planning package provides direction only. The implementation agent writes final localisation.

Needed text surfaces:

- event name mapping for Utopia Manifesto
- opening event title, description, and options
- event details window text
- evolution names and details for the five evolution stages
- focus titles, focus descriptions, and focus completion tooltips
- decision category title, description, and scripted value summaries
- decision names, descriptions, blocked requirements, and success or failure text
- utopian subject value names, selected subject text, and final fate text
- ideas and national spirits
- leader, party, cosmetic tag, faction, subject form, and formable names
- super-event localisation if late super-events are implemented
- achievement titles and descriptions
- scripted GUI labels and hover text

Tone guidance:

- early text should sound curious, public, and politically unsettled
- consent route should sound civic and practical
- Surveyor route should sound precise and state-centered
- Mandate route should sound righteous and severe
- hidden branch should sound measured, uncanny, and self-justifying
- subject text should show whether the project is keeping promises or exporting contradictions
- achievement text can be sharper but should not become cheap comedy

## Acceptance criteria

The event is ready for implementation acceptance only when the following design surfaces exist in game:

- Event 15 registered as Utopia Manifesto, Minor Fire-Once
- old World Tension Subsides behavior removed or replaced completely
- valid target logic avoids majors and strong industrial countries
- AI host accepts automatically
- human host can accept or refuse
- accepting host receives the Utopian focus tree
- focus tree is deep, uneven, and not reduced to five-focus main branches
- focus tree has opening, political, economy, military, diplomacy, expansion, special mechanic, hidden, subject, enforcement, and Ultimate Utopia convergence content
- Need Ledger values are visible and dynamic
- decisions and missions use concrete costs and objectives
- Land Need gates claims and demands
- claims can decay or be renounced when need is solved
- late enforcement can export, impose, or renounce Utopia abroad
- puppet utopias have subject values, decisions, support needs, failure states, and final fates
- wardship and integration use stores, support, compliance, resistance, subject values, and route choices
- AI route, decision, and subject behavior exists
- evolutions can be logged and change active actors or pre-fire opening as mapped
- cosmetic identities, flags, leaders, ideas, and assets are covered
- achievements are implemented with tracking and icons
- late super-event package is researched and wired if the late thresholds are included
- docs and spreadsheet are updated from final localisation
- focus, decision, localisation, country package, and completion audits are run before completion

## Simplification risks to report during implementation

The implementation agent must report any of these as simplifications or blockers:

- no scripted GUI for Need Ledger and no adequate decision category substitute
- focus tree reduced to a linear ladder or five-focus main branches
- Ultimate Utopia convergence omitted
- late enforcement omitted
- puppet utopias reduced to ordinary puppets with no mechanics
- Land Need replaced by ordinary permanent claims
- integration reduced to instant cores
- decisions mostly use political power or command power
- AI accepts but has no route plan
- hidden branch omitted without explicit queue or rejection
- assets left as placeholders
- super-event audio left as default or undocumented
- achievements not implemented
- old Event 15 spreadsheet wording left in place
- live repo restrictions preventing focus tree replacement
