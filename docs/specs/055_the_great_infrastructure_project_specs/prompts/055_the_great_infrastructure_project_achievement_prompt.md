# Achievement Implementation Prompt for Event 55

Implement the complete Event 55 achievement set after the project system and persistent project records exist.

Read the Event 55 source specs, `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and the existing Chaos Redux achievement registry and localisation patterns.

All names below are working labels and require a final player-facing writing pass.

## Achievement 1, From Sea to Sea

- Eligible country: player-controlled Event 55 project host
- Unlock: complete one full-scope coast-to-coast railway or highway across a large connected state route, with distinct distant coast endpoints, then keep it Operational for `365` consecutive days
- Disqualifiers: reduced completion, abandonment, transfer from another host, route severed during the sustain period
- Difficulty: Hard
- Tracking: project generation, host, primary family, route-state count, distinct coast proof, full completion, continuous operation
- Icon direction: locomotive or convoy joining two coastlines across one continental span

## Achievement 2, No Mountain Is High Enough

- Eligible country: player-controlled host of an Evolution II extreme mountain project
- Unlock: complete a full-scope mountain railway, highway, bridge, or tunnel without foreign financier aid, without reducing scope, and after resolving every major engineering defect
- Disqualifiers: foreign bailout, abandonment, reduced route, repeat-firing completion assistance after main construction begins
- Difficulty: Very hard
- Tracking: evolution state, extreme terrain proof, finance sources, incident outcomes, assistance history, final status
- Icon direction: high viaduct or bridge crossing a mountain cut

## Achievement 3, Steel Thread of Nations

- Eligible country: player-controlled host of an international corridor or continental network
- Unlock: complete a full route with at least four sovereign participants and keep it Operational for `730` consecutive days with no participant withdrawal or war among core participants
- Disqualifiers: participant count falls below four, route becomes Dormant or Severed, host annexed before completion of the sustain period
- Difficulty: Very hard
- Tracking: core participant identities, sovereign status, agreement generation, war state, withdrawal, continuous operation
- Icon direction: four steel route segments converging into one junction

## Achievement 4, Master Builder

- Eligible country: player-controlled country with the Event 55 program
- Unlock: complete five projects with five distinct primary families, including at least one international project and one Evolution II or III project, repair at least one damaged project, abandon none, and keep every counted project at Strained or better
- Disqualifiers: counted transferred projects, multimodal double counting, duplicate project generations, any abandonment by the country
- Difficulty: Extreme
- Tracking: primary family ledger, host identity, completion status, international flag, evolution tier, repair history, abandonment history
- Icon direction: engineer's compass over rail, bridge, port, and tunnel symbols

## Achievement 5, The Relief Artery

- Eligible country: player-controlled host of a relief-priority project
- Unlock: while a genuine Famine or Migration request is active, complete a new relief-priority railway, highway, port, or international corridor before the owning crisis reaches its worst stage, receive a valid improved-access receipt from the owning system, and sustain operation for `180` days
- Disqualifiers: preexisting route with no new completion, no relief-priority commitment, owning system rejects route safety, route severed or abandoned during sustain period
- Difficulty: Hard
- Tracking: humanitarian request generation, project authorization date, relief priority, owning-system receipt, crisis stage, continuous operation
- Icon direction: freight train or truck convoy approaching a relief depot over a bridge

## Implementation rules

- Give every achievement a stable repository-compliant ID.
- Implement tracking flags and variables once and guard every completion record against duplication.
- Continuous operation timers reset when the route leaves the required status.
- A transferred project does not satisfy a host-built achievement unless the achievement explicitly allows it.
- One project has one primary family for achievement counting.
- No achievement unlocks from the event firing alone.
- Write final title and description localisation from the direction above.
- Create and wire completed, grey, and not-eligible icon variants through the asset prompt.
- Document the trigger, disqualifiers, tracking, and test scenarios.
- Add achievement-specific acceptance cases to the Event 55 completion audit.
