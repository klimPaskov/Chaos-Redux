# Event 012 Africa final release-candidate completion audit

Date: 2026-07-29

Mode: Read-only completion audit

## Verdict

**Release-candidate result for the narrowed milestone: conditional pass.**

No active Event 012 parser or runtime-registration blocker was found in the settled static sources.

Event 012 is **not complete as a whole**.

The core African event, Charter, action, Scramble, country-loading, localisation, and presentation surfaces have enough static wiring evidence to proceed to user-owned in-game validation, while unfinished formations, external world packages, terminal world content, optional visual pools, models, audio roles, and several proof audits remain explicitly unreachable, dormant, or documented as incomplete.

The remaining focus-loader and layout findings, timed-cooldown uncertainty, achievement proof gaps, and absence of an in-game lifecycle and balance run prevent an unconditional safety claim.

No gameplay file was edited by this audit.

## Completion status by surface

| Surface | Status | Evidence and disposition |
| --- | --- | --- |
| Entry event and registration | Finished for static RC registration | `chaosx.nr12.1` is the fire-once entry in `events/012_african_union.txt`; `common/scripted_effects/chaosx_logic_effects.txt` registers `constant:africa_event.id` in the fire-once pool and rejects unavailable Event 012 candidates through `africa_automatic_event_is_available`. |
| Event definitions and dispatch | Finished for static RC registration | The five Event 012 event files contain 43 unique definitions, comprising 39 country events and 4 news events. The audit found no duplicate ID and found every definition referenced outside its defining occurrence. |
| MCP event parsing | Partial but non-blocking | Refreshed `hoi4.event_inspect` lint for `chaosx.nr12.1`, `chaosx.nr12.220`, `africa_priority_member.1200`, and `africa_world_order.1` returned no blocker. The entry and result notice each returned one `EVENT_OPTION_DANGLING` design warning for an acknowledgement-only option. The priority and world samples returned no issue. The large-workspace analysis was partial, so this is not a complete engine-equivalent parse. |
| Core Charter action runtime | Finished for the reachable RC surface | The decision audit records 213 unique decisions and missions with no duplicate decision ID, missing localisation key, undefined action constant, or missing literal sprite. The 102 action IDs use the shared quote, validation, payment, mission, outcome, and cleanup contracts. |
| Strange formations, actions 74 through 76 | Safely deferred | `africa_select_awaken_stone_cohort`, `africa_select_train_gorilla_heavy_infantry`, and `africa_select_organise_pan_sappers` require `africa_strange_formation_package_ready` in both player visibility and action validation. A repository-wide setter check found no setter. Their models, unit templates, entity consumers, and runtime formation package remain absent. |
| Scramble settlement | Finished for the Africa-only RC closure | `africa_scramble_close_continental_docket` requires the completed aftermath conditions, no active intervention war, and no external candidate carrying `africa_world_package_implementation_ready`. Its effect settles the Scramble, clears the active response flag, records the world order as deferred, and does not install or simulate any external package. |
| External world packages and actions 85 through 92 | Safely deferred | Candidate selection and package installation require the per-country flag `africa_world_package_implementation_ready`. No setter exists. The six external focus packages therefore remain dormant. The terminal identity additionally requires the unset global flag `africa_the_world_super_event_package_ready`. |
| Dormant world focus content | Partial and gated | The focus audit counted 121 world-package focuses. They remain iconless and use simplified AI factors. They are not an active missing-asset blocker while the readiness gates have no setter, but they are not a completed package. |
| Active continental and priority focus trees | Partial with release risks | The focus audit counted 405 focus blocks in total: 276 continental, 8 priority, and 121 dormant world. It found no duplicate focus ID or dangling prerequisite and found localisation for all 405 focuses. The 21 active base and shine icon contracts resolved. Layout and loader risks remain below. |
| Focus layout | Release risk, not a confirmed parser blocker | The focus audit recorded 570 blocking layout diagnostics and 1,028 intersections for the continental tree because nine mutually exclusive overlays reuse the same coordinates. This may be an offline-render false positive when `allow_branch` exclusivity works as designed, but runtime branch exclusivity and player-facing layout were not proven. |
| Focus loading | Release risk | Continental and world loaders use `keep_completed = no`. Duplicate installation or a failed one-shot guard could discard completed-focus progress. The priority loader is designed to avoid replacing meaningful existing trees, but the lifecycle was not exercised in game. |
| AI | Partial | The bounded action controller, decision AI, event response profiles, focus AI factors, and focus-plan files exist. The accepted 64-profile matrix has not received campaign simulation evidence, 107 route-body focus AI blocks remain flat, and no probability sweep or long campaign balance proof was completed. |
| Country and tag loading | Finished for the narrowed RC surface | Event 012 creates no country tag and no Event 012 country-tag registration file. Sixteen priority packages reuse vanilla or Event 006 identities. The protected Event 006 and Soviet namespace audit checked 136 tags and found zero external country-definition collision. |
| Independence Wave carriers | Finished for static asset presence, promotion-gated in play | `DOX`, `DSX`, `DUX`, `DYX`, `DZX`, `EMX`, and `EQX` already exist as Event 006 carriers. All seven have large, medium, and small base TGA flags present. Event 012 does not duplicate these tags. Their priority presentation remains subject to the package-promotion logic and final provenance acceptance. |
| SAF exclusion and RSA | Dispositioned | `SAF` remains the existing South Africa identity and is deliberately outside the Event 006 carrier and priority cosmetic-flag ladder. South Africa uses the dedicated Event 012 RSA event, decision, trigger, effect, and on-action package. This exclusion is not a missing African tag or a fallback tag. |
| Sovereign portraits | Installed but promotion-gated | Sixteen sovereign portrait DDS files and their GFX registrations exist. Their characters are recruited only through the corresponding package paths. Final historical provenance and player-facing acceptance remain documentation work rather than a registration blocker. |
| Charter scripted GUI | Finished for static RC registration | The registration audit resolved 205 texture rows in the six Event 012 GFX files, including all 16 Charter textures and all 16 sovereign portraits. The Charter GUI has 36 button elements aligned with its click, enabled, and visibility handlers, and 63 localisation tokens. Static fallback textures exist for its two frame animations. No live resolution, scaling, hover, or click-region test was performed. |
| Localisation | Finished for referenced English RC surfaces, with two deferred strings | The localisation audit found 3,299 unique Event 012 keys across 10 BOM-encoded English files and no missing referenced event, focus, idea, decision, category, scripted-localisation, or Charter GUI key. It also corrected the scripted-localisation field spelling to `localization_key`. Two requested Afaan Oromoo strings remain absent pending native review and exact placement. |
| Event log and details | Finished for the implemented stages | Event 12 has the `chaosx.event_name.12` mapping, Event Details text, actor and history mappings, cluster membership, evolution type, evolution names, history views, and evolution portrait selection. |
| Evolutions | Finished for baseline plus Evolutions I through III | The event log and detail surfaces carry three logged evolutions. The originally requested Evolution IV is deliberately reinterpreted as the post-unification world-order state rather than another logged tier-6 evolution. This is an accepted simplification and must not be described as a fourth implemented logged evolution. |
| Event 13 natural-disaster API | Finished for the accepted RC call contract | Actions 69 and 70 save the selected enemy as `natural_disaster_call_target_country`, identify Event 012 as a hostile caller, use selected-country targeting, set the family to random, call `call_natural_disaster`, snapshot the result, and apply cooldown and backfire handling. Event 13 source files are unchanged by this integration. |
| Natural-disaster promotion refinement | Finished and aligned | The settled code raises the hostile disaster call to regional severity when the host has `africa_priority_member_full_promotion`. The player-facing descriptions now say that a fully promoted sovereign package raises the call to regional intensity, and `docs/012_africa_natural_disaster_weapons.md` carries the same contract. Localisation retains its BOM. |
| Achievements | Partial | Forty-four achievement definitions and 132 DDS files exist, giving each achievement normal, grey, and not-eligible art. The final owner-system milestone and disqualifier callsite audit remains open. Achievements tied to gated world or model content remain unreachable by design, and static definition presence is not completion proof. |
| Super-events and audio | Partial and dormant | The four super-event image rows are installed but dormant. Scramble Response and Continental Wars audio masters exist as approximately 30.4 MB WAV files, but remain unwired and dormant. Africa Is One and The World audio roles remain blocked or unproduced. No sound ID, slot, runtime trigger, or live playback completion is claimed. |
| Asset matrix | Reconciled but mostly deferred | The authoritative matrix has exactly 239 rows: 43 `installed_runtime`, 28 `installed_dormant`, 12 `deferred_runtime_gated`, 133 `deferred_controlled_pool`, 16 `deferred_model_required`, and 7 `deferred_unique_package_required`. It has zero `pending_runtime_blocker` rows. |
| Workbook and CSV exports | Aligned with incomplete status | The `Events` sheet row for Event 12 describes the current entry, three evolutions, Scramble response, tier, cluster, and danger, and correctly remains `In progress`. The three exported CSV files are newer than the workbook in the settled workspace, so the workbook/export relationship is not stale. Full Event 12 completion is not recorded. |
| Cleanup and bounded scope | Finished for static RC review | Event 012 has no recurring global `on_daily`, `on_weekly`, or `on_monthly` country iteration. Its `every_country` uses are one-shot setup or bounded reconstruction paths, not recurring world ticks. Host transfer, action generation cleanup, mission cancellation, Scramble settlement, priority withdrawal, and RSA cleanup surfaces exist. Their complete lifecycle was not run in game. |

## Confirmed release-candidate blockers

No confirmed active parser or registration blocker remains for the narrowed core release-candidate milestone.

This does not mean the core is proven safe in a running campaign.

The following are active release risks that still require user-owned in-game evidence:

1. The continental focus overlay generated extensive offline layout diagnostics despite intended mutual exclusivity.
2. `keep_completed = no` makes accidental duplicate focus installation potentially destructive.
3. The action target cooldown passes a variable-backed duration into a timed country flag. Static precedent exists, but the exact path was not exercised in game.
4. No full entry-to-host-transfer-to-evolution-to-Scramble-to-cleanup campaign lifecycle was run.
5. No task-specific long-campaign AI, cost, resource, or outcome-distribution balance pass was run.
6. Achievement owner, milestone, and disqualifier callsites have not received a complete end-to-end proof audit.
7. Charter GUI runtime scaling, interaction, animation, and resolution behavior remain visually unverified.

## Explicitly deferred or blocked full-content requirements

### Gated gameplay

- Actions 74 through 76 remain unreachable until the strange-formation package, models, templates, and consumers exist and the readiness flag receives an intentional setter.
- External actions 85 through 92 remain unreachable until individual country packages receive `africa_world_package_implementation_ready`.
- The terminal The World identity remains unreachable until its packages settle and `africa_the_world_super_event_package_ready` is intentionally set.
- Six continent packages and The World remain incomplete country, focus, decision, AI, presentation, rights, and audio packages.
- Three accepted conditional host shells, Basutoland `HZX`, Swaziland `EUX`, and Zanzibar `ELX`, remain blocked from ordinary host play because no accepted playable start package makes them valid hosts. No new tag was added to bypass that condition.

### Assets and future models

- The 16 `deferred_model_required` rows are the Pan, Gorilla Kingdom, The Green, Living Rivers, Stoneborn, and Ancient Hosts country visual packages plus elephant logistics, elephant shock, gorilla heavy infantry, Pan sappers, stone cohorts, riverborn, forest giants, oracle recon, disaster wardens, and plague carriers unit identities.
- The 7 `deferred_unique_package_required` rows are Middle East, Europe, Asia, North America, South America, Oceania, and The World.
- The 12 `deferred_runtime_gated` rows are the Scramble diplomacy, Scramble defence, high-chaos nature, high-chaos nonhuman, high-chaos disease, ancient host, continent sponsorship, continent union, terminal continent war, and The World focus families plus the priority promotion card and route-capstone seal family.
- The 133 `deferred_controlled_pool` rows remain optional controlled-pool content. They must not be treated as missing active references, but neither may they be claimed as produced.
- The 28 dormant installed rows include four super-event images, seven constitutional identity packages, sixteen priority country visual packages, and the priority distinct-mechanic icon family.

### Audio, text, and rights

- Scramble Response and Continental Wars audio masters are produced but unwired.
- Africa Is One and The World audio roles remain blocked.
- Two exact Afaan Oromoo strings remain deferred for native review.
- Sovereign portrait and carrier-flag source provenance and final rights acceptance remain documentation tasks.

## Simplifications and accepted reinterpretations

1. Twenty-two hosts have full playbooks and twenty-nine use compact playbooks.
2. Evolution IV is represented by the post-unification world-order state rather than a fourth logged evolution.
3. Active focuses use family icon reuse rather than unique art for every focus.
4. Dormant world focus trees use iconless nodes and simplified AI until their package gates are intentionally promoted.
5. Many route-body focus AI blocks use flat factors instead of host and overlay-specific strategy.
6. The entry and several notices use generic vanilla African unity or conference event art rather than unique report images.
7. The 215-polity research catalog remains a controlled claimant and identity pool, not 215 country tags.
8. No new African tag, cosmetic carrier, or placeholder country was created to force incomplete packages into runtime.

## Stale contradictions and source-of-truth disposition

1. `docs/plans/012_africa_plans/012_africa_implementation_acceptance_ledger.csv` remains a historical ledger with 809 rows and old dispositions of 48 implemented, 102 merged, 424 queued, and 235 blocked. Its 239 asset rows still read as queued and its achievement rows preserve obsolete art-gap wording. It must not override the current 239-row asset matrix or this audit.
2. Historical country-audit sections that reported missing sovereign portraits or carrier flags are superseded by their own correction and the settled assets: 16 sovereign DDS files and 21 carrier flag files are present.
3. Historical focus-icon handoff wording that described active family art as pending is superseded by the current focus audit and registrations for the 21 active base and shine icon contracts.
4. Historical focus-loader concerns must be read with the later focus audit: the priority loader avoids meaningful existing trees, while `keep_completed = no` remains a real lifecycle risk for paths that do install.
5. The original external brief `Pasted text(3).txt` was unavailable to the source-map audit. Accepted second-edition specs are therefore the design authority, but an independent hash comparison to that missing brief cannot be claimed.
6. Suggested asset filename aliases remain documentation-only aliases. The current Charter header is `gfx/interface/012_africa/charter_header_plate.dds`; suggested alternate names in older tables are not missing runtime files.
7. Older Africa Is One suggested image filenames differ from the installed dormant filename. The installed GFX registration and asset matrix control.

## Accepted-plan disposition

| Plan family | Disposition |
| --- | --- |
| Core architecture, action matrix, Charter runtime, host proof, RSA, and bounded decision audit | Accepted and implemented on the reachable core surface, subject to lifecycle and balance validation. |
| Event 13 selected-enemy wrapper and late full-promotion severity refinement | Accepted and implemented without editing Event 13 source. |
| Evolution visual tranche | Accepted and installed for Evolutions I through III. |
| Charter GUI, sovereign portraits, achievement triplets, and active focus-family art | Assets installed and registered; runtime visual review and the achievement callsite proof remain open. |
| Independence Wave carrier loading | Accepted with existing tags only; no Event 12 country tag created. |
| Sixteen priority packages | Implemented on existing identities with promotion gates; three conditional host shells remain blocked and the packages are not evidence of full Event 12 completion. |
| Strange formation plan | Deferred behind an unset readiness gate pending real 3D and unit packages. |
| External world-order packages | Deferred behind per-country readiness flags with no setters. |
| The World terminal plan | Deferred behind package settlement and an unset super-event readiness gate. |
| Super-event audio research and production | Scramble and Continental Wars masters produced but dormant; Africa Is One and The World remain blocked. |
| 239-row visual plan | Reconciled through the current matrix statuses; old acceptance-ledger asset dispositions are stale. |
| Documentation cleanup plan | Accepted. `docs/events/012_africa.md` is the release-candidate source of truth and explicitly rejects a full-completion claim. |

## Meaningful validation performed

- Read the accepted Event 012 specs, matrices, source map, release-candidate source of truth, subsystem handoffs, and completion audits.
- Consulted the required offline Paradox wiki pages and vanilla script documentation for events, effects, triggers, focus loading, localisation, scopes, on-actions, decisions, AI, GUI, event targets, and script constants.
- Refreshed narrow read-only HOI4 event inspections for the entry, result notice, priority member, and world response.
- Counted current Event 012 event definitions and checked definition uniqueness and external occurrence.
- Confirmed the three strange-formation gate reads and the absence of a setter.
- Confirmed per-country world-package readiness reads, the terminal super-event readiness read, and the absence of setters.
- Confirmed the active Africa-only Scramble closure does not promote external packages.
- Ran the country-tag collision audit: 136 protected Event 006 and Soviet tags, zero external country-definition collision.
- Confirmed that Event 13 source files are clean while Event 12 supplies the accepted hostile-caller inputs.
- Confirmed the late full-promotion regional-severity code, localisation, and documentation alignment.
- Counted 44 achievement definitions and 132 achievement DDS files.
- Confirmed 16 sovereign DDS portraits and all three base flag sizes for the seven Event 006 carriers.
- Recounted all 239 asset-matrix rows and the exact seven status totals.
- Opened the workbook read-only and confirmed Event 12 remains `In progress` with aligned entry and evolution descriptions; the exported CSV timestamps postdate the workbook.

## Validation not performed

- Hearts of Iron IV was not launched.
- No live save, host transfer, mission timeout, action cancellation, focus replacement, evolution, Scramble, Charter GUI, super-event, sound, or achievement lifecycle was exercised.
- No campaign-length AI or resource-balance simulation was completed.
- No live focus overlay render was accepted by the player.
- No binary visual-quality or audio loudness acceptance review was completed.
- MCP event analysis remained partial because of the size of the combined vanilla and mod workspace.

## Remaining blockers and recommended next actions

1. Run a new-game Event 012 lifecycle through entry selection, first proof, Charter opening, focus installation, one full and one failed action, host transfer, all three evolutions, continental settlement, Scramble closure, and cleanup.
2. Exercise all nine mutually exclusive focus overlays and confirm that only one overlay appears without overlap; resolve the 570 layout diagnostics if the runtime view does not prove exclusivity.
3. Prove that every focus loader is one-shot and decide whether `keep_completed = no` is acceptable before any release claim.
4. Complete the 44-achievement owner-system, milestone, disqualifier, and gated-content callsite audit.
5. Run task-specific AI and balance scenarios for the 64 accepted profiles, high-cost actions, natural-disaster hostility, Scramble responses, priority promotion, and route selection.
6. Keep readiness setters absent until each strange formation, continent package, or terminal super-event package has its real gameplay, AI, localisation, assets, rights, and validation evidence.
7. Promote, reject, or retain the 133 controlled-pool rows explicitly; do not silently convert them into an active completion obligation.
8. Produce the 16 future model packages only through the approved 3D planning and production workflow before enabling their consumers.
9. Finish audio selection and wiring for all four super-event roles, including unique sound IDs, slots, rights manifests, loudness checks, and live playback.
10. Reconcile or archive the stale 809-row acceptance ledger so future audits do not mistake historical blockers for current state.
11. Retain the workbook status as `In progress` until the full-content blockers above are resolved.

## Final classification

- **Finished for narrowed RC:** static event registration, reachable Charter and decision registration, Africa-only Scramble closure, Event 13 wrapper inputs, referenced English localisation, current log and detail integration, current active GFX registration, and existing-tag country loading.
- **Partial:** focus runtime confidence, AI and balance, achievements, priority package proof, GUI runtime behavior, super-event presentation, provenance documentation, and full lifecycle validation.
- **Blocked or safely deferred:** actions 74 through 76, six external continent packages, The World, 16 model rows, 7 unique package rows, two audio roles, and two Afaan Oromoo strings.
- **Design gaps:** no completed world-package identities, no complete strange-formation unit packages, incomplete achievement proof coverage, simplified AI, and no accepted resolution of the focus layout and loader risks.

No full Event 012 completion claim is supported.
