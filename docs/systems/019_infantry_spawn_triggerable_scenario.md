# Event 019 Triggerable Scenario Runtime

## Scope and registration

This package implements the Event 019 scenario, **The Unbidden Muster**, as registered Triggerable Scenario `SCN-013`. It accepts one of four types and four intensities, creates the complete military crisis synchronously, and exposes the exact actor roster needed by Event 019 achievement tracking.

The source specification proposed `SCN-008`, but Independence Wave owns that live identity, IDs 1 through 11 are occupied, and Event 020 reserves raw ID 12. The shared registry therefore assigns Event 019 the first collision-free identity, `SCN-013`. Its name-sort value is `5.75`, placing The Unbidden Muster after The Hunger Lines and before The World in Fury.

The current no-context registry/scenario reaudit and live-final AI, balance,
performance, isolation, scenario-safety, and exploit reaudit each report zero
P0, P1, or P2 findings. Every gameplay specialist gate is clean. The final
whole-event completion audit is also PASS, and Event 19 and SCN-013 are `Fully
Functional`. The owner-approved 7/18 regional-flag package is independently
approved for parent-owned package promotion. It contains 91 raw sources, 91 deterministic
spot masters, and 273 native/runtime output pairs, with visual/runtime rows
passing. The PASS handoff is
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`.
The machine JSON retains its immutable literal
`candidate_requires_independent_visual_review` processor-state value. Parent
workbook/catalog export and reconciliation are complete, Event 19 and SCN-013
now read `Fully Functional`, and parent package inventory is complete at 33/33
current files. The final completion audit
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_completion_audit_2026_07_18.md`
is PASS with P0/P1/P2 = 0, so no closure gate remains.

Scenario family discovery follows Chaos unit family contract version 4. Event 19
has exactly one dedicated registry code file,
`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`. A future
family adds one external registration row, its complete provider callbacks, and a
startup call in its existing integration surface. It requires no Event 19 family
list, localisation map, picture map, or registry-file edit.

## Direct caller contract

Player-facing callers should use `infantry_spawn_scenario_request_unregistered`. It persists the exact selections, opens confirmation event `chaosx.nr19.951`, and revalidates the launch when the player accepts. Scripted callers that deliberately require no confirmation may call `infantry_spawn_scenario_launch_unregistered` directly. Both entry points expect the same two exact temporary inputs:

```txt
set_temp_variable = {
	infantry_spawn_scenario_launch_type_input = constant:infantry_spawn_scenario.type_general_mutiny
}
set_temp_variable = {
	infantry_spawn_scenario_launch_intensity_input = constant:infantry_spawn_scenario.intensity_maximum
}
infantry_spawn_scenario_request_unregistered = yes
```

Valid type constants are `type_conventional_flood`, `type_arsenal_lottery`, `type_general_mutiny`, and `type_anomalous_rising`. Valid intensity constants are `intensity_low`, `intensity_medium`, `intensity_high`, and `intensity_maximum`. Fractional, out-of-range, duplicate, terminal-world, or already-running launches do not enter scenario setup.

The shared Triggerable Scenarios window stores the type in `triggerable_scenarios_infantry_spawn_type` and uses the common four-stop `triggerable_scenarios_intensity`. The pure `infantry_spawn_scenario_can_launch_from_triggerable_scenarios` trigger validates both persistent selectors against the exact four Event 019 constants plus the normal host, world-end, setup, and duplicate-launch gates. After the shared confirmation, `trigger_selected_chaosx_scenario` copies the live selectors into the direct runtime's temporary inputs and calls the raw `infantry_spawn_scenario_launch_unregistered` effect. It deliberately does not call the direct-caller confirmation wrapper, so one click never opens a second confirmation.

Anomalous Rising performs an additional preflight: at least one aligned, enabled, spawnable Event 019 family row must publish a complete derivative, parent-isolation, public-package, cleanup, and supported-visual contract. The Event 019 global initializer may initialize its ordinary ledgers and family registry while performing this check, but no launch or actor flag is frozen unless the preflight succeeds.

## Type packages

| Type | Formation package | Immediate political result |
| --- | --- | --- |
| Conventional Flood | At least one baseline, Evolution I, and Evolution II ordinary generation. Higher intensities add more Evolution II generations | Conventional dynamic breakaway or same-tag military government |
| Arsenal Lottery | Repeated Evolution II arsenal generations with the normal serious/strange equipment logic | Immediate arsenal revolt or takeover |
| General Mutiny | Exactly two to eight newly appended `scripted_scenario` lots, assigned only to the newly created claimant | Claimant takeover in the actor. Dynamic actors adopt the same exact lot, unit, and obligation rows as their claimant-breakaway private ledger |
| Anomalous Rising | Two to eight formations from one registered, derivative-capable Evolution IV family | Parent-isolated nonhuman derivative or same-tag anomalous takeover |

Conventional and Arsenal generation deliberately bypass registered-family selection. This prevents a naturally compatible zombie, ghost, golem, or future provider from leaking into either ordinary scenario type.

## Intensity model

| Intensity | Country share | Revolt-state coverage | Conventional/Arsenal generations | Random lots | Family formations | Fronts per splittable host | Extra adjacent wars | Actor manpower |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Low | 10% | 20% | 3 | 2 | 2 | 1 | 0 | 50,000 |
| Medium | 25% | 35% | 4 | 4 | 4 | 1 | 0 | 80,000 |
| High | 50% | 55% | 5 | 6 | 6 | 2 | 2 | 120,000 |
| Maximum | 100% | 80% | 6 | 8 | 8 | 3 | 8 | 180,000 |

The initiating country is always processed after passing the same live-host gate. Other existing, noncapitulated ordinary countries with at least one controlled passable state are sampled once during the explicit launch effect. There is no recurring daily, weekly, or monthly all-country action. Maximum leaves `world_end` untouched.

## Revolt and takeover resolution

Splittable countries use `infantry_spawn_scenario_build_coherent_revolt_region`. It anchors on a controlled, passable, noncapital mainland state and expands only through adjacent eligible states. The capital remains with the former parent. Each successful front creates a real dynamic country, transfers only the selected connected state region, adds those states as cores, gives the actor a capital and formation package, and begins an immediate annexation war against the former parent.

The scenario does not call `start_civil_war`, so a country already participating in a civil war can still receive an independent dynamic actor without nesting the civil-war effect. It also does not transfer existing divisions. All actor formations are freshly materialized through Event 019's authoritative generation, request, claimant, or family ledgers.

One-state and all-island countries use the designed same-tag takeover path. The package is an atomic append transaction: the runtime freezes the existing generation, selected-state, lot, template, component, unit, obligation, claimant, technology-lock, transfer, and achievement-ledger boundaries before materialization. Claimant promotion or government replacement, reserve manpower, scenario AI, scenario pressure, faction departure, and actor registration are applied only after the exact package and diplomacy gates are proved. Package success also requires `infantry_spawn_contributes_to_ordinary_evolution_history = no` while the scenario/setup bypass remains active. The lot, formation, claimant, request, incident, and management append helpers therefore contribute zero to ordinary Event 19 history. Shared history totals are neither snapshotted nor rewound. General Mutiny keeps the exact claimant government, while Anomalous Rising keeps its anomalous takeover identity. A pre-existing unaligned main or claimant ledger rejects the package before materialization and is never resized. The actor attempts an immediate war only against a valid adjacent country. The scenario never manufactures an inaccessible overseas war. Tiny islands therefore retain their state and existing transport position instead of creating a stranded zero-state or transportless micro-rebel.

Dynamic-country creation and the proved same-tag takeover are the only identity
paths. The scenario has no fixed-tag fallback.

High and Maximum actors can declare additional direct wars only against adjacent, existing, noncapitulated ordinary countries for which `can_declare_war_on` succeeds. Regional-war selection excludes all actors in the same scenario roster.

## Actor identity, AI, and parent isolation

The hidden actor event `chaosx.nr19.950` resets Event 019's `ROOT` to the new actor before invoking ledger, claimant, provider, and AI helpers. Confirmation uses `chaosx.nr19.951`. The initiating human receives setup-complete report `chaosx.nr19.952` or setup-failed report `chaosx.nr19.953` one day after synchronous resolution. Conventional actors receive the territorialist profile, Arsenal actors the gambler profile, General actors the counter-command-state profile, and Anomalous actors the anomalous-exploiter profile for Event 019 decisions. Each completed actor also freezes its scenario type and activates a self-removing AI strategy in `common/ai_strategy/019_infantry_spawn_scenario_ai_strategy.txt`: all actors prioritize an army and basic supply, while the four profiles separately favor conventional artillery, mobile arsenal production, claimant-command offense, or anomalous-host offense. The active parent and regional wars provide immediate military objectives.

For ordinary actors, the selected type is also a minimum committed evolution profile: Conventional Flood and Arsenal Lottery receive the complete Evolution I-II country-entry state, General Mutiny receives I-III, and Anomalous Rising receives I-IV. Fresh actors therefore keep exactly that applied profile after every setup flag is cleared. A pre-existing same-tag Event 019 participant retains any fully applied higher stage instead of losing live claimant, registry, or management transactions; the scenario fills only missing required stages. Once the country is marked as a scenario actor, `infantry_spawn_has_evolution_i` through `_iv` read this frozen applied set and ignore later global activations. Derivative actors use their private package and scrub every ordinary applied-stage flag.

General Mutiny creates exactly one dedicated scenario generation so it never reuses or mutates a pre-existing open generation row. It proves one materialized unit for each requested lot. Claimant creation's automatic first assignment is restored immediately. Only the newly appended random-lot tail is then assigned to the new claimant. The runtime freezes the exact claimant UID, archetype, originating generation UID, and former-parent country before calling `infantry_spawn_setup_claimant_breakaway_identity`. A scenario claimant breakaway adopts the already aligned generation, lot, template, component, unit, and obligation records as its derivative private ledger instead of clearing them. Anomalous Rising freezes family, provider, origin, and former-parent identity before calling the provider's `event19_setup_derivative` contract. The actor persists that exact family/provider pair, reloads the same active registry row, and refuses provider setup unless both identities match; later management and cleanup use the same stored pair.

Parent event actors carry `chaos_unit_family_parent_actor`. The shared host and
derivative boundary rejects that flag together with provider-specific parent tags,
original tags, flags, stages, and progression markers before actor creation. Event
19 clears the parent-isolation and public-package proofs before provider setup.
The provider sets a positive parent-isolation proof only after all shared and
parent-specific checks pass, initializes the private package, installs its own
public identity, leadership or council, family ideas, route package, and release
report, then sets the public-package proof. A nonhuman actor is rostered only after
both proofs and the full package succeed. Once its parent war is active, the actor
records exactly one derivative-revolt history row.

All one-person scenario and derivative leaders explicitly use `female = no`.
Technical council characters also use `female = no`, while their player-facing
names and identities remain institutional.

Anomalous actors use only the Event 019 derivative profile published by their
provider. They do not receive parent zombie, Death, or golem country flags and do
not fire any parent event chain. A future provider owns its extra parent-specific
checks, public setup, and cleanup callbacks beside its one external registration
row. The scenario needs no Event 19 list, map, or file edit.

## Idempotence, achievement roster, and cleanup

Each valid launch increments one frozen global serial. Every completed actor copies that serial and the initiating country identity, enters `global.infantry_spawn_scenario_actor_countries` exactly once, and is classified as the origin actor or a hostile actor. `global.infantry_spawn_scenario_hostile_actor_total` is frozen from those exact successful actors. Failed provisional actors are rolled back before roster insertion.

Only after the exact type, intensity, origin, and serial are frozen and every selected actor package has completed does the initiating country set `infantry_spawn_scenario_origin_pulse_active` and call `infantry_spawn_achievement_register_scenario_launch`. Registration schedules a lightweight daily continuity event that checks only scenario achievement evidence. The full Event 19 ledger and AI pulse remains on its ordinary cadence. A failed setup never arms scenario achievement history. Achievement victory uses `infantry_spawn_scenario_launch_has_no_surviving_hostile_actors`, which requires a nonzero hostile total and rejects any rostered hostile actor with the same serial that still exists without capitulating.

`infantry_spawn_triggerable_scenario_launched` is permanent idempotence history. `infantry_spawn_triggerable_scenario_setup_in_progress` and `_active` exist only during synchronous setup. Type-specific bypass, profile-lock, and forced-evolution flags are cleared on each actor and by a final bounded cleanup pass; only the proved ordinary actor's committed `_applied` stage flags remain. Setup completion is set only if every selected actor package completed. Provider or package failure sets `_setup_failed` and never selects a substitute route.

For a nonhuman scenario derivative, defeat and final teardown dispatch
`chaos_unit_family_provider_[provider]_event19_cleanup_derivative`. The provider
must remove all provider-owned public additions before setting the cleanup proof
for the requested phase. Event 19 retains ownership of tracked-formation proof,
private-ledger cleanup, and every common derivative surface. The phase commits
only when every required provider and formation proof exists. Cleanup resolves
the stored exact family/provider lifecycle row independently of its present-day
generation availability. Missing provider proof blocks the shared commit and
leaves the package in the existing invariant-safe cleanup path.

Dynamic-actor rollback deletes the fresh provisional actor army without refunds, proves that no division remains, and only then restores its states to the former parent with troop transfer disabled. Scenario and derivative identity exclude every package append from ordinary Event 19 history, so the package contributes zero shared lot or formation history and rollback never writes a frozen global value. A failed deletion proof retains the actor under a cleanup marker and schedules hidden actor-scoped event `chaosx.nr19.954`. Each retry again requires a zero-division proof before annexation and leaves all live shared counters untouched.

Same-tag rollback uses each newly appended unit's immutable `create_unit` ID plus its unique `Unbidden Muster <template UID>` name. It deletes only those units and templates without refunds, proves that every new unit identity and template is absent, and only then resizes every aligned ledger and auxiliary tail to its frozen boundary and restores the pre-transaction country counters and flags. It does not restore shared lot, formation, claimant, request, incident, or management totals: scenario materialization contributes zero to them, and an immediate or delayed retry must preserve changes made by other countries. Existing Event 019 rows and the country's ordinary army are never deletion targets. If the proof fails, hidden actor-scoped event `chaosx.nr19.955` retries the exact deletion while the ledger tails remain intact. A General Mutiny claimant that exists but cannot complete its same-tag takeover resolves through the specified failed-coup consequence before the technical rollback. No other failure is converted into a gameplay outcome.

## Implemented main-trigger integration

The ordinary global evolution flags are ignored while
`infantry_spawn_scenario_profile_locked` is present, while the explicit
per-country force flag remains authoritative. The implemented pattern applies
to `infantry_spawn_has_evolution_i`, `_ii`, `_iii`, and `_iv` in
`common/scripted_triggers/019_infantry_spawn_triggers.txt`. This prevents an
already-evolved world from overriding Conventional Flood's baseline and
organized passes while preserving a proved higher pre-existing same-tag stage.

## Localisation, icons, and assets

Event 019 localisation covers the direct-caller confirmation, setup reports, type and reach wording, launch-state tooltips, and the generated government-leader names `infantry_spawn_scenario_muster_council` and `infantry_spawn_scenario_unbidden_assembly`. Shared GUI localisation supplies the `#013` row, The Unbidden Muster name, four type descriptions, four type labels, four intensity impacts, and blocked-launch explanations. `common/scripted_localisation/019_infantry_spawn_scenario_scripted_localisation.txt` resolves the direct report values, while `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt` resolves the shared row and confirmation values.

Generic scenario governments resolve `GetInfantrySpawnScenarioActorArmyScene`
through a meta effect before creating their technical leader. Profiles 1, 2, and
3 are valid only for the exact 501, 502, and 503 family-provider pairs and use
their owned zombie, ghost, and golem massed-host scenes. An external provider must
explicitly register `provider_neutral_army`, value 999, unless a later supported
owned profile exists. Profile 999 and the conventional path use the dedicated
identity-neutral `GFX_portrait_infantry_spawn_unassigned_muster`, while arsenal
and mutiny use their scenario-matched army scenes. Any unknown positive profile
fails registration and every Event 19 consumer, so it never reaches this selector.
Profile 999 also rejects every family and provider ID reserved by profiles 1
through 3.
The scenario uses army or massed-host presentation only. No Event 19 scenario
government uses `GFX_portrait_communist_rebels` or a generic human or unknown
portrait. The direct reports reuse
`GFX_report_event_infantry_spawn`, and the shared window renders its existing
generic dynamic row and detail controls. The selector reuses sprites registered
in `interface/019_infantry_spawn.gfx`; no scenario icon or dedicated GUI window
is required.

The 20 claimant, 6 derivative, and 1 neutral fixed identity slots contain no
individual focal person. Their `portrait` identifier names are stable engine
terminology. This fixed-scene contract is separate from the 7/18 regional-flag
candidate, which the independent PASS handoff
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`
clears for parent-owned package promotion. The current source/runtime chain is
91 independent built-in ImageGen full-flag raws -> 91 deterministic 820x520
spot-colour masters -> 273 native PNGs -> 273 bottom-left-origin runtime TGAs.
The former 7/16 motif/composite pipeline and its validation/contact sheets are
archival superseded evidence. The machine JSON retains the literal
`candidate_requires_independent_visual_review` processor-state value.

## Source references

Implementation was checked against the offline wiki snapshot pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Division modding, and Unit modding. Official vanilla effect, trigger, dynamic-variable, script-concept, and script-constant documentation was treated as the primary engine reference. Vanilla dynamic-country creation and La Résistance's exact created-unit ID deletion pattern, plus current Chaos Redux nonhuman derivative, claimant-breakaway, and unit-ledger patterns, supplied concrete precedents.

## Future plans and suggestions

- Rebalance the country shares, state coverage, lots, fronts, and manpower after live scenario observation without changing the four package identities.
- Keep the coherent-region and dynamic-actor helpers scenario-owned. The natural claimant revolt still requires its separately approved exact recreate/delete division-ledger transaction and must not call this state-only transfer path as a substitute.
- Add a dedicated AI target-selection strategy only if testing shows active parent and adjacent wars do not keep actors engaged. It must preserve the no-impossible-overseas-war rule.
