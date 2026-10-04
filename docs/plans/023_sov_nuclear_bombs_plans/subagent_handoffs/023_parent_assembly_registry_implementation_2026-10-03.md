# Event 23 bounded assembly registry implementation

Disposition: `implemented` source patch within the user's bounded-registry authorization; mandatory MCP, audit and runtime acceptance remains outstanding.
Event 23 and the complete visual-asset repair goal remain incomplete.

## Acceptance and ownership

The user explicitly chose to design and implement the Part 6 bounded registry rather than limiting it to previously represented fields.
The parent selected an existing industrial storage depot through the existing Assemble Device Batch decision, preserving the existing mission, costs, duration, batch amounts and AI weights.
This is the parent's implementation rule within that authorization, not a claim that the user specified its factory predicate or nonce schema.
No new GUI, decision family, mission, building, technology, delivery aircraft, unit, country or artwork family is introduced.
Evolution timing remains unchanged under the user's deferred-tuning decision.

## Source changes

| File | Owned patch |
| --- | --- |
| `common/decisions/023_sov_nuclear_bombs_decisions.txt` | Existing assembly action targets `any_owned_state`, rechecks exact depot and costs on click, starts the mission before payment; existing mission cancels on loss of site or reactor support. |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt` | Industrial storage-depot predicate and exact active pointer/id/owner/nonce validation. |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | Start selects and registers the facility; completion revalidates it; rejection, completion and cancellation close the exact receipt. |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | Persisted facility and institutional-access markers, active/closed batch nonces, Event 5 before/after mirrors, annex closure, guarded production transaction and ordinary state-change registry ordering. |
| `common/on_actions/023_sov_nuclear_bombs_on_actions.txt` | Existing exact-state callback admits represented registry roles as well as storage sites; no new periodic hook or world scan. |
| `localisation/english/023_soviet_nukes_l_english.yml` | Assembly mission identifies the exact selected state and explains cancellation on loss of depot, factories or reactor support; existing requirements text retained. |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md` | Assembly helper scope, inputs, outputs, cleanup, side effects, example and evidence limits; no-yield shared action contract reconciled. |
| `docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_spec_part_6_soviet_collapse_integration.md` | Parent-accepted selection rule and user authorization recorded with implementation and validation limits. |
| `docs/events/023_sov_nuclear_bombs.md` | Current transit-subset, assembly and transfer contract replaces stale source descriptions without claiming live acceptance. |
| `023_parent_reference_and_save_evidence_2026-10-03.md` | Local reference spans/hashes, MCP route gaps, and recovered curator handoff recorded. |

The existing bounded registry edits for transit, active dismantlement, command locations, production reactors, access markers and delivery owners precede this patch and still require complete recovery review.
This handoff does not certify all of them merely because assembly now has an identity.

## Local contract checks

Read-only block assertions verified exact selection at start, absence of content grants in facility registration, gated completion, no grant on cancellation, nonce-bound closure, display-target cleanup, before/after assembly receipt fields, final-holder access comparison and payment-after-start ordering.
The first assertion runner incorrectly matched `can_pay_security_cost` as the debit; its debit-token check was corrected to the exact `sov_nuclear_bombs_pay_security_cost = yes` invocation.
No gameplay correction was inferred from that runner error.

| Named source case | Source behavior reviewed | Acceptance limit |
| --- | --- | --- |
| `P23_ASSEMBLY_START_EXACT_DEPOT` | SOV owns and controls a registered industrial depot; atomic technologies and surviving reactor program required; one site/id/owner/nonce bound to the existing mission. | Native decision reachability and text-fit not rendered. |
| `P23_ASSEMBLY_STALE_CLICK` | Click preflight repeats actor, capacity, technology, project, cooldown, affordability and site gates; no payment without the active mission receipt. | Native stale-click scheduling unobserved. |
| `P23_ASSEMBLY_SITE_CAPTURE` | Exact-state callback cancels the active batch, retains historical facility identity and marks it contested; it grants no successor technical or command stage. | Capture callback and save/reload unobserved. |
| `P23_ASSEMBLY_REACTOR_OR_FACTORY_LOSS` | Mission cancellation and timeout success gate reject missing reactor support or invalid exact depot; no reroute. | Native evaluation cadence unobserved. |
| `P23_ASSEMBLY_TIMEOUT_REPLAY` | Completion requires the active production flag, clears it once and closes the matching site nonce; subsequent calls cannot publish another batch. | Engine persistence and reentrant callback ordering unobserved. |
| `P23_ASSEMBLY_SOV_ANNEX` | Country cleanup closes its assembly receipt before clearing Soviet-only project state; physical site history remains. | Annex ordering and local custody continuation unobserved. |

These are source assertions and reviewed contracts, not probability evaluations, engine simulations, or observed campaign outcomes.
No game, log or save was modified.

## Asset and catalog reconciliation

The recovered documentation-curator handoff `023_achievement_asset_documentation_reconciliation_2026-10-03.md` was reviewed against the selected three-v2/four-v1 set and stable 21 runtime destinations.
Its documentation-only validation and missing MCP artifacts remain explicit.
The seven final achievement triplets have the separate 2026-10-03 canonical runtime audit recorded in `023_achievement_icon_runtime_promotion_2026-09-26.md`.
No additional art was generated or modified in this assembly patch.

Read-only workbook comparison confirmed the title, Event Details and four evolution bodies match current localisation exactly, with Minor Fire-Once, Chaos level 2, and empty cluster/world-end fields retained.
This assembly patch changes no workbook field, so no gratuitous workbook save was performed.
The canonical `.tools/export_event_catalog_csv.py` regenerated all three exports from the authoritative XLSX successfully: Events 166 rows/13 columns, Clusters 20/8, Scenarios 17/6.
CSV files were not edited directly, and unrelated workbook or catalog changes remain other agents' property.

## Remaining work and blockers

The corrected decision-reference request returned `timed out awaiting tools/call after 600s`.
The fresh read-only decision/mission auditor `01a10035-754f-7bd3-99ad-e7a35da1b895` was dispatched with `fork_context=false` and a complete bounded prompt; no final handoff has been received at this report's last check.
Its final result must be appended when available.
Previous MCP source lookup timed out after 600 seconds, and previous recovery workers failed workspace routing; local source review is not equivalent MCP evidence.
The real native delivery route, native early bomb payment and cancellation contract, all named probability bindings/comparisons, complete registry conservation, save/reload proof, reactor queue identity, live text/asset consumer evidence, full completion audits and final focused commit remain outstanding.
The physical-severity accident route retains its parent cutoff of Integrity 10 and unchanged four random outcome weights; shared non-yield and true-yield consequence magnitudes still need acceptance evidence.
The original icon prompt remains absent; the user-authorized verbatim replacement prompts provide new lineage, not recovered original provenance.
No fallback, timing tuning, cost tuning, AI-weight tuning, or new scope expansion was used in this patch.
No commit is made while the accepted package and its required evidence remain incomplete.

Skills used for this continuation: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-event-assets`, `chaos-redux-native-raids`, `chaos-redux-save-inspection`, `chaos-redux-shared-git-commit`, and `xlsx`.
No skill was created or changed by this continuation.
