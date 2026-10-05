# Live playtest report, 3–5 October 2026

The game ran from a QA snapshot of the repository (`C:\hoi4_qa\chaos_redux`), refreshed from `HEAD` before each round.
The last snapshot was taken at `fa833647e` plus `e08c1815f` and the texture repack `51f2eed3f`.
Debug launches were used for setup and map filming; the interface takes, the mechanics-guide captures and most system checks were made in a normal launch without `-debug`.

Bugs found and their status are in `bugs.md` (B001–B041). Per-item coverage is in `coverage.csv`.

## Startup

- A clean main menu was reached on every launch after the startup fixes of 3 October.
- The 4 October snapshot showed one new load error (B029, Event 014 siege trigger), fixed in `e08c1815f`.
- The 5 October snapshot shows five load or runtime error sources introduced by the takeover commits (B033) and the biological sabotage scope error (B030); all are routed to their owners. None blocks loading.

## Systems

| System | Result | Notes |
| --- | --- | --- |
| Settings | pass | Every section, event selection, Force Trigger Mode, timer window and chaos value update work. |
| Event Logs | fail | Events, Evolutions, Clusters and Event Details work. History stays empty after events fire (B036). Cluster Details overlaps one line (B038). |
| Chaos Meter | pass | All five tabs, the Air Cleanliness source details, the condemnation record and the Deaths cause tooltip work. Air Cleanliness still prints "-0.000%" (B010). |
| Triggerable Scenarios | fail | All 17 scenarios launch. Every Banner Rises releases no country (B032). The Hunger Lines starts no famine (B040). |
| Super-events | pass | Death, Fallout and Disaster Barrage super-events show art, quote and music. |
| Chaos Warfare | partial | The grand doctrine adopts, the release-policy decisions and raid categories work. No raid was run (needs a war target). |
| Repression and camps | not covered | The camp windows were not reached in these saves. |
| Famine and migration | fail | No famine starts (B040). |
| Air Cleanliness, Air Winter, Fallout | pass | The Fallout sweep, blackout world and Air Winter map work. |
| Condemnation | pass | Records, sanctions and penalties show after nuclear use. |
| Units and models | pass | All 38 custom models were filmed in game. Two chrome textures were fixed (B031); the Feast Cohort texture needs a provider download. |
| Achievements | pass | Achievements unlock in game. |
| Help window | pass | Opens with five tabs. |
| Map modes | fail | Air Winter, Famine and Migration recolour; Civilian Deaths, Contamination and Terror Activity draw nothing (B037). |

## Scenarios

| # | Scenario | Result |
| --- | --- | --- |
| 001 | Zombie Apocalypse | Launches; hordes spawn and declare war. Impassable-state spawn fixed (B023). |
| 002 | Army of Clones | Launches. |
| 003 | Soviet Collapse | Launches; the Union breaks into many states. |
| 005 | The World in Fury | Launches. |
| 006 | Death | Launches; the Death country appears with its focus tree and diplomacy view. |
| 007 | Disaster Barrage | Launches; Abnormal Disaster Path window works (B035 art gaps). |
| 008 | Every Banner Rises | Fails silently (B032). |
| 009 | Coalition Unmasked | Launches. |
| 010 | The Hunger Lines | Launches but no famine starts (B040). |
| 011 | Africa Is One | Launches; the host keeps its vanilla tree (routed to 012). |
| 012 | Black Plague Unbound | Launches. |
| 013 | The Unbidden Muster | Launches. |
| 014 | Fallout | Launches; the strike sweep and blackout work. |
| 015 | Missile Age | Launches. |
| 016 | Global Jihad | Launches. |
| 018 | The Fracture Cascade | Launches. |
| 019 | Assassin Network | Launches. |

## Events

Forced from Settings: Event 024, Event 028 (Asteroid Incoming: the strike choice works and the in-game impact lands on the chosen state; its window shows the blocked description while offering valid targets, routed to 028) and the evolutions of Event 010 (Death).
The remaining "Needs Testing" events (1–21, 26, 29, 35, 39, 42) were not run one by one in this round; they stay pending in `coverage.csv`.

## Artifacts

- Mechanics guide images and recordings: `docs/images/mechanics/`.
- Teaser screenshots and feature notes: `docs/content_dump/` (not in git).
- Saves used: `trailer_*`, `qa_scn*`, `qa_fo_apr`, `qa_cxt_base`, `qa_show_ar*` in the user's save folder.
