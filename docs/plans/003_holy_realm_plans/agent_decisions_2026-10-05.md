# Event 003 Release QA Decisions, 2026-10-05

This decision log records the scoped source changes accepted for this release-QA pass. It does not promote new route design into the Event 003 specification.

## Accepted and implemented

- The release-QA task requires a readable explanation when a forced Event 003 root has no valid host. `chaosx.nr3.1` now redirects to the selected valid mountain host as before, and sends a visible `chaosx.nr3.5` explanation to the invoking country if selection fails. The existing Tibet-first and Bhutan/Nepal-only-if-Tibet-is-gone rule remains the governing design.
- The release-QA task requires one world-news popup per formation chain. The three mutually exclusive formation paths now call `holy_realm_publish_refuge_news`, which sets one campaign flag before broadcasting `chaosx.news.9`.
- The release-QA task requires readable player prose without bookkeeping or implementation wording. High-visibility Holy Realm event, news, decision, focus, idea, Mandala panel, and event-detail strings were rewritten to describe people, places, actions, costs, and consequences in short sentences.
- The focus filter table in the accepted Buddhahood focus specification lists Bodhi, Teaching, Governance, Compact, Nirvana, and Hidden filters, and the current focus source already provides localized labels for those IDs. The task owner explicitly authorized adding those six existing labels to `search_filter_prios` and assigning them to the matching existing focus blocks. Existing route prerequisites, hidden branches, layout, vanilla filters, and AI weights remain intact.
- Release QA found that the daily doctrine pulse used generic `on_daily`, which iterates every country. The task owner explicitly authorized retaining the mechanic through tag-specific callbacks. The pulse now runs only under `on_daily_TIB`, `on_daily_BHU`, or `on_daily_NEP`, guarded by the Holy Realm flag and power balance.
- The decision audit proved that recurring Bhumi advancement paid the same Political Power, Command Power, and Stability milestones on every later call. These milestone grants are now one-time, constant-backed rewards. The three recurring Black Friday refunds are capped below their maximum discounted quotes, and exact-cost manpower, equipment, and Command Power gates are inclusive.
- The decision audit proved that `THR_hold_dharma_teaching` can recur every 75 days and choose the `nr3.110.b` or `nr3.111.b` Political Power outcome. Those returns are reduced to five Political Power while the teaching, reach, legitimacy, and Bhumi effects remain.

## Implemented through parent integration

- Parent integration added the shared native Black Friday quote `global.black_friday_price_pp_155` and changed the Nuclear Sutra decision to charge the displayed 155 PP total. The hidden extra 25 PP debit was removed. The shared price-table source remains parent-owned.

## Unresolved

- Weighted AI and probability balance remain unvalidated by HOI4 MCP. No AI weight, strategy factor, MTTH, or probability value was changed.
- The focus source contains the accepted navigation taxonomy and the accepted capital-sanctuary prerequisite. Final focus position/render comparison remains with the focus auditor and parent review.
- The pilgrimage escort now cancels during its timer when troops leave or control is lost and refunds its saved paid costs through the native cancel-effect path. Engine timing and cap-limited Command Power refunds remain untested without live play or a successful decision scenario inspection.
# Parent integration

The manual Settings no-host gate calls `holy_realm_report_unavailable_refuge_host`, which sends the event-owned `chaosx.nr3.5` explanation and consumes the shared feedback receipt before the generic fallback.
Automatic selection still rejects an event with no valid mountain host.
The existing full 155 PP Nuclear Sutra payment uses one registered native price, `global.black_friday_price_pp_155`, instead of quoting 130 PP and removing another 25 PP out of view.
The shared price-table version is incremented and the native price remains authoritative for display, affordability, payment, and AI cost evaluation.
At ordinary price the cost is 155 PP, and at the table's 25% payment ratio the whole-point ceiling is 39 PP.
Parent source review confirmed that the three tag-specific daily balance callbacks retain the original `is_holy_realm_country` and `has_power_balance` guards and call `holy_realm_daily_doctrine_balance_pulse`.
The existing separate Bodhisattva pulse remains a distinct callback contract.

## Accepted release-QA follow-up - 2026-10-06

- Parent review accepted the capital sanctuary gate for `THR_buddha_mandate`. The accepted Buddhahood Stage 3 spec at `docs/specs/003_holy_realm_specs/003_holy_realm_buddhahood_specs/specs/holy_realm_buddhahood_spec_part_1.md:79-87` requires protecting the capital sanctuary before the Unshaken Seat, while the prior focus availability checked only the Arhat path. The focus now requires control of the current capital and clearance of the existing 180-day recent-fall flag. Its four support-root prerequisites and coordinates are unchanged.
- Parent review accepted repairing three unreachable existing Bodhisattva decision definitions because each already has a cost, localized action, and completion effect but `visible = { always = no }` and no source caller. The Refuge Circuit follows the existing Bodhisattva teaching unlock, White-Scarf Envoys follows the Buddha path, and Wounded Border follows the guardian mission unlock plus a war or serious chaos threat. Their existing memory flags make each action one-time; no new route family or AI weight was added.
- A read-only weighted-source review found `THR_bodhisattva_hold_teachings_for_refugees` and `THR_bodhisattva_teach_foreign_officers` could continue paying stability, manpower, experience, Command Power, Reach, or other effects after the Bhumi advancement cap. All five Bodhisattva Bhumi actions now use `holy_realm_bhumi_advancement_available`, keyed to the centralized `bhumi_max`, and show the same player-facing cap explanation. Their existing AI weights are unchanged.
- Parent review accepted requiring continuous escort-presence validation for `THR_bodhisattva_guard_pilgrimage_route`. The native timer now cancels if the selected state leaves Realm control or has fewer than two divisions. Cancellation returns the saved PP quote, Command Power, and Support Equipment, withdraws the exact sale receipt when still available, frees the teaching slot, clears the active marker, and retains the established Defilements/Sangha Cohesion penalty. The description explains the troop obligation, refund, and penalty.
- Parent review accepted the current terminal route through Fallout. The terminal completion effect records `world_end_final_silence_completed` and `fallout_cause_final_silence_memory`, then requests maximum-intensity Fallout. The active route queues no Event 003 country or country-wide witness popup; Fallout owns the terminal presentation. The retained `.nr3.73`/`.nr3.90` callbacks are not scheduled by the current `.nr3.80` launch, and slot-9 legacy text describes Fallout without adding a new dispatch. The retired `world_end_final_silence` flag and empty `world_end_scenario_triggered` stub no longer imply a parallel Final Silence launch.
- `holy_realm_can_form_silent_mandala` now excludes the owner's terminal-completion flag instead of the retired global `world_end_final_silence` flag. This preserves the non-terminal-only Mandala path and blocks it as soon as terminal Final Silence records its completion, before Fallout's asynchronous world-end transition finishes.

## Current parent reconciliation, 2026-10-06

Acceptance basis is the user's 2026-10-05 release-QA/G6 direction and parent source/UI/asset acceptance.
Source prepares/reuses the selected refuge host before manual history recording and reports already-founded requests through owned .5 feedback, preserving the host rule.
Both Empty Mandala and the dedicated Final Silence terminal achievement require completed cause memory and actual world_end_fallout; their descriptions/tooltips describe Fallout through Final Silence.
The dedicated achievement retains country/capital-safety criteria, and the launch retains strict Chaos greater than 1000.
The retired public Final Silence row is absent.
Seven sixteen-frame Mandala states and fourteen runtime DDS files match approved digest F55E542C65E2604DB946F58D9FB7ACF599FB9C922058E8486525F95824677F56, superseding pending-promotion and glow-only claims.
The default no-flags Refuge tab has a visible selected cue matching its body.
Final focus geometry and post-asset GUI matrix remain open; the regex self-prerequisite alert was false and no guardians dependency was removed.
The probability handoff records interrupted/no-result inspections and no completed evaluation or compare.
See `release_qa_completion_20261006.md` for current dispositions, source evidence and review gates.

## Parent presentation review, 2026-10-06

The user's G4/G6 direction authorizes the existing five Mandala tabs to filter the main action list.
All 47 existing actions remain present and preserve their costs, availability, effects and AI weights; the filters return true for AI countries independently of tab flags.
The initial nine actions separate into Refuge 3, Arhats 2, Diplomacy 1, Doctrine 3 and Warnings 0, with Refuge selected by default.
The closed-refuge-roads action is hidden from humans before its existing Bodhisattva unlock, while its existing active marker preserves its timer presentation.
The complete mapping and source comparison are in `subagent_handoffs/mandala_tab_filtering_20261006.md`.

The first parent-reviewed position-only tranche separated optional military branches, the teaching side lane, the four Schism responses and the later supernatural and nuclear routes.
At that historical source receipt all 111 definitions were identical outside x/y fields and 62 positions changed; later G6 source transformations below have their own preservation evidence.
The reviewed reference and exact source receipt are in `subagent_handoffs/focus_release_20261006_evidence/parent_geometry_applied_20261006.json`.
The independent straight-line source projection has no node intersections or same-row collisions and reduces crossing pairs from 33 to 12.
These are reference-model results, not production MCP diagnostics, and the remaining projected crossings are unresolved.
Those post-change transport failures are historical.
Fresh production inspection/render of current 03BC410C source succeeded with 111 nodes, 129 links, 12 crossings, 9 long links, 4 through-node links and 8 detours; the four through-node problems await further exact position repair, so layout acceptance remains pending.
Seven native `shortcut` entries with initial position `(20,0)` and no zoom override are applied; Secure the High Passes requires Chaos greater than 600 and revalidates target authorization at completion.
Twelve parent-reviewed filter icons are installed in commit `fc92f2896caa961b87bbc62a865c3d2927b9b815`; their former missing-asset status is superseded.
The six Buddha-milestone AND arrows and three distant chapter-entry arrows are expressed as visible native completion requirements instead of connectors, preserving the gameplay conditions, paths, costs, rewards and AI.
This is an explicit presentation simplification accepted by parent G6 review independently of unresolved broad nested-spec acceptance; the six-milestone formula preserves all nine conditions across the 512-vector source proof.
The historical pre-final F5 native result has 111 nodes/120 links, zero crossings/long links, one Vow-to-Refuse through-node link and one Seal-to-First-Doctrine detour.
The parent applied the final three position-only relocations, yielding source `d584ec8fe5988781fa1b36306a44e01cf3680f89d610d256f4dcf6c343d5f575`; all non-position focus bytes remain identical to F5.
Final D584 inspection with8F2E English source reports111 normal/14 continuous focuses and120 connectors, zero crossing/long/through-node/detour findings and zero focus diagnostics; the matching8400x2904 native render/raster was parent reviewed.
The late Suppress Subjects description fix resolves the quote-description warning without geometry/behavior change.
Focus source/locale/evidence commit is `FOCUS_SOURCE_LOCALE_EVIDENCE_COMMIT_PENDING_PARENT`; broader AI/native-gameplay/spec acceptance remains open.
Parent G6 review accepted accurate Storehouses national-logistics prose: one controlled-Realm supply hub, centralized CP 25/Reach 4 and conditional Cohesion 5.
The free compact-member infrastructure promise is removed without gameplay changes or promotion of unaccepted member-support design; foreign aid remains a future proposal.
The two-key prose correction changes the English hash to `bd034b82f5ec41f7da5b04116b8c5c1258fc47baba7f3dde29427b118240a2b8`; native geometry was reviewed under prior 8F2E and its fields are unchanged.
Default Refuge 1920/UI 1 is parent visually accepted, including its intentional blank risk row; the other four tabs, thresholds and six other promoted Mandala-sheet states remain outside matrix acceptance after the recorded render-budget failures.
The tab-filter/manpower/Open Roads/62-position tranche is committed as `0673d82669248621d4fdacbb1e54140c39fa8563`.

Parent review authorized original portrait art for the anonymous fictional 1936 Bodhisattva incarnation and its stages because the legacy portrait source lineage is absent.
This is an imagined supernatural character, not Siddhartha Gautama, Padmasambhava or another named historical person's substituted identity.
The complete 12-DDS portrait package is accepted, installed and committed as `d92a67c4a885943747fbdb0a982c1fcffbe6e6b0`, with ten static portraits and two parent-authorized eight-authored-pose mirrored animations documented in `subagent_handoffs/portraits_release_20261006.md`.
The unused Final Silence portrait remains outside this active package.
The existing Mandala animation package is a separate accepted consumer and does not establish portrait provenance.

## Refuge resource correction, 2026-10-06

Parent accepted removing only the five flat manpower grants from `THR_white_scarf_relief_caravans`, `THR_second_refuge_register`, `THR_open_refuge_roads`, `THR_bodhisattva_hold_teachings_for_refugees` and `THR_bodhisattva_invite_foreign_pilgrims` under the user's G6 release-QA direction.
These actions created 25,000 to 180,000 recruits without a population or mobilization source; several recur.
Political Power prices, route/availability gates, cooldowns, timers, AI weights and all non-manpower outcomes remain intact, including White-Scarf reductions to Final Silence Pressure/Chaos and the separate 120,000-manpower peacekeeping return.
`THR_open_refuge_roads` is one-time because its existing memory permanently blocks the alternative Close Refuge Roads route; repeating that one-way purchase was the defect.
No other decision received a one-time gate or resource rebalance in this tranche.


## Final focus and Storehouses review, 2026-10-06

Parent acceptance within the user G6 repair authority covers the final focus layout and seven shortcuts in `08a32875eb5e693d52903b0cd88fb35a0d809b1e`.
Six Buddhahood milestone arrows and three distant entry arrows become visible completion checks while retaining every requirement; this presentation simplification removes crossing and long links without removing route content.
Native inspection reports zero crossings, long links, node intersections or layout diagnostics for all 111 focuses.
The High Pass focus authorizes force only above the existing 600 coercive threshold and revalidates that threshold for each eligible target.
The Storehouses wording describes its actual national logistics and conditional cohesion reward; an unsupported promise of free foreign infrastructure is removed under G4/G6, with no new grant or broader design acceptance inferred.


## Graphics decisions accepted on 2026-10-06

The current graphics brief authorizes replacing the oversized decision-row animation with a 34x34 static lotus while preserving the registered aliases.
The five concentration decisions now use that static alias.
Dedicated native-alpha 72x88 BoP sides replace the oversized reused focus images, and the doctrine category uses its bespoke 52x40 art.
The clipped first BoP crops and faint first seal were rejected; final images have intact silhouettes and clear margins.
Five raw flag tooltips surfaced by the required validator received short requirement labels without changing eligibility.
Evidence is docs/plans/gfx_fix_2026-10/003_report.md.
