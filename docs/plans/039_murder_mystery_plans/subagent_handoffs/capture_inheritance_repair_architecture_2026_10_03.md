# Event 039 safe capture and limited inheritance repair architecture

Date: 2026-10-03.
Role: `chaosx_scripted_system_architect`, bounded research mode.
Disposition: implementation proposals are `unresolved` pending parent review, with MCP lifecycle evidence `blocked` as described below.
The research handoff is authored, but the Event 039 goal remains incomplete.

## Authority and boundaries

The parent explicitly named Parts 3, 5, 6, and 18 as accepted specifications and requested this capture and inheritance repair investigation.
That instruction is the acceptance basis for the requirements below, together with the recorded implementation authority in `docs/events/039_murder_mystery.md:7-12`.
It does not accept the specific helper names or algorithms proposed here.
The parent owns implementation, final safety review, and reconciliation of the existing shared working tree.

Only this handoff is written.
No gameplay, localisation, workbook, asset, staging, commit, or game-launch action is authorized in this research task.
SCN019 source registration commit `2f8a05eff` is completed according to the supplied parent context.
The separate manual-world-end-disabled eligibility repair and its pending commit stay with their owner.
Neither item is reopened here.

The inspected untracked `039_murder_mystery_character_effects.txt` already installs a route successor before founder retirement.
Its source contract and the explicit regular `murder_mystery_capture_actor` in the parent integration work are retained.
Existing successor names and `GFX_portrait_039_hidden_hand`, `GFX_portrait_039_cells_without_masters`, and `GFX_portrait_039_necessary_mask` are the only proposed presentation consumers.
Their approved asset quality is supplied parent context, not a visual audit performed by this task.
No new characters, countries, portraits, routes, ordinary civil wars, or central MCP router are proposed.

## Accepted requirements and distinct outcomes

| Requirement | Acceptance source | Consequence for this tranche |
| --- | --- | --- |
| Prepare succession before removal, exclude protected and already removed characters, require explicit dispositions | Part 3:5-23, 97-130, 132-157, 183-185 | Capture must revalidate the recorded character, owner, row, protection, and successor immediately before retirement |
| Sparse foreign network, bounded processing, row retirement and current ownership | Part 5:5-11, 26-38, 218-228 | Inheritance cannot search all countries or treat a standalone country flag as a registry row |
| Territorial heir requires a surviving eligible derivative and a safe central package | Part 5:195-208 | A foreign ordinary government's cell is not permission to replace that government's leader or become a central state |
| Global dismantling depends on surviving mature cells and territorial actors | Part 5:210-216 | Capturing the founder alone cannot resolve an intact Assassin State |
| Territorial defeat and inheritance are separate outcomes | Part 6:206-212 | Live-state succession remains local, defeated-state inheritance evaluates surviving foreign ownership |
| Early capture ends the chain, later capture tests inheritance, one derivative can inherit | Part 18:97-106, 108-121 | Preserve phase-sensitive resolution, including Evolution II before territorial creation |

The current request additionally requires a cap, a permanent resolution receipt, eligible bounded foreign cells, correct actor scopes, and no anonymous core-offender resurrection.
The following implementation interpretation is proposed for parent review:

1. Capture before Evolution II records the core capture once and permanently resolves the investigation through bounded cleanup.
2. Capture after Evolution II while an Assassin State is alive installs its verified successor, retires only the registered founder, records the capture, and leaves the territorial movement and foreign cells active.
   It does not consume the foreign inheritance allowance.
3. Capture after Evolution II before any territorial state has existed evaluates the existing foreign cell registry.
   A qualifying cell can preserve underground network ownership without changing its ordinary government's leader, loading a country package, or fabricating another anonymous offender.
   The exact continuation ledger and post-capture incident dispatcher are unresolved implementation inputs because the inspected files do not expose a complete underground-heir contract.
4. A defeated territorial central movement evaluates at most one territorial heir from already registered foreign cell ownership and an existing validated derivative package.
   An ordinary foreign cell cannot satisfy territorial inheritance on its own.
5. No viable heir ends inheritance permanently.
   Surviving lower-stage cells enter the accepted bounded remnant cleanup instead of creating another central state.
   Global resolution waits for mature cells and relevant attached derivatives to be dismantled or detached, with structural registry uncertainty blocking the resolution proof.

Steps 3 and 4 implement different spec cases.
Conflating them with same-country leader replacement would repeat the current defect.
Do not silently promote the proposed underground continuation mechanism to accepted design or omit territorial viability requirements to fit a small patch.

## Current source findings

Line anchors refer to the byte revisions in the evidence inventory and must be refreshed before the parent applies a patch.

| Finding | Exact current anchors | Source consequence |
| --- | --- | --- |
| Capture classification is erased during preparation | Integration effects:700-720 sets `selected_target_is_core_offender`, runtime effects:633-641 clears it, integration effects:746 and 777 then require it | Under the inspected straight-line flow both the named founder path and baseline generic capture path lose their core proof before checking it |
| Character liveness is checked with a COUNTRY-only trigger | Integration effects:695-698, 747, 763, 1255, runtime effects:437, 442, 515-516, 577-581 | Installed docs do not support `exists` as a CHARACTER predicate, so these checks cannot establish character existence or current recruitment |
| A missing or invalid founder becomes another anonymous core | Integration effects:686-721 | The `else` registers a new generic row whenever the founder branch fails, including absent, retired, or inaccessible founder pointers after territorial play |
| Each generic core attempt constructs another row | Integration effects:709-717 | `dynamic_target_base_id + transaction_sequence` is not an immutable baseline-offender identity and can bypass a previous used-row result |
| Successful capture sets terminal readiness regardless of remaining movement | Integration effects:1074-1078 | It also zeroes the investigator country's reach, which is not proof that global foreign rows or the central movement were eliminated |
| Early resolution stops runtime without full cleanup | Integration effects:1137-1144 calls `mark_runtime_resolved`, runtime effects:276-284 | It leaves target/cell and selection state outside the full cleanup path at runtime effects:2031-2082 |
| Late capture queues a test for an intact state | Integration effects:1146-1152 | There is no viable-central-state exclusion or duplicate-test receipt at this scheduling point |
| Current inheritance requires the current central state and original founder | Runtime triggers:718-731 | It cannot evaluate Evolution II before state creation, and cannot evaluate a central actor that has actually disappeared |
| Inheritance picks an arbitrary political character | Integration effects:1177-1188 | `random_character` plus `is_country_leader` permits non-ruling party leaders and assigns an eligible disposition without an audited candidate identity |
| Inheritance is same-country leader replacement | Integration effects:1202-1264 | It scans neither the foreign cell rows nor derivative rows and transfers no central ledger or movement-parent ownership |
| Retirement receipt goes to ROOT, then is read on the central actor | Integration effects:1257 versus 1261 | ROOT is the recipient of event `chaosx.nr39.23`, normally the investigating government, not the entered Assassin State |
| Persistent results mix flag kinds | Integration effects:1271-1273 writes country flags, runtime triggers:723 and 630/706/740 and integration effects:1281 read corresponding global flags | The global inherited/central proof is not published, and the terminal failure branch runs even if a country-only commit proof was set |
| Used-row evidence is written but not revalidated | Runtime effects:560-562 versus 668-670 | Validation reads disposition/protection, but does not explicitly reject `target_used_entries = 1` or validate selected row generation |
| Validator assumes caller equals ROOT | Runtime effects:563-567 | Inside a helper called on another country it marks ROOT's flag instead of the actual helper caller's flag |
| Generic callback overrides owner matching | Runtime effects:587-594 and 621-629 | A callback flag alone can mark the owner valid even if recorded ownership differs, without a specific cross-country capture contract |
| Stale character selection is not cleared on every validation | Runtime effects:542-545 versus 577-581 | A prior character pointer can survive a missing or non-character row unless clear-selection ran beforehand |
| Transient cleanup omits some capture-specific targets and receipts | Runtime effects:1996-2028 | It clears selected owner but not all founder/character/inheritance selection state or pending inheritance receipts |

The current late path does not call `finalize_runtime` directly.
It queues `chaosx.nr39.23`, whose option calls the inheritance helper and then emits `.24` or `.25` at events:227-248.
The unsafe permanent-ready state is established earlier, and a repair that treats `.25` as permission to finalize would erase a viable movement.
Current `.25` at events:266-277 only clears its presentation failure flag.
It does not provide permanent global resolution or remnant cleanup.

`murder_mystery_cleanup_after_country_loss` at integration effects:1988-2002 performs country cleanup and reconciliation but does not dispatch the specified inheritance test.
The named Event 039 on-actions file contains startup and CXT hooks only.
No defeated-central ownership receipt was identified in the inspected files.
The parent must establish the precise bounded owner callback for that receipt before calling the territorial inheritance branch.

Founder registration is an additional prerequisite concern inside this same integration file.
At integration effects:1565-1569 the package creates `MURDER_MYSTERY_FIRST_KNIFE_NAME`, but at 1595-1598 it flags a random character with any country-leader role as the founder.
Capture's exact row ID `390003` and founder flag do not independently prove that the correct ruling character received that flag.
Resolve the exact created/ruling character before marking or registering it, and preserve the existing parent-owned package.

## Character predicates and scope evidence

Installed `documentation/triggers_documentation.md:2708-2715` lists `exists` with `Supported Scopes: COUNTRY` and describes current-country existence.
The offline Triggers table at line 638 has broader wording without a scope restriction.
Installed documentation takes priority.
The conclusion is that CHARACTER-scope `exists = yes` is unsupported by the installed contract, not an observed statement about how the engine happens to coerce that scope.

The verified primitives are:

- `has_character` is COUNTRY-scoped and checks recruitment, installed trigger docs:3410-3420.
- `any_character` is COUNTRY-scoped, installed trigger docs:1272-1279, and the offline Scopes table:401-402 explicitly limits it to that country's recruited characters.
- `is_character` is CHARACTER-scoped identity comparison, installed trigger docs:5345-5352.
- `has_character_flag` is CHARACTER-scoped, installed trigger docs:3422-3435.
- `is_country_leader` checks a leader role, installed trigger docs:5408-5415.
  It does not document a ruling-only filter.
- `has_country_leader` is COUNTRY-scoped with `ruling_only` defaulting to yes, and name, character, or ID criteria, installed trigger docs:3640-3652.
  The existing successor helper already explicitly uses `ruling_only = yes`.
- `retire` is CHARACTER-scoped, installed effect docs:6427-6434.
  `retire_character` is COUNTRY-scoped and unassigns all jobs, installed effect docs:6436-6447.
- Regular event targets support any scope and auto-clear with the chain, installed effect docs:6496-6503 and offline Data structures:303-327.
  Persistent global targets require explicit specific cleanup, installed effect docs:6505-6512, 2733-2749 and offline Data structures:263-275.

Prefer validating the exact generated founder by entering its recorded COUNTRY owner and checking roster membership with `any_character` plus `is_character`, followed by its owner-approved founder identity and disposition checks.
For an existing static token, `has_character = <token>` supplies the documented direct recruitment predicate.
Do not invent a static token for the generated founder.
The installed docs do not explicitly enumerate the dynamic argument acceptance of `is_character = event_target:...` or `has_character = event_target:...`.
The former pattern already appears in parent integration effects:751, but current source alone does not prove its native execution.
The owner must obtain exact MCP/source precedent or runtime acceptance for the chosen dynamic predicate before treating it as fully verified.
No `scope_exists` replacement proves active recruitment.

Offline Scopes:260-266 describes ROOT, THIS, PREV, and recruited-character owner.
Store the actual country caller in a regular event target at helper entry whenever returned flags or variables belong to that caller.
The parent capture helper already does this at integration effects:732.
Shared target validation needs the same treatment for its actor-owned validation flags, because entering the central country does not rebind ROOT.

Vanilla precedent: installed `events/GOE_Iraq.txt:1357-1362` and `1440-1445` retires characters from `every_character` with an explicit character-flag limit, without CHARACTER-scope `exists`.
This establishes the roster-scoped retirement structure, not permission to retire Event 039's unregistered or protected actors.
Offline Effects:2753-2759 similarly separates COUNTRY recruitment checking from CHARACTER identity selection.

## Small owner patch map

Keep these helpers Event 039-owned.
The inspected `chaosx_dynamic_effects.md` registry has no neutral helper covering capture ownership or inheritance, and directs single-event orchestration to its owning source and documentation.

| Helper | Scope and inputs | Outputs | Side effects and direct call sites |
| --- | --- | --- | --- |
| Repair `murder_mystery_validate_selected_target` | COUNTRY actual caller, selected ID, aligned target registry, documented explicit owner callback | Caller-local validated/invalid/protected/used/generation proofs and exact owner/character selection | Clear stale pointers before lookup, preserve used tombstones, replace ROOT writes with explicit actor writes. Called by approve and prepare helpers |
| Retain `murder_mystery_install_movement_successor` | COUNTRY recorded Assassin owner, current route flags and neutrality government | Owner-local `capture_successor_verified` | Reuses the three existing successor packages. Called only by safe founder capture and by a separately verified territorial heir promotion if needed |
| Repair `murder_mystery_select_operation_target` | COUNTRY actual investigator, action, founder or immutable baseline row, permanent capture receipt | One authorized selected core row or fail-closed result | No new anonymous core after state creation or founder capture. Call site remains the existing action transaction |
| Repair `murder_mystery_apply_safe_target_resolution` | COUNTRY capture actor, current registered row, exact owner/founder proof, successor proof | Actor-local capture flags plus permanent core-capture receipt only after successful row consumption | Only registered founder retirement. Generic baseline capture retires no character. Revalidates after successor install and before removal |
| Proposed `murder_mystery_classify_capture_continuation` | COUNTRY investigator with committed core capture, global evolution, bounded registry facts | Early resolution, live central continuation, foreign inheritance pending, or unresolved ownership | Called from integration outcome:1074-1078 and replaces scheduling split:1137-1152. Does not select foreign rows or zero central/network ledgers |
| Replace `murder_mystery_apply_limited_inheritance` | COUNTRY saved inheritance actor, pending receipt, aligned cell registry and, for territorial mode, derivative registry plus defeated-central receipt | Global committed/no-eligible/unresolved result, one persistent selected heir and consumed allowance on commit | No character retirement and no ordinary-government leader replacement. Called from event `.23` after guarded scheduling or precise country-loss owner callback |
| Proposed `murder_mystery_capture_can_resolve_globally` | Trigger in COUNTRY actor context, committed capture/defeat receipts, complete bounded registries | Boolean resolution proof | Requires no viable central/heir, no attached territorial threat, and completed mature-cell dismantling. Misaligned/unknown rows fail closed |
| Proposed `murder_mystery_commit_permanent_resolution` | COUNTRY actual resolution actor, global resolution proof, permanent receipt absent | Global permanent resolution, actor-local recorded receipt, exactly one `.20` schedule | Calls existing bounded cleanup/finalization once. Captures actor before cleanup removes original-host pointers |

Inputs are variables, flags, and event targets with `= yes` calls.
No named-argument scripted-effect API or `$PARAMETER$` substitution is introduced.
Before implementing new helpers the parent should document each in a matching Event 039 helper Markdown file and align `docs/events/039_murder_mystery.md`.
The currently untracked character effects file has an inline contract but no matching character-effects Markdown file was found by this research.
Documentation creation belongs to the owner patch, outside this handoff's sole write permission.

## Candidate hunks and insertion contracts

These are owner-review candidates anchored to current functions, not an applied or validated patch.
The unresolved dynamic-identity predicate and foreign continuation details remain gates.

### A. Preserve core classification through target preparation

At runtime effects:641 remove the clearing of core identity from preparation.
At runtime effects:717-732 clear it as part of explicit selection-context retirement instead.
The selector at integration effects:683-720 is already the producer of this proof.

```diff
@@ murder_mystery_prepare_safe_target_action
-	clr_country_flag = murder_mystery_selected_target_is_core_offender
@@ murder_mystery_clear_selected_target_context
+	clr_country_flag = murder_mystery_selected_target_is_core_offender
```

This does not make the proof sufficient for capture.
Keep row ID, disposition, used status, owner, exact character membership, and permanent capture checks in the named path.
Clear and recompute safe-action validity on each preparation as currently done.

### B. Repair actor identity and row revalidation before capture

At runtime effects:534 save the actual caller before entering registry owner scopes.
At 567 return to that saved actor for flags and compare against it instead of ROOT.

```txt
save_event_target_as = murder_mystery_target_validation_actor
```

The candidate replacement for the current same-owner check is:

```txt
if = {
	limit = { tag = event_target:murder_mystery_target_validation_actor }
	event_target:murder_mystery_target_validation_actor = {
		set_country_flag = murder_mystery_selected_target_owner_validated
	}
}
```

Cross-country capture must pass a distinct owner callback verifying the original founder ID, exact registered central owner and subject, current membership, disposition, generation, protection, and unused status.
Do not preserve runtime effects:587-594 as unrestricted authorization from any `target_owner_callback_passed` flag.
At validation entry clear `murder_mystery_selected_target_character` as well as owner.
Read `target_used_entries` and `target_generation_entries` with the selected row at 560-562.
Reject used rows explicitly even when their disposition has been accidentally changed back to eligible.
For named subjects, compare exact membership inside the recorded country instead of applying COUNTRY `exists` to the subject.
Protected, owner-managed without a removal callback, transferred, unregistered, or mismatched rows cannot install a capture successor or retire a character.
Retain successful used rows as tombstones for the active event generation rather than deleting the only duplicate-removal evidence during reconciliation.

### C. Restrict anonymous baseline fallback and avoid resurrection

At integration effects:704-717 replace the current broad `else` with an explicit baseline-only branch.
Its contract requires no committed core-capture receipt, no founder used/removed receipt, no territorial state ever created, and the registered original host.
It cannot follow a failed named founder safety check.
Give the original baseline offender one stored target-row identity for the current host generation, initialized once and reused by later attempts.
Do not allocate that identity from the current action sequence on every operation.
A fixed new registry ID requires a collision audit and is not assigned here.
Alternatively preserve the first allocated dynamic ID in a host-owned regular variable and require its matching generation thereafter.

After the existing named capture marks row `390003` removed, publish one persistent global core-capture receipt and a recorded generation.
The same receipt is published after consuming the immutable baseline core row.
Keep it distinct from the actor-local `murder_mystery_core_offender_captured` flag, which the current helper clears on entry at 733.
Never clear the permanent receipt in action preparation, inheritance failure, country cleanup, or global finalization.
Use an explicit generation comparison if the owner already supports an authorized new event generation.
Do not add a new restart mechanic in this tranche.

### D. Separate founder capture from permanent resolution

At integration effects:1074-1078 keep `final_capture_success` and local case completion after actual core capture, then call the proposed continuation classifier.
Remove unconditional `permanent_resolution_ready` and do not treat local reach zero as global dismantling proof.
The classifier first checks an existing central actor with country existence, registered package ownership, territorial survival, and unresolved defeat disposition.
A central package whose viability is unknown is an unresolved result, not an inheritance or global-resolution opportunity.
An alive viable central actor leaves runtime active under its verified successor.

At integration effects:1137-1152 replace unconditional early mark and late queueing with guarded one-shot dispatch:

```txt
if = {
	limit = { murder_mystery_capture_can_resolve_globally = yes }
	murder_mystery_commit_permanent_resolution = yes
}
```

The foreign test is scheduled only when global resolution is not established, the central actor is absent/defeated according to a verified owner receipt or has never been created, the foreign eligibility mode is defined, and no pending/completed inheritance receipt exists.
Do not use a plain failed trigger or a missing event target as proof of defeat.
If the old ready flag survives a previous action, clear that transient flag before recomputing continuation.

### E. Replace the unsafe inheritance body, do not repair it by changing one flag

Replace integration effects:1168-1286 and runtime triggers:718-731 as one owner transaction.
Remove random leader selection, registration of `390002` for this purpose, arbitrary successor retirement, ROOT retirement receipts, and same-country inheritance flags.
The existing target ID constant can remain reserved until a separate caller inventory proves it removable.

Iterate indexed rows only in the already aligned foreign cell arrays, with a maximum of `murder_mystery_registry.maximum_cell_rows`.
For each candidate require current COUNTRY existence, current foreign ownership, non-special/nonhuman exclusion, non-retired and non-immune cell state, mature stage and maturity, valid generation and parent lineage, and no incompatible terminal or owner transition.
Exclude the original host and current central country explicitly.
A territorial candidate must additionally match an existing live validated derivative row and its current package, industry, population, supply, Cohesion/legitimacy, and safe leader contract.
Registry alignment is a prerequisite, not an optional reconciliation hint.
Revalidate the selected row and generation immediately before ledger rebinding.

Do not choose an arbitrary eligible row merely to avoid implementing the spec's highest-valid-candidate rule.
The existing inspected files contain no accepted complete ranking or territorial eligibility threshold table.
Candidate scoring and tie handling stay unresolved pending the owner supplying that contract and probability evidence where selection semantics apply.
An underground-only recipient keeps its ordinary government's leader and stores network ownership separately from `murder_mystery_assassin_state`.
An existing territorial derivative promoted to central uses its already accepted country package and successor assets, with no new country creation.

After validated ledger and parent rebind postconditions, publish the same flag kind read by event `.23`:

```txt
set_global_flag = murder_mystery_inheritance_transaction_committed
set_global_flag = murder_mystery_inherited_central_movement
set_global_flag = murder_mystery_central_or_heir_validated
```

The latter two flags belong only to an actual territorial heir.
For an underground continuation publish a distinct documented network-heir receipt and do not advertise central-state viability.
Keep country flags for recipient-local identity and global flags for movement-wide facts.
Check commit postconditions before setting global success.
Do not clear a committed global receipt at helper entry as current line 1169 does.

Current event `.23` uses a binary global commit result at events:241-248.
It needs a third unresolved outcome so adapter, alignment, or ownership failures cannot masquerade as a proven absence of an heir.
Any required narrow presentation/text alignment is parent-owned and must not be silently omitted because this researcher cannot edit localisation.

## Constants, receipts, targets, and cleanup

| Item | Plan | Current source or unresolved value |
| --- | --- | --- |
| Registry bounds | Reuse 28 cells, 12 derivatives, existing first index/step | Constants:491-510, 566-579 |
| Mature stage | Reuse entrenched stage 3 and the existing maturity threshold contract | Constants:267-279, runtime effects:1018-1025 and 1114-1126 |
| Inheritance cap | Add Event 039-owned `maximum_committed_inheritances = 1` | The one-inheritance requirement is accepted, the new constant name is a proposal |
| Inheritance completed/tested state | Persistent global tested/committed/no-eligible receipts for the originating movement generation | A live central continuation does not spend the allowance, repeated completed tests cannot reset it |
| Eligibility tuning | Shared `murder_mystery_inheritance` category for minimum maturity, population, industry, supply, Cohesion/legitimacy, and ranking terms | Exact numbers and score contract are unresolved, no guessed defaults or borrowed world-end tuning |
| Cleanup duration | Reuse an accepted remnant-cleanup band only when found and cited | No complete bounded-remnant-duration contract found in the inspected source |
| Core identity | Permanent capture flag plus generation and immutable baseline row identity | Existing actor capture flags and `390003` remain local/registered evidence, not sufficient global tombstones |
| Permanent resolution | Keep existing global `murder_mystery_runtime_resolved`, add or reuse an owner-approved once-only recorded receipt before dispatch | Must survive cleanup and event `.20` presentation acknowledgment |

`common/script_constants/` is the only proposed tuning location.
Installed script concept docs:216-245 and script-constants documentation:1-32 verify schema and explicit fixed-point access through `constant:` in scoped variables.
No new duration field is patched here.
If the owner adds timed flags, verify their field parsing separately rather than assuming shared constants or variables are accepted there.

Use regular `capture_actor`, `target_validation_actor`, and `inheritance_actor` targets for one synchronous transaction and events fired from it.
Overwrite them at entry and rely on chain cleanup rather than attempting manual regular-target clearing.
Use specific global targets only for persistent current central/heir ownership and the existing registered founder pointer.
After consumed-founder proof is persisted, clear only the owned founder/selection pointers that are no longer needed.
Capture and live-central continuation must not call broad `cleanup_runtime`, which clears the central target and every foreign registry.

Inheritance cleanup clears pending/active flags, candidate targets, row working variables, and any uncommitted ledger snapshot on failure.
It preserves committed count, capture tombstones, generation, and permanent test/no-heir receipts.
If rebind partially fails, restore exact saved parent rows and movement-pointer ownership before returning unresolved.
Do not claim rollback is possible for an irreversible `retire` after the fact, so inheritance performs no retirement.
Country-loss cleanup must resolve or detach relevant rows from that country's exact ownership before reconciliation.
Current cell reconciliation at runtime effects:1065-1066 removes a row when its recorded parent no longer exists.
Therefore snapshot/rebind a surviving foreign row before dead-parent reconciliation destroys the only inheritance candidate evidence.
This ordering is necessary when integration effects:1998-2001 handles loss.

Before permanent cleanup, save the resolution actor and presentation receipt.
Only after a complete bounded resolution proof may existing `finalize_runtime` clear registries.
Keep the capture and inheritance permanent receipts through that cleanup so late action delivery cannot recreate an offender or retry inheritance.
A general guard on `finalize_runtime` needs care because terminal victory and terminal defeat at integration effects:1970 and 1983 also call it.
Scope the capture proof to the capture finalizer, or preserve those terminal callers with explicit existing terminal settlement proof.

## Migration order and acceptance cases

1. Preserve the parent working bytes, review the exact named functions, and establish source/revision-bound MCP inspection.
2. Repair actor-aware validation, character membership checks, stale pointers, used/generation rejection, and exact founder registration.
3. Preserve core selection through preparation and restrict immutable baseline fallback.
4. Add capture receipt and continuation classification, with verified live-central exclusions before queueing `.23`.
5. Replace inheritance selection/ledger rebinding only after the eligibility, rank, foreign ownership, and remnant cleanup contracts are supplied.
6. Align `.23` result kinds and permanent `.20` scheduling, then run the bounded owner review and probability audit/compare obligations below.

| Case | Input facts | Required source and engine acceptance |
| --- | --- | --- |
| CAP_EARLY_BASELINE | Original host, no Evolution II, same immutable baseline core row | Exactly one capture/used-row receipt and one permanent resolution report, complete bounded cleanup, later delivery grants no extra result |
| CAP_LATE_NO_STATE_MATURE_CELL | Evolution II, no territorial state ever created, one mature registered foreign row | Underground inheritance evaluation preserves foreign government's character and caps continuation, no fabricated founder or new state |
| CAP_LATE_LIVE_STATE | Registered founder `390003`, live viable central owner, any foreign count | Exact route successor is ruling before retirement, only founder consumed, runtime and central package remain active, no inheritance allowance spent |
| CAP_NONROOT_ACTOR | Action actor differs from event ROOT and target owner | All action proofs return to actor, successor proof stays on owner, unrelated ROOT flags and variables unchanged |
| CAP_TRANSFER_OR_PROTECTED | Founder transferred, protected, owner-managed without callback, or unregistered | No succession side effect and no retirement, no conversion to anonymous core capture |
| CAP_ALREADY_USED | Used row remains present with eligible disposition or stale selected pointer | Explicit used check rejects it, no second retirement, no replacement anonymous row |
| CAP_WRONG_POLITICAL_CHARACTER | Founder flag accidentally attached to an opposition leader | Identity preflight rejects capture, no protected opposition retirement, registration repair resolves the exact intended founder |
| INC_NO_FOREIGN_ROWS | Central proven defeated or absent before territorial creation, aligned empty registry | No eligible result is permanent for this origin, cleanup/resolution follows phase contract and cannot retry endlessly |
| INC_ONLY_PROTECTED_OR_RETIRED_ROWS | Stored rows are stale, immune, protected, or incompatible | No candidate, ordinary leaders untouched, malformed or unresolvable rows produce unresolved rather than false global victory |
| INC_MATURE_FOREIGN_CELL | Exact current eligible row, correct generation/parent, no territorial package | Network-only continuation, no central-or-heir flag, no ordinary leadership replacement |
| INC_TERRITORIAL_DERIVATIVE | Defeated central owner, viable existing derivative matching foreign registry | One heir, ledger and remaining movement parents rebind exactly once, preserved country/army/package, required viability checks all hold |
| INC_VIABLE_CENTRAL_STATE | Central survives under successor | Inheritance dispatcher skips without publishing no-heir, failure, or permanent-resolution receipts |
| INC_USED_CAP | Committed inheritance count at one, second heir loss | No second central inheritance, no count reset or founder resurrection, accepted hunted-remnant path remains bounded |
| INC_REGISTRY_UNKNOWN | Misaligned arrays, missing generation, unsupported supply/rank evidence | No destructive cleanup or permanent resolution, explicit unresolved ownership/evidence result |
| INC_PARENT_LOSS_ORDER | Dead movement parent, viable foreign candidate rows | Candidate proof is retained before reconcile, rebinding restores lineage, repeated country-loss delivery is idempotent |
| RES_RELOAD_DELAYED | Save/reload around capture, pending `.23`, consumed heir allowance, cleanup and `.20` | Receipts survive, pending dispatch occurs at most once, no reward/retirement repetition, no stale global target authorizes action |

These are acceptance cases, not executed observations.
Source checks must verify flag kind, exact actor returns, successor-before-retire order, no inheritance retirement, row membership and bounds, immutable baseline identity, revalidation after preparation, and teardown preservation of permanent receipts.
Native execution still needs owner-supplied engine acceptance evidence.
The task does not launch the game.

## MCP, validation limits, and unsupported analysis

Connected metadata exposes `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, and `hoi4.probability_inspect`.
`hoi4.script_validate` is not present in the available connected tool list.
The exposed source-lookup schema has no `view`, `keyPath`, or `childOffset`, so bounded child-structure paging is unavailable through this route.
No health, server-version, task-negotiation, helper-expansion, or job support is inferred or invoked.

The actual `reference_context` request used surface `event`, limit 12, and the question about Event039 capture, character predicates, retirement, targets, ROOT, and limited inheritance.
It returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.reference_context`, caused by `timed out awaiting tools/call after 600s`.
It returned no source IDs, revisions, sections, or artifact URIs.
Consequently a revision-bound `reference_read` call cannot be constructed from that result.
Pertinent local sections were read directly as the requested documentation fallback and their SHA-256 revisions are recorded below.
That fallback does not replace MCP event lifecycle evidence.

Additional requested routes were `reference_search` for `exists` in game docs with limit 3, `event_inspect` mode `state_flow` for `murder_mystery_inheritance_transaction_committed` with depth 3/nodes 15/edges 25, and `source_lookup` for `murder_mystery_apply_limited_inheritance`, no references, one definition/15 lines.
Their final transport outcomes are recorded in the addendum below before handoff delivery.
No successful graph, helper coverage, render, compare, or scenario acceptance artifact is currently available from these requests.

Probability inspection was attempted with `source: { path: "common/scripted_effects/039_murder_mystery_integration_effects.txt" }`.
No response was obtained within a local 15-second bounded wait.
`chaosx_ai_probability_auditor` was delegated a read-only inline evidence pass for the random-character selector and the named `INC_*` cases.
Its final evidence status is recorded below.
No weights, ranking constants, eligibility pools, or random probabilities were changed.
Any owner patch changing the random selector or eligible selection pool must first preserve the exact before source and scenario fixture, run the named baseline audit, then apply and compare using the same scenarios.
The missing before snapshot, absent owner patch, and unsupported or unreturned random-character adapter evidence prevent a numeric comparison claim here.

Task-specific work completed: exact source-path review of capture, validator, row consumption, inheritance, country loss and cleanup, contradiction tracing across flag kinds and nested scopes, installed/offline predicate comparison, vanilla retirement precedent inspection, and bounded migration and acceptance-case design.
No implementation validation is claimed, and no runtime character behavior, heir ranking, viable supply predicate, or permanent resolution result has been observed.
No simplification or fallback was applied to gameplay.
Unresolved design mechanics and unavailable MCP evidence are explicitly retained rather than certified as completed work.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or changed.
Focus, GUI, map, decisions, mission scoring, and localisation implementation remain outside this bounded architecture task.

## Evidence inventory

Workspace root for relative paths: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Vanilla root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
All revisions here are raw local SHA-256 hashes, not MCP-returned revisions or Git acceptance claims.

| Relative source | SHA-256 |
| --- | --- |
| `AGENTS.md` | `38E479CB75828BA888860BE8BC3739F9286C0D925CC7D8DE5ECD3B8DADEC46CF` |
| `.agents\skills\chaos-redux-events\SKILL.md` | `73997F2A68D57D4A1BDC231E070773ED9FAD54A0B8CCC29BBB4832CD028B50D6` |
| `.agents\skills\chaos-redux-subagents\SKILL.md` | `62D1531407A24BBBE0D7844CCA3439132CFC4A1BF2CCCBF4180C76725AF69D31` |
| `common\scripted_effects\039_murder_mystery_character_effects.txt` | `E59BAE0A5B51F4E2C1508BEC5986D14D85E96599A78FEF576A61C32B95EDCCC0` |
| `common\scripted_effects\039_murder_mystery_integration_effects.txt` | `98928E7645082F7CC453FAD74FAE4DFDDA2D75381A5A266D569D5B9A3BADDFEC` |
| `common\scripted_effects\039_murder_mystery_runtime_effects.txt` | `8F4B63001770D286E1E9DE736A9ABFFC4378F02273D2CA0B782CCE0837D9085A` |
| `common\scripted_triggers\039_murder_mystery_runtime_triggers.txt` | `B5E45B0D09C95C7B670AEC96A9150F11A804F1AF705C80D6E064872CCE94CFD0` |
| `common\scripted_triggers\039_murder_mystery_integration_triggers.txt` | `16F2972DD0085000611BBFC5530458F6C7AE80BAE6BD80B4409860765861C2B7` |
| `common\script_constants\039_murder_mystery_constants.txt` | `8C9F93E35E4AE5F60BCB75486CC76AC165AF90E825B3C02C4136CB751DE8CE18` |
| `events\039_murder_mystery.txt` | `5B582C80DF580C85DBA01077CCCD734154F6CF2329DEAEC2C454501D79EDC367` |
| `common\scripted_effects\chaosx_dynamic_effects.txt` | `91B4609D44FC19D619FC8B6D22EF4A32B78D20AC14F9F2EF58A1B9DA152D7C04` |
| `common\scripted_effects\chaosx_dynamic_effects.md` | `E421A3EF6D4F96B9335FA7644D56DE3CDA104EE3E9508387B3A7E0BD365C6CE0` |
| Spec Part 3, `docs\specs\039_murder_mystery_specs\039_murder_mystery_spec_part_3_character_safety.md` | `509B1F07EE03EF995DA804E42E272899A0FCA43CC8D704E54F844BAB790E862B` |
| Spec Part 5, `docs\specs\039_murder_mystery_specs\039_murder_mystery_spec_part_5_international_network.md` | `AAFE40079A6B287FD086FC1872DA45FAC55B50854DC17DE30DEAFE46FF404E52` |
| Spec Part 6, `docs\specs\039_murder_mystery_specs\039_murder_mystery_spec_part_6_assassin_state.md` | `4A8386D66AFF165D09AE9A047BEF4F4B295C378FF72D78BF03B1EF403A0AC60A` |
| Spec Part 18, `docs\specs\039_murder_mystery_specs\039_murder_mystery_spec_part_18_acceptance.md` | `916C0B169F69EF10A081E3FDE0704A8AC7DC1E7D319310298A79533A556E3428` |
| `paradox_wiki\Character modding - Hearts of Iron 4 Wiki.md`, sections 33-59 | `8EF3D5F9923026DD81F239944710B7331A8D06AD42E4345B32FCE4E86DD95D98` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, sections 263-275, 303-327, 1514 | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md`, sections 25-63, 250-266, 401-402 | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md`, sections 2733-2759 | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md`, lines 638, 1758, 2033, 2052-2053 | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| Vanilla `documentation\effects_documentation.md`, cited sections above | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Vanilla `documentation\triggers_documentation.md`, cited sections above | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Vanilla `documentation\script_concept_documentation.md`, lines 216-245 | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| Vanilla `common\script_constants\documentation.md`, schema lines 1-32 | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| Vanilla `events\GOE_Iraq.txt`, lines 1357-1362 and 1440-1445 | `51B13BB87D07225AF21BE7488139AE1D67964295590FE2F6A200F7D6C3709C54` |

## Final transport and auditor addendum

The `reference_search` and `source_lookup` requests each returned a tool-call error caused by `timed out awaiting tools/call after 600s`.
Neither returned a documentation or source artifact, revision, or coverage result.

The first `event_inspect` request was rejected with `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.event_inspect: Invalid input: expected object, received string at stateSubject`.
The exposed schema describes `stateSubject` as unknown, and this researcher supplied an unsupported string.
This is a request-shape failure, not evidence that the event service is unhealthy.
A retry omitted that optional field and used `mode = state_flow`, `maxDepth = 1`, `maxNodes = 10`, and `maxEdges = 15`, within the exposed parameter contract.
It produced no response within a local 15-second bounded wait.
No event inspection result or coverage proof was obtained.
This retry does not establish exact Event039 graph selection or lifecycle coverage.
No render or comparison was requested after the prerequisite inspection failed to provide a graph.

The delegated `chaosx_ai_probability_auditor` completed its inline-only pass as agent `01a10141-13e1-7930-aa38-83f310d1b22a`.
It independently attempted `probability_inspect` on the same source object and obtained no response within its local 15-second wait.
Its exposed adapter list includes `direct_random` and `random_list`, but has no explicit `random_character` adapter.
Whether another adapter models character selection remains unresolved.
The auditor returned no artifact URI, source revision, diagnostic, analysis ID, or scenario hash.
All five named `INC_NO_FOREIGN_ROWS`, `INC_ONLY_PROTECTED_OR_RETIRED_ROWS`, `INC_MATURE_FOREIGN_CELL`, `INC_VIABLE_CENTRAL_STATE`, and `INC_USED_CAP` scenarios remain unresolved because there is no complete pool/fixture or analyzer result.
No evaluate, sweep, compare, simulation, sequence, or probability render was performed.
There is no immutable before-source snapshot or applied owner patch for a valid comparison.
The auditor confirmed that downstream owner/named-action gates exist, so the random selector excerpt alone does not prove unsafe retirement is reachable.
This handoff's current-defect findings identify missing identity/ownership guarantees and inconsistent source receipts, with actual native reachability left unverified.

Only this handoff was authored by this task.
The five named effect/trigger working-file hashes were reread after handoff drafting and still match the evidence inventory, so the line-anchored candidates refer to the parent work inspected here rather than an older committed implementation.
Helper documentation, call sites, constants, cleanup, localisation, and implementation acceptance remain owner follow-up, with no gameplay simplification applied.
The parent should treat the candidate hunks as review material and keep the Event039 goal incomplete until the required owner patch and blocked evidence are resolved.
