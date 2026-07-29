# Event 012 Africa country-package and conditional-shell audit handoff

Date: 2026-07-30.

Scope: read-only audit of the sixteen Event 012 priority-member packages, the seven existing Event 006 niche carriers, and the conditional Event 006 host shells HZX, EUX, and ELX.

This handoff was checked against `AGENTS.md`, the required offline Paradox wiki pages, the installed vanilla documentation and country precedents, the Event 012 specifications and matrices, the Event 006 registry and map-binding notes, and the current Chaos Redux source and asset tree.

No gameplay, map, country, tag, localisation, focus, decision, idea, AI, or asset file was changed by this audit, and no commit was created.

## Executive result

The sixteen requested priority identities are wired to existing carriers and do not require a new Event 012 tag or priority-member cosmetic tag.

Seven packages use existing Event 006 niche tags: DOX Asante, DSX Oyo, DUX Kanem-Bornu, DYX Luba, DZX Lunda, EMX Kilwa, and EQX Zulu.

Nine packages use existing vanilla tags: SOK Sokoto, MLI Manden, COG Kongo, UGA Buganda, TIG Aksum, HAR Harar, SUD Nubia, ZIM Great Zimbabwe, and MAD Merina.

The seven niche origins are actionable only while their current country carries a live Event 006 origin receipt, as enforced by `africa_priority_member_has_active_event6_shell_receipt` in `common/scripted_triggers/012_africa_priority_member_triggers.txt:88-96`.

The installed Event 006 map-binding ledger marks DOX, DSX, DUX, and EQX as current-map-ready, while DYX, DZX, and EMX are dormant or unbound because no unique current state was accepted; a bare DYX, DZX, or EMX tag therefore cannot receive Event 012 content.

HZX Basotho, EUX Eswatini, and ELX Zanzibar are conditional Event 006 host shells, not priority-member carriers.

Event 012 maps HZX, EUX, and ELX to compact host playbooks, but they can receive host content only after another runtime has instantiated a real country with an African controlled capital/core, generic focus, and pre-fire contact.

There is no Event 012 priority origin flag, package ID, release path, or creation fallback for HZX, EUX, or ELX.

The current tree has no base, medium, small, or ideology flag files for HZX, EUX, or ELX, so any future shell-instantiation path needs an explicit flag asset decision before it can claim host-shell playability.

## Carrier and package coverage checklist

### Existing Event 006 niche carriers

| Package | Carrier and registry | Country/history surface | Origin and focus loading | Map and playability status | Asset and effect status |
| --- | --- | --- | --- | --- | --- |
| Asante | DOX, IW-093, `is_independence_wave_registry_africa_asante_carrier` | `common/countries/006_independence_wave_DOX.txt:4-11`; `history/countries/DOX - Asante.txt:4-10`; shell history recruits `africa_priority_asante_sovereign` | `africa_priority_origin_asante` requires DOX and a live Event 006 receipt; Event 012 package registration calls `africa_priority_member_ensure_focus_tree_loaded` and directly loads `africa_priority_member_focus_tree` for the seven niche tags | Binding ledger: state 274 Ghana, `ready_high_chaos`; Event 006 runtime must assign state, capital, politics, forces, ideas, and AI before promotion | Base/medium/small DOX flags exist; starting problem, mechanic, force, League, overlap, and post-settlement branches are present in the shared package effects |
| Oyo | DSX, IW-097, `is_independence_wave_registry_africa_oyo_carrier` | `common/countries/006_independence_wave_DSX.txt:4-11`; `history/countries/DSX - Oyo.txt:4-10`; recruits `africa_priority_oyo_sovereign` | DSX plus live Event 006 receipt; direct niche focus-tree load | Binding ledger: state 558 Lagos, `ready_high_chaos`; no fixed history setup beyond dormant sovereign | Base/medium/small DSX flags exist; package-specific corridor, city, force, League, overlap, and post-settlement effects are present |
| Kanem-Bornu | DUX, IW-099, `is_independence_wave_registry_africa_kanem_bornu_carrier` | `common/countries/006_independence_wave_DUX.txt:4-11`; `history/countries/DUX - Kanem-Bornu.txt:4-10`; recruits `africa_priority_kanem_bornu_sovereign` | DUX plus live Event 006 receipt; direct niche focus-tree load | Binding ledger: state 901 Borno, `ready_high_chaos`; Event 006 runtime supplies the compact country setup | Base/medium/small DUX flags exist; lake, caravan, mobile-force, League, overlap, and post-settlement effects are present |
| Luba | DYX, IW-103, `is_independence_wave_registry_africa_luba_carrier` | `common/countries/006_independence_wave_DYX.txt:4-11`; `history/countries/DYX - Luba.txt:4-10`; recruits `africa_priority_luba_sovereign` | DYX plus live Event 006 receipt; direct niche focus-tree load only after Event 006 instantiation | Binding ledger: `unbound`, `disabled_no_unique_current_state`; broad Congo state 538 was rejected as a non-unique Luba anchor | Base/medium/small DYX flags exist and package effects are complete, but the package is not reachable from the dormant bare tag |
| Lunda | DZX, IW-104, `is_independence_wave_registry_africa_lunda_carrier` | `common/countries/006_independence_wave_DZX.txt:4-11`; `history/countries/DZX - Lunda.txt:4-10`; recruits `africa_priority_lunda_sovereign` | DZX plus live Event 006 receipt; direct niche focus-tree load only after Event 006 instantiation | Binding ledger: `unbound`, `disabled_no_unique_current_state`; no uniquely evidenced Lunda state was accepted | Base/medium/small DZX flags exist and package effects are complete, but the package is not reachable from the dormant bare tag |
| Kilwa | EMX, IW-117, `is_independence_wave_registry_africa_kilwa_carrier` | `common/countries/006_independence_wave_EMX.txt:4-11`; `history/countries/EMX - Kilwa Restoration.txt:4-10`; recruits `africa_priority_kilwa_sovereign`; public localisation uses Kilwa/Kilwan | EMX plus live Event 006 receipt; direct niche focus-tree load only after Event 006 instantiation | Binding ledger: `unbound`, `disabled_no_unique_current_state`; broad Tanganyika state 546 was rejected as a non-unique Kilwa anchor | Base/medium/small EMX flags exist and coastal, customs, force, League, overlap, and post-settlement effects are present, but the package is not reachable from the dormant bare tag |
| Zulu | EQX, IW-121, `is_independence_wave_registry_africa_zulu_carrier` | `common/countries/006_independence_wave_EQX.txt:4-11`; `history/countries/EQX - Zulu.txt:4-10`; recruits `africa_priority_zulu_sovereign` | EQX plus live Event 006 receipt; direct niche focus-tree load | Binding ledger: state 719 Natal, `ready_unique_state_confirmed`; Event 006 runtime supplies the compact country setup | Base/medium/small EQX flags exist; crown, land, labour, force, League, overlap, and post-settlement effects are present |

The niche country definitions intentionally contain only African graphical cultures and a map colour, while the histories contain only the dormant sovereign recruitment line.

The intended Event 006 runtime package owns territory, capital, politics, leaders, forces, ideas, focus loading, and AI for these shells, so adding static capitals or ownership in Event 012 would violate the accepted carrier design.

### Existing vanilla carriers

| Package | Carrier and origin path | Vanilla setup and focus state | Event 012 registration and identity surfaces | Findings |
| --- | --- | --- | --- | --- |
| Sokoto | SOK, `is_independence_wave_registry_africa_sokoto_carrier` | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\SOK - Sokoto.txt:1-25` has capital 902, vanilla technology, zero convoys, and generic focuses completed; vanilla history also has `SOK_siddiq_abubakar` | Direct SOK origin path; hidden `africa_priority_member.1240` recruits `africa_priority_sokoto_sovereign`; generic focus receives the Event 012 tree, while a meaningful existing tree is preserved | No mod flag or country-definition replacement is needed; package effects add ideas, bounded force, decisions, and AI-facing focus weights on SOK |
| Manden | MLI, nonmatching vanilla carrier | `...\history\countries\MLI - Mali.txt:1-44` has capital 556, vanilla technology, zero convoys, and generic focuses completed | `record_supported_carrier_origin` maps MLI to `africa_priority_origin_manden`; hidden `.1240` recruits `africa_priority_manden_sovereign`; generic MLI can load `africa_priority_member_focus_tree` | Vanilla country identity, politics, technology, and economy remain intact; Event 012 adds only the validated package surfaces |
| Kongo | COG, `is_independence_wave_registry_africa_kongo_carrier` | `...\history\countries\COG - Congo.txt:1-32` has capital 295, `COG_1936`, and vanilla Congo setup; vanilla `common\national_focus\congo.txt:9-22` provides `congo_focus` when the relevant DLC is active | Kongo origin requires `original_tag = COG` and `has_cosmetic_tag = COG_kingdom_of_kongo`; hidden `.1240` recruits `africa_priority_kongo_sovereign`; meaningful `congo_focus` is preserved and `africa_priority_member_focus_tree_overlay_skipped` is set | The package is additive and does not create a Kongo cosmetic tag; if the required cosmetic identity is absent, the Kongo origin predicate correctly does not validate |
| Buganda | UGA, `is_independence_wave_registry_africa_buganda_carrier` | `...\history\countries\UGA - Uganda.txt:1-45` has capital 548, vanilla technology, zero convoys, and generic focuses completed | Direct UGA origin path; hidden `.1240` recruits `africa_priority_buganda_sovereign`; generic UGA can load the shared tree | Vanilla UGA tag and starting setup remain authoritative |
| Aksum | TIG, nonmatching vanilla carrier | `...\history\countries\TIG - Tigray.txt:1-23,58-64` has capital 842, vanilla technology, ten convoys, and generic history completion; `common\national_focus\horn_of_africa.txt:9-28` supplies `horn_of_africa_tree` for TIG when By Blood Alone is active | `record_supported_carrier_origin` maps TIG to `africa_priority_origin_aksum`; hidden `.1240` recruits `africa_priority_aksum_sovereign`; the meaningful Horn tree is preserved and the Event 012 overlay is skipped | Aksum is deliberately distinct from the Event 006 Tigray identity; no tag or focus replacement is required |
| Harar | HAR, `is_independence_wave_registry_africa_harar_carrier` | `...\history\countries\HAR - Harar.txt:1-23,58-64` has capital 835, vanilla technology, ten convoys, and generic history completion; Horn of Africa tree is available under By Blood Alone | Direct HAR origin path; hidden `.1240` recruits `africa_priority_harar_sovereign`; meaningful Horn tree is preserved and the Event 012 overlay is skipped | Harar receives additive package decisions, ideas, force setup, and AI-facing weights without losing the existing Horn content |
| Nubia | SUD, nonmatching vanilla carrier | `...\history\countries\SUD - Sudan.txt:1-44` has capital 551, vanilla technology, twenty convoys, and generic focuses completed | `record_supported_carrier_origin` maps SUD to `africa_priority_origin_nubia`; hidden `.1240` recruits `africa_priority_nubia_sovereign`; generic SUD can load the shared tree | Sudan's existing tag, capital, and economy remain authoritative |
| Great Zimbabwe | ZIM, nonmatching vanilla carrier | `...\history\countries\ZIM - Zimbabwe.txt:1-46,70` has capital 545, `ZIM_1936`, vanilla technology, five convoys, and generic focuses completed | `record_supported_carrier_origin` maps ZIM to `africa_priority_origin_great_zimbabwe`; hidden `.1240` recruits `africa_priority_great_zimbabwe_sovereign`; generic ZIM can load the shared tree | No separate Great Zimbabwe tag is created; package identity remains an additive Event 012 overlay on ZIM |
| Merina | MAD, `is_independence_wave_registry_africa_merina_carrier` | `...\history\countries\MAD - Madagascar.txt:1-24,47-53` has capital 543, vanilla technology, five convoys, and generic focuses completed | Direct MAD origin path; hidden `.1240` recruits `africa_priority_merina_sovereign`; generic MAD can load the shared tree | Madagascar's existing tag, capital, industry, technology, and naval setup remain authoritative |

The nine vanilla carriers use their owning tags and receive no Event 012 country-definition or history replacement.

The hidden recruitment event is intentionally limited to these nine carriers, while the seven niche shells already recruit their matching sovereign in country history.

## Exact file-surface checklist

The carrier registry is `common/country_tags/006_independence_wave_countries.txt:55-72` for DOX, DSX, DUX, DYX, DZX, ELX, EMX, EQX, HZX, and EUX.

The Event 006 carrier predicates are `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:286-312`, including the Kongo cosmetic requirement and the nonmatching MLI/TIG/SUD/ZIM carrier group.

The Event 012 package-origin and lifecycle predicates are `common/scripted_triggers/012_africa_priority_member_triggers.txt:73-112,116-251,259-274,278-353,377-423`.

The Event 012 origin-recording and package-registration effects are `common/scripted_effects/012_africa_priority_member_effects.txt:21-127,376-617`.

The shared focus loader is `common/scripted_effects/012_africa_priority_member_effects.txt:258-287`.

The shared focus tree is `common/national_focus/012_africa_priority_member_focus.txt`, with tree ID `africa_priority_member_focus_tree` and eight focus IDs: `africa_priority_define_compact_country`, `africa_priority_ratify_political_settlement`, `africa_priority_build_distinct_institution`, `africa_priority_secure_economic_function`, `africa_priority_negotiate_league_role`, `africa_priority_field_national_force`, `africa_priority_resolve_overlap_question`, and `africa_priority_write_post_settlement_programme`.

The decision category is `common/decisions/categories/012_africa_priority_member_categories.txt:9-18` with ID `africa_priority_member_category` and icon `GFX_decision_012_africa_priority_member_category`.

The decision surface is `common/decisions/012_africa_priority_member_decisions.txt`, and all sixteen package tokens appear in the current file.

The idea lifecycle is `common/ideas/012_africa_priority_member_ideas.txt`, with sixteen starting-problem ideas, three settlement ideas, and sixteen mature package ideas wired by `africa_priority_member_apply_starting_problem_idea`, `africa_priority_member_apply_political_settlement_idea`, and `africa_priority_member_apply_mature_compact_idea` in `common/scripted_effects/012_africa_priority_member_effects.txt:289-374`.

The bounded starting-force implementation is `common/scripted_effects/012_africa_priority_member_force_effects.txt:1-277`.

The hidden vanilla sovereign handoff is `events/012_africa_priority_member_events.txt:13-83`, event ID `africa_priority_member.1240`.

The sixteen sovereign character definitions are `common/characters/012_africa_priority_member_characters.txt:10-158`.

The portrait registrations are `interface/012_africa_priority_member_characters.gfx`, with sixteen `GFX_portrait_012_africa_priority_*_sovereign` sprites.

The focus, idea, decision, and report registrations are `interface/012_africa_priority_member_assets.gfx`.

The package and focus localisation is in `localisation/english/012_africa_priority_member_l_english.yml` and `localisation/english/012_africa_priority_member_focus_l_english.yml`.

The sovereign localisation is `localisation/english/012_africa_priority_member_characters_l_english.yml`.

The seven niche country localisation and ideology names are in `localisation/english/006_independence_wave_countries_l_english.yml`.

The route-level cosmetic identities are in `common/countries/012_africa_cosmetic.txt`; no Event 012 priority-member cosmetic identity is defined.

The reusable country collections are in `common/collections/chaosx_country_collections.txt:80-97`; Event 012 consumes the African views without inventing new tags.

## Map and state setup issues

`africa_priority_member_has_viable_compact_base` in `common/scripted_triggers/012_africa_priority_member_triggers.txt:278-286` requires an existing country whose capital is on Africa, owned and controlled by the country, and not capitulated.

Event 012 package registration does not transfer states, assign owners or controllers, add cores, move capitals, create subjects, or apply cosmetic tags.

Starting-force initialization only runs when the package has at least one owned and controlled state, as shown by `common/scripted_effects/012_africa_priority_member_force_effects.txt:247-277`; a package can therefore remain registered with its force-initialized flag unset until a safe controlled state exists, which is an intentional bounded retry rather than a state-transfer fallback.

For the seven niche shells, all map setup remains Event 006 runtime-owned, and the current map-binding ledger is the authoritative gate.

The current binding evidence is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`: DOX state 274 Ghana, DSX state 558 Lagos, DUX state 901 Borno, EQX state 719 Natal, DYX and DZX unbound, EMX unbound, HZX and EUX unbound, and ELX scenario-only unbound.

The Event 006 scenario initializer explicitly places DYX, DZX, ELX, EMX, HZX, and EUX in the blocked package arrays in `common/scripted_effects/006_independence_wave_scenario_effects.txt:1099-1122`.

No map rewrite was performed, and no current source evidence justifies adding a static fallback state for any dormant shell.

## Conditional host shells HZX, EUX, and ELX

HZX is registered as IW-124 Basotho, EUX as IW-125 Eswatini, and ELX as IW-116 Zanzibar in `common/country_tags/006_independence_wave_countries.txt:65,71-72`.

Their country definitions contain only African graphical cultures and colours: `common/countries/006_independence_wave_HZX.txt:4-11`, `common/countries/006_independence_wave_EUX.txt:4-11`, and `common/countries/006_independence_wave_ELX.txt:4-11`.

Their history shells are intentionally empty of capital, ownership, politics, OOB, technology, or force setup: `history/countries/HZX - Basotho.txt:4-7`, `history/countries/EUX - Eswatini.txt:4-7`, and `history/countries/ELX - Zanzibar.txt:4-7`.

Event 012 maps HZX to `africa_host_playbook.basutoland`, EUX to `africa_host_playbook.swaziland`, and ELX to `africa_host_playbook.zanzibar` in `common/scripted_effects/012_africa_effects.txt:342-346`.

The three tags are included in `africa_has_mapped_host_playbook` in `common/scripted_triggers/012_africa_triggers.txt:37-93`.

They are eligible for host initialization only through `africa_is_eligible_host` in `common/scripted_triggers/012_africa_triggers.txt:331-364`, which requires a live country, pre-fire contact, `has_focus_tree = generic_focus`, a controlled African capital, an African core, no capitulation or civil war, and no terminal or world-end flags.

The canonical host initializer is `africa_initialize_selected_host` in `common/scripted_effects/012_africa_effects.txt:398-528`; it saves the host target, applies the mapped playbook, and loads the continental host tree, but it does not make a dormant shell exist.

There is no `africa_priority_origin_basutoland`, `africa_priority_origin_swaziland`, or `africa_priority_origin_zanzibar`, no corresponding package ID, and no package branch for any of these shells.

Conclusion: HZX, EUX, and ELX can safely receive Event 012 host playbook content only if Event 006 or another approved runtime has already materialized a valid country, but they must never be treated as priority-member carriers and Event 012 must not release or create them as a fallback.

No HZX, EUX, or ELX base, medium, small, or ideology flag files exist under `gfx/flags`, `gfx/flags/medium`, or `gfx/flags/small` in the current mod tree.

The missing shell flags are a presentation and future-instantiation blocker, not a reason to add a fallback tag or static history.

## Politics, leaders, portraits, flags, advisors, and parties

All sixteen sovereign IDs are present in `common/characters/012_africa_priority_member_characters.txt` and all sixteen portrait GFX references resolve under `gfx/leaders/012_africa/priority_members`.

The Aksum, Nubia, and Merina sovereigns explicitly use `gender = female` in `common/characters/012_africa_priority_member_characters.txt:74-82,102-110,139-147`; the remaining sovereign blocks do not set female metadata.

The seven niche histories recruit their matching sovereign directly, while the nine vanilla carriers use the guarded `.1240` event recruitment path.

The public names are sovereign offices and titles rather than personal-name pools, for example Asantehene, Alaafin, Sultan, Queen, Kandake, and King.

If the portrait source package is treated as fictional personal leaders rather than institutional or regnal office portraits, the repository rule requiring actual-ish, gender-correct personal name pools remains an unresolved identity-design decision; this audit does not silently redesign those names.

No Event 012 advisor, high-command, commander, or separate party roster is required by the current package specification, and no narrow parser defect was found in those surfaces.

Kongo requires its existing `COG_kingdom_of_kongo` cosmetic identity for the priority origin predicate; Event 012 does not create or overwrite that cosmetic identity.

The seven niche tags have base, medium, and small flag ladders: `DOX`, `DSX`, `DUX`, `DYX`, `DZX`, `EMX`, and `EQX` under `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small`.

Ideology-specific niche flag variants are not present, but the base ladder is a valid HOI4 fallback and matches the accepted asset scope.

## Focus, decision, idea, and asset issues

The package deliberately uses one shared eight-focus tree instead of sixteen cloned trees, with package-specific focus-step effects, ideas, decision rows, scripted localisation, and AI weights providing identity differences.

This is consistent with the anti-bloat design in `docs/specs/012_africa_specs/specs/012_africa_spec_part_9_priority_member_country_packages.md`; it is an accepted architecture rather than a missing route family.

Static asset path checks report 103 unique DDS references in `interface/012_africa_priority_member_assets.gfx` and zero missing files.

The character GFX path check reports sixteen unique portrait DDS references and zero missing files.

The current asset tree therefore supersedes older handoffs that described unresolved Event 012 focus, idea, decision, report, or portrait paths.

## Starting military, technology, industry, supply, and production

Event 012's five starting-force profiles are royal guard, river guard, mobile guard, highland guard, and coastal guard, covering all sixteen package IDs in `common/scripted_effects/012_africa_priority_member_force_effects.txt:12-155`.

Registration creates one package-named division template, bounded primary and reserve formations, and support-dependent equipment and manpower factors, without conjuring a full army.

The effect dispatch provides package-specific equipment, convoy, train, experience, and navy-experience payloads in `common/scripted_effects/012_africa_priority_member_effects.txt:947-1060`.

The nine vanilla carriers retain their vanilla starting capitals, technology, production, convoys, OOB, and politics; Event 012 does not grant a research slot or rewrite their economy.

The seven niche shells receive military, technology, industry, and supply setup from Event 006 runtime before Event 012 can register their package.

No state ownership, port, railway, resource, supply-network, production-line, or technology mutation was found in the narrow Event 012 country-package surface.

## AI and playability

AI-facing focus weights and package-specific decision weights are present in the shared focus and decision systems, and all sixteen package tokens appear in the current trigger, effect, idea, decision, localisation, and scripted-localisation files.

There is no separate per-country Event 012 AI-strategy file; package-specific route preferences are implemented through shared focus-step and decision weights, which is compact but less explicit than sixteen dedicated strategy plans.

The force initializer has an idempotent retry guard and only spawns on an owned controlled state, preventing invalid map placement.

The promotion survey requires a viable compact base, an operating institution, documented strategic function, population and infrastructure, an unresolved League problem, a distinct package identity, and local support before registration; these gates are visible in `common/scripted_triggers/012_africa_priority_member_triggers.txt:288-353`.

The direct niche packages remain unplayable from bare dormant tags by design, and HZX/EUX/ELX remain host-only shells until an approved runtime supplies map state.

## Missing, stale, or blocked surfaces

The first blocker is reachability for DYX, DZX, and EMX: their package content exists, but the current Event 006 map ledger marks them unbound and the Event 012 origin predicates require a live Event 006 receipt.

The smallest safe future change is a separately reviewed Event 006 map-binding and admission design, followed by the existing receipt path; an Event 012 release or country-creation fallback would violate the current specification.

The second blocker is HZX/EUX/ELX shell presentation: no flags exist for these dormant host shells, so any future materialization needs reviewed base and small/medium flag assets.

The third risk is focus lifecycle ordering when a live Event 006 meaningful tree and direct Event 012 niche loading meet on the same carrier.

The fourth design risk is title-based sovereign localisation if the portrait provenance is judged to depict fictional personal leaders rather than regnal or institutional identities.

Older handoffs that claim missing Event 012 DDS assets or only eight installed portraits are stale against the current filesystem path checks and should be reconciled by the documentation owner.

No fallback, replacement tag, static shell history, or broad identity redesign was introduced by this audit.

## Validation and skipped checks

The source audit confirmed sixteen package tokens in the priority trigger, effect, idea, decision, package, scripted-localisation, and localisation surfaces, plus sixteen sovereign character IDs.

The GFX path audit confirmed 103 unique focus, idea, decision, and report DDS references and sixteen sovereign portrait references with zero missing paths.

The flag audit confirmed base, medium, and small ladders for DOX, DSX, DUX, DYX, DZX, EMX, and EQX, and confirmed no corresponding HZX, EUX, or ELX files.

Vanilla history and focus precedents were inspected for MLI, TIG, SUD, ZIM, SOK, UGA, HAR, MAD, and COG, including capitals, generic focus completion, OOB/convoy surfaces, and meaningful Horn or Congo focus-tree IDs.

The Event 006 binding CSV and blocked scenario registry were inspected for all seven niche carriers and the three conditional shells.

No Hearts of Iron IV executable, save, live event, focus renderer, map rewrite, or in-game state-transfer test was run because repository instructions reserve live consumer validation for the user and prohibit agents from launching the game.

## Changed files and parent handoff

Changed file: `docs/plans/012_africa_plans/subagent_handoffs/2026-07-30_event012_africa_country_package_audit_handoff.md`.

Changed identifiers: none; this is a documentation-only handoff.

Gameplay files changed: none.

Remaining parent actions are to preserve the dormant fail-closed gates for DYX, DZX, EMX, HZX, EUX, and ELX, review the DOX/Event 006 focus cleanup ordering, and decide whether the missing conditional-shell flags need a separately scoped asset package.
