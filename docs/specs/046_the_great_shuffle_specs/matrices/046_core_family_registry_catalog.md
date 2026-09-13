# Event 046 core family registry catalog

These are working stable family identities for design and audit.

The implementation can adjust syntax to repository convention after the owner maps every old reference and preserves save meaning.

Player-facing text never exposes these IDs.

## Baseline families

| Working family ID | Scope | Selection group | Status |
| --- | --- | --- | --- |
| `basic_stability` | Country | Baseline politics | Core safe |
| `basic_war_support` | Country | Baseline politics | Core safe |
| `basic_political_power` | Country | Baseline resources | Core safe |
| `basic_command_power` | Country | Baseline resources | Core safe |
| `basic_army_experience` | Country | Baseline military | Core safe |
| `basic_navy_experience` | Country | Baseline military | Core safe |
| `basic_air_experience` | Country | Baseline military | Core safe |
| `basic_reserve_manpower` | Country | Baseline reserves | Core safe |
| `basic_fuel_reserve` | Country | Baseline reserves | Core safe |

## Evolution I families

| Working family ID | Scope | Selection group | Status |
| --- | --- | --- | --- |
| `store_convoys` | Country | National stores | Core safe |
| `store_trains` | Country | National stores | Core safe |
| `store_equipment_<owner_family_id>` | Country | National stores | Owner-expanded core family |
| `store_special_<owner_family_id>` | Country | Owner stores | Owner adapter only |

Ordinary equipment families should come from an owner-controlled equipment-family provider.

Event 46 must not maintain one giant switch over every concrete token.

The provider supplies the stable family ID, compatible tokens, era scale, legal scope, and setter contract.

## Evolution II families

| Working family ID | Scope | Selection group | Status |
| --- | --- | --- | --- |
| `state_population` | State | Population | Core safe |
| `state_shared_factory_bundle` | State | Industry | Core dependency bundle |
| `state_infrastructure` | State | Buildings | Core safe |
| `state_airbase` | State | Buildings | Core safe |
| `state_anti_air` | State | Buildings | Core safe |
| `state_radar` | State | Buildings | Core safe under loaded feature |
| `state_land_fort` | State | Buildings | Core safe |
| `state_coastal_fort` | State | Buildings | Conditional-core |
| `state_naval_base` | State and province | Buildings | Conditional safe |
| `state_supply_hub` | State and province | Supply | Conditional safe |
| `state_railway_graph` | Province graph | Supply | Conditional safe |
| `state_resource_<resource_id>` | State | Resources | Owner-expanded conditional-core family |

Resource family IDs should come from the loaded strategic-resource registry and owner exclusions.

## Evolution III families

| Working family ID | Scope | Selection group | Status |
| --- | --- | --- | --- |
| `politics_party_popularity` | Country | Politics | Core safe normalized bundle |
| `politics_ruling_ideology` | Country | Politics | Conditional safe |
| `politics_law_<law_group_id>` | Country | Politics | Owner-expanded core or conditional family |
| `research_active_progress` | Active research object | Research | Conditional-core |
| `research_doctrine_progress` | Active doctrine object | Research | Conditional safe |
| `production_line_efficiency` | Production line | Production | Conditional-core |
| `production_line_progress` | Production line | Production | Conditional-core |
| `production_assigned_factories` | Production line | Production | Conditional safe |
| `land_unit_experience` | Land unit | Military | Core safe |
| `land_unit_planning` | Land unit | Military | Conditional-core |
| `land_unit_readiness_<surface_id>` | Land unit | Military | Conditional safe |
| `air_wing_experience` | Air wing | Military | Conditional safe |
| `ship_experience` | Ship | Military | Conditional safe |
| `commander_experience` | Commander | Military | Core or conditional |
| `commander_trait_progress_<trait_id>` | Commander | Military | Conditional safe |

Law groups, readiness surfaces, and trait progress families are supplied from loaded owner registries.

## Evolution IV families

External mechanics register under a stable owner namespace.

The design pattern is:

`owner_<owner_id>_<family_id>`

Examples of family roles include current legitimacy, influence, cohesion, pressure, preparedness, severity, local reserves, and active progression.

The family ID describes the mutable current value.

It must not name a historical ledger as if that ledger were mutable gameplay state.

## Evolution V structural candidates

| Working family ID | Scope | Selection group | Status |
| --- | --- | --- | --- |
| `structure_claim_relationship` | Country and state pair | Structural | Conditional safe |
| `structure_state_ownership` | State and country bundle | Structural | Conditional safe |
| `structure_state_control` | State and country bundle | Structural | Conditional safe |
| `structure_capital_location` | Country and state | Structural | Conditional safe |
| `structure_opinion_relationship` | Country pair | Structural diplomacy | Conditional safe |
| `structure_guarantee_relationship` | Country pair | Structural diplomacy | Conditional safe |
| `structure_access_relationship` | Country pair | Structural diplomacy | Conditional safe |
| `structure_land_unit_location` | Unit and province | Structural military | Conditional safe |
| `structure_air_wing_location` | Air wing and airbase | Structural military | Conditional safe |
| `structure_naval_location` | Fleet and port | Structural military | Conditional safe |

The catalog records accepted candidates.

Only families that pass the full structural contract enter the live registry.

## ID maintenance rules

- One family ID has one meaning for the life of a save.
- Owner-expanded IDs use stable owner identities, not array positions.
- A concrete equipment or resource token is not automatically a family.
- A renamed display label does not rename the family ID.
- A removed family keeps a migration or retirement record when old saves can reference it.
- A protected value never receives a placeholder family ID.
