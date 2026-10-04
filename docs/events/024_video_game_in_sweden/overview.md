# Event 24: Video Game in Sweden

Implementation status is incomplete.
The current acceptance ledger is [report 16](../../plans/024_video_game_in_sweden_plans/16_source_repairs_and_remaining_acceptance_2026-10-03.md), with the implemented continuity and restriction repair tranche recorded in [report 22](../../plans/024_video_game_in_sweden_plans/22_runtime_continuity_and_restriction_receipts_2026-10-03.md).
Historical analysis below is not clearance for the current source revision or every accepted route.

The user's explicit 2026-09-20 instruction retires the Field-Validated Planner trait and reward. Field validation remains a mission with its other outcomes. Full field validation, Reality Audit, and event cleanup remove Rulebook Commander without awarding a replacement trait.

## Identity and purpose

Event 24 is the unclustered Chaos level 1 Minor Fire-Once event `chaosx.nr24.1`.

It follows a Swedish campaign cabinet built from relay cabinets, projected maps, printed scenario sheets, and institutional habit.

The event is a finite program with an ordinary baseline and three named evolutions.

Baseline stages are phases of the event and are not evolution rows.

The package keeps the satire inside period institutions, staff procedures, public committees, newspapers, schools, factories, and ministries.

## Registration and host selection

The shared Chaos event registry owns the event id, type, level, fire-once behavior, event name, actor mapping, History row, Event Details row, and three evolution rows.

The normal fire path prepares one host before the event weight is evaluated.

The host priority is:

1. A living country with original tag SWE that owns and controls Stockholm, state 141.
2. A living country with original tag SWE that owns Stockholm.
3. The living original-tag SWE country with the greatest controlled share of the original Swedish core states.

An existing valid host is preserved during repeated checks so the program does not migrate merely because a second country becomes eligible.

The active host must retain original tag SWE, remain uncaptitulated, and keep a valid Swedish territorial foothold.

The category and all decisions are hidden when there is no valid current host.

The event log and details view use `N/A` for the actor when no valid principal Sweden is available.

The shared automatic pool records the no-host state as `video_game_in_sweden_host`, so the Events tab can show the localized `N/A` reason while preserving the fire-once history.

The shared dispatcher checks and records the permanent global fired-event history after the root is sent, while the root's pre-fire flag prevents a history-order race.

That combination prevents a second fire after civil war, annexation, release, puppeting, or tag change while preserving the fire-once record even when no valid host can currently be shown.

## Openings and public Reliance

The opening event has three player-facing routes.

| Opening | Event option | Starting Reliance | Initial public state | Institutional direction |
| --- | --- | ---: | --- | --- |
| Controlled staff trial | `chaosx.nr24.2.a` | 12 | Instrument | A cautious staff exercise with a narrow chain of responsibility. |
| Civilian commercial release | `chaosx.nr24.2.b` | 38 | Habit | A civilian market turns the cabinet into a respectable national pastime. |
| Competitive officer league | `chaosx.nr24.2.c` | 62 | Doctrine | Officers convert the tables into a professional contest with its own prestige. |

`Simulation Reliance` is the only visible numeric mechanic value and ranges from 0 to 100.

The four public states are Instrument at 0 to 24, Habit at 25 to 49, Doctrine at 50 to 74, and Worldview at 75 to 100.

Actions change the normal variable, and a scripted localisation entry renders both the value and its current state in the category header.

The staged idea lifecycle has exactly one active idea at a time.

| Lifecycle stage | Idea id | Meaning |
| --- | --- | --- |
| Experimental war game | `video_game_experimental_war_game` | The cabinet is a trial instrument. |
| Gamified staff culture | `video_game_gamified_staff_culture` | Repetition and ranking make the exercise part of staff culture. |
| National strategy craze | `video_game_national_strategy_craze` | Civilian institutions give the exercise broad social reach. |
| Simulation orthodoxy | `video_game_simulation_orthodoxy` | Offices begin treating the cabinet's categories as authoritative. |
| Validated wargaming methods | `video_game_validated_wargaming_methods` | A successful field test gives the method a bounded institutional place. |

The lifecycle is refreshed by removing the other four ideas before the selected stage is applied.

Civil-war retention is restricted to the selected active Swedish host, rather than copying the staged spirit to both sides.

The controlled opening at high Chaos may begin the staff evolution when the gate is met.

The officer opening at high Chaos may begin the staff evolution when the gate is met.

The commercial opening at high Chaos may begin the public evolution when the gate is met.

If the relevant evolution is disabled, the opening remains usable and its Reliance is capped at a safer public band instead of creating a crisis without a response.

## Baseline program

The baseline category presents four primary actions.

| Action | Decision id | Purpose | Cost family |
| --- | --- | --- | --- |
| Conduct a controlled exercise | `video_game_controlled_exercise` | Run a small staff exercise and build measured confidence. | Army experience, support equipment, fuel. |
| Add a logistics module | `video_game_logistics_module` | Test trains, trucks, support equipment, and factory time against the cabinet. | Trains, trucks, support equipment, civilian factory. |
| Expand public access | `video_game_expand_access` | Let civilian institutions handle a bounded version of the exercise. | Political power and army experience. |
| Conclude the trial | `video_game_conclude_trial` | Close the baseline program after review and record an ordinary conclusion. | No spendable cost. |

The baseline has a finite review window, a repeat cooldown, and an automatic close after the configured baseline lifetime.

The ordinary conclusion is available without entering any evolution.

Controlled exercises include a debrief using the shared confidence and debrief constants.
The first session reduces Reliance by one point and subsequent sessions by three points, while the staged program supplies the finite training benefit.
A competitive opening can move from 62 to 57 after the rail review and to 56, 53, 50, and 47 through four exercises, meeting the ordinary conclusion's below-Doctrine requirement without evolution.

The ordinary conclusion branches by opening and by the last useful institutional result, with separate political, military, cultural, and restrained outcomes.

The baseline can therefore finish as a complete low-scale event rather than requiring the player to chase a route escalation.

The same conclusion action closes a contained Evolution I or Evolution II, and report `chaosx.nr24.20` files a phase-specific outcome.
A contained staff culture is validated and retired (`.20.f`): army experience, Rulebook Commander removal and Validated Wargaming Methods for 120 days.
A contained national craze becomes a cultural institution (`.20.g`): political power and Municipal Campaign Clubs for 120 days.
Baseline trials keep their route outcomes (`.20.a` to `.20.c`).

## Programme package

One country dynamic modifier, `video_game_in_sweden_program_package` ("Campaign Cabinet Programme"), carries every finite action payoff and the Evolution II public costs.
`video_game_in_sweden_refresh_program_package` rebuilds its variables from the `video_game_in_sweden_package` constants after every Reliance change, after each action and once a day through the bounded runtime watch, which also counts down the timed payoffs.
The package is attached only while the programme runs outside restriction enforcement and recovery, and closure removes it, so no bonus outlives the programme.

| Source | Effect while active | Duration |
| --- | --- | --- |
| Controlled route | 3% faster army training | Programme |
| Commercial route | +5% factory efficiency growth | Programme |
| Officer route | +5% army experience gain | Programme |
| Controlled exercise | +3% planning speed and 5% faster training, halved by each repeat under the same war state down to a quarter | 90 days |
| Rail-table review | -5% supply consumption | 180 days |
| Rules revision | +3% maximum planning and -3% terrain adaptation each, up to three; field validation or a red team halves the adaptation cost | Programme |
| Officer league | +3% planning speed, +5% army experience gain | Programme |
| Competitive command culture | +3% planning speed, +5% army experience gain | Programme |
| Formal auxiliary doctrine | +2% planning speed, +2% terrain adaptation | Programme |
| Independent red team | +5% terrain adaptation, -2% planning speed | Programme |
| Full field validation | 8% faster army training | 180 days |
| Preparedness charter | +2% recruitable population | Programme |
| Foreign licence | +15% trade opinion | 180 days |
| Public exhibitions in Evolution II | +3% war support | Evolution II |

The rail-table review lowers Reliance on staff routes and raises it by 2 on the commercial route, where publishers market it as proof of realism.
A rules revision raises Reliance by 9, or by 3 once a field validation or red team has tested the rules, and an official auxiliary doctrine halves either gain.

### Evolution II public costs

While Evolution II runs, the package also carries a factory output cost and a political power gain cost, shown in the category header.
The output cost starts at 4% and the attention cost at 10%.
Both scale by route (controlled 0.75, officer 1.0, commercial 1.25), by Reliance state (Habit or lower 0.75, Doctrine 1.0, Worldview 1.25) and by the Evolution II choice (exhibitions 1.25, civic network 0.8).
Each national league season adds 1.5% to the output cost, for up to four seasons.
Protected shifts cut the output cost by 60%, a preparedness charter by 25%, and separating play from policy halves the attention cost and adds 90 days to the Evolution III delay.
The National Strategy Craze idea keeps its recruitment and war-support benefits.

## Decision category and mission contract

The program uses one normal event-owned decision category named `video_game_in_sweden_program_category`.

The category uses the static picture `GFX_decision_category_picture_024_video_game_in_sweden` and has no scripted GUI or custom mechanic window.

The category is visible only to the valid original-tag Swedish host while the program is active and not disabled.

Each phase keeps between three and five primary actions visible.

Only one active mission is permitted by the shared mission-state trigger.

The four mission definitions are `video_game_field_validation_mission`, `video_game_reality_audit_mission`, `video_game_dual_track_verification`, and `video_game_restriction_enforcement`.

Mission lengths are 120 days for field validation, 180 days for a full reality audit, 120 days for dual-track verification, and 90 days for restriction enforcement.

The narrow reality audit is a 90-day recovery mission and is only available after a partial or failed audit.

Full, partial, failed, timeout, cancellation, and disabled callbacks all clear the active mission state before applying their outcome.

Every spendable action uses no more than four cost types, and each cost is exposed through the decision's custom cost text and the correct resource texticon.

Routine maintenance advances the mission timer without cancelling a live mission.

Mission cancellation is reserved for explicit closure, recovery, or disabled-evolution cleanup.

## Evolution pacing

Each monthly maintenance adds 30 days times an MTTH pace (`common/mtth/024_video_game_in_sweden_mtth.txt`) to the progress of every evolution that is currently eligible, and an evolution fires when its progress reaches the base delay of 120, 150 or 120 days.
Progress toward Evolution II restarts at the staff-culture stage, and progress toward Evolution III starts at Evolution II, so Evolution III can never fire in the opening chain or on the same day as Evolution II.
All factors are `video_game_in_sweden_pace` constants.

| Evolution | Faster | Slower |
| --- | --- | --- |
| I | War 1.4, low army experience 1.25, officer route or league 1.4, a recent apparent prediction 1.2 | Controlled route 0.75, red team 0.7, field validation 0.6, an admitted mismatch in the last 90 days 0.75 |
| II | Commercial route 1.3, each of the first two league seasons 1.2, high war support under high tension 1.2, apparent prediction 1.2, foreign licences 1.15, a public officer league 1.2 | Protected shifts 0.7, separate policy 0.7, low stability 0.75, red team 0.8, auxiliary doctrine 0.85, field validation 0.8, admitted mismatch 0.8 |
| III | Officer competition 1.25, a state-backed league 1.2, no field validation 1.15, apparent prediction 1.2, Totalen Chaos 2.0 | Red team 0.7, protected shifts 0.8, admitted mismatch 0.75, and separate policy adds 90 days |

In source terms the scenario pairs order as required: P24-E1A paces at about 0.53 against 1.96 for P24-E1B, P24-E2A at about 0.64 against about 2.0 for P24-E2B, and P24-E3A at 0.7 with the 90-day separate-policy addition against about 4.1 for P24-E3B. Because progress is added monthly, real timings round up to whole 30-day steps.

## Evolution I: The Staff College Takes the Board

Evolution I requires Chaos at least 200, a valid early program route and 120 days of paced progress (see Evolution pacing).

Its event entry is `chaosx.nr24.11`.

The staff college turns the cabinet into professional culture through rankings, repeated scenarios, and a dispute over what the tables measure.

The evolution event offers three lasting choices.
Formal auxiliary doctrine (`chaosx.nr24.11.a`) caps Reliance at 55 and stops gains past that level while the staff culture lasts, with a small planning and adaptation package.
Competitive command culture (`.11.b`) raises Reliance by 11, gives the strongest planning and army-experience package and rolls the 35 percent Rulebook Commander chance.
Independent red-team supervision (`.11.c`) lowers Reliance by 10, files the red-team review, trades planning for adaptation and stops enemy-behaviour incidents.

The primary actions are:

- `video_game_rules_revision` revises the rulebook and raises Reliance.
- `video_game_field_validation` starts the field validation mission.
- `video_game_red_team` introduces a hostile review and lowers Reliance while improving adaptation.
- `video_game_officer_league` gives the officer corps a bounded competitive institution.

Field validation checks the configured Swedish front states, including southern state 138, central state 141, and northern state 666, along with the required front presence, committed field resources, and review conditions.

The field package requires Stockholm under Swedish control and at least two Swedish divisions in one selected field region, while the full reality audit requires at least two divisions in each of the three named regions.

A full result resolves the field-validation mission and removes the temporary Rulebook Commander trait from a valid Swedish commander.

A partial result preserves a useful but weaker staff method and leaves a temporary field-failure penalty.

A failed result reduces Reliance, applies a finite planning and reinforcement penalty, and leaves recovery through a later controlled exercise or another permitted route.

The commander carrier is never duplicated, and cleanup removes it when the host or program becomes invalid.

## Evolution II: The Nation Takes Its Turn

Evolution II requires Chaos at least 400, Doctrine Reliance, broad public reach and 150 days of paced progress from the staff-culture stage or a commercial baseline.

Its event entry is `chaosx.nr24.12`.

Clubs, schools, newspapers, and workplaces turn the Swedish cabinet into a public institution with military consequences.

The primary actions are:

- `video_game_national_league` expands the public league and raises Reliance with a finite administrative burden.
- `video_game_protect_shifts` protects factory shifts and labor schedules from the public program.
- `video_game_preparedness_clubs` turns the method into bounded civil preparedness.
- `video_game_foreign_licenses` sends up to three meaningful foreign responses through the separate foreign-response pool.
- `video_game_separate_policy` creates a clear political boundary between public simulation and state policy.

National league and preparedness actions carry finite burdens and cooldowns so the route is an institution with opportunity costs rather than a store of minor rewards.

The public route can resolve through expansion, protected production, preparedness, a foreign response, or a separate policy with distinct ordinary and incident outcomes.

## Evolution III: When the Board Directs the Cabinet

Evolution III requires Chaos at least 600, Worldview Reliance and 120 days of paced progress from Evolution II, plus 90 days when play is separated from policy.

Its event entry is `chaosx.nr24.13`.

Senior offices apply the cabinet's categories to transport, weather, production, diplomacy, and real operations.

The opening event keeps all four accepted response paths visible:

- `video_game_begin_reality_audit` tests the model against a full field package.
- `video_game_dual_track` runs the model beside ordinary planning.
- `video_game_restrict_use` imposes an enforceable boundary when stability and war support can absorb it.
- `video_game_trust_model` lets the cabinet direct a meaningful war under a bounded maximum-risk contract.

The maximum-risk route is unavailable during severe campaign instability, a supply gap, a surrender progress threshold of 0.75 or higher, or low stability.

This safety gate means high Chaos can make the opening more forceful without forcing an unanswerable final crisis.

### Reality audit

The full audit starts from the field package, a front presence, committed resources, Stockholm and the minimum audit Stability.
The rail-table review and independent red-team finding are proof inside the audit rather than start conditions.
While an audit runs, `video_game_advanced_logistics_review` and `video_game_independent_adjudicators` appear for whichever review is still missing, so a high-Chaos commercial opening that skipped Evolution I can still reach a full report.

It lasts 180 days with 120 days of proof and can end in full, partial, or failed validation.
Without both reviews the audit waits for its deadline and files a partial report.

Every result only lowers Reliance: full caps it at Habit, partial at Doctrine.
A partial result keeps Independent Staff Comparison for 120 days as a provisional comparison staff.
A failed result restores Simulation Orthodoxy, keeps the Reliance already shed, and applies Unresolved Field Findings for 120 days.
A partial or failed audit opens the narrow 90-day recovery audit when the host can afford its smaller package, and restriction stays available.

Full validation grants the validated-methods idea for a finite period and begins the Reality Check achievement timer.

### Dual track

Dual track tests the cabinet beside normal planning for 120 days with 90 days of proof.
Verification needs the comparison itself: `video_game_dual_track_independent_plans` (army experience and command power) has the conventional staff draw up its own plan, and `video_game_dual_track_resolve_differences` (political power and army experience, Reliance -4) settles each difference against field reports.
Success also needs Stockholm and no supply gap at the end of the proof period; without both comparisons the mission times out into failure, which leaves the Reality Audit and restriction as the final choice.
These two rows are the only actions shown during verification.

Its outcome preserves the ordinary chain of command while recording whether the model has earned a limited planning role.

Failure applies a finite supply and reinforcement penalty and leaves the host able to recover through ordinary review.

### Restrict use

Restriction lasts 90 days with 60 days of proof.

The action requires the stability and war-support gate shown in the tooltip.

Its enforcement can succeed with a controlled political loss or fail with a finite backlash that still leaves a recovery path.

### Trust the Model

Trust the Model costs the configured command power and political power, accepts a stability and war-support burden, and may begin before a qualifying war exists.

During the active surge the first qualifying war against a major or materially stronger opponent is stored in a country event target, and its military context is retained for the final result.

The trust surge lasts no longer than the 365-day reassessment limit.

Maintenance sends a warning before the deadline and opens mandatory reassessment at the configured limit.

Reassessment retains three concrete responses, reality audit, dual track, and restrict use.

If the opponent disappears or the war ceases to be meaningful, the trust path is disqualified and the temporary surge is removed.

The favorable result records a distinct completion flag for According to Plan and still requires the reassessment state.

## Incidents, disabled handling, and recovery

The maintenance hook runs only for the bounded Event 24 host path and advances the finite program every 30 days.

It checks for twelve incident families: terrain, supply, enemy action, template failure, diplomacy, workplace disruption, party or public pressure, casualties as counters, an unexpected counterplan, a foreign bootleg, production without transport and the perfect offensive.
Casualties as counters arises at war in Evolution III or at Worldview Reliance and costs war support and recruitable population.
The unexpected counterplan and the foreign bootleg are rare baseline and Evolution I incidents (weight 50) that share a 240-day cooldown, so a peaceful early programme still meets the occasional embarrassment.
Production without transport arises in Evolution III in peace or war and costs factory efficiency growth and supply, and the perfect offensive arises in Evolution III at war and costs attack and maximum planning.
Entering Evolution III queues one opening incident five days after the evolution report, chosen by the campaign: production without transport always qualifies, a diplomatic category error needs a faction, overlord, war or licence business, and the perfect offensive or casualties as counters need a war.

Only currently valid families enter the weighted incident pool. The pool avoids the last family when another valid family exists and starts a new family cycle after all valid families have appeared.

After the 45-day cooldown (20 days during Trust the Model) a due incident fires on a maintenance check with a 60% base chance.
The chance is multiplied by Reliance state (Instrument 0.6, Habit 0.85, Doctrine 1.0, Worldview 1.25), an officer league or competitive culture (1.25), auxiliary doctrine, a red team and field validation (0.8 each) and an active Trust the Model surge (1.25), clamped between 10 and 100%.
Incidents pause during a severe crisis, restriction enforcement and recovery.

Family weights live in `video_game_in_sweden_incident`.
Supply mismatches weigh twice the other families, terrain falls to a quarter after a successful field validation, enemy-behaviour reports rise with competitive culture, template reports rise with officer competition and a dismissed template report and fall after restriction, workplace reports rise by a quarter per national league season and fall to a quarter with protected shifts, and party reports rise with exhibitions or appropriation and halve with preparedness, a civic network or separate policy.

Every response applies the timed Cabinet Mismatch modifier (`video_game_in_sweden_mismatch_penalty`), priced when the incident is drawn so the report shows the exact cost of each answer.
Severity is the Reliance-state factor (0.5 to 1.5) times war (1.5), Chaos 600 or higher (1.25), a prior relevant validation (0.75) and one tenth more per earlier mismatch up to half again, capped at 2.5.
Admitting the error halves the penalty and its duration, and dismissing it pays in full; the penalty lasts 30 to 90 days.

| Family | Penalty lines |
| --- | --- |
| Terrain | Army attack and army speed |
| Supply | Supply consumption and organisation recovery |
| Enemy behaviour | Planning speed and maximum planning |
| Template | Faster training now, weaker terrain adaptation |
| Diplomatic | Political power gain and monthly opinion gain |
| Workplace | Factory output |
| Party | Stability and political power gain |

Admitting answers also lower Reliance and may file a review, protect shifts, separate play from policy or close the licence office, while dismissing answers raise Reliance and make that family more common.

When an evolution becomes disabled, the handler cancels the active mission, removes temporary route ideas and modifiers, clears transient targets, and returns to the last permitted phase or baseline.

The handler also applies the safer fallback when Chaos falls below a route gate after a high-Chaos opening.

Normal closure removes the category state, active ideas, temporary modifiers, mission flags, commander traits, and event targets while preserving fire-once history and achievement records.

### Crisis memory and mission interruptions

The capital-threat and core-loss crisis flags describe the current campaign rather than permanent history.
Daily observation rebuilds them from Stockholm ownership and control, any owned Swedish core held by another controller, and a finite memory of the last loss lasting `video_game_in_sweden_timing.crisis_memory_days` (60) days.
Once the territory is back and the memory has passed, severe-crisis checks, the incident pause and the Trust the Model gate return to normal.
Each field validation, Reality Audit, narrow audit and Dual-Track verification keeps its own interruption record, reset when the mission starts.
One Swedish core lost during the mission limits the report to a partial result, while Stockholm or two lost cores cancel the mission into its failure result.
Stockholm loss still permanently disqualifies the two achievements.

### Trust the Model mismatches

A wartime terrain, supply or enemy incident resolved during the surge is a battlefield mismatch.
Admitting it ends the surge at the next daily review, and three dismissed battlefield mismatches in the same surge do the same.
Incidents from before the surge never shorten it.

### National Final

The second national league season schedules `chaosx.nr24.35`, a national final 30 days later, once per programme.
The official favourite (weight 60, raised by half under state exhibitions) raises Reliance by 6 and adds 2% war support.
An outsider's upset (weight 40, raised by half with a red team and by a quarter with civic clubs or a preparedness charter) lowers Reliance by 8 and grants 15 political power.

### Evolution II reach gate

Every path into Evolution II requires broad public reach, including the step from Evolution I.
An officer or controlled programme that never widened civilian access stays in Evolution I and can conclude there.

## Commander lifecycle

The Rulebook Commander is a rare result of competitive command culture, not a guaranteed reward.
The officer opening rolls a 20 percent chance, the competitive command culture option of `chaosx.nr24.11` rolls 35 percent, and a formal officer league rolls 25 percent, each from `video_game_in_sweden_award` constants.
At most one commander is marked per programme, and the roll is skipped when no serving army commander leads troops.

The trait is a land personality trait following the vanilla `war_hero` pattern, with `new_commander_weight` at zero, so it never appears in a trait tree and is never rolled for new leaders.

The selection prefers an active Swedish field marshal and then an active Swedish general.

The trait is not created as a new leader.

Successful field validation removes the temporary trait; it does not award a replacement commander trait.

If no valid commander remains, or if the program is disabled or closed, the trait is removed cleanly.

## Foreign response pool

Foreign Licenses selects from a bounded set of meaningful foreign partners.

The pool accepts no more than three countries across the program and requires a living country with diplomatic, geographic, market, faction, or subject relevance.

Each selected partner receives one response event and one temporary opinion or institutional modifier.

The public response choices are copy, study, ban, ridicule, and no action.

The host receives no more than two visible foreign reports unless a human foreign office makes the choice directly, while the total validated response pool remains capped at three.

Foreign countries do not receive Sweden's decision category, Reliance variable, staged ideas, missions, or evolution chain.

The foreign response is dispatched after the configured delay and rechecks the host, partner, pending flag, war state, and capitulation state before opening. The host receives a compact report event after the foreign response is resolved.

## AI and safety contract

Opening AI is route-specific and uses the campaign factors in `video_game_in_sweden_ai`.

Opening factors distinguish peace, war, stability, Chaos, public crisis, and the disabled-safe case.

Every baseline, evolution, recovery, foreign, and conclusion action has route-specific factors in `video_game_in_sweden_ai_route`.

Near capitulation, broken supply, and severe instability suppress the maximum-risk route and favor controlled handling or restriction.

The named probability scenarios are `P24-O1` through `P24-O4` in `P24_FINAL_OPENING_MATRIX`.

The four scenarios cover a peaceful stable staff opening, a peaceful public opening, a wartime officer opening, and a severe emergency with supply and core-loss flags.

The live HOI4 probability inspection resolved the three-option opening pool with no unresolved inputs.

The named four-scenario evaluation produced bounded matrix evidence and reported 12 unresolved external or adapter inputs, so it is not presented as an exact normalized probability claim.

The emergency source state makes controlled handling dominant and sets the commercial opening factor to zero, which is an intentional safety result rather than a hidden forced crisis.

A bounded sweep across Chaos, stability, surrender progress, and army experience covers six additional safety points and preserves the same explicit uncertainty. The current-source control comparison reports zero comparison changes under the identical named matrix.

## Achievements and persistence

`024_video_game_in_sweden_reality_check` requires Evolution III, a full reality audit, the 365-day validated-methods timer, Stockholm held, low Reliance, valid host status, and no disqualifier.

`024_video_game_in_sweden_according_to_plan` requires Evolution III, Trust Model, a meaningful favorable war result, mandatory reassessment, the stored opponent and victory state, Stockholm held, valid host status, and no disqualifier.

Loss of host validity, supply failure, failed war conditions, severe instability, or the relevant route failure sets the persistent disqualifier flags.

Achievement tracking is updated by bounded maintenance, daily observation, and outcome effects, with proof stored in country flags and variables.
Native save-persistence acceptance remains outstanding.

Hidden event `chaosx.nr24.91` observes the selected host daily without a world-wide periodic on-action.
State-control callbacks record Stockholm and core losses at the transaction, while capitulation and annexation callbacks verify that their country owns the saved host context before cleanup.
Mission elapsed time advances daily, and resource or regional interruption receipts remain sticky.
Source regressions cover this contract, while native callback delivery and save persistence remain unverified.

Both achievements have complete, grey, and not-eligible DDS states registered in `interface/chaosx_achievements.gfx`.

Reality Check accepts its low-Reliance proof on day 365 and rejects either loss of Stockholm ownership or control.
Closed receipts and finite ordinary aftermath survive late queued maintenance and repeated cleanup calls.
Commander cleanup follows the stored commander target as well as the host's current officers, including a commander transferred away from the host.

Restriction remains financially available during collapse.
Its political power, Stability and War Support charges are each the lesser of the nominal fee and the current nonnegative reserve, using the installed dynamic readers.
Localisation shows that quote, and payment recomputes all three amounts together before debiting them.
The fixed political-power AI budget hint is absent from this variable-fee action, while its route and crisis willingness factors remain unchanged.

The Trust the Model surge increases supply consumption by eight percent, alongside its planning benefit and recovery risks.

Restriction closes official leagues, removes score-based policy authority, and withdraws state-supported public facilities through distinct departmental receipts.
The existing sixty-day proof period yields receipts at days twenty, forty, and sixty within the existing ninety-day mission.
Its completion closes the category without granting Validated Wargaming Methods.
Only a ninety-day Stability backlash remains, carried by an iconless finite modifier.
The closed host can still receive its final restriction report, and late callbacks cannot renew the result.

Native civilian-office reservations use their actual action terms.
Foreign licensing and establishment of the second ledger reserve an office for thirty days, separately from reply delivery and mission verification.
National seasons begin with forty-five days and increase later reservations to sixty, seventy-five, then ninety days.
Full and narrow audit rows select their respective regional and proof-period descriptions through one flag-based localisation getter.

## Asset inventory and wiring

The active custom inventory contains 31 DDS files: four staged-idea textures, one idea-family texture for the finite foreign Copy and Study modifiers, 17 decision/action textures, one Rulebook Commander texture, six achievement states, one report picture, and one static category picture.
The experimental spirit uses installed vanilla `SWE_wargames`, and the normal category uses the installed vanilla generic crisis icon.
The custom experimental icon remains wired to the two foreign modifiers, so the earlier 30-file reconciliation is superseded for counts.

The parent replaced 25 stale DDS files from the reviewed source package and reopened all 31 final custom DDS files individually at native size, alongside the two shared vanilla textures.
Every custom decoded output equals its processed PNG exactly.
The selected source lineage, exhaustive consumer-to-sprite-to-file table, final paths, sizes, alpha treatment, repairs, and current review evidence are in [the current asset audit](assets_visual_audit_2026-10-03.md).
The current contact sheets include source art, native previews, smooth enlargements, and decoded DDS output.
The complete source workspace remains retained while the event's gameplay and probability work is incomplete.

The unreachable legacy `chaosx.news.24` definition, its modern-logo sprite and unused localisation were retired, and the original DDS was archived as historical evidence with its checksum preserved.
No replacement news-art family was introduced.
Field-Validated Planner and its texture remain retired under the accepted 2026-09-20 decision.

The full and narrow Reality Audit actions share their exact action symbol, and each of the four timed objectives consumes the corresponding start action's unchanged sprite.
The asset prompt authorizes no separate custom mission-art family.
The event introduces no dedicated scripted GUI; the static category picture is presentation in the ordinary decision category.
The standard-category MCP route returned a missing-window render, which remains an explicit evidence limit rather than visual clearance for the decision row layout.

## Implemented surfaces and future depth

Gameplay is implemented in the Event 24 event, decision, scripted effect, scripted trigger, constant, dynamic modifier, idea, trait, opinion, and scripted localisation files.

Shared registration is implemented in the Chaos settings, event log, event details, achievement, localisation, and interface registration files.

The package-owned CXT extension registers an inert hidden carrier through one bounded startup scope and a tag-scoped daily registration fallback. When the daily fallback finds new content, it sets the shared pending-sync flag and does not apply the fixture. The fixture exposes only readiness and public Reliance bounds when setup or the player-triggered apply control consumes it, so CXT does not fire Event24 or receive Sweden-specific gameplay state.

The authoritative Event Catalog workbook contains the last aligned Event Details and three evolution title and body pairs, is marked Needs Testing, and retains the unclustered Minor Fire-Once metadata.
Final catalogue alignment remains queued until the full in-game wording and implementation are finished.

The exporter regenerates the three CSV snapshots after the workbook update.

Future depth can add more period-specific staff personalities, additional Swedish front templates, and more foreign institutional histories while preserving the one-host, one-mission, one-idea, finite-program contract.
