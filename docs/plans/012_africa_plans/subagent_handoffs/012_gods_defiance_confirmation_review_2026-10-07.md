# Event 012 permanent-defiance confirmation source review

Disposition: `implemented` at source level, with MCP comparison, probability evaluation and native behavior still `unresolved` under their assigned owners.
Verdict: no blocking source defect found in the bounded confirmation flow.
This is a manual source and diff review, not execution evidence or a whole-feature completion claim.
Acceptance basis: the parent supplied the accepted confirmation requirement, `docs/specs/012_africa_is_one_gods_of_africa_specs/specs/012_gods_of_africa_full_spec.md:658-672`, and `012_gods_decision_repairs_2026-10-07.md:3-11` records the human confirmation, current-authority recheck, consequence-free cancellation and preserved direct AI choice.

## Scope and observed diff

Only this handoff was written.
No gameplay, other documentation, index, commit or game-launch action was performed.
Read-only Git diff inspection was used solely to satisfy the requested actual-diff review.
The tracked decision diff changes only `gods_of_africa_permanent_defiance.available` and `.complete_effect`, and leaves `visible`, cost, repetition policy and `ai_will_do` unchanged.
The event diff only appends `.622` at `events/012_africa_gods_of_africa.txt:543-570`.
The three new confirmation helper files were read directly because new-file contents are not supplied by an ordinary tracked diff.
The localisation diff includes the seven confirmation keys at `localisation/english/012_africa_gods_l_english.yml:278-284` and a separate expedition-cost change at lines 198-200, which is outside this review.
No diff was present for the canonical defiance owner or the existing core participant/contract guards in the bounded tracked-source comparison.

## Helper and receipt map

All helpers operate on the participant COUNTRY, use boolean calls, and have no parameters, inferred amounts or temporary outputs.

| Helper | Inputs and result | Writes and consumers |
| --- | --- | --- |
| `gods_of_africa_defiance_action_is_valid` | Existing participant/authority eligibility, current history owner/origin, and closable ledger if a demand is active | Read-only shared request/confirmation preflight, matching `gods_of_africa_declare_defiance`'s entry gate |
| `gods_of_africa_defiance_request_is_available` | Action preflight plus AI control or absence of the pending human receipt | Read-only gate inside request helper |
| `gods_of_africa_defiance_confirmation_is_current` | Pending receipt, action preflight, presence and equality of all four frozen authority fields against `event_target:africa_host` | Read-only firing and click guard |
| `gods_of_africa_request_defiance_confirmation` | Rechecks request gate in the decision owner scope | Human: pending flag, four normal variables, one regular named host target, one `.622` call. AI: clears receipt and invokes canonical defiance directly |
| `gods_of_africa_confirm_permanent_defiance` | Requires `is_ai = no` and current confirmation | Consumes receipt before canonical defiance. Rejection only clears receipt. Called by `.622` Confirm |
| `gods_of_africa_clear_defiance_confirmation` | No authorization requirement | Clears only pending flag and four receipt variables. Called by Cancel, confirmation success/rejection, and AI direct branch |

Authority receipt variables are `gods_of_africa_defiance_confirmation_host_id`, `_origin_id`, `_generation` and `_epoch`.
The regular `gods_of_africa_confirmation_host` target is saved inside the frozen host scope before `.622` fires and supplies the dialog name, not authorization or a successor redirect.
Regular-target lifetime belongs to the native event chain and needs no global-target cleanup.
Host loss leaves the unanswered UI envelope pending, while existing authority guards make it inert.
The scan found no other writers or cleanup paths for this pending flag or these four variables, so a second human request cannot overwrite the still-open envelope.
No shared tuning constants, timer, price, deadline band or new gameplay cleanup hook are introduced.
Existing Wrath, protection, ledger closure, history, demand cleanup and report ownership remain in the canonical action.

## Scenario verdicts

Each result below is a source trace through actual helper bodies, not a simulated or native run.

| Case | Source verdict |
| --- | --- |
| Valid human request | PASS: full action gate precedes the five receipt writes, regular host target and single popup call. No debit, Wrath, history, protection, ledger closure or deadline write occurs |
| Duplicate human request while pending | PASS: request availability rejects it before any receipt overwrite or second popup, even if the decision callback is invoked after its displayed availability became stale |
| Valid human Confirm once | PASS: human control, current permissions and all four authority equalities are rechecked, receipt is consumed first, then existing canonical defiance runs |
| Cancel once | PASS: always-visible first option calls only receipt cleanup, with no defiance or report call |
| Repeat Confirm or Cancel before any fresh request | PASS: Confirm finds no pending receipt and only clears already-cleared fields. Cancel remains idempotent. Neither repeats gameplay or `.609` |
| Stale host object, origin, generation or epoch at firing | PASS: Confirm is absent at firing. Cancel remains available because `.622`'s overall trigger only requires the pending envelope |
| Host loss or authority change after popup | PASS: Confirm can remain visibly present, but click-time current-authority and tuple guards reject it and clear the receipt. No successor receives defiance through the old request |
| Negotiation or reconciliation begins after popup | PASS: existing `participant_can_defy` rejects the active negotiation/reconciliation phase on click. Broken history identity or unclosable active ledger also rejects. This is a current-state check, not a permanent record that such a phase once occurred |
| Active demand deadline passes after popup | PASS: unchanged `demand_contract_is_current` rejects an expired active demand. The request does not stop the ordinary deadline or its existing owner resolution |
| AI direct decision | PASS: same wrapper immediately calls existing defiance after the actual action preflight and never opens `.622`. The original willingness expression is unchanged in the diff. Eligibility now also reflects canonical history/ledger permissions, so unchanged weights alone do not prove identical selection behavior |
| AI at popup firing | PASS: `is_ai = no` removes Confirm at firing, leaving only consequence-free Cancel |
| Human becomes AI after popup | PASS: previously visible Confirm still reaches the helper's `is_ai = no` rejection, which clears receipt without gameplay. Cancel also remains safe |
| Unanswered human timeout | SOURCE/DOCUMENTATION PASS: Cancel is option zero and no timeout override exists. The offline reference specifies first-option selection, default 13 days. Actual native expiry remains unverified here |

The invocation scan over engine-facing `.txt` sources found one human request entry point, the permanent-defiance decision at `common/decisions/012_africa_gods_decisions.txt:862`.
Direct canonical calls exist only inside the wrapper's AI branch and guarded Confirm branch at confirmation effects lines 21 and 43.
`gods_of_africa_declare_defiance` is called only by the existing canonical helper at `012_africa_gods_effects.txt:4965`.
There is no alternate human event or GUI call bypassing confirmation in the scanned source.

Participant permission follows `012_africa_gods_triggers.txt:25-36,168-184,576-587` and epoch bindings at `012_africa_gods_epoch_binding_triggers.txt:4-23`, rather than applying the host-only ROOT guard to the participant.
Canonical `gods_of_africa_declare_defiance` retains its own identical preflight at `012_africa_gods_effects.txt:4053-4059`.
The canonical outer helper at lines 4964-4967 still schedules `.609` after that guarded action, so it is not a standalone success-receipt API.
Within the current entry points, the preceding request/confirmation preflight prevents an invalid callback from reaching that outer helper.
`.609` remains an aftermath report, with only its tooltip and report-pending cleanup in its option at `events/012_africa_gods_of_africa.txt:154-170`, and is not a second confirmation or defiance commit.

## Bounded text and art consumer review

The title, body, Confirm and Cancel keys resolve at localisation lines 281-284, and the two availability tooltips plus request explanation resolve at lines 278-280.
The body uses the frozen regular host name `[gods_of_africa_confirmation_host.GetNameDef]` with the correct localisation namespace and plain parchment text.
It describes open-demand refusal, protection withdrawal, closed ordinary friendship, possible punishment and Africa-approved restoration consistently with the canonical outcome and `.609` aftermath wording.
The request explanation describes the wrapper's consequences, while ordinary campaign clocks continue independently.
Both options have no explicit `ai_chance`, consistent with the documented default weight 1, without claiming any normalized selection result.
The existing report sprite resolves at `interface/012_africa_event_pictures.gfx:17` to `gfx/event_pictures/012_africa/report_event_012_africa_gods_defiance.dds`, whose file exists, and is already consumed by `.609`.
No image inspection, new art, image generation or UI redesign was required by this task.
Text fit, rendered appearance and native dynamic naming were not visually established.

## Reference and artifact evidence

The connected metadata exposes `hoi4.event_inspect`, probability inspection and all four reference/source routes.
No new MCP call was made because the parent explicitly retains source/MCP validation and the probability specialist retains scenario fixtures and comparison.
Exposure alone does not establish route health, and this source review does not substitute for those passes.
Parent-provided reference revisions were independently matched against local file SHA-256 and the pertinent sections were reread locally:

| Source and lines | Revision / local SHA-256 |
| --- | --- |
| Installed `documentation/triggers_documentation.md:5244-5252`, `is_ai` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation/effects_documentation.md:2943-2967,6496-6504`, country event and regular target | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:151-163,180-186`, visibility, default weights and timeout | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:263-305`, event targets and localisation namespace | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |

Installed paths above are under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Vanilla `events/WTT_Germany.txt:3277-3333` supplies native report-confirmation anatomy, but does not prove this receipt lifecycle.
Project `events/019_infantry_spawn_scenario.txt:22-60` supplies pending receipt and Confirm/Cancel precedent, but its affirmative-first option order is deliberately not copied.
The neutral helper registry at `common/scripted_effects/chaosx_dynamic_effects.md:3-5,480` identifies owner-local APIs and links the matching confirmation documentation.

The existing specialist artifact is [012_gods_defiance_confirmation_probability_2026-10-07.md](012_gods_defiance_confirmation_probability_2026-10-07.md), with fixtures in `012_gods_defiance_confirmation_probability_2026-10-07_evidence/scenario-set.json`.
At the time read, it records successful BEFORE inspection only, no effective scenario scores and no successful AFTER comparison.
Its exact reported recovery blocker is `Artifact provenance manifest is unavailable`, while stopped/pending inspections and evaluation returned no usable evidence.
Those limits remain with the specialist and parent, and are not treated as a failing gameplay scenario or proof that an exposed route is absent.

Reviewed source identities, SHA-256:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/012_africa_gods_confirmation_effects.txt` | `17d4ad64bee0c5d698d6cab46bb2302effe36e84b68b1fd6584466930ecd4ff4` |
| `common/scripted_effects/012_africa_gods_confirmation_effects.md` | `da61732173ea06230a16a7e0e46625d4e498c83635629bda098598e30b3365c3` |
| `common/scripted_triggers/012_africa_gods_confirmation_triggers.txt` | `a3d99c1fbad86c12b574862191cc4917c133a4694d39d01a14d6bd06eb10b04d` |
| `common/decisions/012_africa_gods_decisions.txt` | `a37d5bf0b1fcdd7a361f7bb27a9ec9b2bda855f6de944af5f76e3070e03b9c87` |
| `events/012_africa_gods_of_africa.txt` | `b61c29b561c4aacf7fe92f185efe60e7dba166bea55f9472895658bf52cc6a97` |
| `localisation/english/012_africa_gods_l_english.yml` | `f81ea6a2059d54766f23c1a316d53525bdf5f73d5d7f6a7d0483695c7c77d2fb` |

## Limitations and follow-up ownership

Completed: actual diff review, call-site inventory, receipt/authority/ledger source traces, listed scenario verdicts and bounded localisation/sprite consumer review.
No source fix is requested from this review and no simplification or fallback was introduced.
Meaningful validation not performed here: engine-scoped script validation, MCP event inspect/render/compare, actual-source fixture execution, probability evaluate/compare and native event execution, all reserved by the parent prompt to their existing owners or excluded from this task.
Native unanswered cleanup is documentation-backed, not observed, and a regular host target's live persistence and display remain native evidence limits.
The parent must review this handoff and reconcile the specialist's pending comparison before making completion claims.
Finished cleanup `4eb9fdeaf`, the separate planner-owned phase proposal and parent-owned Council measured-receipt integration were not reopened.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`.
No skills were created or updated.
