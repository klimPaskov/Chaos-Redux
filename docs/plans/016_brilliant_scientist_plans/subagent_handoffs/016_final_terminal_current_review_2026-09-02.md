# Event 016 terminal current-source review — 2026-09-02

## Scope and status

Read-only terminal closure review, not overall Event 016 acceptance.
Source checkpoint: 2026-09-02 17:19:42 +03:00, HEAD `652c651e6aa0b530e736d951ecbfbde213d07704`, with concurrent uncommitted work preserved.
Only this handoff was written.
No gameplay, configuration, assets, spreadsheet, tests, or commits were changed; no HOI4 launch or logs were used.

Binding source: `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, especially line 48.
The relevant Part 8 terminal/counterplay/aftermath sections and Part 10 terminal achievement requirements were consulted.
Earlier `016_terminal_world_end_fallout_audit_handoff.md` and `016_decision_terminal_review_handoff.md` are historical evidence, not current acceptance.
Their old standalone Fallout effect filename is superseded by the current consolidated files; that is not a missing pipeline.

| Surface | Current status |
| --- | --- |
| Shared Chaos threshold and terminal mutex | Source-supported; separate LabWorld and Singularity readiness, permanent terminal exclusions, explicit verified-disarm reversal. |
| Six components and staged arming | Six distinct native component registrations present; physical loss/counterplay incomplete (T1). |
| Explicit disarmament | Armed/fail-deadly flags removed, persistent history retained, verification releases the commitment mutex; delayed certificate revalidation remains a small gap (T4). |
| Fallout request, lock, retry, cause memory | Source-supported request/lock/finalize ordering and idempotent consequences; MCP cannot expand these helper bodies in focused mode. |
| Defeat aftermath | Qualifying-global receipt gate present; local/regional duplication remains (T2). |
| World-threat history | Date-unit bug makes duration evidence unreliable (T3). |
| Six super-events / seventeen achievements | Exact registry counts confirmed, not an asset or balance acceptance. |
| Mengele terminal | Not designed or implemented here; only existing provider-neutral boundary identified below. |
| MCP | Narrow inspect/render evidence obtained; helper expansion and comparison gates remain incomplete, as detailed below. |

## Concrete findings, severity ordered

### T1 — High: audited facilities and “live” command/power counters are not live terminal prerequisites

Evidence:

- `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1338` counts presently owned-and-controlled facility states and sets/clears `brilliant_scientist_singularity_facilities_verified`.
- Its current callers are only paid audit decisions: `common/decisions/016_brilliant_scientist_directorate_project_board.txt:3858`, and `common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt:170` / `:189`.
- Arming continuation at `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt:434` trusts the retained verified flag and numeric component/node/power counts.
- Final commit readiness at `common/scripted_triggers/016_brilliant_scientist_triggers.txt:958` does not require current facilities at all.
- A current physical predicate already exists: `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:135`, `brilliant_scientist_has_required_singularity_facilities`.
- Node and power construction at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1354` / `:1359` only increment country counters; they bind no physical site and have no decrement writer.
- `brilliant_scientist_destroy_singularity_component` at `:1320` has no caller under current `common/` or `events/`.
The generic post-defeat arsenal dismantler clears the live-command flag, but that is not pre-detonation facility/component counterplay.

Causal fixture: earn all six components, the required node/power counts and weaponization, pass a facility audit, start the timed arming action, then lose the qualifying facility states without another paid audit.
The retained verified flag/counts still satisfy the arming continuation and final resolution.
After arming and fail-deadly activation, the terminal commit gate has no current-facility predicate to reject the same state.
This is source-observable; no unsupported live-engine result is claimed.

Smallest correction: reuse the existing current-facility predicate in start/continuation and terminal commit gates, with a resolution-time audit where needed for the player-facing count.
This closes stale-audit authorization without new content.
It does not by itself implement the accepted physical command/power/component interruption; the parent must connect the existing destruction/invalidation helper to accepted counterplay and physical loss boundaries, preserving permanent completion history separately from operational status.
Do not claim full counterplay from the existence of an uncalled helper.

Parent-requested separation of the repair:

- First gate correction: reuse the exact existing `brilliant_scientist_has_required_singularity_facilities` query for present owned-and-controlled facility sufficiency at arming, fail-deadly authorization and final commit boundaries.
Do not substitute `brilliant_scientist_krg_terminal_decisions_are_active` or a blanket `has_capitulated = no` in the shared final commit gate: the capitulation failsafe intentionally calls that same gate from the losing country, and the ledger-free wrapper must remain separate so an occupied Fallout ledger can retry.
Physical facility loss should block only by the accepted physical predicate, not because an ordinary decision UI has closed.
- Minimal physical receipt map: the existing paid command-node/power-link construction must record its actual authorized facility-state scope and the constructed role/quantity, then derive live counts only from surviving valid owned-and-controlled mapped sites.
Keep historical construction/component completion distinct from live counts; do not erase earned research when a site is captured.
An aligned state/role/quantity receipt list can preserve multiple already-permitted pieces at one state without inventing a one-per-state restriction, additional cost or additional node threshold.
The present construction decisions at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:3862` and `:3891` are country-only and select no site, so the parent must explicitly bind a valid existing facility at accepted construction start and revalidate that same target at completion; there is no current site identity to infer retrospectively.
Use existing state-control/destruction boundaries and bounded commit-time refresh, not a new global recurring scan.
Capturing a mapped site should remove its live contribution once; recovery may restore an intact contribution, while a deliberate destruction receipt must not auto-resurrect it.
This is a minimal implementation boundary recommendation for the already-accepted counterplay, not a new construction family or content plan.

### T2 — Medium: capitulation followed by annexation redispatches local/regional defeat rewards

Evidence:

- `common/on_actions/016_brilliant_scientist_project_on_actions.txt:71` and `:81` both call `brilliant_scientist_evaluate_defeat_after_global_threat`.
- The sovereign predicate at `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt:8` accepts `original_tag = KRG` (or the transformed-host receipt), even after the first defeat.
- The evaluator at `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:529` excludes only submitted/failsafe/qualifying-defeat/world-end receipts.
It does not exclude `brilliant_scientist_local_or_regional_defeat_recorded`.
- The local/regional branch sets that omitted receipt at `:476`, then delivers the recipient package again on another evaluator call.
- Recipient preparation at `common/scripted_effects/016_brilliant_scientist_aftermath_effects.txt:77` / `:84` unconditionally delivers `chaosx.nr16.301` / `.303`.
Those events have no consumed-popup click guard; .301.b adds stability/war support and .303.b grants political power.

Causal fixture: a non-qualifying KRG defeat triggers `on_capitulation`, then the peace settlement annexes the same original-tag KRG.
The second on-action passes the sovereign predicate and repeats local/regional preparation.
The same surviving former host can receive two popups and collect both option rewards.
Global qualifying defeat does not have this defect because its permanent receipt is already checked.

Smallest correction: exclude the existing local/regional recorded receipt at the common evaluator boundary before classification/dispatch.
For queued duplicate-popup safety, guard recipient option settlement with a matching one-use package receipt rather than allowing already-delivered duplicate windows to mutate again.
Do not erase the original defeated-country history or change the chosen custodian.

### T3 — Medium: world-threat duration subtracts encoded date values and compares them to day counts

Evidence:

- `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:362` stores `global.date` as the start date.
- `:388`–`:389` and `:402`–`:405` subtract that date from `global.date` into `brilliant_scientist_world_threat_duration_days`.
- The defeat scorer immediately compares the result to `duration_short_days = 180`, `duration_long_days = 365`, and `duration_epic_days = 730` in `common/script_constants/016_brilliant_scientist_super_event_constants.txt:105`.
- When no start date exists, the scorer leaves the absolute current date value as the duration.
- Installed `documentation/dynamic_variables_documentation.md:977` defines `date` as a date value for comparisons/localisation; `:996` defines `num_days` as current total days.
The required offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:959` explains that the date is encoded with one game hour equal to 0.00001.
Vanilla `common/ai_strategy/GER.txt:3847` uses `global.num_days` for actual day arithmetic.

Causal fixtures: a threat genuinely active for 180, 365, or 730 days does not produce a same-unit elapsed-day value for the three score tiers; a never-active small state instead receives a nonzero absolute-date “duration.”
The former also corrupts the substantial-duration evidence used by `brilliant_scientist_achievement_record_defeat_recipient_evidence` (`common/scripted_effects/016_brilliant_scientist_achievement_effects.txt:167`, `:176`).
The exact numeric score outcome is not a probability certification.

Smallest correction: preserve current date receipts for localisation, separately store start/end `global.num_days` and compute elapsed days from those values.
Initialize duration to zero when no valid start exists.
Do not reconstruct unproved elapsed history by assuming a date value was already a day count.
For disjoint active-threat episodes, accumulate completed active intervals in elapsed days and add only the current open interval when active.
Retain the original first-reveal date separately; otherwise a simple first-start-to-final-defeat subtraction would also count inactive gaps.
The parent was separately notified that other date-plus-duration consumers merit their own scoped review; no unrelated deadline system was audited here.

### T4 — Low: the final durable-settlement certificate has no delayed-state guard

`common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt:461` checks settlement availability when selected, waits the audit interval, and unconditionally calls completion at `:479`.
It has neither `cancel_trigger` nor `cancel_if_not_visible`.
`common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt:536` unconditionally grants the durable-settlement flag and administration gain before invoking the narrower verification helper.

Causal fixture: select a valid certificate, then enter another world-end state during the audit timer.
The delayed effect can still award settlement/admin despite terminal decisions being inactive.
This does not permit rearming because the arm gates retain explicit dismantlement/settlement exclusions, but it creates false post-terminal settlement history.
Reuse `brilliant_scientist_krg_can_verify_durable_nonterminal_settlement` as the cancellation/final commit gate; no new mechanic is needed.
The offline Decision modding page explicitly distinguishes selection-time `complete_effect` from timer-end `remove_effect` and says visibility cancellation is false by default.
Vanilla `common/decisions/AFG.txt:527` supplies a concrete timer cancellation precedent.

## Source-supported terminal scenarios

| Scenario | Current source outcome |
| --- | --- |
| Five components / missing node / missing power count | Arming rejects; no implicit armed or fail-deadly grant. |
| Six distinct native component callbacks, including repeated same callback | Six registrations at `common/special_projects/projects/016_brilliant_scientist_projects.txt:799,869,939,1009,1079,1149`; array membership deduplicates component count in the registration helper. |
| Singularity commitment followed by LabWorld selection | Commitment lock blocks the second route. |
| Armed route under controlled disarmament | Final Singularity readiness rejects while disarmament is active; completed disarmament clears armed/fail-deadly flags. |
| Finished hold and verified nonterminal settlement | Verification at `016_brilliant_scientist_effects.txt:3795` clears the Singularity commitment/lock while retaining construction/history; LabWorld can subsequently commit. |
| LabWorld has stale territory audit | Final completion reruns `brilliant_scientist_krg_audit_terminal_world_state` before readiness; current control, integration and major opposition are recomputed. |
| LabWorld below the shared final-plus threshold | Readiness rejects; it does not raise Chaos itself. |
| Singularity from Chaos below / equal to final minimum | Preparation computes only the nonnegative deficit to shared `tier_final.plus`; prelock Chaos is applied before admission. The special shared-meter reason permits the minimum-to-plus boundary. |
| Fallout ledger occupied | No submitted receipt or consequence package yet; bounded .901 retry is scheduled with a retry-pending guard. |
| Rejected own envelope | Fallout invokes the actor rejection callback, submitted is cleared and retry scheduled; prelock/consequence receipts prevent duplication. |
| Snapshot cannot lock yet | Shared envelope remains pending and host reconciliation retries validation; this is not another Event 016 consequence grant. |
| Successful shared lock | Fallout writes request-locked/transition-active/world-end/Fallout, then calls the source-aware actor finalizer; only its strict matching-actor trigger records scenario 12 and queues super 94. |
| Duplicate terminal execution/finalizer | Submitted/terminal receipts prevent repeated consequence and presentation commits. |
| Map return | Shared pipeline copies source/intensity/date and actor/state to cause-memory fields at `fallout_consolidated_effects.txt:44211`, then clears transient request fields. |
| Generic Chaos decrease during retry | Not a proven exploit: ordinary `add_chaos_meter_value` updates are frozen at the final threshold (`chaos_meter_effects.txt:4457`); hypothetical arbitrary direct variable edits were not treated as gameplay evidence. |
| Threat removed while another event remains a world threat | Event 016 clears only `world_threat_source_brilliant_scientist` and calls the shared refresh, preserving other source ownership. |

The six component tokens are command core, power link, containment lattice, temporal authenticator, delivery architecture and fail-deadly governor.
Their presence does not prove physical interruptibility (T1).
The generic Fallout explicit-terminal predicate is deliberately provider-neutral and has no Chaos threshold; the Event 016 caller owns that requirement.

## Exact registry counts and terminal history

Super-event mapping: the `brilliant_scientist_super_event` registry block in `common/script_constants/016_brilliant_scientist_constants.txt:1028` contains exactly six entries: recognition 90, formation 91, global threat 92, Laboratory World 93, Singularity 94, qualifying defeat 95.
These six entries map individually to image sprites in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:260`, title entries at `:655`, quote entries at `:919`, action entries at `:1183`, and description entries at `:1447`.
This counts registry rows once, not repeated occurrences across five presentation consumers.
The Event 016 queue is collision-safe against the shared visible flag and clears its actor only after visibility ends; current .300/.902 source and render cover its direct scheduling/cleanup branches.

The actual top-level achievement definitions in `common/achievements/chaos_redux_achievements.txt:3305`–`:3387` are exactly seventeen:
borrowed_century, every_door, public_method, the_one_who_left, clean_break, approve_everything, the_former_host, combined_arms_redefined, clever_girl, the_machine_continues, population_one, yesterday_sent_help, not_from_here, no_second_sun, the_last_calculation, the_world_is_the_laboratory, ordinary_people_won.
All have the `016_brilliant_scientist_` prefix.
The terminal-specific completion predicates are in `common/scripted_triggers/016_brilliant_scientist_achievement_triggers.txt:306`–`:349`.
Last Calculation requires a real capitulation failsafe plus submitted and fired receipts; Laboratory World additionally requires verified nonterminal Singularity history as demanded by Part 10, not merely no detonation.
No art/audio package was reaccepted and no weighted option/AI score was evaluated in this audit.
The parent retains probability-owner routing for changed weighted surfaces; current decision/aftermath AI blocks must not be called balanced from this report.

## Smallest existing provider-neutral Fallout boundary

Use the existing COUNTRY-scope `fallout_request_aftermath` envelope at `common/scripted_effects/fallout_consolidated_effects.txt:39229`.
Its inputs are temporary `fallout_request_source_input`, temporary `fallout_request_intensity_input`, optional regular COUNTRY target `fallout_request_actor_input`, and optional regular state target `fallout_request_state_input`.
It owns global-host handoff, free-ledger admission, persistent source/actor envelope, validation, snapshot-before-lock, phase scheduling and durable cause memory.
None of those input fields requires a Kruger identity, project array, meter or country flag.

The existing explicit-source validator at `common/scripted_triggers/fallout_consolidated_triggers.txt:28718` accepts chemical, biological, mixed and strategic-Singularity source kinds, subject to world-end exclusions.
A future approved provider can supply a truthful existing cause and its own authorized actor/receipt logic at this boundary, without copying the Fallout pipeline or fabricating Kruger state.
Do not silently reuse the strategic-Singularity cause for a different provider: its rejection callback at `fallout_consolidated_effects.txt:39321` and post-lock callback at `:39483` are specifically Event 016-owned.
Any future provider acknowledgement belongs in a minimal source/owner dispatch at those already-existing boundaries, with design approval retained by the assigned plan owner.
No new provider, source ID, terminal, achievement or super-event is proposed or implemented here.

## MCP evidence and exact limits

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
All returned current focused artifacts share revision `3278b34c53341a910d3959107765bb43be6cba2fb27f8562b8b0557d20fefc2f`, graph hash `33b3de6736a2f97d06a3ec40f40d528d1018bbec9b4a3064ed2874933698791a`.

Supported syntax actually used:

```json
{"mode":"trace","selector":{"kind":"file","sourcePath":"mod:events/016_brilliant_scientist_super_events.txt"},"direction":"both","expandHelpers":true,"maxDepth":1,"maxNodes":70,"maxEdges":100}
{"view":"neighborhood","selector":{"kind":"event","eventId":"chaosx.nr16.901"},"direction":"both","expandHelpers":true,"maxDepth":1,"maxNodes":35}
```

The initial manifest selected actual event IDs .300/.901/.902/.301/.302 and Fallout .1001/.1008, but its timing render selected only one node.
That bundle is retained as an unsuccessful coverage attempt, not used as proof.
File trace replacement was inspected locally: the super-event file trace contains .300, .901, .902 and four unresolved helper-call endpoints.
The individual .901 render has its real source event plus the two real helper callsites; the PNG was visually inspected and visibly labels those helpers unresolved.
These helpers exist in current source, so their unresolved status is a tool projection limitation, not an absent gameplay claim.
The other individual neighborhood renders selected .300 = 3 nodes, .301 = 5, .303 = 5, Fallout .1001 = 2, Fallout .1008 = 2; the final super-event-file render selected 7.
The traces/renders report `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL`, focused mode, zero helpers, and `validation.passed=false` because workspace-wide helper projections/lifecycle passes were deferred.
Their 2,205 global diagnostics were not counted as Event 016 failures or a clean pass.
There is no standalone LabWorld terminal country event: its owned decision calls the helper directly, which this focused projection cannot prove.

Comparison attempt used only the real freshly returned revision:

```json
{"before":{"revision":"3278b34c53341a910d3959107765bb43be6cba2fb27f8562b8b0557d20fefc2f"},"after":{"revision":"3278b34c53341a910d3959107765bb43be6cba2fb27f8562b8b0557d20fefc2f"},"render":false}
```

It returned `EVENT_REVISION_NOT_CACHED`, no artifacts, and a failed validation block.
Even a successful same-revision comparison would only check comparator availability, not prove an implementation delta.
No usable older terminal graph baseline was established by the prior handoffs.
No report-wrapper JSON was passed as a graph, no nonexistent revision was invented, and no repeat full scan/refresh was attempted.
Required semantic helper comparison remains blocked.

### Exact returned artifacts


Initial manifest trace (coverage-limited):

- event-trace-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b7d4edb432fb77ada84aabe6ff10c49df0ef5ed9e69e720145c1d5b942e68b05/e83c9dd16c54db2f66ba580757fe80dc3763f99a929c291c5df881ef11d66245/event-trace-3278b34c5334.json`

Initial timing bundle (one selected node; not coverage):

- event-timing-3278b34c5334-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1aa52ab3785ae94391732f1858428d836f75413265ce83a53784119fc62cd78/d9250899789c4a6126b82256baf722629290f4b99b3f272896ddf446ca27517f/event-timing-3278b34c5334-manifest.json`
- event-timing-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a09905fab637021995d03886bfee7d60ea19546cee0b5d79d768a3c43f7a80e/9b36a436ed9b91cd6295f740dac4ad0cd6b526f62aa7c24874b230bfc2be55fd/event-timing-3278b34c5334.json`
- event-timing-3278b34c5334.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9369c37e4324e5127529f2a18ca5bbec6bf945467bb80a52c35105cc8e8f6827/b78bffb630bab30edf0c5f436df0019531edf11b11d0f63d4cfee220031ff33e/event-timing-3278b34c5334.svg`
- event-timing-3278b34c5334.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f63de228a7da28c4b00b752d7aaf10f49829dacad4ffc25b063551e28adf54f5/f68c1197e82757197c4af34e06838bca55ec56137905daddb86126c54b1a9ebb/event-timing-3278b34c5334.png`
- event-timing-3278b34c5334.html: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7eadee2d9a4ef1ae546fdf1592dce65b8346ce2b32e6057ec8cfea19238f307b/2d4fc4aec14ce14e0f1c44f0cb8e20a791012c15bdb382e12d7d390322ef2a22/event-timing-3278b34c5334.html`

Super-event file trace:

- event-trace-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2af955b8b9fad313fe6cc49a792934cd48669123b5c361a526952274c852849/a77516ff2c60fe232bfe2b3e002b91c3f958099bf8b8a5ec76a7b6012fc4fdc0/event-trace-3278b34c5334.json`

Aftermath file trace:

- event-trace-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a045f54e64ee94e25b1fa6020bccadd7e3239050b038936dc9b6026c66eef82/b64fa506f467d0abae355595cadad313b5ac14e2ffbe21deb996b6484633ee58/event-trace-3278b34c5334.json`

Singularity retry .901:

- event-neighborhood-3278b34c5334-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f147ffc152acf5dc669c8f49c42bdcec4b77359fbcb385c5dc6525176abceef3/3c53c9c6cc16ab1d51ad0d032adc36115ac5459cf3fcebf0b5d1e85f635e03b5/event-neighborhood-3278b34c5334-manifest.json`
- event-neighborhood-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e007f5ebfcc61fc0e9596ccfd29bfcc22754677f58064519e7600e1e463c19d5/f3db84473ed3c073fac20f7120006e3569e7b626008300006b4ce1e5b4ea2aa5/event-neighborhood-3278b34c5334.json`
- event-neighborhood-3278b34c5334.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00e09b3e1242edbbb7510b6ae5c10f5d95e2aaf3de7f80f1bc8cb90a54e134e1/ca263ee136d61f554663721e4f646c539262ee51635cee93c0c1d4978bc045f6/event-neighborhood-3278b34c5334.svg`
- event-neighborhood-3278b34c5334.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22ade6e8c3c6d4bad52ca62701cbcd69013e8142fc94a57bbc428d8af519ae55/ba76d69032e9c2c1f1afed23ef5701279cf54bf713aa0785f75bce91bf5c5b4c/event-neighborhood-3278b34c5334.png`

Queue .300:

- event-neighborhood-3278b34c5334-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/55a9246ec875cb44ef3477ed0ef2d1fe7dedcbca45207cd6c3b3307e313a2840/9d05111481a9b2fb0107efb88d201094a1e03aba27d49e88c99f47d6ea728345/event-neighborhood-3278b34c5334-manifest.json`
- event-neighborhood-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0676ac3ceb3383ee6b4df658d87de3f84aa4345c80a713146a605a7a91dccaa3/ddd337eb4262d3c1b1ae85e85c85ad06ab729cada55265fd23f1bfc0158839ac/event-neighborhood-3278b34c5334.json`
- event-neighborhood-3278b34c5334.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b5f767abae39c281072d96a967f0846dd3fe018ecf0a792b4ca3caa716c783c/41315d36155fe53b9bd7f6a289de7940eb19117c7faa16d843f028ef1d7b26e8/event-neighborhood-3278b34c5334.svg`
- event-neighborhood-3278b34c5334.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e188a35674d63e2b32dcf22e3fc6e9723ebaca59df18a8e41b0d015ba497efce/140c645f69200389681e38fdf30ca619d344238ddeb4e6baedee98ac43d08f6a/event-neighborhood-3278b34c5334.png`

Local aftermath .301:

- event-neighborhood-3278b34c5334-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/440b426c05c4eead1530fb70b21812e334fff99144b4f950ca8c179677b3fe20/e401fda8ebd8e3df3b438adc6004a0c74285aeb4ddaa13b58766b2aac814ff80/event-neighborhood-3278b34c5334-manifest.json`
- event-neighborhood-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1289361bae907c843df97c321952f4ed99d42e9501fd4870e4c8da63a1f8572/0d5add5d4ef658a7f9ef77245aaafc0824477984959706581b474438222463c0/event-neighborhood-3278b34c5334.json`
- event-neighborhood-3278b34c5334.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ec390db5d75795fb294c45c772e2224e1c50e1e4d99070fa435809663fc66e2/d582a84aab56e689110161353fc3cc15ce56d3678f03b555a1e0b9aab5249bfa/event-neighborhood-3278b34c5334.svg`
- event-neighborhood-3278b34c5334.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c237bcddae78a429be2ab767cc548262cbda3235352d724d59f6fd9d896399a0/c6b080ce2f49b3abf740f4f1ddc1aa8391f07652f94094c103c4415406867cec/event-neighborhood-3278b34c5334.png`

Fallout snapshot .1001:

- event-neighborhood-3278b34c5334-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5073a08514bf159c1c4a86adcd8cfc52253d3653af7ab38879fe6a37199ff23/c388c93d93208704137dd17998b216bc41fca41c9be6cbc0f02cb06e5249c5b6/event-neighborhood-3278b34c5334-manifest.json`
- event-neighborhood-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f466ba77e9101e02fc425fdda5656238b44a589f97e3ade79e15b6e7525033ff/981bae221821e482404184884b5d3e5b2c553fbe98785e65f74cc5ec3814e35c/event-neighborhood-3278b34c5334.json`
- event-neighborhood-3278b34c5334.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6c88d9aa75f1eaccd92111ef80dd00f538d241300bc3e4e3789fff5ebd50dc8/9e7a074391f7f57cc7ea86ed9f00bdf4cd1714f5cf961975cba8a45203f7b0a4/event-neighborhood-3278b34c5334.svg`
- event-neighborhood-3278b34c5334.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25585c8b71d916d0f7e0937a75490b74d82653b2b6710bc9ff00cca5a26012a0/a2cdcf6038a05287de692ff12d919c5917c88047079d8ace154e8929f42985f9/event-neighborhood-3278b34c5334.png`

Fallout map return .1008:

- event-neighborhood-3278b34c5334-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a83910d9ffd5f2f9c4476a8adc7366df615b05e0f3d149da0730e74a5c8e566/aa021335b0a6a3e5d14fe4a41cc8f57010fc84684a7cce30cbd085835765c32d/event-neighborhood-3278b34c5334-manifest.json`
- event-neighborhood-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a20d54b67aa802fe1b95830888e11daf149df1648bd9f347cb3d9c05afcd35a/cad952ab42804cd09e1e9cc6f92598597366ed695417d8d52e537aafe7cba068/event-neighborhood-3278b34c5334.json`
- event-neighborhood-3278b34c5334.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2861652f40e81e67723681eac035c63274dc47de3b2bc752b6cd69838094f17e/572746a341cdcd85eabc29721f41d4947d838e53fdea03cbec95193a5045ea16/event-neighborhood-3278b34c5334.svg`
- event-neighborhood-3278b34c5334.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf0b1ed8166903fa0844a18d0626cc4a9b5cb230beae472ba37b17093ce74bda/0063bd6fea11564add6fafe20983c603b3e20022f97a4c41cdc539d2e395dfd7/event-neighborhood-3278b34c5334.png`

Super-event file render:

- event-neighborhood-3278b34c5334-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3ae4acd8341e431510894423324ec1fa4e61be24f99bb0f66fd5e9c257a6be4c/bc1f39466660f7f0ef7adcccc008397f179ce5f0dc052e243c5291ccce35152e/event-neighborhood-3278b34c5334-manifest.json`
- event-neighborhood-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7b895db3ac2ab9fa4a55bb700b0685fc8e7ba51a1dfa058374d3f06db724b6f/38d044bafd32292dc1ce7cf51a38995d6f41758f000ab3dcb456b3500633dfb9/event-neighborhood-3278b34c5334.json`
- event-neighborhood-3278b34c5334.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5fbbd5cc8e571ed3a4de39f0406e73ad5f94d9ae0edc50f1b4224aa26bc41d3c/91f30162623e105764c13bc53973d99f428bb6cc915b4e6aa882ba14c6a1262c/event-neighborhood-3278b34c5334.svg`
- event-neighborhood-3278b34c5334.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2922797932240f13e601748be3148e2da6a3e8e8b29ab22a6b8339cea4759747/2a731d213e9f97bfae734e5900e11cf2c94d3deae13221e9549b1ec67e08a6a7/event-neighborhood-3278b34c5334.png`

Regional aftermath .303:

- event-neighborhood-3278b34c5334-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9169e4e4bea000485a2919750d694c2196f6da6c091aad7681ec11eb09b2053b/436c43adf79e6611ace6b2894a9b1136b55437f23f68b5276a95bb738014f327/event-neighborhood-3278b34c5334-manifest.json`
- event-neighborhood-3278b34c5334.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f58b14e153c200c44543587b6bb54246c45377f1fc79de24e2fa2483d2dbbd3/f109a1f2f33c54fd847aca82632cfaba39e00769bcb2854be22157fbbea3b3f4/event-neighborhood-3278b34c5334.json`
- event-neighborhood-3278b34c5334.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2be758532d373f86cc31852e9b0d3be859171cd2cb82292ce2859eb6b8242551/3970cbda3da14b8a82cb9402efb4cdb48d0e443450d655a96ce0edf64c68a06a/event-neighborhood-3278b34c5334.svg`
- event-neighborhood-3278b34c5334.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbc4cf17acd5a24c59e5691b2e188cbb7be1eccfdae8592e11e7e7de786d5ebe/8ad5affe81a96ce0d813cfce324bb14d79e1226a9c5efdc4a543595804a1dc00/event-neighborhood-3278b34c5334.png`

Cached PNG paths are derived from the returned artifact SHA-256, not regenerated.
For the inspected .901 image: `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/22/22ade6e8c3c6d4bad52ca62701cbcd69013e8142fc94a57bbc428d8af519ae55/event-neighborhood-3278b34c5334.png`.
Final super-event-file PNG: `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/29/2922797932240f13e601748be3148e2da6a3e8e8b29ab22a6b8339cea4759747/event-neighborhood-3278b34c5334.png`.

## Source hashes and remaining gate

SHA-256 at the checkpoint above:

| File | SHA-256 |
| --- | --- |
| common/scripted_effects/016_brilliant_scientist_effects.txt | 7c4c07af4ab81180186191a320fdd1ebb5874ccb7620cc9cda5b17f6918e0a48 |
| common/scripted_effects/016_brilliant_scientist_super_event_effects.txt | 8d0e861c8e7afcd9e7032e4ebb207c5e1700cb8570cf2233286c0e103387bcbc |
| common/scripted_effects/016_brilliant_scientist_project_effects.txt | 6406e3e8087cd475193a6ca470a81f2976e889a6831098897b9ad334cba349d1 |
| common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt | e3172f478e3341f2a71c79853d273758067f0494d5d10c3d1562654e8dc0f8e7 |
| common/scripted_triggers/016_brilliant_scientist_triggers.txt | ef9b7964617cb6b73cf5bc230fd31751081a0ffc21cca999575dbb45f3853636 |
| common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt | dd64d502d862d8ec5912a59e5f892a7539626560998d1f84e4e4b259d4e48830 |
| common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt | 5f1e6274add0cb94ea5bcebffa81d408a07f01770b1c78324dd8c29652a46646 |
| common/scripted_effects/fallout_consolidated_effects.txt | a25aebe6ab9d8c6d51274af18d82f6bdc357530c588bcc8e541a326ab827c3a6 |
| common/scripted_triggers/fallout_consolidated_triggers.txt | 8cad1d243becb1752dc427f1218e68f8279996be6b8a99bada9e662d527488a8 |
| events/016_brilliant_scientist_super_events.txt | 9d818531b8f3813ecad0c3bfea12ab2ccc9fae38e09898f68f01f255e488ffda |
| events/016_brilliant_scientist_aftermath_events.txt | 8889b4f92aff48169548bea0597355fd1390a79bf525f4a8e349fdba15dfb7b2 |
| events/fallout_world_end_events.txt | 407af86202611e80eeecdc10eddb6c4c0375fb700450fa53c217416251654eff |
| common/on_actions/016_brilliant_scientist_project_on_actions.txt | d56934ac7016e8229a135b63b6240a2ecc70a37bcce3dc3aeb836b60d08125d8 |
| common/achievements/chaos_redux_achievements.txt | a3fafa1fbafdcd35ad9c4ec6cc2058b7aeaf3fb6f740f2b2f5b7c15e9d8f4a00 |
| common/script_constants/016_brilliant_scientist_constants.txt | adfee7fe6093933c394c34c8a6a162795d4bdb4575512c476b417c1173b6e4a6 |

Skills used: chaos-redux-events, chaos-redux-subagents, chaos-redux-improvement-loop, chaos-redux-event-planning, chaos-redux-decisions-missions, chaos-redux-event-assets, chaos-redux-super-events.
They required source-of-truth separation, timer semantics, registry-row counts, and explicit MCP limitations; no skill was changed.
The source review found no reason to duplicate the Fallout pipeline or add content.
T1–T4 and incomplete helper/compare evidence remain explicit blockers to accepting this bounded terminal surface.
No simplification was implemented by this reviewer, and no overall completion claim is made.
