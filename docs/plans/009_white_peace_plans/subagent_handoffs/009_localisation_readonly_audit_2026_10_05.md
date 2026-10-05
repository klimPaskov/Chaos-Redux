# Event 009 read-only localisation audit

Disposition: superseded as a current-content audit by the parent-accepted 2026-10-06 G2/G3 corrections and current source-model handoff. The detailed findings below document the earlier read-only snapshot; use `agent_decisions_2026-10-05.md`, `009_white_peace_validation_matrix.md`, and `009_owned_runtime_patch_2026_10_05.md` for current wording and notification behavior.
Ownership: read-only gameplay/localisation audit.
Changed gameplay and localisation files: none.
Only this audit handoff was written.
Skills used: chaos-redux-events and chaos-redux-subagents.

## Evidence and limits

Read AGENTS.md, both named Event 009 spec files, events/009_white_peace.txt, localisation/english/009_white_peace_l_english.yml, linked White Peace entries in localisation/english/chaosx_gui_l_english.yml and chaosx_achievements_l_english.yml, common/scripted_effects/009_white_peace_effects.txt, relevant shared scripted localisation selectors, and common/achievements/chaos_redux_achievements.txt:1824-1915.
The source review reflects the pre-parent-patch wording observed during this audit.
The supplied `evt009_sheet.jpg` contains numbered `pop00`–`pop06` examples of unrelated vanilla USA/Japan popups and Rhineland/Aussa news; none shows White Peace.

Live MCP metadata exposed reference_context, reference_search, reference_read, source_lookup, event_inspect, and event_render.
Actual calls to reference_context(surface=localisation) and event_inspect(mode=lint, selector.eventId=chaosx.nr9.1) returned `MCP tool hoi4_agent_tools/hoi4.reference_context is not available to the model` and the corresponding event_inspect error.
No GUI inspect/render route appeared in the connected tool metadata searched for this audit.
Event-chain inspection and shared GUI visual coverage are therefore blocked, with no artifact URI and no overflow verdict.
No standalone Technology Tree Viewer was exposed in the connected metadata, which remains a package availability gap, with no technology surface assigned here.
Source review is not equivalent to engine or render evidence.

Offline fallback references read: paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:65-88 (encoding/key rules), 529-540 (namespace/event-target access), 656-690 (scripted localisation selection and default scope).
Wiki SHA256 revision: 1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064.
Installed reference read: C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md:126-159 (contextual localisation and event scopes).
Installed SHA256 revision: 884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7.
Vanilla precedent: localisation\english\events_l_english.yml:20,23 uses scoped country-name tokens in event prose.

## Keys, mappings, scopes, encoding

Audited set: chaosx.nr9.1.t, chaosx.nr9.2 through .5 title/description/option/tooltip keys, white_peace_status_quo_settlement, all shared GUI keys containing white_peace, all five 009_white_peace achievement NAME/DESC/tooltip groups, and the scripted selectors routing Event 9 and White Peace evolution stages.
Missing key list: none found for the actual displayed report keys, linked White Peace GUI outputs, and achievement keys inspected.
Duplicate key list: no duplicates found among Event 009 and White Peace keys across English localisation.
Raw key exposure: none identified in the examined report/options and custom achievement tooltips.
Encoding concerns: none found in the three audited localisation files, which begin EF BB BF.
Sourced quotations: none in the assigned text, so no attributed wording was modified or proposed for normalization.

The spec text handoff recommends visible reports .1-.4, while current source uses hidden .1 and visible .2-.5.
This is a documented suggested-key mapping shift, not a missing .1 description defect, because the spec explicitly permits preserving existing IDs.
Keep the actual ID mapping in subsequent documentation.

chaosx.nr9.2.d uses [white_peace_primary.GetName] and [white_peace_partner.GetName] correctly without event_target: or ? prefixes.
The helper saves regular event targets during selection (effects:684,741), and dispatches the report inside the same effect chain (1193-1221).
No bad dynamic scope was identified in that initial delivery path.
Regular-target survival and later concurrent popup behavior remain runtime uncertainties, not proven by this audit.
No scripted localisation call is reachable from these report descriptions, and their title/description keys contain no colour codes.
Shared GUI output colour codes occur in dark GUI labels, not in the current report descriptions.

## Findings and recommended fixes

1. Invalid forced entry is silent.
Event chaosx.nr9.1 contains preparation and a success-only dispatch, with no failure notification.
The parent reports skip reason 3 / major_locked for USA on 1936-01-01, with Italy-Ethiopia the only war.
Adding only an availability string cannot fix this, because no visible event consumes it on that forced path.
The owner must select an eligible pair or add a visible failure event using the actual skip reason.
Suggested plain failure wording: `No war can be settled. The only eligible conflict involves a major power, and White Peace cannot include major powers at its current stage.`
Adjust `eligible` if the script means merely a potential candidate rather than a fully eligible conflict.
Provide reason-specific text for no war, protected conflicts, recent settlement, and no valid pair without claiming peace occurred.

2. Report prose is materially vague and centered on administrative props.
chaosx.nr9.2.d starts with a neutral channel/paper and ends by ordering countries rather than armies to stop where they stand.
That also obscures return to the pre-war frontier and can imply occupation remains in place.
chaosx.nr9.3.d uses `One settlement sets a pattern`, `dry language`, and files instead of concrete belligerents and troops.
chaosx.nr9.4.d replaces the major government with `A larger flag` and signatures, leaving the actor and settlement unclear.
chaosx.nr9.5.d gives clerks and circulars causal power and says wars have `no order left to continue` rather than stating that governments ordered fighting to cease.
Rewrite around the belligerents, exhausted armies, orders to withdraw to the old frontier, and peace without territorial gain.
The existing .2.d opening sentence chain is repetitive rather than dramatically staccato, but should be combined around one clear settlement action.
Titles .3.t and .5.t are allowed established names, though their descriptions should not duplicate their table/paper framing.
No em dashes or sentence semicolons were identified in these current report strings.

3. Tooltip terms are opaque.
chaosx.nr9.2.tt through .5.tt use `safe`, `rare`, `no-gain formula`, and `conflicts` without saying which countries leave the war or what happens to occupied land.
Prefer selected country names and the consequence `end their war and restore the pre-war borders` where the effect guarantees it.
For multi/broad reports, state that additional eligible belligerents may be settled rather than guaranteeing a count before option-time validation.
Dynamic text opportunity: use the selected primary/partner names in major and multi openings, preserve plain tokens, and show actual settled count only after it exists.

4. Event Details reveals mechanical effects and future reach.
chaosx.events_log.window.event_details.white_peace currently explains that early settlements end one minor war, later several minor wars, and rare major-power involvement.
The latest parent/user rule overrides the older draft direction to list mechanics here.
Suggested final premise wording for parent review: `Exhausted belligerents accept peace without conquest or indemnity, restoring the borders they held before the war. Soldiers leave occupied towns and return to their own frontier as their governments abandon the hope of victory.`
Verify troop withdrawal and border restoration before adopting the second sentence.
A safer first-sentence-only version remains concrete and sufficient.

5. Evolution overview exposes process and probabilities.
chaosx.events_log.window.evolution_details.white_peace.body.event_detail says `inside one firing` and `how rarely larger actors`.
Suggested replacement: `Armistices spread from minor border wars to larger conflicts as exhausted governments accept peace without land or tribute.`
Stage bodies .stage_1 through .stage_3 are more concrete and natural than the overview.
.stage_2 assumes `neither side can secure a decisive result`, which is atmosphere rather than a verified eligibility condition.
.stage_3 says `reopen crossings` and `release armies trapped`, which are not explicit script effects and may imply extra mechanics.
Prefer concrete cessation and withdrawal only where guaranteed by the engine effect.

6. Availability messages hide the real blocker.
chaosx.event_cluster.availability.white_peace.recent_memory uses `memory` and `safe pairs`.
Suggested wording: `Unavailable: the countries that could make peace have already received a recent settlement`.
.major_locked `major settlement stage not reached` is abstract.
Suggested wording: `Unavailable: all possible settlements involve a major power, which White Peace cannot include at this stage`.
.protected_conflicts `visible` is an implementation term.
Suggested wording: `Unavailable: the active wars cannot be interrupted by White Peace`.
.no_safe_pair and chaosx.events_log.events.na_reason.white_peace_pair can use `no countries currently meet the settlement requirements`.
Maintain dark-GUI formatting only on those GUI outputs, with separate plain failure-event keys for parchment.

7. Achievement clarity and scope mismatch.
009_white_peace_no_winner_DESC `Survive the silence` is empty atmosphere.
achievement_white_peace_no_winner_tooltip states only the player's survival, but chaosx.nr9.20 requires both settled countries to exist, remain independent and uncapitulated at its delayed check.
Proposed consequence text: `After a White Peace settlement, both countries must survive independently without capitulating for 180 days.`
The source checks endpoint state rather than continuous state, so `for 180 days` itself may overpromise continuous tracking.
The owner should choose wording consistent with current behavior, such as `Both settled countries must remain independent and uncapitulated when the settlement is checked 180 days later`, or implement continuous failure tracking.
The latter wording is process-heavy, so gameplay correction is preferable if the accepted requirement is continuous survival.
009_white_peace_chain_of_tables_DESC `before any giant sits down` is vague metaphor.
Its tooltip is much clearer, but `six` is static while the threshold is owner tuning and should become dynamic if the constant is exposed for localisation.
achievement_white_peace_the_circular_tooltip uses `firing`, `safe conflicts`, and `safe pairs`.
Replace with a visible settlement outcome, preserving the actual three-conflict/five-pair conditions.
Status Quo Ante and Silence of Giants tooltips omit definitions of prolonged war, an opportunity for a dynamic duration if the existing age model has a reliable value.
No gameplay changes are authorised to this auditor.

## Cross-surface handoff and completion limits

The read-only CSV export shows Event 9 Details currently mirrors the same mechanical Event Details paragraph.
The workbook was not inspected or edited, and CSV evidence does not establish current workbook content.
After the parent accepts final wording, spreadsheet owner must mirror exact final keys: chaosx.events_log.window.event_details.white_peace; chaosx.events_log.window.evolution_details.white_peace.title.stage_1, .stage_2, .stage_3; corresponding body.stage_1, body.stage_2, body.stage_3; and body.event_detail if that field is used.
The spec draft retains `damage to a larger story`, `cleanup valve`, dynamic weights and future mechanics in public Details direction, conflicting with the latest parent/user instruction.
Treat the latest instruction as authoritative and reconcile those draft passages in documentation.
No proposed prose above is an accepted patch.
No hidden achievement path was added to Event Details during this read-only audit.

Meaningful validation completed: report/tooltip key mapping against actual visible events, report colour and reachable-token review, relevant achievement text against unlock consumers, Event Details/evolution wording comparison, and duplicate-key search restricted to Event 009/White Peace keys.
Skipped meaningful validation: MCP event-chain coverage and shared GUI visual overflow due to the exact route blockers above; live behavior because the user owns HOI4 testing; workbook comparison because it was outside this audit ownership.
Unresolved decisions: invalid forced-entry owner behavior, continuous survival versus endpoint check, whether border/troop wording is guaranteed, and final accepted prose for spreadsheet mirroring.
## Second pass against Event 009 owner updates

Read-only re-audit completed 2026-10-05.
Changed gameplay/localisation files: none.
This section supersedes first-pass findings where current source differs.

Current source SHA256:
- localisation/english/009_white_peace_l_english.yml: 0C127660B23019519D9553491807A15D76C663C174F188BEB330C4AF39E47EC5
- common/scripted_localisation/009_white_peace_scripted_localisation.txt: FAFA41CEF1ADB03842B1B687934BEB01054E4BBB19E50C89ECA9DEE0AB093802
- events/009_white_peace.txt: E1D284F8BE3FAB8E1083FC6A0F0ED573E48A64BE54D6D86468F7F40BAE74B1FB
- common/scripted_effects/009_white_peace_effects.txt: 3F270AF72823F6E44C48CEF860A738138E2A64AF8E2443784EED797271C6E2E3

Audited current IDs: hidden .1, acknowledgement reports .2-.5, rejected-entry report .6, world news .7-.10, and delayed achievement check .20 only as a linked consumer.
All current title/desc/option/custom-effect-tooltip references in events/009_white_peace.txt resolve to Event 009 localisation.
All five reason output keys referenced by GetWhitePeaceInvalidEntryReason exist.
No duplicate Event 009 keys, colour characters, em dashes, sentence semicolons, or prohibited records/segments/snapshots/transactions/receipts/ledgers/pilots/providers terms were found in the owner localisation set.
No sourced quotations occur.

Current delivery: .1 prepares, applies the settlement, checks actual settled count, and then dispatches acknowledgement or .6 failure.
The .2-.5 options no longer invoke settlement effects.
In the audited snapshot, if any settled country was human, the report was routed to one saved human recipient; otherwise matching .7-.10 news was fired. That routing was superseded on 2026-10-06 by the accepted per-country pending-report queue, which sends the aggregate event once to every affected human and sends one global news event only for all-AI settlements.
Dispatch uses actual count: one pair uses .2/.7 or .4/.9 for major branch, broad branch with more than two pairs uses .5/.10, otherwise multiple pairs use .3/.8.
Thus the report/news key mapping follows actual executed outcome rather than prospective branch capacity.
Regular report targets are saved before execution at effects:855-856, not overwritten by subsequent pair selection, and referenced without event_target: in localisation.
No bad namespace syntax found in [white_peace_report_primary.GetName] or [white_peace_report_partner.GetName].
The failure reason is copied into the initiating country at effects:1274 and .6 is delivered in that country scope, so ROOT.white_peace_invalid_reason selects the expected local value with a no-safe-pair fallback.
Target persistence in displayed reports/news remains an engine uncertainty until user observation because the MCP route remains unavailable.

Resolved first-pass findings: visible failure delivery exists, reports describe armies and armistice consequences, primary/partner tokens are preserved, report and news descriptions plus reachable reason output are plain and colour-free, and acknowledgement effects execute before display.

Remaining owner findings:

The parent corrected all `.6` invalid-entry strings on 2026-10-06. The new reason values explain no active war, no isolated two-country front, major powers outside the terms, excluded governments, or a recent armistice. These replace the `.6` wording findings recorded from the earlier source snapshot.
It also says earlier minor wars must establish a precedent, but determine_white_peace_stage:241-256 permits major stage through current war and eligible-pair pressure without previous settlements.
Suggested wording: `The wars that could receive these terms involve major powers, which White Peace cannot include at its current stage.`
If the skip-reason priority does not prove every candidate is locked this way, use `A possible settlement involves a major power, which White Peace cannot include at its current stage.`

3. chaosx.nr9.4.d assumes a major versus `smaller neighbor`.
The major-pair trigger allows either or both countries to be major, and does not require geographic adjacency (triggers:68-74).
Use both saved report names, as .9.d already does, or `A major power and its enemy have ended their war` without smaller/neighbor assumptions.

4. chaosx.nr9.3.tt and .5.tt say wars `end`, and .4.tt says the war `ends`, despite being post-effect-only acknowledgements.
Past or present-perfect tense should match descriptions, such as `These wars have ended on their prewar borders without indemnities`.
The report custom-effect-tooltips repeat descriptions with little added information, so removal is also a bounded option if the parent wants acknowledgement-only presentation.

5. chaosx.nr9.6.reason.protected_conflicts `special forces` can mean ordinary military special forces to a player, whereas the source refers to protected/special/nonhuman countries.
Prefer `The active wars involve countries that White Peace cannot include` or a precise public description that does not reveal hidden classifications.
.reason.no_safe_pair `conditions for a contained settlement` stays vague, but it correctly avoids inventing one blocker when several different conditions can fail.

6. .3.d/.8.d `fighting has ended in each country` is broad and could imply all fighting anywhere in the country ended.
The current isolated-pair trigger supports a contained bilateral conflict, so `these wars have ended` is clearer and directly names the reported consequence.
Generic reports remain acceptable for multi-pair outcomes because the saved targets only identify the first pair, and actual outcome count is already used to choose the report.
Adding a real settled count is an optional dynamic text opportunity, not a missing key.

Shared parent-owned surfaces observed during this pass:
- event_details.white_peace is already changed to the concrete armistice premise and no longer exposes future reach.
- evolution_details.white_peace.body.event_detail is already changed to armies/negotiations and no longer says `one firing` or discloses rarity.
- No Winner tooltip now correctly names both countries, but `for 180 days` still exceeds an endpoint-only delayed .20 check unless another owner has added continuous failure tracking.
- Chain of Tables description still uses `giant sits down`, and its tooltip still hardcodes six.
- The Circular tooltip now matches three separate minor wars and removes five-pair/process terminology.
- Shared availability strings still use `memory`, `safe pairs`, `stage not reached`, and `visible` and should be reconciled by the parent.
- Stage 3 evolution prose still mentions reopening crossings and releasing trapped armies beyond explicit settlement effects.
These shared lines were not edited by this auditor.

Meaningful validation: inspected reason selector scopes against failure dispatch, report-key dispatch against settled counts and actor selection, report/news tokens against saved targets, owner keys against exact consumers, and major wording against actual pair trigger.
MCP event inspection and GUI visual overflow remain blocked as recorded above, with no artifact URI.
The workbook remains outside ownership and was not inspected or changed.
Unresolved owner decisions: neutral no-war failure framing, accurate major-lock explanation, major-versus-major wording, and acknowledgement tooltip tense/removal.
## Final working-tree recheck

Read-only recheck, 2026-10-05.
No gameplay or localisation edits by this auditor.
This section supersedes the second pass where fixes have landed.

Current SHA256 revisions:
- localisation/english/009_white_peace_l_english.yml: 5D007F417CC7D6706F40E01FB77CEA81CDCC826950DCC78C0BFCB30F05D63106
- common/scripted_localisation/009_white_peace_scripted_localisation.txt: FAFA41CEF1ADB03842B1B687934BEB01054E4BBB19E50C89ECA9DEE0AB093802
- events/009_white_peace.txt: C03AE498E0222AD28B9AD1AAD584312C77C5FAF84968A31AB3683C75F4F48914
- common/scripted_effects/009_white_peace_effects.txt: 94A417A9845C4A0618F590FA7361454A6D6CB6BBC4F3116A5FE9433D052C819D
- common/scripted_effects/chaosx_settings_effects.txt: 7EEB5523D6101C3B76BD8E02AB3728CFA0A8F08CE49E5A551B497D7CC9FD83A7
- common/on_actions/009_white_peace_on_actions.txt: F84D0C9BCE0876275665DB92CB262D073CD7340A7A988A905B169F4762A06F06

Confirmed resolved: .6 description/action are neutral for no-war state; major_locked no longer promises a prior minor settlement requirement or a unique front; .4 no longer requires a smaller neighboring country; .2-.5 tooltips use completed-action tense; protected-conflicts reason no longer confuses special actors with military special forces.
All event title/description/option/custom-tooltip mappings remain present.
All reason-selector outputs remain plain, and no report/news text or reachable scripted reason output contains colour characters.
Saved report-target namespaces and country-scoped failure reason mapping are unchanged and valid in source.
Report .2-.5, failure .6 and news .7-.10 retain the current outcome-based dispatch mapping described in the second pass.

Settings source: chaosx_settings_effects.txt:4257-4264 calls white_peace_report_failed_manual_request when Event 9 preparation fails.
The owner helper guards a genuine manual Event Details request, excludes cluster-member fire context, checks the saved human requester, and suppresses duplicate feedback through chaosx_manual_event_failure_shown before dispatching .6.
This closes the earlier missing invalid-GUI-force feedback route at source level, without claiming observed runtime execution.

No Winner: .20 now checks one direct carried white_peace_no_winner_partner.
Both countries receive 181-day watch flags; the recent-country cooldown is also 181 days, longer than the 180-day delayed achievement check.
The owner on-action file clears watches on capitulation, annexation, puppet/release/subject transitions.
The earlier endpoint-only localisation objection is closed at source level because failure states now clear the evidence needed by the delayed check.
Event on-action consumer semantics and carried-target runtime delivery remain the parent's validation responsibility.
The tooltip `Both countries must remain alive, independent, and uncapitulated for 180 days after White Peace` matches the implemented tracking intent.

Remaining owner text at this exact hash: .3.d and .8.d still say `The fighting has ended in each country`, despite the parent's stated intended change to `these wars`.
The intended edit is not present in the read working tree and remains a small outstanding wording hunk.
Suggested sentence: `These wars have ended without a transfer of land or an indemnity.`

Remaining shared parent-owned hunks:
- 009_white_peace_no_winner_DESC still says `Survive the silence`, a vague description even though its tooltip is accurate.
- 009_white_peace_chain_of_tables_DESC still uses `before any giant sits down`; its tooltip still says `branch fires` and static `six` rather than the existing tuning value.
- 009_white_peace_the_circular_DESC still centers travelling armistice text; the tooltip already clearly states three separate minor wars.
- shared availability reasons still expose `memory`, `safe pairs`, `stage not reached` and `visible`.
- evolution body.stage_3 still implies reopening crossings and releasing trapped armies beyond explicit settlement effects.
Shared Event Details and evolution introduction are already improved and need no further wording repair on the inspected strings.

Meaningful final validation: actual caller-to-failure-helper link, continuous-failure watch consumers, current report/news/reason key mappings, plain output closure, and corrected major/acknowledgement wording.
No sourced quotations or dynamic tokens were changed by the auditor.
MCP event/GUI route blockers and absent standalone technology viewer remain as previously recorded, with no visual-overflow evidence.
Workbook/CSV remain unedited.
### Final owner delta confirmed

Both chaosx.nr9.3.d (line 6) and chaosx.nr9.8.d (line 27) now contain `These wars have ended without a transfer of land or an indemnity.`
Current localisation SHA256: 458FE9504A4ECF35AB77E54FD3C937907BDB66CECE6FF6731A362997F508A0F2.
This supersedes the last outstanding owner wording hunk above.
No additional owner localisation blockers remain in the audited Event 009 report/news/reason set.
No gameplay or localisation edits were made by this auditor.

Final remaining shared parent-owned wording keys:
- 009_white_peace_no_winner_DESC: vague `Survive the silence`.
- 009_white_peace_chain_of_tables_DESC: vague `giant sits down` metaphor.
- achievement_white_peace_chain_of_tables_tooltip: `branch fires` process wording and static six instead of existing threshold access.
- 009_white_peace_the_circular_DESC: generic travelling armistice text rather than concrete wars ending.
- chaosx.event_cluster.availability.white_peace.no_safe_pair, .recent_memory, .major_locked, .protected_conflicts and chaosx.events_log.events.na_reason.white_peace_pair: safe-pair/memory/stage/visible jargon, with general unavailability less informative than current .6 reasons.
- chaosx.events_log.window.evolution_details.white_peace.body.stage_3: reopening crossings and releasing trapped armies imply extra consequences not explicitly represented by the settlement effect.
NoWinner tooltip is no longer a blocker, and Circular tooltip already states the current three-war condition clearly.
Shared Details and evolution introduction need no further wording changes on the inspected current source.
MCP visual/event inspection remains blocked as documented, so source clearance does not establish rendered or runtime clearance.

## Parent G2/G3 disposition, 2026-10-06

The parent has since resolved the invalid-entry, achievement, detail/evolution, stage-availability, and acknowledgement-wording findings documented at the earlier hashes. The current Event 009 failure reasons state the active-war, isolated-front/capital, major-term, protected-government, and recent-armistice cause in plain language. Shared achievement wording now matches the six separate minor wars, the three-war Circular condition, and continuous 180-day No Winner condition.

Successful result delivery also changed after this audit: each applied pair marks both human endpoints with a transient `white_peace_human_report_pending` country flag. A single post-settlement loop sends the actual aggregate report once to every human belligerent and clears the queue. The old single `white_peace_human_recipient` path described in this snapshot has been removed. All-AI chains still send one global news event. The updated source model and scenario results are in `../source_models/009_white_peace_helper_output_lifetimes.py` and `../source_models/009_white_peace_helper_output_lifetimes_results.json`.

The screenshot sheet shows unrelated `pop00`–`pop06` vanilla cards. It contains no White Peace example; it is not evidence that a file named `evt009_popKK.png` is missing. Live popup/news presentation and MCP visual validation remain unavailable.
