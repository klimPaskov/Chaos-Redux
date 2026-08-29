# Asteroid Incoming: Tuning Matrix

## Purpose

This file gives balance anchors for implementation and probability review. Values are design targets. The implementation should centralize them and verify the exact supported modifiers and rounding behavior before final tuning.

The user-defined population losses and armour bonuses are fixed. Other values can move within the listed ranges when evidence shows that the accepted campaign behavior is not reached.

## Main impact damage

| Profile | Civilian population loss | Industry and production buildings | Infrastructure, rail, and supply | Exposed military and strategic buildings | Local modifier duration |
| --- | ---: | ---: | ---: | ---: | --- |
| Main crater | 100% | 100% | 100% | 100% | Permanent |
| Ring 1 | 50% | 60% to 80% | 70% to 90% | 65% to 85% | 540 to 900 days before full local recovery |
| Ring 2 | 25% | 35% to 55% | 45% to 65% | 40% to 60% | 270 to 540 days |
| Ring 3 | 5% | 10% to 20% | 15% to 30% | 15% to 30% | 90 to 270 days |

Building percentages describe the share of existing levels damaged or removed by the impact profile. Critical one-level buildings need severity-aware handling so Ring 1 and Ring 2 can still disable them.

## Fragment damage

| Profile | Civilian population loss | Industry and production buildings | Infrastructure, rail, and supply | Exposed military and strategic buildings | Local modifier duration |
| --- | ---: | ---: | ---: | ---: | --- |
| Fragment center | 50% | About 50% | 55% to 70% | 50% to 70% | Persistent crater plus 360 to 720 day recovery burden |
| Fragment Ring 1 | 25% | 25% to 40% | 35% to 50% | 30% to 50% | 180 to 360 days |
| Fragment Ring 2 | 5% | 5% to 15% | 10% to 20% | 10% to 20% | 60 to 180 days |

## Continuing rescue deaths

Continuing deaths are a small follow-up pressure. They never replace the immediate percentages.

| Profile | Suggested monthly loss from current surviving population | Maximum normal duration | Preparation and response effect |
| --- | ---: | ---: | --- |
| Main Ring 1 | 0.03% to 0.05% | 6 months | Hospitals and shelter stance can reduce by up to half and shorten duration |
| Main Ring 2 | 0.01% to 0.03% | 4 months | Medical response and debris clearing shorten duration |
| Fragment center | 0.02% to 0.04% | 6 months | Same medical and debris actions apply |
| Fragment Ring 1 | 0.01% to 0.02% | 3 months | Local response can end it early |
| Other profiles | None by default | None | Add only if evidence shows a missing recovery consequence |

Every transaction uses a protected population floor and actual Deaths registration.

## Fragment count

| Chaos | Planned centers | Minimum for evolution to count as applied | Geographic cap behavior |
| --- | ---: | ---: | --- |
| 600 to 699 | 3 | 2 | Reduce cleanly when fewer separated sites exist |
| 700 to 799 | 4 | 2 | Reduce cleanly |
| 800 to 899 | 5 | 2 | Reduce cleanly |
| 900 to 999 | 6 | 2 | Reduce cleanly |

A center cannot appear in the main footprint or another center's first ring. Outer overlaps use the strongest profile once.

## Atmospheric Dust Load calculation

The design uses a hidden raw incident score converted to a visible 0 to 100 load.

| Contributor | Suggested contribution | Cap |
| --- | ---: | ---: |
| Main crater base | 25 points | 25 |
| Actual civilian deaths | 1 point per 500,000 deaths | 25 |
| Destroyed civilian, military, and dockyard levels | 1 point per 4 levels | 20 |
| Destroyed infrastructure, rail, supply, port, air, radar, and other strategic levels | 1 point per 6 levels | 15 |
| Main affected-state footprint | Weighted 0.5 to 2 points per state by ring | 10 |
| Fragment centers and footprints | 3 points per center plus actual destruction contributions | 20 |
| Linked major fires or debris disasters | 1 to 3 points per accepted secondary disaster | 10 |

The final visible load is clamped to 1 through 100 for an impact. A miss remains zero.

The formula should avoid double counting the same building or death through several categories. Fragment destruction contributes through actual losses and its center term.

## Dust stages and global effects

| Stage | Load | Factory output | Construction speed | Production efficiency growth | Supply consumption | Air mission efficiency | Opening Air Cleanliness injection | Monthly dust reservoir |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Residual Haze | 1 to 24 | -3% | -2% | 0% | +2% | 0% to -2% | +50 bp | +1 bp |
| Global Dust Veil | 25 to 49 | -7% | -5% | -3% | +5% | -3% | +100 bp | +2 bp |
| Impact Winter | 50 to 74 | -12% | -10% | -8% | +10% | -5% | +200 bp | +4 bp |
| Severe Impact Winter | 75 to 100 | -20% | -15% | -12% | +15% | -10% | +350 bp | +6 bp |

Weather-quality effects should use supported project modifiers or linked disaster behavior. Do not invent an unsupported dynamic weather control to match the table literally.

## Dust duration

- Opening stage hold: 30 days
- Base monthly Dust Load decay at 75 to 100: 6 points
- Base monthly decay at 50 to 74: 5 points
- Base monthly decay at 25 to 49: 4 points
- Base monthly decay at 1 to 24: 3 points
- Maximum extra global mitigation decay: 3 points per month
- Secondary-disaster increase: capped at 3 points per accepted event and 10 total after the opening transaction

A load of 75 to 100 should normally take about 16 to 24 months to clear without further disasters. A load below 25 should clear within several months.

## National dust protection

| Protection state | Suggested reduction to the country's dust-stage economic and supply penalties | Global decay contribution |
| --- | ---: | ---: |
| Unprepared | 0% | 0 |
| Basic protection | 15% | 0 |
| Organized protection | 30% | Small if observation contribution completed |
| Hardened systems | 45% | Small and capped |

Protection never reduces the initial Air Cleanliness injection or local impact damage.

## Target suitability weighting

The target-state score should roughly reflect the following priorities.

| Factor | Share of positive score |
| --- | ---: |
| Unique land states within three rings | 35% |
| Civilian population | 25% |
| Industry and logistics | 25% |
| Victory points and national significance | 15% |

Isolation penalties can remove up to 40 percent of the score. An island or empty appendage should win only when the country has no better valid state.

## Target-option diversity

- At least two continents when enough valid pairs exist
- No country appears twice
- No state appears twice
- Avoid three countries from one strategic region when broader pairs are within 75 percent of the selected suitability score
- Do not lower state validity to satisfy diversity

## Preparedness effects

| Stance | Primary effect | Secondary effect | Fixed limit |
| --- | --- | --- | --- |
| Preserve command continuity | Reduce government-dislocation duration by 35% to 50% | Improve backup-capital transition | No population reduction |
| Disperse transport and stockpiles | Preserve a bounded share of mobile trains, trucks, fuel, aircraft, or equipment that would otherwise be disrupted | Reduce first rail-corridor cost by 20% to 30% | No building survival in center |
| Prepare hospitals and shelters | Reduce continuing rescue deaths by 35% to 50% | Lower opening local recovery burden | No reduction to immediate ring percentages |

## Mineral stacking

| Controlled sites | Total armour factor from Event 028 |
| --- | ---: |
| One fragment | +20% |
| Three fragments | +60% |
| Main crater | +100% |
| Main plus three fragments | +160% |
| Main plus five fragments | +200% |
| Main plus six fragments | +220% |

The modifier applies to existing land-division armour. The accepted design has no cap.

## Decision cost bands

Exact amounts should scale with country capacity and incident burden. The following ratios guide the design.

- Emergency medical action should consume about 5% to 15% of a medium country's available support equipment and trucks, with minimum and maximum bounds.
- Emergency rail work should consume a meaningful train and fuel reserve without taking the final national supply reserve.
- Reconstruction should commit civilian factories for months instead of paying one small political-power cost.
- Global dust hardening should cost more at higher dust stages and for larger industrial bases.
- Crater security should require actual supplied divisions and equipment around the site.

Every AI action needs reserve floors so it does not spend the last critical stockpile.

## Tuning change control

The implementation can tune values inside these ranges after probability, modifier, and scenario review. The following values require explicit user approval to change.

- Main population loss of 100 percent
- Main Ring 1 population loss of about 50 percent
- Main Ring 2 population loss of about 25 percent
- Main Ring 3 population loss of about 5 percent
- Fragment center population and building loss of about 50 percent
- Fragment Ring 1 population loss of about 25 percent
- Fragment Ring 2 population loss of about 5 percent
- Main crater armour bonus of plus 100 percent
- Fragment-site armour bonus of plus 20 percent
- Uncapped fragment-site stacking
