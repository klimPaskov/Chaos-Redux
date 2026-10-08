# Event 032 finite evolution observation hooks

Date: 2026-10-08.
Disposition: `implemented` for the assigned call sites, with parent integration pending.
Acceptance basis: the parent explicitly accepted part 4 finite-pulse semantics and authorized this bounded two-file patch using its AnyScope notification and threshold-band helpers.
This implements finite observations and makes no continuous-freshness claim.

Changed files:

- `common/on_actions/032_missiles_on_actions.txt`: nine guarded calls to `missiles_notify_evolution_change` after the existing callback work, plus notification ownership comments and the documented uncapitulation callback.
- `common/scripted_effects/chaos_meter_effects.txt:4555`: one call to `missiles_note_chaos_threshold_change` at the end of `update_chaos_meter_tier`, after every tier assignment branch.
- This handoff, which did not exist before creation.

Both source files had empty staged and unstaged diffs before this work.
The reviewed resulting diffs contain only the owned notification additions and comments.
All engine-facing edits used `apply_patch`, and both in-place writes succeeded.
No parent helpers, triggers, constants, events, meter arithmetic, existing hooks, world-end logic, localisation, assets, filesystem permissions, Git state, game, or logs were changed.
Read-only Git diff commands were used as requested, with no Git mutations.
No other agents were spawned.

| Callback | Notification line | Scope and relevance gate |
| --- | --- | --- |
| `on_war_relation_added` | 136 | Existing living-participant guard remains. Either attacking ROOT or defending FROM has an initialized program. Notify after both phase updates. |
| `on_capitulation` | 155 | ROOT is the capitulated country and FROM is the winner. Either initialized program qualifies, including a missile loser with an ordinary winner. Existing achievement mutation precedes notification. |
| `on_uncapitulation` | 165 | New bounded callback. Only the documented ROOT is read, requiring existence and an initialized program. |
| `on_peaceconference_ended` | 183 | ROOT winner or FROM loser has an initialized program. Runs after the existing achievement mutation. |
| `on_peace` | 202 | Existing ROOT program gate, after target cleanup and phase update. No assumed FROM scope. |
| `on_state_control_changed` | 230 | ROOT new controller or FROM old controller has an initialized program. Notification follows the existing registered-site handler. It also observes ordinary land-control changes relevant to program viability. No additional state/world iteration was added. |
| `on_release_as_free` | 245 | ROOT released country or FROM releaser has an initialized program, checked after site reconciliation. |
| `on_release_as_puppet` | 260 | ROOT released country or FROM overlord has an initialized program, checked after site reconciliation. |
| `on_annex` | 281 | ROOT winner initialized, FROM annexed initialized, or FROM has `missiles_program_cleanup_complete`. The cleanup marker preserves relevance after the existing removal helper clears `missiles_program_initialized`. Notification follows cleanup. |

The meter call is unconditional within the completed tier-update method so the parent's stored-band comparison can observe 899-to-900 and downward crossings within a tier.
The helper, rather than this caller, owns threshold filtering and recount suppression.
The callbacks do not schedule jobs directly, and the parent helper owns coalescing and the one-hour `.192` receiver.
No new constants, cleanup state, event targets, or helper definitions were added.
Helper API documentation remains with the parent-owned definitions.

Scope evidence read before editing:

- Offline `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md:216,250,253-257,262-263,450,490`, read through `hoi4.reference_search` and `hoi4.reference_read`, revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`.
- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\on_actions\_documentation.md:20-49,68-74`, including the explicit winner/loser peace-conference contract and listed optional callbacks, revision `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4`.
- Installed `common\on_actions\00_on_actions.txt:931-944,1165-1176,1578-1582,1615-1630,4911-4945,5019-5036,5075-5105` supplies native scope comments and examples. SHA-256: `52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9`.
- Installed `common\on_actions\07_nsb_on_actions.txt:1268-1279` explicitly uses THIS for peace. SHA-256: `939ea1c0cc25c2ce4390d7dda4a8ac84547978931fae36c09d0fab7d7ec79966`.
- Installed `common\on_actions\01_tfv_on_actions.txt:482-503` gives ROOT released/FROM releaser. SHA-256: `a4db7dbc649206a0797b7f99549a16bc41fd9206ed261338a13dcebaF84a4cd3`.
- `hoi4.source_lookup` by native path and line 5076 located `on_actions/on_state_control_changed`, revision `2655f977f32be120bf978e2d916fb36e12ed190c1b594f5dd1f62e8a4e52cfad`. Symbol-only lookup returned zero definitions for the callback and was not treated as missing native support.

Ignored or unproven routes:

- `on_wargoal_expire` was not added. It is listed in installed documentation and vanilla `00_on_actions.txt:378-382` dispatches `war_justification.301` through `random_events`. The wiki identifies FROM as owner, but the inspected installed example and receiver `events/WarJustification.txt:822-848` do not independently establish that binding for a direct `effect` block. This optional route remains unresolved instead of receiving an assumed ROOT/FROM contract.
- `on_justifying_wargoal_pulse` was excluded because the wiki documents daily checking and the parent forbids this periodic route.
- No general stability, research, or production callback was invented. No extra war-goal-generation, faction, subject, or duplicate civil-war callback was added to this bounded assignment.
- Existing planned-inheritance and civil-war exclusions inside the site handler were preserved. The observer helper receives the callback-edge notification and owns deferred evaluation, while the finalizers remain parent-owned.

Validation and integration limits:

- Source review checked that a losing program can notify on capitulation, a cleaned annexed program retains relevance, release notifications follow reconciliation, and unrelated ROOT/FROM participants fail the new guards. These are source-level checks, not executed game scenarios.
- `hoi4.script_validate` on the actual on-actions file returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, 158 checked commands, 31 unchecked argument blocks, and nine roots with unknown inferred scope. No findings were reported, which does not establish complete validation.
- An additional explicit COUNTRY-scope check of the four added guard shapes and threshold call, with FROM bound as COUNTRY and ROOT supplied by the scope, supported all 14 native commands. It returned five unresolved project-helper invocations and no unchecked argument blocks. The installed documentation revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`. A first request incorrectly bound reserved ROOT and was rejected, then corrected without changing source.
- The parent-owned `missiles_notify_evolution_change` definition was read in `common/scripted_effects/032_missiles_evolution_effects.txt:15`, including its coalesced receiver path. `missiles_note_chaos_threshold_change` was still absent in the final source search and lookup during this handoff. Completing that promised AnyScope definition is a parent integration dependency, and the tier call must not ship unresolved.
- The bounded `.192` MCP trace returned focused `EVENT_INSPECTED_PARTIAL` with zero helper projections, revision `10aaec8852ad155188b9418a96fec3a0d1d9c7f07eaa5bd47c57cb3bc29062e8`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd8de541c76077291bc968e97c8cbd77af1707b7ab35226a05027e35373fe3df/c1bf3ad3de1fe9f0b527470aa342e4c8dfb564469766f06d2adb6927c449c48f/event-trace-10aaec8852ad.json`. No helper-lifecycle or runtime proof is inferred from that trace.
- No probability weights or timer definitions were changed here. The parent's frozen-baseline probability comparison, final helper/clock integration, and runtime evidence remain outside this hook assignment. No game execution, event rendering, or full graph comparison was performed.

Post-patch SHA-256 values: on-actions `f9f4a8dab178a89359b293050481779cbf721b56945442f62ec9e9ff86bf79b5`, meter `f2e4a3a6dbdd30bee11b5ceea021213cff23d772bc9ad05317988e15962ac257`.
Pre-patch values: on-actions `8820c68a0a41f1e426684d6356b6b98ba80f7ae405c9d60895409785c6f31a1d`, meter `5d081c81129363dba6960939b6e1d12ede0b637131a5d9a4b09f0728b0bfa8df`.
No gameplay simplification or substitute polling route was implemented.

Parent integration: `missiles_note_chaos_threshold_change` is defined in the new evolution-effects owner, resolving the missing-definition checkpoint above.
The state-control notification was narrowed after review to registered launch sites or an initialized programme's first/last controlled-state edge, retaining both new/former controller relevance checks.
Ordinary non-site frontline movement with continuing programme viability no longer schedules a registry observation.
This preserves the required viability transitions without using battlefield traffic as a background observation clock.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, with the earlier MTTH review retained as context and no skill files changed.
