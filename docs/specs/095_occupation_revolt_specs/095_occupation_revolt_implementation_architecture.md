# Event 095 implementation architecture

Status: proposed implementation contract, not implemented or engine-verified.
The 14 specification parts define gameplay.
This document maps ownership and integration work without pretending that proposed helper names or uninspected native capabilities already exist.

## Repository baseline actually inspected

The full `events/095_occupation_revolt.txt` was fetched at commit `5212636eef9f9607691ddc1348bddade1bafe0dd`.
The file uses namespace `chaosx.nr95`, hidden root `chaosx.nr95.1`, report `chaosx.nr95.2`, and shared news event `chaosx.news.76`.
The root selects only a government in exile, chooses one random enemy, transfers matching controlled core states, defines one mixed Revolt Division template, and creates one unit in every owned state.
The report grants 15% war support and 50 political power before scheduling the news.
Those old grants and the template are baseline facts to review, not automatically accepted parts of the new design.
The new design replaces the universal all-owned-states army and broad transfer with a finite exact opening.

The full historical handoff `docs/plans/famine_and_migration_system_plans/subagent_handoffs/event043_050_051_095_adapter_owner_patch.md` was also read at that commit.
Its Event 095 section says the old root has no exact civilian transaction or local grievance receipt that would justify famine, migration or Deaths adapters.
Its older `fm_*` API names are explicitly superseded in its own banner.
Use current owner contracts rather than copying those historical names into new code.
Its historical tool runs belong to that earlier task and are not evidence of tool execution in this task.

Only lines 1–170 of `common/mtth/chaosx_mtth_variables.txt` were read.
That external file is a partial read, not part of the 46 fully read supplied text sources.
No claim is made that the current event registration, all shared callbacks, offline wiki or installed native code was fully inspected.

## Proposed file ownership

| Surface | Existing or proposed path | Role |
|---|---|---|
| Root and reports | `events/095_occupation_revolt.txt` | Preserve root identity, route finite opening and lifecycle reports |
| Owned effects | `common/scripted_effects/095_occupation_revolt_effects.txt` | Proposed incident orchestration and transaction calls |
| Owned trigger contract | `common/scripted_triggers/095_occupation_revolt_triggers.txt` | Proposed eligibility, phase, operation and target gates |
| Owned constants | `common/script_constants/095_occupation_revolt_constants.txt` | Proposed named tuning and thresholds |
| Owned API documentation | matching `095_occupation_revolt_effects.md` and trigger documentation | Inputs, outputs, scope, actual side effects and call sites |
| Decisions | `common/decisions/095_occupation_revolt_decisions.txt` | Proposed phase-appropriate actions and missions |
| Category | `common/decisions/categories/095_occupation_revolt_categories.txt` | Proposed native category ownership |
| Conditional restoration tree | `common/national_focus/095_occupation_revolt_focus.txt` | Proposed country-adapted tree only where safe and appropriate |
| Event-owned ideas | `common/ideas/095_occupation_revolt_ideas.txt` | Proposed consolidated emergency burden and actual lifecycle |
| Localisation | `localisation/english/095_occupation_revolt_l_english.yml` | Existing family, final copy to be written from direction |
| Shared achievement registry | `common/achievements/chaos_redux_achievements.txt` | Add verified unique IDs through existing owner pattern |
| Shared news | `events/_chaosx_news.txt` | Inspect actual Event 095 news consumer and avoid duplicate registration |
| Shared event framework | Resolve actual owners of category initialization, event type, actor context, log, details, settings and evolutions | Narrow integration only after full relevant reads |
| Country origins | Existing national identities and Event 006 origin/package owners | Reuse, preserve and repair missing fields only |
| Shared consequences | Current famine, migration, humanitarian, Deaths and Condemnation owners | Exact current public contracts and no duplicate physical changes |

All paths labeled proposed require collision inspection.
Do not create a helper without a real in-scope call site.
Do not move event orchestration into `chaosx_dynamic_effects.txt` simply because a shared file already exists.
Extract a genuinely reusable neutral operation only when existing and new consumers justify it, with a separate narrowly reviewed migration.

## Proposed helper contracts

| Internal operation | Scope and required inputs | Outputs and side effects |
|---|---|---|
| `or095_build_candidate` | Selector context, canonical identity, current origin registry, state ownership and control | Validated candidate or reason for rejection, no map or resource changes |
| `or095_prepare_actor_context` | Valid candidate and frozen incident record | Real claimant, occupier and state context for shared root logging, no fake actor fallback |
| `or095_build_opening` | Claimant, authentic home graph, organization, enabled capabilities, military resources | Exact state set, seat, force allocation and source inventory, no commit yet |
| `or095_quote_operation` | Acting country, exact target, phase, source variant, current shared price context | Immutable quote with conditions, required resources and validity generation |
| `or095_commit_opening` | Valid frozen quote and opening record | Supported country/war/state activation and one actual finite resource/force issue |
| `or095_complete_delivery` | Donor, recipient, route, variants, departure receipt and final disposition | Actual delivered, returned, captured and destroyed quantities with reconciliation |
| `or095_apply_local_outcome` | Exact incident, region, causal operation and actual result | Local organization and opportunity change once, no unrelated states |
| `or095_transfer_defection` | Verified local source, donor and recipient, exact native transfer path | Conserved source/recipient unit or inventory transition with no cloning |
| `or095_settle_government` | Current agreement, valid national profile, accepted participants | One governing settlement, Cohesion consequence and dated obligations |
| `or095_settle_war` | Actual war relationship, accepted terms, verified native legal operation | Exact permitted military and sovereign result, no unrelated peace |
| `or095_start_cascade` | Valid initiating success, enabled Evolution IV, finite real candidate pool | Origin-linked preparation opportunities, no recursive full scans |
| `or095_close_incident` | Terminal outcome, pending operation ledger, reservations and survivor facts | UI and temporary-state cleanup, exact refunds, retained episode history |

These names specify logical responsibilities.
They are not tested engine effects.
Before coding, map each to actual supported script scopes, native effects and existing repository helpers.
Where the installed engine cannot implement a promised transition, report the exact limitation and find a verified complete solution before marking that feature finished.

## State and scope discipline

Freeze actor, claimant, owner, controller, source state, destination state and operation identity before nested calls.
Do not rely on repeated `PREV` chains to retain their meaning through helper expansion.
Do not assume that entering another country scope rebinds ROOT.
A hidden recipient event can establish a required recipient ROOT only through a verified native pattern.
Persist incident identity across delayed work with durable records rather than treating a regular saved target as permanent storage.

Every temporary output is initialized by the caller and the helper's contract before a nested or repeated invocation.
The supplied shared helper documents explicitly warn that some equipment-removal helpers mutate their input temporary value and do not return a measured payment.
Those helpers cannot by themselves prove an exact debit or refund.
A measured debit or compatible universal-cost transaction is required.
Use inclusive affordability and checked fixed-point arithmetic before multiplications or unit conversions.

## Country, territory and unit commit order

Resolve the legal country and conflict path before altering the map.
Create the necessary valid country activation state and provisional seat in the order supported by native precedents.
Do not load a tree whose activation predicate is still false.
Keep real hostile field units valid through the chosen state-control transition.
Initialize missing country fields without overwriting surviving history.
Commit finite manpower and equipment to the approved force allocation exactly once.
Then expose the claimant's report, decisions, missions and details with the actual committed facts.

If an intermediate native operation cannot be made safely transactional, preflight every reversible requirement before crossing that boundary and provide a tested recovery path for each remaining failure.
Do not advertise rollback that the engine cannot perform.
The opening must never leave a paid-for but nonexistent country, an orphaned state, a duplicated army or an unrelated country at peace.

## Shared integration and save migration

Inspect the actual owners of `initialize_event_categories`, `get_event_type`, detail registration, debug visibility, event allowlists, actor context, evolution dispatch and logs.
Register Event 095's existing root through the correct Minor Repeatable and Liberations paths.
Medium severity is not a substitute for a required/optional cluster role classification when the framework uses that separate concept.
Read the exact cluster owner before assigning that field.

For saves with the old event already fired, preserve actual countries, armies and territorial outcomes.
Do not try to infer or confiscate all old spawned divisions from template name alone.
Mark legacy units as unproven for new exact-transfer and achievement receipts unless real identity evidence exists.
New incidents use the new bounded cache and occupation-episode history.
The legacy report's 50 political power and 15% war support are not replayed as migration rewards.

No catalog workbook or CSV change belongs to this planning delivery.
Implementation must use the authoritative workbook, preserve its structure, mirror verified final localisation and regenerate export-only CSVs through the project exporter.
Do not mark the event implemented from the existence of these specifications.
