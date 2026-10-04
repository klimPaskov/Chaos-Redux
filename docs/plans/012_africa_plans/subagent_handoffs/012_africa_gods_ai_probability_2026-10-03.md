# Event 012 Gods AI probability continuation audit

Audit date: 2026-10-03. Workspace: `mod_chaos_redux_ea3b2d67c2c0`. Disposition: source review completed, current MCP probability analysis unresolved.

This bounded read-only audit covers `decision_ai_will_do` for the ten named participant response decisions in `common\decisions\012_africa_gods_decisions.txt`. No gameplay, weight, spreadsheet, shared documentation, or Git files were changed. The parent owns implementation and all balance targets.

## Current source snapshot

| Source | Identifiers or role | Local SHA-256 |
| --- | --- | --- |
| `common\decisions\012_africa_gods_decisions.txt` | The ten response decisions and their visibility, availability, and `ai_will_do` blocks | `230F9F22136CDA7A6625641EF45E4D14666B846457E2C466656824D2B0D3F8B6` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | Current contract, capacity, partial affordability, substitute slots, extension, and defiance gates | `B70B438CF6AD01E34690AD67F97AD3630940BEE650D5962A1F84244796E747ED` |
| `common\scripted_effects\012_africa_gods_effects.txt` | Demand preparation, negotiation, resolution, and response effects | `ED5855EAFCCB6655A54B8ACECB56049A6182EC1ED1E824A75D6C62599C1B97A5` |
| `common\scripted_effects\012_africa_gods_equipment_effects.txt` | Current armoured quote and transfer helpers used by capacity checks | `61C7189BDEE1EC84F5C5315B4D5D18F0F97C978CD6F53387D3016E1C1B06B1BA` |
| `common\scripted_triggers\012_africa_gods_equipment_triggers.txt` | Per-chassis reserve and capacity checks | `8113C7F41E3FE55BE1BF191DE7108FA6698CB7CECEE8BD737F4D5691F85EB3AE` |

These are local file hashes, not MCP source revisions. The shared workspace moved during review. The final trigger and main-effect hashes above are the latest bytes read for this handoff. The decision file hash stayed the same across the checks.

## MCP route and retained evidence

I inspected the live tool declarations for `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, and `hoi4.probability_render`. The live inspect schema exposed `decision_ai_will_do`, `source`, `candidatePool`, `refresh`, and `workspaceId`. Its source selector is typed as unknown in the declaration. Input validation specified that the source must be an object containing an identifier, path, inline Clausewitz source, or virtual patch.

The first inspect call without a source returned `An adapter requires a source` and `provide a source alone to discover compatible adapters`. A string source was rejected as the wrong type. After using the source object `{path: "common/decisions/012_africa_gods_decisions.txt"}`, the source-bound inspect with the supplied workspace ID and `refresh = true` remained pending for more than 50 seconds. One identical retry remained pending for its 20-second bounded wait. Both calls were stopped at the wait boundary. This is a transport stall, not a confirmed service-health diagnosis. No current inspect artifact, MCP source revision, analysis ID, candidate-pool hash, scenario hash, blocker payload, or continuation URI was returned.

The latest artifact manifest's `toolVersion = 3.6.0` is reported in the task context. A fresh manifest, connected service health/version, and client task negotiation were not confirmed. No job, helper-expansion, native task, or undocumented route was used.

Prior probability artifacts are retained only as stale-source context:

| Prior inspect | Revision and source hash | Artifact |
| --- | --- | --- |
| 2026-09-25 decision inventory, 36 candidates and 15 file-wide required inputs | Revision `cb808894b33a51fb05d6cf7d5d6cf37359ebd45403586b7a505779e7a14dae25`, source hash `94b21c86205c16af5243748d08e52bdf9584a0069fab23c4ad2bb02e3746f74b` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b3ff62526399ee9d929a528ec02adf8a880f6ffcd4d0dc9e4e1049e00847d89/249f9333cf6cc219fdfe1290f6d4351b7043cf71fd880a1870ca91b1b3404d26/probability-inspect-94b21c86205c.json` |
| 2026-09-26 refreshed decision inventory, 36 candidates and 15 file-wide required inputs | Revision `8b8752b7c0dcc5128addc5410f28ebde4e84b45bb2d36bd62a75ba45de0bf497`, source hash `713a8151187b0c43bd119a69a7cb36f20524e39932d0815c4059a9f9202ab364` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/561edaa3efd8861da97f5c03f8644efc5f76cef4fbccff1e13430b937b1aba3d/75ed9786078df7957ccde1d74274dfa389a0e7253a9e5c1515459fb084afbe83/probability-inspect-713a8151187b.json` |

The September response evaluations returned `INTERNAL_ERROR` and produced no response analysis ID or rendered response view. The historical response scenario set is `012-GODS-BASELINE-RESPONSES-2026-09-25`. Its scenario IDs are preserved below, but neither old inventory applies to the current source hash. The post-change handoff `012_africa_gods_ai_probability_compare_2026-09-25.md` also has no successful response comparison artifact.

## Candidate pool and named scenarios

The ten requested identifiers are not one normalized ten-way race. With an active demand and negotiation closed, the direct response phase contains `gods_of_africa_comply_demand`, `gods_of_africa_partial_compliance`, `gods_of_africa_negotiate_demand`, and `gods_of_africa_refuse_demand`. `gods_of_africa_permanent_defiance` can also be visible in that phase, and its availability allows either a current demand or no active demand. While negotiation is open, the direct choices are hidden. That phase can expose `gods_of_africa_substitute_demand`, the three slot decisions, and `gods_of_africa_return_to_demand`. Defiance is hidden during negotiation.

| Scenario ID | Candidate pool completeness | Actor, state, and external factors | Classification |
| --- | --- | --- | --- |
| `RESP-COOPERATIVE-AFFORDABLE` | Ten requested IDs are known, but no phase-specific evaluator pool was accepted or returned. | No actor tag, host binding, demand state, flags, variables, stock, or external AI factors were bound. | Unresolved |
| `RESP-COOPERATIVE-HARDSHIP` | Same phase split. The ten IDs do not form one selection race. | The scenario name alone does not bind inability to pay, partial capacity, host identity, or other state. | Unresolved |
| `RESP-GAMBLER-WEAK-AFRICA` | Same phase split. Current host and participant eligibility remain unexpanded by MCP. | No supported fixture binds the named strength or current demand state. | Unresolved |
| `RESP-OCCUPIER` | Same phase split. No complete concurrent decision category pool was inspected. | No occupier tag, host target, war state, demand state, or strategy factor was bound. | Unresolved |
| `RESP-LOYAL-ALLY-EMERGENCY` | Same phase split. Target and phase gates remain conditional. | No alliance, emergency, actor, host, demand, or external factor fixture was bound. | Unresolved |
| `RESP-ABUSIVE-AFRICA` | Same phase split. No response analysis or current pool hash exists. | No offender flag, Wrath value, host binding, demand phase, or external factor fixture was bound. | Unresolved |

`africa_host` is a dynamic event-target name in the source. It is not an observed country tag and was not used as one. The prior baseline's empty fixture with `actor = "africa_host"`, empty state, flags, and scopes does not bind Clausewitz variables, country targets, or compound triggers. The scenario matrix named in that baseline is explicitly superseded, so its labels do not supply renewed design approval or current fixture values.

## Source score formulas and conditional bounds

The formulas below are direct source traces with conditional arithmetic. They are classified as score-only, not analyzer traces. They are not click probabilities. The offline AI reference describes `ai_will_do` as a score race that samples values up to each score and selects the highest result. It distinguishes `ai_chance`, which uses probability-proportional sampling. No normalized share or exact runtime selection chance is inferred here.

| Decision | Phase | Source score when its own availability gate passes |
| --- | --- | --- |
| `gods_of_africa_comply_demand` | Direct response | `100` when the current demand is payable. The factor is `0` otherwise, and the availability gate also requires payment capacity. |
| `gods_of_africa_partial_compliance` | Direct response | `15 × 0.25 = 3.75` when the full demand is payable, or `15 × 1.5 = 22.5` otherwise. Partial amount, remaining balance, cooldown, and partial capacity must also pass. |
| `gods_of_africa_negotiate_demand` | Direct response | `20 × 2` when the full demand is not payable, then `× 0.5` when Wrath is above `gods_of_africa_wrath.vengeful`. Conditional source bounds are 10 to 40. |
| `gods_of_africa_substitute_demand` | Negotiation | `10 × 2` when the original demand is not payable, then `× 0.5` above the vengeful Wrath threshold. Conditional source bounds are 5 to 20. |
| `gods_of_africa_substitute_demand_slot_1` | Negotiation | Base 10, multiplied by 2 when the original demand is not payable, for 10 or 20. |
| `gods_of_africa_substitute_demand_slot_2` | Negotiation | Base 9, multiplied by 2 when the original demand is not payable, for 9 or 18. |
| `gods_of_africa_substitute_demand_slot_3` | Negotiation | Base 8, multiplied by 2 when the original demand is not payable, for 8 or 16. |
| `gods_of_africa_return_to_demand` | Negotiation | Flat base 5 when the current contract is valid. |
| `gods_of_africa_refuse_demand` | Direct response | `5 × 3` when the full demand is not payable, or `5 × 0.5 = 2.5` when it is payable. |
| `gods_of_africa_permanent_defiance` | Direct or no-demand state | `5 × 4` for an offender, `× 3` at or above `gods_of_africa_wrath.hostile`, `× 2` during an active demand, and `× 0` while reconciliation is pending. |

The formula permits a source-only rank reversal. With offender status, hostile-or-higher Wrath, an active demand, and no pending reconciliation, permanent defiance reaches `5 × 4 × 3 × 2 = 120`, above comply's raw 100. The decision comment at lines 406-407 says defiance remains rarer than ordinary responses. The unmodified source scores do not establish that claim in this state. This is a conditional source comparison only. No full pool, strategy modifiers, or analyzer ranking confirms that defiance wins in a campaign.

There is also a negotiation-pool duplication risk. `gods_of_africa_substitute_demand` dispatches to the first valid slot in order, so it produces the same slot-1 outcome as `gods_of_africa_substitute_demand_slot_1` whenever slot 1 is valid. Their bases are both 10. When Wrath is below the vengeful threshold their raw source scores match under the same payability state. Slots 2 and 3 have lower bases. This creates a possible repeated route to slot 1 and a possible starvation pressure on later slots, but no analyzer result establishes actual selection frequency.

No source-only positive weight was found on a clearly impossible candidate in these ten definitions. Comply is zero and unavailable when the full demand cannot be paid. Partial payment and substitute slots require their live helper gates. Defiance is gated against an already-defiant participant, pending reconciliation, invalid host generation, final settlement, and an open negotiation. These are source checks only and do not prove that MCP can resolve the compound gates.

All response declarations use `fire_only_once = no`, while contract flags, one-use extension state, partial-payment cooldown, slot validity, and resolution cleanup change future availability. No repeated loop, starvation, or exploit was demonstrated. Repetition and broader snowball behavior remain unresolved without a supported state sequence. No timing distribution applies to this `ai_will_do` score pass.

## Exact binding needed for a useful retry

The current source requires at least a participant country scope, a real host country bound through `event_target:africa_host`, current generation and active-demand state, and the demand family, amount, remaining balance, deadline, and current day. The contract gate also checks that the host is active and that the participant is not at war with it.

The AI modifiers and availability helpers additionally need the relevant flags and variables for negotiation, defiance, offender history, reconciliation, extension use, Wrath, the partial amount and due day, and each frozen substitute slot. Capacity must bind to the actual demand family and current stock. In the final source snapshot, family `mobile_artillery` still checks `motorized_equipment`, while armour delegates to `gods_of_africa_armor_capacity_is_sufficient`. The current `common` source scan found no typed mobile or artillery demand identifiers. The parent's queued mobile/artillery implementation can change these eligibility results without changing any `ai_will_do` base, so the current score pass must be repeated after that implementation lands.

The previous file-wide inspect listed `FROM`, `any_controlled_state`, `check_variable`, `event_target:africa_host`, `exists`, `has_capitulated`, `has_equipment`, `has_fuel`, `has_manpower`, `has_political_power`, `has_variable`, `has_war`, `has_war_with`, `hidden_trigger`, and `meta_trigger`. That list is stale and spans all 36 decisions in the file. It is not a proven required-input list for these ten participant actions. The current inspect returned no input list. The adapter must state which typed country scopes, target bindings, variable bindings, equipment-capacity tests, and compound scripted triggers it can evaluate before fixtures are assembled. Flat state maps and invented scope oracles cannot prove coverage.

The next valid pass should use separate source-supported pools for the direct response phase, negotiation phase, and defiance without an active demand. It should bind each named scenario to an explicitly hypothetical participant and host fixture only if the adapter supports those inputs, then report pool completeness and unresolved external factors for each scenario. The six scenario IDs above should be retained for a matching future compare if a successful baseline analysis returns an analysis ID. None was returned here.

## Recommended owner actions

In `common\decisions\012_africa_gods_decisions.txt`, reconcile the comment that permanent defiance remains rarer with the conditional raw score of 120 against comply's 100. Decide the intended ordering before changing a modifier. This audit selects no revised value.

For `gods_of_africa_substitute_demand` in `common\decisions\012_africa_gods_decisions.txt` and its first-valid-slot dispatch in `common\scripted_effects\012_africa_gods_effects.txt`, decide whether the generic action should remain AI-eligible alongside `gods_of_africa_substitute_demand_slot_1`. If both are retained, give the generic action a distinct AI outcome or otherwise prevent the identical slot-1 outcome from receiving two candidate entries. No patch was applied.

After the parent lands the accepted mobile/artillery work, bind the chosen subtype through `gods_of_africa_participant_has_capacity_for_family` and the matching full, partial, and substitute gates in `common\scripted_triggers\012_africa_gods_triggers.txt`. Refresh the probability baseline after that eligibility change. Any later weight edit still requires a comparison on the same supported scenario fixtures.

## References and route coverage

The offline wiki and installed vanilla source were read locally because the MCP reference calls did not return. These SHA-256 values identify the local files used.

| Reference | Relevant section | Local SHA-256 |
| --- | --- | --- |
| `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md` | Lines 26-36, score races, modifier application, and the distinction from `ai_chance` | `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818` |
| `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | Lines 357-372, decision `ai_will_do` as an MTTH-style block | `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md` | Lines 1-35, decision scope and visible/available evaluation cadence. This file contains no `ai_will_do` weight semantics. | `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\ai_strategy\_documentation.md` | Lines 603-610, technology `research_weight_factor`. This is not a decision-weight definition. | `70F5D755AE7ED4060E49CC64A393D1A0DC5611B3ACC8ABC6DFB4538781C915A1` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\GER.txt` | Lines 250-279, `GER_seize_gold_reserves` base 15 with zero and escalating variable factors, a vanilla conditional decision-score precedent | `6E109AF4C268DCD4E67AEC2D70EF7ABD479D64B06EBB2FC439A9777591C5C3C8` |

`hoi4.reference_context` was attempted for the decision surface and remained pending through a 15-second bounded wait. `hoi4.reference_search` and `hoi4.source_lookup` were attempted in a bounded batch that remained pending for about one minute before cancellation. No reference IDs, revisions, artifact URIs, `nextLine`, or continuation URIs were returned, so `hoi4.reference_read` could not be called against a revision. The exact local wiki and installed files above were read instead. No range-read continuation remains available.

The decision audit handoffs read are in `docs\plans\012_africa_plans\subagent_handoffs\` and include `012_africa_gods_ai_probability_baseline_2026-09-25.md`, `012_africa_gods_ai_probability_compare_2026-09-25.md`, `012_africa_gods_current_weighted_logic_audit_2026-09-26.md`, `012_africa_gods_armored_tribute_2026-10-03.md`, `012_africa_gods_armor_architecture_audit_2026-10-03.md`, `012_africa_gods_mobile_artillery_design_2026-10-03.md`, `012_africa_gods_requirement_text_2026-10-03.md`, and `012_africa_gods_timer_and_text_2026-10-03.md`. The parent handoffs report no AI weight changes in the timer/text or armour tranches. The armour tranche does change affordability through the live capacity helper, so eligibility can change while raw AI bases stay constant.

## Skipped analyses and status

`hoi4.probability_evaluate` was not called because the fresh inspect never returned its current required-input contract, and no supported complete scenario fixture or phase-specific candidate pool was available. `hoi4.probability_sweep` was skipped because the current adapter's accepted variable paths and range syntax were not returned. No simulation was run because no uncertain-input distribution was declared. No sequence analysis was run because this is not a declared custom pool with cadence and transitions. `hoi4.probability_compare` was not run because this read-only continuation changed no AI weight and there is no current matched baseline analysis. `hoi4.probability_render` could not render a current ranking or unresolved view because no analysis ID exists. Event inspect and render were outside this decision-weight surface. No event-option, MTTH, focus, research, mission, strategy-factor, or custom-pool conclusion is made.

Completed work: current source formulas, availability dependencies, phase split, stale prior artifacts, local reference sections, and source-only rank risks are recorded above.

Blocked work: current MCP score evaluation, scenario ranking, sensitivity, external-factor proof, normalized selection results, current rendered evidence, and comparison remain unresolved due the bounded transport stall and unsupported scenario bindings.

No balance target was selected and no numeric weight was recommended. The two source risks requiring owner intent are the defiance score ceiling versus the comment that it remains rare, and the generic substitute route duplicating slot 1. Any later weight patch requires a fresh baseline, an owner-applied change, and a matching `hoi4.probability_compare` on the same supported scenario fixtures. No implementation simplification was made by this auditor. The broader Event 012 goal remains with the parent and is not declared complete here.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-decisions-missions`. No skills were created or updated.
