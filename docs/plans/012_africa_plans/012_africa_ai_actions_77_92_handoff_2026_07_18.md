# Event 12 AI Actions 77-92 implementation handoff

## Scope

This tranche binds the existing 64-profile Event 12 AI registry to the foreign Scramble response, Actions 77 through 92, the three world-order route choices, and post-World administration. It does not claim that Actions 1 through 76 or 93 through 102 have live AI dispatch yet.

## Runtime path

1. The current AI host receives one zero-cost council decision every fourteen days while the Scramble, world order, or Event 12 World aftermath is active and action capacity is open.
2. The host composes its regional, constitutional, and full-playbook profile layers once.
3. Sixteen candidate actions are scored against phase, risk ceiling, partial tolerance, campaign context, and exact target availability.
4. A weighted action selects one target from an existing bounded Event 12 array.
5. The target contributes its relationship, foreign, high-chaos, or continent profile.
6. The shared action validator confirms phase, evolution, target semantics, retry policy, capacity, and dynamic cost.
7. The action launches through the same quote, mission, outcome, disposition, and cleanup kernel as a player action.

No daily, weekly, monthly, or autonomous country iteration was added.

## Matrix disposition

| Row | Action | AI target and campaign rule |
| ---: | --- | --- |
| 77 | Seek International Recognition | Prefers recognition candidates without colonial interests, excludes recognised governments and expedition leaders. |
| 78 | Prepare Anti-Sanctions Network | Requires a sanctions actor or recognition channel and raises priority during active sanctions. |
| 79 | Answer Foreign Ultimatum | Targets the recorded issuer and carries urgent priority. |
| 80 | Mobilise Continental Defence | Host action available only during the intervention phase. |
| 81 | Disrupt Expedition Planning | Targets a non-leading planner that is not already at war with Africa. |
| 82 | Offer Base Withdrawal Treaty | Requires a base holder and a peaceful negotiating state. |
| 83 | Call Global Anti-Colonial Conference | Host action available during the active Scramble response. |
| 84 | Break Intervention Coalition | Prefers low-stability or low-war-support coalition members before other members. |
| 85 | Sponsor Continent Unifier | Requires a unique implementation-ready package candidate and an open sponsorship gate. |
| 86 | Mediate Continent Union | Requires sovereign completion, consent, compatibility, and no active rivalry or war. |
| 87 | Prepare Continental War | Requires the terminal route, a reachable unresolved rival, and a valid war declaration. |
| 88 | Force Continent Submission | Requires a defeated recorded continental opponent. |
| 89 | Form Dynamic Two-Continent Union | Requires the completed mediation plan and a still-compatible consenting partner. |
| 90 | Declare the World Is One | Receives weight only when the full terminal trigger, including presentation readiness, passes. |
| 91 | Administer World Regions | Post-World only, against unresolved package actors, using the controlled capital region as the AI cursor. |
| 92 | Contain Terminal High Chaos | Post-World only, against registered hostile or breached high-chaos actors in maintained arrays. |

## Reachability repairs

- Action 85 can be scored while the sponsorship gate is open before the aftermath settlement. It no longer waits for the world-order flag that the package installation sequence is meant to unlock.
- Action 91's target trigger no longer requires both `world_end` to be absent and `world_end_africa_the_world` to be present.
- Terminal profile and phase checks preserve Actions 91 and 92 after the Event 12 World identity forms while still blocking unrelated world ends.
- State selection admits non-African states only for Action 91. Every other state and region action keeps its African-state restriction.
- The terminal and intervention peace checks now use the maintained package and Scramble arrays rather than scanning all countries.
- Direct player target selectors expose every maintained Scramble participant, package candidate, and installed continent actor without creating duplicate stores.

## Changed surfaces

- AI constants, MTTH context, profile triggers, profile effects, and the host AI decision
- shared action state and terminal phase validation
- bounded Scramble and world-order target triggers
- foreign response event AI chances and response-profile records
- world-route AI weights
- decision-category reachability and target-selection localisation
- `docs/events/012_africa_world_order.md`

## Remaining risks and open work

- The terminal World action still correctly cannot fire until the researched super-event image, final text, licensed audio, unique sound ID, slot, and scenario package set `africa_the_world_super_event_package_ready`.
- Actions 1 through 76 and 93 through 102 still need a live profile-driven dispatcher or equivalent bounded AI callers.
- Campaign simulation and the independent decision and completion audits remain required before the whole Event 12 AI surface can be accepted.

## Validation evidence

- The dispatcher contains sixteen initialized candidate weights, sixteen scored weights, and sixteen weighted-selection branches, one for every Action 77-92 row.
- Every newly added scripted-effect or scripted-trigger call resolves to a repository definition; the four new decisions each have one decision definition, one name key, and one description key.
- The touched script files have balanced scopes and quoted strings, and the added dispatcher contains no country-wide iteration.
- A narrow `africa_world_order.1` HOI4 event lint was requested twice after correcting the selector shape. The tool returned `ARTIFACT_STORAGE_LIMIT` before scanning files or producing diagnostics, so it is recorded only as a tool blocker and not treated as a passing validation result.

## Simplifications

No Action 77-92 concept was replaced, merged, or routed through a fallback. Target selection is bounded to implemented Event 12 stores. The open work above is outside this tranche and remains explicitly incomplete.
