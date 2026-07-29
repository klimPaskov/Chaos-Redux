# Chaos Warfare package decision and mission audit

Status: passed for the bounded package decision and mission surface; no patch required

## Audit scope

The mapped `chaosx_decision_mission_auditor` reviewed exact target retention, costs, cancellation, cleanup, AI eligibility, player-facing requirements, unsupported-route handling, and the prohibition on broad all-country periodic maintenance.

This is a specialist audit result, not a completion claim for the overall package.

## Findings

- Selected-state Chemical air raids use the native raid state target. `common/raids/cbrn_chemical_air_raids.txt` preserves `var:target_state`, while `cbrn_chemical_air_raid_target_from_is_valid` in `common/scripted_triggers/cbrn_chemical_raid_triggers.txt` revalidates the state and its current controller.
- The bounded Japanese biological campaign decisions preserve `FROM` as the selected state and revalidate that state before `japan_bio_campaign_begin_release` debits or dispatches anything.
- Biological doomsday release remains a decision under `chaosx_cbw_doom_category`; it collects exact target states and resolves one batch consequence through `bio_doomsday_resolve_release`.
- Ground Chemical operations, nerve suppression, and the unsupported Japanese chemical adapter reject commitment while their verified current-version condition hooks are false. No cost, payload, or consequence record is created on those rejected paths.
- `common/scripted_effects/chemical_air_bomb_effects.txt` contains no ordinary continuous-air release or estimator path. Idle or merely assigned Chemical-capable aircraft cannot contaminate a region.
- Biological sabotage decisions reserve and release resources through one selected-state record, cancel when the retained record becomes invalid, and clear actor and state operation data on cancellation or resolution.
- Biological countermeasure reservations revalidate their target and release reserved capacity when completion becomes invalid.
- Reviewed CBRN decisions expose route, stock, policy, target, or consequence checks to both player requirements and AI scoring. No AI-only authorization bypass was found.
- No CBRN `on_daily`, `on_weekly`, or `on_monthly` all-country maintenance pulse was found.

## Disposition

No concrete defect or exploit finding was returned, and the auditor made no file edit.

The fail-closed ground Chemical and nerve-suppression routes remain engine-bound scenario blockers. Their rejection is correct no-fallback behavior and is not converted into a decision-audit failure.
