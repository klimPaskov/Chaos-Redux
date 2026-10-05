# Event 027 Doctrine Research

Event 027 is a global Minor Repeatable event. Each firing gives every live country that has at least one valid doctrine action a curriculum batch of doctrine choices. A choice either establishes one eligible Grand Doctrine for free or advances one eligible subdoctrine by exactly one mastery level.

The source design package is `docs/specs/027_doctrine_research_specs/`. Agent decisions taken while finishing the rework are recorded in `docs/plans/027_doctrine_research_plans/agent_decisions_2026-10-04.md`.

## Files

| Surface | Path |
| --- | --- |
| Events (`chaosx.nr27.1` to `.14`, track pages `.60` to `.77`) | `events/027_doctrine_research.txt` |
| Firing, queue, transaction, lifecycle, and AI domain scoring | `common/scripted_effects/027_doctrine_research_effects.txt` |
| AI Grand Doctrine, track, and subdoctrine scoring | `common/scripted_effects/027_doctrine_research_ai_effects.txt` |
| Native mastery adapter (level readback, one-point steps, empty-track assignment) | `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt` |
| Achievement tracking | `common/scripted_effects/027_doctrine_research_achievement_effects.txt` |
| Test-country setup | `common/scripted_effects/027_doctrine_research_cxt_effects.txt`, `common/on_actions/027_doctrine_research_cxt_on_actions.txt` |
| Validity, adapter, terrain, and AI capability triggers | `common/scripted_triggers/027_doctrine_research_triggers.txt`, `common/scripted_triggers/027_doctrine_research_terrain_triggers.txt` |
| Constants | `common/script_constants/027_doctrine_research_constants.txt`, `common/script_constants/027_doctrine_research_terrain_states.txt` |
| Lifecycle callbacks | `common/on_actions/027_doctrine_research_on_actions.txt` |
| Display text | `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt`, `localisation/english/027_doctrine_research_l_english.yml` |

Shared wiring lives in `chaosx_settings_effects.txt` (direct dispatch arm), `chaosx_events_log_effects.txt` (History binder and evolution previews), `chaosx_scripted_localisation_events_log.txt` and `chaosx_scripted_localisation_settings.txt` (cluster, evolution, and History selectors), `event_cluster_constants.txt` and `chaosx_event_cluster_effects.txt` (cluster 9), `chaos_redux_achievements.txt`, and `chaosx_on_actions_chaos_meter.txt` (daily evolution pulse and tag-switch reconcile).

## Participation

A country takes part while it is live (it exists and has not capitulated, or it is a government in exile), has a doctrine system, and has at least one valid doctrine action (`doctrine_research_country_has_valid_action`). Ordinary countries, subjects, governments in exile, and human special countries such as The Revolution (REV) or the cannibal warlords take part through the normal doctrine graph. An actual nonhuman country, as classified by the shared `is_actual_nonhuman_country` trigger (zombie outbreaks, Black Plague rats, Death, wendigo cannibals, nonhuman Infantry Spawn derivatives, and the other listed families), has no doctrine system and receives no batch and no fabricated doctrine (`doctrine_research_country_has_doctrine_system`). A Kruger sovereignty keeps its doctrine graph even when its population is no longer human.

The same trigger gates the firing scan, the event's availability check, the wake, lifecycle reconcile, AI resolution, and the human pages. A country that becomes nonhuman while it still holds a batch closes that batch through the ordinary no-action path: an AI completes it without spending its choices, and a human sees the `.11` closure page. The domain menu, the selected-domain check, and the confirmation (`doctrine_research_selected_choice_is_valid`) read the same doctrine-system trigger, so a page that was already open when the change happened cannot confirm a new choice: the domain menu shows only its closure option, and a Grand Doctrine, track, or subdoctrine page that is still open leads to a confirmation that offers only the review path to `.11`. A pending receipt still recovers. No compensation is granted.

## Firing

1. The shared dispatcher `fire_event_by_temp_id_no_cluster` calls `doctrine_research_fire_global_batch` directly for Event 027. The root event `chaosx.nr27.1` remains the console bridge to the same transaction and marks its campaign as a forced setup for achievements.
2. The transaction resolves the evolution stage, fixes the batch size for this firing (1 at baseline, 2 to 5 at Evolutions I to IV), and appends one global firing envelope with its ID, stage, size, date, History sequence, and status.
3. One `every_country` scan visits each country with a valid doctrine action. Inside that scan each candidate initialises its own ledger, checks that its batch and receipt columns line up and that every receipt points at a retained batch, and repairs a damaged ledger by discarding its unused rows and receipts without compensation. Only a country whose ledger still cannot be repaired is left out.
4. Each recipient appends one queued batch row with its own batch ID, the firing ID, stage, size, remaining choices, creation date, human-start marker, and a snapshot of which domains were empty. A country that cannot take its row is simply absent from the published list; no other country's row is touched.
5. The firing records one actorless History row whose payload is the firing size. The History recorder calls `doctrine_research_bind_firing_history`, which stores the History sequence on the envelope and sends the hidden wake `chaosx.nr27.14` to every published country. If no country received a batch, the attempt still records one History row with payload zero and wakes nobody.

Batch stage and size never change after creation. Later firings append new rows rather than merging with queued or active work, and countries created after a firing receive nothing for it.

## Queue

The wake starts the oldest queued batch when no batch is active. A per-country queued-row count lets lifecycle callbacks skip countries with nothing to resume. Before a new batch opens, closed batches are compacted: every completed or quarantined row except the most recent closed one is removed together with its receipts, so ledger scans stay bounded by the queue.

## Choices

Human countries move through these pages:

- `.2` opens the batch and `.3` chooses a domain.
- `.4` chooses a Grand Doctrine for a domain without one.
- `.5` chooses a track. `.6` routes to the track's page among `.60` to `.77`, which lists eligible subdoctrines in native graph order with two-page navigation for the longest lists. Page changes spend nothing.
- `.7` confirms. Adoption, mastery on an assigned track, and assignment of an empty track each have their own confirmation text.
- `.8` reports the result, `.9` continues the batch, `.10` summarises a finished batch, `.11` covers states with no remaining action, `.12` reports an interrupted transaction, and `.13` reports that stored mastery completed a branch as it was assigned.

Every page shows the remaining choices. AI countries use the same validity triggers and resolve their whole batch in script.

A confirmation runs one receipt transaction:

- Adoption calls `set_grand_doctrine` for the selected native Grand Doctrine and spends the choice only when the doctrine is then active. It never replaces an active Grand Doctrine.
- Mastery on an assigned track reads the branch's native level, adds mastery one point at a time, re-reads the level after every point, and succeeds only when the branch reaches exactly the next level.
- An empty track first receives the selected subdoctrine through `set_sub_doctrine` with its folder and numeric track index. The level is read again, written to the receipt as the pre-level, and the same one-step loop runs. When stored mastery already completes the branch on assignment, the assignment stands, no choice is spent, and `.13` explains the result.

The one-point loop stops at the reward cost of the level being reached: 100 by default and for Chaos Warfare, 60 for Special Forces, and 50 for People's War levels 1, 2, and 4 (`doctrine_research_prepare_transaction_step_limit`). When the country's folder, active Grand Doctrine, track, and subdoctrine mastery gain factors (read through `modifier@<doctrine>_mastery_gain_factor`) sum below zero, the guard is that cost divided by one plus the sum, rounded up and capped at twice the cost (`mastery_point_guard_cap_multiple`), so a country with reduced mastery gain, such as France with the land factor -0.15, still reaches the level (118 points for an Army step). A sum of zero or above leaves the guard at the reward cost. If the level readback does not update inside the effect, the transaction ends as ambiguous after crossing the target threshold once, spends no choice, and quarantines the batch.

Every `<doctrine>_mastery_gain_factor` name read through `modifier@` is a dynamic token, so all 125 of them (4 folders, 12 Grand Doctrines, 14 tracks, and 95 subdoctrines) are pre-registered in `common/synchronized_dynamic_tokens/027_doctrine_research_tokens.txt` to keep multiplayer games in sync; a new `modifier@` read in an Event 027 effect adds its name there.

Receipts record batch, choice number, action, domain, Grand Doctrine, track, track index, subdoctrine, and pre- and post-levels. A pending receipt is recovered only by its exact receipt ID, batch, and choice number; anything that cannot prove its outcome fails closed.

## Domains

| Domain | Native folder | Tracks | Notes |
| --- | --- | --- | --- |
| Army | `land` | Infantry, Combat Support, Armor, Operations | Folder-owned emptiness checks keep Army and Chaos Warfare tracks apart. |
| Navy | `naval` | Submarines, Screens, Carriers, Capital Ships | |
| Air | `air` | Fighter, Strike, Medium, and Heavy Aircraft | |
| Special Forces | `special_forces` | First and Second Special Forces | Requires the installed DLC and technology gates. |
| Chaos Warfare | `land` | Infantry, Combat Support, Armor, Operations | Requires the CBRN establishment package and its native requirements. |
| Future custom | disabled | none | No action until a complete adapter is registered. |

Every Special Forces token lists both Special Forces tracks, is xor-locked with its sibling, and can occupy only one track at a time, so Special Forces mastery is granted and read by folder and subdoctrine. While both Special Forces tracks are occupied, the first Special Forces entry, labelled "Special Forces", covers the active subdoctrines of both tracks and the second entry stays hidden. Empty-track candidates exclude a token whose sibling already holds a track. A Special Forces entry reports the Milestone of the token it shows, because completing a token completes whichever track holds it.

## AI

The AI picks a domain, then a Grand Doctrine or a track and subdoctrine, each through a weighted `random_list` over positive scores. The pool is recalculated after every successful choice. Domain scores read capability that belongs to each domain:

- Army: divisions, land templates, military factories, war with divisions, a land front, alliance membership, and the industry focus term when neither dockyards nor aircraft lead war industry.
- Navy: scores zero without a coast, dockyards, ships, convoys, naval doctrine, or a maritime plan. A landlocked country has a maritime plan when it holds a core or claim on a coastal state it does not control, or has or is justifying a war goal against a country that owns a coastal state (`doctrine_research_ai_has_maritime_plan`, read only after every other naval check fails); the plan gives Navy the base and strategy weights. Otherwise warships, dockyards, the industry focus term when dockyards times 2 reach the military factory count, a war without a land front, a coastal capital, and alliance membership with warships add weight.
- Air: deployed air wings, military factories, and war or alliance membership with air wings. Air industry leads when deployed planes reach 50 per division (`doctrine_research_ai_ratio.air_industry`) and dockyards do not lead; such a power gives Air the industry focus term instead of Army, and its Air also takes the land-front term, because it fights its land war largely from the air.
- Special Forces: readiness, war, production, and alliance terms need templates that field Special Forces battalions. Coast or mountains add a geography term.
- Chaos Warfare: CBRN programme readiness, divisions, plains or mountains, and a land front.

Completion value and strategy signals add weight in every domain. If no domain scores at all, every valid domain falls back to the base weight, so a choice is never wasted. All weights live in `doctrine_research_ai_weight` and the dockyard and aircraft ratios in `doctrine_research_ai_ratio`.

Grand Doctrine and track scores read only terms that differ between the candidates of one pool; country-wide terms such as divisions, factories, war, coast, and faction stay in domain scoring.

- A Grand Doctrine adds the forces weight for the formations it serves: Mobile Warfare for motorised or mechanised forces and again for tanks, Superior Firepower for line or support artillery, anti-tank, or anti-air (`doctrine_research_ai_fields_fire_support`, the same family the Army Combat Support track reads), Grand Battleplan for a defensive war, forests, or mountains, Mass Assault for infantry without mobile templates, militia, or irregulars, and each naval, air, Special Forces, and Chaos Warfare Grand Doctrine for its own ships, planes, battalions, or CBRN programme.
- A track scores the base weight, force fit (`doctrine_research_ai_selected_track_has_force_fit`: its own templates, ships, or planes, a current war for Army Operations, the battalion family of the held Special Forces subdoctrine, and each Chaos Warfare track's own fielded CBRN battalions read through `num_battalions_with_type@`: the battalions its subdoctrine earns mastery from and the companies its bonuses serve), one investment point per level already earned, an empty-track bonus when an empty track fits, completion value when the branch is one step from completion and fits, and continuity with the previous choice of the batch. The sum is squared, so a clearly better branch wins most choices, close branches stay close, and every valid branch keeps a positive weight. A near-complete branch without matching formations keeps only its investment value.

Grand Doctrine and subdoctrine scores also follow the native doctrine preferences of vanilla `ai_will_do`, mirrored in the `doctrine_research_ai_native_grand`, `_base`, `_country`, `_minor`, and `_major` constant categories:

- Grand Battleplan starts from base 2, and Convoy Raiding and Battlefield Support score ten times higher for a country that is not a major. A minor skips Mobile Warfare and Superior Firepower unless it fields armour or motorised templates or they are its only valid Army Grand Doctrines.
- `doctrine_research_ai_score_selected_subdoctrine_fit` gives each naval, air, and Special Forces subdoctrine the forces term only for its own ship, plane, or battalion type (Marines also read a coast and Mountaineers mountains), then applies the native base, original-tag, minor, and major factors. A candidate that vanilla would never pick keeps the base weight, so every valid choice stays possible.

Evidence: `docs/plans/027_doctrine_research_plans/probability_native_preferences_2026-10-05.md` and `probability_track_round2_2026-10-05.md`.

## Evolutions

| Stage | Chaos tier | Batch size |
| --- | --- | --- |
| Calm World | below tier 1 | 1 |
| Evolution I | tier 1 | 2 |
| Evolution II | tier 2 | 3 |
| Evolution III | tier 3 | 4 |
| Evolution IV | tier 4 | 5 |

The first firing opens at the highest stage the Chaos Meter has already enabled. After that, `doctrine_research_evolution_pulse` runs once a day from each global-host branch of the Chaos Meter coordinator. It touches only global variables. A stage that becomes eligible is promoted 90 days later (converted through `chaosx_convert_days_to_date_offset`), one stage per interval, and disabled stages are skipped. Each promotion records one actorless evolution row. While Event 027 itself is disabled in the event settings the pulse does nothing, so no stage is promoted or recorded for an event that cannot fire; it resumes from the stored clock once the event is enabled again.

Each firing then sizes its batches from the highest reached stage whose own Event Details setting is still enabled (`doctrine_research_prepare_firing_profile` with the `doctrine_research_evolution_*_setting_enabled` triggers). A stage switched off after it was reached stops enlarging new batches, while lower reached stages that stay enabled still apply; batches already created keep their stored stage and size.

## Lifecycle

All batch, receipt, choice, and achievement state is owned by the country and never transfers. State control, puppet, release, subject, government, exile, reinstatement, and civil-war callbacks reconcile the affected country: an AI resolves its active batch, a human without an open Event 027 page is shown it once, and a country without active or queued work returns before any ledger work. On a player tag switch the former host is reconciled before its global-host marker is cleared and the new host after it is set. Annexation discards the annexed country's unused batches and receipts.

## National Breakthroughs

Cluster 9 contains one runtime member, row 9001 for Event 027 (optional, Medium severity, Calm World gate). The other accepted members (54, 65, 67, 83, 85, 89) join when their own reworks are implemented. The cluster uses the shared 120-day cooldown.

## Event Log and Event Details

The History row shows the firing size through five saved-size descriptions. Event Details shows the premise and four evolution previews, and the evolution type, title, and body selectors cover every shared evolution view.

## Achievements

| Achievement | Requirement |
| --- | --- |
| `027_doctrine_research_first_lesson` | In one human batch of at least two choices, adopt a Grand Doctrine in a domain that was empty when the batch began, then advance a subdoctrine in that domain. |
| `027_doctrine_research_single_school` | In one human Evolution IV batch, spend all five choices advancing one branch one level each, ending at level 5. |
| `027_doctrine_research_joint_curriculum` | In one human batch of four or more choices, advance more than three distinct tracks. Special Forces progress counts per subdoctrine. |

Evidence comes only from consumed receipts of the active or closing batch. Debug, console, cluster-forced, and test-country setups are excluded.

## Icons and sprites

| Sprite | Texture | Registered in |
| --- | --- | --- |
| `GFX_report_event_027_doctrine_research` | `gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds` | `interface/027_doctrine_research.gfx` |
| `GFX_achievement_027_doctrine_research_first_lesson` with `_grey` and `_not_eligible` | `gfx/achievements/027_doctrine_research_first_lesson*.dds` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_027_doctrine_research_single_school` with `_grey` and `_not_eligible` | `gfx/achievements/027_doctrine_research_single_school*.dds` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_027_doctrine_research_joint_curriculum` with `_grey` and `_not_eligible` | `gfx/achievements/027_doctrine_research_joint_curriculum*.dds` | `interface/chaosx_achievements.gfx` |

Doctrine options reuse the native doctrine icons from the active doctrine definitions, including the Chaos Warfare icons. Asset provenance is in `docs/assets/027_doctrine_research/manifest.md` and `gfx_handoff.md`.

## Integration

A successful adoption calls Event 016's `brilliant_scientist_record_doctrine_research`, which records the decision once in an active Kruger host's policy history. Event 027 is in the default reworked-event enable list, and its catalog row is maintained through `docs/plans/027_doctrine_research_plans/catalog_changes_pending.md` until the workbook owner applies it.

## Validation limits

These behaviours depend on the live engine and are checked in a live session:

- `has_mastery_level` updating in the same effect after `add_mastery`, which the one-step loop relies on;
- whether `add_mastery` applies `<doctrine>_mastery_gain_factor`; the guard is scaled for a negative factor sum, so the step reaches its level in either case, and with a lagging readback and unscaled grants a country with a negative sum and partial progress above the scaled margin could cross a second level;
- `set_sub_doctrine` with a folder and numeric index on an empty track, and the banked-mastery level read after it;
- two Special Forces tracks never holding the same token;
- receipt recovery across save and reload, and lifecycle callbacks after tag switches;
- the AI domain mix, track mix, and branch completion rate in real campaigns.

## Future plans

- Register further doctrine domains only through a complete adapter: native folder, Grand Doctrine and track identities, one-step mastery steps, AI selector, cleanup, and localisation.
- Add the remaining National Breakthroughs members as their reworks land.
- Read focus-route naval plans, such as planned dockyard construction, once their owners expose them as country flags, so a landlocked country can also value Navy for a plan that has no core, claim, or war goal yet.
