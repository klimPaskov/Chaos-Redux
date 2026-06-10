# 007 Fury triggerable scenario specification: The World in Fury

## Scenario identity

| Field | Value |
| --- | --- |
| Scenario ID direction | `SCN-005` |
| Scenario name | The World in Fury |
| Parent event | Event 007 Fury |
| Scenario type | Manual sandbox or challenge setup |
| Player exclusion | Player country is always excluded from becoming Fury |
| Normal prerequisites | none, except impossible or conflicting launch states |
| Intensity | Low, Medium, High, Maximum |
| Type options | Fury Pact, Hostile Fury |

The triggerable scenario is a direct setup. It does not require the Chaos Meter, prior Fury firing, a date gate, an evolution unlock, or a previous world state. It creates instant chaos from the selected intensity and type.

## Scenario purpose

The scenario lets the player create a world where several small AI countries begin the Fury loop at once. It is a challenge setup, not a reward path. The player cannot be selected as a Fury country.

## Type options

### Fury Pact

All Fury countries are inclined to cooperate.

Opening effects:

- Fury actors join a shared Fury faction after setup or after first declaration.
- Fury Pact Cohesion starts above neutral.
- cooperation focus branch is unlocked.
- Fury actors avoid attacking each other while valid non-Fury AI targets exist.
- shared war table decisions are available.
- world-end branch is easier to reach if a main Fury actor becomes dominant.

AI behavior:

- Fury countries send limited aid to weaker Fury partners.
- target partition is preferred if two Fury countries approach the same region.
- rivalry happens only if pact cohesion collapses.

### Hostile Fury

Every Fury actor treats every non-player neighbor as prey. Fury actors can eventually target one another.

Opening effects:

- no Fury faction at start.
- Fury Pact Cohesion is not used or starts collapsed.
- rivalry branch is unlocked.
- Fury actors do not coordinate.
- Fury-on-Fury targeting becomes valid once ordinary targets are exhausted, or earlier at Maximum intensity.

AI behavior:

- Fury countries prefer ordinary weak AI targets first.
- if two Fury countries meet, rivalry pressure rises.
- the winner of a Fury-on-Fury war can inherit momentum.

## Intensity slider

The scenario uses the standard four-stop intensity slider.

| Intensity | Fury actors | Opening strength | Evolutions | Targeting behavior | Notes |
| --- | --- | --- | --- | --- | --- |
| Low | 1 | baseline starting package | none forced | one weaker AI neighbor at a time | closest to ordinary Fury event |
| Medium | 3 if eligible | stronger baseline package | Evolution I behavior enabled | one target at a time, cooperation or rivalry type active | spreads pressure across several regions |
| High | 6 if eligible | Evolution II style package | Evolution II enabled | two or more Fury actors can coordinate or compete | strong scenario challenge |
| Maximum | at least 10 if eligible | Evolution III style package | Evolution III enabled | all-neighbor declaration after short setup, or immediately if scenario setting says so | fulfills requested ten-minor setup |

If the world has fewer than ten safe eligible AI minors at Maximum, selection broadens through the candidate fallback order until ten are found. The player remains excluded. If ten still cannot be found, use every safe eligible candidate and record in scenario details that the world did not have enough safe candidates.

## Candidate distribution

The scenario should distribute Fury actors before stacking them.

Priority:

1. one per continent where possible.
2. one per large region with several minors.
3. avoid immediate overlap unless Hostile Fury at High or Maximum.
4. avoid player adjacency when enough other candidates exist.
5. avoid selecting countries that are already in player faction or subjects.
6. avoid special chaos tags and non-standard countries.

The scenario can broaden from one-state minors to two or three-state minors to reach intensity goals. It should not select majors simply to hit a count.

## Launch flow

The scenario launch should:

1. read selected intensity and type at confirmation time.
2. clear only scenario setup variables from previous preview.
3. build a safe candidate pool.
4. select Fury actors based on intensity.
5. initialize each actor through the same Fury helper used by ordinary event fire.
6. set scenario-specific flags for scaling and type.
7. grant appropriate ideas, decisions, focus tree, and units.
8. start first target selection for each Fury actor.
9. fire scenario setup event or report.
10. clean temporary bypass flags.

The scenario should not permanently bypass ordinary Fury rules outside setup.

## Scenario opening text direction

Title direction: `The World in Fury`.

Description direction: small countries in several regions begin sudden war preparations at the same time. The pattern is too similar to dismiss and too scattered to explain as one government plan.

Fury Pact type text direction: reports show liaison officers, shared signals, and matching war-office forms among the Fury countries.

Hostile Fury type text direction: reports show similar methods but no coordination. Each Fury actor appears to believe the whole map is its own front.

Intensity text direction:

| Intensity | Player-facing impact text |
| --- | --- |
| Low | One small AI country receives the Fury package and begins the normal loop |
| Medium | Several AI minors begin Fury with stronger units and the first evolution pattern |
| High | Many Fury actors appear with cooperation or rivalry behavior |
| Maximum | At least ten AI minors become Fury when the world has enough safe candidates, with stronger forces and all-neighbor pressure |

## Scenario type labels

Suggested UI labels:

| Type | Label | Detail direction |
| --- | --- | --- |
| Fury Pact | Pact | Fury countries can cooperate, form a faction, and share war support |
| Hostile Fury | Hostile | Fury countries are hostile to ordinary states and can turn on each other |

## Player safety

The scenario must never select the player as Fury.

Ordinary scenario target selection should also avoid:

- player country.
- player subjects.
- player faction members.
- countries in direct player wars when settlement could interfere.

At Maximum intensity and world-end escalation, the player can eventually face Fury through terminal warning logic, not through setup selection.

## Balance by intensity

### Low

- one Fury actor.
- baseline weekly units.
- no forced cooperation.
- one target at a time.
- suitable for a local challenge.

### Medium

- three Fury actors if safe.
- stronger initial units.
- Hardened Fury features available.
- target selection remains sequential.
- pact or hostile type visible.

### High

- six Fury actors if safe.
- Evolution II features available.
- cooperation or rivalry branches unlock.
- anti-Fury response can appear earlier.
- weekly units stronger.

### Maximum

- at least ten Fury actors if enough eligible AI minors exist.
- Evolution III features available.
- all-neighbor declarations become valid.
- stronger starting stockpiles and units.
- target distribution tries to cover multiple continents.
- anti-Fury response and world threat state can appear quickly.

## Scenario achievements

The scenario supports achievements that require:

- surviving Maximum intensity.
- defeating all Fury actors in Hostile type.
- defeating Fury Pact after it forms.
- preventing any Fury actor from becoming a major.
- defeating a Fury major without joining a major faction.

Achievement details are in the achievement spec and prompt.

## Acceptance criteria

The implementation is correct when:

- scenario appears in the triggerable scenario registry.
- scenario detail panel shows name, type options, and intensity impact.
- confirmation reads current intensity and type.
- launch excludes player.
- Low creates one Fury actor when safe.
- Medium creates three Fury actors when safe.
- High creates six Fury actors when safe.
- Maximum creates at least ten Fury actors when safe.
- pact type creates cooperation or faction behavior.
- hostile type prevents pact behavior and enables rivalry.
- scenario setup flags are cleaned after launch.
- ordinary Fury random event behavior is not permanently changed by scenario launch.
