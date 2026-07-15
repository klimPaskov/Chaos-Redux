#!/usr/bin/env python3
"""Build the allowlisted vanilla visual-reference library used by asset agents.

The review PNGs under ``chaos-redux-event-assets/assets/vanilla_reference``
are never runtime mod assets.  This script preserves each source canvas,
records exact provenance, and creates contact sheets without normalising or
repainting the source art.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


@dataclass(frozen=True)
class Reference:
	section: str
	category: str
	review_path: str
	source_path: str
	related_definition: str = ""
	sheet: str = ""


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
) -> Reference:
	return Reference(section, category, review_path, source_path, related_definition, sheet)


REFERENCES = (
	# Portraits and flat flag ladders.
	ref("Portraits and flags", "Leader portrait", "portraits/leaders/den_thorvald_stauning.png", "gfx/leaders/DEN/Portrait_Denmark_Thorvald_Stauning.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Leader portrait", "portraits/leaders/ire_eamon_de_valera.png", "gfx/leaders/IRE/Portrait_Ireland_Eamon_de_Valera.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Leader portrait", "portraits/leaders/fin_carl_mannerheim.png", "gfx/leaders/FIN/portrait_fin_carl_mannerheim.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Land commander portrait", "portraits/commanders/generic_africa_land_1.png", "gfx/leaders/Africa/Portrait_Africa_Generic_land_1.dds", "interface/_random_portraits.gfx", "portraits_and_flags"),
	ref("Portraits and flags", "Naval commander portrait", "portraits/commanders/generic_africa_navy_1.png", "gfx/leaders/Africa/Portrait_Africa_Generic_navy_1.dds", "interface/_random_portraits.gfx", "portraits_and_flags"),
	ref("Portraits and flags", "Operative portrait", "portraits/operatives/den_flemming_muus.png", "dlc/dlc028_la_resistance/gfx/leaders/DEN/portrait_DEN_flemming_muus.dds", "dlc/dlc028_la_resistance/interface/lar_portraits.gfx", "portraits_and_flags"),
	ref("Portraits and flags", "Operative portrait", "portraits/operatives/aus_erwin_von_lahousen.png", "dlc/dlc028_la_resistance/gfx/leaders/AUS/portrait_AUS_erwin_von_lahousen.dds", "dlc/dlc028_la_resistance/interface/lar_portraits.gfx", "portraits_and_flags"),
	ref("Portraits and flags", "Advisor dossier", "portraits/advisors/generic_europe_1.png", "gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Advisor dossier", "portraits/advisors/generic_female_europe.png", "gfx/interface/ideas/idea_generic_political_advisor_female_europe.dds", sheet="portraits_and_flags"),
	ref("Portraits and flags", "Advisor dossier", "portraits/advisors/generic_asia_1.png", "gfx/interface/ideas/idea_generic_political_advisor_asia_1.dds", sheet="portraits_and_flags"),
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


SHEET_TITLES = {
	"portraits_and_flags": "Portraits, dossiers, and flat flag ladders",
	"icons": "Core gameplay icon families",
	"icons_extended": "Extended gameplay icon families",
	"event_art": "Report and news event art",
	"units": "Equipment and land unit visual pipelines",
	"units_expanded": "Expanded land, air, and naval unit visuals",
}


def checker(size: tuple[int, int], tile: int = 10) -> Image.Image:
	background = Image.new("RGBA", size, (96, 98, 100, 255))
	draw = ImageDraw.Draw(background)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if (x // tile + y // tile) % 2:
				draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(135, 137, 139, 255))
	return background


def extract_reference(game_root: Path, output_root: Path, entry: Reference) -> tuple[int, int]:
	source = game_root / entry.source_path
	if not source.is_file():
		raise FileNotFoundError(f"Missing vanilla reference: {source}")
	output = output_root / entry.review_path
	output.parent.mkdir(parents=True, exist_ok=True)
	with Image.open(source) as image:
		review = image.convert("RGBA")
		review.save(output)
		return review.size


def validate_reference(game_root: Path, output_root: Path, entry: Reference) -> tuple[int, int]:
	source = game_root / entry.source_path
	output = output_root / entry.review_path
	if not source.is_file() or not output.is_file():
		raise FileNotFoundError(f"Missing source or review for {entry.review_path}")
	with Image.open(source) as source_image, Image.open(output) as review_image:
		if source_image.size != review_image.size:
			raise ValueError(
				f"Canvas mismatch for {entry.review_path}: "
				f"source={source_image.size}, review={review_image.size}"
			)
		if source_image.convert("RGBA").tobytes() != review_image.convert("RGBA").tobytes():
			raise ValueError(f"Decoded pixels differ from vanilla source: {entry.review_path}")
		return review_image.size


def make_contact_sheet(output_root: Path, sheet_name: str, entries: list[Reference]) -> None:
	columns = 4
	cell_width = 250
	cell_height = 190
	rows = (len(entries) + columns - 1) // columns
	sheet = Image.new("RGBA", (columns * cell_width, rows * cell_height + 44), (28, 30, 32, 255))
	draw = ImageDraw.Draw(sheet)
	draw.text((14, 14), SHEET_TITLES[sheet_name], fill=(244, 242, 232, 255))
	for index, entry in enumerate(entries):
		with Image.open(output_root / entry.review_path) as image:
			review = image.convert("RGBA")
		max_size = (210, 125)
		scale = min(max_size[0] / review.width, max_size[1] / review.height)
		if review.width < 70 and review.height < 70:
			scale = min(scale, 4.0)
		else:
			scale = min(scale, 1.0)
		preview_size = (max(1, round(review.width * scale)), max(1, round(review.height * scale)))
		resample = Image.Resampling.NEAREST if scale > 1 else Image.Resampling.LANCZOS
		preview = review.resize(preview_size, resample)
		base = checker(max_size)
		x_offset = (max_size[0] - preview.width) // 2
		y_offset = (max_size[1] - preview.height) // 2
		base.alpha_composite(preview, (x_offset, y_offset))
		column = index % columns
		row = index // columns
		x = column * cell_width + 18
		y = row * cell_height + 44
		sheet.alpha_composite(base, (x, y))
		label = f"{entry.category}\n{Path(entry.review_path).name}"
		draw.multiline_text((x, y + max_size[1] + 8), label, fill=(224, 224, 220, 255), spacing=2)
	output = output_root / "contact_sheets" / f"{sheet_name}.png"
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output)


def write_catalog(output_root: Path, dimensions: dict[str, tuple[int, int]]) -> None:
	lines = [
		"# Vanilla reference catalog",
		"",
		"Generated by `.tools/extract_hoi4_asset_references.py`. All source paths are relative to",
		"`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.",
		"Dimensions are the decoded source canvas and match the lossless PNG review copy.",
		"",
	]
	by_section: dict[str, list[Reference]] = defaultdict(list)
	for entry in REFERENCES:
		by_section[entry.section].append(entry)
	for section, entries in by_section.items():
		lines.extend((f"## {section}", "", "| Category | Review PNG | Size | Vanilla source | Related definition |", "| --- | --- | ---: | --- | --- |"))
		for entry in entries:
			width, height = dimensions[entry.review_path]
			related = f"`{entry.related_definition}`" if entry.related_definition else "—"
			lines.append(
				f"| {entry.category} | `{entry.review_path}` | {width}x{height} | "
				f"`{entry.source_path}` | {related} |"
			)
		lines.append("")
	(output_root / "CATALOG.md").write_text("\n".join(lines), encoding="utf-8")


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
	dimensions: dict[str, tuple[int, int]] = {}
	for entry in REFERENCES:
		if args.check:
			dimensions[entry.review_path] = validate_reference(args.game_root, output_root, entry)
		else:
			dimensions[entry.review_path] = extract_reference(args.game_root, output_root, entry)
	if not args.check:
		for sheet_name in SHEET_TITLES:
			make_contact_sheet(output_root, sheet_name, [entry for entry in REFERENCES if entry.sheet == sheet_name])
		write_catalog(output_root, dimensions)
	print(f"validated {len(REFERENCES)} allowlisted references across {len(SHEET_TITLES)} contact sheets")


if __name__ == "__main__":
	main()
