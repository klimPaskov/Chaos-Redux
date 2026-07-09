# 012 Africa spec part 20, region state group and integration atlas

This atlas names intended state groups and region requirements without assigning exact HOI4 state ids. Exact ids remain an implementation research gate because the live repository and vanilla state map are not available in this sandbox.

## Region group table

| Working state group | Geographic intent | Integration anchors | Mission families | Risks |
| --- | --- | --- | --- | --- |
| `maghreb_coast` | Morocco, Algeria, Tunisia, Libya coastal and interior candidate states | Ports, colonial ownership, western Mediterranean pressure | Observation, liberation war support, port settlement, coastal rail | Strong colonial reaction and foreign naval pressure |
| `nile_valley` | Egypt-facing Sudan, Sudan Nile, Meroe and Nubia candidate states | Nile rail, river supply, Kush or Makuria candidates | River guard missions, site protection, federation or buffer routes | Egypt or outside power reaction if borders become unstable |
| `horn_red_sea` | Ethiopia, Eritrea, Djibouti, Somalia, Red Sea ports | Aksum, Ethiopia variants, Red Sea lanes, highland supply | Highland defense, port diplomacy, Red Sea corridor projects | Italian or British response depending on campaign state |
| `sahel_caravan_belt` | Mauritania, Mali, Niger, Chad, northern Nigeria, Sahel crossings | Caravan routes, Songhai, Kanem-Bornu, Sokoto, Futa candidates | Oasis supply, caravan rail, cavalry and desert infantry missions | Low infrastructure and long integration timelines |
| `gulf_of_guinea` | Senegal to Nigeria coastal and forest states | Asante, Dahomey, Oyo, Benin or Edo, Futa Jallon, Futa Toro | Ports, forest roads, gold and cocoa style resource work | Strong autonomy and rival bloc potential |
| `congo_basin` | Congo river and central forest states | Kongo, Kuba, Luba, Lunda, Kazembe, high-chaos forest actors | River integration, forest logistics, local support, disease containment gates | High resistance and high-chaos route risk |
| `great_lakes` | Uganda, Rwanda, Burundi, western Kenya, lake regions | Buganda and lake diplomacy | Lake transport, highland rail, local member association | Neighbouring regional rivalries |
| `swahili_coast` | Kenya, Tanzania, Mozambique coast, Zanzibar and islands | Kilwa and Swahili city-states, Indian Ocean trade | Port league, convoy protection, coastal restoration, trade missions | Naval blockade and outside expedition risk |
| `zambezi_zimbabwe_plateau` | Zimbabwe, Zambia, Malawi, Mozambique interior links | Great Zimbabwe, Mutapa, Rozwi, Lozi or Barotse | Plateau rail, stone site guard, copper and gold routes | Rival heritage claims and resistance |
| `southern_cape_plateau` | South Africa, Botswana, Namibia, Lesotho, Eswatini candidate states | RSA branch, Azania, Zulu, southern industry, ports | Civil war aftermath, southern integration, mining and rail projects | Allied peace branch and strong outside reaction |
| `indian_ocean_islands` | Madagascar, Comoros, Mauritius, Seychelles where mapped | Merina and island gateway routes | Island convoys, port guards, returnee lane stops, naval defense | Convoy and naval access heavy |
| `atlantic_islands_ports` | Cape Verde, Canary or Atlantic relay ports only where map and ownership fit | Diaspora and Black Star lane relay | Port access, shipping lane, cultural diplomacy, settlement gateway | Foreign refusal or blockade can close lanes |

## Staged coring route

| Stage | Required evidence | Result | Failure pressure |
| --- | --- | --- | --- |
| Claim | Route focus or event claim, target observed, region identified | Claims or diplomatic pressure, no core | Foreign alert and rival appeal can rise |
| Protection | Defense, aid, local support, or League membership | Protectorate, member, or occupation route | Refusal, sanctions, or local suspicion |
| Administration | Rail, supply, port, or local administration mission | Reduced resistance and integration readiness | Resistance, autonomy demand, mission lockout |
| Association | Target accepts constituent, associated, puppet, or federal member path | Partial integration bonuses and subject/member status | Rival bloc formation if pressured |
| Coring | Local support, peace, control, low resistance, and route-specific legitimacy | Selected states become cores in batches | Regional unrest, foreign crisis, or autonomy backlash |

## Region-specific integration requirements

- Maghreb and Swahili coast require port and naval pressure checks before large integration moves.
- Sahel and Sahara groups require supply and rail work before major military or coring rewards.
- Congo basin and Deep Green adjacent regions require local support, forest logistics, and disease safety gates.
- Southern Cape and plateau regions must respect the RSA civil-war outcome before ordinary unifier integration continues.
- Island groups use convoy capacity, naval access, and port capacity as core requirements.
- Nile valley and Horn routes should account for old-polity claims and strong outside reactions before annexation pressure.

## State id handoff rule

The implementation pass should create a state-group audit table from vanilla and repository state files. The table should list exact state ids, owner at 1936 start, colonial owner, core status, ports, railways, supply hubs, resources, victory points, and likely restored polity assignments. No state id should be guessed from memory.
