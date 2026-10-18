# Actual near-completion improvement review

## Review status and scope

This is the actual near-completion design review of the assembled Event 112 Rise of Cossacks specification. It is distinct from the earlier historical research and fourteen-route proposal. All P01 through P14 proposals were accepted and integrated before this review began. None is rejected or deferred by this review.

The reviewer fully read all thirteen assembled gameplay and presentation parts from a frozen snapshot, totaling 536,387 characters. The exact copies, SHA256 values and complete character coverage are recorded in [the review manifest](review_input/manifest.json). The copies remain in `planning_work/planner/review_input/`. Reading was performed through complete bounded text outputs. A truncated attempt to read part 08 was discarded and its complete text was reread. The final coverage contains no unread interval.

Several findings were sent to the parent while the complete read continued. The parent accepted them and has begun or reported completing edits. An accepted disposition in this document records that decision. It does not certify the changed deliverable bytes. The final closure pass must read the actual deltas and inspect the later standalone prompts and research notes before closing the review.

The reviewer changed no deliverable during this pass. Only the review snapshot, coverage manifest and this planning review were written. The architect separately owns the resource and lifecycle audit. The curator separately owns documentation and asset consistency. Their actual reports are cross-referenced where they overlap these findings.

The current exposed tool metadata was searched for HOI4, probability inspection, focus or technology viewers, scripted GUI rendering and formable rendering. It exposed zero matching tools. This establishes a current tool-exposure limitation. It does not establish that an installed standalone viewer is absent or that a service is healthy. No live country, focus, GUI, map, raid, probability or campaign validation was performed. The checks below are design arithmetic and future acceptance requirements.

## Overall judgment

The country design has sufficient historical and political breadth. The five charters allocate real authority and obligations. The fourteen programs preserve regional differences through concrete service, representation, transport, training and receiving arrangements. The eight great projects change the scale and nature of government. Cossack Russia asks how a frontier service institution governs a national civilian society. The Golden Horde project asks how a Cossack founding army obtains mandates from distinct steppe and river institutions. The civic, military and service crown outcomes in Russia remain distinct from the commonwealth and imperial regency alternatives in the Horde project.

Further host trees, public resources, great projects, named people or super-events would add unnecessary scope. The remaining work is to make the accepted structure attainable, remove contradictory contracts, and bind its later political consequences to finite actions. The principal risks are progression rewards that depend on delaying earlier success, an opening industrial path that can disappear at its only building slot, and route text that names an outcome without a concrete action or recipient.

## Complete assembled read ledger

All filenames below begin with `112_rise_of_cossacks_spec_part_` and refer to the exact frozen copies in the manifest.

| Part | File suffix | Complete character coverage |
| --- | --- | --- |
| 01 | `01_core.md` | 0 through 18,139 |
| 02 | `02_hosts_and_geography.md` | 0 through 25,633 |
| 03 | `03_founding_and_shared_systems.md` | 0 through 94,807 |
| 04 | `04_charters_and_regional_paths.md` | 0 through 94,998 |
| 05 | `05_great_projects.md` | 0 through 51,759 |
| 06 | `06_military_and_economy.md` | 0 through 25,716 |
| 07 | `07_evolution_and_lifecycle.md` | 0 through 36,926 |
| 08 | `08_decisions_missions_and_events.md` | 0 through 23,516 |
| 09 | `09_countries_and_characters.md` | 0 through 21,689 |
| 10 | `10_focus_architecture.md` | 0 through 16,259 |
| 11 | `11_ai_balance_and_scenarios.md` | 0 through 18,710 |
| 12 | `12_presentation_and_assets.md` | 0 through 93,806 |
| 13 | `13_integration_and_acceptance.md` | 0 through 14,429 |

## Finding register

Priority High means a blocked required path, reward exploit or contradiction that changes actual play. Priority Medium means a missing finite contract or an ambiguous transition that an implementer would otherwise have to design. Accepted means the parent has selected the correction. Every item still requires the listed closure check against changed files.

| Number | Finding | Priority | Parent disposition at this handoff |
| --- | --- | --- | --- |
| NC01 | First-charter dependency cycle and early interface contract | High | Accepted, edits reported or in progress |
| NC02 | Regional completion thresholds reward delayed success | High | Accepted, edits reported |
| NC03 | National high-meter gates need their own finite political proof | High | Accepted, edits reported |
| NC04 | Service arrears can become a repeatable positive reward | High | Accepted, architect owns correction |
| NC05 | The one-state arsenal path needs preflight proof | High | Accepted, edits in progress |
| NC06 | Raid effects, diplomatic eligibility and icon meanings disagree | High | Accepted, edits reported |
| NC07 | Mission extension prices, durations and stacking disagree | High | Accepted, one shared extension guard selected |
| NC08 | Shared postwar work needs one price and one outcome owner | High | Accepted, parent is adding explicit precedence |
| NC09 | A training objective must have its template before completion | High | Accepted, edits reported |
| NC10 | A blanket war exclusion can block defensive diplomacy | High | Accepted, parent is clarifying valid wartime offers |
| NC11 | Three selected flag families lack reachable country identity acts | Medium | Accepted, edits reported |
| NC12 | Required exact formation defection needs an actual evolution outcome | High | Accepted, architect is updating the five-outcome pool |
| NC13 | Completed projects must release the active preparation place | Medium | Proposed clarification for explicit disposition |
| NC14 | Great-project first-peace and succession tests need finite action profiles | Medium | Core table and recovery accepted, supplemental exact tuning awaits disposition |

## NC01. First-charter dependency cycle and early interface contract

**Affected files and sections:** Part 03 sections 5.3, 6.2 and 6.3, part 04 Five basic charters, part 08 A01 and A02, part 10 FG01 and FG02, part 11 V01 and V05, with the matching part 07 continuity rules.

**Observed issue:** The original assembly required a first accepted civilian settlement and stronger C/J values. The ordinary civilian-council reward itself required an accepted charter. Part 04 also moved the temporary compact reward to initial ratification, although part 03's example used it before ratification. A one-state host could therefore need the result of a constitution to become eligible to establish that constitution. The military tree and an attractive national route cannot repair this opening dependency cycle.

**Accepted exact change:** Keep the free provisional compact at the immediate opening, granting at most +5 Cohesion and +2 Legitimacy once. Make the provisional civilian settlement available before a permanent charter. Its one shared quote has a 35 Political Power base. Three actual checkpoints become eligible no earlier than 30, 60 and 90 days after funding. They require representation, actual home and civil service, and sustained guarantees. Their maximum increments are C +5, +5 and +0, and J +8, +8 and +7, stopping at C60 and J50. The first ordinary council reward and state identity are included in the first checkpoint. They are not a second +1 C and +4 J payment.

At the deliberately conservative clamp-floor example, C35/J25 becomes 40/27 after the compact, then 45/35, 50/43 and 50/50 after the funded checkpoints. That supports a civilian charter after the day-90 survival objective and its separate 30-day ratification hold. The actual founding formula has a higher minimum Cohesion than this conservative check. A player may wait to fund the permanent assembly until the chosen charter is realistically attainable. The assembly does not launch automatically or expire while unfunded.

The receipt and unfinished objectives survive interruption and the survival mission timeout. They create no troops, equipment, building or fresh founding payment on restoration. The shared universal quote can exceed the base 35, so the initial 40 Political Power is not a guarantee of affordability under every modifier.

The primary interface uses five ordinary relevant actions plus at most one eligible emergency or status row. The same rule must govern parts 03, 04, 08, 10, 11 and the presentation handoff. It does not permit six ordinary competing action rows.

**Required closure check:** Read the actual changed bridge in part 03 and all consuming descriptions. Trace a one-state H12 with no sponsor, no evolution, no second council and no military raid from founding to the civilian charter. Confirm that the provisional work appears before the permanent charter, that its council reward is credited once, and that the 120-day assembly mission allows a genuine 30-day hold. Separately trace a late-funded assembly and a restoration with partially completed checkpoints. The five-plus-one display rule must agree in every final text and prompt.

## NC02. Regional completion thresholds reward delayed success

**Affected files and sections:** Part 04 P02, P07 and P09 full and limited outcomes, part 05 GP08, and their focus, achievement and scenario descriptions.

**Observed issue:** Passive C/J recovery stops at 60. P07 full completion required J65, while its limited outcome granted +5 J. Claiming that valid limited outcome at J55 could leave the country at 60. Delaying the same outcome until J60 could instead reach 65. P09's limited +3 J reached only 63 even when delayed optimally. P02's restricted +4 C reached 64 from the passive ceiling, while its full outcome required C65 and merit promotion could already have cost four Cohesion. The one-time M01 cadre reward could have been legitimately earned earlier, below 60. A generic H12 without an available migration or regional community also lacked a guaranteed path to the GP08 J65 gate.

**Accepted exact change:** Set full P02 Cohesion to 60, full P07 and P09 Legitimacy to 60, and the basic GP08 durable outcome to C60/J60. Preserve merit promotion, two actual formations, the command mandate, separate affected-community consent, completed construction, actual access, service rotation, guarantees and compliance periods. The correction removes an ordering exploit without reducing the meaningful political or material work.

These are the only P01 through P14 full-outcome meter gates above 60 in the reviewed snapshot. All five basic charters remain attainable at or below the passive ceiling once their real institutional requirements exist. Sponsor and socialist charters still need a consenting real counterpart. Their unavailability without one is an honest diplomatic condition.

**Required closure check:** Execute a design trace that claims every legitimate reward immediately when its real conditions pass. It must complete P02, P07, P09 and a one-state H12 regional endpoint without extra conquest, unrelated migration, purposeful arrears, peacetime raids or delayed reward collection. Read matching achievement conditions to ensure that no old threshold silently recreates the dependency.

## NC03. National high-meter gates need their own finite political proof

**Affected files and sections:** Part 05 common political proof and GP01 through GP06, with the route receipt and meter owner in part 03, the action catalogue and integrated scenarios.

**Observed issue:** Larger projects required C65 or C70 and J65 or J70, but their required preformation work had no explicit political reward budget. They could be reached in some campaigns through new state councils, host admissions and regional completion rewards. They were not reliably reachable when a diligent player had already earned those finite rewards below 60. Adding more unrelated programs or delaying existing rewards would make the meter, rather than the national political bargain, determine the campaign.

**Accepted exact change:** Within the already funded final constitutional mission, settle one finite endorsement budget after all real mandates, institutions, works, access and compliance conditions are complete. The baseline for each meter is the smaller of 60 and that branch's final gate. Raise only the missing portion to the chosen branch's final gate, with a maximum of +10 per meter. Values already at or above that gate receive no addition. Credit any earlier gain from the same mandate. The budget is once per GP across its variants and persists through reform, restoration and cosmetic changes.

| Project and branch | Baseline before endorsement | Maximum target | Why the political work is sufficient |
| --- | --- | --- | --- |
| GP01 Union | C60/J60 | C65/J65 | Three genuine ratified hosts, distinct regional representation and sustained fulfilled common obligations |
| GP02 civic Russia | C60/J60 | C60/J70 | Actual heartland civic representation, integrated states and the accepted national service settlement |
| GP02 military Russia | C60/J60 | C70/J60 | Real national staff, equipped army, fixed mandate and civilian budget authority |
| GP02 service crown | C60/J60 | C65/J65 | National assembly approval, an authentic institution and the first honored service or property guarantee |
| GP03 commonwealth | C60/J60 | C60/J70 | Genuine separate partner settlements, the river economy and a limited constitutional mandate |
| GP03 imperial order | C60/J60 | C70/J60 | Actual sovereign administrative base, congress authority, non Cossack settlement and sustainable command |
| GP04 council | C60/J60 | C60/J70 | National representation and two actual state settlements |
| GP04 hetman | C60/J60 | C65/J65 | Accepted executive mandate, legislative guarantees and national state work |
| GP05 Pontic network | C55/J60 | C55/J65 | Two real port agreements, inland connection and honored passage |
| GP06 Volga and Ural federation | C60/J60 | C60/J70 | Three ratified regional charters and fulfilled contribution and transit terms |
| GP07 eastern chain | C60/J60 | C60/J60 | No endorsement increment is needed |
| GP08 durable basic outcome | C60/J60 | C60/J60 | No endorsement increment is needed |

The endorsement adds no separate payment, mission, public resource, material grant or formation reward. A currently broken required promise still blocks it. A later loss does not reopen a used positive budget. The actual completion receipt distinguishes endorsement, final political act and presentation so reload cannot award all three as independent political rewards.

**Required closure check:** Test each row after every earlier lawful meter reward has been claimed immediately. Start at the listed baseline and complete only the project's own required work. Confirm exact endpoint values and one common receipt across every alternate constitution. Repeat the final act, change the variant, restore the country, and enter above the required gate. None may regenerate the budget. A breach after endorsement must use ordinary actual-loss recovery.

## NC04. Service arrears can become a repeatable positive reward

**Affected files and sections:** Part 03 sections 6.2 and 6.3, all service dispute repairs and their scenarios. The architect owns the canonical correction.

**Observed issue:** A missed installment cost 2 C and 1 J. Settling an actual unpaid service dispute granted up to 6 C and 2 J, once per dispute, with a Cohesion ceiling but no comparable legitimacy ceiling. If each newly missed installment generated a new dispute, deliberate late payment could produce net +4 C and +1 J repeatedly. That exploit could conceal the honest progression gaps in NC02 and NC03.

**Accepted exact change:** Recovery may restore only the actual unrecovered loss attributed to that specific missed obligation. Prior passive or other positive recovery credited to that loss reduces the remaining balance. Payment, dispute renaming, partial payment, restored country identity or a new review tick does not establish a new entitlement for the same missed installment. Genuine institution completion may have a separate finite outcome budget only when its actual work and owner are explicitly specified.

**Required closure check:** Trace an installment missed once and paid once, the same arrears checked repeatedly, several distinct installments, partial repayment, passive recovery before payment and restoration after payment. The combined attributable meter result can never exceed the honest on-time path. The national threshold fixtures must remain attainable after this exploit is removed.

## NC05. The one-state arsenal path needs preflight proof

**Affected files and sections:** Part 03 primary state viability and workshop bridge, part 01 playable opening, part 02 physical geography, part 06 E02, part 08 A03, part 09 country setup and part 11 V01.

**Observed issue:** The workshop bridge could add a military factory only if its sole state had a valid building slot at completion. A zero-MIL state with every slot occupied, or no usable factory slot, could still be selected without a proved alternative. E02 begins after basic production and cannot repair this dependency. A hypothetical future supplier is not a sustainable founding path when it can refuse or has no actual route.

**Accepted exact change:** Before admitting a primary state, prove one of three ordinary industrial paths. It has an existing military factory that can operate or be repaired, an actually usable free factory slot for the bounded workshop bridge, or a verified native CIV-to-MIL conversion path. A conversion produces its actual building result once and does not also receive the bridge factory. Material changes between selection and completion must revalidate the same path and preserve actual paid work. A state with no proved path is physically unavailable for this opening until an independently accepted adapter exists.

**Required closure check:** Add a no-MIL state with all slots occupied by civilian factories, a genuinely zero-slot state, a damaged existing MIL and a free-slot state whose slot is occupied during the mission. The first may use the verified conversion, the second fails preflight, the third repairs without a duplicate factory, and the last receives its declared cancellation or alternative disposition. No guaranteed donor or free extra slot is assumed.

## NC06. Raid effects, diplomatic eligibility and icon meanings disagree

**Affected files and sections:** Part 03 section 7.6, part 06 raiding table and following diplomatic paragraph, part 07 raid cases, part 08 A18, part 12 D14 and D15, and the standalone asset prompt.

**Observed issue:** Part 03 made R01 ordinary infrastructure disruption with no equipment capture. Part 06 described a depot or railway supply-point raid with capture. Part 12's D14 and D15 reinforced depot and corridor meanings that did not match the canonical pair. Part 06 also implied that a charter breach alone could permit a raid against a nominal partner, while part 03 excluded allies, own subjects, protected treaty partners and current truce partners.

**Accepted exact change:** R01 damages only the selected ordinary infrastructure consumer within its stated 0.5-level normal and 1-level critical bounds. It captures zero equipment. R02 is military-store recovery, with at most 400 actual rifles or 30 actual support equipment, never a second invented depot. The land baseline remains canonical. Coastal or river access is a separately verified R02 adapter. Railways, hubs, ports and facilities need their own inspected and accepted consumer before any R01 variant can target them.

The working decision icons become `prepare_infrastructure_raid` and `prepare_stores_raid`, preserving eighteen subjects. Use a road or ordinary bridge disruption cue for the first, and a finite military-store capture cue for the second. A railway demolition picture must not promise the unavailable railway consumer.

A political breach does not bypass diplomatic exclusions. The incompatible relationship must actually end or be amended, and the target must independently meet the valid war or dispute conditions before a raid can be prepared. The country and state are rechecked again at native resolution.

**Required closure check:** Read all R01/R02 references and both final art descriptions. Test a depleted store, changed owner, current ally, current subject, active truce and legitimately hostile former partner. Each route must retain one native raid instance, one native cost, its exact actual target and one outcome receipt.

## NC07. Mission extension prices, durations and stacking disagree

**Affected files and sections:** Part 04 common mission windows, part 08 A27 and the mission contract, later prompts and any timing scenarios.

**Observed issue:** Part 04 allowed a voluntary 60-day extension for 20 Political Power. A27 allowed a documented external-emergency extension of up to 30 days for 25 Political Power. Part 04 also allowed an external route-loss suspension up to 90 days. The package did not state which missions used each rule or whether they could stack.

**Accepted exact change:** A27 uses the global base of 20 Political Power for up to 60 additional days once on an eligible civil or program mission. There is no separate 25 PP and 30-day profile. One free suspension for a genuine external loss can last up to 90 days as an alternative under the same one-extension guard. The two cannot stack on one mission. A route's separate evacuation or operational crisis window retains its own purpose and does not automatically become another extension of the original work. Native raid timings cannot use A27.

Use the inspected signed native timeout adjustment and preserve the actual elapsed objective. Do not remove and recreate a mission to reset it. Queued first-peace reviews have no running timer until admitted to an available mission place.

**Required closure check:** Exercise a paid extension, an external suspension, an attempted second extension by the other route, an already extended native raid and a saved game during suspension. Confirm a single guard, exact quote, truthful remaining time and success precedence at the adjusted deadline.

## NC08. Shared postwar work needs one price and one outcome owner

**Affected files and sections:** Part 04 common first-peace contract and all fourteen reviews, part 05 national reconstruction, part 06 E04, part 08 A19 through A21 and part 10 FG20.

**Observed issue:** Each P program has a named first-peace price and duration. E04 says a common 60 PP, 180-day reconstruction mission supports each major postwar settlement. A21 repeats that profile. Part 04 correctly says identical P and GP promises should merge, but it does not explicitly say which price and timer governs that merged mission. An implementer could charge the named review and then the generic reconstruction fee for returning the same unit and repairing the same civilian facility.

**Exact proposed change:** E04 and A21 are the default profile only when no more specific original obligation owns the work. The commitment that first created the actual promise supplies the controlling price, duration and outcome. A linked regional or great-project review records fulfillment from that same receipt without another fee, construction requirement, return order, C/J penalty or completion gain. The mission may display both political consequences. Physically distinct promises retain their separately disclosed objectives and actual ordinary construction or delivery costs.

For example, a P01 veteran and municipal review that also fulfills GP02's promise to those same veterans uses the P01 45 PP profile and the declared combined objective window. It does not charge another 60 PP simply because E04 displays the reconstruction. A new promise to a different national industrial district can use the ordinary 60 PP default because that is genuinely new work. P03 and GP04 must likewise share an already promised Kuban land and regional-budget settlement.

**Required closure check:** Trace P01 plus GP02, P03 plus GP04, P09 plus GP06 and a module plus GP08. For one real promise, record one quote, one paid work receipt, one possible breach and one recovery loss balance. For two distinct promises, show the two actual recipients and why each objective exists. Every active cost must remain visible under the mission and commitment limits.

## NC09. A training objective must have its template before completion

**Affected files and sections:** Part 06 M02 and M05, T02 and T04 definitions, part 08 A05, part 10 FG06 and part 09 technology and focus loading.

**Observed issue:** M05 required production of the T04 equipment allowance and training a mobile formation before the program awarded T04. M02 similarly needed an infantry training objective whose exact accepted template relationship was not explicit. A player should not need an undisclosed alternate template or an extra Army Experience workaround to perform the very training the program is meant to enable.

**Accepted exact change:** Unlock the provisional accepted T02 or T04 template when its funded training stage begins, after the actual technology and capability preflight. It creates no unit, manpower, equipment or training result. The ordinary recruitment and training system supplies the actual formation. Completion awards the capability receipt and selected institutional or doctrine benefit once. Existing valid paid training is recognized through the receipt, and a failure cannot delete an actual army or create a replacement.

**Required closure check:** Start M02 and M05 on a fresh carrier that has never possessed T02 or T04. Confirm that the actual required template is available before any mission objective asks for it, that native equipment and training remain paid, and that completing, canceling or restarting the stage never grants a free formation. Check that the initial cavalry and infantry recipes remain usable before the mature templates exist.

## NC10. A blanket war exclusion can block defensive diplomacy

**Affected files and sections:** Part 04 Partners, refusal, and the first peace, especially P02, P06, P08 and P10, plus part 08 diplomatic response contracts and part 11 AI offer scenarios.

**Observed issue:** The common paragraph says that a current war makes offered terms invalid. Read literally, any current war could invalidate a defense compact, socialist service negotiation or coalition precisely when its route is meant to be available. A war against a third party is different from a mutually incompatible war between the negotiating parties.

**Exact proposed change:** State that only a war relationship incompatible with the particular offered terms invalidates their execution. A common defensive war, war against a third party or separately valid wartime support agreement can qualify the offer. Talks between direct enemies may propose recognition or a war settlement, but the treaty and physical contributions take effect only through the actual supported native diplomatic result. An invitation alone never ends a war or supplies consent.

Retain the real exclusions for a contradictory patron obligation, unresolved material breach against the counterpart, impossible route or unaffordable contribution. AI validity must evaluate those specific facts before choosing among accept, counteroffer and refuse.

**Required closure check:** Use three separate cases. Two hosts fighting a third party can negotiate a valid limited defense compact. A host and its direct enemy can negotiate only through a supported conflict-settlement route. A nominally friendly sponsor with an incompatible exclusive contract cannot accept a contradictory new promise. No case invents a ceasefire or automatic war entry.

## NC11. Three selected flag families lack reachable country identity acts

**Affected files and sections:** Part 05 GP05, GP06 and GP07, part 09 identity transitions, part 12 FL18, FL19 and FL20, and the asset prompt.

**Observed issue:** The presentation inventory selected Pontic, Volga-Ural and eastern state flag families, while the corresponding great projects could finish as treaties or networks. The curator correctly prevented an ordinary treaty from changing a member's national flag. That safeguard left the selected sovereign or federal flag consumers without an explicit reachable principal-country transaction.

**Accepted exact change:** After full GP05, GP06 or GP07 and its first-peace review, offer an optional principal-country constitutional identity act. It costs 75 PP and uses a 120-day mission, with C60/J60, the actual owned and controlled regional base, ratified home citizenship and mandate, and partner acknowledgment that the new name does not expand any existing obligation.

For Pontic identity, prove the required two ports and inland link under the accepted direct-ownership predicate. For Volga-Ural identity, prove two distinct actual anchor states spanning G07 and G08. For eastern identity, prove two actual station states including the Omsk base. The final canonical text must state exactly which anchors the principal must directly own and control and which outer connections remain treaty predicates.

Only the principal's valid cosmetic identity and flag change. No new country tag, member annexation, core, population, unit, resource, meter gain or second formation reward follows. A treaty-only ending retains every national flag. Earlier contributions and unresolved obligations remain attached to their actual owners.

**Required closure check:** Follow each of FL18, FL19 and FL20 from a legal completed treaty project into its optional country act. A missing direct anchor, unratified home mandate, refusing partner or active first-peace dispute must block that act with a concrete reason. Keeping the treaty outcome must remain a complete playable result. Repeat and ideology-change cases must use the same identity receipt and approved flag ladder.

## NC12. Required exact formation defection needs an actual evolution outcome

**Affected files and sections:** Part 03 formation transfer contract and F42, part 07 outcome pool and runtime limits, part 08 report inventory, part 12 WR40, part 13 required dependencies and the achievements prompt.

**Observed issue:** Part 13 described exact formation defection as selected required content. Part 07 still called it optional until verification and offered only four director outcomes. Merely changing the word optional would not put an actual formation into the weighted opportunity pool. A personnel volunteer fallback would not preserve the distinct promised unit outcome.

**Accepted exact change:** Use five explicit surviving outcome weights before normalization: new rising 32, state defection 28, personnel volunteers 20, exact formation defection 10 and existing host compact 10. The exact formation candidate uses a real existing unit, with its observed manpower, equipment, experience and unique commander ownership. It does not require fictional free donor manpower to represent people already in that unit. It does not silently downgrade to a material or personnel reward.

The native preservation proof remains a required implementation gate. Until it is met, the full package cannot claim this accepted surface is implemented. The planning document can honestly describe the unresolved native binding. The existing 67-report inventory already has a distinct unit-defection report, so the correction needs a recipient and actual receipt mapping rather than another report family or illustration.

**Required closure check:** Test the complete five-outcome pool, each invalidated candidate, a source with zero free manpower but a real eligible unit, an understrength unit, a commander owned elsewhere, a receiver annexed during preparation and the 90-day new-host limit during the day-14 bootstrap. Update the arithmetic example, scenario inventory and the achievement predicate to the same canonical five classes. A formation transfer must not also receive the volunteer grant.

## NC13. Completed projects must release the active preparation place

**Affected files and sections:** Part 05 selection and continuity rules, compatibility table, GP05 through GP07, part 08 A22 and A23, part 10 route continuation and the optional identity acts in NC11.

**Observed issue:** The common project-change rule is explicitly described before constitutional settlement. Later passages allow a completed Pontic network alongside the Union, and a completed Volga-Ural coalition to become a foundation for Russia or the Horde. The exact treatment of the active principal-project place after successful completion is not stated. A literal lock could prevent these accepted compatible developments, while an unrestricted reset could repeat old rewards or erase old promises.

**Exact proposed change:** Completion closes the active preparation and its paid mission, preserving the completed project in history and its live agreements in the registry. A compatible new project can then be selected without pretending to abandon the completed one. A23's 50 PP and 180-day elective-change rule applies when abandoning funded unfinished preparation. It does not charge a second abandonment price for a completed network. Starting the next project still pays its own listed preparation price.

An incompatible constitutional or national identity transition uses the actual charter-change and new national-settlement contracts. It cannot retain contradictory powers or repeat a used outcome. A completed network's optional identity act uses the same active preparation capacity while it runs and retains all earlier treaty limits.

**Required closure check:** Complete GP05, retain its valid port treaties, and begin GP01. Complete GP06 and begin GP03 while seeking any genuinely expanded mandate. Complete a national project and attempt an incompatible second identity. The first two routes remain reachable with live obligations preserved. The last cannot apply both exclusive constitutions or receive an old grant again.

## NC14. Great-project first-peace and succession tests need finite action profiles

**Affected files and sections:** Part 05 all first-peace, mandate, tribute, succession and failure passages, part 06 E04, part 08 A19 through A21, part 09 succession and part 10 FG20.

**Observed issue:** Part 04 gives each regional program an explicit first-peace price, objective, failure and recovery. Part 05 describes several national tests without all those fields. Examples include the smaller sustainable Union benefit, the Horde's visible legitimacy penalty until its first peace, the cost of continuing an emergency, and the precise restoration of a blocked national institution. These passages contain good political content, but the implementation owner would still have to choose numerical consequences and timing.

**Exact proposed change:** Add a compact owner table that uses the existing A20 mandate-review profile of 60 PP and 120 days, or the A21 reconstruction profile of 60 PP and 180 days. An already specific P obligation takes precedence under NC08. A first-peace review becomes due after 60 consecutive days of peace and a secure administration following full completion, including a project formed during peace. It uses the first free mission place without an invisible expiry. A real earlier blockade, loss or breach uses its own emergency handling and does not erase the later constitutional obligation.

| Project | Existing action profile | Required distinctive work |
| --- | --- | --- |
| GP01 league or federation | A20 mandate review | Return or renew actual common command, settle one contribution dispute, and obtain the affected members' response. A lawful refusal or exit remains lawful |
| GP02 civic Russia | A21 reconstruction | Complete the actual veteran or industrial-district settlement and return a formation whose service mandate expired, or obtain a new accepted mandate |
| GP02 military Russia | A20 mandate review | A real civilian budget hearing, current staff succession and a bounded command renewal or demobilization |
| GP02 service crown | A21 reconstruction | Fulfill the named land or service guarantee and confirm the accepted assembly and institutional succession procedure |
| GP03 commonwealth | A21 reconstruction | Revise a concrete unequal contribution or transit obligation with the actual affected counterpart and perform the agreed work |
| GP03 imperial order | A20 mandate review | End or expressly renew the exact wartime tribute and deployment mandate, preserving the guaranteed local institutions and receiving the real subject response |
| GP04 council or hetman | A20 mandate review | Resolve the actual national executive mandate and land or service promise, preserving separately guaranteed Kuban powers |
| GP05 Pontic network | A21 reconstruction | Restore the actual civilian passage, receiving or port obligation and release transport from an expired expedition |
| GP06 Volga-Ural coalition | A20 mandate review | Ask which original purposes are fulfilled, ratify new common revenue only with consent, or implement a lawful smaller coalition |
| GP07 eastern chain | A21 reconstruction | Complete a real station maintenance obligation and return the promised ordinary civilian authority while retaining a viable route |
| GP08 regional or refuge outcome | A21 reconstruction | Complete the actual home or receiving settlement, service or property obligation, and safe continuing status |

Use one shared charter-breach result of -10 C and -8 J only when the country actually repudiates an accepted promise. Replace GP01's unbounded phrase at least 10 Legitimacy with that exact owner contract unless the parent explicitly selects a different bounded severity. A missed civilian administrative review without a material charter breach can suspend its conditional benefit and cost 4 J once. It does not invent a war or remove an army.

Where no more specific P repair exists, A19 recovery costs 60 PP, permits 150 days, requires the actual obligation to be fulfilled or consensually amended, and then requires 30 days of compliance. It restores only the remaining actual loss and the benefit whose conditions are true. This does not grant a fresh formation reward. A completed peaceful Union replaces its temporary 5 percent coordination benefit with one sustainable 3 percent version in the same slot, if that native modifier is the accepted binding.

For the Horde, replace an undefined automatic legitimacy penalty with an explicit unresolved tribute or emergency-mandate status. Its actual refusal, expiration or unilateral continuation uses the same exact breach contract. Successful settlement closes that status and retains the selected institutional benefit. This keeps imperial pressure tied to an actual political obligation rather than an unexplained permanent meter drain. If the parent retains a separate initial penalty, its amount, cause, loss receipt and recovery must be stated exactly instead.

Leadership succession uses the current charter's actual authority and a functioning interim institutional office. It may reopen a genuinely new command mandate. It cannot regenerate the first-peace reward or require a missing named person. A successor's new breach and its recovery need a new actual cause, with all old promises preserved.

**Required closure check:** Follow one full first-peace review and one failed review into recovery for each row. Test a project completed during peace, a review queued behind an evacuation, an accepted partner exit, a renewed war, a lost capital, and succession without a verified named candidate. Every branch must have a visible cost, timer, actual objective, responsible actor, precise failure and attainable recovery.

## Five-charter and fourteen-program viability crosswalk

The following assessment assumes the accepted finite founding bridge and threshold corrections are present in the final files. It does not claim a live campaign has been run.

| Charter | Meter route | Independent non-meter requirement | Viability conclusion |
| --- | --- | --- | --- |
| Civilian council | Bridge reaches C50/J50 | Actual military and civilian representation | Available to a viable one-state H12 without conquest or patron |
| Confederated council | Bridge plus ordinary fulfilled-service recovery toward C55/J50 | Two genuine institutions with separate constituencies | Can be local to one state without pretending to be the three-host Union |
| Professional ataman | Ordinary recovery reaches C60/J45 | Trained command cadre and a real recorded mandate | Can wait before funding the assembly, preserving the full hold window |
| Socialist service | Bridge reaches C50/J45 | Real consenting socialist counterpart and accepted civil terms | Deliberately conditional on a genuine feasible agreement |
| Sponsor service autonomy | Bridge reaches C50/J45 | Actual sponsor contract, protected home administration and deliverable obligations | Deliberately conditional on a genuine feasible agreement |

| Program | Full meter gate after accepted correction | Distinct required work retained | Honest completion path |
| --- | --- | --- | --- |
| P01 Don civic | C55/J60 | Rural and town representation, real budget work, accountable reserve | Ordinary recovery reaches gate, finite political reward follows |
| P02 professional | C60/J50 | Merit staff, two actual formations, live mandate | No need to delay M01 or restricted completion |
| P03 Kuban | C60/J60 | Affected communities, connected economy, infantry and mounted exercise | Requires actual force and geography, with no meter above passive ceiling |
| P04 Black Sea return | C55/J60 | Actual corridor, accepted receiver and measured group | Can retain limited contact if the community refuses movement |
| P05 Sich | C55/J60 | Civic register, crossing and workshop, two territorial formations | Narrow service-only settlement remains visibly limited until rights change |
| P06 socialist service | C55/J55 | Real delivery or production and mutual compliance | Refused patron terms preserve the independent or provisional path |
| P07 reciprocal Terek | C55/J60 | Two affected authorities, shared work and honored passage | Full agreement no longer depends on delayed limited reward |
| P08 service Terek | C60/J55 | Defensible line, home reserve and actual sponsor compliance | Lawful refusal of unrelated service remains possible |
| P09 Ural commons | C55/J60 | Resident access, real outlet and sustainable seasonal service | Full agreement no longer needs an unrelated legitimacy source |
| P10 Yaik coalition | C55/J60 | Two different pledges, actual force, revenue and delivered reform | Ending the initiating crisis does not erase valid paid negotiations |
| P11 Danubian refuge | C50/J55 | Actual receiving work, measured survivors and supported coastal capability for full outcome | Shore-based safe refuge remains a complete limited result |
| P12 Nekrasov sanctuary | C45/J60 | Voluntary community decision, work and honored guarantees | No military levy or sovereign country is necessary |
| P13 Siberian network | C60/J55 | Two actual anchors, measured shipment and working connection | A smaller commercial link survives refusal of troop transit |
| P14 exile integration | C60/J60 | Real community, mandate, actual contribution and institutional service | Missing named people do not block the institutional alternative |

All fourteen programs have finite full and limited outcomes and a named first-peace recovery in the reviewed snapshot. The accepted threshold corrections preserve that content. The larger projects can use their real receipts without replaying the same construction or military transfer.

## Timing and affordability trace for the small protected host

The initial 40 PP, 35 PP provisional settlement, 60 PP workshop and 60 PP initial assembly imply a meaningful early opportunity cost. A simple controlled design fixture can assume one net PP per day after every native modifier and no discretionary spending. This is a fixture assumption, not a measured engine income.

Funding the provisional work on day 0 leaves 5 PP. With the AI's ordinary 20 PP reserve, the 60 PP workshop becomes affordable on day 75, leaving 20 PP. The 60 PP assembly becomes affordable on day 135, again leaving 20 PP. If the actual bridge, supply and charter objectives are satisfied, a fresh 30-day ratification hold can finish on day 165 within its 120-day mission. The workshop still needs its valid physical consumer and its own actual completion. This trace shows that an ordinary arsenal-first priority can fit within the first year without a free second starting budget.

A different universal quote or native income changes the dates. The AI may wait or reprioritize actual urgent defense. The design must not force an unfunded assembly timer or claim that these calculated dates are engine performance. Military training also requires its real Army Experience and equipment. The arithmetic does not assume those arrive with time alone.

## Native integration, geography and conservation conclusions

The assembled package correctly keeps exact map membership, state geometry, province bindings, consumer lookup and installed native behavior as explicit future dependencies. It distinguishes a treaty anchor from owned and controlled territory, an existing country from a release slot, and a political exile identity from verified native government-in-exile functionality. Those distinctions should remain intact through every correction.

The selected exact formation branch is a required complete-package surface, even though its native proof remains outstanding. Civilian return is likewise selected optional player content with required implementation for its accepted modules. A planning conclusion that those branches are specified is appropriate. A claim that the native systems, live unit preservation, historical people or map geometry have been verified is not.

The principal root remains Fire-Once. The prefire evolution changes the opening context and permits one bounded day-14 opportunity. It does not create a second founding army. The founding starts the new-host cooldown, so a second independent host remains unavailable on day 14. The five-outcome correction must preserve this timeline and revalidate actual material or unit candidates.

Defeat retains only actual surviving people, equipment, countries, characters and obligations. The reviewed lifecycle does not erase prior workshop or opening receipts and does not regenerate an army on restoration. The main remaining defeat check is closure of each newly clarified mission, endorsement and identity act against those same tombstones and actual custodians.

## Required disposition and closure handoff

The parent should record a decision for every NC item, apply accepted text changes and then request the closure pass against the assembled current package and standalone prompts. The review should be promoted into the final specification's review and disposition appendix with its original finding numbers preserved. The frozen input and exact changed-file coverage are planning evidence, not gameplay test results.

The closure pass must read every changed interval and every newly supplied prompt in full, reconcile route, achievement, super-event and asset predicates, and confirm that no accepted finding is merely described as future design work. Native implementation, production, installed-map, probability and live-game acceptance gates remain future work under their proper owners.

Once those finite corrections are closed, no additional broad expansion pass is recommended. The accepted design already supplies the requested regional depth, national alternatives, evolution, modernization, diplomacy and recovery. The remaining implementation work should follow those concrete contracts and produce the required evidence.
