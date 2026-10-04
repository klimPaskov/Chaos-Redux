# Dated occupation benchmark and coverage gap

Disposition: unresolved.
Acceptance basis: the user's requested historical-control and cause-separated population-loss verification for the camp administration rework.
This is a benchmark of the current source-linked arithmetic envelope, not an HOI4 engine result or a casualty target.

## Historical reference

The [United States Holocaust Memorial Museum's account of Nazi murder](https://encyclopedia.ushmm.org/content/en/article/documenting-numbers-of-victims-of-the-holocaust-and-nazi-persecution) estimates six million Jewish people murdered by Nazi Germany, its allies and collaborators, including about 2.7 million at killing centers, about two million in mass shooting operations and related massacres, 800,000 to one million in ghettos and labor or concentration camps, and at least 250,000 through other violence outside camps and ghettos.
These are overlapping approximations with different geographic and institutional boundaries from the mod's generic occupation cohorts; they cannot be turned into a monthly quota or a protected-group selector.
The [USHMM account of Hungary](https://encyclopedia.ushmm.org/content/en/article/the-holocaust-in-hungary) documents roughly 437,000 deportations between 1944-05-15 and 1944-07-09, with about 420,000 people transported to Auschwitz-Birkenau.
That movement supports a dated route design but does not prove an in-game source-state cohort or controller.

## Current modeled envelope

The restricted source test in `historical_envelope_results.json` advances only three registered German occupation origins from their scripted starting dates through 1945-04: Poland 2,063,862 campaign deaths, the Netherlands 107,308, and Hungary 132,801.
Their combined campaign envelope is 2,303,971; the most severe tested 700,000-capacity domestic custody sensitivity adds 51,816 deaths, reaching 2,355,787 across these included rows.
This arithmetic is 3,644,213 below the six-million benchmark, but it is not a like-for-like historical reconstruction: only three origins and one domestic sensitivity are counted, control and supply are assumed in the source evaluator, and the separate Łódź source-control sensitivity is not aggregated into this wider envelope.
The subsequent [European origin inventory](europe_origin_coverage_matrix_2026-09-26.md) enumerates the starting European state IDs for all 21 seeded origins and excludes German home-origin states from occupation admission. Its expressly counterfactual all-foreign-origin full-control calculation reaches 5,874,870 campaign deaths, but includes Britain and Axis allies as if Germany directly controlled every state for the entire period; that near-six-million arithmetic is evidence of premise sensitivity, not historical calibration.
The later [nine-state dated sensitivity](staged_state_control_sensitivity_2026-09-26.md) measures 589,297 modeled local campaign-cause losses from 909,411 apportioned source people under stated month windows, with no competing movement or outside losses. Its Riga and Thessaloniki checks show that population-weighted allocation can understate the source population of a historically concentrated community even before cause-specific deaths are modeled. It is a partial source-model audit and cannot be added to the separate Łódź case or promoted into a six-million match.
The [four-state supplement](supplementary_direct_control_sensitivity_2026-09-27.md) adds Norway, Bohemia, Moravia and Eastern Serbia under separate bounded control windows; the disjoint thirteen-state modeled subtotal is 707,607 occupation-cause losses from 1,081,811 allocated source people. Its separate Denmark no-rescue negative control would imply 2,859 local campaign deaths in only two states, contradicting the historical scale and rescue chronology in [USHMM's Denmark account](https://encyclopedia.ushmm.org/content/en/article/denmark); those Danish modeled deaths are rejected, not added to the subtotal. This reveals a policy-timing and origin-preserving movement gap rather than a reason to tune the global campaign fraction toward any historical total.
The source includes a bounded August–September Łódź state-87 to state-88 occupation-to-custody movement, a separate German state-88 detention setup, and a player/AI paid exact-cohort transfer choice after administration begins.
The manual choice draws a bounded share of a selected living registered occupation row; it is distinct from the historical Łódź episode.
The Łódź sensitivity executes its own dated arithmetic path in this JSON; neither path is proven by a dated engine scenario.
The 700,000-capacity case has 747,616 cumulative admissions because a recorded death can free finite capacity for a later independently debited admission; it does not create people or refill a historical stock ceiling.

| Cause or path | Historical reference | Current modeled evidence | Acceptance consequence |
| --- | --- | --- | --- |
| Killing centers | About 2.7 million across five centers | The state-88 Łódź sensitivity measures arrival violence as a subset of killing-center violence, while the restricted wider envelope has no center-specific engine receipt or complete network. | No Europe-wide center-specific comparison can be claimed. |
| Mass shootings and related massacres | About two million | The generic occupation campaign records actual violence losses, displayed as occupation violence without a method-specific mass-shooting subtotal. | Cause split and historical attribution need a dated engine scenario. |
| Ghettos, labor and concentration camps | 800,000–1,000,000 | The tested domestic capacity sensitivities range from 10,392 to 51,816 custody deaths at zero support, with lower custody and separate labor deaths when fully supported. | The isolated domestic test is not a Europe-wide camp reconstruction. |
| Other violence outside detention | At least 250,000 | The occupation ledger has a wider-loss receipt but no full Europe-wide origin coverage or method-specific control case. | Keep this distinct from custody and site deaths in any comparison. |
| Hungary to Auschwitz movement | About 420,000 transported in May–July 1944 | State 43 is Northern Hungary/Budapest in the map inspection; installed vanilla `STATE_88` localizes Kraków, while the `88-Kielce.txt` filename differs. The mod uses state 88 as its Kraków/Auschwitz-area site abstraction, and no Hungarian source caller proves GER control of state 43. | A separately accepted Hungarian source cohort and route-valid control scenario remain required. |
| Łódź to the state-88 site | The August–September 1944 movement is documented in the Łódź sources cited by `cross_state_movement_handoff.md`. | `camp_occ_try_lodz_auschwitz_transfer` reserves the proven living state-87 row and attempts at most 12 waves per month, bounded by supported undamaged throughput, resident capacity, and exact receipts; the dated arithmetic case measures 72,950 transfers and 47,408 arrival losses. | Natural 1944 killing-role support, GER control, engine debit/credit/bind/rollback receipts and cause calibration remain unverified; the historical transport estimate is not a casualty quota. |

The Japanese China sensitivity in the same JSON is intentionally separate: its 38-month direct-share variants produce 1,350,042, 2,693,037, or 5,379,020 combined campaign/custody/labor deaths under assumed persistence, with zero Pingfang institutional deaths in that arithmetic.
None is an accepted estimate of China's total occupation losses or Unit 731 deaths; Pingfang requires its own measured institutional receipts and dated control case.

## Dated Łódź and state-88 source-control sensitivity

The added `test_dated_lodz_to_krakow_cause_and_capacity_envelope` in `occupation/test_historical_envelopes.py` explicitly assumes German control of states 87 and 88 from July 1941 through September 1944, one supported 25,000-person killing-center level in state 88, zero prior custody and no outside population losses.
It apportions the existing three-million Polish origin ceiling to state 87 using installed vanilla starting-state population as the accepted geographic proxy; the initial modeled state-87 cohort is 247,229 people.
At the current 2.5% monthly campaign fraction, the source records 151,559 occupation-violence deaths through September 1944 and retains 22,720 source survivors.
The August–September living movement is 72,950 people across 24 bounded batches, with one equal source debit and destination credit per accepted batch and no transport death; 23,949 requested living people remain untransferred at the October cutoff.
The distinct arrival-phase request records 47,408 actual destination losses against bound rows, within site violence, while 49 custody and 496 later killing-role deaths leave 24,997 of the imported group alive in state 88.
The September site deaths are applied before that month's occupation transfer, matching the package integration order.
The model conserves the physical source-plus-destination population and the exposed cohort separately, and its cause totals do not assign outside losses to Germany.

[USHMM records about 67,000 deportations from Łódź to Auschwitz-Birkenau in August–September 1944 and about two-thirds murdered upon arrival](https://encyclopedia.ushmm.org/content/en/timeline-event/holocaust/1942-1945/liquidation-of-the-lodz-ghetto).
This sensitivity moves 5,950 more living people and records about 3,408 more arrival losses than the approximate 67,000 transport and 44,000 immediate-murder comparison points; it is not a like-for-like reconstruction because center support, prior custody, control and no-outside-loss assumptions are model inputs rather than engine observations.
The request fraction and throughput are centralized tuning, and every loss requires a bound row and measured physical debit; no casualty or deportation quota was imported into gameplay to force a match.
The isolated two-month sensitivity in `historical_envelope_results.json` begins with the same 96,899-person August living source but omits later campaign attrition and ordinary custody loss: arrival request fractions of 0.55, 0.65 and 0.75 yield 30,539, 46,402 and 72,670 measured arrival losses, respectively, with 55,539, 71,402 and 96,899 living transfers.
With support removed or control absent, it moves nobody; with deaths disabled, it moves only the first 25,000 living people into resident places and records no loss.
That wide sensitivity is a balance uncertainty, not evidence of historical accuracy or an engine receipt.

## Required acceptance work

Execute and validate the source-implemented origin-preserving Łódź movement in a route-valid dated scenario with one measured living-person debit, credit and custody bind, rollback evidence, and later destination deaths attributed to the original authority.
The post-cutover state-88 setup establishes only detention; AI attempts the guarded paid mandate, setup and killing-role helpers in source order. The package now also schedules a bounded hidden country timer when a relevant country enters its registry, so monthly administration does not rely on the Chaos Meter on-action when `settings_chaos_meter_disabled` is set. The timer's live scheduling and month-key persistence remain unverified.
Run dated, controlled GER and JAP occupation scenarios that separate custody, labor, killing-center, institutional, wider territorial, and outside losses; report the actual source-population headroom and all external competing debits.
Compare the cause totals with the linked historical ranges without forcing any cause to match an estimate through a quota.
Until that evidence exists, `historical_total_acceptance_complete` must remain false.
