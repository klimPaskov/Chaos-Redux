# German national transfer: live availability and source margin

Disposition: implemented in package source with bounded tests; native decision eligibility, tooltip rendering and exact engine receipts remain unresolved.

Acceptance basis: the user retained one paid exact-living-cohort national order and chose the oldest eligible registered source on 2026-09-26, recorded in [accepted_implementation.md](../accepted_implementation.md).

## Defect and bounded correction

The earlier availability used a cached `camp_occ_manual_source_state_id` and basic source state flags, while the selector's one-person preflight and the effect's full-request preflight could disagree after a cohort or population changed.
For example, a source with a 100,000-person living row and a 950-person physical margin could pass a one-person probe, yet its 5 percent proposed order would fail the strict source-margin check and charge nothing.
The current state-scoped `camp_occ_manual_transfer_live_source_ready` checks aligned row arrays, native row ID, active status, host, original authority and origin registration, whole-person share, country aggregate and the source physical margin minus one person.
The destination trigger separately checks the supported state-88 killing role, reconciled custody rows, building and developed capacity, the population-share limit and uncommitted population for at least the minimum order.
The decision has separate prerequisite, source, destination and cost tooltip gates; source-name scripted localisation scans the bounded registry at display time rather than trusting the cached execution pointer.
At execution the effect refreshes the oldest pointer, caps the request by the real destination, source physical margin, row and aggregate, rechecks the exact transaction, and pays only after a positive source debit, destination credit and custody bind receipt.
The post-order refresh remains, and no whole-world recurring hook or population-loss API changed.

## Source identity and checks

- Frozen before decision: `../ai_evidence/transfer_availability_decisions_before_2026-09-27.txt`, SHA-256 `e06525307514bb1f66b923f824a3d9ac00937202dc0194fc7ce53fab7633c0f2`.
- Frozen before trigger: `../ai_evidence/transfer_availability_triggers_before_2026-09-27.txt`, SHA-256 `bb0238c5a601c90f2093253cccd9b1b0143c65e091e082913fafe5971eb2724c`.
- Current decision: `common/decisions/genocide_crisis_decisions.txt`, SHA-256 `610117369787dad95b345632a7120a67823b35cfd9384f28fb87663db133fef2`.
- Current occupation triggers: `common/scripted_triggers/camp_administration_occupation_triggers.txt`, SHA-256 `a22382d8b2db75d365318d0882fae9e4e2b0917252ce51f71de8ff38514bc5bd`.
- Current occupation effects: `common/scripted_effects/camp_administration_occupation_effects.txt`, SHA-256 `bed0d4c87bca0a03ced945133b6905c6da14c373c2ecf4a5849caf40bbbc8a67`.
- Current German country effects: `common/scripted_effects/camp_repression_major_country_effects.txt`, SHA-256 `2da1451808946fc5c14d86cd338610e453530a3595462c315ddf3d949e4a13f3`.
- Current scripted localisation: `common/scripted_localisation/camp_administration_country_localisation.txt`, SHA-256 `0f9be6ed056ee95682714629183e383a249f8c322de2ff173c4dba792996145d`.
- Current English decision text: `localisation/english/chaosx_decisions_l_english.yml`, SHA-256 `6e4727bc2d072c02c9f57b59e2d0b30e14660c9120ebacf913f418ae1ec20c10`.

The full occupation source suite runs 60 tests, including a new boundary case where the earliest one-person-valid row cannot fill a minimum order but a later row can, and where destination headroom is 999 versus 1,000 people.
The current five touched Clausewitz files parse with the package source parser; this checks structure, not engine semantics.
The edited English localisation retains UTF-8 BOM and the new destination key occurs once.
The read-only localisation auditor initially questioned whether the live display and effect used different row amounts, then retracted that finding after checking `camp_occ_prove_active_row`: both read the same indexed `camp_occ_row_amounts_k` value.
The auditor also found the blocked custom-cost row lacked a deficient amount and icon; its suggested one-resource scripted-localisation status replaced the generic blocked label without expanding the inline price row.

## References and native limits

Root's `hoi4.reference_context`, `reference_search`, `reference_read` and `source_lookup` routes are absent from its connected tool list; the architecture audit used the connected reference and source-lookup routes and returned decision revision `f1955bb703adb4a0cb975b5b4d082821689739ea5739f0b693128ea30968863f` for its pre-edit read.
The locally read offline [Data structures](../../../../../paradox_wiki/Data%20structures%20-%20Hearts%20of%20Iron%204%20Wiki.md) sections at lines 1069–1077 and 1145–1171, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, document array indexes, temporary variables and scope loops in triggers.
Installed `documentation/triggers_documentation.md` at lines 1035–1070 and 7482–7501, SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, documents `all_of`, `all_of_scopes` and trigger-time temporary-variable arithmetic; the architecture audit also read `any_of` and `any_of_scopes` at lines 1515–1545.
Installed vanilla `common/scripted_triggers/00_scripted_triggers.txt` lines 675–683, SHA-256 `c8470b1937095f1aec1c09ee78365d770fab1aa7e28eb21d35924ca1253dd1db`, uses `any_of_scopes` over a country array; this is a syntax precedent, not a transfer mechanic.
The scripted-localisation audit cited offline `Localisation` lines 656–705 and 729–792, SHA-256 `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, for tooltip-time temporary variables.
The first exact source-file probability baseline inspected all 29 candidates and evaluated six unchanged named scenarios at scenario hash `41e48088659f4bbaf7fbd84b1974491d9d9004e028b1fe399fa081df13516c94`; it returned partial, score-only evidence with unresolved registry and destination bindings.
The [matched post-edit probability comparison](../ai_evidence/transfer_availability_probability_2026-09-27.md) returned partial score-only evidence with unchanged source willingness; typed registry and destination eligibility remain unresolved.
The exact-ID decision inspection returned `DECISION_ANALYZED_PARTIAL` at revision `85c15604da62e9fc58c66a9265d54dad010504d6e6193004dab4077cf5dccc46` with one declared scenario and 218 unresolved definitions; its [artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56e05e8386805be7455f4f3c31444b69289b4a3971da863c51c59dcbdd41d45e/52fdef8886cc12745aed095b568c41b024a18496389f85a9e79929616f34bea6/decision-b81cd3038a69334444927ce4.json) does not establish source or destination eligibility.
Neither these source tests nor the MCP's partial adapter prove that the native interface displays the dynamically selected state, executes a click successfully, or applies a physical receipt in Hearts of Iron IV.
