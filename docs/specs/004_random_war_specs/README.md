# Event 004 Random War specifications

The design source is [`004_random_war_spec.md`](004_random_war_spec.md).
Current implementation documentation is in [`docs/events/004_random_war/overview.md`](../../events/004_random_war/overview.md).
The [2026-10-06 release reconciliation](../../plans/004_random_war_plans/release_qa_completion_20261006.md) distinguishes accepted bounded repairs from broader proposals and unresolved release evidence.

## Changelog

### 2026-10-10 spec audit

Consistency pass: the selection rule, pairing model, evolution table, baseline option packages and asset section now describe the implemented ladder, constants, costs and sprites instead of older ranges and placeholder asset names.
The aggressor and target weight wish-lists became one explicitly proposed weighted-selection section, the duplicated pacing list was reduced to the actual cooldown contract, and three spec-to-source mismatches were recorded for the implementation owner: special Chaos Redux countries can be drawn by the ordinary rungs below their stage gate, protected scripted actors are not excluded, and the cooldowns are flat despite the stated loosening at higher evolutions.

Design pass: a Shared system connections section records that war displacement, food assessment, casualties and chaos already arrive through the hostile-capture adapter and the daily casualty update, so the event must not add duplicate famine, migration, deaths or chaos calls, and that a Random War quarrel is an ordinary Event 009 White Peace candidate.
Weighted pair selection, per-stage cooldowns and protected-actor exclusion are recorded under Open questions as proposals.

