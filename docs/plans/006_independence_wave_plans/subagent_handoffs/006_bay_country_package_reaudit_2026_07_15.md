# Event 006 IW-009 Bavaria country-package reaudit

> **Portrait-specific supersession (2026-07-16):** Generated fictional
> portrait hashes and acceptance evidence in this audit are superseded by the
> male-HOI4 package manifest and final independent audit. The approved
> Rupprecht exemption and unrelated gameplay findings remain current within
> their stated scope.

Date: 2026-07-15

Auditor: `event6_bay_package_reaudit`

Scope: `IW-009` Bavaria (`BAY`) only. Read-only audit of the current working
tree after route-matrix remediation and round-number balancing. This handoff is
the auditor's only file change.

Parent resolution: the exact `IW-009` runtime content-attestation branch and
the exact `IW-009`/`BAY` SCN-008 preflight branch described below have been
applied. No other package ID was admitted through this certification.

## Verdict

**CERTIFY `IW-009` for independent automatic static content attestation.**

**CERTIFY `IW-009` for independent SCN-008 static content attestation.**

The package does not depend on `FORM-01`, `FORM-02`, `FORM-03`, or `FORM-04`.
Its South German content is a package-owned ambition and diplomatic settlement,
not a shared formable transaction. Bavaria therefore does not need to wait for
any of those four families before its exact package-ID branches are admitted.

Blocking findings: **0**. Major findings: **0**. Minor findings: **0**.

At audit time, the two dispatcher triggers were intentionally fail-closed. The
parent resolution above implements the certified exact branches while leaving
every unaudited package ID closed.

## Exact admission boundary

The parent may add only these independently justified branches while leaving
all unaudited package IDs fail-closed:

1. In the automatic content-attestation trigger, admit
   `independence_wave_execution_package_id = constant:independence_wave_package_id.iw_009`.
   The surrounding preflight already requires a registered runtime adapter,
   a dormant/nonliving origin-safe country, and the exact `IW-009`/`BAY`
   identity at
   `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:33-65`.
2. In the SCN-008 preflight trigger, admit only the conjunction of
   `independence_wave_scenario_dispatch_package_id = constant:independence_wave_package_id.iw_009`
   and `is_independence_wave_exact_package_iw_009_tag_available = yes`. The
   scenario registry ranks `IW-009` at
   `common/scripted_effects/006_independence_wave_scenario_effects.txt:163-168`
   and calls the package preflight before reservation at `:379-411`.
3. Do not add `independence_wave_package_content_ready` to dormant BAY history,
   do not add a formable readiness condition, and do not attest `IW-008` or any
   other package through the BAY branch.

The exact runtime adapter is already registered at
`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-18`,
and setup, final validation, and cleanup are already called by the central
dispatcher at
`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-34`.

## Identity, territory, and collision evidence

- The accepted registry row is `IW-009`, reused vanilla tag `BAY`, automatic
  only while not living, anchor/compact states `52|53|54`, reservation group
  `RG-52-53-54`: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:10`
  and `research/006_package_research_resolution.csv:10`.
- The installed-game binding remains valid: state 52 is localized Oberbayern
  and contains Munich, state 53 is Niederbayern, and state 54 is Franken. All
  three installed state histories carry BAY cores. The current binding record
  is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:10`.
- Package loading publishes the exact registered tag, anchor, host, region,
  depth, archetype, and reservation group at
  `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:114-127`.
  Reservation takes state 52 first and treats 53 and 54 as trimmable compact
  states at `:298-306`; the shared allocator checks host loss capacity for the
  anchor and each optional state at
  `common/scripted_effects/006_independence_wave_package_planner_effects.txt:276-330`.
- Vanilla registers `BAY = "countries/Bavaria.txt"`; Chaos Redux adds no BAY
  country-tag definition, country definition, country-history override, or
  duplicate `BAY_rupprecht_of_bavaria` character record. The installed audit
  reports all 91 registered-tag reuse rows present in vanilla and zero reserved
  custom-tag collisions at
  `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_15.md:22-27,72-76`.
  `BAY` is therefore an intentional vanilla reuse, not an Event 006 tag claim.
- Event 005 has no BAY origin/tag row. The ordinary and Liberations-cluster
  capacity witness additionally applies the shared Event 005 country, anchor,
  and host exclusion checks at
  `common/scripted_triggers/006_independence_wave_triggers.txt:605-629`.

## Route and formable evidence

The current source matches the accepted implementation decision at
`docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_package_implementation_map.md:357-368`.

- Setup publishes constitutional, popular/labor, traditional/restoration, and
  emergency-military routes at
  `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:608-620`.
  It explicitly clears patron-client availability, sets the persistent Radical
  Sovereignty exclusion, and clears radical availability at `:614-616`.
- The prepared proof requires those exact four routes, requires patron and
  radical absence, and proves the exclusion at
  `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:266-280`.
  The package-government predicate contains exactly those four governments at
  `:156-163`.
- The Open Sovereignty evolution honors the exclusion and actively clears a
  stale radical route at
  `common/scripted_effects/006_independence_wave_evolution_effects.txt:280-295`.
  The removed BAY patron and radical decisions, installers, ideas, government
  flags, AI conditions, and localisation identifiers are absent from the
  current `common/`, `events/`, Event 006 package localisation, and package doc.
- Setup clears selected/registered formable state and sets only
  `independence_wave_bay_south_german_ambition` at
  `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:621-629`;
  the prepared proof requires both formable flags absent at
  `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:281-286`.
- The mutually exclusive South German restoration and wider German claim
  decisions are at
  `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt:478-521`.
  The restoration path closes the vanilla German-reunification decision without
  creating another tag, while cleanup restores that decision only if this path
  closed it at
  `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:740-746`.
- The package high-chaos action remains a one-shot regional action, not a fifth
  government. Its trigger requires regional-power status, the shared high-chaos
  unlock, and Open Sovereignty at
  `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:165-175`;
  its decision keeps the settled government in force and pays a major security
  cost at
  `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt:562-585`.

## Gameplay, balance, AI, and repeat safety

- BAY receives the accepted shared full focus framework at
  `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:608-624`;
  its proof requires the full assignment at
  `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:263-267`.
  This is not a fallback to the vanilla generic tree.
- The package has 15 entries: one founding mission and 14 decisions, all with
  `ai_will_do`, at
  `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt:300-587`.
  All 15 name and description pairs resolve in the package localisation.
- Round-number tuning starts Civic Settlement at 25 and Mountain Security at
  30, with both stable at 60; minor/standard/major/decisive changes are
  10/15/20/25 at
  `common/script_constants/006_independence_wave_rhineland_bavaria_constants.txt:15-30`.
  The no-host baseline projects reach 65 civic and 70 security in 315 serialized
  days (treasuries +20 civic, passes +20 security, companies +20/+20), leaving
  165 days inside the 480-day mission. Those projects pay real administration
  or security costs and are serialized by
  `has_independence_wave_bay_active_package_project` at
  `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:132-145`.
- The shared starting-force mapping is `regular_defectors`, military tradition
  75, reinforcement mask 1676, and air-inheritance mask 2 at
  `common/script_constants/006_independence_wave_force_package_constants.txt:78-86,292-300,506-514,720-728`.
  Setup calls only the shared mapping and dynamic force effects at
  `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:630-634`;
  there is no BAY OOB or direct free-unit loop.
- Six package ideas implement one founding/mature lifecycle spirit plus one of
  four mutually exclusive route spirits at
  `common/ideas/006_independence_wave_rhineland_bavaria_ideas.txt:96-136`.
  The setup proof requires the lifecycle, force, and AI results at
  `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:287-296`.
- Seven BAY AI strategy plans are exact-tag/origin/setup locked and abort when
  their conditions end at
  `common/ai_strategy/006_independence_wave_rhineland_bavaria.txt:68-133`.
  The remediated civic and mountain profiles test only accepted governments.
- Cleanup removes the mission, every package decision and package idea, both
  visible variables, every BAY package state flag, the radical exclusion, and
  setup/lifecycle completion markers at
  `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:740-795`.
  Generated institutional characters and static advisors are guarded against
  duplicate creation/recruitment; hidden setup event `chaosx.nr6.10` recruits
  the three exact advisor records at `events/006_independence_wave.txt:51-84`.

## Characters, portraits, flags, and localisation

- `BAY_rupprecht_of_bavaria` is reused, never duplicated. Availability requires
  that BAY still has him and GER does not at
  `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:81-85`.
  The traditional installer promotes him only through the restoration route and
  otherwise uses the institutional State Council at
  `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:507-520`.
- The State Council, mountain commandant and distinct small commander portrait
  are registered at
  `interface/006_independence_wave_region_01_portraits.gfx:49-58`; the three
  advisor dossiers are registered at
  `interface/006_independence_wave_nwe_advisors.gfx:23-32`. Their installed DDS
  files exist at the documented 156x210, 50x67, and 65x67 tiers. Independent
  contact-sheet review found the BAY council and commandant consistent with the
  restrained HOI4 portrait treatment and distinct from one another.
- The approved historical sprite points to the required unchanged path at
  `interface/006_independence_wave.gfx:57`. Current SHA-256 for
  `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` is
  `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`,
  exactly matching the accepted ledger at
  `docs/assets/006_independence_wave/northern_western_europe_source_manifest.md:215`
  and `portrait_regeneration_2026_07_15/portrait_package_hashes.sha256:129`.
  The file is tracked and unchanged in the current working tree. Visual review
  also confirmed the approved decoded DDS against the c.1916 Grainer identity
  source and rejected first edit.
- The source manifest documents the white-blue civic family, dynastic route
  distinction, and historical references at
  `docs/assets/006_independence_wave/northern_western_europe_source_manifest.md:74,125-146`.
  The installed vanilla BAY family is complete: communism, democratic, fascism,
  and neutrality at 82x52, 41x26, and 10x7, for 12 valid 32-bit TGA files. No
  vanilla flag binary is copied into Chaos Redux.
- The package localisation is UTF-8 with BOM, has no legacy `:0` keys, and has
  no missing BAY decision, idea, character, advisor, or advisor-trait keys. The
  crisis numbers and decision deltas at
  `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml:101-130`
  match the current round-number constants and effects.

## Audit boundary and completion statement

The HOI4 MCP inspection family was not exposed in this agent session, so no MCP
render artifact is claimed. The audit used the required offline wiki pages,
installed official documentation, installed vanilla BAY/state/character/flag
precedents, current Chaos Redux source, manifests, hash ledgers, and independent
visual/static checks.

No gameplay fallback, placeholder identity, borrowed formable, omitted BAY
route, missing localisation, missing AI path, or missing visual asset was found.
No simplification was introduced by this audit. Overall Event 006 completion is
not claimed; this certification is strictly the `IW-009` package admission
boundary described above.

Skills used: `chaos-redux-events`, `chaos-redux-event-assets`,
`hoi4-focus-trees`, `hoi4-decisions-missions`, and `chaos-redux-subagents`.
No skill was created or updated.
