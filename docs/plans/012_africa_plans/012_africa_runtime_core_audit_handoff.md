# Event 12 Africa core-runtime audit handoff

Status: narrow Event 012 implementation handoff after the core-runtime audit. Event 013 files were preserved unchanged and no commit was created at the parent request.

Audit date: 2026-07-29.

## Scope and source references

This audit covered Event 12 scripted effects, scripted triggers, decisions, on-actions, events, scripted localisation, high-chaos action constants, priority-member force consumers, and related localisation/GFX references.

Required repository guidance was read from `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/hoi4-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

The offline Paradox wiki core pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, event modding, decision modding, idea modding, and AI modding were consulted.

Vanilla documentation was consulted in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation`, including `effects_documentation.md`, dynamic-variable documentation, and the script-constant documentation.

Event 13 contracts were read from `docs/specs/013_natural_disasters_specs/matrices/013_disaster_call_contract.md`, `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-26_event013_dynamic_api_target_audit_handoff.md`, and `common/scripted_effects/013_natural_disasters_effects.txt`.

Event 6 identity constraints were read from `docs/events/006_independence_wave/systems/country_registry.md` and `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`.

## Findings

### Event 6 carrier and tag contract

`common/scripted_effects/012_africa_priority_member_effects.txt:19-126` records Event 12-owned `africa_priority_origin_*` flags through the canonical Event 6 predicates and does not write Event 6 origin markers or `liberation_origin`.

The direct overlap identities are Asante `DOX`, Oyo `DSX`, Sokoto `SOK`, Kanem-Bornu `DUX`, Kongo `COG` overlay-only, Luba `DYX`, Lunda `DZX`, Buganda `UGA`, Harar `HAR`, Kilwa `EMX`, Zulu `EQX`, and Merina `MAD`.

Manden `MLI`, Aksum `TIG`, Nubia `SUD`, and Great Zimbabwe `ZIM` are intentionally handled by the nonmatching vanilla-carrier predicate rather than asserted as same-identity Event 6 rows.

The Event 12 package registry therefore uses the Event 6 identity predicates for the overlap surface, with no new Event 6 tags found in that registration path.

Event 12 also contains ordinary vanilla African `original_tag` values for host playbooks, geography, and target eligibility. The phrase "only Event 6 tags" is therefore satisfied for the Event 6 overlap registry, not literally for every host and geography predicate in Event 12.

### Shared action runtime, cost, cooldown, and AI

High-chaos action IDs 67-76 are declared in `common/script_constants/012_africa_action_constants.txt` and use the shared profile, quote, validation, payment, mission, outcome, and cleanup pipeline in `common/scripted_effects/012_africa_action_effects.txt`.

The profile dispatch assigns dynamic target modes, duration bands, risk tiers, resource components, and action-cap rules for all ten high-chaos actions.

`africa_compute_action_quote`, `africa_select_action_for_quote`, and `africa_begin_quoted_action_against_target` recompute costs against the selected target and current host state rather than trusting a stale UI quote.

High-chaos selector decisions in `common/decisions/012_africa_decisions.txt` intentionally use `cost = 0` and `ai_will_do = { base = 0 }`; they only select the quoted action and are not the payment or AI execution surface.

AI still samples all ten high-chaos IDs through `africa_ai_pick_action_in_selected_family`, applies the high-chaos priority, selects a bounded target array, and invokes the same semantic validator and action-start path as human execution.

The shared cleanup restores capacities, clears action arrays and state flags, decrements the active count, and applies the configured 30-day target cooldown.

The cooldown flag now passes `var:africa_action_cooldown_days` in `common/scripted_effects/012_africa_action_effects.txt:6391-6393`, matching the vanilla SIA timed-flag precedent. Vanilla `effects_documentation.md` does not document the `days` child for `set_country_flag`; this remains a live parser/runtime risk worth checking by the parent in normal validation.

### Event 13 natural-disaster integration

Actions 69 `petition_the_rain` and 70 `defy_the_drought` now reuse the existing `africa_action_target` ledger for exact enemy-country calls through the public Event 013 `call_natural_disaster = yes` contract.

The host must be in Evolution III, at war, nature-authorized by a high-pressure priority package or documented covenant package, and outside the Event 012 hostile-nature cooldown.

The target must be the selected action target, distinct from the host, and at war with the host; no new target array, tag, or recurring world iteration was added.

`africa_reserve_natural_disaster_weapon_cost` reserves 35 political power and 10 command power before the shared action record is created, and `africa_cleanup_action` clears the reservation flag and active reservation variable.

`africa_call_hostile_natural_disaster_from_action` supplies caller type `hostile_actor`, Event ID 12, random family and family group, selected-country mode, the regular `natural_disaster_call_target_country` target, `natural_disaster_call_target_country_supplied = 1`, all three hostile-actor proof values at one, and bounded severity tiers of severe, regional, or catastrophic.

The helper snapshots Event 013 result, reject reason, sequence, family, primary-job, and skipped-primary outputs to host variables, marks the numeric resolved-primary-country target when accepted, starts a 180-day cooldown on every attempted call, and records a bounded wrath backfire on rejection or a 20 percent accepted-call backfire.

The random family remains constrained to the selected enemy country; Event 013 may reject it when that country has no eligible controlled state rather than widening the target.

The action record clears the target's prior accepted/rejected receipt flags before a new Rain or Drought action begins, keeping scripted result wording current.

`weaponise_fictional_pathogen` (73) remains a fictional disease action and is not mapped to a weather family because Event 013 has no pathogen family.

### Strange-force consumer gap

`awaken_stone_cohort`, `train_gorilla_heavy_infantry`, and `organise_pan_sappers` set one-time result flags and action outcome records, but no Event 12 consumer creates a formation or a sabotage network from those flags.

The Event 12 files contain no strange-force division templates, equipment archetypes, entity/model references, or explicit model availability gates for those three outcomes.

The existing common-reserve helper in `common/scripted_effects/012_africa_priority_member_force_effects.txt` is healthy for its sixteen grounded priority packages: it uses dynamic package names, vanilla infantry/cavalry/recon/engineer templates, bounded primary/reserve creation, and no custom entity/model dependency.

All sixteen package predicates are defined in `common/scripted_triggers/012_africa_priority_member_triggers.txt`, and the package template/primary/reserve localisation mappings are present in `common/scripted_localisation/012_africa_priority_member_scripted_localisation.txt` and `localisation/english/012_africa_priority_member_focus_l_english.yml`.

The strange-force rows therefore need a separate guarded consumer or an explicit unavailable-model disposition before their player-facing “formation created” results can be considered truthful.

### Periodic iteration and target persistence

Neither `common/on_actions/012_africa_rsa_on_actions.txt` nor `common/on_actions/012_africa_world_order_on_actions.txt` contains an `on_daily`, `on_weekly`, `on_monthly`, or equivalent recurring world hook.

The `every_country` passes in `012_africa_effects.txt` and `012_africa_world_order_effects.txt` are explicit prefire, roster-refresh, or post-unification census calls with caps and comments restricting them to event/decision/AI-triggered execution.

Human and AI target selection preserve the exact selected country through `africa_action_target`, `africa_selected_country_id`, `africa_selected_country_targets`, and the selected-target flag/array contract.

The active action cleanup clears target state flags, arrays, temporary variables, and the target cooldown; no regular event target is relied on as delayed persistent state.

### Localisation and GFX checks

All ten high-chaos action names, descriptions, and full/partial/failure result keys were found in the Event 12 localisation files.

The custom Event 12 decision and event GFX references resolve to definitions in the Event 12 interface `.gfx` files. The only unresolved names in the mod-only scan were generic vanilla GFX names such as `GFX_decision_generic_industry`, `GFX_decision_generic_break_treaty`, `GFX_report_event_generic_conference`, and `GFX_report_event_generic_african_unity`.

The expected central `docs/events/012_africa/overview.md` file is absent; the repository instead has separate Event 12 charter, evolution, and world-order event documents. This is a documentation-completeness gap for the parent documentation pass.

## Proposed helper map

The narrow implementation adds one local Event 012 effect and three Event 012 triggers while keeping the existing action ledger and the Event 013 public wrapper authoritative.

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `africa_natural_disaster_weapon_actor_is_eligible` | Host country trigger | Evolution III, priority-package ecological pressure, or covenant-nature flags | Boolean host authorization | No mutation | Event 012 action validator, Event 012 AI target candidate, Event 013 call preflight |
| `africa_natural_disaster_weapon_target_is_valid` | Selected target country trigger | Existing `africa_action_target`, host scope, war relation | Boolean exact enemy-target authorization | No mutation | Event 012 action validator and AI candidate branch |
| `africa_natural_disaster_weapon_cost_is_available` | Host country trigger | Political power, command power, cooldown and reservation flags | Boolean reserve authorization | No mutation | Event 012 action validator and AI candidate branch |
| `africa_reserve_natural_disaster_weapon_cost` | Host country effect | Action 69/70 ID and cost trigger | Temporary reserve marker copied to active target ledger | Deducts 35 PP and 10 CP and sets the in-flight reservation flag | `africa_begin_quoted_action_against_target` before shared quote payment |
| `africa_call_hostile_natural_disaster_from_action` | Resolved selected target country effect | Full action 69/70 result, active host target, reserved caller cost, exact enemy war relation | Random Event 013 call outputs copied to host history variables and accepted/rejected flags | Calls Event 013 without target widening, starts cooldown, marks resolved target, applies bounded backfire wrath | Full-result branch of `africa_apply_current_action_outcome` |
| `africa_strange_force_spawn_guard` | Host or registered actor country | strange-force family, action generation, cap, site/actor proof, template/model availability manifest | spawn eligibility, selected template/spec, disposition code | Never creates a placeholder formation; records unavailable/pending only when the approved disposition requires it | Stone cohort, Gorilla heavy infantry, and Pan sapper consumers |
| `africa_strange_force_finalize_result` | Owner country | guarded spawn result and action outcome | truthful full/partial/failure flags and force receipt | Clears one-time site/workshop markers, enforces cap/cooldown, and preserves audit receipts | Strange-force action resolution and cleanup |
| Existing `africa_priority_member_*starting_force_*` helpers | Priority-member country | registered package and bounded owned/controlled state | grounded template and primary/reserve divisions | Idempotent common-reserve setup | Action 102 registration and reinforcement only; no change recommended |

## Constants and tuning-table plan

Reuse Event 12 action duration, risk, cost, capacity, active-action, and cooldown constants for the shared action ledger.

`africa_natural_disaster` in `common/script_constants/012_africa_action_constants.txt` centralizes the caller Event ID, additional PP/CP reserve, 180-day hostile-nature cooldown, 20 percent backfire chance, and five-point wrath backfire.

Reuse Event 13 family, severity, target-mode, caller-type, proof, policy, scale, and reject-reason constants at the call site; Event 012 does not duplicate those IDs.

Severity selection is a bounded ladder: severe for `petition_the_rain`; regional for `defy_the_drought`, `africa_priority_member_full_promotion`, or `africa_covenant_write_warfare_doctrine`; and catastrophic for `africa_covenant_route_capstone`.

Do not use file-scoped `@` constants for values shared between Event 12 and Event 13 files.

## Event-target and cleanup plan

Preserve the Event 12 host target and the exact `africa_action_target` country target through the immediate call chain; `africa_call_hostile_natural_disaster_from_action` saves that country as the regular `natural_disaster_call_target_country` target before calling the public wrapper.

For selected-country or selected-state calls, set the matching supplied-target proof variable and test Event 13 numeric proof outputs rather than trusting a stale regular target.

Clear Event 013 temporary inputs through the public wrapper, retain only accepted/rejected result and numeric proof receipts in host variables, and rely on the regular event target lifecycle rather than creating a global target.

Keep `africa_cleanup_action` responsible for action-generation checks, target flags, state project markers, arrays, host capacities, active counts, and the dynamic recent-target cooldown.

A monthly calamity capstone, if implemented later, must be a bounded host-owned delayed callback with strict war/target revalidation and war-end cleanup; this tranche does not create an `on_monthly` world iteration.

## Migration plan

Keep the existing profile, quote, action record, AI selection, mission, and cleanup kernels as the source of truth.

Reserve the caller-side nature cost in `africa_begin_quoted_action_against_target`, copy that marker into the existing action ledger, and invoke the Event 013 helper only from the full-result path for actions 69 and 70.

Route human and AI actions through the same action validator and helper while preserving the existing bounded target arrays and exact selected-country event target.

Do not reinterpret action 73 as a weather call; a future pathogen integration needs a separate Event 013 family or approved public contract.

Add strange-force consumers only after a reviewed division-template/model manifest exists, or record an explicit unavailable-model disposition and revise the player-facing result text.

Preserve the Event 6 carrier predicates and the grounded priority-member common-reserve helpers during migration.

## Changed files and identifiers

- `common/script_constants/012_africa_action_constants.txt`: added `africa_natural_disaster` caller-cost, cooldown, and backfire tuning.
- `common/scripted_triggers/012_africa_triggers.txt`: added `africa_natural_disaster_weapon_actor_is_eligible`, `africa_natural_disaster_weapon_cost_is_available`, and `africa_natural_disaster_weapon_target_is_valid`.
- `common/scripted_triggers/012_africa_ai_profile_triggers.txt`: routed actions 69/70 through the exact hostile-nature candidate branch and excluded them from generic fallback.
- `common/decisions/012_africa_decisions.txt`: hides the two hostile-nature selectors unless the host has a nature package and is at war; cost and exact-target checks remain in the shared execution validator.
- `common/scripted_effects/012_africa_action_effects.txt`: added `africa_reserve_natural_disaster_weapon_cost`, active-ledger reservation and cleanup, strict action 69/70 validator gates, `africa_call_hostile_natural_disaster_from_action`, Event 013 public-call inputs/outputs, cooldown/backfire handling, and the existing timed-target cooldown `var:` safety patch.
- `common/scripted_localisation/012_africa_scripted_localisation.txt`: routes accepted/rejected hostile-nature receipts into the existing Event 012 result description surface.
- `localisation/english/012_african_union_l_english.yml`: documented hostile-war nature calls, extra ritual payment, cooldown/backfire, and accepted/rejected call wording.
- `docs/events/012_africa/natural_disaster_weapons.md`: helper contract, tuning, target lifecycle, AI parity, UI reuse, and limitations.
- `docs/plans/012_africa_plans/012_africa_runtime_core_audit_handoff.md`: implementation handoff and audit record.

No Event 013 source file, strange-force formation, model/entity, new decision, focus, interface asset, portrait, workbook, or tag was added.

## Validation evidence

- A repository search confirmed the Event 012 call site and all required public Event 013 inputs are present, while `common/scripted_effects/013_natural_disasters_effects.txt` and the Event 013 contract files remain unchanged.
- Event 12 high-chaos IDs 67-76 were found in the profile dispatch, semantic validator, AI family picker, full/partial/failure outcome kernels, scripted localisation, and player-facing localisation.
- Event 12 on-actions contain no periodic world hook; explicit `every_country` calls are confined to event/decision/AI roster or one-shot census paths.
- The sixteen priority-member package predicates and their dynamic template/formation names were cross-checked against their trigger and localisation definitions.
- Custom Event 12 GFX references resolve to the mod’s `.gfx` definitions; generic vanilla GFX references were excluded from the missing-asset conclusion.
- Vanilla SIA examples were checked for `set_country_flag = { ... days = var:... }` before the cooldown syntax patch.
- Static call-site review confirmed the selected enemy is saved from `event_target:africa_action_target`, never selected from a second array, and is guarded by a host war relation and `has_war_with = ROOT`.
- Static output review confirmed result/reject/sequence/family/job/skipped outputs are copied before the action cleanup and that the numeric resolved-primary-country proof gates the target flag.
- Read-only `hoi4_event_inspect` lint was run for `chaosx.nr12.220` and `africa_priority_member.1200`. Both returned `EVENT_INSPECTED_PARTIAL` with artifact resources in workspace `mod_chaos_redux_ea3b2d67c2c0`; validation was false because the large workspace analysis deferred helper/lifecycle passes, with no blocking diagnostics.

HOI4 was not launched and no in-game runtime validation was performed.

## Risks, unsupported fields, and blockers

The Event 013 integration is implemented for actions 69 and 70 only; fictional-pathogen delivery remains a separate unresolved design because Event 013 has no pathogen family.

The strange-force consumers are missing, so their “formation created” localisation is not backed by a unit template, model gate, or `create_unit` call.

The `set_country_flag` timed-duration child is incompletely documented by vanilla; the `var:` form is supported by vanilla SIA but still merits normal live validation for both the existing target cooldown and new hostile-nature cooldown.

The MCP lint reports are partial and cannot substitute for a focused Event 12 load check.

The missing central `docs/events/012_africa/overview.md` file should be resolved by the parent documentation pass or explicitly superseded by a source-of-truth map.

No fallback or silent simplification was introduced. The implementation reuses actions 69 and 70, preserves the Event 012 ledger, and reports the action 73 pathogen boundary and existing strange-force consumer gap explicitly.

## Release-candidate correction (2026-07-29)

The selected-enemy Event 013 disaster-call path for actions 69 and 70 is accepted release-candidate evidence. The Event 12-only wrapper call preserves the exact selected enemy and result outputs, the Event 013 source files remain unchanged, and the final registration scan reports no active blocker.

The strange-force consumer statement above is superseded for the current candidate. Actions `awaken_stone_cohort`, `train_gorilla_heavy_infantry`, and `organise_pan_sappers` have custom formation consumers that are runtime-gated by `africa_strange_formation_package_ready`; the gate remains closed until the approved formation, model, and entity package exists.

The central source-of-truth document now exists at `docs/events/012_africa/overview.md`; the earlier absence note is historical and is superseded by that document and the documentation cleanup handoff.

The sixteen grounded priority-member common-reserve packages remain separate from the deferred strange-force package and should not be conflated during audit or release review.
