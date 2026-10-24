# Investment specification, part 2: Sector projects

## 1. The charter must promise a particular result

The sector determines what the country will own when construction finishes. Before funding, the proposal identifies each principal building, each supporting improvement, the exact state or coastal province, the delivery phase and the commissioning dividend. A generic promise of industrial growth is insufficient.

All labels below are working design labels. Final text is commissioned through part 5. The ordinary envelope provides U principal units, with U equal to 1, 2 or 3 for Small, Standard or Large. Variant substitutions are applied before the final quote. A principal unit is a design allocation, not an interchangeable currency that the player can repeatedly convert between factories, facilities and resources.

| Envelope | Civilian or military main branch | Naval main branch | Strategic materials | Experimental engineering |
|---|---|---|---|---|
| Small, U = 1 | 1 sector factory | 1 dockyard | 1 refinery | 1 native facility, or the defined engineering-complex alternative |
| Standard, U = 2 | 2 sector factories | 2 dockyards | 1 refinery and 1 civilian support factory | 1 facility or alternative, plus 1 civilian support factory |
| Large, U = 3 | 3 sector factories | 3 dockyards | 1 refinery and 2 civilian support factories | 1 facility or alternative, plus 2 civilian support factories |

The supporting improvement and temporary dividend are additional elements explicitly included in the quote. Engineering's alternative contains two physical factories because it represents a usable industrial package in a game without the native facility feature. Its larger number of factories must fit real slots. It is not a hidden second reward granted alongside a facility.

### Quote arithmetic and phase rounding

The ordinary nominal schedules are 300, 360 and 420 funded days at holds of 1, 3 and 5 civilians. Special industry multiplies nominal work and duration by 1.5. Apply the selected policy and site factors, divide nominal work into 25%, 50% and 25%, then round each phase's required duration upward to a five-day boundary at its integer hold. The accepted phase work is the hold multiplied by that rounded duration. Freeze the sum of the three accepted phase work quantities.

For example, a neutral Small special project has 450 nominal days. Its unrounded phase durations are 112.5, 225 and 112.5 days. The actual quote is 115, 225 and 115, totaling 455 days. The UI shows 455, and the paid-work ledger owes 455 at a one-factory hold. This is transparent design arithmetic, not an observation of native engine timing.

A later amendment rounds only prospective work. It preserves already paid work and established due dates. Construction speed benefits from this event must not recursively discount its own accepted work quota. The quoted subsidy is already represented in the Investment envelope.

### Exact site work factors

Apply the following additions to one site factor after the sector and policy factors, then perform the normal phase rounding. In a multi-state program, each site's factor applies to that site's allocated nominal work.

| Accepted condition | Addition to the site factor |
|---|---:|
| Site is owned and controlled but non-core | +10% |
| Current infrastructure is below half the installed native maximum | +10% |
| Payer is at war | +10% |

The site factor is `1 + applicable additions`, capped at 1.30. Thus a non-core low-infrastructure site in a wartime country uses 1.30 once. Use the exact comparison `2 × current level < native maximum` for the infrastructure condition. There is no additional unspecified supply or geography multiplier. Supply and legal control are preconditions, and later disruption uses the declared pause or incident rules. Freeze these factors at purchase. A later accepted amendment may quote genuinely new remaining work from current conditions without repricing paid work.

The normal expected duration ranges are 180–720 funded days for ordinary non-special projects, 270–1,080 for ordinary Special projects, and 360–1,440 for Fever programs. For example, a neutral Large Special verified tender starts at `420 × 1.5 × 1.2 = 756` nominal days before phase rounding, so it belongs in the Special range. A prospective oversized quote must offer a smaller viable scope or document an exceptional balance choice before purchase. Its work cannot be silently shortened to fit a target duration.

## 2. Site selection and supporting works

The proposal presents the three best legal candidates, or fewer if only one or two exist. Ranking favors ownership and control, supply access, available slots, relevant infrastructure, a usable port for naval work, suitable neighboring states for later expansion and lower disruption. Core status is a preference. A legal owned non-core state can qualify when its actual stability and control permit construction. Its work factor is fixed above and its contextual Exposure follows Part 3. Supply loss pauses work rather than adding an undefined multiplier.

Each candidate preview lists the promised outputs and explains any unavailable variant. A candidate cannot be offered merely because its state name is plausible. Factories need current building capacity. Naval bases need a valid coastal province. Refineries and special facilities need their actual construction permissions. Supporting rail work needs a valid route whose endpoints and edges exist.

Infrastructure support normally adds one legal level to the main site. If that level is already capped at quotation, select a legal support state within the two-state ordinary footprint, or offer the same principal factory package with a smaller work requirement. The reduced quote removes the support's cost share. It does not exchange a capped infrastructure level for an unpriced factory.

The accepted quote assigns a work share to every output. At minimum, enabling works must be fully paid before delivery and the principal output's own share must be fully paid before that output appears. The sum of all allocated output work, survey work and commissioning work equals the accepted total. These shares are part of the authored sector data and must be checked against current native relative construction costs. They are not recomputed from whichever bonus is most convenient at completion.

If a legal slot disappears after purchase, the project tries its preselected legal replacement site once, subject to the same beneficiary and scope. Otherwise it offers a smaller settlement or a bounded relocation amendment. A capped or invalid output must not be silently omitted from a full-success receipt. Part 4 owns the paid-work preservation and settlement transaction.

## 3. Civilian industry

### 3.1 Manufacturing estate

The government backs a group of workshops, utilities and production halls intended to widen the ordinary economy. It receives U civilian factories and one infrastructure level. A larger envelope should feel like a connected estate with suppliers and handling space, rather than several unrelated factory gifts.

Mobilization establishes the plan and the supplier agreements. Works completes the enabling infrastructure and, for U of at least two, may open one fully paid factory. Commissioning opens the remaining factories. The dividend grants +10% civilian-factory construction speed for 180 days, reflecting the useful network of contractors and equipment left by the completed program.

A supplier delay increases work still needed to finish the estate. A cost overrun can come from power, foundations or handling requirements that the original bid understated. A corruption incident concerns phantom material deliveries, duplicate invoices or a favored subcontractor. The response must identify what the investigation can still prevent. It cannot return labor that has already been spent.

### 3.2 Utilities and fabrication

This variant concentrates on the conditions for further industrial development. When U is at least two, it trades one promised civilian factory for an additional infrastructure improvement and transport support. The result is U minus one civilian factories, two infrastructure levels distributed across at most two states, and one level of improvement on one existing legal railway segment where that addition was included in the quote.

The railway support is a real, bounded improvement to a verified segment. It cannot invent a new national corridor. If no valid segment exists, the quote can instead include one additional legal infrastructure level within the same two states. If that substitute is also unavailable, the proposal shows the smaller output and removes its prospective work share before purchase.

For Small, the physical package remains one civilian factory and one infrastructure level. Its distinctive return is the utility-focused dividend, +15% infrastructure and railway construction speed for 180 days through verified native modifier channels. If the installed engine lacks a distinct supported railway speed channel, use the supported infrastructure channel plus a prequoted legal railway work component. Do not invent an ignored modifier and present it as a functioning reward.

The larger variant is useful when poor transport limits future development or supply. It sacrifices immediate factory count for enabling work. A player choosing it must see that trade clearly in the proposal. Losing a supporting state before completion removes that state's undelivered work from eligibility and exposes the remaining fabrication site to an explicit smaller-scope decision.

### Historical grounding

TVA's own account describes a coordinated development program joining power, navigation and flood control. That supports the design inference that enabling infrastructure should have a strategic role in an investment program. Investment's factory counts, completion times and bonuses are game design, not measurements of TVA. [TVA, Building a Better Life for the Tennessee Valley](https://www.tva.com/about-tva/our-history/built-for-the-people/building-a-better-life-for-the-tennessee-valley).

## 4. Military industry

### 4.1 Arsenal expansion

The government funds additional production halls and the services needed to operate them. The output is U military factories and one infrastructure level. Commissioning grants +10% factory output for 180 days. The factory capacity joins ordinary production. The project does not imply that a new tank, aircraft or weapon has already been researched or produced.

The main choice is whether the country can afford to divert civilian industry now for future equipment production. A peacetime minor can use the Small envelope to establish an arsenal. A country fighting a defensive war might prefer an accelerated contract, while a country facing imminent loss of the construction state should prefer a safer site or decline.

Its incidents emphasize engineering change, machine-tool deliveries and unrealistic contractor schedules. An urgent military specification can be legitimate while still increasing the cost. The event should give the player evidence to distinguish that case from fabricated invoices. Changing the machinery or contractor alters unfinished work and its completion schedule, not the country's existing production lines.

### 4.2 Precision production

For U of at least two, this variant trades one military factory for two one-use 50% research bonuses restricted to industrial or production technology and a precision dividend. The physical output is U minus one military factories and the normal infrastructure support. Small retains its one military factory and pays 20% additional required work for the specialist package.

The dividend contributes +10% production-efficiency cap and +5% production-efficiency growth for 180 days inside the same consolidated commissioning family. It does not create a fourth spirit. The research bonuses are issued once from the commissioning receipt, with their actual categories checked against the installed technology definitions. They cannot complete an unavailable technology, select mutually exclusive industry branches for the country or grant a special project's payload.

This choice suits a government that already has production lines worth improving or needs industrial technology more than one additional factory. It should be a weaker default for an AI country with almost no military production. The AI compares useful capacity and technological opportunity instead of blindly preferring a larger number of modifiers.

An unfinished precision project can be reduced to the ordinary retained factory package by dropping the undelivered specialist benefits and their unpaid work share. Once the bonuses have actually been awarded, cancellation cannot pretend they remain refundable. The completed receipt prevents a second award through target changes.

### Historical grounding

The Henry Ford's Willow Run collection documents worker training, assembly planning and disruption caused by design changes. These support the design's separate works and commissioning phases and its legitimate rework incidents. The game does not reproduce Willow Run's output rate or claim that every military factory experiences the same history. [The Henry Ford, Willow Run Bomber Plant](https://www.thehenryford.org/collections/explore/sets/detail/willow-run-bomber-plant).

## 5. Naval industry

### 5.1 Shipbuilding yard

The main naval branch delivers U dockyards and one naval-base level in a valid coastal province belonging to the selected state. The site needs legal dockyard slots, control and a real supply connection. The commissioning dividend grants +10% dockyard output for 180 days.

This is a durable shipbuilding investment. Commissioning a yard does not also deliver a finished fleet. Its reward becomes useful through ordinary naval production and the country's researched ship designs. A country with limited naval experience can still buy capacity, but the AI should account for whether it can use it.

The project narrative should make the shore visible. Slipways, dredging, cranes, access roads and workshops create the sense of a place. Its incidents concern specialized machinery, berth construction or a contractor claiming work that the site inspection cannot find. A disrupted port can delay the program even when the inland government still controls the state.

### 5.2 Repair and maritime logistics

When U is at least two, this variant trades one dockyard for an additional port level and one infrastructure level. The output is U minus one dockyards, two naval-base levels and one infrastructure level. Small retains its one dockyard and pays 20% extra work for the additional support package.

The commissioning dividend grants +15% naval repair speed for 180 days. This branch is attractive to a country with a damaged fleet, limited basing infrastructure or a geographically important port. It is less attractive when its useful ports are already capped and the country has little naval activity.

The proposal must allocate naval-base levels to legal coastal provinces. If only one additional port level is possible, it can offer a prequoted infrastructure substitute within the accepted footprint. If the support cannot be legally delivered, the offer is smaller and cheaper before funding. It must not silently describe a two-level port expansion while delivering one.

Landlocked countries retain the naval sector row with a concise geographic explanation. They can choose another sector. A new inland dockyard, an arbitrary foreign port transfer or a civilian-factory substitute would break the selected sector's premise.

### Historical grounding

The Maritime Administration describes existing yards reaching capacity and the construction of emergency yards and slipways. Its account also links production speed to scarce components and simpler designs. The design inference is that naval investment should expand usable capacity with identifiable bottlenecks. [MARAD, The Emergency Shipbuilding Program](https://www.maritime.dot.gov/multimedia/emergency-shipbuilding-program).

## 6. Special industry

Special industry covers facilities whose value depends on specialized processes and supporting expertise. Its two branches give the sector a concrete identity. It is not a generic random reward button.

### 6.1 Strategic materials

The package delivers one synthetic refinery, U minus one civilian support factories and one infrastructure level. The refinery must be constructible for the beneficiary under current technology and game rules. A quoted refinery cannot appear merely because the player selected the Special sector.

The 1.5 work multiplier applies to the whole package. This branch turns a larger construction commitment into a durable source of strategically useful materials and a small supporting industrial base. Its dividend gives +10% resource-gain efficiency for 180 days through a verified supported modifier. The temporary dividend is distinct from the refinery's own ordinary output.

Supplier incidents can concern pressure vessels, specialized processing equipment, feedstock handling or an understated installation cost. Corruption can involve nonexistent imported machinery or materials recorded twice. These are design directions for fiction and presentation, not instructions for manufacturing a real chemical product.

If the refinery is unavailable at proposal time, this branch is blocked with the relevant reason and Experimental engineering remains available if legal. A later loss of legal delivery uses the ordinary relocation or reduced-scope settlement. It does not grant an unresearched refinery or automatically switch a prepaid project to a different reward.

### 6.2 Experimental engineering with native facilities

Where native special-project facilities are available, the package delivers one legal facility of the selected specialization, U minus one civilian support factories and two one-use 50% industrial or production research bonuses. It also includes the enabling infrastructure in the accepted quote.

The specialization chooser is a bounded proposal step. It offers only currently legal categories and valid sites. It checks the one-facility-group-per-state constraint, exact building permission, actual owner/controller, supply and any coastal requirement for naval specialization. The current CXT documentation supplies these legality requirements, while implementation must bind them to installed native definitions. [CXT facility evidence](121_investment_sources_and_review.md#source-register).

The facility enters normal use after commissioning. Its presence does not mean a special project has been completed. Scientists, breakthrough progress, research gates, prototype tests and payloads remain with their owning native or Chaos Redux project systems. The research bonuses support ordinary industrial development and do not bypass those project gates.

Its commissioning dividend is +5% research speed for 180 days, recorded inside the consolidated family and dependent on the qualifying site. This is a proposed broad knowledge spillover, deliberately smaller than the output dividends. The one-time bonuses and facility form the main reward.

### 6.3 Experimental engineering without the native facility feature

The alternative is a precision-engineering complex with one civilian factory, one military factory, U minus one additional civilian support factories, the same enabling infrastructure and the same two one-use 50% research bonuses. It uses the same longer Special work envelope and the +5% research dividend.

This is a complete industrial route with real slots and payment. It is selected and frozen when the charter is accepted. Changing DLC availability, a loaded ruleset or the selected site cannot award both the alternative and a facility. The receipt carries the capability mode and every output is checked against it.

Comparable value means that the alternative offers a substantial productive and technological payoff for a similar opportunity cost. It does not mean a facility and two factories are numerically identical. Part 6 requires all-DLC and no-DLC comparisons in representative small and medium economies. Any balance adjustment belongs in the authored alternative package before accepting a new charter, not in a late silent reward reduction.

### 6.4 Reduced special-industry completion

The government can drop unbuilt support factories, the research bonuses or the dividend in a smaller completion agreement. It cannot label an ordinary office a native research facility. If the principal facility cannot legally be commissioned, the player must receive an explicit alternative contract, relocation or honest partial wind-down.

When only the principal engineering complex remains, minimal completion preserves its necessary functional buildings. Its new quote removes only genuine optional work. A program cannot claim a complete research campus after delivering one unrelated civilian factory.

### Historical grounding

The Department of Energy's Oak Ridge history describes several specialized industrial facilities with distinct functions, construction demands and long-term cleanup consequences. That supports the sector's emphasis on facilities, support and lifecycle responsibility. Impossible Industry's supernatural methods are fictional and are not scientific claims about those historical installations. [DOE, Oak Ridge history](https://www.energy.gov/orem/history).

## 7. Commissioning dividends and custody

| Route | Proposed 180-day contribution |
|---|---|
| Manufacturing estate | +10% civilian-factory construction speed |
| Utilities and fabrication | +15% infrastructure and supported railway construction speed |
| Arsenal expansion | +10% factory output |
| Precision production | +10% production-efficiency cap and +5% efficiency growth |
| Shipbuilding yard | +10% dockyard output |
| Repair and maritime logistics | +15% naval repair speed |
| Strategic materials | +10% resource-gain efficiency |
| Experimental engineering, either capability mode | +5% research speed |

These contributions share one visible commissioning-dividend family. The strongest currently valid contribution of the same type applies, with no additive stacking from repeated receipts. Distinct contributions may coexist within that family only if the underlying independently earned expiry records remain valid. The normal 540-day funded-outcome cooldown makes repeated overlap uncommon.

A Fever program uses its chosen route's table amplitude through one program-level receipt. Full completion of all mandatory sites and links grants 180 days. Agreed reduced terminal commissioning that retains at least one usable principal site grants 90 days. Early site commissioning gives physical assets without an independent dividend. An abandoned or failed program that never reaches an agreed reduced commissioning gets no dividend. Freeze the completed qualifying site set at terminal commissioning. The program dividend requires control of every site in that set and retains its original expiry through a pause or recapture.

Impossible engineering throughput supplies a separate licensed research-speed contribution: +10% ordinary or +15% mega while inspected, and +20% ordinary or +30% mega at full risk. The strongest valid research-speed contribution applies, including the ordinary +5% dividend, without adding them together. The licensed contribution requires actual service and legal custody. Its separate two extra one-use 50% industry research bonuses are issued once at verified anomaly commissioning. They do not substitute for the continuing operating benefit. Both native and no-DLC engineering branches use these same rules.

The dividend belongs to the original beneficiary and qualifying commissioned site. Losing control removes its live contribution while preserving the original expiry. Recapture restores only the unexpired remainder. A new controller receives ordinary use of captured physical buildings, but not the previous government's research rewards, dividend clock or achievement credit.

A failed project may also own the capacity-commitment and economic-distress families. Keep the event's visible national modifier count at three through consolidation and replacement. An operational impossible benefit is represented within the same consolidated benefit family with its own exact source record. It must not create a fourth unrelated spirit simply because its art is different.

## 8. Rare variants that use the existing loop

Rare variants should change a decision or a visible consequence rather than add an unconnected reward roll.

| Variant | Trigger context | Mechanical change | Player-facing direction |
|---|---|---|---|
| Reusable brownfield | Valid same-payer reusable work at the chosen site | Consumes that one credit against corresponding new work, capped at 25% | Show the physical remnants and explain which paid work is still useful |
| Genuine design change | Military or special project with a documented change before commissioning | Larger justified rework cost, with lower corruption suspicion after inspection | Explain why the requirement changed and what the delay buys |
| False supplier invoice | A corruption checkpoint has frozen a fraudulent surcharge | Investigation removes the unjustified future charge and replaces the contractor | Evidence concerns deliveries and invoices, with uncertainty until examined |
| Port access interruption | Naval construction whose access becomes unusable | Pause the affected support work, release its hold and offer repair, relocation or reduction | The location and blocked access matter more than an abstract crisis adjective |
| Early usable unit | A larger site's first fully paid unit is ready before the remainder | Automatic partial commissioning under the receipt rules | Make the new capacity visible while the unfinished promise remains clear |
| Overqualified site | Existing infrastructure removes a genuinely unnecessary support component | A smaller prospective quote, with the principal result unchanged | Explain the work the government can avoid paying for |

These variants use the same charter, phase and payment identities. They do not refresh random-event pacing, multiply inspection allowances or create new public values. Their eligibility and AI response belong to the same owner predicates as the ordinary route.

The expanded multi-state versions and the three impossible methods are specified in [part 3](121_investment_spec_part_3_evolutions_and_consequences.md). The complete actions and settlement behavior are in [part 4](121_investment_spec_part_4_decisions_costs_and_lifecycle.md).
