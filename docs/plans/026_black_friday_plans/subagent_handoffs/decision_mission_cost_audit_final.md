# Event 26 Black Friday — final decision and mission cost audit

Status: audit handoff only. This document does not implement owner adapters, change gameplay, or grant Event 26 completion approval.

## Snapshot and changed files

The audit was frozen against source manifest `af01a8b2c79da8a20ef887e08b0cde828bef86bc41a0d3a4f6ced4f70dec8c78`, Git `HEAD` `76ac44822b70bc4f19a7e2fe82321ae596544a99`, and audit time `2026-08-29T23:01:53Z` (`2026-08-30` in the repository timezone). The manifest covers the 117 physical `common/decisions/*.txt` files present at that time, including current untracked files; category-definition files under `common/decisions/categories/` were inspected but are not action rows.

Changed files in this handoff: documentation only — `docs/plans/026_black_friday_plans/subagent_handoffs/decision_mission_cost_audit_final.md`.

No gameplay file, XLSX, generated export, or live game state was changed. HOI4 was not launched and no logs were searched.

## Executive disposition

Event 26 has a real source registration and expiry path, but its shared universal-cost framework has no consumer call sites in the decision surface. The current `rg` search found zero owner calls to `universal_cost_quote_integer`, `universal_cost_check_quote_affordable`, `universal_cost_pay_component`, `universal_cost_record_transaction`, `universal_cost_settle_transaction`, `universal_cost_refund_transaction`, or `universal_cost_mark_component_refunded` under `common/decisions`. Event 26 only registers and clears the source through `common/scripted_effects/026_black_friday_effects.txt:556` and `:667`.

This leaves all owner-controlled custom costs unregistered at the transaction boundary and leaves mixed native/custom rows at risk of paying twice. The source-level implementation is therefore incomplete even where the native sale ideas and modifiers exist.

### Counts

The exhaustive decision scan produced 3,992 decision-shaped action blocks and 3,054 cost/commitment registry rows. Of those rows, 3,033 are actual purchase or commitment candidates and 21 are retained as explicit not-a-purchase evidence rows.

| Surface signal | Count | Meaning |
| --- | ---: | --- |
| Non-zero native `cost =` | 1,018 | Engine political-power cost fields; 240 additional native declarations are zero/free sentinels. |
| `custom_cost_trigger` | 2,158 | Owner affordability disclosures; these do not debit resources. |
| `custom_cost_text` | 2,159 | Owner display disclosures; one row has display without a matching custom affordability trigger. |
| Selectable missions | 46 | Player-click mission entries; 19 have no native/custom/factory/debit evidence and are classified `D/NA`. |
| Factory commitment fields | 602 | `civilian_factory_use`, `military_factory_use`, or `dockyard_use` signals. |
| Explicit direct debit signals | 426 | Conservative source scan including direct XP/resource/equipment effect syntax, stockpile removal, subtractors, and negative resource effects; owner helpers can hide further components. |
| Native/custom overlap | 171 | Highest double-payment risk: engine `cost` plus owner custom debit in one action. |
| Custom/factory overlap | 404 | Mixed logical transactions requiring an owner adapter plus an engine-inaccessible factory component. |
| Mission/factory overlap | 12 | Mission commitments with factory reservation. |
| Custom text without trigger | 1 | `black_plague_rat_king_execute_terminal_takeover` at `common/decisions/020_black_plague_rat_decisions.txt:916-927`. |
| Custom trigger without text | 0 | No trigger-only mismatch found in the frozen snapshot. |

The row appendix below is the registry. Its `N`, `C`, `M`, `F`, and `P` class letters mean native non-zero cost, custom cost, selectable mission, factory commitment, and conservative explicit direct debit respectively. The appendix includes every union row, including all 21 `D/NA` evidence rows, rather than collapsing repeated owner actions into file-level counts. Current pair intersections are `N+P=108`, `C+N=171`, `C+M=26`, `C+F=404`, `C+P=315`, `M+N=1`, `M+P=11`, `F+N=187`, `F+M=12`, and `F+P=37`; higher-order combinations are listed by exact class in the appendix.

## Severity-sorted issues

### Critical

1. Shared framework integration is absent. `common/scripted_effects/chaosx_universal_cost_effects.txt:389`, `:561`, `:582`, `:922`, `:1160`, and `:1243` define quote, affordability, payment, receipt, settlement, and refund helpers, but there are no calls from the 3,054 current registry rows. Event 26 cannot discount owner-defined PP, CP, manpower, fuel, equipment, XP, factory, or custom-currency actions until each owner wires one logical quote/payment/receipt path.
2. The 171 `N+C` rows can double-charge. Vanilla will process the native `cost` while the owner `complete_effect` processes the custom debit unless the owner converts the row to one adapter transaction or removes the duplicate native component. Every `N+C`, `N+C+F`, `N+C+P`, and `N+C+M` row is blocked pending explicit owner reconciliation.
3. Factory commitments are not a generic stockpile component. The 602 factory signals are engine `civilian_factory_use`, `military_factory_use`, or `dockyard_use` modifiers. The shared payment helper supports only nine native resource kinds and has no factory reservation/refund branch. These rows need exact `D-CF` evidence and an owner adapter that preserves reservation, cancellation, timeout, and save/load behavior.
4. The existing registry is stale against this snapshot. `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md:22-24` records 2,067/2,068 custom fields, while this scan finds 2,158/2,159. Its `BF-NAT-001` row at `:34` says `covered_native`, but the required decision inspection route is unavailable and no owner transaction calls exist. Do not use that status as final coverage proof.

### High

1. `black_plague_rat_king_execute_terminal_takeover` has `custom_cost_text` at `common/decisions/020_black_plague_rat_decisions.txt:923` but no `custom_cost_trigger` before `complete_effect` at `:925`. The display is a requirement sentence, not an affordability check; the owner must expose and revalidate its actual resource/currency debit.
2. The framework's native affordability/payment branches cover Political Power, Command Power, Manpower, Fuel, Infantry Equipment, Support Equipment, Motorized Equipment 1, Train Equipment, and Convoy 1 only. It has no generic branch for other equipment IDs, custom ledgers, factory commitments, laws, advisors, operations, technology/design actions, or special projects. Unsupported components require owner credit/refund adapters and exact actual-paid receipts.
3. Custom-cost displays are not automatically engine-aware. Among 1,212 unique `custom_cost_text` keys, 1,035 resolve in the scanned localisation/scripted-localisation index, 177 do not resolve in that source index, and only 913 resolved entries contain a literal `£` texticon marker. This is a source heuristic, not renderer evidence; unresolved and no-icon keys must be closed by the localisation owner. Examples include literal resource prose at `localisation/english/012_africa_elephant_operations_l_english.yml:11`, `localisation/english/012_africa_world_sponsorship_l_english.yml:94`, and the seven-component prose string at `localisation/english/cbrn_occupation_l_english.yml:19`.
4. AI affordability is owner-defined and incomplete for discounted custom costs. Only 185 current decision rows declare `ai_hint_pp_cost`, and custom rows otherwise do not teach vanilla AI its PP component. Existing `ai_will_do` blocks still need to call the same affordability gate as the player path and, where weights change, require a same-scenario probability comparison.

### Medium

1. The 46 selectable missions have player-click `complete_effect` entry points but varied timeout, cancellation, cooldown, reserve, and duplicate guards. The mission table records each exact lifecycle field. A mission with a custom or factory commitment must distinguish pre-reservation from click-time payment and must refund only actual paid components.
2. The 19 selectable mission rows with no cost/debit/factory evidence are not purchases. They are retained as `D/NA` rows so they cannot be silently omitted from the registry. The four Soviet objective missions with direct resource effects are purchase/commitment rows even though they are non-selectable and are separately called out in the appendix.
3. The source tree is dirty and contains staged deletions plus current untracked decision files. This audit intentionally scans the physical current worktree, not only `HEAD`; the parent must rerun the manifest and registry after any further owner or deletion change.

## Registry strategy and status contract

| Strategy | Use in this audit | Current status |
| --- | --- | --- |
| A | Native dynamic composition through a documented engine country/unit-leader cost modifier. | `blocked_pending_evidence` for row-level engine proof because no callable decision-inspection route exists. The native Event26 idea/dynamic-modifier sources are still the recommended A path. |
| B | One owner adapter calls shared quote, inclusive affordability, actual payment, receipt, and settle/refund for one logical transaction. | `blocked_pending_evidence` for all custom rows and mixed native/custom rows; no consumer call sites exist. |
| C | Static normal/50%/75% variants when a native dynamic route is impossible and the owner accepts explicit variants. | No current rows assigned; this is a fallback requiring parent design approval, not an invented implementation. |
| D-CF | Exact engine-inaccessible factory/dockyard commitment component, paired with B for mixed rows. | `blocked_pending_evidence`; source field evidence is included in each F row and the engine boundary is documented. |
| D/NA | Exact evidence that the action is not a voluntary purchase: no cost/custom/factory/debit, a navigation-only ledger control, or an irreversible failure penalty. | `not_a_purchase_cost`; these rows remain in the audit so the parent can verify exclusion. |

For every positive component, the owner must retain a positive quantum and use the shared upward quote formula. Requirements, reserve floors, target validity, cooldowns, laws, technologies, routes, construction time, upkeep, casualties, and outcome penalties are not discounted costs and must remain separate from the spendable row.

## Required owner adapter behavior

The parent implementation should close the rows in family/owner batches, not by replacing decisions with generic shop buttons. Each owner adapter must:

1. Compute the ordinary current payable component immediately before display and again immediately before payment.
2. Apply the Event26 ratio to each spendable component, round positive values upward to the owner quantum, and show exactly the same quoted value that is paid.
3. Preflight every component, including reserve floors and target validity, before paying any component.
4. Debit one logical transaction with one primary achievement family and distinct component IDs for multi-resource actions.
5. Record actual paid amounts, settle after the non-refundable window, and refund actual paid amounts on cancellation/expiry where the owner promises refund. Unsupported engine components must be externally credited before `universal_cost_mark_component_refunded`.
6. Keep `available`, `activation`, target checks, duplicate guards, cooldowns, AI affordability, and route locks unchanged except for the spendable quote.
7. Revalidate at click/activation time. A `custom_cost_text` or custom trigger alone is disclosure, not payment or framework registration.

## Lifecycle, cognitive-load, and mission-quality findings

The category and mission scan found many large event packages with repeated custom actions. The current source should be reviewed against the six-visible-primary-action maximum and the normal one-to-three active-mission budget in the decisions/missions skill. Category wrapper names are included in every row where the decision is nested; top-level mission definitions have `cat=-` because they are intentionally activated from owner decisions rather than assigned to a category.

The main cognitive-load risks are: raw dynamic resource lists without icon-first localisation, cost values that are hidden inside owner helpers, mixed spendable components and non-consumed requirements in one prose string, and identical-looking mission rows whose consequence is only visible in a long timeout block. The row appendix makes every value's source visible, but it does not make a bad player-facing string acceptable.

The 46 selectable-mission rows and 14 additional non-selectable factory-commitment missions are listed in the mission appendix after the file summary. For each, the table records owner/category, target/region cues, activation, click requirement, duration, selection/complete hook, timeout success/failure hook, cancellation, cooldown, and duplicate guard evidence. `available` is the player affordability/requirement gate; `custom_cost_trigger` is the custom-cost disclosure gate; `complete_effect` is the click/activation payment hook; `timeout_effect`, `cancel_effect`, and `remove_effect` are distinct lifecycle paths.

## Exact D and not-a-purchase evidence

* Factory D evidence: `common/decisions/006_independence_wave_decisions.txt:103` and the other F rows use `modifier = { civilian_factory_use = ... }`; the equivalent military/dockyard fields are recorded where found. Vanilla `documentation/modifiers_documentation.md:2202` documents `civilian_factory_use`, while `common/scripted_effects/chaosx_universal_cost_effects.md` states that factory commitments require an owner adapter. This is an engine-boundary classification, not permission to ignore factory reservations.
* Navigation-only ledger: `common/decisions/006_independence_wave_decisions.txt:938-973` defines `independence_wave_scenario_ledger_previous` with `cost = 0`, a `complete_effect` that only moves an index, and `ai_will_do = { base = 0 }`. It is `D/NA`.
* Irreversible failure penalty: `common/decisions/049_mass_panic_decisions.txt:339-384` has no native/custom cost and applies `add_political_power = -100` and `add_war_support = -1.00` at `:367-368` while resolving a doomsday failure. This is a penalty, not a voluntary purchase.
* No-cost selectable missions: `common/decisions/006_independence_wave_form03_decisions.txt:587-613` and the 18 Event39 rows in `common/decisions/039_murder_mystery_decisions.txt` have `selectable_mission = yes` but no native cost, custom cost, factory modifier, or explicit debit in the owning block. They are retained as `D/NA`; their PP threshold in `available` is a non-consumed requirement.
* Direct resource mission commitments: the four Soviet objective missions at `common/decisions/005_soviet_collapse_decisions.txt:479-513`, `:515-548`, `:998-1035`, and `:1037-1079` contain direct XP/manpower/CP/fuel/equipment effects and are actual commitment rows despite `selectable_mission = no`. They remain blocked pending an owner adapter.

## Source and reference evidence

Required offline wiki references were read from `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Idea modding`, and `AI modding`. Decision semantics used here are at `Decision modding:266-325` for `complete_effect`, custom-cost non-payment, cooldowns, and delayed removal, and `:451-460` for mission timeout, `selectable_mission`, activation, and the fact that `visible` does nothing in missions.

Installed Vanilla documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, `documentation/script_math_functions.md`, and the script-constant documentation. Relevant installed lines include decision refresh/target semantics in `_documentation.md:3-45`, native cost modifiers in `modifiers_documentation.md:608-624`, `:1280-1376`, `:2202`, `:4243`, `:4408`, and `:4557`, payment effects in `effects_documentation.md:901-915`, `:1252-1290`, `:1388-1404`, `:1468-1490`, `:1854-1885`, and purchase-contract support at `:3219-3255`, and resource/mission triggers in `triggers_documentation.md:2205-2218`, `:3022-3032`, `:3835-3965`, `:4121-4135`, and `:4547-4565`.

Vanilla decision/mission precedents were inspected in `common/decisions/AFG.txt`, `_generic_decisions.txt`, `_exiled_governments_decisions.txt`, `TOA_shared_decisions.txt`, `WTT_politcal_power_struggle_decisions.txt`, `stability_war_support.txt`, `resource_prospecting.txt`, `MTG_congress.txt`, `aat_mio_decisions.txt`, and the installed `AST.txt`. The supported build is installed `1.19.2.0` (`Operation Postern v1.19.2.0.a729`, Steam build `23969257`).

## MCP evidence and limitations

The callable tool registry exposes `hoi4_probability_inspect` but no `hoi4.decision_inspect` or `chaosx_ai_probability_auditor` route. The broad probability source probe with `{source:{path:"common/decisions"}}` returned `PROBABILITY_SOURCE_NOT_FOUND` for that directory. Two read-only source inspections were still run:

* Decision adapter `decision_ai_will_do` on `common/decisions/005_soviet_collapse_decisions.txt` returned `PROBABILITY_SOURCE_INSPECTED`, `candidates=211`, `availableCandidates=0`, `requiredInputs=51`, `unresolved=0`, `poolComplete=false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f2d15d50ff6a97513578248d1785b4265b11610a990c9ccca20a098af75670f/3e53db8e31a3dbf49286303ecd0403d7750db38249188a62df6db485cd69bff7/probability-inspect-72ed3330bb09.json`.
* Mission adapter `mission_ai_will_do` on `common/decisions/031_random_terror_missions.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, `candidates=0`, and `requiredInputs=0`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8177ec04b980edaa2225bd8ae7999c94cff5f92d0632eb96b15ec2dbd0470acb/efd9f7e63f5590ef4cae1296a8782004ca4bd3ccd76b70e5eca654d683b8b564/probability-inspect-8c85d2b3e0b8.json`.

No `probability_compare` was run because this audit applied no AI patch and there is no stable before/after owner adapter to compare. No decision-inspect or production GUI evidence is claimed. Event 26 uses existing event log/status and popup presentation and introduces no dedicated scripted GUI, so the mandatory decision-owned GUI inspect/render route is not applicable to this audit. MCP output does not replace source, wiki, vanilla documentation, or parent review.

## Cleanup and exploit-risk notes

The current Event26 lifecycle is source-wired: registration at activation, source clear at expiry, and native idea/dynamic-modifier cleanup in `common/scripted_effects/026_black_friday_effects.txt:553-560`, `:622-682`, and `:467-527`; bounded daily pulses are called from `common/on_actions/chaosx_on_actions_chaos_meter.txt:27`, `:44`, and `:62`. The missing part is the owner transaction lifecycle, not the source registry itself.

Until adapters are installed, the primary risks are double payment on N+C rows, undiscounted owner costs beside discounted native costs, cancellation/timeout consuming resources without a receipt refund, partial payment of multi-resource actions, AI selecting actions it cannot afford, and hidden fifth-or-later costs in prose. Factory reservations also risk being treated as zero-cost because the native `cost` field is zero. The shared framework has no atomic rollback across unrelated effects and no reserve-floor policy; both remain owner responsibilities.

## File summary

The following table is generated from the same frozen manifest. `U` is the number of appendix rows for that file; `NA` is the explicit not-a-purchase subset. The complete owner-level and identifier-level inventory follows in the row appendix.

| Owner file | N | C | M | F | P | U | NA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
<!-- FILE_SUMMARY_ROWS -->

## Exhaustive decision and selectable-mission registry

`ord` is the ordinary source, `aff` the player/AI affordability source, `pay` the payment/commitment effect, `disp` the display source, `life` exact lifecycle lines, `ai` weight/hint, `res` reserve-floor cue, `fam` source-inferred family/component types, `strat` the recommended A/B/C/D route, `status` the current disposition, and `evidence` the reason for an engine boundary or exclusion. `fam` and component counts are source cues where the owner helper is opaque; they are not claims that the shared framework has already wired that helper.

| # | Class | Exact source and owner | Category | Ordinary cost source | Affordability source | Payment / commitment effect | Display source | Lifecycle / refund / cooldown | AI / reserve | Family / component types | Strategy | Status | Evidence |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
<!-- INVENTORY_ROWS -->

## Selectable and commitment-mission quality table

This table covers all 46 `selectable_mission = yes` rows and the 14 non-selectable mission rows that carry a factory commitment. `complete` is the click/activation hook; `timeout` is the deadline hook; cancellation and duplicate evidence are listed separately.

| # | Kind | Exact source and owner/category | Target / region cue | Activation | Requirement / affordability | Duration | Complete / selection hook | Timeout success/failure hook | Cancel / duplicate / cooldown | Cost / commitment |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
<!-- MISSION_ROWS -->

## Remaining blockers and handoff actions

* The parent must wire owner adapters for the 2,098 custom rows, including the 171 native/custom overlaps, and update the authoritative registry after each batch.
* The parent must decide whether the 1,024 native decision rows have sufficient engine evidence to claim A/`covered_native`; this handoff leaves them blocked because the decision inspection route is unavailable.
* The parent must close all 602 factory components with exact reservation/refund behavior and retain the D-CF evidence.
* The parent must resolve the one custom display/trigger mismatch and the 177 unresolved or no-texticon localisation keys through the localisation owner.
* The parent must run named-scenario probability comparisons for any AI/weight patch. This audit does not claim such a comparison.
* The parent must rerun the source manifest and this registry after concurrent worktree changes; the scan includes current physical untracked files and therefore cannot be frozen by the Git commit alone.

No gameplay implementation, XLSX update, generated-file update, or live validation was performed by this subagent. This is intentional scope compliance, not a completion claim.
