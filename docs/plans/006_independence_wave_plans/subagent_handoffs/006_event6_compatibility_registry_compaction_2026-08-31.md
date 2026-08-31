# Event 006 compatibility registry compaction — 2026-08-31

## Disposition

Completed a source-layout-only consolidation of two small Event 006 runtime files. The compatibility effect definitions from `common/scripted_effects/006_independence_wave_compatibility_effects.txt` now live under a marked section in `common/scripted_effects/006_independence_wave_effects.txt`, and the compatibility trigger definitions from `common/scripted_triggers/006_independence_wave_compatibility_triggers.txt` now live under a marked section in `common/scripted_triggers/006_independence_wave_triggers.txt`.

The two former parser files were removed. All moved identifiers and executable blocks are source-equivalent after whitespace normalization. No package admission, allocator weight, reservation, release, ladder, cost, decision category, event, AI, localization, asset, formable, or pre-event behavior changed.

## Scope and verification

- Moved 33 compatibility effect definitions, including the retired no-op crisis stubs.
- Moved 66 compatibility trigger definitions, including retired crisis guards and vanilla formable shortcut guards.
- Confirmed every moved top-level identifier appears exactly once in its canonical receiver.
- Compared every moved executable block against its former file; all blocks match after whitespace normalization.
- No active source reference depended on either former filename; remaining references are historical documentation labels only.
- Updated `.tools/audit_event6_allocator.py` to audit the canonical trigger/effect receivers after the move; its retired-crisis checks still pass.
- The absolute no-pre-event contract remains unchanged: the retired crisis identifiers stay inert and no category, mission, cost, queue, pressure, or early request is introduced.

## Files changed

- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `.tools/audit_event6_allocator.py`
- Removed `common/scripted_effects/006_independence_wave_compatibility_effects.txt`
- Removed `common/scripted_triggers/006_independence_wave_compatibility_triggers.txt`

This is a parser-surface reduction only. The current Event 006 boundary, static validator evidence, and MCP/live-runtime limitations are unchanged.
