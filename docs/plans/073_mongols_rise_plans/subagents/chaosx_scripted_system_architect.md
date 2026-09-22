# Accountable campaign architecture

Role: `chaosx_scripted_system_architect`.

Execution status in this package: NOT EXECUTED.

## Context

Event 073 Mongols Rise restores a cavalry empire with rapid conquest, persistent defensive weakness, three political routes, four regional khanate identities, accountable tribute, Karakorum, connected routes, three Evolutions, succession, collapse and recovery. The main specification is under `docs/specs/073_mongols_rise_specs/`. Plans and evidence are under `docs/plans/073_mongols_rise_plans/`.

## Required reading

The event skill, mechanics, dynamic effects and triggers, lifecycle and Chaos handoffs. Follow the current installed profile’s reading limits and referenced-file requirements. Record unavailable files explicitly. Do not treat a search snippet or a truncated response as a full read.

## Assigned work

Review actor ownership, fire-once commitment, cumulative grants, fixed occurrence scaling, active upgrade deltas, payment transactions, campaign records, succession, successor survival, and bounded scheduling. Identify every place a retry or save reload could duplicate a consequence.

## Ownership

Architecture and review within assigned event-owned systems. Shared changes require parent approval. Use a fresh role context and `fork_turns="none"` when the actual interface supports it. The parent owns shared integration and the disposition of proposals. If this is still a planning-only task, make no gameplay edits.

## Return contract

Return a concise dependency map, source-backed mechanisms, overlap risks, and tests that prove each transaction is idempotent.

Separate source-derived facts, authored proposals, verified implementation, and blocked work. Include actual paths and evidence for completion claims. Do not claim another role ran, a render passed, a model was generated, a recording was licensed, or a game test succeeded unless that action actually occurred.
