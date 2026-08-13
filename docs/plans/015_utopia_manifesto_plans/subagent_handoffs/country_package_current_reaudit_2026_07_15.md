# Event 15 country-package current re-audit — 2026-07-15

## Verdict

**PASS for the current Event 15 country package after the paid-focus atomicity repair recorded below.**

This is a fresh, source-based audit of the current workspace snapshot. The findings were rebuilt from live gameplay, localisation, interface, and asset files rather than inherited from an earlier dated audit. The result covers the requested country-package surface; it is not by itself a claim that every unrelated Event 15 surface is complete.

No country-package blocker remains in the inspected snapshot. No fallback or simplification was used.

## Audit authorities and scope

The audit used the repository rules plus the `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-subagents`, `chaos-redux-focus-trees`, and `chaos-redux-decisions-missions` skills. Before source review or editing, it consulted the required offline wiki pages, including data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, country creation, portraits, cosmetic tags, and national focuses. It also consulted the corresponding vanilla documentation and vanilla precedents for characters/advisors, cosmetic identities, idea replacement, focus invalidation, annexation, state-control callbacks, and character promotion.

The inspected package surface was:

- recipient selection and rejection
- characters, advisors, traits, and institutional leaders
- four people-free institutional portrait masters
- five route identities and all 75 runtime flags
- route commitment versus paid identity formation timing
- original tag, flag, leader, ideology, and election preservation
- parties, ideas, staged institutions, and succession
- League and association-charter reverse indexes
- `on_annex` and `on_state_control_changed` bridges
- founder/host/state isolation and cleanup
- rejection, disable, annexation, collapse, and terminal cleanup
- paid institutional and military growth
- achievement invariants

## Frozen source snapshot

These hashes were recomputed after the paid-focus repair and before this report was written.

| File | SHA-256 | Lines |
|---|---|---:|
| `events/015_utopia_manifesto.txt` | `a7d27155c463424f19fb1d661356a42ccb90cc4b29f8e42a03ea78ba86b9b164` | 5,071 |
| `common/decisions/015_utopia_manifesto_decisions.txt` | `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd` | 5,708 |
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` | 4,119 |
| `common/characters/015_utopia_manifesto_characters.txt` | `5cdf2ea793216351b5a250bbb1bb0eea84103e7668791b30867216af436749cb` | 399 |
| `common/country_leader/015_utopia_manifesto_traits.txt` | `6cd9a84026b739030115c2a81d2303c5a94bd4a3b4b5178b10947897603230a2` | 108 |
| `common/ideas/015_utopia_manifesto_ideas.txt` | `84f1e322ef827edd4eedff68ba99e67ae61e6c4ed1172193cf77eb3f4d05326a` | 488 |
| `common/countries/cosmetic.txt` | `db7814f7dad4a1b27b95f6afa8d87713ebe7a630bb5b4743bbe76550c38b25e4` | 1,744 |
| `common/script_constants/015_utopia_manifesto_constants.txt` | `a426f72ee144e8bbf940ffb46460777b8b69f6f2fbf8b1989c020a663cf901e1` | 669 |
| `common/script_constants/015_utopia_manifesto_country_constants.txt` | `f53c2eade8230ac93c8af734e41b01b42fe861a3bdb2ec6944d048545af67326` | 143 |
| `common/script_constants/015_utopia_manifesto_decision_constants.txt` | `870516531db2a480be8c2f0626997e7b1a65c6fd4c35e796bb6049b93d84d8c9` | 236 |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | `ed44d3a9892061bb77ebe6e6039be8d7a6a1bcc5f292091c4e5ede32b39d2b8d` | 6,275 |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | `da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75` | 967 |
| `common/scripted_effects/015_utopia_manifesto_country_effects.txt` | `078ccd44ef44d768e1954b3beb914726417fa742a0fe35f8bc5c5938977998aa` | 496 |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | `0eeedf55b22818d4452e18adbe75bb106bf45ffcd33cbf6d3573cab6125bc33a` | 2,601 |
| `common/scripted_effects/015_utopia_manifesto_achievement_effects.txt` | `bab3fc080661918b35d88b0418a4067ca716e458a63e36a86aa37a5da6f886e2` | 254 |
| `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt` | `0e027f7512bdf07dd04123ef97802235cd18db5d6f46e6de909d8376df7cce4d` | 288 |
| `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt` | `1d757540eab0082a09df425578e4208e09cb364832d7b170591ea763d50c60c4` | 536 |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | `d0c304d2b4cd5dccd72b40cff8e9ab4caa3beab58838ce68057eacf31bcfe9af` | 2,882 |
| `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt` | `ba4ac12603651718c633a0b3c90b530097ceadcf16969fadcec69c77508a1c5e` | 86 |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `c2b26e499078d0c7782e46db587d377d8d64cee02e372f2ae8e087c7cea7ea81` | 380 |
| `common/achievements/chaos_redux_achievements.txt` | `c1c729f4717129e8abb60303a79e6fe4318598e6ac0221c79c65faa1ffe4391c` | 3,235 |
| `interface/015_utopia_manifesto.gfx` | `272920625cf3220dd6d67b52bcae0aa5d99d820d6f66bd87593391e9df454749` | 1,845 |
| `localisation/english/015_utopia_manifesto_country_package_l_english.yml` | `42bbc60ef46e9f3c8233c9842a0646b02a72560cd77649195b739fb57416ae92` | 223 |
| `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml` | `01452765d2413b06844a46aaba1c5e0a552fbd2a7ea319b70d59262dbd83c445` | 699 |
| `localisation/english/015_utopia_manifesto_focus_l_english.yml` | `c8d34f7e48facc7eac266d64383af3fa66e93c7a9a48d4d46ba2e96a8e570828` | 353 |
| `localisation/english/015_utopia_manifesto_ideas_l_english.yml` | `0591a362d9ed653e132915c4d4a83e019048e5cc8fde2aa0505eca7d53be702a` | 137 |
| `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/asset_records.json` | `828f18554094f6b214a07dde11f4fa61df290b881d8261cc3b6eeb3677f54ea7` | 4,297 |
| `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/imagegen_source_evidence_2026_07_15.json` | `7f892568ced49d74eb0d7e9cdfe3a796aee4dce13200b3f7a16b3fb2b16b6e18` | 267 |

## Current inventory

| Surface | Current count | Result |
|---|---:|---|
| Recipient candidate classes | 3 | Human generic, AI generic, and approved light-tree countries are separately gated |
| Event 15 character definitions | 24 | 8 institutional leaders plus 16 advisors |
| Institutional founder/successor pairs | 4 | 8 leader definitions using four institutional masters |
| Advisor roles and advisor traits | 16 / 16 | One distinct character and trait per role |
| People-free institutional portrait masters | 4 | Household Assembly, Council of Callings, Board of Measure, Stewardship Council |
| Cosmetic route identities | 5 | Voluntary, Council, Planned, Closed, Practical |
| Runtime route flags | 75 | 25 main, 25 medium, 25 small |
| Cosmetic identity localisation keys | 75 | Five identities × five ideology variants × name/definite/adjective |
| Event 15 ideas | 50 | Includes 12 lifecycle/stage families |
| Focus blocks | 124 | Root structural parser; the tree-level id is not counted as a focus |
| Paid focus callers | 34 | 26 institutional plus 8 military |
| Event 15 achievements | 14 | All use durable proofs and/or disqualifiers where required |
| Route-identity asset records | 100 | 16 advisors, 75 flags, 4 institutional portraits, 5 League emblems |
| Unique built-in ImageGen source masters checked | 43 | 21 unique flag masters, 4 institutional masters, 16 advisor masters, 2 generated advisor overlays |

## Findings

### 1. Recipient selection and rejection — PASS

The entry event remains `chaosx.nr15.1`, is triggered-only and one-shot, and evaluates three bounded recipient classes through absolute gates. Candidate collection is bounded and does not rely on a recurring global-country on action. The AI acceptance and human rejection paths are distinct.

Acceptance records the original country state and initializes the package. Rejection clears Event 15 runtime/ideas without recruiting the Event 15 roster, applying a route identity, or leaving package state behind.

### 2. Characters, advisors, traits, and institutional portraits — PASS

The package defines 24 characters: eight institutional leader definitions arranged as four founder/successor pairs, plus sixteen independently gated advisors. Acceptance recruits the package roster once. Advisor availability follows route/institution state; advisor definitions include costs, AI rules, and add/remove hooks rather than acting as unconditional free modifiers.

The four institutional portrait masters are institutional scenes rather than people. Each master is intentionally reused by its founder/successor pair:

- Household Assembly → Commonwealth Council
- Council of Callings → Rotating Congress
- Board of Measure → College of Measure
- Stewardship Council → Directorate of Service

The practical route does not invent a fifth institutional person; its durable succession proof is constitutional/electoral.

### 3. Identity timing and original-country preservation — PASS

Acceptance saves the original ideology group, exact ruling ideology token, exact typed country-leader value, and election state. The implementation covers the 24 live ideology subtypes rather than restoring only a coarse ideology family.

Route commitment alone does not change the country's displayed identity. The tag/flag/name transition occurs only through the paid proclamation decision and its `chaosx.nr15.10` formation event, which calls the current-route identity effect. Identity is cosmetic: the original base tag and its base flags are not overwritten.

Teardown drops the cosmetic tag, restores the saved ideology/election state, and restores the exact recorded leader when that character is still alive and eligible. Event 15 institutional characters are then retired. Party names are not mutated. The practical identity deliberately preserves the current ruling party and leader.

### 4. Parties, ideas, staged institutions, and succession — PASS

Acceptance begins with the Found Manifesto, Unmeasured Country, and Inherited Order package. Route progress advances staged idea families and ends in route-specific final institutions rather than stacking duplicate stages. The 50 idea definitions cover the inspected lifecycle families, and cleanup removes all package stages.

Institutional succession is idempotent for all four institutional routes. The practical route uses its constitutional-election proof. Re-entering succession evaluation cannot create a second generation twice.

### 5. League and association reverse indexes — PASS

League relationships are stored on the founder and reverse-indexed on the partner. The audit followed all seventeen live relationship arrays through registration, update, removal, collapse, annexation, and teardown. `utopia_manifesto_reconcile_league_reverse_links`, `utopia_manifesto_clear_all_league_reverse_links`, and the annexed-partner bridge avoid a recurring world scan.

Association charters use state targets plus founder and host reverse arrays. State loss, host loss, founder teardown, charter withdrawal, and annexation resolve only links belonging to the affected founder/host/state tuple.

The current snapshot also records association-created military access and guarantees against the exact founder. Cleanup removes only relations created by that association; it preserves pre-existing access/guarantees and relations created by another Event 15 founder.

### 6. On-action bridges and scope isolation — PASS

`on_annex` snapshots affected founders before scopes disappear, then routes founder cleanup through `chaosx.nr15.163` and annexed-actor cleanup through `chaosx.nr15.164`. `on_state_control_changed` snapshots the exact association/district founder relationships and routes the state callback through `chaosx.nr15.165`.

Founder, host, and state cleanup are isolated. A country's disable/rejection/terminal teardown cannot indiscriminately erase another founder's League, association, district, or diplomacy state. The pre-fire district/contact path uses actor-local arrays; the earlier shared/global district-contact pointer pattern is absent. The only remaining Event 15 global event target is the intentional latest-actor pointer used by the event log.

### 7. Disable, rejection, collapse, and terminal cleanup — PASS

The common runtime clearer removes active missions, staged/final ideas, identity state, characters, League state, association/district/state links, targets, variables, and temporary package flags. Disable first tears down the package and then sets the collapse disqualifier. Annex-safe callbacks route through the same narrow cleanup families.

Rejection is idempotent and does not need a fabricated fallback leader, tag, flag, or party. Terminal cleanup restores the recorded original state when it still exists; eligibility checks prevent invalid character promotion.

### 8. Paid growth and focus atomicity — PASS after repair

The fresh audit found that all paid focus callers invoked a payment wrapper and then originally applied their focus flags, ledger deltas, route stages, or proof flags unconditionally. A stale affordability cache during a Fallout world rewrite could therefore make the wrapper fail after a focus had been considered available while the downstream reward still fired.

The repair is intentionally narrow:

1. Every one of the 34 paid-cost focuses now has `cancel_if_invalid = yes`.
2. Every paid completion reward calls its payment wrapper first and places its entire remaining reward tail inside the matching success guard:
   - `NOT = { has_country_flag = utopia_manifesto_institutional_growth_payment_failed }`, or
   - `NOT = { has_country_flag = utopia_manifesto_military_growth_payment_failed }`.
3. `on_state_control_changed` now refreshes ROOT and FROM dynamic costs outside `fallout_world_rewrite_callbacks_are_allowed`. Ledger refresh, island reconciliation, reverse-link work, and history-sensitive callbacks remain guarded.
4. The combined auxiliary military decision path in the current snapshot tests the combined bill atomically and refunds a partial deduction if any later component cannot be paid.

The eight military focus callers are:

```text
utopia_manifesto_households_of_service
utopia_manifesto_perfect_island
utopia_manifesto_the_citizen_watch
utopia_manifesto_engineers_before_generals
utopia_manifesto_a_small_army_well_housed
utopia_manifesto_commonwealth_defense_compact
utopia_manifesto_mutual_defense_without_mastery
utopia_manifesto_the_commonwealth_at_war
```

The twenty-six institutional focus callers are:

```text
utopia_manifesto_the_first_common_store
utopia_manifesto_cooperative_land_trusts
utopia_manifesto_commonwealth_by_consent
utopia_manifesto_social_workshops
utopia_manifesto_union_of_tables
utopia_manifesto_standard_houses
utopia_manifesto_cities_in_series
utopia_manifesto_perfect_measure
utopia_manifesto_the_closed_store
utopia_manifesto_penal_works
utopia_manifesto_cut_the_channel
utopia_manifesto_a_mixed_commonwealth
utopia_manifesto_reform_without_paradise
utopia_manifesto_good_place_that_admits_its_limits
utopia_manifesto_schools_of_calling
utopia_manifesto_a_nation_of_many_skills
utopia_manifesto_the_capital_store
utopia_manifesto_regional_storehouses
utopia_manifesto_useful_industry
utopia_manifesto_rail_road_and_common_ground
utopia_manifesto_a_ring_of_social_cities
utopia_manifesto_build_the_island
utopia_manifesto_common_reserve_council
utopia_manifesto_restore_the_route
utopia_manifesto_integrate_the_ring
utopia_manifesto_plenty_in_an_age_of_chaos
```

Paid military formations remain centralized in the military-growth effect family. There are eight `create_unit` meta-effect variants there and no direct `create_unit` reward in the Event 15 focus, decision, or event files. A failed payment therefore creates no formation and now advances no focus milestone, route capstone, ledger delta, or achievement proof.

### 9. Achievements — PASS

Fourteen Event 15 achievements are registered. Their invariant-sensitive conditions rely on durable proof flags/arrays and explicit disqualifiers for conduct that cannot be reconstructed from the final map alone. The inspected paths cover peaceful cases, assignment limits, reserve survival, League membership/conduct, island origin/path, public-use financing, practical constitutional proof, guarded/closed conduct, foreign-hand restrictions, stores, and anti-chain conduct.

Cleanup preserves durable achievement history where the achievement design requires it and removes live package state where it does not.

### 10. Route identities and visual assets — PASS

The asset manifest contains 100 current records:

- 16 advisor portraits at 65×67
- 25 main flags at 82×52
- 25 medium flags at 41×26
- 25 small flags at 10×7
- 4 institutional portraits at 156×210
- 5 League emblems at 64×64

All 100 recorded source, processed, package, and runtime paths were rehashed. The recomputation found zero missing files, zero source/processed/runtime hash mismatches, and zero package/runtime byte mismatches.

The 25 main flag records contain 21 unique images. Four base aliases are deliberate: Voluntary uses the democratic variant as base, Council uses communism, Planned uses neutrality, and Closed uses fascism. Practical has a distinct base plus four ideology variants. All five identity names have complete name/definite/adjective localisation for the base and four ideology variants.

The independent collection digests of sorted `kind|identifier|runtime_sha256` records are:

| Collection | SHA-256 |
|---|---|
| Advisor portraits | `2b2cde20ed811e83c27ea0043898da9e9bcf3f784a5f1fd7574ff1a0ded90a09` |
| Main flags | `10f416979b059b4374f19426be3971e62a2cf72e7fdf997f06c83223fb53064a` |
| Medium flags | `234e322101464e93a7eb2bbfbe7d1f70d1ab833a3911d68dade57753df090c56` |
| Small flags | `123d572632d7893453506139f480e69d4c2db4c129fe4c7dde96b45ea4e1eaef` |
| Institutional portraits | `ee25ee7f88cd16e0502746d588460d762c4e94dcf445313303f1f2cec4875842` |
| League emblems | `9ca0f1f3c471ca5b01cea56bdc2b94bca75dce9b7eb766109130023bcd0d674b` |
| All 100 records | `32d6b649c4877131940ced0362b31d751d1bc8945d356341e4f1cadd1a4bdf75` |

The four runtime institutional portrait hashes are:

| Institution | Runtime SHA-256 |
|---|---|
| Household Assembly | `db9986d91d1273be16023766e157f5aa30b0e7d269f937152abd59da7f692666` |
| Council of Callings | `e5f58092dbe1adddaecb32c4d35c4084c25fb4cdca14671d53b0583dd5357b63` |
| Board of Measure | `b1904a68cff3bfe51be19b5d215b170e823b24661e8aa95098e843875164f322` |
| Stewardship Council | `25d02601de8a98783cb58fd61ca2af548904bc86a5fcef657d038a59edb11514` |

The generated-source evidence links the 43 unique ImageGen masters to their built-in store objects. The source files used by the package are byte-identical to those objects. No third-party person or copied portrait is used.

## Task-specific validation and corroboration

- The local structural checker found 34 paid callers: 26 institutional and 8 military.
- Each caller has exactly one matching affordability trigger, one explicit `cancel_if_invalid = yes`, one correct payment-failure guard, and no unguarded completion-reward tail.
- Focus-tree and Event 15 on-action brace balances are zero after the repair.
- Root independently parsed all 124 focus blocks and corroborated the same 34/26/8 caller counts, guard identities, explicit cancellations, and zero unguarded tails.
- The corrected state-control bridge contains exactly two Event 15 dynamic-cost refresh calls, for ROOT and FROM, outside the Fallout callback guard.
- Asset validation rehashed all 100 manifest records and reproduced all seven collection digests above.
- The country package has 24 characters, 16 advisor roles, 16 matching traits, 50 ideas, five cosmetic identities, 75 identity localisation keys, 75 runtime flag files, and 14 achievements in the current source.

The HOI4 domain MCP focus inspector/renderer was not available to this subagent session. The repair does not alter focus coordinates, prerequisites, or route topology, and root independently corroborated the paid-focus structural invariants. No interactive engine-run claim is made by this static audit.

## Files changed by this re-audit

- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
  - added explicit cancellation to all 34 paid focuses
  - fail-closed all 34 post-payment reward tails
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
  - moved ROOT/FROM dynamic-cost refresh outside the Fallout callback guard while preserving guarded ledger/island work
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/country_package_current_reaudit_2026_07_15.md`
  - this current-snapshot handoff

The current snapshot also contains the collaborating decision/reverse-link correction tranche in the Event 15 decisions, main effects, main triggers, pre-fire effects/triggers, events, and decision localisation. Those files are included in the frozen hash table above; this subagent did not claim ownership of those edits.

## Remaining limitations and risks

- This is a static source, structure, hash, and asset audit. It does not claim an interactive engine execution trace.
- If affordability changes in the final interval between the engine's focus-validity check and the payment wrapper's refreshed check, the wrapper deliberately fails closed: it takes no payment, creates no unit, and applies no downstream package reward. The focus engine may already have marked the focus complete. The unguarded free-reward path is eliminated; the remaining behavior is the requested fail-closed policy.
- Original leader restoration is intentionally conditional on that exact saved character still being alive and eligible. The package does not fabricate a substitute leader.

These are not missing implementation items and did not require a fallback.

## Simplifications, omissions, and blockers

None. All requested country-package surfaces were inspected against the current source, the paid-focus defect found by the fresh audit was repaired across all 34 callers, and no requested route identity, portrait master, flag size, advisor, cleanup bridge, or achievement invariant was omitted.

No commit was created by this subagent; final integration and commit ownership remain with the parent agent.
