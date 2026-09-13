# Event 016 Mengele Prototype quote integration

## Disposition and authority

Status: implemented within the assigned quote, receipt-migration, and component-integrity scope, with current MCP lifecycle evidence blocked.
The acceptance basis is the parent's bounded integration assignment against `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, followed by explicit instructions to require all six private Singularity component flags plus their count and to migrate the remaining Computation presentation consumers to the shared table.
This handoff replaces the fourteen Prototype quote-gap claim in `016_mengele_portfolio_core_2026-09-05.md` for current source.
It does not establish full Mengele portfolio or Event 016 completion.

## Files changed

- `common/scripted_effects/016_mengele_project_stage_effects.txt`
- `common/scripted_effects/016_mengele_project_stage_effects.md`
- `common/scripted_triggers/016_mengele_project_stage_triggers.txt`
- `common/script_constants/016_mengele_project_stage_constants.txt`
- `common/scripted_triggers/016_mengele_computation_decision_triggers.txt`
- `common/decisions/016_mengele_computation_stage_decisions.txt`
- `localisation/english/016_mengele_computation_l_english.yml`
- This handoff.

The shared `016_brilliant_scientist_project_constants.txt` table was read without modification.
No board, no-DLC helper, native project definition, focus, model, Kruger variable, or Kruger history write was added.
No staging or commit was performed, and unrelated working-tree content was preserved.

## Helper map and behavior

| Helper | Scope and inputs | Output and side effects | Call sites |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_load_project_stage_quote` | Country, existing temporary family/stage selectors | All fifteen Prototype quotes from `brilliant_scientist_project_fallback_prototype`, duration from the existing duration table, no payment | Generic begin and existing Computation quote wrapper |
| `brilliant_scientist_mengele_project_stage_can_pay` | Country, same selectors and actual inventory | Inclusive direct PP/support/fuel affordability using the identical shared quote keys, read-only | Existing generic begin and begin-eligibility wrapper |
| `brilliant_scientist_mengele_initialize_project_stage_receipts` | Country, existing arrays and private component flags, no parameters | Independently appends zero slots to five arrays until the shared family count, preserves surviving values, preserves component flags and reconstructs their count only when its initialization marker is absent | Existing begin/native component calls and the added pre-scan cleanup call |
| `brilliant_scientist_mengele_singularity_components_are_complete` | Country, private count and six private component flags | True only for exact count six plus every component flag, no writes or defaults | Singularity Prototype predecessor and authenticated native component completion |
| `brilliant_scientist_mengele_cleanup_provider_receipts` | Country, existing initialized provider receipts | Expands the schema before visiting fifteen slots, then uses unchanged exact cancellation/refund behavior | Existing provider cleanup callers |

The strict active-owner predicate and the complete generic begin, cancel, finish, and direct-refund helper bodies are structurally identical to the captured pre-task source.
Stored direct payments remain authoritative for settlement, and factory reservations remain native decision commitments rather than refundable balances.
Native project callbacks never enter the generic payment path.
The corrected native Singularity completion gate places the completion-flag exclusion beside the component-integrity trigger, repairing the former `NOT` nested inside `check_variable`.
No event targets, periodic scheduler, extra Capacity meter, or public family ID was introduced.

## Constants and presentation migration

All fifteen Prototype loaders and their direct affordability branches reference `brilliant_scientist_project_fallback_prototype`.
Computation remains exactly 2 civilian factories, 68 Political Power, 200 Support Equipment, and 100 fuel.
The unchanged DLC-aware visibility gate still selects the native presentation when available.

Nine legacy constant references were replaced without changing their numeric values:

- One `ai_hint_pp_cost` in `mengele_event016_computation_prototype`.
- Four comparisons in `brilliant_scientist_mengele_computation_prototype_decision_can_pay`.
- Four interpolation tokens in localisation key `mengele_event016_computation_prototype_cost`.

The four unused `mengele_event016_project_stage.computation_prototype_*` mirrors were removed.
The file-scoped `@CR_SC_MENGELE_COMPUTATION_PROTOTYPE_CIVILIAN_FACTORY_USE = 2` remains because the existing native modifier field does not support shared constant tokens.
No AI score, outcome weight, duration, payment amount, or player-facing wording was changed.
The three extended-scope consumer files were compared to their captured baselines and differ only by those constant-token replacements.

## Concrete source-model scenarios

A small in-memory Clausewitz parser evaluated the actual changed helper and trigger blocks against explicit country-state fixtures.
It used the installed shared constants and did not generate gameplay source.
This is deterministic source-model evidence, not HOI4 execution.
The external strict-provider predicate was supplied as an explicit valid/invalid input, while its unchanged source was checked independently against the baseline.
Inventory arithmetic, flags, temporary variables, arrays, trigger composition, conditions, loops, and receipt settlement were evaluated.
Engine modifier application was represented by modifier identifiers, native project completion was false in the decision fixtures, and force-refresh and incident-dispatch callbacks were outside the model.
These tests do not establish modifier strength, incident probability, native project authentication, or factory-release engine behavior.

| Scenario | Observed result |
| --- | --- |
| Every family at Prototype | All fifteen quotes loaded, all four amounts matched the shared table, and no quote-source gap remained |
| Exact payment and separate one-unit shortages | Fifteen exact boundaries accepted and forty-five PP/support/fuel one-unit shortages rejected |
| Begin, stale-stage cancel, matching cancel, repeated cancel | Every family paid once, a mismatching stage did nothing, matching cancellation returned the exact receipt once, and duplicate cancellation returned nothing |
| Invalid-owner completion | Every family refunded its direct receipt without creating Prototype completion |
| Successful and repeated completion | Every family recorded its Prototype once, consumed the receipt, and ignored a repeated finish callback |
| Initialized one-slot schema | Five arrays containing `[2]`, `[68]`, `[200]`, `[100]`, and `[2]` expanded to fifteen slots with the same slot-zero values and zero tails |
| Repeated initialization | Arrays, existing variables, and initialization flags were unchanged on the second call |
| Cancellation after one-slot migration | Returned exactly 68 PP, 200 support, and 100 fuel from the preserved receipt |
| Asymmetric array lengths | Lengths 1, 4, 7, 12, and 15 became fifteen without overwriting any surviving prefix value |
| Six component flags without initialization marker | Flags survived and the derived count became six |
| Each possible missing component flag with count six | All six separate five-flag fixtures failed both the shared native-completion predicate and Prototype begin, with no debit |
| Six flags with count five | Component integrity failed |
| Concurrent Computation and Electronics | Both receipts coexisted, and cancelling Computation preserved the Electronics stage and direct-payment receipt |

The source-model test was repeated after migration of the presentation consumers and removal of the four private mirrors.
The source-level component guard is used by both native completion and paid entry, so an inflated count cannot substitute for a missing component flag.

## Required references and MCP blocker

Read references included AGENTS.md, the event/subagent/decision skills, the accepted completion contract, the prior portfolio handoff, existing dynamic helper source/docs, the required offline wiki core pages, and the specific Data structures array/temporary-variable and Triggers inventory sections.
Installed vanilla `script_concept_documentation.md` and `common/script_constants/documentation.md` established constant access, while `effects_documentation.md` established array append, resize, loop, variable, stockpile, and fuel behavior.
Installed `triggers_documentation.md` was consulted for comparisons and inventory predicates, and the bounded loop in vanilla `SOV_scripted_effects.txt` was used as a loop precedent.
The existing Mengele Computation decisions remain the native receipt/payment/cancellation precedent.

Two correctly formed read-only calls to `hoi4.event_inspect` failed:

1. `mode = state_flow`, selector `{ kind: event, eventId: chaosx.nr16.901 }`, depth 2, nodes 20, edges 30, helpers enabled.
2. `mode = trace`, the same event selector, depth 1, nodes 10, edges 15, helpers disabled.

Both returned `timed out awaiting tools/call after 180s`.
Earlier selector-discriminator validation failures were corrected before these calls and provided no evidence.
No current graph artifact, revision, render, or comparison was returned.
Further render/compare work was not attempted without a current successful inspection baseline, and the parent requested no repeated identical inspection attempts.
Full helper lifecycle analysis, native callback engine behavior, and matching before/after evidence remain unresolved.
There is no claim that the source model replaces the required MCP evidence.

Tested primary source SHA256 values:

- Stage effects: `54308F99F682AB50E97A542B8D0CAEE3617A5A6621E09B27FDE178B7FA8549AE`.
- Stage triggers: `9990812298092939C45070ACBE111F8C0D4248596B9648412019D04201B312AF`.
- Private constants after mirror removal: `28F23577731BAECB1A978827D7D0DBA318CD94E4C99E839197810229B623CDA0`.

## Existing native wiring and unresolved integration

Current `brilliant_scientist_record_new_project_prototype` in `016_brilliant_scientist_project_effects.txt` already dispatches valid Mengele owners to `brilliant_scientist_record_mengele_project_prototype`.
The ten ordinary native definitions in `016_brilliant_scientist_projects.txt` already call that wrapper for Computation, Materials, Biomedical, Teleportation, Cloning, Robotics, Paleogenetics, Xenobiological Synthesis, Alien Arms, and Temporal.
Those existing calls are not missing and were not edited here.
Native definitions outside that file, including the Electronics, Rocketry, High Energy, and Biological Weapons routes, require their own current owner-dispatch audit rather than an assumption that this tranche proves their integration.

Singularity's native definitions still call `brilliant_scientist_register_singularity_component`, whose inspected body writes Kruger's component state.
Routing that parent-owned registry to `brilliant_scientist_record_mengele_singularity_component` for a valid private owner remains separate work.
The private component gate does not perform that dispatch or fabricate a component receipt.

Non-Computation decision adapters and their cost presentation, reserve requirements, factory commitments, and literal callbacks remain outside this tranche.
The new shared quotes do not by themselves create playable decision rows.
Biological Weapons and Singularity Deployment/Weaponization still expose the existing explicit output gaps and refund direct receipts without inventing an adapter.
No biological mechanisms or real-world procedures were added, and these families remain abstract gameplay tokens in this work.

## Limitations and completion boundary

No simplification was introduced in the bounded quote/migration patch.
Current engine evidence is blocked, and the broader portfolio remains incomplete for the explicit output and presentation reasons above.
Longer-than-current arrays are preserved without truncation, while current cleanup visits the fifteen defined families.
Missing historical payment values cannot be reconstructed and are never fabricated from a current quote.
Assets, Event Log, Event Details, workbook, and broader event documentation remain parent-owned integration surfaces, with no new art or localisation key required by this patch.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-decisions-missions`.
No skill was created or changed.
