# Event 23 custody scope and assembly audit resolution

Disposition: source repairs implemented; full Event 23 acceptance remains incomplete.
The previous goal turn made concrete assembly-registry progress, and this continuation changes authoritative gameplay, localisation, documentation and one completed skill-maintenance commit.
No game was launched, no logs were requested or searched, and no live or save/reload acceptance is claimed.

## Implemented repairs

| Surface | Repair and evidence |
| --- | --- |
| Transit and dismantlement receipts | Country helpers entering their stored source state read the caller's nonce through PREV, not the capturing/annexing callback's ROOT; closure no longer depends on the winner's unrelated receipt. |
| Recaptured operational custody | The recorded-owner country explicitly returns to the state for its operationalized flag. Identical recorded-owner and physical-holder pointers therefore receive one operational debit, not two. After accounting, the live operational marker is cleared and a historical marker retained, allowing a successor's physical-custody track without inherited operational access. |
| Local breakaway selection | Existing secure-custody selection stores actor-owned state pointer and ID. All three existing timed stages revalidate and use that actor's exact depot and current holder, not the global Soviet selection. Completion/cancellation preserves its depot between stages and does not clear another actor's target. |
| Repeated per-depot tracks | The current depot must complete or become invalid before the existing selector opens another site. Secured custody, technical access and command formation use exact state-and-holder receipts. The selector projects only the selected depot's proven stages and does not reset an actor's separate historical operational registration. Joint custody and pending Event 5 reconciliation prohibit unilateral progress. |
| Territorial receipt invalidation | A changed physical holder is classified as breakaway or foreign custody. Same-holder callbacks preserve joint-custody agreements. The former holder's secured marker is cleared and mismatched institutional/command markers are contested. Both frozen registry views retain the securing actor and contested markers. |
| Return requests and annex cleanup | Return requests use a separate transient actor pointer. Dead-actor cleanup clears local pointers, while Soviet global selection, coercion and reactor targets are cleared only by SOV cleanup. |
| Event 5 registry snapshots | Before/after receipts include the actual site's holder-owned local selection, ID, progress stage and active-stage marker. No periodic world scan is added. |
| Shared detonation profile lifetime | After all shared deaths, fallout, condemnation and treaty consumers run, the shared hook clears the atomic/test/partial-yield/accident/demonstration markers, preventing completed test metadata leaking into a later source. No consequence coefficient or second consequence call is introduced. |
| Assembly nonce mismatch | Closure requires matching state identity and active nonce, or the same state's already-closed nonce. Mismatch retains the actor cleanup pointer, marks the receipt disputed, writes no closed receipt and blocks replacement production. |
| Assembly text and quantity | Start and UI share the unchanged scratch-only production quote. The mission shows the fixed pending quantity and exact site; both descriptions state that upfront security costs remain spent on cancellation. The existing Status row labels posture and public knowledge. |
| Local stale-click costs | Breakaway secure-custody, three stage actions and return requests repeat exact requirements and affordability on click, and debit only after their start/request succeeds. Availability and custom affordability use the same profile. Numeric costs, durations and AI weights are unchanged. |
| Action Boolean contract | Actor proof, authorization and remote-recovery permission are country flags. Exactly one detonating/non-detonating flag supplies the physical-yield profile. All setters, preflight/callback/receipt checks and context cleanup use the flag contract, with absent or contradictory yield profiles rejected. No cost, consequence or arsenal formula is changed. |
| State-pointer scope validation | Installed `exists` documentation supports COUNTRY only. The action-state and selected local-state blocks use their state ID, registration and passability predicates, and the shared non-yield endpoint checks passability. All genuine country existence checks remain intact. |
| Reservation preflight | Target geometry no longer requires a reservation that has not been created. Source eligibility is validated before debit, with source-specific actor/global/state mirrors after reservation. Operational-country reservations require no fabricated state reserve. A depleted assigned pool can use an existing controlled registered depot as the identity for its separately accounted operational reserve. |

## Changed files

Gameplay and text: `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`, `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`, `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`, `common/decisions/023_sov_nuclear_bombs_decisions.txt`, `common/scripted_localisation/023_sov_nuclear_bombs_scripted_localisation.txt`, `localisation/english/023_soviet_nukes_l_english.yml`, and the Event 23-owned profile cleanup hunk in shared `common/scripted_effects/chaos_meter_effects.txt`.
Documentation: the Event 23 runtime-effect contract, shared nuclear Chaos ladder, this handoff, and the reviewed skill-maintenance handoff.
The exact actor-owned additions are `sov_nuclear_bombs_local_custody_state`, its ID, and the separate transient return-request state.
The new assembly mismatch marker is `sov_nuclear_bombs_assembly_receipt_disputed`; the new quote trigger and text selector are `sov_nuclear_bombs_prepare_production_quote` and `GetSovietNuclearBombsProductionQuote`.

## Meaningful local checks

Read-only block assertions cover five ledger helpers, seven breakaway effects, two selectors, local state/id/holder validation, and absence of shared-selection writes in the migrated local flow.
Logical fixtures cover a capture callback whose ROOT nonce differs from the project owner's nonce, recapture with identical recorded owner and holder, matching active and already-closed assembly receipts, and mismatched state ID or nonce.
The mismatch fixtures retain the pointer and publish no closed receipt; they do not execute HOI4.

Six additional source-level fixtures cover first-depot selection, a second depot after the first becomes operational, a lost depot, another actor's technical access, joint custody and an active-stage selection lock.
They permit the first and next valid selections, reject a lost target and another custodian's access, prohibit unilateral joint-custody progress and preserve the active-stage lock.
Selection is checked to grant no nuclear stockpile, technology, building or shared target, and operationalization requires the actual holder's active delivery stage for the selected state ID.
These fixtures are logical/source checks, not native eligibility, campaign probabilities or save/reload acceptance.
The four Boolean yield-profile combinations were checked explicitly: neither and both are invalid, detonating alone is valid but cannot reach the non-yield endpoint, and non-detonating alone is valid for that endpoint's additional committed-accident guards.
The shared endpoint's old numeric-profile consumer was updated in the same change, leaving its consequence body and one-shot nonce accounting unchanged.
The separate action-flag before-source files are retained under `probability_source_snapshots/action_flags_2026-10-03/`.
A context-free scripted-system architect owns a read-only dataflow review of that representation change, including pending receipt lifetime and demolition permission cleanup.
Its first completed handoff, `023_action_flag_contract_read_only_audit_2026-10-03.md`, confirms the representation mapping and five state-scope corrections, and identifies the circular reservation prerequisite plus two inaccurate contract-document claims.
The parent applied the separate pre/post source-proof repair and corrected both document claims without changing ledger formulas, amounts or consequences.
The architect is rechecking clean assigned, transferred and operational sources, missing mirrors, active idempotence, release and pending receipt lifetime against the exact before bytes in `probability_source_snapshots/reservation_preflight_2026-10-03/`.
The operational-source fallback's candidate eligibility and native outcomes remain subject to the required probability and engine evidence, not inferred from the source repair.
The first recheck confirms those three original findings are closed in source, but identifies remote-holder substitution and malformed rollback counterexamples.
The parent requires remote proof to retain its actual stored holder, gates rollback on source-specific mirrors without requiring a still-valid target, and preserves a disputed active receipt instead of refunding or erasing unknown context.
The architect's final read-only recheck confirms both follow-up P1 counterexamples are closed in source, including stored-holder authority, verified rollback after target invalidation and retention after failed rollback.
Its 20-case actual-source model invokes cleanup twice per case and verifies idempotence for valid and malformed receipts, while explicitly bypassing aggregate reconciliation and claiming no engine execution.
Native custody/cancellation, save/reload and the operational-source probability comparison remain separate unresolved gates.

The security profile's positive affordability constants exactly negate its political-power, support-equipment and manpower debit constants.
The shared production calculation remains 15/25/35/45/50 devices at 0/2/4/6/8 reactors respectively; this verifies formula equivalence, not campaign balance or native construction.
No evolution increment, timing, outcome weight, AI weight, consequence strength or cost amount was tuned.
Part 5 defines the 100/175/275/400/600 ladder as cumulative opening/evolution grants, separately from ordinary production, and the unchanged post-baseline increments remain 75/100/125/200.

## Reviewed audits and reference limits

The full read-only assembly audit is `023_assembly_registry_audit_retry_2026-10-03.md`.
Its closure finding and text findings are addressed above.
The parent also inspected the cost-effect and affordability definitions that were outside that auditor's bounded file allowlist.
Six unique production action IDs remain six actions, but native target-clone row density is still unresolved; this is not dismissed as a renderer issue or silently satisfied by counting IDs.
Probability, decision-scenario, indexed-caller, Event 5 complete transfer-caller and save/reload evidence remain outstanding.

Installed callback source comments bind ROOT/FROM exactly as used here: `common/on_actions/00_on_actions.txt` lines 1615–1624 and 5075–5084, SHA-256 `52A751456F1774AD5001C86D41D4E46494F751D79B6C224B6CD4C0EEBB615EB9`.
Offline Scopes lines 245–281 and Data structures lines 426–449 were read for nesting and persistent pointers, at SHA-256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` and `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
Installed triggers documentation covers check_variable at 2110–2136, clamp_temp_variable at 2145–2152 and add_to_temp_variable at 713–730, revision `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.
Country-flag scope and syntax were read directly at installed triggers lines 3624–3639 and effects lines 6730–6739, at the same triggers revision and effects SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
Offline Data structures lines 104–126 document Boolean flags, persistent country/state ownership and clearing at the previously cited SHA-256.
The installed `exists` section was also read directly and reports COUNTRY scope only, supporting the targeted removal of five invalid state-scope uses rather than an indiscriminate replacement of country existence checks.
Vanilla scripted localisation and the existing project temporary-value selector pattern were inspected for the quote surface.

The tool inventory initially omitted HOI4 domain entries, but direct capability checks and the server's artifact-template response corrected that absence finding.
Script validation is absent, and the exposed source-lookup schema has no view/keyPath support.
The definition-only lookup for the dismantlement closure, with references disabled and a 12-line limit, timed out after 600 seconds.
A further explicit-workspace two-line retry returned `OK`, one complete definition match, no skipped sources, and no override/shadow at revision `0ebe93d6aae18ad00a397aed1dc210b37dc5433fc9a6c129ecfce1cc68b68544`.
It identified the dismantlement closure at `mod:common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`, definition lines 2041–2068, but returned only lines 2041–2042 and continuation 2043.
The parent requested the body continuation under that exact revision; indexed body/caller coverage is not inferred from the two opening lines.
After the continuation handle disappeared, a fresh explicit-workspace body read failed immediately because the connected `hoi4_source_lookup` function was unavailable.
The current exposed inventory contains no HOI4 domain routes, and a subsequent `list_mcp_resource_templates` request for `hoi4_agent_tools` failed its startup handshake after 120 seconds.
This is a current connection gap rather than evidence that earlier successful source reads never occurred.
Two context-free probability auditors own the narrow assembly route retry and the six named local-custody before/after scenarios, respectively.
The exact pre-edit decision, trigger and event-effect bytes were retained under `probability_source_snapshots/local_custody_2026-10-03/`, without claiming that copied helpers are automatically resolved by the MCP adapter.
Both auditors returned completed read-only source handoffs, `023_assembly_probability_route_retry_2026-10-03.md` and `023_local_custody_probability_before_after_2026-10-03.md`, which the parent reviewed in full.
They confirm unchanged source score expressions, retain incomplete candidate pools and external factors, and provide no probability acceptance because the routes are absent and resource discovery fails handshaking.
The local-custody before set lacks the pre-edit runtime helper, so historical helper isolation also remains unresolved.
The audit and skill worker obtained reference context/search evidence where reported, but retained unresolved reads and repeated source/probability timeouts rather than inventing engine coverage.

## Native delivery and remaining work

Installed native raids prove actual bomber-unit assignment and native target selection, but document early equipment collection without a creation/cancellation receipt hook or instance/source pointer sufficient to bind the current exact custody transaction.
The parent inspected raid documentation outcome/scope sections and native AI/raid defines; AI cancellation after 60 launchable days is documented, but native bomb refund/custody behavior is not proven.
The unmodified vanilla `nuclear_strike` AI path has no Event 23 evolution/authorization gate, so the private Event 23 gate alone is not proof that native first use cannot bypass it.
That integration remains a required defect, not an accepted detonation-only fallback.
One concrete preparation/cancellation evidence request was sent to the orchestrator while local repairs continued.

Other required work includes current native delivery integration, full conservation and save/reload evidence, engine acceptance of the repaired per-site local tracks and flag contract, all named probability scenarios and comparisons, native row/text/asset consumer review, full completion audits and final focused gameplay commit.
The visual package retains 75 DDS files and the selected seven achievement triplets, with six decision DDS files replaced and their earlier runtime bytes retained in the promotion archive.
The original icon prompt set remains absent, and the additional legacy icon family's exact prompt coverage still needs reconciliation under the user's approved fresh-generation/replacement authority.
A context-free icon artist is producing a separate six-icon decision replacement package under `docs/assets/023_sov_nuclear_bombs/decision_icon_replacements_v1/`.
The locked consumers remain the existing accounting, storage hardening, reactor construction, device assembly, delivery preparation and command exercise sprites at 33x32 with native transparency.
The parent reopened all six legacy sources and decoded DDS images, and verified the closest canonical decision reference's pixels against its installed vanilla DDS and sprite definition.
Candidate production does not constitute parent approval or runtime promotion.
The parent opened all six new source masters individually and found stray red/yellow fringe on the storage-door source's upper silhouette.
The icon artist received an exact native-edit repair request that preserved the failed original and recorded a separate repaired source lineage, with small-size/DDS approval pending at that request stage.
After inspecting all six actual DDS round trips, processed native/4x views and storage-v2 neutral-composited views, the parent accepted the six replacements and promoted their exact DDS files under the existing sprites.
All six runtime hashes and decoded RGBA pixels match the selected candidates, and the pre-promotion runtime files were archived after matching the historical DDS mirrors.
The documentation curator reconciled the six current crosswalks and manifests, and the parent reviewed its complete handoff and bounded edits, with actual live consumer acceptance still unresolved.
No original prompt was reconstructed, no old asset was falsely claimed as new generation, and no unapproved fallback was used.
The command-board event's current AI acknowledgment has weight 100 and all five phase choices have weight 0, leaving AI-equivalent phase navigation as a concrete source gap.
A bounded improvement-loop planner is preparing a closure design for existing AI phases and the native target-clone row budget, without adding a new system, changing deferred evolution timing or approving a delivery fallback.
The returned 505-line closure addendum and complete handoff were read by the parent and accepted as a queued bounded implementation, with no additional broad expansion.
It identifies deliberate AI navigation, prospective Evolution-IV preparation and a below-III authorization modifier that can block Evolution-II minor use, alongside native target-clone density and the strategic-payment-plus-device cost violation.
The queued implementation uses a deterministic protected-context router and existing cadence/constants, with all probability, native delivery and actual presentation evidence retained as gates.
Device-bearing strategic actions require a three-resource release profile plus the spent device, while non-device strategic actions retain their four-resource profile.
The release profile is implemented in source for wartime demonstration, limited preparation, final authorization, reduction to demonstration, retaliation authorization and site destruction.
It keeps the existing command-power, support-equipment and fuel amounts and removes the political-power charge only for those device-bearing actions, with matching affordability/payment/localisation and a dedicated same-scenario probability handoff pending.
The hostile-nuclear notification now requires actual war with SOV, preventing a friendly strike on Soviet-owned occupied territory from manufacturing an enemy-use receipt or relaxing the AI first-use gate.
The actual new on-action predicates and their exact before-source copy are retained for the required same-scenario review.
The object-pointer syntax auditor returned a complete 58-token bounded inventory and four direct normal-variable ID accesses that disagree with the offline separator rule, without claiming an observed engine parser failure.
The parent reviewed its complete report and actual installed vanilla `THIS.id` precedent, then replaced only those four accesses with explicit `var:` state entry and correctly nested PREV identity reads or writes.
Valid static scopes, event-target aliases and constant category/key accesses remain unchanged, and all four comparisons keep the internal object-ID domain.
The shared no-yield endpoint, dismantlement completion, backup-command loss and accepted-action target receipt use the explicit identity shapes, with native event/lifecycle evidence still unresolved.
The broader Events 1–40 request remains unfulfilled by this Event 23 continuation; no completion is claimed for other agents' work.

## Completed focused skill commit

The reviewed generic callback-scope addition and its completed handoff were committed as `464841023d34ba11dd39d42d36accb5c62c00959`, `Document callback scope and exact custody receipt guidance`.
An isolated index received only the 12-line owned insertion and the handoff; the unrelated event-option audit paragraph in the mixed skill file remained unstaged.
The initial HEAD-moved preflight stopped before staging, then the plan was rebuilt from the current HEAD and published with compare-and-swap.
Path-scoped index reconciliation preserved the working skill and all other staged entries.
The commit contains no gameplay, asset, workbook or unrelated skill changes.
No index lock was removed.

The additional four-sentence generic state-scope guidance and its reviewed handoff were committed as `f32aaa4b7acc3621fcb5375743b63bfc7a81f739`, `Document country-only existence checks for stored states`.
An initial publication preflight detected a moved HEAD and stopped without touching the real index.
The isolated plan was rebuilt from current HEAD, published with compare-and-swap, and reconciled only the two owned paths, preserving unrelated staged entries and the mixed working skill.
This second focused commit also contains no gameplay, asset or workbook changes, and no lock was removed.

Skills used include events, decisions/missions, subagents, native raids, save inspection, shared-tree Git commit, event assets and the asset prompt's static-only frame-animation scope check.
The events skill received the completed reusable callback guidance; no event-specific context was added to a skill.
