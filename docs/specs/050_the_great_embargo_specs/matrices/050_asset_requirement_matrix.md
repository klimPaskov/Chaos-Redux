# Event 050 asset requirement matrix

| Asset ID | Type | Target size | Source mode | Visual role | Runtime consumer | Animation |
| --- | --- | --- | --- | --- | --- | --- |
| `report_opening_isolation` | Report image | `210x176` | Generated period documentary scene | Halted shipments and immediate isolation | Target opening report | Static |
| `report_secondary_sanctions` | Report image | `210x176` | Generated period documentary scene | Neutral cargo inspection and intermediary pressure | Evolution I report | Static |
| `report_fragmented_trade` | Report image | `210x176` | Generated period documentary scene | Overlapping routes and economic fragmentation | Evolution II reports | Static |
| `category_great_embargo` | Decision category picture | Consumer-verified, reference family near `114x101` | Generated full-canvas period scene | Identity and atmosphere | Event 50 decision category | Static |
| `icon_category_great_embargo` | Category icon | `32x32` | Generated native-transparent icon | Open category | Decision category | Static |
| `icon_self_sufficiency` | Decision icon | `32x32` | Generated native-transparent icon | Domestic adaptation | Decision | Static |
| `icon_smuggling_networks` | Decision icon | `32x32` | Generated native-transparent icon | Covert trade | Decision | Static |
| `icon_neutral_intermediaries` | Decision icon | `32x32` | Generated native-transparent icon | Neutral commercial route | Decision | Static |
| `icon_diplomatic_concessions` | Decision icon | `32x32` | Generated native-transparent icon | Negotiated lifting | Decision | Static |
| `icon_defy_the_world` | Decision icon | `32x32` | Generated native-transparent icon | Siege economy | Decision | Static |
| `icon_resource_seizure` | Decision icon | `32x32` | Generated native-transparent icon | Military resource access | Decision | Static |
| `icon_secure_replacement_supply` | Mission icon | `32x32` | Generated native-transparent icon | Timed supply objective | Mission | Static |
| `idea_great_embargo` | National spirit icon | `64x64` | Generated native-transparent icon | Active isolation state | Target crisis spirit or equivalent | Static |
| `achievement_050_01` to `achievement_050_05` | Achievement triplets | `64x64` | Generated completed art, processed variants | Mastery rewards | Achievement registry | Static |

## Reference gates

The asset worker must inspect the exact canonical reference families before production:

- `event_art/report/`
- `icons/decision_categories/`
- `icons/decision_categories/pictures/`
- `icons/decisions/`
- `icons/missions/`
- `icons/ideas/`
- `icons/achievements/`

The decision category picture family must contain its labelled `contact_sheet.png`. If it is missing, the asset worker creates it and updates the reference README and catalog before creating Event 50 art.

## Processing gates

- Full-canvas scene art keeps the required opaque documentary treatment.
- Alpha-backed icons request native transparency in the initial generation.
- Each icon family has its own source art and cannot be satisfied by resizing another icon type.
- Final runtime assets move to event-scoped engine folders.
- Temporary evidence under `docs/assets/050_the_great_embargo/` remains while implementation is active or blocked, then its durable facts are promoted before deletion at verified completion.
