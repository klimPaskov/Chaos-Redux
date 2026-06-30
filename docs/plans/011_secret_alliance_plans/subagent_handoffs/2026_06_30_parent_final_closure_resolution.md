# Event 011 parent final closure resolution

Date: 2026-06-30

Scope: parent implementation pass after the decision, localisation, completion, and improvement-loop audits.

## Resolved audit items

- Replaced fixed Dossier Board meter fills with thresholded evidence, pressure, and preparedness fill elements. The scripted GUI now exposes 25, 50, 75, and 100 percent states for each live value.
- Tightened timed mission success predicates around concrete state and route checks. Capital, industrial, foreign-route, patron, and public-border missions now require relevant controlled states, local divisions, route assets, trains, fuel, or no-route fallback conditions.
- Added stability gates for decisions that spend stability and separated the local defense committee stability spend from the settlement exit spend.
- Added public leader repair before public war calls and during lifecycle refresh. The repair order is patron, founder, then another valid public member.
- Added compact closure cleanup when no valid public members remain.
- Guarded public reveal so it cannot broadcast a public pact without at least one valid public faction member. If no valid public member exists at reveal time, the compact records defeat-state cleanup and closes instead.
- Added a capitulation lifecycle refresh hook for the target-side compact and guarded the preemptive-strike effect so it repairs public leadership before spending resources or declaring war.
- Moved Event 011's public reveal super-event from conflicting slot `11` to slot `28`, restored Holy Realm Divine Sovereignty on slot `11`, and added the slot `28` music, sound, scripted-localisation, track-list, and documentation rows.
- Implemented the evolved-start major patron-founder path. Evolution II or III starts still found the compact through three valid minor founders, then add a valid major patron as hidden patron-founder before the accelerated counterplay and reveal schedule.
- Added state-control tracking for the no-core-loss war-case achievement predicate.
- Updated localisation, event documentation, and source specs to describe the concrete mission and board behavior.

## Asset correction

The interim achievement and animated icon packages that were not imagegen-backed were discarded. Final achievement icon triplets, animation source sheets, frame sheets, static fallbacks, previews, contact sheets, manifests, and handoff notes now point to the regenerated imagegen-backed packages.

## Implementation note

The improvement addendum suggested persistent objective-state flags. The parent implementation uses direct dynamic state predicates instead. This keeps the mission checks current, avoids stale state flags after border or controller changes, and still satisfies the state and route objective requirement.

## Remaining risk for final audit

- No noninteractive HOI4 script parser is shipped with the repository or vanilla documentation set, and the game runtime is an interactive application rather than a command-line validation pass. Static validation, file-format checks, workbook checks, and targeted subagent audits are the available evidence before user live-session verification.
