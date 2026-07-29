# Event 013 dynamic geography and public-call architecture handoff

> Historical audit snapshot, 2026-07-11. The gaps and verdict below describe the pre-implementation state and are retained for audit history. The later geography/API tranches replaced proxy-only eligibility with the curated physical-domain registries and revalidation paths documented in `docs/events/013_natural_disasters/overview.md`, `013_implementation_validation_notes.md`, and the final completion audit. Do not use this handoff as the current implementation status.

Date: 2026-07-11
Mode: read-only scripted-system architecture audit
Owner: parent implementation agent
Gameplay, localisation, asset, spreadsheet, and source-spec edits by this subagent: none

## Historical executive verdict

Event 013 does not yet satisfy the corrected geographic contract.

The current selector still treats infrastructure, resources, agriculture, coastal status, and prior disaster history as substitutes for physical geography. In particular:

- volcanic eruption and massive eruption can still select a generic resource-producing or coastal state;
- heat wave has an Event 051 overlap guard but no climate guard;
- earthquake, flood, winter, storm, fire, slope, ash, and lahar families do not have authoritative physical domains;
- repeated impacts can bypass the family-target predicate;
- regional spread checks generic impact validity rather than family geography;
- physical chain follow-ups can change the current state to tsunami, lahar, or wildfire without revalidating that state;
- a scheduled impact is not revalidated against the physical family domain.

The current public-call correction is sound on the target-proof and retry-order issues inspected in the final live snapshot:

- selected-region resolution now scores eligible states instead of accepting an arbitrary random state;
- random-family retry is no longer artificially limited to random-valid and selected-country modes;
- natural_disaster_target_candidate_saved prevents a stale state event target from proving a new attempt;
- natural_disaster_target_country_candidate_saved prevents a stale country event target from feeding a new state selection;
- natural_disaster_select_state_from_target_country requires current-attempt country proof;
- natural_disaster_planned_origin_family and a random abnormal path lock are committed only after a family/target pair resolves.

The broader API/system contract is still incomplete:

1. The public result does not expose the resolved primary family/state/country, making the reusable API weaker than its target-resolution promise and forcing callers to inspect internal state.
2. Repeat, spread, chain, and execution-time paths remain able to bypass any new entry-time geography rule unless they are changed in the same implementation.
3. Hard physical geography has not yet replaced proxy eligibility.

The current decision-category implementation uses the correct vanilla triggered-picture form and the correct existing sprites. Its predicates are not mutually exclusive. With two active families, two or more picture entries match; the final recovery entry always matches. Vanilla's only directly relevant precedent uses mutually exclusive government predicates, so neither first-match precedence nor an overlapping always fallback is proven. The map must use one authoritative presentation family or otherwise make every entry mutually exclusive.

## Sources consulted

### Repository authority

- AGENTS.md
- .agents/skills/chaos-redux-subagents/SKILL.md
- .agents/skills/chaos-redux-events/SKILL.md
- .agents/skills/hoi4-decisions-missions/SKILL.md
- every file under docs/specs/013_natural_disasters_specs/
- the live Event 013 constants, triggers, effects, decisions, category definitions, scripted localisation, localisation, GFX, on-actions, GUI, dynamic API, and system documentation

### Required offline wiki

The following local pages were consulted:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- Interface modding
- State modding
- Map modding

Relevant engine conclusions:

- regular event targets persist through the current effect chain and fired events, but there is no ordinary clear effect for them;
- random_state and related random-scope effects honor their limit block;
- region = id is a state-scope strategic-region test;
- decision-category pictures require category description localisation to display;
- state and strategic-region map membership must be represented with map identifiers when no state-scope runtime trigger exposes the required physical property.

### Official vanilla documentation

Consulted:

- documentation/script_concept_documentation.md
- common/script_constants/documentation.md
- documentation/effects_documentation.md
- documentation/triggers_documentation.md
- documentation/dynamic_variables_documentation.md

Important constraints:

- script constants can centralize scalar tuning but cannot hold trigger-token lists;
- temperature is not a general state-scope trigger;
- has_terrain is documented for country scope and cannot be used as a reliable state terrain classifier;
- no generic documented state-to-strategic-region numeric output exists for this public API;
- save_event_target_as and has_event_target do not prove that the event target was written by the current attempt.

### Vanilla category precedent

Hearts of Iron IV/common/decisions/categories/JAP_decision_categories.txt, JAP_imperial_influence_decision_cat, uses:

~~~txt
picture = {
	GFX_decision_cat_picture_JAP_imperial_influence_hirohito = {
		OR = {
			has_government = neutrality
			has_government = fascism
		}
	}
	GFX_decision_cat_picture_JAP_imperial_influence_diet = {
		OR = {
			has_government = democratic
			has_government = communism
		}
	}
}
~~~

This proves triggered category pictures are supported. It does not prove behavior when several picture triggers are true. The two vanilla predicates are mutually exclusive.

### Vanilla map baseline

The installed vanilla baseline is Operation Postern v1.19.2.0.a729 (d245).

- strategic-region ids are contiguous from 1 through 304 in this build;
- Chaos Redux currently has no history/states overrides, so vanilla state and strategic-region data are the active map basis;
- strategic-region weather is defined in map/strategicregions;
- state/province membership is defined through history/states, map/strategicregions, and map/definition.csv.

The following current Siberian/cold strategic regions are a mandatory minimum heat exclusion:

138, 147, 148, 149, 150, 151, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266.

Their vanilla weather includes winter minima from -31 to -55 Celsius. This list is a minimum correction, not the complete cold-domain registry.

Vanilla regions with an explicit positive sandstorm weather value are:

28, 126, 127, 128, 134, 162, 182, 183, 195, 196, 216, 225, 232, 236, 237, 238, 254, 289.

Those ids are a useful arid-domain input. They are not by themselves a complete dust eligibility definition because the target must still be a populated, non-impassable land state with appropriate open/arid exposure.

## Required architectural invariant

Every physical impact must pass the same two layers:

1. runtime validity: the state exists, is populated, is not impassable, has a valid responsible country, and is not blocked by scheduling/aftermath policy;
2. immutable family geography: the state belongs to the physical domain for the resolved family.

Scoring is applied only after both layers pass.

No score, resource, building, history flag, infrastructure value, population density, or coastal status can rescue a state that fails immutable family geography.

This invariant must hold at:

- public call resolution;
- repeat resolution;
- path/corridor continuation;
- regional spread;
- chain-family selection;
- chain-target selection;
- delayed impact execution;
- control-transfer queue handling.

## Geography registry

### File and data ownership

Create:

common/scripted_triggers/013_natural_disasters_geography_triggers.txt

The file header should state:

- it is structural map data for vanilla 1.19.2;
- region lists come from vanilla strategic-region weather;
- state lists come from vanilla state/province membership plus reviewed real-world hazard placement where vanilla has no volcano/fault/river token;
- map ids are identifiers, not tuning values;
- unclassified states fail closed for restrictive families;
- the registry must be reviewed whenever the vanilla map changes.

Do not set geography flags on startup. Do not add a daily, weekly, or monthly world scan. Geography should be queried through state-scope scripted triggers.

Use explicit state = id and region = id tests. Scalar thresholds and retry limits belong in script constants. Token lists do not.

### Low-level trigger identifiers

The registry should expose these state-scope predicates:

- natural_disaster_state_is_seismic_zone
- natural_disaster_state_is_flood_exposed_zone
- natural_disaster_state_is_tropical_storm_basin
- natural_disaster_state_is_windstorm_zone
- natural_disaster_state_is_tornado_zone
- natural_disaster_state_is_convective_storm_zone
- natural_disaster_state_is_hail_zone
- natural_disaster_state_is_cold_zone
- natural_disaster_state_is_heat_zone
- natural_disaster_state_is_arid_zone
- natural_disaster_state_is_drought_zone
- natural_disaster_state_is_wildfire_fuel_zone
- natural_disaster_state_is_slope_zone
- natural_disaster_state_is_dry_slope_zone
- natural_disaster_state_is_wet_slope_zone
- natural_disaster_state_is_volcanic_vent_zone
- natural_disaster_state_is_volcanic_plume_zone
- natural_disaster_state_is_lahar_zone
- natural_disaster_state_is_ocean_exposed_coast
- natural_disaster_state_is_storm_surge_coast
- natural_disaster_state_is_storm_corridor_zone
- natural_disaster_state_is_massive_eruption_zone

Expose one dispatch predicate:

- natural_disaster_is_family_geographically_eligible

Input:

- natural_disaster_current_family, a resolved natural_disaster_family enum.

Scope:

- state.

Output:

- true only when the current state is a physically possible target for that family.

Side effects:

- none.

### Data construction rules

Climate:

- build positive region allowlists from vanilla weather;
- keep a positive heat allowlist and an explicit cold exclusion;
- include all Siberian/cold ids listed above in the heat exclusion even though a few vanilla regions have warm summer maxima;
- use snow/blizzard weather and high-altitude state review for winter families;
- do not infer heat from population, infrastructure, agriculture, resources, or previous heat history.

Terrain and hydrology:

- precompute state allowlists from province terrain composition and reviewed river/coast exposure;
- do not use country-scope has_terrain as though it were a state predicate;
- flood eligibility should distinguish floodplains/wet basins/coastal lowlands from arbitrary mountain or desert states;
- dry and wet mass movement both require slope exposure, then diverge on dry versus wet climate.

Volcanism and tectonics:

- use an explicit reviewed state whitelist for active volcanic vents;
- use a narrower reviewed whitelist for massive-eruption-capable zones;
- use plume and lahar exposure lists derived from a vent origin, neighboring geography, and river/slope exposure;
- a coastline, resource deposit, mountain proxy, or previous disaster flag is never a volcanic vent;
- earthquake zones may be broader than vent zones but must still be a reviewed seismic/fault domain.

Coastal hazards:

- tropical cyclone requires both is_coastal = yes and tropical-storm-basin membership;
- tsunami requires is_coastal = yes and ocean-exposed-coast membership;
- storm surge requires is_coastal = yes and storm-surge-coast membership;
- inland seas and sheltered coasts should be reviewed explicitly rather than accepted by is_coastal alone.

Fuel and corridor hazards:

- wildfire requires a reviewed fuel domain and a dry/fire-weather-capable domain;
- a barren hot desert is not automatically a wildfire state;
- moving-storm corridors require a reviewed storm domain and connected neighbor continuation;
- every derived corridor family must pass its own family geography in the selected segment.

### Family eligibility matrix

| Family | Hard state predicate |
|---|---|
| earthquake | natural_disaster_state_is_seismic_zone |
| flood | natural_disaster_state_is_flood_exposed_zone |
| tropical_cyclone | is_coastal and natural_disaster_state_is_tropical_storm_basin |
| extreme_wind | natural_disaster_state_is_windstorm_zone |
| tornado_outbreak | natural_disaster_state_is_tornado_zone |
| thunderstorm | natural_disaster_state_is_convective_storm_zone |
| hailstorm | natural_disaster_state_is_hail_zone |
| blizzard | natural_disaster_state_is_cold_zone |
| cold_wave | natural_disaster_state_is_cold_zone |
| heat_wave | natural_disaster_state_is_heat_zone and not natural_disaster_state_is_cold_zone, plus the existing Event 051 overlap exclusions |
| drought | natural_disaster_state_is_drought_zone |
| dust_and_sandstorm | natural_disaster_state_is_arid_zone |
| wildfire | natural_disaster_state_is_wildfire_fuel_zone |
| dry_mass_movement | natural_disaster_state_is_slope_zone and natural_disaster_state_is_dry_slope_zone |
| wet_mass_movement | natural_disaster_state_is_slope_zone and natural_disaster_state_is_wet_slope_zone |
| volcanic_eruption | natural_disaster_state_is_volcanic_vent_zone |
| ashfall | natural_disaster_state_is_volcanic_plume_zone |
| lahar | natural_disaster_state_is_lahar_zone |
| tsunami | is_coastal and natural_disaster_state_is_ocean_exposed_coast |
| storm_surge | is_coastal and natural_disaster_state_is_storm_surge_coast |
| meteor_impact | generic runtime-valid land state |
| meteor_shower | generic runtime-valid land state |
| whole_earth_rupture | generic runtime-valid land origin; every derived earthquake, slope, or tsunami segment then uses that derived family's predicate |
| massive_eruption | natural_disaster_state_is_massive_eruption_zone |
| moving_storm_corridor | natural_disaster_state_is_storm_corridor_zone; every later segment is adjacent and passes its resolved derived-family predicate |

For a fictional abnormal family, generic land eligibility is acceptable only where the design itself is globally physical. It must not be used to excuse its physically specific derived impacts.

## Integration into the current predicates

natural_disaster_is_valid_family_target should become:

~~~txt
natural_disaster_is_valid_family_target = {
	natural_disaster_is_valid_impact_state = yes
	natural_disaster_is_family_geographically_eligible = yes
	if = {
		limit = {
			check_variable = {
				natural_disaster_current_family = constant:natural_disaster_family.heat_wave
			}
		}
		natural_disaster_is_valid_heat_impact_state = yes
	}
}
~~~

Remove resource, history, agriculture, infrastructure, and generic coastal alternatives from this hard predicate. Retain them only in natural_disaster_score_family_target_state.

natural_disaster_is_valid_repeat_impact_state must also call natural_disaster_is_family_geographically_eligible. An open card is not permission to put a new volcanic eruption, heat wave, tsunami, or other incompatible family in that state.

At delayed execution, copy the persistent state family into natural_disaster_current_family before testing natural_disaster_scheduled_state_is_still_valid, then call the same geography predicate. Physical geography is normally static, but heat overlap, state responsibility, and future map extensions are not.

## Public resolver contract

### Fixed selector semantics

| Request | Family may change? | Target domain may change? | Failure |
|---|---:|---:|---|
| specific family + selected_state | no | no | invalid_target, or heat_exclusion for the existing heat overlap |
| random family/group + selected_state | yes, inside requested pool | no | no_eligible_target after the family pool is exhausted |
| specific family + selected_country | no | no, search owned-and-controlled states of that country | no_eligible_target |
| random family/group + selected_country | yes, inside requested pool | no | no_eligible_target |
| specific family + selected_region | no | no, search only that strategic region | no_eligible_target |
| random family/group + selected_region | yes, inside requested pool | no | no_eligible_target |
| caller_provided state | same as selected_state | no | invalid_target/no_eligible_target |
| caller_provided country | same as selected_country | no | no_eligible_target |
| caller_provided state and country | family rules above | neither scope may change; state must remain owned or controlled by supplied country | invalid_target |
| specific family + coast/dense/nearby_enemy/random_valid | no | remain inside requested mode | no_eligible_target |
| random family/group + coast/dense/nearby_enemy/random_valid | yes, inside requested pool | remain inside requested mode | no_eligible_target |
| locked path segment | only within the explicit derived-family set of that path | adjacent state only | skip/terminate segment |

An exact family is never replaced with another family. A selected state/country/region is never widened to another target mode. A volcano request with no valid vent rejects or skips; it never becomes a meteor, earthquake, or generic coastal eruption.

### Strategic-region semantics

The current maximum_strategic_region = 304 constant matches the contiguous 1 through 304 vanilla ids in Operation Postern 1.19.2.

Keep the range check only if its version dependency is documented. A valid sea-only or otherwise land-empty strategic region is structurally valid but resolves no state and should return no_eligible_target. An id outside the current map range returns invalid_region.

natural_disaster_select_suitable_state_from_target_region is the correct selection shape:

- inject the region id with meta_effect;
- iterate matching states once for the call;
- require hard family validity;
- score only eligible states;
- save the best state and its controller.

This one-shot every_state scan is not a periodic world iteration and does not violate the on-action restriction.

### Per-attempt target proof

Regular event targets cannot be cleared. The live implementation now uses the required two scope-free proof variables:

- natural_disaster_target_candidate_saved
- natural_disaster_target_country_candidate_saved

At the start of natural_disaster_resolve_target:

~~~txt
set_temp_variable = { natural_disaster_target_candidate_saved = 0 }
set_temp_variable = { natural_disaster_target_country_candidate_saved = 0 }
set_temp_variable = { natural_disaster_target_resolved = 0 }
~~~

Set the country proof in the same branch that saves natural_disaster_target_country. Set the state proof in the same branch that saves natural_disaster_impact_state.

natural_disaster_select_state_from_target_country must require the country proof for this attempt, except when an explicitly stored sequence anchor country is being reused for a later hit. That anchor reuse needs its own proof variable and must be copied into the attempt proof deliberately.

Final success requires:

- both proof variables are positive;
- both event targets exist;
- the impact state remains family-valid;
- the impact state's controller is the resolved target country.

The final live snapshot correctly supplies the country half as well. Retain both proofs. They specifically prevent:

- nearby_enemy can fail to draw an enemy, then read the previous target country;
- default random targeting can fail to draw a current country, then read the previous target country;
- the stale country can yield a valid state and incorrectly convert the failed attempt into success.

Do not use has_event_target alone as current-attempt proof.

### Retry transaction

The current broad condition is correct:

- retry only when natural_disaster_call_family = random;
- keep target mode fixed;
- do not retry a locked path target;
- keep the retry count bounded by natural_disaster_sequence.random_target_attempts.

The transaction order must be:

1. resolve one allowed family candidate;
2. clear both attempt proof variables;
3. resolve a target inside the fixed target domain;
4. if unresolved and the family is random, reroll only the family and repeat;
5. after a pair resolves, commit sequence origin/lock metadata;
6. schedule the pair;
7. otherwise record a skipped hit or reject the zero-hit call.

The final live snapshot has correctly moved these assignments until after retry success:

- natural_disaster_planned_origin_family for the first scheduled pair;
- natural_disaster_sequence_locked_family when a random abnormal first family becomes a path lock.

Do not regress this ordering. Placement before target resolution would record the first failed family as the origin and could set an abnormal lock that makes natural_disaster_resolve_family repeat the same failed locked family.

For random families, avoid silently substituting meteor_impact when an abnormal candidate is not allowed. Filter that candidate before selection or reroll within the authorized pool. A specific abnormal request that is locked out already has abnormal_locked and must remain rejected.

The existing retry limit provides bounded failure. For a fixed state/country/region, a stronger future implementation can build a temporary eligible-family pool and select from it, but that is not permission to weaken the hard rules. If bounded random resolution exhausts its attempts, it returns no_eligible_target.

### Public outputs

Keep the existing outputs:

- natural_disaster_call_result
- natural_disaster_call_reject_reason
- natural_disaster_call_sequence_id
- natural_disaster_call_primary_job_count

Add:

- natural_disaster_call_resolved_primary_family
- natural_disaster_call_has_resolved_primary_state
- natural_disaster_call_has_resolved_primary_country
- natural_disaster_call_resolved_target_region
- natural_disaster_call_skipped_primary_count

Add regular event-target outputs:

- natural_disaster_call_resolved_primary_state
- natural_disaster_call_resolved_primary_country

Semantics:

- the resolved outputs describe the first successfully scheduled primary hit, not the last retry or last sequence hit;
- initialize the numeric proof outputs to zero before every call;
- save the output event targets only when the first primary hit is committed;
- callers must test the numeric proof output because a regular event target from an earlier call can still exist in the effect chain;
- resolved_target_region echoes the supplied id only for selected_region, because there is no documented generic state-to-region numeric output;
- primary_job_count remains the scheduled count;
- skipped_primary_count exposes partial sequence resolution;
- a zero-hit rejection leaves all resolved proof outputs at zero.

Update the call_natural_disaster documentation to say retry covers every target mode for a random family, not only random-valid and selected-country.

### Reject-reason mapping

No new reject enum is required:

- exact supplied state exists but is physically incompatible: invalid_target;
- heat exact state is blocked by Event 051 overlap: heat_exclusion;
- supplied country/region/mode is coherent but contains no eligible pair: no_eligible_target;
- strategic-region id outside the current map range: invalid_region;
- random family/group has no valid pair after bounded resolution: no_eligible_target;
- unauthorized abnormal request: abnormal_locked.

Do not fire a report, news item, aftermath card, history entry, or visual card for a rejected or skipped physical impact.

## Secondary paths that must use the same geography

### Repeat impacts

Current selected-state and caller-provided branches accept:

- natural_disaster_is_valid_family_target, or
- natural_disaster_is_valid_repeat_impact_state.

The repeat predicate must include the family geography dispatch. Otherwise an open aftermath card remains a back door around the correction.

### Regional spread

natural_disaster_apply_regional_spread currently builds neighbors with only natural_disaster_is_valid_impact_state.

Change the candidate limit to natural_disaster_is_valid_family_target with natural_disaster_current_family already set. A flood, wildfire, volcano, winter storm, slope failure, or tsunami cannot spread into an incompatible neighbor merely because it is populated.

### Path and corridor continuation

Keep adjacency mandatory. Each segment must use the derived current family, not only the origin lock, when checking natural_disaster_is_valid_family_target.

If there is no eligible adjacent state:

- terminate that physical path segment;
- count the planned segment as skipped;
- do not teleport to a non-neighbor;
- do not change an exact locked family;
- do not reuse a stale event target.

### Chain follow-ups

natural_disaster_execute_chain_followup currently changes the origin state's family to earthquake, tsunami, lahar, or wildfire and then applies losses/damage without a physical target check.

Introduce:

- natural_disaster_resolve_chain_target
- natural_disaster_chain_target_saved_this_attempt
- regular event target natural_disaster_chain_target_state

Rules:

- aftershock may remain in the seismic origin only if that state is earthquake-eligible;
- tsunami must use the origin only when it is an ocean-exposed coast, otherwise it may use an explicitly modeled adjacent eligible coastal state;
- lahar must remain in a reviewed lahar zone linked to a volcanic origin;
- wildfire spread must use a wildfire-fuel state, normally an eligible neighbor;
- if no physical target exists, do not enqueue or execute the damaging chain;
- famine, disease, refugee pressure, supply collapse, and political shock are socioeconomic chains and use their own existing validity, not a fabricated physical-family target.

An explicit chain_policy = tsunami on an inland primary disaster does not authorize an inland tsunami. The primary call may still be accepted, while the impossible secondary impact is skipped and recorded as such.

### Scheduled execution

Before a delayed impact:

1. restore the scheduled state's persistent natural_disaster_family into natural_disaster_current_family;
2. require natural_disaster_scheduled_state_is_still_valid;
3. require natural_disaster_is_family_geographically_eligible;
4. retain the existing heat overlap check;
5. cancel/skip cleanly if any check fails.

Control transfer does not change physical geography, but it can change the responsible country and queue owner. The existing narrow state-control transfer path remains appropriate.

## Decision-category presentation

### Current live implementation

The current single natural_disaster_aftermath_category is the right functional split. It avoids:

- twenty empty category shells;
- duplicating generic recovery decisions;
- duplicating warning and aftermath localisation;
- simultaneous category clutter;
- pretending category metadata automatically relocates decisions from common/decisions.

The current natural_disaster_foreign_relief_category use of GFX_decision_cat_picture_nd_famine is appropriate.

The current aftermath map is not yet robust for multiple active families:

- every matching family predicate can be true at the same time;
- GFX_decision_cat_picture_nd_recovery_overview = { always = yes } is also true at the same time;
- the vanilla JAP precedent does not exercise overlapping picture predicates.

Treat ordered first-match behavior as unproven. Make the picture conditions mutually exclusive.

### Recommended presentation state

Add country variables:

- natural_disaster_category_display_family
- natural_disaster_category_display_state, scope-valued

Add country-scope effect:

- natural_disaster_refresh_category_presentation

It should:

1. clear the previous display selection;
2. scan controlled states with natural_disaster_state_has_displayable_activity;
3. use the existing aftermath priority score inputs;
4. give active abnormal families a priority bonus;
5. give an active warning an urgency bonus;
6. select the highest score using strict greater-than so iteration ties remain stable;
7. store the selected state's family and state scope;
8. clear the variables when there is no displayable activity.

Reuse natural_disaster_select_priority_open_card logic instead of inventing a second unrelated ranking system. Extend it with an optional warning-inclusive mode or factor its score calculation into a shared effect.

Refresh presentation in the same effect chain after:

- warning activation or cancellation;
- impact activation;
- repeat-card replacement;
- chain-family arrival;
- phase transition;
- card closure;
- unresolved-territory transition;
- state control transfer;
- heat-overlap cleanup;
- inbound relief visibility changes that can leave only the overview state.

Do not add a periodic world scan.

The category picture block should compare only the one display-family variable. Every family entry then becomes mutually exclusive. The recovery fallback should match only when the variable is absent or outside 1 through natural_disaster_family.max; do not use always = yes alongside a family match.

If the parent prefers not to store presentation state, every picture predicate must explicitly exclude all higher-priority live family groups, and the fallback must require no displayable family. That approach is more repetitive and evaluates more state scans; the presentation variable is the recommended architecture.

### Existing family-to-picture map

No new art is required.

| Family | Existing category picture |
|---|---|
| earthquake | GFX_decision_cat_picture_nd_earthquake |
| flood | GFX_decision_cat_picture_nd_flood |
| tropical_cyclone | GFX_decision_cat_picture_nd_cyclone |
| extreme_wind | GFX_decision_cat_picture_nd_wind |
| tornado_outbreak | GFX_decision_cat_picture_nd_severe_storm |
| thunderstorm | GFX_decision_cat_picture_nd_severe_storm |
| hailstorm | GFX_decision_cat_picture_nd_hail |
| blizzard | GFX_decision_cat_picture_nd_winter |
| cold_wave | GFX_decision_cat_picture_nd_winter |
| heat_wave | GFX_decision_cat_picture_nd_heat |
| drought | GFX_decision_cat_picture_nd_drought |
| dust_and_sandstorm | GFX_decision_cat_picture_nd_dust |
| wildfire | GFX_decision_cat_picture_nd_firefront |
| dry_mass_movement | GFX_decision_cat_picture_nd_slope |
| wet_mass_movement | GFX_decision_cat_picture_nd_landslide |
| volcanic_eruption | GFX_decision_cat_picture_nd_volcano |
| ashfall | GFX_decision_cat_picture_nd_volcano |
| lahar | GFX_decision_cat_picture_nd_volcano |
| tsunami | GFX_decision_cat_picture_nd_tsunami |
| storm_surge | GFX_decision_cat_picture_nd_cyclone |
| meteor_impact | GFX_decision_cat_picture_nd_skyfall |
| meteor_shower | GFX_decision_cat_picture_nd_meteor_storm |
| whole_earth_rupture | GFX_decision_cat_picture_nd_rupture |
| massive_eruption | GFX_decision_cat_picture_nd_massive_eruption |
| moving_storm_corridor | GFX_decision_cat_picture_nd_corridor |
| no displayable activity | GFX_decision_cat_picture_nd_recovery_overview |
| foreign relief | GFX_decision_cat_picture_nd_famine |

Keep natural_disaster_aftermath_category_desc and natural_disaster_foreign_relief_category_desc. The offline decision reference states that category pictures do not appear without description localisation.

## Edge cases

- A volcanic state already occupied by another country: physical eligibility remains true; selected-country resolution still follows the documented owned-and-controlled rule, while selected-state resolution reports the current controller.
- A valid vent state already has a scheduled impact or blocked aftermath: it is temporarily unavailable. The resolver may choose another valid vent or reject; it may not choose a generic coast.
- A random volcanic group on a fixed non-volcanic state: reroll only inside that group and reject if no member fits.
- A random winter/temperature group on a Siberian state: heat is filtered out; cold wave or blizzard may resolve if otherwise valid.
- A specific heat request in a Siberian/cold state: invalid_target; Event 051 overlap remains heat_exclusion.
- A selected strategic region with no land states: no_eligible_target.
- A selected strategic region with land but no physical match: no_eligible_target.
- A caller-provided state and country that disagree after control changes: invalid_target.
- A random enemy target when the caller is no longer at war: no current-attempt country proof, therefore no target.
- A failed first abnormal family draw: no path lock and no origin-family commit until a later pair succeeds.
- A multi-hit accepted sequence with later dead ends: accepted with scheduled and skipped counts; no invented replacement targets.
- A locked corridor reaching a coastline, mountain wall, or dead end with no eligible neighbor: stop the path.
- A tsunami chain from an inland earthquake: find an explicitly adjacent ocean-exposed coastal target or skip the tsunami.
- A lahar chain from a generic mountain/resource state: never schedule.
- A wildfire spread into barren desert or ice: never schedule.
- A state changes controller before impact: queue transfer may change country output, but execution still rechecks geography and family.
- Several active families in one country: one deterministic display state/family drives the category picture.
- Category visible only because inbound relief remains active: show recovery overview.
- Future vanilla state or region ids not in the reviewed registry: restrictive families fail closed until the registry is updated.

## Validation matrix

| Scenario | Expected result |
|---|---|
| specific volcanic_eruption, selected_state, reviewed vent | accepted; exact state and family returned |
| specific volcanic_eruption, selected_state, Berlin/non-vent | rejected invalid_target; no jobs/cards/reports |
| specific volcanic_eruption, selected_country with no vent | rejected no_eligible_target |
| random volcanic_ash group, selected_country with vent/plume states | resolves only volcano/ash/lahar pairs that fit the selected state |
| specific heat_wave, selected Siberian region/state | rejected invalid_target; never selected |
| random winter_temperature group, selected Siberian state | heat filtered; cold/blizzard or no_eligible_target |
| specific blizzard, Sahara state | rejected invalid_target |
| specific dust, wet tropical forest state | rejected invalid_target |
| specific tropical cyclone, inland Mongolia | rejected invalid_target |
| specific tsunami, generic inland state | rejected invalid_target |
| specific storm surge, sheltered/non-surge coast | rejected invalid_target |
| specific flood, reviewed floodplain | accepted |
| dry mass movement, flat plain | rejected |
| wet mass movement, reviewed wet slope | accepted |
| massive eruption, ordinary volcanic zone not in massive subset | rejected |
| random family, selected_state | retries families against the same state; target never widens |
| random family, selected_country | retries families; country never changes |
| random family, selected_region | retries families; region never changes |
| random family, nearby_enemy with no war target | no_eligible_target; stale country cannot resolve |
| exact family with no valid target | family remains exact and call rejects |
| unauthorized abnormal family | abnormal_locked; no meteor substitution |
| first random family fails, second succeeds | origin family and returned family equal the second successful family |
| first failed abnormal draw then ordinary success | no stale abnormal path lock |
| repeat hit changes family to geographically invalid family | rejected/skipped; open card does not bypass |
| regional spread from flood into non-flood-exposed neighbor | neighbor excluded |
| inland earthquake derives tsunami chain with no coastal neighbor | tsunami chain skipped |
| volcanic origin derives lahar in reviewed lahar zone | chain accepted |
| delayed heat impact gains Event 051 exclusion before execution | impact canceled/skipped |
| path has no eligible adjacent state | path stops; no teleport or stale target reuse |
| accepted partial sequence | primary_job_count equals scheduled hits; skipped output equals omitted hits |
| rejected zero-hit sequence | resolved state/country proof outputs remain zero |
| two public calls in one effect chain | second call cannot accept first call's stale ET without current proof flags |
| one ordinary and one abnormal card active | deterministic abnormal display family drives picture |
| several ordinary cards active | deterministic priority state drives picture |
| no displayable warning/card, inbound relief active | recovery overview picture |
| foreign relief category visible | famine picture |

## Implementation order

1. Add and review the geography registry against the current vanilla map.
2. Replace proxy-based hard family eligibility with the geography dispatch; preserve proxies only as scoring inputs.
3. Add state and country per-attempt proof and relationship validation.
4. Move origin-family and abnormal-lock commits after successful pair resolution.
5. Extend repeat and scheduled-state validation.
6. Filter regional spread.
7. Add physical chain-target resolution.
8. Add stable public resolved outputs and update dynamic-effect documentation.
9. Make category-picture conditions mutually exclusive through the presentation selector.
10. Run the full validation matrix, including concurrent active cards and two public calls in one effect chain.
11. Use the Event 013 completion/localisation audits before any completion claim.

## Expected implementation surfaces

Gameplay:

- common/scripted_triggers/013_natural_disasters_geography_triggers.txt
- common/scripted_triggers/013_natural_disasters_triggers.txt
- common/scripted_effects/013_natural_disasters_effects.txt
- common/script_constants/013_natural_disasters_constants.txt
- common/decisions/categories/013_natural_disasters_categories.txt
- common/scripted_effects/chaosx_dynamic_effects.txt
- common/scripted_effects/chaosx_dynamic_effects.md

Potential presentation localisation only if player-facing wording changes:

- localisation/english/013_natural_disasters_l_english.yml

Documentation that the parent must align after implementation:

- docs/events/013_natural_disasters/overview.md
- accepted Event 013 source specs if the correction changes an authoritative contract

No new image, DDS, sprite definition, or GUI asset is required. Every recommended category picture already exists in interface/013_natural_disasters.gfx.

## Completion gate

Do not claim the correction complete if any of the following remains:

- volcano or massive eruption still accepts resource/coast/history proxies as physical proof;
- heat can select any mandatory Siberian/cold exclusion region;
- repeat, spread, chain, path, or delayed execution bypasses geography;
- a stale country event target can satisfy a new attempt;
- failed pre-retry family metadata is committed to the successful sequence;
- a specific family is silently substituted;
- selected state/country/region widens after failure;
- the public output does not identify the first resolved family and target scopes;
- category picture predicates overlap without proven engine precedence;
- an always fallback remains simultaneously true with a family picture;
- any restrictive family registry is a placeholder rather than a reviewed map dataset;
- localisation/documentation is stale;
- a simplification or fallback was used without explicit approval.

The intended failure behavior is conservative and visible to callers: reject or skip cleanly. It never fabricates a physical disaster in an incompatible place.
