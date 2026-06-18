# 2026-06-18 Event 012 Africa Dossier Resistance Audit

## Scope

Audit target: Authority Atlas historical dossier resistance-watch and observer/direct settlement-fork surface.

Inspected files:
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/prompts/012_africa_decision_mission_prompt.md`
- `docs/plans/012_africa_plans/2026-06-16_foundation_gap_improvement_addendum.md`
- `common/decisions/012_africa_decisions.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/script_constants/012_africa_constants.txt`
- `common/ai_strategy/012_africa.txt`
- `events/012_african_union.txt`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `localisation/english/012_african_union_l_english.yml`

References consulted before audit: `AGENTS.md`, `.agents/skills/hoi4-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, required offline Paradox wiki core pages including Decision Modding, and vanilla decision/effect/trigger documentation in `~/projects/Hearts of Iron IV/`.

## Changed Files

- Added this read-only audit handoff: `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_dossier_resistance_audit.md`

No gameplay or localisation files were edited by this audit. The Event 012 gameplay/localisation files were already changing in the parent working tree during review; findings below reference the current observed state at audit time.

## Findings By Severity

### High: later dossier settlements can bypass the resistance-watch lifecycle

`can_africa_settle_selected_dossier` only checks local office, guard, selected seat control, and unsettled status (`common/scripted_triggers/012_africa_triggers.txt:934`). It does not block settlement while `africa_dossier_resistance_watch_active` is set. Both settlement decisions then call the selected-dossier settlement effects and immediately advance to the next unopened dossier (`common/decisions/012_africa_decisions.txt:1779`, `common/decisions/012_africa_decisions.txt:1822`).

The watch start helpers explicitly no-op when a watch or resistance dossier variable already exists (`common/scripted_effects/012_africa_effects.txt:5783`, `common/scripted_effects/012_africa_effects.txt:5807`). Result: a player or AI can settle another dossier while the first local watch is active, advance selection, and avoid creating a resistance watch for the later settlement. That undermines the intended observer/direct fork risk, creates uneven failure exposure, and lets high-throughput settlements skip the local report consequences.

Recommended fix: add an explicit active-watch blocker to `can_africa_settle_selected_dossier` or to both settlement decision `available` blocks, with a tooltip such as "Resolve the active local resistance watch first." If parallel watches are desired later, queue them deliberately instead of relying on the current single-context variable.

### Medium: watch duration has two tuning sources with different values

The resistance mission uses file-scoped `@africa_dossier_resistance_watch_days = 150` (`common/decisions/012_africa_decisions.txt:16`, mission use at `common/decisions/012_africa_decisions.txt:2092`). The script constant table also defines `constant:africa_decision_days.dossier_resistance_watch = 85` (`common/script_constants/012_africa_constants.txt:479`), but the mission does not use it.

This leaves the dossier watch duration split between two places and with conflicting values. If the mission field cannot parse script constants, keep the file-scoped constant but mirror the script constant value or remove the unused script constant to avoid stale balance assumptions.

### Medium: intervention decisions are mode-aware, but not profile-aware in cost or objective

`africa_mediate_dossier_resistance_watch` and `africa_enforce_dossier_resistance_watch` now use concrete equipment, manpower, PP, and CP costs (`common/decisions/012_africa_decisions.txt:1980`, `common/decisions/012_africa_decisions.txt:2034`). Their effects are profile-aware through `is_africa_archive_resistance_profile_*` helpers and profile-specific value movement.

The cost/objective side is still flat by mode: every observer mediation uses the same support equipment/manpower, and every direct enforcement uses the same infantry/support/manpower/CP. The prompt asked for profile-aware intervention decisions. At minimum, the most obvious profiles should add objective flavor: convoy requirements for river/coast/Indian Ocean dossiers, infantry or command pressure for Maghreb/Southern Stone, motorized or XP for Sahel routes, and trust/cohesion gates for Western Crowns/Great Lakes.

Recommended fix: keep the two decision IDs if scope must stay narrow, but add profile-specific custom trigger branches and tooltips inside their cost helpers or split profile cost helpers under existing scripted triggers/effects.

### Medium: mediation/enforcement record state is not fully reset

The new record effects set country-level `africa_dossier_resistance_mediated`, `africa_dossier_resistance_enforced`, and increment `africa_dossier_resistance_intervention_count` (`common/scripted_effects/012_africa_effects.txt:5968`, `common/scripted_effects/012_africa_effects.txt:5984`). The Authority Atlas progress reset clears per-dossier watch/calm/failed flags and the active context, but the inspected reset path does not clear the per-dossier mediated/enforced flags, the country-level mediated/enforced flags, or the intervention count (`common/scripted_effects/012_africa_effects.txt:4804`).

Current visible localisation does not yet depend heavily on these values, so this is not immediately player-breaking. It becomes a stale-state risk as soon as GUI cards, reports, achievements, or completion audits read these flags/counts.

Recommended fix: extend `africa_clear_authority_atlas_progress_flags` to clear `africa_dossier_[DOSSIER_ID]_resistance_mediated`, `africa_dossier_[DOSSIER_ID]_resistance_enforced`, country-level mediated/enforced flags, and `africa_dossier_resistance_intervention_count`.

### Medium: Congress GUI warning card displays the wrong resistance case

`africa_continental_congress_gui_warning_status_card` reports resistance status but labels the case with `[GetAfricaSelectedHighChaosPackageName]` (`localisation/english/012_african_union_l_english.yml:1452`). That is a Bestiary/high-chaos package resolver, not the archive resistance dossier resolver.

Recommended fix: use `[GetAfricaArchiveResistanceDossierName]` for the active resistance case, or add a scripted localisation that falls back cleanly when no watch context exists.

### Low: intervention start and outcome tooltips are present, but the local report does not expose intervention method

The success/failure events now include profile resolution text through `[GetAfricaArchiveResistanceProfileResolution]` (`localisation/english/012_african_union_l_english.yml:90`, `localisation/english/012_african_union_l_english.yml:93`). That is a clear improvement for local report consequences.

The reports still do not distinguish whether the player used mediation/enforcement or let the baseline watch resolve. Since the mechanics now record `africa_dossier_resistance_mediated` and `africa_dossier_resistance_enforced`, the report can show a method-aware line without adding new events.

Recommended fix: add a small scripted localisation such as `GetAfricaArchiveResistanceInterventionMethodResolution` and append it to `chaosx.nr12.49.d`/`.50.d`.

### Low: cost triggers are duplicated inside availability

`can_africa_mediate_dossier_resistance_watch` and `can_africa_enforce_dossier_resistance_watch` include the resource gates, and those same gates are repeated in `custom_cost_trigger` (`common/scripted_triggers/012_africa_triggers.txt:661`, `common/scripted_triggers/012_africa_triggers.txt:672`; `common/decisions/012_africa_decisions.txt:1990`, `common/decisions/012_africa_decisions.txt:2044`).

This is not invalid, but it makes the requirement tooltip and cost tooltip overlap and increases the chance that a future cost change updates one side but not the other.

Recommended fix: split state eligibility from resource affordability. Keep active-watch/mode/seat-control/intervention-active checks in `available`; keep PP/equipment/manpower/CP in `custom_cost_trigger` or a dedicated cost trigger called only from the custom cost.

## Decision Category Lifecycle Notes

Owner: runtime Africa unifier using `africa_authority_atlas_category`.

The category lifecycle has a sensible path for the narrow surface: open Atlas, survey dossier, create local office, raise guard, settle observer/direct, start local watch, optionally intervene, then success/failure report clears context. The direct/observer route-locks are clear: mediation requires observer watch, enforcement requires direct archive watch.

Lifecycle gap: the category permits a new settlement while a previous settlement watch is active. Because the watch context is single-instance, this creates an untracked settlement rather than a second mission. This is the main exploit and cleanup risk for this surface.

Settlement fork breadth remains narrower than the 2026-06-16 addendum. Current implementation has observer and direct archive forks. Protected Seat, Regional Authority Office, and Reject Counterfeit Claim are still broader planned work, not present in the inspected decision surface.

## Mission Quality Notes

Mission: `africa_dossier_resistance_watch_mission`

- Owner: Africa runtime unifier.
- Category: `africa_authority_atlas_category`.
- Region: stored old-seat state in `africa_archive_resistance_seat_state`.
- Requirement: keep the resistance seat controlled by ROOT or an eligible faction/controller and meet observer trust/cohesion or direct authority/debt gates.
- Duration: current mission uses 150 days through `@africa_dossier_resistance_watch_days`, while script constants list 85 days.
- Success: `africa_complete_dossier_resistance_watch` records calm, route-specific value gains/relief, clamps values, fires `chaosx.nr12.49`.
- Failure: `africa_fail_dossier_resistance_watch` records failed, applies route-specific and general pressure, clamps values, fires `chaosx.nr12.50`.
- Duplicate risk: high if settlement remains available during an active watch, because later settlements skip watch creation instead of becoming duplicate tracked missions.

Intervention decisions: `africa_mediate_dossier_resistance_watch`, `africa_enforce_dossier_resistance_watch`

- Owner/category/region: same active watch context.
- Requirement: active watch, correct mode, stored seat controlled, no active intervention, resource gates.
- Duration: 35-day timed decisions through `constant:africa_decision_days.dossier_resistance_intervention`.
- Success/failure: intervention decision `remove_effect` resolves the watch if the seat remains controlled and fails it if intervention is active but the watch is no longer valid.
- Duplicate risk: low for the same watch due `africa_dossier_resistance_intervention_active`; higher at settlement level because new settlements can skip watch setup.

## Cost And Requirement Clarity Notes

Good: intervention costs are no longer flat PP-only exchanges. Mediation spends PP, support equipment, and manpower; enforcement spends PP, infantry equipment, support equipment, manpower, and command power.

Remaining clarity gaps:
- Profile effects are visible in the event report, but profile-specific costs/objectives are not.
- The cost localisation hardcodes visible numbers that currently match constants. If constants change, localisation must be updated manually unless a dynamic cost string is added.
- Requirement tooltip text says "enough Congress staff" or "enough escorts" while the hard requirement is exact equipment/manpower/CP. This is acceptable flavor, but the cost trigger should remain the authoritative affordability display.

## AI Validity And Route-Lock Notes

No invalid country-target or dead-target issue was found in this surface. The decisions are non-targeted and operate on stored dossier/state variables.

AI equivalents are present:
- Observer/direct watch production strategies in `common/ai_strategy/012_africa.txt`.
- Route/profile-sensitive `ai_will_do` blocks on mediation and enforcement.

Route locks are mostly correct:
- Mediation requires `africa_dossier_resistance_watch_observer`.
- Enforcement requires `africa_dossier_resistance_watch_direct_archive`.
- Enforcement is discouraged for federal/sovereign routes and preferred for general staff/direct archive routes.

AI shares the same settlement bypass risk as the player because the settlement trigger does not block active watches.

## Localisation And Tooltip Gaps

Present and aligned:
- New intervention decision names/descriptions.
- Start/effect/cost tooltips for mediation and enforcement.
- Resistance mission title/description using active dossier/seat localisation.
- Success/failure events with profile resolution text.

Gaps:
- GUI warning card uses high-chaos package name for resistance case.
- Reports do not mention whether the case was mediated, enforced, or naturally resolved.
- Active watch status in scripted localisation reports only active/calm/failed/none, not the dossier and seat unless the player is looking at the mission title or event.

## Cleanup And Exploit-Risk Notes

Good cleanup:
- `africa_complete_dossier_resistance_watch`, `africa_fail_dossier_resistance_watch`, and `africa_clear_dossier_resistance_watch_context` clear active intervention flags.
- Success/failure events preserve context long enough for event localisation, then clear it on option click.

Remaining risks:
- Settlement bypass is the main exploit: settle additional dossiers during an active watch and no new watch is registered.
- Intervention count and mediated/enforced flags can become stale across Authority Atlas reset.
- If the intervention decision cost changes in constants, localisation can silently drift because visible numbers are static.

## Concrete Recommended Fixes

1. `common/scripted_triggers/012_africa_triggers.txt`: add `NOT = { has_country_flag = africa_dossier_resistance_watch_active }` to `can_africa_settle_selected_dossier`, or add equivalent blocked-tooltip logic in both `africa_settle_selected_dossier_observer` and `africa_settle_selected_dossier_direct_archive`.
2. `localisation/english/012_african_union_l_english.yml`: add/update a settlement blocked tooltip explaining that active local resistance must be resolved before opening another settlement.
3. `common/scripted_effects/012_africa_effects.txt`: extend `africa_clear_authority_atlas_progress_flags` to clear per-dossier mediated/enforced flags, country-level mediated/enforced flags, and `africa_dossier_resistance_intervention_count`.
4. `common/decisions/012_africa_decisions.txt` and `common/script_constants/012_africa_constants.txt`: reconcile `@africa_dossier_resistance_watch_days = 150` with `constant:africa_decision_days.dossier_resistance_watch = 85`.
5. `localisation/english/012_african_union_l_english.yml`: change `africa_continental_congress_gui_warning_status_card` resistance case from `[GetAfricaSelectedHighChaosPackageName]` to `[GetAfricaArchiveResistanceDossierName]` or a dedicated fallback resolver.
6. `common/scripted_triggers/012_africa_triggers.txt` and `common/scripted_effects/012_africa_effects.txt`: split intervention eligibility from resource affordability to avoid duplicated cost gates and easier future profile-specific costs.
7. `common/scripted_localisation/012_africa_scripted_localisation.txt` and `localisation/english/012_african_union_l_english.yml`: add an intervention-method report resolver for mediated/enforced/natural outcomes.

## Validation Performed

Read-only validation only. I used targeted `rg`/`nl` scans over the explicit files to verify:
- Current intervention decision IDs, costs, tooltips, AI weights, and effects exist.
- Resistance watch context setup/clear/success/failure paths exist.
- Settlement availability does not check active resistance watch state.
- Success/failure report events preserve and then clear context.
- Localisation keys for the new intervention decisions are present.

No gameplay files were patched and no in-game validation was run.

## Residual Risk

The audit occurred while parent changes were actively modifying Event 012 files. If the parent patches the settlement blocker, duration mismatch, or GUI case resolver after this handoff, those findings should be rechecked against the final diff before acting on them.
