# Camp labor trade-off and legacy decision removal, 10 October 2026

Disposition: implemented in source.
Acceptance basis: the user's 10 October brief (Camps must still be fixed; every visible value must justify itself; remove bloated and repetitive content) and the coordinator's task for this pass.
No game was launched; live behavior, AI timing and save persistence remain user-validated.
Follows [gameplay gates, window redesign and decision trim](gameplay_gates_ui_decisions_2026-10-10.md), which listed the legacy decisions removed here as remaining bloat.

## 1. Labor audit

The forced-labor economy is `camp_admin_refresh_state_economy` (state output) and `camp_admin_refresh_country_economy` (national factory modifier), driven monthly by `camp_admin_monthly_state`.
A save from the 1936 start (`hoi4live_p4_exit`, 13 February 1936) confirmed the chain is wired: every initialized country carries `camp_admin_*` variables, the dispatch timer is armed, and the monthly pass for February 1936 had run.
Historical sites (Dachau area, Kolyma, Magadan) start dormant, so labor begins only once a site is registered and filled, as designed.

Defects and gaps found in the labor loop:

| Finding | Effect | Fix |
| --- | --- | --- |
| Labor mortality and output ignored the mandate. The coercive and radical tooltips promised that conditions and mortality shape output, but nothing did. | No trade-off: the radical mandate only unlocked killing, and forced labor was a flat gain. | Radical mandate on a labor or penal site now multiplies output and labor deaths (`camp_admin_labor.radical_output`, `radical_mortality`). |
| Famine never reached the workforce although camps already feed famine pressure through deaths and surface pressure. | Overcrowded camps in a starving state produced at full strength. | The host state's `famine_food_stage` scales assigned workers (`acute_shortage_workforce`, `famine_workforce`, `catastrophic_famine_workforce`). |
| The legacy site-profile index `camp_labor_output` came from the site type alone. | A suspended or custody-only site still counted a labor burden in the stability and supply ideas. | `camp_admin_scale_profile_labor_output` zeroes the index for an administered site without workers and applies the output factor otherwise. |
| The works priority produced nothing at the default maintenance ceiling, with no hint why. | Players saw 0 percent works output. | The priority tooltip now states that construction output needs a spending ceiling above maintenance. |
| The mandate tooltip described an effect that did not exist. | Misleading text. | Tooltips rewritten to the implemented behavior. |

Connections that already existed and were verified in source: each death receipt feeds the shared Deaths record, the responsible country's hidden atrocity score and Condemnation (scaled by people lost), and `famine_adapt_camp_state`; Famine adds extraction and vulnerability pressure for every state with an active camp.
No new window value was added.
Design and tuning: `docs/systems/camp_forced_labor.md`.

## 2. Legacy decision removal

Verified unreachable before deletion:

- 74 decisions and missions whose `visible` block required `NOT = { has_country_flag = camp_admin_initialized }` or `NOT = { has_country_flag = camp_admin_civil_initialized }`. The 1936 save shows `camp_admin_initialized` on all 99 countries present at the start and `camp_admin_civil_initialized` on ENG, FRA, BEL, ITA, USA, RAJ and COG. A country created later receives the flag at its first administration pass, and it can hold no active network before that.
- 13 missions started only by those decisions or by the retired colonial bridge.
- The four French and Belgian crisis choices (`fr_support_refugee_and_rescue_networks`, `fr_suppress_refugee_and_rescue_networks`, `bel_negotiate_colonial_strike_settlement`, `bel_suppress_colonial_strikes`) and their four missions: the only callers of `camp_rework_begin_france_refugee_response` and `camp_rework_begin_belgium_strike_response` sat inside `camp_rework_update_colonial_country_monthly_bridge`, whose whole body ran only for a country without `camp_admin_civil_initialized`.

- 12 further missions that no effect activates once those decisions are gone (`uk_postwar_raj_review`, `usa_court_review_period`, `ita_desert_camp_closure` and nine like them). A mission can start only through `activate_mission`, and a search of the mod finds no caller.

107 decisions and missions were removed in total.

Removed with them, each time after confirming no remaining reference by name:

- about 280 scripted effects and triggers (payload effects, mission outcomes, dispatcher branches, the retired colonial bridge and its call sites, the cancel-routine-project chains, the unused ledger action-slot display with its 24 scripted-localisation getters), found by an iterated orphan scan;
- 74 `camp_rework_action` identifiers and about 210 unreferenced tuning constants;
- about 320 localisation keys;
- 20 decision sprites and DDS files used only by the removed decisions;
- the Italian security-battalion modifier chain whose only producer was removed.

The monthly pulse, `camp_admin_*` window, civil authority actions, the live country kits and the generic activation, inspection, evidence and dismantlement decisions are unchanged.

## 3. Test scripts

The occupation and partner source suites now stage gameplay conditions: the campaign opens through the production pass (declared actor eligibility), German authority over a state starts its own clock, Hungary's window follows the domination flag, the extended partner windows follow campaign age, and Denmark's government falls on a staged day.
`foundation_source_tests.py` records the day a flag is set so timed flag triggers evaluate.
Suites for removed behavior were trimmed or deleted (the retired colonial dismantlement lifecycle in `foundation_source_tests.py`, the Italian security modifier suite).

## 4. Not done, with reason

- `current_institution_projection_source_tests_2026-10-03.py` records source hashes of files other work changed; its results file is left at its committed value.
- Legacy colonial idea lifecycle (`camp_rework_refresh_colonial_country_ideas`) and the `camp_policy_*` pressure bookkeeping still contain branches for the retired colonial kits. They are valid script that no live path reaches. Removing them touches the pressure model shared with the live kits and is left as a separate pass.
- Specs and older plans under `docs/specs/system_camp_repression_rework_specs` and `docs/plans/system_camp_repression_rework_plans` still describe the removed decisions as historical design; they are superseded for those decisions by this note.
- Nothing here was observed in game.
