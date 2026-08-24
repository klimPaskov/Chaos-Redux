"""Static source audit for the Event 006 Statehood Ledger semantic matrix.

This audit does not launch Hearts of Iron IV and does not claim a runtime GUI
render. It verifies that the source surfaces expose the complete tab, state
selector, cleanup, and static/animated sibling contract documented by the
Event 006 GUI handoff.
"""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
EFFECTS = ROOT / "common" / "scripted_effects" / "006_independence_wave_effects.txt"
SCRIPTED_GUI = ROOT / "common" / "scripted_guis" / "006_independence_wave_scripted_gui.txt"
WINDOW = ROOT / "interface" / "006_independence_wave.gui"
SPRITES = ROOT / "interface" / "006_independence_wave.gfx"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def block(source: str, name: str) -> str:
    match = re.search(rf"(?m)^\s*{re.escape(name)}\s*=\s*\{{", source)
    require(match is not None, f"missing block: {name}")
    opening = source.find("{", match.start())
    depth = 0
    for index in range(opening, len(source)):
        character = source[index]
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return source[opening + 1 : index]
    raise AssertionError(f"unclosed block: {name}")


def main() -> int:
    effects = EFFECTS.read_text(encoding="utf-8-sig")
    scripted_gui = SCRIPTED_GUI.read_text(encoding="utf-8-sig")
    window = WINDOW.read_text(encoding="utf-8-sig")
    sprites = SPRITES.read_text(encoding="utf-8-sig")

    selector = block(effects, "independence_wave_refresh_status_frame_state")
    reset = block(effects, "independence_wave_reset_current_generation")

    recognition_frames = (
        "recognition_unrecognized",
        "recognition_observed",
        "recognition_de_facto",
        "recognition_treaty_backed",
        "recognition_entrenched",
    )
    dependency_frames = ("dependency_calm", "dependency_watch", "dependency_danger")
    league_frames = ("league_rest", "league_drafting", "league_vote", "league_activated")
    formable_frames = (
        "formable_hidden",
        "formable_discovered",
        "formable_eligible",
        "formable_proclaimed",
    )
    for frame in recognition_frames + dependency_frames + league_frames + formable_frames:
        require(f"independence_wave_gui_frame.{frame}" in selector, f"selector missing frame: {frame}")

    require("independence_wave_recognition_band.observed" in selector, "recognition threshold missing")
    require("independence_wave_recognition_band.de_facto" in selector, "de facto threshold missing")
    require("independence_wave_recognition_band.treaty_backed" in selector, "treaty threshold missing")
    require("independence_wave_recognition_band.internationally_entrenched" in selector, "entrenched threshold missing")
    require("has_independence_wave_patron_warning = yes" in selector, "patron warning branch missing")
    require("has_independence_wave_severe_instability = yes" in selector, "instability branch missing")
    require("independence_wave_league_phase.regional_conferences" in selector, "regional league group missing")
    require("independence_wave_league_phase.congress_preparation" in selector, "congress preparation group missing")
    require("independence_wave_league_phase.charter_vote" in selector, "charter vote group missing")
    for phase in (
        "consultative_league",
        "formal_league",
        "durable_league",
        "league_crisis",
        "reformed_league",
        "rival_leagues",
    ):
        require(f"independence_wave_league_phase.{phase}" in selector, f"activated league group missing: {phase}")
    require("has_country_flag = independence_wave_formable_discovered" in selector, "formable discovery branch missing")
    require("has_country_flag = independence_wave_formable_all_required_initial_integration_complete" in selector, "formable eligibility branch missing")
    require("independence_wave_formable_transaction.committed" in selector, "formable committed branch missing")

    tab_names = ("government", "recognition", "security", "league", "ambitions")
    tab_blocks = {}
    for tab in tab_names:
        name = f"independence_wave_status_tab_{tab}_click"
        body = block(scripted_gui, name)
        tab_blocks[tab] = body
        require(f"set_country_flag = independence_wave_status_tab_{tab}" in body, f"tab does not set itself: {tab}")
        for other in tab_names:
            if other != tab:
                require(f"clr_country_flag = independence_wave_status_tab_{other}" in body, f"tab does not clear {other}: {tab}")

    for panel in tab_names:
        require(
            f"independence_wave_status_{'government' if panel == 'government' else panel}_panel_visible"
            in scripted_gui,
            f"panel visibility missing: {panel}",
        )
    require("independence_wave_status_government_panel_visible" in scripted_gui, "default government panel missing")

    for variable in (
        "independence_wave_gui_recognition_frame",
        "independence_wave_gui_dependency_frame",
        "independence_wave_gui_league_frame",
        "independence_wave_gui_formable_frame",
    ):
        require(f"clear_variable = {variable}" in reset, f"generation cleanup missing: {variable}")
    require("clr_country_flag = independence_wave_status_gui_show_animation" in reset, "animation cleanup missing")

    for name in (
        "independence_wave_status_recognition_seal_visible",
        "independence_wave_status_dependency_warning_visible",
        "independence_wave_status_league_charter_visible",
        "independence_wave_status_formable_seal_visible",
        "independence_wave_status_recognition_seal_animated_visible",
        "independence_wave_status_dependency_warning_animated_visible",
        "independence_wave_status_league_charter_animated_visible",
        "independence_wave_status_formable_seal_animated_visible",
    ):
        require(name in scripted_gui, f"animation/static visibility surface missing: {name}")
    for property_name in (
        "independence_wave_status_recognition_seal",
        "independence_wave_status_dependency_warning",
        "independence_wave_status_league_charter",
        "independence_wave_status_formable_seal",
    ):
        require(f"{property_name} = {{ frame = ROOT." in scripted_gui, f"frame property missing: {property_name}")

    require("name = \"independence_wave_status_window\"" in window, "Statehood Ledger window missing")
    require("width = 700 height = 500" in window, "Statehood Ledger size contract missing")
    for sprite in (
        "GFX_independence_wave_recognition_seal_states",
        "GFX_independence_wave_dependency_warning_states",
        "GFX_independence_wave_league_charter_activation_states",
        "GFX_independence_wave_formable_eligibility_seal_states",
        "GFX_independence_wave_recognition_seal_animated",
        "GFX_independence_wave_dependency_warning_animated",
        "GFX_independence_wave_league_charter_activation_animated",
        "GFX_independence_wave_formable_eligibility_seal_animated",
    ):
        require(sprite in sprites, f"registered GUI sprite missing: {sprite}")

    print("Event 006 Statehood Ledger semantic source matrix passed")
    print("- tabs: 5 mutually exclusive click contracts")
    print("- recognition frames: 5; dependency frames: 3; league frames: 4; formable frames: 4")
    print("- cleanup: four frame variables plus animation flag")
    print("- static/animated sibling surfaces: 4 pairs")
    print("- runtime rendering and save/load evidence: not claimed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, OSError) as error:
        print(f"GUI semantic source matrix failed: {error}", file=sys.stderr)
        raise SystemExit(1)
