# Event 015 Focus-Tree Completion Re-audit — 2026-07-15

Owner: `chaosx_focus_tree_auditor`  
Mode: read-only source audit; this handoff is the only file written  
Audit snapshot: `2026-07-15 13:51:27 +03:00`

## Verdict

**PASS for the current Event 015 focus source.**

- Focus-owned P0 findings: **0**
- Focus-owned P1 findings: **0**
- Focus-owned P2 findings: **0**
- Formal improvement-addendum closure: **not yet proved; tracked separately from this focus verdict**

The prior military-cap exploit is closed at both the focus gates and the shared effect guard. The two inconsistent focus textures and the one inconsistent decision texture are normalized. The current 124-node graph is complete, reachable, acyclic, and free of duplicate coordinates, upward prerequisite edges, and straight connector-through-node collisions.

A fresh 124-node engine-render artifact was **not** produced. No `hoi4.focus_*` capability is exposed in this audit session, and the preceding completion audit records the optional inspector's earlier `ARTIFACT_STORAGE_LIMIT`. This report therefore does not claim that a current engine render exists. Layout acceptance is based on the directly reviewed 122-node engine render from `focus_tree_layout_repair.md`, the exact bounded current delta from that rendered graph, and a fresh static audit of the complete 124-node source. That evidence is detailed below.

The formal improvement-loop addendum appears implemented in live source, but its own closure contract is still unmet: the addendum has not been promoted or rejected in an Event 15 source-of-truth record, no fresh event-completion audit is present, and the current decision/mission and country-package completion handoffs retain `FAIL` verdicts. Those package-level audits do not turn a passing focus source into a focus failure.

## Disposition of the previous findings

| Previous finding | Re-audit result | Current evidence |
| --- | --- | --- |
| P1 — focus military growth bypasses batch capacity | **Closed** | All eight military rewards use tier-matched `utopia_manifesto_can_pay_military_growth_*` availability, and `utopia_manifesto_apply_paid_focus_military_growth` independently refreshes costs/capacity and checks `utopia_manifesto_can_pay_military_growth` before creation. |
| P1 — current layout not proved | **Closed for the focus-source verdict, with the renderer limitation disclosed** | Prior 122/170 engine render was directly reviewed; the current layout delta is exactly two island focuses, four prerequisite connectors, and two existing-node x moves. Fresh current graph: 124/174, one root, full reachability, no cycles, no duplicate coordinates, no non-downward edges, and zero straight connector-through-node cases. |
| P1 — formal addendum closure incomplete | **Still unresolved, but not a focus-source defect** | Source tranches are present. Required cross-system audits and source-of-truth disposition remain incomplete. |
| P2 — two focus textures were `95x85` | **Closed** | Both current textures are `94x86`; all 74 referenced focus textures use the same size contract. |
| P2 — one decision texture was `64x64` | **Closed** | `decision_utopia_archipelago_network.dds` is `32x32`; all 46 referenced decision textures use the same size contract. |

## Current graph and layout evidence

### Static graph result

- Focuses: **124**
- Prerequisite references: **174**
- Root: `utopia_manifesto_recover_the_manuscript`
- Reachable from root: **124/124**
- Missing prerequisite ids: **0**
- Cycles: **0**
- Duplicate coordinates: **0**
- Non-downward prerequisite edges: **0**
- Coordinate span: `x = -2..52`, `y = 0..16` — 55 columns by 17 rows
- Proper straight-segment crossing diagnostic: **53**
- Straight connector-through-unrelated-node diagnostic: **0**

The 53 crossing count is a conservative straight-line diagnostic. It is not an engine-routed connector count and is not presented as one.

### Prior rendered evidence and exact current delta

`focus_tree_layout_repair.md` records a directly reviewed final inspector render with:

- 122 focuses and 170 engine connectors;
- width 55, height 17;
- 50 engine-routed connector crossings;
- 7 engine-routed connector-through-node warnings, none in the opening/route band and none incident to the five route openers;
- 20 long connectors;
- a directly reviewed PNG at 4,904 by 1,046 pixels.

The current source differs from that rendered 122-node graph only on the bounded layout surface described by the assignment:

1. `utopia_manifesto_the_archipelago_network` at `(5, 9)`, prerequisite `utopia_manifesto_choose_the_island`.
2. `utopia_manifesto_the_leased_island` at `(9, 10)`, prerequisite `utopia_manifesto_choose_the_island`.
3. Both variants are added to the existing `utopia_manifesto_build_the_island` OR-prerequisite group, producing exactly four added prerequisite connectors in total.
4. `utopia_manifesto_homes_near_work` moved from `x = 16` to `x = 15`.
5. `utopia_manifesto_commonwealth_defense_compact` moved from `x = 50` to `x = 48`.

Removing the two new variants and reverting those two x values reconstructs a 122-node/170-edge graph. In straight-line geometry, the old x values put these connectors through unrelated focuses:

- `utopia_manifesto_count_houses_and_hands -> utopia_manifesto_homes_near_work` through `utopia_manifesto_the_first_common_store`;
- `utopia_manifesto_a_small_army_well_housed -> utopia_manifesto_commonwealth_defense_compact` through `utopia_manifesto_necessary_victory`.

The two current x moves remove both cases. The two added island variants introduce no missing reference, cycle, duplicate coordinate, upward edge, unreachable node, or straight connector-through-node case. The current worktree layout diff contains no other prerequisite, mutual-exclusion, or coordinate edit.

## Accepted focus surfaces

### Five routes and constitutional correction

**Pass.** The five mutually exclusive interpretations remain distinct and complete:

| Route | Opener | Capstone |
| --- | --- | --- |
| Consent of Households | `utopia_manifesto_household_gives_consent` | `utopia_manifesto_commonwealth_by_consent` |
| Common Table | `utopia_manifesto_nothing_private_in_necessity` | `utopia_manifesto_union_of_tables` |
| Guardians of Measure | `utopia_manifesto_country_measured` | `utopia_manifesto_perfect_measure` |
| Closed Island | `utopia_manifesto_one_island_one_measure` | `utopia_manifesto_perfect_island` |
| Joke Understood / open humanism | `utopia_manifesto_read_island_as_a_mirror` | `utopia_manifesto_good_place_that_admits_its_limits` |

Every opener calls its route setter and `utopia_manifesto_commit_current_route_identity`. The hidden route remains guarded by `allow_branch` and `utopia_manifesto_can_reveal_joke_understood`, rather than being permanently visible.

The founding crisis exposes five mutually exclusive correctors: `restore_consent`, `empower_the_councils`, `give_the_surveyors_authority`, `seal_the_island`, and `admit_the_book_was_a_question`. Each corrector sets the intended route, commits identity, records the route-specific correction, completes the matching opener through `unlock_national_focus`, and resolves the crisis. `utopia_manifesto_a_settled_interim_charter` has one OR-prerequisite group containing all five correctors, so every correction rejoins the shared tree.

### Dynamic visibility

**Pass.** `utopia_manifesto_refresh_focus_visibility` calls `mark_focus_tree_layout_dirty` only for a live accepted actor. All five route setters, island-variant commitment, crisis entry, and crisis resolution call this helper. Hidden and correction branches therefore refresh after the state transition that controls their `allow_branch` blocks.

### Island, archipelago, and fixed lease

**Pass.** The island branch contains exactly five mutually exclusive variants: existing island, archipelago network, leased island, coastal refuge, and inland island.

- Archipelago selection requires the live archipelago trigger, records multiple island project states, and requires the configured state count before site proof is granted. Reconciliation removes invalid/lost/non-island states and strands the project when the required network no longer exists.
- Leased selection requires a live maritime/settlement deficit and a viable foreign lessor with an eligible controlled island state. Committing the variant opens the existing Necessary Ground lease case instead of granting territory for free.
- Lease start records exactly one lessor and one leased project state, marks only relations created by this system, applies the lease state package, starts `mission_utopia_hold_island_project_lease`, and clears the completed case.
- `decision_utopia_propose_island_lease_renewal` pays political power, convoys, and support equipment before events `.213/.214`. Acceptance or a counteroffer extends both the stored term and the active mission timeout; refusal leaves the fixed expiry live.
- Mission cancellation or timeout calls `utopia_manifesto_expire_island_project_lease`. Expiry returns control where the recorded lessor is still valid, removes only system-created access/guarantee relations, clears lease state and downstream proof, marks the project stranded, and reopens the lease-case requirement.
- Ownership/controller on-actions reconcile the island scopes while suppressing recursion during the return transaction.
- The paid replan decisions cover existing/coastal/inland/archipelago/leased alternatives. They clear old island proof and lease state through the shared replan helper, so an expired lease cannot leave a false completed site.
- Terminal island cleanup returns an active lease first, then clears state flags, modifiers, arrays, lessor flags, timers, and missions.

### Idea cap

**Pass.** The Event 15 idea lifecycle still has three mutually replacing slots, not one permanent spirit per focus:

1. Opening: Founding Text + administrative-knowledge burden + property-order burden = 3.
2. Route commitment clears Founding Text, normalizes the other opening families, and adds one route-institution stage = at most 3.
3. Common Store replaces the knowledge slot.
4. Garden District or Stewardship replaces the property slot; those families do not coexist.
5. Auxiliary dependency replaces the route-institution slot, and resolution restores exactly one recorded route stage.
6. Second Generation clears residual opening-family burdens.

Every stage helper clears its complete family before adding the next stage. The focus file directly adds only the three guarded opening ideas. No current ordering exceeds three visible Event 15 country ideas.

### Paid military and institutional growth in every ordering

**Pass.** The focus file contains **8** paid military rewards and **26** paid institutional rewards. It contains exactly 8 matching military tier gates and 26 matching institutional tier gates.

The eight military focus call sites are:

- `utopia_manifesto_households_of_service` — foundation;
- `utopia_manifesto_perfect_island` — capstone;
- `utopia_manifesto_the_citizen_watch` — foundation;
- `utopia_manifesto_engineers_before_generals` — foundation;
- `utopia_manifesto_a_small_army_well_housed` — network;
- `utopia_manifesto_commonwealth_defense_compact` — capstone;
- `utopia_manifesto_mutual_defense_without_mastery` — network;
- `utopia_manifesto_the_commonwealth_at_war` — capstone.

Each availability block uses `utopia_manifesto_can_pay_military_growth_foundation`, `_network`, or `_capstone`; each of those combines tier affordability with `utopia_manifesto_military_growth_capacity_available`. The shared focus helper then refreshes the live capacity and dynamic costs and checks the generic `utopia_manifesto_can_pay_military_growth` again before it can call the only unit-creation executor. The executor charges manpower, infantry equipment, support equipment, and army experience before creating one institution-specific formation, then increments the shared batch counter.

The decision helper uses the same generic capacity guard and counter. Consequently, focus-first, decision-first, and interleaved orderings all consume the same capacity. Capacity is rebuilt from the centralized base, controlled-state, and chartered-district constants and clamped to the centralized maximum.

Institutional growth remains deliberately distinct: it charges manpower, support equipment, and political power, changes the Ledger rather than creating units, and increments its own proof counter. All 26 focus gates use the matching tier snapshot, while the shared helper refreshes and rechecks current affordability immediately before payment. Institutional growth has no military-style unit batch cap because it creates no formations; the relevant completion requirement is real payment in every ordering, which is enforced.

### AI

**Pass.** All **124/124** focuses contain `ai_will_do`. The separate AI strategy file contains **12** plans and all 12 use `abort_when_not_enabled = yes`.

Route opener weights inspect route-appropriate government, stability, Ledger, war/surrender, industry/research, geography, and conduct state. The new archipelago and lease weights inspect secure reserves and the absence of better domestic island options. Crisis correction, paid growth, lease renewal/replanning, formation, and post-formation actions use the same availability/cost gates as the player. The repaired military guard therefore closes the previous AI ordering bypass as well as the player bypass.

### Formation, succession, and post-formation play

**Pass.** `utopia_manifesto_proof_of_the_commonwealth` accepts one of the five capstones, requires the island/city/associate proof bands, and exposes the paid formation decision only when the route-specific proof trigger passes.

The proclamation deducts political power, support equipment, trains, and convoys before firing `.10`. The successful option calls `utopia_manifesto_form_current_route_identity`, which revalidates proof and changes politics, institutional leader presentation, flags, and cosmetic identity only. The formation call graph does not annex league members, transfer the actor's states, add or remove cores, replace its original tag, replace its OOB, delete existing forces, or refund proclamation costs.

The shared post-formation band remains reachable: regional proclamation, ring integration, Second Generation, Rule for Need, Beyond the Founder's Island, Commonwealth at War, and Plenty in an Age of Chaos. Second Generation dispatches four institutional successors—Commonwealth Council, Rotating Congress, College of Measure, and Directorate of Service—and records the hidden humanist constitutional-election succession without adding an unrelated ruler.

## Assets and localisation

**Pass.** Fresh reference inventories produced these results:

- 74 unique focus icon references: 74 base sprites, 74 shine sprites, 74 existing textures, and 74 textures at `94x86`.
- 50 idea ids using 12 unique picture handles: 12 registered sprites and 12 existing textures.
- 46 unique decision icon references: 46 registered sprites, 46 existing textures, and 46 textures at `32x32`.
- 20 unique character portrait handles: 20 registered sprites with existing textures.
- Five route cosmetic identities: 25 base/ideology flags in each of `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small` — 75 files total.
- 124 focus ids: all 248 title/description localisation keys resolve.
- 50 idea ids: all 100 title/description localisation keys resolve globally.
- Nine Event 15 English localisation files are present; no focus or idea key required by this audit is missing.

The three previously inconsistent files are now:

| Texture | Current size | SHA-256 |
| --- | ---: | --- |
| `goal_utopia_archipelago_network.dds` | `94x86` | `0BC4F574328AA9E931B54E09C96EBF04FF91A3AE1FBCE75FEB9955BD8EC36D20` |
| `goal_utopia_leased_island.dds` | `94x86` | `9DA7BC9542FA4F543629D42901723E2D24D92DA340EA5B54BA521EA077360021` |
| `decision_utopia_archipelago_network.dds` | `32x32` | `3B976E4C9DAFD8214CF4C729AED24AC2AA43DF7D6E7B1903240D4916029A5F25` |

`interface/015_utopia_manifesto.gfx` still contains two unused historical idea sprite registrations whose texture files are absent (`GFX_idea_utopia_league_of_need` and `GFX_idea_utopia_utopian_league`). Neither handle is referenced by the current idea file, focus tree, or audited decision surface. They are dead interface declarations, not missing assets for an accepted or live focus surface, and therefore do not change this verdict.

## Formal improvement-loop status

### Source implementation

The four bounded tranches named by the formal addendum remain present in current source:

- living Ledger rebuild with separate durable policy/current-condition components, actor-scoped refresh hooks, calling structural pressure, durable relief, and cleanup;
- fifteen evolution-choice consumers routed into existing systems;
- four district-role suitability records plus housing, transport, and role-plan obligations, partial/failure handling, route charter consequences, and cleanup;
- one paid Closed Island Penal Works method attached to the existing district project, with state modifier, visible material/conduct costs, incidents, terminal cleanup, and the shared `chaos_meter_register_deaths` path through the common civilian-population-loss transaction.

The addendum itself says the 124-focus tree is already broad enough and must not gain nodes merely to display addendum work. No additional focus content is required for those tranches.

### Closure evidence

The addendum is **not yet resolved as a package-level completion record**:

- `015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md` still states that it is bounded implementation work and does not amend the accepted specifications.
- No Event 15 spec, canonical event document, or source-of-truth map records the addendum as promoted or formally rejected.
- `decision_mission_completion_audit_2026_07_15.md` currently says `FAIL`.
- `country_package_completion_audit_2026_07_15.md` currently says `FAIL`.
- `localisation_completion_handoff_2026_07_15.md` reports its scoped localisation inventory complete.
- No fresh event-completion audit handoff is present.

These are closure-evidence facts, not a finding that an accepted focus route, focus reward, focus gate, focus asset, or focus localisation key is missing. A global Event 15 completion claim must wait for the parent-owned audits and documentation disposition; this focus-source verdict does not wait on unrelated concurrent audit ownership.

## Exact source snapshot

| File | Lines | SHA-256 |
| --- | ---: | --- |
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | 3,546 | `71B11D239FF3D380CDF5E9BAB3E0D50825E8E604D22671228B7BDE97AC1F1514` |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | 5,282 | `056CD6C600F3D81B3E68CBCC46B3A9D8CF2EB9C7FEE970ADA7E1E4583A3B8C67` |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | 2,354 | `8A24EF272BBEF9CC82E9383AD9E9662C3B5D638B738E1985D7D6A0945BB046ED` |
| `common/scripted_effects/015_utopia_manifesto_country_effects.txt` | 496 | `078CCD44EF44D768E1954B3BEB914726417FA742A0FE35F8BC5C5938977998AA` |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | 862 | `25C9760A5E658C358FFCB103F739EB0EFB80C7373D787A536B5BD4897DC864AB` |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | 2,751 | `6D74B0822DCA7C08A6104E529C4508B4EA5B627B2CCC5CE0AB25B09D9219E1FB` |
| `common/decisions/015_utopia_manifesto_decisions.txt` | 5,075 | `A8D9C6C9770BA38FD5D3A774314D0A58C43230E5FDC2088345280C6F28732881` |
| `common/ideas/015_utopia_manifesto_ideas.txt` | 488 | `84F1E322EF827EDD4EEDFF68BA99E67AE61E6C4ED1172193CF77EB3F4D05326A` |
| `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` | 288 | `E6DB306460F20B84CB452FAAFC300D062A318CBD5B48EB01BB8A24DA30658CBB` |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | 267 | `A1EE56233CC003BBD755C7CD514F6D1B2645C8A83D13933903374021A5FFC72D` |
| `events/015_utopia_manifesto.txt` | 5,000 | `3479C36B2BDBA6DFF1B4A9D0F5D564B3C7E8533A426B5186C8E9F9C318ADE7CC` |
| `interface/015_utopia_manifesto.gfx` | 1,857 | `218CC01E81AD28ABEA77F9AF2C0E6B50049C7376BB68691E01ED0E9F627A8E39` |
| `localisation/english/015_utopia_manifesto_focus_l_english.yml` | 252 | `8D403D3CD8AA8E5B2D63A6FA465EF916D5FE8EBFDA0668C6E89807AD507C1437` |
| `localisation/english/015_utopia_manifesto_ideas_l_english.yml` | 137 | `C581BB8CCD5C736652ECF3D0907925E34A275F3E299E2D617DDCBC74E33644B0` |
| `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md` | 737 | `DAD6C464047BF5C25E92D4865F7E6F5D975B28EFB86E1C6CEA58092976A162B3` |

## Evidence boundaries

- No fresh current engine render was produced, and this report does not imply otherwise. The optional focus tools are not exposed in this audit session; the previous audit documents the earlier artifact-storage failure.
- The fresh 53-crossing and zero-through-node results are static straight-line diagnostics, not engine routing metrics.
- No live game scenario was executed for the five routes, lease expiry, cap ordering, formation, or succession. The conclusions above are source-call-graph and state-transition audits bound to the listed hashes.
- This focus re-audit does not substitute for the addendum's parent-owned decision, event, country-package, or localisation completion audits.

## Simplifications, omissions, blockers, and fallbacks

- No accepted focus route, correction route, island variant, focus reward, AI surface, formation step, succession path, focus asset, or focus localisation surface was omitted.
- No gameplay fallback or simplified substitute was accepted.
- No gameplay, localisation, asset, spec, spreadsheet, or interface source was edited.
- The only evidence limitation is the explicitly disclosed absence of a fresh 124-node engine render. The prior reviewed render plus exact bounded delta and fresh current graph were used as the authorized re-audit evidence path, not represented as a new render.
- There is no blocker to the **focus-source PASS**. The formal addendum remains blocked from a package-level closure claim by its incomplete audit/disposition record.
- No commit was created, as required by the assignment.

## Skills and references used

Skills:

- `hoi4-focus-trees`
- `chaos-redux-events`
- `chaos-redux-subagents`
- `hoi4-decisions-missions`

Offline wiki snapshot pages:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- National focus modding

Vanilla documentation and precedents:

- `documentation/script_concept_documentation.md`, including Script Constants
- `common/script_constants/documentation.md`
- relevant `effects_documentation.md` entries for focus-tree refresh/unlock, ideas, identity, and variables
- relevant `triggers_documentation.md` entries for focus, ideas, flags, equipment, and variable comparison
- vanilla dynamic `allow_branch`/`mark_focus_tree_layout_dirty` and `unlock_national_focus` precedents, including Spain and Ethiopia focus/event patterns

Accepted Event 15 references included the focus architecture, focus graph, route matrix, idea lifecycle matrix, AI matrix, completion matrix, country/formation specification, AI/balance specification, asset acceptance specification, formal improvement addendum, the prior completion audit, and the 122-node layout-repair render handoff.
