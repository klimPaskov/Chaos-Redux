# Event 15 focus-tree completion audit — 2026-07-15

## Verdict

**FAIL.** The current Event 15 focus package is structurally complete and substantially implements the accepted design, but it does not meet the completion bar at this snapshot.

- P0: 0
- P1: 3
- P2: 2

The decisive gameplay defect is a reproducible focus/decision ordering exploit that bypasses the military-growth cap. The tree is also too wide and crossing-heavy to treat layout readability as proved without a current rendered inspection. Finally, the formal improvement-loop addendum cannot be closed until its required fresh audits and source-of-truth disposition exist.

Audit snapshot: `2026-07-15 12:48:40 +03:00`. The worktree was actively shared and dirty; the SHA-256 values below bind every conclusion to the exact files inspected.

## P1 findings

### P1 — focus military growth bypasses the real capacity cap

The ordinary paid-growth decision path is correctly bounded: `utopia_manifesto_can_pay_military_growth` includes `utopia_manifesto_military_growth_capacity_available` in `common/scripted_triggers/015_utopia_manifesto_triggers.txt:2538`.

The focus path is not bounded:

- `utopia_manifesto_apply_paid_focus_military_growth` checks only `utopia_manifesto_can_afford_military_growth` at `common/scripted_effects/015_utopia_manifesto_effects.txt:4881`; it does not check capacity.
- The eight affected focus gates also use affordability rather than the matching `can_pay` trigger: `common/national_focus/015_utopia_manifesto_focus_tree.txt:1137`, `:1321`, `:2281`, `:2312`, `:2337`, `:2482`, `:2631`, and `:3493`.
- `utopia_manifesto_execute_paid_military_growth` increments the batch count after payment. There is no terminal clamp that repairs the omitted gate.

Reproduction by source ordering: use paid military decisions until `utopia_manifesto_military_growth_batches == utopia_manifesto_military_growth_capacity`, then complete any still-available affected focus while its resources are affordable. The focus remains available and adds another batch. In the maximal ordering, eight focus rewards can be taken above the intended capacity.

Costs are real and military growth remains institutionally distinct from the separate institutional-growth path, but the accepted requirement was a real cap in all relevant orderings. That requirement fails.

Required correction: use the tier-matched `utopia_manifesto_can_pay_military_growth_*` gates on all affected focuses and make the shared focus effect independently enforce capacity before executing. The effect-side guard is required even if all current focus availability blocks are corrected.

### P1 — focus layout readability is not proved and static geometry shows a material risk

The structural graph passes: 124 nodes, one root, full reachability, 174 valid prerequisite edges, no cycles exposed by prerequisite closure, no missing references, no non-downward edges, and no duplicate coordinates.

The layout itself is not completion-proof:

- coordinate span is `x = -2..52`, `y = 0..16`, or 55 focus columns;
- the longest direct prerequisite edge spans 20 columns;
- a proper straight-segment intersection audit, excluding shared endpoints, finds **53 crossing edge pairs**;
- representative crossings include `utopia_manifesto_households_of_service -> utopia_manifesto_penal_works` across `utopia_manifesto_the_closed_store -> utopia_manifesto_natural_right_of_need`, and `utopia_manifesto_paid_public_lectures -> utopia_manifesto_independent_need_review` across three separate shared-branch edges.

This geometry test is a diagnostic, not a substitute for the engine renderer. The optional focus inspector was unavailable in the prior attempt because artifact storage was exhausted, and no fresh rendered tree artifact was available to this audit. Because the task requires topology **and layout** to be proved, the combination of 53 predicted crossings, 55-column width, and absent rendered evidence is a P1 completion/visual-validation blocker.

### P1 — formal improvement-loop closure gate is unmet

The four substantive addendum tranches appear in current source:

- live Ledger base/policy/current contribution rebuilding with hysteresis and bounded refresh hooks;
- downstream consumers for the five evolution deliveries;
- state-suitability and obligation logic for district roles;
- Penal Works as a costly state project with incidents, cleanup, and the shared exact civilian-population-loss hook.

However, the addendum explicitly says older audit snapshots cannot prove completion and requires fresh decision, event, country-package, and localisation audit handoffs plus promotion or formal rejection in the Event 15 source-of-truth record (`015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md:674-704`). At this snapshot, the fresh event-completion and localisation audit handoffs and a source-of-truth promotion/rejection record are absent. Therefore the addendum may be described as implemented in source, but not resolved or accepted as complete.

## P2 findings

### P2 — focus icon dimensions are internally inconsistent

All 74 focus icons referenced by the 124 nodes have registered base sprites, shine sprites, and existing textures. Among the referenced textures, however, 72 are `94x86` while the two new island-variant icons are `95x85`. The complete Event 15 goal folder contains 111 DDS files with no duplicate SHA-256 groups, so this is not placeholder duplication; it is a normalization and rendered-alignment concern.

### P2 — one decision icon uses a different size contract

All 46 referenced Event 15 decision icons resolve to registered existing textures. Forty-five are `32x32`; `decision_utopia_archipelago_network.dds` is `64x64`. This should be normalized or explicitly rendered and accepted.

## Acceptance matrix

| Requirement | Result | Evidence |
|---|---:|---|
| Complete topology and structural reachability | PASS | 124/124 nodes reachable from `utopia_manifesto_recover_the_manuscript`; 174 edges; 0 missing references; 0 non-downward edges; 0 duplicate coordinates |
| Rendered layout readability | **FAIL** | 55-column span, 20-column longest edge, 53 predicted proper crossings, no current rendered proof |
| Five political routes, including hidden Joke route | PASS | Five route setters, five capstones, mutual exclusion, hidden reveal trigger, route-local AI weights |
| Constitutional correction and shared rejoin | PASS | Five mutually exclusive correctors; each sets and commits its route, records correction, unlocks the corresponding opener, resolves crisis; `utopia_manifesto_a_settled_interim_charter` uses one OR prerequisite block containing all five correctors |
| Dynamic `allow_branch` refresh | PASS | `utopia_manifesto_refresh_focus_visibility` calls `mark_focus_tree_layout_dirty`; route, crisis, and island setters call the refresh helper |
| Leased-island selection, lease lifecycle, expiry, and recovery | PASS | Five island variants exist; leased selection requires a viable foreign island; lease state/lessor tracking, renewal, expiry return, stranded state, alternate paid replans, and a renewed leased-site recovery path are all wired |
| At most three visible Event 15 ideas in relevant orderings | PASS | Exact abstract slot-state trace reaches a maximum of 3; the focus file directly adds only the three opening spirits at lines 61, 111, and 210; route, garden/property/stewardship, and route/auxiliary helpers clear their slot families before replacement |
| Paid military growth, institutional distinction, real caps | **FAIL** | Costs/distinction pass; focus ordering bypasses the military batch capacity as detailed above |
| AI state awareness and focus weights | PASS with cap defect | 124/124 focuses have `ai_will_do`; 12 AI strategy plans; route preference/avoidance triggers inspect government, stability, Ledger bands, war/surrender, industry/research, geography, shortages, and conduct; AI shares the focus cap bug |
| Formation preserves tag, territory, cores, costs, and forces | PASS | Formation call graph contains no annex, transfer, core grant/removal, resistance erasure, free stockpile/manpower/unit/OOB/technology effects, or cost refund; paid proclamation fires `.10`, successful option forms first and then records post-formation state |
| Route identities and flags | PASS | Five route-specific cosmetic identities; all 75 required flag files exist: five identities x five base/ideology variants x three sizes |
| Post-formation and Second Generation | PASS | Regional proclamation, ring integration, Second Generation, Rule for Need, mature war/plenty focuses, succession helper, four institutional successors, and humanist constitutional elections are present |
| Opening milestone events `.2` through `.15` are live | PASS | `.4` is called by Interpretive Congress at focus line 190; `.12` by Interim Charter at line 217; `.13` by First Common Store at line 144; `.7` is fire-once from crisis entry with no self-recursion; `.10` fires after proclamation costs; other opening milestones have decision/pulse/event callers |
| Focus, idea, decision, character, and flag assets | PASS with P2 normalization notes | 0 missing registered sprites or textures across 74 focus, 12 idea, and 46 decision icon references; character and route-flag references resolve |
| Focus and idea localisation | PASS | 124 focus IDs have all 248 title/description keys; 50 idea IDs have global title/description keys (the `perfect_measure` pair deliberately resolves from focus localisation); all eight Event 15 English localisation files have UTF-8 BOM |
| Formal improvement-loop addendum | **FAIL closure gate** | Source tranches appear implemented, but mandatory fresh audit/promotion evidence is incomplete |

## Route, branch, and lifecycle proof notes

### Five routes and correction reachability

The five capstones are `utopia_manifesto_commonwealth_by_consent`, `utopia_manifesto_union_of_tables`, `utopia_manifesto_perfect_measure`, `utopia_manifesto_perfect_island`, and `utopia_manifesto_good_place_that_admits_its_limits`. All nodes are in the prerequisite closure from the single root.

The crisis correctors are `utopia_manifesto_restore_consent`, `utopia_manifesto_empower_the_councils`, `utopia_manifesto_give_the_surveyors_authority`, `utopia_manifesto_seal_the_island`, and `utopia_manifesto_admit_the_book_was_a_question`. The fifth is correctly guarded by `utopia_manifesto_can_reveal_joke_understood`. `unlock_national_focus` completes the matching opener without rerunning its reward, while each corrector performs the route setter and identity commit itself; this mirrors the documented engine behavior and does not leave a missing route initialization.

`utopia_manifesto_the_founding_crisis` calls the idempotent entry helper even though the crisis flag already made the branch visible. That attempts fire-once event `.7` again, but `.7` has `fire_only_once = yes` and the entry helper does not call itself. This is redundant but not recursive or blocking.

### Idea cap proof

The lifecycle has controlled slots rather than one persistent spirit per focus:

1. Opening state: Founding Text + Unmeasured Country + Inherited Order = 3.
2. Route commitment removes the Founding Text slot, normalizes the knowledge/property slots, and adds exactly one route-institution spirit = at most 3.
3. Garden settlement replaces the property slot; stewardship replaces garden/property; neither stacks with its predecessor.
4. Auxiliary service clears the route-institution slot; restoration clears auxiliary and restores one route-institution stage.
5. Second Generation clears any residual opening burdens.

Exhaustive abstract ordering over those replacement operations never exceeds three concurrent Event 15 country ideas.

### Formation proof

The paid proclamation decision at `common/decisions/015_utopia_manifesto_decisions.txt:4946-4970` deducts political and material costs before firing `chaosx.nr15.10`. In `.10a`, `utopia_manifesto_form_current_route_identity` runs before post-formation achievement/transition cleanup. If proof is invalid, `.10b` records deferral rather than refunding or silently forming. Identity selection changes politics, characters, and the route cosmetic tag only; it does not annex, grant free cores, erase resistance, replace the army, or grant free equipment/technology.

## Exact source snapshot

| File | Lines | SHA-256 |
|---|---:|---|
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | 3546 | `CEF02BF44C1020B13EAA4423DF19218BD888B82C12C1A8687C654EBDCB3A1DA7` |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | 5264 | `9CEEF77E0C71A84FAD6D6B08D2CC3C6D892E8D2B9EE29CA05D220CE288C16AAB` |
| `common/scripted_effects/015_utopia_manifesto_country_effects.txt` | 496 | `078CCD44EF44D768E1954B3BEB914726417FA742A0FE35F8BC5C5938977998AA` |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | 912 | `AC2A56D4859FAAFF641E5567E7B0C34FBDC60F47C4A9ED5AB6E2399B19579488` |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | 2347 | `A4CC59EC21F920C4AA199465329A57E725DFFB13DAAE0E10AB6AAF864AFD07DB` |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | 2745 | `98E319A1FAA99C56029576194378C20C3866C2FB8C40364AD5AA203092D51419` |
| `common/ideas/015_utopia_manifesto_ideas.txt` | 488 | `84F1E322EF827EDD4EEDFF68BA99E67AE61E6C4ED1172193CF77EB3F4D05326A` |
| `common/decisions/015_utopia_manifesto_decisions.txt` | 5053 | `16097FCFD0DCA2C45B15ECDBC16EFFE8B002B470BFD7713E34119771D9A4BB0E` |
| `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` | 288 | `E6DB306460F20B84CB452FAAFC300D062A318CBD5B48EB01BB8A24DA30658CBB` |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | 243 | `9F50786EFD19B7EEF56DCB36ACF82DFC59775F7BA3BFAAA5B27027CC6F5D5A8F` |
| `events/015_utopia_manifesto.txt` | 4474 | `A44FAE2E8B6D6FA7A0AAB71ED496F522AFC3AA6D186DF6E4FC16D80466430752` |
| `common/characters/015_utopia_manifesto_characters.txt` | 399 | `5CDF2EA793216351B5A250BBB1BB0EEA84103E7668791B30867216AF436749CB` |
| `interface/015_utopia_manifesto.gfx` | 1857 | `218CC01E81AD28ABEA77F9AF2C0E6B50049C7376BB68691E01ED0E9F627A8E39` |
| `localisation/english/015_utopia_manifesto_focus_l_english.yml` | 252 | `DE669AD9CF3BC0A16218B2ABA8E77109772FD897BC82954C4663A8D4747E111D` |
| `localisation/english/015_utopia_manifesto_ideas_l_english.yml` | 113 | `3B3662D4B55E76B3C927C2827A1495BFD0F0A93C0F413FAE4CC3634A0EB1B559` |
| `specs/015_utopia_manifesto_spec_part_3_focus_tree_architecture.md` | 1231 | `27F5A6CE61E7C9CD90315A8F122F67F76715B77729D19D9E4AE659F722799317` |
| `matrices/focus_route_matrix.md` | 21 | `2F8F3953A1FB708602086C76CCB2995847DF91EFEB4BC12B023EE0C96542DFC4` |
| `matrices/idea_lifecycle_matrix.md` | 18 | `DCC5006DF14E47BF0D5EBD4B0B1171E71B4090FA1FB1E9A892942584839D7D43` |
| `matrices/country_package_matrix.md` | 18 | `EAB83A4F8D8286290A251DE772CDE199513790359B5AEF3E6CB16F16A0924C30` |
| `matrices/completion_coverage_matrix.md` | 35 | `A3A54C8A8C84E975FF67628002A85CDAA78500DCF1C68752AAF84AC4AB35DC1E` |
| `015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md` | 737 | `DAD6C464047BF5C25E92D4865F7E6F5D975B28EFB86E1C6CEA58092976A162B3` |

## References consulted

Skills used: `hoi4-focus-trees`, `chaos-redux-events`, `chaos-redux-subagents`, and `hoi4-decisions-missions`.

Offline wiki snapshot pages consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.

Vanilla documentation consulted: `script_concept_documentation.md` (including Script Constants), `common/script_constants/documentation.md`, `effects_documentation.md`, and `triggers_documentation.md`. Vanilla precedents checked include dynamic focus layout refresh through `mark_focus_tree_layout_dirty` and route correction/completion through `unlock_national_focus`.

## Meaningful validations not performed

- No current engine-rendered focus-tree inspection was available; the geometric crossing result must not be mistaken for a screenshot or engine-layout result.
- The optional focus inspector was not retried because its previous `ARTIFACT_STORAGE_LIMIT` failure made another artifact-producing call unlikely to add evidence.
- No live scenario execution was performed for each route, lease expiry/recovery, cap-ordering exploit, formation, or succession. The cap defect is nevertheless source-reproducible.
- This focus audit did not substitute for the addendum's required fresh event-completion or localisation audits.

## Simplifications, omissions, and fallbacks

No gameplay, localisation, asset, spec, or spreadsheet source was edited. The only written file is this audit handoff. No fallback mechanic or simplified implementation was accepted. Static graph geometry was used only as an explicitly limited diagnostic; it was not presented as an engine render.

Completion can be reconsidered after the focus growth gates/effect enforce capacity, a current rendered layout demonstrates acceptable readability or the layout is repaired, and the formal addendum's audit/promotion gate is satisfied.
