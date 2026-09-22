# Law Upgrade
## Part 2. Law progression and firing behavior

## One step means one adjacent position

Every participating system supplies an ordered path toward wartime mobilization. The event reads the current position and selects its immediate successor. It does not repeatedly test the newly changed law during the same firing.

The starting position for each category is captured before that category is changed. A firing that reaches Total Mobilization stops there. It cannot then notice that the country is at Total Mobilization and advance a second time into Totalen Krieg!!!.

A country at the final enabled step stays at that step. No Political Power payment, substitute upgrade, extra War Support, or reserve credit replaces a capped step.

## Ordinary law directions

These are the player-facing reference paths. The owning systems remain the authority for the loaded campaign's actual definitions, including valid country-specific additions.

| Family | Forward wartime sequence |
| --- | --- |
| Economy | Civilian Economy → Early Mobilization → Partial Mobilization → War Economy → Total Mobilization → Totalen Krieg!!! |
| Conscription | Disarmed Nation → Volunteer Only → Limited Conscription → Extensive Conscription → Service by Requirement → All Adults Serve → Scraping the Barrel → Totalen Menschen!!! |
| Trade | Free Trade → Export Focus → Limited Exports → Closed Economy |

The extreme endpoints participate only when Evolution III is active and enabled. An already-held extreme law remains recognizable even when that evolution is subsequently disabled. The event must never mistake it for an unknown starting law and reset it.

A country-specific peacetime law can precede the ordinary first step when its owning system explicitly provides that ordering. For example, a future No Army law would need its own declared successor. The event does not create the future law or infer its place from the name.

## Why trade is a wartime direction rather than a universal improvement

The trade path increases domestic control over resources. It can sacrifice the benefits attached to more open trade. Closed Economy is not a new prohibition on importing equipment or resources. Its consequences should come from the loaded trade system rather than a separate Event 82 embargo.

Because every country moves together, an individual state's calculation changes as its trading partners restrict exports too. Resource-rich states retain more of their own production. Import-dependent states can face fewer suppliers. That interaction is part of the event's ordinary strategic consequences and does not need an extra trade crisis.

## Order within the worldwide firing

The event first determines the active evolution and eligible recipient countries. It then captures the relevant current laws and provider prerequisites for those countries.

Each recipient gains the appropriate War Support. Each eligible category advances once from its captured starting position. The resulting law combination receives the penalties appropriate to the resulting War Support.

The notification reports this completed outcome. It shows the old and new positions, capped categories where useful, and a clear reason for a genuinely blocked participating category. It must not imply that a category advanced when it did not.

This is a single world-time occurrence, not a sequence spread over several playable days. The underlying game may process countries in a deterministic order, but the player cannot exploit a pause between countries to accept a different profile.

## Results a category can produce

| Result | Meaning | Player consequence |
| --- | --- | --- |
| Advanced | A valid immediate successor was enacted | The new law and its normal consequences apply |
| At ceiling | No further enabled step exists | The current law remains |
| Structurally blocked | The next step has a real institutional or content prerequisite that is not met | The current law remains and the reason is available |
| Not participating | The category is not part of this evolution or is absent from this country | No change |
| Unrecognized law | The provider cannot place the current law in its declared path | Preserve the law and report the compatibility limitation |

An unrecognized law is not permission to guess. A blocked next step is not permission to leap over it. A category cannot borrow an upgrade from another category.

## Worked campaign examples

### A peaceful country at the beginning

The country begins with Civilian Economy, Volunteer Only, and Export Focus, with 20% War Support. A baseline firing gives it Early Mobilization, Limited Conscription, and 30% War Support. Export Focus remains unchanged because trade has not entered the profile.

A second baseline firing gives Partial Mobilization, Extensive Conscription, and 40% War Support. The country pays no Political Power for either forced step.

### A country that is already heavily mobilized

The country begins with Total Mobilization and Scraping the Barrel. Before Evolution III, those categories remain unchanged. It still receives the normal War Support increase for the active profile.

The result contains no capped-law Political Power reward. The event still counts as one genuine worldwide occurrence because the specified War Support operation and any other participating categories have been processed.

### First exposure at very high Chaos

The first Event 82 firing occurs with Chaos at 850 and all three evolutions enabled. The evolved opening can select Evolution III immediately.

A country at War Economy moves to Total Mobilization. A country already at Total Mobilization moves to Totalen Krieg!!!. Those are different outcomes of the same one-step rule.

A country at All Adults Serve moves to Scraping the Barrel. It does not enter Totalen Menschen!!! until a later firing or a valid voluntary purchase from that predecessor.

### Independent endpoints

A country begins at Total Mobilization and Service by Requirement. An Evolution III firing gives Totalen Krieg!!! and All Adults Serve. It has the extreme economy without the extreme recruitment law.

Another country begins at Partial Mobilization and Scraping the Barrel. The same firing gives War Economy and Totalen Menschen!!!. It receives catastrophic recruitment penalties without the extreme economy's industrial bonuses.

### War Support overflow

A country at 80% War Support receives an Evolution II firing. Its resulting War Support is 100%, with 20 points of the nominal 50-point grant unused. The unused amount produces no other effect.

## Persistence and ownership changes

The current law belongs to the country that holds it. Conquering one state does not transfer that state's former owner's national economy law to the conqueror.

Country release, civil war, and government-in-exile behavior use the relevant country-creation rules. Where a successor inherits an extreme law, it must also receive that law's current penalties and reversal access. Inheritance does not count as a new Event 82 firing or grant fresh War Support.

An annexed country does not keep producing law penalties in another country's scope. If a dormant country later returns, the country-creation owner determines its laws and the next Event 82 firing reads the resulting real state.

A save and reload must preserve the held laws, active evolution, current penalty composition, and already-applied firing. It must not deliver the War Support again.
