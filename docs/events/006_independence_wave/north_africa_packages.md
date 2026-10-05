# Event 006 North Africa and Sahara packages

Agent decision D26 admits two North Africa and Sahara rows through the regional framework engine (`regional_framework_packages.md`). Cyrenaica keeps its existing vanilla-overlay package, and the remaining rows stay blocked for the reasons below.

## Admitted rows

| Row | Tag | Anchor | Depth | Leadership | Government routes | Power centres |
| --- | --- | --- | --- | --- | --- | --- |
| IW-083 Rif | RIF | 290 Spanish Africa | Level 2 | Vanilla Muhammad ibn Abd el-Krim al-Khattabi, President of the Rif Republic from 1921 to 1926 | constitutional, traditional, emergency, patron client | central government and provinces (the republic and the tribes) |
| IW-086 Tripolitania | DHX (X-tag) | 448 Tripoli | Level 1 | Institutional council in the tradition of the 1918 Tripolitanian Republic; the game appoints its leader | constitutional, popular council, traditional, emergency, patron client | traditional authority and assembly |

Radical sovereignty is excluded for both. RIF is released from Spain by the vanilla `release` path, because state 290 carries a RIF core. DHX is created as a dynamic country from its reserved tag, with its registered flags and names.

## Rif Level 2 layer

- Starting problem: The Tribal Levies (stability -5%, organisation -5%).
- Convene the Rif National Assembly (administration cost, 120 days): Legitimacy up, Instability down; opens the levy and network projects.
- Unify the Tribal Levies (security cost, 120 days, after the assembly): replaces the problem with The Rif Regular Army (organisation +5%, stability +3%); Security greatly up, Instability up.
- Fortify the Mountain Redoubts (strategic cost, 180 days): The Mountain Redoubts (defence +10%); Security up.
- Restore the Ajdir Network (administration cost, 120 days, after the assembly): Capacity and Recognition up.
- Incidents: Veterans of Anual (`chaosx.nr6.208`), The Mines of Uixan (`chaosx.nr6.209`).

The decision weights favour the assembly first, the regular army and the redoubts under a severe host threat, and the network on quieter routes.

## Blocked rows

- IW-084 Kabylia (DFX), IW-087 Fezzan (HYX), IW-090 Wadai (DLX) and IW-092 Amazigh Atlas (DNX): no planner gate, loader or reservation exists, because each needs a distinct map state the current map does not have.
- IW-085 Cyrenaica: a vanilla LBA identity overlay by design (`can_plan_independence_wave_package_iw_085` is always false). Its overlay package already exists in the minor overlay registry.
- IW-088 Tuareg Confederation (DJX): no planner gate, an unresearched reservation, and its candidate states 514 and 515 have forced ownership links in the installed map history.
- IW-089 Darfur (DKX): its anchor 767 North Darfur has `force_link_ownership_to = 551` (Khartoum) in the installed map history, so it cannot be owned apart from Khartoum and a release would fail.
- IW-091 Toubou state (DMX): an unresearched reservation with no history or names, and its anchor 775 also has a forced ownership link.

## Assets

The rows reuse existing assets: the vanilla RIF flags, names and leader portrait, the registered DHX flags and names, shared Event 006 and vanilla idea pictures, the shared decision icons and the vanilla report pictures `GFX_report_event_soldiers_parade` and `generic_sign_treaty1`. No new sprite is registered.

## Future plans

- A sourced leader for the Tripolitanian council.
- A five-node focus group for the Rif.
- A FORM-22 Maghreb union contract once a second Maghreb member exists.
