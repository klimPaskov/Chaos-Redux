# Event 006 IW-017 through IW-019 Allocator Admission Audit

**Date:** 2026-07-16
**Mode:** Read-only gameplay audit
**Verdict:** **READY**

The current admission of IW-017 Corsica, IW-018 Sardinia, and IW-019 Sicily is consistent across package identity, automatic planning, runtime execution preflight, scenario preflight, Liberations-cluster capacity, Event 5 collision guards, and SCN-008 ranked allocation.

No gameplay file was edited by this audit. This report is the only file created.

## Audited identities

| Package | Country | Anchor | Baseline host | Reservation group | Earliest automatic band |
|---|---|---:|---|---|---:|
| IW-017 | `COR` Corsica | 1 | `FRA` | `rg_1` | 0, Calm World |
| IW-018 | `ARX` Sardinia | 114 | `ITA` | `rg_114` | 1, Gathering Storm |
| IW-019 | `ASX` Sicily | 115 | `ITA` | `rg_115` | 1, Gathering Storm |

The installed-map binding ledger records `1=FRA`, `114=ITA`, and `115=ITA`. The vanilla state sources agree. State 1 is owned by France and has COR and FRA cores. States 114 and 115 are owned by Italy, with no Event 5 opening-republic core on any of the three anchors. Runtime planning correctly records the live owner of each anchor as the primary host, so later map changes do not force the 1936 host.

## Identity and absence contract

`006_independence_wave_package_triggers.txt` now contains exact dormant-tag triggers for all three packages:

- IW-017 requires `original_tag = COR`.
- IW-018 requires `original_tag = ARX`.
- IW-019 requires `original_tag = ASX`.

Each exact trigger calls `is_independence_wave_candidate_origin_available`. That shared proof requires the country not to exist, not to be reserved by the current liberation plan, not to carry a rejection for the same plan, not to be an Event 5 active origin, not to have the Soviet-collapse liberation origin, and not to be an active Event 6 origin.

Anchor availability independently requires a live owner that controls the anchor, a controller that is not an Event 5 active origin, and no current reservation or protected-state mark.

Region 02 planning now uses these exact immutable tag checks rather than the legacy dormant-history content flag. The package, reservation-group, and anchor checks are exact for each row.

## Runtime adapter and attestation sets

The following admitted package set is identical in the runtime adapter registry and compile-time content-attestation registry:

`IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-017, IW-018, IW-019`

That is exactly 11 admitted IDs.

The runtime preflight also contains exact ID and original-tag pairs for all 11. For the Mediterranean tranche they are IW-017/COR, IW-018/ARX, and IW-019/ASX. It additionally rechecks absence and rejects Event 5 or already-active Event 6 origins.

The scenario preflight contains the same exact 11 ID/tag branches through the immutable tag-availability triggers. The central dispatch effect calls the Mediterranean package setup, final-validation, and cleanup dispatchers, so admission reaches the existing package-owned implementation instead of stopping at selection.

## Region 02 planner wiring

Direct inspection of `006_independence_wave_packages_region_02_effects.txt` confirms each of IW-017, IW-018, and IW-019 has all required publisher surfaces:

- exact load helper
- automatic-weight preparation helper
- region-total weight contribution
- exact anchor reservation helper
- region 02 weighted selector entry

The load mappings are COR/state 1/group 1, ARX/state 114/group 114, and ASX/state 115/group 115. IW-017 retains its `automatic_if_not_living` disposition and registered-tag treatment. IW-018 and IW-019 retain `automatic_ready` and new-event-tag treatment.

## Automatic capacity proof

The Liberations-cluster capacity witness tries these 11 admitted IDs in deterministic order:

`1, 2, 4, 6, 7, 8, 9, 10, 17, 18, 19`

Their reservation groups contain 10 distinct values. IW-008 and IW-010 deliberately share `rg_rhine_saar`. Every other admitted row has a distinct group. The capacity witness records and compares package IDs, country scopes, anchor scopes, and reservation groups, then requires all four temporary arrays to have the exact selected count.

The band and capacity ladder is sufficient at every level:

| Chaos band | Target | Eligible distinct groups with all rows otherwise viable |
|---|---:|---:|
| Calm World | 3 | 6 |
| Gathering Storm | 4 | 9 |
| Rising Chaos | 5 | 10 |
| Chaos Tier | 7 | 10 |
| Totalen Chaos | 10 | 10 |
| World Collapse | 10 | 10 |

The source constants are exactly `3 / 4 / 5 / 7 / 10 / 10`. World Collapse therefore requests exactly 10, not 11. The shared reservation-group collision between IW-008 and IW-010 makes the 11 admitted package rows resolve to the intended maximum of 10 disjoint selections.

## Host-survival proof

After selecting its deterministic witness, the capacity trigger uses `all_of_scopes` over the selected anchor array. For every selected anchor, its owner must exist and own at least one state that is not present in the complete selected-anchor array.

This is an all-owner proof, not a one-host sample. If Sardinia and Sicily are both selected, the shared owner `ITA` evaluates the same full selected-anchor array containing states 114 and 115. Neither island can satisfy the remnant test, so Italy must own a third state. The same proof covers every other selected host and rejects a capacity witness if any host would be erased.

Official trigger documentation confirms that `all_of_scopes` evaluates its trigger for every scope in the array and fails if any evaluation is false. Vanilla uses the same array-scope construct in scripted effects and decisions.

## Event 5 disjointness

Event 5's opening tag registry contains UKR, BLR, MOL, LIT, LAT, EST, GEO, ARM, AZR, UZB, KYR, TAJ, TMS, and KAZ. It does not contain COR, ARX, or ASX.

The Event 6 capacity witness enforces three separate collision proofs:

- The candidate tag must not be an Event 5 base-republic tag.
- The anchor must not be a core of any Event 5 opening republic.
- The live anchor owner must not be SOV and must not own or control any Event 5 opening-republic core.

The installed state sources for 1, 114, and 115 contain no Event 5 opening-republic core. Baseline hosts FRA and ITA are therefore disjoint. If either host later owns or controls an Event 5 opening core, the runtime capacity proof conservatively excludes that package for the joint incident.

## SCN-008 behavior

`independence_wave_scenario_set_intensity_tuning` sets the candidate target to the complete bound registry count before applying Low, Medium, High, or Maximum intensity tuning. Intensity changes territory, force, and country-value tuning, but never reduces the candidate count.

The ranked registry contains 138 distinct bound package IDs. IW-017, IW-018, and IW-019 each occur exactly once. `independence_wave_scenario_attempt_ranked_packages` uses `for_each_loop` over the complete ranked array, so every intensity attempts every bound candidate. Each unavailable package records a rejection, while viable packages pass through the shared reservation API. The plan target is reduced to the exact selected count only after the full ranked loop and optional-territory pass.

## Validation evidence

### Repository allocator audit

Command:

```text
python .tools/audit_event6_allocator.py
```

Result: `Event 006 allocator audit passed`

The audit reported 149 publishers, 126 automatic or high-chaos selectable packages, 138 SCN-008 ranked packages, automatic counts `3 / 4 / 5 / 7 / 10`, World Collapse 10, anchor-first ordering, and the correct Event 5 then Event 6 joint allocation order.

### Independent targeted source test

A separate read-only PowerShell source test passed. It asserted:

- exact equality of the 11-ID adapter, attestation, runtime-preflight, scenario-preflight, and capacity-try sets
- exact region 02 load, weight, reserve, and selector wrappers for IW-017 through IW-019
- exactly 10 distinct capacity reservation groups
- earliest bands IW-017=0, IW-018=1, and IW-019=1
- all automatic target constants including World Collapse=10
- 138 distinct SCN-008 ranked rows with one occurrence of each new package
- invariant scenario candidate count across all intensities
- a full ranked-array `for_each_loop`
- the all-owner host-survival proof
- no Event 5 opening-republic core on states 1, 114, or 115

Result: `TARGETED_ALLOCATOR_TEST_PASSED`

## References consulted

- Repository skills `chaos-redux-events` and `chaos-redux-subagents`
- Offline Paradox wiki core pages required by `AGENTS.md`
- Official effects and triggers documentation for temporary arrays, `for_each_loop`, `all_of_scopes`, `check_variable`, `is_in_array`, and event targets
- Vanilla array-scope and array-loop precedents
- Installed-map package binding ledger and candidate registry
- Vanilla state history for states 1, 114, and 115

## Blockers and limitations

- No blocker was found in the bounded admission surface.
- This is a source-based admission audit. The repository allocator audit explicitly does not simulate a live HOI4 campaign, which was not requested for this read-only task.
- No fallback, omission, or simplification was used.
