# 08. A boss that uses its advantages

## Strategic priorities

The AI pursues actual conquest. It does not wait for a story flag before declaring an adjacent war, leave its full arsenal idle, or choose a peaceful political focus. Its priorities change with the physical campaign.

| State of the campaign | First priority | Next priority | Behavior that must not occur |
| --- | --- | --- | --- |
| One-state opening under immediate attack | Keep the capital supplied and expand the usable front | Break the strongest local encirclement threat | Spending the opening on a long decorative focus while no army functions |
| Secure foothold with several borders | Concentrate against a decisive front while maintaining all wars | Capture supply, industry and access to the next theater | Scattering every special formation evenly across irrelevant fronts |
| Rapid gains with poor sustainment | Repair and reconnect the limiting supply system | Replace losses and prepare the next offensive | Continuing maximum-speed attacks with empty equipment or fuel |
| A powerful neighbor blocks expansion | Concentrate appropriate breakthrough, air and special operations | Disrupt its bases and reinforcement routes | Using only generic infantry despite available relevant families |
| Origin continent has isolated remnants | Build and protect the necessary sea or air route | Establish a beachhead and bring its force to full strength | Waiting for Chaos Always Wins to unlock transport |
| Origin continent is complete but the ending is gated | Hold the continent and pursue reachable external conquests | Maintain worldwide transport preparation | Remaining idle because Chaos is too low or the branch is disabled |
| Terminal global war | Organize simultaneous viable theater campaigns | Remove the strongest remaining sovereign production base | One suicidal landing attempt followed by permanent inactivity |
| Another ending already exists | Continue the Directorate's own military purpose | Adapt to the changed world's physical conditions | Clearing, replacing or repeatedly requesting the other ending |

Initial enemies all enter war, but operational concentration is selective. Being at war with five neighbors does not require equal troop allocations to five fronts. The AI holds defensible fronts, identifies supply and capital approaches, and concentrates where a breakthrough produces useful new territory.

## Dynamic arsenal selection

Each owner adapter publishes usable role, terrain, range, support compatibility, equipment obligations, basing needs, operation capacity and completion or failure receipts. These fields determine whether the capability is relevant now. A family token alone is not enough to select it.

Selection follows four questions. Can the operation occur legally, can the country sustain it, does it solve a current campaign problem, and has that family or useful role been neglected? The last question prevents an optimizer from selecting the same cheap unit forever while the rest of the promised arsenal remains decorative.

Maintain a bounded capability service queue with a stable cursor. Every newly registered usable family receives opening review and a real operational opportunity. A family that cannot currently operate records a reason and a due condition such as a captured coast or a completed native site. It is revisited when that condition changes. It does not disappear because a weighted draw lost repeatedly.

Where two capabilities fill the same immediate role, weights may vary the choice according to enemy armor, terrain, distance, stockpile coverage, previous performance and diversity debt. A compulsory legal minimum roster and a bounded service queue sit outside that discretionary lottery. This keeps variety without promising that every weapon is fired simultaneously.

The country always selects unrestricted in-game CBRN use policy and activates its appropriate command. It performs real operations through the owner system. Possessing aircraft, support companies or finished technologies alone is not an attack. It pays the native delivery costs once, supplies the actual payload and protection requirements, and uses returned results to pick subsequent targets.

The AI may protect its own troops and infrastructure because that helps conquest. It does not refuse an operation because of a political condemnation threshold, a moral-policy prerequisite, the target's ideology or the desire to preserve its own future ending eligibility. Mechanical range, basing, weather, equipment and friendly losses still affect usefulness and legality.

## Production and construction

Production prioritizes the largest material deficit in the active force plan, then reserve restoration, then the next strategic capability. A new rare family receives an initial production or owner-spawn allocation even if ordinary rifles have a larger absolute numeric deficit. Compare normalized coverage, not raw item counts that would always favor cheap high-volume equipment.

Building priorities follow the relevant theater. Rail and supply precede a deep land push. Airfields precede a sustained air campaign. Ports and dockyards precede a large ocean crossing. Captured facilities are repaired when their operational output matters. The AI does not demolish a functioning unique facility merely to replay its construction reward.

A one-state opening uses the exceptional supply support in Part 03. As territorial depth increases, the AI establishes redundant hubs and bases. Losing a central node reduces local momentum, but it does not permanently disable the entire country's shared operation manager.

## Decision and focus behavior

Every AI-usable action in Part 07 uses the same target, cost, availability, debit, result and cleanup contracts as a human. AI weight expresses willingness within the native decision system. It is not presented as a normalized percentage unless the inspected consumer actually normalizes a complete pool.

Focus priorities are role-based. Immediate operational gaps outrank long-term efficiency, while an established army moves toward absorption, ocean reach and global concentration. No required route depends permanently on another country's optional diplomatic answer. A changing front can justify a reviewed bypass or alternate target. It cannot silently grant the reward of unfinished work.

Focus score comparisons require the installed focus-selection model. Do not calculate focus selection as simple weight divided by total when the source uses an independent score race. An explicit strong preference can coexist with variation among viable strategic choices.

## Resistance AI

Countries adjacent to the Directorate immediately value defensive supply, front concentration, anti-armor and air coverage appropriate to the actual enemy composition. Countries on the origin continent treat the threat as urgent even before they gain a border. Overseas countries prepare staging, convoy protection and material aid according to reach and current exposure.

Resistance countries can coordinate through existing factions, access, expeditionary forces, aid and shared war rules. Do not forcibly merge human countries into a new faction or dissolve all their old wars. AI cooperation preference rises with observed Directorate strength, proximity, continental progress and the shared World Threat contribution. A faraway weak state may prioritize evacuation and fortification over an impossible offensive.

The AI chooses equipment and protective responses from the capabilities actually observed or credibly detected. It does not need omniscient access to hidden provider data to make a sensible defense. Direct battlefield observation supplies knowledge of visible families and operations. Intelligence work can improve early warning of an ocean operation without guaranteeing the landing location.

A defender nearing capitulation prefers saving a viable fighting force and denying movable reserves when those actions remain feasible. It cannot evacuate the same population or equipment repeatedly, create a duplicate army abroad, or move fixed industry instantly because a mission expired.

## Probability and timing review cases

These are acceptance targets for the supplied probability auditor. The live HOI4 probability tools were not exposed during this planning pass, so no row below claims a measured engine probability.

| Case | Required inspection | Expected ordering or invariant |
| --- | --- | --- |
| Grace at 1000, 1000 plus a positive supported increment, and 999 | Pool availability and threshold sweep | Exactly 1000 remains unavailable |
| Anniversary minus one hour, anniversary, plus one day | Date and event-selection inspection | No candidate before a full year. No immediate forced dispatch at the anniversary |
| Excess ages 0, 0.5, 1, 2, 3 and 5 years | Evaluate the same complete pool | Owner priority rises at every increasing age |
| Another major fires midway | Sequence with actual reset and cadence | Directorate age-derived weight is preserved |
| All other eligible events removed | Inspect standard selector | Normal sole-candidate behavior is allowed. No private deadline or fabricated competing event is added |
| Large or very old pool weights | Numeric boundary sweep | Positive competitors retain nonzero representation without overflow |
| Uniform spawn in differently sized countries | Complete valid-state draw | Each valid state has equal selection weight. No country-first bias |
| No valid state or occupied carrier | Event and scenario preflight | No mutation, Chaos, fired state or success log |
| Tiny country against late-game neighbor | Force model inputs | Local enemy strength can dominate the world-share term |
| Jungle front with abundant robots | Capability and production evaluation | Terrain-appropriate forces outrank robot-only concentration |
| Inland start with one island remaining later | AI state transition | Coast, delivery and basing work occurs before any terminal request |
| Legal CBRN target with sufficient resources | Decision and operation evaluation | The AI has positive willingness and produces an actual operation |
| New family registered after spawn | Queue and version lifecycle | It receives review without an Event 103 family-list edit or baseline refill |
| Critical fuel shortage | Construction, production and decisions | Supply recovery outranks a discretionary new offensive |
| Losing the last required island at terminal commit | Shared ending conflict evaluation | Terminal request fails without a stale local latch |
| Global random scheduler stopped | Owner lifecycle inspection | Active boss work continues without ordinary event dispatch |

Use the exposed `probability_inspect` route first when available. Build complete scenario inputs from current source, then evaluate and sweep relevant boundaries. Compare implemented source against the accepted design using the same scenarios and preserve before/after source for changed weights. Use simulation only for declared uncertain inputs. Use sequence analysis only with a complete model of candidate pools, cadence, resets, removals, cooldowns and terminal states. Render a comparison or unresolved view when it helps reviewers see the result. After the AGENTS.md retry limit, use named representative calculations from the actual source and state score-versus-probability assumptions and unsupported behavior. An unavailable analyzer alone is a verification limitation.

Balance review should report time to viable first combat, survival of the initial foothold, family representation, conquest momentum, supply failures, naval attempts, operation use and late-game entity cost. It must not weaken the boss simply because a normal country cannot beat it alone. Early defeat should require unusually effective concentration or favorable circumstances. A mature Directorate should be close to impossible to stop while remaining a real military country.
