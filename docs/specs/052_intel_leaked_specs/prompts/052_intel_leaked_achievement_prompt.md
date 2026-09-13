# Achievement Implementation Prompt for Event 052 Intel Leaked

Implement the full Event 52 achievement set through the existing Chaos Redux achievement registry and asset workflow.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, the Event 52 specification, the acceptance criteria, and current achievement precedents before editing.

All achievement names below are working labels. Write final player-facing localisation from the stated direction.

## `chaosx_052_before_the_ink_dries`

Working label: Before the Ink Dries

Description direction: the target makes a newly circulated archive largely useless before foreign governments can turn its freshest material into a severe success.

Eligible country: the human-controlled Event 52 target.

Unlock conditions:

- one ordinary or evolved Event 52 target incident is active
- the target began at Exposure 90 or higher
- the target reduces Exposure to 25 or lower
- no severe named-exploitation outcome succeeded before the threshold was reached
- the target has taken at least one real containment action

Disqualifiers:

- force-trigger or debug setup under the current achievement rules
- invalid or incomplete incident initialization
- Exposure set directly through test controls

Difficulty: high.

Why it is not trivial: the player must spend resources or accept operational losses quickly while the archive is most useful.

Icon direction: a still-wet classified page sealed, destroyed, or rendered unreadable before copying finishes. No text.

Tracking notes:

- store initial Exposure once
- record severe exploitation once through owner proof
- commit achievement only after the current value reaches the threshold through normal incident processing

## `chaosx_052_a_better_falsehood`

Working label: A Better Falsehood

Description direction: the target turns the leak into a controlled deception and causes several hostile governments to act on distinct false assumptions.

Eligible country: the human-controlled Event 52 target.

Unlock conditions:

- Poison the Leak succeeds in one incident
- at least three hostile high-Reliance governments suffer valid domain-specific false-assumption outcomes
- each recipient had a matching strategic use for the false material
- the outcomes occur before the Event 52 sequence closes

Disqualifiers:

- passive Archive Confidence loss
- repeated counting of the same recipient and same outcome
- friendly cooperative recipients
- recipients that never reached the Reliance requirement
- force-trigger or debug setup

Difficulty: very high.

Why it is not trivial: the player must preserve enough control to construct a coherent deception, keep the archive credible, and wait for several relevant foreign actors to commit.

Icon direction: a false order placed over a real code sheet while several foreign arrows follow the planted instruction. No text.

Tracking notes:

- store unique recipient IDs
- require a successful outcome proof from the Event 52 deception owner
- count one qualifying result per recipient
- clear incident-local tracking at cleanup after achievement commit is evaluated

## `chaosx_052_everyone_knows_everything`

Working label: Everyone Knows Everything

Description direction: the player survives a Total Compromise sequence in which a current war enemy is exposed at the same time.

Eligible country: a human-controlled target in a Total Compromise sequence.

Unlock conditions:

- the player and at least one current war enemy are separate Event 52 targets in the same sequence
- the player reduces personal Exposure to zero before passive expiry
- the player retains control of the capital until personal incident closure
- the mutual-target relationship existed while both sides had positive Exposure

Disqualifiers:

- peace before any period of mutual positive Exposure
- capital loss during the qualifying interval
- force-trigger or debug setup

Difficulty: high.

Why it is not trivial: the enemy has exceptional information while the player must spend military and intelligence resources on rapid recovery.

Icon direction: mirrored opposing archives or two open dossiers facing each other, with both sides exposed. No text.

Tracking notes:

- use the sequence ID to prove shared incident ownership
- preserve the qualifying enemy target proof if that enemy resolves first
- evaluate the player's capital-control history through the qualifying interval
- remain compatible without agency DLC

## `chaosx_052_no_names_left_behind`

Working label: No Names Left Behind

Description direction: one country survives three separate personnel-risk incidents without losing exposed people or a critical network.

Eligible country: the human-controlled Event 52 target.

Unlock conditions:

- the same country resolves three separate Event 52 sequences
- each sequence included a real Personnel at Risk state
- no sequence produced an operative capture, destroyed critical network, or equivalent severe generic personnel failure
- each sequence reached normal target closure

Disqualifiers:

- incidents without a personnel-risk profile
- repeated counting of one sequence
- force-trigger or debug setup

Difficulty: long-form high.

Why it is not trivial: repeatable weight decline makes three valid incidents uncommon, and every qualifying incident requires active protection.

Icon direction: several identity cards or silhouettes protected behind destroyed records, with no readable names or text.

Tracking notes:

- store a country-level count of unique resolved qualifying sequence IDs
- use agency-specific severe outcome proof when available
- use the mapped base-game-equivalent severe personnel proof otherwise
- reset the clean streak only when a qualifying incident records a severe personnel failure

## Implementation requirements

- Use the single root Chaos Redux achievement registry.
- Add final localisation for name and description.
- Create and wire completed, grey, and not-eligible icon variants through the Event 52 asset prompt.
- Keep filenames aligned with full achievement IDs.
- Add every tracking flag, variable, unique-recipient set, sequence proof, and disqualifier required above.
- Keep achievement tracking outside ordinary debug or manual setup paths.
- Prevent repeated cleanup, save reload, cluster firing, or target reinitialization from counting twice.
- Document the achievements in the Event 52 overview and catalog-facing notes where current project precedent requires them.
- Include achievement scenarios in the event completion audit.
