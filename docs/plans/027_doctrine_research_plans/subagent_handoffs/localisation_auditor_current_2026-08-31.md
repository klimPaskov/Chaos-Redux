# Event 027 Doctrine Research current localisation audit

## Scope and verdict

This is a bounded read-only audit of the current working-tree Event 027 Doctrine Research localisation after the National Breakthroughs cluster wording patch.

The runtime localisation is mechanically complete at source level and the previous player-facing wording defects are closed. All direct event references resolve, all Event 027 scripted-localisation calls and outputs resolve, the Event Details and evolution selectors point to current text, the debug and settings name is `Doctrine Research`, and the active National Breakthroughs selectors use the new runtime token and wording.

Final localisation completion is not claimed. The standard event popup still lacks one-to-one production visual evidence for the longest track, confirmation, summary, and option strings. The Event Viewer returned a current partial lint and partial options render, but that diagram is not a popup layout render. The shared Event Details GUI produced a production SVG, but the returned response did not prove that the arbitrary Event 027 scenario populated every dynamic Event 027 row and evolution string. Current documentation also retains one stale `Scientific Research` name and stale localisation counts and hashes.

No gameplay, localisation, spreadsheet, or existing documentation file was edited. This handoff is the only file added.

## Sources inspected

The audit compared the user-named runtime files:

- `events/027_doctrine_research.txt`
- `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/027_doctrine_research_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

The debug-name destination was verified in `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:128-130` and `localisation/english/chaosx_event_names_l_english.yml:29` because the requested visible debug-name check cannot be completed from the six named localisation files alone.

All 42 pre-existing Event 027 Markdown files under `docs/events/027_doctrine_research/`, `docs/specs/027_doctrine_research_specs/`, and `docs/plans/027_doctrine_research_plans/` were included in the documentation search. Historical handoffs were treated as dated evidence rather than current source truth.

The required offline localisation and event references were consulted together with installed vanilla localisation formatter and localisation object documentation.

## Current mechanical inventory

| Check | Current result |
| --- | ---: |
| Event 027 English keys | 338 |
| Unique Event 027 English keys | 338 |
| Duplicate keys inside the Event 027 file | 0 |
| Event 027 keys duplicated elsewhere under `localisation/english/` | 0 |
| Unique direct `title`, `desc`, `name`, and `custom_effect_tooltip` references from the event file | 265 |
| Missing direct references | 0 |
| Unique `GetDoctrineResearch*` calls from Event 027 English localisation | 119 |
| `GetDoctrineResearch*` definitions | 119, all unique |
| Missing, duplicate, or unused Event 027 scripted-localisation definitions | 0 |
| Unique scripted-localisation output keys | 162 |
| Outputs resolved in Chaos Redux localisation | 47 |
| Outputs resolved in installed vanilla English localisation | 115 |
| Unresolved outputs | 0 |
| Event 027 event IDs | 31 unique IDs: `.1-.13` and `.60-.77` |

The current Event 027 English file SHA-256 is `30C894D867252F715A8D81EED89458681E9C5856D7ECD04F1ED568AE85CFB923`.

## Missing key list

None.

Every current direct event title, description, option, and tooltip reference resolves. Event Details, five History payload descriptions, four evolution titles, four evolution bodies, evolution type, achievement names, achievement descriptions, achievement tooltips, cluster name and description, settings name, Event Log name, and debug name also resolve.

## Duplicate key list

None in the Event 027 key set.

The compatibility keys `chaosx.event_cluster.scientific_research.name` and `chaosx.events_log.window.cluster_details.description.scientific_research` are distinct aliases, not duplicate YAML keys. They intentionally share visible values with their `national_breakthroughs` successors at `localisation/english/chaosx_gui_l_english.yml:427-428` and `:902-903`.

## Scripted localisation issue list

No missing, duplicate, unused, or unresolved Event 027 scripted-localisation method was found.

The principal selectors are present at `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt:9`, `:19`, `:28`, `:46`, `:65`, `:169`, `:179`, `:186`, `:193`, `:199`, `:205`, and `:211`. The stage selector maps internal stage constants to the player-facing Foundational, Expanded, Advanced, Joint-Service, and Comprehensive keys at `:170-175`. The confirmation and result selectors have explicit adoption, mastery, and fail-closed branches at `:180-182` and `:187-189`.

All 107 option-status methods are one-to-one with their visible option calls. Their complete, Mastery 5 through Mastery 1, selected-at-Mastery-0, and unselected fallbacks resolve to current natural-language state labels at `localisation/english/027_doctrine_research_l_english.yml:332-339`.

## Visible event text findings

The event source exposes 31 Event 027 IDs. Hidden `.1` and `.6` do not require ordinary visible descriptions. The 29 remaining event definitions have the expected visible title, description, option, and tooltip coverage for their actual surfaces.

The previous successful-action gap is closed. `chaosx.nr27.8.d` now reports both the spent choice and the current remaining count at `localisation/english/027_doctrine_research_l_english.yml:247`.

The previous internal-label defect is closed. Adoption confirmation and result text now say that no subdoctrine is advanced at `localisation/english/027_doctrine_research_l_english.yml:292` and `:295`; neither exposes `Event 027 mastery step`.

The opening, domain, Grand Doctrine, track, all 18 subdoctrine pages, confirmation variants, successful result, continuation, completion summary, no-action, suspended-review, and native banked-completion surfaces are specific and mechanically intelligible. Dynamic values use integer formatting where they represent choices or mastery levels.

## Event Details, History, evolution, debug, and achievement wording

Event Details uses the stable one-to-five curriculum premise at `localisation/english/027_doctrine_research_l_english.yml:308`. The five History payload keys at `:309-313` state exactly one through five choices and use the same institutional stage names as the event flow.

The four evolution titles and bodies at `localisation/english/027_doctrine_research_l_english.yml:314-321` agree on Expanded with two choices, Advanced with three, Joint-Service with four, and Comprehensive with five. Their selectors are wired in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:2258-2261` and `:8718-8721`.

History payload routing is present in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5953-5986`, with five size-specific branches before the generic Event Details fallback.

The Event 027 name is `Doctrine Research` at `localisation/english/chaosx_event_names_l_english.yml:29`. Settings routes ID 27 to that key at `common/scripted_localisation/chaosx_scripted_localisation_settings.txt:1760-1761` and `:5761-5762`. Debug routing uses the same key at `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:128-130`. Event Log name routes use it at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:1496-1500`, `:10935-10939`, and `:12723-12727`.

The three achievement names, descriptions, eligibility text, and condition tooltips at `localisation/english/027_doctrine_research_l_english.yml:322-331` are clear and mutually distinct. They state player requirements without exposing receipts, arrays, flags, or hidden achievement implementation.

## National Breakthroughs and stale Scientific Research aliases

The active shared selectors use `constant:event_cluster_id.national_breakthroughs` and current National Breakthroughs localisation at `common/scripted_localisation/chaosx_scripted_localisation_settings.txt:419-422` and `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:584`, `:11754`, `:11894`, `:11996`, `:12094-12095`, and `:12178`.

The current visible name and description are clear at `localisation/english/chaosx_gui_l_english.yml:428` and `:903`: National Breakthroughs gathers repeatable advances in doctrine, production, administration, and other national institutions, with each breakthrough retaining its own conditions and timing. The wording no longer uses the implementation phrase `validates its own owner system`.

Two old localisation aliases remain at `localisation/english/chaosx_gui_l_english.yml:427` and `:902`. They display the new name and description, so they cannot reveal `Scientific Research` to the player. Repository-wide runtime search found no current scripted-localisation selector that calls either old key. Outside the user-named files, `common/script_constants/event_cluster_constants.txt:28-30` explicitly marks `scientific_research` as a compatibility alias, and further old constant members remain at `:130`, `:240-244`, and `:487`. These are compatibility debt, not a current visible localisation failure.

## Cross-surface mismatch notes

One current event document is stale. `docs/events/027_doctrine_research/overview.md:5` still says Event 027 has a membership in `Scientific Research`, while runtime and current player-facing text call the cluster `National Breakthroughs`. The same overview correctly says there are two cluster memberships at `:128`, so the required repair is a name replacement, not a mechanical redesign.

The current evidence ledger is also stale. `docs/plans/027_doctrine_research_plans/mcp_evidence.md:127` calls 341 keys and an older SHA-256 current, while this audit finds 338 keys and SHA-256 `30C894D867252F715A8D81EED89458681E9C5856D7ECD04F1ED568AE85CFB923`. Older localisation handoffs report 333 or 334 keys at `subagent_handoffs/localisation_auditor_final_2026-08-30.md:11` and `subagent_handoffs/localisation_auditor_postfix_2026-08-30.md:35-36`. Those dated handoffs remain useful history, but they must not be cited as current counts.

Historical design specs use `Event 027 mastery step` as an implementation-defined achievement term, for example `docs/specs/027_doctrine_research_specs/027_doctrine_research_achievement_prompt.md:27`, `:68`, and `:107`. This is acceptable inside implementation specifications and does not leak into current player-facing localisation.

No Event Details, History, evolution, achievement, debug-name, or current National Breakthroughs wording mismatch remains in the runtime sources inspected.

## Dynamic text opportunities

No missing dynamic value is required for correctness in the current flow. Choices remaining, batch size, stage, domain, Grand Doctrine, track, subdoctrine, current mastery, maximum mastery, next mastery, completion, Milestone state, successful adoption/mastery totals, distinct domains, and distinct tracks are already dynamic where relevant.

If the event popup render proves that the 18 track descriptions overflow, the safest improvement is one shorter dynamic status selector shared by `.60-.77`. It should preserve all current values while reducing repeated labels. This is a presentation-driven opportunity, not authorization to remove mechanics or dynamic tokens without visual evidence.

## File encoding concerns

No localisation encoding blocker was found.

- `localisation/english/027_doctrine_research_l_english.yml` has UTF-8 BOM and decodes as strict UTF-8.
- `localisation/english/chaosx_gui_l_english.yml` has UTF-8 BOM and decodes as strict UTF-8.
- The three scripted-localisation `.txt` files decode as strict UTF-8. They do not require a localisation BOM.
- The Event 027 English file has one `l_english:` header, 338 parseable one-line keys, no `:0` suffixes, and no leading indentation before keys.

## Prose-quality audit

### Vagueness

No current visible Event 027 sentence leaves the player without the relevant action or consequence. The native banked-completion title `Native Doctrine Progress Resolved` and its description at `localisation/english/027_doctrine_research_l_english.yml:265-268` use specialized doctrine language, but the body explains the assignment, banked mastery completion, unspent choice, and next action. This is understandable in context, though `Native` remains more technical than the rest of the presentation.

### Bloat and overflow risk

All 18 track descriptions at `localisation/english/027_doctrine_research_l_english.yml:62`, `:75`, `:88`, `:100`, `:114`, `:124`, `:136`, `:146`, `:156`, `:166`, `:176`, `:186`, `:197`, `:209`, `:221`, `:226`, `:231`, and `:236` are 658 source characters before dynamic substitution. `doctrine_research.confirm.mastery` at `:293` is 577 characters, `chaosx.nr27.10.d` at `:254` is 543 characters, and the opening at `:4` is 422 characters. These strings carry useful state, but final wrapping, clipping, option displacement, and background containment remain unproved in the standard event popup.

### Obvious explanation

The repeated statements that opening a track or navigating pages does not spend a choice are useful because those are player actions inside a finite curriculum. No tooltip merely repeats its title without adding requirement or consequence information.

### Repetition

The 18 track descriptions intentionally repeat one complete template. This is consistent, but it multiplies any overflow defect across every domain. No accidental sentence-level repetition remains in an individual description.

### Overcomplication

The mastery confirmation and completion summary remain dense because they expose several current-state values. Their information hierarchy is acceptable in source prose, but only a popup render can prove that it remains readable in the consumer.

### Writing-style violations

No em dash, sentence semicolon, staged contrast formula, thesis-antithesis-synthesis structure, staccato chain, update-history phrase, prompt fragment, receipt/ledger/queue explanation, or hidden achievement reveal was found in current Event 027 player-facing localisation. The cluster description is concrete enough for a catalogue summary and no longer uses owner-system jargon.

## Sourced-quotation preservation notes

No sourced or attributed quotation appears in the inspected Event 027 event pages, Event Details, History details, evolution text, cluster text, achievement text, or current event documentation summary. No quotation required preservation and no player-facing text was edited.

## MCP evidence and visual uncertainty

Current Event Viewer lint for selector `{ kind: "event", eventId: "chaosx.nr27.1" }` returned `status: ok`, code `EVENT_INSPECTED_PARTIAL`, workspace `mod_chaos_redux_ea3b2d67c2c0`, and this artifact:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84840ff7eb054dd7b24fb82711b92790a929fdd4e2daa7e3d50c3b46f44573b4/a9e2c0aa717018f1e3271111d6247fbd4644d2d79837f44dc6ad7c1284162fd0/event-lint-2725045f62d1.json`

The current options render returned `status: ok`, code `EVENT_RENDERED_PARTIAL`, and five artifacts. The principal source-linked artifacts are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43e0792c511fa06704e58848c4387d218e24f64cb23c3386cd30c65bdd9baff9/db0b89eb2b6d15305156c79c8c0ffb5e5db3865ad405cddc9009df9780fe84b7/event-options-2725045f62d1-manifest.json`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/209d5abc10ce8f722941d8e2a1e82af9903e7ea885f34a319a2fd258d1159819/f6d7b1bfde2160ea217f6d621cc455ff24e212c06beb7f20316a05ca1ab9ef6e/event-options-2725045f62d1.png`

The shared Event Details GUI inspection for `events_log_event_details_window` returned `GUI_INSPECTED` with:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd8822d1623f3d92a2fc22921388030abae7fe5238be6d2460a17be76488de5f/81a0c688a54c331ccaff1c49069e0b929a6cb2ddef2153e784013c038efda4f4/gui-inspect.da12d8dc1c6ead71.json`

The production GUI render for normal and long-text states at 1920 by 1080 and 1366 by 768 returned `GUI_RENDERED` with:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d835f2aa53451998632fcefc67d3ad11d03c7a155325f316ff2884dc779e8047/c10e4c45a5c46fd7a2c2d34b3a6e8d5ea9378fb75ed20bdfdce71391e1998d14/events_log_event_details_window-full.svg`

The GUI calls returned no blocker in their response. However, the render response exposed only one full-window SVG and did not report which Event 027 dynamic strings were substituted into the shared window. Attempts to read the linked artifact back through the MCP resource route returned no content. The shared GUI render therefore supports source/layout availability but does not close Event 027 text-specific wrapping or overflow by itself.

There is no installed one-to-one standard event-popup renderer in the callable package. The Event Viewer diagram cannot be treated as equivalent to the in-game event popup. Popup overflow remains open for `.60-.77`, `doctrine_research.confirm.mastery`, `.10.d`, and the longest option labels.

The Technology Tree Viewer is absent from the installed package as documented by the parent instructions. No technology or doctrine tree source changed in this wording audit, so no source-accurate technology-tree localisation render exists to add.

## Recommended fixes

1. Replace `Scientific Research` with `National Breakthroughs` at `docs/events/027_doctrine_research/overview.md:5`.
2. Refresh the current localisation count and hash in `docs/plans/027_doctrine_research_plans/mcp_evidence.md:127`, or mark that paragraph as historical rather than current.
3. Retain the two `scientific_research` localisation aliases only while the compatibility constants remain supported. Do not route new selectors through them.
4. Obtain one-to-one standard event-popup evidence for an ordinary long track page, the longest option page, mastery confirmation, and the completion summary before final localisation sign-off. If any string crosses its background, clips, or displaces options, shorten the shared dynamic status presentation without removing values or tokens.
5. If a future wording pass is authorized, consider replacing `Native Doctrine Progress Resolved` with a less technical title while preserving the banked-mastery distinction. This is lower priority than popup evidence and is not a current clarity blocker.

## Meaningful validation performed

- Parsed all 338 current Event 027 English keys and all 265 unique direct event references.
- Compared every direct reference with the current Event 027 key set.
- Compared all 119 `GetDoctrineResearch*` calls with all 119 unique definitions.
- Resolved all 162 scripted-localisation output keys against current Chaos Redux and installed vanilla English localisation.
- Scanned Event 027 keys across `localisation/english/` for duplicates.
- Verified strict UTF-8 and required BOM state for the two English localisation files.
- Checked all Event 027 event IDs and visible title, description, option, and tooltip surfaces.
- Checked Event Details, five History payloads, four evolution stages, settings, Event Log, debug name, achievements, and National Breakthroughs selectors.
- Searched runtime source for `Scientific Research` and `scientific_research` aliases.
- Searched all 42 pre-existing Event 027 Markdown files for stale names, wording, counts, and current-evidence claims.
- Ran current Event Viewer lint and options rendering.
- Ran shared Event Details GUI inspection and production rendering at two resolutions and two text states.

## Skipped or blocked meaningful validation

- One-to-one standard event-popup overflow and wrapping evidence is unavailable because the installed callable package exposes event-chain diagrams, not a production event-popup renderer.
- Event 027-specific dynamic substitution inside the shared Event Details GUI render was not proved by the returned artifact response, and MCP resource readback returned no content.
- Source-accurate Technology Tree Viewer evidence is unavailable because that read-only viewer is absent from the installed package.
- No live game run was performed. Live consumer validation belongs to the user.

## Changed files

- `docs/plans/027_doctrine_research_plans/subagent_handoffs/localisation_auditor_current_2026-08-31.md`

## Final verdict

Source localisation verdict: pass with documentation follow-up. Missing keys, duplicate keys, scripted-localisation resolution, dynamic-value coverage, Event Details wording, History wording, evolution wording, debug naming, achievement wording, National Breakthroughs wording, and encoding all pass in the current working tree.

Final visual localisation verdict: incomplete. Standard event-popup overflow remains unproved, and the Event Details GUI artifact does not prove Event 027-specific dynamic substitution. No broader Event 027 or repository completion claim is made.
