# Event 080: Airship
## Part 7: Map and presentation

## The existing voyage map

Retain the existing dynamic map and its geographical route. The inspected event GUI uses the `airship_scripted_gui` decision-category window and a map sprite selected from the `GFX_airship_trail_` family by voyage position. That establishes an existing presentation to preserve. It does not prove that its current state binding or final-frame lookup is correct.

The revised event-owned window has four clear areas: the route map, the ship and Condition summary, the current host or open-water location, and the active task panel. Native controls and live values sit over or beside the map. Text, buttons, and changing numbers must not be painted into a flat background image.

The map shows completed route segments, upcoming segments, original planned stops, the actual airship position, and a visible indication of delays or diversions. Normal flight advances the marker once per two-day progression transition. Repairs and refits hold it in place. A temporary diversion has its own branch and actual location while the fixed canonical path remains visible.

Do not add a decorative category picture alongside this interactive map. The map already provides the visual identity and the necessary state information.

## What the player sees

| Area | Persistent content | Contextual detail |
|---|---|---|
| Route map | Current position, completed path, upcoming path, planned stops | Diversion branch, missing-contact segment, crash location, fire handoff |
| Ship panel | Physical form, Condition, people aboard | Damage concern, passenger and crew split, evacuation status |
| Location panel | Current actual host and state, or verified open water | Occupation change, denied service, local hazard, host responsibility |
| Task panel | Three to five relevant actions | One to three active missions, real costs, expected delay, default emergency response |

The main three values remain Condition, route progress, and people aboard. Elapsed days and extra delay can appear together in the route tooltip. Experiment context, unresolved passengers, and casualty components are expanded information. The interface does not expose every internal counter as a new status bar.

The host's view explains its own choices and costs. It does not show American private passenger decisions as if they were host controls. The public map can be viewed by other players without granting them authority to change the flight.

## Missing contact

Radio loss changes the public information display. The last known marker remains at the last confirmed position, with the unconfirmed continuation clearly distinguished. The internal actual ship position continues to exist and determines any physical event.

A later contact report moves the public marker to the verified current position. A wreck discovery identifies the actual impact location. The display never treats a last-known position as a confirmed crash location merely because it is easier to draw.

The tooltip separates confirmed deaths, people reported missing, and recovered survivors. An unresolved loss does not show an invented exact death toll or a completed route.

## Ship visual forms

Produce normal, damaged, and critical-condition variants for the baseline ship, Grand Tour ship, and Flying City. Experimental Flight adds a clearly readable equipment variant or attachment treatment to the current physical form. The variation must remain readable at the actual map marker and panel sizes.

Baseline is a large passenger airship with a clear silhouette. Grand Tour visibly expands passenger accommodation and public-facing facilities. Experimental fittings should read as instruments, antennae, or technical structures without turning the ship into an armed bomber. Flying City uses a larger, recognisably related hull with a few large facility groups. Avoid filling the image with tiny windows and machinery that disappear at game scale.

Damaged variants show specific repairable harm without changing the entire ship's identity. Critical variants show visible structural or mechanical problems and a clear status treatment. A wreck variant is distinct from a damaged ship. A ship safely written off on the ground does not reuse an airborne fireball.

The initial asset set contains twelve base presentation combinations: baseline, Grand Tour, experimental-equipped Grand Tour, and Flying City, each in sound, damaged, and critical states. If the approved evolution lifecycle permits a different experimental physical form, add that form explicitly to the manifest rather than reusing an inaccurate silhouette. Small marker versions are exported separately from the larger ship-panel art.

## Movement and animation

The route changing every two days is game-state progression. It is not a requirement to animate all 121 transitions as a video. Preserve the existing map assets wherever they already provide the correct path, and add the native marker and state layers needed for clear live information.

Optional ambient motion is limited to a small propeller or exhaust loop while underway and an appropriate smoke or flame loop during an actual emergency. Such motion needs genuine authored frames, a static fallback, and validation through the frame-animation skill. Pulsing or moving a flat whole image does not establish a valid animation pipeline.

Reduced-motion or unsupported animation should leave every gameplay state readable. The ship's condition and location must never be communicated only through motion.

## Event and news image set

All proposed asset labels are neutral production labels, not final event titles.

| Group | Required scene directions | Intended use |
|---|---|---|
| Reports | Departure, ordinary flyover, planned service, passenger interior, public reception, inspection, technical work, medical transfer | Routine and intermediate country events |
| Emergencies | Damaged approach, radio search, forced landing, impounded ship, rescue, grounded write-off | Country response events and aftermath |
| Terminal reports | Safe homecoming, baseline or Grand Tour crash, Flying City crash, ocean loss | Clear ending distinctions |
| News | Departure, major landmark arrival, diplomatic impoundment, serious emergency, confirmed disappearance, major crash, successful completion | Occasional global coverage |
| Super-event | Confirmed large Flying City crash at the actual geographic type | Rare global catastrophe presentation under the gate below |

A generic healthy ship photograph cannot represent a Flying City crash or a rescue operation. An image need not be unique to every minor passenger anecdote, but different major outcomes require suitable scenes. Fictional high-chaos forms should normally be generated, while sourced historical photographs can inform grounded production references and ordinary scenes where licensing permits.

Country report images use the project's 210 by 176 slanted-card format with the required processing and transparent corners. News images use the 397 by 153 monochrome format. Super-event art uses the 457 by 328 format. Decision icons are 32 by 32 and idea icons 64 by 64. Achievement icons use the exact 64 by 64 shared templates and runtime path contract. The asset prompt contains the production and verification requirements.

## News cadence

Use a departure report, at most three ordinary landmark reports spread across the voyage, and one terminal report. Allow at most one additional non-terminal serious-incident news item unless a genuinely separate later major event requires world coverage. Routine flyovers, every host change, and repeated repairs never qualify.

A serious accident, major impoundment, confirmed disappearance, or crash can bypass the ordinary landmark cooldown. It still uses one causal record. A crash, its retaliation, and its immediate casualty statement belong in a coordinated news package, rather than three global popups repeating the same facts.

If a later rescue substantially changes the confirmed toll, update the event's own record and give the involved countries a follow-up. A second worldwide report requires a genuinely major discovery, such as finding many previously missing people alive. The existence of a new counter value alone is not sufficient.

## Rare Flying City super-event

Plan one optional high-chaos super-event for a Flying City crash with at least 5,000 confirmed direct impact and rescue deaths and extensive immediate state destruction. The physical city form must already have been operating, the actual event must be a crash, and the death threshold must use confirmed people rather than capacity or unverified missing counts.

The presentation fires once for that voyage after the qualifying facts exist. If the threshold is crossed during the immediate four-day rescue period, it can fire on confirmation. Later unrelated fire deaths do not retroactively turn an ordinary impact into this Airship-owned super-event. Event 013 retains its own major-disaster presentation rules.

The image focuses on the loss of a civilian flying settlement and the actual type of impact location. It must not imply a nuclear explosion or place an invented city landmark in the wrong state. Final title, description, button text, quote or cultural remark, and audio require the dedicated research workflow. This spec supplies no finished quotation, title, lyric, or audio track.

The event uses the existing shared super-event framework. There is no new world-end state and no stop to normal automatic events solely because this presentation plays. Global Chaos reaching 1,000 elsewhere still follows the shared world-end rules.

## Localisation direction

The opening should explain civilian ambition, route length, responsibility, and visible management. Host text should name the actual controlling country and state where supported. A colonial owner, displaced government, or historic ruler must not speak as the current host when it has no control.

Passenger text should use people with clear everyday concerns. The final writing can be dry or amused about booking mistakes, bureaucracy, rival receptions, and impatient travellers. Serious injuries, missing people, deaths, and rescue use precise language without jokes that obscure the outcome.

American crash text must report immediate retaliation and distinguish accusation from established cause. The host's report should reflect both its actual local losses and the new war. Successful completion should recognise delivered repairs, successful visits, and recovered data, with no claim that every country welcomed the voyage.

All numerical tooltips reflect actual current results. A new cost, passenger count, or delay must be visible before a choice commits it. Final localisation is written during implementation from these directions, then audited for dynamic scope, grammatical variants, and misleading certainty.

## Presentation acceptance

Review departure, open water, an occupied host, a normal stop, damage, critical Condition, a repair hold, an active trial, a diversion, radio loss, each physical evolution, an intact capture, domestic crash, foreign crash, Flying City catastrophe, and successful completion.

Match these states at the supported resolutions, including 1920 by 1080 and 2560 by 1440 unless the project defines a narrower supported set. Test long country and state names, large casualty counts, and translated text expansion. An unclickable control hidden by the map is a failure even if a still image looks attractive.

Before native implementation, create and review reference images for the event-owned layout. Afterwards, inspect the real GUI hierarchy and render matched scenarios. Reference-image review, native element mapping, hit regions, and final comparisons must all agree. No screenshot, asset filename, or planning image alone proves that the actual GUI works.
