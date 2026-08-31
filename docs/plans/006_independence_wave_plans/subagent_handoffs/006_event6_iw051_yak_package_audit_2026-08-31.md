# Event 006 IW-051 Sakha/YAK package audit — 2026-08-31

## Disposition

`PATCHED LOCAL / HOLD FOR CENTRAL ADMISSION`.

The package has one fully evidenced, YAK-only setup defect and that defect is corrected below.

The package is still not Event 006 admitted: central adapter, content attestation, scenario preflight, and deterministic Join do not list `iw_051`, and identity/rights plus final portrait/flag receipts remain parent-owned blockers.

No central admission was widened, and no identity, rights, probability, map, origin, or protected-host gate was bypassed.

No live HOI4 session was run.

## Authority and evidence reviewed

Before opening or changing source, I read the required offline wiki pages in `paradox_wiki/` (data structures, triggers, effects, modifiers, localisation, scopes, on actions, event, decision, idea, AI, country creation, national focus, character, portrait, cosmetic tag, state, map, unit, and technology references), the installed vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, and the applicable Chaos Redux skills for subagents, events, focus trees, decisions, assets, portraits, and ComfyUI.

The accepted authority set was checked in `docs/specs/006_independence_wave_specs/`, especially `specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `research/006_package_research_resolution.csv`, `matrices/006_candidate_country_registry.csv`, and `research/006_state_anchor_and_reservation_groups.csv`.

The accepted binding is `IW-051 / Sakha / YAK / RG-574 / state 574 Yakutsk`, with compact anchor 574, optional extensions 644/876/877, `mountain_frontier` force archetype, and the registered vanilla tag rather than the historical `BYX` candidate field.

## Narrow source correction

Changed `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1093`:

```text
before: set_temp_variable = { independence_wave_candidate_archetype = constant:independence_wave_package_archetype.nomadic_or_dispersed }
after:  set_temp_variable = { independence_wave_candidate_archetype = constant:independence_wave_package_archetype.mountain_or_frontier }
```

The planner copies this candidate value into `pending_archetype` in `common/scripted_effects/006_independence_wave_package_planner_effects.txt:823-827`, and setup later assigns it to `independence_wave_package_archetype` in `common/scripted_effects/006_independence_wave_effects.txt:727-734`.

The YAK `can_initialize` and prepared gates require `mountain_or_frontier` in `common/scripted_triggers/006_independence_wave_siberian_package_triggers.txt:757-774` and `:840-901`, while the accepted IW-051 force row requires `mountain_frontier`; the old loader value therefore made the local package unable to satisfy its own setup contract.

This correction changes only the YAK planner archetype and does not add a candidate, alter weights, reserve states, or enter the central runtime path.

The same source file contains an unrelated pre-existing IW-177 diff from another agent; stage only the IW-051 hunk when committing.

## Country package coverage checklist

| Surface | Finding | Evidence |
| --- | --- | --- |
| Tag and country identity | Reuses registered vanilla `YAK`; no new tag or duplicate registration | Vanilla `common/country_tags/00_countries.txt:221-229`, `common/countries/Yakutia.txt`; registry/spec rows |
| Vanilla history and anchor | Capital/owner/core baseline is present and untouched; `574` is Yakutsk | Vanilla `history/countries/YAK - Yakutia.txt`; `history/states/574-Siberia 1.txt` |
| Package constants | Present and scoped to IW-051/YAK pressure, duration, cost, and politics | `common/script_constants/006_independence_wave_constants_registry.txt:7547,8453-8522` |
| Package triggers | Present with tag, package, origin, roster, host, anchor, route, focus, force, lifecycle, and completion gates | `common/scripted_triggers/006_independence_wave_siberian_package_triggers.txt:687-913` |
| Package effects | Present for politics, four governments, focus hooks, roster/portrait checkpoint, setup, validation, and generation-safe cleanup | `common/scripted_effects/006_independence_wave_siberian_package_effects.txt:1373-1877` |
| Focus tree | Shared tree hooks are present and rendered/inspected; no new YAK tree was invented | `common/national_focus/006_independence_wave_focus.txt:139,192,226,1461,1732`; shared focus effects |
| Decisions and mission | One YAK category, holding mission, and ten paid projects are localised and gated | `common/decisions/006_independence_wave_siberian_decisions.txt:1746+`; `localisation/english/006_independence_wave_siberian_l_english.yml:311-357` |
| Ideas and politics | Seven YAK ideas, four route governments, party names, and cosmetic tags are wired | `common/ideas/006_independence_wave_ideas_registry.txt:3869-3912`; effects/localisation |
| AI | Four YAK strategy profiles exist and are setup-gated; no new quantitative claim is made | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:2785-2851` |
| Localisation | YAK party, cosmetic, idea, mission, decision, and tooltip keys are present; one non-blocking “a arctic” wording typo remains | `localisation/english/006_independence_wave_siberian_l_english.yml:225-357` |
| Assets | Runtime portrait and four route flag ladders exist only as source-placeholder/provisional evidence; no final identity/rights receipt | `interface/006_independence_wave_portraits_registry.gfx:126-135`; `gfx/leaders/006_independence_wave/`; `gfx/flags/YAK_INDEPENDENCE_WAVE_*` |
| Formable boundary | No IW-051/FORM-14 implementation exists; YAK prepared gate explicitly excludes unregistered formable families | `common/scripted_triggers/006_independence_wave_siberian_package_triggers.txt:876`; formable registry search |

## Map, state, and host safety

Vanilla state `574` is Yakutsk, owned by SOV with SOV/YAK cores, capital VP `10641`, and the accepted protected-host remnant is SOV state `219`.

Optional states `644` Kolyma, `876` Udachny, and `877` Verkhoyansk remain SOV-owned and YAK-core in vanilla history; they are claims/extensions, not added to the compact anchor.

The current package binding is `fixed_anchor_compact` with `574` as the only compact anchor and `644|876|877` as optional extensions, matching `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`.

Read-only `hoi4_map_inspect` covered states 574/644/876/877 and reported valid selected memberships/networks with no selected-state blocker; `hoi4_map_render` rendered victory points, resources, buildings, supply nodes, railways, and ports with validation passed.

The map inspect global failure is workspace-wide floating harbor/port, building-position, and unrelated localisation noise; no map write was made and no selected YAK state was changed.

## Vanilla politics, leader, portrait, flag, advisors, and parties

Vanilla YAK history starts with Pavel Pevznyak (`YAK_pavel_pevznyak`, stalinism leader expiry 1943.1.1.1) and Anatoly Pepelyayev (`YAK_anatoly_pepelyayev`, oligarchism leader expiry 1960.1.1.1); the accepted 1936 package roster requires Pavel only.

The local source portrait candidate is grounded Pavel research and a wired 156x210 placeholder, but it is not a final rights-cleared portrait receipt; the package applies it only after the parent-owned `independence_wave_iw_051_identity_rights_cleared` flag and roster checkpoint.

Vanilla YAK ideology flag ladders are complete and unmodified; generated `YAK_INDEPENDENCE_WAVE_CIVICX`, `ARCTICX`, `SOCIALISTX`, and `EMERGENCYX` ladders are alternate-history route evidence marked `needs_user_review`, not a neutral 1936 replacement.

No advisor, commander, new leader, map binding, historical flag, fallback portrait, or central attestation was invented.

## Focus, decisions, ideas, and asset evidence

The shared focus tree `independence_wave_focus_tree` was inspected and rendered through HOI4 MCP with 184 focuses, 195 connectors, zero crossings/intersections, zero diagnostics, and validation passed; its sole warning is an unrelated vanilla localisation reference.

YAK hooks cover convening the Arctic council, registering communities, integrating river guards, settling former-host ledgers, and opening the Lena-Arctic corridor, with additive/full-framework loading owned by shared focus effects.

The ten local projects cover depots, guards, communities, host ledgers, constitutional autonomy, land compact, Lena councils, emergency command, durable sovereignty, and the network corridor; all corresponding name/description/effect keys were checked.

The local seven-idea set uses existing generic idea pictures and does not claim missing custom icons are complete.

Asset evidence is archived under `docs/assets/portraits/006_independence_wave/` and `docs/assets/006_independence_wave/iw051_sakha_flags_2026_08_15/`; the flag handoff records missing prompt provenance, non-standard DDS evidence, crop loss of the red field, and parent review required.

## Military, technology, industry, supply, and production

Vanilla YAK has two research slots, vanilla starting technology, no active OOB (`#oob = "YAK_1936"` is commented), and no package-local navy/air setup.

The accepted force mapping is p51 `mountain_frontier`, cold-weather infantry/cavalry/river guards, with engineers, reconnaissance, and cold-weather logistics first; local setup checks mapping generation, application, reinforcement count, and no navy/air path.

No army, equipment, production, infrastructure, supply, technology, or map-balance write was made.

## AI and probability

The four YAK strategy IDs are `independence_wave_yak_arctic_survival`, `independence_wave_yak_host_restraint`, `independence_wave_yak_settled_compact`, and `independence_wave_yak_emergency_guard`; all are original-tag and setup/profile gated.

`hoi4_probability_inspect` found the four strategy factors as a source with no weighted surfaces and validated the ten-project `mission_ai_will_do` pool with ten candidates, complete pool, fifteen required inputs, and zero unresolved inputs; the requested decision adapter was remapped by the tool to the mission adapter.

The required callable `chaosx_ai_probability_auditor` is unavailable in this runtime, so no baseline/after probability compare or balance claim is made; the existing artifact references are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f992c00c29dbd0112b4806af07e40fa781bd0fd0f4af48c5ad16ed51251e3992/51bdb74e781ccb7ca000181555cce2a57c094112c4e279e65c0b30a1af0fbf10/probability-inspect-c5fef71b5a54.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c622fdcdca6b8b6e518b33a9a615c681ef831bbcc21e2c8dc8879c0d8f8e240a/161ca1f70fd1a52d14175c6446e9cfacaca4a3f34b079b98041cea6f640844e2/probability-inspect-f48e79327194.json`.

## Central admission, FORM-14, and no-pre-event gating

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` has no `iw_051`, `YAK`, or Sakha branch in runtime adapters, content attestation, or preflight.

`common/scripted_effects/006_independence_wave_join_effects.txt` and the Join callbacks have no IW-051 fixed candidate, so planner loader/weight rows are not admission and must not be promoted locally.

No FORM-14/Siberian Federation route is implemented; keep that boundary unchanged.

The package predicate requires active package content, package ID `iw_051`, original tag `YAK`, and excludes Soviet-collapse origin flags; initialization requires parent-provided identity/rights, origin, anchor, former-host protected-state, roster, focus, force, lifecycle, and capital checks.

The identity flag `independence_wave_iw_051_identity_rights_cleared` is never set by the YAK package, and no category, mission, cost, queue, or package setup can appear before the prepared gates pass.

## Blockers and next owners

- Parent Event 006 central owner: review and, only after receipts, add IW-051 to the central runtime adapter, content attestation, scenario preflight, and deterministic Join surfaces.
- Parent identity/rights owner: publish `independence_wave_iw_051_identity_rights_cleared` after a defensible Pavel/institution identity and rights receipt; the current source-placeholder is not that receipt.
- `chaosx_portrait_creator`: produce and validate the final HOI4-style Pavel portrait or explicitly retain blocked placeholder mode; agents do not operate RunPod.
- Asset/identity owner: resolve neutral 1936 YAK flag policy or repair and approve the generated route ladder evidence; current route files remain `needs_user_review`.
- Map/host owner: prove the protected SOV remnant state 219 and installed-build state rebind after release; static history and selected-state MCP evidence are not a live transaction proof.
- AI owner: run the required same-scenario baseline/after compare through `chaosx_ai_probability_auditor` when that route is available.
- FORM-14 owner: no work required for this package; preserve the explicit exclusion.

The former “a arctic” localisation typo at `localisation/english/006_independence_wave_siberian_l_english.yml:315` is corrected to “an arctic” in the current source.

## Validation and handoff

`python -B .tools/audit_event6_allocator.py` exited 0 with 40 runtime adapters, 32 attested packages, and protected former-host state 219 retained.

`python -B .tools/audit_event6_country_api.py` exited 0 with zero missing or duplicate resolved tags.

`python -B .tools/audit_event6_flags.py --strict` exited 0 with 102 complete Event 006 flag families.

Fresh focus inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69edebd0e6b0e8528d065d89f4b9872663c93f95e10f00ce3edcf42af7610730/012d2af0dbb270c016237a17b5a5f598226ef16fea0a7b941a33908fc7154d80/focus-inspect.3e9e27b9b2b333a1.json`; the corresponding fresh focus render also passed with the same unrelated vanilla localisation warning.

Event inspect/render were partial because of workspace-wide deferred helper/lifecycle diagnostics; no scoped YAK blocker was returned.

No Git commit was created because the shared worktree contains unrelated edits, including an IW-177 hunk in the changed source file; the parent should stage the single IW-051 line and this handoff only.

### Simplifications and omissions

No unapproved fallback, invented leader, invented map binding, invented flag, central attestation, new formable, or live-game claim was used.

Final admission, identity/rights, final portrait, final flag policy, protected-host transaction proof, and the mandatory probability compare remain intentionally unresolved and are not represented as complete.
