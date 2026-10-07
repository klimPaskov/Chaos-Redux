# Executed model test report

Date: 2026-09-22. Python: `3.13.5`.

Command: `python -m unittest -v test_behavior_model.py`, executed from this directory.

**Result: 24 tests passed.** One test exercised 1,000 seeded abstract worlds using seed 880922. Other tests cover full Cartesian coverage, sparse and zero IDs, deduplication, ordinary/raised/lowered caps, preservation, separate owners, unsupported inputs, zero-change Chaos, one global award, legacy state, late countries, duplicate calls after an abstract clearance, and injected partial failure.

The exact unittest output is saved in `behavior_model_test_output.txt`. The executable model and tests are included so their assumptions can be inspected.

## What this proves

The Python model implements the intended additive arithmetic and once-only lifecycle consistently for its supplied abstract sets and integer fields. It catches attempts to supply an incomplete set relative to its provided oracle, preserves unrelated fields, rejects over-cap states before mutation, and retains partial writes without a blind retry after an injected failure.

## What it does not prove

The model receives eligible owners, valid naval regions, caps and counts as already-known inputs. It does not discover an HOI4 map or establish that equivalent native arrays and predicates exist. Its abstract removal helper is not actual minesweeping. Its copied state is not a native save/load test. It does not simulate hostility, damage, naval AI, decay, operation attribution or achievements.

No HOI4 code, MCP tool, live game, custom subagent, visual asset or workbook was tested by this harness. All engine acceptance rows remain NOT RUN.
