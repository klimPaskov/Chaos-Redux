# Event 006 Southern Africa and Indian Ocean packages

Agent decision D29 admitted four Southern Africa and Indian Ocean rows through the regional framework engine (`regional_framework_packages.md`); agent decision D34 later blocked IW-131 Comoros, so three are admitted. The remaining rows stay blocked for the reasons below.

## Admitted rows

| Row | Tag | Anchor | Depth | Leadership | Government routes | Power centres |
| --- | --- | --- | --- | --- | --- | --- |
| IW-126 Barotseland | BAR | 981 | Level 2 | Vanilla roster: Litunga Yeta III, Litunga of Barotseland from 1916 to 1945. | constitutional, traditional, patron client | traditional authority and assembly |
| IW-130 Madagascar restoration | MAD | 543 | Level 2 | Vanilla MAD has no characters; the game appoints the leader of its opening government. | constitutional, popular council, traditional, emergency, patron client | central government and provinces |
| IW-132 Mauritius | FBX (X-tag) | 707 | Level 1 | Institutional government: the Council of Government, chaired by the leader the game appoints. | constitutional, popular council, emergency, patron client | labour councils and ministries |

Radical sovereignty is excluded for all three. Barotseland and Madagascar are vanilla tags released from their vanilla cores; Barotseland keeps its vanilla Litunga, and the game appoints the leader of Madagascar's opening government because vanilla MAD has no characters. Mauritius is created as a dynamic country from its reserved tag and opens under the Mauritian Council of Government, chaired by the leader the game appoints. Barotseland shares RG-SOUTHERN-AFRICA-COARSE with the other southern rows.

## Level 2 layers

### Barotseland (IW-126)

- Starting problem: The Divided Kuta (stability -5%, political power -5%).
- Convene the National Kuta (administration cost, 120 days): Replaces The Divided Kuta with The National Kuta, raises Legitimacy and lowers Instability. Idea: The National Kuta (stability +5%, political power +3%).
- Restore the Floodplain Canals (strategic cost, 180 days, after The National Kuta has been convened): Adds The Floodplain Canals and raises Capacity. Idea: The Floodplain Canals (stability +2%, consumer goods -3%).
- Regulate the Mine Labour Contracts (diplomatic cost, 120 days): Raises Recognition and Legitimacy.
- Incidents: The Kuomboka (`chaosx.nr6.226`), Cattle Sickness on the Plain (`chaosx.nr6.227`).

### Madagascar restoration (IW-130)

- Starting problem: The Highlands and the Coast (stability -5%, political power -5%).
- Convene the Malagasy Assembly (administration cost, 120 days): Replaces The Highlands and the Coast with The Malagasy Assembly, raises Legitimacy and lowers Instability. Idea: The Malagasy Assembly (stability +5%, political power +3%).
- Open the Tamatave Line (diplomatic cost, 120 days): Adds The Tamatave Line and raises Capacity and Recognition. Idea: The Tamatave Line (trade opinion +10%, consumer goods -2%).
- Recall the VVS Exiles (strategic cost, 180 days, after The Malagasy Assembly has been convened): Greatly raises Legitimacy, lowers Recognition abroad and raises Instability.
- Incidents: The Vanilla Planters (`chaosx.nr6.228`), The Rova Question (`chaosx.nr6.229`).

## Blocked rows

- IW-131 Comoros (FAX): admitted at D29 under a Council of the Comoro Sultanates, but its research row requires a sourced real incumbent or claimant, or the archival record of an actual royal council, and forbids a generated institution. The island sultanates were abolished in 1912, no sourced claimant is in the working tree, and the council was not an actual institution, so the row is blocked as Riau and Pattani are (agent decision D34). Its adapter, setup engine, loader and contacts stay wired; the content attestation leaves it out, so every planner, Join and SCN-008 path fails closed.
- IW-121 Zulu (EQX): the research resolution requires a sourced incumbent or claimant, or authentic archival material for the regency or royal council, and forbids a generated dynasty member or institution. The 1936 regent Mshiyeni kaDinuzulu has no rights-cleared portrait in the working tree, and downloading one needs the user's approval.
- IW-122 Ndebele (ERX), IW-123 Xhosa (ESX), IW-124 Basotho (HZX), IW-125 Eswatini (EUX) and IW-127 Herero state (EWX): no planner gate, loader or reservation; each needs a distinct map state or a named community package.
- IW-128 Nama state (EXX) and IW-129 Ovambo state (EYX): unresearched reservations with no history or names, and no planner gate.

## Formables

FORM-30 Southern African Confederation and FORM-31 Indian Ocean League State remain closed: their profiles exist for discovery, but neither has a carrier tag, member contract, consent rule, territory proof or flag, and neither is in the shared commit allowlist. The admitted rows register no formable family.

## Assets

The rows reuse their registered or vanilla flags, names and leader portraits, shared Event 006 and vanilla idea pictures, the shared decision icons and vanilla report event pictures. No new sprite is registered.

## Future plans

- Five-node focus groups for Barotseland and Madagascar.
- A sourced Zulu regency package once a rights-cleared portrait of Mshiyeni kaDinuzulu exists.
- An FORM-31 contract for Madagascar and Mauritius, and for the Comoros once a sourced claimant re-admits it.
