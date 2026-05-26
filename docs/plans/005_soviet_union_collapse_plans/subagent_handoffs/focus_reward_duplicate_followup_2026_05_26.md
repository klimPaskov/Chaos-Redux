# Event 005 Focus Reward Duplicate Follow-Up

Date: 2026-05-26

Scope: read-only audit of remaining near-duplicate focus completion rewards in `common/national_focus/005_soviet_collapse_*.txt`, after the cleanup entries already recorded in `docs/events/005_soviet_collapse_focus_tree_audit.md`. No gameplay, localisation, GFX, or asset files were edited.

## Method

- Parsed 1,696 Event 005 focus blocks across the four Event 005 focus files.
- Exact `completion_reward` duplicates: 0.
- Remaining findings are normalized clusters where the visible focus reward still reduces to the same helper-only or small flat reward pattern.
- The earlier `focus_duplicate_effect_next_issue_2026_05_26.md` logistics packet appears to have been addressed by later audit entries, so this pass ignored that already-documented cluster.

## Route Coverage Table

| Required route surface | Implemented focus branch | Status | Notes |
| --- | --- | --- | --- |
| Custom splinter route identity | `005_soviet_collapse_custom_splinters.txt` generic identity lanes | Implemented but repetitive | Many tags have unique names/icons, but the focus reward signature remains `set flag + generic hidden helper`. |
| Ancient restoration diplomacy/charter routes | `005_soviet_collapse_ancient_restorations.txt` | Implemented but shallow in two clusters | League bargains were already split; the earlier letter/envoy focuses and later charter focuses still share near-identical reward shapes. |
| Shared republic opening routes | `005_soviet_collapse_republics.txt` | Implemented but generic | Legal, foreign, and military bootstrap focuses still lean on one shared helper each. |
| Shared republic route-fork focuses | `005_soviet_collapse_republics.txt` | Implemented but flat | Several important “which road?” fork focuses only set a route-open flag and grant small political power. |

## Top Remaining Clusters

| Priority | Cluster | Focus ids | Current reward signature | Suggested replacement direction |
| ---: | --- | --- | --- | --- |
| 1 | Custom splinter early identity lanes | Pattern: `<TAG>_first_guard`, `<TAG>_legitimacy`, `<TAG>_rival`, `<TAG>_doctrine`, `<TAG>_special_arm`, `<TAG>_enemy_front`, `<TAG>_civil_rule`, `<TAG>_propaganda`, `<TAG>_settlement`, `<TAG>_extreme_gate` for `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`. Example lines: `FTH_first_guard` at `005_soviet_collapse_custom_splinters.txt:51`, `BSC_first_guard` at `:3806`, `NLC_first_guard` at `:22916`. | `set_country_flag = <tag>_focus_*`; `custom_effect_tooltip = soviet_collapse_custom_splinter_route_identity_reward_tt`; hidden `soviet_collapse_apply_custom_splinter_*_identity = yes`. The helper has tag-conditional effects, but the focus file still reads as the same reward lane repeated 19 times. | Keep the shared helper structure, but give the highest-visibility early lanes tag-family payoff text and one visible local hook. Rail tags should point to rail/depot decisions, coastal tags to convoy/port defense, security tags to archive or command control, rural tags to food/manpower resilience, and factory tags to arsenal output. Start with `first_guard`, `legitimacy`, `rival`, and `doctrine`; these establish route feel early. |
| 2 | Custom splinter diplomacy identity lanes | Pattern: `<TAG>_league` and `<TAG>_foreign` for the same 19 custom splinter tags. Example lines: `FTH_league` at `005_soviet_collapse_custom_splinters.txt:189`, `FTH_foreign` at `:212`, `NLC_league` at `:23046`, `NLC_foreign` at `:23069`. | `set_country_flag = <tag>_focus_league/foreign`; same route identity tooltip; hidden `soviet_collapse_apply_custom_splinter_league_identity = yes` or `soviet_collapse_apply_custom_splinter_foreign_identity = yes`. | Split the diplomatic payoff by what the tag actually offers: ports and convoys for `KRS`/`FEV`/`ARD`/`NLC`, corridor mediation for `SZA`/`IUL`/`BAC`, arsenal bargaining for `UWD`, security guarantees for `UDC`/`SDZ`, and commune/host agreements for `FTH`/`BBH`/`GAC`/`DHC`/`KHC`. A small decision unlock or decision upgrade would make these feel less like passive recognition buttons. |
| 3 | Ancient restoration letter/envoy focuses | `KZR_caspian_patrol_letters` (`005_soviet_collapse_ancient_restorations.txt:129`), `SOG_scholar_envoy_rooms` (`:441`), `KHW_canal_recognition_letters` (`:783`), `ALN_mountain_envoy_guarantees` (`:1114`). | Mostly `set_country_flag`, small recognition gain, and either small League support or a small local authority variable. | Make each letter focus preview the later restoration identity: KZR gets Caspian ferry/convoy or toll-patrol logic, SOG gets scholar/city-court legitimacy or research/decryption, KHW gets water/canal logistics or supply construction, and ALN gets pass guarantee/mountain-road defense. |
| 4 | Ancient restoration charter capstones | `KZR_khazar_charter` (`005_soviet_collapse_ancient_restorations.txt:243`), `SOG_sogdian_city_charter` (`:570`), `KHW_khwarazmian_water_charter` (`:900`), `ALN_alan_pass_charter` (`:1231`). | `set_country_flag`; `add_to_variable = { <tag_authority> = large_mandate_gain }`; `add_to_variable = { soviet_collapse_recognition_progress = medium_recognition_gain }`. | Treat charters as concrete institutional payoffs. KZR can unlock toll/transit law decisions, SOG city-court or merchant charter decisions, KHW irrigation-rights and water-route integration, and ALN pass levy/pass-court authority. Add a visible one-time map or advisor/law payoff where appropriate. |
| 5 | Shared republic route-fork focuses | `ukr_soviet_collapse_provincial_governors_or_elected_radas` (`005_soviet_collapse_republics.txt:829`), `soviet_collapse_capital_committee_or_field_committee` (`:2705`), `caucasus_soviet_collapse_caucasus_route_fork` (`:5341`), `central_asia_soviet_collapse_southern_route_fork` (`:6191`), `moldova_soviet_collapse_moldova_route_fork` (`:7218`), `blr_soviet_collapse_which_road_is_belarus` (`:8251`), `kaz_soviet_collapse_the_congress_chooses_a_past` (`:9484`). | `set_country_flag = <route question open>` plus `add_political_power = constant:soviet_collapse_republic_focus.political_power_small`. | These are choice-defining focuses, so they should do more than pay PP. Add a temporary debate/council mission, unlock the next route decision pair, shift a legitimacy or faction-pressure value, or give a small route-specific AI strategy marker. |
| 6 | Shared republic bootstrap helper-only focuses | Legal bootstrap: `ukr_soviet_collapse_guard_the_telegraph_house`, `soviet_collapse_guard_the_radio_stations`, `internal_soviet_collapse_secure_autonomous_capital`, `baltic_soviet_collapse_restore_the_state_seal`, `caucasus_soviet_collapse_convene_mountain_and_city_councils`, `central_asia_soviet_collapse_southern_emergency_majlis`, `moldova_soviet_collapse_independent_republic_council`, `blr_soviet_collapse_national_council_of_minsk`, `kaz_soviet_collapse_alash_memory_restored`. Foreign bootstrap: `ukr_soviet_collapse_open_the_liaison_offices`, `soviet_collapse_foreign_liaison_government`, `internal_soviet_collapse_border_and_rail_liaisons`, `baltic_soviet_collapse_foreign_protection_council`, `caucasus_soviet_collapse_foreign_border_guarantees`, `central_asia_soviet_collapse_the_border_caravans`, `moldova_soviet_collapse_the_romanian_question`, `blr_soviet_collapse_foreign_corridor_administration`, `kaz_soviet_collapse_resource_concessions_debate`. | Legal set: `set_country_flag` plus `soviet_collapse_apply_focus_legal_recognition = yes`. Foreign set: `set_country_flag` plus `soviet_collapse_apply_focus_foreign_channel = yes`. | These can stay compact, but each regional tree should have one extra visible local hook: Ukraine grain/telegraph administration, Belarus rail corridor authority, Kazakhstan distance/resource concessions, Moldova Romanian/Prut diplomacy, Baltic state continuity, Caucasus pass/oil guarantee, Central Asian caravan/border authority, and internal republic capital security. |

## Missing Or Simplified Content

- No exact duplicate completion rewards remain.
- Remaining simplification is mostly helper-only focus rewards and route-opening focuses with small flat political power.
- The custom splinter helpers contain tag-conditional gameplay, so the issue is not “all effects are identical”; it is that many focus entries and player-facing reward tooltips still present as the same generic identity payoff.

## Icon Coverage

| Cluster | Current icon status | Action |
| --- | --- | --- |
| Custom splinter identity lanes | Icons are assigned per tag/focus pattern | No icon work required for this reward pass unless a replacement reward makes an icon obviously wrong. |
| Ancient restoration letters/charters | Icons are assigned and mostly route-themed | Optional: only revisit if the charter reward becomes a law/advisor/decision unlock. |
| Shared republic route forks/bootstrap | Icons are assigned | No immediate icon blocker found in this pass. |

## Localisation And Reward Mismatch

- Route-fork names imply a political decision point, but current reward is only PP and a flag.
- Ancient charter names imply a durable institution, but current reward is mostly recognition and an authority variable.
- Custom splinter focus names are highly specific, but repeated generic tooltip keys can hide the tag-specific payoff inside the helper.

## AI Behavior Gaps

- AI weights exist on the audited focuses.
- If these clusters are patched, AI should gain matching route preference nudges: debate/fork focuses should weight toward the route that fits stability, war state, SOV pressure, and foreign appetite; diplomacy focuses should weight toward ports, corridors, rail access, or security identity rather than only broad League/foreign variables.

## Validation Run

- Read required repo instructions and focus/event/subagent skills.
- Consulted offline Paradox wiki core pages plus National focus modding.
- Consulted vanilla HOI4 documentation for effects/triggers and vanilla focus examples for focus reward/AI structure.
- Parsed current Event 005 focus files read-only and confirmed 1,696 focus blocks.
- Exact duplicate `completion_reward` clusters found: 0.
- Normalized helper-only and flat-reward clusters listed above.

Skipped validation: no game load, parser executable, or live-session validation was run because this was a read-only audit handoff.

## Changed Files

- Added this report only: `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/focus_reward_duplicate_followup_2026_05_26.md`

No gameplay files were changed.
