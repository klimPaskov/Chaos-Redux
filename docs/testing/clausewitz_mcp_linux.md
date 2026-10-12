# Clausewitz-MCP for the isolated Linux game

Clausewitz-MCP is the preferred live route for the Linux HOI4 process; HOI4 Live Tools is a fallback only when it reaches that same WSL process.
The adapter selects a reviewed table by ELF GNU Build ID, refuses unknown builds before memory access, and requires the job's exclusive `/tmp/hoi4_wsl.lock` lease for live tools.
The 1.19.3 table is partial: tools outside its per-build allowlist are blocked and must remain unverified until their addresses and calling conventions are derived.

## Current 1.19.3 port status (2026-10-12)

The installed Linux game is ELF build `a4971c9e8ac9a6f2487dea109e01f9839ee59db7`, SHA-256 `56fc2945cdbf2475a316db3285eb3458ae5d577db149db6dfdba6f004de3a88a`; it was not downgraded or otherwise modified.
Upstream remains pinned at `97c85437081904d5ad07bae1623ec58d1c0a5b9e` and still has no 1.19.3 branch or issue.
The target-only evidence derives the console manager/dispatcher and allocator, the game-state country/tag map, the idler, and all 358 command addresses; 357 command sizes are resolved and one command field layout differs from 1.19.2.
The selector now recognizes 1.19.2 and 1.19.3 separately and continues to refuse every unknown ELF Build ID.
The per-tool status map contains 109 entries (107 upstream tools plus preflight and status): 6 are verified, 103 unverified, and none are marked broken. Verified tools are `clausewitz_linux_preflight`, `clausewitz_linux_tool_status`, `hoi4_status`, `hoi4_debug_read_memory`, `hoi4_debug_list_commands`, and `hoi4_screenshot`.
The `version` operation also returned successfully through `hoi4_debug_console`, but that tool remains unverified overall because its front-end `get_var` probe faulted before a campaign loaded.
The game was launched through WSL, but remained in the front-end/checksum-loading state with no active idler. State mapping, `version`, a long-argument allocator call, and screenshot capture worked, and all 72 attached threads' registers restored after the injected calls.
The front-end `get_var global.chaos_meter_value` probe faulted inside the command handler; the game stayed alive and the bridge now blocks console calls while no active campaign is loaded.
The required active-campaign Chaos Redux variable, Chaos Meter, and event checks remain incomplete because Clausewitz-MCP has no save-load/new-game tool and HOI4 Live Tools did not reach this private WSL process.
The plain-text comparison save `hoi4live_wsl_capture_day0.hoi4` is 1.19.3 USA at 1936.1.1.12 and records `variables/chaos_meter_value = 0`, but it was not loaded into the live process.
The launcher stopped the owned game, restored `settings.txt` and `pdx_settings.txt` byte-exactly, and released the WSL lease; the Linux executable and mod symlinks were unchanged.
Derivation scripts, target tables, call-recovery records, and screenshots are under `/home/klim/tools/Clausewitz-MCP-ports/1.19.3/`.

Clausewitz-MCP is preferred for the Linux process only when its exact ELF build has a reviewed table and this job holds the WSL lease.
HOI4 Live Tools is the fallback only when it reaches that same Linux process; a Windows session does not verify Linux gameplay.

## Initial 1.19.3 blocker snapshot (2026-10-11; historical)

Upstream has no 1.19.3 support: `origin/main` still points to `97c85437081904d5ad07bae1623ec58d1c0a5b9e`, the only advertised branch is `main`, and the public issues endpoint returned an empty list.
The installed Linux executable is ELF build `a4971c9e8ac9a6f2487dea109e01f9839ee59db7` with SHA-256 `56fc2945cdbf2475a316db3285eb3458ae5d577db149db6dfdba6f004de3a88a`.
The required 1.19.2 Linux ELF (build `2a79e51358b8b71c09cfb5ddefa0c03649067a4b`) was not present in the installed game or the inspected Clausewitz research dump locations, so its instruction signatures cannot be reproduced and searched in the 1.19.3 target.
[SteamDB's Linux depot history](https://steamdb.info/depot/394363/manifests/) lists a historical `open_beta` manifest `8705347054517643253` from 28 August 2026; the [1.19.2 beta update notes](https://steamdb.info/patchnotes/24468645/) identify that beta period, but neither source establishes that the manifest contains the required ELF.
Two isolated SteamCMD downloads of that manifest, including one after refreshing app metadata, failed with `Failed downloading 1 manifests (No connection)`; no file was obtained and the installed game was not changed.
The upstream research process was reviewed in `research/README.md`, `research/FINDINGS.md`, `research/dis.sh`, `research/funcs.py`, `research/leascan.py`, `research/callscan.py`, `research/cmdscan.py`, `research/cmdfields.py`, `research/diploscan.py`, `calling/rtti.py`, `calling/fieldmap.py`, `calling/offsets.py`, and `calling/api.py`.
No 1.19.3 offsets, function addresses, command constructors, vtables, or calling conventions were generated; the existing 1.19.2 build gate remains unchanged and refuses the installed ELF before memory access.
Evidence and the exact inspected paths are recorded in `/home/klim/tools/Clausewitz-MCP-ports/1.19.3/PORT_STATUS.md` and appended to `records/cx/clausewitz_mcp_review.md`.

| Surface | 1.19.3 result |
| --- | --- |
| Upstream branch/issue review | No 1.19.3 branch or issue found; latest remote main is the pinned commit |
| Build identification | Verified by `readelf -n` and SHA-256 of the installed ELF |
| Stdio initialization and tool discovery | Previously verified: 107 upstream tools plus the adapter preflight; this does not validate native calls |
| Build preflight and refusal | Verified: the adapter reports the mismatched build and refuses before memory access |
| `hoi4_status` native state read | Unverified as a working read; the prior mismatched-build call was refused before memory access |
| Script-variable reads and event dispatch | Unverified; no native call was made |
| Console dispatch | Unverified; no native call was made |
| Screenshot capture | Unverified against the game; the prior call was refused because another job owned the lease |
| Order construction/posting | Unverified; no command was posted |
| Ptrace attach, thread recovery, and register restoration | Unverified; no attach was attempted |

Clausewitz-MCP is the preferred live interface on Linux only after the exact ELF build has a reviewed table and the job owns the matching WSL lease.
HOI4 Live Tools is the fallback when it is connected to the intended game; results from another OS installation do not validate the Linux process.
For the current 1.19.3 ELF, Clausewitz remains blocked and no state reads or captures should be attributed to it.

## In-place downgrade availability check (2026-10-11; superseded)

This historical branch and downgrade plan is withdrawn by the current direction: keep the single Linux install at 1.19.3 and do not download the 1.19.2 depot or downgrade the game.

Historical direction: a prior user instruction temporarily authorized replacing the existing `/home/klim/games/hoi4` installation with 1.19.2.
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

This section is retained as a historical branch-availability record only. Its earlier in-place update and rollback proposals are withdrawn and must not be executed.

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

Codex's `.codex/config.toml` enables `[mcp_servers.clausewitz_linux]`; Claude Code's `.mcp.json` registers the same WSL stdio command and `.claude/settings.json` no longer disables it.
These are project-local controls; no global configuration was changed.
The supported settings are documented in [Codex MCP configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) and [Claude Code project-server approvals](https://code.claude.com/docs/en/mcp#project-server-approvals-and-workspace-trust).

The exact stdio command is:

```powershell
wsl.exe -d Ubuntu-24.04 -u klim --exec /home/klim/tools/Clausewitz-MCP/.venv/bin/python -B /home/klim/tools/Clausewitz-MCP/chaosx_bridge.py --job clausewitz_linux serve
```

Client enablement does not bypass the adapter's independent Build-ID and lease checks.
`clausewitz_linux_preflight` reports the selected table profile without attaching, while `clausewitz_linux_tool_status` returns the status of every upstream tool on the selected build.
The 1.19.3 adapter blocks tools that are not in its explicitly eligible set; future calls should check `clausewitz_linux_tool_status` and use only tools marked `verified`.
Use this server's qualified tool names: it overlaps `hoi4-live` on names such as `hoi4_status` and `hoi4_screenshot`.

## Launch and lease workflow

Live work requires explicit user authorization, as with `chaos-redux-debug-playtest`.
Read the capture board before acting and append the job's intended work and result.
Acquire the WSL lease only when it is free, and never overwrite or release another job's lease.

Read-only preflight from Windows:

```powershell
wsl.exe -d Ubuntu-24.04 -u klim --exec /home/klim/tools/Clausewitz-MCP/.venv/bin/python -B /home/klim/tools/Clausewitz-MCP/chaosx_bridge.py preflight
```

For the 1.19.3 profile, acquire the lease exclusively inside WSL before launch:

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
`clausewitz-start` checks the installed Build ID against the selected table before starting helpers or editing Linux profile settings, then execs the normal launcher with opt-in integration.
For the existing cache/mount-namespace launch procedure, pass `HOI4_WSL_JOB=clausewitz_linux HOI4_CLAUSEWITZ=1` into `cached-start` along with its existing environment.
The launcher forwards those values when dropping to `klim`; refresh the runtime mod cache using the existing `wsl_hoi4_setup.md` instructions when testing edited content.
The attached mode uses `PR_SET_PTRACER_ANY` only on the game process before exec, allowing same-user tracing subject to ordinary Linux permission checks.
It does not use `LD_PRELOAD`, run the MCP as root, or change `kernel.yama.ptrace_scope`, which was observed as `1` before and after installation.
This per-process permission ends with the process; use a plain restart to remove it from a surviving integration session.
The upstream Clausewitz MCP has no save-load or new-game UI tool. If it starts at the front end, console commands are blocked until the target idler indicates an active campaign; an available save must be loaded through a supported route that reaches this same Linux process before testing events or script variables.

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
| Upstream branch/issue review | Verified: latest upstream remains `97c85437081904d5ad07bae1623ec58d1c0a5b9e`; only `main`, no public issues or 1.19.3 table found |
| Build-ID selection and unknown-build refusal | Verified: 1.19.3 ELF `a4971c9e8ac9a6f2487dea109e01f9839ee59db7` selects the separate partial table; unknown IDs are refused before memory access or injection |
| MCP initialization and tool discovery | Verified over stdio: 109 tools (107 upstream plus preflight and per-tool status) |
| Per-tool status inventory | Verified: `clausewitz_linux_tool_status` reports every upstream tool; only the tool scopes listed below are marked verified |
| State-root read | Verified for startup state: 618 countries, player tag index 0, country index 0, and a valid `CCountry*`; `G_IDLER` was null, so this was not an active campaign |
| Raw memory reads | Verified: live reads of the game-state, console-manager, and idler pointer slots succeeded |
| Console command catalog | Verified: the live registry listed `version` and `get_var`; it had no save-load or new-game console command |
| Console dispatcher (`hoi4_debug_console`) | Unverified overall: `version` returned `Operation Postern v1.19.3.0.c01a`, but `get_var global.chaos_meter_value` faulted inside the handler before a campaign was loaded; the game survived and all injected-call registers were restored |
| Operator allocation and ptrace recovery | Verified: the target `operator new` returned; the console call and allocator call each restored registers for all 72 attached threads, and detach resumed them |
| Private-window screenshot | Verified: screenshots were captured from the owned game window on `:91`; loading-screen evidence is under `/home/klim/tools/Clausewitz-MCP-ports/1.19.3/evidence/` |
| Script-variable tool (`hoi4_script_variable`) | Unverified and blocked: the target dynamic-variable resolver address is not derived |
| Chaos Meter in an active campaign and event firing | Unverified: no active test campaign was loaded, no event was fired, and no live meter value was read |
| Candidate save | Read-only inspection found a compatible text save, USA, 1936.1.1.12, with saved `chaos_meter_value = 0`; it was not loaded into the game |
| Cleanup | Verified: the owned game was stopped, `settings.txt` and `pdx_settings.txt` were restored byte-exactly, and `/tmp/hoi4_wsl.lock` was released |

The successful state, catalog, memory, screenshot, and version calls establish only the listed 1.19.3 tool scopes; every other upstream tool remains unverified and is blocked by the target allowlist.
The `get_var` error occurred while the game had no active idler; the bridge now blocks console calls until an active campaign is loaded.
The active-campaign variable, Chaos Meter, and event checks remain incomplete because Clausewitz-MCP has no save-load/new-game UI tool, and HOI4 Live Tools does not reach this private WSL process.
Do not use a Windows game result as evidence for Linux, and do not use arbitrary native function calls or order loops until their target entries are derived and reviewed.

## Difference from HOI4 Live Tools

| Surface | Clausewitz-MCP Linux | HOI4 Live Tools |
| --- | --- | --- |
| Target | Native Linux process in WSL | Installed Windows game route in this project |
| State | Direct memory reads; some native getter calls | Project's supported telemetry, UI, console, and save tools |
| Actions | ptrace/native command queue or native console dispatcher | Supported live-testing tools with launch, input, time, popups, and saves |
| Compatibility | Exact executable layout and embedded offsets | Its own documented capabilities; Clausewitz tests do not validate it |
| Lock | `/tmp/hoi4_wsl.lock` and capture board | `hoi4_lock` |
| Screenshot | Private X11 game window only via this adapter | `hoi4_screenshot` through that server's capture route |
| Current acceptance | Partial 1.19.3 core state reads, command catalog, screenshot, and console `version`; active-campaign event/meter checks incomplete | Fallback only when it reaches the same Linux process; the configured Windows route does not reach private display `:91` |

Use HOI4 Live Tools as fallback only if it controls the intended game process; a Windows game result does not validate the Linux game.

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
