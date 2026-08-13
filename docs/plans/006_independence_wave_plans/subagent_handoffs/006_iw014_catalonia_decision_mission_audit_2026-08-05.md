# Event 006 IW-014 Catalonia Decision and Mission Audit

## Scope and status

This is a fresh current-state, CAT-only audit after the standalone-admission edits.

It inspected the CAT decisions, category, package triggers and effects, CAT constants and AI strategy, shared cost and route helpers, package dispatch, FORM-07 triggers and effects, formable registry, and the current localisation surfaces.

No gameplay or localisation file was edited.

The offline Paradox wiki decision reference, vanilla decision/effect/trigger documentation, and the Event 006 decision/mission workflow were consulted before this audit.

## Result

IW-014 CAT remains independently admissible as a complete Event 006 carrier.

FORM-07 discovery remains fail-closed when its readiness is false.

No CAT decision, mission, cost, route, AI, cleanup, or timer defect requiring a gameplay patch was found.

## Issue list, sorted by severity

### Medium — player-facing CAT ledger values are not surfaced

`independence_wave_cat_hold_industrial_compact_together` succeeds only when both industrial cohesion and assembly legitimacy reach 60.

The category description and mission text describe the two ledgers but expose neither current value nor the threshold, and no CAT scripted-localisation value token was found.

The CAT decision and mission logic is correct, but this leaves players without a direct progress readout for the timed 420-day crisis.

Recommended narrow follow-up: add the two dynamic variable values and the stable threshold to `localisation/english/006_independence_wave_catalonia_l_english.yml` under `independence_wave_cat_industrial_compact_category_desc`, using the same player-facing ledger pattern as the current Iberian category descriptions.

### Low — Mediterranean Network cancellation does not restate the league-route flag

`independence_wave_cat_open_mediterranean_network` correctly requires package identity, network membership, the league-route availability flag, an unsettled corridor, a stable compact, material cost, capital control, and CAT project serialization before it can begin.

Its cancellation trigger rechecks package identity, network membership, and capital control but not `independence_wave_league_route_available`.

Current source evidence shows that the league-route flag is granted during CAT setup and cleared only by package-wide focus-runtime teardown, which also removes CAT decisions, so no reachable completion bypass was found.

Recommendation: keep this as a low-priority defensive-hardening item. If focus runtime may later be reconfigured without package teardown, add `NOT = { has_country_flag = independence_wave_league_route_available }` to this decision's cancellation trigger.

## Decision category lifecycle notes

The category is visible only for the exact CAT package after IW-014 setup completes.

The lifecycle is setup, 420-day industrial compact crisis, serialized paid construction and settlement work, focus-committed government implementation, immediate durable-sovereignty codification, and an optional 180-day Mediterranean Network corridor.

Industrial cohesion begins at 38 and assembly legitimacy begins at 42, both are clamped to 0 through 100, and both must reach 60 for a stable compact.

`has_independence_wave_cat_active_package_project` lists all eleven CAT actions, and each action tests that predicate before it begins.

The ten timed CAT actions have matching cancellation triggers and cancellation effects. The remaining action, `independence_wave_cat_codify_durable_sovereignty`, is immediate and `fire_only_once`.

## Mission quality notes

| Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAT | `independence_wave_cat_industrial_compact_category` | Catalonia, state 165 | IW-014 setup, both compact ledgers at 60, capital held | 420 days | Cancels and records `independence_wave_cat_compact_crisis_resolved` | Capital loss or timeout records `independence_wave_cat_compact_crisis_failed` and applies the package failure effect | Closed: activation excludes both terminal flags and package cleanup clears both |

The mission is a genuine timed state-building objective, not a passive decision store.

Its paid projects move the local compact ledgers and the shared statehood, host-relation, Network, and League ledgers with separate administrative, security, diplomatic, and strategic outcomes.

## Cost and timer notes

All eleven CAT projects have a matching custom cost trigger, custom cost text, and payment call.

The six CAT cost types resolve in shared localisation.

Administrative projects spend Command Power and manpower while reserving one or two civilian factories for their timed duration.

Security projects spend manpower, Army Experience, infantry equipment, and support equipment.

Diplomatic projects spend Command Power plus a convoy or train, and strategic sovereignty spends stability, war support, and the diplomatic-standard cost.

All shared spend constants used by CAT are negative deductions.

No CAT-local political-power store, free unit creator, equipment grant, or material farming loop was found.

Timed project lengths are deliberately varied through the shared table: 75 days for light administration and constitutional or workers implementation, 120 days for standard and major security work, and 180 days for host, municipal, patron, and Network work.

## Route locks and AI willingness

The five CAT government projects are correctly focus-locked, not self-selecting.

Each project becomes visible only after the generic full focus framework has committed the matching shared route through `independence_wave_focus_lock_constitutional_route`, `independence_wave_focus_lock_popular_council_route`, `independence_wave_focus_lock_traditional_route`, `independence_wave_focus_lock_emergency_military_route`, or `independence_wave_focus_lock_patron_client_route`.

The matching CAT installer then verifies the selected shared route before installing its local government idea, party state, and flag.

All twelve CAT decision or mission entries carry an `ai_will_do` block.

The emergency route gains priority during war, the former-host settlement gains priority outside severe host threat, and the patron route gains priority during severe host threat.

The four CAT AI strategy layers are constrained by original tag, exact package state, setup or local route state, and `abort_when_not_enabled = yes`.

## Mediterranean Network and FORM-07 guard notes

The CAT Network decision is visible only to an exact IW-014 country that is an active Network member, has the league route available, and has not opened its corridor.

On completion it sets `independence_wave_cat_mediterranean_corridor_open`, updates the CAT, Network, and League ledgers, and only attempts to unlock formable discovery inside an existing `has_independence_wave_formable_commit_readiness = yes` guard.

FORM-07 still requires the generic discovery gate and its complete readiness gate even if a discovery-unlock flag were present.

The FORM-07 readiness gate requires the exact Iberian family profile, matching readiness family, identity compatibility, territory adapter, X-tag reservation, flag package, identity adapter, integration adapter, member-policy audit, and `independence_wave_form07_readiness_attested`.

Its own identity runtime contract additionally requires `independence_wave_form07_identity_attested`, `independence_wave_form07_x_tag_reserved`, and `independence_wave_form07_flag_package_ready`.

No writer for those three FORM-07 identity-contract flags exists in `common/`, and CAT itself writes none of the generic FORM-07 commit flags.

Therefore the generic readiness check is false in the current source and the CAT Network completion cannot unlock FORM-07 discovery.

The CAT admission dispatcher explicitly documents and enforces this separation: IW-014 can pass country-package dispatch and final validation without promoting FORM-07.

## Localisation and tooltip notes

All twelve direct CAT decision and mission localisation keys resolve, and CAT localisation remains UTF-8 with BOM.

Timed project completion, failure, host, route, patron-route, sovereignty, and Network outcome tooltips are present.

The only material player-facing gap found is the missing dynamic compact-ledger readout described in the issue list.

## Cleanup and exploit-risk notes

`independence_wave_cleanup_iw_014_catalonia` removes the mission and all eleven CAT decisions, removes CAT ideas, clears the two local variables, terminal mission flags, route-government flags, durable-sovereignty flag, Mediterranean-corridor flag, and the standalone family-registration runtime data.

The package dispatcher calls CAT setup, final validation, and cleanup entry points.

No stale target, dead former-host decision, disabled-route completion, cooldown abuse, core spam, war-goal spam, unit loop, or resource-farming path was found in the CAT decision surface.

No decision-owned scripted GUI exists in this scope, so GUI inspection and rendering were not applicable.

## Meaningful validation

Static CAT contract checks found 12 direct CAT decision or mission IDs, 11 CAT project IDs, zero projects absent from the active-project serialization list, and zero projects absent from CAT cleanup.

The same check found ten timed project actions, all twelve entries with AI willingness, one founding-mission activation block excluding both terminal flags, and two terminal flags cleared by cleanup.

All direct CAT localisation keys and all six CAT cost-text keys resolve.

The CAT-local decision and package-effect files contain zero political-power, unit-creation, or equipment-stockpile effect tokens.

Static FORM-07 verification found zero writers for the three identity-contract flags anywhere under `common/`, zero CAT writers for generic FORM-07 commit flags, and the guarded CAT Network discovery call described above.

No live game validation or full AI scenario execution was run because those checks are user-owned and outside this read-only audit.

## Changed files

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw014_catalonia_decision_mission_audit_2026-08-05.md`

## Simplifications, omissions, and blockers

No gameplay patch was made, as requested.

No unapproved fallback or simplification was used.

The two non-blocking follow-ups are limited to CAT ledger visibility and defensive cancellation hardening for a future focus-runtime reconfiguration.

## Skills used

`chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` guided the CAT audit, Event 006 integration checks, and this handoff.
