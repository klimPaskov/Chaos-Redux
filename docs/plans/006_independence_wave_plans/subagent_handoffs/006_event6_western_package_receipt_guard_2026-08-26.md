# Event 006 Western package founding-mission receipt guard

Date: 2026-08-26.

Owner: `/root/event6_decision_surface_scan`.

Status: bounded source repair complete; Event 006 remains HOLD / PARTIAL and no live-game, save/load, or runtime completion claim is made.

## Scope and verdict

This tranche audited the three founding missions in the consolidated Western registry `common/decisions/006_independence_wave_western_decisions.txt` for symmetry between automatic activation and setup-receipt cancellation.

The affected missions are Brittany IW-004, Catalonia IW-014, and Iceland IW-012.

Each mission already required its package setup-complete receipt in `activation`, while its `cancel_trigger` omitted the matching receipt-absence predicate.

The package setup adapters explicitly clear each receipt before rebuilding the package and restore it only after the prepared-package proof succeeds, so an active mission could outlive an invalid or retried setup generation.

The repair adds one existing-style `NOT = { has_country_flag = <same_setup_receipt> }` clause to each mission's cancellation `OR` block.

No cost, AI weight, route, admission, balance, localisation, scripted GUI, or mission outcome design was changed.

## Severity-sorted issue list

1. High, fixed: `independence_wave_bri_hold_breton_settlement_together` required `independence_wave_iw_004_setup_complete` for activation but did not cancel when that receipt was absent.

2. High, fixed: `independence_wave_cat_hold_industrial_compact_together` required `independence_wave_iw_014_setup_complete` for activation but did not cancel when that receipt was absent.

3. High, fixed: `independence_wave_ice_hold_the_harbour` required `independence_wave_iw_012_setup_complete` for activation but did not cancel when that receipt was absent.

4. Informational, unresolved outside this tranche: analogous receipt-guard coverage in other package decision registries remains owned by separate package audits and was not batch-edited here.

## Exact source changes

Changed file: `common/decisions/006_independence_wave_western_decisions.txt`.

- `independence_wave_bri_hold_breton_settlement_together.cancel_trigger` at line 28 now tests absence of `independence_wave_iw_004_setup_complete`.
- `independence_wave_cat_hold_industrial_compact_together.cancel_trigger` at line 376 now tests absence of `independence_wave_iw_014_setup_complete`.
- `independence_wave_ice_hold_the_harbour.cancel_trigger` at line 595 now tests absence of `independence_wave_iw_012_setup_complete`.

The setup lifecycle evidence is unchanged in `common/scripted_effects/006_independence_wave_western_package_effects.txt`: Brittany clears the receipt at lines 350-351 and restores it only inside the prepared gate at lines 394-395; Catalonia clears it at lines 778-779 and restores it at lines 816-817; Iceland clears it at lines 1239-1240 and restores it at lines 1287-1288.

The corresponding prepared and complete predicates remain in `common/scripted_triggers/006_independence_wave_western_package_triggers.txt` at lines 85-155, 247-319, and 452-517.

## Before and after behavior

Before the repair, each founding mission could remain active after its setup receipt was cleared because cancellation only tested package identity, stable state, and capital or former-host conditions.

After the repair, receipt loss is an explicit cancellation condition and the existing cancellation effect handles the terminal branch without adding a new failure or cleanup system.

Stable package state still resolves through the existing success branch, while timeout, package loss, capital loss, and non-success receipt-loss cancellation retain their existing failure effects.

The missions remain automatic missions with `available = { always = no }`; no player-paid activation path was introduced.

## Decision-category lifecycle notes

`independence_wave_bri_brittany_category`, `independence_wave_cat_industrial_compact_category`, and `independence_wave_ice_north_atlantic_category` each own one package-specific founding mission and their gated follow-on decisions.

The category and mission activation paths remain package- and setup-receipt-gated, and no category is exposed before the active Event 006 origin contract.

Package cleanup already removes the corresponding mission and clears its setup receipt at `independence_wave_cleanup_iw_004_brittany`, `independence_wave_cleanup_iw_014_catalonia`, and `independence_wave_cleanup_iw_012_ice`.

The repair closes the missing cancellation edge between setup rebuild and package cleanup without changing the category lifecycle or restoring any retired pre-event crisis surface.

## Cognitive-load notes

Visible actions are unchanged: each affected category retains one automatic founding mission and its existing gated project decisions.

Active mission count is unchanged at one package-specific founding mission per affected category, and no concurrent mission or new tab was added.

No player-facing value, meter, threshold, cost, or decision text was added; the setup receipt is an internal lifecycle flag.

Text density is unchanged because no category, mission, project, or localisation prose was edited.

Every visible value touched by this patch has no new display requirement because the only changed state is the internal setup receipt; existing package ledger values and threshold descriptions remain in their current package surfaces.

Static source confirms the affected categories are bounded, but this tranche does not claim a live simultaneous-visible project count for ordinary decision panels.

## Mission quality notes

| Owner and mission | Category / region | Requirement and duration | Success | Failure and duplicate risk |
| --- | --- | --- | --- | --- |
| Brittany IW-004 / `independence_wave_bri_hold_breton_settlement_together` | `independence_wave_bri_brittany_category`, Northern Western Europe, capital state 14 | BRI package, setup receipt, unresolved/unfailed compact, dynamic `independence_wave_brittany_duration.founding_crisis` | Existing stable BRI compact cancellation branch marks the compact crisis resolved | Timeout, package loss, receipt loss, or capital loss use the existing failure path; one automatic mission and terminal flags limit duplicate risk |
| Catalonia IW-014 / `independence_wave_cat_hold_industrial_compact_together` | `independence_wave_cat_industrial_compact_category`, Mediterranean Iberia, capital state 165 | CAT package, setup receipt, unresolved/unfailed compact, dynamic `independence_wave_catalonia_duration.founding_crisis` | Existing stable CAT compact cancellation branch marks the compact crisis resolved | Timeout, package loss, receipt loss, or capital loss use the existing failure path; one automatic mission and terminal flags limit duplicate risk |
| Iceland IW-012 / `independence_wave_ice_hold_the_harbour` | `independence_wave_ice_north_atlantic_category`, Northern Western Europe, capital state 100 | ICE package, setup receipt, unstable harbour state, living former host, dynamic `independence_wave_ice_duration.harbour_crisis` | Existing stable ICE harbour-state cancellation branch marks the crisis resolved | Timeout, package loss, receipt loss, capital loss, or former-host loss use the existing failure path; one automatic mission and terminal flags limit duplicate risk |

## Cost and requirement clarity

The three founding missions have zero spendable cost types because they use `available = { always = no }` and do not define `cost`, `custom_cost_trigger`, or `custom_cost_text`.

The bounded cost-count audit is therefore zero for all three missions, and texticon coverage is not applicable to this internal receipt repair.

Existing paid follow-on decisions and their icon-backed cost strings were not changed.

No requirement was converted into a spendable cost, hidden fifth cost, or literal resource label.

## AI validity and route-lock notes

All three missions retain `ai_will_do = { base = constant:independence_wave_decision_ai.urgent }`.

No AI weight, probability modifier, target, package admission, former-host route, or route lock changed.

The required read-only probability discovery was run after the source repair with adapter `mission_ai_will_do` against `common/decisions/006_independence_wave_western_decisions.txt`.

The result was `PROBABILITY_SOURCE_INSPECTED` with source revision `f8908a70fb1931826bd95c196a47ae8068e8d7425f0da2a4cc5d1a25185558a6`, source hash `5427c3b15b8741f8e4572667d8f22961f6a80ba7d5bbe7ec7196081064360fe0`, 30 discovered candidates, 52 required inputs, zero unresolved inputs, zero available candidates, and `poolComplete: false`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb1e5eb6e74a682174e840348b03f6ad55983c2d94b6fa911ed625a0cce590b3/f1439429ba94bdf1f4f13a3907fb761161eb24cc2ac3d3bb8d8ed39dc9ca8c95/probability-inspect-5427c3b15b87.json`.

No probability comparison was run because this repair changes no weighted surface.

The callable tool inventory exposed no `chaosx_ai_probability_auditor` route, so no detailed auditor or numerical balance claim is made.

## Localisation and tooltip gaps

No player-facing localisation key changed because the added receipt predicates are internal lifecycle guards.

Existing mission names, descriptions, timeout effects, and cancellation effects remain wired to their current localisation keys.

No raw trigger text, cost prose, or missing texticon was introduced.

## GUI evidence and disposition

The two Event 006 decision-owned scripted GUI surfaces were inspected and rendered read-only as required; no GUI rewrite was warranted because the repair is an internal mission lifecycle guard.

Statehood Ledger GUI inspection returned `GUI_INSPECTED` with 48 inspected elements and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6d01766c98b51b0e686fc704fd5d5a473b9738e4088ccb53f1e59e6e96479b5/6fb23e39a08e7a06ff3611e11b9009017930871eec7a069593cd9af018db3c39/gui-inspect.6a9e317fb32a3271.json`.

Statehood Ledger render returned `GUI_RENDERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cf000756ada11a3f72b77c58099ed8eb2f376d67cd52aa69bf75f77a8e2a31f/2ab6e40fdd58391d525474767c2387d3d2f23abe09022ce5070de2de3eac9b35/independence_wave_status_window-full.svg`; the result was truncated by the MCP output limit and is fidelity evidence only.

Formable state-puzzle GUI inspection returned `GUI_INSPECTED` with 93 inspected elements and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41be1cd2f50cd8254e6aec15bc83282739c4b2431d0d25538361187af5557783/5b5d24c2e5b5ddcd16f29c9156e5b6b14d741d132fc056d26ddb35feef918e02/gui-inspect.8942d83da568f9f17.json`.

Formable state-puzzle render returned `GUI_RENDERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f86acb57a7f08f83b7b8ebe592088caf6ffda99ea5648ac21ec9b878eadf1d7/c0e9cba068539066fffe749fe3642cb460edee47c62722a77f3a17a2927ac331/chaosx_independence_wave_formable_state_puzzle_w-full.svg`; the result was truncated by the MCP output limit and is fidelity evidence only.

The GUI matrix source audit passed with five mutually exclusive statehood tabs, four formable frames, and cleanup coverage; no GUI surface was modified.

## Cleanup and exploit-risk notes

The new cancellation guards do not add effects, rewards, stockpiles, war goals, cores, factories, or cooldowns.

Existing cancellation effects continue to mark the package crisis resolved only for stable state and otherwise apply the existing package failure helper.

Existing package cleanup still removes the mission and clears the package receipt, so no stale flag or active-mission path was added.

No free-resource loop, duplicate mission activation, equipment farming path, or cooldown bypass was introduced.

## Validation

The focused source assertions passed for all three mission activation receipts, exactly one matching cancellation receipt guard per mission, timeout/cancellation effects, and setup clear-before-prepared-success restore ordering.

`python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 40 runtime adapters, 32 attested packages, 29 compatible reservation groups, the unchanged 3/4/5/7/10 ladder, and the retired pre-event crisis surface.

`python -B .tools/audit_event6_flags.py --strict` passed with 102 registered and complete Event 006 flag families.

`python -B .tools/audit_event6_gui_matrix.py` passed the Statehood Ledger semantic source matrix.

No live Hearts of Iron IV process, save/load test, ordinary decision-panel render, or runtime mission-cancellation test was run, and none is claimed.

## Remaining risks and simplifications

The probability pool is incomplete and no numerical AI balance conclusion is available; this is expected because no weighted surface changed.

The custom probability-auditor route and live runtime validation remain unavailable in this environment.

Other package-specific founding-mission receipt guards remain a separate audit queue and were not broadened into this Western file repair.

No design simplification, fallback, new visible surface, or accepted mechanic change was introduced.
