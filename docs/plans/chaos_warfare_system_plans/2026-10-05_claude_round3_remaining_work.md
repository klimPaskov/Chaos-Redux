# Chaos Warfare workstream remaining work - Claude takeover round 3 (2026-10-05)

## Scope and sources read

The controlling accepted design is `../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md` with its corrections folder, and `../../specs/chaos_warfare_system_specs/specs/12_ui_localisation_assets_achievements.md` for the accepted achievement set.
Status inputs were the spec package README, the Codex handoff `handoff_to_claude_2026-10-04.md`, the requirement ledger `2026-09-20_cbrn_overhaul_requirement_ledger.md`, the completion report `2026-09-25_cbrn_overhaul_completion_report.md`, the round-1 and round-2 status notes, `agent_decisions_2026-10-04.md`, the routed defect list, the takeover fix and review results, the stopped thread's final status record, and the 3-5 October live playtest record under `../../testing/live_qa/20261003_full_playtest/`.

## Routed defects: still closed at HEAD

The fifteen routed static-lint defects and the four effect/trigger-context load errors remain committed in `ccca51294` and present at HEAD.
No routed defect is unfixed, and no CBRN source file is uncommitted: the only working-tree entries in this workstream's area are the two untracked evidence files inherited from the stopped thread.
This round therefore opens no priority-1 routed item.

Two earlier open questions are settled by reading the installed documentation rather than the game:

- `rail_way` is a valid building name for a building-level read: the installed `documentation/triggers_documentation.md` lists it among the supported buildings, beside `bunker`, which the same workstream already reads in state scope after a vanilla precedent. The round-1 review's doubt about its validity is closed; only the weak ordering value of the check remains, and that is item 4 below.
- The rescaled death-rate families are consumed consistently. The military fraction is divided back to a real fraction before its own bound, so the achievement thresholds that read it compare real values; the civilian fraction stays scaled and reaches no consumer other than the shared state-deaths helper, which divides it after counting the population in people.

## Remaining work

### Priority 1 - accepted content that is absent

1. Four achievements in the accepted set have no runtime definition: The Air Is Still Breathable, No Wind Is Friendly, The Antidote Arrived and Unbroken Supply Corridor.
Eleven of the fifteen are implemented and complete, with names, descriptions, condition tooltips and sprites.
The four were dropped in July under a skip rule recorded in `2026-07-13_requirement_traceability_and_migration_ledger.md`, on the grounds that each needs a record the engine did not expose at the time.
That disposition was never checked against the surfaces the workstream has since built: the per-episode action records, the state contamination and expiry records, the protection snapshot, the Condemnation record and the commander service counters now exist.
This is accepted design with no implementation and no acceptance of its removal, so it is the one open content gap that does not need the live game.
Owners: `common/achievements/chaos_redux_achievements.txt`, `common/scripted_effects/cbrn_achievement_effects.txt`, `common/scripted_triggers/cbrn_achievement_triggers.txt`, `localisation/english/cbrn_achievements_l_english.yml`, the achievement sprite file, and the ledger row for the achievement requirement.

2. The division support category still reads "Chemical Tank Support Companies" although the eighteen companies that gave it its name are gone.
Only the three armored delivery detachments carry `category_chemical_tank_support_companies` now, so the category name the player sees in the division designer no longer describes its contents.
Either rename the category and its localisation key to the armored delivery role it now groups, or drop the category from the three units if nothing else needs it.
Owners: `common/units/cbrn_regimental_support.txt`, `common/unit_tags/chaosx_categories.txt`, `localisation/english/chaosx_units_l_english.yml`, and the two Chaos Warfare land subdoctrine files that reference the category.

### Priority 2 - asset and harness hygiene left by the removal

3. The removal left an orphan icon family: 63 registered sprites whose names describe the removed agent-specific tank companies, in `interface/chaosx_subuniticons.gfx` and `interface/chaosx_texticons.gfx`, and 45 texture files that no sprite references.
None is shared with a surviving sprite, and none has a consumer in script, history, localisation or interface files.
They are harmless at runtime but they are dead weight that the next unit author will copy from.
`docs/testing/chaosx_test_country.md` also still states the old unit and support counts; the file holds another owner's uncommitted paragraph, so the count needs a minimal replacement, not a rewrite.

4. The test-country facility candidate preference orders candidates by a railway or supply-node read that nearly every developed state satisfies, so it barely ranks them.
If the live run shows the native gate still refusing every candidate, the preference should rank by the conditions the native gate actually tests rather than by any positive railway level.

### Priority 3 - choices that belong to the user

5. Assault-battalion audio lineage. The runtime set ships because the current animations are timed to it; the archived set stays archived. Swapping it is a listening preference, and all nine files plus their timings move together.

## Live-game acceptance, carried forward

The orchestrator owns these; no agent launches the game.

6. Native raid lifecycle: exactly one equipment payment, and no double refund or free attack on cancellation, target loss, war end or stock shortage, including correct ownership of a paid transaction after a sale expires.
7. Cost rows against engine debits for the occupied, export, emergency, hospital, aid, diplomacy and theater families: the displayed price must equal the deducted price.
8. A real blocked refund driven through "Audit the Occupied Mask Accounts" and "Audit the Shipment to <partner>": the retry, the write-off counts and the reopening of both routes.
9. Test-country facility placement after the supply-connected candidate change, then naming the native rejection from the trace helper and removing the helper together with its caller.
10. Technology and doctrine presentation in the engine, and effective division statistics inside the accepted combined caps.
11. Contamination map-mode colours in a save after a Fallout sweep, and load cleanliness after the unit removal (no unknown unit and no missing texticon).
12. The Event 020 response board layout at the five accepted scenarios and both required resolutions. The GUI inspect and render routes were retried again this round and returned `Invalid tool arguments` for both the minimal inspect call and a narrow render call, so the route stays unusable from this client.
13. One in-game look at any interpolated constant in player-facing text. Vanilla ships the same construction in a tooltip, so nothing else is to be rewritten on this basis; the two converted files stay as working indirection either way.

## Not remaining

The rescaled biological, continuing chemical and agent-class rate families, the four quote-context repairs, the state-scope news repair and the three engine-variable repairs are committed and consistent with their consumers.
Famine and migration remains plan-only and is not authorized by this workstream; the swept-state reads in migration, famine and Event 014 belong to their own owners.
Event 026 stays disabled in the default allowlist behind its own cost-registry gate.
No catalog or spreadsheet change is warranted: no public event, evolution or cluster wording changed in this round.
