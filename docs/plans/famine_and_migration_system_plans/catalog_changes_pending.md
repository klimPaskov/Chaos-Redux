# Famine and migration catalog changes pending

Disposition: accepted and queued.
Acceptance basis: round-2 lead decision 3 (Hunger Lines owner boundary) and agent decision 18 in `agent_decisions_2026-10-04.md`.
Reason queued: the workbook and its CSV exports are not edited by this owner, and the SCN-010 description localisation belongs to the Event 014 owner, so the catalog wording must follow that owner's in-game text.

## SCN-010 The Hunger Lines

Source change: `famine_apply_hunger_lines_scenario_pressure` (committed with decision 18) gives every region the scenario seizes a food shock, a 120-day food crisis and refugee flight.

Requested `Details` addition, after the five type paragraphs:

> In every type, the regions the Hunger Lines seize run short of food and their people begin to flee. At the lowest intensity supply is strained at first and turns into acute shortage once local stores run out; at Maximum those regions slide toward famine within weeks unless relief arrives.

Requested `Intensity Scaling` addition to the Maximum line:

> Seized regions fall into famine within weeks unless relief arrives.

Event 014 owner action: add the same sentence to the SCN-010 scenario description localisation, so the catalog row matches the in-game text, then run `python .tools/export_event_catalog_csv.py` after the workbook update.
