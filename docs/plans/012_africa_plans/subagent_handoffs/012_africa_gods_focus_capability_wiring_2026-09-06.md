# Event 012 Gods of Africa focus capability wiring handoff — 2026-09-06

## Disposition

`implemented` for the narrow capability-wiring tranche. This handoff records the source changes made after the Event 012 focus and completion audits. It does not promote the wider Event 012 package to complete: MCP weighted-logic evidence, live validation, technology evidence, cosmetic flags, and other package-level blockers remain open in the current completion audits.

## Scope

The Event 012 Gods overlay remains in `africa_continental_focus_tree` and the core tribute loop remains usable without completing the overlay. The patch makes accepted focus rewards alter existing owner-ledger behavior instead of leaving the capability flags as presentation-only witnesses.

## Gameplay changes

- `common/scripted_effects/012_africa_gods_effects.txt` now lets `gods_of_africa_focus_needs_profile_unlocked` open the emergency-relief need lane at the medium debt band while retaining the high-debt threshold for hosts without that focus.
- The reciprocal and exaction focus route flags now feed the existing demand-scale doctrine adjustment as a fallback to the durable doctrine variable. An `else_if` keeps a malformed dual-route state from applying both doctrine deltas.
- The logistics focus flag already changes transport need detection to accept either a convoy or train shortfall and reduces the next-demand cooldown through the shared constant-backed timer path.
- The arsenals focus flag already adds the host stability reward to a successful support-equipment transfer. The reserve, relief, and expedition flags already alter the protection transaction's cooldown or defensive rewards.
- `common/scripted_triggers/012_africa_gods_triggers.txt` keeps the last-sentence focus as an explicit gate inside the full catastrophe trigger. The ordinary core loop and lower punishment tiers do not depend on the focus tree.
- `common/decisions/012_africa_gods_decisions.txt` exposes priority lanes from live need variables and gates leniency, protection, offender marking, and settlement actions behind their matching focus capability or completed doctrine/settlement state. The ordinary reconciliation action remains available to an active host without an unrelated focus gate.

## Constants and documentation

The shared timer and transaction values used by the logistics, reserve, relief, and expedition effects are in `common/script_constants/012_africa_gods_constants.txt`. The player-facing behavior and the vanilla-elephantry visual boundary are described in `docs/events/012_africa/gods_of_africa.md`.

## Evidence and limits

Source inspection confirms the focus flags have gameplay consumers in the effects, triggers, and decision files listed above. The existing focus MCP inspection/render reported no blocking diagnostics but did report layout warnings; the probability compare route remains unavailable (`PROBABILITY_SURFACE_EMPTY`), and live in-game validation is user-owned. Recognition, territory, sponsorship, sanctions, reach, and other nonmaterial focus flags remain documented route witnesses without new recurring demand families in this tranche; adding those families requires real one-time transaction effects and anti-repeat state rather than a presentation-only selector.

## Elephant visual boundary

No elephant model work is part of this tranche. `chaosx_elephant` continues to use the normal vanilla `elephantry` sprite/entity family, with no active custom Meshy elephant model, entity, or skeletal action package.
