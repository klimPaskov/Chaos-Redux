# Event 006 AGX conference post-repair re-audit

Date: 2026-07-26.

Scope: read-only verification of commit `187115bd1` as contained in current HEAD `13c4eb38b`.

## Bounded verdict

**PASS for the AGX North Sea Coastal Conference lifecycle and civilian-factory cost-text repair.**

No gameplay, localisation, GUI, focus, or asset source was edited by this re-audit.

## Verified repair contract

The repaired decision is `independence_wave_agx_convene_north_sea_coastal_conference` in `common\decisions\006_independence_wave_wallonia_frisia_decisions.txt`.

Its active `cancel_trigger` now invalidates the 300-day project when any required continuing state is no longer true:

| Continuing gate | Start visibility | Active cancellation |
| --- | --- | --- |
| AGX package | `is_independence_wave_agx_package = yes` | `NOT = { is_independence_wave_agx_package = yes }` |
| Secure waterline | `has_stable_independence_wave_agx_waterline = yes` | `NOT = { has_stable_independence_wave_agx_waterline = yes }` |
| Recognition | `is_independence_wave_recognized_or_later = yes` | `NOT = { is_independence_wave_recognized_or_later = yes }` |
| Network member | `has_country_flag = independence_wave_network_member` | negated member flag |
| Low Countries candidacy | `has_country_flag = independence_wave_low_countries_federation_candidate` | negated candidacy flag |
| Conference mandate | `has_country_flag = independence_wave_agx_north_sea_conference_authorized` | negated authorization flag |
| Client-route exclusion | no `independence_wave_client_route_locked` flag | client-route lock flag present |
| Capital control | required by `available` | capital no longer controlled by ROOT |

The prior route-bypass path is closed: losing recognition, network membership, candidacy, authorization, or client-route eligibility after selection cancels the timer before `remove_effect` can set `independence_wave_agx_north_sea_conference_complete`, grant `independence_wave_nwe_reward_regional_conference`, or unlock the dossier focus.

## Failure and cleanup verification

For a still-live AGX package, the conference cancellation calls `independence_wave_nwe_apply_project_failure`.

That helper applies the existing defined failure package: -10 Legitimacy, -5 Recognition, -10 Capacity, -10 Security, and +15 Instability through the shared country-delta effect.

The canceled decision is removed by the decision lifecycle itself, so it no longer occupies `has_independence_wave_agx_active_package_project`.

No success flag is set on cancellation.

When temporary eligibility returns, a non-client AGX country can make a new paid attempt; when package cleanup occurs, `independence_wave_cleanup_iw_007_frisia` removes the active decision and clears both the authorization and completion flags with the rest of the package state.

## Cost-text verification

Commit `187115bd1` changed the conference to `custom_cost_text = independence_wave_cost_agx_coastal_conference`.

The new primary, `_tooltip`, and `_blocked` keys exist in `localisation\english\006_independence_wave_decisions_l_english.yml`, retain UTF-8 BOM encoding, and each display `constant:independence_wave_decision_cost.civilian_factory_major`.

`civilian_factory_major = 3`, exactly matching the conference's `modifier = { civilian_factory_use = constant:independence_wave_decision_cost.civilian_factory_major }`.

The shared strategic availability trigger requires more than `civilian_factory_standard = 2` available factories, which means three factories are available before the three-factory modifier starts.

The displayed requirement, availability boundary, and active reservation are therefore aligned.

## Remaining low issues

1. The decision still has no named `custom_trigger_tooltip` for its mandate, route, active-project, or capital requirements, and no dedicated player-facing cancellation-result tooltip. The description and cost text are clear enough for this bounded repair, but a later localisation-only pass should replace raw availability detail with named requirement text.

2. The repair handoff `006_agx_decision_lifecycle_repair_2026_07_26.md` refers to a non-existent identifier, `independence_wave_agx_open_north_sea_conference`. The repaired gameplay identifier is `independence_wave_agx_convene_north_sea_coastal_conference`. This is a documentation precision issue only; no consumer uses the incorrect name.

## DM-58 context only

This review did not reopen DM-58.

The current v7 and post-repair DM-58 handoffs retain a source-level PASS for the candidate scope correction, while distinct-owner feasibility and the three-distinct-owner success, failure, rollback, and AI-resource matrix remain unproved.

## Validation and remaining boundary

Meaningful validation traced the conference visibility, availability, active cancellation, failure, success, cleanup, focus authorization, and dossier consumer; compared the exact `187115bd1` diff; verified all eight active cancellation gates in current HEAD; checked the cost key triplet and its BOM; and confirmed that `187115bd1` is an ancestor of current HEAD.

Skipped meaningful validation: no live game or scenario execution was run because this subagent may not launch Hearts of Iron IV.

This is a new dated audit handoff only.

Changed by this audit: `docs\plans\006_independence_wave_plans\subagent_handoffs\006_agx_conference_post_repair_reaudit_2026_07_26.md`.

Changed by the verified repair: `independence_wave_agx_convene_north_sea_coastal_conference`, `independence_wave_cost_agx_coastal_conference`, `independence_wave_cost_agx_coastal_conference_tooltip`, and `independence_wave_cost_agx_coastal_conference_blocked`.

The Event 006 whole-event disposition remains **HOLD**; this PASS does not resolve its separate runtime, focus-layout, compatible-country, formable, SCN-008, asset, achievement, AI/balance, or DM-58 feasibility limitations.
