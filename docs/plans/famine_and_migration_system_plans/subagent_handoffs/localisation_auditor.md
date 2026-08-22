# Famine and Migration Localisation Handoff

## Ownership and changed files

- `localisation/english/famine_migration_l_english.yml`: new English player-facing text for the shared famine and migration system.
- `common/scripted_localisation/famine_migration_scripted_localisation.txt`: new selectors for category phase, national food stage, border policy, historical profile, profile mode, route result, cohort source, and dynamically colored decision costs.
- This handoff records the audit and remaining consumer risks.
- No event id, event pool registration, pacing text, shared scripted GUI, gameplay effect, or gameplay trigger was added by this work.

## Localisation coverage

- Category: `chaosx_famine_migration_category`, its dynamic description, four reveal-phase descriptions, five national food-stage labels, seven border-policy labels, and the unset fallback.
- Decisions and missions: titles and descriptions for all 26 decisions and all three missions currently declared in `common/decisions/famine_migration_decisions.txt`, plus success and failure text for each mission.
- Costs: all 26 live `custom_cost_text` keys, with dynamic affordability fragments for political power, trains, convoys, support equipment, infantry equipment, fuel, and air experience.
- Shared tooltips: state and route validity, transfer accounting, general effect context, and the emergency-airlift transport-aircraft requirement.
- State modifiers: title and description coverage for all nine modifiers in `common/dynamic_modifiers/famine_migration_state_modifiers.txt`.
- Historical profiles: all 15 profile labels from the profile specification, the no-profile fallback, and all four profile-mode labels.
- Dynamic context: route states and all 18 cohort-source families currently represented by the pressure-source constants.
- Achievements: `_NAME`, `_DESC`, and precise unlock/disqualifier tooltip text for all eight ids in `common/achievements/chaos_redux_achievements.txt`, plus the shared `famine_migration_achievement_eligible_tooltip` label.
- Reports: seven report-image context labels for famine, blockade, evacuation, border closure, relief arrival, nuclear evacuation, and return consumers.
- Condemnation: labels and descriptions for deliberate starvation, relief obstruction, deportation, forced return, violent pushback, and concealment contexts declared by the adapter effects.
- Deaths: the existing keys `chaos_meter.deaths.cause.famine`, `chaos_meter.deaths.cause.occupation_repression`, `chaos_meter.deaths.cause.forced_labor`, and `chaos_meter.deaths.cause.forced_displacement` were verified in `localisation/english/chaosx_chaos_meter_l_english.yml`; no duplicate keys were added.
- Mapmodes: the parent-owned Famine and Migration mapmode names, descriptions, hover keys, five food-stage labels, and six migration-role labels were audited in `localisation/english/chaosx_map_modes_l_english.yml`; all 15 keys referenced by the four new selectors in `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` resolve.

## Changed key groups

- Category and values: `chaosx_famine_migration_category*`, `famine_migration_category_phase_*`, `famine_migration_food_stage_*`, and `famine_migration_border_policy_*`.
- Gameplay titles and descriptions: every `fm_*` id in the live decision file, with mission outcome suffixes where applicable.
- Costs and requirements: `famine_migration_cost_*`, `famine_migration_decision_*_tt`, and `famine_migration_airlift_planes_requirement_tt`.
- State modifiers and historical context: `famine_migration_state_*`, `famine_migration_profile_*`, and `famine_migration_profile_mode_*`.
- Movement context: `famine_migration_route_*` and `famine_migration_cohort_*`.
- Achievements: all `famine_migration_*_NAME`, `_DESC`, and `_tooltip` achievement keys plus `famine_migration_achievement_eligible_tooltip`.
- Reports and responsibility: `famine_migration_report_*` and `famine_migration_condemnation_*`.

## Audit results

### Missing keys

- No missing title, description, cost, modifier, or achievement key was found for the identifiers present at the final source rescan.
- No unresolved or renamed famine decision, mission, modifier, achievement, scripted-localisation, or mapmode identifier remains in the frozen source snapshot.
- Historical profile, report, and Condemnation strings exist for planned consumers, but not every planned consumer is currently wired in gameplay.

### Duplicate keys

- No duplicate key exists within `famine_migration_l_english.yml`.
- No repository duplicate was found for the new famine and migration key set at audit time.

### Scripted localisation issues and dynamic text opportunities

- The category uses one primary dynamic Food Security value and two supporting values, Displacement Load and Reception Capacity, plus the current border policy.
- Cost strings use scripted selectors so each verified resource turns red when its current stock is insufficient.
- The emergency-airlift cost text deliberately does not invent a transport-aircraft texticon. Its description and the wired `famine_migration_airlift_planes_requirement_tt` state the five-aircraft cost.
- Historical profile, route, cohort, and profile-mode selectors are available, but current source does not expose all of them in a player-facing consumer. Their presence does not prove an in-game display path.
- The final decision source wires all four prepared custom tooltip keys: the generic action effect on preparation, the five-aircraft requirement on emergency airlift, target validity on evacuation, and exact transfer accounting on evacuation. Other decisions continue to use their ordinary visible trigger and effect rendering where no custom tooltip consumer was added.
- Condemnation labels are prepared for the six adapter contexts, but no famine-specific Condemnation detail selector was verified in this scope.

### Cross-surface mismatch notes

- Emergency airlift consumes political power, five transport aircraft, fuel, and air experience. Political power, fuel, and air experience appear in its cost line. Aircraft remain in its description and wired trigger tooltip because no existing transport-aircraft texticon definition was verified.
- Report-image labels are prepared, but only labels with an actual consumer will display. This work did not add a report-image registry or event consumer.
- Achievement wording follows the scripted trigger and disqualifier surfaces. Any later change to thresholds or disqualifying flags requires a localisation synchronization pass.
- Numeric achievement requirements are stated directly where the trigger contract defines them: 70% blockade survival, a major cohort threshold of the greater of 25,000 people or 2% of initial core population, 180 displacement days, 75% voluntary return, a 60-day corridor, three origins, 5% integrated population, Stability above 50%, three severe core states, a 15% national threatened share, and a 15% affected-state population floor.
- The decision auditor reports a high-severity third-country resettlement contract risk: the safe path attempts a regular destination bind after exact movement, while the architect contract normally accepts only active rows and the persisted inbound cohort may already be destination-bound. The localisation describes the intended safe resettlement outcome and cannot prove that unresolved gameplay contract.

### Encoding and format proof

- `famine_migration_l_english.yml` begins with bytes `239,187,191`, the UTF-8 BOM.
- All localisation keys are flush left with no leading space and omit `:0`.
- Scripted localisation contains no direct `§` or `£` characters.

### Prose-quality repairs

- Vagueness: decision descriptions identify the acting authority, target state, resource commitment, and principal consequence.
- Bloat: repeated system explanations were replaced with short descriptions tied to the selected action.
- Obvious explanation: titles are not restated as button instructions; descriptions add route, reception, mortality, or responsibility consequences.
- Repetition: common transfer-accounting rules are centralized in `famine_migration_decision_transfer_tt` instead of repeated across every movement decision.
- Overcomplication: long administrative phrases were replaced with familiar terms such as shelter, food distribution, safe routes, and receiving states.
- Style rules: player-facing prose avoids em dashes, semicolon-linked sentences, implementation history, tuning commentary, and dramatic filler.
- Refugee framing: controlled medical reception explicitly treats outbreak exposure as a condition requiring care, not as an inherent trait of displaced civilians.

### Sourced quotations

- No sourced or attributed quotation appears on the inspected famine and migration localisation surfaces, so no quotation was altered.
- All dynamic scope tokens, variables, constants, formatting codes, and scripted-localisation calls used by the accepted text were preserved through the prose and format repairs.

## Before and after display

- Before: live ids had no dedicated English localisation file, custom cost keys could display raw, and profile, route, cohort, achievement, report, and responsibility contexts lacked a shared English set.
- After: every live decision, mission, modifier, and achievement id has direct English text; the category summarizes the primary and supporting values; and verified costs display resource-specific affordability state.

## Validation and evidence

- The frozen-source audit found 29 of 29 mission and decision ids with titles and descriptions, 26 of 26 `custom_cost_text` consumers, four of four wired custom tooltip keys, nine of nine dynamic modifier title-description pairs, and eight of eight achievement name-description-tooltip triplets.
- All 88 scripted-localisation key references resolve, all 15 new mapmode selector references resolve, no new localisation key or scripted-localisation name is duplicated elsewhere in the repository, and the final decision source has 1,230 opening and 1,230 closing braces.
- Cost values and affordability checks were compared against the decision file's current triggers and completion effects.
- Achievement threshold prose was compared against `common/script_constants/famine_migration_achievement_constants.txt` and the eight predicates in `common/scripted_triggers/famine_migration_achievement_triggers.txt`.
- Mapmode disclosure was checked against `GetFamineStateMapModeDetail` and `GetMigrationStateMapModeDetail`: public viewers receive stage or role only, while the state owner or controller receives the detailed state ledger. Migration detail explicitly names the state owner before displaying the owner's reception values.
- The mapmode audit found two correctable issues and reported them to the parent before any parent-owned file was touched. The parent replaced “Border weight” with the direct phrase “Thicker borders,” changed the owner variable chains to the documented lowercase `[?FROM.owner.<variable>]` form, and added `State owner: [FROM.owner.GetName]` to make controlled non-owned state disclosure unambiguous.
- Map MCP inspection covered states 64, 126, and 336 and returned `MAP_INSPECTED`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6957bfb217fc3705f617c9e630721b50d8ba690e22f3ca6a168b9e136408271/284bf98a3a9ac115976ca90a5caf0815c18713e4ac231b6a08d6c6d2c6abe398/map-inspect.a672f4ba67035c47.json`.
- Vanilla `interface/texticons.gfx` and English localisation precedents verified the political-power, train, convoy, infantry-equipment, fuel, and air-experience tokens. No support-equipment or transport-aircraft texticon was assumed when a matching definition could not be found.
- The initial mandatory decision-view MCP inspection was blocked by a concurrently incomplete source block and returned `SOURCE_UNCLOSED_BLOCK`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bea533184bc7a1bd0c2c02f4fd98a1e22deb768cf9b5ad9b91bbd82bb4a5b676/5ac186b7560e5b8099c83fc2360e3992b4d317ef42017cd57bf40ae1e78d622f/gui-inspect.3d6e187718ec3c1e.json`.
- The post-correction inspection returned `GUI_INSPECTED` with no famine decision source-structure error. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6eb401564a8f6ceb8bc1184d2bd6e1f15aa388360d821b44f5d740d6cac7ea9d/7647e8b28559b8e1442c513d477e0198fb319bd8b43e9f09b690fb1dca8cf5c0/gui-inspect.5c52c299550ec4f8.json`.
- The post-correction MCP validation did not pass because the global GUI graph reached its diagnostic ceiling and the ordinary `decisions_view` consumer was approximated with one missing window. The returned feature scenario had zero inspected elements, so this is source-linkage evidence rather than visual overflow proof.
- The decision owner's frozen-source GUI inspection also returned `GUI_INSPECTED` for `decision_view` and the famine category scenario. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0d7834193c9556b79c25cb981271f1d5befb263e03f14d42f0cc0a53d0c5af1/3e8da763443f484744b96d84323d26da9646ba10694c0f8c357f0fa07f01b7a1/gui-inspect.4ba915d232717fac.json`.

## Skipped validation and remaining risks

- The ordinary decisions panel is not a package-owned scripted GUI and has no feature-specific declarative layout to rewrite. The MCP route can inspect source linkage and diagnostics, but it cannot prove final in-game line wrapping or icon spacing for this category.
- The map inspector verifies connected state and map data, not custom mapmode tooltip rendering or line wrapping. Its global validation also reported unrelated inherited map position and port diagnostics and a diagnostic-ceiling blocker, so source review remains the evidence for these two tooltip surfaces.
- Live in-game consumer validation belongs to the user and was not performed.
- Profile, report-label, shared tooltip, and Condemnation-context display remains dependent on gameplay consumers outside this localisation-only ownership boundary.
- No simplification or fallback was used in the localisation itself. Unverified texticons were replaced with plain text or retained as explicit prose.
- The work remains uncommitted as required by the parent assignment.
