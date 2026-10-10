# Goal: Complete Event 037 Mysterious People

Implement Event 037 from `docs/specs/037_mysterious_people_specs/`, starting with its README and the coding prompt, under `CLAUDE.md`.

Event 037 is Minor Repeatable, Chaos level `1`, a Medium member of the Sudden Abundance cluster (runtime ID 15), with entry `chaosx.nr37.1`.
Retire the legacy stub, which gives one country recruits and hints at aliens.

Each firing runs one world pass: every inhabited state with ordinary civilian owners gains real population, scaled by stage, through a neutral gain helper that removes the instant recruitable gain.
Each state stores a newcomer share, an unsettled backlog, and a settlement rate.
Ordinary losses need no callbacks because the share is proportional, and one hook in the civilian transfer primitive handles moves.
A monthly host pulse touches only countries with unsettled newcomers and at most three hotspots each.

The player sees newcomers in the country, Overpopulation Pressure from `0` to `100` in five stages, and a stance.
One Newcomers modifier gives a workforce bonus at low pressure and costs stability and construction at high pressure.
Hotspots at `60+` send food need to Famine and at `80+` request flight through Migration, using their public entry points only.

Evolutions at `200`, `400`, and `600` Chaos raise the grant scale, add zero Chaos, and respect disabled stages.
Decisions are two stances, a Registration Drive, Requisition, Emergency Housing, Roads and Water, and an Evolution III New City, plus one mission, Absorb the Newcomers.
No action targets people by origin.

Events are one manifestation report per human country, three evolution reports, a seventeen-event flavour pool with diversity memory, and a rewritten first-firing news event.
Never confirm an origin.
Direct Chaos comes only from four one-shot milestones.

Produce and wire the asset inventory and three achievements, write the event overview, and update the workbook through the catalog handoff.

Finish when every acceptance criterion and balance case is checked, and report anything unresolved.
