# Event 016 Mengele Singularity late-stage output handoff — 2026-09-25

## Disposition

The private Deployment and Weaponization output tranche is implemented under the user-accepted Event 016 final completion contract and Mengele portfolio plan.
It does not complete the playable Singularity route or its Fallout terminal.

## Source behavior

After the private receipt core has validated and settled the exact family/stage callback, Singularity Deployment sets `mengele_event016_singularity_deployment_completed` and grants the existing `brilliant_scientist_singularity_deployment` modifier.
Weaponization requires that predecessor, then sets `mengele_event016_singularity_weaponization_completed` and grants the existing `brilliant_scientist_singularity_weaponization` modifier.
Both outputs mark the callback applied, so a valid paid finish is no longer treated as a source gap and refunded.
The existing modifiers now accept either the Kruger host or a valid Mengele provider with the matching private stage receipt; they remove themselves when neither condition holds.
The existing provider reconciliation restores a missing late-stage modifier from its exact private flag without replaying a payment or terminal effect.

This uses the existing stage tuning, icon, modifier identifiers, and localisation.
It writes no Kruger stage array, terminal commitment, construction receipt, arming flag, Chaos value, Fallout request, super-event, or world-end state.
Private stage completion must not be mistaken for physical device construction or terminal readiness.

## Source scenarios and limits

- A valid provider with six component receipts and Prototype may finish Deployment once; its modifier is enabled by the private flag.
- A valid provider with Deployment may finish Weaponization once; its modifier is enabled by the private flag.
- A repeated or wrong-stage callback remains rejected by the existing private stage request/receipt guards.
- Loss of provider validity removes either modifier while preserving durable private stage history; reconciliation can restore it if a valid provider state returns.
- The Kruger host still satisfies the original modifier gate without any Mengele flag.

These are source-level checks of the existing guard and output chain, not engine or live-game observations.
Playable stage decisions, native component eligibility and risky rewards, physical site construction, provider terminal decision, Fallout admission/retry/finalization, CXT fixtures, and current balance/MCP acceptance remain accepted and queued.
No 3D geometry or external system was changed.
