# Mengele native cloning completion

The dedicated cloning completion effect grants the initial clone programme once per country through its durable germany_mengele_cloning_project_completed receipt.
The legacy sp_mengele_cloning project and the Event 016 native bridge both use this effect.
The helper checks its own receipt before any output and records it before selecting refinement, producing the initial equipment, or scheduling the existing revolt event.
A duplicate callback therefore cannot repeat that initial payload or queue another revolt through this helper.

The first completion keeps the original effect order and payload.
It clears germany_mengele_cloning_unlock_pending, records directorate_special_project_cloning_completed, selects Mengele refinement, produces the initial equipment through germany_mengele_produce_clone_equipment, and conditionally schedules germany_mengele.24.
The existing weekly and programme transition replenishment callers continue to call the separate production helper.
There is no completion-latch clear in the current common or events source inventory.

## Scope and presentation

The helper runs in country scope in common/scripted_effects/germany_mengele_effects.txt.
Its two existing completion callers are common/special_projects/projects/mengele_cloning_projects.txt and common/scripted_effects/016_mengele_project_bridge_effects.txt.
The existing sp_mengele_cloning_completed_tt and the Event 016 stage tooltips describe the unchanged first output.
This internal guard adds no icon or visual asset.
The legacy project uses the existing GFX_sp_mengele_cloning icon, and Event 016 Cloning stages use the existing family stage sprites documented in mengele_cloning_stages.md.

## Reference evidence

The live reference context, search, and source lookup were requested for the helper before editing.
The country-flag trigger search and revision-bound read completed at installed triggers_documentation.md:3624-3638, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.
The event context with limit3 omitted eight general topic sources, so it is not claimed as complete event-topic coverage.
The targeted direct sections below cover the flag syntax used by this small guard.
The exact helper source_lookup request timed out after600 seconds, and the local definition and two caller blocks were read directly.
While those requests were pending, the pertinent installed documentation and offline wiki sections were read directly.

| Source | Read span | SHA-256 |
| --- | --- | --- |
| paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md, Flags | 102-123 | 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |
| Installed documentation/triggers_documentation.md, has_country_flag | 3624-3638 | 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29 |
| Installed documentation/effects_documentation.md, set_country_flag and clr_country_flag | 6730-6737, 2792-2800 | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| Vanilla common/scripted_effects/GER_scripted_effects.txt, GER_add_mefo_bills_penalty guard | 818-832 | 1d6b5cc8e00d685aa3c95cecab41cfeb2da590e90490de5dcce05e8e8e2beeb3 |

## Validation and remaining work

A direct source comparison confirms every original completion effect remains in the same order inside the new flag guard.
Source inventory identifies both callers, the separate replenishment paths, and the existing alternative writer of the completion flag in the deterministic Directorate selector.
The bounded MCP impact request lost its execution handle after the app connection reset and did not deliver evidence.
The independent bounded guard review is 016_cloning_completion_guard_review_2026-10-03.md and confirms the shared latch and unchanged payload order.
Its review excludes the separate custom technology grant after the legacy project output, whose idempotence belongs to the existing custom API.
No runtime outcome is claimed for this guard.

This guard closes the duplicate-payload defect in the shared helper.
Exact provider Prototype ownership, historical completion isolation, cloning project availability overlap, and the full lifecycle matrix remain separate Event 016 completion work.
Future review should keep initial completion distinct from periodic clone equipment replenishment and authenticate the Event 016 project receipt independently of the shared legacy completion flag.

## Private and legacy native availability

The private provider gate for sp_brilliant_scientist_cloning uses the private Theory and Prototype receipts and the exact accepted project's completed state.
The shared directorate_special_project_cloning_completed latch is not proof of that private project and does not veto its availability.
The legacy sp_mengele_cloning retains its original camp eligibility and uses brilliant_scientist_mengele_legacy_cloning_project_is_available for its two country-scoped presentation gates.
A registered Event016 Mengele portfolio owner cannot open a further legacy research job through that gate, including during an incident when the strict live-provider predicate is suspended.
An exact legacy job already being researched remains reachable while the original camp eligibility holds.
Outside the registered portfolio owner context, the wrapper adds no restriction to the original camp gate.
The existing legacy costs, AI weights, output, equipment, refinement, and ordinary CBRN consumers are unchanged.
The internal owner checks are hidden from requirement tooltips.

The installed triggers_documentation.md:6228-6241 documents is_special_project_being_researched in COUNTRY scope and gives a literal sp: project example.
The projects/documentation.md:36-46 documents available and visible in PROJECT scope with FROM as country, so the wrapper is invoked inside the existing FROM blocks.
Offline Scopes:25-40 and63-79 documents trigger conjunction and matching scope types, revision18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49.
Offline Triggers:344-347 and406-416 documents hidden_trigger, revisionabc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06.
The original camp gate and the existing legacy project's FROM structure are the working repository precedents.

The bounded source review is 016_cloning_native_availability_review_2026-10-03.md.
The desktop HOI4 routes remain unexposed after the app reset, and the narrower installed-service domain requests timed out as recorded in native_stage_completion_hooks.md.
No live availability or native research continuation result is claimed from the source gate alone.
The separate pending commitment and exact ownership migration remain queued under the architecture handoff.
