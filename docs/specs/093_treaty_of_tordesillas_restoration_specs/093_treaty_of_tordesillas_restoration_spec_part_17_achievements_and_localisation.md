# Treaty of Tordesillas Restoration: achievements and writing direction


## Achievement rules

These are custom mod achievement specifications, not a claim about Steam achievement eligibility.
Internal IDs are stable planning identifiers.
Titles, descriptions, and flavor copy are directions for the localization workflow, not finished player-facing strings.

Each achievement requires a meaningful sequence and actual world state.
Opening a panel, signing one agreement, reaching an evolution threshold, or merely being alive when another country succeeds is insufficient.
Debug, forced-test, and invalid-event runs follow the project's achievement exclusion rules.

Tracking must distinguish the original participant, a verified successor, a repeated action, and a state that was already a core.
Changing a cosmetic name or reloading the save cannot reset disqualifiers.
An earned achievement is recorded once through the existing system.

## ACH-093-01: the earned Galician settlement

**Internal ID:** `chaosx_093_earned_galician_settlement`.

Eligible country: Portugal or its verified national successor.
Visible.
Hard.
Title direction: the contrast between useful wartime help and a territorial promise actually kept.

The player must sign a valid Galicia-for-aid contract during a live Spanish civil war, deliver 100 percent of every signed standard component through credited real assistance, support the side that wins, receive Galicia through the honored agreement, and retain peaceful ownership and control for 180 days.
Portugal must not have declared war on that recipient or supported its prohibited civil-war enemy during the contract.

This is not awarded for a peacetime sale, a console transfer, a treaty war conquest, or a promise fulfilled only on paper.
A recipient that loses and later reappears does not count without a verified continuity and the original valid victory outcome.

Track the contract identity, recipient continuity, delivery receipts, exact settlement route, recognized Galician states, aggression disqualifier, and continuous holding period.
Icon direction: an aid crate and a signed territorial document, with the actual Galicia shape used only after map verification.

## ACH-093-02: sovereign partners

**Internal ID:** `chaosx_093_sovereign_partners`.

Eligible country: Spain or its verified national successor.
Visible.
Hard.
Title direction: retaining Galicia while building a genuine equal partnership.

Spain must keep Galicia through a recognized Portuguese renunciation or border agreement, ratify the restored treaty without having made Portugal a subject, maintain Confidence of at least 65 for 180 days, and reach Evolution III while both countries complete at least two genuine Event 093 regional integrations outside the protected homeland and Galicia.

Disqualify a forced territorial reversal, a repudiated earned Galicia bargain that remains unresolved, subjecting Portugal, and regions whose cores were already present before the purported project.
A high opinion value alone does not satisfy the relationship condition.

Track the settlement route, independent treaty-power status, each partner's unique completed eligible regions, and the continuous Confidence period.
Icon direction: two distinct seals on one agreement with a secure border, avoiding a fused national flag.

## ACH-093-03: reciprocal restitution

**Internal ID:** `chaosx_093_reciprocal_restitution`.

Eligible country: either treaty power.
Visible.
Very hard.
Title direction: accepting that a successful conquest belongs on the other side of the treaty.

Both crowns must voluntarily hand over legally owned, non-core, wrong-sphere conquests under the treaty.
Each must transfer at least two distinct coherent regional groups, with the handed-over states totaling at least 10 percent of the receiving crown's frozen sphere weight.
Those states must have been acquired from outside the treaty order, not passed back and forth between partners.

The player must participate as a donor and maintain the treaty without an unresolved restitution breach for 180 days after the final qualifying handover.
A transfer from a puppet without a valid settlement, enemy-owned occupation, repeated circulation of the same state, and the protected Galician exception do not qualify.

Track original outside acquisition, donor ownership, receiving sphere, actual transferred state identities, weight credited once, reciprocal partner participation, and the clean period.
Icon direction: two distinct map sectors exchanged across a clear divider, with no currency-store imagery.

## ACH-093-04: two administrations

**Internal ID:** `chaosx_093_two_administrations`.

Eligible country: either treaty power.
Visible.
Very hard.
Title direction: the administrative work behind the two imperial claims.

Each crown must complete at least three Event 093 regional integration projects outside its protected homeland and Galicia.
At least one project per crown must use the large tier.
The completed regions must remain directly owned, controlled, and cored by the proper crown for 180 days after the final qualifying project, while both remain independent treaty partners.

Disqualify empty projects, cancelled projects, native cores that existed before admission, grants made only by another event, and repeated integration of the same states.
The achievement checks both countries, so a player cannot finish it by ignoring the partner.

Track unique project completion, admission tier, previously non-core enrolled states, actual core outcomes, correct sphere, and continuous control.
Icon direction: paired administrative dossiers and regional maps, rather than two generic crowns without a gameplay reference.

## ACH-093-05: the completed partition

**Internal ID:** `chaosx_093_completed_partition`.

Eligible country: either treaty power.
Visible.
Extreme.
Title direction: the user-established idea of two crowns completing one world, with final wording researched and differentiated from the super-event heading.

Complete the actual world-end victory in Part 09.
Both powers must remain sovereign and meet the final 60-percent direct-integration requirement.
All eligible territory must have its proper political settlement, and the final state must hold for 90 days.
Triggering the world-end is insufficient.

Disqualify annexing or puppeting the other crown, an unresolved wrong-sphere subject arrangement, independent associates counted as conquered, and a victory forced only by debug operations.
The final shared scenario completion record and both country conditions must agree.

Track the scenario's unique activation and completion, participant continuity, final political coverage, integration shares, exceptions, and stability period.
Icon direction: a world divided into two clearly separate orders, preserving the dual structure.

## ACH-093-06: defended independence

**Internal ID:** `chaosx_093_defended_independence`.

Eligible country: an independent country that was neither treaty power nor a treaty subject when the world-end began.
Hidden until the scenario is encountered.
Extreme.
Title direction: a country refusing its assigned place in an imperial map.

The player must reject or actively resist the treaty order, remain independent, and directly recover or restore independent ownership of states amounting to at least 10 percent of one crown's frozen sphere weight that were under that crown's order at scenario entry.
Those states must be recovered through recorded player participation, not through an unrelated collapse elsewhere.

The treaty world-end must then fail, and the player must remain independent for a further 180 days.
Merely watching a distant ally defeat Portugal is insufficient.
A release or peace settlement can qualify when the player's actual ownership, control, or recorded settlement authority proves the recovery.

Disqualify joining the treaty as a subject to manufacture an easy release, tag switching to a former crown, circulating the same restored states for repeated credit, and debug-only collapse.
Track scenario-entry status, explicit opposition, original occupied states, unique recoveries with valid attribution, failure outcome, and survival period.

The exact attribution route must be proven in the installed game before this achievement is enabled.
If it cannot be observed safely, the achievement remains blocked rather than quietly granting credit on global failure alone.
Icon direction: a sovereign seal or intact border breaking an imposed map line.

## Achievement assets

All six achievements require the complete 64-by-64 completed, grey, and not-eligible-overlay states from the project's approved immutable template workflow.
Each role has a distinct composition.
Eligibility is not communicated solely by changing a hue.

The final artwork needs exact template integrity, layer provenance, approved conversion, strict runtime DDS checks, and real consumer wiring.

## Localization structure

The opening reports must identify who is demanding, who owns Galicia, who controls it, and whether the proposed agreement is immediate or conditional.
A civil-war message identifies the live recipient rather than assuming a fixed Spanish ideology or leader.

A settlement message distinguishes acceptance, compensated transfer, recognition, earned repudiation, unearned renegotiation, and defeat of the contracted side.
Those are different outcomes and must not reuse a sentence that describes one as another.
The legacy empty report descriptions need complete replacement during implementation.

Treaty descriptions must separate the faction's name, the two treaty powers, and ordinary members.
They must not call a republic a monarchy because the world-end metaphor mentions crowns.
Country names and pronouns must remain correct after legitimate succession or cosmetic changes.

## Writing and humor

Use confident but precise diplomatic language.
The event can be dryly funny when officials treat a disputed province as the first step in allocating every ocean and capital.
Avoid making every sentence an exaggerated proclamation.
The scale of the actions supplies the escalation.

Keep narration distinct from propaganda.
The treaty powers may describe annexation as integration or historical entitlement.
The factual result must still say whether a country loses independence, who receives territory, and what happens to its government.

No fabricated quotation, slogan, cultural saying, or historical royal statement is supplied here.
Final player-facing titles, buttons, descriptions, and remarks are written only after their direction and sources are checked.
The original event name, faction name, evolution names, and world-end name supplied by the user remain authoritative.
