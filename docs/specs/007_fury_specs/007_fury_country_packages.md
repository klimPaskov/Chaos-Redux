# Event 007 Fury Country Package Matrix

## Package model

Fury does not create one bespoke tag. It transforms a selected existing AI minor into a temporary event-created Fury actor. This keeps the event dynamic and avoids hardcoded examples.

Because the candidate can be almost any valid small AI minor, the country package must be generic in script but specific in play through ideas, decisions, focus tree, AI, event log context, and route naming.

## Dynamic Fury country package

| Surface | Required design |
| --- | --- |
| Tag | existing selected AI country |
| Origin flag | `fury_origin_event_007` |
| Active flag | `fury_country` |
| Player rule | never set on player country |
| Base flag | keep existing country flag by default |
| Leader | keep existing leader by default |
| Focus tree | load shared Fury tree only if the event marked the country |
| Ideas | add staged Fury idea package |
| Decisions | add Fury campaign category |
| Faction | no faction at baseline, Fury Pact from Evolution II onward |
| Units | dynamic starting force and weekly growth |
| Compliance | grants controlled compliance after victories, no instant mass cores |
| Event log actor | selected Fury country |

## Politics

Fury should not become a normal ideology sandbox. It can keep its old ideology while gaining a special event identity. The focus tree provides a command fork instead of normal democratic, communist, fascist, and monarchist paths.

Route identities:

| Route | Visible identity |
| --- | --- |
| General Staff Dictate | military command state |
| March Administration | conquest administration state |
| Joint Campaign Office | cooperative Fury member |
| All Fronts Open | high-chaos war command |
| Continental Mandate | no-neighbor consolidation or world-end leader |

## Cosmetic naming

Use optional cosmetic names only when implementation can safely apply them without breaking existing country identity.

Possible dynamic names:

| Condition | Name direction |
| --- | --- |
| baseline Fury | `[Country] March Command` |
| first victory | `[Country] Frontier Command` |
| no-neighbor | `[Country] Continental Authority` |
| world-end leader | `Fury Command` or `The Borderless Command` |
| Fury Pact leader | `[Country] Campaign Office` |

If dynamic cosmetic names are too unsafe for broad country selection, the implementation may keep normal country names and use event log text, ideas, and decisions for identity. This is an accepted design limit, not a missing feature.

## Starting force package

Fury must not start empty. Starting forces scale from the selected country and current event intensity.

Template families:

| Template family | Use |
| --- | --- |
| Fury Militia Columns | weak low-equipment baseline units |
| Border Shock Detachments | first-war attack units |
| Depot Guards | post-victory holding units |
| March Battalions | standard growing-force units |
| Joint Campaign Corps | Evolution II cooperation units |
| All-Front Assault Columns | Evolution III simultaneous-war units |
| Continental Guard | no-neighbor consolidation units |
| World-Fury Cadres | world-end branch units |

Dynamic scaling:

| Situation | Force result |
| --- | --- |
| one-state low industry | few militia and shock units |
| high chaos | more units and better templates |
| Evolution I | stronger initial units |
| Evolution II | two countries each get moderate packages |
| Evolution III | three countries each get stronger packages |
| low manpower | fewer regulars, more weak militia |
| low equipment | weak template quality and possible equipment debt |
| captured capital | one-time depot unit option |
| high occupation strain | fewer new units until administration improves |

## Unit growth pathway

Fury gains units through:

- weekly active Fury pulse
- military focus unlocks
- captured depot decisions
- partner reserve decisions under Evolution II
- all-front emergency decisions under Evolution III
- no-neighbor consolidation forces
- world-end ignition reserves

Every unit source should have a clear story and condition. Avoid repeated flat `add two infantry divisions` style rewards.

## Faction package

Baseline Fury does not need a faction.

Evolution II unlocks a faction or coordination framework.

Possible names:

- Fury Pact
- March Council
- Campaign League
- Borderless Pact

Faction rules:

- only Fury countries can join automatically
- non-Fury countries can join only through explicit future design, not baseline
- Fury countries avoid declaring on each other while coordination exists
- if only one Fury country remains, coordination decisions close
- world-end branch makes the main Fury country the faction leader if valid

## Asset identity

Because Fury can select many existing countries, do not create bespoke flags or portraits for every candidate.

Required shared assets:

- Fury idea icon
- Veteran Fury idea icon
- Joint Fury idea icon
- All-Front idea icon
- Continental Mandate idea icon
- Fury decision category icon
- decision icons for war preparation, depot seizure, integration, coring, coordination, and world-end preparation
- focus icon families for the shared tree
- Fury Pact faction emblem
- first victory news image
- Fury major super-event image
- Fury world-end super-event image

Optional assets:

- fictional Fury Staff Council portrait for high-chaos routes
- animated Fury route emblem if the implementation adds scripted GUI or visual route states

## Compatibility rules

- do not replace a meaningful existing focus tree unless the country is marked by Event 007
- do not overwrite base flags for existing countries
- do not generate real leader portraits
- do not create a cosmetic identity that hides who the selected country originally was unless a major route justifies it
- cleanly remove Fury content if the country capitulates or loses active Fury state
