# Event 005 Decision Cost Patch Handoff

Status: Source patch implemented under the parent-authorized Event 005 cost scope; localization integration and parent review remain pending.

## Changed files

- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- This handoff.

No localization, AI weight, MTTH constant, GUI, focus, shared helper, workbook, or CSV file was changed.

## Changed decisions, triggers, and effects

- `soviet_collapse_emergency_mobilize_reserves` now calls the shared `can_pay_soviet_collapse_emergency_mobilization_cost` trigger from both `available` and `custom_cost_trigger`; the one-use flag, three existing fees, effects, and AI weight remain as authored.
- `can_pay_soviet_collapse_emergency_mobilization_cost` checks stability, war support, and command power inclusively against the same black-friday quote values used by the payment effect.
- The emergency mobilization command-power quote changed from 80 to 60, and its matching spend constant changed from -80 to -60, because the decision skill caps command-power costs at 60.
- `central_asia_soviet_collapse_convene_pass_and_caravan_board` now spends command power, support equipment, and fuel; its infantry-equipment fee was removed from both affordability and payment.
- `central_asia_soviet_collapse_ratify_southern_survival_settlement` now spends political power, command power, and trains; its infantry- and support-equipment fees were removed from both affordability and payment.
- `soviet_collapse_route_aid_through_league_logistics` now spends fuel, trains, and convoys at the ordinary, regional, and major target rates; all matching political-power fee checks and debits were removed.
- `soviet_collapse_offer_new_union_treaty`, `soviet_collapse_open_republic_negotiation_table`, and `soviet_collapse_offer_federal_reintegration_compact` now spend political power, fuel, and trains; their command-power checks and debits were removed.
- `ukr_soviet_collapse_assign_league_arms_quota` now spends infantry equipment, support equipment, and trains; the political-power check and debit were removed, and its black-friday purchase family now records equipment spending.
- `ukr_soviet_collapse_black_sea_security_mission` and `ukr_soviet_collapse_issue_league_security_zone_mandate` now spend political power, convoys, and fuel; command-power checks and debits were removed from their shared helper.
- `ukr_soviet_collapse_register_black_soil_committees` now spends political power, infantry equipment, and support equipment; the command-power check and debit were removed.
- `ukr_soviet_collapse_execute_last_harvest_plan` now spends trains, convoys, and fuel; political-power checks and debits were removed.
- `uwr_authorize_field_release_raids` now spends manpower, infantry equipment, and support equipment; native political-power cost, army XP, command power, and artillery-equipment fees were removed from the decision, affordability trigger, and payment helper. Its existing assault-column spawn payload supplies artillery equipment and uses it in the unit templates.
- `uwr_intake_prisoner_transports` now spends manpower, infantry equipment, and support equipment; native political-power and command-power fees were removed from the decision, affordability trigger, and payment helper.
- Cost debits and affordability checks for all changed shared helpers now use matching concrete train, infantry, support, convoy, and fuel types. The arms-quota gate accepts stockpiles exactly equal to the three fixed debits and checks the matching equipment variants.

All changed paid decisions continue to use the same affordability predicate in `available` and `custom_cost_trigger`; the emergency mobilization predicate is the only newly introduced predicate.

## Localization handoff

The localization owner needs to update each base row and blocked row to the retained values below, keep inline displays at three values or fewer, and make each tooltip describe the full payment and any non-consumed requirement. The UWR raid row must not display the word `Artillery` without a verified texticon.

- `central_asia_soviet_collapse_caravan_board_cost_text`: command power, support equipment, fuel.
- `central_asia_soviet_collapse_settlement_cost_text`: political power, command power, trains.
- `soviet_collapse_foreign_league_logistics_cost_text`: dynamic fuel, trains, and convoy quotes for each target tier.
- `soviet_collapse_moscow_union_treaty_cost_text`, `soviet_collapse_moscow_negotiation_table_cost_text`, and `soviet_collapse_moscow_federal_compact_cost_text`: political power, fuel, trains.
- `ukr_soviet_collapse_league_arms_quota_cost_text`: infantry equipment, support equipment, trains.
- `ukr_soviet_collapse_black_sea_mission_cost_text`: political power, convoys, fuel.
- `ukr_soviet_collapse_black_soil_committees_cost_text`: political power, infantry equipment, support equipment.
- `ukr_soviet_collapse_last_harvest_plan_cost_text`: trains, convoys, fuel.
- `uwr_authorize_field_release_raids_cost_text`: manpower, infantry equipment, support equipment.
- `uwr_prisoner_intake_cost_text`: manpower, infantry equipment, support equipment.

These eleven exact hover keys still need localization: `mol_soviet_collapse_customs_board_cost_text_tooltip`, `mol_soviet_collapse_dniester_line_cost_text_tooltip`, `mol_soviet_collapse_patronage_limits_cost_text_tooltip`, `mol_soviet_collapse_prut_statute_cost_text_tooltip`, `mol_soviet_collapse_romanian_mission_cost_text_tooltip`, `mol_soviet_collapse_sfat_veto_cost_text_tooltip`, `ukr_soviet_collapse_black_soil_committees_cost_text_tooltip`, `ukr_soviet_collapse_bread_line_cost_text_tooltip`, `ukr_soviet_collapse_grain_census_cost_text_tooltip`, `ukr_soviet_collapse_last_harvest_plan_cost_text_tooltip`, and `ukr_soviet_collapse_village_ration_relief_cost_text_tooltip`.

## Validation and blockers

Source review confirmed the retained quotes match the affordability and debit helpers, the emergency command-power quote and debit remain paired at 60 and -60, the UWR decisions no longer carry a native political-power `cost`, the arms-quota check uses inclusive exact equipment affordability, and removed fees have no remaining references in the allowed source files.

Local syntax references used for this patch were `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` (SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`, custom-cost section starting at line 308), `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` (SHA-256 `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06`, `has_equipment` syntax at line 1516 and example at line 1534), installed `documentation\triggers_documentation.md` (SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`, `has_stability` and `has_war_support` entries start at lines 4800 and 5033), installed `documentation\dynamic_variables_documentation.md` (SHA-256 `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA`, reader entries at lines 435 and 439), and installed `documentation\effects_documentation.md` (SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`, `add_equipment_to_stockpile` example at line 1252).

The applicable Event 005 design sources were `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_3_decisions_missions_influence.md` (SHA-256 `9ED5133F5B14667B224E29739FF7EC3A4F7230C8F899DA45A9DEFD33D05D8AD9`, cost-localisation section starts at line 137) and `docs/specs/005_soviet_collapse_specs/005_soviet_collapse_unconventional_warfare_republic.md` (SHA-256 `1E794715AE4BE1123162AB8C4B6B24AD424F3C4592B6CDDD0F2F72D126F72883`, field-release action requirement at line 61).

The full helper-wrapper `hoi4.script_validate` call returned `SCRIPT_CHECK_PARTIAL`: the custom trigger names were unresolved as native commands, so it checked no commands in those bodies. A narrowed payment-effect snippet returned `SCRIPT_CHECK_PARTIAL` with `add_manpower` and `add_equipment_to_stockpile` command kinds and country scope supported, but its equipment argument blocks remained unchecked. Narrowed trigger validation remained pending for more than one minute and was terminated, so there is no completed trigger validation result.

The prior narrow `hoi4.decision_inspect` scenario call remained pending and was terminated during the audit; no scenario balance or runtime acceptance is claimed. Although no `ai_will_do` score was changed, removing fees changes AI affordability and can change its available-decision ranking, so the probability auditor should compare the same named scenarios after its baseline route returns. No post-patch probability comparison is available. The assigned localization owner must update the 12 cost rows and the 11 missing hover keys before the cost surfaces are complete.

The working-tree DHC helper line change in `common/scripted_effects/005_soviet_collapse_effects.txt` predated this patch and is preserved unchanged. The parent’s concurrent changes to `soviet_collapse_initialize_crisis_values`, `soviet_collapse_apply_breakaway_setup_package`, and `soviet_collapse_apply_regional_faction_invite` were also left intact.
