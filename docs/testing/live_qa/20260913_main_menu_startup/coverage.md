# Startup coverage

Acceptance basis: the user explicitly requested autonomous debug launches, repair of the crash and every error emitted while loading the main menu, and repeated relaunches until none remain.
The user explicitly excluded computer control and subsequently prohibited Astra subagents.
This run uses process launch/termination, fresh filesystem logs, and passive captures of the HOI4 window only.
It sends no mouse input, keyboard input, console commands, or desktop controls.

The accepted boundary is a fresh load through the responsive Chaos Redux main menu and the completion of startup database validation.
An empty fresh `error.log`, stable after the menu appears, and a verified game-window image are required for clean acceptance.
A repeated clean launch is required to confirm the final source batch.
Old crash folders and previous logs do not prove a crash in a current cycle.
Each cycle is recorded separately and source mutations during a load must be disclosed.

Campaign selection, country setup, console test-country initialization, save loading, simulated days, map combat, event behavior, and in-campaign graphics/audio are outside this user's requested startup test.
No campaign validation is claimed.
The project playtest skill's normal computer-control and broader gameplay workflow is narrowed by this explicit user instruction.

The exact existing desktop shortcut supplies the game executable, working directory, and `-debug` flag.
The shortcut, launcher configuration, Steam files, Workshop files, normal saves, and unrelated processes remain outside the repair write surface.
Only the HOI4 PID recorded for a cycle may be stopped before a relaunch.
Logs are archived into the run folder; they are not truncated to manufacture a clean result.

The project skill's referenced generic `.agents/skills/hoi4-autonomous-debug-playtest/SKILL.md` package is absent after searches in the repository and configured skill/plugin roots.
This package gap is recorded rather than treated as an installed capability.
The available project skill and explicit user authorization provide the process/log workflow used here.
