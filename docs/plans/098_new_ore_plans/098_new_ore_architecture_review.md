# Event 098 New Ore: scripted architecture review

Historical initial research and proposals.
Final accepted design and dispositions are in [the source review](../../specs/098_new_ore_specs/098_new_ore_review_record.md) and [098_new_ore_final_technical_review.md](098_new_ore_final_technical_review.md).
This report's pending choices and workspace/source observations remain provenance for its original revision, not instructions to reopen settled design.

Status: research and proposed implementation contract, awaiting parent design integration and later native validation. No gameplay files were edited. Source gate passed before this research began.

Repository evidence is pinned to `klimPaskov/Chaos-Redux` commit `a3ef485c5da7e2337122eca04ac65c175050f251`. Current user decisions govern this review. Older source mechanics are evidence of existing implementation, not accepted constraints that weaken the requested result.

## Principal findings

The requested benefit must be actual armor, available to existing and newly produced applicable equipment and forces, and must be at least 1.5 times their otherwise identical armor without Event 098. A nominal additive coefficient of 0.50 does not establish that result. The current legacy implementation does include real equipment armor, but its `armor` equipment type alone fails to establish broad coverage. A fetched concrete counterexample is Event 012 elephant equipment: its archetype is `type = infantry`, with armor 58, although the associated subunit declares both infantry and armor types and has its own armor 58.

The legacy event initially awards the idea to the state's owner. The user requires its actual current controller, including an occupying country or subject that controls it. Its cancellation and removal scripts query a state-local ID through controlled-state iterators, while discovery also writes a global singleton. The iterator may legally resolve that state-local ID, so this review does not claim a proven variable-scope defect. Transfer uses a country scan following idea removal. That structure is unsuitable as the authoritative multi-deposit lifecycle or proof of immediate transfer.

A state-attached registry and narrow reconciliation callback are the recommended architecture. Actual armor application is a separate adapter with a strict numeric acceptance contract. Current Event 028 authors `armor_factor` in country ideas, which warrants investigation before choosing the older equipment-bonus approach. Neither source authorship nor the offline wiki establishes its native coverage or effective stacking.

## Evidence and its limits

All links below address the pinned repository snapshot. Research snapshots and file blob SHAs are preserved in `source_gate/systems/research_manifest.json` and `source_gate/systems/additional_research_manifest.json`. Copied source files are under `source_gate/systems/research_sources/`. The source gate ledger is separate from these later targeted research reads. Offline wiki research was targeted to relevant sections, not claimed as another complete source-gate read.

| Reference | Observed source | Consequence |
| --- | --- | --- |
| [events/098_new_ore.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/events/098_new_ore.txt#L30-L40) | `random_state`, only excluding an existing marker, state-local `ore_state`, singleton `global.ore_state_container`, owner gets idea | Preserve global state draw, replace actor and authoritative storage. No source proof of fire-once or validity beyond marker. |
| [common/ideas/098_new_ore_ideas.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/ideas/098_new_ore_ideas.txt#L10-L33) | Civil-war copying, cancellation, `every_country` on removal, armor attack/defense/speed 1.00, `equipment_bonus armor armor_value = 1.00 instant = yes` | Actual equipment armor exists in authored code. Other combat stats are not substitutes for it. Cancel evaluation timing and equipment reversal require validation. |
| [common/dynamic_modifiers/098_new_ore_dynamic_modifiers.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/dynamic_modifiers/098_new_ore_dynamic_modifiers.txt) | Marker and icon only | State attachment can retain a marker independently of beneficiary country. |
| [common/ideas/028_asteroid_incoming_ideas.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/ideas/028_asteroid_incoming_ideas.txt#L276-L327) | Main crater and fragments use country `armor_factor` | Alternate armor hook is source authored. Its presence does not certify native semantics. |
| [common/on_actions/029_riches_found_on_actions.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/on_actions/029_riches_found_on_actions.txt) | State-control callback plus bounded registered mines for annexation, peace, capitulation | Closest current event-driven territorial lifecycle precedent. Reuse contract ideas, keep 098 state and receipts independent. |
| [elephant equipment](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/units/equipment/012_africa_elephant_equipment.txt#L31-L47) and [elephant unit](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/units/012_africa_elephant_forces.txt#L39-L69) | Infantry equipment archetype with armor 58, subunit own armor 58 | Equipment types and unit types are distinct. Own-subunit armor must be covered. |
| [coal golems](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/units/coal_golems.txt#L33-L66) | Infantry/armor unit, own armor 58 | Second concrete force-level armor contribution needing coverage. |

Offline documentation was fetched from the repository, never the live Paradox Wiki. These snapshots are technical references, subordinate to installed game documentation and native observation. Exact key excerpts are:

- Idea modding line 161: “an equipment archetype or a type of equipment archetypes.” The same paragraph documents `instant = yes` as the way to avoid waiting for a newly researched technology. This supports a retroactive candidate, not proof of every imported variant's entitlement or removal.
- Modifiers line 130: “Non-modifier idea attributes such as `equipment_bonus` or `research_bonus` are impossible to use inside of dynamic modifiers.”
- On actions line 450: “ROOT is new controller, FROM is old controller, FROM.FROM is state ID.”
- List of modifiers line 104 identifies `armor_value` and says “must be used in an eq. category.”
- Scopes line 529 documents random state selection from matching states. Its example line 586 also permits a priority list. It does not explicitly prove a uniform distribution.

[Idea modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Idea%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md), [Modifiers](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Modifiers%20-%20Hearts%20of%20Iron%204%20Wiki.md), [On actions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/On%20actions%20-%20Hearts%20of%20Iron%204%20Wiki.md), [List of modifiers](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/List%20of%20modifiers%20-%20Hearts%20of%20Iron%204%20Wiki.md), [Scopes](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Scopes%20-%20Hearts%20of%20Iron%204%20Wiki.md).

## Armor adapter: mandatory behavior and implementation candidates

### Effective ratio

Define `A_without` as the effective armor for the same country, design, equipment, template, strength, and other modifiers with only 098 entitlement removed. For every applicable positive-armor entry and affected formation:

`A_with >= 1.50 * A_without`.

Hold all other inputs equal. A baseline-zero unarmored item remains outside the armor entitlement unless a separate accepted design gives it armor. Do not convert softness, hardness, attack, defense, production throughput, or piercing into claimed armor.

Under an additive model `A_without = B(1 + m)` and an ore coefficient `b`, the ratio is `(1 + m + b)/(1 + m)`. If `m = 0.50`, then `b = 0.50` gives only 33.3% additional effective armor. Even the legacy `b = 1.00` falls below 50% relative uplift when `m > 1.00`. The expression is a conditional mathematical model, not a claim that every game armor phase follows it.

A genuinely independent multiplier could meet the contract directly. If the only legal hook adds to an existing multiplier pool, the adapter must compensate that pool or use a rigorously established bound. A finite constant without a documented bound cannot prove the guarantee. A tiered static idea bank also cannot prove arbitrary positive stacking unless it covers and rounds upward from the entire supported domain.

### Candidate order

1. Inspect installed `documentation/modifiers_documentation.md`, especially `armor_factor` and equipment modifier documentation. Current 028 authored code supplies a source precedent. Determine its legal scopes, armor targets, combination phases, and removal behavior.
2. If that hook supplies broad force armor and supports variable-backed country modifiers, use one 098-owned aggregate country modifier, with the compensating ratio derived from validated semantics. Do not also apply overlapping equipment bonuses by default.
3. If broader armor requires equipment bonuses, generate disjoint archetype/type coverage from actual enabled vanilla and mod definitions, including positive armor supplied by modules. Explicitly include the elephant infantry archetype. Prove how own-subunit armor is multiplied, and use a separate validated force hook when needed.
4. Any uncovered armor-bearing force remains an implementation blocker. Do not call equipment-only coverage complete or weaken the user target.

Inspect legacy and designer tank paths with and without No Step Back, mechanized and armored-car equipment, amphibious armor, supported naval armor, mod custom armored equipment and unit-native contributions. Naval armor may use a separate stat field or application phase. Do not assume a land `armor_value` bonus modifies it. Air defense and hardness are not armor simply because an item looks armored.

Avoid double coverage when an archetype matches a broad type and is also named explicitly. Preserve underlying designs, research, MIO, variants, stockpile counts, and other-event modifiers. Applying/removing 098 must not rewrite permanent equipment designs or create material permanently imbued with the previous controller's benefit.

### Existing equipment and foreign use

The accepted semantic is country entitlement to armor currently used by its forces, not a lifetime property of production origin. Old stockpile items, deployed equipment, new production, captured equipment, purchases, licenses, and lend-lease imports must follow that entitlement whenever applicable. Exporting equipment must not grant the full controller bonus to a foreign country that lacks ore.

Expeditionaries are especially important: distinguish legal unit owner, operational recipient, equipment design origin, and ore-state controller. Proposed default: the country whose force legally owns the division determines entitlement, even under foreign operational command. This avoids granting the host blanket ore powers or silently removing an ore country's own equipment uplift when it sends an expeditionary. Parent should state this actor convention explicitly, then native validation must confirm the modifier follows it. Volunteers need the same check.

## Deposit authority and lifecycle

### State data

Use a 098-owned global registered-deposit array and an independent persistent record on each selected state. The state is authoritative for deposit existence, discovery serial/date, original-deposit identity, grade/depth, evolution receipts, contract recipients/terms, and any outstanding actor/state/deadline receipts. Store actual current controller as a cached reconciliation input, never as the permanent entitlement authority.

Country fields and country ideas are derived views of currently controlled ore states plus valid weaker contracts. The array is bounded by accepted deposit count, not all world states. State and country pointer fields must be distinguished. Use state-validity checks for state IDs, country existence for country actors, and the current callback scope contract.

One authoritative initial-discovery receipt prevents any second deposit from entry replay. Prepare the valid candidate world-state pool without country size, factories, resources, owner, ideology, war, or continent weighting. Recommended validity: an actual usable state in the present map with a resolvable current controller and no 098 deposit. Additional exclusions require a concrete invalid-map reason and explicit documentation. A territory already containing 029 mines or 028 minerals remains eligible.

One world `random_state` with that validity predicate and no priorities is the source-supported candidate. Uniformity is still a required probability inspection/native evidence point. Do not first choose a country and then a state: that changes each state's probability. Discovery commits only after a real state is recorded and registered. Exhaustion returns a no-state result without announcing an invented deposit. Evolution deposits use the current world pool, sample without replacement, and stay tied to their newly selected state.

### Transfer transaction

On a registered state's controller change, capture state, old actor, new actor, deposit serial, and callback nonce before any nested work. Update the authoritative receipt and reconcile affected old/new countries against all their registered ore states. A country retaining another deposit keeps the benefit appropriate to its remaining aggregate. A country losing its last controlled deposit immediately loses the direct-controller grant, though a separately valid weak foreign contract may still apply.

Do not implement transfer through idea `on_remove`, civil-war copying, occupation delay, or recurring cancel polling. The actual removal and new grant belong to the same control-change transaction. Any `do_effect` or cancellation predicate is defensive, not the primary transfer mechanism. Native validation must check timing before the next combat/stat evaluation.

Reconciliation is idempotent. Repeated callbacks remove/add only the 098 aggregate difference, cannot duplicate discovery, payment, evolution, history, or Chaos receipts, and cannot delete 028/029 modifiers. Freeze persistent normal-variable input frames before synchronous helper/event calls. Nested calls may overwrite scratch fields and ordinary targets. Callers initialize every returned temporary field they consume. Clean only fields owned by the transaction.

### Exceptional actor changes

| Case | Required result |
| --- | --- |
| Owner differs from controller in occupation | Controller receives full direct benefit. Owner retains only a valid separately negotiated weak contract. |
| Subject controls ore | Subject is beneficiary. Overlord receives nothing automatically unless it holds a valid selected foreign-access contract. |
| Civil-war split | Deposit remains on its state. Only actual controller receives full benefit. Copied national ideas cannot create entitlement. Reconcile both sides and dynamic tags. |
| Annexation or country removal | Bounded registered states and linked recipients reconcile. Invalid actor endpoints are removed without deleting geological state identity. |
| Peace conference changes owner but not controller | Reconcile transfer-dependent contracts using the same state record. Do not grant ownership-based direct armor. |
| Release/liberation/autonomy change | Benefit follows actual control. Subject status alone does not change the actor. Use documented hooks only where contract eligibility requires refresh. |
| Save/load | Restore registry and derived country view idempotently. No new initial discovery, elapsed-date reset, rerolled state, duplicated payment, or evolution. |

029 source already shows relevant control, annexation, peace, and capitulation lifecycle hooks. Offline on_actions also lists subject annexation, subject freedom, releases, and civil-war ending. Native ordering and civil-war creation behavior remain unresolved. A safe save/start reconciliation can traverse the bounded registry once.

## Weaker foreign access

Use a compact state-bound supply concession between a current controller and a selected recipient. Its full meaning is the deposit identity, recipient, expiry or revocation state, current exporting controller, and current access strength. It grants genuinely useful actual armor below the direct holder's benefit, across the same applicable armor universe. It does not require the foreign country to conquer or become a subject.

Parent design direction: selected finite-term contracts last 180–360 days, use equipment barter, security, or faction terms, and make an actual upfront transfer. The deposit identity remains the contract's source. Capture or counterparty replacement terminates the old deal with no inheritance and no refund. The new controller may negotiate a fresh deal through the ordinary action. Any diplomatic voluntary buyback uses the stored amount actually paid and remaining stored time for a prorated refund. Do not apply that refund to conquest, hostile cancellation, or expiration. This policy supersedes the earlier automatic-inheritance research option and must be made explicit in player terms.

Contracts never grant the direct-holder floor. A recipient's weaker contracts use the strongest valid access grade rather than unrestricted stacking that can overtake direct control. Direct controller status supersedes weaker access without double stacking. Contracts reference state identity, recipient, and the actual contracting controller. War invalidates access according to the final parent contract policy without inventing a deposit or resetting a paid receipt. A transferred geological source can support new selected access, while the prior actor's deal ends.

Use a small targeted decision/event offer, one accepted concrete cost quote/debit, revocation, and the ordinary diplomatic relation/war hooks needed for eligibility. Preserve at most a small accepted number of selected foreign recipients per deposit. Parent owns exact costs and final action count. The free immediate controller armor must not become a paid unlock or production retrofit.

## Evolutions, economy, and AI

Keep geological/evolution receipts separate from actor transfers. Deep Vein upgrades the original state record and its existing concession grades. New Deposits creates dynamic additional world states, with separate discovery identities and the same controller lifecycle. Ore Wars reads strategic current ore states, strongest relevant access, and current political relationships. Its demands and claims use existing diplomacy and war systems with target validation at execution, not a new diplomacy network. Super Alloy amplifies first-deposit power and weak access while decreasing marginal gain from additional deposits.

Aggregation should apply the strongest deposit's full accepted strength first, then bounded declining additional contributions. Parent tuning direction uses effective direct armor +50% baseline, +75% Deep Vein, +200% Super Alloy, with extra-deposit saturation up to +300% event-only. Foreign access uses effective +20%, +30%, +80%, strongest eligible source only, never stacked with direct control. These are intended effective armor uplifts, not raw coefficients to paste into an additive modifier pool. The first deposit remains extreme at Super Alloy even when the country holds only one. Diminishing returns restrain extra deposits, never reduce the original controller's guaranteed floor. Parent owns the final curve and numeric acceptance.

029 Riches Found can recognize a mine and ore co-located in the same state without borrowing its entitlement or receipts. 092 Greenland Sale must pass the actual completed auctioned state identity to this lifecycle. A tag named Greenland or a Greenland-related sale is insufficient. 086 World Claims may select a currently registered ore target through its existing valid territorial route. 028 Asteroid mineral benefits coexist independently, including in the effective-ratio baseline.

Optional economic rewards can supplement armor through real mine output, accepted extraction improvements, access proceeds, or positive discounts. They cannot replace armor. Source-reading requirements permit useful ore beyond the vanilla trade-resource list. Adding a new market resource requires a separate exact engine contract and is unnecessary for this state mechanic.

Parent research reports universal-cost docs/code parity issues. Any positive ore discount, quote, credit, or paid contract must use the shared inclusive affordability/parity contract after verification. Store exact paid receipts and refund only an actual paid amount. Do not assume documentation describing upward quantization proves current implementation.

AI uses the same state and affordability predicates as players. Controllers value access income against giving armor to likely enemies. Recipients value applicable fielded/produced armor, duration, price, and war risk. Ore Wars should compare strategic target value and conventional strength before demanding or pursuing conflict, avoid repetitive doomed demands, and stop on target change. No AI read-only score is allowed to debit, discover, revoke, or mutate state. AI execution still revalidates exact actor/state/nonce and quote.

## Ore Wars native AI pressure

The offline [AI modding page](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/AI%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md), blob `fff532c774c3b8c5605646c18fa75f89088bcbb7`, identifies actual native strategy hooks. These are more concrete than generic decision `ai_will_do` weights. Its table has some inconsistent trigger-description labels, so installed argument/scope documentation must be checked before implementation.

| Hook | Source-documented role | Proposed Ore Wars use |
| --- | --- | --- |
| `conquer` | Country-target war/justification interest, not frontline control | Bounded interest against a valid ore holder after demand refusal |
| `prepare_for_war` | Country-target preparation/deployment | Viable neighboring target, with explicit expiry and cleanup |
| `front_unit_request` | More/fewer units at a selected land front | Current reachable hostile ore-state front |
| `force_concentration_front_factor` | Front force-concentration priority | Support the relevant ore front |
| `force_concentration_target_weight` | Offensive target scoring | Give the actual ore state strategic capture priority |
| `invasion_unit_request` | Units for selected naval invasion target | Coastal ore state when practical naval access exists |
| `invade` | Country-target naval invasion interest | Supplement coastal targeting, never all distant deposits indiscriminately |

The source distinguishes `front_control` orders for already existing fronts from formation of fronts. Avoid `execute_order` forcing or a scripted automatic `declare_war`. Pressure changes incentives and native choices, not a promise that an AI will fight.

A current concrete repository precedent is [common/ai_strategy/018_resources_found_ai_strategy.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/ai_strategy/018_resources_found_ai_strategy.txt), blob `b40ec0bf45e10904c776c4b10c94ea8d2b94cfb6`. Its `resources_found_cave_resource_corridor_offensive` block enables during war only with valid capacity, uses `abort_when_not_enabled = yes`, and pairs `front_unit_request` with `force_concentration_target_weight`. Both filter hostile states neighboring DHO through event-owned objective flags. This shows an existing state-trigger strategy architecture. Its forced front execution belongs to that event's source and is not adopted here.

For 098, proposed strategy predicates select registered positive-grade ore states that the querying actor does not control, with an actual hostile/eligible holder and practical land or coastal route. Tie the actor's campaign to a stored selected state/controller/expiry receipt. Do not boost every marked state for every country. A neighboring land target receives state-target offensive scoring and unit pressure. A coastal target receives corresponding invasion pressure only when naval reach, transport and relative capability are plausible. A distant landlocked site with no route gets diplomatic access valuation, not magical invasion pressure.

The demand action first offers the bounded diplomatic result. A refusal can create an ordinary legal territorial claim or wargoal when final design allows it, and then enables bounded native strategic interest. Acceptance, new access, target capture, control replacement, peace, actor removal, or expiration disables the old campaign immediately. Cleanup subtracts/removes only the 098 contribution and preserves other-event strategies. Native tests must verify dynamic target identity and cleanup semantics before choosing negative-counterweight removal. Current 006/012 source searches demonstrate event-target country IDs in `add_ai_strategy`. No equivalent native proof of variable-backed state IDs was obtained. State-trigger predicates are therefore the better established current-source starting point.

Parent acceptance should require visible strategic targeting evidence for the relevant state plus correct strategy removal. It must not require guaranteed war declarations or guaranteed successful invasions, which depend on ordinary engine planning and circumstances.

## Bounded maintenance and helper layout

Proposed event-owned helpers: deposit registration, deposit reconciliation, country aggregate refresh, contract eligibility/refresh, armor adapter, and committed payment/evolution receipts. Their matching markdown documents scope, inputs, output defaults, side effects, caller map, cleanup, and failure semantics.

The current shared dynamic effect source and registry were inspected for relevant entries. Their published neutral API list covers factory grants, damage, civilian cleanup, technology union, population transactions, and stockpile debits. No armor entitlement API was identified there. Keep 098 orchestration event-owned, extracting a neutral shared helper only when a real second caller and validated common contract exist.

Callbacks touch one changed state plus affected actors. Actor removal and load traverse only the registered deposits/contracts. Evolution service may use the current event-driven due-date pattern identified by the parent in 019. Avoid recurring whole-world scans. Stored dates/deadlines determine elapsed time, not number of callbacks.

## Concrete validation required before implementation can claim compliance

These are unresolved behavioral claims central to this design, not a generic checklist of absent surfaces.

1. Installed armor modifier documentation: prove `armor_factor` scope, equipment/unit/naval coverage and combination phases. Compare it to enumerated `equipment_bonus armor_value instant=yes`. Confirm reversibility.
2. Numeric paired observations: identical armored designs and formed forces before/after grant, with existing positive armor bonuses and independent 028 benefits. Each applicable observation must meet the promised effective ratio, including original contribution plus equipment contribution.
3. Real retained material: deployed old equipment, stockpiles, new production, licensed/imported/captured items, exports, expeditionaries/volunteers. Observe entitled actor and verify no permanent exported benefit.
4. Control transfer: contested state changes hands, old actor has zero and then multiple other deposits, subject control, civil-war split, annexation, release, peace conference, save/load. Observe same-callback removal/grant and stable state identity.
5. Uniform initial draw: one draw over valid WORLD states, no priorities or hidden country-first weighting, exactly one committed deposit, repeat-entry immunity. The role requests `hoi4.probability_inspect`. No callable route was discovered here, so this proof remains pending.
6. Native expiry and diplomacy hooks: concessions use finite stored terms, terminate on capture or counterparty replacement without refund, follow the accepted war rule, expire once, survive load with stored dates, and cannot duplicate charges or grants. Voluntary buyback refunds only the stored actually paid proportional balance.
7. UI/stat evidence: a textual “+50%” tooltip is insufficient. Capture equipment and force armor stats and relevant actual modifier evidence with exact actor/state/scenario. Static MCP source inspection also cannot prove native combat behavior.

Native installed game and read-only HOI4 MCP inspection were unavailable in this session. Available GitHub connector supplied pinned repository files and offline documentation. No claim of gameplay execution, installed-engine proof, GUI validation, save inspection, or successful universal-cost repair is made.

## Handoff conclusion

Parent can specify the state/controller lifecycle, concession rules, dynamic discovery, and evolutions now, while explicitly retaining armor coverage and effective 1.5 ratio as hard implementation acceptance gates. The core direct benefit remains immediate and powerful. Choosing a validated broad armor hook or completing disjoint armor coverage is necessary before calling this mechanic implemented.
