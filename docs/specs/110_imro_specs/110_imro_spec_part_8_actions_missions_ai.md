# Actions, missions, tuning and AI

## Shared rules for every action

The decision layer changes as the movement becomes a country, a network and a world coalition. Each action has a real target, an eligibility reason, a quoted cost, a duration or immediate result, a meaningful failure and a cleanup rule. Routine categories show three to five primary actions and never more than six. A country normally has one to three active missions, with unrelated native game content preserved.

The [pre-country operator matrix](110_imro_spec_part_2_underground_uprising.md) controls every use of the word movement below. Before a real IMRO government exists, it is an NPC territorial organisation. National PP, CP, factory, manpower and equipment prices are paid only by a named real sponsor or by an actual later IMRO government. The controller is never silently charged for its opponent's organisation. Autonomous NPC cell activity instead uses bounded time, actual local support, retained cadres and physically sourced stores. Existing non-IMRO MAC opposition has the same restriction and cannot spend the incumbent's resources without an explicit lawful decision.

An action uses at most four spendable or committed cost types. Every displayed resource has its correct text icon. There is no fifth price hidden in an effect. Organisation, Mandate and Front Authority are never spent as currencies. Public values are limited to those three across the entire IMRO system, including focus inlays, decisions, event details and secondary panels.

The cost displayed is the same quote used for inclusive affordability and payment. A country with exactly the quoted amount can act. Freeze the quote with actor, target, generation, purpose and resource quantities. Revalidate the target and payer immediately before payment. A changed quote invalidates the old action and displays the new quote before any spend. Each successful transaction has one payment receipt and one closure receipt.

Refund only a measured paid amount whose resource or reservation was not consumed. If a shipment was delivered, the sender does not get its equipment back because the recipient later leaves the Front. If a construction reservation was unused when a target vanished, release that reservation. If a unit was trained and deployed, cancellation cannot create a second manpower return. Dead people are never refunded.

## Numerical tuning owner

All numerical values in this part are proposed starting balance, apart from the brief's fixed 800 and strictly-above-1000 requirements. Keep them in one event constants owner with descriptive symbolic names. Do not scatter copies through focuses, decisions and GUI code. Final tuning must preserve the inequalities and qualitative relationships described here.

| Parameter | Initial design | Dynamic factors and limits |
| --- | --- | --- |
| Organisation and Mandate | 0 to 100 | Clamp after actual events, missions and policy results |
| Front Authority | 0 to 100 | Fresh weighted proof as defined in Freedom or Death, no passive nominal-leader award |
| Regional evolution | Chaos at least 200 | Viable contact plus survival or sustained exile-network conditions |
| Worldwide evolution | Chaos at least 400 | Independent survival 180 days, Mandate at least 55, outward-policy proof, nonempty subject cohort |
| Radical evolution | Chaos at least 800 | Independent IMRO state and completed worldwide uprising |
| Terminal lock | Chaos strictly above 1000 | Full independent-state, conquest, authority, geographic and absolute-power predicate |
| Peaceful controller response | 120 to 180 days | Longer for capable administration and credible negotiation, shorter only under a real military opportunity |
| Cell establishment | 120 to 180 days | Terrain, existing support, actual repression and controller security affect duration |
| Procurement mission | 120 to 180 days | Route length, blockade and sponsor delivery capability |
| Founding reconstruction | 180 to 240 days | Actual damage and productive capacity, no reward before a real project result |
| Autonomy review | 180 days | A material breach can end review early with a specific failure |
| Regional uprising coordination | 120 to 240 days | Ready participants and actual common military pressure shorten it |
| Front command mandate | 180 days normally | Renewable with current consent, contributions and route proof |
| Radical contest | 120 days, or justified 90-day emergency | Institutional collapse can shorten it, successful defence is condition-based |
| Repeat radical attempt | At least 365 days after resolution | Requires a new material institutional collapse and current Chaos at least 800 |
| Terminal Authority endurance | 90 days | Recompute after doctrine split, significant changes reset the qualifying run |
| Terminal operating cycle | 30 days | Event-owned active state registry, no global periodic scan |
| Terminal regional project | 120 to 180 days | At most three major active projects, recheck reach before every loss |
| Standard CP cost | 15 to 45 | Absolute maximum 60 for an action |
| Standard PP cost | 20 to 75 | Large constitutional or diplomatic commitments may reach 100, with meaningful alternatives |
| Routine action cooldown | 90 to 180 days by family and target | Separate receipt for distinct useful targets, no repeat farming on one completed objective |

Mission time is quoted with the same live difficulty inputs as its start conditions. War and target changes can invalidate a mission or change a future quote, but cannot silently shorten an active player's deadline without an explicit emergency event and reason. Timed modifiers last only as long as the institution or operation they represent and remain inside the three-spirit cap when they are focus-owned institutions.

## Opening strength model

Calculate a hidden opening strength index from independent evidence groups. The initial model gives up to 25 points from Chaos, 30 from population-weighted eligible local resistance, 15 from actual military pressure on the controller, 10 from a recorded recent breach or repression grievance, 15 from delivered support and 5 from retained cadres or a valid connected movement receipt. Deduct up to 20 for verified exposure and dismantled infrastructure. Clamp to 0 through 100.

The Chaos contribution is zero near the baseline and reaches its cap at Chaos 1000. Intermediate values interpolate using the shared supported arithmetic. Resistance contributes its average multiplied by 0.30. Controller military pressure has three states: 0 for no relevant war strain, 8 for a significant active war and 15 for severe local exposure supported by actual forces or supply disruption. Delivered aid has 0, 5, 10 and 15 bands for absent, light, standard and major verified support. A promise contributes zero.

Index below 25 is fragile, 25 to below 50 established, 50 to below 75 dangerous and 75 or higher exceptional. Organisation begins within the corresponding range in the underground part, using the index's position within the band. Mandate uses the separate local-consent calculation: start at 30, add up to 20 for credible independence sentiment and protected civic organisation, add up to 15 for an attributable broken compact or repression grievance, subtract up to 20 for IMRO coercion or rejected patron terms, and clamp to 25 through 70 at opening. The government's grievances do not erase the movement's own misconduct.

A connected revolt can supply actual cadres or a readiness factor, but one recorded repression incident does not contribute separately as three different bonuses. Every support group identifies its source receipt. Equipment and manpower limits remain independent hard constraints after the strength index chooses an intended force band.

## Cost and duration scaling

Use light, standard and major operation bands selected from actual target size, distance, damage, threat and available local institutions. The band is qualitative in the interface, with the actual resource quote and time displayed. It is not another persistent score.

| Band | Typical use | PP reference | CP reference when military | Infantry equipment reference when relevant | Civilian factory commitment when relevant |
| --- | --- | --- | --- | --- | --- |
| Light | One local project or a short safe regional connection | 20 to 35 | 15 to 20 | 100 to 250 | One for the mission's committed period |
| Standard | A substantial state project or ordinary foreign support | 35 to 60 | 25 to 35 | 300 to 600 | One to two |
| Major | Difficult reconstruction, distant theatre or central institutional compact | 60 to 100 | 40 to 60 | 750 to 1500 | Two to three |

These columns are alternatives selected for the action. A row does not automatically charge every column. A typical shipment charges PP plus its exact equipment. A training mission charges CP, manpower commitment and equipment. A construction project commits factories and material through the existing construction owner, with PP only where it represents a real political action. Four resource types is the hard per-action limit.

A light country must retain a playable path even with no factories or low PP. Civic negotiation and time-intensive local organisation provide lower-resource alternatives with smaller, slower results. These alternatives do not grant the same outcome at no cost. AI affordability uses a reserve floor after payment, except for explicitly declared survival emergencies.

## Movement and controller action map

| ID and working label | Actor, target and reveal | Cost and time | Success | Failure, cancellation and AI |
| --- | --- | --- | --- | --- |
| U01 Local cell | Movement, eligible neighbouring origin state, surviving network | 25 to 50 PP, 120 to 180 days | Established contact, Organisation increase 5 to 10, new local action reach | Discovery removes only exposed local capacity. AI avoids targets it cannot sustain |
| U02 Arms procurement | Movement or sponsor, actual route and recipient | 20 to 40 PP plus 100 to 600 real infantry equipment from payer, 120 to 180 days | Delivered stores and Organisation increase 3 to 8 | Intercepted stores are lost or captured once, undelivered unspent reservations refunded |
| U03 Civic protection | Movement, attributable local grievance | 20 to 45 PP, 120 to 180 days, optional single project commitment | Mandate increase 5 to 12 and viable public institution | Later breach reverses the political benefit through a new receipt, no repeat reward for same resolved grievance |
| U04 Compartmentalise cells | Movement, exposed local network | 15 to 30 PP, 90 to 120 days and temporary Organisation reduction 5 | Stops spread of a verified compromise | Cannot erase already captured matériel or people. AI uses when further exposure threatens survival |
| U05 Rise | Movement, frozen viable homeland and current controller | Existing stores and mobilisation pool, explicit immediate commitment after preparation | Real country and army transaction | Preflight failure makes no country mutation or spend. AI needs viable supply and purpose |
| U06 Negotiate compact | Movement and controller, exact owner if different | 25 to 60 PP for each substantive actor, 120 to 180-day negotiation | Autonomy or recognised settlement with enforceable terms | Refusal preserves the live movement. No treaty on timeout |
| C01 Investigate cells | Controller, affected state and intelligence commitment | 25 to 50 PP and 15 to 30 CP, 120 to 180 days | Bounded Organisation loss 5 to 15 and one exposure result | Bad intelligence can fail without fabricated civilian casualties. AI needs capacity |
| C02 Protect transport and administration | Controller, actual local supply network | 15 to 35 CP and 100 to 300 support or infantry equipment, 120 to 180 days | Better containment and civilian protection | Forces and stores remain real, mission ends if target control is lost |
| C03 Offer autonomy | Controller and legal owner, movement contact exists | 35 to 75 PP, negotiation then 180-day review | A peaceful resolved compact if both sides honour it | Material breach reopens the same event lineage and changes Mandate and resistance |
| C04 Collective repression | Controller, explicit escalation choice | 25 to 45 CP and security commitment, 90 to 120-day crisis | Can damage exposed organisation while causing severe political backlash | Any civilian losses are measured through the shared owner. AI avoids without a compatible coercive trajectory |
| C05 Recognise independence | Actual sovereign parties to local war | Diplomatic agreement with specific border and war terms | Independent viable Macedonia after observed peace | A sent command is not settlement. Unrelated wars remain intact |

## Country, territorial and network action map

| ID and working label | Actor and prerequisite | Cost and duration | Outcome and tradeoff | Closure and AI |
| --- | --- | --- | --- | --- |
| N01 Repair homeland | Independent Macedonia, damaged controlled location | One to two factories, 120 to 240 days and appropriate material | Actual repair, Organisation and productive-institution improvement | Cancel location-dependent work on loss of control, retain completed repairs |
| N02 Constituent outreach | Government, unsettled representation | 35 to 60 PP, 120 to 180 days | Mandate increase 8 to 15 and a constitutional prerequisite | One reward per represented unresolved issue, AI targets genuine gaps |
| N03 Train cadres | Macedonia, actual experienced force and stores | 20 to 35 CP, a finite cadre manpower commitment, 120 to 180 days | Better training and reorganised template capability | No new force until manpower and equipment are paid |
| N04 Reinforce or raise | Macedonia, valid trained template and supply | Exact manpower plus infantry and optional support equipment, 120 to 180 days | Real reinforcement or one bounded new formation | AI prefers reinforcement when combat strength is low |
| N05 Supply depot | Government or consenting compact, chosen state | One to three factories and appropriate material, 180 to 240 days | Real supply asset and operational capacity | Completed physical assets remain if government changes |
| N06 Territorial dialogue | Macedonia and actual owner, a verified claim area | 35 to 75 PP, 180 days | Negotiated rights, access, border settlement or refusal | No automatic transfer on focus completion |
| N07 Civic integration | Settled state and protected residents, Mandate at least 60 | 50 to 100 PP and one to two factories, 180 to 365 days | Qualified core or integrated territorial status | Recent coercive breach blocks completion, shared puzzle and button agree |
| N08 Delegate defence mandate | Anarchist government and real assemblies | 25 to 50 PP and 15 to 30 CP, 120 to 180 days | Bounded common military command | Expiry requires renewal. Permanent coercion triggers constitutional consequences |
| N09 Federal production compact | Independent willing partner and complementary capacity | 35 to 75 PP, one to two factories, 180 to 240 days | Delivered shared industrial programme | No duplicate factory creation in sender and recipient |
| B01 Regional contact | Movement or government, verified partner | 20 to 40 PP, 120 days | Relationship and negotiation access | Invalid identity closes without invented country creation |
| B02 Support regional movement | Actual willing recipient, viable route | 25 to 50 PP, 250 to 750 infantry equipment, 120 to 180 days | Local readiness and retained capability | Existing uprising and release receipts prevent duplicate armies or declarations |
| B03 Coordinate rising | At least two ready partners | 35 to 60 PP and 25 to 45 CP, 120 to 240 days | Synchronous local commitment where each actor remains eligible | A newly free partner becomes a supporter, not a second subject release |
| B04 Mediate borders | Two willing conflicting partners | 35 to 75 PP, 180 days | Specific treaty, autonomy or unresolved dispute | AI accepts compromise when expected survival improves |
| B05 Form regional compact | At least three independent consenting states | 60 to 100 PP, 180 to 240 days | Sovereign association or explicitly chosen federal institutions | Every affected human country consents to any later absorption |
| B06 Challenge a patron | Actual coercive demand or breached contract | 25 to 75 PP, 90 to 180 days | Renegotiation, collective refusal or dependency choice | Delivered aid stays delivered, future aid and treaties change honestly |

## Worldwide and endgame action map

| ID and working label | Actor and prerequisite | Cost and duration | Outcome | Closure and AI |
| --- | --- | --- | --- | --- |
| F01 Worldwide declaration | IMRO government with complete evolution eligibility | Political focus commitment and one validated originating transaction | Every snapshot subject free, hostile to direct master and in the Front | No partial cohort treated as success, no per-country AI veto |
| F02 Master acceptance | Actual former master and exact snapshot children | No PP purchase to recognise the already actual independence | Recognition and verified exit from owned restoration conflicts | Repeat safe, unrelated wars preserved, failed adapter never reports peace |
| F03 Restoration policy | Former master after declaration | Real war effort and appropriate objectives | Continued war with possible later settlements | AI compares reach and capacity, no fabricated troops |
| F04 Aid a member | Willing sender and recipient with a viable route | 20 to 50 PP plus exact equipment, 120 to 180 days | Delivered aid and a bounded fulfilled-obligation receipt | Small repeated shipments cannot farm Authority |
| F05 Delegate theatre command | Member, IMRO proposal and viable theatre | 35 to 75 PP, defined real contribution, 180-day renewable mandate | Command coefficient and operational capability | Revocation, expiry or logistics loss removes the contribution |
| F06 Propose the charter | Front members and a current coordination body | 50 to 100 PP, 180 days | A voted sovereignty and aid framework | No automatic human agreement, no forced ideology change |
| F07 Regional settlement | Actual war parties and valid war provenance | Diplomatic time, normally 120 to 180 days | Region-specific peace and recovery | Uses the same verified selective-settlement owner as master acceptance |
| R01 Defend institutions | Macedonia in radical contest, specific missing objective | 25 to 60 PP and optionally 15 to 30 CP, within 90 to 120-day crisis | Restores a named institutional condition | Success depends on stated objectives, no hidden overriding roll |
| R02 Radical commitment | Explicit route focus and eligible contest | Political commitment and transformed institution states | Radical takeover and Front responses | A one-way doctrine decision until an actual overthrow or defeat |
| R03 Universal conquest | Radical government and completed expeditionary prerequisites | Real military and supply commitments | War planning and actual conquest before terminal lock where chosen | No remote civilian-loss effect before reach and terminal authorisation |
| R04 Terminal commitment | Current Chaos strictly above 1000 and every separate power, history and scenario condition | Explicit terminal focus, 90-day authority endurance already met | One locked scenario and progressive campaign | Recheck at completion, no reward on rejected launch |
| R05 Regional apparatus | Active terminal regime, actual reachable controlled territory | Two to three factories, 30 to 60 CP and material where required, 120 to 180 days | Increased bounded administrative reach | Revalidate before every loss, stop immediately on defeat or lost authority |
| S01 Survival coordination | Rejecting sovereign countries | 25 to 60 PP, 90 to 180 days | Treaty, aid and compatible operational cooperation | Does not force global peace or erase existing alliances |
| S02 Evacuate survivors | Shared migration route and reception capacity | Real transport or supply commitment, 90 to 180 days where feasible | Measured survivor arrival and truthful route losses | Native emergency evacuations may be shorter where the migration owner supports them |
| S03 Disrupt the apparatus | Actual reachable resistance or military target | 20 to 45 CP and appropriate support, 90 to 180 days | Reduces or halts local campaign capacity | No planet-wide shutdown from one small action |
| S04 Restore civil institutions | Defeated radicals and actual surviving government | 35 to 75 PP, one to two factories, 180 to 365 days | Recovery, accountable administration and constitutional route restoration | Cannot resurrect people, duplicate buildings or reverse foreign independence |

These rows map every action family promised in the design. Implementation may create target-specific decisions within a family where they have distinct counterparties or outcomes. It must not reduce the table to one generic improve-value button, and it must not put every target on screen at once. Use target selection, relevant family filters and a maximum of six current primary actions.

## Action type, phase visibility and mission slots

U01 through U04, U06, C01 through C04, N01 through N09, B01 through B06, F04 through F07, R05 and S01 through S04 are decision-started operations with one visible mission each when their work is timed. U05 is an immediate uprising commitment backed by the preparation missions. C05, F02 and F03 are event options with a persistent matching decision when a response remains outstanding. F01, R02, R03 and R04 are focus commitments that invoke a transaction or reveal actions, not extra timed decision missions.

R01 is a family of immediate resource and institutional commitments inside the single radical-contest mission. Its three objectives are subconditions of that crisis, not three additional hidden missions. The autonomy review and independent survival checkpoint are each a visible passive mission only when they are the current national crisis. Qualifying elapsed history outside a current crisis is a dated receipt, not another objective the player must manage.

Terminal 30-day physical-loss jobs are consequences of the active campaign, not spendable player missions. The player-visible R05 regional apparatus projects still count against the three-mission limit. The event can have no more than three mission objects per actor across all its categories, and no more than two ordinary optional operations while a national crisis slot is reserved. A new crisis never silently deletes or shortens an existing mission. It uses the reserved slot, or offers an explicit choice to cancel a cancellable optional operation with the correct refund before opening its deadline.

| Phase and view | Up to six primary action families in the current view | Active mission rule |
| --- | --- | --- |
| Controller local response | C01, C02, C03, C04, C05, U06 counterpart | One response or compact crisis plus at most two optional operations |
| Underground, viewed by a real sponsor or later IMRO government | U01, U02, U03, U04, U05 as a nonbinding movement recommendation before government control, U06 | One preparation or discovery mission plus two operations. NPC timing and political acceptance remain with the movement |
| Country home programmes | N01, N02, N03, N04, N05, U06 if an existing compact needs review | Three total, with crisis slot reserved when a national crisis is eligible |
| Country territorial view | N06, N07, N01, N04, B04, B05 where eligible | Same shared slots as home programmes, not three extra |
| Country institutional view | N02, N08, N09, N03, B06, N01 where eligible | Same shared slots, route-incompatible actions hidden |
| Balkan partner view | B01, B02, B03, B04, B05, B06 | At most two partner operations and one crisis across all views |
| Front member view | F04, F05, F06, F07, S01, N04 or an equivalent national reinforcement action | Same shared slots, selected target determines exact counterpart |
| Former-master response | F02, F03, F07, F04 where later cooperation is legal | Response is immediate, settlement mission counts only if a real negotiation follows |
| Radical contest | R01 institution actions, R02 commitment entry and relevant immediate national response | One crisis mission, no concealed extra objective missions |
| Radical campaign | R03 conquest actions, R04 commitment entry, R05, N04, N05, F05 | Three projects total, not three in each region |
| Survival and recovery | S01, S02, S03, S04, F04, F07 | At most three actual operations, with recipient capacity checked before evacuation |

View selection and target selection are navigation controls. They do not spend resources or count as actions. Only the current relevant view exposes its primary actions, while a common mission area continues to show every active IMRO mission. A target-specific variation replaces its family row instead of adding another always-visible button.

## Exact quote calculation and payer contracts

For each action's stated range, choose its light, standard or major band from the quoted difficulty. The initial deterministic quote is the low endpoint for light, the midpoint rounded up to the nearest five for standard, and the high endpoint for major. Equipment midpoints round up to the nearest 25. Time uses the low endpoint, midpoint rounded up to a whole day, or high endpoint. Where only one value is stated, use it unchanged. These rules turn the ranges into actual reproducible prices without requiring the implementer to choose an arbitrary number per click.

Target size uses the verified population or project magnitude, difficulty uses actual damage or relevant resistance, and route risk uses the current access and blockade condition. The classifications below are the normative initial quote contract. Two severe conditions or a distant theatre without an established own or consenting-partner depot select major. One severe or two ordinary conditions select standard. Otherwise use light. A route that has no viable access is ineligible, not merely expensive. Standard native population and damage measures may appear in the selected-target explanation, but no new persistent difficulty meter is introduced.

For initial regional projects, a small target is below one million current residents, ordinary is one to five million and large is above five million. These are game planning bands, not historical demographic claims. Construction damage uses the actual fraction of relevant damaged infrastructure: below one quarter, one quarter through one half, or above one half. Existing compatible project owners may supply their own verified size and damage bands through an adapter, with one shared quote used by every consumer.

| Quote input | Low | Ordinary | Severe or ineligible |
| --- | --- | --- | --- |
| Resident target size | Fewer than 1,000,000 current residents | 1,000,000 through 5,000,000 | More than 5,000,000 |
| Relevant construction damage | Less than 25 percent of the affected capacity damaged | 25 through 50 percent | More than 50 percent. No valid building slot or physical project makes construction ineligible |
| Resistance opposing the acting controller | Actual local resistance below 25 | At least 25 and below 60 | At least 60 |
| Resistance supporting a movement or survivor operation | Actual relevant resistance at least 60 | At least 25 and below 60 | Below 25. A required local contact or target reach remains a separate hard condition |
| Local civic or productive institution | Relevant institution functioning and its applicable guarantee honoured | Institution provisional or repairable and still operating | Relevant institution disrupted or breached. A completely absent required facility blocks its dependent action |
| Controller security facing cell work | No active verified containment commitment | One effective C01 or C02 commitment affecting the target | Both commitments or an active C04 security operation. Mere chosen policy without an effective operation does not count |
| Distance | Same state or an adjacent state connected by a viable land route | Further within the same bound world macroregion with a viable contiguous land route | A maritime route or a different macroregion. This is the distant class used in the major-band rule |
| Access | Own route with actual delivery capacity | Continuous granted access through willing parties with actual delivery capacity | Intermittent but presently usable access documented by the route owner. Absent, revoked or physically unusable access is ineligible |
| Blockade or transport interruption | No measured current interruption on the selected route | More than zero and at most 50 percent unavailable capacity | More than 50 percent unavailable capacity. Zero remaining delivery capacity is ineligible |
| Relevant war exposure | No active war threatening the selected actor or target | An active relevant war with the target still secure and supplied | Target under active attack or verified local supply disruption. Loss of required control or route is ineligible |
| Negotiating parties | Two substantive parties | Three or four | At least five. Count actual required signatories, not nominal Front roster size |

The macroregion binding and delivery-capacity measure must come from their verified map and route owners. If a required input is unknown, the action cannot fabricate a light quote. It remains pending that evidence. Terrain affects the actual route and effective security classification, so it is not counted again as an independent difficulty multiplier. Mandate is an eligibility and outcome value where specified, not a substitute for resistance data or a spendable quote input.

| Action families | Inputs used for band selection and exact exceptions |
| --- | --- |
| U01, U03, U04 | Supporting resistance, relevant local institution and effective controller security |
| U02, B02, F04 | Recipient target size, distance, access and measured transport interruption. Use the frozen action-family quantity, not a promised shipment or a quantity chosen to manipulate its own band |
| U06, C03, N06, B04, B05, B06, F06, F07, S01 | Actual negotiating parties, relevant war exposure and route/access where a physical mission is required |
| C01, C02, C04 | Resistance opposing the controller and relevant war exposure. Add actual damage only for C02's physical protection work |
| N01, N05, N07, N09, R05, S04 | Target size, relevant construction damage and relevant productive institution. Multi-party production also includes the actual signatory count |
| N02 | Target size and functioning civic institution, with one settlement receipt per genuinely unresolved represented issue |
| N03, N04 | Relevant defence institution and war exposure determine time and any stated CP range. Manpower and equipment remain the exact selected template requirement |
| N08, F05 | Distance, relevant war exposure and actual signatory count. The existing force or obligation is separately and explicitly identified |
| B01 | Distance and access. Contact alone never creates supply or a new country |
| B03 | Actual participant count and route access determine resource band. Duration is 240 days without common military pressure, 180 when one participant faces the relevant active conflict, and 120 when at least two ready participants face the same controller's actual conflict. Freeze that state at start |
| R01 | The relevant institution is functioning, provisional or disrupted for low, ordinary or severe. The current crisis fixes the completion deadline. Paying for one objective does not extend that deadline |
| S02 | Use the migration owner's verified exact transport quote. The supported route's low, ordinary or severe access/risk condition selects 90, 135 or 180 days unless a documented native emergency evacuation supplies its own shorter duration |
| S03 | Supporting resistance, distance and relevant war exposure, with actual local target reach required |
| U05, C05, F01, F02, F03, R02, R03, R04 | No invented ranged resource price. Use their stated immediate commitment, diplomatic response, existing mobilisation receipt or native focus duration and hard conditions |

These are initial design constants and classifications, not claims that current engine adapters already expose every input. Calibrated changes must update this owner contract and all affected scenario evidence together. An implementation may use an established project owner's classification only after showing its exact mapping and preserving the stated affordability and outcome relationship.

| Contract type | Payer and exact commitment | Consent and closure |
| --- | --- | --- |
| Local PP or CP action | Actual country actor or explicitly consenting sponsor pays the quoted native amount once | A countryless NPC movement has no national-resource price and no treasury. No other country is charged through the actor's scope |
| Equipment shipment | Named sender pays the exact quoted equipment type and quantity from its stockpile | Recipient accepts the offer before dispatch. Receipt records delivered, intercepted, returned or cancelled quantities with a zero residual |
| Training and force generation | Actor commits the exact manpower and equipment required by the verified selected template, reduced only by real preexisting cadre and store assignments | Template cost is the quote. A formation cannot use a qualitative promise as payment |
| Construction | Actual government or consenting project sponsor reserves the quoted one, two or three civilian factories for the quoted duration and pays the verified owner's material requirements | Count factories, PP and each material type within the four-type cap. Excess requirements must be a distinct transparent project stage rather than hidden extra costs |
| Two-party negotiation | Each party sees its own PP quote. A minimum 25 PP base within the quoted family range applies to a substantive negotiating party, with no equipment charged unless offered separately | Reserve both accepted quotes, revalidate both actors and then commit together. No actor pays for the other without a separate explicit aid contract |
| Command mandate | Granting member pays 35, 55 or 75 PP for the selected band and commits a specifically listed existing force or a support obligation. IMRO pays no undisclosed matching cost | Both accept purpose, theatre and duration. Command coefficient is active only after the specified real contribution and supported command or logistics arrangement exist |
| Shared production compact | Each participating government approves its own listed factory, PP and material commitment before start | If one rejects or becomes invalid before commit, release every unspent reservation and do not begin the compact |
| Evacuation | The requesting government or named willing sponsor pays the migration owner's exact transport and capacity quote | Destination consent and capacity exist before departure. Actual survivor and loss receipts close the transfer |
| Terminal apparatus | Regime pays the quoted factory commitment, CP and at most two material types selected from actual equipment needs | Capacity comes from the completed project and current reach. It is not an unlimited death command purchased with CP |

C04's security commitment is a tied-down existing-force requirement, not a second hidden spend. It requires one actual compatible security formation for the selected state, at least half its authorised manpower strength, in the required controlled area and not already reserved to another IMRO operation. Record the unit identity, owner, target, current strength and mission generation in a reservation receipt. The country retains the unit and its normal manpower, equipment and war-casualty ownership. The CP quote pays for the operation and is consumed once work begins.

Moving or assigning the formation elsewhere, dropping below the required strength, losing state control or ending the policy closes the dependent operation without further campaign effects. Completion or cancellation releases the reservation immediately. It does not create a replacement formation, duplicate equipment, return spent CP or refund casualties. Revalidate the existing formation before each consequential step and reconcile its identity on save/load. If the current engine cannot safely identify and release this reservation, keep C04 unavailable until that owner contract is proven. Optional direct equipment expenditure would require a separately displayed and audited revised quote, rather than being inferred from the words security commitment.

Offers have a 30-day administrative response expiry that is not a new player mission and consumes no resources beyond an explicitly shown proposal cost. Ordinary substantive work keeps its 90 to 365-day mission duration. Before a multi-party project commits, accepted reservations remain reversible. On final acceptance, revalidate the complete participant set and quotes. If any party cannot pay, nobody's irreversible delivery or construction begins, and only already spent proposal effort remains spent. Once work actually starts, each resource follows its own paid and consumed receipt.

The receipt contains actor, payer, recipient, target, operation ID, generation, quote version, each resource amount, reserved amount, paid amount, consumed amount, refunded amount and terminal disposition. Every resource must satisfy paid equals consumed plus refunded plus any still-valid reserved delivery balance. A final closed receipt has no unexplained balance. Proposals cannot be accepted from stale event targets after a government or country has disappeared.

## Cross-owner Chaos attribution

Each political impact uses an immutable consequence identity with originating event, originating generation, affected actor or region, actual result and source receipt. The shared Chaos registration owner stores whether that consequence has already been credited. Event 110 supplies the design's total political-shock budget for the consequence and receives only the remaining uncredited amount. If an earlier owner already credited a larger amount, IMRO adds zero and does not subtract the earlier owner's legitimate result.

Manifestation, armed uprising, achieved independence, regional spread and global declaration are distinct consequences only when their distinct observed results exist. A new display or a connected-event-fired flag cannot create another identity for the same event. The worldwide declaration is one political shock with a capped aggregate, not a per-subject political award plus the same global award again. Generic military war and Deaths contributions remain separate only for their actual different consequences.

The 006, 063, 095 and actual 106 adapters must publish or consume the same shared identity where they describe the same release, revolt or resistance consequence. The parent integration owner must inspect the current generic war callback and ensure that any event-specific declaration bonus is not duplicating the political shock already budgeted here. Normal later military casualties and real war escalation retain their legitimate shared contributions. If an owner cannot expose provenance, the overlapping discretionary IMRO political award stays withheld until the shared receipt is reconciled. No estimate based on the current total Chaos is an acceptable duplicate check.

## Authority contribution safeguards

A fulfilled coalition obligation counts only after a materially useful shipment, completed common project, verified defence or successful agreed protection. For the 15-point fulfilled-obligations component, allow at most 5 points from one recipient within 180 days and at most 3 from one operation family. Repeated partial deliveries of one contract share one receipt. Cosmetic promises, a returned loan, a shipment between the same actor and itself or a transaction with an invalid recipient grant zero.

The 15-point logistics component requires actual route coverage, with 5 points for each of three distinct valid theatres. Theatres must contain meaningful members and a live supply obligation, not empty map markers. Destroyed or withdrawn links cease contributing at the next exact lifecycle update. UI gives a qualitative explanation of fulfilled, missing or broken requirements and the one Authority value, rather than exposing five more gauges.

## Chaos impact map

Chaos is a world-system consequence, not a second reward currency. Use the existing shared registration owner and apply a separate source receipt for each genuine political event. The figures below are proposed starting bands. Normal death-derived Chaos stays with the Deaths system, and ordinary war-related Chaos stays with its existing owner.

| Manifestation or result | Proposed Chaos change | Dynamic scale | Guard and overlap rule |
| --- | --- | --- | --- |
| First credible armed movement becomes public | +2 | One local destabilising manifestation | Once per originating event, not on initial hidden candidacy |
| Actual Macedonian uprising | +3 to +5 | Territory and controller's real exposure | Once per rising generation, subtract any same-event shared revolt award rather than doubling it |
| Failed severe containment | +2 to +4 | Actual surviving movement and demonstrated state weakness | One per distinct major containment episode, not every failed investigative action |
| Independent IMRO Macedonia established | +10 to +15 | Military or diplomatic regional consequence, viable state required | Once for first real independence, no extra award for an ideology change |
| Honoured autonomy or peaceful local containment | -2 to -5 | Durable settlement and resolved crisis | One closure receipt, no repeated review farming |
| Movement defeated | -3 to -8 | Actual regional crisis ended | Does not subtract unrelated resistance or war Chaos |
| Balkan network materially spreads | +3 to +5 per new significant region, capped at +15 for the regional phase | Actual distinct organisation or rising, not nominal contact count | Recipient and region receipt, no duplicate 006, 095 or 106 consequence |
| Regional compact settles several disputes | -3 to -6 | Actual implemented settlement | One compact or treaty milestone, not one reward per popup |
| Worldwide Freedom or Death completed | +20 to +50 | 20 base, plus 5 for each additional meaningfully affected macroregion, plus 5 if at least three distinct masters are affected, cap 50 | One global receipt. Includes the declaration's political shock, not duplicate per-subject war awards |
| Worldwide liberation wins a distinct major regional struggle | +5 to +10 | Demonstrated breakdown of an old subject order | At most once per region, no replay on routine peace confirmations |
| Large regional restoration or settlement reduces the crisis | -5 to -10 | Actually ended conflicts and stable sovereignty result | Actual peace proof, no reduction for an issued but ineffective white peace |
| IMRO first obtains substantial cross-regional command | +5 to +10 | Authority at least 60 plus meaningful command in two regions | One unusual-power receipt, no award for reaching 60 repeatedly |
| Radical takeover changes a major existing Front | +5 to +10 | Actual government change and international rupture | One real consequence, no award for evolution reveal or focus unlock |
| Radical conquest establishes a new major theatre | +5 to +10, capped at +20 before lock | Actual sustained conquest beyond the existing regional question | Political consequence only, excludes routine war and death duplicates |
| Terminal commitment | +20 to +30 | Actual qualified world-end launch | Once, checked only after Chaos already exceeds 1000, so the award cannot supply its own threshold |
| Terminal atrocities | Shared Deaths result only | Actual observed physical losses | No additional IMRO per-death or per-state award |
| Radical regime defeated | -20 to -40 | Pre-lock major threat or active terminal campaign ended | One observed defeat, preserve other threats and prior deaths |

The entire early route should contribute tens of Chaos through real consequences, not hundreds manufactured to guarantee the endgame. Exceptional global destruction may drive Chaos much higher through existing systems. Containment and negotiated outcomes can reduce destabilisation without pretending the dead return or the historical liberation never happened.

## AI strategy matrix

AI policy uses eligibility first, affordability second and contextual preferences third. It must never assign a positive weight to an impossible operation and hope the trigger catches it later. Preserve a reserve of PP, command capacity, equipment and manpower appropriate to the country's actual war unless the action directly prevents imminent collapse.

| Actor profile | Preferred conduct | Avoids | Changes under pressure |
| --- | --- | --- | --- |
| Capable calm controller | Targeted intelligence, credible autonomy where useful, transport protection | Expensive indiscriminate repression and unnecessary additional wars | Severe local exposure raises negotiated settlement preference |
| Overstretched controller | Consolidated defence or settlement | Repeated investigations without staff or supplies | A viable IMRO army and broader war make independence recognition more attractive |
| Fragile underground | Civic support, secure cells and delivered arms | Premature rising without viable supply | A real fleeting opportunity may justify a smaller early rising |
| Established movement | Balance Mandate and readiness, choose a survivable moment | Permanent postponement while the controller dismantles it | Broken autonomy increases rising preference only when it can survive |
| Civic Macedonia | Reconstruction, recognition, local rights and charter aid | Coercive integration and contradictory patron obligations | Prioritises homeland defence, then protects credible partners |
| Anarchist Macedonia | Delegate mandates, communal logistics, voluntary aid | Distant war without consent or supply, permanent emergency rule | Renews bounded common command during a real invasion |
| Independent socialist federation | Complementary industry and negotiated partners | Automatic surrender of sovereignty for a small shipment | Can accept limited urgent aid while retaining a route to renegotiate |
| Patron-aligned state | Fulfil useful contracts and secure actual support | Repudiation before alternative supply exists | Escapes dependency when patron coercion outweighs delivered protection |
| Central revolutionary state | Concentrated reconstruction, professional forces, bounded territorial policy | Unwinnable multi-front expansion | Internal reform becomes attractive after stable victory or costly failure |
| Foreign sponsor | A real strategic or political return for useful aid | Infinite aid to a network openly opposing its objectives | Renegotiates, withdraws or separately escalates when the network becomes autonomous |
| Newly freed subject | Defend homeland, request feasible aid, build replacement supply | Irrelevant overseas adventures while losing its capital | Accepts reasonable regional peace preserving sovereignty |
| Former master | Compare actual restoration prospects with costs | Fighting every subject forever despite no access | Accepts when overstretched, fights when credible and politically committed |
| Ordinary Front member at doctrine split | Reject or withdraw from a doctrine threatening its people | Automatic obedience based on old membership | Coordinates survival if the regime becomes a direct threat |
| Radical IMRO | Build real command and logistics, pursue unlocked conquest, qualify legitimately for lock | Terminal focus with failed power or history conditions | Cannot continue mortality after authority is destroyed |
| Surviving opponent | Defend threatened populations, preserve routes, support defections and defeat command | Wasting scarce resources on an unreachable symbolic target | Broadens cooperation across ideology when actual global danger grows |

No numerical AI probability is claimed in this specification. Implementation must define source weights and run exact or bounded probability analyses appropriate to each surface. An `ai_will_do` score is not a normalised percentage. A random event option pool, a timing distribution and a focus selection score need different evidence.

## Required probability scenarios

Preserve immutable before-source files and SHA-256 evidence before changing any existing weight. Save the same complete scenario set and candidate pools for before and after comparisons. At minimum cover calm low-Chaos controller, high resistance without IMRO Mandate, high Chaos without local support, war-exposed controller, two incompatible patrons, living Event 006 Macedonia, civic and anarchist constitutional choices, a small versus large Front, a weak versus strong former master, nested subjects, a human member's doctrine rejection, failed and successful institutional defence, nominal Authority without real power, and a qualified radical world command.

Expected ordering is part of the test. Targeted containment should outrank futile repression for a calm capable controller. Prepared rising should outrank a supply-less attack. Actual viable aid should outrank symbolic unreachable aid. Ordinary members should overwhelmingly reject the death doctrine. The terminal launch score must be zero whenever any hard requirement fails. Exact calibrated percentages are an implementation output after analysis, not invented evidence here.
