# Event 012 high-chaos achievement owner patch handoff

## Scope and status

This handoff covers only exact runtime owners for Event 012 high-chaos achievement rows 35-40. The patch records receipts after real formation creation, package settlement, package restoration, and Stoneborn defeat. No achievement trigger or central achievement-effect file was edited. No commit was created.

## Files changed

- `common/scripted_effects/012_africa_action_effects.txt:6887-6924` adds `africa_achievement_record_strange_force_formation` and calls it from `africa_strange_force_finalize_result` only after `africa_strange_force_spawn_result > 0` and the normal achievement launch gate. Stone, gorilla, pan-sapper, forest, and disaster-warden creations map to the existing achievement family enum. Riverborn, oracle recon, and plague carriers have no corresponding enum and are intentionally not mapped.
- `common/scripted_effects/012_africa_elephant_effects.txt:74` records the elephant family only after the host guard's exact `create_unit` block completes under the normal achievement launch gate.
- `common/scripted_effects/012_africa_priority_member_force_effects.txt:238,261` records the elephant family after the primary and reserve priority-member `create_unit` blocks, respectively, under the same gate.
- `common/scripted_effects/012_africa_promoted_tiera_effects.txt:305` registers a revealed promoted Tier A package as `africa_registered_high_chaos_actor`, the exact package identity consumed by the high-chaos action and constitutional-member surfaces.
- `common/scripted_effects/012_africa_promoted_tiera_settlement_effects.txt:55` records the nonhuman constitutional-member receipt after the accepted league settlement. Lines 175, 192, and 214 write the Green owner-ready gate, Stoneborn constitutional milestone, and Stoneborn erasure witness from their exact post-settlement and defeat owners.

## Existing exact owners deliberately preserved

- Row 38 weather-army victories and weather-war settlement remain owned by the existing Event 012 action and `common/on_actions/012_africa_world_order_on_actions.txt` callbacks. This patch does not duplicate those witnesses.
- `common/scripted_effects/013_natural_disasters_effects.txt:5343-5367` already records Event 012 civilian weaponisation only after a matching hostile caller causes positive civilian deaths. The pre-existing `remove_dynamic_modifier` fixes at lines 6012 and 6022 were preserved and are not part of this patch.
- `common/scripted_effects/012_africa_disease_effects.txt` was audited but left unchanged. Its native lifecycle has no exact owner for the three disease disqualifiers below, and adding a generic seed or accident inference would be a proxy. Existing central action receipts remain outside this bounded owner patch.

## Rows 35-40 coverage

- Row 35 now receives real nonhuman-family witnesses from actual strange-force `create_unit` success and promoted-package force creation. The great-power victory and human-caricature or extermination disqualifiers are not inferred here.
- Row 36 receives the missing actual elephant formation receipt from host and priority-member unit creation. Terrain-region crossings, supply maintenance, protection victory, and their negative disqualifiers have no exact owner in the named elephant files and are not fabricated from stockpile, template, or package flags.
- Row 37 receives the exact Green post-settlement owner-ready witness. Civilian weaponisation is owned by the existing Event 013 impact callback above. No forest-rampage proxy was added.
- Row 38 remains covered by the existing action and world-order owners; no duplicate call was added.
- Row 39 remains fail-closed for the disease disqualifiers. The native adapter has no explicit `africa_achievement_deliberate_uncontrolled_civilian_release`, `africa_achievement_irreversible_disease_outcome`, or `africa_achievement_terminal_disease_outcome` owner. These are impossible-by-design in this scope rather than inferred from ordinary deliberate battlefield dissemination, laboratory accidents, failed actions, or active flags.
- Row 40 receives the Stoneborn constitutional milestone only from the package's post-settlement restoration owner and records erasure only from the exact capitulation cleanup owner. Rights-violation and human-member-war disqualifiers have no exact owner in the promoted Tier A settlement files and are not inferred from refusal, rivalry, or defeat alone.

## Validation and limitations

Targeted searches verified every added call site, the existing Event 013 civilian-death witness, and preservation of the two pre-existing dynamic-modifier fixes. The touched Clausewitz blocks were inspected for balanced scope structure. Live HOI4 validation remains the user's responsibility, and no game launch or save mutation was performed.

No new script constants, event targets, global targets, cleanup registries, or shared dynamic helpers were introduced. The strange-force adapter uses the existing requested-kind temporary value and the existing achievement family constants.

The existing central action family matrix remains untouched by design. It may still record action-level family receipts in addition to the new post-creation witnesses; the new hooks ensure that real materialized formations are represented without relying on action success alone.
