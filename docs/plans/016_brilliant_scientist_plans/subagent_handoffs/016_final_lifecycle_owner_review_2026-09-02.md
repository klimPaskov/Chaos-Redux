# Event 016 lifecycle closure owner review

## Boundary and authority

This is a bounded correction tranche under the accepted final completion contract, not an Event 016 completion claim.
The retained pre-change source is commit `e7307e228e2b4bda3309672e8077ac9889c7bb36`.
This tranche adds no project family, evolution, country, focus, public value, GUI, super-event, achievement, or model.
The unapproved alternative Portal landing design is outside this tranche.

## Finding disposition

| Finding | Owner implementation | Review state |
| --- | --- | --- |
| F1, invalid transfer cancels expedition | Initialize the result, validate all inputs, acquire the transaction lock, then cancel the expedition inside the valid branch and reassert locks closed by nested restoration. | Accepted by bounded postimplementation source review. |
| F2, pending report family aliases history iterator | Dedicated pending-family snapshot, separate from the existing array-copy iterator. | Accepted by bounded postimplementation source review. |
| F3, permanent departure strands host reactions | Run pending country/character cleanup before removing Kruger's roles. | Accepted by bounded postimplementation source review. |
| F4, sovereignty retains or reschedules host reactions | Clear former-host pending state after the split snapshot, use pending-only cleanup for same-tag takeover, and exclude sovereign carriers from all three scheduling and delayed-event gates. | Accepted by bounded postimplementation source review. |
| F5, death and split sovereignty retain foreign frameworks | Close live bilateral partner/site pointers after the split snapshot or before confirmed retirement, retaining permanent history and regular operation settlement targets. | Accepted by bounded postimplementation source review. |
| F6, disabled lower stages receive evolved-opening state | Independently gate each base, seed, delivery, and policy package against its own evolution context. | Accepted by bounded postimplementation source review. |

The earlier suggestion to call the full `brilliant_scientist_clear_host_reaction_state_after_sovereignty` helper for same-tag takeover is superseded.
That helper clears resolved host-policy fields, including the patent-pool accident-pressure consumer and three history arrays.
Same-tag takeover keeps those earned consequences and uses `brilliant_scientist_clear_host_reaction_state_on_terminal_exit` for pending state only.
Scheduler and delayed-event sovereign exclusions also prevent later rescheduling without inventing a resolved receipt.
The new fixed-tag KRG carrier retains its existing sovereign initialization behavior.

The postimplementation reviewer found R1 during the first patch: nested D'Rhondan restoration unconditionally releases both character transaction locks.
The transfer reasserts both locks after cancellation and before snapshots or nationality changes.
The reviewer rechecked this correction before accepting the bounded source patch.
See `016_final_lifecycle_postimplementation_review_2026-09-02.md` for exact final source hashes and scenario traces.

## Source scenarios and scope evidence

- An invalid or missing transfer recipient cannot reach expedition cancellation, nationality changes, or host cleanup.
- A valid transfer carrying active report family A alongside historical families B and C restores family A and its saved stage without the history iterator overwriting it.
- A transfer without an active report leaves the pending-report result false and queues no report.
- Permanent departure clears all three country and character pending reaction kinds while preserving resolved history.
- Same-tag takeover preserves the resolved patent-pool benefit and family history, while queued and future host-only reactions are excluded.
- Split formation completes its selected state transfers and saves its portfolio before ending live joint-laboratory or protection relationships.
- Capital binding uses the frozen formation-capital target, and secondary binding uses a separate secondary-facility target, so foreign relationship cleanup does not invalidate either binding.
- Confirmed-death cleanup does not clear the regular `brilliant_scientist_foreign_operation_actor` or `brilliant_scientist_foreign_operation_host` targets used by final operation settlement.

These are source-control-flow assertions, not game execution evidence.
Vanilla documents `for_each_loop.value` as a temporary iterator, regular event targets as chain-local, and `retire_character` as removing the character and all its roles.
The nationality-transfer precedent is `events/NSB_Poland.txt`, where transfer is followed by verified character presence.

## MCP evidence and open gates

The pre-patch full `state_flow` call for `mod:common/scripted_effects/016_brilliant_scientist_effects.txt` returned `INTERNAL_ERROR`, message `Unexpected internal error`, with no artifacts or scanned files.
It provides no lifecycle coverage.

A narrow `.7` trace and the host-reaction file render succeeded with partial focused coverage at revision `23d07f38466bd55877a4f79f36a99c34bb9b7f0790f582a264bb307cc60e4646`, graph hash `38c248ff95d2c1efe04ff3c5a340f4af0f65f201989d8a235d0aec2d3c68519f`.
The focused graph indexes zero helpers and therefore cannot validate the cleanup-effect implementations.
The file render selects 21 nodes and has layout hash `91b0291e913b9ad74640b2b98ffc7ea71f02086cd9c303a4099d0b6bd2dc72d8`.

- Trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6d20814766c9a3fb157256f1b73b01b7854b77301c3a2cb8f5ee38164038dfb/664521ea3980cd97d5e538890103ca7107ff63a4ab6e628289ffbfbbb21ac72c/event-trace-23d07f38466b.json`
- Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e944344cb9923802b02e49c80928f455e319373ef0e1f8b62dfeaa248883354f/2ac87a4a3f52858260b7b0c7a43615c8470e592f131042575c1d0fbf2fddebb6/event-options-23d07f38466b-manifest.json`

A retry for the atomic-transfer helper succeeded in full mode at revision `741b7f43b88ac9871ece09fb4cff3d13de80c2523f23ecee7b3ac685feed49a7`, graph hash `387950083a8524380970e50c35000d07a7870d4ade12065fa68ebb840676246e`, with 18,859 indexed helpers.
This intermediate snapshot predates the final evolution/sovereignty gates and nested-lock correction.
The requested temporary-variable flow returned zero accesses, producers, consumers, and clears, so it does not validate the pending-family snapshot.
Its 15 report issues and 3,950 workspace-wide blocking diagnostics remain unresolved engine-analysis evidence, not a count of proven Event 016 defects.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1edde66bf38639dd1b571ab6a6d57573c69375ac2b69f885554cf3617423d9b3/52c335611848cac2b78deb2c2682b24cc194c180e08eb25b6875de884133ab16/event-state_flow-741b7f43b88a.json`.

The subsequent cached comparison returned `EVENT_REVISION_NOT_CACHED` with no artifacts.
A seven-file source-overlay comparison, using the retained commit's source without modifying working files, was also attempted in the explicitly reversed direction of current source to original source.
It timed out with `timed out awaiting tools/call after 180s` and produced no returned comparison evidence.
Neither attempt is a passed comparison, and no reverse-comparison result was fabricated or relabeled as forward validation.
The final manifest render for `.7/.8/.9/.21/.22/.23/.24` also timed out after 180 seconds, so the earlier partial render is not presented as final-source evidence.

The probability specialist completed source-backed comparisons of all four evolution option pools and the host-reaction option pool under the retained named scenarios.
Every returned comparison reported zero option-level changes; helper eligibility remains unresolved, so these partial results neither prove exact normalized probabilities nor exercise the new event-root or lifecycle guards.
See `016_final_evolution_probability_2026-09-02.md` for scenario IDs, source hashes, artifacts, fixture limitations, and unresolved inputs.
No AI weight or MTTH value is changed by this correction tranche.
Source snapshots remain recoverable from the retained commit rather than only from hashes or analysis IDs.
Full final-source event helper coverage and source-matched MCP comparisons remain open.
The bounded source specialist review is accepted and recorded separately from those MCP gates.

The MTTH and evolution-mission files have no semantic diff from the retained commit under `git diff --ignore-space-at-eol`.
Their byte hashes may differ through line endings, and that difference is not a balance change by this tranche.

## Remaining work and exclusions

This correction does not certify all project payoffs, foreign-operation balance, containment costs, DHR or KRG route quality, terminal paths, GUI layout, models, audio, assets, or catalog alignment.
The containment documentation's multi-resource cost table also needs reconciliation against the decision skill's four-cost limit during the remaining Directorate decision review.
No new fallback or substitute asset was introduced.
No game was launched, and no logs or user-run tests were requested.

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-mtth`.
They require preserving lifecycle ownership, validating each evolution independently, retaining exact comparison sources, and distinguishing source reasoning from MCP evidence.
