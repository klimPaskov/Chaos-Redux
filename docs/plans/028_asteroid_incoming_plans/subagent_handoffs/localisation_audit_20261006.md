# Event 028 localisation audit

Date: 2026-10-06.
Disposition: unresolved for final presentation acceptance.
Ownership: read-only audit of Event 028 text and source consumers.
This worker changed only this handoff and made no gameplay, localisation, spreadsheet, GUI, or asset changes and no commit.
The parent was editing the shared tree during this review, so findings distinguish initial defects from corrections observed later.

## Source coverage and results

Read the four owned English files under `localisation/english/028*`, `common/scripted_localisation/028_asteroid_incoming_scripted_localisation.txt`, `events/028_asteroid_impact.txt`, the Event 028 decision and category files, and the eight owned news definitions in `events/_chaosx_news.txt`.
The news IDs are 29, 30, 32, 92, 93, 94, 96, and 97.
The ordinary category introduces no event-owned scripted GUI.
The linked shared super-event and Event Details surfaces still require presentation evidence for the assigned text.

- Missing direct localisation keys: none found in title, description, tooltip, custom effect tooltip, custom cost text, or scripted `localization_key` references in the inspected owned sources.
- Missing scripted localisation getters: none found among 42 asteroid getters referenced by owned English text.
- Duplicate keys within owned files: none found.
- Encoding concerns: no concern found in the four owned English files.
- New callback helpers: `asteroid_incoming_deliver_next_news`, `asteroid_incoming_present_impact_super_event`, and `asteroid_incoming_quote_state_recovery_costs` have source definitions in the presentation and recovery effect files.
- Hidden callbacks `chaosx.nr28.10`, `.11`, and `.12` do not need titles or descriptions.
- Scripted localisation syntax issue list: none identified by source review.
- Visible raw flag requirements: none remain in owned decision `available` blocks after excluding `custom_trigger_tooltip` and `hidden_trigger` bodies.
- Custom cost coverage: 16 distinct `custom_cost_text` bases are present, not the 15 stated in the delegation summary, and all 16 have base, `_blocked`, and `_tooltip` keys.
- Runtime scope, selected-branch execution, overflow, wrapping, and visual coverage remain unverified pending MCP presentation results.

## Report and news colour closure

`python .tools/report_colour_audit.py --event 028` reported zero keys with colour.
The full `python .tools/report_colour_audit.py` also exited successfully with zero keys with colour.
The event filter alone is insufficient because the eight news events live in a shared file.
A separate read-only closure walk began from all owned visible event and news titles and descriptions, followed every reached `$key$` reference and every asteroid scripted getter to its possible `localization_key` outputs, and reached 105 distinct localisation keys.
It found no colour glyph and no missing closure key or getter.
This includes the opening board's resolved, locked, and unavailable branches, report opening/toll/damage/capital/transport/next-action families, and the plain fragment news variant.
This proves source closure, not native text fitting.

## Initial defects corrected by the parent during review

The initial `asteroid_incoming_cost_crater_security`, `asteroid_incoming_cost_material_survey`, and `asteroid_incoming_cost_crater_access` values at lines 240, 243, and 246 displayed four resource icons each.
A later source read confirmed three inline icons for each, with omitted command power or civilian factory commitment and its duration retained in the `_tooltip` variants.
All directly referenced custom cost bases have their `_blocked` and `_tooltip` keys.
The parent also replaced internal dust score and threshold language in `chaosx.news.92.d` and `.94.d`, the penalty language in `.93.d`, target-validity language in `.97.d`, and timed restriction and recorded-loss language in `chaosx.nr28.6.d`.
The later values describe thinning dust, restored traffic, withdrawn impact predictions, rescue work, and ruined homes directly.
The parent changed `asteroid_incoming_blocked_state_tt` from recorded damage to impact damage.
No localisation edit listed here was made by this worker.

## Concrete wording findings sent to the parent

Line numbers below refer to `localisation/english/028_asteroid_impact_l_english.yml` and must be refreshed after parent edits.

| Key and observed line | Issue | Recommended parent change |
| --- | --- | --- |
| `asteroid_incoming.event_details.history.fail_closed`, 107 | Implementation prose says the targeting sequence closed and impact effects were not applied. | Keep the title, target tokens, formatting, and line layout. Replace the outcome with `Outcome: The predicted strike was withdrawn. No impact was confirmed.` |
| `asteroid_incoming.site_profile.recon_surveyed`, 195 | Survey records add unnecessary administrative framing. | Preserve the leading space, formatting, and getter. Use ` The site's material is §Y[This.GetAsteroidIncomingCraterSiteProfile]§!.` |
| `chaosx.nr28.5.a.tt`, 45, and `chaosx.nr28.7.a.tt`, 57 | Tooltips merely narrate closing the report. | Remove the redundant custom tooltip calls and keys, or replace them only if closing has a meaningful consequence that the option label does not communicate. |
| `chaosx.nr28.2.d`, 27 | The impact delay is written as two days rather than using its existing tuning source. | Identify the owner-used delay constant and display its value without colour in this parchment description. Preserve target, capital clause, and evolution warning tokens. |
| `asteroid_incoming_reconnect_national_network_mission_desc`, 302 | The opening sentence is filler and the subsequent requirement combines several long conditions. | Lead with the ready date, then use separate complete sentences for rail links, infrastructure share, and the industrial hub requirement. Preserve all conditions and tokens. |
| `asteroid_incoming.mission_failure.local`, 333 | One long chained clause combines deaths, restored damage, reopened emergency, and pressure duration. | Preserve the fact that callers supply a state name before this clause. End the casualty sentence after the cap, then state renewed damage and pressure in separate full sentences, preserving all dynamic values. |
| `decision_asteroid_incoming_survey_extraordinary_material_tt`, 184 | The updated wording still repeats identification and uses singular research bonus after a dynamic use count. | State the material once, then state the exact bonus percentage, research field, and number of uses in a second sentence. Preserve the getter and three dynamic values. |

Prose issue groups: vagueness and implementation framing affect the failed forecast history and survey clause.
Bloat and repetition affect the survey tooltip and mission requirements.
Obvious explanation affects the report acknowledgement tooltips.
Overcomplication affects the network mission and mission failure clause.
No semicolon or em dash violation was identified in the inspected owned English prose.
These recommendations do not change gameplay meaning or invent mechanics.

### Final parent patch status

The parent reports applying the failed forecast history rewrite, direct material wording, dynamic confirmation duration, shorter network mission requirements preserving all state coverage, shorter mission failure clauses preserving all causes and values, and meaningful next-action tooltips for the two report acknowledgements.
These findings are therefore resolved by the parent patch rather than remaining text blockers.
The final source read independently confirmed the dynamic lock duration, both report tooltip replacements, the failed forecast history, direct material clause, shorter network description, and shorter failure clause.
The parent also confirms red blocked cost variants, including the three scripted discount getters, and the full set of 16 native cost triplets.
No unresolved gameplay wording decision is required from the user by this audit.
The unavailable-reason consistency recommendation remains optional parent review of an existing alternate key, not a missing mechanic.

## Dynamic text and consistency

Existing cost quotes, dates, actor/state names, mission targets, material profiles, research fields, and recovery phases provide useful dynamic text.
The hardcoded two-day confirmation text remains an opportunity to reuse the existing delay value.
The unavailable reason `asteroid_incoming.event.na_reason.target_pool` refers to distinct country/state pairs, while the event-log reason at line 3 refers to three countries and surviving controlled territory.
Prefer the latter concrete requirement in both surfaces if the owning eligibility trigger enforces three distinct countries, as the parent task describes.
The short unavailable board prose also repeats that no set of trajectories is available after already explaining the missing targets.
The parent should retain the actual blocked condition and remove that repeated sentence.

Spreadsheet and CSV inspection were excluded by the assigned scope.
No catalogue mismatch is claimed without reading its source workbook.
The spreadsheet owner should mirror the final accepted text of `asteroid_incoming.event_details.description`, `asteroid_incoming.evolution.fragmentation.body`, and `asteroid_incoming.evolution.minerals.body` if their corresponding detail cells differ.
The parent must provide the final key values after any rewrite.

## Quotations

The inspected `chaosx_super_event.116.q` remains `Nature to be commanded must be obeyed\nFrancis Bacon`.
The button `chaosx_super_event.116.a` remains `The Moving Finger writes`.
The existing `super_event_text_20261003.md` handoff records parent acceptance and source verification for the Bacon excerpt and FitzGerald wording.
This worker preserved both strings and did not modernize or repunctuate them.
Historical source verification was not rerun in this bounded audit.
`chaosx.news.32.a` is authored acknowledgement prose, not a sourced quotation.

## References and presentation limits

Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-super-events`, and the relevant read-only presentation instructions of `chaos-redux-scripted-gui`.
`AGENTS.md` was read before source review.
The live reference context succeeded for workspace `mod_chaos_redux_ea3b2d67c2c0`, including installed game and offline wiki sources with no omitted required source kind.
The context heading sections alone do not establish rule coverage.
An attempted detailed read from the heading section returned `REFERENCE_POSITION_OUTSIDE_SECTION`, so the pertinent local sections were read directly.

- Offline wiki: `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, lines 59 to 102 for encoding and key/value format, lines 244 to 258 for nesting, and lines 660 to 687 for scripted localisation branch order and references. Revision reported by MCP: `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
- Installed documentation: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\loc_formatter_documentation.md`, lines 14 to 59 for formatter scope and custom tooltip examples. Revision reported by MCP: `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`.
- Installed localisation object documentation was consulted for object names. No unsupported engine behavior is claimed from a formatter example.

Standalone Technology Tree Viewer is absent from the connected tool inventory and is recorded as a package gap separately from the exposed technology inspect/render/compare routes.
Technology, doctrine, focus, and map gameplay surfaces were not part of this task.
Tool exposure does not establish service health.
No game was launched and no native application was controlled.

MCP event inspection, event rendering, and shared super-event GUI inspection were requested read-only.
Initial event selectors were rejected for missing `selector.kind`, then for using `id` instead of `eventId`.
They were corrected to `{ kind: "event", eventId: "chaosx.nr28.1" }` for the options render and `{ kind: "namespace", namespace: "chaosx.nr28" }` for lint.
At the time this handoff was first written, valid presentation requests were still pending and supplied no artifact URI.
No overflow, wrapping, layout, or complete live coverage claim is made.
The parent must carry this open presentation gate into its completion report if final results remain unavailable.

### Final MCP result received

The corrected event options render returned `EVENT_RENDERED_PARTIAL` for workspace `mod_chaos_redux_ea3b2d67c2c0`.
Its source revision is `05d44b40df4da94b29ea68dcfe8546ffb54c0b721a7931d449f3911c15afd2b8` and graph hash is `c60fb6092cb4073f90b821cae963acd971c1e2b61c0347f9121b4f6f8fab67d7`.
It reports 11 selected nodes, zero branch renders, one blocking event-chain diagnostic, and an inline source inventory truncated to 64 of 397 paths.
The partial graph render does not establish native report fitting or complete localisation branch coverage.
No production GUI image was inspected by this worker.
The final native presentation gate remains parent-owned and open.

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb6b2f92455dc65eaf6914c82f14e809139f91561417bb7d9c112a53cafeb63b/b179de2bd9cb50984982c5a8c949803ecd0e5bc7d58655ed498f8f969806401c/event-options-05d44b40df4d-manifest.json`.
- Source-linked render data: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a9426d48a786478312fe6073e8040158c46dff035e3a3ef755e15db05b75a10/0ab3449bfb0944d00219b28956f1e836c79fc6f75fe55436bdad3752ba427ffa/event-options-05d44b40df4d.json`.

The parent requested finalization without further slow MCP retries.
The namespace lint and GUI inspection results were still pending at finalization, so no successful result is attributed to them here.

## Parent disposition after the audit

The earlier hardcoded-confirmation observation is superseded by the committed constant-driven duration in `17aae2d2b`.
The world-news, closeout, failed-forecast, survey-material, mission-network, and failure-consequence prose findings were patched in that commit.
The native GUI gate remains open; this note does not convert the audit into a visual acceptance.
