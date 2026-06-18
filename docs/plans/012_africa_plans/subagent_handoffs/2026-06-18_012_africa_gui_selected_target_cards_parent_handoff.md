# Event 012 Africa - Continental Congress Selected Target Cards Handoff

## Parent tranche

The Continental Congress scripted GUI now presents selected target state that was previously only visible through decision-category text or individual decisions.

## Files changed

- `interface/012_africa_scripted_gui.gui`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`

## Gameplay/UI surface

- Added dossier target, current operation, and warning docket text cards to `africa_continental_congress_container`.
- Kept all cards read-only; no new decision effects, costs, or route locks were introduced.
- Moved active dossier and active Bestiary case presentation out of the crowded value block into target cards.
- Exposed:
  - selected historical dossier, seat, and dossier profile;
  - selected dossier survey status;
  - Archive guard mission status;
  - regional integration operation status;
  - liberation objective status;
  - return settlement status;
  - Bestiary state operation status;
  - Bestiary warning status and counts;
  - dossier resistance watch status.

## New scripted localisation

- `GetAfricaSelectedDossierSurveyStatus`
- `GetAfricaArchiveGuardMissionStatus`
- `GetAfricaBestiaryWarningStatus`

## Remaining risk

- This improves selected-target readability but does not implement full scrollable region, member, or dossier card lists, nor per-target GUI selection inside the panel.
- No live HOI4 screenshot validation was available in this tranche.
