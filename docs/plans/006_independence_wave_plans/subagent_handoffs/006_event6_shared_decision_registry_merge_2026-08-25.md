# Event 006 shared decision registry merge

Date: 2026-08-25

## Scope and disposition

This source-only pass removes two small Event 006 decision parser files and replaces them with one shared registry:

- `common/decisions/006_independence_wave_shared_decisions.txt`

The receiver contains the complete contents of:

- `common/decisions/006_independence_wave_evolution_incident_decisions.txt`
- `common/decisions/006_independence_wave_rival_bloc_decisions.txt`

The two source files were removed after their full bodies were copied as complete units. No package-local decision file, category file, cost helper, trigger, effect, localisation key, AI weight, admission gate, or event file was changed.

## Preserved surface

The receiver contains two category identifiers and fourteen direct decision identifiers:

- Evolution category: `independence_wave_evolution_incident_category` with five incident decisions.
- Rival-bloc category: `independence_wave_rival_bloc_category` with nine decisions.

The category blocks, decision identifiers, costs, timers, custom-cost triggers/text, availability and cancellation triggers, completion/remove/cancel/timeout effects, and AI blocks are unchanged. The rival-bloc block is separated only by a source comment; comments are parser-neutral.

## Equivalence checks

- Normalized source comparison confirms the complete pre-merge evolution file is present in the receiver.
- Normalized source comparison confirms the complete pre-merge rival-bloc file is present in the receiver.
- The receiver has two top-level category blocks and fourteen direct decision blocks.
- No decision identifiers were renamed or duplicated by the merge.
- The merged file is 24,491 normalized bytes; the source files were 10,828 and 13,446 bytes before line-ending normalization.

This is parser-layout evidence only. It does not prove live decision loading, AI probability completeness, or runtime lifecycle behavior; the current Event 006 probability and live-MCP status remain documented as incomplete/HOLD.

## Deliberate boundaries

Country history shells, package-owned decisions, the shared Event 006 decision registry, FORM registries, minor-overlay registries, GUI surfaces, and on-action files remain separate. These surfaces either encode ownership or share engine callback/category contracts that were not part of this bounded merge.

## Validation

The maintained Event 006 static audits remain the relevant follow-up checks. No live Hearts of Iron IV session was launched, and no completion claim is made for the whole Event 006 package.
