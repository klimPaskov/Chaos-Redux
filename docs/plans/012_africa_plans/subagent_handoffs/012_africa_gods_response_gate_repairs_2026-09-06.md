# Event 012 Gods of Africa response-gate repairs

## Disposition

`implemented` in the current Event 012 source, with live game validation and the remaining MCP scenario limitations still open.

## Scope

This handoff records the narrow response and presentation repairs applied after the Event 012 decision and probability audits.

The elephant formation is explicitly out of this custom-model scope because `chaosx_elephant` reuses the installed vanilla `elephantry` sprite and animation family.

## Repairs

- Transport payment now chooses convoys only when the full hidden capacity requirement, including the protected operating reserve, is available; otherwise it uses trains.
- Transport substitutes now use the same convoy-or-train capacity rule as ordinary payment.
- Permanent defiance and return-to-demand are limited to a live, unexpired demand contract, so an expired contract cannot bypass the owner failure path or reopen a stale response.
- The first-failure safety ceiling now requires zero prior refusals, failed demands, offenses, and punishment receipts, while still excluding a recent extreme punishment.
- The aircraft response cost uses the vanilla fighter-equipment icon rather than the unrelated air-experience icon.
- Continental focus activation refreshes the continental focus layout, and the continental reserve focus requires Evolution II as documented by its route.

## Files

- `common/scripted_triggers/012_africa_gods_triggers.txt`
- `common/scripted_effects/012_africa_gods_effects.txt`
- `common/decisions/012_africa_gods_decisions.txt`
- `common/national_focus/012_africa_continental_focus_tree.txt`
- `localisation/english/012_africa_gods_l_english.yml`

## Remaining boundary

The host decision category still has a broad priority and targeted-action surface, and the focus overlay contains capability flags whose downstream gating needs an explicit route decision before further redesign.

The required MCP event, GUI, and weighted scenario evidence remains partial where the installed adapters cannot bind the dynamic host and participant scopes, and user-owned live validation remains outstanding.
