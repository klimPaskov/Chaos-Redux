# Event 006 Mediterranean tranche admission closeout

Date: 2026-07-16
Parent verdict: **READY for exact-scope commit**
Scope: IW-017 Corsica (`COR`), IW-018 Sardinia (`ARX`), IW-019 Sicily (`ASX`), and FORM-05 Mediterranean Island League (`MIX`).

> Later status note: this bounded Mediterranean verdict predates the completed
> slot-24/6002 runtime integration. Its statements that 6002 presentation is
> pending are historical. Audio 6001 remains blocked.

This is a bounded tranche verdict, not an Event 006 completion claim.

## Playable-package coverage

- `COR` reuses the registered vanilla Corsica identity. The adapter requires the
  tag to be absent and the exact Event 006 package identity. It never writes a
  COR history or country-definition replacement, loads the full Event 006 tree
  only when the current tree is exactly `generic_focus`, and restores only that
  reviewed generic-tree state during cleanup.
- `ARX` is the compact Sardinian island polity, distinct from vanilla `SPM` and
  its mainland Piedmont content. `ASX` is the compact Sicilian island polity,
  distinct from vanilla `TTS` and its mainland Two Sicilies content.
- Every package has identity, guarded setup, capital/anchor binding, forces,
  lifecycle ideas, values, founding missions, costed projects, incidents,
  host-settlement hooks, patron and network behavior, route logic, AI, leaders,
  commanders, portraitless advisers, diplomacy, expansion/settlement content,
  cleanup, and package-specific full-tree content.
- Force profiles remain data-driven: COR uses coastal-maritime profile 17 with
  tradition 53, navy, and no air force; ARX uses coastal-maritime profile 18
  with tradition 52, navy, and no air force; ASX uses regular-defectors profile
  19 with tradition 65, navy, and air force.

## FORM-05 coverage

- FORM-05 is a sovereign charter system, not an annexation formable. It creates
  no subjects, transfers no member states, grants no member cores, and does not
  absorb member armed forces or institutions.
- The charter has a 540-day failure deadline, three separately costed shipping,
  defense, and customs articles, sovereign consent from at least two live
  Event 006 island governments, a 300-day congress process, and a settled
  carrier capital.
- The post-formation maritime board has a 720-day failure deadline, three
  costed institutional projects, public-value requirements of at least 95, a
  live sovereign member requirement, ratification, breakdown, recovery, and
  costed reconvening.
- The decision audit corrected both manually activated deadline missions with
  fail-closed completion conditions and adverse timeout presentation. They no
  longer complete immediately after activation.

## Exact allocator and scenario admission

- Exact identity/absence wrappers, runtime adapters, compile-time content
  attestations, runtime preflight branches, scenario preflight branches, region
  02 planner gates, and automatic-capacity witnesses are present for all three
  packages.
- The compile-time set contains 11 admitted IDs across 10 disjoint reservation
  groups. The automatic bands remain exactly 3, 4, 5, 7, and 10; World Collapse
  remains 10.
- IW-017/IW-018/IW-019 use earliest bands 0/1/1 and anchors 1/114/115.
- The capacity proof rejects Event 5 opening-country, core-state, and host
  collisions. The synchronized allocator still reserves Event 5 and Event 6
  tags and states before optional territory and release.
- Host survival is evaluated over every selected anchor at once. If both
  Sardinia and Sicily are selected, Italy must own a third state outside both
  selected anchors; France likewise must retain a state outside Corsica.
- Every SCN-008 intensity iterates the full 138-entry ranked bound registry and
  attempts every viable candidate. Intensity continues to affect territory and
  forces, while scenario type controls the political setup.

Evidence:

- `006_iw017_iw019_allocator_admission_audit_2026_07_16.md`
- `.tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/
  high-chaos selectable packages, 138 ranked scenario packages, and the exact
  3/4/5/7/10 ladder.

## Collision and vanilla-identity evidence

The regenerated installed-environment audit covers vanilla, 122 Workshop
directories, eight embedded ZIP archives, and three sibling local mods. It
finds zero collision among 102 reserved Event 006 country tags and five Event 6
formable/cosmetic identifiers. It records the reviewed ARX-versus-SPM and
ASX-versus-TTS distinctions and retains COR as vanilla reuse.

Evidence:

- `../tag_audit/006_installed_tag_collision_audit_2026_07_16.md`
- `../tag_audit/006_installed_tag_collision_audit_2026_07_16.json`

## Visual and audio status

- Eight distinct fictional adult-male large portraits are runtime-wired at
  156x210. They were calibrated against the two binding protected portraits,
  reviewed in a contact sheet, decoded back from DDS, and use no small/adviser
  portrait derivatives.
- Protected portrait hashes are unchanged:
  - BAY Rupprecht: `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`
  - RHI Matthes: `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`
- Event 006 contains zero runtime file whose name is an advisor/adviser/dossier
  asset. All six Mediterranean gameplay advisers are portraitless.
- COR uses its vanilla flag family. ARX uses a researched flat Four Moors
  Sardinian civic design; ASX uses the researched flat 1848 Sicilian national
  colour. MIX uses a distinct fictional flat civic design. The complete ARX,
  ASX, and MIX flag ladders contain 45 TGA files.
- Package assets include eight focus icons and shines, eight decision icons,
  eight lifecycle ideas, and one report card. FORM-05 adds seven decisions,
  three ideas, one emblem, and one report card. Every runtime texture is
  registered and has a live consumer.
- This tranche added no audio. A later Event 006 tranche completed 6002
  playback; 6001 remains blocked on exact recording rights.

Evidence:

- `../../../assets/006_independence_wave/mediterranean_portraits_2026_07_16/manifest.md`
- `../../../assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/manifest.md`
- `../../../assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/manifest.md`

## Independent audit chain

- Country packages: `006_mediterranean_country_package_audit_2026_07_16.md`
- Focus trees: `006_mediterranean_focus_tree_audit_2026_07_16.md`
- Decisions and missions: `006_mediterranean_form05_decision_mission_audit_2026_07_16.md`
- Localisation: `006_mediterranean_localisation_audit_2026_07_16.md`
- Allocator/scenarios: `006_iw017_iw019_allocator_admission_audit_2026_07_16.md`
- Portrait production and review: `006_mediterranean_large_portraits_2026_07_16.md`

The localisation audit reconciled 482 consumers with 482 definitions, no
missing or duplicate keys, no working labels, no female identities or pronouns,
and no adviser-art claims. Both owned localisation files retain UTF-8 BOM.

## Simplifications, omissions, and blockers

- No gameplay or visual simplification was used inside this bounded tranche.
- No fallback portrait, flag, icon, focus route, formable behavior, AI package,
  localisation block, or advisor icon was substituted.
- The focus MCP renderer could not persist a render because its artifact store
  was full. The independent focus auditor therefore used direct source/graph,
  coordinate, parent, icon, reward, AI, and consumer checks. This is a tooling
  evidence limitation, not a content substitution.
- This tranche was source-audited and asset-decoded; it is not represented as
  an in-engine playthrough.
- Event 006 remains incomplete outside this tranche. FORM-06 through FORM-48,
  remaining country packages, animations, achievements, catalog reconciliation,
  and the full completion audit remain active work. The later slot-24/6002
  presentation tranche is complete with one dormant hidden-formable route.
