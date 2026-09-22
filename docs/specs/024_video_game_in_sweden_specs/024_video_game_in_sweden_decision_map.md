# Event 24 Decision Map

All labels in this file are working implementation labels. Final player-facing text must be written from the direction in the specification.

## State flow

```text
Entry event
  -> Controlled Staff Trial
  -> Civilian Commercial Release
  -> Competitive Officer League

Baseline program
  -> ordinary conclusion
  -> Evolution I at Gathering Storm

Evolution I
  -> validated officer culture conclusion
  -> Evolution II at Rising Chaos

Evolution II
  -> contained public-culture conclusion
  -> Evolution III at Chaos Tier

Evolution III
  -> Reality Audit
  -> Dual-Track Staff System
  -> Restrict Official and Public Use
  -> Trust the Model
       -> mandatory reassessment
       -> one of the three recovery routes
```

## Primary visible value

Working variable: `simulation_reliance`

| State | Range | Category display role |
| --- | --- | --- |
| Instrument | 0 to 24 | Low-risk tool |
| Habit | 25 to 49 | Default staff method |
| Doctrine | 50 to 74 | Institutional authority |
| Worldview | 75 to 100 | Crisis state |

Every action shows its expected Reliance direction. Exact movement should use centralized tuning and may scale by current stage.

## Baseline route setup

| Working action | Route effect | Starting Reliance direction | Immediate benefit direction | Main later risk |
| --- | --- | --- | --- | --- |
| Controlled Staff Trial | Military-only, debrief required | Low | Small army experience and planning | Low evolution pressure |
| Civilian Commercial Release | Public clubs and commercial distribution | Medium | Public interest and modest cultural value | Faster Evolution II and productivity pressure |
| Competitive Officer League | Formal staff competitions | High | Strongest early military value | Faster Evolution I and commander overreliance |

## Baseline phase

| Working id | Visible when | Costs, maximum four | Requirements | Immediate result | Longer result | Cooldown or limit |
| --- | --- | --- | --- | --- | --- | --- |
| `video_game_controlled_exercise` | Program active before Evolution I | Army XP, support equipment, optional fuel variant | Valid Sweden, usable army | Temporary planning or training value | Can lower Reliance after debrief, repeated use has diminishing returns | Medium cooldown |
| `video_game_logistics_module` | Program active before Evolution II, module not finished | Trains, trucks or support equipment, civilian factory burden | Valid stockpiles | Reduces current supply risk | Lowers future supply-mismatch weight, can reveal model weakness | One main completion, later upgrade only |
| `video_game_expand_access` | Route has not reached its selected user base | Political power or civilian factory burden, route-specific army XP | Route remains valid | Opens officer or public content | Raises Reliance and relevant evolution pressure | Fire once per access tier |
| `video_game_conclude_trial` | Minimum review period passed, Reliance below Doctrine, no mission active | None | Program stable | Removes category and current idea | Finite route-sensitive aftermath | Fire once |

Baseline visible count: normally four.

## Evolution I phase

| Working id | Costs | Requirements | Reliance effect | Main benefit | Main risk | AI preference |
| --- | --- | --- | --- | --- | --- | --- |
| `video_game_rules_revision` | Army XP, command power | Cooldown clear | Increase unless based on validation evidence | Upgrades one planning or doctrine aspect | Higher mismatch pressure and escalating staff cost | Officer league, war, good supply |
| `video_game_field_validation` | Fuel, support equipment, trains, army XP | Divisions and supplied training regions | Decrease on success | Removes or reduces one mismatch family | Mission failure and committed resources | Strong after losses or supply problems |
| `video_game_red_team` | Political power, army XP, optional civilian burden | No active equivalent | Decrease | Better enemy variation and lower overconfidence | Smaller immediate planning benefit | Democratic, cautious, stronger enemy |
| `video_game_officer_league` | Command power, army XP | League not formalized | Increase | Army experience, planning, rare commander-trait chance | Faster evolution and over-standardization | Militarized, low army XP, good supply |

Evolution I visible count: four plus one active mission row when validation is running.

## Field-validation mission

Working id: `video_game_field_validation_mission`

Duration band: 90 to 120 days.

Objective package:

- Maintain the required supplied divisions in the selected Swedish training regions or stable active fronts.
- Retain Stockholm.
- Keep committed trains, fuel, and support equipment available.
- Complete one red-team or logistics review before expiry.

Results:

| Result | Conditions | Reliance result | Other result |
| --- | --- | --- | --- |
| Full success | All objectives maintained | Strong decrease | Correct trait when present, reduce two mismatch weights, finite training benefit |
| Partial success | Main field package maintained, one review or supply condition missed | Moderate decrease | Reduce one mismatch weight, open targeted follow-up |
| Failure | Core objective abandoned or major territory loss | Small decrease or no change | Timed military penalty, cheaper restriction, later re-audit allowed |

The mission auto-completes. No second payment click.

## Evolution II phase

| Working id | Costs | Requirements | Reliance effect | Main benefit | Main cost or risk | AI preference |
| --- | --- | --- | --- | --- | --- | --- |
| `video_game_national_league` | Civilian factory burden, political power | Adequate stability and industry | Strong increase | War support, recruitment interest, public milestone | Productivity pressure, foreign visibility | High tension, strong industry |
| `video_game_protect_shifts` | Political power, small civilian burden | Workplace league active | Decrease | Removes or reduces factory penalty | Lower public benefit and reach | War production pressure |
| `video_game_preparedness_clubs` | Political power, support equipment or trucks | Public network active | Small increase or neutral | Practical civil and recruitment benefit | Lower cultural popularity than league route | Democratic high-tension Sweden |
| `video_game_foreign_licenses` | Convoys, civilian factory burden, political power | Valid partners and route access | Increase | Commercial and diplomatic value, foreign reactions | Leak and foreign adoption risk | Friendly partners, spare convoys |
| `video_game_separate_policy` | Political power, possible stability or war-support cost | Public obsession active | Strong decrease | Retains reduced cultural value, delays Evolution III | Political backlash | Stable democracy, mismatch history |

Evolution II visible count: no more than five.

## Foreign license target flow

The player should not see one decision per country.

Use a bounded target selection flow:

1. Build a valid partner pool from living Nordic neighbors, allies, major powers, overlord, and important trade partners.
2. Exclude countries already targeted, inaccessible partners, active enemies when licensing is impossible, and countries whose response cannot produce a meaningful result.
3. Present one selected partner at a time or one action that chooses from a short curated list.
4. Record the partner and response so it cannot repeat.
5. Stop after three meaningful foreign responses.

AI foreign countries may resolve silently. Human countries receive a response event.

## Evolution III initial phase

Only these four choices appear:

| Working id | Costs | Immediate state | Follow-up |
| --- | --- | --- | --- |
| `video_game_begin_reality_audit` | Army XP, support equipment, fuel, trains | Orthodoxy benefits suspended, audit begins | Reality Audit mission |
| `video_game_dual_track` | Army XP, command power, civilian factory burden | Reliance lowered to Doctrine | Verification mission and finite dual-track outcome |
| `video_game_restrict_use` | Stability, war support, optional political power | Reliance falls rapidly, benefits removed | Short enforcement period, category closes |
| `video_game_trust_model` | Command power, political power, war support or stability | Reliance set to maximum, surge begins | War-sensitive incidents and mandatory reassessment |

## Reality Audit mission

Working id: `video_game_reality_audit_mission`

Duration band: 120 to 180 days.

Required proof:

- Supplied divisions across southern, central, and northern Swedish conditions or equivalent active fronts.
- Stockholm retained.
- At least one logistics review.
- At least one independent red-team result.
- No abandonment of the committed resource package.

Results:

| Result | Reliance | Idea lifecycle | Trait | Event state |
| --- | --- | --- | --- | --- |
| Full success | Falls to Habit | Validated Wargaming Methods | Converts mixed trait when present | Finite aftermath, then closure |
| Partial success | Falls to Doctrine | Provisional dual-track form | Can reduce penalty | One follow-up review |
| Failure | Remains Doctrine or low Worldview | Orthodoxy weakened but unresolved | No automatic correction | Restriction and narrower re-audit remain available |

## Dual-track verification

Working mission: `video_game_dual_track_verification`

Duration band: 90 to 120 days.

Purpose:

Prove that the conventional planning staff and simulation staff can produce independent plans, compare assumptions, and resolve differences.

Success:

- Reliance capped below Worldview.
- Severe mismatch pool removed.
- Finite validated idea granted.
- Category closes after the review.

Failure:

- Reliance remains high Doctrine.
- One final choice between Reality Audit and restriction.

## Restriction enforcement

Working mission: `video_game_restriction_enforcement`

Duration band: 60 to 90 days.

Purpose:

Close official leagues, remove the game from policy meetings, and end state-supported public facilities.

Success:

- Reliance returns to Instrument.
- All Event 24 benefits and penalties end.
- Short backlash expires.
- Category closes.

The mission should fail only if the principal Swedish host disappears or the system is invalid. It is the emergency resolution path.

## Trust the Model surge

Working timed state: `video_game_model_surge`

Maximum duration: no more than one year.

During surge:

- Strong planning and army-experience benefits.
- Strong supply, adaptability, recovery, political-attention, or stability risks.
- Increased weight for a campaign-relevant mismatch incident.
- Achievement tracking for a meaningful war.

Early reassessment triggers:

- Stockholm threatened or lost.
- New Swedish core lost.
- Severe supply failure.
- Major mismatch incident.
- War ends.
- Player voluntarily requests review.

The surge cannot be restarted.

## Reliance movement direction

Exact values are tuning constants. Relative movement should follow this order:

| Action family | Typical movement |
| --- | --- |
| Conclude, restriction, full Reality Audit | Very large decrease or closure |
| Field validation, red team, separate policy | Medium decrease |
| Controlled exercise with debrief | Small decrease or neutral |
| Logistics module | Small decrease when it exposes flaws, small increase when marketed as proof |
| Rules revision | Medium increase without validation, small increase with validation evidence |
| Expand access, officer league | Medium increase |
| National league, repeated public success | Large increase |
| Trust the Model | Set to maximum |

No single ordinary repeatable action should move from Instrument to Worldview.

## Incident pool map

| Incident family | Preconditions | Common effect surface | Reliance consequence | Resolution action |
| --- | --- | --- | --- | --- |
| Terrain mismatch | War or field exercise, no recent terrain validation | Movement, attack, planning, or training | Decrease if admitted, increase if rules are rewritten to dismiss it | Field validation |
| Supply mismatch | Train, fuel, truck, port, or supply pressure | Supply consumption, organization recovery, production | Decrease if logistics module accepted | Logistics review |
| Enemy adaptation | Repeated preferred scenario, weak red team | Planning, initiative, reinforce, temporary command penalty | Decrease if red team empowered | Independent red team |
| Standardized template | Officer league, high Reliance | Training ease and short planning benefit, later adaptability cost | Usually increase first, decrease after failure | Field exercise |
| Diplomatic category error | Evolution III, active diplomacy | Opinion, political power, temporary diplomatic penalty | Decrease if officials admit uncertainty | Reality Audit or dual-track |
| Workplace distraction | Evolution II, national league | Factory output or production efficiency | Decrease through shift protection | Protect essential shifts |
| Party appropriation | Evolution II, high public reach | Stability, political power, ideology-specific flavor | Route-dependent | Separate play from policy |

Each family should have cooldown and prior-occurrence memory. The event should prefer a new relevant family before repeating one.

## Closure cleanup checklist

On any final closure:

- Remove the Event 24 decision category and all active decisions.
- Cancel or resolve active Event 24 missions.
- Remove the current staged idea and any obsolete route ideas.
- Clear temporary foreign selection targets.
- Clear incident scheduling flags and cooldowns that no longer matter.
- Preserve the permanent fired record, evolution history, and achievement proof already earned; remove the temporary Rulebook Commander trait during normal closure. The user's 2026-09-20 instruction retired the former Field-Validated Planner survivor reward.
- Start only the stated finite aftermath modifier.
- Prevent re-entry from a later released Sweden or civil-war splinter.
