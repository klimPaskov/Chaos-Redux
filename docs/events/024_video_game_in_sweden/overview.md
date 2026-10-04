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

## Evolution I: The Staff College Takes the Board

Evolution I requires Chaos at least 200, a 120-day delay, and a valid early program route.

Its event entry is `chaosx.nr24.11`.

The staff college turns the cabinet into professional culture through rankings, repeated scenarios, and a dispute over what the tables measure.

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

Evolution II requires Chaos at least 400, a 150-day delay, and a valid public route.

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

Evolution III requires Chaos at least 600, a 120-day delay, and the prior route conditions.

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

The full audit requires the field package, a front presence, committed resources, a completed logistics review, and an independent red-team finding.

It lasts 180 days with 120 days of proof and can end in full, partial, or failed validation.

A partial or failed audit opens the narrow 90-day recovery audit when the host can afford its smaller package.

Full validation grants the validated-methods idea for a finite period and begins the Reality Check achievement timer.

### Dual track

Dual track tests the cabinet beside normal planning for 120 days with 90 days of proof.

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

It checks for seven incident families: terrain, supply, enemy action, template failure, diplomacy, workplace disruption, and party or public pressure.

Only currently valid families enter the weighted incident pool. The pool avoids the last family when another valid family exists and starts a new family cycle after all valid families have appeared.

Each incident has a concrete response pair or response set, a 45-day incident cooldown, and a route-aware recovery effect.

Trust Model uses a shorter 20-day incident cooldown while its special campaign is active.

Incidents can record overconfidence, lower Reliance, cancel a compromised mission, or open a recovery action without creating an irreversible crisis.

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

### Evolution II reach gate

Every path into Evolution II requires broad public reach, including the step from Evolution I.
An officer or controlled programme that never widened civilian access stays in Evolution I and can conclude there.

## Commander lifecycle

The Rulebook Commander is assigned to at most one valid Swedish corps commander.

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
