# Event 012 core-recognition receipt gate repair

## Gap

`africa_member_can_complete_core_recognition` required `africa_member_core_review_authorized`, but the Event 012 source had no writer for that flag. The dead gate blocked Action 38, the integration-candidate checks used by focus AI, the `africa_integrate_a_proven_region` focus, and the final integration option in `chaosx.nr12.303` even after their other consent and settlement conditions were satisfied.

## Change

The trigger now requires the existing writer-backed `africa_member_continental_constitution_accepted` receipt. The trigger still requires `africa_member_can_begin_integration`, which supplies the current-host-generation, relationship, integration-consent, representation, administration, transport, local-settlement, confidence, route, and burden checks, and it still requires `africa_member_security_settlement_complete`.

No opinion threshold, state-ownership shortcut, continent-wide core, country tag, model, asset, or new flag was added.

## Evidence

- `events/012_african_union.txt` writes `africa_member_continental_constitution_accepted` during charter admission, autonomous-federal acceptance, and final-integration consent.
- `common/scripted_effects/012_africa_action_effects.txt` writes the same receipt from shared relationship transitions, renegotiated clauses, restoration settlement, and Action 38 itself.
- `common/autonomous_states/012_africa_autonomy.txt` and the focus-route settlement predicates already consume the same receipt.
- A source census found no writer for `africa_member_core_review_authorized`; the replacement receipt has multiple accepted writers and is cleared by the existing withdrawal/refusal lifecycle.

## Remaining acceptance

Static reachability is repaired. Live positive and negative integration scenarios still need campaign validation, including refusal, host-generation mismatch, security failure, burden overload, and core-loss cleanup. No completion claim follows from this source patch alone.
