# Event 012 Gods of Africa demand-band monotonicity

## Disposition

Implemented. This is a narrow correction to the accepted conduct-aware demand contract.

## Finding

`gods_of_africa_calculate_demand_amount` assigns `punitive_band` first, then evaluates the independent severe-strength and emergency-need branches. Without a current-band guard, a participant who had earned a punitive quote could be downgraded to severe or emergency merely because those later conditions were also true.

## Change

The severe branch now runs only while the current contract band is below `severe_band`. The emergency branch now runs only while the current band is below `emergency_band`. Ordinary and severe quotes can still escalate when maintained African need requires it, but a punitive conduct quote remains authoritative.

## Evidence

- `gods_of_africa_contract_band` is initialized before the ladder and is frozen into the demand contract by `gods_of_africa_create_demand_contract`.
- `punitive_band` is the highest defined demand band, while `emergency_band` is lower; the new guards preserve that ordering.
- The change does not alter amount scaling, deadlines, capacity checks, or the punishment capability ceiling.

## Validation boundary

The parent reran the focused HOI4 MCP Event 012 inspection after this edit. The returned projection remains aggregate-partial because large helper/lifecycle analysis is deferred, with no focused blocking blocker. Live balance and save-state verification remain owner-owned.
