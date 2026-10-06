# Event 002 Country and Focus Binding Audit

Date: 2026-10-06.

Disposition: unresolved for the initial runtime focus assignment of Event 002 dynamic countries; Event 014's post-reveal Wendigo focus overlay is explicitly wired in source.

Scope: read-only audit of ZZZ focus selection, Event 002 dynamic-country creation paths, shared focus-loading hooks, and the late Wendigo-to-Hannibal transition through Event 014.

No gameplay files were changed. This handoff is the only file written by this audit.

## Findings

`common/national_focus/002_zombies.txt:1-18` defines `ZZZ_focus` with a zero base score, `add = 10` for `original_tag = ZZZ`, `default = no`, and no focus nodes. Its comment says that the tree is intentionally blank because zombies have no strategic thinking.

The active Event 002 outbreak creator is `spawn_selected_dynamic_zombie_outbreak` in `common/scripted_effects/002_zombie_outbreak_effects.txt:2269-2401`; its dynamic-country branch at lines 2296-2301 uses `original_tag = ZZZ`, `copy_tag = ZZZ`, and marks the country with `zombie_outbreak_dynamic_country`.

The other in-scope zombie creators also use the ZZZ identity: `spawn_wendigo_incident_from_completion` at `common/scripted_effects/zombie_special_project_effects.txt:2515-2523`, `spawn_weaponized_zombie_outbreak_from_creator` at lines 3093-3103, `spawn_minor_weaponized_zombie_outbreak_from_creator` at lines 3227-3238, and the profiled and standard scenario creators at `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:1646-1661` and `1758-1772`. Each uses `original_tag = ZZZ` and `copy_tag = ZZZ`; no Event 002 outbreak creator in these active files uses `original_tag = ROOT`.

The inspected Event 002 files contain no `load_focus_tree = { tree = ZZZ_focus }` call, and `common/on_actions` contains no focus-tree load hook. The exact source hypothesis that Event 002 creators inherit a ROOT-origin focus tree is therefore not present in the current sources.

The initial runtime binding remains unresolved. Offline `National focus modding` says focus-tree country scores are evaluated before game start and are effectively not refreshed; installed `create_dynamic_country` documentation says `original_tag` identifies the new country and `copy_tag` copies content from the selected source tag, but it does not enumerate whether a newly created country receives the source tag's focus tree. Source alone cannot prove that the late-created ZZZ countries receive `ZZZ_focus`.

Vanilla's `instantiate_collaboration_government` at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\00_scripted_effects.txt:859-908` creates a dynamic country from `original_tag = country_to_initiate` without a `load_focus_tree` call. This is a structural precedent only and does not establish runtime focus-tree assignment for Event 002.

The Wendigo-to-Hannibal transition is intentionally treated differently after reveal. `cannibalism_prepare_wendigo_merge_identity` at `common/scripted_effects/014_cannibalism_effects.txt:21079-21093` sets `cannibalism_wendigo_hannibal_country` and `cannibalism_wendigo_focus_overlay_available`; the merge flow calls the identity setup at line 21360, then calls `cannibalism_load_wendigo_focus_overlay` at line 21401 before firing `chaosx.nr14.72` at line 21404.

That loader at `common/scripted_effects/014_cannibalism_effects.txt:21678-21691` checks `original_tag = ZZZ`, the Hannibal identity flag, reveal completion, overlay availability, the Wendigo character, absence of `world_end`, and absence of the already-loaded flag. It then runs `load_focus_tree = { tree = cannibalism_wendigo_focus_tree keep_completed = no }` and records the loaded flag. The matching tree is defined at `common/national_focus/014_cannibalism_focus.txt:2952-2995`. Event 002's Wendigo world-end event `chaosx.nr2.11` excludes both a pending transformation and `cannibalism_wendigo_hannibal_country` at `events/002_zombie_outbreak.txt:918-931`, so that branch does not compete after the reveal transition.

No broad or local source patch is recommended from this evidence. If live engine evidence later shows initial dynamic zombies lack the intended blank tree, the narrow guarantee would be an explicit `load_focus_tree = { tree = ZZZ_focus keep_completed = no }` inside each ZZZ dynamic-country initializer. That change should wait on evidence because the current source and docs do not establish a confirmed defect.

## Coverage checklist

| Surface | Result |
| --- | --- |
| ZZZ tag registration | Present at `common/country_tags/chaosx_countries.txt:2`; base country file is `common/countries/Zombie Outbreak.txt`; history file is `history/countries/ZZZ - Zombie Outbreak.txt`. |
| ZZZ focus tree | Confirmed as a deliberately empty tree selected by `original_tag = ZZZ`. |
| Event-created ZZZ countries | Creator sites and their `original_tag`/`copy_tag` values were checked; all in-scope zombie creators use ZZZ. |
| Initial dynamic-country focus binding | Unresolved from source; no explicit ZZZ loader is present and engine assignment timing is not stated in the cited docs. |
| Shared on-action focus selection | No `load_focus_tree` call found in `common/on_actions`. |
| Wendigo/Hannibal post-reveal tree | Explicit Event 014 load of `cannibalism_wendigo_focus_tree` is present and gated to the revealed ZZZ Wendigo identity. |
| Event 002 competing Wendigo world end | `chaosx.nr2.11` excludes the pending transformation and revealed Hannibal country. |
| Map and state setup | Not audited beyond locating dynamic-country creator blocks; no map writes were made. |
| Politics, portraits, flags, advisors, and parties | Not audited beyond ZZZ registration and the focus-transition character/flag gates. |
| Decisions, ideas, focus content, assets, and AI | ZZZ has no focus nodes or focus weights. Event 014's wider tree, decisions, ideas, assets, and AI were not audited. |
| Starting military, technology, industry, supply, and production | Not audited. |
| Playability and live behavior | Not verified in a live game or save. |

## MCP evidence

The read-only focus inspector returned `FOCUS_INSPECTED`, one tree, zero focus nodes, zero branches, fourteen continuous focuses, and layout hash `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`. Source revision: `fc61e5c497fbdb34e2672afa9058ff98bc0aebc4289331932263a9e113f1944d`. The inspector artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3012c49e9d247bdb8d92c422970412000126813550af3d306f85b12ae17bda77/35facbd003d9fa1a85e7c6c1501aa40612dc246fc53c11d49b2f0f3684bd32b7/focus-inspect.fc61e5c497fbdb34.json`.

The read-only focus renderer returned `FOCUS_RENDERED` with a 320 by 240 empty-tree view and no blockers. The SVG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9dcc4571fa7af7b5eebbfcb9a7486acae39e0f0e9d8b717b7b784fca441f95dc/e66e431efe0d3635592c3dd883185e359aa49787a6e2d6c1ed8b297563924531/ZZZ_focus.focus.svg`. Its only diagnostic was an unrelated vanilla localization warning for `continuous_restrict_freedom_desc` in `game:common/continuous_focus/generic.txt`.

Read-only event inspect/render was run for `chaosx.nr2.1`, `chaosx.nr2.11`, and `chaosx.nr14.72`. Each result was focused and partial at event-graph revision `ab653e1cd234b9986c95adebd9236f2fa0f8d6a37dfc14c65ec69da7dfbc5117`; the active analysis reported zero helpers, 10,432 unresolved workspace nodes, and an inline inventory limited to 64 of 398 paths. The `.nr2.11` neighborhood identified the Hannibal-exclusion trigger but left four helper calls unresolved in the focused graph. The `.nr14.72` neighborhood returned three local nodes and no unresolved entries. These event artifacts do not provide helper-lifecycle coverage.

The `.nr2.11` neighborhood JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/403ae9bbe9c4f6534c5791caa95a0b1886a7ec035f71cb6aacbc8f4a638e2a63/9bbcf4a01caf94aaa2be7fde359bc83c6fb72fa5a39ee396d604ba06805f936a/event-neighborhood-ab653e1cd234.json`.

The `.nr14.72` neighborhood JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/007e407d5667db3c61ff03633723bfa5ee35ee1f255c482d1b18f1ca0b21d1ea/5b5ddc37850f5b01203a3758ee9cf063ad1303825eb5f8ef3a8fe91ab82ce87a/event-neighborhood-ab653e1cd234.json`.

The Event 002 root neighborhood JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1eba7b59e6557486f1273524bc2e6683bfb294ccdecff9eabf4116cc2136b663/681fdbd03a0d0ccecb12a5102753c7ee595f096e6248bef576d86820996dc01f/event-neighborhood-ab653e1cd234.json`; it marks helper calls from `chaosx.nr2.1` unresolved, so direct source inspection was required to trace the creator.

The three neighborhood JSON artifacts above were retrieved in bounded byte ranges; each returned range and declared size were checked, and each reconstructed byte stream matched the artifact URI SHA-256.

## Source references

Offline `National focus modding` lines 43-66, revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`, says focus-tree country scores choose the tree before game start and describes `original_tag` filters covering breakaway countries.

Offline `Triggers` line 640, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, says `original_tag` also matches dynamic countries made through `create_dynamic_country`.

Offline `Scopes` line 664, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`, describes `original_tag`, optional `copy_tag`, child effects, and the dynamic-country scope change.

Installed `effects_documentation.md` lines 3033-3045, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, says `create_dynamic_country` creates the country and runs child effects on it; it says `copy_tag` copies from that tag instead of `original_tag` without enumerating focus-tree behavior.

Vanilla `00_scripted_effects.txt` lines 859-908 was located by `hoi4.source_lookup` under owner `instantiate_collaboration_government`, revision `7242261d5030c3a43edbabc7d2dc112f6a0445c5e18ad6eb00a25c238add4034`, and has local SHA-256 `93DDD0D2E9F7A1A5640CFDAFBAE6B9FF0E1B4EE57E829C81D13B0CAC23AD90BF`.

## Source hashes at audit time

| File | SHA-256 |
| --- | --- |
| `common/national_focus/002_zombies.txt` | `6A7B3F66480BC82C88A92AD27C5AC54D2BD064A15A5E646FC638E40A8A17A44E` |
| `events/002_zombie_outbreak.txt` | `9D3FBCA3098DA51FA0E946D8C98BE810E4DA5B2F24F869F7FB52915525D6F253` |
| `common/scripted_effects/002_zombie_outbreak_effects.txt` | `1ADF1B05F532D7A477E7A5DED2BF94ED20B0C0E6543DCC6F583F9AD9626C72ED` |
| `common/scripted_effects/zombie_special_project_effects.txt` | `7DB0E615854AB8D2C7138A80C89CFEACAC3C434A1DF448B1A236FEA75D3CBA7C` |
| `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | `E22C5129D0E27BDF1CD26AC9E58FE6F13A7DCDF7D662411E3EA7ACFCAD6A2FB8` |
| `common/on_actions/002_zombie_outbreak_on_actions.txt` | `AADF42B89EBCC4062CB5A73387C13DDC9A679F9CC18BFF7FD776E23E250E1C6F` |
| `events/014_cannibalism.txt` | `16C7CE010CCE25202867CBE338808166711C85D03FD6A0E8AA2CC35DDE01D302` |
| `common/scripted_effects/014_cannibalism_effects.txt` | `F5160BEC0DE58954F95E07A7FC1DC37720236F48CEE1E56F37F15B58B3724DC9` |
| `common/national_focus/014_cannibalism_focus.txt` | `8C8FCCFA861A3D72D99C602F9604AFC2C5E702CBD8F8B8362ACEA69DD54640F7` |
| `common/on_actions/014_cannibalism_on_actions.txt` | `19D14AA4E98B5DA5DB062A5F526E59F5292AD125470964071B3159C4B46D4AD7` |
| `common/country_tags/chaosx_countries.txt` | `B539C59833D3E264687EBBDEC348814456168F14BC01564938EBA58552ECFB60` |
| `common/countries/Zombie Outbreak.txt` | `868E014430A2CACC7D16A49F07D97EC4B30C4D49486936775B19EC270565BFB7` |
| `history/countries/ZZZ - Zombie Outbreak.txt` | `894D10F3E57D131600D37B7C0C87E70083323716CAC0F8DF5B46D6BC83358E69` |

## Validation limits and remaining work

No source patch, live-game check, save inspection, map edit, test run, index operation, or commit was performed.

The parent should resolve initial ZZZ focus assignment only if runtime evidence or a stronger engine reference shows that `create_dynamic_country` does not inherit the intended source tree. This audit does not certify the wider Event 002 country package or the complete Event 014 focus tree.

## Patch status and workflow

Files changed: this handoff only; no gameplay identifiers, state ids, focus ids, localisation keys, or formable ids were changed.

Before/after behavior: none; this was a read-only audit.

Skills read and applied: `chaos-redux-focus-trees`, `chaos-redux-events`, and `chaos-redux-subagents`; no skill was changed.

The full `common/national_focus` scan found only `ZZZ_focus` and the Event 014 Wendigo overlay using `original_tag = ZZZ`; no third country-tree selector for this identity was found.
