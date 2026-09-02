# Event016 containment decision review handoff

Date: 2026-09-02

Audit mode: bounded read-only source and documentation review; no gameplay edits, no commit, no game launch, no logs, and no MCP probability or compare call.

Scope: the eight decisions in `common/decisions/016_brilliant_scientist_containment_decisions.txt`, their shared constants, the start/resolve/close helpers in `common/scripted_effects/016_brilliant_scientist_containment_effects.txt`, and `docs/events/016_brilliant_scientist/systems/containment.md`.

## Executive verdict

The eight actions are causally distinct and their completion routing is internally aligned: each starts the shared in-progress lock, applies its own upfront payment and temporary industrial burden, and resolves through the matching action constant after its timer. The resolver revalidates live causal state and reopens the board on an invalid route instead of mutating land or custody.

The surface is not closure-ready under the `chaos-redux-decisions-missions` hard cost rule. The physical deductions and negative stability effects are hidden in `complete_effect`, while the only native decision `cost` is Political Power and the availability tooltips spell out many additional resource requirements in literal prose. Depending on whether the two temporary industrial modifiers are counted as separate committed cost axes, the eight actions expose between 4 and 10 cost types; under the strict reading required by the skill, seven of eight exceed the four-type maximum and five exceed it even before timed burdens are counted.

The smallest meaningful remediation is cost consolidation, not a new system: retain the action-specific political or operational anchor, collapse secondary equipment families into one existing logistics/security family or a single route package, represent the two temporary industrial modifiers as one burden, and keep stability as a resolution consequence rather than an upfront payment where the contract permits. The parent should decide the exact balance values; this handoff does not change them.

## Severity-sorted findings

### P1 — Five to ten effective cost axes exceed the hard four-cost maximum

The skill defines a cost as anything the action consumes, removes, reduces, or commits as payment, including stability and temporary factory or production burden. Every action has a regular Political Power cost in its decision block, and the physical deductions and stability reductions are applied immediately in `complete_effect`.

The strict tally below counts Political Power, every negative stockpile/manpower/XP/Command Power/stability effect, and the two independently applied temporary industrial modifiers (`consumer_goods_factor` and `production_factory_efficiency_gain_factor`). The minimum tally excludes stability and the timed modifiers, so it is a useful lower bound rather than a compliance interpretation.

| Decision and source range | Direct upfront payment and hidden deductions | Timed industrial commitment | Minimum direct types | Strict types | Hard-limit result |
| --- | --- | --- | ---: | ---: | --- |
| `brilliant_scientist_release_kruger` (`:18-61`) | Political Power 25; stability -0.02 | Consumer goods +3%; factory efficiency -5% for 21 days | 1 | 4 | At the limit under strict counting; no consolidation required for count alone |
| `brilliant_scientist_exile_kruger` (`:70-115`) | Political Power 40; 10 convoys; 5 trains; 100 support equipment; stability -0.03 | Consumer goods +3%; factory efficiency -5% for 30 days | 4 | 7 | Over budget |
| `brilliant_scientist_arrest_kruger` (`:124-169`) | Political Power 55; 400 support equipment; 1,500 infantry equipment; 12,000 manpower; 15 Army Experience; stability -0.05 | Consumer goods +6%; factory efficiency -10% for 30 days | 5 | 8 | Over budget |
| `brilliant_scientist_shutdown_directorate` (`:178-223`) | Political Power 65; 300 support equipment; 150 motorized equipment; 10 trains; 1,000 fuel; stability -0.07 | Consumer goods +6%; factory efficiency -10% for 45 days | 5 | 8 | Over budget |
| `brilliant_scientist_ratify_sovereign_charter` (`:232-278`) | Political Power 75; 20 convoys; 15 trains; 250 motorized equipment; 300 support equipment; stability -0.04 | Consumer goods +10%; factory efficiency -10% for 45 days | 5 | 8 | Over budget |
| `brilliant_scientist_launch_military_seizure` (`:286-335`) | Political Power 85; 700 support equipment; 3,000 infantry equipment; 300 motorized equipment; 2,500 fuel; 25,000 manpower; 30 Army Experience; stability -0.10 | Consumer goods +10%; factory efficiency -15% for 21 days | 7 | 10 | Highest-risk over-budget action |
| `brilliant_scientist_request_foreign_containment` (`:344-396`) | Political Power 65; 25 convoys; 350 support equipment; 20 Command Power; stability -0.06 | Consumer goods +6%; factory efficiency -10% for 30 days | 4 | 7 | Over budget once timed burden and stability are counted |
| `brilliant_scientist_concede_institutional_authority` (`:398-448`) | Political Power 50; 200 support equipment; 10 trains; stability -0.08 | Consumer goods +10%; factory efficiency -10% for 30 days | 3 | 6 | Over budget under strict counting |

The source of all direct values is `common/script_constants/016_brilliant_scientist_containment_constants.txt:64-137`; the decision modifiers and negative stability effects are in `common/decisions/016_brilliant_scientist_containment_decisions.txt:36-45,87-99,140-153,194-207,249-262,303-319,361-373,415-426`.

If the project treats the two temporary modifiers as one combined industrial burden, subtract one from each strict total, but Exile, Arrest, Shutdown, Charter, Seizure, Foreign Containment, and Concession still exceed four once stability is treated as a reduction. If stability is deliberately moved out of the payment phase and treated as a result consequence, the lower bound is still over budget for Arrest, Shutdown, Charter, and Seizure. The source therefore needs actual consolidation rather than a relabelling exercise.

### P1 — Hidden deductions are not represented by an icon-first cost surface

The regular `cost` fields expose only Political Power, while equipment, fuel, manpower, Army Experience, Command Power, and stability are deducted in each `complete_effect` (`:93-98,146-152,200-206,255-261,309-318,367-372,421-425`). The availability strings in `localisation/english/016_brilliant_scientist_containment_l_english.yml:19-26` repeat many of these values as literal names such as `Support Equipment`, `Infantry Equipment`, `fuel`, and `Army Experience`, and they omit the timed industrial burden and most stability consequences.

This is not a raw nested trigger dump: each decision wraps one named scripted trigger in `custom_trigger_tooltip`. It is nevertheless a hidden-cost and text-density defect because a player sees one native Political Power cost while the physical payment is buried in a requirement tooltip. The supported remediation is to consolidate first, then expose no more than four icon-backed entries through an existing `custom_cost_trigger`/`custom_cost_text` surface or equivalent local pattern, keeping non-consumed conditions in a short requirements tooltip. If custom cost replaces regular `cost`, preserve AI Political Power planning with the documented `ai_hint_pp_cost` pattern.

### P2 — Cost gates and displayed quantities are potentially off by one

The matching availability triggers use strict `>` comparisons against gate values in `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt:42-106`, while the spend constants are the same amounts and the localisation says `ten`, `five`, `one hundred`, and so on. If the engine comparison is strict as documented, a country with exactly the displayed amount cannot start the decision and must hold one extra unit.

This is a source-level clarity concern rather than a confirmed runtime defect because the contract does not say whether the one-unit buffer is intentional. If exact displayed quantities are intended, align each gate with an inclusive check using the repository’s supported comparison form; otherwise document the deliberate reserve margin in the requirements text. Do not silently change balance in this audit.

### P2 — Cancellation is a sunk-payment path and needs an explicit contract decision

`complete_effect` runs immediately on selection, as documented by the offline Decision modding page, and applies the physical deductions before the timer begins (`common/decisions/016_brilliant_scientist_containment_decisions.txt:42-45,93-99,146-153,200-207,255-262,309-319,367-373,421-426`). Each `cancel_effect` only clears `brilliant_scientist_containment_action_in_progress` (`:54,108,162,216,271,328,382,435`); it does not refund Political Power, equipment, manpower, XP, fuel, Command Power, or stability.

The current event contract supports this as paid preparation: `docs/events/016_brilliant_scientist/systems/containment.md:13-18` says every action consumes Political Power and relevant physical resources, and invalid resolution reopens the board without changing land or custody. However, host loss, world-end, or a previously completed resolution can cancel a live timer with no outcome report, so the contract should explicitly state that terminal cancellation is non-refundable. If a refund is required instead, the eight actions need independent receipts and an idempotent refund helper; adding an ad hoc refund to the shared cancel effect would risk duplicate payment.

### P2 — Shared action flag is not itself a cancel predicate

All eight `cancel_trigger` blocks test current host, completed resolution, and `world_end`, but none tests `NOT = { has_country_flag = brilliant_scientist_containment_action_in_progress }` (`:47-53,101-107,155-161,209-215,264-270,321-327,375-381,428-434`). The start helper sets this flag at `common/scripted_effects/016_brilliant_scientist_containment_effects.txt:509-513`, while terminal and board-close helpers clear it at `:197-213,274-280` and through the terminal departure path at `:218-250`.

If a terminal reaction helper clears the shared flag before the native timed decision is removed and before one of the existing three cancel predicates becomes true, the source does not prove that the timer cannot continue to its resolver. The minimal remediation is either to add the missing-flag predicate to every action’s cancel trigger or to have the terminal helper remove the active decision itself, with the choice validated against native callback ordering. This is an ordering risk, not a confirmed duplicate resolution from the reviewed source.

### P3 — Category density is above the preferred visible-action limit

The single `brilliant_scientist_directorate_category` contains eight primary actions (`common/decisions/016_brilliant_scientist_containment_decisions.txt:17-448`). Response-flag gating hides Charter, Military Seizure, Foreign Containment, and Concession in most states, but the release, exile, arrest, and shutdown alternatives can coexist with one or more route actions. The category therefore can exceed the skill’s six-visible-primary-action guideline, and the repeated common visibility clauses keep several unavailable actions on the board as greyed rows during an active timer.

No action ID is demonstrably obsolete: route flags correctly gate the four clause-specific actions, Exile requires its saved recipient target, and the other alternatives are intentionally selectable policy responses. The minimal future treatment is phase filtering or a concise status presentation that preserves the active timer row; do not create a new decision family or category as part of this audit.

### P3 — Started-date metadata is not cleared in the audited surface

`brilliant_scientist_begin_containment_action` sets `brilliant_scientist_containment_action_started_date` at `common/scripted_effects/016_brilliant_scientist_containment_effects.txt:509-513`, but the shared close, invalidation, and decision cancel paths shown in `:197-213,274-280` and `common/decisions/016_brilliant_scientist_containment_decisions.txt:54,108,162,216,271,328,382,435` do not clear it. No read was found within the audited files, so this is inert metadata rather than a confirmed gameplay or UI defect; a broader repository search was intentionally outside this bounded review. Clear it in one shared lifecycle helper only if another consumer is intended to use it.

## Action-by-action requirements versus costs

The following conditions are requirements because they gate whether the action can be selected; they do not count as spendable costs unless a resource is also deducted. The board-open trigger at `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt:8-18` contributes current host, legal transition, unresolved board, no active action, no world-end, and an open deadline/request state.

| Action | Non-consumed requirements | Spendable costs and timed commitments |
| --- | --- | --- |
| Release Doctor Kruger | Low coercive risk, no military-seizure or foreign-containment response, current host, unresolved open board | 25 Political Power, -0.02 stability, light consumer-goods burden, -5% factory-efficiency burden for 21 days |
| Arrange Exile | Moderate coercive risk, valid persisted recipient, transfer recipient remains valid, current host and open board | 40 Political Power, 10 convoys, 5 trains, 100 support equipment, -0.03 stability, light two-axis industrial burden for 30 days |
| Arrest Doctor Kruger | Current host and open board; live resource gates are payment availability, not route requirements | 55 Political Power, 400 support equipment, 1,500 infantry equipment, 12,000 manpower, 15 Army Experience, -0.05 stability, medium two-axis industrial burden for 30 days |
| Shut Down the Directorate | Current host and open board; live resource gates are payment availability, not route requirements | 65 Political Power, 300 support equipment, 150 motorized equipment, 10 trains, 1,000 fuel, -0.07 stability, medium two-axis industrial burden for 45 days |
| Ratify the Sovereign Charter | Charter response flag, charter territory can still form, current host and open board | 75 Political Power, 20 convoys, 15 trains, 250 motorized equipment, 300 support equipment, -0.04 stability, heavy consumer-goods plus medium factory-efficiency burden for 45 days |
| Launch the Military Seizure | Military-seizure response flag, current host and open board; coercive score and formation checks are revalidated at resolution | 85 Political Power, 700 support equipment, 3,000 infantry equipment, 300 motorized equipment, 2,500 fuel, 25,000 manpower, 30 Army Experience, -0.10 stability, heavy consumer-goods plus heavy factory-efficiency burden for 21 days |
| Request Allied Containment | Foreign-containment response flag, faction membership, current host and open board | 65 Political Power, 25 convoys, 350 support equipment, 20 Command Power, -0.06 stability, medium two-axis industrial burden for 30 days |
| Concede Institutional Authority | Concession response flag, institutional capture already proven, current host and open board | 50 Political Power, 200 support equipment, 10 trains, -0.08 stability, heavy consumer-goods plus medium factory-efficiency burden for 30 days |

Positive `add_war_support` on Military Seizure at `:317-318` is a consequence, not a cost. The formation, recipient, faction, route, and causal score checks are requirements; they must remain separate from the cost string.

## Minimal cost-consolidation proposal

The proposal below preserves each action’s identity and causal role while keeping the player-facing payment surface within four types. It is intentionally a design handoff, not an implementation or balance decision.

| Action | Suggested payment shape at or below four types |
| --- | --- |
| Release | Keep Political Power and one consolidated temporary industrial burden; retain the stability change as a resolution risk/consequence if it is not meant to be an upfront payment. |
| Exile | Keep Political Power, one transport package represented by convoys, and support equipment; fold train logistics into the transport package or a non-consumed transfer requirement, then use one industrial burden. |
| Arrest | Keep Political Power, support equipment, and manpower; fold infantry equipment and Army Experience into the security package or the live coercive resolution score, then use one industrial burden. |
| Shutdown | Keep Political Power, support equipment, and fuel; fold truck/train logistics into the support package or a route requirement, then use one industrial burden. |
| Charter | Keep Political Power, one transport package represented by convoys, and support equipment; fold train/truck logistics into that package, then use one industrial burden. |
| Military Seizure | Keep Political Power, a military support package, and manpower; fold infantry/truck/XP/fuel preparation into the package or live coercive score, then use one industrial burden. If fuel is the causal anchor, retain fuel instead of support and consolidate the other physical families around it. |
| Foreign Containment | Keep Political Power, Command Power, and one foreign-logistics package combining convoy/support burden; use one industrial burden. Faction membership remains a requirement. |
| Concession | Keep Political Power and support equipment; fold train logistics into the institutional package and use one industrial burden. |

If stability is contractually required as an upfront cost, one of the direct families must be merged or removed for each affected action; it cannot be hidden as a consequence while still being charged in `complete_effect`. If the temporary modifiers remain two separate commitments, the direct payment shape must be reduced further. Any custom-cost UI must include no more than four icon-backed entries and must not move a fifth cost into a tooltip.

## Completion, cancellation, and resolver alignment

All eight decisions use `days_remove` values from the centralized duration block at `common/script_constants/016_brilliant_scientist_containment_constants.txt:46-62`: 21 days for Release and Military Seizure, 30 days for Exile, Arrest, Foreign Containment, and Concession, and 45 days for Shutdown and Charter. Each `remove_effect` sets the matching `brilliant_scientist_containment_action.*` value and calls `brilliant_scientist_resolve_containment_action` (`common/decisions/016_brilliant_scientist_containment_decisions.txt:55-60,109-114,163-168,217-222,272-277,329-334,383-388,436-441`).

The shared resolver stores the selected action and date, routes Release, Exile, Charter, and Concession to their dedicated outcomes, and routes Arrest, Shutdown, Military Seizure, and Foreign Containment through the coercive resolver at `common/scripted_effects/016_brilliant_scientist_containment_effects.txt:509-554`. Invalid Exile, Charter, formation, and transfer states reopen the board without land or custody mutation, matching `docs/events/016_brilliant_scientist/systems/containment.md:15-18` and the resolver branches at `:292-311,439-459`.

The cancellation path is intentionally different from invalid completion: `cancel_trigger` ends the timed decision without `remove_effect`, and `cancel_effect` only clears the shared action flag. The offline Decision modding page confirms that `cancel_effect` is the place to reverse selection-time effects; this source does not reverse them. Parent should either preserve the documented sunk-preparation contract or add receipts before promising refunds.

## Tooltip, visibility, and cognitive-load notes

No raw nested scripted-trigger block is emitted to the player. The available tooltips are named and concise in structure, but `localisation/english/016_brilliant_scientist_containment_l_english.yml:19-26` contains literal multi-resource lists, with Military Seizure listing six physical resources and Charter listing four. These lists are cost rows disguised as requirements and have no matching texticons.

The eight visible action rows are more than the preferred six-action category limit in a fully unlocked board. The repeated `visible` clauses at `:20-29,72-80,126-133,180-187,234-242,288-296,346-354,400-408` overlap the `brilliant_scientist_sovereignty_board_is_open` checks in the availability triggers; this is maintenance duplication, not an obsolete route. The four response-specific rows are correctly hidden unless their recorded clause exists, and Exile is correctly hidden without its persisted recipient.

The hidden causal score components are intentionally not displayed, which is consistent with the containment document’s statement at `docs/events/016_brilliant_scientist/systems/containment.md:33,35-49`. The player-facing values that are displayed or should be displayed are Political Power, physical equipment, manpower, XP, fuel, Command Power, stability, and the temporary industrial burden; each has a direct consequence, but several are currently omitted from the cost presentation.

## AI validity and route notes

Every action has an `ai_will_do` block in its decision range. AI base values and factors are centralized at `common/script_constants/016_brilliant_scientist_containment_constants.txt:229-243`; no probability or balance certification is claimed because the parent’s weighted audit is running separately.

Release, Exile, Arrest, Shutdown, and the four clause-specific actions all use the board-open requirements before resource gates. Exile additionally requires a saved valid recipient; Charter additionally requires charter formation viability; Foreign Containment requires faction membership; Concession requires proven institutional capture. No invalid target is introduced by the eight country-scoped decisions.

## Mission quality note

None of the eight containment actions is a mission; all eight are timed decisions with `days_remove`. The separate sovereignty deadline mission and its timeout behavior are outside this eight-action audit. The action timers have explicit owners, category, duration, success resolver, cancellation conditions, and duplicate lock through `brilliant_scientist_containment_action_in_progress`; the only remaining source-level concern is the shared-flag cancellation ordering described above.

## References and evidence limits

The required offline Paradox wiki core pages were consulted, with Decision modding used directly for `available`, regular/custom costs, immediate `complete_effect`, timed `remove_effect`, and `cancel_effect` semantics. The required vanilla script-concept and script-constant documentation were consulted for `constant:` field support, and vanilla decision precedents were used for timer and modifier structure.

No MCP or live-game evidence was collected by design, so this handoff cannot prove exact engine ordering for cancellation versus terminal callbacks, inclusive versus strict equipment-gate semantics, dynamic cost localisation rendering, or the real-time opportunity cost of the temporary industrial modifiers. The handoff is an actionable source audit and cost-consolidation proposal, not Event016 completion certification.

Files changed by this subagent: only this handoff document.

Simplifications and omissions: no gameplay or balance simplification was applied. Cost consolidation, cost-localisation wiring, the inclusive-gate decision, the shared-flag cancellation predicate, and any category phasing remain parent-owned follow-up work.
