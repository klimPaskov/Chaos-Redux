# Event 35 Agent Decisions, 2026-10-04

These decisions were taken by the implementing agent under the user's grant of full design authority for the Event 35 takeover.
Each entry records the rule, its basis in the accepted spec package, and its disposition.
Implementation evidence is linked by commit; it proves what exists and does not by itself establish design approval beyond this grant.

## D1. Super-event slot 105 in the shared lists

Disposition: implemented (commit `0efa5b56c`).

Event 35 raises `super_event_visible` slot 105 when the depression becomes worldwide (`great_depression_event.worldwide_super_event_slot`).
Each of the five shared lists (`GetSuperEventImage`, `GetSuperEventTitle`, `GetSuperEventQuote`, `GetSuperEventRemark`, `GetSuperEventDesc`) gained one 105 row that points at `GFX_super_event_105_second_great_depression` and the existing `chaosx_super_event.105.t/.q/.a/.d` keys.
No other shared row changed.
The in-game display remains `needs_live_game`.

## D2. Partner target rules for Acquire Distressed Assets and Exploit Supply Gap

Disposition: implemented.

Both decisions target countries, so their target triggers run in partner-country scope with ROOT as the acting country.

- Acquire Distressed Assets: the partner passes `great_depression_has_proved_partner_relationship` and `great_depression_partner_pair_cooldown_is_open`, is in its own active Event 35 crisis (`great_depression_active_crisis_is_coherent`), and owns and controls a center registered to its current episode that is Shuttered or Abandoned and not liquidated (`great_depression_partner_has_failed_center`).
  Basis: spec part 5 maps this action to "purchase failed assets", so the seller must actually hold a failed asset.
- Exploit Supply Gap: the partner passes the same relationship and cooldown checks and is in its own active Event 35 crisis.
  Basis: the review left the partner rule undecided; the narrowest rule consistent with part 5's exploitation balance is that only an economy in depression has a supply gap to exploit.

Neither trigger uses a state-only condition in country scope any more.
The tooltips for both scripted triggers describe the partner condition, and the new `great_depression_partner_has_failed_center_tt` names the failed-center requirement.
The AI weight bodies did not change; only the set of legal targets did.

Probability evidence: the required before/after `hoi4.probability_inspect`/`hoi4.probability_compare` pass could not run.
`hoi4.probability_inspect` with `adapter = decision_ai_will_do` returned `Invalid tool arguments` with a candidate pool and with no source, and `INTERNAL_ERROR` (zero artifacts) with `source.path = common/decisions/035_great_depression_decisions.txt`.
`hoi4.decision_inspect` in `inspect` mode for `great_depression_acquire_distressed_assets` returned `Invalid tool arguments`.
The route failure is recorded as a blocker for numeric AI evidence; target legality was reviewed from source.
