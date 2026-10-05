# Event 006 West and Central Africa packages

Agent decision D27 admits four West and Central Africa rows through the regional framework engine (`regional_framework_packages.md`), beside the bespoke IW-093 Asante, IW-095 Dahomey and IW-098 Sokoto packages admitted earlier. The remaining rows stay blocked for the reasons below.

## Admitted rows

| Row | Tag | Anchor | Depth | Leadership | Government routes | Power centres |
| --- | --- | --- | --- | --- | --- | --- |
| IW-097 Oyo | DSX (X-tag) | 558 Nigeria | Registry Level 3, admitted with a Level 2 layer | The Oyo Mesi and Council of Ministers, chaired by the leader the game appoints | constitutional, popular council, traditional, emergency, patron client | traditional authority and assembly |
| IW-099 Kanem-Bornu | DUX (X-tag) | 901 Borno | Level 2 | The Council of the Shehu of Bornu, chaired by the leader the game appoints | constitutional, traditional, emergency, patron client | traditional authority and assembly |
| IW-106 Aro Confederacy | EBX (X-tag) | 900 Benue | Level 1 | The Confederated Council of the Aro Towns, chaired by the leader the game appoints | constitutional, popular council, traditional, emergency | central government and provinces |
| IW-107 Biafran regional state | BIA | 900 Benue | Level 1 | Vanilla BIA roster; its democratic government opens under the leader the game appoints | constitutional, popular council, emergency, patron client | labour councils and ministries |

Radical sovereignty is excluded for all four. Every Nigerian row, including Dahomey and Sokoto, shares RG-NIGERIA-COARSE, so a wave releases at most one of them. EBX and BIA share the Benue anchor 900; the shared group keeps them apart within a wave, and once one owns the state the other's anchor is no longer available. BIA is released by `release` from its vanilla core; DSX, DUX and EBX are created as dynamic countries with their registered flags and names.

## Level 2 layers

### Oyo (IW-097)

- Starting problem: The Oyo Mesi Deadlock (stability -5%, political power -10%).
- Seat the Oyo Mesi in Council (administration cost, 120 days): replaces the problem with The Oyo Mesi in Council (stability +5%, political power +5%); Legitimacy up, Instability down.
- Reconcile Ibadan (diplomatic cost, 120 days): Capacity and Recognition up; opens the congress of towns.
- Raise the Alaafin's Horse Guard (security cost, 120 days): The Alaafin's Horse Guard (cavalry attack +10%, cavalry defence +5%); Security up.
- Convene the Yoruba Towns (strategic cost, 180 days, after Ibadan): Recognition and Legitimacy up.
- Incidents: The Ibadan Toll Gates (`chaosx.nr6.210`), The Cocoa Buyers (`chaosx.nr6.211`).

The texts treat Oyo as one Yoruba state among several and never present it as speaking for all Yoruba.

### Kanem-Bornu (IW-099)

- Starting problem: The Lake Trade in Decline (trade opinion -10%, stability -3%).
- Seat the Shehu's Council at Maiduguri (administration cost, 120 days): Legitimacy up, Instability down; opens the lake routes.
- Reopen the Lake Chad Routes (diplomatic cost, 120 days, after the council): replaces the problem with The Lake Chad Trade (trade opinion +10%, stability +3%); Capacity and Recognition up.
- Raise the Kanembu Horse (security cost, 120 days): The Kanembu Horse (cavalry defence +10%); Security up.
- Incidents: The Scholars of Kukawa (`chaosx.nr6.212`), Salt from Bilma (`chaosx.nr6.213`).

## Blocked rows

- IW-094 Fante (DPX), IW-103 Luba (DYX) and IW-104 Lunda (DZX): no planner gate, loader or reservation, because each needs a distinct map state.
- IW-096 Benin Kingdom: no planner gate, and its registered tag BIA is the carrier of the admitted IW-107; a Benin City anchor needs its own binding.
- IW-100 Hausa Federation (DVX): formable or route only, and its anchor 902 is the anchor of the admitted IW-098 Sokoto.

## Formables

FORM-24 West African Federation and FORM-25 Sahel Confederation remain closed: their profiles exist for discovery, but neither has a carrier tag, member contract, consent rule, territory proof or flag, and neither is in the shared commit allowlist. Oyo, Kanem-Bornu, the Aro Confederacy and Biafra register no formable family. FORM-26 Kongo Basin Federation has no admitted member.

## Assets

The rows reuse their registered or vanilla flags and names, shared Event 006 and vanilla idea pictures, the shared decision icons and the vanilla report pictures `GFX_report_event_generic_read_write`, `worker_protests` and `merchant_ship_01`. No new sprite is registered.

## Future plans

- The Oyo signature module: the Alaafin Siyanbola Ladigbolu I with a sourced portrait, the Oyo Mesi balance as a power-struggle layer and city-state relations.
- Sourced leaders or institutional characters for the Bornu, Aro and Oyo councils.
- FORM-24 and FORM-25 carrier contracts once their member rows exist.
