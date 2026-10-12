# Chaos Redux text restoration evidence, 12 October 2026

The owner authorized exact historical restores for A1, A2, the text part of A3, and B6, without new prose, art changes, pushing, or launching HOI4.
The change restores 9,218 existing localisation values across 240 files, restores five deleted Holy Realm output keys and their exact getter, and aligns 52 catalog cells.
Every changed existing value was compared by key with the parent of its offending commit.
New keys, genuinely new mechanic sections, live value bindings, and concurrent assigned work were preserved.

## Assigned items

| Item | Historical source and outcome | Restoration commits |
| --- | --- | --- |
| A1 | Help: parents of `fc0759fe42`, `3098ed9d2b`, `3fa627e5aa`, and `d0fc5e0ec3`. Later timer-reset, Force Mode, and shortcut instructions retained verbatim. Main-screen About already uses the Welcome key restored in `b9258e251e`, so no extra About rewrite was needed. | `440fe01242ca41c7a65c30a29f1fc4540e44014b` |
| A2 | September–October wording sweeps and mixed commits listed below. Exact parent values with supported current numeric bindings. Orders from Unknown Hands description/options additionally restored from `1b87b3f5c^` (`1cb65e610120894598ff48d2808a3af3fa04d897`), retaining its current title. | The system commit table below, plus audit fixes `442c8a9e1d09271dd0f5c8919010c502d1364911`, numeric formatting `8f676ea5258b0fff06b66f14288556db500235e6`, and catalog `3a0a56a5c5ef9b8e66945cecdb0e7e828ccc384e` |
| A3 text | Remaining changed descriptions restored from parents of `3098ed9d2b`, `de40e3899b`, `7b8c66f67c`, `ff2045031a`, `ba94f5d1b4`, and `80cc98a99d`. The existing `63188d7cdc` and `0792029bab` historical restores remain. | `c0fd59ec9b41600bd05e7911800dfeaf0383d46d` |
| B6 | Narrative overrides introduced by `6b9dbffb8`, `e43372952`, `3098ed9d2b`, `8a4fb625cf`, and `477584cac` were removed. Selector matches `6b9dbffb8^` exactly, retaining the cluster branch and generic event-name branch. Event metadata, actor selection, and recorded payloads remain. | `78e6554affd48ebcce7191ccded8c564353ac447`, `442c8a9e1d09271dd0f5c8919010c502d1364911` |

## Sweep inventory

Scanned all 916 localisation commits in the audit window and selected 123 commits containing in-scope existing-key wording changes.
[chaos_redux_text_restore_2026-10-12_keys.json.gz](chaos_redux_text_restore_2026-10-12_keys.json.gz) contains every selected commit's complete old/new changed-key pairs, each restoration's source parent and final disposition, workbook cell deltas, and source revisions.
The August Orders supplement and July history-selector baseline are explicit exceptions to the audit window requested by the owner.

| Offending commit | Date | Existing values changed | Commit subject |
| --- | --- | ---: | --- |
| `2daa4b0a0d` | 2026-09-08 | 7 | Clarify Event 006 localisation surfaces |
| `fc0759fe42` | 2026-09-13 | 1 | Compact Event Details and clarify system help |
| `3098ed9d2b` | 2026-09-13 | 1091 | Commit accumulated mod, tooling, and documentation work |
| `33b6946dd9` | 2026-09-22 | 186 | Update |
| `98790f5c50` | 2026-09-25 | 2 | Improve Event 021 popup descriptions |
| `87910f96e8` | 2026-09-26 | 60 | Clarify CBRN raid and captured-facility presentation |
| `41d972cb2d` | 2026-09-26 | 18 | Bind occupation costs and consequences in localisation |
| `62d4d39599` | 2026-09-26 | 4 | Clarify Event 016 biological raid outcome tooltips |
| `5b4f69f1b3` | 2026-09-27 | 10 | Clarify Event 020 plague and Rat King public text |
| `a8f97f35d5` | 2026-09-27 | 80 | Fix Black Plague timed cancellation and clarify CBRN raids |
| `4a4676ce70` | 2026-09-27 | 1 | Shorten active CBRN MIO branch heading |
| `26ac17214b` | 2026-10-03 | 11 | Fix live-QA startup warnings, scenario labels and runtime error spam |
| `e9264c9fef` | 2026-10-03 | 70 | Fit triggerable scenario texts to the scenario window boxes |
| `a54cf96586` | 2026-10-04 | 32 | Remove receipt and ledger wording from Event 24 player text |
| `d025fe673c` | 2026-10-04 | 1 | Plain Event 028 closeout wording and queue its catalog row update |
| `145d7d530f` | 2026-10-04 | 26 | Write Acid Rain player text in plain words |
| `33e02046a8` | 2026-10-04 | 18 | Name the Event 31 movement directly in its in-world text |
| `841f0194b1` | 2026-10-04 | 32 | Replace engineering terms in Fallout player text |
| `9d9b5116ee` | 2026-10-04 | 18 | Say plainly what blocks camp orders and fit Records text to its rows |
| `b4311cd819` | 2026-10-04 | 50 | Polish Event 039 player text and drop the legacy opening news |
| `35cc24c16f` | 2026-10-04 | 22 | Plain wording for Acid Rain player text and achievements |
| `2a2ca9ac56` | 2026-10-05 | 105 | Remove implementation wording from Event 016 player text |
| `1c93a891ea` | 2026-10-05 | 16 | Tighten the Event 016 doctrine order and incident wording |
| `9c819314be` | 2026-10-05 | 100 | Say who died instead of naming the Deaths ledger in Fallout text |
| `56a20a625d` | 2026-10-05 | 22 | Remove leftover implementation wording from Event 016 and D'Rhondan text |
| `b5fb212495` | 2026-10-05 | 11 | Use plain current wording in Event 014 tooltips |
| `3fa627e5aa` | 2026-10-05 | 10 | Repair shared Event Logs, Settings feedback and crisis map presentation |
| `d872c806e8` | 2026-10-05 | 1 | Describe Chaos totals and pollution contributions plainly |
| `41c30dc02f` | 2026-10-05 | 40 | Fix faction offers, accession prose, and cascade reporting |
| `b32e85be5e` | 2026-10-05 | 126 | Repair plague entry, country callbacks, reports, and response costs |
| `a4078b8dd2` | 2026-10-05 | 158 | Clarify resource fields, bounded costs, and paid aid shipments |
| `2e4eaf7452` | 2026-10-05 | 86 | Clarify muster reports and selected claimant demand prices |
| `978c7b5d57` | 2026-10-06 | 40 | Fix Zombie outbreak lifecycle and receipt-aware refunds |
| `e99130b845` | 2026-10-06 | 44 | Repair Tensions Rising report batches and evolution lifecycle |
| `a06c4155f7` | 2026-10-06 | 188 | Repair Secret Alliance feedback, response costs and decision relevance |
| `ca3aa27717` | 2026-10-06 | 407 | Repair Utopia selection, political teardown and paid development |
| `8540b5be9f` | 2026-10-06 | 58 | Shorten famine and migration decisions and report summaries |
| `bd5e117357` | 2026-10-06 | 32 | Repair White Peace settlement safety and forced-entry feedback |
| `b6a04580d2` | 2026-10-06 | 496 | Repair Soviet Collapse reports, costs and forced-entry feedback |
| `d88a7714f7` | 2026-10-06 | 286 | Repair Fury outbreaks, army ownership and coherent paid actions |
| `250b9f1f06` | 2026-10-06 | 51 | Fix Communist Insurgency reports, interventions and Revolution setup |
| `3ad7a6b195` | 2026-10-06 | 11 | Consolidate zombie counterstrain actions and repair outbreak presentation |
| `ce0b926dc7` | 2026-10-06 | 277 | Repair Holy Realm progression, escorts, forced entry and Fallout integration |
| `12584f289c` | 2026-10-06 | 306 | Aggregate disaster reports and align recovery bills with actual commitments |
| `79a669512a` | 2026-10-06 | 104 | Repair Death launch safety, paid field work, Atlas tabs and textures |
| `f0d05ef166` | 2026-10-06 | 1193 | Remove bookkeeping language from Fallout player text |
| `9225f02da2` | 2026-10-06 | 31 | Replace CBRN bookkeeping prose and shorten occupation actions |
| `8ae1289b0b` | 2026-10-06 | 21 | Clarify independence wave reports and frontier agreements |
| `839850b0d6` | 2026-10-10 | 25 | Rework famine and migration: Hunger Lines famine, national crisis, merged decisions |
| `1d123f7111` | 2026-10-10 | 19 | Open camp and genocide paths on gameplay conditions and trim camp decisions |
| `6288ccfebe` | 2026-10-10 | 688 | Cut decision category text to a line of context and one status line |
| `3b614dbc47` | 2026-10-10 | 2 | Trim the weaponized zombie and communist insurgency category text |
| `2af246bc36` | 2026-10-10 | 124 | Polish Event 014 player text: spoiler leaks, stale numbers and mechanical wording |
| `24b10ad3fb` | 2026-10-10 | 167 | Edit the Mengele project text: distinct stage descriptions, plain requirement lines, US spelling |
| `cc4cd419ca` | 2026-10-10 | 84 | Edit Chaos Meter, tooltip and modifier text |
| `206bf76bd7` | 2026-10-10 | 63 | Edit condemnation, sanctions and CBRN diplomacy text |
| `d0fc5e0ec3` | 2026-10-10 | 80 | Edit Event Log, Triggerable Scenarios and Welcome window text |
| `7e7a6c38e1` | 2026-10-10 | 64 | Edit famine, migration and map mode text |
| `dc76124c66` | 2026-10-10 | 59 | Edit shared decision, idea and requirement text |
| `5210c2414f` | 2026-10-10 | 99 | Give Africa decision requirements readable tooltips and replace placeholder host text |
| `18276e5021` | 2026-10-10 | 58 | Edit disease containment board and biological raid text |
| `c51a19510c` | 2026-10-10 | 54 | Edit Chaos Warfare doctrine, CBRN technology and project text |
| `0dfba3dcd6` | 2026-10-10 | 190 | Edit CBRN raid, protection, occupation and command text |
| `22a63b91f1` | 2026-10-10 | 7 | Edit CBRN unit and equipment descriptions |
| `787c92839e` | 2026-10-10 | 742 | Edit fallout and Air Winter text |
| `e6d26d58c2` | 2026-10-10 | 6 | Shorten famine and migration phase lines and remove last semicolons |
| `567378bbc2` | 2026-10-10 | 60 | Finish Event 32 for release: programme-wide survey, US text, shared fixes |
| `e5f3ed5309` | 2026-10-10 | 697 | Edit Event 006 player-facing text for plain wording and US spelling |
| `983f961dcb` | 2026-10-10 | 7 | Release pass for Event 004 Random War |
| `047ca1c876` | 2026-10-11 | 69 | Edit Event 003 event option tooltips, peace letter text and memory lines |
| `0a538a5c0f` | 2026-10-11 | 98 | Edit Event 003 decision descriptions, Mandala panel text and doctrine balance tooltips |
| `8b8f1edee5` | 2026-10-11 | 14 | Release pass for Event 001 Communist Insurgency |
| `b1cf09f834` | 2026-10-11 | 91 | Edit Event 003 Bodhisattva, power and focus text |
| `dc7a3edc7a` | 2026-10-11 | 17 | Edit Event 003 requirement flag text and remaining tooltips |
| `038317338d` | 2026-10-11 | 7 | Edit Event 003 closing wording pass |
| `9b498ac529` | 2026-10-11 | 19 | Finish the Event 002 release pass for decisions, League and cure text |
| `c92596b25b` | 2026-10-11 | 2 | Copyedit White Peace report and refusal text |
| `f0de9c2e91` | 2026-10-11 | 3 | Copyedit Fury opening news and align decision indentation |
| `eb3e74fd6a` | 2026-10-11 | 128 | Plain mission descriptions and shorter capital lists in Event 005 objectives |
| `4a3fc598d4` | 2026-10-11 | 19 | Replace internal bookkeeping phrases in Event 005 requirement and aid text |
| `f2d2c91687` | 2026-10-11 | 19 | Name Armed Breakaway Momentum consistently and tighten successor birth text |
| `6eaf4c48de` | 2026-10-11 | 6 | Capitalise Chaos Tier in Event 005 requirements and tighten the release-risk note |
| `68151af999` | 2026-10-11 | 14 | Remove AI and game-mechanic wording from Event 005 effect tooltips |
| `de40e3899b` | 2026-10-11 | 25 | Polish Event 010 Death report, news, category and super-event text |
| `240d0a688f` | 2026-10-11 | 49 | Align Event 010 Death decision tooltips with what the scripts do |
| `7b8c66f67c` | 2026-10-11 | 42 | Edit Secret Alliance report text, scenario summaries, log details and mission descriptions |
| `4358e00d8c` | 2026-10-11 | 27 | Tighten Event 010 Death focus, state modifier and requirement text |
| `94bf202221` | 2026-10-11 | 1 | Fix the Recaptured Wasteland state description wording |
| `74c8d50759` | 2026-10-11 | 121 | Align Secret Alliance decision, mission and requirement text with the scripted costs and rules |
| `b38419216f` | 2026-10-11 | 90 | Copyedit Utopia Manifesto event, report and tooltip text |
| `385a2ee0cf` | 2026-10-11 | 89 | Rewrite Event 013 report, news, super-event and legacy clause text for release |
| `6000ec3c94` | 2026-10-11 | 55 | Align Event 013 decision, mission and cost tooltip text with the scripted costs |
| `842fe6c95c` | 2026-10-11 | 71 | Correct Utopia Manifesto focus requirement tooltips and descriptions |
| `e1ec26157a` | 2026-10-11 | 13 | Finish Event 013 card, category, idea and modifier text and name the two unnamed state modifiers |
| `ff2045031a` | 2026-10-11 | 69 | Copyedit Utopia Manifesto ideas, requirement flags, achievements and super-event text |
| `ebe4b96438` | 2026-10-11 | 6 | Finish Utopia Manifesto event and focus copyedit |
| `13a2551d2f` | 2026-10-11 | 1 | Tighten the First Stewardship report text |
| `52d677e0e7` | 2026-10-11 | 233 | Polish Event 015 decision, mission, window and cost text for release |
| `c9f6265057` | 2026-10-11 | 25 | Bind Event 017 decision tooltips to their tuning constants and simplify the join option text |
| `2a2333c33a` | 2026-10-11 | 9 | Polish Event 019 report and event text for release |
| `2ca680b039` | 2026-10-11 | 25 | Align Event 019 tooltip figures and requirement text with the script |
| `53f9b7aa84` | 2026-10-11 | 41 | Polish Event 020 report, evolution, super-event and native raid text |
| `ccdb438be1` | 2026-10-11 | 30 | Correct Event 020 response decision and mission tooltips |
| `e5a8228aeb` | 2026-10-11 | 67 | Polish Event 020 Rat route decisions, focus text and requirement flags |
| `dac3670245` | 2026-10-11 | 83 | Polish Event 015 survey, store and Calling decision text and tie durations to their base terms |
| `ce0cef6c1a` | 2026-10-11 | 20 | Describe Event 019 claimants by what they do instead of where they come from |
| `a35b02f679` | 2026-10-11 | 53 | Polish Event 015 property, Necessary Ground and stewardship text and correct ladder and Assigned Colony statements |
| `a8dc686b19` | 2026-10-11 | 38 | Event 018: align decision tooltips with script constants and remove bookkeeping wording |
| `92fcf200ea` | 2026-10-11 | 32 | Event 018: read focus and modifier figures from script constants, simplify idea descriptions, fix flag text |
| `7c090da95f` | 2026-10-11 | 20 | Event 018: polish event option tooltips and report text |
| `c29dc7570b` | 2026-10-11 | 54 | Polish Event 015 League, defense, correction and formation text and align requirements and deadlines with the script |
| `aea9076468` | 2026-10-11 | 9 | Remove contrast phrasing from Event 015 decision descriptions and state the auxiliary contractor requirements |
| `6c980f4729` | 2026-10-11 | 23 | Name the Choice / Assignment value the same way everywhere in Event 015 |
| `89a0ee37f8` | 2026-10-11 | 217 | Edit achievement names, descriptions and tooltips |
| `ba94f5d1b4` | 2026-10-11 | 41 | Edit super-event descriptions and fit the text boxes |
| `1453fe99cc` | 2026-10-11 | 951 | Edit Fallout government and resource scenes for all regions |
| `2dc972536e` | 2026-10-11 | 12 | Replace working labels in the event registry with plain event names |
| `5f2cb682ed` | 2026-10-11 | 50 | Edit camp administration, Camps UI and camp decision text |
| `f974b1bb1c` | 2026-10-11 | 1 | Tighten the Black Friday report: state the sale length plainly and explain the smaller saving on discounted appointments |
| `29eb8c1f9d` | 2026-10-11 | 13 | Use one spelling of program in Event 23 text and smooth the command category line |
| `024dce0dd6` | 2026-10-11 | 24 | Event 22: final text pass on option tooltips and reports |
| `e01f0bdcc1` | 2026-10-11 | 20 | Event 30: final text pass, opinion modifier names and evolution summary keys |
| `80cc98a99d` | 2026-10-11 | 15 | Event 40: final text pass, achievement names and opinion modifier names |

## Implementation commits

| System | Commit | Existing values restored | Files |
| --- | --- | ---: | ---: |
| b6 | `78e6554affd48ebcce7191ccded8c564353ac447` | 0 | 1 |
| camps | `707df10ab81269eb1eaf9dfaf5e9cd7f804fe783` | 83 | 9 |
| catalog | `3a0a56a5c5ef9b8e66945cecdb0e7e828ccc384e` | 0 | 4 |
| cbrn | `870440c437abb4eed00a6ecee00d6727bcfa967f` | 460 | 30 |
| chaos_condemnation | `a1866880500dbbc83e39bb4194179eebb812ce48` | 125 | 2 |
| event001 | `9a9181c1f3c99a045e9b294bd762dda460b09b77` | 45 | 1 |
| event002 | `f3c31c8d1c7934eee66bca6eef5788807780678f` | 20 | 1 |
| event003 | `e25b11e0304e2ce96e09b7af9aa2d36bd30a9c02` | 338 | 2 |
| event004 | `9b59ef36afb7420c6ffed15eee6b7445f47a0e34` | 6 | 1 |
| event005 | `6eb33d883b2dc50b1604eaf474ad06f52f7e73a8` | 559 | 1 |
| event006 | `22ca369adc6208bc35efa3a21650f86eddb06bc1` | 959 | 53 |
| event007 | `ddfa77393b34a44736f9403a37080cd8d02875d4` | 112 | 2 |
| event009 | `256a17709aaf29cb00d641dd3de3cc04613c37ba` | 12 | 1 |
| event010 | `a6fcb2670e4ebee35ca4b9aed879b3a170131da0` | 98 | 2 |
| event011 | `be16542f341a16d4fe3739e595f016c9f3c41b45` | 164 | 2 |
| event012 | `b81f60173b974143ab7085bc15ca5b38ee899093` | 178 | 15 |
| event013 | `c02ffce521afc9484811e9b47cd87744fb0e7c19` | 161 | 1 |
| event014 | `1f40cb2e3294a502d3a138dc0dd383e55087309e` | 206 | 2 |
| event015 | `3975313519c0bc1a7259fa5335e5db5938166cea` | 777 | 10 |
| event016 | `8114f722529d6b71b309b1dbd66f8a59064ef03d` | 425 | 37 |
| event017 | `6e1e6080f3ba40d775c48925d5c6ea3724c7124e` | 18 | 1 |
| event018 | `5ae2808830d4bc29a3d725554373db265f5627dd` | 253 | 4 |
| event019 | `bc6a099d3f09fe1e9d9db24e7aba276d10567d16` | 135 | 2 |
| event020 | `3dd404db53add92293f09a37bb002e4003ec68bb` | 193 | 10 |
| event021 | `2572ac0a6337bae0ac27d3a4b1e3ae546707178c` | 10 | 1 |
| event022 | `d259cd9f626b4f9685379cc45625d00af83e15d4` | 24 | 1 |
| event023 | `fe70593119bf021c3a3501f2430756db107824af` | 14 | 1 |
| event024 | `82a578a32393c7779f0e85efbadc809a3c73288c` | 38 | 2 |
| event025 | `79328b209cc513972d574d1c376c1dba088d6b0f` | 13 | 1 |
| event026 | `a24fc5ca77ada3404062f99c1382fddc57aff21b` | 2 | 1 |
| event028 | `5cb387e323965bf3d4430fbf9ecba74fe73980b4` | 3 | 1 |
| event029 | `032e851a6086dc907cc1358c44ce35cb269d1813` | 135 | 2 |
| event030 | `5d61c5d413ac1b17c59a1ccc297833621552562d` | 20 | 1 |
| event031 | `682a925492663f9471c93d6a2a18de076081f78d` | 43 | 1 |
| event032 | `2a6223d4be29005d00ae8a189190ea408b89345d` | 96 | 4 |
| event033 | `e0b1a08946de1a69868fdbd073b8c9a7b6c852eb` | 20 | 2 |
| event034 | `a27afb609fd77de536c37397255b6482a5bf1b87` | 3 | 1 |
| event035 | `7cfdaec912d3dbabe4806d0b2eb683d5d4373710` | 13 | 1 |
| event036 | `7c9382190c8dedc3fc6c00352fd626e797f2398c` | 2 | 1 |
| event037 | `b3dfe57de5b9ba9df3a8a04f057cfd2dd0f7467a` | 1 | 1 |
| event039 | `a8903d7b8a15e70eccb1266d74b9bea0605ea5c0` | 57 | 2 |
| event040 | `3ae0eebc2fc6866cdf52e6b73ea2e02d040265d6` | 14 | 4 |
| event042 | `10b3e2638dd0b27870407902b295118169cf6a57` | 2 | 1 |
| event066 | `0d140d27fcf7cd35f5fade167815adc8efa3e83c` | 1 | 1 |
| fallout | `8904ea2f02e36b76b524adbead8ea9fa478d9c19` | 2901 | 2 |
| famine_migration | `76156787c6764bd959d9ebb6156b695691c4acbc` | 97 | 4 |
| interface | `440fe01242ca41c7a65c30a29f1fc4540e44014b` | 128 | 3 |
| shared | `0331ae2fefbadf6eb4848be3e3eafb4af7d95d26` | 242 | 9 |
| super | `c0fd59ec9b41600bd05e7911800dfeaf0383d46d` | 10 | 7 |
| orders | `5b93d3d47baafa2c8b1ecdb115820e8efade1147` | 3 | 1 |
| audit_fixes | `442c8a9e1d09271dd0f5c8919010c502d1364911` | 13 | 10 |
| ledger_formats | `8f676ea5258b0fff06b66f14288556db500235e6` | 1 | 1 |

## Meaningful verification

All 9,218 accepted existing values match both HEAD and the working tree after the final source comparison.
Independent localisation review found and closed the generated Saar threshold substitution, eleven inserted colour openings, a missing Holy Realm getter, the Acid Rain percentage/basis-point mismatch and retired projections, and a concurrent working-tree reversion of 177 Event 016 project values.
The Acid Rain projection lines and Holy Realm getter were restored exactly from their historical parents. The current percentage projection remains active.
Current report-colour audit findings are two Event 038 entries outside this task. It found no owned report-colour issue.
The catalog changed 52 cells with only four worksheet XML payloads changed, preserving the ZIP member set, unrelated values/types/styles, and all workbook status values.
All three generated CSV exports parse and match ordered workbook rows and columns.
No event option count, gameplay outcome, AI selection weight, art path, sprite, or audio routing was changed by this text work.

## Preserved scope and limitations

No unapproved simplifications, invented prose, or weaker substitutes were used.
The following preserved values implement the owner’s exceptions and shared-path ownership, rather than undisclosed simplifications:
- 14 keys: Preserve dynamic dispatch to value localisation. Value keys are retained as additions.
- 3 keys: Concurrent A12 restore owns the use-policy wording and functional delivery terms.
- 1 key: Cloning manpower modifier was replaced by equipment-lot production. Preserve genuinely new mechanic content.
- 1 key: A8 owns the shared row layout. Preserve the concurrent restored ordering.
- 15 keys: Welcome wording already restored by b9258e251e. Preserve its live baseline-count bindings.
- 6 keys: Concurrent A12 original direct containment flow and payments preserved.
- 1 key: Keep new named-outbreak report consumer. Site identity is genuinely new report data.
- Retired and repurposed keys were not resurrected, including the concurrently removed Last Fury Standing description owned by D5.
- Five original Holy Realm chance-output keys were restored because the restored active description requires them.
- The historical Holy Realm “about 1%” label remains an approximation: unchanged option weights give a raw 3.8835% share in an intermediate case and 7.4766% in the strongest case. The owner’s exact-wording instruction takes precedence over a new label or balance change. Source calculations are not observed game behavior.
- The root reference-read connection closed after initial successful wiki/game-document reads. Source lookup returned no definition for the scripted-localisation selector, so exact local source review supplied that evidence. No retry or tooling repair was used for the closed route. The probability auditor’s separate route returned partial scenarios because FROM was unresolved. Its scenario shares were calculated from actual source.
- No live game validation or render is claimed. HOI4 was not launched. Nothing was pushed.

## Reference evidence

| Source | Relevant lines | SHA-256 revision |
| --- | --- | --- |
| paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md | 59–72, 185–214, 706–728 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md | 432–451 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md | 161–170 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_objects_documentation.md | 169–337 | `a5d06da0b42e615fa0c40d0103d9125ed68a7691778e20c0315aca7c82822c81` |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md | 2681–2698, 7820–7841, 7888–7909, 8187–8204 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/WTT_china_political_struggle_localisation.txt | 1–50 | `cd7234a70956224c533e62a376644842bdee68bb9a17a5db0667b6711d8ea434` |

## Skills

Used `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-scripted-gui`, `chaos-redux-super-events`, `chaos-redux-shared-git-commit`, and `chaos-redux-xlsx`. The probability auditor used `chaos-redux-ai-strategies`.
No skills were created or changed.
