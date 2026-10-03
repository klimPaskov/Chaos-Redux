# Event 021 evolution log actor

`event021_select_verified_evolution_log_actor` selects presentation context for the existing evolution logger without changing evolution admission, timing, stage, weights, or Chaos.
It accepts ANY scope, including the global host scheduler.
The caller must initialize the temporary scalar `events_log_evolution_has_actor = constant:random_civil_war_value.zero` before invocation so its output survives the helper call.
The helper resets that scalar and leaves it zero when no verified live participant exists.

It requires aligned front ID, actor, canonical host, crisis ID, and status arrays before any indexed read.
It scans the registered front IDs in their existing order and chooses the first active row whose live human canonical host matches its positive crisis ID and whose actor has the matching positive immutable front ID and crisis ID, active receipt, theater registration flag, and theater-array membership.
Human Event 006 participants remain admissible through the shared actual-nonhuman exclusion.
No country is selected merely because it is the caller or owns the global scheduler.
The selector changes no registry entries or actor state.

For a proved row it saves the regular `events_log_evolution_actor` country target and sets the caller-owned indicator to one.
The three parent evolution callbacks invoke the shared recorder immediately afterwards.
When no row passes, the recorder uses its existing no-actor branch even if a stale regular target exists earlier in the effect chain.
Regular targets expire with their effect chain and are not manually cleared.
The helper's other temporary fields are private within its call frame and are not outputs.

Example: initialize `events_log_evolution_has_actor`, call this helper, then call `record_events_log_evolution_entry` from a successfully enabled parent evolution callback.
Each parent callback retains its own recorded flag, stage, and tier.
Each callback also preinitializes the temporary event ID and type before `event021_prepare_evolution_log_context`, then explicitly assigns its stage and tier after that call.
This preserves the shared Event 021 identity through conservative scripted-helper temporary lifetime without changing the callback's eligibility or progression.
This selector supplies accurate actor metadata and does not implement active-war front creation or its management outcome.

The native array loop contract is installed `documentation/effects_documentation.md`, lines 4279-4312, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Temporary output lifetime follows offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Variable types at line 440, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
The existing shared logger's `events_log_evolution_has_actor` branch is the presentation precedent.
