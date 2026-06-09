# Event 006 Foundation Tranche Handoff

This tranche converts Event 006 from a fixed three-country random release into a first-pass origin-gated independence wave framework. It does not complete the full Event 006 source-spec pack.

## Implemented

- Added Event 006 script constants for release-count tuning, startup setup, decision costs, and AI weights.
- Added Event 006 scripted triggers for origin separation, aftermath categories, committee decisions, and ordinary candidate entry.
- Added Event 006 scripted effects for release-count preparation, host aftermath marking, released-country setup, successful release registration, and congress opening.
- Reworked `chaosx.nr6.1` to:
	- prepare a release target from chaos tier variables
	- build package-family candidate pools before falling back to ordinary releasables
	- reject candidate tags carrying Event 005 Soviet Collapse origin, republic, breakaway, or high-chaos successor flags
	- reserve a host-owned protected state before each release attempt, preferring the capital when safe
	- skip candidates that would consume every host-owned state
	- mark protected host states with `independence_wave_host_survival_reserved` so later releases and border-commission claims do not consume them
	- require the host to keep a controlled-state floor before release
	- set Event 006 origin flags and package variables on released countries
	- apply host aftermath state and a capital ministry mission
	- record actual released countries for news text
- Added first-pass Event 006 idea, decision categories, host aftermath decisions, committee survival decisions, and congress participation.
- Added `independence_wave_liberation_provisional_tree` and load it only after Event 006 origin setup.
- Added route-lock ideas and helper effects for the civic mandate, officer mandate, national directorate, revolutionary committee, patron cabinet, congress support, and formation-ledger reveal.
- Added the revolutionary committee focus route with militia registration, commune supply cells, volunteer-office congress support, and an armed-independence capstone.
- Added the first Patron Ledger decision-category layer with adviser acceptance, rival patron balancing, broker exposure, dependency-clause rejection, arms corridors, treaty-debt conversion, shared cooldowns, patron-leverage effects, and AI weights.
- Added the first Formation Ledger route: regional compact preparation, proclamation, and post-formation ministry integration.
- Hardened the regional compact into a delegate-backed charter path with targeted compact invitations, member count tracking, anti-puppet clause support, charter timeout, secretariat recognition, and recovery after failed integration.
- Added the first Border Commission decision-category layer with border surveys, state-targeted parish claims, league arbitration, protected transfer petitions, dossier ultimatums, observer freezes, cooldowns, and state flags. These actions create claims and pressure rather than free cores or direct transfers.
- Added the first verified country-package path for Event 006 OGB / Volga Bulgaria:
	- high-chaos resolver seeding over Kazan and Cheboksary
	- Event 006 package id/type flags and Volga old-state memory spirit
	- Volga archive and old-name council focus hooks
	- Volga archive assembly, Volga-Bulgar proclamation, and Volga-Kama ministry integration decisions
	- origin-gated separation from Event 005 OGB content
- Added two more verified starter-package paths from the viability audit:
	- ASY / Assyria recognition congress over Mosul with Event 006 package flags, spirit, focus hook, and recognition decisions
	- DNZ / Danzig Free City over Danzig with Event 006 package flags, spirit, focus hook, and free-city board decisions
- Corrected the capital ministry mission semantics so mission failure triggers when the host no longer controls a capital ministry state, while timeout is the successful hold.
- Added player-facing localisation for the news text, decisions, categories, mission, and provisional committee.
- Added first-pass release dossier/detail state. This older handoff originally described per-release entries through the shared evolution-log pipeline; that wording is superseded by the current source-of-truth rule that actual Event 006 evolution rows are release-scale tiers starting no earlier than Gathering Storm, not per-country release progressions.
- Added formation milestone log entries for the implemented Regional Compact, Volga-Bulgar Assembly, Assyrian Recognition Congress, and Danzig Free City proof decisions.
- Added starter-package milestone log entries for the Volga archive, Assyrian recognition congress opening, and Danzig Free City board charter.
- Added `docs/events/006_independence_wave.md` with current behavior, Event 005 separation notes, reused icons, asset needs, and future work.
- Updated the Event 006 primary row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` with the Independence Wave description, evolution summaries, Liberations cluster assignment, and current in-progress status.

## Remaining Completion Blockers

- The candidate ladder now has package-family gates, scoring, and three verified starter packages: OGB/Volga, ASY/Assyria, and DNZ/Danzig Free City. Other completed country-package data is still missing. Dormant tags, additional city states, protectorates, additional historical-return packages, local-polity packages, hidden formables, and strange packages still need verified tags, state groups, leaders, assets, focus overlays, formation decisions, and AI route behavior.
- Release-count scaling uses a basic chaos-tier target floor. It does not yet use full score ladders, candidate quality, host risk shrinkage, or evolution-specific package pressure.
- Host survival now has a per-candidate protected-state pass that uses a temporary cleared event target, strongest-state proxy, and persistent protected-state flag consumed by later release and border target checks, but it is still skip-only around `release = TAG`. It is not yet a full reduced-territory shrink solver with batch value scoring.
- Package overlays are still mostly missing. The provisional focus tree is shared and currently has archive and land-congress clue gates plus small OGB/Volga, ASY/Assyria, and DNZ/Danzig mini-overlays.
- Package-specific formables are still mostly missing. The regional compact path plus the OGB/Volga, ASY/Assyria, and DNZ/Danzig proof decisions are the only implemented formation routes.
- Dossier board and scripted GUI implementations are still missing beyond decision-category surfaces. Patron Ledger and Border Commission exist as first decision-category layers, not full scripted GUIs.
- Event details content is wired for Event 006, the primary spreadsheet row is aligned to the current Independence Wave spec, and current release details use wave/release state without per-country evolution progression rows. Current report/news DDS and GFX wiring has since been completed. Future package and formation-route presentation, catalog rows, optional visual variants, animated assets, and final validation remain incomplete.
- No live-game scenario validation has been performed.

## Validation Performed

- Focused syntax hygiene with `git diff --check` on Event 006 files.
- Unsupported operator scan for `<=` and `>=`.
- Brace balance check over new and modified Event 006 script files.
- UTF-8 BOM check on Event 006 localisation.
- Localisation key scan for forbidden `:0` style keys.
- Localisation coverage check for added focus, idea, and decision ids.

## Notes For Next Tranche

The subagent completion-gap audit in `subagent_handoffs/006_independence_wave_completion_gap_audit.md` describes the pre-tranche implementation state. Its severe findings around missing origin, fixed release count, and unsafe host deletion are partially addressed by this tranche, but its broader completion blockers still apply.

The next implementation tranche should continue from `subagent_handoffs/2026_05_29_starter_package_viability_audit.md`: decide whether UGA may carry Buganda; keep Mapuche blocked until a real tag exists; keep PRA queued until the Event 005 railway package can be separated. The resolver still needs full candidate scoring, package-type assignment from verified package records, actual reduced-territory shrinkage if a safe implementation surface is chosen, broader cleanup hooks, future package and formation event-log milestones, asset wiring, and super-event/achievement support.
