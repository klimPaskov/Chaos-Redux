# Event 012 Africa Country Package Audit Handoff

Date: 2026-06-16

Subagent scope: country-package audit and narrow safe patching for Event 012 Africa regional authorities and high-chaos actors.

## Instructions and References Used

- Read and applied `AGENTS.md`.
- Read and applied repo skills:
	- `.agents/skills/chaos-redux-subagents/SKILL.md`
	- `.agents/skills/chaos-redux-events/SKILL.md`
	- `.agents/skills/hoi4-focus-trees/SKILL.md`
	- `.agents/skills/hoi4-decisions-missions/SKILL.md`
	- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- Consulted required offline wiki pages under `paradox_wiki/`, including data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, country creation, and national focus modding.
- Consulted vanilla HOI4 documentation and examples under `~/projects/Hearts of Iron IV/`, including country tags, country history, effects documentation for `create_country_leader`, `load_focus_tree`, `set_autonomy`, `set_capital`, `set_politics`, and vanilla African country history/state examples.
- Reviewed Event 012 source docs:
	- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
	- `docs/specs/012_africa_specs/matrices/012_africa_niche_polity_package_matrix.md`
	- `docs/specs/012_africa_specs/matrices/012_africa_expanded_subject_matrix.md`
	- `docs/specs/012_africa_specs/matrices/012_africa_ai_strategy_matrix.md`
	- `docs/specs/012_africa_specs/matrices/012_africa_asset_matrix.md`
	- `docs/events/012_africa_foundation.md`

## Country Package Coverage Checklist

- Present: all 16 Event 012 country tags are registered in `common/country_tags/chaosx_countries.txt`:
	- Regional authorities: `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`.
	- High-chaos actors: `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`.
- Present: all 16 country definition files exist under `common/countries/`.
- Present: all 16 country history files exist under `history/countries/` with matching tag prefixes.
- Present: all 16 tags have base, `DEF`, `ADJ`, and ideology-variant country names in `localisation/english/chaosx_countries_l_english.yml`.
- Fixed: all 16 tags now have party short and long localisation keys for `democratic`, `communism`, `fascism`, and `neutrality`.
- Present: regional/high-chaos setup effects assign focus trees through `load_focus_tree` in `common/scripted_effects/012_africa_effects.txt`.
- Present: all 16 tags are bound by the Event 012 subject setup effects when spawned.
- Present: six high-chaos spawned country tags are registered as `is_special_chaos_country` and `is_actual_nonhuman_country` in `common/scripted_triggers/chaosx_dynamic_triggers.txt`.
- Parent follow-up, 2026-06-17: the ten human regional authority country tags are also registered as `is_special_chaos_country`, and `chaosx_dynamic_triggers.md` documents both Event 012 high-chaos and regional authority coverage.
- Parent follow-up, 2026-06-17: the 21 created Event 012 tags received direct public display identities and matching history leader labels. The current display set is West Africa, Sahel, Maghreb Coast, Nile-Horn, East African Railways, Great Lakes, Congo Basin, Zambezi-Stone Cities, South African Liberation, Indian Ocean, Gorilla Highlands, Baobab Roots, Tidemark, Ananse Web, Orisha/Vodun Wilds, Crocodile Rivers, Chimpanzee Telegraph, Okapi Forest, Termite Citadels, Honeyguide Routes, and Great Herds.
- Parent follow-up, 2026-06-17: `africa_generate_created_country_role_staff` now gives all 21 created actors two generated advisors during setup. These are functional role/support staff advisors using vanilla advisor roles and traits, with localisation keys in `012_african_union_l_english.yml`. This narrows the advisor-surface gap but does not replace full bespoke minister rosters or named commander pools.

## File Surface Checklist

- Audited: `common/country_tags/chaosx_countries.txt`, lines 52-68.
- Audited: `common/countries/cosmetic.txt`; no direct Event 012 cosmetic-tag blocker found in the scoped pass.
- Audited: `common/countries/West African Congress.txt`
- Audited: `common/countries/Sahel Caravan.txt`
- Audited: `common/countries/Maghreb Coast.txt`
- Audited: `common/countries/Nile-Horn League.txt`
- Audited: `common/countries/East African Railway Congress.txt`
- Audited: `common/countries/Great Lakes Council.txt`
- Audited: `common/countries/Congo Basin Charter.txt`
- Audited: `common/countries/Zambezi-Stone Cities.txt`
- Audited: `common/countries/South African Liberation Congress.txt`
- Audited: `common/countries/Indian Ocean Congress.txt`
- Audited: `common/countries/Gorilla Highlands.txt`
- Audited: `common/countries/Baobab Senate.txt`
- Audited: `common/countries/Tidemark Dominion.txt`
- Audited: `common/countries/Ananse Web.txt`
- Audited: `common/countries/Orisha Vodun Nature Courts.txt`
- Audited: `common/countries/Crocodile Rivers.txt`
- Audited: all scoped `history/countries/{WAC,SAH,MAG,NHR,EAC,GLK,CBC,ZSC,SLC,IOC,GHP,BBS,TDM,ANW,OVN,CRR}*.txt` files.
- Audited and patched narrowly: `localisation/english/chaosx_countries_l_english.yml`.
- Audited and patched narrowly: `history/countries/GHP - Gorilla Highlands.txt`.
- Audited: `common/scripted_effects/012_africa_effects.txt` for tag, focus-loading, subject, and seat-state setup.
- Audited: `common/ai_strategy/012_africa.txt`.
- Cross-checked: `common/national_focus/012_africa_authority_focus.txt`.
- Cross-checked: `common/ideas/012_africa_ideas.txt`.
- Cross-checked: `interface/012_africa.gfx`.
- Cross-checked: `common/scripted_triggers/chaosx_dynamic_triggers.txt` and `.md` for nonhuman/special-country safety, but did not patch because it is outside the allowed country-package file list.

## Missing or Stale Country Package Surfaces

- `common/scripted_triggers/chaosx_dynamic_triggers.txt`: parent follow-up supersedes the earlier risk. `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, and `CRR` are covered by both `is_special_chaos_country` and `is_actual_nonhuman_country`; `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, and `IOC` are covered by `is_special_chaos_country` only, which is the correct split for human regional authorities.
- `common/scripted_effects/012_africa_effects.txt`: high-chaos package catalog content includes more high-chaos concepts than the six country tags in this audit. Only `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, and `CRR` have scoped country-package surfaces.
	- Parent follow-up, 2026-06-16: all 11 package IDs now have unlock outcomes and visible value movement, so the extra package IDs are no longer pure catalog-only entries. They still are not map country packages, and only the six listed tags have country-package surfaces.
	- Not patched: creating new country packages is outside this subagent scope.

## Map and State Setup Issues

- Confirmed seat-state constants in `common/scripted_effects/012_africa_effects.txt`, lines 19-34:
	- `@africa_wac_seat_state = 558`
	- `@africa_sah_seat_state = 556`
	- `@africa_mag_seat_state = 459`
	- `@africa_nhr_seat_state = 271`
	- `@africa_eac_seat_state = 546`
	- `@africa_glk_seat_state = 548`
	- `@africa_cbc_seat_state = 295`
	- `@africa_zsc_seat_state = 771`
	- `@africa_slc_seat_state = 275`
	- `@africa_ioc_seat_state = 543`
	- `@africa_ghp_seat_state = 768`
	- `@africa_bbs_seat_state = 778`
	- `@africa_tdm_seat_state = 905`
	- `@africa_anw_seat_state = 779`
	- `@africa_ovn_seat_state = 773`
	- `@africa_crr_seat_state = 772`
- Confirmed regional authority spawn transfer checks in `common/scripted_effects/012_africa_effects.txt`, lines 466-511, require ROOT to own and control each seat state.
- Confirmed high-chaos spawn transfer checks in `common/scripted_effects/012_africa_effects.txt`, lines 526-566, use `africa_can_transfer_seat_state_to_high_chaos`.
- Parent follow-up, 2026-06-17: the shared high-chaos/regional seat risk is resolved by giving the overlapping high-chaos actors distinct vanilla African states and matching history capitals: `GHP` uses Rwanda `768`, `BBS` uses Upper Volta `778`, `TDM` uses Mombasa `905`, and `ANW` uses Ivory Coast `779`. The current seat-constant set has no duplicate state IDs across the 16 Event 012 created tags.
- No Event 012 state override files were found for the seat states. Vanilla state ownership, controller setup, buildings, resources, supply, and victory points therefore apply until Event 012 scripted transfer logic runs.

## Politics, Leaders, Portraits, Flags, Advisors, and Parties

- Fixed: `GHP` nonhuman leader portrait.
	- Before: `history/countries/GHP - Gorilla Highlands.txt` used `GFX_portrait_generic_africa_male_01`.
	- After: `history/countries/GHP - Gorilla Highlands.txt` uses `GFX_portrait_independence_wave_gorilla_chair`.
	- The replacement portrait is already registered in `interface/chaosx_characters.gfx` and documented in `docs/assets/006_independence_wave/leader_portraits/manifest.md` as generated/fictional.
- Fixed: party localisation for all 16 scoped tags in `localisation/english/chaosx_countries_l_english.yml`, lines 380-507.
	- Added `TAG_democratic_party`, `TAG_democratic_party_long`, `TAG_communism_party`, `TAG_communism_party_long`, `TAG_fascism_party`, `TAG_fascism_party_long`, `TAG_neutrality_party`, and `TAG_neutrality_party_long` for every scoped Event 012 tag.
- Confirmed: history files use institutional leader names rather than mismatched personal random-name pools. This is appropriate for councils, congresses, courts, webs, rivers, and other symbolic/nonhuman bodies.
- Superseded parent note, 2026-06-16: `BBS`, `TDM`, `ANW`, `OVN`, and `CRR` no longer use generic human portrait assets; generated nonhuman/supernatural portraits are registered in `interface/012_africa.gfx` and referenced by the matching history files.
	- This is not an immediate syntax blocker because institutional leader names avoid personal gender/name mismatch.
	- It is still a country-package asset gap because the visual presentation is not clearly supernatural/nonhuman.
- Superseded parent note, 2026-06-16: generated symbolic root/medium/small flag families now exist for all 16 Event 012 created tags:
	- Found root flag files under `gfx/flags/` for each tag and ideology variant.
	- Found medium flag files under `gfx/flags/medium/`.
	- Found small flag files under `gfx/flags/small/`.
	- `docs/assets/012_africa/generated_flags/manifest.md` is the current flag-family source of truth for these created tags.
- No dedicated advisor or commander packages were found in the scoped country history files. This is acceptable for a minimal package, but leaves the tags shallow if they become playable subjects.

## Focus, Decision, Idea, and Asset Issues

- Confirmed: `africa_setup_regional_authority_subject` in `common/scripted_effects/012_africa_effects.txt`, lines 308-321, loads `africa_regional_authority_focus_tree`.
- Confirmed: `africa_setup_high_chaos_actor` in `common/scripted_effects/012_africa_effects.txt`, lines 335-348, loads `africa_high_chaos_actor_focus_tree`.
- Confirmed: `common/national_focus/012_africa_authority_focus.txt` defines both trees:
	- `africa_regional_authority_focus_tree`
	- `africa_high_chaos_actor_focus_tree`
- Confirmed: focus allowed checks key on `africa_regional_authority_subject` and `africa_high_chaos_actor`, matching the scripted setup flags.
- Confirmed: `common/ideas/012_africa_ideas.txt` defines:
	- `africa_regional_authority_spirit`
	- `africa_high_chaos_actor_spirit`
- Confirmed: `interface/012_africa.gfx` defines matching idea sprites:
	- `GFX_idea_africa_regional_authority`
	- `GFX_idea_africa_high_chaos_actor`
- Parent follow-up, 2026-06-17: the shared focus-tree finding is partially superseded. `common/national_focus/012_africa_authority_focus.txt` now includes role-gated branches for West/Sahel mobility (`WAC`, `SAH`), coast-and-rail links (`MAG`, `EAC`, `IOC`), interior guard posts (`NHR`, `GLK`, `CBC`), southern workshops (`ZSC`, `SLC`), forest/covenant Bestiary seats (`GHP`, `BBS`, `OVN`), river/tide Bestiary seats (`CRR`, `TDM`), and Ananse signal lines (`ANW`). These branches feed the shared future/witness focuses and move Event 012 values through the overlord where applicable. Remaining issue: this is still role-family coverage, not fully bespoke per-tag focus trees.
- Remaining issue: this pass did not audit Event 012 decisions deeply beyond country-package linkage. Decision-specific balance and mission behavior belongs to a decision/missions audit pass.

## Starting Military, Technology, Industry, Supply, and Production Issues

- Confirmed: history files give minimal techs and research slots but no OOB, navy, air force, convoy setup, train setup, or country-specific industry setup.
- Confirmed: `common/scripted_effects/012_africa_effects.txt` provides dynamic setup for regional/high-chaos subjects, including starting spirit, equipment, and guard divisions.
- Remaining issue: maritime or logistics-themed actors such as `IOC`, `TDM`, `EAC`, and `CRR` do not have tag-specific navy, convoy, rail, train, or supply differentiation in the scoped country-package files.

Parent follow-up, 2026-06-17: the starting-logistics finding is partially superseded by the shared setup helper and static OOB patch. `africa_apply_created_country_setup_package` now gives every created Event 012 actor a tag-specific role flag, visible role spirit, role-matched equipment/manpower/command-power or building support, and Event 012 value movement on the Charter leader. `africa_apply_created_country_production_package` now also adds one-time production-line setup: all 21 created Event 012 actors receive a support-equipment line, combat-oriented roles receive an infantry-equipment line, maritime route actors receive a convoy line, mobility actors receive motorized production, and rail/survey actors receive train production. Static land OOB files and `set_oob` references now exist for all 21 created tags. Small DLC-split static naval OOBs now cover `MAG`, `EAC`, `IOC`, `TDM`, `CRR`, `WAC`, `CBC`, `ANW`, and `OVN`; small DLC-split static air OOBs cover `MAG`, `IOC`, `OVN`, `NHR`, and `SLC`. Each created actor now receives two generated role/support advisors. Remaining issues are deeper country-package surfaces: full bespoke focus/decision identities, full minister or commander rosters, and country-specific naval or air branches beyond small patrol/liaison setup.

## AI and Playability Issues

- Confirmed: `common/ai_strategy/012_africa.txt` includes broad AI strategies for:
	- `africa_unifier_active`
	- `africa_regional_authority_subject`
	- `africa_high_chaos_actor`
- Confirmed: AI strategy enable checks align with the same flags set by `common/scripted_effects/012_africa_effects.txt`.
- Remaining issue: no per-tag AI strategy differentiation was found for the 16 country packages.
	- `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, and `IOC` share one generic regional-subject posture.
	- `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, and `CRR` share one generic high-chaos survival posture.
- Remaining issue: high-chaos tags can survive at a basic level through shared equipment/guards, but do not have role-specific playability hooks or route-specific AI behavior.

Parent follow-up, 2026-06-17: the generic AI finding is partially superseded. `common/ai_strategy/012_africa.txt` now has role-specific strategy bands plus one tag-specific AI posture for each of the 21 created Event 012 actors. Remaining AI/package gaps are route-specific decision AI, full bespoke focus trees, deeper naval/air behavior beyond small static OOBs, full minister or commander rosters, and richer tag-specific logistics rather than a single identical AI posture for every created actor.

## Patch Summary

Changed files:

- `history/countries/GHP - Gorilla Highlands.txt`
- `localisation/english/chaosx_countries_l_english.yml`

Changed identifiers:

- Country/leader display identities:
	- `WAC`: West Africa
	- `SAH`: Sahel
	- `MAG`: Maghreb Coast
	- `NHR`: Nile-Horn
	- `EAC`: East African Railways
	- `GLK`: Great Lakes
	- `CBC`: Congo Basin
	- `ZSC`: Zambezi-Stone Cities
	- `SLC`: South African Liberation
	- `IOC`: Indian Ocean
	- `GHP`: Gorilla Highlands
	- `BBS`: Baobab Roots
	- `TDM`: Tidemark
	- `ANW`: Ananse Web
	- `OVN`: Orisha/Vodun Wilds
	- `CRR`: Crocodile Rivers
	- `CTL`: Chimpanzee Telegraph
	- `OKP`: Okapi Forest
	- `TRM`: Termite Citadels
	- `HGD`: Honeyguide Routes
	- `GHC`: Great Herds
- Leader portrait:
	- `GHP` still uses `picture = GFX_portrait_independence_wave_gorilla_chair`
- Generated role-advisor tokens:
	- `africa_staff_wac_port_union_organizers_role_staff`
	- `africa_staff_sah_oasis_route_quartermasters_role_staff`
	- `africa_staff_mag_port_pilots_role_staff`
	- `africa_staff_nhr_nile_horn_surveyors_role_staff`
	- `africa_staff_eac_railway_supply_engineers_role_staff`
	- `africa_staff_glk_lake_muster_staff_role_staff`
	- `africa_staff_cbc_river_forest_quartermasters_role_staff`
	- `africa_staff_zsc_stone_city_builders_role_staff`
	- `africa_staff_slc_mine_port_strike_staff_role_staff`
	- `africa_staff_ioc_monsoon_convoy_pilots_role_staff`
	- `africa_staff_ghp_highland_sanctuary_guides_role_staff`
	- `africa_staff_bbs_baobab_memory_speakers_role_staff`
	- `africa_staff_tdm_tidemark_harbor_voices_role_staff`
	- `africa_staff_anw_ananse_signal_weavers_role_staff`
	- `africa_staff_ovn_omen_keepers_role_staff`
	- `africa_staff_crr_river_marshals_role_staff`
	- `africa_staff_ctl_telegraph_operators_role_staff`
	- `africa_staff_okp_shadow_couriers_role_staff`
	- `africa_staff_trm_citadel_builders_role_staff`
	- `africa_staff_hgd_route_finders_role_staff`
	- `africa_staff_ghc_pathbreakers_role_staff`
- Localisation keys:
	- Added 128 party localisation keys for `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`, `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, and `CRR`.
- No state ids changed.
- No country tags changed.
- No focus tree ids changed.
- No formable ids changed.
- No AI strategies changed.

Before behavior:

- `GHP` displayed a generic human male portrait despite being a nonhuman high-chaos actor.
- The 16 Event 012 tags had country names and ideology variants but no party localisation, causing raw or missing party-key display risk.

After behavior:

- `GHP` displays an existing fictional/generated gorilla council portrait.
- All 16 Event 012 tags have party short and long names for each vanilla ideology.

## Validation

- Confirmed all 16 scoped tags are registered in `common/country_tags/chaosx_countries.txt`, lines 53-68.
- Confirmed all 16 scoped country definition and history files exist.
- Confirmed `GFX_portrait_independence_wave_gorilla_chair` is registered in `interface/chaosx_characters.gfx`, used by `history/countries/GHP - Gorilla Highlands.txt`, and documented in `docs/assets/006_independence_wave/leader_portraits/manifest.md`.
- Confirmed every scoped Event 012 tag now has exactly eight party keys in `localisation/english/chaosx_countries_l_english.yml`.
- Confirmed `localisation/english/chaosx_countries_l_english.yml` still has UTF-8 BOM bytes `efbbbf`.
- Confirmed root flag files exist for all 16 scoped tags and ideology variants, and confirmed missing medium/small variants.
- Confirmed focus tree loading paths:
	- `common/scripted_effects/012_africa_effects.txt` loads `africa_regional_authority_focus_tree` for regional subjects.
	- `common/scripted_effects/012_africa_effects.txt` loads `africa_high_chaos_actor_focus_tree` for high-chaos actors.
	- `common/national_focus/012_africa_authority_focus.txt` defines both focus tree ids and gates them on the expected flags.

Skipped validation:

- No full game launch or in-game validation was performed from this subagent pass.
- No broad scripted syntax/parser pass was run across Event 012 because the working tree contains many unrelated parent/user edits, including Event 013/Natural Disaster work that this audit was instructed to ignore.

## Remaining Setup or Identity Risks

- Parent follow-up, 2026-06-16: the missing root/medium/small flag-family issue was resolved by generating complete symbolic flag families for all 16 Event 012 created tags under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`; see `docs/assets/012_africa/generated_flags/manifest.md`.
- Parent follow-up, 2026-06-16: the generic portrait issue for `BBS`, `TDM`, `ANW`, `OVN`, and `CRR` was resolved with generated nonhuman/supernatural portraits registered in `interface/012_africa.gfx` and referenced by the matching history files; see `docs/assets/012_africa/high_chaos_identity/manifest.md`.
- Parent follow-up, 2026-06-17: regional authority tags are included in `is_special_chaos_country`; this specific shared-trigger risk is resolved.
- Parent follow-up, 2026-06-17: shared regional/high-chaos seat states are resolved; `GHP`, `BBS`, `TDM`, and `ANW` no longer share their one-state capitals with `CBC`, `SAH`, `IOC`, or `WAC`.
- Parent follow-up, 2026-06-17: created-country setup now includes a bounded one-time role package in `africa_apply_created_country_setup_package` for all 21 created actors. Every regional authority and explicit Bestiary actor receives a role flag, a visible role spirit, role-matched equipment/manpower/command-power or building support, and Event 012 value movement on the Charter leader. `africa_apply_created_country_production_package` also adds one-time support, combat, and maritime production-line setup by role family.
- Shared regional and high-chaos focus trees are load-safe and now include role-family branches, but they are not fully bespoke per country package.
- Shared AI strategies are load-safe and role-family differentiated, but not fully bespoke per country package.
- Starting setup is enough for spawned subject survival and now has role-level logistics, production-line differentiation, static land OOBs for all 21 created actors, small static navy/air OOBs where seat infrastructure supports them, and two generated advisors per created actor. It still lacks full bespoke focus trees, route-specific industry depth, full minister or commander rosters, and deeper country-specific naval or air behavior beyond patrol/liaison starts.

## Plan Handoff Path

This handoff is the plan/audit artifact:

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_012_africa_country_package_audit_handoff.md`
