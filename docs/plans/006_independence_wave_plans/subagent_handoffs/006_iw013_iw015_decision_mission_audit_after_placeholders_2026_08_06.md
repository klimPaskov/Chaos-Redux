# IW-013 NAV and IW-015 GLC decision and mission audit after portrait-source placeholders

Date: 2026-08-06

Status: PASS for the reviewed source-owned lifecycle and cost surfaces. The route-cancellation finding retained below is closed in current source by commit `820c6a0c9`; this handoff preserves the pre-fix finding as traceability only.

This is a bounded read-only audit of the Basque and Galician decision categories after the portrait source-placeholder tranche.

It does not change central admission, content attestation, portraits, flags, characters, advisor icons, focus content, or scripted GUI.

The current package remains source-wired but fail-closed for runtime admission under the existing IW-013/IW-015 audit and attestation gates.

## Files reviewed

- `common/decisions/006_independence_wave_iberian_decisions.txt`
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/ai_strategy/006_independence_wave_iberian.txt`
- `localisation/english/006_independence_wave_iberian_l_english.yml`

## Issue list

### Medium — an active Iberian Network project survives League-route withdrawal

The pre-fix source required `independence_wave_league_route_available` in `visible` but omitted it from `cancel_trigger` for both network decisions. Current source now includes `NOT = { has_country_flag = independence_wave_league_route_available }` in both cancellation triggers, so withdrawal cancels the active project before its reward can fire.

Once either long project has started, withdrawal of that route removes the decision from normal presentation but does not cancel its timer, allowing its `remove_effect` to set the local corridor flag and grant the shared network reward.

The implemented narrow owner patch in `common/decisions/006_independence_wave_iberian_decisions.txt` is:

```txt
# Add to each existing cancel_trigger OR block.
NOT = { has_country_flag = independence_wave_league_route_available }
```

Affected identifiers: `independence_wave_nav_open_iberian_network` and `independence_wave_glc_open_iberian_network`.

The existing `cancel_effect` already applies `independence_wave_iberian_apply_project_failure` while the package remains valid, so no extra cleanup helper is needed for this narrow correction.

### No other confirmed issue in this bounded surface

The current named constants include `@CR_SC_IW_IW_NAV_AI_EMERGENCY_PRIORITY` both at its declaration and use site, so the apparent doubled token is intentional naming rather than an undefined constant.

## Decision-category lifecycle notes

Both categories are locally package-gated by original tag, active-country status, and the matching package identifier.

NAV starts the 420-day `independence_wave_nav_hold_fueros_together` mission only after IW-013 setup and only until its resolved or failed terminal flag exists.

GLC mirrors that with `independence_wave_glc_hold_council_together` and IW-015 setup.

Each mission completes through cancellation when both compact ledgers meet the stable threshold, fails on timeout or loss of capital, and cannot re-arm after either terminal flag.

Every ordinary project blocks concurrent package projects, checks its custom resource trigger and capital control before activation, and cancels when its package, route, former-host relationship, or capital condition becomes invalid.

All package-owned decisions and missions are explicitly removed by `independence_wave_cleanup_iw_013_basque` and `independence_wave_cleanup_iw_015_galicia`.

Those cleanup effects also clear both dynamic ledger variables, lifecycle and terminal flags, government-route flags, project flags, sovereignty flags, corridor flags, and package ideas.

## Mission quality notes

| Owner | Category | Requirement and duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| NAV | `independence_wave_nav_iberian_category` | Complete IW-013 setup; Fueros Legitimacy and Industrial Capacity must each reach 60 within the founding-crisis duration. | Both ledgers stable cancels to the resolved terminal state. Timeout or capital loss sets failure and applies the shared project-failure effect. | Terminal flags block reactivation; only one NAV mission exists. |
| GLC | `independence_wave_glc_iberian_category` | Complete IW-015 setup; Council Legitimacy and Port Capacity must each reach 60 within the same founding-crisis duration. | Mirrors NAV with GLC terminal flags and the same shared failure effect. | Terminal flags block reactivation; only one GLC mission exists. |

The ledgers are dynamic variables, initialised in their package setup effects, clamped through `independence_wave_change_nav_compact_values` or `independence_wave_change_glc_compact_values`, and checked with the shared stable threshold rather than duplicated literal values.

## Costs and requirement clarity

The surfaces do not use flat political-power exchanges.

Security projects consume manpower, army experience, infantry equipment, and support equipment.

Administration uses available civilian-factory capacity, command power, and manpower.

Diplomatic projects use command power plus either convoys or trains.

Sovereignty combines factory capacity, stability, war support, and the diplomatic standard cost.

The player-facing cost labels are custom cost text keys, and all reviewed named decisions and mission/project outcomes have localisation.

The category text exposes the live ledger values and the 60-point compact requirement, while project and network effect tooltips state the intended results.

## AI validity and route locks

Standard, high, and urgent `ai_will_do` scores use shared AI constants.

The emergency-command decisions double their score while at war, which is a coherent local priority modifier rather than a random or unbounded weight.

The separate Iberian AI strategies retain package, setup, profile, and relevant compact/host conditions.

Route choices are mutually guarded by the shared availability flag and the absence of the package-local government-route flag, then self-cancel if their route flag is lost.

Former-host projects require a living former host, forbid an active war with that host, and self-cancel on host loss or war.

Network projects require both membership and the League-route flag to become visible, and the current cancellation trigger keeps them route-locked after activation.

Sovereignty is one-shot, requires the founding settlement, a selected government route, stable ledgers, strategic resources, and no active package project.

## Localisation and tooltip review

All reviewed NAV and GLC category, mission, project, route, sovereignty, network, and effect-tooltip keys are present in `006_independence_wave_iberian_l_english.yml`.

No raw compound trigger has been placed in player-facing prose for the reviewed actions.

No advisor icon, advisor sprite, or portrait key is referenced by these decision surfaces.

## Cleanup and exploit-risk review

The per-package active-project trigger includes the complete timed-project set, which prevents concurrent resource-spend or ledger-reward loops inside a package.

The immediate sovereignty decision uses `fire_only_once` and a durable-sovereignty flag.

The host project has a settled flag, and network projects have package-local corridor flags, preventing repeat completion.

Cleanup removes both active decisions and terminal state, preventing stale package variables and decisions after package teardown.

The route-withdrawal race is closed by the current cancellation trigger; no equipment, unit, core, or war-goal farming loop was found in the reviewed NAV/GLC decision effects.

## HOI4 MCP evidence and limitations

No decision-owned scripted GUI is declared in `006_independence_wave_iberian_decisions.txt`, so `hoi4.gui_inspect` and `hoi4.gui_render` do not have an in-scope window to inspect or render.

`hoi4.probability_inspect` reviewed the current decision source at source revision `1e4306c8e4bf58005a0be93a3878d0b0eec45b096b752fa67aabdf5f562c022e` and source hash `72bfdb04bc4d3e6db6911989976d35a21f5913a526ab5fc93407043e841caa15`.

The `decision_ai_will_do` adapter found 2 score surfaces with 9 required scenario inputs and no source-resolution error.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77e3a1a22851c01b4005cfa882c575b555c4dc413015d0429e5c00c130ae8abf/e8877d50bfe64661f09e7b0489f5b65f72cb915b3613f9346853f66407c205d3/probability-inspect-72bfdb04bc4d.json`.

The `mission_ai_will_do` adapter found 22 timed score surfaces with 12 required scenario inputs and no source-resolution error.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80fd19b5b89d029f6bce23f4c5e20fe93245e2091333766f925b061e29dbc79d/9524a6880d8407fa38222bfa3192ca072626f8f4c9fdf3b3984795d069f60a2a/probability-inspect-72bfdb04bc4d.json`.

Both MCP pools are marked `poolComplete = false`, and this deliberately bounded tranche did not run a broad synthetic scenario sweep or simulation.

The required independent `chaosx_ai_probability_auditor` route was attempted before this handoff, but its session could not initialise because `blender_hoi4` and `meshy` timed out while listing tools after 120 seconds.

Accordingly, the MCP source artifacts are useful evidence of discovered score surfaces, not a substitute for the required independent scenario-based probability audit if AI weights are changed.

## Changes and validation

Changed files: this handoff only.

No gameplay, GUI, localisation, focus, AI, admission, attestation, portrait, advisor, or asset file was changed.

Meaningful validation consisted of source-tracing the live lifecycle, cost, active-project, compact-ledger, host/route, reward, cleanup, and localisation paths, plus the two current MCP source-inspection artifacts above.

Skipped validation: no live HOI4 run was performed, no scripted GUI rendering applies, and no synthetic AI sweep was run because this was read-only and the independent probability-auditor route was unavailable.

## Remaining issues and handoff

Do not promote central IW-013/IW-015 admission based on this audit.

The existing source-placeholder portrait status remains pending its separate final-image and attestation work.

No gameplay patch remains for this finding. The source-placeholder portrait, flag identity, command-roster, package-attestation, and named-scenario probability gates remain open; a probability comparison is required only if a future AI weight changes.
