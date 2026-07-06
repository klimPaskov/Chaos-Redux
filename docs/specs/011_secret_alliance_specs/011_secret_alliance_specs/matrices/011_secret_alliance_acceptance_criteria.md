# Secret Alliance acceptance criteria

## Core behavior

- Event 11 remains a minor fire-once event in the random event catalog.
- Initial pact creation chooses three valid countries that are not at war with the player.
- Initial selection prefers minors outside factions and avoids player subjects or special crisis actors.
- Hidden pact members have roles that influence incidents and AI behavior.
- The pact can invite more countries through staged ring membership.
- The player does not immediately know the full pact.
- Evidence and Preparedness matter after reveal.
- Pact Cohesion and Readiness matter after reveal.

## Evolution behavior

- Baseline progression is not logged as an evolution.
- Evolution I adds more minor network activity and supports both active-event and pre-fire evolved opening.
- Evolution II adds major patron behavior or starts as a major-founded pact if it first fires at that stage.
- Evolution II opens the player decision category.
- Evolution III makes the pact public, shows the faction, gives war options, and creates high war likelihood.
- If first fired under Evolution III conditions, the event opens through the Evolution II package before moving to public pact pressure.

## Decisions and missions

- Decision costs use varied concrete resources.
- Major decisions are not only political power or command power costs.
- Missions require actual action, such as unit placement, route protection, inquiry work, or resource commitment.
- Success, failure, and partial success exist for important actions.
- Decision category hides obsolete and invalid actions.
- Border actions only appear when a valid border or route exists.
- Hidden decisions clean up after public reveal.

## Reveal and war

- Any full pact country going to war with the player reveals the pact.
- Public reveal forms Anti-[player country] Pact.
- Full signatories join war on hard reveal.
- Outer-ring members evaluate join, withdrawal, or sympathy based on prior outcomes.
- Reveal fires the planned super-event once the super-event package is researched and wired.
- Hidden sabotage does not continue as hidden behavior after public reveal.

## Assets and super-event

- Super-event has researched title, button text, quote, audio, and image before implementation claims completion.
- Audio is unique, licensed or public domain, and documented.
- Asset package includes decision category icon, decision icons, idea icons, super-event image, achievement icons, and planned animated dossier or warning assets with static fallbacks.
- Generated or sourced assets follow asset skill source rules.

## AI and documentation

- AI uses motive-based and state-based behavior.
- AI does not join invalid members or take invalid border actions.
- Event Details, event log, evolution log, docs, localisation, and catalog wording align after implementation.
- Achievement unlocks require meaningful route success and have disqualifiers.
- Completion audit is run before completion claim.
- Near-completion improvement loop pass is run in the repository environment and its result is resolved.
