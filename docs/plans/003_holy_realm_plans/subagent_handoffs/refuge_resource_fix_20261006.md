# Event003 Refuge Resource Correction - 2026-10-06

## Accepted scope

Parent authorized removal of five flat manpower grants because none had an associated population or mobilization source. This uses the user's G6 release-QA authority. The patch changes no resources other than those five recruit grants and adds the one-time guard to `THR_open_refuge_roads`, a one-way policy choice whose existing memory flag blocks the opposing `THR_close_refuge_roads` action.

## Quote and outcome comparison

The values below use the decision's existing native Black Friday quote. The 50% and 25% columns are payable payment ratios, not discount percentages; positive prices round up to whole Political Power. All five actions now add zero manpower at ordinary, 50%, and 25% quotes.

| Decision | PP payable: ordinary / 50% / 25% | Recruit grant removed | Retained effects |
|---|---:|---:|---|
| `THR_white_scarf_relief_caravans` | 55 / 28 / 14 | 45,000 | Repairs one eligible controlled state, sets resistance on non-core land, adds Stability and Spiritual Legitimacy, lowers Final Silence Pressure and Chaos, and records Ash Mercy under threat. |
| `THR_second_refuge_register` | 70 / 35 / 18 | 70,000 | Raises Spiritual Legitimacy and lowers Compassion Drift. The description no longer promises manpower. |
| `THR_open_refuge_roads` | 120 / 60 / 30 | 180,000 | Opens the refugee policy, costs a small amount of Stability, raises Spiritual Legitimacy and Compassion Drift, and lowers Chaos once. Its existing memory still blocks closing the roads afterward. |
| `THR_bodhisattva_hold_teachings_for_refugees` | 180 / 90 / 45 | 45,000 | Holds a teaching seat, adds Stability, advances Bhumi below its cap, raises Spiritual Legitimacy, lowers Compassion Drift, and records the Ash Mercy mission. |
| `THR_bodhisattva_invite_foreign_pilgrims` | 155 / 78 / 39 | 25,000 | Holds a teaching seat, adds Stability, raises Spiritual Legitimacy and Mandala Reach, and retains its existing completion memory. |

The five costs remain the existing table prices: PP55, PP70, `refuge_commitment_cost = 120`, `bodhisattva_refugee_teaching_cost = 180`, and `bodhisattva_pilgrim_cost = 155`. The Event003 anchors are at `common/script_constants/003_holy_realm_constants.txt:131,137,145`; the quote registrations for the two owner-constant prices are at `common/scripted_effects/026_black_friday_price_table_effects.txt:2439-2441,2523-2525`. The PP55 and PP70 anchors and quote registrations are in `common/script_constants/026_black_friday_constants.txt:157,160` and `common/scripted_effects/026_black_friday_price_table_effects.txt:1439-1450`. Shared payment ratios are 5000 and 2500 basis points (`common/script_constants/026_black_friday_constants.txt:18-20`); the price API documents whole-unit ceiling at `common/scripted_effects/026_black_friday_price_table_effects.md:18,27-28`.

No additional recruit source remains in these five decision effects or their existing teaching helper. The peacekeeping manpower payment/refund in `THR_stand_between_armies` is unchanged.

## One-way refuge decision

`THR_open_refuge_roads` now has `fire_only_once = yes`. It sets `holy_realm_memory_open_refuge_roads`, and the existing `THR_close_refuge_roads` availability requires that flag to be absent. Repeating the opening purchase after its timer completed previously let the one-way choice pay its other rewards repeatedly; the new field makes the decision disappear after its first selection. Its existing AI weight and all effects remain unchanged.

Offline Decision modding wiki `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:282` states that `fire_only_once = yes` makes a decision impossible to fire again after completion. Vanilla precedence is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/aat_mio_decisions.txt:4-12`, where a native priced decision sets `fire_only_once = yes`.

## Localization

Only `THR_second_refuge_register_desc` contained a manpower promise. It now describes the unchanged Spiritual Legitimacy and Compassion Drift effects. The relief, refuge-road, refugee-teaching, and foreign-pilgrim descriptions already describe retained effects and did not need a rewrite. No update-history language was added.

## Current source and probability handoff

The frozen baseline and live pre-patch decision file both have SHA-256 `95CB8C92154516359F5320FCAAC24F7F19D25BF00F60DC6FA64297A981707926`. The current decision file after this patch is SHA-256 `AAE8875AA894F9A865B067E3443B5FFD005E18561609C51A71529AFC60381703`. A source diff against `docs/plans/003_holy_realm_plans/source_snapshots/unfunded_manpower_20261006/003_holy_realm_decisions.txt.before` contains exactly the five removed `add_manpower` lines and the one added `fire_only_once = yes` line; the 47 parent-reviewed tab filters remain present.

The probability auditor completed the baseline inspection attempt before this patch; it returned `Transport closed`. Parent received the after hash for its requested same-scenario `probability_compare`. No probability or AI-weight result is claimed in this handoff.

No game or desktop session was launched, no shared source or spreadsheet was changed, and nothing was staged or committed.
