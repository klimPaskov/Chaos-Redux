# Event 016 alien infantry API and Event 019 provider audit

Date: 2026-08-26

Status: read-only audit handoff; no gameplay source files were changed and no commit was created.

## Scope

This audit covers the reusable alien-infantry API, its unit and equipment declarations, its CXT setup hook, and the Event 019 provider-508 migration surfaces.

The reviewed gameplay files are common/scripted_effects/016_alien_infantry_api_effects.txt, common/scripted_triggers/016_alien_infantry_api_triggers.txt, common/units/016_brilliant_scientist_project_forces.txt, common/units/equipment/016_brilliant_scientist_project_force_equipment.txt, and common/on_actions/016_alien_infantry_cxt_on_actions.txt.

The Event 019 provider files reviewed are common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt, common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt, common/script_constants/016_brilliant_scientist_project_force_constants.txt, and their direct ledger call sites.

## Executive result

The current source matches the accepted API contract in the inspected areas: alien_infantry is the shared unit, alien_laser_weapon_equipment_1 is the buildable variant, the unit has zero human manpower, each battalion requires exactly 200 laser weapons, the public template is a locked ten-battalion 20-width D’Rhondan Landing Cohort, and the source-counted receipts cover Kruger, Mengele, Event 019 provider 508, D’Rhondan sovereignty, and future callers.

The five public API surfaces are present and connected: alien_infantry_grant_contact, alien_infantry_revoke_contact, alien_infantry_can_call_landing, alien_infantry_spawn_landing_cohort, and alien_infantry_reconcile_country.

Event 019 provider 508 now uses receipt 3, the shared landing materializer, the exact 2,000-laser debit/refund path, the allocated cohort deletion ID, and deferred commit/rollback callbacks. Its training and sustainment paths do not publish ordinary manpower, Infantry Equipment, Support Equipment, or a separate obligation row.

No confirmed parser defect was found. The accepted “0.75 recovery” value is correctly represented by the vanilla unit key default_morale = 0.75; adding a separate recovery key would be an unsupported parser risk.

No narrow gameplay patch was justified by the source or documentation evidence. The only changed file in this pass is this handoff.

## Proposed helper map and call sites

| Helper | Scope and inputs | Outputs and side effects | Current call sites |
| --- | --- | --- | --- |
| alien_infantry_grant_contact | COUNTRY; temporary alien_infantry_contact_source_id containing one of the five constant source IDs | Sets only the matching persistent receipt, ensures the hidden operational technology, and reconciles aggregate contact state | Kruger, Mengele, D’Rhondan sovereignty, Event 019 registration, Event 019 derivative setup, and future-source callers |
| alien_infantry_revoke_contact | COUNTRY; the same temporary source ID contract | Clears only the matching receipt and runs reconciliation; it does not revoke another source’s authorization | Event 016 runtime cleanup and Event 019 provider-508 derivative cleanup |
| alien_infantry_can_call_landing | COUNTRY trigger; aggregate contact, pending flag, cooldown, world-end state, laser stockpile, and any controlled valid state | Read-only boolean capacity gate for a new landing request | State-targeted Event 016 decision and Event 019 provider-508 management evaluation |
| alien_infantry_landing_target_is_valid and alien_infantry_landing_state_is_valid | COUNTRY trigger plus the selected state ID; state must be impassable-free, owned by ROOT, and controlled by ROOT | Read-only target validity; invalid targets are rejected before materialization and invalidate pending reservations | Reservation begin, reservation validity, and cohort spawn |
| alien_infantry_begin_landing_reservation | COUNTRY; selected dhrondan_landing_state_id and the can_call_landing gate | Debits exactly 2,000 alien_laser_weapon_equipment_1, marks one pending landing, stores seven reservation days, and activates the landing mission | Event 016 state-targeted decision |
| alien_infantry_cancel_landing_reservation | COUNTRY; pending flag and reservation state | Clears pending state and mission, refunds exactly 2,000 laser weapons, and clears the selected state; repeat-safe | Invalid/lost-state reconciliation, mission cancellation, and Event 019 structural refund callback |
| alien_infantry_spawn_landing_cohort | COUNTRY; selected state, contact, pending/direct-debit mode, optional DHR bootstrap mode, and optional Event 019 deferred transaction receipts | Creates one complete locked template cohort, proves the country-scoped division delta, applies ordinary landing telemetry/cooldown only after success, and refunds on failed materialization | Event 016 mission timeout, D’Rhondan bootstrap, and Event 019 provider-508 materialization |
| alien_infantry_register_landing_state | COUNTRY with dhrondan_landing_state_id resolving to a state | Saves regular event targets for the registry owner/state and appends the state target to the owner’s registry | Successful ordinary landing and deferred Event 019 commit |
| alien_infantry_reconcile_country | COUNTRY; source receipts, pending reservation, selected state, and world state | Recomputes aggregate contact, ensures technology/template while contact exists, initializes telemetry counters, and cancels a pending reservation whose state is no longer valid | Every grant/revoke path and daily/runtime repair paths |
| chaos_unit_family_provider_508_event19_materialize_landing | Event 019 generation context with infantry_spawn_generation_country, origin state target, and allocated deletion ID | Enters the generation country, records deferred transaction identifiers, and delegates all alien creation to alien_infantry_spawn_landing_cohort | Event 019 shared generation transaction |
| chaos_unit_family_provider_508_event19_commit_landing and chaos_unit_family_provider_508_event19_rollback_landing | Event 019 generation country and persistent deferred receipts | Commit records the successful landing only after final ledger proof; rollback deletes the exact cohort and refunds the one proven debit | Event 019 transaction commit/rollback dispatch |
| chaos_unit_family_provider_508_event19_reconcile_sustainment | Event 019 provider callback context | Explicit zero-row callback: clear, record, and clear the provider obligation manifest | Event 019 sustainment reconciliation |

## Contract and constant evidence

The unit declaration in common/units/016_brilliant_scientist_project_forces.txt:303-334 uses alien_infantry, active = no, combat width 2, maximum strength 40, maximum organisation 90, default_morale = 0.75, manpower 0, suppression 5, supply 0.04, reconnaissance 10, initiative 0.50, and exactly 200 alien_laser_weapon_equipment per battalion.

The corresponding equipment declaration in common/units/equipment/016_brilliant_scientist_project_force_equipment.txt:597-629 defines the alien_laser_weapon_equipment archetype and alien_laser_weapon_equipment_1 variant with the accepted 0.98 reliability, 6.5 speed, 60 defense, 40 breakthrough, 0.40 hardness, 30 armor, 30 soft attack, 20 hard attack, 80 piercing, 10 air attack, and 0.75 industrial cost. Licensing and lend lease are disabled, and production requires the aggregate contact trigger.

The API template builder at common/scripted_effects/016_alien_infantry_api_effects.txt:137-170 creates or relocks the only public D’Rhondan Landing Cohort template with ten explicit alien-infantry components, is_locked = yes, and force_allow_recruiting = no.

The five receipt IDs are defined in common/script_constants/016_alien_infantry_api_constants.txt: Kruger pact 1, Mengele expedition 2, Event 019 provider 508 3, D’Rhondan sovereignty 4, and future 5. Grant and revoke compare the same source ID and mutate only the corresponding alien_infantry_contact_receipt_* variable.

The reservation constants are 2,000 laser weapons and seven days. The default landing cooldown is 30 days, with D’Rhondan recovery tiers of 24, 18, and 12 days. Successful ordinary landings apply +1 arrival, +1 Alien Presence, +5 Pact Strain, and +1 landing-history count.

The family block chaos_unit_family_event16_alien_infantry in common/script_constants/016_brilliant_scientist_project_force_constants.txt:507-540 records provider/family 508, source event 16, ten template battalions, zero manpower, zero ordinary equipment, 200 laser weapons per battalion, zero ordinary/support equipment, and zero training/sustainment costs.

The CXT hook in common/on_actions/016_alien_infantry_cxt_on_actions.txt uses one bounded random_country startup registration and an additive tag-guarded on_daily_CXT repair/synchronization path, matching docs/testing/chaosx_test_country.md. It does not add a broad unbounded daily action.

## Event target, variable, and cleanup plan

The selected state is carried in the country variable dhrondan_landing_state_id. The regular event targets alien_infantry_landing_registry_owner and alien_infantry_landing_registry_state are saved only while the registration chain is active, which matches the documented short-lived event-target lifecycle.

The Event 019 transaction carries infantry_spawn_generation_country and infantry_spawn_current_origin_state through the shared generation framework. Provider 508 copies the allocated infantry_spawn_current_delete_cohort_id into alien_infantry_delete_cohort_id and records dhrondan_landing_state_id before invoking the deferred API branch.

The deferred state uses alien_infantry_event19_deferred_mode and alien_infantry_event19_deferred_debit_committed. Commit clears the selected state, deferred flags, deletion ID, and outer transaction receipt after recording the success. Rollback refunds exactly 2,000 laser weapons when the committed debit receipt exists and clears the same transient/persistent transaction state. The API does not introduce a new global event target.

When a reservation becomes invalid because the target is lost or invalid, reconciliation calls the idempotent cancellation helper. A successful ordinary landing clears pending state before applying the cooldown. The source cleanup paths revoke only their own receipt, including Event 019 provider 508 receipt 3.

## Event 019 migration plan and current implementation

1. Provider 508 registration in 016_brilliant_scientist_project_force_event19_effects.txt:51-62 grants only the Event 019 provider-508 receipt and registers the provider identity when the alien arms or operational technology is available.

2. Provider 508 template construction at :668-676 ensures the API-owned locked template and appends ten combat-component manifest entries without creating a second template.

3. Provider 508 materialization at :701-710 passes the shared Event 019 deletion ID and selected origin state into the API deferred branch. The provider does not implement a parallel alien spawn or equipment debit.

4. Provider 508 commit and rollback at :714-720 dispatch to the country-scoped API transaction helpers. The shared spawner therefore owns exact cohort deletion, refund, state markers, landing history, presence, Pact Strain, and cooldown ordering.

5. Provider 508 sustainment at :747-752 deliberately publishes no obligation row. Its clear/record/clear sequence is a framework callback with an empty manifest.

6. Provider 508 management payment at :1613-1623 only satisfies the Event 019 transaction gate. The API materializer owns the 2,000-laser debit. The refund callback at :1654-1662 can cancel a surviving pre-materialization reservation and cannot double-refund a materialized cohort.

7. Provider 508 derivative setup and cleanup at :1921-1927 and :1953-1958 grant and revoke only source receipt 3. The generic Event 019 cleanup remains responsible for the provider framework records.

## Risks, unsupported analysis, and unimplemented gaps

### No confirmed parser defect

The offline Unit Modding page defines default_morale as the unit recovery-rate input, so the current default_morale = 0.75 is correct. The offline and vanilla trigger documentation accept the current shorthand check_variable = { variable > 0 }, and the vanilla effects documentation accepts the current create_unit arguments used by the API: division, owner, count, and id.

No recovery = unit key was added, no broad on-action was added, and no Event 019 ordinary-resource fallback was introduced.

### Engine-unverified inactive-subunit boundary

The API-owned unit is active = no, and the hidden operational technology enables the laser equipment but deliberately does not use enable_subunits. The existing system documentation states that this preserves inactive division-designer status while the API constructs the locked template. The CXT test fixture explicitly calls unlock_subunit = alien_infantry, which is a test-country setup path rather than normal gameplay.

The source-only evidence cannot prove whether the live engine accepts the normal API template construction without an explicit subunit unlock. The dedicated technology/unit MCP lint calls timed out, so this remains a runtime validation follow-up rather than a confirmed source defect.

### Event 019 management capacity gate

Provider 508 management evaluation at :1097-1110 requires the provider receipt, alien_infantry_can_call_landing, and an eligible state. Since alien_infantry_can_call_landing rejects an active pending reservation, active cooldown, insufficient stockpile, and world-end state, Event 019 management will not expose provider 508 during those conditions. This is consistent with the accepted one-pending/30-day anti-duplicate contract, but it is a design/runtime risk if the Event 019 management surface is expected to queue a request while a D’Rhondan reservation or cooldown exists.

### D’Rhondan global state scan remains outside this bounded surface

The existing D’Rhondan country effects still contain global scans/counts of marked landing states. Replacing those scans with the API registry would change a broader D’Rhondan design and was not authorized in this audit; the prior reconciliation handoff records that blocker.

### MCP and probability limitations

The required read-only hoi4.probability_inspect route accepted the source shape { path = ... } but timed out after 180 seconds on the alien landing decision. The adapter-list request returned PROBABILITY_ADAPTERS_LISTED with no artifact. The required chaosx_ai_probability_auditor capability is not exposed in the current tool list, so no custom auditor evidence pass or probability comparison can be claimed.

The Event 019 root chaosx.nr19.1 was confirmed from events/019_infantry_spawn.txt, but the corrected hoi4.event_inspect selector using eventId timed out after 180 seconds in state_flow mode.

The available hoi4.tech_inspect lint route timed out after 180 seconds for both alien_laser_weapon_equipment_1 and alien_infantry. No dedicated unit/equipment route completed, so source review is not equivalent to engine lint evidence.

The previous D’Rhondan probability handoff contains a completed probability-inspect artifact at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba3f44770f08d71e20b0b4a7b7abf983f797e0bbf5dad4931e953ab67fb1db94/b57ddac0f6d7cbe18b9c527093acd93a10f84146ec886f88ef28da658f17ffa9/probability-inspect-fcd942b6523a.json, but it is prior evidence for the D’Rhondan rebellion pulse and not a substitute for the timed-out current landing-decision pass.

## Validation performed

The source audit traced all five receipt grants and revokes, the API call sites, the exact reservation/debit/refund amounts, the country-scoped cohort delta proof, the Event 019 provider-508 callbacks, and the empty sustainment obligation manifest.

The unit and equipment values were compared with the accepted addendum, the offline Paradox wiki, and the matching vanilla documentation. The CXT startup/daily registration was compared with docs/testing/chaosx_test_country.md.

The owned gameplay files returned no entries from git status --short -- <owned paths> before this handoff was added. No live Hearts of Iron IV process was launched, and no in-game completion claim is made.

## Files changed in this pass

- Added docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_api_audit_current_2026-08-26.md.
- No gameplay source, constant, unit, equipment, on-action, decision, or Event 019 provider file was modified.

## Parent action requested

Treat the current API/provider source as contract-aligned pending engine evidence. If a live or completed MCP scenario proves that active = no prevents API construction without unlock_subunit, resolve that boundary in the owning design/spec before changing the normal API. If Event 019 management must bypass D’Rhondan pending/cooldown gating, that is a design change rather than a parser fix and should be accepted before patching the provider gate.

This handoff does not claim whole-event, asset, GUI, probability, or in-game completion.
