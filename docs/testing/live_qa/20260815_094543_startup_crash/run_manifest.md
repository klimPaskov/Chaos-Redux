# Chaos Redux Startup Crash Debug Run

## Run configuration

- Run ID: `20260815_094543_startup_crash`
- Mode: `issue-reproduction`
- Scope: startup crash and fresh debug-launch errors only; no campaign or gameplay session
- Launch target: `C:\Users\klimp\OneDrive\Desktop\hoi4.exe - Shortcut.lnk`
- Candidate log directory: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\logs`
- Artifact root: `docs/testing/live_qa/20260815_094543_startup_crash`
- Repair-cycle budget: 6
- Completed launches: 8 total, consisting of one baseline reproduction, six repair relaunches, and one verification-only relaunch after a concurrent workspace edit
- Repository branch: `master`
- Baseline commit: `a6fe6dd967c66c4e8cd890986257b9da5d0c4cc9`

## Worktree baseline

The run began with 1,121 pre-existing user-owned status entries: 872 tracked changes, 249 untracked entries, and 457 deletions. These changes are preserved. Repairs will be limited to paths directly identified by fresh launch evidence.

## Pre-launch log baseline

| Log | Bytes | Last write UTC | SHA-256 |
| --- | ---: | --- | --- |
| `error.log` | 62,495 | 2026-08-15T06:41:52.1522737Z | `F2FAD8AEDE6C404EC9C0F205EE60A59C8D952872BCB46FE32559E3B52452C4D9` |
| `game.log` | 64 | 2026-08-15T06:40:44.1169980Z | `7C774553DF4D4A55771228E46593F4168830C2892CDF2DBC2E683613E052B734` |
| `setup.log` | 159,361 | 2026-08-15T06:41:52.1532773Z | `EC5AA24615EDC42CE510D2C5B4C8B4E730AF6C9341AC6E41973AF99953651947` |
| `text.log` | 0 | 2026-08-15T06:40:32.2002806Z | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |

`exceptions.log` was absent. The pre-launch copies are under `logs/prelaunch/`.

## Capability gate

- Repository edit access: available
- Shortcut access: available
- Active HOI4 process at baseline: none
- Windows desktop control: explicitly excluded by the user and not used for the completed run
- Screenshot capture: not used because it would require desktop control
- Log read access: available

## Test boundaries

No country was selected and no campaign was started. The acceptance target was deterministic startup completion through province loading, game reset, and both 1936 history passes with no fresh crash directory and an empty `error.log`.

## Final clean-start evidence

- Final process: PID `17256`, launched at 2026-08-15 11:25:24 local time through the supplied shortcut
- Province initialization: `Loaded 13414 provinces`
- Game initialization: `Resetting game`
- History initialization: two `Executing History` passes completed at 1936.01.01.12
- Final `error.log`: 0 lines, 0 bytes
- Latest crash directory after the clean run: `hoi4_20260815_105920`, timestamped before the final launch
- Source-stability check: no startup-loaded file changed between the final launch and acceptance check
- Shutdown: `CloseMainWindow()` accepted and the process exited normally within 30 seconds
