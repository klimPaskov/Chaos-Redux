# Event014 inheritance storage contract

Disposition: implemented bounded source repair for E014-FINAL-01, pending parent review and runtime acceptance.
Acceptance basis: the parent's 2026-10-03 bounded helper-output lifetime repair instruction authorizes caller storage in the existing inheritance transactions and their consumed nested outputs.
This document specifies the existing output API and its storage ownership.

## Donor snapshot API

`cannibalism_capture_current_warlord_inheritance` reads the current country donor and snapshots thirteen regular values plus three origin flags.
Its definition is in `common/scripted_effects/014_cannibalism_effects.txt:12080`.
Scope: country, entered through the actual donor scope.
Inputs: the donor fields and flags in the table below.
Outputs: exactly these sixteen unscoped temporary scalars.

| Output | Donor input | Meaning |
| --- | --- | --- |
| `cannibalism_inherited_hierarchy` | `cannibalism_hierarchy` | Donor value |
| `cannibalism_inherited_larder_route` | `cannibalism_larder_route` | Donor value |
| `cannibalism_inherited_network_route` | `cannibalism_network_route` | Donor value |
| `cannibalism_inherited_larder` | `cannibalism_larder` | Donor value |
| `cannibalism_inherited_frenzy` | `cannibalism_frenzy` | Donor value |
| `cannibalism_inherited_alignment` | `cannibalism_network_alignment` | Donor value |
| `cannibalism_inherited_consumed_population` | `cannibalism_consumed_population` | Donor value |
| `cannibalism_inherited_consumed_population_k` | `cannibalism_consumed_population_k` | Donor value |
| `cannibalism_inherited_warlord_origin` | `cannibalism_warlord_origin` | Donor value |
| `cannibalism_inherited_warlord_region` | `cannibalism_warlord_region` | Donor value |
| `cannibalism_inherited_warlord_name_index` | `cannibalism_warlord_name_index` | Donor value |
| `cannibalism_inherited_warlord_slot_index` | `cannibalism_warlord_slot_index` | Donor value |
| `cannibalism_inherited_warlord_personality` | `cannibalism_warlord_personality` | Donor value |
| `cannibalism_inherited_origin_island` | `cannibalism_origin_island_host` | Flag snapshot, 0 or 1 |
| `cannibalism_inherited_origin_siege` | `cannibalism_origin_siege_commune` | Flag snapshot, 0 or 1 |
| `cannibalism_inherited_origin_march` | `cannibalism_origin_march_host` | Flag snapshot, 0 or 1 |

Defaults: allocate every output inline at zero in the consuming caller's own frame before calling capture and before entering donor country scopes.
A missing regular donor variable reads as zero.
The three origin outputs start at zero and follow the existing island, siege, march `if`/`else_if` priority, so at most one is set to one.
These are temporary snapshots of real flags, with no new persistent numeric flag state.
Side effects: capture writes temporary outputs only and does not change donor population, Larder, equipment, flags, event targets, or identity.
The subsequent apply helpers retain their existing tuning and effects.

The three owners are `cannibalism_create_unified_country_from_selected_host`, `cannibalism_absorb_current_warlord_into_unified_host`, and `cannibalism_create_wendigo_unification_from_selected_hosts`.
They allocate all sixteen outputs at frame entry.
The two-human Wendigo branch overrides `cannibalism_inherited_larder` to zero after capture and disables donor absorption, preserving the nonabsorbed human's local store.
The outer `cannibalism_try_execute_wendigo_unification` does not consume the snapshot after its creating helper returns and does not allocate it again.

Usage inside an owning caller, before entering its donor scope:

```txt
set_temp_variable = { cannibalism_inherited_hierarchy = 0 }
set_temp_variable = { cannibalism_inherited_larder_route = 0 }
set_temp_variable = { cannibalism_inherited_network_route = 0 }
set_temp_variable = { cannibalism_inherited_larder = 0 }
set_temp_variable = { cannibalism_inherited_frenzy = 0 }
set_temp_variable = { cannibalism_inherited_alignment = 0 }
set_temp_variable = { cannibalism_inherited_consumed_population = 0 }
set_temp_variable = { cannibalism_inherited_consumed_population_k = 0 }
set_temp_variable = { cannibalism_inherited_warlord_origin = 0 }
set_temp_variable = { cannibalism_inherited_warlord_region = 0 }
set_temp_variable = { cannibalism_inherited_warlord_name_index = 0 }
set_temp_variable = { cannibalism_inherited_warlord_slot_index = 0 }
set_temp_variable = { cannibalism_inherited_warlord_personality = 0 }
set_temp_variable = { cannibalism_inherited_origin_island = 0 }
set_temp_variable = { cannibalism_inherited_origin_siege = 0 }
set_temp_variable = { cannibalism_inherited_origin_march = 0 }
event_target:cannibalism_unification_host = {
	cannibalism_capture_current_warlord_inheritance = yes
}
# The same caller can enter its destination scope and consume the snapshot.
```

An initialization helper cannot own these outputs for its caller when their first definitions occur inside that helper.
Caller allocation must be inline.
Do not use `ROOT.` or `PREV.` on any of these temporary output tokens.

## Adjacent output APIs

`cannibalism_achievement_capture_current_player_ledger` has country donor scope and reads player state, first-host/exploitation/joint-suppression/decisive-aid flags, and three achievement counters.
The same three inheritance owners allocate its ten temporary outputs at zero before capture and before country scope changes.
The outputs are `cannibalism_achievement_transfer_player`, `cannibalism_achievement_transfer_first_host`, `cannibalism_achievement_transfer_countries_suppressed`, `cannibalism_achievement_transfer_isolated_recovered`, `cannibalism_achievement_transfer_reconstruction`, `cannibalism_achievement_transfer_exploitation_ever`, `cannibalism_achievement_transfer_exploitation_renounced`, `cannibalism_achievement_transfer_exploitation_repeated`, `cannibalism_achievement_transfer_joint`, `cannibalism_achievement_transfer_decisive`.
Capture only changes temporary snapshots.
`cannibalism_achievement_apply_captured_player_ledger` applies the captured flags and counters to the existing destination country under its existing player gate.

`cannibalism_migrate_spread_entries_between_countries` requires valid regular source and destination country targets, a positive destination actor generation, distinct countries, and a valid aligned spread queue.
It returns `cannibalism_spread_migration_result`, with zero for rejection and one after validated migration and ledger rebuild.
The consuming runtime-migration helper allocates this result at zero before calling it.
The migration helper allocates its validation result and loaded `cannibalism_expected_spread_id` at zero.
It retains the existing row cursor setup, exact row-ID comparisons and input targets.
Its side effects remain country and state spread metadata migration and rebuilding the derived pending ledgers.

`cannibalism_migrate_runtime_references_to_unified_country` uses the same regular source/destination targets and returns `cannibalism_runtime_migration_result`, initially zero and set to one after spread migration permits node and external-source rewrites.
The later ordinary absorption owner and `cannibalism_absorb_primary_warlord_donor_into_wendigo` allocate this result at frame entry before entering destination country scope.
Ordinary opening creation calls migration without consuming its result and needs no otherwise-unused return allocation.
The existing gates are preserved and this storage contract does not add generation validation predicates.

`cannibalism_validate_spread_queue` returns `cannibalism_spread_queue_validation_result` at zero or one and can set the existing invariant-failure global flag on rejection.
Each patched direct consumer owns its result before the validation call.
Validation owns the loaded row ID, source generation, and four context-loaded outputs before calling `cannibalism_load_spread_entry_context`.
Its route variable is already assigned directly for each row and needs no additional allocation.
`cannibalism_rebuild_spread_pending_ledgers` allocates its six consumed context fields, including the route, at frame entry.
Its unused source-state-loaded output is not hoisted.
The context loader uses the existing row cursor and seven outputs, along with regular source/target event targets.
Unused route-parameter outputs are not hoisted.

`cannibalism_prepare_consumption_context` owns its existing consumption result, actual population loss and Larder gained outputs before `cannibalism_consume_current_state` returns.
It also allocates the five consumed/forwarded parameter outputs at zero before `cannibalism_set_consumption_parameters_from_context`: `cannibalism_consumption_parameters_valid`, `cannibalism_consumption_base_percent`, `cannibalism_consumption_hard_cap`, `cannibalism_consumption_larder_factor`, and `cannibalism_consumption_larder_cap`.
Inputs such as mode, exact population request, request identity and target are preserved.
`cannibalism_register_current_wendigo_anchor` allocates `cannibalism_consumption_result` as `constant:cannibalism_consumption_result.invalid_scope` and `cannibalism_population_loss_applied` at zero before the host-country consumption call.
Its existing exact-loss equality gate and one-time anchor flags remain unchanged.
The canonical exact-state population helper already has caller-owned result and applied-loss storage and needs no patch.

## Caller map

All listed allocations occur in each caller's frame before nested helper execution.
The paired boundary inventory includes exact defaults and the insertion patch.

| Consuming or forwarding frame | Added output storage |
| --- | --- |
| `cannibalism_create_unified_country_from_selected_host` | `cannibalism_inherited_hierarchy`, `cannibalism_inherited_larder_route`, `cannibalism_inherited_network_route`, `cannibalism_inherited_larder`, `cannibalism_inherited_frenzy`, `cannibalism_inherited_alignment`, `cannibalism_inherited_consumed_population`, `cannibalism_inherited_consumed_population_k`, `cannibalism_inherited_warlord_origin`, `cannibalism_inherited_warlord_region`, `cannibalism_inherited_warlord_name_index`, `cannibalism_inherited_warlord_slot_index`, `cannibalism_inherited_warlord_personality`, `cannibalism_inherited_origin_island`, `cannibalism_inherited_origin_siege`, `cannibalism_inherited_origin_march`, `cannibalism_achievement_transfer_player`, `cannibalism_achievement_transfer_first_host`, `cannibalism_achievement_transfer_countries_suppressed`, `cannibalism_achievement_transfer_isolated_recovered`, `cannibalism_achievement_transfer_reconstruction`, `cannibalism_achievement_transfer_exploitation_ever`, `cannibalism_achievement_transfer_exploitation_renounced`, `cannibalism_achievement_transfer_exploitation_repeated`, `cannibalism_achievement_transfer_joint`, `cannibalism_achievement_transfer_decisive` |
| `cannibalism_absorb_current_warlord_into_unified_host` | `cannibalism_inherited_hierarchy`, `cannibalism_inherited_larder_route`, `cannibalism_inherited_network_route`, `cannibalism_inherited_larder`, `cannibalism_inherited_frenzy`, `cannibalism_inherited_alignment`, `cannibalism_inherited_consumed_population`, `cannibalism_inherited_consumed_population_k`, `cannibalism_inherited_warlord_origin`, `cannibalism_inherited_warlord_region`, `cannibalism_inherited_warlord_name_index`, `cannibalism_inherited_warlord_slot_index`, `cannibalism_inherited_warlord_personality`, `cannibalism_inherited_origin_island`, `cannibalism_inherited_origin_siege`, `cannibalism_inherited_origin_march`, `cannibalism_achievement_transfer_player`, `cannibalism_achievement_transfer_first_host`, `cannibalism_achievement_transfer_countries_suppressed`, `cannibalism_achievement_transfer_isolated_recovered`, `cannibalism_achievement_transfer_reconstruction`, `cannibalism_achievement_transfer_exploitation_ever`, `cannibalism_achievement_transfer_exploitation_renounced`, `cannibalism_achievement_transfer_exploitation_repeated`, `cannibalism_achievement_transfer_joint`, `cannibalism_achievement_transfer_decisive` |
| `cannibalism_create_wendigo_unification_from_selected_hosts` | `cannibalism_inherited_hierarchy`, `cannibalism_inherited_larder_route`, `cannibalism_inherited_network_route`, `cannibalism_inherited_larder`, `cannibalism_inherited_frenzy`, `cannibalism_inherited_alignment`, `cannibalism_inherited_consumed_population`, `cannibalism_inherited_consumed_population_k`, `cannibalism_inherited_warlord_origin`, `cannibalism_inherited_warlord_region`, `cannibalism_inherited_warlord_name_index`, `cannibalism_inherited_warlord_slot_index`, `cannibalism_inherited_warlord_personality`, `cannibalism_inherited_origin_island`, `cannibalism_inherited_origin_siege`, `cannibalism_inherited_origin_march`, `cannibalism_achievement_transfer_player`, `cannibalism_achievement_transfer_first_host`, `cannibalism_achievement_transfer_countries_suppressed`, `cannibalism_achievement_transfer_isolated_recovered`, `cannibalism_achievement_transfer_reconstruction`, `cannibalism_achievement_transfer_exploitation_ever`, `cannibalism_achievement_transfer_exploitation_renounced`, `cannibalism_achievement_transfer_exploitation_repeated`, `cannibalism_achievement_transfer_joint`, `cannibalism_achievement_transfer_decisive` |
| `cannibalism_absorb_current_warlord_into_unified_host` | `cannibalism_runtime_migration_result` |
| `cannibalism_absorb_primary_warlord_donor_into_wendigo` | `cannibalism_runtime_migration_result` |
| `cannibalism_migrate_runtime_references_to_unified_country` | `cannibalism_spread_migration_result` |
| `cannibalism_migrate_spread_entries_between_countries` | `cannibalism_spread_queue_validation_result`, `cannibalism_expected_spread_id` |
| `cannibalism_validate_spread_queue` | `cannibalism_expected_spread_id`, `cannibalism_spread_source_generation`, `cannibalism_spread_source_country_context_loaded`, `cannibalism_spread_source_state_context_loaded`, `cannibalism_spread_target_country_context_loaded`, `cannibalism_spread_target_state_context_loaded` |
| `cannibalism_rebuild_spread_pending_ledgers` | `cannibalism_spread_queue_validation_result`, `cannibalism_expected_spread_id`, `cannibalism_spread_route`, `cannibalism_spread_source_generation`, `cannibalism_spread_source_country_context_loaded`, `cannibalism_spread_target_country_context_loaded`, `cannibalism_spread_target_state_context_loaded` |
| `cannibalism_execute_evolution_iii_reveal` | `cannibalism_spread_queue_validation_result`, `cannibalism_wendigo_unification_result` |
| `cannibalism_integrate_terminal_ai_warlords` | `cannibalism_absorption_result` |
| `cannibalism_begin_current_warlord_slot_release` | `cannibalism_spread_queue_validation_result` |
| `cannibalism_prepare_consumption_context` | `cannibalism_consumption_parameters_valid`, `cannibalism_consumption_base_percent`, `cannibalism_consumption_hard_cap`, `cannibalism_consumption_larder_factor`, `cannibalism_consumption_larder_cap` |
| `cannibalism_register_current_wendigo_anchor` | `cannibalism_consumption_result`, `cannibalism_population_loss_applied` |

The Wendigo wrapper already initializes the result forwarded by its nested creation helper.
`cannibalism_execute_evolution_iii_reveal` allocates that forwarded result before calling the wrapper.
Terminal integration allocates the absorption result it checks after each call.
Submission wrappers and event definitions consume no such return result and receive no unused allocation.
`cannibalism_unified_creation_result` has no outer consumer in these transactions and is left local.

## Constants, targets and cleanup

No tuning constant, weight, cost, duration, selection score, or eligibility predicate is changed.
Zero initial values are storage defaults rather than balance settings.
The existing invalid-scope constant supplies the anchor's failure default.
No shared dynamic helper or initialization wrapper is introduced, and the shared dynamic registry/docs are unchanged.
Existing regular donor, destination, consumption and loaded-context event targets retain their current lifecycle and cleanup.
No permanent variable or new event target is introduced.
Temporary output storage expires with its owning effect frame and must not be cleared before its immediate consumers or forwarding helpers return.
This patch adds no new flag cleanup or periodic hooks.
There are no new icons, assets, localisation keys or UI consumers.

## Evidence and validation limits

The repair handoff and evidence live at `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_inheritance_helper_storage_repair.md` and its same-named evidence directory.
`storage_boundaries.json` records defaults, hashes and exact added hunks.
`source_lifetime.patch` contains the exact source patch against the captured shared file.
`source_contract_checks.json` records actual-source storage projections, pre-repair negative controls and byte-preservation checks.
The one-off check reuses the final completion audit's lexical reader and discards callee-created temporary storage on helper return.
Ordinary opening, later absorption and original-ZZZ ownership are checked with distinct nonzero donor values and all three origin alternatives.
Both-human projection retains route/identity fields and zeroes only inherited Larder.
Nested migration failure and success, forwarded return ownership and exact-population return storage are checked separately.
All original source lines, including provider 523, transfer operations, population guards and the post-capture human exception, retain their original bytes.

These projections do not execute full event transactions, native annexation, equipment transfer, population/deaths accounting, technology union, multiplayer, or engine callback behavior.
The selected opening host retains its actor/global generation equality check.
The destination-validity trigger has no actor/global generation equality comparison, and this bounded storage repair cannot establish rejection of every stale destination.
Spread validation retains exact source-generation metadata comparisons, while the rebuild's generation gate remains source evidence.
No observed runtime output loss or duplicate transfer is claimed.

`hoi4.event_inspect` and the narrow `set_temp_variable` reference search returned no status/artifact within a 45-second client observation window.
Prior reference-context/read/source and event render/compare failures remain linked evidence.
`hoi4.script_validate` is not exposed, and connected health/version/task negotiation is unconfirmed.
No helper-expansion, jobs or tasks were used.
MCP event/helper coverage and native runtime acceptance remain unresolved.
Local wiki and installed documentation excerpts retain absolute Windows paths, exact spans and SHA-256 revisions in `reference_excerpts.json`.
The controlling lifetime rule is offline Data structures lines 438-450, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Installed `set_temp_variable` documentation lines 7820-7839 and the CHI native example lines 803-820 support assignment syntax and unscoped use.

## Follow-up

The parent owns final source review, commit and runtime claims.
Any expansion into Larder scaling, Network data helpers, scored selection, or broader generation gates belongs to a separate owner tranche.
A later source contract audit can extend conservative storage coverage to remaining Event014 APIs without assuming this bounded repair covers the full event.
No mechanic simplification or replacement is introduced.
