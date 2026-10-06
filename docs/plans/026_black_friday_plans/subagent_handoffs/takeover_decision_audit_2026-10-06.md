# Event 026 Black Friday decision and mission audit, 2026-10-06

Disposition: read-only audit. I changed no gameplay source and made no commit. This handoff is the only file written by this subagent.

## Severity-ranked findings

### P1 — Native sale factors can become stale during the one-day sale and make a positive purchase free

D36 calculates the native sale contributions when black_friday_native_sale_apply runs. The contribution then remains stored in a country variable until another explicit status refresh. Current refresh call sites are sale activation, the sale-report option, tag switching, and event-system enable/resume handling: common/scripted_effects/026_black_friday_effects.txt:968, :2402-2425, :4302; common/on_actions/chaosx_on_actions_system.txt:114; common/scripted_effects/chaosx_settings_effects.txt:2917.

If an ordinary -25% cost factor is added after the 75% sale contribution was calculated at a zero ordinary factor, the stored -75% contribution plus the new -25% ordinary factor can total -100%. The positive purchase becomes free until the next explicit refresh. Removing or changing an ordinary factor can also leave the sale amount inaccurate. This is a source-level counterexample, not only a pending live check.

The current registry already records this as D42: an ordinary discount acquired after the stored contribution can make a positive purchase free before another explicit refresh (docs/plans/026_black_friday_plans/event26_cost_surface_registry.md:44-50). The offline modifier reference says modifier contributions add into one scope total and dynamic modifiers recalculate from their variable values daily (paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md:57-59, :112-121). That daily evaluation does not refresh the stored black_friday_sale_* input variables.

I found no on_idea_added, on_idea_removed, advisor-change, or law-change callback in the offline On actions page, installed on-action documentation, or installed common/on_actions/00_on_actions.txt. Keep exact native composition blocked until a safe refresh route exists. A per-purchase refresh or targeted owner call sites could address it; a new daily country-wide scan would violate the accepted performance contract.

### P2 — Native achievement inference still does not prove paid experience or command-power purchases

The parent-added political-power snapshot and guards now require a net PP decrease before laws or political-advisor increases count, and a net PP or command-power decrease before senior staff increases count: common/scripted_effects/026_black_friday_effects.txt:154-175, :186-239. This reduces the false-credit window for institutional families.

Army, navy, and air experience plus command power families still credit from a net balance decrease alone at common/scripted_effects/026_black_friday_effects.txt:240-266. A scripted effect, event, or other non-purchase loss can therefore be mistaken for a qualifying paid transaction; same-day gains can also hide genuine spending. The accepted Part 7 transaction contract requires a positive ordinary cost, positive discounted payment, successful commitment, and registry family membership (docs/specs/026_black_friday_specs/026_black_friday_spec_part_7_assets_and_achievement.md:66-97). Agent decision D6 chose snapshots because native law/hire/spend hooks were unavailable and explicitly accepted that focus/event changes could count (docs/plans/026_black_friday_plans/agent_decisions_2026-10-04.md:82-93).

Treat the native snapshot as a bounded inference, not proof of exact purchase transactions. Reconcile D6 and the comment at common/scripted_effects/026_black_friday_effects.txt:67-79 with the parent-added PP/CP guards. The comment still says a focus or event law, slot, or resource change counts without describing the new net-spend condition.

### P2 — Overall purchase coverage remains incomplete

The decision-price registry scan below passes for direct native decision costs that already use the Black Friday table. It does not make all Chaos Redux custom-cost owners sale-priced. The registry says semantic decomposition and full final-commit reconciliation are still open and records 2,342 active custom-cost declarations, 2,343 custom-cost texts, and 1,316 active native cost declarations across the mod (docs/plans/026_black_friday_plans/event26_cost_surface_registry.md:7-8, :23-36). The 2026-10-05 adoption rescan records 124 newer Event 006 costs as owner-adoption-pending (docs/plans/026_black_friday_plans/owner_adoption_requests.md:61).

The player-facing popup lists base-game exclusions and says eligible purchases receive the sale price. Keep the event completion claim limited to registered/adapted surfaces until the owner registry is complete.

### P3 — The failure report is bounded and clear; its once-per-country behavior is permanent

The parent-added no-op path captures active, fired, disabled, paused, world-end, reserved, and below-chaos reasons, then sends chaosx.nr26.3 only to a human manual/force caller whose notice flag is not set: common/scripted_effects/026_black_friday_effects.txt:4461-4506. Event 3 has matching conditional descriptions and clears the captured reason when dismissed: events/026_black_friday.txt:34-71. All seven keys are present in English localization and contain no report-color codes: localisation/english/026_black_friday_l_english.yml:85-93.

black_friday_entry_notice_shown remains set for the campaign after the first notice. This gives the requested anti-spam behavior, one rejection notice per human country; later distinct failures for that country stay quiet. The automatic reservation path remains silent. I found no duplicate-notice defect in source.

## Lifecycle and category notes

The lifecycle triggers gate reservation on an active event system, enabled state, unfired/unreserved/inactive state, and at least 200 chaos: common/scripted_triggers/026_black_friday_triggers.txt:9-89. Natural selection reserves once, completes its timer path, and activates immediately only when the selected date is Friday. The bounded global pulse activates the reservation on the first eligible Friday, skips low-chaos Fridays, cancels a disabled reservation, and expires the active source on the next daily tick: common/scripted_effects/026_black_friday_effects.txt:2405-2441, :4239-4459. Force mode bypasses the chaos and weekday gates while retaining disabled, active, fired, and system-running guards; activation marks forced or manual runs ineligible for the achievement.

The normal player surface has no Event 026 decision category or mission family. The shared CXT debug category contains its sole dedicated decision, the Black Friday price probe in common/decisions/026_black_friday_cxt_test_decisions.txt:10-22. It has one Political Power cost, is visible only to initialized human CXT, and has ai_will_do base 0. It is a repeatable diagnostic spend with no gameplay reward.

The event-detail status selectors show unavailable, eligible, reserved, active, expired, or disabled states, with the sale percentage and the 600-chaos evolution threshold explained in the visible status/event copy: common/scripted_localisation/026_black_friday_scripted_localisation.txt:38-90; localisation/english/026_black_friday_l_english.yml:17-28. One sale popup is sent to each human country at activation. The manual/force failure report is separately bounded to one per human country per campaign. The current category/action count is below six, active mission count is zero, and the player-facing status values state their cause and consequence. No mission owner, region, requirement, duration, success, failure, or duplicate-risk audit applies because Event 026 defines no mission.

The new sale copy distinguishes rounded decision prices and smaller appointment reductions from the headline sale rate, and the compatibility list names base-game decisions, guarantees, intelligence, licenses, MIOs, upgrades, leader promotions, traits, tactics, and special projects as normal-price surfaces: localisation/english/026_black_friday_l_english.yml:7, :13, :17. The requirement flag black_friday_active is localized in localisation/english/026_black_friday_requirement_flags_l_english.yml:4. No raw requirement key or cost resource label was found in the CXT probe.

## Price table and refund audit

A read-only source-set audit of all common/decisions/*.txt files and the 026 price table at current version 18 found:

- 31 literal price-table keys, each with a corresponding table assignment. Consumption of every literal key was not independently checked.
- 1,066 price-table global assignment keys, all unique with no duplicate declaration.
- 467 direct native decision cost references spanning 155 unique table keys, with zero missing assignments.

The scan validates direct cost-to-table assignment coverage only. It does not validate every owner custom-cost trigger, payment, display, refund, AI, or save-state path.

Parent D43 is present in the current source: black_friday_price_table_refresh_entries now initializes both black_friday_price_payable and black_friday_price_spend before nested quote calls (common/scripted_effects/026_black_friday_price_table_effects.txt:1404-1413), and the event price-table version is 18 (common/script_constants/026_black_friday_constants.txt:73-78). Parent reports three nested Soviet Collapse _spend regressions failed before that caller-owned output repair and passed afterward. My key-set scan did not test helper-return temporary lifetime; D43 repairs that separate defect, and the version bump makes running campaigns rebuild the table.

Refund evidence matches paid prices on the examined paths. The shared refund helper refunds stored actual-paid components and records partial/full refund state (common/scripted_effects/chaosx_universal_cost_effects.txt:1706-1785). The alien-landing adapter acknowledges the exact component, retracts its achievement transaction, refunds the receipt, and clears the receipt only on success (common/scripted_effects/026_black_friday_effects.txt:3920-3945). The Africa elephant custom adapter refunds its recorded actual-paid equipment amount before closing the component path (common/scripted_effects/026_black_friday_effects.txt:4037-4060). The timed Zombie cure decisions store the table price when taken and refund that stored amount on cancellation (common/decisions/002_zombie_outbreak_decisions.txt:277-285, :329-340). Event 015 same-tick refunds use the current price-table amount per decision D10. I found no ordinary-price refund mismatch in these reviewed examples. Other owner rows remain subject to the registry’s pending coverage dispositions.

## Takeover claim reconciliation

The Oct. 4 round-one history summary in C:/Users/klimp/Videos/chaos_redux_trailer/records/cx/phase2_history/026.md predates the Oct. 5 inbox record. The claimed absence of inbox/026.txt is stale; C:/Users/klimp/Videos/chaos_redux_trailer/records/cx/inbox/026.txt exists and contains G1-G9, including the one-notice forced/manual no-op requirement and the low-popup rule.

The early Friday-anchor defect is corrected in constants/026_black_friday_constants.txt:25-32 with friday_remainder 6, consistent with offline Data structures line 1470. D8 lists Event 26 in the default-enabled trigger (common/scripted_triggers/chaosx_settings_triggers.txt:1-28). D36/D37 replace the former flat modifier and license-fee design with the current computed sale carrier and exclude recurring license fees, as stated in agent_decisions_2026-10-04.md:535-560. D42 remains an explicit composition blocker in the current registry at line 44. The current completion registry also remains blocked/incomplete; the former “source-complete” wording is not a full completion basis.

## MCP, documentation, and validation evidence

My live tool inventory exposed the HOI4 reference, source lookup, decision inspection, event inspect/render/compare, script validation, and probability routes. No HOI4 health/version tool was exposed, so I could not verify a server version. No standalone viewer, job, helper-expansion, native-task, or GUI route was needed for this decision audit. No refresh=true call, HOI4 launch, GUI/window operation, or spreadsheet operation was used.

HOI4 event reference context returned status OK in workspace mod_chaos_redux_ea3b2d67c2c0. The context included these offline/installed sources:
- Installed effects documentation: ID 22ac6850d38cfcbcd9843a4b33308ff344734e072b1091f56976ac7156d9a5f3, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.
- Offline Data structures: ID f14465e49809a68e2d566e65d119900781884a569096876a317149af4f3118f, revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4.
- Offline On actions: ID fa085ff7b1e81c987d4090d874df68a1dcb2f584ad358dc29c258de0666dd796, revision 6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a.
- Offline Event modding: ID 7301be784e45a903ff7139af0f86e744532c791d3db4d7ceb50718dcd20e68e3, revision 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d.

The limit-8 context omitted Scopes and Localisation. Bounded reference_read retries for the returned event-context IDs yielded no result within 22 seconds. I read the relevant offline/installed sections directly and retained these paths and lines: Decision modding 284-286 and 357-374; Data structures 549 and 1470; Modifiers 57-59 and 112-121; On actions 95-100; installed effects documentation 4372-4379; installed dynamic_variables_documentation.md 1066-1068; installed common/decisions/_documentation.md 1-46; Triggers 641. Decision AI source references returned by the probability auditor are recorded below.

After the parent’s final edits, script_validate by path returned no result within 35 seconds for events/026_black_friday.txt, common/scripted_effects/026_black_friday_effects.txt, common/scripted_effects/026_black_friday_native_sale_effects.txt, and common/scripted_triggers/026_black_friday_triggers.txt. The narrow event_inspect trace and event_render overview also returned no result within 35 seconds; no artifact, revision, or comparison input returned. I did not run event_compare because there was no current graph artifact or matched current before/after pair. These routes are exposed but nonresponsive in this session; they are not absent.

The scoped probability auditor read these references:
- Decision modding AI: ID 151bbd3b6a875558e43f67a1daa1288c5904dfbedfa09e3fca2e5e42b8ccc58f, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162, lines 357-374.
- Installed country decision docs: ID c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019, lines 1-46.
- is_ai trigger: ID 3df9def003a782f0817bcc5ee0df09acafb5fbcc57d6db9117171907b3007931, revision abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06, line 641.

The probability auditor’s valid source-bound probability_inspect call ended with “timed out awaiting tools/call after 600s.” No probability artifact, scenario hash, comparison ID, or decision weight evaluation was created. A scoped decision_inspect request unexpectedly returned DECISION_ANALYZED_PARTIAL global inventory metadata (8,287 decisions, 2,063 categories, 6,853 paths, 100 unresolved definitions). The auditor did not open or use the broad artifact contents. A narrow source_lookup request resolved mod:common/decisions/026_black_friday_cxt_test_decisions.txt:11 at revision 52417790a2d0678b43a0f6edcbbf0d52d1b08d80eb1080aadb4c451af6b95e1e, but returned location/index metadata only with definitionCount 0. The partial decision-inspect artifact metadata is: source revision a049dddfb21724162f9822bea3a5ada5ebe52940e64a8cd66305e704edb06a8d, report hash 49effb84da4e192e7d18eb80607c20d2c08374767bd57dee1bcfe866cc4203c4, artifact URI hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3fe65559069c2cef724a934dd9fbcd173996949f154b2ac009b5736868261cac/05d4b44f3af4da423b712e4f38beb456cdc57e86529cc93e6dbd93f86b68d3d6/decision-49effb84da4e192e7d18eb80.json. It was partial with decision-coverage validation false and does not resolve the named candidate.

The scoped decision AI source is unambiguous: the CXT probe is human-only and has ai_will_do base 0, so it is not selectable by AI. The offline wiki states decisions default to never chosen absent ai_will_do and base 0 gives zero weight (Decision modding lines 361-372); installed decision docs say visible filters the decision interface (common/decisions/_documentation.md:12-16). This source conclusion does not replace the unresolved MCP probability pass.

## Remaining live and implementation checks

- Confirm natural selection, Friday waiting, same-day Friday activation, chaos-tier snapshot, pause/resume, disable cancellation, terminal cleanup, save/reload, and multiplayer synchronization against Part 8.
- Confirm the CXT table price displays and debits at ordinary, 50%, and 25% payable ratios.
- Confirm native price rounding/debits and overlapping native factors, including a factor added or removed mid-sale.
- Confirm achievement credit and exclusion in a natural sale, including paid PP/CP and experience cases; snapshot checks remain source heuristics.
- Complete owner custom-cost coverage and final implementation-commit reconciliation in the registry.
- Resolve or preserve the exact-composition D42 blocker before claiming the event complete.

Meaningful validation reported from the parent: source tests reproduced three price-table nested-output failures before D43 and passed after the caller-output initialization and version bump. This audit’s own validation was static source-set inspection plus direct file review; MCP validation and live behavior remain unconfirmed.

Parent reports source changes were committed as b8a3f7b95 and 16540a70c. D43 landed after the final MCP validation attempts. The current direct-key scan includes D43, while script_validate and event-chain evidence remain unverified on that final source.

Skills used: chaos-redux-decisions-missions, chaos-redux-events, and chaos-redux-subagents. No skill or gameplay file was changed by this subagent.
