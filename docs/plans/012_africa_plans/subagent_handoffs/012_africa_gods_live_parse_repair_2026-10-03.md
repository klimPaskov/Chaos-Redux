# Event 012 live parser repair

Disposition: source repair implemented; post-commit native error-log evidence remains with the orchestrator.
Acceptance basis: the orchestrator's urgent 2026-10-03 live QA reports 527 Event 012 errors and requires correction before tribute testing resumes.

The parent introduced invalid parameterized scripted-effect and scripted-trigger calls in `46ea61997` and `1e0c71e20`.
The installed engine does not accept those block arguments or their dollar-delimited bodies.
The resulting parser failures also hid definitions later in the affected source files.
The prior source audits did not establish engine validity and are superseded on that point by this live evidence.

Every affected Gods helper now uses explicit caller-set temporary inputs and a plain `= yes` invocation.
The armour capacity helper reads `gods_of_africa_armor_required_amount`.
The chassis measurement and sender read `gods_of_africa_armor_archetype`, with six centralized integer IDs and a private bare-token scripted-localisation mapping.
Only native `meta_trigger`/`meta_effect` text injection supplies the dynamic equipment token.
The floor helper reads and updates temporary `gods_of_africa_equipment_amount`, which the caller copies back to its normal amount field.
The equipment classifier reads temporary `gods_of_africa_family_to_check`.
Response capture reads temporary `gods_of_africa_report_kind`, `_amount`, and `_balance`.
All callers, including the scripted-localisation classification calls, were converted.
No material amount, reserve, deadline, family, report, or AI weight was simplified or removed.

The two existing Gods reception-service functions are committed from the Event 012 addition at the end of `migration_adapter_effects.txt`, preserving the unrelated earlier shared-file edit.
Their native capacity/food-safety dependencies were checked against committed definitions.
The mission names are registered in `common/synchronized_dynamic_tokens/012_africa_gods_tokens.txt`, along with dynamically used chassis tokens absent from the shared token file.
`docs/events/012_africa/strange_forces.md` records the supplied native limitation: `pan_sappers` and `oracle_recon` are support companies, whose custom entities do not appear as division line-battalion models.
Their units were not redesigned.

The five repaired effects/trigger files received a complete token/brace traversal, top-level definition review, and a nested-call check that rejects block arguments to these helpers.
The traversal retained 101 core effect blocks, four equipment effect blocks, two report effect blocks, three equipment trigger blocks, and 59 core trigger blocks, with no leaked coded-trigger definitions at top level.
Scripted localisation and the full migration adapter were also traversed.
The Gods effects and triggers contain no dollar-delimited parameter tokens.
This is source parse evidence, not a claim of a clean native launch or functional tribute acceptance.

The global scan still finds such tokens in other owners' current files: `032_missiles_operations_effects.txt`, `032_missiles_operations_triggers.txt`, `032_missiles_preparation_cost_triggers.txt`, and `camp_administration_origin_effects.txt`.
Those are reported to the orchestrator and excluded from this ownership-limited commit.
The full mod cannot be claimed clean from this scoped repair.

Installed references read directly are `documentation/effects_documentation.md:4833-4851` for `meta_effect`, `documentation/triggers_documentation.md:6404-6422` for `meta_trigger`, and `documentation/script_concept_documentation.md` for the installed concept surface.
Their earlier recorded SHA-256 revisions are retained in the adjacent helper contracts; the urgent live evidence supplies the definitive correction to the erroneous parameter assumption.
The user's provided meta-script example is followed for the bare-token localisation substitution.
No game was launched and no log or save was requested.

The unrelated unfinished lifecycle patch is parked outside the repository at `C:/Users/klimp/AppData/Local/Temp/gods_lifecycle_parked_20261003.patch`; it is not included in this repair.
The complete Gods goal remains incomplete, including lifecycle, mobile/artillery, AI scenario, and native acceptance work.
Skills used: events, decisions/missions, and shared Git commit.
