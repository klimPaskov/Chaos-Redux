# Recovery and government response

## A finite aftermath

The disappearance is already complete when the government responds. The response system helps the country live with the loss. It does not provide a menu for choosing a different victim, rerolling the missing category, or buying the exact missing objects back from an identified source.

A compact temporary decision category appears only when at least one relevant response is available or running. It presents the actual incident summary and up to four response types. A country may run one Event 094 government program at a time. Ordinary production, recruitment, diplomacy, research, and other event systems continue independently.

Response options remain available for 180 days after the relevant incident. A program started within that period can finish its normal duration. A later incident updates the available context without canceling paid work, resetting a clock for free, or stacking another copy of the same modifier. Each response type can be used at most once per country in any 365-day period.

The disappearance itself is not softened by these limits. They limit response farming and interface repetition. A country can lose resources again while a reconstruction program is running.

## Arsenal reconstruction

This response is available after a meaningful equipment-stock loss when the country has functioning military production and can spare the proposed cost. It redirects administrative and civilian support toward rebuilding military reserves.

The proposed starting cost is 25 Political Power and the occupation of one available civilian factory for 90 days. During those 90 days, military factory output receives a 15% bonus. The country still chooses its production lines and supplies their normal inputs. The program does not materialize the missing equipment or replace foreign variants with invented domestic copies.

The opportunity cost is visible before commitment.
A country which needs its only available civilian factory for another urgent task can decline and continue normal production.
The program is worthwhile when additional military output matters more than that civilian capacity and political spending.

A [Greenland Sale reserve allocation](../092_greenland_sale_specs/092_greenland_sale_spec_part_02_purchasing_power_and_payment.md) and this program cannot occupy the same civilian capacity at the same time.
The player can reduce future auction-reserve production to free capacity for arsenal reconstruction, or keep funding a desired purchase and rely on normal military output.
Stopping new reserve production does not withdraw an accepted bid, refund spent principal or erase already earned reserve.
The AI makes that choice from its current war demand and real free capacity rather than charging both projects against the same factory.
A future acceptance case should give a country one available factory already committed to reserve production: reconstruction stays unavailable until that commitment is genuinely released, and no later daily accrual credits the same factory to both uses.

The bonus ends when the program ends. Cancellation releases the factory and ends the bonus, without returning Political Power or deleting equipment legitimately produced while it was active. If the country loses the capacity required to operate it, the program closes cleanly and reports the interruption without imposing another arbitrary loss.

## Command reorganization

A country which has lost generals, field marshals, or admirals can organize a temporary effort to help surviving leadership absorb new responsibilities. The proposed starting cost is 20 Command Power. For 90 days, army and naval leader experience gain receives a 15% bonus where those command systems exist.

The player still appoints commanders and fights or trains through normal systems. Newly recruited people do not inherit the absent commanders' skill levels or traits. This response rewards the work of rebuilding competence rather than filling a list with exact replacements.

The response is not available merely because Command Power or Army Experience was halved. It addresses actual leadership disappearances. A country with no surviving or legitimately recruited eligible leadership has no useful recipient for the bonus and must first resolve that vacancy through normal recruitment.

## Laboratory continuity

A country with compatible unfinished research loss or missing scientists can protect the continuity of the surviving research effort. The proposed starting cost is 25 Political Power. For 90 days, ordinary research speed receives a 10% bonus.

The country still has to assign valid researchers and pursue valid projects. The bonus does not return the missing progress instantly, restore completed technologies that were never lost, or generate a missing scientist. Special projects only benefit through their own explicitly supported continuity operation. A generic research bonus must not be advertised as accelerating every scientific system.

When Wu or Kruger is missing, the unique owner may expose a specialized continuation choice instead of the generic program. The two versions occupy the same Event 094 response slot. They cannot be combined into duplicate bonuses simply because a named character appears in two rosters.

## Support for remaining households

A population disappearance enables a support response centered on remaining people, unresolved inquiries, and functioning local institutions. It has two mutually exclusive approaches within the same response, with the same eventual civic result.

The funded approach costs 25 Political Power and occupies one civilian factory for 60 days. The local-assistance approach has no stockpile or Political Power cost and takes 120 days. It still occupies the country's single Event 094 program slot. The slower route ensures that an exhausted country can make a meaningful response without conjuring funds it does not possess.

Completion records a successful support effort and grants up to five percentage points of stability, limited by the ordinary stability ceiling. This does not restore population or imply that the missing people have returned. At full stability the civic record can still be completed, but the interface must state that no additional stability can be gained.

The program offers a faster paid response or a slower low-resource response. It does not punish a country with another mass loss for failing to finish a countdown. Cancellation gives no completion reward. A new disappearance cannot award the reward again before the shared 365-day response-type cooldown expires.

## Clear costs and closure

A displayed cost must match the actual cost at the instant of commitment. The four proposed programs use at most two spendable resources or occupied-capacity types each. Command Power costs remain below the project limit of sixty. No hidden fifth resource, percentage stock debit, or delayed payment is added during implementation.

All temporary effects have a defined duration, interruption rule, and cleanup path. Annexation ends the former country's government program. A surviving tag's ordinary capitulation does not automatically end a viable local-assistance effort, while a factory-dependent program must still have the necessary capacity. Country transfer does not let the same program pay a second reward.

A report closing the category summarizes the work completed and the circumstances still unresolved. It does not declare the mystery solved. When no relevant option or active program remains, the category disappears from the normal decision list.

## Assistance from other countries

Normal lend-lease, trade, recruitment arrangements, research cooperation, and medicine access can matter more after a disappearance. Half gone can make an existing offer contextually more attractive or allow a short owner-managed request when that diplomacy already exists.

The donor must supply something real. The victim's deficit is not a license to create resources simultaneously in two countries. An offer can be declined, may become unaffordable, and must respect ordinary wartime and diplomatic restrictions. Half gone does not introduce a universal aid button which bypasses them.

Foreign aid supports the remaining country. It does not move the missing population to the donor, establish blame, or erase the incident from history. A replacement commander or visiting scientist is a new participant with legitimate ownership and skills.

## AI response priorities

AI countries suffer the same committed loss and the same category sampling as human countries. They do not select a safer category after seeing the result and do not receive hidden replacement grants.

The AI first checks whether an action is currently available, useful, affordable, and compatible with its active program. It never spends a resource promised only by a future recovery. A program with no eligible recipient or no possible effect has no weight.

Arsenal reconstruction is attractive during sustained military demand when spare civilian capacity exists. It is less attractive when the country cannot maintain meaningful production or urgently needs that civilian capacity for survival. Command reorganization rises in priority after important command vacancies and when surviving leaders are actively gaining experience. Laboratory continuity rises when important unfinished research remains and the necessary staff are available.

Household support is important after a population disappearance, especially where current stability leaves room for the civic benefit. The funded route is preferred when the country can afford its opportunity cost and earlier completion matters. The slower route is preferred when resources are scarce. The AI can decline other programs rather than spending itself into a worse crisis for a negligible bonus.

The proposed decision weights begin from these utilities, not fixed probabilities. The implementation must audit complete legal option pools and include wartime, peacetime, low-resource, multi-loss, and unique-character cases. This specification does not label untested weights as validated behavior.

## Preventing a second bureaucracy

The category needs a short incident summary, relevant choices, and a visible active-program duration. It does not need four new meters, a dossier window, a permanent investigation board, or a new focus tree. Ordinary owner interfaces remain responsible for recruitment, research assignments, medicine access, and production.

The finite response programs are optional extensions to normal recovery. Their value should be assessed against their visible costs during balance testing. A response which is never worth using should be retuned or redesigned, rather than protected by forcing every affected country to take it.
