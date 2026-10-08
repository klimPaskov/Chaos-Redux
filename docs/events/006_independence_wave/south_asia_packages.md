# Event 006 South Asia and Himalaya packages

Agent decision D30 admits eleven South Asia and Himalaya rows through the regional framework engine (`regional_framework_packages.md`). The remaining rows stay blocked for the reasons below.

## Admitted rows

| Row | Tag | Anchor | Depth | Leadership | Government routes | Power centres |
| --- | --- | --- | --- | --- | --- | --- |
| IW-134 Punjab | FDX (X-tag) | 440 | Level 2 | Institutional government: the Punjab Legislative Assembly, chaired by the leader the game appoints. | constitutional, popular council, traditional, emergency, patron client | civilians and army |
| IW-136 Sindh | SIN | 443 | Level 2 | Vanilla SIN has no characters; the game appoints the leader of its opening government. | constitutional, popular council, traditional, emergency, patron client | traditional authority and assembly |
| IW-137 Balochistan | BLC | 1012 | Level 2 | Vanilla BLC has no characters; the game appoints the leader of its opening government. | constitutional, traditional, emergency, patron client | central government and provinces |
| IW-138 Pashtunistan | PSH | 442 | Level 2 | Vanilla PSH has no characters; the game appoints the leader of its opening government. | constitutional, traditional, emergency, patron client | central government and provinces |
| IW-139 Kashmir | KAS | 441 | Level 2 | Vanilla roster: Maharaja Hari Singh, ruler of Jammu and Kashmir from 1925. | constitutional, popular council, traditional, emergency, patron client | traditional authority and assembly |
| IW-140 Hyderabad | HYD | 427 | Level 2 | Vanilla roster: Nizam Mir Osman Ali Khan, ruler of Hyderabad from 1911. | constitutional, popular council, traditional, emergency, patron client | traditional authority and assembly |
| IW-141 Mysore | MYS | 425 | Level 2 | Vanilla roster: Maharaja Jayachamarajendra Wadiyar of Mysore. | constitutional, popular council, traditional, emergency, patron client | labour councils and ministries |
| IW-143 Madras States | RAS | 982 | Level 2 | Vanilla roster: Maharaja Chithira Thirunal Balarama Varma of Travancore, ruler from 1924. | constitutional, popular council, emergency, patron client | traditional authority and assembly |
| IW-145 Assam | FOX (X-tag) | 432 | Level 2 | Institutional government: the Assam Legislative Assembly, chaired by the leader the game appoints. | constitutional, popular council, traditional, emergency, patron client | central government and provinces |
| IW-147 Manipur | MPU | 990 | Level 2 | Vanilla roster: Maharaja Bodh Chandra Singh of Manipur. | constitutional, traditional, emergency, patron client | central government and provinces |
| IW-148 Sikkim | SKK | 985 | Level 1 | Vanilla SKK has no characters; the game appoints the leader of its opening government. | constitutional, traditional, patron client | traditional authority and assembly |

Radical sovereignty is excluded for all eleven. Every anchor is owned by the British Raj at the 1936 start, so the former host is RAJ. Sindh, Balochistan, Pashtunistan, Kashmir, Hyderabad, Mysore, the Madras States, Manipur and Sikkim are vanilla tags released by `release`; the release step adds the planned anchor as a core first, which matters for Pashtunistan because vanilla gives PSH no core on Peshawar. Punjab (FDX) and Assam (FOX) are created as dynamic countries from their reserved tags and open under their legislative assemblies, chaired by the leader the game appoints.

IW-134 Punjab has two loader anchors, 440 West Punjab and 986. Its runtime readiness binds the first, so the automatic path and SCN-008 release Punjab only while 440 is available, and the loader then always chooses 440.

Kashmir, Hyderabad, Mysore, the Madras States and Manipur keep their vanilla rulers. Vanilla SIN, BLC, PSH and SKK have no characters, so the game appoints the leader of their opening governments. Balochistan, Pashtunistan and Kashmir share RG-NORTHWEST-SOUTH-ASIA, Hyderabad, Mysore and the Madras States share RG-SOUTH-INDIA, and Assam, Manipur and Sikkim share RG-NORTHEAST-HIMALAYA, so a wave releases at most one country from each group. State 441 keeps its explicit mutex between automatic Kashmir and the route-only Himalayan Confederation.

The Sikkim row is Level 1 and has no regional layer.

## Level 2 layers

### Punjab (IW-134)

- Starting problem: The Canal Colony Disputes (stability -5%, political power -5%).
- Seat the Punjab Assembly (administration cost, 120 days): Adds The Punjab Legislative Assembly, raises Legitimacy and lowers Instability. Idea: The Punjab Legislative Assembly (stability +5%, political power +3%).
- Settle the Canal Water Shares (strategic cost, 180 days, after The Punjab Legislative Assembly has been seated): Removes The Canal Colony Disputes, raises Capacity and lowers Instability.
- Charter the Punjab Regiments (security cost, 120 days): Adds The Punjab Regiments and raises Security. Idea: The Punjab Regiments (conscription +5%, army org +3%).
- Incidents: The Moneylenders' Bills (`chaosx.nr6.230`), The Returning Soldiers (`chaosx.nr6.231`).

### Sindh (IW-136)

- Starting problem: The Barrage Lands (stability -5%, political power -5%).
- Seat the Sind Assembly (administration cost, 120 days): Adds The Sind Assembly, raises Legitimacy and lowers Instability. Idea: The Sind Assembly (stability +5%, political power +3%).
- Allot the Barrage Lands (strategic cost, 180 days, after The Sind Assembly has been seated): Removes The Barrage Lands, raises Capacity and Legitimacy and lowers Instability.
- Open the Karachi Trade (diplomatic cost, 120 days): Adds The Karachi Wharves and raises Capacity and Recognition. Idea: The Karachi Wharves (trade opinion +10%, consumer goods -2%).
- Incidents: The Haris and the Zamindars (`chaosx.nr6.232`), Silt in the Barrage Canals (`chaosx.nr6.233`).

### Balochistan (IW-137)

- Starting problem: The Government and the Sardars (stability -5%, political power -5%).
- Convene the Kalat Assemblies (administration cost, 120 days): Replaces The Government and the Sardars with The Kalat Assemblies, raises Legitimacy and lowers Instability. Idea: The Kalat Assemblies (stability +5%, political power +3%).
- Secure the Bolan Pass (security cost, 120 days): Adds The Bolan Guard and raises Security. Idea: The Bolan Guard (army defence +10%).
- Open the Makran Road (diplomatic cost, 120 days, after The Kalat assemblies have been convened): Raises Capacity and Recognition.
- Incidents: Raiders on the Western Border (`chaosx.nr6.234`), The Gwadar Dhows (`chaosx.nr6.235`).

### Pashtunistan (IW-138)

- Starting problem: The Tribal Agencies (stability -8%, political power -5%).
- Convene a Grand Jirga (administration cost, 120 days): Replaces The Tribal Agencies with The Grand Jirga, raises Legitimacy and lowers Instability. Idea: The Grand Jirga (stability +5%, political power +3%).
- Recognise the Khudai Khidmatgar (strategic cost, 180 days, after The Grand Jirga has been convened): Greatly raises Legitimacy, raises Recognition and raises Instability.
- Garrison the Khyber (security cost, 120 days): Adds The Khyber Garrison and raises Security. Idea: The Khyber Garrison (army defence +10%).
- Incidents: Tolls on the Khyber Railway (`chaosx.nr6.236`), A Feud at Bannu (`chaosx.nr6.237`).

### Kashmir (IW-139)

- Starting problem: The Durbar and the Valley (stability -5%, political power -5%).
- Widen the Praja Sabha (administration cost, 120 days): Replaces The Durbar and the Valley with The Praja Sabha, raises Legitimacy and lowers Instability. Idea: The Praja Sabha (stability +5%, political power +3%).
- Open the Banihal Road (diplomatic cost, 120 days): Adds The Banihal Road and raises Capacity and Recognition. Idea: The Banihal Road (trade opinion +5%, consumer goods -2%).
- Settle the Weavers' Wages (strategic cost, 180 days, after The Praja Sabha has been widened): Raises Legitimacy and lowers Instability.
- Incidents: The Grievances Report (`chaosx.nr6.238`), The Leh Caravans (`chaosx.nr6.239`).

### Hyderabad (IW-140)

- Starting problem: The Jagir Estates (stability -3%, political power -5%, consumer goods +3%).
- Reform the Legislative Council (administration cost, 120 days): Adds The Reformed Council, raises Legitimacy and lowers Instability. Idea: The Reformed Council (stability +5%, political power +3%).
- Abolish the Jagir Levies (strategic cost, 180 days, after The Legislative Council has been reformed): Removes The Jagir Estates, greatly raises Legitimacy, raises Capacity and raises Instability.
- Expand Osmania University (diplomatic cost, 120 days): Adds Osmania University and raises Recognition and Capacity. Idea: Osmania University (research speed +3%).
- Incidents: The Telangana Villages (`chaosx.nr6.240`), The State Railway (`chaosx.nr6.241`).

### Mysore (IW-141)

- Starting problem: The Dewan and the Congress (stability -5%, political power -5%).
- Seat the Representative Assembly (administration cost, 120 days): Replaces The Dewan and the Congress with The Representative Assembly, raises Legitimacy and lowers Instability. Idea: The Representative Assembly (stability +5%, political power +3%).
- Expand the Bhadravati Works (strategic cost, 180 days): Adds The Bhadravati Works and raises Capacity. Idea: The Bhadravati Works (production speed industrial complex +5%).
- Open the Irwin Canal Lands (administration cost, 120 days, after The Representative Assembly has been seated): Raises Capacity and Legitimacy.
- Incidents: Strike at the Kolar Gold Fields (`chaosx.nr6.242`), The Sandalwood Monopoly (`chaosx.nr6.243`).

### Madras States (IW-143)

- Starting problem: The Temple Entry Question (stability -5%, political power -5%).
- Proclaim Temple Entry (administration cost, 120 days): Replaces The Temple Entry Question with The Temple Entry Proclamation, greatly raises Legitimacy and lowers Instability. Idea: The Temple Entry Proclamation (stability +5%, political power +5%).
- Seat the Sree Mulam Assembly (administration cost, 120 days): Raises Legitimacy and lowers Instability.
- Expand the Cochin Harbour (strategic cost, 180 days): Adds The Cochin Harbour and raises Capacity and Recognition. Idea: The Cochin Harbour (trade opinion +10%, consumer goods -2%).
- Incidents: The Abstention Movement (`chaosx.nr6.244`), The Coir Workers' Strike (`chaosx.nr6.245`).

### Assam (IW-145)

- Starting problem: The Tea Garden Labour (stability -5%, consumer goods +3%).
- Seat the Assam Assembly (administration cost, 120 days): Adds The Assam Legislative Assembly, raises Legitimacy and lowers Instability. Idea: The Assam Legislative Assembly (stability +5%, political power +3%).
- Reform the Garden Contracts (strategic cost, 180 days, after The Assam Legislative Assembly has been seated): Replaces The Tea Garden Labour with The Tea Garden Charter, raises Legitimacy and lowers Capacity. Idea: The Tea Garden Charter (stability +3%, consumer goods -2%).
- Open the Brahmaputra Steamers (diplomatic cost, 120 days): Raises Capacity and Recognition.
- Incidents: The Digboi Lease (`chaosx.nr6.246`), Settlers on the Char Lands (`chaosx.nr6.247`).

### Manipur (IW-147)

- Starting problem: The Valley and the Hills (stability -5%, political power -5%).
- Convene the Durbar with the Hill Chiefs (administration cost, 120 days): Replaces The Valley and the Hills with The Manipur Durbar, raises Legitimacy and lowers Instability. Idea: The Manipur Durbar (stability +5%, political power +3%).
- Open the Imphal Road (diplomatic cost, 120 days): Raises Capacity and Recognition.
- Fund the Hill Schools (strategic cost, 180 days, after The Durbar has met with the hill chiefs): Adds The Hill Schools, raises Legitimacy and raises Capacity. Idea: The Hill Schools (research speed +2%, stability +2%).
- Incidents: The Women of the Bazaar (`chaosx.nr6.248`), The Hill Porterage (`chaosx.nr6.249`).

## Blocked rows

- IW-133 Bengal (BAN), IW-144 Dravidian Federation (FNX) and IW-149 Himalayan Confederation (FSX): formable or route only. They are the natural carriers of FORM-33 and FORM-35 and a possible Bengal route, and no route consumer exists yet.
- IW-135 Khalistan (KHL): the vanilla tag carries a later name that does not fit a 1930s wave, and it shares RG-PUNJAB-SIKH and the anchor 986 with the admitted Punjab row.
- IW-142 Travancore (FLX): it shares the anchor 982 with the admitted Madras States row, whose vanilla ruler is the Maharaja of Travancore.
- IW-146 (FPX): an unresearched reservation that needs a named Naga political package, with no history, names or planner gate.

## Formables

FORM-32 Indus Federation is implemented at source under the accepted D30 contract in `9e2837f8edc1633cd8e96415366821ca5dc16886`.
Its existing carrier takes IDX, with exact FDX, SIN, BLC and PSH membership, explicit proposal replies and two paid 180-day integration stages.
The [ready-formable contract](systems/ready_formable_contracts.md) binds one live stored Punjab anchor at 440 or 986, Sindh at 443, Balochistan at 1012 and Pashtunistan at 442, preserving each member's sovereign territory.
The [signature source report](../../plans/006_independence_wave_plans/subagent_handoffs/signature_source_integration_20261007.md) retains native consent/cost/cleanup, production GUI and full-AI limits.

FORM-33 Dravidian Federation retains its Madras States and Mysore members, with Travancore blocked behind the Madras States anchor.
FORM-34 Northeast Federation retains Assam and Manipur and requires the unresearched Naga package.
FORM-35 Himalayan Confederation retains Kashmir and Sikkim.
Those three families remain closed under their existing missing carrier, member/consent, territory, flag and commit contracts.

## Assets

The rows reuse their registered or vanilla flags, names and leader portraits, shared Event 006 and vanilla idea pictures, the shared decision icons and vanilla report event pictures. No new sprite is registered.

## Focus source status (2026-10-08)

The accepted five-node regional groups for `FDX`, `SIN`, `BLC`, `PSH`, `KAS`, `HYD`, `MYS`, `RAS`, `FOX`, `MPU` are implemented at source in `416688b8963ea0b1a47e3c8682b8125455cfca40`.
The [regional source report](../../plans/006_independence_wave_plans/subagent_handoffs/regional_focus_source_commit_20261007.md) records the parent-reviewed contract, imports, project interlocks and validation limits.
Definitions are in [006_independence_wave_regional_focus_a.txt](../../../common/national_focus/006_independence_wave_regional_focus_a.txt) and [006_independence_wave_regional_focus_b.txt](../../../common/national_focus/006_independence_wave_regional_focus_b.txt), imported by the existing shared Event 006 tree.
Project nodes reuse the completion helpers in [the regional package effects](../../../common/scripted_effects/006_independence_wave_south_asia_package_effects.txt) already used by [their paid decisions](../../../common/decisions/006_independence_wave_south_asia_decisions.txt), with project/focus locks and guarded capstone progression.
Imported-node geometry/connectors, native project behavior, full campaign AI and outstanding portrait gates remain open.

## Future plans

- Sourced institutional leaders for the Punjab and Assam assemblies and sourced leaders for Sindh, Balochistan and Pashtunistan.
- A named Naga political package for IW-146 and a route consumer for the Himalayan Confederation.
