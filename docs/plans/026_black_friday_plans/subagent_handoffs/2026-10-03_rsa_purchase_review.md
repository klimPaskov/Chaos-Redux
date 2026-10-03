# Event 26 RSA purchase review

Review date: 2026-10-03. Review type: read-only source audit. Scope: the five existing RSA purchase decisions and their Event 26 quote, payment, receipt, refund, and display adapters. No source files were edited.

Disposition: the bounded RSA source follow-up is complete. The parent’s regional-request replay fix and narrow host/exile requirement summaries are present in source, and the latest caller-array storage change was rechecked. Post-war category density remains separate Event 12 owner work. Native payment, live UI, save/reload, shared receipt-core audit, and scenario-specific probability evidence remain unresolved. This handoff does not claim universal Event 26 cost coverage or event completion.

The parent transaction ledger, `docs/systems/africa_rsa_purchase_transactions.md`, now records 295 bundle checks plus 30 request-scope checks and explicitly states that native resource operations, shared receipt APIs, external helpers, achievement proof, live display, and save/reload remain unverified. The parent reports that the full 295+30 suite was rerun after the latest caller-array storage change; native APIs and fixtures are mocked. The current RSA callers preinitialize quote, payment, record, refund, settlement, and aligned-array storage. A shared receipt-caller initialization defect is under architect repair, and an actual-source receipt audit remains pending outside this RSA-only scope.

## Source identity

The immutable baseline `docs/testing/2026-10-03_event26_rsa_before/012_africa_rsa_decisions.txt` hashes to `40283784E0D0EA091BD96C96C46F0155EC01E911091B2B20A0389AC5E1D696CC`, matching the supplied baseline and the parent-reported byte-preserving commit `f9f057581c080784b92ed14fd0a736f6f9708958`. Current decision source hash after the requirement-summary update: `0F5CFC6369BE6A42C5C0705C318352B9C70951DFDC7C6244BE9172DD1D15F884`.

| Current source | SHA-256 |
| --- | --- |
| `common/decisions/012_africa_rsa_decisions.txt` | `0F5CFC6369BE6A42C5C0705C318352B9C70951DFDC7C6244BE9172DD1D15F884` |
| `common/scripted_effects/012_africa_rsa_purchase_effects.txt` | `5DF2CAB6B5A0E628C096DB4FBDA1443FD011863135D85C7AA091D230DC531FEE` |
| `common/scripted_effects/012_africa_rsa_support_request_effects.txt` | `206C1AABD0C2BCC908C939E2827018223EF1EF3987241D486961A75EA85D1D92` |
| `common/scripted_effects/012_africa_rsa_effects.txt` | `9D34584A577ED0B33A8DFFA40E4A20EC7AAECE6D201C94A90F40C19BC7385306` |
| `common/scripted_triggers/012_africa_rsa_purchase_triggers.txt` | `EC3C1ADF78C811F6729B63CE4B0544D1DB00D04FE90F59E34F1F80A001431653` |
| `common/scripted_triggers/012_africa_rsa_triggers.txt` | `320D02ECA904154F70C9DB161D52DB692404F1BCDF9AD5518CCA8674376CE77B` |
| `common/script_constants/012_africa_rsa_purchase_constants.txt` | `CC40CFE52805DDE2CE39C96D85D7406E8A8237A90730C07DBAED966018E5F916` |
| `common/script_constants/012_africa_rsa_constants.txt` | `F4979BD1E1F2D575A88E0149036E5F698FEA3B89C5D863DEEF9ED2B48569C41A` |
| `common/scripted_localisation/012_africa_rsa_purchase_localisation.txt` | `4245FE74CF31A6442B536C03BA821C6E4AA95F73A7AA575D816EBEAF57FF3F20` |
| `events/012_africa_rsa.txt` | `89D5165760C2B0505D50265BE01720FBA546BD6F62C45D7082323CAF58CE325E` |
| `localisation/english/012_africa_rsa_l_english.yml` | `DBE357D5F22B510FF80C8E4ACDAE7FC604B0E3874D70DFD33616898F167EC95E` |

The latest purchase-effect change predeclares each of the five aligned temporary arrays with `resize_temp_array ... size = constant:universal_cost_framework.one` in the caller before `africa_rsa_prepare_purchase_bundle` clears and rebuilds them (`common/scripted_effects/012_africa_rsa_purchase_effects.txt:72-87`). This is storage initialization only; the parent reports no cost, target, outcome, AI, cooldown, or route change. The refreshed source hash above reflects this change.

## Findings by severity

### P1: Regional-request replay path closed by the parent update

The recheck confirms the new queue helper sets a payer-owned donor pointer and donor pending flag before queuing `chaosx.nr12.1202` (`common/scripted_effects/012_africa_rsa_support_request_effects.txt:6-15`). The public target predicate now adds a pending-flag exclusion, while `africa_rsa_is_eligible_regional_support_target` preserves the former target-body checks for both initial selection and response validation (`common/scripted_triggers/012_africa_rsa_triggers.txt:302-332`).

The recipient event exposes acceptance only while the pending response remains valid (`events/012_africa_rsa.txt:50-78`). Acceptance registers the donor under the less-than-two cap before the unchanged equipment reward; the reward runs only if the donor receives its unique supporter flag (`common/scripted_effects/012_africa_rsa_support_request_effects.txt:29-46`, `common/scripted_effects/012_africa_rsa_effects.txt:632-644`). A duplicate event copy after the first response sees no pending flag and cannot register or ship again. Refusal consumes one pending request, and stale responses release pending state without a shipment.

Queueing also now follows confirmed settlement. The caller checks `africa_rsa_purchase_confirmation_result`, queues only on successful settlement, and refunds without sending the event on a non-success result (`common/scripted_effects/012_africa_rsa_purchase_effects.txt:267-288`). The old target eligibility predicate body is retained in `africa_rsa_is_eligible_regional_support_target`; only the public decision predicate adds the pending check.

Status: closed at source for the inspected duplicate-request and failed-settlement paths. The parent reports 30 request-specific source checks, including the original target-body comparison and unchanged `chaosx.nr12.1202` AI-chance blocks. Those checks mock native APIs and do not replace multiplayer or in-game event validation.

### P2: Post-war target clones can exceed the category action budget

`africa_rsa_guarantee_neighbor_sovereignty` is targeted through `africa_selected_targets` and can coexist with the citizenship milestone and early lease termination (`common/decisions/012_africa_rsa_decisions.txt:111-177,179-195`). The selected-target capacity starts at five and can grow to nine or sixteen (`common/script_constants/012_africa_constants.txt:433-435`, `common/scripted_effects/012_africa_effects.txt:1098-1122`). The target trigger limits guarantee rows to eligible African neighbors, but each matching country produces a separate native decision entry under the vanilla targeted-decision contract.

Source-derived counterexample: six valid neighboring countries are in the selected roster while citizenship remains incomplete and the temporary lease is active. The category then exposes six guarantee rows, one citizenship action, and one lease-termination action, for eight primary action entries. I could not confirm that exact state through the decision inspector, so the count is a bounded source scenario rather than a native render result. During the civil-war phase, five support target rows plus the relief decision can reach six primary entries, alongside one active objective mission.

Status: unresolved and routed to a separate Event 12 owner plan. Do not suppress existing routes or shrink target pools inside the RSA cost adapter. The target-control count is already at five in the opening phase, above the usual one-to-three target controls guidance.

### P2, conditional: Abnormal settlement remains an owner-visible pending state

The regional-request caller now initializes and checks `africa_rsa_purchase_confirmation_result`; on non-success it refunds and does not queue the recipient event (`common/scripted_effects/012_africa_rsa_purchase_effects.txt:267-288`). The other four owner effects still apply their immediate outcome before settlement. If settlement returns non-success, they retain the receipt pointer and expose the localized `Order pending` cost/status fallback rather than permitting another purchase (`common/scripted_effects/012_africa_rsa_purchase_effects.txt:216-245`, `common/scripted_localisation/012_africa_rsa_purchase_localisation.txt:102-514`).

Status: the regional-request non-success path is closed at source. The retained pending state for the other four actions is intentional and truthfully displayed. The parent reports a generic receipt-caller initialization defect under repair across 13 shared helpers, with an actual-source receipt audit still pending. This audit did not probe native settlement behavior.

### P3: Host and exile eligibility summaries added in source

The current decision source wraps the current-host and exile-recovery predicates in separate `custom_trigger_tooltip` summaries (`common/decisions/012_africa_rsa_decisions.txt:117-122,207-212`). Their keys are present at `localisation/english/012_africa_rsa_l_english.yml:5-6`: the host summary requires the unification host, and the exile summary names independent status, capitulation, capital control, and the inherited mandate.

Status: closed at source for requirement wording. Native blocked-row rendering remains unverified because decision inspection produced no result. Non-consumed requirements remain separate from the cost row.

### P3: The relief AI multiplier duplicates an availability gate

`africa_rsa_protect_civilian_corridor` requires control of state 275 and also doubles its AI weight when state 275 is controlled (`common/decisions/012_africa_rsa_decisions.txt:25-45`). Every available instance therefore receives the same multiplier, so the modifier cannot distinguish selectable situations. This is a source-level redundancy, not a balance target; no AI weight was changed.

The old epsilon gate constants such as `relief_pp_gate` and `citizenship_stability_gate` remain in `common/script_constants/012_africa_rsa_constants.txt:86-107` but have no current references. This is non-blocking cleanup information and does not affect the new shared affordability path.

## Decision lifecycle and cognitive load

`africa_rsa_crisis_category` is visible during the civil war, after continental victory, while the Cape lease exists, or while exile recovery is available (`common/decisions/categories/012_africa_rsa_categories.txt:10-22`). Relief is a one-use civil-war action, regional support remains available per target until two distinct accepted supporters are recorded, citizenship and guarantee each close on their completion flags, lease termination is one-use, and exile recovery is a single-custodian action. These lifecycle gates are source-consistent with the payment entries.

The ordinary decision descriptions and category description are concise. There is no custom scripted GUI or attached value dump in the RSA category, so `hoi4.gui_inspect` and `hoi4.gui_render` were not applicable. The displayed values are costs only. Each value carries its resource icon and amount, and its surrounding title or tooltip explains the purchase purpose; no unexplained mechanic meter is introduced. Native row spacing and clipping remain unverified.

| Phase | Source-derived visible primary actions | Active missions and cognitive-load note |
| --- | --- | --- |
| Civil war | Up to five selected-target support entries plus the relief action, reaching six decision entries. | One active first-proof mission. Target controls are at the high end of the normal one-to-three range. |
| Post-war settlement | Citizenship, lease termination when active, and one guarantee entry per eligible selected neighbor. | No first-proof mission after crisis cleanup. Six valid neighbor entries plus the two ordinary actions yield the P2 eight-entry scenario above. |
| Exile custody | One recovery action while its route, receipt, sovereign status, and capital-control gates hold. | No duplicate mission or second-click objective is introduced by this purchase. |

## Cost, requirements, and primary-family audit

| Decision ID | Spendable costs | Distinct types | Display contract | Primary family |
| --- | --- | ---: | --- | --- |
| `africa_rsa_protect_civilian_corridor` | 35 PP, 20 CP, 5 train equipment, 150 support equipment | 4 | PP/CP/trains inline; support equipment in full cost tooltip | Political Power |
| `africa_rsa_seek_regional_support` | 15 PP | 1 | PP inline and in tooltip | Political Power |
| `africa_rsa_enact_citizenship_land_milestone` | 75 PP, 0.05 stability | 2 | Both inline and in tooltip | Political Power |
| `africa_rsa_guarantee_neighbor_sovereignty` | 40 PP, 10 CP | 2 | Both inline and in tooltip | Political Power |
| `africa_rsa_reconstitute_exile_council` | 60 PP, 25 CP | 2 | Both inline and in tooltip | Political Power |

All five actions stay at or below the four-cost hard limit. Every displayed spendable component uses its texticon: `£pol_power`, `£command_power`, `£GFX_train_texticon`, `£support_equipment_text_icon`, or `£stability_texticon`. The support-equipment sprite is defined by `interface/chaosx_texticons.gfx:90-92`; train and stability icons are in installed `interface/texticons.gfx:105-106,2563-2564`. The relief row shows three components inline and puts the fourth in the full tooltip without adding a fifth cost.

Each decision has one shared `africa_rsa_can_pay_*_purchase` predicate called from both `available` and `custom_cost_trigger`, with custom cost checks hidden. Owner effects revalidate route, target, and objective gates before payment. Relief and citizenship apply their outcome only after bundle payment succeeds. Regional support settles at valid recipient selection, then queues the existing request event; refusal does not refund because the paid action is request submission. Guarantee checks the native `is_guaranteed_by = ROOT` result and refunds on failure. Exile recovery uses the same one-use completion predicate and clears its availability only after the outcome helper.

Political Power is the primary family in every transaction. The regional request explicitly sets the PP-only allowance for Black Friday receipt classification and resets it afterward. `ai_hint_pp_cost` literals match each ordinary PP amount; they are fixed native hints and do not claim discounted or secondary-resource AI scoring. The parent ledger records the 0.01 stability quantum and source-model prices of 0.03/0.02 at the two Black Friday rates.

## Mission and objective-proof notes

| Mission | Owner/category | Region and requirement | Duration | Success/failure | Duplicate risk |
| --- | --- | --- | ---: | --- | --- |
| `africa_rsa_first_proof_mission` | Continental Coalition; `africa_rsa_crisis_category` | State 275 must be controlled and hold an industrial complex or arms factory; civilians must be protected; two distinct African supporters must be recorded; a controlled Cape or Natal naval base must connect to state 275 by an allied-only railway. | 360 days, from `africa_rsa_days.first_proof` | Goal-style auto-completion records the civil-war first proof and its ledger; timeout/cancel records failure and cleans the first-proof ledger. | One activation call in `africa_rsa_prepare_first_proof`; crisis cleanup removes any active mission. No duplicate activation found in the bounded source search. |

This mission is objective context only and was excluded from the five-purchase probability pool per the user's scope clarification.

## AI, route validity, cleanup, and exploit notes

The source bases are `high = 10`, `preferred = 20`, and `modifier_double = 2`. Regional support can target a valid non-neighbor, with neighbors doubled; guarantee targets must be sovereign African neighbors and receive the faction-member multiplier. Citizenship and exile weights are flat inside their route gates. The relief multiplier is redundant with availability as described above. Support target validation excludes nonexistent, capitulated, special/nonhuman, non-African, already-supporting, refused, faction-conflicting, and currently warring targets; it does not require `is_subject = no`. Whether subject governments count as valid supporters is an event-design choice, not a proven defect in this audit.

Completed actions are bounded by one-use flags or the unique supporter/refusal target flags. Refund success clears the receipt pointer; rejected or partial refund keeps it, preventing a new purchase from overwriting unresolved state. The support-request pending flag is set before the event, consumed once by accept/refuse, and cleared through the existing old-host, terminal-host, and continental-crisis cleanup paths. Each cleanup traverses only the payer's pending-donor array. Parent reports repeated-refund and request checks with shared helper APIs mocked.

## Probability and MCP evidence

`chaosx_ai_probability_auditor` inspected the five purchase-weight sources but could not obtain `hoi4.probability_inspect` output. Its broad five-candidate request and one-candidate retry returned no artifact, revision, diagnostic, scenario hash, or error body. `probability_evaluate` and `probability_sweep` were therefore not run because the tool supplied no inspected inputs or confirmed scenario-set schema. The source-only weight observations above are not effective score traces or click probabilities. Scenario names in the auditor's handoff are proposed test cases, not executed MCP scenarios.

`hoi4.decision_inspect` for `africa_rsa_protect_civilian_corridor` with one RSA action scenario timed out after 600 seconds. A no-scenario retry was rejected because the route requires declared scenarios. A minimal one-action scenario without a date also timed out after 600 seconds. No decision artifact or native scenario finding exists. No new HOI4 MCP calls were made during this parent-fix recheck; the earlier missing results remain route blockers.

`hoi4.reference_context`'s first call rejected an overlong question, and a valid short decision-context retry was caller-terminated after about three minutes without output. Two targeted `hoi4.reference_search` calls timed out after 600 seconds. `hoi4.source_lookup` for the exact decision symbol was caller-terminated after about a minute, then retried with `maxLines = 20` and no references and caller-terminated after about a minute without output. No MCP source revision or artifact was returned. Local offline references and installed vanilla files were read directly; they are not substitutes for the missing MCP scenario or probability evidence.

Local references used include `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:308-335,441-455,465-478,511-536`, `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md:28-35`, `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:429-441`, installed `common\decisions\_documentation.md:1-45`, and the vanilla custom-cost precedent `common\decisions\PRC.txt:4270-4310`. The offline Decision modding page says each target match creates a separate decision entry and describes literal `ai_hint_pp_cost`; the installed documentation describes the per-frame and daily decision triggers. Reference file hashes are recorded in the working audit source evidence.

## Changed files, validation, and remaining work

Changed files by this reviewer: only this audit handoff. No gameplay source, localisation, or event files were changed. The five purchase decision IDs are listed in the cost table; the existing first-proof mission is context only. No tests were run by this reviewer. The owner ledger now records 295 bundle checks plus 30 request-specific checks; the parent reports both suites passed after the latest array-storage change, with native APIs and fixtures mocked.

Remaining owner work: route the post-war category-density issue through the Event 12 owner plan; complete the shared receipt-core repair and actual-source receipt audit; complete probability analysis with the category's lease action and expanded target instances in the candidate pool; and obtain native payment, display, and save/reload evidence. The universal cost transaction ledger remains `blocked_pending_evidence` for those native gates, and the parent ledger explicitly says this handoff does not establish universal Event 26 coverage.

Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, the content-budget section of `chaos-redux-scripted-gui`, and `chaosx_ai_probability_auditor`. No skill or source file was modified.
