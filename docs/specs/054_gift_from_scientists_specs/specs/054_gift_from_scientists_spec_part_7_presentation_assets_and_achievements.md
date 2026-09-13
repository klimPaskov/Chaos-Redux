# Event 54: Presentation, Assets, and Achievements

## Presentation choice

Event 54 should use the normal report-event presentation, Event History, Event Details, and evolution views.

The event resolves through one immediate transaction. The consolidated player report and its full-result tooltip present the complete result for one, three, five, or ten grants.

## Event text direction

The event title remains Gift from Scientists.

The main report should use the affected country's viewpoint. It should describe several institutions confirming discoveries that appeared too quickly and too widely to share a normal origin.

The visible facts are:

- the discoveries work
- the country's institutions can use them
- other countries report their own unrelated discoveries
- no source has been verified
- the exact local technologies are known to the player

The report should preserve uncertainty about the cause. It should avoid assigning the event to Kruger, Antarctica, aliens, espionage, time travel, divine intervention, or a central conspiracy.

The tone should be curious, uneasy, and practical. It should avoid panic, grand prophecy, fake scientific language, generic government communiques, and abstract statements about progress changing humanity.

The report should name the country's actual institutions only when a reliable dynamic form exists. A neutral formulation should work for every government and special research actor.

## Acknowledgement direction

The single acknowledgement should sound like a government accepting useful knowledge without understanding its source.

The option can use dry official confidence or cautious scientific understatement. It should not sound like the player is choosing whether to accept the technologies because the grant has already occurred.

The option tooltip should carry the complete grant list when the main report does not show all results.

## Evolution text direction

Multiple Breakthroughs should describe several fields moving at once inside each country.

Accelerated Discovery should introduce discoveries that resemble the work of hidden programs and unfamiliar institutions.

Scientific Deluge should describe normal research order breaking down as whole branches of knowledge become available in a short period.

Evolution text must remain in-world. It should not describe grant counts as tuning, candidate registries, pool expansion, or implementation changes.

## Event Details direction

Event Details should explain the global premise, independent country outcomes, and the possibility of advanced or irrelevant discoveries.

It should not list exact mechanical effects, current candidate identities, custom providers, safety profiles, or hidden exclusions.

The evolution preview can identify the rising scale of the phenomenon and the later appearance of technologies associated with stranger Chaos systems.

## Cluster text direction

Scientific Research cluster text should cover sudden discoveries, military simulation, doctrine leaps, singular researchers, and institutional failure.

The cluster should sound mixed and unstable. It should not present the whole cluster as a reward package.

Event 54's member line should identify a global wave of random completed technologies without turning the cluster details into an effect list.

## Report-event image

Event 54 needs one generated report-event image.

### Asset identity

- Working asset ID: `report_event_054_gift_from_scientists`
- Asset type: report-event image
- Final size: 210x176
- Final folder: `gfx/event_pictures/054_gift_from_scientists/`
- Proposed final file: `report_event_054_gift_from_scientists.dds`
- Proposed sprite: `GFX_report_event_054_gift_from_scientists`
- Source mode: generated fictional period-documentary image

### Image direction

The source scene should show a crowded late-1930s or early-1940s research room where several scientists examine unrelated working prototypes on one table. The scene can include period radio components, optical instruments, engine parts, electrical test equipment, drafting tools, and mechanical assemblies.

The composition should communicate that several fields produced results at once. One clear table and a small group of researchers are stronger than a giant laboratory or a wall of equations.

The source image should look like a plausible period documentary photograph. It should avoid modern laboratories, modern protective equipment, digital screens, readable generated text, famous real scientists, fantastical energy effects, aliens, Antarctic scenery, and explicit Kruger imagery.

After generation, the image receives the standard report-event treatment with black-and-white conversion, sepia, grain, paper border, slight tilt, transparent edge space, and soft shadow.

### Asset review

The processed PNG and DDS must remain readable at 210x176. The prototypes should not merge into an unclear pile. Faces can remain incidental and must not depict a named real person.

The report image is static and appears only with the country report.

## Achievement 1

### Working key

`chaosx_achievement_054_complete_the_chain`

### Working label

Complete the Chain

This is a working design label and not final localization.

### Eligibility

Any player country that began the campaign with three or fewer research slots.

### Required campaign situation

Event 54 grants the player a conventional technology that is at least three years ahead of the current date and has at least three unresearched ordinary technologies in its transitive prerequisite ancestry.

Within 730 days of the grant, the player must research every missing prerequisite node in that ancestry through normal research.

### Disqualifiers

- another Event 54 firing grants one of the missing prerequisite nodes
- an owner callback or another event grants one of the missing prerequisite nodes
- the player becomes a subject before completion
- the original recipient country is annexed or replaced
- the selected technology is removed through an unsupported state change

### Difficulty

Hard and visible.

### Why it is meaningful

The event supplies an advanced result, but the player must reorganize normal research to build the missing foundation. The achievement rewards using an awkward random gift instead of merely receiving it.

### Tracking needs

The event stores the selected technology, the missing prerequisite set, the deadline, and the original recipient. Normal research completion removes nodes from the tracked set. The achievement unlocks when the set reaches zero before the deadline.

The tracker must reject technologies with fewer than three missing prerequisite ancestors and must not count hidden setup nodes.

### Icon direction

A bright advanced technical node connected backward through three darker repaired links. The icon should look like an HOI4 achievement, not a literal software graph.

## Achievement 2

### Working key

`chaosx_achievement_054_borrowed_future`

### Working label

Borrowed Future

This is a working design label and not final localization.

### Eligibility

Any independent player country.

### Required campaign situation

Across one campaign, the player receives registered custom technologies from two different owner systems through Event 54.

At the moment of each grant, the owning event or project must not have delivered its normal primary reward to that player country.

The player must then complete one owner-defined public use milestone for each technology and remain independent until global Chaos reaches 800.

### Disqualifiers

- both technologies come from the same owner provider
- either owner event had already delivered its normal reward to the player at grant time
- an owner callback marks its normal event fired
- the player becomes a subject before 800 Chaos
- either use milestone is satisfied by debug, setup, or a grant callback instead of gameplay use

### Difficulty

Extreme and hidden.

### Why it is meaningful

The achievement requires rare Event 54 outcomes from separate systems, then asks the player to make both foreign pieces of knowledge matter in play. It also tests the owner registry's most important lifecycle rule.

### Tracking needs

Each registered provider can expose one bounded achievement-use callback. The callback records meaningful use of the granted technology but cannot unlock the achievement alone.

Event 54 stores distinct provider identities, grant dates, owner-reward state at grant time, and use completion. The final check also requires independence and 800 Chaos.

The achievement should remain unavailable until at least two implemented providers can satisfy the full contract.

### Icon direction

Two sealed research dossiers from different sources opening onto one bright technical schematic. The visual should communicate borrowed knowledge without using readable text or owner-specific portraits.

## Achievement asset package

Each achievement requires the project's full 64x64 achievement state package using the exact current achievement precedent.

Proposed basenames:

- `chaosx_achievement_054_complete_the_chain`
- `chaosx_achievement_054_complete_the_chain_grey`
- `chaosx_achievement_054_complete_the_chain_not_eligible`
- `chaosx_achievement_054_borrowed_future`
- `chaosx_achievement_054_borrowed_future_grey`
- `chaosx_achievement_054_borrowed_future_not_eligible`

Achievement files remain directly under `gfx/achievements/` because that surface uses root filenames.

The icon artist should inspect the exact achievement reference family, generate native transparent source art where the consumer uses alpha, create the completed icon first, and derive state variants only through the approved achievement workflow.

## Asset coverage summary

| Asset | Count | Source mode | Final role |
| --- | --- | --- | --- |
| Report-event image | 1 | Generated period documentary | Event report |
| Achievement icon triplets | 2 triplets | Generated icon art | Achievement states |

The final asset package must include source PNGs, processed PNGs, DDS files, manifests, contact sheets where useful, and GFX handoff notes.

## Localization audit direction

The final implementation should receive a dedicated localization pass covering:

- event title, description, and acknowledgement
- country-specific grant summary
- full technology-list tooltip
- pool-exhaustion wording
- registered-technology wording
- evolution names and descriptions
- Event History and Event Details
- Scientific Research cluster details and member line
- achievement titles and descriptions
- debug names kept out of player-facing text

The audit should preserve technology names from their owning localization and should not rewrite owner technology names inside Event 54.

All player-facing prose should avoid em dashes, semicolons, staccato fragments, staged contrast formulas, generic dramatic filler, implementation history, raw variable names, and unexplained internal terms.
