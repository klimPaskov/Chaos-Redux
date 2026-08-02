# Event 012 Africa compact-host promotion

Compact hosts are deliberately smaller Event 12 openings. They can become full dossiers only through visible evidence, not through opinion, a passive timer, or an automatic relationship change.

## Evidence contract

The current compact host must control its capital and retain the `compact` host-depth value. It must have identified and published the mapped opening weakness, completed or recovered the first proof mission, proved the first public obligation, convened the provisional congress, and completed both compact signature focuses. The compact signature must have reached `prove_compact_viability`, and the current action phase must be regional or later. Stability and war support must remain above the shared Charter floors in `africa_compact_promotion`.

These checks bind promotion to the opening's weakness, proof mission, leverage, and rival-risk work. The docket never reads opinion as a substitute for evidence.

## Player-facing decisions

`africa_record_compact_promotion_proof` costs the configured proof political power and submits the evidence dossier. Its scripted effect records `africa_compact_long_campaign_survived` and `africa_compact_route_contradiction_proven`, then reconciles the shared six-criterion store. It changes no tag, owner, controller, core, relationship, or opinion.

`africa_promote_compact_host` costs the configured promotion political power and calls the shared `africa_promote_compact_host_package` effect. Promotion requires at least two reconciled criteria, the live capital and depth checks, viable territory, local support, a functioning institution, a distinct role, and no active overlap dispute, access failure, refusal, or prior promotion. Successful promotion preserves the original host country and changes only its host-depth and package state.

`africa_decline_compact_promotion` is the explicit refusal path. It leaves the country as a compact signature and records a hard refusal without changing ownership, relationships, cores, or opinion. `africa_reopen_compact_promotion_docket` is the paid reconsideration path; it clears only that refusal receipt and leaves all evidence flags intact. No path silently overrides a refusal or promotes by opinion.

Promotion also observes the shared `africa_overlap_dispute_active` and `africa_project_access_damaged` receipts written by the regional-action kernel. A successful overlap settlement clears the dispute receipt, while successful rail, river, port, processing, resource, procurement, food, development, and industrial projects clear the access-damage receipt on their resolved scope.

## AI and cleanup

Both decisions are visible to the current host only and use bounded AI willingness. The evidence writer gives a modest preference to a host that has prepared security; the existing shared action controller and host gates remain authoritative. Evidence flags are lifetime campaign receipts, while transient refusal, access, and host-depth state remain subject to the existing package cleanup and generation logic.

## Icon registry

No new art is required for this mechanic. Both decisions use the existing `GFX_decision_012_africa_charter_ledger` sprite registered for `africa_charter_council_category`; no new `.gfx` entry, DDS, or localisation icon key is introduced.

## Future depth

Later accepted content may let a real regional council, rival bloc, post-unification legacy, opening-depth failure, or Tier A identity write one of the four remaining criteria. Those writers must preserve the same evidence gate, refusal/reconsideration cleanup, and no-opinion rule rather than creating another promotion store.

## Validation scenarios

1. A compact host with only opinion or a completed focus cannot see an available evidence decision.
2. A compact host that completes the mapped weakness, first proof, obligation, congress, both signature focuses, capital control, and resilience floors can pay for the evidence decision and receives exactly two criteria.
3. The promotion decision remains unavailable with an active overlap dispute, access failure, refusal, lost capital, or fewer than two criteria.
4. A valid promotion keeps the original tag and owner while changing host depth to `promoted`; it does not annex members, grant continent-wide cores, or alter relationship states.

No new country tag, duplicate store, or automatic opinion path is introduced by this mechanic.
