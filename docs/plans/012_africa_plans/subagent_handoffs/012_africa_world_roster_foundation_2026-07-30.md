# Event 012 Africa world-order roster and polity foundation handoff

Date: 2026-07-30

Owner: `africa_world_roster_foundation`

Scope: six external continent package roster dispositions, constituent status, heartland proof, successor/exile/breakup lifecycle, and the mixed-readiness Scramble aftermath close.

## Files changed

- `common/script_constants/012_africa_world_order_constants.txt` adds `africa_world_constituent_status`, `africa_world_package_resolution`, and the `africa_world_roster` tuning category.
- `common/scripted_triggers/012_africa_world_order_triggers.txt` adds documented-roster, heartland, constituent, successor, exile, breakup, and terminal-resolution proofs, and requires a sovereign candidate to be unsubjugated.
- `common/scripted_effects/012_africa_world_order_effects.txt` adds one-time roster disposition recording, package polity initialization, heartland refresh, constituent outcomes, successor review, exile certification, breakup certification, lifecycle terminal proof, and mixed-readiness aftermath closure.
- `common/on_actions/012_africa_world_order_on_actions.txt` refreshes package heartland proof on state-control changes and invokes package-loss review on capitulation, peace-conference loss, and annexation.
- `common/decisions/categories/012_africa_categories.txt` adds `africa_world_polity_actions_category` for package actors.
- `common/decisions/012_africa_decisions.txt` adds targeted consent, refusal, coercion, withdrawal, successor, exile, and breakup decisions with centralised costs and AI weights.
- `events/012_africa_world_order.txt` adds `africa_world_order.110` for the explicitly documented partial/absent roster close.
- `localisation/english/012_africa_world_order_l_english.yml` adds all decision and roster-event wording and remains UTF-8 with BOM.
- `docs/events/012_africa/world_order.md` documents the foundation helper map, arrays, cleanup, and readiness boundaries.
- This handoff records the implementation evidence and limitations.

## Helper map

`africa_world_finalize_package_roster` runs from the host's one-time nomination pass and writes one integer disposition for each continent into `africa_world_package_resolved_continents`, `africa_world_package_pending_continents`, or `africa_world_package_absent_continents`.

`africa_world_initialise_package_polity_foundation` runs once per installed actor, preserves the original actor and host proof, records the actor as an initial consenting member, scans sovereign same-continent capitals into `africa_world_constituent_countries`, and records controlled same-continent states in `africa_world_package_heartland_states`.

`africa_world_refresh_package_polity_proof` is a narrow actor refresh called by `on_state_control_changed`; it rebuilds only the package actor's heartland state array and sets or clears `africa_world_package_heartland_proof` and `africa_world_package_heartland_lost`.

`africa_world_record_constituent_consent`, `africa_world_record_constituent_refusal`, `africa_world_record_constituent_coercion`, and `africa_world_record_constituent_withdrawal` update country flags, status variables, actor arrays, historical counters, and authority deltas without changing tags, cores, ownership, or opinion as a substitute for a polity result.

`africa_world_handle_package_actor_loss` opens a successor review after capitulation or annexation, nominates at most one eligible same-continent sovereign candidate, and otherwise opens an explicit exile or breakup certification path.

`africa_world_commit_package_successor`, `africa_world_record_exile_resolution`, and `africa_world_record_package_breakup` preserve the original actor record, clear review flags and candidate markers, and set lifecycle flags consumed by `africa_world_package_terminal_resolution_is_proven`.

## Roster and aftermath behavior

`africa_world_roster_is_documented` requires all six continent slots to have an explicit disposition.

`africa_scramble_can_close_continental_docket` now requires documented roster state, at least one uninstalled slot, all Scramble response clauses resolved, and no implementation-ready candidate remaining.

The aftermath mission tries full ratification first and then the Africa-only documented-roster close, preventing the prior mixed-readiness deadlock without inventing a proxy country.

The partial close sets `africa_world_order_deferred` and fires `africa_world_order.110`; it does not open World-Order Council decisions or set any package/model/super-event readiness flag.

## Constants and tuning

`africa_world_roster.minimum_heartland_states` is the controlled-heartland threshold.

`africa_world_roster.minimum_constituents` is the minimum ledger size, including the original actor.

The same category centralises consent, refusal, coercion, withdrawal, successor, exile, and breakup decision political-power costs and authority deltas.

No duration field or unsupported dynamic field was added.

## Parent review corrections

Parent review changed the four authority-loss constants to negative values so refusal, coercion, withdrawal, and breakup reduce authority as their names and tooltips require.

Parent review prevents the original package actor from targeting itself with the constituent-withdrawal decision.

Parent review requires every registered constituent to leave the pending state before `africa_world_package_constituent_settlement_is_proven` can pass.

Parent review made successor nomination actor-local, excludes a country already nominated by another package, and removed the empty deferred-host polity category.

## Event targets, arrays, and cleanup

The existing `event_target:africa_host` remains the only persistent host pointer used by this tranche.

Package-local arrays are actor-scoped and include constituent countries, consented/refused/coerced/withdrawn subsets, heartland states, and successor candidates.

The host's disposition arrays are rebuilt only by the one-time census and event-driven installation refresh.

Successor candidate flags are cleared after successor commitment or breakup certification.

Breakup clears active constituent membership and records withdrawal status for each affected ledger entry.

No recurring all-country on-action was introduced.

## Migration from duplicated logic

The pre-existing random nomination and dead `africa_world_package_roster_incomplete` flag now feed the central disposition helper and its accepted consumer.

Package installation calls polity initialization immediately after the existing distinct-mechanic initializer, and then refreshes the host disposition arrays.

Terminal resolution counting now requires the package proof helper instead of trusting a bare counter.

Existing sponsorship, focus, union, war, and terminal readiness call sites remain intact, and neither readiness flag receives a setter.

## Validation

Brace-count checks across all touched Clausewitz files reported balanced blocks.

`git diff --check` reported no whitespace errors in the touched changes; its output only contained expected LF-to-CRLF notices for the shared worktree.

The localisation file header remains `EF BB BF`.

No unsupported `<=` or `>=` operators were introduced.

The read-only Event Chain Viewer lint was run for `africa_world_order.110` and the world-order effects source. The reports returned status `ok` with no blocking diagnostics, but analysis was marked partial because the configured MCP workspace scanned vanilla sources and deferred the full mod helper projection.

Event-lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ad2b16d308b7e81261d58af95aa494fbe5447f9bd30bbe9b4c633c4bbc2b888/bb0b80de1324f0781d0be312bda7f16a9cd7a19975694e64bebeb484801a0727/event-lint-6f5cefb4cfce.json`.

Event-scan artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d196939006b95cee37e1db8d9eeb9d142ab709bd93659dd7a2b0f745f05562c/1052081dac7868432c672766438c36f5128309b785119e41f6b1ff24718210b1/event-scan-f84da2c23776.json`.

## Risks and unsupported analysis

The MCP report did not ingest the mod's local scripted-effect and decision sources, so runtime scope semantics for the new actor-local arrays still need parent review against the game parser or live save validation.

Annexation can remove an actor before a player can use its successor certification decision; the on-annex hook records the review on the surviving actor scope but does not invent a successor or transfer a package identity.

The six external focus trees, identity art, dynamic union wars, final presentation, and readiness gates remain intentionally outside this tranche.

The implementation does not set `africa_world_package_implementation_ready` or `africa_the_world_super_event_package_ready`.

No fallback country, continent-wide core grant, instant annexation, opinion-only integration, workbook update, acceptance-ledger update, or commit was made by this subagent.
