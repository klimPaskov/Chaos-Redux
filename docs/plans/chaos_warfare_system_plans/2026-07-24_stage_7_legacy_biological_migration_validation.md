# Stage 7 Legacy Biological Migration Validation

Date: 2026-07-24

Status: bounded migration tranche validated. Stage 7 and the full Chaos Warfare goal remain incomplete.

## Scope

This tranche removes the old immediate-contamination implementation after valid release routes were migrated to the shared ordinary-pathogen lifecycle. It also converts special-project field tests to exact facility-state resolution and corrects the abstract camp method to the accepted weapon-strength hierarchy.

## Accepted boundaries

- Ordinary weapon strength is `Tularemia < Anthrax < Plague < Smallpox`; only Smallpox is severe.
- Strategic and battlefield raid reliability is agent-neutral. Every ordinary strategic raid uses the same success, critical-success, and disaster factors, and every ordinary battlefield raid uses the same success factor.
- A delivery result describes operational execution, not weapon severity.
- A release requires an exact target and complete route authority. Random neighboring-state focus effects, passive battalion rolls, abstract camp accounting, inferred targets, and compatibility fallbacks cannot seed an outbreak.
- Weaponized zombies remain separate.

## Migration results

- The four `apply_*_contamination` effects and their scaled variants are removed.
- UWR focus rewards retain stockpiles, special-project progress, expansion planning, claims, and assault columns but no longer contaminate a random neighboring state.
- The Chaos Assault Battalion no longer performs a passive biological outbreak roll.
- Camp biological escalation still consumes the selected stock, records deaths, evidence, resistance, discovery, tribunal exposure, and responsible-country history, but it does not create an ordinary outbreak episode.
- Camp biological potency, deaths, evidence, accident pressure, and suppression follow the accepted four-agent hierarchy.
- Terminal Hazard may multiply an already authorized camp network's resolved deaths while preserving the camp system's evidence, discovery, responsibility, resistance, trauma, Condemnation, and history.
- Field testing resolves only in the exact active project facility. All four agents use the same containment-accident chance; the agent profile changes only the consequences of a real containment failure.
- The lifecycle independently rejects a field-test seed unless its exact actor and victim targets, both scope proofs, current controller, and actor-victim identity all agree.

## Conflict disposition

The older Unconventional Warfare Republic implementation spec and historical handoffs described automatic random neighboring-state contamination from focus completion. That behavior conflicts with the accepted numbered CBRN specifications and explicit no-fallback release contract. The current UWR source-of-truth document supersedes those historical handoffs: future UWR battlefield or strategic use must use native exact-state raids and the shared lifecycle.

## Validation evidence

- No gameplay caller or definition of `apply_anthrax_contamination`, `apply_plague_contamination`, `apply_tularemia_contamination`, `apply_smallpox_contamination`, or any `_scaled` variant remains.
- No gameplay caller or definition of `soviet_collapse_uwr_contaminate_neighbor_front` or the passive Chaos Assault Battalion outbreak helper remains.
- The four strategic raid definitions share one success, critical-success, and disaster constant set.
- The four battlefield raid definitions share one success constant and one success-factor structure.
- The four field-test profiles share one accident-chance constant.
- Existing biological raid assets under `gfx/interface/military_raids/` were neither replaced nor edited.
- Direct source inspection confirms that the field-test reward uses the installed game's documented `facility_state_effects` contract: state scope, active project in `FROM`, and project owner in `FROM.owner`.

The UWR focus inspector reports no connector crossings, node intersections, or long connectors. Its generic focus-sprite resolver also reports unresolved sprite references, including vanilla continuous-focus sprites; that diagnostic is not treated as an asset pass and remains open for the final UWR asset audit.

The event-chain viewer could scan the repository but could not lint or render the eight individual field-test events because the repository-wide event issue count exceeded the tool's fixed 20,000-issue ceiling before target isolation. This is an explicit tooling blocker, not an event pass. The bounded event check therefore used direct source, identifier, localisation, and caller inspection; the mapped event audit remains required before Stage 7 completion.

Historical camp-architecture handoffs still mention the retired immediate-contamination identifiers inside clearly marked superseded preimplementation sections. They are retained as historical rationale rather than active API documentation. The live Event 016 reuse map has been updated to require the lifecycle API and forbid those retired callers.

## Simplifications, omissions, and blockers

No fallback or substitute release path was retained in this tranche.

Stage 7 remains open for its remaining designer, safety, facility-capture, route-aware AI, asset, localisation, package-scenario, and audit requirements. The full Chaos Warfare goal remains incomplete.
