# Event 15 Utopia Manifesto focus-tree final audit

## Verdict

**FAIL**

The current 122-focus source is substantially stronger than the first two audited versions: the normal five-route graph is complete, costs and Ledger movements use the accepted 5/10/15 bands, paid growth is paired, helper/localisation/icon references resolve, the phase ladder is consumed, and the coordinate repair materially reduced the original layout failure. It is still not completion-ready. Five independent P1 findings remain:

1. Dynamic `allow_branch` content is never refreshed after the tree is loaded, so the hidden route and constitutional-crisis branch do not become visible through normal play.
2. Four crisis route corrections change the route flag but do not reconnect the player to the selected route's focuses or capstone.
3. The maximum-three-spirit lifecycle still fails in a guaranteed early sequence and in a valid early-Stewardship ordering.
4. The state-aware opener AI reads one mandatory signal as a Consent preference and several dead or wrong-scope signals as route state.
5. The accepted leased-island project variant is absent; it is represented only by an enable flag on the coastal route and is not an island-project branch or proof.

Audit snapshot:

- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
- SHA-256: `7C2E51B8476F766E86A753FA0F0BC8F3CCCDD25B54ABB2FE1363D029D9F4AB87`
- deterministic layout hash: `248b31c1cbdce685af214ec1665bd6f38037306c59fae3805b9e6876a27c6dff`

## Completion blockers

### P1 FTF-001: dynamic hidden branches never receive a layout refresh

The tree contains fifteen dynamic `allow_branch` blocks and Event 15 contains zero calls to `mark_focus_tree_layout_dirty`.

This matters because `allow_branch` is checked only when a focus tree is loaded. The offline National Focus Modding reference explicitly requires `mark_focus_tree_layout_dirty` to re-evaluate it later, and the official effects documentation defines that effect as the country-scope tree-layout refresh.

The Event 15 tree is loaded at `common/scripted_effects/015_utopia_manifesto_effects.txt:316`. At that point:

- the Joke opener's reveal is false, but its root uses dynamic `allow_branch` at focus line 1347;
- its later focuses use route-dependent `allow_branch` at lines 1385-1553;
- the crisis root and four ordinary correction choices use crisis-dependent `allow_branch` at lines 2921-3059;
- the humanist correction uses the dynamic reveal at line 3097;
- the crisis convergence focus uses the resolved flag at line 3132.

The relevant state changes occur later. Public debate is established by the opening tree at line 83, public education by focuses at lines 341, 1618, and 1707, and crisis state by `utopia_manifesto_enter_constitutional_crisis` at effects lines 762-765. Neither that effect nor `utopia_manifesto_resolve_constitutional_crisis` at lines 767-770 refreshes the tree. Route setters also do not refresh it.

Consequences:

- the direct hidden route cannot reveal after its education, Choice, Concord, and conduct requirements become true;
- the crisis branch remains hidden when a constitutional crisis begins;
- even a forced correction cannot reveal `A Settled Interim Charter` after the crisis is resolved;
- the hidden route's child focuses do not become visible merely because its route flag was set.

Required correction: centralize dynamic focus visibility and call `mark_focus_tree_layout_dirty = yes` on actor-scoped transitions that change Joke reveal, route, crisis, or crisis-resolved state. Refreshing only on crisis entry is insufficient; resolution and hidden-route commitment also change distinct `allow_branch` conditions. Re-run the tree render for each visibility state.

### P1 FTF-002: four crisis route switches cannot enter the selected route

The five route openers are mutually exclusive. Once one is completed, a different opener cannot subsequently be completed. The crisis correction focuses correctly change the route flag and route institution, but the repaired prerequisite topology was added only for the Joke route:

- `Institutions That Can Be Left` accepts either `Read the Island as a Mirror` or `Admit the Book Was a Question` at focus lines 1381-1384.
- `A Mixed Commonwealth` has the equivalent alternative at lines 1413-1416.

No equivalent correction parent exists for the four ordinary routes. Their first route focuses still require only the original opener:

- Consent: `Free Callings` and `Municipal Charters`, lines 290 and 313;
- Common Table: `Councils of Callings` and `The Common Table`, lines 551 and 574;
- Guardians: `Standard Houses` and `Tables of Need`, lines 830 and 858;
- Closed Island: `Households of Service` and `The Closed Store`, lines 1119 and 1148.

For example, a country that completed the Common Table opener and then takes `Restore Consent` cannot complete `Household Gives Consent` because the two openers are mutually exclusive. It therefore cannot reach `Commonwealth by Consent` or set `utopia_manifesto_route_capstone_consent`. The current-route formation trigger requires that capstone at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:1668-1685`. The same failure applies to a genuine switch into Common Table, Guardians, or Closed Island.

The old route's completed capstone does not rescue formation: `utopia_manifesto_can_form_current_route` evaluates the newly selected route and its matching capstone/proofs. Selecting the same route again is safe, and the Joke correction is structurally connected, but four of the five advertised correction outcomes are not valid route switches.

Required correction: make each correction focus an alternative parent of every immediate child of its matching opener, following the existing Joke pattern, or introduce an equally explicit route-rejoin mechanism that does not grant the original opener's reward twice. Then trace every permitted old-route to different-route switch through capstone and formation proof.

### P1 FTF-003: lifecycle helpers still permit four or more Event 15 spirits

The main mature sequence is coherent in isolation: route commitment removes Found Manifesto, replaces Inherited Order with the route property settlement, preserves one administrative track, and adds one route institution; Common Store later replaces the administrative track; Island Made Real replaces the property track with Garden District. Temporary Auxiliary and Stewardship helpers are intended to borrow one of those slots.

Two reachable orderings still break the maximum of three.

#### Guaranteed opening duplication

1. Acceptance initializes Found Manifesto, Unmeasured Country, and Inherited Order at `common/scripted_effects/015_utopia_manifesto_country_effects.txt:113-120`.
2. Acceptance schedules `chaosx.nr15.2` after `public_circulation = 5` days at `events/015_utopia_manifesto.txt:57-58` and `common/script_constants/015_utopia_manifesto_narrative_constants.txt:44`.
3. Every option in that event replaces the base Found Manifesto with either its mitigated or failure stage through `utopia_manifesto_publish_public_edition` or `utopia_manifesto_dogmatize_found_manifesto` at event lines 87-120.
4. `Recover the Manuscript` costs 5 focus-cost units at focus line 51. On completion it tests only for the base idea and re-adds that base at lines 55-58.

The day-5 event therefore removes the base stage before the first normal 35-day focus completes. The focus then adds the base beside the mitigated/failure stage, producing two Found Manifesto stages plus Unmeasured Country and Inherited Order. This is a normal opening sequence, not an edge case. Route commitment eventually clears the duplicate, but the package visibly exceeds the accepted cap for the intervening period.

The same base-only pattern remains for Unmeasured Country at focus lines 105-108 and Inherited Order at lines 202-205, and Second Generation directly removes only their base keys at lines 3252-3254 instead of using family clear helpers.

#### Stewardship before the Garden track exists

`Stewardship Obligations` requires `Ground Held in Trust` and an active stewardship case at focus lines 2778-2779; it does not require `The Island Made Real`. `utopia_manifesto_begin_stewardship_burden` clears only Stewardship and Garden stages before adding the burden at `common/scripted_effects/015_utopia_manifesto_country_effects.txt:419-423`.

Before Island Made Real, the normal three active slots are route institution, route property settlement, and either Unmeasured Country or Common Store. No Garden stage exists to clear, so beginning Stewardship adds a fourth spirit. If Island Made Real completes while that burden is active, `utopia_manifesto_found_garden_district_network` clears the burden at country-effect lines 326-331, silently removing the liability before its status chain resolves.

There is also a narrower Auxiliary consistency defect: `Auxiliary Contracts` and `Foreign Hands in Our Wars` set `utopia_manifesto_auxiliary_dependency_active` at focus lines 1210 and 2278 without calling `utopia_manifesto_begin_auxiliary_dependency`; the actual paid hire decision sets the active flags and calls the lifecycle helper together at decision lines 3867-3872. The focus state can therefore claim active dependency without the matching staged idea.

Required correction: replace the three base-only opening guards with whole-family guards or stage-safe lifecycle calls; use family clear helpers at mature cleanup; define which stable slot Stewardship replaces before Garden exists; prevent Island formation from silently resolving a live burden; and make Auxiliary active-state flags and lifecycle calls describe the same event. Re-run a state trace across opening events, every route stage, early/late Store and Garden orderings, Auxiliary, Stewardship, crisis switching, and formation.

### P1 FTF-004: opener AI is state-aware in form but not coherent in operation

The five openers now call dedicated preference and avoidance triggers, and those triggers mention ideology, stability, Ledger bands, war pressure, industry, infrastructure, research, geography, neighbors, debate, conduct, and route failure. That closes the previous absence of state inputs, but several inputs cannot produce the intended selection behavior.

- `utopia_manifesto_ai_prefers_consent_route` treats `utopia_manifesto_public_debate_proven` as a standalone OR at trigger line 639. The mandatory opening path sets that flag at focus line 83 before `The Country as a Question` can be completed. Consent therefore receives its route bonus for every actor, independent of ideology, stability, Concord, Need, neighbors, or war state.
- The same Consent helper applies a severe avoidance factor below five factories at trigger line 649. The accepted recipient and route specifications favor small, low-industry actors, so an intended democratic minor commonly satisfies both the universal preference and the hard avoidance.
- Common Table's industrial clause checks a country flag named `utopia_manifesto_worker_council_established` at trigger line 664. The implementation creates a state flag of that name at `common/scripted_effects/015_utopia_manifesto_decision_effects.txt:522`, not a country flag. Another option in that clause, `utopia_manifesto_property_transition_started`, is set only by completing the Common Table opener itself at focus line 523 and therefore cannot inform initial opener selection.
- Joke failure weighting checks `utopia_manifesto_district_project_failed` at trigger line 775, but no gameplay file produces that flag. District failure instead sets the target-state flag `utopia_manifesto_district_project_refused` at decision-effect line 605 and, for Guardians, the country flag `utopia_manifesto_assignment_revolt` at line 596.
- Closed/Joke weighting and the Joke reveal gate check `utopia_manifesto_emergency_levy_active` at trigger lines 609, 736, and 787, but no gameplay file sets it. The calling decision records the selected method and a timed `utopia_manifesto_emergency_levy_recent` flag instead at decision lines 576-582.

Because each opener has one binary preference bonus and one binary avoidance factor, these universal, dead, and wrong-scope signals dominate rather than gently contributing to a scenario score. The representative democratic-stable minor, neutral landlocked low-capacity actor, and high-education reformist cases therefore cannot be accepted as validated merely because all input classes appear in the trigger text.

Required correction: use live pre-commit state only; aggregate state flags where needed or query them in a valid state scope; replace dead signal names; remove the mandatory-debate standalone Consent preference; and run explicit comparative weight tables for the five representative scenarios required by the AI spec plus crisis variants. The values should remain centralized.

### P1 FTF-005: the leased-island project variant is missing

The accepted focus architecture says `Choose the Island` offers an existing island, leased island, coastal refuge, or Inland Island (`spec_part_3_focus_tree_architecture.md:925-928`; `focus_route_matrix.md:14`; `focus_graphs/focus_tree_architecture.md:30`). The current tree implements only three children:

- Existing Island, focus lines 2017-2041;
- Coastal Refuge, lines 2043-2068;
- Inland Island, lines 2070-2095.

`utopia_manifesto_prepare_island_variant` likewise chooses only existing, coastal, or inland at `common/scripted_effects/015_utopia_manifesto_effects.txt:772-790`, and the island proof accepts only those three flags at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:487-499`.

The Coastal Refuge reward sets `utopia_manifesto_island_lease_route_enabled` at focus line 2059, but that only enables the general Necessary Ground lease ladder. The island-site decision still targets a controlled core state and requires existing/coastal/inland geography at `common/decisions/015_utopia_manifesto_decisions.txt:1456-1483`. A successful foreign lease is not a fourth island-project selection or proof.

Required correction: implement the distinct leased-island project with a valid foreign target, successful lease result, project-site scope, AI, failure/expiry handling, and formation proof, or formally amend the accepted spec before implementation. Treating Coastal Refuge as a silent substitute is an unreported simplification.

## Layout assessment

**PARTIAL; P2 cleanup remains.**

The coordinate repair is material and should be preserved as the baseline:

- 122 fixed nodes, no coordinate collisions;
- 170 prerequisite connectors, all parents above their children;
- bounds reduced to 55 columns by 17 rows;
- same-row minimum spacing is 2, with zero too-close pairs;
- route openers are contiguous and no current through-node diagnostic is incident to an opener.

The fresh read-only inspector still measures:

| Metric | Current |
| --- | ---: |
| Connector crossings | 50 |
| Connector-through-node intersections | 7 |
| Long connectors | 20 |
| Maximum horizontal span | 20 |
| Maximum Manhattan span | 21 |

Two surfaced through-node diagnostics run `The Island Made Real -> Proof of the Commonwealth` and `Union of Tables -> Proof of the Commonwealth` through the `Commonwealth by Consent` capstone. The inspector also identifies avoidable crossings in the opening fork, the Common Table autonomy/central-plan fork, and the Guardians freedom/obedience fork. Those lines can imply false dependencies at precisely the route-choice and formation surfaces.

This is far better than the previous 86 crossings, 41 node intersections, and 26 long connectors, so the old layout blocker is not carried forward unchanged. It is not a final clean layout, and FTF-002 plus the missing lease branch will alter topology anyway. After those corrections, rerender and remove all connector-through-node cases at route capstones and formation convergence, then reassess the remaining long connectors at normal review scale.

## Structural and balance results

### Inventory

| Surface | Focuses | Result |
| --- | ---: | --- |
| Opening survey | 8 | PASS |
| Consent of Households | 10 | PASS on normal route; crisis rejoin FAIL |
| Common Table | 10 | PASS on normal route; crisis rejoin FAIL |
| Guardians of Measure | 10 | PASS on normal route; crisis rejoin FAIL |
| Closed Island | 9 | PASS on normal route; crisis rejoin FAIL |
| The Joke Understood | 8 | Source complete; dynamic visibility FAIL |
| Callings and education | 7 | PASS |
| Common stores | 7 | PASS |
| Garden and island project | 9 | Existing/coastal/inland PASS; leased variant MISSING |
| Defense | 8 | PASS with Auxiliary lifecycle caveat |
| Foreign Commonwealth | 7 | PASS |
| Necessary Ground | 8 | PASS |
| Stewardship and status | 6 | Content present; ordering lifecycle FAIL |
| Crisis correction | 7 | Source present; visibility and four rejoins FAIL |
| Formation and mature play | 8 | PASS for normal routes; corrected routes FAIL |
| **Total** | **122** | **FAIL overall** |

### Graph and route locks

- 122 focus blocks and 122 unique IDs.
- 170 prerequisite references, zero unresolved references, and zero parents on the same or a lower row than their child.
- 54 directed mutual-exclusion references forming 27 symmetric pairs; zero asymmetric exclusions.
- Five mutually exclusive route openers and five matching normal route capstones exist.
- The normal formation focus accepts all five capstone focuses in one OR prerequisite block and also requires Island Made Real and First Associate.
- The two principal internal route forks are symmetric: Council Autonomy versus Emergency Central Plan, and Useful Freedom versus Exact Obedience.

### Costs, rewards, and pacing

- 18 short focuses at cost 5, 71 standard focuses at cost 10, and 33 long focuses at cost 15.
- Focus-owned Ledger movements use the shared 5/10/15 ladder and its negatives; the prohibited 2/4/7 pattern is absent.
- 34 paid-growth availability gates pair with 34 paid-growth calls: 26 institutional and 8 military.
- Every focus has `completion_reward` and `ai_will_do`.
- No current flag-plus-Ledger reward has an entirely unreferenced gameplay flag.
- The exact eleven previously orphaned rewards remain connected to lifecycle helpers, conduct flags, league state, or case-law state.
- No focus directly grants free divisions, free equipment, factories, cores, claims, war goals, or annexation.

### Cross-file references

- All 52 unique Event 15 scripted effect/trigger calls used by the focus file have definitions.
- The three directly referenced opening idea keys resolve; the route, Store, Garden, Auxiliary, and Stewardship keys called through lifecycle helpers are present in the idea package.
- Decision phases 1 through 9 have focus producers and threshold triggers consumed by decision-family visibility.
- The focus package has all 122 title keys and 122 description keys in `localisation/english/015_utopia_manifesto_focus_l_english.yml`.
- The read-only focus inspector resolved 122 of 122 titles and all 72 used focus sprite families to existing GFX/DDS assets.

These PASS results do not override the runtime visibility, route-rejoin, lifecycle, AI, and missing-variant blockers above.

## Validation evidence

- Read-only `hoi4_focus_inspect`: `FOCUS_INSPECTED`, no source blocker, 122 focuses, 122 resolved titles, layout hash `248b31c1cbdce685af214ec1665bd6f38037306c59fae3805b9e6876a27c6dff`.
- Read-only `hoi4_focus_render`: completed and produced HTML, SVG, PNG, JSON, source-map, and plan artifacts for the same source/layout hash.
- Independent source inventory: 122 unique focuses, 170 resolved prerequisite edges, 27 symmetric mutual-exclusion pairs, zero coordinate collisions, and no non-descending parent edge.
- Independent reference scan: 52 of 52 focus helper/trigger names resolve; all 244 focus localisation keys are present.
- Independent lifecycle trace covered acceptance, the day-5 circulation event, first-focus completion, route commitment, Store/Garden orderings, early Stewardship, Auxiliary start/resolve, crisis correction, and formation gates.
- Independent AI signal trace checked all five opener helpers against their actual flag/variable producers and scopes.

## Required re-audit

Do not reuse this FAIL as a completion claim after only one repair. The next focus-tree audit must verify all of the following together:

1. Dynamic visibility transitions for hidden reveal, route commitment, crisis entry, crisis resolution, and settled charter.
2. Every permitted different-route crisis switch through the selected route's first focuses, capstone, and current-route formation proof.
3. A maximum of three Event 15 spirits across early narrative events and every Store/Garden/Auxiliary/Stewardship ordering.
4. Comparative opener weights for democratic-stable, communist-industrial, neutral-landlocked, authoritarian-at-war, and high-education reformist actors, plus crisis exceptions.
5. A real leased-island project or an explicitly accepted spec amendment.
6. A fresh normal-scale render after topology changes, with route-capstone and formation connector-through-node cases removed.
7. Regression checks for the current PASS results: paid growth, decision phases, Ledger scale, formerly orphaned rewards, normal route formation, localisation, and icons.

## Simplifications, omissions, and blockers

- The current implementation silently substitutes Coastal Refuge plus a general lease enable flag for the accepted leased-island project. That is an unapproved simplification.
- The current layout remains a materially improved but incomplete visual cleanup; seven connector-through-node intersections and twenty long connectors remain.
- No gameplay, localisation, asset, or spreadsheet file was edited by this audit. The only audit-owned file is this report.
- No fallback, placeholder implementation, commit, staging operation, or gameplay simplification was introduced by the auditor.

## References and skills used

- Repo skills: `hoi4-focus-trees`, `chaos-redux-events`, and `chaos-redux-subagents`.
- Offline wiki: Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On Actions, Event Modding, Decision Modding, Idea Modding, AI Modding, and National Focus Modding.
- Official vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, localisation formatter documentation, and `common/script_constants/documentation.md`.
- Vanilla precedents: generic industrial/naval focus branches, Australian state-aware railway focuses, and German mutual-exclusion/relative-layout patterns; vanilla runtime `load_focus_tree` precedents were also checked.

No web Paradox wiki was used.
