# Event 006 formable state-puzzle gameplay integration handoff

## Scope completed

This handoff covers the gameplay and compiled state-puzzle consumer layer for FORM-01, FORM-02, FORM-03, FORM-04, FORM-05, FORM-07, FORM-08, FORM-09, FORM-12, FORM-13, FORM-16, FORM-18, FORM-39, and FORM-48.

## Files changed

- `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt` contains fourteen activation helpers, exact per-state qualification wrappers, and fourteen finite territory-summary helpers.
- Fourteen consumer specs under `docs/formables/state_registry/consumers/` share the `independence_wave_formables` group and grouped window.
- Eleven decision-category files attach `independence_wave_formable_state_puzzle_scripted_gui` to seventeen Event 006 formable categories, including both signature-package categories.
- `has_independence_wave_selected_formable_state_puzzle_territory` is required by the shared player and AI commit trigger, while FORM-05 requires its helper in the dedicated proclamation trigger.
- `docs/events/006_independence_wave/systems/formable_registry.md` documents the consumer crosswalk, finite state sets, activation precedence, and build boundary.

## Helper map and behavior

Each family activation helper first checks a pending founding invitation whose
family variable matches the family. The selected/profile and post-formation
branches are nested under `NOT = { has_pending_independence_wave_formable_founding_invitation = yes }`, which prevents two family overlays from being visible at once. The group OR helper is available to the generic extension, while specs retain exact family activation helpers.

Per-state wrappers delegate to the existing Event 006 package/tag/anchor
contracts: FORM-01 uses SCO/WLS/BRI and both Scottish compact states; FORM-02 uses ICE/AKX/GZX/SCO and both Scottish compact states; FORM-03 uses
AFX/AGX exact carrier anchors or a frozen `BEL_flanders` delegation at state 6; FORM-04 uses RHI/AJX; FORM-05 uses COR/ARX/ASX;
FORM-07 uses CAT/NAV/GLC; FORM-08 uses TRA/AXX; FORM-09 uses BBX/BAX/BOS/MAC/MNT/KOS;
FORM-12 and FORM-13 use the CHU carrier and three frozen Middle Volga member anchors; FORM-16 uses ARM/GEO/AZR exact anchor ownership/control; FORM-18 uses the ASY carrier and both frozen corridor member anchors; FORM-39 uses FIJ/PNG/WPG;
and FORM-48 uses HBX/HAW/FSM. No state or country scan is used and no GUI event
target is created.

Summary helpers use finite boolean combinations rather than dynamic scans.
FORM-02 enumerates four triplets for a three-of-four summary, FORM-05
enumerates three pairs for a two-of-three summary, and FORM-09 enumerates all
twenty triplets for a three-of-six summary. FORM-08 intentionally returns
`always = no`: its researched candidate set is only states 84 and 82 while the
requested summary count is three, so no fabricated third state is introduced.

## Constants, lifecycle, and migration

No new numeric constants were added. Candidate state IDs and required counts
remain source-declared in each consumer spec, while family identity values reuse
the existing `independence_wave_formable_family` constants. The wrappers are a
thin migration layer over existing family helpers; no duplicated package
admission logic is introduced. The state-puzzle layer has no persistent flags,
variables, event targets, or cleanup effects of its own.

## Validation evidence

- All fourteen consumer specs parsed and compiled successfully.
- Category source inspection found exactly seventeen attachments to the shared scripted GUI.
- The added candidate-state map inspection covered `6, 133, 249, 651, 256, 399, 397, 676, 421, 413`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a5152d11c8f65968c12aa6afc775160027e978385a4c818606dbf86e7157158/2971766206eb90ff8cd80d505d8f2596b8a8879e9d93ae713603671bbd7b5141/map-inspect.51a54b869115a612.json`. Selected state and geometry checks passed. Workspace-wide locator diagnostics remain outside this state-puzzle change.
- The mandatory map inspection covered candidate states `1,14,34,36,42,51,82,84,100,104,105,106,114,115,121,122,165,171,184,185,229,230,231,337,378,523,629,636,669,684,792,802`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d69d0834ae73f420e42bfdd6e497722a781f45005d9994420a915dc546f7128/11b66ede49f405df53a7218b343529642daa483f772e0db5d4c646c433d7da9e/map-inspect.ddef3d899acfd6ef.json`. Map validation passed source/geometry/state-region/network checks but reported pre-existing map-position diagnostics (`MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`).
- Event scan for `chaosx.nr006.1` returned partial helper projection with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/233310e9a4f4754f2cc9c0b0a01e6f92f178ce819b3f24e1dd735c284eb491d2/c921c6cec43c0e19a82d1e15cbb579b0f402ef3d05432849c4518c4da23ab4e1/event-scan-8c2577b32af5.json`; helper projection was deferred by the workspace-wide scan.
- Read-only GUI inspection of `chaosx_independence_wave_formable_state_puzzle_window` returned artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87ef8fee524bdc51dc2ba2cc88243364b679996b0b4ece8309eeab9e7c126fe6/b690010cf1ebd2e897ecc1a3a19738d0be5d4299d6318290f835e6c7ad11183a/gui-inspect.54328958868e507f.json`. The workspace reported pre-existing GUI graph collisions, missing generated-window diagnostics, and invalid scripted contexts; no GUI rewrite was attempted.

## Parent build and MCP closure

The parent compiled all fourteen consumer specs, producing fourteen manifests and 100 readable DDS state pieces under `gfx/interface/formables/state_puzzles/006_form*/states/`. The runtime generator emitted the shared group window, scripted GUI, GFX declarations, dynamic localisation, and fourteen family overlays. All 100 DDS files open successfully.

Current `hoi4.gui_inspect` returned `GUI_INSPECTED` for `chaosx_independence_wave_formable_state_puzzle_window`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ef2673ff8f17120d4af57ee1ea186242cab51bbd0de180293f6dee95f5ba358/466d18177cb6f43241458de2d3e61a09c36b90b67dbddf56274eade7e6cc18a1/gui-inspect.fc2200e9c790f7c3.json`. Its aggregate overlap diagnostics arise because the offline scenario displays mutually exclusive family overlays together. Runtime visibility remains guarded by one human-only group block and one activation helper per family.

Current `hoi4.gui_render` returned `GUI_RENDERED` for the shared window at 1920x1080 and 1366x768: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5cf4a0e6908e754ba9e1bae29b05ae013092399118afcfe42cedf62d2833fe9/bad290e958062d59c6887532469bc60e48c725f8a9ce6ea2fd8f95c81eb43eb5/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

## Known limitations

FORM-07 remains identity fail-closed under its existing package contract, and
FORM-48 remains operationally unreachable until its researched HBX/HAW/FSM
identity and package gates are satisfied. FORM-08 is explicitly unreachable at
the state-summary layer until a reviewed third anchor is added; this handoff
does not weaken that contract.
