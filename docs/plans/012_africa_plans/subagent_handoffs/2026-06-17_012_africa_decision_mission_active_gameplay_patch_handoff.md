# Event 012 Africa Decision/Mission Active Gameplay Patch Handoff

Date: 2026-06-17
Agent role: Chaos Redux decision and mission subagent

## Scope

Write scope was limited to:

- `common/decisions/012_africa_decisions.txt`
- `localisation/english/012_african_union_l_english.yml`
- this handoff under `docs/plans/012_africa_plans/subagent_handoffs/`

No Event 010 files were touched. No staging or commit was performed.

## Files Changed

- `common/decisions/012_africa_decisions.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_decision_mission_active_gameplay_patch_handoff.md`

## IDs Touched

Decisions:

- `africa_rsa_secure_charter_supply`
- `africa_rsa_hold_mine_port_belt`
- `africa_rsa_force_allied_negotiators`

Localisation:

- `africa_rsa_secure_charter_supply_req_tt`
- `africa_rsa_secure_charter_supply_cost_tt`
- `africa_rsa_secure_charter_supply_cost_tt_blocked`
- `africa_rsa_secure_charter_supply_cost_tt_tooltip`
- `africa_rsa_secure_charter_supply_effect_tt`
- `africa_rsa_hold_mine_port_belt_req_tt`
- `africa_rsa_force_allied_negotiators_req_tt`

## Issue List

High severity:

- `africa_rsa_hold_mine_port_belt` set `africa_rsa_mine_port_belt_held` but did not require that flag to be absent. It could be repeated for war support and Liberation Momentum after the objective was already proven.
- `africa_rsa_force_allied_negotiators` set `africa_rsa_allied_negotiators_forced` but did not require that flag to be absent. It could be repeated for legitimacy and cohesion.

Medium severity:

- `africa_rsa_secure_charter_supply` behaved like a flat PP store: PP converted into Liberation Momentum and war support on cooldown without consuming logistics, equipment, map proof, or another scarce war resource.
- `africa_rsa_secure_charter_supply` relied on category visibility for the active civil war state. A narrow availability check now also requires `africa_rsa_civil_war_active`.
- Several Event 012 decisions outside the patched RSA trio still combine normal `cost = constant:...` with custom cost triggers/text. The offline wiki warns that custom cost should not be combined with normal cost, while vanilla examples often implement custom costs without a regular PP cost. This needs a parent-level cost model pass because it affects many decisions and localisation keys.

Lower severity:

- RSA victory settlement visibility depends on the civil war emergency category staying visible after continental victory. If a helper later clears `africa_rsa_civil_war_active`, `africa_rsa_prepare_victory_settlement` and `africa_rsa_pretoria_deadline_mission` can be hidden before the victory flow resolves.
- Some helper snippets outside write scope looked potentially malformed or incomplete during inspection. I did not patch outside the allowed files.

## Patched Behavior

Before:

- `africa_rsa_secure_charter_supply` spent PP only and granted Liberation Momentum plus war support every emergency cooldown.
- `africa_rsa_hold_mine_port_belt` could be repeated after the belt was already held.
- `africa_rsa_force_allied_negotiators` could be repeated and did not require the mine-port belt proof.

After:

- `africa_rsa_secure_charter_supply` also requires the RSA civil war to be active and consumes support equipment plus train equipment before applying the morale/logistics reward.
- `africa_rsa_hold_mine_port_belt` is one successful proof of control. Once `africa_rsa_mine_port_belt_held` is set, the decision is no longer available.
- `africa_rsa_force_allied_negotiators` requires the mine-port belt proof and is blocked once `africa_rsa_allied_negotiators_forced` is set.

## Decision Category Lifecycle Notes

- `africa_rsa_civil_war_emergency_category` is an event-route category for the RSA civil war branch. It is hidden until the civil war branch is active and contains emergency support, proof-of-control, allied negotiator, settlement, and deadline content.
- The patched decisions now have their own lifecycle guards instead of relying only on the category. This reduces clutter and repeat farming after one-time branch milestones are complete.
- Parent follow-up: confirm the intended moment for clearing `africa_rsa_civil_war_active`. If that flag is cleared immediately on continental victory, the victory settlement decision and Pretoria deadline mission may need a separate post-war category or a widened category visibility trigger.

## Mission Quality Notes

`africa_rsa_pretoria_deadline_mission`:

- Owner: RSA continental side.
- Category: `africa_rsa_civil_war_emergency_category`.
- Region/objective: hold the Transvaal, Cape, and Natal key states through the Pretoria deadline.
- Requirement: continental victory, allied peace not completed, and no prior Pretoria deadline resolution.
- Duration: `constant:africa_decision_days.rsa_pretoria_deadline`.
- Success: marks allied peace completed and grants high legitimacy/cohesion settlement gains.
- Failure: records deadline failure and applies the pre-defined failure effect.
- Duplicate risk: low from the mission itself because it requires no prior resolution and sets the completion flag. Visibility lifecycle remains the main risk if the parent later cleans up the active civil war flag earlier.

`africa_rsa_hold_mine_port_belt`:

- Owner: RSA continental side.
- Category: `africa_rsa_civil_war_emergency_category`.
- Region/objective: requires control of the Transvaal, Cape, and Natal key states.
- Requirement: continental RSA side, active civil war, and no previous mine-port belt success after this patch.
- Duration: instant decision, not timed mission.
- Success: sets `africa_rsa_mine_port_belt_held`, grants Liberation Momentum and war support.
- Failure: no mission failure path because it is an instant proof decision.
- Duplicate risk: low after patch.

`africa_rsa_force_allied_negotiators`:

- Owner: RSA continental side.
- Category: `africa_rsa_civil_war_emergency_category`.
- Region/objective: political pressure after mine-port belt control is proven.
- Requirement: continental RSA side, active civil war, mine-port belt already held, and no previous forced-negotiator success after this patch.
- Duration: instant decision, not timed mission.
- Success: sets `africa_rsa_allied_negotiators_forced`, grants legitimacy and cohesion.
- Failure: no mission failure path because it is an instant pressure decision.
- Duplicate risk: low after patch.

## Cost and Requirement Clarity Notes

- `africa_rsa_secure_charter_supply` now has a custom cost tooltip for support equipment and train equipment. The localisation describes the resource consumption and the branch state requirement.
- The support equipment and train amounts reuse existing Event 012 constants:
  - `constant:africa_force.league_aid_support_equipment`
  - `constant:africa_force.aid_corridor_trains`
- The train gate uses `train_equipment` and the removal effect subtracts `train_equipment_1`, matching the existing aid-corridor pattern in the decision file. Parent follow-up: if advanced trains are expected to satisfy the cost reliably, centralize this through an equipment-removal helper outside this subagent write scope.

## AI Validity and Route-Lock Notes

- The patched availability guards prevent AI from repeatedly choosing one-time RSA milestone decisions after their flags are set.
- `africa_rsa_force_allied_negotiators` now depends on `africa_rsa_mine_port_belt_held`, which makes AI sequencing safer and less likely to skip straight into the diplomatic reward.
- No AI weights were rewritten. Existing AI weights remain usable because the blocked repeat paths now fail availability rather than depending on weight tuning.
- Parent follow-up: run a broader AI validity pass over Authority Atlas, Bestiary, sponsor, and route-map decisions because several of those systems still depend on dense mapped values and route flags that were outside this narrow RSA patch.

## Localisation and Tooltip Gaps

- Touched RSA tooltips now mention active civil war gating, one-time mine-port belt proof, one-time negotiator pressure, and logistics consumption.
- Broader Event 012 localisation still contains many mapped values and route-specific conditions that should be reviewed for readability. This was not patched because the write request was narrow and the localisation file already had unrelated in-progress changes.

## Cleanup and Exploit-Risk Notes

- The two one-time RSA reward decisions now close their own loops by checking the flags they set.
- `africa_rsa_secure_charter_supply` remains repeatable by design, but it is no longer a pure PP-to-reward exchange. It now consumes material logistics and requires the active civil war state.
- Parent follow-up: review `africa_on_rsa_civil_war_end` and related helpers outside this write scope to ensure stale civil war flags, settlement flags, and emergency category visibility are cleaned in the intended order.
- Parent follow-up: inspect scripted effects/triggers for Event 012 after the current dirty worktree stabilizes. During read-only inspection, several helper snippets outside the allowed files appeared potentially malformed or incomplete, but I did not patch or fully validate them because of scope limits.

## Concrete Recommended Fixes

Immediate follow-ups in allowed Event 012 surfaces:

- `common/decisions/012_africa_decisions.txt`: audit all `custom_cost_trigger` decisions that also use `cost = constant:...`; either confirm this pattern works in the current game version or split PP cost into the custom cost model consistently.
- `common/decisions/012_africa_decisions.txt`: run a full pass over Authority Atlas and Bestiary decision loops for repeated rewards, cooldown abuse, and whether mapped values visibly affect unlocks/blocks.
- `common/decisions/012_africa_decisions.txt`: verify all targeted decisions have valid live targets and close when target countries are dead, integrated, or no longer on the relevant route.

Parent-owned follow-ups outside this subagent write scope:

- `common/scripted_effects/012_africa_effects.txt`: validate RSA civil war cleanup and confirm whether `africa_rsa_civil_war_active` intentionally remains set through the settlement/deadline phase.
- `common/scripted_triggers/012_africa_triggers.txt`: validate Event 012 helper structure and route trigger closures before merging the current Event 012 tranche.
- Focus/event integration files: if a focus or event unlocks the RSA emergency branch, confirm the patched flags are set and cleared in the same lifecycle order expected by the category.

## Validation Run

- Inspected the patched RSA decision block in `common/decisions/012_africa_decisions.txt`.
- Inspected the touched localisation keys in `localisation/english/012_african_union_l_english.yml`.
- Checked brace balance for both touched gameplay/localisation files; both balanced to zero.
- Checked that the touched localisation file still begins with UTF-8 BOM bytes.
- Checked the decision file for unsupported comparison-operator tokens after the patch.

## Skipped Meaningful Validation

- No game load or in-engine run was performed from this subagent turn.
- No full Event 012 decision audit was completed; the safe patch targeted RSA branch exploit loops and one PP-store decision.
- No scripted helper, focus, event, or on-action file was changed because those paths were outside the allowed write scope.

## Remaining Issues

- Broad Event 012 cost modelling still needs a dedicated pass, especially where regular PP cost and custom costs are mixed.
- Authority Atlas and Bestiary loops still need a full exploit and readability audit.
- RSA emergency category lifecycle should be confirmed against the helper that ends the civil war.
- Targeted decisions outside the patched RSA trio need a route-lock and dead-target validity pass.
