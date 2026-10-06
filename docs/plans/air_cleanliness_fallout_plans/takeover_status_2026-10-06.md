# Fallout takeover status — 2026-10-06

Disposition: source fixes and asset integration in progress; the workstream is not declared complete.
The current task authorizes finishing the interrupted October takeover, applies G1–G8, and assigns the Fallout-owned files and any inherited hunks to this workstream.
Initial owner-path status was clean; no stopped-thread owner hunk was silently discarded.
The Fallout inbox contained the quality rules, with no routed L finding; neither final-status JSON supplied a Fallout-specific unfinished-thread entry.

## Publication

Focused core, graphics, and final-status commits are recorded here after their isolated shared-tree publication and adversarial review.
Catalogue wording remains in `catalog_changes_pending.md`; the workbook and export-only CSV files are untouched.

## Current source findings and changes

| Surface | Finding and source change | Evidence limit |
| --- | --- | --- |
| Manual scenario 14 | Settings wrapper ignored the slider; it reads the selected intensity. Forced rejection explains no additional launch through report 905. | Exact native strike sweep and countdown need live observation. |
| Ash-week | Five separate acknowledgment reports added noise. Their immediate resolutions are silent; five choices and one closing report remain, with actual per-step results and the named office. | MCP event trace is focused/partial; native queue and save/reload behavior unobserved. |
| Country/office coverage | October source contains the deterministic tag/geography memory mapper, all 108 orientation cells, 360 candidate titles, six office-role arcs, and eight major-memory openings. | This does not satisfy the entire queued memory library or accepted character-content budget. |
| Winter inheritance | Regional, school, rail, dam, refinery, reactor and furnace outcomes were queued. Twenty-five existing state inputs feed the first account once per distinct outcome; mixed site losses are retained. | Original refugee identity/focus/migration consumers remain open. |
| Scheduler | Nonpositive scores were rejected by both the selector and later receipts. First eligible selection, ordinary reservation/receipt and numerical-row checks now preserve signed scores. | Required same-scenario probability comparisons failed with `Transport closed`. |
| Relief votes | Two automatic votes could pass without a live-member majority or actual supplies; cancellation lost the PP fee. Strict majority, a payable peaceful donor, neutral unfunded results and one-time saved refunds are implemented. | Native costs, deliveries and flag expiry require live checks. |
| Reconstruction | Concurrent delegates overwrote a recipient; cleanup could clear another sender; refusal duration used a bare temporary token. One exact participant pair, carried target/generation checks, matching loss cleanup, literal duration and closed-answer notices are implemented. | Native annex/capitulation and asynchronous reply behavior unobserved. |
| Verification | Equipment loss could reopen the same response indefinitely. A missing-supplies report now closes the visit without a finding. | Stale selection must be exercised in multiplayer or a controlled console case. |
| Treaty presentation | Nine flat families and hidden equipment payments. Six callable families are staged per recipient/phase; legacy costs share per-component affordability and native icons. | Target clones, simultaneous project density and final panel fit are not visually accepted. |
| Climate setting | Reset did not clear the owned static-weather preference. The single shared reset assignment restores its default. | Settings inspection returned source evidence; render failed with `Transport closed`. |

Design reasons and acceptance are recorded in `agent_decisions_2026-10-05.md`.
Current source mechanics are also documented in `docs/systems/air_cleanliness/fallout_start_and_treaty_recovery.md`; the Winter, treaty, implementation-status and B12 documents are reconciled with these source facts.

## Meaningful checks

`python docs/plans/air_cleanliness_fallout_plans/scheduler_source_cases_2026-10-06.py` executes thirty inheritance cases, thirteen production selector/score conditions, and four saved-refund cases.
The inheritance cases cover repeated application, ten identical sites, occupied holdings, opposing outcomes at 0/99/100 Cohesion, material tradeoffs, and the original seed memory beside industrial recovery.
The selector cases preserve priority/id/target/partner tie ordering and reject a nonzero score for an empty selected id.
The refund cases consume the saved fee before credit and cannot credit it twice, including a stored quote different from the current ordinary fee.
These are bounded production-source cases with native primitives and explicit registry/scoring fixtures; they are not probabilities or executed HOI4 behavior.

The report-colour audit reports zero reached Fallout parchment keys carrying U+00A7.
Independent localisation review verifies all 972 orientation cell strings and their selectors, all 360 candidate names, the office and major-memory roots, and the final closure's plain-text reach.

The parent event trace for `chaosx.fallout.78` returned `EVENT_INSPECTED_PARTIAL`, revision `c2dc5badf85f77bed593ecd22f10ae795f1e488f2023fbdb5698b13f2bb30f49`, with zero indexed helpers and an explicit focused-analysis boundary.
Its complete transport bytes were retrieved and hash-verified; the scoped excerpt and reference evidence are under `subagent_handoffs/mcp_2026-10-06/`.
An event-64 options render also returned partial evidence; the after comparison returned `Transport closed`.
The probability auditor retained exact HEAD source blobs and named reconstruction, relief and signed-score scenarios; inspections supplied adapter/source coverage, but evaluate/sweep/compare produced no completed scenario evidence.
The settings source inspection succeeded on shared revision `0bd843f89f50f5651e90cdf11a3c63363c0137cfaa1c455b1a6c8f620720ecb0`; its requested 1920×1080 raster did not return because the transport closed.
Additional worker event/GUI requests stalled or failed; no source-only report is promoted to the missing visual or engine proof.

## Exact orchestrator live checks

The supplied base `qa_001_fresh_head.hoi4` was read with the save-inspection skill's `info` command.
It is a text save, USA/democratic, dated 1936.1.1.12 on HOI4 1.19.2.0 (Operation Postern), normal difficulty.
No game or desktop window was opened by this pass.

1. **Admission and intensity:** use separate copies of the base for Low and Maximum. Open Settings → Scenarios → #014 Fallout, choose the intensity and confirm. Expect every valid province to be struck in both, with differing aftermath severity. Inspect `global.fallout_manual_selected_intensity` in the resulting text saves; it must match the chosen stop. In an already admitted/collapsed copy, console `event chaosx.fallout.900 USA`; expect one “Strike Order Withheld” report and no additional strikes.
2. **Exact sweep and map return:** from Maximum, let the native drops settle. Save after the final drop and after the countdown. Expect 10,154 observed strikes, 1,081 struck states, state strike sum 10,154, one aggregate nuclear-use count, and the seven-day countdown before blackout/map return. Check that wars end, population loss is not repeated, the existing railway/supply collapse occurs, and player continuation keeps a playable country.
3. **Orientation:** continue as human USA after map return. Expect choices 62, 66, 70, 74 and 78 and one closing report 82; acknowledgments 64/68/72/76/80 must not pop up. The closure must identify the installed office and match actual mixed outcomes. Save between two components, reload and finish; expect no repeated choice or duplicated starting-memory gain. The Event Log retains component results. Follow an AI survivor too: its hidden twins must finish without player popups or a scheduler error.
4. **Inheritance fixture:** before a Low launch, select a state that will remain owned/controlled and seed one existing regional or industrial outcome using the console's `eval_effect` facility, for example `USA = { random_owned_controlled_state = { set_state_flag = air_winter_memory_refinery_shutdown_result } }`. Record that state's id in the prelaunch text save. After orientation, expect the corresponding closure line and Scrap +2 in the first-account change. Use two distinct retained states for `air_winter_memory_phase_1_success` and `air_winter_memory_phase_1_failure`: their Cohesion changes must net to zero. Re-running orientation advancement must not apply either again. An occupied site contributes nothing.
5. **Country packages:** from a USA continuation expect Federal Continuity rather than the generic tree. Inspect AI NZL after a normal snapshot: when its exact five-state footprint and controlled Samoa qualified, Samoa must have been released before the snapshot and NZL must receive the Lifeboat package. A human NZL copy keeps its reserved-player path. Confirm no foreign coordinator receives NZL states or units.
6. **Ordinary pacing:** after orientation and the existing quiet period, follow a human and an AI survivor for several months. Expect distinct openings, at most three visible stages per ordinary office/major-memory chain, no repeated opening from the same receipt, and hidden AI closure. Exercise a high-fatigue case with zero or negative eligible scores and verify dispatch does not invalidate the numerical row. The full ten-year run remains the accepted 115–147-beat pacing observation.
7. **Treaty menus and payments:** use the untouched base, form a three-member and then a four-member Air Cleanliness Treaty through its normal decisions. With no active projects expect the one-donor convoy below four and the pooled brigade at four; sampling and seed work share their policy slot through grid work/active/cooldown. In a recipient's Phase 4 priority state expect a relief vote; at Phase 5/6 expect evacuation. Start a project before a threshold changes and ensure it remains visible until native completion/cancellation. Check support, convoy and free-factory cost colours just below, exactly at and above the fee; each actual debit occurs once.
8. **Relief outcomes:** in four-member copies test two yes/two abstain with a payable donor, then three yes/one abstain. The first fails quorum; the second delivers only paid peaceful pledges, at most four. Drain willing donors before the 21-day close: expect the unfunded report, no aid, no recipient penalty, one refund of the caller's saved 25 PP, no 180-day target lock, and the caller free again after fourteen days. Invalidate the recipient by war/control loss and verify the same one-time refund. Repeated cancellation must not mint PP. A completed political rejection retains its ordinary penalty and cooldowns.
9. **Verification stale choice:** open treaty response 6 while its paid option is affordable; consume the required response equipment before selecting it. Expect one missing-supplies notice 8, then a closed inspection with no second event 6 and no finding against the member. The travel equipment remains spent; response equipment is not taken.
10. **Pooled aid and betrayal:** pledge into one exact Phase 3-or-worse state, then test delivery, too few pledges, control change, member withdrawal, sponsor annexation and Fallout pause. Expect one result per involved country and appropriate material refunds. A banned/violator holder stops aid and records the existing Condemnation consequence, with no repeated member report from the same project.
11. **Reconstruction pairing:** after Fallout, use current survivors retaining `air_cleanliness_treaty_ever_member` and no ban. Propose A→B, then attempt C→B and B→C: both must remain unavailable while the first pair is reserved. Test accept, refusal, loss of A, loss of B, and capitulation of each; surviving A recovers its Recognition deposit once on failure/loss and only the exact pair is cleared. A stale answer gives the closing acknowledgment/notice rather than affecting a later sender. After refusal the same pair becomes available only when its 365-day flag expires.
12. **Climate setting:** open Miscellaneous, toggle Static Winter Map and observe the next existing monthly update: weather particles stop while phase ground/vegetation/water cues remain. Reset All Settings; the checkbox must be unchecked and weather resumes through the same monthly lifecycle. Confirm the row, hover tooltip, click region and text fit at 1920×1080 scale 1 and the other supported resolutions.
13. **Graphics and achievements:** inspect every generic focus icon and its shine state, all five USA decision miniatures, the USA category and both NZL rescue miniatures. Force or naturally reach representative repaired report events (Working Machine, Dead City Permit, Orchard Flowers, Health Without Borders, Door List, Open the Sealed City): expect valid, upright framed sepia art without baked text. Inspect all seven accepted achievement triplets and unlock their source-backed conditions; the three prerequisite-route achievements remain explicitly queued.

Use fresh copies rather than attempting the destructive sweep twice in one world.
These checks are for the orchestrator; the agent neither ran nor requested a live user test during implementation.

## Remaining issues, omissions and blockers

The full workstream remains incomplete until its open content and evidence gates are resolved.
The second country-memory chain per major and the wider two-chain-per-spawnable-successor library are still queued from A17, not implemented by this finishing patch.
The accepted fifty-character/leader-block coverage goal is not promoted from six institutional office arcs or broad library counts without its required authored coverage proof.
The original A20 refugee policy/migration outcomes still need successor identity, focus and migration-allocation consumers; this patch supplies the queued site-recovery starting-account outcomes only.
The three baseline achievements lacking their prerequisite routes remain accepted and queued as recorded by A21, rather than being awarded for substitute conditions.
Settings final raster, matched before/after visual evidence, probability evaluate/sweep/compare, event helper/lifecycle coverage, native blackout exclusivity, literal lobby-host authority and railway-topology execution are not proven.
The staged native category does not eliminate multiple eligible targeted rows or impose a universal project-count cap; panel density requires the blocked native visual review.
Grounded source portraits remain explicitly pending the user's styled finals; they are not final painted portrait completion.

## Skills

Used: events, decisions/missions, subagents, shared Git commit, MTTH, scripted GUI, focus trees, event assets, save inspection, and the asset workers' ImageGen/portrait workflows.
No super-event was added: the accepted Fallout consequence is independent of the ordinary super-event framework.
