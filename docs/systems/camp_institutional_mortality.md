# Institutional population losses in camp administration

Status: implemented in package source with parsed-source scenarios; native engine receipts and historical rate calibration remain unproved.
Acceptance basis: the user's accepted camp-administration contract requires finite, cause-separated actual population losses, distinct experimentation, original responsibility and research awards independent of deaths.

## What the system does

The existing bounded country processor pays maintenance and visits each registered operational camp state at most once per calendar month.
The site first processes custody, assigned-labor and, only for a separately authorized killing-center role, violence losses.
An experiment-linked Auschwitz or Pingfang site then requests an institutional loss from the detainees still alive after those causes.
The request is a monthly fraction of living custody, scaled by this month's actual local maintenance support.
`camp_admin_record_deaths` makes one exact physical state-population debit, measures the accepted result, consumes that many people from the aligned living custody rows, and records the institutional cause once on the site and the original responsible country.
The shared Deaths ledger receives that measured receipt with its physical-debit flag disabled, so it cannot remove the same people again.
If the state floor, death-disabling setting, authority gate or row ledger rejects a request, no institutional loss is recorded.
Release and reform change custody membership only and never restore a death.

German state 88 requires active Auschwitz experiment markers and full or restricted Mengele authority under the Nazi route on or after 1943-05-30.
Permission levels select centrally tuned restricted, limited, full or bypass rates.
Japanese state 328 requires the completed Pingfang bureau, its experiment marker and active Ishii authority without the shutdown flag; explicit Japanese-subject control remains valid while the subject relationship holds.
Both routes require an operational site, reconciled positive custody, a coercive or radical national mandate, at least Development spending and at least 75% paid local support.
The Soviet Gulag design and engineer programs continue to use custody and labor causes and receive no generic experiment loss.
Detention, forced labor, experiments and killing-center violence remain separate roles and causes.

The six-month national research project still advances only after its own support-equipment and Political Power payment, valid site, authority and award-slot checks.
Its one-use bonus remains subject to the two-per-calendar-year and same-category restrictions.
Institutional deaths do not add project progress, increase bonus strength or count as an award.
Because the research slot is finite while an experiment institution may continue, measured institutional losses can continue after the one-use award until policy, maintenance, authority or site status changes.
No new global iteration or routine notification was added.

## Tuning and source balance

`common/script_constants/camp_administration_country_constants.txt` owns `camp_admin_institution_mortality` as monthly fractions of the supported living cohort: German restricted 0.001, limited 0.0015, full 0.002, bypass 0.003, and Japanese Pingfang 0.0025.
At 10,000 living detainees and full support, the production helper's parsed-source scenarios measure respectively 10, 15, 20, 30 and 25 actual people lost in one month.
At the 75% minimum supported ratio, the German full-permission example measures 15 people instead of 20.
Over twelve supported months starting with 10,000 detainees and no new intake, the parsed-source German full-permission case records 234 institutional and 235 custody deaths, leaving 9,531 survivors; the Pingfang subject-control case records 292 institutional and 234 custody deaths, leaving 9,474 survivors. Each accepts 24 separate physical cause receipts and no research progress or award from the deaths.
The existing foundation still caps each request at the living cohort, the exact state floor and its maximum single receipt.
These constants distinguish permission and institutions for gameplay tuning. They are not archival monthly rates or casualty targets.

The [USHMM account of Auschwitz medical experiments](https://encyclopedia.ushmm.org/content/en/article/josef-mengele) distinguishes often lethal experiments from the broader camp's labor, selections and killing-center operations.
The [NARA Japanese war-crimes archive](https://www.archives.gov/iwg/reports/japanese-interim-report-march-2002-1.html) documents the archival basis for a separate Japanese institutional path.
Neither source supplies a monthly mortality fraction for these HOI4 state cohorts, so the rates above require historical sensitivity review rather than being presented as an estimate.
China's combined occupation-cause loss scenario remains separate from this Pingfang-only institutional receipt.

The [32 current source scenarios](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/institutional_mortality_source_results.json) exercise four German permission levels, Japanese subject control and shutdown, support threshold, spending and mandate controls, bad custody rows, capture, reform, closure, death disabling, the population floor, date gate, duplicate month and continuation after the research award.
Nine report-helper replay scenarios verify zero report deaths, request-derived hidden atrocity, persistent mutation or award under healthy, empty, mixed, malformed, closed, captured, unfunded, pre-gate and physical-floor fixtures.
An occupied monthly fixture with original GER responsibility, POL ownership and GER control of state 88 verifies finite custody and institutional receipts targeting GER, committed known-baseline adjustment, and no later report death or outside retirement of that same accepted receipt.
The earlier 23-case snapshot and its generic 100-person legacy-adapter fixture are superseded for current report-helper behavior by these production-helper cases.
They verify one physical debit and one institutional state/country receipt for each accepted request in the parsed production model.
They mock engine primitives and do not establish in-game execution.

## Existing systems and remaining attribution work

The automatic `germany_mengele.10`–`.13` report events retain their existing call sites and choices, while `germany_mengele_register_experiment_deaths` is an evidence-only compatibility helper.
It resets the report-death output and former request scratch values to zero, with no physical casualty transaction, request-derived hidden atrocity or persistent mutation.
The parent explicitly accepted this disposition on 2026-10-03 under the user-approved single bounded monthly camp processor contract.
Continuing institutional harm belongs to the existing monthly mortality owner and finite custody receipt kernel, preserving original GER responsibility when POL owns the occupied site.
The [report reconciliation handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_exact_custody_adapter_2026-10-03.md) and `common/scripted_effects/germany_mengele_effects.md` record the acceptance basis, preserved event source and zero-death replay cases.
No orphan explicit casualty adapter was introduced, and no new report-victim cohort claim is made.
Custody capacity refresh and occupation outside reconciliation call the common package-owned `camp_origin_reconcile_host_membership` observer before origin-specific membership actions.
It observes both net state-population decline and growth in the shared state Deaths counter against a verified opening, so a shared loss can remain visible even when population growth masks net decline or ample population headroom remains.
Those signals are tracked separately because they can overlap, and observing them makes no second physical debit or shared death entry.
For exactly one positive proved row, the existing custody or occupation owner can conservatively retire its exact pending exposure receipt once, without claiming that every retired person died or that the external event identified that cohort's victims.
When mixed origins or an unverified opening make attribution uncertain, the observer freezes the last verified rows and aggregates and pauses origin-specific actions under the user's accepted 2026-10-03 mixed-origin PAUSE choice.
Known measured camp deaths and exact movements adjust their observation baseline only after complete physical and row commit or a complete inverse, preventing a subsequent refresh from treating that same accepted receipt as a new outside loss.
Incomplete inverses quarantine both endpoints with separate raw checkpoints, preserving uncertain rows and historical responsibility without inventing deaths.
Loss masked by growth with no shared Deaths signal remains unobservable through these APIs, and a complete source-labelled mixed-origin restoration provider is unavailable.
Distinct real-world victim attribution and historical rate calibration remain unresolved, while basic owner containment is implemented and the former duplicate routine report burst is retired.
The [basic owner integration handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_observer_owner_integration_2026-10-03.md) records 24 helper and 16 joined parsed-production scenarios and the separate finite-survivor proof.
The subsequent [country/civil handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_country_civil_integration_2026-10-03.md) and final result artifact add eighteen joined source cases, including exact PP/support authorization, selected/co-located programme gates, full-union reform and measured engineer release before deferred benefits under declared mocks.
Ordinary halt preserves a pending completed engineer-release receipt for resumption, while deliberate oversight and parent terminal abandonment clear pending identity without undoing the historical release.
Its four narrow MCP source queries timed out, and these source results establish neither fresh engine execution nor final GUI acceptance.
The parent terminal integration has [two source cases](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_parent_lifecycle_source_results.json) covering ordinary uncertain-closure rejection and per-site terminal containment with frozen rows, one history entry per site and no population/death transaction.
The [three Records projection cases](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_records_projection_source_results.json) include occupation-only uncertain hosts, co-location deduplication and a healthy empty host, without state/death mutation.
The [closed-site archive handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_closed_site_archive_integration_2026-10-03.md) adds thirteen source cases retaining original-authority metadata after active membership is removed.
Known metadata joins Records, filtered Locations and national reform preflight, so a custody-only closed ambiguous host retains its warning and PAUSE rather than disappearing from both predicates.
One-time startup bootstrap registers already initialized sites with their existing immutable authority, without recreating active processing, rewriting the core registry, inferring people or cause, or adding a recurring world hook.
The archive is separate from the capped history journal and source-labelled restoration remains unavailable.
The thirteenth source case corrects a display fallback that warned about unrelated territorial loss after all proved custody had already been released and closed as exact aligned zero-live history.
Explicit structural, ambiguous, unverified-opening, transaction and counter reasons still warn, and action freshness remains false for the new unlabelled interval.
The correction changes no flags, rows, site location, physical quantity, responsibility or victim attribution.
Current source labels custody as `Recorded custody` and scans both custody and occupation registries for uncertainty, without creating an unknown death pool or changing proved causes, origins and responsibility.
Bounded country/civil source integration is implemented, with final parent caller/source/probability review and package acceptance still incomplete.
The [current localisation audit](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/current_localisation_audit_2026-10-03.md) records contextual institution/civil tooltip and blocked-reason repairs, ten tooltip branches, eleven production progress projections, seven short-status getters, four quote-boundary fixtures and nine saved-place getters.
The short labels' installed font advances span 105–215 pixels within the 388-pixel field, while bounded source key coverage and font metrics do not establish final pixels or native eligibility.
Full/narrow GUI inspection plus the 1280 synchronous render in `mcp/origin_pause_gui_2026-10-03/` timed out with `MCP -32001: Maximum total timeout exceeded` under the installed 3.6 session.
A negotiated native-task retry returned `INTERNAL_ERROR` with zero inspection artifacts, and render task `camp_origin_gui_oct3:job_2f4e9326be9be5734aa979f3ec1f6512458df95beb62b1fd646f91f7c7c53498` ended failed with `JOB_WORKER_EXIT`.
No fresh visual acceptance, native engine proof or clean launch is established by those source findings or terminal task states.

The package uses existing Records text and native panel sprites. No new icon or DDS is required: the Records labels and values are in `interface/camp_repression_ledger.gui`, its binding is in `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, and existing window textures remain declared in the current interface GFX files.
The source implementation uses `camp_admin_country_experiment_site_active` in `common/scripted_triggers/camp_administration_country_triggers.txt`, `camp_admin_country_apply_institutional_site_mortality` in `common/scripted_effects/camp_administration_country_effects.txt`, its call in the existing `camp_admin_monthly_state`, central constants, and the evidence-only report compatibility helper.

## Future work

If report presentation uses accepted institutional records, define its reporting window without resubmitting records as physical deaths, hidden atrocity, programme progress or research awards.
Finish final country/civil and legacy caller review and matching Records consumer evidence, and require legitimate source-labelled restoration before resolving sticky mixed-origin uncertainty.
The [USA supervised-release handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/usa_legacy_release_2026-10-03/handoff.md) records implemented positive-receipt/payment/cooldown hardening with seven source groups, while the actual bridge prevents negative pressure and retains derived security reach.
The [foreign-purchase retirement handoff](../plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_foreign_purchase_retirement_2026-10-03/handoff.md) records implemented retirement of three duplicate purchases, inert compatibility helpers and matching 80/75/75 stale native PP refunds with 33 cases.
Both changes retain unresolved AI and native payment/timer evidence, without replacement casualties, foreign transport or restoration machinery.
Compare dated site occupancy and measured cause receipts with archival evidence without tuning one cause toward a broad national death total.
Verify native population, Records, death-ledger and research-award behavior through the user-owned game validation surface or a compatible supplied save.

## Engine references read for this change

The connected `hoi4.reference_context`, `reference_search`, `reference_read` and `source_lookup` routes were absent from this task's callable list, so the pertinent local sections were read directly.
Installed `documentation/script_concept_documentation.md` lines 216–246 (SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`) and `common/script_constants/documentation.md` lines 1–31 (`e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`) define shared fixed-point constants and their `constant:` use.
Installed `documentation/effects_documentation.md` lines 7820–7840 (`2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`) and `documentation/triggers_documentation.md` lines 2110–2131 (`7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`) cover temporary-variable input and variable comparisons.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` lines 425–451 (`62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`) describes variable-scope and temporary-variable behavior; offline `Triggers - Hearts of Iron 4 Wiki.md` lines 256–268 and 563–574 (`abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`) covers state scope and `check_variable`.
Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` lines 254–263 (`18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`) distinguishes an event's country `ROOT` from a nested state and its owner; the adjacent `germany_mengele_effects.txt` percent-loss route already names `ROOT` as its death-ledger target.
Installed vanilla `common/scripted_effects/SIA_scripted_effects.txt` lines 761–778 (`ac1e86a0ffe5e46f7083318c584993667eaafb3cd1585e15db71fbd51fa276af`) demonstrates `constant:` values in scoped effects. The existing Chaos Redux `camp_admin_record_deaths` is the primary receipt precedent for this package.
