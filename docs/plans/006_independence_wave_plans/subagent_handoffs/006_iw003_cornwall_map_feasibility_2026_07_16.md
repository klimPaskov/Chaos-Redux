# IW-003 Cornwall map feasibility audit

Date: 2026-07-16

Package: `IW-003` Cornwall / `ACX`

Mode: read-only map, tag, package, and Event 005/Event 006 collision audit

Implementation status: **disabled**

## Verdict: C - keep IW-003 disabled

There is an exact, defensible province split for Cornwall, but there is no state
ID that satisfies both HOI4's contiguous-state requirement and the accepted
all-installed-mod collision rule.

- Vanilla has 1,081 state definitions with exactly one unique ID at every
  integer from `1` through `1081`.
- The only ID that can be appended without a gap is `1082`.
- State `1082` is already defined by 11 installed Workshop mods.
- Every ID from `1082` through `2525` is present in the installed-mod state
  inventory. `2526` is the first unclaimed value, but it would leave 1,444
  missing state IDs and therefore is not a legal standalone Chaos Redux state.
- Renumbering another mod, creating filler states, taking all of vanilla state
  123, or substituting a nearby state would be a fallback. None is accepted.

`IW-003` must therefore remain `disabled_no_unique_current_state`, `ACX` must
remain a reserved dormant shell, and no map or package content should be wired
from this audit.

No gameplay, map, country, asset, localisation, CSV, spreadsheet, or spec file
was edited. This handoff is the only file created.

## Sources consulted

The required offline wiki snapshot was used, including Data structures,
Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding,
Decision modding, Idea modding, AI modding, State modding, Map modding, Country
creation, Buildings, and Resources.

The current vanilla installation was inspected directly, including:

- `documentation/effects_documentation.md`;
- `documentation/triggers_documentation.md`;
- `documentation/modifiers_documentation.md`;
- `documentation/script_concept_documentation.md`;
- `common/script_constants/documentation.md`;
- `history/states/123-Cornwall.txt`;
- `map/definition.csv`, `map/provinces.bmp`, `map/buildings.txt`,
  `map/strategicregions/1-Southern England.txt`, `map/supply_nodes.txt`,
  `map/railways.txt`, `map/adjacencies.csv`, and `map/unitstacks.txt`;
- vanilla country tags, localisation, decisions, events, focuses, AI strategy,
  faction theatres, achievements, and British OOB files that reference state
  123.

Kaiserreich Workshop item `1521695605` supplies the approved large-mod
precedent: its `history/states/123 - Cornwall.txt` assigns province `6526`
alone to Cornwall, while `history/states/1123 - West Country.txt` keeps
`540 3422 3463 9562 11406` together around Plymouth.

The HOI4 map MCP domain tools were not exposed in this subagent session, so the
map proof used the installed source files and a direct province-bitmap geometry
inspection. No rewrite tool was called.

## Exact geographic plan if a legal ID later becomes available

The split below is the safe geography. It is **not authorized for
implementation while the state-ID blocker remains**.

| Property | New Cornwall state | Surviving state 123 |
|---|---|---|
| State ID | the next legal, collision-free contiguous ID; `1082` is technically contiguous but currently blocked | `123` |
| Name | `STATE_<new_id>` = `Cornwall` | retain `STATE_123` = `South-West England` |
| Provinces | `6526` only | `540 3422 3463 9562 11406` |
| Anchor / victory point | Truro, province `6526`, 1 VP | Plymouth, province `540`, 10 VP |
| Manpower | `308230` | `912783`, preserving vanilla's total `1221013` |
| Category | `rural` (2 local building slots, matching Kaiserreich's two-slot precedent) | retain `town` |
| Owner and cores in state history | owner `ENG`; core `ENG` only | owner `ENG`; core `ENG` |
| Starting buildings | infrastructure 3 only | retain infrastructure 4, 1 civilian factory, 1 anti-air, radar 1, air base 6, and Plymouth naval base 8 |
| Resources | none | none; retain later Devon tungsten prospecting on state 123 |
| Local supplies | `0.0` | `0.0` |

Important boundaries:

- Province `11406` remains in state 123. It is part of the West Country host,
  not the Cornish anchor.
- Plymouth, its naval base, its supply node, its railway connection, its air
  group, and its naval OOB locations all remain with state 123.
- Do not add an `ACX` core in static state history. The frozen Event 006
  executor should add the planned core immediately before release. This keeps
  ordinary diplomacy and Event 005 core scans from treating dormant `ACX` as a
  general release candidate.
- Do not create a starting port, factory, mine resource, or supply node in the
  new state without a separate approved design. The existing "port and mines"
  committee is country flavour, not authority to invent map infrastructure.
- The runtime host-remnant proof must still reject the package if the current
  owner cannot lose the new state while retaining another owned state.

The Kaiserreich manpower number is used only for the proposed Cornwall share.
Its unrelated owner claims, state-category token, West Country manpower, and
building changes are not copied.

## Required map mutation ledger if the blocker is resolved

### State and localisation files

1. Override the vanilla relative path `history/states/123-Cornwall.txt`. Keep
   ID 123 and the host values above, but remove province 6526 and the Truro VP.
2. Add `history/states/<new_id>-Cornwall.txt` with province 6526 and the exact
   values above.
3. Add `STATE_<new_id>: "Cornwall"` to a bounded English localisation file
   encoded as UTF-8 with BOM. Do not rename `STATE_123`.

The existing filename `123-Cornwall.txt` must be overridden by the same
relative path even though its displayed state remains South-West England;
adding a second state-123 file under a new filename would create a duplicate.

### `map/buildings.txt`

`map/buildings.txt` is a whole-file override. Copy the current vanilla file,
then change only the leading state field from `123` to the new Cornwall ID for
the 13 placements whose X/Z coordinates fall inside province 6526:

| Current vanilla line | Placement |
|---:|---|
| 1952, 1954, 1956 | three `arms_factory` positions |
| 1958, 1960 | two `industrial_complex` positions |
| 1966 | `naval_base_spawn` |
| 1976 | `bunker` |
| 1977 | `coastal_bunker` |
| 21419 | `supply_node` placement |
| 30693 | `floating_harbor` with explicit province field `6526` |
| 41157 | `special_project_facility_spawn` |
| 54994 | `naval_supply_hub` |
| 59760 | `naval_headquarters` |

These are placement slots, not starting buildings. The state history above
still gives Cornwall only infrastructure 3. All other state-123 placements,
including the stronghold-network position at current line 48464 and every
placement around Plymouth or province 11406, remain state 123.

Because this is a full vanilla-file override, it must be regenerated and the
13 coordinate assignments rechecked after any HOI4 map update. It also makes
the split inherently incompatible with unreviewed map-overhaul combinations.

### Files that do not change

- `map/definition.csv` and `map/provinces.bmp`: no new province is created;
  province 6526 already exists.
- `map/strategicregions/1-Southern England.txt`: all six original provinces
  are already in strategic region 1, so both resulting states remain valid.
- `map/supply_nodes.txt`: the existing node is `1 540` at Plymouth; none is
  moved to Cornwall.
- `map/railways.txt`: the line beginning `1 7 540 3463 ...` remains on the
  host side; province 6526 is not on a vanilla railway.
- `map/adjacencies.csv`: none of the target provinces uses a special adjacency
  that needs to move.
- `map/unitstacks.txt`: positions are province based and remain valid.

## Installed state-ID collision audit

The inventory covered 122 Workshop directories and four local mod directories,
with 23,990 candidate state files. The current contiguous candidate, `1082`,
is claimed in these 11 Workshop items:

| Workshop item | State-1082 definition |
|---|---|
| `1458561226` | `1082-Palmyra Atoll.txt` |
| `1521695605` | `1082 - Guadalajara.txt` |
| `1827273767` | `1082-Liancourt Rocks.txt` |
| `2076426030` | `1082 - Lori.txt` |
| `2265420196` | `1082-State.txt` |
| `2438003901` | `1082-Central Tanganyika.txt` |
| `2777392649` | `1082-Dhofar.txt` |
| `2815832636` | `1082-Jabalpur.txt` |
| `3297046215` | `1082-Darmstadt.txt` |
| `3365515312` | `1082-Malani-Litani.txt` |
| `820260968` | `1082-Dominica.txt` |

The collision matters here because the accepted audit contract requires a
state ID not claimed by any installed mod. Some of these mods are mutually
exclusive total-conversion maps, but silently narrowing the compatibility
contract to a vanilla-only playset would be a user decision, not an auditor
fallback.

## Tag, country-shell, and asset audit

- Vanilla `COR` is Corsica and cannot be reassigned to Cornwall.
- `ACX` is defined only by Chaos Redux in
  `common/country_tags/006_independence_wave_countries.txt`.
- An external search across vanilla, all 122 Workshop directories, and all
  four local mod directories found no competing `ACX` tag definition,
  cosmetic alias, country identity, or localisation key. `ACX` remains the
  locked Cornwall tag.
- Chaos Redux already has the country shell, dormant history shell, and country
  name/adjective localisation for `ACX`.
- The complete `gfx/flags/ACX.tga` triplet exists. Large and small ACX portrait
  DDS outputs also exist under `gfx/leaders/006_independence_wave/`.
- The portraits are not registered in a sprite file or character definition,
  and their names/traits/localisation are not wired. The country shell also has
  no dormant technology, slots, convoys, OOB, AI, ideas, decisions, or focus
  framework. Assets do not make the package content-ready.

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_generated_art_handoff.md`
correctly records the live ACX flag repair as complete and geography as the
remaining country-content blocker. The older
`asset_research/006_generated_flag_blockers.md` list is stale for the flag
layer and should be reconciled only when the parent performs the wider
documentation pass.

## Vanilla state-123 compatibility ledger

A state split is not complete if only the state and map files are changed.
Every hardcoded use of state 123 needs semantic disposition. The current
vanilla audit produced the following ledger.

### Retarget from state 123 to the new Cornwall state

- `common/decisions/ENG.txt`: the Cornwall Blackshirt march availability,
  highlight, and saved march-state scope at current lines 1441, 1445, and 1461.
- `events/MTG_Britain.txt`: the corresponding Cornwall Blackshirt support flags
  at current lines 4195, 4392, and 4588.

These are explicitly Cornwall mechanics. Leaving them on state 123 after the
split would make Plymouth/Devon stand in for Cornwall.

### Keep on surviving state 123

- `common/national_focus/uk.txt` current line 10197: the block is labelled
  Cornwall but explicitly builds Plymouth coastal bunkers in province 540.
- `history/units/ENG_1939_air_bba.txt` and
  `history/units/ENG_1939_air_legacy.txt` current line 53: Plymouth air groups.
- British naval OOB entries located at province 540.
- `common/decisions/resource_prospecting.txt` current Cornwall tungsten
  decisions: they model the Drakelands/Hemerdon mine near Plympton/Plymouth in
  Devon, so their state-123 ownership, flags, and resource effects stay with
  the host. Supporting primary references are the UK government's
  [Mining and quarrying in the UK](https://www.gov.uk/government/publications/extractive-industries-transparency-initiative-payments-report-2018/mining-and-quarrying-in-the-uk)
  and Environment Agency's
  [Hemerdon permit consultation](https://www.gov.uk/government/news/final-consultation-on-permit-for-hemerdon-tungsten-mine).
- The fixed state-123 anti-air blocks near the start of `common/national_focus/uk.txt`
  remain host-specific. Its generic strategic-region-1 loops can already see
  the new state while ENG owns it.
- The French scripted-localisation grammar tests for `STATE_123` remain tied to
  that unchanged key. Add the new state to the correct grammar class rather
  than replacing 123.

### Extend reviewed whole-Britain lists with the new state

Where state 123 is one row in an enumeration of England, Great Britain, or the
British Isles, append the new state so the split does not silently remove
Cornwall from the original mechanic:

- `common/achievements.txt`: Operation Sea Lion and Rule Britannia checks;
- `common/decisions/SS.txt`: Britain recruitment control requirements;
- `events/NewsEvents.txt`: the two Sea Lion state-control checks;
- `common/decisions/GER.txt`: Grossbritannien requirements/highlights and the
  Western Grand Duchy/Wales state set;
- `common/decisions/formable_nation_decisions.txt`: North Sea Empire, European
  Union/British Isles, Roman Britannia, and Greater Proletarian lists;
- `common/scripted_triggers/GER_scripted_triggers.txt`: Grossbritannien zone;
- `common/ai_strategy/GER.txt`: Sea Lion foothold state checks;
- `common/ai_strategy/ENG.txt`: coastal unit-buffer lists and Channel-control
  strategy where the list represents all southern/western British states;
- `common/ai_faction_theaters/ai_faction_theaters.txt`: Britain theatre;
- `common/decisions/RAJ_GOE.txt`: West Britain Company core set.

The Greater Wales transfer in `common/decisions/GER.txt` needs an explicit
design decision: adding the new state preserves the pre-split territorial
coverage, while excluding it protects a live Event 006 Cornwall. It must not be
silently decided by omission. The affected vanilla files are large,
version-sensitive overrides, so each needs a bounded diff and re-audit in the
implementation tranche.

Numeric `123` references that are event IDs, equipment names, ship numbering,
amounts, or non-state regions are noise and must not be mechanically rewritten.

## Conditional Event 006 package binding plan

If a legal ID is later approved, preserve the existing stable identifiers:

- `constant:independence_wave_package_id.iw_003 = 3`;
- `constant:independence_wave_reservation_group_id.rg_123 = 10`;
- tag `ACX`;
- region `NWE`, Level 1 depth, `port_or_island` archetype, and the existing
  coastal-maritime force mapping with tradition score 42 and no navy/air
  inheritance.

The implementation order is:

1. Land the map split and the entire vanilla compatibility ledger above.
2. Add `independence_wave_load_package_iw_003`, its preparation weight,
   automatic-pool row, reservation publisher, and random-list entry to
   `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt`.
   The reservation publisher must reserve the new Cornwall state as the only
   anchor and must never reserve state 123 as compact, extended, or fallback
   territory.
3. Add `can_plan_independence_wave_package_iw_003` and exact dormant-tag/state/
   host checks to `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt`
   and the shared runtime wrapper.
4. Add the package's runtime adapter, preflight, content attestation, setup,
   final-validation, and generic dispatch rows only after its full country
   package is wired.
5. Implement the full no-vanilla-tree country framework: characters and
   sprites, country setup, ideas, decisions/missions, focus content, AI,
   dynamic forces, all localisation, and origin/package-gated mechanics.
6. Remove the `IW-003`/`ACX` pair from
   `independence_wave_scenario_append_unbound_registry_rows` in
   `common/scripted_effects/006_independence_wave_scenario_effects.txt`, raise
   `bound_package_count` by one, lower `disabled_unbound_package_count` by one,
   update the current binding and reservation-group CSVs, insert package 3 into
   the deterministic ranked registry, and align specs, event details, force
   docs, asset manifests, and the event spreadsheet.
7. Keep `independence_wave_package_content_ready` unset until the package audit
   proves every surface. Re-audit FORM-01 separately before adding Cornwall;
   the current exclusion is correct.

SCN-008 can continue requesting the normal intensity ladder (low
anchor/fragile, medium compact/viable, high extended/armed, maximum
extended/high-chaos). Cornwall has no optional compact or extended states, so
all intensities transfer only the unique Cornwall anchor. The frozen achieved
territory level remains anchor; force strength and the related starting values
may scale. A Great Partition promotion must not pull in state 123.

## Event 005 / Event 006 isolation proof

The conditional design remains isolated when all of these rules are kept:

1. The new state begins with an ENG core only. `ACX` is not a Soviet Collapse
   candidate, and Event 005's scoped `every_core_state` discovery cannot reach
   the Cornish anchor through any fixed Soviet successor tag.
2. Event 006 uses `independence_wave_begin_package_reservation` and
   `independence_wave_reserve_candidate_anchor`, which publish the country,
   package, state, host, and reservation group into the shared
   `global.liberation_plan_*` arrays through
   `liberation_release_add_country_reservation` and
   `liberation_release_add_state_reservation`.
3. The shared reservation flags and arrays reject a duplicate tag, package,
   state, protected host-remnant state, or reservation group whether Event 005
   or Event 006 reaches it first.
4. The Event 006 executor adds only frozen planned cores, masks unplanned cores
   for release, and marks the created country `independence_wave_active_origin`.
   `is_soviet_collapse_state_free_of_independence_wave_origin` rejects states
   owned or controlled by that origin and also rejects currently reserved or
   protected states.
5. Cornwall content must gate on Event 006 origin plus package ID 3, never on
   tag `ACX` alone. A living `ACX` causes package rejection/reroll rather than
   reuse.
6. State 123 is never put in the IW-003 reservation. The host-remnant proof
   runs before the new anchor is accepted.
7. No new daily, weekly, monthly, or whole-world on-action scan is required.

## Completion boundary and reopen criteria

This is a feasibility audit, not an implementation authorization. The package
can reopen only after the user accepts a state-ID/compatibility contract that
produces one collision-free contiguous ID, or after a future vanilla/map update
changes the contiguous ID frontier and the full installed-mod audit is rerun.

Until then:

- keep the current package binding disabled;
- keep `ACX` reserved but dormant;
- do not transfer all of state 123;
- do not substitute province 11406 or any neighbouring state;
- do not claim the existing asset layer makes the country package complete;
- do not set content readiness or add Cornwall to FORM-01.

## Simplifications, omissions, and blockers

No fallback or simplification was used. The exact safe geography, mutation
ledger, tag reservation, package route, and isolation contract are documented,
but implementation is blocked by the state-ID requirement. The goal is
therefore intentionally incomplete and IW-003 remains disabled.
