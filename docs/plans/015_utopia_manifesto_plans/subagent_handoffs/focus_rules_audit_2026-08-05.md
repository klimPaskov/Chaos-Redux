# Event 015 focus-tree rules audit

Date: 2026-08-05.

Scope: `common/national_focus/015_utopia_manifesto_focus_tree.txt`, `localisation/english/015_utopia_manifesto_focus_l_english.yml`, `interface/015_utopia_manifesto.gfx`, and the route-gate helpers used by the Event 015 tree. This is a read-only audit; no gameplay or asset file was patched.

The audited focus source hash is `3EE07394582645E6DCB149663FFF9A9FC3A269654B3CD5B57A8141AF34A96BA4`.

The audited focus localisation hash is `A74A0897740409305B710FA6E425C220945843789A1F414DD9A7C9F57A9CADBB`.

## High-priority fixes first

No high-priority focus-tree fix is recommended. The current authored layout and route-gate repair are internally consistent, and there is no narrow prerequisite, exclusion, icon, localisation, reward, or focus-local AI defect requiring a patch.

The previous route-gate repair in `focus_tree_route_gate_audit_2026-08-03.md` remains the applicable implementation. It removed redundant visible opener prerequisites from route children, removed the crisis-only prerequisite from `utopia_manifesto_a_mixed_commonwealth`, and anchored `utopia_manifesto_a_settled_interim_charter` on `utopia_manifesto_the_founding_crisis` while retaining its resolved-crisis gate.

## Route coverage

| Required route or branch | Implemented anchors and capstones | Status and source references |
| --- | --- | --- |
| Recovery and survey | `utopia_manifesto_recover_the_manuscript`, `utopia_manifesto_count_houses_and_hands`, `utopia_manifesto_foundation_survey_complete`, `utopia_manifesto_survey_what_we_lack`, `utopia_manifesto_survey_domestic_alternatives` | Covered. Opening and survey anchors are in `common/national_focus/015_utopia_manifesto_focus_tree.txt:50` and `:3192`; hidden survey flags use custom availability tooltips. |
| Consent of Households | `utopia_manifesto_household_gives_consent`, calling and municipal-charter branches, local review, land trusts, `utopia_manifesto_commonwealth_by_consent` | Covered. Opener at `:276`; route child visibility uses `utopia_manifesto_route_consent_of_households`; crisis correction producer is `utopia_manifesto_restore_consent` at `:3601`. |
| Common Table | `utopia_manifesto_nothing_private_in_necessity`, councils, common table, property transition, recall, communes, council fork, `utopia_manifesto_union_of_tables` | Covered. Opener at `:596`; route flag is shared by normal entry and `utopia_manifesto_empower_the_councils` at `:3649`. |
| Guardians of Measure | `utopia_manifesto_country_measured`, standard houses, need tables, forecasting, cities, freedom/obedience fork, `utopia_manifesto_perfect_measure` | Covered. Opener at `:928`; route flag is shared by normal entry and `utopia_manifesto_give_the_surveyors_authority` at `:3697`. |
| Closed Island | `utopia_manifesto_one_island_one_measure`, service households, closed store, penal works, auxiliaries, assigned colonies, channel project, `utopia_manifesto_perfect_island` | Covered. Opener at `:1276`; route flag is shared by normal entry and `utopia_manifesto_seal_the_island` at `:3745`. |
| The Joke Understood | `utopia_manifesto_read_island_as_a_mirror`, institutions that can be left, mixed commonwealth, satire, audit, reform, `utopia_manifesto_good_place_that_admits_its_limits` | Covered. Natural hidden route starts at `:1587`; `utopia_manifesto_a_mixed_commonwealth` no longer depends on crisis-only `utopia_manifesto_admit_the_book_was_a_question` (`:3793`). |
| Callings and education | `utopia_manifesto_every_hand_knows_the_soil` through `utopia_manifesto_a_nation_of_many_skills` | Covered. Shared education and congress flags are explicit in the early gate; first anchor at `:1885`. |
| Common stores | `utopia_manifesto_the_first_common_store`, capital and regional stores, reserve rotation, `utopia_manifesto_surplus_beyond_the_shore` | Covered. First store at `:125`; payment and route gates remain in scripted availability blocks. |
| Garden settlements | `utopia_manifesto_homes_near_work`, transport, social-city ring, district roles, `utopia_manifesto_a_commonwealth_of_places` | Covered. First settlement anchor at `:2291`; foundation-survey and congress gates are explicit. |
| Island project | `utopia_manifesto_choose_the_island`, existing, archipelago, coastal refuge, inland, leased variants, paid build, `utopia_manifesto_the_island_made_real` | Covered. Choice anchor at `:2388`; all five variants are mutually exclusive, including `utopia_manifesto_the_leased_island`, and `build_the_island` retains one OR prerequisite block for the five variants. |
| Defense and foreign commonwealth | citizen watch, engineers, professional army, restraint/victory fork, auxiliary dependency, exit, defense compact, external cases | Covered. `no_glory_in_the_field` and `necessary_victory` are reciprocal exclusions, and `commonwealth_defense_compact` retains its OR parent lane. |
| Necessary Ground and stewardship | `utopia_manifesto_survey_domestic_alternatives`, peaceful offers, ground held in trust, stewardship, emergency provision, route restoration, `utopia_manifesto_a_settled_interim_charter` | Covered. The support anchor is at `:3192`; settled charter at `:3842` uses the shared founding-crisis prerequisite plus resolved-crisis availability. |
| Crisis correction and formation | `utopia_manifesto_the_founding_crisis`, five mutually exclusive corrections, settled charter, formation proof, proclamation, ring integration | Covered. Founding crisis at `:3572`; correction flags, route flags, and `utopia_manifesto_can_form_current_route` remain wired through the Event 015 scripted effects and triggers. |

No Event 015 route family is missing from the 124-focus source. The 18 nodes with no visible prerequisite children are intentional capstones or support terminals: `utopia_manifesto_commonwealth_by_consent`, `utopia_manifesto_union_of_tables`, `utopia_manifesto_perfect_measure`, `utopia_manifesto_auxiliary_contracts`, `utopia_manifesto_perfect_island`, `utopia_manifesto_good_place_that_admits_its_limits`, `utopia_manifesto_a_nation_of_many_skills`, `utopia_manifesto_surplus_beyond_the_shore`, `utopia_manifesto_the_island_made_real`, `utopia_manifesto_end_the_auxiliary_contract`, `utopia_manifesto_commonwealth_defense_compact`, `utopia_manifesto_the_regional_commonwealth`, `utopia_manifesto_survey_domestic_alternatives`, `utopia_manifesto_a_commonwealth_of_places`, `utopia_manifesto_status_by_consent`, `utopia_manifesto_a_settled_interim_charter`, `utopia_manifesto_the_regional_proclamation`, and `utopia_manifesto_plenty_in_an_age_of_chaos`. Each has a capstone, decision, formation, ledger, or support payoff; none is a decorative orphan.

## Prerequisites, exclusions, and route locks

The multi-reference prerequisite blocks are OR gates, while separate `prerequisite` blocks remain AND gates, matching the offline national-focus documentation. The retained OR lanes cover union-table branches, technical missions, all five island variants, the defense compact, and the first-associate branch.

The five political openers keep symmetric mutual exclusions. The common-table and guardians forks, military restraint/victory fork, necessary-ground case fork, and five island variants retain reciprocal exclusions. Route children that have no visible opener connector still require their route flag through `available` or `allow_branch`; the route setter effects call `utopia_manifesto_refresh_focus_visibility` in `common/scripted_effects/015_utopia_manifesto_effects.txt`.

The leased-island branch is intentionally connector-free to preserve the clean authored layout. Its custom availability gate requires the open survey, uncommitted Maritime and Settlement shortage severity, and an eligible lease target, as implemented by `utopia_manifesto_can_select_leased_island_variant` in `common/scripted_triggers/015_utopia_manifesto_triggers.txt`.

## Icon coverage

| Surface | Result |
| --- | --- |
| Focus blocks | 124 focus blocks; every block has an `icon` field. |
| Event 015 icon IDs | 74 unique focus sprite IDs. |
| `interface/015_utopia_manifesto.gfx` | 0 missing Event 015 sprite definitions and 0 missing referenced texture paths. |
| Reuse risk | `GFX_goal_utopia_assemblies`, `GFX_goal_utopia_auditors`, `GFX_goal_utopia_settlement_charter`, and `GFX_goal_utopia_ring_councils` are each reused four times. This is a visual-variety risk, not a wiring blocker. |

## Localisation and reward mismatch list

The focus localisation audit found 124 title/description pairs, 360 Event 015 English keys, zero missing title or description keys, and zero duplicate keys. All 110 Event 015 custom tooltip references found in the focus source are present in the Event 015 English localisation files.

The focus-block audit found zero missing `completion_reward` blocks, zero missing `ai_will_do` blocks, zero missing icon fields, and no title, description, reward, or availability-tooltip mismatch against the route gates.

All focus durations use the declared file-scoped tuning macros: short = 5 cost (35 days), standard = 10 cost (70 days), and long = 15 cost (105 days). No out-of-band focus cost was found.

## AI behavior gaps

No focus-local AI omission was found. All 124 focus blocks have `ai_will_do` blocks, and the five political opener focuses use route-specific preference and avoidance triggers.

`common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` contains 12 route/state strategy plans covering foundation restraint, each political route, Joke Understood, recovery need/plenty states, concord restraint, constitutional crisis, and mature-commonwealth behavior. The strategies abort when their route/state is not enabled and avoid unrelated war, army, volunteer, and construction behaviors.

No probability sweep was run because this audit had no scenario inputs and was limited to structural route safety rather than global balance tuning.

## MCP validation evidence

`hoi4.focus_inspect` was run with workspace `mod_chaos_redux_ea3b2d67c2c0` against `utopia_manifesto_tree` and completed successfully.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d6de65be7b35785951ea80903be350ee66409d05f9fb033fbbaed0f3f534df1/c2148d7174e0dbf0eeb59c959e0f6be0a5d982ad2f1ee72191ad0079c542864c/focus-inspect.c116a01172f19a36.json`.

The inspect revision is `c116a01172f19a36d786b4e3c3d43e02284132a10071a828ee8a5e3ca823392b`, and the layout hash is `702d82bb13bd4d319eb0836bdbb093280b9bb8b53e6f77d40096f68affc8cbb5`.

The tree reports 124 focuses, 126 connectors, zero connector crossings, zero node intersections, zero long connectors, zero duplicate coordinates, zero same-row spacing violations, and zero Event 015 tree diagnostics. Bounds are x = -3..56 and y = 0..16; maximum horizontal span is 8 and maximum vertical span is 2.

`hoi4.focus_render` also completed successfully and produced HTML, SVG, JSON, source-map, and plan artifacts.

Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6d6fc0e405fe98436f810743b9e795a7f891faba6c7e2725c4c17f421adb783/6a4c3610b23c5dbedde6299bcabc7f2db4bd00f29c610941b5ab9cf8db230dfb/utopia_manifesto_tree.focus.html`.

Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd206326692d85d8ba7533d4070a6c6f67cd89e8bdddafd3dd510059d832767e/3acc9cbe0b05ac5574a67ada39613d0c42b5980d028af97fca3449c754d1b431/utopia_manifesto_tree.focus.svg`.

The MCP aggregate validation is false only because its inventory includes 14 unrelated vanilla continuous-focus icon diagnostics and one missing vanilla continuous-focus localisation key under `game:common/continuous_focus/generic.txt`. None references Event 015 source or assets, so no vanilla file was changed.

No `hoi4.focus_rewrite` was used because the authored tree is already clean and broad rewrites are outside this narrow audit. No live Hearts of Iron IV session was launched, per repository instructions.

## Remaining route risks

Route visibility depends on retaining `utopia_manifesto_refresh_focus_visibility` calls in normal route setters, crisis correction/resolution, and island variant commits.

The MCP validator cannot isolate Event 015 from the unrelated vanilla continuous-focus inventory, so aggregate validation remains red despite clean Event 015 diagnostics.

Live engine tooltip wording, save-state route transitions, and cross-system decision/idea balance remain outside this focus-only audit and should be validated in their owning handoffs.

## Changed files and handoff

Gameplay files changed: none.

The only file added by this audit is this handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/focus_rules_audit_2026-08-05.md`.

No simplifications or unapproved fallbacks were introduced. Parent review should preserve the current focus source and use the MCP artifact links above as the latest layout evidence.
