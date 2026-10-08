# Event 006 Europe and Caucasus packages

Agent decision D33 admits ten remaining Europe, former Russian Empire, Persia and Caucasus rows through the regional framework engine (`regional_framework_packages.md`). The rows that stay blocked are listed below.

## Admitted rows

| Row | Tag | Anchor | Depth | Leadership | Government routes | Power centres |
| --- | --- | --- | --- | --- | --- | --- |
| IW-016 Occitania | OCC | 22 | Level 1 | Vanilla OCC has advisors but no country leader; the game appoints the leader of its opening government. | constitutional, popular council, patron client | central government and provinces |
| IW-020 Venice | ATX (X-tag) | 160 | Level 2 | Institutional government: the Assembly of Venice, named after the assembly of the 1848 Republic of San Marco, chaired by the leader the game appoints. | constitutional, popular council, traditional, patron client | central government and provinces |
| IW-021 Trieste Free State | ICX (X-tag) | 736 | Level 1 | Institutional government: the Municipal Council of Trieste, chaired by the leader the game appoints. | constitutional, popular council, patron client | domestic cabinet and foreign patron |
| IW-036 Courland | BJX (X-tag) | 190 | Level 1 | Institutional government: the Courland Provincial Assembly, chaired by the leader the game appoints. | constitutional, popular council, patron client | central government and provinces |
| IW-037 Polesia | BKX (X-tag) | 94 | Level 1 | Institutional government: the Polesian Provincial Council, chaired by the leader the game appoints. | constitutional, popular council, traditional, patron client | central government and provinces |
| IW-042 Galicia-Lodomeria | GAL | 91 | Level 1 | Vanilla GAL has no characters; the game appoints the leader of its opening government. | constitutional, traditional, patron client | central government and provinces |
| IW-062 Khuzestan | CJX (X-tag) | 413 | Level 1 | Institutional government: the Provincial Anjoman of Khuzestan, the provincial council of the 1907 Persian council law, chaired by the leader the game appoints. | constitutional, traditional, patron client | domestic cabinet and foreign patron |
| IW-064 Circassia | CLX (X-tag) | 827 | Level 2 | Institutional government: the Circassian Khase, the traditional council of the Circassian peoples, chaired by the leader the game appoints. | constitutional, traditional, emergency, patron client | traditional authority and assembly |
| IW-065 Chechnya | CIN | 821 | Level 2 | Vanilla roster: Hasan Israilov and Yusup Tambiev; a democratic opening government is led by the leader the game appoints. | constitutional, traditional, emergency, patron client | traditional authority and assembly |
| IW-066 Dagestan | DAG | 232 | Level 2 | Vanilla roster: Uzun-Haji and Adil-Girey Takhtarov; a democratic opening government is led by the leader the game appoints. | constitutional, traditional, emergency, patron client | central government and provinces |

Radical sovereignty is excluded for all ten. Occitania, Galicia-Lodomeria, Chechnya and Dagestan are vanilla tags released by `release`; Galicia-Lodomeria has no vanilla core on its anchor, so the release step's planned-anchor core makes the release valid. Venice, Trieste, Courland, Polesia, Khuzestan and Circassia are created as dynamic countries from their reserved tags and open under a named institution chaired by the leader the game appoints: the Assembly of Venice (named after the assembly of the 1848 Republic of San Marco), the Municipal Council of Trieste, the Courland Provincial Assembly, the Polesian Provincial Council, the Provincial Anjoman of Khuzestan (the provincial council of the 1907 Persian council law) and the Circassian Khase (the traditional Circassian council).

Vanilla OCC has advisors but no country leader and vanilla GAL has no characters, so the game appoints their opening leaders. Chechnya and Dagestan keep their vanilla rosters (Hasan Israilov and Yusup Tambiev; Uzun-Haji and Adil-Girey Takhtarov), and their democratic opening governments are led by the leader the game appoints. Galicia-Lodomeria binds its first loader anchor, 91 Tarnopol.

Khuzestan (CJX) is the third member of FORM-18, the Council of Communities, whose state puzzle already requires state 413. With CJX admitted, all three FORM-18 members (the carrier at 676, KUR at 1001 and CJX at 413) can now exist in a running game.

Occitania, Trieste, Courland, Polesia, Galicia-Lodomeria and Khuzestan are Level 1 rows with no regional layer.

## Level 2 layers

### Venice (IW-020)

- Starting problem: The Lagoon and the Mainland (stability -5%, political power -5%).
- Convene the Assembly of Venice (administration cost, 120 days): Replaces The Lagoon and the Mainland with The Assembly of Venice, raises Legitimacy and lowers Instability. Idea: The Assembly of Venice (stability +5%, political power +3%).
- Charter the Marghera Works (strategic cost, 180 days, after The Assembly of Venice has been convened): Adds The Marghera Works and raises Capacity. Idea: The Marghera Works (production speed industrial complex +5%).
- Restore the Arsenale (security cost, 120 days): Adds The Arsenale and raises Security. Idea: The Arsenale (production speed dockyard +10%).
- Incidents: Acqua Alta (`chaosx.nr6.280`), The Festival on the Lido (`chaosx.nr6.281`).

### Circassia (IW-064)

- Starting problem: The Scattered Nation (stability -3%, political power -5%).
- Convene the Khase (administration cost, 120 days): Adds The Circassian Khase, raises Legitimacy and lowers Instability. Idea: The Circassian Khase (stability +5%, political power +3%).
- Invite the Diaspora Home (diplomatic cost, 180 days, after The Khase has been convened): Replaces The Scattered Nation with The Returning Families, raises Legitimacy and Recognition. Idea: The Returning Families (monthly population +10%).
- Raise the Kabardian Horse (security cost, 120 days): Adds The Kabardian Horse and raises Security. Idea: The Kabardian Horse (cavalry attack +10%).
- Incidents: The Stud Farms of Kabarda (`chaosx.nr6.282`), The Adyghe Schools (`chaosx.nr6.283`).

### Chechnya (IW-065)

- Starting problem: The Mountain Feuds (stability -5%, political power -5%).
- Convene the Mekhk-Khel (administration cost, 120 days): Replaces The Mountain Feuds with The Mekhk-Khel, raises Legitimacy and lowers Instability. Idea: The Mekhk-Khel (stability +5%, political power +3%).
- Take Over the Grozny Oil Fields (strategic cost, 180 days, after The Mekhk-Khel has been convened): Adds The Grozny Oil Fields, raises Capacity and lowers Recognition. Idea: The Grozny Oil Fields (fuel gain +10%).
- Raise the Mountain Guard (security cost, 120 days): Adds The Mountain Guard and raises Security. Idea: The Mountain Guard (army defence +10%).
- Incidents: A Blood Feud in the Mountains (`chaosx.nr6.284`), The Refinery Workers (`chaosx.nr6.285`).

### Dagestan (IW-066)

- Starting problem: The Many Peoples (stability -5%, political power -5%).
- Seat the Federal Assembly (administration cost, 120 days): Replaces The Many Peoples with The Federal Assembly, raises Legitimacy and lowers Instability. Idea: The Federal Assembly (stability +5%, political power +3%).
- Fix the Languages of State (strategic cost, 180 days, after The Federal Assembly has been seated): Adds The Languages of State, raises Legitimacy and lowers Instability. Idea: The Languages of State (stability +3%).
- Open the Caspian Ports (diplomatic cost, 120 days): Adds The Caspian Ports and raises Capacity and Recognition. Idea: The Caspian Ports (trade opinion +10%, consumer goods -2%).
- Incidents: The Winter Pastures (`chaosx.nr6.286`), The Silversmiths of Kubachi (`chaosx.nr6.287`).

## Blocked rows

- IW-003 Cornwall (ACX): stays blocked under the round-2 instruction.
- IW-005 Flanders, IW-022 Dalmatia, IW-025 Vojvodina, IW-035 Livonia and IW-059 Mesopotamia: vanilla route overlays by design.
- IW-011 Faroe Islands (AKX): a scenario variant only.
- IW-032 Slavonia (BFX), IW-049 Mordovia (BWX), IW-061 Luristan (CIX) and IW-063 Bakhtiari (CKX): no planner gate, loader or reservation.
- IW-034 Ingria (BHX): formable or route only.
- IW-046 Chuvashia (CHU): it shares the CHU tag and RG-MIDDLE-VOLGA-KAZAN with the admitted IW-043 Volga Bulgaria signature package; admitting it needs a reviewed identity split between the two CHU packages.
- IW-055 Nenets (NEN) and IW-056 Evenk (EVE): research-only community variants that need a named community package.
- IW-057 Far Eastern Republic (FER): blocked by D20 (no sourced roster and no neutral flag with recorded provenance).
- IW-067 Lazistan (COX): the Laz had no political institution in the 1930s, and its research allows customary authorities only where specifically sourced.
- IW-068 Pontus (CPX) and IW-069 Cilicia (CQX): restorations whose communities left in the 1920s; no period institution remained to restore, and a made-up council would be a generated institution. Pontus also shares anchor 354 with Lazistan.

## Formables

FORM-17 North Caucasian Federation is implemented at source under the accepted D33 contract in `9e2837f8edc1633cd8e96415366821ca5dc16886`.
Its existing carrier takes NCX, with exact CLX at 827, CIN at 821 and DAG at 232 membership, explicit proposal replies, sovereign-member integration and two paid 180-day stages for mountain defence and an autonomy charter.
The [ready-formable contract](systems/ready_formable_contracts.md) and [signature source report](../../plans/006_independence_wave_plans/subagent_handoffs/signature_source_integration_20261007.md) retain native consent/cost/cleanup, production GUI and full-AI limits.

FORM-06 Adriatic Federation retains Venice and Trieste, with Dalmatia an overlay.
FORM-10 Baltic Federation retains Karelia and Courland, with Ingria blocked and Livonia an overlay.
Those two families remain closed under their existing missing carrier, member/consent, territory, flag and commit contracts.
FORM-18 retains Khuzestan as its third member.

## Assets

The rows reuse their registered or vanilla flags, names and leader portraits, shared Event 006 and vanilla idea pictures, the shared decision icons and vanilla report event pictures. No new sprite is registered.

## Focus source status (2026-10-08)

The accepted five-node regional groups for `ATX`, `CLX`, `CIN`, `DAG` are implemented at source in `416688b8963ea0b1a47e3c8682b8125455cfca40`.
The [regional source report](../../plans/006_independence_wave_plans/subagent_handoffs/regional_focus_source_commit_20261007.md) records the parent-reviewed contract, imports, project interlocks and validation limits.
Definitions are in [006_independence_wave_regional_focus_b.txt](../../../common/national_focus/006_independence_wave_regional_focus_b.txt), imported by the existing shared Event 006 tree.
Project nodes reuse the completion helpers in [the regional package effects](../../../common/scripted_effects/006_independence_wave_europe_caucasus_package_effects.txt) already used by [their paid decisions](../../../common/decisions/006_independence_wave_europe_caucasus_decisions.txt), with project/focus locks and guarded capstone progression.
Imported-node geometry/connectors, native project behavior, full campaign AI and outstanding portrait gates remain open.

## Future plans

- Sourced institutional leaders for the six custom institutions.
- A reviewed identity split for the two CHU packages (Volga Bulgaria and Chuvashia).
