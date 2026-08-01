# IW-012 ICE country-package audit and narrow repair

Date: 2026-08-01.

Scope: static audit of Event 006 package `IW-012`, reused vanilla tag `ICE`, reservation group `RG-100`, anchor state `100`, package-local effects, decisions, ideas, focus carrier, AI, diplomacy, force mapping, formable hooks, localisation, and cleanup.

## Verdict

The package is statically admitted and preserves the vanilla Iceland identity, history, characters, state, flag, OOB, and `iceland_tree` carrier.

One local behavior defect was repaired: failed or cancelled ICE projects now reduce Compact Support by the package's tuned `independence_wave_ice_value.minor_loss` instead of assigning the generic zero-valued minimum.

All ICE-specific zero/clamp references were also moved to `independence_wave_ice_value` so the package remains controlled by its own tuning table.

This is not a runtime-completion claim.

## Country package coverage checklist

| Surface | Status | Evidence and finding |
| --- | --- | --- |
| Tag and identity | Static pass; runtime pending | Vanilla `ICE` remains the registered tag, and package checks use `original_tag = ICE` with package id `constant:independence_wave_package_id.iw_012`. No duplicate country, history, state, flag, portrait, or tag was added. |
| Dormant-origin admission | Static pass | The exact IW-012 wrapper intentionally requires the reused tag to be dormant (`exists = no`) before release; this preserves the normal 1936 vanilla Iceland start. |
| Map and state setup | Static pass; transaction pending | Anchor and capital are vanilla state `100`, with vanilla ownership/core, capital, port, dockyard, industry, and victory point data retained. Host protection and state reservation are checked by package and region planners. |
| Politics and parties | Static pass | Setup initializes the existing vanilla ICE democratic/neutrality distribution and promotes `ICE_sveinn_bjornsson` and `ICE_bjorn_sveinsson_bjornsson`; no invented party or leader is introduced. |
| Leaders, commanders, portraits, advisors, and names | Static pass; date/DLC runtime pending | `has_independence_wave_ice_command_roster` requires the two existing vanilla characters and Bjorn's corps-command role. No opposite-gender random pool, generated portrait, or new advisor icon is used. |
| Flags and cosmetic identity | Static pass | Vanilla ICE flag/cosmetic sources remain authoritative. FORM-02's existing identity adapter owns any later cosmetic transition. |
| Focus carrier and route links | Static pass; engine render pending | Mod-owned `common/national_focus/iceland.txt` keeps `id = iceland_tree` and the vanilla body, then imports the reviewed Event 006 overlay and four ICE route consumers. No replacement focus tree was created. |
| Decisions and mission | Static pass; runtime pending | `independence_wave_ice_hold_the_harbour` and six serialized projects are registered under `independence_wave_ice_north_atlantic_category`, with package, capital, host, cost, cancellation, and failure guards. |
| Ideas and lifecycle | Static pass | Five ICE lifecycle/route ideas are defined, added by project or route effects, refreshed by the package lifecycle helper, and removed by ICE cleanup. |
| Formable and diplomacy | Static pass; runtime pending | The package selects the `north_atlantic_compact` family, checks FORM-02 readiness, and keeps the vanilla Nordic precedence guards. Former-host diplomacy uses a saved event target and target-specific AI cleanup. |
| Starting military and force mapping | Static mapping pass; materialization pending | IW-012 maps to `p12` / `coastal_maritime`, with navy inheritance and the documented reinforcement pathways. Setup calls the generic dynamic force effect only after the ICE roster and profile proofs pass. |
| Technology, industry, supply, and production | Vanilla baseline retained; runtime pending | Vanilla ICE history remains authoritative for research slots, technologies, OOB, port, dockyard, industry, convoys, and supply context. No technology-tree viewer is installed in the available MCP package, so that inspection remains an unresolved limitation. |
| AI and playability | Static surface pass; runtime pending | ICE-local AI strategies use supported types and integer weights, and package setup adds target-scoped former-host diplomacy. Focus selection, decision ordering, force survival, and host behavior still require live evidence. |
| Localisation and assets | Static pass | Direct ICE category, mission, projects, ideas, tooltips, and ledger text are covered by `localisation/english/006_independence_wave_ice_l_english.yml`; shared icon sprites and vanilla ICE art resolve from existing assets. |
| Cleanup | Static pass; rollback pending | ICE cleanup removes the mission, six decisions, five ideas, package flags, and five ICE ledger variables; shared cleanup owns force, focus, network, league, and provenance reset. No runtime annexation, host-death, or formable rollback was run. |

## File surface checklist

### Direct IW-012 surfaces

- `common/scripted_effects/006_independence_wave_ice_package_effects.txt` owns ICE ledger changes, failure consequences, route effects, setup, validation, host AI, and cleanup.
- `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt` owns ICE identity, state/host/roster proofs, route gates, force proofs, lifecycle checks, and setup completion.
- `common/decisions/006_independence_wave_ice_decisions.txt` and `common/decisions/categories/006_independence_wave_ice_categories.txt` own the harbour mission and six projects.
- `common/ideas/006_independence_wave_ice_ideas.txt` owns the five package ideas.
- `common/script_constants/006_independence_wave_ice_constants.txt` owns ICE values, thresholds, durations, politics, and AI tuning.
- `common/ai_strategy/006_independence_wave_ice.txt` owns package-gated AI plans.
- `common/national_focus/iceland.txt` owns the vanilla carrier with additive imports only.
- `localisation/english/006_independence_wave_ice_l_english.yml` owns direct ICE strings.

### Shared dependencies reviewed

- Package setup/final/cleanup dispatch and attestation include `iw_012`.
- Region planner reserves `RG-100` and state `100` for IW-012.
- Force mapping and formable helpers connect the package to `p12` / `coastal_maritime` and FORM-02.
- Shared focus, decision, ledger, network, league, and cleanup helpers remain parent-owned.

## Patch details

Changed `common/scripted_effects/006_independence_wave_ice_package_effects.txt`.

- ICE Shipping Security and Compact Support clamps now use `constant:independence_wave_ice_value.minimum/maximum`.
- `independence_wave_ice_apply_project_failure` now sets `independence_wave_ice_compact_delta = constant:independence_wave_ice_value.minor_loss`.
- ICE route-focus zero deltas now use the ICE minimum namespace.
- Generic shared decision/league deltas intentionally retain `constant:independence_wave_value.minimum` because they target the shared ledgers rather than an ICE ledger.

Changed `common/decisions/006_independence_wave_ice_decisions.txt`.

- The Coastwatch and Armed Neutrality ICE zero deltas now use `constant:independence_wave_ice_value.minimum`.

Before the repair, a failed or cancelled project reduced Port Authority, Civic Cohesion, Coastwatch Readiness, and Shipping Security by five but left Compact Support unchanged at zero delta.

After the repair, all five ICE ledgers receive the package's tuned minor-loss penalty and remain clamped to the package's own 0–100 range.

## Validation performed

- Read `AGENTS.md`, the Chaos Redux subagent, event, decision/mission, and focus-tree skills, the required offline Paradox wiki pages, and the relevant installed vanilla effects, triggers, script-constants, and country/focus references.
- Confirmed every `constant:independence_wave_ice_value.*` reference in the two changed gameplay files resolves in `common/script_constants/006_independence_wave_ice_constants.txt`.
- Confirmed the only remaining generic `independence_wave_value` references in the ICE effects are the three shared decision/league zero deltas, not ICE ledger clamps or ICE ledger outcomes.
- Confirmed brace/depth balance is zero at EOF for both changed Clausewitz files.
- Rechecked direct package ids, state `100`, vanilla `ICE` character ids, `iceland_tree`, six project ids, harbour mission id, five idea ids, FORM-02 family, and force mapping identifiers against the current source and handoff records.

## Skipped meaningful validation

No Hearts of Iron IV process was launched, and no live allocator, date/DLC matrix, save/load, focus-render, AI-playthrough, force-materialization, map transaction, host-death, annexation, or formable rollback scenario was run.

The installed MCP package exposes no Technology Tree Viewer, so technology-tree inspection remains limited to vanilla history and documentation review.

## Remaining risks and blockers

- Runtime execution and rollback evidence remain parent-owned requirements before describing IW-012 as complete.
- The package still depends on the shared Event 006 mission/decision and cleanup framework; this audit did not redesign or replace shared mechanics.
- No fallback country, duplicate tag, generic focus tree, invented leader, copied portrait, replacement flag, or static OOB was added.

## Git and handoff

Only the two gameplay files listed above were patched for this handoff.

No Git commit was created because the shared worktree contains concurrent Event 020, Fallout, and Event 006 documentation changes outside this package scope; the parent agent owns the scoped commit after review.
