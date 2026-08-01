# Event 012 common-reserve deployment handoff

Status: implemented source tranche; live campaign acceptance remains open.

## Scope

This tranche closes the runtime owner gap around the existing common reserve. It does not add a country tag, model, unit entity, recurring world scan, or second stockpile.

## Changed surfaces

- `common/script_constants/012_africa_action_constants.txt` adds the shared minimum stockpile, per-deployment cost, and settlement-window constants.
- `common/scripted_triggers/012_africa_common_reserve_triggers.txt` validates the Action 80 host contract and defender-only partner deployment.
- `common/scripted_effects/012_africa_common_reserve_effects.txt` owns activation, stockpile debit, sequence copy, settlement, deadline, capital-loss, and cleanup semantics.
- `common/scripted_effects/012_africa_action_effects.txt` gates Action 80 by reserve/transport proof and activates the posture only on a full result.
- `common/scripted_effects/012_africa_effects.txt` initializes the shared deployment sequence.
- `common/scripted_effects/012_africa_achievement_effects.txt` adds exact reserve owner/disqualifier writers and counts distinct deployment sequences.
- `common/on_actions/012_africa_world_order_on_actions.txt` wires defensive war start, offensive misuse, peace, capitulation, and annexation callbacks.
- `common/scripted_effects/012_africa_rsa_effects.txt` transfers the reserve posture and sequence to the accepted RSA exile successor.
- `localisation/english/012_african_union_l_english.yml` describes the visible reserve requirements and per-war window.
- `docs/events/012_africa/common_reserve_deployment.md` records the system contract and future extension boundary.

## Acceptance evidence

The positive owner now requires a full Mobilise Continental Defence result, a configured stockpile, an explicit transport receipt, a defended protected partner, an attacker/defender war callback, and an on-time peace settlement with the partner capital held. Deadline, capital-loss, and offensive-use outcomes write the exact sticky achievement disqualifiers. All state is cleared by the existing war callbacks; no daily or monthly iteration was introduced.

## Remaining evidence and risks

Live campaign tests still need to exercise six separate protected defensive wars, an out-of-window settlement, partner capitulation, annexation cleanup, offensive partner misuse, and RSA exile succession. The achievement remains incomplete until those scenarios are accepted. No model work is included; later visual/unit requests remain in the existing asset disposition ledger.
