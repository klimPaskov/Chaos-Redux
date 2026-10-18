# Event 38 Malta Crusaders, AI weights and probability audit, 18 Oct 2026

Disposition: unresolved findings for parent review. Read-only audit of commits `c0dde1edd3` and `ba942d9ebf`. Nothing here was observed in game. Every number is either an MCP result (marked MCP) or a hand calculation from the script (marked hand).

## Surfaces audited

| Surface | File | Count |
| --- | --- | --- |
| Main focus tree `malta_crusaders_focus_tree` | `common/national_focus/038_malta_crusaders_focus.txt` | 108 focuses, all with `ai_will_do` |
| Principality focus tree `malta_principality_focus_tree` | `common/national_focus/038_malta_crusaders_principality_focus.txt` | 39 focuses, all with `ai_will_do` |
| Council, campaign, banner, Eleventh Crusade decisions | `common/decisions/038_malta_crusaders_decisions.txt` | 28 decisions with a score or an explicit 0, 7 missions without AI |
| Principality decisions | `common/decisions/038_malta_crusaders_principality_decisions.txt` | 7 charters, 11 management rows, 1 federation row |
| MTTH-backed scores and intervals | `common/mtth/038_malta_crusaders_mtth.txt` | 27 `malta_ai_*` entries, 2 interval entries |
| Event options | `events/038_malta_crusaders.txt` | events .2, .3, .4, .6, .8, .9, .20, .21, .30 carry real weights |
| AI strategy files for MLT, CRU_*, MQ* | `common/ai_strategy/`, `common/ai_strategy_plans/` | none exist |

Constants read: `common/script_constants/038_malta_crusaders_constants.txt` (`malta_ai`, `malta_standing`, `malta_cohesion`, `malta_demand`, `malta_eleventh`) and `038_malta_crusaders_principality_constants.txt` (`malta_pr_ai`, `malta_pr_loyalty`, `malta_pr_succession`).

Engine semantics used (wiki `AI modding`, MTTH blocks): an MTTH or `ai_will_do` block starts at 1 and applies `base`, `add` and `factor` in written order. Focus, decision and technology `ai_will_do` are score races (a roll between 0 and the score, highest wins), not probabilities. Event `ai_chance` is probability-proportional sampling with a d100 roll. The `factor = 0` opener followed by `modifier = { add = ... }` used throughout Event 38 is correct because the writes are ordered.

## MCP evidence and limits

| Call | Result | Use |
| --- | --- | --- |
| `hoi4.probability_inspect`, `decision_ai_will_do`, `038_malta_crusaders_decisions.txt`, scenario `early_order` | `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-e62ac2c66b1942473b96fdcc`, scenario hash `aa214adca62802d8efb22fe754463137215c429509f6f8ea09e940c8603441ff`, source revision `e18c9e13808e4b719e624a6c07c527fb8a032f02fbf70ab8558b6d1f7028913a`. Every row that uses `mtth:` came back weight 0 with `malta_ai_weight` listed as a missing input. | Not usable for MTTH-backed decisions. Counted as the initial call of the unsupported capability. |
| `hoi4.probability_inspect`, `event_mean_time_to_happen`, `038_malta_crusaders_mtth.txt`, `evaluate: false` | `no_weighted_surfaces`, inventory `probability-inspect-78ce6ce5a2d6`. | The `common/mtth` entries are not discoverable on their own. This was the one corrected retry; the unsupported `mtth:` expansion is not retried again. |
| `hoi4.probability_inspect`, `national_focus_ai_will_do`, settlement trio, scenarios `strained_functional`, `working_functional_civilian`, `united` | `probability-ecf292f7312108347dc099be`, scenario hash `9f63465bf40e9f7ecba6b1c1c2141f04ee7c98b83cbd5e8742bfdfa26c8cafc6`, source revision `1fa12f9bb0a79e97f9ee3098340e764086f655e5d34938cd4ce6e63f6038eacc`. Pool complete for the three-way choice. Weights match the hand calculation exactly. | Score-only evidence. |
| `hoi4.probability_analyze`, `sweep` over `variable.malta_cohesion` | `probability-c345110d831f62d4623e374c`, but `sweepPoints = 1`, so no rank reversal was produced. | Not used. Thresholds were taken analytically from the constants (50 and 75). |
| `hoi4.probability_inspect`, `event_option_ai_chance`, events .2, .20, .30, scenarios `strained`, `working` | `probability-007de39448d72a736c45af0f`, scenario hash `18228098ecbd064e183636fad82f0426b5c58632ec48831c4682b55f04c40fa4`. Weights match hand numbers; probabilities withheld because the three events were pooled together. | Weights only. |

Everything else (mtth scores, decision target factors, principality rows, Eleventh Crusade sequence, demand and succession timing, event .8 probabilities) is hand calculation from the script. None of it is an MCP result. No `render` was produced because there was no multi-scenario sweep or timing result worth drawing.

## Findings

Severity: High = an intended route or an acceptance scenario fails in a plausible campaign. Medium = distorted or starved behavior. Low = tuning hygiene or harmless.

### H1. Eleventh Crusade can be relaunched without a rebuild (High, exact flag trace)

- `malta_eleventh_force_ready` and `malta_eleventh_force_weak` are set at `common/decisions/038_malta_crusaders_decisions.txt:1220`, `:1227`, `:1228` and are never cleared anywhere under `common/` (searched for every `clr_country_flag` of both names). `malta_hold_foothold_failure` (`common/scripted_effects/038_malta_crusaders_action_effects.txt:700`) clears `launched`, `landing_chosen`, `transports_rebuilt` and `volunteers_called`, but not the two force flags. `malta_close_eleventh_crusade` (`core_effects.txt:606`) does not either.
- The launch decision is available on `has_country_flag = malta_eleventh_force_ready` alone (`decisions.txt:1105`), and `malta_ai_launch_eleventh` (`mtth:353-368`) does not read `malta_transports_rebuilt`. After a failed landing the chain select landing (60) then launch (70) is open at once, while rebuild (75) and volunteers (70) are optional. Spec scenario AI-011 ("no suicidal immediate reinvasion") is not met. Only the escalating costs and the failure cap of 3 limit it.
- The sticky `weak` flag has a second effect: after one rebuild timeout the launch score is 25 instead of 70 for failures 0 and 1 and 0 from failure 2, for the rest of the game, even after a proper rebuild.
- Fix: clear both flags in `malta_hold_foothold_failure` and in `malta_close_eleventh_crusade`; add `has_country_flag = malta_transports_rebuilt` to the launch availability at `decisions.txt:1105` and to both modifiers in `malta_ai_launch_eleventh`.

### H2. The AI can never reach Rome, North Africa or a British or Italian bridge state (High, reachability)

- `malta_launch_regional_crusade` multiplies by 0 when `FROM = { is_major = yes }` (`decisions.txt:446-449`). The ultimatum row is `ai_will_do = { factor = 0 }` (`decisions.txt:404`). The registry owners are: Rome (state 2), Dodecanese (164), Tripolitania (661) and Cyrenaica (663) are Italian; Cyprus (183) is British. All are majors, so no AI path owns them.
- `mcf_return_the_keys_to_rome` requires `owns_state = 2 controls_state = 2` (`focus.txt:2297`, availability). Without Rome the AI cannot complete `mcf_return_the_keys_to_rome`, `mcf_the_lateran_and_the_roman_administration`, `mcf_jerusalem_the_sacred_centre`, `mcf_papal_supremacy_over_the_council` and `mcf_the_crown_beneath_the_tiara`, nor set `malta_papal_supremacy`, which `mpf_appeal_to_rome` and `malta_pr_arbitrate_papal` need. Spec scenario AI-009 ("Holy See route competitive") cannot occur for an AI Malta while Italy is a major.
- `malta_select_new_landing` is inconsistent: it uses `factor = 0.25` for majors, not 0 (`decisions.txt:1084`).
- Fix: replace the hard 0 by a constant factor (the landing row's 0.25 is a precedent) gated on strength, for example `num_divisions` of the actor and no current war with a major; or give Rome its own target rule once `malta_western_question` is set.

### M1. The settlement and principality-policy trios are not fully exclusive (Medium, structural, MCP for the scores)

- `mcf_codify_emergency_command` excludes only the Langues (`focus.txt:1439`), `mcf_restore_civilian_courts` excludes only the Langues (`:1708`), the Langues exclude both (`:1565`). Codify and civil courts are not exclusive and neither chain carries a route guard.
- Capstones: `mcf_permanent_grand_magistry` (`:1532`, requires only `malta_dominant_named`, Functional standing, quiet council) and `mcf_constitutional_crusader_kingdom` (`:1829`, requires only Recognized Legitimacy and quiet council) can both complete, each at base 60. `malta_set_government_form` then replaces the Grand Magistry by the Kingdom, which `mcf_return_the_keys_to_rome` also treats as a blocker (`NOT malta_gov_kingdom`).
- MCP scores (settlement trio, standing 3): cohesion 42: codify 45, civil 15, Langues 3.75. Cohesion 55 with `malta_posture_civilian`: Langues 45, civil 30, codify 15. Cohesion 80: Langues 45, civil 15, codify 3.75. At cohesion below 50 the AI takes codify first and then, because the AI eventually takes every available focus, the civil chain as well.
- The same hole exists for `mcf_a_network_of_commanderies` (`:2050`, excludes the league only) and `mcf_restore_the_local_thrones` (`:2097`, excludes the league only); outside Evolution II the league is hidden, so commanderies (20, doubled to 40) and thrones (10) are both taken.
- Fix: add `mutually_exclusive = { focus = mcf_restore_civilian_courts }` to codify, the reverse to civil courts, and add each of `mcf_a_network_of_commanderies` and `mcf_restore_the_local_thrones` to the other's exclusion list.

### M2. Principality route choice is flat and the AI always picks the loyal crown (Medium, score-only, hand)

- `mpf_the_loyal_crown` 50, `mpf_seat_in_the_federation` 40, `mpf_the_claim_of_independence` 5, no input (`principality_focus.txt:498-570`). The crown has no availability condition, the federation seat needs the Malta federation flag (usually not yet set when the choice opens), and independence is unavailable above Cooperative loyalty. A Defiant principality still takes the crown, which adds `loyalty_large`. The federation seat and the independence claim are starved. The patron form is similar: `mpf_appeal_to_rome` 20 (needs `malta_papal_supremacy`, see H2) is below the order and the notables at 30 each (`:871`).
- Fix: add loyalty modifiers from `malta_pr_loyalty` (add to independence and a low factor on the crown below `defiant`; add to the federation seat when `malta_pr_federation` is set).

### M3. Three of four succession arbitrations, the tribute burden and the dissolve have AI 0 (Medium, hand)

- `principality_decisions.txt:553` (burden), `:630-632` (order), `:666-668` (local), `:706-708` (papal), `:787-789` (dissolve). Only `malta_pr_arbitrate_heir` scores (60). The AI never picks the order, local or papal arbitration whatever the charter form (`malta_pr_form_id`).
- `malta_pr_has_failed` (loyalty below 25) is a short window: `malta_pr_break_away` follows after the review count. The AI never dissolves, so it loses the states instead of recovering them.
- Fix: score each arbitration by `malta_pr_form_id` (crown heir, order, local council, papal) and by `malta_papal_supremacy`; add a dissolve score when `malta_pr_has_failed = yes`.

### M4. Regional crusade ignores current wars (Medium, hand)

- `malta_ai_regional_crusade` (`mtth:255-274`) reads Standing, divisions, cohesion and the anchor count, but not `has_war` or a war with a major. The only brake is the one-crusade flag. An AI Malta in its opening wars with up to four displaced owners can open a further front.
- Fix: add a factor under war with a major or above a declared number of wars; the spec principle is "coherent fronts".

### M5. Landing state is chosen from a wider pool than the AI scores (Medium, hand)

- `malta_select_new_landing` scores targets by `malta_state_is_landing_candidate` (`decisions.txt:1064`), but `malta_select_landing` picks `random_owned_state` with `malta_state_is_campaign_pool` (`action_effects.txt:620-621`). A target such as Italy can yield Rome or the wasteland North African coast; Greece can yield the mainland.
- Fix: use `malta_state_is_landing_candidate = yes` in that limit.

### M6. Demand scores ignore whether a compromise is still allowed (Medium to Low, exact for event .8)

- `malta_ai_compromise_demand` and `malta_ai_refuse_demand` (`mtth:58-85`) do not read `malta_can_compromise_demand`, but the event option and decision gate on it. After a compromise with the same order, a payable demand at working cohesion leaves accept 0, compromise unavailable, refuse 0. The AI then picks "later" (100% in event .8) and the demand lapses at 45 days into answer 3, which has the same effect as refuse (`core_effects.txt:433-446`, `:693-697`). Not dangerous, but the AI lets cohesion fall without ever choosing it.
- Fix: add `malta_can_compromise_demand = yes` to the compromise modifiers and a refuse modifier for the case that neither accept nor compromise is possible.

### M7. No AI strategies or plans exist for the package (Medium, spec gap)

- Spec `06_focus_tree_architecture.md:528-545` requires 14 strategy plans (survival first, Grand Magistry, Langues, civil, order routes, Papal, federation, Eleventh recovery, hidden routes). None exist for MLT, `CRU_*` or `MQ*`. Focus order comes only from base weights; war goals, front control and templates for the custom banners are left to the engine default. This is a limit on the claims of this audit, not a defect in a file.

### L1. Magic numbers where the constants file already has a `malta_ai` group (Low)

- Every score in the MTTH file is a literal (`add = 40`, `20`, `10`, `45`, `15`, `30`, `35`, `55`, `90`, ... `mtth:39-381`), plus `has_political_power < 30` (`mtth:123`) and the grievance tests `value = 2` and `value = 0` (`mtth:48`, `:69`, `:83`). Target factors `0.5`, `1.5`, `2`, `0.25` are literals in `decisions.txt:322`, `:326`, `:447-466`, `:1084`, `:1088`. All 147 focus `base` values and the event `ai_chance` bases are literals. The principality entries already use `constant:malta_pr_ai.*`. Spec 28 reserves a constant group `event_038_ai` for scores. Suggest a `malta_ai_score` table beside `malta_ai`.

### L2. Banner ordering contradicts the file header and ignores war state (Low)

- Header (`mtth:4-11`) and spec say the ordinary line comes first, but armored knights score highest (30), then ranged (25), mounted and siege (20), engineers (10) (`mtth:196-247`). Armored Knights are the family with the lowest cap and the heaviest equipment burden. No war or economy input, so an AI at peace fills banners to the cap at the same score as in war.

### L3. Other low items

- Settlement rows ignore resistance and compliance of the target state (`decisions.txt:508-514`, `:557-563`, `:606-612`) and direct settlement scores 0 until Recognized (`mtth:276-283`), so a Functional AI settles only through order grants (20, plus 10 when quiet).
- Charter score is identical for all seven kinds and ignores resistance, supply and the comparison with direct rule (`mtth:408-414`).
- Enforce (35, loyalty at most 30) and lighten (25, loyalty below 40) are contradictory yet both positive in the 25 to 30 band (`principality_decisions.txt:459-466`, `:504-511`).
- Positive weight on gated choices: `malta_ai_raise_siege` second modifier (`mtth:234-237`) and `malta_ai_accept_fortress` first modifier (`mtth:370-375`) do not read their own payability and fortification conditions. Harmless because the decisions gate on availability.
- Volunteers can be called again after every failure because only `malta_volunteers_called` is cleared (`action_effects.txt:703`); bounded by the failure cap of 3 and by costs scaled by failures.
- Event .21 grants to a seated order with equal 25 per order, ignoring grievance and influence (`events:586-660`). Event .30 recipients refuse 75% of the time whatever Malta's strength (`events:670-690`).
- Demand interval stacking: united (1.5) times rotating offices (1.5) gives 438.75 days, above the 330 day band of spec 28. The `minimum_days` floor of 60 is never reached (lowest value 82.5).

## Named scenarios

Candidate pool: complete for each decision set listed; external factors: only those named, everything else assumed available and payable. Classification: score-only except where stated.

### SC-1 Early Malta order, no regions opened (hand)

State: Functional (3 anchors), cohesion 42, legitimacy 40, 12 divisions, at war, convoys below 40, sea road held, banner slot free, all costs payable.

| Decision | Score | Note |
| --- | --- | --- |
| `malta_escort_sea_road` | 90 | 45 war + 35 low convoys + 10 |
| `malta_fortify_port` Malta (heartland) | 80 | 40 times 2 |
| `malta_repair_holy_land_rail` | 35 to 55 | 55 while the corridor counter is below 60 days |
| `malta_settle_order_grant` | 30 | 20 strained + 10 quiet |
| `malta_raise_armored_knights` / ranged / mounted | 30 / 25 / 20 | |
| `malta_launch_regional_crusade` | 0 | the 40 branch needs Recognized, the 15 branch needs 15 divisions |
| `malta_settle_direct_commandery` | 0 | needs Recognized |
| `malta_convene_joint_command` | not eligible | needs cohesion 50 (MCP agrees: never eligible) |

Result: survival rows lead, expansion is correctly off. The main open question is H2/M4 for later phases. Focus choice after the council: frame the settlement 60, then secure the sea road, charter the orders, fortify the Holy Land 40 each, knight banners 30, appeal to governments 25 (hand); settlement trio per M1.

### SC-2 Mid-campaign, Holy Land held (hand)

State: Recognized, cohesion 58, 16 divisions, Levant and Greek regions opened, war with a Greek neighbor possible.

- Regional crusade base 55 (40 + 15). By target: Lebanon or Syria 82.5 (Levant frontier factor 1.5); Greece 82.5 (island state factor 1.5); a target already at war with others times 1.5 again; Turkey 55, or 27.5 above 25 divisions; any major 0 (H2).
- Escort 55 (war + 10), joint command 45 (25 + 20 war), banners 30/25/20, settle direct 30, order grant 10, seize treasury 0 (needs cohesion 60 and political power below 30).
- Demand answer (event .8, exact for the declared state, d100 rounding applies): payable, cohesion working, grievance below 2, influence normal: compromise 15, later 1, so 93.75% compromise. With grievance 2 or more and high influence: accept 30, later 1, so 96.8% accept. Payable, cohesion below 50: accept 40, later 1, 97.6% accept. Half payable only: compromise 45, 97.8%. Nothing payable: refuse 30, 96.8%.

### SC-3 Principality chartered, Evolution II (hand)

Charter 30, plus 30 at 5 or more expedition states, for each of the seven kinds, same score for all (L3). Chartered loyalty starts at 60 (Cooperative). Levy needs loyalty 65 (0 at start), relief 40 when the principality needs relief, integration 10 at loyalty 70, federation 30. Route choice per M2.

### SC-4 Principality under pressure (hand)

Loyalty 28 with a crisis: arbitrate heir 60, relief 40, enforce 35, lighten 25, levy 0, integration 0, burden 0, dissolve 0 (M3). Enforce and lighten both positive (L3). Focus route stays at the loyal crown (M2). Below 25 the principality is failed and the AI still scores dissolve 0.

### SC-5 Rome and the western question opened (hand)

`mcf_the_western_question` needs Recognized Standing and `malta_papal_relations`. It sets `malta_western_question`, which opens state 2 as a campaign target (`map_triggers.txt:149`). The AI crusade against Italy scores 0 as long as Italy is a major (H2), so `mcf_return_the_keys_to_rome` (30) is never available. The Church lane stops there for an AI Malta.

## Timing

Exact, no sampling. Intervals are deterministic day offsets from an MTTH value (not stochastic MTTH draws).

| Interval | Base | Value | Jitter (equal thirds) |
| --- | --- | --- | --- |
| Order demand, stable | 195 | 195 | 180, 195, 210 |
| Order demand, United cohesion | 195 x 1.5 | 292.5 | 277.5, 292.5, 307.5 |
| Order demand, open rivalry | 195 x 0.5 | 97.5 | 82.5, 97.5, 112.5 |
| Order demand, offices rotating | 195 x 1.5 | 292.5 | same |
| Order demand, United and rotating | 195 x 2.25 | 438.75 | outside the spec band (L3) |
| First demand | | 90 days after setup | |
| Principality succession, crown or order | 540 | 540 | |
| Local council | 540 x 0.75 | 405 | |
| Papal appointee | 540 x 1.5 | 810 | |
| Federated | 540 x 1.5 | 810; papal and federated 1215; local and federated 607.5 | |

No interval fires instantly or never fires. Order of the demand kind (hand, exact): Templars 36.4/27.3/18.2/18.2 percent for treasury/command/levy/headquarters; Naval 20/40/20/20; Teutonic 20/20/40/20; Hospitallers, Lazarus and Siege 20/20/20/40.

## Material limits and blockers

Limits (checks that could not answer):
- `hoi4.probability_inspect` cannot expand `mtth:` inside `ai_will_do` or discover `common/mtth` entries, so no MCP number exists for any decision score. Hand values rely on the reading of `factor = 0` plus ordered `add` described above, and on `constant:` tokens being accepted in `has_equipment = { convoy_1 < ... }` and in `mtth` `factor`, which `hoi4.script_validate` does not check inside argument blocks.
- The decision selection rule (one decision per evaluation or all decisions above 0) is not documented locally. Every decision ranking is labeled score-only and starvation claims (integration 10, engineers 10) are conditional on a race.
- No probability, rank-reversal or cumulative result for a focus was produced by MCP beyond the three-way settlement choice.

Implementation blockers: none. M7 is a spec gap (no AI strategy plans) that this audit cannot close. I applied no fix.

## Recommended fix order for the parent

1. H1 (clear the two force flags, require `malta_transports_rebuilt` to launch).
2. M1 (four `mutually_exclusive` lines).
3. H2 and M4 (replace the hard major exclusion and add a war gate to the crusade score).
4. M5 (one `limit`), M3, M2, M6.
5. Move literals to a `malta_ai_score` constants table (L1) when the other tuning is done, then re-run `hoi4.probability_analyze` (`analysis = compare`) on the same scenarios once the analyzer can expand `mtth:`.

## Addendum, 18 Oct 2026: fixes applied

Disposition: implemented for H1, H2, M1 to M7, L1 to L3 except the items listed under "Not done". Source review and hand calculation only. One `hoi4.probability_inspect` call on the principality decisions (`decision_ai_will_do`) returned `PROBABILITY_ANALYZED_PARTIAL` with `malta_ai_weight`, `FROM` and `set_temp_variable` unresolved, so every number below is a hand calculation from the changed script (score, not probability). `hoi4.focus_inspect` on `malta_crusaders_focus_tree` shows 0 connector crossings and 0 node intersections after the four exclusion lines; its 9 warnings (long connectors and linear detours) exist before the change. `hoi4.script_validate` on the changed decision and effect files reports no findings (parameters unchecked).

### What changed

| Finding | Change |
| --- | --- |
| H1 | `malta_hold_foothold_failure` and `malta_close_eleventh_crusade` clear `malta_eleventh_force_ready` and `malta_eleventh_force_weak` (the close also clears `malta_transports_rebuilt`). `malta_launch_eleventh_crusade` requires `malta_transports_rebuilt` plus the force flag, and `malta_launch_ready_tt` says so. Both `malta_ai_launch_eleventh` modifiers read `malta_transports_rebuilt`. The rebuild mission now cancels when the Eleventh Crusade is no longer active, so it cannot set the force flag after a close. |
| H2 | The hard 0 on majors is replaced. Regional crusade: factor `malta_ai_score.major_target_factor` (0.25) for a major target, and factor 0 only while the actor has fewer than `malta_ai.major_target_divisions` (20) divisions. The ultimatum row now scores through the new `malta_ai_ultimatum` entry (25 when payable, Functional, working Cohesion and 10 divisions; 0 while losing a war) with the same major gate. A war with a major halves it again. |
| M1 | `mutually_exclusive` added both ways between `mcf_codify_emergency_command` and `mcf_restore_civilian_courts`, and between `mcf_a_network_of_commanderies` and `mcf_restore_the_local_thrones`. |
| M2 | Principality route weights read `malta_pr_loyalty`: see the table below. Constants `malta_pr_ai.route_*`. |
| M3 | `malta_pr_arbitrate_order`, `_local`, `_papal`, `malta_pr_burden_tribute` and `malta_pr_dissolve` have conditional scores (table below). |
| M4 | `malta_ai_regional_crusade` is halved by any war, halved again by a war with a major, and 0 while `enemies_strength_ratio` is above `malta_ai.losing_ratio` (0.8). |
| M5 | `malta_select_landing` limits to `malta_state_is_landing_candidate`. |
| M6 | Compromise scores need `malta_can_compromise_demand`. New accept row after a spent compromise, and the refuse row also fires when the full price cannot be paid and no compromise is left. |
| M7 | 12 of the 14 specified plans written in `common/ai_strategy_plans/038_malta_crusaders_focus_plans.txt` (survival first, Grand Magistry, Langues, civilian constitutional, Hospitaller, Templar, Teutonic, naval island, siege, Papal Holy See, Eleventh recovery, principality federation) and five condition-gated blocks in `common/ai_strategy/038_malta_crusaders_ai_strategy.txt`. |
| L1 | Every MTTH score and the decision target factors use the new `malta_ai_score` group and extra `malta_ai` thresholds. |
| L2 | The banner order is ranged 30, mounted 25, knights and siege 20, and every banner halves in peace. The file header says so. |
| L3 | Settlement rows get a 1.5 factor for state resistance above 25 and a 1.5 factor for compliance below 50. Enforce applies at loyalty 30 or less, lighten only above 30. The siege banner corridor bonus now needs payability. Rotating offices lengthen only a stable council. |

### Before and after, named scenarios (hand, score only)

| Scenario | Before | After |
| --- | --- | --- |
| Failed landing, nothing rebuilt | select landing 60, launch 70 (stale flag) | launch 0 until rebuild (75) finishes; then 70, or 25 after a timed-out rebuild with fewer than 2 failures |
| Regional crusade, Recognized, 22 divisions, peace, Italy over 25 divisions | 0 | 55 x 0.25 x 0.5 = 6.9 (10.3 if Italy is also at war with others) |
| Same, 14 divisions | 0 | 0 (major gate) |
| Same against a minor with a bridge state, 16 divisions, peace | 82.5 | 82.5 |
| Same, at war with a non-major | 82.5 | 41.25 |
| Same, at war with a major | 82.5 | 20.6 |
| Same, losing (ratio above 0.8) | 82.5 | 0 |
| Ultimatum, 22 divisions, minor target / Italy | 0 / 0 | 25 / 25 x 0.25 x 0.5 = 3.1 |
| Demand: payable, working, grievance below 2, compromise spent | accept 0, refuse 0, later 100% | accept 15, later 1: 93.75% accept |
| Demand: half payable only, compromise spent | refuse 0, later 100% | refuse 30: 96.8% refuse |
| Demand: other cases | unchanged | unchanged |
| Principality route, loyalty 70 (crown / federation / independence) | 50 / 40 / 5 | 75 / 40 / unavailable |
| Loyalty 50 | 50 / 40 / 5 | 50 / 60 / 5 |
| Loyalty 35 | 50 / 40 / 5 | 12.5 / 60 / 20 |
| Loyalty 20 | 50 / 40 / 5 | 12.5 / 60 / 40 |
| Succession crisis, loyalty 45, crown form (heir / order / local / papal) | 60 / 0 / 0 / 0 | 60 / 0 / 70 / 0 |
| Crisis, loyalty 80, supremacy held | 60 / 0 / 0 / 0 | 60 / 45 / 0 / 45 |
| Failed by loyalty, holds land / holds no state (dissolve) | 0 / 0 | 30 / 60 |
| Burden, loyalty 80, at war / at peace | 0 / 0 | 20 / 0 |
| Loyalty 28 (enforce / lighten) | 35 / 25 | 35 / 0 |
| Loyalty 35 (enforce / lighten) | 0 / 25 | 0 / 25 |
| Banners at war (ranged / mounted / knights / siege) | 25 / 20 / 30 / 20 | 30 / 25 / 20 / 20 |
| Banners at peace | same as war | 15 / 12.5 / 10 / 10 |
| Demand interval, United and rotating offices | 438.75 days | 292.5 days |
| Demand interval, rivalry and rotating | 146.25 days | 97.5 days |

### Not done

- The 147 focus `base` values and the event `ai_chance` bases remain literals. They are single rows with no shared table, and a generic constant per number would not make them clearer. The principality route rows changed in M2 use constants.
- The hidden Teutonic alliance and the Holy World preparation plans (2 of 14) belong to the routes the parent deferred (`00_README.md`, "Deferred to a later pass"); they have no flags to read yet.
- The patron form's `mpf_appeal_to_rome` weight (20) was not changed. It is reachable now that Rome can be taken (H2).
- Event .21 grant weights and event .30 refusal at 75 percent were not changed (L3, harmless).
- No re-run of the analyzer comparison: `mtth:` and `set_temp_variable` weights are not modelled, so a before and after comparison can only be hand arithmetic.
