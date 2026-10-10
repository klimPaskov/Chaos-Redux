# Agency Upgrade: evolutions and exhausted development

## Evolution entry

All three evolutions are pre-fire evolved openings. Read the shared Chaos Meter once when the firing is committed and choose the highest evolution whose threshold is met and whose evolution setting is enabled. The selection happens before Event 83 adds its own Chaos. Every recipient of that firing receives the same package size.

The evolutions do not require the country to have experienced a lower package. An agency founded for the first time at 600+ Chaos can immediately receive Intelligence States. Disabled evolution settings remove their own package from consideration rather than secretly disabling higher independently enabled packages. If Evolution III is disabled while Evolution II is enabled and Chaos is 650, use Evolution II.

Crossing 200, 400, or 600 Chaos between firings does not produce another award. Existing temporary rewards continue on their original clocks. The next real firing can use the newly eligible package. There is no intermediate stage that turns a report left open at lower Chaos into a stronger award.

## Evolution I: Expanded Agencies

Each country receives two random valid upgrade increments, two permanent operative slots, and two immediately recruitable operatives.

The second upgrade roll uses the tree after the first award. For an established agency, this may open an additional specialty. For a new agency, two departments or successive valid increments can create the beginning of a useful institutional identity. The player still chooses what to build with normal agency investment afterward.

## Evolution II: Intelligence Boom

Each country receives three random valid upgrade increments, three permanent operative slots, and three immediately recruitable operatives. It also receives one temporary specialty, independently selected for that country.

The following values and selection rules are planning additions that complete the user's unspecified random-bonus details.

| Temporary specialty | Benefit | Duration | Probability when all five are usable |
| --- | --- | ---: | ---: |
| Intelligence Network Gain | +25% | 180 days | 20% |
| Operation Preparation Speed | +25% | 180 days | 20% |
| Counter-Intelligence | +15% | 180 days | 20% |
| Decryption Speed | +15% | 180 days | 20% |
| Encryption | +15% | 180 days | 20% |

The specialty represents a concentrated effort inside the agency. It should be visible in the receipt and consolidated agency-development modifier. It should not require the player to discover a hidden modifier before choosing assignments.

Select among specialties that are actually available to the country after its upgrade grants. In particular, do not select a cryptology specialty that the country cannot use because its relevant department is unavailable. Resource shortages that the player can address through ordinary play do not themselves invalidate operation preparation. If a specialty is excluded, divide the probability equally among the remaining eligible specialties.

If no temporary specialty is usable, grant one additional permanent operative slot instead. This exceptional conversion is disclosed in the receipt. A technical failure to apply a supported modifier is a bug, not an eligibility condition and not permission to use this conversion.

## Evolution III: Intelligence States

Every country receives five random valid upgrade increments, five permanent operative slots, and five immediately recruitable operatives.

It also receives the following fixed suite. These amounts and the duration are preserved exactly from the user's brief.

| Benefit | Amount | Duration |
| --- | ---: | ---: |
| Intelligence Network Gain | +50% | 180 days |
| Operation Preparation Speed | +50% | 180 days |
| Counter-Intelligence | +25% | 180 days |
| Decryption Speed | +25% | 180 days |
| Encryption | +25% | 180 days |

All five benefits apply together. A percentage multiplier can be present before the country has developed a native base to multiply. Such a benefit becomes useful if the player establishes the relevant capability while the 180-day window remains active. Its clock still runs from the firing date. The event does not secretly grant a sixth agency upgrade to force the cryptology department into every roll result.

Intelligence States describes the reach of intelligence institutions. It does not change ideology, turn democracies into dictatorships, grant political power, create a police-state law, or make the country automatically discover every foreign operative.

## Converting exhausted upgrade rolls

The no-wasted-upgrade rule applies at every package level.
Each upgrade roll first selects from the complete current valid unowned pool; only a genuinely empty pool produces a conversion.
An unresolved upgrade identifier, stale registry or failed grant is a bug, not exhaustion.

Each exhausted roll converts to one additional permanent operative slot.
The slot is capacity only and does not add an immediate recruit.
A country with two eligible increments left during Intelligence States receives those two increments and three extra slots, on top of the guaranteed five slots, five recruits and the fixed suite.
If capacity cannot actually be delivered, the event has a compatibility failure and must not pretend the roll converted.

A mature service therefore keeps growing in the one resource that always matters, the number of people it can field.
Temporary conversion families with their own probabilities and 90-day clocks were removed in the 10 Oct 2026 spec audit: they added five more timers and a probability table for an edge case without creating a different decision.

## Temporary benefit lifetime

Each temporary grant (the Evolution II specialty and the Evolution III suite) lasts 180 days from its own firing and is removed exactly at its own expiry.
Grants from different firings add together and expire independently: a repeat on day 60 does not refresh the first suite, which still ends on day 180, while the second ends on day 240.
Permanent slots and recruits are unaffected by any expiry.

Bonuses from other events remain under their own owners.
Expiring Agency Upgrade must not remove an Intel Leaked modifier, a national focus reward, an advisor bonus or a country-specific agency trait.
Native caps still apply where the game enforces them; Event 83 adds no hidden cap of its own.

## Meaning of the percentages

Operation Preparation Speed changes the rate of preparing an operation. It does not mean agency-upgrade construction speed, cheaper operation equipment, faster network growth, or shorter execution phases. For an otherwise unchanged preparation requirement, +50% speed means completing that requirement in two-thirds of the original time. Other applicable native speed modifiers continue to interact according to the native system.

Decryption Speed refers to agency cryptology work. Encryption refers to the strength of the country's agency-era cipher protection. Counter-Intelligence refers to the country's native counter-intelligence capability, expressed as a percentage contribution relative to the appropriate native base.

A flat +0.25 counter-intelligence rating is not a +25% reward. A legacy encryption modifier that does nothing while the agency system is enabled is not an implementation of the encryption reward. These distinctions are acceptance conditions. The technical adapter findings and unresolved keys are kept in the companion plans folder.

## Chaos impact

The following direct Chaos rule is a planning addition. The event's catalog Chaos level remains 1 and is separate from this rule.

| Material occurrence | Event 83 Chaos change | Guard and reason |
| --- | ---: | --- |
| A worldwide agency-expansion firing successfully commits its awards | +5 globally | Once per firing, for the abnormal simultaneous proliferation of intelligence capacity |
| Country-level award, recruit claim, overflow conversion, or receipt acknowledgment | 0 | These are components of the same incident |
| Evolution eligibility, package selection, or evolution-history entry | 0 | Administrative progress does not create another material consequence |
| Expiration of temporary bonuses | 0 | Most of the institutional expansion remains permanent |
| War, annexation, deaths, or political changes caused later by ordinary campaign activity | 0 additional from Event 83 | The existing shared Chaos sources own those consequences |

A repeated legitimate event is a new material expansion and can add another +5. Replaying a recipient, redisplaying a report, reloading a save, or reusing the same firing identifier cannot do so. This is deliberate repeatable arms-race pressure rather than an uncapped per-operative farming source.
