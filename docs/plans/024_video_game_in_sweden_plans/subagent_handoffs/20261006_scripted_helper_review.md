# Event 024 foreign-response helper review, 2026-10-06

## Recommendation

The proposed extraction is safe and behavior-preserving if the new trigger copies the five current `limit` bodies exactly and each caller remains in the answering country's country scope. Add the private predicate `video_game_in_sweden_can_answer_foreign_offer` to `common/scripted_triggers/024_video_game_in_sweden_triggers.txt`, then replace only the repeated condition with `video_game_in_sweden_can_answer_foreign_offer = yes` in the five resolver effects. No further abstraction is needed.

This recommendation is source review only. The parent owns the edits and current-source validation. The reported 33 source cases plus 6 lifetime cases are parent evidence and were not rerun by this reviewer.

## Proposed contract

**Scope:** Country scope of the foreign country that is answering its Event 24 `.40` popup.

**Inputs:** The answering country has `video_game_in_sweden_foreign_response_pending`; it exists and has not capitulated; it can resolve the global `video_game_in_sweden_host` target; the pointed-to host passes `video_game_in_sweden_is_current_host`; and the answering country is not at war with the host.

**Outputs:** Boolean trigger result only. It writes no flags or variables, emits no events, clears no targets, and changes no costs, weights, payouts, or availability.

**Callers:** `video_game_in_sweden_resolve_foreign_copy`, `..._study`, `..._ban`, `..._ridicule`, and `..._no_action` in `common/scripted_effects/024_video_game_in_sweden_effects.txt`.

## Scope and lifetime evidence

The repeated preconditions are identical at `common/scripted_effects/024_video_game_in_sweden_effects.txt:3897-3906`, `:3936-3945`, `:3974-3983`, `:4014-4023`, and `:4054-4063`. They execute in the event recipient's scope because each option in `events/024_hearts_of_iron.txt:1147-1202` calls its resolver from the foreign recipient's `.40` response event.

`video_game_in_sweden_is_current_host` at `common/scripted_triggers/024_video_game_in_sweden_triggers.txt` compares `tag = PREV` inside its own target-country block.
The foreign predicate first enters the saved Swedish host from the responder, so PREV at that outer entry is the responder.
It then invokes the current-host trigger in Sweden, and that trigger enters the saved host again, so PREV at the identity comparison is the calling Swedish country.
The comparison confirms that the saved host is that Swedish caller.
The private trigger adds no scope transition, so extraction preserves both target entries, ROOT, and these PREV relationships.
Parent acceptance: the exact predicate extraction is implemented after this review, and the 33-case suite passes against the extracted trigger.
The earlier reviewer phrase equating the innermost PREV with the foreign responder is corrected here by tracing both entries.


False results preserve the existing `else` behavior in every resolver: clear this country's pending-response flag and invoke `video_game_in_sweden_clear_answering_partner`, which only removes the global partner pointer if it still names the answering country. This retains stale/released partner handling and cannot clear a newer partner's pointer. True results continue through the existing outcome-specific consequences, summary count, and guarded pointer cleanup.

A focused equivalence fixture should assert all five call sites use the shared trigger and that its body equals the previous guard. Scenarios to retain are: pending living responder with current peaceful host passes; missing pending flag fails; dead/capitulated responder fails; missing host target fails; closed, invalid, replaced, or wrong-identity host fails through the current-host predicate; war with the host fails; and a late answer after maintenance released its pointer fails without applying the outcome or clearing a newer pointer.

## Probability boundary

This predicate controls response validity only. It contains no `ai_chance`, `random_list`, MTTH, AI factor, cost, or weighted-pool expression, so the helper extraction itself does not alter any probability surface. Because the edited scripted-effects file also contains weighted incident code, the parent should keep the requested incident-pool frozen-source comparison separate: prove the helper-only diff and caller equivalence, then interpret the 715-pool comparison as evidence for the incident-weight surface. Do not use this architectural review as numeric probability clearance.

No generic shared dynamic effect is warranted. The five call sites are one Event 024 private predicate, and the repository's dynamic-helper documentation requirement applies to new reusable dynamic effects, not this scoped scripted trigger.
