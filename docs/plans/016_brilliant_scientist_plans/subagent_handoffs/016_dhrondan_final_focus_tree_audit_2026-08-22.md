# D’Rhondan final focus-tree audit handoff — 2026-08-22

## Audit status

The D’Rhondan focus package is structurally accepted against the binding 88-focus contract, with explicit non-blocking layout findings and a pending specialist probability review.

No gameplay, focus, AI, localisation, effect, icon, or decision source file was changed by this audit.

This handoff makes no in-game validation claim. Live consumer validation remains parent/user-owned.

## Scope and references

The audit used `AGENTS.md`, the required Chaos Redux focus-tree, events, decisions/missions, event-assets, improvement-loop, and subagents skills, the offline Paradox wiki focus/localisation/effects/triggers/AI pages, the vanilla focus documentation and `common/national_focus/germany.txt` precedent, the binding addendum, acceptance scenarios, and the improvement-loop closure handoff.

Primary source was `common/national_focus/016_dhrondan_focus_tree.txt` with the D’Rhondan constants, effects, ideas, AI plans, scripted triggers, localisation, GFX registration, decisions, and Alien Infantry API files listed below.

## Mandatory MCP evidence

All focus MCP calls used workspace `mod_chaos_redux_ea3b2d67c2c0`.

| Evidence | Result |
| --- | --- |
| `hoi4.focus_inspect` on `common/national_focus/016_dhrondan_focus_tree.txt`, tree `dhrondan_focus_tree` | 88 nodes, 102 connectors, zero connector crossings, zero node intersections, zero long connectors, bounds x2–40/y0–22, layout hash `6f6605398964d2a7b6fa02d051bab7a888e980f816c3bc48f4f6738b10773556`; all 88 custom DHR icon references resolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d6ae0e57dc5e83a0a43eddd6b8d4765181c11b95a7b98575f4aa57626fd8cb/bca9b51b204b323d1ed133624bf0233bd555ba58536190683509ad2f4ad1c96f/focus-inspect.e96a318054c8867f.json` |
| `hoi4.focus_render` at review scale 1 | Deterministic HTML, SVG, JSON, source map, and authored plan artifacts; render size 6992×2788; same layout hash and diagnostics. HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c4f75c5c4e0b78a697433672f8320aa7f7446ceafdc3acc4f86d437a63d57b5/9fc3d520fab8ac86c4b266bdaa0719b65a45dd98e1366b4d098610f90b409427/dhrondan_focus_tree.focus.html`; SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3311d16279d92d222a8c2e2fc3e4da643495a499ca87613a6dc1a305d26bf22e/bf5d45e086de4e71a691934c64d5703c3e7726f0b9d0b8fae2c8cfaa26d1ad39/dhrondan_focus_tree.focus.svg`; JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22a37cc3c0eefa5d157a6bcedbfa2884f7de38c1bf76bd380c2cc9fa3e03d8e4/b40470e6aac9fa245e0617e971b07d2714712c3597f45434061c25ff0db01da1/dhrondan_focus_tree.focus.json` |
| `hoi4.focus_raster` at review scale 1 | Decoded-icon PNG 3888×3032, plus raster HTML/SVG/JSON; custom DHR icon family resolved. PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f9b99a1283fa77aa4579e9d5fe72ad1d5e0ff54532768fe109051be01cb66f6/716c5aa10e214b1d0e6ebd74918af0e4e33f13257ecfc5732aa8f375b51a34f0/dhrondan_focus_tree.focus.png` |
| Focus comparison evidence | No dedicated `hoi4.focus_compare` endpoint is exposed in this runtime. The current deterministic layout hash and graph metrics match the accepted 2026-08-21 focus handoffs, and no source rewrite occurred, so there is no before/after patch comparison to report. |
| `hoi4.probability_inspect` through the national-focus AI adapter | Complete candidate pool discovered: 88 DHR focus candidates, five required scenario inputs, zero unresolved source candidates after the full pool was declared. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e00f3dc37f3cb35d2cdfce09cc43b532ec89dd3857f920273446ac93b906e68b/d34636c869546073b0c719ed326b995970bad819617212f04c3da57d9442ba7e/probability-inspect-2450691318dd.json` |
| `hoi4.probability_evaluate` full 88-candidate pool | One peaceful opening scenario returned `PROBABILITY_ANALYZED_PARTIAL`, 88 candidates, 126 unresolved scenario outcomes, and 34 diagnostics. The ranking/unresolved artifacts are evidence only; route-specific prerequisite and external-factor scenarios were not supplied. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40e836b8581e68f4885ecd72ecaad77e92f4cd7c14395d204f1fc235a7a8e31f/3304ae806916cf7120fd24d69d2ed44381c6d901c007ab3d5eeaa0f97e647826/probability-cfa994ea79073d54b61ed3b8.json`; ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18a2c05defa1dd433f8143901e48cc3663ba19c4ccca0f40e77d8c8b1e6793ec/81249c55fd6e6876d97ea32fa6d4be0fdd0b09804cdf07cc2a4330b8adf29bae/probability-probability-cfa994ea79073d54b61ed3b8-ranking.png` |

`MCP_INLINE_FILES_TRUNCATED` is informational. The twelve `FOCUS_ICON_REFERENCE_MISSING` diagnostics point to imported vanilla continuous-focus entries in `game:common/continuous_focus/generic.txt`, not DHR nodes, and are out of scope.

## Route coverage

The source contains exactly 88 unique DHR focus IDs with the required category allocation.

| Route/category | Count | Source span and anchors | Audit result |
| --- | ---: | --- | --- |
| Survival and paid landing network | 8 | `016_dhrondan_focus_tree.txt:56-178`, `DHR_beneath_an_alien_sky` → `DHR_convene_the_two_world_throne` | Complete opening trunk; paid landing network and no-free-cohort tooltips are wired. |
| Vael IX Imperial Continuity | 8 | `:184-291`, `DHR_vael_ix_takes_the_throne` → `DHR_the_unbroken_imperial_line` | Complete eight-focus regime route with imperial gate and staged mandate rewards. |
| Sera Qel Technocratic Synod | 8 | `:297-402`, `DHR_sera_qel_presents_the_calculus` → `DHR_the_government_of_certainties` | Complete eight-focus regime route with synod gate and staged calculus rewards. |
| Ilyr Ren Two-World Covenant | 8 | `:410-515`, `DHR_ilyr_ren_opens_the_chamber` → `DHR_the_chamber_of_two_skies` | Complete eight-focus regime route with covenant gate and staged chamber rewards. |
| Laboratory economy | 10 | `:523-643`, `DHR_relight_the_field_laboratories` → `DHR_a_two_world_research_complex` | Complete ten-focus industrial/research lane. |
| Alien army and predictive warfare | 12 | `:649-797`, `DHR_restore_the_predictive_staff` → `DHR_perfect_predictive_warfare` | Complete twelve-focus predictive lane; no ordinary alien recruitment hook. |
| Orbital, air, and naval support | 8 | `:804-903`, `DHR_reassemble_the_orbital_office` → `DHR_make_near_space_ours` | Complete eight-focus corridor lane with 18/12-day recovery hooks. |
| Diplomacy and intelligence | 8 | `:909-1004`, `DHR_open_the_translation_bureaus` → `DHR_the_embassy_beyond_the_stars` | Complete eight-focus access and intelligence lane. |
| Expansion and world order | 12 | `:1010-1161`, `DHR_define_the_two_worlds_question` → `DHR_a_place_in_the_world_order` | Complete twelve-focus expansion lane; shared entry uses the selected regime capstone. |
| Crisis and late game | 6 | `:1167-1253`, `DHR_the_enclaves_refuse_the_ledger` → `DHR_the_century_beyond_exile` | Complete six-focus crisis/closure lane with exclusive resolution pair. |

The three regime starts are mutually exclusive at `:191`, `:304`, and `:417`. Route-specific descendants use `dhrondan_focus_is_imperial`, `dhrondan_focus_is_synod`, and `dhrondan_focus_is_covenant` in `common/scripted_triggers/016_dhrondan_focus_triggers.txt:23-36` and in the focus `available` blocks.

`DHR_define_the_two_worlds_question` at `:1018` uses one prerequisite block containing the three mutually exclusive regime capstones, which is correct OR semantics for the selected route. `DHR_begin_postwar_integration` at `:1139` similarly accepts the selected route’s expansion capstone. The crisis resolution at `:1214` accepts one of the two mutually exclusive crisis choices.

The tree has ten search-filtered navigation shortcuts in the header at `:26-50`, and every focus carries a `search_filters` block.

## Layout, ownership, and visual findings

The authored graph is symmetric and lane-owned at normal review scale: the laboratory lane occupies the left band, army/predictive work the adjacent band, politics the central band, orbital support the right band, and diplomacy/expansion the outer bands. The raster and structural render show readable branch separation with no crossings, node intersections, or long connectors.

The two DHR-local linear-detour warnings are:

1. `DHR_count_the_landing_states → DHR_inventory_the_expedition_stores` at `:74-116`, with horizontal span four and vertical span one.
2. `DHR_secure_the_scattered_enclaves → DHR_restore_the_landing_beacons` at `:89-131`, with horizontal span four and vertical span one.

These are intentional opening fan-out connectors. Collapsing the first pair would move the survival-to-laboratory/army handoff into another lane; collapsing the second would move the orbital/diplomacy anchors and weaken the right-side symmetry. The inspect result exposes no movable IDs for a bounded spacing-only correction. `hoi4.focus_rewrite` would require an authored whole-plan rewrite or compact whole-tree layout, so invoking it would be an unsafe bulk layout change outside this audit scope.

The five same-row spacing warnings are the fixed cross-lane pairs `DHR_encode_the_enemy_reaction`/`DHR_restore_the_ninth_diadem` at y6, `DHR_rebuild_the_expeditionary_cadres`/`DHR_codify_imperial_service` at y7, `DHR_convert_terrestrial_workshops`/`DHR_map_the_probability_front` at y6, `DHR_the_twenty_element_substitution`/`DHR_train_human_signal_teams` at y7, and `DHR_the_exoplanetary_materials_board`/`DHR_supply_before_the_order` at y9. Their one-column separation is the authored boundary between adjacent lanes, and moving either endpoint would shift a branch or create a longer connector. These warnings are accepted as non-blocking polish with an exact geometry blocker, not silently left as unexplained queue items.

## Icon coverage

All 88 focus IDs have a unique DDS under `gfx/interface/goals/016_dhrondan_focus/`, all 88 base names and all 88 `_shine` names are registered in `interface/016_dhrondan_focus_icons.gfx`, and the MCP focus inspector resolves every custom DHR focus icon.

| Family | Focus DDS files | Base refs | Shine refs | Result |
| --- | ---: | ---: | ---: | --- |
| Survival | 8 | 8 | 8 | Complete |
| Imperial | 8 | 8 | 8 | Complete |
| Synod | 8 | 8 | 8 | Complete |
| Covenant | 8 | 8 | 8 | Complete |
| Laboratory | 10 | 10 | 10 | Complete |
| Army/predictive | 12 | 12 | 12 | Complete |
| Orbital | 8 | 8 | 8 | Complete |
| Diplomacy/intelligence | 8 | 8 | 8 | Complete |
| Expansion/world order | 12 | 12 | 12 | Complete |
| Crisis/late game | 6 | 6 | 6 | Complete |
| **Total** | **88** | **88** | **88** | **No DHR icon gap** |

The 11 lifecycle idea icons are separate under `gfx/interface/ideas/016_dhrondan_focus/` and are not substituted for focus art.

## Localisation and reward audit

The title and description key audit found 88/88 title keys and 88/88 description keys in `localisation/english/016_dhrondan_focus_l_english.yml`.

No focus name or description/reward mismatch was found. In particular, `DHR_feed_the_landing_reserve` at `:597-604` and localisation `:97-98` says that future cohorts are paid and that the focus itself grants no soldiers; `DHR_rebuild_the_expeditionary_cadres` at `:698-716` and localisation `:113-114` distinguishes human cadres from alien cohorts outside normal recruitment; and `DHR_reopen_the_homeworld_corridor` at `:1227-1244` and localisation `:193-194` retains the per-cohort laser cost.

The paid-cost and recovery descriptions match `common/script_constants/016_alien_infantry_api_constants.txt:21-42` and `common/scripted_effects/016_alien_infantry_api_effects.txt:220-238` and `:261-415`. The network, guarded-descent, and near-space descriptions match the 24/18/12 ordinary recovery ladder while leaving the seven-day reservation and exact 2,000-laser cost unchanged.

Rewards are route-specific and varied across PP, CP, XP, research bonuses, production/building hooks, flags, claims/world-order hooks, lifecycle idea upgrades, crisis hooks, and the predictive-technology upgrade at `:785-797`. No generic reward-only filler branch was identified.

## Idea lifecycles and landing contract

`common/scripted_effects/016_dhrondan_focus_effects.txt:13-118` clears and replaces one political, one predictive, and one off-world lifecycle slot. This enforces at most three simultaneous focus-created spirit families while allowing staged upgrades.

`dhrondan_focus_enable_landing_network` at `016_dhrondan_focus_effects.txt:121-128` sets the landing-network flag, sets `dhrondan_alien_infantry_training_forbidden`, and assigns the shared 2,000-equipment constant. The Alien Infantry API keeps one pending reservation, debits exactly 2,000 weapons, and applies ordinary cooldowns of 30/24/18/12 days at `016_alien_infantry_api_effects.txt:220-238` and `:378-415`.

No focus or decision calls ordinary alien training or grants a free alien cohort. The only training-related focus flag is the intentional prohibition flag.

## AI behavior

All 88 focus blocks contain `ai_will_do` and `search_filters`. Inline weights at `016_dhrondan_focus_tree.txt:16-23` use standard/preferred/urgent tiers, route modifiers, and route-aware modifiers for war, stability, and war support. The four strategy plans at `common/ai_strategy_plans/016_dhrondan_focus_ai.txt:14-173` are DHR-only, enable and abort on the selected regime, and provide distinct Imperial, Synod, and Covenant focus lists and factors.

The probability inspect discovered a complete 88-focus candidate pool. The full-pool evaluation was intentionally limited to one peaceful opening scenario, so route descendants emitted expected `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` warnings and the adapter returned 126 unresolved scenario outcomes. Ordered AI strategy plans and the adapter’s prerequisite/external-factor boundary are documented limitations, not source-level AI omissions.

The required `chaosx_ai_probability_auditor` specialist route was not callable from this isolated subagent runtime. The direct MCP probability artifacts above are therefore evidence of source discovery and a bounded opening analysis only, not a final balance claim. Parent review must attach the specialist’s named Imperial, Synod, Covenant, crisis, and peaceful-war scenario analysis before claiming weighted-AI acceptance. No AI weight patch was made, so no probability comparison pass is required for this audit’s source state.

## Missing, simplified, and unresolved content

No DHR focus route, count, icon, localisation key, route lock, mutual exclusion, lifecycle hook, decision hook, claim/core/world-order hook, or AI source block required by the binding addendum was found missing.

The accepted design intentionally has no ordinary alien training branch and no focus-created unit/equipment spawn; the paid landing API remains the only cohort path.

The existing package retains the documented specification tension between the maximum-15 initial force and the “every disconnected enclave receives a cohort” wording when more than fifteen disconnected components exist. This is recorded in the closure handoff and remains a parent-owned specification clarification; this focus audit does not invent a sixteenth cohort or weaken the cap.

## High-priority follow-up

1. Parent must obtain and attach `chaosx_ai_probability_auditor` evidence for route-aware focus selection and strategy-plan interactions. The current direct full-pool evaluation is partial by design.
2. Parent must reconcile the max-15 versus every-enclave edge case in the binding spec and acceptance scenarios without changing the accepted cap.
3. Parent/user must perform live in-game route, tooltip, reward, landing-cost, cooldown, and normal-zoom visual acceptance. This audit does not claim that proof.
4. No `hoi4.focus_rewrite` is recommended for the two fan-out detours or five one-column cross-lane pairs because the exact safe fix would be a broader authored layout rewrite and the current tree has zero crossings, overlaps, and long connectors.

## Changes and acceptance status

Changed files: none.

Changed focus IDs: none.

Route behavior before/after: unchanged; all three regime locks, shared lanes, expansion gates, crisis exclusivity, and lifecycle effects remain as authored.

Localisation keys changed: none.

Icon IDs changed: none.

Improvement plan written: none; the accepted improvement-loop closure handoff already covers the remaining parent-owned risks.

Acceptance status: the DHR focus package passes the structural 88-node, route-count, icon, localisation, reward/lifecycle, prerequisite, mutual-exclusion, and source-wiring audit. It is conditionally ready for parent review, pending specialist probability evidence and user-owned in-game validation. The two DHR layout detours and five fixed same-row spacing warnings are accepted, explained, and bounded rather than treated as hidden failures; the twelve vanilla continuous-focus missing-icon diagnostics are rejected as out of scope.
