# Event 016 Containment and Sovereignty

## Purpose

The sovereignty board is the final hosted Directorate crisis. It does not select an outcome by a new random roll. Every action is resolved against the institutions, facilities, security posture, project history, foreign relationships, Dependence, Independent Capacity, and Grievance produced during the preceding chain.

The board is decision-led and remains inside the host's existing national-focus tree. It opens after the fourth and final logged evolution, `Sovereign Science`, unless the disabled-evolution safety route has already concluded the chain through the regional compact.

The deadline and outcome reports also resolve a scripted policy clause from the recorded Evolution IV choice. The clause names a supervised compact, binding charter, concession, military seizure, foreign containment, or refusal before the outcome text, with an unrecorded safety line for migrated or malformed state. It is presentation only: the existing containment resolver remains responsible for authority, dependence, independent capacity, grievance, project history, territory, character ownership, and Kruger State formation.

## Sequence

1. Evolution IV records one response: charter, concession, military seizure, foreign containment, or refusal. Concession is offered only after institutional capture is already proven.
2. `brilliant_scientist_start_sovereignty_deadline` prepares a live territory plan, selects one valid exile recipient, calculates the opposing hidden strength scores, and activates the visible sovereignty mission.
3. The host can execute one timed decision. Every decision pays Political Power and Stability, commits one temporary consumer-goods burden, and may pay one physical or operational cost. Selection records an action-specific receipt and hides the other responses until it ends.
4. Completion rechecks every mutable fact. Release, exile, charter, and concession must still satisfy their legal or causal contract. Coercive actions recalculate both strength scores immediately before resolution.
5. A valid result is recorded once, the mission and persistent exile target are cleared, and the outcome report is fired. If a route has become invalid, no land or custody changes; event `.32` reopens the board for another explicit choice.
6. If the deadline expires, event `.30` executes the response selected during Evolution IV against the same current-state checks. The timer does not introduce a random alternative.

## Visible actions and costs

| Decision | Time | Immediate payment | Temporary consumer-goods factor | Governing risk |
| --- | ---: | --- | ---: | --- |
| Release Kruger | 21 days | 25 Political Power, 2% Stability | +3% | Only a low-dependence, low-autonomy, small-site Directorate can leave cleanly |
| Arrange Exile | 30 days | 40 Political Power, 20 convoys, 3% Stability | +3% | Recipient and transfer validity are rechecked atomically |
| Arrest Kruger | 30 days | 55 Political Power, 600 Support Equipment, 5% Stability | +6% | Government and Kruger strength scores decide custody, defection, uprising, or crisis |
| Close the Directorate | 45 days | 65 Political Power, 200 trucks, 7% Stability | +6% | Strong independent production and dangerous projects can resist demolition |
| Ratify the Charter | 45 days | 75 Political Power, 600 Support Equipment, 4% Stability | +10% | The laboratory territory and former-host viability must both pass revalidation |
| Seize the Laboratories | 21 days | 85 Political Power, 6,000 Infantry Equipment, 10% Stability | +10% | The largest government bonus, but high autonomy and weaponized projects can still defeat it |
| Allied Containment | 30 days | 65 Political Power, 20 Command Power, 6% Stability | +6% | Faction membership is required; allied support strengthens containment while foreign contacts create a defection route |
| Concede Authority | 30 days | 50 Political Power, 300 Support Equipment, 8% Stability | +10% | Available only when the Directorate already controls the host's institutions |

The costs are centralized in `common/script_constants/016_brilliant_scientist_containment_constants.txt`. The decision descriptions deliberately describe present facts and consequences rather than expose the numeric hidden scores.
The cost row displays three entries for release and four for each other response, using the matching Political Power, equipment or Command Power, Stability, and consumer-goods texticons.
Each upfront payment independently turns red only when that payment cannot be met; the other entries retain their normal colour.
Affordability accepts the exact displayed Political Power, Stability, and equipment or Command Power amount; consumer-goods demand is a temporary factor, not a stockpile payment or a second factory-efficiency penalty.
Each action's `brilliant_scientist_can_pay_containment_*` trigger is called by both `available` and `custom_cost_trigger`, so selection and the cost display use the same payment boundary.
The availability copy is hidden only from the prerequisite text because the complete payment is already shown in the cost row and its tooltip.
No separate manpower, fuel, Army Experience, train, or secondary-equipment deduction is hidden in these actions.
Preparation is spent immediately and is non-refundable on interruption or invalid final revalidation, while the native decision owns removal of the temporary consumer-goods burden.

The payment shape intentionally keeps political and industrial disruption while concentrating physical preparation into one action-specific requirement.
Exile pays maritime transport, arrest pays security equipment, shutdown pays demolition transport, charter and concession pay administrative equipment, seizure pays weapons, and allied containment pays command coordination.
These inputs do not add success points; the existing recorded causal state still determines whether containment succeeds.

## Causal resolution

The government score derives from Mandate, low Dependence, low Independent Capacity, independently replicated scientific families, public or military oversight, state security, military guards, hardened facilities, foreign or faction backing, and the chosen coercive preparation.

Kruger's score derives from Independent Capacity, Dependence, Grievance, the number of actual facility states, deployed and weaponized project families, private guards, sovereign authority, compromised government control, dangerous incidents, failed assassination attempts, and a multi-site network.

The score margin has four useful regions:

- decisive government control permits confinement or shutdown;
- a smaller government edge can still succeed after bounded resistance;
- sufficient Kruger strength plus a viable enclave creates a laboratory uprising;
- decisive Kruger strength plus a viable broader plan creates the Kruger State, while proven institutional capture can transform the host without secession.

When Kruger can resist but no viable country territory exists, the result is a noncountry laboratory crisis. This is its own specified outcome and does not transfer arbitrary land.

## Persistent history and cleanup

The host records the selected action, action date, outcome, outcome date, and an irreversible `ever_*` flag for the exact result. Project learning already reproduced by national institutions remains available to aftermath consumers. Personal project history remains on `KRG_warren_kruger`. Active Directorate facility markers become former-site markers on nonsovereign departure, preserving later theft, cleanup, and aftermath hooks.

The same Kruger token is transferred through the existing guarded transaction. It cannot be recruited twice, cannot move into an invalid recipient, cannot transfer while assigned to an active special project, and does not replay the original appointment reward.

Transfer validates every input before cancelling an expedition or changing host ownership.
The pending breakthrough retains its own family and stage snapshots while separate iterators copy the completed and pending history arrays.
Permanent departure and confirmed death clear pending host-reaction obligations while the canonical character is still available.
Confirmed death also closes live foreign frameworks without deleting the assassination actor's settlement targets or permanent operation history.

Split sovereignty first secures the territory and inheritance snapshot, then clears the former host's pending reactions and live foreign partner/site pointers.
Same-country takeover clears only pending reactions, preserving earned policy benefits and the country's resolved reaction history.
Host-only reaction schedulers and delayed events exclude both sovereign carrier forms, so an unresolved report cannot be rescheduled after either transition.

### Timed-action receipt

All receipt helpers run in the acting country.
`brilliant_scientist_begin_containment_action` takes `ACTION`, `POLITICAL_POWER`, and `STABILITY`, with positive payment values, and records `brilliant_scientist_active_containment_action` plus the historical start date before debiting the two common payments.
The selecting decision debits its own optional equipment or Command Power anchor exactly once; the native decision modifier owns consumer-goods demand for the timer's lifetime.
`brilliant_scientist_containment_action_is_live` checks the supplied `ACTION` against that receipt, current hosting, the in-progress lock, an unresolved board, and absence of world end.
Both completion and cancellation use that predicate, and `brilliant_scientist_cancel_containment_action` clears state only when its supplied action still owns the receipt.
Board closure and invalid-route reopening clear the receipt; permanent history and the latest start date remain.
An old timer therefore cannot resolve its former action or clear a newer action's lock.

Example country-scope invocation after validating the decision's complete cost and route:

```text
brilliant_scientist_begin_containment_action = {
	ACTION = constant:brilliant_scientist_containment_action.arrest
	POLITICAL_POWER = constant:brilliant_scientist_containment_cost.arrest_political_power
	STABILITY = constant:brilliant_scientist_containment_cost.arrest_stability
}
```

This private helper starts a paid native decision; it is not a public free-grant API or an outcome resolver.

## Assets and wiring

- Report sprite: `GFX_report_event_016_brilliant_scientist_sovereignty_confrontation`
- Runtime DDS: `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_sovereignty_confrontation.dds`
- Sprite registration: `interface/016_brilliant_scientist.gfx`
- Events: `events/016_brilliant_scientist_containment_events.txt`
- Decisions: `common/decisions/016_brilliant_scientist_containment_decisions.txt`
- Localisation: `localisation/english/016_brilliant_scientist_containment_l_english.yml`
- Dynamic policy and per-payment colour selection: `common/scripted_localisation/016_brilliant_scientist_containment_scripted_localisation.txt`

Decision icons currently use registered vanilla political-discourse, operation, oppression, industry, and civil-war preparation sprites. Dedicated project and Kruger State art is tracked in the Event 016 asset manifest and is not substituted by an unregistered sprite.
Cost text uses the installed vanilla `GFX_pol_power`, `GFX_stability_texticon`, `GFX_consumer_goods_texticon`, `GFX_convoy_texticon`, `GFX_infantry_equipment_text_icon`, and `GFX_command_power` sprites, plus the existing `GFX_support_equipment_text_icon` and `GFX_motorized_equipment_text_icon` registrations in `interface/chaosx_texticons.gfx`.

## Future extensions

- Foreign governments that materially funded containment can receive post-settlement reparations or laboratory-access negotiations.
- Former laboratory sites can develop cleanup, black-market, or restoration decisions based on their exact project-family history.
- A peaceful charter can gain bilateral border commissions distinct from the hostile former-host crisis route.
- A noncountry laboratory crisis can expose regional intelligence operations without granting a country until a later viable territorial seizure occurs.
