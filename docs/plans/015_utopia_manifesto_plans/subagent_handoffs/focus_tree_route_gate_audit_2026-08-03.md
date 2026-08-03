# Event 015 focus-tree route-gate audit

Date: 2026-08-03.

Scope: `common/national_focus/015_utopia_manifesto_focus_tree.txt` and `localisation/english/015_utopia_manifesto_focus_l_english.yml` after the structural layout repair.

The current source hash observed during the final audit was `3EE07394582645E6DCB149663FFF9A9FC3A269654B3CD5B57A8141AF34A96BA4`.

## High-priority fixes first

The layout repair had replaced several visible route prerequisites with route-flag `available` gates. That is safe only when the route flag is set by both the normal opener and the crisis correction that unlocks the opener.

The following two route edges were additionally corrected in the focus source.

| Focus | Before this audit | After this audit | Reason |
| --- | --- | --- | --- |
| `utopia_manifesto_a_mixed_commonwealth` | A direct prerequisite on `utopia_manifesto_admit_the_book_was_a_question` blocked the ordinary hidden route after `utopia_manifesto_read_island_as_a_mirror`, which sets `utopia_manifesto_route_joke_understood` without completing the crisis correction focus. | No visible prerequisite; `allow_branch` and the custom `available` tooltip require `utopia_manifesto_route_joke_understood` and the existing payment trigger. | Both the natural hidden route and the crisis-correction route can enter the mixed-property branch, while the route flag and payment gate remain authoritative. |
| `utopia_manifesto_a_settled_interim_charter` | A direct prerequisite on `utopia_manifesto_admit_the_book_was_a_question` blocked four literal crisis corrections. | Visible prerequisite is the shared `utopia_manifesto_the_founding_crisis`; `allow_branch` and `available` still require `utopia_manifesto_constitutional_crisis_resolved`. | All five correction focuses require the founding crisis, and every correction resolves the same crisis flag. The shared visual anchor avoids a route-specific dead end without adding five crossing connectors. |

The earlier structural repair also removed redundant opener prerequisites from the first child of each literal route. Those narrow changes are retained because the matching route flags are set by both normal route completion and crisis correction:

| Route child focuses | Authoritative gate | Crisis correction producer |
| --- | --- | --- |
| `utopia_manifesto_municipal_charters` | `utopia_manifesto_route_consent_of_households` | `utopia_manifesto_restore_consent` |
| `utopia_manifesto_councils_of_callings`, `utopia_manifesto_the_common_table` | `utopia_manifesto_route_common_table` | `utopia_manifesto_empower_the_councils` |
| `utopia_manifesto_standard_houses`, `utopia_manifesto_tables_of_need` | `utopia_manifesto_route_guardians_of_measure` | `utopia_manifesto_give_the_surveyors_authority` |
| `utopia_manifesto_households_of_service`, `utopia_manifesto_the_closed_store` | `utopia_manifesto_route_closed_island` | `utopia_manifesto_seal_the_island` |

The route setters `utopia_manifesto_set_consent_of_households_route`, `utopia_manifesto_set_common_table_route`, `utopia_manifesto_set_guardians_of_measure_route`, `utopia_manifesto_set_closed_island_route`, and `utopia_manifesto_set_joke_understood_route` call `utopia_manifesto_refresh_focus_visibility` in `common/scripted_effects/015_utopia_manifesto_effects.txt`. The refresh helper calls `mark_focus_tree_layout_dirty` after acceptance unless the Event 015 kernel is disabled.

## Route coverage

| Required route or branch | Implemented anchors and capstones | Gate status |
| --- | --- | --- |
| Recovery and survey | `utopia_manifesto_count_houses_and_hands`, `utopia_manifesto_foundation_survey_complete`, `utopia_manifesto_survey_what_we_lack`, `utopia_manifesto_survey_domestic_alternatives` | Covered; hidden survey flags are paired with custom tooltips. |
| Consent of Households | `utopia_manifesto_household_gives_consent`, callings, municipal charters, local review, land trusts, and `utopia_manifesto_commonwealth_by_consent` | Covered; route flag is shared by normal and crisis entry. |
| Common Table | `utopia_manifesto_nothing_private_in_necessity`, calling councils, common table, property transition, recall, communes, council fork, and `utopia_manifesto_union_of_tables` | Covered; route flag is shared by normal and crisis entry. |
| Guardians of Measure | `utopia_manifesto_country_measured`, standard houses, need tables, forecasting, cities, freedom/obedience fork, and `utopia_manifesto_perfect_measure` | Covered; route flag is shared by normal and crisis entry. |
| Closed Island | `utopia_manifesto_one_island_one_measure`, service households, closed store, penal works, auxiliaries, assigned colonies, channel project, and `utopia_manifesto_perfect_island` | Covered; route flag is shared by normal and crisis entry. |
| The Joke Understood | `utopia_manifesto_read_island_as_a_mirror`, `utopia_manifesto_institutions_that_can_be_left`, `utopia_manifesto_a_mixed_commonwealth`, satire, audit, reform, and `utopia_manifesto_good_place_that_admits_its_limits` | Covered; natural hidden route no longer depends on crisis-only `admit_the_book_was_a_question`. |
| Callings and education | `utopia_manifesto_every_hand_knows_the_soil` through `utopia_manifesto_a_nation_of_many_skills` | Covered; agricultural training and congress flags are explicit in the early shared gate. |
| Common stores | `utopia_manifesto_the_first_common_store`, capital/regional stores, reserve rotation, and `utopia_manifesto_surplus_beyond_the_shore` | Covered; payment and route flags remain in custom availability blocks. |
| Garden settlements | `utopia_manifesto_homes_near_work`, transport, city ring, and district roles | Covered; foundation survey and congress flags are explicit. |
| Island project | `utopia_manifesto_choose_the_island`, all five mutually exclusive variants including `utopia_manifesto_the_leased_island`, paid build, and `utopia_manifesto_the_island_made_real` | Covered; variant availability uses the surveyed choice flag and variant trigger. |
| Defense and foreign commonwealth | Citizen watch, engineers, professional army, restraint/victory fork, auxiliary dependency, exit, defense compact, and external cases | Covered; the defense compact keeps its OR parent lane and hidden small-army gate. |
| Necessary Ground and stewardship | Domestic alternatives, peaceful offers, ground held in trust, stewardship, emergency provision, route restoration, and settled charter | Covered; settled charter uses the shared founding-crisis anchor plus resolved-crisis gate. |
| Crisis correction and formation | Founding crisis, five mutually exclusive corrections, settled charter, formation proof, proclamation, and ring integration | Covered; correction flags, route flags, and `utopia_manifesto_can_form_current_route` remain in scripted effects/triggers. |

No Event 015 focus route family was missing from the current 124-focus source.

## Missing or simplified content

No focus-local route was found missing or replaced by a fallback in this audit.

The five island variants are present, including the formerly at-risk `utopia_manifesto_the_leased_island` focus and its `GFX_goal_utopia_leased_island` icon.

Cross-system achievement, idea-lifecycle, and live scenario behavior were not changed or claimed complete here because they are outside the focus-tree scope.

## Icon coverage

| Surface | Result |
| --- | --- |
| Focus blocks | 124 focus blocks; every block has an `icon` field. |
| Event 015 icon IDs | 74 unique focus sprite IDs. |
| `interface/015_utopia_manifesto.gfx` | 0 missing Event 015 sprite definitions for the 74 used IDs. |
| Reuse risk | Reuse is intentional but visually repetitive for `GFX_goal_utopia_assemblies`, `GFX_goal_utopia_auditors`, `GFX_goal_utopia_ring_councils`, and `GFX_goal_utopia_settlement_charter`, each used four times. This is a style risk, not a missing-asset blocker. |

The MCP inventory also reports missing vanilla continuous-focus sprites, but those errors are in `game:common/continuous_focus/generic.txt` and are unrelated to Event 015.

## Localisation and reward mismatch list

The localisation audit found 124 focus IDs, 360 English keys, zero missing title/description pairs, zero duplicate keys, and all changed custom availability tooltip keys present.

The focus-block audit found zero missing `completion_reward` blocks, zero missing `ai_will_do` blocks, and zero missing icon fields.

No focus title, description, reward, or availability tooltip contradicted the route gate after the two fixes above.

No localisation or icon IDs were changed by this audit patch.

## AI behavior gaps

All 124 focuses retain `ai_will_do` blocks, and all five political opener focuses use route-specific preference and avoidance triggers.

The current route preference helpers in `common/scripted_triggers/015_utopia_manifesto_triggers.txt` are route-aware and use live country conditions rather than the stale standalone signals recorded by the older audit. In particular, Joke preference checks public debate plus criticism or concrete failed-case signals, Common Table preference accepts state-level worker-council flags, and Closed Island preference checks the recent emergency-levy flag.

No focus-local AI omission was found.

Probability sweeps were not run because this handoff had no scenario inputs and the requested scope was structural route safety rather than global balance tuning.

## Mutual exclusions and prerequisite semantics

The five political openers retain symmetric mutual exclusions, and the Common Table, Guardians, and island variant forks retain their paired or five-way exclusions.

The multi-reference prerequisite blocks that remain in the tree are OR blocks, while separate prerequisite blocks remain AND gates, matching the offline national-focus documentation.

The new settled-charter prerequisite is intentionally a single shared founding-crisis parent. Its hidden resolved-crisis gate prevents completion before any correction route resolves the crisis.

## Validation evidence

`hoi4.focus_inspect` was run against `utopia_manifesto_tree` after the final source state.

The Event 015 tree reports 124 focuses, 126 connectors, zero connector crossings, zero node intersections, zero long connectors, zero duplicate coordinates, zero same-row spacing violations, and zero Event 015 layout/design diagnostics.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ad21cee1cb50fa3247a6373fb08d38930a6740b5fa92842c7e4c3a21c7e9e99/97d7dfaa3fc1fafde070b417645b2fbfd4ff520101fda7d9ea84598f1f9cdfc8/focus-inspect.1651a612e2ea1f01.json`.

`hoi4.focus_render` was run after the final source state and produced HTML, SVG, JSON, source-map, and plan artifacts.

Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6d6fc0e405fe98436f810743b9e795a7f891faba6c7e2725c4c17f421adb783/2cdd52a989254e7b92d68870fcd6c1960ab466662b269bfe5fd943cbc01e7338/utopia_manifesto_tree.focus.html`.

Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd206326692d85d8ba7533d4070a6c6f67cd89e8bdddafd3dd510059d832767e/c9d2b224e28af0ccba8df27a40e21669f348f9be65682b0302a2f471a768c0cd/utopia_manifesto_tree.focus.svg`.

The MCP aggregate validation remains false because it includes 14 unrelated vanilla continuous-focus icon diagnostics and one missing vanilla continuous-focus localisation key. Those diagnostics do not reference the Event 015 source or assets.

No `hoi4.focus_rewrite` was used because the parent layout repair was already applied and this audit required only narrow prerequisite corrections.

No live Hearts of Iron IV session was launched, per repository instructions.

## Changed files and identifiers

Changed gameplay file: `common/national_focus/015_utopia_manifesto_focus_tree.txt`.

Focus IDs touched by this audit patch:

- `utopia_manifesto_municipal_charters`
- `utopia_manifesto_councils_of_callings`
- `utopia_manifesto_the_common_table`
- `utopia_manifesto_standard_houses`
- `utopia_manifesto_tables_of_need`
- `utopia_manifesto_households_of_service`
- `utopia_manifesto_the_closed_store`
- `utopia_manifesto_a_mixed_commonwealth`
- `utopia_manifesto_a_settled_interim_charter`

The first seven route-child focuses lost redundant visible opener prerequisites while retaining route-flag availability. The mixed-commonwealth focus lost the crisis-only Admit prerequisite. The settled-charter focus changed its parent from the crisis-correction OR block to the shared founding-crisis parent and retained the resolved-crisis availability gate.

No localisation file, icon registration, decision, scripted effect, or scripted trigger was changed by this audit.

## Remaining route risks

Route visibility depends on the existing `utopia_manifesto_refresh_focus_visibility` calls being retained in route setters, crisis entry/resolution, and island variant commits.

The MCP validator cannot isolate Event 015 from the unrelated vanilla continuous-focus icon inventory, so aggregate validation remains red even though the Event 015 tree diagnostics are clean.

Further country-package, achievement, idea-lifecycle, and runtime balance audits should remain separate handoffs rather than being folded into this focus-tree patch.
