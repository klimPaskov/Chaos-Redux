# Event 012 priority-member acceptance pass

Date: 2026-07-30

Scope: P1 acceptance audit of the sixteen rows in `docs/specs/012_africa_specs/matrices/012_africa_priority_member_package_matrix.csv`, the existing Independence Wave carrier handoff, and the current Event 012 priority-member package surface.

This handoff is an acceptance record, not a whole-country completion claim. It keeps the existing niche tags and vanilla carriers, makes no map or country-history changes, and records the three unbound packages as dormant.

## Disposition summary

Thirteen rows are reachable candidates on an existing live carrier, but remain pending end-to-end runtime acceptance because this agent cannot launch Hearts of Iron IV and the parent still owns the final campaign scenarios.

Three rows are blocked with a hard reachability gate because their only approved Event 006 carriers are currently unbound: Luba `DYX`, Lunda `DZX`, and Kilwa `EMX`.

Kongo `COG` is reachable only when the existing `COG_kingdom_of_kongo` cosmetic identity is already present. Event 012 does not create that cosmetic identity.

HZX Basotho, EUX Eswatini, and ELX Zanzibar are not priority-member rows. They remain host-only shells and are excluded from the sixteen-row disposition table.

## Sixteen-row matrix disposition

The valid scenario for every reachable row is the same bounded transaction: an existing carrier has an African owned and controlled capital, the required live origin proof, a committed Event 012 host, a passed promotion dossier, explicit Action 102 approval, and the exact origin-to-package match. Registration then writes only Event 012 package state on the original country scope, queues the appropriate sovereign handoff, loads or preserves the focus surface, applies the row-specific starting idea and force profile, and exposes the politics, League, overlap, refusal, and post-settlement lifecycle.

| Row | Package and carrier | Exact admission proof | Distinct package surfaces | Disposition and valid scenario | Invalid scenario that must stay closed |
| --- | --- | --- | --- | --- | --- |
| 1 | Asante `DOX` / IW-093 | `africa_priority_member_origin_is_asante` in `common/scripted_triggers/012_africa_priority_member_triggers.txt:116-123` requires the original `DOX` carrier or `africa_priority_origin_asante`, a live Event 006 receipt, and no Soviet origin. Current binding is state 274 Ghana in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`. | Starting idea `africa_priority_asante_starting_problem`; mechanic proof `africa_priority_asante_mechanic_complete`; stool/council clause `africa_priority_clause_stool_council_and_autonomy`; royal-guard profile; post proof `africa_priority_asante_post_settlement_action_completed`. | Reachable bounded package. Valid live `DOX` Event 006 origin passes the six-condition survey, Action 102 promotion, exact registration, council politics, League acceptance/counterproposal/refusal, overlap settlement, force reinforcement, and post-settlement action. | Bare `DOX`, an ended Event 006 receipt, a Soviet origin, an uncommitted host, a partial Action 102 result, or a second package must not register. Event 006 cleanup after registration now calls the bounded Event 012 focus restoration hook. |
| 2 | Oyo `DSX` / IW-097 | `africa_priority_member_origin_is_oyo` at `012_africa_priority_member_triggers.txt:125-133` requires `DSX` or its recorded origin plus a live Event 006 receipt. Current binding is state 558 Lagos. | `africa_priority_oyo_starting_problem`; `africa_priority_oyo_mechanic_complete`; `africa_priority_clause_corridor_and_city_compact`; mobile-guard profile with motorized payload; `africa_priority_oyo_post_settlement_action_completed`. | Reachable bounded package. Valid `DSX` origin can complete the Action 102 transaction on its original tag and follow the corridor/city, League, rival, and post-settlement branches. | Bare or ended `DSX`, Soviet provenance, no African controlled capital, wrong requested package, host not committed, or partial Action 102 must remain non-actionable. |
| 3 | Sokoto `SOK` / IW-098 | `africa_priority_member_origin_is_sokoto` at `012_africa_priority_member_triggers.txt:135-142` accepts the existing `SOK` carrier or recorded origin while excluding Soviet provenance. Vanilla `SOK` history remains authoritative. | `africa_priority_sokoto_starting_problem`; `africa_priority_sokoto_mechanic_complete`; `africa_priority_clause_emirate_jurisdiction_and_reform`; mobile-guard profile; `africa_priority_sokoto_post_settlement_action_completed`. | Reachable vanilla carrier. Valid `SOK` registration queues `africa_priority_member.1240`, recruits `africa_priority_sokoto_sovereign` exactly once, loads the shared tree only when the carrier is generic, and otherwise preserves the meaningful vanilla tree additively. | No package activation from a bare `SOK` without Action 102, a Soviet origin, a missing host commit, or a repeated `.1240` event may create a second sovereign or package. |
| 4 | Kanem-Bornu `DUX` / IW-099 | `africa_priority_member_origin_is_kanem_bornu` at `012_africa_priority_member_triggers.txt:144-152` requires `DUX` plus an active Event 006 receipt. Current binding is state 901 Borno. | `africa_priority_kanem_bornu_starting_problem`; `africa_priority_kanem_bornu_mechanic_complete`; `africa_priority_clause_lake_and_caravan_covenant`; mobile-guard profile with train payload; `africa_priority_kanem_bornu_post_settlement_action_completed`. | Reachable bounded package. Valid live `DUX` can use the lake/corridor mechanic, preferred League stage, refusal-to-resistance path, bounded force, and post-settlement action. | Bare `DUX`, ended receipt, unbound or Soviet origin, invalid host, or partial promotion remains closed. |
| 5 | Manden `MLI` / vanilla carrier | `record_supported_carrier_origin` in `common/scripted_effects/012_africa_priority_member_effects.txt:115-127` maps original `MLI` to `africa_priority_origin_manden`; `africa_priority_member_origin_is_manden` at `012_africa_priority_member_triggers.txt:154-158` requires that flag and rejects Soviet provenance. | `africa_priority_manden_starting_problem`; `africa_priority_manden_mechanic_complete`; `africa_priority_clause_assembly_and_corridor_guarantee`; mobile-guard profile; `africa_priority_manden_post_settlement_action_completed`. | Reachable vanilla carrier. Valid `MLI` retains its vanilla identity and generic tree unless a meaningful tree is present, then receives additive Event 012 decisions, ideas, forces, AI weights, sovereign recruitment, and settlement branches. | A tag-only `MLI` without a refreshed origin dossier, Soviet provenance, missing controlled base, wrong package ID, or partial Action 102 must not activate. |
| 6 | Kongo `COG` / existing cosmetic carrier | `africa_priority_member_origin_is_kongo` at `012_africa_priority_member_triggers.txt:160-167` accepts `original_tag = COG` only through `is_independence_wave_registry_africa_kongo_carrier`, which requires `has_cosmetic_tag = COG_kingdom_of_kongo`, or through the recorded origin flag. | `africa_priority_kongo_starting_problem`; `africa_priority_kongo_mechanic_complete`; `africa_priority_clause_cultural_citizenship_separate_from_territory`; river-guard profile with convoy payload; `africa_priority_kongo_post_settlement_action_completed`. | Reachable only with the existing Kongo cosmetic identity. Valid `COG` preserves meaningful `congo_focus` and sets `africa_priority_member_focus_tree_overlay_skipped` while the package adds its cross-border, civic, League, rival, force, and post-settlement surfaces. | Bare `COG` without `COG_kingdom_of_kongo`, a Soviet origin, a fabricated Event 012 cosmetic tag, map transfer, or a partial Action 102 result must stay closed. |
| 7 | Buganda `UGA` / vanilla carrier | `africa_priority_member_origin_is_buganda` at `012_africa_priority_member_triggers.txt:169-176` accepts original `UGA` or the recorded origin flag while excluding Soviet provenance. | `africa_priority_buganda_starting_problem`; `africa_priority_buganda_mechanic_complete`; `africa_priority_clause_kingdom_federal_balance`; royal-guard profile with convoy payload; `africa_priority_buganda_post_settlement_action_completed`. | Reachable vanilla carrier. Valid `UGA` receives the guarded sovereign handoff and the kingdom/federal balance package additively. | A bare `UGA` with no Action 102 promotion, a missing controlled base, Soviet provenance, or a repeated recruitment transaction remains closed. |
| 8 | Aksum `TIG` / nonmatching vanilla carrier | `record_supported_carrier_origin` maps original `TIG` to `africa_priority_origin_aksum`; `africa_priority_member_origin_is_aksum` at `012_africa_priority_member_triggers.txt:178-182` requires the recorded flag and excludes Soviet provenance. | `africa_priority_aksum_starting_problem`; `africa_priority_aksum_mechanic_complete`; `africa_priority_clause_heritage_without_annexation`; highland-guard profile; `africa_priority_aksum_post_settlement_action_completed`. | Reachable vanilla carrier. Valid `TIG` keeps the meaningful Horn tree when present and receives the Aksum heritage/civic, League, force, and post-settlement package additively. | Original `TIG` without the recorded Event 012 origin, a Soviet origin, an attempted Event 006 identity substitution, or no Action 102 must not activate Aksum. |
| 9 | Harar `HAR` / vanilla carrier | `africa_priority_member_origin_is_harar` at `012_africa_priority_member_triggers.txt:184-191` accepts original `HAR` or its origin flag while excluding Soviet provenance. | `africa_priority_harar_starting_problem`; `africa_priority_harar_mechanic_complete`; `africa_priority_clause_corridor_non_monopoly`; mobile-guard profile with train and motorized payload; `africa_priority_harar_post_settlement_action_completed`. | Reachable vanilla carrier. Valid `HAR` preserves meaningful Horn content and adds the city/corridor package and guarded sovereign handoff. | A bare `HAR` without Action 102, Soviet provenance, an uncommitted host, or an invalid capital/controller must stay closed. |
| 10 | Kilwa `EMX` / IW-117 | `africa_priority_member_origin_is_kilwa` at `012_africa_priority_member_triggers.txt:193-201` requires `EMX` or its origin flag plus an active Event 006 receipt. | `africa_priority_kilwa_starting_problem`; `africa_priority_kilwa_mechanic_complete`; `africa_priority_clause_distributed_customs_and_patrols`; coastal-guard profile with convoy and naval-experience payload; `africa_priority_kilwa_post_settlement_action_completed`. | Blocked with gate. The package source is complete, but current Event 006 binding is `unbound` / `disabled_no_unique_current_state`; no live receipt can be produced by the installed allocator. A future approved Event 006 binding may use the existing receipt path without changing Event 012. | Bare `EMX`, a speculative Tanganyika-state fallback, static history ownership, a new tag, or a fabricated receipt must remain impossible. |
| 11 | Nubia `SUD` / nonmatching vanilla carrier | `record_supported_carrier_origin` maps original `SUD` to `africa_priority_origin_nubia`; `africa_priority_member_origin_is_nubia` at `012_africa_priority_member_triggers.txt:203-207` requires that flag and excludes Soviet provenance. | `africa_priority_nubia_starting_problem`; `africa_priority_nubia_mechanic_complete`; `africa_priority_clause_dual_river_recognition`; mobile-guard profile with train/support payload; `africa_priority_nubia_post_settlement_action_completed`. | Reachable vanilla carrier. Valid `SUD` retains the vanilla capital, economy, and generic tree where applicable while adding the river-rights, dual-recognition, League, force, and post-settlement package. | A tag-only `SUD`, Soviet provenance, wrong package ID, no viable owned/controlled African base, or partial action must stay closed. |
| 12 | Luba `DYX` / IW-103 | `africa_priority_member_origin_is_luba` at `012_africa_priority_member_triggers.txt:209-217` requires `DYX` or its origin flag plus an active Event 006 receipt. | `africa_priority_luba_starting_problem`; `africa_priority_luba_mechanic_complete`; `africa_priority_clause_mining_revenue_and_local_consent`; river-guard profile; `africa_priority_luba_post_settlement_action_completed`. | Blocked with gate. Current Event 006 binding is `unbound` / `disabled_no_unique_current_state`; the broad Congo state 538 was rejected as non-unique. The package remains dormant until a separately approved Event 006 binding exists. | Bare `DYX`, a broad-state fallback, static territory/history, a fabricated receipt, or direct Event 012 release must remain closed. |
| 13 | Lunda `DZX` / IW-104 | `africa_priority_member_origin_is_lunda` at `012_africa_priority_member_triggers.txt:219-227` requires `DZX` or its origin flag plus an active Event 006 receipt. | `africa_priority_lunda_starting_problem`; `africa_priority_lunda_mechanic_complete`; `africa_priority_clause_cross_border_access_and_citizenship`; mobile-guard profile with motorized payload; `africa_priority_lunda_post_settlement_action_completed`. | Blocked with gate. Current Event 006 binding is `unbound` / `disabled_no_unique_current_state`; no uniquely evidenced Lunda anchor was accepted. | Bare `DZX`, speculative cross-border ownership, static history/map fallback, fabricated receipt, or direct Action 102 package registration must remain closed. |
| 14 | Great Zimbabwe `ZIM` / nonmatching vanilla carrier | `record_supported_carrier_origin` maps original `ZIM` to `africa_priority_origin_great_zimbabwe`; `africa_priority_member_origin_is_great_zimbabwe` at `012_africa_priority_member_triggers.txt:229-233` requires that flag and excludes Soviet provenance. | `africa_priority_great_zimbabwe_starting_problem`; `africa_priority_great_zimbabwe_mechanic_complete`; `africa_priority_clause_bounded_restoration_mandate`; highland-guard profile with motorized/support payload; `africa_priority_great_zimbabwe_post_settlement_action_completed`. | Reachable vanilla carrier. Valid `ZIM` receives the bounded restoration, land/heritage, League, rival, force, and post-settlement surfaces without a new Great Zimbabwe tag. | A tag-only `ZIM`, Soviet provenance, unsafe maximal-border transfer, or partial Action 102 must stay closed. |
| 15 | Merina `MAD` / vanilla carrier | `africa_priority_member_origin_is_merina` at `012_africa_priority_member_triggers.txt:235-242` accepts original `MAD` or its origin flag while excluding Soviet provenance. | `africa_priority_merina_starting_problem`; `africa_priority_merina_mechanic_complete`; `africa_priority_clause_asymmetric_island_federalism`; coastal-guard profile with convoy payload; `africa_priority_merina_post_settlement_action_completed`. | Reachable vanilla carrier. Valid `MAD` keeps its vanilla island setup and generic focus where applicable, recruits `africa_priority_merina_sovereign` through `.1240`, and receives the island confidence and post-settlement package additively. | A bare `MAD`, Soviet provenance, island-wide map rewrite, wrong package ID, or partial Action 102 must stay closed. |
| 16 | Zulu `EQX` / IW-121 | `africa_priority_member_origin_is_zulu` at `012_africa_priority_member_triggers.txt:244-252` requires `EQX` or its origin flag plus an active Event 006 receipt. Current binding is state 719 Natal, `ready_unique_state_confirmed`. | `africa_priority_zulu_starting_problem`; `africa_priority_zulu_mechanic_complete`; `africa_priority_clause_crown_land_and_labour_balance`; mobile-guard profile; `africa_priority_zulu_post_settlement_action_completed`. | Reachable bounded package. Valid live `EQX` can complete Action 102, load the Event 012 tree on the niche carrier, and run crown/land/labour, League, refusal/rival, force, overlap, and post-settlement branches on the original tag. | Bare `EQX`, ended receipt, Soviet origin, no host commit, partial Action 102, or a competing package must remain closed. |

## Country package coverage checklist

- Tag ownership: all sixteen rows resolve to existing `DOX`, `DSX`, `SOK`, `DUX`, `MLI`, `COG`, `UGA`, `TIG`, `HAR`, `EMX`, `SUD`, `DYX`, `DZX`, `ZIM`, `MAD`, and `EQX` carriers. No Event 012 country tag or priority-member cosmetic tag is defined.
- Provenance: the seven niche identities use `africa_priority_member_has_active_event6_shell_receipt` at `common/scripted_triggers/012_africa_priority_member_triggers.txt:93-96`; the nine vanilla carriers use direct or recorded identities, with Soviet-origin exclusion.
- Action 102: `africa_priority_member_can_register_package` at `common/scripted_triggers/012_africa_priority_member_triggers.txt:409-423` requires the active Event 012 global, host commit, explicit `africa_priority_package_promotion_approved`, no active package, and a valid exact origin. The Action 102 result is `promote_priority_member_package` in `common/scripted_effects/012_africa_action_effects.txt` and invokes `africa_priority_member_register_from_origin` only on the full result branch.
- Original-host preservation: `africa_priority_member_register_requested_package` at `common/scripted_effects/012_africa_priority_member_effects.txt:551-610` writes package state on the current scope, sets `africa_priority_member_content_loaded_on_original_tag`, and performs no owner, controller, core, capital, subject, faction, or cosmetic mutation.
- Kongo gate: `is_independence_wave_registry_africa_kongo_carrier` at `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:290-293` requires both original `COG` and `COG_kingdom_of_kongo`.
- Character ownership: the seven niche histories recruit their institutional sovereigns, while `events/012_africa_priority_member_events.txt:13-83` event `africa_priority_member.1240` queues exactly one guarded sovereign for the nine vanilla carriers. Political roles and party names are installed only by the explicit settlement helpers in `common/scripted_effects/012_africa_priority_member_character_effects.txt`.
- Politics: the three route helpers `africa_priority_member_apply_council_politics`, `africa_priority_member_apply_civic_politics`, and `africa_priority_member_apply_producer_politics` at `common/scripted_effects/012_africa_priority_member_effects.txt:636-712` provide distinct party names, ideologies, and package flags for all sixteen rows.
- Ideas: `common/ideas/012_africa_priority_member_ideas.txt` contains sixteen starting-problem ideas, three settlement ideas, and sixteen mature ideas; the clear/apply lifecycle is `common/scripted_effects/012_africa_priority_member_effects.txt:289-374`.
- Mechanics: `africa_priority_member_apply_mechanic_payload` at `common/scripted_effects/012_africa_priority_member_effects.txt:718-945` has a package-specific branch and completion flag for every row.
- Force identity: `common/scripted_effects/012_africa_priority_member_force_effects.txt:12-155` covers royal, river, mobile, highland, and coastal profiles; `:247-277` limits creation to an owned and controlled state, marks inherited carrier forces, and retries safely when no controlled state is available.
- League roles and refusal: preferred clauses for all sixteen packages are at `common/scripted_effects/012_africa_priority_member_effects.txt:1292-1308`; acceptance, counterproposal, resistance, refusal, withdrawal, and rivalry are implemented at `:1311-1456` and exposed by events `.1210` and `.1230`.
- Overlap and post-settlement: four settlement modes and package-specific overlap flags are recorded by `common/scripted_effects/012_africa_priority_member_effects.txt:1458-1697`; sixteen post-settlement completions are dispatched at `:1700-1819`.
- Focus lifecycle: `africa_priority_member_ensure_focus_tree_loaded` at `common/scripted_effects/012_africa_priority_member_effects.txt:258-287` loads `africa_priority_member_focus_tree` for niche/generic carriers with `keep_completed = yes`, preserves meaningful vanilla trees via `africa_priority_member_focus_tree_overlay_skipped`, and marks layout dirty. The tree is `common/national_focus/012_africa_priority_member_focus.txt`, ID `africa_priority_member_focus_tree`, with eight focus IDs.
- Decisions and AI: `common/decisions/012_africa_priority_member_decisions.txt` and category `common/decisions/categories/012_africa_priority_member_categories.txt` expose registration, politics, League, overlap, departure, sixteen mechanics, sixteen force decisions, and sixteen post-settlement decisions. Shared focus and decision AI weights are package-aware; no separate country AI file is required by the current compact architecture.
- Localisation and assets: package, focus, character, scripted-localisation, and GFX files contain the sixteen package identifiers. Current static checks find 119 unique DDS references across `interface/012_africa_priority_member_assets.gfx` and `interface/012_africa_priority_member_characters.gfx`, with zero missing files. The seven niche carrier flag ladders and the committed conditional-shell flag ladders resolve as TGA assets.
- Model boundary: no unit or building model was added or claimed. Force visuals remain documented consumers of the package force identity and are model-dependent until a separate approved model handoff exists.

## File surface checklist

| Surface | Current source of truth | Acceptance result |
| --- | --- | --- |
| Carrier registry and identity | `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:271-312`; `common/country_tags/006_independence_wave_countries.txt` | Existing tags only; COG cosmetic gate and MLI/TIG/SUD/ZIM nonmatching carrier group resolve. |
| Origin and promotion triggers | `common/scripted_triggers/012_africa_priority_member_triggers.txt:93-423` | Active receipt, exact origin, viable compact base, six-condition survey, local support, host commit, and Action 102 gates present. |
| Registration and lifecycle effects | `common/scripted_effects/012_africa_priority_member_effects.txt:21-617` | Full package registration, original-tag proof, starting problem, focus loader, sovereign queue, and bounded force initialization present. |
| Characters and sovereign handoff | `common/characters/012_africa_priority_member_characters.txt:10-158`; `common/scripted_effects/012_africa_priority_member_character_effects.txt`; `events/012_africa_priority_member_events.txt:13-83` | Sixteen titled sovereigns; female metadata is explicit for Aksum, Nubia, and Merina; no random opposite-gender name pool is used. |
| Politics and parties | `common/scripted_effects/012_africa_priority_member_character_effects.txt:23-621`; `common/scripted_effects/012_africa_priority_member_effects.txt:636-712` | Three package-aware routes and party names are present; role promotion waits for settlement. |
| Focus | `common/national_focus/012_africa_priority_member_focus.txt`; `common/scripted_effects/012_africa_priority_member_effects.txt:258-287`; `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:860-868,918-925` | Eight-focus shared tree, additive/preservation loader, and bounded DOX/SOK post-cleanup restoration hook are present; live campaign confirmation remains pending. |
| Decisions and missions | `common/decisions/012_africa_priority_member_decisions.txt`; `common/decisions/categories/012_africa_priority_member_categories.txt` | Registration, mechanic, force, League, overlap, departure, and post-settlement actions are present with package selectors. |
| Ideas | `common/ideas/012_africa_priority_member_ideas.txt`; `common/scripted_effects/012_africa_priority_member_effects.txt:289-374` | Starting, settlement, and mature lifecycle is present for all sixteen rows. |
| Force, equipment, supply | `common/scripted_effects/012_africa_priority_member_force_effects.txt`; `common/scripted_effects/012_africa_priority_member_effects.txt:947-1070` | Five structural force profiles and package payloads are bounded; no static army, technology, industry, port, rail, state, or supply mutation is performed by Event 012. |
| Localisation and visual assets | `localisation/english/012_africa_priority_member*_l_english.yml`; `interface/012_africa_priority_member*.gfx`; `gfx/leaders/012_africa/priority_members` | Current references resolve; older handoffs claiming missing DDS files are stale. |
| Docs and matrices | `docs/specs/012_africa_specs/matrices/012_africa_priority_member_package_matrix.csv`; this handoff; prior tag-loading and country audits | This dated handoff supersedes stale “all blocked because assets are missing” wording but does not supersede the historical ledger status. |

## Map and state setup issues

`africa_priority_member_has_viable_compact_base` at `common/scripted_triggers/012_africa_priority_member_triggers.txt:278-286` requires an African capital owned and controlled by the candidate and rejects capitulation.

The Event 012 package does not transfer territory, assign owners or controllers, grant cores, move capitals, create subjects, create factions, or apply cosmetic tags.

The current Event 006 binding ledger is the sole reachability authority for niche carriers: `DOX` state 274, `DSX` state 558, `DUX` state 901, and `EQX` state 719 are bound; `DYX`, `DZX`, and `EMX` are unbound and must remain dormant.

The blocked scenario arrays at `common/scripted_effects/006_independence_wave_scenario_effects.txt:1099-1122` must not be bypassed by Event 012.

HZX, EUX, and ELX remain host-only shells without a live country package that supplies a controlled African capital/core and generic focus. Their base, medium, and small flag ladders now exist in the current tree (`318cc9d89`), but flags do not create a playable country.

## Politics, leaders, portraits, flags, advisors, and parties

All sixteen sovereign IDs and portrait references are present. Aksum, Nubia, and Merina set `gender = female`; the other sovereign blocks do not set female metadata. Names are institutional or regnal titles such as Asantehene, Alaafin, Sultan, Mai, Mansa, Manikongo, Kabaka, Kandake, Mulopwe, Mwaant Yaav, King, and Queen.

The seven niche histories own the matching sovereign before runtime, and `.1240` owns the nine vanilla recruitment transactions. No Event 012 advisor, high-command, commander, or separate party roster is required by the current matrix.

Kongo's existing `COG_kingdom_of_kongo` cosmetic identity remains a prerequisite and is not created by this package.

## Focus, decision, idea, and asset issues

The shared eight-focus tree is intentionally compact and uses package-specific focus-step effects, localisation, ideas, decisions, and AI weights instead of sixteen cloned trees.

The read-only focus inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b059c81cf1975ce5e8dc14ebea9459fa801007e81ef8917f5560c203831534e7/58667f3fd5efbfcb000921e66cdf9d4f9d2877b23ecb65b389670383a12c5384/focus-inspect.5c0ab81c1958ab45.json`. It reports eight package focuses, no intersections, no package icon errors, and only three long-connector layout warnings.

The package focus loader preserves a meaningful vanilla tree by setting `africa_priority_member_focus_tree_overlay_skipped`; generic and niche carriers receive the shared tree on full registration.

Current interface references are technically present, but model-dependent force visuals remain consumers only and are not accepted as produced 3D assets.

## Starting military, technology, industry, supply, and production

The nine vanilla carriers retain their vanilla histories, technology, production, capital, convoys, economy, and OOB. The seven niche carriers receive their map, politics, technology, industry, supply, and AI setup from the live Event 006 runtime before Event 012 registration.

The bounded Event 012 force initializer creates one named template and at most a primary plus reserve formation, only on an owned and controlled state. It marks inherited carrier divisions rather than conjuring a full army and retries safely when control is temporarily absent.

The package payload dispatch adds bounded equipment, convoy, train, army-experience, and navy-experience values. It does not add research slots or rewrite production lines.

## AI and playability

Shared focus and decision AI weights distinguish route preferences and package mechanics. The six-condition promotion dossier and local-support floor prevent unsupported carriers from registering.

The valid live-carrier scenario requires a committed host, a current Event 006 receipt for the seven niche rows, exact origin proof, at least three survey criteria, minimum local support, explicit Action 102 promotion, and one safe owned/controlled state for force initialization.

The invalid scenario set includes bare dormant niche tags, ended receipts, Soviet origins, missing Kongo cosmetic identity, missing host commit, wrong requested package, duplicate active package, no viable African capital, all states occupied at force creation, and partial Action 102 outcomes. These paths must not write `africa_priority_member_package_active`.

Refusal and departure use the shared League state machine, clear constitutional acceptance, increase host rival pressure, and move the member through resistance/leaving/rival states. Post-settlement actions are available only after the package-specific focus and force/overlap requirements.

## DOX/SOK Event 006 focus cleanup ordering resolution

The parent authorized a bounded integration after the initial audit. The defect affected the direct niche `DOX` path and the Event 006 `SOK` path: Event 006 cleanup could replace the focus tree while leaving an active Event 012 package.

The Event 012 registration path can load `africa_priority_member_focus_tree` for a live `DOX` niche package at `common/scripted_effects/012_africa_priority_member_effects.txt:258-287,561-577` and leaves `africa_priority_member_package_active` and `africa_priority_member_focus_tree_loaded` set. A live Event 006 `SOK` package can instead preserve `independence_wave_focus_tree` under the meaningful-vanilla-tree branch, leaving the Event 012 overlay skipped while the Event 012 package is active.

Before the bounded fix, the Event 006 Asante cleanup at `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:813-864` called `load_focus_tree = { tree = generic_focus keep_completed = no }` after clearing the Event 006 tree without restoring an active Event 012 package tree.

The shared Event 006 reset and active-origin end at `common/scripted_effects/006_independence_wave_effects.txt:383-397,2799-2838` still clear Event 006 focus/runtime flags and dispatch Event 006 package cleanup, but intentionally do not call `africa_priority_member_cleanup_runtime` (`common/scripted_effects/012_africa_priority_member_effects.txt:1841-1863`), so the bounded restoration hook is needed when the Event 012 package survives.

Before the fix, if Event 006 IW-093 ended after a DOX Event 012 package had registered, cleanup could replace the Event 012 tree with `generic_focus` while the Event 012 package and loaded flag remained active. Before the fix, if Event 006 IW-098 ended after a SOK Event 012 package had registered, cleanup could replace the preserved Event 006 tree with `generic_focus` without ever loading the Event 012 tree. Those historical paths were inconsistent and were not acceptable final acceptance states.

The SOK cleanup retains its explicit contract that Event 012 focus and lifecycle flags are intentionally not cleared (`common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:867-919`); the new helper call now makes that preservation contract true for the focus tree as well.

The bounded fix is now present in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:860-868` for `independence_wave_cleanup_iw093_asante` and `:918-925` for `independence_wave_cleanup_iw098_sokoto`. Each path keeps the existing Event 006 cleanup and generic-tree load, then calls the public Event 012 helper `africa_priority_member_ensure_focus_tree_loaded = yes`. That helper is internally gated by `africa_priority_member_has_package`, so inactive cleanup is unchanged, while an active Event 012 package restores `africa_priority_member_focus_tree` and its loaded flag after Event 006 removes its tree.

The fix does not call `africa_priority_member_cleanup_runtime`; Event 012 package state remains owned by its terminal cleanup path, and the original-tag/additive loading contract is preserved.

Source-level scenarios passed for DOX inactive, DOX active, SOK inactive, and SOK active. Inactive cases leave the prior Event 006 generic-tree behavior intact because the Event 012 helper's package gate fails. Active DOX restores the Event 012 tree through the niche-tag branch; active SOK restores it through the post-cleanup `generic_focus` branch.

The remaining limitation is live campaign validation, which is parent-owned because agents must not launch Hearts of Iron IV.

## Changes in this pass

Changed files: only this dated handoff was added.

Gameplay files changed: `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt` only, in the two authorized cleanup effects. No Event 012 gameplay file or helper was changed because the existing public loader was sufficient.

Tags, states, leaders, parties, focus IDs, localisation keys, formables, assets, and map bindings changed: none.

No commit was created, as requested by the parent task.

## Validation and skipped validation

Performed read-only source checks for all sixteen package IDs across triggers, effects, focus, decisions, ideas, characters, localisation, scripted localisation, GFX, and carrier registry files.

Performed four source scenarios against the cleanup call order and Event 012 helper gate: DOX inactive `PASS`, DOX active `PASS`, SOK inactive `PASS`, and SOK active `PASS`.

Performed the read-only national-focus inspection for `africa_priority_member_focus_tree`; package diagnostics found no icon-reference errors or focus intersections and only the three recorded long-connector warnings.

Performed static DDS path resolution against the two priority-member GFX files; 119 unique references were found and zero were missing.

Performed current flag-ladder checks for the seven niche tags and the three host shells; base, medium, and small files exist for all ten tags, but host-shell flags do not satisfy the live host map/capital/core/focus gate.

Skipped live campaign and in-game validation because agents must not launch Hearts of Iron IV. Parent-owned scenarios remain required for final acceptance of the thirteen reachable carriers.

## Remaining risks and simplifications

The thirteen reachable rows are source-complete bounded packages, not final end-to-end accepted campaigns until the parent runs the valid and invalid live-carrier scenarios.

DYX, DZX, and EMX intentionally remain dormant; no territory, static history, new tag, cosmetic substitute, or fallback was added.

HZX, EUX, and ELX intentionally remain host-only; current flags are presentation assets only and do not authorize shell materialization.

The DOX/SOK Event 006 cleanup ordering defect is resolved at source level; live campaign confirmation remains pending.

No model package was created; model-dependent force visuals remain documented consumers.

The historical `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` still marks all sixteen rows blocked and contains stale older asset wording. This handoff records current source evidence and does not rewrite that shared historical ledger.
