# Event 006 Package Registry Handoff: Regions 09–11

## Scope and ownership

This handoff covers only the package readiness triggers and package publisher effects for `IW-093` through `IW-132` in regions 09–11. The parent agent retains aggregate allocator wiring, country/tag implementation, final Event 006 integration, audit, and commit ownership.

Skills used:

- `chaos-redux-subagents` for bounded ownership and handoff requirements.
- `chaos-redux-events` for Event 006 scripting and integration conventions.

No skill was created or updated.

## Reference basis

- Read the required offline wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Read the installed official documentation for effects, triggers, dynamic variables, script concepts, and script constants.
- Checked vanilla scripted precedents for regular event-target capture (`POL_remove_danzig_effect`), weighted `random_list` structure (`BUL_get_random_bulgarian_destination_royal_visit`), and array membership inside a scripted trigger (`00_scripted_triggers.txt`).
- Followed the shared Event 006 planner/readiness/reservation contracts and the implemented Region 01–05 registries before creating these files.

## Files created

- `common/scripted_triggers/006_independence_wave_packages_region_09_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_10_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_10_effects.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_11_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_11_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_packages_regions_09_11_handoff.md`

## Implemented package coverage

### Region 09: West and Central Africa

Bound packages with readiness, loader, and exact reservation publisher:

- `IW-093`, `IW-095`, `IW-097`, `IW-098`, `IW-099`, `IW-100`, `IW-101`, `IW-106`, `IW-107`.

Automatic weighted pool:

- `IW-093`, `IW-095`, `IW-097`, `IW-098`, `IW-099`, `IW-101`, `IW-106`, `IW-107`.

`IW-100` is `formable_or_route_only`; it has a callable readiness trigger, loader, and reservation publisher but no automatic weight and no selector entry. High-chaos gating is applied only to `IW-093`, `IW-097`, `IW-099`, `IW-101`, and `IW-106`.

### Region 10: East Africa, Horn, and Great Lakes

Bound and automatic packages:

- `IW-108`, `IW-110`, `IW-111`, `IW-113`, `IW-114`, `IW-115`, `IW-119`.

None of these rows has a high-chaos disposition, so no high-chaos gate is present.

### Region 11: Southern Africa and Indian Ocean

Bound and automatic packages:

- `IW-121`, `IW-126`, `IW-130`, `IW-131`, `IW-132`.

None of these rows has a high-chaos disposition, so no high-chaos gate is present.

## Omitted package coverage

The following rows are deliberately absent from triggers, loaders, reservers, weights, and selectors because the accepted binding audit leaves them unbound:

- `IW-094`, `IW-096`, `IW-102`, `IW-103`, `IW-104`, `IW-105`, `IW-109`, `IW-112`, `IW-117`, `IW-122`, `IW-123`, `IW-124`, and `IW-125`: disabled because no unique authoritative current-map state exists.
- `IW-116`: scenario-only but `scenario_only_unbound`.
- `IW-118`, `IW-120`, `IW-127`, `IW-128`, and `IW-129`: specific-community variants whose accepted rows remain unbound.

No fallback state, tag, or package binding was introduced.

## Manually reviewed archetypes

| Package | Archetype | Manual basis |
| --- | --- | --- |
| IW-093 Asante | `agrarian_regional` | Confederated Asante heartland, forest forces, and community institutions. |
| IW-095 Dahomey | `agrarian_regional` | Compact historic heartland with local infantry and palace or national guards. |
| IW-097 Oyo | `agrarian_regional` | Yoruba heartland, cavalry tradition, and a regional constitutional restoration. |
| IW-098 Sokoto | `agrarian_regional` | Caliphal or emirate federation rooted in a broad northern heartland. |
| IW-099 Kanem-Bornu | `river_or_corridor` | Lake Chad trade corridor and mobile Sahel connections. |
| IW-100 Hausa Federation | `urban_administrative` | Explicit city-state federation built around urban guards and trade institutions. |
| IW-101 Kongo | `river_or_corridor` | Lower Congo river trade and river-infantry identity. |
| IW-106 Aro Confederacy | `agrarian_regional` | Forest confederacy with local guards and community authority. |
| IW-107 Biafran regional state | `industrial_breakaway` | Modern breakaway profile with industrial and local militia. |
| IW-108 Buganda | `urban_administrative` | Kampala-centered royal and colonial administration with lake communications. |
| IW-110 Rwanda | `agrarian_regional` | Compact agrarian national state with local infantry. |
| IW-111 Burundi | `agrarian_regional` | Compact agrarian national state with local infantry. |
| IW-113 Harar | `urban_administrative` | City-emirate, merchant institutions, and urban guards. |
| IW-114 Afar | `nomadic_or_dispersed` | Pastoral and sultanate confederation with mobile desert forces. |
| IW-115 Somaliland | `port_or_island` | Coastal sultanate federation, ports, sailors, and trade access. |
| IW-119 Tigray | `mountain_or_frontier` | Highland anchor and highland infantry. |
| IW-121 Zulu | `agrarian_regional` | Regional kingdom or national state with traditional guards and land institutions. |
| IW-126 Barotseland | `river_or_corridor` | Upper Zambezi and floodplain identity with river guards. |
| IW-130 Madagascar | `port_or_island` | Island kingdom or republic with coastal access and limited strategic depth. |
| IW-131 Comoros | `port_or_island` | Island sultanate federation with coastal guards and sailors. |
| IW-132 Mauritius | `port_or_island` | Island colonial successor dependent on maritime trade. |

## Reservation and collision behavior

Every bound row uses `fixed_anchor_compact`. In all 21 accepted rows, `compact_state_ids` duplicates the single anchor and `extended_state_ids` is empty. Each publisher therefore reserves the anchor exactly once and makes no compact or extended call. No choose-one row exists in this slice.

The accepted reservation groups remain authoritative:

- `RG-NIGERIA-COARSE` covers the Nigerian package family and prevents concurrent plan selection. This also resolves the explicit state collisions `IW-106`/`IW-107` on state 900 and `IW-098`/`IW-100` on state 902.
- `RG-GREAT-LAKES-COARSE` coordinates `IW-108`, `IW-110`, and `IW-111`.
- `RG-HORN-HIGHLANDS-COARSE` coordinates `IW-113`, `IW-114`, `IW-115`, and `IW-119`.
- `RG-SOUTHERN-AFRICA-COARSE` coordinates `IW-121` and `IW-126`.
- Other packages retain their accepted Ghana, Congo basin, or single-state group.

All reservation publishers copy the current `independence_wave_wave_territory_level` and `independence_wave_wave_force_level`, call the shared begin/finish lifecycle, and publish no fallback territory.

## Validation evidence

- Compared every bound row against the accepted binding CSV for tag, anchor state, reservation group, binding mode, and automatic disposition.
- Compared every loader against the candidate registry for depth and manually reviewed archetype assignment.
- Coverage audit found exactly 21 can-plan triggers, 21 loaders, 21 reservation publishers, 20 automatic weight helpers, and the matching 20 selector entries. `IW-100` is the sole bound non-automatic package.
- Confirmed all five high-chaos weights and only those weights require `is_independence_wave_high_chaos_pool_open`.
- Confirmed all 19 distinct anchor state files exist in the installed current-map state history.
- Confirmed all 12 reused tags exist in installed tag registries. The nine accepted `reserve_new_event6_X_tag` values are currently unused and collision-free: `DOX`, `DSX`, `DUX`, `DVX`, `DWX`, `EBX`, `EQX`, `FAX`, and `FBX`.
- Cross-file symbol audit found no duplicate Region 09–11 definitions among 89 package and regional helper definitions.
- Confirmed all unbound IDs are absent, all fixed anchors are reserved once, no choose-one publisher appears, and no compact/extended publisher duplicates an anchor.
- The optional Event Chain Inspector returned `EVENT_INSPECTED_PARTIAL` with no blockers for all six helper files. It skipped two event-analysis sources and truncated its inline inventory, so its result is recorded as partial evidence rather than a passing parser verdict; the exact source and registry audits above remain the validation basis for this tranche.

## Risks and parent integration notes

- `IW-114` points at state 908, initially owned by `AFA`; that state is also AFA's protected capital and its sole 1936 state. The accepted binding explicitly requires rejection while capital protection or host-survival would be violated. The shared readiness and reservation lifecycle remains authoritative; no substitute anchor was added.
- The parent integration registered the nine collision-free Event 006 X-tags after this bounded tranche. Their full researched country content, leaders, assets, and package-content readiness flags remain separate completion gates.
- The parent allocator now calls the region 09, 10, and 11 weight-preparation and selection helpers from its aggregate regional allocation flow.

## Simplifications, omissions, and blockers

No simplification or fallback was used. The omitted rows are the explicit accepted unbound dispositions listed above. There is no blocker inside this bounded registry tranche; full country-package content and final execution remain parent integration work.
