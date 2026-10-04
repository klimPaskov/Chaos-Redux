# Event 012 Gods lifecycle audit — 2026-10-03

## Scope, ownership, and acceptance basis

This is a bounded read-only completion audit of membership, enrollment, archival, re-entry, unifier loss, successor generations, and hidden settlement history.
The only file written is this handoff.
No gameplay, localisation, other documentation, assets, workbook, index, or Git history was edited.
The parent owns the response/punishment receipt tranche; the architect owns mobile/artillery planning; `chaosx_ai_probability_auditor` owns AI and probability evidence separately.
Those surfaces were not audited here, and this report makes no overall Event 012 completion or balance claim.

The acceptance basis is the explicit active-goal contract in the parent's 2026-10-03 audit instruction: enroll every valid major/player independently; retain participant hidden history indefinitely until final settlement; permanent defiance stops ordinary demands and ends only through accepted restoration; unifier capitulation/disappearance cancels live demands, punishment, participant state, and current authority; add no world scans or clocks.
The full spec supports enrollment and archival at lines 101–114, permanent marks at 290–311 and 658–670, accepted reconciliation at 1044–1057, victory/restoration authority at 1075–1077, settlement evaluation at 1087–1104, independent relationships/control changes at 1430–1456, and cleanup at 1616–1642.
Spec location and existing implementation documentation are not additional approval for resetting permanent history.

AGENTS.md and `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-event-planning`, and `chaos-redux-improvement-loop` were applied.
The relevant `chaos-redux-decisions-missions` lifecycle guidance was applied when tracing reconciliation mission cleanup.
No new design expansion or asset production was performed; asset, portrait, model, GUI layout, focus depth, and catalog production are outside this audit.

## Verdict by surface

| Surface | Status | Evidence and limit |
| --- | --- | --- |
| Independent enrollment and retention after loss of major rank | Source-present; MCP/runtime acceptance blocked | Candidate/live gates separate initial major/player qualification from continued participation. Registry membership prevents duplicate enrollment. See triggers 139–195 and effects 190–237, 310–390. |
| Bounded census, callbacks, and review | Source-present; MCP/runtime acceptance blocked | Existing one-time `global.countries` census; maintained candidate array; callbacks touch transaction countries, including government-change civil-war sides; one `.607` review at 90 days with cap 640. No extra scan/clock is proposed. |
| Hidden history in uninterrupted participation | Source-present | Effects 720–745 append aligned kind/day arrays and cumulative counters with no timer expiry or rolling truncation in that helper. |
| History after archive/cleanup followed by re-entry | Partial; must fix F1 | Cleanup retains the stored record, but registration unconditionally deletes it. |
| Permanent defiance during uninterrupted participation and same-host re-entry | Partly preserved | Demand gate rejects `gods_of_africa_defiant`; archive/clean and register retain that flag. Re-entry still loses the historical record and has stale reconciliation state. |
| Unifier-loss cancellation | Live cancellation source-present; durable defiance partial | Loss cancels live participant authority and clocks. It also clears the only ordinary-demand opt-out flag; later registration has no restoration/previous-defiance gate. See F2. |
| Reconciliation after archive/revival | Partial; must fix F3 | Mission removed and dates cleared while pending/payment flags remain. |
| Final settlement of the current live roster | Source-present; acceptance limited | Outcome is evaluated before live state is finalized; hidden arrays/counters remain. Archived survivors are outside that traversal; see U2. |
| Membership as proof of mutation authority | Partial source coverage; runtime reachability unresolved | `generation_is_current` is weaker than `is_registered`. Some live mutation gates use only the former; final receipt presentation intentionally also uses the weaker predicate. See U1. |

## Must-fix findings

### F1 — Re-entry erases the retained hidden settlement ledger

**Source fact:** `common\scripted_effects\012_africa_gods_effects.txt:310–359`, `gods_of_africa_register_participant`, has only the `participant_can_register` gate, with no first-enrollment or same-generation preservation branch.
It writes the participant generation at 329, resets Wrath at 330–331 and historical counters at 332–341, and clears `gods_of_africa_history_kinds` and `gods_of_africa_history_days` at 349–350.
The gate in `common\scripted_triggers\012_africa_gods_triggers.txt:175–188` requires valid current major/player eligibility, host activity, absence from the live array, and capacity; it does not distinguish a returning participant from a new participant.

`gods_of_africa_archive_invalid_participant` at effects 395–500 and `gods_of_africa_clean_participant` at 2943–3031 remove live membership/contracts while retaining the hidden history arrays/counters and permanent defiance flag.
The capitulation/annex callbacks use `clean_participant` at `common\on_actions\012_africa_gods_on_actions.txt:37–51`; quarterly invalidation uses `archive_invalid_participant` at effects 202–207.
The maintained candidate review can subsequently call register again at effects 210–215.

**Scenario `L1_same_host_revival`:** P has compliance, refusal, aid, and/or defiance history in host generation G; P capitulates or otherwise becomes invalid; P is removed from the live array; the same surviving country becomes non-capitulated and again qualifies as major/player while the host remains active in G; the next maintained-candidate review registers P.
The source path resets the entire settlement counter/history pair even though neither final settlement nor a new host generation occurred.
For a former defiant participant, ordinary demands remain blocked by the retained defiance flag, but its permanent prior conduct no longer exists in the aligned record/counters.
A reconciled participant can similarly lose its prior-defiance record on later re-entry.

**Bridge check:** `gods_of_africa_initialize_world_order_history` at effects 244–305 seeds separate `gods_of_africa_world_history_*` flags/status from Scramble receipts.
It does not restore the Gods kind/day arrays or counters.
Its indexed call is the World Is One manual-scenario path in `events\chaosx_triggerable_scenarios.txt:98`, not ordinary re-entry.
Searches of `common` and `events` found no reader that reconstructs the deleted kind/day arrays or prior-defiance opt-out from `gods_of_africa_defiance_day`.
The new report receipt clearing calls are not this historical ledger and are not the cause of F1.

**Required parent action:** separate first enrollment from returning enrollment and preserve the accepted durable history, including prior defiance, until settlement.
Reset live contract/presentation state independently.
A new generation may reset live authority, but the current instruction supplies no acceptance basis for discarding the durable ledger merely because the generation changes.
If historical records are split by generation, retain the prior records and their final-settlement consumers rather than silently replacing them.

### F2 — Loss cancellation plus successor registration can discard permanent opt-out without accepted restoration

**Source fact:** `gods_of_africa_cancel_on_unifier_loss`, effects 3143–3180, cancels each live participant, clears the live arrays, removes active/activation/consolidation/clock flags, clears schedule variables, and zeros public Strength.
`gods_of_africa_cancel_participant`, effects 3182–3263, removes participant/contract/punishment authority, but also clears `gods_of_africa_defiant` at 3217.
It retains hidden arrays/counters at this point.
A later registration then performs F1's unconditional reset and has no permanent opt-out, defeated-by-participant, or accepted-restoration predicate.

Host annexation is covered by the existing world-order bridge at `common\on_actions\012_africa_world_order_on_actions.txt:345–366`.
`africa_begin_host_transfer` at `common\scripted_effects\012_africa_host_transfer_effects.txt:960–982` cancels Gods authority before the host pointer changes.
Transfer stages/restores the candidate census at 115–120, 467–478, and 736–737; the successor receives the new pointer/mandate/generation at 1127–1138.
These operations preserve discovery candidates, not a Gods participant history restoration or opt-out restoration.

**Scenario `L2_successor_authority`:** P declares permanent defiance; the unifier is defeated/annexed; cancellation clears P's live defiance and participant flags; a successor later obtains a valid activated Gods generation; P remains an eligible candidate.
The register and demand gates permit fresh ordinary eligibility without requiring participant reconciliation or a separate accepted Gods restoration milestone, and the retained history is then deleted.
This is a source-permitted conditional path, not evidence that a successor currently auto-launches the Gods loop.
No claim of observed civil-war variable cloning is made.

**Same host versus successor:** in effects 18–63, the outer initializer gate rejects `gods_of_africa_cancelled_on_unifier_loss` before reaching the generation-change branch that clears it.
`system_can_activate` in triggers 56–77 also rejects that loss receipt.
A temporary recovery of the defeated old host therefore does not by itself restore its ordinary authority, which is consistent with cancellation.
Changing that host's generation alone cannot reach the initializer's inner receipt-clear branch either.
An explicit restoration owner would need to establish the approved milestone and then intentionally reopen that lifecycle; such a milestone must not be inferred from the comment or a new numeric generation alone.

**Required parent action:** distinguish cancelled live defiance presentation/authority from durable permanent opt-out and prior-defiance history.
A successor's enrollment/demand eligibility must consume the durable opt-out until the accepted restoration path explicitly changes it.
The existing bilateral reconciliation completion at effects 2799–2821 is a demonstrated intentional defiance clear; unifier loss is not participant acceptance.
The full spec's separate victor/re-legitimation promise at 1075–1077 is also not proved by the current loss callback, which records the host defeat milestone without an individual victor authority-exemption gate in these Gods helpers.
The exact milestone and whether an existing successor mandate satisfies that promise remain an unresolved parent design disposition, not an approved new route or authority reset.

### F3 — Archive/cleanup leaves live reconciliation flags without a live review contract

**Source fact:** archive at effects 395–500 and clean at 2943–3031 remove `gods_of_africa_reconciliation_mission`, clear the start/due/retry variables, and clear offer/report flags.
Neither clears `gods_of_africa_reconciliation_pending` nor `gods_of_africa_reparations_paid`.
Register at 310–359 also does not clear those flags.
This was checked against both complete helper bodies, not inferred from a shortened snippet.

**Scenario `L3_pending_review_revival`:** defiant P is inside a reconciliation review; P capitulates; clean removes the mission and clears the deadline but retains pending/payment state; P recovers and re-registers under the same host.
`gods_of_africa_start_reconciliation` at effects 2774–2797 refuses to open a fresh review because pending is already set.
`participant_can_reconcile` at triggers 533–547 instead accepts a missing due-day variable.
The participant reconciliation decision at `common\decisions\012_africa_gods_decisions.txt:515–535` can therefore expose a pending reconciliation route with no matching current review deadline.
The mission at 57–78 has `activation = { always = no }`, so automatic activation does not repair that state.
Its cancel effect only removes the mission; installed `remove_mission` documentation explicitly excludes complete/timeout processing.
This finding does not claim unpaid acceptance: the host acceptance decision at 1042–1070 separately requires paid reparations and an offer.

**Required parent action:** clear live reconciliation pending/payment/offer state during archive/clean, while retaining durable defiance and historical paid/attempt facts in the hidden ledger.
The existing owner tick can reopen a fresh review using its existing clock and cooldown rules after re-entry.
Do not add a replacement world scan or clock.

## Unresolved questions and limits

**U1 — Membership proof is not universal; reachability is unobserved.**
Triggers 160–173 test live country, participant flag, and generation equality, without host-array membership.
Triggers 190–195 add actual membership; protection uses that stronger check at 633–650, and its transfer preflight also uses it.
Ordinary-demand eligibility at 246–264, active/current contract gates at 197–234, voluntary-aid eligibility at 682–719, and history mutation at effects 720–745 use the weaker predicate.
Thus a declared state with matching participant flags/generation but no array membership can satisfy some live gates if the remaining conditions hold.
Ordinary archive/clean/loss paths clear the participant flag, so they do not establish an actually reachable unauthorized participant.
No source finding here proves civil-war flags/variables are copied.
The exact missing runtime question is whether `start_civil_war`, dynamic-country slot reuse, annexation/release, or another engine transition can produce that matching nonmember state, and whether callback insertion resolves it before any action can run.
No save was supplied; engine inheritance and country-object lifetime were not guessed.
If live authority is meant to require registration, apply membership at the live mutation/action gates, preserving a separate presentation/history predicate: final settlement deliberately clears the host array before `.608` acknowledgement while retaining the participant flag for that receipt.
Blindly strengthening the shared generation predicate would break that source-present receipt design.

**U2 — Final settlement traverses live members only.**
Effects 3265–3287 evaluate/reward/finalize only `gods_of_africa_participants`; effects 3293–3318 then empty that registry.
Archived countries retain their local history until re-registration, but have no archived-participant settlement traversal here.
For a surviving capitulated/temporarily invalid participant still archived when settlement occurs, no final evaluation is shown by this path.
The full spec says every surviving participant is evaluated at 1089; the parent should disposition which archived survivors receive an outcome versus retain history only for later Event 012 consumers.
This is an unresolved coverage/design question, not authority to invent rewards for invalid countries.

**U3 — Engine object and delayed-event lifetime.**
Source proves old-host recovery remains blocked by the loss receipt and participant generation mismatch closes ordinary mutations after pointer succession.
A save/runtime observation would be needed to establish exactly which participant variables/arrays survive annexation and release, whether a reused dynamic slot is the same country object, and whether queued `.600`/`.606`/`.607` jobs remain attached to that object after replacement.
No save, observed inheritance, live game launch, or log collection occurred.

## Meaningful validation and MCP blockers

The review traced the explicit scenarios L1–L3 through full source bodies, callback scope, registry gates, mission ownership, and final-settlement consumers.
These are symbolic source traces, not executed engine scenarios.
Read-only `git show de1ae251:<path>` comparisons established that register, archive, and cancel-participant history behavior is identical to that baseline after excluding the parent's new report-receipt clearing call.
`record_history`, the World history bridge, and the previously read clean-participant body were also unchanged from that baseline.
F1/F3 are lifecycle findings rather than a claim that the new numeric report receipts caused an old-history defect.
The timer, actual-tank, and requirement-text tranches (`7e549314`, `46ea61997`, `6aa4a930`) remain separately owned; they were not re-audited or amended here.

The initial tool inventory exposed schemas for reference context/search/read/source lookup and event inspect/render/compare.
Actual `hoi4.reference_context` and `hoi4.event_inspect` calls returned respectively `MCP tool \`hoi4_agent_tools/hoi4.reference_context\` is not available to the model` and `MCP tool \`hoi4_agent_tools/hoi4.event_inspect\` is not available to the model`, with `isError = true`.
A bounded retry for `.606` and attempts to call reference search/read/source lookup, event render, and event compare then failed at the client binding with `TypeError: tools.mcp__hoi4_agent_tools__hoi4_<route> is not a function`.
No successful server revision, graph, render, comparison, continuation URI, analysis-mode coverage, or event artifact was returned.
The `de1ae251` source baseline exists, but there is no valid cached/graph-bearing MCP baseline and no callable comparison route; the read-only Git review is not `hoi4.event_compare` evidence.
Reference read had no returned citation id/revision to bind because context failed; no MCP reference retrieval success is claimed.
No helper-expansion mode, persistent job, or native MCP task was used without confirmed health/version/client negotiation.
Required event inspect/render/compare acceptance is **blocked**, and source review is not equivalent evidence.
No probability pass was attempted in this deterministic lifecycle assignment; the separately assigned `chaosx_ai_probability_auditor` remains required for weighted surfaces.

## Local reference fallback evidence

Paths are Windows-native; SHA-256 identifies the local source revision actually read.
Installed documentation is the primary syntax authority, with the offline wiki read in parallel.
The peace-conference scope descriptions differ: installed `00_on_actions.txt:5019` documents ROOT as the country that just went to peace, whereas the wiki table describes winner/loser.
This audit does not assume an undocumented universal FROM binding or make onboarding depend on that callback alone; the maintained candidate review remains the fallback.

| Source | Read section / source precedent | SHA-256 |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 661–670 activate mission; 4296–4310 scope-array iteration; 6083–6091 remove mission without complete/timeout effects | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 5672–5684 exact array membership | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\on_actions\00_on_actions.txt` | 931–945 capitulation; 1296–1310 government change; 1578–1595 release; 1615–1628 annexation; 5019–5029 peace callback | `52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\COG_scripted_effects.txt` | 197–213 exact vanilla `global.countries` scope-array precedent, including nonexistent tags | `77fd69835f9a7115fc60d85de61c5c31e4c7880e30fb6d6e8ae494f318b02710` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 1147–1156 membership definition/example; 1210–1256 array loops and PREV semantics; 1261–1269 nonexistent country-scope example | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md` | 208–218 government change/civil-war sides and peace; 252–263 capitulation, annexation, puppet and release scope contracts | `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a` |
| `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | 465–478 explicit mission activation, timeout and cancellation | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |

## Source snapshots and documentation disposition

The shared workspace changed during the parent's receipt work.
The critical effects/triggers/callback/event snapshot below was reread after that change; helper names and cited ranges refer to this snapshot, not a frozen final parent revision.
Other dependency hashes identify the bounded source reads made during this audit.

| Mod-relative source | SHA-256 |
| --- | --- |
| `common\scripted_effects\012_africa_gods_effects.txt` | `b3f52f8c6689dccacdc18ede8f43c7d292266c2d0bcf0e199449dcaa6d56453a` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `b70b438cf6ad01e34690ad67f97ad3630940bee650d5962a1f84244796e747ed` |
| `common\on_actions\012_africa_gods_on_actions.txt` | `129e048309e535f68ea9e199df4ae601dc45ebd73ed7fa747146b879798c26e0` |
| `events\012_africa_gods_of_africa.txt` | `5d2f37e1f854b7bc97158ada548810c02b6d047cae75e9c120804a43335a04f8` |
| `common\decisions\012_africa_gods_decisions.txt` | `230f9f22136cda7a6625641ef45e4d14666b846457e2c466656824d2b0d3f8b6` |
| `common\scripted_effects\012_africa_host_transfer_effects.txt` | `1618810a08c9caf4c89f900299b0b4347e814e531ba1c8712574f1089a70e04d` |
| `common\scripted_effects\012_africa_world_order_effects.txt` | `6a9b793ddc2f3998394aa9909706bed61859769cc63ad09bdfe815fc228b6e7a` |
| `common\on_actions\012_africa_world_order_on_actions.txt` | `01aa58fd5324d6ad7e7941782d4b6e75a04952e28e24529a83e8756164370bb2` |
| `common\script_constants\012_africa_gods_constants.txt` | `dea075a53455cbcb894e33a8e5e8bf15dd1a5c2969edcec63ea70a96d18dbeea` |
| `docs\specs\012_africa_is_one_gods_of_africa_specs\specs\012_gods_of_africa_full_spec.md` | `2ccb9fbdedb7f7715187397b6bdc31610dc0fdd7cf4e2b1388f16d7490066798` |
| `docs\events\012_africa\gods_of_africa.md` | `8fd289a20ce7b52858312c45425b30ae1d8de42b9d61a08bc266055c0988ddc2` |

`docs\events\012_africa\gods_of_africa.md:33` explicitly describes fresh-generation history reset, while line 61 promises permanent defiance and preserved prior-defiance history.
Against the active-goal acceptance basis, the reset statement documents existing behavior; it does not approve an exception to permanence.
The same-generation re-entry reset and orphaned reconciliation flags are not disclosed there.
Lines 114–132 correctly leave owner lifecycle acceptance unresolved; that gap should remain visible until F1–F3 and the required evidence are dispositioned.
No documentation reconciliation was applied outside this handoff.
No additional asset handoff is required for the bounded lifecycle fixes; report art/localisation production and their acceptance remain parent-owned and unreviewed here.

Disposition: bounded census/callback/review source work in `de1ae251` is implemented within the supplied authorization, with runtime/MCP limits retained.
F1–F3 are outstanding fixes against the accepted active contract, not automatically accepted new expansion plans.
U1–U3 remain unresolved source-legitimacy, settlement-coverage, and runtime questions.
No unreviewed plan was promoted, rejected, or silently marked complete.

## Recommended next actions

1. Parent separates durable history/opt-out from live participant contracts and applies F1–F3 using the existing maintained registry and owner clocks.
2. Parent records which accepted restoration milestone can reopen successor authority and dispositions archived surviving participants at settlement; do not treat a generation increment alone as that decision.
3. Parent rechecks L1–L3 against the final patch and obtains required event inspect/render/compare evidence when the routes are callable, preserving the current exact route blocker until then.
4. Retain U1/U3 as precisely stated missing runtime evidence, with no assertion of cloning or slot persistence and no request for logs or a game launch.
5. Parent reconciles the canonical lifecycle wording with the final implementation and this handoff; probability, mobile/artillery, and report work stay in their existing assignments.

The lifecycle contract is **partial**, with required MCP validation **blocked**.
No simplification, new gameplay fallback, additional clock, or world scan was introduced by this audit.
