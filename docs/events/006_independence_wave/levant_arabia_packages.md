# Event 006 Levant and Arabia packages

Agent decision D25 admitted five Levant and Arabia rows through the regional framework engine (`regional_framework_packages.md`); agent decision D34 later blocked IW-076 Hadhramaut, so four are admitted. The other six rows of the region stay blocked; the reasons are listed below.

## Admitted rows

| Row | Tag | Anchor | Depth | Leadership | Government routes | Power centres |
| --- | --- | --- | --- | --- | --- | --- |
| IW-073 Hejaz | CUX (X-tag) | 679 Hejaz | Level 2 | The Consultative Council of the Hejaz, chaired by the leader the game appoints | constitutional, traditional, emergency, patron client | traditional authority and assembly |
| IW-078 Imamate of Oman | IMO | 1015 Interior Oman (Nizwa) | Level 2 | Vanilla Imam Muhammad bin Abdullah al-Khalili | constitutional, traditional, emergency, patron client | traditional authority and assembly |
| IW-081 Lebanon | LEB | 553 Lebanon | Level 2 | Vanilla roster led by Abdallah Bayhum | constitutional, popular council, emergency, patron client | domestic cabinet and foreign patron |
| IW-082 Palestine | PAL | 454 Palestine | Level 2 | Vanilla Ahmed Hilmi Pasha under the democratic party | constitutional, popular council, traditional, emergency, patron client | central government and provinces |

Radical sovereignty is excluded for all four. The vanilla PAL government is the mandate administration, so a released Palestine opens under its democratic party and suspends the High Commissioner's leader role for its own generation; cleanup restores the role exactly as vanilla defines it and restores the recorded ruling party.

LEB and PAL exist in the 1936 start as mandate subjects, so the planner can choose them only after they have ceased to exist. IMO is dormant at the start and is released from Oman. CUX is created as a dynamic country from its reserved tag.

## Level 2 layers

Each Level 2 row starts with a problem idea, has a decision category of paid projects, and receives two incidents.

### Hejaz (IW-073)

- Starting problem: Living on the Pilgrimage (stability -5%, political power -5%, consumer goods +3%).
- Seat the Consultative Council of Mecca (administration cost, 120 days): Legitimacy up, Instability down; opens the customs house.
- Guarantee the Hajj Routes (security cost, 120 days): replaces the problem with Guardians of the Hajj (stability +5%, trade opinion +10%); Recognition greatly up.
- Reopen the Jeddah Customs House (diplomatic cost, 120 days, after the council): The Jeddah Customs House (consumer goods -3%, trade opinion +5%); Capacity and Recognition up.
- Incidents: The Pilgrim Ships from Java (`chaosx.nr6.206`), The Hashemite Question (`chaosx.nr6.207`).

### Imamate of Oman (IW-078)

- Starting problem: The Treaty of Seeb Unsettled (stability -5%, trade opinion -10%).
- Convene the Shaykhs at Nizwa (administration cost, 120 days): Legitimacy and Security up.
- Renew the Treaty of Seeb (diplomatic cost, 120 days, needs a living former host at peace) or Close the Coast Road (security cost, 120 days): mutually exclusive settlements of the problem. The treaty adds The Treaty of Seeb and eases the host relation; closing the road adds The Interior Stands Alone and angers the host.
- Open the Interior Caravan Routes (strategic cost, 180 days, after either settlement): Capacity and Recognition up.
- Incidents: The Date Harvest Tithe (`chaosx.nr6.204`), Surveyors at Fahud (`chaosx.nr6.205`).

### Lebanon (IW-081)

- Starting problem: The Unwritten Pact (stability -8%, political power -10%).
- Apportion the Great Offices (administration cost, 120 days) or Open the Offices to Every Citizen (strategic cost, 180 days): mutually exclusive settlements. The first adds The National Pact; the second adds The Civic Charter, with more Legitimacy but more Instability.
- Proclaim the Free Port of Beirut (diplomatic cost, 120 days, after a settlement): The Free Port of Beirut (trade opinion +15%, consumer goods -3%).
- Settle the Mandate Accounts (diplomatic cost, 75 days, needs a living former host at peace): Recognition up and the host relation eased.
- Incidents: The Silk Mills of Mount Lebanon (`chaosx.nr6.200`), Letters from the Mahjar (`chaosx.nr6.201`).

### Palestine (IW-082)

- Starting problem: Divided Municipalities (stability -8%, political power -10%).
- Convene the Legislative Council (administration cost, 120 days): replaces the problem with The Legislative Council; Legitimacy and Recognition up, Instability down.
- Appoint the Land Registry Commission (strategic cost, 180 days, after the council): Capacity and Legitimacy up, Instability down.
- Seek Guarantees for the Holy Places (diplomatic cost, 120 days): Guarantees for the Holy Places; Recognition greatly up.
- Incidents: The General Strike (`chaosx.nr6.202`), Two Harbours on One Coast (`chaosx.nr6.203`).

The Palestine package describes a provisional government that has to build institutions both communities can share. Its texts avoid casting either community as the problem.

## AI

The shared generic Event 006 AI profiles apply. Decision weights use `independence_wave_decision_ai`: opening councils and the Hajj routes are high or urgent, civic settlements are preferred on civic routes, and the security-heavy alternatives are preferred under a severe host threat.

## Blocked rows

- IW-076 Hadhramaut (CXX): its research row requires a sourced real incumbent or claimant, or the archival record of an actual royal council, and forbids a generated institution. The Qu'aiti and Kathiri sultans reigned in 1936, but no rights-cleared portrait of either is in the working tree, and the Council of the Hadhrami Sultanates used at D25 was not an actual institution. Its runtime adapter, setup engine, loader and contacts stay wired, and the content attestation leaves it out, so every planner, Join and SCN-008 path fails closed (agent decision D34). It returns when a sourced sultan is added.
- IW-074 Najd (CVX): its disposition is formable or route only, and its anchor 292 contains the Saudi capital, which the release planner protects. No route consumer exists, so it stays out of the attestation.
- IW-075 Jabal Shammar (CWX), IW-077 Mahra (CYX), IW-079 Jabal al-Druze (DAX) and IW-080 Syrian Coast (DBX): no planner gate, loader or reservation exists. IW-075 could be bound to state 857 (Ha'il) in a later tranche; the others need a distinct map state that the current map does not have.

## Assets

The rows reuse their existing assets: the registered CUX and CXX flags and names, the vanilla LEB, PAL and IMO flags, names and leader portraits, shared Event 006 and vanilla idea pictures, the shared decision icons and vanilla report event pictures (`GFX_report_event_worker_protests`, `merchant_ship_01`, `gathering_protest`, `generic_read_write`, `generic_sign_treaty1` and `generic_conference`). No new sprite is registered.

## Future plans

- A sourced leader for the Hejaz council.
- A sourced Qu'aiti or Kathiri sultan, which would re-admit the Hadhramaut.
- A five-node focus group for each Level 2 row.
- A FORM-20 Arabian federation or FORM-21 Levantine federation contract once three members of either exist.
