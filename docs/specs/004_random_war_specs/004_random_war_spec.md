# 004 Random War Event Specification

## Design goal

Random War creates an unexpected war between eligible countries. The base event creates one declaration. Evolutions increase the number of linked declarations and later allow compatible Chaos Redux special countries to enter the pool.

The event should stay simple: a border incident, false order, ultimatum, disputed claim, panicked commander, or government exploiting confusion.

## Cluster placement

This event belongs in the **Wars** cluster.

The event is available from campaign start. The **Wars** cluster becomes visible or active around chaos tier 2.

## Selection rule

Selection draws from the eligible country pool under cooldowns, and player-controlled countries sit in the same pool as every other eligible country.

The implemented ladder stops at the first pair that passes every hard exclusion, in this order:

1. a compatible special-country pair, only when the stage's special chance passes its roll
2. a major or faction-member aggressor from the Chaos Tier stage upward
3. a bordering pair
4. any legal pair worldwide

Candidates inside one rung are drawn with equal chance.
The factor lists under Country eligibility describe weighted selection, which is a proposal rather than current behaviour.

## Core flow

1. Select an eligible aggressor and legal target using the existing pairing model.
2. Retain the invocation's stage, requested declaration count and selected actors.
3. Create each declaration only while the pair remains legal at that step.
4. Build the remaining linked dispute from the realized participants, excluding already-hostile pairs from additional declaration credit.
5. Finish the chain before sending its participant responses and observer summary.
6. Record the declarations actually created and the distinct countries actually involved.

The evolution ladder specifies the requested size of a dispute, while the realized chain records what happened.
After each declaration, faction calls, subject relations, capitulation or another crisis can make a later pair unavailable.
Use the existing legal-pair exclusions and permitted safe-pair fallback rather than forcing that stale pair.
If the remaining eligible pairs cannot complete the requested linked dispute, retain the wars already created and identify the unfilled slots as blocked.
Do not report the requested count as an accomplished count, reopen an existing war for another receipt, or add a disconnected filler conflict solely to reach the number.
An invocation that creates no declaration uses the existing unsuccessful-launch feedback and grants no participant reward.
An invocation that creates some declarations is reported as that partial incident, not as a second complete firing.

Every involved country receives at most one participant response for this invocation.
A country that both attacked and was attacked receives the defender response, following the accepted response priority.
One observer summary covers the completed chain and uses its actual distinct participant count.
Observer relevance includes major or faction-leader involvement, a neighboring participant, a compatible special country, or the late evolution stage.
Participant resources and temporary effects are applied once through that response, while shared war systems own the underlying war and its normal consequences.

Future acceptance cases should interrupt a three-country chain after its first declaration, make the next pair already hostile through a faction call, and remove one actor before the final step.
Each case must show truthful realized counts, one response per live participant, no repeated war reward and no forced stale declaration.
Existing option weights, special-country draw thresholds and stage-size tuning remain unchanged by this contract.

## Baseline: Border Incident Becomes War

Available from campaign start when Event ID 4 is enabled and selected by the random event system.

Result:

- 1 eligible aggressor declares war on 1 eligible target.
- Calm World baseline pair selection blocks major-versus-non-major pairings so the first-stage event stays regional or scale-matched instead of opening with a major power overrunning a minor.
- Aggressor and target are saved for localisation and event log text.
- Aggressor and target receive short cooldowns so the same countries are not selected repeatedly.

Report direction:

A border incident becomes a war before either government can control the story. Each side issues its own explanation as troops cross the line and diplomats argue over who moved first.

Aggressor options:

- **The order stands**
  - war continues
  - small war support gain
  - command power cost

- **Blame the general staff**
  - war continues
  - small stability loss
  - the country is barred from aggressor selection for the dismissal cooldown

Target options:

- **Hold the line**
  - political power cost
  - small war support gain
  - a timed idea with a short defensive package on core territory

- **Mobilize the reserves**
  - small stability cost
  - a timed idea that speeds mobilization and training and widens the recruitment share

Each response package stays at three modifiers or fewer so its tooltip reads at a glance, and reserve mobilization draws on the country's own population instead of granting flat manpower.
The current costs, durations and cooldown lengths live in `common/script_constants/004_random_war_constants.txt`, with the static idea modifiers tuned through file-local constants in the event's ideas file because those fields reject `constant:` tokens.

## Country eligibility

### Hard requirements

An aggressor must exist, control at least one state, be sovereign, not be capitulated, and be outside the recent-aggressor and dismissal cooldowns.

A target must exist, control at least one state, be sovereign, not be capitulated, and be outside the recent-target cooldown.

A pair is legal only when the two countries are not already at war with each other, are not allies through faction or subject relations, and the aggressor passes the engine declaration check against that target.
In Calm World a major may not be paired against a non-major, so the first stage stays scale-matched; that restriction lifts once the chaos tier advances.

### Weighted selection, proposed (spec audit 2026-10-10)

Current selection is equal-chance inside each ladder rung, so a border incident between two tense rivals is no more likely than one between two quiet neighbours.
A bounded scoring pass would make the chosen pair read as a plausible quarrel without adding a visible meter.

Keep the score small and legible, built from factors the player can already see:

- aggressor side: high war support, an aggressive ruling ideology, a claim or core on the target, local strength advantage
- target side: shared border, poor relations, a contested core or claim, few active wars
- reductions: an aggressor already fighting several wars, a target already overwhelmed, a faction leader at the baseline stage

Use the Event 009 weighted-pool pattern (`score_white_peace_pair`, `add_current_white_peace_primary_to_weighted_pool`, `select_weighted_white_peace_primary_candidate`) rather than a new mechanism, keep every factor in the event's constants file, and keep the ladder as the fallback when no scored candidate qualifies.
This proposal does not change the stage table, declaration counts or special-country chances.

## Pairing model

The implemented rungs are the special-country pair, the major or faction pair from the Chaos Tier stage upward, the bordering pair, and the global pair.
Later stages therefore loosen pairing by reaching the wider rungs more often, not by relaxing a distance test.
Hard exclusions always apply, in every rung and at every stage.

### Known spec-to-source mismatches

The first item was resolved in the 2026-10-10 release pass.

- Resolved: the ordinary major, bordering and worldwide rungs, and the ordinary rungs of a chain, now exclude special Chaos Redux countries as aggressor and target, so the stage's special chance is the only way in.
- Protected scripted actors are not excluded beyond the sovereignty, capitulation and declaration checks, so a country held inside another event's scripted crisis can be pulled into an unrelated war.
- Aggressor and target cooldowns are single flat values, so the stated loosening of cooldown limits at higher evolutions does not happen.
  A per-stage cooldown entry in the existing constants group would deliver it without new runtime state.

## Evolution track: War Contagion

War Contagion increases declaration count and widens the country pool.

| Stage | Chaos tier | Name | Declarations | Special chaos country chance | Behavior |
| --- | --- | --- | --- | --- | --- |
| Baseline | campaign start | Border Incident Becomes War | 1 | 0% | one aggressor declares on one target |
| I | Gathering Storm, 200+ | Triangular Incident | 3 | 0% | three countries form a linked dispute |
| II | Rising Chaos, 400+ | Four Fronts | 4 | 20% | four declarations form a conflict web |
| III | Chaos Tier, 600+ | Contagious Ultimatums | 5 | 35% | majors and faction members become more likely |
| IV | Totalen Chaos, 800+ | The War Week | 6 | 55% | several wars fire in one chain |
| V | World Collapse, 1000+ | Open Season | 7 to 8 | 70% | late-game war wave while normal random events still run |

Thresholds, declaration counts, special-country chances and cooldowns live in the event's constants file.
Only the highest enabled stage available at the current chaos tier is used; a disabled evolution falls back to the next enabled lower stage or the baseline profile.
Random draws use half-open integer ranges, so the d100 roll and the final-stage declaration draw carry exclusive upper bounds.

### Evolution I: Triangular Incident

Select three countries.

Preferred pattern:

- A declares on B
- B declares on C
- C declares on A

Fallback pattern:

- create three safe pairwise declarations among the selected countries

### Evolution II: Four Fronts

Create four declarations.

Possible patterns:

- A declares on B, B declares on C, C declares on D, D declares on A
- A declares on C, B declares on D, C declares on B, D declares on A
- two linked disputes joined by one extra declaration

### Evolution III: Contagious Ultimatums

Create five declarations.

Changes:

- one major country can enter the pool more often
- faction members can appear with reduced weight
- compatible special chaos countries become a normal rare outcome
- the conflict web should stay readable

### Evolution IV: The War Week

Create six declarations.

Changes:

- one declaration may ignore normal rationality weighting
- faction entanglement is allowed with restraint
- compatible special chaos country involvement becomes common
- observer reports become more common when majors or special countries are involved

### Evolution V: Open Season

Create seven to eight declarations.

Changes:

- compatible special chaos country involvement is strongly favored if one exists
- one major power or faction leader can be included if it is not already overwhelmed
- irrational pairings are acceptable
- event log text marks this as the highest War Contagion stage

## Compatible special chaos countries

Later evolutions can include special Chaos Redux countries that are safe for normal diplomacy and war.

Compatibility uses the shared `is_special_chaos_country` trigger, which already covers the zombie hordes, Holy Realm, the Mengele civil-war and post-coup actors, and the other live special actors.
The complementary `uses_normal_civilian_systems` trigger identifies an ordinary civilian participant and is the gate the ordinary rungs should use.

Use three simple roles:

1. **Special aggressor**
   - special country declares on a normal country

2. **Special target**
   - normal country declares on the special country

3. **Special catalyst**
   - special country becomes one node in the larger conflict web

The event uses existing compatible tags. It does not create new special countries.

## Pacing and safeguards

A selected aggressor and a selected target each receive a temporary cooldown flag, and dismissing the general staff adds a longer aggressor exclusion.
Chain members carry a one-day flag so a single invocation cannot reuse a country inside its own chain.
The cooldowns are the only pacing brake, so they must stay long enough that the same quarrel does not reappear in consecutive firings and short enough that the late stages can still assemble seven or eight declarations.

## Shared system connections

Random War creates ordinary wars, so it inherits the shared consequences instead of scripting its own.

- Front movement feeds the humanitarian systems automatically: `on_state_control_changed` calls the hostile-capture adapter, which adds bounded war flight pressure through `migration_request_war_pressure` and queues one famine food assessment for the captured state.
  Random War must not add a second famine or migration request for the same war, or the same displacement is paid for twice.
- Casualties feed the Chaos Meter and the deaths ledger through the daily casualty update, so no event-specific chaos or deaths call is needed for the war itself.
- A war created here is an ordinary Event 009 White Peace candidate, so a stalled Random War quarrel can end through that event rather than a bespoke settlement branch.
- Cluster participation is owned by the Wars cluster rows; the event still fires normally when the cluster roll does not.

Condemnation is not involved: a declaration of war is not a condemnation source, and only the weapons a participant later uses can create one through its owning system.

## Event log and settings

Record:

- Event ID 4
- event name
- aggressor
- target
- realized declaration count and any blocked requested slots
- special chaos country involvement
- active War Contagion stage
- fired count

Event details text should say that Random War creates unexpected wars, and higher chaos allows larger linked war webs and compatible special-country participation.

The event enable setting controls all Random War firings. Evolution settings should select the highest enabled War Contagion stage available under the current chaos tier.

## Presentation and assets

No new final art is required.

- Report events use the registered `GFX_report_event_random_war` sprite.
- The observer news event uses the vanilla `GFX_news_event_generic_chaco_war` image.
- The two target response ideas use the existing `generic_wall_line` and `generic_infantry_bonus` images.

If a dedicated image is ever added, keep the registered sprite names and use `gfx/event_pictures/004_random_war/report_event_random_war.dds` at 210x176 and `gfx/event_pictures/news_event_random_war.dds` at 397x153, both declared in `interface/chaosx_pictures.gfx`.
Suitable subjects are mobilization, border troops, troop columns, a diplomatic crisis, or a government war announcement.

## Localisation direction

### Evolution names

- Triangular Incident
- Four Fronts
- Contagious Ultimatums
- The War Week
- Open Season

### Event details text

Explain:

- Random War creates unexpected wars
- repeatable weighting makes repeated firings less common over time
- chaos unlocks larger war webs
- later stages can include compatible Chaos Redux special countries

## Catalog update text

### Details

Random War catches two countries in a sudden declaration. Later stages can link several wars and draw compatible Chaos Redux powers into the same conflict web.

### Evo I

Gathering Storm: Triangular Incident links three countries in one sudden conflict.

### Evo II

Rising Chaos: Four Fronts links four declarations in one conflict web and may draw in a compatible Chaos Redux power.

### Evo III

Chaos Tier: Contagious Ultimatums links five declarations and can draw major powers, faction members, or a compatible Chaos Redux power into the conflict.

### Evo IV

Totalen Chaos: The War Week links six declarations in a short chain, with a compatible Chaos Redux power likely to participate.

### Evo V

World Collapse: Open Season spreads seven or eight declarations as ordinary events continue, and compatible Chaos Redux powers are likely to join.

### Cluster

Wars. Secondary connection: Minor events.

## Implementation checklist

- Keep event root as `chaosx.nr4.1`, registered as repeatable ID 4 and available from campaign start.
- Keep Wars cluster visibility or active status beginning around chaos tier 2.
- Keep the prepared pair on the dispatching country and consume it after firing, so a later invocation prepares fresh participants.
- Keep one participant response per country with defender priority, and one observer summary per invocation.
- Keep every threshold, declaration count, special-country chance and cooldown length in the event's constants file.
- Exclude special Chaos Redux countries from the ordinary rungs and keep them behind the stage's special chance.
- Update event registration, event type lookup, event log names, debug names, detail text, localisation, docs and the spreadsheet row together.
- Keep evolved variants readable in the event log and evolution view.

## Open questions

These proposals are not accepted design and are not implementation requirements until the user or a parent accepts them.

- Weighted pair selection, proposed (spec audit 2026-10-10): score candidate pairs from war support, ideology, claims, borders, relations and existing war load instead of drawing each rung with equal chance.
- Per-stage cooldown lengths, proposed (spec audit 2026-10-10): replace the single flat aggressor and target cooldowns with one entry per War Contagion stage so the late stages can genuinely reuse a crowded world.
- Protected-actor exclusion, proposed (spec audit 2026-10-10): exclude a country currently held inside another event's scripted crisis from ordinary selection, using that event's own live-actor trigger rather than a new marker.
