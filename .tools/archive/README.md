# Archived Chaos Redux tools

This directory preserves retired or event-specific scripts that no longer belong to the supported shared toolchain.

Archived scripts are read-only historical source. They may contain stale paths, assumptions, identifiers, package counts, or validation contracts. Do not run them as current acceptance checks and do not cite an old passing result as current evidence.

The archived set contains:

- `audit_hoi4_country_tags.py`, the former broad installed country-tag scanner;
- `audit_chaosx_country_tags.py`, the former Event 006 and Soviet Collapse namespace scanner;
- `generate_chaosx_building_positions.py`, the former one-off shared `map/buildings.txt` override generator;
- `generate_formable_state_geometry_registry.py`, the former active-map geometry producer;
- `build_formable_state_registry.py`, the former universal state-index and trigger builder;
- `build_formable_state_puzzle_consumer.py`, the former per-consumer asset and manifest compiler.

The supported Event 006 validators live only at the `.tools/` root, and the parent README documents them. Do not keep a second copy here: an archived duplicate drifts against the live source contracts that the maintained validator reads, and a stale copy that still runs is more misleading than one that has been removed.

If one of these checks becomes useful again, review it against the current repository and required HOI4 MCP workflow first. Promote a repaired, reusable validator back to the supported `.tools/` surface only when it protects a current cross-system contract and is documented in the parent README.
