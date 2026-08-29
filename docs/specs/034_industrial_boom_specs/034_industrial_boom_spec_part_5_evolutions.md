# Industrial Boom specification, part 5: Evolutions

## Evolution structure

Industrial Boom has one escalation track with three evolution stages.

| Stage | Working name | Minimum world state | Core change |
| ---: | --- | --- | --- |
| I | Speculative Mania | Rising Chaos | Credit, confidence, and political resistance make the boom stronger and harder to restrain |
| II | The Industrial Miracle | Chaos Tier | Selected regions produce development beyond ordinary material constraints |
| III | Runaway Industrialization | Totalen Chaos | Industrial growth spreads through the map at abnormal speed and becomes highly volatile |

The world-state threshold makes each evolution possible. It does not activate the evolution instantly. An active boom receives the evolution through dynamic pacing and event conditions. A new Event 34 firing can use an evolved opening when the stage is already unlocked, enabled, and appropriate for the target.

Evolution activation gives no Chaos by itself. Chaos changes come from concrete abnormal outcomes described below.

Every stage is independently controlled by the shared evolution enable system. A disabled stage cannot set its recorded flag, unlock its decisions, change the opening, or satisfy a later stage. If a higher stage is enabled while a lower stage is disabled, the implementation should follow the project-wide evolution dependency rule and avoid creating a hidden lower-stage state. The safe design is to require lower stages for higher stages.

## Evolution pacing

Active-event evolution uses MTTH-style pacing centered around a meaningful delay. The normal center should be around one quarter of a year, with strong factors moving it earlier or later.

Evolution becomes more likely when:

- The boom remains active for a long time.
- Overheating stays high.
- The player repeatedly runs the economy hot.
- Several regional projects are active.
- The target has strong industry.
- The target is at war and has high equipment demand.
- The prior evolution has produced concrete incidents.
- The global Chaos value is well above the threshold.

Evolution becomes less likely when:

- The country is already preparing a controlled landing.
- Overheating stays low.
- The economy is cooling.
- Projects are suspended.
- The target has poor logistics that would turn the evolution into an immediate unavoidable crash.
- The event has only recently fired.

An evolution should not appear during the final days of a landing mission unless the stage can change the landing in a readable way. The default is to pause evolution pacing while a controlled landing is in its final confirmation window.

## Evolution I: Speculative Mania

### Identity

The expansion becomes self-reinforcing through credit, confidence, political pressure, and expectations of endless growth. Firms announce projects before materials are secured. Banks and ministries treat future capacity as present wealth. Workers, local governments, and military procurement offices resist any action that might slow orders.

The evolution remains grounded in recognizable economic behavior. It does not yet require physically impossible construction.

### Active-event entry

When an existing boom evolves:

- The country receives an evolution report.
- The boom modifier strengthens.
- Speculative pressure becomes a major hidden contributor to Overheating.
- The cooldown and political cost of cooling increase.
- New speculative incidents enter the pool.
- High-risk project offers appear.
- Existing incomplete projects may gain a short progress surge and a lasting fragility increase.
- The AI re-evaluates its strategy immediately.

The evolution should not reset Overheating or restart the baseline lifecycle. It alters the active state.

### Pre-fire evolved opening

When Event 34 fires after Evolution I is already available and enabled:

- Starting Overheating is higher.
- The initial boom modifier is stronger.
- One speculative opportunity is prepared for the early phase.
- Cooling and reserve actions remain available from the start.
- The target receives a clear indication that restraint will face resistance.
- Initial Industrial Regions may include one state with speculative construction pressure.

A pre-fire Evolution I opening must still give the target time to benefit before danger. It should not begin in Pre-crash unless the target also has severe external weaknesses.

### New action family

#### Approve a Speculative Expansion

The country accepts a high-yield project whose financing and material base are uncertain.

Benefits:

- Strong temporary construction and output.
- Rapid regional project progress.
- Chance to create a lasting project quality improvement when completed at low Overheating.

Risks:

- Immediate Overheating.
- Higher speculative drift.
- Unfinished works if cancelled.
- Stronger Event 35 severity when the project fails near collapse.

The offer should name its target region and visible purpose. It should not be a generic gamble button.

#### Impose Credit Restraint

The country limits project finance and slows the creation of new obligations.

Costs:

- Temporary construction penalty.
- Stability or war support pressure when public confidence in the boom is high.
- Slower project progress.

Benefits:

- Lower speculative drift.
- Reduced chance of bubble incidents.
- Better landing forecast.

#### Liquidate Speculative Projects

This emergency action is described in part 3. Evolution I makes it a central path and removes its status as a rare incident response.

### Speculative opportunity types

The event should choose from a bounded pool that matches the target's geography and economy.

- New factory district near an existing Industrial Region.
- Port and shipyard expansion for a maritime country.
- Railway and depot expansion for a continental country.
- Synthetic material complex when fuel or rubber pressure exists.
- Machine-tool and conversion complex.
- Resource processing network in a suitable state.

An opportunity should never promise a reward that the state cannot support. A port project needs a coastal state. A resource project needs a credible material basis.

### Incidents

#### Order-book frenzy

Firms accept more orders than they can fulfill. The player may force prioritization, allow delays, or use reserves.

#### Credit pyramid

Several projects depend on the success of one another. The player may rescue the chain, cancel the weakest project, or keep it running.

#### Restraint backlash

Cooling creates opposition from firms, workers, local governments, or military procurement. The action can be maintained at a stability cost or weakened to preserve support.

#### The profitable shell

A project appears productive in reports but has little physical progress. Investigation can expose it, while continued support may preserve output briefly and worsen the later correction.

#### Local land rush

Population and construction pressure around one Industrial Region increase local strain. The country can fund support infrastructure, limit expansion, or accept fragility.

### Success

A successful Speculative Mania landing converts selected projects into real capacity after cancelling weak obligations. It can produce more lasting development than baseline, provided the country finishes integration at low pressure.

### Failure

A Speculative Mania crash passes higher financial fragility and unfinished-project exposure into Event 35. Event 35 begins at Evolution I and receives a higher severity seed than a baseline crash with the same final Overheating.

### AI behavior

Aggressive wartime AI may accept one high-risk expansion when Overheating is low and supply is secure. Cautious AI prefers credit restraint and reserves. No AI should accept another speculative project while one unresolved project already threatens the landing.

### Chaos outcomes

Evolution I activation gives zero Chaos. A speculative bubble or project failure normally gives zero event-owned Chaos because ordinary economic instability is already represented by later concrete consequences. One small guarded Chaos gain is allowed when an unprecedented speculative project creates a nationally significant abnormal industrial expansion before its physical basis exists. This should occur once per country per Event 34 firing and only after a visible consequence.

## Evolution II: The Industrial Miracle

### Identity

The boom begins creating capacity faster than ordinary industrial constraints allow. Railways, factories, synthetic plants, repair networks, and industrial districts appear at a speed that engineers cannot explain through normal mobilization. The country can turn selected states into Industrial Miracle Regions.

The miracle remains tied to materials, states, and player choices. It does not create arbitrary factories across every state.

### Active-event entry

When an existing boom evolves:

- One or more current Industrial Regions become eligible for Miracle designation.
- The temporary boom modifier strengthens.
- Project progress accelerates.
- Regional fragility becomes active.
- New project profiles unlock.
- Overheating receives a moderate immediate increase.
- The event presents the first physically abnormal development in a specific state.
- A one-shot Chaos milestone may occur when the first impossible structure or capacity increase is completed.

Existing protected regions retain their protection. Existing projects are not deleted. The player chooses whether to upgrade a current project into a Miracle project or keep it conventional and safer.

### Pre-fire evolved opening

When Event 34 begins at Evolution II:

- Starting Overheating is higher than Evolution I.
- At least one valid Industrial Region is ready for Miracle designation.
- The opening report describes completed work that should have taken much longer.
- The country receives the stronger temporary modifier.
- The first Miracle project offer arrives during Ignition or early Expansion.
- The player can refuse the Miracle designation and pursue a safer evolved landing with fewer permanent rewards.

The evolved opening should not grant a permanent slot, factory, railway, or resource before the player has completed a project.

### Industrial Miracle Regions

The country may designate a small number of primary regions. The cap remains readable:

- One for a small player country.
- Up to two for a medium economy.
- Up to three for a large major.

A Miracle Region receives:

- Faster project progress.
- Stronger temporary local industrial effects.
- Higher project reward ceiling.
- Higher pressure contribution.
- A visible Fragile Miracle status when Overheating is high.

The state should have a clear visual marker and tooltip. The player does not manage a numeric local meter.

### Miracle project profiles

#### Permanent Industrial Capacity

The region attempts to convert temporary expansion into a limited factory or building-slot reward.

Requirements:

- Strong infrastructure or a completed support project.
- Sustained low Overheating during integration.
- Valid country and state legacy budget.

Risks:

- High material pressure.
- High fragility.
- Severe Event 35 shutdown exposure after a crash.

#### National Rail Spine

The region becomes the center of rapid railway, depot, and supply development.

Potential result:

- Railway and infrastructure improvements.
- Supply resilience.
- Reduced future boom pressure.

This profile should be especially valuable for countries whose industrial base is limited by internal transport.

#### Synthetic and Recycling Complex

The region expands synthetic production, recycling, scrap recovery, and material substitution.

Potential result:

- Appropriate synthetic or resource-efficiency benefits.
- Reduced material pressure.
- Better resilience against embargo and blockade.

The project should not create every strategic resource without basis.

#### Machine-City Network

The region develops linked factories, machine shops, conversion facilities, and worker settlements.

Potential result:

- Strong construction and conversion legacy.
- Limited capacity increase within the country cap.
- Higher population and infrastructure pressure while active.

#### Automated Scheduling and Production Control

The region develops extraordinary coordination practices that increase production efficiency without requiring a large physical reward.

Potential result:

- Strong long-duration production-efficiency growth or conversion benefit.
- Lower future maintenance pressure.
- Safer repeat booms.

### Miracle incidents

#### The railway completed overnight

A rail segment appears finished far ahead of schedule. The country can integrate and inspect it, divert it to immediate use, or refuse to rely on it until safety work is complete.

#### The factory without a supply record

A working complex appears to have consumed fewer materials than its construction should require. The country can investigate, expand, or limit operations.

#### The city around the works

Housing, transport, and population growth accelerate around a Miracle Region. Investment lowers fragility, while neglect raises labor and infrastructure pressure.

#### Materials that should not be available

A project receives components no ministry can account for. The player can use them, quarantine them, or restrict the project. The event should preserve uncertainty without adding a separate supernatural resource.

#### The impossible production schedule

A region reports output that exceeds its installed machinery. Continued exploitation raises Overheating and may trigger the first concrete Chaos milestone.

### First miracle Chaos milestone

The first completed physically impossible project can add a guarded event-owned Chaos increase. The change represents a concrete violation of ordinary industrial limits that governments, engineers, and foreign observers can see.

Rules:

- The evolution activation itself gives zero.
- The milestone fires only after a completed visible abnormal result.
- It occurs once per Event 34 firing, with a longer country repeat guard for similar manifestations.
- It does not duplicate Chaos from deaths, war, annexation, contamination, or world tension.
- A cancelled or purely planned project gives no Chaos.

### Success

A successful Miracle landing can retain substantial map development and production practices. The strongest permanent rewards require low Overheating and completed integration. A country that only exploits the temporary miracle receives less permanent conversion.

### Failure

A crash idles or damages Miracle Regions through Event 35. Event 35 begins with Evolutions I and II active. Fragile Miracle Regions become high-priority depression states and contribute strongly to starting severity.

### AI behavior

AI chooses Miracle projects according to its bottleneck:

- Transport-limited AI favors rail and supply.
- Resource-limited AI favors synthetic and efficiency work.
- Wartime equipment deficit can justify capacity work.
- Cautious AI favors scheduling, repair, and logistics.
- AI avoids maximum-capacity work when Overheating is already dangerous.

### Containment and reversal

A country can refuse further Miracle designations, cool the economy, complete integration, and land safely. Successful containment of a visibly abnormal expansion can support one guarded Chaos reduction only when it closes the same recorded abnormal source. Ordinary successful landings should not farm negative Chaos.

## Evolution III: Runaway Industrialization

### Identity

Industrial growth begins to spread from existing centers into neighboring states. Factories, mines, railways, worker settlements, and construction sites expand at a rate that normal administration cannot fully direct. The country can harness the spread, create new production corridors, or attempt to contain it before the system collapses.

The event becomes an economic anomaly whose stakes remain the target country’s management and survival.

### Active-event entry

When an existing boom reaches Evolution III:

- The boom modifier reaches its strongest form.
- Overheating volatility increases sharply.
- Each valid Miracle Region may identify one neighboring spread candidate.
- The player receives a choice between controlled corridor growth and unrestricted expansion.
- Existing projects gain progress and fragility.
- A new map-linked spread incident occurs after a short delay.
- Runaway expansion can create guarded Chaos milestones when it establishes major abnormal capacity in new states.

The stage does not reset project caps or permanent legacy budgets.

### Pre-fire evolved opening

When Event 34 begins at Evolution III:

- Starting Overheating begins in the upper stable or lower strain range according to country strength.
- One primary Industrial Region and one potential neighboring spread state are identified.
- The first spread decision appears early.
- Reserve and protection actions are available immediately.
- The country receives the strongest temporary production package.
- The opening report shows industrial work expanding beyond ordinary plans.

The target should have a plausible survival path. A weak player country may receive fewer spread candidates and stronger scaling support, while the final potential remains dangerous.

### Spread rules

Industrial spread moves from a primary region to a valid adjacent state.

A valid spread state should:

- Be controlled by the target country.
- Normally be a core state.
- Have population.
- Be passable.
- Have an adjacency or verified economic connection to the primary region.
- Not already hold an incompatible Event 34 project.
- Have enough remaining building or infrastructure potential to show development.

Spread prefers:

- Existing rail connections.
- Moderate infrastructure.
- Resource access.
- Strategic depth.
- States that reduce industrial concentration.

Spread avoids:

- Frontline states at high risk of immediate loss unless the player deliberately accepts the risk.
- Isolated islands without a valid maritime connection.
- Tiny remote possessions.
- States with severe active disaster or contamination conditions that block ordinary civilian industry.

### Spread strategies

#### Controlled Industrial Corridor

The country chooses one neighboring state and commits logistics, protection, and civilian capacity.

Benefits:

- Lower Overheating than unrestricted spread.
- Better project quality.
- Stronger chance of lasting rail, infrastructure, or capacity.
- Easier landing integration.

Costs:

- Large civilian commitment.
- Trains, trucks, fuel, or convoys according to geography.
- Slower immediate output than unrestricted spread.

#### Unrestricted Expansion

The country permits rapid development wherever the boom reaches.

Benefits:

- Strong immediate output and construction.
- Faster spread.
- More temporary secondary states.

Risks:

- Large Overheating increase.
- Severe fragility.
- Harder protection.
- Greater Event 35 severity.
- More likely abnormal Chaos milestones.

#### Contain the Spread

The country stops new secondary development and concentrates on current regions.

Benefits:

- Lower drift.
- Better landing forecast.
- Reduced incident pool.

Costs:

- Temporary output and construction loss.
- Stability or war support pressure when the boom has broad public support.
- Lost chance for the strongest Evolution III legacy.

### Secondary spread states

Secondary states should use simple qualitative statuses:

- Surveyed.
- Expanding.
- Integrated.
- Fragile.
- Abandoned.

The player should see only active relevant states through a compact selector or state markers. The main category must not list every eligible neighboring state.

Secondary states contribute to the primary region's project. They do not each create a new independent project slot or permanent reward receipt.

### Runaway incidents

#### The unplanned works

Construction begins outside the approved corridor. The player can recognize it, dismantle it, or redirect it.

#### The mine below the survey line

A mine or extraction site expands beyond known deposits. Continued use can lower material pressure and raise abnormality risk.

#### The railway that keeps growing

A rail line extends into a neighboring state without a matching approved schedule. Integration can create a strong logistics result, while unchecked growth raises fragility.

#### The industrial city without a charter

A settlement and production center forms around the works. The country can provide services, enforce control, or accept disorder.

#### The production map no longer matches the land

National records cannot reconcile the location and output of new capacity. The country must pause, audit, or continue using it.

#### Network cascade

One failure disrupts several connected states. Protection and reserves determine whether the shock remains local or pushes the economy toward Event 35.

### Runaway Chaos milestones

Concrete outcomes that may add guarded Chaos:

- The first integrated spread state whose capacity appeared at impossible speed.
- A production corridor that reaches a large abnormal capacity threshold.
- Unrestricted expansion entering several states during one firing.
- A visible network cascade that disrupts a large share of national industry.

Rules:

- Each milestone requires a new observable consequence.
- Repeat guards prevent pressure farming through repeated state toggles.
- Ordinary factory construction, resource extraction, state damage, and deaths continue using their shared Chaos sources where applicable.
- Event 34 adds only the abnormal-significance component.

### Success

A country that stabilizes Evolution III can retain a major industrial base within the country and state legacy caps. The best result should be campaign-defining. It requires more than surviving at 99 Overheating and pressing an emergency button.

Exceptional success requires:

- Controlled spread through bounded corridors.
- Integrated primary and secondary states.
- Low final Overheating.
- Strong reserves.
- Protected primary regions.
- A completed landing mission.
- No unresolved network cascade.

### Failure

A crash at Evolution III:

- Ends every Event 34 temporary bonus.
- Starts Event 35 at Evolution III with Evolutions I and II active.
- Begins with very high Depression Severity.
- Marks Miracle Regions and spread corridors as fragile depression states.
- Passes unfinished projects, depleted reserves, protection state, region loss, and crash cause.
- Creates no second global pacing event.

### AI behavior

AI uses a strict risk model.

- Cautious AI normally chooses containment or one controlled corridor.
- Balanced AI chooses controlled spread when supply is strong and Overheating is below strain.
- Wartime gambler AI may choose unrestricted expansion when losing a major war or facing critical equipment deficits.
- No AI chooses unrestricted expansion in Pre-crash.
- AI begins landing earlier when several high-value projects are already secured.
- AI protects the most connected primary region before opening a second corridor.

## Evolution inheritance summary

| Active Event 34 stage at collapse | Event 35 inherited stages | Severity direction |
| --- | --- | --- |
| Baseline | Baseline Event 35 | Severe but recoverable, scaled by final state |
| Evolution I | Event 35 Evolution I | Adds speculative and unfinished-project exposure |
| Evolution II | Event 35 Evolutions I and II | Adds fragile Miracle Regions and greater physical overcapacity |
| Evolution III | Event 35 Evolutions I, II, and III | Very high starting severity with network and spread exposure |

## Evolution text direction

Evolution text should show the changed economic pattern through observed activity.

### Speculative Mania

Viewpoint:

- Government, industrial authorities, firms, workers, and local officials living inside endless confidence.

Visible information:

- Projects announced before inputs exist.
- Orders and financing expanding faster than physical work.
- Resistance to restraint.

Uncertainty:

- Whether the confidence is justified.
- Which projects have a real basis.

Tone:

- Energetic, confident, increasingly reckless.
- Irony can come from official certainty and visible excess.

### The Industrial Miracle

Viewpoint:

- Engineers, planners, workers, inspectors, and foreign observers confronting completed work that should have taken longer.

Visible information:

- New capacity, rail, buildings, and output.
- Missing or inconsistent material records.

Uncertainty:

- How the work was completed.
- Whether it can be maintained.

Tone:

- Wonder mixed with technical unease.
- Avoid religious miracle language unless final localisation uses it deliberately and consistently.

### Runaway Industrialization

Viewpoint:

- Local authorities and national planners trying to follow development that has spread beyond the approved plan.

Visible information:

- New works, railways, settlements, mines, and factories in adjacent states.
- Networks that are productive and hard to control.

Uncertainty:

- Where the spread will stop.
- Which parts are physically sustainable.

Tone:

- Concrete and administrative under pressure.
- Avoid generic claims that the economy has become alive unless a later design explicitly establishes that fact.

## Evolution acceptance tests

The evolution design passes when:

- Each stage changes rules, decisions, incidents, state behavior, AI, and Event 35 inheritance.
- Active booms evolve without requiring Event 34 to fire again.
- New firings can begin in an evolved form.
- Disabled evolutions do not leak state or block baseline resolution.
- Evolution activation gives zero Chaos.
- Concrete abnormal outcomes can create guarded Chaos changes.
- Evolution II and III can be contained without forcing collapse.
- The safest path gives less maximum legacy than the risky path.
- High-tier AI understands when to stop.
- A stage does not merely apply a larger copy of the same modifier.
