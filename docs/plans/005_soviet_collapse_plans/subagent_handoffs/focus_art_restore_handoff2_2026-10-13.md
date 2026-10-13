# Event 005 focus-art restoration handoff

Disposition: implemented within the user-authorized restoration scope. The parent registry at `bee7a9ae39aa6c94f321c345da90303be2d5f5a6` is restored exactly, and current focus consumers are mapped so the legacy definitions are no longer shadowed.

## Changed files and identifiers

- `interface/005_soviet_collapse.gfx` is an exact byte copy of the parent-commit file. It restores 3,548 sprite definitions, including the legacy focus overlay art registry.
- `interface/005_soviet_collapse_focus_icons.gfx` retains 1,436 definitions for 718 post-parent focus IDs and removes 2,024 duplicate base/shine declarations that shadowed existing focus IDs.
- 232 missing DDS textures required by the restored legacy sprites were recovered byte-exactly from the same parent commit's Git LFS objects. Their paths, SHA-256 values, LFS object IDs, dimensions, and byte lengths are recorded in `focus_art_restore_texture_manifest_2026-10-13.json`.
- The row-level source and binding crosswalk for all 1,760 current focus IDs is `focus_art_restore_crosswalk_2026-10-13.csv`. It records the icon sprite, current and previous texture paths, registry, dimensions, and texture hash.

The current 1,760 focus IDs divide into 1,012 existing IDs restored to their parent art, 718 post-parent IDs that keep their dedicated current sprites, and 30 UWR/KMB specialist IDs kept in `interface/005_soviet_collapse_uwr_kmb_icons.gfx`. For example, `AAX_civil_rule` again uses `GFX_focus_AAX_civil_rule` with `005_aax_custom_splinter_focus.dds` at 86x94; `AAX_aksakal_mediation` retains its post-parent `focus_005_aax_aksakal_mediation.dds` binding at 88x100.

No focus script, route logic, reward, AI weight, localization key, or gameplay behavior changed. Existing focus source IDs and their `icon` names remain the same.

## Route behavior before and after

Before this patch, 1,012 existing focus IDs had matching sprite definitions in both registries. The later `005_soviet_collapse_focus_icons.gfx` definitions pointed those IDs to generated or reused one-to-one textures and shadowed the older overlay bindings.

After this patch, the exact parent definitions supply those 1,012 IDs and the duplicate newer declarations are absent, so existing IDs use the original art treatment again. The 718 focus IDs without a parent registry binding keep their current texture assignments, and all 30 specialist IDs remain in their separate registry.

## Asset and source evidence

The runtime source was compared against `bee7a9ae39aa6c94f321c345da90303be2d5f5a6`; the restored main GFX file is byte-identical to that commit. The original in-worktree registry bytes were preserved before editing under `.tmp/interface_restore_handoff2/focus005/005_soviet_collapse.gfx.before` and `.tmp/interface_restore_handoff2/focus005/005_soviet_collapse_focus_icons.gfx.before`, with SHA-256 hashes `3508a457907ee8a005c97e604902b3dfa005eb3fd1e2ab298b1bd1341330fa28` and `35729eddc270ff3cf29f648a7525076474fc23e8fbd0ebb5143b4b6cd9da5f73` respectively. The exact parent source snapshots are preserved alongside them in that same temporary folder.

All 232 restored focus textures match the parent LFS object SHA-256 and have valid DDS headers and dimensions. Their dimensions are 86x94 (137 files), 88x100 (86), 84x94 (4), 80x89 (2), 77x94 (1), 82x86 (1), and 82x98 (1).

A source crosswalk over all Event 005 focus files found 1,760 icon assignments, with each base sprite, matching `_shine` sprite, and texture resolving. There are no duplicate sprite names across the restored main registry, the retained new-focus registry, and the UWR/KMB specialist registry.

The offline wiki reference `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`, lines 305–336 (snapshot dated 2026-09-19), describes GFX sprite registration, duplicate-name load order, and the paired focus and `_shine` sprite names. Vanilla precedent was read from `common/national_focus/argentina.txt:46`, `interface/goals.gfx:5656`, and `interface/goals_shine.gfx:39229` in the installed game; it uses separate base and shine definitions for a focus icon.

## Validation limits and remaining risks

`hoi4.reference_context` was called for focus guidance but did not return an artifact before the request stalled; it was not retried. Direct local wiki and source review supplied the relevant evidence. The installed documentation directory has no national-focus-mod documentation page. Focus inspection and rendering were not run in this subtask, as requested; the parent separately reported the 600-second renderer failure and owns the screenshot list. No game was launched.

At the initial handoff, 186 restored declarations referenced 95 additional absent historical texture paths and the static scan found no active consumers outside the registry.
The follow-up recovered all 95 exact original payloads from earlier Git/LFS objects; every path is present and hash-verified, and every original declaration remains registered.
The current source has no missing legacy texture registration; the initial absence is historical evidence, not a remaining blocker.
The parent independently checked that no sprite ID present in either pre-edit Event 005 registry is missing from the current registrations.

No simplifications or substitutions were made. No localization or focus IDs were changed. No commit was created, as directed by the parent task.

The additional 95-path exact-source/hash/dimension evidence is `focus_art_restore_legacy_texture_recovery_2026-10-13.json` in this handoff folder.
