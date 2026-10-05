# Event 006 package incidents

Each Level 2 package that had no story incidents of its own now has two. They give the package's own ledgers, its founding history and its former host a voice after release.

## How it works

1. When a released country settles its founding posture (`chaosx.nr6.41` for players, `chaosx.nr6.42` for the AI), `independence_wave_schedule_package_incident_a` stores the current Event 006 generation in `independence_wave_package_incident_generation` and schedules the package's first incident after `independence_wave_package_incident.first_delay_days`.
2. Either answer to the first incident schedules the second after `independence_wave_package_incident.second_delay_days`.
3. Every incident trigger checks the package identity and `can_fire_independence_wave_package_incident`, which requires an active Event 006 origin of the same generation. An event scheduled for an earlier release of the tag therefore never fires.
4. Each option sets its receipt, zeroes the shared deltas, and applies its Statehood deltas through `independence_wave_decision_apply_country_deltas`, its package ledger deltas through the package's own clamped helper, and, where the text says so, a former-host hostility change through `independence_wave_decision_apply_host_deltas`. Costly options require and spend 35 political power or the light manpower cost.
5. `independence_wave_clear_package_incident_runtime` runs in the generation reset and at origin end.

No hook iterates countries or runs on a daily, weekly or monthly pulse.

## Incidents

| Package | Event | Title | Options |
| --- | --- | --- | --- |
| Scotland (IW-001) | `chaosx.nr6.101` | The Clyde Shipyard Ledgers | Honour the Admiralty contracts; Requisition the yards for Scotland |
| Scotland (IW-001) | `chaosx.nr6.102` | Raids on the Highland Estates | Pass a Crofters' Charter; Restore order on the estates |
| Wales (IW-002) | `chaosx.nr6.103` | Coal for Whom? | Keep the export contracts; Reserve coal for the Welsh railways |
| Wales (IW-002) | `chaosx.nr6.104` | The Language of the Courts | Bilingual courts in every county; Let each county decide |
| Brittany (IW-004) | `chaosx.nr6.105` | The Fleet at Brest | Hand the harbour to Breton crews; Share Brest with the French officers |
| Brittany (IW-004) | `chaosx.nr6.106` | Breton in the Schools | Fund Breton teacher colleges; Teach both languages |
| Catalonia (IW-014) | `chaosx.nr6.107` | The Barcelona Collectives | Recognize the workers' committees; Return the factories to their owners |
| Catalonia (IW-014) | `chaosx.nr6.108` | The Ebro Water Board | Favour the irrigators; Favour the power stations |
| Transylvania (IW-023) | `chaosx.nr6.109` | The University of Cluj | Divide it into two faculties; One university under the state |
| Transylvania (IW-023) | `chaosx.nr6.110` | The Saxon Town Charters | Restore limited town charters; One law for every town |
| Macedonia (IW-026) | `chaosx.nr6.111` | The Bands in the Hills | Enlist the bands; Disarm them |
| Macedonia (IW-026) | `chaosx.nr6.112` | The Tobacco Harvest | Buy the harvest for the state; Sell it to foreign merchants |
| Bosnia (IW-029) | `chaosx.nr6.113` | The Endowment Lands | Return the endowment lands; Keep them for the treasury |
| Bosnia (IW-029) | `chaosx.nr6.114` | The Drina Ferries | Garrison the crossings; License the ferrymen |
| Karelia (IW-033) | `chaosx.nr6.115` | Timber for Leningrad | Deliver the timber; Keep the timber in Karelia |
| Karelia (IW-033) | `chaosx.nr6.116` | Volunteers from Finland | Accept the volunteers; Raise a Karelian militia instead |
| Crimea (IW-041) | `chaosx.nr6.117` | Returning Families at Simferopol | Open the return registers; Settle the current tenants first |
| Crimea (IW-041) | `chaosx.nr6.118` | The Sevastopol Dockyards | Pay the crews from the treasury; Lease the docks to merchants |
| Ruthenia (IW-038) | `chaosx.nr6.119` | The Language of the State | Three official languages; Ukrainian as the state language |
| Ruthenia (IW-038) | `chaosx.nr6.120` | The Carpathian Sich | Absorb the Sich into the army; Disband the Sich |
| Kuban (IW-040) | `chaosx.nr6.121` | Stanitsa Allotments | Equal allotments for newcomers; Keep the Cossack land rights |
| Kuban (IW-040) | `chaosx.nr6.122` | The Grain Arrears | Return the grain to the villages; Sell it through Novorossiysk |
| Tatarstan (IW-044) | `chaosx.nr6.123` | The Kazan Madrasas | Reopen the madrasas; State schools only |
| Tatarstan (IW-044) | `chaosx.nr6.124` | The Volga Barge Strike | Raise the bargemen's pay; Put the river under martial law |
| Bashkiria (IW-045) | `chaosx.nr6.125` | The Ishimbay Oil Wells | Keep the engineers on contract; Nationalize the wells |
| Bashkiria (IW-045) | `chaosx.nr6.126` | The Kurultai Elections | Call the elections; Taxes first, elections later |
| Armenia (IW-070) | `chaosx.nr6.127` | The Refugee Quarters | Build permanent quarters; Settle them in the border villages |
| Armenia (IW-070) | `chaosx.nr6.128` | The Party Committees | Give them commands; Keep parties out of the army |
| Georgia (IW-071) | `chaosx.nr6.129` | The Batumi Port Dues | Lower the dues; Keep the dues for the treasury |
| Georgia (IW-071) | `chaosx.nr6.130` | The Autonomy Statutes | Grant the autonomy statutes; One undivided republic |
| Azerbaijan (IW-072) | `chaosx.nr6.131` | The Baku Oil Workers | Share the revenue; Break the strike |
| Azerbaijan (IW-072) | `chaosx.nr6.132` | Foreign Oil Concessions | Grant the concessions; Keep the fields national |
| Hawaii (IW-173) | `chaosx.nr6.133` | The Plantation Strike | Recognize the unions; Back the planters |
| Hawaii (IW-173) | `chaosx.nr6.134` | The Pearl Harbor Yards | Lease the berths; Keep the yards for the island guard |
| California (IW-184) | `chaosx.nr6.135` | The Central Valley Water | Water for the farms; Water for the cities and shipyards |
| California (IW-184) | `chaosx.nr6.136` | The Studios Abroad | Court the studios; Tax the studios |
| Basque Country (IW-013) | `chaosx.nr6.137` | The Bilbao Foundries | Accept Madrid's orders; Seek buyers abroad |
| Basque Country (IW-013) | `chaosx.nr6.138` | The Provincial Treasuries | Restore the provincial treasuries; One Basque treasury |
| Galicia (IW-015) | `chaosx.nr6.139` | The Vigo Canneries | Buy tinplate abroad; Ration the canneries |
| Galicia (IW-015) | `chaosx.nr6.140` | The Foros Rents | Abolish the foros; Buy out the landlords |
| Don Host (IW-039) | `chaosx.nr6.141` | The Novocherkassk Regalia | Restore the ataman's office; Keep the elected charter |
| Don Host (IW-039) | `chaosx.nr6.142` | The Millerovo Railwaymen | Station guards at the yards; Negotiate safe passage |
| Lebanon (IW-081) | `chaosx.nr6.200` | The Silk Mills of Mount Lebanon | Buy the cocoons for the state; Let Lyon set the price |
| Lebanon (IW-081) | `chaosx.nr6.201` | Letters from the Mahjar | Give the emigrants a vote; Ask the emigrants for a loan |
| Palestine (IW-082) | `chaosx.nr6.202` | The General Strike | Negotiate with the strike committee; Reopen the ports under emergency rule |
| Palestine (IW-082) | `chaosx.nr6.203` | Two Harbours on One Coast | Keep Jaffa as the national harbour; License the Tel Aviv harbour too |
| Imamate of Oman (IW-078) | `chaosx.nr6.204` | The Date Harvest Tithe | Collect the tithe for the treasury; Leave the tithe with the tribes |
| Imamate of Oman (IW-078) | `chaosx.nr6.205` | Surveyors at Fahud | Admit them on the Imam's terms; Turn them back at the wadi |
| Hejaz (IW-073) | `chaosx.nr6.206` | The Pilgrim Ships from Java | Build our own quarantine station at Jeddah; Rely on the Kamaran station |
| Hejaz (IW-073) | `chaosx.nr6.207` | The Hashemite Question | Invite the Hashemite family home; Keep the council in charge |
| Rif (IW-083) | `chaosx.nr6.208` | Veterans of Anual | Give them commands in the army; Settle them on the plain of Nekor |
| Rif (IW-083) | `chaosx.nr6.209` | The Mines of Uixan | Honour the mining concession; Take the mines for the republic |
| Oyo (IW-097) | `chaosx.nr6.210` | The Ibadan Toll Gates | Buy out the tolls; Leave the tolls to Ibadan |
| Oyo (IW-097) | `chaosx.nr6.211` | The Cocoa Buyers | Back the farmers' hold-up; Sell through the buying pool |
| Kanem-Bornu (IW-099) | `chaosx.nr6.212` | The Scholars of Kukawa | Fund the Kukawa schools; Open state schools in Maiduguri |
| Kanem-Bornu (IW-099) | `chaosx.nr6.213` | Salt from Bilma | Let the caravans pass free; Tax the caravans at the lake |
| Buganda (IW-108) | `chaosx.nr6.214` | The Bataka Petition | Hear the clan heads; Uphold the estate titles |
| Buganda (IW-108) | `chaosx.nr6.215` | The Cotton Ginneries | Set a minimum price for the growers; Leave the price to the ginners |
| Rwanda (IW-110) | `chaosx.nr6.216` | The Coffee Quotas | End the compulsory quotas; Keep the quotas for export |
| Rwanda (IW-110) | `chaosx.nr6.217` | Hunger in the Hills | Open the royal granaries; Ask the missions to distribute grain |
| Burundi (IW-111) | `chaosx.nr6.218` | The Festival of the Sorghum | Hold the festival at court; Keep the ceremony modest |
| Burundi (IW-111) | `chaosx.nr6.219` | Recruiters from the Mines | Allow the recruiters; Ban the recruiters |
| Harar (IW-113) | `chaosx.nr6.220` | The Coffee of the Harar Hills | Found a coffee board; Leave the trade to the merchants |
| Harar (IW-113) | `chaosx.nr6.221` | The Shrines of the City | Protect every shrine and church alike; Restore the shrines first |
| Somaliland sultanate federation (IW-115) | `chaosx.nr6.222` | The Livestock Ships to Aden | Tax the livestock exports; Let the herders trade free |
| Somaliland sultanate federation (IW-115) | `chaosx.nr6.223` | The Dervish Veterans | Honour the Dervish veterans; Keep them out of the council |
| Tigray (IW-119) | `chaosx.nr6.224` | The Salt Bars of the Plain | Tax the salt caravans; Let the salt pass untaxed |
| Tigray (IW-119) | `chaosx.nr6.225` | The Clergy of Aksum | Give the clergy a seat; Keep the church outside the council |
| Barotseland (IW-126) | `chaosx.nr6.226` | The Kuomboka | Fund the royal barge; Hold a smaller crossing |
| Barotseland (IW-126) | `chaosx.nr6.227` | Cattle Sickness on the Plain | Quarantine the herds; Sell the herds before the ban |
| Madagascar restoration (IW-130) | `chaosx.nr6.228` | The Vanilla Planters | Set export grades; Let the planters sell freely |
| Madagascar restoration (IW-130) | `chaosx.nr6.229` | The Rova Question | Restore the Rova; Keep the palace closed |
| Punjab (IW-134) | `chaosx.nr6.230` | The Moneylenders' Bills | Pass the debt relief bills; Protect the market towns' credit |
| Punjab (IW-134) | `chaosx.nr6.231` | The Returning Soldiers | Raise a provincial guard; Grant them colony land |
| Sindh (IW-136) | `chaosx.nr6.232` | The Haris and the Zamindars | Protect the haris' tenancy; Leave the batai to custom |
| Sindh (IW-136) | `chaosx.nr6.233` | Silt in the Barrage Canals | Fund the canal clearance; Leave the canals for next season |
| Balochistan (IW-137) | `chaosx.nr6.234` | Raiders on the Western Border | Send the levies; Let the sardars settle it in jirga |
| Balochistan (IW-137) | `chaosx.nr6.235` | The Gwadar Dhows | Let the dhows trade untaxed; Levy customs at Pasni |
| Pashtunistan (IW-138) | `chaosx.nr6.236` | Tolls on the Khyber Railway | Charge tolls on the railway; Keep the pass free |
| Pashtunistan (IW-138) | `chaosx.nr6.237` | A Feud at Bannu | Let the jirga judge it; Send the frontier constabulary |
| Kashmir (IW-139) | `chaosx.nr6.238` | The Grievances Report | Carry out the recommendations; Postpone them |
| Kashmir (IW-139) | `chaosx.nr6.239` | The Leh Caravans | Tax the caravans at Leh; Keep the caravan trade free |
| Hyderabad (IW-140) | `chaosx.nr6.240` | The Telangana Villages | Abolish vetti labour; Leave the villages to the landlords |
| Hyderabad (IW-140) | `chaosx.nr6.241` | The State Railway | Build from the treasury; Sell bonds abroad |
| Mysore (IW-141) | `chaosx.nr6.242` | Strike at the Kolar Gold Fields | Mediate a wage award; Back the mining company |
| Mysore (IW-141) | `chaosx.nr6.243` | The Sandalwood Monopoly | Keep the state monopoly; Sell licences to foreign buyers |
| Madras States (IW-143) | `chaosx.nr6.244` | The Abstention Movement | Reserve seats for every community; Keep the property franchise |
| Madras States (IW-143) | `chaosx.nr6.245` | The Coir Workers' Strike | Recognise the coir workers' union; Break the strike |
| Assam (IW-145) | `chaosx.nr6.246` | The Digboi Lease | Raise the oil royalties; Renew the lease on the old terms |
| Assam (IW-145) | `chaosx.nr6.247` | Settlers on the Char Lands | Keep settlement within the lines; Open the wastelands to settlement |
| Manipur (IW-147) | `chaosx.nr6.248` | The Women of the Bazaar | Ban the rice exports; Let the rice mills keep exporting |
| Manipur (IW-147) | `chaosx.nr6.249` | The Hill Porterage | Abolish the porterage duty; Refer it to a commission |
| Aceh (IW-150) | `chaosx.nr6.250` | Veterans of the Long War | Pension the veterans; Disband the old bands |
| Aceh (IW-150) | `chaosx.nr6.251` | The Penang Buyers | Sell through the state warehouses; Hold the harvest for other buyers |
| Minangkabau (IW-151) | `chaosx.nr6.252` | The Merantau | Build schools at home; Tax the remittances |
| Minangkabau (IW-151) | `chaosx.nr6.253` | The Inheritance Case | Uphold the adat inheritance; Let families choose the law |
| Bali (IW-155) | `chaosx.nr6.254` | The Royal Cremation | Fund the royal cremation; Hold a modest ceremony |
| Bali (IW-155) | `chaosx.nr6.255` | The Painters of Ubud | Support the cooperative; Tax the art dealers |
| Shan federation (IW-159) | `chaosx.nr6.256` | The Poppy Fields | License and tax the poppy; Suppress the poppy trade |
| Shan federation (IW-159) | `chaosx.nr6.257` | A Disputed Succession | Let the Federal Council decide; Back the senior claimant with troops |
| Mon State (IW-161) | `chaosx.nr6.258` | The Monastery Lands | Confirm the monasteries' lands; Tax the monastery estates |
| Mon State (IW-161) | `chaosx.nr6.259` | The Tavoy Tin Mines | Take a state share; Renew the leases |
| Kachin state (IW-162) | `chaosx.nr6.260` | The Jade Traders | Tax the jade at Mogaung; Keep the jade trade free |
| Kachin state (IW-162) | `chaosx.nr6.261` | The Mission Schools | Bring the schools under the council; Leave the schools to the missions |
| Laos (IW-166) | `chaosx.nr6.262` | The Clerks of the Administration | Train Lao officials; Keep the experienced clerks |
| Laos (IW-166) | `chaosx.nr6.263` | The That Luang Festival | Fund a royal festival; Leave it to the monasteries |
| East Turkestan (IW-169) | `chaosx.nr6.264` | The Soviet Trade Agreement | Sign the trade agreement; Keep trading with India |
| East Turkestan (IW-169) | `chaosx.nr6.265` | The Hami Grievances | Restore the Hami lands; Keep the new tax rolls |
| Inner Mongolia (IW-170) | `chaosx.nr6.266` | The Wool Buyers of Kalgan | Set a fair wool price; Sell through the Kalgan houses |
| Inner Mongolia (IW-170) | `chaosx.nr6.267` | Envoys from Ulaanbaatar | Receive the envoys; Close the border |
| Ryukyu (IW-171) | `chaosx.nr6.268` | The Dialect Placards | Abolish the placards; Leave the schools as they are |
| Ryukyu (IW-171) | `chaosx.nr6.269` | Shuri Castle | Restore Shuri Castle; Leave the work for later |
| Samoa (IW-175) | `chaosx.nr6.270` | The Titles Court | Let the Fono judge titles; Keep the Land and Titles Court |
| Samoa (IW-175) | `chaosx.nr6.271` | The Mau Procession | Honour the fallen of 1929; Ban the procession |
| Quebec (IW-180) | `chaosx.nr6.272` | The Abitibi Settlers | Fund the settlers; End the settlement grants |
| Quebec (IW-180) | `chaosx.nr6.273` | Strike at Thetford Mines | Recognise the miners' union; Back the mining companies |
| Newfoundland (IW-182) | `chaosx.nr6.274` | The Labrador Boundary | Survey and post the boundary; Offer a joint commission |
| Newfoundland (IW-182) | `chaosx.nr6.275` | The Merchants of Water Street | Set a fish price for the outports; Leave the trade to the merchants |
| Texas (IW-185) | `chaosx.nr6.276` | The Hot Oil Runners | Enforce the quotas; Look the other way |
| Texas (IW-185) | `chaosx.nr6.277` | The Border Bridges | Open the bridges to free trade; Tax the border trade |
| Yucatan (IW-192) | `chaosx.nr6.278` | The Leagues of Resistance | Recognise the leagues; Ban the leagues |
| Yucatan (IW-192) | `chaosx.nr6.279` | The Price of Twine | Buy the crop at a fixed price; Let the price fall |
| Venice (IW-020) | `chaosx.nr6.280` | Acqua Alta | Fund the lagoon defences; Leave the repairs to the parishes |
| Venice (IW-020) | `chaosx.nr6.281` | The Festival on the Lido | Invite the foreign studios; Keep it a showcase of our own |
| Circassia (IW-064) | `chaosx.nr6.282` | The Stud Farms of Kabarda | Keep the horses for the guard; Sell the horses abroad |
| Circassia (IW-064) | `chaosx.nr6.283` | The Adyghe Schools | Teach in Adyghe and Kabardian; Keep Russian in the schools |
| Chechnya (IW-065) | `chaosx.nr6.284` | A Blood Feud in the Mountains | Let the elders reconcile the families; Send the guard |
| Chechnya (IW-065) | `chaosx.nr6.285` | The Refinery Workers | Raise the refinery wages; Keep the refineries running |
| Dagestan (IW-066) | `chaosx.nr6.286` | The Winter Pastures | Guarantee the winter pastures; Open the plains to farming |
| Dagestan (IW-066) | `chaosx.nr6.287` | The Silversmiths of Kubachi | Fund the craft school; Tax the silver trade |

## Files

- `events/006_independence_wave_package_incident_events.txt` (events `chaosx.nr6.101` to `.142`).
- `common/scripted_effects/006_independence_wave_package_incident_effects.txt` and `common/scripted_triggers/006_independence_wave_package_incident_triggers.txt`.
- `common/script_constants/006_independence_wave_package_incident_constants.txt` (`independence_wave_package_incident`).
- `localisation/english/006_independence_wave_package_incidents_l_english.yml`.

## Icons and pictures

The incidents use existing report pictures only: vanilla `GFX_report_event_merchant_ship_01`, `generic_train`, `generic_parliament`, `generic_read_write`, `gathering_protest`, `worker_protests`, `election_vote`, `generic_sign_treaty1`, `generic_conference`, `soldiers_parade`, `finnish_soldiers_snow`, `tank_factory` and `journalists_speech`. No new sprite is registered.

## Future plans

- Let a recorded answer change a later decision or focus, for example a cheaper charter project after the Crofters' Charter.
- Add a third incident tied to each package's route government once the route events of every package are reviewed.
- Give RHI, BAY, AFX, COR, ARX and ASX the same generation receipt for their existing incidents.
