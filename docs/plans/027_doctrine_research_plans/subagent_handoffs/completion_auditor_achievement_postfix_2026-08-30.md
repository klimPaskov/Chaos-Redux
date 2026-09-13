# Event 027 First Lesson achievement postfix audit

Date: 2026-08-30  
Mode: read-only source audit after the parent achievement patch

## Verdict

**First Lesson source check: PASS. The previously reported source defect is closed.**

`doctrine_research_achievement_first_lesson_check` now enforces the specification's missing condition: the consumed adoption must belong to a domain recorded as empty at the start of that same batch. This is source compliance, not acceptance completion; runtime achievement and native-doctrine evidence remains outstanding.

Audited live identities:

- `common/scripted_effects/027_doctrine_research_achievement_effects.txt`: SHA-256 `955d7c51c0a3105abb9abeb7a929f2ab2a23093a7c3909361d42fe3529f1abe1`.
- `common/scripted_triggers/027_doctrine_research_triggers.txt`: SHA-256 `11fbe721afeddbcf1df9f9f3ff7656aed22e8d1e12b11d2fd3660cd041330fc2`.

## Exact First Lesson compliance

The implementation at `common/scripted_effects/027_doctrine_research_achievement_effects.txt:10-77` now proves all source-level parts of the accepted route:

- the batch was human-started and contains at least two choices (`:24-25`);
- the first qualifying receipt is `choice_consumed`, is an adoption, and supplies the batch, domain, and choice number (`:28-41`);
- the adoption domain maps one-for-one to the matching batch-start snapshot at the same `doctrine_research_achievement_batch_index`: Army, Navy, Air, Special Forces, and Chaos Warfare (`:42-47`);
- the later mastery scan is entered only when that selected snapshot is positive (`:48-53`);
- the mastery receipt is consumed, belongs to the same batch and domain, has a strictly greater choice number, and leaves the branch above Mastery 0 (`:54-64`);
- only then is `doctrine_research_achievement_first_lesson` set (`:72-75`).

An invalid or unmapped adoption domain leaves `doctrine_research_first_lesson_domain_was_empty` at zero and fails closed. Native or external mastery cannot substitute for the required consumed Event 027 mastery receipt. No Event 027 debug or force receipt path was found that bypasses this check; the root achievement continues to use the project's ordinary achievement-registry contract at `common/achievements/chaos_redux_achievements.txt:4203-4206`.

The old finding in `completion_auditor_postfix_2026-08-30.md:159-165` is therefore superseded only for this defect.

## Array alignment, braces, and scope

The batch index assumption is supported by the ledger invariant:

- initialization creates all five snapshot arrays beside the batch arrays (`common/scripted_effects/027_doctrine_research_effects.txt:217-243`);
- each new batch appends its ID, human-start marker, and exactly one value to every snapshot array in one block (`:1755-1784`);
- `doctrine_research_country_state_is_aligned` requires every snapshot-array count to equal `doctrine_research_batch_ids^num` (`common/scripted_triggers/027_doctrine_research_triggers.txt:1027-1051`);
- normal batch start runs initialization and refuses corrupt state (`common/scripted_effects/027_doctrine_research_effects.txt:1789-1792`).

The achievement check relies on that established invariant rather than repeating the alignment trigger locally. This is safe for the normal call path; a pre-snapshot or externally damaged ledger is marked corrupt instead of being accepted. No migration backfill for already misaligned rows is assumed by this verdict.

The First Lesson block closes independently at line 77 with 59 opening and 59 closing braces. Both nested `for_loop_effect` indices are temporary variables, the inner loops do not change country scope, and the outer batch index remains available while reading the parallel arrays. No scoped temporary-variable misuse was found.

## Special Forces balance recheck

**Classification: PASS WITH DISCLOSED LIMITATION; unchanged.**

- With both Special Forces tracks occupied, the leading occupancy OR in both availability triggers is false, so neither ambiguous active track contributes a mastery action (`common/scripted_triggers/027_doctrine_research_triggers.txt:533-627`).
- With exactly one track occupied, active mastery is valid only for that occupied track while the other remains empty (`:1947-1958`).
- Empty-track candidates retain exact folder-index installation and all eight reused tokens retain `NOT = { has_doctrine = <token> }` duplicate prevention (`:2350-2388`, `:2802-2873`).
- Army, Navy, Air, and Chaos Warfare remain independent alternatives in `doctrine_research_country_has_valid_action` (`:966-974`).

The limitation remains that two occupied Special Forces tracks yield no Event 027 Special Forces mastery action, even if a branch is incomplete. This is the accepted fail-closed consequence of the missing native token-to-occupied-track identity, not a fallback or cross-domain substitution.

## Remaining acceptance blockers

These blockers are separate from the closed First Lesson source defect:

1. First Lesson still lacks accepted positive and negative runtime cases, including same-domain pass, cross-domain failure, native-only failure, cross-batch failure, batch-start-nonempty failure, and save/reload between choices.
2. Doctrine/technology inspect, render, and compare evidence remains blocked by `SCAN_BYTE_LIMIT`; low, middle, final, fractional, banked, empty-track, Special Forces, and native-completion behavior therefore remains unproven by the required engine route.
3. Receipt idempotency and achievement persistence still need interruption, duplicate confirmation, overlapping batch, annexation, controller/tag, and lifecycle traces.
4. Final achievement consumer evidence and the broader Event 027 event comparison, probability, presentation, and evolution-timing blockers recorded in `mcp_evidence.md` remain open.

No gameplay, localisation, asset, workbook, specification, or existing handoff file was edited. This new handoff is the only write from this audit.
