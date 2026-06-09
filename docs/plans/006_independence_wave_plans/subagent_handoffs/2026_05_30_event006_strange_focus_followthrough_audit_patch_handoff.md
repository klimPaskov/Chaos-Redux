# Event 006 Strange Focus Follow-through Audit and Patch Handoff

Scope: Event 006 Independence Wave strange/containment focus follow-through. No flag, country, history, Event 005, asset, or country-package files were edited.

## Changed files

- `common/national_focus/006_independence_wave_focus.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_event006_strange_focus_followthrough_audit_patch_handoff.md`

## High-priority fixes first

1. `independence_wave_moral_tribunal` and `independence_wave_unmarked_ministry` used `available = { ... }`, so the wrong sealed outcome branch could be visibly present but locked after the hidden module appeared. Patched both first focus nodes to `allow_branch = { ... }` so the contained branch is hidden until `independence_wave_strange_contained` and the revealed branch is hidden until `chaosx_iw_strange_revealed`.
2. Strange-package startup added `constant:independence_wave_focus.radicalization_gain` to `independence_wave_occult_pressure`. Patched it to `constant:independence_wave_focus.occult_pressure_gain_medium`, matching the variable being changed and keeping tuning in the focus constants table.

## Changed focus ids

- `independence_wave_moral_tribunal`: branch visibility changed from selectable-gate `available` to hidden branch-gate `allow_branch`.
- `independence_wave_unmarked_ministry`: branch visibility changed from selectable-gate `available` to hidden branch-gate `allow_branch`.

No focus ids were renamed, removed, or moved.

## Route coverage table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Hidden strange module reveal after sealed audit, containment, or reveal | `independence_wave_sealed_bureau_charter` | Present | `allow_branch` accepts `independence_wave_sealed_archive_audited`, `independence_wave_strange_contained`, or `chaosx_iw_strange_revealed`; reward calls `independence_wave_focus_sealed_bureau_charter`. |
| Containment follow-through | `independence_wave_moral_tribunal` -> `independence_wave_quarantine_bureau` -> `independence_wave_restore_public_registry` | Present, patched | Root branch now stays hidden until containment succeeds. Descendants keep the same containment `available` checks as a safety lock. |
| Revealed strange follow-through | `independence_wave_unmarked_ministry` -> `independence_wave_census_without_names` -> `independence_wave_border_office_of_absence` | Present, patched | Root branch now stays hidden until strange reveal. Descendants keep the same revealed-route `available` checks as a safety lock. |
| Containment versus reveal incompatibility | `independence_wave_moral_tribunal` and `independence_wave_unmarked_ministry` | Present | Mutual exclusion is defined on both root branch nodes. |
| Decision-driven layout refresh | Sealed audit, reveal, containment success, containment failure effects | Present | `mark_focus_tree_layout_dirty = yes` is present on effects that set audited/contained/revealed branch flags. |

## Missing or simplified content

- This is still a bounded first strange module, not a full strange route family. It does not create strange tags, final strange formables, strange super-events, final strange assets, or broad world-threat behavior. `docs/events/006_independence_wave.md` already states that limit.
- The root module still requires `independence_wave_recognition_desk`. If design intent is that sealed/contained/revealed content should become selectable before the normal recognition trunk is complete, the parent should decide that as a route-design change.
- The contained and revealed branches have only three focuses each. They are functional follow-through modules, not full late-game strange branches.

## Icon coverage table

| Focus id | Icon id | Coverage | Notes |
| --- | --- | --- | --- |
| `independence_wave_sealed_bureau_charter` | `GFX_goal_generic_intelligence_exchange` | Present | Vanilla `goals.gfx` defines the sprite. |
| `independence_wave_moral_tribunal` | `GFX_focus_generic_self_management` | Present | Vanilla `goals.gfx` defines the sprite. |
| `independence_wave_quarantine_bureau` | `GFX_focus_generic_home_defense` | Present | Vanilla `goals.gfx` defines the sprite. |
| `independence_wave_restore_public_registry` | `GFX_goal_generic_national_unity` | Present | Vanilla `goals.gfx` defines the sprite. |
| `independence_wave_unmarked_ministry` | `GFX_goal_generic_political_pressure` | Present | Vanilla `goals.gfx` defines the sprite. |
| `independence_wave_census_without_names` | `GFX_goal_generic_allies_build_infantry` | Present | Vanilla `goals.gfx` defines the sprite. |
| `independence_wave_border_office_of_absence` | `GFX_goal_generic_more_territorial_claims` | Present | Vanilla `goals.gfx` defines the sprite. |

## Localisation and reward mismatch list

- All seven hidden-module focus ids have name and `_desc` localisation in `localisation/english/006_independence_wave_l_english.yml`.
- No focus/localisation rename was needed.
- No reward text mismatch was found for the seven-focus module. Rewards match the contained/revealed route tone: containment reduces occult pressure and raises legitimacy/cohesion, while reveal raises occult pressure, radicalization, manpower, claims, and foreign attention.
- Corrected one reward/setup mismatch in `independence_wave_setup_released_country`: occult pressure now uses an occult-pressure constant instead of the radicalization-gain constant.

## AI behavior gaps

- All seven hidden-module focuses have `ai_will_do`.
- The focus AI distinguishes containment/reveal conditions locally, but the broader AI strategy file only has a generic `independence_wave_strange_package_containment` posture. There is no separate AI strategy for contained public-registry recovery versus revealed unmarked-ministry escalation.
- Focus `ai_will_do` base values remain local numeric weights, matching the current focus-file pattern. The route thresholds and reward values use script constants.

## Route behavior before and after

- Before: once `independence_wave_sealed_bureau_charter` appeared, the contained and revealed branch roots were visible as locked focuses if their outcome flag was absent.
- After: the contained branch root appears only after `independence_wave_strange_contained`; the revealed branch root appears only after `chaosx_iw_strange_revealed`. Existing `mark_focus_tree_layout_dirty` calls refresh the tree when those flags change.
- Before: strange-package setup raised occult pressure by referencing `radicalization_gain`.
- After: strange-package setup raises occult pressure with `occult_pressure_gain_medium`.

## Validation run

- `rg -n "<=|>=" common/national_focus/006_independence_wave_focus.txt common/script_constants/006_independence_wave_constants.txt common/scripted_effects/006_independence_wave_effects.txt localisation/english/006_independence_wave_l_english.yml docs/events/006_independence_wave.md`: no matches.
- Brace balance:
  - `common/national_focus/006_independence_wave_focus.txt`: `brace_balance=0`
  - `common/script_constants/006_independence_wave_constants.txt`: `brace_balance=0`
  - `common/scripted_effects/006_independence_wave_effects.txt`: `brace_balance=0`
- Localisation format:
  - `xxd -p -l 3 localisation/english/006_independence_wave_l_english.yml`: `efbbbf`
  - `rg -n "^\\s*[^#\\n]+:0\\s" localisation/english/006_independence_wave_l_english.yml`: no matches.
- `git diff --check -- common/national_focus/006_independence_wave_focus.txt common/scripted_effects/006_independence_wave_effects.txt common/script_constants/006_independence_wave_constants.txt localisation/english/006_independence_wave_l_english.yml docs/events/006_independence_wave.md`: no whitespace output. These Event 006 files are untracked in the current parent worktree, so I also ran `git diff --no-index --check /dev/null` on the two touched script files; both produced no whitespace output and exited non-zero only because `/dev/null` differs from the full file.
- Icon references checked against vanilla `interface/goals.gfx`; all seven icon ids are defined there.

## Skipped validation and why

- No in-game validation was run. This subagent performed static validation only.
- No full Event 006 completion audit was attempted; the prompt scoped this pass to strange/containment focus follow-through.
- No commit was created because the relevant Event 006 gameplay files are currently untracked parent-owned worktree files. Committing them here would stage far more than this narrow patch.

## Remaining route risks

- If the parent wants the sealed module to bypass the normal recognition trunk entirely, `independence_wave_sealed_bureau_charter` needs a route-design decision, not a small audit patch.
- The strange branch still lacks custom focus icons and final strange route assets. Current generic icons are valid and defined.
- The broader strange route needs later AI strategy separation if contained and revealed states become long-lived route families.

Plan handoff path: none written beyond this audit/patch handoff.
