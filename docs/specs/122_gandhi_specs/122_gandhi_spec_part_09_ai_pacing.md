# Part 09. AI, pacing, regional conditions, and rare campaign variants

The AI must make the same political and material choices that the player sees. It can support sovereignty without joining the League, join the civic League without changing faction, develop national deterrence without accepting foreign launch command, or defeat the supreme mandate and preserve a reformed institution. No stage is an automatic upgrade paid for by waiting.

All weights, price anchors, durations, and variant conditions in this part are authored design values. They have not been measured in a live game. They are not claims about actual selection percentages. Action identifiers refer to Part 08. The other core parts own the exact opening, League, nuclear, and world-authority gates.

## 1. Legality before preference

An AI candidate must first pass the same existence, authority, scope, consent, payment, access, applicable mission-cap, lifecycle, and native-policy checks as a player action. Refusal, veto, cancellation, lawful exit, and free responses remain available when paid-work slots are full. Failed legality removes it from the selectable set. A favorable opinion, high Cohesion, authoritarian ideology, or very large score cannot restore an illegal choice.

The evaluation order is explicit.

1. Resolve the actual actor, target, country or state scope, proposal generation, and relevant owner. Reject expired or superseded terms.
2. Apply current terminal and lifecycle rules. New stage work stops when its evolution is disabled. Existing obligations receive their safe completion or exit route.
3. Check independent consent, current legal ownership or control, viable allocation, native faction and war rules, and player-continuation safety where relevant.
4. Check the full quote and actual reservation capacity. Existing paid projects and national survival requirements remain real constraints.
5. Check character location, access, current stock, research, delivery, national law, and exact retaliation facts for actions that need them.
6. Score the remaining candidates against current circumstances, including a meaningful decline, wait, compromise, or peaceful alternative.
7. Revalidate on commitment. A score generated yesterday does not authorize today's changed target or arsenal.

Human status, major status, ideology, and geographic location are never blanket eligibility filters for the global incident. A particular country's legal regime or actual state can change its treatment and strategy. Fascist occupation is the explicit mechanical exception from the brief, while charter admission still tests behavior and actual consent.

The AI must not pretend to know another country's hidden exact device count. It can use observed launches, inspections, owner disclosures, deployed delivery evidence, and its actual intelligence. An unverified arsenal is uncertain. It is not automatically zero and not automatically an unlimited nuclear threat. A knowingly unverified political claim under D59 has an initial relative preference of 2 against truthful negotiation at 18, modified by actual exposure risk. It never creates legal launch eligibility or a capability receipt. D61 doctrine choices use A7 for research and inspection, A8 for threats, and A9 for any proposed central command.

## 2. Relative scoring model

Use a small auditable relative-score vocabulary. A normal candidate starts at a profile-specific base. Strongly favorable conditions multiply by 2, modestly favorable by 1.5, modestly unfavorable by 0.5, and strongly unfavorable by 0.25. These are design anchors, not literal script instructions. Avoid stacking numerous redundant factors describing the same fact. Cap the final legal preference within a reviewed range, initially 1 to 200, so a single extreme factor does not erase all other lawful choices.

A genuinely unavailable action has no candidate and no positive weight. An action that is legal but undesirable can retain a small positive score when that matches the actor's real interests. Suicidal or internally impossible commitments should fail their substantive feasibility requirement rather than acquire a token random chance.

For event choices, compare the complete actual option set and the actual engine's weighting behavior. For decision selection, treat `ai_will_do` as a desirability score, not a percentage. The implemented scheduler, other available decisions, timing, and native AI behavior affect what happens. Tiny event weights may round away under the current source rules, and an all-zero set can select an unintended first option. Every authored choice set therefore retains a legal safe fallback such as decline, defer within the existing deadline, or preserve the current state. The default must not be a strike, annexation, or constitutional surrender.

### AI profile map

| Profile and actions | Initial relative bases | Factors that increase willingness | Factors that reduce willingness |
| --- | --- | --- | --- |
| A1, territorial settlement, D01 to D08 | Ready settlement 20, exact negotiation 18, refusal 15 | High denied economic footprint, war exhaustion, defensible recipient, retained core economy, agreed access | Vital supply or basing loss, unresolved living claimant, active hostile beneficiary, severe insecurity. Illegal allocation is excluded |
| A2, host and personal safety, D09 to D16 | Offer viable sanctuary 12, negotiate release 15, protective operation 8, decline 10 | Lawful reachable host, domestic support, secure route, credible sponsor, high value of peaceful institution | Exposed capital, unaffordable burden, impossible extraction, domestic instability, captive leverage. Missing access excludes movement |
| A3, civic construction and aid, D17 to D19 and D26 | Targeted work 15, measured aid 12, postpone 10 | Actual severe local need, viable delivery, affordable surplus, high recipient reliability, preservation of sovereignty | Critical domestic equipment deficit, competing repair needs, route vulnerability, repeated undelivered promises |
| A4, mediation, D20 to D23 | Seek terms 18, accept credible terms 16, amend 12, reject 10 | Stalemate, attrition, threatened sovereignty, verifiable balanced terms, recognized impartial mediator | Near-term attainable war aims, opponent's proven breach, unacceptable security loss, no way to settle all relevant wars |
| A5, civic institution, D24 to D30 and D34 | Found or join 14, remain 14, lawful exit 8, censure 8 | Actual durable successes, fulfilled material aid, fair burdens, useful mediation, respected vetoes | Broken obligations, aggression against members, coerced office changes, chronic funding failure, serious deception |
| A6, defense compact, D31 to D33 | Join exact defense 12, provide narrow help 14, decline 10 | Credible nearby threat, reachable ally, practical supply, compatible native faction obligations | Distant unsupported front, stronger existing alliance, an offensive mandate disguised as defense, severe national survival risk |
| A7, research and verification, D35 to D39 | Fund real research 10, accept reciprocal inspection 14, reduce under safeguards 12, defer 10 | Existing scientific capacity, credible external threat, symmetric inspection, verifiable reciprocal reduction, industrial surplus | Costly immature program, insecure inspected sites, one-sided disarmament, unproven custody, fragile delivery |
| A8, nuclear demands and use, D40 to D46 and D59 and D61 | Negotiate 18, reciprocal restraint 16, authorized threat 4, actual launch 1 | Verified coercion threat, real lawful capability, exact accepted owner mandate, credible limited settlement, documented retaliation right | Civilian harm, national veto, exposed bluff, owner disagreement, interception risk, loss of legitimacy, a viable peaceful alternative |
| A9, supreme mandate, D47 to D49 | Preserve civic charter 18, negotiate limited authority 12, ratify coercive mandate 2 | Full verified gates, sustained results, actual broad consent, credible affordable enforcement, severe unresolved international danger | Centralized personal control, low trust, likely member split, expensive global reach, independent nuclear opposition, peaceful order already working |
| A10, world demands and opposition, D50 to D55 and D62 to D63 | Negotiate 18, conditional accommodation 12, sovereign refusal 12, organized opposition 10 | Accommodation gains security with limited concessions, or opposition has credible allies and survivable defenses | A demand destroys sovereignty without protection, coercer lacks credibility, allies cannot reach, settlement obligations impossible |
| A11, completion and legacy, D56 to D58 and D60 | Fulfill agreed peace 18, recognize real peaceful legacy 20, revise failed mandate 16 | Actual obligations met, no unresolved strategic custody, stable observation, legitimate post-crisis institutions | Concealed unresolved sovereigns, new war, active independent opposition, disputed arsenal, an expiring campaign unable to finish |

A nuclear strike retains a low initial relative base because the movement's political premise makes actual use a grave rupture. This is a narrative design choice, not a fabricated claim that use occurs in one percent of games. A national owner's lawful military AI still needs explicit integration with the common policy and delivery owners. Gandhi content must not issue a second command outside those owners.

## 3. Named assessment scenarios

These scenarios make the intended contextual differences reviewable. They do not supply a numerical predicted outcome. Future source auditing must enumerate every actual candidate in each implemented scenario before reporting normalized probabilities.

| Scenario | Relevant facts | Intended legal choices and preference |
| --- | --- | --- |
| S1, exhausted colonial holder | Non-fascist holder has extensive denied non-core industry, stable core territory, an agreed independent beneficiary, and no unresolved claimant | A1 should favor direct or partial settlement. Continued refusal remains possible within the finite campaign. No economic penalty touches unrelated core industry |
| S2, vulnerable supply corridor | A contested non-core state contains the holder's only viable wartime route and has a living claimant whose consent is absent | Immediate release is excluded. Exact wartime negotiation, access settlement, or refusal remains. A high Momentum value cannot bypass the claimant |
| S3, fascist consolidator | Holder receives its one-time resistance and compliance adjustment and a finite control benefit | A1 may favor retention because its immediate cost differs. Later voluntary settlement or truthful League membership is still possible. Ideology switching cannot generate another bonus |
| S4, poor newly independent island | Country lacks spare industry and equipment, has a real port, and has just gained sovereignty | It can accept recognition and civic membership without a PP entrance toll. A3 favors a credible sponsored supply project. It cannot provide aid from nonexistent stocks |
| S5, industrial neutral mediator | A reachable neutral has spare civilian capacity, no war with either party, and both principals request talks | A4 favors a paid conference. The real thirty-day window and single qualified extension apply. Native peace execution and sixty-day observation remain separate |
| S6, members in rival factions | Civic partners share successful aid but belong to incompatible existing military blocs | A5 can favor continued civic cooperation. A6 rejects impossible dual faction membership and may favor narrower lawful help. Neither member is forcibly moved |
| S7, credible nuclear restraint | Three cooperative owners disclose real usable national devices, delivery, and lawful vetoes while an adversary offers reciprocal inspection | A7 and A8 favor verification and a measured security bargain. There is no pooled stock and no reason to spend a device to prove membership |
| S8, paper nuclear threat | A chair claims a weapon while the actual owner has withdrawn consent, lost delivery, or never produced a usable device | Nuclear threat eligibility fails or its credibility collapses. A8 favors withdrawal, truthful clarification, and negotiated repair. A fake stock count cannot restore leverage |
| S9, coercive but fragile congress | Nominal high Chaos coexists with uncertain owner consent, low current Cohesion, or insufficient real regional participation | The full mandate gate fails. The AI continues civic reform or defense. Chaos alone creates no new authority |
| S10, viable sovereign opposition | A target receives a harsh world demand but has actual allies, functioning industry, protected supply, and an independent arsenal | A10 may strongly favor refusal and organized opposition. The demand does not immediately defeat the target. Native wars and actual negotiated outcomes decide the conflict |
| S11, exhausted command host | A real mandate has lost its host support, allies defect, delivery is doubtful, and the campaign deadline approaches | A9 to A11 favor negotiated rollback or constitutional change over impossible renewed deadlines. No automatic nuclear revenge or compulsory global peace resolves the failure |
| S12, achieved peaceful legacy | The civic League has the exact five-member, three-region, six-success, three-peace and 180-day conditions | A11 recognizes a legitimate completed peaceful campaign. The AI receives no extra pressure to become nuclear or coercive simply because a focus remains visible |

The future AI reviewer should also compare identical legal circumstances for a human neighbor and an AI neighbor, a major and a minor, and two geographically different but materially equivalent actors. Differences must come from actual relationships and capability rather than hidden favoritism.

## 4. Campaign pacing and dynamic factors

### Original movement

The opening reply lasts fourteen days. Ready sovereignty commits immediately. The separate unsettled-territory mandate lasts thirty days. Refusal produces the actual ideology-specific response. Ordinary Chaos bands of 0, 200, 400, 600, 800, and 1000 set the initial Momentum anchors of 40, 45, 50, 55, 60, and 65 and base local endurance of 150, 180, 210, 240, 270, and 270 days.

Momentum can vary the not-yet-fixed local term by up to thirty days, within a ninety to three-hundred-day local clamp. Every local term remains capped by fire date plus 314 days. The stage is sampled before event outcomes change Chaos. Once a term exists, later Momentum, ideology, host changes, or occupation transfers cannot refresh it. New occupation inherits the remaining global window.

The AI therefore faces a real finite choice. A country can withstand the disruption and keep its territory. Higher industrial dependence, active fronts, legitimate beneficiaries, or a credible peace proposal make that choice more expensive. It cannot indefinitely restart a strike by moving one division or toggling occupation law. Historical successful settlements remain true even after the campaign ends.

### Civic consolidation

Founding takes thirty days after the full Chaos 400 gate and durable results exist. Failure to retain three qualified consents leads to the ninety-day reconsideration interval. Admission takes twenty-one days. The next ordinary civic leadership review occurs after 360 days. Expulsion includes fourteen days for a response and the proper two-thirds vote. Ordinary exit takes thirty days with immediate suspension of new obligations.

Constructive work takes sixty days for a modest project or ninety days for a major one. Mediation takes thirty days, with one fifteen-day extension only after both sides accepted a concrete outstanding provision. Aid and treaty promises are not durable success. Genuine sovereignty and peace require sixty days of observation.

Cohesion below 40 opens a sixty-day reform congress. One ninety-day viability clock runs while Cohesion is below 20 or viable membership below three. It resets only when both Cohesion is at least 20 and membership is at least three. Switching the failed condition does not restart it. Expiry leads to a reduced bilateral network or dissolution choice. These are opportunities to repair the institution, not automatic wars. A member can leave lawfully and still cooperate through an existing bilateral agreement.

Momentum and Cohesion changes follow Part 03's actual-outcome receipts and incident caps. Do not subtract them every time a tooltip refreshes. Foreign interdiction of promised aid and deliberate refusal to honor it require different assessments. Routine quiet civic life does not incur perpetual fatigue. The initial movement's thirty-day absence-of-results fatigue is finite and tied to that original campaign.

### Earned deterrence

At Chaos 800, a strong League can organize national research cooperation if the other program conditions hold. Ninety days is a cooperation term, not a countdown to a free bomb. Existing nuclear research, actual native project completion, national production, real devices, and credible delivery decide when Nuclear Pacifism can be granted.

A verified inspection takes thirty days. An agreed small-batch dismantlement stage uses a sixty-day anchor, scaled by the actual quantity and facilities under its owner. Technical capacity, devices, custody, policy, permission, and delivery remain separate. Research assistance can survive an office change, but national authorization is always rechecked before use. Members can complete peaceful disarmament and remain politically important without retaining an arsenal.

### Coercive world authority

Chaos must be strictly above 1000 at mandate voting and campaign entry, with every other Part 05 condition met. The 120-day supreme congress precedes the mandate campaign. The campaign lasts 720 days from mandate ratification. World demands allow forty-five days for a reply. Negotiated settlement windows last up to 180 days within the campaign.

Every substantive settlement and actual demobilization or disarmament obligation must complete by campaign day 720. Only then may the one final ninety-day stable-compliance observation finish, with an absolute ceiling at day 810. This is a narrow observation allowance, not extra time for a new war, a new settlement, or a repeated mandate. A material breach during that allowance prevents victory.

After ratification, the lower maintenance floors apply: five viable signatories across three regions, C at least 35, a lawful command host, and at least two consenting usable nuclear owner states with two devices total. Falling below a floor opens one thirty-day emergency recovery window. Actual consent, production, access, or lawful relocation must repair the cause. All failed floors share that original deadline, and another failed floor inside the window cannot reset it. Every floor must recover. Unrepaired expiry ends the mandate. Once the single window has been used and closed, any subsequent maintenance failure ends the mandate. Spending one of the entry gate's six devices therefore does not automatically end the campaign. Gandhi's death remains final and cannot use this window to restore him.

A later fall in Chaos creates political pressure for restraint or reform rather than deleting actual wars or earned institutions. Campaign failure leaves real native wars requiring actual settlement. It does not grant compulsory peace, reset the world, or erase human opposition. Shared terminal priority can independently prevent the Gandhi terminal outcome.

### Reconsideration without world polling

Prefer exact relevant callbacks and the project's existing bounded scheduling. An actor reevaluates after a changed offer, payment, control, war, membership, charter breach, character state, policy, or arsenal fact. Ordinary nonurgent reconsideration can use an authored seven-day actor-level cooldown. This cooldown never pauses a true reply or mission deadline and is not another world scan.

Do not recalculate every country's preferences on every day tick. Reuse the already registered eligible inventory and process bounded slices with a stable cursor. Add a new state, country, or crisis when its owning callback establishes relevance. A one-time stage audit may validate the complete actual member or sovereign set through shared infrastructure, without introducing a new repeated global observer.

## 5. Regional and strategic variation

Regional variation should follow geography, logistics, history already represented in the country, and the actual conflict. Do not attach inherent peacefulness, irrationality, or nuclear enthusiasm to an ethnicity or religion. The shared inhabited-region map determines gate diversity. Moving a capital never manufactures another region.

| Actual setting | Distinct choices and cost pressures | Consequence for AI and content |
| --- | --- | --- |
| Landlocked release with disputed access | Negotiate rail or border access, repair a real route, seek a credible neighbor's guarantee | Aid needs a deliverable route. Recognition alone cannot remove isolation. Mediation must include the actual route owner |
| Island or archipelagic member | Preserve convoy access, port capacity, escorts, and reachable refuge | A distant ally's nominal support is less valuable without shipping and basing. A small paid shipment may be more useful than an impossible industrial promise |
| Contiguous industrial occupation | Weigh denied useful output against border security, transport, and legal sovereignty | Partial settlement and exact access terms are meaningful. Core industry remains outside occupation denial |
| Sparse or low-industry territory | Use limited repair, administrative access, and external material support | PP-only spending cannot conjure industry. A poor independent member still has one civic vote and can refuse foreign command |
| Divided country with living claimants | Separate homeland identity, current owner, current controller, and exact disputed allocations | No core-based automatic annexation. The AI needs claimant consent and a viable capital before committing a settlement |
| Frontier under immediate military threat | Fund protection, evacuation, supply, and a genuinely reachable defense partner | Native war risk shapes willingness. Civic membership does not auto-call distant members or supersede an existing faction |
| Mature scientific and industrial country | Choose actual research effort, facilities, inspection exposure, delivery investment, and reduction | A strong native program can contribute quickly but retains ownership and veto. It cannot convert its prestige into foreign stock |
| Remote command host with broad nominal membership | Maintain real access, regional representation, industrial support, and enforceable commitments | World mandate feasibility declines when power cannot reach targets. Relocating a capital or offices does not cure that material weakness |

## 6. Nine concrete rare variants

These are conditional authored variants of real systems. They are not historical claims, an endless crisis generator, or hidden dice rewards. A variant opens once for its exact triggering episode and reuses the action, payment, mission, and cleanup contracts from Part 08. Its rarity comes from the conjunction of actual circumstances. No numerical spawn probability is asserted.

### V1. Rival allies shelter one convenor

**Trigger.** Gandhi's current host loses safe access while two eligible refuge offers exist in rival native factions. Both governments consent to sanctuary, but neither can legally join the other's defense arrangement. Gandhi is alive and a real route exists to at least one destination.

**Choices and costs.** Choose a reachable civilian refuge using D11 and P2, pay P5 for an actually supported protective movement, or preserve a temporary civic council while negotiating safe passage. A second offer can remain a diplomatic alternative, not a second character. No faction switch is bundled into sanctuary.

**Outcome and AI.** The accepted host receives the real person and a finite burden. Civic work can continue across faction lines. The AI prefers safe lawful access and viable domestic support over nominal allied strength. If every route fails, personal eligibility remains unavailable and the institution follows its continuity rules. No teleportation, duplicate Gandhi, or office-based project reset occurs.

### V2. The last-state succession bargain

**Trigger.** A willing holder owns only non-core territory, every owned state has an accepted independent successor allocation, and the human or AI holder could otherwise be eliminated by complete release.

**Choices and costs.** Choose a valid successor before mutation through D07, renegotiate a narrower lawful allocation, or refuse. The real cost is surrender of the original holdings and accepted property. There is no PP fee for preserving the player's ability to continue.

**Outcome and AI.** Full succession executes only under the distinct audited zero-host mode, exact peace requirements, and postcommit continuation. AI acceptance requires a viable successor with actual land and institutions. Missing consent or an invalid successor leaves the original country intact. A successful case gives the ordinary bounded substantive receipt, not extra rewards for deleting a tag.

### V3. A fascist government chooses verifiable reform

**Trigger.** A fascist holder has already received its once-per-state consolidation, later proposes a genuine sovereignty settlement, and requests civic admission without current aggression against a member.

**Choices and costs.** Commit actual territory through D02 or D05, accept twenty-one-day charter consultation under D25, or retain territory and remain outside. Paid aid or reconstruction uses its real P3 or P4 costs. A propaganda declaration alone buys nothing.

**Outcome and AI.** Genuine settlement can mature and admission tests actual conduct. Past consolidation is not reapplied, and a government-label switch never resets the campaign. The AI can choose a useful limited reform while remaining politically distinct. A verified lie instead opens the ordinary evidence and expulsion process. No blanket ideological ban or automatic trust appears.

### V4. Two simultaneous wars defeat an apparent peace

**Trigger.** Parties accept a mediated agreement for one real war, but another native war still keeps materially relevant parties in conflict. The mediator discovers the overlap before claiming success.

**Choices and costs.** Expand the concrete proposal with every required party, use the single fifteen-day extension only if both principal sides have accepted a concrete outstanding provision, or record a limited agreement and continue the unresolved case separately. Administration consumes actual P2 capacity. Territorial concessions require exact P1 consent.

**Outcome and AI.** A limited agreement remains historical fact but does not masquerade as durable general peace. The AI prefers terms it can legally fulfill and rejects a fake universal white peace. Sixty-day maturity begins only for the correctly settled protected episode. Expiry produces an honest impasse without duplicating or undoing completed terms.

### V5. A poor member hosts useful scientific work

**Trigger.** An independent member has relevant actual research capacity or an existing project but insufficient industry to finance the agreed cooperation alone. A richer member has spare capacity and is willing to sponsor it. The strong-League program gate is otherwise met.

**Choices and costs.** The recipient commits its native research effort and the sponsor explicitly pays its P6 support, choose a smaller ordinary project, or postpone the nuclear program in favor of P4 civic work. No sponsor consent is inferred from membership.

**Outcome and AI.** Useful cooperation can strengthen a small country's role while finished research and devices remain nationally owned. The AI compares actual research maturity and civilian opportunity cost. A broken sponsorship ends only future support, preserves completed work, and earns no completed contribution receipt. Neither scientific reputation nor a ninety-day timer produces a device.

### V6. A captured depot contains an uncertain strategic claim

**Trigger.** Native control changes at a location associated with a real nuclear custody claim, while the new holder lacks proven technical access, national authorization, or verified native usable stock. An original owner or observer remains available.

**Choices and costs.** Guard the actual location with real national forces and supply, permit a consenting inspection under P7, negotiate return under a supported existing owner, or deny access and accept diplomatic uncertainty. Operational integration is unavailable unless the optional conserved custody adapter has actually been implemented and accepted.

**Outcome and AI.** The depot can matter politically without increasing a bomb count. The AI values physical security and a credible settlement over a fabricated instant arsenal. Any proven transfer must debit and credit through its real owner. Loss or destruction cannot create a nominal refund. This variant remains playable even when its optional operationalization branch is unavailable.

### V7. The indispensable owner refuses launch authority

**Trigger.** A League demand relies on a national arsenal owner whose native policy tightens or whose government revokes an uncommitted authorization. Other members support the demand, but their own devices or delivery do not independently establish the same threat.

**Choices and costs.** Respect the veto and amend the demand, seek a separately lawful owner commitment, fund actual conventional protection, or pursue a domestic political dispute through ordinary institutions. D42 veto is free. New military preparations and P8 diplomacy are paid by their actual actors.

**Outcome and AI.** A majority cannot seize the vetoing country's bombs. The AI reduces threat credibility and favors a realistic bargain. An already pending native delivery stays with its owner and cannot be fictionally refunded. If the chair lies about continuing authority, verified exposure can reduce M and C and prompt exit. No forced launch resolves the disagreement.

### V8. Gandhi dies during a successful civic campaign

**Trigger.** Gandhi dies after the unique initial appearance while the League has durable successes, active projects, and at least three viable members. His death is a real character lifecycle event, not an arbitrary random punishment for success.

**Choices and costs.** Convene institutional succession under D15 with P2 or P8 administration, choose collective civic leadership, or settle dissolution. Members can continue funded aid or cancel uncommitted work through its actual owner. National arsenals and vetoes remain national.

**Outcome and AI.** The personal supreme path ends permanently. A peaceful institutional legacy remains attainable if its actual gates hold. The AI prefers continuity when members can sustain useful work and favors dissolution when they cannot. No second resurrection, copied Gandhi, instant civil war, or nuclear revenge occurs.

### V9. One small sovereign still has an unresolved status

**Trigger.** The command host believes the world settlement is complete, but the complete sovereign audit finds a small refusing country, disputed strategic custody, or a legally active opposition arrangement outside the current three displayed target cards.

**Choices and costs.** Bring that exact case into the visible target set, negotiate a lawful accommodation under D51, accept a political rollback under D55, or pursue an actual lawful war if time and capability permit. Diplomacy uses actual remaining P8 funding and any settlement or military costs remain real.

**Outcome and AI.** The unresolved sovereign blocks premature victory. The AI cannot omit it because it is small or inconvenient. A settlement completed by day 720 can enter the one final ninety-day observation. New substantive settlement after day 720 cannot use that allowance. Failed mandate leaves a playable world and actual wars, with no automatic annexation or forced terminal result.

## 7. Exploit resistance and honest failure

| Exploit or failure pressure | Required protection | Legitimate alternative retained |
| --- | --- | --- |
| Releasing, annexing, and rereleasing the same beneficiary | Exact beneficiary and substantive episode receipts, maturity, attribution, and incident caps | A genuinely new settlement can still be evaluated on its actual facts |
| Manufacturing wars to obtain peace credits | Exclude fabricated wars and same-player transfer cycles. Require real conflict, actual mediation, exact execution, and observation | Real peace from difficult or unequal wars can count |
| Moving capitals to pass regional gates | Use the shared validated inhabited-region mapping and actual participation | A real new independent member in another region can contribute |
| Splitting one shipment into many contribution credits | One actual contribution episode and payer, with received material and no duplicate credit | Several independently paid useful projects can contribute |
| Canceling projects after receiving partial rewards | Commit exact payment once, reward actual verified completion, refund only recoverable unspent assets | Real partial work remains and can be finished later at its actual cost |
| Rotating hosts to reset deadlines or duplicate Gandhi | One character, one current custodian, immutable project generation and deadline | Lawful office transfer and refuge remain possible |
| Toggling ideology to repeat fascist consolidation | Once-per-state per-incident receipt and fixed campaign ceiling | Current ideology changes active treatment as required |
| Recruiting powerless clients to fake global consent | Independent sovereign agency, active member duties, actual factory denominator, region and receipt gates | Poor but independent participating countries remain valid members |
| Threatening with borrowed or captured fictional devices | National native inventory, real custody, policy, owner consent, and delivery evidence | Physical custody can still be guarded, inspected, or negotiated |
| Paying one native bomb twice or refunding a fired device | Native delivery owner pays once and confirms outcome. Pending action remains owned through policy changes | Honest cancellation can recover only a still-uncommitted owned reservation |
| Relaunching the supreme mandate to extend its clock | One incident-owned mandate deadline and explicit no-extension rule | Negotiated rollback, ordinary peace, and a reformed League stay playable |
| Omitting small targets from the visible cards | Complete paged inventory with stable cursor and final complete legal-status audit | Bounded presentation remains readable |
| Treating all dissent as world-ending resistance | Distinguish material sovereign opposition and strategic arsenal control from individual disagreement | Ordinary domestic dissent can remain under an actually completed settlement |

Do not impose extra Chaos costs merely to discourage an exploit. Native wars, deaths, faction changes, releases, and nuclear use retain their actual shared owners. Custom outcomes need distinct receipts and bounded effects. Votes, menus, stage gates, promises, and failed information requests do not generate Chaos.

## 8. AI implementation handoff and acceptance

The future implementation should define actor-owned temporary strategies with explicit activation and abort conditions. Preferences end when membership, targets, current war, character state, charter stage, or authority no longer supports them. Do not leave permanent war plans, diplomatic targets, or industrial reservations attached to countries after the relevant Gandhi institution ends.

The source author and the AI auditor have distinct roles. The author owns code and scenario setup. `chaosx-ai-probability-auditor` inspects exact before and after definitions, complete legal candidate sets, engine behavior, target coverage, and the named scenarios. An audit report must distinguish an event option weight, decision desirability, MTTH timing, and an observed simulation frequency. It cannot label them all probability.

The acceptance set should include every scenario S1 to S12, each rare variant's real entry and exit, all-zero and tiny-weight cases, exact affordability, full mission slots, rival factions, a host change, Gandhi's death, concealed versus inspected arsenals, a policy veto during a pending operation, peaceful disarmament, mandate expiry, and competing terminal ownership. Tests must prove that legal and payment gates dominate preference, not simply that the AI sometimes selects a button.

No HOI4-named MCP tools were exposed during this planning session. No AI tool sweep, native-game test, runtime probability measurement, delivery test, or save/reload test was run. The complete supplied source-reading gate was performed, and current repository evidence is recorded separately. Future tool availability must be discovered honestly. Missing runtime access does not justify inventing selection frequencies or reporting a design as playable.

## Source basis

The AI gates, score/probability distinction, lifecycle strategy cleanup, scoped scheduling, payment constraints, and validation separation follow the fully read supplied AI, decisions, MTTH, events, cleanup, and subagent sources. The current nuclear owner and occupation limitations are recorded in `122_gandhi_repository_research.md`. The campaign thresholds and clocks follow Parts 01 through 05 and Part 08. The regional variants and numerical preference anchors are authored event design, subject to future balance review.
