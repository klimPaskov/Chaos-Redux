# Event 012 Africa Foundation API

This document describes the reusable Event 012 scripted API added for the first foundation pass. It is intentionally limited to constants, triggers, scripted effects, and handoff documentation. It does not wire events, decisions, focus trees, localisation, countries, assets, UI, or dispatcher/log files.

## Files

- `common/script_constants/012_africa_constants.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_effects/012_africa_effects.txt`

## Runtime Context

`africa_select_random_unifier_candidate` selects a random country that passes `is_africa_valid_unifier_candidate`. The trigger requires an existing country with capital in Africa, at least one owned or controlled African state, and excludes special chaos countries, actual nonhuman countries, capitulated countries, existing Africa formables, world-end actors, and flagged broken shells. Subject countries qualify only through the explicit subject allowance flag or an active liberation-war story.

`africa_prepare_runtime_context_from_this` runs in the selected country scope. It saves the global event target `africa_unifier_country`, sets the durable owner variables `global.africa_unifier_country` and `global.africa_unifier_country_id`, sets `global.africa_runtime_ready`, `africa_runtime_context_ready`, `event_012_africa_fired`, and the country flag `africa_unifier_active`, then initializes all core values.

`africa_clear_runtime_context` clears the global event targets, country flags, and runtime variables owned by this foundation API, including the unifier, Charter League leader, RSA branch targets, RSA branch state, and World Is One gate state.

## Core Values

`africa_initialize_core_values` initializes all mapped values from the specs:

- `africa_legitimacy`
- `africa_authority`
- `africa_league_cohesion`
- `africa_liberation_momentum`
- `africa_regional_trust`
- `africa_colonial_alarm`
- `africa_paper_core_burden`
- `africa_covenant_pressure`
- `africa_archive_mandate`
- `africa_old_seat_legitimacy`
- `africa_local_sovereignty`
- `africa_restoration_debt`
- `africa_mythic_pressure`
- `africa_nonhuman_sovereignty`
- `africa_bestiary_alarm`
- `africa_habitat_trust`
- `africa_mythic_volatility`

Initial values and clamp bounds live in `africa_initial_value` and `africa_value_bounds`.

## Paper-Core Staging

The foundation API deliberately avoids instant full cores across Africa.

- `africa_grant_continental_paper_claims`: adds claims on African states and marks them with `africa_paper_claim`.
- `africa_unlock_state_integration_from_from`: country scope, with `FROM` as the target state. Marks a claimed African state as integration-unlocked.
- `africa_mark_state_authority_tracked_from_from`: country scope, with `FROM` as the target state. Marks a state as tracked by a regional authority or integration office.
- `africa_complete_living_core_from_from`: country scope, with `FROM` as the target state. Adds a real core only after the state is owned and controlled by the caller and has been integration-unlocked.

## Charter League

`africa_create_charter_league_from_template` creates the Pan-African Charter League through `create_faction_from_template` using `faction_template_africa_charter_league`, `africa_charter_league`, and `GFX_faction_logo_generic_democratic`.

The faction template is not created in this foundation patch. The parent must add the faction template before calling this helper in live script.

Membership helpers:

- `africa_add_from_to_charter_league`
- `africa_mark_from_as_protected_charter_member`
- `africa_mark_from_as_full_charter_member`

These helpers expect the unifier in `ROOT` and the target African country in `FROM`.

## RSA Branch

RSA-in-Allies state is tracked by:

- `africa_mark_rsa_allies_branch_start`
- `africa_mark_rsa_continental_side`
- `africa_mark_rsa_loyalist_side`
- `africa_mark_rsa_continental_victory`
- `africa_white_peace_allies_after_rsa_continental_victory`

The peace helper does not wire any on-action. It expects the parent to call it after the continental side wins. It white-peaces countries in England's faction that are still at war with `event_target:africa_rsa_continental_side`.

## Authority Atlas

`africa_register_authority_atlas_catalog` seeds global arrays with 32 historical dossier IDs and 11 high-chaos package IDs. Required minimum counts are constants:

- `africa_authority_atlas.minimum_historical_dossiers = 24`
- `africa_authority_atlas.minimum_high_chaos_packages = 6`

Registered count constants are also provided:

- `africa_authority_atlas.historical_dossier_count = 32`
- `africa_authority_atlas.high_chaos_package_count = 11`

Historical dossier IDs include Kush/Meroe, Aksum, Punic Harbor Ledger, Numidia, Garamantes, Manden, Songhai, Jolof-Wolof, Futa, Asante, Oyo, Benin/Edo, Dahomey, Kanem-Bornu, Hausa, Wadai-Baguirmi, Funj/Sennar, Adal/Harar, Ajuran, Swahili Coast, Kilwa, Kongo, Ndongo-Matamba, Luba, Lunda, Buganda, Bunyoro, Great Zimbabwe, Barotse, Merina, Comorian Sultanates, and Zulu-Nguni.

High-chaos package IDs include Gorilla Highlands, Chimpanzee Marshes, Okapi Court, Crocodile Rivers, Baobab Senate, Termite Surveyors, Honeyguide Commons, Great Herds, Tidemark Dominion, Ananse Ledger, and Orisha/Vodun/Nature Courts.

`africa_mark_selected_dossier_opened` expects `africa_selected_dossier_id` to be set on the current country. `africa_mark_selected_high_chaos_package_unlocked` expects `africa_selected_high_chaos_package_id`.

## Evolution Logging

The evolution helpers follow the existing `record_events_log_evolution_entry` pattern:

- `africa_record_evolution_i_if_needed`
- `africa_record_evolution_ii_if_needed`
- `africa_record_evolution_iii_if_needed`
- `africa_record_evolution_iv_if_needed`
- `africa_mark_world_is_one_gate_ready`

Each helper sets `events_log_evolution_event_id`, `events_log_evolution_type`, `events_log_evolution_stage`, `events_log_evolution_tier`, and actor context from `event_target:africa_unifier_country`, then checks `is_current_evolution_enabled = yes` before recording. Disabled evolutions do not set the recorded flags or unifier unlock flags.

## Known Integration Requirements

- Add `faction_template_africa_charter_league` before using the Charter League creation helper in live event/focus/decision code.
- Wire Event 012 event-log name/detail localisation and evolution display localisation in the parent implementation.
- Add country tags, focus tree, decision categories, UI, GFX, localisation, and nonhuman shared classifications in later scoped patches.
- Hook RSA victory peace logic from an explicit event or civil-war-end handler owned by the parent.
