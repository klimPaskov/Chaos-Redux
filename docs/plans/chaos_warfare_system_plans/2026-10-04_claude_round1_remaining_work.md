# CBRN workstream remaining work - Claude takeover round 1 (2026-10-04)

## Scope and sources read

Disposition: items 1 to 11 are `implemented` with the commits listed under Round 1 outcome; items 12 to 15 stay `unresolved` until the orchestrator's live run.

The controlling accepted design is `../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md` with the corrections folder beside it.
Status inputs were the Codex handoff `handoff_to_claude_2026-10-04.md`, the requirement ledger `2026-09-20_cbrn_overhaul_requirement_ledger.md`, the completion report `2026-09-25_cbrn_overhaul_completion_report.md`, the routed defect list and the takeover fix/review results for this workstream.
All 15 routed static-lint defects and the four routed effect/trigger-context load errors are fixed and committed in `ccca51294`; spot checks confirm the engine reads, the rescaled rate families and their single consumers, so they are not reopened here.

## Agent decisions taken in this round

The sabotage AI target gate will call the actor-country contract directly as `ROOT = { bio_sabotage_actor_relationship_with_from_is_valid = yes }` instead of the raid-target wrapper.
Basis: the installed raid documentation guarantees `FROM` and `var:target_state` only inside the raid's own `ai_will_do`, `show_target`, `available`, `launchable` and `launchable_from` blocks, and the wrapper re-reads `var:target_state` from a nested country scope where that guarantee does not hold.
The physical state profile already performs the selected-state checks in the same predicate, so the direct country call keeps every restriction with no extra scope assumption.

The temporary CXT facility trace helper will be committed rather than deleted.
Basis: its caller is already in HEAD from another owner's commit `eb08e1dde`, so a checkout of HEAD without the helper logs an unknown effect; the helper is read-only, gated behind the existing explicit setup-trace flag, and is removed together with the caller once the construction rejection is identified.

The occupied and export quarantine markers will gain one bounded player-triggered reconciliation action instead of an automatic clear.
Basis: the accepted contract forbids blindly clearing quarantine, refunding unknown deltas and worldwide pulses, while a marker that is set and never cleared permanently removes a decision family from the game.

Per-subunit selection audio for the assault battalion will be recorded as an engine limitation rather than implemented.
Basis: vanilla selection audio is the global `select_army`, `select_vehicle` and `select_tank` sound-effect groups chosen by unit kind, and entity audio is attached to animation-state events, so no per-subunit selection hook exists that does not replace every country's infantry voices.

## Priority 1 - routed or blocking defects

1. The finished biological sabotage native-scope repair is still uncommitted, so the reported Country-only trigger errors are fixed only in the working tree.
Owners: `common/scripted_triggers/biological_sabotage_triggers.txt`, `common/scripted_triggers/biological_sabotage_raid_triggers.txt`, `.agents/skills/chaos-redux-native-raids/SKILL.md`, `docs/systems/cbrn_warfare/biological_warfare/biological_sabotage.md`, `docs/plans/chaos_warfare_system_plans/2026-10-04_biological_sabotage_native_scope_repair.md`, `docs/testing/2026-10-04_bio_sabotage_scope_*`.
The repair report also links a probability narrative that does not exist; the native-raid surface exposes no weighted adapter, so that limit is recorded instead of linked.

2. HEAD calls `chaosx_test_country_trace_facility_candidate` while `common/scripted_effects/chaosx_test_country_facility_diagnostics.txt` is untracked.

3. `cbrn_occupied_transaction_recovery_pending` and `cbrn_export_native_mismatch_@FROM` are set on blocked refunds and native mismatches and are never cleared anywhere in source.
The occupied programme is then unavailable for the rest of the game behind a hidden trigger, and the affected export recipient can never receive aid again, with no player-facing explanation.

## Priority 2 - player-visible gaps

4. The Event 020 response board tranche is uncommitted and lacks its matching before and after layout evidence for the five accepted scenarios at both required resolutions.
A narrow `hoi4.gui_inspect` of `black_plague_response_category_window` responded in this round (code `GUI_INSPECTED`, 19 inspected elements, 18 diagnostics, no blockers), so the evidence route works; its sibling-spacing finding and the hidden-element size reports still need review.

5. CXT provisioning cannot place `land_facility` or `biowarfare_facility`: both declare `need_supply`, and the search transfers a random foreign state that has no supply connection to a landless test country.
The candidate search should prefer CXT-owned, supply-connected states before any foreign transfer.

6. Six displays in `localisation/english/biowarfare_disease_containment_l_english.yml` still use raw `[?constant:...]` expressions, which the installed constants documentation does not support in interpolated text.

7. The in-game Warfare help page (`chaosx.help.body.warfare`) does not teach the accepted loop: three authorization policies with their command-power price and reassessment, exactly two raid categories, automatic stock-backed protection, and Condemnation consequences.

## Priority 3 - closure items

8. The CBRN procurement conversion and filter fixed-factory commitments still need their accepted-exception or factory-family disposition in the Event 026 registry.

9. The assault-battalion audio manifest and finalize handoff describe an obsolete repair, and the nine runtime consumers do not match the archived derivatives by format or duration.

10. The eighteen legacy agent-specific chemical-tank entries remain as inactive compatibility definitions although the accepted amendment removes them.

11. Raid outcome callbacks expose no division-to-headquarters pointer, so commander service and the prepared-army achievement stay country scoped; the player-facing criteria must say what is actually measured.

## Live-game acceptance, carried forward

The orchestrator owns these; no agent launches the game.

12. Native raid lifecycle: exactly one equipment payment, no double refund or free attack on cancellation, target loss, war end or shortage, and correct ownership of paid transactions after a sale expires.
13. Cost rows and engine debits for the occupied, export, emergency, hospital, aid, diplomacy and theater families: the displayed price must equal the deducted price.
14. Technology and doctrine presentation in the engine, and effective division statistics inside the accepted combined caps.
15. Load cleanliness for the dormant holder tag and dated scientists, the chemical facility shader response, and the CXT facility placement after the search change.

## Round 1 outcome

Every item's design choices and their basis are recorded in `agent_decisions_2026-10-04.md`.

| Item | Status | Commit | What remains |
| --- | --- | --- | --- |
| 1. Sabotage native-scope repair with the direct actor gate | implemented | `3137c7996` | The disappearance of the Country-only warnings is a live-load check. The source tests pass 106 of 106 against the current source. |
| 2. CXT facility trace helper | implemented | `533549db3` | Remove helper and caller together once the orchestrator's trace names the native rejection. |
| 3. Occupied and export record audits | implemented | `329048c82` | The native return and write-off counts during a real blocked refund are a live-game check. |
| 4. Event 020 response board | source change implemented; visual acceptance unresolved | `4e54aacd5` | Category-level visibility is reviewed in source because the GUI fixture cannot set the country and global flags the gate reads. The pre-change inspect and its one spacing finding are real, and the fix is correct in source, but no post-change inspect and no render of any resolution exists; the route was rejected again on 2026-10-05. Corrected by review on 2026-10-05. |
| 5. CXT supply-connected placement | implemented | `23a9383ce` | Whether the native gate now accepts a candidate is item 15's live check. |
| 6. Containment maxima | implemented | `de73c23f9` | None. |
| 7. Warfare help page | implemented | `858cca927` | None. |
| 8. Procurement factory commitments | implemented as accepted exceptions | `ca65fd278` | None. |
| 9. Assault-battalion audio lineage | implemented | `e0af506e4` | Choosing which audio lineage ships is a listening decision for the user. The package manifest under the ignored `docs/assets/` folder is updated on disk only. |
| 10. Legacy chemical-tank companies | implemented as a recorded exception | `5bdc93d89` | Removal waits for a coordinated change to the synchronized token list. |
| 11. Commander service wording | implemented | `42b516034` | None. |
