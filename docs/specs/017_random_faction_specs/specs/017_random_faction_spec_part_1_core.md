# Event 17: Random faction, core specification

## Event identity

`Random faction` is a minor repeatable diplomacy event about the collapse of small-state neutrality under faction pressure. A country that looks too small to matter is suddenly pulled into the architecture of the wider war. The event remains low severity on an individual firing, but its repeatable memory and evolutions make it a world-shaping pressure system over time.

The event replaces the old two-faction assumption with a dynamic faction list. It should never assume that the Axis or Comintern exist. It should look for actual living factions, choose from them, and make the selected minor join one. If the selected country is controlled by a human player, the player receives one to four faction options and must choose one of them. If the selected country is AI-controlled, the same option logic runs through AI weights.

## Playable promise

The player should feel that neutrality is becoming a scarce resource. The first firing can look almost like diplomatic noise, but a campaign that keeps rolling this event should start to show patterns: neighbors watching each other, faction leaders trying to preempt rivals, frontier states militarizing, and whole regions losing confidence that they can remain outside the blocs.

The event should never become a pure random button. It should have readable logic:

- ideology can pull a minor toward one faction
- geography can pull a minor toward a nearby protector
- fear can pull a minor toward the faction most likely to defend it
- previous local alignments can pull neighbors into copycat behavior
- high chaos can make neutrality harder to maintain
- wars can make a faction choice dangerous instead of decorative

## Baseline firing flow

The normal automatic flow has four steps.

1. Build the eligible minor pool. This pool includes independent minor countries that exist, are not subjects, are not already in a faction, are not capitulated, are not a special chaos country that should ignore normal diplomacy, and are still able to use normal diplomatic behavior. A human-controlled country can be in this pool if it meets the same rules.
2. Build the living faction pool. A faction is valid only if the faction leader exists, the faction has a usable leader scope, and joining the faction does not require joining an impossible or invalid diplomatic state. The implementation should not assume hardcoded faction names.
3. Pick one eligible minor. If the country is AI-controlled, choose a faction through weighted logic and apply the result. If the country is human-controlled, open a country event with one to four faction options. The player cannot decline all options.
4. Apply alignment memory. The country joins the chosen faction, the event log records the actor and faction leader, regional pressure is stored, and nearby eligible neutrals receive hidden pressure memory for later follow-ups.

## Eligible country model

The selected country must be a normal minor that can plausibly join a faction.

### Required country traits

- exists and owns a capital
- independent
- not a subject, puppet, integrated puppet, collaboration government, Reichskommissariat, or equivalent subject form
- not already in a faction
- not a major power
- not capitulated
- not a government in exile
- not blocked by shared special chaos country triggers
- not blocked by an event-specific recent alignment cooldown
- has at least one valid faction target

### Strong exclusions

The event should not select countries that are not meant to use ordinary diplomacy. This includes nonhuman countries, terminal crisis actors, scripted world threats, countries managed by special isolation systems, and countries whose current event package deliberately disables standard faction joining. Use shared Chaos Redux classification triggers where possible instead of creating a duplicate local classifier.

### Soft weighting factors

Eligible countries should not be equally likely in all situations. The selection score should consider:

| Factor | Effect on selection |
| --- | --- |
| Bordering a faction member | strong increase |
| Multiple faction members nearby | strong increase |
| Low stability | moderate increase |
| Low war support while threatened | moderate increase |
| Has a threatening neighbor | moderate increase |
| Has recently resisted faction pressure | moderate decrease |
| Has recently joined and left a faction through another system | strong decrease |
| Has high neutrality resilience from decisions or ideas | moderate decrease |
| Human-controlled eligible minor | allowed, but not guaranteed |

The user asked that a random minor, or the player if selected, can be chosen. The implementation should not target the player by default, but it should not exclude the player either.

## Faction option model

The selected country receives a set of one to four possible faction leaders.

### Option count

- If one valid faction exists, show or apply one option.
- If two valid factions exist, show or apply two options.
- If three valid factions exist, show or apply three options.
- If four or more valid factions exist, show four random faction options.

The four-option rule matters for player agency. If there are at least four factions in the world, the player should see four valid choices.

### Faction validity

A candidate faction should be rejected if:

- the leader does not exist
- the leader is capitulated or cannot receive ordinary diplomacy
- the selected country is already at war with the leader
- joining the faction would require a broken scope or dead target
- the faction is restricted by a special event rule that forbids ordinary members
- the faction leader is a special nonhuman or terminal actor unless a later event evolution explicitly allows that kind of chaos interaction

At baseline, a country should not be pulled into a faction that is already at war with the selected country. Evolution II can relax wartime restrictions for countries that are already at war with someone else, but direct enemy factions should remain invalid unless another event specifically creates that exception.

### Faction scoring for AI and option order

The player sees a random set, not a sorted diplomatic recommendation. The AI should still understand why it chooses one. The option score should use:

| Factor | AI direction |
| --- | --- |
| same ideology or close ideology group | strong increase |
| faction leader is nearby | strong increase |
| faction leader is stronger than local rivals | moderate increase |
| selected country has high relations with leader | moderate increase |
| selected country has a common enemy or feared neighbor | moderate increase |
| faction is already fighting a neighbor of the selected country | strong increase at Evolution II and higher |
| faction has low cohesion from this event's pressure system | moderate decrease |
| faction leader has recently failed to protect a member | moderate decrease |
| selected country has neutrality resilience | reduce all scores, then choose among remaining options if event still fires |

## Player-facing country event

The selected human country receives a short country event with one to four faction options. The options are the actual faction choices. There is no neutral or refuse option.

The event should show:

- the selected country's situation as immediate and public
- the available faction leader names or faction names
- whether choosing a faction will likely pull the country into an active war
- a short visible effect tooltip for the chosen option
- no hidden future evolution spoilers

The tone should be anxious but not apocalyptic. It should describe a small government making a choice under pressure. It should not become a staff-room memo or a generic diplomatic note. Final localisation should mention the country, the faction, and the sense of losing room to maneuver.

## AI-controlled result

The AI version should not show a visible event to the human unless the selected country is relevant to the human through normal event notification rules. The AI receives the same effective options and chooses through weighted logic. The actual join should happen through the shared helper used by the player option so logging, memory, spirits, chaos, and cleanup stay identical.

## Baseline effects

The baseline result should be small enough to remain a minor repeatable event and visible enough to matter.

### Selected minor

The selected country joins the chosen faction. It receives a temporary mixed national spirit or country modifier representing emergency diplomatic reorientation. The spirit should be short-lived and should not become a permanent reward. Its exact values should be tuned dynamically, but its role is:

- short-term stability strain or political disorganization
- small defensive coordination gain if faction is at war
- small diplomatic acceptance or relation adjustment with the faction leader
- a recent alignment cooldown flag so the country cannot be selected again too soon

### Chosen faction leader

The faction leader receives event memory that a minor joined through Event 17. This should be useful for logs, AI, and evolved reaction decisions. The leader should not receive a large free reward in baseline.

### Neighboring neutral minors

Nearby eligible neutral minors receive hidden regional pressure memory. At baseline this memory should not immediately force action. It should increase their chance of later selection, especially under Evolution I.

### Regional memory

The target region receives a pressure mark for the faction that gained the member. The region can be a continent bucket or a more precise scripted region if the implementation already has one. The purpose is to prevent the repeatable event from feeling like isolated global dice rolls.

## Event log and event details

The event log should show the selected minor as the actor. The detail window should also identify the faction joined, if the event log system can show a secondary target cleanly. If only one actor can be shown, use the selected minor and put the faction name in the entry text through dynamic localisation.

Event Details text should describe the situation and premise. It should not list modifiers, AI weights, option odds, or hidden pressure variables.

## Cluster role

The event belongs in the diplomacy family as a low severity member. The preferred route is to attach it to the existing diplomatic panic style cluster if that cluster remains the repository's diplomacy cluster. If the implementation creates a separate bloc-alignment cluster later, Event 17 should be a low severity required or optional member according to the cluster design.

Cluster behavior should stay diplomatic. It can combine with relation shocks, guarantees, propaganda, and border readiness. It should not directly create a war goal through the cluster by default.
