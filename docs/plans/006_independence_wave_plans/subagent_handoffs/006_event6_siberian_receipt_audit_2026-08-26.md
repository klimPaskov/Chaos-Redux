# Event 006 Siberian founding-mission setup-receipt audit

Date: 2026-08-26.

Status: complete for the bounded receipt-lifecycle surface; six minimal source guards were added and no files were staged or committed.

## Scope and evidence

This audit covers the founding mission blocks for Altai, Buryatia, Khakassia, Sakha, Udmurtia, Komi, Tatarstan, and Ruthenia in `common/decisions/006_independence_wave_siberian_decisions.txt`.

The only gameplay file changed is `common/decisions/006_independence_wave_siberian_decisions.txt`; this handoff is the only documentation file created for this subagent task.

I read `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, the Event 006 README and mechanics/package specifications, the current Event 006 plan and package handoffs, the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding, and the relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

The offline references confirm that mission `activation` controls automatic activation, `available = { always = no }` is appropriate for an automatic mission, `cancel_trigger` removes a timed mission without running its timeout path, and country flags are valid trigger/effect state for this receipt contract.

## Severity-ordered findings

### High severity before patch: six founding missions could outlive a missing setup receipt

Altai IW-053, Buryatia IW-052, Khakassia IW-054, Sakha IW-051, Udmurtia IW-048, and Komi IW-050 already required their package setup-complete flag in `activation`, but their founding-mission `cancel_trigger` blocks did not cancel when that same flag was absent.

The resulting asymmetry could leave an already active founding mission present while its package setup was being rebuilt or had failed to prepare, even though the mission could no longer activate from that receipt state.

The patch adds one matching `NOT = { has_country_flag = <same_setup_flag> }` guard to each affected founding-mission cancellation `OR` block and leaves every other trigger, effect, cost, AI weight, admission, route, and balance expression unchanged.

### No issue: Tatarstan and Ruthenia were already covered

Tatarstan IW-044 already had `NOT = { has_country_flag = independence_wave_iw_044_setup_complete }` in `independence_wave_tat_hold_river_compact_together` at source line 2830 before this audit.

Ruthenia IW-038 already had `NOT = { has_country_flag = independence_wave_iw_038_setup_complete }` in `independence_wave_rut_hold_mountain_compact_together` at source line 3401 before this audit.

Those existing guards remain unchanged.

No other omission was found in the requested receipt contract after the focused assertions below.

## Exact package and guard audit

| Package | Category and founding mission | Region/anchor | Activation receipt | Setup clear and prepared restore evidence | Cancel guard after patch | Disposition |
|---|---|---|---|---|---|---|
| Altai IW-053 | `independence_wave_altai_mountain_compact_category`; `independence_wave_altai_hold_mountain_council` | Altai, state 654 Oyrot | `independence_wave_iw_053_setup_complete` at line 27 | `common/scripted_effects/006_independence_wave_siberian_package_effects.txt`: setup effect line 319 clears; initialization begins line 343; prepared gate line 384 restores at line 385 | `NOT = { has_country_flag = independence_wave_iw_053_setup_complete }` at line 39 | Added missing guard. |
| Buryatia IW-052 | `independence_wave_buryatia_frontier_compact_category`; `independence_wave_bya_hold_frontier_council` | Buryatia, state 564 Ulan-Ude | `independence_wave_iw_052_setup_complete` at line 624 | `common/scripted_effects/006_independence_wave_siberian_package_effects.txt`: line 783 clears; initialization begins line 806; prepared gate line 844 restores at line 845 | `NOT = { has_country_flag = independence_wave_iw_052_setup_complete }` at line 633 | Added missing guard. |
| Khakassia IW-054 | `independence_wave_khakassia_frontier_compact_category`; `independence_wave_kha_hold_frontier_council` | Khakassia, state 569 Minusinsk | `independence_wave_iw_054_setup_complete` at line 1195 | `common/scripted_effects/006_independence_wave_siberian_package_effects.txt`: line 1242 clears; initialization begins line 1265; prepared gate line 1303 restores at line 1304 | `NOT = { has_country_flag = independence_wave_iw_054_setup_complete }` at line 1204 | Added missing guard. |
| Sakha IW-051 | `independence_wave_sakha_arctic_compact_category`; `independence_wave_yak_hold_arctic_council` | Sakha, state 574 Yakutsk | `independence_wave_iw_051_setup_complete` at line 1766 | `common/scripted_effects/006_independence_wave_siberian_package_effects.txt`: line 1733 clears before initialization line 1757; prepared gate line 1796 restores at line 1797 | `NOT = { has_country_flag = independence_wave_iw_051_setup_complete }` at line 1775 | Added missing guard. |
| Udmurtia IW-048 | `independence_wave_udm_industrial_forest_category`; `independence_wave_udm_hold_workshop_congress` | Udmurtia, state 399 Izhevsk | Inline activation at line 2333 includes `independence_wave_iw_048_setup_complete` | `common/scripted_effects/006_independence_wave_udm_package_effects.txt`: line 254 clears; initialization begins line 277; prepared gate and restore are inline at line 312 | Inline cancel trigger at line 2336 now includes `NOT = { has_country_flag = independence_wave_iw_048_setup_complete }` | Added missing guard. |
| Komi IW-050 | `independence_wave_komi_northern_compact_category`; `independence_wave_komi_hold_northern_council` | Komi, state 397 Syktyvkar | `independence_wave_iw_050_setup_complete` at line 2532 | `common/scripted_effects/006_independence_wave_komi_package_effects.txt`: line 331 clears; initialization begins line 354; prepared gate line 392 restores at line 393 | `NOT = { has_country_flag = independence_wave_iw_050_setup_complete }` at line 2542 | Added missing guard. |
| Tatarstan IW-044 | `independence_wave_tat_river_compact_category`; `independence_wave_tat_hold_river_compact_together` | Tatarstan, state 249 | `independence_wave_iw_044_setup_complete` at line 2821 | `common/scripted_effects/006_independence_wave_tatarstan_package_effects.txt`: line 333 clears; initialization begins line 356; prepared gate line 394 restores at line 395 | Existing `NOT = { has_country_flag = independence_wave_iw_044_setup_complete }` at line 2830 | Already correct; unchanged. |
| Ruthenia IW-038 | `independence_wave_rut_mountain_compact_category`; `independence_wave_rut_hold_mountain_compact_together` | Ruthenia, state 73 | `independence_wave_iw_038_setup_complete` at line 3392 | `common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt`: line 346 clears; initialization begins line 369; prepared gate line 407 restores at line 408 | Existing `NOT = { has_country_flag = independence_wave_iw_038_setup_complete }` at line 3401 | Already correct; unchanged. |

## Decision-category lifecycle notes

Each requested surface uses one automatic/timed founding mission with `available = { always = no }` and an `activation` trigger that is evaluated by the mission system.

The mission is the category's founding phase, while the package projects remain phase-gated and serialized through their package active-project trigger; the receipt is also part of the package project-ready trigger for the paid decisions.

The founding mission's existing cancel effect marks the compact crisis resolved only when stable ledgers, the package route government, the designated anchor ownership/control, and the required capital control are all satisfied; otherwise a package-owned failure flag and existing project-failure helper run for an admitted package.

The existing timeout effect marks the package compact crisis failed and calls the same package failure helper; no timeout or success behavior was changed.

No decision-owned scripted GUI is linked to these categories, so GUI inspect/render/rewrite evidence is not applicable to this bounded source surface.

## Mission quality notes

| Mission owner | Requirement and route gate | Duration | Success | Failure/cancel | Duplicate risk |
|---|---|---|---|---|---|
| Altai IW-053 | Altai package, identity-rights clearance, exact IW-053 runtime readiness, setup receipt, state-654 ownership/control, capital state-654 control, former-host variable, and unresolved/unfailed compact | `constant:independence_wave_altai_duration.founding_crisis` | Stable Altai ledgers plus Altai route government and state/capital control set the resolved flag | Missing receipt, package/force/anchor/capital invalidation, timeout, or a non-success cancellation invokes existing Altai failure cleanup | Low; one automatic founding mission and package project gate |
| Buryatia IW-052 | Buryatia package, setup receipt, and unresolved/unfailed compact | `constant:independence_wave_buryatia_duration.founding_crisis` | Stable Buryatia ledgers plus route government and state/capital control set the resolved flag | Missing receipt, package/anchor/capital invalidation, timeout, or a non-success cancellation invokes existing Buryatia failure cleanup | Low; one automatic founding mission and package project gate |
| Khakassia IW-054 | Khakassia package, setup receipt, and unresolved/unfailed compact | `constant:independence_wave_khakassia_duration.founding_crisis` | Stable Khakassia ledgers plus route government and state/capital control set the resolved flag | Missing receipt, package/anchor/capital invalidation, timeout, or a non-success cancellation invokes existing Khakassia failure cleanup | Low; one automatic founding mission and package project gate |
| Sakha IW-051 | Sakha package, setup receipt, and unresolved/unfailed compact | `constant:independence_wave_sakha_duration.founding_crisis` | Stable Sakha ledgers plus route government and state/capital control set the resolved flag | Missing receipt, package/anchor/capital invalidation, timeout, or a non-success cancellation invokes existing Sakha failure cleanup | Low; one automatic founding mission and package project gate |
| Udmurtia IW-048 | Udmurtia package, setup receipt, current-generation force package, and unresolved/unfailed compact | `constant:independence_wave_udm_duration.founding_crisis` | Stable Udmurtia ledgers plus route government and state/capital control set the resolved flag | Missing receipt, force-generation/package/anchor/capital invalidation, origin end, timeout, or a non-success cancellation invokes existing Udmurtia failure cleanup | Low; one automatic founding mission and active-project gate |
| Komi IW-050 | Komi package, setup receipt, current-generation force package, and unresolved/unfailed compact | `constant:independence_wave_komi_duration.founding_crisis` | Stable Komi ledgers plus route government and state/capital control set the resolved flag | Missing receipt, force-generation/package/anchor/capital invalidation, origin end, timeout, or a non-success cancellation invokes existing Komi failure cleanup | Low; one automatic founding mission and active-project gate |
| Tatarstan IW-044 | Tatarstan package, setup receipt, and unresolved/unfailed compact | `constant:independence_wave_tatarstan_duration.founding_crisis` | Stable Tatarstan ledgers plus route government and state/capital control set the resolved flag | Existing receipt guard plus package/anchor/capital invalidation, timeout, or a non-success cancellation invokes existing Tatarstan failure cleanup | Low; one automatic founding mission and package project gate |
| Ruthenia IW-038 | Ruthenia package, setup receipt, and unresolved/unfailed compact | `constant:independence_wave_ruthenia_duration.founding_crisis` | Stable Ruthenia ledgers plus route government and state/capital control set the resolved flag | Existing receipt guard plus package/anchor/capital invalidation, timeout, or a non-success cancellation invokes existing Ruthenia failure cleanup | Low; one automatic founding mission and package project gate |

## Cognitive-load and player-facing surface

The patch does not add a decision, mission, category, tab, value, or tooltip, so normal action density and text density are unchanged.

Each category contains one founding mission and a set of phased paid projects; paid projects are gated by package readiness, route flags, completion flags, and a single active-project lock rather than being executable concurrently.

The founding mission is not a player-paid action and exposes no spendable value; the setup receipt is an internal lifecycle requirement whose significance is cancellation of stale foundation state.

The source has no new raw value dump or new player-facing number, and existing category descriptions and project tooltips remain the authoritative explanation of requirements and outcomes.

The categories retain the existing phased project layout; a broader visual or action-density review would be a separate decision-surface task and was not mixed into this one-line lifecycle patch.

## Cost and requirement clarity

The eight founding missions have no direct spendable cost, so their cost-count audit is zero and texticon coverage is not applicable to the mission itself.

The paid project costs and their existing texticon localisation were not changed; no cost string, requirement string, material palette, factory use, manpower, command power, route requirement, admission gate, or balance value was altered.

The source/localisation scan of every `custom_cost_text` key referenced by these eight categories found icon-backed command power, manpower, civilian factory, stability, army experience, infantry equipment, support equipment, and the conditional convoy-or-train transport value, with no literal resource label or fifth simultaneous spendable type in this bounded surface.

The receipt flag is a non-consumed setup requirement, not a fifth hidden spendable cost.

## AI validity and route-lock notes

All eight founding missions retain their existing `ai_will_do = { base = constant:independence_wave_decision_ai.urgent }` and no AI weight or target changed.

Package identity, current-generation force-package, capital, route, origin, and admission/fail-closed gates remain as authored; the new cancellation guards only remove a mission when its own setup receipt is absent.

I ran the required read-only HOI4 probability route on the owned decision source with `mission_ai_will_do` adapter, workspace `mod_chaos_redux_ea3b2d67c2c0`, and refresh enabled.

The probability inspection returned `PROBABILITY_SOURCE_INSPECTED`, source revision `29b9f4988065da535cba9877f28b8e4d996f74f22a2c8521a7263c2c5bde3f59`, source hash `21a73ff35313df30cee31c5a8cb158364235d828c06e32711b5b2d5c7518401f`, 88 candidates, 0 available candidates, 16 required inputs, 0 unresolved inputs, and `poolComplete: false`.

The probability artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d95a3f6997519eccd4cd25db28f7e82dfc737b35e9548308b3008f628861a944/f5fd9b6dbd0883ae76d068a152d0b82ff3e477b21227ad25ec53498a907b9a88/probability-inspect-21a73ff35313.json`.

No probability comparison was run because no weight or probability-bearing expression changed, and no quantitative balance claim is made.

The callable tool inventory did not expose a `chaosx_ai_probability_auditor` subagent route or a `hoi4.decision_inspect`/`hoi4.mission_inspect` route; those are recorded as tooling limitations rather than treated as gameplay evidence.

## Localisation, tooltip, cleanup, and exploit notes

No localisation key changed, and the new receipt guards are internal triggers that do not require a new player-facing string or texticon.

Existing mission timeout and cancellation tooltips remain connected to their package failure helpers; no raw trigger prose was added to the UI.

When setup clears a receipt for a rebuild, the new founding-mission cancellation path removes the stale mission and follows its existing success/failure branch; no reward or cost path was added.

No duplicate mission ID, free reward loop, equipment loop, war-goal loop, or cooldown bypass was introduced; project serialization and package failure cleanup are unchanged.

## Changed source and behavior

Changed source: `common/decisions/006_independence_wave_siberian_decisions.txt`.

Changed identifiers: `independence_wave_altai_hold_mountain_council`, `independence_wave_bya_hold_frontier_council`, `independence_wave_kha_hold_frontier_council`, `independence_wave_yak_hold_arctic_council`, `independence_wave_udm_hold_workshop_congress`, and `independence_wave_komi_hold_northern_council` received their matching setup-receipt absence guard.

Before the patch, those six missions required a receipt for activation but did not cancel on receipt loss; after the patch, receipt loss is an explicit cancellation condition and existing package cleanup runs unchanged.

`independence_wave_tat_hold_river_compact_together` and `independence_wave_rut_hold_mountain_compact_together` already had the matching guards and are byte-for-byte unchanged by this patch.

## Validation

The focused source assertion checked all eight missions for the matching activation receipt, matching cancel absence guard, exactly one prepared setup gate, clear-before-prepared ordering, and restore only inside the prepared gate; all eight assertions passed.

`python -B .tools/audit_event6_allocator.py` passed the Event 006 allocator, package, static-witness, and sequencing checks.

`python -B .tools/audit_event6_flags.py` passed with 102 registered Event 006 tags, 102 complete flag families, and 0 incomplete flag families.

No live HOI4 session, save/load test, or runtime mission cancellation test was run, and none is claimed here.

## Remaining risks and simplifications

The Event 006 implementation remains HOLD / PARTIAL under the current specs; this narrow fix does not admit ALT, BYA, KHA, YAK, UDM, or KOM to any central dispatcher or scenario surface and does not change TAT/RUT admission.

The probability inspection is source evidence only and explicitly incomplete; because no probability changed, no probability comparison or balance conclusion is available.

Runtime engine behavior, live mission cancellation, and save/load persistence remain for the parent or user validation boundary.

No broader design, cost, AI, admission, route, balance, localisation, GUI, or asset changes were made, and no separate plan handoff was needed beyond this audit handoff.
