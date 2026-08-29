# Event 006 Eurasian country-package tranche audit

Date: 2026-08-29

Scope: Bounded audit of IW-048 Udmurtia (`UDM`), IW-050 Komi (`KOM`), IW-051 Sakha (`YAK`), IW-052 Buryatia (`BYA`), and IW-053 Altai (`ALT`).

Disposition: PACKAGE-LOCAL / FAIL-CLOSED / NO ADMISSION. One narrow localization repair was applied for two vanilla party-restoration keys; no gameplay, map, asset, AI-weight, spreadsheet, or central-admission change was made.

## Authority and evidence boundary

The accepted contract is defined by `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, and the current source-of-truth map at `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.

The required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, countries, states, maps, focuses, divisions, and technology were consulted, together with the relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` and the installed vanilla country, character, history, state, focus, idea, flag, and AI files.

The `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-comfyui` skills were applied for the bounded audit, fail-closed admission rule, source-backed asset boundary, and portrait-worker ownership rule.

## Package coverage checklist

| Surface | IW-048 UDM | IW-050 KOM | IW-051 YAK | IW-052 BYA | IW-053 ALT |
| --- | --- | --- | --- | --- | --- |
| Carrier and tag | Vanilla `UDM` is registered once and remains the carrier. | Vanilla `KOM` is registered once and remains the carrier. | Vanilla `YAK` is registered once and remains the carrier. | Vanilla `BYA` is registered once and remains the carrier. | Vanilla `ALT` is registered once and remains the carrier. |
| Installed anchor | State 399, Izhevsk. | State 397, Syktyvkar; optional 262 and 581. | State 574, Yakutsk; optional 644, 876, and 877. | State 564, Ulan Ude. | State 654, Oyrot/Gorno-Altaysk; optional 40, Altai Krai/Barnaul. |
| Former-host rule | Vanilla owner is `SOV`; protected remnant is `SOV=219`. | Vanilla owners are `SOV`; protected remnant is `SOV=219`. | Vanilla owners are `SOV`; protected remnant is `SOV=219`. | Vanilla owner is `SOV`; protected remnant is `SOV=219`. | Vanilla owners are `SOV`; protected remnant is `SOV=219`. |
| Package setup | Local trigger/effect setup exists, but no central admission. | Local trigger/effect setup exists, but no central admission. | Local trigger/effect setup exists, but no central admission. | Local trigger/effect setup exists, but no central admission. | Local trigger/effect setup exists, but no central admission. |
| Roster gate | Requires parent-owned `independence_wave_iw_048_identity_rights_cleared` and `UDM_boris`. | Requires parent-owned `independence_wave_iw_050_identity_rights_cleared` and `KOM_pavel_murashev`. | Requires parent-owned `independence_wave_iw_051_identity_rights_cleared` and `YAK_pavel_pevznyak`. | Requires parent-owned `independence_wave_iw_052_identity_rights_cleared`, `BYA_seymon_ignatyev`, and `BYA_bidia_dandaron`. | Requires parent-owned `independence_wave_iw_053_identity_rights_cleared`, `ALT_grigory_gurkin`, and `ALT_samuil_yufit`. |
| Force contract | p48 industrial-security intent remains unresolved against the package `industrial_breakaway` archetype. | p50 `mountain_frontier`; no navy or air pathway. | p51 `mountain_frontier`; no navy or air pathway. | p52 `mounted_mobile`; no navy or air pathway. | p61 `mounted_mobile`; accepted tradition 61 conflicts with shared row value 57. |
| Politics/economy | Baseline laws, four government routes, compact lifecycle, and industrial/forest variables are local. | Baseline laws, four government routes, compact lifecycle, and northern/taiga variables are local. | Baseline laws, four government routes, compact lifecycle, and arctic/river variables are local. | Baseline laws, four government routes, compact lifecycle, and frontier/council variables are local. | Baseline laws, four government routes, compact lifecycle, and mountain/frontier variables are local. |
| Ideas and decisions | Seven package ideas, one founding mission, and ten paid projects are present and localized. | Seven package ideas, one founding mission, and ten paid projects are present and localized. | Seven package ideas, one founding mission, and ten paid projects are present and localized. | Seven package ideas, one founding mission, and ten paid projects are present and localized. | Seven package ideas, one founding mission, and ten paid projects are present and localized. |
| Shared focus | Uses guarded callbacks in `independence_wave_focus_tree`; no bespoke country tree. | Uses guarded callbacks in `independence_wave_focus_tree`; no bespoke country tree. | Uses guarded callbacks in `independence_wave_focus_tree`; no bespoke country tree. | Uses guarded callbacks in `independence_wave_focus_tree`; no bespoke country tree. | Uses guarded callbacks in `independence_wave_focus_tree`; no bespoke country tree. |
| Portrait/flag rights | Vanilla generic Boris Berman portrait and vanilla flag ladder have no accepted Event 006 rights receipt. | Vanilla generic Murashev portrait and symbol/flag provenance remain unresolved. | Pavel Pevznyak has a gated source-placeholder consumer; final/rights evidence remains absent. | Generic vanilla roster portraits and neutral flag identity remain unresolved; Erbanov/Markizov evidence is not admitted. | Generic vanilla Gurkin/Yufit portraits and neutral flag identity remain unresolved. |
| AI evidence | Four package strategies are source-present; typed probability evidence is unavailable. | Four package strategies are source-present; typed probability evidence is unavailable. | Four package strategies are source-present; typed probability evidence is unavailable. | Four package strategies are source-present; typed probability evidence is unavailable. | Four package strategies are source-present; typed probability evidence is unavailable. |
| Central runtime | No adapter, attestation, preflight, SCN-008 branch, or deterministic Join. | No adapter, attestation, preflight, SCN-008 branch, or deterministic Join. | No adapter, attestation, preflight, SCN-008 branch, or deterministic Join. | No adapter, attestation, preflight, SCN-008 branch, or deterministic Join. | No adapter, attestation, preflight, SCN-008 branch, or deterministic Join. |

## File-surface checklist and concrete findings

### Identity, carrier, history, capital, and map

Vanilla `common/country_tags/00_countries.txt` maps `UDM`, `KOM`, `YAK`, `BYA`, and `ALT` to their respective vanilla country files, with no duplicate Event 006 tag definitions in `common/country_tags/006_independence_wave_countries.txt`.

Vanilla histories `history/countries/UDM - Udmurtia.txt`, `KOM - Komi Republic.txt`, `YAK - Yakutia.txt`, `BYA - Buryatia.txt`, and `ALT - Altai Republic.txt` provide capitals 399, 397, 574, 564, and 654 respectively, ordinary vanilla technologies and research slots, baseline politics, and the reused character roster. None has a package-specific OOB, so the package force effects remain the source of starting force behavior.

The installed-map binding is exact in `006_current_installed_map_package_bindings.csv`: UDM state 399; Komi state 397 with optional 262/581; Sakha state 574 with optional 644/876/877; Buryatia state 564; and Altai state 654 with optional 40. The corresponding vanilla state files are `399-Izhevsk.txt`, `397-Syktyvkar.txt`, `574-Siberia 1.txt`, `564-TS 6.txt`, `654-sov state 8.txt`, `262-Torzhok.txt`, `581-Northern Urals.txt`, `644-state 3.txt`, `876-Udachny.txt`, `877-Verkhoyansk.txt`, and `40-USSR.txt`.

The vanilla state owners are `SOV`, with the expected carrier cores on the compact anchors; state 564 also has the existing `FER` core, and state 654/40 retain their vanilla `ALT` cores. The package triggers require the anchor to be owned and controlled, set as capital, and protected-host settlement to be valid before runtime readiness. No map write was made.

The reservation/load registry has planner and reservation entries for `iw_048` through `iw_053` in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1060-1128,1184-1188,1213-1217`. These entries are candidate-planner surfaces only and do not establish central admission.

### Package-local setup, cleanup, and lifecycle

UDM is implemented in `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt` and `common/scripted_effects/006_independence_wave_udm_package_effects.txt`. Its package proof is `is_independence_wave_udm_package`, its roster gate is `has_independence_wave_udm_command_roster`, and its setup/cleanup are `independence_wave_setup_iw_048_udm` and the corresponding generation-safe cleanup effect.

KOM is implemented in `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt` and `common/scripted_effects/006_independence_wave_komi_package_effects.txt`. Its package proof is `is_independence_wave_komi_package`, its roster gate is `has_independence_wave_komi_command_roster`, and its local setup/cleanup keep the 420-day founding mission and ten-project lifecycle behind package and generation checks.

Sakha, Buryatia, and Altai are implemented in `common/scripted_triggers/006_independence_wave_siberian_package_triggers.txt` and `common/scripted_effects/006_independence_wave_siberian_package_effects.txt`. The exact setup/cleanup effects are `independence_wave_setup_iw_051_sakha`/`independence_wave_cleanup_iw_051_sakha` at lines 1719/1816, `independence_wave_setup_iw_052_buryatia`/`independence_wave_cleanup_iw_052_buryatia` at lines 781/864, and `independence_wave_setup_iw_053_altai`/`independence_wave_cleanup_iw_053_altai` at lines 317/404.

All five package cleanups remove package decisions, ideas, route/lifecycle flags, ledgers, and local AI state before restoring carrier politics and vanilla party names. The cleanup references for `BYA_neutrality_party_long` and `YAK_neutrality_party_long` were previously undefined in vanilla and are repaired by this tranche's localization-only patch.

### Politics, leaders, portraits, flags, advisors, and parties

The package histories reuse the following vanilla leaders without changing identities: `UDM_boris` / Boris Berman, `KOM_pavel_murashev` / Pavel Murashev, `YAK_pavel_pevznyak` / Pavel Pevznyak, `BYA_seymon_ignatyev` / Seymon Ignatyev and `BYA_bidia_dandaron` / Chakravartin Bidia Dandarovitch Dandaron, and `ALT_grigory_gurkin` / Grigory Gurkin and `ALT_samuil_yufit` / Samuil Yufit. All inspected entries use male names and male-presenting generic portrait tokens without opposite-gender metadata or name-pool pairing.

The corresponding vanilla character definitions are in `common/characters/UDM.txt`, `KOM.txt`, `YAK.txt`, `BYA.txt`, and `ALT.txt`, while vanilla portrait registrations are in `interface/_leader_portraits.gfx`. No package-specific advisor, high-command, commander, institutional portrait, generated name pool, or invented historical leader was added.

UDM remains blocked on Boris Berman source/rights acceptance and on an accepted identity-matched flag policy. KOM remains blocked on Murashev source/rights and a defensible neutral symbol/flag provenance. Sakha has only the gated source-placeholder portrait consumer `gfx/leaders/006_independence_wave/portrait_YAK_independence_wave_pavel_pevznyak.dds`, registered as `GFX_portrait_YAK_independence_wave_pavel_pevznyak` in `interface/006_independence_wave_portraits_registry.gfx:126-135`; this is not final or rights-cleared evidence. Buryatia remains blocked on the roster portrait/source and neutral-identity decision. Altai remains blocked on Gurkin/Yufit identity/rights and neutral flag provenance.

The only existing mod flag files in scope are Event 005 KOM democratic variants and gated YAK route variants under `gfx/flags/`; UDM, BYA, and ALT have no Event 006-specific flag assets. Vanilla normal/medium/small ladders exist for all carriers, but structural presence does not prove origin, identity, or rights acceptance.

The local package route party names and tooltips are present in `localisation/english/006_independence_wave_udm_l_english.yml`, `006_independence_wave_komi_l_english.yml`, and `006_independence_wave_siberian_l_english.yml`. The repair adds exact vanilla short-name values as the missing long-name restoration keys:

* `BYA_neutrality_party_long: "Chakravartin Restorationists"`.
* `YAK_neutrality_party_long: "White Russian Army"`.

No party ideology, popularity, leader, portrait, flag, or rights gate was loosened by this change.

### Focus, decisions, missions, ideas, and assets

All five packages use the shared `independence_wave_focus_tree` declared in `common/national_focus/006_independence_wave_focus.txt:38`, with package-gated helper callbacks and aliases rather than bespoke country trees. UDM callbacks are in `common/scripted_effects/006_independence_wave_udm_package_effects.txt:218-246`; Komi's named callbacks are the northern congress, railhead communities, forest guards, former-host ledgers, and Pechora corridor helpers; the Siberian callbacks are in the consolidated package effects file.

The package decisions are in `common/decisions/006_independence_wave_siberian_decisions.txt`. Static definition counts are UDM 12, KOM 12, YAK 11, BYA 11, and ALT 12, comprising each package's founding mission/category surfaces plus ten project decisions where defined. Every discovered decision ID has a matching localization key in the package localization files.

The package ideas are in `common/ideas/006_independence_wave_ideas_registry.txt:700-742` for ALT, `1023-1065` for BYA, `2897-2969` for KOM, `3870-3912` for YAK, and `4312-4384` for UDM. Each carrier has seven package ideas, and all seven-per-package IDs have matching localization.

No focus icon, idea icon, decision icon, flag, portrait, or other visual asset was created or repurposed. The portrait worker must resolve grounded source/rights or an explicitly approved fictional package before any admission patch.

### Starting military, technology, industry, supply, and production

The local force contracts are UDM industrial-security intent, KOM p50 `mountain_frontier`, YAK p51 `mountain_frontier`, BYA p52 `mounted_mobile`, and ALT p61 `mounted_mobile`. The package triggers require named reinforcement pathways and explicitly reject unsupported navy/air routes; no large army, equipment, technology, or industrial balance change was introduced.

UDM's source-of-truth p48 force intent is `industrial_security`, while its loader uses the available package archetype `industrial_breakaway`; this contract has not been normalized because doing so would be a design/balance change outside this bounded audit. Altai's accepted tradition constant is 61 while the shared p61 force row remains 57 in the current table; the trigger intentionally keeps this mismatch fail-closed rather than tuning the table. These are package admission blockers, not safe local repairs.

Vanilla histories provide only the existing carrier technology baselines and research slots, and no package adds a technology or doctrine. The installed runtime exposes no Technology Tree Viewer, so no new technology-tree acceptance claim is made.

Supply, railway, port, resource, building, and victory-point behavior is sourced from the listed installed state files but has no fresh current engine receipt because the required map-inspection route is unavailable. No map rewrite or state transfer was attempted.

### AI and probability

The source AI registry defines four package strategies for each carrier in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`: ALT lines 27-75, BYA lines 392-446, KOM lines 1562-1610, YAK lines 2797-2851, and UDM lines 3406-3457. The profiles cover survival, host restraint, settled development, and emergency defense/build priorities with package constants; no AI weight was changed.

The mandatory `chaosx_ai_probability_auditor` route is not callable in this runtime, and no `hoi4_agent_tools` probability inspection/compare route is exposed. Existing read-only attempts recorded `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with no artifact, so no typed scenario probability, MTTH, strategy-factor, or balance claim is made and no compare pass was possible.

### Central adapter, attestation, preflight, SCN-008, Join, and cleanup

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` contains zero literal references to each of `iw_048`, `iw_050`, `iw_051`, `iw_052`, and `iw_053`; the same zero-reference result holds for `common/scripted_effects/006_independence_wave_join_effects.txt`. Therefore none of the five has a central runtime adapter, content-attestation branch, normal preflight, SCN-008 preflight, capacity row, setup/final-validation/cleanup dispatch branch, or deterministic Join path.

This absence is consistent with the current source-of-truth map and is intentionally preserved. Planner/load/reservation rows are not admission evidence, and no central OR-list was widened in this tranche.

Former-host protection remains package-local and generation-safe in the trigger/effect files, but no current engine receipt proves the SOV remnant after a release transaction. State 219 must remain protected before any future central promotion.

## Validation and exact limitations

The following focused static validators passed on the current workspace:

* `python -B .tools/audit_event6_country_api.py` reported 242 broad unique tags, 191 resolved carriers, zero missing, zero duplicates, and a passing IW-031 crosswalk.
* `python -B .tools/audit_event6_allocator.py` reported the current 40 runtime adapters, 32 content attestations, 29 groups, and the expected fail-closed boundary without promoting these five IDs.
* `python -B .tools/audit_event6_flags.py --strict` reported 102 registered Event 006 tags and 102 complete flag families.
* A package-local decision/idea/localization check reported UDM/KOM/YAK/BYA/ALT decision counts 12/12/11/11/12 with zero missing localization, seven ideas each with zero missing localization, and one match each for the repaired BYA/YAK restoration keys.
* A central-reference check reported zero `iw_048`/`iw_050`/`iw_051`/`iw_052`/`iw_053` references in both the central dispatch trigger and deterministic Join effect files.

The installed callable-tool registry exposes no `hoi4_agent_tools` map, focus, event, technology, or probability route and no `chaosx_country_package_auditor` or `chaosx_ai_probability_auditor` route. Prior package handoffs record the same artifact-manifest integrity failure for attempted read-only receipts. This is an explicit engine-evidence blocker, not a source-only pass.

No live Hearts of Iron IV process was launched, no map write was made, and no fallback parser or stale artifact was substituted for unavailable MCP evidence.

## Changes, remaining blockers, and simplifications

Changed file: `localisation/english/006_independence_wave_siberian_l_english.yml`.

Before: BYA and YAK cleanup effects referenced undefined vanilla restoration keys `BYA_neutrality_party_long` and `YAK_neutrality_party_long`.

After: the localization file supplies those keys using the exact vanilla short party strings, so generation-safe cleanup no longer depends on missing localization entries.

No tag, state ID, leader, party ideology, focus tree ID, focus route, decision ID, mission ID, idea ID, formable ID, flag, portrait, AI weight, force mapping, central registry, attestation, preflight, Join, map, or spreadsheet surface changed.

The five packages remain blocked on identity/portrait rights, identity-matched flag/symbol provenance, parent-owned rights flags, host-remnant runtime proof, central adapter/attestation/preflight/SCN-008/Join wiring, typed AI/probability evidence, and the package-specific UDM and ALT force-contract discrepancies described above. YAK's source-placeholder consumer remains gated and is not a final asset.

No unapproved fallback, broad identity redesign, new package, generic content substitution, balance simplification, or admission shortcut was used. This handoff records an incomplete package tranche and does not claim Event 006 completion.
