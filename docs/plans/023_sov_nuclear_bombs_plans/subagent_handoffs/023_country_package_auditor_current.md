# Event 023 country package auditor handoff

Status: PARTIAL. The bounded Event 005 release bridge and the three breakaway-stage effect guards were patched and reviewed, but the package is not ready for unconditional sign-off because native queued reactor construction cannot be cancelled by any documented effect and the Stage 1/2 route interpretation remains unresolved.

Date: 2026-09-05.

## Scope

This audit covers Event 023 Soviet-collapse country and custody integration only.

The allowed gameplay write scope was `common/on_actions/023_sov_nuclear_bombs_on_actions.txt`, `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`, `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`, and `common/scripted_effects/005_soviet_collapse_effects.txt`.

No SOV history, focus, leader, portrait, flag, country-definition, tag, unit, map, decision, trigger, or unrelated country system was edited.

## Evidence used

- Offline wiki pages consulted before source review: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.
- Vanilla documentation consulted: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`.
- Vanilla precedents consulted: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/00_on_actions.txt` for `on_release_as_free`, `on_release_as_puppet`, `on_annex`, `on_state_control_changed`, and `on_nuke_drop`, plus the vanilla Philippines nuclear-reactor focus and nuclear special-project building effects.
- Event MCP post-change lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9495899e317b825db01431cfe15901525036fc63e042d80d25dade52b1926dcf/e18ea383f8a2d21bf65b1dd674770bc89ea2e490cef533a04e33147a1d92d008/event-lint-e091020adf34.json`.
- Event MCP post-change state render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11c54a7943a346767e1e40e8f0e313851f72f7d9a9b50e34cdf47ffa9d9da4ed/6d3411b13e8b98b86be047b5a81e3c66a98fdb2d86873de1787a3a525c1b690e/event-state-e091020adf34.json`.
- The post-change Event Viewer returned `EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, and `validation = false` because helper/lifecycle analysis was deferred across the large workspace; the graph was focused and the inline inventory was truncated.
- Artifact-backed Event 023 compare timed out after 180 seconds, so the visual/source before-and-after comparison is not engine evidence.
- Read-only `hoi4.map_inspect` and `hoi4.map_render` calls for the state/building/supply/railway surface each timed out after 180 seconds.
- Read-only `hoi4.tech_inspect` and `hoi4.tech_render` calls for the `atomic_research` dependency each timed out after 180 seconds; no technology artifact was received.
- The mandatory delegated probability audit `chaosx_ai_probability_auditor` (`01a06e9c-102e-7721-8f2b-3cbeb44c41d2`) did not return an artifact after multiple wait windows and was shut down while still running; no probability result is claimed.

## Country package coverage checklist

| Surface | Evidence | Result |
|---|---|---|
| Event 005 pre-transfer snapshot | `common/scripted_effects/005_soviet_collapse_effects.txt:4267-4385` | PASS after patch: all four existing release-host branches snapshot immediately before their existing `release` effect. |
| Post-transfer reconciliation | `common/on_actions/023_sov_nuclear_bombs_on_actions.txt:23-46`; `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:1129-1303` | PASS in source and focused MCP: the state callback uses exact `FROM.FROM`; release callbacks reconcile only pending states in the released country’s owned/controlled set. |
| Owner/controller/custody/access separation | `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:55-99,648-906,1182-1286` | PASS: ledger owner/controller pointers, custody state, technical denial, operationalization, command, and delivery flags are separate. |
| Immediate breakaway use prevention | `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:466-584,648-709`; `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:44-132` | PASS for native action: transferred custody is not an allowed launch source, and operationalization occurs only after the staged chain. |
| Three staged access missions | `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:2195-2335`; `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:702-717,773-794` | PARTIAL: every start/completion effect now rechecks exact state validity, current owner/controller, and `breakaway_physical` custody; full delivery route is only checked at Stage 4 by design. |
| Ledger conservation on restoration | `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:55-99,837-906` | PASS by source arithmetic: restoration reclassifies operational/transferred buckets into assigned custody, moves actor attribution, and does not change total registered/accounted quantities. |
| Annexation, side-change, and target cleanup | `common/on_actions/023_sov_nuclear_bombs_on_actions.txt:23-63`; `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:1182-1358` | PARTIAL: exact state reconciliation and bounded annex cleanup exist, but the global selected/pending target cleanup is not actor-specific under concurrent contexts. |
| SOV disappearance | `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:8-14`; `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:22-26`; runtime refresh at `55-99` | PASS by source: Soviet production/evolution actor gates require existing SOV, while the bridge and local state ledgers do not. |
| Pending reactor on control loss | `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:201-216,315-405` | FAIL: Event 023 bookkeeping is cleared, but the native queued `add_building_construction` job is not cancelled. No documented supported queue-cancellation effect was found. |
| Duplicate nuclear consequences/hooks | `common/on_actions/023_sov_nuclear_bombs_on_actions.txt:65-112`; runtime `480-489` | PASS: one Event 023 `on_nuke_drop` hook and one `launch_nuke` call exist; Chaos/Fallout/humanitarian/achievement hooks remain separate consumers. |

## File surface checklist

| File | Inspected | Changed | Notes |
|---|---:|---:|---|
| `common/on_actions/023_sov_nuclear_bombs_on_actions.txt` | Yes | No | Exact state, release, annex, and nuke callbacks are present and bounded. |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | Yes | No | Ledger, custody, action, reconciliation, and cleanup helpers were reviewed. |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | Yes | Yes | Added current custody checks to all three stage starts and completions and made delivery completion explicitly Stage 4. |
| `common/scripted_effects/005_soviet_collapse_effects.txt` | Yes | Yes | Moved the Event 023 snapshot from the parent’s unconditional SOV call into each actual release host immediately before `release`. |
| `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_country_package_auditor_current.md` | Yes | Yes | This handoff. |

## Findings

### Event 005 snapshot and exact reconciliation

`soviet_collapse_release_scope_from_soviet_collapse_owner` has four existing release paths: SOV host, original-union owner host, breakaway/republic/subject owner host, and controller host.

The Event 023 snapshot now runs inside each host at `005_soviet_collapse_effects.txt:4290,4314,4349,4384`, directly before the corresponding `release = event_target:soviet_collapse_dynamic_release_target` at the next line.

The previous single SOV-scope call would not cover release paths hosted by a non-SOV owner/controller and could snapshot unrelated SOV-owned target-core states, so it was removed without changing the existing release predicates or release effects.

`on_state_control_changed` follows the vanilla `ROOT = new controller`, `FROM = old controller`, `FROM.FROM = exact state` contract and calls reconciliation on that exact state.

The free and puppet release callbacks call country reconciliation, which scans only `every_owned_state` and `every_controlled_state` with the pending snapshot flag and therefore does not perform a world-wide loop.

### Custody and staged access

The runtime ledger distinguishes operational, assigned, reserved, transferred, dismantled, missing, and expended quantities, and separately records site owner, controller, holder actor, custody state, technical denial, and operationalization.

`sov_nuclear_bombs_operationalize_breakaway_site` only converts transferred custody into a breakaway operational actor after the explicit final delivery stage calls it.

All three start helpers and all three completion branches in `023_sov_nuclear_bombs_event_effects.txt:2195-2335` now require the selected state to be registered, transferred, non-terminal, non-denied, owned or controlled by the current actor through the existing helper, and explicitly set to `constant:sov_nuclear_bombs_custody.breakaway_physical`.

The native action validator accepts transferred custody only for demolition, and the non-demolition path has one `launch_nuke` call. Breakaway physical possession therefore cannot launch immediately.

The literal requirement that all three stages require the full bomber/airbase delivery route is not fully met. `sov_nuclear_bombs_event_has_local_delivery_capability` remains a Stage 4 gate because the accepted Event 023 specification says Stage 2 still lacks a verified launch route and Stage 4 is where current delivery-platform and exact-route requirements are applied.

This is an unresolved design contract between the user’s audit criterion and `docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_spec_part_6_soviet_collapse_integration.md:80-125`; adding the full delivery predicate to Stage 1/2 would also require aligning the out-of-scope decision availability and cost path in `common/decisions/023_sov_nuclear_bombs_decisions.txt:1055-1094`.

The selected state is a mutable global event target and the scoped files have no safe state-identity trigger for clearing it on side change. The exact state callback updates custody, and completion now fails closed when the target drifts, but a visible active mission can remain until its cancel/timeout path.

### Ledger conservation and cleanup

`sov_nuclear_bombs_refresh_ledger_reconciliation` derives physical custody from operational, assigned, reserved, and transferred buckets and derives accounted total from those buckets plus dismantled, missing, and expended quantities.

`sov_nuclear_bombs_restore_site_to_soviet` moves the current operational/transferred site quantities to assigned SOV custody, decrements the former holder actor, adds SOV actor attribution, clears transferred/operational site buckets, and leaves the global total unchanged.

Annexation is bounded by the Event 023 actor/operational/transfer predicates in `on_actions/023_sov_nuclear_bombs_on_actions.txt:48-63`. The cleanup helper clears action context and transient actor targets while intentionally leaving site ledgers to exact state callbacks.

Residual risk: `sov_nuclear_bombs_cleanup_annexed_actor` can clear the global pending-reactor target and selected state target without proving that the pointed state belongs to the annexed actor. No safe state equality predicate was found in the allowed files, so no broader cleanup rewrite was invented.

### Reactor construction and control loss

`sov_nuclear_bombs_queue_reactor_site` uses the state-scoped vanilla `add_building_construction` effect and records a state pending flag plus a global pending-state target.

The exact control-change callback clears the state marker, global pending target, SOV pending count, and SOV bookkeeping flags when control is lost.

Vanilla `effects_documentation.md` documents `add_building_construction`, `set_building_level`, and `remove_building`, but no queued-construction cancellation or construction-job identity effect. Repository and vanilla searches also found no supported `cancel_building_construction` or equivalent.

Using `remove_building` or `set_building_level` as a substitute would affect completed reactor levels rather than reliably cancelling the queued job and could corrupt a replacement owner’s construction, so this remains a blocker for the parent/system owner.

### SOV disappearance and duplicate hooks

The Event 023 primary actor trigger requires `tag = SOV` and `exists = yes`, which halts Soviet-only production, evolution, and command routes when SOV disappears.

The collapse bridge trigger requires the active collapse and ledger state but does not require SOV to exist, and ledger refresh sets Soviet usable devices to zero without deleting per-state or breakaway actor buckets.

The Event 023 `on_nuke_drop` hook is unique to `023_sov_nuclear_bombs_on_actions.txt`. The other `on_nuke_drop` hooks belong to the shared chaos-meter, humanitarian, and achievement systems, and the Event 023 runtime deliberately does not call their consequence effects directly.

### Country, map, politics, and package identity

No new country tag, state definition, core, claim, capital, victory point, port, rail, resource, building, leader, portrait, flag, advisor, party, focus, unit, or technology was added by this bridge.

Opening storage selection uses existing owned-and-controlled, non-impassable, non-capital states in `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:121-167`, and the state callbacks use the correct vanilla state scope.

There is no static Event 023 map package to audit or rewrite in this bounded task. The required read-only map inspection and rendering calls timed out after 180 seconds, so supply, railway, port, and state-building conclusions are source-level only and not MCP-verified.

Event 023 uses vanilla `atomic_research`, `nukes`, `strategic_bomber1`, and optional `iw_large_airframe` checks rather than a custom technology tree. The installed MCP evidence notes that a standalone Technology Tree Viewer is absent; this is recorded as a package capability gap, not as a claim that the exposed technology routes are healthy.

Because the requested write scope excludes country identity and static setup files, no politics, leader, portrait, flag, advisor, party, focus, starting army, navy, air force, equipment, manpower, supply, or production-package defect was introduced or patched here.

### AI and playability

The source has breakaway decision weights of `0.40` for technical access, `0.25` for command formation, and `0.10` for delivery integration at `common/decisions/023_sov_nuclear_bombs_decisions.txt:1055-1094`; the operationalization mission is non-selectable and has a flat `0.20` score in the mission definitions.

The previous probability handoff `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_ai_probability_baseline.md` recorded missing engine baselines for the same collapse scenarios.

The mandatory current `chaosx_ai_probability_auditor` route was delegated but returned no result or artifact after multiple wait windows and was shut down while still running, so no MCP probability, timing, or ranking claim is made and no AI weight was changed.

The existing flat weights and mutable selected-state target remain playability risks, but their decision and trigger files are outside this subagent’s bounded patch scope.

## Changed files and exact behavior

### `common/scripted_effects/005_soviet_collapse_effects.txt`

- Changed `soviet_collapse_release_scope_from_soviet_collapse_owner` only.
- Before: the parent’s Event 023 snapshot call ran once in unconditional SOV scope before branch selection.
- After: each of the four existing actual release hosts calls `sov_nuclear_bombs_snapshot_event5_release_tranche = yes` immediately before its existing `release` effect.
- Existing release conditions, autonomy decisions, and post-release effects were preserved.

### `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`

- Changed `sov_nuclear_bombs_start_breakaway_technical_access`, `sov_nuclear_bombs_start_breakaway_command_formation`, `sov_nuclear_bombs_start_breakaway_delivery_integration`, and `sov_nuclear_bombs_complete_breakaway_operationalization`.
- Added the exact `breakaway_physical` custody-state check to every staged start and completion branch.
- Before: the completion `else` path could fall through to delivery for any non-technical/non-command stage.
- After: delivery completion requires the explicit delivery progress stage, current crisis, command formation, local delivery capability, current selected state, and `breakaway_physical` custody before operationalization.

The inspected `023_sov_nuclear_bombs_on_actions.txt` and `023_sov_nuclear_bombs_runtime_effects.txt` were not changed.

## Validation and skipped validation

- The four scoped gameplay files have balanced Clausewitz blocks with final nesting depth zero after the patch.
- Source assertions found exactly four Event 005 snapshot call sites, all immediately followed by an existing release, six staged custody checks, one Event 023 `on_nuke_drop` hook, and one runtime `launch_nuke` call.
- Event MCP lint and state rendering returned partial focused artifacts with no blocking diagnostics, but workspace-wide validation remained false because helper/lifecycle analysis was deferred.
- Event MCP compare was attempted with before/after artifacts and timed out after 180 seconds.
- Map MCP inspect and render were attempted for state/building/supply/railway evidence and each timed out after 180 seconds.
- Technology MCP inspect and render were attempted for the vanilla nuclear prerequisite surface and each timed out after 180 seconds.
- The probability audit was attempted through the required specialist route and timed out without an artifact.
- Live HOI4 execution was not run, as live consumer validation belongs to the user.

## Remaining blockers and risks

1. Native queued reactor construction is not cancelled on control loss; only Event 023 bookkeeping is cancelled.
2. The user’s “route on all three stages” criterion conflicts with the accepted Stage 2 separation that denies a verified launch route until Stage 4, and the out-of-scope decision availability/cost path would need alignment.
3. Mutable global selected/pending targets are not proven actor-specific during simultaneous annexation or side-change cleanup.
4. Event compare, map evidence, and probability evidence are unavailable because the MCP calls timed out; source review is not being treated as equivalent engine evidence.
5. The installed standalone Technology Tree Viewer is absent and the exposed technology inspect/render calls also timed out, although Event 023 does not define a custom technology tree.

## Parent integration checklist

- Resolve a supported construction-queue cancellation/receipt callback before claiming the control-loss requirement complete.
- Decide whether “route” means full vanilla delivery capability at all three stages or the narrower custody/state route, then align the Event 023 spec and out-of-scope decision availability path.
- Add state-identity-safe mission and global-target cleanup in the owning decision/trigger surface if side-change concurrency must be fully closed.
- Re-run Event MCP compare, map inspection/render, and the named probability scenarios when those services return results.
- Re-run the vanilla technology dependency inspection/render when the route returns results.

Disposition: bounded implementation is recorded as implemented with unresolved blockers; no broad redesign, fallback effect, new tag, new unit, whole-world loop, or unsupported queue-cancellation effect was added.
