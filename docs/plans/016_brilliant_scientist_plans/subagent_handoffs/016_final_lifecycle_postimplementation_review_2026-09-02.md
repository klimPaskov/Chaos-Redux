# Event 016 lifecycle postimplementation source review — 2026-09-02

## Scope and verdict

This is the bounded read-only follow-up to `016_final_lifecycle_preimplementation_review_2026-09-02.md`, under `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
The parent owns gameplay, event, and documentation integration.
This worker changes only this handoff.
The reviewed diff was `git diff HEAD --ignore-space-at-eol` against `e7307e228e2b4bda3309672e8077ac9889c7bb36`.
Source hashes below were recaptured at `2026-09-02T11:37:36+03:00`; concurrent changes after that point require rechecking the affected entry.

F1–F6 are addressed in the inspected source within the bounded findings, including the refined F4 history-preservation requirement.
The nested-lock issue found during this review, R1 below, was corrected by the parent and rechecked before this final source verdict.
No additional unresolved code defect was found in this bounded follow-up.
This is source acceptance of the named corrections, not an exhaustive Directorate/project audit, a probability certification, a passed MCP comparison, or an Event 016 completion claim.

## Review-discovered R1 — Nested expedition locks corrected

`common/scripted_effects/016_brilliant_scientist_effects.txt:2939` validates the transfer before setting both transaction locks at 2940–2941 and cancelling the expedition at 2944–2945.
That corrects the original F1 invalid-input mutation.
However, `dhrondan_fail_expedition` calls `dhrondan_clear_expedition_state` (`common/scripted_effects/016_dhrondan_contact_effects.txt:293`), which calls `dhrondan_restore_kruger_after_expedition` at 225.
When the canonical expedition obligation exists, that restore helper sets the same locks at 118–119 and unconditionally clears both at 132–133.
The first patch therefore continued into snapshots, role cleanup, and nationality mutation without its outer locks still held.
This was a source-level lock invariant violation, not a claim that an actual duplicate character or reward occurred.

The parent applied the narrow correction: `effects.txt:2948–2949` reassert both country and global `brilliant_scientist_character_transaction_lock` immediately after expedition cancellation and before the old-host target/snapshots at 2950 onward.
Cancellation remains inside the validated branch.
The source recheck confirms the locks survive the nested cleanup into the remainder of the transfer transaction, and no shared lock-system redesign was introduced.
The DHR failure helper itself remains repeat-safe because its work requires `dhrondan_expedition_in_progress` (`016_dhrondan_contact_effects.txt:281–295`).

## Findings disposition and conservation evidence

| Finding | Source disposition | Meaningful traced result |
| --- | --- | --- |
| F1 invalid transfer | Addressed, including R1 | Missing/invalid recipient, active scientist, confinement, existing lock, or world-end failure leaves the expedition and permanent host state unchanged because only the temporary committed result is initialized outside the validated branch. A valid transfer still intentionally cancels its active Kruger expedition and reasserts both locks before snapshots. |
| F2 pending breakthrough identity | Addressed | `effects.txt:3020` stores `brilliant_scientist_transfer_pending_breakthrough_family`; restoration at 3192 reads that dedicated snapshot. The four history iterators at 3169/3174/3179/3184 retain their different name. Pending family A/stage S survives history ending in B/C, with one `.6` queue. A no-pending transfer cannot consume stale snapshot data because restoration requires the pending sentinel initialized at 3013. |
| F3 terminal containment reactions | Addressed | `containment_effects.txt:220` calls terminal reaction cleanup before role removal, host reconciliation, and canonical-active exit. It clears the three country and character pending flags and two pending context variables without clearing resolved history. |
| F4 same-country sovereignty | Addressed | `country_effects.txt:1102` calls pending-only terminal cleanup, not the new-carrier history reset. All three scheduler limits in `host_reaction_effects.txt:15/42/67` and event triggers in `events/016_brilliant_scientist_host_reaction_events.txt:34/127/196` exclude the existing sovereign-country trigger. Both queued reports and future unresolved host-only reaction scheduling are blocked on either sovereign carrier. |
| F5 death and split foreign cleanup | Addressed | Death invokes relationship cleanup at `foreign_effects.txt:927` before retiring Kruger. Split formation calls former-host pending cleanup and relationship cleanup immediately after the portfolio snapshot (`country_effects.txt:977–979`), after selected territory has already transferred. Permanent foreign-operation and learned-technology receipts are not reset by these added calls. |
| F6 disabled evolved-opening state | Addressed in source | All four base packages, four seed blocks, and three lower-stage delivered/policy blocks initialize exact event/type/stage/tier context and test `is_current_evolution_enabled` before their writes. Existing base-applied and opening-runtime-applied guards remain. |

In this table `effects.txt`, `containment_effects.txt`, `country_effects.txt`, `foreign_effects.txt`, `host_reaction_effects.txt`, and `evolution_effects.txt` mean the corresponding `common/scripted_effects/016_brilliant_scientist_*.txt` files.

### F4 history is policy, not disposable pending context

The unchanged pending-only terminal helper is `host_reaction_effects.txt:157` after the three added scheduler lines.
It composes country-pending and character-pending cleanup without clearing resolved outcomes or canonical career receipts.
Do not replace the same-tag call with `brilliant_scientist_clear_host_reaction_state_after_sovereignty`, whose subsequent country reset belongs to the newly initialized KRG carrier.
Country `reaction_patent_pool` remains a live accident-pressure input (`effects.txt:3595`), while primary-facility civic/industrial flags drive accident pressure (`effects.txt:3583/3590`) and the restricted-district flag affects foreign security (`foreign_effects.txt:581`).
The three custody-family arrays retain the selected method's history/deduplication, and `reaction_exchange_family` records the immediate exchange grant's family (`host_reaction_effects.txt:320–323`).
The new guards neither replay these rewards nor erase those consequences.
The earlier F4 suggestion to reuse sovereignty cleanup unchanged is superseded by this refined pending-only recommendation and the implemented sovereign guards.

### F5 joint-laboratory and assassination settlement scopes

Joint-site status is used during territory selection (`territory_effects.txt:372/444/481`) and facility eligibility (`common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt:20`).
Formation revalidates at `country_effects.txt:933`, transfers all selected states at 963–972, and only then snapshots at 977 and clears foreign relationships.
The later capital binding uses the frozen `brilliant_scientist_formation_capital_state` target and KRG ownership (`country_effects.txt:744–750`), not joint-site status.
The secondary binder uses its independent target and secondary-facility flag (`country_effects.txt:761–767`).
Clearing joint partner/site flags after that snapshot cannot retroactively invalidate selection or prevent the chosen capital binding.

`brilliant_scientist_clear_foreign_relationships` only removes current framework/partner/site state and the legacy foreign context (`foreign_effects.txt:1192–1219`).
Its nested `brilliant_scientist_clear_foreign_context` clears global `foreign_target_state` and `foreign_actor`, not the regular `foreign_operation_actor` and `foreign_operation_host` (`effects.txt:3333–3342`).
Those regular operation targets therefore remain available after confirmed death for the caller's detected-risk, resolution-history, and event-dispatch steps (`foreign_effects.txt:1486–1495`).
Resolution bookkeeping still has its once-only actor guard and appends both actors' permanent ledgers (`foreign_effects.txt:184–229`).
The added cleanup does not clear operation-history arrays, resolved-target arrays, provenance, learned technology, or permanent `*_ever_*` relationship history.

## Disabled-stage and shared-context scenarios

These are manual source-path traces, not execution of the Clausewitz engine.
`is_current_evolution_enabled` checks the stage's disabled setting and required Chaos tier (`common/scripted_triggers/chaosx_settings_triggers.txt:49–51`), so a stage below its current tier also remains ineligible.

| Scenario | Expected result supported by inspected branches |
| --- | --- |
| All enabled, required tiers reached | The existing four stage packages and seeds remain available once their original chronology/prefire conditions pass; the new guards add no reward call. Repeated synchronization cannot repeat base packages because `*_base_applied` remains checked. |
| All disabled | Every base, seed, and lower-stage prefire delivered/policy block fails its stage gate. No fabricated evolution receipt or seed output is introduced. Existing disabled-stage safety is still applied. |
| Only IV enabled, IV tier reached | Only IV's seed/base package may apply; I/II/III base, seed, delivered, and policy writes are skipped. III-disabled safety retains the regional/safe-resolution path rather than granting forbidden authorization. |
| I/II/IV enabled, III disabled | I/II retain their permitted packages and lower delivery receipts; III cloning/robotics seed, base package, delivered receipt, secret-project policy, and forbidden authorization are not written by prefire preparation. IV retains its separately enabled package and safe-resolution gate. |
| Stage already recorded/applied, then disabled | The added guards prevent fresh grants without deleting chronology, canonical delivered history, existing project history, or applied receipts. Existing safety removes live forbidden authorization as designed; that is not deletion of chronology. |
| Active delivery and later scheduling | Each delivery records its own chronology before its matching base helper (`evolution_effects.txt:824–886`). The log wrappers initialize their own context (`effects.txt:3234–3304`). Scheduler choice and delay use separate `brilliant_scientist_evolution_schedule_target` / delay variables (`evolution_effects.txt:659–767`). |

Every added shared enablement check is immediately preceded by explicit event ID, evolution type, stage, and tier assignments.
Nested project-seed calls can change shared temporary state, but the next seed block resets all four values before its own test (`evolution_effects.txt:189–254`).
The three lower-delivery blocks likewise reset all four values after base/seed processing (`evolution_effects.txt:598–637`).
Traced direct base, recorded-state, preparation, synchronization, scheduling, and delivery-completion callers do not consume an inherited pre-call evolution context after these calls without rebuilding it.
No current shared-temp context collision was found in those callers.
These helpers still leave shared context set on return; this review does not certify arbitrary future callers that assume the context is preserved.

## MCP and probability boundary

No new MCP request was issued by this worker during this pass, per the parent's explicit instruction while its graph/compare work was running.
The preimplementation handoff retains this worker's exact inspect/render artifacts and comparison blockers; those artifacts are not relabeled as post-patch evidence.
The parent reported a successful full helper baseline with revision prefix `741b7f43`, 18,859 indexed helpers, and a temporary-variable state-flow query returning zero accesses.
The full revision and artifacts were not delivered to this worker, so the prefix is only attributed parent status, not an independently inspected artifact or exact baseline identifier.
Zero temporary-variable accesses do not validate F2's snapshot transfer.
The reported 3,950 global diagnostics are not 3,950 proven Event 016 defects.
The parent reported that its cached `event_compare` returned `EVENT_REVISION_NOT_CACHED`; the required comparison gate therefore remains unpassed.
The parent owns the final inspect/render/compare evidence and the probability auditor's same-scenario comparison; the latter result was not available at this source checkpoint.
No probability balance target or weight was edited or certified here.

## Reviewed source bytes

| Path | SHA-256 |
| --- | --- |
| `common/scripted_effects/016_brilliant_scientist_effects.txt` | `9953d59e79cfc1e08e42be80bb56bbfa4411e9fea71cb5b8fa8a2b6182b95ab6` |
| `common/scripted_effects/016_brilliant_scientist_containment_effects.txt` | `15ec7ea15a9abca7d7c916a6f1dfdc872e540f643f96768919f74ba07092523e` |
| `common/scripted_effects/016_brilliant_scientist_country_effects.txt` | `29b2ae27fd1dfd914108d87a116df77cb0dcccb66e24456e153e5a4784297a44` |
| `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` | `6192259e7d657c77b951e40871ecef2cf691d3fe008beda40832a9c1fcfb66a9` |
| `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt` | `b888ab495bb1846e5289405e4f96d1fd5bc1af5b8f799a9000f3938ecec324b4` |
| `common/scripted_effects/016_brilliant_scientist_host_reaction_effects.txt` | `7ee4fca1a436a23e25cee8c74c9713f431ecefe001aaad35932fab28df3519c2` |
| `events/016_brilliant_scientist_host_reaction_events.txt` | `304f414dde65f73de59788157fb5902b600d30900bd880795adf8e24f499f550` |
| `common/scripted_effects/016_dhrondan_contact_effects.txt` — nested lock reference | `e287e95ecf46988609b5ef84743d31d41281914fe244e36539f6ba2cb85be66a` |

## Disposition and remaining work

The accepted contract remains unchanged; no new family, evolution, country, focus, meter, GUI, super-event, achievement, or fallback was introduced by this review.
The pending-only F4 remedy replaces the overly broad earlier reset suggestion.
R1 is resolved by the reasserted locks and direct source recheck.
Parent-owned MCP/probability comparison and final owner-handoff alignment remain separate closure gates; this audit does not waive them.
The updated `docs/events/016_brilliant_scientist/evolutions.md` was read and correctly describes the current Temporal and Alien Arms seed outputs as Prototypes, matching the inspected seed effects rather than the stale Deployment wording.
The cited canonical part 4 lines 485–493 describe an advanced Prototype opening; this documentation-only wording correction does not change gameplay seed counts or stage effects.
Portal transport design, model/audio/counter assets, focus layouts, the Directorate GUI, localisation, catalog exports, and overall Event 016 acceptance are outside this follow-up.
No new asset requirement was created and no asset completion claim is made.

Guidance used: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, and the previously consulted `chaos-redux-decisions-missions` lifecycle guidance.
They constrain the review to accepted design and distinguish source evidence from required MCP/probability evidence.
No skill was changed.
Required offline wiki and installed vanilla documentation references are retained in the preimplementation handoff; the material engine fact for F2 remains that `for_each_loop.value` writes a temporary iterator.
No game was launched, no logs were requested, and no user-run testing request was made.
