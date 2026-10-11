# Disease Containment Board

The shared board opens from the Disease Containment category header and lists only the diseases the country has identified.
A disease is identified when its outbreak is in a state the country owns or controls or in a state directly across its border, or when a Black Plague state is visible to the player.
Identified ids persist in the country array `disease_containment_known_diseases`.
A country with no identified disease sees an empty selector and the line "No outbreak has been identified."

## Layout

Top to bottom: the disease selector (a grid of one button per identified disease, scrollable), national readiness (Preparedness, Medical capacity, Outbreak status), the four list filters, the state list, and the selected state's report beside it.
The selected disease and the inspected state are picked out by colour, and the response target is marked in the state's detail line.
Go to State, Refresh and Close keep their original behaviour.

## Registry

Disease ids are `disease_containment_agent` constants.
Ordinary diseases are the contiguous range `ordinary_first` to `ordinary_last`.
Their contaminated state modifier must be named `<key>_contaminated_state`.
Black Plague is the one registry-backed disease and is discovered from `global.black_plague_active_states`.

Adding an ordinary disease:

1. Add its id to `disease_containment_agent` and move `ordinary_last`.
2. Add a name key `disease_containment_agent_<name>` and a modifier-key line `disease_containment_modifier_key_<name>` in the board localisation.
3. Add one line each to `GetDiseaseContainmentModifierKey`, `GetDiseaseContainmentEntryName` and `GetDiseaseContainmentSelectedDiseaseName`.

Discovery and the state list then include the new disease with no other change.

## Scans

Opening or refreshing the board runs one state scan per ordinary disease id (`disease_containment_board_discover_ordinary_diseases`).
Selecting a disease or changing a filter rebuilds only the state list.
No recurring on action calls these scans.
