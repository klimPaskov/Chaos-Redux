# Event 012 Gods lifecycle fix review, 2026-10-03

## Verdict and boundaries

No remaining source defect was found in the restored L1–L3 repair at the source revisions below.
The bounded repair is implemented in source and suitable for the parent's lifecycle tranche review, with required MCP and engine acceptance unconfirmed.
This handoff does not establish completion of all Gods mechanics or Event 012.
The parent's latest instruction explicitly requests immediate manual findings without waiting for slow MCP receipts.

The acceptance basis is the parent's explicit assignment to preserve participant history, retain permanent opt-out through loss and succession, remove interrupted review permissions, retain completed reparations and paid-offer history, require bilateral accepted reconciliation to clear opt-out, and use the explicit participant/host territory predicate.
The prior findings in `012_africa_gods_lifecycle_audit_2026-10-03.md` and the implementation handoff `012_africa_gods_lifecycle_fix_2026-10-03.md` were read.
No simplification or new gameplay fallback was introduced by this review.
Only this new review handoff was written.
No gameplay, other documentation, skills, assets, workbook, Git index, or commit was changed, and HOI4 was not launched.
Mobile/artillery implementation, weighted balance, and U1–U3 remain separately owned.

## Completion status by bounded surface

| Surface | Manual source status | Required evidence limit |
| --- | --- | --- |
| L1 same-host revival | Confirmed against restored source | Native state persistence and MCP lifecycle coverage unconfirmed |
| L2 durable opt-out after loss/successor | Confirmed for a previously defiant participant | Successor activation and the separate victor/re-legitimation promise are not established by this repair |
| L3 interrupted paid reconciliation | Confirmed against cleanup, payment, deadline, and acceptance callers | Native mission execution and MCP lifecycle coverage unconfirmed |
| Participant territory Wrath floor | Confirmed explicit participant-controlled host-core predicate | Native controller/core behavior unobserved |
| Lifecycle documentation | Current wording matches this patch | Broader documented gaps remain open |

## L1: same-host revival preserves history

`common\scripted_effects\012_africa_gods_lifecycle_effects.txt:4–35` recognizes an existing `gods_of_africa_history_count`, including zero, as an initialized ledger.
Only a participant with neither that proof nor the initialization flag receives zeroed counters and cleared kind/day arrays.
Existing Wrath and its band are retained, with initialization only when each variable is absent.

`common\scripted_effects\012_africa_gods_effects.txt:310–352` now calls that helper instead of unconditionally resetting history during registration.
Registration binds the current host generation, clears live review state independently, restores live defiance from durable opt-out, inserts the participant, and refreshes its floors.
The complete archive and clean bodies at `388–495` and `2934–3024` retain the hidden history arrays and cumulative counters.
The bounded review at `190–218` can register the recovered eligible participant again without deleting that ledger.

The reviewed trace is prior conduct, archive or cleanup, same-country recovery, and re-registration under the same active host.
It also covers an existing empty ledger and a previously reconciled participant with retained prior-defiance history.
No source path in this trace resets the existing ledger or Wrath merely because registration runs again.
The aligned append at `715–740` continues recording kind and day together.
These are manual source traces, not executed engine scenarios.

## L2: live cancellation does not pardon permanent defiance

Defiance sets both the live flag and `gods_of_africa_permanent_opt_out` at effects `2730–2743`.
The migration helper at lifecycle effects `37–42` remembers an existing live defiance flag before cleanup can remove it.
Register, archive, clean, and host-loss cancellation invoke it at effects `315`, `391`, `2936`, and `3178`.

Host loss still closes the live registry, clocks, participant authority, missions, and active contracts at effects `3135–3173` and `3175–3258`.
Cancellation may clear live defiance at `3212`, but it does not clear the durable opt-out.
Later registration restores live defiance at `333–336` before ordinary demand dispatch.
`common\scripted_triggers\012_africa_gods_triggers.txt:246–264` excludes live defiance from ordinary demands, so a generation change or successor enrollment does not pardon the participant in this trace.

A repository search of `common` and `events` found the sole explicit durable-opt-out clear in `gods_of_africa_complete_reconciliation` at effects `2797`.
That resolver requires an active current participant, live future reconciliation deadline, paid reparations, and a pending offer at effects `2788–2812` and triggers `533–545`.
Its live acceptance caller is the host target decision at `common\decisions\012_africa_gods_decisions.txt:1042–1073`, which tests the participant through FROM and invokes acceptance in FROM scope.
The reconciliation mission has a completion helper at decisions `77`, but its availability is always false at `66`, so it does not provide a source-enabled self-approval route.
Mission removal executes neither completion nor timeout effects according to the installed documentation cited below.
Historical defiance entries and counters are retained when accepted reconciliation appends its own kind-9 record.

This finding addresses the durable opt-out of a previously defiant participant.
It does not settle the full spec's independent victor/restoration promise at `012_gods_of_africa_full_spec.md:1075–1077`, prove successor activation, or infer country-object inheritance.

## L3: interrupted payment loses permission and keeps the transaction record

`gods_of_africa_clear_reconciliation_review`, lifecycle effects `46–55`, removes the mission, clears pending/payment/offer/failure-report flags, and clears start, due, and retry dates.
It is called during registration, archival, participant cleanup, and unifier-loss cancellation before obsolete live authority survives those paths.
It contains no refund, reverse transfer, pardon, or history deletion.

The payment effect at core effects `3571–3582` retains the existing real participant debit and host credit.
After payment it sets paid/offer permission, requests `reconciliation_offer`, and appends the record through the existing history helper.
`common\script_constants\012_africa_gods_constants.txt:511` defines that kind as 12, distinct from accepted reconciliation kind 9.
The payment predicate at triggers `1009–1014` prevents another payment within the same already-paid or offered review.
Cleanup removes permission to consume an interrupted payment as a current accepted offer, while the completed transfer and kind-12 record remain.
A later review can charge a fresh offer under the existing contract, without refunding the interrupted one or erasing its history.

Triggers `533–545` now require a due-day variable and a strictly future deadline.
Missing deadlines no longer pass reconciliation eligibility.
The participant decision at decisions `513–536` uses that eligibility and payment predicate.
After re-entry, the existing owner tick at effects `155–162` can start a fresh review through `2763–2786`, recreating its deadline and explicitly activating its mission.
No added world scan or replacement clock is needed by the repaired trace.

## Explicit participant/host territory floor

Effects `690–710` replaces the ROOT-sensitive core check with `gods_of_africa_participant_holds_host_core_state = yes`.
Triggers `298–304` checks `any_controlled_state` of the current participant for an African state that is a core of `event_target:africa_host`.
The existing host-array call at effects `140–142` therefore tests each participant, and registration at `348` uses the same predicate.
This does not depend on the initiating event's ROOT or treat a participant's own unoccupied cores as host territory.
The source distinguishes holding a host core from a host core controlled by somebody else.

The new lifecycle helpers and their reviewed callers use `= yes`, variables, and native scope blocks.
No named argument block or `$PARAMETER$` API was introduced.

## Accepted-plan and documentation disposition

Disposition of prior F1–F3: implemented source repair, with the manual L1–L3 review confirmed and required engine/MCP evidence unconfirmed.
This updates the status of those exact prior findings and does not supersede the entire prior audit.
`docs\events\012_africa\gods_of_africa.md:33,61–63,122` describes retained history, durable opt-out, interrupted review cleanup, paid-offer history, and continuing validation limits consistently with this patch.
No lifecycle documentation contradiction was found in those current passages.
No plan was promoted or rejected by this review.
U1 membership reachability, U2 archived-survivor settlement coverage, and U3 country-object/delayed-event lifetime remain separate unresolved questions from the original audit.
The separate victor/re-legitimation disposition also remains unresolved.
There are no additional asset, portrait, GUI, animation, or catalog production requirements created by this bounded repair.
Their broader Event 012 completion is outside this handoff.

## MCP and meaningful validation limits

Manual validation read full relevant registration, archive, clean, cancellation, history, review, payment, deadline, and acceptance bodies and their bounded callers.
The restored tracked changes were compared read-only against Git HEAD, and the untracked lifecycle helper was read directly.
The scenario conclusions above are symbolic source reviews and documentation checks, not native execution or balance validation.
No new weighted selection or AI weight was audited in this deterministic lifecycle assignment.
The separately assigned `chaosx_ai_probability_auditor` retains weighted-scenario evidence ownership.

Live metadata exposed event inspect/render/compare and reference context/search/read/source lookup.
Two initial event-selector probes returned argument-validation errors, first requiring `selector.kind` and then requiring `selector.eventId` instead of `id`.
The corrected request selected `{ kind: "event", eventId: "chaosx.nr12.606" }` in trace mode, both directions, depth 1, 6 nodes, 10 edges, and no helper expansion.
That request and reference context/search requests had no final receipt observed at handoff.
The context requested event references with limit 4, and the targeted search requested installed `remove_mission` evidence with limit 1.
A read-only state render for the same event, downstream depth 0 and one node, and a read-only comparison request narrowed to that event with one chain/render node and rendering disabled were dispatched without waiting for their receipts.
The comparison request did not assert a cached baseline revision, so valid before/after coverage remains unconfirmed.
There is no successful inspected lifecycle coverage, render, comparison, server revision, or artifact URI claimed here.
Reference-read citation binding is unconfirmed because no context/search receipt was available to supply its id and revision.
The exact current limitation is pending or unobserved client receipts, not a proven absent server route or a proven server failure.
The parent explicitly owns receipt collection and narrower retries, and separately has its own `.606`, context, and search requests pending.
Required MCP evidence remains unconfirmed and blocks an engine/MCP acceptance claim, while this manual source review is ready for the parent's bounded tranche decision.
No helper-expansion mode, native task, job inspection, or job cancellation was used without version/health/client negotiation.

## Installed and offline reference evidence

The following local sections were read directly during this review.
Installed documentation is the primary syntax authority, with the offline wiki read in parallel.
Hashes identify the actual local revisions rather than an unreturned MCP revision.

| Windows source path | Sections read | SHA-256 |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 661–670 explicit activation, 6083–6091 removal without completion/timeout | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 1318–1325 current-country controlled states, 5006–5013 variable existence, 5390–5397 state core ownership | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\SWI_scripted_effects.txt` | 1886–1901 mission removal and separate flag cleanup precedent | `1db766b3da05ca60c44b8708d20225eef780137c4fbf21572215f22a9395f939` |
| `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | 465–478 explicit mission activation, availability, timeout, and cancellation | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 1147–1156 membership, 1210–1256 array iteration and participant scope | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 260–263 ROOT, current scope, PREV, and FROM distinction | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |

## Reviewed source snapshots and next actions

| Mod-relative file | SHA-256 |
| --- | --- |
| `common\scripted_effects\012_africa_gods_effects.txt` | `76f71b03463b822bbc4d32c5747c94c6b984271c40ef89f4cc84b27d2c6ca493` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `a1901d841764217cd4db311d5207862bed5ce22268b030adb81cef07b77b35f9` |
| `common\script_constants\012_africa_gods_constants.txt` | `e02f806af62c71d8bea7b9f04697fb254f097b081eeef06549e10ab50db45d79` |
| `common\scripted_effects\012_africa_gods_lifecycle_effects.txt` | `e506c7315a2f7046d8af3b9204f009448f949ec4be6cb176b3c971fd8cc9623b` |
| `common\decisions\012_africa_gods_decisions.txt` | `230f9f22136cda7a6625641ef45e4d14666b846457e2c466656824d2b0d3f8b6` |
| `common\on_actions\012_africa_gods_on_actions.txt` | `129e048309e535f68ea9e199df4ae601dc45ebd73ed7fa747146b879798c26e0` |
| `events\012_africa_gods_of_africa.txt` | `5d2f37e1f854b7bc97158ada548810c02b6d047cae75e9c120804a43335a04f8` |
| `docs\events\012_africa\gods_of_africa.md` | `8993a1118f16599decb0e5787d18f4abf7eb845b880f4b4ab5e14a621c148d55` |

The parent should include the new lifecycle helper when reviewing its own commit, retain the explicit unconfirmed MCP/engine limits, and collect pending receipts with narrower retries as already assigned.
Do not treat a focused event trace as full scripted-helper lifecycle evidence even if it returns successfully.
No further L1–L3 gameplay correction is recommended from this snapshot.
Revisit this bounded conclusion if those lifecycle blocks change during the next implementation tranche.

Skills applied: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, and the relevant reconciliation lifecycle guidance in `chaos-redux-decisions-missions`.
No skill was created or updated.
