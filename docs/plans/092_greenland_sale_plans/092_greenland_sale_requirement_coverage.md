# Greenland Sale: requirement coverage

This is a design-coverage map, not an engine test result.
Part numbers refer to the 13 files in `docs/specs/092_greenland_sale_specs/`.
The original wording remains in [the preserved brief](092_greenland_sale_user_brief_original.md).

| ID | User requirement | Covered by | Disposition |
| --- | --- | --- | --- |
| U01 | Retain ID 092, name, Minor Fire-Once, level 1 and no cluster | 01 | Explicit and unchanged. |
| U02 | Keep current catalog status rather than claim implementation | Index and source register | To Be Reworked retained. |
| U03 | Sell Greenland as the only founding lot | 01, 04, 10 | No secondary publication until founding terminal outcome. |
| U04 | Use the actual current owner, never assume Denmark | 01, 04 | Current legal ownership and full control determine seller. |
| U05 | Give every valid country access | 01, 04, 05 | No major-only or historical-tag preference. Seller cannot buy its own lot. |
| U06 | Highest bid remains unbeaten for about ten days | 01 | Resolved to 240 hours from accepted funded bid. |
| U07 | Every accepted higher bidder resets the countdown | 01 | Full reset, no self-raise or stale-price auto-spend. |
| U08 | No predetermined winner | 01, 05 | Affordability and private interest determine competition. |
| U09 | Dynamic current bid and next bid | 01, 03 | Published opening reserve and upward-rounded 5-percent raises. |
| U10 | Price reflects industry and resources | 03 | Usable current economic assessment, damage and resource access. |
| U11 | Price reflects infrastructure, ports and airfields | 03, 08 | Actual facilities and useful connected access, not cosmetic labels. |
| U12 | Interest reflects position, bases and sea access | 03, 05, 08 | Buyer-specific usable foothold and network value. |
| U13 | Interest reflects claims and regional priorities | 03, 05, 11 | Claims affect willingness, not ownership or price exemptions. |
| U14 | Wars and rivalries matter | 04, 05, 08 | No hostile seller-buyer contract. Third-party war alters risk and funding. |
| U15 | Buyers can keep raising while willing and able | 01, 05 | Full prefunding for each lead. No arbitrary final-auction duration cap. |
| U16 | AI stops at an unaffordable or poor-value next bid | 02, 05 | Hard paid-funds limit and lower private ceiling. |
| U17 | Player decides whether to enter and continue | 01, 12 | Explicit next-bid confirmation and visible commitment. |
| U18 | No fixed Greenland price | 03 | Current assessment determines the founding reserve. |
| U19 | Prior economic events change value | 03, 11 | Current improvements and damage feed assessment and private value. |
| U20 | Meaningful buyer cost and corresponding seller benefit | 02 | One conserved funded principal, usable domestic construction receipt. |
| U21 | Determine an appropriate HOI4 economic representation | 02 and source register | Industrial Reserve chosen. Native adapters still require proof. |
| U22 | Treat divided Greenland without forcing history | 04 | One actual owner and its eligible holdings, with honest partial-lot label. |
| U23 | No bids means Greenland remains unsold | 01 | Finite first-bid window, no imposed buyer or fallback transfer. |
| U24 | Evolution I at 200 permits distant possessions | 06, 10 | Ordinary remote non-core state auctions. |
| U25 | Overseas lots selected from current map | 04, 06 | Current geography, owner, control and usefulness. |
| U26 | Evolution II at 400 permits larger colonial regions | 07, 10 | At least two coherent connected states, no fixed upper lot size. |
| U27 | Regional size reflects live geography and ownership | 07 | No fixed colonial borders or unrelated world-state bundle. |
| U28 | Evolution III at 600 permits strategic lots | 08, 10 | Real ports, major islands, resources, chokepoints and staging access. |
| U29 | Strategic interest can outweigh economic value | 03, 05, 08 | Private positional premium separated from base economic assessment. |
| U30 | Evolution IV at 800 permits homeland territory | 09, 10 | Protected capital and survival, core political cost and use of proceeds. |
| U31 | Pressure makes normally unacceptable sales possible | 05, 09 | Credible severe-pressure AI motive with a retained-home recovery plan. |
| U32 | Cores remain harder to sell | 03, 09 | Higher floors, domestic cost and separate eligibility. |
| U33 | Never sell a country out of existence | 04, 09 | Capital, inhabited retained home and combined pending-lot checks. |
| U34 | Evolved auctions recur after the founding precedent | 06, 10 | Fire-once entry separated from continuing market activity. |
| U35 | Limit concurrent auctions | 06, 08, 10 | One founding lot, then two or three with seller and publication pacing. |
| U36 | Keep the same closing rule for every later lot | 01, 06–10 | Fully funded highest bid and 240-hour unchanged-leader clock. |
| U37 | Connect World Claims | 11 | Real current claims increase willingness without free cores. |
| U38 | Connect Independence Wave and liberation | 04, 11 | Live ownership and existing commitments remain authoritative. |
| U39 | Connect economy and resource events | 02, 03, 11 | Capacity affects funding, physical changes affect value. |
| U40 | Expand the idea at full specification depth | 01–13 | Full baseline, four evolutions, motives, consequences and production handoffs drafted. |

## Workflow requirements and genuine gaps

| ID | Requirement | Actual status |
| --- | --- | --- |
| W01 | Fully read every currently supplied text source before drafting | Complete for all 46 files, 109 full-text chunks, all 20 role definitions. |
| W02 | Use the full event-planning skill and other supplied skills | Every supplied skill read. Applicable criteria inform design and handoffs. Reading an irrelevant skill does not require adding its feature. |
| W03 | Fully read all required external must-read references | Incomplete. The reading report identifies missing and partial references, including live MTTH lines 1–150 only. |
| W04 | Follow the source-reading protocol when available | Not found in the supplied archive or searched Project/repository locations. No invented compliance. |
| W05 | Use provided subagents | Role definitions and review criteria used by the parent. Actual independent subagent execution was not available and did not occur. |
| W06 | Mandatory near-completion improvement-loop subagent | Blocked by the absent executable subagent route. Parent review is not a substitute. |
| W07 | Exact probability and MTTH inspection with the requested tool | Not performed. Probability tool route was unavailable. |
| W08 | Preserve idea-first main specification and separate implementation detail | Main 13 parts contain game design. Source, role, validation and execution records are in the plans folder. |
| W09 | Produce all requested specialist prompts | Asset, achievement, decision/mission, coding and 3,968-character goal prompts are present. |
| W10 | Honestly disclose truncation, simplification and incomplete work | Supplied full-text reading was not abbreviated. External gaps, untested tuning, missing audits and unproduced runtime artifacts are explicit. |
| W11 | Use live repository evidence rather than invented implementation claims | Five bounded files fully read at a pinned commit. Other repository information is expressly partial or snippet-only. |
| W12 | Do not claim final implementation, final art or finished localisation | None produced or claimed. Catalog remains To Be Reworked. |

## Deliberate scope exclusions

The request does not require a new ideology, country tag, focus tree, naval unit, weapon, biological operation, super-event or world-ending scenario.
Those features are not invented merely to activate more specialist skills.
The four evolutions share a market contract but change seller motives, lot shapes and strategic stakes.
Exact native interfaces, current construction constants, valuation coefficients and tuned probabilities remain explicit implementation and calibration work.
