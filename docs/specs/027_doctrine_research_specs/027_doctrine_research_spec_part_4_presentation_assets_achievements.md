# Event 027: Doctrine Research

## Part 4: Presentation, assets, and achievements

## Player-facing writing direction

Doctrine Research should read as a positive military-institution event. The subject is the work of general staffs, service schools, field instructors, formation commanders, translated manuals, after-action studies, and live exercises.

The writing should show practical military learning through visible activity:

- officers returning from fronts with corrected field manuals
- training formations testing revised methods
- naval staffs comparing convoy and fleet results
- air commands revising mission doctrine from recent combat
- joint schools arguing over which lesson deserves adoption
- special formations formalizing techniques already used in the field
- CBRN staffs converting protection, logistics, reconnaissance, and operational evidence into doctrine

The event should not default to generic scientists making a discovery in a laboratory. The event name uses research in the broad military sense of study, trial, doctrine writing, and institutional learning.

The tone remains restrained. Mild irony may come from service rivalry, duplicated manuals, officers claiming ownership of a successful lesson, or a country trying to turn one campaign into a universal rule. The event should not use broad jokes during descriptions of mass casualties or real military disasters.

## Information shown to the player

The opening report should explain:

- the country has a doctrine-development batch
- how many choices the batch contains
- Grand Doctrine adoption uses one choice without an event mastery step
- later choices can be stacked or distributed

The choice pages should show:

- remaining choices
- doctrine domain
- current Grand Doctrine or unselected state
- track and subdoctrine when relevant
- current mastery level
- next mastery level
- completion state when the next step finishes a track
- whether a Grand Doctrine Milestone is expected from track completion

The closing report should summarize the visible results of the batch.

The player-facing text should not expose:

- internal domain IDs
- adapter IDs
- track indexes
- temporary variables
- hidden AI scores
- transaction receipts
- queue internals
- hidden achievement checks
- unsupported doctrine families

## Event title and option direction

The catalog and event identity remain Doctrine Research.

Final option wording belongs to implementation. The following directions should guide it:

| Option family | Speaker and intent | Tone |
| --- | --- | --- |
| Open doctrine selection | The national command authorizes the staff to choose where the breakthrough is applied. | Plain, confident, institutional. |
| Select Army, Navy, Air, Special Forces, Chaos Warfare, or another domain | The service or command branch argues for its curriculum. | Concise, service-specific, lightly competitive when appropriate. |
| Adopt a Grand Doctrine | The government and high command accept a broad military philosophy. | Formal commitment with a clear note that the choice grants no mastery step. |
| Advance a track | The relevant school converts recent experience into the next mastery level. | Practical and specific to the unit family or operational role. |
| Return to a prior page | The staff reopens the current agenda. | Neutral navigation wording. |
| Close an exhausted batch | The staff confirms that no eligible doctrine work remains. | Matter-of-fact, without false compensation. |
| Batch summary | The country's military institutions record what was adopted. | Reflective and concise. |

Cultural references are unnecessary for the ordinary event. If implementation uses one brief service-specific allusion, it must be researched and must fit the country or doctrine involved.

## Dynamic localisation direction

The event needs dynamic text for:

- country name and flag
- batch size
- remaining choices
- doctrine domain name
- Grand Doctrine name
- track name
- subdoctrine name
- current mastery level
- next mastery level
- maximum mastery level
- branch completion state
- native Milestone state
- number of domains and tracks developed in the final summary

The display should use whole numbers for choices and mastery levels.

Important result types should have consistent visual treatment:

- remaining choices in a clear positive color
- Grand Doctrine adoption in the doctrine-domain color or a stable highlight color
- mastery advancement in the normal positive color
- branch completion and native Milestone activation in a stronger completion color
- blocked visible requirements in the normal blocked color

Color must be paired with a label or icon. The player should not need color alone to distinguish adoption, progress, completion, or invalid state.

## Event Details direction

Event Details should describe a worldwide period of military study and practical doctrine development.

It should explain that countries can establish a Grand Doctrine or advance one mastery level, and that evolutions increase the number of choices in one firing.

It should not list internal batch queues, exact AI factors, implementation history, stale catalog wording, or hidden achievement rules.

The evolution preview should state the batch size at each stage and preserve the distinction between mastery levels and native Grand Doctrine Milestones.

## History and evolution row direction

The History row represents one global doctrine wave. It has no country actor.

The row should communicate the date and Event 027 identity. Its detail view can state how many choices the current stage granted to each valid country.

Evolution rows should describe the widening curriculum:

- Evolution I establishes two separate choices
- Evolution II establishes three
- Evolution III establishes four
- Evolution IV establishes five

Final evolution names and descriptions should focus on the institutional scale of the doctrine cycle. They should not sound like a war, disaster, or scientific anomaly.

## Report-event image

Event 027 needs one reusable report-event image.

### Source mode

Generated period-authentic documentary scene.

The image is fictional and represents a general worldwide pattern. It does not depict one specific historical person, battle, or archive item. Generation fits better than using one country's real photograph as the visual identity for an event that affects every country.

### Scene direction

The image should depict a 1936 to 1945 joint-service field exercise or military school demonstration.

A strong composition includes:

- one clear officer, instructor, or staff focal subject
- infantry and artillery activity in the middle distance
- an armored vehicle or armored formation visible without dominating the scene
- aircraft overhead or an air liaison element
- a distant coastal, harbor, or naval cue when the composition can include it naturally
- maps, boards, manuals, range markers, radios, or observation equipment as secondary props
- period uniforms, equipment, vehicles, architecture, and photographic technology

The scene should feel active. It should show doctrine being tested and taught.

### Avoid

- a generic command table as the entire image
- a modern classroom
- modern uniforms, helmets, vehicles, aircraft, radios, or screens
- readable generated text
- flags or insignia that make the event belong to one country
- cinematic color grading
- futuristic holograms
- a collage or split panel
- a literal doctrine user interface
- a battle scene centered on death or destruction

### Target

Use the active Chaos Redux report-event reference and consumer to confirm the exact final canvas. The current asset skill identifies `210x176` as the standard report-event target used by the project. The implementation agent must inspect the local reference and sprite before production.

Recommended runtime path:

`gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds`

Recommended sprite identity:

`GFX_report_event_027_doctrine_research`

The final sprite name must follow the local report-event convention if it differs.

## Doctrine icon reuse

Choice pages should reuse the doctrine assets already owned by the doctrine graph:

- domain icons
- Grand Doctrine icons
- track icons when available
- subdoctrine icons
- native completion or Milestone indicators when the event surface can use them cleanly

Event 027 should not create replacement doctrine icons for vanilla or Chaos Warfare branches.

Every reused icon needs verified sprite ownership and a valid event-picture or option-icon consumer. A missing icon is an implementation finding. The event must not wire an unrelated focus, idea, or decision icon as a substitute.

## Achievement set

The event has three achievements. Their labels below are working labels for tracking and asset planning. Final titles and descriptions belong to implementation.

The set rewards the three defining uses of the event:

- establishing a doctrine and immediately beginning it
- concentrating a full evolved batch in one branch
- distributing an evolved batch across several tracks

The set avoids duplicating the official achievement for fully mastering all subdoctrines in a Grand Doctrine.

## Achievement 1: First Lesson

### Working key

`027_first_lesson`

### Role

Reward a country that uses one evolved batch to establish a Grand Doctrine and begin its practical mastery.

### Eligibility

- the current country is human-controlled when the batch begins
- the batch contains at least two choices
- the achievement has not already been unlocked
- achievements are enabled under the project's normal achievement rules

### Required route

1. During one Event 027 batch, use one choice to adopt a Grand Doctrine in a domain that had no active Grand Doctrine at batch start.
2. During a later choice in the same batch, select a subdoctrine in that same domain or advance one of its selected subdoctrines.
3. The later choice must create an event-attributed mastery step and leave the branch at Mastery I or higher.

### Disqualifiers

- the mastery step occurs in a different doctrine domain
- the mastery level comes only from combat, training, faction sharing, another event, a focus, a decision, or debug action
- the country loses the batch through annexation
- the player uses a debug or force-completion route that disqualifies achievements under project rules

### Difficulty

Medium.

The achievement requires Evolution I or higher and a country with an unselected valid domain.

### Tracking

Track the adopted domain and batch identity. Count only a later successful Event 027 mastery receipt in the same domain and batch.

### Icon direction

A closed field manual opened to its first marked lesson, with a small officer-school insignia, pencil, or pointer. The image should communicate the first practical step after choosing a doctrine. Use the achievement reference frame and state-triplet workflow.

## Achievement 2: Single School

### Working key

`027_single_school`

### Role

Reward maximum concentration during one Evolution IV batch.

### Eligibility

- the current country is human-controlled when the batch begins
- the batch contains exactly five choices from Evolution IV
- one eligible subdoctrine branch has five unearned event mastery levels at the start of the concentrated sequence
- the branch uses a verified five-level structure

### Required route

- direct all five Event 027 choices in the batch into the same subdoctrine branch
- every choice must produce one event-attributed mastery step in that branch
- the branch must be fully mastered by the end of the fifth choice

The first choice may select the subdoctrine in an empty track and grant its first event mastery step. A Grand Doctrine adoption does not count as one of the five mastery steps.

### Disqualifiers

- any choice adopts a Grand Doctrine
- any choice targets another domain, track, or branch
- the branch completes before all five Event 027 mastery receipts have been recorded
- banked mastery, faction sharing, combat, another event, focus, decision, or debug effect supplies one of the five required event-attributed levels
- the batch closes with an unused choice

### Difficulty

Hard.

The player must prepare a valid five-level branch before the late-chaos event fires and must commit the entire batch to it.

### Tracking

Store the first successful branch identity for the batch. Every later successful mastery receipt must match it. Track five Event 027 mastery receipts and verify full completion at batch close.

### Icon direction

Five lesson markers or five stacked doctrine tabs converging on one military-school crest. The subject should remain readable at 64x64 and should not resemble the official all-subdoctrine achievement.

## Achievement 3: Joint Curriculum

### Working key

`027_joint_curriculum`

### Role

Reward deliberate distribution across several military track categories.

### Eligibility

- the current country is human-controlled when the batch begins
- the batch contains at least four choices
- at least four distinct valid tracks can receive an event mastery step during the batch

### Required route

- record successful Event 027 mastery steps in four distinct track identities during one batch
- the tracks may belong to one Grand Doctrine or several doctrine domains
- Grand Doctrine adoption choices do not count as track development
- repeated development of one track counts once

A fifth choice in an Evolution IV batch may target any valid branch without disqualifying the achievement.

### Disqualifiers

- fewer than four distinct tracks receive event-attributed mastery steps
- one or more counted levels come only from another mastery source
- the country loses the batch through annexation
- project achievement rules disqualify the save

### Difficulty

Hard.

The country needs a sufficiently broad valid doctrine portfolio and must resist concentrating every choice in the highest immediate-value branch.

### Tracking

Use the current batch identity and a deduplicated set of track identities. Unlock at the fourth distinct successful Event 027 mastery receipt.

### Icon direction

Four service or track symbols arranged around one central curriculum binder, compass, or staff-college crest. The design should communicate coordinated study without using national flags or tiny text.

## Achievement visibility

All three achievements can be visible. Their descriptions should state the player-facing requirements clearly enough to support deliberate pursuit.

The implementation may hide Single School until Evolution IV is known when the project achievement framework supports hidden reveal without confusing the player. The default recommendation is visible because the event has no secret route.

## Achievement asset requirements

Each achievement needs the complete project triplet:

- completed icon
- grey or locked icon
- not-eligible icon

Achievement files remain in the root achievement folder under the full achievement ID, according to the project asset convention.

Recommended basenames:

- `027_doctrine_research_first_lesson`
- `027_doctrine_research_single_school`
- `027_doctrine_research_joint_curriculum`

Final IDs and filenames must match the root achievement registry exactly.

## Asset inventory

| Asset | Type | Source mode | Final consumer | Priority |
| --- | --- | --- | --- | --- |
| Doctrine Research report image | Report-event image | Generated period documentary scene | Human opening and summary event family | Required |
| First Lesson triplet | Achievement icon triplet | Generated icon art | Achievement registry | Required |
| Single School triplet | Achievement icon triplet | Generated icon art | Achievement registry | Required |
| Joint Curriculum triplet | Achievement icon triplet | Generated icon art | Achievement registry | Required |
| Doctrine-domain and branch icons | Existing doctrine assets | Reuse after graph and sprite inspection | Choice pages | Required reuse |

## Presentation acceptance

The event presentation is ready when:

- the opening report clearly explains batch size and choice types
- every consuming option states its result
- navigation never looks like a consuming option
- mastery level and native Milestone terminology remain distinct
- dynamic doctrine names and levels render without raw keys
- the report image matches the active report-event reference and period
- achievement icons are separate original assets with complete triplets
- reused doctrine icons resolve to their real owning sprites
- Event Details and evolution rows match the accepted batch sizes
- the final summary reports the batch without exposing hidden tracking
