# Event 013 localisation audit handoff

Date: 2026-07-01

Scope:
- `localisation/english/013_natural_disasters_l_english.yml`
- `localisation/english/046_great_earthquake_l_english.yml`
- `localisation/english/099_desert_storm_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- Event 013 scripted localisation and direct report/news call sites as needed for key coverage

Workspace note:
- The worktree was already dirty. This pass did not revert, normalize, or stage unrelated changes.
- The Event 013 localisation file already contained parent edits before this pass, including the new `chaosx.nr13.209.d` key and several office-language removals. The changes below list only this subagent pass.

## Findings

Missing key list:
- None found for the checked Event 013 direct report, report option, direct/no-log report, news, Natural Disaster family, scripted localisation, Event 046 placeholder, Event 099 placeholder, and Event 013 achievement surfaces.

Duplicate key list:
- None found among the scoped localisation files checked.

Scripted localisation issue list:
- No broken Event 013 scripted localisation reference was found in `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`.
- `GetNaturalDisasterStateFamilyName`, `GetNaturalDisasterNewsTitle`, `GetNaturalDisasterNewsDesc`, and `GetNaturalDisasterLatestFamilyLabel` all resolve to keys present in the scoped Event 013 localisation.
- The new direct report text uses `[natural_disaster_direct_report_state.GetName]` and `[natural_disaster_direct_report_state.GetNaturalDisasterStateFamilyName]`, matching the `save_global_event_target_as = natural_disaster_direct_report_state` call before `chaosx.nr13.209`.

Dynamic text opportunities:
- Existing dynamic state and disaster-family text is already used for `chaosx.nr13.201.d` through `chaosx.nr13.209.d` and for the generic disaster news surface.
- No additional dynamic localisation was needed for this narrow text audit.

Cross-surface mismatch notes:
- Event 013 news text mostly describes the specific disaster family that struck.
- One meteor-shower news paragraph still used a government denial frame, which conflicted with the Event 013 writing rules. Patched.
- Event 046 and Event 099 placeholder localisation still used archive/desk-style routing language. Patched to report/disaster wording.
- Achievement name already reads `Ash Winter Watch`, not `Ash Winter Bureau`.

File encoding concerns:
- Scoped localisation files kept UTF-8 BOM after patching.
- No `:0` key version markers were introduced.

Recommended fixes:
- Completed in this pass for:
  - `localisation/english/013_natural_disasters_l_english.yml`, key `chaosx.nr13.news.skyfall.d`
  - `localisation/english/046_great_earthquake_l_english.yml`, keys `chaosx.nr46.1.t`, `chaosx.nr46.1.d`, `chaosx.nr46.1.a`, `chaosx.nr46.2.t`, `chaosx.nr46.2.a`
  - `localisation/english/099_desert_storm_l_english.yml`, keys `chaosx.nr99.1.t`, `chaosx.nr99.2.t`, `chaosx.nr99.2.d`, `chaosx.nr99.2.a`

## Patch

Changed files:
- `localisation/english/013_natural_disasters_l_english.yml`
- `localisation/english/046_great_earthquake_l_english.yml`
- `localisation/english/099_desert_storm_l_english.yml`

Changed keys:
- `chaosx.nr13.news.skyfall.d`
- `chaosx.nr46.1.t`
- `chaosx.nr46.1.d`
- `chaosx.nr46.1.a`
- `chaosx.nr46.2.t`
- `chaosx.nr46.2.a`
- `chaosx.nr99.1.t`
- `chaosx.nr99.2.t`
- `chaosx.nr99.2.d`
- `chaosx.nr99.2.a`

Dynamic localisation added or fixed:
- None. Existing dynamic scope syntax was retained.

Behavior or display before and after:
- `chaosx.nr13.news.skyfall.d`
  - Before: Ended with governments calling the damage local until the next sky report.
  - After: Ends with struck districts, rail crews, and families watching the next sky report.
- Event 046 placeholder
  - Before: Presented as a seismic archive and used archive-close wording.
  - After: Presents as a ground report and says earthquake reports are carried by Natural Disasters.
- Event 099 placeholder
  - Before: Presented as a dust storm archive and used archive-close wording.
  - After: Presents as a dust storm report and says sand and dust storm reports are carried by Natural Disasters.

Why the change is safe and bounded:
- Localisation-only patch.
- No gameplay ids, event ids, triggers, effects, scripted localisation definitions, or UI layouts were changed.
- Event 099 placeholder events are currently hidden, but the stale wording was in the scoped localisation file and was safe to clean while auditing the parent-named files.

Meaningful validation run:
- Checked BOM on the scoped localisation files after patching.
- Checked duplicate localisation keys across the scoped localisation files.
- Checked referenced Event 013/046/099/Natural Disaster keys from the relevant event, decision, achievement, and scripted localisation surfaces against the scoped localisation files.
- Searched scoped Event 013-facing localisation for stale `Ash Winter Bureau`, Natural Disasters office/bureau/desk wording, archive wording, and the removed government denial sentence.

Skipped meaningful validation and why:
- Did not run the game or inspect logs. This was a localisation-only pass and the user requested a repo audit/patch handoff.
- Did not validate unrelated dirty files or unrelated achievement strings outside Event 013 scope.

Unresolved wording decisions:
- None requiring parent input for this narrow pass.
- The larger Event 013 prose surface still contains direct-report and disaster-response language that is serviceable, but a full prose rewrite was out of scope and not performed.

Plan handoff path:
- This file.
