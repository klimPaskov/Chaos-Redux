# Event 006 FORM-01 through FORM-04 architecture repair handoff

Date: 2026-07-15

Role: `chaosx_scripted_system_architect`

Status: implementation repair complete; readiness remains deliberately closed pending parent re-audit.

## Workflow references used

- Repository guidance: `AGENTS.md`.
- Repo skills: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-focus-trees`.
- Offline wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, Cosmetic tag modding, and Country creation.
- Vanilla documentation: script concepts and constants, script-constant schema, dynamic variables, effects, triggers, decisions, events, focuses, ideas, modifiers, scopes, and localisation; vanilla state, adjacency, diplomatic-relation removal, naval-base, and `strength_ratio` precedents were checked directly.

## Scope implemented

### Proposal-bound founding consent

- Added an explicit carrier action, `independence_wave_issue_founding_invitations`, after method and consent-rule selection.
- Every founding invitation persists the exact carrier country scope, carrier and invited-member Event 006 generations, FORM family, and monotonically increasing proposal sequence on the invited country. The one non-Event-006 BEL delegation is explicitly bound to the zero-generation sentinel.
- A valid live invitation cannot be overwritten by a competing proposer, and a bound invitee cannot open a competing proposal of its own.
- The carrier owns aligned invited-country and invited-generation arrays. Proposal close, congress failure, successful commitment, and generation cleanup use these bounded arrays; no country-wide periodic scan was added.
- FORM-01 through FORM-04 consent evaluation accepts only a response paired to ROOT's exact live proposal. Generic family-only declarations and generic AI willingness no longer count for these four families.
- Response decisions are visible and available only for an exact pending invitation. FORM-03 AFX/AGX and BEL_flanders responses use the same shared binding; the former prospective-carrier search is no longer a consent authority.
- The congress rebuild freezes a second carrier, carrier generation, invited-member generation, family, and sequence snapshot on every consenting row. Mutation preconditions and the canonical member-origin end helper require that frozen snapshot as well as the consenting ledger row.

### Prevalidated mutation contract

- `can_independence_wave_commit_selected_formable` now routes FORM-01, FORM-02, FORM-03, and FORM-04 through exact family preconditions before `independence_wave_formable_mutation_prevalidated` is set.
- Identity and integration adapters require the prevalidation flag. The family mutations are therefore a bounded deterministic pass after country, territory, consent, connection, and integration-policy inputs have been proved in the same effect chain.
- The obsolete temporary FORM-01/02/04 consent-counter effects were removed. They ran too late, inside identity dispatch, and could not protect the paid commit decision.
- Unexpected adapter failure still uses the existing identity rollback path, but territory and origin changes are no longer entered without the strict prevalidation proof.

### FORM-01 Celtic Congress

- Requires living exact SCO, WLS, and BRI founders, all frozen as consenting to the carrier's proposal.
- Every non-carrier founder requires an actual faction, non-aggression, military-access, or guarantee relation with the carrier; geographic proximity is not treated as diplomacy.
- The carrier and every fully integrating founder prevalidate its whole compact: SCO states 121 and 133, WLS state 122, and BRI state 14 remain owned and controlled by their authorizing government.
- Autonomous founders retain their state, country, focus tree, and Event 006 origin.

### FORM-02 North Atlantic Union

- Requires GZX/Newfoundland and any two exact eastern founders from ICE, scenario-created AKX, and SCO.
- AKX is eligible only with `independence_wave_scenario_origin`, package `constant:independence_wave_package_id.iw_011`, and state 337.
- Every accepted founder must have a naval base in its certified anchor: ICE 100, AKX 337, GZX 331, or SCO 121.
- Every accepted non-carrier founder requires a verified treaty relation with the carrier. The carrier also requires nonzero convoy capacity before commitment. The accepted sources define neither a higher reserve threshold nor an engine-computable pairwise sea-route formula, so no additional numerical formula was invented.
- The carrier and every fully integrating founder prevalidate its whole compact: ICE 100, AKX 337, GZX 331, and SCO 121 plus 133. If any member remains autonomous, the carrier-capital rule remains unchanged; a fully integrated union retains the accepted 100, 331, 121, 337 priority.
- Vanilla state history confirms naval bases in all four accepted port anchors.

### FORM-03 Low Countries Confederation

- AFX/AGX core consent and BEL_flanders founding consent are bound to one exact carrier proposal and frozen at congress time.
- The existing verified border/treaty connection proof remains mandatory for every consenting non-carrier.
- Only the second consenting AFX/AGX core anchor can be integrated. BEL remains sovereign at founding.
- HOL and LUX remain post-charter sovereign associates. The repair did not transfer, core, or otherwise claim states 6, 7, 8, 35, 977, or 980.
- FORM-03 autonomous-member and post-charter cleanup were not routed through the FORM-01/02/04 reciprocal-diplomacy cleanup.

### FORM-04 Rhenish League

- Requires living RHI and AJX, capitals in states 51 and 42, both exact states owned and controlled, direct state adjacency, national adjacency, and peace between the founders.
- Direct GER control of state 42 or 51 remains a hard territorial failure.
- Parent design resolution: a stronger living Germany is an AI preference, not a player formation prohibition. `should_independence_wave_form04_ai_avoid_german_dominance` vetoes ordinary AI pursuit when carrier-to-GER `strength_ratio` is below `0.67`, meaning Germany is roughly one-and-a-half times stronger.
- The AI veto is waived by the accepted `can_independence_wave_use_rhine_bavaria_high_chaos_actions` route. Human availability is unaffected by this strength comparison.

### Symmetric autonomous-member cleanup

- FORM-01/02/04 autonomous installation persists the exact carrier scope and carrier Event 006 generation; an already autonomous member is not eligible for a second founding compact.
- Four member-side ownership flags distinguish member-to-carrier access, member-to-carrier guarantee, carrier-to-member access, and carrier-to-member guarantee.
- A flag is set only when Event 006 creates that relation. Existing relations receive no ownership flag.
- Carrier cleanup traverses the frozen founding ledger before clearing it and requires the exact stored carrier-generation-family pairing. Member cleanup removes only flagged `military_access` and `guarantee` relations with `diplomatic_relation ... active = no`, then clears the exact autonomous idea, flags, family, and carrier pointers.
- Event 5 origin state is untouched. Integrated origins still use `independence_wave_end_active_origin` with the canonical `formable_absorption` reason after the frozen proposal and ledger row are both rechecked.

## Files changed

- `common/script_constants/006_independence_wave_form01_02_04_constants.txt`
- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`
- `common/decisions/006_independence_wave_formable_registry_decisions.txt`
- `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt`
- `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`
- `common/decisions/006_independence_wave_form01_02_04_decisions.txt`
- `common/decisions/categories/006_independence_wave_form01_02_04_categories.txt`
- `common/scripted_triggers/006_independence_wave_form03_triggers.txt`
- `common/scripted_effects/006_independence_wave_form03_effects.txt`
- `common/decisions/006_independence_wave_form03_decisions.txt`
- `common/decisions/categories/006_independence_wave_form03_categories.txt`
- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `localisation/english/006_independence_wave_form01_02_04_l_english.yml`
- `docs/events/006_independence_wave/systems/formable_registry.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_formable_architecture_repair_2026_07_15.md`

## Validation and evidence

- Traced the full action path from invitation dispatch through response, ledger rebuild, frozen consent, `can_independence_wave_commit_selected_formable`, identity dispatch, integration dispatch, proposal close, and generation cleanup.
- Confirmed every FORM-01/02/03/04 founding-response decision and its category gate depends on the exact pending-invitation trigger. AI consent therefore has no path around carrier, carrier-generation, invited-member-generation, family, or sequence validation. The live-invitation predicate uses `PREV` for the invitee inside the stored-carrier scope, so it remains correct both in member decisions and in carrier-rooted candidate loops.
- Confirmed the three strict FORM-01/02/04 triggers use explicit accepted countries and compact states rather than transient counters. FORM-03 runtime proof uses the same frozen invitation contract.
- Confirmed each adapter's required non-carrier processed count is entailed by the strict precondition before the first mutation, so the territory/origin/relation phase has no remaining script branch that can fail after prevalidation.
- Confirmed FORM-02's AKX provenance through the accepted Event 006 scenario chain: IW-011 is selectable from the scenario-ranked package array, the frozen execution context loads that selected package ID into setup, generic origin setup persists it as `independence_wave_package_id`, and the scenario release marker sets `independence_wave_scenario_origin`. Vanilla state history contains naval bases in states 100, 121, 331, and 337.
- Confirmed the FORM-04 adjacency check follows the vanilla `any_neighbor_state = { state = ... }` precedent and the AI strength check follows the documented `strength_ratio` country comparison.
- Confirmed reciprocal cleanup follows the vanilla relation-removal pattern and is guarded by direction-specific creation ownership.
- Confirmed the touched formable scripts have balanced blocks, no unsupported comparison operators, no duplicate top-level trigger/effect identifiers, and no daily, weekly, monthly, or all-country scan. Localisation files retain UTF-8 BOM.
- The requested HOI4 MCP domain tools were not exposed in this agent session, so no MCP event/focus/GUI/map render or lint result is claimed.

## Readiness, blockers, and omissions

- No readiness or progression attestation was added, promoted, or claimed. The former FORM-01 through FORM-04 self-certifying registration effects now fail closed and clear stale generic, family, and FORM-03 progression attestations. The shared gate requires each matching family attestation and requires both FORM-03 base and progression attestations. The families remain closed until the parent re-audits the repaired operational contract and deliberately restores evidence-backed registration.
- FORM-02's source design does not specify a safe convoy reserve threshold or a scriptable pairwise sea-route formula. The implemented proof is therefore limited to exact accepted ports, exact bilateral treaty relations, and nonzero carrier convoys; any stronger numerical reserve rule remains a parent design decision rather than an invented tuning value.
- No asset was created or changed; the task explicitly excluded assets.
- Asset completeness was not certified here. FORM-03 progression art and the KCX/NUX/RLX carrier-ideology flag lookup findings remain separate asset-audit inputs to the parent readiness decision.
- No general-purpose `chaosx_dynamic_effects` API was added. The reusable proposal and cleanup helpers are documented in the formable-registry system document because their contract is Event 006 formable-specific.
- No fallback, placeholder, world scan, or territory simplification was used.
- The dirty worktree was preserved and no commit was created, as instructed.
