# White Peace Event Catalog Workbook Handoff

## Workbook changed

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Sheets and rows updated

- Sheet: `Main Sheet`
- Event row updated: `10`
- Cluster row added/filled: `16`

## Fields updated

- Event `009` / White Peace
- `B10` Event Name: `White Peace`
- `C10` Details
- `D10` Evo I
- `E10` Evo II
- `F10` Evo III
- `K10` Cluster ID: `4`
- `L10` Member Severity: `Low`
- `M10` Status: `Implemented`

- Peace cluster row
- `O16` Cluster ID: `4`
- `P16` Cluster Name: `Peace`
- `Q16` Details
- `R16` Members (ID): `9`
- `S16` Type: `Minor Repeatable`
- `T16` Chaos level: `1`
- `U16` Status: `Implemented`

## Exact wording summary

- Event detail mirrors the in-game Event Details wording:
  `White Peace searches for wars that can end without conquest, indemnity, or scripted-story damage...`
- Evolution detail mirrors the in-game evolution wording and titles:
  `Repeated Minor Settlements`
  `Major-Country Settlement`
  `Broad Diplomatic Settlement`
- Cluster detail mirrors the in-game Peace cluster description:
  `Peace incidents reduce conflict through settlements, ceasefires, exhaustion, negotiations, and other de-escalation shocks...`

## Validation performed

- Read and aligned against:
  - `docs/specs/009_white_peace_specs/specs/009_white_peace_event_text_log_cluster.md`
  - `docs/specs/009_white_peace_specs/specs/009_white_peace_spec.md`
  - `docs/events/009_white_peace/overview.md`
  - `localisation/english/009_white_peace_l_english.yml`
  - `localisation/english/chaosx_gui_l_english.yml`
- Reopened the workbook after saving and verified the edited cells contained the intended values.
- Confirmed workbook sheet structure remained:
  - `Main Sheet`
  - `Info`
  - `Legend`

## Parent follow-up

- Parent resolved the Peace cluster review marker after checking `common/script_constants/event_cluster_constants.txt`: `event_cluster_peace.unlock_tier = 0`, and existing workbook convention represents unlock-tier `0` clusters as Chaos level `1`.
- Parent updated `T16` to `1` and `U16` to `Implemented`.
- Parent performed a final alignment pass after localisation audit patches and updated `C10`, `D10`, `E10`, `F10`, and `Q16` to mirror the final in-game localisation wording.

## Remaining risks and blockers

- No gameplay validation was performed or claimed.
