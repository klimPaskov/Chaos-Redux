# Host origin ambiguity containment architecture

Disposition: accepted and queued for the pause policy, with the implementation architecture proposed for parent review.
Acceptance basis: the direct user decision of 2026-10-03 supplied by the parent and recorded in `../handoff_prompt_2026-10-03.md` chooses a sticky pause of origin-specific actions after an unlabelled outside loss threatens multiple living original cohorts, until a source-labelled receipt restores provenance.
Unknown-origin continuation pools, proportional row subtraction and newest-first attribution across original cohorts are rejected by that decision.
This handoff is design only and changes no gameplay, costs, AI, visual layout, core accounting or shared registry.
The parent owns implementation, integration, acceptance and the final completion claim.

## Current-source findings

The inspected production source has already diverged from the September audit.
`common\scripted_effects\camp_administration_occupation_effects.txt` contains `camp_occ_distribute_unknown_origin_removal`, which subtracts proportions from original rows and writes `camp_occ_unknown_origin_removed_k` and country unknown-origin totals.
`common\scripted_effects\camp_administration_effects.txt` contains the same policy in `camp_admin_consume_outside_rows` under `camp_admin_origin_estimated`.
These paths must be replaced, not retained as the implementation of the pause policy.
The paired effect documentation still describes newest-first outside retirement and requires reconciliation with the actual accepted behavior.
The Records adapter `GetCampAdminUnknownOriginNote` and `camp_admin_records_unknown_origin_note` explicitly describe unknown totals and estimated remaining origins, so they also require replacement.

Occupation observation currently uses the largest of net population decline, new territorial Deaths and occupation membership headroom shortfall.
Custody capacity reconciliation observes only `camp_admin_detainees_k > camp_admin_population_headroom_k`.
A custody host can therefore lose people, including deaths recorded by the shared territorial ledger, without reaching that shortfall.
Growth can hide a physical decline even when shared Deaths records the loss.
Neither aggregate carries an original cohort identity.
The shared `apply_exact_state_civilian_population_loss` and its paired documentation confirm one physical-loss contract with no occupation-root, custody-row or original-state field.
Its `state_civilian_population_loss_applied` output is a calculated request after clamping and rounding, so existing package code correctly measures before and after population rather than treating that output as an engine receipt.

Occupation rows belong to their immutable responsible country and align IDs, root IDs, originals, hosts, authorities, profiles, live amounts, deaths, removals, releases, movements and statuses.
Custody rows belong to the physical state and align IDs, originals, authorities, occupation roots, live amounts, deaths, arrival deaths, releases, removals and statuses.
State `camp_occ_remaining_k` and `camp_admin_detainees_k` are the current reservations used by admission and workforce logic.
Freezing uncertain rows requires preventing those snapshot quantities from being used as verified living workers or transaction receipts.
`camp_admin_site_rows_reconciled` currently checks shape, authority and equality of rows to the aggregate, but that equality does not establish provenance after an outside loss.

Existing exact occupation-to-custody transfers already prove the selected source row and preserve original state, authority and occupation root through measured source debit, destination credit and custody bind.
`camp_occ_rollback_custody_transaction` inverses the bind before attempting physical undo and retains `camp_occ_custody_rollback_failed` on mismatch.
That safety order must remain intact.
Existing destination import proof establishes only the newly arriving row and cannot resolve an earlier outside loss among existing rows.
The generic occupation-to-occupation transaction has no named production caller, but its public contract must receive the same guards before future use.

## One physical-host observer

Use one package-owned observer for both row families at a physical host.
Independent family observers miss a host with occupation origin A and custody origin B, even when each family separately reports only one origin.
They can also observe each other's known package death as an outside loss and retire exposure twice.
The observer scans only the host's existing state custody arrays and the existing immutable authority's occupation arrays filtered by current host.
If both registered authorities differ, inspect each existing authority's bounded rows and keep the authority identities distinct.
Do not add a global cohort registry or recurring world scan.

Treat an original cohort as its immutable lineage, not a current array index.
Occupation lineage includes original state, original authority and root ID.
Custody lineage includes original state, original authority and occupation root, with a native custody row ID distinguishing a root-zero local admission when needed.
Also retain the occupation versus custody membership distinction because a territorial loss cannot identify which reservation suffered it.
Distinct original states certainly require containment.
Distinct roots or authorities under one original state require containment for exact row actions too, because the state name alone cannot prove the selected root's survivors.
Several row fragments of one lineage do not supply proof that an unlabelled loss belongs to one particular fragment.
The one-origin conservative control applies only where the affected membership and row are uniquely attributable for the operation being requested.

At each observation, compute three separate facts in state scope:

1. `net_decline_k = max(previous_population_k - state_population_k, 0)`.
2. `shared_loss_k = max(chaos_state_civilian_deaths_total - previous_shared_deaths_people, 0) / people_per_k`.
3. Current reservation/headroom inconsistency using the existing physical floors and population-share limits.

If either of the first two facts is positive and multiple living lineages or memberships occupy the host, set a sticky `camp_origin_ambiguous` state flag before any row subtraction.
A headroom inconsistency also fails closed when the affected rows cannot be identified.
Record the reason separately rather than treating a capacity mismatch as a camp death.
Malformed, missing or over-limit arrays fail closed as unresolved records and cannot be treated as a single origin.
Retain the last verified row amounts, identities and historical cause totals intact.
Record host observations separately and advance the observation baseline after recording the interval so a second observation is inert.
Natural growth never clears ambiguity.
Neither a later fall to one visible row nor a closed site proves that the lost cohort has been identified.

The observer must run before any relevant origin action and before ordinary capacity refresh can mutate membership.
Availability can use a read-only preview of the same pending-signal and lineage checks for an immediate blocked reason.
Execution must repeat observation and validation even if the prior availability check passed.
Do not rely solely on the monthly pulse or a GUI display refresh to set the flag.

## Aggregate observation and physical accounting

Containment never calls a population-changing effect, `chaos_meter_register_deaths` or a cause/death projection.
It never subtracts the same host loss once from occupation and again from custody.
Keep net decline and shared Deaths deltas as separate territorial observations because they can overlap.
For an interval summary, their maximum is an observed outside-loss signal, not an exact number of original-cohort victims.
Keep current headroom shortfall separate and do not accumulate the same persistent shortfall on every refresh.
Do not convert observed amounts into a transferable unknown-origin population pool.

While ambiguous, `camp_occ_remaining_k`, `camp_admin_detainees_k` and aligned row live amounts retain the last verified reservation snapshot.
They must be labelled uncertain and denied to admission, transfer, mortality, release, conversion and supported-workforce consumers.
Physical state population, building capacity and past accepted cause totals remain observable.
Capacity may be refreshed arithmetically, but it cannot automatically consume origin rows while ambiguity is set.
An ambiguous site's productive worker contribution and worker-dependent project progress must not use the frozen custody snapshot as verified current labor.
Pause those contributions through the existing economy and institution validity gates and clear the affected site's current output modifiers through `camp_admin_clear_state_output`.
Retain paid project progress and its existing cancellation rules, and let the parent keep the existing maintenance and non-worker policy design.

For the unique one-origin control, retain the documented conservative exposure retirement bounded by current living membership and observed physical constraints.
It changes outside-removal exposure records, not death cause totals or responsibility.
It still supplies no claim that every territorial death belonged to that origin because unrelated residents can share the state.
Do not extend that control into newest-first selection among distinct roots or original cohorts.

Every known package physical transaction needs one common baseline adjustment for all affected families.
Observe the source and destination before quoting or mutating anything.
After a successful death, adjust the observed population baseline by the measured physical debit and the shared Deaths baseline by the measured shared receipt.
After a successful movement, adjust source and destination population baselines by their measured debit and credit, with no shared Deaths addition.
Then observe any residual against the adjusted baseline.
This preserves any unexplained residual rather than wiping it by blindly copying the current total over an older baseline.
The existing family observation fields can mirror the canonical host baseline during migration, but they must no longer independently retire another family's receipts.
Never run the outside-loss observer between physical transfer stages and metadata commit because that intermediate debit is a known transaction in flight.
Successful inverse must account for the measured inverse receipts exactly once before normal observation resumes.
A failed inverse retains both the existing rollback quarantine and host provenance quarantine, with the measured residual preserved.

## Proposed helper map

New helper names below are proposed contracts, not implemented APIs.
Put package-owned helpers in `common\scripted_effects\camp_administration_origin_effects.txt` with paired `camp_administration_origin_effects.md`, and read-only predicates in `common\scripted_triggers\camp_administration_origin_triggers.txt`.

| Helper | Scope and inputs | Outputs | Side effects and direct call sites |
|---|---|---|---|
| `camp_origin_initialize_host` | Actual state, existing registered row families | Initialized canonical observation baseline | Idempotent state variables and flags, called at accepted occupation registration and custody initialization before new membership changes |
| `camp_origin_inspect_host_rows` | Actual state, regular current-host target, existing authority scope pointers | Temporary row validity, distinct lineage/membership result, verified occupation and custody sums | Read-only aligned scans, used by observer, preview, restoration and transaction preflight |
| `camp_origin_observe_host` | Actual state, canonical baseline | Temporary net decline, shared loss, current shortfall and ready/rejected result | Sets sticky ambiguity and records host evidence, replaces origin guessing in `camp_occ_reconcile_external_population` and `camp_admin_refresh_capacity`, runs before action execution and lifecycle closure |
| `camp_origin_host_provenance_ready` | State trigger with explicit initialized baseline and read-only pending-signal preview | Boolean availability result | No persistent writes, used by exact row proof, reconciled custody predicate, source/destination imports, release and reform gates |
| `camp_origin_country_cohorts_ready_for_reform` | Country trigger, bounded union of existing custody sites and occupation hosts | All affected hosts ready or rejected | No persistent writes, used by every national reform whose effect calls both custody reform and `camp_occ_close_country` |
| `camp_origin_adjust_known_receipt` | State, complete one-shot measured signed population delta, shared Deaths receipt and transaction identity | Accepted or rejected adjustment result | Adjusts canonical baselines by known amounts, consumes inputs, called after committed package deaths, both endpoints of transfers and validated physical inverse |
| `camp_origin_apply_restoration_receipt` | Actual ambiguous host, trusted complete source-labelled receipt covering its unresolved epoch and every affected row | Accepted/rejected result and receipt sequence | Ledger correction only after full preflight, consumes all request fields, clears ambiguity only after complete successful restoration and fresh baselines |
| `camp_origin_terminal_containment` | Actual state and explicit capture/annexation/terminal closure reason | Administrative closure with unresolved provenance retained | Stops current outputs and bounded operational references, preserves uncertainty and immutable historical records, called by package close-site and occupation close-state branches |
| `camp_origin_refresh_country_projection` | Existing authority country, bounded existing site and occupation-state lists | Current ambiguous host count and Records state | Country display projection only, deduplicates a co-located host, called at existing package interface/monthly/lifecycle seams |

No new helper should be shipped without the listed direct call sites and matching documentation.
The restoration provider does not currently exist in production, so its implementation must either be integrated with a real source-labelled provider or remain explicitly queued rather than become an orphan recovery button.

## Persistent data and constants

Proposed state flags are `camp_origin_observation_initialized`, `camp_origin_ambiguous` and `camp_origin_ambiguity_terminal`.
Ambiguity has no expiry.
Normal state variables are `camp_origin_observed_population_k`, `camp_origin_observed_state_deaths_people`, `camp_origin_observation_sequence`, `camp_origin_ambiguity_sequence`, `camp_origin_unresolved_net_decline_k`, `camp_origin_unresolved_shared_loss_k`, `camp_origin_current_shortfall_k`, `camp_origin_last_verified_occupation_k`, `camp_origin_last_verified_custody_k` and `camp_origin_last_restoration_sequence`.
Unresolved observation counters describe host evidence and cannot be spent, transferred or used as a new cohort.
Country projection variables are `camp_origin_ambiguous_host_count` and, if needed by Records, separate territorial observation totals with deduplication by host.
Receipt, scan and request temporaries must use an independent prefix so nested country/state scans do not overwrite `camp_occ_active_row_index`, selected custody row or in-flight bind receipts.

Reuse existing `constant:camp_admin_value.zero`, `one` and `people_per_k` for shared arithmetic.
Retain each family's existing physical floor and maximum receipt without unifying their different values as an incidental balance change.
Add a package `camp_origin_value` category only for genuinely new shared schema tokens, including a documented `maximum_row_scan = 1000` safety bound matching the engine effect-loop limit.
This is a fail-closed safety bound, not permission to process an incomplete prefix of a larger row registry.
Add any new Records history-kind IDs to the existing package history category after checking unused IDs.
Do not add AI weights, loss fractions, random selection, an ambiguity timeout or a tuning threshold that tolerates an unexplained whole-person loss.
Historical loss-rate balance remains parent-owned.

The narrowest terminal implementation retains frozen row amounts and sets host terminal flags rather than pretending uncertain survivors reached an ordinary released status.
If the parent elects an explicit `unresolved_closed` row status for clarity, it must update every row validator and live-sum consumer in the same tranche.
That status must preserve the frozen quantity as historical uncertainty and must not contribute to active membership, deaths, releases or movements.
The host flag solution avoids an unnecessary full status migration.

## Required action and lifecycle gates

| Existing surface | Required guard and result |
|---|---|
| `camp_occ_prove_active_row`, `camp_occ_record_deaths`, `camp_occ_state_can_pulse` | Host observation and provenance readiness before the physical debit, with a second check after reconciliation and before the debit. Return actual death zero and consume request inputs on rejection |
| `camp_occ_transfer_survivors_exact`, `camp_occ_preflight_custody_source`, `camp_occ_transfer_to_custody_exact` | Observe both endpoints before physical stages, require clear host provenance and existing exact row/authority/array proof, reject ambiguous source or destination before any physical mutation |
| `camp_occ_refresh_manual_transfer_source`, manual Auschwitz order and dated Łódź waves | Exclude ambiguous sources and destinations from selection and revalidate execution. Preserve the existing payment-after-success rule and clear stale selected source/pending wave references |
| `camp_admin_admit_detainees`, `camp_admin_preflight_import`, `camp_admin_bind_import` | Reject ambiguous hosts. A new proven arrival cannot clear an older ambiguity. Keep existing fractional request, capacity, authority and bind guards |
| `camp_admin_record_deaths` and `camp_admin_consume_rows` | Observe and gate before the sole physical debit. Block every row death on an ambiguous host, including selected positive ID, zero-selected generic custody/labor/violence/institutional death and bound-row arrival violence. Defend the row-consumer helper against a direct bypass |
| `camp_admin_release_detainees`, `camp_admin_release_survivors`, `camp_admin_release_selected` | Reject origin-tagged survivor release while ambiguous, with actual released zero. Do not set census-intake closure, suspended-success history, settlement flags or rewards from a failed release. Release changes membership only and never adds population |
| `camp_admin_site_rows_reconciled`, selected release, Soviet service-release readiness and country release loop | Extend readiness beyond array equality to provenance. Country release must preflight every affected site again at execution before releasing from any site or settling national policy |
| `camp_admin_reform_site`, `camp_admin_begin_reform`, generic/country/civil reform and their country preflights | No release, civilian target, quota settlement, civilian conversion or completion reward derived from uncertain snapshot amounts. Preserve all-or-nothing preflight and paid-action rejection/refund behavior |
| Country institutional awards with partial engineer-release branches | Engineer release requires positive release proof before its cohort completion marker. Ordinary awards and costs remain governed by the owner, and worker-dependent site validation cannot use uncertain detainees |
| Colonial direct full-site release and legacy dismantlement paths | Trace `camp_repression_colonial_country_effects.txt` direct release, `camp_rework_legacy_closure_site_can_begin`, `camp_rework_site_can_complete_dismantlement` and integration reform/close adapters. An uncertain release cannot satisfy custody receipts or allow payment/rewards to survive rejection |
| Workforce/output consumers | `camp_admin_has_supported_workforce`, state economy refresh, project target/work/progress and institution site validity require proven survivors. Pause the affected site's worker contribution while retaining already accepted project progress |
| Voluntary occupation/site closure | Preflight before a claimed survivor release. No original-cohort release totals or reform-derived workforce are published from ambiguity |
| Capture/control loss and terminal annexation | Call terminal containment before existing unregister/teardown removes active processing. Stop operations and output without claiming a measured origin release, changing population or writing Deaths. Preserve original authority, cohort roots, past deaths and ambiguity evidence |
| Reopening | A same-authority reopen cannot clear host ambiguity or reseed uncertain membership. A new institution phase needs its own accepted design and cannot overwrite this record |

Keep `camp_admin_site_is_operational` as the authority/infrastructure lifecycle predicate where it is needed to observe or close an uncertain site.
Making that broad predicate false can accidentally hide the site from Soviet all-affected-site preflight and terminal cleanup.
Use separate provenance readiness for actual cohort actions and supported workforce.
Country all-site guards must include ambiguous operating sites as affected targets and reject the operation, not filter them out and release from the remainder.
National reform also has to preflight occupation-only hosts in `camp_occ_states` because existing `camp_admin_country_sites_ready_for_reform` checks custody sites alone, while the successful country effect closes occupation cohorts too.
Execution code must not proceed with deductions or rewards merely because a broad country availability trigger passed earlier.

The control-change bridge is `genocide_on_state_control_changed` in `common\scripted_effects\genocide_crisis_effects.txt`, which already enters the actual changed state through `FROM.FROM` and calls `camp_occ_on_state_control_changed`.
Keep that scope contract and perform containment inside existing package adapters.
The terminal country path is `camp_rework_on_country_annexed` in `camp_repression_rework_effects.txt`, which calls `camp_admin_integration_close_country` before removing active arrays and tearing down infrastructure.
Contain uncertain hosts before that removal, including both `camp_active_site_states` and `camp_occ_states` through their existing bounded adapters.
Do not add a new recurring hook.

## Verified restoration receipt

Existing aggregate shared Deaths and state population snapshots cannot supply this receipt.
No production provider inspected here labels an earlier external loss with the complete original-cohort distribution.
That is a recovery-provider gap, not permission to infer a distribution or add an administrative clear button.
A source-labelled receipt for a new incoming cohort proves the new cohort only and must be rejected as restoration for an old ambiguity epoch.

The proposed receipt must identify the actual host, unresolved observation epoch, trusted source adapter and monotonic receipt sequence.
It must account for every previously live affected occupation and custody row by family, immutable row ID, original state, original authority, root and before/after amounts.
It must explicitly identify unaffected rows and any loss outside the package cohorts rather than forcing all territorial losses into those cohorts.
Every current row must be covered exactly once, and an append, movement, rollback or later outside observation after the receipt's snapshot invalidates its coverage.
A boolean proof token, matching aggregate total, valid array shape or one correctly labelled row does not establish complete restoration.

Preflight validates all identity tuples against the frozen registry and verifies nonnegative surviving amounts, no survivor amount above its verified before amount unless a separate exact accepted incoming receipt explains it, aligned arrays, no duplicate IDs, current authority handling and physical reservation limits.
For each row, `before + accepted incoming - accepted outgoing - proven package deaths - labelled external membership removal - labelled release = restored survivors`.
The receipt must reconcile the observation interval and territorial-loss evidence without treating net change and Deaths as additive deaths.
If unrelated residents account for an observed loss, explicitly validate that portion in the trusted provider's measured transaction rather than deriving it as a convenient residual.
Validate the full vector first, then apply all ledger corrections atomically through the owner families.
Do not write population, shared Deaths, camp cause totals or transfers because those physical effects have already occurred.
Keep external membership correction distinct from camp cause attribution.
On any rejection, keep every row, ambiguity flag and historical total unchanged and consume all one-shot receipt inputs.

Only after a complete successful receipt updates all affected current membership sums and leaves no uncovered observation interval may the helper set fresh canonical baselines, record the receipt sequence and clear `camp_origin_ambiguous`.
A restoration receipt does not erase the history of uncertainty and does not reopen a terminally closed site.
No legitimate caller currently supplies that full receipt, so spontaneous restoration remains unavailable until the parent integrates a provider with documented measured source evidence.
Do not ship a helper that clears the flag from a caller's `proven = 1` declaration alone.

## Targets and cleanup

Use regular event targets for the current host and actual transfer or receipt source/destination in the same effect chain.
Save each target while already in its actual state scope.
Retain existing `camp_occ_transfer_destination` and `camp_occ_custody_destination` contracts.
Do not create a global event target for a host or cohort.
Persistent scoped variables and immutable row IDs carry the durable record.
Restore or use a separate host target name so origin inspection cannot overwrite an in-flight transaction target.

Consume restoration request arrays, selected IDs, proof fields, known-receipt adjustment fields and transient result defaults on success and failure.
Do not clear the sticky ambiguity flag in initialization, imports, bind, capacity refresh, growth, monthly resets, capture, annexation, reopening or ordinary inverse cleanup.
Failed inverse preserves the transaction receipts and both affected endpoint quarantines before the regular targets expire, so recovery does not depend on an expired pointer.
Terminal cleanup cancels existing project/program references to the host, clears current economic modifiers and active selections, and makes future operational callbacks inert.
Preserve frozen row history, immutable authority, past cause totals, observation evidence and uncertainty flags after unregistering active processing.
Never transfer historical responsibility to the conqueror.
Repeated terminal cleanup is idempotent and changes no population, Deaths or survivor release totals.

## Files and presentation handoff

Implementation owners should expect changes to the new origin effect/trigger files and paired effect documentation, the existing occupation/foundation effect and trigger files, integration adapters and their paired documentation, country/civil/colonial release or reform guards, and the narrowly affected `camp_repression_rework_triggers.txt` custody-receipt guards.
Use `camp_administration_constants.txt` for the small new package schema category if necessary and `camp_administration_occupation_constants.txt` only if an occupation-specific schema token is truly needed.
Do not change the shared loss API, `chaos_meter_effects.txt`, core on-actions or shared registry definitions.

Replace the existing unknown-origin Records note through `common\scripted_localisation\camp_administration_ui_localisation.txt` and `localisation\english\camp_administration_ui_l_english.yml`.
Suggested stable keys are `camp_admin_origin_records_paused`, `camp_admin_origin_action_blocked` and `camp_admin_origin_terminal_uncertain`.
Suggested player wording is: "Losses at this location do not identify the people affected. Figures for each place of origin remain uncertain, and orders that depend on those figures are paused until their survivors are accounted for."
For terminal records: "The site has closed. Surviving records leave the losses and remaining people by place of origin unresolved."
Preserve exact past accepted camp cause totals and distinguish them from territorial observations.
Country totals that include an uncertain host must identify the uncertainty rather than presenting the frozen amount as a verified current count.
Add the precise blocked reason to affected native decisions and existing Locations controls through owner localisation adapters, without creating a new visual layout or shared UI framework.
The parent owns GUI scenario inspection, matching renders/comparison and final text fit after implementation.
Existing sprites and the current window can be reused, with no new icon or art request required by this containment.

## Migration order

1. Preserve an immutable current-source snapshot and call-site map, then introduce the common host baseline and read-only row inspection contract.
2. Replace both unknown/proportional outside-consumption branches with host observation and frozen ambiguity. Retain conservative one-origin handling only for uniquely attributable membership.
3. Add pre-action and post-observation guards to physical death, both transfer endpoints, bind, release and reform consumers before enabling the new observer in the monthly seam.
4. Route all accepted package death, movement and inverse receipts through one canonical known-receipt adjustment, preserving the existing one-debit/one-projection order.
5. Add terminal containment to existing close/unregister/control-loss/annexation adapters before their active lists are cleared.
6. Replace Records unknown-pool wording and expose the blocked reason in the existing owner presentation.
7. Exercise the source matrix below against parsed production helpers, then complete the owning MCP before/after inspections and probability audit where availability changes an AI selection surface.

If an inherited record carries `camp_occ_origin_estimated`, `camp_admin_origin_estimated` or nonzero unknown-origin removal totals from the rejected proportional implementation, set containment without re-running a physical debit.
Do not reconstruct earlier exact rows from the current aggregate or erase existing historical evidence.
The old estimate cannot be promoted into the last verified cohort snapshot.
Such provenance recovery requires an immutable earlier verified row receipt or the full trusted restoration vector above.
This is a data-integrity rule, not a live-game or save compatibility claim.

## Source-test matrix required for implementation

These are planned parsed-production tests with mocked engine primitives, not tests run by this design handoff.
Instrument physical debit/credit calls, shared territorial entries, row mutations, reservation changes, payment/settlement receipts, and known baseline adjustments.
Record the complete state/country row vectors before and after each scenario.

| ID | Scenario | Required result |
|---|---|---|
| O01 | Occupation host holds A=10k and B=10k, population 100k. Outside loss makes population 90k and shared Deaths +10,000 | Sticky host ambiguity, original rows remain last verified 10k/10k, no invented original loss/death/release, observation recorded once, package physical calls and shared entries zero |
| O02 | Repeat O01 observation and then add 30k unrelated growth | No repeat observed loss, flag remains set, every origin transaction remains blocked |
| O03 | Same A/B rows, population changes 100k to 105k, shared Deaths +10,000 | Growth-masked loss sets ambiguity through Deaths delta, with zero second debit or shared entry |
| O04 | Custody A=10k/B=10k, population 200k to 190k, both totals still below capacity and 20 percent headroom | Independent outside observation detects ambiguity despite no custody shortfall. No proportional row subtraction |
| O05 | One occupation A=10k and one custody B=10k share one host | Common detector marks both memberships unavailable. One host observation is not counted as a full removal from each family |
| O06 | Unique one-origin occupation A=20k, outside decline/Deaths=10k | Conservative exposure retirement leaves at most 10k, outside-removal record only, no camp cause/death or second physical change |
| O07 | Same original state but distinct roots, or native root-zero custody admissions with distinct immutable rows | Exact row actions fail closed when the lost membership cannot be uniquely established |
| O08 | Exact source A transfer of 5k to a clear destination already holding B=10k, then 1k selected-row destination death | Source debit=5k, destination credit=5k, original/root/authority preserved, arrival row A later has 4k, death has one physical debit and one shared entry. Repeated observers see no outside loss from these exact receipts |
| O09 | New unrelated incoming transfer attempts to use an already ambiguous host | Reject before physical debit or bind, return zero committed receipt, preserve ambiguity. A valid incoming receipt cannot clear the old epoch |
| O10 | Destination/source outside loss arrives after a valid quote but before execution | Fresh execution observation blocks mutation and owner payment/settlement. National multi-site release preflights all sites before releasing any |
| O11 | Release from clear exact rows, and the same request at an ambiguous host | Clear release consumes only proven membership with zero physical creation and zero shared Deaths. Ambiguous release returns zero, with no success history, intake-closure flag, repeated settlement or civilian target |
| O12 | Valid transfer bind followed by failed source commit, exact inverse succeeds | Bind inverse first, then measured physical undo, original row unchanged, voided custody addition only, no Deaths and no false outside signal after known-receipt accounting |
| O13 | Inverse bind or either physical inverse fails | Preserve residual and sticky rollback plus host quarantines at both affected endpoints. No second destructive debit under a live bound row, no retry, no fabricated source restoration |
| O14 | Capture or annexation while ambiguous, followed by repeated cleanup | Operational outputs and selected references stop before active unregister, ambiguity/history/root/authority remain, no population change, shared entry or claimed origin release. Repeat cleanup is inert |
| O15 | Partial, wrong-host, wrong-epoch, wrong-authority, duplicate-row, missing-row, replayed or unrelated-incoming restoration receipt | Reject atomically, no row mutation, no flag clear, no population or shared Deaths mutation |
| O16 | Complete trusted restoration vector labels 10k external removal from A, B unaffected, and covers every pending observation | A/B current amounts become proven 0k/10k with matching family aggregates, historical cause totals unchanged, no physical or shared entry, receipt sequence published once, flag clears only after full commit |
| O17 | Receipt covers one earlier loss but a later unlabelled loss or row append changes the snapshot | Coverage becomes stale and ambiguity remains, even if the receipt's total equals one current aggregate |
| O18 | Malformed parallel arrays, missing host authority, uninitialized legacy observations or row count above effect-loop safety bound | Fail closed with a specific records reason, no truncated scan treated as proof, no physical action or origin fabrication |
| O19 | Custody package death at a host also holding occupation rows, followed by occupation reconciliation, and the reverse ordering | One physical debit and one shared territorial entry per accepted death, canonical adjustment prevents sibling-family double retirement or false ambiguity |
| O20 | Unlabelled loss is masked by growth and absent from shared Deaths | Report undetectable from available snapshots. Do not claim a test or helper recovers information that does not exist |

## Evidence and limits

Evidence is archived beside this report under `origin_ambiguity_mcp_2026-10-03\`.
`source_manifest.json` records exact SHA-256 identities and immutable snapshots for the principal inspected package sources, so concurrent worktree edits do not silently change this handoff's baseline.
The direct installed MCP was checked afresh through `C:\Users\klimp\Documents\Projects\hoi4-agent-tools\dist\bin\stdio.js` using SDK 1.30.0 from that installation.
Initialization reported server `hoi4-agent-tools` version 3.6.0 and successful live tool/schema listing, archived in `server_and_schemas.json`.
The direct client uses ordinary synchronous calls, with no native tasks requested.
No `hoi4.script_validate` route was exposed in that live listing.

`hoi4.reference_context` and targeted `hoi4.reference_search` calls succeeded, and the relevant revision-bound sections were read with `hoi4.reference_read`.
The context had no `missing` or `omittedSources`, but many generic context matches were navigation sections, so syntax coverage relies on the targeted reads rather than the context summary.
The optional `script_doc` source kind was unavailable with zero files, while installed `game_doc` and offline `wiki` sources were available.
Search for `add_state_population` returned no source and is not treated as a supported command.
The physical state-loss helper and installed `add_manpower` section were inspected directly instead.

Installed references read include `documentation\dynamic_variables_documentation.md` 1168-1171 at revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, `documentation\triggers_documentation.md` 4827-4842 at revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, and `documentation\effects_documentation.md` 6496-6504 at revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Installed script constants were read in `documentation\script_concept_documentation.md` 216-222 at revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` and `common\script_constants\documentation.md` 1-34 at revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` reads cover flags 102-126, regular event targets 303-328 and scoping 444-480 at revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Additional local scope/array/on-action sections and vanilla source precedents are recorded in `local_reference_evidence.json`.

The bounded `hoi4.map_inspect` request for state IDs 87 and 88 with `lookupOnly = true` and `includeOverview = false` timed out at MCP error -32001 after 120,000 ms.
Map/state topology evidence is therefore blocked for this run, and local state-ledger source review does not replace that missing MCP result.
No map topology or mapmode change is proposed.
The remaining bounded inspection outcomes are recorded in the final inspection appendix below.

No gameplay implementation, source-test execution, probability balance change, render comparison or runtime validation was performed by this design task.
Availability changes can affect AI candidate selection even when numeric weights stay fixed, so the parent should preserve the baseline decision sources and run the required probability auditor comparison against matching named clear/ambiguous scenarios after implementation.
Source-only tests cannot establish live event scopes, effect-loop execution, dynamic tooltip pixels, clicks or save persistence.
Loss masked by both growth and absent Deaths is undetectable from the existing aggregate API.
Source-labelled recovery remains blocked on a complete legitimate provider.
No unapproved attribution fallback or gameplay simplification is proposed.

### Final inspection appendix

| Route | Current result and evidence |
|---|---|
| `hoi4.map_inspect` | State 87/88 bounded lookup timed out with -32001 at 120 seconds. Exact request is archived in `map_failure.json` |
| `hoi4.source_lookup` | Each targeted lookup for `camp_occ_reconcile_external_population`, `camp_admin_refresh_capacity` and `apply_exact_state_civilian_population_loss` timed out with -32001 at 45 seconds. Exact requests are in their `source_*.json` files. Local inspected snapshots provide source evidence only |
| `hoi4.event_inspect` | File selector `events/camp_administration_country_events.txt`, helper expansion disabled, bounds 80 nodes/100 edges. Returned `EVENT_INSPECTED_PARTIAL` at revision `fe29c3107ffb1b915f40bec0d44cfb169d2661c742fa682aa5d513e53d9938fb`. The report is a large-scan summary with `complete = false`, no helper catalog and deferred helper/lifecycle analysis. It does not validate the proposed helper design |
| `hoi4.decision_inspect` | The first inspect request was rejected with -32602 because this route requires declared scenarios despite an optional-looking live schema. The corrected SOV source-inspection scenario request timed out with -32001 at 45 seconds, archived in `decision_with_scenario.json`. Current eligibility remains unproved by this route |
| `hoi4.gui_inspect` | The first window-only request was rejected with -32602 because `windowName` and `scenario` must be supplied together. Retried with the existing declared Records fixture `records_1944_10_01_source_sensitivity_1920.json`, then timed out with -32001 at 45 seconds. Archived in `gui_with_scenario.json`. No GUI layout or render evidence is claimed |

The event scan resource is `hoi4-agent://workspace/camp_origin_architecture_oct3/artifact/527b5c4ec3b2be80788c7b498003fa058a7636829691516b7dca41d0749115ea/6db4e82367fabdbd7216909638669cf17b27c81710c6f0628637519e4d370b28/event-scan-fe29c3107ffb.json`.
Its complete returned 170,100-byte scan envelope is archived locally as `event-scan-fe29c3107ffb.json` with the same SHA-256.
The linked 89,579,713-byte graph resource is retained by identity in `events.json` and its preserved direct-server temporary path is recorded in `event_artifact_retention.json`, without claiming that the large graph was reviewed completely.
The scan reports 386 source files and a truncated 256-entry source-hash inventory, while the compact inline file list retains only 64 paths.
Those coverage limits cannot establish all linked camp helpers or lifecycle behavior.
The independent principal package snapshots in `source_manifest.json` showed zero source drift when this report was finalized, recorded in `source_drift.json`.

Files created by this task are this architecture report and the bounded evidence directory, including requests, results, server schemas, principal source snapshots and local reference excerpts.
Gameplay helper implementation, call-site edits, constants, cleanup logic, localisation changes and source tests are queued for the parent.
Skills used are `chaos-redux-state-ledgers`, `chaos-redux-subagents`, `chaos-redux-events` and the applicable release/GUI-action integrity guidance in `chaos-redux-decisions-missions`.
No skill was created or updated because this task did not implement or establish a new reusable workflow beyond the existing state-ledger contract.
