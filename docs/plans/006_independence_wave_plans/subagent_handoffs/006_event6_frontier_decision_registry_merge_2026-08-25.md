# Event 006 frontier decision registry merge

Date: 2026-08-25.

## Scope

The package-owned IW-060 Kurdistan and admitted IW-040 Kuban decision files were independent parser surfaces with unique category, decision, and file-scoped constant namespaces. They now live in `common/decisions/006_independence_wave_frontier_decisions.txt` under explicit source markers.

## Source-equivalence receipt

- The receiver preserves both package constants: `CR_SC_INDEPENDENCE_WAVE_KUR_CIVILIAN_FACTORY_USE = 1` and `CR_SC_INDEPENDENCE_WAVE_KUB_CIVILIAN_FACTORY_USE = 1`.
- It preserves two category roots and 23 unique decision identifiers, with balanced braces at 503 opening and 503 closing braces.
- Each source category and decision body matches its marked receiver section after line-ending normalization and comment-only banner compaction.
- No decision key, cost, timer, trigger, effect, cancellation, cleanup, AI block, or package gate was changed.

## Boundaries

This is a source-layout consolidation only. It does not promote IW-060, alter IW-040 admission, change the deterministic Join order, widen package adapters, or claim live parser, probability, tooltip, or runtime evidence. FER remains separate because its decision file was an active lifecycle-repair surface, and Kosovo remains separate during its owned working-tree repair.

## Validation

The pre-merge bodies were read from the parent commit snapshots `git show HEAD^:<source>` before the old parser paths were removed. A focused receipt confirms executable-body parity, 23 unique decisions, two category roots, preserved constants, and balanced braces. The maintained Event 006 allocator, scenario matrix, and country-API validators remain the required post-merge checks.
