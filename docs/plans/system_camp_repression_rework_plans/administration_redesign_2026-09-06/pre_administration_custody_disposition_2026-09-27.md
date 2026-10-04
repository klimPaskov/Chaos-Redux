# Pre-administration custody disposition

Disposition: accepted second policy, implemented in source; native lifecycle evidence remains unresolved.
Acceptance basis: on 2026-10-03 the parent selected explicit zero-recorded-survivor closure under the user's current instruction to take recommended choices without waiting, within the approved finite-custody and legacy-reconciliation contract.
This acceptance records the current parent decision and makes no claim that an earlier direct human reply exists.

Current implementation is `camp_admin_integration_record_unrecorded_closure`, called by the accepted dismantlement completion adapter.
Its idempotent record requires an uninitialized site and valid original responsible authority, reports no recorded survivor figure, and creates no population, custody, manpower or death receipt.
The earlier diagnostic below describes the pre-choice source snapshot and does not override this disposition.

`camp_admin_initialize_site` in `common/scripted_effects/camp_administration_effects.txt` lines 66–115 starts an old site with zero detainees and empty aligned custody rows. Positive admission at lines 269–313 requires a proven source and appends a finite row. The country census in `camp_administration_country_census_effects.txt` lines 7–161 apportions policy/date/host stock; calling it during teardown would enroll a new cohort rather than recover an observed survivor count. The inspected old site flags and variables provide no exact pre-administration prisoner amount.

The legacy start and completion predicates in `camp_repression_rework_triggers.txt` lines 141–177 and discovery predicates in `genocide_crisis_triggers.txt` lines 245–268 still admit `NOT camp_admin_initialized` states. The administration reform and closure wrappers in `camp_administration_integration_effects.txt` lines 116–153 act on initialized reconciled custody. Consequently a pre-administration physical teardown can complete with no finite survivor release and no Administration Records closure entry. Source-only wording now promises release of recorded survivors; it does not supply a missing receipt.

The affected package-owned callers are the generic dispatcher (`camp_repression_action_dispatcher_effects.txt` lines 284–297), selected-site GUI (`camp_repression_rework_effects.txt` lines 4071–4115), German Auschwitz closure (`camp_repression_major_country_effects.txt` lines 1176–1197), Japanese shutdown (lines 1804–1835), Soviet Gulag closure (lines 2349–2379), the shared colonial start and completion (`camp_repression_colonial_country_effects.txt` lines 1665–1686 and 1714–1796), and discovery liberation (`events/genocide_crisis_events.txt` lines 179–302 into `genocide_crisis_effects.txt` lines 1059–1080). The separately owned Soviet-collapse aftermath caller in `common/scripted_effects/005_soviet_collapse_effects.txt` subsequently gained a completion-receipt guard for its own cleanup, stability and native-cost refund, but it still shares this pre-administration custody exception; see `uwr_aftermath_receipt_handoff_2026-09-27.md`.

The audit considered two policies: require initialized reconciled custody before closure, or permit explicit closure of an unrecorded legacy site with no survivor claim.
The parent selected the second policy on 2026-10-03 under the current user authorization.
Neither policy permits inference of prisoners from buildings, general state population, a census ceiling or historical transport estimate.
Current source implements the explicit unrecorded Records entry; existing receipt-based retry and terminal cleanup remain part of the acceptance contract.

Acceptance scenarios after the choice: uninitialized site with no recorded custody; initialized empty site; initialized valid live cohort; misaligned rows; loss of authority before completion; discovery popup whose control changes before click; retry after timer expiry; other-package Soviet-collapse reward after a rejected camp close. A successful positive release must consume only the observed living rows and never add population.

The read-only architecture audit used the offline wiki `Data structures` lines 303–328, revision `62273f37`, and `Event modding` lines 192–229, revision `96327b89`; installed vanilla `effects_documentation.md` lines 6496–6504, revision `2cdc93d2`, and `common/decisions/_documentation.md` lines 1–46, revision `5e7e686b`. Its bounded `hoi4.event_inspect` and `hoi4.decision_inspect` returned partial results without helper execution proof; no live game or source patch was run for this disposition.
