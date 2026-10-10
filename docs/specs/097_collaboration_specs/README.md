# Event 097 Collaboration Specification Package

Event 097 Collaboration is a Minor Repeatable event at Chaos level 1 and a Medium member of the Intelligence cluster.
Each firing gives every country a layer of native collaboration inside every other country, and four evolutions turn those networks into deeper recruitment, prepared local administrations, an internal fifth column, and installed collaboration governments.
Both designs below keep the existing `chaosx.nr97` namespace and the `chaosx.nr97.1` entry event.
Neither is implemented; the legacy script is `events/097_collaboration.txt`.

## Start here: two design variants

This folder holds two separately authored designs for the same event.
**The flat variant is the design.** The orchestrator selected it on 10 October 2026 within the user's planning-package brief, and the nested variant is `superseded` by it; its files stay below as historical design and are not implementation inputs.
Use only the flat files and the root-level prompts. The [conflict table](#where-the-variants-conflict) records what each variant chose; the flat column is authoritative.

| | Flat variant (`COL-097-DESIGN-1`) | Nested variant |
| --- | --- | --- |
| Design in brief | Every firing adds one uniform native collaboration layer (10, 20 after I, 25 after II or IV) to every directed country pair before any report, with no player choice, decision, spirit or new value. The evolutions only change what native collaboration does: a one-time compliance handover on capture (II), two one-time native breakthroughs as a losing country nears its capitulation threshold (III), and a once-per-defeat push toward the native collaboration-government route (IV). | Every firing adds a 15-point layer (25 after I) scaled by a stance each country picks in the opening report (Accept, Cultivate, Screen), applied by a batched multi-day pass. The evolutions add band-based state seats, a three-band Fifth Column national spirit with Open Gates state handovers, two decision categories, installed governments with auxiliaries and a four-stage Installed Administration spirit, Turned Regime defections, and a Competing Orders super-event. |
| Entry document | [Specification index](097_collaboration_spec_index.md) | This README, [Nested variant files](#nested-variant-files) |
| Specification | Root-level `097_collaboration_spec_part_1_core.md` through `097_collaboration_spec_part_10_acceptance.md` | `specs/097_collaboration_spec_part_1_core.md` through `specs/097_collaboration_spec_part_6_ai_presentation_achievements.md` |
| Supporting design | None in this folder; capability gates, contracts and probability scenarios are in `docs/plans/097_collaboration_plans/` | `matrices/`, `research/`, `handoffs/`, `quality/` |
| Prompts | Root-level `097_collaboration_coding_prompt.md`, `097_collaboration_asset_prompt.md`, `097_collaboration_achievement_prompt.md`, `097_collaboration_goal_prompt.md` | `prompts/` coding, goal, asset, super-event, achievement, decision and mission prompts |
| Achievements | Six `chaosx_097_*` challenges (flat Part 9) | Six `097_collaboration_*` challenges (nested Part 6) |
| Acceptance record | [Decision register](../../plans/097_collaboration_plans/097_collaboration_decision_register.md), parent choices of 5 October | [Plan dispositions](../../plans/097_collaboration_plans/097_collaboration_plan_dispositions.md), parent choices of 6 October |
| Provenance | `package_metadata/` holds the original archive receipt (historical) | `docs/plans/097_collaboration_plans/097_collaboration_source_inventory.md` |

Both acceptance records are parent-authored expansions of the brief, not user approval of every number, and neither establishes a merged design or engine feasibility.

## Shared identity

The current Intelligence cluster identifier is **20**, using `constant:event_cluster_id.intelligence` from `common/script_constants/event_cluster_constants.txt`.
The [identifier audit](../../plans/repo_cleanup/specification_package_audit_2026-10-07/handoffs/identifier_overlaps.md) confirms 20 on the canonical event-catalog `Clusters` sheet; ID 9 belongs to National Breakthroughs and ID 8 to Diseases.
The [shared identifier registry](../shared_identifier_registry.md) records that both variants share the `chaosx.nr97.1` root.
The Intelligence cluster is Fire-Once with repeatable members, so a consumed cluster does not stop Event 097 from firing alone later.

Both variants must also respect two current shared systems:

- The Fallout transition (`common/scripted_effects/fallout_consolidated_effects.txt`) snapshots and resets every collaboration pair and then proves the world clean, so Event 097 stops selecting, granting and writing collaboration once that transition begins.
- [Event 052 Intel Leaked](../052_intel_leaked_specs/specs/052_intel_leaked_spec_part_5_evolutions_repeatability_and_connections.md#event-097-collaboration-connection) reserves one hook in which exposed contact chains can reduce an existing collaboration network without creating a new system.

## Explicit user decisions

These come from the [original brief](../../plans/097_collaboration_plans/097_collaboration_original_brief.md) and are fixed in both variants:

- Event 097 Collaboration is Minor Repeatable at Chaos level 1, in the Intelligence cluster as a Medium member, with status To Be Reworked.
- Every country gains collaboration against every other country, globally and symmetrically, through the normal collaboration mechanic, ignoring ideology, alliances, relations, and plausibility.
- The event is repeatable; each firing deepens the networks, and values stack only as far as the normal system allows.
- There is no separate Collaboration currency or large event-specific management system. The normal collaboration mechanic is the event.
- The four evolutions, their names, their Chaos requirements of 200, 400, 600, and 800, and their described behavior.
- The connection to Event 095 Occupation Revolt, where installed governments can become targets of a national restoration uprising if enough opposition survives.
- The connection to [Event 093 Treaty of Tordesillas Restoration](../093_treaty_of_tordesillas_restoration_specs/README.md), whose spheres can rely on collaborator governments.

## Where the variants conflict

Each row needs one choice before dependent implementation; the 10 October proposal below would settle all of them at once.

| Conflict | Nested variant | Flat variant |
| --- | --- | --- |
| Baseline layer and symmetry | Part 1: 15 points, 25 with I, modified by the Accept, Cultivate and Screen stances | Parts 1-2: uniform 10/20/25-point layers granted before any acknowledgment |
| Special-country eligibility | Part 1 excludes all nonhuman and special Chaos actors through shared classifiers | Part 1 includes unusual political countries whenever the native backend supports them and requires each incompatibility to be named |
| Evolution II | Seats begin at a 15-point network and use band-based compliance and resistance values | Requires C of at least 50 and offers F = min(80, C + 20) once per sponsor, target and state |
| Evolution III | Fifth Column national spirit, Open Gates and four wartime countermeasure decisions | Two staged native collaboration grants near defeat; a generic surrender spirit is rejected (register D24) |
| Evolution IV and connections | Turned Regime, Installed Administration lifecycle, restoration-pressure points, explicit decisions, Event 052, 063 and Fallout links | Native readiness offer and bounded Event 095, 093, 052 and Fallout connections |
| Chaos and presentation | Matrices define recurring outcomes, a rolling cap and the Competing Orders super-event | Parts 7-8 define one manifestation entry with a breadth increment, five reports and no super-event |
| Achievements | Six `097_collaboration_*` challenges | Six different `chaosx_097_*` challenges; do not merge the twelve by accident |
| Conditional omission | Part 6 and disposition R8 remove blocked Open Gates and Turned Regime surfaces together | Prompts prohibit hidden simplification; an omission needs recorded approval |

## Nested variant files

Specification:

- `specs/097_collaboration_spec_part_1_core.md`: participants, layers and stances, the opening report, the application pass, records, public readings, Event Details, cleanup
- `specs/097_collaboration_spec_part_2_evolutions.md`: Deep Networks, Administrations in Waiting, The Fifth Column, Collaboration Governments
- `specs/097_collaboration_spec_part_3_occupation_capitulation_and_governments.md`: network bands, prepared cadres, seated administrations, the Fifth Column, Open Gates, prepared governments, the Installed Administration lifecycle, Turned Regime, competing orders
- `specs/097_collaboration_spec_part_4_decisions_and_responses.md`: Divided Loyalties, Prepared Governments, Collaborators Unmasked
- `specs/097_collaboration_spec_part_5_connections_and_cluster.md`: the public contract and the links to Events 095, 052, 039, 063 and 093, the Intelligence cluster, and Fallout
- `specs/097_collaboration_spec_part_6_ai_presentation_achievements.md`: AI, presentation, the Competing Orders super-event, achievements, DLC compatibility, balance review

Matrices, research, handoffs, and quality: `matrices/097_collaboration_chaos_impact_map.md`, `matrices/097_collaboration_ai_probability_scenarios.md`, `matrices/097_collaboration_edge_case_matrix.md`, `research/097_collaboration_research_notes.md`, `handoffs/097_collaboration_localisation_direction.md`, `handoffs/097_collaboration_catalog_alignment.md`, `quality/097_collaboration_acceptance_criteria.md`.

Its parent acceptance covers the stance choice, layer sizes, the band ladder, every number, both decision categories, Collaborators Unmasked and its national version at restoration, Open Gates, Turned Regime, the Installed Administration lifecycle, local auxiliaries, the restoration pressure contract, the Event 052 and 063 links, the single Tordesillas entry point, the Chaos impact map, the super-event and the achievements.
All numbers are tuning anchors that must pass the balance and probability reviews named in the variant.
Payment rules that depend on what a country holds, such as trains or trucks for A3 and convoys or trucks for A5, are accepted design and not fallbacks.

## Open questions

### Variant selection (resolved)

Disposition: the flat variant is accepted and the nested variant `superseded`, by orchestrator decision on 10 October 2026; the audit proposal and its reasoning follow.
Ported into the flat parts: the named special-country incompatibilities and the bounded daily application pass (Part 1), the two reports to a displaced government (Part 5), and the national Purge or Amnesty choice at restoration (Part 6), with acceptance cases in Part 10.
Not ported: the Competing Orders super-event; the flat variant keeps its single manifestation report and no super-event.

The flat variant follows the brief's closing rule, that the normal collaboration mechanic is the event, much more closely.
Every value it shows is native (collaboration, compliance, the collaboration-government route), every evolution changes what that native value does, and its register already rejects a surrender spirit, a management surface and a generic puppet fallback.
The nested variant answers the same brief with a per-firing stance popup for every country, a vetting spirit family, a Fifth Column spirit with up to seven modifier lines, five host and two installer decisions, auxiliary divisions, a four-stage spirit on every installed government, a restoration-pressure point table, two public band readings and a super-event.
That is the large event-specific management layer the brief rules out, and the stance popup repeats the same choice on every firing.

If the proposal is accepted, mark the nested specification, matrices, research, handoffs, quality file and prompts `superseded` by the flat variant, and port only these nested contributions into the flat parts:

- the shared nonhuman and special-country classifiers as the named incompatibility that flat Part 1 requires, rather than a blanket exclusion
- the bounded multi-day application pass, so one firing does not perform every directed pair in a single day
- the two short reports to a displaced government when a collaboration government is installed over it and when that government loses its protector
- the national Collaborators Unmasked choice at restoration, as one Purge or Amnesty decision per restoration that reduces only the former installer's network
- optionally, the Competing Orders super-event when two powers each hold at least two Event 097 governments, if the parent wants one milestone presentation

The Fallout gate and the Event 052 hook are already part of both variants after this audit.


### Engine and owner questions

Flat variant: the native capability gates C01 to C06 in the [native capability matrix](../../plans/097_collaboration_plans/097_collaboration_native_capability_matrix.md), chiefly a reliable read of the current capitulation threshold (Part 4), the narrow democratic government route (Part 5) and DLC boundaries.

Nested variant:

- The installer route for democratic and non-aligned governments if the scripted collaboration-government effect honors the ideology rules (Part 3).
  The mod's `common/ideologies/00_ideologies.txt` sets `can_create_collaboration_government = no` for the democratic group and gives `can_collaborate = yes` only to two groups.
- Whether a negative collaboration change stops at zero, which A2 and Purge need (Part 4); if it does not, the user decides whether A2 may set the value to the current reading minus the points.
- Whether Open Gates and Turned Regime have clean engine routes (Part 3), and whether the conditional-removal proposal in Part 6 has the required approval.
- The Event 039 type conflict that must be settled before writing the shared cluster rows (Part 5).
- Whether Fallout's reset sees collaboration between countries that do not occupy each other, a question for the Fallout owner (Part 5).

The installed vanilla documentation now documents `add_collaboration` and `set_collaboration` on a 0 to 1 scale; every other engine fact recorded in the research notes and the plans folder remains unverified.

## Revision log

### 2026-10-10 spec audit

- Rewrote this entry as a variant map: which files and prompts belong to each variant, a one-paragraph design for each, and a single conflict table.
- Added the Fallout gate and the Event 052 hook to the flat variant (Part 6, Part 10, prompts) and refreshed both variants' Tordesillas references to the existing Event 093 package.
- Flat Parts 3 and 5: a harsh occupation now defers the Evolution II handover and Evolution IV readiness offer until the occupier relaxes it, tying the collaborator dividend to the famine, camp and condemnation consequences of brutal rule.
- Replaced Codex-specific spawning wording and `.agents/skills/` links in both asset prompts and the flat goal prompt with the self-contained-prompt rule and `.claude/skills/` paths.
- Recorded the proposal to select the flat variant; the orchestrator accepted it the same day, the nested variant is superseded, and four nested contributions were ported into flat Parts 1, 5, 6 and 10.
