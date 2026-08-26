# Event 016 final improvement-loop closure and disposition addendum

Date: 2026-08-26

Status: broad expansion is closed. Event 016 is not complete.

## Recommendation

Stop expanding Event 016.

The reusable Alien Infantry and D’Rhondan API, four evolutions, Directorate, fifteen-family project portfolio, native Portal Warfare raids, DHR country package and 88-focus tree, Event Log and Event Details integration, six super-event packages, and accepted 2D presentation inventory already form a deep connected package. Another evolution, cluster, route, country, formable, project family, raid family, GUI, super-event, or routine report would duplicate an existing consumer or add maintenance burden without resolving the remaining blockers.

The remaining work is bounded ownership, runtime production, specialist evidence, and user acceptance. It is not permission to invent more content. In particular, no fifth evolution, Event 016 cluster, or fallback animation may be invented.

This addendum is a closure and disposition handoff. It does not claim whole-event completion and it does not supersede the binding specifications under `docs/specs/016_brilliant_scientist_specs/`.

## Evidence boundary

This pass reviewed the complete Event 016 specification and acceptance package, the current documentation under `docs/events/016_brilliant_scientist/`, the active source-of-truth and runtime maps, prior improvement-loop closures, current 2026-08-25 and 2026-08-26 audits and handoffs, and the present source identifiers named below.

The current implementation baseline includes these controlling corrections:

- Commit `d77afae7e` fixes the caller-country ownership of `alien_infantry_landing_state_registry` in `common/scripted_effects/016_alien_infantry_api_effects.txt:301-327` by saving the invoking country and selected state before the registry mutation.
- Commit `6224387cf` reconciles the current registry, Portal, DHR, MCP, and completion-audit documentation without changing gameplay.
- Commit `31a66c4f4` compacts the Event 016 asset workspace without deleting accepted runtime assets or provenance.
- Commit `fc23d2736` records the reviewed V10 model-evidence cleanup while retaining the accepted and rejected evidence needed for recovery.
- Commit `0e724fb8a` promotes the accepted Meshy V13 Alien Infantry firearm package into static runtime entity, GFX, animation, and sound registrations while leaving locator, strict-audio, positional/runtime, and live-acceptance gates open.

The authoritative current audit is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_event_completion_audit_2026-08-26.md`. The current source correction and documentation map are `016_alien_dhrondan_country_scoped_registry_2026-08-26.md` and `016_documentation_registry_reconciliation_2026-08-26.md` in the same folder.

## Fresh read-only MCP evidence

No rewrite tool was used.

- Event `chaosx.nr16.47` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics, revision `43388d6b2737a1c8e2409f324449210941414fee69c903a1c69d441ca9d33b97`, and state-flow artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d969525a2d72030b8c813baeaea7beccd1ad3c48f87effaaed8ad9a7c5254ca8/fbccf1bc536af6d8baf4fb4b0dfacc396bc9ce5f113f5e1c9c59e2a0e70d8d5a/event-state_flow-43388d6b2737.json`. The matching state render returned `EVENT_RENDERED_PARTIAL` with manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5cecc786dfdc4d32361ba41f10a6561b0b59c871b20c4d8f27225ad5bb1908f/2ebbe1c0e66d7ee9c4afad4c92b745ea222aa42d7bec5d7cb92c1a07fc7e0c3e/event-state-43388d6b2737-manifest.json`. Both defer workspace-wide helper and lifecycle projections.
- `dhrondan_focus_tree` returned `FOCUS_INSPECTED` and `FOCUS_RENDERED`. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ec9308d1eabaa92654cf7d4d33a61bc7b5b594e83aa68fb9c579f0b1f8e1d1a/0995cc439583c2427c5cb1306fcc69e202cbf331d1f616c4480935a285b4abaa/focus-inspect.657b6c83f13c8ce8.json`. The render entry is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9bfde2307f7a3cb5c1b075a579b8d3ef0c2da8cba297241a06d825d7e21888bc/cb6769370b3bd005965b354225387ac1cb38dd9df57fb34e5e25d671a035f658/dhrondan_focus_tree.focus.html`. This confirms the current 88-focus topology and presentation, not route-selection probabilities or live completion.
- `kruger_directorate_container` returned `GUI_INSPECTED` with 22 exact inspected elements at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d0f18dca88c956c86aca0c3cb42406a4f49f9894c7664c33d3cae507ab6c89d/c9d922395187ef3597fc6651cfac89ea239129d78f05d0f8fab62eda0dcc55aa/gui-inspect.a8ef2f3c25ad8c30.json`. The bounded normal, long-text, and missing-localisation render at 1366x768 returned `GUI_RENDERED` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce/a3fac435d5dd1419343a0a6abcb8d08a69413377375f09e1ba9185289a01417e/kruger_directorate_container-full.svg`. The shared GUI graph still truncates thousands of unrelated repository-wide symbol and overlap diagnostics, so this is not a clean global GUI certification.
- `events_log_event_details_window` returned `GUI_INSPECTED` with four exact inspected elements at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c87b9dd3610beee8cc573d1554815517a514c96b239e7a8104bdbf04e8779e13/c670cc62e3a1f3cf905743924f794157e3aab65addfed5efe891191c84431c5b/gui-inspect.9a78f87f08e167ce.json`. Its bounded normal, long-text, and missing-localisation render returned `GUI_RENDERED` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0562d57039da950e557344639a82b2fa14063c3f2b79ff1d8c7d7dbb1d9b578c/27150df077b4e79e2622aaa344214e2f0c6fd002f6f4be4f17f4db14f8873d53/events_log_event_details_window-full.svg`. The ad hoc scenario proves that the shared surface parses and renders. It does not execute Event 016 selection or prove live dynamic text.
- `chaosx_super_events` returned `GUI_INSPECTED` and `GUI_RENDERED` for the Event 016 review scenario. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea680569b8b13067432c62a70fd9b37968ecc8c388690a89118aed6186d61ddc/43eccde8aa29665cc5b791d348a6d4213f22139eec5aa3eba5aadb4469e96254/gui-inspect.49b85ff4548c9093.json`. The render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/debd7e6b0d1974547ba67e7e9c2bc405a54c93f02da79d0555588cb96aea83c3/b51b2bcc8440ece71d851c9fadc055c3e71a3b37590d76275313b5afb516fa12/chaosx_super_events-full.svg`. This is shared-window evidence, not live validation of the six Event 016 queues, tracks, or Fallout transitions.
- The map inspector completed for states 1, 12, and 77 at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e98d53e847e82f118a5546d05b6462964590c065a82a094fd0e9cd526a29794/3c64b88f65500c6bd1e5db9c63cad41f07be02885b12198cb3734f4306a0b5b9/map-inspect.9056736b9426fa78.json`. The state-layer render returned `MAP_RENDERED` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2313a7a7ca341ae980ec1057e84b0273f97085a8a035fe4b402304693975da3/4ae4fc94e7db6c0feecb11d89db0cbced0feda6dbe8eeb8ddf47e44460c97fe4/map-state.png`. The global map inspector retains unrelated `map/buildings.txt` position and floating-harbor errors, and neither route executes the dynamic DHR transfer or Portal beachhead transaction.
- `brilliant_scientist_alien_infantry_tech` returned `TECH_INSPECTED_PARTIAL` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb123959e723090f55186e5527e9dd2794c50b5d9badf8b66e8b95ac98e9078d/0dbe9b793f2f9b0cbe5b8f2c25cee5ebd88852a1e9902631cb54becfc71b8431/technology-trace-d8fd72fc8ed3.json` and `TECH_RENDERED_PARTIAL` under `technology-technology-d8fd72fc8ed3`. The package still lacks a complete standalone Technology Tree Viewer and comparison workflow. The partial source-linked trace and render cannot certify every technology placement, unlock, and consumer across the 672-technology workspace.

These artifacts are current structural evidence only. They do not replace source review, probability audit, model reimport, or user-owned live HOI4 acceptance.

## Finding dispositions

### F016-IL-01: caller-country Alien Infantry landing registry

Classification: **resolve now**.

Evidence: `alien_infantry_register_landing_state` in `common/scripted_effects/016_alien_infantry_api_effects.txt:301-327`, the country-scoped consumers in `common/scripted_effects/016_dhrondan_country_effects.txt`, commit `d77afae7e`, and `016_alien_dhrondan_country_scoped_registry_2026-08-26.md`.

Disposition: treat the source ownership defect as closed. Do not reintroduce a global array, a DHR-only parallel ledger, or another landing writer. The remaining two-provider ordinary and Event 019 transfer matrix is runtime acceptance, not a new API design. Carry that matrix as a queued validation item instead of reopening the source patch.

Acceptance boundary: country A and country B retain separate landing registries through duplicate registration, state loss, DHR formation, transfer, claim creation, receipt revocation, and Event 019 deferred commit. The fresh `.47` MCP evidence is partial and does not prove those transactions dynamically.

### F016-IL-02: reusable Alien Infantry and custom-technology API depth

Classification: **reject as duplicate or filler** for any new API, ledger, unit family, technology tier, or landing route.

Evidence: the five public API surfaces in `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md` and `docs/events/016_brilliant_scientist/systems/alien_infantry.md`, the seven-family grant surface in `docs/events/016_brilliant_scientist/systems/custom_technology_api.md`, `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt`, and the country-owned registry fix above.

Disposition: the API already separates contact sources, exact 2,000-weapon debit and refund, ordinary landing, DHR sovereignty, Event 019 provider 508, template reconciliation, and operational technology grants. A second DHR landing API, Kruger-specific Alien Infantry identity, normal recruitable alien template, or new alien technology layer would fragment this accepted reusable contract.

Queued evidence only: the partial technology trace and render do not provide a complete tree comparison. Keep technology projection and live equipment, tactic, and template acceptance open without inventing another technology.

### F016-IL-03: exactly four Event 016 evolutions

Classification: **reject as duplicate or filler** for any fifth evolution or replacement evolution chain.

Evidence: `events/016_brilliant_scientist_evolutions.txt:13`, `:84`, `:164`, and `:216` define `chaosx.nr16.21` through `.24`. `docs/events/016_brilliant_scientist/evolutions.md` and `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_4_evolutions_and_event_chain.md` require exactly four. The hidden `.90` scheduler is not an evolution. World Collapse is a terminal eligibility state, not Evolution V.

Disposition: the four stages already change institutional reach, foreign contest, forbidden autonomy, and sovereign or terminal play. Any fifth stage would duplicate terminal escalation and break the catalog and Event Log contract.

Queued evidence only: current event inspection is focused and partial. The parent still needs the user-owned active and prefire path matrix for all four stages, disabled-evolution safety, actor transfer, and Event Log delivery.

### F016-IL-04: Directorate and project portfolio

Classification: **reject as duplicate or filler** for another meter, project family, cross-project trial, routine report, or event-owned GUI.

Evidence: `brilliant_scientist_directorate_category`, `kruger_directorate_container`, the four visible and two hidden causal values described in `docs/events/016_brilliant_scientist/systems/directorate.md`, and the fifteen family ledgers described in `docs/events/016_brilliant_scientist/systems/projects.md`. The prior closures `016_nonmodel_content_closure_handoff_2026-08-03.md` and `016_post_opening_guard_improvement_loop_closure_handoff_2026-08-03.md` already rejected additional safe non-model synergies.

Disposition: Electronics plus Teleportation already feeds the Portal Calibration Network. Advanced Materials plus Rocketry already feeds the High-Speed Materials Trial. Computation, Robotics, Cloning, Paleogenetics, Xenobiological Synthesis, Temporal, Alien Arms, High Energy, recovery, counter-program, project-force, and terminal consumers are already connected. A simulation cell, audit bureau, fifth recovery action, additional project currency, or another tab would be duplication.

Queue with reason: the accepted optional KRG biological stockpile and delivery ledger in `docs/plans/016_brilliant_scientist_plans/016_krg_biological_stockpile_delivery_addendum.md` remains blocked behind a stable native CBRN reservation, outcome, cancellation, and expiry callback. No parallel payload ledger, free charge, or delayed-flag surrogate is authorized.

Queue with reason: the strict completion record still lacks an explicit current `chaosx_event_ui_worker` attestation for the dedicated Directorate GUI. Fresh exact-window inspect and render evidence is successful, but shared GUI diagnostics remain globally truncated and live interaction acceptance belongs to the user. This is an audit and ownership task, not a redesign invitation.

### F016-IL-05: Portal Warfare raid lifecycle

Classification: **queue with reason**.

Evidence: the native raids `brilliant_scientist_portal_facility_raid` and `brilliant_scientist_portal_special_project_facility_raid` in `common/raids/016_brilliant_scientist_portal_raids.txt`, `brilliant_scientist_portal_raid_establish_beachhead` in `common/scripted_effects/016_brilliant_scientist_raid_effects.txt:53-64`, and the sole active-marker write `brilliant_scientist_portal_beachhead_active` at line 59. `016_portal_lifecycle_patch_2026-08-26.md` confirms that the native raid engine owns preparation, reservation, cancellation, expiry, outcome, and history, while no accepted post-outcome owner clears or transitions the active beachhead.

Disposition: queue the transient beachhead lifecycle to a named future Portal containment, spread, or beachhead owner. The accepted owner must distinguish the transient active marker from the permanent history markers `brilliant_scientist_portal_raid_breach_recorded`, `brilliant_scientist_portal_raid_targeted`, `brilliant_scientist_portal_facility_extracted`, and `brilliant_scientist_portal_factory_extracted`.

Do not implement an arbitrary timer, immediate clear, native `days_re_enable` surrogate, whole-world scan, or speculative sealing action before the owner and exact lifecycle are approved and promoted. The prior suggested 21-day and 25-Command-Power sealing values are planning proposals, not accepted mechanics in this closure.

The static map inspect and render cannot execute dynamic province control or cleanup, so Portal lifecycle acceptance remains unresolved even though the map routes themselves returned successfully.

### F016-IL-06: DHR country package and 88-focus tree

Classification: **queue with reason** for five support hooks. **Reject as duplicate or filler** for every new route, regime, country, formable, decision family, or DHR super-event.

Evidence: `common/national_focus/016_dhrondan_focus_tree.txt` contains the accepted 88-focus tree. Fresh focus inspect and render succeed. `docs/events/016_brilliant_scientist/systems/dhrondan_country.md` owns the fixed DHR tag, three regimes, revolt transaction, country decisions, characters, initial cohorts, and postwar integration.

The following focus-written flags still have no accepted downstream consumer:

| Identifier | Writer | Current direct reward | Disposition |
| --- | --- | --- | --- |
| `dhrondan_alien_components_standardized` | `DHR_standardize_alien_components`, focus source line 592 | Laser-production helper | Queue for removal or explicit reserved external-API documentation. |
| `dhrondan_laboratory_route_complete` | `DHR_a_two_world_research_complex`, line 641 | Laboratory-capacity helper | Queue for removal or explicit reserved external-API documentation. |
| `dhrondan_predictive_warfare_perfected` | `DHR_perfect_predictive_warfare`, line 795 | Predictive technology and command effects | Queue for removal or explicit reserved external-API documentation. |
| `dhrondan_orbital_office_reassembled` | `DHR_reassemble_the_orbital_office`, line 812 | Orbital-support helper | Queue for removal or explicit reserved external-API documentation. |
| `dhrondan_access_map_exchange_ready` | `DHR_exchange_maps_for_access`, line 953 | Diplomatic-credit helper | Queue for removal or explicit reserved external-API documentation. |

Reason: each focus already delivers its promised reward. Creating five shallow decisions merely to consume five flags would make optional support lanes compulsory and add no strategic choice. Prefer removal unless another accepted package names an external consumer.

Queue the two-provider DHR formation and transfer matrix because dynamic state transfer, third-party occupation preservation, capital selection, cohort distribution, and one-cohort or 2,000-gun conservation are not executable by the current map adapter.

### F016-IL-07: Event Log, Event Details, and cluster status

Classification: **resolve now** for source disposition. **Reject as duplicate or filler** for new log rows, details tabs, or a cluster.

Evidence: `common/scripted_effects/chaosx_events_log_effects.txt:2567-2583` supplies the four evolution detail previews. `common/scripted_localisation/016_dhrondan_country_scripted_localisation.txt:9-14` supplies `GetDhrondanEventDetailClause`, with the sovereignty paragraph in `localisation/english/016_dhrondan_country_l_english.yml:133-134`. The current catalog and final audit record exactly four evolutions and a blank cluster field.

Disposition: retain one Event 016 history identity, four evolution rows, the two world-end entries, and the conditional DHR sovereignty clause. Events `.4-.18`, `.40-.52`, project incidents, foreign outcomes, and routine DHR diplomacy remain consequence reports rather than new Event Log catalog rows.

The shared Event Details window now has fresh inspect and render evidence, but the review scenario does not execute actual Event 016 selection or dynamic actor binding. Queue live actor, wrapping, four-evolution, DHR-clause, and world-end presentation acceptance to the user. Do not add a dedicated Event 016 details GUI.

The Event 16 cluster remains blank. An Event 016 cluster would contradict the binding no-cluster contract and would not cure any runtime blocker.

### F016-IL-08: super-events and terminal presentation

Classification: **reject as duplicate or filler** for any seventh super-event or routine milestone package.

Evidence: `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_8_super_events_world_end_and_aftermath.md`, `docs/events/016_brilliant_scientist/systems/super_events_and_aftermath.md`, and the two shared world-end registry entries at `common/scripted_effects/chaosx_events_log_effects.txt:1219-1243`. The fixed six packages are international recognition, Kruger State formation, global Kruger threat, Laboratory World, Strategic Singularity, and qualifying defeat aftermath.

Disposition: the six packages already cover public recognition, sovereignty, existential threat, both terminal fantasies, and crisis-scale defeat. Evolution II alone must not fire recognition, and ordinary projects, Evolutions I-IV, DHR sovereignty, routine raids, or DHR diplomacy do not justify another super-event.

Fresh shared-window inspect and render evidence proves only that the common surface parses and renders. Queue user-owned audio, queue dispatch, settings, terminal exclusivity, Fallout, and live text-layout acceptance. Do not interpret the shared GUI render as proof that all six Event 016 packages fire correctly.

### F016-IL-09: 2D asset and presentation inventory

Classification: **resolve now** for closure. **Reject as duplicate or filler** for new 2D families not named by an accepted consumer.

Evidence: `docs/specs/016_brilliant_scientist_specs/matrices/016_asset_inventory.md`, `docs/assets/016_brilliant_scientist/manifest.md`, current asset handoffs, the cleanup commits `31a66c4f4` and `fc23d2736`, and the final localisation and completion audits. Current report, news, super-event, portrait, focus, decision, project, technology, achievement, flag, counter, and Directorate UI references are substantially present and linked.

Disposition: do not create another report family, animated UI ornament, focus-icon route, achievement triplet, DHR portrait family, or super-event image to make the package feel larger. Preserve the cleaned source and provenance workspace until the model blockers and final user review are complete.

The Alien Infantry and Portal Raider counters, equipment icon, particle, light, and sourced audio candidates do not by themselves satisfy the remaining 3D runtime acceptance gates.

### F016-IL-10: Alien Infantry Meshy V13 runtime package

Classification: **partial; queue remaining runtime acceptance with reason**.

Evidence: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md`, `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/handoff.md`, and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_runtime_promotion_2026-08-26.md`.

The accepted V13 facts are a firearm-bearing Meshy 7 model, stable 24-bone humanoid rig, seven exact semantic action exports, and actual-byte PDX reimports for idle, move, laser attack, defend, support attack, retreat, and death. Commit `0e724fb8a` promotes the static `alien_infantry_entity` and its GFX, animation, and sound references.

Disposition: retain the V13 package as current provider/static-runtime evidence and keep final runtime acceptance queued through `chaosx_3d_model_pipeline` for a supported Meshy/Blender-authored muzzle locator, particle/light effect binding, strict audio selection/acknowledgement/impact/special-role provenance, positional/runtime review, and user-owned live acceptance. No locator may be inferred from the rig or substituted with a manual Blender parenting step.

The static entity and action/audio references are promoted, but provider evidence does not prove live consumer acceptance. No historical professional-source action, semantic alias, transform-only motion, manual Blender replacement, inferred muzzle, generic infantry entity, or static fallback animation may be wired.

### F016-IL-11: Portal Raider model/runtime package

Classification: **queue with reason**.

Evidence: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/portal_raider_3d_model_handoff.md` and `docs/events/016_brilliant_scientist/systems/portal_raider_api.md`.

Disposition: the only generated Portal Raider geometry omitted the mandatory ray rifle and remains rejected and unwired. Keep recovery with the 3D pipeline. It still owes firearm-bearing geometry, packed materials, accepted armature and weights, genuine idle, move, attack, defend, support-attack, retreat, guard, wounded, death, and portal-arrival roles, export and actual-byte reimport, synchronized sourced audio, and parent-owned entity wiring.

Portal Raider counters and native raid mechanics are separately valid evidence. They do not authorize `portal_raider_entity`, arrival animation, unit actions, or sound binding. Do not substitute the Alien Infantry model, a rifle-less mesh, a generic infantry model, or transform-only arrival motion.

### F016-IL-12: weighted logic and remaining engine acceptance

Classification: **queue with reason**.

Evidence: `016_current_mcp_audit_2026-08-26.md`, `016_dhr_probability_audit_2026-08-25.md`, `016_dhr_route_consumers_2026-08-26.md`, and the final completion audit.

The current DHR rebellion evaluation proves only the declared conditional 10/90, 20/80, and 40/60 revolt/no-revolt branch arithmetic. It does not prove cumulative 90-day pulse timing. DHR focus selection, expedition targeting, landing decisions, Event 019 provider 508, evolution choices, Directorate actions, special projects, random lists, raid AI, and terminal routing retain incomplete pools, missing scenario inputs, or absent same-revision baselines.

The required final `chaosx_ai_probability_auditor` pass started each investigated surface with `hoi4.probability_inspect`. Its current rebellion scenario `DHR_REBELLION_TIERS_2026_08_25_CURRENT_CHECK` confirms conditional shares of 0/100, 10/90, 20/80, and 40/60 at artifact `probability-816ab61f71b349643834123e.json`, with no rank reversal. Its current DHR focus matrix `DHR_FOCUS_ROUTE_MATRIX_2026_08_26_CURRENT_CHECK` returned `PROBABILITY_ANALYZED_PARTIAL`, 440 rows, 38 unresolved items, and 34 diagnostics at `probability-8717b0cfcbe9a0ae84d4d675.json`; route dominance, starvation, repetition, and rank reversal remain unresolved. Portal raid inspection returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, and no applicable adapter at `probability-inspect-653eee865c1c.json`, so the authored native-raid factors remain source-only.

Disposition: no tuning change is authorized by this addendum. Every future weighted patch must start with `hoi4.probability_inspect`, use complete named scenarios through `chaosx_ai_probability_auditor`, and compare the same scenarios after the owner applies the patch. Source factors must not be described as click probabilities.

Queue the following current MCP limits rather than hiding them: partial event helper and lifecycle projection, truncated global GUI diagnostics, inability of the map adapter to execute dynamic state transactions, partial technology projection, and the absence of a complete standalone Technology Tree Viewer and technology comparison workflow.

Live HOI4 acceptance belongs to the user. This includes opening and referral idempotence, all four evolutions, Directorate interaction, DHR transfer and capital behavior, Portal raid outcomes and beachhead state, Event 019 equipment conservation, Event Log and Event Details presentation, super-event audio and queue behavior, world-end exclusivity, Fallout transitions, CXT setup, and both custom-unit consumers.

## Prior addendum disposition

No prior accepted expansion is silently reopened.

| Plan | Current disposition |
| --- | --- |
| `016_brilliant_scientist_improvement_loop_addendum.md` | Closed. Promoted R2, R3, R4, R5, and R7 remain implemented design. Rejected R1 and R6 remain rejected. |
| `016_nonmodel_content_closure_handoff_2026-08-03.md` | Confirmed. No additional safe non-model synergy remains. |
| `016_post_opening_guard_improvement_loop_closure_handoff_2026-08-03.md` | Confirmed. Opening repairs did not create a new content gap. |
| `016_alien_dhrondan_improvement_loop_closure_handoff_2026-08-22.md` | Confirmed for broad expansion. The later country-owned registry defect is resolved at source by `d77afae7e`. |
| `016_alien_dhrondan_post_tranche_ownership_addendum_2026-08-26.md` | Registry finding resolved at source. Portal lifecycle remains queued. Five DHR support hooks remain queued. Model and engine evidence remain blocked or partial. |
| `016_krg_biological_stockpile_delivery_addendum.md` | Accepted and queued behind the native CBRN callback. No fallback is authorized. |
| `016_portal_lifecycle_patch_2026-08-26.md` | Queued. It records the ownership gap and forbids an arbitrary cleanup patch. It does not approve exact lifecycle mechanics. |
| Alien Infantry V13 and Portal Raider model handoffs | Alien Infantry's static entity/action registration is promoted, with locator/effect, strict-audio, positional/runtime, and live acceptance queued; Portal Raider remains rejected and unwired. |

## Explicit non-additions

- No fifth evolution.
- No Event 016 cluster.
- No fallback animation, semantic action alias, transform-only animation, or generic model substitution.
- No new DHR route, regime, country, formable, GUI, super-event, or shallow decision for the five support hooks.
- No new Directorate meter, tab, project family, cross-project trial, or routine incident report.
- No new Portal raid family, arbitrary beachhead timer, or whole-world cleanup scan.
- No new Event Log row for ordinary follow-ups and no dedicated Event 016 Event Details GUI.
- No seventh super-event and no super-event for a routine project, evolution, DHR formation, or raid.
- No parallel Alien Infantry or KRG biological payload ledger.

## Parent resume checklist

1. Treat `d77afae7e` as the source fix and run the two-provider ordinary/Event 019 DHR transfer matrix without reopening the registry design.
2. Keep the Portal beachhead lifecycle queued until a named owner and exact accepted lifecycle exist. Preserve permanent raid history separately from the transient active marker.
3. Remove or explicitly reserve the five DHR support flags. Do not add new decisions solely to consume them.
4. Keep Alien Infantry final locator/effect/audio/positional/live acceptance and Portal Raider runtime wiring blocked until their remaining 3D gates pass. Accept no fallback animation.
5. Complete the outstanding named probability comparisons, event and GUI evidence, dynamic transfer scenarios, technology projection where the tools permit it, and explicit Directorate UI-worker attestation.
6. Leave the Event Log at four evolutions, no cluster, two world-end rows, and the conditional DHR detail clause. Leave the super-event inventory at six.
7. Carry user-owned live HOI4 acceptance as open. Do not claim whole-event completion from source, MCP, asset, or model handoffs alone.

## Promotion and completion boundary

Keep this file in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/`.

Do not promote it into `docs/specs/016_brilliant_scientist_specs/` because it introduces no accepted design change. If a Portal lifecycle is later approved, promote only that exact accepted lifecycle into the relevant Portal raid and decision specifications. If one of the five DHR hooks receives a real external consumer, promote only that ownership contract.

This pass closes broad Event 016 expansion. It does not close Event 016 implementation, model production, runtime validation, or user acceptance.
