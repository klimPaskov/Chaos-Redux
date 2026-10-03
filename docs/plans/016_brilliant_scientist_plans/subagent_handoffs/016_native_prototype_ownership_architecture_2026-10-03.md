# Event016 native Prototype ownership architecture

Date: 2026-10-03.
Role: chaosx_scripted_system_architect.
Disposition: architecture delivered, implementation and engine validation remain parent-owned.
Scope: Cloning and the two Rocketry Prototype alternatives only.
Only this handoff is written.

## Recommendation and acceptance boundary

Keep `sp_brilliant_scientist_cloning` as the accepted Cloning route.
Use exact country-output wrappers for that project, `sp_rockets_flying_bomb`, and `sp_air_jet_engine`, with a separate completed-native adoption path.
Retain an explicit per-project provider selection receipt for Rocketry rather than inferring selection from whichever alternative happens to be completed.

The recommended resolution of the missing lifecycle seam is an explicit, zero-cost provider native-route commitment, followed by native research in the existing project UI.
Its pending flag means that the provider selected that exact project and passed its gate.
It does not mean that native research started, paid, or remains active.
This selects the practical recommendation under the supplied instruction to take the recommended option, without asserting that a native start/cancel hook exists.

The accepted closure plan requires selected-alternative pending ownership at line 63 and its exact callback consumption at lines 88 and 126.
It also permits completed-native adoption at lines 138 and 120, after Theory, without replaying native payment or output.
These requirements can coexist when selection, fresh exact output, and historical adoption are separate transactions.
They do not authorize an aggregate completed-project OR to substitute for selected-alternative ownership.

An explicit commitment action and its release semantics are a concrete design amendment if the accepted pending receipt was intended to mirror native start/cancel automatically.
This handoff does not silently mark that stronger contract implemented or superseded.
The parent must record the interpretation or amendment and wire an actual selection entry point before claiming pending ownership complete.
If actual native start/cancel synchronization is mandatory, the exact missing input is an engine-proven effect-bearing start/cancel seam, or accepted authorization to use explicit commitment/release instead.
No choice of Cloning project is reopened.

## Current source findings

1. `brilliant_scientist_mengele_rocketry_native_output_is_authentic` accepts completion of either Rocketry alternative without a pending-project check, at stage triggers 1448-1456.
`reconcile_reused_native_project_prototypes` invokes family-level reconciliation from the existing generic completion boundary at stage effects 1559-1570.
Consequently, the reviewed path cannot distinguish a fresh selected Flying Bomb output from an already-completed Jet Engine when checking Rocketry ownership.
No exact selected-alternative receipt is read by that predicate.

2. Cloning authenticity correctly queries only `sp_brilliant_scientist_cloning`, at stage triggers 1489-1496.
However, the private availability bridge also rejects `directorate_special_project_cloning_completed`, at bridge triggers 59-69.
The legacy `sp_mengele_cloning` output invokes `germany_mengele_complete_cloning_project`, which sets that shared completed flag at Germany effects 106-119.
A legacy completion can therefore block the accepted custom route without proving its exact completion or the private provider Prototype.
Remove that shared-flag veto only from the private accepted-route gate.
Do not clear the shared flag, delete the legacy project, or alter its external consumers.

3. The accepted Cloning project's country output currently calls `cbrn_complete_cloning_project`, at projects 397-427.
That adapter dispatches Event016 story owners through the generic Prototype recorder and ordinary discoverers through the neutral clone API, at CBRN effects 65-76.
The legacy project has its own output and refinement/equipment/neutral API consumers, at legacy projects 67-78.
An additive exact-source marker/wrapper belongs on the accepted project's country output, before generic dispatch can classify the receipt.
The existing CBRN call must still run once with its existing owner distinctions.
The legacy output must never call the private accepted-project wrapper.

4. `adopt_completed_native_after_theory` already isolates the enclosing Theory transaction and restores its selectors/results at stage effects 1464-1512.
`sync_native_project_prototypes` currently authenticates country completion state rather than selected project ownership at 1515-1536.
Availability at 1666-1709 publishes research access and is explicitly not receipt settlement.
It cannot become a native start receipt.
The existing Electronics radar ordering retry remains outside this design change.

## Exact output hooks and adoption rules

| Exact source | Required additive hook | What it establishes |
| --- | --- | --- |
| `sp_brilliant_scientist_cloning.project_output.country_effects` | `brilliant_scientist_mengele_native_output_cloning` | An output from the accepted custom project, never proof from `sp_mengele_cloning` or its shared flag. |
| `sp_rockets_flying_bomb.project_output.country_effects` | `brilliant_scientist_mengele_native_output_rocketry_flying_bomb` | That exact Rocketry alternative emitted output. |
| `sp_air_jet_engine.project_output.country_effects` | `brilliant_scientist_mengele_native_output_rocketry_air_jet_engine` | That exact Rocketry alternative emitted output. |

All wrappers run in the documented country scope, with FROM as the project at the native output boundary.
Use literal per-project wrapper identity rather than a guessed persistent project database number or an inherited family temporary.
Each wrapper records a durable exact output-observed flag even when private settlement is currently ineligible, without granting private stages merely for observation.
It may settle a fresh private Prototype only with a valid provider, exact Theory flag, incomplete private Prototype, empty matching paid receipt, and its matching selected pending flag.
The other alternative's output may retain native rewards and observation history, but cannot consume the selected pending flag or settle that private stage.
Record a rejected/retired provider disposition so a later generic adoption call cannot relabel that stale alternative as accepted history.

The direct output hook is completion evidence.
Do not require a country completed query inside that same hook unless engine evidence proves its visibility there, since that can introduce another ordering dependency.
The historical adoption path must use the exact country `is_special_project_completed` query.
It must not replay `project_output`, call `complete_special_project`, restart research, charge provider Prototype costs, or fabricate a pending native start.

Use two independent provenance facts: the exact source project and the settlement mode.
`fresh_output` means the exact synchronous project-output wrapper consumed the matching current provider selection receipt.
`adopted_completed` means an explicit reconciliation accepted an already-completed exact native object after Theory.
Absence of an output-observed marker means completion time is unknown, including projects completed before hook installation.
Label these receipts adopted, never fresh.
A country completed bit alone cannot reconstruct whether Theory existed at the original native start or who owned that research at that time.

At successful Theory settlement, preserve accepted completed-native adoption for an exact eligible project.
Cloning has only the one accepted exact source, so legacy completion alone yields no adoption.
Rocketry may auto-adopt a single unambiguous eligible completed alternative when there is no competing pending receipt or rejected/retired disposition.
If both exact Rocketry projects are historical candidates, use explicit selection of the historical source rather than an arbitrary OR branch priority.
If a pending alternative already exists, only its matching source can settle that receipt.
A fresh output with no pending commitment records observation and leaves the private stage unsettled until a distinct explicit adoption transaction accepts the exact completed source.
This avoids disguising missing selection ownership as a fresh native receipt.

These hooks suffice for exact completion identity and completed-native adoption under the approved design.
They do not, alone, satisfy the pending writer, prior-selection, or native cancellation requirements.

## Concrete selection and cancellation seam

No effect-bearing native start/cancel callback was identified in the bounded installed project documentation read here, consistent with the parent's search result.
`available` and `visible` are display-time triggers.
`is_special_project_being_researched` is a country-state query, not a callback.
An observation at Theory settlement can detect research already in progress at that moment, but cannot observe a later start or cancellation and is not a complete substitute.
Do not add daily/world-scanning polling or invent an `on_project_start`/`on_project_cancel` effect.

Recommended parent implementation: first reuse an existing explicit exact-project selector effect if the parent can identify one.
If none exists, add a narrowly scoped instant commitment action under the existing provider category while the family is awaiting its native Prototype.
For Rocketry, expose two mutually exclusive choices for the two existing IDs and retain only one pending flag.
These are selection actions with zero resource payment and no timer, not provider Prototype research decisions.
Cloning has one fixed commitment source and needs no project-choice prompt.
An exact completed source uses adoption instead of opening a fresh commitment.
A historical two-source Rocketry ambiguity may use the same explicit source selection boundary with adoption semantics.
No AI weight change is specified by this architecture.

Keep native gates, breakthrough costs, resource costs, complexity, prototype time, and rewards authoritative.
The selection action does not start native research or cancel native research.
Native cancellation in the engine may leave a provider commitment selected for eventual resume because no automatic cancellation effect is available.
An explicit provider release can clear a selection after verifying that its project is not currently being researched, without refunding native costs or changing native clocks.
Mark the released receipt retired so delayed output cannot be adopted automatically through a completion OR.
Provider loss and terminal cleanup clear selection ownership in the original provider scope and preserve native knowledge/output history.

Automatic clearing on native cancellation and proof of same-project release/reselection callback isolation remain unresolved engine/design points.
Do not claim that a fresh mutable country token provides callback-generation isolation.
If strict same-project reselection is needed, the parent needs an engine-proven retirement boundary before permitting it.
Do not silently forbid native resume, silently switch alternatives, or silently waive a pending requirement to conceal this gap.

## Proposed helper map

These are local Event016 proposals, not implemented definitions.
Document their defaults and lifecycle in the matching stage helper documentation when the parent implements them.

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_select_native_prototype` | Country, explicit literal source wrapper, valid provider, Theory, exact native gate, incomplete Prototype, empty paid receipt, no conflicting pending. Default source is none and rejects. | Writes exactly one static per-project pending selection flag, dedicated selected result, no debit or clock. | Existing exact selector if proven, otherwise the proposed instant commitment action. |
| Three `brilliant_scientist_mengele_native_output_*` wrappers above | Country, literal source, native country-output boundary. | Observed-source marker, exact pending validation, dedicated fresh result, matching pending consumption, existing private stage output. | Three exact existing project outputs only. |
| `brilliant_scientist_mengele_adopt_completed_native_prototype` | Country, explicit eligible exact source, completed query, provider and Theory, no conflicting pending/retired/rejected source, empty paid receipt. | Private Prototype once, adopted provenance, no replay of native output. Defaults reject absent/ambiguous source. | Existing after-Theory adoption adapter and explicit exact completed-source adoption. |
| `brilliant_scientist_mengele_release_native_prototype_selection` | Country, literal selected source and release/cleanup reason. | Clears matching pending, retires unresolved ownership, preserves observed native facts and learned packages. No native refund. | Explicit release if accepted, existing provider/terminal cleanup in original owner scope. |

Reuse the existing private stage output core and exact predecessor guards.
Set dedicated Prototype success before any nested later-stage retry and preserve the enclosing Theory adapter's existing result restoration.
Clear family/stage/source/index selectors after the transaction.
No event target or persistent special-project numeric token is needed for these three static source identities.

Constants and tuning: no new costs, durations, AI factors, or gameplay tuning values.
Use boolean flags for selected, observed, adopted/fresh, and rejected/retired state rather than numeric 0/1 variables.
If the parent uses a small provenance enum instead, place only those static metadata constants in a subsystem script-constant category and verify its supported fields against installed documentation.
No balance target or probability claim is made.

## Narrow migration and validation requirements

1. Separate Cloning private availability from the legacy shared completed latch, preserving the accepted exact project gate and Theory.
2. Add the three exact output wrappers to existing definitions and preserve original native outputs and payments.
For Rocketry use the existing same-path vanilla overrides, without creating duplicate project definitions.
3. Split fresh completion from historical adoption for these two families.
Remove their aggregate completion OR from the fresh ownership path, while preserving explicit adopted completion support.
4. Wire a real exact selection writer and the matching consumption/release/cleanup paths.
Do not mark availability flags pending or treat legacy clone entitlement as private stage proof.
5. Preserve existing CBRN/legacy Cloning payload idempotence and other-family callbacks.
No broad fifteen-family helper migration is proposed.

Required parent scenarios: legacy Cloning complete with custom Cloning incomplete, custom historical Cloning adopted after Theory, custom fresh Cloning with matching pending, either Rocketry alternative selected while the other is completed, stale other-alternative callback, both historical alternatives, missing Theory, missing pending, active paid Prototype timer, repeated exact output, output before completed-query visibility, native cancellation/resume, explicit release/reselection, provider cleanup followed by delayed output, and ordinary CBRN/legacy consumers retaining native payoffs.
Same-project release/reselection must remain unresolved until supported evidence settles it.
MCP inspection/comparison, source preservation comparisons, and final wiring remain parent-owned.

## Limits and delivery

This is source-only architecture, not engine evidence.
No MCP route was called or health-tested, so no MCP outage is asserted.
The exact MCP evidence gap is the explicit source-only delegation and absence of supplied live ownership/cancellation artifacts.
No start/cancel callback absence is claimed for all possible engine integrations, only for the bounded documentation reviewed and the parent's reported narrowed search.
Scripted `complete_special_project` can also emit country output, so fresh_output means a witnessed callback transaction, not independent proof that native research payment occurred.
No engine launch, models, gameplay/localisation edits, other documentation edits, index changes, or commit.
No fallback or implementation simplification was applied.
The explicit commitment/release interpretation remains visible as a proposed design amendment, not a silent replacement of stronger lifecycle acceptance.
Skills used: chaos-redux-subagents and chaos-redux-events, unchanged from the preceding review.
AGENTS.md and the subagent skill hashes remain identical to the versions read for that review.

## Bounded source and reference ledger

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Wiki pages identify the offline snapshot as captured 2026-09-19.
The SHA-256 hashes below identify the local reference/source revisions, with no live engine revision claimed.
The guessed installed `common/special_projects/documentation.md` path was absent.
The actual project documentation was located and read at `common/special_projects/projects/documentation.md`.

| Local source path | Bounded line spans | SHA-256 |
| --- | --- | --- |
| `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md` | 19-24, 59-64, 81-94, 105, 109, 120-138, 198-204 | `6A6ABB79B71515D90F2BC22E616EC53A789BFD281011EE592C1BFDE6F3073456` |
| `common/scripted_effects/016_mengele_project_stage_effects.txt` | 989-1000, 1094-1116, 1464-1570, 1666-1760 | `8161A88971EEA2989126634AA41E433E652934D76D906414A048BD3498A12C40` |
| `common/scripted_triggers/016_mengele_project_stage_triggers.txt` | 1448-1456, 1489-1496 | `5AB7041CE22F13FBFECF641F4CA9E6FC7D693DDF366DA14E631A3DFA498E537C` |
| `common/scripted_triggers/016_mengele_project_bridge_triggers.txt` | 59-69 | `03B38228120B24D5228AC9986AC3745F7760DCEBC38D61D6DCE8DE29C50325CD` |
| `common/special_projects/projects/016_brilliant_scientist_projects.txt` | 397-427 | `CD52D36792B2A9A9AC767268F131D0B36F1495D43F2B2AD8C52E5BA328E2AB23` |
| `common/special_projects/projects/mengele_cloning_projects.txt` | 17-78 | `6E5A2A8BC286E2DB00288070EF52A815FAC6DD5C376FBC0641C440229F57B645` |
| `common/scripted_effects/cbrn_special_project_effects.txt` | 65-76 | `2CA72052A129837D232B3CBD907159EFC1A7D5E6511CCC61C98A958311D8E105` |
| `common/scripted_effects/germany_mengele_effects.txt` | 104-119 | `6C201B87CCED6AE86ACD148E6B19801AAC1E17045B704ADC92BE5A29AAB32557` |
| `common/special_projects/projects/rocket_projects.txt` | 14, 23-33, 51-96 | `85BF63426DA240CE8EDFA97D9545570B3638E1244413DBAD8D459434EDE0F1D8` |
| `common/special_projects/projects/air_projects.txt` | 797, 806-839, 841-903 | `66940F2E3B34D3DAD14605D147090420C252F0F0F642A463A50731A3F3242727` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/special_projects/projects/rocket_projects.txt` | 10, 19-29, 47-72 | `C2AA6F2822C6A5DC1F7EDC34D917EF2440F245C47EA02358AD05F8F38C7DE6DA` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/special_projects/projects/air_projects.txt` | 793, 802-851 | `9A8E41F1DD41D22BCB6BA8974BC217AE9F2404F262E508A4D32B3F7C10C077E1` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/special_projects/projects/documentation.md` | 1-65, 158-163, 198-225 | `16879504BC72AA357F1D3C0F1093E94A3946F8C35E7942F65AC9A5D3BCD6C643` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/special_projects/special_projects_documentation.md` | 63-69, 107-126 (targeted search corroboration only) | `E5D1766E95FE9C71D676046720BB699918E2565C8A43FE5A9183359C98BFCBFE` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` | 3624-3638, 6228-6256 | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` | 2792-2799, 2900-2923, 6730-6737 | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 102-125 | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | 885-886 | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 3172-3195 | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | 53-61, 254-259 | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |

## Parent disposition

The parent accepts and queues the recommended exact selection actions and separate completion/adoption modes under the user instruction to take the recommended option on 2026-10-03.
Automatic native cancellation cleanup and selection persistence/reselection remain unresolved, and no stronger existing lifecycle requirement is waived under the no-simplifications constraint.
Its exact acceptance and limits are recorded in docs/specs/016_brilliant_scientist_specs/specs/016_native_prototype_ownership_amendment_2026-10-03.md.
This promotes the bounded selection and provenance design into an accepted spec and does not claim the full selection/ownership lifecycle implemented.
The separate Cloning availability portion is implemented in 018b7d55c with its bounded source review.
Same-project release/reselection evidence and the remaining exact writers, adoption, consumption, cleanup, AI and CXT work remain open.
