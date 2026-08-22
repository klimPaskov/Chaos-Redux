# Implementation Surface Map

## Source-of-truth location

The accepted design should live under a system spec folder such as:

`docs/specs/chaos_warfare_system_specs/`

Working implementation handoffs, audits, and migration notes should live under:

`docs/plans/chaos_warfare_system_plans/`

The final repository naming can be adjusted to the project's system-spec convention. Do not place accepted design only in a loose prompt file.

## Existing gameplay files that require review

| Path | Ownership | Required change |
| --- | --- | --- |
| `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt` | grand doctrine | replace broad baseline bonuses, fill milestones, reveal system content |
| `common/doctrines/subdoctrines/land/chaos_warfare_infantry_subdoctrines.txt` | infantry track | replace flat stacks and old route names, unlock protected formations |
| `common/doctrines/subdoctrines/land/chaos_warfare_armor_subdoctrines.txt` | armor track | remove genocide terminology, add sealed crew, delivery, suppression tradeoffs |
| `common/doctrines/subdoctrines/land/chaos_warfare_combat_support_subdoctrines.txt` | fire support track | shell logistics, projector consolidation, persistent fire plans |
| `common/doctrines/subdoctrines/land/chaos_warfare_operations_subdoctrines.txt` | operations track | HQ, forecast, decon, biosecurity, no confirmed-use immunity |
| `common/technologies/chaosx_technologies.txt` | CBRN techs | gas-mask equipment, doctrine-only techs, complete agent roles, AI weights |
| `common/units/chaos_battalion.txt` | doctrine line unit | replace universal arsenal requirement and abusive stat profile |
| `common/units/livens_projector_support.txt` | chemical support | migrate agent-specific companies to one profile-driven unit |
| `common/units/chemical_tank_support.txt` | armored chemical support | consolidate variants, remove parachute use, add essential equipment |
| `common/units/equipment/modules/chemical_air_bomb_modules.txt` | air designer | payload handling, module balance, operation eligibility marker |
| `common/units/equipment/chemical_special_bombs.txt` | special chemical payload | align special raids and agent classes |
| `common/abilities/chemical_abilities.txt` | commander abilities | migrate general-wide buffs to HQ and order scope or compatibility wrappers |
| `common/combat_tactics.txt` | chemical tactics | AI weights, protection counters, doctrine gating, no free activation |
| `common/unit_leader/chaosx_traits.txt` | CBRN commander trait | align with Army HQ roles and new abilities |
| `common/ideas/cbw_ideas.txt` | national ideas | readiness, policy, civil defence, cleanup, lifecycle |
| `common/ideas/cbw_spirits.txt` | officer corps | mutually exclusive spirit families and bounded modifiers |
| `common/occupation_laws/chaosx_occupation_laws.txt` | occupation | remove or replace Concentration doctrine law, add bounded CBRN policies |
| `common/raids/chemical_special_raids.txt` | chemical raids | shared exposure helper, payload reservation, exact state results |
| `common/raids/biological_raids.txt` | bio raids | incubation, attribution, payload, countermeasure integration |
| `common/raids/categories/chaosx_raid_categories.txt` | raid UI | category visibility and profile text |
| `common/special_projects/projects/chemical_special_projects.txt` | advanced agents | full agent role, safety, delivery and tech gates |
| `common/special_projects/projects/biowarfare_main_projects.txt` | bio projects | safety and program choices, retain existing projects |

## Existing scripted systems

| Path | Required change |
| --- | --- |
| `common/scripted_effects/chemical_warfare_effects.txt` | become the shared chemical exposure orchestration layer or call a new documented helper file |
| `common/scripted_effects/chemical_ability_effects.txt` | reserve payload, calculate order coverage, call shared exposure, migrate to HQ abilities |
| `common/scripted_effects/chemical_air_bomb_effects.txt` | separate reliable raids from continuous estimator, consume payload, prevent idle-aircraft contamination |
| `common/scripted_effects/chemical_infantry_effects.txt` | replace current Chaos Battalion contamination and casualty hooks with equipped-role logic |
| `common/scripted_effects/chemical_livens_support_effects.txt` | consolidate profile handling |
| `common/scripted_effects/chemical_tank_shell_effects.txt` | consolidate chassis and agent profiles, call shared exposure |
| `common/scripted_effects/biowarfare_effects.txt` | incubation, outbreak, accident, evidence, payload and countermeasure alignment |
| `common/scripted_effects/chaos_meter_effects.txt` | only required if shared Deaths, Air Cleanliness, or Condemnation call contract changes |
| `common/scripted_triggers/cbw_triggers.txt` | readiness, protection, policy, support, target, AI and operation triggers |
| `common/on_actions/chaosx_on_actions_chemical_warfare.txt` | targeted combat and operation hooks, no broad new global pulse |
| `common/script_constants/chemical_warfare_constants.txt` | all chemical, protection, readiness, operation and death tuning |
| `common/script_constants/biowarfare_constants.txt` | outbreak, safety, spread and countermeasure tuning |
| `common/script_constants/chaos_meter_constants.txt` | only shared thresholds owned by Chaos Meter |
| `common/dynamic_modifiers/chemical_special_raid_modifiers.txt` | align raid outcomes and state effects |

## New recommended gameplay files

Exact names should follow repository convention.

| Proposed path | Content |
| --- | --- |
| `common/units/cbrn_regimental_support.txt` | consolidated protective, recon, pioneer, ammunition, medical, biosecurity and suppression companies |
| `common/units/cbrn_hq_support.txt` | six Army HQ support companies |
| `common/units/equipment/cbrn_protective_equipment.txt` | gas masks, decon equipment, instruments, optional medical equipment |
| `common/units/equipment/cbrn_payload_equipment.txt` | class payload, shell lots, air payload and conversion |
| `common/scripted_effects/cbrn_exposure_effects.txt` | shared action, exposure, deaths, contamination, evidence and Condemnation interface |
| `common/scripted_effects/cbrn_protection_effects.txt` | military and civilian coverage, filter consumption, distribution and cleanup |
| `common/scripted_effects/cbrn_hq_effects.txt` | Army HQ preparation, ability start, operation resolution and cleanup |
| `common/scripted_triggers/cbrn_triggers.txt` | shared policy, readiness, coverage, payload, target and AI triggers |
| `common/decisions/cbrn_warfare_decisions.txt` | program, protection, operations, containment and international responses |
| `common/decisions/categories/cbrn_warfare_categories.txt` | decision categories and scripted GUI entry |
| `common/scripted_guis/cbrn_warfare_scripted_guis.txt` | custom CBRN window if accepted |
| `common/scripted_localisation/cbrn_warfare_scripted_localisation.txt` | dynamic values, targets, requirements and status |
| `common/ai_strategy/cbrn_country_profiles.txt`, `cbrn_protection_production.txt`, `cbrn_regimental_support.txt`, `chemical_warfare_research.txt`, `chemical_warfare_cylinders.txt`, `chemical_warfare_livens.txt`, `chemical_warfare_tank_shells.txt`, and `biological_warfare_production.txt` | posture, research, protection, payload, unit, and production differentiation |
| `common/military_industrial_organization/organizations/cbrn_organizations.txt` | generic and country program designers if current schema uses this path |
| `common/military_industrial_organization/policies/cbrn_policies.txt` | only if verified and useful |

## Army HQ and regimental support references

The implementation agent must inspect the installed 1.19 files for exact locations. Do not infer the correct folder or schema from this plan.

Required local searches:

- Army HQ support company definitions
- HQ ability definitions
- `unit_modifiers`
- essential equipment blocks
- regimental support row units
- battalion adjusters
- company-gated abilities
- AI Army HQ templates and support assignment

## Equipment and enum surfaces

- `common/script_enums.txt` must register every new equipment bonus type.
- Equipment archetypes, models, modules, unit needs, technologies, text icons, GFX, and localisation must be updated together.
- Essential equipment must be defined for any unit with scripted or adjuster benefits.

## Country history

Review current additions in:

- Britain
- France
- Germany
- Soviet Union
- United States
- Italy
- Japan
- Poland
- Czechoslovakia
- Belgium
- Netherlands
- Commonwealth dominions and other assigned profiles

Remove identical offensive bundles. Add population and OOB-informed protective reserves and differentiated program stockpiles.

## Localisation

Likely files:

- `localisation/english/chaosx_abilities_l_english.yml`
- `chaosx_achievements_l_english.yml`
- `chaosx_decisions_l_english.yml`
- `chaosx_doctrines_l_english.yml`
- `chaosx_equipment_l_english.yml`
- `chaosx_ideas_l_english.yml`
- `chaosx_occupation_laws_l_english.yml`
- `chaosx_operations_l_english.yml`
- `chaosx_raids_l_english.yml`
- `chaosx_special_projects_l_english.yml`
- `chaosx_technologies_l_english.yml`
- `chaosx_units_l_english.yml`
- `chaosx_gui_l_english.yml` if the window uses shared GUI localisation

All files need UTF-8 with BOM and the repository key format.

## Interface and GFX

Likely existing registries:

- `interface/chaosx_doctrines.gfx`
- `interface/chaosx_techtree.gfx`
- `interface/chaosx_equipment.gfx`
- `interface/chaosx_subuniticons.gfx`
- `interface/chaosx_decisions.gfx`
- `interface/chaosx_ideas.gfx`
- `interface/chaosx_operations.gfx`
- `interface/chaosx_raids.gfx`
- `interface/chaosx_texticons.gfx`
- `interface/chaosx_achievements.gfx`

A new GUI and GFX file can own the CBRN window if the existing decision GUI is unsuitable.

## Documentation

Update or supersede:

- `CHAOS_REDUX_MECHANICS.md`
- all existing `docs/systems/cbrn_warfare/chemical_warfare/chaos_warfare_*.md`
- chemical and biological system docs
- `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md`
- Deaths and Air Cleanliness docs
- doctrine spreadsheet if still authoritative
- event docs and event catalog rows only where actual event behavior changes

## Zombie boundary

Do not rewrite the weaponized-zombie system as part of this goal. Only update shared helper call sites when required. Preserve:

- zombie special projects
- zombie cure
- zombie disease bombs
- weaponized zombie templates and leaders
- zombie event and world-threat behavior
