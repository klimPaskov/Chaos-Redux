# Event 019 Dynamic Unit Provider API Completion — 2026-08-22

## Outcome

Event 19 discovers every installed custom combat family through the shared Chaos unit-family registry and owner-side provider callbacks. The corrected current census is 97 land sub-units: 50 combat and 47 support. Nineteen providers (`501-514`, `518`, `520-523`) cover all 50 combat units and four inseparable support attachments. The remaining 43 support definitions are explicitly parent-owned because they cannot form a legal standalone division without a combat regiment.

The sole dedicated Event 19 registry code file remains `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`. No family-specific or second Event 19 registry file was created. A future family adds one idempotent registration surface and one complete owner-side provider package; Event 19 contains no current-family or custom-equipment list that must be extended.

## Provider contract

Every one of the 19 providers exposes exactly thirteen unique runtime callbacks:

- `event19_evaluate_eligibility`
- `event19_build_template`
- `event19_spawn_unit`
- `event19_reconcile_sustainment`
- `event19_get_equipment_token`
- `event19_publish_custom_equipment_tokens`
- `event19_get_presentation`
- `event19_evaluate_management`
- `event19_pay_management_action`
- `event19_refund_management_action`
- `event19_setup_derivative`
- `event19_remove_public_additions`
- `event19_cleanup_derivative`

The source scan found 247 core callback declarations, 247 unique provider/callback pairs, zero duplicates, and zero missing callbacks. Each provider also has one registration definition and one owner-side registration call.

`event19_get_presentation` returns the provider-owned family-name, request-cost, and sustainment-cost localisation-key tokens. The decision cache and delayed lifecycle records consume those tokens through `GetTokenLocalizedKey`; there is no numeric Event 19 family-name or cost selector. All 57 required provider presentation tokens resolve to English localisation keys.

## Dynamic equipment accounting

Ordinary Event 19 profiles 100-129 remain in the Event 19 constants because they belong to the event's ordinary Evolution III table. Custom profiles 130-148 are stable values in the owning provider constants:

- Event 012 elephant: 130
- Event 012 strange formations: 131-138
- CBRN Chaos Assault Battalion: 139-141
- Event 016 project forces: 142-148, with clone and Aryan clone sharing 142 under distinct family IDs

`event19_get_equipment_token` resolves each standing obligation through the recorded family/provider row. `event19_publish_custom_equipment_tokens` publishes every custom stockpile touched by a provider transaction. Event 19 snapshots those tokens before payment and after payment, de-duplicates shared tokens such as clone equipment, proves exact provider refund restoration, and proves that structural rollback preserves the post-payment stockpile state. Provider 508 retains its dedicated alien-landing materialize/commit/rollback API; the generic publisher observes its laser stockpile without applying a second debit or refund.

The 20 published custom equipment identifiers all resolve to concrete local equipment definitions: coal golem, elephant, eight Africa strange-force types, three CBRN protective types, clone, autonomous robot, paleogenetic, xenobiological, alien laser, teleportation, and temporal equipment. Generic infantry, support, and motorized obligations resolve through the shared standard-token bridge.

Selected-lot exact dynamic equipment tokens and amounts are country-persistent aligned arrays because decision availability is evaluated after the refresh effect returns. They are cleared by `infantry_spawn_clear_exact_profile_totals`, which is called by selected-lot refreshes, management cleanup, derivative cleanup, and annexed-country cleanup.

## New owner package coverage

Provider 523 is owned by Event 014 and covers all nine cannibal irregular combat units, including `cannibal_bone_riders`. It is spawn-only, requires the active Cannibalism system and absence of the cleanup-complete flag, uses exact owner totals of 7,350 manpower, 990 infantry equipment, and 35 motorized equipment before Event 19 scaling, and does not install Cannibalism country identity, stages, evolutions, counts, or progression on Event 19 actors.

The CXT inventory contains all 97 current sub-unit definitions: 88 in the static baseline plus nine Event 014 registrations through the owner-side wrapper and guarded `cannibal_bone_riders` extension. There are no duplicate unit definitions and no uncovered CXT tokens.

## Documentation contract

The future-unit obligation is synchronized across:

- `common/scripted_effects/chaosx_dynamic_effects.md`
- `docs/testing/chaosx_test_country.md`
- `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`
- `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`
- `docs/events/019_infantry_spawn/overview.md`
- `docs/events/019_infantry_spawn/systems/triggerable_scenario.md`
- `docs/specs/019_infantry_spawn_specs/README.md`
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_5_evolution_iv.md`
- `docs/specs/019_infantry_spawn_specs/review/decision_only_surface_addendum_2026-08-05.md`
- `docs/plans/019_infantry_spawn_plans/source_of_truth_map.md`

A future land sub-unit must receive one explicit disposition: existing provider combat component, new provider combat family, inseparable support attachment, or parent-owned support consumer. Its owner must also satisfy the CXT extension contract. A future family must not add an Event 19 family list, custom-equipment switch, scripted-localisation family switch, or second Event 19 registry file.

## Validation evidence

- Provider contract: 19 providers, 247 unique core callbacks, zero missing and zero duplicate provider/callback pairs.
- Registration reachability: one registration definition and one registration call for every provider.
- Equipment resolution: 20 published custom tokens, 20 concrete local definitions, zero missing.
- Presentation resolution: 57 owner presentation tokens, 57 English localisation keys, zero missing and zero duplicate Event 19 localisation keys.
- Unit/CXT census: 97 unique sub-unit definitions, 88 static CXT matches, nine dynamic Event 014 matches, zero uncovered.
- Source structure: all 22 changed provider, Event 19, constants, trigger, and localisation script files have balanced braces; no unsupported comparison operators occur in those files.
- Central-list removal: zero references to the removed custom Event 19 resource-profile keys and zero obsolete `event19_get_management_cost_display` or display-profile runtime identifiers.
- File ownership: exactly one Event 19 registry code file exists.
- HOI4 MCP: refreshed `hoi4.event_inspect` lint for `chaosx.nr19.1` returned `EVENT_INSPECTED_PARTIAL` and wrote `event-lint-a6101ec18545.json`; refreshed probability source discovery for `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt` returned `PROBABILITY_SOURCE_DISCOVERED` and wrote `probability-inspect-e35eee038249.json`.

The MCP event graph remains partial because helper expansion is bounded, and the installed probability adapter does not normalize the meta-dispatched provider pool. Those are evidence limits, not source fallbacks. The dedicated probability auditor remains required before the full Event 19 completion claim.

## Simplifications, fallbacks, and blockers

No gameplay simplification or fallback was introduced in this API tranche. Support-only definitions are not omitted: all 43 have an explicit engine-valid parent-owned disposition. The full Event 19 goal remains open until the required near-completion specialist audits and final completion audit are reconciled.
