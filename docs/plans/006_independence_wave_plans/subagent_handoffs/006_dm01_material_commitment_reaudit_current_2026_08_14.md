# Event 006 DM-01 material-commitment re-audit — 2026-08-14

## Current disposition

DM-01, `independence_wave_secure_provisional_capital`, is source-complete for the accepted material-commitment contract. It remains a country-scoped automatic mission, not a player-clicked selectable decision, and its activation is fail-closed behind the paid scripted start effect.

This receipt supersedes the pre-implementation garrison-only findings in `006_dm01_spec_alignment_audit_2026_08_12.md` and refreshes the older material-commitment receipt after the IW-045 source tranche. It does not claim whole-Event-006 completion: current authority is 32 content-attested packages, 29 compatible reservation groups, 161 unattested selectable rows, and 40 runtime adapters. IW-045 is included in that current authority; the remaining whole-event gaps are documented separately.

## Source contract checked

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt` contains force-tier-aware garrison, infantry-equipment, support-equipment, and isolated-capital transport affordability helpers.
- `common/scripted_effects/006_independence_wave_decision_effects.txt` pays the selected material tier once at mission start, consumes either the train or motorized alternative when the capital has no supply node, and starts the automatic mission only after the complete gate passes.
- `common/script_constants/006_independence_wave_decision_constants.txt` centralizes the light, standard, and major material quantities, the 75-day ceiling, and the fragile/viable duration adjustments. The resulting founding windows are 30, 45, or 75 days.
- `common/decisions/006_independence_wave_decisions.txt` cancels on origin invalidation, capital loss, or garrison loss; timeout records the secured administration outcome; cancellation applies the bounded failure outcome and fires the emergency relocation event.
- `events/006_independence_wave.txt` contains the bounded relocation response and its owned-state/dispersed-office fallback.
- `localisation/english/006_independence_wave_decisions_l_english.yml` describes the force-tier garrison, material commitment, isolated-capital transport alternative, duration band, and failure consequence.

The payment is sunk at activation and is not refunded on cancellation. Cleanup removes the mission and clears its reservation, success, failure, administration, and relocation state exactly once. This matches the accepted “material commitment” interpretation and avoids a retry refund loop.

## Mandatory probability evidence

`hoi4.probability_inspect` ran against the current decision source with the `mission_ai_will_do` adapter. It returned `PROBABILITY_SOURCE_INSPECTED`, source revision `4060832c53e9900f635edd17f688ee890c6342b9016de2d5c1b2519aede6f052`, source hash `efc4d478e6f23c5c4b07f6b079d8296b138a0a17d774f5b7c2bc53c53e904035`, 54 discovered candidates, 42 required inputs, and zero inspect-unresolved inputs. The pool is incomplete with zero available candidates because the adapter cannot construct a runnable mission from the empty source fixture. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7d549b107ce13cfcd100d4abcea363bb2aa671b082675a8b12149fc503c7fd6/a97311c3ca2838002d0071f1931d95395d397ea49e0cb343a22706908595d4d9/probability-inspect-efc4d478e6f2.json`.

The six named scenarios `E6_DM01_CURRENT_2026_08_14` were evaluated with empty typed state fixtures. The run produced 324 candidate/scenario rows, 543 unresolved values, and 20 diagnostics; DM-01 was never eligible in all six fixtures, which is expected because the mission is `always = no` and requires a live country, capital, force tier, equipment, and transport state. The current/current comparison returned zero comparison changes with the same unresolved boundary. No normalized probability, timing, dominance, starvation, or live-AI balance claim is made.

Evaluate JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1a8df332e15f7dc069cbf0bb0678f827cb5d969815df05671cfd0bab86964c8/5ba4617552ba8a1943dd56271f5e6297374007c6e0d9b6a6e999b8cfabb4a83c/probability-3fbf1a03f93218d72350d8de.json`.

Compare JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18351ffab48344963ae4d76203433158b826a109000145b56aee98f67b72b6e1/f3a17ab82d1c3808d9cb5d3476d87293b5593e409e781f081b675a1d220c958b/probability-43a574760d1b65c97b13eccc.json`.

## Remaining limits

The source and localisation now agree on the material-commitment design, but the probability adapter still needs non-empty typed country fixtures before a meaningful balance result can be claimed. The central Event 006 package authority and Join gate are unchanged by this DM-01 re-audit. These limits are separate from DM-01 and are not silently widened here.
