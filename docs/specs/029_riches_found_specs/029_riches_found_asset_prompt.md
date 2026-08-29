# Event 029 asset-production prompt

Create the complete visual asset package for Chaos Redux Event 029, Riches Found.

Read the repository `AGENTS.md`, `chaos-redux-event-assets`, the complete `docs/specs/029_riches_found_specs/` package, and the current installed-vanilla and Chaos Redux references for every requested asset type before production.

Use context-free project subagents with `fork_context=false`.

Route generated non-icon art to `chaosx_generated_event_art`.

Route gameplay icons, state-modifier icons, idea icons, evolution icons, and achievement icons to `chaosx_icon_artist`.

Do not route any asset to the portrait worker because Event 029 requires no character portrait.

Do not route any asset to the 3D worker because Event 029 requires no custom unit, vehicle, creature, building mesh, map entity, skeletal action, sound package, or counter.

Do not create animation.

The accepted presentation uses one static decision-category picture.

## Event identity

- Event ID: `029`
- Event slug: `riches_found`
- Temporary evidence root while work is active: `docs/assets/029_riches_found/`
- Permanent spec root: `docs/specs/029_riches_found_specs/`
- Asset handoff path: `docs/plans/029_riches_found_plans/subagent_handoffs/`

The event is a dynamic state-bound mining rush and wealth-control crisis.

Baseline art must resemble period documentary photography from the late 1930s or 1940s.

High-chaos art can introduce fictional obsession and supernatural effects while keeping period workers, guards, officials, equipment, and mine architecture as the visual anchor.

Avoid modern machinery, modern streets, modern uniforms, contemporary protective gear, modern UI, cinematic color grading, readable generated text, maps as the main subject, generic war-room compositions, and fantasy treasure imagery.

## Reference inspection gate

Before creating each family, inspect the matching contact sheet and catalog under:

`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`

Required families include:

- `event_art/report/`
- `icons/decisions/`
- `icons/missions/`
- `icons/decision_categories/`
- `icons/decision_categories/pictures/`
- `icons/ideas/`
- `icons/state_modifiers/`
- `icons/achievements/`

Inspect the active vanilla or Chaos Redux sprite and GUI consumer to confirm canvas, crop, alpha, frame count, runtime path, and DDS behavior.

The decision-category picture reference family uses a 114x101 reference canvas, but the actual consumer determines final size.

Record every inspected source path and consumer in the manifest and handoff.

## Generated report images

Create separate source art for every report image.

Planning target: 210x176 after processing, unless the active consumer proves another size.

Final proposed runtime folder: `gfx/event_pictures/029_riches_found/`.

Required assets:

1. `riches_found_discovery_report`
   - Surveyors and workers around newly exposed valuable material.
   - Officials try to control access while prospectors arrive.
   - Mood is practical amazement and immediate competition.
   - No giant crystal, treasure chest, fantasy glow, or modern open-pit equipment.

2. `riches_found_rush_report`
   - Rapid mine-camp growth, improvised housing, merchants, workers, period transport, and crowded access.
   - Show opportunity, congestion, and strained order.

3. `riches_found_concession_report`
   - Foreign engineers or concession staff, local officials, guards, and workers at a controlled mine entrance or processing site.
   - Show unequal leverage through physical access and equipment.
   - Do not use a meeting table or handshake as the main scene.

4. `riches_found_raid_report`
   - Armed claimants, raiders, or guards contest a pay wagon, railhead, assay office, bridge, or shaft entrance.
   - One concrete target must be readable.
   - Avoid battlefield panorama and gore.

5. `riches_found_collapse_report`
   - Rescuers, damaged supports, dust, blocked workings, and broken period equipment after collapse.
   - Focus on rescue and physical loss.

6. `riches_found_gold_disease_report`
   - Workers and guards obsessively searching, counting, hiding, or fighting over small amounts of valuable material.
   - Use hands, posture, locked boxes, barricades, and suspicion.
   - No plague, infection, medical suit, zombie, or glowing-virus imagery.

7. `riches_found_opened_depths_report`
   - Period miners in a deep chamber with one impossible spatial, light, or accounting-linked feature.
   - The supernatural force acts through valuation, promises, and the mine.
   - No horned demon, lava cavern, copied religious altar, or generic occult temple.

8. `riches_found_gilded_sovereignty_report`
   - A functioning guarded mine enclave controls gates, payroll, transport, housing, and workers more visibly than the state.
   - Show order, wealth, and political separation without a new national flag.

9. `riches_found_bottomless_account_report`
   - Underground assay or ledger space where weighed material, official records, and observers are linked through an impossible transaction.
   - No readable generated text and no floating game interface.

For every report image, retain the ImageGen source, prompt, processed PNG, final DDS, review contact sheet, source hash, final hash, and manifest entry.

## Static decision-category picture

Create `riches_found_category_picture`.

Proposed runtime folder: `gfx/interface/decisions/029_riches_found/` after consumer verification.

Subject:

- mine entrance
- railhead or road
- pay transport
- workers
- guards
- rough offices
- growing settlement

The image must support the whole baseline category.

It must not depict Gold Disease or demons.

It must not contain fake buttons, meters, number fields, labels, generated text, or any decoration that implies a click target.

Create a static picture only.

## Decision-category icon

Create `decision_category_riches_found` for the verified category-icon canvas.

Use a strong mine entrance or mining-tool silhouette with one high-value ore specimen and an industrial shadow.

Keep the subject readable at native size.

Do not derive it from the category picture.

## Decision icons

Create separate 32x32 transparent icons with dark outline, subtle shadow, centered silhouette, and no opaque square background.

Use exact stable filenames after parent lock.

Required list:

- `decision_riches_found_survey`
- `decision_riches_found_claim_register`
- `decision_riches_found_claim_freeze`
- `decision_riches_found_claim_court`
- `decision_riches_found_camp_administration`
- `decision_riches_found_local_labor`
- `decision_riches_found_specialist_labor`
- `decision_riches_found_sanitation`
- `decision_riches_found_rail_spur`
- `decision_riches_found_port_route`
- `decision_riches_found_shaft_reinforcement`
- `decision_riches_found_processing_works`
- `decision_riches_found_housing`
- `decision_riches_found_development_fund`
- `decision_riches_found_drive_deeper`
- `decision_riches_found_dividend`
- `decision_riches_found_local_revenue`
- `decision_riches_found_central_revenue`
- `decision_riches_found_stabilization_fund`
- `decision_riches_found_audit`
- `decision_riches_found_replace_administration`
- `decision_riches_found_concession_auction`
- `decision_riches_found_exclusive_concession`
- `decision_riches_found_offtake`
- `decision_riches_found_disclosure`
- `decision_riches_found_publish_contract`
- `decision_riches_found_nationalize`
- `decision_riches_found_buyout`
- `decision_riches_found_mine_police`
- `decision_riches_found_private_guards`
- `decision_riches_found_army_cordon`
- `decision_riches_found_armed_workers`
- `decision_riches_found_pay_train`
- `decision_riches_found_truce`
- `decision_riches_found_temporary_closure`
- `decision_riches_found_quarantine`
- `decision_riches_found_workforce_replacement`
- `decision_riches_found_seal_depths`
- `decision_riches_found_repair`
- `decision_riches_found_evacuation`
- `decision_riches_found_permanent_seal`
- `decision_riches_found_religious_assistance`
- `decision_riches_found_occult_assistance`
- `decision_riches_found_scientific_assistance`
- `decision_riches_found_bargain`
- `decision_riches_found_close_account`

Do not resize focus icons, idea icons, or report art to satisfy this list.

Closely related levels of one action can share a visual only when the action is semantically identical and the parent approves the reuse.

## Mission icons

Create separate mission-specific icons for:

- `mission_riches_found_secure_rush`
- `mission_riches_found_open_railhead`
- `mission_riches_found_protect_pay_train`
- `mission_riches_found_break_claim_war`
- `mission_riches_found_restore_shaft`
- `mission_riches_found_hold_mine`
- `mission_riches_found_public_settlement`
- `mission_riches_found_audit_concession`

Show the objective and avoid a generic clock-only symbol.

## State-modifier icon family

Create separately authored coordinated icons for:

- `riches_found_state_new`
- `riches_found_state_developed`
- `riches_found_state_contested`
- `riches_found_state_closed`
- `riches_found_state_ruined`
- `riches_found_state_sealed`
- `riches_found_state_corrupted`
- `riches_found_state_gold_sick`
- `riches_found_state_opened_depths`

Use the verified state-modifier canvas.

Planning reference is 64x64.

Ordinary states use shaft, rail, tools, gates, damage, and sealing motifs.

Evolved states use captured ledgers, obsessive possession, and impossible depth motifs.

## Controller idea icons

Create separate 64x64 transparent icons for:

- `riches_found_idea_windfall_receipts`
- `riches_found_idea_managed_revenue`
- `riches_found_idea_resource_dependence`
- `riches_found_idea_captured_revenue_state`
- `riches_found_idea_gold_sick_administration`
- `riches_found_idea_infernal_accounts`
- `riches_found_idea_reformed_settlement`

Use treasury, ledger, mine, contract, guard, and state motifs.

Do not derive them from decision or focus art.

## Evolution icons

Create icons for:

- `riches_found_evolution_resource_curse`
- `riches_found_evolution_gold_disease`
- `riches_found_evolution_demons_beneath_mine`

The Resource Curse shows mine wealth capturing government or treasury.

Gold Disease shows concealed material and possession without medical imagery.

Demons Beneath the Mine shows an opened shaft responding through impossible symbols or light without a generic creature.

## Achievement icons

Create 64x64 completed art for these full IDs after the parent locks the final achievement keys:

- `029_public_fortune`
- `029_claim_jumper`
- `029_the_pay_train_runs`
- `029_all_that_glitters`
- `029_no_man_owns_the_mountain`
- `029_close_the_account`
- `029_the_last_shift`

Then create the required grey and not-eligible variants through the repository achievement workflow.

Achievement files must remain directly under `gfx/achievements/` when the verified engine convention matches the current skill.

Use the reusable not-eligible overlay from the reference workflow.

Do not place achievement files in an event subfolder when the engine expects root files.

## Required package outputs

Every asset row must return:

- source mode
- source ImageGen output or approved source file
- full prompt
- source checksum
- processed PNG
- final DDS
- final runtime path
- native dimensions
- alpha result
- contact-sheet review
- proposed sprite name
- intended consumer
- reference folder inspected
- vanilla or Chaos Redux consumer inspected
- manifest entry
- `gfx_handoff.md` entry
- status of `complete`, `needs_user_review`, `blocked`, or `canceled`

The asset subagents must not edit event, decision, mission, idea, dynamic-modifier, scripted-effect, scripted-trigger, GUI, localisation, achievement registry, docs, or spreadsheet files.

The parent owns final non-portrait `.gfx` wiring, gameplay references, documentation, catalog alignment, and live visual validation.

## Forbidden substitutions

Do not use:

- primitive local drawings as final art
- resized unrelated icons
- focus art as decision art
- idea art as decision art
- report art as category art without a separate composition
- modern photographs
- film stills
- reenactments
- generated readable text
- treasure chests
- giant fantasy crystals
- horned generic demons
- copied living religious symbols
- waving flags
- a portrait, flag, 3D model, unit counter, sound, or animation to fill an unrequested surface

A missing or rejected required asset remains blocked.

Do not create a placeholder and call the package complete.

## Temporary workspace cleanup

Keep `docs/assets/029_riches_found/` while production, review, or implementation remains active or blocked.

Before the Event 029 goal is fully complete, the parent must move durable provenance, prompts, review facts, hashes, and runtime crosswalks into permanent event or plan documentation, verify that runtime consumers point only to engine-facing folders, and delete the complete temporary event workspace.

Do not delete the skill-local reference library or another event's workspace.
