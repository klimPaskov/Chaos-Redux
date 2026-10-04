# Event 027 AI domain probability, round 2, 2026-10-05

Disposition: implemented (decisions D17 and D18 in `agent_decisions_2026-10-04.md`). The evidence covers the AI domain `random_list` in `doctrine_research_ai_choose_scored_domain` (`common/scripted_effects/027_doctrine_research_ai_effects.txt:76`, entries 2 to 6: Army, Navy, Air, Special Forces, Chaos Warfare), fed by `doctrine_research_ai_score_domains`. The scenario IDs and states follow `probability_domain_compare_2026-10-04.md`. Validation limit: the score vectors are traced from source for qualitative states; they are not native country readings.

## MCP route

`hoi4.probability_evaluate` with adapter `random_list`, selector `{ path }`, and the explicit five-entry candidate pool, in workspace `mod_chaos_redux_ea3b2d67c2c0`. `hoi4.probability_compare` was not used for the same reason as on 2026-10-04: the `random_list` source is unchanged, and the change lives in the score effect that feeds its weight variables.

## D17: a landlocked country with a maritime plan

DR-A05L is DR-A05 for a fully landlocked country: no coastal state, a claim on a coastal state it does not control, Army active, Navy empty, no fleet or dockyards, at peace. DR-A05N is the near-landlocked DR-A05 state of 2026-10-04 (one coastal state), which the change does not touch.

| Run | Analysis ID | Scenario hash | Source revision |
| --- | --- | --- | --- |
| D17 | `probability-f52aea923ed27276b9b6a643` | `976c40e06f7170e07a48bcaa5f1288f446a8ec8a7c543e0a86fabc1bac935022` | `78088751377c5de105a72db245ab821353d6c2f426cef7401abb852dccdee468` |

| Scenario | Army / Navy / Air / SF | Score vector |
| --- | --- | --- |
| DR-A04 landlocked minor, no plan | 68.2% / 0% / 27.3% / 4.5% | `15, 0, 6, 1` (unchanged) |
| DR-A05L before | 68.2% / 0% / 27.3% / 4.5% | `15, 0, 6, 1` |
| DR-A05L after | 60.0% / 12.0% / 24.0% / 4.0% | `15, 3, 6, 1` |
| DR-A05N near-landlocked (unchanged) | 53.6% / 14.3% / 21.4% / 10.7% | `15, 4, 6, 3` |

Trace for DR-A05L after: the Navy block is entered through `doctrine_research_ai_has_maritime_plan`; base 1, plus the strategy weight 2 because the country has neither naval readiness nor a naval strategy signal; the forces, production, industry, war, geography, alliance, and readiness terms stay at zero. Navy sits above the landlocked score and below the near-landlocked state, so a plan raises Navy without making it dominate. DR-A04 has no core, claim, or war goal on the coast, so `doctrine_research_ai_has_naval_capability` stays false and Navy keeps weight 0. The analyzer flags Navy as starved in DR-A04 and DR-A05L before (intended) and Chaos Warfare as starved everywhere (no valid action).

## D18: air-centred industry

DR-A03 is the air-centred continental power of 2026-10-04 with deployed planes above 50 per division and dockyards below the naval industry ratio. DR-A03-nofront is the same power in an air war without a land front. DR-A01, DR-A02, and DR-A04 are the 2026-10-04 states: the land major stays below the air industry ratio, the island naval power is dockyard-led (naval industry is checked first), and the landlocked minor deploys no planes.

| Run | Analysis ID | Scenario hash | Source revision |
| --- | --- | --- | --- |
| D18 | `probability-2b89cc5681f283e5b17be463` | `947b5701395a6eb945cce1fcc0584b6cf04e948c69d2bcf4a97a2bed27305a16` | `6c1f73ae386bd5f9481354b0da4a5ed3b74b84e5ee9cb9a907651caf7acaa378` |
| D18, DR-A03-nofront | `probability-8a4d5d993389078782218933` | `c5aa9aa236622d4e9847e2799cfb05a89dfc6d969d8872edb0ff3080b4f02a3e` | `54eaf155f1b5e6410bb7df8c3bdd598fc26b3c33cad03aa6e48a97b9f2fff1fa` |

| Scenario | Army / Navy / Air / SF | Score vector | Expected ordering |
| --- | --- | --- | --- |
| DR-A01 land major (unchanged) | 42.0% / 24.0% / 28.0% / 6.0% | `21, 12, 14, 3` | Army, Air, Navy |
| DR-A02 island naval power (unchanged) | 30.8% / 36.5% / 26.9% / 5.8% | `16, 19, 14, 3` | Navy leads |
| DR-A03 before | 42.0% / 24.0% / 28.0% / 6.0% | `21, 12, 14, 3` | |
| DR-A03 after | 34.6% / 23.1% / 36.5% / 5.8% | `18, 12, 19, 3` | Air leads |
| DR-A03-nofront after | 32.0% / 28.0% / 34.0% / 6.0% | `16, 14, 17, 3` | Air leads |
| DR-A04 landlocked minor (unchanged) | 68.2% / 0% / 27.3% / 4.5% | `15, 0, 6, 1` | Army clear lead |

Trace for DR-A03 after: Army loses the industry focus weight (21 to 18). Air gains the industry focus weight 3 and, because the power is air-led and fights on a land front, the geography weight 2 (14 to 19). Moving the industry focus term alone would leave Army ahead at 18 to 17, short of the round 2 target that Air leads or ties Army; the shared land-front term closes that gap. Without a land front Army also loses its geography term while the warships take the Navy war term, and Air leads 17 to Army 16 and Navy 14. The first DR-A03-nofront run declared Navy at 12 and was replaced by `probability-8a4d5d993389078782218933`.
