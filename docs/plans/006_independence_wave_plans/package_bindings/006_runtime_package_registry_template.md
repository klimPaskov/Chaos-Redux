# Event 006 runtime package registry template

## Authority

Runtime package rows reconcile these accepted sources:

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv`
- installed country tags and state history

Working names are never copied into player-facing localisation by this layer.

## Per-package contract

Every enabled, current-map-bound row has:

1. a static `can_plan_independence_wave_package_iw_NNN` trigger that checks the open transaction, remaining Event 6 slot, package and reservation-group uniqueness, absent/valid target tag, and available unique anchor;
2. a loader that resolves the tag, anchor, current primary host, package ID, reservation group, region, depth, economic archetype, pool disposition, and registered-tag status;
3. an automatic weight preparer when the disposition is automatic or high-chaos;
4. an exact reservation publisher that reserves the unique anchor first, then compact states, then extended states;
5. inclusion in its regional random list only when automatic selection is allowed.

Scenario-only packages retain their trigger, loader, and reservation publisher but receive no automatic weight. Route-only and community-specific rows are not silently promoted into the automatic pool. Disabled or unbound rows receive no runtime publisher until the missing research or unique current-map anchor is resolved.

## Territory rules

- For `fixed_anchor_compact`, the first installed anchor ID is the single coordinator anchor and additional IDs in `anchor_state_ids` are compact territory.
- For `choose_one_ordered`, the first currently viable state becomes the single coordinator anchor; later IDs are alternatives, never cumulative territory.
- The anchor is not published a second time when it also appears in `compact_state_ids`.
- Compact and extended reservations are optional and are trimmed when occupied by another package, protected for a host, or beyond the host's remaining loss capacity.
- A failed anchor rolls back the whole candidate and leaves the selection loop to reroll.
- Static state IDs express accepted package identity; runtime owners determine the actual hosts.

## Weight rules

Weights are recomputed before every draw. They use registered-tag readiness, current-wave region and host novelty, prior-wave package/region/host memory, signature depth at low chaos, and high-chaos eligibility. Regional totals are the sum of viable package weights, so the two-stage regional draw remains mathematically equivalent to one global weighted list.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt` owns the aggregate draw. It retries rejected candidates up to the full registry attempt ceiling and marks the Event 6 plan contribution invalid if it cannot freeze the exact chaos-band count. A short pool never reduces the wave count and never reaches ownership execution.

## Archetype resolution

The seven economic archetypes are assigned by reading the row's opening archetype, force archetype, territory, economy, and signature direction together. Keyword-only bulk mapping is not accepted. Ambiguous assignments are recorded for parent review instead of being guessed silently.

## Current implementation slices

- Region 01: `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt` and `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt`
- Region 02: `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt` and `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt`
- Region 03: `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt` and `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt`
- Region 04: `common/scripted_triggers/006_independence_wave_packages_region_04_triggers.txt` and `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt`
- Region 05: `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt` and `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt`

Remaining regions must use separate numbered files so bounded implementation and review do not overlap.
