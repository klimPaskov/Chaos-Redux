# Event 011 Secret Alliance achievement matrix

Achievement titles are working labels, not final localisation. Final titles and descriptions should be written during implementation from the directions below.

## Achievement set

| Working ID | Working label | Visibility | Difficulty | Eligible play | Unlock conditions | Disqualifiers | Why it is not trivial | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 011_secret_alliance_the_empty_chair | The Empty Chair | Visible | Hard | Any country targeted by the normal event | Cause the hidden pact to collapse before public reveal, identify at least one true founder, and avoid declaring war on any innocent suspect | Triggerable scenario, pact reveals, target annexes an unconfirmed suspect, debug or forced fire | Requires investigation, restraint, and successful fracture rather than simple conquest | Empty conference chair beneath a broken pact seal |
| 011_secret_alliance_every_thread | Every Thread | Visible | Very hard | Any target | Reach the maximum Evidence band before reveal, correctly confirm every active member, and enter the reveal with no false-confirmed suspect | Any active member remains unidentified, any innocent country is publicly named, scenario launch | Requires complete network reconstruction while the pact adapts and destroys routes | Hand holding several connected cords |
| 011_secret_alliance_their_man_in_the_room | Their Man in the Room | Hidden | Very hard | Any target in Evolution II or III | Turn a founder or major sponsor, preserve the channel until reveal, and use its false planning effect to weaken the coalition opening | Channel exposed before reveal, turned country removed for invalidity, scenario launch | The player must identify the right motive, pay a specific concession, and protect the source through multiple operations | One reversed seal among matching seals |
| 011_secret_alliance_divide_the_table | Divide the Table | Visible | Hard | Any target after reveal | Remove at least half of the valid reveal membership from the target war through separate terms, defection, or refusal, without capitulating any of those members first | Target capitulates a counted member before its exit, coalition wins target war | Rewards motive knowledge and diplomacy during war rather than battlefield elimination | Conference table divided into separate sections |
| 011_secret_alliance_surrounded_not_buried | Surrounded, Not Buried | Visible | Extreme | Launch the Coalition Unmasked scenario at Maximum intensity | Survive the opening war, remain independent, and force the coalition to dissolve or accept a settlement while controlling the target capital | Lower scenario intensity, human-consent bypass, target becomes subject, world-end state | Maximum scenario begins with the broadest safe coalition and little preparation time | Central shield holding against a complete ring |
| 011_secret_alliance_two_giants_one_grave | Two Giants, One Grave | Hidden | Extreme | Normal event or High or Maximum scenario | Defeat a revealed coalition containing two active major members, keep the target's starting capital, and end with Coalition Resolve collapsed | One major leaves before reveal, target loses starting capital at final settlement, coalition victory | Requires surviving multi-theater major pressure and breaking sponsor coordination | Two large broken seals outside a surviving center |

## Tracking notes

### The Empty Chair

Track:

- normal automatic event origin
- public reveal has never occurred
- at least one true founder confirmed
- no innocent country has been attacked or publicly confirmed through the event system
- pact collapse effect completed

A quiet refusal from one member is not enough. The pact itself must lose the ability to continue.

### Every Thread

Track membership snapshots carefully. The final check should compare the confirmed set against active valid membership immediately before reveal. Countries removed earlier because they ceased to be valid do not count as hidden active members. Countries that were once members and later defected should appear in the player's confirmed history.

### Their Man in the Room

The turned member must produce a wartime consequence such as delayed entry, false deployment, exposed depot, or public refusal. Merely clicking a turn decision is insufficient.

### Divide the Table

A counted member exit must arise from the event's coalition-fracture systems. Normal capitulation or annexation does not count. This prevents the achievement from becoming a standard conquest task.

### Surrounded, Not Buried

The target must select Maximum intensity before launch. The scenario should record that selection in an immutable run flag used by the achievement. A later difficulty change cannot qualify.

### Two Giants, One Grave

A country counts as a major only if it qualified as a major at reveal. The achievement should not be affected by later dynamic major-status changes. Record the two qualifying major members at reveal.

## Localisation direction

- Titles should use intelligence, conference, encirclement, and betrayal language without revealing hidden mechanics outside the achievement UI.
- Descriptions should state visible campaign requirements clearly.
- The hidden achievements may conceal one condition but must remain discoverable through their icon and broader event theme.
- Avoid generic wording about completing the event or defeating the alliance.
- Do not mention implementation flags, variables, event IDs, or scenario internals.

## Asset and implementation coverage

Each achievement requires:

- registry entry in the shared Chaos Redux achievement file
- event-owned tracking flags or variables
- exact disqualifier cleanup
- English localisation
- completed, grey, and not-eligible DDS files
- GFX entry
- event documentation entry
- acceptance check against normal firing and manual scenario origin

## Achievement balance checks

- None unlock merely because Event 011 fired.
- None unlock from a single obvious decision.
- At least two reward investigation mastery.
- At least one rewards preserving and exploiting a turned source.
- At least one rewards wartime diplomatic fracture.
- At least one rewards the triggerable scenario at its hardest setting.
- At least one covers the rare two-major Evolution III coalition.
