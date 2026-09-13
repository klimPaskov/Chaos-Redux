# Startup localisation repair handoff

Status: source repairs implemented; fresh main-menu startup confirmation is parent-owned and pending.

## Scope and preservation

Owned common/scripted_localisation and localisation only.
These three files existed untracked before this pass, so Git diff cannot isolate their changes.
Original bytes are retained beneath baseline/localisation/common/scripted_localisation in this QA folder.
No commit was made.

## Root causes and changed files

### common/scripted_localisation/016_clone_maturation_localisation.txt

Changed unsupported `localisation_key` fields to engine-recognized `localization_key`.
All trigger conditions, constants, inclusive affordability comparisons, selector names, and referenced key values remain unchanged.

Affected keys:

- `clone_maturation_political_power`
- `clone_maturation_political_power_blocked`
- `clone_maturation_support_equipment`
- `clone_maturation_support_equipment_blocked`
- `clone_maturation_fuel`
- `clone_maturation_fuel_blocked`
- `clone_maturation_civilian_factories`
- `clone_maturation_civilian_factories_blocked`

### common/scripted_localisation/016_mengele_conventional_incident_localisation.txt

Changed unsupported `localisation_key` fields to engine-recognized `localization_key`.
All trigger conditions, constants, inclusive affordability comparisons, selector names, and referenced key values remain unchanged.

Affected keys:

- `mengele_event016_incident_technical_political_power`
- `mengele_event016_incident_technical_political_power_blocked`
- `mengele_event016_incident_technical_support_equipment`
- `mengele_event016_incident_technical_support_equipment_blocked`
- `mengele_event016_incident_technical_fuel`
- `mengele_event016_incident_technical_fuel_blocked`
- `mengele_event016_incident_technical_civilian_factories`
- `mengele_event016_incident_technical_civilian_factories_blocked`
- `mengele_event016_incident_industrial_political_power`
- `mengele_event016_incident_industrial_political_power_blocked`
- `mengele_event016_incident_industrial_support_equipment`
- `mengele_event016_incident_industrial_support_equipment_blocked`
- `mengele_event016_incident_industrial_fuel`
- `mengele_event016_incident_industrial_fuel_blocked`
- `mengele_event016_incident_industrial_civilian_factories`
- `mengele_event016_incident_industrial_civilian_factories_blocked`
- `mengele_event016_incident_exotic_political_power`
- `mengele_event016_incident_exotic_political_power_blocked`
- `mengele_event016_incident_exotic_support_equipment`
- `mengele_event016_incident_exotic_support_equipment_blocked`
- `mengele_event016_incident_exotic_fuel`
- `mengele_event016_incident_exotic_fuel_blocked`
- `mengele_event016_incident_exotic_civilian_factories`
- `mengele_event016_incident_exotic_civilian_factories_blocked`
- `mengele_event016_incident_biological_political_power`
- `mengele_event016_incident_biological_political_power_blocked`
- `mengele_event016_incident_biological_support_equipment`
- `mengele_event016_incident_biological_support_equipment_blocked`
- `mengele_event016_incident_biological_fuel`
- `mengele_event016_incident_biological_fuel_blocked`
- `mengele_event016_incident_biological_civilian_factories`
- `mengele_event016_incident_biological_civilian_factories_blocked`

### common/scripted_localisation/021_random_civil_war_localisation.txt

Wrapped four bare comparisons in `check_variable = { variable > 0 }` at lines 103, 111, 124, and 137.
Affected selectors: `event021_GetCrisisTargetName` (two conditions), `event021_GetPriorityFrontName`, and `event021_GetRailMissionStateName`.
Preserved the state variables, strict zero thresholds, names, fall-through values, and all dynamic target tokens.

## Task-specific validation

Compared patched bytes against a transformation of each original-byte backup and confirmed that only the stated corrections occurred.
Resolved every literal localization_key reference in all three files against installed repo localisation: no missing keys and no duplicate key definitions among those references.
Offline core wiki pages were consulted, with Localisation and Data structures guidance and installed vanilla triggers_documentation.md check_variable syntax as the targeted references.
Installed vanilla loc_formatter_documentation.md and loc_objects_documentation.md were consulted alongside a vanilla scripted-localisation shorthand comparison precedent in BBA_ethiopia_scripted_loc.txt.
Used chaos-redux-debug-playtest, chaos-redux-events, and chaos-redux-subagents guidance.

Read-only event MCP calls succeeded for Event 016 lint/render and Event 021 lint.
They returned EVENT_INSPECTED_PARTIAL / EVENT_RENDERED_PARTIAL and validation.passed=false because large-workspace helper projections and lifecycle passes were deferred.
This is not full engine or visual confirmation of repaired selector output.

Useful artifact URIs:

- Event 016 lint: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f37a59ec98e563df2977c2195d365f7a21b276005bc047cd2e35e7198d0de55a/53635e74fced1df1877fe865144a95cd1ceb66cde226e6d47f2599554119bffa/event-lint-4bccb6ec7fe1.json
- Event 016 options render manifest: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ada6519e8bbcf0f9d658f735a2de8efa5f1be4222f89b0e53eaf32dc0cf23ee/94a810f3f45c2535a87ee7184749375918cfc3e958a2ed6b537a3f238083eda0/event-options-4bccb6ec7fe1-manifest.json
- Event 021 lint: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21e3fe49d911b74698a491f97669ff580f3bf0a0d14689f85d9ee4a35eb1660d/cbac511aead2e7b76ace7d3530bff9c030304af65c006bb34003e90ee4f34a5d/event-lint-4bccb6ec7fe1.json

## Audit categories and before/after

Before: Event 016 cost-selector key fields were rejected by the loader, and Event 021 attempted to evaluate state-id variable names as native triggers.
After: Event 016 fields use supported spelling, and Event 021 comparisons use the documented variable trigger.
Missing keys: none in checked references.
Duplicate keys: none in checked references.
Scripted localisation issues: 40 unsupported field names and four bare variable comparisons repaired.
Dynamic text added: none; existing target-name and variable tokens preserved exactly.
Cross-surface or spreadsheet wording changes: none, because no player-facing strings changed.
Encoding concerns: none introduced; byte comparison includes existing encoding and line endings.
Prose categories (vagueness, bloat, obvious explanation, repetition, overcomplication, style rules): no prose rewritten in this loader-syntax repair.
Sourced quotations: no quotation-bearing text edited.
Balance and gameplay meaning: unchanged.

## Remaining checks and uncertainty

Parent must review the fresh startup batch to confirm that these loader errors disappeared and supply any remaining localisation errors.
GUI layout/overflow was not claimed verified, since this pass changed loader syntax and did not edit GUI strings or layout.
No technology surface is in scope, so standalone Technology Tree Viewer availability is not an acceptance check for this patch.
Unresolved wording decisions: none.
Plan handoff: none needed; no missing mechanic discovered.
No simplifications or fallbacks were made.

## Additional named reason integration

Parent accepted missing reason registrations within startup loader scope.
Changed common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt and localisation/english/chaosx_chaos_meter_l_english.yml.
Both files had preexisting edits and their complete pre-patch bytes were backed up under baseline/localisation.
Added nine death reason branches each to GetChaosMeterDeathsSelectedCause and GetChaosMeterDeathsDetailCause, plus five murder-mystery branches to GetChaosMeterHistoryReason.
Parent owns numeric registrations in chaos_meter_constants.txt and Death counter registration.

New localisation keys and wording:

- `chaos_meter.deaths.cause.asteroid_main_impact`: Main asteroid impact
- `chaos_meter.deaths.cause.asteroid_main_ring_one`: Main asteroid impact, first damage ring
- `chaos_meter.deaths.cause.asteroid_main_ring_two`: Main asteroid impact, second damage ring
- `chaos_meter.deaths.cause.asteroid_main_ring_three`: Main asteroid impact, third damage ring
- `chaos_meter.deaths.cause.asteroid_fragment_impact`: Asteroid fragment impact
- `chaos_meter.deaths.cause.asteroid_fragment_ring_one`: Asteroid fragment, first damage ring
- `chaos_meter.deaths.cause.asteroid_fragment_ring_two`: Asteroid fragment, second damage ring
- `chaos_meter.deaths.cause.asteroid_rescue_failure`: Deaths during asteroid rescue operations
- `chaos_meter.deaths.cause.acid_rain`: Acid rain exposure
- `chaos_meter.history.reason.special.murder_mystery_entry`: Leader assassination
- `chaos_meter.history.reason.special.murder_mystery_reversal`: Murder investigation compromised
- `chaos_meter.history.reason.special.murder_mystery_network`: The Assassin State emerges
- `chaos_meter.history.reason.special.murder_mystery_world_end`: The Assassin State begins its final war
- `chaos_meter.history.reason.special.murder_mystery_defeat`: The Assassin State is defeated

Before: missing named registrations could not resolve to the event-specific reasons.
After: the selectors recognize each distinct new reason and reference a unique English label.
The murder labels follow the actual mapped source consumers: opening assassination, compromised investigation, territorial Assassin State reveal, final war, and defeat.
Validation confirms only 23 new branches were inserted, all existing source bytes outside these additions remain identical, old YML bytes are preserved as a prefix, and the 14 new keys exist once.
No existing prose, quotation, formatting or dynamic tokens changed.
No new dynamic values, icons, campaign counters, GUI layout or spreadsheet changes were authored.
No vagueness, bloat, repetition, obvious explanation, overloaded sentence or style-rule repair applies to existing text in this additive label pass.
No simplifications were made.
Campaign counters and GUI appearance were not visually tested, and fresh startup confirmation remains parent-owned.
Shared GUI MCP rendering was not attempted because this bounded pass adds labels to the existing selector contract and does not redesign the shared surface.

Parent subsequently registered all specified constants.
Cross-check confirmed Death IDs 26 through 34 and murder History IDs 217 through 221, with two death-selector branches per reason and one history branch per reason.
Parent retains campaign cause-breakdown expansion outside startup parser scope.

## Cycle 02 portal containment collisions

Cycle 02 reached the main menu but text.log reported both definitions of eight duplicate English keys.
Changed localisation/english/016_brilliant_scientist_projects_l_english.yml and localisation/english/chaosx_raids_l_english.yml.
Original bytes backed up under baseline/localisation before this pass.
Canonical ownership is chaosx_raids_l_english.yml, which owns Portal Warfare raid presentation.
Removed the eight repeated entries from the projects file and retained one definition per key in raids.
Used the clearer existing projects wording, with an explicit original-defender requirement matching brilliant_scientist_portal_beachhead_can_be_sealed_by_root.

Final canonical keys:

- `brilliant_scientist_portal_containment_category_desc`: Enemy transit corridors remain open behind our lines. Recapture the breach province, then seal its terminal to prevent further use.
- `brilliant_scientist_seal_recaptured_portal_breach_cost`: £command_power §Y25§!
- `brilliant_scientist_seal_recaptured_portal_breach_complete_tt`: Seal the hostile transit corridor. Captured factories and facilities remain where they were taken.
- `brilliant_scientist_seal_recaptured_portal_breach_desc`: Commit engineers and command staff to isolate the hostile transit terminal in [From.GetName]. We must hold the breach province throughout the twenty-one-day operation.
- `brilliant_scientist_seal_recaptured_portal_breach_cancel_tt`: Sealing stops. The breach remains open while its participants are still at war.
- `brilliant_scientist_seal_recaptured_portal_breach_requirements_tt`: We are the original defender and control the breach province. The enemy corridor remains active, and no sealing operation is underway. Requires £command_power §Y25§!.
- `brilliant_scientist_seal_recaptured_portal_breach`: Seal the Recaptured Portal Breach
- `brilliant_scientist_portal_containment_category`: Portal Containment

Task-specific validation: all eight collided keys resolve exactly once across English localisation.
Byte-backed comparison confirmed every line outside those eight key definitions in both files is unchanged.
Read the live decision definition, category registration, sealing trigger, and sealing effect before selecting wording.
Prose repair: removed saved-record and transient-record implementation terminology, an unnecessary semicolon, and overloaded raid wording by retaining the existing direct description.
Preserved [From.GetName], command-power icon, color tokens, 25 cost, twenty-one-day duration, continuous province control, retained captures, and active-breach cancellation meaning.
No sourced quotations were changed.
No missing keys, new scripted-localisation issue, dynamic value change or catalog mismatch was introduced.
Fresh startup collision confirmation remains parent-owned.
No simplifications, gameplay changes, GUI changes, key renames or commit.

## Event 025 category registration labels

Added three category names and descriptions to localisation/english/025_alien_technology_in_antarctica_l_english.yml for existing outpost reconfiguration, weather-data exchange, and expedition withdrawal actions.
Inspected exact category registration and child decision definitions and existing Event 025 localisation.
Backup retained under baseline/localisation, with all previous file bytes preserved as a prefix.

Added keys:

- `chaosx_nr25_outpost_emphasis_category`: Outpost Priorities
- `chaosx_nr25_outpost_emphasis_category_desc`: Configure the outpost for resupply, surveys, signals, protection, or travel between Antarctic sectors.
- `chaosx_nr25_cooperation_category`: Expedition Cooperation
- `chaosx_nr25_cooperation_category_desc`: Exchange verified weather and route data with another expedition.
- `chaosx_nr25_utility_category`: Expedition Safety
- `chaosx_nr25_utility_category_desc`: Evacuate the expedition when the Antarctic recovery race becomes too dangerous.

Task-specific validation: all six keys resolve once across English localisation and the pre-patch file bytes remain unchanged.
No prior prose, sourced quotation or dynamic tokens altered.
No gameplay, event catalog or GUI layout changes.
No simplifications or commit.
Fresh startup validation remains parent-owned.
