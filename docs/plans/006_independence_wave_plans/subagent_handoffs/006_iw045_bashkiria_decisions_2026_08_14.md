# IW-045 Bashkiria decision/category handoff (2026-08-14)

## Scope and disposition

The IW-045 Bashkiria decision surface is implemented in the two owned gameplay files below. The category and all decisions fail closed on the exact BSK package gate and setup flag. No content-attestation, central admission, Join, focus, asset, or unrelated package file was edited by this tranche.

- `common/decisions/categories/006_independence_wave_bashkiria_categories.txt`
- `common/decisions/006_independence_wave_bashkiria_decisions.txt`

The package remains central-admission fail-closed until the parent completes its adapter/attestation evidence. The category is `independence_wave_bashkiria_frontier_compact_category`; visibility requires `is_independence_wave_bashkiria_package = yes` and `independence_wave_iw_045_setup_complete`.

## Stable decision and mission IDs

The founding mission is `independence_wave_bsk_hold_frontier_congress`. The ten serialized projects use the exact IDs already consumed by the BSK active-project trigger and cleanup effect:

1. `independence_wave_bsk_secure_frontier_depots`
2. `independence_wave_bsk_integrate_frontier_guards`
3. `independence_wave_bsk_register_bashkir_communities`
4. `independence_wave_bsk_settle_former_host_ledgers`
5. `independence_wave_bsk_ratify_constitutional_autonomy`
6. `independence_wave_bsk_adopt_agrarian_compact`
7. `independence_wave_bsk_convene_socialist_councils`
8. `independence_wave_bsk_establish_frontier_emergency_command`
9. `independence_wave_bsk_codify_durable_sovereignty`
10. `independence_wave_bsk_open_ural_network_corridor`

The previous draft aliases (`secure_oilfield_depots`, `integrate_border_guards`, `register_community_compacts`, `establish_emergency_command`, and `open_volga_ural_corridor`) were removed from the decision source so the runtime trigger, cleanup, and localisation contracts resolve one name each. Canonical BSK localisation keys already exist in `localisation/english/006_independence_wave_bashkiria_l_english.yml`; that file was not modified here.

## Mission quality audit

Owner is the living BSK country package (`original_tag = BSK`, package `iw_045`), category is `independence_wave_bashkiria_frontier_compact_category`, and the geographic anchor is state 651/Ufa in the `volga_urals_siberia_far_east` regional lane. The requirement is the exact package/setup/current-force-generation gate plus state-651 capital control; success requires both package ledgers at the stable threshold, one installed route government, and continued ownership/control of state 651. The founding timeout is 420 days. Failure is explicit on timeout, package loss, capital/state loss, or failed package cancellation and applies one idempotent crisis penalty. Duplicate risk is contained by the single mission ID, core cleanup, and the serialized active-project gate; projects cannot overlap because every availability block requires `NOT = { has_independence_wave_bsk_active_package_project = yes }`. The four government-route projects are mutually locked by the shared route-government predicate, while the host and network projects carry their own target/route gates.

## Lifecycle and costs

The founding mission has the BSK `founding_crisis` timeout constant (420 days). It is not manually selectable. It cancels/resolves on package loss, state-651 ownership/control loss, capital control loss, or the conjunction of stable Congress Cohesion and Frontier Readiness, an installed route government, and state-651 control. Timeout and failed cancellation set `independence_wave_bsk_compact_crisis_failed` and call the idempotent BSK failure helper; valid completion sets `independence_wave_bsk_compact_crisis_resolved`.

Each project requires `is_independence_wave_bsk_project_ready`, the state-651 capital control gate (plus the explicit former-host or network conditions where applicable), a shared concrete material/resource cost trigger, and `NOT = { has_independence_wave_bsk_active_package_project = yes }`. Completion first calls `independence_wave_bsk_begin_project` and the shared payment effect. Timed projects use the shared decision durations: short (45 days), standard (75 days), long (180 days); sovereignty uses the shared strategic duration. Cancel effects revalidate the BSK package before applying the idempotent failure penalty. The BSK project-ready trigger now includes current force-package generation proof, so rollover invalidates active project readiness without duplicating generation guards in every decision.

Cost surfaces are visible and non-free: administration projects use BSK administration triggers and shared command-power/manpower payment effects; security projects use shared equipment/manpower/experience costs; former-host and network projects use shared command-power plus convoy/train costs; sovereignty uses the strategic stability, war-support, command-power, convoy/train, and factory gate. The civilian-factory burden is exposed with the file-scoped BSK modifier value and the shared BSK cost trigger floor.

AI validity is bounded to the package-local `ai_will_do` blocks (high/standard/urgent shared constants, with war modifiers on security-sensitive work); no invalid target is selected by the project lane. The probability adapter did not expose an available runtime pool, so no claim is made about relative AI ranking, starvation, or timing. The decision tooltips use existing canonical BSK name/description/effect keys and shared cost text; no untranslated decision-owned key was found. Cleanup removes the mission and all ten projects, clears package ideas, ledgers, route/crisis/progress flags, and restores the vanilla BSK party ladder. Payment effects are shared and failure is idempotent, so no free reward loop, duplicate completion reward, or repeated cancellation penalty is introduced by this source.

## Route and host/network behavior

The four route projects are locked to their corresponding route triggers and require no previously installed BSK route government. The former-host ledger project requires a live non-war former host or the documented local fallback after depot security; if the live host becomes hostile during the timer, the cancel path closes the ledger locally when the fallback remains valid, otherwise it applies the failure penalty. Durable sovereignty requires the founding settlement, resolved crisis, stable ledgers, and an installed route government. The Ural network project additionally requires the founding settlement, resolved crisis, network membership, league route availability, stable ledgers, and capital control.

## Validation evidence

- Static brace counts: decisions `242/242`; category `2/2`.
- Decision IDs compare exactly with `has_independence_wave_bsk_active_package_project` and `independence_wave_cleanup_iw_045_bashkiria` (no missing or extra project IDs).
- No old `iw_044`, old BSK project aliases, or undefined `independence_wave_bashkiria_duration.project_*` tokens remain in the decision source.
- Canonical decision name/description keys were checked against the existing BSK localisation file; all are present, including the five renamed canonical projects.
- Mandatory probability inspection was rerun after source creation with adapter `mission_ai_will_do`, workspace `mod_chaos_redux_ea3b2d67c2c0`: `PROBABILITY_SOURCE_INSPECTED`, source hash `b7b031d727e03702aabc0decda0612f29957d2a01bfcb3565b1e30f06be54844`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3be489e648d9102219603e3d15c8ba474a0d069775bab700790dec89eda4493/f351c9cf3f5ec42b3381462159b78a0502c21ccfccc227a836c931b17c478b98/probability-inspect-b7b031d727e0.json`. MCP found 11 mission candidates, 0 available candidates, an incomplete pool, 15 required inputs, and no unresolved source expressions; no quantitative AI balance claim is made. The earlier pre-file call returned `PROBABILITY_SOURCE_NOT_FOUND` and is superseded by this current-source result.
- The BSK AI-strategy audit separately reports no weighted strategy surface and `PROBABILITY_SURFACE_EMPTY`; it remains an evidence blocker, not a reason to widen AI weights.

## Remaining issues and parent actions

- Central attestation/Join and final package admission remain intentionally untouched and fail closed.
- The shared package-dispatch list remains parent/core-owned integration; this tranche does not add BSK to central setup/final-validation/cleanup dispatch, so the new category and decisions are inert until that adapter wiring and its evidence are accepted.
- Parent-owned localisation/catalog reconciliation should retain the canonical BSK keys and remove or deprecate stale aliases only if no other source references them.
- MCP typed-scenario evaluation/compare remains incomplete because the discovered mission pool has no available candidates. Live gameplay validation remains parent/user-owned.

No commit or staging was performed.
