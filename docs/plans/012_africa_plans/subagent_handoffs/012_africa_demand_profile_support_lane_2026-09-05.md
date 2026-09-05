# Event 012 Gods of Africa — demand profile support lane

## Disposition

implemented

## Scope

The owner-local Gods demand profile now treats support equipment as a real African shortage alongside infantry equipment, fuel, manpower, industry, emergency relief, transport, and aircraft. The emergency lane also fails closed when the debt variable is absent, so a partially restored host is not interpreted as being in crisis.

## Changed surfaces

- `common/scripted_effects/012_africa_gods_effects.txt`
  - initializes and evaluates `gods_of_africa_need_support_equipment`
  - includes support equipment in priority selection, fallback selection, demand scaling, and demand preparation
  - accepts a support-equipment priority request
  - replenishes `africa_common_defence_stockpile` when an infantry-equipment demand is actually transferred
- `common/decisions/012_africa_gods_decisions.txt`
  - adds `gods_of_africa_prioritize_support`
- `localisation/english/012_africa_gods_l_english.yml`
  - adds the support-priority name, description, and effect tooltip
- `docs/events/012_africa/gods_of_africa.md`
  - records the support-equipment need lane, emergency fail-closed behavior, and reserve synchronization

## Evidence and limits

The existing payment and capacity helpers already support `support_equipment`; this tranche connects that family to the maintained need selector and host policy. The vanilla Elephantry visual remains unrelated and continues to be reused through `sprite = elephantry`. Focused Event 012 MCP lints should be rerun after this source change; the large workspace may still return deferred workspace-wide validation, which is not equivalent to live-game acceptance.
