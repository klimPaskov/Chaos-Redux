# Event 016 Alien Infantry and Empire of D’Rhonda current completion audit

Date: 2026-08-26

Auditor: `chaosx_event_completion_auditor`

Mode: read-only gameplay audit; this handoff is the only file authored by the auditor.

Overall status: **INCOMPLETE**.

The accepted Alien Infantry and Empire of D’Rhonda implementation is broad and substantially aligned in current source, and the V13 model promotion closes the former missing-action blocker. Completion is still withheld because the muzzle particle and light have no supported locator or runtime binding, the accepted owner-scoped landing-registry scenarios have not been dynamically proved, current MCP comparison coverage is unavailable, weighted surfaces do not yet have complete named-scenario evidence, strict audio-role coverage remains incomplete, and user-owned live acceptance does not exist. Historical pre-promotion records remain retained with superseded notices, while current pointers are reconciled by the documentation handoff for this pass.

This audit distinguishes source and artifact evidence from engine or live proof. `Evidenced` means the current source or immutable artifact matches the accepted requirement. `Incomplete` means a real implementation exists but one required consumer, evidence layer, or disposition is missing. `Missing` means no required implementation or document was found. `Contradictory` means current sources or current-status documents disagree. `Blocked` means the required route was attempted or inspected and cannot presently provide the required proof.

## Authority and accepted-plan disposition

The binding design is `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`.

The parent-owned acceptance checklist is `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`.

The accepted addendum is promoted into the spec pack. The broad improvement loop is correctly closed: no extra DHR route, country, formable, scripted GUI, raid family, super-event, or parallel Alien Infantry system is required. Events `.40-.47` remain follow-up events rather than evolutions, DHR has no separate super-event, and Event 016 remains one minor fire-once event with exactly four logged evolutions and no cluster.

The narrow 2026-08-26 ownership addendum is only partially disposed:

- The severity-one landing-registry ownership defect is repaired in current source. `alien_infantry_register_landing_state` saves the invoking country and selected state as regular event targets before returning to the caller-owned `alien_infantry_landing_state_registry`, and DHR consumes only the pact host's array.
- `common/scripted_effects/chaosx_dynamic_effects.md:457-463` documents the corrected caller-owned contract.
- The binding spec and acceptance checklist now state the accepted caller-owned registry rule and the addendum's cross-country, ordinary-versus-provider-508, idempotence, and receipt-revocation scenarios. Dynamic execution evidence remains incomplete.
- The five support-route markers listed below were consumed by the subsequent route-consumer repair. The older audit wording is retained as historical context only; current source consumers are listed in the corrected focus/decision row below.
- The V13 one-image Meshy package is accepted, exported, actual-byte reimported, and promoted into current runtime files. The particle/light locator and broader audio-role gates remain open.

The older `016_alien_dhrondan_improvement_loop_closure_handoff_2026-08-22.md` is stale where it says the fifteen-cohort cap conflicts with one cohort per enclave and where it says model recovery needs new user approval. The current binding spec resolves the enclave case through separately recorded supplemental costed cohorts, and current policy preauthorizes planned provider recovery while balance and capability permit it.

The 2026-08-26 ownership addendum also cites two paths that do not exist:

- `docs/specs/016_brilliant_scientist_specs/016_source_of_truth_map.md`
- `docs/specs/016_brilliant_scientist_specs/acceptance/016_alien_dhrondan_acceptance_scenarios.md`

The actual files are under `docs/plans/016_brilliant_scientist_plans/`. The plan-level `016_source_of_truth_map.md` is dated 2026-07-14 and explicitly labels much of its implementation and asset state historical, so it should not be presented as a current spec-pack path.

## Completion status by surface

| Surface | Status | Current evidence and disposition |
| --- | --- | --- |
| Public identifiers and receipts | Evidenced in source | `alien_infantry` and `alien_laser_weapon_equipment_1` are the concrete unit/equipment consumers. `common/script_constants/016_alien_infantry_api_constants.txt` assigns independent receipt IDs 1-5 for Kruger, Mengele, Event 019 provider 508, DHR sovereignty, and future sources. `common/scripted_effects/016_alien_infantry_api_effects.txt:12-131` grants and revokes only the selected receipt. |
| Unit, equipment, template, tactics, and hidden technologies | Source-evidenced; current MCP comparison incomplete | The exact battalion/equipment values, ten-battalion locked template, two alien-only tactics, predictive dependency, equipment gates, and enum registration are present. The current technology inspect/render is partial because workspace-wide helper projections are deferred, and no before/after technology comparison exists. |
| DHR envoy project and access routes | Evidenced in source | The air project, breakthrough cost 5, very-long time, insane complexity, four resource costs of 5, Kruger/KRG/Mengele/future gates, one-use Antarctica 025 bypass, Event 036 exclusion, and both shared project selectors are implemented. |
| Expedition and pact chain `.40-.47` | Source-evidenced; current full-chain MCP blocked | Events, costs, 180-day missions, Kruger suspension/restore, exact Directorate deltas, Mengele separation, pact receipts, landing report, failure, warning, and revolt bridge exist. `.47` has a retained partial inspect and successful state-render artifact, while fresh `.40` inspect/render calls timed out, so the whole chain is not currently rendered or compared. |
| Paid state landing | Source-evidenced; runtime scenario proof blocked | The one-pending seven-day reservation, exact 2,000-gun debit/refund, target revalidation, 30/24/18/12 cooldown ladder, success telemetry, state/history markers, and Honor Accord values exist. State loss, delayed cancellation, duplicate request, and cooldown transitions still lack current engine/live acceptance. |
| Event 019 provider 508 | Source-evidenced; transaction proof incomplete | Provider/family 508 registers as spawn-only, uses the one API template, narrows each request/actor to one state, delegates the exact debit, defers telemetry until commit, deletes/refunds only on proven rollback, and revokes only its receipt during derivative cleanup. The retained `nr19.1` MCP artifact is structural only and does not prove one-cohort or stockpile conservation. |
| Rebellion probability and cadence | Exact source arithmetic evidenced; complete probability acceptance incomplete | Constants and source implement the 90-day country pulse with gates 6 arrivals, strain 30, chaos 600 and exact conditional 10/20/40 revolt weights. Existing MCP evidence proves branch arithmetic only, not cumulative cadence or all weighted surfaces. |
| DHR state formation and force conservation | Source-evidenced; high-risk runtime behavior blocked | Current source captures the pact host's registry, transfers host-owned marked states, preserves third-party control, adds DHR cores while restoring host cores, claims lost states, chooses a viable marked capital, deletes host cohorts without refund, and transfers the laser stockpile. The adapter cannot execute the dynamic controller/core/capital transaction. |
| Initial and supplemental cohorts | Source-evidenced; dynamic component proof blocked | The ordinary count is `max(5, min(15, marked_states + floor(arrivals / 2)))`. Each disconnected viable component is seeded before capital concentration, and any component beyond the ordinary reserve receives one separately counted 2,000-gun supplemental cohort through the same API. No current engine run proves flood-fill termination, component isolation, exact debit count, or rollback behavior. |
| Fixed DHR country and roster | Evidenced in source and assets | The fixed dormant DHR tag, country history, three regimes, twelve recruited identities, five civilian advisors, one high-command advisor, three commanders, flags, ideas, portraits, and runtime role installers exist. Dynamic annexation/reinitialization remains unproved. |
| CXT extension contract | Source-evidenced; live harness proof blocked | Event 016 provides the modifier-free hidden carrier `chaosx_cxt_extension_event016_alien_infantry`, matching `_apply` setup effect, bounded additive `on_startup` registration, guarded `on_daily_CXT` repair, Envoy/equipment/sub-unit registrations, and one locked non-recruitable model-overridden CXT template. The processed-token array prevents the core helper from creating a recruitable duplicate. No live CXT invocation proves first-run registration, equipment fill, model/counter display, or idempotent daily repair. |
| DHR 88-focus tree | Current inspect/render and source structure evidenced; quantitative AI proof incomplete | Current source contains exactly 88 focuses and 88 inline `ai_will_do` blocks in the accepted `8/24/10/12/8/8/12/6` distribution. Three mutually exclusive political routes and three replace-in-slot spirit lifecycles exist. The probability auditor obtained a current focus inspect/render with 88 focuses, 102 connectors, and no layout diagnostics. The all-88 weighted pool was discovered, but no route evaluation can run without prerequisite history, route/bypass state, plan activation/abort state, and complete external factors. |
| DHR focus and decision consumers | Source-complete; current weighted proof incomplete | All five route-support markers now have real consumers: standardized components and the orbital office influence the paid landing AI, perfected predictive warfare gates and weights reclamation, the completed laboratory route gates and weights enclave support, and access-map exchange gates the Covenant compact. The four opening survival markers likewise influence the landing or enclave-support AI. Existing decisions cover reclamation, enclave supply, integration, and compact behavior; there is no ordinary decision MCP inspector/renderer in the installed route set. |
| Dedicated scripted GUI | Not applicable by accepted design | DHR introduces no dedicated scripted GUI. The normal focus, decision, event, and country surfaces are intentional. No `chaosx_event_ui_worker` handoff is required for DHR, and no new DHR GUI should be invented to close marker gaps. |
| Event Log, Event Details, and evolutions | Evidenced in source | Event 016 registers exactly four evolution stages and four detail previews. `chaosx.events_log.window.event_details.brilliant_scientist` appends `GetDhrondanEventDetailClause` only after sovereignty. `.40-.52` remain consequence popups, not new log events or evolutions. |
| Workbook and CSV exports | Evidenced and aligned | Direct read-only workbook inspection found row 16 with four populated evolution fields, a blank fifth field, both Event 016 world ends, `Minor Fire-Once`, chaos level 1, blank cluster, and `Needs Testing`. Every row-16 and row-19 field matches the current CSV export exactly, and the CSV is newer than the workbook. |
| V13 mesh and seven actions | Evidenced in immutable package and current runtime bytes | The approved source, Meshy 7 lineage, 59,999-triangle mesh, scale 0.8, packed textures, seven distinct provider actions, and actual-byte reimports are documented in `attempts/v13_firearm_preset/final_manifest.md`. Current runtime mesh/action hashes match that manifest. |
| Runtime entity and accepted audio roles | Static registration present; live acceptance incomplete | `gfx/entities/alien_infantry.gfx` and `.asset` register the mesh, seven actions, scale, and four state sound references. The locked template currently sets `override_model = alien_infantry_entity`. The particle and light definitions remain unbound because the mesh has no supported muzzle locator, and static references do not prove live consumer playback. |
| Required sourced audio breadth | Incomplete under the strict 3D pipeline | The four binding-spec roles have CC0 source pages, authors, licenses, original/derived checksums, exact WAVs, synchronization points, sound definitions, and entity events. The model pipeline handoff explicitly leaves subunit selection/acknowledgement, impact, and special-action roles blocked rather than substituting generated or placeholder audio. |
| Large and map counters | Evidenced except live display | Original large and on-map counter art, installed vanilla definition/DDS inspection, skill-local reference-family inspection, sampled vanilla green, native alpha, final DDS, GFX registration, hashes, and comparison evidence are present. User-owned live display remains pending. |
| Icons, flags, event art, country interface, and achievement hook | Evidenced | The completed package has 88 focus DDS files, 11 lifecycle idea DDS files, exact decision/project/equipment/technology/tactic/report/news registrations, four DHR flag ladders, and no unresolved consumed token. Seven unused art candidates are intentionally archived outside runtime. The existing `016_brilliant_scientist_not_from_here` triplet and alternative DHR completion path satisfy the existing-achievement requirement without adding an eighteenth achievement. |
| Fictional DHR portraits | Asset-complete; routing attribution needs clarification | The twelve native-ImageGen sources, processed PNGs, full DDS, nine role cards, hashes, GFX registrations, runtime character tokens, and parent visual approval are documented. The handoff names owner `/root/dhr_portraits` but does not explicitly state that it is the required `chaosx_portrait_creator` handoff; add role attribution if the task path is not already durable proof of that route. No asset regeneration is indicated. |
| Current documentation and manifests | Reconciled for V13 static promotion; historical records retained | Event 019 family coverage, the public dynamic API registry, DHR country/focus docs, V13 manifest, model promotion handoff, icon package, portrait handoff, counter handoff, and audio provenance are useful. Historical V8/V10/Quaternius and pre-promotion unwired statements remain evidence-only with superseded notices; current runtime pointers distinguish provider evidence, static registration, and live acceptance. |
| Mandatory final audit and live acceptance | Blocked/incomplete | Focus, decision/mission, country, localisation, event-completion, asset, and probability handoffs exist, but several predate the registry or V13 promotion and retain superseded blockers. Full current MCP comparisons and user-owned in-game acceptance are absent. |

## Binding requirement crosswalk

### Public Alien Infantry contract

| Requirement | Classification | Evidence or gap |
| --- | --- | --- |
| One provider-neutral unit/equipment API shared by Event 016, Event 019, DHR, and future callers | Evidenced | Public API files and `docs/events/016_brilliant_scientist/systems/alien_infantry.md` use the shared identifiers; no DHR copy was found. |
| Independent numeric receipts; one revocation preserves every other source | Evidenced in source; engine scenario blocked | Constants define five independent sources, grant/revoke branches mutate one named variable, and `alien_infantry_has_contact` ORs positive receipts. The accepted multi-receipt revocation scenario has no current adapter/live proof. |
| Caller-owned landing history across independent countries/providers | Source-evidenced; dynamic acceptance blocked | Current effect code, dynamic API docs, binding addendum, and acceptance scenarios state the owner-country contract and required cross-country/provider matrix. Dynamic execution evidence remains unavailable. |
| Exact battalion values and 200 laser weapons per battalion | Evidenced | `common/units/016_brilliant_scientist_project_forces.txt:303-333` resolves width 2, HP 40, organisation 90, recovery 0.75, recon 10, initiative 0.5, suppression 5, supply 0.04, manpower 0, and need 200 through file-scoped constants. |
| One locked ten-battalion, 20-width, 2,000-gun template with no manual recruit/duplicate/edit path | Evidenced in source | `alien_infantry_ensure_landing_template` creates ten battalions, `is_locked = yes`, `force_allow_recruiting = no`, reapplies both locks, and currently overrides the model to `alien_infantry_entity`. The offline Division Modding reference confirms that a locked template prevents player creation/deletion/editing unless recruiting is force-enabled. |
| Exact laser equipment values, no licensing, no lend-lease, contact-gated production | Evidenced | `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt:597-629` resolves the accepted values, `can_license = no`, `can_be_lend_leased = { always = no }`, and `can_be_produced = { alien_infantry_has_contact = yes }`. |
| Two exact predictive tactics restricted to Alien Infantry and unlocked by dependent hidden technology | Evidenced in source; current technology comparison blocked | `common/combat_tactics.txt:1280-1320` requires `has_unit_type = alien_infantry`; `common/technologies/016_brilliant_scientist_project_force_technologies.txt:106-114` depends on the base tech and enables both tactics. |
| No normal alien training or focus/decision bypass of the 2,000-gun landing | Evidenced in source | The unit is inactive, the only public creation path is the locked API template, focus helpers set `dhrondan_alien_infantry_training_forbidden`, and no DHR focus/decision directly creates a unit or free laser stockpile outside the one-time sovereignty force contract. |
| Package-owned idempotent CXT registration | Source-evidenced; live harness acceptance blocked | `common/ideas/016_alien_infantry_cxt_extension_ideas.txt`, `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt`, and `common/on_actions/016_alien_infantry_cxt_on_actions.txt` satisfy the documented carrier/`_apply`/startup/daily contract. Event 016 intentionally creates a locked one-battalion test template and records `alien_infantry` as processed instead of exposing the normal recruitable CXT path. |

### Event 019 provider 508 migration

| Requirement | Classification | Evidence or gap |
| --- | --- | --- |
| Provider and family identity 508, spawn-only, one API template | Evidenced | Registration and build callbacks are at `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:169-184` and `:668-675`. |
| Each automatic/scenario actor produces at most one selected-state cohort without changing shared intensity | Evidenced in source; dynamic scenario blocked | `common/scripted_effects/019_infantry_spawn_core_effects.txt:430-460` narrows provider 508 to one state. No current engine artifact proves all scenario wrappers. |
| Exactly one 2,000-gun debit; deferred state/history/cooldown commit; exact delete/refund on rollback | Evidenced in source; transaction acceptance blocked | Provider callbacks at `:698-720`, the API commit/rollback at `016_alien_infantry_api_effects.txt:551-597`, and Event 019 documentation align. The retained Event Inspector path cannot prove stockpile conservation or delayed same-tag rollback. |
| Derivative cleanup revokes only receipt 508 | Evidenced | Setup and cleanup at `:1921-1958` grant/revoke only `event019_provider_508` before generic derivative cleanup. |

### D’Rhondan contact, landing, and rebellion

| Requirement | Classification | Evidence or gap |
| --- | --- | --- |
| Exact Envoy Craft project and route visibility/availability | Evidenced | `common/special_projects/projects/016_dhrondan_envoy_project.txt` and `016_dhrondan_contact_triggers.txt` align with the accepted air/5/very-long/insane/resources and route/operational-work contract. |
| Antarctica 025 bypass once; Event 036 is not alien-contact proof | Evidenced | `dhrondan_antarctic_craft_bypass_is_valid` requires `antarctica_success`, consumes its own flag, and no Event 036 identity is present in the DHR contact/API surface. |
| Both shared project selectors include the craft without bypassing gates | Evidenced in source; weighted selection acceptance incomplete | `cbrn_project_effects.txt` includes the gated random completion row. `germany_mengele_effects.txt:2238-2451` includes all-project and random availability flags/weight. Current selection probabilities remain part of the incomplete probability pass. |
| Kruger and Mengele expeditions cost 50 PP and 500 fuel and last 180 days | Evidenced | Contact constants and decisions/missions use the exact values. |
| Kruger suspension/restore and exact Directorate deltas; no Directorate deltas for Mengele | Evidenced in source; transfer/runtime scenario blocked | `016_dhrondan_contact_effects.txt:39-112` uses the fixed character and canonical role helpers. Authorization applies +10 Mandate/Dependence/Independent Capacity, +5 Exposure, -5 Grievance; return applies +5 Mandate/Dependence/Independent Capacity. The Mengele branch does not call them. |
| `.40-.47` own follow-ups and are not evolutions | Evidenced in source; current render blocked | All eight triggered events exist with registered pictures and localisation. Event 016's evolution registry remains stages 1-4 only. |
| One seven-day pending landing, exact loss refund, success telemetry, cooldown reductions only | Evidenced in source; dynamic acceptance blocked | API constants/effects/triggers/decisions align. The focus reward changes cooldown markers only and grants no free cohort. |
| Honor Accord 75 PP, -10 strain, 180-day cooldown | Evidenced | Constants, decision, effect, and localisation align. |
| Ninety-day pulse with exact gates and 10/20/40 conditional revolt chances | Source-evidenced; probability/cadence acceptance incomplete | The country-scoped mission and random list align. Existing evidence proves branch shares, not cumulative cadence or recovery. |

### DHR country package and focus tree

| Requirement | Classification | Evidence or gap |
| --- | --- | --- |
| Fixed dormant DHR tag and idempotent initialization | Evidenced in source; runtime reinitialization blocked | Tag, country, history, empty dormant OOB, global one-time receipts, character recruitment, runtime install, and focus reload exist. Annexation/release replay remains unproved. |
| Transfer host-owned marked states, retain third-party occupations, claim lost states, add DHR and preserve host cores, choose viable marked capital | Source-evidenced; engine state-transfer proof blocked | `016_dhrondan_country_effects.txt:18-133` implements the contract. Static map inspection cannot execute or compare it. |
| Delete surviving host cohorts without refund and transfer full laser stockpile | Source-evidenced; live conservation blocked | `dhrondan_conserve_revolt_military_assets` uses `delete_units` and `send_equipment`. No current runtime receipt proves exact conservation. |
| Ordinary opening formula and one separately recorded costed supplemental cohort per uncovered component | Source-evidenced; dynamic flood-fill proof blocked | Constants and `:315-465` implement the formula, component pass, supplemental store, extension counter, and API debit. The earlier max-15 contradiction is superseded. |
| Later uprising joins existing DHR; annexation recovery cannot duplicate opening package | Source-evidenced; runtime idempotence blocked | Global formation/news/opening flags and active-tag branches exist. No current engine scenario proves all replay cases. |
| Three accepted regimes, five civilian advisors, one high command, three commanders | Evidenced | Current character source defines exactly twelve identities: three leaders, six advisor/high-command figures, and three corps commanders. Runtime role installers map Imperial, Synod, and Covenant governments as accepted. |
| Exactly 88 focuses in accepted category distribution and three eight-focus political routes | Evidenced | Current counts are 88 focuses, 88 `ai_will_do` blocks, and the accepted `8/24/10/12/8/8/12/6` family distribution. |
| At most three focus-created spirits coexist | Evidenced in source | `016_dhrondan_focus_effects.txt:13-119` clears and replaces one homeworld/political, one predictive/military, and one off-world lifecycle slot. |
| Distinct route identities, rewards, diplomacy, expansion, and AI priorities | Incomplete quantitative acceptance | Distinct routes, focus rewards, decision gates, and four strategy plans exist. Generic support focuses are not fully enumerated in each route plan, and the named focus-probability scenarios remain partial. |
| Origin reclamation, integration, enclave crises, news, Event Log, Event Details, and existing achievement hook remain reachable | Source-evidenced; runtime reachability blocked | Current decision triggers consume the four world-order markers; country events `.48-.52`, sovereignty news, DHR detail clause, and `Not From Here` alternative path exist. Live route traversal remains pending. |
| Every reward marker has a consumer or explicit reserved disposition | Source-complete; weighted proof incomplete | `dhrondan_alien_components_standardized` and `dhrondan_orbital_office_reassembled` feed landing AI; `dhrondan_laboratory_route_complete` gates and weights enclave support; `dhrondan_predictive_warfare_perfected` gates and weights reclamation; and `dhrondan_access_map_exchange_ready` gates the Covenant compact. The four opening survival markers have separate landing/enclave-support AI consumers. |

### Assets and presentation

| Requirement | Classification | Evidence or gap |
| --- | --- | --- |
| One approved V13 source; Meshy 7 exclusively; vanilla scale; packed materials; actual-byte reimport | Evidenced | V13 final manifest, generated task lineage, final hashes, Blender adapter reports, and runtime promotion align. |
| Genuine idle, move, laser attack, defend, support attack, retreat, and death | Evidenced | Seven distinct Meshy action IDs and seven distinct current runtime `.anim` hashes match the final manifest. Training/wounded reuse idle/defend only as non-required HOI4 states; they do not replace any accepted role. |
| Laser particle/light/sound synchronized at a supported muzzle point | Missing/blocked | Static entity sound references use the accepted V13 action times, but positional playback is not accepted. `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash` are defined but never referenced by the entity or an action event. The mesh has no muzzle node and the adapter has no approved locator-authoring route. Vanilla's `units_infantry.asset` precedent binds weapon effects to a named `muzzle` node, so binding at entity origin or an inferred hand point is not acceptable evidence. |
| Four accepted sourced audio roles | Evidenced | CC0 provenance, source pages, creators, licenses, original/derived hashes, transformations, runtime WAVs, definitions, and exact entity times exist for laser fire, movement, idle, and death. |
| Full custom-unit audio-role coverage under the 3D pipeline | Incomplete/blocked | Selection/acknowledgement would replace tag-wide vanilla voices, and impact/special candidates were not accepted. The handoff correctly keeps these blocked rather than using synthesized, generated, recorded, placeholder, or unlicensed substitutes. |
| Bespoke vanilla-green counters for all used surfaces | Evidenced except live display | Large and map counter packages pass definition/DDS/reference/palette/original-art/hash/GFX evidence. |
| All other original assets and existing achievement hook resolve | Evidenced | Focus, idea, decision, project, report/news, equipment, technology, tactic, flag, country interface, portrait, and existing achievement assets resolve. Seven unconsumed candidates are explicitly archived and are not missing current consumers. |
| Complete fictional portrait packages through the required portrait workflow | Asset evidence complete; route attribution ambiguous | Native ImageGen, processing, DDS, role-card, wiring, and manifest evidence are complete. The handoff should explicitly identify `chaosx_portrait_creator` if `/root/dhr_portraits` is not a durable alias for that custom role. |

## Exact gaps, contradictions, and stale completion claims

### P0 blockers

1. **No supported muzzle particle/light binding.** Current sound synchronization is real, but the particle and light are definition-only. The model promotion handoff explicitly refuses to invent a locator, which is correct. Completion requires a provider/adapter-supported muzzle node or an explicitly accepted permanent blocker; placing the effect at entity origin or an inferred hand point would be an unapproved fallback.

2. **No complete current MCP comparison package.** This auditor's fresh event, focus, and technology calls timed out after 180 seconds. The probability auditor subsequently obtained a current focus inspect/render and current all-88 probability discovery, but the contact chain, DHR follow-ups, Event 016 root/evolution chain, Event 019 provider path, and Alien Infantry technology still lack current full inspect/render/compare evidence. No valid before/after MCP revision baseline exists for event, focus, technology, probability, decision, or state-transfer comparisons.

3. **No dynamic cross-country registry/formation acceptance.** The source defect is corrected, but the addendum's exact two-country, ordinary-versus-provider-508, duplicate-registration, lost-state, receipt-revocation, capital, claims, core, controller, and cohort-isolation matrix has not been executed or promoted into the acceptance checklist.

4. **No user-owned live acceptance.** Unit rendering, action selection, audio mixing, counter display, state-targeted decisions, stockpile conservation, DHR release/transfer, focus loading, annexation recovery, Event Log/Details presentation, and campaign behavior remain unaccepted in game.

### P1 actionable gaps

1. **DHR marker weighted proof remains open.** The route-support and opening-survival flags now feed existing landing, enclave, reclamation, and compact surfaces; rerun named probability scenarios when the MCP route is responsive rather than adding duplicate decisions.

2. **The registry fix still needs dynamic acceptance.** The caller-owned registry contract and cross-country/provider cases are now promoted into the binding spec and acceptance checklist; execute them when the adapter or user-owned live route is available.

3. **The current model runtime documentation required reconciliation.** The canonical Alien Infantry system, asset runtime handoffs, V13 manifest, Event 016 ledgers, and current model handoffs are updated by `alien_infantry_docs_reconcile_current_2026-08-26.md`; retained V8/V10/V11/Quaternius records now carry superseded notices. `016_current_mcp_audit_2026-08-26.md` now records the promoted static action and sound references while retaining its pre-promotion MCP receipt and live-acceptance limitation.

4. **The current `override_model = alien_infantry_entity` source edit lacks matching handoff coverage.** The runtime promotion handoff lists the GFX/entity/model/sound files but not `common/scripted_effects/016_alien_infantry_api_effects.txt`. Update the owner handoff so this player-facing model consumer is not an undocumented source patch.

5. **The ownership addendum retains historical source paths.** The current binding spec and acceptance checklist use their real paths; the addendum's historical source list remains evidence-only and must not be used as a current pointer.

6. **Historical asset status should be visibly superseded.** `docs/assets/016_brilliant_scientist/dhrondan_icon_package/manifest.md:44` says the 88 DHR focus sprites were not included because identifiers were unavailable. The later completion handoff proves all 88; the earlier manifest should link to that superseding package so a reader cannot treat the old paragraph as current.

7. **Portrait handoff routing is not explicit.** The asset package is complete, but the handoff records only `/root/dhr_portraits`. Add the custom role name if that path does not already prove `chaosx_portrait_creator` ownership.

### P2 balance and evidence risks

1. Generic laboratory, orbital, diplomacy, and army support focuses rely on inline base weights when omitted from a regime strategy plan. This may be intentional flexibility, but the accepted distinct-AI-priority requirement cannot be quantitatively closed until complete focus histories, route/bypass state, plan activation/abort state, and external factors are supplied to the named probability auditor.

2. Current contact-mission analysis scores both Kruger and Mengele at 10,000 in all three supplied scenarios, producing six extreme-growth warnings from base 1. The source authorization helper remains deterministically Kruger-first if both routes qualify. This may be an intentional route preference, but it is not a balanced stochastic choice and should receive an explicit design disposition before anyone changes the weights.

3. The source audit identified no static contradiction in the DHR flood-fill/component algorithm, Event 019 deferred transaction, or fixed-character Kruger transfer. These are still the most failure-sensitive dynamic paths and should be prioritized over cosmetic polish when adapters/live acceptance become available.

4. The existing workbook `Needs Testing` status is accurate and should not be promoted while these blockers remain.

## MCP evidence and exact limits

This audit attempted the required read-only routes against the current working tree.

- `hoi4.event_inspect` for `chaosx.nr16.40` timed out twice with `tool call failed ... timed out awaiting tools/call after 180s`.
- `hoi4.event_render` for `chaosx.nr16.40` timed out with the same 180-second tools/call limit.
- This audit's `hoi4.focus_inspect` and `hoi4.focus_render` calls for `dhrondan_focus_tree` timed out, but the later shared receipt `016_current_mcp_audit_2026-08-26.md` records a successful current inspect and render with 88 focuses, 102 connectors, zero layout diagnostics, and retained artifacts.
- This audit's `hoi4.tech_inspect` attempt timed out, but the later shared receipt records `TECH_INSPECTED_PARTIAL` and a partial `hoi4.tech_render` with helper projections deferred by the large workspace.

After repeated event adapter timeouts, no responsible `event_compare` could be run because there was no successful fresh current revision/baseline pair. The later `.47` render does not provide that missing comparison baseline, and source diffs are not substituted for MCP comparison evidence.

The later shared receipt provides partial artifacts at revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5` for `chaosx.nr16.47` and `chaosx.nr19.1`, a successful 88-focus inspect/render, a partial Alien Infantry technology inspect/render, and successful exact-window Directorate GUI inspect/render. These artifacts cover only one contact event and the Event 019 root, retain helper and diagnostic truncation limits, and do not provide a current full-chain comparison. They are not treated as engine proof for `.40-.46`, `.48-.52`, the Event 016 root/evolution chain, deferred material conservation, or current model consumers.

The installed inventory exposes no ordinary decision/mission inspect/render/compare route. The map adapter can inspect static states and adjacency but cannot execute the dynamic state-owner/controller/core/capital transaction. The technology adapter has no accepted current before/after baseline. These are exact route limits, not source-level passes.

## Probability audit status

The mandatory weighted pass was routed to `chaosx_ai_probability_auditor`. No files or weights were changed.

| Weighted surface | Current result | Evidence and limit |
| --- | --- | --- |
| Rebellion pulse | Conditional branch weights evidenced; cadence incomplete | Current evaluation of `dhrondan_resolve_rebellion_pulse` found a complete two-entry pool with exact conditional 10/90, 20/80, and 40/60 shares and no unresolved rows. It intentionally warns about 90% no-revolt dominance at the lowest tier. Fresh repeat inspections timed out after 180 seconds, and the artifact does not prove 90-day cumulative probability or recovery timing. Artifact: `probability-ce533f32be4dd0efbce3f9f8`. |
| Kruger, Mengele, and Honor Accord missions | Partial current analysis | Current mission inspection/evaluation (`DHR_CONTACT_MISSION_CURRENT_2026_08_26`) scores both expeditions exactly 10,000 in all three supplied scenarios and ranks Kruger first, Mengele second. Six extreme-modifier-growth warnings cover the base 1 to 10,000 jumps. Honor Accord remains unresolved because its custom tooltip and numeric pact-strain inputs were not supplied. These are scores, not click probabilities. Inspection hash `83639e955d12040e516d539282e627405fa1ef9a8370c01d09157681db61bc0e`; analysis `probability-301c379c5bcb210d3f4b6a53`. |
| Paid landing decision/mission | Incomplete | Decision inspection timed out; discovery found no `decision_ai_will_do` candidate and redirected to the mission surface. Prior partial landing evaluation left target, contact, and equipment inputs unresolved. No target-pool rank, dominance, starvation, or click probability is proved. |
| All 88 DHR focuses | Pool discovered; route behavior incomplete | Current probability inspection includes all 88 candidates at revision `2dbd6a16cb9411764af79b1b0bb5a40cdc7aaf33a895fc4aff3203dfff77fd34`, hash `9bf21fd9611bbde6f0b6717c1ca8a27482b8216993316feda9896d65cca5bbf3`. No candidate can be evaluated without complete external factors and route history/state. Focus scores are a score race, not normalized weight/sum probability. |
| DHR strategy plans and country strategies | Source-only | The adapter discovered no weighted surface for the strategy-factor query. `weight = 1`, preferred 15, urgent 20, and route role ratios remain source-only. Ordered plan influence and reversals are not proved. |
| Diplomatic Event `.49` | Incomplete | The `.49` pool must be isolated from the event file's other categorical pools. Evaluation ended when MCP transport closed. Source gives accept 70/refuse 30, accept multipliers for opinion/democracy, refuse multiplier for low opinion, and no `ai_chance` on `.49.c`; no exact normalized scenario result exists. |
| Event 019 provider 508 | Blocked | `custom_weighted_pool` inspection timed out after 180 seconds and a narrower trigger call returned `Transport closed`. Provider-present, provider-absent, cleanup, candidate selection, and cadence scenarios remain unresolved. |
| Envoy special-project AI | Adapter-unsupported | Source has `ai_will_do` base 100 plus route/operational gates. Probability inspection rejected special-project AI because the adapter accepts event, decision/mission, focus, technology/doctrine, direct-random/random-list, strategy-factor, and custom-pool surfaces only. No project timing/rank claim is made. |

Weighted surfaces without closed named-scenario evidence are paid landing, focus route selection, strategy-plan influence, Event `.49`, provider 508, Honor Accord eligibility, and special-project AI/timing. The exact conditional rebellion branch shares are closed, but cumulative cadence is not. No balance change is authorized from source-only inspection or partial MCP analysis.

Key retained MCP resources from the probability auditor:

- Rebellion evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e6b12c1c58d429149c8cfd862db1eb27fa2828abe9b019d28f7742f5b3bc5d5/4f8da02cda90ddb1005a32456c01c0b3f80491073478574d0c2381ef2d085338/probability-ce533f32be4dd0efbce3f9f8.json`.
- Contact mission inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea7c12998a0f1a2275e033f0a1f90be6f33e60eae31e041ea7aba9c64d4c2dba/b9f26b676c4b23aa7c6b4bbffe5953cd9e427e6d212e236fa2e3b7e38136fd3f/probability-inspect-83639e955d12.json`.
- Contact mission scenario evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64eee18a2659d1f266a284be9271f9931fb4840b67081bebb47202530d40e6bb/9f1134e49fcf839607fa3b0b513632835e88d5969c837961a46b7f02443a78de/probability-301c379c5bcb210d3f4b6a53.json`.
- Current 88-focus structural inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d743b1772bae618bb7dc5a800f0bc33437e627b2d6498ffa983ad3aa97b7154/c9595722a9b9feaec22bf818e2a0c05684fbd3801aec6d35c33205990a68c977/focus-inspect.e751d1b2a47f0b39.json`.
- Current all-88 focus inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0137269cc99049cd200df540e6e704a099850ffaaa91167415f56c0f5e48719/c0123e5598fd23548389eb7422ab517781c00289f0832a1f992544b183eaaed5/probability-inspect-9bf21fd9611b.json`.
- Landing-surface discovery: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ba5df215c4597dc8b93ed286e3ef8a68f9de8030ef0db45a30451759f9c70bb/c77bf302d219c97c7c01d6cd5f37f42bb13ab7f3d5f0bd7df3da6df2dcd64919/probability-inspect-ee65b59c5aeb.json`.
- Event `.49` discovery: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3079874637a8cff279a993a85f894ce665790b956895101e9c80b818d2c0da84/88041f721f1160ae22df30e4c768dc3b1299123753827d21e26699da6b1d5beb/probability-inspect-3450c0c84ae1.json`.

## Asset evidence

### V13 runtime byte reconciliation

Current runtime SHA-256 values match the V13 final manifest:

| Runtime file | SHA-256 |
| --- | --- |
| `alien_infantry.mesh` | `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342` |
| `alien_infantry_idle.anim` | `D6936AE996DBE998DBEE0633B4DCAC346B6C5D974FC643ACA62AAC73719CB2EF` |
| `alien_infantry_move.anim` | `727BCA51B68EEA445198C1029331FF06F15F69215358ABC9CC29A4064096217F` |
| `alien_infantry_laser_attack.anim` | `288209BC4B9CBB3D19A629C2277DF7816CDF33B475EA68BF0D368F7C2E2150F0` |
| `alien_infantry_defend.anim` | `F07A8BC46D68F72DD622014CE31BA9420A3CC1FF419BF3690D44D5F42E9E3A73` |
| `alien_infantry_support_attack.anim` | `DADC3823EA4C2FE5F21F10DAE310F52D54E5379A124C01CDEE3AA954F4EE3061` |
| `alien_infantry_retreat.anim` | `DB9E72F782A19C84A7C4C8CF429654D0BAAAC59A7999B381CA9267DD598BD2DC` |
| `alien_infantry_death.anim` | `D8D26A8B7A6F01ADCB64103885171C837DB36CB7BBB6A6A15EB6C2D66F15D7A0` |

The entity fires laser audio at 4.8 seconds for attack and 1.6333 seconds for support attack, movement at 0/0.6333 seconds, retreat at 0/0.5 seconds, idle on state entry, and death at onset. No particle or light event appears in `gfx/entities/alien_infantry.asset`.

### Sourced audio and counters

The four runtime WAV hashes match the provenance manifest:

| Role | Runtime SHA-256 |
| --- | --- |
| Laser fire | `4E9552C0D023A34BBE816DAD3443E7C4C0C889720C5F5735871F2D7D7682C770` |
| Movement | `E0B36F9B38769ADD16F2569189B7B013749D6F014C37CDB146CD61B060A6A99E` |
| Idle | `B0234598B2DC11635A8713C076A0F6C7E697F29FCA21813EA68922AD38D91C7A` |
| Death | `AFFCE4695B4B493BD2611E591EFA39931BBFAE19E0079D9C77DA5B71D201263B` |

The large counter hash is `5F982AF84059CB980828E5CBE63489AABB13F04A2AABFBC81B9B01038193FC6A`; the on-map counter hash is `775980A00D618DCC675BFD12192F53C11ACAD7380D36B008A69FAA432CBDC07B`.

### DHR 2D package

Current runtime counts are 88 focus DDS files, 11 lifecycle idea DDS files, 12 full portrait DDS files, four DHR flag identities at each size, and the registered decision/project/report/news/equipment/technology/tactic/counter families. The focus GFX file has 88 base and 88 shine registrations. The portrait handoff has twelve full and nine role-card consumers with source/process/runtime hashes.

## Task-specific validation performed

- Read the binding addendum, acceptance checklist, source-of-truth maps, improvement-loop closure, ownership addendum, current API/contact/country/focus/decision/localisation/event-completion/model/icon/portrait/counter/audio handoffs, Event 019 family documentation, and current implementation source.
- Consulted the required offline wiki core pages plus focus, technology, equipment, units, divisions, graphical assets, entities, and country creation. Consulted installed vanilla effects/triggers/script-concept documentation and the exact `units_infantry.asset`, infantry counter, locked-template, event, focus, and special-project precedents.
- Counted exactly 88 DHR focus blocks, 88 inline focus weights, 88 focus DDS files, 11 lifecycle idea DDS files, 12 character definitions, and 12 full DHR portrait DDS files.
- Reconciled the five contact receipts, public API writer/reader scopes, Event 019 provider-508 callbacks, exact landing costs/timing, rebellion thresholds, state transfer, stockpile conservation, ordinary/supplemental cohort formulas, three spirit lifecycles, and four world-order decision consumers.
- Verified the Event 016 CXT extension carrier-to-effect name match, bounded startup scope, tag-scoped daily repair, registered project/equipment/sub-unit tokens, locked non-recruitable template, model override, and processed-token duplicate guard against the shared CXT contract documentation.
- Hashed the current mesh, seven actions, four runtime WAVs, and both counters and matched them to their manifests/handoffs.
- Read the authoritative workbook rather than treating CSV as source. Compared every Event 16 and Event 19 workbook field against the current CSV export; both rows match exactly.
- Attempted the mandatory current MCP event, focus, and technology routes and retained the exact timeout limits instead of substituting source review. Incorporated the named probability auditor's later successful current focus inspect/render, all-88 pool discovery, contact-mission scenario evaluation, and conditional rebellion evaluation together with their unresolved inputs and adapter limits.

No source-only review, bracket check, file count, hash match, or retained historical MCP artifact is presented as live engine proof.

## Recommended parent actions

1. Resolve the V13 muzzle locator through a supported provider/adapter route and bind the existing particle and light at the verified attack/support discharge times. If no supported locator can be produced, retain it as an explicit completion blocker; do not infer a node or bind at origin.

2. Promote the caller-owned landing registry contract and exact cross-country acceptance matrix into the binding spec and acceptance checklist, then execute the matrix when the adapter or user-owned live route is available.

3. Rerun narrow current `event_inspect`/`event_render` for Event 016 root/evolutions, `.40-.47`, `.48-.52`, and Event 019 provider 508; rerun focus and technology inspect/render; create legal MCP before/after revisions and compare every changed surface.

4. Complete the named probability audit with full scenario inputs before changing any weight. If a weight changes, require the owner patch and same-scenario `hoi4.probability_compare` through the auditor.

5. Preserve the current marker consumers and document any future extension against those stable readers. Do not create filler mechanics to consume an already-used flag.

6. Reconcile the V13 runtime state across `alien_infantry.md`, the runtime handoff/crosswalk/sound header, the current MCP audit, the API model-override handoff, the early icon manifest, and the source-of-truth pointers.

7. Add explicit `chaosx_portrait_creator` attribution to the existing DHR portrait handoff if `/root/dhr_portraits` is not already durable role evidence.

8. Preserve workbook status `Needs Testing` and withhold completion until the dynamic state-transfer/transaction scenarios, current MCP comparisons, strict model/audio gates, and user-owned live acceptance close.

## Simplifications, omissions, and blockers

This read-only audit introduced no fallback, balance change, gameplay simplification, asset substitution, or source patch.

Existing unresolved items are explicit: unbound muzzle particle/light, incomplete strict audio-role breadth, unproved registry acceptance scenarios, incomplete probability evidence, unavailable current MCP comparisons, ambiguous portrait-role attribution, and no live acceptance.

The unused DHR art candidates, absence of a DHR super-event, absence of a dedicated DHR scripted GUI, exactly four evolutions, the fifteen ordinary-cohort cap with separately recorded supplemental enclave cohorts, and reuse of genuine idle/defend animations for non-required training/wounded entity states are intentional dispositions rather than hidden simplifications.

No commit was created.
