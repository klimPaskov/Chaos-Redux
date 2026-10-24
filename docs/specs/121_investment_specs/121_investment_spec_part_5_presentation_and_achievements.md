# Part 5: Presentation, assets, and achievements

## Reading and design status

This part defines Investment's presentation and achievement requirements within the complete eight-part specification.
Read it with [core](121_investment_spec_part_1_core.md), [sector projects](121_investment_spec_part_2_sector_projects.md), [evolutions and consequences](121_investment_spec_part_3_evolutions_and_consequences.md), [decisions, costs, and lifecycle](121_investment_spec_part_4_decisions_costs_and_lifecycle.md), [AI and validation](121_investment_spec_part_6_ai_and_validation.md), [integration and ownership](121_investment_spec_part_7_integration_and_ownership.md), and [delivery and usage maps](121_investment_spec_part_8_delivery_and_usage_maps.md).
It is accepted parent-authored design within the requested planning scope, not evidence of implementation.
All headings, semantic consumer codes, achievement descriptions, identifiers, and art labels are structural and nonfinal.
They are not final player-facing localisation.
Proposed technical names become stable only after collision and consumer checks under Part 7.

Investment keeps design identity 121 and original catalog identity 132.
The pinned pre-migration repository contained The Pact at catalog 121 and Investment at 132; the authorized migration now places Investment at 121 and preserves The Pact separately as a displaced concept.
Presentation work must follow the reviewed migration and protect The Pact's existing text, sprites, achievements, and workbook row.
No assets or localisation have been produced, and no HOI4 MCP, installed-vanilla inspection, or live-game check has run for this package.

## A construction programme the player can follow

The ordinary decision category carries the mechanic because the player chooses a sector, funds concrete phases, and responds to a small number of changing obligations.
Its basic summaries and site rows communicate those choices without a dedicated window.
The beneficiary is the one country selected by the firing.
The category never implies that other countries received the same charter.

Keep exactly two persistent public values: Work Complete, from 0 to 100, and Exposure, from 0 to 100.
Work Complete represents verified paid construction against the current agreed scope.
An amendment can enlarge its denominator, but cannot erase receipts, regenerate checkpoints, or reset the inspection quota.
Exposure communicates unresolved procurement, supervision, and technical promises.
It is a risk index and must never be labelled as a percentage chance of failure.
Explain earned reductions and any still-active full-risk floor without exposing internal residual records or adding sub-meters.
A safer future policy does not erase risk already accepted.

Show sector, site phase, native timer, promised buildings, held capacity, and the next exact quote as ordinary status information.
Do not introduce site progress gauges, a treasury balance, a second risk score, or an operating-stability meter.
Each of the maximum four site rows identifies the state, the actual promised work, the current phase, and any actionable blocker.
Use basic formatted rows rather than an imitation interface painted into an image.
After commissioning, mark earned output separately from remaining promises.
During a licence, construction progress can remain complete while Exposure, service commitment, and the native licence timer explain current obligations.

At sector selection, present the four sector rows and decline.
The proposal presents funding, site change, delivery-policy change, and return.
The site chooser presents the best three legal candidates and return.
Funded work presents acceleration, inspection, remaining-scope revision, and wind-down.
At a phase boundary, funding the next phase replaces acceleration.
One live incident replaces these controls with revised funding, contractor investigation, smaller unfinished scope, and wind-down.
Do not leave both control sets visible together.
Keep ordinary phases at three to five primary actions, never above six.

Use normally one or two native missions, never more than three.
A charter-level construction mission, the current actionable deadline, and a licensed-operation mission are sufficient.
The site table retains the individual due dates when several sites have obligations.
Do not create four simultaneous site missions merely because the charter has four sites.
The category must still make the earliest binding deadline and its affected site clear.

The eligible static category picture provides identity for this simple surface.
Its image has no interactive controls or live numbers.
Player feedback comes from native states, concise tooltips, the two public values, and earned-output summaries.
National completions and serious disasters use reports and selective news because their consequences remain tied to this country's programme.

## Direction-only localisation coverage

The following semantic consumer codes organise the writing assignment.
Part 7 allocates the actual event IDs and keys after resolving the catalog conflict.
Every accepted outcome needs its normal, blocked, and conditional wording where applicable.

| Consumer, structural code | Required surfaces and writing direction |
| --- | --- |
| OFFER | Report title, description, four sector options, decline, and eligibility explanation. Establish a subsidised opportunity, actual construction, one beneficiary, and the right to decline without charge. Do not describe the offered buildings as already constructed. |
| QUOTE | Proposal report or decision text, site choices, return, delivery-policy options, and funding confirmation. State frozen scope, three paid phases, hold, duration, outputs, and Materials versus native/exclusive Engineering delivery. Disclose the exact accepted contextual work factors and risk additions. Separate promises from immediate effects. |
| PHASE | Mobilisation, works, commissioning, phase-authorisation decisions, native construction mission, and boundary notices. Explain what was paid, what actually landed, what hold ended, and what needs a new authorisation. Avoid treating elapsed days as proof of paid work. |
| INSPECTION | Inspection decision, exact political-power quote, funded inspection days, once-per-phase availability, and actual earned procurement-risk reduction. Explain a full-risk floor that masks the displayed change. Inspection consumes capacity without construction credit and cannot remove unrelated technical risk. |
| AMENDMENT | Acceleration, delivery policy, site relocation, remaining-scope revision, and active evolution offers. Describe only the changed unpaid scope and its quote. Keep earlier payment and delivery intact, and explain a changed progress denominator. |
| INCIDENT | Delay, overrun, corruption, four response options, response deadline, and investigation results. Distinguish verified corruption from suspicion. Describe revised future work without promising recovery of consumed factory-days. |
| PAUSE | Shortage, capture, control recovery, between-phase funding, the single orderly extension, and the cumulative dormant limit. Name the affected site and released allocation. Explain the remaining obligation without calling released capacity a refund. |
| TERMINAL | Full completion, reduced settlement, voluntary wind-down, involuntary expiry, and payer retirement. Distinguish commissioned assets, unfinished losses, one-use brownfield credit, remaining distress, and the 540-day funded terminal cooldown. |
| METHOD | Conventional completion, inspected prototype, and full-risk offers for all three methods. Use Part 3's exact ordinary/mega packages. Explain prototype validation, the full-risk floor, delayed type-specific self-assembly units, and Engineering's continuing research-speed benefit plus separate once-only bonuses. An offer is not verified operation. |
| OPERATION | Activation, service, repair, validation, extension, assumption, disappearance, and expiry. Show the fixed 180-calendar-day licence, one paid extension up to original day 360, actual one/three-civilian service hold, and funded operating days separately from paused or corrective work. Retain the original dates and consumed reviews. |
| WARNING AND CLOSURE | Malfunction, critical warning, paid containment, emergency closure, and hazardous continuation. Distinguish the critical warning's 30-day gameplay response from A05's fault-relative 30-day eligibility clock. Show each actual quote and subsequent 30-funded-day action with its separate 60-calendar-day limit. Emergency closure is always executable and never paid-containment success. |
| SUCCESSION | Temporary control loss, recovery, permanent transfer, inherited-service election, and declined assumption. Show only remaining future operation and fresh service costs. A temporary occupier receives no charter. No pending extra-building coupon, research reward, original payment, or achievement progress transfers. |
| CRISIS | Critical financing warning, rescue, distress bridge, Event 35 acknowledgment, retry, and rejected handoff. Show the 90-day critical condition and material loss separately. Explain preserved warning time and actual settlement. Never call a rejected request an accepted depression or expose internal receipts. |
| RECOVERY | National account/contractor recovery while Investment owns distress. Show the ordinary cost quote from base 25 PP, one/three held civilians, 30 funded days, 60-calendar-day limit, one attempt, and reduction of min(90, remaining distress days). No building, construction credit, fresh charter, or cooldown reset is implied. |
| CATEGORY | Category name, short description, two value labels and explanations, site rows, quote summary, and cooldown/visibility states. Show the meaningful next action instead of a narrative wall. |
| TOOLTIPS | Availability, requirements, costs, capacity duration, effects, reduced rewards, blocked geography, slots, supply, ownership, existing commitments, and retained-output rules. Use exact dynamic targets and values. All spendable costs use correct texticons, with at most four cost types per action. |
| LOG AND DETAILS | Firing, sector commitment, evolution activation, material incident, commissioned output, terminal outcome, and anomaly consequence. Use the original beneficiary and the shared history owner's single record. Update its relevant detail state rather than firing another random-event log entry for each phase. Distinguish current state from historical promises and zero-Chaos unlocks from actual anomaly consequences. |
| NEWS | A completed nationally significant programme or a material industrial disaster. State the beneficiary, real place, visible consequence, and uncertainty. Avoid global claims from a local outcome or a news popup for every phase. |
| ACHIEVEMENTS | Titles, descriptions, progress explanations, eligibility blockers, award notice, and complete/grey/not-eligible states. Explain the material conditions without exposing implementation flags or pretending partial progress is an award. |

Use familiar words, direct subjects, and concrete consequences.
Keep source quotations unchanged if any are later authorised.
Original player-facing prose must not contain em dashes or sentence semicolons.
Never put tuning notes, debug terminology, proposed IDs, tool limitations, or implementation history into player text.
The catalogue's mirror fields follow final in-game wording through its workbook owner after implementation, not during this planning pass.

### Option-family writing direction

These families guide future wording. They are not sample options or final titles.

| Family | Speaker and stance | Tone and humour | Visible and withheld facts | Dynamic variation |
| --- | --- | --- | --- | --- |
| Sector offer and phase funding | Public works board proposes, government authorizes | Credible ambition, restrained confidence | Show real outputs, hold, work and authorization. Future incident truth stays unknown. | Beneficiary, sector, state, phase and actual quote |
| Tender, acceleration and scope revision | Procurement authority explains changed commitments | Precise, administrative | Show only unpaid changes, accepted risk and retained work. No claim that safer policy erases past risk. | Policy, remaining sites, revised duration and outputs |
| Investigation and incident responses | Inspectors present disclosed evidence | Administrative strain. Dry procedural humour is permissible before serious loss. | Separate suspicion from verified cause, and payment from completed correction. | Actual case, affected contractor role, site and remaining work |
| Decline, wind-down and reduced settlement | Cabinet accepts a bounded result | Calm, candid, without ridicule | Show retained assets, lost work and finite aftermath. Do not promise refunds. | Accepted scope and actual surviving outputs |
| Fever offer and sequence | Planning board argues for a coordinated programme | Civic prestige and scale, restrained enthusiasm | Show sites, concurrency, Materials/Engineering route, and one terminal dividend. | Country, site order, real route and programme size |
| Impossible offer and validation | Engineers propose a concrete process under uncertainty | Procedural unease, sparse bureaucratic humour | State exact prototype/full-risk terms, service, uncertainty and separate rewards. Withhold unresolved random outcomes. | Method, sector, capability route and legal flagship |
| Hazardous continuation | Responsible minister knowingly authorizes risk | Direct acknowledgment, no humour | Disclose actual cascade risk and possible physical/economic loss before commitment. | Current warning, affected sites and exact risk band |
| Containment and emergency closure | Operating authority prioritizes isolation | Measured responsibility. Serious damage and casualties are sober. | Distinguish paid work, immediate isolation, exact fee, damage and remaining consequences. | First fault, deadlines, available capacity and lawful quote |
| Extension and inherited service | Operator accepts remaining future obligations | Practical and conditional | Show unchanged expiry, fresh service and unavailable inherited rewards. | Original source, present owner-controller and remaining time |
| Distress recovery | Original payer's accounts office repairs national contracts | Accountable, restrained | Show one paid attempt and bounded timer reduction. Do not claim recovered buildings or an erased crisis. | Surviving payer, distress owner, remaining days and quote |

Any cultural, literary, political, or period allusion needs relevant documented research before use.
Verify meaning and speaker plausibility, avoid national stereotypes, and omit an unsupported allusion.
This guard applies to every family. Dynamic variation must follow actual actor/site facts rather than inferred culture.

## Asset manifest and consumer coverage

Every row below is a required production or reuse decision.
An existing accepted asset can satisfy a row only after its current consumer, provenance, source package, and acceptance have been reconciled.
Do not overwrite a live mod or vanilla texture or repoint its existing sprite merely because a new image is proposed.
For a requested dedicated consumer currently using a shared stand-in, create a new sprite and change only that consumer.

The manifest uses unique event-owned filenames.
Propose new interface/121_investment.gfx for its 24 non-achievement declarations.
This is a new owner allocation, not an inspected existing path.
The pinned [Event 34 graphics file](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/interface/034_industrial_boom.gfx) establishes the event-owned report, category, decision, and idea pattern.
All image dimensions below are output dimensions in pixels.
Category dimensions are explicit design targets that still require inspection of the actual ordinary-category consumer before production.
If that consumer differs, record a reviewed dimension amendment rather than silently resize or invent a new UI.

### Scenes and category art

These report and news scenes default to generated fictional, period-authentic documentary art.
If an accepted brief names a real photographed person, place, work, or historical artifact, route that row to attributed source research instead.
The final report processor supplies black-and-white/sepia treatment, subtle tilt, transparent corners, and soft shadow.
Do not ask generation to paint the report-card treatment.
News outputs are black-and-white.

| Code | Final runtime path | Size | Proposed sprite and consumer | Subject and lifecycle coverage |
| --- | --- | --- | --- | --- |
| R01 | gfx/event_pictures/121_investment/report_event_121_investment_works.dds | 210x176 | GFX_121_investment_report_works, OFFER, QUOTE, PHASE, AMENDMENT | A credible period works yard with foundations, steel gantry, and active preparation. Covers proposed and unfinished work without depicting an already earned factory. |
| R02 | gfx/event_pictures/121_investment/report_event_121_investment_interruption.dds | 210x176 | GFX_121_investment_report_interruption, INCIDENT, PAUSE, incomplete TERMINAL, corrective work and closure | A secured industrial bay with idle equipment, retained materials, and conspicuous empty working space. Covers interruption, missing abnormal output, and safe isolation without inventing damage, deaths, or corruption proof. |
| R03 | gfx/event_pictures/121_investment/report_event_121_investment_commissioning.dds | 210x176 | GFX_121_investment_report_commissioning, successful TERMINAL, safe expiry | Completed industrial sheds and a working gantry with a restrained workforce. Keep the scene compatible with the actual sector, avoiding ships, weapons, or named machinery absent from the output. |
| R04 | gfx/event_pictures/121_investment/report_event_121_investment_anomaly.dds | 210x176 | GFX_121_investment_report_anomaly, verified OPERATION and warning | Period industrial equipment with one clearly impossible mechanical discontinuity. Use only after a verified anomaly, not as evidence that an unaccepted proposal already works. |
| R05 | gfx/event_pictures/121_investment/report_event_121_investment_damage.dds | 210x176 | GFX_121_investment_report_damage, actual industrial damage | A visibly damaged industrial bay and a secured perimeter. No bodies, invented casualty count, or damage to unrelated facilities. |
| N01 | gfx/event_pictures/121_investment/news_event_121_investment_completion.dds | 397x153 | GFX_121_investment_news_completion, NEWS completion | A broad completed works panorama for a fully commissioned Fever programme spanning at least three states. Fire once from the authoritative success receipt, not once per site. |
| N02 | gfx/event_pictures/121_investment/news_event_121_investment_disaster.dds | 397x153 | GFX_121_investment_news_disaster, NEWS disaster | A distinct wider composition of actual industrial damage. Use once after a verified severe industrial cascade with attributable physical damage. Ordinary overruns and rejected crisis requests cannot trigger it. Event 35 retains its own crisis presentation. |
| C01 | gfx/interface/decisions/121_investment/decision_category_121_investment.dds | 32x32 target | GFX_decision_category_121_investment, CATEGORY button | An original compact works seal combining a structural beam and gear. Native transparent background. |
| C02 | gfx/interface/decisions/121_investment/category_picture_121_investment.dds | 114x101 target | GFX_121_investment_category_picture, CATEGORY picture | A simplified period construction yard with gantry and open foundation, separately composed for this surface. Opaque documentary source with consumer-required edge treatment, no fake controls or labels. |

R05 and N02 may share one retained scene master only when separately reviewed crops remain accurate at both canvases.
Their processed PNGs, runtime textures, and consumer records remain distinct.
Other scene reuse must be equally explicit.
No image may imply a fact that its consuming event has not established.

### Decisions, missions, and visible modifiers

Each row requires original family-specific generated raster source art with native transparency.
Do not resize a focus, report, achievement, or idea image into a decision icon.
Reuse within a row's named actions is intentional semantic reuse.
The exact consumer decides hover, disabled, and tint behaviour through native UI, not separately generated button art.

Decision outputs use gfx/interface/decisions/121_investment/ and the proposed GFX_decision_121_investment_ alias shown below.
Mission icons use the same runtime folder with separate source art and filenames.
All these decision and mission outputs are 32x32.

| Code | Exact filename | Alias suffix | Consumer and original subject |
| --- | --- | --- | --- |
| D01 | decision_121_investment_civilian.dds | civilian | Civilian sector and its project rows. Compact workshop gear and roof. |
| D02 | decision_121_investment_military.dds | military | Military sector and its rows. Munitions press and inert unfinished casing, no free-equipment implication. |
| D03 | decision_121_investment_naval.dds | naval | Naval sector and its rows. Ship keel under a short construction gantry. |
| D04 | decision_121_investment_special.dds | special | Strategic-materials, engineering, and the three anomaly method choices. Industrial retort with copper coil, readable before supernatural content appears. |
| D05 | decision_121_investment_inspection.dds | inspection | Inspection, contractor investigation, anomaly validation, and national distress recovery. Magnifying lens over a mechanical seal. |
| D06 | decision_121_investment_scope.dds | scope | Site selection, relocation, and unfinished-scope revision. Survey caliper and structural plan fragment without lettering. |
| D07 | decision_121_investment_policy.dds | policy | Tender policy, acceleration, and explicit operating-risk choices. Heavy paired pulley and bound tender sheet, no generated text. |
| D08 | decision_121_investment_commitment.dds | commitment | Phase funding, revised completion, repair, remaining-service assumption, and paid licence extension. Suspended industrial counterweight held by a robust locking mechanism. |
| D09 | decision_121_investment_closure.dds | closure | Wind-down, paid containment, and emergency closure, distinguished by exact text and costs. Secured industrial shutter and clamp. |
| M01 | mission_121_investment_construction.dds | construction_mission | Active construction mission. Hourglass against a partly assembled girder. |
| M02 | mission_121_investment_obligation.dds | obligation_mission | Proposal, phase funding, incident response, critical warning, corrective action, or distress recovery. Clock face without numerals beside an unsealed works document. |
| M03 | mission_121_investment_operation.dds | operation_mission | Licensed operation or the current funded repair, validation, or containment action, with its purpose explicit. Contained coil and restrained timing motif, distinct from construction. |

Use native return and decline presentation where the existing consumer already supplies it.
Their text and effects still require full coverage.

The following three 64x64 idea textures use gfx/interface/ideas/121_investment/.
Their proposed aliases are GFX_idea_121_investment_commitment, GFX_idea_121_investment_dividend, and GFX_idea_121_investment_distress.
Idea picture values use the suffix after GFX_idea_, subject to the automatic idea-ID override check.

| Code | Exact filename | Consumer and subject |
| --- | --- | --- |
| I01 | idea_121_investment_commitment.dds | Actual source-owned construction, service, corrective, and distress-recovery commitments. A load-bearing industrial frame under tension. Hide or clear each contribution when its actual hold ends. |
| I02 | idea_121_investment_dividend.dds | Consolidated commissioned and licensed benefits, including military precision and Engineering research speed. A completed gear assembly with a restrained industrial wreath. Use one Fever programme receipt and the strongest valid same-type benefit, with original expiry and custody conditions. |
| I03 | idea_121_investment_distress.dds | Actual Investment distress, including the bridge and finite 180/360-day fallback or cascade aftermath where Event 35 has not assumed the same effect. An idle flywheel and fractured support. Keep original expiry and avoid duplicate crisis ownership. |

These are three presentation families, not permission to combine incompatible state, country, or external-owner effects into one unsafe implementation.
The ownership part controls internal contributions.
Do not add a fourth visible Investment spirit for precision, each sector, each site, or an anomaly warning.

### Lifecycle review

The required review matrix covers uncommitted offer, unaffordable quote, invalid coast, blocked facility/slots, active work, phase release, next-phase funding, incident controls, capture/pause, cumulative dormancy, reduced settlement, conventional success, and external crisis acknowledgment.
Confirm the correct picture, icon, modifier presence, two public values, native timer, and available actions for each.
No row may show both an active hold and text claiming it was released, an expired bonus and an active benefit, or a success picture for unpaid promises.

Materials Fever shows R=1/2/3 refineries, two principal allocations each, B−2R civilian support factories, and one infrastructure level per quoted site.
Engineering shows F=1/2/3 native facilities or exclusive two-factory alternatives, B−2F support civilians, one infrastructure per site, and its two base research bonuses once per programme.
Self-assembly uses frozen ordinary U or mega B as its count basis, with civilian extras for civilian/special routes, military extras for military, and dockyards for naval.
An agreed reduction decreases the still-unearned count basis as Parts 3/4 specify.
Its promised placements must already be legal within the accepted sites. No extra refinery, facility, research coupon or support improvement is implied.

Early Fever sites show physical assets only.
One terminal programme dividend lasts 180 days for full scope or 90 days for an agreed reduced commissioning with a usable principal site.
Its qualifying site set is frozen at commissioning, all those sites require control, and expiry never restarts.
An abandoned programme without agreed reduced commissioning receives no dividend.

Distress recovery reuses D05 and M02 with I01's actual hold and I03's existing aftermath.
It remains owned by the residual distress record, with no new charter slot or site-recapture requirement.
Capacity loss pauses work within its 60-day limit.
Success reduces the original timer once. Failure, cancellation, expiry, annexation or Event 35 ownership releases the recovery hold without a reduction or date reset.

Part 3's additional consumers use these explicit bindings, keeping the complete inventory at 39 DDS outputs.

| Anomaly state | Existing asset bindings and required distinction |
| --- | --- |
| Method offer and prototype work | R01, D04/D05, and the relevant sector icon. Text distinguishes self-assembly, extraction, and throughput, including prototype/full-risk ordinary/mega values. No working anomaly is pictured before verification. |
| Ready to activate | R03, D08 and M02. Whole currently agreed conventional scope and prototype validation must be paid and commissioned first. Show the earlier of 90 calendar days and the flagship site's remaining cumulative dormant allowance, retained at commissioning. The licence starts at actual funded activation. Unstarted expiry grants no operating Chaos or coupon. |
| Verified operation | R04, M03, I01 and applicable I02 contribution. Self-assembly extras wait for 30 funded operating days and resolved safety review. A repairable fault retains the same-case coupon, but expiry forbids late delivery. Engineering research speed is inspected +10%/+15% or full-risk +20%/+30%, ordinary/mega. It applies the strongest same-type benefit, without adding the ordinary +5%, and has two separate extra one-use 50% bonuses at anomaly commissioning. |
| Repair or validation | R02, D08 for repair or D05 for validation, M03 and M02. Repair costs 30 funded service days with no PP fee. Validation uses the ordinary quote from base 25 PP plus 30 funded service days and can include fault repair if quoted. Output is off and these days are not operation. |
| Critical warning | R04 or R02, M02, and four response controls. The ordinary service hold and output pause. Paid containment/validation accepted within 30 calendar days replaces that warning mission with the paid action and its separate 60-day deadline. |
| Paid containment | R02, D09, M03, M02 and actual I01 hold. Show the accepted ordinary quote from base 25 PP, including lawful discount or zero, plus 30 funded service days. Cleanup may finish after expiry without restored output or restarted licence. Only critical-warning acceptance retires a warning mission. |
| Emergency closure | D09 and R02, or R05 after observed damage. Charge min(exact current ordinary quote from base 25 PP, nonnegative available PP), unless valid same-case containment/validation political authorization covers it. A lawful zero quote still authorizes. No repeated fee or containment achievement. |
| Transfer and extension | D08 and M03. Permanent owner-controller assumption requires no conflicting charter/service and fresh capacity. Dates, extension use, consumed reviews, and unavailable one-time rewards stay explicit. |
| Expiry, disappearance, or cascade | R03 for safely retained conventional assets, R02 for vanished abnormal output, R05 for actual damage. N02 requires the defined severe cascade. Clear expired I01/I02 contributions and show I03 only for its actual owned aftermath. |

The self-assembly, extraction, and throughput variants share R04 and the sector/method icons.
Their mechanics differ through text and actual effects, so separate scene paintings would add repetition without improving the choice.

## Five achievements with verifiable conditions

Use the proposed technical IDs below after registry collision review.
Their names are not titles.
One immutable qualifying charter record supplies beneficiary, tier, sector, agreed outputs, paid phase receipts, site custody, incident origin, service days, terminal result, and award guard.
Publish the authoritative outcome before consuming the active proof.
A completed building, a selected option, or a cumulative spending counter alone is insufficient.

Only qualifying human-beneficiary work counts toward these player achievements.
AI countries retain the complete gameplay and rewards, but cannot accumulate player achievement credit.
A later human takeover does not convert AI-paid work into qualifying work.
The beneficiary must remain human-controlled through each qualifying construction or operating interval.
Use the existing achievement framework's player handling rather than inventing account tracking.

A charter created or materially advanced by debug grants, forced outcomes, synthetic payments, or an unregistered entry route is ineligible.
Read-only inspection is not a disqualifier.
Captured or inherited completed sites, successor-country handovers, unrelated grants, and inherited-service records never provide original construction, operating, incident, or achievement credit.
Brownfield credit is consumed once and never counts as new paid work.
Legitimate relocation can preserve eligibility only with the same charter identity, full promised scope, legal replacement, and retained receipts.
Scope reduction, cancellation, and repeated callbacks cannot manufacture completion credit.
Previously earned achievements survive later cleanup.

| Condition | Difficulty metadata | Reveal condition |
| --- | --- | --- |
| A01 Portfolio | Hard | Ordinary event access |
| A02 Recovery | Medium | Ordinary event access |
| A03 Linked commissioning | Hard | Fever access |
| A04 Licensed stewardship | Hard | Impossible access |
| A05 Controlled containment | Very Hard | First actionable qualifying anomalous fault after 30 actual operating days |

Once revealed, an achievement remains visible.
Hide exact late-stage condition text before reveal without hiding immediate mechanical risk from a purchaser.
These metadata do not add award requirements.

### A01: Portfolio condition

Proposed ID: 121_investment_achievement_portfolio.
One beneficiary completes four distinct ordinary, non-anomalous charters, covering civilian, military, naval, and special sectors once each.
At least one uses a Standard or Large envelope.
The projects span at least three distinct states and fully deliver every accepted mandatory output.
At the final award check, all four qualifying outputs remain valid and beneficiary-controlled, with no unpaid completion obligation.
Either fully specified special-engineering route qualifies, including the exclusive no-DLC bundle.

Store one success reference per sector and the distinct-site set.
An amended Fever charter cannot count as an ordinary charter, and one special bundle cannot count as both civilian and special.
Inherited facilities, reduced settlements, aborted projects, or a native facility without its paid commissioning proof fail.
Loss of a required retained output prevents the final conjunction without awarding substitute credit twice.

Icon subject: one compact assembly combining gear, riveted plate, anchor hook, and copper coil.
Use four broad integrated forms, aged brass and dark steel, not a four-panel collage.

### A02: Recovery condition

Proposed ID: 121_investment_achievement_recovery.
Complete a Standard-or-larger conventional charter after a genuine material overrun or confirmed corruption incident.
The accepted incident system must freeze its cause and severity while mandatory work remains.
Choose and complete contractor investigation, actually fund and perform the legitimate remaining work including any required correction, preserve all original mandatory outputs, and finish with Exposure at most 24.
Require at least 1,080 credited civilian-factory-days of actual construction across that charter, excluding inspection time, salvage credit, and unpaid quotes.
Every required output must be beneficiary-controlled and every remaining completion liability settled at award.

Record the incident origin, investigation receipt, positive paid construction after investigation, unchanged output obligation, paid-work sum, and final success.
Routine inspection alone does not qualify.
Later national distress recovery cannot substitute for this charter's successful corrected construction.
Player-created starvation, a forced incident, an investigation after all required work was already complete, scope reduction, or a local settlement after failed delivery does not qualify.
Removing an unjustified future surcharge is a valid investigation result and does not itself disqualify an otherwise complete recovery.
The native and exclusive engineering paths use the same evidence tests.

Icon subject: a damaged steel girder held true by a substantial handwheel repair jack, with a visible repaired joint.
The working repair dominates, with no money pile or tiny written document.

### A03: Linked commissioning condition

Proposed ID: 121_investment_achievement_megaproject.
Complete a Fever charter admitted or explicitly amended at Chaos 200+ with at least three mandatory sites in distinct states.
Deliver the entire accepted mandatory scope and at least two real output classes.
Require at least 3,600 credited paid construction factory-days.
Under sequential commissioning, one complete early site must remain beneficiary-controlled and usable for at least 90 days while later accepted work continues.
At final full-programme commissioning, require the single charter Exposure to be at most 24, with no failed linked site or accepted Event 35 crisis consequence from that charter.

Use the frozen programme scope, legal amendment history, delivery receipts, paid-work sum, and early-site custody record.
Do not infer 90 continuous days from two snapshots.
Normal corrected incidents can occur.
Dividing one state into several rows, substituting a reward multiplier for a second output class, cutting mandatory scope, or counting captured work fails.
Native facilities and their exclusive engineering bundles qualify according to their actual quoted output classes, not feature availability.

Icon subject: a single massive gantry spanning three distinct industrial masses joined by a short service link.
Retain three readable forms rather than a detailed map.

### A04: Licensed stewardship condition

Proposed ID: 121_investment_achievement_operation.
Complete an Impossible Industry charter admitted or amended at Chaos 600+ and commission its paid flagship.
Then achieve 180 consecutive beneficiary-controlled days of actually paid licensed operation, with the required ordinary or mega service hold present.
Warning pauses, repair, validation, and containment are not operating days, even when corrective service is paid, and break the current continuous interval.
Resolve the day-30 and day-90 operating reviews safely without a hazardous continuation choice.
There must be no disappearance, serious cascade, captured interval, unpaid service interval, or permanent shutdown during qualification.
The corresponding fully specified engineering route qualifies even where its licensed benefit is research-oriented.

An unextended licence qualifies only from its safe expiry receipt and an unbroken 180-day service ledger, not an active-bonus flag after expiry.
At day 180, unfunded expiry settles before a new hazard.
A day-180 review applies only when the extension is actually funded.
An extended licence can prove a later 180-day continuous interval within its original 360-calendar-day limit.
Its authoritative milestone must also settle every applicable review safely, including the 180-funded-operating-day review.
A new controller's service receipt cannot inherit the former owner's construction or operating credit.

Icon subject: a factory wheel with one floating mechanical section held within substantial copper restraints.
Keep a restrained cold-violet interior accent and solid period metal, not a generic glowing cloud.

### A05: Controlled containment condition

Proposed ID: 121_investment_achievement_containment.
After at least 30 actual paid days of licensed operation, encounter a genuine material operating fault with a malfunction or critical-warning receipt before irreversible cascade.
Freeze the eligibility clock at the first actionable qualifying fault after those 30 operating days.
Within 30 calendar days of that fault, accept paid containment's ordinary-cost quote from base 25 PP and its valid service authorization.
Lawful discounts and a legitimate zero quote qualify. A zero quote still needs its authentic authorization receipt.
Complete 30 genuinely funded days at the ordinary one-civilian or mega three-civilian service hold before the separate 60-calendar-day deadline measured from acceptance.
Critical-warning acceptance retires its gameplay response mission and keeps output off.
For a malfunction, disclose the achievement eligibility date in its status/tooltip without adding a mandatory emergency-close timer.
Its cleanup may finish after licence expiry without extending the licence or reviving output.
Surrender the remaining anomalous benefit, remove only the project's owned temporary contributions, release all remaining service holds, and preserve its legitimately commissioned conventional buildings.
There must be no hazardous continuation response, serious cascade, attributable casualty/contamination consequence, or accepted Event 35 crisis from that incident.
The closing receipt must record the actual limited Chaos repayment, including zero if the source premium was already returned, and every permanent consequence that remains.

The achievement adds no cost beyond Part 3's paid-containment action.
Emergency closure remains executable at its bounded actual quote, with no repeated fee after valid same-case containment/validation political authorization, including a lawful zero quote.
Emergency or default closure, missed paid-action deadline, ordinary expiry alone, voluntary cancellation without a real fault, debug warnings, unpaid corrective work, inherited service, or a false clean slate fails.
Do not require repayment of unrelated Chaos or disappearance of already recorded damage.

Icon subject: a heavy industrial iris safely enclosing a cracked anomalous core, with an isolated copper conduit and robust locking clamps.
Convey controlled loss rather than an explosion trophy.

## Achievement art, verification, and handoff

Each accepted ID requires one original transparent 64x64 subject source and three final 64x64 runtime DDS states directly under gfx/achievements/.
For each ID above, the exact filenames are its ID followed by .dds, _grey.dds, and _not_eligible.dds.
These fifteen files are one complete five-achievement requirement set.
Extend [common/achievements/chaos_redux_achievements.txt](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/achievements/chaos_redux_achievements.txt), preserving its single root unique_id = chaos_redux_achievements.
The inspected economic entries consume durable country proof flags through happened and custom tooltips.
Publish each Investment proof only after its complete conjunction passes, with its own human/debug/custody guards.
The existing possible examples do not establish those new guards.
Add GFX_achievement_<id> and matching grey/not-eligible aliases in [interface/chaosx_achievements.gfx](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/interface/chaosx_achievements.gfx), once per state.
That file documents stock filename lookup under gfx/achievements/.
Use [localisation/english/chaosx_achievements_l_english.yml](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/localisation/english/chaosx_achievements_l_english.yml) for <id>_NAME, <id>_DESC and the separate eligibility/condition tooltips.
These pinned observations establish integration surfaces, not native achievement behavior or finished implementation.

Use the supplied immutable achievement_template.png, achievement_template_grey.png, and overlay.png from the current asset skill's achievement template folder.
Generate no frame, red cross, text, or fake checkerboard into the subject.
Derive an aligned grayscale subject from the colour source, then place the unchanged overlay on that grayscale source.
Run process_achievement_icons.py on the complete source triplet.
Do not generate three independent state paintings or run unrelated single-image conversions as a substitute.
Require exact template hashes, 64x64 dimensions, composition pixel equality, strict BGRA DDS validation, and a native-size triplet contact sheet reviewed by the parent.

For all other rows, preserve exact requests, references, immutable sources, processed previews, alpha evidence, candidate selection, conversion results, and live consumer mappings.
Use the current .claude/skills/chaos-redux-event-assets/ reference library and tools.
The active workspace is docs/assets/121_investment/.
Promote durable provenance, requirement coverage, and accepted lineage into permanent documentation before full-completion cleanup.
No runtime reference may point into that workspace.

Future work routes scenes to chaosx_generated_event_art or chaosx_asset_source_researcher, icons to chaosx_icon_artist, and wording to chaosx_localisation_auditor.
The parent owns nonportrait integration and final acceptance.
Achievement implementation uses the parent and bounded scripted-system work, not an invented achievement-production specialist.
These are planned routes, not claims that canonical specialists have run.
Follow current bounded source/available-tool validation and disclose unavailable checks without awaiting user live testing.
