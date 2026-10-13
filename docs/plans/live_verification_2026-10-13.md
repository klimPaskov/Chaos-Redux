# Live verification, 13 October 2026

**Handoff 1 is incomplete.**
Five owned Linux launches reached the Chaos Redux main menu, and the recoverable parser failures were repaired and rechecked.
The final launch still contains mod-caused errors, so this report makes no clean-load statement.
Campaign entry, interaction, console dispatch and time progression have no verified route to this isolated Linux process, so the requested campaign screenshots, super-event playback, unit muster, terror-chain completion and two-year performance run were not delivered.

## Run configuration and evidence

The common handoff rules, restore plan, prior load/camp report, performance ranking and Linux live-testing guide were read.
The target was WSL Ubuntu-24.04, `/home/klim/games/hoi4/hoi4`, version 1.19.3, ELF Build ID `a4971c9e8ac9a6f2487dea109e01f9839ee59db7`.
Launches used the existing cache-backed launcher, private display `:91`, llvmpipe, debug mode and a 1920x1080 window.
The enabled playset was Chaos Redux plus HOI4 Live Telemetry, with zero active DLCs reported by the Linux game.
Windows HOI4, its settings and its running-session state were not operated.
The owner’s Windows logs were copied and reviewed read-only.

Clausewitz preflight accepted the exact ELF but reported a partial table with campaign/event acceptance incomplete.
Its current inventory marked only preflight, tool status, startup status, reviewed raw reads, command-catalog reads and private-window screenshots verified.
Console, game speed, pause, decisions, scientists, units and script-variable operations remained unverified.
The connected HOI4 Live Tools status identified the separate Windows installation, so it was not used as a Linux fallback.
No raw desktop/input bypass or unverified native call was used.

The first background start exited before fresh logs were written.
The documented persistent WSL shell route produced the successful launches below.
Owned game PIDs were 93977, 2123, 6214, 10566 and 11414.
The shared source continued changing during the run, so each native observation describes its loaded cache snapshot rather than every later checkout change.

| Native snapshot | `error.log` bytes | Observed result | Screenshot |
| --- | ---: | --- | --- |
| `launch_01` | 124,376 | Main menu reached. Trait and migration/famine parser failures exposed. | [Menu 1](../../.tmp/live_verification_2026-10-13/launch_01.png) |
| `launch_02` | 454,390 | Main menu reached. Migration helper/minimap fixes cleared. Current human-modifier parameter calls, GFX/music/encoding and missing contracts exposed. | [Menu 2](../../.tmp/live_verification_2026-10-13/launch_02.png) |
| `launch_03` | 18,969 | Main menu reached. Human-modifier family and registry failures cleared. Remaining small syntax, camp, occupation and quote failures exposed. | [Menu 3](../../.tmp/live_verification_2026-10-13/launch_03.png) |
| `launch_04` | 10,260 | Main menu reached. Recoverable camp/quote/category/occupation failures cleared. One newly introduced migration token remained. | [Menu 4](../../.tmp/live_verification_2026-10-13/launch_04.png) |
| `launch_05` | 9,175 | Main menu reached. Token warning cleared. Known source/art/build blockers remain. | [Final menu](../../.tmp/live_verification_2026-10-13/launch_05.png) |

Every `text.log` snapshot was empty.
Raw logs, timestamps, SHA-256 values, renderer information, exact source snapshots and repair-only patches are under `.tmp/live_verification_2026-10-13/`.
The final `error.log` is [launch_05/error.log](../../.tmp/live_verification_2026-10-13/launch_05/error.log), SHA-256 `294a9dcc17579eef4c439478e18091ada6e423ea98d1fcd7cbd1da18ba97337d`.
The final screenshot shows version `Operation Postern v1.19.3.0.c01a (20a5)` and the restored initial About viewport.
It does not show an active campaign.

The last owned game and private helpers were stopped.
Both Linux settings files were restored byte-exactly to the initial backup, and the matching lease was released.
[Cleanup evidence](../../.tmp/live_verification_2026-10-13/cleanup.json) records settings SHA-256 `ff1da04e251fdb0544ceb8144a3a5c5b5b2e9e1d7da43fb87012f782fa5e9350` and pdx-settings SHA-256 `6bb29af57dd7b1cc93c9a58fff9e6e1a1074601d98f3b4659a2d108cbd234bac`.
No push was performed.

## Requested pass/fail table

`Blocked` means the requested native action or screenshot was not obtained.
Source review and a main-menu screenshot are not substituted for campaign passes.

| Requested test | Result | Evidence or limit |
| --- | --- | --- |
| C1 clean load | **Fail / incomplete** | Final fresh log retains the blockers listed below. |
| Localisation collisions | **Pass, source inventory only** | 387 YML files, 85,315 unique entries and 5,606 scripted names. No duplicate groups. Final native text log empty. |
| Welcome window text | Blocked | No verified campaign-entry/UI route. |
| Main-screen About text | Partial | Initial viewport renders in all menu captures. Scrolling/full text was not exercised. |
| Chaos Redux help text | Blocked | Campaign interaction unavailable. |
| History rows contain event names only | Blocked | Event Logs not opened in a campaign. |
| Flag hover names the country the click pans to | Blocked | Hover/pan sequence not run. |
| Clusters omit Show control and subheaders | Blocked | Clusters view not opened. |
| Cluster member checkboxes and automatic-fire text spacing | Blocked | Checkbox/click/layout states not observed. |
| Auto event logs under Miscellaneous | Blocked | Settings interaction not run. |
| Super-event volume-arrow tooltips | Blocked | Hover state not observed. |
| Crisis pressure off by default and applies to all events | Blocked | Campaign default/wording not observed. |
| Chaos Meter history alignment | Blocked | Window not opened. |
| Condemnation description | Blocked | Tab not opened. |
| Deaths entry spacing | Blocked | Tab not opened. |
| World-end details positioning | Blocked | Scenario/details view not opened. |
| Launch Scenario button centered | Blocked | Native scenario view not obtained. |
| Chemical folder upper area matches `cd2f068437`, lower area consolidated | Blocked | Technology view not opened. |
| Biological folder has no disconnected cards | Blocked | Technology view not opened. |
| All scientists with levels and traits | Blocked | Scientist roster not opened. |
| Inhumane icon is the original | Blocked, native | No scientist/trait view capture. No icon was replaced by this run. |
| Chemical abilities usable by an army leader | Blocked | No army/leader action run. Intended soft-attack bonuses remain a separate parser blocker. |
| Restored biowarfare decision flow | Blocked | No decision interaction run. |
| Fast biological policy change | Blocked | No policy change run. |
| Biological raid starts without friction | Blocked | No raid action run. |
| Biological responses visible on map | Blocked | No active map response observed. |
| Migration picture inside its box | Blocked | Migration window not opened. |
| Migration/famine decisions appear only under real pressure | Blocked, native | Source cost/receipt cases preserved, but no native pressure scenarios run. |
| Migration/famine costs fuel or convoys, never PP | Blocked, native | Physical-cost helper cases passed in source fixtures. No native debit observed. |
| Every camp button works with no error line | **Incomplete** | No button clicks run. Belgian camp contracts still produce fresh load errors. |
| Fractures absent at Calm and increase/redder by tier | Blocked | Settings tier sequence not run. Minimap attachment parser error repaired. |
| Fractures avoid main buttons | Blocked | Campaign hit regions not observed. Geometry and art were retained. |
| Starting biological breakthroughs: JAP, ENG, USA, SOV | Blocked | No new 1936 campaign entered. |
| Starting chemical breakthroughs: GER, ENG, FRA | Blocked | No new 1936 campaign entered. |
| Germany has tabun | Blocked | Native starting-state inspection unavailable. |
| Japan starts unrestricted | Blocked | Native starting-state inspection unavailable. |
| Zombie outbreak super-event original audio/text/layout | Blocked | Event not fired. No playback capture or audible check. |
| Two additional super-events original audio/text/layout | Blocked | Neither additional event was fired. |
| `e chaosx_test`: all unit families at assembly sites | Blocked | Console/campaign route unverified. No unit-spawn claim. |
| C5 random terror chain to its end | Blocked | No chain was fired or advanced. Existing source repair remains distinct from live proof. |
| C4 speed 5 for two in-game years | Blocked | No game time advanced. No simulation benchmark or slowdown conclusion. |
| Save/reload and effect-state diffs | Not run | No active campaign/checkpoint created. |

Per-surface campaign screenshots are missing because those surfaces could not be reached through the allowed verified route.
The five menu captures are the actual screenshots delivered.

## Confirmed repairs and their limits

| Surface and files | Repair / provenance | Meaningful evidence |
| --- | --- | --- |
| `018_resources_found_decisions.txt`, `039_murder_mystery_decisions.txt` | Guard state-dependent AI lookups and absent assassin/terminal targets, preserving existing valid-target scores and blocked factors. | Read-only independent source audit. Valid resource scores remain 35, 240, 255, 620, 290 and 620 in the named cases. Murder major-target score remains 6, invalid target 0. These are scores, not probabilities. No campaign retest. |
| `013_natural_disasters_effects.txt`, `028_asteroid_incoming_runtime_effects.txt`, `032_missiles_effects.txt`, `035_great_depression_effects.txt`, `035_great_depression_decision_effects.txt` | Guard 63 actual removals for 33 diagnosed file/modifier pairs with same-scope presence checks. | The Windows log had 5,674 corresponding absence-removal rows. Present modifiers still receive the same removal, absent ones perform no removal. Native startup parser accepted the changes, but those runtime branches were not exercised. |
| Nine migration/famine scripts and four API docs | Replace rejected PROFILE/TARGET/RECEIPT dollar parameters with temporary numeric/scope/token inputs and native meta text. Retain exact payer/action/state receipt names and physical fees. | 50 production-body transport cases, 11 famine regressions through a temporary native-meta adapter, and pressure contract. Final native log clears this parser family. The maintained unadapted famine runner lacks meta-trigger support and its transport test fails for that tooling reason. |
| Four human-state modifier helpers, 89 common callers and one delivery event caller | Bare temporary-input helper calls replace MODIFIER/DAYS blocks. Retain actual human filters, targeted instances, arrays and saved expiry names. | 16 source lifetime/filter/cleanup cases. Native helper/caller parser errors clear. Country-specific modifier behavior remains unobserved in a campaign. |
| `chaos_ui_wear_scripted_gui.txt`, `chaos_ui_wear.md` | Restore the earlier `parent_window_name` attachment, retained in `4b054623^`. The installed documentation's `parent_window_window` example is rejected by this engine. | Fresh parser diagnostic disappears. Root `mini_map_interface` precedent inspected. No layout/art/geometry changed and no campaign visual pass claimed. |
| Three GFX registries, payload texticon wrapper, migration-priority locality and two music assets | Remove source BOMs, repair sprite wrapper enclosure, add required locality BOM, and remove invalid `.asset` station declarations while retaining the existing `.txt` station membership. | These observed parser/encoding errors disappear. Sprite paths, OGG bytes, song IDs, volume variants and station assignments remain intact. No audible super-event proof. |
| `migration_priority_effects.txt`, `chaosx_occupation_laws.txt`, `chaos_meter_constants.txt` | Correct `not_equals`, check targetless `scope_exists` within FROM, restore five exact combat multipliers from `76d2bc4a4^` / `15cdf416b`. | 29 source cases. Values remain 0.90, 0.96, 1.00, 1.08 and 1.16, not the different distribution ladder. Native diagnostics clear. |
| `chemical_warfare_categories.txt`, two category keys | Exact category restoration from `be6f9e53b`. | Existing original sprite/DDS consumed. Unknown-category diagnostic clears. |
| Camp responsibility triggers, site evidence resolver, French response mission/completion/timing/text | Exact contracts restored from `72aa7ba56` and `be6f9e53b`. Existing French launcher again has its actual 150-day mission and completion path. | Fresh corresponding missing-definition errors clear. Independent restored-mission AI score is unchanged at 0.00. Native mission/button outcomes were not run. Belgian dependencies remain unresolved. |
| Chemical direct-decision completion and doomsday target predicates | Reset caller-owned proofs and reverse exact PP debit only after no-release/no-stock-debit rejection. Preserve fee after real stock consumption and reject C6-classified nonhuman actors/states. | Source cases cover exact 100 PP success, full rejection refund, partial dispatch fee retention and stale proofs. AI formulas remain unchanged. Native physical target-type ROOT binding remains unverified. |
| Three occupied mask quote consumers | Use the existing quote trigger, remove its wrong-kind effect call and retain caller-owned quote outputs. | 16 production-body cases, including empty standalone payment/text frames and selected-state escrow. Formula, gates and text unchanged. Native missing-effect diagnostic clears. |
| Synchronized token table | Register explicit physical-transport decision inputs, including later administration/civilian additions. | Final native log has no corresponding dynamic-token/OOS warning. Other agents' Event 042 token work remains outside this job's commit. |

Exact changed paths, original bytes, source hashes, local reference spans, caller inventories and owned patches are retained in the named scratch handoffs.
These include [migration repair](../../.tmp/live_verification_2026-10-13/migration_load_repair.md), [human modifier repair](../../.tmp/live_verification_2026-10-13/human_modifier_load_repair.md), [final parser repair](../../.tmp/live_verification_2026-10-13/final_parser_repair.md), [camp/category repair](../../.tmp/live_verification_2026-10-13/camp_category_load_repair.md), [chemical contract](../../.tmp/live_verification_2026-10-13/chemical_decision_contract_repair.md), [mask quote](../../.tmp/live_verification_2026-10-13/mask_quote_repair.md), [Windows decision review](../../.tmp/live_verification_2026-10-13/windows_decision_review.md) and [localisation review](../../.tmp/live_verification_2026-10-13/localisation_review.md).

## Remaining failures, omissions and blockers

1. **Belgian camp contracts:** `bel_congo_resource_quota_cycle`, `bel_congo_transport_corridor_project`, `bel_colonial_strike_response` and `camp_rework_begin_belgium_strike_response` still produce fresh errors.
   Their historical dependency surface includes removed selection, start, completion, cost and country-action contracts, plus an unregistered icon.
   Restoring only names or disabling the actions would not restore the requested behavior, so no such substitute was installed.
   The full dependency recovery remains incomplete.
2. **Trait soft-attack-only intent:** the installed modifier catalog contains no documented soft-attack-only equivalent in the affected `sub_unit_modifiers` entries.
   General attack would also increase hard attack, so that substitute was rejected and reverted.
   The intended `soft_attack` fields remain rejected in the final log.
   Equivalent defence, supply-consumption and breakthrough name corrections are present in the working tree, but the incomplete trait repair was not included in this job's commits.
3. **Elephant build mismatch:** the owner’s Windows 1.19.2 definition is a frontline unit in `common/units/cavalry.txt`, whereas isolated Linux 1.19.3 defines `elephantry` as support in `common/units/recon.txt:863`.
   The exact restored frontline template therefore produces two Linux load diagnostics.
   Moving it to support or overriding the global vanilla unit would alter the requested formation/balance, so neither reduction was installed.
4. **Art:** MQC/MQT/MQE/MQO/MQN still produce 30 flag-loading rows across the two atlas passes.
   Their three-size ladders and the original Matignon DDS remain with [handoff 4's list](icons_needing_new_art_2026-10-13.md).
   The Belgian quota/strike icon is also recorded there.
   This run produced no substitute artwork.
5. **Unlocated runtime diagnostics:** the Windows log contains the historical `UPPER_LEFT` font and single `Ven` promotion diagnostics.
   No current literal font assignment or Ven bracket expression was established, and neither appeared in the menu-only Linux launches.
   Their campaign origin remains unresolved rather than declared fixed.
6. **Verified live route:** an active Linux campaign, UI interaction, event/console dispatch and bounded time controls are indispensable for the requested gameplay results and screenshots.
   The current route does not provide them.
   No Windows substitution, source preview or unloaded runtime artifact was counted as gameplay proof.

The remaining Linux DLC-backend, BLT game-rule and PRC character rows were traced to installed vanilla paths absent from the mod.
They are recorded separately from mod-caused rows, and no installed game file was edited.
The Windows log's SHA-256 remains `5f7e1cc59937d984bf7230929b5850f1a9221b655a234963a7074cb99545d0c9` after this job's read-only review.

**No gameplay simplification or substitute art was introduced by this run.**
The incomplete outputs and unresolved contracts above are explicit omissions/blockers, not approved reductions or passes.

## Commits, documentation and skills

- `878705d6892836e7efa5e2422c5dc1de5dc7ee34`: decision/scope guards, 63 modifier cleanup checks, minimap attachment, exact transport token registration, art dependency list and reusable cache-identity guidance.
- `1947065ccbd0947708c6c68308e27e905354ee5e`: recoverable camp/French/category definitions, chemical rejection accounting/C6 gates, occupied quote output handoffs and exact restored text.
- Concurrent restore commits that incorporated related shared-file fixes include `20cf3fba1`, `b3ca3d493`, `c130ce414`, `4ac3bafbd`, `587732e49` and `3d71316b5`.
  They are distinct from this job's commits and do not prove live campaign behavior.

Both owned commits used a temporary index and guarded `update-ref` publication.
Unrelated Event 042 tokens, text moves and other staged/unstaged work were preserved.
No screenshot, log, scratch test, source archive or checkpoint was added to Git.
The event catalog workbook was not changed because no player-facing catalog wording or availability approval was assigned by this verification run.

Skills used: debug-playtest, subagents, shared-git-commit, events, scripted-gui, event-assets, ideas-modifiers and official skill-creator.
Specialists also used decisions-missions, characters-leaders, units-divisions, map-states, equipment and native-raids.
Only the canonical debug-playtest skill was updated, with one generic loaded-cache/current-source identity rule.
Its full-file read was 13,170 tokens without truncation, and the existing sync/read-limit checks completed.
The parent performed that narrow update after the skill-maintainer role was unavailable.
The parent also reviewed the modifier cleanup directly after its specialist routing attempt failed without edits.

## Final status

The source repairs and actual native menu/log evidence are delivered.
C1, the campaign verification checklist, super-event playback, CXT muster, C5 live chain and C4 two-year performance run remain incomplete.
Further unchanged menu launches cannot establish the missing campaign results or remove the unresolved source/art/build dependencies.
