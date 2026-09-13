# Event 045 probability and AI scenario contract

This document defines the mandatory named scenarios for every weighted Event 045 surface. It does not choose final numeric weights. The implementation owner chooses the intended balance, and `chaosx_ai_probability_auditor` verifies whether the source produces the required ordering.

Every audit begins with `hoi4.probability_inspect`. The auditor must state whether the candidate pool and external factors are complete. Use exact evaluation where the pool is complete, bounded or score-only evidence where it is not, sweeps for changing escalation or strength, and `hoi4.probability_compare` after every patch.

## P45-S01: Coherent calm-world opening

- World state: Chaos below 200, six valid regional governments, no common faction, no large existing regional war
- Candidate disputes: Macedonia, Aegean access, Southern Dobruja, absurd frontier incident
- Required ordering: disputes supported by current borders and at least two interested governments outrank flavour-only causes
- Opening expectation: two camps, four to six participants preferred, no unsupported adjacent power
- Failure condition: one-on-one opening when four or more coherent participants exist

## P45-S02: Fragmented Yugoslav space

- World state: Yugoslavia absent, several valid successor governments exist, neighboring states have mixed claims and relations
- Required ordering: successor-border and Macedonian disputes gain relevance, but participants without geographic or political connection remain excluded
- Opening expectation: camp construction recognizes successor states individually and avoids rebuilding a fictional unified Yugoslav actor
- Failure condition: dead-tag targeting, duplicate successor participation, or indiscriminate regional enrollment

## P45-S03: Same-faction regional map

- World state: all otherwise valid regional governments belong to one faction and are not in a valid internal rupture state
- Required result: automatic Event 045 weight is unavailable and displayed as `N/A`
- Failure condition: camp logic forces same-faction allies into opening war

## P45-S04: Contained regional belligerent

- Actor: Balkan belligerent with weak equipment reserves, exposed capital rail line, one valid claim, and no outside sponsor
- Required ordering: defensive mission and armistice tools outrank a new offensive claim or wider intervention request
- Sweep: improve equipment, supply, capital security, and allied strength
- Expected movement: claim pressure and support requests rise only as survival becomes credible

## P45-S05: Opportunistic regional belligerent

- Actor: Balkan belligerent with favorable strength, secure supply, an occupied registered claim, and rival sponsor involvement
- Required ordering: press claim and secure corridor outrank immediate armistice
- Hard limit: unregistered claims remain zero or unavailable
- Failure condition: AI pursues unrelated land or rejects all settlements after total military defeat

## P45-S06: Outside containment coalition

- Actor: outside major with no direct claim, high current war load, two credible mediation partners, and escalation in European Crisis
- Required ordering: conference, support suspension, and armistice pressure outrank arms, volunteers, guarantee, and direct intervention
- Sweep: reduce war load and remove mediation partners
- Expected movement: containment weakens gradually, not instantly

## P45-S07: Rival-driven exploitation

- Actor: outside major with theater access, reserves, war support, and a strategic rival supporting the opposite camp
- Required ordering: bounded arms or volunteers may outrank containment
- Direct intervention rule: remains below indirect support until a guarantee, faction commitment, strategic access threat, or hostile major proof exists
- Failure condition: direct war becomes the default response to the first rival shipment

## P45-S08: Evolution II fragmentation

- Target: participant with capital loss, severe instability, heavy casualties, occupation, and at least one valid provider-backed breakaway candidate
- Comparison target: otherwise similar participant with stable capital, low casualties, and no valid candidate
- Required ordering: the first target has materially higher fragmentation eligibility
- Hard limit: missing provider proof makes the result unavailable, not merely low weight
- Failure condition: empty tag creation, duplicate civil war, or fragmentation from time alone

## P45-S09: Evolution III former-ally rupture

- Candidate pair A: former allies with incompatible active claims and disputed occupation
- Candidate pair B: former allies with no claim, occupation, ideological, leadership, or settlement dispute
- Required ordering: pair A can rupture after pacing, pair B remains unavailable
- Sweep: remove occupation, settle the claim, or reconcile the settlement term
- Expected movement: rupture chance falls or disappears as the concrete dispute is removed

## P45-S10: World-war origin honesty

- Scenario A: Event 045 linked wars bring opposing major-led factions into direct conflict and spread beyond the original theater
- Scenario B: the same global war already existed before Event 045 fired
- Required result: Scenario A can set verified origin and reach Another World War, Scenario B cannot
- Failure condition: escalation score alone grants origin credit or the final stage without current proof

## Required comparison report

For every weighted patch, report:

- source surface and identifiers
- baseline scenario hashes
- candidate-pool completeness
- exact, bounded, sampled, or score-only status
- ordering before the patch
- intended ordering supplied by the owner
- ordering after the patch
- starvation, dominance, and invalid-target findings
- unresolved external factors

A passing comparison proves the accepted ordering. It does not prove that one precise percentage will hold in every campaign state unless the complete normalized pool and all external factors were supplied.
