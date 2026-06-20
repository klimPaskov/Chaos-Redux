# Event 012 Country Package Lifecycle Audit Handoff

## Scope

Bounded audit of Event 012 created and transformed actors around `africa_apply_created_country_setup_package`, regional authority/high-chaos setup helpers, Charter member exit/resistance decisions, companion focus trees, role ideas, and visible documentation.

## Files Changed

- `common/decisions/012_africa_decisions.txt`
- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_country_package_lifecycle_audit_handoff.md`

## Changed Identifiers

- Decisions:
  - `africa_member_petition_to_leave_charter`
  - `africa_member_prepare_resistance_war`
- Helper reference removed from those decisions:
  - `africa_remove_created_country_role_spirits`
- Preserved role idea family:
  - `africa_west_african_congress_seat`
  - `africa_sahel_caravan_seat`
  - `africa_maghreb_coast_seat`
  - `africa_nile_horn_league_seat`
  - `africa_east_african_railway_seat`
  - `africa_great_lakes_council_seat`
  - `africa_congo_basin_charter_seat`
  - `africa_zambezi_stone_cities_seat`
  - `africa_south_african_liberation_congress_seat`
  - `africa_indian_ocean_congress_seat`
  - `africa_gorilla_highlands_seat`
  - `africa_baobab_senate_seat`
  - `africa_tidemark_dominion_seat`
  - `africa_ananse_web_seat`
  - `africa_orisha_vodun_nature_courts_seat`
  - `africa_crocodile_rivers_seat`
  - `africa_chimpanzee_telegraph_league_seat`
  - `africa_okapi_court_seat`
  - `africa_termite_citadel_engineers_seat`
  - `africa_honeyguide_commons_seat`
  - `africa_great_herds_compact_seat`
  - `africa_bonobo_kinship_congress_seat`
  - `africa_hyena_radio_dominion_seat`
  - `africa_bird_of_the_walls_seat`
  - `africa_sao_terracotta_host_seat`

## Findings

### Country Package Coverage Checklist

- Tag registration: covered for the ten regional authorities and fifteen high-chaos actors in `common/country_tags/chaosx_countries.txt`.
- History/OOB surface: covered by matching `history/countries/<TAG> - ...txt` files that load land OOBs, with naval/air OOB variants where relevant.
- Setup package: covered by `africa_apply_created_country_setup_package`, which applies one-time role flags, visible role spirits, production lines, role stockpiles, staff, command staff, and capital infrastructure/port/industry where relevant.
- Created-role classification: covered by `africa_role_*` flags and `africa_regional_authority_subject` / `africa_high_chaos_actor`.
- Focus loading: covered by `africa_setup_regional_authority_subject` and `africa_setup_high_chaos_actor`, which load `africa_regional_authority_focus_tree` or `africa_high_chaos_actor_focus_tree` after setup.
- Decision consequences: mostly covered by Charter aid, leave, resistance, integration docket, mandate, and ten post-mandate package decisions.

### File Surface Checklist

- `common/scripted_effects/012_africa_effects.txt`: audited setup package, staff generation, guard divisions, production package, mandate success/failure, release/transfer helpers, and setup loaders.
- `common/scripted_triggers/012_africa_triggers.txt`: audited Charter candidate exclusions, regional authority mandate eligibility, regional package eligibility, and Charter actor control checks.
- `common/decisions/012_africa_decisions.txt`: patched Charter leave/resistance lifecycle and audited regional authority mandate/package decision gates.
- `common/national_focus/012_africa_authority_focus.txt`: audited shared regional authority and high-chaos companion tree identity branches and tag capstones.
- `common/ideas/012_africa_ideas.txt`: audited umbrella spirits and role-specific seat spirits.
- `localisation/english/012_african_union_l_english.yml`: audited existing visible keys; no change needed.
- `docs/events/012_africa_foundation.md`: updated lifecycle description.

### Missing Or Stale Country Package Surfaces

- No missing tag/history/OOB/focus/idea surface found in this bounded pass.
- Parent follow-up closed the membership-state residual after this audit: `africa_charter_league.former_member` now exists and Charter leave records that state while resistance remains separate.

### Map And State Setup Issues

- No new map ownership/controller issue found in the audited helper path. Regional and high-chaos spawns transfer one seat state after adding a core and bind the created country afterward.
- The setup package adds capital infrastructure and role-specific ports/factories/dockyards; no broad state setup patch made.

### Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- Role staff and command staff are generated with institutional names, which matches the council/body-style actor rule and avoids opposite-gender personal-name defects.
- Nonhuman/supernatural actors remain explicitly nonhuman through `africa_high_chaos_actor`, `africa_high_chaos_nonhuman`, and role localisation.
- No party, flag, or portrait patch made.

### Focus, Decision, Idea, And Asset Issues

- Finding fixed: Charter leave/resistance removed `africa_remove_created_country_role_spirits`, stripping the visible role identity from created actors while leaving hidden role flags and setup staff behind.
- After the patch, leave/resistance still remove Charter umbrella spirits (`africa_regional_authority_spirit`, `africa_high_chaos_actor_spirit`) but preserve the named role seat spirit.
- Companion trees already contain role-gated branches and tag-specific capstones; no broad focus-tree layout patch made.
- No asset changes made.

### Starting Military, Technology, Industry, Supply, And Production Issues

- Created countries receive OOBs from history, one-time guard divisions from setup, role stockpiles, and production-line packages.
- Role-specific production categories exist for infantry/support, convoys, motorized, and trains.
- No starting force or technology patch made.

### AI And Playability Issues

- Decisions have AI weights for mandate and package actions.
- Documentation records `common/ai_strategy/012_africa.txt` role/tag AI coverage for the created actors; this file was read only as evidence and not edited.
- Residual risk: shared companion trees remain shared trees, not fully bespoke country trees. The role branches, tag capstones, setup package, and AI mitigate sameness inside the current bounded scope.

## Before And After Behavior

Before:

- `africa_member_petition_to_leave_charter` and `africa_member_prepare_resistance_war` removed Charter membership flags and also called `africa_remove_created_country_role_spirits`.
- A created actor that left or resisted stopped showing its WAC/SAH/GHP/etc. seat spirit even though its role flags, generated staff, OOB, focus tree, and tag identity remained.

After:

- The same decisions still end subject/faction bindings, remove Charter umbrella spirits, set former/resistant state, remove the actor from Charter arrays, and apply the existing political/war consequences.
- The actor keeps its named role seat spirit, preserving visible country-package identity after exit or resistance.

## Validation

- Targeted `rg` checks confirmed the only remaining `africa_remove_created_country_role_spirits` references are the helper definition and no decision call sites.
- Targeted `rg` checks confirmed the two patched decisions still remove `africa_regional_authority_spirit` and `africa_high_chaos_actor_spirit`.
- `git diff --check` passed on touched files.

## Remaining Risks

- Membership-state overload was closed by parent follow-up: peaceful exit now uses a distinct former-member constant rather than overloading `resistant_member`.
- Existing tags and shared trees should still receive a later full country-package completion audit before Event 012 is claimed complete.
