# Event 029: Riches Found

Implementation status markers in this package: **Implemented** means current source carries the behaviour (source review only, live testing belongs to the user); **Pending** means accepted design not yet in source; **Proposed** means an audit proposal awaiting acceptance.
The source map is [the Event 029 overview](../../events/029_riches_found/overview.md), and dated decisions are in [the plans folder](../../plans/029_riches_found_plans/).

## Catalog identity

- Event ID: `29`, entry event `chaosx.nr29.1`.
- Event name: Riches Found.
- Type: Minor Repeatable.
- Chaos level: 1 (Calm World).
- Cluster: none, by the user's 2026-10-07 instruction recorded in [the catalog correction handoff](../../plans/029_riches_found_plans/subagent_handoffs/catalog_alignment_2026_10_07.md), which supersedes the older agent decision D2 that kept clusters 7 and 15.
- Catalog status: Needs Testing.
- Catalog wording is owned by [the catalog alignment file](029_riches_found_catalog_alignment.md).

## Event promise

A completely random ordinary country discovers exceptional mineral wealth in one suitable state.

The discovery delivers an immediate national windfall of exactly 1,000 political power.

The selected state becomes a persistent source of revenue and industrial leverage, and its value follows whoever controls it.

A mining rush follows: workers, prospectors, transport firms, merchants, engineers, guards, criminals, officials, foreign concession seekers, and neighbouring states compete around one location.

The player decides how fast the mine is developed, who receives the revenue, who controls access, how the site is protected, and how much authority is surrendered to private or foreign interests.

The mine can become a durable development engine, a captured patronage system, an armed enclave, an obsessive killing ground, or a place where impossible bargains are made.

## Separation from Event 018 Resources Found

Riches Found is not another strategic-resource discovery roll.

Event 018 owns deposits that add or expand map resources, deeper physical discoveries, caves, fossils, Oth-Kesh, and its underground terminal route.

Event 029 owns windfall governance and control of one exceptionally valuable mining site.

The ordinary reward comes from a persistent state modifier and a controller-wide aggregate, not from adding steel, oil, aluminium, chromium, tungsten, or rubber to the map.

A state carrying an Event 018 field or cave marker, or an existing Event 029 mine, is not eligible.

The supernatural track never reveals Oth-Kesh, never calls the Event 018 cave chain, and never selects The World Opens Below.

Implemented: the target gate excludes Event 018 markers and registered mines.

## Valid recipient country

The entry event selects one existing country from the ordinary country pool.

A valid recipient:

- exists and owns and controls at least one eligible state;
- is not classified by `is_special_chaos_country` or `is_actual_nonhuman_country`;
- is not a civil-war shell, scripted system carrier, or temporary country that the repository excludes from ordinary civilian events;
- can receive political power and country modifiers normally, with a valid government and capital.

Every valid recipient has the same selection weight; mine count, size, ideology, major status, and player control never bias the roll (user requirement: a completely random recipient).

When no valid country and state pair exists, Event Details shows `N/A` and the event does not enter selection.

Force-trigger mode bypasses ordinary selection only through the existing settings contract.

Implemented: `riches_found_prepare_random_event_fire` builds one pool entry per eligible country, selects and revalidates a fresh pair on every call, and `riches_found_has_no_valid_discovery_pair` drives the `N/A` lock without preparing anything during interface refresh.

## Suitable state selection

The event selects one state owned and controlled by the recipient.

Positive selection factors are meaningful population, room for development, a land or usable port connection, existing infrastructure or rail, an existing settlement, adjacency to other land states, and border proximity when armed competition is plausible.

Wasteland, empty islands without a usable port, impassable terrain, states reserved by another persistent site system, states in an active catastrophic disaster, and states in the middle of a scripted transfer are rejected.

Selection stays random after weighting and must not always choose the capital, richest state, or largest population.

The chosen state is saved as the mine's identity and added to the bounded mine registry (at most 64 entries).

## Deposit profiles

The discovery assigns one deposit profile.

The profile is the mine's quality: it sets the output factor, steers incident weights, foreign interest, development needs, and collapse risk, and selects the discovery picture.

There is no second hidden quality roll; a separate quality band would duplicate the profile without giving the player anything to act on.

| Profile | Output factor | What the player should expect |
| --- | --- | --- |
| Alluvial field | lowest | Fastest rush, weakest claims, most claim jumping and petty crime; administration and sanitation matter first. |
| Deep vein | standard | Slower opening, costly shafts, rising collapse pressure until the shafts are reinforced. |
| Gemstone bed | high | Theft, substitution, and smuggling; legitimacy is hard to keep and mine police matter. |
| Platinum lode | highest | Strong foreign and state interest, concession offers, and processing demands. |

Implemented: profiles, their factors in `riches_found_scaling`, profile incident weights, and the four profile discovery pictures.

## Immediate discovery package

The receiving country gains exactly 1,000 political power once (user requirement).

The grant uses the native political-power cap; no cap change, deferred credit, or replacement currency is added (agent decision D3).

The state receives the persistent mine identity, and the entry event offers five opening policies that set the mine's lasting policy profile:

| Option | Policy profile | Direction |
| --- | --- | --- |
| Build a public fortune | Public Development | Slower output, stronger legitimacy and order. |
| Make the mine an instrument of state | State Extraction | Strong national receipts, dependence risk. |
| Invite foreign investment | Concession Economy | Fast development with foreign leverage. |
| Place the mine under armed authority | Militarized Mine | Order by force, legitimacy cost. |
| Take everything the mountain will yield | Predatory Extraction | Highest short-term output, highest failure risk. |

No option is a dominant reward choice.

Starting values then vary once, at discovery, through the owner's stability, core status, infrastructure, war and local resistance, the Chaos Meter, democratic government, and the deposit profile.

The opening report describes workers arriving, prices changing, claims being staked, routes filling, and officials losing control of access; it does not read as a reward list.

Implemented: the five options, `riches_found_apply_starting_conditions`, the idempotent grant behind `riches_found_discovery_grant_paid`, and the evolved opening descriptions.

## Persistent state identity

The mine belongs to the state, not to the discovering country.

The identity survives temporary closure, occupation, sabotage, damage, loss of the state, and government change.

It ends only through permanent exhaustion, permanent sealing, catastrophic collapse beyond recovery, Event 028's permanent main crater, a supernatural closure, or a later accepted adapter.

The discovering country keeps the one-time windfall and loses ongoing benefits when it no longer controls the state.

## Controller transfer contract

The mine follows the current controller through war, occupation, civil war, peace settlement, annexation, liberation, and release.

The controller refresh:

1. removes the mine's contribution from the previous controller aggregate;
2. records the new controller once;
3. recalculates control quality from core status, compliance, resistance, route damage, and current condition;
4. adds the bounded contribution to the new controller aggregate;
5. replaces controller-specific decisions and missions;
6. preserves development, damage, closure, pressure, incidents, contracts, and evolution history;
7. clears invalid foreign targets and re-evaluates a surviving contract once;
8. sends a transfer report only when the change is strategically meaningful or a crisis is active.

No whole-world daily, weekly, or monthly scan is allowed.

Implemented: the narrow `on_state_control_changed` hook (new controller `ROOT`, old controller `FROM`, state `FROM.FROM`) reconciles registered mines and refreshes registered mines beside the changed state; annexation, peace conference, and capitulation walk only the mine registry.

## Physical destruction by Asteroid Incoming

The [Event 028 impact profile](../028_asteroid_incoming_specs/028_asteroid_incoming_spec_part_3_impact_damage_and_aftermath.md) decides whether the mine state survives.

A permanent main crater ends the mine: its contribution is removed, site projects and missions close under their cancellation policies, and the controller aggregate is rebuilt from surviving mines.

The historical record, the original payment, and the national aftermath remain, and the destroyed site cannot satisfy sealing, evacuation, reform, or bargain achievements.

Impact deaths never satisfy a mine obligation and never trigger a second mine-death debit.

A surviving ring state or fragment centre instead revalidates works, supply, and transport, and the player uses the ordinary repair, closure, and reopening choices.

The mine checks this during its ordinary refresh and never launches Asteroid Incoming, adds an incident roll, or grants a replacement windfall.

Pending: no Event 029 source reads the Event 028 crater markers yet.

## Visible values

Every value the player sees must change a decision.

| Value | Shown as | Why the player needs it |
| --- | --- | --- |
| Extraction Pressure (primary) | Number with the next threshold (warning 60, severe 80, emergency 95) | It is the main risk dial: it raises output and every danger, and the cooling actions answer it. |
| Local Order | Number with a band | It gates reopening, the stabilization fund, Drive Deeper, and the security overlay. |
| Revenue Legitimacy | Number with a band | It gates audits, dividends, administration replacement, and resistance to the Resource Curse. |
| Mine Development | Band only: Provisional, Organized, Industrial, Mature | It gates Drive Deeper and Trade Access for Infrastructure and scales output; the exact number adds nothing the band does not. |

All four range from 0 to 100 internally.

Extraction Pressure rises through deep mining, output drives, requisition, exclusive concessions, weak oversight, wartime desperation, and predatory policy, and falls through closure, reinforcement, revenue settlement, sealed sections, and controlled recovery.

Mine Development rises through construction, investment, foreign capital, and repairs, and falls through raids, sabotage, fighting, closure decay, and collapse.

Local Order rises through fair claims, mine police, pay protection, supplied garrisons, and trusted administration, and falls through claim jumping, wage theft, private-army rivalry, raids, smuggling, requisition, Gold Disease, and occupation; order made by force contains corruption less well than order made by administration.

Revenue Legitimacy rises through dividends, local development, transparent terms, and credible audits, and falls through secret concessions, patronage, displacement, unpaid labour, guard abuses, central seizure, and exposed theft.

Implementation status: the committed header shows all four as numbers plus deposit, phase, policy, objective, revenue route, reserve, and account lines; an uncommitted 2026-10-10 header in another session shows phase, pressure, order, and legitimacy only.
Both must converge on the header in [Presentation](#presentation).

## Hidden state

Hidden values exist for causality and surprise and are never shown as raw numbers: concession exposure, illicit capture, deep excavation, private-security autonomy, foreign claim pressure, collapse pressure, Gold Disease pressure, supernatural pressure, sealed-depth integrity, and treasury dependence.

Each hidden value must have at least one producer and at least one consumer that changes something the player can see (an incident, a stage, a decision's availability, or an output factor).

Their effects reach the player through reports, stage labels, decision availability, modifier text, and one-line tooltips.

Proposed (unresolved): merge foreign claim pressure into concession exposure and sealed-depth integrity into deep excavation, because each pair is produced and consumed by nearly the same actions; implement only if a source review confirms no consumer distinguishes them.

## State modifier lifecycle

The state carries one persistent mine record and exactly one active state-modifier presentation.

The visible stages are Newly Discovered Riches, Established Riches District, Contested Mine District, Closed Mine District, Ruined Workings, Permanently Sealed Workings, Corrupted Mine District, Gold-Sick Mine District, and Opened Depths, plus the lasting Gold Fever Memory modifier after Gold Disease is contained.

Stages replace each other through one lifecycle helper and never stack.

The modifier's effects derive from development, pressure, order, legitimacy, closure, damage, control, and the active evolution; its tooltip carries the deposit profile and the policy profile, which do not need header space.

Implemented: `common/dynamic_modifiers/029_riches_found_state_modifiers.txt` and the nine stage icons.

## Controller aggregate

The controller receives one aggregate country presentation summarizing every mine it controls, never one spirit per mine.

Its stages are Windfall Receipts, Managed Mineral Revenue, Resource-Dependent Treasury, Captured Revenue State, Gold-Sick Administration, Infernal Accounts, and Reformed Resource Settlement; the highest-priority stage among the controlled mines is shown.

The tooltip shows the number of producing mines, the current national benefits against their caps, and one line naming the main reason output is reduced.

It does not repeat the selected mine's condition, which the category header already shows.

Implemented: the stages and the aggregate rebuild; the tooltip trim is pending.

## Controller benefits

The user-supplied benefit set is ticking political power, nationwide construction speed, production efficiency, military factory output, and a civilian-factory benefit.

The civilian-factory benefit is consumer-goods relief, because HOI4 has no literal civilian-factory output modifier.

One mine's score is `profile x development x operating state x policy x control quality x order and legitimacy x evolution factor`, built by reusable helpers from script constants.

## Diminishing returns and caps

The first controlled mine contributes at full value, the second at 0.60, the third at 0.25, and later mines at 0.10.

The national totals are capped: political power +0.30 a day, construction speed +18%, production efficiency +10%, military factory output +12%, consumer-goods relief 8% (`riches_found_scaling`).

Diminishing returns apply only to the national aggregate; each mine keeps its local value, incidents, and strategic worth.

The tooltip states that later mines add less and that the totals are capped, without a formula.

Implemented.

## Operating states

A mine is open and expanding, regulated, under concession, under military control, under predatory extraction, contested, temporarily closed, quarantined, partially sealed, permanently sealed, collapsed, or exhausted.

Open states give the normal contribution; contested, quarantined, and partially sealed states give reduced value; a temporarily closed mine keeps its development but produces almost nothing; sealed, collapsed, and exhausted mines leave only their historical identity and aftermath.

## Presentation

The event uses one ordinary decision category, `riches_found_mine_management`, with the static picture `GFX_decision_cat_picture_riches_found` and no scripted GUI.

The category header shows, in this order:

1. the selected mine and its operating condition;
2. the current layer or phase and the Mine Development band;
3. Extraction Pressure with its next threshold, then Local Order and Revenue Legitimacy;
4. at most one conditional line, shown only when something needs an answer: the first unmet containment step, a repair objective, an active mine about to fall, or the next Bottomless Account obligation.

The deposit, policy profile, and revenue route move to the state modifier tooltip and to the revenue decisions' tooltips, where they explain a choice instead of filling the header.

A country with one mine sees it directly; a country with several uses the selected-mine flow, which opens on the mine with an active mission, crisis, recent control change, or threshold warning.

The AI evaluates every valid mine without the selection step.

The decision-layer contract that keeps each view within three to five actions (six at most) and one to three missions is owned by [Part 3](029_riches_found_spec_part_3_decisions_missions_foreign_interference.md#decision-layers).

## Player experience arc

The first decisions are about access and claims.

The next are about whether the rush becomes a settlement, a state project, or a private enclave.

The middle game is transport, revenue, contracts, labour, and protection.

The late ordinary game is keeping the site productive without letting violence, corruption, or foreign control make the mine stronger than the government.

At high chaos, the same choices acquire new costs, and pressure becomes an invitation to obsession and supernatural bargaining.

A well-managed mine stays useful; failure follows visible choices, neglected pressure, weak control, war, conquest, and bad crisis management, never the discovery itself.
