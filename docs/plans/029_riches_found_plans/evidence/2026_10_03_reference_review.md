# Event 029 reference and source review

Disposition: implemented evidence record with unresolved gameplay acceptance.
The acceptance basis is the user's explicit instruction to implement the complete Event 029 specification package.
This record does not establish package completion.

## Connected reference evidence

`hoi4.reference_context` for the decision surface returned `OK` for workspace `mod_chaos_redux_ea3b2d67c2c0`.
The four-source context omitted Triggers, Scopes, and Localisation.
A ten-source follow-up timed out awaiting `tools/call` after 600 seconds.
The exact-token `has_manpower` search also timed out after 600 seconds.
The `has_equipment` and `on_state_control_changed` searches remain pending until their final tool results are read.
The missing detailed coverage is being read directly from local installed documentation, with MCP retrieval failures retained as route gaps.

| Reference read | Path | Lines | Revision | Rule used |
| --- | --- | --- | --- | --- |
| Country Decisions | Installed game `common/decisions/_documentation.md` | 1-46 | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` | `available` and `visible` refresh every frame, targeted scopes use acting country and `FROM`, daily target filtering narrows state candidates. |
| Decision cost | Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | 284-336 | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` | Custom costs require explicit debit in `complete_effect`, and political-power hints require a constant amount. |
| State targeted decisions | Same offline page | 576-595 | Same revision | `state_target = any_controlled_state` narrows candidates, and `FROM` is the target state. |

The exact-token `ai_hint_pp_cost` and `state_target` searches returned those cited wiki sections.
The underlying installed trigger documentation was also consulted for `command_power`, `has_equipment`, and `has_manpower`.
It documents `command_power` in country scope and equipment and manpower availability checks in country scope.
The current Event 029 source already uses `command_power` and static file-local political-power hint aliases.
These existing repairs were preserved.

## Structural source evidence

A source nesting walk over the current decision file found 92 decision definitions and nine mission definitions inside `riches_found_mine_management`.
Every `ai_will_do` block is a child of its decision or mission.
This establishes source placement and does not establish mission runtime behavior or native category presentation.

The CXT daily hook calls `chaosx_test_country_sync_registered_content`, whose current implementation only marks pending work.
The package fixture is applied by initial CXT setup or the player-triggered registered-systems action.
The fixture creates one capital-state mine without paying the discovery grant.

## Immutable comparison inputs

Snapshots were copied before this audit's gameplay patches and must remain unchanged.

| Snapshot under `2026_10_03_before/` | SHA-256 |
| --- | --- |
| `events__029_riches_found.txt` | `618f87c3bf88f6791ad6785ed73faf1c4d6d49332bee47b3b078c476cb8604e4` |
| `common__decisions__029_riches_found_decisions.txt` | `1a485534b48a59d780a53c09642e4618659c69f8fcedda9f735cca412f886a14` |
| `common__scripted_effects__029_riches_found_effects.txt` | `a991dde1db89165ced86dbf714228975113d012163d073723c898873941e987c` |
| `common__scripted_effects__029_riches_found_incident_effects.txt` | `01648014f105c149509f789be9ae3d30e013545921203ba867cbbd16d5c2f9fc` |
| `common__mtth__029_riches_found_mtth.txt` | `32c989917b468b76c5a6a98a4190b0d490c38651f1be429eadd667b2927acb5f` |
| `common__script_constants__029_riches_found_constants.txt` | `499394210e8818a5d1f94c6153e27dc7d8c69f378dc871891622806975a610f0` |

## Unresolved evidence

The current probability inspection returned `PROBABILITY_SOURCE_DISCOVERED` with source hash `0f70e76d1dd0c1b13cab670173a89b9eaa1d9500f2380a810c1a48b015953fd7` and revision `bfda944ca879c510d241794903dee459d92f35fb74b7dc350b5c188bf3c35301`.
Its adapter inventory classifies 101 timed entries as `mission_ai_will_do` and one entry as `decision_ai_will_do`.
That classification differs from the source's 92 decisions and nine missions and must be retained as an analysis limitation.
The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b51bd817d8acbc390eb28f44251b69119dbaa57d704227b72e978cb4ec664c9e/153aa92c6aab913062324f97deb29b1f408a15f0e64937a00db73dc86dbcc3aa/probability-inspect-0f70e76d1dd0.json`.
Named scenario evaluation, threshold sweeps, and same-scenario comparisons remain pending.
Required localisation, decision, completion, and probability auditors were dispatched with `fork_context=false`.
