# Part 4: Decisions, integration, and formables

## Decision surface

The main category uses a compact status header for National Momentum and Imperial Administration. It exposes only the current phase's most relevant actions. Normal phases should show three to five primary actions and no more than three active missions.

Target-heavy territorial actions use the project's selected-target pattern so the player inspects one foreign target at a time while AI can evaluate all valid targets.

## Territorial pressure families

Bulgaria selects one current owner and one claimed region, then chooses a method that fits its government, strength, supply, and diplomatic situation.
The existing demand, negotiation, border-pressure, local-organization support, war-preparation, protectorate, and intervention actions are organized around three consequences rather than shown as interchangeable war-goal buttons.

| Approach | Usable situation and commitment | Success | Refusal or failure |
| --- | --- | --- | --- |
| Negotiated revision or transit | The owner can accept a viable settlement; pay political power and temporarily commit civilian factories during negotiations, with a supplied frontier or established relations as requirements. | Agreed ownership moves the region into normal integration. Transit preserves the other state's sovereignty and provides access rather than core or formation proof. | Refusal spends the completed diplomatic effort and reveals the target's commitments; Bulgaria may consolidate or use a later backed demand. No instant war is required. |
| Backed ultimatum or limited campaign | Bulgaria has a supplied reachable front and real ready forces; commit equipment and fuel, plus conservative command power when the action uses military preparation. | A concession gives only the agreed territory; a war uses the actual result. A bounded objective preserves Momentum more effectively than prolonging unrelated fronts. | A failed demand or stalled objective reduces Momentum and exposes the opportunity cost of the mobilized frontier. An unwinnable wider faction war remains avoidable through withdrawal or settlement. |
| Protectorate agreement or intervention | The selected political route permits a layered order, or Bulgaria has a valid role in a current regional war; pay political power and provide a real equipment or transport contribution. | A protectorate remains a distinct governed country and only designated outer formation groups can count through that loyal subject. Intervention attaches the claim to the current war without automatically making a belligerent into a subject. | Refusal leaves the target independent; partner revolt, loss of the route, or collapse suspends its qualifying proof. Changing a partner's label cannot create direct Bulgarian cores. |

Border incidents and support for local Bulgarian organizations retain their own preparation roles within these approaches.
Organization support needs the existing historical and political basis in the target region, costs political power and real local material support, and strengthens negotiation or pressure without manufacturing territorial control.
A border incident commits frontier equipment and fuel, risks reciprocal mobilization, and can make a backed demand credible; it cannot bypass the legal hostile-pair and current-war checks.

Use only the costs relevant to the selected method, with at most four spendable types.
Political power is paid once; civilian factories remain committed for the action's duration and are released when its project ends.
Presence of ready divisions, state control, diplomatic access, and a functioning route are requirements rather than hidden additional payments.
Government direction changes which method is easier to sustain: military rule favors rapid backed pressure, central administration favors negotiated direct incorporation, and federation favors preserved local government.
Royal rule can use direct or client arrangements under its existing branch rules.
A target changing owner, entering Bulgaria's faction, or becoming a subject requires revalidation before an offer resolves.

When the same target group is part of an active Third Balkan War, use the [Event 045 settlement contract](../../045_third_balkan_war_specs/specs/045_third_balkan_war_spec_part_4_claims_settlement_connections.md).
The player sees ownership, transit, subject terms, and any formal waiver before agreement.
A settlement that preserves peace can leave Greater Bulgaria incomplete; refusing it preserves the ambition while exposing the supplied army and Momentum to further war.
This connection neither starts Event 045 nor grants its progression.
Without that event, the same ordinary Bulgarian methods remain available.

## Integration loop

A controlled claim does not become a core automatically.
Each target group retains the four administrative states: occupied, pacified, integrating, integrated.
Control time, current control, compliance, resistance, stability, garrison capacity, route condition, and Imperial Administration explain readiness; a high national value alone does not prove completed local work.
The player sees the missing local condition rather than a formula ledger.

The existing transport, municipal, security, and autonomy projects support a practical choice between rapid occupation, durable direct incorporation, and preserved local government.

- Military-first pacification requires supplied security forces in the region and commits support equipment or trucks. It can make a threatened region usable sooner, but extractive occupation weakens distant administration and does not complete core integration.
- Civil administration temporarily commits civilian factories and consumes transport equipment to restore the named connection, fund municipal administration, standardize laws, and keep local services operating. Reconstruction and local industrial programs retain their normal focus and project links. It is slower and competes with the short-term arsenal route, but supplies the work proof for direct incorporation.
- Negotiated autonomy uses the route's existing local-elite or protectorate agreement and costs political power and temporarily commits civilian factories to administration. It reduces the immediate governing burden while preserving local government, so it may qualify a designated outer subject group but not a central direct-core requirement. Later incorporation uses the normal project and cannot reuse the agreement as completed work.

Political routes shape these methods without adding another set of currencies or a separate integration screen.
The common price of overexpansion is that new fronts compete with projects that turn earlier victories into lasting strength.
Bulgaria can choose the next conquest instead of reconstruction, but Administration and the real garrison/supply position constrain what it can retain.
AI should consolidate a controlled high-value group when another campaign would exhaust the same transport and equipment; a federation AI should preserve an eligible partner instead of buying the direct-incorporation path under another name.

## Integration missions

Important regions use timed objectives rather than passive stockpile gates.
A project names the region, one necessary corridor or transport restoration objective, and the supplied security or civilian-service condition it must maintain.
Use the existing project duration and readiness tuning with terrain, resistance, damage, and distance as factors; do not require the player to monitor a third progress currency.

Successful completion moves that region forward once and can improve Imperial Administration.
Failure identifies the lost control, interrupted route, or deteriorating local condition and preserves only work that the owner can still prove; it cannot finish in enemy-held territory.
A reconquest may resume bounded previous work after revalidation, without a second success reward.
Partial administrative recovery can improve current capacity but cannot count the same completed region again as a new conquest or produce a core before its local proof is complete.

## Formable 1: Greater Bulgaria

Greater Bulgaria requires the central Greater Bulgaria territorial group to be owned and controlled, with a meaningful share integrated. Subjects do not automatically satisfy direct-core requirements, though the federation route can satisfy designated outer groups through loyal protectorates.

Formation grants a new cosmetic identity and flag, a substantial but bounded power increase, improved integration tools, and new post-formation focuses and decisions.

## Formable 2: Bulgarian Empire

Requires Evolution II, Greater Bulgaria or equivalent territorial proof, broader Balkan dominance, sufficient Imperial Administration, and completion of a valid imperial political settlement.

The formation can tolerate a mix of directly held territory and designated loyal subjects when the political route explicitly supports that order.

## Formable 3: Old Great Bulgaria

Requires Evolution III, a secure Balkan homeland, Black Sea access, the northern Black Sea core group, and enough surrounding steppe or maritime strategic points to prove a real regional sphere.

The formation uses an exact state-puzzle presentation once final state IDs are locked. The puzzle should show required state shapes in their real geographic positions, with clear controlled and missing states.

The final proclamation grants the final cosmetic identity and flag, stronger integration tools for the eastern sphere, a Black Sea military package, and the event's major final power spike.

## Exploit controls

- One-time formation rewards are flagged and cannot be repeated through tag or cosmetic changes.
- Equipment and unit grants are not repeatable decision farms.
- Integration cannot be started on land Bulgaria neither controls nor administers through an accepted subject route.
- Losing a region pauses or reverses integration rather than allowing completion while occupied by an enemy.
- A subject route cannot satisfy every direct-control requirement for free.
- Current-owner targeting prevents dead historical tags from blocking the system.
