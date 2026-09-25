# Event 006 state 684 map inspection — 2026-09-25

## Disposition

Status: **STATE-SCOPED STRUCTURAL PASS; WORKSPACE MAP-LOCATOR VALIDATION OPEN**.

This parent-owned map inspection records the installed-map evidence for the existing IW-179 Caroline Islands anchor. It does not admit IW-179, clear its identity or rights gate, prove allocator uniqueness, or establish full SCN-008 map safety.

## State and province evidence

The vanilla state definition `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/684-Caroline Islands.txt` identifies state 684 as Caroline Islands, owned by Japan in 1936, with an FSM core and 11 provinces: 2489 and 13027–13036.

The current read-only `hoi4.map_inspect` request selected state 684 and those 11 provinces at map revision `f0f26f53ee1a5c6d970a05da8da746573ab078c0ce93ba75267f13bee260203b`. It returned `MAP_INSPECTED`, one inspected state, 11 inspected provinces, and zero diagnostics whose details referenced the selected state or provinces.

The inspector passed map-file/definition, bitmap geometry, state/strategic-region membership, and network/adjacency checks. The positions/locators check did not pass at workspace scope.

Selected map artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8a3a3910bd4b02fa68fb4a6344330ffc3cac15d71628673286e4b711f40347e/30ca779ed73e419ec4f9a4597dc812c1e87dfb898d6770fc0f4f16acf0474f8c/map-inspect.f0f26f53ee1a5c6d.json`.

## Workspace-wide map blocker

The map response reports `MAP_DIAGNOSTICS_TRUNCATED`: 2,654 omitted error diagnostics, comprising 1,323 `MAP_BUILDING_POSITION_INVALID` and 1,331 `MAP_PORT_ADJACENT_SEA_INVALID` findings. The tool retains only 1,999 of its 2,000 diagnostic slots, so this report cannot establish workspace-wide locator or port validity.

The scoped structural checks and absence of selected-state diagnostics do not prove the full 138-package allocator's anchor reservations, optional-state trimming, protected-host survival, supply, or collision scenarios. No map source was changed.

## Remaining work

Keep IW-179 fail closed until its accepted identity, portrait-source, provenance, and rights contract is met. For SCN-008, retain this state-scoped result as partial evidence and obtain current map and scenario evidence for the full candidate set; do not treat it as a substitute for the blocked workspace-wide position/locator check or live execution.
