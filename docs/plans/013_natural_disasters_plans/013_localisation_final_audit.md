# Event 013 Natural Disasters localisation final audit

> Disposition, 2026-07-10: superseded by `013_localisation_final_reaudit_2026-07-10.md`, which records the corrected package at 0 P0, 0 P1, and 0 P2. The findings below are retained as the pre-correction audit trail.

> Historical audit only: the non-final verdict and findings below are superseded. Do not use this file as the current localisation status; use `013_localisation_final_reaudit_2026-07-10.md` and the final Event 013 completion audit.

Audit date: 2026-07-10

Audit mode: read-only static review of the accepted Event 013 specification, live script references, English localisation, scripted localisation, event-log routing, scenario and cluster text, achievements, scripted GUI text, and custom decision costs.

## Historical verdict

Event 013 is not localisation-final.

The key set is complete and structurally healthy. The audit found no P0 key, encoding, duplicate-key, or scope-syntax failure. It did find five P1 player-facing correctness or completion blockers and four P2 wording or presentation defects.

Priority meanings used here:

- **P0:** localisation cannot resolve, is missing, is duplicated, or is structurally broken.
- **P1:** visible text is materially misleading, hides required live state, violates an accepted Event 013 presentation gate, or lacks the required research handoff.
- **P2:** visible text works but retains implementation language, stale wording, or repository-style violations.

## P0 findings

None.

## P1 findings

### P1-01: The aftermath card and abnormal GUI discard the funded warning action's identity

The warning catalogue has 75 distinct actions, but the displayed result collapses every family to one of three implementation-order labels:

- `natural_disaster.warning_result.primary`: "the first family warning direction was funded"
- `natural_disaster.warning_result.secondary`: "the second family warning direction was funded"
- `natural_disaster.warning_result.tertiary`: "the third family warning direction was funded"

Evidence:

- The three generic result keys are at `localisation/english/013_natural_disasters_l_english.yml:313-315`.
- `GetNaturalDisasterWarningResult` routes only by primary, secondary, or tertiary at `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt:657-674`.
- The generic result is shown on the aftermath card at `localisation/english/013_natural_disasters_l_english.yml:312` and in the abnormal GUI at line 386.

Impact: a player who funded "Open the Squares", "Post the Port-Withdrawal Watch", or any of the other 73 specific actions is later told only that the first, second, or third direction was funded. This is working-taxonomy language, and it breaks the accepted requirement that warning and aftermath presentation remain family-specific.

Required correction: route warning results by family plus chosen direction, or persist a dedicated action-result value. The card and GUI should name the physical action or its concrete protection, not its ordinal position in the family specification.

### P1-02: Persistent missions do not name the state they are tracking

The four rescue slots, three stabilization slots, three reconstruction slots, chain mission, and inbound-relief mission are country missions tied to stored state variables. Their names and descriptions use "first priority state", "second state", "tracked state", or "recorded state" instead of the actual state name. Inbound relief also omits the recorded donor.

Evidence:

- Mission text is at `localisation/english/013_natural_disasters_l_english.yml:528-563`.
- Rescue state variables are assigned at `common/scripted_effects/013_natural_disasters_effects.txt:3184-3208`.
- Stabilization state variables are assigned at lines 3221-3237, reconstruction state variables at lines 3250-3266, and the chain state at line 3751.
- Inbound relief stores both donor and target state, for example at `common/decisions/013_natural_disasters_decisions.txt:6924-6933`.

Impact: the mission list can show several simultaneous deadlines without telling the player which named state each deadline governs. The implementation already retains the necessary scope pointers, so this is a localisation omission rather than missing gameplay data.

Required correction: include the applicable variable scope in each mission name or description, for example the stored rescue, stabilization, reconstruction, chain, or inbound-relief state. The inbound-relief presentation should also name the donor when that variable exists.

### P1-03: Cost presentation does not match the full availability gate

All 14 custom cost-text families present numeric resource amounts as the action cost, but the action gates generally require strictly more than the displayed amount. Several gates also impose an undisclosed reserve threshold.

Evidence:

- The shared affordability triggers use strict `>` checks for manpower and equipment at `common/scripted_triggers/013_natural_disasters_triggers.txt:283-336`.
- Fixed-fuel checks in the individual decisions also use strict `>`, beginning at `common/decisions/013_natural_disasters_decisions.txt:82-84` and recurring across the costed actions.
- Warning transport and rescue additionally require fuel ratio above 2 percent through `natural_disaster_factor.minimum_fuel_ratio`, while their cost text presents only the fixed fuel deduction. The trigger is at `common/scripted_triggers/013_natural_disasters_triggers.txt:290-310`, and the constant is at `common/script_constants/013_natural_disasters_constants.txt:448`.
- Shelter text says "at least 10% Stability" at `localisation/english/013_natural_disasters_l_english.yml:680`, but the trigger requires stability strictly greater than 10 percent at `common/scripted_triggers/013_natural_disasters_triggers.txt:300-303`.
- Reconstruction requires stability above 5 percent at `common/scripted_triggers/013_natural_disasters_triggers.txt:321-329`, but the reconstruction cost text at `localisation/english/013_natural_disasters_l_english.yml:702-710` discloses only the 2 percent deduction.

Impact: a country holding exactly the displayed manpower, equipment, train, convoy, or fuel amount can still be blocked. Low-fuel-ratio and low-stability countries can also be blocked by requirements that the displayed cost does not explain. This affects the 108 decisions that use custom Event 013 cost text.

Required correction: make affordability checks inclusive with the supported long comparison form where exact payment is intended, or explicitly disclose a deliberate reserve requirement. The displayed 10 percent shelter threshold must use the same boundary as the trigger.

### P1-04: Event Details and related catalogue text expose mechanics and log architecture

The accepted Event Details direction is to describe the premise and visible situation, not a mechanical effect list. The live entry instead enumerates warnings, deaths, damaged buildings, supply disruption, follow-up hazards, and recovery state, then calls their storage a "season record".

Evidence:

- The accepted rule is explicit in `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_1_core.md:137` and `docs/specs/013_natural_disasters_specs/implementation_readiness/013_source_to_file_surface_map.md:32`.
- The live Event Details text is at `localisation/english/013_natural_disasters_l_english.yml:332`.
- The evolution summary says "future Event 013 seasons" and "extra history rows" at line 340.
- The Natural Disasters cluster description says "Event 013 seasons" and "Event 013 history row" at `localisation/english/chaosx_gui_l_english.yml:370`.

Impact: these entries describe implementation and event-log bookkeeping rather than the current world state. They also make the Event Details surface read like a compact mechanics note, which is the presentation mode the accepted source map rejects.

Required correction: rewrite the Event Details, evolution summary, and cluster description as world-facing prose about local reports, widening regional crises, and abnormal moving paths. Do not mention internal event numbers, history rows, records, or storage behavior.

### P1-05: Super-event slots 69 and 70 use recycled ordinary-event buttons instead of the researched cultural directions

All six Event 013 super-event roles have complete title, quote, remark, and description keys. Slots 69 and 70, however, do not preserve the cultural remark directions documented by the research handoff, and no final-selection note explains an alternate sourced choice.

Evidence:

- The meteor-impact research proposes "Who is able to stand?" at `docs/super_events/013_natural_disasters/archive/text_research.md:200-204`.
- The storm-corridor research proposes "Here's a night pities neither wise men nor fools." at lines 268-277.
- Live slot 69 uses "Mark every fall." at `localisation/english/013_natural_disasters_l_english.yml:351`. This is shortened from the ordinary meteor-shower report button at line 132.
- Live slot 70 uses "The path is still moving." at line 355. The same line is the ordinary storm-corridor news button at line 153.

Impact: two researched presentation roles fall back to report and news acknowledgements rather than a verified cultural remark. That does not satisfy the Event 013 super-event research gate.

Required correction: select and document a research-backed remark for each role. The researched candidates may be edited by the final writer, but any replacement needs equivalent source, context, rights, and selection evidence.

## P2 findings

### P2-01: Reconstruction cost tooltips present an existing mission burden as a new action cost

The three reconstruction tooltips say the action uses "construction capacity" at `localisation/english/013_natural_disasters_l_english.yml:704`, line 707, and line 710. The reconstruction action effects deduct support equipment, trucks, train or convoy capacity, fuel, and stability. They do not add a construction burden. The country already carries the reconstruction mission's heavy consumer-goods modifier, for example at `common/decisions/013_natural_disasters_decisions.txt:5800-5803`.

Required correction: either remove "and construction capacity" from the per-action cost tooltip, or describe it separately as the continuing reconstruction-mission burden.

### P2-02: The abnormal GUI and scenario text retain implementation vocabulary

Examples:

- "Event 013", "Evolution III", and "does not waive costs or complete missions" at `localisation/english/013_natural_disasters_l_english.yml:370`.
- `EVENT 013` in the GUI title at line 372.
- "animated frame sheets", "static accessibility fallbacks", and "frame-sheet motion" at lines 397-402.
- "live Event 013" and "Evolution III disaster cards" at line 406.
- "The barrage remains non-terminal" at `localisation/english/chaosx_gui_l_english.yml:139`.

These strings should describe what the player sees, such as moving paths, a reduced-motion display, severe abnormal seasons, and the states at risk. They should not expose asset construction, event identifiers, implementation guarantees, or design classification.

### P2-03: Event 013 localisation violates the event writing punctuation standard

`localisation/english/013_natural_disasters_l_english.yml` contains 23 em-dash lines and seven semicolon lines. The event-writing standard rejects em dashes in sentences and asks for direct sentences rather than semicolon-linked clauses.

Concentrated examples include the card and GUI separators at lines 304, 311-312, and 375-384, evolution titles at lines 334-338, quote attribution at lines 342-362, and semicolon-linked player instructions at lines 332, 370, 408, 491, 529, and 543.

The delayed-tsunami description at line 364 also uses the prohibited dialectical construction "This is not a single wave: each...".

Required correction: replace em dashes with colons, commas, parentheses, or line breaks as appropriate. Split semicolon clauses into direct sentences, and state the tsunami condition affirmatively.

### P2-04: Two orphaned entry-event keys retain generic legacy wording

`chaosx.13.t` and `chaosx.13.d` at `localisation/english/013_natural_disasters_l_english.yml:2-3` are not referenced by the live Event 013 event file. The canonical entry is hidden `chaosx.nr13.1` and has no title or description reference at `events/013_natural_disasters.txt:11-42`.

The description, "A season of specific disasters, delayed impacts, and contested recovery", is also generic specification language.

Required correction: remove the orphaned keys if they have no external consumer, or document and rewrite them if another registration surface intentionally consumes them.

## Coverage and integrity results

| Surface | Result | Evidence summary |
| --- | --- | --- |
| Referenced localisation keys | Pass | 727 Event 013 implementation-referenced keys checked, zero missing and zero duplicated across `localisation/english/*.yml`. |
| Encoding | Pass | UTF-8 BOM present on `013_natural_disasters_l_english.yml`, `chaosx_achievements_l_english.yml`, `chaosx_gui_l_english.yml`, and `chaosx_event_names_l_english.yml`. |
| Decision names and descriptions | Pass | All 130 decision or mission ids in `common/decisions/013_natural_disasters_decisions.txt` have exact name and `_desc` keys. |
| Warning catalogue | Pass | Exactly 75 warning ids, three for each of 25 families. All 75 names and all 75 descriptions exist and are unique, and every description gives a concrete physical action in a named state. No generic Action A, B, or C label was found. |
| Reports and news | Pass | Event 4 plus 25 affected-country reports and 25 news events have all 153 title, description, and option keys. Family and state wording is distinct. |
| Dynamic state scopes | Pass with P1 content omission | Report, news, and abnormal-notice event targets are saved before their immediate events. Event-target namespace syntax, state-target `[FROM.GetName]`, scoped variables, GUI arrays, and date getters match supported localisation forms. Mission target data exists but is not displayed, as recorded in P1-02. |
| Aftermath card | Pass with P1 warning defect | Family, severity, state, linked state, deaths, damage, disruption, recovery, follow-up, cleanup, and reassessment fields are wired. The warning result loses action identity, as recorded in P1-01. |
| Scripted GUI | Pass | All 25 direct GUI text, button-text, and tooltip references resolve. Dynamic path-queue and selected-state keys also resolve. |
| Custom costs | Pass with P1 and P2 defects | All 14 base, blocked, and tooltip key families exist. Numeric deductions align with the shared constants and payment effects. Availability boundaries and reserve requirements differ from presentation, and reconstruction mislabels the mission burden. |
| Achievements | Pass | Ten achievement ids have `_NAME`, `_DESC`, and custom requirement tooltip keys. The tooltip wording matches the implemented completion and disqualifier conditions by static review. |
| Super-events | Pass with P1 research defect | Slots 67-72 each have `.t`, `.q`, `.a`, and `.d` keys and scripted-localisation routes. Slots 69 and 70 fail the final cultural-remark handoff described in P1-05. |
| Event log and evolutions | Pass with P1 wording defect | Event name, history name, Event Details, three evolution titles and bodies, selected evolution summary, and cluster selectors resolve. The live prose exposes log architecture, as recorded in P1-04. |
| Scenario and cluster | Pass with wording defects | Disaster Barrage type, description, intensity, impact, and Natural Disasters cluster keys resolve. Maximum and cluster prose retain design or implementation language. |

## Required remediation order

1. Preserve and display the exact funded warning action or concrete protection.
2. Add dynamic state names to all persistent mission slots, plus donor identity to inbound relief.
3. Align cost availability boundaries and hidden reserve requirements with the cost presentation.
4. Rewrite Event Details, evolution summary, cluster description, abnormal GUI help, and Maximum scenario text as player-facing world state.
5. Finalize sourced cultural remarks for super-event slots 69 and 70.
6. Correct reconstruction burden wording, punctuation, and orphaned entry keys.

After those changes, rerun the exact-key, duplicate-key, cost, mission-scope, and super-event research comparisons. This audit made no gameplay or localisation edits.
