# IW-043 / IW-058 decisions and events handoff - 2026-07-18

Owner lane: `/root/iw043_iw058_decisions_finish`

Status: bounded decisions, incidents, and English localisation tranche complete; no commit created

## Owned files

- `common/decisions/categories/006_independence_wave_iw043_iw058_categories.txt`
- `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`
- `events/006_independence_wave_iw043_iw058.txt`
- `localisation/english/006_independence_wave_iw043_iw058_categories_l_english.yml`
- `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`
- `localisation/english/006_independence_wave_iw043_iw058_events_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw043_iw058_decisions_events_handoff_2026_07_18.md`

No scripted architecture, focus, country-core, GFX, DDS, portrait, advisor, spreadsheet, or protected BAY/RHI file was edited by this lane. In particular, the tranche adds zero advisor-art consumers and makes zero advisor-art changes.

## Implemented surface and identifiers

The implementation contains two decision categories, 32 decisions or missions, and 20 triggered incidents.

### IW-043: 15 decisions

1. `independence_wave_iw043_convene_delegation_roll_call`
2. `independence_wave_iw043_ratify_tatar_bashkir_representation`
3. `independence_wave_iw043_ratify_chuvash_municipal_autonomy`
4. `independence_wave_iw043_ratify_mari_udmurt_language_rights`
5. `independence_wave_iw043_ratify_resident_civic_and_religious_equality`
6. `independence_wave_iw043_secure_kazan_cheboksary_navigation`
7. `independence_wave_iw043_reopen_volga_customs_and_ferries`
8. `independence_wave_iw043_settle_muftiate_and_civic_courts`
9. `independence_wave_iw043_discipline_the_river_guard`
10. `independence_wave_iw043_repair_cheboksary_workshops`
11. `independence_wave_iw043_negotiate_former_host_transit`
12. `independence_wave_iw043_dispatch_volga_trade_delegation`
13. `independence_wave_iw043_hold_form12_accession_congress`
14. `independence_wave_iw043_hold_form13_compact_congress`
15. `independence_wave_iw043_reopen_congress_clause`

### IW-058: 17 decisions

1. `independence_wave_iw058_secure_mosul_council_quarter`
2. `independence_wave_iw058_enumerate_council_seats`
3. `independence_wave_iw058_ratify_assyrian_self_identification`
4. `independence_wave_iw058_ratify_chaldean_self_identification`
5. `independence_wave_iw058_ratify_syriac_self_identification`
6. `independence_wave_iw058_ratify_aramean_self_identification`
7. `independence_wave_iw058_settle_church_civil_competence`
8. `independence_wave_iw058_open_diaspora_expert_mission`
9. `independence_wave_iw058_discipline_levies_under_civilian_law`
10. `independence_wave_iw058_patrol_nineveh_approaches`
11. `independence_wave_iw058_fortify_mountain_river_corridor`
12. `independence_wave_iw058_request_named_external_guarantee`
13. `independence_wave_iw058_negotiate_former_host_security_settlement`
14. `independence_wave_iw058_survive_reclamation_crisis`
15. `independence_wave_iw058_hold_form18_federal_congress`
16. `independence_wave_iw058_ratify_sovereign_autonomy_compact`
17. `independence_wave_iw058_reopen_community_guarantee`

### Incident IDs

- IW-043 owns `chaosx.nr006.4301` through `chaosx.nr006.4310`.
- IW-058 owns `chaosx.nr006.5801` through `chaosx.nr006.5810`.
- All 20 IDs are unique across `events/`.

## Bounded target pools and relationship-aware reach

There are three explicit country-target lists:

| Decision | Count | Unique | Undefined | Duplicate | Carrier excluded |
|---|---:|---:|---:|---:|---|
| IW-043 Volga trade delegation | 150 | 150 | 0 | 0 | `CHU` absent |
| IW-058 diaspora expert mission | 150 | 150 | 0 | 0 | `ASY` absent |
| IW-058 named external guarantee | 150 | 150 | 0 | 0 | `ASY` absent |

The IW-043 pool retains the 136-tag canonical Event 006 set and uses the 14-tag diplomatic set `SOV ENG FRA GER USA TUR POL ROM FIN EST LAT LIT SWE PER`. The two IW-058 pools retain the same 136-tag canonical set and use `ENG FRA USA SOV GER ITA TUR IRQ SYR PER SAU JOR EGY GRE`. `SWE` and `GRE` complete the required 150-tag shapes without restoring the exact carrier.

Every listed tag resolves in the combined mod and vanilla `common/country_tags` registries. No targeted action uses `any_country`, `every_country`, `random_country`, or a periodic world scan.

The target triggers call the architecture-owned public wrappers in candidate `FROM` scope:

- `is_independence_wave_iw043_reachable_partner`
- `is_independence_wave_iw058_reachable_partner`

Each of the three target-selection AI blocks calls all five matching target-scope tiers:

- `*_major_reach`
- `*_treaty_reach`
- `*_league_reach`
- `*_patron_reach`
- `*_diaspora_reach`

The factors favor relationships appropriate to the action: treaty and league reach for Volga trade, league/patron/diaspora reach for the expert bureau, and major/treaty/patron reach for a named security guarantee. The target-country scope is always explicit through `FROM`.

## Exact formation binding and paid mission lifecycle

Six missions bind an existing supplied formation:

- `independence_wave_iw043_secure_kazan_cheboksary_navigation`
- `independence_wave_iw043_discipline_the_river_guard`
- `independence_wave_iw058_secure_mosul_council_quarter`
- `independence_wave_iw058_discipline_levies_under_civilian_law`
- `independence_wave_iw058_patrol_nineveh_approaches`
- `independence_wave_iw058_fortify_mountain_river_corridor`

All six use the same fail-closed lifecycle:

1. `available` and `custom_cost_trigger` require `can_bind_independence_wave_iw0xx_force_package`.
2. Activation calls `independence_wave_bind_iw0xx_force_package` before beginning the paid transaction.
3. The transaction starts only after the exact bind reports success.
4. The active flag and receipt are written only inside both the successful bind result and successful paid-transaction result.
5. A payment failure after binding releases the exact formation immediately.
6. Timeout removal revalidates the same generation-scoped formation before committing the transaction or success state.
7. The two discipline missions call `independence_wave_commit_iw0xx_force_discipline` after validation and require its success before writing civilian-control proof. They convert the bound formation to `Middle Volga River Guard` or `Assyrian Levies Detachment`; they do not create a unit.
8. Success, timeout, failed validation, cancellation, and package cleanup all release the binding. Rollback closes the transaction ledger and never returns the spent package.

The owned decision/event files contain no `create_unit`, `load_oob`, `add_equipment_to_stockpile`, or other free-unit reward.

## Concrete foreign relationships

### Volga trade

Successful removal of `independence_wave_iw043_dispatch_volga_trade_delegation` executes `give_market_access = FROM`. The agreement therefore creates real bilateral market access with the exact selected target, in addition to the IW-043 package-value changes.

### IW-058 diaspora bureau

Successful removal of `independence_wave_iw058_open_diaspora_expert_mission` saves the selected country as the regular chain target `independence_wave_iw058_diaspora_partner` and fires `chaosx.nr006.5805`. The incident requires that exact target to exist and remain out of war with the council. Options A and B create market access with the saved partner; option C closes the bureau and creates no relationship. The description names the selected country.

### IW-058 guarantee

Successful removal of `independence_wave_iw058_request_named_external_guarantee` saves the exact target and fires `chaosx.nr006.5807`.

- Option A makes the selected country execute `give_guarantee = ROOT` and records explicit sovereignty safeguards.
- Option B creates the same real guarantee, saves the exact guarantor as the patron action target, and registers the recognition patron channel with political leverage.
- Option C rejects the terms and creates no guarantee.

Neither acceptance option creates subject, client, puppet, or autonomy status. The targeted decisions and events write no cooldown or tombstone flag onto the foreign target country.

## Localisation coverage

The three dedicated English files remain UTF-8 with BOM and contain no duplicate keys:

- category localisation: 22 keys;
- decision localisation: 187 keys;
- event localisation: 171 keys.

All 32 decision name/description pairs, all 96 decision cost/effect tooltip references, and all 170 localisation-like `chaosx.nr006.43xx` / `58xx` references in event source resolve. Player-facing text describes the constitutional settlements, named partner relationships, concrete guarantee choices, and formation outcomes without transaction, adapter, registry, proof-writer, update-history, or fallback language. FORM-12/13/18 are presented as the Volga-Ural Accession Congress, Idel-Ural Compact Congress, and Mesopotamian Federal Congress.

## Meaningful validation evidence

- Source cardinality: 2 categories, 32 decision/mission blocks (15 IW-043 and 17 IW-058), 32 `ai_will_do` blocks, and 20 unique incident IDs.
- Reference resolution: all 37 scripted helper calls, 18 focus prerequisites, 12 idea references, and 75 distinct script-constant references used by the owned gameplay files resolve in current repository sources.
- Target integrity: all three pools contain exactly 150 unique defined tags; carrier exclusions, zero duplicates, and zero undefined tags were checked from source.
- Binding integrity: all six exact-formation missions contain two can-bind gates, bind-before-payment, exact validation on removal, and three authored release paths; both discipline missions gate civilian proof behind successful in-place conversion.
- Relationship integrity: source contains one selected-target Volga market-access effect, two exact diaspora-partner market-access outcomes, and two exact guarantor `give_guarantee = ROOT` outcomes.
- Scope integrity: no world-country iterator, target-country tombstone, unit-creation effect, or advisor-art reference exists in the owned gameplay files.

The required read-only `hoi4.event_inspect` was attempted twice. The bounded file lint timed out while building its graph; a narrow `chaosx.nr006.5805` state-flow request returned `EVENT_HELPER_PROJECTION_LIMIT` at the fixed 200,000-helper ceiling and produced no artifact. Direct source-linked cardinality, reference, state-lifecycle, and relationship checks above are therefore the available evidence for this lane.

## Simplifications, omissions, blockers, and parent follow-up

No fallback, placeholder, free unit, refund, carrier substitution, or deliberately weaker gameplay substitute was introduced in the owned tranche.

Two external completion dependencies remain and must not be mistaken for decision-layer fallbacks:

1. Architecture intentionally leaves FORM-12/13/18 readiness fail-closed until the exact keyed formable adapters are attested. These decisions cannot commit a generic formable.
2. The 20 referenced decision/category/report-event GFX consumers are owned by the parallel asset lane and were not registered by this lane at the time of this handoff. No advisor art is requested or permitted by these consumers.

The parent should run the independent decision/mission and event-completion audits after the asset lane and all package call sites have settled. This lane made no commit.
