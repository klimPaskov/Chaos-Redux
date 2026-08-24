# Event 006 AI and constant registry consolidation

## Scope

This source-layout pass consolidates the 38 Event 006 package AI strategy files into `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` and the 65 Event 006 package constant files into `common/script_constants/006_independence_wave_constants_registry.txt`.

Each surviving registry contains a compact source marker for every former filename. The executable definitions remain in their original order and retain their original identifiers, values, gates, and ownership. No country shell, decision, on-action, scripted-effect, scripted-trigger, focus, or localisation surface was merged by this pass.

## Preservation evidence

The normalized executable-definition SHA-256 for the AI strategy content is `0f12e466a3bde262ca82741abd79ae11d60ea2d9db27b63cdafa11761f4b321b` before and after consolidation.

The normalized executable-definition SHA-256 for the script-constant content is `3819be70364749a37a4ca210595b28531ea70089e2b394b9ea2dd98db8268f75` before and after consolidation.

The AI registry has balanced braces and 637 unique top-level definitions. The constants registry has balanced braces and 377 unique top-level definitions. No duplicate top-level identifiers were found in either source family. File-scoped AI `@` constants remain in the same executable file as the strategy rows that consume them, so the merge does not introduce cross-file constant visibility assumptions.

## Size result

The 38 AI files totalled 193,918 committed source bytes and the compact registry is 190,728 bytes, saving 3,190 bytes. The 65 constant files totalled 226,844 committed source bytes and the compact registry is 196,155 bytes, saving 30,689 bytes. The pass removes 101 old files and saves 33,879 source bytes.

## Documentation synchronization

Current Event 006 event documentation and the source-of-truth map now point to the two registries. Historical handoffs remain unchanged as dated evidence. The 87 country shells remain separate because their filenames are country identity boundaries. On-actions remain separate because callback composition and duplicate engine keys require explicit ownership review. Decisions, scripted effects, scripted triggers, focus trees, and scripted localisation remain separate because their block and ownership boundaries have not been audited for safe composition.

## Validation boundary

This is a source-layout change only. It does not claim live AI selection, probability, event, tooltip, or in-game acceptance. Existing Event 006 allocator, country API, flag-family, scenario-matrix, focus, decision, and probability evidence remains authoritative and the whole event remains HOLD / PARTIAL.
