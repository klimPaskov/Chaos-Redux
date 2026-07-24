# IW-019 Sicily country-package re-audit

Date: 2026-07-24

Audit reference: portrait-wiring commit `7e46ac65d814e4c7274bab1359568473ff5d0d18` (`Wire sourced Sicily leadership portraits`).

The audit started at repository `HEAD` `667a4a92e`; no post-portrait-wiring diff was found on the relevant IW-019 package paths.

This audit used `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-subagents`, the required offline Paradox Wiki pages (including Portrait modding and Graphical asset modding), and the relevant Hearts of Iron IV documentation and vanilla state/history files.

The event-catalog workbook was not edited.

## Verdict

The static ASX country package is internally wired for tag `ASX`, package `iw_019`, anchor state `115` (Sicily), regional group `RG-115`, and its current six-character roster.

The runtime automatic-pool verdict is **FAIL CLOSED** because `common\scripted_triggers\006_independence_wave_package_dispatch_triggers.txt` attests only `iw_004`, `iw_007`, and `iw_017`; `iw_019` is not admitted by `has_independence_wave_runtime_package_content_attestation_for_execution_id`.

The Luigi Rizzo role split is internally correct in the gameplay files: Rizzo is a civilian-large despotism country leader and is not a corps commander, while Vincenzo Di Benedetto is the sole army-large corps commander.

The current Rizzo political-leader portrait consumer is **not independently role-authorized** by the existing Sicily visual/provenance audit. That audit explicitly authorized the existing army/corps-command large consumer only and did not audit a civilian political-leader consumer. A separate role/consumer audit or an approved role correction is required before Rizzo can be admitted as a grounded political portrait. This is a fail-closed audit finding, not a claim that the historical identity is false.

## Country package coverage checklist

| Surface | Result | Evidence and remaining risk |
|---|---|---|
| Identity, tag, adjective, and package id | PASS (static) | `ASX`, `ASX_DEF`, `ASX_ADJ`, ideology variants, and `iw_019` are consistent across `common\country_tags\006_independence_wave_countries.txt`, `common\countries\006_independence_wave_ASX.txt`, localisation, package triggers, effects, focus, decisions, and dispatch adapters. |
| Territory, capital, origin, and host survival | PASS (static) | State `115`/Sicily is the anchor and capital, `RG-115` is the regional anchor, and `execution_effects` transfers frozen states while preserving a former-host state and Italy's state `2`/Rome capital. Live map execution was not run. |
| History and starting shell | PASS (static) | `history\countries\ASX - Sicily.txt` remains absent-at-start and recruits the intended six-character roster; baseline laws are present and runtime setup owns territory, politics, forces, ideas, focus, and AI. |
| Roster and role metadata | PASS for split; BLOCKED for Rizzo visual-role admission | Six all-male characters are recruited. Rizzo has civilian-large and country-leader definitions only; Di Benedetto has army-large and corps-commander definitions only; both role assertions are checked by package triggers. |
| Portrait provenance and likeness | PASS for Sturzo, Lanza di Scalea, and Di Benedetto | Independent audits and runtime DDS identity checks pass for the authorized consumers. Rizzo source/likeness also passed, but only for the pre-existing army/corps-command large consumer; current civilian use remains unaudited. |
| Portrait GFX and runtime DDS | PASS for four wired full portraits | Four `spriteType` entries resolve to 156x210 runtime DDS files. No Event-006 advisor, dossier, `_small`, female, or alternate portrait asset is present or required. |
| Flags and country graphics | PASS for file coverage; REVIEW for route ownership | Normal, medium, small, and all ideology-variant `ASX` TGA files exist and load. The supplied 1848 S.015 flag design is documented, but the asset handoff still marks route ownership as under review. |
| Localisation | PASS (static) | Country names, adjectives, ideology names, six character names/descriptions, focus names/descriptions, decision names/tooltips, ideas, incidents, host routes, Form05 terms, and debug names are covered in `localisation\english\006_independence_wave_mediterranean_l_english.yml`. |
| Politics, parties, laws, and ideas | PASS (static) | `independence_wave_initialize_asx_politics` and the five route installers set the intended starting/routing politics; three baseline ideas and five route ideas are defined and referenced. |
| Focus tree | PASS (static) | The ASX branch in `common\national_focus\006_independence_wave_focus.txt` contains the port, grain, garrison, administration, property, customs, and mutually exclusive Two Sicilies/Mediterranean republic routes with icons, localisation, prerequisites, availability, and AI weights. |
| Decisions, mission, and incidents | PASS (static) | ASX founding mission `hold_port_authority_together`, ten projects, and ASX incidents `chaosx.nr6.23`, `chaosx.nr6.26`, and `chaosx.nr6.27` have references, effects, cancellation/timeout paths, and localisation. |
| Formable and league integration | PASS (static) | FORM05 trigger/effect paths recognize package `iw_019`, anchor `115`, ASX, Mediterranean island league, Maritime Congress, and member/invitation flows. |
| Forces, technology, industry, supply, and production | PASS (static package wiring) | Force profile `regular_defectors`/p19 with military-tradition score `65` is loaded through the dynamic starting-force system, with coastal infantry, defectors, port defense, navy/air inheritance, equipment, stockpile, train, convoy, fuel, and AI production hooks. No custom technology tree is claimed. |
| AI and playability | PASS (static) | ASX island survival, founding restraint, host-threat, civic maritime, straits-command, and Two Sicilies dossier strategy blocks are scoped to the package and route flags. Live campaign balance was not run. |
| Diplomacy, host, patron, and cleanup | PASS (static) with cleanup observation | Four host-route paths, patron/host-threat checks, Italian property hooks, and cleanup of ASX decisions/ideas/claims/flags are present. ASX cleanup does not visibly restore a generic focus tree or retire ASX characters, unlike the COR cleanup path; this parity risk was not patched because it is outside the portrait-wiring scope and no harmful runtime case was demonstrated. |

## File-surface checklist and findings

### Identity, map, origin, and host

- `common\country_tags\006_independence_wave_countries.txt` maps `ASX` to `countries/006_independence_wave_ASX.txt`.
- `common\countries\006_independence_wave_ASX.txt` supplies the western-European graphical culture and ASX colour shell.
- `history\countries\ASX - Sicily.txt` recruits the six characters and sets the conservative baseline laws while leaving the country absent at game start.
- Vanilla `history\states\115-Sicily.txt` confirms owner `ITA`, cores `ITA` and `TTS`, Palermo and secondary victory points, port/air/industry infrastructure, and the state anchor used by the package.
- Vanilla `history\states\2-Italy.txt` confirms that Italy retains its Rome capital state when state `115` is transferred.
- `common\scripted_effects\006_independence_wave_execution_effects.txt` performs the frozen-state ownership/controller transfer and former-host protection checks; the package setup and preflight triggers require the ASX anchor to be owned and controlled before activation.

No static state, capital, core, port, supply, railway, resource, or host-survival contradiction was found. Live map/MCP map-rewrite validation was not run.

### Politics and leader-role split

- `common\characters\006_independence_wave_mediterranean_characters.txt` defines `ASX_sicilian_provisional_assembly` as Luigi Sturzo, `ASX_sicilian_crown_council` as Pietro Lanza di Scalea, `ASX_luigi_rizzo` as a male civilian-large country leader with despotism support, `ASX_vincenzo_di_benedetto` as a male army-large corps commander, and two male portraitless political-advisor characters.
- `common\scripted_effects\006_independence_wave_mediterranean_package_effects.txt:499` promotes `ASX_luigi_rizzo` only in the military-government route and assigns despotism.
- `common\scripted_triggers\006_independence_wave_mediterranean_package_triggers.txt:55-56` asserts `ASX_luigi_rizzo` is not a corps commander and `ASX_vincenzo_di_benedetto` is a corps commander.
- Di Benedetto's localisation describes him only as a “retired Sicilian general recalled for synchronized independence emergency,” matching the approved army-command role.
- No opposing-gender name pool, female metadata, generated personal identity, institutional-person name collision, or advisor portrait dependency was found.

The role split is internally clean. The blocker is consumer authorization: `006_sicily_trial01_portrait_visual_provenance_audit_2026_07_22.md` records Rizzo's independent visual/provenance PASS for the existing full `army`/corps-command large consumer only and states that no separate navy slot or new role was authorized. It does not review the current civilian political consumer. Since the character now consumes the same portrait as a civilian-large country leader, a separate role/consumer audit is required before this portrait can satisfy the grounded-person visual policy.

### Portrait, GFX, runtime DDS, and asset coverage

`interface\006_independence_wave_mediterranean_portraits.gfx` defines exactly these active full portrait sprites, with no `_small` or alternate Event-006 portrait sprites:

| GFX id | Runtime path | Dimensions | SHA-256 |
|---|---|---:|---|
| `GFX_portrait_ASX_independence_wave_luigi_sturzo` | `gfx\leaders\ASX\ASX_luigi_sturzo.dds` | 156x210 | `4768e69316d2a03754be052143c68a157902c6953d99ce9389472ed1ada52e57` |
| `GFX_portrait_ASX_independence_wave_pietro_lanza_di_scalea` | `gfx\leaders\ASX\ASX_pietro_lanza_di_scalea.dds` | 156x210 | `7d1201f05a7189001b88a9d7aa9b5e2ed565379cbd30f2fe170ef6aaa245475a` |
| `GFX_portrait_ASX_independence_wave_luigi_rizzo` | `gfx\leaders\ASX\ASX_luigi_rizzo.dds` | 156x210 | `659c819547559f50025fb3007cd5c60947a150ca4673238cc179dc2f0867d714` |
| `GFX_portrait_ASX_independence_wave_vincenzo_di_benedetto` | `gfx\leaders\ASX\ASX_vincenzo_di_benedetto.dds` | 156x210 | `bc709fe8d00916a60da4b7445e872a746a41901f3c619502824b078dbf7ec173` |

All four runtime DDS files were opened and checked as 156x210 legacy BGRA files of 131,168 bytes. The Sturzo, Lanza, and Rizzo runtime hashes match their reviewed final DDS packages. Di Benedetto's manifest and GFX handoff record the runtime DDS hash above, and the file is present and pixel-identical to the approved processed PNG.

The independent Di Benedetto audit passes provenance, likeness, commander style, role fit, ownership, and exclusivity, and authorizes only the army/corps-command large portrait. The independent Sturzo/Lanza/Rizzo audit passes source, likeness, native HOI4 style, and male-only policy, but authorizes Rizzo only for the pre-existing army/corps-command consumer. It does not authorize Rizzo's current civilian political consumer.

No ASX advisor portrait, dossier portrait, `_small` portrait, female asset, generated leader identity, or missing portrait icon was found in active `common`, `interface`, or `gfx` references. Historical stale inventories under `docs\assets` still mention old fictional names such as `ASX_salvatore_licata`; no active gameplay reference to that name remains.

### Flags, ideas, focus, decisions, events, and localisation

- `gfx\flags\ASX.tga` and its normal, medium, small, and ideology-variant files exist, open successfully, and have the expected 82x52, 41x26, and 10x7 RGBA dimensions.
- `interface\006_independence_wave_mediterranean_assets.gfx` resolves the ASX focus, decision, Form05 Maritime Congress, and idea sprites, and all referenced DDS files exist at their declared dimensions.
- ASX focus IDs in `common\national_focus\006_independence_wave_focus.txt:2776-2889` are localized and connected to route flags, package checks, prerequisites, icons, and AI behavior.
- ASX mission/project definitions in `common\decisions\006_independence_wave_mediterranean_decisions.txt:297-464` have visible/available gates, costs, durations, completion effects, cancellation/timeout behavior, and localized tooltips.
- `common\ideas\006_independence_wave_mediterranean_ideas.txt` defines the contested port, state compact, constitutional assembly, labor compact, crown council, island guard, and protected mandate ideas used by setup and routes.
- ASX incidents `chaosx.nr6.23`, `chaosx.nr6.26`, and `chaosx.nr6.27` have options/effects and localized event text.

No missing active localisation or icon reference was found in these surfaces.

### Forces, technology, industry, supply, and AI

The binding and force-map rows identify IW-019 as `regular_defectors`, profile `p19`, military tradition `65`, with naval and air inheritance and the coastal-infantry/port-defense/defecting-host-unit pathways. `common\scripted_effects\006_independence_wave_force_effects.txt` and `006_independence_wave_force_package_effects.txt` load that profile dynamically and provide equipment, stockpile, division-template, train, convoy, fuel, production, and supply values. The package AI in `common\ai_strategy\006_independence_wave_mediterranean.txt` is scoped to ASX and its route/host-threat flags.

The installed HOI4 MCP package exposes no Technology Tree Viewer. No custom IW-019 technology tree is present, so technology-tree render/compare validation remains an unresolved tooling limitation rather than an asserted pass.

### Formable, host, diplomacy, and cleanup

`common\scripted_triggers\006_independence_wave_form05_triggers.txt`, `common\scripted_effects\006_independence_wave_form05_effects.txt`, and the Form05 registry accept ASX/`iw_019`/state `115` for the Mediterranean island league, Maritime Congress, invitations, and member flows. The package setup installs four host routes and the traditional-authority-versus-assembly struggle, and the host-threat/patron AI helpers are present.

`independence_wave_cleanup_iw_019_sicily` removes the founding mission, ASX decisions, ASX ideas, ASX claims, formable variables, and package flags. It does not visibly restore a generic focus tree or retire ASX characters; this is recorded as a low-confidence cleanup-parity observation for parent review and was not patched in this portrait-focused audit.

## Runtime admission evidence

`common\scripted_triggers\006_independence_wave_package_dispatch_triggers.txt:33-50` lists content attestations only for `iw_004`, `iw_007`, and `iw_017`. Although the adapter list and the IW-019 preflight branch are present, the exact IW-019 package id cannot pass the content-attestation block.

`common\scripted_triggers\006_independence_wave_triggers.txt:497-504` sets the execution id to `iw_019`, checks ASX and the preflight, and therefore returns false until that attestation is deliberately added after the remaining audits.

`docs\plans\006_independence_wave_plans\package_bindings\006_current_installed_map_package_bindings.csv` still labels IW-019 `automatic_pool_ready`/`ready_automatic`. That binding row is stale or lower-authority than the runtime gate and should be reconciled by the parent or documentation curator; it was not edited here.

## Validation performed

- `python .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable publishers, and 138 ranked publishers, and confirmed Event-005 anchors precede Event-006 anchors.
- A targeted static reference scan resolved ASX character, focus, decision, event, idea, GFX, and localisation references and found no active `ASX_salvatore_licata` reference.
- Runtime DDS files were hash-checked, opened with Pillow, and verified as 156x210 legacy BGRA files; ASX flags were opened with Pillow and verified at all expected dimensions; focus, decision, and idea DDS paths were checked for existence and declared dimensions.
- Role checks confirmed Rizzo is `is_corps_commander = no` and Di Benedetto is `is_corps_commander = yes`; no ASX advisor/dossier/`_small`/female portrait reference exists in active content.
- Live HOI4 startup, campaign execution, map rewrite/render, GUI render, and Technology Tree Viewer checks were skipped. The installed tooling has no Technology Tree Viewer, and the parent owns live runtime admission decisions.

## Required follow-up and blockers

1. Commission or record a separate independent audit of the Rizzo civilian-large political-leader consumer, or change the role to one covered by the existing visual audit. Do not infer authorization from the historical source alone.
2. Keep IW-019 out of the automatic pool until its exact content attestation is added after the role/consumer audit and any resulting package re-audit.
3. Reconcile the stale `ready_automatic` package-binding row, stale source-of-truth/resume text, and old portrait inventories with the accepted role split and runtime gate.
4. Review the ASX cleanup parity observation (generic focus restoration and character retirement) in a runtime-safe scope before final completion claims.
5. Resolve the documented 1848 S.015 flag route-ownership review if the final route family needs a fixed historical/constitutional assignment.

No gameplay, asset, localisation, map, or workbook files were changed by this audit. The only intended change is this handoff.

