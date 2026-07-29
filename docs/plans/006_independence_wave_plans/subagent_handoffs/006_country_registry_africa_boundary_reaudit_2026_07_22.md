# Event 006 country registry and Event 012 Africa boundary re-audit

Audit date: 2026-07-22

Scope: the canonical Event 006 country-registry API, its exact Event 012
Africa consumers, shared-tag dispatch boundaries, and country-history ownership.
No gameplay, country-definition, asset, portrait, or localisation patch was
needed. This handoff is the review artifact for the parent agent.

## Result

The registry API and the Africa boundary are internally aligned. The CSV,
static arrays, named collections, exact trigger OR lists, and documented
overlap views agree. Event 012 records its own origin flags, rejects active
Event 006/Soviet origins, and loads the Africa tree only over `generic_focus`;
an existing meaningful tree is preserved. There is no Event 012 call to an
Event 006 origin wrapper and no reuse-tag country-history overwrite.

No source file in the requested gameplay surface was changed. The only file
added by this audit is this handoff.

## Registry coverage checklist

Source of truth: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`.

| Surface | Evidence | Result |
| --- | --- | --- |
| Candidate rows | CSV data rows | 206 |
| New Event 006 X rows | `tag_resolution = reserve_new_event6_X_tag` | 102 |
| Registered-tag reuse rows | `tag_resolution = reuse_registered_tag` | 91 rows, 89 unique tags |
| Overlay rows | all overlay resolutions with blank `resolved_tag` | 13; excluded from selectable arrays |
| Tagged rows / unique carriers | CSV `resolved_tag` | 193 / 191 |
| Shared resolved tags | duplicate counter | `CHU` x2 (`IW-043`, `IW-046`), `BIA` x2 (`IW-096`, `IW-107`) only |
| Static carrier arrays | `common/script_constants/006_independence_wave_country_registry_constants.txt:21-110` | 191 all, 102 new, 89 reuse; exact CSV sets |
| Named collections | `common/collections/006_independence_wave_country_collections.txt:11-104` | six carrier views plus 14 regional active-scope views; inputs point to the canonical arrays |
| Exact carrier triggers | `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:28-236` | Event 006-owned 102, reuse 89, resolved union exact; no omissions or extras |
| Africa overlap views | constants `:36-50`, triggers `:238-284` | 12 all / 11 non-overlay / 8 current-map-bound |
| Regional groups | constants `:52-110`, CSV `region_overlay` | all 14 deduplicated resolved-tag sets match the documented counts |

The 14 resolved-tag group counts are 11, 9, 9, 9, 14, 14, 10, 9, 11,
13, 12, 17, 29, and 24 in the order documented by
`docs/events/006_independence_wave/systems/country_registry.md:28-48`.

## Africa overlap and map boundary

The exact direct Event 012 identity rows are:

| Africa package | Carrier | Event 006 row | Installed-map binding |
| --- | --- | --- | --- |
| Asante | `DOX` | `IW-093` | `274`, `ready_high_chaos` |
| Oyo | `DSX` | `IW-097` | `558`, `ready_high_chaos` |
| Sokoto | `SOK` | `IW-098` | `902`, `ready_if_tag_not_living` |
| Kanem-Bornu | `DUX` | `IW-099` | `901`, `ready_high_chaos` |
| Kongo | `COG` | `IW-101` | overlay-only, nonselectable |
| Luba | `DYX` | `IW-103` | disabled; no unique current state |
| Lunda | `DZX` | `IW-104` | disabled; no unique current state |
| Buganda | `UGA` | `IW-108` | `548`, `ready_if_tag_not_living` |
| Harar | `HAR` | `IW-113` | `835`, `ready_unique_state_confirmed` |
| Kilwa | `EMX` | `IW-117` | disabled; no unique current state |
| Zulu | `EQX` | `IW-121` | `719`, `ready_unique_state_confirmed` |
| Merina | `MAD` | `IW-130` | `543`, `ready_if_tag_not_living` |

The installed binding evidence is
`docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`.
The eight map-bound rows prove map feasibility only; package-content and
visual readiness remain separate gates. `COG` is recognized only with
`COG_kingdom_of_kongo` (`common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:290-293`), so the IW-101 overlay cannot become a standalone Event 006 carrier.

Manden (`MLI`), Aksum (`TIG`), Nubia (`SUD`), and Great Zimbabwe (`ZIM`) are
explicit Event 012 vanilla carriers, not falsely mapped registry overlaps.
`TIG`'s Event 006 row is Tigray, while Event 012's Aksum identity is carried by
its own Africa origin flag.

## Exact Event 012 consumers and origin separation

The only direct registry consumers under the Event 012 prefix are:

- `common/scripted_triggers/012_africa_priority_member_triggers.txt`
- `common/scripted_effects/012_africa_priority_member_effects.txt`

Registration is called from
`common/scripted_effects/012_africa_action_effects.txt:5905` and the ratification
decision at `common/decisions/012_africa_priority_member_decisions.txt:18`.

The boundary checks are consistent:

- `is_independence_wave_registry_event6_origin` (`...registry_triggers.txt:11`)
  is the live Event 006 origin predicate.
- `is_independence_wave_registry_soviet_origin` (`:15`) is the live Soviet
  origin predicate.
- `is_independence_wave_registry_africa_origin` (`:21-26`) requires the Africa
  package-active and origin-validated flags and rejects both live origins.
- `africa_priority_member_can_register_package`
  (`common/scripted_triggers/012_africa_priority_member_triggers.txt:380-394`)
  rejects Event 006 active flags/origin and Soviet origin before package
  activation.
- `africa_priority_member_record_iw_overlap_origin`
  (`common/scripted_effects/012_africa_priority_member_effects.txt:21-119`)
  writes only `africa_priority_origin_*` flags. It does not write
  `liberation_origin` and never calls
  `independence_wave_registry_record_event6_origin` or its cleanup wrapper.
- Event 006 alone owns the two lifecycle wrappers at
  `common/scripted_effects/006_independence_wave_country_registry_effects.txt:11-24`;
  Event 006 cleanup calls the clear wrapper from
  `common/scripted_effects/006_independence_wave_effects.txt`.

This is an additive reuse boundary: Africa keeps its own package ID, flags,
ideas, decisions, forces, AI, and identity. It does not transfer territory,
grant cores, or invoke Event 006 setup merely because a carrier tag appears in
the registry.

## Focus and content loading

`africa_priority_member_ensure_focus_tree_loaded`
(`common/scripted_effects/012_africa_priority_member_effects.txt:261-289`)
requires `africa_priority_member_has_package` plus the safe Africa origin
predicate. It:

1. loads `africa_priority_member_focus_tree` only when the current tree is
   `generic_focus`;
2. uses `keep_completed = yes`;
3. marks an already loaded Africa tree as loaded; and
4. marks any other meaningful or unrecognised tree as
   `africa_priority_member_focus_tree_overlay_skipped` instead of replacing it.

Therefore an Event 006 or Soviet tree is preserved and the Africa package's
ideas, decisions, forces, and AI remain additive. No supported no-tree trigger
is available in the installed surface, so the missing/unrecognised-tree path
is intentionally fail-closed.

## CHU/BIA shared-tag dispatch

The CSV duplicate rows are not duplicate country definitions.

- CHU package predicates
  `is_independence_wave_iw043_country` and
  `is_independence_wave_iw046_country` require `original_tag = CHU`, the exact
  package ID, and the matching package flag
  (`common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:19-49`).
  `has_valid_independence_wave_chu_package_mutex` (`:80-98`) rejects both
  package flags together and requires flag/ID agreement. Setup also checks the
  requested package ID (`:103-119`).
- The keyed setup/final-validation/cleanup entry points are in
  `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:102-123`.
  They cannot route IW-046 through IW-043 because the country trigger and
  package-ID checks are exact. IW-046 remains fail-closed pending its own
  attestation.
- BIA has no specialized adapter because both IW-096 and IW-107 are currently
  fail-closed in the 2026-07-22 collision/readiness audit. IW-096 has no
  current-map loader (`readiness_verdict = disabled_no_unique_current_state`);
  IW-107's generic planner loader at
  `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt:131-145`
  still carries the distinct `iw_107` package ID and state-900 anchor, while
  its candidate gate requires the legacy content-ready flag and grants none.
  The runtime adapter/content-attestation gate therefore cannot execute either
  BIA row. There is no path that infers IW-096 content from the BIA tag or
  overwrites IW-107 with it.

When a BIA row is eventually admitted, it will need an exact package-ID setup,
validation, and cleanup adapter before content attestation is granted. That is
future package work, not an API defect in this audit, so no patch was made.

## Country-history and package surfaces

Read-only history audit results:

- 85 dedicated new Event 006 X-tag history files use normal names such as
  `ACX - Cornwall.txt`; they are not generic shell names.
- 17 reserved/unresearched X tags (`DJX`, `DMX`, `DNX`, `ENX`, `EXX`, `EYX`,
  `FPX`, `GDX`, `GGX`, `GHX`, `GLX`, `HHX`, `HMX`, `HQX`, `HTX`, `HWX`,
  `HXX`) have no dedicated history file and remain mapped to the shared
  unresearched country definition. This matches the registry's fail-closed
  identity status.
- None of the 89 registered reuse tags has a mod country-history file. Vanilla
  and registered carriers therefore retain their original history; Event 006
  and Event 012 setup remains runtime-owned and additive.
- No history file writes Event 012 origin flags, Soviet origin flags, or
  `liberation_origin`. The only Event 006-specific history-side character
  recruitment found is the expected dormant HBX civic-convention character.

No tag, country definition, state owner/controller/core, party, leader,
portrait, advisor, flag, idea, decision, technology, unit, industry, supply,
production, or AI file was changed by this registry audit. The registry itself
owns only static membership, exact provenance gates, and two Event 006 origin
wrappers.

## Validation evidence

Read-only checks performed:

- Parsed the CSV with `utf-8-sig`: 206 rows, 102 new rows, 91 reuse rows, 13
  overlays, 191 unique resolved tags, and only CHU/BIA duplicate tags.
- Compared the CSV-derived sets with every static array; all, Event 006-owned,
  and reuse sets were exact. Deduplicated CSV sets for all 14 regions matched
  the corresponding arrays exactly.
- Compared the exact registry trigger OR lists with the constants; no missing
  or extra carrier or overlap tag was found.
- Parsed the map-binding CSV for all 12 Africa overlap package IDs and checked
  the eight current-map-bound statuses listed above.
- Grepped all Event 012 consumers for Event 006 wrapper calls and
  `liberation_origin` writes; none were found. Registry carrier predicates and
  all 16 Africa origin package identities are present and consumed.
- Audited `history/countries` filenames and origin markers; no registered-tag
  history overwrite or cross-event origin grant was found.
- Consulted the required offline Paradox wiki core pages and vanilla script
  documentation for collections, scopes, triggers, effects, events, and
  script constants before this audit.

Not run: in-game load, live save testing, or map rewrite. No map write was in
scope. The installed HOI4 agent package exposes no Technology Tree Viewer, so
technology dependency visualization remains an unresolved tooling limitation;
the registry API does not own technology setup.

## Remaining risks and queued work

- IW-096/IW-107 (BIA) and IW-043/IW-046 (CHU) remain fail-closed until exact
  content and visual attestation is granted. Shared-tag package-ID mutexes must
  be retained when those rows are promoted.
- DYX, DZX, and EMX remain Africa overlap carriers in the canonical arrays but
  are not current-map selectable until their binding rows gain a unique state.
- COG/IW-101 remains an overlay-only Kongo route and must not become a
  standalone Event 006 release without a new identity decision.
- The Africa loader's preserved-tree path is safe but intentionally does not
  synthesize a no-tree fallback; a supported no-tree trigger would require a
  separate engine/API review.
- The global Event 006 runtime content-attestation gate is currently closed;
  this audit did not alter that parent-owned readiness decision.

No simplification or gameplay fallback was introduced. No rollback is needed;
only this handoff file was added.
