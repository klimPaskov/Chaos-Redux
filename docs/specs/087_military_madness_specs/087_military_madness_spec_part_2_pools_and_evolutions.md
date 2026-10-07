# Military Madness: Pools and Evolutions

## Broad military advantages

The broad pool contains statistics with a general military role. It covers land firepower, protection, movement, endurance, preparation, reinforcement, logistics, training, military experience, and broad air and naval combat.

Soft attack and hard attack are separate potential results when each has a supported national application. Defense and breakthrough are separate. Armor and piercing are separate. Organization capacity and organization recovery are separate. Maximum entrenchment and entrenchment speed are separate. Maximum planning and planning accumulation are separate.

Broad air and naval combat are families of individual statistics. A roll selects one supported statistic from them. A family label must never disguise several unrelated bonuses as one modifier.

A country can draw a land, naval, or air result regardless of its current force composition. The baseline is deliberately capable of changing the balance of a war by itself.

## Evolution I: Military Insanity

At 200 Chaos, each country receives three independent rolls. One comes from the broad pool. Two come from the combined broad and expanded pools.

The expanded pool introduces specialist capabilities that can shape an operation or military institution. Special-forces capacity and performance become possibilities. Amphibious assaults, naval invasion preparation, river crossings, paradrop performance, equipment capture, and specific air or naval tasks become possible results.

A country might receive exceptional organization, unusually strong amphibious attacks, and accelerated naval invasion preparation. Another might receive three separate organization bonuses. These are examples of possible independent draws, never stored combinations.

The extra rolls allow circumstances to interact. A broad bonus can support an unexpected specialist result. It can also be unrelated to the other two. That mismatch is an intended part of the event.

## Evolution II: Impossible Warfare

At 400 Chaos, each country receives six independent rolls. Two come from the broad pool. Four come from the combined broad, expanded, and situational pools.

The situational pool includes terrain, weather, time of day, offensive and defensive conditions, fortifications, encirclement, reconnaissance, and intelligence-derived combat effects. Mountains, hills, forests, jungles, deserts, marshes, urban terrain, snow, and extreme temperatures become distinct sources of advantage when the installed systems expose those effects.

The sea and air receive equal conceptual breadth. Positioning, screening, submarine warfare, carrier operations, convoy attacks, convoy defense, and narrowly defined air missions can enter the pool.

Specialist advantages do not change the map. A mountain bonus does not create mountains. A snow advantage does not change the weather. A night advantage does not lengthen the night. Their value depends on the campaign.

Situational conditions are retained precisely. A defensive forest modifier is not silently converted into a universal attack bonus because the latter is easier to implement. An encirclement effect must identify whether it changes a penalty, combat performance, or another actual supported calculation.

## Evolution III: Gods of War

At 600 Chaos, each country receives ten independent rolls. Three come from the broad pool. Seven come from the entire compatible military pool.

This stage opens the fullest available range of temporary military statistics. Compatible unit-specific, mission-specific, system-specific, and country-origin effects are admitted alongside all earlier categories.

Country-specific origin describes where an effect comes from. It is not automatically an eligibility restriction. A statistic discovered in a national system can be offered elsewhere when it has a genuine temporary national application there. Conversely, a modifier whose consumer only exists inside one country's special system cannot be declared universal without a working adapter.

Chaos Redux providers can contribute unusual military statistics used by their existing forces and military systems. A bonus can improve an existing anomalous formation or a supported military subsystem. It cannot grant a new country, doctrine tree, weapon stockpile, program, military action, or permanent unlock merely to make its own result usable.

The event remains a random temporary enhancement system at this stage. Its larger pool does not authorize unrelated resource windfalls or event chains.

## Drawing from the pools

The guaranteed broad slots are drawn first. The remaining slots draw from a single deduplicated union of all eligible entries for the selected stage. Each eligible canonical entry has equal selection weight within the relevant draw.

Sampling is with replacement. A selected entry stays available for the next slot. Magnitude is drawn independently after selecting the entry. Every permitted magnitude step for that entry has equal weight.

Pool membership does not create an extra lottery. A broad entry appearing in both the baseline list and the combined list still occupies one place in the combined list. A provider exposing several aliases for the same effect does not receive several chances.

Two effects that genuinely differ in target or condition remain distinct. General land defense, mountain defense, and infantry defense can all exist when they have different real applications. Renaming the same general defense effect three times does not produce three valid entries.

The random order used to make draws has no strategic meaning. Presentation may sort results by statistic or expiry without changing the draws.

## Minimum broad coverage

At Evolution I, one of three slots is guaranteed broad. Both remaining slots can also be broad.

At Evolution II, two of six slots are guaranteed broad. The other four can raise the total to six.

At Evolution III, three of ten slots are guaranteed broad. The other seven can raise the total to ten.

Duplicate broad rolls still count as broad rolls. The guarantee concerns the origin of each draw, not a number of distinct statistics.

## A genuinely expanding pool

The pool is generated from the supported installed game, enabled content, country-system providers, and Chaos Redux providers. It is not confined to the examples in this package.

Discovery identifies possible effects. Admission establishes what each effect actually changes, where it works, whether it reverses correctly, what number format it uses, and which excessive values remain safe.

The build produces a versioned, deterministic catalog that the game can sample. New compatible entries become available when that catalog is regenerated. Runtime draws use the compiled catalog rather than attempting to discover arbitrary files or invent new engine modifier names during a campaign.

Every discovered candidate receives an explicit disposition. Supported entries identify their stage and magnitude profile. Unsupported candidates identify the technical reason. Unverified candidates remain visible in the coverage report and prevent a claim of complete compatibility.

The final production pool must include all compatible discoveries, even when they are obscure, difficult to localize, or unlikely to help a particular recipient. Lack of implementation effort is not a technical exclusion.

## Eligibility and useful outcomes

Missing ships do not exclude naval bonuses. Missing aircraft do not exclude air bonuses. Current peace does not exclude combat bonuses. A unit-specific result can remain valid before the country recruits that unit.

Missing engine support, an absent required system, or a country scope that cannot carry the effect is different. Such a candidate cannot be offered until it has a valid temporary national application.

Current usefulness, military strength, ideology, human control, difficulty setting, front conditions, and the quality of the country's previous rolls never change selection weights.

## Technical boundary

Every admitted reward must be a scalable temporary military statistic with a reversible application. Permanent technologies, discrete unlock commands, generated equipment grants, and changes to history are outside that contract.

Boolean capabilities with only one meaningful nonzero value require special scrutiny. They cannot be passed off as magnitude-randomized statistics by assigning meaningless large numbers. The compatibility report must record this type conflict. A genuine scalable military adapter can make a related statistic eligible, but it cannot turn one unlock into several fictitious modifiers.

A missing broad pool is a configuration failure, not permission to issue fewer rolls, use a fixed entrenchment reward, or drop the broad minimum. Distribution must not begin with an invalid pool.
