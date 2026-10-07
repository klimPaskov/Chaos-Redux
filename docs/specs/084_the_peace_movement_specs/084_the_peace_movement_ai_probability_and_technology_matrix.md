# 84 · AI, probability, technology, and capability audit matrix

## Evidence status

This is an intended-behavior specification and an implementation test plan. No HOI4 probability tools, technology graph tools, live game, or configured project subagent ran during this planning turn. Values below are proposed inputs and expected rankings. They are not empirical balance results, simulated victory rates, or validated cumulative timing curves.

## Government response priorities

The AI must first exclude impossible, unaffordable, and institutionally invalid actions. It must reserve enough capacity for essential active missions instead of starting three expensive projects that all fail. It values survival and credible existing commitments over a cosmetic identity change. Religious affiliation and private sexual orientation never act as universal response-weight shortcuts.

For a normal eligible five-option response event, provisional base weights are tolerate 30, negotiate 40, co-opt 15, suppress 10, and eradicate 5. Actual option probabilities require normalizing only the eligible options after contextual modifiers. Eradication receives AI weight zero without a serious actual armed or institutional threat, even if the player is legally permitted to choose a coercive campaign. An already delivered lawful settlement also zeroes gratuitous suppression and eradication choices absent a new distinct violation.

At peace with adequate civilian capacity, add 25 to negotiation and 15 to tolerance. During a genuine defensive war, add 25 to service negotiation and 15 to a valid accountable defense mandate. A government with a fulfilled co-optation project prefers maintaining it over reopening the same case. A high-Reaction government facing an actual armed seizure can add 25 to valid suppression and 15 to valid eradication. A documented failure of repression adds 25 to negotiation and zeroes repeating the identical failed campaign while its cooldown remains active.

These are event-option weights. Decision `ai_will_do` values and focus scores do not inherit the same probability interpretation. Their actual adapters, availability checks, evaluation schedules, and competing actions must be inspected.

## Evolution timing proposal

The next eligible evolution has base MTTH 90 days. A network of at least three affected countries applies a factor of 0.75. A completed transnational congress applies 0.75. At least one legitimate movement-led government applies 0.75. A qualifying unresolved repression sequence applies 0.50 where relevant to The Reaction or Armed Peace. A completed international reconciliation with no unresolved qualifying rupture applies 1.50 to conflict-dependent evolution, but does not suppress Love and Liberation's peaceful civic development.

Clamp the resulting intended interval to 30 through 180 days through the project's verified implementation pattern. Do not claim a clamped numeric variable is equivalent to a valid engine MTTH construct until the actual caller and adapter are inspected. A threshold or repression gate becoming false stops eligibility. Already completed stages remain completed.

Pre-fire high-Chaos initialization uses the explicit opening rules in Part 5 rather than retroactively running an MTTH timer before the event exists. Manual setup establishes the mature stages directly and logs that scenario history once.

## Named probability scenarios

| ID | World state | Required qualitative result or exact design boundary |
|---|---|---|
| AI01 | Peaceful pluralist origin, I15/R10, adequate resources | Tolerance or a focused agreement outranks an unprovoked coercive campaign |
| AI02 | Long defensive war, low War Support, real service grievance | Service negotiation and lawful defense preparation outrank an unrelated cultural prestige project |
| AI03 | Poor one-state player or AI country | Unaffordable actions excluded, no invalid civil-war partition, a reduced-scope civic path remains |
| AI04 | High I and low R with delivered legal agreement | No civil war, no automatic opposition-army spawn, maintenance remains valuable |
| AI05 | I60/R70 without a rupture | Danger and mediation visible, civil war not automatic |
| AI06 | I60/R70 with failed eradication and viable territorial commands | Command crisis and real partition path become available |
| AI07 | I80/R90 in an unpartitionable one-state map | Capital or authority crisis replaces unsupported territorial war |
| AI08 | A new high-Reaction government with no armed opponent | AI does not infer that ordinary religion or queer culture is a security threat |
| AI09 | Foreign contact with base 20% and no modifiers | The implemented event-roll result should match 20%, distinct from candidate weights |
| AI10 | Exchange, war weariness, tolerance, and sponsor all present | Raw 65% proposal clamps to 60% |
| AI11 | Invalid or closed nonexistent route | Candidate excluded, not granted a 5% floor |
| AI12 | Several foreign sponsors contact the same affected recipient | One +5 foreign-network monthly contribution, no multiplication |
| AI13 | Chaos199 / 200 | Love and Liberation gate changes only at the latter boundary |
| AI14 | Chaos399 / 400 | The Reaction gate changes only at the latter boundary |
| AI15 | Chaos599 / 600 with no repression history | Armed Peace remains ineligible in both states until its separate cause exists |
| AI16 | Chaos600 and two distinct recent repressions | Armed Peace timing becomes eligible after earlier stages, with proposed accelerants |
| AI17 | All evolution accelerants active | Intended interval clamp is honored, cumulative timing depends on the verified adapter |
| AI18 | Chaos falls below the next threshold midway through a wait | No new evolution while ineligible, established institutions remain |
| AI19 | Same scenario with scheduled war beginning on day60 | Evaluate the changed modifiers over the actual horizon, not one static snapshot |
| AI20 | Same scenario with settlement on day90 | Peaceful rights remain, conflict-dependent escalation responds to resolved grievances |
| AI21 | Rival existing factions and two interested governments | Congress respects sovereignty and membership, no invalid automatic faction swap |
| AI22 | A bloc leader has unpaid obligations and no equipment | Aid commitment does not invent supplies or force another human's shipment |
| AI23 | Valid defensive invasion during a convention | Emergency defense available without granting a completed constitution |
| AI24 | Focus paths with unavailable naval geography | Landlocked AI chooses passage or land logistics, not a fictitious fleet unlock |
| AI25 | Manual Low versus Maximum | Mature political setup is clear, no ordinary evolution delays, materially valid force allocation |
| AI26 | Chaos1000 and movement share51% | The Gay World fails the strict Chaos condition |
| AI27 | Chaos1001 and movement share50% | The Gay World fails the strict population condition |
| AI28 | Chaos1001, shareabove50%, no meaningful opponent | No terminal enemy is invented, diplomatic consolidation is available |
| AI29 | All terminal requirements met, branch disabled | No automatic terminal activation |
| AI30 | Terminal underway, rival ideology changes cosmetically | Active restoration command and war still count until substantively resolved |
| AI31 | Terminal underway, majority briefly lost | 90-day recovery crisis rather than immediate silent deletion of the scenario |
| AI32 | Two players act on congress and terminal gates on the same date | One committed global outcome, separate sovereign local choices |

## Required probability audit execution

The implementation parent must spawn `chaosx_ai_probability_auditor` with `fork_turns="none"` and a complete self-contained brief. Begin with `hoi4.probability_inspect` for the relevant event, decision, focus, MTTH, and helper sources. Use `hoi4.probability_evaluate` for named states, `hoi4.probability_sweep` for threshold and capacity boundaries, `hoi4.probability_simulate` only for declared uncertain inputs, and `hoi4.probability_compare` after a patch. Use `hoi4.probability_render` for probability, timing-survival, sensitivity, and unresolved evidence views when useful.

Separate exact, bounded, sampled, and unresolved results. Report the game-version adapter, scenario inputs, horizon, scheduled state changes, seeds where applicable, and competing options. A Python toy simulation, handwritten normalization, or guessed MTTH distribution does not replace the required project tools. The auditor supplies evidence and does not silently choose new design priorities or write source.

## Technology and doctrine contract

The event introduces political and organizational unit unlocks, not a new universal arms race. Existing infantry equipment, support equipment, transport, aircraft, ships, and doctrines remain the technological basis. No country gets a research slot simply for becoming a movement government. A new authority inherits legitimate knowledge from its actual parent, with complete package validation.

| Surface | Required graph or consumer inspection | Intended result |
|---|---|---|
| Rainbow and Guard subunits | Infantry equipment categories, supported subunit enablement, reinforcement ratios, training templates | Distinct units consume existing supported equipment and remain trainable after lawful unlock |
| Lotus subunit | Organization/recovery modifiers, support compatibility, recruitment unlock ownership | High cohesion is bounded and does not bypass armor, supply, casualty, or technology mechanics |
| Liberation Brigade | Infantry and support dependencies, professional conversion path | No inaccessible dead-end unit and no duplicate unit created during conversion |
| Air-defense focus | Current aircraft tree, DLC airframe variants, actual research-bonus categories | A valid bounded research benefit and no guessed technology ID |
| Maritime protection | Current naval tree, escort and convoy consumers, coastline and port requirements | No landlocked fleet or nonexistent equipment dependency |
| Medical-service project | Existing support or training modifiers and their actual scope | A concrete supported benefit, not a fictional global healing statistic |
| Civil-war knowledge inheritance | Parent technologies, doctrines, facilities, scientists, startup setup | Knowledge is inherited appropriately, material and research slots are not multiplied |
| Manual setup | Declared scenario tech state versus current campaign | Preserve actual researched progression, no silent advanced technology grant |

Run `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` before and after technology, unit-unlock, or doctrine-related changes. Inspect the installed and repository versions, not remembered vanilla identifiers. A full playable-country audit must cover research slots, techs, doctrines, facilities, any scientists, usable unit templates, and complete startup grants. The planning package does not claim these graph tools were run.

## DLC and supported fallbacks

Core political play must function without an intelligence DLC. Where native operatives or agency operations are unavailable, use an abstract political investigation case with the same bounded public consequence and no fabricated operative slot. Role-specific character effects require actual supported role consumers. Advanced aircraft or naval designer content uses the installed route rather than a hardcoded universal DLC assumption.

A capability fallback must preserve the political objective and be visible in the coverage report. It may not silently substitute a global country modifier for a carefully limited elite unit ability. Unsupported model actions, tags, equipment categories, or character scopes are blockers until an equivalent is explicitly selected and documented.
