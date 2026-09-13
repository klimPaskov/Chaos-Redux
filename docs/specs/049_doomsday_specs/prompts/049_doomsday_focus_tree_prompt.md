# Event 049 Doomsday Focus-Tree Implementation Prompt

## Role

Implement the shared emergency focus content for countries that become Doomsday administrations under Evolution II.

Read:

- `specs/049_doomsday_spec_part_3_societies_and_responses.md`
- `specs/049_doomsday_spec_part_6_evolutions.md`
- `specs/049_doomsday_spec_part_7_focus_content.md`
- `specs/049_doomsday_spec_part_8_final_vigil.md`
- `specs/049_doomsday_spec_part_9_last_day_and_aftermath.md`
- `diagrams/049_doomsday_route_map.md`
- `prompts/049_doomsday_decision_mission_prompt.md`
- `prompts/049_doomsday_asset_prompt.md`
- `quality/049_doomsday_probability_scenarios.md`

Follow `AGENTS.md`, `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.

## Core architecture

Create a real 18 to 24 focus shared emergency branch or equivalent event-owned focus layer.

It becomes available only after a valid national Doomsday administration takes power.

Do not replace every country’s full national tree. Preserve existing completed history and compatible national content.

Do not add a focus inlay window. Doomsday Conviction and Time Until the End remain in the decision category.

The branch must adapt to:

- Country and government form.
- Takeover route.
- Dominant and secondary society currents.
- War and invasion state.
- Institutional continuity.
- Geography, ports, railways, islands, colonies, and occupied territory.
- Existing leaders, laws, parties, and national institutions.
- Famine, migration, disaster, contamination, and relief pressure.
- Final Assembly current preference.

A shared tree that uses identical text, targets, rewards, and AI in every country is incomplete.

## Focus durations

- Use a 7-day opener for the transfer of authority.
- Use 35-day focuses for urgent forks, institution transfers, and policy programs.
- Use 70-day focuses for broad demobilization, administrative restructuring, and major international commitments.
- Add accelerated alternatives or bypasses when the countdown is too short for normal completion.
- Do not divide one reward into several short focuses without a new choice or action.

## Required branch families

### Opening trunk

Implement a transfer-of-authority opener, a national inventory group, and a custodial mandate convergence.

The trunk should establish leadership, staged ideas, immediate decisions, and the remaining institutional state. It should not grant free reserves or buildings.

### Peace and Demobilization

Cover:

- The last muster.
- Orderly demobilization.
- Defensive-only civil protection.
- Prisoner and objector policy.
- Arms-line conversion.
- Armistice and Final Assembly peace eligibility.

Include a real fork between broad demobilization and retained defensive service.

### Bread, Shelter, and Records

Cover:

- Food and reserve distribution.
- Shelter projects.
- Hospitals.
- Archive duplication.
- Rail, port, and communications continuity.
- A reopening plan.

Unlock decisions and missions. Do not grant all buildings or relief instantly.

### Observance and Social Peace

Cover:

- Safe public vigils.
- Religious and civic cooperation.
- Reconciliation.
- Plural or centralized observance fork.
- Final-day communications and medical staffing.

Final localisation requires country and culture research. Working labels are not final text.

### Internal government fork

Create a meaningful mutually exclusive choice between:

- Communal Devolution.
- Custodial Administration.

Communal Devolution should strengthen local councils, relief, autonomous settlement, and Communal Stewards while weakening central command and taxation.

Custodial Administration should strengthen national distribution, records, continuity service, and Reserve Custodians while risking elite control and unequal access.

### Final Assembly Diplomacy

Cover:

- Delegation type.
- Common relief routes.
- Demobilization compact.
- Assembly current influence.
- Full membership petition.

A country under immediate invasion must retain a valid defensive route.

### Hidden Avenging Witnesses extension

Reveal only after severe suppression history and revolutionary takeover.

Cover:

- Prisoner release.
- Missing-person and evidence work.
- Tribunal or revolutionary punishment fork.
- Judgment and memory.

Do not reveal or weight this route without the required campaign evidence.

## Idea lifecycle

Use a small number of staged ideas. At minimum review the planned roles:

- Doomsday Administration.
- Hollowed Institutions.
- The Last Muster.
- Common Relief Network.
- Suppression Reckoning.

Upgrade, replace, mitigate, or worsen them through focuses and mission outcomes. Do not create one new national spirit per focus.

## Rewards

Major rewards should unlock or change:

- Decisions and missions.
- Military service and unit roles.
- Shelters, hospitals, storage, rail, ports, and archives.
- Relief and migration adapters.
- Leadership, council, party, and government identity.
- Final Assembly diplomacy and current influence.
- Failed-date recovery.
- Armistice and prisoner policy.

Flat political power, stability, War Support, and small modifiers may support these changes. They cannot be the main reward of important focuses.

## Layout

Use a compact first-glance layout.

Suggested lane order:

1. Peace and Demobilization
2. Communal Devolution
3. Central trunk
4. Custodial Administration
5. Bread, Shelter, and Records
6. Observance and Social Peace
7. Final Assembly Diplomacy as a lower convergence line

Place the hidden Avenging Witnesses extension below the internal-government area after reveal.

Use short direct connectors, clear branch roots, visible forks, and real capstones. Avoid ladders, zigzags, overlaps, crossed lines, and fake nonlinearity.

## Focus filters and navigation

Assign accurate current-engine search filters to every focus.

Use Focus Navigation shortcuts if the implemented tree region is large enough to need them. Candidate navigation families are peace and defense, relief and continuity, government form, and Final Assembly.

Do not reveal hidden content through filters or navigation.

## MCP workflow

MCP use is mandatory.

Before editing:

- Run `hoi4.focus_inspect` on the owning tree and loading rules.
- Render the relevant full tree and current branch context with `hoi4.focus_render`.
- Inspect vanilla and Chaos Redux loading precedents.

During implementation:

- Use bounded `hoi4.focus_rewrite` where appropriate.
- Review every returned layout and diagnostic.
- Render at normal in-game zoom with real titles and icons.
- Repeat until every branch, fork, convergence, and capstone is clear at first glance.

After implementation:

- Inspect and render again.
- Compare the final structure.
- Treat MCP failure as a blocker. Source-only review is not equivalent.

## AI and probability

Create route-specific AI plans for:

- Custodial stabilizer.
- Communal federation.
- Pacifist demobilizer.
- Devotional reconciler.
- Revolutionary reckoning.

AI must consider war, invasion, institutions, movement currents, takeover route, remaining time, relief pressure, and Final Assembly state.

Run the mandatory probability baseline, patch, and compare cycle through `chaosx_ai_probability_auditor` using `FOCUS-01` through `FOCUS-06` in the probability scenario file.

## Assets and localisation

Use dedicated focus icons from the asset prompt. Do not reuse or resize decision or idea icons.

Write final country-aware localisation from the specification direction. Avoid generic route text and hidden mechanic exposure.

Leader, council, party, cosmetic identity, and portrait changes must match the country package. Grounded individuals use sourced portraits.

## Audit and completion

After implementation, spawn `chaosx_focus_tree_auditor`.

Require a route coverage table with:

| Required route | Implemented branch | Status | Notes |
| --- | --- | --- | --- |

The audit must cover:

- Branch depth.
- Prerequisites and mutual exclusions.
- First-glance layout.
- Filters and navigation.
- Decisions and mission links.
- Idea lifecycle.
- AI and probability evidence.
- Country adaptation.
- Icons and localisation.
- Countdown pacing and bypasses.
- Hidden-route safety.
- Failed-date aftermath links.

Do not claim completion with a shallow reward ladder, generic shared text, missing AI, missing icons, missing decision links, or unreadable layout.
