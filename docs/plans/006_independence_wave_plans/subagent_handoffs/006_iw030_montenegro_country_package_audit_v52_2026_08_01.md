# Event 006 IW-030 Montenegro package tranche v52

## Scope

This tranche adds a bounded runtime package for the registered vanilla `MNT` carrier, state 105, and reservation group `RG-105`. It does not create a country, history file, flag, portrait, advisor icon, formable, or new tag.

## Implemented surfaces

- `common/script_constants/006_independence_wave_montenegro_constants.txt` centralizes politics, mountain cohesion, crown legitimacy, crisis duration, and AI tuning.
- `common/ideas/006_independence_wave_montenegro_ideas.txt` defines the negative and mature lifecycle ideas plus constitutional, workers' council, crown, and emergency route ideas.
- `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt` proves identity, state 105 host survival, the vanilla three-character roster, four government routes, host routes, Danubian ambition, league membership, p30 force mapping, lifecycle, AI, and array alignment.
- `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt` installs baseline laws, the shared full focus framework, public and MNT-specific ledgers, route governments, host settlement, force mapping, AI, and cleanup.
- `common/decisions/006_independence_wave_montenegro_decisions.txt` adds one timed founding mission and ten concrete-costed actions.
- `common/ai_strategy/006_independence_wave_montenegro.txt` adds mountain survival, host restraint, settled-frontier, and emergency-guard strategies.
- `events/006_independence_wave.txt` owns synchronous recruitment of the vanilla MNT roster through `chaosx.nr6.350`.
- `localisation/english/006_independence_wave_montenegro_l_english.yml` provides finished English party, idea, decision, and tooltip text with a UTF-8 BOM.
- `docs/events/006_independence_wave/montenegro_package.md` records the runtime contract and blocker disposition.

## Source and admission status

Vanilla MNT history is identity-compatible and remains untouched. Vanilla state 105 and its map geometry pass the bounded map inspection. Vanilla MNT flags can be reused for the base identity. No Event 006 advisor art is used.

The package is **NOT ATTESTED**. The vanilla `MNT_kristo_popovic` portrait is a generic European texture, so it cannot satisfy the grounded real-person portrait policy. The two remaining period characters also require source, ownership, date-fit, and identity-preserving HOI4 repaint evidence before runtime admission. The shared Event 006 focus tree still has fourteen global blocking geometry diagnostics. The package must stay outside `has_independence_wave_runtime_package_content_attestation_for_execution_id` and scenario preflight until both gates clear.

## Validation

- Vanilla state 105 map inspection passed.
- New localisation file was rewritten with a UTF-8 BOM after the MCP localisation check identified the missing BOM.
- The central allocator and protected-tag surface audits remain the parent-owned validation gates.
- No in-game launch or live save test was performed.

## Follow-up

1. Source a real male MNT-era leader or institutional leadership solution that is not generic, then retain the unchanged archival source, exact head-and-shoulders crop, source-locked HOI4 repaint, 156x210 processing, independent likeness/style/provenance audit, and DDS/GFX handoff.
2. Re-audit the MNT roster and package after the portrait decision.
3. Resolve the global focus geometry blocker or record an accepted focus admission decision before adding IW-030 to content attestation.
4. Do not add advisor icons or copy vanilla MNT history into the mod.

## Country package coverage checklist

| Surface | Status | Evidence and review boundary |
| --- | --- | --- |
| Tag registration and identity | Covered for reuse | `common/country_tags/00_countries.txt` registers vanilla `MNT = "countries/Montenegro.txt"`; the Event 006 registry constants include `MNT` in `registered_reuse_tags`, `selectable_bound_tags`, `registered_reuse_bound_tags`, and `balkans_and_danube`; no new tag is required. |
| Planner and reservation binding | Registered but not executable | `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt:can_plan_independence_wave_package_iw_030` and `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt:independence_wave_load_package_iw_030` bind MNT, state `105`, region `balkans_danube`, and `RG-105`; the dormant-tag legacy content flag cannot be granted to an absent country, so an exact MNT admission wrapper remains required. |
| Release and cleanup identity | Covered in adapter | `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt:is_independence_wave_mnt_package` proves `original_tag = MNT` and package id `iw_030`; `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt:independence_wave_cleanup_iw_030_montenegro` owns mission, decision, idea, variable, and flag cleanup. |
| Country definition and history | Safe vanilla reuse | Vanilla `common/countries/Montenegro.txt` and `history/countries/MNT - Montenegro.txt` remain untouched; the history supplies capital state `105`, three research slots, native starting technologies, politics, and the three vanilla characters. No replacement history file or duplicate country definition was added. |
| State and map anchor | Covered, runtime-gated | Vanilla `history/states/105-Montenegro.txt` remains the compact anchor with MNT core, YUG host ownership, victory points `9809` and `9821`, naval bases, resources, and local supply; the bounded `hoi4.map_inspect` for state `105` passed. |
| Politics, parties, and laws | Covered in adapter | `independence_wave_initialize_mnt_politics` and `independence_wave_ensure_mnt_baseline_laws` in `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt` establish four route-compatible party names and the vanilla civilian economy, export focus, and volunteer-only baseline. |
| Leaders and roster | Recruitment wired, provenance incomplete | `events/006_independence_wave.txt:chaosx.nr6.350` synchronously recruits `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, and `MNT_blazo_dukanovic`; `has_independence_wave_mnt_command_roster` checks the three-character roster and commander roles. Portrait provenance, ownership, date fit, and identity-preserving repaint evidence remain open for all live route consumers. |
| Portraits and gender metadata | Blocking visual gap | Vanilla `MNT_kristo_popovic` uses generic `GFX_portrait_europe_generic_land_19`; this violates the grounded real-person portrait requirement for a live leader role. Jovanovic and Dukanovic have named vanilla portraits but still need source, ownership, date-fit, and identity-preserving repaint evidence before admission. No opposite-gender pairing was introduced. |
| Flags and cosmetic identity | Base covered, variants open | Vanilla MNT base and ideology flags are present and may be reused while the carrier identity remains MNT; no mod-side flag asset or cosmetic-tag replacement was added. Historical or route-specific variants remain source-review work. |
| Advisors and high command | Intentionally not added | No MNT-specific advisor, high-command portrait, or advisor icon is referenced by the adapter, so no missing advisor art is hidden behind the readiness gate. |
| Focus tree | Adapter wired, shared geometry blocks admission | Setup assigns `independence_wave_focus_assignment.full_framework` and the shared `independence_wave_focus_tree`; no generic-focus substitution or MNT-specific tree was claimed. `hoi4.focus_inspect` reported `passed: false` with 184 focuses, 223 connectors, 45 crossings, 7 node intersections, and 28 long connectors, summarized as 14 blocking diagnostics. |
| Decisions and mission | Covered | `common/decisions/006_independence_wave_montenegro_decisions.txt` defines the timed founding mission `independence_wave_mnt_hold_mountain_compact_together` plus ten costed projects for depots, guards, administration, host ledgers, four government routes, sovereignty, and the Balkan corridor. |
| Ideas and lifecycle | Covered | `common/ideas/006_independence_wave_montenegro_ideas.txt` defines the divided/mature lifecycle ideas and four route ideas; setup, route effects, failure, and cleanup are connected through the MNT effect and trigger contracts. |
| Formable and ambition hooks | Shared registry only | `independence_wave_mnt_focus_open_balkan_corridor` sets `independence_wave_unlock_formable_discovery`; the shared formable registry provides Balkan and Danubian families. No MNT-specific formable tag or automatic family registration is present, matching the compact-and-negotiated expansion contract. |
| Starting force and command | Contract covered, runtime-dependent | The adapter loads the dynamic p30 mapping and applies it only after the synchronous MNT roster is present; `common/script_constants/006_independence_wave_force_package_constants.txt:p30` maps to `mountain_frontier` and five reinforcement pathways. No separate MNT OOB file is copied. |
| Technology, industry, supply, and production | Vanilla baseline plus dynamic force | Vanilla MNT starts with three research slots and its native 1936 technology set; the adapter adds no unsupported technology or production line. Baseline laws, state resources, local supply, and p30 force mapping are the only package-owned setup surfaces. The installed MCP exposes no Technology Tree Viewer, so a technology render remains unresolved. |
| AI and playability | Covered in package, admission pending | `common/ai_strategy/006_independence_wave_montenegro.txt` adds mountain survival, host restraint, settled frontier, and emergency guard strategies using centralized constants; the setup trigger requires the AI profile and all force/lifecycle gates. Live playability cannot be claimed until the package passes the closed admission gates. |
| Localisation and assets | Localisation covered, source manifest open | `localisation/english/006_independence_wave_montenegro_l_english.yml` contains party, idea, decision, and tooltip keys and now has a UTF-8 BOM; shared cost localisations resolve globally. No MNT-specific portrait/flag/advisor asset manifest exists because the carrier assets are either vanilla reuse or still blocked on source review. |

## File surface checklist

- `common/script_constants/006_independence_wave_country_registry_constants.txt` and `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt` contain the registered-reuse MNT identity and region membership.
- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt` and `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt` contain the IW-030 planner, weight, reservation, and state-105 binding.
- `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt`, `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt`, `common/ideas/006_independence_wave_montenegro_ideas.txt`, `common/decisions/006_independence_wave_montenegro_decisions.txt`, and `common/ai_strategy/006_independence_wave_montenegro.txt` form the package-owned runtime surface.
- `events/006_independence_wave.txt:chaosx.nr6.350` is the event-owned roster handoff and must remain the only synchronous MNT recruitment site.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` calls the MNT setup, final-validation, and cleanup adapters, while `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` currently admits the adapter id but not IW-030 content or scenario preflight.
- `localisation/english/006_independence_wave_montenegro_l_english.yml` and `docs/events/006_independence_wave/montenegro_package.md` are aligned with the package identifiers and blocker wording.
- Vanilla reference surfaces remain `common/country_tags/00_countries.txt`, `common/countries/Montenegro.txt`, `history/countries/MNT - Montenegro.txt`, `history/states/105-Montenegro.txt`, `common/characters/MNT.txt`, `common/national_focus/generic.txt`, and `common/national_focus/yugoslavia.txt`; none should be copied into the mod for this reuse package.

## Missing or stale admission surfaces

1. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:has_independence_wave_runtime_package_content_attestation_for_execution_id` has no `iw_030` branch, so the package cannot execute through the compile-time content gate.
2. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:is_independence_wave_runtime_package_preflight_ready` has no IW-030/MNT identity pair, and `is_independence_wave_scenario_package_preflight_ready` has no IW-030 exact wrapper branch.
3. `common/scripted_triggers/006_independence_wave_package_triggers.txt` has no `is_independence_wave_exact_package_iw_030_tag_available` wrapper; adding one before the portrait and focus audits clear would weaken readiness and is intentionally deferred.
4. `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt:can_plan_independence_wave_package_iw_030` still calls the legacy `MNT = { is_independence_wave_candidate_tag_available = yes }` path, which cannot grant a country flag to a dormant absent tag; the exact package wrapper must replace or supersede that path as part of a parent-owned admission change.
5. The shared `independence_wave_focus_tree` geometry diagnostics are global but directly block IW-030 because the MNT adapter requests `full_framework`; no local MNT focus patch can safely mask them.
6. The MNT leader portrait/source package is incomplete, with the generic Popovic texture a hard blocker and Jovanovic/Dukanovic provenance evidence still missing from the handoff.

## Narrow patch disposition

No gameplay patch was applied by this audit. The only change in this tranche is this documentation handoff amendment, and no admission flag, attestation branch, exact wrapper, scenario preflight branch, or fallback portrait was added.

## Validation evidence and skipped checks

- `python -B .tools/audit_event6_allocator.py` passed with the parent-owned allocator counts and continued to report only the previously attested package set, excluding IW-030.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` reported zero external country-definition or identity-surface collisions in the protected Event 006/Soviet tag audit.
- `hoi4.map_inspect` for state `105` passed all bounded state/map checks; artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72009e53731423fb0dc8446e9a007272dcc8b99468e90b1cec716c6cae276954/4d72acf222083092f2661f9230c99ac788be53a20b4425397e60232bfeaf24de/map-inspect.2444266cacbb3790.json`.
- `hoi4.focus_inspect` for `independence_wave_focus_tree` returned `passed: false` with 14 blocking diagnostics; artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd8e1f88cdbcccbb0c924a2da58d87e8a4eac731c4860ab13a032780d665b9ac/fa0127171c9352baca2387ea255299b28a402cb1527faefd3827c3151d503b23/focus-inspect.e1bc52a97e7612c9.json`.
- The initial MCP localisation check caught a missing BOM on the new MNT localisation; the file was rewritten with a UTF-8 BOM and the current bytes begin `239,187,191`.
- No in-game launch or save test was performed, as runtime consumer validation belongs to the parent/user boundary.
- No Technology Tree Viewer is installed in the current HOI4 MCP package, so technology-tree rendering could not be performed; no technology rewrite was attempted.
- Portrait source provenance, ownership, date-fit, and repaint audits were not fabricated locally and remain an asset/source-research handoff.

## Current handoff recommendation

Keep IW-030 registered for planning and adapter review, but leave it outside content attestation, normal preflight, and scenario preflight. Admit only after a sourced non-generic male leadership solution and full portrait package are independently audited, the shared focus geometry receives an accepted resolution, and the parent adds exact MNT identity/preflight wrappers without restoring the dormant-tag flag gate.
