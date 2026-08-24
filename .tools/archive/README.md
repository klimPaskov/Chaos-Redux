# Archived Chaos Redux tools

This directory preserves retired or event-specific scripts that no longer belong to the supported shared toolchain.

Archived scripts are read-only historical source. They may contain stale paths, assumptions, identifiers, package counts, or validation contracts. Do not run them as current acceptance checks and do not cite an old passing result as current evidence.

The archived set contains:

- `audit_hoi4_country_tags.py`, the former broad installed country-tag scanner;
- `audit_chaosx_country_tags.py`, the former Event 006 and Soviet Collapse namespace scanner;
- `audit_event6_allocator.py` (historical copy; the maintained validator is now `.tools/audit_event6_allocator.py`);
- `audit_event6_country_api.py` (historical copy; the maintained validator is now `.tools/audit_event6_country_api.py`);
- `audit_event6_flags.py` (historical copy; the maintained validator is now `.tools/audit_event6_flags.py`);
- `audit_event6_form16.py` (historical copy; the maintained validator is now `.tools/audit_event6_form16.py`);
- `audit_event6_gui_matrix.py` (historical copy; the maintained validator is now `.tools/audit_event6_gui_matrix.py`);
- `audit_event6_scenario_matrix.py` (historical copy; the maintained validator is now `.tools/audit_event6_scenario_matrix.py`);
- `generate_chaosx_building_positions.py`, the former one-off shared `map/buildings.txt` override generator;
- `generate_formable_state_geometry_registry.py`, the former active-map geometry producer;
- `build_formable_state_registry.py`, the former universal state-index and trigger builder;
- `build_formable_state_puzzle_consumer.py`, the former per-consumer asset and manifest compiler.

If one of these checks becomes useful again, review it against the current repository and required HOI4 MCP workflow first. Promote a repaired, reusable validator back to the supported `.tools/` surface only when it protects a current cross-system contract and is documented in the parent README.
