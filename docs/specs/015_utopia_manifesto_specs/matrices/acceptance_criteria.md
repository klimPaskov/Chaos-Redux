# Utopia Manifesto acceptance criteria

## Core event

| Requirement | Pass condition |
| --- | --- |
| Event 15 replacement | old World Tension Subsides behavior is fully replaced |
| Classification | Event 15 is Minor Fire-Once and has no cluster |
| Targeting | eligible minors and non-major player minors can receive it, majors and strong industry countries are excluded |
| AI choice | AI always accepts when eligible |
| Player choice | human player can accept or refuse |
| Tree loading | acceptance loads the Utopian tree only for the accepting host |

## Focus tree

| Requirement | Pass condition |
| --- | --- |
| Depth | main branches are not five-focus mini lanes |
| Uneven structure | branch length follows mechanics rather than symmetry |
| Opening | opening spine establishes Need Ledger, Common Stores, Vocational Rolls, Land Need, and Fracture |
| Public routes | Free Household, Morean, Surveyor, and Mandate routes all have early, middle, late, and convergence content |
| Hidden route | Outopia is hidden until route conditions reveal it |
| Branch interaction | politics, economy, military, expansion, and subject systems change each other |
| Ultimate branch | mature branches converge into route-colored Ultimate Utopia outcomes |
| Late enforcement | late focuses unlock decisions and goals to export, impose, or renounce Utopia abroad |
| Puppet utopias | utopian subjects have values, decisions, failure states, and final fates |
| AI | AI route selection and late enforcement respect country situation and route validity |

## Mechanics

| Requirement | Pass condition |
| --- | --- |
| Need Ledger | values are visible and change through focuses, decisions, missions, wars, and subjects |
| Land Need | claims and demands depend on real need and can decay or be renounced |
| Common Stores | stores matter domestically and in subject networks |
| Vocational Rolls | chosen work and forced assignments have different consequences |
| Outopia Fracture | contradiction rises through coercion, false claims, and subject abuse |
| Subject values | Local Stores, Consent, Vocational Acceptance, Dependence, Autonomy, and Fracture Import or compact equivalents are represented |
| Costs | decisions use concrete resources and objectives, not mostly political power |
| Cleanup | invalid targets, dead subjects, route changes, and solved claims are cleaned up |

## Assets and text

| Requirement | Pass condition |
| --- | --- |
| Icon coverage | every implemented focus, decision, idea, subject form, and achievement has an icon or planned reusable family |
| Subject visuals | Charter, Surveyor, Mandate, and Outopia subject forms have visual direction |
| Animation | Ultimate Utopia and hidden Outopia state have static fallback and animated presentation plan when implemented |
| Localisation | final text uses in-world wording and does not paste working labels |
| Docs | event docs, spec files, prompt files, and catalog wording agree with implementation |

## Completion workflow

| Requirement | Pass condition |
| --- | --- |
| Subagent routing prompt | `prompts/utopia_manifesto_subagent_routing_prompt.md` is read and followed |
| Near-completion improvement loop | `chaosx_improvement_loop_planner` is spawned with `fork_context=false` after a meaningful implementation tranche and before final completion audit |
| Explicit loop context | planner prompt includes event id, slug, current goal, user constraints, spec paths, implemented surfaces, blockers, accepted plans, queued plans, rejected plans, and the exact depth or anti-bloat question |
| Loop disposition | every improvement-loop addendum or closure handoff is implemented, promoted into specs, queued with a reason, rejected with a reason, or recorded as closure before completion is claimed |
| Tool unavailable case | missing loop-subagent access is reported as a blocker and not hidden as completed work |
| Final audit order | final completion audit happens after the improvement-loop output has a recorded disposition |
