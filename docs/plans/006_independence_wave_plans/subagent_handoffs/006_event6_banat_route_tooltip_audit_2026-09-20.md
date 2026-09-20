# Event 006 Banat route tooltip post-patch audit

Status: implemented for the requested bounded source and static audit.

This audit made no gameplay, decision, localisation, scripted-effect, GUI, asset, spreadsheet, spec, or unrelated documentation changes. It wrote only this handoff.

## Scope

The audit covered these five decisions in `common/decisions/006_independence_wave_balkan_decisions.txt`:

- `independence_wave_axx_ratify_municipal_charter`
- `independence_wave_axx_convene_mountain_workers`
- `independence_wave_axx_restore_village_autonomy`
- `independence_wave_axx_establish_mountain_commission`
- `independence_wave_axx_accept_rail_patron_compact`

The reviewed parent patch is commit `4e547b21260a2b51727e62030dc238b605f131de`, `Clarify Event 006 Banat route outcomes`.

## Issue list sorted by severity

Critical: none found.

High: none found.

Medium: none found.

Low: the retired shared key `independence_wave_axx_route_effect_tt` remains in two historical handoff documents, not in active decision, localisation, or scripted-effect source. Those documents were pre-existing worktree or parent-patch records and were left untouched.

Validation limitation: the installed HOI4 MCP tool inventory exposes no decision-specific inspect or render route. No unrelated event, GUI, weighted, or live-game check was substituted for that missing route.

## Inspected files and references

Repository instructions and skills inspected:

- `AGENTS.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`

Decision and route source inspected:

- `common/decisions/006_independence_wave_balkan_decisions.txt`
- `localisation/english/006_independence_wave_balkan_l_english.yml`
- `common/scripted_effects/006_independence_wave_balkan_package_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/script_constants/006_independence_wave_constants_registry.txt`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_banat_route_tooltip_patch_2026-09-20.md`

Required reference material inspected:

- The offline `paradox_wiki/` pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`.
- Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`.
- Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md`.
- Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\anti_japan_infiltration.txt` and its English localisation precedent.

## Tooltip and scripted-effect match

| Decision | Route-specific key | Existing effect evidence | Result |
| --- | --- | --- | --- |
| `independence_wave_axx_ratify_municipal_charter` | `independence_wave_axx_constitutional_route_effect_tt` | `independence_wave_install_axx_constitutional_government` adds `axx_municipal_charter`, raises civic mandate by `major_gain`, raises mountain defence by `minor_gain`, and calls administrative progress with standard capacity gain. | Match. |
| `independence_wave_axx_convene_mountain_workers` | `independence_wave_axx_workers_route_effect_tt` | `independence_wave_install_axx_workers_government` adds `axx_mountain_workers_council`, raises civic mandate by `minor_gain`, raises mountain defence by `standard_gain`, and calls administrative progress with standard capacity gain. | Match. |
| `independence_wave_axx_restore_village_autonomy` | `independence_wave_axx_traditional_route_effect_tt` | `independence_wave_install_axx_traditional_government` adds `axx_village_autonomy_compact`, raises civic mandate by `major_gain`, raises mountain defence by `standard_gain`, and calls diplomatic progress with standard recognition gain. | Match. |
| `independence_wave_axx_establish_mountain_commission` | `independence_wave_axx_emergency_route_effect_tt` | `independence_wave_install_axx_emergency_government` adds `axx_mountain_defence_commission`, lowers civic mandate by `minor_loss`, raises mountain defence by `decisive_gain`, and calls security progress with standard security gain. | Match. |
| `independence_wave_axx_accept_rail_patron_compact` | `independence_wave_axx_patron_route_effect_tt` | `independence_wave_install_axx_patron_government` adds `axx_patron_rail_compact`, raises civic mandate by `standard_gain`, raises mountain defence by `minor_gain`, and calls diplomatic progress with standard recognition gain. | Match. |

The route installers are in `common/scripted_effects/006_independence_wave_balkan_package_effects.txt:159-272`. The shared administrative, security, and diplomatic progress helpers are in the same file at lines `64-89`. The wording uses the defined Banat pressure ladder where `minor_gain = 5`, `standard_gain = 10`, `major_gain = 15`, `decisive_gain = 20`, and `minor_loss = -5`.

The progress helpers also apply shared legitimacy, capacity, security, recognition, and instability deltas. The five tooltips summarize the route-distinctive outcomes and do not contradict those secondary shared effects. They do not expose raw tuning numbers or hidden route state.

## Before and after behavior

Before the parent patch, all five `remove_effect` blocks used the generic `independence_wave_axx_route_effect_tt` key, whose text only said that the selected route became active and changed Banat ledgers.

After the parent patch, each `remove_effect` uses the matching route-specific key listed above, while the installer, progress helper, cost, timer, availability, cancellation, and AI clauses remain unchanged.

The five route-specific localisation keys are each defined exactly once and have non-empty English text. The old shared key has no active decision, localisation, or scripted-effect source reference.

## Decision category lifecycle notes

All five decisions belong to `independence_wave_axx_banat_council_category`.

Each decision is visible only while the Banat package and its matching constitutional, popular-council, traditional, emergency-military, or patron-client route are active and before a Banat government is installed.

Each decision is available only when its existing custom cost is affordable, the current capital is controlled by the country, and no other Banat package project is active.

The administrative routes use the existing short 75-day timer, the traditional and patron routes use the existing long 180-day timer, and the emergency route uses the existing standard 120-day timer.

Completion installs the route government, locks the shared government route, removes the prior route ideas, adds the selected route idea, and applies the existing progress helper.

Cancellation remains gated by package validity, matching route validity, and current-capital control. No cancellation clause changed in the parent patch.

The active-project trigger lists all five decision IDs, so these route projects cannot run in parallel with another Banat project.

## Cognitive-load notes

The five scoped actions form a route-choice family rather than five simultaneous generic actions. The route predicates resolve through the shared government-route variable and matching route flags, and the `NOT = { has_independence_wave_axx_route_government = yes }` guard removes the family after route installation.

No scoped decision is a mission, and the patch adds no active mission or new visible action.

The tooltips expose only the material route values that matter for the choice: civic mandate, mountain-defence readiness, administrative capacity, recognition, or security. They use short sentences and do not expose raw variable dumps, threshold math, or implementation history.

The category contains an adjacent Banat founding mission, but that mission is outside the requested five-decision scope and was not treated as part of this tooltip audit.

## Mission quality notes

Mission quality is not applicable to the five scoped IDs because all five are ordinary timed decisions without `days_mission_timeout`, `activation`, `selectable_mission`, or `timeout_effect` blocks.

No owner, category, region, requirement, duration, success, failure, or duplicate-mission finding applies to these five decision IDs.

## Cost and requirement clarity

The parent patch did not change any cost or requirement clause.

The two administrative-route decisions use the existing administration-light palette of three spendable types: command power, manpower, and civilian-factory commitment. The two diplomatic-route decisions use the existing diplomatic-standard palette of command power and either convoys or trains. The emergency decision uses the existing security-major palette of four spendable types: manpower, army experience, infantry equipment, and support equipment.

The cost-count audit is within the four-type limit for every scoped decision.

The existing cost localisation uses texticons for every displayed spendable value, including `£command_power`, `£manpower_texticon`, `£civ_factory`, `£convoy_texticon`, `£GFX_train_texticon`, `£army_experience`, `£infantry_equipment_text_icon`, and `£support_equipment_text_icon`. No literal resource-name cost string was introduced by the parent patch.

Non-consumed route, package, capital-control, and active-project checks remain requirements and are not mixed into the cost strings.

## AI validity and route-lock notes

The existing AI weights remain `high` for the constitutional and workers decisions, `standard` for the traditional and patron decisions, and `urgent` for the emergency decision with the existing war multiplier.

The AI clauses contain no target country or state scope. Their validity is constrained by the same route, package, capital-control, and active-project checks used for the human action.

`independence_wave_select_government_route` records the selected route, sets the route lock, applies the shared route politics, and refreshes country state. The installer-specific government flags are then recognized by `has_independence_wave_axx_route_government`.

I dispatched `chaosx_ai_probability_auditor` for the required decision-weight route, but the user explicitly instructed this audit to conclude without waiting for additional MCP work. No probability-auditor result is therefore claimed here. The source diff still provides direct evidence that no AI-weight or probability-bearing clause changed.

## Localisation and tooltip gaps

No route-specific key is missing, duplicated, empty, or attached to the wrong decision.

The five route-specific strings name the installed route authority and correctly describe the direction and relative strength of the route-specific ledger or progression outcome.

The shared secondary progress deltas are summarized rather than enumerated. Expanding these short route tooltips into full effect lists is not recommended for this bounded patch because it would increase text density without correcting a mismatch.

## Cleanup and exploit-risk notes

The patch introduced no new payment, reward, timer, visibility, cancellation, or cleanup path.

The existing completion path removes the old route ideas, adds exactly one route idea, locks the route, and applies one existing progress helper. The active-project guard prevents concurrent project selection.

The existing cancellation path has no separate `cancel_effect` on these five decisions. That behavior predates the tooltip patch and was not changed. This audit found no new exploit or duplicate route path introduced by the parent patch.

## Meaningful validation and limits

- Reviewed `git show 4e547b21260a2b51727e62030dc238b605f131de` and confirmed that the parent commit changes only five tooltip tokens in the decision file and replaces one localisation key with five route-specific definitions.
- Confirmed that the scoped worktree files have no uncommitted changes relative to `HEAD`.
- Checked each decision ID against its expected tooltip key and confirmed one non-empty localisation definition per key.
- Confirmed that the old shared key is absent from active decision, localisation, and scripted-effect source.
- Matched each tooltip sentence to the existing installer, ledger delta, and administrative, diplomatic, or security progress helper.
- Checked the existing cost trigger, payment effect, cost localisation, route lock, active-project, cancellation, and AI references without modifying them.

Skipped meaningful validation: no decision-specific `hoi4.gui_inspect` or `hoi4.gui_render` route is exposed, so no decision production render exists for this text-only patch. The probability-auditor result was not awaited because the user explicitly requested immediate conclusion. No live game was launched.

## Recommendation

No further source edits are recommended for this bounded post-patch audit.

The parent patch is source-consistent and the five route-specific tooltip keys are correctly wired. Any future redesign of secondary progress disclosure or cancellation failure handling should be reviewed as a separate gameplay decision, not folded into this tooltip-only change.
