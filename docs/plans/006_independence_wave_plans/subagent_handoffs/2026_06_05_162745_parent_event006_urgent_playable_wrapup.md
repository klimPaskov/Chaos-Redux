# Parent Handoff: Event006 Urgent Playable Wrap-Up

## Scope

Urgent Event006 cleanup after the 2026-06-05 correction:

- keep Kuban (`KUB`) and Altai (`ALT`) out of the accepted Event006 playable surface
- make manual Independence Wave firing more likely to release valid package candidates without weakening host-survival guarantees
- keep Event006 evolution logs to the tier-scale release pattern, not package or per-release spam
- protect the shared event/evolution log UI from Event006 type collisions
- record the scripted GUI audit result

## Files changed by parent

- `common/script_constants/006_independence_wave_constants.txt`
  - moved unused Event006 dossier/package/formation evolution type constants out of the low shared range and into `8807`-`8887`
  - kept the only active Event006 evolution type as `88`
  - kept four authored release-scale stages:
    - `gathering_storm_stage = 1`
    - `rising_cascade_stage = 2`
    - `old_names_stage = 3`
    - `impossible_statehood_stage = 4`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
  - removed repeated host-weakness checks from package seed triggers so manual firing can seed valid package candidates from stable hosts
  - preserved the final `can_independence_wave_host_release_current_candidate_safely` gate, including host survival and invoker/weakness/peripheral checks
  - kept explicit `KUB`/`ALT` exclusions in `can_independence_wave_use_candidate_tag`
- `common/national_focus/006_independence_wave_focus.txt`
  - removed four superseded KUB/ALT package focus blocks:
    - `independence_wave_kuban_black_sea_records`
    - `independence_wave_kuban_petition_map`
    - `independence_wave_altai_oyrot_records`
    - `independence_wave_altai_petition_map`
- `docs/events/006_independence_wave.md`
  - updated the Event006 focus count to 121
- `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md`
  - updated the Event006 focus icon reference count to 121
  - removed the four superseded KUB/ALT focus rows from the ledger

## Subagent result reviewed

`chaosx_scripted_system_architect` completed a bounded scripted GUI audit and wrote:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_162210_event006_scripted_gui_technical_audit.md`

Result: Event006 scripted GUI is currently display-only by design. It has five decision-category panels, no `buttonType` blocks, no GUI click handlers, no GUI effects, and no Event005/KUB/ALT references. No GUI patch was applied.

## Validation

- Brace balance passed for:
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
  - `events/006_independence_wave.txt`
  - `common/national_focus/006_independence_wave_focus.txt`
- Unsupported comparison-operator scan passed for touched Event006 script/localisation surfaces.
- `common/national_focus/006_independence_wave_focus.txt` has 121 focus blocks after the KUB/ALT focus-surface cleanup.
- The four removed KUB/ALT focus IDs are absent from both the focus tree and the focus icon reuse ledger.
- Event006 keeps active tier evolution type `88`; inactive secondary package/dossier/formation type constants are isolated in `8807`-`8887` with no conflicts found in other `common/script_constants/*.txt` files.
- `git diff --check` passed for the touched tracked Event006 files.
- `tmp/hoi4-error-logs/` contained only the old `watchdog.log`; no current `error.log` was present during this pass.

## Remaining risks

- KUB/ALT helper triggers and effects still exist in inactive remnants, but `can_independence_wave_use_candidate_tag` excludes both tags and the shared focus tree no longer exposes their package surface.
- Package/dossier/formation log helper functions remain present as compatibility remnants, but their type IDs no longer collide with the shared low evolution-type range and the playable Event006 entry records only the tier-scale evolution log.
- No live in-game validation was run by the parent.
