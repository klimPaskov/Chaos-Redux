# Event 006 IW-093 / IW-098 country-package closure audit

Date: 2026-08-26.

Scope: paired closure audit for IW-093 DOX (Asante) and IW-098 SOK (Sokoto), including shared character, flag, focus, decision, AI, formable, planner, attestation, dispatch, capacity, and Join surfaces.

Verdict: HOLD both packages.

No gameplay source was changed, no central admission list was widened, no map write was attempted, no RunPod operation was performed, and no live game test was run.

## Admission decision

Both packages have country-local adapters and fail-closed setup, final-validation, and cleanup dispatches, but neither package is in `has_independence_wave_runtime_package_content_attestation_for_execution_id` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-199`.

The shared preflight and planner require that attestation before reservation or execution in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:204-338` and `common/scripted_effects/006_independence_wave_package_planner_effects.txt:104-106`.

The Join probe list in `common/scripted_effects/006_independence_wave_join_effects.txt:213-` also excludes `iw_093` and `iw_098`, so Join cannot bypass the central gate.

The current structural validator confirms this state: `python .tools/audit_event6_allocator.py` reported 40 runtime adapters, 32 attested packages, and adapter-only fail-closed IDs including IW093 and IW098.

Adding either package to the attestation or Join lists now would bypass unresolved identity and runtime-content gates and is not evidence-backed.

## Country-package coverage checklist

| Surface | IW-093 DOX Asante | IW-098 SOK Sokoto |
| --- | --- | --- |
| Tag and shell | `DOX` is registered in `common/country_tags/006_independence_wave_countries.txt:55`; shell is `common/countries/006_independence_wave_DOX.txt` | `SOK` is the registered vanilla dormant tag in `common/country_tags/00_countries.txt:270`; no new mod tag is needed |
| History and anchor | `history/countries/DOX - Asante.txt`; fixed state 274 and Kumasi VP 12787 | vanilla `history/countries/SOK - Sokoto.txt`; fixed state 902 and Sokoto VP 1891 |
| Package loader and reservation | `independence_wave_load_package_iw_093` publishes `rg_ghana_asante_fante`, region `west_central_africa`, signature depth, and state 274 in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1534-1547` | `independence_wave_load_package_iw_098` publishes `rg_nigeria_coarse`, region `west_central_africa`, signature depth, and state 902 in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1579-1592` |
| Local setup and cleanup | Present in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:593-647` and `:788-849` | Present in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:649-706` and `:851-913`, with Event 012 safety guard |
| Focus and decisions | Pair roots and full shared tree are loaded by `independence_wave_focus_tree`; 18 package decisions are present | Same shared tree and 18 package decisions, with Event 012 replacement guard |
| Ideas, values, and parties | Package ideas, four tracked values, route flags, and party names are present | Package ideas, four tracked values, route flags, and party names are present |
| Force mapping | Required `river_jungle` profile and `p93` tradition | Required `mounted_mobile` profile and `p98` tradition |
| AI | Five package strategies are present | Five package strategies are present |
| Central admission | Adapter only, not attested | Adapter only, not attested |

## File-surface checklist

The paired gameplay source is in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt`, `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt`, `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`, `common/decisions/006_independence_wave_iw093_iw098_decisions.txt`, `common/ideas/006_independence_wave_ideas_registry.txt`, `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, and `localisation/english/006_independence_wave_iw093_iw098_l_english.yml`.

The shared dispatch, planner, force, formable, capacity, and Join surfaces are `common/scripted_effects/006_independence_wave_effects.txt`, `common/scripted_effects/006_independence_wave_package_planner_effects.txt`, `common/scripted_effects/006_independence_wave_force_package_effects.txt`, `common/scripted_effects/006_independence_wave_force_effects.txt`, `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_effects/006_independence_wave_join_effects.txt`, and `common/on_actions/006_independence_wave_on_actions_registry.txt`.

The shared character and portrait wiring is `common/characters/006_independence_wave_characters_registry.txt`, `interface/006_independence_wave_small_assets.gfx`, and `gfx/leaders/006_independence_wave/`.

## Map and state setup

Vanilla `history/states/274-British Africa.txt` has state 274 with provinces including Kumasi 12787 and VP 12787, while `history/states/902-Sokoto.txt` has state 902 with Sokoto province 1891 and VP 1891.

DOX reserves only state 274 and requires Kumasi province 12787 to be the capital proof; SOK reserves only state 902 and requires the Sokoto anchor proof.

The source package uses ownership, control, capital, and surviving-former-host checks before setup and final validation, so no broad northern-Nigeria or Gold-Coast ownership expansion is justified.

The shared `rg_nigeria_coarse` mutex is intentionally shared by IW-095, IW-097, IW-098, IW-099, IW-100, IW-106, and IW-107; this is a reservation design constraint, not a reason to widen capacity or alter map ownership.

The required read-only HOI4 map inspection for states 274 and 902 and provinces 12787, 10862, and 1891 timed out after 180 seconds, and the smaller retry returned `Transport closed`.

No map MCP artifact exists, so the state-file evidence above is not being represented as engine-render evidence.

## Politics, leaders, portraits, flags, advisors, and parties

DOX initializes neutrality with Asante-specific party names and requires `DOX_prempeh_ii` as the ruling Prempeh II leader in `common/characters/006_independence_wave_characters_registry.txt:363-375`; both DOX commanders are required by `has_independence_wave_iw093_command_roster`.

SOK initializes neutrality with Sokoto-specific party names and retains the dormant vanilla SOK identity; Event 006 requires date-appropriate leadership and blocks on Event 012 state safety.

SOK has no Event 006 Hasan character or pre-cutover role path. `has_independence_wave_iw098_date_appropriate_leadership` in `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt` is post-cutover-only and requires vanilla `SOK_siddiq_abubakar`, so every date before 1938-06-17 fails closed.

Event 012 owns the existing SOK Siddiq character and portrait surface; Event 006 must not duplicate or silently transfer that identity or its source/rights receipt.

The pair-specific portrait sprites are wired in `interface/006_independence_wave_small_assets.gfx:63-80` to runtime DDS files under `gfx/leaders/006_independence_wave/`.

`DOX_kwame_frimpong`, `DOX_kwaku_ntim`, and `SOK_bello_rabah` remain fictional ImageGen commander portraits documented in `docs/assets/006_independence_wave/iw093_iw098_commanders_2026_07_19/metadata/prompts.md`; fictional portraits do not close the grounded restored Asante/Sokoto identity gate.

The Dikko source trail is recorded in the research dossier, but an independently accepted current source/treatment receipt is still required before SOK command-roster attestation.

The Prempeh source master exists at `docs/assets/portraits/006_independence_wave/portrait_DOX_prempeh_ii_source.jpg`, but the previous portrait handoff records unresolved likeness/treatment acceptance, so it cannot be treated as final clearance.

All reviewed pair characters are explicitly male with male personal names; no opposite-gender portrait/name pairing or institutional-body random-name misuse was found.

Local DOX base and ideology flags exist at `gfx/flags/DOX*.tga`, but the exact period/route provenance is not verified and local DOX medium/small variants are absent.

No local SOK base, ideology, medium, or small flags exist; vanilla provides only SOK ideology variants, and no exact period/route flag receipt is admitted for Event 006.

No advisors or high-command entries are declared for either package; this matches the frozen package dossier rather than an invented generic leader fallback.

## Focus, decision, idea, formable, and asset issues

The shared focus tree has DOX roots for Kumasi administration, Form-24 preparation, sovereign Asante confederacy, and veterans guardianship, plus SOK roots for the emirate council, Form-25 preparation, and frontier command.

The 18 paid decisions are package-specific and use tracked values, project durations, and material costs; their source comments explicitly avoid direct formable commits, free divisions, and central content attestation.

DOX ideas `independence_wave_iw093_unsettled_restoration_idea` and `independence_wave_iw093_cocoa_rail_compact_idea` and SOK ideas `independence_wave_iw098_disputed_emirate_compact_idea` and `independence_wave_iw098_caravan_network_compact_idea` have source definitions, icons, and receiver localisation.

Form-24 and Form-25 are only discovery/transaction profiles in `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`; no actual WFX or SFX tag, country definition, history, member/territory contract, consent receipt, or formable flag family was found.

The formable gaps independently block final package attestation and must not be papered over with a generic federation or invented flag.

The installed HOI4 MCP exposes no Technology Tree Viewer. No package-specific Event 006 technology tree is authored; SOK retains vanilla `infantry_weapons = 1` and zero convoys in its dormant history, while Event 006 force setup remains dynamically gated.

## Starting military, technology, industry, supply, and production

DOX setup requires the current force mapping, `river_jungle` profile, and `p93` military tradition before `independence_wave_apply_dynamic_starting_force`; the shared force registry resolves profile p93 to `river_jungle` and tradition p93 to 64.

SOK setup requires the current force mapping, `mounted_mobile` profile, and `p98` military tradition before dynamic force application; the shared force registry resolves profile p98 to `mounted_mobile` and tradition p98 to 70.

Neither package has a static Event 006 army injection in country history; dynamic starting-force application is gated by command-roster, mapping, generation, and package setup receipts.

DOX source constants define anchor 274, Kumasi VP 12787, opening values 45/-25/25/15, and river-jungle force mapping; SOK defines anchor 902, opening values 50/-30/30/35, and mounted-mobile force mapping.

Both packages use the shared host-derived population, factories, infrastructure, rail, port, supply-node, convoy, train, fuel, equipment, and manpower budget calculations; no unbounded army, equipment, factory, or supply patch is warranted.

## AI and playability

DOX strategies `independence_wave_iw093_foundation`, `_host_crisis`, `_royal_confederacy`, `_constitutional_cabinet`, and `_veterans_emergency` are defined in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:1260-1320`.

SOK strategies `independence_wave_iw098_foundation`, `_host_crisis`, `_sultanic_federal`, `_northern_constitution`, and `_frontier_command` are defined in the same file immediately after the DOX block.

The mandatory probability inspection for these strategy factors could not run after the HOI4 MCP transport closed; no quantitative AI or admission claim is made from source-only inspection.

Join callbacks remain narrow and affected-country scoped in `common/on_actions/006_independence_wave_on_actions_registry.txt`; Join enforces independent, peaceful, non-origin, no-pending-operation, reduction, and coordinator-capacity gates and does not widen central package admission.

The planner host-loss ceiling and surviving-host-capital proof remain active; no capacity relaxation is safe while both packages are un-attested.

## Exact blockers and smallest next owner patch

1. The portrait/source owner must close grounded identity receipts: final accepted Prempeh II treatment, sourced Asante commander replacements for Frimpong and Ntim, a sourced Hasan dan Mu'azu Ahmadu pre-cutover character, an independently rights-cleared Event 006 Siddiq path if post-cutover is retained, and accepted sourced Dikko and Bello commander treatments. The portrait worker owns processing, runtime DDS/sprite outputs, manifests, and handoff; this agent must not use RunPod.
2. The asset/source owner must verify or replace exact period/route DOX and SOK flags and provide the consumer-required base/medium/small family with provenance and manifest evidence.
3. The formable owner must independently specify Form-24 and Form-25 identities, members, substate/territory proofs, consent, tags, flags, and integration before either package can satisfy its formable receipt.
4. After both packages independently pass identity, portrait, flag, formable, focus/decision, force, AI-probability, and final visual audits, the parent may add exact package IDs to the central attestation list and then review Join ordering. Do not perform that central patch before the independent receipts exist.

## Validation and limitations

The scoped `audit_event6_allocator.py` validator passed and reported the expected adapter-only fail-closed pair state.

Source review covered tag registration, country/history, state anchors, shared dispatch/attestation/planner/capacity/Join, focus, decisions, ideas, AI, characters, portraits, flags, formable profiles, force mapping, and Event 012 guards.

Vanilla state files, SOK history/character definitions, and vanilla flag files were inspected for the map and dormant-identity checks.

Read-only HOI4 map inspect/render, focus inspect, event inspect, and AI probability inspect were attempted; map calls timed out and subsequent focus/event/probability calls returned `Transport closed`, so no MCP artifacts can be cited.

Technology-tree inspection remains unresolved because the installed package exposes no Technology Tree Viewer.

Live game validation and map rewrite were skipped by task scope; no rollback or recovery evidence is needed because no map write occurred.

Simplifications and omissions: no implementation simplification was made; the packages remain intentionally incomplete and centrally unadmitted pending the blockers above.
