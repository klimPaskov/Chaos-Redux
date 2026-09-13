# Acid Rain building damage parser repair

Disposition: implemented; launch19 native parser acceptance verified, campaign behavior pending.
The user authorized safe corrections of observed startup errors and direct source edits.

Twelve state building comparisons in acid_rain_apply_state_damage use check_variable around the original building_level@TYPE expression.
The bounded cursor order, comparison thresholds, state scope, damage receipts, and pressure arithmetic are unchanged.
Installed dynamic-variable documentation and vanilla state-scope building_level comparisons support this syntax.

The twelve damage_building calls previously passed acid_rain_damage_one to a field documented as a literal float.
Each caller now initializes dynamic_building_damage_type from its original building token and invokes damage_state_building_dynamic.
One dominating amount initializer copies acid_rain_damage_one before the bounded loop.
The shared helper interpolates these required temporary inputs through meta_effect and leaves them unchanged.
No rounding, clamp, random targeting, fallback damage amount, or new target selection was added.
The current exact integer amount is preserved; arbitrary fractional or large numeric serialization has not been validated.
See dynamic_building_damage19_handoff.md for the installed vanilla references, helper contract, and source hashes.

Parent review checked the exact twelve comparison replacements and twelve caller replacements against separately archived immediate backups.
The two source stages and their hashes are recorded in event33_building19.json and event33_dynamic_damage19.json.
MCP narrow Event 33 inspection and rendering returned partial projections with helper expansion absent.
The required matching revision comparison returned EVENT_REVISION_NOT_CACHED with zero artifacts.
These routes do not establish runtime building damage or ledger correctness.
Actual damage, cursor advancement, receipts, and repeated-pulse behavior remain live campaign test cases.

Launch19 reached frontend startup and cleared all24 repeated invalid-building-trigger records and all24 malformed damage-amount records.
The Acid Rain source and shared helper stayed byte-identical during the run.
See launch_19_results.md for runtime limits and archived logs.
