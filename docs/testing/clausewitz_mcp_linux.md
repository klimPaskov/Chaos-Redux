# Clausewitz-MCP for the isolated Linux game

The pinned server is installed and project configuration is present but disabled.
**Live gameplay verification is incomplete:** the reviewed upstream offsets target HOI4 1.19.2, while the installed Linux executable is a different build.
The adapter deliberately refuses memory reads, native calls, and event execution on that binary.
Do not remove this check, substitute the installed build ID for the expected one, change the shared game without explicit authorization and its exclusive lease, or interpret upstream `doctor` reporting `ready` as build compatibility.

## In-place downgrade availability check (2026-10-11)

The user authorized replacing the existing `/home/klim/games/hoi4` installation with 1.19.2, superseding the earlier side-by-side request.
**The downgrade is incomplete because Steam does not expose the requested branch to the cached account.**
The metadata-only command below logged in successfully without a password or Steam Guard prompt and exited successfully:

```bash
/usr/games/steamcmd +@sSteamCmdForcePlatformType linux +login klimpaskov +app_info_update 1 +app_info_print 394360 +quit
```

Standard input was closed, and a monitor would terminate only this SteamCMD process group if an authentication prompt appeared.
The complete response is `C:/Users/klimp/Videos/chaos_redux_trailer/records/cx/clausewitz_1192_appinfo.txt`; its `depots.branches` section begins at line 10002.
Neither `1.19.2` nor `1.19.2.0` appears among the 32 advertised branches or their depot manifests.
Steam indicates private branches exist, but this response does not expose an accessible 1.19.2 branch; no password, hidden branch, historical depot, or replacement offset was guessed.

| Available branch | Steam build ID |
| --- | --- |
| public | 25205862 |
| open_beta | 25826175 |
| 1.19.1.0 | 23764500 |
| 1.18.3.0 | 23541986 |
| 1.17.5.2 | 22500574 |
| 1.17.3.0 | 21119377 |
| 1.16.10 | 20110105 |
| 1.16.9 | 18823923 |
| 1.16.8 | 18550822 |
| 1.16.7 | 18518426 |
| 1.16.6 | 18460246 |
| 1.16.5 | 18239579 |
| 1.16.4 | 17895991 |
| 1.16.3 | 17868586 |
| 1.16.2 | 17781108 |
| 1.16.1 | 17692163 |
| 1.16.0 | 17590860 |
| 1.15.4 | 17075581 |
| 1.15.3 | 16721020 |
| 1.14.10 | 16033080 |
| 1.14.5 | 14111852 |
| 1.14.3 | 13788539 |
| 1.13.7 | 13209680 |
| 1.12.14 | 12405907 |
| 1.11.13 | 9324400 |
| 1.10.8 | 7337794 |
| 1.10.5 | 6513881 |
| 1.9.x | 5841295 |
| 1.8.2 | 4649066 |
| 1.7.1 | 3948182 |
| 1.6.2 | 3698640 |
| 1.5.4 | 2895913 |

These are Steam build IDs, not verified ELF IDs for uninstalled branches.
`readelf -n /home/klim/games/hoi4/hoi4` still returns `a4971c9e8ac9a6f2487dea109e01f9839ee59db7`, which differs from the required `2a79e51358b8b71c09cfb5ddefa0c03649067a4b`.
The descriptor declares `supported_version="1.19.*"`, and the user confirms 1.19.2 compatibility, but no 1.19.2 smoke test or fresh launch-log review was possible.
No game state, custom variable, Chaos Meter, event, screenshot, clip, detach, or register/thread recovery test was performed during this attempt.
The existing launcher already routes both plain `start` and opt-in `clausewitz-start` to the single installation, and the adapter already gates that path; both remain unchanged and project MCP entries remain disabled.

The board was notified before any proposed game change.
The observed lease remained `astra_live_cr`, with Linux HOI4 PID 35812; this job never acquired or released another job's lock and never signalled its game.
No `app_update` ran, no side-by-side directory was created, and Linux profile settings, mod symlinks, Windows HOI4, and Windows Steam were untouched.
No profile backup was needed because execution stopped before the mutation stage.
Game-download disk use was zero; the retained Steam response is 188,037 bytes, excluding Steam's own metadata/log cache changes.
C: had 56.652 GiB free before the metadata request and 30.579 GiB at the post-query check; concurrent shared-disk activity means that difference is not attributable to this metadata-only task.
The existing app manifest reports 6,816,192,348 bytes installed.

To resume, an accessible Steam branch delivering the required ELF must first be available.
Then coordinate the board, wait for a free lease and no `hoi4` process, acquire the lease exclusively, back up the Linux settings and mod symlinks without following them, and recheck disk headroom before an in-place `app_update 394360 -beta <verified-branch> validate`.
Preserve the selected beta in the Steam app manifest and explicitly include the same `-beta` on future SteamCMD maintenance commands; do not claim a pin before checking the saved branch.
Retain at least 15 GiB free and verify the executable's ELF ID before any attach-mode launch.

No return to 1.19.3 is necessary: it is still installed.
For a future rollback after a successful downgrade, use the same exclusive-lease, no-running-game, backup, disk, and cached-login checks with:

```bash
/usr/games/steamcmd +@sSteamCmdForcePlatformType linux +force_install_dir /home/klim/games/hoi4 +login klimpaskov +app_update 394360 -beta public validate +quit
```

This selects the current public release, which was Steam build 25205862 at this check; it does not guarantee 1.19.3 after the public branch changes.
Re-query branch metadata and verify the installed build before calling that a 1.19.3 rollback.
There were no substitutions or gameplay simplifications; installation, branch pinning, and all requested live verification remain unperformed because the requested branch is unavailable.

## Installation and ownership

| Item | Location or version |
| --- | --- |
| Distro and user | WSL `Ubuntu-24.04`, `klim` |
| Reviewed upstream | `https://github.com/smerss/Clausewitz-MCP` at `97c85437081904d5ad07bae1623ec58d1c0a5b9e` |
| Checkout | `/home/klim/tools/Clausewitz-MCP`, detached HEAD, tracked upstream files unchanged |
| Runtime | `.venv/bin/python`, Python 3.12.3, NumPy 2.2.6 |
| Dependency lock | [clausewitz_linux.requirements.txt](../../.tools/live_testing/clausewitz_linux.requirements.txt), copied to `requirements-chaosx.lock` in the checkout |
| Adapter source | [clausewitz_linux.py](../../.tools/live_testing/clausewitz_linux.py), installed as `chaosx_bridge.py` in the checkout |
| Linux game | `/home/klim/games/hoi4/hoi4` |
| Required ELF build | `2a79e51358b8b71c09cfb5ddefa0c03649067a4b` (upstream 1.19.2) |
| Installed ELF build | `a4971c9e8ac9a6f2487dea109e01f9839ee59db7` (setup notes: 1.19.3, Steam build 25205862) |
| Private display | `:91`; no Windows desktop capture or input |
| Launcher | `C:/Users/klimp/Videos/chaos_redux_trailer/records/cx/wsl_hoi4_launcher.sh` |
| Coordination | `records/cx/video_capture_board.md` in that same trailer directory |
| Exclusive lease | `/tmp/hoi4_wsl.lock`, contents `clausewitz_linux` for this route |

Only the official PyPI NumPy wheel was downloaded, with hash `fd83c01228a688733f1ded5201c678f0c53ecc1006ffbc404db9f7a899ac6249` enforced by pip.
No compiler, injected library, source dependency build, global package, service, network listener, or global MCP entry was installed.
The private virtual environment occupies about 85 MiB; the complete upstream checkout before installation occupied 4.5 MiB.
Pip caching and version checks were disabled, and the wheel provenance is retained in `numpy-wheel-provenance.json` inside the WSL checkout.
No Windows HOI4, Steam installation, Windows settings, or game binary was modified.

The security review is `C:/Users/klimp/Videos/chaos_redux_trailer/records/cx/clausewitz_mcp_review.md`.
It found no malicious, obfuscated, or phone-home behavior in the security-focused static review.
The runtime uses `process_vm_readv`, `process_vm_writev`, and ptrace register redirection; some apparent read tools call native getters and therefore inject calls.
It is version-sensitive and can crash or hang a game when offsets or calling conventions are wrong.
The adapter supplies build/PID/lease checks, Linux documentation paths, private-window-only screenshots, and a correction for upstream's duplicate broken memory-write wrapper without changing upstream tracked files.

## Project configuration

Codex's `.codex/config.toml` contains `[mcp_servers.clausewitz_linux]` with `enabled = false`.
Claude Code's `.mcp.json` contains the same server command; `.claude/settings.json` lists `clausewitz_linux` in `disabledMcpjsonServers` because `.mcp.json` has no corresponding portable `enabled` field.
These are project-local controls; no global configuration was changed.
The supported settings are documented in [Codex MCP configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) and [Claude Code project-server approvals](https://code.claude.com/docs/en/mcp#project-server-approvals-and-workspace-trust).

The exact stdio command is:

```powershell
wsl.exe -d Ubuntu-24.04 -u klim --exec /home/klim/tools/Clausewitz-MCP/.venv/bin/python -B /home/klim/tools/Clausewitz-MCP/chaosx_bridge.py --job clausewitz_linux serve
```

An authorized testing session may set Codex's entry to `enabled = true`, or remove just this server's name from Claude's project rejection list, then reconnect its MCP client.
Keep it disabled after the test session.
Client enablement does not bypass the adapter's independent build and lease checks.
The adapter's `clausewitz_linux_preflight` tool can report installation, compatibility, and lease metadata without attaching to a game.
Use this server's qualified tool names: it overlaps `hoi4-live` on names such as `hoi4_status` and `hoi4_screenshot`.

## Launch and lease workflow

Live work requires explicit user authorization, as with `chaos-redux-debug-playtest`.
Read the capture board before acting and append the job's intended work and result.
The integration session observed another owner, `astra_live_cr`, and never acquired, removed, or impersonated its lease.
The observed running Linux process was PID 35812; it was not attached to or controlled.

Read-only preflight from Windows:

```powershell
wsl.exe -d Ubuntu-24.04 -u klim --exec /home/klim/tools/Clausewitz-MCP/.venv/bin/python -B /home/klim/tools/Clausewitz-MCP/chaosx_bridge.py preflight
```

After a reviewed compatible upstream/build pair is available, acquire the lease exclusively inside WSL before launch:

```bash
python3 - <<'PY'
import os
fd = os.open('/tmp/hoi4_wsl.lock', os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
with os.fdopen(fd, 'w') as lease:
    lease.write('clausewitz_linux\n')
PY
export HOI4_WSL_JOB=clausewitz_linux
export HOI4_RENDERER=llvmpipe
bash /mnt/c/Users/klimp/Videos/chaos_redux_trailer/records/cx/wsl_hoi4_launcher.sh clausewitz-start 1920 1080
```

An existing lease is a stop condition; wait for its owner to finish rather than overwriting it.
Plain `start` remains the default game launch and does not change process tracing permissions.
`clausewitz-start` checks compatibility before starting helpers or editing Linux profile settings, then execs the normal launcher with opt-in integration.
For the existing cache/mount-namespace launch procedure, pass `HOI4_WSL_JOB=clausewitz_linux HOI4_CLAUSEWITZ=1` into `cached-start` along with its existing environment.
The launcher forwards those values when dropping to `klim`; refresh the runtime mod cache using the existing `wsl_hoi4_setup.md` instructions when testing edited content.
The attached mode uses `PR_SET_PTRACER_ANY` only on the game process before exec, allowing same-user tracing subject to ordinary Linux permission checks.
It does not use `LD_PRELOAD`, run the MCP as root, or change `kernel.yama.ptrace_scope`, which was observed as `1` before and after installation.
This per-process permission ends with the process; use a plain restart to remove it from a surviving integration session.

Stop only the game owned by this lease and release only the matching lease:

```bash
HOI4_WSL_JOB=clausewitz_linux bash /mnt/c/Users/klimp/Videos/chaos_redux_trailer/records/cx/wsl_hoi4_launcher.sh stop && python3 - <<'PY'
from pathlib import Path
p = Path('/tmp/hoi4_wsl.lock')
if p.is_file() and p.read_text().strip() == 'clausewitz_linux':
    p.unlink()
PY
```

If the stop command fails, keep the lease until the recorded process is safely stopped.
Never run that cleanup on another job's session.

## Verification and limits

| Capability | Result on this installation |
| --- | --- |
| Upstream installation doctor | Finds the Linux install and running Linux process; reports `ready`, but does not check ELF compatibility |
| MCP initialization and tools/list | Passed: 107 upstream tools plus `clausewitz_linux_preflight` |
| Adapter preflight | Reports the exact incompatible ELF builds, private display, current lease, and unchanged ptrace scope |
| Game-state read (`hoi4_status`) | Refused before memory access because the build is incompatible |
| Script-variable read (`hoi4_script_variable`) | Not exercised in game; uses native function calls and is build-gated |
| Chaos Redux event (`hoi4_debug_console`) | Not fired; native console dispatch is build-gated |
| Chaos Meter | Not read or visually verified in this session |
| Screenshot (`hoi4_screenshot`) | Lease refusal verified; actual capture not attempted against the other job's game |
| Guard regression tests | Eight passed, including incompatible-build launch refusal and no desktop-capture fallback |
| Windows stdio bridge | Exact `.mcp.json` command tested separately; evidence in `records/cx/clausewitz_mcp_windows_stdio.json` |

The game was already running under another job's lease, and a compatible build is independently missing.
No launch, campaign control, game-memory read/write, ptrace attachment, event firing, or screenshot of that session was performed.
There is no claim of live Chaos Redux acceptance.
The requested real-game verification remains blocked until version-compatible offsets/calling conventions have been reviewed and an exclusive test slot is available.
Do not merely relabel the old offsets or regenerate a few tables: addresses are embedded across multiple modules, and upstream save tokens and map caches also carry version/vanilla assumptions.

When those prerequisites are met, use a dedicated paused non-Ironman Chaos Redux test game and record the active mod/cache revision.
List tools and retain their live schemas, call `hoi4_status` and `hoi4_session_info`, and compare country/date values with a private-window screenshot.
Read one known native dynamic variable using `hoi4_script_variable` and compare it with visible or save-backed state before treating that resolver as supporting custom/global mod variables.
Choose the event from its actual source and invoke `hoi4_debug_console` with `event <verified-event-id> <country-tag>` once; verify its effects and event history rather than treating a successful dispatch as proof of gameplay.
Read the Chaos Meter's actual scoped variable from source, obtain a value using a supported resolver or a dedicated save, and compare the meter before and after the event.
The upstream resolver's custom/global-variable support is unverified; do not assume it behaves like `hoi4_eval_effect` or the dedicated save inspector.
Use `chaos-redux-save-inspection` when a save is needed, and distinguish save snapshots from live memory.
Capture the event and meter through `hoi4_screenshot`, which this adapter restricts to the recorded game PID on `:91` and never falls back to WSLg or the Windows desktop.
The game launch, menu navigation, popup handling, and save/load workflow are not supplied by this MCP as equivalents of the HOI4 Live Tools workflow.
Continuous micro/order loops and arbitrary native function calls have not been accepted for this installation.

## Difference from HOI4 Live Tools

| Surface | Clausewitz-MCP Linux | HOI4 Live Tools |
| --- | --- | --- |
| Target | Native Linux process in WSL | Installed Windows game route in this project |
| State | Direct memory reads; some native getter calls | Project's supported telemetry, UI, console, and save tools |
| Actions | ptrace/native command queue or native console dispatcher | Supported live-testing tools with launch, input, time, popups, and saves |
| Compatibility | Exact executable layout and embedded offsets | Its own documented capabilities; Clausewitz tests do not validate it |
| Lock | `/tmp/hoi4_wsl.lock` and capture board | `hoi4_lock` |
| Screenshot | Private X11 game window only via this adapter | `hoi4_screenshot` through that server's capture route |
| Current acceptance | Transport verified; live use blocked | Remains the default skill route for authorized Windows testing |

Do not call the Windows server as a fallback for this Linux-only task.

## Maintenance and uninstall

The adapter is a maintained entry point called by both project MCP entries and the opt-in launcher.
After a reviewed adapter edit, copy `.tools/live_testing/clausewitz_linux.py` to `/home/klim/tools/Clausewitz-MCP/chaosx_bridge.py` and run `.tools/live_testing/test_clausewitz_linux.py` with the WSL Python interpreter.
The source checkout must remain at the reviewed commit with no tracked modifications.
Any upstream upgrade requires a fresh review, dependency lock, and compatibility evidence.

Backups taken before edits are in `C:/Users/klimp/Videos/chaos_redux_trailer/records/cx/clausewitz_mcp_backups/`: `launcher.sh`, `codex_config.toml`, `mcp.json`, `claude_settings.json`, and `debug_playtest_SKILL.md`.
For exact removal without overwriting later unrelated work:

1. Disable/disconnect `clausewitz_linux` in both clients; stop an integration-owned game and release its lease using the commands above only if that lease is yours.
2. Remove just `[mcp_servers.clausewitz_linux]` from `.codex/config.toml`, just `mcpServers.clausewitz_linux` from `.mcp.json`, and just its name from `.claude/settings.json`'s `disabledMcpjsonServers` list.
3. Restore `wsl_hoi4_launcher.sh` from `clausewitz_mcp_backups/launcher.sh` if no later edits exist; otherwise remove only the `clausewitz-start` case, `HOI4_CLAUSEWITZ` handling, bridge launch branch, and added forwarding using that backup as the comparison.
   Preserve unrelated later launcher changes and the job-aware lease support if another workflow uses it.
4. Delete the exact installation directory inside WSL after confirming it is the owned clone:

   ```bash
   target=/home/klim/tools/Clausewitz-MCP
   test "$(realpath -- "$target")" = /home/klim/tools/Clausewitz-MCP || exit 1
   test "$(git -C "$target" remote get-url origin)" = https://github.com/smerss/Clausewitz-MCP.git || exit 1
   rm -rf -- "$target"
   ```

5. If removing project support entirely, remove only `.tools/live_testing/clausewitz_linux.py`, `.tools/live_testing/clausewitz_linux.requirements.txt`, `.tools/live_testing/test_clausewitz_linux.py`, and the short Linux routing paragraph from the canonical debug-playtest skill, then run `python .tools/sync/sync_agents.py`.
   Retain this guide and the external review/verification records as historical evidence if desired.

No game-file restore, Windows Steam repair, environment-variable cleanup, global MCP removal, or ptrace sysctl rollback is needed.
No dependency build cache was created; no files outside this installation's own artifacts were deleted.

Skills used: `openai-docs`, `chaos-redux-shared-git-commit`, `chaos-redux-debug-playtest`, and `skill-creator` for the narrow routing edit.
No gameplay or asset changes were made.
There is no substituted gameplay implementation; the missing live tests are explicitly incomplete.
