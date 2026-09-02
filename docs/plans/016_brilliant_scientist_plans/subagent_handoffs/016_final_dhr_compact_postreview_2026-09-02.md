# Event 016 DHR compact lifecycle post-review

## Result and boundary

Read-only source review of the owner-applied C1–C3 compact patch found no new concrete source regression in the bounded `.49` delivery, response, notification, and `.52` expiry chain.
The prior C1–C3 source defects are addressed: response mutations are click-guarded, every delivery requires the undelivered receipt, and stale watchdogs must match the current recipient and respect the current deadline.
This is conditional source acceptance, not overall Event 016 completion or a claim of complete MCP lifecycle validation.
The mandatory bounded inspect/render returned partial evidence without helper bodies, and the one before/after comparison failed because a requested revision was not cached.
The source does not establish a generation identity for an already-open popup that might survive annexation and later re-release; that engine-lifetime guarantee remains unproven.

Scope was restricted to `chaosx.nr16.49`, `.50`, `.51`, `.52`, their exact offer decision, receipt helpers/triggers, timing constants, and English tooltips.
No gameplay, asset, configuration, spreadsheet, or other documentation file was edited by this auditor.
No game was launched, no logs were requested, and no commit was made.
The binding design remains `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
The preceding `016_final_dhr_compact_lifecycle_review_2026-09-02.md` remains the prepatch evidence; its C1–C3 findings are superseded for the source hashes below, not erased.

## Remaining findings, severity ordered

1. **Validation blocker, not a demonstrated gameplay defect: same-pair popup lifetime after annexation/re-release is unproven.**
   `dhrondan_compact_receipt_matches_recipient` identifies the current actor/recipient pair, not an immutable per-popup generation (`common/scripted_triggers/016_dhrondan_country_triggers.txt:178`).
   Its ordinary safety argument is serialization until guarded native timeout, followed by the actor-owned deadline.
   The offline event documentation establishes the normal native timeout and separately describes freezing delayed events on nonexistent recipients, but does not establish that an already-displayed popup must disappear, finish its timeout while annexed, or be unable to survive a later re-release.
   If such an old popup survived beyond cleanup and a later offer reused the same pair, the current pair/deadline guard alone would not distinguish it.
   Do not claim this scenario is proven safe or turn that hypothetical engine behavior into an asserted current exploit.
   No simpler verified engine mechanism was identified in the bounded reference review, and no unapproved fallback is recommended.

2. **Validation blocker: required MCP comparison and complete helper lifecycle evidence are unavailable in this pass.**
   The post graph has zero helpers despite `expandHelpers=true`; it therefore cannot prove the helper-owned expiry loop, receipt finalization, reconciliation, or full decision-to-popup chain.
   `event_compare` returned `EVENT_REVISION_NOT_CACHED`, `validation.passed=false`, zero artifacts, and no changed-file result.
   Preserve these limits in owner completion reporting; source reasoning is not equivalent to the missing tool evidence.

There is no additional actionable source patch recommendation from this post-review.
No gameplay simplification was introduced by this auditor.
No new asset, GUI, country, evolution, reward, or weighted design was audited or requested.

## Source acceptance and exact ownership

| Surface | Evidence | Review result |
| --- | --- | --- |
| Offer authorization | `common/decisions/016_dhrondan_country_decisions.txt:178`, `:186` | Availability forbids an active offer; completion captures the original DHR actor and recipient before dispatch, records the persistent target, sets the initial deadline, and schedules only while the receipt still matches. |
| One-time delivery | `events/016_dhrondan_country_events.txt:32`, `:43` | Both existing countries, exact receipt ownership, unexpired deadline, and mandatory `NOT delivered` are common admission requirements. Immediate marks delivery and refreshes the deadline once. |
| Identity independent of legality | `common/scripted_triggers/016_dhrondan_country_triggers.txt:178` | Current recipient must equal both original regular recipient and current global offer target; regular actor must be DHR and own the active flag. Invalid diplomacy can still close its owned receipt. |
| Valid versus cleanup option pool | `events/016_dhrondan_country_events.txt:51`, `:84`, `:111` | `.a/.b` require the same valid predicate; `.c` is its inverse. Cleanup cannot compete in the valid source pool. No probability claim is made. |
| Click/timeout commit | `common/scripted_triggers/016_dhrondan_country_triggers.txt:192`, `:208`; `events/016_dhrondan_country_events.txt:66`, `:98` | Both mutation blocks recheck existence, sovereignty, Covenant route, peace, absence of an existing compact/NAP, exact pair ownership, delivery, and current unexpired deadline at execution time. |
| Acceptance/refusal settlement | `events/016_dhrondan_country_events.txt:67`, `:74`, `:99`, `:101` | Acceptance applies the existing NAP/opinions/partner history and DHR stability once; refusal applies its existing opinion effect once. Receipt is cleared before notification `.50/.51`. Actor-side opinion uses the explicit regular recipient, not a shifted ROOT. |
| Invalid/stale response cleanup | `common/scripted_effects/016_dhrondan_country_effects.txt:276`; event `:78`, `:105`, `:113` | All three cleanup paths call the ownership-and-delivery guard. A different recipient or no active receipt produces no mutation. |
| Permanent history conservation | `common/scripted_effects/016_dhrondan_country_effects.txt:268` | Finalizer clears only active/delivered flags, expiry variable, and global pending target. It does not clear concluded/partner flags or undo settled relations. |
| Native timeout and grace | event `:31`; constants `:78`, `:79`; effects `:288` | Native timeout remains 13 days, explicitly mirrored by the shared timeout constant. First delivery records current date plus 13 days plus one cleanup-grace day. |
| Bounded watchdog | triggers `:219`; event `:142`; effects `:296` | Original actor/current actor and original recipient/current target must match. Before current expiry, reschedule only the remaining duration; at expiry, finalize. No daily poll or world iteration is added. |
| Runtime reconciliation | effects `:306`, `:353` | Current active receipt with persistent target restores regular pointers and retains an existing deadline. An undated active receipt receives one complete window without popup redispatch or reward. Orphaned/no-active state is cleared. |

The exact receipt-writer/caller search found no additional clearing or deadline-writing path outside the reviewed chain.
`.50` and `.51` contain only notification presentation and their empty acknowledgement options (`events/016_dhrondan_country_events.txt:117`, `:126`); they cannot settle the reward again.
The new English accept/refuse/expired tooltips (`localisation/english/016_dhrondan_country_l_english.yml:124`) describe the current guarded result and invalid closure without implementation-history wording.
The existing `.a/.b` AI blocks and decision score are unchanged in the reviewed diff; probability evaluation/comparison is owned by the parent's `chaosx_ai_probability_auditor`, not certified here.

## Meaningful source scenarios

These are source traces, not simulated engine executions or MCP scenario proofs.

| Scenario | Source outcome and limit |
| --- | --- |
| Valid acceptance | `.a` commits only while the delivered owned receipt is valid and unexpired; one stability grant, one compact settlement, pending state cleared before `.50`. A stale repeat with no active receipt is inert. |
| Valid refusal | `.b` applies the existing refusal opinion once and clears before `.51`; later intentional offers remain subject to the existing decision cooldown. |
| War, subject change, Covenant route loss, world end, existing NAP, or recipient compact status changes after popup opened | Previously visible `.a/.b` cannot execute their diplomacy/reward block when the current predicate fails; their else branch closes only the delivered owned receipt. |
| Initially invalid but still owned delivery | `.49` can show only cleanup `.c`; it marks the one delivered receipt, and owned cleanup closes it. This does not compete in a valid AI option pool. |
| Deferred duplicate `.49` while first popup is live | Common `NOT delivered` admission rejects it, regardless of whether diplomacy remains valid. No second immediate refresh or duplicate response pool is admitted. |
| Deferred stale `.49` after receipt cleared, or after a new different-recipient offer | Active/pointer ownership fails; it cannot refresh, grant, or clear the new offer. A hypothetical arbitrarily long deferred same-pair event is not assigned a fabricated generation identity. |
| Old `.52`, different current recipient | Event trigger fails the original-recipient/current-target comparison; the new offer is untouched. |
| Early `.52`, same current pair | Reads the new offer's current expiry, not its own original scheduling age; it schedules remaining days and cannot clear that receipt before its current expiry. This remains safe whether new offer is delivered or still undelivered. |
| First delivery occurs later than authorization | Delivery refreshes deadline to actual delivery plus 14 days. The initial watchdog reschedules to that deadline, retaining the normal native popup window. |
| Native 13-day timeout in ordinary existing-country lifecycle | Normal first-option resolution enters the same guarded effect block. The actor deadline is one day later; an expired/invalid commit is prohibited even if invocation ordering is unexpected. An invalid option invocation can only close its owned delivered receipt. |
| Recipient destroyed while DHR remains | Response commit fails existence. The actor-owned watchdog does not require recipient existence and can finalize the matching receipt at its deadline; this depends on the country target remaining addressable, not on a recipient timer. Popup lifetime through subsequent re-release remains the explicit validation blocker above. |
| Actor destroyed | No recipient response can commit while actor existence fails. Actor delayed timers are documented to freeze while the country does not exist; do not describe cleanup as instantaneous while DHR is absent. Runtime reinitialization restores surviving current pointers, preserves any past deadline, and schedules bounded cleanup with minimum one-day delay. |
| Reinitialization before deadline | Reconciliation does not extend an already dated offer or redispatch `.49`; multiple pending watchdogs are harmless source-wise because each checks current ownership and expiry before idempotent finalization. |
| Undated active receipt | Reconciliation gives one dated window and no new popup. Subsequent reconciliation retains it; ordinary native timeout still governs any existing popup. This does not prove preexisting popup lifetime through annexation. |

## Reference basis

Required AGENTS.md, the core offline wiki pages, and the event/decision skill references were consulted.
The relevant narrow engine references are:

- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:31`: delayed country-event timers on nonexistent countries pause until release.
- The same page `:149`: option visibility trigger is evaluated at event firing, which is why effect-time guards are required.
- The same page `:174` and `:178`: immediate execution and native timeout behavior; the default timeout is 13 days and timeout selects the first option.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:292`: regular event targets carry into events fired from their chain; `:415` does not support using temporary variables as persistent per-popup snapshots.
- Installed vanilla `documentation/effects_documentation.md:2943`, `:6496`, `:6505`, `:2733`: country-event scheduling, regular/global event targets, and explicit global-target cleanup.
- Installed vanilla `events/Generic.txt:38`, `:56` and `events/WTT_China.txt:191` use `tag = event_target:...`, supporting the explicit target comparison syntax used here.
- Installed vanilla `documentation/effects_documentation.md:3564` documents `diplomatic_relation`'s `active` field; the MCP unresolved `active` label is not evidence that this native field is an absent scripted helper.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, and `chaos-redux-event-planning`.
Their audit/evidence and bounded-ownership requirements kept this review source-specific and kept incomplete MCP evidence separate from source acceptance.
No skill was changed, and no asset-specific skill was needed for this patch.

## MCP invocation, artifacts, and exact limits

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Only bounded post inspection/render and one cached-revision comparison were requested; there was no broad refresh or retry loop.

```json
{
  "tool": "hoi4.event_inspect",
  "workspaceId": "mod_chaos_redux_ea3b2d67c2c0",
  "mode": "trace",
  "selector": {"kind":"manifest","manifest":{"id":"event016_dhr_compact_postreview","eventIds":["chaosx.nr16.49","chaosx.nr16.50","chaosx.nr16.51","chaosx.nr16.52"]}},
  "direction": "both",
  "expandHelpers": true,
  "maxDepth": 2,
  "maxNodes": 28,
  "maxEdges": 70
}
```

`hoi4.event_render` used the same workspace/selector/direction/helper/depth/node values with `view="neighborhood"` and no `maxEdges` argument.
It returned 20 selected nodes, 42,462 omitted workspace nodes, layout hash `2280cc55fdc9b9713f713715155fff7b76bd9b95c7161cdc46c0eb920216a805`, and partial status.
The selected trace itself reports `truncated=false`; this does not make the helper-free graph complete.
The returned PNG was visually inspected: `.49.a/.b` link to `.50/.51`, acknowledgements terminate, and `.52` links to unresolved schedule/clear calls.
No separate post options or timing PNG was generated; do not label the prepatch options/timing PNGs as postpatch evidence.

Post revision: `d8c9140e69ae6d53f2fb77284bb37300a75d320975ad211d21933a46986988cf`.
Graph hash: `968ca8618104d6399b47b0fac0eacfc1221bd54aea4b4cd64e6edb2a6384eb9a`.
Both inspect/render report `validation.passed=false` and explain that large-workspace analysis deferred workspace-wide helper projections and lifecycle passes.
The reported 2,205 workspace issues are not all Event 016 diagnostics; zero blocking diagnostics is not a clean lifecycle pass.

Exact source-linked unresolved nodes in this selected chain are `dhrondan_refresh_compact_expiry` at event line 45; `dhrondan_clear_diplomatic_offer` at 74, 101, 151; `dhrondan_close_owned_compact_response` at 78, 105, 113; `dhrondan_schedule_compact_expiry` at 149; and native `active` at 67.
The four real helper definitions exist in the reviewed effects file at 288, 268, 276, and 296 respectively.
The focused graph's source hash map includes the event file but excludes these helper files, so it cannot certify their contents.

Artifacts:

- Trace JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c69470b87745fddecb64df23f924d95345c35c1c15edd92204b7e5908c1274f/4b07fb702f0e9b84e5f752f0cf8409dc6dc00422583cc3d90926d94f1781a085/event-trace-d8c9140e69ae.json`
- Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/328d517e996679bb886e263fe499617f730d6539da17e769ffa7d07d234e96e7/3c74b877d13023da371350777cd5870b93f843c5d9ce7909395e770f755942ef/event-neighborhood-d8c9140e69ae-manifest.json`
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1006b5db9905cc559c2be0f607a6170eeace6f5026ce1935992a572485189c4/bf8f129dd08a2a07e8699dd526162588f8cbbfc57da5a9deee1e64dab3a12749/event-neighborhood-d8c9140e69ae.json`
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/365c031ecc6766c68980e4dcbfa721e94a6cc7ab624d814a64a2d2bde140ec0e/868611596b41402ac402afe2fade1abc7088f2673a72ea5d2f2561484be65ae2/event-neighborhood-d8c9140e69ae.svg`
- Render PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0a9ae7ae429570dba3d8b1e4b0947fedffc95c95ff4bc589941ccbcebeaf8e8/8e9a14c9fa6257276f4c62ebe0393f450a63c35e1243c01e2349102305b3e6fd/event-neighborhood-d8c9140e69ae.png`

Local cached PNG for direct owner inspection:
`C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/c0/c0a9ae7ae429570dba3d8b1e4b0947fedffc95c95ff4bc589941ccbcebeaf8e8/event-neighborhood-d8c9140e69ae.png`.

Exact comparison request:

```json
{
  "workspaceId":"mod_chaos_redux_ea3b2d67c2c0",
  "before":{"revision":"18bf807c8be35655138be368b38a6ff43f90d4c9ac0a1470ca1d9d44f43afd8f"},
  "after":{"revision":"d8c9140e69ae6d53f2fb77284bb37300a75d320975ad211d21933a46986988cf"},
  "render":false,
  "refresh":false
}
```

Result: `status="error"`, `code="EVENT_REVISION_NOT_CACHED"`, blocker message `Requested event graph revision is not cached`, no files scanned, no changed files, no artifacts, `validation.passed=false`.
The earlier report-wrapper artifact is not retried as an alleged durable full graph; its schema incompatibility was already recorded in the pre-review.

## Frozen source identity

Captured 2026-09-02 12:55:46 +03:00 with HEAD `588c2f12f02890cf3f7947847927307347204629`.
HEAD alone is not the audit identity because the owner's patch is in the shared working tree.

| File | SHA-256 |
| --- | --- |
| `events/016_dhrondan_country_events.txt` | `6bfe2a945fa02dcda157f8e3eb50c553b41530ffba3d6bae914312bf83115b00` |
| `common/scripted_effects/016_dhrondan_country_effects.txt` | `953b15ab38a0f71a2d4364d4cabec6dcc78eacf1b16adbcffa9eb4af5391fc56` |
| `common/scripted_triggers/016_dhrondan_country_triggers.txt` | `e82b7b4f44ff3b38ff0561a268960f811d04363071555cdd6e30ebebebe53ee2` |
| `common/decisions/016_dhrondan_country_decisions.txt` | `7170ba263608ba78243d78d680925c37849b13244064f83fddb32b33b06896a9` |
| `common/script_constants/016_dhrondan_country_constants.txt` | `a5921c1d2d84c6956bae32dd6cc8487fe1599f2ccbda13c491507358a46960d7` |
| `localisation/english/016_dhrondan_country_l_english.yml` | `eb35fb48fbc1b2ca76986fecdeb6edf67e27ef633fbf6bcc898d38aa35f3dd8a` |

The MCP trace event-file hash matches the reviewed event source byte hash above.
Parent retains final documentation, the probability-owner result, any further engine-evidence disposition, and final commit/completion ownership.
