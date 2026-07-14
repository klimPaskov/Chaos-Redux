# Independence Wave research validation report

Validation date: 2026-07-10

## Result

The 2026-07-10 research baseline passed **258 targeted checks**. These checks cover package coverage, tag policy, baseline map anchoring, source references, research dispositions, the wave ladder, cross-file mirrors, prompt completeness, CSV integrity, and package navigation. The 2026-07-14 implementation reconciliation supersedes the baseline's installed-map and audio-rights assumptions where stated below.

## Coverage totals

- Candidate packages: **206**
- Candidate research resolution rows: **206**
- Registered tag reuse: **78**
- New Event 6 tags ending in `X`: **128**
- Duplicate resolved tags: **0**
- Reservation groups: **111**
- Source-register entries: **74**
- URL-backed source entries: **35**
- Bibliographic or institutional source packets without a direct URL: **39**
- Content files excluding this report and the generated manifest: **47**
- Content lines excluding this report and the generated manifest: **9,384**
- Goal prompt characters: **3,986**

The 39 source packets without direct URLs are books or grouped institutional research packets. They are recorded with title or source-family direction, creator or institution, period, design use, confidence, and caution. They do not claim item-level image, portrait, flag, or recording rights. Final visible assets still require their own provenance records.

## Candidate and tag checks

- All 206 package IDs are unique and match between the candidate registry and resolution matrix.
- Every required research field is filled.
- Every resolved tag is a valid three-character uppercase tag.
- Every new Event 6 tag matches `[A-Z][A-Z]X`.
- New tags are unique and avoid the dated public `X`-ending baseline and the current Chaos Redux custom registry.
- Edo Benin uses `DRX`, while Biafra retains `BIA`. The two identities no longer share a tag.
- Every resolution field mirrored into the expanded candidate registry matches exactly.

## Disposition checks

- `automatic_pool_ready`: **11**
- `automatic_pool_ready_if_not_living`: **44**
- `automatic_pool_ready_if_unique_state_exists`: **77**
- `high_chaos_only`: **32**
- `formable_or_route_only`: **9**
- `specific_community_variant_only`: **30**
- `scenario_variant_only`: **3**

Every package points to a valid reservation group and valid source IDs. A restrictive disposition counts as a completed research outcome. It prevents an unsafe broad identity or coarse-map overlap from entering an automatic wave.

## Map and wave checks

- All 111 reservation-group rows have uniform CSV structure.
- The first five automatic chaos-tier counts are exactly **3, 4, 5, 7, and 10**.
- The World Collapse tuning row keeps the automatic count at 10 and changes intensity rather than adding a terminal Event 6 branch.
- The package contains no terminal Event 6 scenario surface.

Numeric state IDs remain a dated public baseline. The named geographic anchor, overlap group, compact-release rule, and host-survival rule are binding. Implementation must rebind the IDs to the installed game and current map overrides.

### Installed-map reconciliation, 2026-07-14

- All **206** packages were evaluated against the installed 1,081-state map.
- **149** packages are bound and **57** remain unbound.
- The bindings reference **205** distinct installed state IDs, all of which exist.
- All **111** accepted reservation groups still cover all 206 packages exactly once.
- The collision ledger contains **14** rows: 12 same-group overlaps, one cross-group automatic blocker at state 354 Trabzon, and one cross-group route exclusion at state 441 Kashmir.
- No fallback or nearby broad-state substitution was used.

The machine-readable result is under `../../../plans/006_independence_wave_plans/package_bindings/`. The two cross-group findings remain explicit implementation decisions.

## Super-event checks

The production prompt and research files contain two distinct approved packages:

1. **The League of New States**
   - original button text recorded
   - Woodrow Wilson Point XIV excerpt and attribution recorded
   - Jeremiah Clarke musical selection, segment, reserved path, and suggested audio ID recorded
   - the exact London Brass Players recording is blocked because United States redistribution rights were not verified

2. **Every Border a Casus Belli**
   - original button allusion recorded
   - Hosea 8:7 King James Version quote and attribution recorded
   - Tchaikovsky United States Marine Band recording, segment, rights basis, preserved source checksum, final path, and suggested audio ID recorded

The two reserved OGG paths and suggested IDs are distinct. Both selected edit plans use 110-second segments. Only `6002` has a cleared and preserved source for later production.

## Package integrity checks

- Every CSV has one uniform column count.
- All package text files decode as UTF-8.
- Every path listed in the README exists.
- The goal prompt remains inside the required 3,500 to 4,000 character range.
- No package-disposition or quote-source placeholder remains. The later `6001` recording-rights verification is an explicit blocker, not a hidden source assumption.
- New research prose avoids em dashes and semicolons.

## Remaining boundary

The remaining tasks are implementation, production, and explicit blocker resolution:

- choose the state-level exclusion behavior for Trabzon and Kashmir without silently changing reservation groups
- Clausewitz implementation
- final ordinary localisation
- visual asset sourcing and generation
- obtain rights clearance for the accepted `6001` recording, or ask the user before reopening selection
- trim, convert, checksum, and wire the verified `6002` source
- gameplay, AI, map, scenario, focus, decision, GUI, and super-event validation

The map and tag scans are complete for the 2026-07-14 snapshot and must be repeated only if the installed build or registries change. No fallback recording is authorized.
