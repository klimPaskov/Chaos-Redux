# Event 006 Dossier Board Host Tools Audit Patch Handoff

## Scope

Bounded decision and mission audit for the Event 006 Independence Wave Dossier Board host-tools tranche. Scope was limited to the host release ledger, host-targeted Dossier Board decisions, their shared scripted triggers/effects, constants, localisation, and existing docs/handoff notes.

Forbidden paths were not edited by this audit: no flag image files, flag graphics, `gfx/flags`, `common/countries`, `history/countries`, or Event 005 files were changed by this patch. The worktree already contained Event 005 modifications before this audit began; they remain outside this patch.

## References Used

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_collection_operator.md`, `script_collection_input.md`, `script_concept_documentation.md`.
- Vanilla precedents for targeted decisions, `target_array`, custom costs, and AI weights in `~/projects/Hearts of Iron IV/common/decisions/` and `common/decisions/categories/`.

## Issue List

1. Medium: `can_independence_wave_host_target_release` trusted decision `target_array` filtering but did not prove that `FROM` was still in `ROOT`'s `independence_wave_host_released_countries` ledger. If the shared trigger or effect path is reused later, a host could theoretically pass a non-ledger release target.
2. Medium: Host target gates did not reject capitulated releases. They rejected non-existing, subject, self, and war targets, but a living capitulated release could still remain a valid target.
3. Low: `independence_wave_register_successful_release` appended the released country to the host-scoped array without a duplicate guard. Normal release selection should prevent duplicate registration, but helper re-entry would duplicate target cards.
4. Low: `independence_wave_arrest_committee_couriers_cost_tt` and `independence_wave_arm_loyalist_councils_cost_tt` lacked `_blocked` and `_tooltip` localisation variants for `custom_cost_text`.

## Patch

Changed files:

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_event006_dossier_board_host_tools_audit_patch_handoff.md`

Changed identifiers:

- `can_independence_wave_host_target_release`
- `independence_wave_register_successful_release`
- `independence_wave_arrest_committee_couriers_cost_tt_blocked`
- `independence_wave_arrest_committee_couriers_cost_tt_tooltip`
- `independence_wave_arm_loyalist_councils_cost_tt_blocked`
- `independence_wave_arm_loyalist_councils_cost_tt_tooltip`

Before behavior:

- Host-targeted decisions used `target_array = independence_wave_host_released_countries`, but the shared host target trigger did not independently verify host-ledger membership.
- Capitulated Event 006 releases could remain target-valid if they still existed, were independent, and were not at war with the host.
- A duplicate call to `independence_wave_register_successful_release` could duplicate entries in the host-scoped target array.
- Blocked custom costs for the courier and loyalist decisions could fall through to missing localisation keys.

After behavior:

- `can_independence_wave_host_target_release` now requires `FROM` to be present in `ROOT.independence_wave_host_released_countries`.
- Host tools now reject capitulated release targets.
- Host-scoped ledger registration only appends a release if it is not already in that host's array.
- Courier and loyalist custom costs now have blocked and hover text variants.

## Decision Category Lifecycle Notes

`independence_wave_host_aftermath_category` opens through `is_independence_wave_host_aftermath_active`, which requires `independence_wave_recent_host` and `independence_wave_host_aftermath_open`. `independence_wave_recent_host` is timed through `independence_wave_mark_host_aftermath`, so the category naturally closes when the recent-host flag expires. `independence_wave_host_aftermath_open` remains as historical state; that is acceptable for this tranche because visibility still depends on the timed flag.

The host ledger is country-scoped and persistent. New saves after this tranche will populate it during release registration. Existing saves created before this host ledger existed will not have prior releases backfilled; this is noted only, not patched, because adding a backfill would require broader fallback behavior and global reconstruction outside the requested scope.

## Mission Quality Notes

Relevant mission:

- Owner: former host country.
- Category: `independence_wave_host_aftermath_category`.
- Region: host capital administration, represented through host-owned controlled capital checks rather than a named map region.
- Requirement: keep an owned and controlled capital while `independence_wave_hold_capital_ministry` is active.
- Duration: `@independence_wave_host_capital_mission_days`.
- Success: timeout sets `independence_wave_capital_ministry_secured`, `chaosx_iw_host_kept_capital`, stability gain, and host anger relief.
- Failure: completion path sets `independence_wave_capital_ministry_failed`, stability loss, and host anger gain when `can_independence_wave_host_take_capital_mission` is false.
- Duplicate risk: existing terminal flags prevent repeat mission activation after success or failure.

No new timed mission was added in this host-tools tranche.

## Cost And Requirement Clarity Notes

The three host tools are not passive political-power exchanges:

- `independence_wave_offer_local_autonomy` spends political power and host stability for host anger relief and target pressure/radicalization relief.
- `independence_wave_arrest_committee_couriers` spends political power and command power, lowers host stability, and changes target legitimacy, radicalization, and foreign attention.
- `independence_wave_arm_loyalist_councils` spends political power, command power, and infantry equipment, then increases loyalist pressure and target instability variables.

The command power and equipment gates use strict `>` thresholds with `.9` floors to avoid unsupported inclusive comparison tokens. The visible custom cost text now has blocked and tooltip variants for the two decisions that use `custom_cost_text`.

## AI Validity And Route-Lock Notes

AI weights are bounded and situational:

- Autonomy favors democratic and stable hosts, and de-emphasizes war and revolutionary-committee targets.
- Courier arrests favor fascist or wartime hosts, weak-legitimacy targets, and avoid observer-invited contexts.
- Loyalist councils favor fascist or unstable hosts and national-directorate targets, and de-emphasize democratic hosts.

Target validity now rejects non-ledger targets, non-existing releases, subjects, capitulated releases, self-targets, and active host wars. No civil war tags, border transfers, scripted GUI, or Event 005 coupling were added.

## Localisation And Tooltip Gaps

Patched:

- Added blocked and hover variants for `independence_wave_arrest_committee_couriers_cost_tt`.
- Added blocked and hover variants for `independence_wave_arm_loyalist_councils_cost_tt`.

Remaining non-blocking gap:

- The host category description reports global open dossier count, not host-local ledger count. That matches current available display variables, but a host-local dynamic count would be clearer if a future tranche adds a helper for array-size localisation.

## Cleanup And Exploit-Risk Notes

Patched:

- Duplicate host-ledger array entries are now prevented in `independence_wave_register_successful_release`.
- Host target trigger now requires ledger membership and rejects capitulated releases.

Remaining risks:

- Stale annexed or removed countries may remain in the host-scoped array. Target gates prevent them from appearing because `exists = yes` is required, but a later cleanup helper could keep arrays smaller.
- Existing saves without the host ledger will not show these targeted host tools for older releases. This is intentionally noted only.

## Validation

Passed:

- Brace balance:
  - `common/decisions/006_independence_wave_decisions.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
- Unsupported operator check: no unsupported inclusive comparison tokens found in the bounded Event 006 decision/effect/trigger/constants/localisation set.
- Localisation BOM check: `localisation/english/006_independence_wave_l_english.yml` begins with UTF-8 BOM.
- Cost localisation check: the two patched custom-cost ids now have base, `_blocked`, and `_tooltip` keys.

Skipped:

- Runtime in-game UI validation was not run from this environment.

## Concrete Recommended Fixes

Completed in this patch:

- Harden `common/scripted_triggers/006_independence_wave_triggers.txt`: `can_independence_wave_host_target_release`.
- Harden `common/scripted_effects/006_independence_wave_effects.txt`: `independence_wave_register_successful_release`.
- Complete host-tools custom cost localisation in `localisation/english/006_independence_wave_l_english.yml`.

Future optional cleanup:

- Add a narrow stale-ledger cleanup helper for host and global release arrays if later Event 006 work introduces a safe lifecycle point.
- Add a host-local dossier count display if a future scripted-localisation helper can expose host array size cleanly.
