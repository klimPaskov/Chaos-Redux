# Event 027 agent decisions, 2026-10-04

Disposition: accepted and implemented under the full-authority mandate that the user granted for the Event 027 takeover. Each decision records the choice, its spec basis, and the implementing commit. Items that only a live session can prove are marked needs_live_game.

Commits: `b55edd969` (adoption of the stopped rework plus D1 to D5, D7, D8, D9, D11), `317e43684` (D6), `2a8be6e32` (D10).

## D1. Reopen empty-track assignment with its first mastery step

Decision: `doctrine_research_empty_track_is_verified` delegates to `doctrine_research_native_mastery_adapter_is_verified` again, and the registry-level `doctrine_research_empty_track_adapter_is_verified` checks `doctrine_research_adapter_registry_initialized`, as at the pre-rework HEAD. The stopped thread's `always = no` closure is not adopted.

Basis: the spec README, part 1 and part 2, and the acceptance criterion "An empty track can select one eligible subdoctrine and receive its first event mastery step". The closure was an evidence gate, not a design change, and it removed every fresh-track page (`.60` to `.77`) after a Grand Doctrine adoption and made First Lesson and Single School unreachable.

Implementation: the existing transaction (`set_sub_doctrine` with folder and numeric track index, post-assignment level readback written to the receipt pre-level, `adoption_only`/`.13` when stored mastery completes the branch, then the one-step loop) runs unchanged. The `.7` confirmation has its own empty-track text (`doctrine_research.confirm.assign_mastery`). The AI reaches the same subdoctrines through `doctrine_research_selected_empty_subdoctrine_is_valid`.

Source trace for the achievements: after an adoption every track of that domain is empty, so the next choice in the same batch takes the empty-track path, produces a consumed mastery receipt with a positive post-level, and satisfies First Lesson. In an Evolution IV batch an empty track yields a 0 to 1 receipt followed by four ordinary steps to level 5, which satisfies Single School.

needs_live_game: `set_sub_doctrine` on an empty track with folder and index, and the banked-level readback after it.

## D2. Per-country firing isolation and ledger repair

Decision: all-or-nothing publication is replaced. The recipient scan initialises and validates each candidate's ledger inside the `every_country` block, repairs a corrupt ledger by discarding its unused rows and receipts without compensation (`doctrine_research_repair_country_state`), and leaves out only a country whose ledger still fails. Each append is isolated; the firing commits whenever at least one batch was published, records one actorless History row with the firing size, and wakes every published country. A firing with no recipient records one payload-zero row and wakes nobody.

Basis: spec part 1, "Every live country with at least one valid registered doctrine action receives one batch".

Source trace of the counterexample: country A has a valid ledger and country B a misaligned one. In the scan A passes and is added; B's initialisation sets the corrupt flag, the repair discards B's rows and clears the flag, and B is added with an empty ledger. Both append a queued row, the binder wakes both, and A's `.14` wake starts A's batch.

## D3. Daily evolution pulse after the first firing

Decision: `doctrine_research_evolution_pulse` runs `doctrine_research_process_evolution` from each global-host branch of `chaosx_on_actions_chaos_meter.txt`, only after `doctrine_research_fired_once`. The tag-switch branch reconciles the former host before clearing its marker and the new host after setting it.

Basis: spec part 3, promotion about 90 days after eligibility; the first firing still opens at the highest enabled stage.

## D4. Mastery point guard at one level's reward cost

Decision: the one-point loop stops at the reward cost of the level being reached: `mastery_point_loop_limit = 100` (DEFAULT_REWARD_MASTERY in vanilla `00_defines.lua`, also the Chaos Warfare thresholds), `special_forces_mastery_point_loop_limit = 60` (every reward in vanilla `special_forces_subdoctrines.txt`), and `peoples_war_short_level_point_limit = 50` for People's War levels 1, 2, and 4, with level 3 (`peoples_war_full_cost_level`) at 100.

Basis: the spec's one-step rule. A readback that does not update in the same effect now ends as ambiguous after crossing the target threshold once instead of granting about ten levels. Residual edge: a People's War step to level 3 with at least 50 points of partial progress can also cross level 4 if the readback lags.

needs_live_game: whether `has_mastery_level` updates in the same effect after `add_mastery`.

## D5. One re-prompt and bounded lifecycle work

Decision: lifecycle reconcile returns before any ledger work for countries without a ledger, an active batch, or queued rows, and re-prompts a human only when no Event 027 page is open (the prompted flag), including the `adoption_only` case, so repeated state-control callbacks produce exactly one `.13` page. Closed batches are compacted before the next batch opens, keeping the most recent closed row, and achievement checks read only the active or closing batch.

Basis: spec part 1 persistence rules and the `MAX_EFFECT_ITERATION = 1000` limit.

## D6. AI domain weights follow real capability

Decision: Navy scores zero without a coast, dockyards, ships, convoys, or naval doctrine; its war term needs warships and a war without a land front, and its geography term a coastal capital. An industry focus term goes to Navy when dockyards times 2 reach the military factory count and to Army otherwise. Army takes the land-front war and geography terms. Special Forces readiness, war, production, and alliance terms need Special Forces templates (including marine commandos), and Grand Doctrine and subdoctrine scoring use the same readiness. Air terms need deployed air wings. When no domain scores, every valid domain falls back to the base weight. Human and AI validity pools are unchanged.

Basis: spec part 3 AI strategy and the DR-A scenarios in `027_doctrine_research_probability_scenarios.md`. Evidence: `probability_domain_compare_2026-10-04.md`.

## D7. National Breakthroughs cooldown

Decision: cluster 9 uses `event_cluster_cooldown_days.national_breakthroughs = 120`, both shared gate blocks reject it while `event_cluster_national_breakthroughs_cooldown` is set, and the cooldown branch sets the flag with the days passed through a temp variable.

Basis: the shared cluster contract followed by every other positive repeatable cluster.

## D8. Event Details text keeps the choice-count premise

Decision: the Event Details description that explains the one-to-five choice range is kept. It states the premise without raw effects, which settles the open mechanics-versus-premise question.

## D9. Adoption of the stopped thread's rework

Decision: the stopped thread's direct dispatch, firing envelopes, History binder, `.14` wake, receipt alignment and replay guards, AI zero-choice closure, achievement debug exclusions, grouped level getter, caller-side temp declarations, cluster 9 with row 9001, Event Details and evolution selectors, and preview rows are adopted. Only Event 027 hunks of shared files were committed; Equipment from Heavens, Various Anomalies, and Acid Rain hunks stay uncommitted. The settings dispatch arm was rebuilt from HEAD plus only the Event 027 `if`/`else` wrapper.

## D10. Special Forces mastery with both tracks occupied

Decision: Special Forces grants and readbacks filter by folder and subdoctrine only. While both tracks are occupied, the first Special Forces entry and page (labelled "Special Forces") cover the active subdoctrines of both tracks and the second entry stays hidden. Receipts keep the selected track label, and Joint Curriculum and the batch summary count Special Forces progress per subdoctrine. Empty-track candidates exclude a token whose xor sibling holds a track; assignment keeps the numeric `set_sub_doctrine` index.

Basis: vanilla `special_forces_subdoctrines.txt` (each token lists both tracks and is xor-locked with its sibling) and the "fully adapted or explicitly absent" adapter criterion. Known display limit: the first track's Milestone readback reads the first native track even when the advanced token sits in the second.

needs_live_game: two Special Forces tracks never holding the same token.

## D11. Catalog changes are recorded, not applied

Decision: the workbook changes are listed in `catalog_changes_pending.md` for the workbook owner; agents do not edit the xlsx or the exported CSVs.

## D12. A reached stage applies only while its own setting is enabled

Decision: `doctrine_research_prepare_firing_profile` sizes each firing from the highest reached stage whose Event Details setting is still enabled (`doctrine_research_evolution_i_setting_enabled` to `_iv_setting_enabled`), instead of the raw reached stage. Switching Evolution IV off after it was reached makes the next firing use Evolution III, or the highest lower stage that stays enabled; batches already created keep their stored stage and size. The reached stage itself, the promotion clock, and the recorded evolution rows are unchanged.

Basis: spec part 3, "Every stage's availability, record, and effect must check its own enabled state", and the acceptance criterion "Event enable and disable state controls automatic selection and evolution gates cleanly". The round 1 profile read the reached stage directly, so a disabled stage kept enlarging every later batch. Found in the round 1 review; implemented in the review commit.

## D13. One opening page after a suspended curriculum

Decision: the `.12` continue option starts the next curriculum when none is active, and otherwise opens `.2` only when no Event 027 page has been shown for the active curriculum (the prompted flag). A `.14` wake or a lifecycle callback that already opened the next curriculum while `.12` was waiting no longer produces a second `.2` page.

Basis: D5 (exactly one open page per curriculum). Found in the round 1 review; implemented in the review commit.
