# Event 006 country-registry API handoff

## Delivered

- Added the `independence_wave_country_groups` static country-group category
  with 191 unique resolved tags, 102 Event 006-owned X tags, 89 unique reused
  tags, 14 deduplicated region arrays, and three Africa overlap views.
- Added named runtime collections over those arrays. Collections intentionally
  enumerate only currently existing country scopes; static arrays remain the
  dormant availability source.
- Added exact membership/origin predicates and Event 006 origin lifecycle
  wrappers. Event 012 never calls the Event 006 origin writer.
- Updated Event 012 compatible-overlap recognition and the supported-carrier
  recorder. MLI/TIG/SUD/ZIM remain explicit Event 012 vanilla carriers and are
  not falsely mapped to compatible Event 006 identity rows; TIG's Event 006
  identity remains Tigray, not Aksum.
- Changed Event 012 focus loading to generic-tree-only replacement with an
  additive preserved-tree mode; Event 006/Soviet origin gates fail closed.
- Added the canonical field guide at `docs/events/006_independence_wave/systems/country_registry.md`.

## Files changed

- `common/script_constants/006_independence_wave_country_registry_constants.txt`
- `common/collections/006_independence_wave_country_collections.txt`
- `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`
- `common/scripted_effects/006_independence_wave_country_registry_effects.txt`
- `common/scripted_effects/006_independence_wave_country_registry_effects.md`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/012_africa_priority_member_triggers.txt`
- `common/scripted_effects/012_africa_priority_member_effects.txt`
- `docs/events/006_independence_wave/systems/country_registry.md`

## Exact Event 012 hunks

1. All `africa_priority_member_origin_is_*` predicates now reject active Event
   006/Soviet origins and use shared exact carrier predicates for direct
   overlaps. The four nonmatching vanilla carriers remain accepted through a
   dedicated predicate.
2. `africa_priority_member_has_supported_carrier_identity` uses the canonical
   overlap/nonmatching predicates and its stale `eight identities` wording was
   replaced with the direct-overlap plus four-vanilla-carrier contract.
3. `africa_priority_member_can_register_package` gained the shared Soviet
   origin guard while retaining the parent-owned Event 006 guards.
4. `africa_priority_member_record_iw_overlap_origin` records only Africa
   flags; the existing recorder calls it and handles MLI/TIG/SUD/ZIM separately.
5. `africa_priority_member_ensure_focus_tree_loaded` now requires the safe
   Africa origin scope, loads only from `generic_focus`, and records a skipped
   overlay when a meaningful tree must be preserved.

## Validation evidence

- CSV-derived counts: 206 rows; 102 new X rows; 91 reuse rows; 13 overlays;
  191 unique resolved tags; duplicate resolved tags only CHU and BIA.
- Parsed static arrays: all=191, Event 006-owned=102, registered reuse=89;
  all 14 region arrays exactly match deduplicated CSV tags.
- Parsed exact trigger OR lists: Event 006-owned=102 and registered reuse=89;
  no duplicate GLX/KUB omissions remain.
- Africa overlap groups: all=12, non-overlay=11, current-map bound=8. The last
  count is map feasibility, not package-content readiness.

The required read-only focus inspection was run for
`africa_priority_member_focus_tree` before changing the loader. Artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/290f3dec4e23006e9418591082322b803eb313b422956df0ceba70ff2001f716/ac77b81f953fcd8aecc5e4ff9626f8795ad01eea266b3020b914207e6e1c78e9/focus-inspect.8a83173d7922817b.json`.
It confirms the Africa tree is a separate eight-focus tree. The inspector also
reported pre-existing missing focus sprite/texture diagnostics (22 blocking
focus diagnostics overall); no asset files were changed in this registry lane.

## Risks and follow-up

- Collections are not a dormant-country test; callers needing dormant
  availability must use static groups or exact registry triggers.
- DYX/DZX/EMX remain documented overlap carriers but are not current-map
  selectable until their package bindings are installed.
- The focus loader intentionally fails closed for a carrier with no recognised
  focus tree because the installed engine surface has no supported no-tree
  trigger in this scope. No meaningful tree is overwritten.
- No advisor assets, tags, or country definitions were added.
