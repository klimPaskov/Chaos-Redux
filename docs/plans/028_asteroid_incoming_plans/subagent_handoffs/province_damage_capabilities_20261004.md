# Event028 province-building damage capabilities, 2026-10-04

## Scope and result

This is read-only engine-capability research from chaosx_scripted_system_architect.
The parent owns adapter integration, gameplay changes, and completion claims.
Only this new handoff is written.
No gameplay, engine, asset, GUI, localisation, Git index, or commit is changed, and the game is not launched.
AGENTS.md was reread.
The previously read events and subagents skills govern the owner/helper boundary and evidence limits.
No skill is modified.

The source-supported proposal is a STATE-scoped set_building_level batch over matching provinces, with a zeroing batch for the main crater and ascending exact-original-level cohorts for proportional ring losses.
It avoids applying a state aggregate removal amount separately to every province.
Installed documentation does not establish the province aggregate semantics of building_level@type, and the installed setter section omits detailed selector-comparison semantics.
Those native acceptance gaps remain explicit.
This report does not claim the province adapter, exact receipts, railway destruction, or queued-project cancellation is resolved.

## Native command evidence

Installed documentation\effects_documentation.md:

| Command | Scope and exact evidence | Consequence for this adapter |
| --- | --- | --- |
| remove_building | STATE/COUNTRY, lines 5838 to 5873. type, level as amount removed, explicit state or province, both literals/variables supported. Lines 5869 to 5871 require a state building when province is absent and explicitly prohibit recursive province lookup. | The current Event028 explicit-state call cannot clear all provincial installations. |
| set_building_level | STATE, no supported targets, lines 6621 to 6629. The section says it sets a specific building level in a state or province but supplies no parameter example. | The command exists, while detailed province-selector syntax comes from the offline wiki and source precedents. |
| add_building_construction | STATE, lines 839 to 846. Starts construction for a level amount in a state/province. | Addition or queued construction is not a reliable destructive adapter. |
| damage_building | STATE/COUNTRY, lines 3374 to 3415. type/tags, damage, repair_speed_modifier, state or province targeting. Lines 3412 to 3413 say a state-only province-building search selects the first matching province. | A state-only call does not distribute proportional damage over every existing provincial installation. It is also health damage, not an observed count of permanently removed levels. |

The installed examples explicitly permit province = 500 or a variable like var:target_province for damage/remove.
They do not document a selector block for damage_building.
Do not transplant the construction/setter province selector into damage_building by assumption.

Offline Effects wiki lines 3614 to 3616 document set_building_level and add_building_construction with:

- type, level, instant_build, and a scalar province ID or province selector block.
- all_provinces, id, coastal/naval-base/border/border-country/victory-point/supply-node restrictions.
- An inner level comparison that filters provinces by existing building level below, at, or above the supplied number.
- Execution in the containing STATE even when a specific province is selected.

The same page at 3669 to 3677 gives this setter example:

~~~txt
set_building_level = {
	type = bunker
	level = 3
	province = {
		all_provinces = yes
		limit_to_border = yes
		level < 3
	}
}
~~~

The outer level is the new absolute level.
The inner level is a selection condition on the type's existing province level.
They must not be confused with remove_building.level, which is a removal amount.

The requested exact cohort form is:

~~~txt
set_building_level = {
	type = bunker
	level = 1
	province = {
		all_provinces = yes
		level = 2
	}
}
~~~

This is a source-supported candidate from the wiki's “at” comparison description.
The installed setter documentation does not explicitly define whether this inner equality is exact, and the bounded searches found no literal-equality selector precedent in installed scripted effects/events, project scripted effects, or Kaiserreich scripted effects.
The known project precedent uses level > 0, and the wiki example uses level < 3.
Exact equality and all-match execution must therefore be confirmed natively before relying on the cohort proof.
Do not silently replace equality with greater-than-or-equal behavior.
Using two repeated level keys to manufacture an interval is also not verified and is not proposed.

## Exact current project and vanilla precedents

common\scripted_effects\chaosx_camp_visual_anchor_effects.txt:5 to 24:

~~~txt
@CHAOSX_CAMP_VISUAL_ANCHOR_REMOVE_LEVEL = 0

chaosx_refresh_camp_visual_anchor = {
	set_building_level = {
		type = concentration_camp_site
		level = @CHAOSX_CAMP_VISUAL_ANCHOR_REMOVE_LEVEL
		province = {
			all_provinces = yes
			level > 0
		}
	}
	set_building_level = {
		type = extermination_camp_site
		level = @CHAOSX_CAMP_VISUAL_ANCHOR_REMOVE_LEVEL
		province = {
			all_provinces = yes
			level > 0
		}
	}
}
~~~

This establishes a current project source pattern for all positive-level provinces of an existing type.
It is not an executed zeroing test by this worker.

Installed common\scripted_effects\SOV_scripted_effects.txt:8286 to 8294 uses:

~~~txt
add_building_construction = {
	type = supply_node
	province = {
		all_provinces = yes
		limit_to_victory_point = yes
	}
	level = 1
	instant_build = yes
}
~~~

This confirms a vanilla province-selector consumer under STATE scope, although it adds buildings and does not establish deletion or exact-level equality.

Current common\scripted_effects\028_asteroid_incoming_effects.txt:584 to 602 instead emits:

~~~txt
remove_building = {
	type = [BUILDING_TYPE]
	level = asteroid_incoming_remove_levels
	state = var:asteroid_incoming_selected_state_id
}
~~~

Its own comment at 582 to 583 already records province coverage as a native integration gap.
The positive-removal guard is based on an amount prepared from the state getter.
A province branch must not retain that aggregate-amount eligibility gate if the getter's province coverage is unproven.
Presence can instead be checked with the documented any_province_building_level trigger, or an all-positive selector can safely target only existing levels.
Do not use an uncertain zero aggregate read to infer that all provinces are empty.

## Actual 63-token inventory and bounds

A read-only mechanical pass extracted every asteroid_incoming_selected_building = token:... assignment in the current Event028 effects file and parsed the buildings blocks of the installed two building files and the three project building files.
The result was 63 calls, 63 unique tokens, and 63 unique effective building definitions.
There were no missing tokens, duplicated definitions, or uncovered building definitions in those roots.
The spawn_points-only file contributes no building token.
This is source inventory coverage, not DLC availability or native transaction acceptance.

Classification follows the installed 00_buildings.txt:7 to 8 comment and offline Building modding:63 to 73: province_max marks a province building.
A state_max alongside province_max does not convert it into a state building.

| Group | Tokens and actual bound |
| --- | --- |
| Province cap 10, ordinary | naval_base, bunker, coastal_bunker. Installed 00_buildings.txt:150 to 198, province_max at 165, 180, 196. |
| Province cap 1, ordinary vanilla non-landmarks | supply_node, naval_facility, naval_supply_hub, naval_headquarters, nuclear_facility, air_facility, land_facility, dam, dam_mountain, cataract_dam_mountain, canal_kiel, canal_panama. Installed 00_buildings.txt:98 to 113, 126 to 148, 356 to 400, 500 to 707. |
| Province cap 1, vanilla landmarks | 22 definitions in 01_landmark_buildings.txt:37 to 649, named below. |
| Province cap 1, project | biowarfare_facility, cw_facility, concentration_camp_site, extermination_camp_site, anomaly_signal_beacon_pilot. Project chaosx_buildings.txt:38 to 108 and 189 to 244, chaosx_3d_model_pilots.txt:6 to 34. Each explicitly has province_max = 1. |
| Special railway graph | rail_way, 00_buildings.txt:115 to 124, nominal province_max = 1. This nominal construction definition does not prove railway graph-segment levels or a railway deletion API. Exclude it from the ordinary batch adapter. |
| State buildings | 20 tokens, named below. Preserve the separate state-building path. |

The 22 landmark tokens are landmark_big_ben, landmark_colosseum, landmark_cristo_redentor, landmark_eiffel_tower, landmark_statue_of_liberty, landmark_kremlin, landmark_hofburg_palace, landmark_berlin_reichstag, landmark_berlin_volkshalle, landmark_taj_mahal, landmark_sadabad_complex, landmark_hagia_sophia, landmark_forbidden_city, landmark_nanjing_presidential_palace, landmark_nanjing_presidential_palace_prc, landmark_nanjing_presidential_palace_gen, landmark_great_wall_section, landmark_tokyo_imperial_palace, landmark_national_diet, landmark_hakko_ichiu, landmark_prague_castle, and landmark_bojnice_castle.

The 20 state tokens are infrastructure, arms_factory, industrial_complex, air_base, stronghold_network, dockyard, anti_air_building, synthetic_refinery, fuel_silo, radar_station, mega_gun_emplacement, rocket_site, nuclear_reactor, nuclear_reactor_heavy_water, commercial_nuclear_reactor, energy_infrastructure, industrial_infrastructure, concentration_camp, extermination_camp, and gulag_labor_camp_network.

Thus 63 = 20 state + 42 ordinary province + 1 railway graph.
The 42 ordinary provincial types comprise 39 with cap 1 and three with cap 10.
A full ascending pass needs at most 39 + 3 * 10 = 69 cohort setter attempts per affected state before skipping zero-loss cohorts.
The main crater needs 42 all-positive zeroing attempts, independent of per-type level cap.
No 20-level universal bound, huge generated level table, proxy building, or map-wide province iterator is needed for this source inventory.

Declared caps are bounds of the current source package, not proof that console/history/scripted alterations can never leave over-cap existing levels.
Before a bounded ring ladder, reject/report any matching type above its verified bound using any_province_building_level with level > the bound.
Do not silently omit such a cohort or pretend it was damaged.
Recheck classification and bounds if the building definitions change.
No dynamic native “get building province_max” variable was established by the inspected documentation, so any small cap/classification dispatch must explicitly mirror the audited definitions.

## Narrow helper map and main-clear proposal

| Proposed helper | Scope, inputs, output, side effects and direct call site |
| --- | --- |
| asteroid_incoming_clear_selected_province_building | STATE. Input selected registered building token. Sets every positive-level province of that type to zero. No predictive level-loss output. Called from the main-center province branch of the existing selected-building adapter. |
| asteroid_incoming_set_selected_province_level_cohort | STATE. Inputs selected building token, old integer level, new integer level. Executes one all-provinces exact-level batch. No country scope change or per-province aggregate amount. Called from the ring/fragment ascending ladder. |
| Existing asteroid_incoming_capture_selected_building_receipt | STATE. Receives observed before/after totals only after the getter is validated for provincial sums. Records one type delta, not a predicted delta per selector. Called once after that type's complete ladder. |

No helper was added or implemented.
Parent integration should retain the current selected token's industry/logistics/strategic bucket and deduplicated state transaction.
Only the province mutation route changes.
The existing shared damage_state_building_dynamic helper is unsuitable for this permanent per-province level reduction because it emits a state-only damage_building and has no all-province selection or matching-level receipt.

Main zeroing candidate, matching the current camp pattern:

~~~txt
# STATE scope. The caller supplies a registered building token.
meta_effect = {
	text = {
		set_building_level = {
			type = [BUILDING_TYPE]
			level = 0
			province = {
				all_provinces = yes
				level > 0
			}
		}
	}
	BUILDING_TYPE = "[?asteroid_incoming_selected_building.GetTokenKey]"
}
~~~

Zero is the requested final level, not a tuning amount.
There is no additional coastal/border/victory-point filter.
Those filters would leave legitimate installations outside the main-crater clearance.
instant_build is documented by the wiki, but its default and queue interaction in this setter are not defined by the installed section.
This candidate deliberately mirrors the observed project source form and does not claim it cancels pending construction or active projects.

Cohort batch candidate:

~~~txt
meta_effect = {
	text = {
		set_building_level = {
			type = [BUILDING_TYPE]
			level = [NEW_LEVEL]
			province = {
				all_provinces = yes
				level = [OLD_LEVEL]
			}
		}
	}
	BUILDING_TYPE = "[?asteroid_incoming_selected_building.GetTokenKey]"
	OLD_LEVEL = "[?asteroid_incoming_province_old_level|.0]"
	NEW_LEVEL = "[?asteroid_incoming_province_new_level|.0]"
}
~~~

Both level numbers are emitted as literals rather than assuming that the selector parses temporary variables.
The building token becomes its raw registered type via GetTokenKey, not its localised name.
The helper uses variable inputs and = yes call sites when integrated, not unsupported named scripted-effect parameter blocks.
No country event target, province scope pointer, or new tag is required.

## Ascending-ladder proof, rounding and bounded calculation

Let G(L) be the required integer final level for original level L.
Require 0 to L inclusive, for the fixed severity chosen before processing this type.
Visit original cohorts 1, 2, ... M in ascending order, and emit the new level only for provinces exactly at that old level.
After changing cohort L, a changed province is below L, while later cohorts are above L.
It therefore cannot match a later cohort.
An unchanged province remains at L, but that cohort is never revisited.
This proves one transformation per province if native equality is exact, each batch targets all matches, the scripts execute synchronously, and no nested side effect raises a processed province into a future cohort.

Descending traversal is unsafe: a transformed province can land on a lower level that will be selected again.
A direct all_provinces removal amount calculated from the state sum is also unsafe because the same aggregate amount would be applied to each matching province.

The fraction must be named according to its meaning:

- Destruction fraction d: requested lost levels = floor(L * d), final G(L) = L - floor(L * d).
- Retained fraction r: final G(L) = floor(L * r).

Those formulas are different even when r = 1 - d.
For L = 3 and d = 0.5, floor-loss leaves 2, while floor-retention leaves 1.
The current prepare_selected_building_loss at Event028 effects:564 to 575 multiplies a loss fraction and calls round_temp_variable.
The wiki Data structures:573 and installed script_math_functions.md:281 to 286 define nearest rounding, not floor.
For that same example, the current rounded-loss preparation removes 2.
The parent must preserve the accepted severity meaning and explicitly resolve this rounding difference.
This worker does not silently change balance, add a chance for binary buildings, or choose a fraction.

Floor-loss at any destruction fraction below 1 preserves a cap-1 building.
Floor-retention below 1 removes a cap-1 building.
That matters for hubs, facilities, canals, dams, landmarks, and project anchors.
These are consequences of the requested formula, not interchangeable implementation details.

No floor_temp_variable effect was found in the installed registry.
A source-supported bounded arithmetic alternative uses existing variable operations and while_loop_effect rather than inventing such an API:

~~~txt
# Caller has initialized old_level, destruction fraction, and the cap.
# Caller-owned temporaries survive any helper/meta frames.
set_temp_variable = {
	asteroid_incoming_province_loss_remainder = asteroid_incoming_province_old_level
}
multiply_temp_variable = {
	asteroid_incoming_province_loss_remainder = asteroid_incoming_selected_fraction
}
set_temp_variable = {
	asteroid_incoming_province_loss_whole = constant:asteroid_incoming_runtime.zero
}
while_loop_effect = {
	limit = {
		check_variable = {
			var = asteroid_incoming_province_loss_remainder
			value = constant:asteroid_incoming_runtime.one
			compare = greater_than_or_equals
		}
	}
	subtract_from_temp_variable = {
		asteroid_incoming_province_loss_remainder = constant:asteroid_incoming_runtime.one
	}
	add_to_temp_variable = {
		asteroid_incoming_province_loss_whole = constant:asteroid_incoming_runtime.one
	}
}
set_temp_variable = {
	asteroid_incoming_province_new_level = asteroid_incoming_province_old_level
}
subtract_from_temp_variable = {
	asteroid_incoming_province_new_level = asteroid_incoming_province_loss_whole
}
~~~

The unit-subtraction loop computes floor of the nonnegative product and is bounded by 10 iterations per cohort for current ordinary provincial caps.
Reject a destruction fraction outside 0 to 1 before it runs.
This arithmetic snippet uses the destruction-fraction interpretation explicitly.
For floor-retention, the product input and final assignment differ, while the same floor calculation and cohort proof apply.
Native fixed-point multiplication and exact-threshold behavior are still acceptance questions.
The existing zero/one constants are identity values, and the actual cap must come from the audited type classification.
Do not invent a separate duration, probability, or balance tuning table.

## Actual-level readback: supported expression, unsupported aggregation

Installed dynamic_variables_documentation.md:1096 to 1103 places building_level under STATE scope and documents:

~~~txt
building_level@arms_factory
~~~

The section says only “building level of a building with type”.
It does not say whether a provincial type returns the sum across all provinces, a maximum, an average, the first instance, or no meaningful value.
damaged_building_level:1118 to 1120 and non_damaged_building_level:1139 to 1141 also lack provincial aggregate semantics.
They do not establish an alternative exact sum.

Current Event028 source at 633 and 643 dynamically reads the type before and after mutation.
The source receipt helper at 609 to 621 records the clamped difference.
Those are existing expressions and accounting, not evidence that province sums are read correctly.

Proposed readback envelope:

~~~txt
# Caller-owned STATE temporaries are declared before entering meta text.
set_temp_variable = { asteroid_incoming_selected_before = constant:asteroid_incoming_runtime.zero }
set_temp_variable = { asteroid_incoming_selected_after = constant:asteroid_incoming_runtime.zero }
meta_effect = {
	text = {
		set_temp_variable = { asteroid_incoming_selected_before = building_level@[BUILDING_TYPE] }
	}
	BUILDING_TYPE = "[?asteroid_incoming_selected_building.GetTokenKey]"
}
# Apply this type's complete zeroing batch or ascending ladder here.
meta_effect = {
	text = {
		set_temp_variable = { asteroid_incoming_selected_after = building_level@[BUILDING_TYPE] }
	}
	BUILDING_TYPE = "[?asteroid_incoming_selected_building.GetTokenKey]"
}
# Call the existing receipt helper once only after provincial-sum semantics are established.
~~~

Do not predict actual losses by multiplying an aggregate or by assuming each cohort's match count.
The setter does not document a returned match count.
any_province_building_level is existential, not a count or sum.
No verified all-province numeric reducer or province-scope iterator was established here.
If the getter does not provide a sum, exact numerical provincial receipts remain blocked.
This report supplies no proxy, zero receipt, fake total, or huge province table as a substitute.

The documented existence check can separately verify main clearance:

~~~txt
any_province_building_level = {
	province = { all_provinces = yes }
	building = bunker
	level > 0
}
~~~

After a main clear, this should be false for each ordinary provincial type.
A false existence result establishes absence of positive levels for that type, not the number of levels lost.
Conversely, a zero aggregate read is insufficient when this trigger remains true.

## Meaningful source-model tests and native cases

A read-only PowerShell model tested original integer levels 0 through 10 against destruction fractions 0, 0.05, 0.25, 0.35, 0.5, and 1.
All 66 ascending-cohort cases matched L - floor(L * d).
This verifies the ordering mathematics, not native selector parsing, fixed-point arithmetic, or getter semantics.

For original province levels [0, 1, 2, 4, 10] and destruction fraction 0.5:

| Method | Final levels | Lost total |
| --- | --- | --- |
| Ascending exact cohorts, once | [0, 1, 1, 2, 5] | 8 from original sum 17 |
| Descending mutable cohorts | [0, 1, 1, 1, 1] | 13, repeated hits |
| Aggregate floor loss 8 removed from every province | [0, 0, 0, 0, 2] | 15, aggregate overkill |

The level-10 descending chain is 10 to 5 to 3 to 2 to 1.
The source model assumes exact native cohort equality, which remains unexecuted.

Parent/user-owned native evidence should distinguish these specific failure modes:

1. Exact-selector fixture: place existing bunkers at levels 1, 2, 3 in separate valid provinces. A single inner level = 2 setter to level 1 must change only the level-2 province. This distinguishes exact equality from greater-than-or-equal matching.
2. All-match fixture: two provinces at level 2 must both change in that same batch. This distinguishes all matching provinces from first match.
3. Aggregate-getter fixture: existing bunkers [0, 1, 2, 4, 10] should read 17 before and 9 after the floor-loss half profile if the getter is a sum. A max reader would instead read 10 and 5. A first-positive reader can read 1 and 1. Their deltas are not the required 8.
4. Binary-type fixture: use a legal multi-province supply-node arrangement to distinguish a sum from a binary/state maximum, respecting each type's state_max/group restrictions. Do not create illegal repeated special-project facilities as a normal fixture.
5. Main-clear fixture: several provinces with positive forts, one-level installations, and relevant damaged buildings must all end at zero, with any_province_building_level > 0 false. Verify actual receipts separately.
6. Floor endpoints and threshold fixture: d = 0 leaves levels unchanged, d = 1 clears levels, and products exactly at/near integers follow the chosen floor convention under native fixed-point math.
7. Cap breach fixture: an existing over-cap level must be reported/rejected for ring processing rather than omitted from the bounded ladder.
8. Re-entry fixture: an already applied state transaction must not run another ladder or append its type delta again.
9. Queue/project fixture: a zeroed main-crater province must not regain a building through pending construction, repair, or an active project after the setter. Cancellation remains a separate API/integration requirement.
10. Physical-holder fixture: provincial levels change in the intended stored state even when current owner and controller differ. Existing aggregation must attribute one measured loss without changing the original target identity.

The worker did not execute any native case or write fixtures into gameplay.
Game validation is user-owned.

## Railway and queue boundaries

rail_way is present among the 63 definitions, but the declaration's province_max = 1 is not a railway graph-level bound.
Its actual path/edge levels and loss receipts need a dedicated native railway adapter.
Do not conclude that set_building_level type = rail_way at all provinces destroys every railway segment or that building_level@rail_way sums rail losses.
No railway graph mutation is proposed by this research.

The installed effect-heading search found build_railway and construction addition, but no documented cancel-building-construction or remove-building-construction effect.
This is a bounded documentation gap, not proof that every engine facility is impossible.
Main-crater construction queue cancellation, active state/special-project cleanup, and future rebuild prevention remain separate parent-owned tasks.
Neither a zeroed level nor damage_building proves those queues are canceled.

## MCP evidence

The connected schemas were checked.
Reference context/search/read, source_lookup, event inspect, and map inspect were exposed.
source_lookup still has no view/keyPath.
script_validate was absent.
No server-version/health or task negotiation was established, so helper-expansion/jobs/tasks were not used.

Fresh live results:

- reference_context event succeeded, identifying the installed STATE effect registry and offline Buildings section. The small bundle omitted broad event/scopes/localisation topics. Only pertinent setter/trigger/variable/source sections are claimed read, rather than claiming whole-context coverage.
- reference_search set_building_level and matching reference_read succeeded. Section ID 75d4c8872ed1c5708285834b2df51627beb1062635e552c4a29bb316f491b7c7, installed effects revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af, lines 6621 to 6629, nextLine null.
- Wiki reference_read succeeded for Buildings section ID 3dab18fb80de55a30c18ec7d25270ec577d2360c03a09f17f2e10db41e7d3d07, revision 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c, lines 3614 to 3616. The relevant examples at 3656 to 3677 were read locally.
- building_level reference_read succeeded for section ID 01110bbd97da5ffd6b7bcc26612a1fb5e4171d22fbfcc88882058f5347bc7806, revision 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda, lines 1101 to 1103, nextLine null.
- any_province_building_level reference_read succeeded for section ID d10db4298ca6dd8ccc540a24e631b7d3f4ffbfe41546011cc868c805f2f3fd45, triggers revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29, lines 1621 to 1642, nextLine null.
- source_lookup chaosx_refresh_camp_visual_anchor returned one unshadowed definition, entire lines 7 to 24, revision ee16f1dacebf49d427b40f03c2885f015fed64a3675ce97783734888823d1b08, nextLine null. The initial guessed symbol chaosx_camp_visual_anchor_clear_state returned no definition and was corrected to the actual source identifier.
- source_lookup asteroid_incoming_remove_selected_building_levels returned one unshadowed definition, entire lines 584 to 602, revision 457e553927071467f0d9292d3e43db9b5a972ec063a05b7a9de64c3ba75990be, nextLine null. References were deliberately disabled.
- event_inspect .4 trace succeeded with depth/node/edge each one and expandHelpers false. EVENT_INSPECTED_PARTIAL, focused, revision f0e16475c8407b53ed214cb41838952142f1cd8c62e083191f7d8916d82ac506. Helper/lifecycle projections were deferred, and inline inventory was 64 of 388 paths.
- map_inspect succeeded for lookupOnly state 64/province 6521, includeOverview false. Revision db506e6eafcd7513a9aa63f77def167ab18ed365ec83ae6fb56052b1063d1e30, one state and one province, no unknown province IDs. Full map validation was not requested, and inline inventory was 64 of 2066 paths.

Artifacts retained:

- Event: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1b4b50cbaa488d39deea5bc1326515fc059fa6bc6a4c4153df8cba5f170f1e9/c290c6dda3669299e369bcfa0d18bc3ca98ddccc3349dbd593e22a55834397b9/event-trace-f0e16475c840.json.
- Map: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/641d7004e6024780db0045e10dcf832d93690bf059dddf020c4e15e842265fc2/9a375331d06075e1d05a11fe1e14146b5e156c519ceebfa0784cd961b060cc50/map-lookup.db506e6eafcd7513.7f4bb8ad66327b5e.json.

A map artifact byte-range read at offset 0/length 3000 and the narrower length-300 retry both returned MCP -32603: Artifact provenance manifest is unavailable.
No bulk artifact contents or retrieved-byte hash is claimed.
No timeout occurred on the listed live inspection/reference calls.
MCP results are offline source/scenario evidence, not native engine execution.
No GUI, focus, probability, or unrelated system was designed or inspected for this adapter.

## Source identity ledger

R = C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.
V = C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV.
Each root plus suffix is an exact Windows path.
Physical SHA-256 values below bind the inventory and citations to the observed source snapshot, not a completion claim.

| Path | Relevant lines/read coverage | SHA-256 |
| --- | --- | --- |
| R\AGENTS.md | Repo instructions reread | 38E479CB75828BA888860BE8BC3739F9286C0D925CC7D8DE5ECD3B8DADEC46CF |
| R\common\scripted_effects\028_asteroid_incoming_effects.txt | 558 to 679, token assignments throughout 682 to 1174, receipt and type dispatch inventory | D3C5A26E55EDFA2439A833ADA0D6CC9F13C5794FCBA8857BAF3E6D0F73B97438 |
| R\common\scripted_effects\028_asteroid_incoming_runtime_effects.txt | Existing native provincial trigger at 97, state-profile caller path | 276CBAF89FFCB4071A077DAA6948E787D6BA723FD08D2342332E023F14EB2564 |
| R\common\scripted_effects\chaosx_camp_visual_anchor_effects.txt | Entire 1 to 24 | A52A51F1FD0BFE225DBA488089222930340BD28DC025AB1A89A8B04709D248E4 |
| R\common\scripted_effects\chaosx_dynamic_effects.txt | Existing dynamic building-damage helper at 47 to 60 | F9591FE2BEAB4AC7570813BA76D1B4DBF63FC9FF10DC3315ADFFFCCAB2A895C2 |
| R\common\scripted_effects\chaosx_dynamic_effects.md | Existing shared-helper contract and owner boundary | 089FD416BA8D908CE59123A31378175FCC9577B8BA1E7B0DD6B2D04E0791FD6E |
| R\common\buildings\chaosx_buildings.txt | All building blocks classified, exact cap sections at 67 to 70, 103 to 106, 209 to 214, 238 to 243 | AF9FD98C11F71A791C75D3FFBE1AAD5F64A0F15DDB4CF67474FFA42A780FB468 |
| R\common\buildings\chaosx_3d_model_pilots.txt | Building block 6 to 34, cap at 29 to 32 | 448F3E1CF9EDCA39A748A4306C55C84A513E0458E0F651409341A992B3783ED1 |
| R\common\buildings\chaosx_3d_model_spawns.txt | Spawn-point root classified as containing no building definitions | A7CC35CD8A6430C535C53FF6A0BA0B714EBB872E70FF2764B8426DEDEB0ABA14 |
| R\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md | 1760, 3614 to 3616, 3656 to 3677 | 997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C |
| R\paradox_wiki\Building modding - Hearts of Iron 4 Wiki.md | 63 to 76, provincial classification and terrain caps | 1E5FB5410A26AF12B5B791B193F8F602C4EF8A3614ED897AE4C67084477F7BFC |
| R\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md | Variable arithmetic/comparators at 563 to 574 and token interpolation rules | 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4 |
| V\common\buildings\00_buildings.txt | All building blocks classified, direct cap review 98 to 198 and provincial blocks 356 to 707 | 9FA27D266F726DE04C71311551698C6466257636DCC34D2573A3568D397BD539 |
| V\common\buildings\01_landmark_buildings.txt | All 22 blocks at 37 to 649 classified, each province_max 1 | 9528C42836E08BA01019D62D42607D0D5FB2473B8AA7AA7CB852D95E7A08002C |
| V\common\scripted_effects\SOV_scripted_effects.txt | 8275 to 8294, province-selector vanilla consumer | CC9E16837AFA1428D11E053DC982446B35587980DAA011A1DF12114C3ACE2BF4 |
| V\common\scripted_effects\00_scripted_effects.txt | 26 to 40, state removal and instant construction example | 93DDD0D2E9F7A1A5640CFDAFBAE6B9FF0E1B4EE57E829C81D13B0CAC23AD90BF |
| V\documentation\effects_documentation.md | 839 to 846, 3374 to 3415, 5838 to 5873, 6476 to 6494, 6621 to 6629, meta_effect and while_loop_effect:8573 to 8586 | 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF |
| V\documentation\triggers_documentation.md | 1621 to 1642, province-building existence/level query | 7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29 |
| V\documentation\dynamic_variables_documentation.md | STATE getter at 1096 to 1103, damaged/non-damaged getter sections | 538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA |
| V\documentation\script_math_functions.md | 281 to 286, nearest-rounding semantics and floor-name search | 3C7116906F0BC7590CDD014F5A8B3CF8EF9F0685044FC10E29FABD19AFAF832B |

The shared source may continue changing after these reads.
Parent implementation must bind its final type inventory and meaningful validation to its own final source bytes.

## Completion and remaining blockers

Completed: this research handoff, actual 63-token/cap inventory, exact native/documented command distinctions, bounded batch code proposals, ascending-order proof and 66 host arithmetic cases, getter-verification cases, and current MCP evidence.
Files changed by this worker: only docs\plans\028_asteroid_incoming_plans\subagent_handoffs\province_damage_capabilities_20261004.md.
Gameplay helpers, direct call sites, constants, receipts and cleanup implemented: none.
No simplifications or fallback implementation were made.

Unresolved: native exact-level selector/all-match semantics, setter immediacy and damage/queue interaction, provincial aggregate getter sums, floor-versus-current-rounding acceptance, over-cap handling, separate railway graph loss, and construction/project cancellation.
The parent receives a concrete narrow adapter proposal and its proof limits.
The underlying Event028 physical-clearance and actual-receipt goal is not declared resolved.

