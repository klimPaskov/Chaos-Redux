# Event 006 Patronage and Recognition Decision Audit Handoff

## Scope

Audited the Event 006 major/regional-power Patronage and Recognition tranche:

- Category: `independence_wave_patronage_recognition_category`
- Triggers: `can_independence_wave_open_patronage_recognition`, `can_independence_wave_major_target_release`, `can_independence_wave_major_recognize_committee`, `can_independence_wave_major_supply_rifles`, `can_independence_wave_major_offer_military_mission`, `can_independence_wave_major_demand_cabinet_seats`, `can_independence_wave_major_sabotage_rival_patron`
- Decisions: `independence_wave_major_recognize_committee`, `independence_wave_major_supply_rifles`, `independence_wave_major_offer_military_mission`, `independence_wave_major_demand_cabinet_seats`, `independence_wave_major_sabotage_rival_patron`
- Effects: `independence_wave_major_recognize_committee_effect`, `independence_wave_major_supply_rifles_effect`, `independence_wave_major_offer_military_mission_effect`, `independence_wave_major_demand_cabinet_seats_effect`, `independence_wave_major_sabotage_rival_patron_effect`

No flag assets, flag graphics, country definitions, country history, or Event 005 Soviet Collapse files were touched.

## Issue List

1. Medium: `can_independence_wave_open_patronage_recognition` used `global.independence_wave_actual_release_count > 0`. That variable is reset at the start of each Event 006 wave, while `global.independence_wave_released_countries` is intentionally persistent. A later zero-release wave could hide the major-power category even though living Event 006 releases still exist.
2. Low: the persistent release target array can retain annexed/dead entries. The current target triggers correctly require `exists = yes`, so this is UI/performance cleanup risk rather than a functional break.
3. Low: category priority matches `independence_wave_patron_ledger_category` at `87`. This is not invalid, but the parent may want a distinct priority if category ordering becomes important.

## Patch

Changed `common/scripted_triggers/006_independence_wave_triggers.txt`.

Before:

- `can_independence_wave_open_patronage_recognition` opened only when the current-wave release counter was above zero.

After:

- The gate now checks `any_of_scopes` over `global.independence_wave_released_countries` and requires at least one existing, independent Event 006 release.
- Major/regional powers still must be non-Event-006 actors, non-subjects, and either majors or above the regional factory threshold.

This keeps the category tied to real living targets without adding whole-world polling, new country files, puppet creation, faction creation, Event 005 coupling, or asset work.

## Decision Category Lifecycle Notes

`independence_wave_patronage_recognition_category` has a clear reveal path through `can_independence_wave_open_patronage_recognition`. The patch makes that reveal follow the persistent Event 006 release ledger instead of the current-wave counter. `visible_when_empty = yes` remains acceptable because the gate now requires at least one living independent Event 006 release before outside powers see the category.

## Mission Quality Notes

No missions belong to this tranche. All audited items are click decisions with `days_re_enable = @independence_wave_major_patronage_days`.

- Owner: non-subject outside major/regional power
- Category: `independence_wave_patronage_recognition_category`
- Region: global targeted country array, limited to Event 006 releases
- Requirement: actor eligibility plus target eligibility, resource gates where relevant
- Duration: repeat cooldown, not timed mission duration
- Success: immediate target variable/flag/resource effects
- Failure: no timed failure path because these are discrete diplomatic/patronage actions
- Duplicate risk: target-side completion flags prevent each release from receiving duplicate recognition, rifle supply, military mission, cabinet demand, or sabotage outcomes

## Cost And Requirement Clarity

Costs are not passive political-power-only exchanges:

- Recognition and cabinet demands use political power as diplomatic expenditure.
- Rifle supply uses political power plus real infantry/support equipment spending.
- Military mission uses political power plus army XP and command power.
- Rival sabotage uses political power plus command power.

Custom costs have matching effect spending for rifle supply, military mission, and sabotage. The localisation cost keys exist and are compact icon/value text. Target filters are hidden from raw UI with `hidden_trigger` rather than exposing long trigger blocks.

## AI Validity And Route-Lock Notes

AI weights exist for every decision. They respond to government, war state, target route flags, patron-cabinet route, officer route, anti-puppet clause, and balanced-rival-patron state. Target eligibility excludes dead targets, subjects, self-targeting, and countries at war with the actor. No invalid country targets, impossible borders, puppet creation, faction creation, or Event 005 route coupling were found.

## Localisation And Tooltip Gaps

Localisation exists for category name/description, all five decision names/descriptions, all five effect tooltips, and the three custom cost text keys. The localisation file remains UTF-8 with BOM and does not use `:0` keys. No new localisation was needed for the patch.

## Cleanup And Exploit-Risk Notes

The target-side flags block repeat farming per release. Rifle and mission decisions spend real resources before granting target gains. Sabotage clamps patron leverage after reducing it. No free-unit loop, equipment farming loop, war-goal spam, core spam, puppet route, or faction route was found in this tranche.

Remaining cleanup risk: stale countries may remain in `global.independence_wave_released_countries` after annexation. Current `exists = yes` checks keep them from being valid targets, but a future ledger cleanup helper would keep the array smaller.

## Validation

Performed:

- Consulted offline wiki pages for decisions, targeted decision scope semantics, effects, triggers, localisation, data structures, scopes, on actions, modifiers, events, ideas, and AI.
- Consulted vanilla documentation for effects, triggers, script concepts, and script constants.
- Checked vanilla targeted decision precedent in `~/projects/Hearts of Iron IV/common/decisions/HOL.txt`.
- Verified targeted decision scope semantics: ROOT is the actor, FROM is the target.
- Ran brace-balance checks on the bounded Event 006 decision, category, constants, trigger, and effect files.
- Ran unsupported operator scan for `<=` and `>=` across the bounded Clausewitz files.
- Checked localisation encoding and confirmed UTF-8 with BOM.
- Checked localisation for `:0` key style in `localisation/english/006_independence_wave_l_english.yml`.

Skipped:

- Runtime HOI4 UI validation, because this subagent cannot launch and verify an in-game session.
- Git commit, because the bounded Event 006 files are pre-existing dirty/untracked work from the wider implementation tranche; committing them would capture work outside this audit.

## Remaining Risks

- Runtime UI ordering for the Patronage and Recognition category has not been seen in game.
- Persistent release-ledger cleanup remains future hardening.
- Broad patron-vs-patron intelligence chains, host-border guarantees, and autonomy brokering remain outside this bounded first-pass tranche.
