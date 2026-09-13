# Focus and decision skill cleanup handoff

Disposition: `implemented` for the bounded documentation cleanup; the contradictions listed below remain `unresolved`.
Acceptance basis: the parent assigned review and concise organization of these exact skills and Markdown templates under the user's preservation requirement, with executable templates, schemas, YAML, gameplay, external operations, child agents, and commits excluded.
This handoff includes the retained earlier focus edits and this worker's changes against the saved original, including user changes already present in that original.
The parent owns final review and the task commit.

## Scope and reading inventory

The editable surfaces were `.agents/skills/chaos-redux-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and the five Markdown files in `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/`.
The saved original is `C:/Users/klimp/.codex/tmp/chaos-redux-skill-cleanup-20260913/original/.agents/skills/`.
The focus original and current skill were read in complete bounded ranges.
The decision skill and all five template Markdown files were read fully; before editing, their current bytes matched the saved original, so those reads covered both versions' complete content.
The complete current template code was read: `formable_state_puzzle.gui`, `formable_state_puzzle.gfx`, `formable_state_puzzle_scripted_gui.txt`, `formable_state_puzzle_scripted_triggers.txt`, `formable_state_puzzle_scripted_effects.txt`, `formable_state_puzzle_scripted_localisation.txt`, `formable_state_puzzle_localisation.example.yml`, `state_manifest.schema.json`, and `state_manifest.example.json`.
Those non-Markdown templates are absent from the saved original snapshot; no comparison against a nonexistent original is claimed, and this worker did not edit them.
The current universal `docs/formables/state_registry/consumer_spec.schema.json` and `consumer_spec.template.json` were also read completely to interpret the migration guidance and identify the unresolved example palette mismatch.

Repository authority was read from the supplied `AGENTS.md` instructions and the current source; exact current ownership passages were checked at `AGENTS.md:105`, `AGENTS.md:114`, and `AGENTS.md:324`.
The complete `chaos-redux-subagents/SKILL.md` and official `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md` were read.
Oversized combined initial tool outputs were not used as complete reading evidence: missing material was recovered through bounded reads, or verified byte-identical content for the original/current Markdown pair.

Offline wiki consultation covered the eleven required core pages plus National focus modding, Interface modding, and Scripted GUI modding.
The decision category attachment and picture sections and scripted-GUI dirty-variable and event-target warnings were checked directly.
No web Paradox wiki was used.
Relevant installed vanilla documentation consulted directly was `common/decisions/_documentation.md`, `common/scripted_guis/_documentation.md`, `common/focus_inlay_windows/documentation.md`, and the Script Constants section of `documentation/script_concept_documentation.md`.
Vanilla precedents inspected were `common/decisions/categories/AUS_decision_categories.txt` and prerequisite examples in `common/national_focus/austria.txt`.
The guessed `common/focus_tree_navigation/` directory does not exist in this installation; no navigation syntax was inferred or changed.
Large unrelated vanilla documentation databases, archived producers, the runtime generator implementation, generated registry binaries/data, and runtime consumer artifacts were not exhaustively read or run because this task changed documentation hierarchy and ownership wording only.

## Per-file disposition and changes

| File | Disposition | Changes and retained scope |
| --- | --- | --- |
| `chaos-redux-focus-trees/SKILL.md` | `implemented` | Retained the preflight/prerequisite move ahead of design guidance, nested existing numbered subsections and their children, moved animated portrait guidance under localisation/icons, and retained the five safe wording changes listed below. Moved `AGENTS.md` reading to the start of preflight so repository authority precedes system checks. |
| `chaos-redux-decisions-missions/SKILL.md` | `implemented` | Nested `4.1` under dynamic values and `15.1`–`15.7` under focus/decision integration. Added the missing coordinating `or` between the existing three alternatives for weak reward families. |
| `templates/formable_state_puzzle/README.md` | `implemented` | Corrected only the two live-validation ownership claims using explicit repository authority. All nine setup steps, ten non-negotiable contracts, helper rows, migration steps, references, and dependencies remain. |
| `templates/formable_state_puzzle/static_category_picture_option.md` | `implemented` | Moved the existing rejection conditions directly after the selection gate as its subsection. Every condition, owner-record field, explanation, and both fenced snippets remains. |
| `templates/formable_state_puzzle/universal_state_registry_workflow.md` | `implemented` review, unchanged | Preserved every maintenance step, source boundary, restoration/review condition, runtime restriction, evidence gate, command, and handoff requirement. |
| `templates/formable_state_puzzle/category_attachment_audit.md` | `implemented` review, unchanged | Preserved strict-policy scope, crosswalk, seven audit steps, failure conditions, and completion gate. |
| `templates/formable_state_puzzle/validation_checklist.md` | `implemented` review, unchanged | Preserved every checklist item and its conditions, including optional variable refresh/cleanup, provenance, AI, geometry, GUI/map MCP, DDS, and exact blocker reporting. |

No requirements were removed or merged, including cross-file repetition.
Repeated baseline, audit, and completion statements serve different workflow stages; they were retained rather than assumed redundant.
All frontmatter, inline technical literals, code fences, commands, identifiers, paths, values, examples, dependency names, qualification conditions, exceptions, and requirement strengths remain, apart from the two expressly evidenced ownership corrections.
The separate animation paragraphs were retained: the asset section covers production ownership and identity assignment, while improvement guidance also requires a clear trigger and cleanup state.
Model prose was not changed, and no agents were spawned.

### Safe wording changes

| Original wording | Revised wording | Preservation basis |
| --- | --- | --- |
| `A focus tree defines the playable identity of a country.` | `A focus tree defines a country's playable identity.` | Same country identity subject and design purpose; the following reward sentence is exact. |
| `A real branch should usually include:` | `A real branch should usually have:` | Same recommendation strength and unchanged complete requirement list. |
| `A focus reward should usually do at least one of these things:` | `A focus reward should usually do at least one of these:` | Removed only `things`; threshold, strength, and list are exact. |
| `For large focus-tree work, update documentation.` | `Update documentation for large focus-tree work.` | Same imperative and task scope. |
| The decision reward alternatives ended `convert them into staged idea upgrades, make them change a visible mechanic value.` | The same alternatives end `convert them into staged idea upgrades, or make them change a visible mechanic value.` | Added conjunction for the existing alternatives without adding or deleting an alternative. |

### Evidenced authority corrections

README setup step 9 formerly said the parent owned runtime wiring, final source review, and live-consumer validation.
It retains parent ownership of runtime wiring and final source review and assigns live-consumer validation to the user.
README Ownership boundaries formerly assigned final in-game acceptance to the event/system owner; it retains all source/design/integration responsibilities and assigns final in-game acceptance to the user.
The explicit basis is `AGENTS.md:105` and `AGENTS.md:324`, which assign live-game/live-consumer validation to the user and forbid agents from launching HOI4 for it, corroborated by `chaos-redux-subagents/SKILL.md:10` and its UI ownership gate.
These corrections do not delegate source/MCP validation or final completion claims to the user.

## Unresolved contradictions and decisions needed

The following passages remain intact; none was silently reconciled through a weaker rule or a template-code change.

| Exact location | Conflict or uncertainty | Decision needed |
| --- | --- | --- |
| `README.md:76`–`README.md:81`, helper refresh row at `README.md:106`, and migration step 5 at `README.md:125` | Setup step 6 and the checklist support live trigger counting and an optional variable refresh path, but the migration step says to add the bounded refresh effect unconditionally, and its helper row lists required call sites without that condition. The scripted-GUI template also declares a dirty variable while direct count localisation is live. | Confirm whether migration step 5 and the helper row apply only to the verified variable/dirty path, and whether the copied GUI must adapt dirty gating for the live-trigger path. |
| `formable_state_puzzle_scripted_localisation.txt:203`, `:272`, `:339`, compared with its generic control result at `:65` and shared trigger template | Fixed-entry `control_result` tests full qualification, which includes ownership and core status in the sample helper; it can report “Not controlled” for a controlled non-core state. The generic path tests control separately. README hover guidance requires distinct factual control and core results. | Approve a separately scoped template-code repair that distinguishes factual control from full eligibility and supports the declared owner/subject/ally policy. Code remains unchanged here. |
| `formable_state_puzzle_localisation.example.yml:3` and `:11` versus README player-text restrictions and the skill's localisation requirements | The category description mentions installed-map implementation and the requirement tooltip exposes a helper name and trigger mechanics. The supplied YAML also uses indented keys, contrary to repository localisation style. | Decide a bounded YAML/template repair with owner-neutral player wording and the required encoding/style; YAML was expressly excluded here. |
| `category_attachment_audit.md:24` versus `universal_state_registry_workflow.md:9` and README registry migration rules | Audit step 2 says the consumer manifest contains exact installed-map geometry, while the registry workflow forbids copying registry geometry into a second owner manifest. A manifest reference/hash may be intended, but that intent is not explicit in the audit wording. | Confirm whether the audit should resolve geometry through the canonical registry and recorded provenance rather than require embedded geometry. |
| `README.md:139`, `universal_state_registry_workflow.md:111`, and its supported maintenance/restoration sections | Handoff requirements still list builder `--check` and compiler results although existing consumers are reviewed artifacts and archived producers are not routine commands. Historical evidence versus fresh restoration evidence is not distinguished. | Specify acceptable historical/reuse evidence and which results are required only for an approved restoration/new-consumer migration. |
| `consumer_spec.template.json:35` versus README contract 3 and validation checklist unresolved-state palette | The universal consumer example's unresolved RGBA is ochre (`190, 150, 40, 230`), while the copied package's contract requires grey unresolved pieces with hatch/non-colour cues. | Decide whether to repair the example palette or explicitly distinguish consumer modes through a separately authorized JSON/example change. |
| Focus skill section 13, paragraphs beginning `Only load or replace` and `Existing countries` | The first statement permits runtime tree loading/replacement only for event-created countries; the next permits blind replacement with explicit design support. The scope/exception relationship is not explicit. | Confirm whether explicit design support is an exception for existing-country replacement, and the exact event/general scope. |
| Decision skill `Formable state-puzzle presentation standard` at `SKILL.md:749` versus completion item at `SKILL.md:981`, and README Selection gate/strict attachment policy | The main standard is unconditional when exact control is central; completion allows a documented static picture, while the template supplies four narrow static gates and a strict family policy that disallows the alternative. | Confirm the intended precedence and exception scope before tightening or adding an explicit cross-reference to that exception. Existing specific gates and strict policy remain loaded by required reading and intact. |
No current gameplay, focus, decision, GUI, map, technology, asset, sound, or weighted-logic surface was edited.
Runtime MCP operations and game testing therefore were not run for this skill-only task; the existing skill/template requirements for future implementation remain unchanged.

## Verification and limits

Both skills pass the official skill-creator validator.
The default Windows Python encoding initially failed to decode the decision skill's existing Unicode prose; rerunning the validator with `python -X utf8` passed without changing file contents.
Every relative Markdown link and fragment in the owned Markdown files resolves against the current linked Markdown resources.
Numbered subsection hierarchy is nested consistently, and the setup/migration/audit step sequences remain exact.
The two focus prerequisite fences and both static-picture fences retain exact raw bytes against the saved original; all other owned files retain their complete original fence inventories.
Skill frontmatter bytes and inline technical-literal multisets match the saved original.
The exhaustive line map below accounts for every nonblank original line, detects any unmatched revised instruction, and records exact moves, hierarchy changes, safe wording, and authority corrections.
Mechanical line mapping supports the detailed review; it is not behavioral engine validation.
No simplifications were introduced in this cleanup.
The unresolved conflicts above remain pending rather than counted as resolved work.

Skills used: official `skill-creator`, `chaos-redux-subagents`, `chaos-redux-focus-trees`, and `chaos-redux-decisions-missions`.
No skills were created, and no code templates, schemas, YAML, runtime scripts, model prose, or outside worker-owned repository files were changed.
## Exhaustive original-to-revised line map

Every nonblank original line is mapped below.
An exact range maps each original line to the corresponding revised line in order; heading-only rows preserve the title and change only hierarchy.
Empty separator lines carry no instructions and are excluded.
The named safe wording substitutions and two authority corrections are the only non-exact prose mappings.
No passage was deleted or merged.
Line numbers refer to the saved original and the final files at handoff time.

### `.agents/skills/chaos-redux-focus-trees/SKILL.md`

Original SHA-256: `ab356ca55842c75c4784b89a7223652f7894b467605d74439c2f8eaf5a6c6301`.
Revised SHA-256: `74805c1f8522ee8630912fd8946c6d547fd43d61e4a907fc71ba08a803253d3f`.
All 1088 nonblank original lines mapped; 2 fenced blocks retain exact bytes.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–18 | 1–18 | exact |
| 21–64 | 55–98 | exact |
| 66–68 | 21–23 | exact |
| 70–75 | 26–31 | exact |
| 76 | 25 | exact |
| 77–98 | 32–53 | exact |
| 100 | 100 | exact |
| 102 | 102 | safe wording |
| 104–154 | 104–154 | exact |
| 157 | 157 | heading hierarchy |
| 159–192 | 159–192 | exact |
| 195 | 195 | heading hierarchy |
| 197–224 | 197–224 | exact |
| 226 | 226 | heading hierarchy |
| 228–239 | 228–239 | exact |
| 241 | 241 | heading hierarchy |
| 243–256 | 243–256 | exact |
| 258 | 258 | heading hierarchy |
| 260–274 | 260–274 | exact |
| 276 | 276 | heading hierarchy |
| 278–320 | 278–320 | exact |
| 322 | 322 | heading hierarchy |
| 324–344 | 324–344 | exact |
| 346 | 346 | heading hierarchy |
| 348–360 | 348–360 | exact |
| 362 | 362 | heading hierarchy |
| 364–387 | 364–387 | exact |
| 390 | 390 | heading hierarchy |
| 392 | 392 | exact |
| 394 | 394 | safe wording |
| 396–404 | 396–404 | exact |
| 406 | 406 | heading hierarchy |
| 408–414 | 408–414 | exact |
| 416 | 416 | heading hierarchy |
| 418–433 | 418–433 | exact |
| 435 | 435 | heading hierarchy |
| 437–464 | 437–464 | exact |
| 466 | 466 | heading hierarchy |
| 468–477 | 468–477 | exact |
| 480 | 480 | heading hierarchy |
| 482–496 | 482–496 | exact |
| 499 | 499 | heading hierarchy |
| 501–511 | 501–511 | exact |
| 513 | 513 | heading hierarchy |
| 515–530 | 515–530 | exact |
| 532 | 532 | heading hierarchy |
| 534–557 | 534–557 | exact |
| 559 | 559 | heading hierarchy |
| 561–567 | 561–567 | exact |
| 569 | 569 | heading hierarchy |
| 571–583 | 571–583 | exact |
| 586 | 586 | heading hierarchy |
| 588–617 | 588–617 | exact |
| 620 | 620 | heading hierarchy |
| 622–656 | 622–656 | exact |
| 659 | 659 | heading hierarchy |
| 661–679 | 661–679 | exact |
| 682 | 682 | heading hierarchy |
| 684–732 | 684–732 | exact |
| 735 | 735 | heading hierarchy |
| 737–803 | 737–803 | exact |
| 806 | 806 | heading hierarchy |
| 808–824 | 808–824 | exact |
| 826 | 826 | heading hierarchy |
| 828–930 | 828–930 | exact |
| 932 | 932 | safe wording |
| 934–1041 | 934–1041 | exact |
| 1043 | 1043 | heading hierarchy |
| 1045–1060 | 1045–1060 | exact |
| 1062 | 1062 | heading hierarchy |
| 1064–1087 | 1064–1087 | exact |
| 1089 | 1089 | heading hierarchy |
| 1091–1110 | 1091–1110 | exact |
| 1112 | 1286 | heading hierarchy |
| 1114–1118 | 1288–1292 | exact |
| 1120–1292 | 1112–1284 | exact |
| 1294–1312 | 1294–1312 | exact |
| 1314 | 1314 | safe wording |
| 1316–1505 | 1316–1505 | exact |

### `.agents/skills/chaos-redux-decisions-missions/SKILL.md`

Original SHA-256: `d919392397a3151d2640d562615afb9110c4d909a079ab591337a97bb5745456`.
Revised SHA-256: `a49aab722eb3fa798d7d577b162e3e49689bfb31a0d65603c0e86eacd472bb01`.
All 698 nonblank original lines mapped; 0 fenced blocks retain exact bytes.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–116 | 1–116 | exact |
| 118 | 118 | heading hierarchy |
| 120–132 | 120–132 | exact |
| 134 | 134 | safe wording |
| 136–486 | 136–486 | exact |
| 489 | 489 | heading hierarchy |
| 491–516 | 491–516 | exact |
| 519 | 519 | heading hierarchy |
| 521–541 | 521–541 | exact |
| 544 | 544 | heading hierarchy |
| 546–558 | 546–558 | exact |
| 561 | 561 | heading hierarchy |
| 563–587 | 563–587 | exact |
| 590 | 590 | heading hierarchy |
| 592–602 | 592–602 | exact |
| 605 | 605 | heading hierarchy |
| 607–631 | 607–631 | exact |
| 634 | 634 | heading hierarchy |
| 636–1014 | 636–1014 | exact |

### `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/category_attachment_audit.md`

Original SHA-256: `39d2e430d9d0fbce91e441c72a26e90a61bef7faaefb79ce1c39bfa99871da8a`.
Revised SHA-256: `39d2e430d9d0fbce91e441c72a26e90a61bef7faaefb79ce1c39bfa99871da8a`.
All 21 nonblank original lines mapped; 0 fenced blocks retain exact bytes.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–33 | 1–33 | exact |

### `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/README.md`

Original SHA-256: `275a605ff8b640a2263ce60c7caa8c934ae05a1bb429ec35ee4a760e7a47ef4f`.
Revised SHA-256: `f5dcf60ff3f11ec15caa46942e880e11f55bd879a4ccbc8146135d1877ec2dbe`.
All 91 nonblank original lines mapped; 0 fenced blocks retain exact bytes.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–93 | 1–93 | exact |
| 95 | 95 | authority correction |
| 97–128 | 97–128 | exact |
| 130 | 130 | authority correction |
| 132–139 | 132–139 | exact |

### `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/static_category_picture_option.md`

Original SHA-256: `72e21690d6305df709364ff6c918be5ac784eced9913e1204c6920eadde4d772`.
Revised SHA-256: `e42dbf180b098a996f401f58fe5882ffcc3aa11609fe5fb3b76e9155975590ff`.
All 51 nonblank original lines mapped; 2 fenced blocks retain exact bytes.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–14 | 1–14 | exact |
| 16–68 | 20–72 | exact |
| 70 | 16 | heading hierarchy |
| 72 | 18 | exact |

### `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/universal_state_registry_workflow.md`

Original SHA-256: `faefd6cecdbeed5bbabcabec688a0917f55b0dba73d203d9879d676a2896be91`.
Revised SHA-256: `faefd6cecdbeed5bbabcabec688a0917f55b0dba73d203d9879d676a2896be91`.
All 59 nonblank original lines mapped; 1 fenced blocks retain exact bytes.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–113 | 1–113 | exact |

### `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/validation_checklist.md`

Original SHA-256: `5d30aea98e16a8a9c1b6b43249b6103cd41727a24f2060fdf96f21a18f9012ba`.
Revised SHA-256: `5d30aea98e16a8a9c1b6b43249b6103cd41727a24f2060fdf96f21a18f9012ba`.
All 57 nonblank original lines mapped; 0 fenced blocks retain exact bytes.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–72 | 1–72 | exact |
