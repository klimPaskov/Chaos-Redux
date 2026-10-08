# Competing biological intelligence operations audit

Date: 2026-10-08.
Mode: bounded read-only source/spec audit and parent implementation map.
Changed files: this handoff only.
No gameplay, index, commit, external tool, or asset changes were made.

## Acceptance basis and disposition

The parent's direct user instruction requires research, real equipment, authorization, and attacks through native raids, with exactly Chemical Raids and Biological Raids, one human/AI executable path, necessary hidden helpers only, and removal of competing public attack adapters.
`docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md:5-17` records the 2026-09-20 user acceptance and supersedes conflicting earlier proposals.
The current requirement-ledger wording is another agent's draft during this task and is disposition evidence only, not independent acceptance evidence.
No later correction in `docs/specs/chaos_warfare_system_specs/corrections/` was found authorizing a public operative-attack exception.
Existing source and earlier descriptions prove that a feature exists, not that it survives the accepted raid-only amendment.

The conflicting operative-interface portions of spec 06 at lines 228, 248-266, the decision prompt at line 76, and the older staged/coding prompts are superseded by amendment 13 and the direct removal instruction.
The ordinary biological project, payload, lifecycle, covert consequences, response, and achievement requirements are retained.
The network, assigned-operatives, intelligence-operation phases, operation-only capture consequences, and operation-only Command Power grant are part of the retiring interface and must be disclosed as retired behavior.
Their existence does not justify a new proxy, extra attack surface, or fabricated native callback.
The older instruction to keep weaponized zombies separate preserves that disease/project/outbreak package, not an exception to the current native attack interface.

## Completion status by surface

| Surface | Status | Evidence and practical limit |
| --- | --- | --- |
| Two CBRN categories | Source implemented | `common/raids/categories/chaosx_raid_categories.txt` defines `chemical_raids` and `biological_raids`, both army-intelligence categories. The separate portal category is unrelated to CBRN. |
| Four ordinary biological raid families | Source implemented, engine evidence partial | Strategic, battlefield, and supply-chain definitions already cover Anthrax, Plague, Tularemia, and Smallpox and dispatch the ordinary lifecycle. |
| Raid-only public attack entry | Incomplete | Four ordinary intelligence operations and one zombie intelligence operation remain in `common/operations/chaosx_bioweapon_operations.txt`. |
| Shared ordinary lifecycle and covert records | Must preserve | Native sabotage already uses the covert lifecycle/achievement route. Event 016 also still emits `operative_release`. |
| Operative capture | Unique retiring behavior, no native replacement proved | Actual `on_operative_captured` has character/operation context. The documented raid instance has actor, victim, state, and province, without an operative pointer or captured-character callback. |
| Zombie native replacement | Present, preservation audit partial | Six hostile/friendly native raids retain profile and outbreak consumers. Their current permission gates differ from the intelligence operation. |
| Covert achievement | Existing source gap | Biological covert operation counting is enclosed by a one-time family-history guard. Three completed covert releases are not proved to produce the required count of three. |
| Operation images/phases/text | Existing, retirement cleanup pending | All five intelligence operations share the eight operation sprites and three custom phases. Do not remove those assets while retaining the zombie operation. |
| Documentation/spec/prompt alignment | Stale | Current operative and sabotage docs still advertise the competing surface. Older operative retention claims require explicit superseded dispositions. |
| Weighted AI/outcome evidence | Blocked or unresolved | Probability subagent found unsupported operation/raid AI adapters and unresolved effect-derived random-list weights. |
| Event completion proof | Partial | Native bridge inspect/render reached four events and eleven unresolved helper nodes. Helper projections and lifecycle passes were deferred. |

## Exact existing replacement map

| Competing public ID and definition line | Native covert replacement | Other existing release choices |
| --- | --- | --- |
| `operation_plant_anthrax_outbreak`, line 92 | `bio_sabotage_anthrax_base`, `bio_sabotage_anthrax_theater`, `bio_sabotage_anthrax_terminal` | `anthrax_strike`, `anthrax_battlefield_dissemination` |
| `operation_plant_plague_outbreak`, line 186 | `bio_sabotage_plague_base`, `bio_sabotage_plague_theater`, `bio_sabotage_plague_terminal` | `plague_strike`, `plague_battlefield_dissemination` |
| `operation_plant_tularemia_outbreak`, line 280 | `bio_sabotage_tularemia_base`, `bio_sabotage_tularemia_theater`, `bio_sabotage_tularemia_terminal` | `tularemia_strike`, `tularemia_battlefield_dissemination` |
| `operation_plant_smallpox_outbreak`, line 374 | `bio_sabotage_smallpox_base`, `bio_sabotage_smallpox_theater`, `bio_sabotage_smallpox_terminal` | `smallpox_strike`, `smallpox_battlefield_dissemination` |
| `operation_plant_weaponized_zombie_outbreak`, line 470 | `weaponized_zombie_strike_low`, `weaponized_zombie_strike_medium`, `weaponized_zombie_strike_high` | Matching `_friendly` variants in the separate friendly raid file |

Ordinary covert replacements live in `common/raids/biological_sabotage_raids.txt:64-1642`, call `biological_native_raid_bridge.2`, and reach `bio_resolve_supply_chain_raid_outcome` in `common/scripted_effects/biological_sabotage_raid_effects.txt:161`.
Strategic replacements live in `common/raids/biological_raids.txt:100,515,930,1345`, call bridge `.3`, and reach `bio_resolve_strategic_raid_outcome` in `biological_raid_effects.txt:570`.
Battlefield replacements live in `common/raids/biological_battlefield_raids.txt:76,246,319,392`, call bridge `.1`, and reach `bio_resolve_battlefield_dissemination`.
All three bridges are immediate hidden actor-country events in `events/biological_native_raid_bridge_events.txt:9,69,130`.
Their callback-owned regular targets identify exact actor, victim, selected state, agent, and outcome.
Bridge `.4` owns facility recovery and is not a covert attack replacement.

These are capability replacements, not equal copies of the retiring equipment bill, target profiles, time, network, or operative requirements.
The four intelligence operations use native intelligence-operation equipment, projects, network strength, two or three operatives, exact selected states, and 105-210 days.
They are not decision-based attacks.
The twelve native sabotage definitions instead reserve payload/support equipment and Command Power, assign a land division from a supply-node origin, use native timers and doctrine tiers, and retain their own state profiles and cooldowns.
Their stock/CP reservations are Anthrax 10/40/12, Plague 12/50/15, Tularemia 10/40/12, and Smallpox 8/60/20.
No new raid type, weapon selector, staging decision, offensive preparation decision, or attack decision is required to retire the competing interface.
Do not copy the intelligence-operation equipment costs or scripted Command Power recovery into these native callbacks.

## Unique consumers and preservation boundary

### Ordinary operation-exclusive code

`common/scripted_effects/biological_operation_effects.txt` owns the complete `bio_operative_release_*` resolver/attempt/seed/Command Power/capture family.
Its `bio_operative_release_dispatch_seed_internal:105` is the unpatched remaining consumer from the parent's former eleven-caller inventory.
This audit recommends structural retirement rather than spending a lifetime repair on a competing public adapter.
`common/scripted_triggers/biological_operation_triggers.txt` owns the operation actor, exact agent/state, native context, country AI, capture token/context, and seeded-episode matching gates.
`common/on_actions/chaosx_on_actions_biological_operations.txt:10` calls the capture adapter only for the four ordinary operation tokens.
No external reader of `bio_operative_release_attempt_count`, its last-result fields, Command Power refund ledger, or `bio_confirmed_operative_capture_count` was found in the bounded gameplay/localisation scan.

Capture records either confirm a matching live episode or record an actual attempt without false weapon-use, treaty, death, contamination, or medical-saturation proof.
The exclusive capture chain writes `bio_confirmed_operative_capture_history`, `bio_last_confirmed_operative_capture_*`, per-agent operative capture/confirmed-attempt history, and the shared covert-discovery/coverup flags.
`bio_lifecycle_confirm_operative_release_from_capture` in `biological_lifecycle_effects.txt:1614-1672` depends on the exclusive capture-match trigger.
If the ordinary operation package is removed, remove this now-exclusive helper coherently or retain a documented genuine remaining caller.
No genuine other caller was found.
Do not leave a dangling trigger, fire a synthetic capture, select a random commander, or use stock/raid success as an operative-capture proxy.
The latest removal authority permits retiring this operation-specific behavior with disclosure.
If an independently accepted future capture requirement is later produced, that requirement is blocked until a real supported native consumer is proved.

### Shared code that must remain

Keep `constant:bio_lifecycle_route.operative_release` and its profile, eligible-route checks, shared detection/attribution handling, achievement classification, and log localisation.
`common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt:88` still emits this route from its native owner.
The parent is repairing that separate native adapter, so deletion or renumbering of the shared token would break current content.
Keep `cbrn_achievement_covert_discovered_history`, `cbrn_achievement_covert_coverup_history`, covert operation/result history, operation-type history, the achievement ID `chaos_warfare_clean_hands_dirty_work`, and its trigger/localisation.
`cbrn_achievement_effects.txt:455-468` already accepts either `operative_release` or `food_water_medical_sabotage` as biological covert delivery.
Shared lifecycle discovery at `biological_lifecycle_effects.txt:1476-1567` still sets covert-discovery history for both route families.
Native sabotage also preserves failed-attempt evidence, exact-state lifecycle seeding, Condemnation, domestic consequence handling, humanitarian-corridor calls, and UWR aftermath marking.
No live operative adapter is needed to keep those shared capabilities.

The covert count at `cbrn_achievement_effects.txt:466-467` is inside `NOT = { has_country_flag = cbrn_achievement_operation_biological_covert_history }`.
The other writer at lines 281-282 belongs to `cbrn_achievement_record_chemical_action`.
The biological lifecycle calls `cbrn_achievement_record_biological_operation` at line 816.
Therefore do not claim that three native biological covert releases satisfy the existing three-operation achievement without a task-specific counter test and owner review of this guard.
This is a shared source gap, not a unique mechanic requiring preservation of the intelligence-operation interface.

### Zombie package

`common/scripted_effects/zombie_special_project_effects.txt:2066-2091` maps developed `weaponized_zombie_infectiousness` into the native low/medium/high raid flags.
Native hostile/friendly raids already use the corresponding visible flags, real `zombie_disease_bomb_equipment`, aircraft, preparation, and `apply_weaponized_zombie_strike_consequences:3912`.
That native consequence helper preserves successful-deployment history, use counters, `used_bioweapon`, `used_unconventional_weapon`, `used_weaponized_zombie_weapon`, treaty use, Condemnation, political/stability/war-support consequences, and the Kruger confirmed-offensive-use callback where its existing hostile/target checks apply.
Friendly strikes against zombie-held targets also retain `achievement_fight_fire_with_fire`.
Preserve the project, profile, actual spawn helpers, outbreak package, native raid images, and all shared consumers.

The zombie intelligence operation has its own native bill of 75 zombie payload plus 100 support equipment and 95 days.
Existing zombie raids instead reserve 125 zombie payload and 15 Command Power and prepare for ten days.
The raid package is already strain-sensitive, so the operative infection/network success calculator is not needed as a substitute.
The intelligence-operation-only `bioweapon_target` setter in `biowarfare_effects.txt:192` has no non-cleanup reader in the bounded source scan.
It is not evidence of a lost accepted functional consumer.

Zombie native permission parity remains a source-review gap.
Current native `visible`, `available`, and `launchable` do not call the intelligence operation's `bio_kruger_last_resort_authority_is_valid` or its AI gate.
`brilliant_scientist_biological_agent_weaponized_zombies_is_unlocked` at `016_brilliant_scientist_biological_operations_triggers.txt:24` checks only delivery technology/completion/project alternatives.
The native launch checks war and target, while availability checks payload.
Review the accepted authorization contract through real native preflight and outcome contexts before claiming an equivalent, fully authorized zombie end state.
Do not infer accepted policy coverage from the unlock helper's name.

## Exact implementation order for the parent

1. Record the ordinary and zombie public-operation retention claims as superseded by the direct raid-only instruction and amendment 13, with the preserved capabilities above.
2. Verify retained native ordinary and zombie route/permission/consumer coverage, including the covert-count acceptance case and exact current policy at outcome.
3. Remove all five public operation blocks from `common/operations/chaosx_bioweapon_operations.txt`; remove that exclusively biological-operation file when empty rather than leave an alternate public attack path.
4. Remove the exclusive ordinary `biological_operation_effects.txt`, `biological_operation_triggers.txt`, and `chaosx_on_actions_biological_operations.txt` package, together with `bio_lifecycle_confirm_operative_release_from_capture` if it has no remaining real caller.
5. After both ordinary and zombie operations are gone, remove only the exclusive `bio_set_integrated_operations_bw_modifiers_from_operation_actor`, `bio_operation_calculate_plant_success_chance`, `bio_operation_apply_weaponized_zombie_consequences`, and `bio_execute_weaponized_zombie_plant_operation` blocks in shared `biowarfare_effects.txt`.
6. Retire `bio_operation_plant_outbreak` in `common/script_constants/biowarfare_constants.txt` only after a fresh constructor-aware call-site scan confirms its four current consumer files have lost every use.
7. Retire the three custom phase blocks in `common/operation_phases/chaosx_bioweapon_operation_phases.txt` and the operation-exclusive keys in `localisation/english/chaosx_operations_l_english.yml` after all five operations are removed.
8. Retire the eight operation-only sprite declarations in `interface/chaosx_operations.gfx` and runtime DDS consumers after a fresh GFX/localisation/meta-constructor scan. Preserve durable asset provenance instead of treating unrelated raid icons as replacement art evidence.
9. Reconcile the docs/spec/prompt files listed below, preserving current shared lifecycle and native event-owner wording, then review the final scoped diff and perform matching MCP/source acceptance.

These are removal/consolidation steps, not an authorization to redesign disease mechanics, rebalance scores, change policies, rewrite zombie events, or manufacture capture proof.
The parent remains responsible for owner patches, final wiring, review, and commit.

## Documentation and asset disposition

Update the current source map in `docs/systems/cbrn_warfare/cbrn_native_raid_migration.md` to distinguish all five retired intelligence attacks from surviving native hidden adapters.
Replace the current feature promises in `biological_warfare/bioweapon_operative_outbreak_operation.md` with the retirement disposition and native successor links.
Reconcile `biological_warfare/biological_sabotage.md:17,24,75,98`, `biological_warfare/biowarfare_system.md:13`, `biological_warfare/README.md:20`, and `cbrn_biological_ai.md:86`, which still describe active ordinary operative operations.
Check `common/scripted_effects/cbrn_scripted_effects.md` and `common/scripted_triggers/cbrn_scripted_triggers.md` for removed helper claims.
Reconcile the conflicting operative sections of spec 06, matrix `biological_agent_countermeasure_matrix.md`, `chaos_warfare_coding_prompt.md`, `chaos_warfare_decision_mission_prompt.md`, and `handoffs/staged_implementation_plan.md`.
Keep `handoffs/source_reading_ledger.md` as a historical read receipt unless it is explicitly presented as a current implementation claim.
Do not rewrite historical handoff results or archived source hashes to imply the migration was already performed.

Operation-only sprites are `GFX_operations_plant_bioweapon`, `GFX_operations_plant_bioweapon_map`, and full/small variants of `GFX_phase_bioweapon_plant_reservoir`, `GFX_phase_bioweapon_seed_medical_chain`, and `GFX_phase_bioweapon_contaminate_transport_hub`.
Their runtime DDS files are under `gfx/interface/operations/chaosx_bioweapon/`, with the exact paths declared in `interface/chaosx_operations.gfx`.
Existing native map/equipment sprites in `interface/chaosx_raids.gfx` and `interface/chaosx_equipment.gfx` remain consumers of surviving raids.
This migration does not require new images, portraits, animated sprites, custom 3D units, unit sound packages, event roots, super-events, or dedicated scripted GUI.
No new event-catalog row is implied by removing an intelligence operation.
The authoritative workbook should only receive changes if its current fields actually advertise the removed surface, through its owning worker after final implementation facts exist.
No workbook or export CSV was edited or treated as an authoritative audit input here.

## Meaningful acceptance requirements

- Public source census: no `operation_plant_*_outbreak` definition or alternate public ordinary/zombie attack adapter remains. Surviving biological attacks are listed under `biological_raids` and human/AI use the same native definition and callback.
- Native preflight and outcome cases: project missing, exact stock shortage, allowed/disallowed current authorization, eligible/ineligible selected state, target-controller change, missing/duplicate agent or outcome markers, and valid actor/victim/state identity.
- Resource and route cases: one native payload/CP collection contract, no second debit/refund, no operation-only Command Power grant, no replacement state, and no preparation/staging decision requirement.
- Lifecycle cases: failed attempts create evidence without confirmed use, accepted partial/full covert releases seed the chosen agent in the exact state, lifecycle use/history/treaty/Condemnation and corridor hooks remain attached to their actual receipt.
- Achievement cases: three independently accepted covert native releases increase the intended completed-operation count to three, a first family type increments the type count once, later discovery/coverup disqualifies Clean Hands, and failed/rejected releases cannot grant completion.
- Zombie cases: project/strain/profile continuity, hostile/friendly routing, actual outbreak spawn, accepted authorization, use/treaty/Condemnation history, and existing friendly anti-zombie achievement receipt. No synthetic operative capture.
- Retirement cleanup: constructor-aware scans of script, GUI/GFX, localisation, docs, and constants retain Event 016's shared `operative_release` token and leave no unresolved exclusive helper consumer.

No executable fixture was added or run by this auditor.
These acceptance cases are required parent work and are not claimed passed.
Native callback cardinality, reservation/cancellation settlement, delayed lifecycle execution, persistence, and native panel reachability remain engine-evidence limits.

## MCP and reference evidence

Reference/context/search/read and source-lookup routes were exposed and answered live calls.
The event context bundle omitted some broad core topics, so this audit made targeted reads for only the actual scope and callback rules used below and does not claim complete core-reference coverage.
`script_doc` source inventory was unavailable through the reference search route.
No helper-expansion, job, or native task request was made because the parent's reported tools 3.10.0/task-negotiation capability was not independently confirmed here.

Installed `common/raids/_documentation.md:133-181,237-301`, revision `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e`, was read through MCP for native target/origin/unit/equipment and outcome scopes.
The direct local dynamic-variable section at lines 547-559 exposes actor, victim, state, and province.
It does not expose a captured operative.
Vanilla `common/raids/air_raids.txt:143-178` is the read source precedent for explicit target-state scope and raid-instance unit loss/experience.
Offline `Data structures - Hearts of Iron 4 Wiki.md:263-269`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, supports saved scope pointers.
Offline `On actions - Hearts of Iron 4 Wiki.md:600`, revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`, describes the actual operative-capture scopes.
Installed on-action documentation lines 93-103, revision `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4`, lists the capture callback.
Installed dynamic-variable documentation lines 1340-1345, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, identifies actual assigned country/state and the zero/unassigned case.
Installed trigger documentation lines 6955-6964, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, requires CHARACTER scope for `operative_leader_operation`.

`hoi4.source_lookup` at workspace-index revision `d73e353a61a8fe49275a34d5b5f19f34b21ae08b82eb3060dbf15156e8780a6f` found `biological_native_raid_bridge.2` at lines 69-128 and `bio_resolve_supply_chain_raid_outcome` at lines 161-207.
The same source lookup returned no indexed `anthrax_strike` definition although direct source contains it, so raid lookup coverage is not inferred from its complete index label.

Narrow trace/render used namespace `biological_native_raid_bridge`, both directions, depth two, at most 30 nodes, no helper expansion, and revision `10aaec8852ad155188b9418a96fec3a0d1d9c7f07eaa5bd47c57cb3bc29062e8`.
Trace returned `EVENT_INSPECTED_PARTIAL` and render returned `EVENT_RENDERED_PARTIAL`.
The manifest selects bridge events `.1-.4` plus eleven unresolved helper nodes, with `complete = false`.
The helpers exist in source, so the graph's absent-active-catalog findings are coverage limits, not evidence that those helpers are missing from gameplay.
The first selector attempt lacked `kind` and returned `-32602` discriminator errors, then the corrected namespace selector worked.

- [Trace artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79da7c6919267958e6ba287a321ce3e5b2f46acedc0614116b3ea1b7081a4fe2/775bab53c2919eee3777afd23447fb20aba116aece7a6f262faa744eca0e6227/event-trace-10aaec8852ad.json).
- [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36a73575e8c21743fe6f6742ded333c9809195ef8bc57b4b1331f2d17db9058d/49d300c101b164f5cfce71daeb995d66058da6ecb8bf65f9c6b53706b68b462a/event-neighborhood-10aaec8852ad-manifest.json).
- [Render data](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0cc8250ebe8b6ff1dcdec1a077787cdc0de43db63d47d1a58c5e11aef70580c/fb3532c33d9f3f0c51ec1f6083e021562269c50df07653784985f12f1912b1a4/event-neighborhood-10aaec8852ad.json).
- [Render SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f1fc69c425f5624d90405fa2c905fccc844bce20599d5fad11292dfa289cbbe/f0afec39d53b1db536149380a05df03c6541f631779050c6016f1cc136d9444f/event-neighborhood-10aaec8852ad.svg).
- [Render PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/900ed74d9f8ace2f55a1f2f7d84f3e5b8f9ed8c5e9191aec63ba3766b4edf0ab/9b6d1d3eee54f71396c8a8c2de2717b099a24334ad7a3e08f1197e0cba4e4d2e/event-neighborhood-10aaec8852ad.png).

The manifest resource's returned text envelope parsed successfully, but this auditor did not verify the original artifact checksum or full byte retrieval.
A subsequent byte-range resource read returned `-32603: Artifact provenance manifest is unavailable`.
Artifact availability must therefore be rechecked before downstream reuse.
The parent retained a 96,802,897-byte baseline graph and saved the final comparison receipts in `docs/testing/2026-10-08_bio_remaining_callers/event_compare_receipts.json`.
The proper scan revision with a reverse original-source overlay returned `EVENT_REVISION_NOT_CACHED`.
The actual graph-artifact retry with `maxChainNodes = 1` and `render = false` returned `ARTIFACT_NOT_FOUND`, with provenance manifest unavailable.
No comparison artifact was produced, and the parent requested no duplicate call against these failing routes.
This read-only audit has no before/after gameplay delta, and does not claim complete graph comparison evidence for the future retirement patch.

`hoi4.script_validate` on the actual sabotage callback's scope-saving/hidden-country-event snippet, under explicit raid-instance scope with actor/state/victim bindings, returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, and four `SCRIPT_COMMAND_UNRESOLVED` findings on `var:actor_country`, `var:target_state`, and `var:victim_country`.
It checked zero native commands, did not check parameters, and did not establish callback validity.
The direct installed documentation supports these scopes separately, without converting this validator result into a pass.

## Probability subagent evidence and limits

The mandatory weighted pass was routed through read-only `chaosx_ai_probability_auditor` as `/root/bio_competing_operation_audit/operative_probability`.
No weights were changed and no numeric retuning is recommended.
The live adapter enum has no intelligence-operation or native-raid AI adapter.
Operation and four replacement raid-file inspections returned `no_weighted_surfaces` despite the real source AI blocks.
This is an exact adapter gap, not evidence of absent AI.
The ordinary source AI base scores are 1, 1, 0.85, and 1, with further route/target/doctrine factors, and are not normalized probabilities or a proven complete selection pool.

The random-list inspector found the complete three-entry ordinary operation outcome pool at `biological_operation_effects.txt:168`.
Scenario `unbound_effect_derived_outcome_weights`, hash `325617942c987ed70f77acff4dbf19bfba788f79899689a13b92bf14fdf977e0`, returned `PROBABILITY_ANALYZED_PARTIAL` with three `VALUE_UNRESOLVED` outputs for failure, partial, and full-success temporary weights.
All weights, probabilities, and ranks are null because the adapter does not execute the upstream success helper.
The two-entry zombie outcome list at `biowarfare_effects.txt:196` was discovered, but its infectiousness/network-derived weights were also not scenario-resolved.
No fabricated no-doctrine/full-doctrine numbers, custom race pool, sweep, seeded simulation, sequence, or numeric comparison was substituted.
A later probability-render request returned `PROBABILITY_ANALYSIS_STALE` after the shared workspace revision changed, so only the evaluator-emitted revision-bound render resources exist.

- [Operation AI inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69ad3e9a860401ff9d471290402e98ea7ace92b8fedc828fdc86c5774ffd7d56/1baeb43f5ddbc9f8576524e8973cabf471cbfbc734dea793fa2063925d7d9e74/probability-inspect-e06c3f8fb1e6.json), revision `95b45a9c923cd95599c3ac4e7f8d1fed45f519da75916732e9acdbd44eddc25d`.
- [Ordinary random-list inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eef74afcb052ddd1f3ac930294a8c852924caaabf5ce38386c2a15d37e1c1dc0/b6f9d96c43ffa3fe1c960e0bb904839294dd7fcc333d243bd62b966d41de8b93/probability-inspect-59c7e81940a1.json), revision `06152fff4a434a9efe0c8bb1654f50f8df0cc3e716a48dd972ee609699e42b7c`.
- [Ordinary partial analysis](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de81b5f79ddcbf1776beb50345513fad6eb3ecd5701d2f1fb079bfe8cca082f5/6158d939bb04f8748a463e22c2cf4b87660f1a57717481379de929121390e1cc/probability-3acac7bb2e4740b5538aca43.json), revision `6a65235fce3040587485807522e1d4853a587f0444633c72d0943b980b214b11`.
- [Ordinary unresolved render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c6ba1b5217ed0db379a3da35b6179312229bd7a78f3ef36055a830e9b9dd9be/be544b0ea11f4fb9d488be1d6afe691ee16e9127d9422f5ce1ec0a7a8adbff10/probability-probability-3acac7bb2e4740b5538aca43-unresolved.svg).
- [Zombie random-list inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9705a6abbed01bb8285f45a9555a547674bb30d063f0ac5d2581320846a1173d/1bbc732428375cdb6295713933370c9d9947c836a871c5bead1ca4b7f7aee6e8/probability-inspect-b63228aef61d.json).
- [Strategic raid AI inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72ad09c5bbed778d37139456225b1a149ddcb957b4591c0fe785526539040aec/ca830588182bbb63a36f6f7cfbf29380f1fc4fc58214cb2f17206b0cd49ede97/probability-inspect-23bcb390a41b.json), revision `ce0f03e46ef49658ee21073545c69d054dca7db3c04203012e2cc8f82544d3e3`.
- [Sabotage raid AI inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/849337eb9fcdea0c6f6f1eb795ca46bf4a373cdc1fdbabb1318deb71d9bcfbbe/7358da4326f8ba767218ac327adc27a97a6b0501dc9dd5209436f8e5658a5a54/probability-inspect-9f9beab397c9.json), revision `9c15fc83735bc13002baaba868217ed0ef00703b9eb6dfebc2469c9ba87217cc`.
- [Battlefield raid AI inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ba60f728eec493bf1ab7146811796d9dd2340c8a5810e533230a65cedcca577/aba4146a745d8ba1e2836e2cee182adad09ab763021925bf6562c20b556b814e/probability-inspect-f8496edd3c29.json), revision `88cc1ae74e915f8e2ad20c08b5de0b9650de61ec318f4f6a038f0cce2caed62d`.
- [Zombie raid AI inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/155228ffb02ca6686dd20d4a93444fddaabed4089ac1e003f1c17fa55ecd9c40/ea1a912d3480e3e421f45e0cb242b7612c33bfd76e8eddf4e88f9297b40a4563/probability-inspect-1fd1fcdeda2a.json), revision `77594ea840b44ecdf39836815768aaae6b97aa282ef52971fdad4b565e27c0db`.

## Source fingerprints

These SHA-256 values identify the exclusive package read during this audit, before any parent retirement patch.

| File | SHA-256 |
| --- | --- |
| `common/operations/chaosx_bioweapon_operations.txt` | `0262704a1ef4a8493414b5c07c98e17ac7cdeba8ce0184f2d0b22bdc44e185fa` |
| `common/scripted_effects/biological_operation_effects.txt` | `9ad65c9590c4a226050a57ec577752caab127fdcdfd2d733faf9e0033f0c6665` |
| `common/scripted_triggers/biological_operation_triggers.txt` | `996e40c3fd771d27e465b9bde135bc650e432682ca5419973c850ba8feda2133` |
| `common/on_actions/chaosx_on_actions_biological_operations.txt` | `01fbebf83f3178e4ac6fa623827c35a6fc2113f32666840ab6fdbceaa7de2059` |
| `common/operation_phases/chaosx_bioweapon_operation_phases.txt` | `4566ef4798e595b7e4dd8d0f701008af9a029ca6df5c9fd165bdde5c70452cd9` |
| `interface/chaosx_operations.gfx` | `1170ca0b8fed6d1686d5bd7a9d15c08f2e8444292181105e6481d31a030f583a` |

## Remaining blockers and next action

The raid-only end state is incomplete while any of the five public intelligence attacks remains.
Implement the bounded retirement/consolidation above with owner-reviewed native authorization and covert-achievement continuity, then reconcile the source docs and run the meaningful cases.
Native execution, cancellation settlement, callback cardinality, full lifecycle sinks, complete event graph comparison, and numeric native raid/operation AI evidence remain unproved.
No new gameplay simplification was introduced by this auditor.
The recommended removal explicitly retires operation-specific network/operative/phases/capture/Command Power behavior under the current accepted design instead of silently calling those mechanics migrated.

Skills used: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, and `chaos-redux-native-raids`.
No skill was created or modified.
