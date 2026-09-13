# Script-constant startup repair

Disposition: implemented within the user's authorization to repair confirmed startup errors while preserving active event work.

The installed scalar-constant contract requires a first `schema` entry with a `data` type.
Seven categories in `common/script_constants/016_brilliant_scientist_raid_lifecycle_constants.txt` lacked that schema.
One category in `016_brilliant_scientist_custom_technology_constants.txt` and two in `016_brilliant_scientist_technology_action_constants.txt` used `any_value` instead of `data`.
The repair supplies the required schemas and corrects those three field names.
Every existing category, constant identifier, numeric value and consumer is retained.
Integer-only agent, route, production and payload tables use `int`; tables containing fractions use `fixed_point`.

The parent reviewed installed `common/script_constants/documentation.md`, `documentation/script_concept_documentation.md`, vanilla scalar definitions and the valid country/state array precedents, alongside the required offline wiki references.
The focused Event 16 MCP trace returned `EVENT_INSPECTED_PARTIAL` at revision `d1b1deacde71076676d9f3a8922e7d45b97be37b957c82abd5293f57c6ee523a`; this is source-linked inspection, not complete event validation.

Launches 01–06 stopped before the main menu at the same native stack.
Launch 07, PID 22276, began at 2026-09-05 09:57:13 local time after this repair and remained alive through later database, script and flag loading.
Its fresh log advanced through 09:58:39 and exposed later errors that the earlier launches had not reached.
The parent then stopped this recorded startup process for repair; no campaign was entered and no visual main-menu acceptance is claimed.
The original files are archived in `pre_patch_schemas/`, and the fresh engine evidence is in `logs/launch_07/logs/`.

The earlier dump named a parsed Form48 constant object, but two reversible single-entry probes did not alter the failure and were rejected.
Those Event 6 files were restored byte-for-byte before this repair.
The successful later-stage launch supports these schema corrections as the repair for the observed early failure; it does not establish which malformed category individually caused it.

No balance target, weight, cost, duration, asset, localisation or gameplay design was changed.
No simplification or fallback was introduced.
The broader clean-start gate, all event/system playtests, save/reload coverage, teaser media and mechanics-guide updates remain incomplete.
