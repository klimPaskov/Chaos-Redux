# Part 6: AI choices and validation

## 6.1 Intended behavior and evidence status

Investment gives viable AI minors equal access, then favors useful capacity, sustainable commitments and recoverable Exposure. AI must recognize shortages, preserve earned work and close unsafe projects when continuation has no defensible return.

This part defines proposed scores and acceptance criteria. Probability tests, HOI4 MCP, installed-game checks and live results remain unrun. Implementation must compare the design's intended subsidy with native construction costs.

The pinned Event 34 target gate admits majors or human players. Investment deliberately replaces that restriction with the broader pool in [Part 1](121_investment_spec_part_1_core.md). Its reservation mechanism is useful precedent, while its recipient gate and lifecycle effects remain with Event 34. Source: [Event 34 triggers](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_triggers/034_industrial_boom_triggers.txt).

## 6.2 Legality before preference

Country selection is uniform, one entry per eligible country. Major status, human control, industry size and ideology add no weight. Retain the actor before generic firing history.

Eligibility requires an existing country able to use normal civilian industry, a legal owned and controlled supplied industrial site, at least one genuinely usable civilian factory after other commitments, and no active charter, open proposal or terminal cooldown. Use the compatibility classifier in Part 1, rather than excluding a usable economy solely because it has a special Chaos identity. Zero usable capacity gives no free bootstrap award. Country eligibility does not make every sector or envelope legal.

Each purchase uses the effect's pure preflight for recipient, charter generation, site, phase, capacity, quote, ownership and delivery. Naval work needs a legal coast. Special work needs exact native facility or refinery legality, or its frozen alternative. Impossible outputs are unavailable.

Recheck legality immediately before mutation. A zero score cannot protect a direct callback or stale selection. Construction wind-down and proposal decline remain free.

Scoring reads current facts and disclosed information. It may write caller-owned calculation outputs, but cannot allocate receipts, spend, advance work, choose random targets or reveal hidden corruption. Tooltips and AI evaluation never reroll proposals or incidents.

## 6.3 Score semantics

These are proposed raw scores. Apply listed additions and multipliers to each base, then clamp legal purchases to 10–240. Legality removes impossible choices. Keep safe decline or return at least 20 when other choices disappear.

Native decision `ai_will_do` values are priority scores. They are not percentages or a predicted distribution of clicks. Event-option `ai_chance` values are normalized by their own native mechanism. The supplied AI sources describe d100 rounding, which can erase very small shares, and a first-option fallback when every weight is zero. Validate the actual option table after translation. Do not allow a first purchase to become the all-zero fallback.

Decision and event-option scores are different mechanisms. Record legal alternatives and calculated weights separately from later native choices.

### Sector and variant choice

Apply these sector preferences only after the exact site and promised outputs are legal.

| Choice | Base | Adjustments |
|---|---:|---|
| Civilian manufacturing | 100 | +35 at peace, +30 when usable civilian capacity is below five, +20 when the proposed enabling improvement relieves a demonstrated supply constraint |
| Military arsenal | 80 | +70 during war with a major or +35 during another active war, applied once, +25 for a documented production-capacity shortage, -25 when the proposed hold would consume all presently usable civilian capacity |
| Naval yard | 55 | +45 during a naval war or a documented maritime production need, +20 when port improvement supports the existing supplied yard, -30 when the legal proposal offers little usable naval production |
| Special industry | 55 | +35 for legal materials output addressing a resource deficit, +25 for an Engineering package with a usable research path in either capability mode, -35 when the longer commitment would leave an essential obligation unsupported |
| Decline | 20 | +50 when every affordable offer uses all usable civilian capacity, +70 during imminent territorial collapse, +40 when every legal site has a disclosed severe threat |

“Production shortage” must resolve to a documented engine or owner read, not a new public currency. Where that read cannot be established, omit its adjustment and report the missing binding.

Within a sector, use base 100 for its ordinary capacity variant and 60 for its support or precision variant. Add 50 to utilities, rail support or repair logistics when the corresponding native infrastructure constraint is present. Add 35 to precision when at least one promised research bonus has a valid eligible consumer. Apply a factor of 0.6 when the variant increases work by 20% and its extra benefit has no current strategic use. These rules preserve the Small variant’s principal building and never purchase an unavailable technology.

For Experimental engineering, the native-feature check chooses the delivery branch before acceptance. AI does not compare the native bundle with the no-feature bundle as two simultaneously redeemable prizes. The legal branch receives the same preference assessment using its actual slots, work and useful outputs.

## 6.4 Envelope and delivery-policy choice

Envelope legality uses the exact quote, including specialization, geography and delivery policy. These nominal anchors remain unchanged:

| Ordinary envelope | Held civilians | Principal units | Nominal funded days |
|---|---:|---:|---:|
| Small | 1 | 1 | 300 |
| Standard | 3 | 2 | 360 |
| Large | 5 | 3 | 420 |

Special industry multiplies the nominal duration by 1.5. Megaproject anchors are 3 held civilians for 4 principal allocations over 480 days across two states, 6 for 8 over 600 across three, and 10 for 12 over 720 across four. Each special facility or exclusive two-factory alternative consumes two allocations. Respect the twelve conventional-primary and three-facility ceilings. The implementation uses the agreed scope and work budget from Parts 2 and 3, not an assumed value per building.

Materials networks use one, two or three refineries, consuming two allocations each, with the remaining allocations as civilian support factories. Engineering uses the corresponding facility or exclusive two-factory bundles and supporting civilians. Both include the quoted infrastructure per site. Self-assembly never turns a spare allocation into another refinery or facility.

After sector and policy factors, multiply each site's preceding work quote once by `1 + 0.10 × N`, where N counts non-core status, infrastructure below half the installed maximum and payer at war. The contextual increase caps at 30%. Freeze it at acceptance before phase rounding. Supply and control remain legal requirements. Do not invent an additional geography or supply multiplier. Expected funded-duration targets are 180–720 days for ordinary non-special, 270–1080 for ordinary Special and 360–1440 for Fever. An outlying proposal needs smaller viable scope or an explicit exceptional balance decision before purchase.

Use ordinary envelope bases Small 110, Standard 85 and Large 60. The default recommendation should hold at most 25% of pre-charter usable civilian capacity where such an envelope exists. Add 30 to a choice inside that preferred share, and subtract 25 above it. Add 30 to Standard or Large when a documented need would use all its principal outputs. Subtract a further 35 when the hold exceeds half that capacity, and 60 when it consumes all of it. Add 25 to Small when it is the only affordable envelope. These penalties remain preferences, so a one-factory country can still accept Small in reasonably secure peace. War urgency may justify a larger legal commitment but never removes affordability.

Phase rounding follows Part 4. Allocate nominal work into 25%, 50% and 25% shares, divide each by its integer hold, round each duration upward to a multiple of five days, then freeze payable work as hold times that duration. For example, a Small special project has 450 nominal civilian-factory-days. Its one-civilian phase durations become 115, 225 and 115 days, so its accepted payable work is 455. This is analytical design arithmetic. It does not claim a native execution result. Later amendments round only unpaid prospective work.

Compare those choices with keeping the ordinary charter when Fever becomes available. Keeping the agreed deal has base 100. A legal two-site program has base 75, a three-site program 55 and a four-site program 35. Add 35 when all linked sites are supplied and the country retains at least half its usable capacity outside the proposed hold. Subtract 50 when any proposed site faces an active front. Do not favor a larger program merely because it creates more possible salvage.

| Delivery policy | Base | Adjustments |
|---|---:|---|
| Verified tender | 100 | +40 at peace or with high existing Exposure, +25 for a threatened but legal site |
| Matched capital | 100 | +25 with stable supply and at least half usable capacity left free |
| Accelerated | 35 | +55 during a major war with a specific urgent production need, -50 at Exposure 50 or above, -50 when the increased hold consumes all available capacity |
| Keep current paid scope | 110 | +40 during shortage or site disruption |

Acceleration reserves `ceil(1.5 × C)` for the relevant quoted capacity, respects the cap of twice original capacity and real availability, and adds at least 10% to remaining required work. It is an explicit amendment. Paid work, delivered outputs, checkpoint identities and the phase’s audit quota do not reset.

Exposure preferences read the one public sum defined in Part 3. Context adds 10 once for any non-core site, 10 once for a selected land site adjacent to hostile-controlled land and 10 once when peak accepted total hold reaches half the frozen initial usable capacity. Context caps at 30. A policy upgrade adds only the increase above the highest policy risk previously accepted. Safer future policy, recapture and menu cycling do not erase or repeat contributions.

For a megaproject delivery sequence, sequential commissioning has base 110 and parallel work 60. Add 40 to parallel only when every simultaneously funded site remains legal and the country retains half its usable capacity after the hold. Add 40 to sequential when a site is threatened or early completed capacity materially helps the country. Only authorized concurrent holds can earn concurrent work.

Early sites supply physical assets. Fever has one terminal program dividend: full mandatory-network completion earns 180 days, and agreed reduced commissioning with a usable principal site earns 90. Failed or abandoned scope earns no dividend without that reduced settlement. AI evaluates this actual terminal benefit, with no per-site dividend stacking.

## 6.5 Site selection and phase management

Build the best-three site list from owned and controlled candidates passing the exact sector preflight. Score legal sites at base 100, adding 30 for a verified capital or supply connection, 20 for spare legal output capacity, 20 for suitable existing infrastructure, and 15 for a reusable same-payer brownfield contribution that the new scope can actually consume. Subtract 50 for an active hostile frontier and 30 for relevant physical damage. Break ties by stable state ID.

For naval work, score the actual legal coastal province and port opportunity, retaining its identity with the state. A state-level coast flag does not certify the promised province building. For a network, validate the actual railway path. Candidate ranking cannot manufacture an inland port or a cosmetic railway.

The same state may not appear twice in a charter’s site set. A choice made through the site menu persists until changed by an explicit legal selection. Reopening the menu is not a new random draw.

At a phase boundary, funding the next phase has base 100 when legal and affordable, +35 when it completes the principal output. Inspection has base 30, +50 at Exposure 50 or above when reducible procurement risk remains, and +40 after a disclosed relevant warning. Respect the phase audit allowance and exact ordinary-cost quote from base 25 PP. Its selected site's currently authorized integer allocation is held for 20 funded days, or 40 for Fever, without construction credit. A zero quote is valid authorization. Inspection cannot remove protected anomalous risk or bank reduction against future additions. An unaffordable inspection never blocks wind-down.

At shortage, prefer the one orderly 30-day extension only when a real recovery of capacity is evidenced. Otherwise reduce unfinished extras or wind down. Proposal and funding windows are 90 days. The funding extension lies within the cumulative 180 inactive-day site cap, and overlapping inactive reasons count once. AI must not renew an expired window by returning to a menu.

## 6.6 Incident and anomaly responses

Baseline incidents use charter checkpoints at 30% and 70%. Fever uses 25%, 50% and 75% across the whole charter. An amendment retains consumed original checks and adds only enough to reach the three-check ceiling. One unresolved incident replaces ordinary project controls with its four responses.

| Incident response | Base | Adjustments |
|---|---:|---|
| Fund revised completion | 80 | +35 when a principal output is close and affordable, -60 when the revision consumes all usable capacity |
| Investigate and replace contractor | 65 | +50 with disclosed corruption evidence, +30 at Exposure 50 or above, -30 when the remaining useful scope is very small |
| Reduce unfinished scope | 45 | +65 for a real capacity shortage, +40 when removable extras preserve the principal output |
| Wind down | 20 | +100 when no affordable legal completion remains, +70 near the final inactive-day deadline, +50 for persistent severe territorial risk |

AI may read disclosed suspicion, loss and warning state. It must not read the hidden genuine-corruption bit to obtain perfect knowledge. The incident’s truth is frozen, and an investigation resolves that truth rather than rerolling it.

Delay, overrun and corruption cases add unresolved contributions of 5, 10 and 20 respectively. The corruption addition is identical before truth is known. Remove only the remaining applied contribution after verified paid correction, or investigation plus an actually funded viable settlement. Quote acceptance alone does not clear it. The critical financing warning begins at unresolved Exposure 75+, counts 90 qualifying calendar days and preserves elapsed days while its condition pauses. AI evaluates wind-down's real losses before assuming it prevents an already earned national consequence.

Anomaly choice first includes ordinary completion, with base 100 and +70 at Exposure 50 or above. Each legal anomalous method starts at 55. Self-assembly gains 35 when every additional principal building can be legally delivered. Extraction gains 40 for a real deficit in the selected resource. Throughput gains 35 where the affected production or construction activity is actually useful.

Engineering throughput uses a real continuing research-speed benefit in both native and no-DLC modes: inspected +10% ordinary or +15% mega, full-risk +20% ordinary or +30% mega. Its usefulness receives the same +35 adjustment when research can use it. The strongest valid same-type contribution replaces weaker contributions within the existing family, including the ordinary +5% Engineering dividend. Two extra one-use 50% industry bonuses remain a separate once-only commissioning reward.

Self-assembly counts frozen ordinary U or mega B allocations, equally across capability modes. Extras are civilian for civilian and special routes, military for military, and dockyards for naval. Freeze their legal placements among existing sites. License activation requires the whole currently agreed conventional scope and prototype validation to be paid and commissioned. A reduced agreement lowers any unearned basis. At conventional commissioning, the first-service window is the smaller of 90 calendar days and the flagship site's retained unused portion of its cumulative 180-day dormancy allowance. Waiting consumes that same flagship allowance. Other commissioned sites supply no additional grace, and zero remainder retires the unstarted method immediately. Missing the window earns no operating premium or coupon. The license starts at actual funded activation.

The inspected operating route has base 100. The full-risk route has base 25, +35 for a specific wartime need and a factor of 0.25 at Exposure 50 or above. Use effective Exposure, including ambient additions and the full-risk floor of 50. The inspected prototype pays 20% additional relevant work before retiring its remaining method-uncertainty residual. Later paid validation also removes the full-risk floor and applies the smaller benefit only while licensed. Continued hazardous operation starts at 10. Paid containment has base 100, +70 after a warning. Emergency closure has base 70, +80 when service capacity or legal control has ended.

Malfunction repair has base 85, +35 when useful operation has at least 60 calendar days remaining, -60 with fewer than 30 remaining. Paid validation has base 75, +45 for full-risk Exposure of 50 or more, -50 with fewer than 30 days left. Repair costs 30 funded service days at the ordinary one-civilian or mega three-civilian hold, no PP, with output off and a 60-calendar-day deadline. It removes only that fault's remaining applied residual, which may be smaller than its nominal +10. Unfinished anomalous rework has a separate quote. Validation may include the same correction explicitly, without duplicate work.

The operational license is 180 days, with one explicitly paid extension and a total limit of 360 days. Renewal has base 45, +35 when operation remains useful and stable, -60 after a serious warning. It is unavailable at the total limit or without the required ordinary one-civilian or megaproject three-civilian service hold.

Operating reviews occur at 30 and 90 funded operating days, and at 180 only with a paid extension. Self-assembly extras require the first 30 qualifying days and successful safety check. Inspection, repair, validation and containment time do not qualify as anomalous operating time. A pending coupon retires at license expiry, so late repair cannot grant it. Part 5's 180-consecutive-day stewardship streak resets on a pause, while cumulative review progress and consumed checks persist.

Emergency warnings allow 30 calendar days to accept and pay for a response while output and service pause. Paid containment or validation then has 30 funded service days and a separate 60-calendar-day hard deadline. Output stays off and license expiry advances. Cleanup may finish after expiry, but validation cannot restart it. Failure defaults to emergency closure. Its fee is `min(current ordinary-cost quote from base 25, max(0, available PP))`, unless valid same-case containment or validation political authorization already covers it. A legitimate zero quote is authorization and cannot be charged again.

Expiry precedes a coincident day-180 hazard unless a paid extension sustains operation. A new owner-controller can assume service only after permanent transfer, with no conflicting active charter or service. Pending building and research rewards do not transfer. AI cannot obtain another operating period through callbacks or controller changes.

Finite distress recovery has raw score 80, +40 with at least 120 distress days remaining and -50 below 60. Apply legality and affordability first. It costs the ordinary quote from base 25 PP plus one held civilian for ordinary aftermath or three for mega, for 30 funded days within 60 calendar days. One attempt is allowed per distress receipt. Verified success shortens the original distress by `min(90, remaining days)`. It belongs to the surviving payer's distress receipt, requires no state recapture and creates no charter slot or new firing. Failure, original expiry, annexation or Event 35 ownership ends the hold without reduction or clock reset.

## 6.7 Analytical incident probability

Exposure is a risk index, not a failure percentage. The design assigns a distinct incident probability at each eligible checkpoint:

| Exposure at checkpoint | Single checkpoint | At least one in two | At least one in three |
|---|---:|---:|---:|
| 0–24 | 5% | 9.75% | 14.2625% |
| 25–49 | 15% | 27.75% | 38.5875% |
| 50–74 | 30% | 51.00% | 65.70% |
| 75–100 | 45% | 69.75% | 83.3625% |

These are analytical calculations, not simulation or native results. For a fixed probability `p`, independent rolls and every checkpoint reached, the model is `P(at least one) = 1 - (1 - p)^n`. Expected incident count is `n × p` under those same assumptions. The table does not say that an entire charter fails at those rates. Ordinary incidents remain repairable.

For a fixed known two-checkpoint path with probabilities 5% then 15%, the corresponding probability is `1 - 0.95 × 0.85 = 19.25%`. A three-checkpoint path with 5%, 15% and 30% gives `1 - 0.95 × 0.85 × 0.70 = 43.475%`.

Changing Exposure after an incident, conditional continuation, AI response choices and wind-down make the campaign adaptive. A complete forecast must branch on those histories and whether each later checkpoint is reached. Multiplying an average probability across an adaptive campaign is not an accepted audit.

The initial conditional issue mix is 40 delay, 35 overrun and 25 corruption. At a 15% checkpoint with that unchanged mix, the unconditional one-checkpoint probabilities are 6% delay, 5.25% overrun, 3.75% corruption and 85% no incident. Reweighting an issue because of real conditions requires a fresh normalized calculation. It must not change the chance of an incident or permit an illegal consequence implicitly.

Anomaly reviews use their separate conditional mix: 50 malfunction, 30 disappearance and 20 critical warning, changing at Exposure 75+ to 40, 25 and 35. A 15% review therefore gives 7.5%, 4.5% and 3% respectively. At Exposure 75+, a 45% review gives 18%, 11.25% and 15.75%. Explicit hazardous continuation later risks a cascade at 30% below Exposure 75 or 60% at 75+. If every warned actor in the upper band continues and remains in that band, the critical-warning branch alone gives `0.1575 × 0.60 = 9.45%` per reached review. This is an analytical conditional-policy example, not an overall failure rate or native observation.

Record each checkpoint’s charter identity, index, eligibility snapshot, Exposure band, roll result and selected issue before resolving its consequences. Preserve the result across reload, pause, amendment and site changes. If a large work update crosses multiple unconsumed checkpoints, process them in order and retain later due work while one issue is active. Never reroll a consumed checkpoint or turn a scope reduction into a second threshold crossing.

Audit the implemented random surface, fixed and changing bands, and issue mixtures. Separate exact, bounded, sampled and unresolved results. [Part 8](121_investment_spec_part_8_delivery_and_usage_maps.md) owns the tooling workflow.

## 6.8 Named acceptance scenarios

All cases below are required future scenarios, not completed tests. Capture actor, charter, site, phase, generation, ownership epoch, accepted quote, actual payment, capacity held, work credited, due date, output delta and terminal receipts.

| ID | Fixture and action | Required result |
|---|---|---|
| AI-01 Minor access | Compare viable AI minor, human minor and major | Equal pool participation per eligible country, legal affordable choices for the AI minor |
| AI-02 Constrained choice | One affordable sector and several blocked ones | Only legal purchases can commit, with positive preference for a useful legal choice |
| AI-03 Empty offer | All purchases become invalid before response | Free decline or safe close, no first-option purchase from an all-zero table |
| COST-01 Equality | Each required resource and capacity exactly equals quote | Inclusive affordability succeeds, display and commitment agree |
| COST-02 Shortfall | Reduce one required component by its smallest supported unit | Reject before payment, hold, phase authorization or timer creation |
| COST-03 Quote change | Sale or cost modifier changes before and after acceptance | Current acceptance policy is explicit, accepted work and hold remain frozen afterward |
| COST-04 Other owners | Boom, Depression and unrelated holds coexist | Investment counts availability correctly and releases only its own amount |
| COST-05 Quoted emergency | Apply discounts, a zero quote and low or negative PP | Charge the exact quoted cap, recognize zero political authorization, never repeat a covered same-case fee |
| QUOTE-01 Context factors | Combine non-core, low infrastructure and war, including exact half-maximum infrastructure | Sum at most 30%, multiply once per site, freeze before rounding and use the correct duration envelope |
| WORK-01 Phase accounting | Mobilization, Works and Commissioning each complete | Authorization and paid work are phase-specific, early outputs obey their earned cost share |
| WORK-02 Audit pause | Inspect ordinary and mega projects | 20 or 40 funded days cost capacity but earn no construction progress, one audit per phase |
| ID-01 Replay | Deliver completion twice and after reload | One observed output, terminal receipt, release and history consequence |
| ID-02 Superseded work | Old callback arrives after a new phase or amendment | Exact stale generation fails without modifying current work |
| ID-03 Foreign ROOT | Sender remains ROOT and nested helpers overwrite targets | Frozen recipient receives the correct transaction, caller outputs survive correctly |
| STATE-01 Prepayment capture | Holder changes after preview | Revalidate before spending and reject or reselect legally |
| STATE-02 Occupation | Active site is occupied, then recaptured | Pause and release its hold, retain paid work, require fresh authorization to resume |
| STATE-03 Transfer | Permanent owner change during work | Retire original unearned obligations, preserve real buildings, grant no inherited construction authority |
| STATE-04 Annexation | Payer disappears with callbacks pending | Tombstone its charter, clean via registered states, pay no accidental annexer |
| TIME-01 Inactive cap | Combine shortage, capture and incident delays | Count overlapping reasons once, never reset elapsed inactivity, retire unfinished scope at 180 days |
| TIME-02 Calendar cutoffs | Duplicate and irregular owner callbacks cross due dates | Credit only eligible funded time, with no early or duplicate work |
| SITE-01 Lost delivery slot | Native construction consumes the promised slot | Explicit bounded relocation or smaller legal settlement, no phantom completion |
| FAC-01 Native facility | Test all offered vanilla specializations and illegal sites | Exact native building and group gates, coast and supply rules hold |
| FAC-02 Facility reward | Commission a facility without a completed project | No inferred project, technology, equipment or scientist grant |
| DLC-01 Equivalent branch | Paired fresh all-DLC and no-DLC campaigns | Frozen exclusive bundle, same special work envelope, real bounded comparable value |
| DLC-02 Provider isolation | Ordinary country compared with prepared CXT | Fixture completions cannot counterfeit gameplay payment or provider receipts |
| SALVAGE-01 Reuse | Same payer starts later work at the same site | Credit is at most 25% of corresponding work, consumed once and never reissued |
| ANOM-01 License ending | Run to 180 without extension, then with paid extension | Expiry precedes hazard, extension is paid once and never exceeds 360 total days |
| ANOM-02 Warning | Compare no response, late paid containment and validation | Correct 30-day response and 60-day service deadlines, no duplicate closure fee or expired restart |
| ANOM-03 Inherited operation | Permanent owner-controller with no active charter assumes service | Fresh service-only receipt, unchanged expiry, no pending coupons or inherited construction, operating-day, incident or reward achievement credit |
| ANOM-04 Operating clock | Mix operation with repair, inspection, warning and containment | Qualifying days advance reviews, pauses reset only the achievement streak, expiry retires pending coupons, same-check correction never rerolls |
| ANOM-05 Continued hazard | Explicitly authorize continuation, then resolve its frozen warning | Disclosed conditional cascade risk, observed bounded loss, one receipt and no automatic continuation |
| RNG-01 Checkpoint identity | Cross several thresholds, amend to Fever and reload | Preserved ordered rolls, at most three construction checks, no repeated audit or hidden truth advantage |
| EXP-01 Residual integrity | Add risk near raw 100, inspect, then validate or repair clipped sources | Store actual applied residuals, inspect incident→context→policy→Fever, remove only remaining source amounts, no negative balance or future credit |
| EXP-02 Repeated context | Reaccept, recapture, reduce scope and upgrade policy repeatedly | Context triggers once, policy adds only a new historical maximum, clipped additions never refill after reduction |
| NAT-01 Reachable financing failure | National Fever, initial capacity 20, hold 9, base Exposure 55, corruption +20, then 90 unresolved days and two failed linked sites with at least 2,400 paid civilian-factory-days written off. Separately, test threshold 2 just below and exactly at 25% verified conventional paid-work loss, with half the promised scope failed and a qualifying 35% peak hold | Threshold 1 can qualify before cleanup. Hold 9 adds no 50%-capacity context. Threshold 2 requires the paid-loss floor against its frozen accepted budget, which reductions and cleanup cannot shrink. Unpaid promises and service work add no qualifying loss. Earlier real settlement, inspection or exit prevents either conjunction when its conditions fail |
| OUT-01 Special networks | Compare Regional, National and Grand Materials and Engineering | Refineries or facilities consume two allocations each, support and infrastructure match the frozen legal package |
| SELF-01 Coupon basis | Compare native and no-DLC representations, then reduce agreed scope | Same frozen U/B basis and conventional extra type, reduced unearned basis, legal preassigned placement, no refinery or facility coupon |
| LIC-01 Activation | Finish only the flagship, then the whole agreed scope, with 0, 20 or 120 unused flagship dormant days | No unpaid activation. First service has 0, 20 or 90 days respectively, waiting consumes flagship grace, other sites supply none, timeout earns no premium or coupon |
| DIV-01 Program dividend | Commission early sites, full network, reduced settlement and abandonment | One terminal receipt, 180 or 90 days as applicable, no early dividend, all retained qualifying sites required, no expiry restart |
| ENG-01 Licensed research | Compare operating modes and capability branches while ordinary +5% is live | Correct 10/15/20/30% continuing benefit, strongest same-type contribution, separate one-time bonuses, exact pause and expiry |
| REC-01 Distress recovery | Complete, pause, cancel and overlap recovery with original expiry or Event 35 acceptance | One 30-funded-day attempt within 60 calendar days, exact reduction only on verified success, independent release and unchanged cooldown |
| ACH-01 Final program risk | Sites finish at different risks, final full-program commissioning occurs at Exposure 24 or 25 | A03 samples the single charter value at final full commissioning |
| ACH-02 Fault eligibility | First actionable qualifying malfunction or critical warning after 30 actual operating days, with discounted or zero PP quote | A05 accepts within its 30-day eligibility window and completes 30 funded days within 60, no extra fee or malfunction emergency-close timer |
| CHAOS-01 Attribution | Fire, evolve, operate and contain an anomaly | Zero unlock Chaos, guarded outcome premiums, exact limited repayment and no shared double charge |
| DEP-01 Caller identity | Attempt Event 121 against the pinned gateway | Current code rejects unsupported production identity, approved extension proves its own source |
| DEP-02 Result handling | Exercise accepted 1/2/3, duplicate 4 and positive rejection | Only fresh acceptance acknowledges a new handoff |
| DEP-03 Retired context | Retry after source retirement or a full receipt ledger | Preserve original receipt and durable acknowledgment, never mint around a rejection |
| END-01 Terminal closure | Success, failure, abandonment, capture and retirement | Exact hold release, finite aftermath, no surviving callback that recreates work |

## 6.9 Source and native acceptance

Source acceptance requires resolved definitions, exact identities and scopes, immutable branches and complete terminal paths. Tests must exercise transitions and changed facts. Conservatively discard a temporary created only inside a callee unless the caller preinitialized it.

Native acceptance observes usable capacity, `civilian_factory_use`, missions, state transfer, exact construction legality, modifier expiry, option rounding and visible costs. Run feature-present and feature-absent fixtures separately. Source checks do not establish engine behavior.

The ordinary path must work with evolutions disabled and write no hidden evolution state. Test all four sectors, each ordinary envelope where legal, both special branches, the immutable no-feature bundle and a legal megaproject scale. Validate useful bounded values against current native construction costs, including the declared subsidy and opportunity cost.

If native execution is unavailable, finish authorized source fixes and identify unobserved cases precisely. Do not require the user to perform a live test. Record actual evidence and later canonical specialist results in the review record and Part 8.
