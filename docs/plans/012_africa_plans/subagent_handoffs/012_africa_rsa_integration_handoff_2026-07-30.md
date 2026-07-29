# Event 012 RSA shared-entry integration handoff — 2026-07-30

## Status

The accepted RSA Allied-rupture package now has one reachable shared Event 12 entry route. Original SAF remains the player-led host, the vanilla `south_african_focus` tree is preserved, and the public `africa_rsa_start_allied_civil_war` effect is called exactly once from the canonical `chaosx.nr12.1` immediate block after the public branch gate succeeds. This handoff is implementation evidence for the parent agent; it is not a live-save completion claim.

## Files changed

- `common/scripted_triggers/012_africa_rsa_triggers.txt`
  - Added `africa_rsa_shared_entry_is_eligible` for the original SAF meaningful-tree exception.
  - The trigger reuses the existing African contact gate, Allied/ENG framework gate, autonomy list, capital/core checks, and owned/controlled Transvaal, Cape, and Natal port states.
  - Its bounded exile-patron check is deferred until `africa_prefire_contacts_frozen` exists, then requires `africa_rsa_has_exile_patron_candidate`.
- `common/scripted_triggers/012_africa_triggers.txt`
  - Extended `africa_has_any_eligible_host` with the RSA exception.
  - Added `africa_can_initialize_selected_host`, the single shared initializer OR.
- `common/scripted_effects/012_africa_effects.txt`
  - Added RSA to the existing one-shot weighted prefire pool and post-freeze validation.
  - Switched the canonical initializer to `africa_can_initialize_selected_host`.
  - Prevented the generic continental tree loader from replacing original SAF's meaningful tree.
- `common/scripted_effects/chaosx_settings_effects.txt`
  - Extended the existing Event 12 dispatcher validation with the RSA exception; no new dispatcher or world scan was added.
- `events/012_african_union.txt`
  - Root trigger accepts generic hosts or the RSA shared-entry trigger.
  - Immediate block initializes the host, then tests `africa_rsa_allied_branch_can_start` and calls `africa_rsa_start_allied_civil_war` once for SAF only.
- `common/script_constants/012_africa_rsa_constants.txt`
  - Added `africa_rsa_log` payload constants for opening governments, three settlements, exile continuation, and no-patron terminal.
- `common/scripted_effects/012_africa_rsa_effects.txt`
  - Added `africa_rsa_record_event_log_history` with explicit current-scope actor and payload inputs.
  - Recorded system rows at Coalition/Union opening, each settlement effect, exile transfer, and the explicit no-patron branch.
- `common/scripted_effects/chaosx_events_log_effects.txt`
  - Added a narrow RSA host actor fallback for Event 12 ordinary rows when the global `africa_host` target is available.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
  - Added payload-specific Event 12 title and detail branches before the generic Africa fallback.
- `localisation/english/012_africa_rsa_l_english.yml`
  - Added player-facing title/detail strings for all RSA system-history payloads. Existing concurrent RSA localisation edits were preserved and the UTF-8 BOM remains present.
- `docs/events/012_africa/overview.md`
  - Reconciled the stale “SAF external-only” wording and documented the shared-entry/loader/history helper contract.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_rsa_integration_handoff_2026-07-30.md`
  - This handoff.

## Helper map and call sites

| Helper | Scope | Inputs | Outputs/side effects | Call sites |
| --- | --- | --- | --- | --- |
| `africa_rsa_shared_entry_is_eligible` | COUNTRY, prefire SAF | Existing host state, faction/ENG relation, frozen-contact state | Eligibility only; no mutation | `africa_has_any_eligible_host`, weighted prefire selector, prefire validation, `.1` trigger, initializer OR |
| `africa_can_initialize_selected_host` | COUNTRY | Generic or RSA eligibility | Eligibility only; centralizes the one exception | `africa_initialize_selected_host` |
| `africa_rsa_start_allied_civil_war` | COUNTRY, original SAF | Public RSA gate | Existing snapshot, flags, dynamic civil war, opening events | Exactly one `.1` immediate call |
| `africa_rsa_record_event_log_history` | COUNTRY actor | Temporary `africa_rsa_history_payload` | One Event 12 system-history row, actor id, payload, view refresh, temporary cleanup | RSA opening, settlement, exile, no-patron effects |

## Constants and tuning

`africa_rsa_log.*` uses integer payloads `12001`, `12002`, `12004`–`12008`; the event id remains `constant:africa_event.id`. Existing civil-war ratios, costs, timing bands, and AI constants remain unchanged. No magic gameplay value was introduced.

## Event-target and cleanup plan

The integration reuses the existing regular/global targets. `africa_host` remains the Event 12 host ledger; `africa_rsa_continental_coalition`, `africa_rsa_allied_union_government`, and `africa_rsa_exile_patron` remain owned by the RSA package. The new history helper has no persistent targets and clears every temporary logging input after each row. Existing RSA victory cleanup still clears transient arrays, variables, flags, and global targets. The loader change prevents SAF tree replacement without creating a second tree.

## Migration from duplicated logic

No civil-war logic was copied into the shared event. The shared layer only admits original SAF and delegates all branch behavior to the existing public RSA effect. Event Log outcome text is payload-dispatched through the existing shared history arrays rather than a parallel GUI or registry. Generic hosts retain their original predicates and loader behavior.

## Validation and evidence

- Required offline Paradox wiki pages and the relevant vanilla documentation pages were read before editing, including event, focus, trigger/effect, event-target, and `load_focus_tree` behavior.
- Read-only `hoi4.event_inspect` trace was run for `chaosx.nr12.1200`; it returned `EVENT_INSPECTED_PARTIAL` with a linked artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35f8fde8d214506dfdadf76239b2089bf5d3b021bd3500f71f58e838895e0ba5/9afb3865ebe655613a1b4a8308a43de3d0b95a1dcdfb30c403f42e21998f6034/event-trace-8698fd27aef8.json`. The report has 14 blocking diagnostics in the broad repository trace; no RSA-specific unsupported field was returned.
- Read-only `hoi4.focus_inspect` was run for `common/national_focus/012_africa_continental_focus_tree.txt` / `africa_continental_focus_tree`; it returned `FOCUS_INSPECTED` with linked artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a6c3a16a7cc9fde34a9c3be93f12558ef7fa59c9ed097397db95c5109a08f68/72efa9ef995be2c0863b88be3c8a824165b66df542a91da93d85a126e85fe3ae/focus-inspect.8301baab82208485.json`. The source already reports 570 blocking layout diagnostics; this slice does not alter its layout.
- Targeted source checks confirmed one `africa_rsa_start_allied_civil_war` definition and one `.1` call site, all RSA log payload constants have title/detail mappings, the RSA localisation file retains its BOM, and the loader's SAF exclusion is present in both replacement branches.
- No in-game launch or live-save validation was performed, per repository instructions.

## Known limitations and follow-up

- Shared weighted selection can still choose a prospective RSA candidate before its frozen roster is available; post-freeze validation rejects the route if no bounded patron is present, without introducing a fallback host or world scan.
- The MCP event trace is broad and partial because the repository-wide artifact is large; the linked artifact and diagnostics are retained as unsupported-analysis evidence.
- Parent-owned workbook/spec promotion and final live-consumer/event-log visual acceptance remain open.
- No alternate South African host, fallback civil war, new country tag, or periodic world iteration was added.

