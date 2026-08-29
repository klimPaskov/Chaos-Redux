# Great Depression 2.0 specification, part 7: Evolution III, The Second Great Depression

## Evolution role

The action, mission, incident, and stage labels in this file are structural working labels unless they come directly from the accepted brief. Final player-facing wording belongs to implementation.

The Second Great Depression turns Event 35 into a worldwide economic condition. International trade contracts, industrial orders weaken, construction slows, expensive policy becomes harder to maintain, and countries with existing Event 35 crises face stronger pressure.

The evolution creates one global episode and many local pressure states. It does not open the full national Event 35 category for every country on the same day. A country converts into the full crisis only when local vulnerability and world pressure justify it.

This evolution creates a recoverable global economic crisis while ordinary event play continues. Countries can recover, cooperate, exploit the crisis, or fragment into separate economic blocs.

## Availability and activation

The Second Great Depression becomes available at Totalen Chaos.

Normal activation should require:

- Event 35 is active in at least one valid country.
- Evolution III is enabled.
- The source country has active Evolution II or an inherited Evolution III floor.
- International contraction or contagion has reached a material scale.
- No global Event 35 episode is already active.
- The dynamic evolution delay has elapsed.

A base timing target near `120` days is appropriate after the conditions are met.

Activation accelerators:

- Several countries have Event 35 active.
- Financial Contagion has converted another major.
- A large origin reaches Economic Paralysis.
- A major Event 34 supplier boom collapses.
- Several important ports, markets, or clearing agreements fail.
- Totalen Chaos world conditions already include severe trade disruption.

Activation reducers:

- Most exposed countries are stabilizing.
- A coordinated rescue is active.
- Major supplier countries remain stable.
- World trade and convoy conditions are secure.
- The source country is recovering rapidly.

An Event 34 Evolution III collapse activates the enabled worldwide module immediately. It starts the global episode at a high opening condition, but it still uses the normal one-time registry and global-news contract.

Evolution logging adds zero Chaos. The first actual worldwide pressure application is a separate concrete outcome.

## Global episode identity

Only one active Second Great Depression global episode exists at a time.

The global ledger records:

- Episode ID.
- Activation date.
- Source country and source national episode.
- Activation source, including Event 34 collapse when relevant.
- Highest world contraction stage.
- Countries under lighter pressure.
- Countries converted into full Event 35.
- Active supplier countries.
- Major international agreements.
- Recovery proof progress.
- Guarded Chaos receipts.
- Global announcement receipt.

A later Event 35 Evolution III activation joins the active global episode and deepens it when valid. It does not create a second global category or worldwide announcement.

## Public global state

The player does not track a second raw global number. The system uses one qualitative world stage supported by hidden global pressure.

| World stage | Working label | Meaning |
| ---: | --- | --- |
| `1` | Market Shock | Credit, orders, and trade begin contracting across several countries |
| `2` | General Contraction | Most connected economies experience material output and construction pressure |
| `3` | Worldwide Depression | Full national crises are common and international recovery is failing |
| `4` | Fragmented Recovery | Some blocs and countries recover while others remain deeply depressed |
| `5` | International Reconstruction | World pressure is declining and final recovery proof has begun |

The stage appears in Event Details, relevant categories, and the global episode report. It is a category, not another player-managed meter.

## Hidden world pressure

The global system may calculate a hidden pressure score from:

- Industrial weight of countries in active Event 35.
- Severity of major economies.
- Number and strength of contagion links.
- Global convoy and trade disruption.
- Major supplier capacity.
- Active Event 34 boom demand.
- Collapse of supplier booms.
- International rescue commitments.
- Number of countries in recovery.
- World tension and war disruption only where they materially affect the economy.
- Major disaster, famine, or contamination pressure through registered shared sources.

The hidden score moves the qualitative stage and local pressure. It must not be shown as a raw global total.

## Initial world registration

On activation, Event 35 performs one bounded initialization over valid normal civilian countries. It classifies each country into:

- Protected or lightly exposed.
- Global Contraction pressure.
- Severe exposure.
- Existing full Event 35.
- Active Industrial Boom supplier.
- Invalid special actor.

After initialization, only registered countries are processed through sparse schedules. The event must not add a recurring daily or weekly scan over the whole world.

A later country can enter the registry through exact relationship, country-creation, Event 34, or Event 35 adapters.

## Global Contraction condition

Countries without the full crisis receive a dynamic national condition whose strength depends on local exposure.

It can affect:

- Factory output.
- Construction speed.
- Production-efficiency growth.
- Consumer or administrative capacity.
- Trade and convoy resilience.
- Stability pressure.

The condition should remain lighter than full Event 35 at the same time. It cannot become a substitute full crisis with no decisions.

Local pressure rises through:

- Trade and market dependence.
- Faction, subject, or credit links to depressed majors.
- Existing economic scars.
- Low stability.
- Concentrated industry.
- Blockade or convoy failure.
- Dependence on one supplier.
- Collapse of an active supplier boom.

Local pressure falls through:

- Self-sufficiency.
- Stable institutions.
- Diversified trade.
- Strong reserves.
- Recovery reforms.
- A successful regional clearing agreement.
- Aid from a stable supplier.
- Low exposure to the global market.

## Conversion into full Event 35

A country converts when:

- Global pressure is severe enough.
- Local exposure is high.
- The country remains materially vulnerable for the conversion delay.
- It uses normal civilian systems.
- It does not already have Event 35.
- No conflict contract blocks activation.
- A global conversion receipt does not already exist for the episode.

The consequence call records entry source The Second Great Depression, global episode ID, starting world stage, local exposure, supplier dependence, and starting Severity.

Conversion remains country-specific. Some countries can pass through the entire global episode under lighter pressure without opening the full category.

## International action families

### Regional Clearing Agreement

A group of valid countries keeps essential trade and payments working. Members commit convoys, fuel, civilian capacity, or reciprocal access. The agreement lowers exposure and can form an economic bloc.

Membership rules:

- Existing diplomatic or geographic relationship.
- At least two valid countries.
- A leader with enough capacity.
- No conflicting exclusive agreement.
- Clear exit and failure conditions.

### Coordinated Public Works and Reconstruction

Countries contribute to shared transport, ports, or industrial rebuilding. Projects target exact states or routes. Contributors receive trade, influence, or recovery benefits. Failed projects create a registered international shock.

### International Debt Conference

Countries negotiate standstills, restructuring, relief, or creditor guarantees. It can lower global finance pressure. It may create concessions, delayed payments, or blocs. It never grants a free global reduction.

### Protectionist Bloc

Members restrict outside trade and support internal supply. It can protect members from some external pressure while weakening global recovery, relations, and nonmember trade.

### Competitive Devaluation or Currency Break

A country seeks export or fiscal relief through currency action represented by event effects and trade policy. It can help locally while raising pressure on partners. The design should avoid claiming engine-level exchange rates that do not exist.

### Reconstruction Supplier Compact

Stable industrial countries commit orders and material to depressed partners. It creates demand for suppliers and relief for recipients. It also concentrates risk.

### Global Recovery Conference

Available during Fragmented Recovery or International Reconstruction. It requires several major participants, declining national Severity, and material contributions. Success advances the global proof. Failure can delay recovery or strengthen rival blocs.

## Industrial Boom supplier role

An active Event 34 country becomes an important supplier because foreign orders rise while other economies contract.

### Supplier demand

The boom gains:

- Stronger usable demand.
- Faster project progress where Event 34 permits it.
- Foreign influence or concessions from exact agreements.
- A chance to stabilize recipients.

The boom also receives:

- Higher Overheating.
- Freight and convoy pressure.
- Labor and maintenance strain.
- Greater exposure to foreign default.
- Stronger collapse consequences.

### Supplier choices

- Accept World Orders.
- Ration Foreign Contracts.
- Finance Reconstruction.
- Demand Concessions.
- Build a Supplier Bloc.
- Refuse Further Exposure.

These actions belong to Event 34's category through a reusable Event 35 adapter. Event 35 must not duplicate the full boom mechanic.

### Supplier collapse

When a supplier boom collapses:

- Event 34 starts or deepens Event 35 in the supplier.
- Global pressure rises through one guarded supplier-collapse receipt.
- Dependent countries receive exact local shocks.
- Unfinished reconstruction agreements are frozen or transferred.
- The worldwide stage may deepen.
- The supplier cannot remain marked as a stable boom.

## Stable non-boom suppliers

A country without Event 34 can still provide ordinary aid or reconstruction supply. It receives smaller benefits and costs. It does not gain Event 34's extreme output or Overheating system.

## Global stage progression

### Market Shock

- First worldwide pressure package applies.
- Worldwide news event fires once.
- Countries receive initial exposure classifications.
- Emergency national and regional decisions open.

### General Contraction

- Lighter global modifiers strengthen.
- More countries become eligible for full conversion.
- Supplier and protectionist blocs form.
- International rescue becomes important.

### Worldwide Depression

- Several industrially important countries have full Event 35 or high pressure.
- Trade and construction penalties are strongest.
- National recovery is harder.
- Social Collapse and contagion consequences become more common where enabled.

### Fragmented Recovery

- Some major economies have recovered or stabilized.
- Global pressure stops rising.
- Economic blocs compete over reconstruction.
- Countries can relapse if supplier or credit arrangements fail.

### International Reconstruction

- Most industrial weight is outside severe crisis.
- Final global recovery missions open.
- Lighter country pressure decays.
- Remaining national depressions continue independently.

## Global recovery calculation

Global recovery should consider industrial weight and should not rely on country count alone.

Positive factors:

- Major industrial countries in Stabilization or Recovery.
- Declining average Severity among active major crises.
- Reopened Depression Centers.
- Stable supplier capacity.
- Restored ports, convoys, and trade links.
- Successful clearing, debt, or reconstruction agreements.
- No recent large contagion conversion.

Negative factors:

- Major economies in Economic Paralysis.
- Supplier boom collapse.
- Several new full-crisis conversions.
- Failed international rescue.
- Severe global trade disruption.
- Major war or disaster shocks with real economic effect.

The final recovery proof should last at least `120` days under stable conditions. A major supplier collapse or new major-country depression can pause or reset it.

## End of global episode

The global episode ends when:

- The world stage has reached International Reconstruction.
- Weighted severe-depression pressure remains below the recovery threshold.
- No unresolved global emergency or supplier-collapse chain remains.
- The proof period completes.

Resolution:

- Removes or decays Global Contraction conditions.
- Closes international emergency decisions.
- Preserves valid economic blocs and agreements with post-crisis purpose.
- Leaves active national Event 35 crises in place.
- Records the final world stage, recovered industrial weight, supplier outcomes, and political blocs.
- Applies a guarded Chaos reversal only for matching Event 35 global pressure previously added.

## Global announcement role

The first actual worldwide pressure application uses one global news event and one dedicated super-event. They fire when several countries receive the worldwide condition, not when the evolution variable is logged.

The news event identifies the contraction as an international economic state, shows several kinds of public evidence, and names the origin country only when that origin is known. It must not imply that every country has the full national Event 35 crisis.

The super-event marks the first worldwide economic consequence of Evolution III. It receives one stable slot, one generated period scene, one verified quote, one unique licensed musical cue, and one guarded receipt. It must present a worldwide contraction that remains recoverable and must not fire again when later origins join the same global episode.

## News and reports

World news should cover:

- First application of worldwide pressure.
- Formation of a major clearing or protectionist bloc.
- Collapse of a critical supplier boom.
- Failure of a major recovery conference.
- Entry into International Reconstruction.
- End of the global episode.

Routine national conversions use country reports and Event 35 history.

## Chaos impact

Evolution III activation adds zero Chaos.

The first concrete worldwide pressure application may add one guarded major Event 35 Chaos change because it imposes real contraction across several countries. An initial working target around `+20` is proportionate to a worldwide economic outcome, subject to the shared Chaos balance review.

Additional guarded outcomes may include:

- Collapse of a critical supplier network.
- Several major-country conversions.
- Failure of a world recovery conference that deepens the stage.

Generic Chaos from war, deaths, annexation, ideology change, contamination, and world tension is not duplicated.

Ending the global episode may remove only the matching Event 35 global pressure that was previously added. The reversal should be capped by the recorded Event 35 contribution.

## Interaction with event clusters

A Negative Economy cluster firing cannot activate The Second Great Depression merely because several economic events fire together. The global evolution still requires Totalen Chaos, enabled evolution state, Event 35 source conditions, and its own dynamic progression or inherited Event 34 Evolution III collapse.

Cluster members can create economic shocks that later affect the hidden world pressure through exact adapters.

## Multiplayer

Every player sees the same global stage and world episode. Each country manages its own national Severity and decisions.

Foreign aid, supplier, bloc, and conference actions require clear source and target ownership. One player cannot pay another player's costs through a local-only UI without an accepted transaction.

The worldwide news event fires once globally. Country reports remain targeted.

## AI behavior

AI evaluates:

- Local Severity or exposure.
- Industrial weight.
- Trade and convoy condition.
- Stability.
- Faction and subject responsibilities.
- Supplier capacity.
- Active Event 34 Overheating.
- Expected bloc benefits.
- War state.
- Ability to pay international commitments.
- Rival influence.
- Global recovery stage.

AI should form or join blocs that match its actual relationships and needs. It should avoid accepting supplier orders that would push an Event 34 boom near collapse without a strong strategic reason. It should contribute to global recovery when the cost is affordable and the agreement protects vital partners.

## Disabled evolution behavior

If The Second Great Depression is disabled:

- No global episode starts.
- No worldwide pressure package applies.
- No Evolution III worldwide news event fires.
- Existing national Event 35 and enabled lower evolutions continue.
- Event 34 inherited Evolution III still raises national starting Severity and converts inherited regions, but global content remains off.
- A previously active global episode retires through a safe cleanup path without ending national crises or granting a recovery reward.
