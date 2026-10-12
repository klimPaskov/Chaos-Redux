# Disease Containment Board

Disposition: rejected by the owner on 12 October 2026 and unhooked under A12. The GUI files remain on disk; the layout and registry notes below describe the historical board. The active response flow is documented in [the restoration comparison](../../../plans/biowarfare_restore_comparison_2026-10-12.md).

The board is one information view of the country's outbreak situation.
It has no per-disease selector, tabs or filters.
Disease-specific measures are decisions in the Biological Outbreak Response category, state-targeted where they act on one state.

## Layout

Top to bottom: title with Refresh and Close, the overall status line (outbreak status, affected states, critical states), national readiness (Preparedness and Medical capacity), then the affected-state list with the selected state's report beside it.
The list is ordered worst first: dangerous Black Plague states, ordinary outbreaks, then Black Plague states that are threatened, contained or recovering.
Each entry names the state and the outbreak it carries as data, with its status.
The state report shows owner and controller, the outbreak, its detailed records where they exist, the Black Plague response target when one is set, and Go to State.
The category header shows the outbreak status and the number of affected states, with an Open Board button.

## Which states are listed

- Black Plague states from `global.black_plague_active_states` that are tracked and visible to the player.
- States the country owns, controls or borders that carry an ordinary disease (`<key>_contaminated_state` dynamic modifier).

Each listed state records its outbreak in the state variable `disease_containment_board_state_disease` (a `disease_containment_agent` id), read by `GetDiseaseContainmentStateOutbreakName`.

## Registry

Ordinary diseases are the contiguous ids `ordinary_first` to `ordinary_last` in `disease_containment_agent`.
Adding an ordinary disease:

1. Add its id and move `ordinary_last`.
2. Add a name key `disease_containment_agent_<name>` and a modifier-key line `disease_containment_modifier_key_<name>`.
3. Add one line each to `GetDiseaseContainmentModifierKey` and `GetDiseaseContainmentStateOutbreakName`.

The new disease is then scanned and listed with no other change.

## Scans

Opening or refreshing the board runs one state scan per ordinary disease id and stores the result in `disease_containment_board_ordinary_entries`.
Black Plague driven rebuilds of an open board reuse that stored result and never rescan.
No recurring on action runs the scan.

## Response target

Clicking a state only inspects it.
The Black Plague response state used by its local decisions is chosen with the state-targeted decision Select Black Plague Response State, and the board shows it as information.
That decision is visible once a Black Plague outbreak is identified (`disease_containment_board_knows_black_plague`).

## Icons

No new art. Existing sprites: `GFX_decision_bio_expand_biosecurity_capacity`, `GFX_decision_bio_expand_medical_capacity`, `GFX_black_plague_crisis_seal_static` and `_animated`, `GFX_chaosx_button_123x34`, `GFX_tiled_window`, `GFX_tiled_window_transparent`, all registered in existing `.gfx` files.

## Future plans

An ordinary-disease state registry would remove the observable-state scan.
The Black Plague local response decisions could become individually state-targeted instead of using the designated response state.
