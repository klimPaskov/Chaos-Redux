# Parent design review

## Review status

This is the drafting assistant's own review of the planning package.
It is not a returned subagent report.
The required independent improvement-loop, probability, and completion reviews were not executed and remain open.
No native gameplay validation is claimed.

## Decisions incorporated into the source specification

| Issue | Resolution |
| --- | --- |
| The stake was ambiguous when the defender wins | Declare one target, transfer it only on attacking victory, retain it on defensive victory |
| Global scope could conflict with old one-neighbor implementation | Replace country sampling with canonical worldwide pair discovery |
| Simultaneous fights could share unsafe opponent state | Require exact conflict identity and native prototype proof |
| Several neighbors can compete for one state | Reserve incompatible endpoints, prioritize baseline opportunities, record genuine collisions |
| High Chaos could create unbounded duplicate root replacement | Use cumulative root admission per wave and separate active occupancy |
| Momentum could jump sideways or switch opponent | Require newly opened adjacency from the latest capture and preserve the original pair |
| Random continuation could contradict the chain's stopping rule | Roll only to seed the chain, then continue after valid wins until a defined stop |
| Repeated firings could reset live conflicts | Keep independent wave records and use global reservation visibility |
| Extra consequences could overwhelm a Medium member | Avoid per-battle rewards and per-capture Chaos grants, use bounded event-owned milestones |
| Achievements could reward unrelated conquest | Require exact Event 078 receipts and continuous holds |
| Presentation could become a second management game | Keep native combat and a compact information category |
| Final localization could be invented during planning | Deliver direction briefs and required subjects only |

## Ideas considered and rejected

A paid political-power escalation decision was rejected because the outbreak is mandatory and the important choices already involve real military commitment.
A normal-war escalation option was rejected because it contradicts the requested mechanic.
Free border divisions, organization resets, and guaranteed replacement equipment were rejected because they would remove the cost of simultaneous fighting.
A second territorial award to the defender was rejected because the user specifies one disputed state.
An unrelated national focus tree or new country package was rejected because the event does not create a country or a persistent government route.
An event-specific currency, large scripted GUI, and animated background were rejected because they do not improve the core task of tracking actual border battles.

The three achievement routes were retained because they recognize different sustained accomplishments without changing battle outcomes.
The Chaos containment condition was retained because it rewards a real military stop and verified local stability without returning territory or paying unrelated resources.

## Remaining design risks

Worldwide simultaneous fighting can have a much larger campaign effect than a conventional small border event.
Wars/Medium is retained because it is the user's requested catalog assignment.
High-Chaos balance must still be tested, especially on fragmented maps with many eligible state fronts.
A balance problem must lead to an explicit tuning review rather than a hidden reduction in worldwide scope.

The strict newly opened adjacency rule can end an advance even when other enemy border states remain available.
That is intentional and keeps Border Momentum tied to the latest capture.
The player-facing explanation must make that rule understandable.
The first evolution's long-border allowance and the 25/75 percent seed values are proposed tuning, not user-specified or gameplay-tested values.

The strongest technical risk remains native concurrency and result identity.
The specification does not pretend those questions have been solved.
No proposed implementation may be labelled complete while they remain unproven.

## Relevance review of supplied skills

| Skill area | Application to this event |
| --- | --- |
| Planning, events, mechanics, dynamic effects and triggers | Core design, lifetime rules, shared integration, and source discipline |
| Subagent coordination | Bounded specialist briefs and truthful execution status |
| Decisions and missions | Native informational category and meaningful hold objectives |
| Event assets | Report, news, category icon, and achievement pipeline |
| Improvement loop | Required independent near-completion review remains open |
| Debug and playtest | Native compatibility, persistence, multiplayer, and consumer acceptance |
| Scripted GUI | Reviewed, dedicated GUI not selected because native surfaces cover the design |
| Frame animation | Reviewed, no useful animation consumer selected |
| Focus trees | Reviewed, no country route requiring a focus tree is created |
| Super events | Reviewed, ordinary report and world news are sufficient for this minor-repeatable event |
| 3D model pipeline and ComfyUI | Reviewed, no new unit model, portrait, or 3D consumer exists |
| MTTH | Active evolution target and mandatory verified timing audit |

Relevance review is not a claim that every skill's production workflow was executed.
Workflows without an actual consumer were not invented to increase the package size.
The external references and mandatory execution gaps remain listed in the reading and tooling limits.

## Required closure before implemented completion

Execute the native feasibility gates.
Complete the external reading required by the actual chosen implementation surfaces.
Run the probability specialist and resolve its evidence-backed findings.
Run `chaosx_improvement_loop_planner` near completion using the required isolated handoff.
Fold accepted improvements into the source specification and implementation.
Then run the completion review with actual code, assets, tests, and catalog evidence.
Until then, this is a completed drafting package with explicit uncompleted implementation and specialist requirements.
