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
