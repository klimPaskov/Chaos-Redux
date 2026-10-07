# Doctor Wu direct parent design review

## Evidence boundary

This is a direct review of the five authored Markdown specification parts. It is not a specialist subagent review, a probability-tool result, an HOI4 source implementation audit, or a live-game test. The scenarios below compare the proposed design with its stated requirements. Runtime and integration acceptance remain open.

## Document-level scenario review

| Scenario | Expected design result | Current finding |
| --- | --- | --- |
| A human-controlled major qualifies through both criteria | One country entry in the host pool | Part 1 explicitly deduplicates and proposes an equal country draw. Runtime selection is unimplemented. |
| A small human country has a working civilian region but little industry | It remains eligible and can retain a useful founding institute | Part 1 separates appointment from paid expansion and provides foreign production agreements through Part 4. |
| Every initial candidate refuses | Wu moves through untried candidates, then remains discoverable underground | Part 1 supplies a finite referral circuit and changed-circumstance rediscovery. |
| The first host is healthy | A contained proof occurs without a national epidemic or artificial containment reward | Parts 1 and 3 state this explicitly. |
| The host has active zombie infection | Living patients can recover while dead hordes and independent actors remain | Part 3 separates living infection, outbreak support, and established armies/countries. |
| The host has plague and an organized Rat Nation exists | Human treatment reduces compatible biological support without deleting the Rat Nation | Part 3 preserves the actor and its owner-defined political and military outcomes. |
| Every evolution is disabled and Authority is low | Medical and later compatible research remain possible under explicit supervision | Parts 2 and 5 make Authority a permission/control issue rather than a technology gate. Detailed advanced-family proof remains open. |
| A public host wants tissue and regenerative research without a military mandate | It has a civilian prerequisite route | Part 5 now explicitly permits M07 through M04, M05, or two validated cures. M04 supplies the civilian route. |
| A cure project encounters repeated setbacks | Verified progress survives and a finite conservative route remains available | Part 3 rejects unchanged endless success rerolls and separates clinical, material, and transport problems. |
| A treatment-relevant disease version changes | Compatibility is re-evaluated and adaptation is possible | Part 3 retains old stock identity and useful prior knowledge. Owner-specific timings are unverified. |
| The country possesses a cure but an overseas ally is blockaded | Knowledge remains complete while delivery is blocked | Part 4 offers local licensed production or a valid alternate route, without fake convoy delivery. |
| A small treated group occupies a large infected country | Only reached eligible living people receive the clinical effect | Parts 3 and 4 separate coverage from national ownership. The eventual stock granularity is an open implementation design choice. |
| One treatment receives passive institute support and a disease-specific cure | The same clinical effect is not counted twice | Part 3 selects the strongest applicable Wu measure per outcome and preserves owner combination rules. |
| The cabinet performs the same audit repeatedly | It cannot farm Authority reductions from a resolved dependency | Part 2 attaches reductions to actual concessions, violations, and removed dependencies. |
| A laboratory is captured after Wu was evacuated | The occupier gains only what actually remained | Part 2 separates person, site, staff, material, records, and host-local investment. |
| Wu leaves after treatments have been documented and shared | Existing trained institutions retain those results | Parts 2 and 4 preserve copied knowledge and actual stocks. Full death/continuity design remains open. |
| A public host later chooses classification | Existing patients and documented knowledge do not disappear | Part 2 provides an explicit transition, and Part 4 states that published knowledge cannot be recalled. |
| The host deliberately causes a disease and then treats it | Treatment can still help patients, while history remains and the action cannot become a reliable Chaos-reduction loop | Part 3 excludes artificial demonstration credit and requires episode-aware containment accounting. Event-wide numeric accounting is still open. |
| A new Wu appointment resolves while old Kruger tech-sharing callbacks still exist | No research-group acceptance is inferred from hiring Wu | The source register identifies the conflict. No code fix or migration has been performed. |
| A future Wu clone programme produces shared clone equipment | It cannot add a second manpower stream beside the shared stock consequence | The boundary is recorded. The user constraint and existing continuous reserve-manpower design still need a real shared-owner settlement. |

## Hypothetical calculations

These examples use the proposed design's numbers. They are arithmetic checks, not observed campaign outcomes or validated balance.

### Deduplicated host draw

Assume seven hypothetical major countries, four hypothetical player countries, and two countries in both groups. The union contains 7 + 4 − 2 = 9 countries. An equal country draw gives the player-controlled group a 4/9 chance, approximately 44.44 percent. It does not guarantee a human host, and a player major has the same individual 1/9 probability as every other eligible country.

### Research commitments

The common elective classes imply 60 civilian-factory-days for Routine, 240 for Substantial, and 540 for Exceptional work, before any justified preparation adjustment. Support equipment and political power remain the separate costs stated in Part 5.

Cure research intentionally uses faster medical-emergency durations with the same class resource types: 45, 180, and 450 civilian-factory-days for familiar, severe, and exceptional treatment development. Part 3 explicitly states that its durations supersede the elective defaults. This distinction was added during review to remove a timing ambiguity.

### Treatment production

Under the proposed basic production anchor, twenty civilian allocations require 600 civilian-factory-days and 1,000 support equipment. Four simultaneously committed civilian factories would complete that standard output in 150 days, assuming no interruption or other adjustment. The clinical coverage ceiling is twenty million eligible living people, not an automatic national cure.

A severe standard doubles that industrial and support-equipment requirement. An exceptional fictional standard quadruples it. These rates are intentionally visible proposals, and their practical balance remains untested. Treatment-version compatibility, route capacity, actual affected populations, and delivery still matter after the arithmetic.

### Cost and concurrency limits

The common research action has three spendable cost types. The field-medicine army-experience option replaces the political-power payment rather than adding a fourth hidden currency. Initial appointment has no affordability trap. Staff and material access that are only requirements are explicitly distinguished from actual payments.

The proposed institute supports one founding research lane, a paid second research lane, and one additional emergency response mission. Production is a standing commitment rather than a mission per batch. The final UI still needs a native phase audit to confirm that simultaneous research, delivery, and emergency contexts remain within the visible-action and mission limits.

## Changes made during this review

The medical prerequisite map was added to Part 5 so the public path to tissue and regenerative work does not depend on a military mandate or a vaguely named hidden clinical stage.

The cure resource packages were stated explicitly in Part 3, with a clear distinction between cure durations and elective-project durations.

The source register preserves the three major owner conflicts rather than hiding them in the design: old Event 089 technology-sharing semantics, the supplied cluster-name mismatch, and the existing clone reserve-manpower economy. It also records the newer Kruger biological-ledger amendment and its own incomplete validation state.

## Open review gates

The following work cannot be marked complete from this direct review: the nineteen unread supplied source files, full related-owner reads, the remaining advanced specifications, exact AI choice weights, MTTH probabilities, owner-specific medical effects, medical-stock implementation, old-save migration, catalogue updates, technology and unit-family integration, detailed UI phases, generated assets, model/audio coverage, and all applicable independent audits.

The mandatory independent improvement-loop planner has not run. Its eventual review must evaluate the completed event without inheriting a manufactured closure claim from this document. The same applies to the completion auditor and specialist probability, decision, country, focus, UI, localisation, portrait, asset, and production reviews.
