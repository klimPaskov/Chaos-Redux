# Event014 Larder logistics implementation handoff

Disposition: implemented source fix, ready for parent review and the mandatory auditor comparison.
Acceptance basis: the parent authorized source application after auditor `01a10385` delivered ten frozen source snapshots and eight named partial-baseline fixtures.
The parent accepted `1200 + 100 * actual controlled states + 50 * existing administrative contract index`, the existing 5000 ceiling, ordinary cap 2000, dispatch/received accounting, post-annex finalization and the separate generation guard.
This is not Event014-wide completion, engine acceptance, GUI acceptance or an AI balance signoff.
No Git/index/commit, game, log, workbook, asset, portrait, model or GUI-layout action was taken.

## Changed files and ownership

| File | Owned change |
| --- | --- |
| `common/scripted_effects/014_cannibalism_effects.txt` | Capacity API, frozen-capital capture/quote, one-shot dispatch/received commit, opening assignment, all clamp/finalization hooks, caller output ownership, profile integration, derived-field initialization/cleanup and exact opening last-state migration provenance. |
| `common/script_constants/014_cannibalism_constants.txt` | One new fixed-point `cannibalism_larder_logistics` tuning group. Existing tuning values retained. |
| `common/scripted_triggers/014_cannibalism_triggers.txt` | Positive expected host generation/current actor equality, private quote/commit context and opening-only migration-source provenance. |
| `localisation/english/014_cannibalism_l_english.yml` | Only existing `cannibalism.gui.larder.tt` and `cannibalism.gui.global_larder.tt` text, including the current effective capacity and overflow loss. |
| `docs/events/014_cannibalism/larder_logistics.md` | Owner API contracts, transfer/finalization lifecycle, fifty-flag administrative mapping, rationale, reference proof, icons and validation limits. |
| `common/scripted_effects/chaosx_dynamic_effects.md` | One Event014 owner API index link, with private helpers retained in the Event014 owner file. |

The shared index also received an independent Event012 recovery/epoch API addition while this task ran.
It is preserved and excluded from the owned patch.
The source manifest distinguishes the actual current index hash from the owned-only after hash.
The prior lifetime fix remains intact, and no historical 67-projection or archive-checker evidence was edited or re-labelled as a current engine pass.
The two protected plain descriptions `chaosx.nr14.60.d` and `.62.d` remain identical to the pre-patch current source.
UI layout, observation-writer and data-workflow proposals remain unimplemented by this owner.

## Delivered behavior

The effective-capacity API serves normal and unified countries without changing the existing fifty-flag category score or its 50/80/110 stages.
All fifty flags remain five-point administrative contracts, with no conversion to physical buildings or paid storage-project counts.
The named risk, burden, harvest-enforcement and pending markers were disclosed before application and are individually documented as completed focus-owned, current operational contracts.
The legacy supply-ceiling pending marker currently extends mission duration by 60 days and has no storage payment/completion writer.
No unpaid storage building is credited or granted.
No derived-score exclusions, weights or cost retunes were introduced.

A one-state zero-index host has capacity 1300, permitting the unchanged inclusive 1200 reserve and strict-above-1200 bonus.
The hard ceiling remains 5000 and ordinary capacity remains 2000.
Store surplus after a lower cap is discarded at an existing actor pulse or relevant operation boundary.

The quote freezes regular source/destination capital objects before tag changes or annexation and uses `GetID` meta parameters to generate literal state distance syntax.
Missing capture, invalid country/generation context or an unwritten/negative distance rejects the quote with no transfer.
Source-frame outputs are allocated inline by the four consuming owners before helpers and scopes.
Later transfers consume quote success before one dispatch debit and one distance-adjusted credit, preventing reuse.
Migration failure prevents the Larder/annex continuation.
Autonomy uses an explicit donor country pointer for the puppet transaction and never credits donor land to capacity.

Opening identity assignments preserve the existing bootstrap and managed/mobile additions, with their original rapid/managed/mobile branch order.
They use the received snapshot once and do not call the later-donor credit helper.
CBL and primary Wendigo clamp after actual annexation, with fresh actual recipient territory.
The both-human Wendigo branch retains the original zero donor snapshot and disabled absorption, skips donor debit/credit and uses only the transformed country's own territory.
The existing native troop, technology, commander, identity and equipment paths are retained behind their successful transaction gates.

Review found that the initial CBL capital transfer can remove the selected donor's last state before runtime migration checks source existence.
The exact opening-only proof preserves that already validated source context across this existing step.
It requires the captured source/recipient pointer identities, positive captured source generation, surviving successful quote, live positive-generation CBL recipient and its actual frozen capital ownership/control.
The proof is allocated and cleared in the CBL constructor and is never set by later absorption, autonomy or Wendigo.
Existing live-source migration remains supported and no later/stale destination bypass is provided.

## Helpers, call sites and cleanup

New private effects: `cannibalism_refresh_larder_effective_capacity`, `cannibalism_capture_current_larder_transfer_capitals`, `cannibalism_clamp_and_publish_current_larder`, `cannibalism_prepare_larder_transfer_quote` and `cannibalism_apply_initial_larder_inheritance`.
The existing `cannibalism_add_current_warlord_larder_to_unified_host` is the one-shot later transfer commit.
New private triggers are `cannibalism_larder_transfer_context_is_valid` and `cannibalism_runtime_migration_source_is_valid`.
The shared existing destination trigger retains its prior identity/reveal/existence gates and adds positive expected-generation equality.

The eight original global-ceiling store clamp sites are fully migrated.
The two identity sites defer to constructor finalization, the later-donor recipient site defers to absorption/autonomy finalization, and the five immediate gain/debit sites use the country-aware finalizer.
The mixed actor-pulse and shared foreign-seed local clamps also use that finalizer.
Ordinary consumption and warlord-only local clamps retain their local bound.
Profile calculation refreshes capacity without recursive profile calls or premature store clamps.

Three existing initialization owners populate the normal-country capacity API before its tooltips are used.
Incarnation reset, integration release, local victory and final cleanup clear the derived capacity.
Final cleanup uses the existing bounded actor registry before it is emptied, with no daily or whole-world scan.
No new global target or variable is introduced.
Temporary inputs/outputs expire with their frame, capture proofs are consumed and regular capital pointers expire with their effect chain.

## Evidence and meaningful validation

Evidence lives in [the implementation evidence folder](2026-10-04_larder_logistics_implementation/evidence/).

- [Before/after source manifest](2026-10-04_larder_logistics_implementation/evidence/source_manifest.json) records exact hashes and the concurrent index-row disposition.
- [Owned source patch](2026-10-04_larder_logistics_implementation/evidence/owned_source.patch) excludes the unrelated Event012 index addition.
- [Source checks and fifteen scenario receipts](2026-10-04_larder_logistics_implementation/evidence/source_validation_and_math_receipts.json) verify output ownership, original score preservation, quote consumption before debit, one debit/credit, post-annex placement, both-human zero, generation proof, opening last-state provenance and protected descriptions/tooltips.
- [Fifty-flag mapping](2026-10-04_larder_logistics_implementation/evidence/fifty_flag_mapping.json) retains the exact completed writers and the disclosed special flags.
- [Frozen baseline receipt](2026-10-04_larder_logistics_implementation/evidence/frozen_baseline_receipt.json) verifies all ten copied source files against their original manifest hashes without modifying them.
- [Connected MCP results](2026-10-04_larder_logistics_implementation/evidence/mcp_requests_and_results.json) retain source revisions, artifact URIs, partial coverage and missing capabilities.

The existing structural checker was used only on touched scripts and compared to their before snapshots.
It caught two introduced initialization indentation errors, which were fixed before source application.
No generic parser/emulator framework was added.
The feature-specific receipts are source assertions and declared fixed-point arithmetic, not runtime or normalized AI probability measurements.
The accepted tuning and normal/ceiling constants are retained in source and the scenario receipts expose their consequences.

| Source scenario | Result |
| --- | --- |
| Opening host with twelve final states, 2000 store, 300 bootstrap and 100 managed addition | Capacity 2400, final store 2400, preventing a premature one-state clamp from discarding 1100. |
| Opening one-state donor after capital transfer | Exact validated opening provenance permits migration when the donor has become inactive. Final 1000 store plus 300 bootstrap fits capacity 1300. |
| Locality submission | Dispatch/receipt 850, final host 1150 within capacity 1300. |
| Regional submission at distance 1000 | Dispatch 850, receipt 765, final host 1765 within capacity 2200. |
| Distant surrender at distance 3000 | Dispatch 1300, receipt 910, final host 3410 within capacity 4200. |
| Remote autonomy at distance 6000 | Dispatch 200, receipt 80, donor keeps 800 and host reaches 4880, with no donor-territory credit. |
| Control loss to one state and zero index | Next finalization reduces 3000 stores to 1300, discarding 1700. |
| Both-human preservation | Donor transfer remains zero and donor store is preserved. |
| Failed migration, invalid/stale generation, missing capital or unwritten distance | No Larder commit or donor annex continuation. |
| Repeated quote commit | Consumed quote cannot debit or credit twice. |
| Reserve/bonus and saturation | 1200 satisfies the reserve but not the strict bonus, 1201–1300 can satisfy both, and capacity never exceeds 5000. |

The eight parent comparison IDs remain `locality_submission`, `regional_submission`, `distant_surrender`, `remote_autonomy`, `cap_loss`, `both_human_preservation`, `insufficient_larder_terminal_gate` and `stale_generation_no_transfer`.
The auditor's missing fixture values remain missing in its original evidence.
Supplementary owner examples are explicitly declared rather than silently filled into the frozen fixtures.

## Omissions, blockers and follow-up

No requested gameplay simplification, zero-distance fallback, new route, new country/package, asset placeholder, cost or weight retune was introduced.
No implementation blocker remains identified for the authorized source work.
The parent must request the mandatory same-eight-fixture `hoi4.probability_compare` from auditor `01a10385`, carrying its incomplete candidate pools and unbound inputs.
That comparison has not been run by this source owner.

Connected probability inspection found four Event71 candidates with an incomplete pool and two required score inputs.
Event trace remains partial, with helpers unexpanded and lifecycle projections deferred.
The narrow post-change source lookup returned the quote definition and the exact GetID/meta block, with no engine execution claim.
`hoi4.script_validate` is not exposed, and advanced helper jobs were not used without verified health/version/client negotiation.
Native GetID/distance, annex timing, constructor source transition and control-loss cadence have no observed engine acceptance evidence here.
Existing native country/leader/tag preparation has no rollback proof if an engine transaction fails after preflight, although Larder/annex continuation remains guarded.
GUI visual comparison and observation/data-writer implementation remain with their separate owners.

Icons/assets: none added, existing Larder tooltip surfaces reused.
Skills used: events, subagents, decisions/missions, focus trees and scripted GUI linked-consumer guidance.
No skill was created or updated.
Parent review, probability comparison and the parent-owned meaningful commit remain next.
