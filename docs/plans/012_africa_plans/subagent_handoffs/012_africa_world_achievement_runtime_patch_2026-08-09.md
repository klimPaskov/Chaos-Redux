# Event 012 world-achievement runtime owner patch

Date: 2026-08-09.

Scope: rows 41-44 of `012_africa_achievement_matrix.csv`, plus the requested priority-member colonial-puppet witness in the existing Event 012 puppet callbacks.

No commit was created because the parent agent requested a shared-workspace patch without a commit.

## Files changed

- `common/scripted_effects/012_africa_world_order_effects.txt` records sponsored movement collapse at the installed package actor-loss witness used by capitulation and annexation paths.
- `common/scripted_effects/012_africa_world_sponsorship_effects.txt` records sponsorship betrayal for an installed obligation default and for the explicit ideological-congress capture outcome.
- `common/on_actions/012_africa_world_order_on_actions.txt` records sponsored package puppeting and priority-member colonial puppeting in `on_puppet`, `on_release_as_puppet`, and `on_subject_autonomy_level_change`.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_world_achievement_runtime_patch_2026-08-09.md` records this handoff and the no-path dispositions.

The pre-existing `on_startup` provider block in `common/on_actions/012_africa_world_order_on_actions.txt` was preserved unchanged.

## Runtime owner map

The narrow scripted helpers in `012_africa_world_order_effects.txt` are:

- `africa_world_record_sponsored_movement_collapse` takes the installed actor scope, reads `africa_is_one` and `africa_world_package_sponsored`, and sets the global collapse flag with no cleanup side effects.
- `africa_world_record_sponsored_puppet_status` takes the subject callback ROOT scope, reads `africa_is_one`, `africa_world_package_sponsored`, and `is_subject`, and sets the global puppeted flag with no foreign-control inference.
- `africa_world_record_sponsorship_betrayal` takes the installed sponsorship candidate scope, reads `africa_is_one`, and sets the global betrayal flag; callers prove the active obligation or capture branch before invoking it.

The existing actor-loss, exile, breakup, sponsorship-default, sponsorship-capture, and subject callbacks remain the only call sites.

### Row 41: `africa_another_continent_stood_up`

- Sponsored collapse is written at the installed actor-loss witness and repeated at the exact exile and breakup terminal resolvers when the actor still carries `africa_world_package_sponsored` after `africa_is_one`.
- Sponsored puppeting is written by the three subject-creation/autonomy callbacks when the current subject still carries `africa_world_package_sponsored` after `africa_is_one`.
- Sponsorship betrayal is written by `africa_world_sponsorship_default_current_mode` for every installed grounded mode, including decision timeout callers, and by `africa_world_sponsorship_record_ideological_capture` for the explicit congress-capture branch.
- Offer refusal before installation remains non-betrayal because it never enters the obligation/default helpers.

### Row 42: `africa_two_continents_one_name`

The existing positive integration helper and conquest-only disqualifier remain unchanged.

No exact confidence-collapse owner exists in the installed two-continent protocol.

No `start_civil_war` or equivalent union civil-war path exists in the installed Event 012 union files.

Union strain, treaty dissolution, and contested compact-breaking war were not promoted into either disqualifier because doing so would proxy a different mechanic.

### Row 43: `africa_war_between_worlds`

The existing `on_capitulation` and `on_peaceconference_ended` owners already record continental-war victory and settlement through the achievement helpers.

No debug-surrender entry point exists in Event 012, so `africa_achievement_debug_surrender_used` remains definition-only.

No global-revolt threshold or terminal revolt outcome exists in the installed continental-war protocol, so `africa_achievement_global_revolt_threshold_reached` remains definition-only.

The generic `africa_world_union_member_revolt` and `africa_world_region_revolt` action-failure flags were not treated as the missing global threshold.

### Row 44: `africa_the_world_is_one`

`africa_form_terminal_world_identity` already calls both `africa_achievement_record_africa_world_formation` and `africa_achievement_record_world_terminal_super_event` on the exact terminal commit path.

Other world-end implementations already call `africa_achievement_record_other_world_end`, and the world-order docket close already calls `africa_achievement_record_unresolved_continent_identity`.

The earlier shared triggerable-scenario selector note referred to an unregistered Event 012 placeholder entry. That route has since been retired from the shared selector and launch dispatch; the Event 012 source specification therefore remains authoritative, and the former forced-scenario helper and negative checks are absent.

## Constants, event targets, and cleanup

No constants or tuning values were added because the patch only writes existing achievement flags at exact lifecycle witnesses.

No new event targets were introduced.

Existing sponsorship cleanup remains responsible for removing live obligation decisions and target-array membership after default, fulfilment, actor loss, or terminal closure.

The new collapse and betrayal writes occur before the existing cleanup effects clear live sponsorship state.

## Validation and evidence

- `rg` confirmed three collapse writers (loss, exile, breakup), two betrayal writers, three sponsored-puppet writers, and three priority-member colonial-puppet writers in the intended owner files.
- `rg` confirmed that confidence-collapse, union-civil-war, debug-surrender, global-revolt-threshold, and forced-scenario flags still have no writers outside their definitions/core trigger references.
- Read-only `hoi4.event_inspect` scan of `chaosx.nr12.1` completed with artifact `event-scan-550da12aba6a` in workspace `mod_chaos_redux_ea3b2d67c2c0`.
- Read-only `hoi4.event_inspect` trace of `africa_world_package.31` completed with artifact `event-trace-fa5988c7ac2c` in the same workspace.
- Read-only `hoi4.event_inspect` trace of `africa_world_package.734` completed with artifact `event-trace-7d299e83e01a` in the same workspace.
- The MCP reports are workspace-wide partial analyses with unresolved diagnostics retained in the linked artifacts; no source write was performed through MCP.

Live Hearts of Iron IV execution was not run, per repository policy.

## Parent integration notes

The parent agent should retain these additions while layering its separate `on_war_relation_added`, `on_state_control_changed`, and live regional-proof hooks into the same on-actions file.

No core achievement, ledger, high-chaos, focus, matrix, or workbook files were edited.

## Follow-up W4 runtime repair (2026-08-10)

The shared working tree received a bounded follow-up patch with no commit. This section supersedes the earlier W4 notes where they describe the pre-repair source, especially the statements that two-continent confidence collapse, union civil-war, or global-revolt threshold writers were absent.

### Files changed

- `events/012_africa_world_package_union_war.txt` gates `africa_world_package.709.b` behind `africa_world_union_strain_deferral_used` and makes `africa_world_package.731.a` scope `event_target:africa_world_continental_war_protocol_defender` before calling `africa_world_continental_war_protocol_accept_constitutional_settlement`.
- `common/scripted_effects/012_africa_world_union_war_effects.txt` records the paired one-deferral flag, clears it on renegotiation and union pair cleanup, and sets a timed post-clear reopen lock using a constant-to-temporary-variable duration.
- `common/scripted_triggers/012_africa_world_union_war_triggers.txt` gates `africa_world_union_protocol_is_openable` on the reopen lock.
- `common/script_constants/012_africa_world_order_constants.txt` adds `africa_world_union_protocol.tuning.reopen_lock_days = 2`, longer than the one-day confidence pulse.
- `localisation/english/012_africa_world_union_war_l_english.yml` describes `.731` as a constitutional settlement or renewed hostilities; the UTF-8 BOM was preserved.

### Runtime semantics

`.731.a` now resolves prewar defender counterterms through the defender scope, preserving the helper's settlement flags, event log roles, and existing cleanup path. `.731.b` remains attacker-scoped and starts the actual war.

The strain deferral flag is set on both union actors when `.709.b` is chosen, survives the delayed `.718` pulse and its immediate `.709` review, and blocks another deferral until renegotiation or union dissolution/cleanup clears it. The helper itself repeats the guard so direct callsites cannot bypass the episode limit.

`africa_world_union_protocol_clear_pair` clears the union open flag before setting `africa_world_union_protocol_reopen_locked` for two days through `set_temp_variable` and `set_global_flag { days = ... }`. `africa_world_union_protocol_is_openable` rejects new unions while that lock is active, preventing stale delayed `.760` pulses from attaching to a newly reopened pair.

### Post-patch MCP evidence

- `hoi4.event_inspect` lint for `.709` completed with focused diagnostics at zero blocking findings: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3bcd64a4cf5492fcdf2ed78cc658cc669d5d027eca111387cca573d7d7b41d2/009b085e2fe743fe209c70c9a214ee387be8d337e5d1de09fccb1cb57607b79d/event-lint-827e73d023d7.json`.
- `hoi4.event_inspect` state-flow artifacts for `.709` and `.731` are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1219af295ee97f3c750d7ec7b4a91f0383dc14d7c5eec93ae646898b9fa83d6c/e0035ba708e970b195039dd247ec3a1ba2a186605108ffa619e9e32fe079948d/event-state_flow-b154a6c24147.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7664195f26437e2cf2baae2754cdc034420629ad4c701139922b47b14dd4f5df/2c52b4ba90e772635be5efc4162396983aaedcde66f26283400b2e34f96eed22/event-state_flow-b154a6c24147.json`.
- Focused options rendering for `.731` returned zero blocking diagnostics with selected nodes for both options: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88563f19f9097658bb3c6765091d80b58d752c0fbc696209782b9b72994c3ebf/8dcd6114127a89e5fa3707ab303b703c2b3e436cf9154555a684eeea40ef5c53/event-options-b154a6c24147-manifest.json`.
- Focused timing rendering for `.760` returned zero blocking diagnostics and retained the one-day pulse timing: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f31c360ce3d91064e5e4143d61c11e7c0292193d9920ee23b871305c94a09a6a/29817c173166ae75e2e8d2d0fc05de6c36e00935276b94de6a85c8b6c6ab8e9b/event-timing-b154a6c24147-manifest.json`.
- `hoi4.probability_inspect` first inspected the event-option adapter with no source diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28e8ed029b16099ffafb73942cc9d0df2357c675ae71c860c20079c8d7cfc840/661b66c4f272aa7bdc1084091fdf24894d8c6ddc3dc67dcaf24c38fcb350d13a/probability-inspect-6c8aade2aa9e.json`.
- The matching event-option compare was partial because the bounded six-option pool was not proven complete; no normalized probabilities were claimed: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/437388279f1f900a5d4c2f1b6a91760bfe89508495ab95419d4265ade306716d/6a815f1b8af4b2547f3e1742ee1ed764dab1588d43146692fbcc2174a22562b5/probability-e56c0d9211d64e7bcb7eb80f.json`.

The MCP event reports are workspace-wide analyses with linked evidence and retained unresolved inventory; the focused render surfaces reported zero blocking diagnostics. No Hearts of Iron IV process was launched and no commit was created.
