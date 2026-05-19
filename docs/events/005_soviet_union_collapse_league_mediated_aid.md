# Event 005 League-Mediated Aid

League-mediated aid is the foreign intervention path that sends support through the Free Republics' League instead of directly binding one republic to one sponsor.

## Flow

1. A foreign patron uses `soviet_collapse_route_aid_through_league_logistics` from `soviet_collapse_foreign_patron_category`.
2. The target must be a breakaway republic and a Free Republics' League member.
3. The sponsor must either have a normal aid route to the target or qualify for the League aid channel through relief, reconstruction, or conference-style patron behavior.
4. The target still runs the normal foreign-aid acceptance gate, so League membership does not force a republic to accept every sponsor.
5. The sponsor pays political power, fuel, trains, and convoys. Costs scale by ordinary, regional, and major target tier.
6. The target receives distributed equipment, logistics influence, a small arms influence increase, independence resilience, League cohesion, recovery progress, and reduced patronage risk.
7. Moscow's crisis state gains foreign and League pressure because the League has proven it can distribute outside aid.

## Balance Role

Direct corridors raise logistics and arms influence but also raise patronage risk. League-mediated aid trades higher negotiation and transport cost for less target dependency, better League cohesion, and stronger independence resilience. It is most attractive when a republic already has a dangerous patronage profile or when a sponsor wants to support the League without opening a direct client track.

## Files

- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/scripted_localisation/005_soviet_collapse_scripted_localisation.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `.tools/verify_event005_completion_gate.py`

## Icons

No new icon is required. The decision reuses `GFX_decision_soviet_collapse_foreign_trade` from `interface/005_soviet_collapse_icons.gfx`, which already has a working DDS asset in the Event 005 decision icon package.

Future extension can add a dedicated League logistics decision icon under `gfx/interface/decisions/decision_soviet_collapse_league_logistics.dds` and register it in `interface/005_soviet_collapse_icons.gfx`, but the current gameplay surface does not depend on new art.
