# Event 032 payload observation boundaries

Date: 2026-10-08.
Disposition: read-only review completed, proposed call sites remain `unresolved` pending parent implementation.
Only this handoff was written.
No gameplay, stock, policy, arithmetic, log, ownership, Git, game, or agent changes were made.

Use the existing COUNTRY helper `missiles_note_payload_change = yes` from `common/scripted_effects/032_missiles_evolution_effects.txt:248-253`.
It checks the current country's initialized/not-cleaned program flags and delegates to the coalesced observation owner.
It needs the affected country as current scope and does not require a new ROOT-binding event.
Put calls at completed owner transactions, after their stock and receipt work, inside the existing acceptance branch.
Do not add a second debit, refund, policy gate, or ownership mutation.

## Nuclear owners

`E` below is `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`.
`R` is `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`.
The ten supplied native writes map to seven owner methods.

| Current owner | Native writes | Proposed completed boundary and COUNTRY scope |
| --- | --- | --- |
| `sov_nuclear_bombs_initialize_event_state`, E:516-582 | E:568 | After E:580 inside the one-time opening branch. Plain call in the current Soviet actor COUNTRY after registration, opening sites, evolution/posture setup, and final opening assessment. Do not hook the earlier ledger-only registration helper. |
| `sov_nuclear_bombs_credit_evolution_devices`, R:408-431 | R:422 | After R:429 inside the accepted tranche branch. Current credited COUNTRY, after native stock, ledger credit, stage receipt, input cleanup, and reconciliation. |
| `sov_nuclear_bombs_register_production_devices`, R:437-460 | R:451 | After R:458 inside the accepted completed-batch branch. Current producing COUNTRY. This is an event-owned production transaction, not a generic native-production callback. |
| `sov_nuclear_bombs_commit_reserved_device`, R:680-784 | R:697,776 | After R:782 inside the accepted commit branch. Current action COUNTRY, whose native inventory is used, after reservation closure and reconciliation. This shared endpoint also receives verified native-delivery commits, so do not duplicate a notification in each arithmetic or confirmation caller. |
| `sov_nuclear_bombs_operationalize_breakaway_site`, R:1210-1300 | R:1286 | After R:1298, enter the proven `var:sov_nuclear_bombs_site_holder` COUNTRY for the completed grant. The method itself runs in STATE scope. The source already proves the recipient's existence and native custody conditions. |
| `sov_nuclear_bombs_mark_site_transferred`, R:1304-1431 | R:1348,1370 | After R:1429, notify the source COUNTRY participants: SOV and the validated retained former `var:sov_nuclear_bombs_site_holder` where applicable. The helper still retains that holder at this point. The newly capturing controller receives physical custody here, not a native-stock grant. Preserve the distinction. |
| `sov_nuclear_bombs_return_site_custody_to_soviet`, R:1503-1591 | R:1561,1564 | After R:1581 inside successful settlement, notify SOV and the former native holder when the holder-debit branch ran. The former-holder identity must first be retained through settlement as described below. |

The return method overwrites `sov_nuclear_bombs_site_holder = SOV` at R:1568 and clears the native-with-holder marker at R:1573.
Consequently, a simple appended holder lookup at R:1581 would address SOV twice and miss the losing country.
Retain a valid per-transaction old-holder reference through successful settlement, using an existing caller receipt if suitable or a narrowly scoped notification-only reference.
A chain-local event target would need current-transaction validity as well as existence, because regular targets can remain from earlier work in the same chain.
Do not introduce persistent ownership changes or move the notification into the native arithmetic to avoid this identity requirement.
Notifying only SOV is insufficient when only the losing holder has an Event 032 program.

No notification belongs in generic ledger refresh, reservation-only moves, or the periodic native-use reconciliation path.
These inventory operations do not establish a new native payload gain/loss every time they run.
Keep Event 023 authorization and custody ownership and Event 076 Fallout ownership unchanged.
The existing native detonation pipeline continues to own consequences.

## Biological owners and current consolidation

The current bytes contain neither `common/scripted_effects/biological_operation_effects.txt` nor `common/operations/chaosx_bioweapon_operations.txt`.
Targeted `rg` found no remaining `bio_operative_release_*` definitions, and `hoi4.source_lookup` returned zero definitions for `bio_operative_release_dispatch_seed_internal`.
The old operative documentation and its line pointers are stale.
The dated competing-operations handoff describes retirement into existing native raid routes, and those current bridge definitions and consumers were verified directly.
No deleted source was restored or treated as an implementation target.

| Current owner | Proposed completed boundary and COUNTRY scope |
| --- | --- |
| `bio_facility_capture_initialize_exact_state_ledger`, `common/scripted_effects/biological_facility_capture_effects.txt:106-194` | After capture settlement at the method tail, notify the existing, living `var:bio_stockpile_safety_arsenal_actor` COUNTRY. The method runs in STATE scope. It removes the original custodian's unallocated national payload once and then commits the state ledger and notices. Current controller or callback ROOT is not a substitute for that stored custodian. |
| `bio_facility_capture_restore_on_original_recapture`, same file:210-262 | After line 260 inside the valid recapture branch, enter CONTROLLER for one notification. The entire four-model restoration and captured-ledger closure have completed. The original custodian is the current controller on this guarded path. |
| `bio_facility_capture_transfer_fraction_to_controller`, same file:335-382 | At the end of the existing CONTROLLER block after line 380, notify once when the transfer total is positive. This is the central four-model recovery transfer, after state-ledger recomputation and country receipt updates. Do not notify separately after each model's arithmetic. |
| `bio_stockpile_safety_resolve_selected_ordinary_accident`, `common/scripted_effects/biological_stockpile_safety_effects.txt:685-753` | At the end of the supplied stock-loss-proof branch, after the final notification choice at line 750, call in the current arsenal COUNTRY. Preserve the existing proof gate. Avoid `refresh_risk_band`, monitor scheduling, stock snapshots, and the individual debit branches. |
| Native biological completion bridges, `events/biological_native_raid_bridge_events.txt:64,125,186` | Add one plain COUNTRY notification after each current resolver returns, inside its existing exact-actor/agent/outcome bridge gate: `.1` after `bio_resolve_battlefield_dissemination`, `.2` after `bio_resolve_supply_chain_raid_outcome`, `.3` after `bio_resolve_strategic_raid_outcome`. These hidden country events already bind the raid actor as ROOT/current country. |

The three live resolver definitions are `biological_battlefield_effects.txt:497-555`, `biological_sabotage_raid_effects.txt:161-207`, and `biological_raid_effects.txt:570-653` under `common/scripted_effects/`.
Their actor targets are respectively `bio_battlefield_actor`, `bio_sabotage_actor_target`, and `bio_raid_actor`.
The current raid definitions enter `var:actor_country` and fire these country bridges.
Raw `actor_effects` starts in RAID_INSTANCE scope, so the COUNTRY notifier must not be inserted there without entering the actor.

A completed native raid can have already consumed equipment even when its outcome fails or its lifecycle dispatch is rejected.
The bridge notification therefore belongs after the resolver returns, outside its success-only internal branches, while retaining the bridge's existing identity gate.
It observes current stock only and must not invent a debit or refund.
Native collection occurs after raid creation, so a completion notification does not establish immediate collection-time observation or coverage of cancellation/refund cases without a callback.
Those remain observation gaps, alongside native production and generic research completion.

`biological_lifecycle_effects.txt` contains no native stockpile add/remove call in the inspected current file.
Its state-scoped seed, disease ticks, spread, attribution, and recovery are not stock transaction owners.
Do not use lifecycle dispatch or recurring ticks as a substitute stock observer.
Likewise, facility destruction and third-party controller updates act on an already-detached state ledger and should not produce another national stock-loss notification.

The parent's chemical conversion, proven debit, profile-change, and finite `.193` expiry hooks are excluded from these recommendations.
No duplicate chemical subscriptions are proposed.

## Evidence and limits

All fifteen queried symbols were checked against current source lookup.
Fourteen live definitions resolved without overrides at workspace revision `c074741ffe9b6d3e299fce423b9ba5aaaf3e8a0f5d12371112488e576e01d38c`, and the retired operative helper resolved to zero definitions.
Relevant transaction blocks and their actual nested COUNTRY/STATE scopes were read locally, beyond the bounded lookup excerpts.
The supplied notifier resolved at revision `96d0ca37d327a0e35df7bb626d71c6e3c699a7e4ab9db15621694574bbbb041a`.

Reference reads: installed `documentation/effects_documentation.md:1252-1266,1804-1812`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:1516`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
Installed `common/raids/_documentation.md:167-180,243-298,548-557` establishes native collection timing and RAID_INSTANCE actor scope, SHA-256 `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e`.
Vanilla `common/raids/land_infiltration_raids.txt:111-129` was inspected as a native outcome-block precedent.

Current file SHA-256 anchors: Event 023 event effects `5731ac6922418322fc7d6870ff015d07d1c6465c47951b32e917313c8c683f9f`, Event 023 runtime effects `8a071d832f2aabf8a4c37ac85680ebcd61be60bc4a4b912449d28e407d2de338`, facility capture `00d870fe2fc877ca389368b5809b5b9ec741fcf9bab018fdf524fc158fad34f0`, stockpile safety `610af2118ef4fa2a5b195c4e799f12dbfe97475ce66c8374ab4286bf54285c75`, lifecycle `48c76e4f94eaba0f4a071649adf07bcd2de032cfbe5c9931c9bb9e9f6bcd9b9c`, native bridge events `5796e5527386360858b3bfc9fa7ca85f2dc6b03c92a8c27fe774325d0085bbbc`.

Focused MCP traces for `chaosx.nr23.1` and biological bridges `.1-.3` returned `EVENT_INSPECTED_PARTIAL`, revision `56af34a28398270c41e0b96f0f3a24fd68a89a02b5af35d57a2040adcc0e5143`, with zero helper projections.
These are bounded source evidence, not complete helper lifecycle or runtime proof.
- `chaosx.nr23.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c506b3bec76bde667b28fea440e007595640260ea50c22bb3275ebbd21a07ac/eacf07900124a81ffc785d0ae374f142fb59c4532f688e13f6223dc084fc81db/event-trace-56af34a28398.json`.
- `biological_native_raid_bridge.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5be7d0d8c399ff5307fc5a9050801b54594b4c1e0173ef95f596186bf417c018/24cc3c9347a47c861981b43f433088586ff117bf652ff177a6ccebe4b74a7b56/event-trace-56af34a28398.json`.
- `biological_native_raid_bridge.2`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c1a136c0e16aecdb49f6e401d07d427b8c4178a5f2dab871ed6b6c9e4b9e290/1e20bc690a62acde975f2615c45a4755db53684258c98d817314746aa836c37e/event-trace-56af34a28398.json`.
- `biological_native_raid_bridge.3`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c5e39f8de6d6c31d00ed0cdf718ba1e22ed0003006a59570e8d09753f730b4c/e59d006595b5c774ef9f19fca54dc44ea4f3467ec8e22cb9b6bb1e27362f5e41/event-trace-56af34a28398.json`.

No probability evaluation, mutation tests, native runtime test, or whole-repository payload inventory was performed.
Coverage is the named Event 023 writers and biological owners plus the live replacement callbacks for the retired operative path.
No polling fallback or gameplay simplification was introduced.
Skills applied: events, subagents, and native raids, whose scope contract places the proposed native notifications in the existing actor-country bridge returns.
