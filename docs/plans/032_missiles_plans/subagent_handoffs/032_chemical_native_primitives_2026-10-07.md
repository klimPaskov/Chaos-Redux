# Event 032 chemical native primitives, 2026-10-07

Disposition: `implemented` for this primitive layer, with parent integration and runtime validation pending.
Acceptance basis: the parent explicitly assigned these three helpers, accepted shared CBRN ownership, the four prepared-air concrete models, measured native debit/credit, and caller-owned temporary outputs.
The architecture input is [032_chemical_escrow_api_architecture_2026-10-07.md](032_chemical_escrow_api_architecture_2026-10-07.md).
Its proposed receipt system is outside this patch.

## Changed files and ownership

- New `common\scripted_effects\cbrn_payload_reservation_native_effects.txt`, containing only the three helpers below and their API comments.
- New handoff `docs\plans\032_missiles_plans\subagent_handoffs\032_chemical_native_primitives_2026-10-07.md`.

Both files were absent at discovery and immediately before creation.
The three helper definitions were absent from `common\scripted_effects` before creation and occur only in the new file on the final definition scan.
Source SHA-256: `A583E9E786593678A1A59ED32B97A90A0D9C3E6241A7CA04084D9A0C459A4ADD`.
Existing gameplay, documentation, tests, constants, equipment definitions, events, decisions, focuses, GUI and assets were not edited.
No Git/index operations, further agents, game launch or log search were performed.

## API map

All helpers run in the actual payer's COUNTRY scope and use `helper = yes`, with no argument block.
They preserve the native calling scope rather than redirecting to ROOT.

| Helper | Required caller inputs | Caller-owned outputs | Side effects and direct consumers |
| --- | --- | --- | --- |
| `cbrn_payload_resolve_air_model` | `cbrn_action_agent`, `cbrn_action_delivery_route` | `cbrn_payload_native_model`, `cbrn_payload_native_model_matched` | Derives class through `cbrn_chemical_air_raid_set_agent_class_internal` after initializing its nested class scratch. No stock mutation. Parent receipt reservation and model validation are intended consumers. |
| `cbrn_payload_measure_model_debit` | `cbrn_payload_native_model`, `cbrn_payload_native_requested` | `cbrn_payload_native_before`, `cbrn_payload_native_after`, `cbrn_payload_native_observed`, `cbrn_payload_native_valid` | Calls `cbrn_state_escrow_measure_model_debit = yes` once for a supported token and forwards its exact observations. Parent receipt reservation owns payment acceptance and recovery. |
| `cbrn_payload_measure_model_credit` | Same model and request inputs, with an explicit authorized held refund | Same four measurement outputs | Calls `cbrn_state_escrow_measure_model_credit = yes` once for a supported token. Parent verified original-payer refund owns authorization, once-only settlement and remainder. |

Resolver output storage must exist in its caller before invocation, with model initialized to `constant:cbrn_math.zero` and matched initialized to `constant:cbrn_proof.missing`.
The resolver derives class afresh from agent, so a supplied mismatched class cannot choose a model.
Supported routes are exactly `constant:cbrn_delivery_route.chemical_air_raid` and `.strategic_chemical_raid`.
Unsupported routes or an agent deriving no supported class return zero model and missing proof.
Model proof establishes a mapping only, and does not establish unlock, profile, policy, target eligibility or payment.

| Derived class | Concrete token | Exact agents supplied by the existing resolver |
| --- | --- | --- |
| `choking` | `token:choking_chemical_air_payload_lot_1` | Chlorine, Phosgene |
| `blister` | `token:blister_chemical_air_payload_lot_1` | Mustard, Lewisite |
| `nerve` | `token:nerve_chemical_air_payload_lot_1` | Tabun, Sarin, Soman |
| `incapacitating` | `token:incapacitating_chemical_air_payload_lot_1` | Malodor, Behavioral Agent |

Each measurement caller must create all four public outputs with `constant:cbrn_math.zero` before invoking a wrapper.
The model and request are required caller-created inputs, with no inferred request default.
The public request remains original and the model remains unchanged.
Debit bounds only the nested request to available nonnegative model stock.
`valid = constant:cbrn_math.one` means a nonnegative stock/delta observation within the nested request, including valid zero or partial payment.
Full reservation additionally requires observed quantity equal to the original request under the parent's whole-count contract.
Credit observes after minus before, and debit observes before minus after.
Invalid observations are forwarded without a success clamp.
Unsupported model tokens return zero outputs and invalid status without invoking native accounting.
Negative requests reject through the existing primitive, and fractional requests remain a caller contract error rather than being rounded here.

### Output lifetime and nested scratch

Public outputs survive helper return only because the outer caller creates their storage first.
Resolver initializes `cbrn_action_agent_class` before its nested resolver call.
The outer caller must separately precreate that class if it needs the derived value after this resolver returns.
Both measurement wrappers initialize or copy all seven nested scratch fields before invocation: `cbrn_mask_native_model`, `_requested`, `_before`, `_after`, `_observed`, `_valid`, and `_debit`.
The debit scratch is initialized even though its actual write occurs inside nested meta-effect text.
The wrappers map before, after, observed and valid back into public storage immediately after the nested helper returns.
These temporaries are unscoped and shared names can overwrite existing outer mask scratch.
Do not keep an unconsumed mask observation across this call or interleave measurement transactions.
No temporary result persists across delayed events, and parent receipt storage must freeze required evidence before action resets or asynchronous callbacks.

```text
# Caller already created and validated the exact model and requested quantity.
set_temp_variable = { cbrn_payload_native_before = constant:cbrn_math.zero }
set_temp_variable = { cbrn_payload_native_after = constant:cbrn_math.zero }
set_temp_variable = { cbrn_payload_native_observed = constant:cbrn_math.zero }
set_temp_variable = { cbrn_payload_native_valid = constant:cbrn_math.zero }
cbrn_payload_measure_model_debit = yes
# Parent consumes observed evidence here before any reset or other transaction.
```

## Referenced contracts, tuning and migration

Reuse is sound because the COUNTRY primitives in `common\scripted_effects\cbrn_state_escrow_native_effects.txt`:9-43 and 198-229 paste arbitrary `GetTokenKey` model values into the stock getter and native stockpile effect.
Their bodies have no mask-model whitelist, STATE receipt mutation, actor-target rebinding or consequence calls.
Their mask scratch names do not constrain the concrete equipment family.
Native debit and credit accounting is therefore reused rather than duplicated.
Source SHA-256: `107D041E9762E2E54E131C4D23E26CDAB8842F2CD611213F45F181091CD1B567`.
Existing API prose was read at `common\scripted_effects\cbrn_scripted_effects.md`:759-786.

The exact class mapping is `common\scripted_effects\cbrn_chemical_raid_effects.txt`:22-62, SHA-256 `B770477F77423347EEDA57E644EE3ACFA3EB6AAE9E492347A9FF71E049C67D8C`.
The four model tokens match `common\scripted_effects\cbrn_payload_effects.txt`:145-170, SHA-256 `84D3D8A19C94954ADCA3D4B7EE8030BE9EB3F77552B8F8C6D8014A47A34732B9`.
Their existing concrete definitions were located at `common\units\equipment\cbrn_payload_equipment.txt`:363, 393, 423 and 453, with token enumeration at `common\script_enums.txt`:735-741.
Existing dynamic effects and their matching markdown index were checked before creating the layer.
Generic stock-removal helpers do not supply the measured concrete-model contract required here.

No constants or tuning values were added or changed.
The layer uses existing `cbrn_math.zero/one`, `cbrn_proof.missing/supplied`, `cbrn_agent_class` and `cbrn_delivery_route`.
The reused debit primitive retains `cbrn_math.negation_multiplier`.
No event targets, persistent flags or cleanup hooks are created.
No receipt cleanup, capture, removal, disposal, profile guard, stock grant, consequences, AI weights or pacing were implemented.
The only positive stock write is the explicitly invoked measured refund primitive.

Migration is parent-owned: use resolver plus measured debit when creating the CBRN receipt, record actual held quantity, retain partial/mismatch evidence, and use measured credit only for an authorized refundable remainder.
Event32 direct consumers, full receipt state machine, once-only closure, physical-custody dispositions, profile guard, existing helper/API docs and tests remain with the parent.
There are no new Event32 call sites in this patch, as explicitly required by this assignment.

## Meaningful validation and exact limits

Completed source review traced all nine supported agents through the existing class resolver to exactly four prepared-air models, checked unsupported-route rejection and supplied-class replacement, and reviewed both native accounting bodies for arbitrary token support, measured deltas, partial/zero behavior, invalid observation preservation and nested scratch lifetime.
`hoi4.source_lookup` returned each measurement primitive without overrides and the vanilla `bba_get_fighter_GER_effect` precedent at `game:common/scripted_effects/00_scripted_effects.txt`:1842-1863 under index revision `30e08c98e142a7028d4efa8d70f1b7b3f0205a52ee95e49476479945570d014a`.
Vanilla `common\scripted_effects\CZE_scripted_effects.txt`:438-459 was also read for meta text/replacement structure.

All three actual helper bodies were submitted to `hoi4.script_validate` with `kind = effect`, `scope = country`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.
They returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, and checks performed only for syntax, command kind and declared scope, with no error diagnostics.
Resolver checked 23 commands with 18 unresolved findings, and each accounting wrapper checked 21 commands with 20 unresolved findings.
Native argument blocks remain unchecked and the nested scripted helpers remain unresolved by this native-documentation validator.
The final bounded calls still omit 18, 21 and 21 findings respectively, so complete MCP validation is not claimed.
Documentation set revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
An attempted larger finding limit was rejected with `limit must be <=32`, then corrected to 32.
Exact argument and nested helper source contracts were reviewed separately, and that review does not replace unresolved engine evidence.

A read-only Event32 trace used selector `chaosx.nr32.1`, depth 1, two nodes, two edges and no helper expansion.
It returned `EVENT_INSPECTED_PARTIAL`, focused analysis, zero indexed helpers, one blocking event-analysis diagnostic, and graph revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9836b8cae2f4e7b0499395248d3a710f9361bb62d987d8583ba19bf1f3ac5b07/ab441fb0146b848c20c4de9f276e72c8e506a0a8adf9422cbd99e74eea430b6d/event-trace-8f4a82aa5d84.json`.
A bounded prefix read confirms `complete = false`.
The full 1,079,948-byte report was not consumed, so its full source inventory and diagnostic detail remain unreviewed.
The exact coverage gap is focused event analysis excluding scripted-helper lifecycle inspection, with incomplete report coverage, rather than an absent MCP route or a proved runtime failure.
No long graph expansion, event render/compare, stock simulation or actual-source transaction tests were run in this primitive-only assignment.
Parent integration owns those tests and full event evidence.

Parent testing targets are all nine agents on both supported routes, deliberately mismatched supplied class, unsupported agent/route/model, whole-count full and stock-bounded partial debit, zero stock/request, negative request/stock, observed delta of opposite sign or exceeding request, partial/zero credit, original request preservation, and conservative caller/helper/meta output lifetime.
Those are pending test cases rather than executed scenarios.
Native stock getters, equipment unlock/producer/variant behavior, refunds after policy or profile change, and actual engine temporary lifetime remain unobserved.
The model token does not preserve individual manufacturer or variant identity, and repeated credit is unsafe unless the parent verifies and closes the exact held receipt.

## Offline and installed reference evidence

Reference context/search/read routes were available and called with the explicit workspace.
The initial context omitted Triggers, Modifiers and Scopes under its small result limit.
Relevant trigger and scope sections were subsequently read, while modifier rules are outside this layer.
No required reference file was reported missing.

| Reference read | Lines | Source revision / SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, temporary lifetime and token values | 435-443, 955-972 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md`, equipment and meta construction | 2253, 4617-4682 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md`, scope types | 32-64 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md`, operators and context | 66-87 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Installed `documentation\effects_documentation.md`, COUNTRY stock mutation, meta effect and temporary assignment | 1252-1266, 4833-4852, 7820-7840 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md`, variable comparisons | 2110-2135 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\script_concept_documentation.md`, script constants | 216-222 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md`, schema and access | 1-34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |

Installed paths above are relative to `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Installed equipment documentation says omitted producer applies to all creators, while offline wiki prose gives a different optional-producer default.
The layer retains the existing producer-unspecified measurement contract and makes no producer-preservation claim.
Guidance used: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, and the named architecture handoff.
No skill was created or updated.
No simplification or accounting fallback was made within the assigned primitive scope.
Completed work is this reusable layer and API/testing handoff, with Event32 runtime completeness and unresolved MCP/native evidence remaining parent-owned.
