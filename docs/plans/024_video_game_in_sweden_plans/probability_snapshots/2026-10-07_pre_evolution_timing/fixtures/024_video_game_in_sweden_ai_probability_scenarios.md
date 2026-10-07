# Event 24 AI and Probability Scenarios

This file defines the later `chaosx_ai_probability_auditor` pass. It does not claim exact probabilities. Exact results require the complete implemented candidate pool, all modifiers, and the HOI4 MCP probability tools.

## Required workflow

For every weighted surface:

1. Run `hoi4.probability_inspect` first.
2. Confirm the complete option or candidate pool.
3. Declare external factors and scheduled state changes.
4. Use `hoi4.probability_evaluate` for named static scenarios.
5. Use `hoi4.probability_sweep` for Reliance, Chaos, supply, and stability boundaries.
6. Use `hoi4.probability_simulate` only where repeated random selection or MTTH sampling needs empirical evidence.
7. Use `hoi4.probability_compare` after any weight patch, using the same scenario ids.
8. Use `hoi4.probability_render` when a matrix, timing view, or sensitivity chart improves review.

Do not present a normalized exact probability when the pool or external state is incomplete.

## Opening option scenarios

### P24-O1: Calm democratic peace

State:

- Democratic or neutral Sweden.
- At peace.
- High stability.
- Adequate army experience.
- No supply shortage.
- Calm World.

Expected ordering:

1. Controlled Staff Trial.
2. Civilian Commercial Release.
3. Competitive Officer League.

Acceptance:

Controlled must be clearly dominant without making the other two impossible.

### P24-O2: Calm democratic rearmament

State:

- Democratic Sweden.
- At peace.
- High world tension.
- Low army experience.
- Good industry and supply.

Expected ordering:

1. Controlled Staff Trial or Civilian Commercial Release, close enough to vary.
2. Competitive Officer League remains plausible but below the safer routes.

Acceptance:

No route should exceed the others so heavily that campaign variation disappears.

### P24-O3: Militarized Sweden at war

State:

- Fascist, military, or strongly authoritarian Sweden.
- At war.
- Low army experience.
- Good supply, fuel, and trains.
- Gathering Storm or higher.

Expected ordering:

1. Competitive Officer League.
2. Controlled Staff Trial.
3. Civilian Commercial Release.

Acceptance:

Officer League should dominate, while Controlled remains a credible fallback.

### P24-O4: Emergency defense

State:

- Any ideology.
- At war.
- Recent core loss.
- Poor supply and low fuel.
- Low stability.

Expected ordering:

1. Controlled Staff Trial.
2. Competitive Officer League at low probability.
3. Civilian Commercial Release near zero or invalid.

Acceptance:

The AI must not choose a costly public launch during collapse.

## Evolution MTTH scenarios

### P24-E1A: Evolution I controlled program

State:

- Gathering Storm.
- Reliance 30.
- Controlled route.
- One successful exercise.
- Red team active.
- At peace.

Expectation:

Evolution I remains possible but slow. Median timing should be clearly longer than the base target.

### P24-E1B: Evolution I officer league

State:

- Gathering Storm.
- Reliance 45.
- Officer League formalized.
- Sweden at war.
- No field validation.

Expectation:

Evolution I occurs materially faster than P24-E1A.

### P24-E2A: Public craze contained

State:

- Rising Chaos.
- Reliance 55.
- Commercial route.
- Essential shifts protected.
- Play separated from policy.
- High stability.

Expectation:

Evolution II remains possible but slower than base.

### P24-E2B: National league expansion

State:

- Rising Chaos.
- Reliance 65.
- Two league seasons.
- Foreign licensing active.
- High world tension.

Expectation:

Evolution II occurs faster than P24-E2A and faster than the base target.

### P24-E3A: High reliance with safeguards

State:

- Chaos Tier.
- Reliance 78.
- Red team active.
- Recent field validation success.
- Play separated from policy.

Expectation:

Evolution III remains eligible but slower. Safeguards must have a visible effect.

### P24-E3B: Simulation orthodoxy pressure

State:

- Chaos Tier or Totalen Chaos.
- Reliance 90.
- Officer league and national league active.
- No recent validation.
- Several apparent prediction successes.

Expectation:

Evolution III occurs much faster than P24-E3A, but not in the same day as Evolution II.

## Evolution option scenarios

### P24-C1: Evolution I, stable democracy

Expected ordering:

1. Formal auxiliary doctrine or Independent red-team supervision.
2. Competitive command culture.

### P24-C2: Evolution I, militarized wartime Sweden

Expected ordering:

1. Competitive command culture.
2. Formal auxiliary doctrine.
3. Independent red-team supervision.

The red-team option remains possible after a recent mismatch.

### P24-C3: Evolution II, strong industry and high tension

Expected ordering:

1. Channel clubs into preparedness or Let the national league flourish.
2. Keep the craze outside government.

Route and ideology decide the top option.

### P24-C4: Evolution II, factory and stability crisis

Expected ordering:

1. Keep the craze outside government.
2. Channel clubs into preparedness.
3. Let the national league flourish near zero.

### P24-C5: Evolution III after supply failure

State:

- Severe supply shortage.
- Recent lost core.
- Low fuel or trains.

Expected ordering:

1. Reality Audit.
2. Restrict Official and Public Use.
3. Dual-Track Staff System.
4. Trust the Model invalid or near zero.

### P24-C6: Evolution III, stable high-Chaos militarized Sweden

State:

- High stability.
- Strong supply.
- Active offensive war goal.
- No recent core loss.
- Totalen Chaos.

Expected ordering:

1. Trust the Model or Dual-Track Staff System, depending ideology and risk profile.
2. Reality Audit.
3. Restriction.

Trust the Model must be plausible, not automatic.

### P24-C7: Near capitulation

Expected ordering:

1. Restrict Official and Public Use.
2. Reality Audit only when resources and territory make it feasible.
3. Dual-track low.
4. Trust the Model invalid.

## Decision AI scenarios

### P24-D1: Logistics action under train shortage

Compare Commission a Logistics Module and other baseline actions.

Expectation:

The logistics action becomes the top non-conclusion action when train and supply conditions are poor, provided Sweden can afford the minimum package.

### P24-D2: Field validation after mismatch

Expectation:

Field Validation gains a strong preference after a mismatch incident, recent failed offensive, or severe supply penalty. It must still be invalid when Sweden cannot field or supply the required divisions.

### P24-D3: National league during total mobilization

Expectation:

Protect Essential Shifts should outrank National League Season when factory output and war production are under severe pressure.

### P24-D4: Foreign licensing while blockaded

Expectation:

Foreign licensing is invalid without usable convoy access or valid partners.

### P24-D5: Conclude ignored baseline

State:

- Minimum review passed.
- Reliance below 50.
- At peace.
- Adequate army experience.
- No immediate evolution pressure.

Expectation:

Conclude the Trial becomes the dominant action. AI must not maintain a low-value category forever.

## Foreign response scenarios

Candidate pool:

- Copy.
- Study.
- Ban.
- Ridicule.
- Ignore.

### P24-F1: Friendly Nordic neighbor

Expectation:

Copy and Study lead. Ignore remains possible. Ban and Ridicule are low.

### P24-F2: Hostile major intelligence power

Expectation:

Study leads. Ban or Ridicule may follow depending ideology and world tension. Copy is low unless the country has low army experience.

### P24-F3: Authoritarian unstable state

Expectation:

Ban leads when public distribution threatens internal control. Study remains plausible through military channels.

### P24-F4: Peacetime complacent rival

Expectation:

Ridicule and Ignore lead. A prior Swedish military victory should sharply reduce Ridicule.

### P24-F5: Invalid or exhausted pool

Expectation:

Ignore or no-action resolves safely. The system must not target a dead country, repeat a partner, or exceed the three-response cap.

## Incident-selection scenarios

Candidate pool must include only incidents that are valid in the current campaign.

### P24-I1: War in mountainous or forested terrain

Expectation:

Terrain mismatch gains weight when no recent terrain validation exists. It should fall sharply after a successful relevant field exercise.

### P24-I2: Train and fuel shortage

Expectation:

Supply mismatch dominates. Diplomatic and workplace incidents remain secondary.

### P24-I3: Evolution II at peace with national league

Expectation:

Workplace distraction and party appropriation lead. Combat mismatch incidents are invalid or low.

### P24-I4: Evolution III during active diplomacy

Expectation:

Diplomatic category error becomes plausible when Sweden is pursuing guarantees, faction entry, licensing, or negotiations. It should not fire without a meaningful foreign target.

### P24-I5: Repetition control

State:

- One incident family fired recently.

Expectation:

A different valid family is preferred until cooldown or campaign change. The system should not repeat the same incident on consecutive checks without a narrow reason.

## Required sensitivity sweeps

Run sweeps across:

- Reliance from 0 to 100 at every threshold.
- Chaos from 0 to 1,000, with attention to 199, 200, 399, 400, 599, 600, 799, and 800.
- Stability from crisis to high stability.
- Supply, train, fuel, and convoy availability.
- Army experience from very low to high.
- Peace, offensive war, defensive war, and near capitulation.
- Democratic, communist, fascist, and non-aligned routes.
- Evolution enabled and disabled states.

## Required compare pass

Any patch to option weights, MTTH modifiers, incident random lists, foreign response weights, or decision `ai_will_do` requires:

1. Baseline scenario evidence.
2. Owner-applied patch.
3. `hoi4.probability_compare` using the same scenario ids.
4. A report that states whether the expected ordering improved, regressed, or remains unresolved.

The auditor does not choose the balance target. The targets are the ordering and validity requirements in this file.
