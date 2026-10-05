# Event 002 release QA handoff

**Disposition: incomplete for full release sign-off.** Owned-source fixes are applied. The parent must finish the shared Settings dispatch hunk and shared localisation requests, and the HOI4 event/probability/GUI MCP evidence remains unresolved after bounded 600-second timeouts. No game was launched, no desktop UI was controlled, no workbook or CSV was written, and no commit was created.

## Files changed by this handoff

- `events/002_zombie_outbreak.txt` consumes and revalidates a Settings-selected initial state while preserving the ordinary automatic event fallback, resets the once-only news state when a new campaign begins, and sends successful outbreak sites through the shared announcement helper. It also gates and receipts the one `.12` acknowledgement and first `.13` anniversary.
- `common/scripted_effects/002_zombie_outbreak_effects.txt` adds `prepare_zombie_outbreak_initial_spawn` and `queue_zombie_outbreak_world_news`, and makes `on_zombie_threat_defeated` idempotent for the current campaign. The Settings selector excludes non-normal-civilian hosts and states not controlled by their owning country.
- `common/scripted_triggers/002_zombie_outbreak_triggers.txt` adds `is_at_war_with_any_zombie_or_weaponized_country` for the five prevention revocation availability gates, `zombie_initial_outbreak_selection_is_current` for the Settings-selected host/state recheck, and `is_zombie_counterstrain_system_active` for standard and standalone weaponized counterstrain availability/cancellation. The existing `is_at_war_with_any_zombie_country` semantics and every numeric AI weight remain unchanged.
- `common/decisions/002_zombie_outbreak_decisions.txt` blocks prevention revocation while the country is fighting the main, standard dynamic, or weaponized horde; adds shutdown cancellation/refunds to the four standard cure tiers, eight weaponized counterstrain decisions, five prevention actions and five revocations; and closes League formation, investment and disband timers when their required route ends. It displays `zombie_revoke_measures_war_tt`.
- `common/scripted_localisation/002_zombie_outbreak_scripted_localisation.txt` adds `GetZombieOutbreakNewsSiteCount`, which selects singular or plural wording for the aggregate state total.
- `localisation/english/002_zombie_outbreak_l_english.yml` replaces the unsuitable first-reveal title, description, quote and button; simplifies reachable weaponized summary text; replaces postwar bookkeeping labels; provides the count phrase and war-gate tooltip; and preserves UTF-8 BOM.
- `localisation/english/002_zombie_outbreak_requirement_flags_l_english.yml` replaces two implementation-facing country-flag explanations with player-readable wording and preserves UTF-8 BOM.
- `common/script_constants/002_zombie_constants.txt` adds `zombie_outbreak.initial_state_population_threshold_k` and the root and Settings selector now use that same million-person threshold. It renames the postwar delay to `first_anniversary_delay_days` and removes the annual memorial repeat.
- `docs/events/002_zombie_outbreak/overview.md` adds `.14`/`.15` to the developer Event Map, documents the once-only counted outbreak report and records the sourced first-reveal reference.
- `docs/plans/002_zombie_outbreak_plans/agent_decisions_2026-10-05.md` records task authority, accepted bounded corrections, proposals and evidence limits.
- `docs/plans/002_zombie_outbreak_plans/catalog_changes_pending.md` records the workbook follow-up without modifying workbook or CSV files.
- `docs/plans/002_zombie_outbreak_plans/source_snapshots/pre_release_20261005/` contains byte-for-byte snapshots of the owned event, scripted support files and localisation before this pass, plus SHA-256/byte-count manifest.

The parent separately changed the out-of-scope caller `events/zombie_weaponized_special_projects.txt:271` to use the shared world-news helper; that edit is parent-owned.

## Exact shared integration request for Settings launch

Before this pass, `common/scripted_effects/chaosx_settings_effects.txt:4007-4020` opens a manual event request in the current Settings country. The shared function must gate the new selector on `events_log_manual_event_detail_trigger > 0`; its nonmanual event selection path should retain the current root fallback. It captures that requester, but the Event 002 path had no prefire branch. After setting `event_fire_record_id` around line 4385, the generic dispatch at lines 4545-4553 fired `chaosx.nr[EVENT_ID].1` in the requester country. The owned `.1` event's `random_state` therefore saw the requester's states and silently did nothing when that country had no eligible populated mainland state. If `has_zombie_outbreak` was already set, the event also silently skipped its initialization branch.

The new owner helper is `prepare_zombie_outbreak_initial_spawn`. It rejects an active main, standard dynamic, or weaponized horde, or a disabled system, with `forced_event_feedback_reason.already_active` or `.unavailable`; otherwise it selects a normal-civilian country and one of its non-island states whose population exceeds `constant:zombie_outbreak.initial_state_population_threshold_k` and whose controller is its owner. The active-horde test requires the relevant outbreak country to control a state. That shared fixed-point constant remains set to 1,000,000 people (1,000 thousands) and the root fallback reads the same key. Success saves event targets `zombie_initial_outbreak_host` and `zombie_initial_outbreak_state`, and sets `zombie_outbreak_prefire_ready = 1` inside the successful nested `random_owned_state` block. The `.1` consumer rechecks host eligibility and the state's population, ownership, and control against the captured host; it does not rely on a state-scope `exists` check. Failure leaves the readable `no_state` reason. The root event consumes that selected state when present and retains its prior ordinary fallback for non-Settings callers.

Parent-owned integration is to add an Event 002 ID branch in `fire_event_by_temp_id_no_cluster`: run the helper; if ready, dispatch `chaosx.nr2.1` to `event_target:zombie_initial_outbreak_host`; otherwise suppress dispatch and call the existing forced-event feedback report with `chaosx_forced_event_failure_reason`. Preserve the existing `no_target` behavior for other events. Until this branch lands, the helper is available but the Settings retarget path is not wired, so G7 remains incomplete.

The parent should apply the branch only after reviewing the helper contract and preserve the Settings requester separately for event-log context. Source-based tests for the three launch cases are:

- USA with no qualifying owned state but a valid populated state in another country retargets the outbreak to that host/state.
- An active main or dynamic horde rejects a forced initial launch with “The requested event cannot occur because its situation is already active.”
- No qualifying populated mainland state in any country rejects the launch with “The requested event cannot occur because no state meets its requirements.”

These are requested source/engine cases, not observed run outcomes. The shared Settings code is outside my authorized edit scope and remains a parent integration blocker.

## G2 once-only world report

Before changes, `chaosx.news.3` had two direct callers: the owned dynamic outbreak path in `events/002_zombie_outbreak.txt` and `events/zombie_weaponized_special_projects.txt:271`. Both scheduled the same major world report after three days. The parent replaced the special-project caller with `queue_zombie_outbreak_world_news`.

The helper confirms that `event_target:outbreak_state` is controlled by a main or dynamic zombie country before incrementing `global.zombie_outbreak_news_site_count`. The first valid call sets `zombie_outbreak_world_news_queued` and queues one `chaosx.news.3` report three days later. Later successful sites before it opens update the visible count without queueing another popup. `chaosx.news.3.d` uses a singular/plural scripted phrase and names the selected target state. This is a source-level maximum of one report per initialized campaign; no live game output was observed.

The postwar source iterates all eligible countries once to queue `.12`; `activate_zombie_postwar_order` and `on_zombie_threat_defeated` now guard repeat callbacks. A country acknowledges one `.12` compact, which schedules one `.13` first-anniversary memorial 365 days later. `.13` preserves its one-time 10 PP remembrance effect and clears its open receipt without requeueing. The annual self-requeue was removed, and queued, open, acknowledged and completed flags prevent duplicate callbacks or reward claims.

## Super-event source and visual evidence

The selected quote is “The graves stood tenantless, and the sheeted dead / Did squeak and gibber in the Roman streets.” William Shakespeare, *Hamlet*, Act 1, Scene 1; the speaker is Horatio. The primary text is the [Folger Digital Text](https://www.folgerdigitaltexts.org/Ham/). Attribution confidence is very high and the text is public domain. It fits the first reveal because it describes empty graves and the dead walking through Rome before a wider calamity; it is literary imagery, not a literal zombie reference.

The button is “They're coming to get you!” Research cites [TCM's Night of the Living Dead quote entry](https://www.tcm.com/articles/148239/quote-it-night-of-the-living-dead-quotes-from-night-of-the-living-dead) and the original film's Library of Congress registration history. The researcher supports U.S. public-domain status for the 1968 original only; rights in other jurisdictions and later restorations were not verified. No copyrighted film line is used as the main quote.

The parent-provided full screenshots `C:/Users/klimp/Videos/chaos_redux_trailer/screenshots/evt002_pop00.png` through `evt002_pop06.png` and `records/qa/evt002_sheet.jpg` were inspected. `pop01.png` and `pop02.png` both show the same slot-1 super-event window at 19:00 on 19 January 1936 with identical text, geometry and map state. This is one modal remaining open across captures, not evidence of two trigger firings. `pop05.png` shows the vanilla Rheinland news event, not an Event 002 report; it does not prove Event 002's world-news count. The actual `screenshots/evt002_popKK.png` path supplied in the original brief is absent.

`events/002_zombie_outbreak.txt:173-210` contains the only initial slot-1 path found: event `.3` is `fire_only_once`, sets `super_event_visible` to value `1` for 30 days, sets `global.current_super_event_audio_id = 1`, then calls `play_current_super_event_audio`. The shared live window is `interface/chaosx_super_events.gui`, mapped by `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`; its quotation and button strings come from `chaosx_super_event.1.q` and `.a`. The parent attempted the shared before/after GUI render; it timed out after 600 seconds. Text fit and post-change clipping therefore remain visually unresolved.

## Task-specific evidence

- `python .tools/report_colour_audit.py --event 002` returned `total keys with colour: 0` after the edits. A separate targeted check confirmed no `§` token in the edited `chaosx.news.3.t` or `.d` strings. The replacement quote is plain ASCII and contains no `§` formatting.
- The actual bytes for `.a` and `.q` were inspected using Python `ascii(repr(...))`: both are ASCII-only and contain the literal `\n` sequence inside the YML string; no corrupted apostrophe, em dash, section sign, or raw YAML newline was found.
- The read-only event completion audit found all 27 literal Event 002 event title/description/option references and all 36 static GFX references in the named source files resolve against mod and installed vanilla definitions. It explicitly did not prove dynamic selection, in-game visual quality or runtime behavior.
- The locator's unrelated screenshot composite shows the outbreak modal and other unrelated windows; this was not treated as repeated world-news evidence.
- No `.xlsx` or CSV file was changed. `catalog_changes_pending.md` is the follow-up contract.

## References retained

The MCP tool list exposed live schemas for `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, `hoi4.decision_inspect`, and probability tools. No connected server version/health or task-negotiation endpoint was exposed. Reference context/search succeeded for the limited offline corpus, but detail reads were not reattempted after the domain service backlog appeared.

- Offline wiki `Effects` § `news_event`, `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:901`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, documents delayed news-event firing in current scope.
- Offline wiki `Event modding`, `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:37-75`, `:151-179`, and `:192-229`, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`, covers event IDs, localisation, option visibility/AI chance, and event firing/delays.
- Offline wiki `Decision modding` § AI, `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:357-374`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, describes decision AI willingness scores.
- Installed `documentation/effects_documentation.md:2943-2967`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, defines the supported scope and delay arguments for `country_event`.
- Installed `common/decisions/_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, documents decision visibility and activation.
- Installed `documentation/effects_documentation.md:5372-5380`, `:5522-5530`, `:5574-5582`, and `:6496-6510` documents `random_country`, `random_owned_state`, `random_state`, and event-target persistence; file revision/SHA-256 is `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
- Installed `documentation/triggers_documentation.md:1612-1619` documents `any_owned_state` and its supported scope navigation targets, including `PREV`; file SHA-256 is `7D27ED77DADAF3A213A4B3B8E78A9B0DEA9CE1A55F001D1E27886807A0A3FB2D2F535F14F`.
- Installed `documentation/script_concept_documentation.md:216-244`, SHA-256 `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7`, and `common/script_constants/documentation.md:12-28`, SHA-256 `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C`, define the globally reusable fixed-point schema used for `initial_state_population_threshold_k`. Installed `documentation/triggers_documentation.md:2482` and offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:345,414` describe `custom_trigger_tooltip`; its wiki snapshot revision is `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`.
- Offline wiki `Idea modding` § Implementation, `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md:102-129`, revision `a64049d0a02a9de4689b7c0ef80b5a887b6c6c747d3907f68c109ed3fd099ac`, and installed `documentation/effects_documentation.md:2244-2268`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, cover timed-idea application relevant to existing outbreak decisions.
- Offline wiki `Localisation` § Scripted localisation, `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:656-705`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, describes `defined_text` selection. It is reference context only; live localisation rendering is not claimed.

Vanilla precedent: installed `events/MTG_USA.txt:451` schedules `mtg_news.1` after three days (source SHA-256 `BED0AFA639F082E51EDB2936201035CF479D59FDFF866F721F8882E851B656A3`). Installed `events/AAT_NewsEvents.txt:11` defines a vanilla `news_event`. Installed `events/AAT_Finland.txt:676-682` filters a `random_country` before applying effects, and `:4656-4665` filters `random_owned_state` before spawning units (source SHA-256 `363C53751ED2FBE113FBED5635940F4494B5C67F3BFA0A3787AA327F6CDFDA13`). The decision auditor also read installed `common/decisions/AUS.txt:103-179` as a timed decision/cancellation precedent. Installed `common/decisions/AFG.txt:732-736` uses a `custom_trigger_tooltip` inside decision availability. These are structural precedents, not proof that current Event 002 source behaves in game.

## MCP routes and blockers

- Valid `hoi4.event_inspect` trace for `chaosx.nr2.1` timed out awaiting `tools/call` after 600 seconds. `hoi4.event_render` for the current chain also timed out after 600 seconds. No graph, revision, comparison or render artifact exists.
- `hoi4.probability_inspect` for Event 002 `event_option_ai_chance` timed out after 600,158 ms. No evaluation, sweep, comparison, scenario IDs, source revision or probability artifact was produced. The release follow-up found no reusable `scenarioSet`, scenario hash, or `analysisId` in the baseline result; the snapshot manifest contains source hashes only. Its pre-patch decision snapshot SHA-256 is `C85F9A4CB4CDC1A89A1FF939D84E7D8BD9503B60D6FFDF2E6F6AAE8809793AF3`, while the current decision source SHA-256 is `32B08D85865EA115894D1C065E23E955E42F66AC9DB080E7611BAFE44335770C`. Per the parent, lifecycle/availability changes did not alter numeric AI values; this follow-up cannot independently verify that through a same-scenario comparison. No `probability_compare` was submitted because no exact saved `scenarioSet` is available; inventing scenarios or fixtures would violate the same-scenario comparison requirement.
- The decision auditor's `hoi4.decision_inspect`, `hoi4.source_lookup`, and reference route yielded no results; its local source review covered 38 decisions, four categories and no missions.
- `hoi4.gui_inspect` for `zzz_cure_progress_container` and `hoi4.gui_render` for the 1920×1080 scale-1 view timed out. The independent event completion auditor reports event, render and GUI inspection calls timed out after 600 seconds. No MCP evidence is claimed.
- The parent captured GUI evidence for the super-event text after this patch, but the post-change render route timed out. It must remain a shared-GUI visual-review blocker.

## Decision and balance audit status

No numeric AI weights or balance targets changed. The new revocation trigger changes only availability and the localized requirement tooltip. The AI's old `factor = 0` clauses still mention `ZZZ` only; while an active zombie war makes the revocation unavailable, their score explanations remain narrower than the trigger, and numerical ranking is unresolved. After the required probability baseline becomes available, compare the same saved scenarios on before-source snapshot `source_snapshots/pre_release_20261005/common/decisions/002_zombie_outbreak_decisions.txt` and the after-source file.

Lifecycle fixes now cover the four standard cure timers, eight weaponized counterstrain timers, five prevention application timers, five prevention revocation timers, League formation, League investment, and League dissolution. Paid PP and Black Friday receipts are refunded on shutdown or loss of the relevant route; pending cure or penalty ideas and disbanding flags are cleared. The eight weaponized counterstrain decisions use `is_zombie_counterstrain_system_active`, so research remains available while either a standard outbreak or a living weaponized profile exists; this avoids cancelling or blocking standalone weaponized-profile research merely because it does not set the standard outbreak flag. League investment also cancels and refunds if the outbreak, membership, or available capacity is lost during its timer; the final addition must fit fully within the 170-point cap, so a pending action that no longer fits receives its PP and sale credit back. The 3-point major and 1-point minor capacity thresholds are centralized beside `max_investment`. League dissolution cancels and refunds if the outbreak ends before its seven-day timer resolves. The read-only lifecycle peer review confirmed the once-only memorial flags and reward; its counterstrain review identified the standalone-profile regression, which was corrected in the owned trigger and decisions. Remaining findings: the weaponized cure category can expose eight cure and eight profile-review actions; the League cure-duration tooltip does not match its multipliers; and the martial-law tooltip overstates protection. Five shared reversal descriptions remain parent-owned. Weighted AI comparison remains unresolved because no valid probability baseline scenario or artifact was returned.

The completion audit questioned both world-end events `.8` and `.11` triggering at Chaos tier 5, which starts inclusively at 1000 in `common/script_constants/chaos_meter_constants.txt:26`. The parent confirms the active contract is inclusive at 1000; the events correctly admit that boundary, and no threshold or MTTH change is requested.

## Assets, achievement and integration audit

- Existing Event 002 super-event images, report/event images, achievement DDS files, leader portrait DDS files, custom model runtime references, and specialized zombie sound wiring were inspected. The completion auditor found all 36 static `GFX` references in the bounded event/common files resolve, and noted that model source/sound handoffs exist in places. No asset was generated or rewired.
- Portrait provenance remains unresolved: no `chaosx_portrait_creator` handoff was located for the registered ZZZ leader and seven weaponized portrait family. Existing DDS presence does not prove approved source or processing.
- Later dated zombie model rebuild handoffs describe seven installed variants with eight actions, but earlier production plans/handoffs remain contradictory; the Wendigo package is still explicitly blocked and its old all-Meshy/sprite=zombies claims conflict with the current live Blender fallback and `infantry` consumer. Counter art has unique runtime paths but remains pending independent parent visual review. Keep the temporary asset workspace while these gaps remain; no broad asset regeneration was requested or performed.
- The event-owned `zzz_cure_progress_scripted_gui` attaches `zzz_cure_progress_container` in the shared interface file. No bounded `chaosx_event_ui_worker` handoff or before/after cure display evidence was found; the shared GUI routes timed out.
- Event log actor mapping, Event Details, evolutions, and the public Zombie Apocalypse branch source wiring exist but were not engine-verified. The `.11` Wendigo terminal is hidden and should not be added to public Event Details merely to fill the developer map. Visible `.14` and `.15` are now listed in the Event Map.
- Shared localisation requests for event-log details and achievement descriptions are listed below and remain parent-owned.

## Parent-owned requests

1. Apply the Settings dispatch branch described under G7 and preserve `settings_selected_event_id` and manual request attribution for event-log records.
2. In `localisation/english/chaosx_decisions_l_english.yml`, replace the five incorrect backward descriptions for `revoke_hygiene_measures_desc`, `revoke_migration_restrictions_desc`, `revoke_quarantine_protocols_desc`, `reopen_borders_desc`, and `revoke_extreme_martial_law_desc` with their matching `disease_revoke_*_desc` removal prose already present nearby. Clarify the martial-law prevention scope because it prevents new dynamic rear-area outbreak rolls, not established zombie fronts.
3. Review shared `localisation/english/chaosx_gui_l_english.yml:657,690` event-log detail wording and `localisation/english/chaosx_achievements_l_english.yml:105,114,118` implementation-facing descriptions; use the separate localisation audit for exact wording suggestions.
4. Complete the parent-owned post-change render of the shared super-event window and record the result or timeout.
5. Have the workbook owner review `catalog_changes_pending.md`, update the source workbook only if a player-facing catalog field must mirror the changed text, and run the exporter after any workbook save.

## Simplifications, omissions, and blockers

- Settings invalid-host retargeting is not end to end until the parent-owned generic dispatcher calls `prepare_zombie_outbreak_initial_spawn`; the helper and root consumer are in place, but this shared integration remains a blocker.
- MCP graph, probability and GUI evidence is absent due to the exact timeouts listed above. Source-only review is not engine validation.
- No probability baseline or same-scenario comparison exists; no AI balance claim is made.
- The shared revocation-description, event-details, and achievement-description localisation hunks remain parent-owned.
- Decision lifecycle/cost work, category clutter redesign, cure GUI review, portrait provenance, model/Counter review dispositions, shared GUI after-render, and spreadsheet alignment remain incomplete.
- No commits were created, per the parent task's shared-tree boundary.

## Read-only lifecycle peer review and resolutions (2026-10-05)

The reviewer confirmed that `.12` and `.13` queue, open, acknowledge, and complete once per country. The first memorial still grants the existing 10 Political Power, and the annual self-queue is gone. First-defeat effects remain inside the campaign idempotency guard. A quote-aware source scan found balanced nesting and strings; it did not prove engine parsing.

The review caught lifecycle issues that were corrected in owned sources: counterstrain research now remains available for standalone live weaponized profiles; cure tier 0 cannot overlap a counterstrain using the shared `searching_for_cure` idea; League investment checks its remaining capacity at selection, during its timer, and at resolution, cancelling and refunding if the full contribution no longer fits; League formation cancels and refunds when its initial horde-footprint or Chaos-tier conditions lapse; League dissolution cancels and refunds if the outbreak shuts down before the timer ends. The 170 investment cap is preserved using centralized last-valid totals of 167 for a 3-point major contribution and 169 for a 1-point minor contribution.

Paid Political Power amounts are saved from the same price variables used by each action and refunded on cancellation: the eight counterstrains; four cure tiers; five prevention actions and five revocations; League formation, investment, and dissolution. Cancellation removes the associated timed idea/penalty and clears the stored amount. Successful completion clears the stored amount. The Black Friday helper call is preserved in each cancellation path.

## Remaining review items

- Probability comparisons remain unresolved. The weighted-logic MCP baseline timed out and provided no reusable scenario fixture or artifact. Numeric AI weights were not changed; the new availability and lifecycle gates still need any required same-scenario probability review when a saved baseline becomes available.
- The shared Black Friday withdrawal helper withdraws credit against the current sale sequence. The owned decision files store the exact PP paid but do not carry an original sale-sequence receipt into that shared helper. A cancellation after a later sale sequence begins restores the correct PP, but reversal of its original sale credit is unverified. The helper/API is shared and outside this ownership; parent review is required before claiming sale-credit reversal is exact.
- Investment/cure changes are source reviewed only. The decision MCP route returned no artifact; no engine timing or race behavior was observed.

This peer review used no MCP routes, launched no game, and changed no gameplay files. The owner incorporated its concrete source findings before recording this status.
# Parent closure of shared integration

The Settings manual Event002 preparation and host-dispatch branches are implemented in `common/scripted_effects/chaosx_settings_effects.txt`.
The weaponized-project caller uses the same counted once-only news helper as the core event.
The five shared revocation descriptions are corrected in `localisation/english/chaosx_decisions_l_english.yml`.
The capacity helper derives remaining investment room from the maximum and actual contribution, without mirrored last-valid thresholds.
Receipt-aware credit capture and refund withdrawal are implemented for all 25 refundable decisions, with 26 refund branches and 25 successful cleanup branches.
See `refund_receipt_api_20261005.md` for the actual-source scenario results and explicit historical-credit limits.
The shared-integration requests above are resolved in source, while the recorded MCP visual, event, and probability evidence gates remain open.
