# Event 021 Random Civil War Localisation Audit

> **Evidence status.** The source patch and bounded localisation checks in this handoff remain historical audit provenance. Its older MCP artifact and workspace-wide diagnostic statements are superseded by the current focused Event 021 evidence in `docs/events/021_random_civil_war/acceptance_evidence.md`; its unresolved presentation follow-ups remain queued unless newer source evidence closes them.

## Outcome

Event 021 had mechanically significant localisation gaps and widespread implementation-facing prose. I applied a narrow patch to `localisation/english/021_random_civil_war_l_english.yml` only. The patch restores the missing idea and achievement localisation contract, converts all seven implemented decision costs to compact value-plus-texticon strings, removes the visible hidden-pressure reference, adds one safe dynamic capital name, and rewrites Event Details, evolution, Event 006 boundary, scenario, achievement, and popup text as current-world prose.

The audit does not establish complete player-facing presentation. Exact cluster skip reasons are not implemented, the event-list `N/A` strings are not wired to a consumer, several required dynamic targets are absent, and the standard decision category cannot be rendered by the installed scripted-GUI MCP route.

## Sources inspected

- `events/021_random_civil_war.txt`
- `common/decisions/021_random_civil_war_decisions.txt`
- `common/decisions/categories/021_random_civil_war_categories.txt`
- `common/scripted_localisation/021_random_civil_war_localisation.txt`
- Event 021 constants, parent effects, triggers, ideas, achievements, GFX, shared Event Log and Event Details selectors, scenario selectors, cluster registration, visible/debug event-name mappings, authoritative CSV exports, and all Event 021 presentation, localisation, decision, achievement, and auditor prompts named in the task
- Event 021 static category, report, and news DDS images after read-only PNG conversion in a temporary directory

## Changed files

- `localisation/english/021_random_civil_war_l_english.yml`
- `docs/plans/021_random_civil_war_plans/subagent_handoffs/localisation_auditor.md`

No unrelated file was edited.

## Missing key list

### Fixed

The following 25 required keys were missing and are now defined:

- Idea database keys: `event021_fractured_command`, `event021_fractured_command_desc`, `event021_war_torn_administration`, `event021_war_torn_administration_desc`, `event021_unsettled_settlement`, `event021_unsettled_settlement_desc`
- Achievement eligibility and happened tooltips: `021_random_civil_war_achievement_eligible_tooltip`, `021_random_civil_war_hold_the_center_tooltip`, `021_random_civil_war_no_state_left_behind_tooltip`, `021_random_civil_war_a_flag_of_our_own_tooltip`, `021_random_civil_war_war_within_a_war_tooltip`, `021_random_civil_war_the_terms_hold_tooltip`, `021_random_civil_war_fractals_of_sovereignty_tooltip`
- Achievement UI names and descriptions: `_NAME` and `_DESC` for all six `021_random_civil_war_*` achievement IDs

### Remaining

No missing localisation key remains in the bounded event, decision, mission, idea, achievement, scripted-localisation, scenario, or Event Log references checked. The five `event021_Get*` identifiers are defined-text function names, not missing YAML keys.

## Duplicate key list

No duplicate Event 021 key was found in the English localisation database, and no duplicate key exists inside the Event 021 English file.

## Scripted localisation issues

- `event021_GetAuthorityBand`, `event021_GetCrisisPhase`, and `event021_GetCrisisSummary` resolve to defined fallback keys. Their referenced keys are present.
- `event021_GetScenarioTypeName` and `event021_GetScenarioIntensityName` are not referenced outside their own scripted-localisation file. They are currently dead presentation helpers, although the shared scenario selectors independently resolve all Event 021 scenario strings.
- `event021_GetAuthorityBand` falls back to `Collapse`. If the category can appear before `random_civil_war_state_authority` is initialized, it can present an invalid crisis state rather than `N/A`. Source behavior was not changed because initialization guarantees were not proven.
- The three evolution records publish event ID, type, stage, tier, actor, and `events_log_evolution_has_actor` before using the shared recorder. Event Details previews expose all three stages and their title/body selectors.
- `event021_target_na`, `chaosx.nr21.1.no_target`, and `chaosx.nr21.1.skip` have no source reference outside localisation. The required no-target and skipped-result presentation therefore remains unwired.

## Dynamic text opportunities

- The category has no dynamic selected or priority front name despite the specification requiring one for multi-front crises.
- The rail mission does not name a state, rail junction, or route. Its requirement only checks whether any owned controlled state has sufficient infrastructure.
- Event opening and follow-up text has no dynamic claimant, front, region, depot, sponsor, or settlement name. I added `[ROOT.Capital.GetName]` only where the event scope is safely the recipient country.
- Event Details payload text has no actor, country, capital, or front token even though the shared history row stores an actor.
- Scenario impact values are prose approximations rather than values derived from the scenario-share constants.
- The category prints the authority variable directly. A scripted display helper would allow a safe `N/A` state when authority has not been initialized.

## Cross-surface mismatches

- `docs/spreadsheets/chaos_redux_events_catalog.csv` still contains only the stale row `Random civil war` with the old one-sentence description and `To Be Reworked`. It contains no Event 021 evolution, Wars-cluster, or `SCN-018` Fracture Cascade records. The XLSX was not edited because this task authorized only narrow Event 021 localisation fixes.
- The shared Wars cluster description is generic and acceptable, but Event 021 records only skipped counts. No exact target-reservation or collision skip-reason strings were found for the required cluster presentation.
- The decision file implements two 30-day missions. The Event 021 decision specification calls for roughly 120 to 180 days for Hold the Capital and named rail objectives. This is a gameplay/design mismatch, not a localisation-only correction.
- Every decision availability gate uses strict `>` against the displayed positive cost. A country holding exactly the displayed amount is blocked even though the cost string says that amount is sufficient.
- The normal active-crisis surface can expose relief-corridor action text to any managing crisis country, not only an exposed neighbor. This weakens the required separation between government and neighbor phases.
- Achievement registry IDs and the newly added `_NAME`, `_DESC`, and tooltip keys now agree. The older `chaosx.achievements.*` mirror strings were retained and aligned because another presentation surface may consume them.
- Event 006 boundary language is now in-world. Visible strings no longer say `Event 006`, `country package`, `normal human country`, or `same-tag takeover`.

## File encoding concerns

- `localisation/english/021_random_civil_war_l_english.yml` remains UTF-8 with BOM (`EF BB BF`).
- No `:0` key was found.
- Every non-empty localisation line matches the repository's one-line key/value form.
- No Event 021 GFX texture reference points to a missing file, and no sprite name is duplicated in `interface/021_random_civil_war.gfx`.

## GFX and presentation inspection

- `decision_category_picture_021_civil_war.dds` is `114x101`, has no fake button, meter, label, or map control, and matches the specified static category-picture role.
- `report_event_021_random_civil_war_opening.dds` is `210x176`.
- Both news images are `397x153`.
- All three event/news images communicate rail, military, and civilian disruption without generated text or a literal world map.
- Direct DDS viewing was unsupported, so the images were converted read-only into `%TEMP%\event021_localisation_audit` for visual inspection. Runtime DDS files were not changed.

## Prose-quality issues and repairs

### Vagueness

Before, Event Details described a `recorded Event 021 fracture`, a `protected remnant`, and a planned `force package`. After, it describes rival authorities contesting territory, capitals, supplies, loyalty, and peace terms. The opening popup now names `[ROOT.Capital.GetName]`.

Remaining vagueness: the rail mission still says `connected high-capacity route` because no named route target exists in script, and several popup events cannot name a claimant or region because no safe localisation target is exposed.

### Bloat

Scenario and Event Log text no longer carries qualifiers such as `bounded`, `complete human`, `normal human`, and `terminal world-end`. Scenario summaries now state who is affected and what kind of conflict appears.

### Obvious explanation

Decision costs no longer say `Requires command capacity, infantry equipment, and trains`. They show exact values with matching texticons. Tooltips retain only the public action and consequence.

### Repetition

Evolution records no longer repeat `Event 021` or describe entering a review system. Each record states the new in-world development: additional fronts, cross-border pressure, or recurring national fractures.

### Overcomplication

The Event 006 independence popup and achievement text no longer describe packages, origins, nested generations, or implementation classifiers. They describe an established independence movement, its homeland, its former host, and the obligations required for recognition and survival.

### Style-rule repair

- Removed the visible em dash in the category description.
- Removed the sentence semicolon in the loyalty-review tooltip.
- Removed the hidden `Fracture Pressure` name from decision text.
- Removed update/implementation history and technical system labels from player-facing prose.
- Rewrote the multi-front `has not disappeared, but` contrast construction.
- Preserved displaced civilians as people needing shelter and administration, separate from weapons traffic and armed cadres.

## Changed keys

Existing keys changed:

- Category and summary: `event021_civil_war_crisis_category_desc`, `event021_summary_neighbor`
- Decisions and costs: `event021_secure_arsenals_tt`, `event021_secure_arsenals_cost_text`, `event021_defend_capital_tt`, `event021_defend_capital_cost_text`, `event021_review_loyalty_tt`, `event021_review_loyalty_cost_text`, `event021_seize_depot_cost_text`, `event021_open_relief_corridor_cost_text`, `event021_offer_emergency_settlement_desc`, `event021_offer_emergency_settlement_cost_text`, `event021_reconstruct_administration_cost_text`
- Mission: `event021_hold_the_capital_mission_desc`
- Evolution: `event021_evolution_i_body`, `event021_evolution_iii_body`, `event021_evolution_i_log`, `event021_evolution_ii_log`, `event021_evolution_iii_log`
- Event Log and Details: `event021_event_log_evolution_summary`, `event021_event_log_detail`, `event021_event_log_detail_opening`, `event021_event_log_detail_multi_front`, `event021_event_log_detail_exposure`, `event021_event_log_detail_settlement`, `event021_event_log_detail_reconstruction`, `event021_event_log_detail_failed_opening`
- Popups and news: `chaosx.nr21.2.d`, `chaosx.nr21.3.d`, `chaosx.nr21.6.d`, `chaosx.nr21.8.d`, `chaosx.nr21.10.d`, `news_event_021_global_fracture.d`
- Scenario: all four `chaosx.scenarios.random_civil_war.desc.*` keys, all four `chaosx.scenarios.random_civil_war.impact.*` keys, `chaosx.scenarios.random_civil_war.confirmation`, and the three Event 021 scenario launch-status keys
- Achievement mirrors: all six `chaosx.achievements.021_random_civil_war_*.desc` keys

New keys are the 25 entries listed under Missing key list.

## Dynamic localisation added or fixed

- Added `[ROOT.Capital.GetName]` to `chaosx.nr21.2.d` and `event021_hold_the_capital_mission_desc`.
- Replaced static literal-resource decision costs with direct centralized constant values and matching texticons for command power, political power, army experience, infantry equipment, trains, motorized equipment, convoys, and manpower.
- Preserved all existing dynamic tokens, scripted-localisation calls, colour codes, constants, conditions, and formatting codes.

## Behavior and display before and after

- Before: Event 021 ideas and all achievement registry tooltips/names/descriptions could display raw keys. After: the required database keys are present.
- Before: decision cost rows hid exact amounts behind prose. After: each row shows two to four exact, icon-backed costs sourced from Event 021 constants.
- Before: a tooltip revealed hidden Fracture Pressure. After: it describes the visible State Authority consequence.
- Before: Event Logs, scenarios, and Event 006 boundary text described packages, systems, bounded processing, and event numbers. After: they describe governments, commands, independence movements, borders, relief, and settlements.

## Sourced-quotation preservation

No attributed or sourced quotation appears on any inspected Event 021 surface. No quotation was altered.

## MCP evidence and exact limitation

- Event trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e829c728b23e87ba72eddec54178d4de789cb660fcf4c04f0d72a588c87a427/a5c9fffefe3951d59f83fd5644f8d2950b6c1fa1a6ecf7489c6bf4f2c7d461b4/event-trace-eaac06f8f701.json`
- Event option render data: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/60932954749a138960b62c78391a67ddc8af072739f0ca2a13e3b81984638326/5c7550a3f05761baa8ff984ad648ac316bdd46fce008adadbdb03038b7a6e3a5/event-options-eaac06f8f701.json`
- Event option PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77f68966e0eba270ef9cfe185d67bec74d131944a4cf3eb1f749ed596468deac/e4645bea07d8e292d7cfdfe5909b65ac7c599c419f94feeca5355e4414e42f19/event-options-eaac06f8f701.png`
- Event lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a12256c88098350f82762fdbb345863b85cf19a9c9ca7ebcb03338fd9b24ae21/5681a8c08409d0bb8d70c60be08b5cdf834222d7bb1061ba20ce4c5932e883c1/event-lint-eaac06f8f701.json`
- GUI inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8a23699fb8d9666c196d8eb45976b0695285f1d203bf40f9976bccecac8a83d/ad5489d3eb6afc5a55bfacb4b580035d654ba82b3c38412e7d5d14a9269d0f78/gui-inspect.8e1cb219910b0741.json`

The GUI inspector reported `inspectedElementCount: 0`, `missing: 1`, and `approximated: 1` for `event021_civil_war_crisis_category`. This is a vanilla decision-category database surface, not a scripted-GUI window. The render route returned a 661-byte SVG with no usable decision-category layout. Therefore production-render evidence for category text wrapping, cost overflow, and normal decision-list layout is unavailable. Source and asset inspection are recorded but are not treated as equivalent visual proof.

The event trace and lint returned partial repository-wide analyses with 18 blocking diagnostics and thousands of unresolved nodes in the full workspace. No Event 021-specific localisation defect was identified inline, but the global diagnostic volume prevents treating those results as a clean Event 021 lint pass.

## Meaningful validation run

- Verified all bounded event, decision, mission, idea, achievement, scripted-localisation, scenario, and Event Log references against the English localisation database after the patch.
- Verified every cost texticon token against existing Chaos Redux or installed vanilla localisation usage and kept each row within the four-entry limit.
- Verified no duplicate Event 021 English key, no `:0`, UTF-8 BOM retention, and one-line localisation syntax.
- Verified every Event 021 GFX texture path and sprite name in `interface/021_random_civil_war.gfx`.
- Visually inspected the static category picture and all three event/news pictures at their native dimensions.
- Re-ran the read-only event lint after localisation changes and retained the artifact URI above.

## Skipped meaningful validation

- No in-game rendering or playtest was performed. Repository rules reserve live consumer validation for the user.
- Standard decision-category overflow and wrapping could not be validated because the installed GUI MCP only resolved scripted-GUI windows and returned no Event 021 category elements.
- The XLSX workbook was not opened or edited because the requested patch boundary allowed only narrow Event 021 localisation/encoding fixes. The read-only CSV mismatch is recorded above.
- No probability pass was run because no AI weight, chance, MTTH, or gameplay tuning value was changed.

## Recommended follow-up fixes

- `common/decisions/021_random_civil_war_decisions.txt`: make availability agree with displayed costs when the country holds exactly the required amount, add named rail/capital objective tooltips, and review the 30-day mission durations.
- `common/scripted_localisation/021_random_civil_war_localisation.txt`: add selected-front, named-route, and safe authority-`N/A` display helpers, or remove the two unused scenario helpers.
- `common/scripted_effects/021_random_civil_war_parent_effects.txt` and `common/scripted_effects/chaosx_event_cluster_effects.txt`: wire exact no-target and cluster skip-reason payloads to visible localisation rather than recording only skipped counts.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`: expose safe stored actor/front/capital context in Event Details where the row context supports it.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`: after final implementation facts are accepted, align Event 021, its three evolutions, the Wars cluster membership, and `SCN-018`, then regenerate all CSV exports.

## Unresolved wording decisions and residual risks

- A named rail route cannot be written accurately until script exposes the selected route or state targets.
- A claimant name cannot be added safely to popups or Event Details until the owning event target and its lifetime are confirmed for each event and log context.
- `Countries outside ordinary human politics` is the least technical safe scenario wording found for the actual-nonhuman exclusion. The parent may prefer a project-wide established phrase if one exists.
- The eligibility tooltip says `normal campaign`, `force-trigger`, and `scenario assistance` because the achievement UI must communicate disqualification. This is mechanics-facing achievement text, not narrative prose.
- No central improvement plan was written. The unresolved items are direct implementation follow-ups inside the existing Event 021 specification, not a new design gap.

## Completion and simplifications

The requested localisation audit and narrow localisation patch are complete. Event 021 presentation as a whole is not proven complete because exact skip-reason wiring, dynamic front/route text, workbook alignment, and production rendering of the standard decision category remain unresolved. No fallback presentation or unrelated cleanup was added.
