# Event 006 Americas packages

Agent decision D32 admits six Americas rows through the regional framework engine (`regional_framework_packages.md`), beside California (IW-184), admitted earlier. The remaining rows stay blocked for the reasons below.

## Admitted rows

| Row | Tag | Anchor | Depth | Leadership | Government routes | Power centres |
| --- | --- | --- | --- | --- | --- | --- |
| IW-180 Quebec | QUE | 468 | Level 2 | Vanilla QUE has no characters; the game appoints the leader of its opening government. | constitutional, popular council, traditional, emergency, patron client | traditional authority and assembly |
| IW-182 Newfoundland | GZX (X-tag) | 331 | Level 2 | Institutional government: the restored Newfoundland House of Assembly, suspended in 1934, chaired by the leader the game appoints. | constitutional, popular council, traditional, patron client | domestic cabinet and foreign patron |
| IW-185 Texas | HCX (X-tag) | 375 | Level 2 | Institutional government: the Texas Legislature, chaired by the leader the game appoints. | constitutional, popular council, traditional, emergency, patron client | central government and provinces |
| IW-192 Yucatan | YUC | 474 | Level 2 | Vanilla YUC has no characters; the game appoints the leader of its opening government. | constitutional, popular council, traditional, emergency, patron client | labour councils and ministries |
| IW-200 Guarani state | GAR | 688 | Level 1 | Vanilla roster: the Guarani Council, the institutional leader of vanilla GAR. | constitutional, traditional, patron client | traditional authority and assembly |
| IW-203 Patagonian state | HUX (X-tag) | 512 | Level 1 | Institutional government: the Congress of the Patagonian Territories, chaired by the leader the game appoints. | constitutional, popular council, patron client | central government and provinces |

Radical sovereignty is excluded for all six. Quebec, Yucatan and the Guarani state are vanilla tags released by `release`. Newfoundland, Texas and the Patagonian state are created as dynamic countries from their reserved tags and open under a named institution chaired by the leader the game appoints: the Newfoundland House of Assembly (suspended in 1934 and restored by the release), the Texas Legislature and the Congress of the Patagonian Territories. Vanilla QUE and YUC have no characters, so the game appoints the leader of their opening governments; the Guarani state keeps the vanilla Guarani Council.

Two rows have two loader anchors. The Patagonian state binds its first anchor, 512 Patagonia. The Guarani state's first anchor, 301, holds Asuncion, which the planner protects as Paraguay's capital, so the row binds 688 Chaco Boreal and its runtime readiness also requires 301 to be unavailable; the loader then always chooses 688, and the release step gives Guarani the planned core it lacks there.

The Guarani and Patagonian states are Level 1 rows with no regional layer.

## Level 2 layers

### Quebec (IW-180)

- Starting problem: The Power Trusts (political power -5%, consumer goods +3%).
- Seat the Legislative Assembly (administration cost, 120 days): Adds The Legislative Assembly, raises Legitimacy and lowers Instability. Idea: The Legislative Assembly (stability +5%, political power +3%).
- Nationalise the Power Trusts (strategic cost, 180 days, after The Legislative Assembly has been seated): Replaces The Power Trusts with The Hydro Commission, raises Capacity and lowers Recognition. Idea: The Hydro Commission (production speed industrial complex +5%).
- Charter the Caisses Populaires (administration cost, 120 days): Adds The Caisses Populaires and raises Legitimacy and Capacity. Idea: The Caisses Populaires (stability +2%, consumer goods -2%).
- Incidents: The Abitibi Settlers (`chaosx.nr6.272`), Strike at Thetford Mines (`chaosx.nr6.273`).

### Newfoundland (IW-182)

- Starting problem: The Dominion Debt (stability -3%, political power -5%).
- Restore Responsible Government (administration cost, 120 days): Adds The House of Assembly, raises Legitimacy and lowers Instability. Idea: The House of Assembly (stability +5%, political power +3%).
- Settle the Bondholders (diplomatic cost, 180 days, after Responsible government has been restored): Removes The Dominion Debt, raises Recognition and lowers Capacity.
- Found the Fisheries Board (strategic cost, 180 days): Adds The Fisheries Board and raises Capacity. Idea: The Fisheries Board (trade opinion +10%, consumer goods -2%).
- Incidents: The Labrador Boundary (`chaosx.nr6.274`), The Merchants of Water Street (`chaosx.nr6.275`).

### Texas (IW-185)

- Starting problem: The Oil Glut (stability -3%, political power -5%).
- Seat the Legislature at Austin (administration cost, 120 days): Adds The Texas Legislature, raises Legitimacy and lowers Instability. Idea: The Texas Legislature (stability +5%, political power +3%).
- Empower the Railroad Commission (strategic cost, 180 days, after The Texas Legislature has been seated): Replaces The Oil Glut with The Proration Orders, raises Capacity and lowers Instability. Idea: The Proration Orders (fuel gain +10%).
- Muster the Ranger Companies (security cost, 120 days): Adds The Ranger Companies and raises Security. Idea: The Ranger Companies (army defence +5%, stability +2%).
- Incidents: The Hot Oil Runners (`chaosx.nr6.276`), The Border Bridges (`chaosx.nr6.277`).

### Yucatan (IW-192)

- Starting problem: The Henequen Haciendas (stability -5%, consumer goods +3%).
- Seat the Yucatan Congress (administration cost, 120 days): Adds The Yucatan Congress, raises Legitimacy and lowers Instability. Idea: The Yucatan Congress (stability +5%, political power +3%).
- Turn the Haciendas into Ejidos (strategic cost, 180 days, after The Yucatan Congress has been seated): Removes The Henequen Haciendas, greatly raises Legitimacy, lowers Capacity and raises Instability.
- Open the Port of Progreso (diplomatic cost, 120 days): Adds The Port of Progreso and raises Capacity and Recognition. Idea: The Port of Progreso (trade opinion +10%, consumer goods -2%).
- Incidents: The Leagues of Resistance (`chaosx.nr6.278`), The Price of Twine (`chaosx.nr6.279`).

## Blocked rows

- IW-181 Acadia (GYX), IW-186 Cherokee state (HDX), IW-188 Lakota state (HFX), IW-189 Dine state (HGX) and IW-194 Miskito state (MIS): no planner gate, loader or reservation, because each needs a distinct map state.
- IW-183 Cascadia (HAX): formable or route only, with a cross-border reservation and no route consumer.
- IW-187 Haudenosaunee Confederacy (HEX), IW-190 Pueblo federation (HHX), IW-191 Maya federation (MAY), IW-195 Garifuna coastal state (HMX), IW-199 Quechua federation (HQX), IW-202 Gran Chaco federation (HTX), IW-205 Amazonian confederation (HWX) and IW-206 Maroon republic (HXX): specific community variants with no planner gate; each needs a named community package.
- IW-193 Zapotec-Mixtec Oaxaca federation (HKX) and IW-198 Aymara state (HPX): their research requires a sourced leader from the exact named community or authentic material for the actual institution, and forbids a generated council; the working tree has neither.
- IW-201 Muisca restoration (HSX): a restoration needs a period royal or customary institution, and no Muisca institution existed in the 1930s; a council made up for it would be a generated institution.
- IW-196 Caribbean Federation, IW-197 Mapuche or Wallmapu state and IW-204 Araucania and Patagonia restoration: vanilla route overlays by design. D32 also fixes the IW-196 and IW-204 overlay triggers to read the carrier itself rather than ROOT.

## Formables

FORM-44 Rio de la Plata Confederation has the Guarani and Patagonian states, and FORM-45 Mesoamerican Federation has Yucatan. FORM-40, FORM-41, FORM-42, FORM-43, FORM-46 and FORM-47 have no admitted member. All remain closed: none has a carrier tag, member contract, consent rule, territory proof or flag, and none is in the shared commit allowlist.

## Assets

The rows reuse their registered or vanilla flags, names and leader portraits, shared Event 006 and vanilla idea pictures, the shared decision icons and vanilla report event pictures. No new sprite is registered.

## Future plans

- Five-node focus groups for Quebec, Newfoundland, Texas and Yucatan.
- Sourced institutional leaders for the Newfoundland, Texas and Patagonian institutions, and sourced leaders for Quebec and Yucatan.
- Named community packages for the Haudenosaunee, Pueblo, Maya, Garifuna, Quechua, Chaco, Amazonian and Maroon rows, and distinct map states for Acadia, the Cherokee, Lakota, Dine and Miskito rows.
