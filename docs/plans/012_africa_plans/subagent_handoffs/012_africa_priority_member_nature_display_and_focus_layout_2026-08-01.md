# Event 012 priority-member nature display and focus layout handoff

## Scope

This bounded tranche improves the already-installed priority-member nature arsenal without adding a country tag, cosmetic carrier, action store, model, or Event 013 source change.

## Changes

- `common/scripted_localisation/012_africa_scripted_localisation.txt` now exposes `GetAfricaPriorityMemberNaturePowerName`, reading the registration-time `africa_priority_member_nature_power` ladder and returning a stable player-facing authority label.
- `localisation/english/012_african_union_l_english.yml` adds Trace, Low, Medium, High, Ancestral, and Unrecorded labels and shows the current band in the nature category, both player actions, and the launch tooltip.
- `common/national_focus/012_africa_priority_member_focus.txt` tightens the existing eight-node overlay from columns 10–30 to 16–24. The prerequisite graph, focus count, route logic, and package-aware effects are unchanged.
- `docs/events/012_africa/natural_disaster_weapons.md` and `docs/events/012_africa/overview.md` record the visible authority band and its presentation-only status.

## Validation

- `hoi4.focus_inspect` reports `longConnectorCount = 0`, no Event 012 focus diagnostics, and the same eight focuses.
- The focused Event 012 lint remains source-clean for this tranche. The large-workspace report is partial because workspace-wide helper projections are deferred.
- A static Event 012 audit confirmed six unique localisation keys, one scripted-localisation definition, balanced braces and quotes in touched script files, and UTF-8 BOM in the English localisation file.

## Remaining risks

The authority band is display-only and does not replace Event 013 severity or the shared action ledger. Live-save proof for low, high, and ancestral packages, rejected calls, cooldown cleanup, and quote rollback remains open. The generic focus inspector continues to report unrelated missing vanilla continuous-focus sprites outside this tree.
