# Event 050: The Great Embargo

## Part 3: Target responses and mission design

All names are working labels. Final localisation must use finished in-world wording and should not copy these headings as automatic button text.

## Category structure

The target receives one event-owned decision category while the crisis is active. The category should show one public value, one short status summary, up to five primary actions, and no more than one active timed objective.

The visible action set changes by phase. Obsolete actions disappear. Stronger versions replace weaker versions. Target selection uses a compact selected-country flow when several neutral or coalition countries could be approached.

The normal presentation layer is:

1. ordinary category icon
2. static category picture
3. concise stage and trend text
4. normal decisions and one mission

A full scripted GUI is not needed. The mechanic has one public value and a small action set. Normal decisions give clearer access to costs, targets, timing, and blocked reasons.

## Strategy families

The six accepted response families should create several viable strategies.

### Adaptation strategy

The target reduces the real harm of the embargo through Self-Sufficiency, stockpiling, infrastructure, and selective replacement trade. This route is reliable but slow and expensive.

### Evasion strategy

The target builds Smuggling Networks and Neutral Intermediaries. This route can lower effective isolation quickly. It carries exposure risk and becomes more dangerous under Evolution I.

### Settlement strategy

The target offers Diplomatic Concessions to key participants. This route can end the crisis early, but the price persists after Pressure disappears.

### Mobilization strategy

The target chooses Defy the World and reorganizes the country around isolation. This route can preserve regime cohesion and military output for a time. It can also strengthen coalition resolve and create later exhaustion.

### Expansion strategy

The target prepares Resource Seizure when essential supply cannot be replaced. This route can solve the material problem through force and can turn a medium economic crisis into a wider war.

The target can combine compatible families. It should not be able to complete every major response without serious cost. Defiance can coexist with self-sufficiency. Open concessions should weaken the political case for extreme defiance. A discovered smuggling network can make diplomatic settlement harder.

## Opening mission

### Working label: Secure Replacement Supply

The opening mission begins after the player has had a brief inspection window. Its normal duration should be around 150 days, with dynamic adjustment for opening Pressure and dependence.

The mission asks the target to establish one credible response before Pressure becomes critical. Valid completion routes include:

- completing the first stage of a self-sufficiency project
- opening one functioning neutral intermediary route
- completing one smuggling route without immediate exposure
- securing a settlement commitment from a core participant

The mission should auto-complete when a valid route is proven. It should not require a second confirmation click.

#### Full success

The target secures reliable replacement access before Pressure reaches the severe band. It receives a meaningful reduction in immediate economic damage, a Pressure reduction, and improved access to later actions in the successful family.

#### Partial success

The target secures a route after Pressure has already reached the severe band, or the route provides only one important resource family. The target receives limited relief and keeps the next phase active.

#### Failure

The deadline expires without a viable route. Pressure rises, the target's most exposed economic area receives a stronger temporary penalty, and Resource Seizure or emergency defiance becomes easier to justify. Failure should matter without deciding the entire crisis.

## Working response: Self-Sufficiency

### Purpose

Self-Sufficiency converts construction capacity, industrial output, transport equipment, and time into lower dependence. It is the safest long-term strategy and the slowest immediate answer.

### Project selection

The first click should open or select a project family based on the target's actual exposure. Useful families include:

- domestic oil extraction and fuel conservation
- synthetic rubber and fuel substitutes
- steel, aluminum, tungsten, or chromium expansion where the map can support it
- salvage and material recovery
- railway and inland transport improvement
- emergency stockpile protection
- industrial redesign for reduced imported inputs

The player should see the highest-value options first. A country without a meaningful oil problem should not receive an oil-only project as its recommended response.

### Costs and commitments

A project can consume or commit up to four cost types. Suitable costs include:

- civilian factory burden
- construction capacity
- trains or trucks
- support equipment
- fuel during conversion
- temporary factory output
- stability when rationing is severe

Political power can appear when the project requires legal or administrative action. It should not be the main price.

### Timing

A normal project should take around 120 to 180 days. Smaller emergency measures can complete sooner and provide temporary mitigation. Large extraction or synthetic programs should take longer and create durable value.

### Outcomes

Completion should:

- reduce effective embargo damage in the selected exposure family
- lower Pressure by a modest amount when the project removes coalition leverage
- improve future resilience to Event 50
- create visible state or production changes where appropriate
- avoid granting a free industrial boom unrelated to the crisis

Permanent gains must be bounded. A repeatable event cannot become an infinite resource or factory farm. State projects should have one-time completion flags, upgrade ceilings, or diminishing alternatives.

### Failure and interruption

A project can be delayed by loss of states, severe bombing, insufficient construction access, or another economic crisis. Interruption should preserve partial progress when the relevant industrial base survives. A project that loses its entire valid target must refund or convert its unspent commitment safely.

### AI direction

Import-dependent AI should prioritize the exposure that most directly affects current war production. AI at peace can prefer durable extraction. AI in a fuel emergency should prefer faster conservation or synthetic relief.

## Working response: Smuggling Networks

### Purpose

Smuggling creates covert routes through borders, ports, merchant firms, criminal groups, intelligence contacts, and falsified cargo identities. It offers fast relief and high variance.

### Route selection

The target selects one plausible route from a bounded candidate list:

- land border corridor
- neutral port and transshipment route
- faction-member covert supply
- colonial or subject route
- merchant shipping network
- financial and licensing front

Each route needs a valid host or geographic basis. The event should not offer a land-border operation through a country that does not border the target or a maritime route when neither side has usable ports.

### DLC handling

Intelligence agency assets can improve success, secrecy, and target selection where available. The action still works without intelligence DLC through an event-owned covert-trade model.

### Costs

Suitable costs include:

- convoys
- fuel
- infantry or support equipment used to pay intermediaries
- civilian factory burden
- intelligence exposure
- stability or corruption pressure

### Operation timing

A normal network should take around 90 to 150 days to establish. A high-risk emergency route can open faster with a greater chance of exposure.

### Outcome bands

#### Clean success

The route opens, provides material relief, lowers effective isolation, and may reduce Pressure. The host remains publicly neutral.

#### Profitable leakage

The route works but the host extracts a high price. The target receives supply relief while accepting a persistent commercial concession or higher route cost.

#### Partial exposure

The target receives short-term supply, while coalition suspicion rises. Evolution I can convert this state into direct pressure on the host.

#### Public exposure

The route closes or becomes expensive, Pressure rises, the host must answer a coalition ultimatum, and future smuggling through the same route becomes harder.

### Network management

The target should have a small cap on active networks. One or two active routes are enough for baseline. Evolution II can raise the cooperation cap for embargoed states.

The category should not display every possible border and port at once. Use a selected-target flow and hide invalid routes.

### AI direction

AI should favor smuggling when legal replacement trade is scarce, suitable neighbors or ports exist, and the target can absorb the exposure risk. Weak AI governments should avoid repeated high-risk attempts after a public failure.

## Working response: Neutral Intermediaries

### Purpose

The target offers favorable trade, access, contracts, political support, or future concessions to a country outside the coalition. The intermediary legally or semi-legally resells goods, issues certificates, provides shipping, or acts as a diplomatic channel.

### Candidate quality

A good intermediary has at least one of these advantages:

- access to resources the target lacks
- a usable land or sea route
- shipping or financial capacity
- favorable relations with the target
- weak alignment with the coalition
- strong commercial interest
- faction or subject ties that reduce enforcement risk

The candidate list should rank useful states and hide countries that cannot provide a meaningful route.

### Negotiation structure

The target makes an offer. The intermediary can:

- accept the initial terms
- demand a larger economic concession
- demand political access or support
- accept secretly
- refuse because coalition pressure is too strong
- disclose the offer to the coalition

Human-controlled intermediaries receive the choice directly. AI responses use relations, profit, alignment, fear of sanctions, route capacity, and war state.

### Costs

Suitable prices include:

- civilian factory use
- resource export preference
- production license or research cooperation when supported
- political support
- military access
- a temporary trade agreement
- convoys or fuel
- a future diplomatic obligation

The player-facing action must state the public price before acceptance. Hidden disclosure chances and future incidents can remain uncertain.

### Outcome

A functioning intermediary lowers effective damage immediately and can lower Pressure if the coalition cannot stop it. The route can become a target under Evolution I.

The target should not stack unlimited intermediaries. Baseline should support one main route and one limited backup. Additional candidates can replace a failed route.

### AI direction

Weak and import-dependent targets should favor this action. AI should reject an intermediary whose price is greater than the expected economic relief or whose route is already blocked.

## Working response: Diplomatic Concessions

### Purpose

Concessions exchange lasting policy or strategic value for coalition defection or a negotiated end.

### Target selection

The target chooses the convenor or one core participant. Minor background members should not each offer a separate concession decision.

### Concession families

The offer should follow the public justification and current campaign state:

- withdrawal from a disputed area
- pledge against further claims
- guarantee or non-aggression commitment
- inspection or monitoring access
- compensation for nationalized property
- preferred resource or commercial contract
- debt settlement
- end to foreign political support
- release or autonomy arrangement where directly relevant
- basing, transit, or strategic access

The implementation must not create territorial concessions that the target cannot deliver or promises involving dead countries and invalid states.

### Settlement strength

A minor concession can convince one conditional participant to leave. A major concession can create a coalition-wide settlement vote. The player should know the public commitment before accepting it.

### Costs and persistence

Concessions survive the end of the crisis for a defined term or until their obligation is fulfilled. They should not disappear when Pressure reaches zero.

A repeated Event 50 can use the target's history of compliance or broken concessions as a coalition factor. It should not restore the old crisis ledger.

### Failure

A rejected concession can strengthen hardliners, reveal weakness, or increase the price of the next offer. Repeated identical offers should be blocked.

### AI direction

Weak targets, governments already losing a war, and states with critical dependence should favor concessions. Strong targets should still concede when the requested cost is limited and the embargo threatens a more important war objective.

## Working response: Defy the World

### Purpose

The target accepts prolonged isolation and uses the coalition as a domestic political narrative. The response turns economic pressure into emergency mobilization, rationing, propaganda, and siege-economy organization.

### Immediate effect

Defiance should provide a noticeable temporary package suited to the target:

- improved war support or political cohesion where valid
- reduced immediate factory disruption
- faster emergency conversion
- stronger rationing and stockpile controls
- improved resistance to diplomatic pressure

It should also create costs:

- coalition resolve can increase
- consumer welfare and civilian construction suffer
- long-term production efficiency can deteriorate
- democratic or pluralist governments pay a political cost
- authoritarian governments risk deeper repression or post-crisis exhaustion

### Regime variation

Authoritarian regimes with strong legitimacy claims can gain more domestic cohesion from defiance. A fragile regime may fail to convert the embargo into support. Democratic governments can form emergency unity, but should face parliamentary or electoral resistance when the crisis continues.

The event should not assume every dictatorship benefits automatically. Current stability, legitimacy, ideology, recent defeats, and public justification all matter.

### Commitment

Defiance is a strategic commitment, not a free temporary buff. Entering it should close or weaken some concession options for a period. Leaving it early can create a credibility penalty.

### End state

A target that survives severe Pressure through defiance can keep a bounded self-reliance or political-memory outcome. It also receives exhaustion that removes the temporary surge and creates a recovery period.

### AI direction

Strong, isolated, ideological, and militarily capable AI targets should consider defiance. Weak AI targets should avoid it when critical shortages are already breaking their army or economy.

## Working response: Resource Seizure

### Purpose

Resource Seizure converts economic desperation into a military project. It should appear only when the target faces severe Pressure or a proven critical shortage and a plausible nearby resource target exists.

### Availability

The action requires:

- Pressure in the severe band, normally 70 or higher, or an equivalent critical shortage
- one nearby or strategically reachable state group with relevant resources
- a valid owner that can be threatened or attacked
- sufficient military strength to make preparation credible
- an aggressive government, route, strategy, or emergency political decision
- no existing war state that makes a duplicate preparation nonsensical

### Preparation mission

The action starts a 120 to 180 day objective. The target must prepare forces, supply, fuel, and equipment for a named resource region. The mission should use real map and stockpile requirements.

Possible requirements include:

- supplied divisions positioned in named border or staging states
- a minimum fuel reserve
- available trains or convoys for the route
- control of a named port or railway
- sufficient equipment for the committed force

### Outcomes

#### Coercive access

The owner accepts an ultimatum and grants temporary resource or trade access. The target avoids war but Pressure rises and the owner may seek protection.

#### Limited occupation plan

The target receives a bounded war goal or border-conflict route focused on the resource region. No free cores are granted.

#### Coalition intervention

A core enforcer guarantees or supports the threatened country. The military route becomes harder and the embargo can harden into wartime enforcement.

#### Abandoned preparation

The target cancels or fails the mission. It loses credibility, wastes part of the committed stockpile, and returns to economic responses.

### Chaos handling

Issuing a serious resource ultimatum can produce one event-owned Chaos milestone. A war, annexation, puppeting, casualties, and occupation use their normal shared Chaos and Deaths sources. Event 50 must not duplicate those gains.

### AI direction

Aggressive AI can choose this route when military strength, supply, and target vulnerability make success plausible. It should refuse suicidal wars against a stronger faction merely because Pressure is high.

## Action replacement by phase

### Opening phase

Usually visible:

- Self-Sufficiency
- Smuggling Networks
- Neutral Intermediaries
- Diplomatic Concessions
- Defy the World
- Secure Replacement Supply mission

The category should cap primary actions at five. When all five response families are technically available, a selected-target flow or phase choice can keep the list within the cap.

### Severe phase

Resource Seizure can replace the least relevant ordinary action. An emergency version of Self-Sufficiency can replace its slower opening version. Failed intermediary targets should disappear.

### Fracture phase

Coalition-splitting diplomacy, settlement votes, and exposed-trader management replace opening setup actions. Completed project families collapse into status entries or upgraded actions.

### Resolution phase

Only the actions needed to complete the chosen settlement, cancel invalid commitments, or handle the immediate aftermath remain visible.

## Decision exploit controls

- Permanent resource or building gains have project ceilings.
- Repeated concessions cannot buy the same participant several times.
- Smuggling routes use unique hosts and active caps.
- Intermediary agreements carry persistent costs for their full term.
- Defiance cannot be toggled repeatedly for temporary bonuses.
- Resource Seizure needs a valid target and consumes a real preparation commitment.
- Crisis-ending actions cannot be repeated after resolution begins.
- A later firing creates new decision state while respecting durable prior investments and obligations.
