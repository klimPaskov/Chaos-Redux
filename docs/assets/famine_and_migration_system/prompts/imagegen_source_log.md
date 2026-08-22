# ImageGen source log

All listed masters were produced with the built-in ImageGen tool on 2026-08-22. Each call used a distinct asset-specific prompt, requested genuine transparent background in the initial call, and specified no generated text, no modern objects, no checkerboard, no matte, no halo, and centered small-scale readability. The resulting PNG was copied unchanged into the matching `source/` folder before processing.

Reference inspection was completed first against the canonical `vanilla_reference` root and its labeled contact sheets for decisions, decision categories, state modifiers, achievements, and category pictures. Reference PNGs were review-only and were not used as runtime art.

## Category icon

- `fm_cat_displacement`: railway ticket, shelter tag, and border post combined as one relief/migration emblem; native alpha source at `source/category/fm_cat_displacement.png`.

## State modifier icons

- `fm_state_supply_strain`: ration card and partly filled grain measure.
- `fm_state_acute_shortage`: emptying grain measure and damaged rail route.
- `fm_state_famine`: empty bowl, broken wheat, and obstructed rail.
- `fm_state_catastrophic_famine`: collapsed grain store and sealed route.
- `fm_state_exodus`: family bundles and road/rail movement.
- `fm_state_reception`: shelter, ration, and registration symbols.
- `fm_state_overcrowded`: crowded shelter and strained supply.
- `fm_state_trapped_border`: closed gate and civilian bundles on the origin side.
- `fm_state_return`: home, rail, and reconstruction.

## Decision icons

- `fm_dec_release_reserves`: opened ration-controlled grain sacks.
- `fm_dec_relief_convoy`: cargo ship, escort, and relief crate.
- `fm_dec_airlift`: transport aircraft lowering a relief crate.
- `fm_dec_evacuate`: period train and civilian suitcase.
- `fm_dec_open_border`: open gate and shelter lamp.
- `fm_dec_close_border`: closed gate and barrier.
- `fm_dec_quarantine`: shelter and medical inspection lamp.
- `fm_dec_distribute`: rail junction toward shelters.
- `fm_dec_integrate`: home, work hammer, and family token.
- `fm_dec_return`: homeward rail and repaired house.

## Achievement masters

- `famine_migration_break_the_blockade`: relief ship entering a damaged harbor beneath a broken blockade chain.
- `famine_migration_no_one_left_at_the_gate`: open border gate, shelter lantern, and civilian luggage.
- `famine_migration_roads_home`: families returning by rail toward repaired homes.
- `famine_migration_bread_across_the_front`: bread crate crossing a guarded bridge with symbolic relief markings.
- `famine_migration_hungry_not_contagious`: shelter, food bowl, and medical screening.
- `famine_migration_a_place_at_the_table`: shared table, travel tokens, and home symbol.
- `famine_migration_the_grain_stayed_home`: sealed grain store and non-readable requisition stamp.
- `famine_migration_the_country_did_not_empty`: generic repaired homes, rail, and grain emblem without a map outline.

Achievement `_grey` and `_not_eligible` states are deterministic derivatives, not additional ImageGen masters, as required by the achievement triplet workflow.
