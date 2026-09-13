# Event 027 doctrine mastery index runtime analysis

## Status

This is a read-only Launch 08 investigation dated 2026-09-05.

The exact behavior-preserving repair is blocked because the launch runtime rejects every `index` child in the Event 027 `add_mastery` blocks, while the installed documentation and offline wiki document that field as valid.

For this analysis, no gameplay source, constants, weights, technology definitions, event behavior, staging area, or save was edited, staged, committed, or launched.

The requested scope is limited to `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`, its direct consumers, the Launch 08 log evidence, and the doctrine/technology syntax references.

## Launch 08 evidence

The primary runtime evidence is `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_08/logs/error.log`.

The log contains 428 lines for `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`: 214 `Invalid effect 'index'` lines and 214 paired `Unknown effect-type: index` lines.

There are 107 unique source locations, from source line 17155 through 19699 in steps of 24, and each location is reported twice.

The first parser pass reports all 107 locations at 10:31:56, beginning with `line : 17155` and its paired `near line: 17156` entry.

The second parser pass reports the same 107 locations at 10:32:19 and ends with `line : 19699` and its paired `near line: 19700` entry.

The first affected block is the `mobile_infantry` / `infantry` branch at source lines 17150-17155, where `index = 0` is the fifth child of the nested `add_mastery` block.

The last affected block is the `rangers_2` / `special_forces_second` branch at source lines 19694-19699, where `index = 1` is nested in the same position.

Unrelated parser messages immediately before this batch concern `has_terrain` scope and missing AI helper triggers in `common/scripted_effects/027_doctrine_research_effects.txt` around lines 3725-3772; they do not explain the `index` failures.

The Launch 08 code revision is recorded in `logs/launch_08/logs/code_revisions.log` as game hash `a729d47bd1c55457e6886b6eeb2fcdef4ac05057` with timestamp `2026-06-29 15:17:03 +0200`.

The installed executable identifies itself as `Operation Postern v1.19.2.0.a729`, `hoi4_branch.txt` reports `1.19.2.0/develop`, and `appmanifest_394360.acf` reports build ID `23969257`.

The matching `a729` suffix and 1.19.2 branch evidence make an old pre-doctrine engine an unproven explanation; local files do not provide a release-specific mapping that proves why this binary rejects a field documented as available since 1.17.

## Source shape and direct consumers

`common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt` currently has 21648 lines, 107 `add_mastery = {` blocks, and 107 `index =` lines.

All 107 `index` lines are inside their corresponding `add_mastery` blocks, with no `index` line at the surrounding scripted-effect or `while_loop_effect` level.

The current file uses only literal indexes `0`, `1`, `2`, and `3`; the distribution is 30, 32, 21, and 24 blocks respectively.

The representative source form is:

    doctrine_research_exact_step_mobile_infantry_track_infantry = {
    	while_loop_effect = {
    		add_mastery = {
    			amount = @DOCTRINE_RESEARCH_MASTERY_POINT_INCREMENT
    			folder = land
    			sub_doctrine = mobile_infantry
    			track = infantry
    			index = 0
    		}
    	}
    }

The exact mastery dispatcher is `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt:21027`, and it calls the static branch helpers after reading the native level.

The public mastery dispatcher at `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt:21403-21408` routes Special Forces through its track-qualified adapter and all other domains through `doctrine_research_apply_exact_mastery`.

The confirmation path at `common/scripted_effects/027_doctrine_research_effects.txt:3513-3529` selects the empty-track or active-track mastery path, and `:3517` calls `doctrine_research_apply_mastery` after the receipt is prepared.

The human confirmation event at `events/027_doctrine_research.txt:4779` calls `doctrine_research_confirm_selection`, so the rejected helper blocks are on the live confirmation path rather than dead declarations.

The shared track-index adapter at `common/scripted_effects/027_doctrine_research_effects.txt:2121-2136` maps infantry, combat support, armor, and operations to indexes 0-3, maps the four naval and four air tracks to indexes 0-3, and maps the two Special Forces tracks to indexes 0 and 1.

The receipt stores that selected track index at `common/scripted_effects/027_doctrine_research_effects.txt:2152`, so removing the `add_mastery` filter would break the exact-target proof the receipt is designed to preserve.

The empty-track adapters use the documented extended `set_sub_doctrine` form with the same folder and track indexes at `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt:19719-20889` and `:21417-21612`.

## Syntax references

The installed documentation explicitly places `index` inside the `add_mastery` argument block at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:1477-1500`.

That documentation describes `index` as an optional 0-indexed track filter after `folder`, `grand_doctrine`, `sub_doctrine`, and `track`, which is the same nesting and ordering used by the Event 027 source.

The same installed documentation documents the extended `set_sub_doctrine` form and clarifies that its `track` value is the 0-indexed position among all tracks in the folder at `effects_documentation.md:7774-7797`.

The installed trigger documentation covers the paired native readback used by this helper at `triggers_documentation.md:4181-4194` for `has_mastery_level`.

The offline Effects page records the same `add_mastery` signature, including `index = <int>` and version added 1.17, at `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:614-622`.

The offline Doctrine modding page lists `set_sub_doctrine`, `add_mastery`, `has_mastery`, and `has_mastery_level` as the native doctrine effects and triggers at `paradox_wiki/Doctrine modding - Hearts of Iron 4 Wiki.md:23-42`.

The offline Technology modding page confirms that doctrines are technology objects in engine code, that their definitions are folder-based, and that modern sub-technologies use explicit indexes at `paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md:31-35` and `:256-262`.

## Vanilla precedent search

The installed vanilla source tree contains many `add_mastery` examples, but the bounded search found no vanilla source block that supplies an `index` child.

Representative precedents include `common/national_focus/usa.txt:6789-6792` with amount and track only, `common/national_focus/italy.txt:3897-3901` with folder, grand doctrine, and track, `common/national_focus/australia_taog.txt:10541-10545` with folder and track, and `events/SEA_Communist_China.txt:4299-4302` with amount and track.

The repository test precedent at `common/scripted_effects/chaosx_test_country_effects.txt:144-148` also omits `index`.

Therefore vanilla precedent confirms the nested `add_mastery` block and its ordinary filters, but it does not prove a runtime spelling or acceptance path for the optional `index` filter.

The binary embeds the same generated `add_mastery` documentation and the `TRACK_EFFECT_CONDITION_TRACK_INDEX` label, but those strings do not prove that the parser accepts the field in this exact build or context.

## Parser finding

The parser error points at the `index` child itself, not at the surrounding `add_mastery`, `while_loop_effect`, or scripted-effect declaration.

The identical error on every literal value across all 107 branches isolates the failure to runtime support or runtime registration of the `index` child, rather than a bad value, bad ordering, or a single malformed block.

Moving `index` outside `add_mastery`, renaming it to `track_index`, replacing literals with variables, or reordering the existing children has no documented or runtime evidence and is therefore not a safe repair candidate.

The installed docs and offline wiki make the current nesting the documented syntax, while the Launch 08 runtime rejects that syntax; this is an exact documentation/runtime capability blocker.

The available local files cannot distinguish a release-specific documentation mismatch, a parser regression, or a context-specific engine limitation in `v1.19.2.0.a729`.

The candidate syntax outcomes are:

| Candidate | Evidence | Disposition |
| --- | --- | --- |
| `index = 0` nested in `add_mastery` | Exact installed-doc and offline-wiki form, rejected at all 107 source locations | Blocked by runtime |
| `track_index = 0` | The token appears in binary dynamic-token strings, but not in the `add_mastery` documentation or any source precedent | Unproven and unsafe |
| `index = { value = 0 }` | No installed documentation or vanilla precedent | Unproven and unsafe |
| Omit `index` | Documentation says omitted filters pass, which broadens the target set | Behavior-changing and rejected |
| Replace with `set_sub_doctrine` | Changes assignment state instead of adding mastery to the selected active track | Not equivalent and rejected |

## Why dropping `index` is not safe

The installed documentation states that omitted filters pass, so deleting `index` would broaden `add_mastery` to every matching track rather than preserve one exact slot.

The Special Forces branches demonstrate the concrete risk: the same eight subdoctrine IDs have active branch helpers for both `special_forces_first` with `index = 0` and `special_forces_second` with `index = 1` at source lines 19339-19699.

The Event 027 receipt separately records the selected track index and verifies a one-level native postcondition, so a broad mastery application would invalidate the intended receipt and banked-mastery behavior even if the file loaded.

Replacing `index` with `set_sub_doctrine` is not equivalent because that effect changes subdoctrine assignment and does not add mastery to an already active exact track.

No numeric, effect, subdoctrine, track, or balance substitution is proposed.

## MCP evidence and modern subdoctrine limitation

The mandatory read-only technology inspection was run with `hoi4_tech_inspect` in `lint` mode for `folderId = land`, both directions, sub-technologies included, depth 2, node limit 128, and refresh enabled.

It returned `TECH_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0` at revision `90e33d754169693e59b0484cbf76dcd86b6a2dc22d3004ac3ef370c8899fe177` with graph hash `b0c030ed8a5ed4716e0945160c8d585a1e64bc52352556b638a91e4c909bfa0c`.

The inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83b8f73b73adfae2fa1785b6977e232de99f9ea12c5626db049bcf93810e2cf4/d08bf9fa28beeaf550769aa9eebc367e6186738bbad282900c43a8554e59d7f9/technology-lint-90e33d754169.json`.

The route resolved the current technology graph, but its aggregate validation remained false because the full workspace reported 1357 blocking technology diagnostics; this does not validate effect-parser fields.

The focused read-only doctrine render used `hoi4_tech_render` with `folderId = land` and `view = doctrine`.

It returned `TECH_RENDERED` at revision `cd3ca880b2036d137c9162aeba39bb4597da7785d9fc2f94d60c72fa13f6bd7c`, graph hash `c5fce2b700030282ed702f068a95763e3548ca391b881831136ad10fb73034d0`, and six selected doctrine nodes.

The doctrine render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/570d949fc327e525b50d28b1113e5e1b6cf7a7f87190f1171c7994a398fe77e5/c708cc7d3d2da34abdf72084a7828a53f6a96df2163d229a0a989e6d76d99b68/technology-doctrine-cd3ca880b203-manifest.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a1f0bbe687f0d64dc6d5b3fb64d3235427ffedf749275f9329156668dc59f6e/d375e1d062f9b7ba72e146ee980f77b3aa6dffc6a33b389190aeb29b458fc169/technology-doctrine-cd3ca880b203.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4b1d78531041dab827aca19f1c8156f8a946a311356e083f8829885aea54945/113866cf6147ae0c5276b33294319ae295f991456ce7dd208ef334b235c11ea3/technology-doctrine-cd3ca880b203.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7945b2bc3acf4ccc0cace4f91640955341bd003fb622adb74d981c7ca89100c/f668edf6434b9c7ff11751ffae69726cb642d01d2588be4e921f11fa54746c6f/technology-doctrine-cd3ca880b203.png`.

The targeted `technologyId = chaos_warfare` explain query returned `TECHNOLOGY_NOT_FOUND` because `chaos_warfare` is a Grand Doctrine identifier, not a technology identifier; folder-level doctrine rendering is the available route for this modern subdoctrine surface.

The current tool catalog exposes `hoi4_tech_inspect`, `hoi4_tech_render`, and `hoi4_tech_compare`, but no separate standalone Technology Tree Viewer route.

That viewer absence is recorded as an evidence gap, and the available source-backed technology routes cannot prove whether the running effect parser accepts `add_mastery.index`.

The narrow Event MCP lint for `chaosx.nr27.1` also completed as `EVENT_INSPECTED_PARTIAL` at revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8` with graph hash `c6850dd8ad35035c9a83ff251c3df14e4e6123af303e2037d032ccbf5ea51b2e` and no returned blockers.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1dd848cc08b5a44813283976013d74b407175bc3fe130e1eeb83a4d41aa5c992/0459f8fa2f518fa94e2f27c2df4912189d8a9def7286021faa7a88effdaeeb37/event-lint-1102e50fad94.json`.

That Event MCP result is partial because workspace-wide helper and lifecycle projections were deferred, and it does not replace the Launch 08 engine parser evidence.

## Disposition and required follow-up

No minimal behavior-preserving source repair is proven in the available evidence.

The exact blocker is the absence of a local engine or MCP route that validates `add_mastery.index` or supplies an authoritative alternate spelling for the installed `v1.19.2.0.a729` runtime.

The next repair tranche should use a minimal one-block fixture against the exact binary or an equivalent authoritative engine schema test, then apply only the confirmed syntax to all 107 branches.

Until that evidence exists, preserve every `index` child and do not launch another QA pass for this tranche.

No simplifications, omissions, or behavior substitutions were made in this read-only investigation.
