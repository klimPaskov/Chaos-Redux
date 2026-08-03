# Event 006 overlay watch permanent-identity-loss cleanup

Date: 2026-08-03

Status: **Implemented and source-audited as a bounded lifecycle repair.**

## Policy

The IW-022 Dalmatia, IW-025 Vojvodina, and IW-035 Livonia overlays preserve temporary route interruptions, but an interrupted paid watch cannot remain alive forever after its carrier loses the exact researched dynamic identity. Each overlay now allows a centralized 30-day suspension grace window. The first inactive carrier hook pauses the existing mission and extends its timeout by one day; every later inactive hook repeats that extension and increments the suspension ledger. At the grace threshold the overlay removes the active mission, clears running/interrupted/suspended and shared overlay flags, removes overlay ideas, marks permanent identity loss, and clears the suspension counter.

The route-active trigger rejects a carrier marked with permanent identity loss, so a later cosmetic return cannot silently resurrect the old paid watch. A new vanilla dynamic carrier has a fresh country scope and may initialize its own route normally. Temporary loss shorter than the grace window continues through the existing suspend/resume path. Terminal cleanup also resets each package's hold-progress variable to its minimum, matching ordinary watch failure cleanup.

## Gameplay surfaces changed

- `common/script_constants/006_independence_wave_iw022_dalmatia_constants.txt`
- `common/script_constants/006_independence_wave_iw025_vojvodina_constants.txt`
- `common/script_constants/006_independence_wave_iw035_livonia_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw022_dalmatia_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw025_vojvodina_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw035_livonia_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw022_dalmatia_effects.txt`
- `common/scripted_effects/006_independence_wave_iw025_vojvodina_effects.txt`
- `common/scripted_effects/006_independence_wave_iw035_livonia_effects.txt`

Each package owns its cancellation effect and uses its own generation-local flag and variable names. No global iterator, country creation, tag mutation, resource reward, or unrelated carrier cleanup was added. The existing paid start, timeout, failure, and temporary resumption paths remain intact.

## Static checks

- Every package duration block defines `watch_suspension_grace_days = 30` beside the existing timeout and pause-extension constants.
- Every route-active trigger rejects only its own permanent-loss flag.
- Every start effect initializes a zero suspension counter; every resume effect resets it.
- Every pause effect calls `add_days_mission_timeout` with the existing one-day extension, increments the counter, and dispatches permanent cleanup at `greater_than_or_equals` the centralized grace constant.
- Permanent cleanup removes only the package's own watch mission and ideas, resets hold progress and suspension state, and clears the shared overlay-active flag that the package itself owns.

## Remaining boundary

The source re-audit is recorded in `006_overlay_watch_permanent_identity_loss_reaudit_2026_08_03.md` and found no P1/P2 defect. No live or save/load evidence is claimed; exact mission-timeout ordering remains a user-side runtime boundary. The obsolete pasted flag log is not used as evidence.
