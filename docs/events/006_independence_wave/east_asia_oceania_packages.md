# Event 006 Southeast Asia, East Asia and Oceania packages

Agent decision D31 admits thirteen Southeast Asia, East Asia and Oceania rows through the regional framework engine (`regional_framework_packages.md`), beside Hawaii (IW-173) and Fiji (IW-177), admitted earlier. The remaining rows stay blocked for the reasons below.

## Admitted rows

| Row | Tag | Anchor | Depth | Leadership | Government routes | Power centres |
| --- | --- | --- | --- | --- | --- | --- |
| IW-150 Aceh | ATJ | 1050 | Level 3 signature source with a Level 2 foundation | Vanilla roster: Sultan Alauddin Muhammad Da'ud Syah II, the last Sultan of Aceh, exiled in 1907. | constitutional, traditional, emergency, patron client | traditional authority and assembly |
| IW-151 Minangkabau | FUX (X-tag) | 1048 | Level 2 | Institutional government: the Minangkabau Council of the Nagari, chaired by the leader the game appoints. | constitutional, popular council, traditional, emergency, patron client | traditional authority and assembly |
| IW-154 Bugis state | FXX (X-tag) | 673 | Level 1 | Institutional government: the Hadat Council of South Celebes, chaired by the leader the game appoints. | constitutional, traditional, patron client | traditional authority and assembly |
| IW-155 Bali | BLI | 1052 | Level 2 | Vanilla roster: Ida I Dewa Agung Gde Oka Geg, Dewa Agung of Klungkung. | constitutional, traditional, emergency, patron client | traditional authority and assembly |
| IW-159 Shan federation | GCX (X-tag) | 999 | Level 2 | Institutional government: the Federal Council of Shan Chiefs (formed 1922), chaired by the leader the game appoints. | constitutional, traditional, emergency, patron client | central government and provinces |
| IW-161 Mon State | IAX (X-tag) | 994 | Level 3 signature source with a Level 2 foundation | Institutional government: the Provisional Mon Federal Council of monasteries, cultural associations and town notables, chaired by the leader the game appoints. | constitutional, popular council, traditional, patron client | traditional authority and assembly |
| IW-162 Kachin state | IBX (X-tag) | 998 | Level 2 | Institutional government: the Council of the Kachin Duwas, chaired by the leader the game appoints. | constitutional, traditional, emergency, patron client | central government and provinces |
| IW-166 Laos | LAO | 1069 | Level 2 | Vanilla roster: King Sisavang Vong of Luang Prabang, on the throne from 1904. | constitutional, traditional, emergency, patron client | central government and provinces |
| IW-167 Champa | CHM | 286 | Level 1 | Vanilla CHM has no characters; the game appoints the leader of its opening government. | constitutional, traditional, patron client | traditional authority and assembly |
| IW-169 East Turkestan | GMX (X-tag) | 617 | Level 2 | Institutional government: the Provisional Council of East Turkestan, chaired by the leader the game appoints. | constitutional, traditional, emergency, patron client | central government and provinces |
| IW-170 Inner Mongolia | MEN | 621 | Level 2 | Vanilla roster: Prince Demchugdongrub, head of the Mongol autonomy movement from 1933. | constitutional, traditional, emergency, patron client | traditional authority and assembly |
| IW-171 Ryukyu | OKN | 526 | Level 2 | Vanilla roster: Hiroshi Sho, head of the former Ryukyuan royal house from 1920. | constitutional, popular council, traditional, patron client | traditional authority and assembly |
| IW-175 Samoa | SAM | 726 | Level 2 | Vanilla SAM has no characters; the game appoints the leader of its opening government. | constitutional, popular council, traditional, patron client | traditional authority and assembly |

Radical sovereignty is excluded for all thirteen. Aceh, Bali, Laos, Champa, Inner Mongolia, Ryukyu and Samoa are vanilla tags released by `release` from their vanilla cores. Minangkabau, the Bugis state, the Shan federation, Mon State, the Kachin state and East Turkestan are created as dynamic countries from their reserved tags and open under a named council chaired by the leader the game appoints: the Minangkabau Council of the Nagari, the Hadat Council of South Celebes, the Federal Council of Shan Chiefs (the federation's council from 1922), the Provisional Mon Federal Council, the Council of the Kachin Duwas and the Provisional Council of East Turkestan.

Aceh, Bali, Laos, Inner Mongolia and Ryukyu keep their vanilla leaders: Sultan Alauddin Muhammad Da'ud Syah II, the Dewa Agung of Klungkung, King Sisavang Vong, Prince Demchugdongrub and Hiroshi Sho. Vanilla CHM and SAM have no characters, so the game appoints the leader of their opening governments. Aceh and Mon State have implemented Level 3 signature source over their Level 2 foundations, as described in [the Event 006 signature modules](signature_modules.md).

Aceh and Minangkabau share RG-SUMATRA, the Bugis state and Bali share RG-EAST-INDONESIA, the Shan, Mon and Kachin rows share RG-MAINLAND-SE-ASIA-COARSE, Laos and Champa share RG-LAOS-VIETNAM-HIGHLANDS, East Turkestan and Inner Mongolia share RG-INNER-ASIA, and Samoa shares RG-PACIFIC-ISLANDS with Fiji, so a wave releases at most one country from each group. East Turkestan's anchor 617 is Sinkiang's capital, which the planner protects, so it is chosen only after Urumqi has passed to a country whose capital is elsewhere. Inner Mongolia and Samoa need their vanilla tags to be absent, as Mengkukuo exists at the 1936 start.

The Bugis state and Champa are Level 1 rows with no regional layer.

## Level 2 layers

### Aceh (IW-150)

- Starting problem: The Uleebalang and the Ulama (stability -5%, political power -5%).
- Convene the Council of Notables (administration cost, 120 days): Replaces The Uleebalang and the Ulama with The Council of Notables, raises Legitimacy and lowers Instability. Idea: The Council of Notables (stability +5%, political power +3%).
- Fund the Madrasah Reform (strategic cost, 180 days, after The Council of Notables has been convened): Raises Legitimacy and Capacity.
- Reopen the Pepper Ports (diplomatic cost, 120 days): Adds The Pepper Ports and raises Capacity and Recognition. Idea: The Pepper Ports (trade opinion +10%, consumer goods -2%).
- Incidents: Veterans of the Long War (`chaosx.nr6.250`), The Penang Buyers (`chaosx.nr6.251`).

### Minangkabau (IW-151)

- Starting problem: Adat and the Reformers (stability -5%, political power -5%).
- Join Adat and Ulama (administration cost, 120 days): Replaces Adat and the Reformers with The Council of Adat and Ulama, raises Legitimacy and lowers Instability. Idea: The Council of Adat and Ulama (stability +5%, political power +3%).
- Charter the Thawalib Schools (strategic cost, 180 days, after Adat and ulama sit in one council): Adds The Thawalib Schools, raises Legitimacy and raises Capacity. Idea: The Thawalib Schools (research speed +3%).
- Take Over the Ombilin Mines (diplomatic cost, 120 days): Adds The Ombilin Coal Mines, raises Capacity and lowers Recognition. Idea: The Ombilin Coal Mines (production speed industrial complex +5%).
- Incidents: The Merantau (`chaosx.nr6.252`), The Inheritance Case (`chaosx.nr6.253`).

### Bali (IW-155)

- Starting problem: The Eight Kingdoms (stability -5%, political power -5%).
- Convene the Paruman Agung (administration cost, 120 days): Replaces The Eight Kingdoms with The Paruman Agung, raises Legitimacy and lowers Instability. Idea: The Paruman Agung (stability +5%, political power +3%).
- Restore the Subak Courts (strategic cost, 180 days, after The Paruman Agung has been convened): Adds The Subak Courts, raises Legitimacy and raises Capacity. Idea: The Subak Courts (stability +3%, consumer goods -2%).
- Open the Island Steamers (diplomatic cost, 120 days): Adds The Island Steamers and raises Capacity and Recognition. Idea: The Island Steamers (trade opinion +10%).
- Incidents: The Royal Cremation (`chaosx.nr6.254`), The Painters of Ubud (`chaosx.nr6.255`).

### Shan federation (IW-159)

- Starting problem: The Sawbwa States (stability -5%, political power -5%).
- Bind the Federal Council (administration cost, 120 days): Replaces The Sawbwa States with The Federated Shan States, raises Legitimacy and lowers Instability. Idea: The Federated Shan States (stability +5%, political power +3%).
- Extend the Lashio Railway (diplomatic cost, 120 days): Raises Capacity and Recognition.
- Regulate the Bawdwin Mines (strategic cost, 180 days, after The Federal Council has been given authority over the states): Adds The Bawdwin Mines, raises Capacity and lowers Recognition. Idea: The Bawdwin Mines (production speed industrial complex +5%).
- Incidents: The Poppy Fields (`chaosx.nr6.256`), A Disputed Succession (`chaosx.nr6.257`).

### Mon State (IW-161)

- Starting problem: A Language Without Schools (stability -3%, political power -5%).
- Seat the Council at Moulmein (administration cost, 120 days): Adds The Mon Federal Council, raises Legitimacy and lowers Instability. Idea: The Mon Federal Council (stability +5%, political power +3%).
- Open Mon Language Schools (strategic cost, 180 days, after The Mon Federal Council has been seated): Replaces A Language Without Schools with The Mon Schools, raises Legitimacy and raises Capacity. Idea: The Mon Schools (research speed +2%, stability +3%).
- Reopen the Moulmein Port (diplomatic cost, 120 days): Adds The Moulmein Port and raises Capacity and Recognition. Idea: The Moulmein Port (trade opinion +10%, consumer goods -2%).
- Incidents: The Monastery Lands (`chaosx.nr6.258`), The Tavoy Tin Mines (`chaosx.nr6.259`).

### Kachin state (IW-162)

- Starting problem: The Hills and the Plains (stability -5%, political power -5%).
- Convene the Duwas at Myitkyina (administration cost, 120 days): Replaces The Hills and the Plains with The Duwas' Council, raises Legitimacy and lowers Instability. Idea: The Duwas' Council (stability +5%, political power +3%).
- Raise the Kachin Levies (security cost, 120 days): Adds The Kachin Levies and raises Security. Idea: The Kachin Levies (army defence +10%).
- Open the Jade Mines Road (strategic cost, 180 days, after The duwas have met at Myitkyina): Raises Capacity and Recognition.
- Incidents: The Jade Traders (`chaosx.nr6.260`), The Mission Schools (`chaosx.nr6.261`).

### Laos (IW-166)

- Starting problem: The Kingdom and the South (stability -5%, political power -5%).
- Unite the Provinces under the Crown (administration cost, 120 days): Replaces The Kingdom and the South with The Royal Council, raises Legitimacy and lowers Instability. Idea: The Royal Council (stability +5%, political power +3%).
- Open the Mekong Route (diplomatic cost, 120 days): Adds The Mekong Route and raises Capacity and Recognition. Idea: The Mekong Route (trade opinion +10%, consumer goods -2%).
- Fund the Buddhist Institute (strategic cost, 180 days, after The provinces have been united under the crown): Raises Legitimacy and Capacity.
- Incidents: The Clerks of the Administration (`chaosx.nr6.262`), The That Luang Festival (`chaosx.nr6.263`).

### East Turkestan (IW-169)

- Starting problem: The Oasis Governors (stability -5%, political power -5%).
- Convene the Oasis Delegates (administration cost, 120 days): Replaces The Oasis Governors with The Oasis Assembly, raises Legitimacy and lowers Instability. Idea: The Oasis Assembly (stability +5%, political power +3%).
- Reopen the Caravan Roads (diplomatic cost, 120 days): Adds The Caravan Roads and raises Capacity and Recognition. Idea: The Caravan Roads (trade opinion +10%).
- Raise the Oasis Guards (security cost, 120 days): Adds The Oasis Guards and raises Security. Idea: The Oasis Guards (army defence +10%).
- Incidents: The Soviet Trade Agreement (`chaosx.nr6.264`), The Hami Grievances (`chaosx.nr6.265`).

### Inner Mongolia (IW-170)

- Starting problem: Banners and Settlers (stability -5%, political power -5%).
- Convene the Autonomy Council (administration cost, 120 days): Adds The Mongol Autonomy Council, raises Legitimacy and lowers Instability. Idea: The Mongol Autonomy Council (stability +5%, political power +3%).
- Settle the Banner Pastures (strategic cost, 180 days, after The Mongol Autonomy Council has been convened): Removes Banners and Settlers, raises Legitimacy and lowers Instability.
- Raise the Banner Cavalry (security cost, 120 days): Adds The Banner Cavalry and raises Security. Idea: The Banner Cavalry (cavalry attack +10%, cavalry defence +5%).
- Incidents: The Wool Buyers of Kalgan (`chaosx.nr6.266`), Envoys from Ulaanbaatar (`chaosx.nr6.267`).

### Ryukyu (IW-171)

- Starting problem: The Cycad Years (stability -5%, consumer goods +3%).
- Seat the Assembly at Shuri (administration cost, 120 days): Adds The Ryukyu Assembly, raises Legitimacy and lowers Instability. Idea: The Ryukyu Assembly (stability +5%, political power +3%).
- Relieve the Sugar Debts (strategic cost, 180 days, after The Ryukyu Assembly has been seated): Removes The Cycad Years, raises Legitimacy and lowers Instability.
- Open the Emigrant Bank (diplomatic cost, 120 days): Adds The Emigrant Remittances and raises Capacity and Recognition. Idea: The Emigrant Remittances (trade opinion +5%, consumer goods -2%).
- Incidents: The Dialect Placards (`chaosx.nr6.268`), Shuri Castle (`chaosx.nr6.269`).

### Samoa (IW-175)

- Starting problem: The Mau and the Administration (stability -5%, political power -5%).
- Convene the Fono of Faipule (administration cost, 120 days): Replaces The Mau and the Administration with The Fono of Faipule, raises Legitimacy and lowers Instability. Idea: The Fono of Faipule (stability +5%, political power +3%).
- Return the Reparation Estates (strategic cost, 180 days, after The Fono of Faipule has been convened): Raises Legitimacy and Capacity.
- Open the Apia Copra Market (diplomatic cost, 120 days): Adds The Apia Copra Market and raises Capacity and Recognition. Idea: The Apia Copra Market (trade opinion +10%, consumer goods -2%).
- Incidents: The Titles Court (`chaosx.nr6.270`), The Mau Procession (`chaosx.nr6.271`).

## Blocked rows

- IW-152 Riau (FVX) and IW-158 Pattani (GBX): their leadership resolution requires a sourced incumbent or claimant, or authentic material for an actual royal council, and forbids a generated dynasty member or institution. The Riau-Lingga and Pattani sultanates were abolished in 1911 and 1902, and no sourced 1936 claimant or council material is in the working tree.
- IW-153 Dayak federation (POK), IW-157 West Papua (WPG), IW-160 Karen state (GDX), IW-163 Chin state (GGX), IW-168 Hmong regional state (GLX), IW-174 Aotearoa Maori state (GRX) and IW-178 Papua regional federation (PNG): specific community variants with no planner gate; each needs a named community package.
- IW-164 Arakan or Rakhine (GHX): its public name and leadership must follow a named community settlement, and its reservation is unresearched.
- IW-165 Wa state (GIX) and IW-176 Tonga (GTX): no planner gate, loader or reservation, because each needs a distinct map state.
- IW-156 Moluccan federation: a vanilla route overlay by design.
- IW-172 Ainu state (ANU): its research restricts it to a named Ainu institution with a sourced leader or archival institution material, which the working tree does not have.

## Formables

FORM-36 Maritime Federation and FORM-37 Mainland Southeast Asian Federation are implemented at source under the accepted D31 contracts in `9e2837f8edc1633cd8e96415366821ca5dc16886`.
FORM-36 places MRX on its existing carrier and binds Aceh ATJ at 1050, the Bugis state FXX at 673 and Bali BLI at 1052.
FORM-37 places MSX on its existing carrier and binds Mon IAX at 994, Shan GCX at 999 and Kachin IBX at 998.
Both use explicit proposal replies, sovereign-member integration and two paid 180-day stages, as detailed in [the ready-formable contracts](systems/ready_formable_contracts.md).
Riau remains blocked, the Moluccan row remains a vanilla overlay, and Karen, Chin and Arakan remain blocked.
The three FORM-37 members share RG-MAINLAND-SE-ASIA-COARSE, and the Bugis state and Bali share RG-EAST-INDONESIA, so those members arrive in different waves.
The [signature source report](../../plans/006_independence_wave_plans/subagent_handoffs/signature_source_integration_20261007.md) retains native consent/cost/cleanup, production GUI and full-AI limits.

FORM-38 Polynesian League State retains Hawaii and Samoa, with Tonga and Aotearoa blocked.
It remains closed under its existing missing carrier, member/consent, territory, flag and commit contract.

## Level 3 signature modules

Aceh builds its school and port institutions, forms PUSA only after 5 May 1939, retires its merchant credit before opening the FORM-36 route, and preserves the vanilla roster. Mon can choose local federal councils or a central river office, then fund its Salween transport and border watch before offering a sovereign FORM-37 compact. A costed Mon school-delegate program is optional and does not gate FORM-37. See [the Event 006 signature modules](signature_modules.md) for the full focus, decision, formable and cleanup contract.
The ten Aceh and eleven Mon signature focuses are implemented at source in `9e2837f8edc1633cd8e96415366821ca5dc16886`, with the separate native, imported-layout, full-AI and grounded portrait gates retained.

## Assets

The rows reuse their registered or vanilla flags, names and leader portraits, shared Event 006 and vanilla idea pictures, the shared decision icons and vanilla report event pictures. No new sprite is registered.

## Focus source status (2026-10-08)

The accepted five-node regional groups for `ATJ`, `FUX`, `BLI`, `GCX`, `IAX`, `IBX`, `LAO`, `GMX`, `MEN`, `OKN`, `SAM` are implemented at source in `416688b8963ea0b1a47e3c8682b8125455cfca40`.
The [regional source report](../../plans/006_independence_wave_plans/subagent_handoffs/regional_focus_source_commit_20261007.md) records the parent-reviewed contract, imports, project interlocks and validation limits.
Definitions are in [006_independence_wave_regional_focus_b.txt](../../../common/national_focus/006_independence_wave_regional_focus_b.txt), imported by the existing shared Event 006 tree.
Project nodes reuse the completion helpers in [the regional package effects](../../../common/scripted_effects/006_independence_wave_east_asia_oceania_package_effects.txt) already used by [their paid decisions](../../../common/decisions/006_independence_wave_east_asia_oceania_decisions.txt), with project/focus locks and guarded capstone progression.
Imported-node geometry/connectors, native project behavior, full campaign AI and outstanding portrait gates remain open.

## Future plans

- Rights-cleared character or portrait work for the Aceh education route remains pending in the [portrait research handoff](../../plans/006_independence_wave_plans/subagent_handoffs/signature_portraits_20261006.md); the signature mechanics do not assign a new named character.
- Sourced institutional leaders for the six custom councils.
- Named community packages for the Dayak, Karen, Chin, Hmong, Papuan and Maori rows, and sourced claimants for Riau and Pattani.
