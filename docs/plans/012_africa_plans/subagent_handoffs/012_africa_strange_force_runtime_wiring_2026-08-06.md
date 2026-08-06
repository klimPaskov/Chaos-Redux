# Event 012 strange-force runtime wiring handoff

Date: 2026-08-06.

Owner: `chaosx_scripted_system_architect`.

## Scope and disposition

This handoff wires the eight Event 012 strange-formation consumers without changing the package-readiness decision.

The shared global gate `africa_strange_formation_package_ready` remains unset and no code in this change sets it.

The runtime therefore refuses every attempted formation until the global gate and all four per-family manifest receipts are supplied.

No new country tags, fictional package tags, generic unit fallback, recoloured vanilla entity, or Event 019 provider shortcut was added.

## Files changed

- `common/script_constants/012_africa_strange_force_constants.txt` adds the integer dispatcher schema `africa_strange_force_kind` with stable IDs for the eight families.
- `common/scripted_effects/012_africa_action_effects.txt` adds the guarded spawn/finalise helpers, eight exact wrappers, natural-disaster Wardens handoff, and Action 67, 68, 73, 74, 75, and 76 call sites.
- `common/scripted_effects/012_africa_focus_route_effects.txt` adds the Living Rivers route consumer at Covenant node 10 when an existing river or lake overlay is active.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_strange_force_runtime_wiring_2026-08-06.md` records the helper contract, gates, call sites, cleanup, validation, and blockers.

`common/scripted_effects/012_africa_priority_member_effects.txt` and `common/decisions/012_africa_decisions.txt` were intentionally not changed.

The existing decision selectors and Action 74-76 validator continue to require the unset shared package gate.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `africa_strange_force_spawn_guard` | Country | Temporary `africa_strange_force_requested_kind`; global package gate; family manifests; owned controlled state | Temporary `africa_strange_force_spawn_result` and refusal state | Checks global cap, grants hidden bridge technology, adds the family equipment stockpile, creates one exact division template and unit, and never substitutes a generic formation | All eight family wrappers |
| `africa_strange_force_finalize_result` | Country | Guard result and requested family | Persistent receipt or explicit runtime-refusal flags | Increments `global.africa_strange_force_formation_count`, writes the permanent one-time receipt, and applies the existing 30-day action cooldown | Guard only |
| `africa_strange_force_spawn_stone_cohorts` | Country | None beyond current country scope | Guard result | Requests `stone_cohorts` and its exact model/entity consumer | Full Action 74 semantics |
| `africa_strange_force_spawn_gorilla_heavy_infantry` | Country | None beyond current country scope | Guard result | Requests `gorilla_heavy_infantry` and its exact model/entity consumer | Full Action 75 semantics |
| `africa_strange_force_spawn_pan_sappers` | Country | None beyond current country scope | Guard result | Requests `pan_sappers` as the exact support subunit | Full Action 76 semantics |
| `africa_strange_force_spawn_riverborn` | Country | Covenant route plus an existing river/lake overlay | Guard result | Requests `riverborn` from the Living Rivers route consumer | Covenant route node 10 |
| `africa_strange_force_spawn_forest_giants` | Country | Full Action 68 target | Guard result | Requests `forest_giants` after the bounded Green compact result | Full Action 68 semantics |
| `africa_strange_force_spawn_oracle_recon` | Country | Full Action 67 target | Guard result | Requests `oracle_recon` after the Oracle network result | Full Action 67 semantics |
| `africa_strange_force_spawn_disaster_wardens` | Country | Natural-disaster caller country | Guard result | Requests `disaster_wardens` as an exact support subunit | Accepted Action 69/70 natural-disaster bridge |
| `africa_strange_force_spawn_plague_carriers` | Country | Full Action 73 target | Guard result | Requests `plague_carriers` after the bounded pathogen result | Full Action 73 semantics |
| `africa_strange_force_spawn_disaster_wardens_after_natural_disaster` | Active action target country | Action 69/70 and `africa_natural_disaster_call_accepted_recorded` | None | Uses the existing `africa_natural_disaster_action_actor` global event target when present, otherwise the existing host target, and then calls the Wardens wrapper | `africa_apply_current_action_outcome` after `africa_call_hostile_natural_disaster_from_action` |

The guard uses static branch definitions rather than a dynamic unit-name or entity fallback so every consumer remains auditable against the gameplay handoff.

## Exact formation contracts

| Family | Hidden bridge technology | Equipment stockpile | Template and exact subunit consumer | Entity/model token |
| --- | --- | --- | --- | --- |
| Stone Cohorts | `africa_stone_cohorts_tech` | `africa_stone_cohorts_equipment_1`, 160 | `Africa Strange Stone Cohorts`, two `stone_cohorts` regiments | `chaosx_stone_cohorts` |
| Gorilla Heavy Infantry | `africa_gorilla_heavy_infantry_tech` | `africa_gorilla_heavy_infantry_equipment_1`, 240 | `Africa Strange Gorilla Heavy Infantry`, two `gorilla_heavy_infantry` regiments | `chaosx_gorilla_heavy_infantry` |
| Pan Sappers | `africa_pan_sappers_tech` | `africa_pan_sappers_equipment_1`, 180 | `Africa Strange Pan Sappers`, one vanilla `infantry` carrier plus the exact `pan_sappers` support slot | `chaosx_pan_sappers` |
| Riverborn | `africa_riverborn_tech` | `africa_riverborn_equipment_1`, 220 | `Africa Strange Riverborn`, two `riverborn` regiments | `riverborn` |
| Forest Giants | `africa_forest_giants_tech` | `africa_forest_giants_equipment_1`, 180 | `Africa Strange Forest Giants`, two `forest_giants` regiments | `chaosx_forest_giants` |
| Oracle Recon | `africa_oracle_recon_tech` | `africa_oracle_recon_equipment_1`, 120 | `Africa Strange Oracle Recon`, one vanilla `infantry` carrier plus the exact `oracle_recon` support slot | `chaosx_oracle_recon` |
| Disaster Wardens | `africa_disaster_wardens_tech` | `africa_disaster_wardens_equipment_1`, 160 | `Africa Strange Disaster Wardens`, one vanilla `infantry` carrier plus the exact `disaster_wardens` support slot | `disaster_wardens` |
| Plague Carriers | `africa_plague_carriers_tech` | `africa_plague_carriers_equipment_1`, 140 | `Africa Strange Plague Carriers`, two `plague_carriers` regiments | `plague_carriers` |

The vanilla `infantry` entries in the three support-only templates are structural carrier slots required by the division-template contract.

They do not replace the custom support consumer, do not supply a generic formation path, and cannot run while the custom manifest gate is closed.

All eight templates are locked with `is_locked = yes` and `force_allow_recruiting = no` so the exact consumer remains the guarded runtime spawn rather than a duplicate manual training path.

The guard applies `africa_strange_force.formation_equipment_factor`, `formation_manpower_factor`, and `formation_experience_factor` through the vanilla `create_unit` factor fields.

## Gate, cap, and refusal contract

Every branch requires `africa_strange_formation_package_ready` plus these four global receipts for its family:

- `africa_strange_force_<family>_model_manifest_ready`.
- `africa_strange_force_<family>_entity_manifest_ready`.
- `africa_strange_force_<family>_counter_manifest_ready`.
- `africa_strange_force_<family>_audio_manifest_ready`.

The package owner must set those receipts only after the corresponding model, entity/action, counter, and audio manifests pass their independent rights and runtime reviews.

The global counter `global.africa_strange_force_formation_count` is initialized to zero when absent and is incremented only after a successful exact unit creation.

The counter must remain below `constant:africa_strange_force.formation_cap` (8) before any branch can grant technology, stockpile, template, or unit effects.

Missing gate, manifest, owned-state, cap, permanent receipt, or cooldown proof sets `africa_strange_force_runtime_refused` and the corresponding family-specific `africa_strange_force_<family>_runtime_refused` flag.

Refusal never sets `africa_strange_formation_package_ready`, a bridge technology, a stockpile, or a placeholder formation.

## Event-target and cleanup plan

The guard saves its current country scope as the short-lived `africa_strange_force_spawn_owner` event target so nested actor calls cannot accidentally resolve `ROOT` back to the active action target.

Action formations execute in the active action target country, matching the existing `africa_create_action_record` and `africa_apply_current_action_outcome` scope contract.

Disaster Wardens run only after the existing `africa_call_hostile_natural_disaster_from_action` API records `africa_natural_disaster_call_accepted_recorded` on the active target.

When `africa_natural_disaster_action_actor` exists, Wardens are created on that exact registered actor; the existing host event target is the only fallback scope when no actor target exists.

No new event target or world iteration was introduced.

The global formation counter and one-time receipts intentionally survive action cleanup because they represent lifetime formation creation rather than an active mission pointer.

The timed family cooldown reuses `constant:africa_action_threshold.cooldown_days` (30 days) through a temporary duration variable, following the existing timed-flag pattern.

Existing `africa_cleanup_action` and priority-member cleanup remain authoritative for action targets, natural-disaster actor targets, reserves, and mission lifecycle.

## Migration from duplicated action logic

Actions 74, 75, and 76 no longer write their old `*_raised_once` proof flag unconditionally.

Each action first calls its exact wrapper and writes the legacy success flag only when `africa_strange_force_spawn_result` is positive.

Actions 67, 68, and 73 retain their existing bounded outcome flags and add the exact Oracle, Forest, and Plague consumers after those outcomes.

Action 69/70 natural-disaster resolution remains unchanged; Wardens are a post-acceptance consumer attached after the existing API call.

Living Rivers has no direct action and is consumed only from Covenant route node 10 when the route and an existing river/lake overlay provide the region proof.

The existing Event 019 provider remains untouched and is not used as a fallback or duplicate consumer.

## Inspection and validation evidence

The required offline wiki pages and vanilla documentation for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, divisions, units, script constants, and `create_unit`/`division_template` precedents were consulted before editing.

The Event 012 read-only MCP lint returned partial large-workspace evidence with no blocking diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e725ef767826c3f34473841ca989f672fca234856769ba689e5799dc52d6ed18/387eb36af049c3dcf278088db4a97ced13ccccd834f77358fe11a4e763d42506/event-lint-944ba605ebe4.json`.

The event artifact deferred workspace-wide scripted-helper projections and retained a cached revision, so it is not treated as direct proof of the newly inserted helper internals.

The technology read-only MCP lint for `africa_stone_cohorts_tech` returned partial large-workspace evidence with no blocking diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a9dbc4408744030e72fe53911436385592fdc53a355b289e0e22e5eea26b664/17151611c18f0716743e4847cb4206ebb93e9dacdade026a91c5b033429f5a3a/technology-lint-c4729570afa6.json`.

The random-list probability inspection was rerun after the patch and returned a complete source inspection with no diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/116e4e83003bd95754551d18f553f0aaa0ebdda5905ae30fd6ad76bb3b2abad9/6885e7b66e7318d05f952de291330b651853aabd9ed9ddf710e471ec07370018/probability-inspect-2d45c4e3f8b0.json`.

The probability inspection reports the existing `random_list` source as incomplete with one unresolved candidate, but this change does not alter weights or add a probability-bearing helper, so no probability compare pass was required.

A local structural audit confirmed balanced Clausewitz braces and quotes in all three touched gameplay/constant files.

A local cross-reference audit confirmed all eight bridge technologies, equipment IDs, subunit IDs, and entity/model tokens resolve against the peer gameplay definitions.

The same audit confirmed no package-readiness setter, new country-tag assignment, or unsupported `<=`/`>=` operator was added.

Hearts of Iron IV was not launched; live consumer validation remains parent/user-owned.

## Blockers and known limitations

All six model handoffs inspected for Stone Cohorts, Gorilla Heavy Infantry, Pan Sappers, Riverborn, Forest Giants, and Oracle Recon remain blocked or missing their approved model/entity/audio/counter manifests.

The Disaster Wardens and Plague Carriers manifests are likewise not present in the current repository acceptance state.

Because the manifest receipts and shared package gate remain absent by design, all eight runtime branches are dormant and will record explicit refusal if called.

The three support-only templates rely on a vanilla `infantry` carrier solely to satisfy the support-slot schema; the exact custom support IDs remain the consumer and no fallback formation is created.

No GFX, entity, animation, counter, audio, rights, or bulk localisation work is included in this runtime handoff.

The parent package owner must supply and review the per-family manifest receipts before setting the global package gate and exercising the eight consumers.
