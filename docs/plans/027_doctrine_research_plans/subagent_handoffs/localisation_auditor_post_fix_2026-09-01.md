# Event 027 Doctrine Research localisation audit after wording fixes

Date: 2026-09-01

Mode: read-only audit. This handoff is the only file written. No gameplay, localisation, specification, achievement, GUI, or workbook source was edited.

Status: full localisation acceptance is **not proven**. Mechanical key coverage is strong, but current player-facing text still has one broken scripted-localisation sentence, several specification coverage gaps, raw implementation language, and unresolved ordinary-event overflow evidence.

## Scope and references

Audited the current shared-worktree versions of:

- `events/027_doctrine_research.txt`
- `localisation/english/027_doctrine_research_l_english.yml`
- `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt`
- Event Details, history, and evolution selectors in `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_effects/chaosx_logic_effects.txt`, and `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- Event name and GUI localisation in `localisation/english/chaosx_event_names_l_english.yml` and `localisation/english/chaosx_gui_l_english.yml`
- Event 027 achievements in `common/achievements/chaos_redux_achievements.txt`, `common/scripted_effects/027_doctrine_research_achievement_effects.txt`, and Event 027 localisation
- National Breakthroughs registration, membership, name, and description in `common/script_constants/event_cluster_constants.txt`, `common/scripted_effects/chaosx_event_cluster_effects.txt`, shared scripted localisation, and GUI localisation
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- Every file under `docs/specs/027_doctrine_research_specs/`, with the player-facing contract taken principally from the four numbered specs, acceptance criteria, achievement prompt, catalog/cluster handoff, coding prompt, and review/closure documents

Required offline Paradox wiki localisation and event/decision references and the relevant installed vanilla documentation were consulted. No web Paradox wiki was used and Hearts of Iron IV was not launched.

The audited files were already modified or untracked in the shared worktree. Findings therefore describe the exact current snapshot, not a clean Git revision. Useful snapshot SHA-256 values are:

- `events/027_doctrine_research.txt`: `134FD2AEB6F1C2354D3758A46BBF13CA476FAA5567E52B2B0F4CBA09388FBEF7`
- `localisation/english/027_doctrine_research_l_english.yml`: `BCADE443732B5D38ADD8CE73F0FB1A196ED322DA7821040020A993BE4F6690E9`
- `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt`: `E0434C39C6A2F832F2C1F09B6FAA3B3ED0550A4D1892237CBB3FFEC35E1A05D9`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`: `EC766D3E74E15240BD6E504BF14D8F6F630FE6F1D2FB062AF4F5AF818912B72A`

## Remaining defects

### High: completion summary produces an ungrammatical sentence

`chaosx.nr27.10.d` says `Staff effort was [GetDoctrineResearchConcentrationStatus].` The scripted-localisation function resolves to either `doctrine_research.summary.concentrated` = `all successful choices developed one track` or `doctrine_research.summary.distributed` = `successful choices developed several tracks`.

The resulting sentences are `Staff effort was all successful choices developed one track` and `Staff effort was successful choices developed several tracks`. Both are grammatically broken. Every key and function resolves, so a reference-only check does not catch this defect.

Recommended fix in `localisation/english/027_doctrine_research_l_english.yml`: either make the returned keys predicates that fit `Staff effort was ...`, such as `concentrated in one track` and `distributed across several tracks`, or rewrite the host sentence so the existing clauses fit. Preserve `GetDoctrineResearchConcentrationStatus` and the underlying condition.

### High: the domain menu omits the dynamic summary required by the choice-flow spec

The domain options `chaosx.nr27.3.army`, `.navy`, `.air`, `.special_forces`, and `.chaos_warfare` contain only static domain names. The choice-flow specification requires each domain option to show the active Grand Doctrine or unselected state, valid track count, and whether the next action is Grand Doctrine adoption or subdoctrine mastery.

The page description explains the two possible action types but does not identify which state applies to each option. The player must enter a domain to discover whether it is an adoption or mastery choice.

Recommended fix: add or reuse dynamic scripted-localisation summaries per domain and include them in the option labels or dedicated tooltips. This is a localisation/helper change tied to existing values, not a request for a new mechanic.

### High: the track menu omits the preview required by the choice-flow spec

The `chaosx.nr27.5.*` options only say `Study the ... track`. The specification requires the track-selection option to preview the current subdoctrine, current and next mastery level, completion state, and whether completion reaches the Grand Doctrine Milestone. Those details appear only after the player opens the track page.

Recommended fix: add dynamic track-option tooltips or labels using the existing track, subdoctrine, level, completion, and milestone helpers. Keep the track-page confirmation as the authoritative final preview.

### Medium: the opening report omits the adoption/no-mastery rule required by the spec

`chaosx.nr27.2.d` says a choice can establish a Grand Doctrine or advance a subdoctrine, but it does not state that Grand Doctrine adoption consumes the choice without granting an Event 027 mastery step. That rule is disclosed later on `.4`, after the domain is selected. The choice-flow specification requires it on the opening report.

Recommended fix: add one concise sentence to `.2.d`, for example that establishing a Grand Doctrine spends one choice but grants no subdoctrine mastery step. Do not describe transaction internals.

### Medium: `.12` exposes implementation language

`chaosx.nr27.12.d` uses `verified one-step advance` and `next queued curriculum`; `.12.a.tt` repeats `next queued curriculum`. `Verified` reads like an audit/transaction result, while `queued` exposes the batch queue rather than the current world state. This conflicts with the specification and repository rule against implementation-facing prose.

Recommended fix: say concretely that the selected branch did not advance and no choice was spent, then direct the player to the active curriculum or the next curriculum awaiting review. Preserve `GetDoctrineResearchRemainingChoiceStatus`.

### Medium: Evolution III assigns agency to a doctrine domain

`chaosx.events_log.window.evolution_details.doctrine_research.body.stage_3` says `Established domains can divide those choices among several eligible tracks.` A doctrine domain cannot make or divide choices. The intended actor is the participating country or its staff.

Recommended fix: use a direct subject, for example `Countries with established Grand Doctrines can divide those choices among several eligible tracks.` Update the workbook's Evolution III cell to the same accepted wording.

### Medium risk: track-page descriptions are repetitive telemetry and may overflow the ordinary event popup

The `.60` through `.77` track-page descriptions repeat domain, Grand Doctrine, track, remaining choices, current branch, mastery, next subdoctrine, status, milestone, and confirmation instructions. Most of those facts are required, but the current label-heavy single-paragraph presentation is bloated and repeats information already present in the page title and option text.

Recommended fix: retain every required value while condensing repeated labels and using deliberate localisation line breaks if the normal country-event consumer supports them. Do not remove current/next mastery, completion, milestone, choice cost, or success-only spending information.

The HOI4 Event Viewer produced only a partial structural render and is not a one-to-one country-event popup renderer. Consequently, clipping, poor wrapping, and vertical overflow for these long descriptions are not proven absent. This visual uncertainty blocks full localisation acceptance.

### Low: `.13` is semantically correct but overloaded

`chaosx.nr27.13.d` correctly reports that existing mastery completed the branch during assignment and that no curriculum choice was spent. Its first sentence carries the assigned branch, track, Grand Doctrine, existing mastery, and completion result in one clause chain. It is understandable, but it is denser than necessary.

Recommended fix: split the assignment and completion into two direct sentences while preserving the dynamic subdoctrine, track, Grand Doctrine, and remaining-choice tokens.

## `.12` and `.13` navigation semantics

The current script matches the required behavior structurally:

- Confirmation result `ambiguous` routes from `.7` to `.12`. `.12` spends no choice. If the active-batch flag remains, its option returns to `.2`; otherwise it invokes `doctrine_research_start_next_batch`. This matches the required active-curriculum/next-pending-curriculum recovery, subject to the wording defect above.
- Confirmation result `adoption_only` routes from `.7` to `.13`. `.13` clears the result receipt, spends no Event 027 choice, returns to `.5` when the selected domain still has a valid action, and otherwise routes to `.11`. This matches the required nearest valid track-selection recovery and avoids an unconditional invalid loop.

No navigation-semantic defect was found in these two events. The conclusion is source-structural; runtime interaction was not launched.

## Mechanical localisation audit

### Missing key list

- None among 265 unique direct `title`, `desc`, option `name`, and `custom_effect_tooltip` references parsed from `events/027_doctrine_research.txt`.
- None among the 162 localisation keys returned by Event 027 scripted localisation, including 95 nested `$KEY$` references, when checked against mod English localisation plus installed vanilla English localisation.
- All Event 027 achievement names, descriptions, eligibility tooltip, and happened-condition tooltips are present.
- Event Details premise, five history payloads, four evolution titles, four evolution bodies, Event 027 name mapping, National Breakthroughs name, and National Breakthroughs description are present.

### Duplicate key list

- No duplicate Event 027 localisation keys were found across `localisation/english/**/*.yml` for the Event 027, doctrine-research helper, Event Details/evolution, and Event 027 achievement namespaces.
- The three Event 027 achievement identifiers occur once each in `common/achievements/chaos_redux_achievements.txt`.
- The compatibility `scientific_research` cluster localisation and constant aliases coexist with canonical `national_breakthroughs` keys. They are distinct keys rather than duplicates, and canonical runtime selectors resolve to National Breakthroughs.

### Scripted localisation issue list

- All 119 Event 027 scripted-localisation functions referenced by Event 027 localisation have matching `defined_text` definitions.
- All 119 definitions are used by the audited localisation.
- No unresolved returned localisation key or nested localisation key was found.
- Semantic composition defect remains in `chaosx.nr27.10.d` plus `GetDoctrineResearchConcentrationStatus`, as detailed above.
- Neutral fallback keys such as `Unknown Doctrine Domain`, `Unclassified`, and `No Doctrine Track` prevent raw identifiers from leaking if a selector reaches an unexpected value. Their appearance would still indicate a runtime state problem; this audit did not execute scenarios that force each fallback.

### File encoding concerns

- `localisation/english/027_doctrine_research_l_english.yml`, `localisation/english/chaosx_event_names_l_english.yml`, and `localisation/english/chaosx_gui_l_english.yml` begin with the UTF-8 BOM bytes `EF BB BF`.
- No Event 027 localisation encoding defect was found.
- The XLSX workbook is a ZIP/XML package and is not subject to the YAML BOM rule.

## Event Details, history, evolutions, and workbook consistency

- Event 027 is explicitly actorless in `events_log_set_default_actor_for_current_event`, matching the global-history specification.
- The history payload override records `global.doctrine_research_last_firing_size`, and payload selectors map batch sizes one through five to the five Event 027 history strings, with the Event Details premise as the Event 027 fallback.
- The Event Details preview appends all four Event 027 evolution stages. Shared scripted localisation maps the four stage constants to the four Event 027 titles and bodies.
- In workbook row 27, Event Details and Evolution I through IV exactly match the corresponding localisation values. Evolution V and World-End are empty, as specified.
- Workbook identity fields are aligned: `Doctrine Research`, `Minor Repeatable`, Chaos Tier `1`, cluster ID `9`, and status `Needs Testing`.
- National Breakthroughs workbook row 9 has the same name and description as the canonical GUI localisation and lists members 27, 54, 65, 67, 83, 85, and 89 with severities Medium, Medium, Low, Medium, Low, Medium, and High. Runtime cluster registration gives Event 027 canonical row ID 9001 and Medium severity.
- Cluster Memberships identifies Event 027 as Doctrine Research, Medium, with the note that the selected breakthrough grants each eligible country one doctrine curriculum. This does not incorrectly freeze the evolved choice count.
- The workbook and localisation are consistently affected by the Evolution III prose defect. Exact mirroring therefore does not by itself establish writing acceptance.

## Achievement audit

- `027_doctrine_research_first_lesson`, `027_doctrine_research_single_school`, and `027_doctrine_research_joint_curriculum` are uniquely registered and have direct localisation coverage.
- Their public descriptions and tooltips preserve the specification's same-curriculum, same-domain, five-choice single-branch, and four-distinct-track requirements.
- Eligibility text correctly limits qualification to human-controlled countries without exposing hidden receipt flags or implementation variable names.
- No cross-surface achievement wording contradiction was found.

## Dynamic text opportunities

Required rather than optional:

- Add the specified per-domain dynamic state summary to `.3` options.
- Add the specified current/next/completion/milestone preview to `.5` track options.

Useful but lower priority:

- Consider rendering the `.12` destination as `active curriculum` versus `next curriculum awaiting review` through scripted localisation if the current state can be read safely. The current combined sentence is accurate but exposes the queue abstraction.
- Existing dynamic values for country, stage, batch size, choices remaining, domain, Grand Doctrine, track, subdoctrine, mastery, completion, milestone, and transaction result should be retained.

## Prose-quality issue list

### Vagueness

- `.3` and `.5` options conceal the concrete current state required to choose intelligently.
- `.12` uses `verified` instead of stating plainly that the branch did not advance.

### Bloat

- `.60` through `.77` repeat a long telemetry-style fact list in every track page.
- `.13.d` overloads its opening sentence with assignment and completion details.

### Obvious explanation

- No tooltip was found that merely repeats its title without adding a requirement, cost, or consequence. The confirmation and recovery tooltips generally add useful spending or destination information.

### Repetition

- Track pages repeat domain, Grand Doctrine, and track in the description after those values are already established by navigation and option text.
- The final summary repeats several facts acceptably for recap, but its concentration sentence is currently broken rather than merely repetitive.

### Overcomplication

- `.12` combines two possible navigation destinations through queue terminology.
- `.13` compresses too many relationships into one sentence.

### Style-rule repair still needed

- Remove transaction/audit language `verified` and queue implementation language `queued` from `.12`.
- Correct the agentless Evolution III sentence.
- No em dash or sentence semicolon was found in Event 027 localisation.
- No prompt fragment, tuning history, update-history language, or raw variable/flag identifier was found in the inspected player-facing strings outside the `.12` implementation-language issue.

## Sourced-quotation preservation

No inspected Event 027, Event Details, evolution, achievement, National Breakthroughs, or workbook surface contains a sourced or attributed quotation. There was no quotation text to alter or preserve.

## HOI4 MCP evidence and limits

Read-only MCP routes used:

- Event inspect/lint for `chaosx.nr27.1`: status OK, code `EVENT_INSPECTED_PARTIAL`, no reported lint issue, but `complete: false`.
  - Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3d0db2afc2e45bded1bea38cf286e86d43b5be1b3556e6bdc6d013337c620c0/94d1b4dee5ac4790122fd212e2628e1454785c6bcc6003c9777b27d04b9bddd0/event-lint-b8b928ac6119.json`
- Event option render for `chaosx.nr27.1`: status OK, code `EVENT_RENDERED_PARTIAL`.
  - Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3c208585ba3c4be3eef6cf6d2228297abea24338bfbf7cf3ff458a576b7b1fb/337a4c27d1cc3476a307f11dee815add754946e68858e0bd440005d655801005/event-options-b8b928ac6119-manifest.json`
  - JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb7b72038753f72f9c7aadf28cc3c37e53fc843e8681ab6e1346e8fab2dc3bc7/995237c3ce5ce60018d343c552bef0df71474dad6bfb74c9300f7160479a011c/event-options-b8b928ac6119.json`
  - SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c85b3eeef71e676f62fe448b92a1b8c81b96c213b88f450e39cd0d4fbea6f68e/02bb7821ce2d7e1091e81956ae015b5ec9dbc0283625f5482d369c3697ac1578/event-options-b8b928ac6119.svg`
  - PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4432bd2b7daffd97c1aea724a3582b1c43e0e50520cd1f1716df2fdbc81c58f4/61df270927375ae13129ea67cf070c7ccef98ac10e2cb58d0097baeebdd2aca4/event-options-b8b928ac6119.png`
- Shared Event Details GUI inspect for `events_log_popup_window` with narrow scenario ID `event_027_details`: status OK, code `GUI_INSPECTED`.
  - Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d1235a1c769986e561a0a583a49270975c2ab02af80f95a7e903ff67bd6ee4c/7f004259fa2577e8c8ab5a34d92a4755a9affdd3faa5f40b702658f86f075a98/gui-inspect.9ecf2aec50469dfa.json`
- Shared Event Details GUI render at 1920x1080 and 1366x768 with normal, long-text, and missing-localisation state requests: status OK, code `GUI_RENDERED`.
  - Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8dda658773a6276cf9f498a056dbda020e083ba643da0cc1498e2f35516fd1b2/9618b26c04b7426b27af04bd267e57096f78bb7c2abf88c06f7f243236a4cb5e/events_log_popup_window-full.svg`

Evidence limits:

- The event inspect and event render explicitly report partial coverage. They do not prove the complete `.2` through `.13` and `.60` through `.77` chain under every dynamic state.
- The shared GUI scenario did not supply a live selected Event 027 history/evolution record with resolved runtime arrays. It establishes that the shared window can be inspected and rendered, not that every Event 027 history/evolution payload is visually populated without overflow.
- The installed Event Viewer is structural and does not provide the production one-to-one vanilla country-event popup view. Therefore ordinary-event description and option wrapping, clipping, and overflow remain unverified.
- A Technology Tree Viewer is absent from the installed package as stated by the localisation-agent contract. No technology/doctrine-tree visual acceptance is inferred from source inspection.
- Hearts of Iron IV was not launched, as required.

## Recommended repair order

1. Fix `chaosx.nr27.10.d` and/or `doctrine_research.summary.concentrated` / `.distributed` so both scripted results form grammatical sentences.
2. Implement the specified dynamic summaries for `.3` domain options and `.5` track options.
3. Add the adoption/no-mastery rule to `.2.d`.
4. Replace `verified` and `queued` in `.12.d` and `.12.a.tt` with direct player-facing language.
5. Correct Evolution III in Event Details localisation and the matching workbook cell.
6. Condense and production-render the longest `.60` through `.77` descriptions without deleting required state, cost, or consequence information.
7. Optionally split `.13.d` for first-reading clarity while preserving all dynamic tokens.

## Acceptance conclusion

Direct key coverage, scripted-key resolution, duplicate-key hygiene, UTF-8 BOM, achievement naming, Event Details/history/evolution wiring, workbook mirroring, National Breakthroughs membership, and `.12`/`.13` source navigation are supported by the current evidence.

Full localisation acceptance is **not proven** because the completion summary is visibly broken after scripted substitution, required dynamic option summaries are absent, the opening report omits a specified cost/consequence rule, `.12` exposes implementation terms, Evolution III has an incorrect subject, and production country-event overflow evidence is unavailable.

