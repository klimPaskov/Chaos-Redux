# Air Cleanliness documentation

This directory documents shared air contamination, atmospheric recovery, natural-source pressure, Air Winter, treaty behavior, and fallout-facing integration.

## Navigation

- [`air_contamination_mechanic.md`](air_contamination_mechanic.md) is the main Air Cleanliness mechanic contract.
- [`contamination_source_ledger.md`](contamination_source_ledger.md) defines source registration and contribution accounting.
- [`natural_sources.md`](natural_sources.md) defines wildfire, volcanic, ash, and other natural contamination sources.
- [`winter.md`](winter.md) defines the Air Winter pressure and mitigation model.
- [`air_cleanliness_treaty.md`](air_cleanliness_treaty.md) defines the treaty lifecycle and its current implementation boundary.
- [`fallout_generic_focus_tree.md`](fallout_generic_focus_tree.md) documents the generic fallout-survivor focus tree that consumes the shared atmospheric state.

Chemical and biological delivery mechanics belong in `../cbrn_warfare/`. Chaos gains and death accounting belong in `../chaos_meter/`.
