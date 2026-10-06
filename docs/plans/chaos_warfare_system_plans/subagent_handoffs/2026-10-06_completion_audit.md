# CBRN takeover completion audit - 2026-10-06

Disposition: **partial implementation; completion remains blocked**.
This is a read-only audit of the takeover claims and the parent-owned October 6 tranche.
No gameplay, asset, workbook, CSV or Git-index change was made by this auditor.
The parent owns integration and final disposition.

## Inputs and acceptance

Read AGENTS.md, the events, subagents, improvement-loop, event-planning, scripted-GUI, native-raids, event-assets and 3D-pipeline guidance applicable to the bounded review.
The supplied takeover history and inbox, package README and historical PACKAGE_MANIFEST, accepted amendment `specs/13_2026_09_20_accepted_cbrn_overhaul.md`, October 5 round-3 remaining-work note and `agent_decisions_2026-10-04.md` were reviewed.
The accepted amendment is authoritative; old skip decisions and a commit labelled done do not remove accepted requirements.
The package manifest explicitly marks its old counts/hashes as historical provenance.

## Completion by surface

| Surface | Current disposition | Evidence and limit |
| --- | --- | --- |
| Routed quote, native scope and fixed-point repairs (`ccca51294`, `3137c7996`) | Implemented in source | Emergency/hospital quotes execute in trigger gates, occupied quote is in `if.limit` (`cbrn_occupied_transaction_effects.txt:124`), affordability uses `universal_cost_component_is_affordable`, and rescaled rates retain their population divisor. Raid AI has a separately owned probability pass; native transaction behavior remains unproved. |
| Occupied/export reconciliation (`329048c82`) | Implemented in source; native evidence unresolved | Decisions `cbrn_reconcile_occupied_mask_records` and `cbrn_reconcile_export_shipment_records` are at `cbrn_protection_decisions.txt:483,502`. The occupied retry/write-off path at `cbrn_occupied_transaction_effects.txt:372` and export retry/write-off preserve delivered outcomes and clear the quarantine only after reconciliation. A real blocked native refund is still required evidence. |
| Event 020 board (`4e54aacd5`) | Source implemented; visual acceptance partial | The current zero-capacity full/cropped/annotated production PNGs were reviewed: readable, unorganized label only, no visible overlap or clipping. Current inspect/render routes work; the old “unusable route” status is stale. The matching five-state/both-resolution source comparison timed out after 600 seconds with no artifact or task handle returned. Ordinary decision rows and cost rows are outside this narrow board render and remain unproved. |
| CXT facility preference and documentation (`23a9383ce`, `469fe5021`) | Implemented in source; native facility gate unresolved | Supply-connected owned candidates precede adjacent borrowed states; native construction is still the final gate. The flag-gated temporary trace must remain until the exact native rejection is resolved, then helper and caller must be removed together. The parent replaced the unverified fixed template count with registry-driven wording. |
| Containment maxima (`de73c23f9`) | Implemented in source | Both getters are present in `biowarfare_disease_containment_scripted_localisation.txt`. This does not prove that all `[?constant:...]` interpolation is unsupported; vanilla counter-evidence already exists. |
| Warfare help (`858cca927`, `5e8532905`) | Implemented in source; nested rendering unresolved | `chaosx.help.body.warfare` reads policy cost/reassessment getters and `GetCBRNHelpCondemnationSummary`, whose constants match the mechanics. Native rendering of the nested text has not been observed by this auditor. |
| Procurement commitments (`ca65fd278`) | Accepted exception implemented in documentation | BF-CBRN-013/014/015 at `event26_cost_surface_registry.md:155-157` preserve one/three/two native factories under the accepted procurement adapter; the sale applies to spendable PP/support components. Other owners' registry coverage is not thereby complete. |
| Commander wording (`42b516034`) | Implemented in source/documentation | Country service receipts are described without inventing participation of a particular raid division or army. An assigned-army pointer is not established by these receipts. |
| Contamination map mode (`7a06d83a7`) | Implemented in source; colour consumer unresolved | `cbw_triggers.txt:284-300` reads the ordinary marker or positive intensity with a future expiry, preserving Fallout's accepted removal of its marker. Actual map colours remain native evidence. |
| Legacy company removal (`42d7b3f2e`) and parent cleanup | Source cleanup implemented | The eighteen definitions are removed. Parent cleanup renames the surviving armored category, preserves modifier values in both subdoctrine files, removes orphan registries/textures and updates the 79-unit roster documentation. Native loading and doctrine consumer acceptance remain unproved. |
| Air Is Still Breathable and The Antidote Arrived | Parent implementation present; runtime/asset acceptance pending | Current source was re-read after parent fixes. Air uses confirmed current-war per-major flags and symmetric new-war cleanup; Antidote requires real advanced issue, severe contamination, strict cumulative losses, medical/decontamination proof, zero final contamination and continuing controller ownership. Definitions/triggers/localisation are wired. Final art and native execution remain parent-owned. |
| No Wind Is Friendly / Unbroken Supply Corridor | Accepted design blocked | No exact forecast-failure/army-recovery receipt is established for No Wind. No exact assigned-army supply/battle-objective read is established for Corridor. The parent rejected the weaker inherited No Wind candidate and removed its runtime registration; the accepted achievement itself remains incomplete. |
| Assault battalion audio (`e0af506e4`, `469fe5021`) | Runtime preservation decided; completion blocked by provenance | The shipped nine float WAVs and the unused PCM16 recovery set are separate lineages. Timing/preservation decisions do not supply source-page, license and original-to-derived checksum proof for the shipped lineage. See `chaosx_chaos_assault_battalion_model.md:47-53`; the old source manifest does not exist. |
| Other graphics, historical advisor portraits and ancillary asset rows | In flight / not re-audited as complete | Asset workers/parent own final processing, source/handoff evidence and wiring. Existing roster counts and old completion notes are not fresh portrait or asset acceptance. |

## Concrete findings and minimal follow-up

1. **Accepted achievements remain missing.** Spec 12 lines 385-397 and 438-443 require forecast failure/recovery and assigned-army supply. Keep these accepted requirements blocked with exact missing native signals; do not award them through friendly damage, target capture, country supply, railway level, equipment ratio or a supply modifier.
The inherited No Wind candidate also read helper-local friendly-damage temporary outputs after the damage helper returned and stored one overwriteable actor receipt per state.
The parent removed that candidate; this is a rejected implementation, not acceptance of removing the achievement.

2. **Runtime unit-audio attribution is incomplete.** The model guide identifies source/license evidence only for the unused recovery candidates and explicitly distinguishes those bytes from the runtime files.
Recover the shipped recordings' sources/licenses and a measured original-to-derived checksum crosswalk, or route an explicitly reviewed sourced replacement with fresh animation synchronization.
Preserve current bytes until that choice is concrete; an arbitrary archive swap is not a fix.

3. **One atmospheric jump can generate four news popups.** `air_contamination_update_threshold_flags` (`chaos_meter_effects.txt:4855`) uses independent branches at 4871/4889/4907/4925 with news at 4886/4904/4922/4940.
Each global fired flag prevents repetition of that threshold, but one CBRN delta crossing all thresholds still queues four distinct notices.
Owned entry points are `cbrn_chemical_state_effects.txt:105,143` and `cbrn_biological_air_effects.txt:134,194` through `air_contamination_apply_delta_bp`.
Resolved by the parent during this audit: three next-threshold guards suppress lower notices while preserving every crossed threshold and fired flag; one jump to 100 emits only the highest ordinary threshold news.
This is a narrow shared-callback correction under the user's no-spam rule, not the originally suggested CBRN-only optional parameter.

4. **Old GUI evidence claims were overstated.** The takeover history already retracts the claim that five matching post-change scenarios existed for `4e54aacd5`.
The October 6 zero-capacity render closes only that exact current scenario; preserve the new source hashes and artifacts and do not retroactively call the original commit visually validated.
The reviewed event-owned handoffs prove Event 020 ownership/reference mapping, but their text does not explicitly demonstrate a `chaosx_event_ui_worker` identity; retain that handoff provenance limit unless the parent has independent routing evidence.

## Presentation and entry-point audit

The prescribed report-colour audit returned zero reached coloured keys for the `cbrn`, `biological`, `chemical` and `cbw` event-file prefixes, including their scripted-localisation substitutions.
This is owned-family source evidence, not a claim about unrelated reports.
The CBRN maintenance and native bridge events are hidden and directly produce zero player report windows; helper-driven downstream effects are unresolved in the bounded MCP graph and are not counted as proven zero.
The defective reconditioned-mask report (`cbrn_protection.2`) is one report per successful paid batch, not a self-repeating report; the parent correction limits an atmospheric jump to one ordinary threshold news while retaining every crossed milestone flag.
The standalone `chaosx_cbw_doom.1/.2` definitions have no exact literal caller in the reviewed owned source; their reachability is unresolved rather than assumed.
G7 forced selected-country feedback is **not applicable to this system**: the reviewed CBRN accepted amendment and event namespaces provide no numbered public Settings root; no CBRN root/registry entry was found in the bounded Settings dispatch read.
The shared Settings framework and Event 020's public root remain their respective owners' surfaces.

## Meaningful validation and limits

Live reference_context/search/read and source_lookup answered; installed game documentation and offline wiki were read for country events, on_state_control_changed, on_capitulation and temporary-variable lifetime.
Installed `effects_documentation.md:2943-2967` revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` documents country-event scope.
Offline `On actions` lines 254/450 revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a` supplies winner/new-controller bindings; `Data structures:435-443` revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` supplies helper-output lifetime.
Reference searches for `has_army_supply` and `supply_ratio` returned no installed/wiki section; the installed unit-leader dynamic-variable section at 1176-1380 exposes no exact current supply read.

Bounded event inspect/render ran without refresh or helper expansion at graph revision `9d95527b43af472a9652ed29130c120e8dbe66acf038b3fc4f9f2952712bfc5c` and remained `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL`.
The direct trace includes all 59 event roots from the 16 named files and 189 nodes with `truncated = false`; the scope render projects 11 state-bearing roots by view design.
The focused boundary defers helper/lifecycle passes and contains unresolved helpers; it is not engine proof.
Event comparison encountered `EVENT_GRAPH_ARTIFACT_INVALID` for a trace artifact (unsupported graph schema) and `EVENT_REVISION_NOT_CACHED` for the earlier graph revision; no successful matching event comparison is claimed.

Whole-file and explicit STATE achievement script checks returned `SCRIPT_CHECK_PARTIAL`, `valid = null`.
The final containment snippet checked 28 commands with no invalid findings, but retains nine unresolved items and omitted/unchecked argument findings; manual source review is separate from complete MCP validation.
The two renamed doctrine files are `family: unsupported`, zero checked commands, so their empty finding lists provide no semantic validation.
The parent reports passing 106 sabotage, 21 aid and 46 occupied source scenarios; this auditor did not rerun them or treat them as native execution.
The parent-supplied USA baseline-save values (game 1.19.2, 1936.1.1.12, eligible flag true, protection 55, policy 2) are live observations, not completion scenarios for the two new achievements.

MCP routes are exposed in this worker and the installed package is 3.9.0; no separately exposed connected health/version route or native task negotiation was available.
The live GUI schema accepts `scenario.id`, `closedFlags`, `sourceBaseline`; `uiScale` belongs at scenario top level or in the render resolution entry, not inside `scenario.resolution`.
No Hearts of Iron IV launch, desktop control or log search occurred.
The five-state GUI call requested `pre_outbreak_hidden`, `active_zero_unorganized`, `active_organized`, `exhausted_capacity`, and `recovered_no_active_response`, at 1920x1080 and 2560x1440, scale 1, with explicit flags, closedFlags, exact values, generated scenarios disabled and the historical mod-owned GUI sourceBaseline.
The final result was `timed out awaiting tools/call after 600s`, with no artifact or task handle; the server outcome remains unresolved, not proven failed.
No retry was made after that timeout.
Detailed route/artifact/source identities are in the adjacent audit evidence manifest.

## Remaining acceptance

Keep native raid payment/cancellation, all displayed-versus-deducted cost families, blocked-refund recovery, CXT facility construction, combined doctrine/division statistics, map colours, full Event 020 decision presentation, portrait/asset handoffs and shipped unit-audio provenance unresolved.
No workbook/CSV change is justified by this audit alone; catalog changes require final public event wording and the workbook owner.
No goal-complete claim is supported while the accepted missing achievements or these evidence gates remain open.

## Final adversarial commit review

Reviewed `affec7c4e58438610069302272425a8dabe253df`, `e08c6fadfeca19934617a2fe6a98f13e178f906a` and `f824eaa5217e88f1099aaad3fb37ff4088113795` through `git show` and current source.
This pass was source-only except for the parent's explicitly authorized single final `hoi4.script_validate` call on `cbrn_consequence_effects.txt` after its two follow-up fixes.
No gameplay, graphics, other handoff or Git-index edit was made by this auditor.

The review found two additional returning-output dependencies in the new achievement paths, and the parent repaired both during this pass.
Before the repair, the immediate death path called `chaos_meter_register_state_civilian_deaths_percent` and read `chaos_deaths_change` after return without owning that scalar beforehand.
The output is calculated inside the returning native-deaths adapter (`chaos_meter_effects.txt:3647-3683`), so the new Antidote strict-loss gate at `cbrn_achievement_effects.txt:815` could consume a lost immediate-loss result despite real casualties.
Current `cbrn_consequence_effects.txt:256-258` now initializes `chaos_deaths_change` before that call and captures its computed, rounded and capped result afterward.
The continuing-death event's existing preallocation remains in place.

Before the second repair, the consequence path called `cbrn_apply_state_evidence_delta_internal` and copied `cbrn_state_attribution_output` after return, while its first creation was in the deeper `cbrn_refresh_state_attribution` helper.
This made the new Air confirmed-attribution gate at `cbrn_achievement_effects.txt:352` depend on an unprotected output return.
Current `cbrn_consequence_effects.txt:346-348` now owns that scalar before the evidence helper, so the same ancestor storage reaches the nested attribution calculator at `cbrn_exposure_effects.txt:1092-1132` and survives both returns.
The current consequence-file SHA-256 after these two repairs is `43b8546fb77cf3086940020739f8f9f6e29d8dbe513b12b1e1387219f643692b`.
The two repaired dependencies are additional to the ten initializers in `f824eaa5`; they were not included in that earlier narrow three-API audit.

The original ten initializers still match their actual consumers: four class-return guards, two Air-return guards and four previous/new-contamination guards across two consuming delta callers.
No original coefficient, threshold, cleanup formula or native payment was changed by those assignments.
The non-consuming consequence delta call still requires no unused previous/new allocation.

No remaining concrete introduced scope/lifetime fault or impossible gate was found in the reviewed achievement path after these repairs.
Air uses current-war per-major flags, reciprocal new-war cleanup, confirmed exposure and protection checks; its nested `PREV` entries address the victim while the suffix addresses the enemy major.
Antidote keeps controller-loss invalidation, a failed-episode latch until clean, severe-stage proof, actual advanced issue, medical/decontamination proof and cumulative immediate/continuing loss checks before qualifying.
This is source-contract review, not proof of native achievement execution.

No lost shared gameplay hunk was found in the inspected commits.
The shared achievement registry commit adds exactly the two CBRN definitions and the GFX commit adds exactly their six sprites.
The other owner's uncommitted Event 042 achievement additions remain in the working tree; the Event 029 CXT documentation paragraph remains separately modified.
The category rename changes only the category token in units/tags/subdoctrine consumers and preserves the modifier bodies.
The old token remaining in `gfx/texticons/unit_category_chemical_tank_support_companies_icon_small.dds` is a retained texture filename under the correctly renamed sprite, not a stale category registration.
Graphics production and approval remain parent/asset-worker responsibilities and were not closed by this source pass.

The one authorized consequence-file MCP check returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, 392 checked commands, zero findings and zero omitted findings.
It still has nine unknown-scope helper roots and 259 unchecked native argument blocks, against installed-documentation aggregate revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
That limited result does not replace the native execution, asset, GUI or probability gates recorded above.
No other MCP route, live game, desktop, log search or broader helper sweep was used in this final pass.
