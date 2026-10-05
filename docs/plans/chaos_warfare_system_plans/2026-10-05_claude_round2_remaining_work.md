# CBRN workstream remaining work - Claude takeover round 2 (2026-10-05)

## Scope and sources read

The controlling accepted design is `../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md` with its corrections folder.
Status inputs were the spec package README and manifest, the Codex handoff `handoff_to_claude_2026-10-04.md`, the requirement ledger `2026-09-20_cbrn_overhaul_requirement_ledger.md`, the completion report `2026-09-25_cbrn_overhaul_completion_report.md`, the round-1 status table `2026-10-04_claude_round1_remaining_work.md`, the routed defect list, the takeover fix and review results, and the stopped thread's final status record.

## Routed defects: all closed in HEAD

The fifteen routed static-lint defects and the four routed effect/trigger-context load errors are committed in `ccca51294` and verified present at HEAD by direct source reads:
the doomsday AI morale gate reads `has_war_support`, the battlefield operation target reads `bunker`, the protection target uses `limit_to_victory_point`, the three quote helpers are no longer called as effects, and the trigger-side affordability check uses `universal_cost_component_is_affordable`.
No routed defect is unfixed or fixed only in the working tree, so this round opens no priority-1 routed item.

## Owner working tree at this round

No CBRN source file is uncommitted.
The working tree's CBRN-adjacent entries belong to other owners: `docs/testing/chaosx_test_country.md`, the Event 020 rat model and entity files, and the repository-wide line-ending churn in `localisation/english/chaosx_gui_l_english.yml`.
The two untracked files from the stopped thread, `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-03_cbrn_immediate_protection_probability/parent_before_evaluate_request.json` and `docs/testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/startup_error.json`, remain untouched.

## Audits run this round

These were mechanical sweeps over current source, not re-verification of finished work. Each one could have failed.

| Audit | Scope | Result |
| --- | --- | --- |
| Achievement presentation | 11 Chaos Warfare achievements | Every `_NAME`, `_DESC` and `happened`/`possible` tooltip key exists; all sprite families registered. |
| Sprite binaries | 184 registered `cbrn`/`chaos_warfare` sprites | All `texturefile` paths resolve to existing files. |
| Localisation references | 236 CBRN, chemical and biological script and GUI files, 643 key references | No unresolved key; scripted-localisation getters accounted for. |
| Player-visible flag tooltips | 10 CBRN decision files | No unlocalised flag inside `available`, `allow` or `bypass`; the eleven raw flag reads all sit in `visible`, which the engine does not tooltip. |
| AI weights and icons | 32 CBRN decisions | Every actionable decision has `ai_will_do` and `icon`. The one exception, `cbrn_answer_inspection_demand_mission`, is a pure countdown with `available = { always = no }`, where `ai_will_do` has no meaning. |
| Engine variable reads | CBRN and raid files, against the installed dynamic-variable documentation | One real defect, fixed below. The remaining 24 suspects are caller-supplied contract inputs, `get_supply_vehicles_temp` outputs, or meta-effect assembled names. |
| Raid payload tokens | every `essential_equipment` block in `common/raids/` | All CBRN tokens resolve to defined equipment. |
| Decision categories | CBRN decision files | Every category is registered. |

## Defect found and fixed this round

`total_equipment_produced_gas_mask_equipment` is not an engine variable.
The installed dynamic-variable documentation defines `total_equipment_produced_<equipment type>` over the equipment type enum, and `gas_mask_equipment` is an archetype of type `support`, not a type.
The read returned zero, so `cbrn_doctrine_mask_production_baseline` was stored as zero at doctrine adoption and `cbrn_chaos_warfare_has_post_adoption_mask_production` compared zero against zero and was always false.
The archetype also carries `is_buildable = no`, so no cumulative production figure for it could exist.

The predicate had no caller anywhere in script, and no accepted requirement asks for a cumulative-production proof; it is a leftover of the retired reserve-and-formation establishment package whose neighbouring compatibility name is the only part Event 027 still reads.
The baseline assignment, the predicate and its helper-reference entry are removed rather than rewritten, because the engine exposes no per-archetype cumulative production figure and a stockpile reading would not mean what the predicate's name claims.

## Remaining work

### Priority 1 - player-visible acceptance that only the live game can settle

1. Native raid lifecycle: exactly one equipment payment, and no double refund or free attack on cancellation, target loss, war end or stock shortage, including correct ownership of paid transactions after a sale expires.
2. Cost rows and engine debits for the occupied, export, emergency, hospital, aid, diplomacy and theater families: the displayed price must equal the deducted price.
3. A real blocked refund driven through "Audit the Occupied Mask Accounts" and "Audit the Shipment to <partner>": the retry, the write-off counts and the reopening of both routes.
4. Load cleanliness for the dormant scientist holder tag and the dated scientists, plus the disappearance of the Country-only sabotage trigger warnings.
5. CXT facility placement after the supply-connected candidate change, then naming the native rejection from `chaosx_test_country_trace_facility_candidate` and removing the trace helper together with its caller.

### Priority 2 - evidence routes blocked from this session

6. Event 020 response board post-change layout evidence for `black_plague_response_category_window`.
   The source change is in `4e54aacd5` and its spacing fix is correct in source, but no post-change inspect or render exists at either required resolution.
   This round retried the route four times with different argument shapes, including the minimal call with only `windowName`: every call returned `Invalid tool arguments`, while `hoi4_source_lookup` answered normally at revision `fc979ea536b5` and resolved the window at `interface/020_black_plague_response.gui` lines 25 to 190.
   The GUI inspect and render routes are therefore unusable from this client, not merely slow. The remaining acceptance is a live look at the five accepted scenarios.
7. Technology and doctrine presentation in the engine, and effective division statistics inside the accepted combined caps.
   Source upper bounds fit every cap; engine aggregation, commander-skill conversion and equal-cost battle outcomes are unproven, and `hoi4.tech_compare` has never returned a cached revision for this mod.
8. The `[?constant:...|format]` question. One in-game look at any interpolated constant settles whether the mod's 7,025 reads across 86 localisation files render.
   Vanilla ships the same construction in a player-facing tooltip, so the two CBRN files converted to getters are kept as working indirection and nothing else is to be rewritten on this basis.

### Priority 3 - owner closure items

9. The in-game Warfare help page quotes `5` Command Power, `90` days, the `0`-`1000` Condemnation scale, the three-times concealment ceiling, `180` days and `5`% to `15`% as literals, although `GetCBRNPolicyChangeCostQuote` and `GetCBRNPolicyReassessmentDaysQuote` already exist beside them.
   Every quoted number matches its constant today, so this is a tuning-drift risk rather than a wrong display.
   The key lives in the shared `localisation/english/chaosx_gui_l_english.yml`, which currently carries 333 lines of another thread's uncommitted line-ending churn on the same lines, and another thread has already committed against this same key.
   It stays open until that churn is committed or the key's owner takes it; editing it now would entangle their diff.
10. Assault-battalion audio lineage. The nine runtime consumers are 32-bit float and the archived derivatives are 16-bit PCM with eight of nine durations differing. No runtime file was replaced. Which set ships is a listening judgement; per-unit selection audio is recorded as an engine limit.
11. `docs/testing/chaosx_test_country.md` still lacks the CXT facility placement change, because the file holds another owner's uncommitted edits. The change is recorded in the CXT audit note instead.
12. The eighteen legacy agent-specific chemical-tank entries stay as a recorded accepted exception until a coordinated change can renumber the ordered token list in `common/synchronized_dynamic_tokens/chaosx_tokens.txt`.

## Not remaining

The occupied transaction array only accumulates forward, so a fee row stuck before `329048c82` has no entry to audit. This is acceptable for a project that is validated in new saves.
`rail_way > 0` in the CXT candidate preference is a valid state read of a real vanilla building and matches existing use in two other owners' triggers; it only orders candidates, and the native gate still decides.
No catalog or spreadsheet change is warranted: no public event, evolution or cluster wording changed in this round.
Famine and migration remains plan-only and is not authorized by this workstream.
Event 026 stays disabled in the default allowlist behind its own universal cost-registry gate, which belongs to that workstream.

## Round 3 status update (2026-10-05, after the October live playtest commit)

Commit `e1413d2a3` added the 3-5 October live playtest record (`docs/testing/live_qa/20261003_full_playtest/`), and the matching run log is in the user's game log folder.
Its snapshot base `fa833647e` contains this workstream's commits `cab3acb5b`, `a35f1b277` and `3137c7996`.
A full 1936 run on that snapshot logs none of the three errors those commits addressed: no Country-only scope lines from the sabotage triggers, no flag-lookup errors for the dormant scientist holder tag, and no runtime recruitment warnings from the startup history effects.
Priority-1 items 4 (load cleanliness, holder tag and dated scientists) and the sabotage half of item 1 are therefore closed by supplied evidence.
The same run never entered the test-country harness, so facility placement stays open.

The playtest records one defect that reaches a surface this workstream owns: the Contamination map mode draws no colour in a post-strike world (`bugs.md` B037).
Its nuclear branch reads `has_dynamic_modifier = { modifier = nuclear_fallout_state }` through `mapmode_state_has_nuclear_contamination` in `common/scripted_triggers/cbw_triggers.txt`.
`common/scripted_effects/fallout_consolidated_effects.txt` line 16915 applies the state marker through `chaos_meter_apply_nuclear_fallout_to_state`, and line 16916 removes it again in the next statement, so every state hit by the manual aggregate path keeps its intensity and expiry variables but loses the marker the map mode reads.
Those two lines belong to the Fallout owner, whose commit `c7da5a541` only wrapped the existing removal in a presence check, so the order predates it.
The repair is theirs; this workstream owns the reading trigger and should confirm the mode colours once the marker survives.

The Event 020 board inspect route was retried once with the minimal call carrying only `windowName`, and returned `Invalid tool arguments` again, as in the two previous rounds. No further attempt was made.

## Implementation pass (2026-10-05)

Contamination map mode (B037, this workstream's part): implemented on the consumer side, see `agent_decisions_2026-10-04.md` section 14.
The Fallout marker removal turned out to be accepted Fallout design (spec 68 line 69), so the routing note above is superseded: the Fallout owner has nothing to change, and the nuclear branch now also reads the live intensity and expiry record that the sweep keeps.
The colours remain a live-game check in a post-sweep save.
Warfare help page figures (priority 3 item 9): implemented, see section 15. The blocking churn was line endings only, so the edit did not entangle another diff.
Harness document placement rule (priority 3 item 11): implemented, see section 16. The Event 029 paragraph in the same file stays the other owner's uncommitted work.
Assault-battalion audio (priority 3 item 10): decided, see section 17. The runtime set ships; a user listening preference can still reopen it.
Legacy chemical-tank entries (priority 3 item 12): implemented, see section 18. The eighteen companies, their trigger file, tokens, localisation, sprite aliases and orphaned textures are removed, and Event 027's eighteen always-false force-fit reads go with them. The token-renumbering premise of section 8 did not hold, so no coordinated pass was needed. The other owner's 136 uncommitted lines in `common/synchronized_dynamic_tokens/chaosx_tokens.txt` stay uncommitted; only the three removed blocks are committed. Load cleanliness after the removal is a live-game check.
