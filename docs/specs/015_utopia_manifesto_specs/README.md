# Event 15 Utopia Manifesto Planning Package

> Status recorded 2026-10-10: this directory is the accepted source design and provenance package for an implemented event.
> Event 15 is not release-qualified; the open qualification gates are listed in `docs/plans/015_utopia_manifesto_plans/release_completion_2026-10-05.md`.
> Parent-accepted October repairs and their acceptance basis are in `docs/plans/015_utopia_manifesto_plans/agent_decisions_2026-10-05.md`, and the independent October audit is `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/final_completion_release_audit_2026-10-05.md`.
> The July 18 whole-event `PASS` in `docs/plans/015_utopia_manifesto_plans/completion_audit.md` and the July source-of-truth resume packet are frozen historical snapshots, not the current verdict.
> Current source counts are summarized in `matrices/completion_coverage_matrix.md`.
> References to replacing World Tension Subsides describe historical catalog provenance, not the current event identity.

This package is the source design for Chaos Redux Event 15, `utopia_manifesto`.

Event 15 is a Minor Fire-Once event with no cluster membership.
A weak country discovers or revives a utopian manifesto.
An AI country accepts it, and a human player can accept or reject it.
Under the accepted October implementation decision, only a safe country with `generic_focus` is eligible until an exact original-tree capture and return mapping exists.
Acceptance replaces that captured generic tree with the Utopia tree and opens the Common Provision board and its paid founding survey immediately.
The older approved-light-tree candidate class remains blocked, and no generic fallback is applied to a country whose original tree was not captured.

The specification calls the mechanic the Commonwealth Ledger, which is its design and script name (`utopia_manifesto_ledger_*`, `utopia_manifesto_ledger_category`).
The player-facing board name is Common Provision.

All player-facing names in this package are working labels unless a file states otherwise. They define purpose, tone, route identity, and implementation coverage. They are not pasteable localisation.

## Package map

- `specs/` contains the eight-part source specification.
  Each part ends with an implemented record that is canonical for the installed behavior.
- `matrices/` contains target selection, route, decision, idea, AI, achievement, asset, and implementation-proof matrices.
- `focus_graphs/` contains branch and mechanic flow diagrams.
- `research/` contains the historical design basis, bibliography, source-reading ledger, and manual improvement-loop review.
- `prompts/` contains the historical goal, coding, decision, asset, achievement, and super-event build contracts.
  They record what the implementation was asked to build and are not an active queue.
  The former per-role `prompts/subagents/` files were retired on 2026-10-10 because the work they commissioned is installed; current routing is `.claude/skills/chaos-redux-subagents/SKILL.md`.
- `handoffs/` contains the historical implementation order, subagent orchestration, and planning-environment blockers.
- `catalog/` contains the historical Event 15 catalog replacement plan.
  Pending catalog wording is in `docs/plans/015_utopia_manifesto_plans/catalog_changes_pending.md`.

## Design promise

The event asks whether an economically weak state can turn an old literary model into a functioning country. The resulting campaign revolves around provision, chosen or assigned work, common stores, consent, settlement, and the claim that land may be demanded only when genuine need exists. The tree supports democratic, council-socialist, technocratic, coercive, and hidden humanist interpretations. It also makes the source text's harsher features playable, including colonial claims to underused land, compulsory labor, mercenary warfare, and restricted tolerance.

The mechanic is built around four visible pressures:

1. **Need** measures material and strategic shortage.
2. **Plenty** measures the ability to provide food, housing, transport, tools, and reserves.
3. **Concord** measures consent, public confidence, and local acceptance.
4. **Choice versus Assignment** measures whether occupations and duties are selected freely or imposed by planners.

The values alter focus access, decisions, integration rules, external claims, route corruption, AI behavior, and the final state identity.

## Historical limits of the planning run

The original planning run had no mounted repository, offline wiki, vanilla installation, or subagent runtime, so its exact paths, state IDs, and precedent checks were deferred to implementation.
Those limits do not describe the current repository and must not be used to reopen completed implementation.
The formal improvement addendum was implemented and promoted, and the 2026-07-18 final improvement-loop closure says to stop broad expansion.
The October release audit records current source repairs and the unresolved MCP, visual, probability, and asset-lineage qualification gates.

## Open questions

These items are unresolved.
Items marked proposed (spec audit 2026-10-10) are design proposals, not accepted design; each names the owner and the existing identifiers on both sides.

1. **Common Provision presentation budget**, proposed (spec audit 2026-10-10).
   The installed value tooltips list up to twelve raw contribution numbers each (for example `utopia_manifesto_ledger_gui_need_tt` shows base, policy, industry, transport, war, occupation, ground, capital, subject, and pressure terms), and the Ground tab prints about fifteen counters.
   This conflicts with the Part 7 rule that the player sees public bands rather than exact numbers in every tooltip.
   Proposal: each value tooltip shows its band, the two largest current causes in words, and the next threshold that opens or closes an action; the Callings hover shows only uncovered severity and the active method; the Ground tab shows case stage, method, integrity band, local support band, and the next step; the League block shows cohesion band and member count.
   Owner: Event 15 presentation in `localisation/english/015_utopia_manifesto_l_english.yml` and `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt`, with no gameplay change.
   Details are in Part 2, Player-facing presentation.
2. **Displayed counters that no rule reads**, unresolved implementation defect plus proposal.
   `utopia_manifesto_case_domestic_alternatives` is printed on the Ground tab but is never written in source, so it always reads 0 while the real gate is the flag `utopia_manifesto_domestic_alternatives_reviewed` read by `utopia_manifesto_case_has_domestic_alternative`.
   The source search on 2026-10-10 also found no rule that reads `utopia_manifesto_institutional_growth_batches`, `utopia_manifesto_league_refusal_count`, `utopia_manifesto_league_exit_count`, or `utopia_manifesto_stewardship_votes`; they are presentation-only.
   Proposal: remove these from the board (and show "domestic alternatives reviewed" as a yes/no line), or make a rule consume them.
   Owner: Event 15 localisation and effects.
3. **Condemnation for Penal Works and Assigned Colony**, accepted design not implemented.
   Part 3 (Penal Works) and Part 2 (Assigned Colony) require condemnation integration, but Event 15 source contains no `condemnation_add_source` call; Penal Works registers deaths only.
   Proposed fix (spec audit 2026-10-10): after Penal Works (`decision_utopia_attach_penal_works_to_district`) applies a positive exact civilian loss, and when `decision_utopia_impose_assigned_administration` succeeds, call `condemnation_add_source` with `constant:condemnation_source.atrocity`, public visibility, and the exact applied loss as `condemnation_civilian_deaths`, following `random_terror_add_condemnation_source` in `common/scripted_effects/031_random_terror_effects.txt`.
   Owner: Event 15 decision effects; the Condemnation system is consumed unchanged.
4. **Real refugee arrivals as settlement Need**, proposed (spec audit 2026-10-10).
   `utopia_manifesto_has_live_migration_pressure` currently reads only own war occupation and Event 15 district flags, so refugees delivered by the shared Migration system never create the settlement Need that Parts 1 and 2 promise.
   Proposal: add a read-only clause on Migration's country variable `migration_reception_load` above a script-constant floor; on completion of a Refugee Municipality district (`decision_utopia_found_refugee_municipality`), a Migration-owned adapter modelled on `migration_install_gods_of_africa_reception_service` may install shelter capacity through `migration_set_reception_shelter_service`, with an exact Event 15 receipt and cleanup on district loss.
   Owners: Event 15 for the trigger and district caller, Migration for the adapter; Event 15 never moves population (Famine and Migration spec Part 7 keeps the Event 15 board political and economic).
5. **Common stores during an actual famine**, proposed (spec audit 2026-10-10).
   When an owned state has `famine_food_stage_is_active`, `decision_utopia_release_emergency_stores` could deliver its existing reserve debit as food through the Famine owner's `famine_add_reserves` at that state, using its returned accepted amount so excess is not duplicated.
   `decision_utopia_send_surplus_abroad` could do the same at a recipient state with an active famine stage, which gives the aid a concrete target instead of an abstract relation gain.
   Owner: Famine owns the state reserve and stage; Event 15 owns the decision, cost, and Need change.
6. **Approved-light-tree recipients**, blocked by the accepted 2026-10-05 restriction until an exact original-tree capture and return mapping exists.

## Changelog

- 2026-10-10, spec audit.
  - Replaced the status banner with current pointers to the October release report, decisions, and audit, and condensed the planning-run limits to their still-valid intent.
  - Recorded the Common Provision board name beside the Commonwealth Ledger design name across the package and stated that the board opens at acceptance.
  - Retired the sixteen `prompts/subagents/` build prompts, which used obsolete Codex spawn syntax and commissioned installed work; git history keeps them.
  - Marked the remaining prompts as historical build contracts and repointed live skill links to `.claude/skills/`.
  - Reconciled stale statements: the Auxiliary contract no longer charges or refunds Political Power, the October release report exists, the catalog status is Needs Testing, and the deleted `docs/assets/015_utopia_manifesto/` workspace is historical.
  - Recorded that the 8 October resource-case clause is met by the generic case-relevance lifecycle (Part 4).
  - Added the open questions above: a presentation budget, inert displayed counters, the missing condemnation integration, and Migration and Famine connections.
