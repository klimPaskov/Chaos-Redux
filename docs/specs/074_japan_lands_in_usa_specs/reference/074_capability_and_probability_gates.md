# Capability and probability gates

This file separates requested behavior from verified engine capability.
All live-game and HOI4 MCP results are pending.
The repository evidence listed in the source register is useful precedent and does not replace current-version tests.

## Blocking implementation gates

| Gate | Required evidence | Unacceptable substitute |
| --- | --- | --- |
| G01. Legal defended landing | A province-level control and spawn prototype preserves defenders, ownership, valid movement, and actual deployment under a defended coast | Deleting defenders, transferring the whole state's ownership, or leaving the promised army at home |
| G02. Geographic profiles | Current game/map IDs, province adjacency, ports, cities, railways, hubs, airfields, legal selection and spawn positions | Assuming legacy state 378 proves all current map data |
| G03. Creation accounting | Actual manpower and equipment before and after creation with exact template manifests | Paying the embedded equipment twice or calling empty divisions ready |
| G04. Supply isolation | Measured demand and coverage with Japan unable to supply across the Pacific, including partial-state and port-loss tests | An unsupported local warehouse, a worldwide supply bonus, or permanent immunity |
| G05. Air packages | Valid equipment, variants, wings, fuel, range and airfield consumers across the supported DLC profiles | Granting a designer hull without a usable configuration |
| G06. Ordinary grant technology | Supported templates and equipment for low-tech Japan, with any necessary grant-only unlock explicitly validated | Undoing another event's research loss or unlocking an entire modern tree |
| G07. Local operations | Verified actor and geographic scope for movement, recovery, preparation and defense benefits | Country-wide combat buffs described as local |
| G08. AI retention and exploitation | Observed mainland deployment, orders, reinforcement choices, enemy response and ordinary retreat | Declaring success because a strategy definition parses |
| G09. Dispatch and fire-once | Existing selection, history and cooldown order inspected, invalid placement consumes nothing | Root rejection after the shared event has already been recorded |
| G10. Paid transactions | Effective cost parity, recorded reservation, save persistence, success and refund receipts | Refunds inferred from missing units or debits repeated at completion |
| G11. Timing and weighted behavior | Current-version probability adapter and named scenarios reviewed by the probability auditor | Treating weights as percent chances or claiming a 90-day MTTH is a deadline |
| G12. Presentation consumers | Exact native category and mission consumer references, sprite wiring and actual-byte exports | Native-looking mockups presented as implemented GUI |
| G13. Super-event research | Checked final text, quotation context, licensed recording, slot collision audit and actual sound wiring | Working labels or default music promoted as finished presentation |
| G14. Independent closure | Executed near-completion improvement pass and completion audit with all findings disposed | Calling this author-written plan an independent subagent audit |

A blocked gate is not permission to silently replace the requested mechanic.
Record the concrete failing capability, reproduction case, and available evidence under `docs/plans/074_japan_lands_in_usa_plans/`.
Resolve it before marking the associated feature complete.
The package's baseline includes the features behind G01 through G09, so those gates are not optional polish.

## Map-profile worksheet

Resolve southern California, the Bay Area, the Oregon coast and Columbia approach, and Washington/Puget access against the actual map.
For each profile record the game version, map mod, state IDs, legal province IDs, owner and controller requirements, port locations and levels, connected deployment cells, protected defender locations, airfield capacity, reachable transport links, and ordinary objectives outside the initial footprint.

A profile must explicitly identify which provinces are granted wartime control and which remain American targets.
A state name cannot stand in for that geometry.
Store the immutable opening footprint separately from the live operating registry.
Only the immutable snapshot decides whether a later conquest was outside the opening for achievements and Chaos.

Support simultaneous high-tier profiles without demanding every profile be legal.
California retains priority over Oregon and Washington when safely usable.
Map feasibility cannot become a check for naval supremacy, Japanese strength, American garrison weakness, or Japanese noncapitulation.
A heavily defended but legally valid coast must be tested, not permanently excluded through an invented strength requirement.

## Persistent transaction contract

These are required concepts, not claims that the exact field names already exist.
Use repository conventions after inspection.

Keep permanent receipts for the consumed root, original landing date, frozen campaign factor, prelanding achievement conditions, immutable footprint, realized starting tier, highest realized tier, issued force by role, issued material by equipment family, initial embedded manifest, named reserve lots, paid reservations, paid completions, earned and reversed Chaos credits, news, super-event, and achievement evidence.
Keep the support-closed state distinct from campaign-operations-closed and from the ordinary game's war state.

At a successful root, snapshot inputs, resolve legal geometry, prepare buildings and support, assign wartime control, create and verify the promised force and material, then record the committed episode and publish reports through the shared dispatcher order.
HOI4 script does not provide a general rollback database.
The implementation must therefore build a nonyielding validated commit sequence and prove its failure behavior, rather than claim perfect rollback from a design diagram.
Any irreversible state change needs a proven completion path before the dispatcher consumes the event.

On a higher tier, compute remaining cumulative entitlement from receipts, not surviving units or current stockpiles.
Record pending entitlements separately from actual issue.
Reloading a pending or completed operation must not execute it again.
If a map target changes between request and completion, use the explicit reservation/cancellation rules.

## Paid-action cost and resolution contract

J01 and U01 reserve and debit their full effective listed costs at the start.
Their organization period grants no field effect.
A valid completion consumes the reservation and creates exactly one batch without a second debit.
Precompletion legal invalidation or unavailable legal assembly after bounded reselection refunds the recorded reservation once.
Cancellation never refunds a delivered batch.
The request cooldown is not reset by canceling and rerequesting.

J02, J03, J04, U02, U03, U04, and U05 debit their complete effective cost when field preparation starts.
That work is a committed operational expenditure.
Losing the target to combat, losing its route, or ending the war cancels unfinished benefits without a resource refund.
A rejected click before any work starts changes nothing.
The interface must make this distinction clear before purchase.
All seven preserve real completed construction even if later fighting destroys the local advantage.

Native automatic PP cost and custom scripted PP debit must not both charge the same amount.
Universal cost modifiers apply consistently to displayed, affordable, reserved, spent and refunded values.
Refund the historical paid amount, not a recomputation under a later modifier.
Only the completed project consumes its lifetime completion allowance, but every started field project spends its cost.
Changing targets cannot reset a once-per-location completion record or an action cooldown.

## Army rounding and entitlement example

The design's campaign factor is a declared deterministic formula, not probability output.
For 250 prelanding American divisions, it is 1.15.
The four immediate targets become 35, 70, 115, and 175 after rounding to the nearest five with halves upward.
Apply the same rounding rule separately to the lifetime total and derive the additional remaining allowance from that total.
This keeps all generated batches in units of five and makes role allocation reconcile exactly.

For example, the tier III lifetime total is 180 × 1.15 = 207 divisions before rounding, which becomes 205.
With 175 immediate divisions, 30 remain available as follow-on divisions.
Do not separately round the original follow-on number and then accidentally exceed the rounded lifetime total.
An implementation test must cover every five-point factor step from 1.00 through 1.50.

## Named probability scenarios

| Scenario | Controlled inputs | Questions for the auditor |
| --- | --- | --- |
| P01. Ordinary baseline | Both actors stable, California valid, Chaos below 200 | Are only legal profiles selectable and are ordinary decisions useful? |
| P02. Japan collapsing | Minimal navy, empty national equipment, high surrender progress | Do these conditions improperly suppress landing selection or American urgency? |
| P03. Strong USA | American division counts around each scaling boundary | Are there discontinuities, order reversals, or unintended unlimited scaling? |
| P04. Damaged primary port | Supply adequate before damage, limited after damage | Does unloading repair outrank offensive preparation without repeatedly buying a useless repair? |
| P05. No access | All registered access lost for 1, 7, 29, and 30 days | Are deliveries zero-weight when invalid and permanently closed at the right point? |
| P06. Split pockets | Two or three high-tier regions, one port threatened | Do linking and defensive actions outrank an unrelated inland offensive? |
| P07. Active evolution | Chaos 199, 200, 399, 400, 599, 600 and each toggle combination | Is the next enabled stage selected correctly with no disabled-stage history or stacked upgrade burst? |
| P08. Changing Chaos | Threshold crossed, then falls below it, then returns | Does timing use the correct eligible periods and the verified adapter? |
| P09. Support near expiry | Eligible for upgrade close to an absolute deadline | Does actual closure prevent late free extensions and revive nothing after permanent closure? |
| P10. Resource shortage | Each action just below, equal to, and above its effective cost | Are costs, affordability and willingness aligned without an overdraft? |
| P11. Multiple wars | Japan needs home defense and USA has a distant theater | Does the new front receive priority without a global abandonment order? |
| P12. Human transition | Human/AI switches for either actor and a save reload | Do entitlement, target, timing and strategic ownership remain stable? |

Required sequence is inspection, named evaluation, threshold sweep, justified simulation, comparison after revisions, and rendering when it improves interpretation.
Declare exact, bounded, sampled and unresolved results separately.
No numeric chance, completion probability, or balance conclusion in this package is attributed to an unexecuted tool.

## Country and feature scope

| Surface | Japan | United States |
| --- | --- | --- |
| Tag and country identity | Reuse existing JAP | Reuse existing USA |
| Government, party, ideology, names and flags | Preserve all existing routes and assets | Preserve all existing routes and assets |
| Focus tree | Preserve existing tree | Preserve existing tree |
| Leaders and commanders | Reuse valid existing characters without clones | Preserve existing characters |
| Units | Grant ordinary validated invasion formations | Paid ordinary emergency formations |
| Decisions and missions | Four action families, at most two simultaneous missions | Five action families, at most two simultaneous missions |
| AI | Mainland operating priority while useful | Urgent mainland defense while useful |
| New equipment, doctrine, 3D units or tags | None planned | None planned |

Any necessary technology grant must still be inspected with `hoi4.tech_inspect`, rendered with `hoi4.tech_render`, and compared with `hoi4.tech_compare`.
A grant profile is not permission to rewrite the technology tree.
There is no reason to perform a new-tag production pipeline while this scope remains unchanged.
If an approved later addition introduces a tag, the full vanilla, Chaos Redux, Workshop and local-mod collision audit becomes mandatory before creation.
