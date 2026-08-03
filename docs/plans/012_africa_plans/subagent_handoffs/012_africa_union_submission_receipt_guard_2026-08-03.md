# Event 012 W4 union submission receipt guard

## Gap

`africa_world_union_protocol_target_is_eligible` read `africa_world_package_submission_settlement`, but the canonical Action 88 and continental-war submission effects write `africa_world_submission_settlement`.

The package-prefixed spelling had no writer in the Event 012 source, so a package that had reached a terminal submission settlement could still pass the later union-partner eligibility check.

## Change

The trigger now rejects the canonical `africa_world_submission_settlement` flag.

No country tag, model, asset, localisation, focus route, or package gate was changed.

## Evidence

- `common/scripted_triggers/012_africa_world_union_war_triggers.txt` reads `africa_world_submission_settlement`.
- `common/scripted_effects/012_africa_world_union_war_effects.txt` writes the flag for continental-war submission.
- `common/scripted_effects/012_africa_world_order_effects.txt` writes the flag for Action 88 and clears it during package cleanup.
- A focused source census found no remaining `africa_world_package_submission_settlement` reference in the trigger/effect files.
- Brace and quote structure for the edited trigger file is balanced.

## Remaining acceptance

Static source wiring is corrected.

Live W4 union scenarios still need to observe that submitted actors are rejected while eligible sovereign packages remain valid; this handoff does not claim campaign acceptance.
