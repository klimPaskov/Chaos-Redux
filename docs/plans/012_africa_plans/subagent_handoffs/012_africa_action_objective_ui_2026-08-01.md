# Event 012 action objective UI tranche

Date: 2026-08-01

## Scope

This bounded tranche exposes the already-quoted action objective class in the existing Charter Court summary. It changes no action constants, decisions, costs, durations, targets, tags, country definitions, or model consumers.

## Changes

- `common/scripted_localisation/012_africa_charter_gui_scripted_localisation.txt` adds `GetAfricaCharterActionObjectiveName`, mapping the seven shared objective enums to player-facing labels with a safe `No timed review` default.
- `localisation/english/012_africa_charter_gui_l_english.yml` adds the seven labels and places the objective beside the selected proposal and action family. The human-facing window is called the Charter Court and regional courts rather than a leader council surface.
- `docs/events/012_africa/action_duration_objective_contract.md` records the UI contract and its fallback behavior.

The displayed value reads `africa_quote_objective`, which is written by the existing quote refresh path from the 102-row action contract. It never infers objective class from opinion, target identity, or a generic duration band.

## Validation

- The seven objective localisation keys appear exactly once and the scripted-localisation function appears once.
- The edited localisation file retains UTF-8 BOM encoding.
- `git diff --check` reports no whitespace errors for the tranche.
- `hoi4.gui_inspect` for `africa_charter_window` under scenario `default` returned `GUI_INSPECTED`. Its remaining diagnostics are workspace-global or pre-existing; no Event 012-specific missing window or sprite failure was introduced by this text-only surface change.

## Remaining boundary

Live GUI click, text-fit, and branch-aware render acceptance remain open. The constitutional route identifier `council_of_crowns` remains a technical and matrix identity; this tranche only removes council wording from the primary Charter presentation and does not rename that accepted route or create a new identity.
