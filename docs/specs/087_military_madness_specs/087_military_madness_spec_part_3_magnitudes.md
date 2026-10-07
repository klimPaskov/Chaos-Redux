# Military Madness: Magnitudes

## Magnitude philosophy

A successful roll should matter immediately to the relevant military calculation. The ordinary positive range is measured in hundreds of percent. Sensitive statistics use a different scale because a small change in their displayed number can have an enormous effect.

The ranges below are selected design targets. They have not been certified against the user's installed HOI4 executable, documentation, and full modifier composition. Production admission requires that verification for every actual engine binding.

A percentage bonus, an added percentage point, a flat value, and a reduction in a penalty are different units. The catalog must retain the distinction. A modifier increasing a percentage-based chance by twenty percentage points cannot be implemented as a twenty-percent relative increase by accident.

All magnitude draws use discrete steps. The displayed values are normally multiples of five. Percentages use steps of 5 or 25 percentage points as listed. These are magnitude increments, not a statement that every modifier is an additive probability.

## Broad pool targets

| Statistic | Random benefit per roll | Step | Interpretation |
|---|---:|---:|---|
| Land soft attack | +200% to +500% | 25% | One attack axis across its supported national scope |
| Land hard attack | +200% to +500% | 25% | Separate from soft attack |
| Division defense | +200% to +600% | 25% | Defensive combat statistic |
| Division breakthrough | +200% to +600% | 25% | Offensive protection statistic |
| Land armor | +100% to +400% | 25% | Armor statistic, not additional equipment |
| Land piercing | +100% to +400% | 25% | Piercing statistic |
| Division speed | +100% to +250% | 25% | Movement statistic with a certified finite range |
| Maximum organization | +100% to +250% | 25% | Capacity, without an invented immediate refill |
| Organization recovery | +100% to +400% | 25% | Recovery rate |
| Maximum entrenchment | +100% to +400% | 25% | Relative capacity where supported |
| Entrenchment speed | +200% to +600% | 25% | Accumulation speed |
| Maximum planning bonus | +100% to +300% | 25% | Relative planning capacity |
| Planning accumulation | +200% to +600% | 25% | Accumulation speed |
| Reinforcement chance | +15 to +40 percentage points | 5 points | Requires the exact native chance unit |
| Army supply consumption | 40% to 80% lower | 5% | Reduction with certified composition safety |
| Army fuel consumption | 40% to 80% lower | 5% | Separate from supply |
| Air fuel consumption | 40% to 80% lower | 5% | Country-scoped air consumption |
| Naval fuel consumption | 40% to 80% lower | 5% | Country-scoped naval consumption |
| Training duration | 40% to 80% shorter | 5% | Time reduction with a positive valid floor |
| Army experience gain | +200% to +600% | 25% | Gain rate, not an immediate experience grant |
| Navy experience gain | +200% to +600% | 25% | Gain rate |
| Air experience gain | +200% to +600% | 25% | Gain rate |
| Broad air attack | +150% to +400% | 25% | One supported attack statistic |
| Broad air defense | +150% to +400% | 25% | One supported protection statistic |
| Broad air agility | +100% to +300% | 25% | Only with a real national application |
| Broad naval gun attack | +150% to +400% | 25% | Distinct native gun types become distinct entries |
| Broad naval torpedo attack | +150% to +400% | 25% | One supported torpedo statistic |
| Broad naval protection | +100% to +300% | 25% | Actual protection statistic, never invented ship health |
| Naval speed | +50% to +150% | 25% | Broad fleet mobility |

The table defines semantic statistics, not a claim that every row corresponds to one native modifier token. A narrow engine key cannot masquerade as a broad effect. A national adapter must deliver the stated scope or the binding remains unresolved.

## Evolution I targets

| Specialist family | Random benefit per roll | Step | Admission requirement |
|---|---:|---:|---|
| Special-forces capacity | +100% to +300% | 25% | Preserve whether the native value is relative or flat |
| Special-forces attack | +100% to +300% | 25% | One statistic affecting supported special forces |
| Special-forces defense | +100% to +300% | 25% | Separate from attack |
| Amphibious combat bonus | +100% to +300% | 25% | Bonus route with verified semantics |
| Amphibious penalty reduction | 40% to 80% lower penalty | 5% | Separate alternative when the engine exposes a penalty |
| River-crossing combat bonus | +100% to +300% | 25% | Retains crossing condition |
| River-crossing penalty reduction | 40% to 80% lower penalty | 5% | Cannot reverse the penalty beyond its valid domain |
| Naval invasion preparation | 40% to 80% shorter | 5% | Preparation time, not instant launch |
| Naval invasion capacity | +50 to +150 divisions | 5 divisions | Only if the discovered effect really uses a flat capacity |
| Paradrop combat performance | +100% to +300% | 25% | Split distinct supported combat axes into entries |
| Paradrop preparation or disruption recovery | 40% to 80% shorter | 5% | Exact supported temporary timing statistic required |
| Equipment capture chance | +20 to +60 percentage points | 5 points | Chance type and ceiling must be certified |
| Reconnaissance | +100% to +300% | 25% | Base reconnaissance, without granting free intelligence |
| Planning retention | 40% to 80% less decay | 5% | Reduce a real decay statistic |
| Specialized reinforcement effect | +100% to +300%, or +15 to +40 points | 25% or 5 points | Select the profile from the actual value type |
| Air mission efficiency | +50% to +150% | 25% | One distinct mission or supported broad mission statistic |
| Air interception or escort performance | +100% to +300% | 25% | One task-specific statistic |
| Naval detection or spotting | +100% to +300% | 25% | Distinct detection types remain separate |
| Naval retreat or disengagement | +100% to +300%, or 40% to 80% shorter | Typed profile | Beneficial sign depends on the actual statistic |
| Military training or exercise losses | 40% to 80% lower | 5% | Loss reduction with a valid floor |

A descriptive family can discover several entries. Each entry still has one fixed value type and one fixed range before sampling. The game never randomly chooses between percentage and flat units for the same entry.

## Evolution II targets

| Situational family | Random benefit per roll | Step | Scope of the effect |
|---|---:|---:|---|
| Terrain attack | +100% to +300% | 25% | A separate entry for each supported terrain condition |
| Terrain defense | +100% to +300% | 25% | Separate from terrain attack |
| Terrain movement | +50% to +150% | 25% | A supported terrain-specific movement statistic |
| Terrain penalty reduction | 40% to 80% lower | 5% | A distinct penalty, not an invented general buff |
| Weather combat bonus | +100% to +300% | 25% | A specific supported weather condition |
| Weather penalty reduction | 40% to 80% lower | 5% | Preserve the effect's actual condition and domain |
| Heat or cold acclimatization | +100% to +300% | 25% | Gain rate or a separately typed supported statistic |
| Night combat bonus | +100% to +300% | 25% | One applicable military domain |
| Night penalty reduction | 40% to 80% lower | 5% | A distinct alternative when available |
| Offensive or defensive condition bonus | +100% to +300% | 25% | Exact qualifying combat condition |
| Fort assault performance | +100% to +300% | 25% | Specific supported fort-related statistic |
| Fort penalty reduction | 40% to 80% lower | 5% | No instant fort removal |
| Encirclement-related penalty reduction | 40% to 80% lower | 5% | Exact native encirclement condition required |
| Naval positioning | +50% to +150% | 25% | Verify native limits |
| Screening performance | +50% to +150% | 25% | Verify native limits and value type |
| Submarine attack or protection | +100% to +300% | 25% | Distinct axes and conditions become distinct entries |
| Submarine visibility | 40% to 80% lower | 5% | Benefit direction must be verified |
| Carrier sortie or air performance | +100% to +300% | 25% | Each distinct statistic is its own entry |
| Convoy attack | +100% to +300% | 25% | One applicable combat statistic |
| Convoy protection | +100% to +300% | 25% | One applicable defensive statistic |
| Specific air mission damage | +100% to +300% | 25% | One mission type |
| Intelligence-derived combat advantage | +50% to +150% | 25% | Requires a real combat consumer |

The terrain family includes every compatible mountain, hill, forest, jungle, desert, marsh, urban, plain, and other installed terrain entry. Snow and extreme temperatures follow the actual weather or climate definitions. Labels do not create new terrain.

## Evolution III and newly discovered statistics

Every new statistic receives the profile that matches its actual calculation. Unit-specific attack, defense, endurance, or mission power ordinarily uses +100% to +300% in 25% steps. A direct broad statistical equivalent retains its broad-pool magnitude profile.

A flat capacity normally uses a range with at least five meaningful steps in multiples of five. Its exact minimum and maximum must be chosen after the installed system's scale is known. An unknown custom capacity cannot inherit +100% by default.

A bounded chance normally uses +15 to +40 percentage points in 5-point steps when those points remain meaningful and safe. A cost, loss, visibility, time, or penalty reduction normally uses 40% to 80% lower in 5% steps.

A Chaos Redux statistic without an interpretable unit, clear beneficial direction, real military consumer, and certified reversible range remains unverified. The system owner must supply that meaning rather than receiving an arbitrary gigantic number.

## Safety without national balancing

A single roll uses a certified range. Repeated rolls retain their original values and stack in the package record. The combined applied result also respects the statistic's genuine technical domain.

For an additive percentage statistic with no reached technical bound, +200% and +300% contribute +500%. They are not multiplied together. Any base value and unrelated modifiers remain governed by the actual game calculation.

For a reduction, two individually valid rolls may exceed a safe total. The event therefore distinguishes the requested combined contribution from the amount the engine can safely apply. Excess contributions are retained until their own expiry. They can continue holding the result at a technical bound after another package expires.

A safety bound is never chosen to make the event fair. Positive advantages must not be clipped at a convenient balance target. Every production bound requires an identified engine limitation, a documented valid domain, or measured overflow protection.

A proposed 5% remaining-consumption floor can be used as an initial verification target for a reduction adapter. It is not a claim that every HOI4 cost uses that floor. The final floor is selected per actual statistic and must account for supported effects outside Event 087.

## Communicating the result

The player sees the rolled magnitude with its correct unit and sign. When a genuine technical limit constrains the combined effect, the result view distinguishes the rolled total from the currently applied amount and explains why they differ.

That display does not offer a reroll. A saturated or presently irrelevant result is still a valid result with its original expiry.
