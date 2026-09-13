# Event 35 Great Depression 2.0 recovery-depth addendum

## Disposition

This is the accepted implementation-depth addendum for the current Event 35 tranche.

The gameplay design delta is implemented in the Event 35 source, localisation, asset, documentation, and workbook surfaces.

No earlier improvement-loop addendum exists under `docs/plans/035_great_depression_plans/`.

The files in `subagent_handoffs/` are implementation and asset handoffs, not unresolved expansion addenda.

The accepted specification is already broad enough.

The design problem identified by this addendum was the missing delayed projects, aligned evidence, sparse relationships, outcome history, and bounded repeat behavior behind the accepted choices.

The implementation deepens the existing mechanic without adding a route, meter, country package, focus tree, map rewrite, dedicated scripted GUI, technology surface, or additional super-event.

Do not request another Event 35 improvement-loop pass for this design delta unless a new audit identifies a separate unresolved requirement.

## Ownership and implementation boundary

This document records the accepted design delta and its implementation handoff.

It does not authorize this planner to edit gameplay, localisation, workbooks, or assets.

The parent owns implementation, wiring, balance targets, localisation, achievement registration, asset wiring, final audits, and user-run live validation.

The exact design delta is named **Recovery Administration and Episode Evidence**.

It has five linked parts:

1. Make center stage, treatment, and project progress independent aligned facts.
2. Make relapse, repeat history, legacy selection, and diminishing returns operate on exact episode receipts.
3. Replace the shallow evolution flags with bounded sparse ledgers and staged resolution.
4. Freeze a compact episode summary before active cleanup.
5. Evaluate the six accepted achievements from immutable receipts rather than current flags.

## Evidence from the current implementation

### Source evidence

The table below is the pre-implementation review snapshot that motivated this addendum.

Its gap descriptions are historical rationale, not a statement that the current source still has each gap.

| Current surface | Concrete current behavior | Gap that this addendum closes |
| --- | --- | --- |
| `great_depression_register_initial_centers` in `common/scripted_effects/035_great_depression_effects.txt` | Iterates controlled states and accepts eligible states until the cap is reached. | The constants define industry, infrastructure, and population weights, but the registry does not use a deterministic ranked selection transaction. |
| `great_depression_center_state_ids`, `great_depression_center_stage_entries`, and `great_depression_center_project_entries` | The arrays are created at registration. | Later center actions and deterioration mostly mutate state flags and state variables without replacing the aligned array entries. |
| `great_depression_clear_center_state_flags` and center action effects | The helper clears stage and treatment-like flags together. | The specification requires physical stage and policy treatment to coexist independently. |
| `great_depression_reopen_selected_center`, `great_depression_rebuild_selected_center`, and route center effects | Costs are paid and the center is immediately reopened, restructured, or otherwise resolved. | Projects need authorization, mobilization, active work, interruption, certification, completion, and failure. |
| `great_depression_rebuild_selected_center` | Can add a civilian factory immediately when none exists. | A project may restore an exact Event 35 loss, but it must not mint a free permanent factory without a matching loss receipt. |
| `great_depression_update_registered_centers` | Center deterioration is driven mainly by national sustained-severity day counters. | Each center needs its own exposure duration, project protection, interruption, and final state. |
| `great_depression_update_phase_hysteresis` | A threshold crossing can set a relapse flag and move the national phase backward. | Relapse does not currently reopen exact proof obligations, pause projects, identify a cause, or preserve completed work. |
| `great_depression_add_recovery_legacy` | Adds the doctrine-specific permanent idea and can leave earlier doctrine legacies in place across repeated episodes. | Event 35 promises one bounded country legacy, a final Strong, Uneven, or Hollow result, and at most two state legacies or scars. |
| `great_depression_weekly_pulse` | The whole weekly delta is multiplied by `1.00`, `0.65`, or `0.40` after aggregate successful-action thresholds. | This can attenuate worsening as well as relief and does not diminish a repeated action family at one center. |
| `great_depression_apply_exposure` | Writes one target's current exposure variables and can convert it when the supplied stage is conversion-ready. | Financial Contagion needs a bounded source-target registry, relationship proof, time at stage, contributor attribution, merge-by-pair, and anti-ping-pong rules. |
| `great_depression_activate_social_collapse` and `great_depression_resolve_social_collapse` | Opens an organized strike at the severe gate and most response effects resolve it immediately. | Social Collapse needs staged movement and incident history with explicit peaceful, coercive, emergency, coup, separatist, and civil-conflict gates. |
| `great_depression_process_global_episode` | Moves Shock to Contraction, then Contraction to Recovery when one global proof value reaches one. | The accepted worldwide lifecycle has five qualitative stages, country pressure, positive and negative international transactions, a final proof period, and bounded cleanup. |
| `great_depression_increment_global_contribution` | A country is recorded once and three recorded countries can establish recovery proof. | Harmful and constructive actions currently share the same contribution path, and no recipient improvement or industrial weight is proved. |
| recovery cleanup | Clears active center arrays and many flags when recovery closes. | Achievement evaluation and final legacy allocation need a frozen episode summary before destructive cleanup. |
| `common/achievements/chaos_redux_achievements.txt` | No Event 35 achievement definitions are present. | The six accepted icon triplets exist, but exact eligibility and receipt-backed award logic are still absent. |
| `common/decisions/035_great_depression_decisions.txt` | Contains 75 decisions with `ai_will_do` and 15 missions that use activation, availability, timeout, and priority but have no mission-local `ai_will_do`. | The player surface needs phase and receipt filtering to keep a normal view near three to five actions and one to three live objectives, and mission AI must remain trigger-driven or receive an explicit auditable weight surface. |
| `great_depression_ai_movement_is_broad` and `great_depression_ai_movement_is_narrow` | Both currently evaluate to `always = yes`. | Several Social Collapse AI options can be suppressed by contradictory zero-factor gates. |

### Integration evidence

`events/035_great_depression.txt` constructs the reusable API contract in `chaosx.nr35.1` and calls `great_depression_allocate_receipt` and `great_depression_start_or_deepen`.

During this review, concurrent parent work added `great_depression_process_active_registry` to the existing global-host branches in `common/on_actions/chaosx_on_actions_chaos_meter.txt`.

The parent must preserve exactly one execution on each host-selection branch and verify that a host transition cannot process the registry twice on the same day.

The scheduler is source-reachable now, but downstream weekly lifecycle behavior is still not Event Viewer-proven because the viewer leaves the scripted-effect helpers unresolved.

### Read-only MCP evidence and limitations

The Event Chain Viewer was rerun against the exact selector `{ kind = event, eventId = chaosx.nr35.1 }` after implementation.

The bounded neighborhood render returned `EVENT_RENDERED_PARTIAL` with four selected nodes and no explicit blocker. Its manifest SHA-256 begins `77c8c00e`, its JSON SHA-256 begins `bb0cc4e`, its SVG SHA-256 begins `b9472e`, and its PNG SHA-256 begins `18b260`.

The render verifies the entry event and bounded neighborhood, but reports `validation = false` because large-workspace helper and lifecycle expansion remained deferred. A full event lint request timed out after 180 seconds. Downstream API lifecycle behavior therefore remains source-reviewed rather than fully Event Viewer-proven.

`hoi4.map_inspect` returned `MAP_INSPECTED` for a world catalog containing 1,081 states and produced an overview artifact.

The inspection artifact is `map-inspect.3221f1fb1857ee2a.json` with SHA-256 `9d80218e9af5fb97e029b9f1b1c0c31d67037037054136fbbf1c2f55fdd5c37b`.

That evidence supports a dynamic state-property selector and rejects fixed state IDs as a viable Event 35 design.

The map inspection also emitted thousands of inherited building-position and port diagnostics outside Event 35 ownership.

Those diagnostics do not expand this addendum into map repair work.

`hoi4.map_render` timed out after 180 seconds for both the state plus state-buildings, railways, and supply-nodes view and the lighter state plus state-buildings view.

The visual map-facing conclusion for center target selection is therefore unresolved.

The parent must rerun the state plus state-buildings render before accepting map-target click coverage or claiming the center selector is visually proven.

`hoi4.probability_inspect` now discovers 75 `decision_ai_will_do` candidates from `common/decisions/035_great_depression_decisions.txt`, with 19 required trigger families and no unresolved source identifiers. The source hash is `b43d26f1260255587cd3c4bc5c286f0fdd2c87929e6304fd38551af4f0905635`.

The bounded selector combining that path with `identifier = great_depression_category` returns a complete six-candidate doctrine pool with eleven required inputs and zero unresolved source identifiers. Its inspection artifact SHA-256 is `292ec9c28b1e17eb55b2e5d090b1212b47efb060eaa193c8271ae1ca21bc8a8f`.

The Event 35 option surface contains five weighted candidates across three option pools. Complete pair evaluations prove the coup response at `75%` execute and `25%` stand down, and regional autonomy at `60%` recognize and `40%` integrate. The corresponding analysis IDs are `probability-692a1a7bfc5ae12b70bc1223` and `probability-71187a323866dbc4a89aaa5d`.

The full named doctrine/action/contagion/social/global/evolution scenario audit and same-scenario comparison remain assigned to the read-only `chaosx_ai_probability_auditor`. Its final disposition belongs in the completion report rather than being inferred from the source inspection alone.

No focus-tree surface is included in this addendum.

No scripted GUI surface is included in this addendum.

No technology or doctrine-tree surface is included in this addendum.

The installed MCP package has no Technology Tree Viewer, which is a known tool limitation but does not block this technology-free plan.

## Historical and regional design basis

These connections are design anchors rather than a requirement to copy one country's institutions into every Event 35 target.

The mechanic must translate them into country-neutral administrative stages and relationship records.

| Historical connection | Design use | Boundary |
| --- | --- | --- |
| The 1933 United States bank holiday suspended transactions, examined institutions, and reopened banks in stages. [Federal Reserve History, Bank Holiday of 1933](https://www.federalreservehistory.org/essays/bank-holiday-of-1933) and [Emergency Banking Act of 1933](https://www.federalreservehistory.org/essays/emergency-banking-act-of-1933) | `great_depression_declare_temporary_bank_holiday_and_audit` should authorize an audit project. Reopening follows viability proof, recapitalization, and confidence certification rather than one immediate relief click. | Do not imply that every country creates the Federal Deposit Insurance Corporation or follows United States law. |
| The 1937 to 1938 United States recession followed policy tightening and the early withdrawal of support during an incomplete recovery. [Federal Reserve History, Recession of 1937-38](https://www.federalreservehistory.org/essays/recession-of-1937-38) | Relapse should preserve completed capacity, reopen unfinished proof obligations, and record premature withdrawal as one cause. It should not replay the opening shock. | The historical literature debates the relative fiscal and monetary causes, so the mechanic should use a general `support_withdrawal` cause rather than claim one universal explanation. |
| Public works and employment programs used sponsored projects and administrative records rather than instant national output. [National Archives, Works Progress Administration records](https://www.archives.gov/research/african-americans/record-groups/rg-069-wpa) and [National Industrial Recovery Act](https://www.archives.gov/milestone-documents/national-industrial-recovery-act) | Public works projects gain an early employment treatment, require a work period, and grant permanent state capacity only after certification. | No project may create a free factory before completion or without its documented reward contract. |
| The 1931 Creditanstalt failure propagated through bank, currency, sovereign, and short-term credit links. [IMF, Germany in the Interbellum](https://www.elibrary.imf.org/display/book/9781513511795/ch006.xml), [IMF, The Debt Web](https://www.elibrary.imf.org/view/journals/022/0055/001/article-A009-en.xml), and [BIS Second Annual Report](https://www.bis.org/publ/arpdf/archive/ar1932_en.pdf) | Financial Contagion must store the source-target relationship, exposure type, duration, and contribution share. Debt standstill and clearing actions resolve a specific link. | Adjacency alone is not sufficient exposure proof and a random unrelated country must not become a contagion target. |
| The 1933 London Economic Conference failed to settle essential monetary and credit disagreements, while the 1936 Tripartite Agreement represented narrower monetary coordination. [Office of the Historian, 1933 conference outcome](https://history.state.gov/historicaldocuments/frus1919Parisv13/ch17) and [1936 Tripartite financial stabilization agreement](https://history.state.gov/historicaldocuments/frus1936v01/ch15) | The global episode should distinguish failed conferences, fragmentation, and extractive actions from constructive clearing, reconstruction, supplier, and coordinated-demand transactions. | A conference decision alone cannot establish global recovery proof. |
| The Bonus Army confrontation and the 1934 strike wave show that unemployment protest, organized labor action, public sympathy, coercion, and political consequences were distinct stages rather than one generic unrest flag. [National Archives, Bonus Army](https://prologue.blogs.archives.gov/2020/07/15/the-1932-bonus-army-black-and-white-americans-unite-in-march-on-washington/) and [National Park Service, 1934 labor unrest](https://home.nps.gov/articles/000/the-saylesville-massacre-and-american-tradition.htm) | Social Collapse should record movement family, incident family, response, escalation, and final settlement separately. A strike can end in negotiation, repression, emergency government, or further crisis. | These examples are United States cases. Other countries should use the same abstract incident families with localised national framing. |

The main design inference from these sources is that recovery has administrative sequence, contagion follows proved relationships, unrest has actors and incidents, and a durable settlement needs proof after the dramatic decision.

## Addendum A: center stage, treatment, and project depth

### A1. One aligned center ledger

The existing `great_depression_center_state_ids` array remains the canonical index.

Every aligned center array must always have the same length and use the same index.

The parent should preserve the existing stage, project type, loss receipt, and factory baseline arrays and add these aligned arrays:

| Array | Stored fact |
| --- | --- |
| `great_depression_center_treatment_entries` | Current policy overlay, independent from physical stage. |
| `great_depression_center_project_stage_entries` | Project lifecycle stage. |
| `great_depression_center_project_start_day_entries` | Day authorization was accepted. |
| `great_depression_center_project_stage_day_entries` | Day the current project stage began. |
| `great_depression_center_project_due_day_entries` | Current due day after any valid pause adjustment. |
| `great_depression_center_project_pause_day_entries` | First continuous interruption day, or zero when not paused. |
| `great_depression_center_owner_country_entries` | Country scope that registered the center, used for episode continuity. |
| `great_depression_center_event35_civilian_loss_entries` | Exact civilian factory levels removed by Event 35 in that center. |
| `great_depression_center_event35_military_loss_entries` | Exact military factory levels removed by Event 35 in that center. |

State flags and dynamic modifiers become a derived display and modifier view of the ledger.

They must not be the source of truth for achievement evaluation or project progress.

Add one helper that replaces an aligned entry by index and one helper that rebuilds the state view from the aligned entry values.

Every center mutation must update the ledger first and then refresh the state view.

Do not clear treatment flags when changing physical stage.

Do not clear physical stage flags when applying a treatment.

### A2. Exact center dimensions

Physical center stage remains:

`Distressed -> Idled -> Shuttered -> Abandoned or Liquidated`, with `Reopened` as the positive physical resolution.

Only one physical stage may be active at a time.

Treatment is a separate enum:

| Treatment | Primary source decisions | Mechanical role |
| --- | --- | --- |
| None | No live intervention | No protection from local deterioration. |
| Emergency relief | `great_depression_protect_depression_center` | Halves the center's local deterioration contribution for 42 days. It does not reopen capacity. |
| Public works | `great_depression_launch_regional_works_program` | Starts employment relief during active work and permits infrastructure or state-capacity reward only after certification. |
| Strategic guarantee | `great_depression_designate_strategic_plant_network` and `great_depression_guarantee_essential_orders` | Protects a viable industrial baseline while orders remain funded. |
| Financial stabilization | `great_depression_declare_temporary_bank_holiday_and_audit` and `great_depression_recapitalize_viable_institutions` | Suppresses financial deterioration only after the audit reaches active work. |
| State direction | `great_depression_establish_emergency_production_board` and `great_depression_nationalize_failing_industry` | Protects production at a continuing administrative and input commitment. |
| Retrenchment | austerity and liquidation route actions | Reduces fiscal pressure while increasing local social and center abandonment risk. |
| Market clearance | liquidation-led route actions | Permits exact industrial loss and later reorganization without presenting the center as protected. |

### A3. Deterministic center registration

Initial registration must score every valid controlled state using the existing constants `center_industry_weight`, `center_infrastructure_weight`, and `center_population_weight`.

Use this exact formula:

`score = ((civilian factories + military factories + dockyards) * 4) + (infrastructure level * 2) + (population tier * 1) + inherited priority`.

Population tier is one point per full million residents, capped at 20.

Inherited priority is `1000` for the accepted Event 34 region and zero otherwise.

Add named constants for the population divisor, population cap, and inherited priority rather than hard-coding those values in the effect.

An inherited Event 34 region receives the existing inherited-region priority before ordinary scoring.

Ties resolve by lower state ID so the transaction is deterministic and testable.

Run one bounded best-candidate pass for each required center slot.

Each pass scans controlled eligible states, ignores states already in the registry, saves the highest-scoring candidate as an event target, appends it and every aligned default entry, then clears the temporary candidate before the next slot.

The normal cap remains one to three centers based on economy size.

The fourth center remains rare and requires the existing large-economy threshold or an inherited Event 34 region that would otherwise be excluded.

No fixed state list, country list, regional list, or adjacency heuristic should be added.

`great_depression_select_depression_center` must select an already registered center for management.

It must not register a non-center as a side effect.

Adding a later valid center must be a separate explicitly named transaction that appends every aligned array entry and raises the achievement requirement count.

### A4. Project state machine

Add `great_depression_center_project_stage` constants with these exact stages:

| Stage | Duration | Player meaning |
| --- | ---: | --- |
| None | No timer | No structural project exists. |
| Authorized | Immediate transaction | Cost, route ownership, center index, project type, and receipt are frozen. |
| Mobilizing | 21 days | Administration and inputs are assembled. No permanent reward is granted. |
| Active work | 70 days | The treatment overlay operates and interruption is checked. |
| Certification | 42 days | The center must remain controlled, viable, and below the specified failure condition. |
| Paused | Up to 28 continuous days | Loss of control or a proved input interruption suspends progress. |
| Completed | Terminal | The exact physical result and legacy candidate are written once. |
| Failed | Terminal | Sunk commitment, center pressure, and failure receipt are written once. |

The total uninterrupted project is 133 days, which fits inside the existing 135-day center mission contract.

The existing action cost family is charged once at authorization through the current dynamic cost engine.

Do not add a second hidden charge at stage transitions.

No refund is available after authorization because the commitment itself provides the early treatment benefit.

Preserve each current center action's total Severity value, but split structural relief across real progress:

| Current total | Authorization | Active-work entry | Completion |
| ---: | ---: | ---: | ---: |
| Protect Center `-3` | `-3` | Not applicable | Not applicable |
| Reopen or Rebuild `-5` | `0` | `-2` | `-3` |
| Restructure or Consolidate `-2` | `0` | `-1` | `-1` |
| Abandon or Liquidate `+4` | `+4` | Not applicable | Not applicable |
| Public Works or Strategic Rescue `-5` | `0` | `-2` | `-3` |

A failed structural project applies the existing mission-failure pressure `+5` once.

A project pauses when the center is not controlled by the episode owner or when its route-specific input proof fails.

If the interruption clears within 28 continuous days, resume the prior stage and shift the due day by the exact paused duration.

If it persists for 28 continuous days, fail the project.

A project also fails when Severity remains at `100` for 28 continuous days during active work or certification, when the state is removed from valid country continuity, or when the player deliberately abandons or liquidates the center through an incompatible route.

Relapse does not automatically fail a project.

It moves a project in certification back to active work and resets only its 42-day certification proof.

### A5. Existing decision conversion map

The parent should convert existing instant decisions to project transactions as follows:

| Existing decision | Project or treatment result | Completion effect |
| --- | --- | --- |
| `great_depression_protect_depression_center` | 42-day Emergency relief treatment, not a structural project | Center deterioration is reduced. Physical stage is unchanged. |
| `great_depression_reopen_idled_plants` | Reopen project | Idled becomes Reopened after certification. |
| `great_depression_rebuild_shuttered_center` | Rebuild project | Shuttered becomes Reopened. A factory may be restored only against an exact Event 35 loss receipt in this center and never above the frozen baseline. |
| `great_depression_restructure_or_consolidate_center` | Reorganization project | Center becomes Reopened with a restructured state legacy candidate, or Liquidated with an exact loss receipt when the chosen route owns liquidation. |
| `great_depression_abandon_depression_center` | Immediate terminal abandonment transaction | Center becomes Abandoned, records a permanent disqualifier, and cannot be silently removed from the registry. |
| `great_depression_launch_regional_works_program` | Public works project | Applies early employment treatment. Permanent infrastructure or capacity appears only at completion. |
| `great_depression_convert_works_into_lasting_capacity` | Lasting-capacity project available only after completed public works | Converts a temporary treatment into one state legacy candidate. It does not add a free factory. |
| `great_depression_designate_strategic_plant_network` | Strategic-rescue project | Protects the recorded industrial baseline and can end Reopened after certification. |
| `great_depression_consolidate_failing_industry` | Consolidation project | Records exact retained and lost capacity. It cannot both remove a factory and report no loss. |
| `great_depression_declare_temporary_bank_holiday_and_audit` | National 21-day audit proof that does not occupy a center project slot | Opens a staged audit. It does not immediately mark finance restored. |
| `great_depression_recapitalize_viable_institutions` | National 42-day follow-up available after audit viability proof | Grants Financial stabilization treatment only after the follow-up proof completes. |
| `great_depression_nationalize_failing_industry` | State-direction project | Transfers route ownership and begins active work. It does not instantly certify recovery. |
| `great_depression_auction_or_reorganize_failed_assets` | Asset-reorganization or liquidation project | Writes exact buyer, route, state, building type, amount, and final physical result. |

### A6. Center action surface

The category should expose at most one center selector, one currently valid center intervention, one live project mission, and one route-wide action at the same time.

A decision remains hidden when the selected center's physical stage, treatment, project stage, route, or episode receipt makes it invalid.

Project progress should use the existing mission surface and localisation substitutions.

No dedicated scripted GUI is needed.

## Addendum B: relapse, legacy, and diminishing returns

### B1. Relapse transaction

Add a relapse transaction that can execute only after Stabilization or Recovery began and Severity later crosses the existing relapse threshold.

It writes:

| Fact | Required value |
| --- | --- |
| `great_depression_relapse_count` | Increment once per distinct threshold crossing after a 42-day clear period. |
| `great_depression_relapse_day` | `global.num_days` at the accepted crossing. |
| `great_depression_relapse_cause` | One enum value from support withdrawal, policy whiplash, supplier failure, contagion return, social incident, project failure, or external shock. |
| `great_depression_relapse_source_receipt` | Receipt that supplied the cause, or zero for unresolved external shock. |
| `great_depression_relapse_proof_reset_count` | Number of proof windows actually reopened. |

The cause resolver checks exact recent receipts in this order: deliberate withdrawal, doctrine switch or policy whiplash, Event 34 supplier failure, Financial Contagion stage increase, Social Collapse incident, center project failure, then external shock.

Relapse must not apply the opening shock, rebuild the center registry, repay already paid project costs, or erase completed centers.

It clears the national stabilization and recovery proof day counters.

It returns a project in Certification to Active work.

It returns a Reopened center to Distressed only when that center lacks a completed structural receipt and has an expired treatment.

It reopens the existing `great_depression_prevent_a_relapse` mission under a new relapse sequence receipt.

### B2. Final recovery result

Before cleanup, derive one episode result:

| Result | Exact gate |
| --- | --- |
| Strong Recovery | Recovery proof succeeds, every required center is Reopened or approved positive restructured, no unresolved project remains, no center is Abandoned or Liquidated, and no Event 35 factory loss remains unrepaired. |
| Uneven Recovery | Recovery proof succeeds and national viability is preserved, but at least one center is Liquidated, one exact Event 35 loss remains, one state scar is required, or one project ended Failed. |
| Hollow Recovery | Recovery proof succeeds while any center remains Abandoned, a maximum-emergency or social-collapse scar remains unresolved, or the national recovery depended on withdrawal without a completed structural project. |

Recovery cannot close while a required center is still Idled, Shuttered, or in a nonterminal project stage.

### B3. One country legacy and at most two state outcomes

The country may have exactly one Event 35 recovery legacy after an episode.

Before applying it, remove every other Event 35 doctrine legacy idea.

The selected legacy is determined by final route ownership, final result, and completed project evidence rather than the last button clicked.

Repeated episodes may replace the legacy only when the new result is stronger or the final route legitimately changes after its own completed structural proof.

They must never stack all six doctrine legacies.

At most two registered centers receive a durable state outcome.

Priority order is one positive state legacy for the highest-value completed structural project, then one scar for the greatest exact unrepaired loss or failed project.

If no scar is required, a second distinct completed project may receive a positive state legacy.

No state can receive both the positive legacy and the scar from the same episode.

### B4. Per-family diminishing returns

Remove aggregate successful-action multiplication from the whole weekly Severity pulse.

Worsening from untreated conditions, incidents, contagion, project failure, or external shocks must always apply at full value.

Relief is diminished only when the same action family is repeated for the same center or national proof window:

| Repetition | Relief effectiveness | Rule |
| --- | ---: | --- |
| First accepted use | 100 percent | Full existing relief and receipt. |
| Second accepted use | 65 percent | Rounded through the existing fixed-point Severity helper. |
| Third accepted use | 40 percent | Full cost remains. |
| Fourth use | Blocked | Remains blocked until a new phase, relapse sequence, project stage, or distinct center opens a new proof window. |

Use one bounded sparse action-use registry with aligned episode ID, action family, center index or national window ID, proof-window ID, and accepted-use count arrays.

The lookup key is `episode ID + action family + center index or national window ID + proof-window ID`.

A doctrine switch does not reset it.

A repeat Event 35 episode receives a fresh tactical action ledger, but permanent legacy improvement remains bounded by B3.

## Addendum C: Financial Contagion

### C1. Sparse source-target registry

Use the existing global source cap and create one global row per material source-target pair.

The row must contain aligned values for source country token, source episode ID, target country token, exposure type, exposure stage, contribution score, stage day, last action day, conversion receipt, and resolved flag.

Valid exposure types are direct credit, trade dependence, supplier dependence, clearing or currency link, distressed asset ownership, and inherited Event 34 contract.

At least one type must have explicit relationship proof before a row is created.

Use exact base contribution scores of direct credit `4`, inherited Event 34 contract `4`, supplier dependence `3`, clearing or currency link `3`, trade dependence `2`, and distressed asset ownership `2`.

When several relationship proofs exist for one pair, retain the highest-scoring type and add one breadth point, capped at a row contribution score of `5`.

Broad `exists` and `not ROOT` target validation is insufficient.

When the same source-target pair is supplied again, merge into the existing row and update contribution and stage.

Do not append a duplicate row.

When several sources pressure one target, retain separate rows and calculate each source's material share.

This share is required for `Containment Line` attribution.

A dominant source is the largest row and at least 40 percent of the target's total contribution.

A secondary material source is any other row at or above 20 percent.

### C2. Stage timing and conversion

Financial Contagion retains the accepted stages Observed, Pressured, Dependent, Conversion Ready, Converted, and Resolved.

Stage advance requires both exposure duration and target vulnerability:

| Advance | Minimum duration | Additional gate |
| --- | ---: | --- |
| Observed to Pressured | 28 days | Source remains in Deep Depression or worse. |
| Pressured to Dependent | 42 days | Target has a proved trade, credit, supplier, or asset dependency and has not completed a matching protection action. |
| Dependent to Conversion Ready | 42 days | Target's total active contribution score reaches `6` and at least one source remains dominant or secondary material. |
| Conversion Ready to Converted | 14-day warning | Target remains valid and no containment transaction resolves the dominant links. |

One source-target row may advance at most one stage per weekly pulse.

A converted target cannot immediately expose its source back through the same receipt.

Require a distinct relationship type and a 42-day anti-ping-pong cooldown before reverse propagation.

Conversion constructs the existing reusable Event 35 API contract exactly once and stores the returned crisis receipt in the row.

### C3. Relationship actions

Ring-fence, credit, standstill, clearing, diversification, rescue, asset sale, and withdrawal decisions must target a proved row.

Every transaction records provider cost, recipient change, row stage before and after, and resolution result.

Provider costs occur in the provider scope.

Recipient Severity relief or exposure reduction occurs in the recipient scope.

An action cannot set the row Resolved unless it lowers the exposure stage below material or the source episode recovers.

Deleting, annexing, or invalidating a target marks the row Invalidated and disqualifies containment mastery rather than silently removing it.

## Addendum D: Social Collapse

### D1. Movement and incident ledger

Social Collapse needs one primary movement record, at most one secondary rival in a large or fragmented country, and an append-only incident summary for the episode.

Store primary and secondary movement family, home center index, opening day, current stage, support band, last response, last incident family, emergency-government lifecycle, coup receipt, separatist receipt, civil-conflict receipt, and final settlement.

Use the accepted movement families: trade-union and social-democratic coalition, communist council movement, syndicalist or factory-occupation movement, nationalist or fascist mass movement, military emergency faction, monarchist or traditional-authority restoration group, regional autonomy or separatist movement, business and creditor emergency coalition, and rural protest when exact agricultural or food-pressure proof exists.

Resolve the primary family deterministically in this order when the evidence exists: valid regional identity plus an abandoned, unequally rescued, or repressed center, exact rural or food-pressure adapter, military discontent plus very low stability, communist council receipt, communist-backed occupation receipt, strong fascist or nationalist party support, valid monarchist or traditional institution, finance or liquidation route plus creditor distress, then the trade-union and social-democratic fallback.

An optional secondary rival requires at least three registered centers or a valid fragmented-country receipt and must use the next valid family from a different institutional base.

Do not invent a person, tag, party, regional identity, or grounded portrait to fill a movement role.

Do not randomize movement selection without a declared pool and probability audit.

### D2. Stages and response timing

Use the existing qualitative enum as a strict state machine:

`Grievance -> Organized Strike -> Political Mandate -> Emergency Government -> Coup Crisis or Separatist Crisis -> Civil Conflict Eligible -> Resolved`.

One major incident family is attached at each escalation rather than treated as the stage itself.

Major incident families are general strike, occupation, riot, mutiny, and government crisis.

Negotiation, employment compact, security deployment, occupation breaking, council recognition, emergency government, socialization, and property-credit guarantee write response receipts and modify the next 28-day proof window.

They do not immediately call `great_depression_resolve_social_collapse` unless the response's proof window has already completed.

A peaceful settlement requires 42 days without a new major incident and one completed negotiated, employment, or constitutional response.

Coercive containment requires 42 days without a new incident but writes a scar candidate and cannot satisfy The Social Peace if permanent emergency rule remains.

A coup or separatist crisis requires Severity at least `90` for 98 continuous days, Government Crisis stage, Stability below 30 percent, a valid organized movement, one failed major response or mandate mission, no protected recent-civil-war aftermath, and valid actors.

A coup requires elite or military support and no coherent regional base.

A separatist crisis requires an existing valid regional identity or tag, a registered center in that region, and a coherent territorial base.

If no valid regional actor exists, use an autonomy or regional-government crisis and do not create a fallback tag.

Event 35 civil-conflict eligibility requires a coup or separatist receipt plus a second failed 42-day response window and valid territory and force-package proof.

No baseline strike before Evolution II can satisfy the achievement incident gate.

### D3. AI predicates

Replace the two placeholder movement predicates with mutually exclusive evidence:

- `great_depression_ai_movement_is_broad` is true for a national support band, incidents in two or more centers, a valid secondary rival, or Political Mandate and above.
- `great_depression_ai_movement_is_narrow` is true for one home center, one incident family, no secondary rival, and a stage below Political Mandate.

The predicates may both be false when evidence is unresolved.

They must never both be true.

## Addendum E: The Second Great Depression and global recovery

### E1. One five-stage global episode

Retain one bounded global episode with the existing five stages:

| Stage | Entry gate | Exit gate |
| --- | --- | --- |
| Shock | First valid worldwide activation transaction | 30 days and initial country-pressure registration completed. |
| Contraction | Shock exits | Materially affected country count and supplier-risk snapshot are frozen. |
| Coordination | At least two valid constructive international transactions or one valid major conference transaction | Reconstruction score reaches the threshold and no critical fragmentation lock remains. |
| Recovery | Reconstruction threshold reached | 120 continuous proof days with sufficient industrial recovery and no major Event 34 supplier collapse. |
| Retired | Recovery proof succeeds or a documented forced-cleanup blocker ends the episode | All active pressure rows and temporary global modifiers are cleaned once. |

### E2. Country pressure registry

Use a bounded global country-pressure registry rather than iterating the world every pulse.

Register a country only when Event 35 is active, it is materially exposed through Financial Contagion, it is a proved Event 34 supplier, or it performs a global episode transaction.

Each row stores country token, baseline civilian and military factory count, baseline Severity or non-conversion state, current pressure band, contribution class, contribution value, recipient improvement receipts, supplier-collapse receipt, and last update day.

Updates operate only over registered rows.

### E3. Constructive, protective, and fragmenting transactions

Global decisions must not all call one contribution increment.

Classify them:

| Class | Existing decisions | Global effect |
| --- | --- | --- |
| Constructive | regional clearing agreement `+1`, coordinated public works `+2`, successful international debt conference `+2`, reconstruction supplier compact `+2`, successful global recovery conference `+2`, emergency trade clearing `+1`, reconstruction and employment fund `+2`, coordinated industrial demand `+2` | Adds reconstruction value only after provider payment and a proved recipient or network improvement. |
| Protective | guarantee property and credit, protect domestic market | Reduces the actor's pressure or one linked target's pressure but contributes little or no global reconstruction. |
| Fragmenting | protectionist bloc, competitive devaluation or currency break, withdraw from international commitments | Adds one fragmentation point, raises supplier risk when linked, and never increments global recovery proof. |

Conference failure must be a real outcome when participation, supplier, currency, or reconstruction evidence is insufficient.

The 1933 conference precedent supports failure without creating a separate super-event.

### E4. Industrially weighted recovery proof

Replace the current three-contributor proof with an industrially weighted threshold.

Use each registered country's frozen usable civilian and military factory count as its weight, with a per-country cap of 30.

Add centralized constants for the weight cap, required constructive value `6`, recovered-weight share `0.60`, maximum critical-weight share `0.15`, and final proof duration `120` days.

The Recovery stage begins only when constructive value reaches `6`, constructive transactions have improved at least one major recipient, at least three distinct provider countries have valid constructive receipts or every valid provider has contributed when fewer than three exist, recovered registered weight reaches at least 60 percent, critical registered weight is no more than 15 percent, and no critical supplier row remains in collapse.

The final proof lasts 120 continuous days.

A new major conversion, a critical Event 34 supplier collapse, or weighted pressure returning above the recovery band resets the proof day without returning the world to Shock.

On successful retirement, apply the accepted bounded Chaos relief once and record the global completion transaction.

## Addendum F: frozen episode summary and achievements

### F1. Freeze before cleanup

Add `great_depression_freeze_episode_summary` and call it before any active center array, relationship row, project flag, or phase proof is cleared.

The summary must be compact and durable.

It stores episode ID, caller type, source event and episode, opening Severity, peak Severity, final Severity, final route, final Strong or Uneven or Hollow result, original center count, later center count, reopened count, positive restructured count, abandoned count, liquidated count, unresolved count, civilian loss total, military loss total, repaired Event 35 loss total, maximum-emergency result, relapse count, Financial Contagion result, Social Collapse result, global episode contribution result, and continuity owner.

Freeze the original center IDs in a durable achievement array before the first active center mutation.

Later valid center additions use a separate durable array and become requirements for Every Center Reopened.

Do not retain every weekly pulse after cleanup.

Retain only exact terminal receipts and the compact summary needed by achievements, inherited Event 34 recovery contracts, and repeat history.

### F2. Six exact achievement evidence contracts

| Achievement | Required immutable facts | Disqualifier facts |
| --- | --- | --- |
| Back to Work | Independent caller, severe opening, frozen original centers, all original centers positive, zero Event 35 civilian and military loss, same-episode recovery proof. | Event 34 inherited source, Event 35 loss, abandonment or liquidation, invalid transfer continuity, debug or late tracking. |
| Every Center Reopened | Peak Severity `100`, maximum-emergency success, at least three centers or every valid smaller-economy center, original plus later center arrays all positive, Strong or Uneven result. | Abandoned, Liquidated, Shuttered, unresolved, invalidly removed, forced cleanup, transfer bypass. |
| Containment Line | Financial Contagion active, deep source Severity, scaled material foreign exposure count, at least one proved containment action, every outgoing material row Contained or source-recovered, no attributable conversion, source recovery. | Material conversion attributed to the player row, invalidated target cleanup, evolution disabled after exposure, force cleanup, ownership loss. |
| The Social Peace | Evolution II active, peak Severity at least `90`, at least one qualifying major incident family after activation, peaceful settlement proof, no coup, no Event 35 civil conflict, no permanent emergency rule. | Permanent emergency or military government, coup, separatist conflict, civil conflict, debug clear, ownership move. |
| Lean but Standing | Final liquidation-led route, exact center consolidation or auction receipt, exact Event 35 civilian or military loss with state and type, protected national industrial floor, no political collapse, same-episode recovery proof. | Loss from another system only, no exact Event 35 loss, route ownership broken, viability-floor failure, forced completion. |
| Recovery of Nations | Global episode ID, substantial constructive transaction value, at least one major recipient improvement attributable to the player, player recovery or non-conversion, Recovery stage, 120-day proof, no final-period major supplier collapse, independent valid player. | Duplicate or refunded contribution, contribution after proof, player-caused critical supplier collapse, forced global end, invalid continuity. |

Achievement evaluation runs in the same completion transaction after the summary is frozen and before active cleanup.

Awards are idempotent.

An achievement helper must test its own eligibility flag, evidence receipt family, and disqualifier family.

Current dynamic modifiers and current center flags are never sufficient evidence.

## Exact implementation surfaces for the parent

| File or surface | Required parent work |
| --- | --- |
| `common/script_constants/035_great_depression_constants.txt` | Add treatment, project-stage, relapse-cause, recovery-result, contribution-class, incident-family, project timing, exposure timing, anti-ping-pong, global proof, and action-family window constants. Keep all tuning centralized. |
| `common/scripted_effects/035_great_depression_effects.txt` | Add aligned-array replacement and view refresh helpers, deterministic center scoring, per-center pulse processing, relapse transaction, final result resolver, legacy replacement, sparse contagion/global registries, global proof, summary freeze, and cleanup order. |
| `common/scripted_effects/035_great_depression_decision_effects.txt` | Convert instant center and evolution actions into authorization, response, relationship, contribution, and receipt transactions. Ensure provider and recipient scopes pay and receive the correct side of each effect. |
| `common/scripted_triggers/035_great_depression_triggers.txt` | Add coherent aligned-ledger checks, project completion and failure gates, relapse-cause evidence, final result gates, sparse-row validation, and immutable achievement evidence triggers. |
| `common/scripted_triggers/035_great_depression_decision_triggers.txt` | Correct center selection to existing registered centers, add separate later-center registration if still required, and gate actions by stage, treatment, project, route, and receipt. |
| `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt` | Enforce three to five visible actions, one to three objectives, exact relationship targets, mutually exclusive movement predicates, and constructive versus fragmenting global gates. |
| `common/decisions/035_great_depression_decisions.txt` | Keep the accepted decision IDs but route them to staged project and ledger effects. Remove broad unrelated evolution targets. Update mission activation and completion around project stages and proof windows. |
| `common/ideas/035_great_depression_ideas.txt` | Make country legacies mutually replacing and add only accepted state legacy or scar modifier consumers. |
| `common/dynamic_modifiers/035_great_depression_dynamic_modifiers.txt` | Add temporary treatment and project-stage views only where a dynamic modifier is materially useful. Avoid duplicating the center ledger in modifiers. |
| `common/achievements/chaos_redux_achievements.txt` | Register the six accepted achievements against exact scripted triggers after their evidence layer exists. |
| `common/on_actions/chaosx_on_actions_chaos_meter.txt` | Preserve the current global-host calls to `great_depression_process_active_registry`, prove one execution per day across host-selection branches, and do not add another all-country scheduler. |
| `events/035_great_depression.txt` | Preserve the current API entry. Order recovery completion as freeze summary, evaluate inherited and achievement receipts, apply legacy, clean active state, then emit report or news. |
| Event 34 adapters | Consume the frozen Event 35 recovery receipt for `The Long Fall` and supplier-collapse proof. Do not duplicate Event 34's achievement ownership. |
| Event 35 documentation | Document aligned arrays, sparse registry bounds, state transitions, cleanup, project interruptions, repeat rules, and achievement transaction order. |

The parent must also update localisation, decision effect tooltips, achievement text, workbook rows, and asset wiring in the implementation change, but this planning subtask does not edit those surfaces.

The six Event 35 achievement icon triplets already exist under `gfx/achievements/`.

The existing generated art, icon, text, and audio handoffs should be reviewed and wired by the parent rather than replaced by this mechanic pass.

## AI and probability contract

Every changed `ai_will_do`, mission score, timing weight, random selection, or custom weighted pool requires the standard baseline audit, owner-applied patch, and same-scenario `hoi4.probability_compare` pass through `chaosx_ai_probability_auditor`.

This planner does not choose new balance targets.

The parent must preserve the accepted scenario names and evaluate at least:

- Center, action, and doctrine behavior: `ACT-01` through `ACT-05` and `DOC-01` through `DOC-07`.
- Financial Contagion: `CTG-01` through `CTG-10`.
- Social Collapse: `SOC-01` through `SOC-05`.
- Global episode: `GLB-01` through `GLB-10`.
- Evolution timing: `EVO-01` through `EVO-08`.

The bounded source audit produced and closed these implementation findings:

- `great_depression_ai_action_is_affordable` now requires every nonzero resource component to be payable, matching the custom cost trigger instead of accepting any one affordable component.
- Broad and narrow Social Collapse movement predicates are mutually exclusive and evidence-based; unresolved evidence may make both false but can never make both true.
- Relationship cooldowns, source-episode receipts, conversion attribution, and propagation depth prevent merged-row, repeated-aid, and recursive-conversion farming.
- Global recovery uses classified constructive and fragmenting transactions, industrial weighting, final-period supplier proof, and episode-scoped receipts; supplier collapse resets proof without replaying the super-event.
- Missions have explicit `ai_will_do` blocks and use activation plus mission-state gates without paying their mapped cost twice.

Required behavioral checks are:

1. An AI never selects a project that its center stage cannot start.
2. An AI does not abandon the last viable center unless the approved liquidation survival conditions are all true.
3. A broad movement prefers a broad settlement or national employment response over a narrow coercive response when both are affordable.
4. A narrow movement does not starve all valid responses through contradictory zero factors.
5. Constructive global actions can rank during Coordination and Recovery preparation.
6. Fragmenting actions never improve global recovery proof.
7. AI can finish one structural project before opening another center project unless emergency conditions justify a switch.
8. A relapse does not cause repeated doctrine switching solely to reset action returns.

The adapter-discovery blocker is closed: the MCP now exposes 75 decision-weight candidates and a complete bounded six-doctrine pool. Full named-scenario ranking and the same-scenario comparison remain pending the final read-only auditor report.

## Acceptance scenarios

### Center ledger and projects

1. Start an independent episode in a country with at least four eligible industrial states and verify the deterministic score selects the same one to three centers on repeated identical setup.
2. Verify an inherited Event 34 region receives its priority without creating more than the permitted fourth center.
3. Change a center from Distressed to Idled while Emergency relief is active and verify exactly one physical stage and one treatment remain.
4. Start a Reopen project and verify payment occurs once, no immediate Reopened stage appears, and project stages occur at days 0, 21, 91, and 133.
5. Lose control for 14 days and regain it, then verify the project resumes and the deadline shifts by exactly 14 days.
6. Lose control for 28 continuous days and verify one failure receipt, one pressure consequence, no refund, and no duplicate failure.
7. Rebuild a center with no Event 35 factory-loss receipt and verify no civilian or military factory is created.
8. Rebuild a center with one exact Event 35 civilian loss and verify restoration cannot exceed one or the frozen baseline.
9. Verify every aligned center array has identical length after initial registration, later valid addition, stage change, project failure, and recovery freeze.
10. Rerun the MCP state plus state-buildings render and verify the center target surface against the selected state view. This acceptance remains unresolved after two 180-second render timeouts.

### Relapse, legacy, and returns

1. Enter Stabilization, withdraw support through a receipt-backed action, cross Severity `50`, and verify relapse cause `support_withdrawal`, no opening shock, and no center registry rebuild.
2. Relapse during Certification and verify only the certification window resets while completed work and paid cost remain.
3. Complete Strong Recovery twice under different doctrines and verify only one Event 35 country legacy exists.
4. Complete an Uneven recovery with one failed project and one exact loss, then verify no more than two state outcomes are applied and one is the highest-priority scar.
5. Repeat one center action family four times in the same proof window and verify relief is 100, 65, and 40 percent, with the fourth blocked.
6. Apply a worsening weekly condition after three successful actions and verify the worsening value is not multiplied by the diminishing-return factor.

### Financial Contagion

1. Attempt exposure against an unrelated country and verify no row is created.
2. Apply the same proved source-target relationship twice and verify one merged row rather than two rows.
3. Maintain one link through 28, 42, and 42-day windows and verify at most one stage advance per pulse.
4. Resolve a dominant link during the 14-day conversion warning and verify no Event 35 conversion call occurs.
5. Convert a target and verify one reusable API receipt, one Chaos change, and one row conversion receipt.
6. Attempt reverse propagation through the same relationship inside 42 days and verify it is blocked.
7. Pay aid from a provider and verify the provider loses the cost, the recipient receives the improvement, and the row records both sides.

### Social Collapse

1. Open a narrow one-center strike and verify `movement_is_narrow` is true while `movement_is_broad` is false.
2. Expand to a national support band or add a valid secondary rival and verify the predicates reverse without both becoming true.
3. Choose negotiation and verify the crisis remains open for a 42-day settlement proof rather than resolving immediately.
4. Fail a response at Severity `90` and verify coup or separatist eligibility does not occur before 98 continuous days and every other extreme-outcome gate is true.
5. Fail the second 42-day response window and verify civil-conflict eligibility writes one receipt without immediately starting conflict unless the accepted outcome action executes.
6. Keep emergency government after national recovery and verify The Social Peace remains disqualified.

### Global episode

1. Activate a worldwide episode twice and verify one global episode ID and one super-event emission.
2. Register countries from active crisis, exposure, Event 34 supply, and transaction paths and verify no unregistered world iteration occurs.
3. Execute Protectionist Bloc, Currency Break, and Withdrawal and verify none increments constructive reconstruction value.
4. Execute a constructive aid transaction without recipient improvement and verify it does not count toward final proof.
5. Improve one major recipient and enough weighted affected countries, then verify entry to Recovery.
6. Cause a major supplier collapse on day 119 of final proof and verify the 120-day proof resets without replaying Shock.
7. Complete final proof and verify one bounded Chaos relief, one global completion receipt, and one cleanup transaction.

### Achievement evidence

1. Evaluate all six achievements after `great_depression_freeze_episode_summary` and before active cleanup.
2. Verify the same summary and receipt set cannot award an achievement twice.
3. Transfer a required center to bypass failure and verify the relevant continuity disqualifier persists after cleanup.
4. Remove a factory through combat with no Event 35 loss receipt and verify it does not satisfy Lean but Standing or disqualify Back to Work.
5. Remove a factory through a validated Event 35 liquidation transaction and verify exact state, building type, amount, route, and receipt survive cleanup.
6. Attribute a foreign conversion among multiple sources and verify Containment Line disqualifies only material source contributors.
7. Record a baseline pre-Evolution-II strike and verify it cannot satisfy The Social Peace's qualifying incident requirement.
8. Record a constructive global transaction after Recovery proof is already complete and verify it cannot satisfy Recovery of Nations.

## Completion gates for this addendum

The parent may mark this addendum implemented only when all of the following are true:

- Every center mutation updates the aligned ledger and derived state view.
- Center stage, treatment, and project stage are separate facts.
- Structural center decisions are delayed, interruptible, and capable of failure.
- No center action creates a factory without an exact restoration or accepted completion contract.
- Relapse preserves history and completed work while resetting only the required proof.
- Event 35 permanent country legacies are mutually replacing and state outcomes are capped at two.
- Diminishing returns reduce repeated relief only and never suppress worsening.
- Financial Contagion uses proved sparse source-target rows with attribution.
- Social Collapse uses staged movement and incident receipts with strict extreme-outcome gates.
- The worldwide episode uses five stages, classified transactions, industrial weighting, and 120-day final proof.
- The episode summary freezes before cleanup.
- All six achievements evaluate exact immutable evidence.
- `great_depression_process_active_registry` executes exactly once per day through the existing global-host scheduler even during a host transition.
- The Event Viewer resolves the Event 35 scripted-effect chain or the unresolved helper limitation remains explicitly carried as a blocker.
- The state plus state-buildings map render succeeds and verifies the center target surface.
- The AI probability auditor completes baseline and post-change comparison for the same named scenarios.
- Parent-owned localisation, workbook, assets, documentation, and achievement registration match the implemented facts.

## What must not be added

Do not add a second public recovery meter.

Do not add another doctrine route.

Do not add a focus tree, formable, country package, or map rewrite.

Do not add a dedicated scripted GUI for center cards or global recovery.

Do not add another super-event beyond the accepted worldwide activation.

Do not add technologies or doctrine-tree nodes.

Do not model every historical relief institution as its own decision.

Do not create a global daily, weekly, or monthly all-country iteration.

Do not turn relationship proof into geographic adjacency alone.

Do not retain unlimited historical arrays after episode cleanup.

These additions would broaden the event without fixing the current depth and evidence gaps.

## Promotion and parent handoff

This file remains under `docs/plans/035_great_depression_plans/` as the accepted implementation handoff and evidence record.

If accepted, promote the relevant rules rather than copying the entire addendum into one file:

- Merge center ledger, projects, relapse, legacy, and repeat rules into specification parts 3 and 4 and the state lifecycle map.
- Merge Financial Contagion rules into part 5 and the reusable crisis API.
- Merge Social Collapse rules into part 6.
- Merge global registry, transaction classes, and proof into part 7.
- Merge weighted audit requirements into part 9 and the AI probability matrix.
- Merge frozen summary and achievement evidence into part 11.
- Update the package manifest and full specification after those source-of-truth parts are reconciled.

The implemented design delta addressed shallow transaction depth and missing durable evidence behind an already broad accepted surface.

The proposed expansion is one Recovery Administration and Episode Evidence layer, not a new content route.

The research basis is staged bank reopening, administrated public works, premature-withdrawal relapse, relationship-specific 1931 contagion, distinct labor and political escalation, and the contrast between failed and successful international coordination.

Implementation surfaces are listed above.

The remaining validation questions are external to the source implementation: completion of the named probability comparison, full MCP helper and lifecycle expansion after the 180-second lint timeout, map-facing visual review after the state render timeouts, live visual review of the generated assets, and scheduler single-execution proof across host transitions.

No gameplay requirement from this improvement addendum remains queued.
