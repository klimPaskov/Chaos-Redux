# World Claims: decision and mission contract matrix

Working identifiers below are proposed, not registered runtime IDs. Tuning formulas are owned by `086_world_claims_tuning.md`. Costs use exact quoted amounts, inclusive affordability checks, one payment receipt, and no more than three inline payment values. The set of spendable payment types is PP, support equipment, trucks, and trains.

| Working family | Visibility and validity | Start / payment | Active state | Success | Failure / cancellation | AI intent |
| --- | --- | --- | --- | --- | --- | --- |
| `wc_select_ambition` | I+ feature active, candidate fits holdings, resolver and resources valid | Free, freeze envelope/anchors/thresholds/signature | One selected project, switch lock 90 days | Chosen project and optional-claim priority | Invalid candidate cannot be adopted; old selection remains until new commit succeeds | Prefer fit, access and continuity |
| `wc_civil_integration` | Controlled noncore WC target, current Compliance at most 90, family reward unconsumed, real administrative connection, free project slot | PP and support by R formula, freeze quote and anchors | 120 days of continuous target/anchor control and connection validity | Add 10 claimant-specific Compliance points up to 100, mark receipt | Target or anchor loss fails, no recovery grace in this initial implementation; native context invalidation is separately diagnosed | Valuable low-Compliance target, defensible, resources above reserve |
| `wc_connect_heartland` | 2 distinct held anchors, actual connected corridor of 2–25 states, supported connection predicate, at least one uncredited WC target, free slot | Trucks and trains by G formula | 180 days continuous corridor and anchor control; usable native connection at completion, permitted repair during mission | Grant 25% preparation credit once to selected eligible relationships | Any corridor control loss fails; unusable connection at deadline fails; no refund after ordinary progress | Prefer a reachable, defensible connection that matters to chosen ambition |
| `wc_frontier_pledge` | 75% envelope possessed, all anchors held, current selected signature, free slot | Free, freeze exact anchors and requirement | 180 days, no anchor-control interruption | Holding milestone only, still recheck live formation predicates | Anchor loss fails, disappointed 90 days, retry lock 90 days | Only near-ready defensible project |
| `wc_offer_assurance` | Actual public overlap, two distinct living governments, ordinary diplomacy allows contact, no incompatible ongoing war/offensive, no duplicate agreement, below agreement cap | Offer reserves no PP. Acceptance atomically rechecks both parties and charges 25 each | Offer expires after 30 days; accepted term is 180 days; one agreement record shared by both | Suspend event-owned offensive pursuit in overlap; at term end reverse eligible linked crisis amount at most 5 once | Refusal/expiry costs zero; declaration/incompatible commitment breaches once; later technical invalidation cannot create extra reversal | Prefer containment against stronger alternative threats, avoid invalid conflicting commitments |
| `wc_proclaim_dynamic` | Independence, current profile permits scale, Q/E and I/Q thresholds, anchors, holding, resources and identity coverage ready, reward unconsumed | PP by E formula, once | Commit transaction, no separate timer | Territorial recognition, optional prepared identity, connected remainder objectives, one confidence period, successor discovery | Stale predicate or invalid resource means no payment and no partial cosmetic change | Usually take earned result, respect existing identity ownership |
| `wc_bridge_native` | Genuine provider conditions, territory policy, DLC and source integration verified | Native cost only | Native completion owns transaction | Native effects once, compatible WC recognition and provenance only where independently warranted | Provider failure preserves WC state; never invoke its effect unconditionally | Prefer eligible genuine provider over a near-copy |
| `wc_consolidate_proclamation` | Unconsolidated completed ambition, formed/retained-identity route, anchors held, free slot | Free | 180 days with anchors and required integrated share retained | Durable achievement/successor milestone | Required share or anchor loss fails, disappointed 90 days, retry lock 90 days | Take when territory secure |
| `wc_browse_or_change_page` | Valid prepared candidate/page | Free, no payment or reward | Presentation only | Select visible page or preview | Unknown page reports incomplete resource coverage | AI does not use GUI controls |

## Transaction ordering

An acceptance or completion resolves current country identities, target validity, profile features, prior receipts, live territory, affordability, and asset/provider readiness before payment. After payment it records the transaction identity and commits effects once. A queued acknowledgement is not a second execution point. The final implementation must prove an engine-safe ordering or recovery mechanism for partial failure.

For a bilateral assurance, a pending offer contains the two claimant epochs, frozen overlap, quoted PP, expiry, and optional linked crisis receipt. If either party cannot pay at acceptance, neither pays. Do not charge the proposer merely for sending a refused proposal. A stale offer cannot bind a released successor or a different country reusing the same tag.

## Targeting and cost descriptions

Civil integration targets one state. R is the declared administrative group used only to price the work. Its UI must not suggest every state in R receives +10. A connection project affects only the frozen corridor's selected WC relationships. Already credited members get no duplicate credit. Minimum group size is two because two distinct anchors are required.

Claims and earned cores are automatic. None of the above decisions becomes a hidden prerequisite for those universal benefits. A player with no spare equipment retains the event's baseline power.

## Assurance breach and pursuit

A passive wave that grants a new claim does not breach an assurance. Starting a WC pledge explicitly directed at the protected overlap, making a new ordinary declaration against the partner, or initiating another documented incompatible WC offensive commitment does. Existing wars make the original assurance invalid rather than being retroactively ignored.

Normal diplomatic treaties, native peace, claim removal, and state transfer are outside this agreement's automatic effects. A provider or shared diplomacy system may expose a valid peace action through its own rules. World Claims does not create an unauthorized surrender operation.

## Limits and cancellation

Two active projects and two active assurances are separate caps. A free pledge still consumes a project slot. Browsing and proclamation do not. The country sees three to five relevant primary actions with a hard limit of six; candidates and pages are selectors, not additional paid-action rows.

A technical cancellation before any progress or benefit can refund exactly the unused quoted commitment once. The implementation must distinguish that receipt from refunds granted by other systems. Defeat, lost control, resource scarcity after payment, and voluntary abandonment after progress are ordinary failures without refunds.

A map-registry mismatch suspends affected systems and records a migration blocker. It does not reinterpret all in-progress projects as free refund opportunities. Country annexation retires active projects and receipts under lifecycle policy. Save/load is neither success nor cancellation.

## Units

Player percentages are percentage points. The Compliance contract uses 0–100 values if confirmed by the installed effect documentation. Native Stability and War Support modifiers may use fractions, so +10 percentage points must be converted once through the correct documented unit. Do not infer a decimal scale from a similar-looking modifier. Equipment counts and PP are integer amounts.
