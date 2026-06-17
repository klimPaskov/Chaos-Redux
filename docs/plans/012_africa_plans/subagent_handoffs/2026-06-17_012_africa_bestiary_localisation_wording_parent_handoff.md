# Event 012 Africa Bestiary Localisation Wording Cleanup

Date: `2026-06-17`

Owner: parent implementation pass

## Changed files

- `localisation/english/012_african_union_l_english.yml`

## Gameplay surface

Player-facing Bestiary localisation now keeps supernatural and nonhuman actor identities explicit without using implementation-facing labels such as `fictional` or meta phrasing about whether an actor is a normal human state.

## Keys changed

- `africa_gorilla_highlands_seat_desc`
- `africa_baobab_senate_seat_desc`
- `africa_tidemark_dominion_seat_desc`
- `africa_ananse_web_seat_desc`
- `africa_orisha_vodun_nature_courts_seat_desc`
- `africa_crocodile_rivers_seat_desc`
- `africa_chimpanzee_telegraph_league_seat_desc`
- `africa_okapi_court_seat_desc`
- `africa_termite_citadel_engineers_seat_desc`
- `africa_honeyguide_commons_seat_desc`
- `africa_great_herds_compact_seat_desc`
- `africa_high_chaos_actor_focus_tree_desc`
- `AFR_BEST_forest_covenant_desc`
- `AFR_BEST_mutual_defense_desc`
- `africa_open_honeyguide_route_commons_desc`
- `africa_staff_ghp_highland_sanctuary_guides_role_staff_desc`

## Before

Several visible strings described Bestiary actors as `fictional` or used out-of-world contrast text such as `pretending it is a normal human state`.

## After

The same strings describe the actors as nonhuman, supernatural, Bestiary-bound, or governed through liaison law and Charter limits.

## Validation

- `rg` in `localisation/english/012_african_union_l_english.yml` shows no remaining `fictional`, `normal state`, `human state`, `implementation`, or `generated` player-facing hits.
- Remaining `pretending` hits are in-world phrasing about the Charter not claiming immediate administrative control and false seats pretending at inheritance.
- The localisation file still has a UTF-8 BOM.

## Commit note

This patch is intentionally left for the broader Event 012 localisation commit because `012_african_union_l_english.yml` is currently a large uncommitted rewrite relative to `HEAD`; staging it only for these wording changes is not cleanly separable.
