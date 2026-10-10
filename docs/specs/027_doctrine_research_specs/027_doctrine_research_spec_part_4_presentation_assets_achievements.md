# Event 027: Doctrine Research

## Part 4: Presentation, assets, and achievements

## Writing direction

Doctrine Research reads as a positive military-institution event about general staffs, service schools, field instructors, translated manuals, after-action studies, and live exercises.
"Research" means study, trial, and doctrine writing, never scientists in a laboratory.

Useful images include officers returning from the front with corrected field manuals, training formations testing revised methods, naval staffs comparing convoy results, air commands revising mission doctrine, joint schools arguing over which lesson to adopt, and CBRN staffs turning protection and logistics evidence into doctrine.
The tone stays restrained.
Mild irony can come from service rivalry, duplicated manuals, or officers claiming ownership of a successful lesson, never from casualties.

| Option family | Speaker and intent | Tone |
| --- | --- | --- |
| Choose a domain | A service argues for its curriculum. | Concise, service-specific, lightly competitive. |
| Establish a Grand Doctrine | Government and high command accept a broad military philosophy. | Formal commitment that names the cost of one choice and no mastery step. |
| Advance a track | The relevant school turns recent experience into the next level. | Practical and specific to the unit family. |
| Navigation | The staff reopens the agenda. | Neutral. |
| General staff (R5) | The national command leaves the remaining choices to the staff. | Plain and confident. |
| Nothing left to study | The staff confirms that no eligible doctrine work remains. | Matter-of-fact, without false compensation. |
| Summary | The institutions record what was adopted. | Reflective and brief. |

The player-facing word for a batch is curriculum (part 1, Terminology).
Text never says batch, receipt, adapter, queue, or implementation history.

## Visible values

The planning rule is one or two visible values per surface, three when needed, four at most.
Internal state, such as receipts, queues, scores, and stage numbers, stays internal.

| Surface | Implemented values | Target values |
| --- | --- | --- |
| Domain option | Grand Doctrine or unselected state, next action, tracks ready | Grand Doctrine or "no Grand Doctrine", and a marker when a track is one step from its Milestone (R7) |
| Track option | Held subdoctrine, current level, maximum, next level; tooltip adds completion state and Milestone state | Held subdoctrine and "Mastery 2 -> 3", plus a completion line only when this step completes the track and its Milestone (R7) |
| Result | Subdoctrine and level reached, or doctrine established, and choices remaining | Unchanged |
| Summary | Stage, choices offered, adoptions, mastery levels, domains developed, tracks developed, concentration, Milestone reached | One line per action taken and the Milestones reached (R6) |

### R6. The summary lists outcomes instead of statistics (pending)

The implemented summary shows eight counters, and none of them changes what the player does next, because the curriculum is already over.
The revised summary lists each action in order, such as "Established Fleet in Being" or "Mobile Infantry reached Mastery 4", and names any Grand Doctrine Milestone reached.
Distinct-domain counts, distinct-track counts, and the concentrated or distributed label are removed; the achievement checks that read them stay internal.

### R7. Option labels show only what decides the click (pending)

The track count and the "next action" label on domain options repeat what the next page shows.
The decision-relevant fact on the domain menu is whether a track there is one step from completing, so that marker replaces them.
On track options the completion and Milestone states matter only when this step finishes the track, so they appear only then, as one line.

## Event Details and History (implemented)

Event Details describes a worldwide period of military study, states that a curriculum grants one to five choices, and that a choice establishes a Grand Doctrine or advances one subdoctrine by one level.
The four evolution previews state the curriculum size of each stage.
The History row of each firing states how many choices every participating country received.
Evolution rows name the curriculum stage and its size and never read like a war, disaster, or anomaly.

## Report-event image (implemented)

`GFX_report_event_027_doctrine_research` uses `gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds`, registered in `interface/027_doctrine_research.gfx`.
It is a generated, internationally neutral, period-authentic joint-service field exercise with an instructor focal subject, infantry and artillery activity, an armoured vehicle, aircraft overhead, and maps or observation equipment as secondary props.
It avoids readable generated text, national insignia, modern equipment, a lone command table, and battle carnage.
Provenance and review are in `docs/assets/027_doctrine_research/manifest.md` and `gfx_handoff.md`.

## Doctrine icons (implemented)

Choice pages reuse the native domain, Grand Doctrine, track, and subdoctrine icons, including the Chaos Warfare icons.
Event 027 creates no replacement doctrine icons and never substitutes a focus, idea, or decision icon for a missing doctrine icon.

## Achievements (implemented)

The three achievements reward the three defining uses of a curriculum: establishing a doctrine and immediately beginning it, concentrating a full curriculum in one branch, and spreading one across several tracks.
None duplicates the native Doctrine of Choice achievement, which requires mastering every subdoctrine of a Grand Doctrine.

Shared rules:

- the country is human-controlled when the curriculum begins
- evidence comes only from consumed Event 027 receipts of the active or closing curriculum, never from final doctrine state
- native mastery, faction sharing, focuses, decisions, other events, and debug grants never count
- debug, console, cluster-forced, and test-country setups make a campaign ineligible
- annexation before completion leaves the achievement locked
- delegated choices (R5, pending) count as the country's own receipts

| Achievement ID | Title | Requirement |
| --- | --- | --- |
| `027_doctrine_research_first_lesson` | First Lesson | In one curriculum of at least two choices, establish a Grand Doctrine in a domain that was empty when the curriculum began, then advance a subdoctrine in that same domain with a later choice. |
| `027_doctrine_research_single_school` | Single School | In one Evolution IV curriculum, spend all five choices advancing one branch one level each, ending at level 5. No choice may adopt a Grand Doctrine, target another branch, or rely on banked or native progress for one of the five levels. |
| `027_doctrine_research_joint_curriculum` | Joint Curriculum | In one curriculum of at least four choices, advance four distinct tracks through Event 027 steps. Repeat steps on one track count once, adoptions do not count, and Special Forces progress counts per subdoctrine because one subdoctrine can occupy either native track. |

Single School needs a branch with five unearned levels when the Evolution IV curriculum fires, so the player has to prepare it.
Army and Chaos Warfare share the `land` folder, so Joint Curriculum spreads across one land Grand Doctrine plus naval, air, or Special Forces tracks, or four tracks of one Grand Doctrine.

Each achievement has a completed, grey, and not-eligible icon in `gfx/achievements/`, registered as `GFX_achievement_<id>` with `_grey` and `_not_eligible` variants in `interface/chaosx_achievements.gfx`.
The icons show a field manual opened at its first marked lesson, five doctrine tabs converging on one school crest, and four service symbols around a curriculum binder.
