# Event 006 decision and mission surface audit handoff

Date: 2026-08-22

Scope: Read-only audit of Event 006 decisions, missions, package costs, category density, tooltips, and probability surfaces against `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`, `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv`, current source, the offline Paradox wiki, and vanilla Hearts of Iron IV documentation and precedents.

Worktree rule: No gameplay, localisation, interface, or scripted-system files were edited by this audit; the only new file is this handoff.

## Executive disposition

The highest-impact remaining accepted-mechanic gap is package cost presentation, specifically the Form 05 maritime charter package. Its custom cost strings are player-facing and still spell out resource names such as `Command Power`, `manpower`, `convoys`, and `civilian factory`, while also using long prose with `and`, `plus`, `requires`, or `assigns`. The source payment and reservation logic is materially aligned with the displayed values and stays within the accepted four conceptual spendable-cost groups, so the smallest safe next patch is localisation-only icon conversion for the affected Form 05 base, tooltip, and blocked keys.

The parent DM-01 automatic cost disclosure patch is present in the current source and is not duplicated here. The DM-01 disclosure correctly explains that payment was reserved by `independence_wave_start_provisional_capital_mission` and retains matching `custom_cost_trigger` and `custom_cost_text` handling in `common/decisions/006_independence_wave_decisions.txt:35-41`.

## Issue list, sorted by severity

### P1: Form 05 custom cost localisation violates icon-first presentation

Affected localisation file: `localisation/english/006_independence_wave_form05_l_english.yml`.

Affected visible identifiers are `independence_wave_form05_delegation_cost`, `independence_wave_form05_shipping_cost`, `independence_wave_form05_opening_cost`, `independence_wave_form05_customs_cost`, `independence_wave_form05_capital_cost`, `independence_wave_form05_shipping_board_cost`, and `independence_wave_form05_customs_clearinghouse_cost` at lines 75-86, plus their `_tooltip` and `_blocked` variants at lines 88-111.

The affected strings expose literal names and prose, for example `independence_wave_form05_opening_cost` says `Commits ... plus ... Command Power, ... manpower, and ... convoys, and assigns ... civilian factory.`

The corresponding decisions are in `common/decisions/006_independence_wave_form05_decisions.txt:43-181` and `:318-537`, so these strings are not dead documentation; they are attached to the active charter actions through `custom_cost_text` and related trigger text.

The package's payment and reservation effects remain coherent: opening and customs use the combined command-power commitment, manpower, convoy-or-train transport commitment, and one civilian-factory assignment; the other actions use the matching subsets. No new spendable type needs to be added or removed to fix the presentation.

Bounded patch safety: safe as a localisation-only patch. Replace the literal labels with the existing texticons `£command_power`, `£manpower_texticon`, `£convoy_texticon`, `£GFX_train_texticon`, and `£civ_factory`, preserving every existing constant, amount, alternative transport meaning, and blocked-state semantics. Use the already icon-first Form 05 defence, proclamation, reopening, coastal-warning, and first-board-reconvening strings as the local style precedent.

### P2: Additional package cost prose remains after Form 05

`localisation/english/006_independence_wave_form01_02_04_l_english.yml:66-68` uses `independence_wave_form0124_administrative_diplomatic_cost`, its `_tooltip`, and `_blocked` variant with literal `Command Power`, `Manpower`, `Convoys`, `Trains`, and `civilian factory` labels.

`localisation/english/006_independence_wave_montenegro_l_english.yml:72-77` uses literal labels in `independence_wave_mnt_cost_administration_light` and `independence_wave_mnt_cost_administration_standard`, including their tooltip and blocked variants, while the strategic variants at lines 78-80 already use icons.

`localisation/english/006_independence_wave_pacific_l_english.yml:173-175` and `:188-240` contains the Form 48 invitation, carrier, and member cost families with literal command power, convoy, fuel, equipment, and factory names in base, tooltip, and blocked strings.

`localisation/english/006_independence_wave_form03_l_english.yml:190-228` has icon-first base and blocked strings, but its `_tooltip` variants still spell out `command power`, `manpower`, `stability`, `trains`, `convoys`, and `civilian factory`. These are lower risk than Form 05 because the primary cost rows already use icons, but they remain inconsistent with the strict icon-first requirement.

Bounded patch safety: safe as follow-up localisation-only work, staged package by package. Do not alter the underlying cost constants or payment effects during this cleanup.

### P2: Category density is a review risk, not a proven simultaneous-action defect

`common/decisions/categories/006_independence_wave_categories.txt:12-93` gates categories by active phase, former-host existence, provisional/recognized status, route flags, regional-power status, and unlock flags.

The core source groups contain more than six potential IDs in several families: security DM-17 through DM-23, host DM-24 through DM-30, patron DM-31 through DM-38, and league/high-chaos combinations including DM-60 through DM-62. The Form 03 package also owns many potential actions in one category.

Those decisions have target, route, phase, cooldown, and active-mission gates, so source ID count does not prove that more than six primary actions are simultaneously visible. The installed HOI4 MCP server has no `hoi4.decision_inspect` route, which prevents an engine-backed simultaneous visibility count in this audit.

Bounded patch safety: do not hide, phase, merge, or remove actions without decision-category engine evidence or an accepted design decision. A category-density pass is recommended after a decision inspection route becomes available.

### P2: Category descriptions still expose raw value rows

`localisation/english/006_independence_wave_decisions_l_english.yml:2-17` exposes multiple ledger values directly in category descriptions. The founding and government categories show the five primary values, while league and high-chaos descriptions add relationship and counter rows.

The dedicated status surface partially addresses this by presenting phase, host/patron/network state, and the five primary values, but raw category rows remain a cognitive-load concern when the player is scanning ordinary decisions.

Bounded patch safety: a concise localisation reduction could be safe, but this is a presentation refinement rather than an emergency gameplay fix. Do not redesign the shared status GUI in this handoff.

### MCP and GUI evidence blockers

The installed MCP tool list exposes no `hoi4.decision_inspect`; this is an exact route blocker, not evidence that source review is equivalent to engine inspection.

The status window GUI was inspected successfully, but its graph is global and diagnostically noisy: 48 inspected elements, 74,055 nodes, 25,331 elements, fidelity counts of 498 modelled, 6 approximated, 65 ignored, 1 missing, 4 unsupported, and 12 unresolved. It reports 75 visible overlaps and truncated global diagnostics, including 1,603 index-symbol collisions and 71 unresolved GUI references. This is not a safe basis for a local rewrite of the shared status surface.

The shared Form 03/formable puzzle GUI was also inspected, with 93 inspected elements, 615 modelled, 15 approximated, 64 ignored, 14 missing, and 15 unresolved. It reports 521 visible overlaps and truncated global diagnostics. It is a shared framework, not a safe local rewrite target for this decision audit.

## Decision category lifecycle notes

The founding and government categories are visible for an active Event 006 country. Recognition and patron categories begin at provisional status, network and league categories require recognized status plus their route unlocks, borders and high-chaos require regional-power status plus explicit unlock flags, and the formables category requires recognized status plus formable discovery. The formables category also attaches the shared `independence_wave_formable_state_puzzle_scripted_gui` at `common/decisions/categories/006_independence_wave_categories.txt:78-85`.

The DM-01 automatic provisional-capital mission is intentionally not normally activatable after the material gate has opened it. It has a reserved-cost disclosure, cancellation on loss of active-country/capital/garrison conditions, a short timeout, one-shot protection, and explicit failure/success ledger effects in `common/decisions/006_independence_wave_decisions.txt:21-80`.

Form 05's charter deadline and institution projects are phase and flag gated. The deadline mission is cancelled or times out when the carrier no longer satisfies the charter state, while institution actions are blocked by the active-mission and integration flags in `common/decisions/006_independence_wave_form05_decisions.txt`.

Form 03 post-charter work is similarly gated by integration progress and active language/state-works projects. The current `independence_wave_form03_reopen_charter_talks` decision includes its existing civilian-factory modifier at `common/decisions/006_independence_wave_form03_decisions.txt:650-658`; no stale factory-gate mismatch was found there.

## Cognitive-load notes

The founding, government, recognition, and network groups each have roughly five or six source actions before target and phase filtering. Security, host, patron, and league families have seven or more potential IDs, but their route and target gates need an engine-visible category count before any visibility change is considered safe.

Form 05 has a bounded active charter surface: during the carrier phase, the deadline mission, three institution articles, seat/charter work, and proclamation are gated so the active primary set stays near the intended limit. Its post-formation projects are likewise gated by institution and ratification state. The category is not a confirmed density failure in source alone.

Form 03 and Form 48 have many potential project/member actions, and their shared package surfaces warrant a later live category-density review. The source does not justify deleting or merging an action in this read-only pass.

Player-facing values have clear names in the status window, but ordinary category descriptions provide raw rows without consistently explaining what threshold, consequence, or next action each value controls. This is a P2 clarity issue after the cost icon pass.

## Mission quality notes

DM-01 owner and category are the active provisional country and founding category; its region is the country capital; its requirement is controlled capital plus the security/garrison gate; its duration is `constant:independence_wave_decision_duration.short`; success is the timeout path that secures the capital and applies positive capacity/security effects; failure is cancellation with relocation, government, and instability penalties; duplicate risk is controlled by the country flags, reserved-cost flag, `fire_only_once`, and active-mission gate.

The DM-02 through DM-05 founding missions are owned by the active country, live in the founding category, and use capital/administrative requirements, founding durations, success effects, timeout penalties, cancellation checks, and matching civilian-factory modifiers. The source map confirms the corresponding DM IDs and duration bands.

Form 05's charter deadline is owned by the carrier country and the formable category, covers the carrier's charter region and member-state obligations, and uses a bounded integration deadline. Success is institution ratification and ledger completion; timeout/failure damages the charter ledger and closes or reopens the package according to existing effects; duplicate risk is constrained by charter flags, active project flags, and the deadline mission lifecycle.

Form 03's ratification and reopening missions are owned by the formable carrier and its package category, require integration thresholds and living autonomous members where specified, use the package's long/integration durations, and have explicit completion, expiry, cancellation, and retry paths. Their repeated-project risk is bounded by `has_active_language_action`, state-works, institution, and charter flags.

The MCP mission probability pool recognized 54 candidates, but the empty fixture made all candidates unavailable and left lifecycle state unresolved. This is a fixture limitation, not a conclusion that the live mission pool is empty.

## Cost and requirement clarity

The core cost palette in `localisation/english/006_independence_wave_decisions_l_english.yml:28-47` is generally icon-first, including command power, manpower, convoy/train alternatives, stability, equipment, and civilian-factory assignments.

Form 05 opening and customs actions use four conceptual spendable groups: command power, manpower, convoy-or-train transport, and civilian-factory assignment. Defence uses manpower, infantry equipment, support equipment, and civilian-factory assignment. Proclamation/reopening use stability, command power, convoy-or-train transport, and civilian-factory assignment. These are within the four-group cap and match the existing scripted payment/modifier structure.

Form 01/02/04 administrative-diplomatic actions use command power, manpower, convoy-or-train transport, and civilian-factory assignment, also within the cap. Form 48 carrier convoy uses command power, convoys, fuel, and civilian factories; carrier procurement uses convoys, infantry equipment, support equipment, and civilian factories; carrier basing uses command power, support equipment, and civilian factories. The problem in these packages is presentation prose, not a fifth hidden spendable type.

The Form 05 and MNT strings fail texticon coverage for displayed spendables because they use literal resource names. The Form 03 base rows have texticons, but several tooltip variants still spell out resource names and should be converted in a later localisation pass.

The offline Decision modding and Effects pages require custom cost disclosure to correspond to an actual cost/payment path. The current source satisfies that contract for the reviewed packages: Form 05 and MNT custom cost strings are paired with scripted payment effects and factory-use modifiers, while DM-01's disclosure is now explicitly tied to its reservation flag.

## AI validity and route-lock notes

The core DM-01 through DM-62 decisions each expose an `ai_will_do` block in `common/decisions/006_independence_wave_decisions.txt`, and package decisions carry their own AI blocks or shared package weights. Target validity, dead-country checks, route gates, and phase flags are present in the reviewed source; no new invalid-target or closed-route defect was established.

The required probability workflow was run read-only. Decision source inspection returned 10 candidates with 0 available, 87 required inputs, and 54 unresolved inputs. Mission source inspection returned 54 candidates with 0 available, 49 required inputs, and 10 unresolved inputs. These results came from an empty/non-live fixture and must not be interpreted as live balance rankings.

Decision probability evaluation returned `PROBABILITY_ANALYZED_PARTIAL` with 10 candidates, 2,941 unresolved entries, 8 diagnostics, and analysis ID `probability-cde6d11510a44025e6983f34`. Mission probability evaluation returned `PROBABILITY_ANALYZED_PARTIAL` with 54 candidates, 517 unresolved entries, 20 diagnostics, and analysis ID `probability-39034c9332d617b69cda8b6a`. No numeric AI rebalance is recommended from these partial empty-fixture results.

## Localisation and tooltip gaps

The Form 05 cost key family at `localisation/english/006_independence_wave_form05_l_english.yml:75-111` is the immediate localisation gap. Form 01/02/04 administrative-diplomatic keys at `localisation/english/006_independence_wave_form01_02_04_l_english.yml:66-68`, MNT administration keys at `localisation/english/006_independence_wave_montenegro_l_english.yml:72-77`, and Form 48 package cost keys at `localisation/english/006_independence_wave_pacific_l_english.yml:173-240` are the next package-local cleanup targets.

Form 03's `_tooltip` keys at `localisation/english/006_independence_wave_form03_l_english.yml:192-228` explain the actions and durations, but should use icons for all spendables instead of literal names. The existing effect/requirement semantics should remain unchanged.

## Cleanup and exploit-risk notes

The reviewed DM and package missions have explicit cancellation, timeout, one-shot, active-flag, and cooldown patterns. DM-01 reservation disclosure does not introduce a second payment path because the comment and `custom_cost_trigger` make the custom row disclosure-only while payment remains in `independence_wave_start_provisional_capital_mission`.

No new free-unit loop, equipment-farming loop, war-goal spam path, core spam path, or cooldown bypass was found in the bounded source audit. The cost localisation issues do not themselves alter payment or cleanup behavior.

The GUI inspection diagnostics are global graph issues and should not be “fixed” by changing the shared status or formable GUI during this decision-surface pass.

## MCP artifact references

Decision probability inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ba26c539ca3e05e751b252b5e3d777fade3c896a9adda6453d52467315bc618/560f522be102978b4e3ced7a982facf3da705222126629945eef47a8c1d575fd/probability-inspect-9450608eb3c7.json`.

Mission probability inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b50c6970929ba4993e7060c99de41a8845a104b4002008b4d91e5879b8fd0a81/9478cedf308f61364936dcc86667dbd4653562d374e17f6fa16cf135a3828150/probability-inspect-9450608eb3c7.json`.

Decision probability evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/835167fd580bebd059596ee090e312b7d669224093a9478193e88cabd3c5ea34/0b6aad4a70d837b32629d692e3ab7a7a0a32c0759800552fe7d39f87abf3942b/probability-cde6d11510a44025e6983f34.json`.

Mission probability evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57a02eefdc0cca0ca71706b6c494d7f74f31c7a5e5c9c96e08bd1beee18ecb51/1dc5003e860da891a0796715156e231da2d19d4c10013ccd3423901ea81824fc/probability-39034c9332d617b69cda8b6a.json`.

Status GUI inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db0f2525b02bef25a61cc17ed8ec3e5ef07d0541cd3e5d76a4cd0aa000f61289/404ab4eb73fbd7bceb5a94fc10032c63261a1d566ce9f5203f1438139a1433d4/gui-inspect.dee9143e5b83c257.json`.

Status GUI render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d245b460614d138ebe4d724b8fbbe4c0c3ae510648ae12c90abf3733e231c13/866248e87cf4346878b806c1ed95e4ff9c4104fe189bb96d7a6e0e34f732adec/independence_wave_status_window-full.svg`.

Shared formable GUI inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9f395fe9634891bdabb95bb3e378adfe63c0d4a97f13dc71caaf138326b7ec2/1c7b8906f662e8e5f9056c959ae72b4d11da88755002e23a8b310b349263b6a9/gui-inspect.c53f898f1fe7e31f.json`.

## Recommended follow-up

1. Apply a localisation-only Form 05 patch to convert the affected base, tooltip, and blocked cost keys to the existing texticons while preserving all constants and payment semantics.

2. Apply the same icon-first cleanup package by package to Form 01/02/04, MNT, Form 48, and Form 03 tooltip variants.

3. Obtain an engine-backed decision-category inspection or an accepted scenario-based visibility review before changing category density, phasing, or action count.

4. Re-run the probability workflow only after a concrete balance/AI patch and stateful scenarios exist; use `probability_compare` with the same named scenarios for any weighted change.

## Validation and skipped validation

Completed: source/spec/map review; required offline wiki and vanilla documentation review; vanilla decision precedents (`CZE.txt` factory-use decision and `AUS.txt` factory-count precedent); decision and mission probability inspect/evaluate; mandatory status and shared formable GUI inspect; status GUI render.

Skipped: `hoi4.decision_inspect` because the installed MCP server does not expose that route; formable GUI render because the first attempt timed out after 180 seconds and the retry returned `ARTIFACT_STORAGE_LIMIT`; probability sweeps/compare because no gameplay patch was made and the available fixture lacks the required lifecycle, country, target, stockpile, and ledger state; live HOI4 playtest because this audit is read-only and live validation belongs to the parent/user workflow.

## Changed files and remaining blockers

Changed files: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_decision_surface_audit_2026-08-22.md` only.

No gameplay or localisation patch was applied in this audit, so there is no before/after runtime behavior change to validate.

Remaining blockers are the unavailable decision-inspection MCP route, partial empty-fixture probability state, formable GUI render storage/timeout failure, and the need for parent review before any category-density redesign. The Form 05 icon-only localisation patch is bounded and safe for the parent to apply next.
