# Fallout orchestrator console fixtures, 2026-10-06

These are bounded synthetic cases for the orchestrator, not engine results produced by this pass.
Load a separate copy of `qa_001_fresh_head.hoi4` for each destructive Fallout or treaty branch.
The save inspection identified USA, 1936.1.1.12, HOI4 1.19.2.0, normal difficulty.
The offline Console commands reference documents `eval_effect` at line 170; installed effects documentation documents country/state scopes and the individual effects used below.

## Manual admission and after-map-return checks

Run Low and Maximum separately through Settings, Scenarios, #014 Fallout, selecting the slider stop before confirming.
In a copy already admitted or collapsed, run `event chaosx.fallout.900 USA`.
Expect exactly one Strike Order Withheld report and no additional strike sweep.
Compare the saved `global.fallout_manual_selected_intensity` with the selected stop.
Expect all 10,154 valid provinces to be struck, a total of 1,081 struck states, and the seven-day countdown before blackout/map return.
Continue as USA and count five Ash-week choices plus one closing report; result acknowledgments 64/68/72/76/80 must remain silent.
The closing text must match the five actual outcomes and installed office.

## Four-member treaty fixture

Use the untouched base before Fallout.
This fixture creates a bounded synthetic treaty without waiting for natural formation; it is not a test of invitation or founder-election logic.
Run the following lines in the console.

```text
eval_effect USA = { air_cleanliness_treaty_initialize_lifecycle = yes set_variable = { global.air_cleanliness_treaty_generation = 1 } set_global_flag = air_cleanliness_treaty_active save_global_event_target_as = air_cleanliness_treaty_founder air_cleanliness_treaty_register_member = yes }
eval_effect ENG = { air_cleanliness_treaty_register_member = yes }
eval_effect FRA = { air_cleanliness_treaty_register_member = yes }
eval_effect CAN = { air_cleanliness_treaty_register_member = yes }
eval_effect USA = { set_variable = { global.air_contamination_bp = 7500 } add_equipment_to_stockpile = { type = support_equipment_1 amount = 100 } add_equipment_to_stockpile = { type = convoy_1 amount = 100 } }
eval_effect ENG = { add_equipment_to_stockpile = { type = support_equipment_1 amount = 100 } capital_scope = { air_winter_initialize_state = yes set_variable = { air_winter_phase = 4 } set_variable = { PREV.air_winter_response_priority_state = id } } }
eval_effect FRA = { add_equipment_to_stockpile = { type = support_equipment_1 amount = 100 } }
eval_effect CAN = { add_equipment_to_stockpile = { type = support_equipment_1 amount = 100 } }
```

Verify the members array contains only USA, ENG, FRA and CAN before treating it as a four-member denominator.
If the source save already carried membership, use a genuinely untouched base copy; do not clear a live campaign's members to fit this fixture.
All four countries must be at peace, membership-eligible, and without a banned/weapons-use history.
At least one peaceful prospective donor must have 30 support equipment at admission, including cases that deliberately drain supplies later.
Use the normal decision panel to call a Relief Vote for ENG.
Caller USA and recipient ENG vote yes automatically.
Human ballot clicks require a multiplayer fixture with human FRA and CAN; switching tags after dispatch does not undo AI choices already made.
For a single-player controlled quorum case, let the other ballots finish by day thirteen, then replace only the synthetic vote arrays before the day-twenty-one result:

```text
eval_effect USA = { clear_array = global.air_cleanliness_treaty_relief_vote_yes clear_array = global.air_cleanliness_treaty_relief_vote_no add_to_array = { array = global.air_cleanliness_treaty_relief_vote_yes value = USA } add_to_array = { array = global.air_cleanliness_treaty_relief_vote_yes value = ENG } }
```

That is two yes/two abstain and must reject even though no member voted no.
In a separate copy, run the same line and then `eval_effect USA = { add_to_array = { array = global.air_cleanliness_treaty_relief_vote_yes value = FRA } }` before closing.
Three yes/one abstain must approve if a payable yes donor remains.
This deliberately controls the close-effect inputs; it does not prove human ballot interaction.
Observe only actual paid deliveries, with at most four and one result per live member.

## Exact PP boundary and one-time refund

To set current USA PP to 24, 25 or 75, use the following effect with the final literal changed to that amount.
The temporary value is deliberately unscoped.

```text
eval_effect USA = { set_temp_variable = { fallout_qa_pp_delta = political_power } multiply_temp_variable = { fallout_qa_pp_delta = -1 } add_political_power = fallout_qa_pp_delta add_political_power = 25 }
```

At 24 the decision cost is blocked; at 25 it is ready and an admitted vote leaves zero PP before ordinary daily income.
An invalid or unfunded vote refunds its saved 25 once; a second cancellation cannot credit more.
To create the unfunded case, admit with a payable donor, then drain every possible donor before the 21-day close.
For this vanilla fixture, use `eval_effect USA = { add_equipment_to_stockpile = { type = support_equipment_1 amount = -100000 } }`, and repeat the same line with FRA and CAN.
ENG is the recipient and never pays a relief pledge.
Expect no aid, no recipient rejection penalty or 180-day target lock, and fourteen days before another vote can open.

The standard timing test must run without Easy Decisions.
In a separate debug copy, toggle `easy_decisions` and repeat cancellation/unfunded cases: the admitted owner effect still charges 25, refunds only that amount, and the global fourteen-day report gap prevents a second one-day session from overwriting the first result report.
Toggle `easy_decisions` back after this isolated test.
Observe AI callers too: custom-cost affordability is explicit, but native AI reserve behavior is not established by the blocked probability routes.

## New Zealand and portrait consumers

In a Fallout run launched while playing USA, let AI NZL qualify after its pre-snapshot Samoa disposition.
After map return, `tag NZL` for the ordinary in-place base-save case.
If allocation created a dynamic output instead, use the actual output tag from the resulting text save rather than guessing a token.
Expect Lifeboat Parliament as leader and the dedicated 42-focus tree.
Complete the Relief Speaker and Harbor Constable routes in separate copies and expect their declared leaders, traits and large portraits rather than a raw character token.
Complete Dairy Relief Fleet, Storm Port Engineers and Radio Weather Chain; satisfy their normal resource/ownership gates and inspect all three advisors, costs 45/45/25 and traits.
Radio Service Board must show the attributed institutional source card; its painted final remains pending user input.

## Inspection and reconstruction

Open the verification response while affordable, drain the required response equipment, then choose it.
Expect one supplies-unavailable report and no reopened response or finding against the member.
For reconstruction, keep two surviving former members at peace and unbanned.
Propose A to B; C to B and B to C must remain unavailable while that exact pair is reserved.
Test acceptance, refusal, annexation and capitulation of each participant in separate copies.
A surviving proposer recovers its Recognition deposit exactly once on failure/loss; a stale answer must close without changing a later pair.
The same refused pair remains unavailable for 365 days.

## Visible consumers

At 1920x1080 scale 1, 1366x768 and 2560x1440, inspect the blackout message, all viewport edges and pointer regions, with transition active and then hidden.
Clicks must not advance the transition or affect the underlying map; keyboard exclusivity remains an unresolved native capability.
Inspect the Static Winter Map checkbox, tooltip and click region, toggle it through the existing monthly update, then Reset All Settings.
Inspect all generic focus icons and shine states, the compacted endpoints, the USA decision/category icons, both NZL rescue icons, and the thirty repaired framed reports.
Use the specific representative events and achievement conditions listed in `takeover_status_2026-10-06.md` rather than arbitrary forced chain results without authenticated receipts.
