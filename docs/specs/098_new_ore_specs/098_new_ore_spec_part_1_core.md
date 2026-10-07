# Event 098: New Ore

## The material and the territory

One previously unknown mineral is discovered in one randomly selected state. Its alloy gives armor an immediate, exceptional advantage. The deposit belongs to the place where it is found. The country physically controlling that place receives the strongest benefit, and conquest transfers that benefit to the new controller.

The discovery creates a strategic prize that can appear in an industrial heartland, a remote colony, an island, a mountain district, or an otherwise unremarkable border state. Its location changes the campaign. A small country can acquire bargaining power far beyond its industrial size. An armored major can gain a decisive advantage and become dangerously dependent on one exposed state. The material remains valuable after rival deposits appear because every source provides direct access, denies a rival that access, and can support selected foreign partners.

The deposit is a persistent state feature. It is represented by its own ore identity, state marker, visible state information, and access rules. The game does not turn it into ordinary steel or tungsten. Existing national research, production, doctrines, diplomacy, and military operations remain the means through which countries exploit the advantage.

The event retains ID `098`, the name **New Ore**, classification **Minor Fire-Once**, opening Chaos level **1**, and **Positive Economy, High member**. Fire-once applies to the initial global discovery. Later discoveries are consequences of Evolution II within the same active event.

All additional labels in this package are working labels, not final localisation. The four evolution names supplied by the user are retained.

## What the player must be able to rely on

The first deposit grants its current controller at least 50% more actual armor on every applicable armored force and equipment consumer. Existing equipment and deployed forces benefit immediately. Newly produced, newly deployed, captured, licensed, and imported applicable equipment uses the same current access rule when it belongs to that country.

The bonus does not depend on selecting a particular model, editing a particular template, researching a special tank, paying for initial exploitation, or constructing a refinery. The discovery is already usable when announced. A poor country receives the same direct material advantage as a rich country. Its economy, armed forces, fuel, supply, and ability to defend the deposit determine what it can accomplish with that advantage.

The ore changes armor. The specified percentage is not an attack, defense, hardness, breakthrough, production, speed, reliability, or hit-point bonus. Normal combat relationships continue to apply. Strong armor can still be met by sufficiently strong piercing, air power, isolation, supply failure, encirclement, or loss of the source territory. The design does not promise a proportional reduction in casualties or an automatic victory.

### Measuring the armor promise

For each applicable consumer, compare its actual armor with and without Event 098 access while preserving the same equipment, strength, technology, doctrine, other events, and other modifiers. Call the value without Event 098 `A0` and the required value with it `A1`.

At baseline, `A1` must be at least `1.50 × A0`. Deep Vein raises the intended floor to `1.75 × A0`. The Super-Alloy raises a single directly controlled deposit to `3.00 × A0`. These are effective outcome requirements. An authored modifier of `0.50` is insufficient evidence if additive stacking produces a smaller relative increase.

Consumers with zero armor remain at zero from this event. The ore strengthens armor that exists. A force is not excluded because its equipment uses an unexpected category name or its armor originates partly in a custom subunit. The coverage review must include conventional tanks, tank derivatives, mechanized and armored-car families where they have armor, armored naval equipment, and custom armored forces. For custom corporeal forces, protective fittings can express the material in their existing visual identity. The implementation must inventory positive armor contributions and resolve any genuinely incompatible consumer explicitly.

Aircraft statistics that describe a different property must retain their own meaning. A surface without an actual armor statistic cannot be declared covered by relabelling air defense as armor. If a supported custom aircraft or other consumer does expose actual armor, it belongs in the coverage review.

The broad coverage and effective floor remain requirements wherever the engine implementation needs further proof. The implementation handoff identifies that proof separately from this design.

## Selecting the first state

Select uniformly from the complete eligible state pool, directly at state level. Each eligible state has the same chance. Selecting a country first would give countries with fewer states a different per-state chance and would violate this rule.

A valid state is a real state on the playable map with at least one traversable land province and a valid current country controller. Pure system carriers, non-map placeholders, sea-only entries, and structurally unusable states are excluded through shared, documented validity rules. Their exclusion must describe why the place cannot function as ordinary territory.

Population, existing resources, industry, infrastructure, terrain, ownership, core status, ideology, faction, human control, war status, armored strength, and distance from the player do not weight selection. Zero-industry and sparsely populated states remain eligible. Occupied territory, colonial territory, puppet-controlled territory, and active fronts remain eligible. Special Chaos countries are not excluded merely because their armies are unusual.

The chosen state is recorded before announcing the discovery. The event validates its current controller again when applying access. If the state remains valid but control changed during resolution, the new controller receives the benefit. If the state became structurally invalid before the discovery was committed, choose again from the current complete valid pool. A failed attempt does not create a phantom deposit or consume a successful discovery receipt.

If the valid pool is empty, discovery waits for a valid opportunity. It does not substitute a capital, a named country, Greenland, or the event recipient's own territory. A diagnostic reports the empty pool in the implementation environment.

## The opening experience

The controller receives an immediate report centered on the material's observed resistance to damage, the deposit's location, and the strategic opportunity. The armor effect is active when the report appears. Acknowledging the report does not apply the effect a second time.

Other countries receive one global news announcement identifying the state and its controller. This information is public because territorial competition is the event's main engine. Other governments know where to negotiate or fight. The story can leave the mineral's origin and complete properties uncertain without concealing the current armor benefit from its recipient.

The controller's first practical choices concern access. It can reserve the material, entertain commercial offers, support a security partner, or allocate access within its faction. The default is a military monopoly. Remaining with that policy carries no upkeep or hidden decay.

Foreign countries can inspect the source state and approach the controller. Their first useful information is the direct advantage, the weaker access available to them, who controls the source, and whether a valid agreement is available. A country that lacks an armored force can still value diplomatic income, future military development, or denial of the deposit to a rival.

## Current control decides access

| Territorial situation | Direct beneficiary | Consequence |
| --- | --- | --- |
| Owner and controller are the same country | That country | Full direct access |
| Another country occupies the state | Occupying controller | The legal owner receives no direct benefit from its ownership alone |
| A subject controls the state | The subject | The overlord needs a separate foreign-access agreement or direct control |
| A faction member controls the state | That member | Faction membership creates a possible agreement route, not automatic full access |
| State control changes in battle | New current controller | Recalculate old and new countries in the same control-change resolution |
| A peace settlement changes ownership but leaves control unchanged | Existing controller | Keep its current benefit and valid contracts |
| A release, annexation, civil war, or transfer changes control | Resulting controller | Recalculate using the actual resulting state and country identities |
| The state temporarily has no valid controller | Nobody through that state | Keep the geological deposit, suspend its direct contribution, and terminate its source agreements |

The old controller loses only the part of its access that depended on the lost state. It may retain direct access from another deposit or weaker access from a surviving agreement. Its country must not briefly drop to zero and receive an unrelated source's bonus twice during the recalculation.

The new controller receives direct access immediately, including existing applicable forces. This transfer is a deliberate gameplay abstraction for access to ongoing material supplies, standardized protective components, and national deployment of the alloy. Permanently tagging every manufactured tank with the ore would preserve the previous controller's advantage after losing the source and would contradict the event's central territorial rule.

The deposit cannot be moved in stockpiles, evacuated with a capital, sold separately as an inventory object, exhausted through ordinary production, or destroyed by an ordinary change in control. Ordinary bombing, damaged infrastructure, resistance, and occupation conditions continue to affect the territory through their normal systems. They do not reduce the promised direct armor floor while a country controls the valid deposit.

## Forces serving abroad

The material entitlement follows the country to which the force or equipment belongs, rather than the province in which it is currently fighting. Volunteers abroad retain their owning country's entitlement. A host does not gain full ore access merely because an allied armored division enters its territory.

Expeditionary forces require explicit ownership-versus-command validation. The intended result is that temporary operational command does not export a country's permanent armor entitlement or grant its entire host army access. If a specific engine consumer evaluates the commanding country, the implementation must resolve that discrepancy rather than leaving an undocumented loophole.

Lend-lease and equipment capture transfer equipment ownership normally. The recipient evaluates the equipment under its own current ore access. A former controller cannot export permanently enhanced legacy equipment after losing the state, and a current controller can strengthen received older equipment. Designers and production licences do not act as mineral-access licences.

## The two public values

The mechanic exposes two persistent aggregate values: **current armor advantage** and **directly controlled deposit count**. The first communicates present military strength. The second explains access, territorial concentration, and later diminishing returns.

Named state records, partner identities, agreement terms, and deadlines are actionable records. They do not become separate prestige, extraction, refinement, influence, monopoly, or threat meters. Hidden AI assessments and timing calculations feed decisions and qualitative explanations.

Use a consistent steel-blue identity for the armor advantage and an ore-stone motif for deposits. Accompany color with explicit labels, icons, numbers, and state names. A loss report explains which source changed and what the resulting advantage is.

## The durable strategic loop

The controller decides how much access to share and uses normal military and diplomatic tools to keep the state. A customer decides whether weaker access is sufficient, whether a second supplier is worth securing, and whether its partner can defend the deposit. A rival decides whether to bargain, strengthen its own piercing and operational counterplay, support a competing source, or pursue the territory.

Every new deposit changes these choices without erasing earlier decisions. Existing agreements can become expensive compared with new alternatives. A former monopolist can become a reliable supplier or attempt to reunify the sources. A newly fortunate minor can attract a protector, buy time with exports, and build an armored army around its direct advantage.

The material remains powerful at every stage. Limits operate through geography, access commitments, ownership risk, export selection, and diminishing additional deposits. They do not dilute the baseline armor promise.
