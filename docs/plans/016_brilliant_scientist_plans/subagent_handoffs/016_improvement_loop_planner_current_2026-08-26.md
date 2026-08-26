# Event 016 current improvement-loop closure delta

Date: 2026-08-26

Status: broad expansion remains closed; Event 016 remains incomplete.

Owner: parent Event 016 implementation agent.

## Closure decision

Do not add another expansion layer to Event 016.

`016_improvement_loop_final_2026-08-26.md` already closes broad expansion, and the later source tranches do not create a new route, project-family, country, evolution, cluster, GUI, or super-event gap. They close two of that handoff's queued documentation findings: all five DHR support-route markers and all four opening-survival markers now have live consumers, and the required named `chaosx_event_ui_worker` attestation for the Directorate GUI now exists.

The remaining gaps are bounded ownership, engine evidence, custom-unit runtime acceptance, and user-owned live acceptance. They are not permission to invent more content.

This file is a closure/delta handoff, not a new accepted addendum. It does not claim whole-event completion or in-game acceptance.

## Accepted design preserved

- Event 016 remains a minor fire-once incident routed through the shared fire-once dispatcher.
- The logged evolution inventory remains exactly `chaosx.nr16.21`, `.22`, `.23`, and `.24`. The hidden `.90` scheduler is not an evolution.
- The Event 016 cluster field remains blank.
- The reusable Alien Infantry API remains provider-neutral and source-counted through independent numeric receipts for Kruger, Mengele, Event 019 provider 508, DHR sovereignty, and future consumers.
- Kruger and Mengele retain distinct craft-expedition and mission routes into the shared contact API.
- DHR remains the fixed country package with exactly 88 focuses, three mutually exclusive regimes, paid landings, the ninety-day rebellion pulse, bounded formation, and postwar integration.
- Project families retain real stage costs, breakthrough and resource burdens, incidents, units, raids, recovery, synthesis, and terminal consumers rather than modifier-only rewards.
- Native Portal raids remain the owner of preparation, reservation, native outcomes, cooldown, and raid history.
- The Alien Infantry runtime consumer remains the firearm-bearing Meshy 7 V13 package. No generic infantry entity or static-animation fallback is accepted.

## Current source findings

### Source-closed findings

1. `alien_infantry_register_landing_state` in `common/scripted_effects/016_alien_infantry_api_effects.txt` saves the invoking country as `alien_infantry_landing_registry_owner`, saves the selected state as `alien_infantry_landing_registry_state`, and appends idempotently to the caller country's regular `alien_infantry_landing_state_registry`. There is no global landing array in this contract.

2. `dhrondan_capture_revolt_inputs` and `dhrondan_release_and_transfer_landing_states` in `common/scripted_effects/016_dhrondan_country_effects.txt` iterate the pact host's scoped registry. Host-owned states transfer to DHR; third-party-owned registered states remain owned by that third party and receive a DHR claim. The source correction is complete, but its cross-country transaction matrix is not dynamically accepted.

3. The five formerly set-only support flags are now consumed:

   - `dhrondan_alien_components_standardized` is read through `dhrondan_focus_has_standardized_components` by the paid-landing AI.
   - `dhrondan_laboratory_route_complete` is read through `dhrondan_focus_has_laboratory_route` by the enclave-support decision and AI.
   - `dhrondan_predictive_warfare_perfected` is read through `dhrondan_focus_has_predictive_warfare` by reclamation availability, cancellation, and AI.
   - `dhrondan_orbital_office_reassembled` is read through `dhrondan_focus_has_orbital_office` by the paid-landing AI.
   - `dhrondan_access_map_exchange_ready` is read through `dhrondan_focus_has_access_map_exchange` by the Covenant compact target-root.

4. The four optional survival milestones are also consumed. `dhrondan_focus_has_landing_states_counted`, `dhrondan_focus_has_expedition_stores_audited`, and `dhrondan_focus_has_landing_beacons_restored` modify the existing paid-landing AI; `dhrondan_focus_has_scattered_enclaves_secured` modifies the existing enclave-support AI. No duplicate decision or generic spirit is needed.

5. `common/national_focus/016_dhrondan_focus_tree.txt` contains exactly 88 focus blocks. Current read-only focus inspection returned 88 resolved titles, 102 connectors, zero crossings, zero node intersections, zero DHR-specific diagnostics, and revision `fc93286a7c2008c03104d15f1d43f6ccb87593e08da916febd11996499e48394`.

6. The current event source contains exactly four logged evolution events. The fifth event in `events/016_brilliant_scientist_evolutions.txt` is the hidden scheduler `.90`, matching the binding specification and catalog contract.

7. `sp_dhrondan_envoy_craft` retains the accepted air specialization, breakthrough cost, resource drain, Kruger/KRG/Mengele/future access routes, Antarctica bypass contract, project output, and AI surface. Kruger and Mengele each have their own paid decision and 180-day mission in `common/decisions/016_dhrondan_contact_decisions.txt`; their completion effects grant different source receipts into the shared API.

8. The named Directorate GUI worker attestation now exists at `016_dhrondan_gui_worker_attestation_2026-08-26.md`. It proves Event 016 ownership from `brilliant_scientist_directorate_category` through `brilliant_scientist_directorate_scripted_gui` to `kruger_directorate_container`, records the exact 500x360 and collapsed 500x58 layout, four visible-value ceiling, zero gameplay-changing GUI controls, and the same-day exact-window inspect/render artifacts. The earlier closure statement that this attestation is missing is stale.

9. The Alien Infantry API creates only the locked, non-recruitable ten-battalion `D’Rhondan Landing Cohort`, uses `override_model = alien_infantry_entity`, and debits exactly 2,000 laser weapons for a successful cohort. `docs/events/016_brilliant_scientist/systems/alien_infantry.md`, the public API documentation, the V13 manifest, and the runtime handoff form the current generic-unit and model documentation chain.

### Still-open source ownership gap

`brilliant_scientist_portal_raid_establish_beachhead` in `common/scripted_effects/016_brilliant_scientist_raid_effects.txt` sets `brilliant_scientist_portal_beachhead_active`, changes the selected province controller, and creates the Portal Breach Cadre. No accepted source owner clears or transitions the transient active marker. The separate flags `brilliant_scientist_portal_raid_breach_recorded`, `brilliant_scientist_portal_raid_targeted`, `brilliant_scientist_portal_facility_extracted`, and `brilliant_scientist_portal_factory_extracted` are permanent history, not cleanup candidates.

The exact-province, actor, defender, one-breach-per-state, defender-resolution, war-end, invalid-country, and idempotent-cleanup contract remains queued in `016_alien_dhrondan_post_tranche_ownership_addendum_2026-08-26.md`. Its proposed 21-day and 25-Command-Power values are not accepted tuning. No arbitrary timer, native cooldown surrogate, immediate clear, or world scan may be substituted.

## Read-only MCP evidence and limits

No rewrite tool was used.

- Current `hoi4.focus_inspect` and `hoi4.focus_render` for `dhrondan_focus_tree` succeeded. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4248284f4d496a671b3767501f34921ee6ba0c4ac600c39eb0537525ef0f4b2d/7a9f20dc10b71cf71fb49c65eb4f0d9ec401bcce687c646aac5bf3473f7df833/focus-inspect.fc93286a7c2008c0.json`. Render entry: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23b539c032ae69ed551b0d3b9fbf0d05ca7578c374e400fe1a67d49d4eee96d2/7fc84b15e8eede9a671dc7d1e40e611bd590091ea8de1b338971ffcd09c5ea71/dhrondan_focus_tree.focus.html`. The only inline warning is the unrelated vanilla `continuous_restrict_freedom_desc` reference.

- Current `hoi4.event_inspect` for `chaosx.nr16.1` returned `EVENT_INSPECTED_PARTIAL` at revision `2b3b330f662608cdaac0d1c2b27f7e233c232225f39fbfe52312dc45d434449c`. The focused overview render returned nine selected nodes and zero blocking render diagnostics. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52019e323a248b24065b1901039a1ee77910106b2460a6c2f83d4d4ef8917ba3/0863c74c2f057c4168da703287b46d2fbbbff6a45a71ec142ee4951a96361a22/event-trace-2b3b330f6626.json`. Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6195b4bf57c4bc205170ba2f01040e73c950ab09faf26e20cf8867de8c38cae/afebf59ebf5af10602721d1209265c37f7c3e9bff21d9c21a779b4134e7f1522/event-overview-2b3b330f6626-manifest.json`. Full helper and lifecycle projection remains deferred by workspace size.

- Current `hoi4.event_inspect` state flow for `chaosx.nr16.47` returned `EVENT_INSPECTED_PARTIAL` at the same revision. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51042354f3e27caa4dca0d63e7b2fb7532bdf259a39b8a1d5016b152f6e60bae/be3ee4dc26d2d8ef3eb82bd2154908463e64352f17a2ed7121d40d34d31b5263/event-state_flow-2b3b330f6626.json`. The matching `hoi4.event_render` state view timed out after 180 seconds. The inspect does not execute the DHR transfer transaction.

- The same-day named GUI-worker evidence remains the current exact-window evidence for `kruger_directorate_container`: inspect artifact `gui-inspect.017d249c791c0735.json` with 22 Event 016 elements and packaged render `kruger_directorate_container-full.svg`. A fresh refresh started during this closure pass and was terminated at the parent's instruction not to wait on long MCP calls. This is an evidence limitation, not a discovered layout defect.

- The retained same-day map inspect/render proves static state/map parsing only. The map adapter cannot execute the dynamic owner/controller/core/claim/capital and cohort transaction. No map rewrite is proposed.

- The installed package exposes `hoi4.tech_inspect` and partial source-linked technology rendering, but it has no complete standalone Technology Tree Viewer and no accepted current technology comparison baseline. Alien Infantry technology placement, grants, tactic unlocks, and live consumers therefore remain partially evidenced rather than accepted.

- The installed package has no ordinary decision/mission visual inspect/render/compare route. Decision source review and probability adapters are not equivalent to live decision UI evidence.

## Weighted-logic disposition

No weight change is authorized by this closure.

The current named `chaosx_ai_probability_auditor` handoff is `016_alien_ai_probability_audit_current_2026-08-26.md`. It started investigated surfaces with `hoi4.probability_inspect` and records the exact conditional DHR rebellion shares, partial DHR focus and expedition scoring, incomplete landing inputs, Event `.49` isolation limits, Event 019 provider-508 adapter limits, and special-project AI incompatibility. The later survival/support-marker patches do not have a valid identical before/after comparison baseline.

Retain these rules:

- DHR revolt shares of 0/100, 10/90, 20/80, and 40/60 are conditional branch arithmetic only, not cumulative ninety-day revolt odds.
- Kruger-first selection when both expedition routes qualify is deterministic source priority, not a normalized random choice. Do not tune it without an explicit design disposition.
- Focus `ai_will_do`, decision/mission scores, native raid factors, special-project AI, Event `.49`, and provider 508 must not be described as click probabilities without complete named scenarios.
- Any future weighted patch requires a new auditor baseline, owner-applied patch, and same-scenario `hoi4.probability_compare`.

## 1. Implement now

These are bounded closure tasks that do not invent scope.

1. Reconcile stale closure wording. Update `016_improvement_loop_final_2026-08-26.md` so F016-IL-06 no longer lists the five support flags as unused, F016-IL-12 recognizes the four survival-marker consumers, and the resume checklist no longer asks to remove already-consumed flags. Record `016_dhr_route_consumers_patch_2026-08-26.md`, `016_dhrondan_survival_marker_consumption_2026-08-26.md`, and commit `56e5afbad` as the closing evidence.

2. Reconcile stale GUI wording. Update the same closure and the controlling completion handoff to recognize `016_dhrondan_gui_worker_attestation_2026-08-26.md` and commit `18f7c7d67`. Preserve its renderer limitations and user-owned live acceptance; do not redesign the compact GUI.

3. Add this closure delta to the Event 016 source-of-truth pointer chain. `016_core_runtime_handoff_map.md` should identify this file as the current improvement-loop disposition and retain `016_alien_dhrondan_post_tranche_ownership_addendum_2026-08-26.md` only for the unresolved Portal lifecycle and registry acceptance matrix.

4. Keep the caller-owned registry acceptance matrix in the binding acceptance checklist. Do not reapply the source patch. The next owner should execute country A/country B, ordinary/provider-508, duplicate-registration, state-loss, receipt-revocation, third-party occupation, capital, claim, core, controller, cohort, and 2,000-gun conservation cases when a capable adapter or user-owned live route is available.

5. Keep generic-unit documentation aligned with current runtime facts. The canonical Alien Infantry unit/API documentation should point to the V13 runtime handoff and mark older V8/V10/V11 or Quaternius records as historical. Preserve the locked, non-recruitable, zero-human-manpower, 2,000-weapon cohort contract and the exact seven required actions.

## 2. Queue with reason

1. Queue the Portal beachhead lifecycle under a named Portal containment owner. Reason: the transient marker has no cleanup owner, but exact lifecycle/tuning and a bounded war-relation hook are not yet accepted. Promote only the final accepted province/actor/defender/cleanup contract into the Portal specs before implementation.

2. Queue the full probability completion pass. Reason: the current adapter evidence is partial or unsupported for several weighted surfaces and no legal identical baseline exists for the post-marker-patch state. Do not change weights merely to make the audit quiet.

3. Queue the Alien Infantry muzzle/effect, strict-audio, positional/runtime, and live-consumer gates to `chaosx_3d_model_pipeline`. Reason: V13 establishes the Meshy 7 firearm-bearing model and seven source-backed actions, but no supported provider/adapter-authored muzzle locator exists, particle/light binding remains open, and selection/acknowledgement/impact/special-role audio breadth is incomplete. No inferred hand point or entity-origin fallback is authorized.

4. Queue the separate Portal Raider firearm-bearing model/action/audio package. Reason: its rifle-less geometry is rejected and unwired. Alien Infantry may not substitute for it.

5. Queue the optional KRG biological stockpile/delivery addendum behind the native CBRN reservation/outcome/cancellation/expiry callback. Reason: no safe native callback exists and no parallel payload ledger or free-charge fallback is authorized.

6. Queue user-owned live acceptance for opening/referral idempotence, all four evolutions, Directorate interaction, DHR transfer/capital behavior, Event 019 material conservation, native raid outcomes and beachhead state, Event Log/Details, super-event audio/queue/Fallout, terminal exclusivity, CXT setup, and custom-unit consumers.

## 3. Rejected or out of scope

- A fifth evolution or a replacement for `.21-.24`.
- An Event 016 cluster.
- Another DHR route, regime, country, formable, focus, decision family, super-event, or dedicated GUI.
- A second Alien Infantry registry, DHR-only landing ledger, Kruger-only unit identity, recruitable alien template, or additional alien technology tier.
- New decisions or spirits solely to consume markers that already have live readers.
- Another Directorate meter, tab, project family, synergy report, or routine incident.
- A new Portal raid family, arbitrary beachhead expiry, immediate active-marker clear, native cooldown surrogate, or whole-world cleanup on-action.
- A generic infantry entity, rifle-less model, inferred muzzle point, semantic action alias, transform-only motion, or static animation fallback.
- A DHR super-event or an ordinary Event Log row for `.40-.52`, project incidents, raids, or routine diplomacy.

## 4. Evidence blockers

1. The two-country/provider landing registry and DHR formation matrix has not been executed dynamically. Source ownership is corrected; dynamic transaction acceptance is not.

2. The current `.47` state render timed out after 180 seconds. Current root and `.47` inspectors are partial and defer large-workspace helper/lifecycle projection.

3. The map adapter cannot execute dynamic ownership, controller, core, claim, capital, cohort, and stockpile transactions.

4. The technology surface lacks a complete standalone Technology Tree Viewer and an accepted current before/after comparison baseline.

5. Ordinary decision/mission visual inspection and comparison routes are absent from the installed package.

6. Weighted landing, focus, expedition, Event `.49`, provider 508, native raid, special-project, and terminal scenarios remain partial, unsupported, or without identical baselines. No tuning conclusion is closed by source inspection.

7. Alien Infantry muzzle/effect binding, strict audio-role breadth, positional/runtime proof, and live consumer acceptance remain open. Portal Raider remains rejected and unwired.

8. User-owned live HOI4 acceptance is absent. No source count, MCP artifact, asset manifest, or static model registration replaces it.

## Promotion and resume rule

Keep this file in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/`.

Do not promote it wholesale into `docs/specs/016_brilliant_scientist_specs/` because it introduces no new accepted design. Promote only a later-approved Portal lifecycle contract, or a changed registry/technology/model acceptance rule, into the exact binding spec and acceptance sections that own it.

The parent should resume with documentation reconciliation, registry transaction evidence, the named Portal lifecycle disposition, probability completion, and 3D/runtime acceptance. Broad Event 016 expansion remains closed throughout.

No gameplay, asset, localisation, spreadsheet, or skill file was changed by this planning pass.
