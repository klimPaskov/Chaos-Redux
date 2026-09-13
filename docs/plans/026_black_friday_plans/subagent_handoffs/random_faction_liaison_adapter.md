# Event 26 Black Friday: Random Faction liaison adapter handoff

Date: 2026-09-02.

Scope: the remaining `random_faction_request_liaison` action in the Random Faction owner surface.

Write boundary: `common/decisions/017_random_faction_decisions.txt`, `common/scripted_effects/017_random_faction_effects.txt`, `common/scripted_triggers/017_random_faction_triggers.txt`, `localisation/english/017_join_faction_l_english.yml`, and this handoff only.

No shared Event 26 framework file, registry, Part 8, catalog, generated file, or unrelated owner file was edited.

## Result

The single logical decision `random_faction_request_liaison` now uses the Event 26 quote, payment, receipt, settlement, refund, and achievement path while an active sale is available.

When Event 26 is inactive, the adapter returns success without touching the Event 26 ledger and the unchanged owner effect performs the ordinary full-price payment: ROOT pays 15 command power and `FROM` pays 60 `support_equipment_1`.

When Event 26 is active, ROOT quotes and pays the command-power component and `FROM` quotes and pays the support-equipment component independently, with one transaction ID in each payer-country scope.

The owner outcome remains gated on both settled receipts and is not applied on an atomic payment, receipt, or settlement failure.

## Severity-sorted issue list

### Resolved high

The liaison action was the remaining Random Faction paid action without Event 26 sale pricing, so its visible values and debit path could not follow the active sale. The decision now routes availability, custom cost, and completion through the liaison-specific adapter without adding a second visible action or changing the owner outcome.

### Open medium

The mandatory production GUI inspection and render found real shared `countrydecisionview` clipping and zero-size diagnostics, including `GUI_ACCIDENTAL_CLIPPING` and `GUI_INVALID_SIZE`. The defects are in the shared decision window and outside this write boundary, so no GUI rewrite was authorized or made.

The mandatory probability audit could inspect the unchanged AI source and resolve the wartime factor, but its named scenarios could not materialize the typed `FROM` target scope. Eligibility, rank, and conditional probability therefore remain unresolved, and no balance conclusion is claimed.

### Open low

HOI4 was not launched, so live debit, receipt, settlement, refund, localisation rendering, and save-state behavior remain live risks.

The shared settlement primitive has no un-settle operation. The adapter refunds every still-recorded receipt exactly once on all expected failure branches, but an unexpected failure after one payer transaction has already settled would require shared-framework support outside this write scope.

## Decision category lifecycle notes

The action remains in `random_faction_bloc_pressure_category` and keeps its existing `target_array = global.random_faction_faction_leaders`, target-root visibility, target leader predicate, newly-aligned phase gate, requested-liaison action limit, and `days_re_enable = constant:random_faction_days.decision_reenable_long`.

The category lifecycle remains phase-gated: the newly aligned phase exposes at most stabilize alignment, request liaison, and quiet opposition; the pressured-neutral phase exposes its existing council, observer, publish, and border-post surfaces; and the faction-leader phase exposes its existing staff, radio, corridor, and commitment surfaces.

No primary action, mission, tab, category, or GUI layout was added.

## Cognitive-load notes

The action displays exactly two spendable values and labels their payer scopes: ROOT pays command power and `[FROM.GetName]` provides support equipment.

The same quote-backed values are used by `random_faction_request_liaison_available_tt`, `random_faction_request_liaison_cost_text`, `random_faction_request_liaison_cost_text_blocked`, and `random_faction_request_liaison_cost_text_tooltip`.

The action has two distinct spendable cost types, below the four-type limit, and introduces no extra counter, tab, or visible mechanic value.

The selected leader, route, action limit, cooldown, and resulting liaison duration remain expressed through the existing decision surface rather than a new explanatory panel.

## Mission quality notes

`random_faction_request_liaison` is an immediate decision owned by ROOT in `random_faction_bloc_pressure_category`; its region/target is the selected current faction leader in `FROM` from `global.random_faction_faction_leaders`.

Its requirements remain the existing newly-aligned visibility, absent `random_faction_requested_liaison` flag, leader relationship, faction membership, and ordinary or active-sale payer affordability checks.

The unchanged owner outcome applies the existing 180-day `random_faction_liaison_mission` timed idea and `random_faction_requested_liaison` flag, improves relations, changes pressure and resilience, and schedules the existing cleanup.

There is no separate success or failure mission branch for this immediate action; expiry and cleanup remain owned by the existing liaison implementation.

The 180-day action flag and existing target checks prevent duplicate liaison activation, and no new duplicate mission instance is introduced.

## Cost and requirement clarity

| Payer | Ordinary payable value | Active-sale quote | Framework kind and family | Owner component id | Display icon |
| --- | --- | --- | --- | --- | --- |
| ROOT | `constant:random_faction_decision_cost.command_power_low` = 15 | `black_friday_random_faction_liaison_command_power_cost` | `command_power` / command power | `@random_faction_request_liaison_root_component_id` = 1701 | `£command_power` |
| FROM | `constant:random_faction_decision_cost.support_equipment_low` = 60 | `black_friday_random_faction_liaison_support_equipment_cost` | `support_equipment_1` / equipment | `@random_faction_request_liaison_leader_component_id` = 1702 | `£support_equipment_text_icon` |

The two dedicated owner component IDs are intentionally outside the current shared owner-component range and are used once per payer scope.

The effect-side quote calls `universal_cost_quote_integer` with the Event 26 source and default rounding quantum, which performs deterministic upward rounding before payment.

The trigger-side display and affordability bridge uses the same Event 26 source composition, ordinary constants, family masks, and default quantum.

Both payers are preflighted before any debit, and `universal_cost_pay_component` rechecks the payer immediately before each native debit.

The cost strings are concise, icon-first, and contain no literal resource names or raw 15/60 values.

## AI validity and route-lock notes

The existing `ai_will_do` block at `common/decisions/017_random_faction_decisions.txt:97` is unchanged: base `constant:random_faction_ai_weight.medium`, strong weighting for matching ideology and wartime, preferred weighting for positive relations and adjacency.

The route lock remains `random_faction_is_current_faction_leader_for_root`, which requires an allowed current faction leader in the same faction as ROOT.

The required read-only `chaosx_ai_probability_auditor` was agent `01a06313-6bec-71d1-ae6c-7aa48388ce83`.

Its source-inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42cb98fcd05a206b2d3ae8a5ad56949352bdf6b84882c4c36f7611253c28fc78/b7ae3232735822d89aa7d37e38bb570b8b6b44f2bf52c3f63d7bea3ea16851b4/probability-inspect-864b9ada4bc8.json`.

Its scenario evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07203d664f5fb655ca1235b11d157f9ce78eca6e43436b34b13747fd57070a4f/cf7dbf47b0dc996ceb6937e28912db0ec98b74ad5618614ae547f58204348894/probability-06b330f50d199f74a85d496d.json`.

The auditor found no AI change warranted, skipped sweep and compare because the AI surface was unchanged, and made no live selection-probability claim.

## Localisation and tooltip coverage

`localisation/english/017_join_faction_l_english.yml:88` contains the dynamic availability text, and lines 109-111 contain the dynamic normal, blocked, and tooltip cost strings.

All four strings use the current command-power and support-equipment quote variables, and all spendable values use the correct texticons.

The file remains UTF-8 with BOM.

The existing `random_faction_request_liaison_tt` outcome text was preserved because it describes the unchanged effect rather than a static cost.

## Cleanup and exploit-risk notes

The active adapter clears its payer-scoped scratch state at entry and exit, clears the leader payment marker before attempting payment, and leaves the owner action marker unset unless both receipts settle.

Each payer receives one allocated transaction ID, one recorded component with the dedicated owner component ID, and one settlement attempt.

If ROOT payment succeeds but the leader payment or receipt fails, the recorded ROOT transaction is refunded and the owner action is not applied.

If either settlement path fails before the owner action succeeds, every still-recorded payer transaction is sent through the shared idempotent refund helper; a component credited directly after a record failure is not refunded a second time.

The achievement is recorded once after both settlements, using the ROOT command-power transaction, command-power family, ordinary cost, and actual paid quoted amount.

The unchanged owner effect skips native payment only when the matching active-sale payer marker was set, preventing duplicate native debit after adapter success. Inactive play leaves those markers unset and follows the original native payment helpers.

No daily or weekly world scan, free-unit loop, equipment farm, war-goal loop, core loop, cooldown bypass, or second visible action was introduced.

## Changed files and identifiers

- `common/decisions/017_random_faction_decisions.txt:61` keeps the single liaison decision and wires `random_faction_black_friday_can_pay_request_liaison_cost`, `random_faction_black_friday_pay_request_liaison`, and completion gating.

- `common/scripted_triggers/017_random_faction_triggers.txt:1079` adds `random_faction_black_friday_can_pay_request_liaison_cost` with inactive ordinary-trigger fallback and active two-payer quote/affordability display values.

- `common/scripted_effects/017_random_faction_effects.txt:7-8` declares owner-local component IDs 1701 and 1702.

- `common/scripted_effects/017_random_faction_effects.txt:2072-2329` adds the liaison state-clear, quote, payer payment/receipt, settlement/refund, and owner-payment orchestration helpers.

- `common/scripted_effects/017_random_faction_effects.txt:2332` preserves the original `random_faction_decision_request_liaison` outcome and gates only its native payment calls when the matching active-sale receipts succeeded.

- `localisation/english/017_join_faction_l_english.yml:88,109-111` updates the four liaison cost/availability surfaces.

## Validation and skipped validation

Bounded source checks completed before this handoff:

- Clausewitz brace-depth audit returned zero for all three touched script files.

- The touched decision, effect, and trigger files contained no literal unsupported `>=` or `<=` operators.

- Each new liaison helper had exactly one definition.

- All four liaison localisation keys were present, each referenced both dynamic quote variables, and no liaison cost string retained literal 15 or 60.

- The localisation file retained its UTF-8 BOM.

Read-only GUI evidence used workspace `mod_chaos_redux_ea3b2d67c2c0`, scenario `event026_random_faction_decision_category_current`, and window `countrydecisionview`.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/859053891a6a13689715a1c45a84c3b2084084af3f2374a32417f3882f324f03/b64db9575e62f0a2d123ca2d28d39f30b84eefc574410fadc85393e566ae9467/gui-inspect.344bc60573fcaf59.json`.

The production render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf551d536d5f323e23809df0f5530c6e66fe7983b7cd75e14d4bec5fd0e44e19/ef564788bbee6ef7e317b9479c95dda8a5f08468ad3c40ec674bcd1088af498e/countrydecisionview-full.svg`.

The render showed no visible-overlap blocker but did show the shared clipping, invalid-size, and unsupported-property diagnostics listed above; no unrelated GUI file was changed.

Skipped meaningful validation: HOI4 live execution, save-state testing, and manual refund/settlement failure injection were not run because this bounded task does not launch the game and the shared framework is outside the write set.

No universal Event 26 coverage claim is made.

## Parent follow-up and remaining scope

Parent integration completed: the shared Event 26 registry records component IDs 1701 and 1702, current documentation records 104 bounded components and ten adapted Random Faction actions, and the earlier static language in `random_faction_adapter.md` is marked superseded.

Those shared files remained outside this handoff's write boundary and were reconciled by the parent after source review.

No simplification was made within the liaison implementation scope; live validation and universal coverage remain explicitly unclaimed.

Plan handoff path: `docs/plans/026_black_friday_plans/subagent_handoffs/random_faction_liaison_adapter.md`.
