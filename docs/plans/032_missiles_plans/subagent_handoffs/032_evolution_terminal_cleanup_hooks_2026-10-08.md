# Event 032 terminal evolution-clock cleanup subscriptions

Date: 2026-10-08.
Disposition: `implemented` for all 15 proven runtime subscriptions after parent recovery, with native execution still unverified.
Acceptance basis: the parent's explicit bounded patch assignment to subscribe only Event 032 clock cancellation at existing canonical `world_end` commits.
No Event 032 terminal branch or shared terminal setter was introduced.

Inventory scope was current engine source under `common/` and `events/`, using exact canonical scalar, quoted, multiline, and block-form `set_global_flag` matching.
Predicates, `world_end_*` flags, identifiers, comments, docs, and snapshots were excluded from commit classification.
The 15 matches in 13 TXT files were each confirmed through local surrounding source and `hoi4.source_lookup` owner/block chains.
No additional match was found in the non-TXT engine-source candidates.
No inline or meta-generated canonical boundary was found, and no ambiguity required a source skip.

Every installed call is `missiles_cancel_all_evolution_clocks = yes`, immediately after the existing `acid_rain_interrupt_for_world_end = yes` callback and inside the original guard and scope.
The supplied helper at `common/scripted_effects/032_missiles_evolution_effects.txt:88-117` was read in full.
Its 18 flag clears and 10 variable clears affect only Event 032 evolution clock receipts and dates.
It does not set or clear `world_end`, change terminal-owner state, clear recorded evolution/history, change payloads, or schedule work.
This invalidates queued clock work through its flags and receipts and does not claim to remove already queued engine events.

| Runtime file | Exact owner | Canonical write line at verification | Added call or blocked insertion |
| --- | --- | --- | --- |
| `events/002_zombie_outbreak.txt` | `chaosx.nr2.8` | 894 | Added at 896 |
| `events/002_zombie_outbreak.txt` | `chaosx.nr2.11` | 945 | Added at 947 |
| `common/scripted_effects/010_death_effects.txt` | `death_try_start_world_end` | 3665 | Added at 3667 |
| `common/scripted_effects/007_fury_effects.txt` | `fury_start_world_end` | 1638 | Added at 1640 |
| `common/scripted_effects/012_africa_world_order_effects.txt` | `africa_form_terminal_world_identity` | 4035 | Added at 4037 |
| `common/scripted_effects/014_cannibalism_effects.txt` | `cannibalism_try_start_ordinary_world_end` | 12637 | Blocked, insert after acid-rain call at 12638 |
| `common/scripted_effects/014_cannibalism_effects.txt` | `cannibalism_complete_wendigo_terminal_lock` | 21608 | Blocked, insert after acid-rain call at 21609 |
| `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` | `brilliant_scientist_execute_lab_world_terminal` | 738 | Added at 740 |
| `common/scripted_effects/018_resources_found_cave_effects.txt` | `resources_found_cave_begin_world_end` | 2250 | Added at 2252 |
| `common/scripted_effects/020_black_plague_evolution_effects.txt` | `black_plague_evolution_v_perform_terminal_takeover` | 884 | Added at 886 |
| `common/scripted_effects/031_random_terror_effects.txt` | `random_terror_finalize_false_revelation` | 7261 | Blocked, insert after acid-rain call at 7262 |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` | `murder_mystery_activate_world_end` | 2173 | Blocked, insert after acid-rain call at 2174 |
| `common/scripted_effects/chaosx_settings_effects.txt` | `toggle_world_end` | 3480 | Added at 3482 |
| `common/scripted_effects/germany_mengele_effects.txt` | `mengele_clone_world_order_launch` | 1561 | Added at 1563 |
| `common/scripted_effects/fallout_consolidated_effects.txt` | `fallout_lock_transition` | 41347 | Added at 41349 |

Source scopes: `chaosx.nr2.8` uses COUNTRY `immediate/hidden_effect`, and `chaosx.nr2.11` uses COUNTRY `immediate/hidden_effect/if`.
The remaining sites retain their scripted-effect caller scope and enclosing `if` blocks, except `fury_start_world_end`, which commits at the helper body level.
The settings site is the `else/if` branch in `toggle_world_end` that restores an already-backed-up terminal flag, and it retains the existing backup gate and cleanup callbacks.
Adding the AnyScope cancellation call requires no ROOT/FROM rebinding or new event target.

Event 23 produced no canonical writer in this inventory and no Event 23 file was edited.
The Fallout subscription is at Event 76's existing `fallout_lock_transition` after its snapshot/admission guard and terminal write.
No Fallout admission logic, Event 23 consequence logic, owner outcomes, AI, history, assets, or subsequent branch ordering was edited.

Three in-place writes failed with exit code 1 and `Failed to write file` for their exact paths.
The affected files remain byte-for-byte equal to their captured pre-edit states.
Following the parent instruction, no file was removed or replaced and no filesystem permissions were changed.
These are four unimplemented call sites, not ambiguous design boundaries.
Apply only these exact hunks through the parent's guarded recovery route, using fresh content and preserving all other edits:

```diff
*** Begin Patch
*** Update File: C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/014_cannibalism_effects.txt
@@ cannibalism_try_start_ordinary_world_end = {
 		set_global_flag = world_end
 		acid_rain_interrupt_for_world_end = yes
+		missiles_cancel_all_evolution_clocks = yes
@@ cannibalism_complete_wendigo_terminal_lock = {
 		set_global_flag = world_end
 		acid_rain_interrupt_for_world_end = yes
+		missiles_cancel_all_evolution_clocks = yes
*** End Patch
*** Begin Patch
*** Update File: C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/031_random_terror_effects.txt
@@ random_terror_finalize_false_revelation = {
 		set_global_flag = world_end
 		acid_rain_interrupt_for_world_end = yes
+		missiles_cancel_all_evolution_clocks = yes
*** End Patch
*** Begin Patch
*** Update File: C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/039_murder_mystery_integration_effects.txt
@@ murder_mystery_activate_world_end = {
 			set_global_flag = world_end
 			acid_rain_interrupt_for_world_end = yes
+			missiles_cancel_all_evolution_clocks = yes
*** End Patch
```

Current-diff and preservation evidence:

- Staged and unstaged diffs for all 13 owners were read before patching. No staged changes appeared in this owner set.
- Existing unstaged changes were present in `014_cannibalism_effects.txt`, `031_random_terror_effects.txt`, `039_murder_mystery_integration_effects.txt`, and `chaosx_settings_effects.txt` and were preserved.
- Exactly 11 added call lines changed ten runtime files. Removing only these lines in memory reproduced the original raw SHA-256 of every inspected file, without line-ending normalization. Failed files matched their original raw hashes unchanged.
- The post-edit canonical-write inventory still contains 15 writes. Eleven have one adjacent cancellation call and the four blocked sites have none. No duplicate subscription or additional terminal write was introduced.

| Runtime file | Pre-edit raw SHA-256 | Post-edit raw SHA-256 |
| --- | --- | --- |
| `events/002_zombie_outbreak.txt` | `1c5c9fb5f98c910d7d49fff71131626c0e27fb2d3317c88615702b6b11fedad4` | `6d058c570372bf05a6584c9eb8f4dfdfe31e0e7b64194f551f369b9cbc5be40d` |
| `common/scripted_effects/010_death_effects.txt` | `790eb2e633d35e384a1831e12f362e37ce26200446e74432bd6572bcc0fe024e` | `285ac11992d6b569c4c90ac5cf6b520fdd80ab4096a05afcad3ec4ad14d380d6` |
| `common/scripted_effects/007_fury_effects.txt` | `7fa51bdf9338a6d21e0ff0c2f7cab583cf1883e12798545049085b5c735ff86d` | `eaad4f8533408c6f905ad22f3c3e73093fe50378b0595111ecab5a66ff617151` |
| `common/scripted_effects/012_africa_world_order_effects.txt` | `677e4614fbec22203c07110ff3205cae2e02df4b3bee8bb77265f44c148f9b6d` | `8dee50b14435ae3b26272eef0c13819bcb37a3c91f8fe84e7e03f745d2c95dee` |
| `common/scripted_effects/014_cannibalism_effects.txt` | `5b59a1e84651ec44f712f5ef60ada011ba0ac979ffdc143ee199f57550430827` | `5b59a1e84651ec44f712f5ef60ada011ba0ac979ffdc143ee199f57550430827` |
| `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` | `03e4fdd84428ad14635fa4931fab5da3b9497f90e4df51cdd45e663269394ac3` | `f0fb4ac2d2caa454a91e8b2a4806176386b05edede1a7d35cc70d231b9a71037` |
| `common/scripted_effects/018_resources_found_cave_effects.txt` | `5957300fa0a0a0a62addad640443c3511c22ba0fe89dda8624127881bfde3ef9` | `9b1f81ea88bc36a4edf153df76fc71925bc8c0113af7a936abff1ffd528331f5` |
| `common/scripted_effects/020_black_plague_evolution_effects.txt` | `f6aa7de6d310d8d6e8fde8afb9f45cb983aeffd7a0ec75606c5873d0741832bb` | `60f16cda0a893342e5882278e1e9424fe2c0ea909faa472f6a4b9f8262b68381` |
| `common/scripted_effects/031_random_terror_effects.txt` | `187abfbc691562a8aa86e57043a76cae986e238753382112c3c344f4cc29e73e` | `187abfbc691562a8aa86e57043a76cae986e238753382112c3c344f4cc29e73e` |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` | `134ddf291a00c4eaa7f5cf39e2fc2d1979abb4182730b3fec6387d22905aa724` | `134ddf291a00c4eaa7f5cf39e2fc2d1979abb4182730b3fec6387d22905aa724` |
| `common/scripted_effects/chaosx_settings_effects.txt` | `ee23baff71d0249c5f87edb3e3d79327f5acb4d9f6d41cd2feb9766b7ab84580` | `67ebade9ce82080d669a99d548938873c58bbf5e18836704b43d124d12069858` |
| `common/scripted_effects/germany_mengele_effects.txt` | `3dd326a79dd57d4f5ae53049c6df72746a9975c8e162044849f41aeef5c6472b` | `954868b29b73f60c14a815f79938d2913e144a5e3edc1567be28d16eac19332f` |
| `common/scripted_effects/fallout_consolidated_effects.txt` | `d244054324be5f8860afda69461ab014af7cad294ef58698990ca5a74d8b7de2` | `7bc8da7dcc620f3239f2a58750ce4a1761b7d9f24800e322728a68f728f5b70e` |

Reference and MCP evidence:

- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:102-126`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, documents global flag access and clearing in any effect scope.
- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:2773-2782,2801-2809,7085-7093`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, documents AnyScope `clear_variable`, `clr_global_flag`, and `set_global_flag`. These sections were read through `hoi4.reference_read` after reference context/search.
- Installed vanilla `common/on_actions/00_on_actions.txt:384-399` was inspected as a native global-flag effect-block precedent. The existing acid-rain, Africa, and faction cleanup calls supplied the exact repository subscription pattern.
- Every owner had a successful source-location lookup. Event-file lookup revision: `79a28526ecf259f67d13bbd7b69a90887eae2fa0cee937242d3b8df226d371b7`. Scripted-owner lookup revision: `b06a1f1d7686ad8dd5705ee9c3fbd6609bf952047c215c86d00035c2fcc94fd6`. All matched nodes were executable flag assignments, with no shadowed owner or truncated block chain.
- The supplied cancellation helper resolved at source revision `2b7e25b56df76abb08f208cf98e8570004eb14734da0ed6be7afec85bed98327`.
- The helper's actual body was checked through `hoi4.script_validate` in explicit COUNTRY and STATE scopes. Splitting its 28 commands into two bounded reads per scope exposed every finding. Each returned `SCRIPT_CHECKED`, `valid = true`, 14 checked commands, zero unresolved commands, zero unchecked argument blocks, and zero omitted findings. Coverage is syntax, native command kind, and declared scope, with `parametersChecked = false`. This is not runtime proof. Documentation revision: `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
- Initial validation requests exceeded the live limit of 32 and were rejected. The corrected full-body results omitted seven findings, so the bounded split checks above replaced them as complete finding coverage.
- Bounded event traces for `.8` and `.11` returned focused `EVENT_INSPECTED_PARTIAL`, revision `e59ab758e239e5ea62d20e5c085f4aa12ec8c39fae3ec9dac0d5ddca379ebd2d`, with zero helper projections. They do not establish complete helper lifecycle coverage.
- `chaosx.nr2.8` artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f9f402f14adf180b1af93d41d535a7b69d046ea0fd93473a7b7ff5297405500/5afb42dc6003044bb88bb271106ad2b2454fa1e429351c5fd1fc9e261a7b4c3c/event-trace-e59ab758e239.json`.
- `chaosx.nr2.11` artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/226f3049d26821ce395f1ad905a0f14da79300abf007911fa29c596e978584b2/4d6ec86e03b1a76112eb13b8767521730da5913c884779ee4f5e895df0fff6e6/event-trace-e59ab758e239.json`.

Meaningful validation skipped: live engine execution, terminal-outcome playthroughs, queued-event runtime behavior, full event render/compare, and the parent's aggregate probability comparison.
This patch changes no timing formulas, weights, or parent helper bodies.
Runtime and final integrated clock acceptance remain with the parent and user, and full integration remains blocked until the four supplied hunks are applied.

No gameplay simplification, generic terminal setter, periodic observer, fallback branch, new constants, or new helper definition was introduced.

Parent recovery: the four exact supplied hunks were applied to the three previously blocked files using guarded `apply_patch` replacement through an explicitly named task-temporary file.
Each current file was copied and hash-checked before replacement, and all non-hunk content, including concurrent owners' changes, was preserved.
The source-write failure is resolved; the earlier 11/15 table and hashes above record the worker checkpoint, not the final integration count.
All 15 canonical terminal writers now invoke the same Event 032 clock-only cleanup adjacent to their existing subscriptions.
Only the ten successful runtime files and this handoff were written.
No Git writes, game launch, log access, subagents, permission changes, or coarse file replacement were performed.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`; no skill files were changed.
