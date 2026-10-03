# Event025 exact aircraft overlap owner contract

Date: 2026-10-03.
Mode: plan-only continuation by `chaosx_scripted_system_architect`.
Owned output: this file only.
Disposition: accepted arbitration requirements traced, proposed aviation owner extension unresolved pending parent acceptance, MCP evidence blocked.
The parent reports that prior agent `agent01a101a9-ef69-7971-82fa-86df727d5443` was `not_found` and produced no handoff.
The parent owns destruction and transfer callers and tests independently of this sidecar.
No gameplay, index, workbook, source snapshot, or runtime file was edited, no HOI4 process was launched, and no commit was made because the explicit assignment forbids index changes.

## Recommendation and acceptance boundary

Implement exact identity and successful-delivery receipts in the existing Event016 owner boundary and shared Event025/Event036 ledger.
For a real fresh-campaign aircraft collision, propose one narrowly scoped neutral aviation base and its aircraft refinement under that owner.
Use the existing jet aircraft consumers, retain the seven current families, and keep all reward selection inside the owner API.
Do not relabel Portal or Temporal as aviation or propulsion, reuse native project-completion callbacks as neutral grants, or give Event025 a copied technology list.

The parent's current assignment explicitly treats specs `006_outcomes_rewards_and_aftermath.md` and `014_acceptance_criteria.md` as accepted inputs.
Their accepted contract covers base-first Event025 rewards, eligible upgrades, full-pool Integration, country-specific exact overlap, both event orders, neutral provenance, and a real converted reward for achievement 14.
That acceptance does not establish approval for a new aircraft family, new hidden technologies, aircraft modifier values, wider vanilla grants, or changed Event036 stockpile behavior.
The owner extension described below is a concrete proposal for the parent to resolve within the authorized scope.
It has not been promoted into a spec or implemented.

Correcting the existing exclusion alone restores access to unrelated missing bases, but cannot establish a genuine aircraft collision or make the cross-event achievement truthful.
If the parent does not accept a real owner extension, the exact-overlap achievement route remains incomplete.
Broad field matching is not an acceptable substitute.

## What the current owners actually expose

Paths in this section are relative to `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`.

| Surface | Exact source evidence | Consequence |
| --- | --- | --- |
| Portal base | `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:38-45`, `common/technologies/016_brilliant_scientist_project_technologies.txt:37-48` | Grants `brilliant_scientist_portal_warfare_tech`, enables `teleportation_equipment_1` and `portal_raider`. |
| Portal upgrade | Owner API `:375-387`, `common/technologies/016_brilliant_scientist_project_force_technologies.txt:36-46` | Grants `brilliant_scientist_portal_warfare_weaponization_tech` and strengthens the same land unit. |
| Temporal base | Owner API `:85-90`, project technologies `:172-182` | Grants `brilliant_scientist_temporal_guard_tech`, enables `temporal_guard_equipment_1` and `temporal_guard`. |
| Temporal upgrade | Owner API `:448-457`, force technologies `:121-132` | Grants `brilliant_scientist_temporal_guard_weaponization_tech` and strengthens the same land unit. |
| Actual consumers | `common/units/016_brilliant_scientist_project_forces.txt:112-140`, `:322-357` | Both are infantry land consumers with equipment needs, not aircraft. |
| External random pool | Owner API `:523-583`, `common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt:26-56` | Seven base families and eleven upgrades, with no aviation selector. |
| False field attribution | Owner API `:695-696`, `:760-761` | Portal is assigned field `aircraft`, Temporal field `propulsion`. These assignments do not establish matching IDs. |
| Whole-base exclusion | Owner API `:679-687` | `chaosx_external_alien_recovery_exclude_overlap` bypasses the entire base helper. The per-request `allow_base` is not read. |
| Event036 legacy output | `events/036_alien_spacecraft.txt:46-69` | Resolver runs in `immediate`, then option A grants `jet_fighter1`, `jet_fighter2`, and 200 `jet_fighter_equipment_2`. |
| Existing neutral Rocketry | `common/scripted_effects/016_conventional_technology_api_effects.txt:58-59`, `:88-90`, `:199-206` and paired Markdown | A real conventional package exists, but grants durable package flags and existing stage modifiers, not the Event036 jet IDs. It is outside the seven-family random pool. |
| Existing native aviation seams | `common/special_projects/projects/air_projects.txt:840-846`, `common/scripted_effects/016_mengele_native_prototype_effects.txt:249-254`, `016_mengele_project_stage_effects.txt:1411-1415` | Jet and axial-jet completion callbacks settle native Event016 project state. They cannot be called to manufacture a neutral recovery reward. |

The existing aviation-related native content and neutral Rocketry package are useful precedents, but neither is an existing neutral aircraft overlap family.
No exact shared technology or equipment ID between the current seven-family API rewards and Event036's legacy jets was found.
This conclusion is bounded to the inspected owner files and targeted Event016 aviation searches, not a completed MCP source-lookup closure.

The shared dynamic library was checked before proposing helpers.
`common/scripted_effects/chaosx_dynamic_effects.txt:481-529` and its paired Markdown document `union_compatible_researched_technologies_from_donor`, which copies a donor's researched technology union rather than selecting a receipt-bound alien reward.
It is unsuitable here because it would import unrelated knowledge and cannot prove the reward source or exact conversion.
The dynamic-helper documentation already points to the custom and conventional owner APIs at `chaosx_dynamic_effects.md:358-359`.
Extend those owner surfaces and their documentation rather than introduce a central router or wrapper skill.

## Proposed minimal real owner extension

The following identifiers are proposals, not existing or accepted definitions.
A search of current `common/` and `events/` found no definitions for the two proposed technology names.
The parent must still inspect the effective vanilla/mod source set before registering them.

| Owner vocabulary | Proposed exact IDs and runtime outputs | Boundary |
| --- | --- | --- |
| `chaosx_custom_technology_family.aviation` | New grant-only `alien_aviation_systems_tech`, owner effect grants the existing `jet_fighter1` and `jet_fighter2` knowledge, whose consumers are `jet_fighter_equipment_1` and `jet_fighter_equipment_2` | Append a new selector without renumbering the existing seven. The hidden bridge represents a real owner-managed operational aircraft package, not a field-label alias. |
| `chaosx_custom_technology_upgrade.aviation_refinement` | New `alien_aviation_refinement_tech`, dependency on `alien_aviation_systems_tech`, real static aircraft refinement on the installed `jet_fighter` consumer | Append a new upgrade selector without renumbering the existing eleven. The parent chooses supported aircraft stat fields and their values after reference and balance review. A marker-only upgrade fails acceptance. |
| Exact overlap identity | `alien_aviation_systems_tech` plus canonical payload IDs `jet_fighter1`, `jet_fighter2`, `jet_fighter_equipment_1`, `jet_fighter_equipment_2` | Both sources dispatch through the same operational owner branch. Persist its selector and applied source receipt, then resolve canonical IDs through the owner map. |
| Propulsion identity | None proven for the current external pool and Event036 output | Keep the existing code reserved if needed, but no live propulsion collision is certified by Temporal or by the presence of jet aircraft. |

This deliberately proposes an exception to the current API's documented prohibition on vanilla technology grants, confined to the accepted aviation payload if the parent accepts the extension.
Both the owner file header and paired Markdown must state that exception explicitly.
The other seven family grants retain their existing semantics.
Do not duplicate vanilla aircraft definitions, equipment unlock lists, native special-project definitions, or native completion hooks.
The owner can grant the established jet technology IDs directly rather than add a second `enable_equipments` declaration for the same equipment.

The installed vanilla precedent is `common/technologies/air_techs.txt:535-618`, where `jet_fighter1` and `jet_fighter2` enable the corresponding concrete jet equipment.
`common/units/air.txt:157-166` defines `jet_fighter` as an active fighter consumer of `jet_fighter_equipment`.
`common/units/equipment/x_plane_airframes.txt:131-138` defines that duplicate archetype and `:359-386` defines `jet_fighter_equipment_2`.
Its designer and DLC behavior must be checked before treating direct grants as complete aircraft production access.
Those source definitions do not prove actual runtime production.

An existing higher aircraft tier also exists: `supersonic_fighter1` and `supersonic_fighter_equipment_1` at vanilla `air_techs.txt:625-655` and `x_plane_airframes.txt:389` onward.
Its technology has a `Gotterdammerung` branch gate and native special-project prerequisite.
It is not the default recommendation for a universal replacement reward because its supported configuration behavior is unverified.
Selecting it would be a separate parent-approved output contract, not an implicit fallback or permission to complete the native project.

The extension grants learned technology and production/refinement access only.
It adds no air wings, divisions, free formations, provider-neutral land rows, project facilities, or unrelated equipment.
The existing 200-aircraft Event036 stockpile is separate legacy behavior.
Its preservation, suppression on exact conversion, and one-shot delivery remain Event036-owner decisions.
The Event025 owner must never reproduce that stockpile grant.

## Helper map and dispatch seam

All helpers below run in the receiving country's scope.
Callers invoke them with `= yes`, using documented selector/request variables rather than named-argument scripted-effect syntax.
Existing names should be extended where possible.

| Helper | Inputs and defaults | Outputs | Side effects and direct callers |
| --- | --- | --- | --- |
| Existing `chaosx_grant_custom_operational_technology` | Family selector and optional validated source. Proposed aviation selector maps to exact owner IDs. Invalid selector fails closed. | Existing applied output plus proposed `knowledge_changed` output distinguishing new knowledge from an idempotent repair. | Owner grants operational knowledge, records provenance, reconciles consumers. Event025 selection and Event036 base dispatch use it. |
| Existing `chaosx_grant_custom_technology_upgrade` | Upgrade selector and source. Aviation refinement requires its real operational dependency. | Existing applied output plus `knowledge_changed`. | Owner installs the selected real refinement and records base/dependency and upgrade provenance distinctly. The converted delivery is the upgrade, not its dependency repair. |
| Proposed `chaosx_custom_technology_has_exact_recovery_overlap` trigger | Requested family/payload identity, other event's delivered country receipt, and actual owned canonical output. No receipt means false. | Boolean only. | Read-only owner identity query used by the shared ledger and owner candidate filter. It never treats display-field equality or a world counter as overlap. |
| Existing `chaosx_grant_random_custom_operational_technology` | Owner candidate rules plus exact excluded family identities from the request. Ordinary callers default to no exclusion. | Applied marker and exact selected family. | Weights and grants only eligible missing bases. Exclude individual exact matches and keep unrelated bases eligible. |
| Existing `chaosx_grant_external_alien_recovery_reward` | Source `25` or `36`, explicit base policy, exact overlap identities, optional preferred conversion family. Defaults follow the documented ordinary base-first request. | Applied, knowledge changed, actual result/tier/family/upgrade, matched identity, conversion applied, source. | Owns selection, neutral grant dispatch, per-source consumption, and Integration. It resets every result before selection and commits consumption only after a real accepted result. |
| Existing `chaosx_alien_recovery_ledger_prepare_api_request` | Fully initialized source, policy, exact identity and counterpart receipt inputs. | Complete owner request and initialized caller-owned output storage. | Binds this transaction's source. It no longer creates a flag that skips all bases because one exact family overlaps. |
| Existing Event025/Event036 ledger resolvers and `record_api_result` | Current country, source-specific pending/delivered state, owner outputs. | Stable per-source delivery record and public copies. | Preserve one-shot source behavior, copy the exact selected identity, and commit a conversion proof only on owner success. Event036 legacy option must finalize delivery after its actual grant. |
| Proposed `chaosx_alien_recovery_ledger_conversion_is_proven` trigger | Two country-specific delivered sources, stored exact match, actual upgraded/Integration result, successful converted-delivery proof. | Boolean only. | Achievement tracking and parent tests consume it. No reward grant, field inference, or target mutation. |

The actual dispatch remains Event025 winner settlement -> shared ledger -> Event016 owner API -> existing operational/upgrade grants.
For Event036, use its source resolver and selected option -> the same owner API and ledger delivery commit.
Do not call a private native project settlement callback or duplicate owner logic into either event.
The current direct seams are the ledger owner calls at `025_alien_technology_in_antarctica_ledger_effects.txt:350` and `:497` and the Event036 option-A grant at `036_alien_spacecraft.txt:56-69`.
The parent's winner caller `chaosx_nr25_apply_winner_settlement` currently derives overlap from Event036 field flags and `brilliant_scientist_alien_spacecraft_recovered`, so it must adopt exact delivered receipts rather than keep that broad inference.
Its live line numbers can move during the parent's concurrent edits.

Every temporary output consumed after a helper returns needs caller-owned storage initialized before that call, including nested owner grants, ledger calls, and achievement queries that calculate temporary state.
Initialize applied, changed, selected-family, selected-upgrade, overlap, and conversion outputs to their documented none/false values at each relevant boundary.
Persistent per-source records use separate names to avoid temporary shadowing.
No stale family, upgrade, or field from a prior call may become the current reward.

## Exact receipt provenance and tiers

Reuse the permanent country arrays `chaosx_custom_technology_operational_provenance` and `chaosx_custom_technology_upgrade_provenance`.
The existing writers encode `selector * provenance_stride + source`, with stride `1000000` and validated sources from `1` inclusive to the stride exclusive at owner API `:94-131` and constants `:86-91`.
Append selectors without changing existing receipts.
The base family namespace and upgrade namespace remain distinct even if their numeric selectors coincide.
Use source `25` only for actual Event025 delivery and source `36` only for actual Event036 delivery.
Independent research or runtime repair may prove knowledge ownership but cannot establish a recovery origin.

The current upgrade grant records its prerequisite-family provenance as well as upgrade provenance at API `:515-516`.
Therefore an operational provenance array entry alone does not prove that the original reward was a base aircraft package.
Persist per-source actual result kind, family, upgrade, delivery status, and the exact matched prior-source identity in the shared ledger.
A conversion receipt should retain both source IDs, the collision family, actual delivered replacement identity, and its tier.
Given the present two-source contract, fixed per-event country variables plus a durable conversion flag are smaller than a new global registry.

Keep delivery status separate from resolution status.
`event036_recorded` presently means the resolver ran, and its legacy-result writer at ledger `:250-271` exposes tier zero with applied false.
This is not proof that the later option granted jets.
The currently permitted legacy option also needs a final consumed/delivered guard because re-exposing an allowed legacy path must not pay its stockpile twice.
On failure keep pending state and a defined repair/retry route that cannot issue the same source reward again after successful consumption.

Result tiers remain base `1`, upgrade `2`, Integration `3`, with none `0`.
Preserve `result_overlap_conversion` as an outcome classification only when the exact conversion proof is present.
Expose actual family/upgrade separately from broad presentation field and matched collision field.
A non-overlapping replacement base can have tier `1` and prove safe arbitration, but it is not an upgraded reward and cannot unlock achievement 14.
An unrelated upgrade's actual field must not inherit aircraft merely because the collision request concerned aircraft.
Store a separate monotonic highest-aircraft tier only for delivered aviation bases/refinements.
Generic Integration tier `3` does not prove aircraft tier `3` without an explicitly aircraft-specific output contract.

## Event-order behavior and achievement 14

| Order and exact state | Required dispatch | Achievement consequence |
| --- | --- | --- |
| Event036 first, same-country aviation base actually delivered, other missing bases remain | Event025 keeps base selection enabled and excludes only the owned exact aviation base. It grants another valid base. | No achievement from two base deliveries alone. |
| Event036 first, exact aviation base delivered, no other valid base remains | Event025 selects an eligible real upgrade, then Integration only when the full compatible pool is exhausted. Aviation refinement supplies a real candidate in a fresh campaign. | Counts only after a new upgraded/Integration result is actually applied and recorded against the proven collision. |
| Event025 first, aviation base delivered through owner API | Event036 suppresses the overlapping legacy base/stockpile path and requests the compatible aircraft refinement. | Counts after actual refinement delivery, not when Event036 merely opens or sets a pending flag. |
| Event025 first, Portal, Temporal, or another non-aviation result | Event036 can deliver its independent ordinary aircraft result. | No exact collision and no achievement. |
| Different countries | Each country checks only its own source receipts and owned IDs. | A global repeated-recovery count cannot prove achievement eligibility. |
| Repeated successful source call | Return historical record, applied false, no knowledge/stat/stockpile changes. | No new conversion, tier increase, or source attribution. |
| Already-owned aviation refinement with other valid bases remaining | A non-duplicate other-base result would require a parent-accepted Event036 replacement policy, or another accepted aircraft improvement. | Tier-one substitution never counts as an upgrade. Current upgrade-only request does not by itself authorize early Integration. |

The last row is a policy seam, not acceptance for new content.
Spec006 prefers aircraft-specific improvements for a later overlapping Event036 result, while its Integration rule requires exhaustion of all valid bases and compatible upgrades.
The current Event036 `allow_base = 0` request at ledger `:490` can reach Integration with unrelated bases still missing.
Do not silently resolve that conflict by early Integration, an unrelated free formation, or calling an unrelated land upgrade an aircraft improvement.
The parent can accept a different valid missing-base substitution under the current task, or define another real aircraft-specific replacement, and must record that decision.
For the ordinary fresh-campaign Event025-first collision, the proposed aviation refinement is unowned and supplies the direct accepted-shape upgraded aircraft result.

Achievement 14 is `025_alien_technology_two_crashes_one_answer` in spec011 `:387-407`.
It requires both current-country recovery identities, a true overlap conversion, and a successfully applied upgraded reward.
Current tracker `025_alien_technology_in_antarctica_achievement_effects.txt:111-118` reads both recorded flags, conversion-used, and result tier at least `1`.
Replace that broad proof with the durable conversion query and an actual upgrade/Integration tier check, so later unrelated result exposure cannot manufacture or erase proof.
The tracker flag is `chaosx_nr25_achievement_two_crashes_one_answer`.
A targeted search found its current setter but no reference in `common/achievements/`, so native achievement registration also remains a parent-owned integration dependency.
This sidecar does not declare the whole achievement complete.

## Constants and tuning plan

Append the aviation family and refinement selectors in `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt` without renumbering existing entries.
Keep the existing source IDs, provenance stride, result and tier vocabulary.
Add exact collision identities as owner vocabulary, not overloaded display-field numbers.
Keep aircraft and propulsion identities independent if future accepted content introduces both.
The current `0/1/2` scalar and one Event036 field cannot represent simultaneous distinct collisions.
Do not invent value `3` or a bitmask in a fixture without a reviewed source contract.
Two explicit identity inputs or a bounded owner-managed identity array would be sufficient when two actual payloads exist.

No weight, probability, reward-strength, or balance target is chosen by this handoff.
Existing candidate weight `chaosx_custom_technology_tuning.random_candidate_weight = 1` is source evidence, not approval for a new candidate or a normalized probability claim.
The parent owns the new candidate's weight and aircraft refinement values.
Put approved refinement tuning in an owner subsystem constant category with a short stat table covering base access, refinement output, compatibility, source grants, and maximum tiers.
For technology definition fields that reject `constant:` tokens, use documented file-scoped mirrors in the same technology file and record their authoritative shared keys.
Keep Integration's current tuning unchanged unless the parent separately authorizes a balance change.

## Event targets, lifetime, and cleanup

Reward ownership and historical recovery receipts remain country-scoped permanent knowledge.
No new global event target is needed for reward selection or achievement conversion.
If a caller temporarily leaves the receiving country scope, save a regular recipient target and return to that exact recipient rather than assume ROOT was rebound.
Existing `chaosx_alien_recovery_event025_owner` and physical-custody targets keep their current owner-specific lifetimes.
Destroying or transferring the artifact clears or moves physical access only, preserving learned aviation technologies, source provenance, completed conversion proof, and historical winner identity.
Do not grant aviation knowledge to a physical transferee automatically.
The parent's active destruction and transfer implementation must continue to own those tests.

Clear request-only normal bridges, exact exclusions, preferred-conversion selectors, and the obsolete broad exclusion flag after resolution or rejection.
Retain pending data required for a bounded failed-delivery repair and every successful consumed/source receipt.
Explicit runtime reconciliation can restore receipt-backed knowledge and consumers without issuing a new reward, rewriting provenance, creating native history, or increasing highest tiers.
No recurring whole-world scan or periodic reward hook is proposed.

## Migration and owner dependencies

1. Parent records acceptance or rejection of the proposed aviation package, vanilla-jet exception, refinement output, and exhausted-refinement replacement policy.
2. Event016 owner adds the exact static map, append-only selectors, grant/reapply/eligibility support, explicit changed-result semantics, and paired helper documentation.
3. Event016 owner fixes base filtering to read the actual request policy and exclude exact individual family identities, preserving valid non-overlapping bases.
4. Event025/Event036 ledger owner persists actual selected family and upgrade, source delivery, exact collision and conversion proof, with caller-owned temporary storage.
5. Event036 owner commits a source receipt only after successful option delivery and guards its existing stockpile separately, using the owner branch for shared aviation knowledge.
6. Parent updates winner settlement, broad field localisation, achievement proof/registry, overview and integration documentation, and acceptance fixtures.
7. Parent reviews the new general-package CXT extension contract and registers bounded idempotent test setup if the new package is implemented, with no automatic free formation or periodic grant hook.
8. Probability auditor establishes the accepted expanded candidate pool and compares the owner-applied patch using immutable before sources and the same named scenarios, preserving any fixture changes explicitly.

The proposed implementation affects owner API effects/triggers/constants, grant-only technology definitions, owner runtime reconciliation and Markdown, the shared ledger and triggers, the Event036 option seam, the parent winner caller, achievement tracking/registration, and associated localisation/docs.
It requires no change to Portal or Temporal gameplay, native jet-project definitions, country histories, Kruger or Directorate routes, Event016 evolution state, custom land providers, or unrelated equipment.
Existing Event036 option A sets `brilliant_scientist_alien_spacecraft_recovered` and calls `brilliant_scientist_try_schedule_alien_spacecraft_contact`.
That existing contact path is distinct from the neutral package and must not be imported into Event025 grants or the new neutral conversion branch.
The Event036 owner must review its preservation policy separately instead of infer that neutral aircraft knowledge should create Event016 contact/history state.

## Meaningful validation and evidence gaps

Completed: live AGENTS and the events/subagents skills were read, accepted reward and acceptance surfaces were traced, the supplied probability-auditor handoff and scenario contract were read, exact owner technology/unit outputs and installed vanilla jet consumers were inspected, and source identity hashes below were checked.
The current owner API, triggers, constants, technology files, units, Event036 source and shared ledger still matched the supplied frozen probability baseline at the recorded hash check.
Repository HEAD at that check was `cbeb25d4ffe892875674fd4454894bf1168b9e73`.
The shared tree contains concurrent changes, so this is a read-time identity check rather than a workspace-wide immutability claim.

Required MCP tool names and exposed schemas were discovered from the connected tool inventory.
The first probability request incorrectly used `source.file` and returned `MCP error -32602`, `Unrecognized key: "file" at source`.
It was corrected to `source: { path: "common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt" }` with adapter `random_list`, but produced no result before the pending request was cancelled.
The first event request omitted `selector.kind` and returned `MCP error -32602`, `Invalid discriminator value. Expected 'event' | 'namespace' | 'file' | 'source' | 'node' | 'manifest' at selector.kind`.
A retry with `selector: { kind: "event", id: "chaosx.nr25.1" }` likewise produced no result before cancellation.
No accepted selector coverage is claimed from that retry.

An initial `hoi4.tech_inspect` unlock request returned the transport error `timed out awaiting tools/call after 600s`.
Its provisional technology selector was `teleportation_tech`, so it supplied no evidence for the actual owner technology even apart from the timeout.
A corrected request for `brilliant_scientist_portal_warfare_tech` was also attempted and produced no result before the pending request was cancelled.
`hoi4.reference_search` for `set_technology`, `hoi4.reference_context` for the neutral technology work surface, and `hoi4.source_lookup` for `jet_fighter2` were attempted but returned no result before their pending requests were cancelled.
No reference ID/revision was returned to permit a valid `hoi4.reference_read` continuation.
The exposed source-lookup schema also lacks `view` and `keyPath`, so bounded-child lookup was not assumed available.
Connected version/health, native task negotiation, helper-expansion support and standalone viewer availability were not confirmed.
No helper-expansion or background rewrite was used.

These are transport/delivery and schema-attempt gaps, not proof that every exposed tool is absent.
There is no MCP source revision, artifact URI, candidate-pool completeness, normalized probability, rendered graph, comparison, scenario hash, or engine-validation result for this handoff.
Event render/compare and technology render/compare remain unrun following unsuccessful inspection delivery.
Reference rules were read directly from local files as permitted for a route gap, with hashes and line spans below.
Source inspection and local citations are not equivalent to required MCP evidence.

Reuse the existing read-only `chaosx_ai_probability_auditor` handoff `025_reward_probability_baseline_20261003.md` and its `025_reward_probability_baseline_20261003_evidence/scenario_contract.md`.
Do not spawn a duplicate baseline audit to obscure its blocked status.
The frozen source directory there is the actual before-source evidence for a later owner patch.
Its ten names remain `no_owned_bases`, `one_owned_base`, `overlap_aircraft_other_bases_missing`, `overlap_propulsion_other_bases_missing`, `overlap_both_other_bases_missing`, `all_bases_owned_upgrade_available`, `all_bases_and_upgrades_owned`, `repeated_event025_receipt`, `event036_first`, and `event025_first`.

Adding aviation changes the candidate universe from seven to eight bases and eleven to twelve upgrades.
The original fixtures that condition on Portal being aircraft remain false exact-collision fixtures.
Retain them as negative controls and record separate accepted aviation-positive variants rather than silently rewrite their inputs while claiming identical scenarios.
The propulsion and both-field positive fixtures remain blocked until actual output identities and source inputs exist.
The auditor must report this candidate/schema contract change explicitly and use the same preserved scenario definitions for each valid before/after comparison.
No probability number is inferred here from equal source weights.

Parent validation must establish: other-base selection survives an exact aircraft exclusion, real same-country collision in both orders, a non-aviation reward never collides, actual refinement output changes its aircraft consumer, independent research is not recovery provenance, repeated Event036 options cannot duplicate its stockpile, temporary outputs survive conservative helper-return cleanup, pending delivery does not consume success, and destruction/transfer preserve learned receipts.
Achievement positives require a real applied tier-two refinement or exhausted-pool Integration, while both-base, pending, broad-label-only, different-country and unrelated-reward cases must fail.
Also validate that the new branch creates no Event016 project/history/evolution state, land provider rows, free formations, or unrelated equipment.
Required probability compare remains assigned to `chaosx_ai_probability_auditor` after the owner patch.
No implementation tests or live-game checks were run in this plan-only assignment.

## Source and reference identities

The following hashes are local SHA-256 identities, not MCP revisions.
Owner paths are relative to the workspace above.

| Source | SHA-256 |
| --- | --- |
| Accepted spec006 | `5E0F7F84FD846176218FF029ED0BDD954A4059651EDF70B9636CB155CD7740AA` |
| Accepted spec014 | `C072F6F2150858F9159803D046F6CBE629DCC1C206612BF8A5B3232608AA5D10` |
| `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` | `4AA4CB9BAE94A76B8F33A5EA37F76E3C1AB040168FB688C7B9CD4A3C9EB6D3E1` |
| `common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt` | `EDE44BE51D047929E45DE9EDBF59D5064C98983E5A914C46F0D7FC31B58AA19B` |
| `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt` | `12F0D51FC9EC7ABF7C4F3CB8308AB94526B8992E3834C607D73C5942E508A26B` |
| `common/technologies/016_brilliant_scientist_project_technologies.txt` | `60BF2225FA86B235EE30898A9B1D19383D6D89AF72613764FD1A72D75AE7548E` |
| `common/technologies/016_brilliant_scientist_project_force_technologies.txt` | `8B0129A6B71FFCB5AD5D4EF354329D3ED10B18919D0849922A52763049F3F1D0` |
| `common/units/016_brilliant_scientist_project_forces.txt` | `FD0DF90E8C27DB087E7DF09BA8E325F3AE887A80B673677179D0FD5403489357` |
| `events/036_alien_spacecraft.txt` | `6531D27F883458F3D5E874CBEF1C01A197D23D101C57CAA2FC38D35567A69C73` |
| `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt` | `91F55888298A54E2B711EFE1CA1AD4C2F122951D6121089E1DD637886C4692DE` |
| `common/scripted_effects/016_conventional_technology_api_effects.txt` | `33B2CF385F2B2B687C891E778655ED9418B3D66031FA97AB65124D8FADDAA52B` |
| `common/scripted_effects/016_mengele_native_prototype_effects.txt` | `F3EBE41D73C86160313119D5FEF8A135C670A34569DA715D718194C4BACC13D9` |
| `common/scripted_effects/016_mengele_project_stage_effects.txt` | `C7DDD7577B76778EC90F502378323AFCBC2DA851B8D854554AB81EF96484A36D` |
| `common/special_projects/projects/air_projects.txt` | `A8906A75813900DF6E19BA21163D6B9E28A0B8B9989BC260B914B7A9D1C4F0E4` |

Installed references below use the root `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Offline wiki paths are relative to the workspace.

| Reference and sections read | Local SHA-256 |
| --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:263-283`, `:435-447`, event targets, persistence, temporary output lifetime and scoping | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:1937-1943`, `:4504-4542`, `:4683-4713`, technology grants, relative weights and scripted-effect invocation | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:875-877`, `:2359-2383`, ownership and scripted-trigger invocation | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:258-263`, country/root/previous scope distinctions | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:656-682`, scope-aware defined text and temporary getters | `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064` |
| `paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md:98-197`, static modifiers, completion effects, unlocks and hidden bridges | `C5428838DB20C4C812C66AFF82CBAFC58DB3B73453C30436BCE0D97436170BEE` |
| Installed `documentation/effects_documentation.md:1174-1208`, `:2733-2749`, `:5413-5429`, `:6496-6514`, `:7805-7833`, equipment bonus precedent, targets, weights and country technology grants | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Installed `documentation/triggers_documentation.md:3844-3853`, `:4882-4890`, event-target and country technology queries | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Installed `documentation/script_concept_documentation.md:120-184`, `:216-249`, localisation scopes and script constants | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| Installed `common/script_constants/documentation.md`, complete schema and examples | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| Installed `common/technologies/air_techs.txt:535-618`, `:625-655`, real jet unlocks and gated higher tier | `B9CBD21B2DBFA819B07D435F3557B037420F8885A7D0EC8C221C1A78015B941D` |
| Installed `common/units/air.txt:157-166`, real jet consumer | `13A5F3FF144C9BC754C7D7AEA60D2A90CB282C335BFE312F9762785134D0C574` |
| Installed `common/units/equipment/x_plane_airframes.txt:1-32`, `:131-175`, `:359-401`, aircraft archetypes and outputs | `0747E1A834D4C44EEEE593BC0D5CBD7F636BE6F34BE89BE53B19F83AFCD08F8A` |

## Simplifications, omissions, and blockers

No gameplay fallback or simplification was applied.
Only this proposed contract was written using the events and subagents skills.
No skill was created or updated.
The owner extension, aircraft refinement fields and values, exhausted-refinement replacement policy, actual propulsion/two-field payloads, native achievement registration, DLC/designer consumer checks, and mandatory MCP probability/event/technology evidence remain unresolved dependencies.
No GUI, focus, map, or decision-button helper was designed or changed in this sidecar, so it makes no completion claim for those surfaces.
The completed deliverable is the narrow architecture recommendation, not Event025 implementation or exact-overlap gameplay validation.
