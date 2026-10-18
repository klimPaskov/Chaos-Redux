# Event 006 league expulsion evidence helpers

## `independence_wave_allocate_automatic_packages`

Country-scope allocator called by `independence_wave_prepare_and_execute_standalone_incident` and `liberations_joint_prepare_and_execute_incident` after the shared coordinator enters allocation.
It captures the current chaos-band tuning through `independence_wave_begin_plan_contribution`, then reserves admitted package anchors until the exact target is selected, the pool is exhausted, or the attempt limit is reached.
The shared `independence_wave_count` constants define 3, 4, 5, 7, 10, and 10 countries across the six chaos bands.
It publishes `independence_wave_plan_contribution_ready` only when the selected count equals the frozen target and the metadata arrays align.
An incomplete selection sets `independence_wave_plan_exact_count_failed` and `liberation_plan_reject_reason.insufficient_pool` without rewriting either the Event 006 target or the shared expected country count.
The caller retains ownership of cancellation, reservation cleanup, execution, and the terminal receipt.
This helper changes reservation metadata and frozen evolution state but performs no country release, ownership transfer, or public presentation.
It adds no event targets or cleanup lifecycle beyond the existing plan contribution.

Usage: `independence_wave_allocate_automatic_packages = yes` inside an allocating plan that includes Event 006.

## `independence_wave_apply_generic_government_route_politics`

Country-scope helper called by `independence_wave_select_government_route` after
the route has passed its package and ledger gates. It maps the seven shared
government routes to a concrete ruling-party/elections posture: constitutional
republic to democratic elections, popular council to communism without
elections, radical sovereignty to fascism without elections, traditional,
emergency, and patron-client routes to a non-elective neutrality posture, and
the researched neutral commission route to a non-elective democratic posture.
Package-specific adapters run afterward when they have a documented carrier
party surface and may override the shared posture. This helper has no input
store, does not add political power, and runs only at the one-time route lock.

## `independence_wave_record_league_expulsion_ground`

Country-scope writer for the DM-60 charter case. Callers invoke it only at a
factual transaction point while the country is an active league member under
the anti-puppetry charter and the formal, durable, or reformed league phase.

Inputs:

- temporary `independence_wave_expulsion_ground_input`: one value from
  `constant:independence_wave_expulsion_ground`;
- temporary `independence_wave_expulsion_has_target_input`: zero or one;
- when the target input is one, temporary
  `independence_wave_expulsion_evidence_target_input` is a surviving country
  scope to persist as the secondary witness.

Outputs and side effects:

- increments the accused country's `independence_wave_charter_violation_count`;
- writes `independence_wave_expulsion_ground`,
  `independence_wave_expulsion_ground_date`, and the optional persistent
  country-scope witness variable;
- sets `independence_wave_expulsion_ground_recorded` and clears any prior
  resolved marker;
- promotes the current ground to
  `constant:independence_wave_expulsion_ground.repeated_charter_violation`
  once the threshold in
  `constant:independence_wave_decision_gate.repeated_charter_violation_threshold`
  is reached.

Current call sites:

- patron-client route selection after a strict charter member locks that route;
- `on_annex` before the victim country is removed;
- `on_war_relation_added` when a defensive-charter member starts an external
  war (civil-war participants are excluded);
- DM-43 refusal response;
- DM-44 cancellation while its threatened member remains at war;
- DM-61 sponsored member coup.

## `independence_wave_expel_league_member`

DM-60 resolution helper. It requires the active factual-case flag, marks the
case resolved, unregisters the aligned league member/founder rows, preserves
the network and Event 006 origin, and applies the existing discredited-member
idea lifecycle.

## `independence_wave_clear_league_expulsion_case`

Generation cleanup for the case flag, repeated marker, ground/date, secondary
target pointer, and violation count. It is called by Event 006 generation
reset and origin termination, never by a periodic world action.

## `independence_wave_clear_binding_arbitration_request`

Clears the DM-43 pending requester pointer, request date, pending flag, and
refusal marker. DM-43 uses it on success/cancellation; Event 006 cleanup uses
it as a stale-pointer guard.

## `independence_wave_start_sponsored_member_coup`

Target-country helper for DM-61. It starts a vanilla `start_civil_war` revolt
using the target's current government to select the opposing ideology and a
central `independence_wave_decision_coup.revolt_size` value injected by
`meta_effect`. It does not spawn free sponsor units or run a world scan.

## `independence_wave_revalidate_reclamation_front_operation`

Country-scope lifecycle guard for the active DM-58 operation. It is called after
the generation-matched league row is removed by
`independence_wave_unregister_league_member`.

Inputs:

- the persistent global `independence_wave_reclamation_fronts_coordinated`
  operation flag;
- the aligned `global.independence_wave_league_member_*` registry and its
  current member count;
- the frozen `global.independence_wave_reclamation_front_members` witness array.

Outputs and side effects:

- invokes `independence_wave_cleanup_reclamation_front_operation` when the
  league drops below the formation minimum or the exiting country is a recorded
  witness member;
- clears the shared operation flag, coordinator target, state receipts,
  readiness fields, and frozen witness arrays through the shared cleanup path;
- deliberately leaves already-issued finite `take_state_focus` war goals to
  their own timed expiry and never manufactures replacement targets.

The witness-array membership check is generation-safe for the single active
operation because the array is rebuilt only by the current-generation DM-58
resolver and is cleared by every operation reset path.

## `independence_wave_prepare_event021_adapter_origin`

Country-scope package-only preparation entry used by Event 021 when it reuses a
complete human Event 006 country package. It requires the transient
`random_civil_war_event6_adapter_preparing` and
`independence_wave_event6_adapter_package_ready` flags, then delegates to the
shared reversible package-state primitive.

Inputs:

- regular event targets `independence_wave_setup_former_host` and
  `independence_wave_setup_anchor_state`;
- the temporary or normal `independence_wave_setup_*` package values;
- the two explicit Event 021 adapter-window flags.

Outputs and side effects:

- prepares country-local package values, force metadata, identity lifecycle
  defaults, and the temporary `independence_wave_origin_prepared` receipt;
- does not record Event 006 origin history or fired state;
- does not advance the Event 006 generation sequence or evolutions;
- does not register Event 006 active, network, or league membership;
- leaves final identity confirmation and Event 021 origin provenance to the
  Event 021 parent transaction.

The normal Event 006 entry remains `independence_wave_prepare_country_origin`.

## `independence_wave_impose_recognition_blockade`

Country-scope helper called by the failure branches of DM-28 (Demand Recognition by Force) and DM-51 (Prepare a Border Ultimatum) after their recognition loss has been applied.
It acts only on an Event 006 package country that does not already hold treaty-backed recognition (`has_independence_wave_treaty_backed_recognition`).
It sets `independence_wave_recognition_blockade_active` and runs the country refresh, so the Recognition Blockade idea replaces the current recognition idea and the once-per-generation dormant-identity opening-confidence feedback is recorded.
The flag is cleared when the country reaches treaty-backed recognition (`independence_wave_refresh_recognition_idea`), when the former host's outcome becomes recognized separation (`independence_wave_set_host_outcome`), and when the origin ends (`independence_wave_remove_origin_ideas` and the generation reset).
DM-11 and DM-16 weigh a blockaded country or blockaded target up for the AI.
No world iteration is used.

## League patron capture latch

`independence_wave_change_league_values` sets the global `independence_wave_league_patron_captured` latch when the League's patron capture meter first reaches `independence_wave_league.patron_captured` (60) during a formal, durable, or reformed League phase.
The latch compares the meter before and after the change, so a meter that stays above the level does not latch again.
`independence_wave_enter_league_crisis` reads the latch next to the cohesion, confidence, failed-rescue, member-war, and rival-bloc causes.
`independence_wave_reform_league` clears it and returns a meter at or above the captured level to `independence_wave_league.reform_patron_capture` (30, the statehood-incident warning level).
`independence_wave_dissolve_league_to_network` and `independence_wave_restart_informal_network` clear it with the other failure latches.
No world iteration is used.

## Event 006 country-registry effects

This section covers only the two lifecycle wrappers needed by the canonical
Independence Wave origin ledger. The static carrier data lives in the section marked `[source: 006_independence_wave_country_registry_constants.txt]` of
`common/script_constants/006_independence_wave_constants_registry.txt`;
the exact country-scope predicates live in the country-registry section of
`common/scripted_triggers/006_independence_wave_package_triggers.txt`.

### `independence_wave_registry_record_event6_origin`

- Scope: country.
- Inputs: none; the caller has already validated the Event 006 setup package.
- Outputs: sets `independence_wave_active_origin`, clears the ended marker, and
  writes `liberation_origin = constant:liberation_origin.independence_wave`.
- Side effects: only the normal Event 006 origin markers. It does not create a
  tag, change ownership, add cores, load a focus tree, or touch Event 012 flags.
- Call site: `independence_wave_prepare_country_origin` in
  `common/scripted_effects/006_independence_wave_effects.txt`.

### `independence_wave_registry_clear_event6_origin`

- Scope: country.
- Inputs: none; called after the Event 006 package and ledger cleanup chain.
- Outputs: clears the live Event 006 origin, preserves
  `independence_wave_origin_ended`, and resets `liberation_origin` to `none`.
- Side effects: no tag, focus, state, or Event 012 mutation.
- Call site: `independence_wave_end_active_origin` in the same Event 006 effect
  file.

### Provenance and cleanup contract

Event 012 records its own `africa_priority_origin_*` and package flags. It must
never call either helper, so an Africa promotion cannot acquire Event 006
origin provenance by sharing a carrier tag. Event 006's existing package,
network, event-target, and focus cleanup still runs before the clear wrapper.
The registry itself owns no event targets: the short-lived setup targets remain
the existing `independence_wave_setup_former_host` and
`independence_wave_setup_anchor_state` targets, and the existing Event 006
cleanup chain remains responsible for clearing them and global targets.

### Static carrier status API

The country-group constants in the `[source: 006_independence_wave_country_registry_constants.txt]` section of
`common/script_constants/006_independence_wave_constants_registry.txt`
expose package-row status projections for later callers:

- `selectable_bound_tags` is the current-map-bound selectable pool (138 rows,
  137 unique carrier scopes).
- `selectable_unbound_tags` is the explicit fail-closed selectable pool (55
  rows, 55 unique carrier scopes). Missing geography is preserved; no nearby
  state or substitute tag is implied.
- `event6_owned_bound_tags` and `event6_owned_unbound_tags` split custom `X`
  registrations by current-map status.
- `registered_reuse_bound_tags` and `registered_reuse_unbound_tags` split
  vanilla-tag reuse rows by current-map status.
- `overlay_route_carrier_tags` and its route-specific subsets expose the
  original carriers for all thirteen non-selectable overlays. Overlay
  carriers may also appear in a selectable pool when the same vanilla country
  has a separate Event 006 row; route triggers remain the identity gate.

Country groups de-duplicate tags, so BIA appears in both bound and unbound
status projections: IW-107 is bound while IW-096 is unbound. Exact package
identity, anchor, host, reservation group, readiness, scenario rank, and
package status remain row-level facts in the canonical candidate registry,
package-id constants, and current-map binding CSV. Use those sources and the
existing region load/reserve dispatchers when a caller needs a specific row;
do not infer a row from a carrier tag alone.

The public `chaosx_country_independence_wave_*` collections mirror these
status and overlay views. Collections are active views and naturally omit
dormant reserved tags; static country-group constants remain the source for
registration audits and fail-closed admission checks.

## Event 006 roster checkpoint effects

### `independence_wave_apply_roster_checkpoint`

Country-scope helper for the synchronous Event 006 package-roster receipt.
The helper is called after a package-specific setup trigger has selected the package country.
It has no explicit inputs and reads the current `THIS` country scope.

The helper preserves the former `chaosx.nr6.350` immediate branches exactly.
It writes the TRA, MNT, KOS, KUB, TAT, BSK, RUT, MAC, AXX, BAX, BBX, BOS, NAV, and GLC roster checkpoint flags when their package and command-roster triggers pass.
It applies the MNT political-carrier portrait overrides for `MNT_kristo_popovic` and `MNT_blazo_jovanovic`.
It applies the BSK `Yakov Bykin` portrait override once behind `independence_wave_bsk_portrait_override`.
It applies the RUT `Augustin Voloshyn` portrait override for the Event 006 package scope.

The helper does not release countries, create characters, change package costs, mutate central attestation, open the pre-event UI, or use event targets.
It has no constants or tuning table because the checkpoint is a fixed roster receipt and the package-specific triggers remain the source of eligibility.
There is no event-target cleanup plan because the helper does not persist scope pointers.

### Call sites and migration

The active package setup callers use the helper directly in Bosnia, Bashkiria, Iberia, IW043/IW058, IW093/IW098, Karelia/Crimea, Komi, Kosovo, Kuban, Macedonia, the Mediterranean package, Montenegro, the Pacific package, Ruthenia, Tatarstan, Transylvania, and UDM.
The hidden compatibility event `chaosx.nr6.350` delegates to the same helper so older external references retain the roster and portrait behavior.
Direct calls are synchronous within the current package setup effect, so immediate checkpoint flag tests observe the flags before setup continues.

## League failure latches and charter cleanup

`independence_wave_clear_league_failure_latches` (global scope) clears the three failure latches `independence_wave_league_failed_rescue`, `independence_wave_league_member_war`, and `independence_wave_league_patron_captured`.
`independence_wave_reform_league` calls it directly.

`independence_wave_clear_league_charter_and_leader` (global scope) ends the current charter generation.
It clears the five charter articles and the radical charter marker, calls the failure-latch helper, clears the leader country flag through the saved event target and the stored variable, and clears the leader and congress-leader variables.
`independence_wave_dissolve_league_to_network` and `independence_wave_restart_informal_network` both call it, so the dissolution and re-entry boundaries clear the same state.

`independence_wave_change_league_values` gates on `has_independence_wave_live_league_phase` and the patron-captured latch on `has_independence_wave_formal_league_phase`, both documented in `006_independence_wave_decision_triggers.md`.
The permanent border war idea reads the reclamation-conflict host outcome directly; no mirror flag exists.
