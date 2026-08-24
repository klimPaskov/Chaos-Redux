# Event 006 research CSV schema repair

Date: 2026-08-24

Owner: `/root`

## Scope

This bounded documentation repair restores valid CSV column alignment in the two accepted Event 006 research tables identified by the completion audit.

## Files changed

- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`

The package table had 46 rows with an unquoted comma inside the leadership-resolution field. Those rows were repaired without changing their text or package disposition. The repaired IDs are IW-055, IW-056, IW-060, IW-066, IW-079, IW-080, IW-082, IW-088, IW-091, IW-092, IW-115, IW-118, IW-120, IW-127, IW-128, IW-129, IW-133, IW-134, IW-135, IW-137, IW-138, IW-139, IW-146, IW-153, IW-157, IW-160, IW-163, IW-164, IW-168, IW-172, IW-174, IW-178, IW-186, IW-187, IW-188, IW-189, IW-190, IW-191, IW-193, IW-195, IW-198, IW-199, IW-200, IW-202, IW-205, and IW-206.

The reservation table had one unquoted comma inside the RG-RHINE-SAAR host-survival rule. That field is now quoted and the row remains a nine-column record.

## Validation

Python's CSV parser now reads all 206 package rows as 16-column records and all 111 reservation-group rows as nine-column records. The source IDs, package dispositions, reservation capacities, and wording were not otherwise changed.

This repair does not promote a package, change the 32/29/40/161 implementation boundary, alter the exact 3/4/5/7/10 ladder, or widen any runtime admission gate.

## Remaining limits

Research schema validity does not prove identity, rights, portrait, flag, map, typed-probability, package-admission, or live transaction completion. Event 006 remains HOLD / PARTIAL.
