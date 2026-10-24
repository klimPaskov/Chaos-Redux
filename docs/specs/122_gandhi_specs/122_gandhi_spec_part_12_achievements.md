# Part 12. Achievement design and receipt contracts

## Status and ownership

This is an implementable design for twelve difficult achievements. ACH01 through ACH12 are internal working references, not final achievement names, localisation, registered identifiers, or allocated numeric IDs. The current Gandhi contract governs every route. Achievement requirements add optional challenges to that contract. They do not change event availability, force a route, create new playable content, or weaken a settlement requirement.

No achievement backend, account identifier, unlock API, or runtime achievement file has been inspected. Before implementation, identify the actual repository framework and its supported country, campaign, multiplayer, save, and presentation contracts. Bind the logical conditions below to that framework. Do not invent a Steam unlock API or claim platform achievements. This is a future integration requirement, not an unfinished planning deliverable.

The parent owns registrations, proof producers, predicates, and final unlock integration. The scripted-system architect can implement narrowly assigned persistent receipt helpers. Domain owners supply authoritative liberation, peace, civilian, membership, nuclear, succession, and world-end results. The icon artist produces the approved 64 by 64 triplets. The localisation auditor later writes and verifies final titles, descriptions, progress labels, and hidden-state wording. No new public meter, spendable resource, national spirit, rich GUI, military unit, or technology tree is introduced for achievements.

## Shared proof rules

### Scope and permanence

An attempt belongs to one Gandhi incident and one country lineage. A country lineage means one actual country generation, not just a tag string. A destroyed country and a later country using the same tag are different generations. Cosmetic names, an election, ideology changes, leader changes, and a lawful capital move do not create a new generation.

An unlock is permanent once the framework commits it. Later war or loss cannot remove it. Before the unlock, any condition specified as continuous must remain true for its full interval. A violation cancels that interval rather than freezing it. Re-entering a permitted state starts a new interval only where the individual achievement allows it. The same earned receipt cannot be spent, duplicated, or reassigned to another attempt.

Receipts are internal evidence. Their counters never appear as a third persistent custom value alongside Movement Momentum and League Cohesion. A normal achievement list can show concise progress and blocked reasons through the existing consumer. It must not expose hidden countries, unknown arsenals, unrevealed endings, or private multiplayer information.

### Required record fields

The exact storage schema is chosen after the framework audit. Its logical record must preserve the following fields and relationships.

| Field | Required meaning |
| --- | --- |
| Incident identity | The single Gandhi fire-once incident and its start date. A manual re-fire does not create another legitimate attempt. |
| Actor lineage | Country generation that performed or authorized the relevant action, with its tag at that time. |
| Beneficiary lineage | Actual sovereign recipient or protected country generation. A later tag reuse cannot impersonate it. |
| Episode identity | Authoritative liberation, war settlement, reconstruction, disarmament, command mandate, or defeat episode. |
| Proof class | Committed action, materially completed action, durable success, rejected action, invalidated evidence, or terminal result. |
| Exact scope | Sorted state list, affected sovereign parties, relevant war identities, or distinct national arsenal owners as appropriate. |
| Frozen scale | Relevant pre-action population, state count, industrial contribution, or measured device stock. Use the field required by the challenge and retain its measurement basis. |
| Consent and role | The parties that consented and the actor's actual host, contributor, mediator, national-owner, or opposition role. |
| Time and maturity | Commitment date, completion date, required observation interval, and any interruption. |
| Conservation | Required before and after stock, payment, transfer, dismantlement, or settlement facts. Do not infer delivery from an order. |
| Continuation | Authorized country succession and explicit human continuation choice, kept separately from country identity. |
| Invalidity | Fabrication, known debug forcing, repeated farm, overturned settlement, false report, conflicting transaction, or missing proof. |

Each proof producer emits once after its owning transaction commits. A popup, decision selection, scheduled event, promise, missing error, or diplomatic opinion modifier is insufficient. Use actual postconditions. An interrupted transaction produces no success receipt. Repeated callbacks locate the existing episode and do not increment it.

### Substantive scale and independent parties

The event's own durable-success definition remains authoritative. For this achievement suite, a qualifying sovereign settlement must additionally include at least one inhabited state and meet one of these challenge-scale tests: two inhabited states, at least 500,000 people in the settled states at the frozen pre-transfer snapshot, or at least three usable civilian and military factories recorded before Gandhi's temporary denial. These are proposed challenge tuning anchors. They are not historical claims or extra requirements for ordinary independence.

The qualifying beneficiary must remain genuinely independent for 60 consecutive days. A puppet with a changed name, an unresolved foreign controller, an already independent country receiving no substantive sovereignty, or a release immediately reversed by reconquest fails. An existing beneficiary can qualify through a real territorial settlement without acquiring Gandhi creator origin. Its immutable Event 006 origin remains intact.

A qualifying peace episode uses the actual war and parties recorded by the shared settlement owner. It requires 60 days of observed peace for the recorded parties and fronts. Unrelated wars are not silently erased. A manufactured war between controlled partners, repeated declaration and settlement of the same dispute, or an unrelated automatic White Peace result without recorded Gandhi mediation contributes no achievement credit.

Independent parties cannot be subjects of the credited actor or nominal shells created to multiply counts. Distinct means distinct country generations and substantive episodes. A single multi-beneficiary treaty episode can provide the actual beneficiary count for a challenge, but at most two credits toward any condition expressly using the event's founding or escalation gate totals. This treaty limit is separate from the identity of the one global Gandhi incident. Achievement code must not change those gate credits.

Pure constructive or civilian project results do not become core sovereignty or mediated-peace gate credits. Where a challenge expressly requires a durable civilian recovery or protection result, the actual owner must prove completion followed by 60 consecutive observed days with that outcome still valid, unless the challenge sets a longer interval for the outcome. An institutional membership interval is a separate condition. These are achievement-specific receipts and never substitute for the event's required sovereignty or peace evidence.

### Country changes, multiplayer, and human continuation

Use the actual backend's supported identity and participation data. Country proof and human-account proof are separate questions.

- Ordinary country progress remains with its country generation through elections, ideology changes, cosmetic changes, and legitimate government succession.
- Full-territory consensual succession may transfer an attempt only through the existing audited succession transaction and the source human's explicit continuation choice. Store source generation, selected successor generation, receipt identity, and continuation result. Other successor countries inherit their own sovereign history, not a copy of the human attempt.
- Arbitrary tag switching, occupying a country after another player completed its work, or taking over an unrelated save cannot create personal credit. A known forced switch invalidates any human-specific attempt whose continuity cannot be established.
- In multiplayer, several countries may independently qualify. Each needs its own actual contribution and qualifying role. A shared treaty can support different countries' distinct achievements, but one country's payment or veto cannot be copied to every participant.
- A disconnected player does not lose committed country evidence. The backend must distinguish a continuing participant from a new controller before displaying a personal unlock. If it cannot, record country-level completion only and do not claim account attribution.
- AI-only national actions can support world conditions and beneficiary durability. They do not substitute for an actor-specific human contribution when an achievement requires that action. A project intentionally committed by the qualifying actor may complete automatically later.
- Known debug or force-trigger paths, receipt fabrication, and test-country grants cannot unlock these achievements. Universal console detection is not claimed. Bind to actual framework restrictions and record any enforcement limit.

### Evaluation and load

Evaluate on relevant committed transactions and scheduled maturity dates. Recheck only the attempt's recorded countries, states, wars, contributions, and arsenal owners. Reuse the core event's ownership, diplomacy, regime, death, and cleanup callbacks. No achievement needs a new daily global scan.

Loading a save restores pending maturity dates, invalidation state, and the original episode identities. It does not reissue earned receipts. A version migration preserves known proof conservatively. Missing historical evidence produces unavailable progress for that condition, never a retroactive invented victory.

## Achievement coverage

| Reference | Challenge focus | Qualifying player role | Earliest public visibility |
| --- | --- | --- | --- |
| ACH01 | End serious noncooperation through several durable liberations | Nonfascist refusing holder | First local campaign activation |
| ACH02 | Use the fascist exception once, then give up its territorial advantage through real releases | Fascist holder | The exception's first committed treatment |
| ACH03 | Complete consensual succession of the host's entire non-core estate | Human source continuing as a chosen successor | Full-territory succession becomes a valid option |
| ACH04 | Deliver minority protection and civilian recovery across countries | Member or accepted civilian partner | First relevant civilian mission |
| ACH05 | Sustain a broad successful League entirely outside the nuclear evolution | League member with real contributions | League constitution |
| ACH06 | Reconcile a former host with several states it released | Former host | First durable release |
| ACH07 | Leave coercive command and preserve a viable peaceful association | Dissenting member | Public coercive mandate or unlawful-use crisis |
| ACH08 | Exercise a real national launch veto and secure a credible settlement | Nuclear owner | A valid command request reaches that owner |
| ACH09 | Complete reciprocal verified disarmament by several real owners | Participating national arsenal owner | Verified reciprocal talks open |
| ACH10 | Preserve a functioning League after Gandhi's death | Continuing member | Gandhi's actual post-incident death |
| ACH11 | Complete the Ultimate Society's real terminal settlement | Lawful command host | The public supreme-mandate route is revealed |
| ACH12 | Defeat the supreme campaign and preserve sovereign opposition | Material opposition participant | An actual supreme campaign targets its coalition |

All visibility states are presentation gates, not unlocks. Hidden achievement slots may show the framework's ordinary concealed state without leaking a route name or condition. Final wording is deferred.

## ACH01. Negotiated end to a substantial refusal

**Entry and scale.** The actor is a nonfascist owner or controller when its campaign activates. Its initial affected estate contains at least four inhabited non-core states and at least one million people. At least two of those states remain in valid nonfascist noncooperation for 60 consecutive days within the original bounded campaign. Actual zero-output treatment and the appropriate temporary morale variant must be recorded.

**Achievement predicate.** Before the relevant campaign window expires, the actor commits sovereign settlements benefiting at least three independent country generations from that initial estate. Each settlement meets the shared substantive test. All three mature for 60 days. No refusing active state from the actor's initial estate remains unresolved, and no replacement occupation is used to evade this condition.

**Receipts and timing.** Retain the initial estate snapshot, treatment interval, allocation and consent receipts, each committed transfer, each maturity, and cleanup of the last refusing state. Unlock only when the last required durable receipt matures and the unresolved-estate check passes. Maturity may occur after economic denial has ended. It never extends denial.

**Disqualifiers.** A fascist switch during the qualifying treatment interval, a fabricated beneficiary, an unfulfilled release promise, destructive removal of factories, or ignoring the campaign until it expires does not qualify. Naturally expiring penalties are not a settlement.

**Continuity and art.** Follow the actor lineage across ordinary government changes. Full-estate succession belongs to ACH03 and cannot duplicate the same actor attempt here. Motif: an opened iron padlock resting on a folded territorial deed, with one clear opening as the focal point.

## ACH02. Voluntary liberation after fascist consolidation

**Entry and scale.** The actor is fascist at refusal. At least four inhabited non-core states and one million people fall within its initial estate. The exception commits its one-time treatment on at least three states, with a single receipt per state for the incident.

**Achievement predicate.** While still fascist, the actor later grants genuine sovereignty to at least three independent beneficiaries covering at least half of its initial affected population. Each beneficiary satisfies the substantive settlement test and remains independent for 60 days. The actor pays at least one agreed, actually received civilian reconstruction contribution to one of them.

**Receipts and timing.** Preserve before and after resistance and compliance values, clamping, original deadlines, treatment identities, the voluntary release package, the paid delivery, and beneficiary maturities. Unlock after the last maturity and paid-delivery verification.

**Disqualifiers.** Ideology cycling cannot earn another consolidation receipt. The actor must not have gained additional exception applications on the same states through a controller change. Puppet relabelling, forced faction entry, confiscated repayment, or immediate reconquest fails. Neither output retention nor the initial resistance reduction alone is an achievement.

**Continuity and art.** A routine leader change within the same fascist state preserves the attempt. A change away from fascism before the required releases ends this attempt. Motif: a military baton laid aside beside an open civic charter and a small intact olive sprig. Use no historical extremist emblem.

## ACH03. Consensual succession without a host remnant

**Entry and scale.** The human actor owns no core state and at least four inhabited states with a combined population of one million. The accepted all-territory succession option is genuinely available. The exact allocation produces at least two independent successor countries, each with a viable agreed state package.

**Achievement predicate.** The source explicitly chooses full succession and its human continuation country. All materially affected living claimants consent. The transaction covers every owned source state, resolves the relevant wars, applies the audited zero-host exception, and performs the human transfer only after successor setup. Every resulting successor remains independent and mutually at peace with the others for 90 days.

**Receipts and timing.** Link the complete pre-commit allocation, whole-estate coverage, consent, relevant war closure, source removal, exact successor packages, and explicit human continuation. Unlock on the chosen successor's attempt after the 90-day observation interval.

**Disqualifiers.** An omitted last state, silent player elimination, unattended continuation, a puppet successor, a fabricated council identity, or unrelated wars erased by the transfer fails. An arbitrary later tag switch cannot claim the source attempt.

**Continuity and art.** Only the explicitly selected successor receives the human continuation. Other successors retain their independent country records and cannot duplicate this award through the same transaction. Motif: an old key passed into an open hand beside two distinct plain door keys. Avoid crowns, annexation maps, or a destroyed home.

## ACH04. Civilian protection with measurable recovery

**Entry and scale.** The actor joins the League or becomes an accepted civilian cooperation partner. It undertakes protection or recovery obligations in at least three distinct inhabited states belonging to at least two independent countries other than itself. At least 500,000 people are covered by the frozen affected-state snapshots.

**Achievement predicate.** Complete three paid and geographically deliverable obligations. At least one verifies protection or restoration of civilian access for an identified threatened community through the existing owner system. At least one verifies physical recovery or relief actually received. At least one verifies a lawful refugee reception, return, or safe access settlement. These may be three different tasks, but a single completion cannot fill two required families.

**Receipts and timing.** The civilian owner records actual beneficiary, scope, access, paid goods or capacity, before and after condition, and verified result. Begin one 90-day observation interval after the last required task completes. All three protected outcomes must remain valid through that interval. An actor-caused reversal invalidates the attempt. Unlock when the interval completes with all owner proofs still valid.

**Disqualifiers.** A paid promise without delivery, compulsory displacement presented as protection, taking civilian homes for the contributor, double-counted migration credit, or creating the same crisis to repair it fails. Unsupported minority or access proof must remain unverified rather than replaced by a generic stability increase.

**Continuity and art.** Each multiplayer contributor needs its own paid and completed obligations. Motif: a repaired small doorway sheltered by an open hand, with a single visible roof repair. Avoid ethnic caricatures or invented community flags.

## ACH05. Durable nonnuclear League success

**Entry and scale.** The actor is a consenting independent League member before its first qualifying contribution. The League reaches five independent members across three inhabited macroregions, measured through the shared region mapping.

**Achievement predicate.** Sustain that membership scale for 360 consecutive days, with at least seven distinct durable substantive receipts during or before the interval. Include three sovereign beneficiaries and two genuinely mediated peace episodes. The actor must deliver three material contributions to three separate member beneficiaries. Movement Momentum and League Cohesion remain at least 60 at the end, and no member is being compelled by a Gandhi mandate.

**Nonnuclear condition.** Nuclear Pacifism must never have activated in this Gandhi incident before the unlock. No League authority may have authorized an actual nuclear threat or use. Independent national research does not violate this condition by itself.

**Receipts and timing.** Unlock after the 360-day membership interval, required durable receipts, and paid deliveries. Revalidate the founding identities and shared macroregions. Capital hopping cannot manufacture regional coverage.

**Disqualifiers.** A member becoming a subject, forced membership, an actor-created war used for mediation, or a brief departure concealed from the membership record breaks the relevant interval. This challenge does not prevent normal later evolution after the award.

**Continuity and art.** All qualifying members may earn their own award only through their individual contributions. Motif: a compact woven ring of differently textured ribbons around a small olive branch, showing cooperation without a single dominant crown.

## ACH06. Reconciliation between a former host and its successors

**Entry and scale.** The actor has committed genuine releases for three qualifying beneficiary generations from its own initial estate. At least two beneficiaries must have a different stable home-region identity from the actor, using Part 10's coherent homeland or core-population mapping. Freeze the actor's mapping before its first qualifying release and each beneficiary's mapping at its own release. Current capitals and overseas possessions cannot alter the comparison.

**Achievement predicate.** All three beneficiaries voluntarily join the same civic League network as the former host after their sovereignty matures. The former host completes one paid, actually received civilian contribution for each. All four countries remain independent, mutually at peace, and free to leave for 180 consecutive days after the last contribution.

**Receipts and timing.** Link the original release, immutable beneficiary identity, independent membership acceptance, delivered aid, and continuous relationship interval. Unlock at the end of that interval. The parties need not join the same military faction.

**Disqualifiers.** Membership imposed through a subject relationship, armed ultimatum, stolen domestic mandate, compulsory nuclear command, or an expulsion-and-rejoin farm fails. Existing claims need not disappear automatically, but no party may be prosecuting them by war during the interval.

**Continuity and art.** The former host owns the attempt. A later human takeover of a beneficiary does not transfer it. Motif: two visibly different hands clasped above a released chain link, with a neutral background supplied only by the immutable achievement template.

## ACH07. Principled exit and a surviving peaceful association

**Entry and scale.** The actor has been a genuine member for at least 120 days and has delivered two material contributions. A public coercive mandate, attack on a member, or unlawful nuclear use then creates the accepted emergency-exit condition.

**Achievement predicate.** The actor explicitly rejects the coercive policy and uses a lawful withdrawal path. It retains sovereignty and its own lawful property. After the coercive policy or route ends through defeat, abandonment, or reversal, the actor helps constitute or rejoin the event's accepted reformed civic League. At least three independent states across two regions participate and complete two new durable peace or civilian settlement receipts over 180 days.

**Receipts and timing.** Preserve prior membership, paid contributions, the triggering breach, explicit dissent and exit, political closure of coercion, renewed consent, and post-reform outcomes. Start the 180-day interval when renewed consent establishes the required three-state, two-region association. Maintain that scale continuously and earn both new durable results within the interval. A break resets that interval, and only outcomes completed and matured after its new start can qualify. Unlock at its end with both owner proofs valid.

**Disqualifiers.** The actor must not have voted for the coercive mandate, surrendered its national launch veto to that mandate, or participated in its unlawful nuclear use before dissenting. Joining a few days before leaving, resigning merely to avoid a paid debt, or exploiting confiscated property fails.

**Continuity and art.** Other departing players need their own qualifying membership and contributions. Motif: an intact folded charter beside a deliberately untied command cord. Avoid a destruction motif that would imply dissent itself destroys peace.

## ACH08. A credible national veto followed by settlement

**Entry and scale.** The actor owns at least one actual usable nuclear device, has verified delivery capability against the disputed target, and receives a genuine Gandhi command request during the nuclear or supreme-authority crisis. This is a national-owner attempt, not a League treasury attempt.

**Achievement predicate.** The actor exercises its own lawful veto before any debit or launch. The same crisis subsequently ends in an accepted verified peace or reciprocal-disarmament settlement involving the actor and at least one independent nuclear-capable opponent. Both parties observe the settlement for 90 days. The actor never authorizes or carries out a nuclear strike during this Gandhi incident before unlocking.

**Receipts and timing.** Preserve the real request, owner permission state, device and delivery evidence at the request, the veto, absence of a corresponding launch or debit, the actual crisis settlement, and its maturity. Unlock after 90 days.

**Disqualifiers.** A request against an unreachable target, an empty arsenal, a bluff falsely reported as a device, a cancelled animation after stock consumption, or a scripted request created only for the achievement fails. A veto cannot override another owner's lawful inventory.

**Continuity and art.** Request-time proof remains with the vetoing owner. Later capture never transfers that receipt to the captor. The settlement must still verify the actor's continuing sovereign participation, and voluntary verified dismantlement can satisfy the settlement. Motif: a physical lock on a closed launch control housing, with the owner key visibly outside it. Do not paint UI labels or a red cross into the subject.

## ACH09. Reciprocal dismantlement of real arsenals

**Entry and scale.** The actor is one of at least three independent national owners entering a reciprocal agreement. Together they possess at least six verified usable devices, with every owner holding at least one and the actor holding at least two at the frozen opening snapshot.

**Achievement predicate.** Each owner dismantles every device recorded in its opening obligation through a supported measured national debit. No credit comes from a transfer, capture, use, reservation, or inventory relabel. At closure, each of the three owners has zero actual usable nuclear devices and keeps that condition for 180 consecutive days. The actor performs its own dismantlement and at least one genuine inspection or assurance obligation.

**Receipts and timing.** Record each owner's baseline, every measured decrement, any intervening acquisition or production, verified final zero, inspection result, and the continuous interval. A newly acquired device must be dismantled before closure, and acquisition during the 180 days resets that interval.

**Disqualifiers.** Missing conservation evidence, optional unimplemented cross-owner escrow, a hidden substitute stockpile, a strike masquerading as dismantlement, or counting the same device twice fails. If the installed adapter cannot measure a real debit, this award remains unavailable for that implementation.

**Continuity and art.** Ownership changes end the affected agreement unless all new legal owners explicitly ratify a fresh measured obligation. Motif: an opened, empty warhead casing beside two plain inspection seals. It depicts dismantlement, without technical internal detail.

## ACH10. Institutions outlast the convenor

**Entry and scale.** The actor is an independent member of a League containing at least five independent members across three regions when Gandhi dies after the incident has begun. A historical death before the event and the event's single fictional return do not satisfy this trigger.

**Achievement predicate.** Through the accepted institutional-succession route, retain at least four of those original members across two regions for 180 consecutive days after the succession settlement. The actor accepts the new lawful civic leadership process and completes two actual material contributions. The continuing League earns three new durable receipts, including one peace settlement and one civilian recovery result.

**Receipts and timing.** Store the genuine death, pre-death roster, transition choice, new leadership consent, retained generations, contributions, and post-transition outcomes. Unlock after the observation period and required maturities.

**Disqualifiers.** The actor must not have caused or knowingly sponsored Gandhi's death, blocked an accepted rescue it was obliged to deliver, or used the transition to impose supreme command. A recurring resurrection or relabelling another character as Gandhi fails the one-person contract.

**Continuity and art.** A changed convenor is ordinary institutional continuity, not a transfer of country achievements. Motif: a lit reading lamp beside an empty plain chair and an open service ledger. Avoid a generated historical likeness.

## ACH11. Verified Ultimate Society victory

**Entry and scale.** The actor is the lawful command host, Gandhi is alive and ruling there under its explicit domestic constitutional mandate, and the full supreme-route entry contract was satisfied. Preserve the actual entry roster, industry denominator, distinct nuclear owners, usable-device count, delivery proof, and consent records.

**Achievement predicate.** The actor completes the exact terminal victory defined by the world-authority part. Every materially active sovereign country has a legally resolved status, interstate wars and independent strategic opposition have ended, real demobilization and disarmament duties are met, and the final 90-day stability interval completes. The shared world-end owner atomically accepts Gandhi's terminal result.

**Receipts and timing.** Unlock only from that committed terminal result and a matching actor lineage. Opening the congress, passing a vote, exceeding 1,000 Chaos, issuing demands, obtaining a nuclear arsenal, or winning the host's first war is insufficient.

**Disqualifiers.** Exactly 1,000 Chaos at route entry, paper devices, duplicated nuclear owners, unresolved microstates, forced player elimination outside a lawful settlement, or another terminal owner winning the race fails. Gandhi's death before terminal commit prevents this personal route.

**Continuity and art.** If lawful refuge changes the command host, the new host must receive the route's explicit mandate. It does not automatically inherit another human's personal attempt. Motif: a heavy central seal above a restrained globe, communicating imposed authority without claiming historical Gandhi approved it.

## ACH12. Defeat the supreme campaign and retain sovereign choice

**Entry and scale.** The actor is an independent opposition participant when an actual supreme campaign targets it or its accepted coalition. The coalition contains at least three independent states across two regions. The actor has not previously ratified the coercive mandate.

**Achievement predicate.** The supreme campaign records a genuine defeat, not merely an entry failure. The actor must have made a decisive recorded contribution through either a real military objective or the accepted opposition peace route. Military proof requires actor-controlled capture or defence of a named campaign objective that materially causes the defeat. Diplomatic proof requires its authored settlement accepted by the relevant opposing parties and enforced in the outcome. Preserve at least three original coalition members as sovereign countries for 90 days afterward.

**Receipts and timing.** Link threat, opposition commitment, actual contribution, authoritative defeat cause, surviving members, and postwar settlement. Unlock after the 90-day interval. An actor can qualify without killing Gandhi or destroying the ordinary League.

**Disqualifiers.** A self-created puppet opposition, an unopposed expiry with no actor contribution, a token equipment gift after victory, seizing an ally's proof, or a false nuclear-inventory report fails. The actor must not use a nuclear strike during the qualifying opposition campaign.

**Continuity and art.** Each player requires its own causal contribution. Another country's victory broadcast does not unlock the whole coalition. Motif: a cracked metal command crown above an intact plain civic banner. Keep the banner fictional and without text.

## Asset handoff

The motifs are composition briefs, not final artwork or approved source images. Produce one original transparent subject for each registered achievement. The color subject is centered on a 64 by 64 canvas. Derive grey from that same subject while preserving placement and alpha. The not-eligible source uses the unchanged supplied red-cross overlay.

Inspect the achievement contact sheet and exact consumer, then use the immutable achievement_template.png, achievement_template_grey.png, and overlay.png files from the current canonical template directory. Run process_achievement_icons.py on the complete state triplet. Final DDS files go directly under gfx/achievements/ with the exact registered achievement ID and its _grey and _not_eligible suffixes. Do not allocate final names or sprite aliases until collision and registration checks pass.

Retain source PNG, prompt, processing evidence, all three input layers, template hashes, decoded DDS checks, and a native-size contact sheet. Verify exact compositing, alpha, dimensions, and state correspondence. No generated border, fake checkerboard, painted red cross, text, or unrelated recolored subject replaces this workflow.

## Required future verification

| Scenario | Expected result |
| --- | --- |
| Promise accepted but transfer transaction aborts | No sovereignty or achievement receipt |
| Same liberation callback runs twice | One episode and one beneficiary credit |
| A tag is destroyed and later reused | No inherited beneficiary maturity or human attempt |
| A fascist holder changes ideology and control repeatedly | No second exception receipt and no refreshed deadline |
| A coalition member changes capital to another region | No fabricated region coverage |
| A human chooses one successor during whole-estate succession | One continuation, with no duplicated attempts among successors |
| A different multiplayer user takes over a successful country | Country evidence persists, personal attribution requires supported continuity proof |
| A device disappears through use or capture | No dismantlement credit |
| A launch is requested after the owner's arsenal becomes empty | No credible-veto achievement |
| Gandhi dies after a supreme mandate but before final settlement | Personal supreme victory fails, institutional route remains possible |
| Another world end commits first | No Gandhi terminal victory or achievement |
| Final stable-compliance callback repeats after loading | One permanent unlock |
| Render tool is unavailable but source checks pass | Report visual verification as unavailable, without inventing an asset review |

The parent should verify every predicate against an intentionally failing near-miss as well as a qualifying scenario. The meaningful risks are false credit, duplicated evidence, lost continuity, hidden-state leakage, and proof that never reflects a real world change. No campaign-balance, in-game, multiplayer, or asset-production result is claimed by this specification.
