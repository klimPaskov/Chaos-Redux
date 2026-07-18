# Event 015 focus-tree final audit

Date: 2026-07-18  
Role: `chaosx_focus_tree_auditor`  
Mode: fresh audit of the exact current source, with one narrow helper correction  
Verdict: **PASS after patch**

## Outcome

Event 015's replacement tree meets the accepted focus architecture. The audited tree contains 124 unique focuses and 174 valid prerequisite references; all 124 focuses are structurally reachable from one root. All five political routes, including the reveal-gated humanist recovery, and every required shared lane are present. The tree has explicit AI on all 124 focuses, 34 failure-closed paid focuses, complete focus localisation, complete focus/shine icon wiring, and no free equipment, divisions, cores, annexations, or state transfers in the focus-reachable reward chain.

One P2 defect was found in an associated identity helper and patched. The helper used the nonexistent script constant `constant:utopia_manifesto_case_method.none` when clearing a temporary achievement input. The declared sentinel is `.unset`; the correction at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:713` makes the focus-adjacent source set resolve 388/388 referenced script constants.

No focus definition, focus id, route condition, reward, AI weight, localisation key, or icon id was changed by this auditor.

## High-priority findings first

| Priority | Finding | File and identifier | Disposition |
| --- | --- | --- | --- |
| P0 | None | — | — |
| P1 | None | — | — |
| P2 | The peaceful-case achievement helper reset `utopia_manifesto_achievement_case_method_input` with undeclared `constant:utopia_manifesto_case_method.none`. A failed reset could leave invalid/stale temporary method state after a case-resolution call. | `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:713`; `utopia_manifesto_record_achievement_peaceful_case_resolution`; declared category at `common/script_constants/015_utopia_manifesto_constants.txt:365` | Patched to `constant:utopia_manifesto_case_method.unset`; constant audit now resolves 388/388. |
| P3 | None | — | — |

Open P0-P3 findings after the patch: **0**.

## Frozen audited snapshot

These hashes describe the files used for the verdict. The identity-effect hash includes the one-token correction above.

| SHA-256 | Lines | Source |
| --- | ---: | --- |
| `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` | 4,119 | `common/national_focus/015_utopia_manifesto_focus_tree.txt` |
| `d84f8357ae4aa1cfb4e92cf11c07ad0f7894de9ae2972fcd2e492cb4250decdc` | 3,501 | `common/scripted_triggers/015_utopia_manifesto_triggers.txt` |
| `6d226343835f1de50f63a07378b7a84c7d04a91f44691c1643ca804b84b519c4` | 8,044 | `common/scripted_effects/015_utopia_manifesto_effects.txt` |
| `078ccd44ef44d768e1954b3beb914726417fa742a0fe35f8bc5c5938977998aa` | 496 | `common/scripted_effects/015_utopia_manifesto_country_effects.txt` |
| `36cd2cc4c245f19a2a8f6bb7660ccaa77e630a681504cd50a1184180a8083c63` | 972 | `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` |
| `85dbaf6a8f66517e27d61685390cfe178e2aa6efafae46a80eb4e8284d649a74` | 677 | `common/script_constants/015_utopia_manifesto_constants.txt` |
| `b54d543548255f116fe73aa055b274b845a4dbc7dba6fa0d8bcd083ea72df1d1` | 239 | `common/script_constants/015_utopia_manifesto_decision_constants.txt` |
| `84f1e322ef827edd4eedff68ba99e67ae61e6c4ed1172193cf77eb3f4d05326a` | 488 | `common/ideas/015_utopia_manifesto_ideas.txt` |
| `e6db306460f20b84cb452faafc300d062a318cbd5b48eb01bb8a24da30658cbb` | 288 | `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` |
| `73a06f68cc6ba23e61c51ba1c9610ff35586fee129623bea5f53478c09cf4037` | 531 | `common/on_actions/015_utopia_manifesto_on_actions.txt` |
| `e58b33608294970dc0f383c88c4660f36119800990bd90c5b08b7ec0c5556f28` | 5,825 | `common/decisions/015_utopia_manifesto_decisions.txt` |
| `32c7993f1ad23f74fcddedc81f119e367b038bc631b6ae48558360a940ece29f` | 5,459 | `events/015_utopia_manifesto.txt` |
| `cb27494bad4e6c0817cd4d80a0164f73086bdcaa9450428a9aefda902f357057` | 353 | `localisation/english/015_utopia_manifesto_focus_l_english.yml` |
| `f838c2a2356e2c46f7500d3ce35835cfd794df9161c7251a35ce3e195a51bdfb` | 137 | `localisation/english/015_utopia_manifesto_ideas_l_english.yml` |
| `1f061f7bf04372777cc422831b4ff93ff808ec769c258b1457d212b02295fc53` | 2,009 | `interface/015_utopia_manifesto.gfx` |
| `c85df258c4aaaf37e905fdc14883cda6b0f8a1f41840df745a3136c830a66d01` | 196 | `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json` |

Accepted references used for coverage comparison:

| SHA-256 | Lines | Reference |
| --- | ---: | --- |
| `27f5a6ce61e7c9cd90315a8f122f67f76715b77729d19d9e4ae659f722799317` | 1,231 | `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_3_focus_tree_architecture.md` |
| `2fdd7a4b9cabf823a38e943f36ac1361e2fcf0a7e7e001434e73ef13dc42032a` | 85 | `docs/specs/015_utopia_manifesto_specs/focus_graphs/focus_tree_architecture.md` |
| `fda4e4d410269d343f9a03aa958cf173b54382939bf47f073eb1110516d6bb2a` | 27 | `docs/specs/015_utopia_manifesto_specs/matrices/focus_route_matrix.md` |
| `3a636423885ea4d8a6f5e1dc680f854b7d288143fa800da9ea0b84698b9bcb83` | 160 | `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_final_improvement_loop_closure_2026-07-18.md` |

## Graph and layout audit

| Check | Result |
| --- | ---: |
| Focus blocks / unique ids | 124 / 124 |
| Prerequisite references | 174 |
| Missing prerequisite targets | 0 |
| Structural roots | 1: `utopia_manifesto_recover_the_manuscript` |
| Structurally reachable focuses | 124/124 |
| Structural terminals | 10 |
| Longest prerequisite chain | 17 focuses, ending at `utopia_manifesto_plenty_in_an_age_of_chaos` |
| Directed mutual-exclusion references | 68 |
| Missing or non-reciprocal exclusions | 0 |
| Coordinates present | 124/124 |
| Duplicate coordinate pairs | 0 |
| Non-downward prerequisite edges | 0 |
| Straight prerequisite segments through unrelated nodes | 0 |
| Conservative straight-segment intersections | 53 |
| Bounds | x = -2..52; y = 0..16 |

The 53 straight-segment intersections are a conservative static proxy, not an engine-rendered connector count. No edge passes through an unrelated focus coordinate, no focus overlaps another coordinate, and no parent is at or below its child. The MCP render limitation is recorded below.

Prerequisite semantics were checked using HOI4's documented structure: references in one `prerequisite` block are OR; separate blocks are AND. The important convergences are correct:

- route alternatives: `utopia_manifesto_union_of_tables`, `utopia_manifesto_technical_missions`, `utopia_manifesto_a_mixed_commonwealth`, `utopia_manifesto_build_the_island`, and `utopia_manifesto_a_settled_interim_charter` use one multi-reference OR block;
- interlocked lanes: `utopia_manifesto_commonwealth_defense_compact`, `utopia_manifesto_the_first_associate`, and `utopia_manifesto_proof_of_the_commonwealth` combine OR alternatives with separate required AND blocks;
- terminal play: `utopia_manifesto_beyond_the_founders_island`, `utopia_manifesto_the_commonwealth_at_war`, and `utopia_manifesto_plenty_in_an_age_of_chaos` require both of their intended parent lanes.

## Route coverage

| Required route or system | Status | Current identifiers and proof |
| --- | --- | --- |
| Opening survey | Complete | `utopia_manifesto_recover_the_manuscript` through `utopia_manifesto_the_country_as_a_question`; store and agriculture are both required before congress/charter convergence. |
| Consent of Households | Complete | `utopia_manifesto_household_gives_consent`, free callings, municipal charters, public lectures, independent review, land trusts, voluntary League, and `utopia_manifesto_commonwealth_by_consent`. |
| Common Table | Complete | `utopia_manifesto_nothing_private_in_necessity`, calling councils, common table, workshops, property transition, recall, communes, autonomy/central-plan fork, and `utopia_manifesto_union_of_tables`. |
| Guardians of Measure | Complete | `utopia_manifesto_country_measured`, standard houses, need tables, board, forecasting, cities, freedom/obedience fork, technical missions, and `utopia_manifesto_perfect_measure`. |
| Closed Island | Complete | `utopia_manifesto_one_island_one_measure`, service households, closed store, penal works, auxiliaries, Natural Right, assigned colonies, channel project, and `utopia_manifesto_perfect_island`. |
| Hidden humanist recovery | Complete | `utopia_manifesto_can_reveal_joke_understood`; reveal-gated `utopia_manifesto_read_island_as_a_mirror`; mixed property, sunset, satire, audit, reform, and `utopia_manifesto_good_place_that_admits_its_limits`; crisis recovery via `utopia_manifesto_admit_the_book_was_a_question`. |
| Callings | Complete | `utopia_manifesto_every_hand_knows_the_soil` through `utopia_manifesto_a_nation_of_many_skills`; calling decision unlocks occur at seven route/shared touchpoints. |
| Common stores | Complete | `utopia_manifesto_the_first_common_store`, capital/regional growth, useful industry, rotation/release, reserve proof, and `utopia_manifesto_surplus_beyond_the_shore`. |
| Settlements and island variants | Complete | homes/transport/city ring; five mutually exclusive site variants; paid `utopia_manifesto_build_the_island`; proof at `utopia_manifesto_the_island_made_real`. |
| Defense | Complete | citizen watch, engineers, professional guard, restraint/victory fork, auxiliary dependency and exit, paid `utopia_manifesto_commonwealth_defense_compact`. |
| League / foreign commonwealth | Complete | store demonstration, surplus offer, cross-border houses, small-place league, reserve council, paid mutual defense, and `utopia_manifesto_the_regional_commonwealth`. |
| Necessary Ground | Complete | survey, domestic alternatives, peaceful offer ladder, trust, limit/right fork, first associate, and `utopia_manifesto_a_commonwealth_of_places`. |
| Stewardship | Complete | obligations, emergency provision, paid route restoration, local charter, charter period, and `utopia_manifesto_status_by_consent`. |
| Constitutional crisis | Complete | `utopia_manifesto_the_founding_crisis`; five mutually exclusive route corrections; convergence at `utopia_manifesto_a_settled_interim_charter`. |
| Formation | Complete | route capstone + settlement/island proof + first associate at `utopia_manifesto_proof_of_the_commonwealth`; paid proof mission; paid proclamation decision; `chaosx.nr15.10`; five route identities; regional proclamation. |
| Post-formation | Complete | paid integration, succession, need law, founder-island policy, paid mature war rules, and `utopia_manifesto_plenty_in_an_age_of_chaos`. |

## Route locks, visibility, and mutual exclusions

The 68 directed exclusions are reciprocal and form seven complete components:

1. five political openers;
2. council autonomy versus emergency central plan;
3. useful freedom versus exact obedience;
4. five island variants;
5. no glory versus necessary victory;
6. limit of need versus natural right;
7. five constitutional corrections.

The hidden humanist route is not a public sixth opener. Its trigger requires unresolved-route or eligible crisis state plus Choice-led Assignment, sufficient Concord, public debate/education/criticism, and no penal, unjust-case, or repeated emergency-levy conduct. The correction focus explicitly unlocks the hidden opener; the opener bypass consumes that correction state. Route setters clear competing route flags and call `utopia_manifesto_refresh_focus_visibility`, whose accepted-actor path invokes `mark_focus_tree_layout_dirty = yes`.

## Paid-focus atomicity and dynamic costs

| Payment family | Foundation | Network | Capstone | Total |
| --- | ---: | ---: | ---: | ---: |
| Institutional | 12 | 10 | 4 | 26 |
| Military | 3 | 2 | 3 | 8 |
| Total | 15 | 12 | 7 | 34 |

All 34 paid focus blocks have:

- the matching tier-specific public affordability trigger;
- `cancel_if_invalid = yes` and no `continue_if_invalid = yes`;
- the matching dynamic tier input, plus a concrete formation input for all eight military focuses;
- a completion-time cost refresh and generic live affordability recheck;
- deductions before institutional proof, template creation, formation deployment, Ledger reward, flags, events, or unlocks;
- exactly one top-level statement after the payment helper: an `if` that rejects the matching payment-failure flag and contains the entire downstream reward tail;
- no `select_effect` payment, so loss of affordability on the last tick fails closed rather than spending at selection and later granting a free tail.

The dynamic cost kernel derives institutional and military costs from central base, per-controlled-state, tier, and capacity constants. The current focus-adjacent source set contains 388 unique `constant:` references and all 388 resolve after the patch.

`on_state_control_changed` refreshes prices for both the accepted new controller and accepted old controller. Both refresh calls are outside the Fallout-only callback guards. No daily, weekly, monthly, or equivalent global repair scan was introduced.

## Reward depth and free-resource audit

The tree does not reduce to generic modifier dust:

- 77 distinct four-value Ledger signatures occur across 124 focuses;
- focus rewards use 36 non-Ledger scripted helper families, 153 route/system flags, three founding events, seven decision-unlock APIs, staged idea transitions, island/district projects, case/League/stewardship proofs, paid institutional growth, and paid military formations;
- the focus file contains no direct political-power, stability, war-support, manpower, experience, equipment, unit, core, annexation, ownership-transfer, or state-transfer reward effect;
- recursive expansion from the 37 direct focus reward helper calls reaches 143 scripted-effect definitions. The only reachable `create_unit` is `utopia_manifesto_deploy_paid_formation`; the only reachable equipment/manpower/army-experience/political-power effects use explicitly negated dynamic cost variables inside the paid executors.

The formation chain changes proof, politics, ideas, flags, and one of five cosmetic identities. It does not annex League members, transfer states, add cores, create unpaid divisions, or grant equipment. The three directly focus-fired events (`chaosx.nr15.4`, `.12`, and `.13`) only select constitutional/store policy flags, idea stages, and Ledger consequences.

No shallow fake branch or repeated generic-reward-only focus was found. No broad improvement plan is warranted under the accepted final improvement-loop closure.

## Staged national-spirit audit

| Check | Result |
| --- | ---: |
| Idea definitions | 50 unique |
| Unique idea pictures | 12 |
| Ideas covered by lifecycle clear helpers | 50/50 |
| Ideas covered by lifecycle add helpers | 50/50 |
| Idea pictures resolving to installed 64x64 DDS | 12/12 |
| Maximum concurrent focus-created lifecycle slots | 3 |

The opening uses manifesto, administrative knowledge, and inherited-property slots. Route commitment clears the manifesto slot and establishes route institution, administration, and property. Common stores replace administration; completed garden districts replace property; auxiliaries temporarily replace the route institution and restore its recorded stage; stewardship temporarily replaces the district/property slot and restores the appropriate family. Focus rewards do not bypass these lifecycle APIs to stack duplicate stages.

## AI behavior gaps

No open AI gap was found.

- 124/124 focuses have explicit `ai_will_do`.
- All file-scoped `@utopia_*` tokens used by the focus tree resolve locally.
- The five openers use distinct preference/avoid triggers; the humanist opener and its crisis correction retain the hidden base weight.
- `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` contains 12 unique packages. All 12 have `allowed`, `enable`, and `abort_when_not_enabled = yes`; all local AI constants resolve.
- Route packages vary war restraint, civilian/arms/infrastructure construction, army build, and volunteer behavior. Separate packages cover valid-case Closed Island escalation, low Plenty, high Need, low Concord, constitutional crisis, and mature commonwealth play.

## Icon coverage

| Surface | Usages / entries | Unique ids | Definition coverage | Texture coverage | Dimensions |
| --- | ---: | ---: | ---: | ---: | ---: |
| Focus icons | 124 | 74 sprites | 74/74 base + 74/74 `_shine` | 74/74 | 74/74 at 94x86 |
| National-spirit pictures | 50 | 12 pictures | 12/12 `GFX_idea_*` | 12/12 | 12/12 at 64x64 |

Base and shine definitions use the same texture for every referenced focus sprite. There are no missing DDS files, texture mismatches, repeated missing-icon fallbacks, or focus icon omissions. The current `final_icon_frame_audit.json` independently reports 124 focus usages and 74 unique focus sprites.

## Localisation and reward mismatch list

| Check | Result |
| --- | ---: |
| Focus names | 124/124 |
| Focus descriptions | 124/124 |
| `available` blocks | 94 |
| `bypass` blocks | 5 |
| Public condition wrappers | 99/99 |
| Unique referenced public tooltip keys | 99 |
| Missing or duplicate relevant keys | 0 |

Manual comparison of the 124 localised names/descriptions against focus reward signatures found no name/reward or description/reward mismatch. The rewards implement the named institution, policy, route, proof, or project rather than unrelated political-power/stability dust. There is no focus-effect hover spam wrapper; the 99 custom wrappers are public availability/bypass explanations.

Mismatch list: **none**.

## Changed files and behavior

| File | Auditor change |
| --- | --- |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | One token at line 713: `constant:utopia_manifesto_case_method.none` -> `constant:utopia_manifesto_case_method.unset`. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/focus_final_audit_2026_07_18.md` | This handoff. |

Changed focus ids: **none**.  
Changed localisation keys: **none**.  
Changed icon ids: **none**.

Route behavior before and after: unchanged. The patch only makes the peaceful-case achievement helper clear its temporary method input to the category's declared sentinel after recording evidence; it does not alter route selection, focus availability, payment, rewards, formation, or AI.

## Meaningful validation and limits

Fresh task-specific checks run against the frozen hashes above:

- balanced focus-block extraction and graph audit for ids, prerequisites, reachability, exclusions, coordinates, depth, and connector proxies;
- all 34 paid caller blocks checked for matching gate/tier/family, cancellation semantics, formation input, payment guard, and a failure-closed reward tail;
- recursive focus-reward helper expansion checked for free units/equipment/cores/annexation/state transfer;
- route/formation hooks traced into scripted triggers/effects, decisions, mission, event `.10`, and identity helpers;
- focus and public-tooltip localisation coverage checked against current English definitions;
- focus/shine and idea sprite definitions resolved to current DDS files and header dimensions;
- script-constant references in focus, trigger, effect, idea, and identity surfaces rechecked after the patch: 388/388 resolve;
- current vanilla Canadian equipment-gated focus precedent and official current effect/trigger/AI documentation consulted alongside the required offline wiki pages.

`hoi4.focus_inspect` and `hoi4.focus_render` were both exposed and called for `utopia_manifesto_tree`. Each returned:

- status: `error`;
- code: `ARTIFACT_STORAGE_LIMIT`;
- blocker message: `Artifact storage retention limit has been reached`;
- artifacts: 0;
- files scanned: 0.

No MCP render or MCP lint result is claimed. Static source evidence is used as explicitly allowed by the audit prompt. Engine-routed connector appearance, live tooltip wrapping, AI choice distribution, mission scheduling, and multiplayer interleaving remain unobserved validation limits, not inferred source defects.

Skipped meaningful validation: an engine-backed focus render and live runtime observation, because the domain tool could not allocate artifacts and this subagent has no game-runtime surface.

## Missing, simplified, fallback, and remaining-risk report

- Missing accepted routes or systems: none.
- Simplified route content: none.
- Shallow/generic branch substitutions: none.
- Missing focus localisation or assets: none.
- Missing focus AI behavior: none.
- Implementation fallbacks: none.
- Validation substitution: static graph/source evidence was used only because both requested MCP calls failed with the exact artifact-storage blocker above; no gameplay fallback was introduced.
- Remaining route risks: only the unobserved engine/render/runtime limits above.
- Broad improvement-plan handoff: none written; the accepted closure remains correct and no broader depth gap was found.
- Gameplay files changed by this auditor: one (`015_utopia_manifesto_identity_effects.txt`), with the exact one-token patch documented above.
- Commit: none; parent retains commit ownership.

## Skills used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`

No skill was created or updated.
