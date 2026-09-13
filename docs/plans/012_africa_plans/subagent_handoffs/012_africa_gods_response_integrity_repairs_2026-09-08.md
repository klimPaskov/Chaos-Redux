# Event 012 Gods of Africa response-integrity repairs

## Disposition

Implemented as a narrow Africa-only correctness repair. The accepted broader protection scope remains queued and is documented as incomplete rather than promoted by this handoff.

## Changed surfaces

- `common/scripted_effects/012_africa_gods_effects.txt`
  - Restores the substitute entry path through the frozen slot wrappers, releases active-demand and priority-offender counters during archival, pardon, cleanup, cancellation, and settlement, and clears stale participant presentation and memory flags at lifecycle boundaries.
  - Adds the public-pardon and offense-escalation host effects, and consumes the defensive-preparation flags in bounded punishment outcomes.
  - Makes the accepted recognition, territory-return, support-termination, and strategic-resource lanes real demand families with live capacity checks, guarded state transfer or steel-rights grant, and participant outcome flags.
- `common/scripted_triggers/012_africa_gods_triggers.txt`
  - Closes response actions during war, validates current demand contracts, permits bounded no-demand defiance, and adds explicit gates for public pardon and offense escalation.
- `common/decisions/012_africa_gods_decisions.txt`
  - Routes mission timeout to failed demand, prevents refusal and substitute actions from appearing outside their valid state, exposes host pardon and escalation actions, and shows the protection transaction cost.
- `common/ai_strategy/012_africa_gods_ai_strategy.txt`
  - Uses the vanilla `pp_spend_priority` and `force_build_armies` strategy tokens instead of unsupported strategy keys.
- `localisation/english/012_africa_gods_l_english.yml`
  - Describes the current extension, pardon, escalation, resource-rights icon, and protection-cost surfaces.
- `docs/events/012_africa/gods_of_africa.md`
  - Records the implemented protection boundary, focus-capability limitations, and validation blockers.

## Behavior covered

The substitute action now reaches one of the three frozen capacity-checked slots and cannot be offered after the contract expires or during war. An expired response fails the demand instead of being reclassified as a refusal, while the owner tick can still record treaty breaks and close the contract. Pardon and escalation are explicit host actions with current-participant gates; pardon lowers Wrath without erasing hidden offense history, and escalation uses the normal punishment ceiling. Defensive preparation now has bounded consumers in punishment resolution. Archive, cancel, settlement, and pardon paths release host counters and stale participant presentation state idempotently. Focus-gated diplomatic lanes resolve through the same immutable contract and payment path: recognition grants a participant flag, territory return selects and transfers one controlled African host-core state only when the participant still owns one, sponsorship demands record support termination, and the resource lane grants the host real steel rights from one participant-controlled state. Judgment reach now gates offender escalation, sanctions add a bounded diplomacy memory during punishment, and sanctuary/security protection can issue a guarantee or military-access compact.

## Validation

- The focused Clausewitz parser remains brace-balanced and quote-balanced for the edited Event 012 scripts.
- Focus MCP inspection remains `status=ok` with `validation.passed=true` for the 300-node Africa tree.
- Event MCP inspection is the installed aggregate partial lint route for this large workspace and remains non-blocking only for the focused source; it is not a substitute for live scenario validation.
- The probability adapter remains score-only and incomplete, so no normalized odds or compare claim is made.
- No non-Africa decision category or generic recurring world scan was changed.

## Remaining limits

The accepted protection families beyond the equipment/fuel/PP package and the remaining transport, intelligence, reconstruction, disaster, migration, and trade lanes still require an owner-approved implementation tranche. Live GUI, save-state, and full probability acceptance remain user- or tool-capability-owned.
