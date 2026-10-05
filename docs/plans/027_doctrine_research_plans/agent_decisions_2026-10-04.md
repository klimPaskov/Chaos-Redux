# Event 027 agent decisions, 2026-10-04

Disposition: accepted and implemented under the full-authority mandate that the user granted for the Event 027 takeover. Each decision records the choice, its spec basis, and the implementing commit. Items that only a live session can prove are marked needs_live_game.

Commits: `b55edd969` (adoption of the stopped rework plus D1 to D5, D7, D8, D9, D11), `317e43684` (D6), `2a8be6e32` (D10), `408809418` (D16), and the round 2 follow-up commits named in the final report (the D10 Milestone readback, D17, D18).

## D1. Reopen empty-track assignment with its first mastery step

Decision: `doctrine_research_empty_track_is_verified` delegates to `doctrine_research_native_mastery_adapter_is_verified` again, and the registry-level `doctrine_research_empty_track_adapter_is_verified` checks `doctrine_research_adapter_registry_initialized`, as at the pre-rework HEAD. The stopped thread's `always = no` closure is not adopted.

Basis: the spec README, part 1 and part 2, and the acceptance criterion "An empty track can select one eligible subdoctrine and receive its first event mastery step". The closure was an evidence gate, not a design change, and it removed every fresh-track page (`.60` to `.77`) after a Grand Doctrine adoption and made First Lesson and Single School unreachable.

Implementation: the existing transaction (`set_sub_doctrine` with folder and numeric track index, post-assignment level readback written to the receipt pre-level, `adoption_only`/`.13` when stored mastery completes the branch, then the one-step loop) runs unchanged. The `.7` confirmation has its own empty-track text (`doctrine_research.confirm.assign_mastery`). The AI reaches the same subdoctrines through `doctrine_research_selected_empty_subdoctrine_is_valid`.

Source trace for the achievements: after an adoption every track of that domain is empty, so the next choice in the same batch takes the empty-track path, produces a consumed mastery receipt with a positive post-level, and satisfies First Lesson. In an Evolution IV batch an empty track yields a 0 to 1 receipt followed by four ordinary steps to level 5, which satisfies Single School.

needs_live_game: `set_sub_doctrine` on an empty track with folder and index, and the banked-level readback after it.

## D2. Per-country firing isolation and ledger repair

Decision: all-or-nothing publication is replaced. The recipient scan initialises and validates each candidate's ledger inside the `every_country` block, repairs a corrupt ledger by discarding its unused rows and receipts without compensation (`doctrine_research_repair_country_state`), and leaves out only a country whose ledger still fails. Each append is isolated; the firing commits whenever at least one batch was published, records one actorless History row with the firing size, and wakes every published country. A firing with no recipient records one payload-zero row and wakes nobody.

Basis: spec part 1, "Every live country with at least one valid registered doctrine action receives one batch".

Source trace of the counterexample: country A has a valid ledger and country B a misaligned one. In the scan A passes and is added; B's initialisation sets the corrupt flag, the repair discards B's rows and clears the flag, and B is added with an empty ledger. Both append a queued row, the binder wakes both, and A's `.14` wake starts A's batch.

## D3. Daily evolution pulse after the first firing

Decision: `doctrine_research_evolution_pulse` runs `doctrine_research_process_evolution` from each global-host branch of `chaosx_on_actions_chaos_meter.txt`, only after `doctrine_research_fired_once`. The tag-switch branch reconciles the former host before clearing its marker and the new host after setting it.

Basis: spec part 3, promotion about 90 days after eligibility; the first firing still opens at the highest enabled stage.

## D4. Mastery point guard at one level's reward cost

Decision: the one-point loop stops at the reward cost of the level being reached: `mastery_point_loop_limit = 100` (DEFAULT_REWARD_MASTERY in vanilla `00_defines.lua`, also the Chaos Warfare thresholds), `special_forces_mastery_point_loop_limit = 60` (every reward in vanilla `special_forces_subdoctrines.txt`), and `peoples_war_short_level_point_limit = 50` for People's War levels 1, 2, and 4, with level 3 (`peoples_war_full_cost_level`) at 100.

Basis: the spec's one-step rule. A readback that does not update in the same effect now ends as ambiguous after crossing the target threshold once instead of granting about ten levels. Residual edge: a People's War step to level 3 with at least 50 points of partial progress can also cross level 4 if the readback lags.

needs_live_game: whether `has_mastery_level` updates in the same effect after `add_mastery`.

## D5. One re-prompt and bounded lifecycle work

Decision: lifecycle reconcile returns before any ledger work for countries without a ledger, an active batch, or queued rows, and re-prompts a human only when no Event 027 page is open (the prompted flag), including the `adoption_only` case, so repeated state-control callbacks produce exactly one `.13` page. Closed batches are compacted before the next batch opens, keeping the most recent closed row, and achievement checks read only the active or closing batch.

Basis: spec part 1 persistence rules and the `MAX_EFFECT_ITERATION = 1000` limit.

## D6. AI domain weights follow real capability

Decision: Navy scores zero without a coast, dockyards, ships, convoys, or naval doctrine; its war term needs warships and a war without a land front, and its geography term a coastal capital. An industry focus term goes to Navy when dockyards times 2 reach the military factory count and to Army otherwise. Army takes the land-front war and geography terms. Special Forces readiness, war, production, and alliance terms need Special Forces templates (including marine commandos), and Grand Doctrine and subdoctrine scoring use the same readiness. Air terms need deployed air wings. When no domain scores, every valid domain falls back to the base weight. Human and AI validity pools are unchanged.

Basis: spec part 3 AI strategy and the DR-A scenarios in `027_doctrine_research_probability_scenarios.md`. Evidence: `probability_domain_compare_2026-10-04.md`.

## D7. National Breakthroughs cooldown

Decision: cluster 9 uses `event_cluster_cooldown_days.national_breakthroughs = 120`, both shared gate blocks reject it while `event_cluster_national_breakthroughs_cooldown` is set, and the cooldown branch sets the flag with the days passed through a temp variable.

Basis: the shared cluster contract followed by every other positive repeatable cluster.

## D8. Event Details text keeps the choice-count premise

Decision: the Event Details description that explains the one-to-five choice range is kept. It states the premise without raw effects, which settles the open mechanics-versus-premise question.

## D9. Adoption of the stopped thread's rework

Decision: the stopped thread's direct dispatch, firing envelopes, History binder, `.14` wake, receipt alignment and replay guards, AI zero-choice closure, achievement debug exclusions, grouped level getter, caller-side temp declarations, cluster 9 with row 9001, Event Details and evolution selectors, and preview rows are adopted. Only Event 027 hunks of shared files were committed; Equipment from Heavens, Various Anomalies, and Acid Rain hunks stay uncommitted. The settings dispatch arm was rebuilt from HEAD plus only the Event 027 `if`/`else` wrapper.

## D10. Special Forces mastery with both tracks occupied

Decision: Special Forces grants and readbacks filter by folder and subdoctrine only. While both tracks are occupied, the first Special Forces entry and page (labelled "Special Forces") cover the active subdoctrines of both tracks and the second entry stays hidden. Receipts keep the selected track label, and Joint Curriculum and the batch summary count Special Forces progress per subdoctrine. Empty-track candidates exclude a token whose xor sibling holds a track; assignment keeps the numeric `set_sub_doctrine` index.

Basis: vanilla `special_forces_subdoctrines.txt` (each token lists both tracks and is xor-locked with its sibling) and the "fully adapted or explicitly absent" adapter criterion. The Special Forces Milestone readback follows the shown or advanced token (`doctrine_research_selected_special_forces_subdoctrine_completed`, round 2), because completing a token completes whichever native track holds it; an entry without a token reads its own track. The track menu (`.5`), result page (`.8`), and batch summary therefore report the Milestone of the token in either track.

needs_live_game: two Special Forces tracks never holding the same token.

## D11. Catalog changes are recorded, not applied

Decision: the workbook changes are listed in `catalog_changes_pending.md` for the workbook owner; agents do not edit the xlsx or the exported CSVs.

## D12. A reached stage applies only while its own setting is enabled

Decision: `doctrine_research_prepare_firing_profile` sizes each firing from the highest reached stage whose Event Details setting is still enabled (`doctrine_research_evolution_i_setting_enabled` to `_iv_setting_enabled`), instead of the raw reached stage. Switching Evolution IV off after it was reached makes the next firing use Evolution III, or the highest lower stage that stays enabled; batches already created keep their stored stage and size. The reached stage itself, the promotion clock, and the recorded evolution rows are unchanged.

Basis: spec part 3, "Every stage's availability, record, and effect must check its own enabled state", and the acceptance criterion "Event enable and disable state controls automatic selection and evolution gates cleanly". The round 1 profile read the reached stage directly, so a disabled stage kept enlarging every later batch. Found in the round 1 review; implemented in the review commit.

## D13. One opening page after a suspended curriculum

Decision: the `.12` continue option starts the next curriculum when none is active, and otherwise opens `.2` only when no Event 027 page has been shown for the active curriculum (the prompted flag). A `.14` wake or a lifecycle callback that already opened the next curriculum while `.12` was waiting no longer produces a second `.2` page.

Basis: D5 (exactly one open page per curriculum). Found in the round 1 review; implemented in the review commit.

## D14. The daily evolution pulse respects the event's own enabled state

Decision: `doctrine_research_evolution_pulse` runs `doctrine_research_process_evolution` only while Event 027 is absent from `global.disabled_events`, in addition to the existing `doctrine_research_fired_once` gate. While the event is disabled in the event settings no stage is promoted and no evolution row is recorded; the stored clock resumes when the event is enabled again, and the next firing still re-evaluates the stage through `doctrine_research_prepare_firing_profile`.

Basis: acceptance criterion "Event enable and disable state controls automatic selection and evolution gates cleanly" and spec part 3 ("Every stage's availability, record, and effect must check its own enabled state"). Before the daily pulse existed, evolution processing only ran inside a firing, which a disabled event cannot reach; the D3 pulse removed that implicit gate, so a disabled Event 027 kept writing "Doctrine Research I to IV" rows into the Event Log. Event 026's daily pulse applies the same disabled-event check. Found in the second round 1 review; implemented in the review commit.

Validation limit recorded with it: the one-point guard of D4 equals exactly one level's reward cost, so it also relies on `add_mastery` granting its literal amount when a country carries a negative `<doctrine>_mastery_gain_factor` (needs_live_game, listed in the overview's validation limits).

## D15. Counts on the curriculum pages read as labels

Decision: the opening (`.2`), domain (`.3`), continue (`.9`), and summary (`.10`) descriptions and the five domain options state their numbers as labels ("Choices in this curriculum: 1", "Choices remaining: 1", "Grand Doctrines established: 1", "tracks ready: 1") instead of number-plus-plural sentences.

Basis: the baseline curriculum has one choice and is the most common page in a campaign, so the previous sentences rendered "with 1 doctrine choices", "has 1 choices remaining", and "offered 1 choices" for every Calm World firing; the domain options rendered "1 tracks". The other curriculum pages already used the "Choices remaining:" label. Found in the second round 1 review; implemented in the review commit.

## D16. AI scores mirror the native doctrine preferences

Decision: the stopped thread's uncommitted round 2 AI scoring is adopted and finished (lead decision D-R2-1). Grand Doctrine and subdoctrine scores multiply the campaign-evidence score by the vanilla `ai_will_do` factors, held in the `doctrine_research_ai_native_*` constant categories:

- Grand Battleplan starts from its native base 2; Convoy Raiding and Battlefield Support take factor 10 for a country that is not a major.
- A minor never takes Mobile Warfare or Superior Firepower (native factor 0) unless it fields armour or motorised templates (`doctrine_research_ai_fields_mobile_forces`) or they are its only valid Army Grand Doctrines. Mass Assault's force term reads infantry without mobile templates, or militia and irregulars.
- `doctrine_research_ai_score_selected_subdoctrine_fit` runs for all 107 subdoctrine candidates. Each naval, air, and Special Forces subdoctrine adds the forces term only for its own ship, plane (`has_deployed_air_force_size` or `num_deployed_planes_with_type@<airframe>`), or battalion type; Marines add the coast term and Mountaineers the mountain term. The vanilla base, original-tag, minor, and major factors then multiply the score, starting from `doctrine_research_ai_native_base.neutral`, and a product below the base weight is raised to the base weight, so every valid choice stays possible.

Basis: spec part 3 ("use native or country-specific doctrine preferences where available", "preserve country-specific and custom-system AI factors") and the AI acceptance criterion "Grand Doctrine scoring reuses native or country-specific strategy where available". The factors were checked against every `ai_will_do` block in vanilla `common/doctrines/grand_doctrines/*.txt` and `subdoctrines/**/*.txt` (tag lists, minor and major factors, base-0 subdoctrines, the Irregulars and Guerilla War template requirement, and the Flying Batteries `rocket_artillery` requirement); no mismatch was found. Deviation from vanilla, by design: a native zero leaves a valid candidate at the base weight instead of removing it, because Event 027 must spend every choice on some valid doctrine.

Evidence: `probability_native_preferences_2026-10-05.md` (analyses `probability-3073104d02ab0bddedb3a99e` and `probability-f5be3a5b4624a7ace9ad0003`). Baseline: HEAD `c065f4e31`; the stopped thread's `probability_round2_before/` copy is identical to it and is not committed.

needs_live_game: the AI doctrine mix of minors and of the tagged majors in a real campaign.

## D17. A landlocked country with a maritime plan values Navy

Decision: `doctrine_research_ai_has_maritime_plan` is true for a country without a coastal state that holds a core or claim on a coastal state it does not control, or has or is justifying a war goal against a country that owns a coastal state. It is the last alternative of `doctrine_research_ai_has_naval_capability`, so its state and country scans run only when every other naval check has failed. Inside the Navy scoring block such a country receives the base weight and the strategy weight; the forces, production, industry, war, geography, alliance, and readiness terms still need real ships, dockyards, or a coast. A landlocked country without such a plan keeps Navy at 0 (DR-A04 unchanged).

Basis: spec part 3 ("A future naval plan can justify doctrine adoption before a fleet exists when the plan is explicit through AI strategy, focus route, or country identity") and the DR-A05 failure signal "current coastline is a permanent zero-weight blocker despite an explicit route plan". Vanilla exposes no trigger for planned dockyards, so the plan is read from observable cores, claims, and war goals; a justification in progress counts because it is the AI's own declared plan. The plan disappears with the claim or war goal, so a route that becomes invalid stops raising Navy (the second DR-A05 failure signal).

Evidence: `probability_domain_round2_2026-10-05.md` (analysis `probability-f52aea923ed27276b9b6a643`): DR-A05L Navy 12.0% (was 0%), DR-A04 Navy 0%.

needs_live_game: the cost of the coastal-claim scan for landlocked AI countries on a firing day (expected small: it runs only for countries with no coast, ships, dockyards, convoys, or naval doctrine).

## D18. Air-centred industry gives Air the industry focus

Decision: `doctrine_research_ai_score_domains` sets `doctrine_research_ai_air_industry_led` when the country deploys planes and `num_deployed_planes` reaches `num_divisions` times `doctrine_research_ai_ratio.air_industry` (50, about twice the planes per division of a balanced power), unless dockyards already lead. An air-led power gives the industry focus term to Air instead of Army, and its Air also takes the land-front geography term that Army receives. The Air war term (at war with air wings) is unchanged, and dockyard-led industry still goes to Navy.

Basis: DR-A03 ("Air should lead or remain within the top bounded pool"; failure signal "Air production and air war do not affect the score") and the round 1 gap in `probability_domain_compare_2026-10-04.md`, where Army led 42% to 28%. Moving only the industry focus term leaves the traced DR-A03 vector at Army 18, Air 17; the land-front term is added because an air-centred power fights its land war largely from the air, and it brings Air to 19. `num_deployed_planes` and `num_divisions` are documented dynamic variables (`dynamic_variables_documentation.md`), and vanilla reads `num_deployed_planes` the same way in `operation_strat_effects.txt`.

Evidence: `probability_domain_round2_2026-10-05.md` (analyses `probability-2b89cc5681f283e5b17be463` and `probability-8a4d5d993389078782218933`): DR-A03 Air 36.5%, Army 34.6%; without a land front Air 34.0%, Army 32.0%; DR-A01, DR-A02, and DR-A04 unchanged.

needs_live_game: the planes-per-division mix of real AI campaigns, to confirm that the ratio separates air-centred powers from balanced ones.

## D19. Grand Doctrine and track choices follow candidate fit

Decision: `doctrine_research_ai_score_selected_grand` and `doctrine_research_ai_score_selected_track` read only terms that differ between the candidates of one pool. The divisions, military factory, dockyard, war, coast, faction, domain strategy, and domain readiness terms are removed from both scorers; they stay in `doctrine_research_ai_score_domains`, where they separate domains. The two wrapper triggers that only those scorers used (`doctrine_research_ai_has_selected_domain_strategy_signal`, `doctrine_research_ai_selected_owner_system_ready`) are deleted.

- Track score: base 1, plus `track_fit` 3 when `doctrine_research_ai_selected_track_has_force_fit` holds, plus `investment` 1 for every level the track's active subdoctrine has earned, plus `empty_track_fit` 2 for an empty track that fits, plus `completion` 3 when the track is one step from completing its branch and fits, plus `continuity` 2 for the track of the previous choice in the batch. The sum is squared before it enters the `random_list`.
- Force fit per track: Army Infantry reads infantry, motorised, militia, or irregular templates; Combat Support line, motorised, or rocket artillery, support artillery, anti-tank, or anti-air; Armor tanks, mechanised, or armoured cars; Operations a current war. Navy Screens read destroyers or light cruisers and Capital Ships battleships, battlecruisers, or heavy cruisers; Heavy Aircraft also read maritime patrol planes. A Special Forces track reads the battalion family of the subdoctrine it holds, or any Special Forces battalion when empty. Each Chaos Warfare track reads its own fielded battalions through `num_battalions_with_type@`: Hazard Assault Formations the protection or chemical reconnaissance detachments, Contaminant Fire Support the projector batteries, Toxic Armored Warfare the light, medium, or heavy chemical tank detachments, and Integrated CBRN Command the HQ operations section.
- Grand Doctrine score: base 1 (Grand Battleplan its native base 2), the forces weight for the formations each Grand Doctrine serves, and the D16 native factors. Mobile Warfare adds the forces weight a second time for tank templates (`doctrine_research_ai_fields_armour`), so a tank army that also fields artillery prefers it over Superior Firepower.

Bounded randomness: the track score is squared instead of filtered by a top band. Squaring keeps every valid track at a positive weight, lets a clearly better track win most choices, and leaves equal tracks equal. A ratio band would make every lead of twice the next score deterministic, and in DR-C01 the three level-2 tracks with fit sit above any reasonable band, so it would not separate that case. Grand Doctrine scores are not squared, because the native minor factor of 10 would become 100.

Completion gate: completion needs force fit only. The lead item allowed "force fit or existing investment", but completion already requires a current level above 0, so existing investment is always present when completion applies and that alternative would never gate anything. A near-complete branch the country has no formations for keeps its investment value and no longer wins on completion (DR-C02T: 18.8% against 27.1% for each fitting track; it led at 26.2% before).

Basis: spec part 3 (force composition fit, current-war fit, completion value that must not overpower a severe strategic mismatch, empty-track value, existing investment, multi-choice allocation, and "bounded randomness among the best valid candidates") and the AI acceptance criteria "Track scoring uses force fit ... and completion value", "Completion value cannot force a severe strategic mismatch", "Strong score lead can produce stacking", "Bounded randomness does not allow low-value candidates to dominate", and "Chaos Warfare relevance responds to actual CBRN readiness".

Evidence: `probability_track_round2_2026-10-05.md` (analyses `probability-0d64502a80a1ed77cf016732`, `probability-118a2fd43d7ac254d6dc67d2`, and `probability-3188942c7063a03d8b239fc2`): DR-C01 Armor 52.8%, DR-C04 25% each, DR-C05 dominant 69.1%, DR-B01 Mobile Warfare 45.5% (highest), DR-D03 Hazard Assault 92.3%, DR-D04 Integrated CBRN Command 57.1% (highest), DR-B02, DR-B02-major, and DR-B04 orderings unchanged, and a fresh fitting branch completed by all five Evolution IV choices in 7.2% of close-score batches (0.25% before).

needs_live_game: the AI track mix and branch completion rate in real campaigns.

## D20. Nonhuman countries without a doctrine system stay out of Doctrine Research

Decision: `doctrine_research_country_has_valid_action` also requires the new 027-owned trigger `doctrine_research_country_has_doctrine_system`, which is false for a country where the shared classifier `is_actual_nonhuman_country` holds, unless the country is a Kruger sovereignty (`brilliant_scientist_is_kruger_sovereign_country`). The zombie outbreak countries, Black Plague rat countries, Death, the wendigo cannibals, nonhuman Infantry Spawn derivatives, and the other families in that classifier therefore receive no batch, no curriculum page, and no AI Grand Doctrine or mastery. Ordinary countries, subjects, governments in exile, and human special countries such as REV and the cannibal warlords are not in the classifier and keep participating. A Kruger sovereignty whose population became machine, clone, engineered, or alien is in the classifier through `brilliant_scientist_is_actually_nonhuman_sovereignty`, and the exception keeps it on its normal doctrine graph.

Basis: spec part 1 "Valid country families" ("A plague state with no normal doctrine system receives no fabricated Army doctrine. A Kruger sovereignty with a valid normal or custom doctrine graph may participate through that graph.") and DR-D05 (no candidate and no fabricated reward for a special nonhuman country without an adapter). No current special country registers a custom doctrine adapter, so DR-D06 has no member yet; a future owner adapter would add its own exception to this trigger.

Integration: the firing scan, the shared availability check in `chaosx_logic_effects.txt`, the `.14` wake, lifecycle reconcile, AI resolution, and the human pages all read `doctrine_research_country_has_valid_action`, so no shared file changes. A country that becomes nonhuman while it holds a batch closes it through the existing no-action path (AI completion without spending choices, or the human `.11` page) without compensation, and Event 027 is unavailable when no country outside the classifier has a valid action.

needs_live_game: none beyond the existing lifecycle callbacks; the gate is a pure trigger.

## D21. The one-point guard scales with negative mastery gain factors

Decision: every one of the 107 `doctrine_research_exact_step_*` effects first sets `doctrine_research_transaction_gain_factor` to its own `modifier@<subdoctrine>_mastery_gain_factor` (0 for the four Chaos Warfare subdoctrines) and calls the new `doctrine_research_prepare_transaction_step_limit`, and its `while_loop_effect` compares the guard with the temp `doctrine_research_transaction_step_limit` instead of a constant. The helper:

- sets the reward cost of the level being reached: `mastery_point_loop_limit` 100, `special_forces_mastery_point_loop_limit` 60 for the Special Forces domain, and `peoples_war_short_level_point_limit` 50 for People's War unless the expected level is `peoples_war_full_cost_level` (People's War's own limit block moved into the helper);
- adds the folder factor (`land`, `naval`, `air`, or `special_forces_mastery_gain_factor`; Chaos Warfare reads `land`), the factor of the active Grand Doctrine of the domain (read through `has_doctrine` for each native Grand Doctrine), and the track factor (`<track>_track_mastery_gain_factor`; Special Forces takes the lower of its two tracks, because a token can sit in either native track);
- when the sum is below zero, divides the cost by one plus the sum, rounds up (`round_temp_variable`, then one more point when the rounded value is below the quotient), and caps the result at `mastery_point_guard_cap_multiple` (2) times the cost; a non-positive divisor uses the cap. A sum of zero or above leaves the limit at the cost, so all current behaviour is unchanged for those countries.

All tokens are static, so no `meta_effect` is needed: each step names its own subdoctrine, and the 125 modifier tokens read were checked against the `<Doctrine>_mastery_gain_factor` and `<Doctrine>_track_mastery_gain_factor` type lists of `documentation/modifiers_documentation.md` (lines 1248 to 1278). The Chaos Warfare Grand Doctrine and subdoctrines are not in those generated lists and no vanilla or mod content modifies them, so their factors are not read. `modifier@<token>` in country scope follows vanilla `SWE_scripted_effects.txt:824`. No days, timed flag, or unary minus is used.

Worked case: vanilla France's `FRA_victors_of_wwi` carries `land_mastery_gain_factor = -0.15` (`common/ideas/france.txt:1257`), so an Army step gets 100 / 0.85 = 117.647, rounded up to 118 points; Japan (`japan.txt:2611`, -0.1) gets 112 and Siam (`siam.txt:563`, -0.15) 118.

Basis: D4 and the D14 validation limit. If `add_mastery` applies gain factors, the previous fixed guard of 100 one-point grants delivered 85 real points to France, the level never arrived, every Army step ended ambiguous, and the batch was quarantined. The scaled guard reaches the level whether or not the engine applies the factors. The cap of twice the cost bounds the loop well under `MAX_EFFECT_ITERATION` and keeps the readback-lag overshoot below two levels' cost.

Residual edge (needs_live_game, recorded in the overview validation limits): if the readback lags inside the effect and `add_mastery` ignores gain factors, a country with a negative sum whose branch already holds partial progress above the scaled margin (18 points for France) could cross a second level before the step ends as ambiguous. This is the same failure class as the D4 People's War edge and needs both unproven engine behaviours at once.

## D22. Chaos Warfare fit reads every battalion a track serves, and open pages honour the doctrine-system gate

Decision, AI fit: each Chaos Warfare track's force fit in `doctrine_research_ai_selected_track_has_force_fit` reads the battalions its subdoctrine earns mastery from (the `mastery = { sub_units }` block in `common/doctrines/subdoctrines/land/chaos_warfare_*_subdoctrines.txt`) as well as the companies its bonuses serve. Hazard Assault Formations adds `chaos_battalion`; Contaminant Fire Support adds `cbrn_chemical_projector_battery` and `cbrn_chemical_ammunition_train`; Toxic Armored Warfare adds the light, medium, and heavy `cbrn_*_armored_delivery_detachment`; Integrated CBRN Command adds `cbrn_hq_protective_logistics_section` and `cbrn_hq_medical_countermeasure_directorate`. D19 read only a subset, so a country fielding the projector batteries or armoured delivery detachments that actually earn that track's mastery saw no fit. Every added sub-unit is defined in `common/units/` and pre-registered in `common/synchronized_dynamic_tokens/`. The D19 scenario weights are unchanged, because those scenarios field none of the added battalions.

Decision, participation: `doctrine_research_selected_domain_has_valid_action`, `doctrine_research_selected_choice_is_valid`, and the five domain options of the `.3` menu also read `doctrine_research_country_has_doctrine_system`. D20 gated the batch dispatch, the AI loop, and the `.11` closure, but a human page that was already open when the country became nonhuman still offered domain, track, and confirm options through the per-domain triggers. The domain menu now shows only the closure option, the track page shows its no-option exit, and the confirmation offers only the rebuild path to `.11`. A pending receipt still recovers through its own receipt branch, so no transaction in flight is stranded.

Basis: spec part 3 force composition fit and "Chaos Warfare relevance responds to actual CBRN readiness"; spec part 1 "Valid country families" and DR-D05 (no fabricated reward for a special nonhuman country).

needs_live_game: none beyond D19 and D20; both changes are trigger reads.
