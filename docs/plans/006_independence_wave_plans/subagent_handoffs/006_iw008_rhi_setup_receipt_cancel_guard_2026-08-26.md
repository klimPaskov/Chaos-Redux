# Event 006 IW-008 Rhineland setup-receipt lifecycle repair

Date: 2026-08-26

Status: implemented narrow decision and category lifecycle repair; Event 006 remains HOLD / PARTIAL.

## Scope

This handoff covers the admitted IW-008 Rhineland founding-mission and decision-category lifecycle only.

It does not change package admission, reservation capacity, routes, costs, AI weights, focuses, localisation keys, scripted GUI layout, assets, or super-event wiring.

## Issue list by severity

### High, fixed: setup-reset, capital-loss, mission, and category mismatch

`independence_wave_rhi_keep_rhine_arteries_open` activates only after `independence_wave_iw_008_setup_complete` is present, but its cancellation trigger previously ignored loss of that receipt.

`independence_wave_setup_iw_008_rhineland` clears the receipt before attempting setup and restores it only after `has_prepared_independence_wave_iw_008_package_setup = yes` succeeds.

The formerly active mission could therefore survive a failed or retried setup outside the generation that created it, and `independence_wave_rhi_corridor_category` could still expose its ordinary package rows because it was gated only on package identity.

The cancellation success branch also checked only stable Corridor Authority, so a capital or receipt-loss cancellation could resolve the mission when the authority value had already reached its threshold.

### High, queued but not changed: IW-009 Bavaria has the same source pattern

`independence_wave_bay_hold_the_state_together` activates on `independence_wave_iw_009_setup_complete` in `common\decisions\006_independence_wave_rhineland_bavaria_saar_decisions.txt`, while its cancellation trigger lacks that receipt.

`independence_wave_setup_iw_009_bavaria` clears the receipt before setup and restores it only after its prepared proof succeeds in `common\scripted_effects\006_independence_wave_rhineland_bavaria_saar_package_effects.txt`.

This tranche intentionally repairs IW-008 only, so IW-009 remains the next safe same-file follow-up after a fresh concurrent-worktree check.

## Changed files and identifiers

- `common\decisions\006_independence_wave_rhineland_bavaria_saar_decisions.txt`: added the setup-receipt cancellation guard and made the success branch of `independence_wave_rhi_keep_rhine_arteries_open` require the receipt and capital control as well as stable Corridor Authority.
- `common\decisions\categories\006_independence_wave_categories.txt`: made `independence_wave_rhi_corridor_category` visible only while the exact RHI package and its current setup receipt both exist.
- `docs\events\006_independence_wave\northern_western_europe_packages.md`: aligned the package lifecycle description.
- `docs\plans\006_independence_wave_plans\subagent_handoffs\006_iw008_rhi_setup_receipt_cancel_guard_2026-08-26.md`: this handoff.

## Before and after

Before the change, a rebuild cleared the setup receipt while an already active founding mission could remain active and the category could retain stale package actions, and a capital or receipt loss could resolve the mission if Corridor Authority was already stable.

After the change, only a stable Corridor Authority with the current receipt and controlled capital resolves the mission, while receipt or capital loss follows the existing failure effect and the category remains hidden until a successful setup reissues the receipt.

The pre-existing success path, capital-loss failure path, timeout failure path, shared project-failure helper, cleanup removal, and urgent mission AI weight are unchanged.

## Decision category lifecycle and cognitive-load notes

The category begins with one non-selectable founding mission plus four ordinary founding projects: bridge dispatch, factory and rail guard integration, former-host customs ledgers, and river-crossing security.

The government-settlement rows are hidden until one selected government-route trigger is true, so the source does not expose all route settlements simultaneously.

`independence_wave_rhi_corridor_authority` is displayed as a current value out of 100 with an explicit threshold of 65, and the mission localisation states the 420-day deadline and consequence of failure.

No dedicated decision-owned scripted GUI is bound to `independence_wave_rhi_corridor_category`, so no GUI layout or click surface was changed.

## Mission quality, costs, AI, and cleanup

The owner is IW-008 Rhineland in the Rhine Corridor category, with anchor state 51 and a 420-day founding-crisis duration.

The mission requires the exact active RHI package and current generation receipt, resolves only with stable Corridor Authority and capital control, and fails through the existing package failure path after receipt loss, capital loss, or timeout.

The mission is non-selectable and has no spendable cost itself.

The visible RHI project cost strings use at most four spendable types, with the inspected administration, security, diplomatic, and strategic strings using the matching command-power, manpower, equipment, transport, stability, and civilian-factory texticons rather than literal resource labels.

No AI score, target selection, route weight, MTTH, random pool, or balance constant changed, so no probability comparison or AI-weight audit was required for this patch.

`independence_wave_cleanup_iw_008_rhineland` already removes the mission and clears the setup receipt, and the category guard now prevents stale decision rows from remaining visible during the same lifecycle loss.

## Localisation and super-event notes

Existing localisation already explains the displayed Corridor Authority value, 65 threshold, deadline, and failure consequence, so no localisation key or tooltip change was necessary.

No super-event, event option, or dedicated scripted-GUI surface belongs to this founding mission, so no super-event or GUI wiring changed.

## Validation and MCP evidence

- Targeted static lifecycle assertion passed: activation receipt, mission cancellation receipt guard, resolved-branch receipt and capital guards, category receipt guard, setup clear, prepared-proof restore, and IW-008 central content attestation all matched.
- `python -B .tools\audit_event6_allocator.py` passed after the final patch and retained 32 attested packages, 29 compatible reservation groups, and the two-package `RG-RHINE-SAAR` capacity with IW-008 at anchor 51.
- `hoi4.event_inspect` traced setup event `chaosx.nr6.10` with `EVENT_INSPECTED_PARTIAL`, revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e5931721c7013aa64bcf6023148061be71d938a5870abce0ca6ff7516d539de/e6ae974941dd26851b7c930a8b01e01c9c9ee31a63861435a36678b58d580ab8/event-trace-744cd12bca3e.json`.

The event inspector does not project decision or mission lifecycle semantics, and no `hoi4.decision_inspect` or `hoi4.mission_inspect` endpoint is exposed, so the source assertion is not presented as engine-runtime evidence.

No live game session was run.

## Remaining follow-up

The exact IW-009 Bavaria receipt mismatch is the highest-priority bounded follow-up.

Other founding-mission families were not batch-edited in this tranche and should receive a fresh source scan before any wider repair, because concurrent work has already changed several earlier candidates.

No files were staged or committed.
