# Event 006 IW-013 NAV and IW-015 GLC Decision and Mission Audit

## Scope and outcome

Audited the current NAV and GLC Iberian decision categories in `common/decisions/006_independence_wave_iberian_decisions.txt` with their direct package triggers, effects, constants, cost helpers, localisation, AI strategies, and cleanup dispatch.

Patched one narrow localisation drift defect in `localisation/english/006_independence_wave_iberian_l_english.yml`.

The four descriptions that state the founding-compact threshold now render `[?constant:independence_wave_iberian_pressure.stable|0]` instead of a literal `60`.

No decision, mission, effect, trigger, AI score, country package, portrait, advisor, icon, or shared system was changed.

## Changed files and identifiers

- `localisation/english/006_independence_wave_iberian_l_english.yml`
  - `independence_wave_nav_iberian_category_desc`
  - `independence_wave_nav_hold_fueros_together_desc`
  - `independence_wave_glc_iberian_category_desc`
  - `independence_wave_glc_hold_council_together_desc`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_decision_mission_audit_2026_08_06.md`

Before the patch, the player-facing threshold could disagree with `independence_wave_iberian_pressure.stable` after a tuning change.

After the patch, the category summaries and both founding-mission descriptions read the same script constant used by `has_stable_independence_wave_nav_compact` and `has_stable_independence_wave_glc_compact`.

## Issues sorted by severity

### Medium: AI can select a pre-stability emergency route that cannot satisfy the founding mission on time

`independence_wave_nav_establish_pyrenean_command` and `independence_wave_glc_establish_coastal_command` have the `urgent` AI score, which is `100`, and double it at war.

Each route takes `120` days, reduces one compact measure by `5`, and prevents selection of another government route.

NAV begins at `46/34` and reaches only `86/59` after that route plus all three core compact projects at day `480`.

GLC begins at `43/36` and reaches `83/61` after the equivalent sequence, also at day `480`.

The founding mission expires at day `420`, while its normal three-project recovery path reaches NAV `71/64` and GLC `68/66` at day `360`.

This is a source-derived AI timing risk, not an asserted click probability.

Do not patch it until the mandatory named-scenario probability baseline and post-patch compare are available.

Recommended bounded owner patch after that evidence exists: add a zero-factor `ai_will_do` modifier while the respective compact is not stable to the two emergency-route decisions only.

### Low: player-facing founding threshold could drift from the script constant

The four affected strings used literal `60` even though the actual stability predicate reads `constant:independence_wave_iberian_pressure.stable`.

This was patched as described above.

### Low: some blocked available conditions remain engine-generated rather than custom trigger tooltips

The normal project decisions expose capital control, active-project serialization, and route or former-host conditions through `available` blocks.

Existing title, description, custom-cost, and effect-tooltip coverage explains the principal conditions, but the current source has no local custom trigger-tooltip wrappers for every engine-generated blocked line.

This was not changed because UI exposure cannot be confirmed without live consumer evidence and a broad tooltip wrapper pass would exceed the bounded audit.

## Decision category lifecycle notes

`independence_wave_nav_iberian_category` and `independence_wave_glc_iberian_category` each contain one founding mission and eleven paid projects.

The mission activates only after its exact package setup flag, cannot rearm after its resolved or failed terminal flag, and cancels successfully when both compact values meet the stable predicate.

Capital loss causes a failure path, while package withdrawal cancels the local surface.

Each ordinary project serializes through `has_independence_wave_nav_active_package_project` or `has_independence_wave_glc_active_package_project`.

Former-host settlement also cancels when the persisted former host no longer exists or a war starts with it.

`independence_wave_cleanup_iw_013_basque` and `independence_wave_cleanup_iw_015_galicia` remove the active mission, all eleven local decisions, local ideas, ledger variables, lifecycle flags, route flags, network flags, and terminal flags.

The cleanup dispatch is called from `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`.

Neither category has a `scripted_gui` binding, so no decision-owned scripted-GUI inspection or render applies to this scope.

## Mission quality notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_nav_hold_fueros_together` | NAV | Basque Founding Compact | Iberia | Fueros Legitimacy and Industrial Capacity each meet the stable constant while the capital remains controlled | 420 days | `cancel_effect` marks the compact resolved after `has_stable_independence_wave_nav_compact` | Timeout or capital loss marks failure and applies the Iberian project-failure deltas | Low, parallel to GLC but uses NAV-specific values and effects |
| `independence_wave_glc_hold_council_together` | GLC | Galician Founding Council | Iberia | Council Legitimacy and Port Capacity each meet the stable constant while the capital remains controlled | 420 days | `cancel_effect` marks the compact resolved after `has_stable_independence_wave_glc_compact` | Timeout or capital loss marks failure and applies the Iberian project-failure deltas | Low, parallel to NAV but uses GLC-specific values and effects |

The missions are real timed objectives rather than passive stockpile checks.

Their distinct regional ledgers, starting values, reward hooks, and ideas keep the parallel structure intentional.

## Cost and requirement clarity notes

The decisions do not use political-power store exchanges.

Security projects consume manpower, Army Experience, infantry equipment, and support equipment through `independence_wave_decision_pay_security_standard` or `_major`.

Administration projects consume spare civilian-factory capacity during their timers, command power, and manpower.

Diplomatic projects consume command power plus convoys or trains.

The sovereignty action consumes stability, war support, a diplomatic-standard package, and spare civilian factories.

The custom cost triggers match the payment helpers, and the custom cost text has normal, blocked, and tooltip entries in `localisation/english/006_independence_wave_decisions_l_english.yml`.

Shared cost and duration values are centralized in `common/script_constants/006_independence_wave_decision_constants.txt`.

## AI validity and route-lock notes

Every local decision and mission has `ai_will_do` coverage.

Package identity checks, setup flags, capital control, active-project serialization, route flags, existing-government guards, Network membership, and living-former-host checks prevent invalid actions from appearing or completing.

The former-host variable is protected by `has_independence_wave_living_former_host`, which requires both the persisted scope variable and `exists = yes`.

The emergency-route timing risk above remains unresolved because the required probability result was interrupted.

The intended probability route was delegated to `chaosx_ai_probability_auditor` with mandatory `hoi4.probability_inspect`, typed `decision_ai_will_do` and `mission_ai_will_do` scenarios, and a threshold sweep.

The delegated audit was interrupted before it returned an MCP artifact, analysis identifier, scenario hash, evaluate result, sweep, or compare result.

Therefore this handoff records no numeric click probability, no score-to-choice conversion, and no AI-weight patch.

## Localisation and tooltip gaps

All two category names, two category descriptions, two founding-mission descriptions, twenty-two project names and descriptions, cost keys, and project-effect tooltips resolve in the assigned Iberian localisation or shared decision localisation.

The current former-host descriptions resolve `[independence_wave_former_host.GetNameDef]` only while the decision is visible behind the living-host guard.

The completed dynamic-threshold patch removes the identified localisation drift risk.

## Cleanup and exploit-risk notes

All compact-value changes are clamped to the shared minimum and maximum.

Core project output flags make the local projects one-time actions, government selection is guarded by the route-government predicate, sovereignty is `fire_only_once`, and Network opening is guarded by a completion flag.

No free-unit loop, equipment-farming loop, core or claim spam, or repeatable route-reward loop was found in this bounded surface.

Project cancellation deliberately retains paid commitment and applies the defined project-failure consequence when the carrier remains valid but loses its capital, route, or former-host negotiation context.

## Evidence and validation

Consulted the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding.

Consulted the installed vanilla decision examples plus the official `effects_documentation.md`, `triggers_documentation.md`, `dynamic_variables_documentation.md`, and `script_concept_documentation.md`.

The decisive vanilla semantics used here are that mission activation is daily, `visible` does not control missions, `cancel_trigger` and `cancel_effect` provide early mission cleanup, and `remove_mission` bypasses mission outcome effects during full package cleanup.

The static post-patch check verified the four dynamic threshold tokens, both mission blocks, all eleven project identifiers per carrier, the source stable constant, and the required UTF-8 BOM.

The first version of that check expected ten projects and failed because the source correctly contains eleven per carrier.

The corrected check passed with `DYNAMIC_THRESHOLD_KEYS=4`, `FOUNDING_MISSIONS=2`, `PROJECTS_NAV=11`, and `PROJECTS_GLC=11`.

Meaningful validation skipped: live-game and save consumer tests belong to the user, and there is no decision-owned scripted GUI to render.

Meaningful validation blocked: the mandatory MCP decision and mission probability evidence was interrupted before artifact production, so source review is explicitly not treated as equivalent probability evidence.

## Parent follow-up

Run or resume the NAV and GLC `decision_ai_will_do` and `mission_ai_will_do` MCP audit under named normal and wartime founding scenarios.

If its baseline confirms the emergency-route priority risk, apply the two-decision zero-factor pre-stability AI guard and run `hoi4.probability_compare` against those same scenarios.

Do not use this audit to admit NAV or GLC, change their portrait or flag status, or alter shared Event 006 balance.

## Skills used

`chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` guided the audit, lifecycle review, and handoff boundary.
