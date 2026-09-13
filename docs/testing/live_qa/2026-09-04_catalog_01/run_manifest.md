# Chaos Redux catalog playtest â€” 2026-09-04

Status: launch 07 passed the former native crash after schema repair; later startup errors remain and no live feature case has passed.

The user authorized launching and controlling HOI4, inspecting fresh logs and dedicated saves, repairing confirmed defects, relaunching, and testing across separate saves and countries.
The user requires a clean, crash-free main menu before campaign testing.
Major GUI and focus redesigns require an observation-backed plan rather than implementation during this run.

- Initial branch: `master`.
- Initial HEAD: `b0093d361f0cb63d498d0a499ff5d0f051fe2cb9`.
- Initial worktree/index inventory: `baseline_git_status.txt` (5,165 entries; preserve concurrent work).
- Mode: catalog coverage, beginning with shared-system smoke tests and 29 catalog events marked `Needs Testing`.
- Initial harness: USA, fresh 1936 non-Ironman; separate dedicated saves for country-specific and mutually exclusive paths.
- Launch target: `C:/Users/klimp/OneDrive/Desktop/hoi4.exe - Shortcut.lnk`.
- Candidate logs: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/logs`; active location requires post-launch freshness verification.
- Baseline log metadata and hashes: `baseline_logs.json`; copies: `logs/baseline/`.
- Teaser destination: `docs/content_dump/2026-09-04_catalog_01/`; admit only verified Chaos Redux feature captures and descriptions.
- QA screenshots, including main-menu proof and bug evidence: this run's `screenshots/`, outside the teaser destination.
- Bug report and repair history: `repair_ledger.md`, outside the teaser destination.
- Dedicated saves: none created yet.
- Launched PIDs: 3736 (launch 01) and 32932 (launch 02); both exited in confirmed crashes.

## Workflow and references

The parent read `chaos-redux-debug-playtest`, Computer Use initialization, guidance, API and confirmation rules, and `chaos-redux-subagents`.
The offline core wiki pages and troubleshooting page were consulted; installed console documentation was opened.
Owning skills and installed engine documentation will be consulted for each actual patch surface.
The playtest skill's missing generic reading reference was sent to the skill maintainer for narrow recovery or correction before launch.
Windows application enumeration through `@oai/sky` succeeded.
Events 21â€“39 and the mechanics guide contain concurrent edits; inspect exact current diffs and preserve other owners' work before every patch.

## Updated ownership constraint

The user clarified that active development is limited to events 6, 12, 16 and 23.
Preserve their concurrent edits and restrict any necessary changes there to isolated safe fixes.
Other event work is stopped and confirmed errors may be repaired within the existing design.
Desktop control remains suspended until startup crashes and errors are resolved.

## Additional user requirements

Use the Chaos Redux test country (CXT) where it makes test setup easier, following its documented setup contract.
After startup repairs and the initial playtest work, inventory every current Chaos Redux 3D unit and record each in game.
Record exact unit/entity identifiers, visible actions covered, video path and descriptive caption, and report missing or blocked cases honestly.
This is an additional full-coverage media requirement, not a replacement for event/system testing or mechanics-guide updates.

## Historical blocked checkpoint (superseded)

Startup remains blocked on the unanswered request to apply `repression_parser_fix.patch` directly after the required production rewrite rolled it back.
That same dependency persisted through three goal turns; independent comparison/mission fixes, the recording inventory and the skill note were completed while waiting.
No successful main-menu launch, live feature test, save or teaser recording is claimed.
After approval, recheck current source identity and preserve concurrent changes, apply only the reviewed 14-element repair, then launch through the existing shortcut and inspect fresh startup logs before computer control.
Review `unit_recording_inventory.md` and `shared_system_coverage.md` after startup is stable.
The full playtest objective remains incomplete.

## User-approved resumption

The user approved direct application and autonomous testing; the updated scripted-GUI skill makes rewriting optional.
The previous blocked status is superseded.
Launch 03 cleared error.log but still crashed; launch 04 is capturing the native exception for diagnosis.
See the latest repair-ledger sections before resuming any pending launch or UI action.

## Historical checkpoint after launch 04

The full exception dump completed and HOI4 and ProcDump have exited.
No main-menu or campaign test has passed; no teaser media has been captured.
The crash evidence worker is analysing the exception context, and the localisation worker owns bounded duplicate-key fixes outside protected event work.
The repaired repression overview has been visually reviewed using the production render and click-region artifacts; runtime acceptance remains pending.
Direct source editing is authorized; there is no outstanding permission request.


## Launch 06 checkpoint

Launches 05 and 06 tested two reversible isolations of the constant object named in the full dump; both reproduced the same native stack with an empty error.log.
Both Event 6 source files are restored byte-for-byte to pre_probe_05 originals; no diagnostic substitution remains.
Six launches have failed before the main menu, reaching the playtest skill's default repair-cycle limit.
The outstanding issue is native constant/schema-path diagnosis beyond the single entry; no safe permanent crash patch has been demonstrated.
Teaser captures, mechanics-guide media replacement, system/event playtests and 3D recordings remain unperformed.


## Active repair checkpoint after launch 07

Schema repair committed as aec2089c1, limited to3 scalar-constant files and schema_startup_repair.md.
Launch 07 progressed beyond the former native failure but produced later startup errors; its recorded PID22276 was stopped for repair with no campaign entered.
Uncommitted parent repairs include531 source-matched effect-keyword corrections in10 files and107 file-local mastery amount corrections in027_doctrine_research_exact_mastery_effects.txt.
Four bounded workers own Event24 definitions/traitrefs, decision parser errors, idea modifiers, and the accepted containment parameter-call repair in3 Event16 files.
The debug-playtest skill's reusable schema-triage note was reviewed and accepted; its other existing edits remain preserved.
No main-menu visual acceptance, clean startup, teaser media, save or campaign feature test is claimed.
Next: review worker handoffs/currentdiffs, finish the safe parser tranche, archive current state and launch through the approved shortcut for fresh-error comparison.



## Current checkpoint after launch 08

Launch 08 started 2026-09-05 10:30:13 local, PID 31608, using the unchanged approved shortcut.
It remained responsive through later startup loading with no new crash directory; the parent stopped this exact process at the error gate and archived all logs under logs/launch_08/logs/.
No visual main-menu or country-map acceptance is claimed.
The final error log has 4,598 lines, compared with 7,559 in launch 07; these counts are diagnostics, not unique bug counts.
Containment parameter cascades, all clear_country_flag errors, repaired idea modifier/constant errors, Event 024 wrapper and digit-leading trait errors, and mastery amount-token errors disappeared.
The 214 doctrine index errors remained, disproving the earlier assumption that they were only cascades from the amount token.
Current follow-up patches include the isolated Event 021 MTTH trigger correction and three independently traced terminal temporary-cleanup deletions; these await launch 09.
Decision parser tranche 2, containment hint constants, doctrine index analysis, missing flag source recovery, and MTTH comparison are delegated with bounded ownership.
All teaser media, mechanics-guide media replacements, catalog/shared-system live tests, saves, and 3D unit recordings remain pending clean startup.
The goal remains active, with autonomous testing authorized and no pending permission request.


## Current checkpoint after launch 09

Launch 09 remained responsive but failed the clean error gate; see launch_09_results.md for preserved logs and exact limits.
The parent stopped verified HOI4 PID 24272 and removed the hash-matching unreferenced doctrine probe after archiving.
The next probe will use nonzero mastery because zero caused InitPostRead failure.
Event 31 direct flag encoding, Event 32 helper structure, remaining documented trigger aliases, and Event 39 missing constant declarations are under bounded review.
No campaign, save, teaser screenshot, recording, or mechanics-guide media replacement has been performed.
Events 6, 12, 16, and 23 remain protected from broad edits; only separately justified isolated parser repairs are in scope.

## Launch 10 in progress

Launched through the unchanged supplied shortcut on 2026-09-05 at11:32:14 local time, verified PID24320.
The source snapshot, launch timestamp and probe copy are under logs/launch_10/.
The unreferenced nonzero mastery probe has SHA256 c692315e518f95fe399385b616ad483fe0b079801c2a01bf8b6790db270fd749.
The parent must stop only the verified process, archive the fresh logs, then remove the hash-matching temporary common/scripted_effects/zz_codex_qa_doctrine_index_probe.txt file.
No desktop control or gameplay test has begun.

## Current checkpoint after launch 11

Launches 10 and 11 were stopped at the error gate and their logs archived; no HOI4 process or temporary parser probe remains.
Launch 11 accepted all107 doctrine track_index fields without their former parser errors; exact-track runtime behavior still needs live validation.
Event32 operations source changed independently during launch11 by exactly the audited missing closing brace.
The parent preserved it, recorded provenance under event32_brace_observed/, and requires a fresh native retest rather than accepting a mixed-source launch for that file.
Seven zero-effect history declarations for the existing Event39 dormant templates await the next loader test.
No campaign, save, teaser capture, guide media replacement, or unit recording has occurred.
The attempted checkpoint-document commit was deferred by an existing shared .git/index.lock; it was not removed.


## Current checkpoint after launch 13

No HOI4 process or disposable doctrine probe remains.
Launch 13 accepted the seven empty dated history declarations and recorded frontend startup completion in 27187ms; other errors keep the clean-start gate pending.
The production doctrine index parser repair and Event32 helper-brace registration are native-verified at the parser level, with runtime semantics and probability binding limitations still recorded.
All shared systems/catalog events, teaser screenshots, recordings, saves, and mechanics-guide media remain pending.
The next tranche should use logs/launch_13/logs/error.log as fresh evidence, prioritizing remaining invalid triggers, missing constants, and individually traced cleanup calls.
Events 6, 12, 16, and 23 remain protected from broad edits.
No broad redesign or gameplay fallback was introduced.

## Commit and handoff checkpoint

The empty .git/index.lock dated10:56:30 was removed only after it was over an hour old, no Git process was running, and an exclusive file open succeeded.
Commits:763094b1b registers only the seven task-created inert history inputs plus their native-validation report; c6eb611fb records launches9–13; 037f56c28 commits23 task-owned playtest skill guidance lines.
The unrelated pre-existing generic-skill reference deletion remains unstaged.
Other gameplay repairs in larger concurrently developed or untracked feature files remain preserved in the worktree with immediate backups; they were not swept into these commits.
All bounded subagent work for this tranche has returned.
No permission is pending, the comprehensive goal remains active, and the next fresh-error source is logs/launch_13/logs/error.log.

## Launch 14 checkpoint

Launch 14 reached engine frontend startup completion and cleared all targeted diagnostics from the preceding repair tranche.
The error log remains nonempty; normalized distinct lines decreased from 746 to 721, with only reload bookkeeping newly present.
Eight tracked sources stayed unchanged; Event 32 operations changed independently and has no controlled whole-file acceptance from this launch.
See launch_14_results.md for exact hashes, comparison evidence, targeted repair limits, and source-snapshot provenance.
No campaign or feature-media coverage has begun, and the clean-start gate remains pending.

## Launch 15 checkpoint

Launch 15 completed engine startup in 74473ms, then was stopped at the nonempty-error gate.
Nine repaired sources remained unchanged; Event 32 operations changed independently and its actual before/after bytes are archived.
Political-power aliases, two Event 28 reserve aliases, the Event 26 refund marker, and three Event 35 cleanup calls cleared their targeted diagnostics.
Acid Rain mission cleanup exposed two missing legacy mission IDs; these require correction before that repair can be accepted.
See launch_15_results.md and logs/launch_15/ for evidence and limits.
All campaign and feature-media coverage remains untested.

## Launch 16 checkpoint

Launch 16 completed engine startup in 58391ms, remained responsive, and was stopped at the nonempty-error gate.
The stale Acid Rain mission diagnostics and two Great Depression adapter cleanup diagnostics are absent; all four captured sources stayed unchanged.
Normalized distinct diagnostic lines decreased to 697, with no new family beyond an aggregate count.
See launch_16_results.md for exact evidence and runtime limits.
Current fresh native error source is logs/launch_16/logs/error.log; no HOI4 process remains.
Feature coverage, saves, teasers, all custom-unit recordings, and mechanics-guide media remain pending.

## Launch 17 checkpoint

Launch 17 completed engine startup in 117464ms and was stopped at the nonempty-error gate.
All fifteen targeted country-check corrections are parser-accepted, with ten tracked sources unchanged and no new diagnostic family beyond the aggregate count.
Normalized distinct lines are 683; fresh evidence is logs/launch_17/logs/error.log.
Event32 command-power and Event39 custom-pool probability limitations remain unresolved; no numerical probability pass is claimed.
Event24 foreign-event ROOT identity concern is recorded in launch_17_results.md and its handoff for follow-up.
Pending six Event32 core cleanup removals and 32 infrastructure comparisons were held until this launch ended.
No feature-media or campaign coverage has started.

## Launch 18 checkpoint

Launch 18 completed engine startup in 100042ms and was stopped at the nonempty-error gate; no HOI4 process remains.
Thirty-two registry infrastructure comparisons and six Event 32 core cleanup calls cleared their exact parser diagnostics.
All four tracked files stayed unchanged during launch; the current error log has 1940 lines and 678 normalized distinct lines.
See launch_18_results.md and logs/launch_18/ for full source/log evidence and runtime limits.
The next fresh-error source is logs/launch_18/logs/error.log.
No campaign, save, feature-media capture, guide media update, or custom-unit recording has occurred.
MCP probability reports remain partial where eligibility/resource/helper inputs cannot bind; no numerical acceptance is claimed.
Launch17 checkpoint commit was deferred by a shared index.lock created at12:55:11 while other Git processes were observed; it was preserved.
Completed checkpoint commits this tranche:6f0f3cddf (launch14),3681c41c9 (launch15),302e73478 (launch16).

## Launch 19 checkpoint

Launch19 completed frontend startup in78467ms without a crash and was stopped at the nonempty-error gate.
Seven tracked sources stayed unchanged, with1758 error lines remaining.
Five infrastructure comparisons, twelve building comparisons, twelve literal damage-field substitutions, and25 proven cleanup deletions cleared their targeted diagnostics.
See launch_19_results.md and logs/launch_19/ for the current native evidence.
No campaign or feature-media coverage has started; the comprehensive goal remains active.

Launch17–19 checkpoint commits remain deferred: the shared index.lock created at12:55:11 remains present, with other Git processes observed at13:41:45.
The lock is preserved; no source or checkpoint file was swept into an unrelated commit.
