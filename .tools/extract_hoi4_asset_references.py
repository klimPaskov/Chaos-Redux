#!/usr/bin/env python3
"""Build the allowlisted visual-reference library used by asset agents.

The review PNGs under ``chaos-redux-event-assets/assets/vanilla_reference``
are never runtime mod assets. This script preserves each source canvas, records
exact provenance, and creates one contact sheet per semantic type without
normalising or repainting the source art.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import shutil

from PIL import Image, ImageDraw, ImageOps


@dataclass(frozen=True)
class Reference:
	section: str
	category: str
	review_path: str
	source_path: str
	related_definition: str = ""
	sheet: str = ""
	source_root: str = "vanilla"


REFERENCE_ROOT = Path(
	".agents/skills/chaos-redux-event-assets/assets/vanilla_reference"
)


def ref(
	section: str,
	category: str,
	review_path: str,
	source_path: str,
	related_definition: str = "",
	sheet: str = "",
	source_root: str = "vanilla",
) -> Reference:
	return Reference(section, category, review_path, source_path, related_definition, sheet, source_root)


BASE_REFERENCES = (
	# Portraits and flat flag ladders.
	ref("Portraits and flags", "Leader portrait", "portraits/leaders/den_thorvald_stauning.png", "gfx/leaders/DEN/Portrait_Denmark_Thorvald_Stauning.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Leader portrait", "portraits/leaders/ire_eamon_de_valera.png", "gfx/leaders/IRE/Portrait_Ireland_Eamon_de_Valera.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Leader portrait", "portraits/leaders/fin_carl_mannerheim.png", "gfx/leaders/FIN/portrait_fin_carl_mannerheim.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Leader portrait", "portraits/leaders/eth_haile_selassie.png", "gfx/leaders/ETH/Portrait_Ethiopia_Haile_Selassie.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Leader portrait", "portraits/leaders/ice_sveinn_bjornsson.png", "gfx/leaders/ICE/portrait_ice_sveinn_bjornsson.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Leader portrait", "portraits/leaders/lux_charlotte.png", "gfx/leaders/LUX/portrait_LUX_charlotte_wilhelmine.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Land commander portrait", "portraits/commanders/generic_africa_land_1.png", "gfx/leaders/Africa/Portrait_Africa_Generic_land_1.dds", "interface/_random_portraits.gfx", "portraits_and_flags"),
	ref("Portraits and flags", "Naval commander portrait", "portraits/commanders/generic_africa_navy_1.png", "gfx/leaders/Africa/Portrait_Africa_Generic_navy_1.dds", "interface/_random_portraits.gfx", "portraits_and_flags"),
	ref("Portraits and flags", "Operative portrait", "portraits/operatives/den_flemming_muus.png", "dlc/dlc028_la_resistance/gfx/leaders/DEN/portrait_DEN_flemming_muus.dds", "dlc/dlc028_la_resistance/interface/lar_portraits.gfx", "portraits_and_flags"),
	ref("Portraits and flags", "Operative portrait", "portraits/operatives/aus_erwin_von_lahousen.png", "dlc/dlc028_la_resistance/gfx/leaders/AUS/portrait_AUS_erwin_von_lahousen.dds", "dlc/dlc028_la_resistance/interface/lar_portraits.gfx", "portraits_and_flags"),
	ref("Portraits and flags", "Advisor dossier", "portraits/advisors/generic_europe_1.png", "gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Advisor dossier", "portraits/advisors/generic_female_europe.png", "gfx/interface/ideas/idea_generic_political_advisor_female_europe.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Advisor dossier", "portraits/advisors/generic_asia_1.png", "gfx/interface/ideas/idea_generic_political_advisor_asia_1.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Advisor dossier", "portraits/advisors/generic_africa_1.png", "gfx/interface/ideas/idea_generic_political_advisor_africa_1.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Advisor dossier", "portraits/advisors/generic_europe_6.png", "gfx/interface/ideas/idea_generic_political_advisor_europe_6.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Advisor dossier", "portraits/advisors/high_command_fevzi_cakmak.png", "gfx/interface/ideas/idea_tur_fevzi_cakmak_high_command.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Army-small dossier", "portraits/advisors/army_small_ger_friedrich_paulus.png", "gfx/interface/ideas/idea_GER_friedrich_paulus.dds", "interface/_leader_portraits.gfx; common/characters/GER.txt", "portraits_and_flags"),
	ref("Portraits and flags", "Army-small dossier", "portraits/advisors/army_small_ger_gunther_von_kluge.png", "gfx/interface/ideas/idea_GER_gunther_von_kluge.dds", "interface/_leader_portraits.gfx; common/characters/GER.txt", "portraits_and_flags"),
	ref("Portraits and flags", "Army-small dossier", "portraits/advisors/army_small_ger_erwin_rommel.png", "gfx/interface/ideas/idea_erwin_rommel.dds", "interface/ideas.gfx; common/characters/GER.txt", "portraits_and_flags"),
	ref("Portraits and flags", "Flag, normal", "flags/normal/arm.png", "gfx/flags/ARM.tga", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Flag, medium", "flags/medium/arm.png", "gfx/flags/medium/ARM.tga", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Flag, small", "flags/small/arm.png", "gfx/flags/small/ARM.tga", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Flag, normal", "flags/normal/ice.png", "gfx/flags/ICE.tga", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Flag, medium", "flags/medium/ice.png", "gfx/flags/medium/ICE.tga", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Flag, small", "flags/small/ice.png", "gfx/flags/small/ICE.tga", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Flag, normal", "flags/normal/isr.png", "gfx/flags/ISR.tga", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Flag, medium", "flags/medium/isr.png", "gfx/flags/medium/ISR.tga", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Flag, small", "flags/small/isr.png", "gfx/flags/small/ISR.tga", sheet="portraits_and_flags"),

	# Core event and national-content icon families.
	ref("Core gameplay icons", "National focus", "icons/national_focus/focus_generic_nuclear_development.png", "gfx/interface/goals/focus_generic_nuclear_development.dds", sheet="icons"),
	ref("Core gameplay icons", "National focus", "icons/national_focus/focus_aus_reestablish_austrian_navy.png", "gfx/interface/goals/focus_AUS_reestablish_austrian_navy.dds", sheet="icons"),
	ref("Core gameplay icons", "National focus", "icons/national_focus/focus_eth_expand_the_levy.png", "gfx/interface/goals/focus_ETH_expand_the_levy.dds", sheet="icons"),
	ref("Core gameplay icons", "Idea / national spirit", "icons/ideas/idea_generic_deal_with_the_devil.png", "gfx/interface/ideas/idea_generic_deal_with_the_devil.dds", sheet="icons"),
	ref("Core gameplay icons", "Idea / national spirit", "icons/ideas/idea_aus_habsburg_monarchy_restored.png", "gfx/interface/ideas/idea_AUS_habsburg_monarchy_restored.dds", sheet="icons"),
	ref("Core gameplay icons", "Idea / national spirit", "icons/ideas/idea_chi_incompetent_officers.png", "gfx/interface/ideas/idea_chi_incompetent_officers.dds", sheet="icons"),
	ref("Core gameplay icons", "Decision", "icons/decisions/decision_generic_intelligence_operation.png", "gfx/interface/decisions/decision_generic_intelligence_operation.dds", sheet="icons"),
	ref("Core gameplay icons", "Decision", "icons/decisions/decisions_generic_infiltration.png", "gfx/interface/decisions/decisions_generic_infiltration.dds", sheet="icons"),
	ref("Core gameplay icons", "Decision", "icons/decisions/decision_border_war.png", "gfx/interface/decisions/decision_border_war.dds", sheet="icons"),
	ref("Core gameplay icons", "Mission (decision pipeline)", "icons/missions/decision_chl_mapuche_organizations_mission.png", "gfx/interface/decisions/decision_CHL_ibanez_cracking_down_on_mapuche_organizations_mission.dds", sheet="icons"),
	ref("Core gameplay icons", "Decision category", "icons/decision_categories/decision_category_generic_prospect_for_resources.png", "gfx/interface/decisions/decision_category_generic_prospect_for_resources.dds", sheet="icons"),
	ref("Core gameplay icons", "Decision category", "icons/decision_categories/decision_category_hol_secret_staff_talks.png", "gfx/interface/decisions/decision_category_hol_secret_staff_talks.dds", sheet="icons"),
	ref("Core gameplay icons", "Achievement, completed", "icons/achievements/30_minutes_of_hel.png", "gfx/achievements/30_minutes_of_hel.dds", sheet="icons"),
	ref("Core gameplay icons", "Achievement, eligible grey", "icons/achievements/30_minutes_of_hel_grey.png", "gfx/achievements/30_minutes_of_hel_grey.dds", sheet="icons"),
	ref("Core gameplay icons", "Achievement, not eligible", "icons/achievements/30_minutes_of_hel_not_eligible.png", "gfx/achievements/30_minutes_of_hel_not_eligible.dds", sheet="icons"),
	ref("Core gameplay icons", "Officer corps spirit", "icons/officer_corps_spirits/spirit_idea_aggressive_reconnaissance.png", "gfx/interface/officer_corp/spirits/spirit_idea_aggressive_reconnaissance.dds", sheet="icons"),
	ref("Core gameplay icons", "Officer corps spirit", "icons/officer_corps_spirits/spirit_idea_air_power_projection.png", "gfx/interface/officer_corp/spirits/spirit_idea_air_power_projection.dds", sheet="icons"),
	ref("Core gameplay icons", "Officer corps spirit", "icons/officer_corps_spirits/spirit_idea_big_gun_club.png", "gfx/interface/officer_corp/spirits/spirit_idea_big_gun_club.dds", sheet="icons"),
	ref("Core gameplay icons", "Technology", "icons/technologies/basic_machine_tools.png", "gfx/interface/technologies/basic_machine_tools.dds", sheet="icons"),
	ref("Core gameplay icons", "Technology", "icons/technologies/radio.png", "gfx/interface/technologies/radio.dds", sheet="icons"),
	ref("Core gameplay icons", "Special project", "icons/special_projects/sp_nuclear_bomb.png", "gfx/interface/special_project/project_icons/sp_nuclear_bomb.dds", sheet="icons"),
	ref("Core gameplay icons", "Special project", "icons/special_projects/sp_naval_rocket_launching_submarine.png", "gfx/interface/special_project/project_icons/sp_naval_rocket_launching_submarine.dds", sheet="icons"),
	ref("Core gameplay icons", "Balance of power", "icons/balance_of_power/bop_fin_paasikivi_good_side.png", "gfx/interface/bop/bop_FIN_paasikivi_good_side.dds", sheet="icons"),
	ref("Core gameplay icons", "Balance of power", "icons/balance_of_power/prc_bop_left_side.png", "gfx/interface/bop/PRC_bop_left_side.dds", sheet="icons"),

	# Additional engine surfaces frequently used by large event packages.
	ref("Extended gameplay icons", "Intelligence agency upgrade", "icons/intelligence_agency/agency_cryptology_1.png", "gfx/interface/operatives/icons/agency_cryptology_1.dds", "interface/countryintelligenceagencyview.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Intelligence agency upgrade", "icons/intelligence_agency/agency_commando_training.png", "gfx/interface/operatives/icons/agency_commando_training.dds", "interface/countryintelligenceagencyview.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Intelligence operation", "icons/intelligence_operations/infiltrate_armed_forces.png", "gfx/interface/operations/infiltrate_armed_forces.dds", "interface/lar_operations.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Intelligence operation", "icons/intelligence_operations/collaboration_government.png", "gfx/interface/operations/collaboration_government.dds", "interface/lar_operations.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Commander trait", "icons/commander_traits/trait_adaptable.png", "gfx/interface/traits/trait_adaptable.dds", "interface/unitleaderwindow.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Commander trait", "icons/commander_traits/trait_panzer_leader.png", "gfx/interface/traits/trait_panzer_leader.dds", "interface/unitleaderwindow.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Medal", "icons/medals/eng_medal_1.png", "gfx/interface/medals/ENG_medal_1.dds", "interface/medals.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Medal", "icons/medals/eng_medal_2.png", "gfx/interface/medals/ENG_medal_2.dds", "interface/medals.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Military raid outcome", "icons/military_raids/raid_outcome_success.png", "gfx/interface/military_raids/raid_outcome_success_icon.dds", "interface/military_raids/military_raids.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Military raid unit", "icons/military_raids/raid_unit_paratrooper.png", "gfx/interface/military_raids/raid_unit_large_paratrooper.dds", "interface/military_raids/military_raids.gfx", "icons_extended"),
	ref("Extended gameplay icons", "State modifier", "icons/state_modifiers/cze_sudetenland_separatism.png", "gfx/interface/state_modifiers/modifiers_CZE_sudetenland_separatism.dds", "interface/countrystateview.gfx", "icons_extended"),
	ref("Extended gameplay icons", "State modifier", "icons/state_modifiers/conscription_exemptions_granted.png", "gfx/interface/state_modifiers/modifiers_conscription_exemptions_granted.dds", "interface/countrystateview.gfx", "icons_extended"),
	ref("Extended gameplay icons", "MIO trait", "icons/military_industrial_organizations/generic_trait_facilities.png", "gfx/interface/military_industrial_organization/generic_mio_trait_icon_facilities.dds", "interface/military_industrial_organization/industrial_organization_policies_and_traits_icons.gfx", "icons_extended"),
	ref("Extended gameplay icons", "MIO department", "icons/military_industrial_organizations/department_air_transport.png", "gfx/interface/military_industrial_organization/department_icons/generic_mio_department_icon_air_transport.dds", "interface/military_industrial_organization/industrial_organization_policies_and_traits_icons.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Faction logo", "icons/factions/allies.png", "gfx/interface/factions/faction_logos/faction_icon_allies.dds", "interface/factions/factions.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Faction logo, miniature", "icons/factions/allies_miniature.png", "gfx/interface/factions/faction_logos/faction_icon_allies_miniature.dds", "interface/factions/factions.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Building icon", "icons/buildings/fort.png", "gfx/interface/buildings/building_fort_icon.dds", "interface/countrystateview.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Historical building / facility", "icons/buildings/facility.png", "gfx/interface/buildings/historical_buildings/large/facility_icon.dds", "interface/countrystateview.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Modifier icon", "icons/modifiers/army_speed_factor.png", "gfx/interface/modifiers/MODIFIER_ARMY_SPEED_FACTOR.dds", "interface/countryarmyview.gfx", "icons_extended"),
	ref("Extended gameplay icons", "Modifier icon", "icons/modifiers/max_planning.png", "gfx/interface/modifiers/MODIFIER_MAX_PLANNING.dds", "interface/countryarmyview.gfx", "icons_extended"),

	# Event art surfaces.
	ref("Event art", "Report event", "event_art/report/report_event_soldiers_parade.png", "gfx/event_pictures/report_event_soldiers_parade.dds", sheet="event_art"),
	ref("Event art", "Report event", "event_art/report/report_event_soldiers_marching.png", "gfx/event_pictures/report_event_soldiers_marching.dds", sheet="event_art"),
	ref("Event art", "News event", "event_art/news/news_event_001.png", "gfx/event_pictures/news_event_001.dds", sheet="event_art"),
	ref("Event art", "News event", "event_art/news/news_event_002.png", "gfx/event_pictures/news_event_002.dds", sheet="event_art"),

	# Equipment art, land counters, map counters, and 3D material references.
	ref("Unit visual pipelines", "2D equipment technology art", "units/equipment/technology_art/infantry_equipment_0.png", "gfx/interface/technologies/infantry_equipment_0.dds", "interface/Technologies.gfx", "units"),
	ref("Unit visual pipelines", "2D equipment technology art", "units/equipment/technology_art/motorized_equipment_1.png", "gfx/interface/technologies/motorized_equipment_1.dds", "interface/Technologies.gfx", "units"),
	ref("Unit visual pipelines", "2D equipment technology art", "units/equipment/technology_art/support_equipment_1.png", "gfx/interface/technologies/support_equipment_1.dds", "interface/Technologies.gfx", "units"),
	ref("Unit visual pipelines", "Land division counter, 2 frames", "units/land/counters_large/unit_infantry_icon.png", "gfx/interface/counters/divisions_large/unit_infantry_icon.dds", "interface/subuniticons.gfx", "units"),
	ref("Unit visual pipelines", "Land division counter, 2 frames", "units/land/counters_large/unit_motorized_icon.png", "gfx/interface/counters/divisions_large/unit_motorized_icon.dds", "interface/subuniticons.gfx", "units"),
	ref("Unit visual pipelines", "Land division counter, 2 frames", "units/land/counters_large/unit_medium_tank_icon.png", "gfx/interface/counters/divisions_large/unit_medium_tank_icon.dds", "interface/subuniticons.gfx", "units"),
	ref("Unit visual pipelines", "Land map counter, 2 frames", "units/land/map_counters/onmap_infantry.png", "gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds", "interface/subuniticons.gfx", "units_expanded"),
	ref("Unit visual pipelines", "Land map counter, 2 frames", "units/land/map_counters/onmap_artillery.png", "gfx/interface/counters/divisions_small/onmap_unit_art_icon.dds", "interface/subuniticons.gfx", "units_expanded"),
	ref("Unit visual pipelines", "Division-template emblem", "units/land/division_template_emblems/custom_template_000.png", "gfx/interface/counters/division_templates_large/custom_template_000.dds", "interface/subuniticons.gfx", "units_expanded"),
	ref("Unit visual pipelines", "Division-template emblem", "units/land/division_template_emblems/custom_template_001.png", "gfx/interface/counters/division_templates_large/custom_template_001.dds", "interface/subuniticons.gfx", "units_expanded"),
	ref("Unit visual pipelines", "Air map counter", "units/air/map_counters/onmap_fighter.png", "gfx/interface/counters/air_small/onmap_fighter.dds", "interface/navalcombat.gfx", "units_expanded"),
	ref("Unit visual pipelines", "Air map counter, inverted", "units/air/map_counters/onmap_fighter_inverted.png", "gfx/interface/counters/air_small/onmap_fighter_inverted.dds", "interface/navalcombat.gfx", "units_expanded"),
	ref("Unit visual pipelines", "Air map counter, inverted", "units/air/map_counters/onmap_tactical_bomber_inverted.png", "gfx/interface/counters/air_small/onmap_tac_bomber_inverted.dds", "interface/navalcombat.gfx", "units_expanded"),
	ref("Unit visual pipelines", "Naval map counter", "units/naval/map_counters/onmap_destroyer.png", "gfx/interface/counters/ships_small/onmap_destroyer.dds", "interface/subuniticons.gfx", "units_expanded"),
	ref("Unit visual pipelines", "Naval map counter, inverted", "units/naval/map_counters/onmap_destroyer_inverted.png", "gfx/interface/counters/ships_small/onmap_destroyer_inverted.dds", "interface/subuniticons.gfx", "units_expanded"),
	ref("Unit visual pipelines", "Naval map counter", "units/naval/map_counters/onmap_submarine.png", "gfx/interface/counters/ships_small/onmap_submarine.dds", "interface/subuniticons.gfx", "units_expanded"),
	ref("Unit visual pipelines", "3D land model diffuse material", "units/models_3d/land_materials/eastern_european_infantry_diffuse.png", "gfx/models/units/eastern_european_infantry_diffuse.dds", "gfx/models/units/eastern_european_infantry.mesh", "units"),
	ref("Unit visual pipelines", "3D land model diffuse material", "units/models_3d/land_materials/generic_tank_medium_diffuse.png", "gfx/models/units/tanks/generic_tank_medium_diffuse.dds", "gfx/models/units/tanks/generic_tank_medium.mesh", "units"),
	ref("Unit visual pipelines", "3D air model diffuse material", "units/models_3d/air_materials/generic_plane_light_diffuse.png", "gfx/models/units/planes/generic_plane_light_diffuse.dds", "gfx/models/units/planes/generic_plane_light.mesh", "units_expanded"),
	ref("Unit visual pipelines", "3D naval model diffuse material", "units/models_3d/naval_materials/generic_destroyer_diffuse.png", "gfx/models/units/ships/generic_destroyer_diffuse.dds", "gfx/models/units/ships/generic_destroyer.mesh", "units_expanded"),
)


def asset_ref(
	section: str,
	category: str,
	asset_dir: str,
	source_path: str,
	filename: str | None = None,
	related_definition: str = "",
	source_root: str = "vanilla",
) -> Reference:
	name = filename or Path(source_path).stem.lower()
	return ref(
		section,
		category,
		f"{asset_dir.rstrip('/')}/{name}.png",
		source_path,
		related_definition=related_definition,
		source_root=source_root,
	)


def vanilla_asset(
	section: str,
	category: str,
	asset_dir: str,
	source_path: str,
	filename: str | None = None,
	related_definition: str = "",
) -> Reference:
	return asset_ref(section, category, asset_dir, source_path, filename, related_definition)


def chaos_asset(
	section: str,
	category: str,
	asset_dir: str,
	source_path: str,
	filename: str | None = None,
	related_definition: str = "",
) -> Reference:
	return asset_ref(
		section,
		category,
		asset_dir,
		source_path,
		filename,
		related_definition,
		source_root="chaos_redux",
	)


def moved_asset(
	section: str,
	category: str,
	review_path: str,
	related_definition: str = "",
) -> Reference:
	"""Register a legacy review PNG after it has been moved into the canonical tree."""
	return ref(
		section,
		category,
		review_path,
		(REFERENCE_ROOT / review_path).as_posix(),
		related_definition=related_definition,
		source_root="moved_review",
	)


EXTRA_REFERENCES = [
	# Portraits: keep each portrait family useful for comparison work.
	vanilla_asset("Portraits and flags", "Leader portrait", "portraits/leaders", "gfx/leaders/Africa/Portrait_Africa_Generic_1.dds", "africa_generic_1"),
	vanilla_asset("Portraits and flags", "Leader portrait", "portraits/leaders", "gfx/leaders/AFG/Portrait_Afghanistan_Mohammed_Zahir_Shah.dds", "afg_mohammed_zahir_shah"),
	vanilla_asset("Portraits and flags", "Land commander portrait", "portraits/commanders", "gfx/leaders/Africa/Portrait_Africa_Generic_land_2.dds", "generic_africa_land_2", "interface/_random_portraits.gfx"),
	vanilla_asset("Portraits and flags", "Land commander portrait", "portraits/commanders", "gfx/leaders/Africa/Portrait_Africa_Generic_land_3.dds", "generic_africa_land_3", "interface/_random_portraits.gfx"),
	vanilla_asset("Portraits and flags", "Naval commander portrait", "portraits/commanders", "gfx/leaders/Africa/Portrait_Africa_Generic_navy_2.dds", "generic_africa_navy_2", "interface/_random_portraits.gfx"),
	vanilla_asset("Portraits and flags", "Operative portrait", "portraits/operatives", "dlc/dlc028_la_resistance/gfx/leaders/Africa/portrait_africa_generic_operative_female_1.dds", "africa_generic_operative_female_1", "dlc/dlc028_la_resistance/interface/lar_portraits.gfx"),
	vanilla_asset("Portraits and flags", "Operative portrait", "portraits/operatives", "dlc/dlc028_la_resistance/gfx/leaders/Africa/portrait_africa_generic_operative_female_2.dds", "africa_generic_operative_female_2", "dlc/dlc028_la_resistance/interface/lar_portraits.gfx"),
	vanilla_asset("Portraits and flags", "Operative portrait", "portraits/operatives", "dlc/dlc028_la_resistance/gfx/leaders/Africa/portrait_africa_generic_operative_male_1.dds", "africa_generic_operative_male_1", "dlc/dlc028_la_resistance/interface/lar_portraits.gfx"),

	# Flags: include complete normal, medium, and small ladders for each tag.
	*[vanilla_asset("Portraits and flags", f"Flag, {size_name}", f"flags/{size_name}", f"gfx/flags/{size_dir + '/' if size_dir else ''}{tag}.tga", tag.lower(),) for tag in ("AFG_second_empire_neutrality", "ANU_fascism", "ARG_gen_nazism_party", "ARM_UK") for size_name, size_dir in (("normal", ""), ("medium", "medium"), ("small", "small"))],

	# National focus icons. This family is intentionally broad (16 examples).
	*[vanilla_asset("Core gameplay icons", "National focus", "icons/national_focus", source, filename) for source, filename in (
		("gfx/interface/goals/focus_ARG_fascist_researchers.dds", "focus_arg_fascist_researchers"),
		("gfx/interface/goals/focus_AUS_bring_phonix_insurance_from_the_ashes.dds", "focus_aus_bring_phonix_insurance_from_the_ashes"),
		("gfx/interface/goals/focus_AUS_danubian_socialist_communes.dds", "focus_aus_danubian_socialist_communes"),
		("gfx/interface/goals/focus_AUS_defence_of_the_homeland.dds", "focus_aus_defence_of_the_homeland"),
		("gfx/interface/goals/focus_AUS_heritage_of_an_empire.dds", "focus_aus_heritage_of_an_empire"),
		("gfx/interface/goals/focus_AUS_lawmaking_leniency.dds", "focus_aus_lawmaking_leniency"),
		("gfx/interface/goals/focus_BRA_kgbrazil.dds", "focus_bra_kgbrazil"),
		("gfx/interface/goals/focus_BRA_ulasr.dds", "focus_bra_ulasr"),
		("gfx/interface/goals/focus_ETH_boots_on_the_shore.dds", "focus_eth_boots_on_the_shore"),
		("gfx/interface/goals/focus_generic_pope.dds", "focus_generic_pope"),
		("gfx/interface/goals/focus_generic_population_growth.dds", "focus_generic_population_growth"),
		("dlc/dlc001_german_historical_portraits/gfx/interface/goals/focus_GER_strengthen_the_waffen_ss.dds", "focus_ger_strengthen_the_waffen_ss"),
		("gfx/interface/goals/focus_ICE_hrafninn_flygur.dds", "focus_ice_hrafninn_flygur"),
	)],

	# Ideas and national spirits. Keep this family at 15 examples.
	*[vanilla_asset("Core gameplay icons", "Idea / national spirit", "icons/ideas", source, filename) for source, filename in (
		("gfx/interface/ideas/fra_liberte_egalite_solidarite.dds", "fra_liberte_egalite_solidarite"),
		("gfx/interface/ideas/generic_volunteer_expedition_bonus.dds", "generic_volunteer_expedition_bonus"),
		("gfx/interface/ideas/generic_wall_line.dds", "generic_wall_line"),
		("gfx/interface/ideas/home_of_the_revolution.dds", "home_of_the_revolution"),
		("gfx/interface/ideas/idea_CZE_ceskoslovenska_lodstvo.dds", "idea_cze_ceskoslovenska_lodstvo"),
		("gfx/interface/ideas/idea_DEN_danish_produce.dds", "idea_den_danish_produce"),
		("gfx/interface/ideas/idea_generic_coastal_defense_ships.dds", "idea_generic_coastal_defense_ships"),
		("gfx/interface/ideas/idea_generic_constitutional_guarantee.dds", "idea_generic_constitutional_guarantee"),
		("gfx/interface/ideas/idea_generic_flexible_foreign_policy.dds", "idea_generic_flexible_foreign_policy"),
		("gfx/interface/ideas/idea_generic_oppression.dds", "idea_generic_oppression"),
		("gfx/interface/ideas/idea_generic_purge.dds", "idea_generic_purge"),
		("gfx/interface/ideas/generic_air_bonus.dds", "generic_air_bonus"),
	)],

	# Decisions and decision categories are separate visual families.
	*[vanilla_asset("Core gameplay icons", "Decision", "icons/decisions", f"gfx/interface/decisions/{name}.dds", name.lower()) for name in (
		"decision_generic_disband_irregulars",
		"decision_generic_guerilla_base_2",
		"decision_tungsten",
		"decision_usa_congress",
		"decisions_generic_counter_infiltration_3",
		"decision_aluminium",
		"decision_BOL_establish_arica_department",
		"decision_BOL_reintegrate_acre_state",
		"decision_BOL_reintegrate_litoral_department",
		"decision_BRA_integralism",
		"decision_cat_central_europan_federation",
		"decision_cat_exiles",
	)],
	*[vanilla_asset("Core gameplay icons", "Decision category", "icons/decision_categories", f"gfx/interface/decisions/{name}.dds", name.lower()) for name in (
		"decision_category_CHL_mapuche_reconcilliation_decisions",
		"decision_category_generic_arms_trade",
		"decision_category_generic_communism",
		"decision_category_generic_communist_revolution",
		"decision_category_infiltration",
		"decision_category_JAP_imperial_glory_red",
		"decision_category_spr_reassert_american_dominance",
		"decision_category_army_reform",
		"decision_category_border_conflicts",
		"decision_category_border_war",
		"decision_category_generic",
		"decision_category_generic_crisis",
		"decision_category_generic_democracy",
	)],
	*[vanilla_asset("Core gameplay icons", "Mission / decision pipeline", "icons/missions", f"gfx/interface/decisions/decisions_generic_counter_infiltration_{suffix}.dds", f"decisions_generic_counter_infiltration_{suffix}") for suffix in ("0", "1", "2", "3")],

	# Achievements include all three UI states for each reference.
	*[vanilla_asset("Core gameplay icons", f"Achievement, {state}", "icons/achievements", f"gfx/achievements/{name}{suffix}.dds", f"{name}{suffix}") for name in ("assuming_direct_control", "britzkrieg", "crusader_kings_2", "the_revolution_triumphant") for suffix, state in (("", "completed"), ("_grey", "eligible grey"), ("_not_eligible", "not eligible"))],

	# Officer corps, intelligence, traits, medals, raids, state modifiers, MIOs,
	# factions, buildings, and modifiers all have five or more examples.
	vanilla_asset("Extended gameplay icons", "Officer corps spirit", "icons/officer_corps_spirits", "gfx/interface/officer_corp/spirits/spirit_idea_aa_curtain.dds", "spirit_idea_aa_curtain"),
	vanilla_asset("Extended gameplay icons", "Officer corps spirit", "icons/officer_corps_spirits", "gfx/interface/officer_corp/spirits/spirit_idea_academy_scholarships.dds", "spirit_idea_academy_scholarships"),
	*[vanilla_asset("Extended gameplay icons", "Intelligence agency upgrade", "icons/intelligence_agency", f"gfx/interface/operatives/icons/{name}.dds", name) for name in ("agency_anti_partisan", "agency_cryptology_2", "agency_invisible_ink")],
	*[vanilla_asset("Extended gameplay icons", "Intelligence operation", "icons/intelligence_operations", f"gfx/interface/operations/{name}.dds", name) for name in ("boost_resistance", "capture_ciphers", "coordinated_strike")],
	*[vanilla_asset("Extended gameplay icons", "Commander trait", "icons/commander_traits", f"gfx/interface/traits/personal/{name}.dds", name) for name in ("trait_armor_officer", "trait_brilliant_strategist", "trait_infantry_officer")],
	*[vanilla_asset("Extended gameplay icons", "Medal", "icons/medals", f"gfx/interface/medals/{name}.dds", name.lower()) for name in ("ENG_medal_3", "FRA_medal_1", "generic_communism_medal_1")],
	vanilla_asset("Extended gameplay icons", "Military raid outcome", "icons/military_raids", "gfx/interface/military_raids/raid_outcome_critical_success_icon.dds", "raid_outcome_critical_success"),
	vanilla_asset("Extended gameplay icons", "Military raid outcome", "icons/military_raids", "gfx/interface/military_raids/raid_outcome_failure_icon.dds", "raid_outcome_failure"),
	vanilla_asset("Extended gameplay icons", "Military raid unit", "icons/military_raids", "gfx/interface/military_raids/map_icons/raid_unit_icon_air_raids.dds", "raid_unit_air_raids"),
	*[vanilla_asset("Extended gameplay icons", "State modifier", "icons/state_modifiers", f"gfx/interface/state_modifiers/{name}.dds", name.lower()) for name in ("modifier_generic_guerilla_base", "modifier_generic_sabotage", "modifier_generic_state_assault")],
	*[vanilla_asset("Extended gameplay icons", "MIO department", "icons/military_industrial_organizations", f"gfx/interface/military_industrial_organization/department_icons/{name}.dds", name) for name in ("generic_mio_department_icon_air_transport_engine", "generic_mio_department_icon_air_transport_line_efficiency", "generic_mio_department_icon_air_transport_production")],
	*[vanilla_asset("Extended gameplay icons", "Faction logo", "icons/factions", f"gfx/interface/factions/faction_logos/{name}.dds", name) for name in ("faction_logo_axis", "faction_logo_comintern", "faction_logo_eu")],
	*[vanilla_asset("Extended gameplay icons", "Building icon", "icons/buildings", f"gfx/interface/buildings/{name}.dds", name) for name in ("building_intel_icon", "building_railway_gun", "building_no_building")],
	*[vanilla_asset("Extended gameplay icons", "Modifier icon", "icons/modifiers", f"gfx/interface/modifiers/{name}.dds", name.lower()) for name in ("MODIFIER_ATTRITION", "MODIFIER_ORG_LOSS_WHEN_MOVING", "MODIFIER_SUPPLY_CONSUMPTION_FACTOR")],

	# Event art is split by use, with one sheet per subtype.
	*[vanilla_asset("Event art", "Report event", "event_art/report", f"gfx/event_pictures/{name}.dds", name) for name in ("report_event_001", "report_event_airplane_crash", "report_event_african_soldiers")],
	*[vanilla_asset("Event art", "News event", "event_art/news", f"gfx/event_pictures/{name}.dds", name) for name in ("news_event_003", "news_event_004", "news_event_005")],
	chaos_asset("Event art", "Super event", "event_art/super_event", "gfx/super_events/003_holy_realm/super_event_angelic_world_order.dds", "super_event_angelic_world_order"),
	chaos_asset("Event art", "Super event", "event_art/super_event", "gfx/super_events/007_fury/super_event_world_in_fury.dds", "super_event_world_in_fury"),
	chaos_asset("Event art", "Super event", "event_art/super_event", "docs/assets/006_independence_wave/dds_decoded_png/super_events/super_event_006_asset_005_league_formation.png", "super_event_006_league_formation"),
	moved_asset("Event art", "Super event, Chaos Redux review copy", "event_art/super_event/super_event_angel_directorate.png"),
	moved_asset("Event art", "Super event, Chaos Redux review copy", "event_art/super_event/super_event_divine_sovereignty.png"),
	# Balance of power, special projects, and the moved legacy examples.
	*[vanilla_asset("Core gameplay icons", "Balance of power", "icons/balance_of_power", f"gfx/interface/bop/{name}.dds", name.lower()) for name in (
		"bop_FIN_paasikivi_bad_improved_side",
		"bop_FIN_paasikivi_bad_side",
		"bop_FIN_paasikivi_good_improved_side",
		"bop_FIN_prince_wolfgang_bad_improved_side",
		"bop_FIN_prince_wolfgang_bad_side",
		"bop_FIN_prince_wolfgang_good_improved_side",
		"bop_FIN_prince_wolfgang_good_side",
		"PRC_bop_left_side_max",
		"PRC_bop_right_side",
		"PRC_bop_right_side_guotao",
	)],
	*[vanilla_asset("Core gameplay icons", "Special project", "icons/special_projects", f"gfx/interface/special_project/project_icons/{name}.dds", name) for name in (
		"sp_air_axial_jet_engine",
		"sp_commercial_nuclear_reactor",
		"sp_land_flamethrower_tank",
		"sp_rockets_rocket_interceptor",
	)],
	moved_asset("Core gameplay icons", "Special project, Chaos Redux review copy", "icons/special_projects/chaos_redux/sp_plague_bomb.png"),
	moved_asset("Core gameplay icons", "Special project, Chaos Redux review copy", "icons/special_projects/chaos_redux/sp_sarin_bomb.png"),

	# The legacy achievement template images are still useful as UI-state examples.
	moved_asset("Core gameplay icons", "Achievement template, Chaos Redux review copy", "icons/achievements/chaos_redux/achievement.png"),
	moved_asset("Core gameplay icons", "Achievement template, Chaos Redux review copy", "icons/achievements/chaos_redux/achievement_grey.png"),
	moved_asset("Core gameplay icons", "Achievement template, Chaos Redux review copy", "icons/achievements/chaos_redux/achievement_not_eligible.png"),

	# Technology references combine vanilla icons, current Chaos Redux technology
	# art, and the moved medium/small legacy examples.
	*[chaos_asset("Core gameplay icons", "Technology", "icons/technologies/chaos_redux", f"gfx/interface/technologies/{name}.dds", name) for name in (
		"anthrax_bomb_equipment",
		"bio_surveillance_networks",
		"cbrn_biosecurity_assault_formation",
		"gas_mask",
		"mustard_gas_tech",
		"portable_anemometer",
		"sarin_gas_tech",
	)],
	moved_asset("Core gameplay icons", "Technology, legacy medium", "icons/technologies/legacy/medium/1.png"),
	moved_asset("Core gameplay icons", "Technology, legacy medium", "icons/technologies/legacy/medium/2.png"),
	moved_asset("Core gameplay icons", "Technology, legacy medium", "icons/technologies/legacy/medium/3.png"),
	moved_asset("Core gameplay icons", "Technology, legacy small", "icons/technologies/legacy/small/1.png"),
	moved_asset("Core gameplay icons", "Technology, legacy small", "icons/technologies/legacy/small/2.png"),
	moved_asset("Core gameplay icons", "Technology, legacy small", "icons/technologies/legacy/small/3.png"),

	# Equipment and unit visual pipelines.
	vanilla_asset("Unit visual pipelines", "2D equipment technology art", "units/equipment/technology_art", "gfx/interface/technologies/artillery1.dds", "artillery1"),
	vanilla_asset("Unit visual pipelines", "2D equipment technology art", "units/equipment/technology_art", "gfx/interface/technologies/anti_tank_equipment.dds", "anti_tank_equipment"),
	*[vanilla_asset("Unit visual pipelines", "Land division counter, 2 frames", "units/land/counters_large", f"gfx/interface/counters/divisions_large/{name}.dds", name) for name in ("unit_amphibious_mechanized_icon", "unit_amphibious_tank_icon", "unit_anti_air_icon")],
	*[vanilla_asset("Unit visual pipelines", "Land map counter, 2 frames", "units/land/map_counters", f"gfx/interface/counters/divisions_small/{name}.dds", name.removeprefix("onmap_unit_").removesuffix("_icon")) for name in ("onmap_unit_amphibious_mechanized_icon", "onmap_unit_amphibious_tank_icon", "onmap_unit_anti_air_icon")],
	*[vanilla_asset("Unit visual pipelines", "Division-template emblem", "units/land/division_template_emblems", f"gfx/interface/counters/division_templates_large/{name}.dds", name) for name in ("custom_template_002", "custom_template_003", "custom_template_004")],
	vanilla_asset("Unit visual pipelines", "Air map counter", "units/air/map_counters", "gfx/interface/counters/air_small/onmap_cas.dds", "onmap_cas"),
	vanilla_asset("Unit visual pipelines", "Air map counter", "units/air/map_counters", "gfx/interface/counters/air_small/onmap_heavy_fighter.dds", "onmap_heavy_fighter"),
	vanilla_asset("Unit visual pipelines", "Naval map counter", "units/naval/map_counters", "gfx/interface/counters/ships_small/onmap_battlecruiser.dds", "onmap_battlecruiser"),
	vanilla_asset("Unit visual pipelines", "Naval map counter", "units/naval/map_counters", "gfx/interface/counters/ships_small/onmap_battleship.dds", "onmap_battleship"),
	vanilla_asset("Unit visual pipelines", "3D land model diffuse material", "units/models_3d/land_materials", "gfx/models/units/asian_infantry_diffuse.dds", "asian_infantry_diffuse"),
	vanilla_asset("Unit visual pipelines", "3D land model diffuse material", "units/models_3d/land_materials", "gfx/models/units/cavalry_horse_diffuse.dds", "cavalry_horse_diffuse"),
	vanilla_asset("Unit visual pipelines", "3D land model diffuse material", "units/models_3d/land_materials", "gfx/models/units/ENG_infantry_diffuse.dds", "eng_infantry_diffuse"),
	*[vanilla_asset("Unit visual pipelines", "3D air model diffuse material", "units/models_3d/air_materials", f"gfx/models/units/planes/{name}.dds", name) for name in ("generic_plane_heavy_diffuse", "generic_plane_medium_diffuse", "generic_jet_plane_diffuse", "generic_guided_missile_diffuse")],
	*[vanilla_asset("Unit visual pipelines", "3D naval model diffuse material", "units/models_3d/naval_materials", f"gfx/models/units/ships/{name}.dds", name) for name in ("generic_battleship_diffuse", "generic_carrier_diffuse", "generic_light_cruiser_diffuse", "generic_heavy_cruiser_diffuse")],
]


REFERENCES = BASE_REFERENCES + tuple(EXTRA_REFERENCES)


MINIMUMS = {
	"icons/national_focus": 15,
	"icons/ideas": 15,
	"icons/decisions": 15,
	"icons/decision_categories": 15,
	"icons/technologies": 15,
	"icons/achievements": 15,
	"icons/missions": 5,
	"icons/officer_corps_spirits": 5,
	"icons/special_projects": 5,
	"icons/balance_of_power": 5,
	"icons/intelligence_agency": 5,
	"icons/intelligence_operations": 5,
	"icons/commander_traits": 5,
	"icons/medals": 5,
	"icons/military_raids": 5,
	"icons/state_modifiers": 5,
	"icons/military_industrial_organizations": 5,
	"icons/factions": 5,
	"icons/buildings": 5,
	"icons/modifiers": 5,
	"event_art/report": 5,
	"event_art/news": 5,
	"event_art/super_event": 5,
	"flags": 5,
}


def checker(size: tuple[int, int], tile: int = 10) -> Image.Image:
	background = Image.new("RGBA", size, (96, 98, 100, 255))
	draw = ImageDraw.Draw(background)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if (x // tile + y // tile) % 2:
				draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(135, 137, 139, 255))
	return background


def extract_reference(game_root: Path, repo_root: Path, output_root: Path, entry: Reference) -> tuple[int, int]:
	source = source_file(game_root, repo_root, entry)
	if not source.is_file():
		raise FileNotFoundError(f"Missing {source_label(entry).lower()} reference: {source}")
	output = output_root / entry.review_path
	output.parent.mkdir(parents=True, exist_ok=True)
	if source.resolve() == output.resolve():
		with Image.open(output) as image:
			return image.size
	with Image.open(source) as image:
		review = image.convert("RGBA")
		review.save(output)
		return review.size


def validate_reference(game_root: Path, repo_root: Path, output_root: Path, entry: Reference) -> tuple[int, int]:
	source = source_file(game_root, repo_root, entry)
	output = output_root / entry.review_path
	if not source.is_file() or not output.is_file():
		raise FileNotFoundError(f"Missing source or review for {entry.review_path}")
	if source.resolve() == output.resolve():
		with Image.open(output) as review_image:
			return review_image.size
	with Image.open(source) as source_image, Image.open(output) as review_image:
		if source_image.size != review_image.size:
			raise ValueError(
				f"Canvas mismatch for {entry.review_path}: "
				f"source={source_image.size}, review={review_image.size}"
			)
		if source_image.convert("RGBA").tobytes() != review_image.convert("RGBA").tobytes():
			raise ValueError(f"Decoded pixels differ from {source_label(entry).lower()} source: {entry.review_path}")
		return review_image.size


def sheet_key(entry: Reference) -> str:
	parts = Path(entry.review_path).as_posix().split("/")
	if parts[0] == "flags":
		return "flags"
	if parts[0] in {"icons", "event_art", "portraits"}:
		return "/".join(parts[:2])
	if parts[0] == "units":
		return "/".join(parts[:-1])
	return "/".join(parts[:-1]) or "misc"


def sheet_title(key: str, entries: list[Reference]) -> str:
	if key == "flags":
		label = "Flags — normal, medium, and small ladders"
	else:
		label = key.replace("_", " ").replace("/", " / ").title()
	return f"{label} — {len(entries)} references"


def contact_sheet_path(output_root: Path, key: str) -> Path:
	return output_root.joinpath(*key.split("/"), "contact_sheet.png")


def grouped_references() -> dict[str, list[Reference]]:
	groups: dict[str, list[Reference]] = defaultdict(list)
	for entry in REFERENCES:
		groups[sheet_key(entry)].append(entry)
	for entries in groups.values():
		entries.sort(key=lambda entry: entry.review_path)
	return dict(sorted(groups.items()))


def make_contact_sheet(output_root: Path, key: str, entries: list[Reference]) -> None:
	columns = 5 if len(entries) >= 15 else 4
	cell_width = 300
	cell_height = 220
	header_height = 58
	preview_size = (260, 140)
	rows = (len(entries) + columns - 1) // columns
	sheet = Image.new(
		"RGBA",
		(columns * cell_width, rows * cell_height + header_height),
		(28, 30, 32, 255),
	)
	draw = ImageDraw.Draw(sheet)
	draw.text((18, 18), sheet_title(key, entries), fill=(244, 242, 232, 255))
	for index, entry in enumerate(entries):
		with Image.open(output_root / entry.review_path) as image:
			review = image.convert("RGBA")
		scale = min(preview_size[0] / review.width, preview_size[1] / review.height)
		if review.width >= 80 or review.height >= 80:
			scale = min(scale, 1.0)
		else:
			scale = min(scale, 4.0)
		preview_dimensions = (
			max(1, round(review.width * scale)),
			max(1, round(review.height * scale)),
		)
		resample = Image.Resampling.NEAREST if scale >= 1 else Image.Resampling.LANCZOS
		preview = ImageOps.contain(review, preview_dimensions, method=resample)
		base = checker(preview_size)
		x_offset = (preview_size[0] - preview.width) // 2
		y_offset = (preview_size[1] - preview.height) // 2
		base.alpha_composite(preview, (x_offset, y_offset))
		column = index % columns
		row = index // columns
		x = column * cell_width + 20
		y = row * cell_height + header_height
		sheet.alpha_composite(base, (x, y))
		label_path = Path(entry.review_path)
		if key == "flags":
			label_path = label_path.relative_to("flags")
		label = f"{label_path.as_posix()}\n{review.width}x{review.height}"
		draw.multiline_text((x, y + preview_size[1] + 8), label, fill=(224, 224, 220, 255), spacing=2)
	output = contact_sheet_path(output_root, key)
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output)


def source_file(game_root: Path, repo_root: Path, entry: Reference) -> Path:
	if entry.source_root == "vanilla":
		return game_root / entry.source_path
	if entry.source_root in {"chaos_redux", "moved_review"}:
		return repo_root / entry.source_path
	raise ValueError(f"Unknown source root {entry.source_root!r} for {entry.review_path}")


def source_label(entry: Reference) -> str:
	return {
		"vanilla": "Vanilla HOI4",
		"chaos_redux": "Chaos Redux source",
		"moved_review": "Moved legacy review copy",
	}[entry.source_root]


def validate_minimums(groups: dict[str, list[Reference]]) -> None:
	requirements = {key: 5 for key in groups}
	requirements.update(MINIMUMS)
	missing = [
		f"{key}: {len(groups.get(key, []))}/{minimum}"
		for key, minimum in requirements.items()
		if len(groups.get(key, [])) < minimum
	]
	if missing:
		raise ValueError("Reference coverage below minimum: " + "; ".join(missing))


def write_catalog(output_root: Path, dimensions: dict[str, tuple[int, int]], groups: dict[str, list[Reference]]) -> None:
	lines = [
		"# Canonical asset-reference catalog",
		"",
		"Generated by `.tools/extract_hoi4_asset_references.py`. Review PNGs are organized by semantic asset type.",
		"Vanilla entries are lossless review copies from the installed HOI4 directory; Chaos Redux entries",
		"are explicitly marked so project-specific visual language is available without being mistaken for vanilla art.",
		"Every type has a local `contact_sheet.png`; common icon families target 15 examples and other tracked",
		"families target at least 5. Contact sheets are not counted as reference examples.",
		"",
		"## Coverage",
		"",
		"| Asset type | References | Minimum | Contact sheet |",
		"| --- | ---: | ---: | --- |",
	]
	for key, entries in groups.items():
		minimum = MINIMUMS.get(key, 5)
		lines.append(f"| `{key}` | {len(entries)} | {minimum} | `{key}/contact_sheet.png` |")
	lines.append("")
	by_section: dict[str, list[Reference]] = defaultdict(list)
	for entry in REFERENCES:
		by_section[entry.section].append(entry)
	for section, entries in by_section.items():
		entries.sort(key=lambda entry: entry.review_path)
		lines.extend((f"## {section}", "", "| Category | Review PNG | Size | Source kind | Source path | Contact sheet | Related definition |", "| --- | --- | ---: | --- | --- | --- | --- |"))
		for entry in entries:
			width, height = dimensions[entry.review_path]
			key = sheet_key(entry)
			related = f"`{entry.related_definition}`" if entry.related_definition else "—"
			lines.append(
				f"| {entry.category} | `{entry.review_path}` | {width}x{height} | {source_label(entry)} | "
				f"`{entry.source_path}` | `{key}/contact_sheet.png` | {related} |"
			)
		lines.append("")
	(output_root / "CATALOG.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		"--game-root",
		type=Path,
		default=Path(r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV"),
	)
	parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
	parser.add_argument("--check", action="store_true", help="Validate existing review files without rewriting them")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	output_root = args.repo_root / REFERENCE_ROOT
	groups = grouped_references()
	validate_minimums(groups)
	dimensions: dict[str, tuple[int, int]] = {}
	for entry in REFERENCES:
		if args.check:
			dimensions[entry.review_path] = validate_reference(args.game_root, args.repo_root, output_root, entry)
		else:
			dimensions[entry.review_path] = extract_reference(args.game_root, args.repo_root, output_root, entry)
	if not args.check:
		legacy_contact_sheets = output_root / "contact_sheets"
		if legacy_contact_sheets.is_dir():
			shutil.rmtree(legacy_contact_sheets)
		for key, entries in groups.items():
			make_contact_sheet(output_root, key, entries)
		write_catalog(output_root, dimensions, groups)
	else:
		missing_sheets = [
			str(contact_sheet_path(output_root, key))
			for key in groups
			if not contact_sheet_path(output_root, key).is_file()
		]
		if (output_root / "contact_sheets").exists():
			missing_sheets.append(str(output_root / "contact_sheets") + " (broad legacy directory)")
		if missing_sheets:
			raise FileNotFoundError("Missing per-type contact sheets: " + "; ".join(missing_sheets))
	print(f"validated {len(REFERENCES)} references across {len(groups)} per-type contact sheets")


if __name__ == "__main__":
	main()
