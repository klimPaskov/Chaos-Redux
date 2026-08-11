# Event 012 Africa achievement callsite completion audit

> Historical audit notice, 2026-08-10: this read-only callsite snapshot predates the current owner operations, W4 repairs, Nile/Gold operations, elephant operations, and high-chaos operations. Its queued and model-gated statuses are retained as provenance only; the final reconciliation handoff is the current disposition authority.

## Audit scope and conclusion

This is a read-only completion audit of all 44 accepted Event 012 achievements after `99f405fe4`, using current `HEAD` `3d57a19792cd` on 2026-07-29.

`99f405fe4` is an ancestor of the audited `HEAD`.

The shared worktree contained unrelated Event 006 image and localisation edits at the final snapshot; none were read as Event 012 evidence or modified by this audit.

All 44 achievements are registered, all 44 have completion triggers and English localisation, and all 44 have installed normal, grey, and not-eligible DDS variants.

The achievement package is not completion-proof:

- 27 achievements are conditionally reachable through active gameplay, but at least one required disqualifier, cleanup, or exact-result proof is absent or simplified.
- 9 achievements are unreachable through otherwise active Event 012 systems because a required positive owner callsite is missing.
- 4 achievements are blocked by deferred nonhuman/model packages.
- 4 achievements are blocked by deferred external-world packages and the terminal super-event package.
- 0 of 44 achievements has enough source evidence for a full completion claim against the accepted matrix.

The most important distinction is that model and world achievements are safely dormant, while restoration, maritime, development, reserve, and weather achievements are active-surface implementation gaps rather than intentional gates.

## Evidence anchors

- Accepted requirements: `docs/specs/012_africa_specs/matrices/012_africa_achievement_matrix.csv` has 44 data rows and `docs/specs/012_africa_specs/matrices/012_africa_achievement_matrix_notes.md` requires a row disposition, owner tracking, disqualifier checks, and validation scenarios.
- Registry: `common/achievements/chaos_redux_achievements.txt:3418-3657` contains 44 Event 012 blocks, each pointing to its named completion trigger.
- Completion predicates: `common/scripted_triggers/012_africa_achievement_triggers.txt:40-545` contains the 44 row predicates.
- Core action callsites: action start, full result, and all-result hooks are called at `common/scripted_effects/012_africa_action_effects.txt:3594`, `:6468`, and `:6482`; their achievement dispatch is at `common/scripted_effects/012_africa_achievement_effects.txt:227-755`.
- Unification snapshots: `common/scripted_effects/012_africa_focus_route_effects.txt:2140-2162` captures pre-unification food evidence and the Africa-is-One relationship snapshot.
- War evidence: `common/on_actions/012_africa_world_order_on_actions.txt:51-59`, `:63-130`, and `:134-220` owns protection-war, capitulation, Scramble, continental-war, and peace hooks.
- Missing generic milestone dispatch: `africa_achievement_record_milestone` is defined at `common/scripted_effects/012_africa_achievement_effects.txt:187-220`, but there is no `africa_achievement_record_milestone = yes` callsite under `common/` or `events/`.
- Missing restoration dispatch: `africa_achievement_record_restoration_identity` is defined at `common/scripted_effects/012_africa_achievement_effects.txt:1096-1138`; its only invocation is internal to the otherwise uncalled Stoneborn milestone branch at `:216`.
- Other definition-only positive helpers: reserve-war proof at `:1919`, weather-army proof at `:1929`, elephant formation/supply/victory at `:1962-1972`, and terminal-super-event proof at `:2006` have no gameplay callsites.
- Definition-only failure helpers: coercive annexation at `common/scripted_effects/012_africa_achievement_effects.txt:2021-2029`, forced relocation at `:2089-2091`, and other-world-end at `:2121-2125` have no gameplay callsites.
- Deadline safety: the unset sentinel is `10000000` at `common/script_constants/012_africa_achievement_constants.txt:60`, so missing duration-start writers make rows unreachable rather than immediately true.
- Model gate: actions 74-76 require unset `africa_strange_formation_package_ready` at `common/scripted_effects/012_africa_action_effects.txt:2894-2928` and are hidden behind the same flag at `common/decisions/012_africa_decisions.txt:1389-1425`; no setter exists.
- World gate: candidate installation requires unset country flag `africa_world_package_implementation_ready` at `common/scripted_effects/012_africa_world_order_effects.txt:463-480`, and the Africa-only close explicitly excludes ready candidates at `common/scripted_triggers/012_africa_world_order_triggers.txt:233-250`; no setter exists.
- Terminal gate: `africa_form_terminal_world_identity` requires unset `africa_the_world_super_event_package_ready` at `common/scripted_effects/012_africa_world_order_effects.txt:1674-1694`; no setter exists.
- Presentation: `gfx/achievements/` contains 132 `africa_*.dds` files, exactly three per achievement, and `localisation/english/012_africa_achievements_l_english.yml:4-135` contains the player-facing strings.

## Status legend

- `REACHABLE/PARTIAL`: active positive path exists, but exact-result, disqualifier, or cleanup evidence is incomplete.
- `ACTIVE/BLOCKED`: the owner system is active, but a required positive writer is absent.
- `MODEL-GATED`: the accepted requirement depends on a deferred nonhuman actor, unit, or model package and remains unreachable.
- `RUNTIME-EVIDENCE-GATED`: the static unit/entity consumer exists, but exact achievement owners or live witnesses remain absent and the row stays unreachable.
- `WORLD-GATED`: the accepted requirement depends on deferred external-continent or terminal super-event packages and remains unreachable.

For disqualifiers, `runtime` means a helper has a real caller, `definition-only` means the helper exists without a caller, and `no writer` means no literal result setter exists under `common/` or `events/`.

## Row-complete callsite audit

| # | Achievement | Owner and positive milestone path | Disqualifier setter and cleanup audit | Reachability and smallest safe patch |
|---:|---|---|---|---|
| 1 | `africa_guardians_without_borders` | Protection action ledger, protection-war on-actions, and Africa-is-One snapshot are active. | Broken guarantee and protected-partner capitulation are runtime; coercive-annex flags are definition-only because the annex helper has no caller. | `REACHABLE/PARTIAL`. Call coercive-annexation only from the real territorial absorption result and ensure unresolved protection wars cannot be cleaned without settlement. |
| 2 | `africa_last_convoy_home` | Full aid-corridor proof plus the protection peace hook records the convoy settlement. | Partner capitulation and corridor abandonment are runtime; `last_convoy_partner_annexed` has no writer. | `REACHABLE/PARTIAL`. Set the annex DQ at the actual partner annexation result, not at war start or target selection. |
| 3 | `africa_no_empty_promises` | Full sovereignty guarantees and the unification high-confidence snapshot are active. | Broken guarantee is runtime; guaranteed-partner coercive annexation is only inside the uncalled annex helper. | `REACHABLE/PARTIAL`. Wire the existing coercive-annex helper from the actual absorption effect. |
| 4 | `africa_the_interveners_left` | Scramble coalition full-result and expedition-defeat on-actions are active. | League-member capitulation is runtime; `partition_accepted` has no writer. | `REACHABLE/PARTIAL`. Set partition acceptance at the exact Scramble settlement option that cedes or partitions Africa. |
| 5 | `africa_archive_of_the_living_state` | Archive evacuation is counted on its full action; restoration is rechecked on later full actions for the evacuated target. | Archive-partner annexation is definition-only through the uncalled annex helper; permanent destruction and sale/suppression have no writers. | `REACHABLE/PARTIAL`. Call the restoration helper at the exact restoration commit and add destruction/suppression DQs to their final dispositions. |
| 6 | `africa_twelve_empty_chairs_filled` | `create_regional_charter` calls the congress helper, which starts the two-year clock when twelve live full members exist. | Expulsion and coerced accession are runtime and reset the clock; ordinary member capitulation/loss does not reset this congress clock. | `REACHABLE/PARTIAL`, with a simplified positive proof: one regional-charter action is treated as “all agenda items completed.” Move the call to the real all-agenda result and reset/recount on every qualifying member loss. |
| 7 | `africa_the_clause_is_the_country` | Clause renegotiation and the Africa-is-One member snapshot are active. | Untracked-member annexation is definition-only through the uncalled annex helper; protected-clause cancellation has no writer. | `REACHABLE/PARTIAL`. Wire annexation and clause-cancellation DQs at their final member disposition effects. |
| 8 | `africa_exit_without_war` | Exit preparation starts the timer; a later full action on a peacefully reassociated former member can complete it. | Exit war/coup and coerced return have no writers. | `REACHABLE/PARTIAL`. Record both DQs from the actual exit crisis and forced-return resolutions. |
| 9 | `africa_no_second_capital` | Rival monitoring and arbitration/defection full results own the 180-day crisis ledger. | Crisis overrun is runtime; rival annexation and terminal rival coercion have no writers. | `REACHABLE/PARTIAL`. Add exact annex and terminal-coercion DQs to rival-crisis final dispositions. |
| 10 | `africa_every_region_speaks` | Regional representation and overlap-settlement action proofs fill the two nine-region arrays. | Region unrepresented and overlap unresolved have no writers or array cleanup owners. | `REACHABLE/PARTIAL`. Add loss/cancellation hooks that set DQs or remove the affected stable region proof. |
| 11 | `africa_confidence_is_contagious` | Live relationship counts and duration refreshes run from actions/evolutions; the unification snapshot supplies the high-confidence count. | Coercive administration and cascade are runtime; direct annexation is definition-only through the uncalled annex helper. | `REACHABLE/PARTIAL`. Wire direct annexation and refresh/reset the clock on all relationship losses, not only cascade. |
| 12 | `africa_federation_by_consent` | Federal route commit and autonomous-federal/fiscal/representation snapshot evidence are active. | Coercive administration is runtime; military takeover and lifetime Covenant use have no writers. | `REACHABLE/PARTIAL`. Persist takeover and Covenant-route history at route commitment and wire direct forced annexation. |
| 13 | `africa_republic_of_many_capitals` | Republic route, regional-institution proofs, and election/succession actions are active. | Republic suspension, one-region centralisation, and military transition have no writers. | `REACHABLE/PARTIAL`. Set the three lifetime DQs at their constitutional result barriers. |
| 14 | `africa_crowns_at_one_table` | Crown-charter full actions mark recognised courts; monarchical origin, council, and succession predicates are active. | Coercive administration is runtime; court deposition and monarchy abolition have no writers. | `REACHABLE/PARTIAL`. Add deposition/abolition DQs when a counted court loses its recognised constitutional status. |
| 15 | `africa_union_of_work_and_land` | People’s Union route, processing actions, regional labour proofs, food reserve, and duration refresh are active. | Military takeover, private resource concession, and preventable famine have no writers. | `REACHABLE/PARTIAL`. Connect the three DQs to exact constitutional, concession, and famine outcomes. |
| 16 | `africa_order_without_partition` | Military route, Scramble intervention victories, emergency reduction, and representation-restoration actions are active. | Permanent maximum emergency, member genocide, and regional partition have no writers. | `REACHABLE/PARTIAL`. Persist these result states at emergency, atrocity, and settlement commits. |
| 17 | `africa_confederation_that_endured` | Confederation route, live sovereign-member count, burden ceiling, and Scramble settlement evidence are active. | Ceiling breach and member cascade are runtime; confederal-to-federal annexation has no writer. | `REACHABLE/PARTIAL`. Wire the annex DQ and reset/recount duration on every sovereign-member loss. |
| 18 | `africa_covenant_with_the_impossible` | Covenant review can count a target only if it already has `africa_registered_high_chaos_actor`; no runtime setter for that actor flag exists. | Rights violation is runtime; rampage and terminal-disease DQs have no writers. | `MODEL-GATED`. Keep dormant until at least three actual nonhuman actor packages own registration, rights, obligations, rampage, and terminal cleanup; an explicit actor-package ready gate would make the intentional block clearer. |
| 19 | `africa_kings_of_the_savanna` | Restoration helper can count Luba/Lunda/Kuba and milestone helper can settle overlaps/order, but neither helper has a gameplay caller. | Court annexation and destruction have no writers. | `ACTIVE/BLOCKED`. Call restoration enums from the three real package settlements, and call the two milestone enums only from final peaceful overlap/court-order results. |
| 20 | `africa_nile_has_many_memories` | Restoration helper can count Kush/Nubia/Makuria/Alodia and milestone helper can prove overlap/corridor, but neither has a gameplay caller. | Erasure, corridor failure, and capital dispute have no writers. | `ACTIVE/BLOCKED`. Wire exact restoration and settlement results plus their three failure dispositions. |
| 21 | `africa_ports_of_the_monsoon` | Maritime polities and ports are counted by active federation and port actions. | `africa_achievement_maritime_convoy_access_active` has no writer, so the three-year deadline stays at the unset sentinel; both loss DQs have no writers. | `ACTIVE/BLOCKED`. Start/clear maritime access from a real live convoy-access predicate and wire two-port loss and inland-shortcut results. |
| 22 | `africa_walls_courts_and_caravans` | Aksum/Harar package predicates exist, but no owner records both restoration identities or `africa_achievement_horn_corridors_operational`; the one-year clock never starts. | Package war, abolition, and corridor loss have no writers. | `ACTIVE/BLOCKED`. Wire Aksum/Harar settled-package commits, the joint corridor operational result, and all three invalidating outcomes. |
| 23 | `africa_the_old_gold_roads` | Processing zones are active, but Great Zimbabwe/Mutapa/Rozwi identity recording has no gameplay caller. | Local ownership initializes at maximum and has no live writer; foreign majority, polity annexation, and corridor failure have no writers. | `ACTIVE/BLOCKED`. Record the three exact polity settlements and feed ownership from the real resource system before starting the five-year clock. |
| 24 | `africa_member_who_said_no` | Priority-player refusal/rival flags are active, but the recognised-alternative milestone is only a branch of the uncalled milestone helper. | Colonial puppet, League destruction, and terminal high-chaos use have no writers. | `ACTIVE/BLOCKED`. Call the milestone at the final independent rival-confederation recognition and persist the three lifetime DQs. |
| 25 | `africa_return_without_compulsion` | Passage waves, origin groups, citizenship, trust, and duration evidence are active. | Forced-relocation helper is definition-only; disaster negligence and returnee discrimination have no writers. | `REACHABLE/PARTIAL`. Call forced relocation only on a real forced-movement result and add the two failure DQs. |
| 26 | `africa_tools_books_and_ballots` | Technical missions, diaspora projects, citizenship, representation, and trust evidence are active. | Trust collapse is runtime; military-only labour and representation denial have no writers. | `REACHABLE/PARTIAL`. Persist those two programme/constitutional failures at final outcomes. |
| 27 | `africa_four_oceans_homeward` | Voluntary passage waves fill the four-origin array. | Forced relocation is definition-only and catastrophic return loss has no writer. | `REACHABLE/PARTIAL`. Wire both disqualifiers from the exact return-wave disposition. |
| 28 | `africa_capital_without_capture` | Diaspora investment bonds count distinct owned projects. | Local ownership initializes at maximum and never receives live ownership evidence; all three capture/corruption DQs have no writers. | `REACHABLE/PARTIAL`, but ownership is a default rather than proof. Replace the default with real project ownership and wire government-capture/corruption outcomes. |
| 29 | `africa_rails_rivers_roads_and_ports` | Road, rail, river, and port actions plus region proofs can fill the active arrays and start the duration. | Network split is runtime on qualifying action failure; connected-region loss has no writer. | `REACHABLE/PARTIAL`. Add loss cleanup for a previously counted region and verify failure means an actual network split before making the sticky DQ permanent. |
| 30 | `africa_ore_leaves_as_machines` | Processing actions count resource/processing zones and start the duration. | Concession failure is runtime, but foreign-concession share initializes at minimum and has no live writer; raw-export crisis and forced seizure have no writers. | `REACHABLE/PARTIAL`, with a default-value false proof. Feed real concession share and add the two missing failure outcomes. |
| 31 | `africa_bread_before_banners` | Food-region proofs and reserve actions are atomically snapshotted before the Africa-is-One commit. | Formed-too-early, preventable famine, and maximum ecological wrath against civilians have no writers; the positive snapshot still prevents an early false unlock. | `REACHABLE/PARTIAL`. Add the three lifetime DQs at formation, famine, and disaster-use results. |
| 32 | `africa_development_without_overstretch` | Development project and developed-region counters are active. | Duration start requires `africa_achievement_all_regions_medium_confidence`, which is never set and is only cleared by confidence collapse; burden and confidence-collapse DQs are runtime, exploitation scandal has no writer. | `ACTIVE/BLOCKED`. Compute/set the all-regions confidence proof from the relationship ledger and wire exploitation scandal before starting the duration. |
| 33 | `africa_common_reserve_answers` | Reserve-war helper exists but has no caller, so the six-war counter never increases. | Deadline miss, protected-capital loss, and offensive abuse have no writers. | `ACTIVE/BLOCKED`. Call the helper from the real reserve-arrival success result and add the three exact failure dispositions. |
| 34 | `africa_no_foreign_boot_remains` | Scramble victory/settlement and current hostile-control checks are active. | African-core cession, unreversed member capitulation, and external puppet creation have no writers. | `REACHABLE/PARTIAL`. Persist all three postwar settlement failures; do not infer them only from current hostile-control count. |
| 35 | `africa_beasts_but_not_caricatures` | Three strange formation actions are explicitly ready-gated; elephant/weather families and the great-power-war milestone have no active callsites. | Rights violation is runtime; caricature use and extermination have no writers. | `MODEL-GATED`. Keep dormant until four genuine formation families, their actor rights, combat participation, and war-victory result exist. |
| 36 | `africa_elephants_crossed_the_desert` | Elephant formation, terrain, supply, and protection-victory helpers remain without achievement callers, but the `chaosx_elephant` unit/entity package and host/Action 102 formation consumers are now statically wired. | All three elephant failure DQs still have no writers, and no live movement, supply, destruction, or war-purpose witness has been accepted. | `RUNTIME-EVIDENCE-GATED`. The model package is available, but keep the achievement dormant until its exact owners and live witnesses exist. |
| 37 | `africa_the_forest_kept_its_word` | Ecological-bargain and drought/disaster full actions count distinct targets and drive the five-year wrath window. | Broken bargain is runtime; disaster weaponisation and forest rampage have no writers. | `REACHABLE/PARTIAL`. Add exact civilian-weaponisation and actor-rampage DQs and reset the duration on those results. |
| 38 | `africa_rain_on_command` | Weather action surfaces are active, but weather-army defeat and weather-war milestone helpers have no callers. | Maximum member disaster, neutral-African targeting, and wrath collapse have no writers. | `ACTIVE/BLOCKED`, not protected by a package-ready gate. Wire hostile-army defeat and campaign victory from actual weather combat outcomes, or explicitly gate the route until those outcomes exist. |
| 39 | `africa_disease_made_and_unmade` | Disease actions record branch/create/countermeasure; a failed weaponisation records an outbreak and full containment decrements active outbreaks. | Uncontrolled civilian release, irreversible outcome, and terminal disease outcome have no writers. | `REACHABLE/PARTIAL`. Wire the three disease severity/end-state DQs from the disease system’s final dispositions. |
| 40 | `africa_stone_walks_into_parliament` | Stone cohort action is model-ready gated and the Stoneborn constitutional milestone has no gameplay caller. | Rights violation, human-member war, and erasure have no runtime owners for Stoneborn. | `MODEL-GATED`. Keep dormant until the Stoneborn country/model package can own recognition, seats, rights, inter-member war, erasure, and the five-year peace clock. |
| 41 | `africa_another_continent_stood_up` | Sponsor action and final package completion call the identity helper, but candidate installation requires the unset per-country world-package ready flag. | Collapse, puppeting, and sponsorship betrayal have no writers. | `WORLD-GATED`. Correctly dormant until the six external continent packages exist; then wire their three final failure dispositions. |
| 42 | `africa_two_continents_one_name` | Union negotiation and integration callsites exist, but a compatible target must first be an installed completed world package. | Conquest-only is runtime; confidence collapse and union civil war have no writers. | `WORLD-GATED`. Correctly dormant; add the two missing union-failure DQs before any package-ready flag is set. |
| 43 | `africa_war_between_worlds` | Continental-war victory and settlement on-actions exist, but eligible opponents must first be installed world packages. | Debug surrender and global revolt threshold have no writers. | `WORLD-GATED`. Correctly dormant; add both invalidation hooks before world packages are enabled. |
| 44 | `africa_the_world_is_one` | Terminal formation records continent/rival/world identity evidence, but it requires the unset terminal super-event ready flag; the terminal-super-event helper has no caller. | Other-world-end helper is definition-only and unresolved-continent identity has no writer. | `WORLD-GATED`. Correctly dormant; wire the exact super-event completion, global incompatible-world-end hook, and unresolved-identity result before setting readiness. |

## Completion status by surface

| Surface | Status | Evidence and gap |
|---|---|---|
| Accepted matrix | Finished as design input | All 44 accepted rows remain present and none is formally rejected or superseded. |
| Achievement registry | Finished | 44 registry blocks at `common/achievements/chaos_redux_achievements.txt:3418-3657`. |
| Completion triggers | Finished as declarations, not as runtime proof | 44 predicates at `common/scripted_triggers/012_africa_achievement_triggers.txt:40-545`; several read flags/counters with no owner writer. |
| Core positive ledger | Partial | Action, focus, and on-action dispatch exists, but nine active rows lack required positive writers. |
| Disqualifier ledger | Partial | A small set of shared DQs is active; most route-, restoration-, military-, disaster-, and world-specific DQs have no result owner. |
| Cleanup and duration reset | Partial | Some shared failure helpers reset clocks, but member loss, court loss, region loss, capital loss, corridor loss, and many constitutional failures do not. |
| Model/nonhuman achievements | Blocked | Rows 18, 35, and 40 remain unavailable pending actor/unit/model packages; row 36 has a static unit/entity consumer but remains unavailable until achievement owners and live movement, supply, destruction, and war-purpose witnesses exist. Row 18 is implicitly blocked by absent actor registration rather than a named ready flag. |
| World-order achievements | Blocked safely | Rows 41-44 cannot reach installed external packages or terminal identity without intentionally unset readiness flags. |
| Localisation | Finished for the registered package | Names, descriptions, and tooltips exist for all 44 rows. |
| Achievement assets | Finished for file presence | 132 DDS files exist, exactly three named variants per row. Visual quality was outside this callsite audit. |
| Documentation and acceptance ledger | Stale | `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv:249-292` still says every icon triplet is unresolved even though all 132 files are installed; its blanket “owner-system callsites unresolved” wording is no longer row-specific. |
| Catalog alignment | Not proven by this audit | No row-by-row catalog comparison or workbook update was part of the callsite task. |

## Accepted-plan disposition

The 44-row achievement matrix remains the accepted source of truth.

No row has an implementation rejection, merge, or supersession record.

The registry, trigger, localisation, and icon portion of `docs/plans/012_africa_plans/012_africa_achievements_handoff.md` is implemented.

The handoff’s prose claims that owner systems set milestones and disqualifiers, but the row table above demonstrates that many of those owners are definition-only or absent.

Rows 18, 35, and 40 should remain queued behind the nonhuman/model packages. Row 36 has cleared the model-package barrier but remains queued behind its achievement callsites and live movement, supply, destruction, and war-purpose evidence.

Rows 41-44 should remain queued behind the six external continent packages and terminal super-event package.

Rows 19-24, 32-33, and 38 are not valid queue-only package gaps: their owner systems are otherwise active and need implementation or an explicit reviewed gate.

## Meaningful validation performed

- Counted 44 registry definitions, 44 named completion predicates, 44 matrix rows, and 132 achievement DDS files.
- Traced the action kernel from selection/start through full/partial/failure resolution into the achievement dispatch.
- Traced war, capitulation, and peace evidence through the Event 012 on-actions.
- Searched every achievement helper name for real `= yes` callers under `common/` and `events/`.
- Compared every trigger-side global disqualifier with literal global-flag writers, then separately checked whether the writer’s helper itself has a caller.
- Verified that missing duration starts use the `10000000` unset sentinel and therefore remain unreachable rather than auto-completing.
- Verified that none of the three package-ready flags has a setter.
- Did not use the optional HOI4 event inspector because this audit concerns static achievement, action, focus, decision, and on-action callsites rather than an event-chain ambiguity; source tracing supplied the concrete evidence.

No valid/invalid runtime campaign scenario has been demonstrated for any achievement family.

That absence is meaningful because the accepted achievement prompt requires at least one valid and one invalid path per family and explicit lifetime-disqualifier testing.

## Smallest safe patch order

1. Wire the existing coercive-annexation, forced-relocation, and other-world-end helpers from exact final result barriers.
2. Add active positive writers for restoration identities/milestones, maritime convoy access, Horn corridors, all-regions medium confidence, reserve-war answers, and weather combat results.
3. Add missing disqualifiers only at exact owner outcomes and reset affected clocks/arrays on member, court, region, corridor, capital, and package loss.
4. Replace proxy/default evidence: move “all congress agendas complete” to the actual congress conclusion and feed local ownership/foreign concession shares from live resource results.
5. Keep model and world ready flags unset until their packages can satisfy every positive and negative condition in the affected rows.
6. After callsites exist, run family-level valid/invalid scenario inspection and update `012_africa_acceptance_ledger.csv` plus the canonical Event 012 documentation with row-specific dispositions.

## Remaining blockers

- Nonhuman country and unit/model packages for rows 18, 35, and 40.
- Achievement owners and live movement, supply, destruction, and war-purpose evidence for row 36 after the `chaosx_elephant` unit/entity package wiring.
- Six external continent packages for rows 41-43.
- Terminal The World text/image/music/audio/scenario package for row 44.
- Missing active owner callsites for rows 19-24, 32-33, and 38.
- Missing or unreachable lifetime disqualifiers across all 27 otherwise reachable rows.
- No family-level valid/invalid scenario evidence.

No gameplay files were edited, no fallback was introduced, and no achievement is marked complete by this audit.
