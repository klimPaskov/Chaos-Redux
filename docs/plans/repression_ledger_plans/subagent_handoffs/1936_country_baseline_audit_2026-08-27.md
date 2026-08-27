# 1936 Germany, Japan, and Soviet repression baseline audit

Date: 2026-08-27.

Scope: bounded startup initialization, active-site and country registries, monthly Deaths ownership, Soviet famine-aftereffect pressure, ideas/display refresh, category visibility, later-event responsibility, and balance-facing country-package surfaces for GER, JAP, and SOV.

Status: the intended baseline helpers and country-specific values are present, but a critical registry migration risk remains for Japan. No gameplay file was changed in this audit and no commit was created.

## Executive findings

The explicit on_startup path enters GER, JAP, and SOV directly, which is required because vanilla on_startup has no country scope.

The direct initializers are correctly guarded by original tag and ideology, set country-specific baseline variables, create only the bounded historical sites, refresh ideas and display values, and do not fire escalation events or create later major sites.

SOV has the requested operating three-site gulag baseline, the shared monthly state Deaths pipeline, and a famine marker on state 881 that feeds dynamic state pressure modifiers from Soviet famine pressure.

GER and JAP have the requested lower-priority operating site at one historical location each, while their other historical footprints remain quiet or dormant and their later escalation sites remain event-owned.

Critical risk: the startup initializers register sites before the versioned migration, but that migration clears and rebuilds the active-site arrays. The migration pass iterates current controllers, while camp_rework_register_active_site requires the stored responsible country to equal its current ROOT. Japan's baseline state 716 is owned and controlled by MAN and state 611 is owned and controlled by MEN in the 1936 vanilla state files. A fresh schema migration can therefore leave the active state flag and JAP responsibility variable in place while dropping the state from JAP.camp_active_site_states, global.genocide_active_camp_states, and global.camp_repression_active_countries. This can hide Japan's category and suppress its monthly Deaths contribution after migration.

The migration comments say that stored perpetrators are preserved across controller changes, but the registration gate does not implement that claim for a responsible country different from the current controller. This needs a parent-owned, narrowly scoped post-migration re-registration correction before the baseline can be considered complete.

## Scenario traces

### GER 1936 baseline

| Surface | Source-traced result |
| --- | --- |
| Startup scope | on_startup directly scopes GER and calls genocide_initialize_historical_german_sites. |
| Country guard | The initializer requires original_tag = GER and has_government = fascism. |
| Active site | State 53 (Oberbayern/Dachau footprint) receives camp_rework_historical_baseline_site, genocide_concentration_site, genocide_site_has_responsible_country, and genocide_responsible_country = GER; the baseline helper registers a detention site. |
| Dormant footprints | States 64 (Brandenburg/Sachsenhausen) and 60 (Süd-Hannover/Buchenwald) receive quiet historical footprints but are not activated by the baseline. |
| Later escalation | State 88 (Kielce/Auschwitz route) remains dormant; Mengele/Auschwitz and additional sites remain event or later-decision owned. |
| Tuning | Germany starts with racial policy radicalization 4 and SS archive control 2 from camp_rework_1936_baseline. |
| Ideas and display | The initializer recalculates country values, refreshes major-country ideas, and rebuilds display values. The active, non-overstretched branch selects germany_ss_camp_administration; dormant-only logic retains germany_dormant_ss_camp_legacy. |
| Monthly Deaths | State 53 is processed once by camp_rework_monthly_global_pulse through camp_rework_apply_monthly_state_effects, which owns the chaos_meter_register_state_civilian_deaths_percent call. |
| Category | Visibility is supplied through the shared eligibility and active/inherited-network trigger path, not through a GER-only unconditional carveout. |

### JAP 1936 baseline

| Surface | Source-traced result |
| --- | --- |
| Startup scope | on_startup directly scopes JAP and calls genocide_initialize_historical_japanese_sites. |
| Country guard | The initializer requires original_tag = JAP and has_government = fascism. |
| Active site | State 716 (Liaotung/Manchurian forced-labor footprint) receives historical baseline detention activation and stores genocide_responsible_country = JAP during the direct JAP state scope. |
| Dormant footprint | State 611 (North China) receives a quiet historical forced-labor footprint but is not activated by the baseline. |
| Controller mismatch | Vanilla state 716 is owned and controlled by MAN, and state 611 is owned and controlled by MEN. This is the exact condition that makes the post-initializer migration registration risk material. |
| Later escalation | Pingfang, North China escalation, Ishii experiments, and additional sites remain event or later-decision owned; the startup helper does not fire japan_ishii events or create a new major site. |
| Tuning | Japan starts with Kwantung autonomy 2, Ishii influence 2, and occupation test records 1 from camp_rework_1936_baseline. |
| Ideas and display | The initializer recalculates values, refreshes major-country ideas, and rebuilds display values. The active, non-overstretched branch selects japan_imperial_occupation_repression; the dormant branch uses japan_dormant_occupation_legacy. |
| Monthly Deaths | The intended path is the shared active-state pulse, but it is not reliable after migration clears the arrays unless Japan's stored-responsibility site is re-registered under JAP. |
| Category | The category can be visible immediately after the direct initializer while active flags/arrays exist, but migration can remove the registry evidence used by has_active_camp_network and the shared category trigger. This is a startup acceptance blocker. |

### SOV 1936 baseline

| Surface | Source-traced result |
| --- | --- |
| Startup scope | on_startup directly scopes SOV and calls genocide_initialize_historical_soviet_sites. |
| Country guard | The initializer requires original_tag = SOV and has_government = communism. |
| Active sites | States 644, 874, and 881 receive historical baseline gulag activation, genocide_gulag_site, genocide_soviet_mass_repression_site, stored SOV responsibility, and active registry membership. |
| Building conversion | The gulag helper removes any concentration-camp level and ensures gulag_labor_camp_network level 1 with instant construction, using the valid display-only building in common/buildings/chaosx_buildings.txt. |
| Famine pressure | State 881 receives camp_rework_soviet_famine_pressure; the initializer sets famine pressure 12, grain extraction burden 4, and forced-labor quota 4. camp_rework_soviet_refresh_famine_states projects famine state flags and dynamic local modifiers from Soviet famine pressure. |
| Monthly Deaths | The three active gulag states are processed once by the shared global pulse. camp_rework_apply_monthly_state_effects owns the Deaths adapter call, preventing a duplicate country-bridge Deaths path. |
| Tuning | NKVD authority 6, republic fear 6, and old movement grievance 4 are set from the shared 1936 constants. The monthly famine bridge applies the existing decay, grain, quota, paranoia, stability, and relief terms and leaves threshold escalation to Soviet events. |
| Ideas and display | The initializer refreshes SOV ideas and display values. With three gulag sites and active pressure, the network administration, NKVD authority, and famine-pressure idea branches are available according to existing thresholds. |
| Category | Active network, gulag count, famine pressure, and compatibility visibility satisfy the SOV category trigger path. |

## File-surface checklist

| File | Identifiers checked | Finding |
| --- | --- | --- |
| common/on_actions/genocide_crisis_on_actions.txt | on_startup, fixed GER/JAP/SOV calls, camp_rework_run_versioned_migration | Explicit actor scope is correct; migration ordering creates the Japan registry risk. |
| common/on_actions/chaosx_on_actions_chaos_meter.txt | on_monthly | Shared monthly pulse is host-gated and calls genocide_initialize_system_if_needed plus genocide_monthly_global_pulse; no second broad monthly Deaths loop was found here. |
| common/scripted_effects/genocide_crisis_effects.txt | baseline detention/gulag helpers and three historical initializers | Baseline state IDs, responsibility, idempotence guards, building conversion, famine marker, constants, idea refresh, and display refresh are present. |
| common/scripted_effects/camp_repression_rework_effects.txt | camp_rework_register_active_site, camp_rework_register_country_for_monthly_pulse, camp_rework_run_versioned_migration, camp_rework_monthly_global_pulse, camp_rework_apply_monthly_state_effects, camp_rework_rebuild_display_values | Shared ownership is coherent, but migration's current-ROOT responsibility gate can reject Japan's foreign-controlled sites. |
| common/scripted_effects/camp_repression_major_country_effects.txt | major-country idea refreshes, Soviet famine refresh/update, and monthly bridges | GER/JAP/SOV ideas, Soviet famine pressure, and country bridges are wired; Deaths remains owned by the shared state pulse. |
| common/script_constants/camp_repression_rework_constants.txt | camp_rework_1936_baseline, site contributions, pool factors, death percentages, Soviet famine tuning | Baseline values and Deaths/famine tuning are centralized. |
| common/scripted_triggers/camp_repression_rework_triggers.txt | has_camp_category_visible_action, has_active_camp_network, focus-hook watch, generic-kit routing | Shared eligibility includes active, inherited, managed, reform, crisis, and compatibility visibility; fixed GER/JAP unconditional visibility was not used. |
| common/decisions/categories/genocide_crisis_categories.txt | camp_repression_network_category, imperial_occupation_crisis, gulag_and_mass_repression_system | All three categories use visible_when_empty = yes; visibility still depends on country-specific/shared trigger paths. |
| common/scripted_guis/camp_repression_ledger_scripted_gui.txt | camp_repression_ledger_category_scripted_gui, camp_repression_ledger_scripted_gui | Category and full-ledger windows require a human eligible ROOT and the shared category trigger. |
| common/decisions/camp_repression_generic_decisions.txt and common/decisions/camp_repression_major_country_decisions.txt | generic repression actions and GER/JAP/SOV major-country actions | Existing actions remain separate from startup seeding; later reforms/escalations retain their existing ownership. |
| common/buildings/chaosx_buildings.txt | gulag_labor_camp_network and concentration building definitions | Gulag building ID and level cap are valid; no new building was added. |
| map/buildings.txt | visual anchors for 53, 60, 64, 88, 611, 644, 716, 874, 881 | Required historical baseline states have existing anchors; no map write was made. |
| common/ideas/camp_repression_* and major-country idea files | germany_ss_camp_administration, germany_dormant_ss_camp_legacy, japan_imperial_occupation_repression, japan_dormant_occupation_legacy, sov_gulag_network_administration, sov_nkvd_repression_authority, sov_famine_pressure | Existing idea lifecycle IDs are refreshed by country helpers; no new icon or idea asset is required. |

## Map and state setup

Vanilla state files confirm the selected IDs and ownership: 53, 60, and 64 are German states; 716 is owned by MAN; 611 is owned by MEN; 644, 874, and 881 are Soviet states; and 88 is Polish and remains dormant.

The corresponding 1936 controllers default to those owners in the vanilla history files, so the MAN/MEN controller mismatch is present at the exact startup scenario under audit rather than being a hypothetical occupation case.

The read-only HOI4 map inspection selected states 53, 64, 60, 716, 611, 644, 874, 881, and 88 and confirmed the state/region/network surfaces needed for the baseline. A dry-run allocation against existing state 53 returned the expected MAP_STATE_ID_COLLISION; no map mutation was performed.

Global map diagnostics were not clean because the workspace contains unrelated existing MAP_BUILDING_POSITION_INVALID and MAP_PORT_ADJACENT_SEA_INVALID diagnostics around map/buildings.txt lines near 26352. State, region, and network checks for the selected baseline states passed, but global map diagnostics remain a limitation.

## Politics, leaders, portraits, flags, advisors, and parties

This bounded feature does not alter country tags, country definitions, leaders, portraits, flags, advisors, party names, ideology setup, diplomatic relations, or focus-tree identity.

No cross-country text or country-identity leakage was found in the named baseline helpers, constants, registry effects, idea refreshes, or category triggers. The helpers write country/state variables and flags under explicit GER/JAP/SOV scopes and use existing country-specific idea/localisation IDs.

No portrait or asset production route is applicable to this baseline audit.

## Focus, decision, idea, and asset coverage

The focus-hook watch includes GER, JAP, and SOV, and shared active-country registration is idempotent. No focus-tree change is required by the bounded startup design.

The decision categories, generic decisions, and major-country decisions are present and use shared registry/eligibility logic. The main category acceptance issue is not a missing decision file; it is the Japan registry loss that can occur during versioned migration.

The existing ledger icon, scripted GUI windows, and country idea icons are reused. The accepted plan explicitly requires no new visual asset for this baseline.

## Military, technology, industry, supply, and production

The baseline changes only repression buildings, country/state variables, ideas, and local pressure modifiers. It does not add armies, divisions, equipment, research, production lines, convoys, trains, fuel, railways, ports, or supply routes.

SOV's only bounded industrial map effect is ensuring level 1 gulag_labor_camp_network on states 644, 874, and 881. GER and JAP use the existing detention/concentration building path without opening later experimental or radicalized sites.

The installed HOI4 MCP package exposes no Technology Tree Viewer, so no technology-tree inspection was possible. Technology is not a dependency of this baseline, but that route remains an explicit unresolved tooling limitation.

## AI and playability

The monthly shared pulse is host-gated and active country registration is idempotent; country-specific focus-hook routing includes all three actors. The source-level Deaths and famine paths are bounded and use centralized site contribution, pool-factor, and death-percent constants.

No probability pass was completed. The required chaosx_ai_probability_auditor route was not callable in this subagent session, and the parent requested that tool work stop before a hoi4.probability_inspect pass. Therefore no MCP-proven claim is made about AI weights, event probabilities, decision scores, or long-run balance.

Static source review indicates the intended low-priority GER/JAP baseline and moderate SOV famine starting pressure, but those are not substitutes for the required scenario probability audit or live consumer validation.

## Validation evidence

The required offline wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding.

Vanilla documentation was consulted for triggers, effects, modifiers, localisation objects and formatters, script concepts and constants, on-action structure, event targets, and the relevant on-startup precedent.

Read-only map inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d577f6689247e98ca7cdf2fd2298e2850343a3349a737bd76d184c2473d830/0f6655ee30c14ff7ff9c564025dc163b938d13953774adaeea26c12acd23411a/map-inspect.b3694ee7fbc627de.json.

Map overview render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06862ee46ae6ff2778002719a3bbd5bcd567fefa7fd3c1da0f612bd363b84d11/e74c39259d4f73472825632624ff6e271645b981026bfcc416b59d45c77532f2/map-overview.b3694ee7fbc627de png.

The current read-only category GUI inspection covered GER and a SOV primary scenario with related GER/JAP scenarios. It found the expected category window and no visible-overlap diagnostic, but the workspace-wide GUI source graph is blocked by approximately 2000 unrelated diagnostics, including duplicate GFX index symbols and GUI_SCRIPTED_CONTEXT_INVALID findings. Current GUI inspect artifacts: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ff1293678f2dfa19e8d9eaf520c8de1866322bcb7fa41c86e8484c42c721e2b/8e0f4e47aa06f415d3fe0ad7ac67b33589cf646bff70933c227d09bffb597a33/gui-inspect.d07486f8c83ba4eb.json and hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f43f016cfc35be8d843e79d64fd8bc205bebeee2e4b6612c56de4b82842d3bb2/306a4cee2754a3eb612179046ba4b087c513d07251569be45d8a624d58bc8cca/gui-inspect.d07486f8c83ba4eb.json.

A previous repository GUI audit recorded category and full-ledger renders across 1280x720, 1366x768, 1600x900, and 1920x1080. Category artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81ce704abc07fb41f4e2b5f55084d16e7781529aa5377c5e1a4a7f4c321ac235/101b7b0b48df864b4d4dedb8d68021986193a3a3c10cef306af3fc26e3ec3442/repression_ledger_category_window-full.svg.

Narrow event inspection and render for soviet_gulag.1 completed with partial status and no event-specific blocking diagnostics. Event trace artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/55c9d3acb837a031cc5ebbe907b71c7888c9cbd8cff565320bfa30ec512cb8ea/8d85a81f5bbe02d3e526b089c5c75622fc888260b4099544fe2dd62b9352f379/event-trace-f4498b37c697.json. Rendered event state artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2440546f1fcc10a3743a84f6f3a0967919e2807c3d4ed4bc8c630cb89f7fb72/4764ff3e92a54d5453ab3016e4ed9eec87abca3c4d07781ba431c9f9b2fba400/event-state-f4498b37c697.png.

The current category GUI render attempt was aborted when the parent requested immediate handoff completion, so it must not be represented as current render evidence.

Live HOI4 save/in-game validation was not run by this subagent, in accordance with the repository boundary that the user owns live consumer validation.

## Missing, stale, or risky surfaces

1. Critical: repair migration re-registration for stored responsible countries whose current controller differs, specifically JAP responsibility on state 716 and any future JAP state 611 activation. Preserve genocide_responsible_country = JAP, re-enter that country scope for array membership, and separately classify current controller only where the design requires it. The fix must remain idempotent and must not assign the site to MAN or MEN merely because they control the state.

2. Secondary: genocide_initialize_system_if_needed only repeats the direct historical seed when the global initialization flag is absent. A legacy save that already has genocide_crisis_system_initialized but lacks camp_rework_1936_baseline_initialized may skip the direct baseline seed; the versioned migration cannot invent missing historical baseline states. Parent should decide whether the existing-save migration contract needs a narrow compatibility bridge.

3. Re-run the category GUI render after the Japan registry correction with GER, JAP, and SOV scenarios and record normal, hover, active, disabled, long-text, and missing-localisation states. Treat unrelated global GUI graph diagnostics separately from country-baseline acceptance.

4. Run the required chaosx_ai_probability_auditor/hoi4.probability_inspect and same-scenario comparison once tool work resumes. Until then, AI, weighted event, decision, and long-run balance claims remain unresolved.

5. Keep later escalation in events/germany_mengele.txt, events/japan_ishii.txt, and events/soviet_gulag.txt or their existing decision/event owners. The startup helper should not be expanded to add Auschwitz, Pingfang, experimental sites, or major threshold events.

## Changed files and ownership

Only this documentation handoff was added: docs/plans/repression_ledger_plans/subagent_handoffs/1936_country_baseline_audit_2026-08-27.md.

No gameplay files, IDs, state history, buildings, ideas, decisions, events, GUI definitions, localisation, assets, or map data were changed by this audit.

No commit was created; the parent retains integration, any scoped correction, final validation, and commit ownership.

## Post-patch re-audit — 2026-08-27

Audit mode: read-only source and HOI4 inspection after the migration patch described by the parent. Only this handoff was updated in this pass; no gameplay, localisation, GUI, map, or other agent files were edited.

### Migration exception and ordinary-registration safety

The current camp_rework_register_active_site implementation at common/scripted_effects/camp_repression_rework_effects.txt lines 624-740 first supplies ROOT as the responsible country only when no responsibility variable exists.

Its registration limit then requires the stored genocide_responsible_country to pass camp_rework_country_is_eligible and accepts either a matching tag = ROOT or the global camp_rework_migration_in_progress flag. The mismatch branch is therefore restricted to an eligible stored responsible country while migration is active.

The ordinary path remains strict because the mismatch branch is false whenever camp_rework_migration_in_progress is absent. A repository search found the migration flag set only at line 4438 inside camp_rework_run_versioned_migration and cleared at line 4553, with no other setter in common. The patch does not assign responsibility to the current controller and does not open ordinary registration to a mismatched owner.

The registration effect still writes the state into global.genocide_active_camp_states and then enters var:genocide_responsible_country to append PREV to that country's camp_active_site_states and global monthly-pulse registry. This is the required cross-country write during migration, and the country-array insertion remains duplicate-safe.

### Pool preservation and Japan state 716

The migration pass at lines 4427-4553 clears the global and country arrays, then iterates current controllers. It preserves an existing non-none camp_state_pool_type because its fallback block runs only when the state variable is absent or equal to camp_rework_pool_type.none.

The direct JAP initializer enters state 716 from the JAP scope, and genocide_activate_historical_baseline_detention_site stores genocide_responsible_country = PREV, where PREV is JAP in that fixed state scope. With ROOT = JAP during direct registration, the existing pool classifier sees that state 716 is not a JAP core and that its MAN controller and owner are subjects of JAP. The intended Japan-relative result is the country-kit trigger is_japan_china_manchuria_pool_state, with the shared stored pool value classified as camp_rework_pool_type.colonial_subject.

During migration, state 716 is encountered through current controller MAN. Its existing colonial_subject pool value is non-none, so the migration fallback does not overwrite it with a controller-relative occupied_noncore or core_fallback value. The new migration-only registration branch accepts the eligible stored JAP responsibility, leaves the pool value intact, appends state 716 to JAP.camp_active_site_states, appends it to global.genocide_active_camp_states, and re-registers JAP in global.camp_repression_active_countries during pass three.

This is source-level confirmation that JAP responsibility and the intended Japan-relative pool classification survive the versioned migration while MAN controls state 716. The same design remains safe for future state 611 activation while MEN controls that state, provided its direct activation first stores JAP responsibility and establishes its non-none Japan-relative pool value.

### GER, JAP, and SOV startup registration after migration

GER state 53 retains GER responsibility and is re-registered through the ordinary matching-tag branch because its current controller is GER. Quiet historical states 60 and 64 remain excluded by the migration pass's genocide_historical_quiet_camp guard, so no dormant site is promoted.

JAP state 716 is re-registered through the migration-only mismatch branch described above. Quiet state 611 remains dormant and is excluded because it retains genocide_historical_quiet_camp and has no active building or active-site condition.

SOV states 644, 874, and 881 retain SOV responsibility and are re-registered through the ordinary matching-tag branch because their current controllers are SOV. All three retain active gulag flags and the gulag_labor_camp_network building.

Pass three runs after all cross-country writes and registers every country with active state arrays for the monthly pulse, then recalculates its country values. The recalculate path synchronizes genocide_decisions_visible when active sites or visible reform work exist. Therefore the shared camp_repression_network_category remains visible for GER, JAP, and SOV after migration through has_camp_category_visible_action.

The JAP imperial_occupation_crisis category remains eligible through original_tag = JAP and the post-pass genocide_decisions_visible flag or active Japan route. The SOV gulag_and_mass_repression_system category remains eligible through its active-network, gulag-site-count, famine-pressure, and Soviet-site conditions. This is a source trace, not a live-save UI claim.

### Monthly Deaths and Soviet famine aftermath

camp_rework_monthly_global_pulse at lines 2286-2303 iterates global.genocide_active_camp_states once and calls camp_rework_apply_monthly_state_effects once for each valid active state. That shared state effect at lines 1934-1950 prepares the monthly death profile and owns the chaos_meter_register_state_civilian_deaths_percent call. The separate camp_rework_apply_state_death_burst path is event/decision burst logic, not a second monthly baseline path.

After migration, the global state array therefore contains GER 53, JAP 716, and SOV 644, 874, and 881. Those states continue to reach the shared monthly Deaths adapter, subject to the existing valid-active-site trigger and caps.

SOV state 881 retains camp_rework_soviet_famine_pressure and its famine state variables because migration clears registries, not state famine flags or state variables. SOV remains in global.camp_repression_active_countries after pass three. The monthly country dispatcher calls camp_rework_soviet_monthly_bridge at lines 665-714, which updates famine pressure through camp_rework_soviet_update_famine and refreshes famine state modifiers through camp_rework_soviet_refresh_famine_states. The famine aftermath therefore continues to feed state 881 after migration while the shared state pulse owns recurring Deaths.

### Category and display refresh

The category definitions at common/decisions/categories/genocide_crisis_categories.txt lines 9-16, 64-76, and 81-117 still use visible_when_empty = yes with their existing eligibility predicates. The shared trigger at common/scripted_triggers/camp_repression_rework_triggers.txt lines 369-381 continues to require an eligible country plus active network, visible reform, compatibility visibility, inherited network, or crisis evidence.

Migration pass three recalculates country values after registry reconstruction. The compatibility sync at common/scripted_effects/camp_repression_rework_effects.txt lines 2362-2379 sets genocide_decisions_visible when active count or visible reform work is present. The direct initializers also retain their idea and display refresh calls, so no new post-patch display writer is required.

### Read-only HOI4 evidence and blockers

The post-patch map inspection selected states 53, 60, 64, 88, 611, 716, 644, 874, and 881 and returned MAP_INSPECTED with state/region/network checks passing. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6650265b77bb7dc774c344c6a9023e0491860916bcc6835fa659776d7c77cbb7/018c5d4c90f17888dc411442b6dfc493f6ad17b1448f7d41ba2d613ff074e050/map-inspect.d657ca783504e847.json.

The same map run reported global locator validation failure with 1323 MAP_BUILDING_POSITION_INVALID and 1331 MAP_PORT_ADJACENT_SEA_INVALID diagnostics in existing map/buildings.txt data. These are workspace-wide diagnostics and not evidence of a baseline-state membership failure. No map write was performed.

A fresh read-only event trace for soviet_gulag.1 was attempted with selector kind event, direction both, helper expansion, depth 5, and bounded node/edge limits. The HOI4 event tool timed out after 180 seconds awaiting tools/call. This is the exact event-route blocker for this pass; the prior audit's partial soviet_gulag.1 trace/render artifacts remain the available event evidence, and no event source changed in the migration patch.

The installed HOI4 MCP package still exposes no Technology Tree Viewer. No technology inspection was needed for this registry-only patch.

No live HOI4 save or in-game category test was run. No probability pass was run because this post-patch request is a source/registry re-audit and the parent did not authorize additional weighted analysis.

### Remaining risks and evidence boundary

The migration exception is source-safe for the requested Japan case: it is gated by migration state and eligibility, preserves JAP responsibility, preserves the existing Japan-relative pool value, and leaves ordinary mismatched registration rejected. A live save is still required to prove the engine's nested ROOT/PREV scope behavior and final array contents.

The legacy-save case where genocide_crisis_system_initialized already exists but camp_rework_1936_baseline_initialized is absent remains unresolved from the previous audit. The versioned migration repairs registries for existing records but does not invent missing historical baseline records.

No gameplay patch was applied by this re-audit, no IDs were changed, no files other than this handoff were modified, and no completion claim is made beyond the source and read-only artifact evidence above.
