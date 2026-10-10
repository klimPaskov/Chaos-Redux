# Event 027: Doctrine Research acceptance criteria

## How to read this file

These criteria cover behaviour that could realistically fail or hide a simplification.
`[x]` means present in source, `[ ]` means pending, and *(live)* marks a criterion whose source exists but depends on engine behaviour the user confirms in a live session.
General completion, reporting, localisation, and catalog-export rules come from `CLAUDE.md` and are not repeated here.

## Identity and firing

- [x] `chaosx.nr27.1` is the console bridge; ordinary dispatch calls the firing transaction directly and records one actorless History row per firing.
- [x] Event 027 is Minor Repeatable, Calm World, enabled in the default reworked-event list, and named Doctrine Research on every log surface.
- [x] Choice pages and AI resolution add no History rows.
- [x] Every live country with a doctrine system and a valid action receives one curriculum; a damaged ledger is repaired without compensation before it is skipped.
- [x] Countries created after a firing receive nothing; removed countries lose unused choices without transfer.
- [x] Nonhuman countries without a doctrine system receive nothing; Kruger sovereignties keep their graph.

## Choice rules

- [x] A domain without a Grand Doctrine offers every eligible Grand Doctrine; adoption spends one choice, grants no step, and never replaces a doctrine.
- [x] A held subdoctrine advances exactly one level per choice. *(live: same-effect readback)*
- [x] An empty track assigns one subdoctrine and grants its first step in the same choice. *(live: assignment and bank readback)*
- [x] A bank that completes the branch on assignment leaves it assigned and spends nothing.
- [x] Navigation, pagination, and invalidated targets spend nothing.
- [x] The doctrine cost of the chosen action is waived; nothing is refunded or compensated.
- [x] One step never crosses two levels, including with negative mastery gain factors. *(live: whether `add_mastery` applies gain factors)*

## Domains

- [x] Army, Navy, Air, Special Forces, and Chaos Warfare adapters exist; future custom domains stay disabled until a full adapter is registered.
- [x] Army and Chaos Warfare never offer actions on the same `land` folder at once.
- [x] Special Forces stays available while both tracks are occupied. *(live: no duplicate subdoctrine across tracks)*
- [x] Chaos Warfare adoption requires the owning establishment gate, and its steps run the native reward effects.
- [x] No invalid identity reaches a mastery trigger or effect, and a broken custom adapter cannot remove ordinary domains.
- [x] Every visible option uses a native doctrine icon.
- [x] The `<doctrine>_mastery_gain_factor` tokens read through `modifier@` are pre-registered. *(live: fresh `error.log` without those token lines)*

## Evolutions

- [x] Curricula hold 1, 2, 3, 4, and 5 choices from baseline to Evolution IV.
- [x] The first firing opens at the highest eligible stage; later stages promote about 90 days after eligibility, one at a time.
- [x] A curriculum's size never changes after creation, and an evolution never grants an immediate curriculum.
- [x] Each stage honours its own enabled setting; a disabled Event 027 promotes nothing.
- [x] Evolution rows are actorless and state the correct choice counts.

## Queue and persistence

- [x] Later firings append separate curricula; closed rows are compacted.
- [x] One-time receipts prevent duplicate effects. *(live: save and reload recovery)*
- [x] Controller changes route remaining choices to the current controller exactly once. *(live: tag-switch callbacks)*
- [x] Annexation discards every curriculum and receipt of the annexed country.

## Human flow

- [x] Every page shows the remaining choices, every consuming option states its result, and navigation reads as navigation.
- [x] Every valid option is reachable through native-order pagination.
- [x] Confirmation revalidates, and an open page cannot confirm for a country that lost its doctrine system.
- [ ] R1: the opening report carries the first domain menu.
- [ ] R2: an assigned track advances from the track menu without the subdoctrine page and confirmation.
- [ ] R3: the result page continues the curriculum, offers "advance the same branch again", and shows the summary after the last choice.
- [ ] R4: the Chaos Warfare adoption confirmation states its civilian-death cost.
- [ ] R5: the general staff option resolves the remaining choices with the AI resolver and is the first option, so an unanswered page delegates instead of cascading. *(live: which option the engine picks on timeout)*
- [ ] R6: the summary lists outcomes and Milestones instead of counters.
- [ ] R7: domain and track options show only the values in part 4's Visible values table.

## AI

- [x] The AI uses the human validity pool, rescores after every choice, and never selects an invalid candidate.
- [x] Domain scores follow domain-owned capability, including the landlocked maritime plan and air-led industry.
- [x] Grand Doctrine and subdoctrine scores apply the vanilla `ai_will_do` factors.
- [x] Track and subdoctrine scores are squared sums of fit, investment, completion, empty-track value, and continuity; completion without fit never wins on its own.
- [x] Groups A to D have recorded evidence after the last weight change, except the zero-reset subdoctrine change.
- [ ] Group E has a bound multi-choice timeline.
- [ ] Group F has complete-pool recurrence evidence, and DR-F04 has a second cluster member to test against.
- [ ] Real-campaign AI mixes and branch completion rates. *(live)*

## Cluster

- [x] Cluster 9 National Breakthroughs holds row 9001 for Event 027, optional, Medium, Calm World, with a 120-day cooldown.
- [x] One cluster firing calls the Event 027 fanout once and grants no extra choices.
- [ ] Participation tuning with the complete member pool once a second member is implemented.

## Achievements

- [x] First Lesson, Single School, and Joint Curriculum are registered with titles, descriptions, tracking, disqualifiers, and complete icon triplets.
- [x] Only consumed receipts of the active or closing curriculum count, and forced, console, cluster-forced, debug, and test-country setups are excluded.
- [x] Joint Curriculum counts Special Forces progress per subdoctrine.

## Presentation and documentation

- [x] The report image and achievement icons are final, wired, and documented in `docs/assets/027_doctrine_research/`.
- [x] Event Details, History payloads, and evolution previews state the correct choice counts without raw state.
- [x] `docs/events/027_doctrine_research/overview.md` describes the implemented behaviour.
- [ ] The queued workbook status change in `catalog_changes_pending.md` is applied and the CSVs re-exported.
- [ ] After R1 to R7, the overview, localisation, and catalog wording follow the new flow.
