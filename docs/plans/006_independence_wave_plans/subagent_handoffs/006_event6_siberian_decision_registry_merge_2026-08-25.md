# Event 006 Siberian decision registry merge — 2026-08-25

## Scope and outcome

The four clean Siberian package decision files are consolidated into `common/decisions/006_independence_wave_siberian_decisions.txt`:

- Altai / IW-053
- Buryatia / IW-052
- Khakassia / IW-054
- Sakha / IW-051

Each source contributed one disjoint category, eleven decisions, and one package-specific civilian-factory constant. The receiver keeps all constants, category keys, decision identifiers, costs, triggers, effects, timers, cancellation, cleanup, and AI blocks under source markers.

## Validation

- Receiver is UTF-8 with BOM and has four source markers.
- The merged file has four unique categories, 44 unique decision definitions, and four unique package constants.
- Braces are balanced (`993` opening and `993` closing braces).
- Each former source file's complete executable body, beginning with its constant or category assignment, is present unchanged in the receiver; only redundant leading banner comments were removed.
- The four former files total 93,781 bytes; the compact receiver is 93,606 bytes, saving 175 source bytes while removing four parser files.
- Current Altai and Sakha package notes now point to the registry source blocks. No package trigger/effect, focus, localisation, AI, admission, or runtime behavior changed.
- No live decision parser, GUI, or save/load receipt is claimed.

## Boundary

This is a source-layout consolidation only. The Siberian packages remain in their existing admission state and no decision identifiers or cost namespaces were renamed.
