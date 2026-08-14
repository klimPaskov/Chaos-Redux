# IW-051 Sakha/YAK package audit handoff

Date: 2026-08-14.

Disposition: blocked and fail-closed; no country gameplay source files were changed.

This is an audit handoff, not an admission claim. YAK must not be added to the Event 006 runtime pool until the gates below are resolved and the parent-owned admission, attestation, preflight, and Join surfaces accept the package.

## Accepted package contract

| Surface | Evidence | Finding |
| --- | --- | --- |
| Registry | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:52` | `IW-051` is Sakha, registered tag `YAK`, disposition `reuse_registered_tag`, pool policy `automatic_pool_ready_if_not_living`, anchor state `574`, Yakutsk, reservation group `RG-574`. |
| Research resolution | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:52` | The provisional government must be a specifically sourced local institution; a sourced real male period leader is required when valid, otherwise the package is blocked. The existing flag may be reused only after identity and origin review. |
| Reservation | `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:46` | State 574 may be reserved only when unique, YAK is not living, and the SOV host-remnant test succeeds. The protected host state must be retained before reservation. |
| Force profile | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:52` | Required identity is cold-weather infantry, cavalry, and river guards using `mountain_frontier`, training value 62, with engineers, reconnaissance, and cold-weather logistics opening first. |
| Installed map binding | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:52` | Compact anchor is 574; optional extensions are 644, 876, and 877; source binding records all four as SOV-owned and requires runtime ownership to remain authoritative. |

## Coverage checklist

| Package surface | Status | Concrete evidence or blocker |
| --- | --- | --- |
| Tag registration | Existing vanilla tag | Vanilla `common/country_tags/00_countries.txt` maps `YAK` to `countries/Yakutia.txt`. No duplicate Chaos Redux tag registration was found. The tag is a living vanilla country, so the automatic-pool rule cannot be assumed. |
| Country definition | Existing vanilla baseline | Vanilla `common/countries/Yakutia.txt` defines Asian graphical cultures and cyan country colour. No package-local country definition is required or authorized. |
| State and capital | Blocked pending current-map proof | Vanilla `history/countries/YAK - Yakutia.txt` uses `capital = 574`. Vanilla `history/states/574-Siberia 1.txt` has owner `SOV`, cores `SOV` and `YAK`, victory point `10641`, infrastructure 1, and air base 1. Extension files are `history/states/644-state 3.txt`, `history/states/876-Udachny.txt`, and `history/states/877-Verkhoyansk.txt`. Source binding is not current-engine evidence. |
| Host and origin collision | Blocked | YAK is living in vanilla and the binding requires `ready_if_tag_not_living`. The SOV protected-state and origin-remnant checks must be proven against the installed map and current Event 006 origin state before any release path is admitted. |
| Politics and parties | Vanilla baseline only | Vanilla YAK history starts democratic with elections allowed and popularity 60 democratic, 20 communist, and 20 neutrality. No Event 006 package political setup is wired. |
| Leaders and portraits | Hard blocker | Vanilla `common/characters/YAK.txt` supplies `YAK_pavel_pevznyak` and `YAK_anatoly_pepelyayev`. Their portrait definitions resolve through generic Asian textures in vanilla `interface/_leader_portraits.gfx`, not dedicated YAK portraits. No grounded leader-source or portrait-worker evidence is attached to this package. The research row explicitly blocks without a defensible sourced leader or institution. |
| Flags | Reuse candidate, not cleared | Vanilla provides `YAK_communism.tga`, `YAK_democratic.tga`, `YAK_fascism.tga`, and `YAK_neutrality.tga` in the normal, medium, and small ladders. No flag was changed. Reuse remains gated by released-identity, origin, and asset-provenance review. |
| Focus tree | Not admitted | `common/national_focus/006_independence_wave_focus.txt` has no YAK-specific IW-051 package hook in the reviewed source. Existing Event 005 YAK content is confined to `common/national_focus/005_soviet_collapse_republics.txt`, including `internal_soviet_collapse_yakut_lena_resource_board`, `internal_soviet_collapse_yakut_aldan_convoy_roads`, and `internal_soviet_collapse_yakut_arctic_resource_compacts`. Those existing focuses do not prove Event 006 admission. |
| Decisions and ideas | Missing package-local tranche | No IW-051 decision or idea files were found in the owned Event 006 package families. Adding a new decision/idea suite before leader, map, and admission gates are resolved would be a broad package implementation, not a safe audit patch. |
| AI and probability | Missing and unverified | No IW-051 AI strategy file or package-specific weighted target was found. The mandatory probability inspection and comparison pass was not run in this finalization because the parent requested an immediate stop; no probability artifact is claimed. |
| Technology | Vanilla baseline only | Vanilla YAK history grants two research slots and generic infantry, reconnaissance, engineers, military police, mountaineers, trucks, motorized infantry, paratrooper, artillery, and doctrine technologies. No YAK-specific Event 006 technology surface is wired. The installed package exposes no Technology Tree Viewer, so tree-level engine evidence remains unresolved. |
| Military and industry | Mismatch with accepted force profile | Vanilla YAK history has no active `oob` assignment (the OOB line is commented), so the accepted cold-weather/cavalry/river-guard force is not present in the vanilla starting setup. The state has 407866 manpower, pastoral category, infrastructure 1, and air base 1. A package-local force helper would have no caller while the central release adapter is absent. |
| Supply and production | Not package-wired | No IW-051 production, depot, river-transport, or supply setup exists in the reviewed package families. The accepted force profile requires river and rail depot consolidation, but central setup and map ownership remain parent-owned. |
| Formables | Not in scope for this tranche | The registry describes a Siberian federation route, but no IW-051-specific formable implementation was accepted for this package-local audit. Do not create a formable or alter membership from this handoff. |
| GUI and map writes | Not performed | No GUI or map rewrite was made. No central adapter, attestation, preflight, deterministic Join, Event 006 origin, or map file was changed. |
| Assets and manifests | Missing package evidence | No custom Sakha flag, leader portrait, focus icon, idea icon, or asset manifest was added. No portrait fallback is authorized. |

## Required MCP evidence still outstanding

The parent stop request halted new MCP calls during finalization, so this handoff deliberately claims no fresh engine artifact references. Source inspection must not be treated as an MCP substitute. Before admission, run the mandatory read-only routes for the exact package surfaces:

- `hoi4.map_inspect` and a state-layer render for states 574, 644, 876, and 877, including owner, controller, cores, capital, victory points, buildings, supply, rail, resources, and host-remnant evidence.
- `hoi4.focus_inspect` and `hoi4.focus_render` for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, after any YAK hook is proposed.
- `hoi4.event_inspect` and read-only event rendering for the Event 006 setup/root path, including the package selector or `chaosx.nr6.350` bridge if that remains the package entry point.
- `hoi4.probability_inspect` first, followed by the required scenario comparison through `chaosx_ai_probability_auditor`, if an IW-051 AI strategy, focus weight, decision score, or other weighted surface is added.
- The read-only technology inspection route for any new technology dependency. The installed package has no Technology Tree Viewer, which remains an explicit unresolved limitation.

## Central-boundary finding

The package cannot be admitted by adding only local constants, scripted effects, ideas, AI, decisions, localisation, or focus hooks. The current Event 006 authority boundary recorded by the existing country-admission audits keeps the central adapter, attestation, preflight, origin, and Join logic outside this subagent scope. IW-051 has no verified package-local caller for its force profile, no admission attestation, and no deterministic setup path. A local helper without a parent-owned call site would be dead code and must not be presented as a working package.

## Safe next steps for the parent

1. Obtain and archive a defensible real male period leader or an explicitly sourced local institution, then route any portrait through `chaosx_portrait_creator`; do not reuse the generic vanilla portrait as identity proof.
2. Re-run the full installed-tag collision and origin audit with YAK living/non-living scenarios, then prove the SOV protected-state remnant and state-574 uniqueness through the map MCP route.
3. Resolve the central Event 006 admission/force-setup call site before writing package-local force or AI effects.
4. After those gates pass, add a narrow package-local tranche with fail-closed guards, then obtain focus, event, probability, and asset evidence before claiming readiness.

## Files changed by this audit

Only this documentation handoff was added:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw051_sakha_package_audit_2026_08_14.md`

No `common/`, `history/`, `interface/`, `gfx/`, localisation, central adapter, attestation, preflight, origin, Join, or map source file was changed. No source implementation tranche landed. The package remains blocked, not complete.
