# Event 006 Balkan decision registry merge — 2026-08-25

## Scope and outcome

Five clean Balkan package decision files are consolidated into `common/decisions/006_independence_wave_balkan_decisions.txt`:

- Banat / IW-024
- Bosnia / IW-029
- Epirus / IW-028
- Macedonia / IW-026
- Thrace / IW-027

Each source contributed one disjoint category and twelve disjoint decisions. The receiver keeps every package-local constant, category key, decision identifier, cost, trigger, effect, timeout, cancellation, cleanup, and AI block under a source marker. Montenegro and Transylvania remain separate because both use the same pre-existing file-scoped `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_*` names; merging them would create a constant collision or require an identifier rewrite.

## Validation

- Receiver is UTF-8 with BOM and has five source markers.
- The merged file has five unique categories, 60 unique decision definitions, and ten unique package-local constants.
- Braces are balanced (`1081` opening and `1081` closing braces).
- Each of the five former source files' complete executable body, beginning with its constants or category assignment, is present unchanged in the receiver. Only redundant leading banner comments were removed.
- The five former files total 96,656 bytes; the compact receiver is 96,338 bytes, saving 318 source bytes while removing five parser files.
- Current package notes for Banat, Bosnia, and Macedonia now point to the registry source blocks. No package trigger/effect, focus, localisation, AI, admission, or runtime behavior changed.
- No live decision parser, GUI, or save/load receipt is claimed.

## Boundary

This is a source-layout consolidation only. The Balkan packages remain in their existing admission state, and Montenegro/Transylvania remain separate until their constant namespace can be changed under an explicit gameplay-neutral ownership decision.
