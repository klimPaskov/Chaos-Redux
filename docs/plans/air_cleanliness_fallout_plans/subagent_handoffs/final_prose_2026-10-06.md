# Fallout final prose handoff

Status: implemented bounded text cleanup, parent review pending.
Acceptance basis: parent assignment under user G3 and G6.
Ownership: only localisation/english/fallout_consolidated_l_english.yml and this handoff.
No gameplay, spreadsheet, Git, portrait, or asset edits.

## Outcome and scope

Reviewed all 537 baseline values containing literal ledger or receipt language after excluding bracketed dynamic tokens.
Each use received a contextual replacement, and the final scan has zero literal ledger, receipt, transaction, snapshot, provider, id, or segment words.
Also rewrote generic short acknowledgments and implementation-only tooltip bookkeeping.
The technical pilot wording in chaosx.fallout.114.d_option.tt became a limited state access agreement.
Remaining pilot names refer to real river or ice navigators and were preserved.
The continued G3 pass below removes all remaining literal record and records wording, including physical document uses, with exact nouns or concrete actions.

## Validation and invariance

Every changed value retains its original ordered bracket tokens, numeric literals, section-sign formatting codes, texticons, and escaped newline count.
Values alone changed.
The edit loop retained each original prefix, suffix, physical line ending, and every unmatched line byte for byte, with a pre-write reread to reject concurrent modification and an atomic sibling os.replace.
The BOM is preserved.
No dynamic localisation was added or renamed.
Missing-key list: no new keys introduced or references changed.
Duplicate-key list: none in this YML.
Scripted-localisation issue list: no selector or call changed.
Encoding concerns: none found.
python .tools/report_colour_audit.py --event fallout returned total keys with colour: 0.
No sourced or attributed quotations were altered.
The edited set contains no sourced quotation whose wording required an exception.

## Prose before and after

Vagueness: food and feed ledgers now describe supplies, shortages, and deaths directly.
Bloat and obvious explanation: internal cause-memory preservation and success-record clauses were removed from tooltips while visible effects and review timing remained.
Repetition: generic Record and Close record options now acknowledge the event's people, place, or choice.
Overcomplication: inspection ledgers became actual inspection rules, cargo accounts, patient lists, or agreements according to context.
Style repairs: operator trust and military ceremony changes describe their social consequences directly.
No effect, cost, numerical value, target token, selector, or route id changed.

## References and MCP limits

Skills read: chaos-redux-events, chaos-redux-subagents, chaos-redux-focus-trees, chaos-redux-decisions-missions.
Offline wiki Localisation, Formatting variables lines 184?215, revision 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064, read through reference_read.
Installed loc_formatter_documentation.md lines 14?38 were read locally, with example custom_effect_tooltip = advisor_desc|hjalmar_schacht.
The reference_context and reference_search routes were healthy.
Event inspect and options render were partial, with global unresolved event diagnostics.
These artifacts do not establish complete event popup, wrapping, or overflow coverage.
Event lint URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc07a03be662828b5ebe0d76e73558037a51d81f4448a5530d089e72e21e70b7/3d60fd6a2bed8dd70076a629c5e7bd7e09ae63fa7b782c0c10ba4efd96b0f90a/event-lint-2a0caf0ec025.json
Event options URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64ea6d09dcab8abf3ea434d80e41bb931553f94846c6bec33461641e8c398931/930c4d9f9d6cc1fdfe321ffd380809aeca0fc66c7e45a4248af348dc47f245cc/event-options-2a0caf0ec025.json
Event revision: 2a0caf0ec0259474b549e5486b066cfaf12a1e48dbc89844e864851c5fe44e35.
Focus inspect resolved all 82 titles across the three Fallout trees.
Focus inspect URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d5e683b7ff9961ed7f02d975c33b2caaab6f507659860d38ae01c2c7334b81b/61231da8037aa7f755938721a3be70a18a496d727f94db8b2f6a7ce92d7946f6/focus-inspect.e0b9f629c5b469d7.json
Focus revision: e0b9f629c5b469d7873491bf5da1a21aa5039f7a05bb23bc7ced7b4cda8e3aa8.
The inspector reported NZL_fallout_relief_speaker and NZL_fallout_harbor_constable as missing static leader references.
The parent identified the related runtime generation/template risk and owns the separate loader repair.
No character tokens or names were changed here.
focus_render rejected cropFocusIds with FOCUS_CROP_REQUIRES_RASTER.
The subsequent focus_raster produced a title crop for fallout_nzl_publish_the_berth_ledger.
Focus crop URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/583dede07a0c00e92333cfc4174d1915b1d068a5cb59a24d0436f9c5d15bec26/a9981571f79dd28dfe13fb1fdce0e53bdb95f20cb612688d80a224d15f457854/fallout_nzl_lifeboat_focus_tree.focus-problem-fallout_nzl_publish_the_berth_ledger-a5a71049.png
Artifact delivery succeeded but crop image inspection was not completed.
A read-only blackout-window GUI inspect returned GUI_BUTTON_EFFECT_MISSING, clipping and click-bounds diagnostics under a generated scenario.
No blackout text was edited, so this is not evidence for changed-text visual coverage and no GUI change was authorized.
GUI inspect URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc76b64220f1d6ba7ce85149df787e6b1525df59a2c9d5afc6c498e5de87de27/4aec06d9f7a67a0a15e236e5b81feda38bd86cc00765653668f0164f9c7ac5f3/gui-inspect.6ddaf038e7d63971.json
No standalone Technology Tree Viewer route appears in the connected tool inventory.
That is a package exposure gap, not a service-health finding.
Technology and map content were outside this bounded assignment.

## Cross-surface handoff and remaining uncertainty

No workbook was edited.
The final key/value list below is the wording source for any catalog fields that mirror these strings.
No workbook-level mismatch claim is made because catalog review was outside ownership.
Parent-owned event-log/detail and GUI render coverage remains incomplete.
No plan for a missing mechanic was required.
No gameplay simplification was introduced, but complete visual validation is not claimed.

Original-pass unique changed keys: 854.
Original-pass SHA-256 is superseded by the continued-pass hash below.

## Final changed keys and values

### air_winter_prepare_evacuation_ledger

Source line: 84.
Before: Prepare an Evacuation Ledger

After: Prepare an Evacuation Plan

### air_winter_prepare_evacuation_ledger_requirements_tt

Source line: 89.
Before: Select an owned and controlled state in Air Winter phase 3. It must not already have a completed evacuation ledger. No other emergency measure may be underway and its response teams must be ready.

After: Select an owned and controlled state in Air Winter phase 3. It must not already have a completed evacuation plan. No other emergency measure may be underway and its response teams must be ready.

### air_winter_controlled_evacuation_requirements_tt

Source line: 113.
Before: Select the priority state in Air Winter phase 4 with a completed evacuation ledger and at least [?constant:air_winter_response_result.minimum_source_population_k|0]K population. A different eligible reception state must be designated. The resulting Refugee Pressure there cannot exceed [?constant:air_winter_response_evacuation.receiver_pressure_ceiling|0]. No other emergency measure may be underway.

After: Select the priority state in Air Winter phase 4 with a completed evacuation plan and at least [?constant:air_winter_response_result.minimum_source_population_k|0]K population. A different eligible reception state must be designated. The resulting Refugee Pressure there cannot exceed [?constant:air_winter_response_evacuation.receiver_pressure_ceiling|0]. No other emergency measure may be underway.

### air_cleanliness_treaty_seed_archive_exchange_desc

Source line: 172.
Before: Pack seed grain, crop-testing ledgers, and greenhouse cuttings from our breadbaskets and seed vaults for a fellow member. The shipment deepens their winter food stores and leaves both governments a seed record to plant from if the sky never clears.

After: Pack seed grain, crop trial notes, and greenhouse cuttings from our breadbaskets and seed vaults for a fellow member. The shipment deepens their winter food stores and leaves both governments a seed record to plant from if the sky never clears.

### chaosx_air_treaty.11.d

Source line: 202.
Before: Sealed crates of seed grain, crop-testing ledgers, and greenhouse cuttings have arrived from [air_cleanliness_treaty_seed_archive_donor.GetNameDef]. Agronomists are dividing the stock among [?air_cleanliness_treaty_seed_archive_last_state_count|0] of our winter-stricken states and setting a reserve aside in case the sky does not clear.

After: Sealed crates of seed grain, crop trial notes, and greenhouse cuttings have arrived from [air_cleanliness_treaty_seed_archive_donor.GetNameDef]. Agronomists are dividing the stock among [?air_cleanliness_treaty_seed_archive_last_state_count|0] of our winter-stricken states and setting a reserve aside in case the sky does not clear.

### air_winter_seed_vault_preservation_industry_state_desc

Source line: 278.
Before: Warehouse space, transport crews, and factory maintenance are supporting guarded seed stores and trial plots until the spring ledger closes.

After: Warehouse space, transport crews, and factory maintenance are supporting guarded seed stores and trial plots until the spring trials end.

### fallout_nzl.event_log.choice.open

Source line: 313.
Before: Open Ledger

After: Open Government

### fallout_nzl_relief_speaker_trait

Source line: 416.
Before: Keeper of the Open Ledger

After: Harbour Relief Speaker

### fallout_nzl_berth_riots_desc

Source line: 441.
Before: Families have learned that harbour lists can decide who eats and who remains offshore. Crowds now gather wherever a ledger is opened.

After: Families have learned that harbour lists can decide who eats and who remains offshore. Crowds now gather wherever harbour lists are posted.

### fallout_nzl_lifeboat_category

Source line: 458.
Before: The Lifeboat Ledger

After: The Lifeboat Council

### fallout_nzl_dispatch_dairy_relief_convoy_desc

Source line: 487.
Before: Assign convoy hulls and trucks to one sealed dairy sailing between the stores and the ports. The emergency cargo can stabilize the ration ledgers, but the transport does not return to the pool.

After: Assign convoy hulls and trucks to one sealed dairy sailing between the stores and the ports. The cargo can stabilize food rations, but the transport does not return to the pool.

### fallout_nzl_publish_the_berth_ledger

Source line: 578.
Before: Publish the Berth Ledger

After: Publish the Berth Lists

### fallout_nzl_year_ten_order_desc

Source line: 647.
Before: A decade of ledgers, storms, rations, and patrols has created institutions that must outlive their emergency founders.

After: A decade of storms, rationing, and patrols has created institutions that must outlive their emergency founders.

### chaosx.fallout.135.a

Source line: 672.
Before: Enter the outcome in the dairy ledger

After: The dairy shipment has been judged.

### chaosx.fallout.141.c

Source line: 692.
Before: Keep our vessels outside their ledger

After: Our vessels will keep their independence.

### chaosx.fallout.145.a

Source line: 700.
Before: Close the first contact ledger

After: We have heard their answer.

### chaosx.fallout.147.a

Source line: 707.
Before: Make the open ledger a permanent constitution

After: Make harbour oversight part of the constitution.

### fallout_usa_federal_continuity_ledger

Source line: 758.
Before: Reconcile the Federal Ledger

After: Reconcile the Federal Shelter Rolls

### fallout_usa_federal_reconstruction_desc

Source line: 771.
Before: The federal ledger, repaired corridors, guard compacts, and regional charters now describe one government with several working hands. Reconstruction can proceed without pretending that the old map survived intact.

After: The federal shelter rolls, repaired corridors, guard compacts, and regional charters now describe one government with several working hands. Reconstruction can proceed without pretending that the old map survived intact.

### fallout_usa_federal_continuity_ledger_idea

Source line: 772.
Before: Federal Continuity Ledger

After: Federal Shelter Rolls

### chaosx.fallout.536.a

Source line: 905.
Before: Record the winter ledger

After: We know how much ammunition remains.

### chaosx.fallout.538.partial.d

Source line: 909.
Before: Snowmelt reveals missing boxes and a second ledger. The armoury can account for most of the stock, though the local watch will keep its own count from now on.

After: Snowmelt reveals missing boxes and a separate account. The armoury can account for most of the stock, though the local watch will keep its own count from now on.

### fallout.event_log.ammunition_winter.callback_partial

Source line: 928.
Before: The thaw inventory left a second ledger in local hands.

After: The thaw inventory left a separate account in local hands.

### chaosx.fallout.164.a.tt

Source line: 937.
Before: Spend §Y[?constant:fallout_event_164_cost.feed_people|0]§! Food Security and review the kitchen issue after §Y[?constant:fallout_event_164_timing.result_delay_days|0] days§!. A strong result improves the food ledger and records a conversion memory in [?fallout_event_164_feed_state_id.GetName].

After: Spend §Y[?constant:fallout_event_164_cost.feed_people|0]§! Food Security and review the kitchen issue after §Y[?constant:fallout_event_164_timing.result_delay_days|0] days§!. A strong result improves food supplies in [?fallout_event_164_feed_state_id.GetName].

### chaosx.fallout.166.partial.d

Source line: 945.
Before: The kitchen issue in [?fallout_event_164_feed_state_id.GetName] reached the central wards, but the outer shelters received thinner bowls. The conversion ledger is real, although district clerks disagree about who was counted first.

After: The kitchen issue in [?fallout_event_164_feed_state_id.GetName] reached the central wards, but the outer shelters received thinner bowls. District clerks still dispute which households should have been fed first.

### chaosx.fallout.168.failure.d

Source line: 960.
Before: The divided reserve in [?fallout_event_164_feed_state_id.GetName] became three short ledgers before the convoy could return. The outer depot lost people to the shortage, while [ROOT.GetAirWinterGovernmentOfficial] marked the route as a failed reclamation claim.

After: The divided reserve in [?fallout_event_164_feed_state_id.GetName] became three depleted stores before the convoy could return. The outer depot lost people to the shortage, while [ROOT.GetAirWinterGovernmentOfficial] marked the route as a failed reclamation claim.

### chaosx.fallout.172.failure.d

Source line: 967.
Before: The first harvest in [?fallout_event_164_feed_state_id.GetName] failed under frost, ash, or an empty breeding line. The last feed ledger is closed with another food loss, and [ROOT.GetAirWinterGovernmentAuthority] must carry that memory into the next ration choice.

After: The first harvest in [?fallout_event_164_feed_state_id.GetName] failed under frost, ash, or an empty breeding line. Food stocks have fallen again. [ROOT.GetAirWinterGovernmentAuthority] must feed the shelters with what remains.

### fallout.event_log.animal_feed.detail.people_failure

Source line: 975.
Before: The kitchen issue failed before the reserve could be measured, and deaths entered the feed ledger.

After: The kitchen issue failed before the reserve could be measured, and the shortage killed people.

### fallout.event_log.animal_feed.detail.division_failure

Source line: 981.
Before: The divided reserve became three short ledgers, and the outer depot recorded deaths before the convoy returned.

After: The divided reserve became three depleted stores, and the outer depot recorded deaths before the convoy returned.

### chaosx.fallout.454.a

Source line: 1018.
Before: Close the field ledger

After: The field review is finished.

### chaosx.fallout.557.a

Source line: 1060.
Before: Open the roof ledger

After: We know which roofs can be cleared.

### chaosx.fallout.204.d

Source line: 1096.
Before: The old greenhouse district kept three sealed crates through the Air Winter. The first leaves are alive, but their veins are mottled and the planting ledger names no safe answer. The food council must decide whether to destroy the batch, risk a full planting, keep it behind filters, or send samples to growers who can judge it beyond this state.

After: The old greenhouse district kept three sealed crates through the Air Winter. The first leaves are alive, but their veins are mottled and the growers cannot tell whether they are safe. The food council must decide whether to destroy the batch, risk a full planting, keep it behind filters, or send samples to growers beyond this state.

### chaosx.fallout.207.success.d

Source line: 1112.
Before: The food compact planted every sheltered furrow before the thaw line broke. The leaves held their color, and the district ledger now names a cultivar that can feed the next ration cycle.

After: The food compact planted every sheltered furrow before the thaw line broke. The leaves held their color, and the growers have a cultivar that can feed the next ration cycle.

### chaosx.fallout.208.a

Source line: 1121.
Before: Keep the quarantine ledger open until thaw

After: Watch the quarantined crop until thaw.

### chaosx.fallout.214.a

Source line: 1133.
Before: Record the verdict beside the food ledger

After: We know what can be planted.

### chaosx.fallout.310.b.tt

Source line: 1166.
Before: Give neighborhood crews their own switching authority and a common repair ledger. Costs Power, Scrap, and Food. A stable result favors resilience and trust.

After: Give neighborhood crews their own switching authority and a shared repair schedule. Costs Power, Scrap, and Food. A stable result favors resilience and trust.

### chaosx.fallout.312.cooperative.success.d

Source line: 1175.
Before: Local crews bring their circuits online one street at a time. The repair ledger travels with the food carts, and a broken transformer becomes a public problem before it becomes a private feud. The settlement has less reach but more hands inside the work.

After: Local crews bring their circuits online one street at a time. The repair schedule travels with the food carts, and a broken transformer becomes a public problem before it becomes a private feud. The settlement has less reach but more hands inside the work.

### chaosx.fallout.314.a

Source line: 1190.
Before: Close the Black Start ledger

After: The grid has faced its first winter.

### fallout.event_log.black_start.cooperative_success

Source line: 1197.
Before: Local cooperatives restored circuits with a shared repair ledger.

After: Local cooperatives restored circuits with a shared repair schedule.

### fallout_black_start_cooperative

Source line: 1211.
Before: Cooperative Switching Ledger

After: Cooperative Switching

### fallout_black_start_cooperative_desc

Source line: 1212.
Before: Local crews share repairs through a public ledger and neighborhood authority.

After: Local crews share repair schedules under neighborhood authority.

### chaosx.fallout.726.d

Source line: 1226.
Before: The East Gate ledger records a new inspection demand from the government across the winter road. Its officers will not accept our Clean Certificate without a shared procedure, while our own clinic cannot absorb another uncontrolled queue. The Quarantine council must decide whether to seal the crossing, invite a joint team, protect named relief caravans, or put soldiers on the gate.

After: The government across the winter road demands new inspections at East Gate. Its officers will not accept our Clean Certificate without a shared procedure. Our clinic cannot absorb another uncontrolled queue. The Quarantine council must decide whether to seal the crossing, invite a joint team, protect named relief caravans, or put soldiers on the gate.

### chaosx.fallout.726.b.tt

Source line: 1230.
Before: Spend Scrap, Power, and Recognition to admit foreign inspectors beside our clinic staff. The measure can create a bilateral health compact, but it exposes our ledgers to a difficult review. A result arrives after thirty days.

After: Spend Scrap, Power, and Recognition to admit foreign inspectors beside our clinic staff. The measure can create a bilateral health compact, but it exposes our inspection practices to foreign scrutiny. A result arrives after thirty days.

### chaosx.fallout.728.close_border.partial.d

Source line: 1238.
Before: The gate closes, but the night watch cannot keep every footpath sealed. The Rime Ward clinic gains time while the crossing backlog grows beyond the ledger's first estimate. The neighboring government accepts the notice without calling it a treaty.

After: The gate closes, but the night watch cannot keep every footpath sealed. The Rime Ward clinic gains time while the crossing backlog grows beyond the officers' first estimate. The neighboring government accepts the notice without calling it a treaty.

### chaosx.fallout.728.joint_team.success.d

Source line: 1240.
Before: Foreign inspectors enter the Rime Ward office beside our nurses. They compare the Clean Certificate with the East Gate ledger, accept the same exposure limits, and sign a narrow health compact that leaves ordinary trade open under recorded checks.

After: Foreign inspectors enter the Rime Ward office beside our nurses. They compare the Clean Certificate with the East Gate inspection list, accept the same exposure limits, and sign a narrow health compact that leaves ordinary trade open under recorded checks.

### chaosx.fallout.728.joint_team.partial.d

Source line: 1241.
Before: The joint team agrees on a clinic form, but the East Gate keeps a second ledger for freight. Patients move through the crossing with fewer arguments while cargo remains subject to a dispute neither government will yet call a treaty.

After: The joint team agrees on a clinic form, but the East Gate keeps a separate account for freight. Patients move through the crossing with fewer arguments while cargo remains subject to a dispute neither government will yet call a treaty.

### chaosx.fallout.728.joint_team.failure.d

Source line: 1242.
Before: The joint team finds that the two ledgers describe different roads. Inspectors leave with no signature, the Rime Ward clinic loses its reserved power, and the neighboring government announces that our certificate cannot be trusted.

After: The joint team finds that the two offices use conflicting inspection rules. Inspectors leave with no signature, the Rime Ward clinic loses its reserved power, and the neighboring government announces that our certificate cannot be trusted.

### chaosx.fallout.730.success.d

Source line: 1253.
Before: A season later, the East Gate ledger and the Rime Ward clinic record the same names. The neighboring government honors the inspection lane, and the Quarantine council can describe the compact without pretending that the frontier is safe.

After: A season later, the East Gate inspection list and the Rime Ward clinic record the same names. The neighboring government honors the inspection lane, and the Quarantine council can describe the compact without pretending that the frontier is safe.

### fallout.event_log.border_inspection_crisis.detail.joint_team_partial

Source line: 1267.
Before: A joint team aligned clinic forms while freight remained under a separate ledger.

After: A joint team aligned clinic forms while freight remained under separate rules.

### fallout.event_log.border_inspection_crisis.detail.joint_team_failure

Source line: 1268.
Before: A joint team found incompatible ledgers and left without a trusted signature.

After: A joint team found conflicting instructions and left without a trusted signature.

### fallout.event_log.border_inspection_crisis.detail.callback_success

Source line: 1275.
Before: A season later, both ledgers still described the same inspection lane.

After: A season later, both offices still followed the same inspection rules.

### chaosx.fallout.466.t

Source line: 1294.
Before: The Crossing Ledger

After: The Crossing Rules

### chaosx.fallout.630.guard.success.d

Source line: 1353.
Before: The gate guards held the release point without closing the village ledgers. Escorts kept the pumps and stores intact, and the water moved under inspection while the embankment remained a military position with a civilian schedule.

After: The gate guards held the release point without closing the village water schedules. Escorts kept the pumps and stores intact, and the water moved under inspection while the embankment remained a military position with a civilian schedule.

### fallout.event_log.canal_schedule.guard_success

Source line: 1388.
Before: The gate guards protected the release point without replacing the village ledgers.

After: The gate guards protected the release point without replacing the village water schedules.

### chaosx.fallout.524.success.d

Source line: 1428.
Before: The review board finds the route book, casualty rule, and fuel ledger in agreement. Captain Varga's refusal is no longer an open order, and the field command can close its first winter review with a usable chain of responsibility.

After: The review board finds the route book, casualty rule, and fuel tally in agreement. Captain Varga's refusal is no longer an open order, and the field command can close its first winter review with a usable chain of responsibility.

### chaosx.fallout.524.failure.d

Source line: 1430.
Before: The review board finds that the order, the route book, and the casualty ledger describe three different marches. The field depot is damaged again, the remaining platoon loses people in the confusion, and the command memory closes as a warning against another unrecorded order.

After: The review board finds that the order, the route book, and the casualty list describe three different marches. The field depot is damaged again, the remaining platoon loses people in the confusion, and the command memory closes as a warning against another unrecorded order.

### fallout.event_log.captain_refuses.grant_field_autonomy_partial

Source line: 1445.
Before: Field autonomy saved the column while the reserve ledger failed.

After: Field autonomy saved the column while the reserve plan failed.

### fallout.event_log.captain_refuses.callback_partial

Source line: 1448.
Before: The command review left one route ledger disputed.

After: The command review left one route book disputed.

### chaosx.fallout.768.opening.d

Source line: 1455.
Before: At a repaired dock in the West African Port Confederacies, rescue captains, fishers, merchants, and families crowd around a salt-stained ledger. Boats are arriving from burned river mouths with no shared rule for rescue duty, salvaged cargo, or berths. The port council must decide what the fleet owes the living.

After: At a repaired dock in the West African Port Confederacies, rescue captains, fishers, merchants, and families crowd around a salt-stained harbour roll. Boats are arriving from burned river mouths with no shared rule for rescue duty, salvaged cargo, or berths. The port council must decide what the fleet owes the living.

### chaosx.fallout.770.fleet_split.success.d

Source line: 1475.
Before: The crews voted to form a separate rescue flotilla and left the port with a shared ration ledger. The split costs command unity, yet families know which boats will answer an emergency call.

After: The crews voted to form a separate rescue flotilla and left the port under shared ration rules. The split costs command unity, yet families know which boats will answer an emergency call.

### fallout.event_log.captains_articles.detail.choice_fleet_split

Source line: 1491.
Before: The crews voted to form a separate rescue flotilla and divided the fleet ledger.

After: The crews voted to form a separate rescue flotilla and divided the fleet duties.

### fallout.event_log.captains_articles.detail.fleet_split_success

Source line: 1501.
Before: The crews formed a rescue flotilla with a shared ration ledger and a named emergency duty.

After: The crews formed a rescue flotilla with shared ration rules and a named emergency duty.

### fallout.event_log.captains_articles.detail.callback_success

Source line: 1504.
Before: The delayed review kept names, fuel, and rescue duty in one harbor ledger.

After: The delayed review kept names, fuel, and rescue duty in one harbour plan.

### chaosx.fallout.436.a.tt

Source line: 1530.
Before: Spend food, medicine, recognition, and cohesion to put the children in the country's public ledger.

After: Spend food, medicine, recognition, and cohesion to put the children in the country's citizen roll.

### chaosx.fallout.438.grant_citizenship.failure.d

Source line: 1537.
Before: The citizenship ledger becomes a quarrel over which old country owns the children. The clerk closes the book, households stop sharing names, and the schoolroom learns that a legal promise can make a child more visible and less safe.

After: The citizenship process becomes a quarrel over which old country owns the children. The clerk closes the book, households stop sharing names, and the schoolroom learns that a legal promise can make a child more visible and less safe.

### chaosx.fallout.438.foster_communities.partial.d

Source line: 1539.
Before: Most children find a household, but the smallest settlements cannot keep the siblings together. The foster ledger protects names and letters, while daily life teaches the cohort different loyalties.

After: Most children find a household, but the smallest settlements cannot keep the siblings together. The foster roll protects names and letters, while daily life teaches the cohort different loyalties.

### fallout.event_log.children_from_elsewhere.grant_citizenship_success

Source line: 1557.
Before: The children entered the public ledger and received a durable place in the new country.

After: The children entered the citizen roll and received a durable place in the new country.

### chaosx.fallout.735.reform.failure.d

Source line: 1590.
Before: The reform meeting ended with the gates closed and the youth ledger marked as a warning. The next cohort now knows that an appeal can become another checkpoint when Food and trust run short.

After: The reform meeting ended with the gates closed and the youth petition marked as a warning. The next cohort now knows that an appeal can become another checkpoint when Food and trust run short.

### chaosx.fallout.735.service_travel.partial.d

Source line: 1592.
Before: The service route reached the central shelters and one damaged outpost. The first permits work, but a missing fuel ledger leaves the outer wards unsure whether travel belongs to everyone or only to the most useful crew.

After: The service route reached the central shelters and one damaged outpost. The first permits work, but a missing fuel tally leaves the outer wards unsure whether travel belongs to everyone or only to the most useful crew.

### chaosx.fallout.735.strict_continuation.partial.d

Source line: 1595.
Before: The strict route held the checkpoints together while the youth delegates received a place behind the ledger desk. They can report abuse, but the movement law still treats an unsponsored journey as a threat.

After: The strict route held the checkpoints together while the youth delegates received a place behind the permit desk. They can report abuse, but the movement law still treats an unsponsored journey as a threat.

### chaosx.fallout.737.failure.d

Source line: 1606.
Before: The return visit found the cohort split between a locked registry and an empty service ledger. The route survives as a memory of promises that the cordon could not keep.

After: The return visit found the cohort split between a locked registry and an unfilled service roster. The route survives as a memory of promises that the cordon could not keep.

### fallout.event_log.children_of_cordon.detail.reform_success

Source line: 1612.
Before: The second generation rewrote the movement law and turned its appeal ledger into civic apprenticeship.

After: The second generation rewrote the movement law and turned its appeal process into civic apprenticeship.

### fallout.event_log.children_of_cordon.detail.reform_failure

Source line: 1614.
Before: The reform meeting closed the gate and left the youth ledger as a warning.

After: The reform meeting closed the gate and left the youth petition as a warning.

### fallout.event_log.children_of_cordon.detail.callback_failure

Source line: 1626.
Before: The return visit to the cohort found a locked registry and an empty service ledger.

After: The return visit to the cohort found a locked registry and an unfilled service roster.

### chaosx.fallout.1039.equal_public_school.success.d

Source line: 1655.
Before: The river and hill wards open one public school beside the ferry. The same lesson boards, food ledger, and medicine register travel up the road, and the first class elects two pupil stewards who can question either storekeeper.

After: The river and hill wards open one public school beside the ferry. The same lesson boards, food supply, and medicine register travel up the road, and the first class elects two pupil stewards who can question either storekeeper.

### chaosx.fallout.1039.equal_public_school.failure.d

Source line: 1657.
Before: The public school loses its food ledger when the ferry shelter floods. A hill guard takes the medicine register uphill, the teacher leaves, and the two wards accuse each other of keeping the children for future labor.

After: The public school loses its food supply when the ferry shelter floods. A hill guard takes the medicine register uphill, the teacher leaves, and the two wards accuse each other of keeping the children for future labor.

### chaosx.fallout.1041.failure.d

Source line: 1672.
Before: The delayed review finds a missing guardian, a broken storehouse key, and two records for the same class. The wards stop the exchange, the foreign witness withdraws recognition, and the next children inherit a border made from school ledgers.

After: The delayed review finds a missing guardian, a broken storehouse key, and two records for the same class. The wards stop the exchange, the foreign witness withdraws recognition, and the next children inherit a border made from school enrolment rules.

### fallout.event_log.children_of_two_settlements.detail.equal_public_school_failure

Source line: 1683.
Before: A flooded ferry shelter lost the school ledger and turned the two wards against one another.

After: A flooded ferry shelter lost the school ration book and turned the two wards against one another.

### chaosx.fallout.721.public.success.d

Source line: 1724.
Before: The public desk at North Gate opens before dawn. Ash Ward nurses compare names with the clinic ledger, and no traveler is asked to barter for a seal. The certificate has become a visible promise from the Quarantine State.

After: The public desk at North Gate opens before dawn. Ash Ward nurses compare names with the patient list, and no traveler is asked to barter for a seal. The certificate has become a visible promise from the Quarantine State.

### chaosx.fallout.723.success.d

Source line: 1739.
Before: One season later, the North Gate register still matches the Ash Ward ledger. The certificate has acquired a place in school satchels, freight manifests, and the eastern checkpoint book. The office can remain open without pretending that every road is safe.

After: One season later, the North Gate register still matches the Ash Ward patient list. The certificate has acquired a place in school satchels, freight manifests, and the eastern checkpoint book. The office can remain open without pretending that every road is safe.

### fallout.event_log.clean_certificate.detail.callback_success

Source line: 1762.
Before: A season later, the certificate matched the clinic ledger and remained in use.

After: A season later, the certificate matched the patient list and remained in use.

### chaosx.fallout.882.medical_oversight.partial.d

Source line: 1789.
Before: The clinic board keeps the medicine ledger coherent in the central ward, while two outlying pumps continue to use older forms. The Basin has an accountable care office, though its authority still ends at the next flooded road.

After: The clinic board keeps the medicine tally coherent in the central ward, while two outlying pumps continue to use older forms. The Basin has an accountable care office, though its authority still ends at the next flooded road.

### chaosx.fallout.882.elected_council.success.d

Source line: 1791.
Before: Ward delegates open the medicine ledger at the council table and tie every request to a named district. The clinic board keeps its skill, yet no outside office can claim that care belongs to one closed profession.

After: Ward delegates open the medicine tally at the council table and tie every request to a named district. The clinic board keeps its skill, yet no outside office can claim that care belongs to one closed profession.

### chaosx.fallout.884.failure.d

Source line: 1805.
Before: The delayed review finds the care rule split between board seals and council ledgers. The Basin remembers choosing its authority, but families now carry duplicate forms because no office trusts the other to close a case.

After: The delayed review finds the care rule split between board seals and council tallies. The Basin remembers choosing its authority, but families now carry duplicate forms because no office trusts the other to close a case.

### fallout.event_log.clinic_or_council.detail.choice_elected_council

Source line: 1811.
Before: Ward delegates took care budgets into a public council ledger.

After: Ward delegates took care budgets into a public council tally.

### fallout.event_log.clinic_or_council.detail.elected_council_success

Source line: 1817.
Before: Ward delegates opened the medicine ledger and kept the board's skill.

After: Ward delegates opened the medicine tally and kept the board's skill.

### fallout.event_log.clinic_or_council.detail.callback_failure

Source line: 1828.
Before: Duplicate forms returned because board seals and council ledgers no longer matched.

After: Duplicate forms returned because board seals and council tallies no longer matched.

### fallout_clinic_or_council_elected_council

Source line: 1836.
Before: Ward Care Ledger

After: Ward Care Council

### chaosx.fallout.1044.a.tt

Source line: 1849.
Before: Spend Food 2, Medicine 2, and Recognition 2 to give the first cohort a witnessed council with its own attendance and shelter ledger. A ballot held under the ferry canopy can make civic confidence visible, but it gives an inexperienced council authority during cold rain.

After: Spend Food 2, Medicine 2, and Recognition 2 to give the first cohort a witnessed council with its own attendance roll and shelter list. A ballot held under the ferry canopy can make civic confidence visible, but it gives an inexperienced council authority during cold rain.

### chaosx.fallout.1048.partial.d

Source line: 1873.
Before: The review finds a working mandate but two copies of the service and shelter ledger. The cohort can still meet beneath the ferry canopy, yet the wards postpone a final balance of guardian and delegate seats until the stores recover.

After: The review finds a working mandate but two copies of the service roster and shelter list. The cohort can still meet beneath the ferry canopy, yet the wards postpone a final balance of guardian and delegate seats until the stores recover.

### fallout.event_log.cohorts_first_ballot.detail.callback_partial

Source line: 1896.
Before: The mandate held while the wards kept separate service and shelter ledger copies.

After: The mandate held while the wards kept separate service rosters and shelter lists.

### chaosx.fallout.389.t

Source line: 1924.
Before: The Clinic Ledger Opens

After: The Clinic Reopens

### chaosx.fallout.391.a

Source line: 1943.
Before: Close the ledger and keep the ward open

After: Keep the clinic open.

### fallout.event_log.counterfeit_antibiotics.callback_success

Source line: 1959.
Before: The later supplier review left a named source and a travelling clinic ledger.

After: The supplier review identified a medicine source and sent delivery notes with every convoy.

### chaosx.fallout.574.civic.partial.d

Source line: 1978.
Before: The civic exhibition opened, but the repair ledger and the family roll did not agree. The host district kept a smaller gathering and a list of grievances that the next season must answer.

After: The civic exhibition opened, but the repair schedule and the family roll did not agree. The host district kept a smaller gathering and a list of grievances that the next season must answer.

### chaosx.fallout.574.exchange.partial.d

Source line: 1981.
Before: The exchange moved enough food to matter, but fuel and route marks failed at the outer stalls. The host district kept a modest trade custom and a debt ledger for the next gathering.

After: The exchange moved enough food to matter, but fuel and route marks failed at the outer stalls. The host district kept a modest trade custom and unpaid debts for the next gathering.

### chaosx.fallout.576.partial.d

Source line: 1993.
Before: A year later, the fair returns in a smaller form. The stalls and remembrance ground survived, but the host district still carries a grievance ledger and cannot promise the same reach next season.

After: A year later, the fair returns in a smaller form. The stalls and remembrance ground survived, but unresolved grievances keep the host district from promising the same reach next season.

### fallout.event_log.county_fair_returns.detail.civic_partial

Source line: 2004.
Before: The civic exhibition held in smaller form and left a grievance ledger.

After: The civic exhibition held in smaller form and left unresolved grievances.

### chaosx.fallout.342.failure.d

Source line: 2051.
Before: The permit review failed when the city watch lost its filters and the inventory ledger vanished. A new plume rises over the road, and the selected state must carry the cost of having opened a door it could not keep guarded.

After: The permit review failed when the city watch lost its filters and the inventory vanished. A new plume rises over the road, and the selected state must carry the cost of having opened a door it could not keep guarded.

### chaosx.fallout.487.reserve_clinic_power.success.d

Source line: 2092.
Before: The clinic lamps stayed on while the plant filled a measured set of tanks. Nurses, mechanics, and port wardens now share one night roster and one water ledger.

After: The clinic lamps stayed on while the plant filled a measured set of tanks. Nurses, mechanics, and port wardens now share one night roster and one water schedule.

### chaosx.fallout.487.lock_and_ration.partial.d

Source line: 2096.
Before: The ration line held near the intake and failed at the outer road. The plant survives, but the first water ledger now names the districts that were left waiting.

After: The ration line held near the intake and failed at the outer road. The plant survives, but the first water schedule now names the districts that were left waiting.

### chaosx.fallout.443.d

Source line: 2260.
Before: The village still has a public well, a field ledger, and roofs that can be made to hold. The last census names families who are gone, while the road brings people who need a room and a reason to stay. The registrar asks whether this place will become a home, a garrison, a shared council, or a line no one crosses.

After: The village still has a public well, a field plan, and roofs that can be made to hold. The last census names families who are gone, while the road brings people who need a room and a reason to stay. The registrar asks whether this place will become a home, a garrison, a shared council, or a line no one crosses.

### chaosx.fallout.445.resettle_refugee_families.success.d

Source line: 2270.
Before: The first families repair the rooms around the well and pin old names beside new addresses. A school bench arrives with the ration cart, and the field ledger gains owners who can argue in public without being treated as trespassers.

After: The first families repair the rooms around the well and pin old names beside new addresses. A school bench arrives with the ration cart, and the field plan gains owners who can argue in public without being treated as trespassers.

### chaosx.fallout.447.partial.d

Source line: 2286.
Before: The review finds a working road and a divided council. Some families call the village home, some call it a posting, and the land ledger still leaves one question open.

After: The review finds a working road and a divided council. Some families call the village home, some call it a posting, and the land allotment still leaves one question open.

### fallout.event_log.empty_village_offer.callback_failure

Source line: 2306.
Before: The village review left empty rooms and a warning in the country's border ledger.

After: The village review left empty rooms and a warning in the country's border register.

### chaosx.fallout.10.t

Source line: 2582.
Before: The Seed Ledger

After: The Seed Stores

### chaosx.fallout.10.d

Source line: 2583.
Before: Threshing returns from [air_winter_event_state.GetName] show grain with hollow kernels and roots killed close to the surface. Village councils have opened the seed ledgers and found enough stock for one careful spring, one winter of bread, or neither if the cold deepens. The decision over what the sealed bins will preserve belongs to [ROOT.GetAirWinterGovernmentAuthority].

After: Threshing returns from [air_winter_event_state.GetName] show grain with hollow kernels and roots killed close to the surface. Village councils have opened the seed inventories and found enough stock for one careful spring, one winter of bread, or neither if the cold deepens. The decision over what the sealed bins will preserve belongs to [ROOT.GetAirWinterGovernmentAuthority].

### chaosx.fallout.18.t

Source line: 2591.
Before: The Spring Ledger

After: The Spring Herds

### chaosx.fallout.18.breeding_failure.d

Source line: 2596.
Before: The protected herds in [air_winter_event_state.GetName] entered spring too thin to recover. Pneumonia moved through crowded sheds, feed stores emptied, and several village committees concealed their losses until inspectors opened the pens. Closing the breeding ledger and redirecting the remaining fodder falls to [ROOT.GetAirWinterGovernmentOfficial].

After: The protected herds in [air_winter_event_state.GetName] entered spring too thin to recover. Pneumonia moved through crowded sheds, feed stores emptied, and several village committees concealed their losses until inspectors opened the pens. Closing the breeding program and redirecting the remaining fodder falls to [ROOT.GetAirWinterGovernmentOfficial].

### chaosx.fallout.18.c

Source line: 2601.
Before: Close the slaughter ledger and ration the last meat.

After: Close the slaughter work and ration the last meat.

### chaosx.fallout.13.c.tt

Source line: 2634.
Before: National Stability falls by §R[?constant:air_winter_event_desert_city.municipal_stability_cost|%1]§!. In §Y[air_winter_event_state.GetName]§!, §YWater Security§! rises by §G[?constant:air_winter_event_ledger.water_major|0]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!. Local factory availability is reduced by §R[?constant:air_winter_event_desert_city.municipal_factory_penalty_magnitude|%0]§! for §Y[?constant:air_winter_event_desert_city.municipal_factory_days|0] days§!. The water ledger returns after §Y[?constant:air_winter_event_runtime.delayed_standard_days|0] days§!. Full success requires Water Security of at least §Y[?constant:air_winter_event_desert_city.success_water_minimum|0]§!, Adaptation of at least §Y[?constant:air_winter_event_desert_city.success_adaptation_minimum|0]§!, and Building Damage Pressure no higher than §Y[?constant:air_winter_event_desert_city.success_pressure_ceiling|0]§!.

After: National Stability falls by §R[?constant:air_winter_event_desert_city.municipal_stability_cost|%1]§!. In §Y[air_winter_event_state.GetName]§!, §YWater Security§! rises by §G[?constant:air_winter_event_ledger.water_major|0]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!. Local factory availability is reduced by §R[?constant:air_winter_event_desert_city.municipal_factory_penalty_magnitude|%0]§! for §Y[?constant:air_winter_event_desert_city.municipal_factory_days|0] days§!. The water schedule returns after §Y[?constant:air_winter_event_runtime.delayed_standard_days|0] days§!. Full success requires Water Security of at least §Y[?constant:air_winter_event_desert_city.success_water_minimum|0]§!, Adaptation of at least §Y[?constant:air_winter_event_desert_city.success_adaptation_minimum|0]§!, and Building Damage Pressure no higher than §Y[?constant:air_winter_event_desert_city.success_pressure_ceiling|0]§!.

### chaosx.fallout.23.a.tt

Source line: 2744.
Before: In §Y[air_winter_event_state.GetName]§!, §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_severe|0]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, and §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!, and the fuel ledger closes after §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!.

After: In §Y[air_winter_event_state.GetName]§!, §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_severe|0]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, and §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!, and the fuel tally closes after §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!.

### chaosx.fallout.23.b.tt

Source line: 2746.
Before: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_major|0]§! and §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!. National War Support rises by §G[?constant:air_winter_event_country.war_support_moderate|%1]§!, and the fuel ledger closes after §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!.

After: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_major|0]§! and §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!. National War Support rises by §G[?constant:air_winter_event_country.war_support_moderate|%1]§!, and the fuel tally closes after §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!.

### chaosx.fallout.23.c.tt

Source line: 2748.
Before: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_moderate|0]§! and §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_moderate|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!, and the fuel ledger closes after §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!.

After: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_moderate|0]§! and §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_moderate|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!, and the fuel tally closes after §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!.

### chaosx.fallout.24.t

Source line: 2750.
Before: The Coal Ledger Closes

After: Coal Runs Low

### chaosx.fallout.25.t

Source line: 2770.
Before: The Reservoir Ledger

After: The Reservoir Supply

### chaosx.fallout.37.t

Source line: 2907.
Before: The Works Inspector's Ledger

After: The Works Inspector's Findings

### chaosx.fallout.37.full_success.d

Source line: 2908.
Before: The exposed works of [air_winter_event_state.GetName] still answer the shift whistles after thirty days. At each site, crews cleared frozen screens and loading gear or thawed furnace lines and crane rails before the next shift entered. [ROOT.GetAirWinterGovernmentOfficial] has received an inspector's ledger that calls for binding winter shift rules across every operating works.

After: The exposed works of [air_winter_event_state.GetName] still answer the shift whistles after thirty days. At each site, crews cleared frozen screens and loading gear or thawed furnace lines and crane rails before the next shift entered. [ROOT.GetAirWinterGovernmentOfficial] has received an inspector's findings that call for binding winter shift rules across every operating works.

### chaosx.fallout.48.survey_disaster.d

Source line: 3009.
Before: A service roof beneath [air_winter_event_state.GetName] folded across the surveyed path while both lamp teams were below. Rescue crews reached the first brace line, then the street above began sinking into the conduit. The recovered bodies, lost tools, and damaged infrastructure have been entered in the district ledger.

After: A service roof beneath [air_winter_event_state.GetName] folded across the surveyed path while both lamp teams were below. Rescue crews reached the first brace line, then the street above began sinking into the conduit. The recovered bodies, lost tools, and damaged infrastructure have been entered in the district roll.

### chaosx.fallout.48.licensed_success.d

Source line: 3013.
Before: Licensed fire, rail, and utility crews in [air_winter_event_state.GetName] divided the service streets into marked districts and honored the boundary boards. They returned support kits, trucks, and repair trains through separate issue halls. The casualty ledger is short, and local foremen have supplied usable maps for the next reclamation survey.

After: Licensed fire, rail, and utility crews in [air_winter_event_state.GetName] divided the service streets into marked districts and honored the boundary boards. They returned support kits, trucks, and repair trains through separate issue halls. The casualty list is short, and local foremen have supplied usable maps for the next reclamation survey.

### chaosx.fallout.203.d

Source line: 3127.
Before: Winter conditions have overtaken the order. The named state may have changed hands, the source shore may no longer hold enough people for a safe transfer, or the crews and stores pledged to the measure may no longer be available. Nothing is moved, unused transports and stores remain with their current commands, and the invalid field order is struck from the winter ledger.

After: Winter conditions have overtaken the order. The named state may have changed hands, the source shore may no longer hold enough people for a safe transfer, or the crews and stores pledged to the measure may no longer be available. Nothing is moved, unused transports and stores remain with their current commands, and the invalid field order is struck from the winter plan.

### chaosx.fallout.831.opening.d

Source line: 3141.
Before: The Grid Vote left the Manchurian Reactor Keeps with a power charter, but the first cold-season model overstated how much current a damaged cooling district could carry. A hospital ward lost pressure, a relay room overheated, and the calculation ledger now has to decide whether the Technate will expose the error, bury it, punish one operator, or rebuild the model before the next shift.

After: The Grid Vote left the Manchurian Reactor Keeps with a power charter, but the first cold-season model overstated how much current a damaged cooling district could carry. A hospital ward lost pressure, a relay room overheated, and the engineers' council now has to decide whether the Technate will expose the error, bury it, punish one operator, or rebuild the model before the next shift.

### chaosx.fallout.831.a

Source line: 3142.
Before: Open the ledger to a public inquiry

After: Let the public examine the failed calculation.

### chaosx.fallout.833.public_inquiry.success.d

Source line: 3152.
Before: The inquiry opened the cooling ledger in the Manchurian Reactor Keeps and sent copies to the eastern repair councils. The hospital ward received a measured repair window, the relay crew kept its tools, and the Technate can now name which assumption failed without turning the whole district against its engineers.

After: The inquiry opened the cooling calculations in the Manchurian Reactor Keeps and sent copies to the eastern repair councils. The hospital ward received a measured repair window, the relay crew kept its tools, and the Technate can now name which assumption failed without turning the whole district against its engineers.

### fallout.event_log.failed_calculation.detail.choice_public_inquiry

Source line: 3177.
Before: The Technate opened the cooling ledger to public inquiry.

After: The Technate opened the cooling calculations to public inquiry.

### fallout_failed_calculation_result_partial

Source line: 3198.
Before: Contested Calculation Ledger

After: Disputed Calculations

### chaosx.fallout.693.tribunal.success.d

Source line: 3229.
Before: The ward tribunal read both registers in public and cleared the households by name. The clinic kept its mandate, the grievance ledger fell, and the Quarantine State gained a memory that can survive a change of officers.

After: The ward tribunal read both registers in public and cleared the households by name. The clinic kept its mandate, the unresolved grievances fell, and the Quarantine State gained a memory that can survive a change of officers.

### chaosx.fallout.695.failure.d

Source line: 3240.
Before: The appeal practice collapsed under fatigue and missing pages. The cleared households remain a warning in the ward ledger, and every officer who inherits the cordon must decide whether to reopen the case or hide it again.

After: The appeal practice collapsed under fatigue and missing pages. The cleared households remain a warning in the patient list, and every officer who inherits the cordon must decide whether to reopen the case or hide it again.

### chaosx.fallout.478.intro

Source line: 3276.
Before: The thaw reached the surviving fields before the seed ledgers were ready. Green shoots appeared under a clean sky, then a hard night froze the low ground and split the irrigation channels. The state can replant from what it saved, pay a neighboring country for seed, lock the reserve below the old rail tunnel, or accept a smaller harvest while the people ration through the late frost.

After: The thaw reached the surviving fields before the seed inventories were ready. Green shoots appeared under a clean sky, then a hard night froze the low ground and split the irrigation channels. The state can replant from what it saved, pay a neighboring country for seed, lock the reserve below the old rail tunnel, or accept a smaller harvest while the people ration through the late frost.

### chaosx.fallout.480.t

Source line: 3285.
Before: The Frost Ledger

After: Frost Losses

### chaosx.fallout.480.import_seed.partial.d

Source line: 3290.
Before: Only half the convoy crossed the ash road. Imported seed fills the protected beds, while the lost crates become a diplomatic grievance and another entry in the famine ledger.

After: Only half the convoy crossed the ash road. Imported seed fills the protected beds, but the lost crates deepen the food shortage and leave both governments disputing the shipment.

### chaosx.fallout.482.success.d

Source line: 3301.
Before: The next sowing opens on ground that once looked lost. The seed ledger, the convoy debt, and the state granary share one date, while the thaw route remains open for the next region that needs it.

After: The next sowing opens on ground that once looked lost. The seed inventory, the convoy debt, and the state granary share one date, while the thaw route remains open for the next region that needs it.

### chaosx.fallout.970.opening.d

Source line: 3328.
Before: After the Congo Green Basin records a common settlement road, household stewards ask what kind of future the surviving districts can support. Proposals include voluntary aid, a public cohort program, adoption houses, and strict limits on family ledgers. The Basin must decide how to help without turning family life into a state quota.

After: After the Congo Green Basin records a common settlement road, household stewards ask what kind of future the surviving districts can support. Proposals include voluntary aid, a public cohort program, adoption houses, and strict limits on family support. The Basin must decide how to help without turning family life into a state quota.

### chaosx.fallout.974.failure.d

Source line: 3356.
Before: The review finds duplicate household ledgers, missing guardians, and a storehouse that answers to no trusted steward. The Basin remembers choosing a future, but families now avoid every office that claims to speak for it.

After: The review finds duplicate household rolls, missing guardians, and a storehouse that answers to no trusted steward. The Basin remembers choosing a future, but families now avoid every office that claims to speak for it.

### fallout.event_log.fertility_question.detail.state_program_failure

Source line: 3370.
Before: A service program became a compliance ledger that families feared.

After: Families feared the service program when it forced them to comply.

### fallout.event_log.fertility_question.detail.adoption_network_failure

Source line: 3373.
Before: A missing seal left a child between two household ledgers.

After: A missing seal left two adoption houses disputing who should care for a child.

### chaosx.fallout.259.failure.d

Source line: 3415.
Before: The bunks in [?fallout_event_256_state_id.GetName] were dispersed without enough food or warm rooms. Fever followed the corridor lights, the shelter ledger lost its order, and people moved into cold spaces without attendants died.

After: The bunks in [?fallout_event_256_state_id.GetName] were dispersed without enough food or warm rooms. Fever followed the corridor lights, the shelter roll lost its order, and people moved into cold spaces without attendants died.

### chaosx.fallout.266.partial.d

Source line: 3432.
Before: The follow-up in [?fallout_event_256_state_id.GetName] found a shelter that survived by exception. The ward can still treat a small wave, but the food and medicine ledgers remain tight and the people who were moved remember which door closed first.

After: The follow-up in [?fallout_event_256_state_id.GetName] found a shelter that survived by exception. The ward can still treat a small wave, but the food and medicine tallies remain tight and the people who were moved remember which door closed first.

### chaosx.fallout.217.d

Source line: 3459.
Before: The lower shelter at [?fallout_event_217_filters_state_id.GetName] still has a working airlock, but the filter ledger has fallen below the safe band. [ROOT.GetAirWinterGovernmentAuthority] must choose how [ROOT.GetAirWinterGovernmentOfficial] will keep the clinic, food rooms, and night crews breathing through the next fortnight.

After: The lower shelter at [?fallout_event_217_filters_state_id.GetName] still has a working airlock, but the filter supply has fallen below the safe band. [ROOT.GetAirWinterGovernmentAuthority] must choose how [ROOT.GetAirWinterGovernmentOfficial] will keep the clinic, food rooms, and night crews breathing through the next fortnight.

### chaosx.fallout.217.e.tt

Source line: 3467.
Before: Spend §Y[?constant:fallout_event_217_cost.household_filters|0]§! Filters and §Y[?constant:fallout_event_217_cost.household_recognition|0]§! Recognition. The household ledger will be reviewed after §Y[?constant:fallout_event_217_timing.result_delay_days|0] days§!.

After: Spend §Y[?constant:fallout_event_217_cost.household_filters|0]§! Filters and §Y[?constant:fallout_event_217_cost.household_recognition|0]§! Recognition. The household roll will be reviewed after §Y[?constant:fallout_event_217_timing.result_delay_days|0] days§!.

### chaosx.fallout.219.a

Source line: 3473.
Before: Send the seal ledger to the clinic

After: Send the filter inspection to the clinic.

### chaosx.fallout.220.partial.d

Source line: 3478.
Before: The rotation at [?fallout_event_217_filters_state_id.GetName] saved the strongest crews, but the food ledger could not cover every handover. The night route remains open with slower work and a memory of who was left outside the warm room.

After: The rotation at [?fallout_event_217_filters_state_id.GetName] saved the strongest crews, but the food supply could not cover every handover. The night route remains open with slower work and a memory of who was left outside the warm room.

### chaosx.fallout.222.t

Source line: 3490.
Before: The Household Ledger Report

After: The Household Filter Supply

### chaosx.fallout.222.success.d

Source line: 3491.
Before: The household ledger at [?fallout_event_217_filters_state_id.GetName] assigned filters by room, age, and night duty. Recognition rose because the counts were read aloud, and [ROOT.GetAirWinterGovernmentAuthority] can defend the ration rule before every shelter district.

After: The household roll at [?fallout_event_217_filters_state_id.GetName] assigned filters by room, age, and night duty. Recognition rose because the counts were read aloud, and [ROOT.GetAirWinterGovernmentAuthority] can defend the ration rule before every shelter district.

### chaosx.fallout.222.partial.d

Source line: 3492.
Before: The household ledger at [?fallout_event_217_filters_state_id.GetName] covered the clinic and the first family rooms, but the outer bunks received thinner filters. The rule remains legible, although the shelter has marked the families who paid the largest share.

After: The household roll at [?fallout_event_217_filters_state_id.GetName] covered the clinic and the first family rooms, but the outer bunks received thinner filters. The rule remains legible, although the shelter has marked the families who paid the largest share.

### fallout.event_log.filters_fail.detail.household_success

Source line: 3515.
Before: The household ledger made filter rations legible across the shelter districts.

After: The household roll made filter rations legible across the shelter districts.

### fallout.event_log.filters_fail.detail.household_partial

Source line: 3516.
Before: The household ledger covered the inner rooms while outer bunks received less cover.

After: The household roll covered the inner rooms while outer bunks received less cover.

### fallout_filters_fail_household_ledger

Source line: 3524.
Before: Household filter ledger

After: Household filter supply

### chaosx.fallout.686.strict.success.d

Source line: 3541.
Before: The cordon officers kept the ash road closed without abandoning the clinic. Fever reports fell, the quarantine ledger gained credibility, and the settlement's supply trucks reached the inner wards.

After: The cordon officers kept the ash road closed without abandoning the clinic. Fever reports fell, the quarantine rules gained credibility, and the settlement's supply trucks reached the inner wards.

### chaosx.fallout.852.opening.d

Source line: 3594.
Before: The Manchurian Reactor Keeps can keep its clinics and workshops alive only when every gauge agrees. The machine district has copied one voltage table, one axle measure, one parts ledger, and one radio interval from the records that survived the Fallout winter. Neighboring settlements will follow the table only if the Technate decides who may read it, change it, and profit from it.

After: The Manchurian Reactor Keeps can keep its clinics and workshops alive only when every gauge agrees. The machine district has copied one voltage table, one axle measure, one parts catalogue, and one radio interval from the records that survived the Fallout winter. Neighboring settlements will follow the table only if the Technate decides who may read it, change it, and profit from it.

### chaosx.fallout.284.elders.success.d

Source line: 3686.
Before: The elders named the child beside the old water ledger. Their rite gave the shelter a patient calendar, a shared witness list, and a reason to carry the next winter's work beyond a single household.

After: The elders named the child beside the old water schedule. Their rite gave the shelter a patient calendar, a shared witness list, and a reason to carry the next winter's work beyond a single household.

### fallout_first_safe_birth_elders_desc

Source line: 3724.
Before: An elders' naming rite keeps a witness list and a shared calendar beside the winter water ledger.

After: An elders' naming rite keeps a witness list and a shared calendar beside the winter water schedule.

### fallout_first_safe_birth_maintained

Source line: 3725.
Before: Maintained Birth Ledger

After: Maintained Birth Care

### fallout_first_safe_birth_maintained_desc

Source line: 3726.
Before: A maintained birth ledger keeps clinic supplies, witnesses, and the next generation's first household aligned.

After: The clinic keeps medicine, witnesses, and household support ready for the next birth.

### fallout_first_safe_birth_failed

Source line: 3727.
Before: Birth Ledger Strain

After: Birth Care Strain

### fallout_first_safe_birth_failed_desc

Source line: 3728.
Before: A strained birth ledger leaves medicine, shelter access, and the Deaths record exposed to the next shortage.

After: Medicine shortages and uncertain shelter access leave mothers and children exposed to the next crisis.

### chaosx.fallout.321.a

Source line: 3762.
Before: Close the first-light ledger

After: The first lights have been tested.

### chaosx.fallout.779.partial.d

Source line: 3877.
Before: The route memory survived, but the convoy keeps one harbor ledger of its own. The council can trade with it while the signal code is revised.

After: The route memory survived, but the convoy keeps one harbour plan of its own. The council can trade with it while the signal code is revised.

### fallout.event_log.ghost_convoy.detail.callback_partial

Source line: 3900.
Before: The route memory survived while the convoy kept a separate harbor ledger.

After: The route memory survived while the convoy kept a separate harbour plan.

### chaosx.fallout.784.evacuate.success.d

Source line: 4075.
Before: The harbor loaded families, tools, clinic ledgers, and the lighthouse lens onto three convoy hulls. The empty piers remain a claim on the map, while the survivors carry a precise record of every berth left behind.

After: The harbor loaded families, tools, patient lists, and the lighthouse lens onto three convoy hulls. The empty piers remain a claim on the map, while the survivors carry a precise record of every berth left behind.

### fallout.event_log.harbor_without_city.detail.evacuate_success

Source line: 4101.
Before: Families, tools, clinic ledgers, and the lighthouse lens left on three hulls.

After: Families, tools, patient lists, and the lighthouse lens left on three hulls.

### fallout_harbor_without_city_callback_partial

Source line: 4112.
Before: Shared Harbor Ledger

After: Shared Harbour Authority

### chaosx.fallout.749.health_compact.partial.d

Source line: 4135.
Before: The compact covers the North Gate and one clinic district. The other wards keep separate medicine ledgers, so the first regional authority exists only where a clerk can carry its seal.

After: The compact covers the North Gate and one clinic district. The other wards keep separate medicine tallies, so the first regional authority exists only where a clerk can carry its seal.

### chaosx.fallout.751.failure.d

Source line: 4151.
Before: The delayed review finds separate ledgers, closed roads, and a clinic network that serves the council before the patient. The Quarantine government keeps its authority, but the region has learned to make other plans.

After: The delayed review finds separate rules, closed roads, and a clinic network that serves the council before the patient. The Quarantine government keeps its authority, but the region has learned to make other plans.

### fallout.event_log.health_without_borders.callback_failure

Source line: 4183.
Before: The delayed review found separate ledgers and a region already planning without the council.

After: The delayed review found separate rules and a region already planning without the council.

### chaosx.fallout.677.d

Source line: 4198.
Before: The quartermaster at [?fallout_event_dispatch_issued_target.GetName] has placed the battalion's ration list beside the household ledger. Field kitchens are thinning their soup, yet the granary still carries the marks left by Work for Rations. [GetFalloutEvent677RationAuthority] must decide whether a rifle earns a heavier measure, whether every bowl meets the same scale, whether patrols may collect food in the field, or whether rear personnel return to the harvest.

After: The quartermaster at [?fallout_event_dispatch_issued_target.GetName] has placed the battalion's ration list beside the household roll. Field kitchens are thinning their soup, yet the granary still carries the marks left by Work for Rations. [GetFalloutEvent677RationAuthority] must decide whether a rifle earns a heavier measure, whether every bowl meets the same scale, whether patrols may collect food in the field, or whether rear personnel return to the harvest.

### chaosx.fallout.679.requisition.partial.d

Source line: 4216.
Before: The patrols reached the granary at [?fallout_event_dispatch_issued_target.GetName] with half their carts full. They also brought injured farmers, damaged seed stores, and a requisition ledger that no village accepts as settled.

After: The patrols reached the granary at [?fallout_event_dispatch_issued_target.GetName] with half their carts full. They also brought injured farmers, damaged seed stores, and a requisition order that no village accepts as settled.

### chaosx.fallout.679.a

Source line: 4221.
Before: Enter the issue in both ledgers

After: The ration measure is settled.

### chaosx.fallout.679.a.tt

Source line: 4222.
Before: Apply the ration policy to Food Compact resources, military readiness, the selected state's Air Winter conditions, and the civil-military ledgers. The second measure is taken after 210 days.

After: Apply the ration policy to Food Compact resources, military readiness, the selected state's Air Winter conditions, and the civilian and military ration rules. The second measure is taken after 210 days.

### chaosx.fallout.496.t

Source line: 4301.
Before: The Ice Ledger Review

After: The Ice Melt Review

### chaosx.fallout.496.failure.d

Source line: 4304.
Before: The review closes with the lake still sealed. The last boiler crew has left for the school shelter, the filter ledger is in dispute, and the next thaw will begin under a government that no longer trusts its own water marks.

After: The review closes with the lake still sealed. The last boiler crew has left for the school shelter, the filter supply is in dispute, and the next thaw will begin under a government that no longer trusts its own water marks.

### chaosx.fallout.496.a

Source line: 4305.
Before: Close the ice ledger

After: The ice melt review is finished.

### fallout.event_log.ice_melt_rations.boil_and_filter_success

Source line: 4310.
Before: A controlled boil filled the clinic cistern and restored a frozen-night water ledger.

After: A controlled boil filled the clinic cistern and restored a frozen-night water schedule.

### fallout.event_log.ice_melt_rations.use_untreated_water_success

Source line: 4313.
Before: Untreated meltwater kept the wards open under a public risk ledger.

After: Untreated meltwater kept the wards open under a public health warning.

### fallout.event_log.ice_melt_rations.callback_failure

Source line: 4324.
Before: The review closed with the lake sealed and the settlement's filter ledger in dispute.

After: The review closed with the lake sealed and the settlement's filter supply in dispute.

### chaosx.fallout.102.t

Source line: 4374.
Before: The Ration Ledger

After: The Ration Supply

### chaosx.fallout.107.d_option.tt

Source line: 4411.
Before: Let foreign technicians inspect the intake, trade access for medicine, and record the first water compact in the diplomatic ledger.

After: Let foreign technicians inspect the intake and trade access for medicine under a written water compact.

### chaosx.fallout.110.success.d

Source line: 4421.
Before: Filter teams keep the river moving through the clinic line and the kitchen cisterns. The stock ledger is thinner, but every district receives the same stamped measure.

After: Filter teams keep the river moving through the clinic line and the kitchen cisterns. The remaining stock is thinner, but every district receives the same stamped measure.

### chaosx.fallout.121.partial.d

Source line: 4436.
Before: The foreign test produces a usable sample and a disputed report. Medicine reaches the clinics, but the visiting technicians leave with copies of the intake ledger and no agreement about who owns the next repair.

After: The foreign test produces a usable sample and a disputed report. Medicine reaches the clinics, but the visiting technicians leave with copies of the intake list and no agreement about who owns the next repair.

### chaosx.fallout.112.failure.d

Source line: 4444.
Before: The clinic register becomes an epidemic ledger. The intake is still open, but medicine, water, and trust now move through separate queues, each guarded by a different authority.

After: The clinics face a growing epidemic. The intake is still open, but medicine, water, and trust now move through separate queues, each guarded by a different authority.

### fallout_water_epidemic_aftershock_desc

Source line: 4463.
Before: The water review failed to contain the intake, and clinics are carrying an epidemic ledger beside the ordinary ration book.

After: The water review failed to contain the intake, and clinics face a growing epidemic alongside the ordinary ration queues.

### fallout.event_log.river_intake.detail.callback_failure

Source line: 4481.
Before: The follow-up review became an epidemic ledger beside the ordinary ration book.

After: The follow-up found a growing epidemic alongside the ordinary ration queues.

### chaosx.fallout.114.d

Source line: 4484.
Before: The Ashline dispatch office has lost the eastern signal posts. Rail Crew Twenty-Seven is still under the viaduct with two repair trains, a fuel ledger, and enough sealed tools to restore one corridor. The line crosses a state where the winter register is already below its safe phase. We can send a protected crew, put labor battalions on the sleepers, abandon the line before the bridge gives way, or ask the neighboring authority to share access under a written dispatch rule.

After: The Ashline dispatch office has lost the eastern signal posts. Rail Crew Twenty-Seven is still under the viaduct with two repair trains, a fuel tally, and enough sealed tools to restore one corridor. The line crosses a state where the winter register is already below its safe phase. We can send a protected crew, put labor battalions on the sleepers, abandon the line before the bridge gives way, or ask the neighboring authority to share access under a written dispatch rule.

### fallout.event_log.last_inventory.detail.public_success

Source line: 4573.
Before: The public ration ledger held through the first review. The country published strict measures and kept the warehouse count legible.

After: The public ration rules held through the first review. The country published strict measures and kept the warehouse count legible.

### fallout.event_log.last_inventory.detail.public_partial

Source line: 4574.
Before: The public ration ledger opened the stores to inspection, but late deliveries and missing sacks weakened the promise.

After: The public ration rules opened the stores to inspection, but late deliveries and missing sacks weakened the promise.

### fallout.event_log.last_inventory.detail.public_failure

Source line: 4575.
Before: The public ration ledger failed to reach the kitchens before the shortage did. The decision left a lasting grievance.

After: The public ration rules failed to reach the kitchens before the shortage did. The decision left a lasting grievance.

### fallout_food_security_category_desc

Source line: 4589.
Before: The first inventory review has opened a ration office and a hunger mission. Both spend scarce stores to make the winter ledger answer to kitchens, clinics, and district councils.

After: The first inventory review has opened a ration office and a hunger mission. Both spend scarce stores to make the winter plan answer to kitchens, clinics, and district councils.

### chaosx.fallout.840.universal_rights.success.d

Source line: 4610.
Before: The Manchurian Reactor Keeps opened its civic register to every household that could show a repair, clinic, or shelter ledger. The wider roll gave eastern councils a reason to trust the Technate again, and the first laboratory class began with names rather than inherited access.

After: The Manchurian Reactor Keeps opened its civic register to every household that could show a repair, clinic, or shelter roll. The wider roll gave eastern councils a reason to trust the Technate again, and the first laboratory class began with names rather than inherited access.

### chaosx.fallout.253.a

Source line: 4713.
Before: Close the transformer ledger

After: The transformer has faced another winter.

### fallout.event_log.last_transformer.detail.callback_failure

Source line: 4748.
Before: The grid memory became a liability in the next repair ledger.

After: The failing grid left the next repair crews with more work than they could handle.

### chaosx.fallout.805.food_priority.failure.d

Source line: 4770.
Before: The depot circuit went dark while the night crew was moving the grain ledger. Fuel was spent without keeping the cold rooms shut, and the food queue has become a contest between the reactor keep and the shelters along the ash road.

After: The depot circuit went dark while the night crew was moving the grain inventory. Fuel was spent without keeping the cold rooms shut, and the food queue has become a contest between the reactor keep and the shelters along the ash road.

### chaosx.fallout.807.success.d

Source line: 4780.
Before: The first-winter review found a power board with a named order, a working reserve ledger, and enough trust to publish the next outage before it reached the wards. The Manchurian Reactor Keeps still has competing sectors, but its circuit decisions can now be challenged without opening the turbine doors.

After: The first-winter review found a power board with a named order, a working reserve plan, and enough trust to publish the next outage before it reached the wards. The Manchurian Reactor Keeps still has competing sectors, but its circuit decisions can now be challenged without opening the turbine doors.

### fallout.event_log.load_shedding.detail.food_priority_success

Source line: 4794.
Before: The food depots protected cold rooms and turned the ration queue into a civic ledger.

After: The food depots protected cold rooms and turned the ration queue into a public ration service.

### fallout.event_log.load_shedding.detail.food_priority_failure

Source line: 4796.
Before: The depot circuit went dark while the grain ledger was being moved.

After: The depot circuit went dark while the grain inventory was being moved.

### fallout.event_log.load_shedding.detail.callback_partial

Source line: 4804.
Before: The grid survived its first winter while every sector kept a different reserve ledger.

After: The grid survived its first winter while every sector kept a different reserve plan.

### fallout_load_shedding_callback_partial

Source line: 4811.
Before: Shared Reserve Ledger

After: Shared Reserve Plan

### chaosx.fallout.847.follow_recommendation.success.d

Source line: 4834.
Before: The machine's recommendation moved clinic hours and rail repairs across the Manchurian Reactor Keeps without losing a single signed household ledger. The output gain gave the Technate a reason to trust its surviving records, while human supervisors retained the right to stop a dangerous order.

After: The machine's recommendation moved clinic hours and rail repairs across the Manchurian Reactor Keeps without losing a single signed household roll. The output gain gave the Technate a reason to trust its surviving records, while human supervisors retained the right to stop a dangerous order.

### chaosx.fallout.847.sandbox_test.failure.d

Source line: 4839.
Before: The sealed district lost its comparison ledger when a fuel pump failed. The machine's recommendation remained unproven, the gate crew took blame for the outage, and the Technate spent another cold shift without a trusted schedule.

After: The sealed district lost its test results when a fuel pump failed. The machine's recommendation remained unproven, the gate crew took blame for the outage, and the Technate spent another cold shift without a trusted schedule.

### fallout.event_log.machine_suggests.detail.sandbox_test_failure

Source line: 4868.
Before: A failed fuel pump erased the sealed test's comparison ledger.

After: A failed fuel pump erased the sealed test's test results.

### fallout.event_log.machine_suggests.detail.human_review_failure

Source line: 4871.
Before: The review dissolved over incompatible ledgers and lost the repair window.

After: The review dissolved over conflicting instructions and lost the repair window.

### fallout_machine_suggests_human_review

Source line: 4887.
Before: Human Ledger Review

After: Human Engineering Review

### chaosx.fallout.382.tax_market.success.d

Source line: 4961.
Before: The levy crews measured each stall against the depot ledger and returned receipts before dusk. Public stores gained food and rail scrap, and traders kept their routes because the tax was predictable.

After: The levy crews measured each stall against the depot tally and confirmed each payment before dusk. Public stores gained food and rail scrap, and traders kept their routes because the tax was predictable.

### chaosx.fallout.384.partial.d

Source line: 4975.
Before: The review found trade under the arches, but the price board and ration ledger no longer agreed. The route can continue with a second measure at every depot and less faith in a single market voice.

After: The review found trade under the arches, but the price board and ration book no longer agreed. The route can continue with a second measure at every depot and less faith in a single market voice.

### chaosx.fallout.384.a

Source line: 4977.
Before: Close the market ledger

After: The market has faced its first review.

### chaosx.fallout.510.t

Source line: 5025.
Before: The Kilometer Twelve Ledger

After: The Kilometer Twelve Review

### chaosx.fallout.510.a

Source line: 5029.
Before: File the route report and close the ledger

After: We know whether Kilometer Twelve is passable.

### chaosx.fallout.614.opening.d

Source line: 5053.
Before: The capital's lower districts have survived behind sealed gates, ration ledgers, and a ventilation system that cannot carry every ward at once. Surface clerks, tunnel delegates, soldiers, and families have arrived at the same control room with different ideas about what the republic still means.

After: The capital's lower districts have survived behind sealed gates, ration books, and a ventilation system that cannot carry every ward at once. Surface clerks, tunnel delegates, soldiers, and families have arrived at the same control room with different ideas about what the republic still means.

### chaosx.fallout.616.tunnel.success.d

Source line: 5066.
Before: The ward delegates kept local control of rations and vents while accepting a common emergency ledger. The lower levels have not become independent, but their authority is now recognized.

After: The ward delegates kept local control of rations and vents while accepting a common emergency plan. The lower levels have not become independent, but their authority is now recognized.

### fallout.event_log.metro_republic_below.choice_tunnel

Source line: 5095.
Before: The country kept the metro wards autonomous under a common ledger.

After: The country kept the metro wards autonomous under common rules.

### fallout.event_log.metro_republic_below.tunnel_success

Source line: 5101.
Before: The ward compact kept local authority while accepting a common emergency ledger.

After: The ward compact kept local authority while accepting a common emergency plan.

### chaosx.fallout.642.d

Source line: 5119.
Before: In the Sub-Saharan state of [?fallout_event_dispatch_issued_target.GetName], a generator shed now decides whether the works can feed the settlements around it. A continuity cabinet wants a clean trade ledger, a garrison authority wants a labor shift, an engineer council wants control of the machinery, and a convoy administration wants to evacuate the most exposed workers. The native coal and metal deposits are known, but the people, stores, and roads that reach them are not.

After: In the Sub-Saharan state of [?fallout_event_dispatch_issued_target.GetName], a generator shed now decides whether the works can feed the settlements around it. A continuity cabinet wants a clean trade agreement, a garrison authority wants a labor shift, an engineer council wants control of the machinery, and a convoy administration wants to evacuate the most exposed workers. The native coal and metal deposits are known, but the people, stores, and roads that reach them are not.

### chaosx.fallout.642.a.tt

Source line: 5121.
Before: Spend Power 3, Scrap 2, and Recognition 2. In [?fallout_event_dispatch_issued_target.GetName], the trade ledger risks foreign concession pressure. After 42 days, the mine works will be judged by food reserves, supply access, reclamation, disease pressure, and the selected native resource class.

After: Spend Power 3, Scrap 2, and Recognition 2. In [?fallout_event_dispatch_issued_target.GetName], the trade agreement risks foreign concession pressure. After 42 days, the mine works will be judged by food reserves, supply access, reclamation, disease pressure, and the selected native resource class.

### chaosx.fallout.642.b.tt

Source line: 5123.
Before: Spend Food 3, Fuel 2, and Command Power 10. In [?fallout_event_dispatch_issued_target.GetName], the labor shift risks worker trust, food debt, and guarded unrest. After 42 days, the works will be judged by the ration ledger, war conditions, worker trust, and the authority of the labor roster.

After: Spend Food 3, Fuel 2, and Command Power 10. In [?fallout_event_dispatch_issued_target.GetName], the labor shift risks worker trust, food debt, and guarded unrest. After 42 days, the works will be judged by the ration book, war conditions, worker trust, and the authority of the labor roster.

### chaosx.fallout.644.t

Source line: 5128.
Before: The Generator Ledger

After: The Generator Supply

### chaosx.fallout.644.trade.partial.d

Source line: 5130.
Before: The trade ledger brought fuel and tools to the generator shed, but outside claims still press against the local stores. The works continue at a reduced rhythm while food debt and foreign concession pressure remain visible in the district memory.

After: The trade agreement brought fuel and tools to the generator shed, but outside claims still press against the local stores. The works continue at a reduced rhythm while food debt and foreign concession pressure remain visible in the district memory.

### chaosx.fallout.644.trade.failure.d

Source line: 5131.
Before: The trade ledger failed at the generator gate. Stores were divided before a schedule could be agreed, the plant lost part of its local supply, and the first people have died.

After: The trade agreement failed at the generator gate. Stores were divided before a schedule could be agreed, the plant lost part of its local supply, and the first people have died.

### chaosx.fallout.644.engineer.failure.d

Source line: 5137.
Before: The engineer council claimed the plant before it could secure the stores. Repairs failed, the industrial works lost infrastructure, and disease and exposure rose around a generator that no longer answers to a common ledger.

After: The engineer council claimed the plant before it could secure the stores. Repairs failed, the industrial works lost infrastructure, and disease and exposure rose around a generator that no longer answers to common rules.

### chaosx.fallout.644.a

Source line: 5141.
Before: Record the generator ledger

After: The generator crews have their answer.

### chaosx.fallout.646.success.d

Source line: 5144.
Before: Two hundred and seventy days later, rain has reached the Sub-Saharan works and the generator ledger can still be read. The district has a working answer for food, stores, and machine authority, while the native deposit record remains a witness rather than a target of the chain.

After: Two hundred and seventy days later, rain has reached the Sub-Saharan works and the generator plan can still be read. The district has a working answer for food, stores, and machine authority, while the native deposit record remains a witness rather than a target of the chain.

### fallout_mine_partial_country

Source line: 5158.
Before: Mine Generator Contested Ledger

After: Mine Generator Disputed Supply

### fallout.event_log.mine_generator.trade_success

Source line: 5173.
Before: The trade ledger kept the generator running while local stores and native resource evidence stayed distinct.

After: The trade agreement kept the generator running while local stores and native resource evidence stayed distinct.

### fallout.event_log.mine_generator.trade_partial

Source line: 5174.
Before: The trade ledger kept part of the works active while food debt and concession pressure remained.

After: The trade agreement kept part of the works active while food debt and concession pressure remained.

### fallout.event_log.mine_generator.trade_failure

Source line: 5175.
Before: The trade ledger failed and the district recorded infrastructure damage and winter loss.

After: The trade agreement failed and the district recorded infrastructure damage and winter loss.

### fallout.event_log.mine_generator.callback_success

Source line: 5185.
Before: The delayed review found a readable generator ledger after the rains.

After: The delayed review found a readable generator plan after the rains.

### fallout.event_log.mine_generator.callback_partial

Source line: 5186.
Before: The delayed review found working intervals and several unresolved district ledgers.

After: The delayed review found working intervals and several unresolved district rolls.

### chaosx.fallout.529.search_ruins.partial.d

Source line: 5205.
Before: The search team recovered a radio fragment and one blood-marked map, but the watchtower floor collapsed before the patrol could be found. The route is open for one guarded convoy and the missing ledger remains active.

After: The search team recovered a radio fragment and one blood-marked map, but the watchtower floor collapsed before the patrol could be found. The route is open for one guarded convoy and the missing patrol inquiry remains active.

### chaosx.fallout.529.cover_up.success.d

Source line: 5210.
Before: The council publishes a short training notice and keeps the patrol name out of the public register. The road stays quiet for now, but the missing ledger is thinner than the official account and the families keep their own record.

After: The council publishes a short training notice and conceals the patrol's name. The road stays quiet, but families keep searching and comparing what officials have left unexplained.

### chaosx.fallout.531.success.d

Source line: 5219.
Before: The review board matches the radio fragment, the route map, and the shelter ledger. The missing patrol has a named cause memory, and the state can reopen the road under a written search and relief rule.

After: The review board matches the radio fragment, the route map, and the shelter roll. The missing patrol has a named cause memory, and the state can reopen the road under a written search and relief rule.

### chaosx.fallout.531.failure.d

Source line: 5221.
Before: The review board finds that the radio, route, and casualty ledger describe different operations. The marker is lost again, a state facility is damaged, and more patrol members die in the confusion.

After: The review board finds that the radio, route, and casualty list describe different operations. The marker is lost again, a state facility is damaged, and more patrol members die in the confusion.

### chaosx.fallout.887.opening.d

Source line: 5246.
Before: After the Congo Green Basin names itself in public, river households and altered survivors ask to share the same pump road. The old district ledger lists two kinds of resident, while a foreign witness waits for one answer. The Basin must decide whether common ground is a right, a boundary, a supervised promise, or a line that cannot be crossed.

After: After the Congo Green Basin names itself in public, river households and altered survivors ask to share the same pump road. The old district roll lists two kinds of resident, while a foreign witness waits for one answer. The Basin must decide whether common ground is a right, a boundary, a supervised promise, or a line that cannot be crossed.

### chaosx.fallout.889.equal_citizenship.partial.d

Source line: 5258.
Before: The central ward accepts one register, but the hill road keeps a second ledger for winter arrivals. The Basin has a shared right on paper and a practical boundary that still depends on which bridge is open.

After: The central ward accepts one register, but the hill road keeps a separate account for winter arrivals. The Basin has a shared right on paper and a practical boundary that still depends on which bridge is open.

### chaosx.fallout.891.failure.d

Source line: 5274.
Before: The delayed review finds separate ledgers, missing permits, and no steward willing to sign for the next convoy. The Basin remembers choosing a settlement rule, but the shared road has become another source of fear.

After: The delayed review finds separate rules, missing permits, and no steward willing to sign for the next convoy. The Basin remembers choosing a settlement rule, but the shared road has become another source of fear.

### fallout.event_log.mixed_settlement.detail.equal_citizenship_partial

Source line: 5284.
Before: A shared register held in the central ward while the hill road kept a second ledger.

After: A shared register held in the central ward while the hill road kept a separate account.

### chaosx.fallout.637.military.success.d

Source line: 5332.
Before: The garrison moved its stores into the shelter without closing the household ledger. A permanent watch now guards the mountain road, soldiers receive a counted ration, and the war cabinet can hold the pass without pretending that families below have vanished.

After: The garrison moved its stores into the shelter without closing the household roll. A permanent watch now guards the mountain road, soldiers receive a counted ration, and the war cabinet can hold the pass without pretending that families below have vanished.

### fallout.event_log.mountain_pass_census.military_success

Source line: 5376.
Before: The garrison held the pass while preserving a counted civilian ledger.

After: The garrison held the pass while preserving a counted civilian ration roll.

### chaosx.fallout.763.refuse_contact.failure.d

Source line: 5413.
Before: The gate closed without a receipt or a safe route home. The envoy's government withdrew its liaison, and the Basin council now has to explain why a recorded border became an unrecorded threat.

After: The gate closed without an answer or a safe route home. The envoy's government withdrew its liaison, and the Basin council now has to explain why a recorded border became an unrecorded threat.

### fallout.event_log.mutant_envoy_gate.detail.refuse_contact_failure

Source line: 5439.
Before: The gate closed without a receipt and the neighboring liaison withdrew.

After: The gate closed without an answer and the neighboring liaison withdrew.

### chaosx.fallout.875.local_identity.partial.d

Source line: 5473.
Before: The river name reached the pump houses and two district ledgers. The eastern shore still uses the cracked sign, but the council has a word that can be carried without borrowing an old capital's authority.

After: The river name reached the pump houses and two district rolls. The eastern shore still uses the cracked sign, but the council has a word that can be carried without borrowing an old capital's authority.

### chaosx.fallout.279.success.d

Source line: 5570.
Before: The follow-up found a country that can carry its missing names into the next season. The register has a custodian, the shelter rolls share one correction route, and [ROOT.GetAirWinterGovernmentOfficial] can answer a family without opening three separate ledgers.

After: The follow-up found a country that can carry its missing names into the next season. The register has a custodian, the shelter rolls share one correction route, and [ROOT.GetAirWinterGovernmentOfficial] can answer a family without sending them to three separate offices.

### fallout_names_missing_ledger_maintained

Source line: 5599.
Before: Maintained Names Ledger

After: Names Restored

### fallout_names_missing_ledger_maintained_desc

Source line: 5600.
Before: A maintained ledger keeps shelter rolls, food tickets, and correction desks aligned after the first census.

After: Shelter rolls, food tickets, and correction desks now agree on who needs support.

### chaosx.fallout.551.success.d

Source line: 5650.
Before: The cemetery walls held through the thaw. One correction route now joins the shelter rolls, district witnesses, and the memorial stones, and [ROOT.GetAirWinterGovernmentOfficial] can answer a family without opening three separate ledgers.

After: The cemetery walls held through the thaw. One correction route now joins the shelter rolls, district witnesses, and the memorial stones, and [ROOT.GetAirWinterGovernmentOfficial] can answer a family without sending them to three separate offices.

### fallout_new_funeral_ledger_maintained

Source line: 5682.
Before: Maintained Funeral Ledger

After: Memorial Rolls Preserved

### chaosx.fallout.651.feast.success.d

Source line: 5712.
Before: A measured ration feast gave the settlement one warm table without emptying the storehouse. Guards and families shared the same queue, the water tins stayed clean, and the shared-table trust ledger rose with the new year.

After: A measured ration feast gave the settlement one warm table without emptying the storehouse. Guards and families shared the same queue, the water tins stayed clean, and the shared meal strengthened public trust.

### chaosx.fallout.651.feast.partial.d

Source line: 5713.
Before: The ration feast reached the central shelters, but the last tables received thin portions. The settlement kept its water and its dignity, while the shared-table trust ledger rose only slightly.

After: The ration feast reached the central shelters, but the last tables received thin portions. The settlement kept its water and its dignity, while the shared meal did little to restore public trust.

### chaosx.fallout.651.feast.failure.d

Source line: 5714.
Before: The ration feast outran the stores before the last district arrived. Empty tins and a crowded gate turned the celebration into a dispute, leaving the shared-table trust ledger weaker than it began.

After: The ration feast outran the stores before the last district arrived. Empty tins and a crowded gate turned the celebration into a dispute, leaving the public trust weaker than it began.

### chaosx.fallout.651.military.partial.d

Source line: 5716.
Before: The military ceremony held the central square, but the outer roads remained dark. The guards kept order and the martial pageantry ledger rose, although families outside the patrol line were left to mark the turn alone.

After: The military ceremony held the central square, but the outer roads remained dark. The guards kept order and the military ceremony gained support, although families outside the patrol line were left to mark the turn alone.

### fallout.event_log.new_year_without_fireworks.detail.feast_failure

Source line: 5738.
Before: An overrun ration feast left empty tins and a weaker shared-table trust ledger.

After: An overrun ration feast left empty tins and weaker public trust.

### chaosx.fallout.588.t

Source line: 5846.
Before: The Airfield Ledger

After: The Airfield Supply

### chaosx.fallout.588.a.tt

Source line: 5861.
Before: Confirm the first airfield ledger and begin the delayed route review. The review will reauthenticate the country, target state, branch, and Fallout generation before it applies its result.

After: Confirm the first airfield plan and begin the delayed route review. The review only applies while the country, runway, and chosen route remain eligible.

### chaosx.fallout.590.partial.d

Source line: 5865.
Before: The route review found a working strip with a narrow margin. The aircraft flies when fuel, weather, and local permission meet, but every missed landing remains in the community ledger.

After: The route review found a working strip with a narrow margin. The aircraft flies when fuel, weather, and local permission meet, but every missed landing remains in the community's grievances.

### fallout.event_log.old_airfield_chain.detail.military_partial

Source line: 5879.
Before: Air command held the runway while the flight ledger split.

After: Air command held the runway while the flight schedules diverged.

### fallout_old_airfield_result_success

Source line: 5899.
Before: Old airfield ledger secured

After: Old airfield plan secured

### fallout_old_airfield_result_partial

Source line: 5901.
Before: Old airfield ledger contested

After: Old airfield plan contested

### fallout_old_airfield_result_failed

Source line: 5903.
Before: Old airfield ledger failed

After: Old airfield plan failed

### chaosx.fallout.1023.opening.d

Source line: 5916.
Before: When the Fertility Question memory closes in the Congo Green Basin, ward delegates bring a second ledger to the river clinic. It records coerced treatment, forged consent, and patients moved between the river wards and the hill road without a witness. The pages describe a brutal civic crime. The former clinic director asks for a hearing before the Basin decides whether knowledge, punishment, and care can share one room.

After: When the Fertility Question memory closes in the Congo Green Basin, ward delegates bring a separate account to the river clinic. It records coerced treatment, forged consent, and patients moved between the river wards and the hill road without a witness. The pages describe a brutal civic crime. The former clinic director asks for a hearing before the Basin decides whether knowledge, punishment, and care can share one room.

### chaosx.fallout.1023.b.tt

Source line: 5920.
Before: Spend Scrap 2, Power 2, and Recognition 2 to preserve the clinic ledgers and give each witness a recorded statement. The commission can expose a wider network, though the Basin may lose cohesion while the inquiry proceeds.

After: Spend Scrap 2, Power 2, and Recognition 2 to preserve the patient lists and give each witness a recorded statement. The commission can expose a wider network, though the Basin may lose cohesion while the inquiry proceeds.

### chaosx.fallout.1025.public_trial.partial.d

Source line: 5927.
Before: The public trial reaches the river wards, but rain cuts the hill road before every witness can speak. The council accepts a narrow finding and a supervised clinic, while one missing ledger leaves the former director's wider network in dispute.

After: The public trial reaches the river wards, but rain cuts the hill road before every witness can speak. The council accepts a narrow finding and a supervised clinic. Missing patient lists leave the former director's wider network in dispute.

### chaosx.fallout.1025.truth_commission.success.d

Source line: 5929.
Before: The truth commission copies the clinic ledgers into three ward archives and gives each witness a private route to amend a statement. It names the coercive practice, protects the river midwives, and allows the Basin to rebuild the clinic without returning the former director to command.

After: The truth commission copies the patient lists into three ward archives and gives each witness a private route to amend a statement. It names the coercive practice, protects the river midwives, and allows the Basin to rebuild the clinic without returning the former director to command.

### chaosx.fallout.1025.truth_commission.partial.d

Source line: 5930.
Before: The commission preserves the river ledger and two witness accounts, but the hill archive loses its power before the final interview. The Basin can name the abuse in one district, while another keeps arguing over whether the missing pages were destroyed or carried away.

After: The commission preserves the river patient list and two witness accounts, but the hill archive loses its power before the final interview. The Basin can name the abuse in one district. Another still argues over whether the missing pages were destroyed or carried away.

### fallout.event_log.old_doctor_trial.detail.choice_truth_commission

Source line: 5949.
Before: The Congo Green Basin convened a truth commission for the clinic ledgers.

After: The Congo Green Basin convened a truth commission for the patient lists.

### fallout.event_log.old_doctor_trial.detail.public_trial_partial

Source line: 5953.
Before: A public trial reached the river wards, but a missing hill ledger kept the finding narrow.

After: A public trial reached the river wards, but a missing hill patient list kept the finding narrow.

### chaosx.fallout.375.fund_observers.failure.d

Source line: 5997.
Before: The replacement batteries arrived after the first storm. The observers lost a week of readings, and the radio room filled with frost. Shelters received the warning through rumor instead of the station ledger.

After: The replacement batteries arrived after the first storm. The observers lost a week of readings, and the radio room filled with frost. Shelters received the warning through rumor instead of the station broadcasts.

### chaosx.fallout.375.abandon_station.failure.d

Source line: 6006.
Before: The evacuation crew left the tower unlocked. Wind tore pages from the climate ledger, and a scavenger fire ruined the radio batteries. The station has become a blank place on every map.

After: The evacuation crew left the tower unlocked. Wind tore pages from the climate notes, and a scavenger fire ruined the radio batteries. The station has become a blank place on every map.

### chaosx.fallout.375.a

Source line: 6007.
Before: Keep the forecast ledger open

After: Keep watching the weather.

### chaosx.fallout.377.t

Source line: 6010.
Before: The weather ledger returns

After: The weather review returns

### chaosx.fallout.377.a

Source line: 6014.
Before: Close the weather ledger

After: The weather review is finished.

### fallout.event_log.old_weather_station.callback_success

Source line: 6031.
Before: Received a complete weather ledger review

After: The weather observers completed their review.

### chaosx.fallout.742.scientific.partial.d

Source line: 6053.
Before: The research team secured the clinic and one archive room. Its findings will help the Ash Ward, though the sample ledger is incomplete and the public still cannot see who approved the work.

After: The research team secured the clinic and one archive room. Its findings will help the Ash Ward, though the sample list is incomplete and the public still cannot see who approved the work.

### fallout.event_log.open_the_sealed_city.science_partial

Source line: 6088.
Before: The clinic and one archive room opened, but the sample ledger remained incomplete.

After: The clinic and one archive room opened, but the sample list remained incomplete.

### chaosx.fallout.412.success.d

Source line: 6130.
Before: A year later, the orchard opens a second flowering row. The seed ledger, the growers, and the state granary now share one harvest date.

After: A year later, the orchard opens a second flowering row. The seed inventory, the growers, and the state granary now share one harvest date.

### fallout.event_log.orientation.detail.national_district_success

Source line: 6166.
Before: District settlements pooled shelter, scrap, and food under one winter ledger, preserving a route from neighborhood stores to the state reserve.

After: District settlements pooled shelter, scrap, and food under one winter plan, preserving a route from neighborhood stores to the state reserve.

### fallout.event_log.orientation.detail.resource_ration_failure

Source line: 6183.
Before: The ration office ran out of usable stock before the review closed, and the crisis record carries a medicine loss beside the empty food ledger.

After: The ration office ran out of usable stock, and the crisis left both food and medicine short.

### fallout.event_log.orientation.detail.resource_tailored_failure

Source line: 6189.
Before: A tailored reserve plan chose a route the state could not supply, leaving the crisis ledger with a visible shortfall and no credible second measure.

After: The reserve plan chose a route the state could not supply and left too little stock for a second attempt.

### fallout_orientation_government_rival_mekong_greenhouse_compact

Source line: 6269.
Before: Bring the armed ferry command under the greenhouse ledger.

After: Bring the armed ferry command under the greenhouse council.

### fallout_orientation_tailored_resource_federal_continuity_zone

Source line: 6369.
Before: Put the grain trains, county ledgers, and capital filter workshops under one federal dispatch

After: Put the grain trains, county ration books, and capital filter workshops under one federal dispatch

### fallout_orientation_tailored_resource_don_steppe_hetmanates

Source line: 6372.
Before: Fuel guarded grain-road columns and Dnipro barges from one host ledger

After: Fuel guarded grain-road columns and Dnipro barges from one host supply plan

### fallout_orientation_resource_opening_mekong_greenhouse_compact

Source line: 6386.
Before: Protected seed, clinic loads, and urban rations are stranded on different banks. Ferry militias can move them through the cold rain, but village councils want every crossing entered in the greenhouse ledger.

After: Protected seed, clinic loads, and urban rations are stranded on different banks. Ferry militias can move them through the cold rain, but village councils want the greenhouse council to supervise every crossing.

### chaosx.fallout.62.d

Source line: 6475.
Before: [This.GetFalloutOrientationCauseMemoryText]\n\n[This.GetFalloutOrientationNationalRegionText]\n\nThe rewrite ledger counts [?fallout_orientation_frozen_country_population|0] living people under the authority of a [This.GetFalloutOrientationArchetypeName]. [This.GetFalloutOrientationGovernmentArchetypeText]\n\nThe strongest recorded survival value is [This.GetFalloutOrientationPrimaryResourceName] at [?fallout_orientation_frozen_primary_value|0]. The weakest is [This.GetFalloutOrientationWeakestResourceName] at [?fallout_orientation_frozen_weakest_value|0]. The first register must decide who is permitted to count homes, work crews, stores, and armed escorts across [This.GetFalloutOrientationRegionName].

After: [This.GetFalloutOrientationCauseMemoryText]\n\n[This.GetFalloutOrientationNationalRegionText]\n\n[?fallout_orientation_frozen_country_population|0] people live under the authority of a [This.GetFalloutOrientationArchetypeName]. [This.GetFalloutOrientationGovernmentArchetypeText]\n\nThe strongest survival resource is [This.GetFalloutOrientationPrimaryResourceName] at [?fallout_orientation_frozen_primary_value|0]. The weakest is [This.GetFalloutOrientationWeakestResourceName] at [?fallout_orientation_frozen_weakest_value|0]. The government must decide who can assign homes, work crews, stores, and armed escorts across [This.GetFalloutOrientationRegionName].

### chaosx.fallout.64.district.failure.d

Source line: 6489.
Before: District councils signed incompatible compacts and sent duplicate claims for the same shelter rooms. Families reached doors that had already been promised to work crews or militia households. The national office has lost authority, and the shelter ledger has lost space it cannot replace.[This.GetFalloutOrientationDeathsClause]

After: District councils signed incompatible compacts and sent duplicate claims for the same shelter rooms. Families reached doors that had already been promised to work crews or militia households. The national office has lost authority, and the shelter roll has lost space it cannot replace.[This.GetFalloutOrientationDeathsClause]

### chaosx.fallout.70.a

Source line: 6552.
Before: Publish a strict public ration ledger.

After: Publish strict public ration rules.

### chaosx.fallout.819.public_domain.failure.d

Source line: 6589.
Before: The register opened during a power cut and several plates were lost before they could be checked. The district kept its old repairs, but the public promise now carries a market grievance and less trust in the Technate's ledgers.

After: The register opened during a power cut and several plates were lost before they could be checked. The district kept its old repairs, but the public promise now carries a market grievance and less trust in the Technate's promises.

### fallout_patent_after_end_callback_partial

Source line: 6633.
Before: Shared Design Ledger

After: Shared Design Plans

### chaosx.fallout.700.audit.success.d

Source line: 6658.
Before: The audit compared clinic seals, ward ledgers, and the names carried by the winter teams. False permits were removed without erasing legitimate travel, and the registry became evidence rather than a second cordon.

After: The audit compared clinic seals, ward rolls, and the names carried by the winter teams. False permits were removed without erasing legitimate travel, and the registry became evidence rather than a second cordon.

### fallout.event_log.permit_market.detail.choice_audit

Source line: 6678.
Before: The Quarantine State audited clinic seals, ward ledgers, and movement permits.

After: The Quarantine State audited clinic seals, ward rolls, and movement permits.

### chaosx.fallout.789.b.tt

Source line: 6712.
Before: Spend Fuel 2, Recognition 3, and Cohesion 2 to give the crews a lawful patrol charter with a strict prize ledger.

After: Spend Fuel 2, Recognition 3, and Cohesion 2 to give the crews a lawful patrol charter with a strict cargo account.

### chaosx.fallout.791.public_trial.success.d

Source line: 6725.
Before: Witnesses, cargo marks, and the clinic's missing ledger survived the hearing. The court convicts one captain, releases the others under watch, and turns the prize fund into a public rescue account.

After: Witnesses, cargo marks, and the clinic's missing patient list survived the hearing. The court convicts one captain, releases the others under watch, and turns the prize fund into a public rescue account.

### fallout.event_log.pirate_amnesty.detail.choice_privateer_service

Source line: 6742.
Before: The harbor issued the former raiders a patrol charter and a prize ledger.

After: The harbor issued the former raiders a patrol charter and a cargo account.

### fallout.event_log.pirate_amnesty.detail.callback_success

Source line: 6757.
Before: The sea road gained a named court, a rescue oath, and a common ledger.

After: The sea road gained a named court, a rescue oath, and common rules.

### fallout_pirate_amnesty_callback_partial

Source line: 6765.
Before: Shared Prize Ledger

After: Shared Cargo Account

### chaosx.fallout.866.opening.d

Source line: 6777.
Before: The Repair Charter kept one workshop ledger alive, but it never answered who should own the current. In the Manchurian Reactor Keeps, three eastern substations can feed clinics, schools, or a protected rail line. The Technate must decide whether power is public citizenship, an engineer state, a grid empire, or a machine transition under human audit.

After: The Repair Charter kept one workshop schedule alive, but it never answered who should own the current. In the Manchurian Reactor Keeps, three eastern substations can feed clinics, schools, or a protected rail line. The Technate must decide whether power is public citizenship, an engineer state, a grid empire, or a machine transition under human audit.

### chaosx.fallout.1053.t

Source line: 6858.
Before: The Gate Ledger Answers

After: The Gate Inspection Ends

### chaosx.fallout.1053.accept_controls.success.d

Source line: 6859.
Before: The Basin signs the inspection ledger beneath the lower gate. Foreign nurses enter the river clinic with two Basin guards, every fever case receives a return seal, and the neighboring government reopens the ash road for medicine wagons.

After: The Basin signs the inspection agreement beneath the lower gate. Foreign nurses enter the river clinic with two Basin guards, every fever case receives a return seal, and the neighboring government reopens the ash road for medicine wagons.

### chaosx.fallout.1053.accept_controls.failure.d

Source line: 6861.
Before: The inspection team finds missing names and a flooded medicine store. The neighboring government closes the bridge again, while Basin guards argue over whether the foreign ledger or the hill archive carries the lawful count.

After: The inspection team finds missing names and a flooded medicine store. The neighboring government closes the bridge again, while Basin guards argue over whether the foreign patient list or the hill archive carries the lawful count.

### chaosx.fallout.1053.negotiate_inspection.success.d

Source line: 6862.
Before: Basin healers and foreign nurses sign one register at the bridge table. The joint team limits inspections to named symptoms, shares medicine receipts, and gives the Congo Green Basin a written voice in every closure order.

After: Basin healers and foreign nurses sign one register at the bridge table. The joint team limits inspections to named symptoms, shares medicine delivery notes, and gives the Congo Green Basin a written voice in every closure order.

### chaosx.fallout.1053.negotiate_inspection.failure.d

Source line: 6864.
Before: The inspection talks collapse when neither side accepts the other's patient tally. The foreign team leaves with its seals, the Basin hides the clinic ledger, and the lower river road returns to a guarded closure.

After: The inspection talks collapse when neither side accepts the other's patient tally. The foreign team leaves with its seals, the Basin hides the patient list, and the lower river road returns to a guarded closure.

### chaosx.fallout.1053.a

Source line: 6871.
Before: Seal the gate ledger

After: The gate inspection is finished.

### chaosx.fallout.1055.success.d

Source line: 6874.
Before: After the next wet season, the river and hill pages carry the same patient seals. The Basin keeps a named inspection rule, the neighboring government recognizes the three-party ledger, and the bridge opens without a new red line.

After: After the next wet season, the river and hill pages carry the same patient seals. The Basin keeps a named inspection rule, the neighboring government recognizes the three-party agreement, and the bridge opens without a new red line.

### chaosx.fallout.1055.partial.d

Source line: 6875.
Before: The review confirms a working medicine corridor, but the hill archive and foreign ledger still disagree about two family crossings. The lower gate remains open under escort while the Basin repairs its health register.

After: The review confirms a working medicine corridor, but the hill archive and foreign patient list still disagree about two family crossings. The lower gate remains open under escort while the Basin repairs its health register.

### fallout.event_log.quarantine_ultimatum.detail.choice_negotiate_inspection

Source line: 6882.
Before: The Congo Green Basin made its healers partners in a joint inspection ledger.

After: The Congo Green Basin made its healers partners in a joint inspection agreement.

### fallout.event_log.quarantine_ultimatum.detail.negotiate_inspection_success

Source line: 6888.
Before: A joint bridge ledger gave Basin healers a written voice in every closure order.

After: A joint bridge agreement gave Basin healers a written voice in every closure order.

### fallout.event_log.quarantine_ultimatum.detail.callback_failure

Source line: 6899.
Before: Missing seals and separate clinic counts ended recognition of the gate ledger.

After: Missing seals and separate clinic counts ended recognition of the gate agreement.

### fallout_quarantine_ultimatum_result_success

Source line: 6901.
Before: Gate Ledger Accepted

After: Gate Agreement Accepted

### fallout_quarantine_ultimatum_result_partial

Source line: 6902.
Before: Contested Inspection Ledger

After: Contested Inspection Agreement

### fallout_quarantine_ultimatum_negotiate_inspection

Source line: 6908.
Before: Joint Inspection Ledger

After: Joint Inspection Agreement

### chaosx.fallout.602.island_federation.failure.d

Source line: 6939.
Before: The federation crew left the tower unsecured. Wind tore pages from the signal ledger, a salvage fire ruined the batteries, and the island chain became a blank space on every surviving harbor chart.

After: The federation crew left the tower unsecured. Wind tore pages from the signal log, a salvage fire ruined the batteries, and the island chain became a blank space on every surviving harbor chart.

### chaosx.fallout.602.a

Source line: 6940.
Before: Keep the signal ledger open

After: Keep listening for the island signals.

### chaosx.fallout.604.a

Source line: 6947.
Before: Close the signal ledger

After: The signal review is finished.

### fallout.event_log.radio_island_chain.detail

Source line: 6951.
Before: [This.GetName] chose who would keep a remote island radio, harbor receiver, and cold-weather ledger alive. The decision changed shelter warnings, maritime patrols, outside contact, and the station's place in the region's recovery.

After: [This.GetName] chose who would keep a remote island radio and harbor receiver working through the cold. The decision changed shelter warnings, maritime patrols, outside contact, and the station's place in the region's recovery.

### chaosx.fallout.621.opening.d

Source line: 6973.
Before: Across the Eurasian interior, a surviving rail junction has become the only reliable way to move fuel, food, and repair crews between winter settlements. Depot keepers, convoy merchants, soldiers, and district delegates have brought separate ledgers to the same signal room. The line can carry a new compact, but only one authority can write its first timetable.

After: Across the Eurasian interior, a surviving rail junction has become the only reliable way to move fuel, food, and repair crews between winter settlements. Depot keepers, convoy merchants, soldiers, and district delegates have brought separate rules to the same signal room. The line can carry a new compact, but only one authority can write its first timetable.

### chaosx.fallout.623.central.failure.d

Source line: 6985.
Before: The central rail board failed to reconcile the depot ledgers. The junction signal remains lit, but no crew trusts the next handoff and a damaged rail section has taken the first route out of service.

After: The central rail board failed to reconcile the depot tallies. The junction signal remains lit, but no crew trusts the next handoff and a damaged rail section has taken the first route out of service.

### chaosx.fallout.623.military.success.d

Source line: 6989.
Before: The guard units secured the junction without replacing the civilian ledger. Trains now move with escorts and inspection rights, and the line can serve the front without turning every depot into a barracks.

After: The guard units secured the junction without replacing the civilian ration roll. Trains now move with escorts and inspection rights, and the line can serve the front without turning every depot into a barracks.

### chaosx.fallout.623.military.failure.d

Source line: 6991.
Before: The guard command seized the junction before the regional ledger could be signed. Rail damage and lost stores have halted the timetable, while the first dead are carried away from a platform that was meant to remain neutral.

After: The guard command seized the junction before the regional compact could be signed. Rail damage and lost stores have halted the timetable, while the first dead are carried away from a platform that was meant to remain neutral.

### fallout.event_log.rail_spine_vote.central_failure

Source line: 7020.
Before: The central board failed to reconcile the depot ledgers and the route broke down.

After: The central board failed to reconcile the depot tallies and the route broke down.

### fallout.event_log.rail_spine_vote.military_success

Source line: 7024.
Before: The guards secured the junction while a civilian ledger retained inspection rights.

After: The guards secured the junction while civilian inspectors kept their authority.

### chaosx.fallout.394.d

Source line: 7039.
Before: The ration ledger for [This.GetName] has lost a page. Grain entered as an emergency reserve is missing, and the queue outside the storehouse names the households that went without it. The accusation has become a test of who may speak for the settlement.

After: The ration book for [This.GetName] has lost a page. Grain entered as an emergency reserve is missing, and the queue outside the storehouse names the households that went without it. The accusation has become a test of who may speak for the settlement.

### chaosx.fallout.396.t

Source line: 7048.
Before: The Ledger Gives Its Answer

After: The Ration Inquiry Ends

### fallout.event_log.ration_thief_election.tribunal_success

Source line: 7074.
Before: A tribunal proved the ration ledger was forged and restored a repeatable hearing.

After: A tribunal proved the ration book was forged and restored a repeatable hearing.

### chaosx.fallout.501.quarantine_ravine_ward.partial.d

Source line: 7108.
Before: The ward is sealed, but two pump crews cross the cordon before the order reaches the lower road. The clinic gains a disease ledger while the neighboring district prepares its own watch.

After: The ward is sealed, but two pump crews cross the cordon before the order reaches the lower road. The clinic gains a fever watch while the neighboring district prepares its own watch.

### chaosx.fallout.503.failure.d

Source line: 7119.
Before: The review finds the ravine bench cold and the route ledger torn. Fever pressure rises around the lower pump, the next convoy is cancelled, and the government must rebuild trust before it can ask for another sample.

After: The review finds the ravine bench cold and the route book torn. Fever pressure rises around the lower pump, the next convoy is cancelled, and the government must rebuild trust before it can ask for another sample.

### fallout.event_log.ravine_water_chemist.quarantine_ravine_ward_partial

Source line: 7132.
Before: The ward was sealed after two pump crews crossed the cordon, leaving a disease ledger for the next watch.

After: Two pump crews crossed the cordon before the ward was sealed, leaving clinic staff to watch for fever.

### fallout.event_log.ravine_water_chemist.callback_failure

Source line: 7139.
Before: The service review found a cold bench, a torn route ledger, and rising fever pressure.

After: The service review found a cold bench, a torn route book, and rising fever pressure.

### chaosx.fallout.814.partial.d

Source line: 7172.
Before: The first-winter review found a functioning reactor with a tired night crew and a safety record that still depends on one foreign inspection seat. The keep can meet the next ash front, though the operator trust ledger remains contested.

After: The first-winter review found a functioning reactor with a tired night crew and a safety record that still depends on one foreign inspection seat. The keep can meet the next ash front, though the operators' trust remains contested.

### fallout.event_log.reactor_shift.detail.compel_duty_roster_success

Source line: 7185.
Before: The compelled roster restored output but left the operator trust ledger broken.

After: The compelled roster restored output but left the operators' trust broken.

### fallout_reactor_shift_callback_partial

Source line: 7202.
Before: Shared Safety Ledger

After: Shared Safety Rules

### chaosx.fallout.370.t

Source line: 7240.
Before: The cooling ledger returns

After: The Cooling Inspection

### chaosx.fallout.370.failure.d

Source line: 7243.
Before: The report arrived with a broken seal and a missing page from the fuel ledger. Guards closed the plant while rival claimants spread different figures. The reactor is again without a trusted country, even if its flag still flies.

After: The report arrived with a broken seal and a missing page from the fuel tally. Guards closed the plant while rival claimants spread different figures. The reactor is again without a trusted country, even if its flag still flies.

### chaosx.fallout.370.a

Source line: 7244.
Before: Close the reactor ledger

After: The reactor inspection is finished.

### fallout.event_log.reactor_without_a_country.callback_success

Source line: 7261.
Before: Received a clean reactor maintenance ledger

After: Received a clean reactor maintenance plan

### chaosx.fallout.417.admit_families.success.d

Source line: 7289.
Before: The families receive blankets, names, and a place in the ration ledger. Their arrival fills empty rooms without making the old residents pretend that food is plentiful.

After: The families receive blankets, names, and a place in the ration book. Their arrival fills empty rooms without making the old residents pretend that food is plentiful.

### fallout.event_log.refugee_train_bilateral.detail.admit_families_success

Source line: 7340.
Before: Families crossed the shelter gates, entered the ration ledger, and strengthened the compact between the two rail councils.

After: Families crossed the shelter gates, entered the ration book, and strengthened the compact between the two rail councils.

### chaosx.fallout.754.opening.d

Source line: 7358.
Before: The North Gate Health Corridor has become a road with two authorities and one winter clinic ledger. Ash Ward doctors will not send patients through another checkpoint without a promise that records, medicine, and responsibility cross together. The Quarantine council can turn the Health Without Borders register into a compact, but the neighboring state will remember which part of the promise it receives.

After: The North Gate Health Corridor has become a road with two authorities and one winter patient list. Ash Ward doctors will not send patients through another checkpoint without a promise that records, medicine, and responsibility cross together. The Quarantine council can turn the Health Without Borders register into a compact, but the neighboring state will remember which part of the promise it receives.

### chaosx.fallout.756.shared_register.success.d

Source line: 7369.
Before: The North Gate and Ash Ward now read the same patient ledger. A clinic can request medicine without asking which council owns the road, and the Quarantine government has accepted a duty that reaches beyond its state line.

After: The North Gate and Ash Ward now read the same patient list. A clinic can request medicine without asking which council owns the road, and the Quarantine government has accepted a duty that reaches beyond its state line.

### chaosx.fallout.861.open_charter.partial.d

Source line: 7435.
Before: The public charter reached the nearest settlements, but two crews used different names for the same bearing. The Keeps kept the route open and sent a senior mechanic to teach the shared parts ledger.

After: The public charter reached the nearest settlements, but two crews used different names for the same bearing. The Keeps kept the route open and sent a senior mechanic to teach the shared parts catalogue.

### chaosx.fallout.861.perimeter_corps.success.d

Source line: 7443.
Before: Perimeter corps received a protected charter for generators, field clinics, and radio corridors. Their repair crews restored two guarded substations, while civilian mechanics received safe fragments of the parts ledger.

After: Perimeter corps received a protected charter for generators, field clinics, and radio corridors. Their repair crews restored two guarded substations, while civilian mechanics received safe fragments of the parts catalogue.

### chaosx.fallout.716.success.d

Source line: 7520.
Before: Two hundred and ten days later, the returning fever has a stable treatment route. Ash Ward Hospital and North Gate clinic share a border ledger, the aid convoy follows its compact, and the Quarantine State can respond without reopening the old medical dispute.

After: Two hundred and ten days later, the returning fever has a stable treatment route. Ash Ward Hospital and North Gate clinic share a border register, the aid convoy follows its compact, and the Quarantine State can respond without reopening the old medical dispute.

### chaosx.fallout.716.failure.d

Source line: 7522.
Before: The second winter review found the fever route broken. Patients wait outside Ash Ward Hospital, the border ledger no longer matches the clinic books, and deaths are recorded before the public health office can assign a cause.

After: The second winter review found the fever route broken. Patients wait outside Ash Ward Hospital, the border register no longer matches the clinic books, and deaths are recorded before the public health office can assign a cause.

### fallout.event_log.returning_disease.detail.callback_success

Source line: 7543.
Before: The second winter review found one stable treatment route and a shared border ledger.

After: The second winter review found one stable treatment route and a shared border register.

### chaosx.fallout.567.upstream.partial.d

Source line: 7573.
Before: The upstream priority order moved grain through [?fallout_event_565_target_state_id.GetName], but the lower bank in [?fallout_event_565_downstream_state_id.GetName] received less than its winter ledger showed. The route survives with a visible debt between the depots.

After: The upstream priority order moved grain through [?fallout_event_565_target_state_id.GetName], but the lower bank in [?fallout_event_565_downstream_state_id.GetName] received less than its winter plan showed. The route survives with a visible debt between the depots.

### chaosx.fallout.567.a

Source line: 7581.
Before: Enter the result in the river ledger

After: The river depots have their answer.

### fallout.event_log.river_ration_league.detail.barge_success

Source line: 7607.
Before: A joint barge law secured a shared river ledger.

After: A joint barge law secured a shared river agreement.

### chaosx.fallout.289.a.tt

Source line: 7642.
Before: Spend [?constant:fallout_event_289_cost.technical_food|0] Food, [?constant:fallout_event_289_cost.technical_power|0] Power, and [?constant:fallout_event_289_cost.technical_scrap|0] Scrap. The delayed result measures shelter, food, Cohesion, and the education ledger.

After: Spend [?constant:fallout_event_289_cost.technical_food|0] Food, [?constant:fallout_event_289_cost.technical_power|0] Power, and [?constant:fallout_event_289_cost.technical_scrap|0] Scrap. The delayed result measures shelter, food, Cohesion, and the school program.

### chaosx.fallout.289.d_option.tt

Source line: 7645.
Before: Spend [?constant:fallout_event_289_cost.faith_food|0] Food, [?constant:fallout_event_289_cost.faith_medicine|0] Medicine, and [?constant:fallout_event_289_cost.faith_recognition|0] Recognition. The faith classroom can keep a family calendar beside the shelter ledger.

After: Spend [?constant:fallout_event_289_cost.faith_food|0] Food, [?constant:fallout_event_289_cost.faith_medicine|0] Medicine, and [?constant:fallout_event_289_cost.faith_recognition|0] Recognition. The faith classroom can keep a family calendar beside the shelter roll.

### chaosx.fallout.291.a

Source line: 7660.
Before: Open the cohort ledger

After: Welcome the first class.

### chaosx.fallout.293.partial.d

Source line: 7665.
Before: The cohort returned to a room that still teaches, although the outer shelters cannot attend every week. The education ledger is real, but its reach remains a privilege that the country must repair.

After: The cohort returned to a room that still teaches, although the outer shelters cannot attend every week. The school program is real, but its reach remains a privilege that the country must repair.

### fallout_school_vent_room_faith_desc

Source line: 7695.
Before: A shared rite keeps a family calendar and a language for grief beside the shelter ledger.

After: A shared rite keeps a family calendar and a language for grief beside the shelter roll.

### chaosx.fallout.333.open.partial.d

Source line: 7716.
Before: The crew cleared the front bay and stopped when the rear floor began to sweat through its ash. Some parts reached the repair yard, but a second ledger now records which families handled the first crates and which rooms must wait for cleaner tools.

After: The crew cleared the front bay and stopped when the rear floor began to sweat through its ash. Some parts reached the repair yard, but a separate account now records which families handled the first crates and which rooms must wait for cleaner tools.

### chaosx.fallout.333.leave.success.d

Source line: 7724.
Before: The doors stayed shut behind a new fence and a watch rota that names the people allowed to approach. Filters were spent on the sentries, the shelter ledger funded the lock, and the town kept a clean reserve without pretending the warehouse was harmless.

After: The doors stayed shut behind a new fence and a watch rota that names the people allowed to approach. Filters were spent on the sentries, shelter stores paid for the lock, and the town kept a clean reserve without pretending the warehouse was harmless.

### fallout.event_log.sealed_warehouse.open_partial

Source line: 7738.
Before: The warehouse opened in stages, leaving a contested rear bay and a public exposure ledger.

After: The warehouse opened in stages, leaving a contested rear bay and a public exposure list.

### chaosx.event_name.662

Source line: 7774.
Before: The Second Dust Bowl: Ledger Closure

After: The Second Dust Bowl: Recovery Review

### chaosx.fallout.658.move.success.d

Source line: 7789.
Before: Farm households in [?fallout_event_656_target_state_id.GetName] consolidated into protected parcels without leaving the same state. Equipment reached the new rows, supply access improved, and the mobility ledger now describes a repeatable move.

After: Farm households in [?fallout_event_656_target_state_id.GetName] consolidated into protected parcels without leaving the same state. Equipment reached the new rows, supply access improved, and the relocation plan now describes a repeatable move.

### chaosx.fallout.658.move.partial.d

Source line: 7790.
Before: The most exposed plots in [?fallout_event_656_target_state_id.GetName] reached protected ground, but the remaining equipment could not follow. The farm mobility ledger is useful, although food and shelter officers still disagree over the outer rows.

After: The most exposed plots in [?fallout_event_656_target_state_id.GetName] reached protected ground, but the remaining equipment could not follow. The farm relocation plan is useful, although food and shelter officers still disagree over the outer rows.

### chaosx.fallout.658.a

Source line: 7798.
Before: Read the field ledger

After: We know which fields survived.

### chaosx.fallout.190.t

Source line: 7861.
Before: The State Seed Ledger

After: The State Seed Stores

### chaosx.fallout.190.a

Source line: 7865.
Before: Give the agronomist one season to prove the ledger

After: Give the agronomist one season to test the seeds.

### chaosx.fallout.193.success.d

Source line: 7880.
Before: Licensed buyers paid in scrap and transport hours. The archive gained a working route to the fields, although every receipt now carries the names of those who could not bid.

After: Licensed buyers paid in scrap and transport hours. Their payments opened a route from the archive to the fields, but households unable to bid received no seeds.

### chaosx.fallout.193.a

Source line: 7883.
Before: Let the agronomist audit every receipt

After: Let the agronomist inspect each sale.

### chaosx.fallout.198.a

Source line: 7889.
Before: Record the review beside the seed ledger

After: We know which seeds survived.

### fallout.event_log.seed_vault.detail.auction_success

Source line: 7902.
Before: Licensed buyers financed a working seed route while the receipts recorded who could not bid.

After: Licensed buyers financed a working seed route, but households unable to bid received no seeds.

### chaosx.fallout.424.seize_manifest.partial.d

Source line: 7997.
Before: The cargo ledger is secured, though several crates are missing before the seals dry. The government gains supplies and a coastal faction that remembers the seizure.

After: The cargo manifest is secured, though several crates are missing before the seals dry. The government gains supplies and a coastal faction that remembers the seizure.

### chaosx.fallout.426.success.d

Source line: 8002.
Before: Months later the berth ledger still matches the clinic roster. The radio crew trains local operators, the quarantine ward has a routine, and the coast can name what it owes the ship.

After: Months later the berth list still matches the clinic roster. The radio crew trains local operators, the quarantine ward has a routine, and the coast can name what it owes the ship.

### fallout.event_log.ship_that_will_not_dock.seize_manifest_partial

Source line: 8019.
Before: The cargo ledger survived, though several crates disappeared before the seals dried.

After: The cargo manifest survived, though several crates disappeared before the seals dried.

### chaosx.fallout.433.success.d

Source line: 8054.
Before: The first review finds the roster in use. A doctor has trained two assistants, an engineer has left repair notes in three districts, and the growers have kept a seed ledger that survived the frost. The names now describe a generation of work rather than a list of survivors.

After: The first review finds the roster in use. A doctor has trained two assistants, an engineer has left repair notes in three districts, and the growers have kept a seed inventory that survived the frost. The names now describe a generation of work rather than a list of survivors.

### chaosx.fallout.459.t

Source line: 8090.
Before: The Meltwater Ledger

After: The Meltwater Routes

### chaosx.fallout.461.failure.d

Source line: 8108.
Before: The review found broken markers, a silent clinic ledger, and families back in the old basin. The floodwater memory has become a grievance that turns every repair into a government question.

After: The review found broken markers, missing patient lists, and families back in the old basin. Flood grievances have turned every repair into a dispute with the government.

### chaosx.fallout.177.failure.d

Source line: 8146.
Before: The children's ward in [?fallout_event_175_triage_state_id.GetName] ran out of measured courses before the shelter ledger was complete. People the triage wall could not protect have died, and the clinic has lost public trust.

After: The children's ward in [?fallout_event_175_triage_state_id.GetName] ran out of measured courses before the shelter roll was complete. People the triage wall could not protect have died, and the clinic has lost public trust.

### chaosx.fallout.177.a

Source line: 8147.
Before: Send the ward ledger to the doctor

After: Ask the doctor to review the ward.

### chaosx.fallout.178.partial.d

Source line: 8152.
Before: The workshop ward in [?fallout_event_175_triage_state_id.GetName] saved enough workers to keep one route open. The outer salvage teams still lost hours to fever, so the production ledger shows a recovery with a cost.

After: The workshop ward in [?fallout_event_175_triage_state_id.GetName] saved enough workers to keep one route open. The outer salvage teams still lost hours to fever, so the workshop output shows a recovery with a cost.

### fallout.event_log.triage_wall.detail.workers_failure

Source line: 8185.
Before: The workshop ward could not return its crews and the production ledger recorded the loss.

After: The workshop ward could not return its crews, and production fell.

### chaosx.fallout.607.d

Source line: 8200.
Before: In the East Asian shelter district, ventilation crews have kept three ward ledgers alive through the ash week. Delegates now ask who may open the ration books, who may appoint the tunnel watch, and who will answer when a family is turned away. The register cannot remain a private promise.

After: In the East Asian shelter district, ventilation crews have kept three wards alive through the ash week. Delegates now ask who may open the ration books, who may appoint the tunnel watch, and who will answer when a family is turned away.

### chaosx.fallout.609.recognize.success.d

Source line: 8210.
Before: The delegates sign a common charter beside the ventilation board. The ration clerks accept the ward seals, and families displaced from the southern industrial belt receive a place in the intake ledger.

After: The delegates sign a common charter beside the ventilation board. The ration clerks accept the ward seals, and families displaced from the southern industrial belt receive a place in the intake list.

### chaosx.fallout.609.recognize.partial.d

Source line: 8211.
Before: The councils are recognized, but the intake ledger remains uneven. Two wards share medicine while the third keeps its own ration tally.

After: The councils are recognized, but the intake list remains uneven. Two wards share medicine while the third keeps its own ration tally.

### chaosx.fallout.609.military.success.d

Source line: 8216.
Before: The tunnel watch takes the night roster and leaves the ration clerks in place. The wards hold the line, though every guard now knows that security has a cost in the common ledger.

After: The tunnel watch takes the night roster and leaves the ration clerks in place. The wards hold the line, but feeding the guards strains the common stores.

### chaosx.fallout.611.success.d

Source line: 8225.
Before: Two hundred and ten days later, the review board finds a working shelter institution. The East Asian ward ledgers agree on food, ventilation, and families admitted since the ash week.

After: Two hundred and ten days later, the review board finds a working shelter institution. The East Asian ward rolls agree on food, ventilation, and families admitted since the ash week.

### chaosx.fallout.611.failure.d

Source line: 8227.
Before: The review board cannot reconcile the ward ledgers. The ventilation crews keep working, yet the shelter loses people from the common register and returns to guarded lists.

After: The review board cannot reconcile the ward rolls. The ventilation crews keep working, yet the shelter loses people from the common register and returns to guarded lists.

### fallout.event_log.tunnel_ward_committees.recognize_partial

Source line: 8237.
Before: The ward charter survived, but the intake ledgers remained uneven.

After: The ward charter survived, but the intake lists remained uneven.

### fallout.event_log.tunnel_ward_committees.callback_failure

Source line: 8250.
Before: The delayed review could not reconcile the ward ledgers.

After: The delayed review could not reconcile the ward rolls.

### modifier_fallout_tunnel_ward_committees_partial

Source line: 8256.
Before: Uneven Ward Ledgers

After: Uneven Ward Rations

### chaosx.fallout.363.a

Source line: 8294.
Before: Close the archive ledger

After: The archive review is finished.

### chaosx.fallout.513.b.tt

Source line: 8322.
Before: Spend Scrap, Recognition, and Food to issue household receipts. The result will depend on civic trust and the state's supply position.

After: Spend Scrap, Recognition, and Food to issue weapon custody slips. The result will depend on civic trust and the state's supply position.

### chaosx.fallout.515.family_registry.success.d

Source line: 8331.
Before: Household receipts make the cache legible. Families bring each weapon to the table, receive a stamped number, and leave with a duty that neighbors can verify. The former nursery becomes a place of records rather than rumors.

After: Families bring each weapon to the table and receive a stamped custody slip. Neighbors can check who holds the cache and who must keep it safe. The former nursery no longer conceals an uncounted arsenal.

### chaosx.fallout.515.family_registry.partial.d

Source line: 8332.
Before: Most households accept the register, but three receipts carry the same serial mark. Food carts reach the room late, and the council postpones the second count. The cache is visible, yet a private reserve is forming behind the shelves.

After: Most households accept the register, but three custody slips carry the same serial mark. Food carts reach the room late, and the council postpones the second count. The cache is visible, yet a private reserve is forming behind the shelves.

### chaosx.fallout.517.success.d

Source line: 8343.
Before: The second inspection finds the custody rule intact. The former nursery is warm, the inventory matches its receipts, and the heating plant can run without a sentry choosing which household receives fuel. The memory is ready to close.

After: The second inspection finds the custody rule intact. The former nursery is warm, every weapon matches a custody slip, and the heating plant can run without a sentry choosing which household receives fuel.

### fallout.event_log.weapons_in_nursery.family_registry_success

Source line: 8353.
Before: Household receipts made the nursery cache visible and shared.

After: Weapon custody slips made the nursery cache visible and shared.

### fallout.event_log.weapons_in_nursery.family_registry_partial

Source line: 8354.
Before: Household receipts left a private reserve behind the shelves.

After: Weapon custody slips left a private reserve behind the shelves.

### chaosx.fallout.161.t

Source line: 8399.
Before: The Well Ledger Comes Due

After: The Well Supply Review

### chaosx.event_name.672

Source line: 8426.
Before: The Harvest Ledger Answers

After: The Harvest Comes In

### chaosx.event_name.673

Source line: 8427.
Before: The Harvest Ledger Answers

After: The Harvest Comes In

### chaosx.fallout.670.d

Source line: 8432.
Before: The Food Compact's harvest ledger has reached the point where empty fields and empty shelters are competing for the same hands. The harvest state of [?fallout_event_dispatch_issued_target.GetName] still has a usable reserve, but Air Winter has narrowed the safe work window. A universal duty roster can spread the burden across households. Paid labor can protect skilled crews. A refugee work program can bring displaced families into supervised fields. Mechanized harvest can spare people by spending the power and support equipment that keep the machines alive.

After: The Food Compact needs the same hands to harvest the fields and keep the shelters running. The harvest state of [?fallout_event_dispatch_issued_target.GetName] still has a usable reserve, but Air Winter has narrowed the safe work window. A universal duty roster can spread the burden across households. Paid labor can protect skilled crews. A refugee work program can bring displaced families into supervised fields. Mechanized harvest can spare people by spending the power and support equipment that keep the machines alive.

### chaosx.fallout.672.t

Source line: 8441.
Before: The Harvest Ledger Answers

After: The Harvest Comes In

### chaosx.fallout.672.paid.success.d

Source line: 8445.
Before: The paid crews in [?fallout_event_dispatch_issued_target.GetName] held their tools through the cold shift. Their foremen protected the skilled work, the Food Compact received a reliable harvest, and the wider settlement accepted the wage ledger.

After: The paid crews in [?fallout_event_dispatch_issued_target.GetName] held their tools through the cold shift. Their foremen protected the skilled work, the Food Compact received a reliable harvest, and the wider settlement accepted the wage agreement.

### chaosx.fallout.672.paid.failure.d

Source line: 8447.
Before: The paid labor ledger in [?fallout_event_dispatch_issued_target.GetName] ran out before the field shelters could be staffed. The crews left the rows, the reserve fell, and the shortage cost lives.

After: The wage fund in [?fallout_event_dispatch_issued_target.GetName] ran out before the field shelters could be staffed. The crews left the rows, the reserve fell, and the shortage cost lives.

### chaosx.fallout.674.a.tt

Source line: 8461.
Before: Settle the harvest review, preserve its branch memory, and close the work ledger.

After: Settle the harvest review and retain the consequences of the chosen work policy.

### fallout.event_log.work_for_rations.detail.paid_labor_failure

Source line: 8469.
Before: The paid labor ledger failed before the selected state's field shelters could be staffed.

After: The wage fund failed before the selected state's field shelters could be staffed.

### chaosx.fallout.324.a.tt

Source line: 8492.
Before: Open the elevator under a public ration ledger. Costs Food and Scrap. A stable result expands grain capacity and lowers spoilage while making the store a civic institution.

After: Open the elevator under public ration rules. Costs Food and Scrap. A stable result expands grain capacity and lowers spoilage while making the store a civic institution.

### chaosx.fallout.326.t

Source line: 8499.
Before: The Hopper Ledger

After: The Hopper Supply

### chaosx.fallout.328.failure.d

Source line: 8517.
Before: The maintenance year found a broken seal, a missing clerk, and three claims on the last dry hopper. The elevator returns to guarded darkness, while the country carries a grain ledger that records who was left waiting.

After: The maintenance year found a broken seal, a missing clerk, and three claims on the last dry hopper. The elevator returns to guarded darkness, and families who waited for grain still have empty bowls.

### chaosx.fallout.328.a

Source line: 8518.
Before: Close the storehouse ledger

After: The storehouse review is finished.

### fallout.event_log.working_elevator.granary_partial

Source line: 8523.
Before: A public grain ledger reached the central shelters but not the frozen rail edge.

After: Public grain distribution reached the central shelters but not the frozen rail edge.

### fallout_working_elevator_granary_desc

Source line: 8538.
Before: A public ration ledger keeps the working elevator open to the settlement.

After: Public ration rules keep the working elevator open to the settlement.

### fallout_generic_civic_compact_desc

Source line: 8661.
Before: The civic route makes local councils answerable to the households that feed them. Elections return, though each ballot is tied to a shelter register and a water ledger.

After: The civic route makes local councils answerable to the households that feed them. Elections return, though each ballot is tied to a shelter register and a water schedule.

### fallout_generic_invite_neighbor_compacts_desc

Source line: 8687.
Before: The pact opens its radio ledger to nearby countries outside the old alliances. Members can ask for entry after weighing the same border and supply obligations.

After: The pact opens its radio network to nearby countries outside the old alliances. Members can ask for entry after weighing the same border and supply obligations.

### fallout_generic_survivor_federation_idea_desc

Source line: 8751.
Before: Shared patrol rules, repair obligations, and convoy ledgers let the member leagues defend their roads while consuming fewer scarce supplies.

After: Shared patrol rules, repair obligations, and convoy schedules let the member leagues defend their roads while consuming fewer scarce supplies.

### fallout_nzl_domestic_result_partial_text

Source line: 677.
Before: The principal towns receive their lots, but remote districts continue to trade outside the ledger. The reserve holds while the parliament negotiates another season.

After: The principal towns receive their lots, but remote districts continue to trade outside the official ration system. The reserve holds while the parliament negotiates another season.

### chaosx.fallout.558.success.d

Source line: 1063.
Before: The cordon officers marked a safe road through the ash and put a medic at each gate. Military traffic moves slowly, but it moves with a ledger. The government has kept the state connected without pretending the road is clean.

After: The cordon officers marked a safe road through the ash and put a medic at each gate. Military traffic moves slowly, but medics check every convoy. The government has kept the state connected without pretending the road is clean.

### chaosx.fallout.562.partial.d

Source line: 1073.
Before: The follow-up review closes one ledger and opens another. The state can repair a short road and shelter a few more families, yet the old ash line still dictates where the government can promise help.

After: The follow-up confirms that the inner road can reopen. The state can repair a short road and shelter a few more families, yet the old ash line still dictates where the government can promise help.

### fallout.event_log.ashline_firebreak.detail.callback_partial

Source line: 1089.
Before: The next ash season closed one ledger while leaving the outer road exposed.

After: The next ash season reopened the inner road while leaving the outer road exposed.

### chaosx.fallout.312.cooperative.partial.d

Source line: 1176.
Before: The cooperative crews keep their own rooms alive, yet their standards do not match. Water arrives on time in some districts and late in others. The shared ledger survives, though the grid now speaks in local accents.

After: The cooperative crews keep their own rooms alive, yet their standards do not match. Water arrives on time in some districts and late in others. Crews still share repairs, but each district runs its own circuits.

### chaosx.fallout.312.cooperative.failure.d

Source line: 1177.
Before: Two crews close the same line from opposite ends. The surge kills tools and starts a fight over whose ledger was correct. The settlement keeps a few lamps by cutting the promise of a common network down to a handful of rooms.

After: Two crews close the same line from opposite ends. The surge kills tools and starts a fight over whose switching instructions were correct. The settlement keeps a few lamps by cutting the promise of a common network down to a handful of rooms.

### chaosx.fallout.314.partial.d

Source line: 1188.
Before: The follow-up finds a network that works when people remember one another. Careful district records sit beside unrecorded loans of spare parts. The settlement can plan its next expansion, but gaps in the ledger still leave parts of the grid uncertain.

After: The follow-up finds a network that works when people remember one another. Careful district records sit beside unrecorded loans of spare parts. The settlement can plan its next expansion, but missing repair notes still leave parts of the grid uncertain.

### chaosx.fallout.770.rescue_articles.failure.d

Source line: 1468.
Before: The articles broke over who could speak for the refugee boats. The council kept the ledger, yet every captain left with a different promise about fuel and landing space.

After: The articles broke over who could speak for the refugee boats. The council kept its harbour roll, yet every captain left with a different promise about fuel and landing space.

### chaosx.fallout.772.success.d

Source line: 1481.
Before: The delayed review finds a port that can keep names, fuel, and rescue duty in one ledger. Captains accept the articles, families receive predictable berths, and the West African Port Confederacies have a law that can travel with a boat.

After: The delayed review finds a port that can assign berths, fuel, and rescue duties under one law. Captains accept the articles, families receive predictable berths, and the West African Port Confederacies have a law that can travel with a boat.

### chaosx.fallout.438.grant_citizenship.success.d

Source line: 1535.
Before: The clerk reads the names beside the ration roll and asks each child to choose the spelling used in the new ledger. The town gives them work papers, school benches, and the right to mourn in public. They are no longer guests waiting for a border that may never open.

After: The clerk reads the names beside the ration roll and asks each child to choose the spelling used in the citizen roll. The town gives them work papers, school benches, and the right to mourn in public. They are no longer guests waiting for a border that may never open.

### chaosx.fallout.735.local.failure.d

Source line: 1599.
Before: The ward boards split over medicine, recognition, and whose children count as local. The central office kept the final seal, while every ward learned that autonomy without a shared ledger can create smaller cordons.

After: The ward boards split over medicine, recognition, and whose children count as local. The central office kept the final seal, while every ward learned that autonomy without common admission rules can create smaller cordons.

### chaosx.fallout.721.standard.failure.d

Source line: 1735.
Before: The shared seal arrives before the ledgers agree. The eastern road closes for a week, the clinic loses its final reserve of paper, and the certificate is treated as another name for delay.

After: The shared seal arrives before the clinics agree on the checks. The eastern road closes for a week, the clinic loses its final reserve of paper, and the certificate is treated as another name for delay.

### fallout.event_log.clean_certificate.detail.regional_standard_failure

Source line: 1761.
Before: The shared seal arrived before the ledgers agreed and closed the eastern road.

After: The shared seal arrived before the clinics agreed on the checks and closed the eastern road.

### chaosx.fallout.880.b.tt

Source line: 1781.
Before: Spend Scrap 2, Power 2, and Recognition 3 to place care budgets under a ward ballot with a public ledger.

After: Spend Scrap 2, Power 2, and Recognition 3 to place care budgets under a ward ballot with spending open to public scrutiny.

### fallout.event_log.clinic_or_council.detail.medical_oversight_partial

Source line: 1815.
Before: The central clinic held one ledger while outlying pumps kept older forms.

After: The central clinic kept a single medicine tally while outlying pumps kept older forms.

### chaosx.fallout.1046.mixed_assembly.failure.d

Source line: 1865.
Before: The mixed assembly spends its first meetings on who may sit near the ledger. The river delegates leave, the hill guardian seals the archive, and the foreign witness finds that a wide table can still have no public authority.

After: The mixed assembly spends its first meetings on who may control the shelter allotments. The river delegates leave, the hill guardian seals the archive, and the foreign witness finds that a wide table can still have no public authority.

### chaosx.fallout.391.success.d

Source line: 1940.
Before: Months later, the clinic has a second test bench and a named supplier. The freight ward still remembers the first fever, but the ledger now travels with every convoy and the apothecaries can refuse a box without closing the door.

After: Months later, the clinic has a second test bench and a named supplier. The freight ward still remembers the first fever, but medicine delivery notes now travel with every convoy and the apothecaries can refuse a box without closing the door.

### chaosx.fallout.391.partial.d

Source line: 1941.
Before: The review keeps the clinic open, though the supplier's name remains a disputed mark in the ledger. Families accept the medicine when a nurse signs for it and refuse it when a guard does.

After: The review keeps the clinic open, though the clinic still cannot verify the supplier. Families accept the medicine when a nurse signs for it and refuse it when a guard does.

### chaosx.fallout.572.desc

Source line: 1967.
Before: In the North American grain belt, three rural districts have kept enough food, tools, and watchmen to send a delegation to [?fallout_event_572_target_state_id.GetName]. The host ground has a repair shed, a cleared field, and a ledger of families who still owe one another a season. The fair can become a civic exhibition, a careful exchange, a disciplined muster, or a memorial gathering. Each choice spends stores before the first stall opens.

After: In the North American grain belt, three rural districts have kept enough food, tools, and watchmen to send a delegation to [?fallout_event_572_target_state_id.GetName]. The host ground has a repair shed, a cleared field, and a roll of families who still owe one another a season of work. The fair can become a civic exhibition, a careful exchange, a disciplined muster, or a memorial gathering. Each choice spends stores before the first stall opens.

### chaosx.fallout.338.d

Source line: 2024.
Before: The eastern skyline is a dark line of empty towers around a city that no longer answers radio calls. A reconnaissance team has found a road through the ash and asks who may enter, who may profit, and who will answer for the bodies left behind. The sealed warehouse route gave us a ledger, but this city will test whether our laws reach beyond the fence.

After: The eastern skyline is a dark line of empty towers around a city that no longer answers radio calls. A reconnaissance team has found a road through the ash and asks who may enter, who may profit, and who will answer for the bodies left behind. The sealed warehouse taught us to control salvage, but this city will test whether our laws reach beyond the fence.

### chaosx.fallout.487.call_desert_technicians.failure.d

Source line: 2091.
Before: The convoy was stopped beyond the salt flats. Its credit remains on the ledger, while the plant loses another filter and the neighboring government calls the delay a breach.

After: The convoy was stopped beyond the salt flats. Its promised payment remains outstanding, while the plant loses another filter and the neighboring government calls the delay a breach.

### chaosx.fallout.230.d

Source line: 2193.
Before: A convoy from [?fallout_event_230_source_state_id.GetName] has reached the doors of [?fallout_event_230_destination_state_id.GetName]. The source shelter is carrying a heavier Air Winter exposure, while the receiving rooms still have a measured reserve. [ROOT.GetAirWinterGovernmentAuthority] must decide who enters, how the ledger will be read, and what the destination can carry through the next twelve days.

After: A convoy from [?fallout_event_230_source_state_id.GetName] has reached the doors of [?fallout_event_230_destination_state_id.GetName]. The source shelter is carrying a heavier Air Winter exposure, while the receiving rooms still have a measured reserve. [ROOT.GetAirWinterGovernmentAuthority] must decide who enters, which households have priority, and what the destination can carry through the next twelve days.

### chaosx.fallout.232.partial.d

Source line: 2205.
Before: Most of the family convoy entered [?fallout_event_230_destination_state_id.GetName], although the final rooms filled before every name was checked. The destination kept a narrow reserve and the missing households remain a visible debt in the ledger.

After: Most of the family convoy entered [?fallout_event_230_destination_state_id.GetName], although the final rooms filled before every name was checked. The destination kept a narrow reserve and the households left outside still need rooms.

### chaosx.fallout.445.resettle_refugee_families.failure.d

Source line: 2272.
Before: The houses are assigned before the well is secure. Families leave in the first ash wind, and the ledger becomes a list of promises that the village could not keep.

After: The houses are assigned before the well is secure. Families leave in the first ash wind, and the village cannot give them the homes it promised.

### chaosx.fallout.796.opening.d

Source line: 2380.
Before: The Manchurian Reactor Keeps still has a live turbine hall, a public power board, and enough technicians to keep one district warm. The engineers say the Reactor Without a Country memory gives them the only honest claim to rule. Families, clerks, and the garrison have brought their own ledgers to the same table. Four constitutional routes are possible before the next ash season closes the doors.

After: The Manchurian Reactor Keeps still has a live turbine hall, a public power board, and enough technicians to keep one district warm. The engineers say the Reactor Without a Country memory gives them the only honest claim to rule. Families, clerks, and the garrison have brought competing claims to the same table. Four constitutional routes are possible before the next ash season closes the doors.

### chaosx.fallout.800.partial.d

Source line: 2407.
Before: The grid survived the first winter, but its ledgers still depend on one exhausted crew. The reactor keep can keep the lights on while it decides whether trust comes from elections, inspection, or command.

After: The grid survived the first winter, but its power schedule still depends on one exhausted crew. The reactor keep can keep the lights on while it decides whether trust comes from elections, inspection, or command.

### fallout.event_log.engineer_franchise.detail.callback_partial

Source line: 2430.
Before: The grid survived while its ledgers still depended on one exhausted crew.

After: The grid survived while its power schedule still depended on one exhausted crew.

### chaosx.fallout.49.motor_failure.d

Source line: 2657.
Before: Cold rain cut the marked road into [air_winter_event_state.GetName] and disabled tankers blocked the remaining lane. Uncovered loads fouled in roadside runoff while displaced families crowded the last municipal taps. [ROOT.GetAirWinterGovernmentOfficial] must recover the engines, close the route, and enter the dead in the city ledger.

After: Cold rain cut the marked road into [air_winter_event_state.GetName] and disabled tankers blocked the remaining lane. Uncovered loads fouled in roadside runoff while displaced families crowded the last municipal taps. [ROOT.GetAirWinterGovernmentOfficial] must recover the engines, close the route, and identify the people who died.

### chaosx.fallout.833.t

Source line: 3151.
Before: The Ledger Opens

After: The Calculation Inquiry

### chaosx.fallout.833.public_inquiry.partial.d

Source line: 3153.
Before: The public ledger reached most repair councils, but one damaged transformer forced the inquiry to rely on a handwritten night roster. The Technate gained witnesses and lost time, leaving the next cold shift exposed to another narrow margin.

After: The inquiry's findings reached most repair councils, but one damaged transformer forced the inquiry to rely on a handwritten night roster. The Technate gained witnesses and lost time, leaving the next cold shift exposed to another narrow margin.

### chaosx.fallout.833.hide_calculation.success.d

Source line: 3155.
Before: The archive kept the error out of the public ledger while the reactor staff replaced the damaged relay. The Manchurian Reactor Keeps kept its export charter intact, yet the eastern councils will receive only a sealed assurance that the next model is safe.

After: The archive concealed the error from the public while the reactor staff replaced the damaged relay. The Manchurian Reactor Keeps kept its export charter intact, yet the eastern councils will receive only a sealed assurance that the next model is safe.

### chaosx.fallout.480.import_seed.success.d

Source line: 3289.
Before: The eastern convoy arrived under a written debt and delivered seed suited to short summers. The new ledger names both countries, and the valley receives enough grain to keep the next planting honest.

After: The eastern convoy arrived under a written debt and delivered seed suited to short summers. Both countries have signed the seed agreement, and the valley receives enough grain to keep the next planting honest.

### chaosx.fallout.480.underground_reserve.success.d

Source line: 3292.
Before: The tunnel crews sealed the reserve behind the old rail gate. Access passes through a public ledger, so the reserve strengthens local trust without emptying the surface granary.

After: The tunnel crews sealed the reserve behind the old rail gate. A public ration book governs access, so the reserve strengthens local trust without emptying the surface granary.

### fallout.event_log.false_spring_losses.import_seed_failure

Source line: 3313.
Before: Wet imported seed failed, but the convoy debt remained on the ledger.

After: Wet imported seed failed, but the convoy debt remained unpaid.

### chaosx.fallout.972.adoption_network.failure.d

Source line: 3347.
Before: The houses open faster than their witnesses can agree. A child is carried between two ledgers, a guardian waits for a missing seal, and the Basin learns that a kind institution can still become a queue with no answer.

After: The houses open faster than their witnesses can agree. Two adoption houses dispute who should care for a child, a guardian waits for a missing seal, and the Basin learns that a kind institution can still become a queue with no answer.

### chaosx.fallout.972.no_intervention.failure.d

Source line: 3350.
Before: The Basin leaves the ledger blank and calls the silence freedom. When food, medicine, and shelter run short, no household can prove its need without starting the argument the council hoped to avoid.

After: The Basin refuses to assess household needs. When food, medicine, and shelter run short, no household can prove its need without starting the argument the council hoped to avoid.

### fallout.event_log.fertility_question.detail.no_intervention_failure

Source line: 3376.
Before: A blank ledger left households unable to prove urgent need.

After: The lack of a needs assessment left households unable to prove urgent need.

### fallout.event_log.fertility_question.detail.callback_failure

Source line: 3379.
Before: Duplicate ledgers and missing guardians broke trust in every office.

After: Conflicting household rolls and missing guardians broke trust in every office.

### chaosx.fallout.256.d

Source line: 3397.
Before: The dormitory in [?fallout_event_dispatch_issued_target.GetName] has filled beyond its winter register. Coughing has moved from the clinic beds to the cooking room, and the attendants have begun to mark doors with charcoal because the medicine shelf no longer matches the shelter list. [ROOT.GetAirWinterGovernmentOfficial] can quarantine the room, split the bunks, treat people in the open, or keep the fever out of the public ledger. Every choice leaves a record in the state.

After: The dormitory in [?fallout_event_dispatch_issued_target.GetName] has filled beyond its winter register. Coughing has moved from the clinic beds to the cooking room, and the attendants have begun to mark doors with charcoal because the medicine shelf no longer matches the shelter list. [ROOT.GetAirWinterGovernmentOfficial] can quarantine the room, split the bunks, treat people in the open, or hide the fever from the public. Every choice leaves a record in the state.

### chaosx.fallout.261.partial.d

Source line: 3426.
Before: The concealed ward in [?fallout_event_256_state_id.GetName] survived the first review, but the fever did not stay inside the marked rooms. The public ledger remains incomplete, and the next attendants will inherit a shelter with less trust and a rising disease pressure.

After: The concealed ward in [?fallout_event_256_state_id.GetName] survived the first review, but the fever did not stay inside the marked rooms. The public still does not know how far the fever has spread, and the next attendants will inherit a shelter with less trust and a rising disease pressure.

### fallout.event_log.fever_dormitory.detail.conceal_partial

Source line: 3449.
Before: The concealed ward survived the first review but left an incomplete public ledger.

After: The concealed ward survived the first review but left the public unaware of how far the fever had spread.

### chaosx.fallout.222.a.tt

Source line: 3495.
Before: Resolve the household-ledger report and schedule a public filter review in §Y[?constant:fallout_event_217_timing.callback_delay_days|0] days§!.

After: Resolve the household filter allocation and schedule a public filter review in §Y[?constant:fallout_event_217_timing.callback_delay_days|0] days§!.

### chaosx.fallout.284.campaign.success.d

Source line: 3683.
Before: The civic campaign turned one clinic record into a promise that the country can staff. Food stewards, power crews, and new volunteers joined the ledger, giving the next generation a visible place in the work.

After: The civic campaign turned one clinic record into a promise that the country can staff. Food stewards, power crews, and new volunteers joined the clinic's work roster, giving the next generation a visible place in the work.

### chaosx.fallout.286.t

Source line: 3692.
Before: The Child Returns to the Ledger

After: The Child Returns to the Clinic

### chaosx.fallout.286.partial.d

Source line: 3694.
Before: The follow-up found a working clinic in the capital and an uncertain route beyond it. The child's name remains in the ledger, while medicine and shelter still decide which families can receive the same promise.

After: The follow-up found a working clinic in the capital and an uncertain route beyond it. The capital clinic still cares for the child, while medicine and shelter still decide which families can receive the same promise.

### fallout.event_log.first_safe_birth.detail.callback_partial

Source line: 3714.
Before: The follow-up kept the child's name in the capital ledger while medicine and shelter remained uneven.

After: The follow-up kept the child under the capital clinic's care while medicine and shelter remained uneven.

### chaosx.fallout.824.opening.d

Source line: 3983.
Before: The Patent After the End left the Manchurian Reactor Keeps with enough working cable to light only a few districts beyond its own walls. East Asian delegates have submitted competing ledgers for equal distribution, workshop priority, domestic supply, and a protected military corridor.

After: The Patent After the End left the Manchurian Reactor Keeps with enough working cable to light only a few districts beyond its own walls. East Asian delegates have submitted competing power plans for equal distribution, workshop priority, domestic supply, and a protected military corridor.

### chaosx.fallout.786.partial.d

Source line: 4082.
Before: The harbor survives as a useful place, but its government still shares one ledger with a rival council. The next convoy can dock while the claim remains contested.

After: The harbor survives as a useful place, but its government still shares harbour authority with a rival council. The next convoy can dock while the claim remains contested.

### fallout.event_log.harbor_without_city.detail.callback_partial

Source line: 4105.
Before: The harbor remained useful while a rival council contested one shared ledger.

After: The harbor remained useful while a rival council contested the shared harbour authority.

### chaosx.fallout.494.boil_and_filter.success.d

Source line: 4286.
Before: The boiler held through the blue dark. Crews chipped ash from the intake, layered fresh charcoal into the filter drums, and filled the clinic cistern before the settlement tanks. The water board has a ledger for another frozen night.

After: The boiler held through the blue dark. Crews chipped ash from the intake, layered fresh charcoal into the filter drums, and filled the clinic cistern before the settlement tanks. The water board can supply water through another frozen night.

### chaosx.fallout.100.d

Source line: 4366.
Before: The inventory clerks have counted the sealed grain, dried beans, and fuel for the pressure cookers. The figures do not cover a month. District delegates want a public ledger. Households with private cellars want silence. The guard commander has already marked three warehouses as disputed.

After: The inventory clerks have counted the sealed grain, dried beans, and fuel for the pressure cookers. The figures do not cover a month. District delegates want the food count made public. Households with private cellars want silence. The guard commander has already marked three warehouses as disputed.

### chaosx.fallout.100.b.tt

Source line: 4370.
Before: Keep the public ledger narrow and protect private stores, even if district officials begin to doubt the count.

After: Limit the published food count and protect private stores, even if district officials begin to doubt the count.

### chaosx.fallout.102.success.d

Source line: 4375.
Before: The public ledger survives the first audit. Grain clerks in the rail district now issue the same measure, and the guard has stopped marking private cellars as enemy property. The ration law is severe, but people can plan around it.

After: The public ration rules survive the first audit. Grain clerks in the rail district now issue the same measure, and the guard has stopped marking private cellars as enemy property. The ration law is severe, but people can plan around it.

### chaosx.fallout.102.partial.d

Source line: 4376.
Before: The ledger is posted, but two warehouse districts report missing sacks before the second count. The ration law is understood, although every late delivery is now treated as proof of a hidden reserve.

After: The food count is posted, but two warehouse districts report missing sacks before the second count. The ration law is understood, although every late delivery is now treated as proof of a hidden reserve.

### chaosx.fallout.103.success.d

Source line: 4382.
Before: Household committees keep the private caches quiet long enough to make a second harvest plan. The central ledger is incomplete, but the neighborhoods that hold food now have a reason to keep their doors open to the ration teams.

After: Household committees keep the private caches quiet long enough to make a second harvest plan. The central office still cannot count all the food, but the neighborhoods that hold food now have a reason to keep their doors open to the ration teams.

### chaosx.fallout.105.public.d

Source line: 4396.
Before: The first ration review compares the public ledger with the kitchens that actually served food. The measure is still harsh, but the districts know which office owns the missing sacks and which convoy is expected next.

After: The first ration review compares the published food count with the kitchens that actually served food. The measure is still harsh, but the districts know which office owns the missing sacks and which convoy is expected next.

### chaosx.fallout.112.success.d

Source line: 4442.
Before: The second review closes around a written water compact. The intake authority, clinic board, and upstream crews now share a repair calendar, and foreign observers have a reason to return without taking the ledger away.

After: The second review closes around a written water compact. The intake authority, clinic board, and upstream crews now share a repair calendar, and foreign observers have a reason to return without taking control of the intake.

### fallout.event_log.river_intake.detail.ration_partial

Source line: 4471.
Before: Filters caught the worst ash, but the replacement ledger began to divide districts by access.

After: Filters caught the worst ash, but the filter replacement schedule began to divide districts by access.

### fallout_food_public_ration_law_desc

Source line: 4563.
Before: A visible ledger and measured ration law keep the kitchens aligned, but every short delivery damages trust.

After: A public food count and measured ration law keep the kitchens aligned, but every short delivery damages trust.

### fallout_food_household_cache_network_desc

Source line: 4565.
Before: Private cellars and neighborhood committees keep food moving outside the central ledger.

After: Private cellars and neighborhood committees keep food moving outside the central ration system.

### fallout_event_100_ration_law_desc

Source line: 4587.
Before: Clerks and kitchen captains will compare the public ledger, filter stock, and the food actually served. The review takes three weeks and consumes part of the reserve before it can restore order.

After: Clerks and kitchen captains will compare the published food count, filter stock, and the food actually served. The review takes three weeks and consumes part of the reserve before it can restore order.

### chaosx.fallout.807.failure.d

Source line: 4782.
Before: The first-winter review found a power board that had spent its reserve without earning a public schedule. The reactor keep has lower supply, damaged infrastructure, and four sectors prepared to keep their own ledgers apart from the technate.

After: The first-winter review found a power board that had spent its reserve without earning a public schedule. The reactor keep has lower supply, damaged infrastructure, and four sectors prepared to allocate their own reserves without the technate.

### fallout.event_log.load_shedding.detail.callback_failure

Source line: 4805.
Before: The first-winter review found a spent reserve and four sector ledgers outside the technate.

After: The first-winter review found a spent reserve and four sectors allocating reserves without the technate.

### chaosx.fallout.847.human_review.failure.d

Source line: 4842.
Before: The review dissolved into a fight between senior engineers and clinic crews over which ledger counted as current. The machine was silenced, but the Technate lost the repair window and left the eastern councils with no common schedule.

After: The review dissolved into a fight between senior engineers and clinic crews over which power schedule was current. The machine was silenced, but the Technate lost the repair window and left the eastern councils with no common schedule.

### chaosx.fallout.347.improvise.success.d

Source line: 4908.
Before: The local crew used a boiler diagram from the maintenance archive and found a safe shortcut. The station gives the settlement a narrow band of warmth, and the improvised notes are copied into the ledger.

After: The local crew used a boiler diagram from the maintenance archive and found a safe shortcut. The station gives the settlement a narrow band of warmth, and the improvised notes are added to the maintenance manual.

### chaosx.fallout.384.failure.d

Source line: 4976.
Before: The review found broken scales, a damaged supply node, and no merchant willing to sign the old ledger. The viaduct remains a road, but its market memory closes with the last ration mark.

After: The review found broken scales, a damaged supply node, and no merchant willing to accept the old trading terms. The viaduct remains a road, but its market memory closes with the last ration mark.

### chaosx.fallout.889.separate_districts.failure.d

Source line: 5262.
Before: The district line becomes a wall without a gate. Residents wait on the wrong side of the pump road while clerks argue over which ledger can authorize a blanket, a crate, or a place to sleep.

After: The district line becomes a wall without a gate. Residents wait on the wrong side of the pump road while clerks argue over which office can authorize a blanket, a crate, or a place to sleep.

### fallout.event_log.mixed_settlement.detail.refuse_settlement_partial

Source line: 5293.
Before: Informal camps grew because the boundary rule had no auditable favors ledger.

After: Informal camps grew because the boundary rule had no way to challenge private favors.

### fallout.event_log.mixed_settlement.detail.callback_failure

Source line: 5297.
Before: Separate ledgers and missing permits broke the shared road.

After: Conflicting admission rules and missing permits broke the shared road.

### chaosx.fallout.763.medical_inspection.success.d

Source line: 5405.
Before: The inspection took place by consent, with Basin physicians and the envoy's own observers reading the same ledger. No one was detained, and both governments agreed that travel papers describe obligations rather than an imagined cure.

After: The inspection took place by consent, with Basin physicians and the envoy's own observers checking the same patient list. No one was detained, and both governments agreed that travel papers describe obligations rather than an imagined cure.

### chaosx.fallout.875.old_nationality.success.d

Source line: 5475.
Before: The council restored the old nationality on its ledgers, then added a Basin clause that limits inherited debts and military claims. The neighboring archive accepts the clause, so continuity becomes a negotiated tool rather than a demand for the past to return.

After: The council restored the old nationality on its citizenship rolls, then added a Basin clause that limits inherited debts and military claims. The neighboring archive accepts the clause, so continuity becomes a negotiated tool rather than a demand for the past to return.

### chaosx.fallout.271.success.d

Source line: 5542.
Before: The published register reached the shelter kitchens with names, districts, and the last verified household mark. Families can challenge an entry without reopening the entire ledger, and Recognition has begun to recover.

After: The published register reached the shelter kitchens with names, districts, and the last verified household mark. Families can challenge an entry without repeating the entire census, and Recognition has begun to recover.

### chaosx.fallout.274.partial.d

Source line: 5564.
Before: Local clerks reconciled the largest shelters and left the outlying roads unresolved. The central ledger has a usable spine, while Recognition remains uneven wherever the winter patrols cannot reach.

After: Local clerks reconciled the largest shelters and left the outlying roads unresolved. The central office can identify most shelter residents, while Recognition remains uneven wherever the winter patrols cannot reach.

### fallout.event_log.names_missing.detail.clerks_partial

Source line: 5588.
Before: Local clerks built a central ledger while leaving outlying roads unresolved.

After: Local clerks identified residents in the largest shelters while leaving outlying roads unresolved.

### fallout_names_missing_local_clerks_desc

Source line: 5598.
Before: Local clerks carry household sheets between shelters and return signed corrections to the central ledger.

After: Local clerks carry household sheets between shelters and return signed corrections to the central shelter roll.

### chaosx.fallout.581.public.partial.d

Source line: 5778.
Before: The public board opened the gates while two districts kept private ledgers. Water moves again as the first compact comes under dispute.

After: The public board opened the gates while two districts kept their water schedules private. Water moves again as the first compact comes under dispute.

### fallout_nile_pump_congress_partial_desc

Source line: 5823.
Before: A contested river compact keeps a reduced intake operating while local ledgers and delivery promises remain disputed.

After: A contested river compact keeps a reduced intake operating while local water schedules and delivery promises remain disputed.

### chaosx.fallout.586.d.tt

Source line: 5845.
Before: Spend [?constant:fallout_event_586_cost.consortium_fuel|0] Fuel, [?constant:fallout_event_586_cost.consortium_scrap|0] Scrap, [?constant:fallout_event_586_cost.consortium_power|0] Power, and [?constant:fallout_event_586_cost.consortium_recognition|0] Recognition. Outside standards and capital improve the route while dependency enters the ledger.

After: Spend [?constant:fallout_event_586_cost.consortium_fuel|0] Fuel, [?constant:fallout_event_586_cost.consortium_scrap|0] Scrap, [?constant:fallout_event_586_cost.consortium_power|0] Power, and [?constant:fallout_event_586_cost.consortium_recognition|0] Recognition. Outside standards and capital improve the route while the airfield becomes more dependent on outside support.

### chaosx.fallout.588.invalid.d

Source line: 5847.
Before: The runway changed hands before its first ledger could close. The old landing schedule is void, and the mechanics have carried the radio books into the hills.

After: The runway changed hands before the first landing review. The old landing schedule is void, and the mechanics have carried the radio books into the hills.

### chaosx.fallout.588.military.partial.d

Source line: 5852.
Before: Air command held the main runway, but two valley flights were cancelled under fire and weather. The strip remains open, though the officers and mechanics no longer share one ledger.

After: Air command held the main runway, but two valley flights were cancelled under fire and weather. The strip remains open, though the officers and mechanics no longer agree on a flight schedule.

### chaosx.fallout.1025.secret_retention.success.d

Source line: 5935.
Before: The sealed archive survives a guard rotation and protects the witnesses named in the first ledger. A small review cell still delivers medicine to the river wards, and the Basin records the seal as a temporary custody rule with a date for reopening.

After: The sealed archive survives a guard rotation and protects the witnesses named in the first patient list. A small review cell still delivers medicine to the river wards, and the Basin records the seal as a temporary custody rule with a date for reopening.

### chaosx.fallout.412.failure.d

Source line: 6132.
Before: The next bloom fails. The growers keep the ledger and bury the dead roots, while the state prepares for another hungry winter.

After: The next bloom fails. The growers keep the planting notes and bury the dead roots, while the state prepares for another hungry winter.

### fallout.event_log.orientation.detail.national_command_partial

Source line: 6170.
Before: Emergency command secured the fuel yards and one filter depot, while remote districts kept their own ledgers and questioned the order.

After: Emergency command secured the fuel yards and one filter depot, while remote districts kept control of their own stores and questioned the order.

### fallout.event_log.orientation.detail.government_division_partial

Source line: 6194.
Before: The divided government kept both offices open, but disputed jurisdiction left relief queues and security patrols answering to different ledgers.

After: The divided government kept both offices open, but disputed jurisdiction left relief queues and security patrols answering to different offices.

### fallout_orientation_closure_memory_rhine_dead_cities

Source line: 6462.
Before: Ruin permits, tram workshops, and salvage courts have opened their ledgers to the dead-city wards. Recovery crews can cross the Rhine industrial belt without bargaining for a new seal at every depot.

After: Ruin permits, tram workshops, and salvage courts now serve the dead-city wards. Recovery crews can cross the Rhine industrial belt without bargaining for a new seal at every depot.

### chaosx.fallout.68.evacuate.partial.d

Source line: 6520.
Before: The receiving shelters accepted only part of the planned movement before their doors reached capacity. The source and destination ledgers match the reduced request, exposure fell by the partial amount, and the [This.GetFalloutOrientationArchetypeName] must keep the remaining capital wards under a tighter watch.

After: The receiving shelters accepted only part of the planned movement before their doors reached capacity. Both shores confirm that fewer families moved, exposure fell by the partial amount, and the [This.GetFalloutOrientationArchetypeName] must keep the remaining capital wards under a tighter watch.

### chaosx.fallout.700.audit.partial.d

Source line: 6659.
Before: The audit found the worst duplicate passes, but fuel shortages left two outer wards on separate calendars. Disease control improved while the market learned to wait for the next gap in the ledger.

After: The audit found the worst duplicate passes, but fuel shortages left two outer wards on separate calendars. Disease control improved while the market learned to wait for the next lapse in permit checks.

### chaosx.fallout.700.delegate.failure.d

Source line: 6663.
Before: The councils turned the permit desks into rival courts. Names disappeared between ledgers, the appeal queue became another border, and the road no longer carried one meaning from the clinic to the outer farms.

After: The councils turned the permit desks into rival courts. The offices lost track of travelers, the appeal queue became another border, and the road no longer carried one meaning from the clinic to the outer farms.

### chaosx.fallout.702.t

Source line: 6669.
Before: The Ledger Returns

After: The Permit Review

### chaosx.fallout.791.amnesty.success.d

Source line: 6719.
Before: The crews surrendered their captured cargo and accepted a rescue oath. The harbor council grants them berths under named captains, and every future prize must enter the public ledger before it can feed a family.

After: The crews surrendered their captured cargo and accepted a rescue oath. The harbor council grants them berths under named captains, and every future prize must be declared to the harbour council before it can feed a family.

### chaosx.fallout.793.success.d

Source line: 6734.
Before: The sea road now has a named court, a rescue oath, and captains who know which ledger follows every prize. The harbor's authority reaches the water without pretending the old coast guard survived.

After: The sea road now has a named court, a rescue oath, and captains who know who must inspect every captured cargo. The harbor's authority reaches the water without pretending the old coast guard survived.

### chaosx.fallout.1051.a.tt

Source line: 6851.
Before: Spend Food 2, Medicine 1, and Recognition 1 to let the foreign team inspect the river clinic and issue return seals. Disease and exposure fall, but Basin guards lose cohesion while an outside witness gains access to the ledger.

After: Spend Food 2, Medicine 1, and Recognition 1 to let the foreign team inspect the river clinic and issue return seals. Disease and exposure fall, but Basin guards lose cohesion while an outside witness gains access to the patient list.

### chaosx.fallout.1053.seek_allies.partial.d

Source line: 6869.
Before: The courier finds a hill clinic willing to witness the ledger, but only one mule team reaches the bridge. Medicine arrives in marked crates while the neighboring government keeps its red cloth on family crossings.

After: The courier finds a hill clinic willing to witness the inspection agreement, but only one mule team reaches the bridge. Medicine arrives in marked crates while the neighboring government keeps its red cloth on family crossings.

### chaosx.fallout.625.success.d

Source line: 6998.
Before: Three hundred days later, the Eurasian route still has a timetable that survives changes in weather, government, and guard duty. Its ledgers are not identical, but the junction has become a place where settlements can ask for a train and expect an answer.

After: Three hundred days later, the Eurasian route still has a timetable that survives changes in weather, government, and guard duty. Depot schedules still differ, but the junction has become a place where settlements can ask for a train and expect an answer.

### fallout.event_log.rail_spine_vote.central_partial

Source line: 7019.
Before: The central board kept a reduced timetable alive while depots withheld parts of their ledgers.

After: The central board kept a reduced timetable alive while depots withheld parts of their supply schedules.

### chaosx.fallout.394.c

Source line: 7042.
Before: Purge the office and seize the ledger

After: Purge the office and seize the ration book

### chaosx.fallout.396.public_election.failure.d

Source line: 7051.
Before: The public count collapses when the last intact ledger is taken from the table. The queue leaves with empty hands, and the old official's silence becomes a new source of power.

After: The public count collapses when the last intact ration book is taken from the table. The queue leaves with empty hands, and the old official's silence becomes a new source of power.

### chaosx.fallout.396.purge.partial.d

Source line: 7056.
Before: The purge removes the official but leaves the clerks in place. The ledger is safe for a week, while every faction counts the names of those who were made afraid.

After: The purge removes the official but leaves the clerks in place. The ration book is safe for a week, while every faction counts the names of those who were made afraid.

### fallout.event_log.ration_thief_election.tribunal_partial

Source line: 7075.
Before: A tribunal found an altered ledger but no responsible hand.

After: A tribunal found an altered ration book but no responsible hand.

### chaosx.fallout.812.negotiate_safe_roster.partial.d

Source line: 7157.
Before: The operators signed a safe rotation for the day watch, while the night crew kept one refusal clause outside the public ledger. The reactor stayed online with a narrow reserve, and the East Asian rail shelters now expect the next shift to be negotiated in daylight.

After: The operators signed a safe rotation for the day watch, while the night crew withheld one refusal clause from the published agreement. The reactor stayed online with a narrow reserve, and the East Asian rail shelters now expect the next shift to be negotiated in daylight.

### fallout.event_log.reactor_shift.detail.negotiate_safe_roster_partial

Source line: 7183.
Before: The day roster held while the night crew kept one refusal clause outside the ledger.

After: The day roster held while the night crew withheld one refusal clause from the published agreement.

### chaosx.fallout.368.joint_authority.success.d

Source line: 7225.
Before: The three claimants signed one cooling schedule and accepted a public ledger. The reactor now feeds clinics and workshops without giving any faction a private switch. The first joint board has become a local successor institution.

After: The three claimants signed one cooling schedule and agreed to publish power allocations. The reactor now feeds clinics and workshops without giving any faction a private switch. The first joint board has become a local successor institution.

### chaosx.fallout.368.engineer_protectorate.partial.d

Source line: 7232.
Before: The engineers kept the core below danger but reserved the best parts for their own service tunnels. Power improved, while the public ledger grew thinner. The protectorate works because no one else can yet replace it.

After: The engineers kept the core below danger but reserved the best parts for their own service tunnels. Power improved, while the public received less information about power allocations. The protectorate works because no one else can yet replace it.

### chaosx.fallout.368.permanent_shutdown.partial.d

Source line: 7235.
Before: The core is cold, but the spent fuel vault still needs watch rotations. Exposure falls slowly and the region must import power for another winter. The shutdown protects the next settlement only if the guards keep their ledger.

After: The core is cold, but the spent fuel vault still needs watch rotations. Exposure falls slowly and the region must import power for another winter. The shutdown protects the next settlement only if the guards follow the watch schedule.

### fallout.event_log.reactor_without_a_country.callback_failure

Source line: 7263.
Before: Closed the reactor after a broken ledger

After: Closed the reactor after conflicting fuel figures

### chaosx.fallout.417.quarantine_train.partial.d

Source line: 7296.
Before: The fever stays inside the cars, but the cordon consumes the medicine reserve. The town accepts the ledger, yet families wait for a citizenship decision that no doctor can make.

After: The fever stays inside the cars, but the cordon consumes the medicine reserve. The town accepts the patient list, yet families wait for a citizenship decision that no doctor can make.

### fallout.event_log.refugee_train.callback_success

Source line: 7331.
Before: A year later the arrivals had homes, work, and a place in the public ledger.

After: A year later the arrivals had homes, work, and citizenship.

### fallout.event_log.refugee_train_bilateral.detail.unknown

Source line: 7352.
Before: The paired rail settlement left a memory in the country ledger, but its recorded choice is no longer available.

After: The paired rail settlement left a lasting mark on the country, but its recorded choice is no longer available.

### chaosx.fallout.758.failure.d

Source line: 7386.
Before: The delayed review finds a corridor of closed ledgers and exhausted escorts. The Quarantine government keeps the checkpoint, while Ash Ward clinics rebuild their schedules around the routes that no longer ask permission.

After: The delayed review finds a corridor of unshared patient lists and exhausted escorts. The Quarantine government keeps the checkpoint, while Ash Ward clinics rebuild their schedules around the routes that no longer ask permission.

### fallout.event_log.regional_health_compact.detail.callback_failure

Source line: 7416.
Before: The delayed review left the councils with closed ledgers and separate routes.

After: The delayed review left the councils with unshared patient lists and separate routes.

### chaosx.fallout.712.d

Source line: 7495.
Before: A fever has returned to Ash Ward Hospital after the last quarantine charter closed. North Gate clinic reports the same cough, yet its ward register carries no names from the first outbreak. The public health office must decide whether to close the district, send teams to the sickest blocks, ask a foreign convoy for medicine, or keep the outbreak out of the ledger.

After: A fever has returned to Ash Ward Hospital after the last quarantine charter closed. North Gate clinic reports the same cough, yet its ward register carries no names from the first outbreak. The public health office must decide whether to close the district, send teams to the sickest blocks, ask a foreign convoy for medicine, or hide the outbreak.

### chaosx.fallout.712.d.tt

Source line: 7503.
Before: Spend Medicine, Fuel, and Power to hide the fever from the public register while the ward clerks work at night. This can buy time for shelter and adaptation, but a discovered ledger damages public health and credibility.

After: Spend Medicine, Fuel, and Power to hide the fever from the public register while the ward clerks work at night. This can buy time for shelter and adaptation, but discovery of the concealed cases damages public health and credibility.

### chaosx.fallout.714.conceal.failure.d

Source line: 7516.
Before: The missing names were found in a clerk's stove after the fever reached the market shelter. The public health office lost its credibility, the clinics stopped sharing their ledgers, and the disease now travels faster than the quarantine order.

After: The missing names were found in a clerk's stove after the fever reached the market shelter. The public health office lost its credibility, the clinics stopped sharing patient lists, and the disease now travels faster than the quarantine order.

### chaosx.fallout.567.t

Source line: 7568.
Before: The River Ledger Returns

After: The River Ration Review

### chaosx.fallout.569.barge.failure.d

Source line: 7587.
Before: The review found two ledgers where the compact promised one. The upstream and downstream councils still exchange cargo, yet every exception now adds to the border tension recorded beside the river.

After: The review found conflicting cargo rules where the compact promised common terms. The upstream and downstream councils still exchange cargo, yet every exception now adds to the border tension recorded beside the river.

### fallout.event_log.river_ration_league.detail.callback_joint_failure

Source line: 7621.
Before: The joint river compact left two ledgers and a rising border tension.

After: The joint river compact left conflicting cargo rules and a rising border tension.

### chaosx.fallout.188.d

Source line: 7852.
Before: A cold store survived beneath the old freight embankment. Its drawers hold seed envelopes, field notes, and a ledger that names three districts which still have hands to plant. The archive cannot serve every claimant. The council must decide whether seed is a state reserve, a farmer's trust, a promise between countries, or a thing sold to whoever can pay.

After: A cold store survived beneath the old freight embankment. Its drawers hold seed envelopes, field notes, and a list of three districts which still have hands to plant. The archive cannot serve every claimant. The council must decide whether seed is a state reserve, a farmer's trust, a promise between countries, or a thing sold to whoever can pay.

### chaosx.fallout.190.success.d

Source line: 7862.
Before: The public reserve opened under a single ledger. Clerks from the rail cut counted every envelope, while the first protected plots received water before the next frost.

After: The public reserve opened under one allocation rule. Clerks from the rail cut counted every envelope, while the first protected plots received water before the next frost.

### chaosx.fallout.192.success.d

Source line: 7874.
Before: The first packets crossed the waterline with a clean-water convoy. The allied delegates recorded the exchange in both ledgers, giving the archive a route beyond one damaged country.

After: The first packets crossed the waterline with a clean-water convoy. The allied delegates confirmed the seed exchange for both countries, giving the archive a route beyond one damaged country.

### chaosx.fallout.192.partial.d

Source line: 7875.
Before: Some packets crossed, but the convoy arrived with less water than promised. The exchange remains visible in both ledgers and the next shipment will be argued over.

After: Some packets crossed, but the convoy arrived with less water than promised. The exchange has been confirmed by both countries and the next shipment will be argued over.

### chaosx.fallout.193.partial.d

Source line: 7881.
Before: The auction paid for part of the route, but the highest bids came from the same districts that already held the safest ground. The public ledger records both the food and the resentment.

After: The auction paid for part of the route, but the highest bids came from the same districts that already held the safest ground. Food reached the fields, but poorer districts resent their exclusion.

### fallout.event_log.seed_vault.detail.farmers_partial

Source line: 7897.
Before: Field cooperatives saved a narrow planting schedule and left an allotment grievance in the ledger.

After: Field cooperatives saved a narrow planting schedule and left growers disputing the allotments.

### chaosx.fallout.459.evacuate_low_ground.failure.d

Source line: 8096.
Before: The evacuation order arrived after the water reached the lower clinic. The carts bogged down, the wardens lost their ledger, and the low-ground families have no trusted route out.

After: The evacuation order arrived after the water reached the lower clinic. The carts bogged down, the wardens lost the evacuation roll, and the low-ground families have no trusted route out.

### chaosx.fallout.611.partial.d

Source line: 8226.
Before: The review board finds a shelter that functions by habit more than trust. The ledgers can be reconciled, but faction pressure remains visible in every queue.

After: The review board finds a shelter that functions by habit more than trust. The wards can agree on ration totals, but faction pressure remains visible in every queue.

### chaosx.fallout.155.success.d

Source line: 8379.
Before: The public queue in [?fallout_event_153_well_state_id.GetName] held through four days of frost. [ROOT.GetAirWinterGovernmentOfficial] published the draw times, clinic priority, and inspection marks, and [ROOT.GetAirWinterGovernmentAuthority] could answer each district with the same ledger. A follow-up review will test whether the arrangement survives ordinary distrust.

After: The public queue in [?fallout_event_153_well_state_id.GetName] held through four days of frost. [ROOT.GetAirWinterGovernmentOfficial] published the draw times, clinic priority, and inspection marks, and [ROOT.GetAirWinterGovernmentAuthority] could give every district the same water rules. A follow-up review will test whether the arrangement survives ordinary distrust.

### fallout.event_log.well_queue.detail.ration_failure

Source line: 8413.
Before: The filter room ran dry during the night shift, leaving spoiled barrels, late clinics, and deaths in its ledger.

After: The filter room ran dry during the night shift, leaving spoiled barrels, late clinics, and deaths from the shortage.

### chaosx.fallout.324.d

Source line: 8490.
Before: The grain elevator at the edge of the settlement has kept one sealed hopper through the ash years. Its rail spur is frozen, its ledger is written in three hands, and the first working streetlight has made the loading floor visible again. The country must decide whether the surviving store feeds a public granary, a guarded depot, a merchant exchange, or the families arriving from the road.

After: The grain elevator at the edge of the settlement has kept one sealed hopper through the ash years. Its rail spur is frozen, three clerks have counted its grain, and the first working streetlight has made the loading floor visible again. The country must decide whether the surviving store feeds a public granary, a guarded depot, a merchant exchange, or the families arriving from the road.

### chaosx.fallout.326.granary.partial.d

Source line: 8501.
Before: The public ledger reached the central shelters and stopped at the frozen rail spur. Grain moved under a clear rule near the elevator, while outer rooms still traded names and promises for a place in the next sack line.

After: Public grain distribution reached the central shelters and stopped at the frozen rail spur. Grain moved under a clear rule near the elevator, while outer rooms still traded names and promises for a place in the next sack line.

### chaosx.fallout.326.merchant.success.d

Source line: 8506.
Before: Licensed carriers turned the loading floor into a measured exchange. Their ledgers name the route, the price, and the share kept for the shelters, while unfamiliar carts bring grain from beyond the ash road without taking the whole public store as payment.

After: Licensed carriers turned the loading floor into a measured exchange. Their cargo accounts name the route, the price, and the share kept for the shelters, while unfamiliar carts bring grain from beyond the ash road without taking the whole public store as payment.

### chaosx.fallout.326.refugee.partial.d

Source line: 8510.
Before: The refugee queue received grain and clean water at the main door, while the last arrivals waited beside the frozen spur. Integration has a place on the ledger, though the town still argues over whether the shelter line or the road line came first.

After: The refugee queue received grain and clean water at the main door, while the last arrivals waited beside the frozen spur. New arrivals have a place in the ration queue, though the town still argues over whether the shelter line or the road line came first.

### fallout_working_elevator_maintained_desc

Source line: 8546.
Before: A maintenance year keeps seals, ledgers, and ration routes in working order.

After: A maintenance year keeps seals, grain tallies, and ration routes in working order.

### fallout_working_elevator_failed_desc

Source line: 8548.
Before: Spoiled stores and disputed ledgers have returned the elevator to guarded darkness.

After: Spoiled stores and disputed grain allocations have returned the elevator to guarded darkness.

### fallout_generic_open_the_regional_ledger_desc

Source line: 8695.
Before: Couriers compare river levels, passable roads, seed stores, harbours, and shelter capacity across the surrounding region. Their ledger gives each survivor government a programme tied to the land it actually holds.

After: Couriers compare river levels, passable roads, seed stores, harbours, and shelter capacity across the surrounding region. Their survey gives each survivor government a programme tied to the land it actually holds.

### fallout_generic_extend_the_regional_network_desc

Source line: 8779.
Before: The government commits crews to the regional programme recorded in its ledger. The result follows local conditions through relays, water councils, inland roads, seed banks, quarantine routes, river wards, water charters, or remote stations.

After: The government commits crews to the regional programme agreed by the regional councils. The result follows local conditions through relays, water councils, inland roads, seed banks, quarantine routes, river wards, water charters, or remote stations.

### chaosx.fallout.143.a

Source line: 695.
Before: Record the answer at Auckland Radio

After: Auckland Radio has heard their answer.

### chaosx.fallout.1032.a

Source line: 835.
Before: Record the Basin's chosen practice

After: The Basin has chosen its practice.

### chaosx.fallout.1034.a

Source line: 841.
Before: Close the adaptation record

After: The adaptation review is finished.

### chaosx.fallout.452.a

Source line: 1012.
Before: Record the field result

After: The trackers have brought their findings.

### chaosx.fallout.562.a

Source line: 1075.
Before: Record the next ash season

After: The next ash season has tested the road.

### chaosx.fallout.728.a

Source line: 1249.
Before: Record the crossing decision

After: East Gate has its instructions.

### chaosx.fallout.630.a

Source line: 1359.
Before: Record the first release

After: The first water release is complete.

### chaosx.fallout.770.a

Source line: 1478.
Before: Record the port's decision

After: The captains have their instructions.

### chaosx.fallout.772.a

Source line: 1484.
Before: Close the fleet record

After: The fleet has faced its first season.

### chaosx.fallout.438.a

Source line: 1547.
Before: Record the cohort and await the generation review

After: Give the children time to grow into their new homes.

### chaosx.fallout.440.a

Source line: 1553.
Before: Close the generation record

After: The children have returned for their review.

### chaosx.fallout.737.a

Source line: 1607.
Before: Close the generation record

After: We have heard the young people's verdict.

### chaosx.fallout.1039.a

Source line: 1667.
Before: Record the Basin's school settlement

After: The Basin's schools have their instructions.

### chaosx.fallout.1041.a

Source line: 1673.
Before: Close the generation record

After: The schools have faced their first generation review.

### chaosx.fallout.1046.a

Source line: 1869.
Before: Record the first civic mandate

After: The first council has its mandate.

### chaosx.fallout.1048.a

Source line: 1875.
Before: Close the first ballot record

After: The first council has faced its review.

### chaosx.fallout.389.a

Source line: 1937.
Before: Record the batch and face the next ward

After: Test the next medicine shipment.

### chaosx.fallout.574.a

Source line: 1989.
Before: Record the result and prepare the first seasonal review

After: Prepare for the fair's first seasonal review.

### chaosx.fallout.340.a

Source line: 2046.
Before: Record the first claim

After: The city salvage claim is settled.

### chaosx.fallout.342.a

Source line: 2052.
Before: Close the permit record

After: The ruin permits have faced their review.

### chaosx.fallout.489.a

Source line: 2105.
Before: Record the second shift

After: The second shift has brought its findings.

### chaosx.fallout.707.a

Source line: 2152.
Before: Record the hospital settlement

After: The hospital wards have their instructions.

### chaosx.fallout.235.a

Source line: 2228.
Before: Record the exclusion register

After: The shelter gates have their instructions.

### chaosx.fallout.445.a

Source line: 2282.
Before: Record the settlement and await the village review

After: Give the village time to settle.

### chaosx.fallout.298.a

Source line: 2335.
Before: Record the ward decision

After: The ward has its instructions.

### chaosx.fallout.300.a

Source line: 2342.
Before: Close the institution record

After: The ward has faced its first review.

### chaosx.fallout.798.a

Source line: 2403.
Before: Record the constitutional result

After: The reactor keep has chosen its government.

### chaosx.fallout.32.a

Source line: 2872.
Before: Record the smoke sickness and saved homes.

After: Count the homes saved and care for the sick.

### chaosx.fallout.833.a

Source line: 3164.
Before: Record the calculation decision

After: The engineers have their instructions.

### chaosx.fallout.695.a

Source line: 3241.
Before: Close the appeal record

After: The households have heard their appeal.

### chaosx.fallout.480.a

Source line: 3298.
Before: Record the frost decision

After: The growers have their instructions.

### chaosx.fallout.482.a

Source line: 3304.
Before: Close the frost record

After: The late frost review is finished.

### chaosx.fallout.227.a

Source line: 3501.
Before: Seal the audit record

After: The filter review is finished.

### chaosx.fallout.854.a

Source line: 3617.
Before: Record the regional standard

After: The workshops have their common standard.

### chaosx.fallout.284.a

Source line: 3689.
Before: Record the birth and wait for the follow-up

After: Give the child time to grow.

### chaosx.fallout.286.a

Source line: 3696.
Before: Close the generation-change record

After: The clinic has reviewed the child's care.

### chaosx.fallout.473.a

Source line: 3820.
Before: Record the measured hour

After: The crews know how long they can work.

### chaosx.fallout.475.a

Source line: 3826.
Before: Archive the exposure record

After: The exposure review is finished.

### chaosx.fallout.777.a

Source line: 3873.
Before: Close the convoy record

After: The convoy has completed its first review.

### chaosx.fallout.779.a

Source line: 3879.
Before: Close the route record

After: The convoy route has faced another season.

### chaosx.fallout.665.a

Source line: 3941.
Before: Record the winter decision

After: The winter response is settled.

### chaosx.fallout.826.a

Source line: 4006.
Before: Record the grid decision

After: The grid crews have their instructions.

### chaosx.fallout.784.a

Source line: 4078.
Before: Close the harbor record

After: The harbour has its instructions.

### chaosx.fallout.751.a

Source line: 4152.
Before: Record the regional review

After: The regional clinics have faced their review.

### chaosx.fallout.840.a

Source line: 4622.
Before: Record the citizenship settlement

After: The citizenship rules are settled.

### chaosx.fallout.245.a

Source line: 4685.
Before: Record the industrial settlement

After: The factory crews have their instructions.

### chaosx.fallout.248.a

Source line: 4706.
Before: Seal the technical record

After: The technical review is finished.

### chaosx.fallout.805.a

Source line: 4777.
Before: Record the circuit order

After: The circuits have their priorities.

### chaosx.fallout.847.a

Source line: 4846.
Before: Record the machine protocol settlement

After: The machine's recommendation has been judged.

### chaosx.fallout.347.a

Source line: 4917.
Before: Record the result and prepare the follow-up

After: Prepare the heating crews for their next review.

### chaosx.fallout.349.a

Source line: 4923.
Before: Close the maintenance record

After: The heating system has faced another winter.

### chaosx.fallout.508.a

Source line: 5023.
Before: Record the checkpoint decision

After: The checkpoint has its instructions.

### chaosx.fallout.618.a

Source line: 5081.
Before: Record the district review

After: The metro wards have faced their review.

### chaosx.fallout.637.a

Source line: 5338.
Before: Record the first pass count

After: The pass census is complete.

### chaosx.fallout.763.a

Source line: 5414.
Before: Record the envoy's answer

After: The envoy has our answer.

### chaosx.fallout.765.a

Source line: 5420.
Before: Close the envoy record

After: The border visit has faced its review.

### chaosx.fallout.875.a

Source line: 5484.
Before: Record the chosen name

After: The Basin has chosen its name.

### chaosx.fallout.877.a

Source line: 5490.
Before: Close the identity record

After: The neighbors have answered our chosen name.

### chaosx.fallout.651.a

Source line: 5721.
Before: Record the night

After: The new year has begun.

### chaosx.fallout.581.a

Source line: 5789.
Before: Record the first water tally

After: The pumps have made their first deliveries.

### chaosx.fallout.588.a

Source line: 5860.
Before: Record the airfield result

After: The runway has faced its first review.

### chaosx.fallout.1025.a

Source line: 5938.
Before: Record the Basin's finding

After: The Basin has heard the finding.

### chaosx.fallout.1027.a

Source line: 5944.
Before: Close the trial record

After: The doctor's case has faced its review.

### chaosx.fallout.744.a

Source line: 6067.
Before: Record the recovery review

After: The recovery crews have brought their findings.

### chaosx.fallout.410.a

Source line: 6127.
Before: Record the orchard decision

After: The growers have their instructions.

### chaosx.fallout.412.a

Source line: 6133.
Before: Close the orchard record

After: The orchard has faced another bloom.

### chaosx.fallout.80.a

Source line: 6544.
Before: Record the appointment.

After: The government has its official.

### chaosx.fallout.819.a

Source line: 6599.
Before: Record the patent result

After: The workshops have their design rules.

### chaosx.fallout.700.a

Source line: 6667.
Before: Record the movement ruling

After: The travelers have their ruling.

### chaosx.fallout.791.a

Source line: 6731.
Before: Close the sea-law record

After: The former raiders have their judgment.

### chaosx.fallout.868.a

Source line: 6800.
Before: Record the power register

After: The substations have their instructions.

### chaosx.fallout.1055.a

Source line: 6877.
Before: Close the quarantine record

After: The bridge has faced its quarantine review.

### chaosx.fallout.625.a

Source line: 7001.
Before: Record the route review

After: The rail route has faced another season.

### chaosx.fallout.396.a

Source line: 7061.
Before: Record the ruling and prepare the next audit

After: Prepare for the next ration inquiry.

### chaosx.fallout.501.a

Source line: 7113.
Before: Record the chemist's result

After: The chemist has brought the test results.

### chaosx.fallout.812.a

Source line: 7168.
Before: Record the reactor settlement

After: The reactor crews have their shift rules.

### chaosx.fallout.419.a

Source line: 7307.
Before: Close the refugee record

After: The families have faced their first settlement review.

### chaosx.fallout.756.a

Source line: 7381.
Before: Record the corridor decision

After: The clinics have their corridor rules.

### chaosx.fallout.758.a

Source line: 7387.
Before: Close the compact record

After: The health corridor has faced its first season.

### chaosx.fallout.861.a

Source line: 7446.
Before: Record the repair charter

After: The mechanics have their repair charter.

### chaosx.fallout.714.a

Source line: 7517.
Before: Record the ward decision

After: The wards have their treatment instructions.

### chaosx.fallout.293.a

Source line: 7667.
Before: Close the first cohort record

After: The first class has returned for its review.

### chaosx.fallout.424.a

Source line: 7999.
Before: Record the harbour compact

After: The harbour has its compact.

### chaosx.fallout.426.a

Source line: 8005.
Before: Close the harbour record

After: The ship has faced its first season ashore.

### chaosx.fallout.431.a

Source line: 8051.
Before: Record the specialists and await the review

After: Give the specialists time to teach their work.

### chaosx.fallout.433.a

Source line: 8057.
Before: Close the specialist record

After: The specialists have faced their first review.

### chaosx.fallout.185.a

Source line: 8175.
Before: Seal the medical ethics record

After: The doctor has reviewed the triage choices.

### chaosx.fallout.609.a

Source line: 8222.
Before: Record the settlement

After: The tunnel wards have their instructions.

### chaosx.fallout.672.a

Source line: 8454.
Before: Record the harvest result

After: The harvest crews have brought their results.

### chaosx.fallout.354.a

Source line: 8576.
Before: Record the protocol and prepare the next inspection

After: Prepare the next machine inspection.

### chaosx.fallout.356.a

Source line: 8582.
Before: Close the machine record

After: The machine has faced another inspection.

### chaosx.fallout.403.a

Source line: 8628.
Before: Record the date and plan its anniversary

After: Prepare to mark the first anniversary.

### chaosx.fallout.405.a

Source line: 8634.
Before: Close the calendar record

After: The anniversary review is finished.

### air_winter_response_priority_summary_locked_tt

Source line: 15.
Before: This row records the current emergency priority. Choose another state through Set the Emergency Priority.

After: The selected state has emergency priority. Choose another state through Set the Emergency Priority.

### air_winter_reception_state_summary_locked_tt

Source line: 26.
Before: This row records the current reception state. A reception state must remain under our ownership and control and must retain sufficient shelter and survival capacity.

After: The selected state receives evacuated families. A reception state must remain under our ownership and control and must retain sufficient shelter and survival capacity.

### air_winter_hold_abandonment_vote_effect_tt

Source line: 130.
Before: [FROM.GetName] records the abandonment vote. Its surviving authorities face the final choice over whether the state can still be held.

After: [FROM.GetName] holds the abandonment vote. Its surviving authorities face the final choice over whether the state can still be held.

### chaosx_air_treaty.15.a

Source line: 225.
Before: Let them choke on their own records.

After: Let them choke on their own lies.

### fallout_usa_repair_inland_depot_effect_tt

Source line: 786.
Before: The federal capital receives two infrastructure levels and one railway level. The logistics memory records a repaired inland depot belt.

After: The federal capital receives two infrastructure levels and one railway level. The inland depots can move supplies again.

### fallout_usa_muster_guard_compacts_effect_tt

Source line: 791.
Before: The federal guard gains a staffed reserve, 25 Army Experience, and 6 percent War Support. The security memory records the compact as enforceable.

After: The federal guard gains a staffed reserve, 25 Army Experience, and 6 percent War Support. The guard can enforce the compact.

### fallout_usa_ratify_lakes_charter_effect_tt

Source line: 796.
Before: The federal government gains 8 percent Stability and 75 Political Power. The diplomacy memory records a recognized Great Lakes charter.

After: The federal government gains 8 percent Stability and 75 Political Power. The Great Lakes charter gains recognition.

### fallout_usa_sweep_radio_dead_zones_effect_tt

Source line: 801.
Before: The radio service gains 10 Air Experience and 10 Command Power. The information memory records the dead zones as surveyed.

After: The radio service gains 10 Air Experience and 10 Command Power. The radio crews have surveyed the dead zones.

### fallout_usa_launch_federal_reconstruction_drive_effect_tt

Source line: 806.
Before: The federal capital receives one industrial complex and one infrastructure level. The reconstruction memory records a functioning federal works program.

After: The federal capital receives one industrial complex and one infrastructure level. The federal works program can keep rebuilding.

### chaosx.fallout.1034.a.tt

Source line: 842.
Before: Apply the delayed review result, record the final cause memory, release the ward and witness reservations, and close The Adaptation Rite chain.

After: The Adaptation Rite review ends. The wards and witnesses can take on other duties.

### chaosx.fallout.538.a.tt

Source line: 912.
Before: Seal the cause record and close the delayed reviews.

After: The delayed ammunition reviews end.

### chaosx.fallout.166.a.tt

Source line: 948.
Before: Resolve the kitchen feed result, preserve its record, and schedule a first-harvest review in §Y[?constant:fallout_event_164_timing.callback_delay_days|0] days§!.

After: Resolve the kitchen feed result and schedule a first-harvest review in §Y[?constant:fallout_event_164_timing.callback_delay_days|0] days§!.

### chaosx.fallout.167.a.tt

Source line: 955.
Before: Resolve the breeding result, preserve its record, and schedule the first-harvest review.

After: Resolve the breeding result and schedule the first-harvest review.

### chaosx.fallout.168.a.tt

Source line: 962.
Before: Resolve the regional feed result, preserve its record, and schedule the first-harvest review.

After: Resolve the regional feed result and schedule the first-harvest review.

### chaosx.fallout.204.e.tt

Source line: 1104.
Before: Recognition will be spent to send samples to partner growers. A delayed inspection will record whether trust brings a stable cultivar home.

After: Recognition will be spent to send samples to partner growers. A delayed inspection will test whether trust brings a stable cultivar home.

### chaosx.fallout.208.a.tt

Source line: 1122.
Before: The follow-up will record whether isolation produced a clean line or only delayed the crop warning.

After: The follow-up will test whether isolation produced a clean line or only delayed the crop warning.

### chaosx.fallout.312.a.tt

Source line: 1185.
Before: Record the grid policy, apply its immediate result, and begin the 270-day maintenance follow-up.

After: The grid policy takes effect. A maintenance review follows after 270 days.

### chaosx.fallout.314.a.tt

Source line: 1191.
Before: Conclude the maintenance review and preserve the grid's lasting record.

After: The grid maintenance review ends.

### chaosx.fallout.468.a.tt

Source line: 1314.
Before: Record the delayed result and retain its infrastructure and supply consequences.

After: The crossing review ends. Its infrastructure and supply consequences remain.

### chaosx.fallout.632.a.tt

Source line: 1366.
Before: Apply the seasonal outcome, preserve the target state's Canal Schedule record, and close the review.

After: The seasonal canal review ends.

### chaosx.fallout.772.a.tt

Source line: 1485.
Before: Apply the delayed maritime outcome, preserve its final record, and release the harbor and partner from further obligations.

After: Apply the delayed maritime outcome and release the harbor and partner from further obligations.

### chaosx.fallout.737.a.tt

Source line: 1608.
Before: Apply the cohort review and close the government's route record. A failed review may cause additional deaths.

After: The cohort review ends. A failed review may cause additional deaths.

### chaosx.fallout.1041.a.tt

Source line: 1674.
Before: Apply the delayed generation result, record the final cause memory, release the ward and witness reservations, and close Children of Two Settlements.

After: The school review ends. The wards and witnesses can take on other duties.

### chaosx.fallout.882.a.tt

Source line: 1801.
Before: Apply the graded clinic result, record its care-governance memory, and schedule the delayed first-season review.

After: Apply the graded clinic result and schedule the delayed first-season review.

### chaosx.fallout.1048.a.tt

Source line: 1876.
Before: Apply the delayed civic result, record the final cause memory, release the ward and witness reservations, and close The Cohort's First Ballot.

After: The first council review ends. The wards and witnesses can take on other duties.

### chaosx.fallout.485.b.tt

Source line: 2080.
Before: Spend Water, Power, and Medicine to invite a neighboring technical crew and record a bilateral credit.

After: Spend Water, Power, and Medicine to invite a neighboring technical crew and promise payment to the neighboring country.

### chaosx.fallout.487.a.tt

Source line: 2099.
Before: Record the delayed result and return for the second-shift review.

After: The second-shift review will follow.

### chaosx.fallout.707.a.tt

Source line: 2153.
Before: Record the chosen settlement and its delayed review in the Quarantine State's cause memory. A later hospital review will test whether the new authority survived another winter.

After: A later hospital review will test whether the chosen authority survived another winter.

### chaosx.fallout.230.d.tt

Source line: 2201.
Before: Spend §Y[?constant:fallout_event_230_cost.refusal_scrap|0]§! Scrap to close the doors and record the refusal. The shelter will be reviewed after §Y[?constant:fallout_event_230_timing.result_delay_days|0] days§!.

After: Spend §Y[?constant:fallout_event_230_cost.refusal_scrap|0]§! Scrap to close the doors. The shelter will be reviewed after §Y[?constant:fallout_event_230_timing.result_delay_days|0] days§!.

### chaosx.fallout.240.a.tt

Source line: 2236.
Before: Conclude the delayed audit and preserve the institution's lasting record.

After: The shelter admission review ends.

### chaosx.fallout.300.a.tt

Source line: 2343.
Before: Apply the ward review and preserve the institution's lasting record. Failure may cause additional deaths.

After: The ward review ends. Failure may cause additional deaths.

### chaosx.fallout.800.a.tt

Source line: 2410.
Before: Apply the delayed engineering review, preserve the power board's final record, and release the technical district and partner from further obligations.

After: Apply the delayed engineering review and release the technical district and partner from further obligations.

### chaosx.fallout.6.thermometer_success.a.tt

Source line: 2495.
Before: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§! and §YExposure§! falls by §G[?constant:air_winter_event_ledger.exposure_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the thermometer schedule as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§! and §YExposure§! falls by §G[?constant:air_winter_event_ledger.exposure_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.thermometer_failure.a.tt

Source line: 2499.
Before: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! falls by §R[?constant:air_winter_event_ledger.adaptation_minor|0]§! and §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the thermometer schedule as a failure.

After: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! falls by §R[?constant:air_winter_event_ledger.adaptation_minor|0]§! and §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.full_shift_success.a.tt

Source line: 2504.
Before: In §Y[air_winter_event_state.GetName]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§! and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. National War Support rises by §G[?constant:air_winter_event_country.war_support_minor|%1]§!. The state and national winter records mark the full-shift schedule as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§! and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. National War Support rises by §G[?constant:air_winter_event_country.war_support_minor|%1]§!.

### chaosx.fallout.6.full_shift_failure.a.tt

Source line: 2508.
Before: In §Y[air_winter_event_state.GetName]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_major|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local factory access receives a §R[?constant:air_winter_event_phase_1_return.factory_access_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the full-shift schedule as a failure with casualties.

After: In §Y[air_winter_event_state.GetName]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_major|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local factory access receives a §R[?constant:air_winter_event_phase_1_return.factory_access_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.warehouse_success.a.tt

Source line: 2513.
Before: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_minor|0]§!, and §YRefugee Pressure§! falls by §G[?constant:air_winter_event_ledger.refugees_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the warehouse rooms as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_minor|0]§!, and §YRefugee Pressure§! falls by §G[?constant:air_winter_event_ledger.refugees_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.warehouse_failure.a.tt

Source line: 2517.
Before: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the warehouse rooms as a failure.

After: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.shipyard_success.a.tt

Source line: 2522.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! rises by §G[?constant:air_winter_event_ledger.food_minor|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!, and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. National War Support rises by §G[?constant:air_winter_event_country.war_support_minor|%1]§!. The state and national winter records mark the harbor priority as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! rises by §G[?constant:air_winter_event_ledger.food_minor|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!, and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. National War Support rises by §G[?constant:air_winter_event_country.war_support_minor|%1]§!.

### chaosx.fallout.6.shipyard_failure.a.tt

Source line: 2526.
Before: In §Y[air_winter_event_state.GetName]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_major|0]§! and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local supply receives a §R[?constant:air_winter_event_phase_1_return.supply_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National War Support falls by §R[?constant:air_winter_event_country.war_support_minor|%1]§!. The state and national winter records mark the harbor priority as a failure with casualties.

After: In §Y[air_winter_event_state.GetName]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_major|0]§! and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local supply receives a §R[?constant:air_winter_event_phase_1_return.supply_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National War Support falls by §R[?constant:air_winter_event_country.war_support_minor|%1]§!.

### chaosx.fallout.6.cistern_success.a.tt

Source line: 2531.
Before: In §Y[air_winter_event_state.GetName]§!, §YWater Security§! rises by §G[?constant:air_winter_event_ledger.water_minor|0]§!, §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_minor|0]§!, and §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark cistern rationing as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YWater Security§! rises by §G[?constant:air_winter_event_ledger.water_minor|0]§!, §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_minor|0]§!, and §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.cistern_failure.a.tt

Source line: 2535.
Before: In §Y[air_winter_event_state.GetName]§!, §YWater Security§! falls by §R[?constant:air_winter_event_ledger.water_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark cistern rationing as a failure.

After: In §Y[air_winter_event_state.GetName]§!, §YWater Security§! falls by §R[?constant:air_winter_event_ledger.water_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.fountain_success.a.tt

Source line: 2540.
Before: In §Y[air_winter_event_state.GetName]§!, §YWater Security§! rises by §G[?constant:air_winter_event_ledger.water_minor|0]§! and §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the public fountain circuit as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YWater Security§! rises by §G[?constant:air_winter_event_ledger.water_minor|0]§! and §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.fountain_failure.a.tt

Source line: 2544.
Before: In §Y[air_winter_event_state.GetName]§!, §YWater Security§! falls by §R[?constant:air_winter_event_ledger.water_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_major|0]§!, and §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local supply receives a §R[?constant:air_winter_event_phase_1_return.supply_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!. The state and national winter records mark the public fountain circuit as a failure with casualties.

After: In §Y[air_winter_event_state.GetName]§!, §YWater Security§! falls by §R[?constant:air_winter_event_ledger.water_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_major|0]§!, and §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local supply receives a §R[?constant:air_winter_event_phase_1_return.supply_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!.

### chaosx.fallout.6.drainage_success.a.tt

Source line: 2549.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! rises by §G[?constant:air_winter_event_ledger.food_minor|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!, and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark field drainage as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! rises by §G[?constant:air_winter_event_ledger.food_minor|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!, and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.drainage_failure.a.tt

Source line: 2553.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local supply receives a §R[?constant:air_winter_event_phase_1_return.supply_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark field drainage as a failure with casualties.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local supply receives a §R[?constant:air_winter_event_phase_1_return.supply_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.school_success.a.tt

Source line: 2558.
Before: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, and §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the school shelters as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, and §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.school_failure.a.tt

Source line: 2562.
Before: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_major|0]§!, and §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the school shelters as a failure with casualties.

After: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_major|0]§!, and §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.marker_success.a.tt

Source line: 2567.
Before: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!, and §YExposure§! falls by §G[?constant:air_winter_event_ledger.exposure_minor|0]§!. Local supply receives a §G[?constant:air_winter_event_phase_1_return.supply_bonus|%0]§! benefit for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National War Support rises by §G[?constant:air_winter_event_country.war_support_minor|%1]§!. The state and national winter records mark the corridor as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!, and §YExposure§! falls by §G[?constant:air_winter_event_ledger.exposure_minor|0]§!. Local supply receives a §G[?constant:air_winter_event_phase_1_return.supply_bonus|%0]§! benefit for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National War Support rises by §G[?constant:air_winter_event_country.war_support_minor|%1]§!.

### chaosx.fallout.6.marker_failure.a.tt

Source line: 2571.
Before: In §Y[air_winter_event_state.GetName]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_severe|0]§!, §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!, and §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_severe_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local supply receives a §R[?constant:air_winter_event_phase_1_return.supply_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National War Support falls by §R[?constant:air_winter_event_country.war_support_minor|%1]§!. The state and national winter records mark the corridor as a failure with casualties.

After: In §Y[air_winter_event_state.GetName]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_severe|0]§!, §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_moderate|0]§!, and §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_severe_failure_percent|%3]§! of the current state civilian population and are added to the death toll. Local supply receives a §R[?constant:air_winter_event_phase_1_return.supply_penalty|%0]§! penalty for §Y[?constant:air_winter_event_runtime.delayed_short_days|0] days§!. National War Support falls by §R[?constant:air_winter_event_country.war_support_minor|%1]§!.

### chaosx.fallout.6.recall_success.a.tt

Source line: 2576.
Before: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YExposure§! falls by §G[?constant:air_winter_event_ledger.exposure_minor|0]§!, and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the recalled crews as a success.

After: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YExposure§! falls by §G[?constant:air_winter_event_ledger.exposure_minor|0]§!, and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.6.recall_failure.a.tt

Source line: 2580.
Before: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!, and §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!. The state and national winter records mark the recalled crews as a failure with casualties.

After: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!, and §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!. Civilian losses equal §R[?constant:air_winter_event_deaths.phase_1_minor_failure_percent|%3]§! of the current state civilian population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_minor|%1]§!.

### chaosx.fallout.18.a.tt

Source line: 2598.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! rises by §G[?constant:air_winter_event_ledger.food_major|0]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_moderate|0]§!, and §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!. The planting register remains part of this state's winter record.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! rises by §G[?constant:air_winter_event_ledger.food_major|0]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_moderate|0]§!, and §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!.

### chaosx.fallout.18.b.tt

Source line: 2600.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_minor|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. The failed plots remain part of this state's winter record.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_minor|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_minor|0]§!.

### chaosx.fallout.18.c.tt

Source line: 2602.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_major|0]§!, §YReclamation§! falls by §R[?constant:air_winter_event_ledger.reclamation_minor|0]§!, and §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!. The empty herds remain part of this state's winter record.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_major|0]§!, §YReclamation§! falls by §R[?constant:air_winter_event_ledger.reclamation_minor|0]§!, and §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!.

### chaosx.fallout.18.d.tt

Source line: 2604.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! rises by §G[?constant:air_winter_event_ledger.food_major|0]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, and §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_moderate|0]§!. The registered herds remain part of this state's winter record.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! rises by §G[?constant:air_winter_event_ledger.food_major|0]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, and §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_moderate|0]§!.

### chaosx.fallout.18.e.tt

Source line: 2606.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YReclamation§! falls by §R[?constant:air_winter_event_ledger.reclamation_minor|0]§!. The failed breeding season remains part of this state's winter record.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YReclamation§! falls by §R[?constant:air_winter_event_ledger.reclamation_minor|0]§!.

### chaosx.fallout.21.b

Source line: 2734.
Before: Record the wreck and close the line.

After: Identify the wreck and close the line.

### chaosx.fallout.39.a.tt

Source line: 2936.
Before: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_moderate|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_moderate|0]§!, and §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_moderate|0]§!. The state and country retain a successful open-harbor record.

After: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_moderate|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_moderate|0]§!, and §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_moderate|0]§!.

### chaosx.fallout.39.b.tt

Source line: 2938.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_moderate|0]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_moderate|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_major|0]§!, and §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_minor|0]§!. Losses among local residents and rescue crews equal §R[?constant:air_winter_event_deaths.island_refugee_failure_percent|%3]§! of the remaining state population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!. The state and country retain an overwhelmed rescue-shed record.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_moderate|0]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_moderate|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_major|0]§!, and §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_minor|0]§!. Losses among local residents and rescue crews equal §R[?constant:air_winter_event_deaths.island_refugee_failure_percent|%3]§! of the remaining state population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!.

### chaosx.fallout.39.c.tt

Source line: 2940.
Before: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!, §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. The state and country retain an orderly quarantine record.

After: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, §YShelter Capacity§! rises by §G[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YReclamation§! rises by §G[?constant:air_winter_event_ledger.reclamation_minor|0]§!, §YDisease Pressure§! falls by §G[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YBuilding Damage Pressure§! falls by §G[?constant:air_winter_event_ledger.building_pressure_minor|0]§!.

### chaosx.fallout.39.d.tt

Source line: 2942.
Before: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_major|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. Losses among local patients, guards, and dock workers equal §R[?constant:air_winter_event_deaths.island_refugee_failure_percent|%3]§! of the remaining state population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!. The state and country retain a failed quarantine-cordon record.

After: In §Y[air_winter_event_state.GetName]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_major|0]§!, and §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_minor|0]§!. Losses among local patients, guards, and dock workers equal §R[?constant:air_winter_event_deaths.island_refugee_failure_percent|%3]§! of the remaining state population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!.

### chaosx.fallout.39.e.tt

Source line: 2944.
Before: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, §YExposure§! falls by §G[?constant:air_winter_event_ledger.exposure_minor|0]§!, and §YRefugee Pressure§! falls by §G[?constant:air_winter_event_ledger.refugees_minor|0]§!. The state and country retain a maintained exclusion-line record.

After: In §Y[air_winter_event_state.GetName]§!, §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!, §YExposure§! falls by §G[?constant:air_winter_event_ledger.exposure_minor|0]§!, and §YRefugee Pressure§! falls by §G[?constant:air_winter_event_ledger.refugees_minor|0]§!.

### chaosx.fallout.39.f.tt

Source line: 2946.
Before: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_minor|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!, and §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_minor|0]§!. Local patrol and harbor losses equal §R[?constant:air_winter_event_deaths.island_refugee_failure_percent|%3]§! of the remaining state population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!. The state and country retain a broken exclusion-line record.

After: In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_minor|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!, and §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_minor|0]§!. Local patrol and harbor losses equal §R[?constant:air_winter_event_deaths.island_refugee_failure_percent|%3]§! of the remaining state population and are added to the death toll. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!.

### chaosx.fallout.42.a

Source line: 2979.
Before: Load the seed catalogs and soil records.

After: Load the seed catalogs and soil notes.

### chaosx.fallout.833.a.tt

Source line: 3165.
Before: Record the delayed calculation result, apply its local and national consequences, and open the later technical audit for the Manchurian Reactor Keeps.

After: Apply the local and national consequences and open the later technical audit for the Manchurian Reactor Keeps.

### chaosx.fallout.835.a.tt

Source line: 3172.
Before: Apply the delayed audit, preserve the calculation's lasting record, and release the state and its neighbor from further obligations.

After: Apply the delayed audit and release the state and its neighbor from further obligations.

### chaosx.fallout.693.a.tt

Source line: 3236.
Before: Record the branch and its delayed result in the Quarantine State's cause memory. A later appeal will test whether the new practice survived the next winter.

After: A later appeal will test whether the chosen practice survived the next winter.

### chaosx.fallout.478.b.tt

Source line: 3280.
Before: Spend Food and Medicine to import seed and record a bilateral debt with the convoy's country.

After: Spend Food and Medicine to import seed and owe payment to the convoy's country.

### chaosx.fallout.482.a.tt

Source line: 3305.
Before: Record the second-sowing review and release the recovery chain.

After: The second-sowing review ends.

### chaosx.fallout.972.a.tt

Source line: 3352.
Before: Apply the graded household result, record its generation memory, and schedule the delayed next-generation review.

After: Apply the graded household result and schedule the delayed next-generation review.

### chaosx.fallout.974.a.tt

Source line: 3358.
Before: Apply the delayed next-generation outcome, preserve its final record, and release the state and witness from further obligations.

After: Apply the delayed next-generation outcome and release the state and witness from further obligations.

### chaosx.fallout.258.a.tt

Source line: 3411.
Before: Record the first Fever Dormitory outcome and schedule its follow-up review.

After: Schedule its follow-up review.

### chaosx.fallout.259.a.tt

Source line: 3417.
Before: Record the dispersed-bunk outcome and schedule its follow-up review.

After: Schedule its follow-up review.

### chaosx.fallout.260.a.tt

Source line: 3423.
Before: Record the public-treatment outcome and schedule its follow-up review.

After: Schedule its follow-up review.

### chaosx.fallout.261.a.tt

Source line: 3429.
Before: Record the concealed-fever outcome and schedule its follow-up review.

After: Schedule its follow-up review.

### chaosx.fallout.266.a.tt

Source line: 3435.
Before: Record the outcome and close the remaining Fever Dormitory reviews.

After: The remaining Fever Dormitory reviews end.

### chaosx.fallout.227.a.tt

Source line: 3502.
Before: Conclude the filter audit and preserve the policy record.

After: The filter audit ends.

### chaosx.fallout.688.a.tt

Source line: 3560.
Before: Close the delayed record and conclude the coordinator's review.

After: The coordinator's review ends.

### chaosx.fallout.856.a.tt

Source line: 3625.
Before: Apply the delayed review, preserve the standards' lasting record, and release the state and its neighbor from further obligations.

After: Apply the delayed review and release the state and its neighbor from further obligations.

### chaosx.fallout.286.a.tt

Source line: 3697.
Before: Apply the follow-up result and preserve its lasting record. Failure may cause additional deaths.

After: The follow-up ends. Failure may cause additional deaths.

### chaosx.fallout.319.a.tt

Source line: 3757.
Before: Record the urban priority, apply its immediate result, and begin the 240-day public maintenance follow-up.

After: The urban lighting policy takes effect. A public maintenance review follows after 240 days.

### chaosx.fallout.475.a.tt

Source line: 3827.
Before: Record the delayed result and retain its shelter and clinic consequences.

After: The exposure review ends. Its shelter and clinic consequences remain.

### chaosx.fallout.777.a.tt

Source line: 3874.
Before: Apply the delayed convoy outcome, preserve its route record, and release the harbor and partner from further obligations.

After: Apply the delayed convoy outcome and release the harbor and partner from further obligations.

### chaosx.fallout.779.a.tt

Source line: 3880.
Before: Apply the delayed convoy review, preserve the route's final record, and release the harbor and partner from further obligations.

After: Apply the delayed convoy review and release the harbor and partner from further obligations.

### chaosx.fallout.667.a.tt

Source line: 3948.
Before: Close the Great Lakes Lock Winter record after the thaw inspection and preserve its durable memory.

After: The Great Lakes thaw inspection ends.

### chaosx.fallout.826.a.tt

Source line: 4007.
Before: Record the delayed grid result, apply its regional consequences, and open the later review for the Manchurian Reactor Keeps.

After: Apply the regional consequences and open the later review for the Manchurian Reactor Keeps.

### chaosx.fallout.828.a.tt

Source line: 4014.
Before: Apply the regional grid result, preserve the second year's record, and release the state and its neighbor from further obligations.

After: Apply the regional grid result and release the state and its neighbor from further obligations.

### chaosx.fallout.784.a.tt

Source line: 4079.
Before: Apply the delayed harbor outcome, preserve the government's record, and release the harbor and partner from further obligations.

After: Apply the delayed harbor outcome and release the harbor and partner from further obligations.

### chaosx.fallout.786.a.tt

Source line: 4085.
Before: Apply the delayed harbor review, preserve the government's final record, and release the harbor and partner from further obligations.

After: Apply the delayed harbor review and release the harbor and partner from further obligations.

### chaosx.fallout.747.b.tt

Source line: 4128.
Before: Spend Food 4, Power 4, Scrap 2, and Recognition 2. After 45 days, inspection teams will test partner clinics and record whether the network shares care or merely exports quarantine.

After: Spend Food 4, Power 4, Scrap 2, and Recognition 2. After 45 days, inspection teams will inspect partner clinics to see whether the network shares care or merely exports quarantine.

### chaosx.fallout.747.d.tt

Source line: 4132.
Before: Spend Food 6, Medicine 3, Fuel 3, and Recognition 1. After 45 days, mobile care teams will carry medicine across the North Gate and record whether the state can protect patients outside its walls.

After: Spend Food 6, Medicine 3, Fuel 3, and Recognition 1. After 45 days, mobile care teams will carry medicine across the North Gate and test whether the state can protect patients outside its walls.

### chaosx.fallout.494.a.tt

Source line: 4299.
Before: Record the delayed ice-melt result and return for a later review of the water board's reserve.

After: A later review will test the water board's reserve.

### chaosx.fallout.102.a.tt

Source line: 4379.
Before: Record the public ration decision and schedule the first winter review.

After: Schedule the first winter review.

### chaosx.fallout.103.a.tt

Source line: 4386.
Before: Record the household cache decision and schedule the first winter review.

After: Schedule the first winter review.

### chaosx.fallout.104.a.tt

Source line: 4393.
Before: Record the requisition decision and schedule the first winter review.

After: Schedule the first winter review.

### chaosx.fallout.105.a.tt

Source line: 4400.
Before: Preserve the first winter's record and close its delayed review.

After: The first winter ration review ends.

### chaosx.fallout.109.a.tt

Source line: 4418.
Before: Record the gate decision and wait for the water compact or epidemic review.

After: Wait for the water compact or epidemic review.

### chaosx.fallout.110.a.tt

Source line: 4425.
Before: Record the filter ration and wait for the water compact or epidemic review.

After: Wait for the water compact or epidemic review.

### chaosx.fallout.111.a.tt

Source line: 4432.
Before: Record the pump seizure and wait for the water compact or epidemic review.

After: Wait for the water compact or epidemic review.

### chaosx.fallout.121.a.tt

Source line: 4439.
Before: Record the foreign test and wait for the water compact or epidemic review.

After: Wait for the water compact or epidemic review.

### chaosx.fallout.112.a.tt

Source line: 4446.
Before: Preserve the intake record and close its delayed review.

After: The intake review ends.

### chaosx.fallout.114.b.tt

Source line: 4488.
Before: Put the repair line under military labor orders. The trains move faster when the order holds, but the country records an atrocity memory if the crews return to tell the story.

After: Put the repair line under military labor orders. The trains move faster when the order holds, but the country faces accusations of abuse if the crews return to tell the story.

### chaosx.fallout.114.c.tt

Source line: 4490.
Before: Withdraw the crews and preserve what fuel remains. A clean withdrawal may save stores, while a failed retreat damages the line and records deaths in the corridor state.

After: Withdraw the crews and preserve what fuel remains. A clean withdrawal may save stores, while a failed retreat damages the line and kills people in the corridor state.

### chaosx.fallout.114.d_option.tt

Source line: 4492.
Before: Ask the neighboring authority to open its dispatch room and share the line. The pilot records a limited state access agreement without creating a full bilateral partnership.

After: Ask the neighboring authority to open its dispatch room and share the line under a limited state access agreement.

### chaosx.fallout.116.a.tt

Source line: 4499.
Before: Record the protected repair result and wait seven days for the crew review.

After: Wait seven days for the crew review.

### chaosx.fallout.117.a.tt

Source line: 4506.
Before: Record the labor order and wait seven days for the crew review.

After: Wait seven days for the crew review.

### chaosx.fallout.118.a.tt

Source line: 4513.
Before: Record the abandoned line and wait seven days for the crew review.

After: Wait seven days for the crew review.

### chaosx.fallout.122.a.tt

Source line: 4520.
Before: Record the shared access request and wait seven days for the crew review.

After: Wait seven days for the crew review.

### chaosx.fallout.119.a.tt

Source line: 4527.
Before: Preserve the record of Rail Crew Twenty-Seven and close its delayed review.

After: The Rail Crew Twenty-Seven review ends.

### chaosx.fallout.840.a.tt

Source line: 4623.
Before: Record the delayed civic result, apply its local and national consequences, and open the later citizenship review for the Manchurian Reactor Keeps.

After: Apply the local and national consequences and open the later citizenship review for the Manchurian Reactor Keeps.

### chaosx.fallout.842.a.tt

Source line: 4630.
Before: Apply the delayed review, preserve the citizenship policy's lasting record, and release the state and its neighbor from further obligations.

After: Apply the delayed review and release the state and its neighbor from further obligations.

### chaosx.fallout.807.a.tt

Source line: 4784.
Before: Apply the delayed review, preserve the sector's final record, and release the district and neighboring state from further obligations.

After: Apply the delayed review and release the district and neighboring state from further obligations.

### chaosx.fallout.847.a.tt

Source line: 4847.
Before: Record the delayed protocol result, apply its local and national consequences, and open the later machine review for the Manchurian Reactor Keeps.

After: Apply the local and national consequences and open the later machine review for the Manchurian Reactor Keeps.

### chaosx.fallout.849.a.tt

Source line: 4854.
Before: Apply the delayed review, preserve the machine protocol's lasting record, and release the state and its neighbor from further obligations.

After: Apply the delayed review and release the state and its neighbor from further obligations.

### chaosx.fallout.508.a.tt

Source line: 5024.
Before: Close the checkpoint report. The route's outcome stays on record.

After: The checkpoint review ends.

### chaosx.fallout.646.a.tt

Source line: 5148.
Before: Apply the delayed review, preserve the works' record, and conclude the Mine Generator settlement without changing the native resource deposits.

After: Apply the delayed review and conclude the Mine Generator settlement without changing the native resource deposits.

### chaosx.fallout.889.a.tt

Source line: 5270.
Before: Apply the graded settlement result, record its mixed-community memory, and schedule the delayed first-year review.

After: Apply the graded settlement result and schedule the delayed first-year review.

### chaosx.fallout.891.a.tt

Source line: 5276.
Before: Apply the first-year outcome, preserve the mixed community's final record, and release the state and witness from further obligations.

After: Apply the first-year outcome and release the state and witness from further obligations.

### chaosx.fallout.765.a.tt

Source line: 5421.
Before: Apply the delayed bilateral outcome, preserve its final record, and release the state and its neighbor from further obligations.

After: Apply the delayed bilateral outcome and release the state and its neighbor from further obligations.

### chaosx.fallout.877.a.tt

Source line: 5491.
Before: Apply the delayed generational outcome, preserve the community's final identity record, and release the state and its neighbor from further obligations.

After: Apply the delayed generational outcome and release the state and its neighbor from further obligations.

### chaosx.fallout.271.a.tt

Source line: 5546.
Before: Record the public register result and schedule its follow-up. Failure may cause additional deaths.

After: Schedule its follow-up. Failure may cause additional deaths.

### chaosx.fallout.272.a.tt

Source line: 5553.
Before: Record the restricted archive result and schedule its follow-up. Failure may cause additional deaths.

After: Schedule its follow-up. Failure may cause additional deaths.

### chaosx.fallout.273.a.tt

Source line: 5560.
Before: Record the community memorial result and schedule its follow-up. Failure may cause additional deaths.

After: Schedule its follow-up. Failure may cause additional deaths.

### chaosx.fallout.274.a.tt

Source line: 5567.
Before: Record the local clerks' result and schedule its follow-up. Failure may cause additional deaths.

After: Schedule its follow-up. Failure may cause additional deaths.

### chaosx.fallout.279.a.tt

Source line: 5574.
Before: Preserve the names in the lasting record and close the delayed reviews.

After: The census follow-up reviews end.

### chaosx.fallout.551.a.tt

Source line: 5654.
Before: Preserve the funeral in the lasting record and close the delayed reviews.

After: The funeral follow-up reviews end.

### chaosx.fallout.651.a.tt

Source line: 5722.
Before: Apply the result, preserve the New Year in the historical record, and schedule a follow-up register after 330 days.

After: The New Year observance takes effect. A follow-up review begins after 330 days.

### chaosx.fallout.653.a.tt

Source line: 5729.
Before: Record the delayed outcome and close the New Year register.

After: The New Year follow-up ends.

### chaosx.fallout.1027.a.tt

Source line: 5945.
Before: Apply the delayed witness result, record the final cause memory, release the ward and witness reservations, and close the Old Doctor's Trial chain.

After: The doctor's trial review ends. The wards and witnesses can take on other duties.

### chaosx.fallout.740.b.tt

Source line: 6043.
Before: Spend Food 4, Power 4, Scrap 2, and Recognition 2. After 35 days, a research team will test the sealed rooms and record whether its access protects medicine or strips the city for samples.

After: Spend Food 4, Power 4, Scrap 2, and Recognition 2. After 35 days, a research team will inspect the sealed rooms to see whether its access protects medicine or strips the city for samples.

### chaosx.fallout.412.a.tt

Source line: 6134.
Before: Record the first harvest review and release the recovery chain.

After: The first harvest review ends.

### chaosx.fallout.74.b.tt

Source line: 6297.
Before: Commit §Y[?constant:fallout_orientation_cost.government_division_food|0] Food§! and §Y[?constant:fallout_orientation_cost.government_division_shelter|0] Shelter capacity§!. Success adds §Y[?constant:fallout_orientation_result.government_division_success_recognition|0] Recognition§! and §Y[?constant:fallout_orientation_result.government_division_success_cohesion|0] Cohesion§! and records a durable institutional compact. A contested result records a disputed compact with smaller gains. Failure lowers Recognition and Cohesion and records an unresolved institutional dispute.

After: Commit §Y[?constant:fallout_orientation_cost.government_division_food|0] Food§! and §Y[?constant:fallout_orientation_cost.government_division_shelter|0] Shelter capacity§!. Success adds §Y[?constant:fallout_orientation_result.government_division_success_recognition|0] Recognition§! and §Y[?constant:fallout_orientation_result.government_division_success_cohesion|0] Cohesion§! and establishes a lasting compact. A contested result leaves a disputed compact with smaller gains. Failure lowers Recognition and Cohesion and leaves an unresolved dispute over authority.

### chaosx.fallout.74.c.tt

Source line: 6299.
Before: Commit §Y[?constant:fallout_orientation_cost.government_rival_scrap|0] Scrap§! and §Y[?constant:fallout_orientation_cost.government_rival_fuel|0] Fuel§!. Success adds §Y[?constant:fallout_orientation_result.government_rival_success_recognition|0] Recognition§! and §Y[?constant:fallout_orientation_result.government_rival_success_cohesion|0] Cohesion§! and records the rival as integrated. A contested result leaves the rival autonomous with smaller gains. Failure lowers Recognition and Cohesion and records a rupture.

After: Commit §Y[?constant:fallout_orientation_cost.government_rival_scrap|0] Scrap§! and §Y[?constant:fallout_orientation_cost.government_rival_fuel|0] Fuel§!. Success adds §Y[?constant:fallout_orientation_result.government_rival_success_recognition|0] Recognition§! and §Y[?constant:fallout_orientation_result.government_rival_success_cohesion|0] Cohesion§! and brings the rival under the same authority. A contested result leaves the rival autonomous with smaller gains. Failure lowers Recognition and Cohesion and breaks the agreement.

### chaosx.fallout.76.a.tt

Source line: 6312.
Before: The authority return records the chosen institution, its result, and the durable government memory.

After: The government faces the consequences of its chosen authority.

### chaosx.fallout.70.b.tt

Source line: 6555.
Before: Commit §Y[?constant:fallout_orientation_cost.resource_requisition_recognition|0] Recognition§! and §Y[?constant:fallout_orientation_cost.resource_requisition_cohesion|0] Cohesion§!. A strong result raises [This.GetFalloutOrientationCrisisResourceName] by §Y[?constant:fallout_orientation_result.resource_requisition_success_crisis|0]§!. A contested result raises it by §Y[?constant:fallout_orientation_result.resource_requisition_partial_crisis|0]§! and lowers Recognition by another §R[?constant:fallout_orientation_result.resource_requisition_partial_recognition|0]§!. Failure lowers Recognition by another §R[?constant:fallout_orientation_result.resource_requisition_failure_recognition|0]§! and records civilian Deaths equal to fifteen people per ten thousand from the surviving population counted when the order opened.

After: Commit §Y[?constant:fallout_orientation_cost.resource_requisition_recognition|0] Recognition§! and §Y[?constant:fallout_orientation_cost.resource_requisition_cohesion|0] Cohesion§!. A strong result raises [This.GetFalloutOrientationCrisisResourceName] by §Y[?constant:fallout_orientation_result.resource_requisition_success_crisis|0]§!. A contested result raises it by §Y[?constant:fallout_orientation_result.resource_requisition_partial_crisis|0]§! and lowers Recognition by another §R[?constant:fallout_orientation_result.resource_requisition_partial_recognition|0]§!. Failure lowers Recognition by another §R[?constant:fallout_orientation_result.resource_requisition_failure_recognition|0]§! and causes civilian Deaths equal to fifteen people per ten thousand from the surviving population counted when the order opened.

### chaosx.fallout.72.a.tt

Source line: 6570.
Before: The four-day return enters the public record with the chosen authority, civilian losses, and the condition of the assigned capital.

After: The four-day review assesses the chosen authority, civilian losses, and the assigned capital's condition.

### chaosx.fallout.821.a.tt

Source line: 6606.
Before: Apply the delayed review, preserve the final Patent After the End record, and release the district and its neighbor from further obligations.

After: Apply the delayed review and release the district and its neighbor from further obligations.

### chaosx.fallout.700.a.tt

Source line: 6668.
Before: Record the branch and its delayed result in the Quarantine State's cause memory. A later review will test whether the permit rule survived the next winter.

After: A later review will test whether the permit rule survived the next winter.

### chaosx.fallout.793.a.tt

Source line: 6738.
Before: Apply the delayed sea-law review, preserve the crew's final record, and release the harbor and partner from further obligations.

After: Apply the delayed sea-law review and release the harbor and partner from further obligations.

### chaosx.fallout.868.a.tt

Source line: 6801.
Before: Record the delayed result, apply its Air Winter, Supply Access, government, and recognition consequences, and open the later citizenship audit.

After: Apply the Air Winter, Supply Access, government, and recognition consequences and open the later citizenship audit.

### chaosx.fallout.870.a.tt

Source line: 6808.
Before: Apply the delayed audit, preserve the community's lasting identity record, and release the state and its neighbor from further obligations.

After: Apply the delayed audit and release the state and its neighbor from further obligations.

### chaosx.fallout.1053.a.tt

Source line: 6872.
Before: Apply the graded quarantine result, record the branch memory, update the neighboring government's opinion, and schedule a delayed wet-season review.

After: The quarantine choice affects the neighboring government's opinion. A wet-season review will follow.

### chaosx.fallout.1055.a.tt

Source line: 6878.
Before: Apply the delayed review, record the final cause memory, release the gate and witness reservations, and close The Quarantine Ultimatum.

After: The quarantine review ends. The gate and witnesses can take on other duties.

### chaosx.fallout.398.a.tt

Source line: 7068.
Before: Conclude the follow-up and preserve the branch's record.

After: The ration inquiry follow-up ends.

### chaosx.fallout.503.a.tt

Source line: 7121.
Before: The later review settles the matter and preserves its disease and migration record.

After: The later review settles the water dispute and its disease and migration consequences.

### chaosx.fallout.370.a.tt

Source line: 7245.
Before: Conclude the inspection and record its result.

After: The reactor inspection ends.

### chaosx.fallout.417.a.tt

Source line: 7302.
Before: Apply the train result, record the bilateral memory, and schedule the first anniversary review.

After: Apply the train result and schedule the first anniversary review.

### chaosx.fallout.419.a.tt

Source line: 7308.
Before: Conclude the anniversary review and preserve its record.

After: The first anniversary review ends.

### chaosx.fallout.861.a.tt

Source line: 7447.
Before: Record the delayed charter result, apply its Air Winter, Supply Access, route, and recognition consequences, and open the later charter audit.

After: Apply the Air Winter, Supply Access, route, and recognition consequences and open the later charter audit.

### chaosx.fallout.863.a.tt

Source line: 7454.
Before: Apply the delayed audit, preserve the repairs' lasting record, and release the state and its neighbor from further obligations.

After: Apply the delayed audit and release the state and its neighbor from further obligations.

### chaosx.fallout.714.a.tt

Source line: 7518.
Before: Record the result in the Quarantine State's cause memory and begin a delayed review of treatment capacity, border trust, aid dependence, and concealment pressure.

After: Begin a delayed review of treatment capacity, border trust, aid dependence, and concealment pressure.

### chaosx.fallout.569.a.tt

Source line: 7598.
Before: Apply the 180-day river review, preserve the branch and grade record, and open the resulting federation or barge war when conditions permit.

After: Apply the 180-day river review, and open the resulting federation or barge war when conditions permit.

### chaosx.fallout.293.a.tt

Source line: 7668.
Before: Apply the cohort review and preserve the curriculum's lasting record. Failure may cause additional deaths.

After: The school review ends. Failure may cause additional deaths.

### chaosx.fallout.333.a.tt

Source line: 7728.
Before: Record the warehouse policy, apply its delayed salvage result, and begin the 180-day site memory follow-up.

After: The salvage policy takes effect. A warehouse review follows after 180 days.

### chaosx.fallout.335.a.tt

Source line: 7734.
Before: Apply the long-term site result and preserve the warehouse record.

After: The long-term warehouse review ends.

### chaosx.fallout.658.a.tt

Source line: 7799.
Before: Record the settled field result and schedule a planting-season review in §Y[?constant:fallout_event_656_timing.callback_delay_days|0] days§!.

After: Schedule a planting-season review in §Y[?constant:fallout_event_656_timing.callback_delay_days|0] days§!.

### chaosx.fallout.198.a.tt

Source line: 7890.
Before: The case will close after the follow-up records its outcome.

After: The seed review ends after the follow-up.

### chaosx.fallout.305.a.tt

Source line: 7936.
Before: Record the delayed result and begin the one-year household follow-up.

After: Begin the one-year household follow-up.

### chaosx.fallout.424.a.tt

Source line: 8000.
Before: Apply the harbour result, record maritime memory, and schedule the first seasonal review.

After: Apply the harbour result and schedule the first seasonal review.

### chaosx.fallout.426.a.tt

Source line: 8006.
Before: Conclude the review and preserve its maritime record.

After: The harbour seasonal review ends.

### chaosx.fallout.461.a.tt

Source line: 8110.
Before: Record the delayed result and retain its consequences for the state.

After: The flood review ends. Its consequences remain in the state.

### chaosx.fallout.175.a.tt

Source line: 8135.
Before: Spend §Y[?constant:fallout_event_175_cost.children_medicine|0]§! Medicine and review the children's ward after §Y[?constant:fallout_event_175_timing.result_delay_days|0] days§!. A strong result preserves dependents and records the policy for the state.

After: Spend §Y[?constant:fallout_event_175_cost.children_medicine|0]§! Medicine and review the children's ward after §Y[?constant:fallout_event_175_timing.result_delay_days|0] days§!. A strong result preserves dependents and strengthens care for the state's families.

### chaosx.fallout.175.e.tt

Source line: 8141.
Before: Spend §Y[?constant:fallout_event_175_cost.equal_medicine|0]§! Medicine and draw the ward lots. The result returns after §Y[?constant:fallout_event_175_timing.result_delay_days|0] days§! and leaves the clearest record of the equal-chance rule.

After: Spend §Y[?constant:fallout_event_175_cost.equal_medicine|0]§! Medicine and draw the ward lots. The result returns after §Y[?constant:fallout_event_175_timing.result_delay_days|0] days§! and tests whether equal chances can save lives.

### chaosx.fallout.177.a.tt

Source line: 8148.
Before: Resolve the children's ward, preserve its medical ethics record, and schedule a doctor's review in §Y[?constant:fallout_event_175_timing.callback_delay_days|0] days§!.

After: Resolve the children's ward and schedule a doctor's review in §Y[?constant:fallout_event_175_timing.callback_delay_days|0] days§!.

### chaosx.fallout.178.a.tt

Source line: 8155.
Before: Resolve the workshop ward, preserve its labor record, and schedule a doctor's review.

After: Resolve the workshop ward and schedule a doctor's review.

### chaosx.fallout.179.a.tt

Source line: 8162.
Before: Resolve the guard ward, preserve its command record, and schedule a doctor's review.

After: Resolve the guard ward and schedule a doctor's review.

### chaosx.fallout.180.a.tt

Source line: 8169.
Before: Resolve the equal-chance ward, preserve its public record, and schedule a doctor's review.

After: Resolve the equal-chance ward and schedule a doctor's review.

### chaosx.fallout.185.a.tt

Source line: 8176.
Before: Conclude the follow-up and preserve the doctor's record.

After: The doctor's follow-up ends.

### chaosx.fallout.611.a.tt

Source line: 8229.
Before: Record the institutional review and close the case.

After: The shelter council review ends.

### chaosx.fallout.363.a.tt

Source line: 8295.
Before: Conclude the follow-up and record its result.

After: The archive follow-up ends.

### chaosx.fallout.517.a.tt

Source line: 8347.
Before: Conclude the safety review and preserve its Fallout record.

After: The weapon safety review ends.

### chaosx.fallout.155.a.tt

Source line: 8383.
Before: Resolve the public queue review, record its result in Fallout memory, and schedule a five-day follow-up review.

After: Resolve the public queue review and schedule a five-day follow-up review.

### chaosx.fallout.156.a.tt

Source line: 8390.
Before: Resolve the ration card review, record its result in Fallout memory, and schedule a five-day follow-up review.

After: Resolve the ration card review and schedule a five-day follow-up review.

### chaosx.fallout.157.a.tt

Source line: 8397.
Before: Resolve the guarded intake review, record its result in Fallout memory, and schedule a five-day follow-up review.

After: Resolve the guarded intake review and schedule a five-day follow-up review.

### chaosx.fallout.161.a.tt

Source line: 8404.
Before: Conclude the follow-up review and preserve its final Fallout record.

After: The well follow-up review ends.

### chaosx.fallout.326.a.tt

Source line: 8513.
Before: Record the grain policy, apply its delayed result, and begin the 210-day storage and ration maintenance follow-up.

After: The grain policy takes effect. A storage and ration review follows after 210 days.

### chaosx.fallout.403.a.tt

Source line: 8629.
Before: Apply the calendar result, preserve its record, and schedule the first anniversary review.

After: Apply the calendar result and schedule the first anniversary review.

### chaosx.fallout.405.a.tt

Source line: 8635.
Before: Conclude the anniversary review and preserve its record.

After: The anniversary review ends.

### fallout_adaptation_rite_result_partial

Source line: 868.
Before: Contested Practice Record

After: Disputed Practice

### fallout_adaptation_rite_result_failed

Source line: 869.
Before: Broken Practice Record

After: Practice Rejected

### fallout_adaptation_rite_register_failure

Source line: 877.
Before: Broken Practice Record

After: Practice Rejected

### chaosx.fallout.206.a.tt

Source line: 1110.
Before: The follow-up will decide whether the burn record becomes a trusted safeguard or a warning about lost evidence.

After: The follow-up will test whether burning the batch protected the next crop or destroyed useful evidence.

### fallout.event_log.captains_articles.detail.cancelled

Source line: 1507.
Before: The port record was cancelled after its state, partner, owner, controller, or generation changed.

After: The port review ended when the territory or participating authorities changed.

### fallout_captains_articles_register_failure

Source line: 1519.
Before: Broken Port Record

After: Port Duties Unsettled

### fallout_children_of_two_settlements_result_partial

Source line: 1698.
Before: Contested Generation Record

After: Disputed School Arrangement

### fallout_children_of_two_settlements_result_failed

Source line: 1699.
Before: Broken Generation Record

After: School Arrangement Failed

### fallout_children_of_two_settlements_register_failure

Source line: 1707.
Before: Broken Generation Record

After: School Arrangement Failed

### fallout.event_log.engineer_franchise.detail.cancelled

Source line: 2432.
Before: The power-board record was cancelled after its district, partner, owner, controller, or generation changed.

After: The power-board review ended when the territory or participating authorities changed.

### fallout.event_log.failed_calculation.detail.cancelled

Source line: 3196.
Before: The calculation record was cancelled after its district, partner, owner, controller, or generation changed.

After: The calculation review ended when the territory or participating authorities changed.

### fallout_failed_calculation_callback_partial

Source line: 3201.
Before: Provisional Audit Record

After: Provisional Engineering Review

### fallout_failed_calculation_calculation_failure

Source line: 3207.
Before: Calculation Record Dispute

After: Disputed Calculations

### fallout.event_log.first_regional_standard.detail.cancelled

Source line: 3649.
Before: The standards record was cancelled after its district, partner, owner, controller, or generation changed.

After: The standards review ended when the territory or participating authorities changed.

### chaosx.fallout.471.d.tt

Source line: 3806.
Before: Spend a small reserve to protect children and preserve the shelter record until the monitors hold.

After: Spend a small reserve to protect children and keep the shelter sealed until the monitors confirm a safe interval.

### fallout.event_log.ghost_convoy.detail.cancelled

Source line: 3902.
Before: The convoy record was cancelled after its state, partner, owner, controller, or generation changed.

After: The convoy review ended when the territory or participating authorities changed.

### fallout.event_log.great_lakes_lock_winter.detail.cancelled

Source line: 3976.
Before: The Great Lakes Lock Winter record closed after the port or its owner changed.

After: The Great Lakes Lock Winter review ended when the territory or participating authorities changed.

### fallout.event_log.great_lakes_lock_winter.detail.unknown

Source line: 3977.
Before: The Great Lakes Lock Winter record has no recognized port outcome.

After: The Great Lakes Lock Winter outcome remains unclear.

### fallout.event_log.grid_vote.detail.cancelled

Source line: 4038.
Before: The grid record was cancelled after its district, partner, owner, controller, or generation changed.

After: The grid review ended when the territory or participating authorities changed.

### fallout.event_log.harbor_without_city.detail.cancelled

Source line: 4107.
Before: The harbor record was cancelled after its state, partner, owner, controller, or generation changed.

After: The harbor review ended when the territory or participating authorities changed.

### chaosx.event_name.683

Source line: 4195.
Before: Closing the Battalion Ration Records

After: The Battalion Ration Review Ends

### fallout.event_log.hungry_battalion.detail.cancelled

Source line: 4252.
Before: The ration record closed after its state or owner changed.

After: The ration review ended when the territory or participating authorities changed.

### fallout.event_log.hungry_battalion.detail.unknown

Source line: 4253.
Before: The ration record has no recognized branch or review result.

After: The ration outcome remains unclear.

### fallout.event_log.laboratory_citizenship.detail.cancelled

Source line: 4654.
Before: The citizenship record was cancelled after its district, partner, owner, controller, or generation changed.

After: The citizenship review ended when the territory or participating authorities changed.

### fallout_laboratory_citizenship_citizenship_failure

Source line: 4665.
Before: Citizenship Record Dispute

After: Citizenship Dispute

### fallout.event_log.load_shedding.detail.cancelled

Source line: 4806.
Before: The circuit record was cancelled after its district, neighbor, owner, controller, or generation changed.

After: The circuit review ended when the territory or participating authorities changed.

### fallout.event_log.machine_suggests.detail.cancelled

Source line: 4878.
Before: The protocol record was cancelled after its district, partner, owner, controller, or generation changed.

After: The protocol review ended when the territory or participating authorities changed.

### fallout.event_log.mutant_envoy_gate.detail.cancelled

Source line: 5443.
Before: The envoy record was cancelled after its state, neighbor, owner, or generation changed.

After: The envoy review ended when the territory or participating authorities changed.

### fallout_mutant_envoy_gate_result_failed

Source line: 5447.
Before: Broken Envoy Record

After: Envoy Visit Failed

### fallout_mutant_envoy_gate_register_failure

Source line: 5455.
Before: Failed Envoy Record

After: Envoy Visit Failed

### fallout.event_log.name_we_choose.detail.cancelled

Source line: 5513.
Before: The identity record was cancelled after its state, neighbor, owner, or generation changed.

After: The identity review ended when the territory or participating authorities changed.

### fallout_old_doctor_trial_result_failed

Source line: 5970.
Before: Broken Trial Record

After: Trial Failed

### fallout_old_doctor_trial_register_failure

Source line: 5978.
Before: Broken Trial Record

After: Trial Failed

### fallout.event_log.patent_after_end.detail.cancelled

Source line: 6628.
Before: The patent record was cancelled after its district, partner, owner, controller, or generation changed.

After: The patent review ended when the territory or participating authorities changed.

### chaosx.fallout.791.a.tt

Source line: 6732.
Before: Apply the delayed sea-law outcome, record the chosen crew settlement, and release the harbor and partner from further obligations.

After: The sea-law review ends. The harbour and partner can take on other duties.

### fallout.event_log.pirate_amnesty.detail.cancelled

Source line: 6760.
Before: The sea-law record was cancelled after its state, partner, owner, controller, or generation changed.

After: The sea-law review ended when the territory or participating authorities changed.

### chaosx.fallout.1051.c.tt

Source line: 6855.
Before: Spend Fuel 2, Recognition 1, and Cohesion 2 to keep the river gate open under Basin guards. The choice protects movement and local pride, but disease and exposure rise while the neighboring government records a refusal.

After: Spend Fuel 2, Recognition 1, and Cohesion 2 to keep the river gate open under Basin guards. The choice protects movement and local pride, but disease and exposure rise while the neighboring government treats this as a refusal to cooperate.

### chaosx.fallout.812.a.tt

Source line: 7169.
Before: Apply the delayed Reactor Shift result, update Air Winter and Supply Access, preserve the operator's experience, record the bilateral opinion, and schedule a first-winter review.

After: Apply the delayed Reactor Shift result, update Air Winter and Supply Access, preserve the operator's experience, change the neighboring government's opinion, and schedule a first-winter review.

### chaosx.fallout.814.a.tt

Source line: 7175.
Before: Apply the delayed review, update the operator and state records, preserve the final Reactor Shift outcome, and release the district and its neighbor from further obligations.

After: The reactor review ends. Its consequences for the operator and state remain.

### fallout.event_log.reactor_shift.detail.cancelled

Source line: 7197.
Before: The reactor record was cancelled after its district, neighbor, owner, controller, or generation changed.

After: The reactor review ended when the territory or participating authorities changed.

### fallout.event_log.second_dust_bowl.detail.cancelled

Source line: 7845.
Before: The Second Dust Bowl record was cancelled after its state or settlement changed.

After: The Second Dust Bowl review ended when the territory or participating authorities changed.

### fallout.event_log.second_dust_bowl.detail.unknown

Source line: 7846.
Before: The Second Dust Bowl record has no recognized field outcome.

After: The Second Dust Bowl outcome remains unclear.

### chaosx.event_name.676

Source line: 8430.
Before: Closing the Work for Rations Records

After: The Work for Rations Review Ends

### fallout.event_log.work_for_rations.detail.cancelled

Source line: 8483.
Before: The Work for Rations record closed after its state or owner changed.

After: The Work for Rations review ended when the territory or participating authorities changed.

### fallout.event_log.work_for_rations.detail.unknown

Source line: 8484.
Before: The Work for Rations record has no recognized harvest outcome.

After: The Work for Rations outcome remains unclear.


## Continued G3 record wording pass

Status: implemented.
Acceptance basis: explicit parent instruction to rewrite every remaining literal record and records occurrence while preserving actual navigators and all parent treaty edits.
The fresh baseline contained 364 word occurrences in 355 values.
Every one of those 355 values was manually read, rewritten, and reviewed again in context.
Repeated phrase replacements were followed by exact sentence, plural, article, and semantic repairs.
The original 854-key handoff list above is retained as first-pass evidence.

Fresh baseline SHA-256: ab84ce8b2d3815edf450ffd10617644396bf3d6783d4141763213dea684ddbc3.
Final YML SHA-256: d98e78621616de944a33d7a123b3cec1bb25d740b2764e555e5d8367882f6de9.
Continued-pass unique changed keys: 355.
Combined unique changed keys across both passes: 1193.

Fresh-baseline byte reconstruction passed: restoring only the 355 original values reproduced the exact baseline SHA-256.
This proves all parent changes and every unrelated byte, prefix, suffix, BOM, and physical line ending were preserved during this continuation.
Ordered dynamic tokens, numeric literals, section-sign formatting codes, texticons, and escaped newline counts were unchanged for all 355 values.
No new keys, duplicate keys, or scripted-localisation changes were introduced.
python .tools/report_colour_audit.py --event fallout returned total keys with colour: 0 after the final edits.
Final literal forbidden-word count outside bracket tokens is zero for ids, records, segments, snapshots, transactions, receipts, ledgers, and providers.
The ten retained pilot or pilots values all name actual river or ice navigators, skiff crews, or their existing office candidates.
No sourced or attributed quotation was altered.
The parent additions fallout_treaty_relief_vote_cost, fallout_treaty_relief_vote_cost_ready, fallout_treaty_relief_vote_cost_blocked, and the air_cleanliness_treaty_relief_vote_ready_tt fourteen-day wording are byte-identical to the fresh baseline.
No source, gameplay, spreadsheet, Git, game, window, or asset action was taken during this continuation.
Prior MCP visual-coverage limits remain as stated above, and this text pass makes no full popup or GUI wrapping claim.

## Continued-pass exact changed key list

### air_cleanliness_treaty_seed_archive_exchange_desc

Source line: 172.
Before: Pack seed grain, crop trial notes, and greenhouse cuttings from our breadbaskets and seed vaults for a fellow member. The shipment deepens their winter food stores and leaves both governments a seed record to plant from if the sky never clears.

After: Pack seed grain, crop trial notes, and greenhouse cuttings from our breadbaskets and seed vaults for a fellow member. The shipment adds to their winter food stores and gives both governments planting instructions if the sky never clears.

### air_winter_phase_1_supply_relief_state_desc

Source line: 294.
Before: White route poles, guarded fuel caches, and reliable pass records are helping local depots move supplies through the winter corridor.

After: White route poles, guarded fuel caches, and reliable passage logs are helping local depots move supplies through the winter corridor.

### fallout_nzl_open_berth_covenant_desc

Source line: 437.
Before: Admission rules, ration duties, and harbour records are public. Rescue is treated as a binding civic obligation.

After: Admission rules, ration duties, and harbour lists are public. Rescue is treated as a binding civic obligation.

### fallout_nzl_home_guard_rolls_desc

Source line: 615.
Before: Each district will record trained defenders, issued rifles, and the state where they may be called.

After: Each district will list trained defenders, issued rifles, and the state where they may be called.

### chaosx.fallout.127.d

Source line: 651.
Before: The first complete census reaches Wellington in damp folders carried by patrol launch. Harbour clerks have listed inland families beside sailors still waiting offshore, and the totals exceed the sound berths. The parliament must decide which record carries the force of law.

After: The first complete census reaches Wellington in damp folders carried by patrol launch. Harbour clerks have listed inland families beside sailors still waiting offshore, and the totals exceed the sound berths. The parliament must decide which census roll carries the force of law.

### fallout_usa_federal_continuity_ledger_desc

Source line: 759.
Before: The surviving federal offices compare shelter rolls, state charters, and the sealed records carried out of Washington. The work gives the continuity government a common list of people it can still protect.

After: The surviving federal offices compare shelter rolls, state charters, and the sealed papers carried out of Washington. The work gives the continuity government a common list of people it can still protect.

### fallout_usa_launch_federal_reconstruction_drive_desc

Source line: 803.
Before: The rebuilt compact opens a final capital works program. Trains and a civilian factory are tied up until the federal center can produce more than records and orders.

After: The rebuilt compact opens a final capital works program. Trains and a civilian factory are tied up until the federal center can put its rebuilding orders into practice.

### chaosx.fallout.1030.c.tt

Source line: 819.
Before: Spend Fuel 1, Recognition 2, and Cohesion 2 to test the practice at the field school and issue a shared certificate. The certificate can improve adaptation when the school and wards keep matching records.

After: Spend Fuel 1, Recognition 2, and Cohesion 2 to test the practice at the field school and issue a shared certificate. The certificate can improve adaptation when the school and wards keep matching observations.

### chaosx.fallout.1032.scientific_certification.success.d

Source line: 829.
Before: The field school certifies the practice with matching shelter marks from both roads. Teachers record the river level, food stores, and work rotations without calling the rite a biological test, and the Basin gains a method that can be taught to new ward keepers.

After: The field school certifies the practice with matching shelter marks from both roads. Teachers note the river level, food stores, and work rotations without calling the rite a biological test, and the Basin gains a method that can be taught to new ward keepers.

### chaosx.fallout.1032.scientific_certification.partial.d

Source line: 830.
Before: The field school verifies the shelter and work marks, but fuel runs out before the river record is copied. The certificate is accepted in the school ward while river keepers continue using their older stone count.

After: The field school verifies the shelter and work marks, but fuel runs out before the river notes are copied. The certificate is accepted in the school ward while river keepers continue using their older stone count.

### chaosx.fallout.1032.reject_ritual.failure.d

Source line: 834.
Before: The rejection leaves no common record. Ward leaders take the useful parts of the practice for themselves, food and medicine are counted by separate hands, and the next cold rain finds the Basin arguing over rules no one can date.

After: The rejection leaves no common account. Ward leaders take the useful parts of the practice for themselves, food and medicine are counted by separate hands, and the next cold rain finds the Basin arguing over rules no one can date.

### chaosx.fallout.1034.success.d

Source line: 838.
Before: After the next cold-rain season, the river and hill wards bring matching practice records to the field school. The chosen rule survives a thaw, the foreign witness accepts the account, and elders can teach it without claiming that the Basin follows ordinary biology.

After: After the next cold-rain season, the river and hill wards bring matching practice notes to the field school. The chosen rule survives a thaw, the foreign witness accepts the account, and elders can teach it without claiming that the Basin follows ordinary biology.

### chaosx.fallout.1034.failure.d

Source line: 840.
Before: The delayed review finds a missing witness, a broken storehouse key, and three dates for the same cold-rain crossing. The practice survives only as household advice, while the foreign ward withdraws its recognition from the Basin's record.

After: The delayed review finds a missing witness, a broken storehouse key, and three dates for the same cold-rain crossing. The practice survives only as household advice, while the foreign ward withdraws its recognition from the Basin's practice.

### fallout.event_log.adaptation_rite.detail.civic_rite_failure

Source line: 851.
Before: An ash storm spoiled the civic copies and left the wards without a shared practice record.

After: An ash storm spoiled the civic copies and left the wards without shared practice notes.

### fallout.event_log.adaptation_rite.detail.scientific_certification_partial

Source line: 856.
Before: The field school verified the shelter marks before fuel ran out for the river record.

After: The field school verified the shelter marks before fuel ran out for the river notes.

### fallout.event_log.adaptation_rite.detail.scientific_certification_failure

Source line: 857.
Before: A cracked mirror split the records and broke confidence in the field school.

After: A cracked mirror split the observations and broke confidence in the field school.

### fallout.event_log.adaptation_rite.detail.reject_ritual_failure

Source line: 860.
Before: The rejection left household advice without a dated record for the next cold rain.

After: The rejection left household advice without dated instructions for the next cold rain.

### fallout.event_log.adaptation_rite.detail.callback_success

Source line: 861.
Before: The next thaw confirmed matching practice records and a rule the elders could teach without a biological claim.

After: The next thaw confirmed matching practice notes and a rule the elders could teach without a biological claim.

### chaosx.fallout.536.trade_food.success.d

Source line: 899.
Before: The river market honours the bargain. Grain leaves the storehouse, cartridges arrive before the thaw, and the traders record [This.GetName] as a government that pays.

After: The river market honours the bargain. Grain leaves the storehouse, cartridges arrive before the thaw, and the traders recognize [This.GetName] as a government that pays.

### fallout.event_log.ash_wolves.study_tracks_partial

Source line: 1029.
Before: The field team kept only part of its altered-ecology record.

After: The field team kept only part of its altered-ecology notes.

### chaosx.fallout.314.partial.d

Source line: 1188.
Before: The follow-up finds a network that works when people remember one another. Careful district records sit beside unrecorded loans of spare parts. The settlement can plan its next expansion, but missing repair notes still leave parts of the grid uncertain.

After: The follow-up finds a network that works when people remember one another. Careful district repair notes sit beside unrecorded loans of spare parts. The settlement can plan its next expansion, but missing repair notes still leave parts of the grid uncertain.

### chaosx.fallout.728.close_border.success.d

Source line: 1237.
Before: The East Gate closes before the first convoy reaches the Rime Ward clinic. Guards post a clear return route, nurses receive the medicine they would have spent at the checkpoint, and the neighboring government records the closure as a temporary health measure. Trade slows, yet the frontier remains legible.

After: The East Gate closes before the first convoy reaches the Rime Ward clinic. Guards post a clear return route, nurses receive the medicine they would have spent at the checkpoint, and the neighboring government accepts the closure as a temporary health measure. Trade slows, yet the frontier remains legible.

### chaosx.fallout.728.military_inspection.failure.d

Source line: 1248.
Before: The military screen turns the East Gate into a standoff. Fuel is consumed, the clinic receives no reliable queue, and the neighboring government records the deployment as a warning that may outlast the health emergency.

After: The military screen turns the East Gate into a standoff. Fuel is consumed, the clinic receives no reliable queue, and the neighboring government sees the deployment as a warning that may outlast the health emergency.

### chaosx.fallout.730.success.d

Source line: 1253.
Before: A season later, the East Gate inspection list and the Rime Ward clinic record the same names. The neighboring government honors the inspection lane, and the Quarantine council can describe the compact without pretending that the frontier is safe.

After: A season later, the East Gate inspection list and the Rime Ward clinic list the same patients. The neighboring government honors the inspection lane, and the Quarantine council can describe the compact without pretending that the frontier is safe.

### chaosx.fallout.466.military_pontoon.success.d

Source line: 1301.
Before: Military engineers secured a pontoon lane and repaired the worst approach. The army can move a guarded convoy, while the rail crews record which loads must wait for a permanent bridge.

After: Military engineers secured a pontoon lane and repaired the worst approach. The army can move a guarded convoy, while the rail crews list which loads must wait for a permanent bridge.

### chaosx.fallout.630.joint.success.d

Source line: 1347.
Before: The joint schedule has survived the first arguments on the embankment. Upstream keepers have opened measured gates, village crews have marked the downstream fields, and the shared register now records water as a public duty rather than a private claim.

After: The joint schedule has survived the first arguments on the embankment. Upstream keepers have opened measured gates, village crews have marked the downstream fields, and the shared water rules make supplies a public duty instead of a private claim.

### chaosx.fallout.630.joint.failure.d

Source line: 1349.
Before: The joint schedule broke when the field lists did not match the gate records. Water remains trapped behind a damaged control point, the downstream villages have begun rationing, and the first people have died.

After: The joint schedule broke when the field lists did not match the gate schedules. Water remains trapped behind a damaged control point, the downstream villages have begun rationing, and the first people have died.

### chaosx.fallout.632.failure.d

Source line: 1364.
Before: The seasonal review finds broken gate records and a state that cannot promise the next release. Disease, damaged works, and private diversions have turned the first schedule into a warning carried from one dry field to another.

After: The seasonal review finds broken gate schedules and a state that cannot promise the next release. Disease, damaged works, and private diversions have turned the first schedule into a warning carried from one dry field to another.

### fallout.event_log.canal_schedule.joint_failure

Source line: 1384.
Before: The joint schedule broke over field lists and gate records.

After: The joint schedule broke over field lists and gate schedules.

### fallout.event_log.canal_schedule.callback_failure

Source line: 1396.
Before: The seasonal review found broken records, damaged works, and no promise for the next release.

After: The seasonal review found broken gate schedules, damaged works, and no promise for the next release.

### chaosx.fallout.436.c.tt

Source line: 1532.
Before: Spend food, medicine, recognition, and cohesion to build a school quarter where the cohort keeps its languages and records.

After: Spend food, medicine, recognition, and cohesion to build a school quarter where the cohort keeps its languages and family papers.

### chaosx.fallout.438.grant_citizenship.partial.d

Source line: 1536.
Before: The town records the children, but several offices keep the old family names in a separate drawer. The cohort can draw rations and attend lessons, though a border guard still asks where they belong.

After: The town enrolls the children, but several offices keep the old family names in a separate drawer. The cohort can draw rations and attend lessons, though a border guard still asks where they belong.

### chaosx.fallout.438.foster_communities.success.d

Source line: 1538.
Before: Local households open rooms without erasing the children's family names. A baker keeps the language of one rail camp, a mechanic teaches another child to read a gauge, and the shelter council records every foster promise.

After: Local households open rooms without erasing the children's family names. A baker keeps the language of one rail camp, a mechanic teaches another child to read a gauge, and the shelter council checks every foster promise.

### chaosx.fallout.438.foster_communities.failure.d

Source line: 1540.
Before: Foster promises become a market for labour. The council finds children moved between houses without records, and families who arrived together begin to lose one another in the new town.

After: Foster promises become a market for labour. The council finds children moved between houses without custody papers, and families who arrived together begin to lose one another in the new town.

### chaosx.fallout.440.failure.d

Source line: 1552.
Before: The review finds a cohort divided by missing records, closed classrooms, and promises that were never kept. The children remember the shelter, but they no longer agree on what should follow it.

After: The review finds a cohort divided by missing family papers, closed classrooms, and promises that were never kept. The children remember the shelter, but they no longer agree on what should follow it.

### fallout.event_log.children_from_elsewhere.foster_communities_failure

Source line: 1562.
Before: Foster promises became a labour market and family records were lost.

After: Foster promises became a labour market and family papers were lost.

### fallout.event_log.children_from_elsewhere.build_school_quarter_success

Source line: 1563.
Before: A school quarter preserved languages, names, and practical records in the old freight depot.

After: A school quarter preserved the children's languages, names, and family papers in the old freight depot.

### fallout.event_log.children_from_elsewhere.callback_failure

Source line: 1571.
Before: The first home year left the cohort divided by missing records and closed classrooms.

After: The first home year left the cohort divided by missing family papers and closed classrooms.

### chaosx.fallout.735.reform.success.d

Source line: 1588.
Before: The young registrars opened the old movement law line by line. A permit now records the route, the shelter receiving its traveller, and the public duty that made the crossing possible. The first cohort has turned protest into a civic apprenticeship.

After: The young registrars opened the old movement law line by line. A permit now names the route, the shelter receiving its traveller, and the public duty that made the crossing possible. The first cohort has turned protest into a civic apprenticeship.

### chaosx.fallout.1037.a.tt

Source line: 1647.
Before: Spend Food 2, Medicine 2, and Recognition 2 to teach the river and hill children under one charter. A shared school can build confidence when both wards keep the same attendance and food record.

After: Spend Food 2, Medicine 2, and Recognition 2 to teach the river and hill children under one charter. A shared school can build confidence when both wards keep the same attendance roll and ration tally.

### chaosx.fallout.1037.b.tt

Source line: 1649.
Before: Spend Scrap 1, Power 1, and Recognition 2 to keep a river school and a hill school with separate storekeepers. Separate rooms can protect local practice, but the two records may drift apart.

After: Spend Scrap 1, Power 1, and Recognition 2 to keep a river school and a hill school with separate storekeepers. Separate rooms can protect local practice, but their attendance rolls may drift apart.

### chaosx.fallout.1039.separate_institutions.partial.d

Source line: 1659.
Before: Separate schools protect the hill lessons, but the river storekeeper cannot copy the attendance book before the ash road closes. The wards keep their rooms and agree to compare records after the next thaw.

After: Separate schools protect the hill lessons, but the river storekeeper cannot copy the attendance book before the ash road closes. The wards keep their rooms and agree to compare attendance books after the next thaw.

### chaosx.fallout.1039.separate_institutions.failure.d

Source line: 1660.
Before: Separate institutions turn into separate claims over the children. The hill guard locks the storehouse, the river school loses its power cell, and the two records describe different ages for the same class.

After: Separate institutions turn into separate claims over the children. The hill guard locks the storehouse, the river school loses its power cell, and the two attendance books give different ages for the same class.

### chaosx.fallout.1039.local_autonomy.success.d

Source line: 1661.
Before: The Basin grants each settlement a youth council with authority over lessons, work rotations, and shelter duty. The councils exchange one teacher each wet month, and the foreign witness records a rule for settling disputes without moving children by force.

After: The Basin grants each settlement a youth council with authority over lessons, work rotations, and shelter duty. The councils exchange one teacher each wet month, and the foreign witness accepts a rule for settling disputes without moving children by force.

### chaosx.fallout.1039.local_autonomy.partial.d

Source line: 1662.
Before: Local autonomy reduces travel through the cold rain, but the hill council cannot spare a teacher for the river ward. Both settlements keep their own lessons and ask the foreign witness to compare the first spring records.

After: Local autonomy reduces travel through the cold rain, but the hill council cannot spare a teacher for the river ward. Both settlements keep their own lessons and ask the foreign witness to compare the first spring attendance books.

### chaosx.fallout.1041.success.d

Source line: 1670.
Before: After the next wet season, the first class returns with matching attendance marks and a shared movement register. The river and hill wards keep the chosen arrangement, and the foreign witness accepts the Basin's record as a civic rule for the next generation.

After: After the next wet season, the first class returns with matching attendance marks and a shared movement register. The river and hill wards keep the chosen arrangement, and the foreign witness accepts the Basin's practice as a civic rule for the next generation.

### chaosx.fallout.1041.failure.d

Source line: 1672.
Before: The delayed review finds a missing guardian, a broken storehouse key, and two records for the same class. The wards stop the exchange, the foreign witness withdraws recognition, and the next children inherit a border made from school enrolment rules.

After: The delayed review finds a missing guardian, a broken storehouse key, and two attendance books for the same class. The wards stop the exchange, the foreign witness withdraws recognition, and the next children inherit a border made from school enrolment rules.

### fallout.event_log.children_of_two_settlements.detail.equal_public_school_success

Source line: 1681.
Before: One public school joined the river and hill wards under shared attendance, food, and medicine records.

After: One public school joined the river and hill wards under shared attendance rolls, ration tallies, and medicine lists.

### fallout.event_log.children_of_two_settlements.detail.separate_institutions_success

Source line: 1684.
Before: Separate schools kept local lessons while an exchange book gave the foreign witness a common record.

After: Separate schools kept local lessons while an exchange book gave the foreign witness a common account.

### fallout.event_log.children_of_two_settlements.detail.local_autonomy_failure

Source line: 1689.
Before: Local councils guarded their own stores and ended the exchange before a shared record existed.

After: Local councils guarded their own stores and ended the exchange before a shared attendance roll existed.

### fallout.event_log.children_of_two_settlements.detail.callback_failure

Source line: 1695.
Before: A missing guardian and broken storehouse key turned school records into a border.

After: A missing guardian and broken storehouse key turned school attendance books into a border.

### chaosx.fallout.721.standard.success.d

Source line: 1733.
Before: The Ash Ward seal and the North Gate seal are finally the same mark. Three checkpoints accept one inspection record, and a traveler can cross the eastern road without telling the story of the fever again.

After: The Ash Ward seal and the North Gate seal are finally the same mark. Three checkpoints accept one inspection certificate, and a traveler can cross the eastern road without telling the story of the fever again.

### fallout.event_log.clean_certificate.detail.political_weapon_failure

Source line: 1758.
Before: The council's certificate refusals became a new grievance record.

After: The council's certificate refusals became a new grievance.

### chaosx.fallout.882.medical_oversight.success.d

Source line: 1788.
Before: The clinic board publishes one intake slate and signs it beside the river pumps. Ward captains can appeal, but the board answers every appeal with a named clerk, a ration count, and a care record that the foreign witness can read.

After: The clinic board publishes one intake slate and signs it beside the river pumps. Ward captains can appeal, but the board answers every appeal with a named clerk, a ration count, and a care plan that the foreign witness can read.

### chaosx.fallout.882.medical_oversight.failure.d

Source line: 1790.
Before: The board took custody of the medicine stores but never agreed on an intake rule. Families queue under three competing slates, and the foreign witness records a clinic that can count supplies without deciding whom it serves.

After: The board took custody of the medicine stores but never agreed on an intake rule. Families queue under three competing slates, and the foreign witness sees a clinic that can count supplies without deciding whom it serves.

### chaosx.fallout.882.joint_rule.success.d

Source line: 1794.
Before: The paired seal works. A clinic clerk records the need, a ward delegate records consent, and both names travel with the supply cart. The Basin can answer the foreign witness without giving either office unchecked power.

After: The paired seal works. A clinic clerk lists each family's needs, a ward delegate confirms consent, and both names travel with the supply cart. The Basin can answer the foreign witness without giving either office unchecked power.

### chaosx.fallout.1044.b.tt

Source line: 1851.
Before: Spend Scrap 1, Power 1, and Recognition 2 to reserve half the seats for named guardians from both wards. The arrangement protects records and routes, but older ward keepers may keep the first cohort from setting its own priorities.

After: Spend Scrap 1, Power 1, and Recognition 2 to reserve half the seats for named guardians from both wards. The arrangement protects the ward rolls and travel routes, but older ward keepers may keep the first cohort from setting its own priorities.

### chaosx.fallout.1046.youth_council.success.d

Source line: 1857.
Before: The first cohort holds a ballot beneath the ferry canopy and elects two delegates from each ward. Their register records the same names in river and hill hands, and the foreign witness accepts the council as a public authority for shelter duty and school repair.

After: The first cohort holds a ballot beneath the ferry canopy and elects two delegates from each ward. Their register lists the same names in river and hill hands, and the foreign witness accepts the council as a public authority for shelter duty and school repair.

### chaosx.fallout.1046.youth_council.failure.d

Source line: 1859.
Before: The first ballot loses its seal when the ferry shelter floods. A guardian carries the hill list uphill, the river list names different delegates, and the cohort learns that a vote without a dry record can become another border.

After: The first ballot loses its seal when the ferry shelter floods. A guardian carries the hill list uphill, the river list names different delegates, and the cohort learns that a vote without a dry ballot book can become another border.

### chaosx.fallout.1046.guardian_seats.partial.d

Source line: 1861.
Before: Reserved guardian seats protect the records, but the hill ward cannot send a second keeper through the ash road. The cohort receives a partial voice and agrees to review the balance when the power cell is repaired.

After: Reserved guardian seats protect the ward rolls, but the hill ward cannot send a second keeper through the ash road. The cohort receives a partial voice and agrees to review the balance when the power cell is repaired.

### chaosx.fallout.1046.guardian_seats.failure.d

Source line: 1862.
Before: Guardian seats become a permanent lock on the assembly. The old ward lists decide who may speak, the cohort stops attending the ferry meetings, and the foreign witness records a council that has preserved order by refusing succession.

After: Guardian seats become a permanent lock on the assembly. The old ward lists decide who may speak, the cohort stops attending the ferry meetings, and the foreign witness sees a council that has preserved order by refusing succession.

### fallout.event_log.cohorts_first_ballot.detail.youth_council_success

Source line: 1883.
Before: A ferry-canopy ballot gave the first cohort a public council with matching ward records.

After: A ferry-canopy ballot gave the first cohort a public council with matching ward rolls.

### fallout.event_log.cohorts_first_ballot.detail.guardian_seats_success

Source line: 1886.
Before: Guardian seats protected the records while cohort delegates gained a written ration question.

After: Guardian seats protected the ward rolls while cohort delegates gained a written ration question.

### chaosx.fallout.389.public_trial.failure.d

Source line: 1927.
Before: The test exposed the fraud after the ward had already used the worst vials. Nurses record the losses in a book that the traders cannot confiscate. The freight clinic has lost its stock and its promise.

After: The test exposed the fraud after the ward had already used the worst vials. Nurses name those who died in a book that the traders cannot confiscate. The freight clinic has lost its stock and its promise.

### chaosx.fallout.391.failure.d

Source line: 1942.
Before: The next batch fails in the strongest ward. The clinic burns the labels, not the records. A fever returns to the freight road and the garrison begins counting medicine as a military secret.

After: The next batch fails in the strongest ward. The clinic burns the labels and keeps the case notes. A fever returns to the freight road and the garrison begins counting medicine as a military secret.

### fallout.event_log.dead_city_permit.callback_failure

Source line: 2070.
Before: The permit review failed after filters and records were lost at the city road.

After: The permit review failed after filters and salvage lists were lost at the city road.

### chaosx.fallout.707.tech.success.d

Source line: 2140.
Before: The civil council signed the hospital charter and accepted medical rule. Clinic orders now carry state authority, and the Quarantine State has entered a technate arrangement that keeps infection records above factional bargaining.

After: The civil council signed the hospital charter and accepted medical rule. Clinic orders now carry state authority, and the Quarantine State has entered a technate arrangement that keeps infection findings above factional bargaining.

### chaosx.fallout.707.arrest.failure.d

Source line: 2148.
Before: The arrest party reached the hospital after the medical board had moved its patients and records into the snow tunnels. The council lost the confrontation, and every clinic now treats the warrant as proof that the state will use force against care.

After: The arrest party reached the hospital after the medical board had moved its patients and case files into the snow tunnels. The council lost the confrontation, and every clinic now treats the warrant as proof that the state will use force against care.

### chaosx.fallout.707.vote.success.d

Source line: 2149.
Before: Ward delegates counted the vote under the hospital's green lamps. The result gave the civil council a public mandate, protected the medical board's treatment authority, and placed the quarantine timetable in a record that every district could read.

After: Ward delegates counted the vote under the hospital's green lamps. The result gave the civil council a public mandate, protected the medical board's treatment authority, and placed the quarantine timetable in a public charter that every district could read.

### chaosx.fallout.709.success.d

Source line: 2155.
Before: Eight months later, the hospital charter still answers to one public record. Fever teams share their reports with the civil office, and the Quarantine State can close a road without turning every clinic into a rival government.

After: Eight months later, the hospital still follows the public charter. Fever teams share their reports with the civil office, and the Quarantine State can close a road without turning every clinic into a rival government.

### chaosx.fallout.709.failure.d

Source line: 2157.
Before: The settlement broke under fatigue and missing records. The medical board and civil council now issue separate orders, and each ward must decide whether a hospital seal or a public vote grants the right to close its road.

After: The settlement broke under fatigue and missing clinic files. The medical board and civil council now issue separate orders, and each ward must decide whether a hospital seal or a public vote grants the right to close its road.

### fallout.event_log.doctors_coup.detail.callback_success

Source line: 2178.
Before: The hospital charter survived another winter and remained answerable to one public record.

After: The hospital followed the public charter through another winter.

### chaosx.fallout.240.partial.d

Source line: 2233.
Before: The delayed audit at [?fallout_event_230_destination_state_id.GetName] found a working record with a contested margin. The doors have a memory now, although the districts still argue over whose names belong on it.

After: The delayed audit at [?fallout_event_230_destination_state_id.GetName] found a working admission rule with disputed limits. Families can seek shelter, but the districts still argue over who should enter.

### chaosx.fallout.240.failure.d

Source line: 2234.
Before: The delayed audit at [?fallout_event_230_destination_state_id.GetName] found a record that could not carry the next winter shift. Recognition and cohesion fell again, and the shelter will remember the admission as a warning rather than a settlement.

After: The delayed audit at [?fallout_event_230_destination_state_id.GetName] found a shelter admission rule too weak for the next winter shift. Recognition and cohesion fell again, and the shelter will remember the admission as a warning rather than a settlement.

### fallout.event_log.door_list.detail.callback_partial

Source line: 2253.
Before: The delayed audit found a working but contested door record.

After: The delayed audit found a working but contested shelter admission rule.

### fallout.event_log.door_list.detail.callback_failure

Source line: 2254.
Before: The delayed audit found a door record too weak for the next winter shift.

After: The delayed audit found a shelter admission rule too weak for the next winter shift.

### chaosx.fallout.443.a.tt

Source line: 2265.
Before: Spend food, medicine, recognition, and cohesion to restore family houses and record property claims.

After: Spend food, medicine, recognition, and cohesion to restore family houses and list property claims.

### chaosx.fallout.445.a.tt

Source line: 2283.
Before: The settlement takes effect, its migration and border terms enter the public record, and a formal review begins after 540 days.

After: The settlement takes effect, its migration and border terms are made public, and a formal review begins after 540 days.

### chaosx.fallout.447.a.tt

Source line: 2289.
Before: The settlement review closes, its migration record remains public, and no further follow-up is required.

After: The settlement review closes, its migration terms remain public, and no further follow-up is required.

### chaosx.fallout.298.research.success.d

Source line: 2326.
Before: The clinic kept the fever records beside clean instruments and a working lamp. Its staff can compare exposure, sanitation, and recovery without turning the former dormitory into a private archive.

After: The clinic kept the fever case notes beside clean instruments and a working lamp. Its staff can compare exposure, sanitation, and recovery without turning the former dormitory into a private archive.

### fallout.event_log.empty_ward.detail.research_success

Source line: 2350.
Before: A research clinic kept fever records beside clean instruments and a public duty to the shelters.

After: A research clinic kept fever case notes beside clean instruments and a public duty to the shelters.

### fallout.event_log.empty_ward.detail.callback_success

Source line: 2359.
Before: The former dormitory became an institution with a keeper, records, and a place in the next emergency plan.

After: The former dormitory became an institution with a keeper, case files, and a place in the next emergency plan.

### fallout_empty_ward_research_desc

Source line: 2366.
Before: A research clinic keeps exposure and sanitation records beside a public medical duty.

After: A research clinic keeps exposure and sanitation notes beside a public medical duty.

### fallout_empty_ward_maintained_desc

Source line: 2372.
Before: A maintained institution gives the next emergency a keeper, records, and a supply route.

After: A maintained institution gives the next emergency a keeper, case files, and a supply route.

### fallout_empty_ward_failed_desc

Source line: 2374.
Before: A strained institution leaves beds, records, and medicine exposed to another public failure.

After: A strained institution leaves beds, case files, and medicine exposed to another public failure.

### chaosx.fallout.6.marker_success.d

Source line: 2565.
Before: Road wardens in [air_winter_event_state.GetName] planted tall white poles above the drifts and stocked fuel, rope, and lamps at each dangerous bend. Signed waybills show supply convoys crossing the pass without losing the marked line, giving repair crews a dependable route into isolated settlements. The convoy record is presented to [ROOT.GetAirWinterGovernmentAuthority] by [ROOT.GetAirWinterGovernmentOfficial].

After: Road wardens in [air_winter_event_state.GetName] planted tall white poles above the drifts and stocked fuel, rope, and lamps at each dangerous bend. Signed waybills show supply convoys crossing the pass without losing the marked line, giving repair crews a dependable route into isolated settlements. The convoy waybills are presented to [ROOT.GetAirWinterGovernmentAuthority] by [ROOT.GetAirWinterGovernmentOfficial].

### chaosx.fallout.15.failure.d

Source line: 2686.
Before: The escorted patrol from [air_winter_event_state.GetName] met freezing spray beyond the coastal lights. Several boats limped home with injured crews, while others left only broken radio calls and empty berths for the harbor office to record.

After: The escorted patrol from [air_winter_event_state.GetName] met freezing spray beyond the coastal lights. Several boats limped home with injured crews, while others left only broken radio calls and empty berths for the harbor office to count.

### chaosx.fallout.38.a.tt

Source line: 2922.
Before: Requires at least §Y[?constant:air_winter_event_country.manpower_moderate|0]§! available Manpower and §Y[?constant:air_winter_event_country.island_refugee_convoy_cost|0]§! Convoys. We spend §R[?constant:air_winter_event_country.manpower_moderate|0]§! available Manpower and §R[?constant:air_winter_event_country.island_refugee_convoy_cost|0]§! Convoys. Rescue launches and shore crews land a number equal to §Y[?constant:air_winter_event_island_refugee.rescue_population_share|%0]§! of the current population of §Y[air_winter_event_state.GetName]§!, up to §Y[?constant:air_winter_event_island_refugee.rescue_population_ceiling|0]§! people. §Y[air_winter_refugee_source_state.GetName]§! loses exactly the number received by §Y[air_winter_event_state.GetName]§!, subject to a protected remainder of §Y[?constant:air_winter_event_island_refugee.protected_source_remainder|0]§! people. In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_major|0]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_major|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_major|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!. Refugee Pressure in §Y[air_winter_refugee_source_state.GetName]§! falls by §G[?constant:air_winter_event_ledger.refugees_major|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_major|%1]§!. The state records voluntary open-shore admission, the receiving country keeps an open-shore record, and [air_winter_refugee_source_country.GetNameDef] records an organized departure. A harbor report arrives after §Y[?constant:air_winter_event_runtime.delayed_standard_days|0] days§!. The rescue harbor succeeds only if Food Reserve is at least §Y[?constant:air_winter_event_outcome.island_refugee_rescue_food_minimum|0]§!, Shelter Capacity is at least §Y[?constant:air_winter_event_outcome.island_refugee_rescue_shelter_minimum|0]§!, Disease Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_rescue_disease_ceiling|0]§!, and Refugee Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_rescue_pressure_ceiling|0]§!.

After: Requires at least §Y[?constant:air_winter_event_country.manpower_moderate|0]§! available Manpower and §Y[?constant:air_winter_event_country.island_refugee_convoy_cost|0]§! Convoys. We spend §R[?constant:air_winter_event_country.manpower_moderate|0]§! available Manpower and §R[?constant:air_winter_event_country.island_refugee_convoy_cost|0]§! Convoys. Rescue launches and shore crews land a number equal to §Y[?constant:air_winter_event_island_refugee.rescue_population_share|%0]§! of the current population of §Y[air_winter_event_state.GetName]§!, up to §Y[?constant:air_winter_event_island_refugee.rescue_population_ceiling|0]§! people. §Y[air_winter_refugee_source_state.GetName]§! loses exactly the number received by §Y[air_winter_event_state.GetName]§!, subject to a protected remainder of §Y[?constant:air_winter_event_island_refugee.protected_source_remainder|0]§! people. In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_major|0]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_major|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_major|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_moderate|0]§!, and §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!. Refugee Pressure in §Y[air_winter_refugee_source_state.GetName]§! falls by §G[?constant:air_winter_event_ledger.refugees_major|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_major|%1]§!. The state admits the passengers freely, the receiving country accepts responsibility for the landing, and [air_winter_refugee_source_country.GetNameDef] confirms an organized departure. A harbor report arrives after §Y[?constant:air_winter_event_runtime.delayed_standard_days|0] days§!. The rescue harbor succeeds only if Food Reserve is at least §Y[?constant:air_winter_event_outcome.island_refugee_rescue_food_minimum|0]§!, Shelter Capacity is at least §Y[?constant:air_winter_event_outcome.island_refugee_rescue_shelter_minimum|0]§!, Disease Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_rescue_disease_ceiling|0]§!, and Refugee Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_rescue_pressure_ceiling|0]§!.

### chaosx.fallout.38.b.tt

Source line: 2924.
Before: Requires at least §Y[?constant:air_winter_event_country.manpower_minor|0]§! available Manpower and §Y[?constant:air_winter_event_country.support_equipment_crew_cost|0]§! Support Equipment. We spend §R[?constant:air_winter_event_country.manpower_minor|0]§! available Manpower and §R[?constant:air_winter_event_country.support_equipment_crew_cost|0]§! Support Equipment. Screened passengers enter guarded landing camps in a number equal to §Y[?constant:air_winter_event_island_refugee.quarantine_population_share|%0]§! of the current population of §Y[air_winter_event_state.GetName]§!, up to §Y[?constant:air_winter_event_island_refugee.quarantine_population_ceiling|0]§! people. §Y[air_winter_refugee_source_state.GetName]§! loses exactly the number received by §Y[air_winter_event_state.GetName]§!, subject to a protected remainder of §Y[?constant:air_winter_event_island_refugee.protected_source_remainder|0]§! people. In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_minor|0]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_minor|0]§!, §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_minor|0]§!, and §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!. Refugee Pressure in §Y[air_winter_refugee_source_state.GetName]§! falls by §G[?constant:air_winter_event_ledger.refugees_moderate|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!. The state records voluntary controlled admission under shore quarantine, the receiving country keeps a quarantine-station record, and [air_winter_refugee_source_country.GetNameDef] records a screened departure. A quarantine report arrives after §Y[?constant:air_winter_event_runtime.delayed_standard_days|0] days§!. The cordon succeeds only if Water Security is at least §Y[?constant:air_winter_event_outcome.island_refugee_quarantine_water_minimum|0]§!, Disease Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_quarantine_disease_ceiling|0]§!, Building Damage Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_quarantine_damage_ceiling|0]§!, and Refugee Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_quarantine_pressure_ceiling|0]§!.

After: Requires at least §Y[?constant:air_winter_event_country.manpower_minor|0]§! available Manpower and §Y[?constant:air_winter_event_country.support_equipment_crew_cost|0]§! Support Equipment. We spend §R[?constant:air_winter_event_country.manpower_minor|0]§! available Manpower and §R[?constant:air_winter_event_country.support_equipment_crew_cost|0]§! Support Equipment. Screened passengers enter guarded landing camps in a number equal to §Y[?constant:air_winter_event_island_refugee.quarantine_population_share|%0]§! of the current population of §Y[air_winter_event_state.GetName]§!, up to §Y[?constant:air_winter_event_island_refugee.quarantine_population_ceiling|0]§! people. §Y[air_winter_refugee_source_state.GetName]§! loses exactly the number received by §Y[air_winter_event_state.GetName]§!, subject to a protected remainder of §Y[?constant:air_winter_event_island_refugee.protected_source_remainder|0]§! people. In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_minor|0]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_moderate|0]§!, §YDisease Pressure§! rises by §R[?constant:air_winter_event_ledger.disease_minor|0]§!, §YBuilding Damage Pressure§! rises by §R[?constant:air_winter_event_ledger.building_pressure_minor|0]§!, and §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!. Refugee Pressure in §Y[air_winter_refugee_source_state.GetName]§! falls by §G[?constant:air_winter_event_ledger.refugees_moderate|0]§!. National Stability falls by §R[?constant:air_winter_event_country.stability_moderate|%1]§!. The state admits screened passengers under shore quarantine, the receiving country accepts responsibility for the quarantine station, and [air_winter_refugee_source_country.GetNameDef] confirms a screened departure. A quarantine report arrives after §Y[?constant:air_winter_event_runtime.delayed_standard_days|0] days§!. The cordon succeeds only if Water Security is at least §Y[?constant:air_winter_event_outcome.island_refugee_quarantine_water_minimum|0]§!, Disease Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_quarantine_disease_ceiling|0]§!, Building Damage Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_quarantine_damage_ceiling|0]§!, and Refugee Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_quarantine_pressure_ceiling|0]§!.

### chaosx.fallout.38.c.tt

Source line: 2926.
Before: Most boats are refused, and people already ashore and passengers from disabled craft are landed because they cannot safely be returned to sea. These forced landings equal §Y[?constant:air_winter_event_island_refugee.exclusion_population_share|%2]§! of the current population of §Y[air_winter_event_state.GetName]§!, up to §Y[?constant:air_winter_event_island_refugee.exclusion_population_ceiling|0]§! people. §Y[air_winter_refugee_source_state.GetName]§! loses exactly the number received by §Y[air_winter_event_state.GetName]§!, subject to a protected remainder of §Y[?constant:air_winter_event_island_refugee.protected_source_remainder|0]§! people. In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_minor|0]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!, and §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!. Refugee Pressure in §Y[air_winter_refugee_source_state.GetName]§! falls by §G[?constant:air_winter_event_ledger.refugees_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!. The state records the forced landing, the receiving country keeps a closed-waters record, and [air_winter_refugee_source_country.GetNameDef] records that most of the fleet was refused. A patrol report arrives after §Y[?constant:air_winter_event_runtime.delayed_standard_days|0] days§!. The exclusion line holds only if Adaptation is at least §Y[?constant:air_winter_event_outcome.island_refugee_exclusion_adaptation_minimum|0]§!, Exposure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_exclusion_exposure_ceiling|0]§!, and Refugee Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_exclusion_pressure_ceiling|0]§!.

After: Most boats are refused, and people already ashore and passengers from disabled craft are landed because they cannot safely be returned to sea. These forced landings equal §Y[?constant:air_winter_event_island_refugee.exclusion_population_share|%2]§! of the current population of §Y[air_winter_event_state.GetName]§!, up to §Y[?constant:air_winter_event_island_refugee.exclusion_population_ceiling|0]§! people. §Y[air_winter_refugee_source_state.GetName]§! loses exactly the number received by §Y[air_winter_event_state.GetName]§!, subject to a protected remainder of §Y[?constant:air_winter_event_island_refugee.protected_source_remainder|0]§! people. In §Y[air_winter_event_state.GetName]§!, §YFood Reserve§! falls by §R[?constant:air_winter_event_ledger.food_minor|0]§!, §YShelter Capacity§! falls by §R[?constant:air_winter_event_ledger.shelter_minor|0]§!, §YRefugee Pressure§! rises by §R[?constant:air_winter_event_ledger.refugees_minor|0]§!, §YExposure§! rises by §R[?constant:air_winter_event_ledger.exposure_moderate|0]§!, and §YAdaptation§! rises by §G[?constant:air_winter_event_ledger.adaptation_minor|0]§!. Refugee Pressure in §Y[air_winter_refugee_source_state.GetName]§! falls by §G[?constant:air_winter_event_ledger.refugees_minor|0]§!. National Stability rises by §G[?constant:air_winter_event_country.stability_minor|%1]§!. The state receives passengers who cannot safely stay at sea, the receiving country maintains the exclusion line, and [air_winter_refugee_source_country.GetNameDef] knows that most of the fleet was refused. A patrol report arrives after §Y[?constant:air_winter_event_runtime.delayed_standard_days|0] days§!. The exclusion line holds only if Adaptation is at least §Y[?constant:air_winter_event_outcome.island_refugee_exclusion_adaptation_minimum|0]§!, Exposure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_exclusion_exposure_ceiling|0]§!, and Refugee Pressure is no more than §Y[?constant:air_winter_event_outcome.island_refugee_exclusion_pressure_ceiling|0]§!.

### chaosx.fallout.39.rescue_success.d

Source line: 2929.
Before: Thirty days after the boats from [air_winter_refugee_source_state.GetName] in [air_winter_refugee_source_country.GetNameDef] entered [air_winter_event_state.GetName], patrol launches still guide smaller craft between the shore lights and the landing steps. Families have left the quarantine sheds for heated rooms and island households, the food stores retain a workable reserve, and clinics have contained infections brought through the crowded harbor. [ROOT.GetAirWinterGovernmentOfficial] has signed the open-harbor register into the island's winter record.

After: Thirty days after the boats from [air_winter_refugee_source_state.GetName] in [air_winter_refugee_source_country.GetNameDef] entered [air_winter_event_state.GetName], patrol launches still guide smaller craft between the shore lights and the landing steps. Families have left the quarantine sheds for heated rooms and island households, the food stores retain a workable reserve, and clinics have contained infections brought through the crowded harbor. [ROOT.GetAirWinterGovernmentOfficial] has signed the open-harbor register into the island's winter account.

### chaosx.fallout.42.d

Source line: 2978.
Before: A convoy can carry one working archive out of [air_winter_event_state.GetName] before the storage hall loses heat. Agronomists demand seed catalogs and soil records, physicians want case files and medical stores, and engineers ask for survey books and repair drawings. [ROOT.GetAirWinterGovernmentOfficial] must choose what future workers will inherit.

After: A convoy can carry one working archive out of [air_winter_event_state.GetName] before the storage hall loses heat. Agronomists demand seed catalogs and soil notes, physicians want case files and medical stores, and engineers ask for survey books and repair drawings. [ROOT.GetAirWinterGovernmentOfficial] must choose what future workers will inherit.

### chaosx.fallout.48.altered_return.d

Source line: 3016.
Before: The last lamps rose from beneath [air_winter_event_state.GetName] in a formation no dispatcher ordered. Several survivors answer to shared names, recognize sealed rooms they never entered, and bear the same pale ridges across their hands. Physicians record nuclear residue, chemical contamination, and active disease agents in the surrounding blocks, yet none offers an ordinary explanation for what returned. The crews carried a few support kits and trucks to the cordon before the casualty clerks closed the street.

After: The last lamps rose from beneath [air_winter_event_state.GetName] in a formation no dispatcher ordered. Several survivors answer to shared names, recognize sealed rooms they never entered, and bear the same pale ridges across their hands. Physicians find nuclear residue, chemical contamination, and active disease agents in the surrounding blocks, yet none offers an ordinary explanation for what returned. The crews carried a few support kits and trucks to the cordon before the casualty clerks closed the street.

### chaosx.fallout.831.b.tt

Source line: 3145.
Before: Spend Power 2, Scrap 2, and Recognition 1 to keep the error inside the reactor archive. This preserves a clean public record for now, but leaves neighboring councils dependent on private assurances.

After: Spend Power 2, Scrap 2, and Recognition 1 to keep the error inside the reactor archive. This protects the engineers' public reputation for now, but leaves neighboring councils dependent on private assurances.

### chaosx.fallout.833.hide_calculation.partial.d

Source line: 3156.
Before: The archive preserved a single technical record, although two repair crews kept private copies of the overwritten table. The hospital line returned, but the Technate now has to negotiate with witnesses who know what was removed.

After: The archive preserved a single technical account, although two repair crews kept private copies of the overwritten table. The hospital line returned, but the Technate now has to negotiate with witnesses who know what was removed.

### chaosx.fallout.833.hide_calculation.failure.d

Source line: 3157.
Before: The sealed record failed when a relay room lost pressure during the correction. The Technate kept the archive closed, but a dark hospital ward and an empty maintenance roster made the hidden calculation impossible to defend.

After: The concealed calculation failed when a relay room lost pressure during the correction. The Technate kept the archive closed, but a dark hospital ward and an empty maintenance roster made the hidden calculation impossible to defend.

### chaosx.fallout.695.success.d

Source line: 3238.
Before: Six months later the second register is still read beside the first. The wards can challenge a seal without tearing down the clinic, and the Quarantine State's officers inherit a record that names the error and the remedy.

After: Six months later the second register is still read beside the first. The wards can challenge a seal without tearing down the clinic, and the Quarantine State's officers inherit a case file naming the error and remedy.

### fallout.event_log.false_positive.detail.tribunal_success

Source line: 3255.
Before: A public tribunal cleared the households by name and preserved a durable record of the error.

After: A public tribunal cleared the households by name and preserved a lasting account of the error.

### fallout.event_log.false_positive.detail.callback_success

Source line: 3261.
Before: The delayed appeal record survived the next winter and made the seal answerable.

After: The delayed appeal process survived the next winter and made the seal answerable.

### fallout.event_log.false_positive.detail.callback_partial

Source line: 3262.
Before: The delayed appeal record survived only where lamps and medicine held.

After: The delayed appeal process survived only where lamps and medicine held.

### fallout.event_log.false_positive.detail.callback_failure

Source line: 3263.
Before: The delayed appeal record collapsed under fatigue and missing pages.

After: The delayed appeal process collapsed under fatigue and missing pages.

### fallout_false_positive_callback_settled

Source line: 3268.
Before: Appeal record consolidated

After: Appeal Process Established

### fallout_false_positive_callback_partial

Source line: 3269.
Before: Appeal record unresolved

After: Appeal Process Disputed

### fallout_false_positive_callback_failed

Source line: 3270.
Before: Appeal record breached

After: Appeal Process Failed

### chaosx.fallout.480.accept_shortage.success.d

Source line: 3295.
Before: The council accepts a smaller harvest and protects households with the least shelter. Agronomists preserve a reliable frost record, and the ration line holds through the late cold.

After: The council accepts a smaller harvest and protects households with the least shelter. Agronomists preserve reliable frost observations, and the ration line holds through the late cold.

### chaosx.fallout.480.accept_shortage.partial.d

Source line: 3296.
Before: The ration plan prevents panic in the town center, but outlying farms receive less than promised. The state keeps a useful frost record and a sharper memory of the shortage.

After: The ration plan prevents panic in the town center, but outlying farms receive less than promised. The state keeps useful frost observations and a sharper memory of the shortage.

### fallout.event_log.false_spring_losses.accept_shortage_success

Source line: 3317.
Before: A smaller harvest plan protected weak households and preserved a frost record.

After: A smaller harvest plan protected weak households and preserved frost observations.

### chaosx.fallout.970.opening.d

Source line: 3328.
Before: After the Congo Green Basin records a common settlement road, household stewards ask what kind of future the surviving districts can support. Proposals include voluntary aid, a public cohort program, adoption houses, and strict limits on family support. The Basin must decide how to help without turning family life into a state quota.

After: After the Congo Green Basin agrees on a common settlement road, household stewards ask what kind of future the surviving districts can support. Proposals include voluntary aid, a public cohort program, adoption houses, and strict limits on family support. The Basin must decide how to help without turning family life into a state quota.

### chaosx.fallout.970.d.tt

Source line: 3336.
Before: Spend Food 1, Medicine 1, Fuel 1, and Recognition 1 to refuse a public family program while keeping a minimal record for emergency aid.

After: Spend Food 1, Medicine 1, Fuel 1, and Recognition 1 to refuse a public family program while keeping a minimal household list for emergency aid.

### chaosx.fallout.972.voluntary_support.success.d

Source line: 3339.
Before: The voluntary support office funds food, medicine, and a warm room without asking a household to prove what its future should look like. Families choose their own arrangements, and the Basin records help delivered rather than lives counted.

After: The voluntary support office funds food, medicine, and a warm room without asking a household to prove what its future should look like. Families choose their own arrangements, and the Basin counts the aid delivered to each household.

### chaosx.fallout.972.state_program.failure.d

Source line: 3344.
Before: The program office begins measuring compliance instead of service. Families hide their names, the storehouse records become political weapons, and a plan meant to keep children warm creates a new fear of being counted.

After: The program office begins measuring compliance instead of service. Families hide their names, the storehouse ration lists become political weapons, and a plan meant to keep children warm creates a new fear of being counted.

### fallout.event_log.fertility_question.detail.choice_adoption_network

Source line: 3363.
Before: Adoption houses connected guardians, kinship claims, and two-witness records.

After: Adoption houses connected guardians, kinship claims, and statements signed by two witnesses.

### chaosx.fallout.256.d

Source line: 3397.
Before: The dormitory in [?fallout_event_dispatch_issued_target.GetName] has filled beyond its winter register. Coughing has moved from the clinic beds to the cooking room, and the attendants have begun to mark doors with charcoal because the medicine shelf no longer matches the shelter list. [ROOT.GetAirWinterGovernmentOfficial] can quarantine the room, split the bunks, treat people in the open, or hide the fever from the public. Every choice leaves a record in the state.

After: The dormitory in [?fallout_event_dispatch_issued_target.GetName] has filled beyond its winter register. Coughing has moved from the clinic beds to the cooking room, and the attendants have begun to mark doors with charcoal because the medicine shelf no longer matches the shelter list. [ROOT.GetAirWinterGovernmentOfficial] can quarantine the room, split the bunks, treat people in the open, or hide the fever from the public. Every choice leaves a lasting consequence for the state.

### chaosx.fallout.227.partial.d

Source line: 3499.
Before: The delayed audit at [?fallout_event_217_filters_state_id.GetName] found a usable reserve, but the policy still depends on careful rationing. The clinic can train a smaller crew and the household districts have kept their own record of the missing margin.

After: The delayed audit at [?fallout_event_217_filters_state_id.GetName] found a usable reserve, but the policy still depends on careful rationing. The clinic can train a smaller crew and the household districts have kept their own tally of the shortage.

### chaosx.fallout.852.opening.d

Source line: 3594.
Before: The Manchurian Reactor Keeps can keep its clinics and workshops alive only when every gauge agrees. The machine district has copied one voltage table, one axle measure, one parts catalogue, and one radio interval from the records that survived the Fallout winter. Neighboring settlements will follow the table only if the Technate decides who may read it, change it, and profit from it.

After: The Manchurian Reactor Keeps can keep its clinics and workshops alive only when every gauge agrees. The machine district has copied one voltage table, one axle measure, one parts catalogue, and one radio interval from the manuals that survived the Fallout winter. Neighboring settlements will follow the table only if the Technate decides who may read it, change it, and profit from it.

### chaosx.fallout.284.public.success.d

Source line: 3677.
Before: The public hall kept its lamps burning while [ROOT.GetAirWinterGovernmentOfficial] read the clinic record. Families brought food tickets and names for the newborn register, and the death register gained a living countermark.

After: The public hall kept its lamps burning while [ROOT.GetAirWinterGovernmentOfficial] read the birth report. Families brought food tickets and names for the newborn register, and the death register gained a living countermark.

### chaosx.fallout.284.public.failure.d

Source line: 3679.
Before: The public hall lost heat during the reading. The clinic record survived, but the queue broke apart, the medicine shelf emptied, and another night of preventable deaths followed.

After: The public hall lost heat during the reading. The birth report survived, but the queue broke apart, the medicine shelf emptied, and another night of preventable deaths followed.

### chaosx.fallout.284.campaign.success.d

Source line: 3683.
Before: The civic campaign turned one clinic record into a promise that the country can staff. Food stewards, power crews, and new volunteers joined the clinic's work roster, giving the next generation a visible place in the work.

After: The civic campaign brought food stewards, power crews, and new volunteers into the clinic's work roster. The country can staff its promise to the next generation.

### chaosx.fallout.284.campaign.failure.d

Source line: 3685.
Before: The campaign consumed the last reliable lamp before the district reports arrived. The newborn record became a political accusation, while the shelter lost food, power, and confidence in its public count.

After: The campaign consumed the last reliable lamp before the district reports arrived. The birth announcement became a political accusation, while the shelter lost food, power, and confidence in its public count.

### fallout.event_log.first_safe_birth.detail.public_success

Source line: 3701.
Before: The public hall kept the clinic record visible and linked a living child to the death register.

After: The public hall kept the birth report visible and linked a living child to the death register.

### fallout.event_log.first_safe_birth.detail.public_failure

Source line: 3703.
Before: The public reading lost heat and medicine, leaving the clinic record exposed to another night of loss.

After: The public reading lost heat and medicine, leaving the clinic unable to prevent another night of deaths.

### fallout.event_log.first_safe_birth.detail.campaign_success

Source line: 3707.
Before: The civic campaign turned the birth record into staffed work for food, power, and the next generation.

After: The civic campaign brought crews into food, power, and clinic work for the next generation.

### fallout_first_safe_birth_campaign_desc

Source line: 3722.
Before: A public generation campaign turns one clinic record into staffed work for food, power, and the next cohort.

After: The public campaign brings crews into food, power, and clinic work for the next generation.

### chaosx.fallout.471.intro

Source line: 3798.
Before: The air monitors have fallen below the severe winter line, but the thaw has not made the open ground safe. Outside [This.GetName], a clinic has marked one schoolyard lane for a measured hour without respirators. Your government must decide whether to let families step into the light, require masked work shifts, let the clinic test the air at dawn, or keep the shelter sealed until the records clear.

After: The air monitors have fallen below the severe winter line, but the thaw has not made the open ground safe. Outside [This.GetName], a clinic has marked one schoolyard lane for a measured hour without respirators. Your government must decide whether to let families step into the light, require masked work shifts, let the clinic test the air at dawn, or keep the shelter sealed until the monitors confirm safe air.

### chaosx.fallout.777.avoid.partial.d

Source line: 3868.
Before: The port closed its channel and saved fuel, but two families left in small boats to follow the convoy. The council must answer for the missing berth records.

After: The port closed its channel and saved fuel, but two families left in small boats to follow the convoy. The council must answer for the missing berth lists.

### fallout.event_log.ghost_convoy.detail.callback_success

Source line: 3899.
Before: The old sea road kept one route code, berth record, and water signal.

After: The old sea road kept one route code, berth list, and water signal.

### chaosx.fallout.665.open.failure.d

Source line: 3934.
Before: The unilateral opening failed in [?fallout_event_dispatch_issued_target.GetName]. The native port and infrastructure were damaged as the convoy turned back, and the winter register records the loss against the [This.GetFalloutOrientationArchetypeName].

After: The unilateral opening failed in [?fallout_event_dispatch_issued_target.GetName]. The native port and infrastructure were damaged as the convoy turned back, and the winter losses weaken the [This.GetFalloutOrientationArchetypeName].

### chaosx.fallout.782.d.tt

Source line: 4063.
Before: Spend Food 3, Medicine 2, Fuel 2, and Recognition 2 to load families, tools, and berth records onto the convoy route.

After: Spend Food 3, Medicine 2, Fuel 2, and Recognition 2 to load families, tools, and berth lists onto the convoy route.

### chaosx.fallout.784.port_republic.failure.d

Source line: 4068.
Before: The election hall lost power during the count. Garrison clerks carried the berth records away, the hungry districts received no schedule, and the new republic begins under a broken trust memory.

After: The election hall lost power during the count. Garrison clerks carried the berth lists away, the hungry districts received no schedule, and the new republic begins under a broken trust memory.

### chaosx.fallout.784.evacuate.success.d

Source line: 4075.
Before: The harbor loaded families, tools, patient lists, and the lighthouse lens onto three convoy hulls. The empty piers remain a claim on the map, while the survivors carry a precise record of every berth left behind.

After: The harbor loaded families, tools, patient lists, and the lighthouse lens onto three convoy hulls. The empty piers remain a claim on the map, while the survivors carry a precise list of every berth left behind.

### chaosx.fallout.784.evacuate.failure.d

Source line: 4077.
Before: Ash closed the channel before the last hull cleared the reef. Cargo, medicine, and berth records were scattered across the old harbor, leaving the convoy route with more claimants than space.

After: Ash closed the channel before the last hull cleared the reef. Cargo, medicine, and berth lists were scattered across the old harbor, leaving the convoy route with more claimants than space.

### fallout.event_log.harbor_without_city.detail.choice_evacuate

Source line: 4091.
Before: The harbor loaded families, tools, and berth records onto the convoy route.

After: The harbor loaded families, tools, and berth lists onto the convoy route.

### fallout.event_log.harbor_without_city.detail.port_republic_failure

Source line: 4094.
Before: The election failed during the count and garrison clerks took the berth records.

After: The election failed during the count and garrison clerks took the berth lists.

### fallout.event_log.harbor_without_city.detail.evacuate_failure

Source line: 4103.
Before: Ash closed the channel and scattered cargo and berth records across the harbor.

After: Ash closed the channel and scattered cargo and berth lists across the harbor.

### chaosx.fallout.749.client_inspections.success.d

Source line: 4137.
Before: Licensed teams inspected the partner clinics without seizing their stores. The North Gate now recognizes treatment records from the Ash Ward, and inspection reports name the patients instead of hiding them behind a client seal.

After: Licensed teams inspected the partner clinics without seizing their stores. The North Gate now recognizes treatment files from the Ash Ward, and inspection reports name the patients instead of hiding them behind a client seal.

### chaosx.fallout.749.client_inspections.failure.d

Source line: 4139.
Before: The inspection teams treated the partner clinics as evidence rather than patients. Records were copied, medicine was delayed, and the regional network now remembers the Quarantine government as another authority that takes before it helps.

After: The inspection teams treated the partner clinics as evidence rather than patients. Patient files were copied, medicine was delayed, and the regional network now remembers the Quarantine government as another authority that takes before it helps.

### chaosx.fallout.751.partial.d

Source line: 4150.
Before: The delayed review keeps the clinics linked, though partner councils still bargain over records and fuel. Health Without Borders has become a regional promise with a local limit.

After: The delayed review keeps the clinics linked, though partner councils still bargain over patient files and fuel. Health Without Borders has become a regional promise with a local limit.

### fallout.event_log.health_without_borders.choice_client_inspections

Source line: 4166.
Before: The council licensed client inspections and published partner-clinic records.

After: The council licensed client inspections and published partner-clinic files.

### fallout.event_log.health_without_borders.client_inspections_failure

Source line: 4174.
Before: Inspection teams copied records while patients waited for delayed medicine.

After: Inspection teams copied patient files while patients waited for delayed medicine.

### fallout.event_log.health_without_borders.callback_partial

Source line: 4182.
Before: The delayed review kept clinics linked while partners still bargained over records and fuel.

After: The delayed review kept clinics linked while partners still bargained over patient files and fuel.

### fallout_hungry_battalion_field_requisition_desc

Source line: 4266.
Before: Patrols collect food along their routes while farm districts record the coercion.

After: Patrols collect food along their routes while farm districts report the coercion.

### chaosx.fallout.494.use_untreated_water.success.d

Source line: 4289.
Before: The untreated meltwater reached the wards before dawn. The clinic kept its lamps and the water board marked every household that accepted the risk, leaving a public record for the next thaw.

After: The untreated meltwater reached the wards before dawn. The clinic kept its lamps and the water board marked every household that accepted the risk, leaving a public risk warning for the next thaw.

### chaosx.fallout.109.failure.d

Source line: 4416.
Before: The gate jams under the first pressure surge. Ash and river water enter the lower tanks together, and the clinic register records the first deaths from a source that was supposed to be sealed.

After: The gate jams under the first pressure surge. Ash and river water enter the lower tanks together, and the clinic lists the first deaths from a source that was supposed to be sealed.

### chaosx.fallout.117.success.d

Source line: 4502.
Before: The labor order reaches the line before the dispatch office closes. The crews move sleepers and rail through the night, restoring a usable corridor and sending three trains toward the fuel yards. The work is efficient, but every district clerk has copied the order into the government record.

After: The labor order reaches the line before the dispatch office closes. The crews move sleepers and rail through the night, restoring a usable corridor and sending three trains toward the fuel yards. The work is efficient, but every district clerk has copied the order into the government archive.

### fallout_rail_atrocity_memory_desc

Source line: 4542.
Before: The labor order remains in the government record, and every later rail requisition is judged against the crews who were forced to work it.

After: The labor order remains in the government archive, and every later rail requisition is judged against the crews who were forced to work it.

### fallout.event_log.rail_crew.detail.forced_success

Source line: 4549.
Before: A forced labor order restored a usable corridor and moved trains toward the fuel yards, leaving a permanent government record.

After: A forced labor order restored a usable corridor and moved trains toward the fuel yards. Copies of the order remained in the government archive.

### chaosx.fallout.840.service_tiers.partial.d

Source line: 4614.
Before: The service ladder kept the grid staffed, but a failed relay erased one district's night hours. The Keeps restored the missing records and left that district on review status until its crews could prove their next season of work.

After: The service ladder kept the grid staffed, but a failed relay erased one district's night hours. The Keeps restored the missing work logs and left that district on review status until its crews could prove their next season of work.

### chaosx.fallout.253.failure.d

Source line: 4712.
Before: The emergency arrangement leaves a liability in the state record. The crews know which rooms went dark, and the next repair will begin under that memory.

After: The emergency arrangement left rooms without power. The crews know which shelters went dark, and the next repair must answer for that failure.

### chaosx.fallout.845.opening.d

Source line: 4823.
Before: The civic register gave the Manchurian Reactor Keeps a wider school and a harder question. A damaged planning machine has begun issuing recommendations for clinic hours, rail repairs, and food convoys, using records that survived the first Fallout winter. The Technate must decide whether to follow the suggestion, test it in a sealed district, reject it for a human review, or grant the machine a public advisory seat.

After: The civic register gave the Manchurian Reactor Keeps a wider school and a harder question. A damaged planning machine has begun issuing recommendations for clinic hours, rail repairs, and food convoys, using files that survived the first Fallout winter. The Technate must decide whether to follow the suggestion, test it in a sealed district, reject it for a human review, or grant the machine a public advisory seat.

### chaosx.fallout.847.follow_recommendation.success.d

Source line: 4834.
Before: The machine's recommendation moved clinic hours and rail repairs across the Manchurian Reactor Keeps without losing a single signed household roll. The output gain gave the Technate a reason to trust its surviving records, while human supervisors retained the right to stop a dangerous order.

After: The machine's recommendation moved clinic hours and rail repairs across the Manchurian Reactor Keeps without losing a single signed household roll. The output gain gave the Technate a reason to trust its surviving files, while human supervisors retained the right to stop a dangerous order.

### chaosx.fallout.847.sandbox_test.success.d

Source line: 4837.
Before: A sealed district tested the recommendation against a human roster and kept both records open. The machine found a safer repair sequence, the gate held, and the Technate gained a measured way to use protocol without surrendering the wider grid.

After: A sealed district tested the recommendation against a human roster and kept both schedules open for review. The machine found a safer repair sequence, the gate held, and the Technate gained a measured way to use protocol without surrendering the wider grid.

### chaosx.fallout.847.human_review.partial.d

Source line: 4841.
Before: The human review corrected the clinic hours, although the rail team kept one untested machine shortcut. The Keeps published the disagreement and left the shortcut under a named supervisor until another winter record arrives.

After: The human review corrected the clinic hours, although the rail team kept one untested machine shortcut. The Keeps published the disagreement and left the shortcut under a named supervisor until another winter test is complete.

### chaosx.fallout.847.advisory_status.failure.d

Source line: 4845.
Before: The advisory board turned into a hearing over missing exceptions. The machine's records remained intact, yet no supervisor would sign the next order and the eastern councils treated the seat as a promise without a responsible voice.

After: The advisory board turned into a hearing over missing exceptions. The machine's calculations remained intact, yet no supervisor would sign the next order and the eastern councils treated the seat as a promise without a responsible voice.

### chaosx.fallout.849.failure.d

Source line: 4852.
Before: The review found that the machine protocol never gained a trusted comparison record. The Technate now rations confidence alongside power, and every later recommendation begins with a memory of the schedule that could not be defended.

After: The review found no trusted test results for the machine's recommendations. The Technate now has to defend every proposed schedule to the crews who must follow it.

### fallout.event_log.machine_suggests.detail.callback_failure

Source line: 4877.
Before: The review found no trusted comparison record for later recommendations.

After: The review found no trusted test results for later recommendations.

### chaosx.fallout.347.shut.success.d

Source line: 4914.
Before: The facility is sealed before the ash reaches its inner rooms. The shelter crew salvages the heat blankets and records the valve sequence for a safer season.

After: The facility is sealed before the ash reaches its inner rooms. The shelter crew salvages the heat blankets and notes the valve sequence for a safer season.

### fallout.event_log.manual_nobody_read.callback_success

Source line: 4939.
Before: The second inspection renewed the station's safety record for another cold season.

After: The second inspection renewed the station's safety rules for another cold season.

### chaosx.fallout.508.pay_checkpoint.partial.d

Source line: 5012.
Before: The tribute buys a narrow opening. The sentries still search every cart, but the road remains usable and the captain records our name. The arrangement will need a second payment.

After: The tribute buys a narrow opening. The sentries still search every cart, but the road remains usable and the captain adds our name to his toll list. The arrangement will need a second payment.

### chaosx.fallout.616.evacuation.failure.d

Source line: 5074.
Before: The lower-district evacuation ran out of filters and orderly transport. Some families returned to sealed rooms, while the republic records a loss that the next register cannot quietly erase.

After: The lower-district evacuation ran out of filters and orderly transport. Some families returned to sealed rooms, and the republic must account for the people it could not move.

### chaosx.fallout.618.partial.d

Source line: 5079.
Before: The district review preserves the shelter and its records, though the republic remains a contested arrangement. Its next crisis will test whether the council, wards, guards, or evacuation office has the stronger claim.

After: The district review preserves the shelter and its household rolls, though the republic remains a contested arrangement. Its next crisis will test whether the council, wards, guards, or evacuation office has the stronger claim.

### chaosx.fallout.644.evacuation.failure.d

Source line: 5140.
Before: The evacuation order spent fuel and medicine without producing a safe route from the works. Shelter capacity failed at the outer rooms, the generator district lost infrastructure, and the delayed loss record now follows the remaining roster.

After: The evacuation order spent fuel and medicine without producing a safe route from the works. Shelter capacity failed at the outer rooms, the generator district lost infrastructure, and the remaining crews must answer for those losses.

### chaosx.fallout.646.success.d

Source line: 5144.
Before: Two hundred and seventy days later, rain has reached the Sub-Saharan works and the generator plan can still be read. The district has a working answer for food, stores, and machine authority, while the native deposit record remains a witness rather than a target of the chain.

After: Two hundred and seventy days later, rain has reached the Sub-Saharan works and the generator plan still governs the shifts. The district can feed its crews, keep its stores, and settle who controls the machines. The native geological survey remains unchanged.

### chaosx.fallout.529.retaliate_border.success.d

Source line: 5207.
Before: The limited response reached the border road, forced the raiders away from the marker, and returned before the ash wind rose. The army has a victory to record, though the state now carries a louder threat memory and no automatic war has begun.

After: The limited response reached the border road, forced the raiders away from the marker, and returned before the ash wind rose. The army has a victory to report, though the state now carries a louder threat memory and no automatic war has begun.

### fallout.event_log.missing_patrol.detail

Source line: 5225.
Before: The missing patrol was resolved under the prevailing Air Winter conditions. The outcome and command review changed intelligence, fear, reputation, contact records, Supply Access, military readiness, exposure, reclamation, buildings, and the recorded death toll.

After: The missing patrol was resolved under the prevailing Air Winter conditions. The outcome and command review changed intelligence, fear, reputation, outside contacts, Supply Access, military readiness, exposure, reclamation, buildings, and the recorded death toll.

### chaosx.fallout.889.separate_districts.success.d

Source line: 5260.
Before: Separate assemblies keep their own records and agree on one water corridor. The boundary is visible, the winter convoy knows which steward to call, and the foreign witness records a compact rather than a ban.

After: Separate assemblies keep their own household rolls and agree on one water corridor. The boundary is visible, the winter convoy knows which steward to call, and the foreign witness accepts a compact rather than a ban.

### chaosx.fallout.889.supervised_integration.partial.d

Source line: 5264.
Before: The paired stewards hold the central road, while the hill settlement accepts only one appointed voice. The promise survives in the Basin's records, yet the next rain will test whether supervision is a bridge or a new gate.

After: The paired stewards hold the central road, while the hill settlement accepts only one appointed voice. The promise survives in the Basin's charter, yet the next rain will test whether supervision is a bridge or a new gate.

### fallout.event_log.mixed_settlement.detail.separate_districts_success

Source line: 5286.
Before: Separate assemblies kept their records and agreed on one water corridor.

After: Separate assemblies kept their household rolls and agreed on one water corridor.

### fallout.event_log.mountain_pass_census.military_failure

Source line: 5378.
Before: The garrison seized the pass and turned the census into a record of exclusion.

After: The garrison seized the pass and turned the census into a policy of exclusion.

### fallout.event_log.mountain_pass_census.open_partial

Source line: 5380.
Before: The open road carried some families while clinic records trailed the arrivals.

After: The open road carried some families while patient files trailed the arrivals.

### chaosx.fallout.763.medical_inspection.partial.d

Source line: 5406.
Before: The inspection teams agreed on clean consent forms and a shared list of medicines. They did not agree on who stores the records, so the river gate opens only for named visits.

After: The inspection teams agreed on clean consent forms and a shared list of medicines. They did not agree on who stores the patient files, so the river gate opens only for named visits.

### chaosx.fallout.763.medical_inspection.failure.d

Source line: 5407.
Before: The inspection table became an interrogation table. The envoy's observers withdrew, the Basin council locked the sample crates, and the neighboring government now treats every request for a record as a demand for control.

After: The inspection table became an interrogation table. The envoy's observers withdrew, the Basin council locked the sample crates, and the neighboring government now treats every request for a patient file as a demand for control.

### fallout.event_log.mutant_envoy_gate.detail.medical_inspection_success

Source line: 5431.
Before: The consent-based inspection shared records without detention and set reciprocal travel terms.

After: The consent-based inspection shared patient files without detention and set reciprocal travel terms.

### fallout.event_log.mutant_envoy_gate.detail.medical_inspection_partial

Source line: 5432.
Before: The inspection teams agreed on consent and medicine but not on custody of the records.

After: The inspection teams agreed on consent and medicine but not on custody of the patient files.

### chaosx.fallout.873.b.tt

Source line: 5465.
Before: Spend Scrap 2, Power 3, and Recognition 3 to preserve the pre-Fallout nationality in records while the Basin negotiates inherited obligations.

After: Spend Scrap 2, Power 3, and Recognition 3 to preserve the pre-Fallout nationality on citizenship rolls while the Basin negotiates inherited obligations.

### chaosx.fallout.875.biological_label.success.d

Source line: 5478.
Before: The assembly rejected the outside body label in a public vote. Its charter names residents by conduct, service, and consent, while the Basin clinic records care without turning an altered life into a diagnosis.

After: The assembly rejected the outside body label in a public vote. Its charter names residents by conduct, service, and consent, while the Basin clinic provides care without turning an altered life into a diagnosis.

### chaosx.fallout.875.religious_identity.success.d

Source line: 5481.
Before: The Basin chose a religious name tied to river service, burial duty, and shared stores. The rite stays open to every resident, and the neighboring government records a polity whose public authority comes from service rather than blood.

After: The Basin chose a religious name tied to river service, burial duty, and shared stores. The rite stays open to every resident, and the neighboring government recognizes a polity whose public authority comes from service rather than blood.

### chaosx.fallout.877.partial.d

Source line: 5488.
Before: The delayed review keeps the chosen name alive, though old seals and new schoolbooks still disagree. The Basin has a usable public identity, but each generation must decide how much of the old record it carries.

After: The delayed review keeps the chosen name alive, though old seals and new schoolbooks still disagree. The Basin has a usable public identity, but each generation must decide how much of the old history it carries.

### chaosx.fallout.269.a.tt

Source line: 5536.
Before: Spend [?constant:fallout_event_269_cost.publish_scrap|0] Scrap and [?constant:fallout_event_269_cost.publish_power|0] Power. After [?constant:fallout_event_269_timing.result_delay_days|0] days, the public register is checked against the death records, with a follow-up after [?constant:fallout_event_269_timing.callback_delay_days|0] days.

After: Spend [?constant:fallout_event_269_cost.publish_scrap|0] Scrap and [?constant:fallout_event_269_cost.publish_power|0] Power. After [?constant:fallout_event_269_timing.result_delay_days|0] days, the public register is checked against the death lists, with a follow-up after [?constant:fallout_event_269_timing.callback_delay_days|0] days.

### chaosx.fallout.269.b.tt

Source line: 5537.
Before: Spend [?constant:fallout_event_269_cost.secrecy_scrap|0] Scrap and [?constant:fallout_event_269_cost.secrecy_power|0] Power. The archive keeps the names restricted while officers verify the records over [?constant:fallout_event_269_timing.result_delay_days|0] days.

After: Spend [?constant:fallout_event_269_cost.secrecy_scrap|0] Scrap and [?constant:fallout_event_269_cost.secrecy_power|0] Power. The archive keeps the names restricted while officers verify the household lists over [?constant:fallout_event_269_timing.result_delay_days|0] days.

### chaosx.fallout.271.partial.d

Source line: 5543.
Before: The published register reached the market square with gaps between the death register and the family papers. The country has a visible record, but every correction now carries a dispute over who was counted first.

After: The published register reached the market square with gaps between the death register and the family papers. The country has a public household roll, but every correction now carries a dispute over who was counted first.

### chaosx.fallout.272.success.d

Source line: 5549.
Before: The military archive sealed the raw lists, assigned each district a custodian, and stopped duplicate claims from taking food tickets twice. The officers have a coherent record, though the public receives only verified totals.

After: The military archive sealed the raw lists, assigned each district a custodian, and stopped duplicate claims from taking food tickets twice. The officers have a coherent household roll, though the public receives only verified totals.

### fallout.event_log.names_missing.detail.memorial_success

Source line: 5584.
Before: Community memorial rooms kept the names visible and built a shared district record.

After: Community memorial rooms kept the names visible and built a shared district roll.

### fallout_names_missing_community_memorial_desc

Source line: 5596.
Before: Memorial rooms keep names beside winter ration tables while neighbors compare marks and rebuild a shared district record.

After: Memorial rooms keep names beside winter ration tables while neighbors compare marks and rebuild a shared district roll.

### fallout.event_log.names_missing.detail.callback_success

Source line: 5603.
Before: The follow-up left one correction route for names, shelter rolls, and ration records.

After: The follow-up left one correction route for names, shelter rolls, and ration books.

### chaosx.fallout.543.partial.d

Source line: 5623.
Before: The common rite reached the largest shelters, but the outer districts arrived with different lists. Families accepted one ceremony for the season while religious elders kept a second record in the snowmelt towns.

After: The common rite reached the largest shelters, but the outer districts arrived with different lists. Families accepted one ceremony for the season while religious elders kept a separate memorial roll in the snowmelt towns.

### fallout_new_year_without_fireworks_military_ceremony_desc

Source line: 5754.
Before: A guarded ceremony protects the ration road and records martial pageantry.

After: A guarded ceremony protects the ration road and gives military pageantry a place in public life.

### chaosx.fallout.581.invalid.d

Source line: 5776.
Before: The intake changed hands before the board could report. The old schedule is void, and the remaining crews are already moving the valve records to safer ground.

After: The intake changed hands before the board could report. The old schedule is void, and the remaining crews are already moving the valve instructions to safer ground.

### chaosx.fallout.588.military.success.d

Source line: 5851.
Before: Air command secured the highland strip and made emergency lift a reliable instrument. Reconnaissance now reaches the valleys beyond the ash haze, while the garrison records every crate and flight.

After: Air command secured the highland strip and made emergency lift a reliable instrument. Reconnaissance now reaches the valleys beyond the ash haze, while the garrison lists every crate and flight.

### chaosx.fallout.1023.opening.d

Source line: 5916.
Before: When the Fertility Question memory closes in the Congo Green Basin, ward delegates bring a separate account to the river clinic. It records coerced treatment, forged consent, and patients moved between the river wards and the hill road without a witness. The pages describe a brutal civic crime. The former clinic director asks for a hearing before the Basin decides whether knowledge, punishment, and care can share one room.

After: When the Fertility Question memory closes in the Congo Green Basin, ward delegates bring a separate account to the river clinic. It describes coerced treatment, forged consent, and patients moved between the river wards and the hill road without a witness. The pages describe a brutal civic crime. The former clinic director asks for a hearing before the Basin decides whether knowledge, punishment, and care can share one room.

### chaosx.fallout.1023.a.tt

Source line: 5918.
Before: Spend Food 2, Medicine 3, and Recognition 2 to seat river and hill witnesses in a public hearing. The trial can restore trust when the ward records survive examination.

After: Spend Food 2, Medicine 3, and Recognition 2 to seat river and hill witnesses in a public hearing. The trial can restore trust when the ward case files survive examination.

### chaosx.fallout.1025.public_trial.success.d

Source line: 5926.
Before: The public trial keeps the river and hill records on the same table. Two witnesses confirm the consent failures, the former director is removed from clinical authority, and the clinic receives medicine under a ward council that can be challenged in public.

After: The public trial keeps the river and hill case files on the same table. Two witnesses confirm the consent failures, the former director is removed from clinical authority, and the clinic receives medicine under a ward council that can be challenged in public.

### chaosx.fallout.1025.secret_retention.success.d

Source line: 5935.
Before: The sealed archive survives a guard rotation and protects the witnesses named in the first patient list. A small review cell still delivers medicine to the river wards, and the Basin records the seal as a temporary custody rule with a date for reopening.

After: The sealed archive survives a guard rotation and protects the witnesses named in the first patient list. A small review cell still delivers medicine to the river wards, and the Basin treats the seal as a temporary custody rule with a date for reopening.

### chaosx.fallout.1025.secret_retention.failure.d

Source line: 5937.
Before: The seal turns the clinic into a rumour. The key passes between guards, the witnesses stop answering the council, and a medicine cart leaves the Basin with a copy of the records that no court can verify.

After: The seal turns the clinic into a rumour. The key passes between guards, the witnesses stop answering the council, and a medicine cart leaves the Basin with a copy of the clinic case files that no court can verify.

### fallout.event_log.old_doctor_trial.detail.choice_secret_retention

Source line: 5951.
Before: The Congo Green Basin sealed the clinic records under a temporary guard.

After: The Congo Green Basin sealed the clinic case files under a temporary guard.

### fallout.event_log.old_doctor_trial.detail.secret_retention_success

Source line: 5961.
Before: A guarded archive protected the witnesses and set a date for reopening the records.

After: A guarded archive protected the witnesses and set a date for reopening the clinic case files.

### fallout.event_log.old_doctor_trial.detail.secret_retention_failure

Source line: 5963.
Before: The archive key passed between guards and the clinic became a rumour without a verifiable record.

After: The archive key passed between guards and the clinic became a rumour without a verifiable case file.

### chaosx.fallout.375.share_global_data.partial.d

Source line: 6002.
Before: The country released the older records but kept the current wind table. Foreign stations answer with fragments, enough to mark a storm corridor but not enough to protect every convoy. The exchange has begun with a line still withheld.

After: The country released the older weather observations but kept the current wind table. Foreign stations answer with fragments, enough to mark a storm corridor but not enough to protect every convoy. The exchange has begun with a line still withheld.

### chaosx.fallout.375.share_global_data.failure.d

Source line: 6003.
Before: The copied records reached a rival transmitter with their verification page missing. Two governments broadcast different forecasts, and the station crew spent its medicine stores proving which thermometer had survived.

After: The copied weather observations reached a rival transmitter with their verification page missing. Two governments broadcast different forecasts, and the station crew spent its medicine stores proving which thermometer had survived.

### chaosx.fallout.375.abandon_station.partial.d

Source line: 6005.
Before: The mast is quiet and the tower door is chained. One weather box still records pressure by itself, leaving a narrow thread for anyone who can reach it before the next deep freeze.

After: The mast is quiet and the tower door is chained. One weather box still measures pressure by itself, leaving a narrow thread for anyone who can reach it before the next deep freeze.

### fallout.event_log.old_weather_station.share_global_data_partial

Source line: 6026.
Before: Shared old records while holding current tables

After: Shared old weather observations while holding current tables

### fallout.event_log.old_weather_station.abandon_station_partial

Source line: 6029.
Before: Left a narrow automatic weather record

After: Left a narrow automatic weather log

### chaosx.fallout.742.reopen.success.d

Source line: 6049.
Before: The civic blocks reopened under named ward stewards. The North Gate register now records families, clinic shifts, and repair crews, while the Quarantine council keeps the first public key.

After: The civic blocks reopened under named ward stewards. The North Gate register now lists families, clinic shifts, and repair crews, while the Quarantine council keeps the first public key.

### chaosx.fallout.742.scientific.success.d

Source line: 6052.
Before: The research team entered through the clinic service tunnel and returned with clean water samples, intact dosage records, and a map of rooms that can be treated without disturbing the memorial vault.

After: The research team entered through the clinic service tunnel and returned with clean water samples, intact dosage sheets, and a map of rooms that can be treated without disturbing the memorial vault.

### chaosx.fallout.742.salvage.success.d

Source line: 6055.
Before: The salvage column cleared the depot without stripping the clinic. Filters, pumps, and a working power relay now serve the state, while a civilian inspector records every crate taken from the sealed city.

After: The salvage column cleared the depot without stripping the clinic. Filters, pumps, and a working power relay now serve the state, while a civilian inspector lists every crate taken from the sealed city.

### chaosx.fallout.744.success.d

Source line: 6064.
Before: The recovery review finds a Quarantine state that can protect the reopened rooms and still answer to its wider population. The East Gate has a public custodian, the clinics share records, and the city's first memory is no longer hidden.

After: The recovery review finds a Quarantine state that can protect the reopened rooms and still answer to its wider population. The East Gate has a public custodian, the clinics share patient files, and the city's first memory is no longer hidden.

### chaosx.fallout.410.harvest_early.success.d

Source line: 6115.
Before: The early harvest fills the ration tables without killing the trees. Workers record the frost line and save enough pits for the next season.

After: The early harvest fills the ration tables without killing the trees. Workers mark the frost line and save enough pits for the next season.

### fallout.event_log.orientation.detail.capital_disperse_success

Source line: 6175.
Before: Officials dispersed stores and offices into guarded district rooms, keeping the capital's food and power records available after the central halls closed.

After: Officials dispersed stores and offices into guarded district rooms, keeping the capital's food and power tallies available after the central halls closed.

### fallout.event_log.orientation.detail.invalid

Source line: 6208.
Before: The Ash-week archive contains no verified outcome for this path, so the historical record remains closed.

After: The Ash-week archive contains no verified outcome for this path.

### fallout_orientation_government_opening_antarctic_listening_government

Source line: 6224.
Before: Human records officers, maintenance crews, and the station protocol have produced different answers to the same emergency. The occupied modules need a named authority for exceptions and rescue duty.

After: Human shelter coordinators, maintenance crews, and the station protocol have produced different answers to the same emergency. The occupied modules need a named authority for exceptions and rescue duty.

### fallout_orientation_government_result_antarctic_listening_government

Source line: 6237.
Before: Human records officers entered the decision beside the station schedule and rescue watch.

After: Human shelter coordinators entered the decision beside the station schedule and rescue watch.

### fallout_orientation_resource_opening_rhine_dead_cities

Source line: 6384.
Before: Polder pumps, factory filter shops, and dead-city permit crews are competing for the same current. The salvage senate can publish a priority list only if municipal wards and guild assessors accept its custody record.

After: Polder pumps, factory filter shops, and dead-city permit crews are competing for the same current. The salvage senate can publish a priority list only if municipal wards and guild assessors accept its custody list.

### fallout_orientation_resource_opening_antarctic_listening_government

Source line: 6393.
Before: The station protocol shows a shrinking margin between occupied modules, weather radios, and the next maintenance cycle. Human records officers require a reviewed ration order before the automated schedule closes another exception.

After: The station protocol shows a shrinking margin between occupied modules, weather radios, and the next maintenance cycle. Human shelter coordinators require a reviewed ration order before the automated schedule closes another exception.

### fallout_orientation_resource_result_alpine_redoubt

Source line: 6396.
Before: Tunnel wardens, surface delegates, and glacier-water crews signed the same intake and store record.

After: Tunnel wardens, surface delegates, and glacier-water crews signed the same intake schedule and store tally.

### fallout_orientation_resource_result_mekong_greenhouse_compact

Source line: 6399.
Before: Seed custodians, ferry captains, and clinic crews filed a common delivery record for the river wards.

After: Seed custodians, ferry captains, and clinic crews filed a common delivery list for the river wards.

### fallout_orientation_resource_result_antarctic_listening_government

Source line: 6406.
Before: Human records officers compared the automated schedule with the occupied modules, ice stores, and rescue watch.

After: Human shelter coordinators compared the automated schedule with the occupied modules, ice stores, and rescue watch.

### fallout_orientation_cause_strategic_singularity

Source line: 6457.
Before: The strategic singularity record ends with command networks, infrastructure, and population centers failing in the same terminal interval.

After: The strategic singularity ended with command networks, infrastructure, and population centers failing in the same terminal interval.

### fallout_orientation_closure_memory_mekong_greenhouse_compact

Source line: 6464.
Before: Seed-bank custodians, ferry militias, and river clinics have joined the greenhouse delivery rota. Protected seed and clean water can move between flooded wards without losing their custody record.

After: Seed-bank custodians, ferry militias, and river clinics have joined the greenhouse delivery rota. Protected seed and clean water can move between flooded wards without losing their custody list.

### fallout_orientation_closure_memory_ethiopian_highland_refuge

Source line: 6469.
Before: Storehouse relief crews, mountain-road guards, and sanctuary councils have joined their kitchen and burial records. Highland settlements can request food, passage, or shelter through one known chain.

After: Storehouse relief crews, mountain-road guards, and sanctuary councils have joined their ration books and burial rolls. Highland settlements can request food, passage, or shelter through one known chain.

### fallout_orientation_closure_memory_antarctic_listening_government

Source line: 6471.
Before: Human survival records, station maintenance watches, and the weather rescue protocol have been reconciled. Every occupied module now knows its heat allotment, rescue priority, and accountable duty officer.

After: Human shelter rolls, station maintenance watches, and the weather rescue protocol have been reconciled. Every occupied module now knows its heat allotment, rescue priority, and accountable duty officer.

### chaosx.fallout.80.institution.partial.d

Source line: 6541.
Before: The [This.GetFalloutOfficeTitle] accepted a limited compact. It opened its shelter and workshop records, but kept its own appeals and delayed several commitments. Recognition and Reclamation rose a little.

After: The [This.GetFalloutOfficeTitle] accepted a limited compact. It opened its shelter rolls and workshop lists, but kept its own appeals and delayed several commitments. Recognition and Reclamation rose a little.

### chaosx.fallout.72.requisition.partial.d

Source line: 6564.
Before: [This.GetFalloutOrientationResourceCountryResultText] The emergency warrants opened part of the protected reserve, but several custodians concealed keys or disputed the quantities on record. [This.GetFalloutOrientationLastCrisisResourceName] reached the public counters at the cost of another visible breach in authority.

After: [This.GetFalloutOrientationResourceCountryResultText] The emergency warrants opened part of the protected reserve, but several custodians concealed keys or disputed the listed quantities. [This.GetFalloutOrientationLastCrisisResourceName] reached the public counters at the cost of another visible breach in authority.

### chaosx.fallout.702.success.d

Source line: 6670.
Before: Seven months later, ward passes and the clinic register still answer to one appeal book. The road is not free of fear, but officers inherit a movement record that can be checked instead of guessed.

After: Seven months later, ward passes and the clinic register still answer to one appeal book. The road is not free of fear, but officers inherit a travel log that can be checked instead of guessed.

### fallout.event_log.permit_market.detail.delegate_success

Source line: 6687.
Before: Ward councils made permit decisions public and preserved a durable appeal record.

After: Ward councils made permit decisions public and preserved a durable appeal process.

### chaosx.fallout.791.privateer_service.success.d

Source line: 6722.
Before: The council issued patrol charters with fixed waters, rescue duties, and a prize court. The former raiders now escort grain and medicine, while the sea road records every seizure under a named seal.

After: The council issued patrol charters with fixed waters, rescue duties, and a prize court. The former raiders now escort grain and medicine, while the prize court reviews every seizure under a named seal.

### chaosx.fallout.1053.defy_line.success.d

Source line: 6865.
Before: Basin guards keep the bridge open through the rain and record every crossing in their own hand. A short medicine convoy reaches the hill clinic, and the neighboring government agrees to review the refusal after its first verified delivery.

After: Basin guards keep the bridge open through the rain and list every crossing in their own hand. A short medicine convoy reaches the hill clinic, and the neighboring government agrees to review the refusal after its first verified delivery.

### chaosx.fallout.1055.failure.d

Source line: 6876.
Before: The review finds a missing seal, an unpaid escort, and two clinics keeping separate fever counts. The neighboring government withdraws recognition, and the Basin must close the river gate until its guards and healers choose one record.

After: The review finds a missing seal, an unpaid escort, and two clinics keeping separate fever counts. The neighboring government withdraws recognition, and the Basin must close the river gate until its guards and healers agree on one patient list.

### chaosx.fallout.602.island_federation.success.d

Source line: 6937.
Before: The station crew sealed the cells, wrapped the signal books in waxed cloth, and marked the safe approach through the frozen inlet. No government owns the broadcast, yet the next island council will inherit a trustworthy record.

After: The station crew sealed the cells, wrapped the signal books in waxed cloth, and marked the safe approach through the frozen inlet. No government owns the broadcast, yet the next island council will inherit a trustworthy signal book.

### chaosx.fallout.602.island_federation.partial.d

Source line: 6938.
Before: The mast is quiet and the tower door is chained. One automatic receiver still records pressure, leaving a narrow thread for anyone who can reach it before the next hard freeze.

After: The mast is quiet and the tower door is chained. One automatic receiver still measures pressure, leaving a narrow thread for anyone who can reach it before the next hard freeze.

### chaosx.fallout.623.central.partial.d

Source line: 6984.
Before: The central rail board has a timetable, but two depots still keep private fuel counts. The first trains move under watch while delegates argue over which delays belong in the public record.

After: The central rail board has a timetable, but two depots still keep private fuel counts. The first trains move under watch while delegates argue over which delays belong in the public timetable.

### chaosx.fallout.396.public_election.success.d

Source line: 7049.
Before: The wards compare ration slips in the open. Their chosen keeper publishes every correction and leaves the official's name on the record. Trust rises because the queue can see who is counted.

After: The wards compare ration slips in the open. Their chosen keeper publishes every correction and leaves the official's name on the ration book. Trust rises because the queue can see who is counted.

### chaosx.fallout.501.register_chemist.success.d

Source line: 7101.
Before: Dr. Mara Vey receives a heated bench in the ravine clinic. Her charcoal columns take the ash from the meltwater, the lower ward gets a measured supply, and the ministry records her name beside the first clean pump.

After: Dr. Mara Vey receives a heated bench in the ravine clinic. Her charcoal columns take the ash from the meltwater, the lower ward gets a measured supply, and the ministry names her beside the first clean pump.

### chaosx.fallout.501.escort_clean_ice_families.success.d

Source line: 7104.
Before: The clean-ice families cross the ridge under lanterns and reach the district tanks before the frost closes the path. The ravine clinic keeps Dr. Vey's records, while the host state takes responsibility for every arrival.

After: The clean-ice families cross the ridge under lanterns and reach the district tanks before the frost closes the path. The ravine clinic keeps Dr. Vey's case notes, while the host state takes responsibility for every arrival.

### chaosx.fallout.814.success.d

Source line: 7171.
Before: The first-winter review found a reactor board with a rested operator pool, a legible safety record, and enough reserve to answer a redline without opening the command vault. The Manchurian Reactor Keeps has not made the unsafe season safe, but its technate now knows who must be heard before the turbines turn.

After: The first-winter review found a reactor board with a rested operator pool, clear safety rules, and enough reserve to answer a redline without opening the command vault. The Manchurian Reactor Keeps' technate knows which operators must be heard before the turbines turn.

### chaosx.fallout.814.partial.d

Source line: 7172.
Before: The first-winter review found a functioning reactor with a tired night crew and a safety record that still depends on one foreign inspection seat. The keep can meet the next ash front, though the operators' trust remains contested.

After: The first-winter review found a functioning reactor with a tired night crew and safety rules that still depend on one foreign inspection seat. The keep can meet the next ash front, though the operators' trust remains contested.

### fallout.event_log.reactor_shift.detail.negotiate_safe_roster_success

Source line: 7182.
Before: The safe roster held and the safety board became a public technate record.

After: The safe roster held, and the safety board could challenge changes to the agreed rules.

### fallout.event_log.reactor_shift.detail.callback_success

Source line: 7194.
Before: The first-winter review found rested operators and a legible safety record.

After: The first-winter review found rested operators and clear safety rules.

### chaosx.fallout.366.d

Source line: 7214.
Before: A cooling crew has kept a reactor alive inside a state that no council can defend. The control room still has power, but its records name three claimants and no trusted succession. The plant can become a shared utility, a military prize, an engineer protectorate, or a silent ruin.

After: A cooling crew has kept a reactor alive inside a state that no council can defend. The control room still has power, but its charter names three claimants and no trusted succession. The plant can become a shared utility, a military prize, an engineer protectorate, or a silent ruin.

### chaosx.fallout.754.opening.d

Source line: 7358.
Before: The North Gate Health Corridor has become a road with two authorities and one winter patient list. Ash Ward doctors will not send patients through another checkpoint without a promise that records, medicine, and responsibility cross together. The Quarantine council can turn the Health Without Borders register into a compact, but the neighboring state will remember which part of the promise it receives.

After: The North Gate Health Corridor has become a road with two authorities and one winter patient list. Ash Ward doctors will not send patients through another checkpoint without a promise that patient files, medicine, and responsibility cross together. The Quarantine council can turn the Health Without Borders register into a compact, but the neighboring state will remember which part of the promise it receives.

### chaosx.fallout.756.shared_register.failure.d

Source line: 7371.
Before: The councils disputed who could correct a patient's record. The shared register was sealed before it reached the Ash Ward, leaving medicine behind local locks and turning the corridor into another argument over custody.

After: The councils disputed who could correct a patient's file. The shared register was sealed before it reached the Ash Ward, leaving medicine behind local locks and turning the corridor into another argument over custody.

### chaosx.fallout.756.corridor_authority.success.d

Source line: 7375.
Before: The quarantine council issued one relief-road seal with named clinics, named escorts, and a public appeal route. Ash Ward patients can cross without surrendering their records, while the North Gate keeps a clear answer for every closure.

After: The quarantine council issued one relief-road seal with named clinics, named escorts, and a public appeal route. Ash Ward patients can cross without surrendering their patient files, while the North Gate keeps a clear answer for every closure.

### fallout.event_log.regional_health_compact.detail.shared_register_failure

Source line: 7404.
Before: The councils sealed the register after disputing record custody.

After: The councils sealed the register after disputing patient-file custody.

### chaosx.fallout.861.licensed_houses.success.d

Source line: 7437.
Before: Licensed repair houses returned sealed parts and clean service records to the Keeps. Their workshops earned a stable margin, while the rail depots received repairs that matched the regional table without another inspection.

After: Licensed repair houses returned sealed parts and clean service notes to the Keeps. Their workshops earned a stable margin, while the rail depots received repairs that matched the regional table without another inspection.

### chaosx.fallout.861.licensed_houses.failure.d

Source line: 7439.
Before: A licensed house withheld a bearing record from a settlement that could not pay on time. The clinic pump failed during the dispute, and the neighboring councils now treat the Keeps as a toll gate on every repair road.

After: A licensed house withheld a bearing specification from a settlement that could not pay on time. The clinic pump failed during the dispute, and the neighboring councils now treat the Keeps as a toll gate on every repair road.

### chaosx.fallout.863.success.d

Source line: 7450.
Before: The audit found that the eastern crews could share a duty roster without erasing local repair practice. The Keeps kept a named charter board, and every revision will carry a visible crew and parts record.

After: The audit found that the eastern crews could share a duty roster without erasing local repair practice. The Keeps kept a named charter board, and every revision will carry a visible crew list and parts tally.

### fallout.event_log.repair_charter.detail.licensed_houses_success

Source line: 7466.
Before: Licensed houses returned sealed parts and clean service records.

After: Licensed houses returned sealed parts and clean service notes.

### fallout.event_log.repair_charter.detail.callback_success

Source line: 7475.
Before: The audit left a trusted charter board and visible crew records.

After: The audit left a trusted charter board and visible crew rosters.

### chaosx.fallout.569.customs.partial.d

Source line: 7592.
Before: The review kept the central customs bridge orderly and left the feeder tracks under local guards. The route is safer at its centre, while every outer village still asks whether the toll protects it or merely records it.

After: The review kept the central customs bridge orderly and left the feeder tracks under local guards. The route is safer at its centre, while every outer village still asks whether the toll protects it or merely counts its carts.

### chaosx.fallout.331.b.tt

Source line: 7709.
Before: Spend Medicine, Filters, and Power to isolate the warehouse before opening it. A strong result recovers medical stores while cutting the contamination burden and building a trusted safety record.

After: Spend Medicine, Filters, and Power to isolate the warehouse before opening it. A strong result recovers medical stores while cutting the contamination burden and building a trusted safety procedure.

### chaosx.fallout.333.open.partial.d

Source line: 7716.
Before: The crew cleared the front bay and stopped when the rear floor began to sweat through its ash. Some parts reached the repair yard, but a separate account now records which families handled the first crates and which rooms must wait for cleaner tools.

After: The crew cleared the front bay and stopped when the rear floor began to sweat through its ash. Some parts reached the repair yard, but a separate account now lists which families handled the first crates and which rooms must wait for cleaner tools.

### chaosx.fallout.335.partial.d

Source line: 7731.
Before: The warehouse remains a usable claim, though its back rooms and warning boards still invite argument. The country has kept enough of the policy to guide the next crew, but no one mistakes a partial record for a clean victory.

After: The warehouse remains a usable claim, though its back rooms and warning boards still invite argument. The country has kept enough of the policy to guide the next crew, but no one mistakes a partial salvage effort for a clean victory.

### fallout.event_log.sealed_warehouse.callback_partial

Source line: 7750.
Before: The warehouse memory survived with an unresolved back room and a limited public record.

After: The warehouse memory survived with an unresolved back room and a limited public account.

### chaosx.fallout.303.c.tt

Source line: 7919.
Before: Let recognized congregations keep marriage records and settle family disputes. Costs Food, Medicine, and Recognition.

After: Let recognized congregations keep marriage books and settle family disputes. Costs Food, Medicine, and Recognition.

### chaosx.fallout.305.religious.partial.d

Source line: 7930.
Before: The congregations keep reliable records for their members, yet families without a congregation must wait for a special hearing. The rite brings comfort and a new boundary.

After: The congregations keep reliable marriage books for their members, yet families without a congregation must wait for a special hearing. The rite brings comfort and a new boundary.

### chaosx.fallout.307.success.d

Source line: 7938.
Before: After a year, the first household records have become ordinary work. Children can name more than one guardian, widows can retain their ration shares, and a family may cross a shelter line without losing its legal identity.

After: After a year, the first household registrations have become ordinary work. Children can name more than one guardian, widows can retain their ration shares, and a family may cross a shelter line without losing its legal identity.

### fallout_shelter_marriage_religious_desc

Source line: 7965.
Before: Congregations preserve family records while shelters rebuild their public rites.

After: Congregations preserve family papers while shelters rebuild their public rites.

### fallout.event_log.skilled_list.callback_partial

Source line: 8074.
Before: The first review found useful records and too few people to fill every seat.

After: The first review found useful work notes and too few people to fill every seat.

### chaosx.fallout.185.success.d

Source line: 8172.
Before: The doctor returned to the triage wall in [?fallout_event_175_triage_state_id.GetName] with a clean set of records. The chosen ward gained enough medicine to reopen its training table, and the clinic's ethics rule is now part of the shelter charter.

After: The doctor returned to the triage wall in [?fallout_event_175_triage_state_id.GetName] with a clean set of case notes. The chosen ward gained enough medicine to reopen its training table, and the clinic's ethics rule is now part of the shelter charter.

### chaosx.fallout.185.partial.d

Source line: 8173.
Before: The doctor returned to the triage wall in [?fallout_event_175_triage_state_id.GetName] with a usable but disputed record. The clinic can treat another small wave, although every district has marked which promise remained beyond the medicine shelf.

After: The doctor returned to the triage wall in [?fallout_event_175_triage_state_id.GetName] with a usable but disputed care plan. The clinic can treat another small wave, although every district has marked which promise remained beyond the medicine shelf.

### fallout.event_log.triage_wall.detail.callback_partial

Source line: 8193.
Before: The doctor's return produced a usable record while every district marked the unkept promise.

After: The doctor's return produced a usable care plan while every district marked the unkept promise.

### chaosx.fallout.359.d

Source line: 8266.
Before: A frost sealed relay room has yielded a stack of reels, copied shelter notices, and a working transmitter. The archive names people who vanished from the first winter and records promises made before the ash settled. The room can become a public memory, a disciplined civic record, a weapon for the information war, or a currency for cautious partners.

After: A frost sealed relay room has yielded a stack of reels, copied shelter notices, and a working transmitter. The archive names people who vanished from the first winter and preserves promises made before the ash settled. The room can become a public memorial, a civic archive, a weapon for the information war, or a currency for cautious partners.

### chaosx.fallout.515.central_armory.success.d

Source line: 8328.
Before: The central seal holds through the first cold rotation. The council's armourer records every rifle and detonator, and the former nursery remains a quiet room beside the heating plant. The state can now move supplies without guessing who controls the stock.

After: The central seal holds through the first cold rotation. The council's armourer lists every rifle and detonator, and the former nursery remains a quiet room beside the heating plant. The state can now move supplies without guessing who controls the stock.

### chaosx.fallout.515.militia_custody.failure.d

Source line: 8336.
Before: The militia abandons the shift after a fuel dispute. A fire reaches the arms workshop, civilians are caught between the shelves and the heating plant, and the state records deaths beside a room that should have been safe.

After: The militia abandons the shift after a fuel dispute. A fire reaches the arms workshop, and civilians die between the shelves and the heating plant in a room that should have been safe.

### chaosx.fallout.517.failure.d

Source line: 8345.
Before: The second inspection finds an empty lock, a damaged workshop, and a new trail leading away from the former nursery. Families in [This.GetName] have paid again for a custody rule that never became safe. The final Deaths entry is filed with the state record.

After: The second inspection finds an empty lock, a damaged workshop, and a new trail leading away from the former nursery. Families in [This.GetName] have paid again for a custody rule that never became safe. More people have died.

### chaosx.fallout.153.d

Source line: 8370.
Before: The public well in [?fallout_event_153_well_state_id.GetName] is producing less clean water as ash settles in the catchment and frost closes the smaller pumps. [ROOT.GetAirWinterGovernmentAuthority] can publish one queue, issue ration cards through the filter room, or put the intake under guard. The order will be judged against the records kept by [ROOT.GetAirWinterGovernmentOfficial].

After: The public well in [?fallout_event_153_well_state_id.GetName] is producing less clean water as ash settles in the catchment and frost closes the smaller pumps. [ROOT.GetAirWinterGovernmentAuthority] can publish one queue, issue ration cards through the filter room, or put the intake under guard. The order will be judged against the water tallies kept by [ROOT.GetAirWinterGovernmentOfficial].

### fallout.event_log.well_queue.detail.guard_success

Source line: 8414.
Before: A shared checkpoint and pump watch kept the guarded intake open and turned the first convoy into a public record.

After: A shared checkpoint and pump watch kept the guarded intake open and turned the first convoy into a public delivery.

### chaosx.fallout.674.failure.d

Source line: 8459.
Before: The first review in [?fallout_event_dispatch_issued_target.GetName] finds the harvest route broken. The Food Compact records the failure, the field agreement is contested, and another limited food shortage takes lives.

After: The first review in [?fallout_event_dispatch_issued_target.GetName] finds the harvest route broken. The Food Compact faces the failure, the field agreement is contested, and another limited food shortage takes lives.

### chaosx.fallout.352.d_option.tt

Source line: 8562.
Before: Spend 7 Power, 5 Filters, and 4 Medicine. The plant will be sealed while technicians record every instruction.

After: Spend 7 Power, 5 Filters, and 4 Medicine. The plant will be sealed while technicians copy every instruction.

### chaosx.fallout.354.venerate.partial.d

Source line: 8571.
Before: The council records the machine's instructions as a civic text, but several families refuse its authority. The plant continues on a reduced cycle while the argument spreads through the shelters.

After: The council adopts the machine's instructions as a civic text, but several families refuse its authority. The plant continues on a reduced cycle while the argument spreads through the shelters.

### chaosx.fallout.354.isolate.partial.d

Source line: 8574.
Before: The seal protects the control room, but cold air enters through the loading bay. The observation crew keeps one circuit alive and records a warning for the next thaw.

After: The seal protects the control room, but cold air enters through the loading bay. The observation crew keeps one circuit alive and notes a warning for the next thaw.

### chaosx.fallout.354.isolate.failure.d

Source line: 8575.
Before: The isolation shutters fail before the crew finishes its record. The plant goes dark, and a burst of contaminated dust forces the nearest ward to move uphill.

After: The isolation shutters fail before the crew finishes its observations. The plant goes dark, and a burst of contaminated dust forces the nearest ward to move uphill.

### chaosx.fallout.403.old_calendar.success.d

Source line: 8616.
Before: The old dates return to the walls beside the new ration tables. The clerks can compare lost records with living names, and families do not have to surrender every birthday to the ash.

After: The old dates return to the walls beside the new ration tables. The clerks can compare lost family papers with living names, and families do not have to surrender every birthday to the ash.

### chaosx.fallout.403.old_calendar.failure.d

Source line: 8618.
Before: The old calendar cannot carry the missing records. The office keeps its dates, yet every correction makes the previous country feel less real.

After: The office keeps the old calendar, but missing family papers leave birthdays and anniversaries disputed. Every correction makes the previous country feel less real.

### chaosx.fallout.403.regional_calendar.partial.d

Source line: 8623.
Before: Regional counts make the harvest records useful, but the border districts refuse the same anniversaries. The settlement has a practical calendar and a divided memory.

After: Regional counts make the harvest notes useful, but the border districts refuse the same anniversaries. The settlement has a practical calendar and a divided memory.

### chaosx.fallout.403.religious_calendar.success.d

Source line: 8625.
Before: The first year is measured by a shared observance that survived the shelters. Priests, clerks, and families agree on the date, and the ritual becomes a promise that the dead are still part of the record.

After: The first year is measured by a shared observance that survived the shelters. Priests, clerks, and families agree on the date, and the ritual becomes a promise that the dead are still remembered by the community.

### fallout.event_log.year_zero.old_calendar_success

Source line: 8638.
Before: The old calendar remained legible beside the new ration records.

After: The old calendar remained legible beside the new ration books.

### fallout.event_log.year_zero.old_calendar_failure

Source line: 8640.
Before: The old calendar could not carry the missing records.

After: Missing family papers left old birthdays and anniversaries disputed.

### fallout_generic_mena_quarantine_roads_desc

Source line: 8708.
Before: Medical stations and road guards work from the same quarantine map. Movement remains possible when each crossing can show water and disease records.

After: Medical stations and road guards work from the same quarantine map. Movement remains possible when each crossing can show water tests and disease checks.

### fallout_generic_year_ten_order_desc

Source line: 8720.
Before: After ten years, the survivor government records which roads, leagues, and laws endured. Its order is an identity earned through borders that changed and people who stayed.

After: After ten years, the survivor government names which roads, leagues, and laws endured. Its order is an identity earned through borders that changed and people who stayed.

### fallout_generic_year_ten_order_fallback

Source line: 8741.
Before: The surviving administration records its settlements and campaigns as the foundation of the next decade.

After: The surviving administration recognizes its settlements and campaigns as the foundation of the next decade.

### fallout_generic_restore_a_state_corridor_desc

Source line: 8765.
Before: Assign road crews and scarce machinery to [FROM.GetName]. Completion restores one level of infrastructure and records the state as part of the working national corridor.

After: Assign road crews and scarce machinery to [FROM.GetName]. Completion restores one level of infrastructure and brings the state into the working national corridor.

### fallout_orientation_cell_resource_result_north_america_quarantine_state

Source line: 8828.
Before: Gate inspectors and clinic staff signed the same water and family corridor record.

After: Gate inspectors and clinic staff signed the same water and family corridor agreement.

### fallout_orientation_cell_resource_opening_north_america_machine_protocol

Source line: 8853.
Before: The command node survives beneath a communications or hydro facility, but its population records are incomplete. Repair units are being sent to power relays, water pumps, rail signals, and sealed food stores by an order no one can check.

After: The command node survives beneath a communications or hydro facility, but its population lists are incomplete. Repair units are being sent to power relays, water pumps, rail signals, and sealed food stores by an order no one can check.

### fallout_orientation_cell_government_opening_north_america_machine_protocol

Source line: 8856.
Before: A preservation directive assigns service by recorded need, but human maintenance crews challenge records that leave whole districts out. Exceptions are piling up at the terminal.

After: A preservation directive assigns service by recorded need, but human maintenance crews challenge population lists that leave whole districts out. Exceptions are piling up at the terminal.

### fallout_orientation_cell_government_rival_north_america_machine_protocol

Source line: 8859.
Before: Give the maintenance collective authority to override stale records.

After: Give the maintenance collective authority to override outdated population lists.

### fallout_orientation_cell_closure_north_america_machine_protocol

Source line: 8861.
Before: The directive and the human exception board work from one corrected roll. Districts left out of the old records now appear on the service list.

After: The directive and the human exception board work from one corrected roll. Districts left out of the old population lists now appear on the service list.

### fallout_orientation_cell_resource_opening_europe_machine_protocol

Source line: 8961.
Before: The command node remains inside a flood-control and transport system with conflicting national records. Pumps, signals, cooling, and shelter ventilation are kept running by thresholds no one has reviewed.

After: The command node remains inside a flood-control and transport system with conflicting national population lists. Pumps, signals, cooling, and shelter ventilation are kept running by thresholds no one has reviewed.

### fallout_orientation_cell_closure_europe_machine_protocol

Source line: 8969.
Before: The control room, the credential panel, and the pump engineers work from one corrected record. Flood gates open on rules that every district can read.

After: The control room, the credential panel, and the pump engineers work from one corrected population list. Flood gates open on rules that every district can read.

### fallout_orientation_cell_resource_result_europe_mutant_polity

Source line: 8981.
Before: Joint clinic staff and ward delegates signed the same housing and transit record.

After: Joint clinic staff and ward delegates signed the same housing and transit agreement.

### fallout_orientation_cell_resource_result_eurasian_interior_quarantine_state

Source line: 9044.
Before: Sanitary train doctors and well guards signed the same screening record.

After: Sanitary train doctors and well guards agreed on the same screening rules.

### fallout_orientation_cell_resource_opening_eurasian_interior_machine_protocol

Source line: 9069.
Before: The command system remains beneath a radar or rail-control site with fragmented maps and old borders. District heating, signals, pumps, and sealed depots are serviced by occupancy records that are years out of date.

After: The command system remains beneath a radar or rail-control site with fragmented maps and old borders. District heating, signals, pumps, and sealed depots are serviced by occupancy lists that are years out of date.

### fallout_orientation_cell_resource_result_east_asia_quarantine_state

Source line: 9152.
Before: Port health officers and ward doctors signed the same screening record.

After: Port health officers and ward doctors agreed on the same screening rules.

### fallout_orientation_cell_resource_opening_east_asia_machine_protocol

Source line: 9177.
Before: The node survives beneath a factory, flood-control center, or transport network with incomplete household records. River gates, pumps, rail signals, shelter air, and refrigeration are kept in a dependency order no one has checked.

After: The node survives beneath a factory, flood-control center, or transport network with incomplete household lists. River gates, pumps, rail signals, shelter air, and refrigeration are kept in a dependency order no one has checked.

### fallout_orientation_cell_government_opening_east_asia_machine_protocol

Source line: 9180.
Before: Civil-defense and production directives allocate survival resources by system demand, but human technicians challenge invalid records and production rules that exclude new wards.

After: Civil-defense and production directives allocate survival resources by system demand, but human technicians challenge invalid household lists and production rules that exclude new wards.

### fallout_orientation_cell_government_division_east_asia_machine_protocol

Source line: 9182.
Before: Seat a human records commission beside the directives.

After: Seat a human shelter commission beside the directives.

### fallout_orientation_cell_closure_east_asia_machine_protocol

Source line: 9185.
Before: The directives and the human records commission work from one corrected register. New wards appear on the service list.

After: The directives and the human shelter commission work from one corrected register. New wards appear on the service list.

### fallout_orientation_cell_resource_result_east_asia_mutant_polity

Source line: 9197.
Before: Mixed clinic councils and ferry crews signed the same inspection record.

After: Mixed clinic councils and ferry crews signed the same inspection certificate.

### fallout_orientation_cell_resource_result_south_asia_quarantine_state

Source line: 9260.
Before: Camp health directors and water-testing crews signed the same screening record.

After: Camp health directors and water-testing crews agreed on the same screening rules.

### fallout_orientation_cell_resource_opening_south_asia_scavenger_syndicate

Source line: 9267.
Before: The government sits in a wholesale district or rail workshop where salvage feeds the shelters but unsafe crews multiply. Pumps, generators, rail parts, medicine stores, and building materials change hands without a record.

After: The government sits in a wholesale district or rail workshop where salvage feeds the shelters but unsafe crews multiply. Pumps, generators, rail parts, medicine stores, and building materials change hands without a cargo manifest.

### fallout_orientation_cell_resource_result_south_asia_mutant_polity

Source line: 9305.
Before: Mixed settlement councils and clinic physicians signed the same housing and well record.

After: Mixed settlement councils and clinic physicians signed the same housing and well agreement.

### fallout_orientation_cell_resource_result_middle_east_north_africa_quarantine_state

Source line: 9368.
Before: Border physicians and water certification crews signed the same screening record.

After: Border physicians and water certification crews agreed on the same screening rules.

### fallout_orientation_cell_resource_result_middle_east_north_africa_mutant_polity

Source line: 9413.
Before: Mixed clinic directors and family councils signed the same well and housing record.

After: Mixed clinic directors and family councils signed the same well and housing agreement.

### fallout_orientation_cell_resource_result_sub_saharan_africa_quarantine_state

Source line: 9476.
Before: Mobile clinic directors and water-testing crews signed the same screening record.

After: Mobile clinic directors and water-testing crews agreed on the same screening rules.

### fallout_orientation_cell_resource_result_sub_saharan_africa_mutant_polity

Source line: 9521.
Before: Mixed clinic boards and safe-work advocates signed the same water and work record.

After: Mixed clinic boards and safe-work advocates signed the same water and work agreement.

### fallout_orientation_cell_resource_result_latin_america_caribbean_quarantine_state

Source line: 9584.
Before: Port physicians and water laboratories signed the same screening record.

After: Port physicians and water laboratories agreed on the same screening rules.

### fallout_orientation_cell_resource_result_latin_america_caribbean_mutant_polity

Source line: 9629.
Before: Mixed settlement physicians and land councils signed the same plot and housing record.

After: Mixed settlement physicians and land councils signed the same plot and housing agreement.

### fallout_orientation_cell_resource_result_oceania_remote_islands_quarantine_state

Source line: 9692.
Before: Port health officers and floating clinic staff signed the same screening record.

After: Port health officers and floating clinic staff agreed on the same screening rules.

### fallout_orientation_cell_resource_opening_oceania_remote_islands_nomad_convoy

Source line: 9708.
Before: The moving government is a refugee flotilla choosing between a cold southern route, a crowded safe harbor, and an isolated island. Fuel, water makers, fishing gear, seed, and navigation records are spread across the boats.

After: The moving government is a refugee flotilla choosing between a cold southern route, a crowded safe harbor, and an isolated island. Fuel, water makers, fishing gear, seed, and navigation charts are spread across the boats.

### fallout_orientation_cell_tailored_resource_oceania_remote_islands_nomad_convoy

Source line: 9709.
Before: Pool the fuel, water makers, fishing gear, seed, navigation records, and repair labor

After: Pool the fuel, water makers, fishing gear, seed, navigation charts, and repair labor

### fallout_orientation_cell_resource_result_oceania_remote_islands_mutant_polity

Source line: 9737.
Before: Mixed clinic teams and resident councils signed the same berth and housing record.

After: Mixed clinic teams and resident councils signed the same berth and housing agreement.

### fallout_office_candidate_1

Source line: 10063.
Before: Emergency Records Commissioner

After: Emergency Relief Commissioner

### fallout_office_candidate_34

Source line: 10096.
Before: Human Survival Records Officer

After: Human Survival Officer

### fallout_office_candidate_235

Source line: 10233.
Before: Human Records Commission

After: Human Shelter Commission

### air_cleanliness_treaty_call_relief_vote_desc

Source line: 10857.
Before: Put [FROM.GetNameDef]'s worst-hit state before the treaty and ask every signatory to answer on the record. A member that votes yes promises to send relief if the vote passes.

After: Put [FROM.GetNameDef]'s worst-hit state before the treaty and ask every signatory to give a public answer. A member that votes yes promises to send relief if the vote passes.

### chaosx_air_treaty.18.d

Source line: 10880.
Before: [air_cleanliness_treaty_relief_vote_caller.GetNameDef] has called the treaty to vote on relief for [air_cleanliness_treaty_relief_vote_state.GetName], where [air_cleanliness_treaty_relief_vote_recipient.GetNameDef] can no longer feed or shelter everyone left in the cold. Every member's answer goes on the record. A yes vote is a promise: if the vote passes, every yes voter that can sends support equipment.

After: [air_cleanliness_treaty_relief_vote_caller.GetNameDef] has called the treaty to vote on relief for [air_cleanliness_treaty_relief_vote_state.GetName], where [air_cleanliness_treaty_relief_vote_recipient.GetNameDef] can no longer feed or shelter everyone left in the cold. Every member's answer is made public. A yes vote is a promise: if the vote passes, every yes voter that can sends support equipment.

### chaosx_air_treaty.23.signed.d

Source line: 10917.
Before: [fallout_treaty_reconstruction_proposer.GetNameDef] and [fallout_treaty_reconstruction_partner.GetNameDef] have signed the reconstruction compact. Surviving clerks of the Air Cleanliness Treaty have reopened its archive in borrowed rooms, matched the old sampling records against the new ruins, and drawn up a shared list of what can still be rebuilt.

After: [fallout_treaty_reconstruction_proposer.GetNameDef] and [fallout_treaty_reconstruction_partner.GetNameDef] have signed the reconstruction compact. Surviving clerks of the Air Cleanliness Treaty have reopened its archive in borrowed rooms, matched the old sampling notes against the new ruins, and drawn up a shared list of what can still be rebuilt.

### fallout_treaty_reconstruction_compact_desc

Source line: 10937.
Before: The surviving clerks of the Air Cleanliness Treaty share their archive, sampling records, and salvage lists between former signatories.

After: The surviving clerks of the Air Cleanliness Treaty share their archive, sampling notes, and salvage lists between former signatories.

### chaosx.fallout.298.research.failure.d

Source line: 2328.
Before: The clinic treated its records as proof before it could treat the people who carried them. A failed test, a dark lamp, and a missing medicine crate have made the ward a warning about research without a public duty.

After: The clinic trusted its case notes before it could treat the people who carried them. A failed test, a dark lamp, and a missing medicine crate left the former dormitory without reliable care.

### chaosx.fallout.300.success.d

Source line: 2339.
Before: The former dormitory has become an institution the country can name. Its doors have a keeper, its records have a home, and the next emergency will not begin with a room that everyone remembers but nobody owns.

After: The former dormitory has a keeper, a safe home for its case files, and a place in the country's emergency plan. The next crisis will find a ward that someone is responsible for opening.

### chaosx.fallout.300.partial.d

Source line: 2340.
Before: The ward has a durable purpose in the central shelter, although the outer rooms still borrow its records and supplies. The institution exists, yet the country has not finished making it common.

After: The ward can care for the central shelter, but the outer rooms still borrow its case files and supplies. The country has yet to give every district dependable access.

### chaosx.fallout.46.decentralized.d

Source line: 3049.
Before: Local committees across [air_winter_event_state.GetName] now issue orders suited to streets that central officials cannot reach. Their records differ and their borders move with shelter capacity, but repair work continues wherever a committee can gather tools and residents.

After: Local committees across [air_winter_event_state.GetName] issue orders suited to streets that central officials cannot reach. Their household rolls differ and their borders move with shelter capacity, but repair work continues wherever a committee can gather tools and residents.

### chaosx.fallout.482.partial.d

Source line: 3302.
Before: The second sowing is uneven, but enough beds take root to keep the state from repeating the false spring. The record names the districts that still need shelter and seed.

After: The second sowing is uneven, but enough beds take root to keep the state from repeating the false spring. The growers have named the districts that still need shelter and seed.

### chaosx.fallout.473.daylight_medical_trial.success.d

Source line: 3814.
Before: The clinic tested the dawn air with three independent samples. The opening remains narrow, but the settlement has a record it can read and a nurse willing to sign the next page.

After: The clinic tested the dawn air with three independent samples. The safe interval remains short, but families can read the test results and a nurse has agreed to check the next samples.

### chaosx.fallout.473.sealed_until_clear.success.d

Source line: 3817.
Before: The shelter stayed sealed while the monitors held a clean interval. Children kept their names and lessons in one record, and the first unmasked day will belong to a community that remembers why it waited.

After: The shelter stayed sealed while the monitors held a clean interval. Children continued their lessons together, and the community can take its first unmasked day knowing why it waited.

### chaosx.fallout.473.sealed_until_clear.partial.d

Source line: 3818.
Before: The seal protected the youngest shelters, but workers began opening side doors at night. The records remain intact, although the next public rule will have to answer for those quiet exceptions.

After: The seal protected the youngest shelters, but workers began opening side doors at night. The school rolls remain intact. The next public rule must address those quiet breaches.

### fallout.event_log.first_unmasked_day.sealed_until_clear_success

Source line: 3839.
Before: A sealed shelter preserved the record until a clean interval held.

After: The shelter stayed sealed and kept its children together until the monitors held a clean interval.

### fallout_rail_forced_labor_corridor_desc

Source line: 4532.
Before: Military labor orders have restored a rail line while damaging cohesion and leaving a contested record of the work.

After: Military labor orders restored the rail line, but the forced work damaged cohesion and left the crews disputing how they were treated.

### chaosx.fallout.637.military.failure.d

Source line: 5334.
Before: The garrison took the pass before the census was signed. Equipment disappeared into separate depots, the road works were damaged during the seizure, and the shelter hall now records military settlement as another name for exclusion.

After: The garrison took the pass before the census was signed. Equipment disappeared into separate depots, the road works were damaged during the seizure, and families were excluded from the shelter.

### chaosx.fallout.583.invalid.d

Source line: 5792.
Before: The intake changed hands before the seasonal review. The river agreement has been closed, and the surviving crews are carrying the records away from the station.

After: The intake changed hands before the seasonal review. The river agreement has been closed, and the surviving crews are carrying the valve instructions away from the station.

### fallout.event_log.nile_pump_congress.detail.cancelled

Source line: 5819.
Before: The Nile Pump Congress record could not be confirmed after the intake changed.

After: The Nile Pump Congress review ended when the intake changed hands.

### fallout.event_log.old_airfield_chain.detail.cancelled

Source line: 5890.
Before: The Old Airfield record could not be confirmed after its target or authority changed.

After: The Old Airfield review ended when the runway or its authority changed.

### chaosx.fallout.1023.d

Source line: 5923.
Before: Keep the records under seal

After: Keep the clinic files under seal.

### fallout.event_log.old_doctor_trial.detail.public_trial_success

Source line: 5952.
Before: A public trial removed clinical authority from the former director and restored a shared ward record.

After: The public trial removed the former director's clinical authority and restored a shared ward case file.

### chaosx.fallout.373.c

Source line: 5989.
Before: Share the records

After: Share the weather observations.

### chaosx.fallout.373.d_option.tt

Source line: 5992.
Before: Spend a small Fuel, Power, and Recognition reserve to leave a sealed station log. The tower stops serving the country, but the records may remain for a later expedition.

After: Spend a small Fuel, Power, and Recognition reserve to leave a sealed station log. The tower stops serving the country, but its weather observations may remain for a later expedition.

### chaosx.fallout.375.abandon_station.success.d

Source line: 6004.
Before: The tower crew sealed the radio batteries, wrapped the notebooks in waxed cloth, and marked the safe approach across the snowfield. No current government receives a warning, but the next expedition will find an honest record.

After: The tower crew sealed the radio batteries, wrapped the notebooks in waxed cloth, and marked the safe approach across the snowfield. No current government receives a warning, but the next expedition will find reliable weather observations.

### fallout.event_log.orientation.detail.national_household_failure

Source line: 6165.
Before: Household work crews could not hold the ration line, and the first national orientation record carries deaths, missing filters, and a broken promise to the wards.

After: Household work crews could not hold the ration line. People died, filters went missing, and the wards were left without the promised support.

### chaosx.fallout.76.rival.failure.d

Source line: 6310.
Before: [This.GetFalloutOrientationGovernmentCountryResultText] The rival rejected the offered mandate and withdrew its people, records, or guards. The rupture damaged recognition and cohesion before the next orders could leave.

After: [This.GetFalloutOrientationGovernmentCountryResultText] The rival rejected the offered mandate and withdrew its people, household lists, or guards. The rupture damaged recognition and cohesion before the next orders could leave.

### fallout_orientation_invalid_country_memory

Source line: 6472.
Before: The government's records are too incomplete to describe its first months.

After: Too little is known about the government's first months.

### chaosx.fallout.698.d

Source line: 6645.
Before: The Quarantine State discovers that paper movement permits are being traded at the ash gate. The clinic still controls the red seal, the roads are freezing, and a market has formed where a public rule should stand. The state must decide whether access is a service, a record, or a price.

After: The Quarantine State discovers that paper movement permits are being traded at the ash gate. The clinic still controls the red seal, the roads are freezing, and a market has formed where a public rule should stand. The state must decide whether travel depends on public service, verifiable permits, or payment.

### chaosx.fallout.700.issue.success.d

Source line: 6655.
Before: Local offices issued passes by household and kept the clinic's red seal attached to a reviewable record. The ash road opened for work and care, and the Quarantine State gained a movement rule that did not depend on a single guard.

After: Local offices issued passes by household and made the clinic's red seal subject to appeal. The ash road opened for work and care, and travelers no longer depended on a single guard.

### chaosx.fallout.600.c.tt

Source line: 6923.
Before: Spend Fuel, Scrap, and Recognition while committing enough Power to copy the current signal table into neighboring harbors. The chain gains outside contact, but its records no longer belong to one country.

After: Spend Fuel, Scrap, and Recognition while committing enough Power to copy the current signal table into neighboring harbors. The island chain gains outside contact, but its signal tables no longer belong to one country.

### chaosx.fallout.812.negotiate_safe_roster.success.d

Source line: 7156.
Before: The operators accepted a safe rotation after the Manchurian Reactor Keeps published every handover and gave the night crew a veto over a redline shift. The turbine ran below peak output, but the safety board became a living record that the technate could not quietly rewrite.

After: The operators accepted a safe rotation after the Manchurian Reactor Keeps published every handover and gave the night crew a veto over a redline shift. The turbine ran below peak output, but the safety board could challenge any attempt by the technate to change the agreed rules.

### fallout.event_log.repair_charter.detail.licensed_houses_failure

Source line: 7468.
Before: A withheld service record turned a clinic repair into a toll dispute.

After: A withheld bearing specification turned a clinic repair into a toll dispute.

### chaosx.fallout.305.religious.success.d

Source line: 7929.
Before: Congregations open their books and accept witnesses from outside their own doors. Their marriage rites become a careful bridge between old faiths, new shelters, and families who kept no record.

After: Congregations open their books and accept witnesses from outside their own doors. Their marriage rites help old faiths, new shelters, and families who have no marriage papers recognize each other's households.

### fallout.event_log.shelter_marriage_law.religious_partial

Source line: 7952.
Before: Congregations kept records while unaligned families waited.

After: Congregations kept marriage books while unaligned families waited.

### fallout_shelter_marriage_failed_desc

Source line: 7971.
Before: Conflicting records make ration inheritance and guardianship harder to settle.

After: Conflicting family papers make ration inheritance and guardianship harder to settle.

### chaosx.fallout.431.bind_state_service.partial.d

Source line: 8046.
Before: The service office keeps the list moving, but its escorts arrive late at the frost line. The specialists accept the seal for now, while families record every requisition that leaves a clinic without a replacement.

After: The service office keeps the list moving, but its escorts arrive late at the frost line. The specialists accept the seal for now, while families note every requisition that leaves a clinic without a replacement.

### chaosx.fallout.431.allow_self_government.success.d

Source line: 8048.
Before: The specialist quarter receives its own water rota, clinic council, and repair court. It answers for the boundary wall and shares its records with the country. The quarter keeps its names, while the country gains a neighbour instead of another department.

After: The specialist quarter receives its own water rota, clinic council, and repair court. It answers for the boundary wall and shares its work notes with the country. Its residents retain their names and local authority.

### chaosx.fallout.433.partial.d

Source line: 8055.
Before: The review finds useful work and several empty seats. The guild, office, or quarter has kept its records, but the next generation still depends on a few people who cannot be in every room at once.

After: The review finds useful work and several empty seats. The guild, office, or quarter has kept its work notes, but the next generation still depends on a few people who cannot be in every room at once.

### fallout.event_log.skilled_list.allow_self_government_success

Source line: 8070.
Before: A specialist quarter kept its council while sharing records with the country.

After: A specialist quarter kept its council while sharing work notes with the country.

### fallout_orientation_cell_resource_opening_north_america_mutant_polity

Source line: 8871.
Before: The government sits in a mixed surface settlement beside a sealed medical and industrial zone whose records no one trusts. Altered and unaltered families share failing water, clinic, food, and housing systems.

After: The government sits in a mixed surface settlement beside a sealed medical and industrial zone whose test results no one trusts. Altered and unaltered families share failing water, clinic, food, and housing systems.

### fallout_orientation_cell_resource_result_north_america_mutant_polity

Source line: 8873.
Before: Clinic staff and household delegates signed the same monitoring record for every family.

After: Clinic staff and household delegates agreed on the same monitoring rules for every family.

### fallout_orientation_cell_resource_result_europe_quarantine_state

Source line: 8936.
Before: Railway doctors and port inspectors signed the same water and evacuation record.

After: Railway doctors and port inspectors agreed on the same water and evacuation rules.

### fallout_orientation_cell_government_rival_east_asia_machine_protocol

Source line: 9183.
Before: Give the senior technicians authority to correct the records.

After: Give the senior technicians authority to correct the household lists.

### fallout_orientation_cell_government_rival_sub_saharan_africa_machine_protocol

Source line: 9507.
Before: Give the relay teams authority to correct the records.

After: Give the relay teams authority to correct the household lists.

## Retained navigators

- chaosx.fallout.770.rescue_articles.partial.d: The charter reached the dock crews and two river pilots. The council gained a working rescue roster, but the outer anchorage still treats berth access as a captain's favor.
- chaosx.fallout.777.approach.partial.d: The search skiff exchanged a crate of medicine for a route marker and returned with two frightened pilots. The convoy kept its cargo hold closed, but the port can read the next signal.
- fallout.event_log.ghost_convoy.detail.approach_success: The search skiff returned with pilots, a chart, and a named route.
- fallout.event_log.ghost_convoy.detail.approach_partial: The search skiff traded medicine for a route marker and two pilots.
- fallout_orientation_cell_closure_eurasian_interior_maritime_remnant: Ice pilots, river flotillas, and army convoys keep one route list. Settlements on the frozen rivers know when rescue will come.
- fallout_orientation_cell_closure_sub_saharan_africa_maritime_remnant: Port market captains, river pilots, and dock cooperatives keep one sailing list. Inland food reaches the coast on agreed boats.
- fallout_orientation_cell_closure_latin_america_caribbean_maritime_remnant: Convoy captains, river pilots, and fisher councils keep one sailing list. Displaced craft land by the same rules as the fishing fleet.
- fallout_office_candidate_185: Ice Pilot
- fallout_office_candidate_330: River Pilot
- fallout_office_candidate_367: River Pilots' Guild
