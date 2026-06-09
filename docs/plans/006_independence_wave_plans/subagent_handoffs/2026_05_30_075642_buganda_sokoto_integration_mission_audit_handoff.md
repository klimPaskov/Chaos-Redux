# Event 006 Buganda/Sokoto Integration Mission Audit Handoff

Timestamp: 2026-05-30 07:56:42 UTC

## Scope

Audited and narrowly patched the Event 006 post-formation integration missions:

- `independence_wave_integrate_buganda_lukiko_charter`
- `independence_wave_integrate_sokoto_emirate_federation`

Scoped files inspected:

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

## Findings By Severity

1. Medium: mission failure/success helper effects were player-visible as raw scripted helper output.
   - The lifecycle was mechanically correct, but the visible effect surface could show implementation helpers instead of clear failure/success consequences.
   - Patched with `custom_effect_tooltip` plus `hidden_effect` wrappers for both missions.

2. Low: mission failure condition relied on a named scripted trigger without a player-facing condition line.
   - The trigger itself was correct, but the mission UI could expose helper wording rather than a plain "becomes a subject or loses state control" condition.
   - Patched with custom trigger tooltips for both mission `available` blocks.

3. Low: non-selectable mission behavior was implicit.
   - Vanilla defaults make non-selectable missions work without the line, but the mission intent is clearer and safer with `selectable_mission = no`.
   - Patched both mission blocks.

No issue found with Event 005 routing, country deletion, state transfer, core spam, free expansion, or direct flag/visual asset handling in this slice.

## Decision Category Lifecycle Notes

- Category: `independence_wave_formation_ledger_category`.
- Buganda mission activates after `independence_wave_buganda_lukiko_charter_proclaimed`.
- Sokoto mission activates after `independence_wave_sokoto_emirate_federation_proclaimed`.
- Both missions are blocked from reappearing after either integrated or failed flags.
- Both missions remain independent from Event 005 systems and do not route `UGA` or `SOK` into Soviet Collapse helpers.

## Mission Quality Notes

Buganda mission:

- Owner/tag: `UGA`.
- Category: `independence_wave_formation_ledger_category`.
- Region/state: Uganda, state `548`.
- Requirement/loss condition: fails if `UGA` becomes a subject or no longer owns and controls state `548`.
- Duration: `@independence_wave_buganda_integration_days` / 100 days.
- Success: `independence_wave_finish_buganda_lukiko_integration`, setting `independence_wave_buganda_lukiko_charter_integrated`, integration stage, cohesion/local-polity gains, and one infrastructure level in controlled core state `548`.
- Failure: `independence_wave_discredit_buganda_lukiko_charter`, setting `independence_wave_buganda_lukiko_charter_failed` and pressure gain.
- Duplicate risk: low; integrated/failed flags gate reactivation.

Sokoto mission:

- Owner/tag: `SOK`.
- Category: `independence_wave_formation_ledger_category`.
- Region/state: Sokoto, state `902`.
- Requirement/loss condition: fails if `SOK` becomes a subject or no longer owns and controls state `902`.
- Duration: `@independence_wave_sokoto_integration_days` / 110 days.
- Success: `independence_wave_finish_sokoto_emirate_integration`, setting `independence_wave_sokoto_emirate_federation_integrated`, integration stage, cohesion/old-state-memory gains, and one infrastructure level in controlled core state `902`.
- Failure: `independence_wave_discredit_sokoto_emirate_federation`, setting `independence_wave_sokoto_emirate_federation_failed` and pressure gain.
- Duplicate risk: low; integrated/failed flags gate reactivation.

## Cost And Requirement Clarity Notes

- These are timed missions, not paid player decisions, so no political power or equipment cost is required.
- Failure requirements are now localised:
  - `independence_wave_integrate_buganda_lukiko_charter_failure_tt`
  - `independence_wave_integrate_sokoto_emirate_federation_failure_tt`
- Success/failure outcome text is now localised and hides mechanical helper effects.

## AI Validity And Route-Lock Notes

- No `ai_will_do` is required because both missions are automatic non-selectable missions.
- Route locks are valid:
  - Buganda requires `is_independence_wave_buganda_package`, `tag = UGA`, and `independence_wave_package_buganda`.
  - Sokoto requires `is_independence_wave_sokoto_package`, `tag = SOK`, and `independence_wave_package_sokoto`.
- No dead target, targeted-decision route, closed border, or Event 005 dependency was introduced.

## Localisation And Tooltip Gaps

Patched localisation keys:

- `independence_wave_integrate_buganda_lukiko_charter_failure_tt`
- `independence_wave_integrate_buganda_lukiko_charter_failure_effect_tt`
- `independence_wave_integrate_buganda_lukiko_charter_success_effect_tt`
- `independence_wave_integrate_sokoto_emirate_federation_failure_tt`
- `independence_wave_integrate_sokoto_emirate_federation_failure_effect_tt`
- `independence_wave_integrate_sokoto_emirate_federation_success_effect_tt`

No `:0` localisation keys were added.

## Cleanup And Exploit-Risk Notes

- Missions do not delete countries, transfer states, grant extra territory, or grant free cores.
- Success rewards are bounded to integration flags, small state administration improvement, and existing Event 006 variables.
- Failure flags prevent repeated pressure farming from repeated mission failures.
- No cleanup hook was needed beyond the existing integrated/failed flags because no temporary targets, cooldown flags, or timed flags are created by these two missions.

## Changed Files

- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_075642_buganda_sokoto_integration_mission_audit_handoff.md`

## Before And After Behavior

Before:

- Missions activated after proclamation and succeeded on timeout.
- Failure happened if the country became a subject or lost state ownership/control.
- UI could expose helper-trigger/effect wording and non-selectable behavior was implicit.

After:

- Missions still activate after proclamation and succeed on timeout.
- Failure condition is unchanged mechanically and now has a clear custom tooltip.
- Success and failure effects are unchanged mechanically but hidden behind concise player-facing effect text.
- Both missions explicitly declare `selectable_mission = no`.

## Validation

Run:

- Consulted offline wiki pages before Chaos file inspection: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Consulted vanilla docs/precedents: `common/decisions/_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, and vanilla mission examples in `ETH.txt` and `FRA.txt`.
- `git diff --check -- common/decisions/006_independence_wave_decisions.txt localisation/english/006_independence_wave_l_english.yml`: no whitespace errors reported for tracked diff.
- `git diff --no-index --check /dev/null common/decisions/006_independence_wave_decisions.txt`: no whitespace errors reported; command exits non-zero because the file is untracked versus `/dev/null`.
- `rg -n '<=|>=' common/decisions/006_independence_wave_decisions.txt localisation/english/006_independence_wave_l_english.yml`: no matches.
- `rg -n 'days\s*=\s*(constant:|@)|value\s*=\s*-[A-Za-z_]' common/decisions/006_independence_wave_decisions.txt localisation/english/006_independence_wave_l_english.yml`: no matches.
- `rg -n '^\s*[^#\n]+:0\s' localisation/english/006_independence_wave_l_english.yml`: no matches.
- `xxd -p -l 3 localisation/english/006_independence_wave_l_english.yml`: `efbbbf`.
- Brace balance on `common/decisions/006_independence_wave_decisions.txt`: `brace_balance=0`.

Skipped:

- No in-game validation was run.
- No commit was created per parent instruction.

## Remaining Issues And Recommended Fixes

- No remaining blocker for the two audited missions.
- There are unrelated parent edits and untracked Event 006 files in the worktree; this patch did not revert or normalize them.
- Existing indentation around nearby formation-ledger entries is uneven in places, but it is outside the mission lifecycle fix unless the parent wants a formatting-only pass.
