# Event 006 Starter Package Audit And Icon Wiring Parent Handoff

Date: 2026-06-01

## Scope

Closed a bounded starter-package hardening pass for Event 006 Independence Wave after the scripted-GUI value-board tranche. This pass focused on existing starter overlays only: OGB/Volga, ASY, DNZ, UGA/Buganda, SOK, GAR, CHR, KUR, and the generic railway Timetable Authority path.

## Parent Changes

- Replaced the stale `GFX_decision_independence_wave_border_commission` decision icon reference on `independence_wave_map_kurdish_pass_districts` with registered `GFX_decision_independence_wave_border_survey`.
- Normalized top-level indentation for four existing Dossier Board host-response scripted effects so helper scans can identify them correctly:
  - `independence_wave_evacuate_host_archives_effect`
  - `independence_wave_offer_local_autonomy_effect`
  - `independence_wave_arrest_committee_couriers_effect`
  - `independence_wave_arm_loyalist_councils_effect`
- Wired the generated Kurdish Mountain Assembly idea icon:
  - `GFX_idea_independence_wave_kurdish_mountain_assembly`
  - `picture = independence_wave_kurdish_mountain_assembly`
- Updated the idea-icon GFX handoff after wiring.

## Subagent Outputs Reviewed

- `chaosx_country_package_auditor` wrote `2026_06_01_event006_starter_package_current_audit_handoff.md` and patched bounded Event 006 package issues:
  - Charrua/Kurdistan integration mission timeout constants.
  - Stale Event 005 `soviet_collapse_breakaway_state` guards to `soviet_collapse_breakaway`.
  - KUR inclusion in the local-polity package achievement marker path.
  - Event 006 docs icon ledger entry for the Kurdish idea sprite.
- `chaosx_icon_artist` created the Kurdish Mountain Assembly idea icon package:
  - source PNG
  - processed PNG
  - final DDS
  - prompt
  - manifest and GFX handoff entries
  - asset handoff `2026_06_01_event006_kurdish_mountain_idea_icon_handoff.md`

## Validation

- Brace balance and trailing whitespace passed on:
  - `common/decisions/006_independence_wave_decisions.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/ideas/006_independence_wave_ideas.txt`
  - `interface/006_independence_wave_icons.gfx`
  - `localisation/english/006_independence_wave_l_english.yml`
  - relevant handoff markdown files
- `rg -n "<=|>="` returned no matches on touched Event 006 script/GFX files.
- Mechanical reference checks passed:
  - no missing decision/focus icon sprites against `interface/006_independence_wave_icons.gfx`
  - no missing idea sprites for Event 006 idea `picture =` tokens
  - no missing localisation keys for checked Event 006 decision, focus, and idea ids
- DDS validation from the icon subagent reports `idea_independence_wave_kurdish_mountain_assembly.dds` as `68 x 68`, ARGB8888.

## Commit Status

No commit was created. The repository already has a broad dirty worktree with many untracked Event 006 files and unrelated Event 005 modifications; committing this narrow pass safely would require first separating prior untracked Event 006 work from this tranche.

## Remaining Gaps

- Event 006 remains incomplete as a full source-spec pack.
- Starter packages are coherent overlays, not complete bespoke country packages.
- Railway/Timetable Authority remains generic and still needs deeper tag-specific route design before it can be treated as a full railway country family.
- No flag artwork follow-up is required from this pass.
