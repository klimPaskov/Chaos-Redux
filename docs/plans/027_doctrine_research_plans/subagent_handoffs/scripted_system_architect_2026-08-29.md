# Event 027 scripted-system architecture audit

> **Superseded status notice (2026-09-01):** This pre-rework architecture audit is preserved as historical evidence and is superseded as a current status authority by ../documentation_state.md. Its proposed exclusion of Event 027 or Chaos from the default allowlist predates the current source.

Date: 2026-08-29

Scope: read-only architecture review for the Event 027 Doctrine Research rework.

Owner boundary: this handoff proposes scripted interfaces, data layout, lifecycle handling, and validation. The parent agent owns gameplay implementation and wiring.

Repository status at audit time: the worktree contained many pre-existing parent changes, including an existing Event 027 plan directory and probability_baseline_2026-08-29.md. This handoff was the only requested file added by this audit. No gameplay file was edited.

## Executive conclusion

Event 027 should use an Event 027-owned adapter registry plus country-owned batch and receipt state. The registry should dispatch only to statically declared, validated adapters for Army, Navy, Air, Special Forces, Chaos Warfare, and later custom domains. An invalid custom row must be hidden without disabling valid ordinary rows, and an unknown or malformed domain must never fall back to Army.

The exact mastery operation is the gating issue. Vanilla documents add_mastery as a mastery-point mutation and has_mastery_level as a threshold predicate, but the installed official dynamic-variable documentation does not expose a direct fractional mastery read or a direct exact-one-level mutation. The implementation must therefore expose a mastery option only when an adapter can prove the postcondition post_level = pre_level + 1 without spending or overwriting banked mastery. A threshold-sized add_mastery grant is not a safe substitute because branch reward thresholds differ and fractional banked progress can spill into another level.

Grand Doctrine adoption can remain a separate transaction that consumes one Event 027 choice and grants no Event 027 mastery step. Track and empty-track mastery actions remain hidden or unresolved until the adapter's exact-step capability is proven. Chaos Warfare must enter through the native doctrine and subdoctrine effects so its adoption flags, track identities, mastery flags, downstream gates, and AI state remain authoritative.

## Evidence reviewed

| Surface | Evidence | Architecture consequence |
| --- | --- | --- |
| Current Event 027 | events\027_doctrine_research.txt:22-111 defines chaosx.nr27.1 and .2, selects a random major or human country, and exposes only four land Grand Doctrine options with ai_chance = { base = 25 }. | The existing popup cannot be extended by adding a few options. It needs a repeatable batch continuation path and an adapter-owned candidate pool. |
| Event registration | common\scripted_effects\chaosx_logic_effects.txt:235-286 puts event 27 in global.fire_once_events and builds global.all_events by concatenating major, fire-once, and repeatable arrays at :328-347. | The parent must move event 27 to the repeatable list and preserve the shared automatic selector instead of adding a second world pulse. |
| Event dispatch | common\on_actions\chaosx_on_actions_system.txt:132-165 routes the existing automatic selector through the shared event pool. common\scripted_effects\chaosx_settings_effects.txt:4329-4442 contains the weighted selector. | Event 027 automatic timing and domain-choice scoring are separate surfaces. Do not treat old option scores as event timing probabilities. |
| Shared dynamic helpers | common\scripted_effects\chaosx_dynamic_effects.txt:1-6 reserves the file for neutral cross-system helpers and keeps event-owned orchestration and one-off adapters in the owning file. :448-496 demonstrates token-valued array iteration and guarded application. | Keep the doctrine registry and transaction private to Event 027 unless a helper is genuinely neutral and has another caller. Do not create a central MCP or script router. |
| Parallel-array registry pattern | common\scripted_effects\006_independence_wave_effects.txt:857-890 commits only after flags and aligned arrays validate. :981-1040 finds rows by country and generation, appends all parallel fields together, and writes the row by index. common\scripted_triggers\006_independence_wave_triggers.txt:479-532 checks array alignment. | Store queue and receipt records in parallel arrays with an alignment trigger. Never emulate nested records with unpaired arrays. |
| Atomic transaction pattern | common\scripted_effects\civilian_transfer_effects.txt:1018-1103 runs preflight, exact mutation, receipt/finalize, rollback on failed finalization, and cleanup. common\scripted_effects\migration_spontaneous_movement_effects.txt:224-324 stages an attempt, binds targets, validates, and aborts staged state on failure. | Event 027 needs prepare, mutate, reconcile, and terminal-cleanup phases, but doctrine effects are not known to be reversible, so ambiguous mastery must quarantine rather than guess or roll back. |
| Event-target guidance | paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:254-311 distinguishes regular targets, which survive the current event chain and clear automatically, from global targets, which persist until explicitly cleared. | Use regular targets only for a live event chain. Persist batch ownership and receipts as country variables and arrays, not as event-target pointers. |
| Array and variable guidance | paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:410-422 describes scoped regular variables versus unscoped temporary variables. :817-824 defines zero-based persistent regular arrays and temporary arrays. | Queue and receipt state must be regular country arrays. Temporary variables are only for one adapter call or one page rebuild. |
| CXT contract | docs\testing\chaosx_test_country.md:69-105 documents package-owned setup effects for surfaces with no native runtime database array. common\scripted_effects\chaosx_test_country_effects.txt:207-245 registers hidden-idea carriers through a guarded global array and dispatches their _apply effects. common\on_actions\chaosx_test_country_on_actions.txt:4-31 and common\on_actions\016_alien_infantry_cxt_on_actions.txt:4-29 show bounded startup registration plus tag-scoped on_daily_CXT repair. | CXT is a test setup bus, not the runtime doctrine adapter registry. If Event 027 adds a new test-only doctrine or system fixture, use a modifier-free carrier, idempotent _apply effect, bounded startup registration, and daily repair. Do not use CXT to route live Event 027 choices. |
| Native folder gates | C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\doctrines\folders\doctrine_folders.txt:1-50 makes land, naval, and air always allowed. special_forces at :37-50 requires either the No Compromise, No Surrender or Arms Against Tyranny DLC. | Folder existence is not enough for adapter eligibility. The row must also evaluate the selected Grand Doctrine and branch availability blocks. |
| Native Grand Doctrine topology | C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\doctrines\grand_doctrines\land_grand_doctrines.txt:1-386 defines four land doctrines and their track order. sea_grand_doctrines.txt:1-248 defines three naval doctrines. air_grand_doctrines.txt:1-248 defines three air doctrines. special_forces_grand_doctrines.txt:1-119 defines two Special Forces doctrines. | Preserve the track order declared by each Grand Doctrine. Do not use the order of separate track definition files as a substitute. |
| Native Special Forces graph | C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\doctrines\tracks\special_forces_tracks.txt:16-31 gives special_forces_second the active gate can_unlock_second_track_of_sf_doctrine = yes. C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\doctrines\subdoctrines\special_forces\special_forces_subdoctrines.txt:1-10 and later branch blocks use both Special Forces tracks and mutual exclusions. | Special Forces needs its own adapter. It must not be translated to Army mastery, and its second track must be omitted when the native active gate fails. |
| Native mastery effects | Official docs C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:1477-1502 describe add_mastery and its folder, Grand Doctrine, subdoctrine, track, and zero-based index filters. :7094-7105 documents set_grand_doctrine. :7774-7802 documents set_sub_doctrine and warns that an explicit track index is among all tracks in the folder. | Every mutation must identify folder, Grand Doctrine, subdoctrine, track, and index where applicable. A variable-valued doctrine token requires a proven static dispatch or meta_effect; arbitrary callback names must not be constructed from untrusted text. |
| Native mastery queries | Official docs C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:4163-4195 document has_mastery and has_mastery_level. :4843-4855 documents has_subdoctrine_in_track. :3526-3553 documents completion checks. | Integer level can be reconstructed with ordered has_mastery_level probes when the adapter knows the branch maximum. Fractional points and the amount needed to land on exactly the next level remain unproven. |
| Dynamic doctrine value documentation | C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md:455-457 lists land_doctrine_level as an auto-generated value based on the same-named trigger. No relevant fractional mastery value is listed in the installed document. | Do not invent land_doctrine_mastery, a current-point variable, or a writable level field. Treat fractional mastery read support as an adapter capability that requires engine evidence. |
| Chaos Warfare Grand Doctrine | common\doctrines\grand_doctrines\chaos_warfare_grand_doctrine.txt:31-42 places chaos_warfare in the land folder, uses the CBRN adoption gate, and uses Army XP. :88-123 declares ordered tracks infantry, combat_support, armor, operations and native milestone callbacks. | Chaos is a separate domain despite sharing the land folder. The ordinary Army allowlist must explicitly exclude chaos_warfare. |
| Chaos Warfare gates | common\scripted_triggers\cbrn_doctrine_triggers.txt:12-70 defines agent, chemical-project, historical-profile, adoption, and AI viability gates. :239-340 defines track-level and institutional milestones. :342-418 defines downstream technology gates. | Event 027 may waive doctrine purchase cost, but it must not waive the owning system's equipment, formation, policy, readiness, technology, project, or operational requirements. |
| Chaos Warfare transitions | common\scripted_effects\cbrn_doctrine_effects.txt:75-100 initializes adoption state. :374-496 records branch adoption and mastery-level flags, unlocks, and technology grants. :573-707 is a separate legacy migration path. | Use native set_grand_doctrine and set_sub_doctrine so definition-owned effects run. Do not call the migration effect or duplicate its flag and technology grants from Event 027. |
| Branch-specific thresholds | Chaos branches use the owner constant CBRN_*_REWARD_THRESHOLD in common\doctrines\subdoctrines\land\chaos_warfare_*_subdoctrines.txt, for example infantry :112-114 and armor :104-106. Native Special Forces uses mastery = 60, for example special_forces_subdoctrines.txt:55 and :197. A land branch also contains an explicit mastery = 50, for example land\infantry_subdoctrines.txt:773. | Never centralize a universal mastery-point grant. Each adapter must own or prove its branch threshold table. |
| Existing Event 016 integration | common\scripted_effects\016_brilliant_scientist_context_effects.txt:595-622 records the doctrine-research result behind country and character one-time guards. docs\events\016_brilliant_scientist\overview.md:27 treats Event 027 as the external research posture source. | Preserve the hook on a successful Event 027 result, but invoke it at most once per existing identity guard. Do not let repeated mastery pages create repeated Scientist receipts. |

## MCP and weighted-logic evidence status

The installed callable tool inventory did not expose hoi4.event_inspect, hoi4.tech_inspect, hoi4.tech_render, hoi4.probability_inspect, hoi4.probability_evaluate, hoi4.probability_sweep, hoi4.probability_compare, hoi4.probability_render, hoi4.probability_simulate, or hoi4.probability_sequence.

The weighted-logic auditor route was dispatched to agent 01a04e48-074b-74c3-864a-b812735475e1 with fork_context=false and returned the same unavailable-route result.

The required chaosx_ai_probability_auditor completed a read-only source audit and confirmed that no MCP probability or doctrine artifacts, revisions, scenario hashes, comparison IDs, or rendered evidence exist. It found the current four base = 25 options, the fire-once registration, and no Event 027 track, branch, batch, or cluster implementation. Scenarios DR-A01 through DR-G03 remain unresolved.

This source review is not engine evidence. The parent must not claim normalized probabilities, timing distributions, dominance, starvation, rank reversals, DLC behavior, or sequence outcomes until the required MCP routes become callable. Any AI-weight patch requires the same named baseline and hoi4.probability_compare pass after implementation.

## Proposed registry architecture

### Ownership and dispatch rule

The registry should live beside Event 027 in an owner file such as common\scripted_effects\027_doctrine_research_registry_effects.txt, with matching owner triggers and documentation. The names are proposed interfaces, not new files created by this audit.

HOI4 script does not provide a proven safe way to call an arbitrary scripted effect by a token stored in an array. Store a numeric dispatch_id in the registry and use explicit static if or else_if dispatch to the known adapter effects. meta_effect may inject a proven data token into a static effect such as set_grand_doctrine or add_mastery; it must not turn an unvalidated registry string into an executable callback.

Future custom domains extend the registry by adding a stable row and a static dispatch branch. Runtime discovery from a text name alone is not part of the contract.

### Stable domain rows

The following IDs are proposed for common\script_constants\027_doctrine_research_constants.txt. They are architecture IDs, not native doctrine IDs.

| Domain ID | Domain | Native folder | Baseline status | Notes |
| --- | --- | --- | --- | --- |
| event_027_domain.invalid = 0 | Invalid | None | Always disabled | Used for failed dispatch and malformed saved rows. |
| event_027_domain.army = 1 | Army | land | Required | Allowlist only new_mobile_warfare, superior_firepower, grand_battleplan, and mass_assault; exclude chaos_warfare. |
| event_027_domain.navy = 2 | Navy | naval | Required | Use the three native naval Grand Doctrines and each doctrine's declared track order. |
| event_027_domain.air = 3 | Air | air | Required | Use the three native air Grand Doctrines and each doctrine's declared track order. |
| event_027_domain.special_forces = 4 | Special Forces | special_forces | Conditional | Enable only when DLC, native Grand Doctrine availability, branch topology, icons, AI factors, and exact-step support are proven. |
| event_027_domain.chaos_warfare = 5 | Chaos Warfare | land | Required custom domain | Use only chaos_warfare and the four CBRN compatibility identities. |
| event_027_domain.custom_start = 100 | Future custom range marker | Owner-defined | Extension point | A custom row must still provide every contract field and a static dispatch branch. |

Every row should carry a separate dispatch_id, contract version, display key, icon key, native folder token, feature-gate selector, AI-factor selector, cleanup selector, and per-operation capability bits. Domain IDs must remain stable when display text or callback implementation changes.

### Adapter registry fields

Use a small set of aligned global arrays for registry metadata, for example:

    global.event_027_registry_domain_ids
    global.event_027_registry_dispatch_ids
    global.event_027_registry_contract_versions
    global.event_027_registry_orders
    global.event_027_registry_enabled
    global.event_027_registry_feature_states
    global.event_027_registry_one_step_capable
    global.event_027_registry_display_keys
    global.event_027_registry_icon_keys
    global.event_027_registry_folder_tokens
    global.event_027_registry_ai_selectors
    global.event_027_registry_cleanup_selectors

Do not store a variable number of Grand Doctrine or track rows inside one array element. Each adapter owns its static candidate allowlists and appends the currently valid candidates to temporary country-scope pools for the current page or AI decision.

The registry validator must prove the following before setting a row enabled:

1. The domain ID is unique and not invalid.
2. The dispatch selector, contract version, display identity, feature gate, cleanup selector, and AI selector are present.
3. Every Grand Doctrine candidate belongs to the declared folder and has a stable static dispatch path.
4. Each candidate Grand Doctrine has a usable ordered track list, and duplicate track identities have explicit indices.
5. Every selected branch has a valid empty-track selector, current-branch reader, maximum-level reader, completion reader, and mutation capability.
6. one_step_capable is true only after the adapter has a proven exact postcondition method.
7. All required owner gates pass through the owner trigger or native availability equivalent.
8. The row's aligned arrays still have equal lengths.

If one row fails, set only that row invalid and retain other valid rows. If the registry cannot prove the required baseline row itself, Event 027 may close without a doctrine mutation; it must not select a substitute domain.

### Domain adapters

#### Army

The Army adapter uses the land folder and the four ordinary land Grand Doctrines. The current land Grand Doctrines all declare the ordered tracks infantry, combat_support, armor, and operations.

The adapter must exclude chaos_warfare explicitly because Chaos uses the same folder and track identities. A broad folder = land query would otherwise mix ordinary and Chaos branches.

#### Navy

The Navy adapter uses naval, new_fleet_in_being, new_convoy_raiding, and new_base_strike. The track order must be read from each Grand Doctrine declaration, currently submarines, screens, carriers, and capital_ships.

A human country does not need a current fleet or coastline when the native doctrine system permits adoption. AI domain factors may strongly reduce a maritime choice for a landlocked country, but the human adapter must not invent a new availability gate.

#### Air

The Air adapter uses air, new_strategic_destruction, new_battlefield_support, and new_operational_integrity. The current track order is fighter_aircraft, strike_aircraft, medium_aircraft, and heavy_aircraft.

AI factors should call or reuse existing air-production, wing, mission, airbase, enemy, and route signals when available. A fixed major-country bonus is not a sufficient Event 027 domain score.

#### Special Forces

Special Forces is source-verified as a distinct doctrine folder, not as an Army extension. The folder requires either No Compromise, No Surrender or Arms Against Tyranny. Both Special Forces Grand Doctrines require at least one of tech_mountaineers, marines, paratroopers, or rangers_tech.

The current Grand Doctrine track list is special_forces_first, special_forces_second. The second track's native active gate is can_unlock_second_track_of_sf_doctrine = yes. Native Special Forces branches list both tracks and use mutual exclusions, so the empty-track adapter must pass the intended track index explicitly and let native branch availability decide the valid branch pool.

Special Forces reward thresholds are not the ordinary 100-point assumption; the inspected branch uses mastery = 60. The adapter therefore needs its own threshold and maximum-level contract. It must remain hidden if exact one-step support, branch topology, AI factors, or the installed DLC graph is not proven through the unavailable MCP route.

#### Chaos Warfare

Chaos is a separate domain even though its Grand Doctrine is in land. The public-to-native track mapping is:

| Public identity | Native subdoctrine | Native track |
| --- | --- | --- |
| Hazard Assault Formations | extermination_columns | infantry |
| Toxic Armored Warfare | chemical_suppression | armor |
| Contaminant Fire Support | contaminant_firebases | combat_support |
| Integrated CBRN Command | integrated_chemical_operations | operations |

Chaos Grand Doctrine adoption must use the native chaos_warfare availability equivalent, which currently calls cbrn_chaos_warfare_adoption_capable. That gate includes gas-mask and agent technology, completed chemical projects, established command, historical program profile, and scenario override paths.

Chaos AI participation must additionally respect cbrn_chaos_warfare_ai_has_viable_program, which excludes actual nonhuman countries and requires a viable military, industrial, enemy-use, profile, or route signal. The Event 027 AI adapter should call this owner trigger rather than copying its state table.

Chaos branch adoption must use native set_sub_doctrine so the branch-owned effects record cbrn_*_track_active and other owner state. Native mastery reward effects must remain the source of CBRN flags, unlocks, and available technology grants. Event 027 must not call cbrn_migrate_legacy_chaos_warfare, manually set mastery flags, grant a downstream unit, or turn an event step into a policy, equipment, formation, operation, or technology shortcut.

The adapter should expose downstream state as read-only eligibility context. For example, cbrn_can_claim_delivery_integration requires the protective foundation, a delivery-track mastery threshold, operational payload, and a protected order; cbrn_can_claim_theater_exploitation requires two tracks at mastery three, decontamination capacity, and an intelligence/weather cell; cbrn_can_claim_terminal_command requires all four tracks active, a mastery-five track, the policy floor, and advanced protection. These remain owner-system gates after Event 027 succeeds.

#### Future custom domains

A custom owner must provide an explicit row, static dispatch path, stable domain identity, native or owner-specific Grand Doctrine and track selectors, branch pool, integer and fractional mastery semantics, exact one-step proof, AI factors, DLC gate, icons, cleanup, and scenario coverage.

The row is invalid if any required field is missing. A custom owner must not borrow the Army adapter merely because its doctrine is in the land folder.

## Proposed helper map

The names below are pseudo-interfaces for parent implementation. They describe scope, inputs, outputs, side effects, and call sites; they are not gameplay changes made by this audit.

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| event_027_registry_initialize | Global | Schema version and static row declarations | Rebuilt aligned registry arrays and schema status | Clears and rebuilds only registry metadata; no country doctrine mutation | Existing Event 027/event-system initialization path. |
| event_027_registry_validate | Global | Registry arrays | Per-row valid flag, invalid reason, baseline status | None beyond validation state | Immediately after initialization and before a pool build if schema is stale. |
| event_027_registry_dispatch | Country | event_027_domain_id, operation selector, operation inputs | Operation result and adapter reason | Calls one statically known owner adapter | Every domain, Grand Doctrine, track, branch, AI, and cleanup operation. Unknown IDs return invalid. |
| event_027_adapter_build_domain_pool | Country | Batch row and current country state | Temporary aligned domain IDs, display keys, icons, action kinds | None | Event opening, every human page, every AI choice. |
| event_027_adapter_build_grand_pool | Country | Domain ID | Temporary eligible Grand Doctrine IDs and static dispatch IDs | None | Domain page when no Grand Doctrine is active. |
| event_027_adapter_build_track_pool | Country | Domain ID, active Grand Doctrine | Temporary ordered tracks with indices and selected branch state | None | Domain page when a Grand Doctrine is active. |
| event_027_adapter_build_empty_branch_pool | Country | Domain ID, Grand Doctrine ID, track ID, folder index | Temporary eligible subdoctrine IDs and display values | None | Empty-track page and AI branch selection. |
| event_027_adapter_read_state | Country | Domain ID, Grand Doctrine ID, track ID, subdoctrine ID | Current level, maximum level, selected state, track completion, native milestone state, read-capability bits | None | Pool construction, preflight, post-mutation reconciliation, recovery. |
| event_027_adapter_adopt_grand_doctrine | Country | Domain ID, one static Grand Doctrine dispatch ID | Mutation result and post-adoption identity | Calls native set_grand_doctrine through static dispatch | One Grand Doctrine adoption transaction. |
| event_027_adapter_adopt_subdoctrine | Country | Domain ID, subdoctrine ID, folder, explicit folder track index | Mutation result and post-adoption branch identity | Calls native set_sub_doctrine through static dispatch; owner branch effect may initialize state | Empty-track transaction before any mastery step. |
| event_027_adapter_prepare_exact_step | Country | Domain ID, branch identity, pre-state, receipt ID | Exact-step capability result and planned native action | None; no mastery mutation | Transaction preflight. |
| event_027_adapter_apply_exact_step | Country | Prepared receipt and exact native action | Mutation result, post-read request, step result | Calls the proven native or owner-specific mastery action once | Mastery transaction mutation phase. |
| event_027_adapter_reconcile_step | Country | Receipt ID, pre-state, post-state | applied, not_applied, ambiguous, or invalid | May run only owner-approved idempotent reconciliation; never duplicates rewards by default | After mutation and save/reload recovery. |
| event_027_adapter_score_ai | Country | Domain, Grand Doctrine, track, branch, current state | Nonnegative factor and hard-validity result | None | Same pool used by AI resolution and probability audit. |
| event_027_cleanup_country | Country | Cleanup reason and optional batch ID | Cleanup result | Marks abandoned rows and removes pending receipts; never transfers doctrine or CBRN state | Narrow annexation/terminal hooks and invalid-owner recovery. |
| event_027_cxt_register_test_fixture | Country | CXT harness state only | Registration-added result | Registers a hidden-idea carrier through the CXT bus if a dedicated test fixture is later required | Bounded startup and on_daily_CXT, not live Event 027 execution. |

The adapter interface should return temporary values from a caller-provided temporary context. It should not write permanent country variables while merely building a page or an AI score.

## Exact-one mastery transaction

### Durable data model

The batch is owned by the country, not by a global event target. Use parallel regular country arrays with one active-row index and ordered queued rows. A proposed row has:

    event_027_batch_ids
    event_027_batch_evolution_stages
    event_027_batch_total_choices
    event_027_batch_remaining_choices
    event_027_batch_statuses
    event_027_batch_owner_epochs
    event_027_batch_open_dates
    event_027_batch_active_row

The receipt ledger is also country-scoped and parallel. A proposed receipt row has:

    event_027_receipt_ids
    event_027_receipt_batch_ids
    event_027_receipt_ordinals
    event_027_receipt_states
    event_027_receipt_action_kinds
    event_027_receipt_domain_ids
    event_027_receipt_grand_doctrine_ids
    event_027_receipt_folder_tokens
    event_027_receipt_track_ids
    event_027_receipt_track_indices
    event_027_receipt_subdoctrine_ids
    event_027_receipt_pre_levels
    event_027_receipt_post_levels
    event_027_receipt_owner_epochs

A scalar global event_027_next_batch_id or event_027_next_receipt_id may supply uniqueness. It must be initialized idempotently and never be used as a country owner pointer. If Event Details or achievements need a global historical index, append immutable IDs and tokens to separate aligned history arrays; do not store live event-target pointers in that history.

Use flags for booleans such as event_027_transaction_inflight and event_027_has_active_batch. Use numeric variables only for IDs, indices, counts, stages, and explicit result enums.

A batch ID plus receipt ordinal identifies one choice. The receipt state should distinguish at least prepared, effect_applied, choice_consumed, ambiguous, invalid, and abandoned.

### Transaction phases

1. Revalidate the country, active batch row, remaining-choice count, registry row, current domain, target Grand Doctrine, target track, selected branch, and owner epoch.
2. Rebuild the candidate pool immediately before mutation. A page opened earlier is not authoritative.
3. Read and store the pre-state, including selected identities, integer level, maximum level, completion state, and all owner-specific proof fields that the adapter requires.
4. Allocate a receipt ID and append a prepared receipt before the native mutation. Bind it to the batch ID, receipt ordinal, domain ID, Grand Doctrine ID, folder, track, explicit index, branch, pre-level, and owner epoch.
5. For Grand Doctrine adoption, call the native set_grand_doctrine action once. For empty tracks, call native set_sub_doctrine first and re-read the branch before planning mastery. For active branches, skip adoption and re-read the selected branch.
6. Apply one exact mastery action only when the adapter capability bit is true. The action must target the selected folder, Grand Doctrine, subdoctrine, track, and explicit index so a shared land track cannot absorb another domain's progress.
7. Re-read the post-state through the adapter. The expected mastery result is exactly one level beyond the post-bank-settlement baseline, not merely a positive has_mastery result.
8. Mark the receipt effect_applied only after the postcondition proves the intended action. Then decrement the batch's remaining choice count exactly once and mark the receipt choice_consumed.
9. Rebuild the pool for the next choice. If no valid action remains, close the batch without compensation. If more choices remain, continue through the human page or the bounded AI continuation path.

The choice decrement must never happen before the receipt is proven applied. Reopening a page, clicking back, firing a duplicate child event, or resolving the same country after reload must find the existing receipt and refuse to repeat the native effect.

### Grand Doctrine adoption

Adoption is a separate action kind. It must prove that the domain has no active Grand Doctrine, the selected Grand Doctrine exists and is currently available, the action does not replace progress, and the post-state reports the selected identity. It consumes one choice and grants no Event 027 mastery step.

The Chaos adapter must use the native set_grand_doctrine = chaos_warfare transition through a static dispatch path. A successful result must verify the expected CBRN adoption flags or native state without manually replaying cbrn_chaos_warfare_adopt.

### Active-track mastery

For an active branch, the adapter must first read the integer level and determine that it is below the branch maximum. It must then prove how much native fractional mastery is already banked or prove that a native exact-one-level action exists.

A threshold-sized add_mastery call is not sufficient. add_mastery accepts a point amount and can spill through a reward threshold when fractional progress is already present. The branch threshold can be 60, 50, 100, or another owner-defined value. A post-read that discovers two levels after the mutation is too late to make the action exact, and doctrine effects are not known to be reversible.

### Empty-track mastery and banked mastery

An empty track follows this order:

1. Validate and select one eligible branch through the native or owner-specific transition.
2. Re-read the branch after native banked mastery resolves.
3. Preserve every level and every fractional remainder produced by native banked mastery.
4. If the branch is complete because of the bank alone, return to the pool without consuming the Event 027 mastery choice unless a verified combined transaction proves an additional event step.
5. If another level remains, apply one exact Event 027 step only if the adapter can distinguish the bank-settlement baseline from the event increment.
6. Consume the choice only after the postcondition proves exactly one event step beyond the bank-settlement baseline.

If the engine exposes no fractional read and no exact one-step effect, the empty track is not a valid Event 027 mastery option. Selecting a branch and then granting a generic threshold amount would violate the bank-preservation requirement.

### Save/reload recovery

The receipt is a durable two-phase record, not a temporary flag.

| Recovered state | Recovery action |
| --- | --- |
| prepared and exact pre-state still holds | Retry the same prepared action only if the adapter can prove no native mutation occurred. |
| prepared or effect_applied and exact post-state holds | Mark effect_applied, consume the choice once if not already consumed, and never re-run the native effect. |
| choice_consumed | Treat as terminal and rebuild the next pool. |
| Expected identity changed, level changed by an external source, or post-state is greater than one event step | Mark ambiguous, do not consume, do not retry, and retain evidence for owner review. |
| Country or owner epoch is gone | Mark the row abandoned or clear it in the narrow lifecycle hook; never transfer it to an annexer, overlord, civil-war side, or liberator. |

There is no safe generic rollback for set_grand_doctrine, set_sub_doctrine, or add_mastery. Recovery should stop on ambiguity instead of attempting to subtract mastery or reconstruct owner flags.

## Event targets, queue cleanup, and country identity

Use regular save_event_target_as only for a current Event 027 chain, such as carrying the country or a selected state into an immediate child event. Guard every use with has_event_target. Regular targets automatically clear after the originating chain; this matches the wiki and avoids orphan pointers.

Do not store the batch owner as a global event target. A global pointer would outlive the chain and would require manual clearing after annexation, invalidation, completion, and every terminal error. The country owns its own queue and receipt arrays.

Use narrow existing lifecycle boundaries rather than a new whole-world cleanup action:

| Lifecycle | Current repository pattern | Event 027 behavior |
| --- | --- | --- |
| Annexation | common\on_actions\006_independence_wave_on_actions_registry.txt:65-82 documents FROM as the annexed country and cleans it before removal. | In on_annex, clean pending Event 027 batches and receipts on FROM. Do not transfer them. Preserve only immutable historical records if an achievement contract requires them. |
| Puppet or subject change | The same file uses narrow on_puppet and release callbacks at :84-103; chaosx_on_actions_chaos_meter.txt:126-170 shows existing subject callbacks. | Preserve the country's queue. A subject change changes control context, not batch ownership. Rebuild human/AI routing for the current controller. |
| Release or independence | 006_independence_wave_on_actions_registry.txt:47-59 touches both affected scopes. | Preserve the existing country's queue and never manufacture a second batch on the released or overlord scope. |
| Capitulation | 006_independence_wave_on_actions_registry.txt:95-103 uses a narrow capitulation callback. | Preserve the batch and let the current controller resolve it through the same pool. Capitulation is not annexation. |
| State controller change | common\on_actions\chaosx_on_actions.txt:23-49 documents ROOT as new controller, FROM as old controller, and FROM.FROM as the state. | Do not attach Event 027 cleanup to a controller change because the doctrine batch has no state owner. Controller change is not country identity change. |
| Cosmetic tag change | Event 027 specification docs\specs\027_doctrine_research_specs\027_doctrine_research_spec_part_2_choice_flow.md:384-395 requires preservation. | Keep state on the country scope. Do not key live ownership only by display tag or original_tag. |
| Civil war or dynamic country | The specification at docs\specs\027_doctrine_research_specs\027_doctrine_research_spec_part_1_core.md:82-94 requires the original scope to retain a valid batch and the new side to receive no retroactive batch. | Use an owner epoch and a narrow civil-war/new-country proof if the engine provides one. If clone semantics cannot be proven, quarantine a copied receipt rather than applying it to the new scope. |

The current repository commonly pairs stable IDs with generation values, as in Event 006's host ledger and the migration receipts. Reuse that principle for batch and receipt identity. Do not invent an unavailable country-ID getter. If no engine-supported identity proof distinguishes a cloned country after a civil war, record the limitation and fail closed for that row.

## CXT integration boundary

The CXT contract is relevant only if the rework adds a new definition or system that needs a test-country fixture. The documented pattern is:

1. Add a modifier-free hidden idea whose ID is the package carrier.
2. Add an idempotent package setup effect named exactly <carrier>_apply.
3. Have a package wrapper place token:<carrier> in chaosx_test_country_registration_extension_effect and call chaosx_test_country_register_extension_effect.
4. Register the wrapper from a bounded existing-country on_startup scope.
5. Retain a guarded on_daily_CXT wrapper because on_startup does not repair a loaded save.
6. Use on_weekly_CXT only for recurring maintenance not already owned by the daily hook.

The CXT dispatcher resolves the carrier token to a static _apply effect through meta_effect, and each package effect guards its direct changes with a stable flag or current definition state. This is a useful precedent for idempotent setup and token safety, but it must not be copied as the live Event 027 callback router. The doctrine registry needs domain and operation validation at every call, whereas CXT registers test setup packages once and then repairs them.

No CXT gameplay or setup file was changed by this audit.

## Constants and tuning plan

The parent should add an Event 027 owner constants file such as common\script_constants\027_doctrine_research_constants.txt. Keep native doctrine thresholds in their owner definitions or an adapter-specific table; do not duplicate them as a universal Event 027 threshold.

| Constant category | Proposed contents | Constraint |
| --- | --- | --- |
| Schema | Registry contract version and schema version | Enables save/load migration and duplicate-registration prevention. |
| Domain IDs | Invalid, Army, Navy, Air, Special Forces, Chaos, custom-range marker | Stable architecture IDs; never use display text. |
| Registry status | Valid, invalid, feature-gated, unsupported, stale | Invalid rows hide without affecting other rows. |
| Batch stages | Opening, domain, Grand Doctrine, track, empty branch, AI continuation, closed, abandoned | Stage is persisted per batch. |
| Receipt states | Prepared, effect applied, choice consumed, ambiguous, invalid, abandoned | Receipt state is persisted per country. |
| Action kinds | Grand Doctrine adoption, active-track step, empty-track step | Adoption must remain distinct from mastery. |
| Evolution sizes | Baseline one choice through the accepted five-choice ceiling | Snapshot the resolved size into the batch. |
| Index sentinels | Invalid index and first array index | Avoid magic index values in dispatch and cleanup. |
| Transaction results | Invalid, adopted without mastery, step applied, no step, ambiguous | Localisation can distinguish navigation, no-op, and consumed results. |
| Capability bits | Exact fractional read, exact one-step action, safe bank settlement, native reward reconciliation | A missing bit removes the mastery action from the pool. |
| Chaos constants | Existing CBRN owner constants only | Do not copy CBRN thresholds, gates, or route factors into generic Event 027 constants. |

Use constant:<category>.<key> where the effect or trigger accepts script constants. If a duration field rejects constants, follow the repository's existing temporary-variable bridge. This rework has no reason to introduce duration magic numbers into native mastery effects.

## Migration plan

1. Remove event 27 from the fire-once registration and add it to the repeatable event registration. Keep chaosx.nr27.1 as the root ID so existing event identity and logs remain stable.
2. Add the registry schema and static rows for ordinary Army, Navy, Air, conditional Special Forces, and Chaos. Validate rows before exposing any option.
3. Migrate ordinary Army adoption first and compare its post-state to the old four-option behavior. Explicitly exclude Chaos from that allowlist.
4. Add Navy and Air using their Grand Doctrine-declared track orders and owner availability blocks.
5. Add Special Forces only after the DLC, second-track active gate, branch topology, and exact-step capability are all proven. Do not use an Army fallback for an unproven SF graph.
6. Add Chaos through the native Grand Doctrine and subdoctrine transition. Preserve brilliant_scientist_record_doctrine_research behind its existing one-time guards and do not call the CBRN legacy migration effect.
7. Replace the fixed .2 popup with the batch opening, domain, adoption, track, branch, confirmation/reconciliation, and continuation events required by the accepted specification. Keep human and AI resolution on the same candidate builders and transaction wrapper.
8. Add country-owned parallel queue and receipt arrays, alignment triggers, save/reload recovery, and narrow lifecycle cleanup. Existing batches must not be overwritten when another repeatable firing appends a new batch.
9. Add AI factor callbacks after baseline probability inspection. Do not reuse the four equal ai_chance values as final domain, doctrine, track, branch, or allocation weights.
10. Add any CXT fixture only if the implementation introduces a new definition or system that needs one. Keep CXT registration separate from runtime Event 027 dispatch.
11. Update Event 027 documentation, event log/details integration, localisation, spreadsheet alignment, and acceptance records after gameplay implementation. This audit intentionally does not edit those surfaces.

## Validation plan for the parent

### Source validation already completed

- Current Event 027 source and event registration were inspected.
- Native land, naval, air, and Special Forces Grand Doctrine definitions and track order were inspected.
- The Special Forces DLC folder gate and second-track active gate were inspected.
- Chaos Warfare adoption, AI, mastery, milestone, downstream, identity, and owner-effect surfaces were inspected.
- Existing dynamic effect and trigger boundaries were inspected.
- Existing parallel-array alignment, target-generation, transaction, receipt, rollback, save/reload, and lifecycle patterns were inspected.
- The CXT extension contract and package carrier pattern were inspected.

### Required engine validation not available in this runtime

When the HOI4 MCP routes are callable, run the narrow Event 027 and doctrine inspections before implementation claims. Start every weighted pass with hoi4.probability_inspect, delegate the read-only scenario evidence to chaosx_ai_probability_auditor, and run hoi4.probability_compare with the same scenarios after any weight change.

The named probability scenarios from docs\specs\027_doctrine_research_specs\027_doctrine_research_probability_scenarios.md are DR-A01 through DR-G03. The current audit has no normalized probability, timing, or sequence result for any of them.

### Targeted implementation checks

- Compare every registry row against the native graph and reject stale Grand Doctrine, track, branch, index, DLC, and icon entries.
- Assert parallel queue and receipt array alignment before append, after mutation, and during recovery.
- Assert that unknown domain IDs, invalid dispatch selectors, stale owner epochs, missing targets, and unsupported mastery capabilities produce no doctrine effect.
- Assert that a repeated receipt cannot repeat a native effect or decrement a batch twice.
- Exercise zero, partial, threshold-adjacent, and over-threshold banked mastery cases for every supported branch family once exact engine semantics are available.
- Exercise ordinary Army and Chaos together to prove their shared land folder does not cross-target mastery.
- Exercise Navy and Air without current fleets or air wings for human availability, then audit the AI scores separately.
- Exercise Special Forces with each DLC gate combination and with the second-track active gate both true and false.
- Exercise save/reload at prepared, effect-applied, and choice-consumed receipt states.
- Exercise cosmetic tag change, subject transition, controller change, capitulation, annexation, and civil-war creation according to the accepted ownership rules.
- Exercise a malformed future adapter and confirm that ordinary domains remain available.

## Risks, unsupported fields, and limitations

1. Exact fractional mastery read support is not documented in the installed official dynamic-variable reference and was not engine-verified because the required MCP routes were unavailable.
2. No direct exact-one-level native mastery effect was found in the reviewed official effects documentation. add_mastery is point-based and can overshoot from banked progress.
3. set_sub_doctrine uses a folder-wide zero-based track index, not merely the index of matching branches. A stale index can mutate the wrong track.
4. Ordinary Army and Chaos share the land folder and four track identities. A folder-only mastery filter is unsafe.
5. Special Forces uses a separate folder, conditional DLC gate, two tracks with the same display identity, a second-track active trigger, mutual exclusions, and a different reward threshold. Display labels cannot be used as stable IDs.
6. Native branch reward thresholds can differ. A shared constant of 100 or a fixed five-level assumption is not safe for future custom domains.
7. Chaos native adoption and reward effects change flags, unlocks, technologies, units, readiness, and CBRN route state. Manual Event 027 duplication can create duplicate or out-of-order owner state.
8. Native effect ordering and save atomicity between a doctrine mutation and a later receipt decrement were not engine-verified. The durable receipt/reconcile state is the safe design, but ambiguous postconditions must stop rather than guess.
9. The current callable runtime exposed no HOI4 MCP inspection routes, so this audit has no engine artifact IDs, layout revisions, probability comparisons, or rendered proof.
10. Country clone semantics through civil war, dynamic country creation, and every tag transition were not proven from the unavailable engine route. Use owner epochs and narrow lifecycle proofs; quarantine ambiguous copied state.
11. The existing automatic event system already iterates through countries. This handoff proposes no new broad daily or weekly world iteration.
12. The existing Event 027 code has no cluster membership. Do not add a second cluster fanout until the parent inspects the current event-cluster registry and proves a need.

## Completion status

Architecture audit: complete.

Reusable gameplay helper implementation: intentionally not performed because the user assigned implementation and wiring to the parent.

Gameplay files changed: none.

Documentation file added: docs\plans\027_doctrine_research_plans\subagent_handoffs\scripted_system_architect_2026-08-29.md.

Meaningful validation: source inspection of the listed Chaos Redux, offline wiki, vanilla doctrine, official effects/triggers, official dynamic-variable, CXT, and lifecycle artifacts; read-only probability-auditor dispatch completed with the required MCP-unavailable result.

Skipped validation: HOI4 MCP event/doctrine/probability inspections and live gameplay validation were unavailable or outside this subagent's authority. No fallback source-only result is presented as engine evidence.

Skills used: chaos-redux-events, chaos-redux-mtth, and chaos-redux-subagents, plus the required read-only chaosx_ai_probability_auditor route. No skill was created or modified.
