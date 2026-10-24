# AI, dynamic tuning, and Chaos

## Status of the numbers

This file specifies initial tuning proposals and required behavior. No probability, engine, or balance result has been measured in this planning session. All factors must be centralized and checked against the actual shared owners and native AI semantics before implementation is accepted.

Bloc cohesion is the only persistent public custom numeric value. Native state, army, economy and diplomacy values remain native inputs. Shared camp, Deaths, Migration, Resistance and Condemnation values stay in their owner surfaces. Current eligibility conditions can be explained as facts and missing requirements without inventing a second readiness score.

## Dynamic cost and time model

Select the action's concrete package first, such as a local protection agreement, a frontier client, a port relief route, or a multi-region command commitment. Derive the quote from that package's actual inputs. A small state can contribute a smaller useful force or a different role. It cannot receive the same outcome for zero material cost because a scaling factor fell below zero.

| Tuning input | Proposed influence | Bound and explanation |
| --- | --- | --- |
| Actor economic scale | Material package size varies with usable civilian and military industry and existing obligations | Normal contribution multiplier 0.5 to 2.0 around a medium actor. Availability still requires the actual quoted resources. |
| Current military scale | Campaign and aid packages follow useful formations, equipment deficits and reserve needs | Do not charge for more units than the operation can employ or transfer more than the donor can spare. |
| Route difficulty | Distance, hostile transit, damaged transport, naval exposure and inland access change transport and time | Duration factor 1.0 to 1.75 for ordinary routes. No route means invalid, not an arbitrarily expensive valid action. |
| Administrative capacity | Current control, local institutions, inherited administration and resistance change setup time | Duration factor 0.8 to 1.5. An authority failure blocks the action instead of multiplying its cost indefinitely. |
| Preparation | Completed relevant supply, reception or institutional work reduces repeat setup | Duration factor 0.75 to 1.0. Only a real reusable asset counts. Prior preparation never duplicates its reward. |
| Current emergency | An actual endangered front or closing route prioritizes an achievable response | Can shorten a local mission into a 30 to 60-day emergency band. Large construction or impossible transit remains impossible. |
| Existing commitments | Overlapping factory use, assigned forces, fuel and deliveries limit new work | A resource cannot be pledged twice. Partial uncommitted capacity can fund a smaller separately quoted operation. |
| World Chaos | Raises strategic pressure and willingness to accept risky political options | It can shift eligibility timing and bounded risk preferences. It does not create equipment or fabricate victim counts. |

A normal mission duration starts from its 90, 120 to 180, or 180 to 365-day anchor and applies only relevant factors, then clamps to its stated band. A focus uses its supported 35, 55 or 70-day anchor and a source-verified duration mechanism. Costs and time are rounded consistently by the shared owners and shown before commitment. Stored date offsets use the project's date conversion helpers, not raw subtraction of a day count from an internal date value.

## Cohesion tuning

| Cause | Initial anchor | Repeat guard | Consequence and reversal |
| --- | --- | --- | --- |
| Valid founding authority | Set to 50 | Once for the founding episode | Sets a starting condition, not a recurring reward. |
| A new government fulfills its first compact contribution | +5 | Once per genuine member accession and charter episode, with no gain from rapid rejoining | Makes normal coordination more reliable. |
| A promised common defense is actually delivered | +10 | Once per documented defense episode, with a 180-day actor-pair guard | Repairs a real obligation. Sending the same aid again cannot repeat the milestone. |
| A disrupted essential supply agreement is restored | +5 | Once per actual interruption and repair episode, at most +10 from this family in 180 days | Restores confidence after material recovery. Deliberately toggling access is not a qualifying interruption. |
| A due material promise fails without an agreed revision | -5 to -10 | Once at settlement of that promise | Negotiated correction or a later fulfilled replacement can recover some confidence. |
| A full member leaves or refuses a major common charter | -10 | Once for the departure or charter dispute | The government also stops contributing current capacity. A free rejoin does not cancel all effects. |
| A strategically important client is lost | -10 | Once for its actual government or regional loss episode | Regaining a flag is insufficient. Restored authority and supply are required for recovery. |
| Founder command collapses | -25 | Once for that leadership collapse | A recognized successor can rebuild coordination through actual commitments. |
| Unilateral target expansion violates a negotiated compact | -15 | Once per disputed charter revision | Assent, narrower agreement, split, or withdrawal resolves the dispute. |
| Current recognized succession is completed | +10 | Once per distinct leadership vacancy, no gain from voluntary leader swapping | Starts the new common command durability record. |

Clamp cohesion to 0 to 100. Several consequences of the same episode can be real, such as lost client capacity and lost confidence, but they must not apply the same cohesion debit twice through an annexation hook and a monthly review. A review discovers unmet conditions among explicitly registered active actors and settles each episode once. Do not implement that review as `on_daily`, `on_weekly`, or `on_monthly` without explicit user authorization: those hooks iterate over all countries by default. Use bounded owner callbacks or a specifically authorized active-record dispatcher; if an all-country recurring pass is indispensable, leave it unresolved pending explicit authorization.

## Actor strategy matrix

| Actor and current condition | Highest priorities | Conditional choices | Rejected or low-priority behavior |
| --- | --- | --- | --- |
| Founder with strong industry, reliable access and divided but manageable institutions | Secure command, maintain a defensive reserve, deliver first commitments | Concentrated command when it can fund obligations, negotiated order when sovereignty disputes dominate | Distant unsupported wars, empty clients, simultaneous maximum commitments |
| Founder with weak military capacity and potential partners | Preserve a viable state, negotiate useful access, build one attainable contribution | Negotiated order, limited partner arrangements, regional restraint | Spending its last equipment on prestige or demanding an immediate global campaign |
| Founder whose charter threatens key domestic institutions or whose movement has lost military support | Resolve the political crisis and preserve surviving authority | Negotiated withdrawal or rupture, depending on compliant institutions and loyalist control | Automatic perpetual hardline policy despite no enforcement capacity |
| Full member under direct attack | Defend its current theater and request promised support | Continue compact if support is delivered, renegotiate or leave if abandoned | Sending its entire army overseas while its capital is undefended |
| Compatible but threatened prospective member | Assess actual targets, protected communities, existing wars and sovereignty | Limited cooperation or refusal, conditional membership after a meaningful charter settlement | Joining from a shared religion alone |
| New frontier client | Capital defense, supply, affordable replacements | Delegated authority when support is reliable, local consolidation or independence when it is not | Starting another client or campaign before its own base is viable |
| Port client facing route loss | Preserve port and transport, seek alternate supply, reduce commitments | Defensive independence or negotiated break | Naval invasion without ships, convoys, support or an eligible route |
| Interior client without transit | Local sustainment, negotiate access, reduce external obligations | Independent adherence or repudiation if sponsor demands remain impossible | Treating a nominal alliance as actual passage through a neutral country |
| Independent adherent after founder defeat | Protect real territory and forces, settle local command | Regional campaign or a new compact with current agreements | Resetting to the old founder's strategy, receiving another starting army, counting old allies as available |
| Threatened government with an army and allies | Defense, protection agreement, feasible counteroffensive | Relief and reception matching capacity, support for resistance | Accepting a mission it cannot reach, dissolving its existing faction for a symbolic compact |
| Distant protector with industry or shipping | Reception, transport, material aid, diplomatic protection | Military intervention when a genuine theater and force exist | Promising unreachable land liberation as its only useful response |
| Repudiating successor | Stop persecution, secure authority, fulfill custody and relief obligations | Defensive guarantees, recognition and recovery | Keeping doctrine-dependent bonuses while claiming completed reform |
| Terminal crusader government | Sustain assigned theaters and current common commitments | Replace a lost route, negotiate resources, defend or renew leadership | Treating the terminal state as free victory or ignoring surviving opponents |
| Terminal opponent | Preserve viable states and populations, isolate and defeat sustaining governments | Shelter, resistance, coalition support, local settlements | Assuming founder capitulation ends all crusader actors |

## Route and action score proposals

AI validity is a hard gate before scoring. An invalid route has zero willingness and cannot be selected through a minimum-weight floor. Among valid options, start with score 1.0 and use a small documented factor set. A primary strategic fit can receive 2.0, a useful secondary fit 1.0, a costly but plausible alternative 0.5, and a strongly disfavored valid option 0.1. These are relative design anchors, not probabilities.

For a well supplied founder, concentrated command can receive the primary fit when it has actual capacity to honor obligations and members accept that arrangement. Negotiated order receives the primary fit when strong potential members resist subordination or the leader depends on their routes. Rupture receives the primary fit only with a capable internal opposition, an untenable charter conflict, or severe current loss of enforcement and support. Ideology does not override missing institutions.

For clients, delegated authority is favored by delivered aid, usable access and acceptable demands. Independent adherence is favored by local sustainment, sponsor failure and continuing doctrinal commitment. Repudiation is favored by a capable alternative authority, unacceptable expanded targets, credible protection, or defeat that breaks the movement's governing base. None of those routes is a random cosmetic skin.

Protection and relief scores use proximity to threatened people, existing promises, route feasibility, available transport, usable receiving capacity, domestic pressures and competing wars. A country should not repeatedly choose an action with an unpayable price. It can choose a smaller useful package, request support, or close a task honestly when no viable role remains.

The auditor must establish whether a surface uses a weighted event selection, independent focus score race, native decision willingness, MTTH, or a custom pool. Scores cannot be normalized as weight divided by sum unless that is the actual selection model. Do not report a willingness score as the chance a country will click a decision.

## Campaign and target selection

Military targets are selected from current reachable political opponents. Evaluate a limited local theater before a remote expansion. Existing war obligations, protected states, supply routes, military strength, and the political cost of attacking a protector matter. A target group's geographic presence alone is not a sufficient war plan.

The demographic target charter is authored political content with valid identity data. The AI does not search the world for the largest vulnerable group or use expected civilian deaths as a maximization objective. Purity Doctrine selection considers the movement's internal politics and the resulting alliance and domestic conflicts. It cannot choose an unsupported classification simply because it would produce a larger enemy pool.

The membership AI preserves current government identity. Religion can inform a proposed relationship only alongside route, sovereignty, actual targets, protection obligations and military interests. Malta, the Holy Realm and SPARTA require their specific developed direction to be inspected. Their event numbers do not confer compatibility.

## Harder player crises

Apply the project's mandatory harder-crisis behavior to supported pressures when a player is directly involved. For a player leading the crusade, threatened governments prioritize viable protection and coordinated defense more strongly. For a player resisting the movement, capable hostile governments prioritize relevant campaigns and honor feasible support commitments more reliably. These changes remain within valid resources and routes.

An initial proposed pressure factor is 1.15 on the relevant strategic priority, capped at 1.25 across overlapping player-pressure causes. It affects willingness or scheduled attention, not physical population loss, hidden prices, free factories or spawned equipment. A pressure factor cannot make an invalid action available. The probability auditor must check that the result remains challenging without creating a deterministic pile-on or starving other active wars.

There is no event-specific toggle for this behavior. Existing global settings continue under their owners. Exact current conditions and paid costs remain truthful to the player.

## Chaos impact map

Event-owned Chaos represents the distinct political and institutional spread of this abnormal international order. The shared owners already account for ordinary war, conquest, military buildup, deaths and other generic consequences. Each event-owned source must name the additional material change and a unique episode receipt. If the shared owner already records that same political change, this event row contributes zero and references the shared receipt.

| Material cause | Proposed event contribution | Dynamic basis | Repeat guard and overlap rule | Containment or reversal |
| --- | --- | --- | --- | --- |
| First actual capture of governing authority by the militant order | +5 to +10 | Existing country importance, real institutional reach and international exposure | Once for the founding episode. No grant for a failed preview, candidate selection or narrative rumor. | Actual early suppression can reverse part of this political contribution, without undoing shared deaths. |
| First operational transnational persecution compact | +5 to +10 | Real member governments, enforceable obligations and demonstrated cross-border reach | Once for the first sustained compact. A native faction creation alone is insufficient and its generic Chaos is not repeated. | Genuine breakup of the operational compact can reduce the outstanding event-owned spread contribution. |
| First durable independent persecuting client in a new world region | +5 to +10 | Viable local government, supply, institutions and military independence | Once per unique region for the episode after tenure. Release and annexation events do not pay it again. | Destroying or repudiating the sustaining government can reverse the corresponding current institutional spread, once. |
| A regional network becomes a durable multi-region governing order | +10 to +20 | Current real authorities and political reach, not raw unit count or civilian deaths | Once for the first broad governing milestone. Military buildup and conquest remain shared. | Loss of the durable network reverses only the still-outstanding event-owned political contribution. |
| A doctrine dispute creates a new capable independent persecuting government | +3 to +5 | A real new political rupture with continuing control and forces | Once per actual schism, capped at two such sources for this event episode. Evolution activation itself is zero. | Defeat or repudiation settles that schism's source. |
| A protection arrangement collapses and exposes a previously protected region to a real crusader authority | +3 to +5 | Lost enforceable protection and a new political opportunity actually used | Once for a distinct protection episode, capped at two per episode. Do not add this for the same political transfer already credited as a regional client milestone. | Restored protection can settle the outstanding source. Losses already suffered remain. |
| Shared deaths, wars, annexations, ordinary faction changes, famine or migration consequences | 0 additional from Event 115 | Shared systems' own actual outcomes | Reuse the owner's source. Never repeat the same deaths or physical movement in an event wrapper. | Shared owner decides its reversible and irreversible consequences. |
| Purity Doctrine eligibility, activation, logging or branch unlock | 0 | No independent material outcome yet | Always zero for these administrative changes | No artificial negative grant for disabling the evolution. |
| Final Crusade eligibility or terminal declaration | 0 artificial threshold grant | Current world position and shared terminal transition | Never push the meter above 1000 to create eligibility | Final war consequences continue through shared systems. |
| Complete ordinary or terminal defeat of the movement | Request negative settlement of the outstanding event-owned political sources, bounded by what this episode actually added and subject to the shared meter accepting the change | Current defeat of all sustaining governments | Retire each cause once and record the actual applied reversal. A frozen or disabled meter can apply zero. Replayed cleanup cannot create negative Chaos farming. | Does not refund the Chaos consequences of actual deaths or other irreversible shared outcomes. |

The ledger of event-owned political contributions is internal accounting for deduplication and reversal. It is not another player meter. A maximum of six first-region sources, two schism sources and two protection-collapse sources bounds the ordinary episode. Repeated oscillation over the same state or government cannot earn fresh global instability indefinitely.

Manual scenario setup must coordinate with the scenario owner's initial Chaos. If setup already accounts for the first manifestation, suppress exactly the duplicate event contribution for that setup receipt. Later actual growth, schisms, failed protection and containment still use this map. Manual launch cannot permanently silence the event's subsequent Chaos consequences.

## Required probability scenarios

The AI auditor starts with the actual implemented source, exact revision, candidate pool and `hoi4.probability_inspect`. Required scenario families include a small founder with no route, a capable founder with reluctant members, a player-led founder facing protection, a threatened player with a viable ally, an isolated client, a well supplied client, a departed adherent, a repudiating state, a blocked relief route, an over-capacity destination, a disabled evolution, a doctrine threatening members, and every terminal boundary.

Evaluate validity and intended ordering first. Sweep material thresholds for rank reversals and discontinuities. Use simulation only for explicitly uncertain inputs. Use sequence analysis only with a complete event pool, cadence, cooldowns, removals and state transitions. Record conclusions as exact, bounded, sampled, score-only or unresolved.

When an owner changes weights or timing, retain the baseline and run same-scenario probability comparison after the bounded patch. The auditor remains read-only. An event, focus or GUI structural render cannot replace this evidence. No probability percentage or time-to-terminal distribution is claimed by this planning package.

## Surface inventory and factor composition

| Surface | Selected design mechanism | Complete local alternatives and ownership |
| --- | --- | --- |
| Ordinary event timing and firing | Existing shared Minor Fire-Once pool and timer | The full enabled project pool is an implementation input. Event 115 never supplies a substitute partial pool. |
| Founder choice | Deterministic authored profile priority after all suitability checks | Valid Romanian profile first, then valid Slovak profile. No valid profile means a clean non-firing result. A later profile addition requires an explicit priority rule. |
| Invitation response | Native event-option AI after hard validity | Full assent, limited cooperation, or refusal. Expired and charter-invalid offers close before scoring. |
| Governing and client routes | Native focus selection semantics with actual route prerequisites | The three applicable founder or client routes and current shared branch candidates. Decision-only political responses remain independently available. |
| Decisions and missions | Native willingness under the actual decision or mission owner | Current role, phase and target-valid actions in Part 06. Human selection does not restrict the AI target set. |
| Purity Doctrine timing | Shared evolution MTTH | Valid proposal versus continuing baseline. The enacted charter requires each government's actual political response. |
| Doctrine response | Native event-option AI after validity | Assent, request a narrower agreement, refuse the change, or begin withdrawal or repudiation where politically valid. No option secretly applies another option's charter. |
| Terminal assent | Current-state political decision with no hidden automatic assent | Each counted government assents or refuses after current charter, force and obligation review. AI assents only when its chosen continuing-crusade route and current interests support the commitment. |
| Terminal selection and race | Shared serialized world-end selector | All currently eligible world-end branches under the shared owner. Event 115 cannot normalize its own candidate against an incomplete rival pool. |

Implementation assigns stable IDs after migration and records for each surface its actor, target scope, owner, native mechanism, full peer set, hard predicates, score expression, tie handling, cost, cooldown and unresolved external factors. Zero scoring is supplementary to explicit invalidity triggers. The table defines the intended mechanisms without claiming that uninspected native adapters already implement them.

The harder-player factor is applied once to the relevant final strategic-priority input. Use the maximum applicable proposed pressure factor, capped at 1.25, rather than multiplying the same player involvement through event, focus, decision and target layers. The ordinary world-Chaos preference is another single documented input. Each surface records where those inputs enter so a shared helper and a local factor cannot apply them twice.

For the Chaos bands, choose the lower value by default and the higher value only when the current political magnitude is independently established. Founder capture uses native major status. A first compact uses three or more genuinely committed governments. A regional client uses proven independent sustainment and the qualifying regional base. The broad-network source uses four qualifying regions rather than three. Schism and protection-collapse sources use the participation of a current major government or major defense grouping. These criteria choose the magnitude once when the fresh receipt is created. Later growth cannot top up the same receipt silently.

Each event-owned Chaos receipt records cause family, episode, actor or region, credited magnitude, any corresponding shared receipt, and outstanding reversible amount. A shared receipt for the same political fact takes precedence and sets the event duplicate to zero. Only the current outstanding event amount can be reversed. Reconquest, new charter numbering, leader swapping or manual retry cannot reset the per-episode family guard.

Separate the planned magnitude, requested delta and actual applied delta in that receipt. The pinned shared meter tests its current value before accepting an ordinary change. It permits overshoot from below 1000, then rejects ordinary positive and negative changes at or above 1000. A disabled meter also rejects changes. The event credits only the observed accepted delta, using a valid shared result or a controlled before-and-after observation of the same call. A rejected request has zero applied credit and cannot be replayed later as a newly discovered political milestone.

A real political defeat can retire the underlying cause even when the meter refuses its negative settlement. Preserve the original credited amount, requested reversal, actual zero reversal and unreversed historical balance with the rejection reason. Do not claim the meter fell, clear the balance as if it had been refunded, create an event-specific bypass, or schedule repeated failed attempts. Any later reconciliation must act on that same receipt under an explicitly supported shared policy.

The pinned Deaths conversion path can increment its generated-from-deaths accounting after a rejected Chaos call. That counter alone therefore does not prove an actual change to global Chaos. Civilian deaths and their accepted Deaths records continue to matter when the meter is frozen. Event 115 must never repeat the casualty or add another Chaos source to compensate for the rejected conversion.

The receipt identity and partial-settlement rules at the end of Part 06 also govern cohesion. First contribution is once per country in the event episode, including re-entry. A defense episode is keyed to the actual attack, defended theater, promised pair and operation, with its 180-day repeat guard beginning at settlement. A supply repair needs a genuine externally caused interruption and actual restoration, not a deliberate access toggle. Periodic reviews settle those same receipts rather than creating new causes.
