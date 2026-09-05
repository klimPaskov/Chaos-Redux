# Event 012 maintained-need dispatch gate — 2026-09-05

## Disposition

Implemented in the current Event 012 source. The patch is bounded to the Gods-of-Africa demand preparation path and does not alter elephant model reuse or other decision categories.

## Change

`gods_of_africa_prepare_demand_for_participant` now calls `gods_of_africa_select_demand_family` only when the host's maintained land-equipment, fuel, manpower, industry, emergency, transport, or aircraft need flag is active. A configured priority wins only when it matches one of those active need lanes; otherwise the deterministic emergency, fuel, manpower, industry, transport, aircraft, then land fallback chooses an active lane. Priority values for optional families therefore cannot manufacture a demand with no corresponding maintained need.

## Evidence

- Source: `common/scripted_effects/012_africa_gods_effects.txt`, `gods_of_africa_prepare_demand_for_participant`.
- Documentation: `docs/events/012_africa/gods_of_africa.md`, Tribute loop section.
- Event MCP lint was rerun against `chaosx.nr12.603` after the patch. The adapter returned `EVENT_INSPECTED_PARTIAL` with no blockers; workspace-wide helper projection remained partial because the repository exceeds the inline source inventory.
- The vanilla elephant path is unchanged: `common/units/012_africa_elephant_forces.txt` still binds `chaosx_elephant` to `sprite = elephantry`.

## Limits

The gate uses the seven maintained need flags already owned by Event 012. Recognition, territory, alliance access, and other optional demand-family scaffolding remain separate until their own need signals are implemented.
