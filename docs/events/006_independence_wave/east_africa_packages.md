# Event 006 East Africa, Horn and Great Lakes packages

Agent decision D28 admits seven East Africa, Horn and Great Lakes rows through the regional framework engine (`regional_framework_packages.md`). The remaining rows stay blocked for the reasons below.

## Admitted rows

| Row | Tag | Anchor | Depth | Leadership | Government routes | Power centres |
| --- | --- | --- | --- | --- | --- | --- |
| IW-108 Buganda | UGA | 548 | Level 2 | Vanilla UGA roster; the game appoints the Kabaka's government leader. | constitutional, popular council, traditional, emergency, patron client | traditional authority and assembly |
| IW-110 Rwanda | RWA | 768 | Level 2 | Vanilla roster: Mwami Mutara III Rudahigwa, Mwami of Rwanda from 1931 to 1959. | constitutional, traditional, emergency, patron client | traditional authority and assembly |
| IW-111 Burundi | BRD | 769 | Level 2 | Vanilla roster: Mwami Mwambutsa IV, Mwami of Burundi from 1915 to 1966. | constitutional, traditional, emergency, patron client | restoration court and military guardians |
| IW-113 Harar | HAR | 835 | Level 2 | Vanilla HAR has no characters; the merchant council's leader is appointed by the game. | constitutional, popular council, traditional, emergency, patron client | municipal commission and industrial security |
| IW-114 Afar state | AFA | 908 | Level 1 | Vanilla roster: Sultan Mohamed Yayyo of Aussa. | constitutional, traditional, emergency, patron client | central government and provinces |
| IW-115 Somaliland sultanate federation | SOM | 269 | Level 2 | Vanilla SOM has no characters; the sultans' council's leader is appointed by the game. | constitutional, traditional, emergency, patron client | central government and provinces |
| IW-119 Tigray | TIG | 842 | Level 2 | Vanilla TIG has no characters; the highland council's leader is appointed by the game. | constitutional, traditional, emergency, patron client | restoration court and military guardians |

Radical sovereignty is excluded for all seven. Every row uses a vanilla tag released by `release` from its vanilla core. Buganda, Rwanda and Burundi share RG-GREAT-LAKES-COARSE, and Harar, Afar, Somaliland and Tigray share RG-HORN-HIGHLANDS-COARSE, so a wave releases at most one country from each group. The vanilla Afar state owns its anchor at the 1936 start, so the planner can choose it only after it has ceased to exist.

Vanilla UGA, HAR, SOM and TIG have no country-leader characters, so the game appoints the leader of their opening government, as accepted for KHA and DAH. Rwanda, Burundi and the Afar state keep their vanilla monarchs.

## Level 2 layers

### Buganda (IW-108)

- Starting problem: The Kabaka and the Lukiiko (stability -5%, political power -8%).
- Convene the Great Lukiiko (administration cost, 120 days): Replaces The Kabaka and the Lukiiko with The Lukiiko Constitution, raises Legitimacy and lowers Instability. Idea: The Lukiiko Constitution (stability +5%, political power +5%).
- Settle the Mailo Land Claims (strategic cost, 180 days, after The Great Lukiiko has been convened): Raises Capacity and Legitimacy and lowers Instability.
- Open the Port Bell Wharf (diplomatic cost, 120 days): Adds The Lake Victoria Wharves and raises Capacity and Recognition. Idea: The Lake Victoria Wharves (trade opinion +10%, consumer goods -2%).
- Incidents: The Bataka Petition (`chaosx.nr6.214`), The Cotton Ginneries (`chaosx.nr6.215`).

### Rwanda (IW-110)

- Starting problem: The Court and the Chiefdoms (stability -5%, political power -5%).
- Convene the Mwami's Council (administration cost, 120 days): Replaces The Court and the Chiefdoms with The Mwami's Council, raises Legitimacy and lowers Instability. Idea: The Mwami's Council (stability +5%, political power +3%).
- Abolish the Ubuhake Contracts (strategic cost, 180 days, after The Mwami's council has been convened): Greatly raises Legitimacy, raises Capacity and raises Instability while the patrons resist.
- Open the Lake Kivu Trade (diplomatic cost, 120 days): Adds The Lake Kivu Trade and raises Capacity and Recognition. Idea: The Lake Kivu Trade (trade opinion +5%, consumer goods -2%).
- Incidents: The Coffee Quotas (`chaosx.nr6.216`), Hunger in the Hills (`chaosx.nr6.217`).

### Burundi (IW-111)

- Starting problem: The Princely Rivalry (stability -5%, political power -5%).
- Reconcile the Bezi and the Batare (administration cost, 120 days): Replaces The Princely Rivalry with The Royal Compact, raises Legitimacy and lowers Instability. Idea: The Royal Compact (stability +5%, political power +3%).
- Settle the Mandate Accounts (diplomatic cost, 75 days, needs a living former host at peace): Raises Recognition and eases hostility and obligations with our former host.
- Build the Usumbura Lake Port (strategic cost, 180 days): Adds The Usumbura Lake Port and raises Capacity and Recognition. Idea: The Usumbura Lake Port (trade opinion +5%, consumer goods -2%).
- Incidents: The Festival of the Sorghum (`chaosx.nr6.218`), Recruiters from the Mines (`chaosx.nr6.219`).

### Harar (IW-113)

- Starting problem: The City Within the Walls (stability -5%, trade opinion -5%).
- Seat the Merchants' Council of the Jugol (administration cost, 120 days): Replaces The City Within the Walls with The Merchants' Council and raises Legitimacy and Capacity. Idea: The Merchants' Council (stability +5%, trade opinion +5%).
- Reopen the Zeila Caravan Road (diplomatic cost, 120 days, after The Merchants' Council has been seated): Adds The Zeila Caravans and raises Capacity and Recognition. Idea: The Zeila Caravans (trade opinion +10%, consumer goods -2%).
- Raise the City Guard (security cost, 120 days): Raises Security and Legitimacy.
- Incidents: The Coffee of the Harar Hills (`chaosx.nr6.220`), The Shrines of the City (`chaosx.nr6.221`).

### Somaliland sultanate federation (IW-115)

- Starting problem: Rival Sultanates (stability -8%, political power -5%).
- Convene the Sultans' Council at Hargeisa (administration cost, 120 days): Replaces Rival Sultanates with The Sultans' Council, raises Legitimacy and lowers Instability. Idea: The Sultans' Council (stability +5%, political power +3%).
- Open Berbera to the Gulf Trade (diplomatic cost, 120 days): Adds The Berbera Trade and raises Capacity and Recognition. Idea: The Berbera Trade (trade opinion +10%, consumer goods -2%).
- Divide the Grazing Wells (strategic cost, 180 days, after The Sultans' Council has been convened): Lowers Instability and raises Legitimacy.
- Incidents: The Livestock Ships to Aden (`chaosx.nr6.222`), The Dervish Veterans (`chaosx.nr6.223`).

### Tigray (IW-119)

- Starting problem: The Divided Highlands (stability -5%, political power -5%).
- Convene the Council at Mek'ele (administration cost, 120 days): Replaces The Divided Highlands with The Mek'ele Council, raises Legitimacy and lowers Instability. Idea: The Mek'ele Council (stability +5%, political power +3%).
- Settle the Church Lands of Aksum (strategic cost, 180 days, after The council at Mek'ele has been convened): Raises Legitimacy and Capacity.
- Garrison the Highland Passes (security cost, 120 days): Adds The Highland Passes and raises Security. Idea: The Highland Passes (army defence +10%).
- Incidents: The Salt Bars of the Plain (`chaosx.nr6.224`), The Clergy of Aksum (`chaosx.nr6.225`).

## Blocked rows

- IW-109 Bunyoro (EEX), IW-112 Ankole (EHX), IW-116 Zanzibar (ELX), IW-117 Kilwa restoration (EMX) and IW-120 Oromo regional federation (ORO): no planner gate, loader or reservation; each needs a distinct map state or a named community package.
- IW-118 Maasai regional state (ENX): an unresearched reservation with no history or names, and no planner gate.

## Formables

FORM-27 Great Lakes Federation, FORM-28 East African Federation and FORM-29 Horn League State remain closed: their profiles exist for discovery, but none has a carrier tag, member contract, consent rule, territory proof or flag, and none is in the shared commit allowlist. The admitted rows register no formable family.

## Assets

The rows reuse their registered or vanilla flags, names and leader portraits, shared Event 006 and vanilla idea pictures, the shared decision icons and vanilla report event pictures. No new sprite is registered.

## Focus source status (2026-10-08)

The accepted five-node regional groups for `UGA`, `RWA`, `BRD`, `HAR`, `SOM`, `TIG` are implemented at source in `416688b8963ea0b1a47e3c8682b8125455cfca40`.
The [regional source report](../../plans/006_independence_wave_plans/subagent_handoffs/regional_focus_source_commit_20261007.md) records the parent-reviewed contract, imports, project interlocks and validation limits.
Definitions are in [006_independence_wave_regional_focus_a.txt](../../../common/national_focus/006_independence_wave_regional_focus_a.txt), imported by the existing shared Event 006 tree.
Project nodes reuse the completion helpers in [the regional package effects](../../../common/scripted_effects/006_independence_wave_east_africa_package_effects.txt) already used by [their paid decisions](../../../common/decisions/006_independence_wave_east_africa_decisions.txt), with project/focus locks and guarded capstone progression.
Imported-node geometry/connectors, native project behavior, full campaign AI and outstanding portrait gates remain open.

## Future plans

- Sourced leaders for the Buganda, Harar, Somaliland and Tigray governments.
- FORM-27 and FORM-29 carrier contracts now that two or more members of each exist.
