# Event 042 - Equipment from Heavens

Event 042 is a Chaos level 1 Minor Repeatable event rooted at `chaosx.nr42.1`. It selects one uniformly random eligible ordinary country and drops an enormous, deliberately unoptimized military arsenal across its owned and controlled states. The source specification is `docs/specs/042_equipment_from_heavens_specs/`.

The event is registered in `global.repeatable_events`, belongs to the reworked default-enabled set, and is a Low member of the Various Anomalies cluster.

## Event map

| Event | Role |
| --- | --- |
| `chaosx.nr42.1` | Hidden canonical entry. Rechecks or replaces the recipient and opens the single delivery transaction. |
| `chaosx.nr42.2` | Discovery popup with the manifest tooltip; acknowledgment starts recovery. |
| `chaosx.nr42.9` | Sequential hidden recovery visit; applies local effects and schedules the next visit. |
| `chaosx.nr42.10` | Dormant compatibility report, crate-field image. |
| `chaosx.nr42.11` | Dormant compatibility report, vehicle-descent image. |
| `chaosx.nr42.12` | Dormant compatibility report, aircraft-field image. |
| `chaosx.nr42.13` | Final recovery summary, overwhelmed-depot image. |
| `chaosx.nr42.14` | Dormant nuclear-cargo compatibility report, atomic-cache image. |
| `chaosx.nr42.15` | Dormant special-cargo compatibility report, sealed Chaos cargo image. |
| `chaosx.nr42.16` | Final recovery summary including an accident. |
| `chaosx.nr42.17` | Final recovery report when every landing ground has been lost. |
| `chaosx.nr42.18` | Empty-recipient-pool explanation for manual firing. |
| `chaosx.nr42.19` | Hidden stale-chain closer, scheduled 44 days after discovery acknowledgment. |
| `chaosx.nr42.30` | Hidden Tiny Arsenal State pulse, every 30 days while the route is open. |
| `chaosx.nr42.31` | Hidden Borrowed Nightmare expiry check, every 14 days while the route is open. |

## Trigger and runtime flow

1. The shared dispatcher calls `equipment_from_heavens_prepare_random_event_fire` from `fire_event_by_temp_id_no_cluster`. It collects every country passing `equipment_from_heavens_country_is_valid_recipient` into one temporary pool and picks one with `random_scope_in_array`. Every eligible country has exactly equal weight.
2. Eligibility is the shared ordinary-country contract: not `is_special_chaos_country`, not `is_actual_nonhuman_country`, not the CXT test country, at least one passable owned and controlled state, and no open Event 42 landing-report chain of its own. Player status, major status, industry, manpower, army, fuel, supply, geography, ideology, war state, prior deliveries, and need are never read.
3. When no country qualifies, `evaluate_event_pool_candidate_unavailability` returns `equipment_from_heavens_recipient`. The Events tab shows `N/A`, the event leaves the automatic pool, manual and force firing display the empty-pool explanation, and a cluster transaction records the member as skipped with that reason.
4. The dispatcher fires `chaosx.nr42.1` in the recipient's scope. The shared history recorder binds the Event Log sequence to the recipient before the event runs, and the default actor mapping makes the recipient the Event Log actor.
5. The hidden immediate block runs `equipment_from_heavens_open_delivery` once. It resolves the active evolution stage, rolls magnitude, composition group, and provenance signature, builds and grants the manifest, rolls the nuclear and special slots when active, plans the reports, records compact history, applies guarded Chaos, snapshots achievements, and runs the AI assessment for AI recipients.
6. The discovery option shows the manifest through custom tooltips and starts recovery once; it does not grant additional equipment.
7. Three to seven recovery visits run sequentially over roughly two weeks. A hazardous-cargo accident replaces one middle visit, keeping the same site limit. Only one final summary is displayed, including an accident when one occurred, or a halt report if no landing ground remains. The final option closes the chain and clears its transient state. A recipient receives two popups per successful delivery; other countries receive none.

## One transaction

The stockpile grant happens only through the hidden `chaosx.nr42.1` entry. Reports never call a grant, the pacing handler, the repeatable-cap handler, or the Event Log recorder, so they cannot duplicate equipment, history rows, pacing, or weight reduction. Scheduled report events and the persisted recipient arrays survive save and reload unchanged.

Persistent recipient state during a chain:

- flags `efh_chain_active`, `efh_manifest_manual`, and the one-use `efh_pending_manual` marker
- variables `efh_delivery_sequence`, `efh_delivery_date`, `efh_manifest_stage`, `efh_manifest_magnitude`, `efh_manifest_group`, `efh_manifest_signature`, `efh_manifest_scale`, `efh_manifest_nuclear_amount`, `efh_manifest_reroll_count`, `efh_report_next_index`, `efh_report_total`
- arrays `efh_manifest_family_entries`, `efh_manifest_tier_entries`, `efh_manifest_role_entries`, `efh_manifest_amount_entries`, `efh_manifest_designer_entries`, `efh_manifest_special_entries`, `efh_manifest_special_amount_entries`, `efh_report_state_entries`, `efh_report_theme_entries`, `efh_report_day_entries`

After closure only the compact global history remains: `global.efh_history_sequence_entries`, `_delivery_`, `_recipient_`, `_stage_`, `_magnitude_`, `_group_`, `_family_count_`, `_nuclear_`, `_special_count_`, and `_report_count_entries`.

## Manifest construction

The conventional registry is `common/scripted_effects/042_equipment_from_heavens_registry_effects.txt`, generated from one family table and reviewed by hand. It holds 28 families with stable ids, minimum stage, highest safe tier, composition group, quantity class, designer route, and mismatch flag.

| Stage | Families added |
| --- | --- |
| Baseline | infantry, support, artillery, anti-tank, anti-air, rocket artillery (tier 1), trucks, trains, convoys, armored cars, light, medium, and heavy tanks, fighters, close air support, tactical, strategic, and naval bombers |
| Evolution I | mechanized, amphibious mechanized, tank destroyers, self-propelled artillery, self-propelled anti-air, amphibious tanks, heavy fighters, transport planes, advanced rocket artillery |
| Evolution II | modern tanks, super-heavy tanks, and the highest-tier weighting |

Construction order:

1. Magnitude from the stage table: 60/30/10, 50/35/15, 40/40/20, 35/40/25.
2. Composition group with equal weight: infantry, guns, armor, air, logistics, or foreign warehouse.
3. Anchor family drawn uniformly from the group. The foreign warehouse draws from every non-awkward family and receives a reduced anchor share.
4. One to three strategically awkward families drawn uniformly from the fixed awkward pool (anti-tank, amphibious equipment, trains, convoys, strategic and naval bombers, transport planes). The pool is fixed and never reads the recipient's geography or war.
5. Supporting families up to the stage count: 4-8 at baseline, 7-12 at Evolution I, 8-14 at Evolutions II and III.
6. Technology tier per family. The recipient's research only identifies the current tier. Baseline weights are current 55, ahead 30, foreign 10, highest 5. Evolution I uses 20, 45, 10, 25 and "ahead" can mean two generations. Evolutions II and III use 10, 30, 10, 50.
7. Quantity from the family's class band and magnitude, multiplied by the role share (anchor 1.0, foreign-warehouse anchor 0.65, support 0.30-0.55, awkward 0.25-0.45) and the global scale (stage 1.00/1.15/1.25/1.35 times one plus 0.05 per major at war up to 0.20 plus 0.03 per Chaos tier). Values are computed in thousands, clamped to 2,000,000 units per family, and rounded to clean units.

Recipient capacity never lowers any value. A one-state minor and a major draw from identical tables.

## Complete variants under every DLC configuration

With No Step Back, tank families create one neutral complete variant on the recipient (`Unmarked Light Tank`, `Unmarked Medium Tank`, `Unmarked Heavy Tank`, `Unmarked Tank Destroyer`, `Unmarked Assault Howitzer`, `Unmarked Flak Carrier`, `Unmarked Amphibious Tank`, `Unmarked Battle Tank`, `Unmarked Siege Tank`) with explicit turret, gun, suspension, armor, engine, and radio modules, then grant it by variant name. With By Blood Alone, aircraft families do the same (`Unmarked Fighter`, `Unmarked Ground Attack Plane`, `Unmarked Medium Bomber`, `Unmarked Heavy Bomber`, `Unmarked Torpedo Bomber`, `Unmarked Heavy Fighter`). Without the DLC, complete legacy tokens are used. Bare chassis and empty airframes are never granted.

Every designer grant is verified by the stockpile delta of `num_equipment@<token>`. If the delta is below half of the requested amount, the row is rerolled into an unused non-designer family of the same stage and role with its own band, so a technical failure never shrinks the package. Variant names are literal strings so the lookup never depends on the game language. Creating a variant grants no production access, because production still needs the ordinary chassis or airframe research.

## Landing reports

Report count is 3-4 for Enormous, 4-6 for Colossal, 5-7 for Impossible, plus one from Evolution II, clamped to 3-7. The first report is always first discovery and the last is final reconciliation. Middle themes are drawn without replacement from cargo recovery, depot congestion, provenance anomaly, civilian disruption, and advanced cargo when the manifest is evolved or carries nuclear or special cargo. Hazardous nuclear or special cargo adds a 12 percent chance of one recovery accident report.

Discovery selects its image from actual special cargo, atomic cargo, air or armor dominance, and finally ordinary crate fields. Final summaries use the depot image.

States are chosen from owned and controlled states, preferring unused ones and revisiting states only when the recipient has fewer states than reports. Planned visit days are ascending between day 1 and day 14; sequential scheduling keeps at least one day between visits if planned days coincide. A lost state is replaced by another valid state for the actual recovery burden.

Each report applies the single `equipment_from_heavens_landing_zone` dynamic modifier. The burden merges by maximum and caps at 3.0, logistics cargo adds capped relief, and the modifier refreshes its duration rather than stacking. Per burden point it gives -0.5 local supply, -8 percent building speed, and -10 percent infrastructure repair. Durations are 30, 45, or 60 days by magnitude, plus 15 for physical themes.

The recovery accident removes up to one percent of the anchor consignment, limited to equipment still in the stockpile, and deals one level of infrastructure damage in the landing state. The final summary states the actual loss.

## Provenance signatures

One of eleven signatures is chosen per firing and appears in the discovery report. The signature never becomes a meter and never reveals a sender.

## Evolutions

One ordered global track, type 42, with actorless log entries:

1. Everything Falls, Chaos 200+ (tier 1).
2. Arsenal of the Future, Chaos 400+ (tier 2).
3. Chaos Arsenal, Chaos 600+ (tier 3).

`equipment_from_heavens_evolution_pulse` runs from the global host daily hook in `common/on_actions/chaosx_on_actions_chaos_meter.txt`. Only the first unrecorded stage can be pending, and only while every earlier stage is recorded and enabled. When the shared enable and Chaos gate passes, a delay is set from 90 days plus or minus 30, reduced by 5 days per 100 Chaos above the threshold, 15 days if a delivery happened within 180 days, 3 days per major at war up to 15, and 10 days if the previous stage was demonstrated by a delivery, with a 45-day floor. When the delay expires the stage records `efh_evolution_*_recorded` and one Event Log evolution row. Activation grants nothing and changes no Chaos.

The active stage used by a manifest is the highest stage whose chain of recorded stages is still enabled. Disabling a stage returns future deliveries to the lower pool. Existing stockpile, templates, and receipts are never removed. An evolution recorded before the first delivery applies to that first delivery.

## Nuclear caches

From Evolution II a nuclear slot rolls after the conventional manifest: 25 percent at Chaos 400-599, 35 at 600-799, 45 at 800-999, and 55 at 1000+, capped at 55. Quantities are 25-75, 75-150, or 150-250 bombs by magnitude, rounded to five, and granted with `add_nuclear_bombs`.

Launch proof: the vanilla `nuclear_strike` raid in `common/raids/nuclear_raids.txt` is visible when `num_of_nukes > 0` or the nuclear special project is complete, has no technology requirement in `allowed`, and requires ten strategic bombers at an air base, a war with the target, 20 command power, and one bomb as essential equipment. A recipient without nuclear research can therefore launch the received stockpile through ordinary raid rules. No launch-only contract is needed, nothing grants production, research, facilities, special projects, missiles, or thermonuclear access, and the raid type closes when the stockpile reaches zero unless the country has completed the nuclear project. Visibility of an already prepared raid instance still requires live acceptance. Chaos Redux does not override this raid.

Use enters the shared `on_nuke_drop` handlers (Chaos Meter, fallout, and humanitarian) once. Event 42 adds only its achievement receipt there.

## Evolution III special equipment

From Evolution III, 0-3 special families are drawn without replacement with weights 40/40/15/5, clamped to the allowlist. Each allowlisted family receives a hidden fielding receipt technology that only unlocks its battalion, plus one editable neutral template. The registry, evidence, and every excluded family are documented in `docs/events/042_equipment_from_heavens/systems/special_equipment_registry.md`.

## Event-owned Chaos

| Outcome | Change | Guard | History reason |
| --- | ---: | --- | --- |
| First successful skyfall | +2 | `efh_chaos_first_skyfall`, once globally | `special.equipment_from_heavens_skyfall` |
| First cache to a country with no bombs | +10, or +5 if it already had production access | `efh_chaos_first_nuclear_actor`, once globally | `special.equipment_from_heavens_proliferation` |
| First fieldable special family outside its owner | +5 | `efh_chaos_first_arsenal_escape`, once globally | `special.equipment_from_heavens_arsenal_escape` |

Evolution activation, ordinary repeat deliveries, reports, and receipts add nothing. The mass-casualty +10 variant of the escape milestone has no consumer because every payload family is excluded. Actual nuclear use, deaths, contamination, war, and conquest remain with the shared sources.

## AI

AI and players draw from identical tables. After an AI delivery, `equipment_from_heavens_ai_assessment` classifies the manifest once and sets timed flags (365 days) that enable the plans in `common/ai_strategy/042_equipment_from_heavens.txt`:

- armor windfall when fuel ratio is above 25 percent and manpower above 20,000: armor and mechanized production -30, armor role +20
- air windfall when it also owns a controlled air base: all aircraft production -30
- infantry windfall with the manpower margin: infantry, artillery, anti-tank, anti-air, and support production -30
- logistics windfall: trucks, trains, and convoys production -30

The -30 factors keep a domestic replacement line. Families that fail their conditions are counted as reserve or unusable and remain in the stockpile. No manpower, fuel, bases, supply, doctrine, research, commanders, or divisions are granted. Nuclear use relies on the vanilla raid AI, which only weighs potential and current enemies and consumes the finite stock. Special templates exist for the AI to recruit through ordinary logic, and the stockpile bounds how many can be equipped.

## Cluster integration

Various Anomalies is live cluster ID 11, the ID assigned in the authoritative workbook. It is a one-time cluster that unlocks at Chaos level 4 (tier 3). Members are Equipment from Heavens (row 11001, optional, Low, primary trigger) and BOOM (row 11002, event 47, optional, Low, primary trigger). BOOM is still awaiting its rework and stays disabled by default, so its row reports the disabled skip reason.

Event 42 keeps its own level 1 eligibility. Each member has one row, so a transaction can create at most one Event 42 delivery whether it is the root or a member. The cluster counts as one pacing event and records its own cluster history row. Event 42 still records its own history row, fired count, and repeatable-cap reduction. Landing reports add no pacing.

## Event Log and Event Details

- Name `chaosx.event_name.42` is "Equipment from Heavens" in both the log and debug selectors.
- Actor: the recipient through `events_log_set_default_actor_for_current_event`.
- History detail loads the compact record with `equipment_from_heavens_load_open_history_payload` and shows recipient, magnitude, dominant group, landing sites, and whether nuclear or unknown cargo appeared.
- Evolution rows use type 42 with stage titles and bodies in every evolution surface, and the Event Details catalog lists the three stages.
- Unavailable state shows `N/A` with the reason "no ordinary country holds a state where the cargo could land".

## Achievements

| Id | Condition | Tracking |
| --- | --- | --- |
| `042_equipment_from_heavens_tiny_arsenal_state` | Player recipient with fewer than ten factories fields fifty more divisions within a year while holding its capital, then makes a major capitulate or accept its conditional surrender within three years. | Snapshot at delivery, 30-day pulse with an exact final growth-window check `chaosx.nr42.30`, `on_capitulation` and `on_peace_proposal` hooks. |
| `042_equipment_from_heavens_nuclear_lottery` | Player recipient with no bombs and no nuclear production access receives a cache and conducts a strike before gaining production access. | Snapshot after the cache, `on_nuke_drop` receipt. |
| `042_equipment_from_heavens_borrowed_nightmare` | Player recipient receives a special family from a normal delivery before its owner event fires, then wins a land battle within 1095 days with a commander whose army contains that equipment, before the owner event fires. | Snapshot on the first special family, native `on_army_leader_won_combat` callback. |

Safeguards: manual or force-triggered deliveries, AI recipients, and recipients that pass to AI control never qualify. Each route has separate active and completed flags, so a later delivery cannot overwrite an open route. Failed routes clear their state and may reopen on a later valid delivery. Borrowed Nightmare checks the victorious commander's army for the saved equipment type. Stockpile declines, attrition, transfers, defeats, and victories by other armies cannot award it. The director approved this commander-army victory requirement on 6 October 2026. The 14-day pulse only expires the route.

## Runtime files

- Events: `events/042_equipment_from_heavens.txt`
- Constants: `common/script_constants/042_equipment_from_heavens_constants.txt`
- Triggers: `common/scripted_triggers/042_equipment_from_heavens_triggers.txt`
- Effects: `common/scripted_effects/042_equipment_from_heavens_effects.txt`, `_registry_effects.txt`, `_special_effects.txt`, `_achievement_effects.txt`, `_cxt_effects.txt`
- Fielding receipts: `common/technologies/042_equipment_from_heavens_fielding_technologies.txt`
- Landing zone: `common/dynamic_modifiers/042_equipment_from_heavens_state_modifiers.txt`
- AI: `common/ai_strategy/042_equipment_from_heavens.txt`
- Hooks: `common/on_actions/042_equipment_from_heavens_on_actions.txt`, `common/on_actions/042_equipment_from_heavens_cxt_on_actions.txt`
- CXT carrier: `common/ideas/042_equipment_from_heavens_cxt_ideas.txt`
- Scripted localisation: `common/scripted_localisation/042_equipment_from_heavens_scripted_localisation.txt`
- Localisation: `localisation/english/042_equipment_from_heavens_l_english.yml`
- Sprites: `interface/042_equipment_from_heavens.gfx`
- Tokens: every equipment and name token used through variables is registered in `common/synchronized_dynamic_tokens/chaosx_tokens.txt`

Shared owner files touched: event registration and pool reason in `common/scripted_effects/chaosx_logic_effects.txt`, dispatcher in `common/scripted_effects/chaosx_settings_effects.txt`, actor, history binding, evolution previews, and payload loading in `common/scripted_effects/chaosx_events_log_effects.txt`, selectors in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, the reworked allowlist in `common/scripted_triggers/chaosx_settings_triggers.txt`, Chaos history reasons, the evolution pulse hook, the cluster registry, and the achievement registry.

## Assets

Asset provenance, prompts, and review notes are in `docs/events/042_equipment_from_heavens/systems/assets.md`.

| Sprite | File |
| --- | --- |
| `GFX_report_event_equipment_from_heavens_crate_fields` | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_crate_fields.dds` |
| `GFX_report_event_equipment_from_heavens_vehicle_descent` | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_vehicle_descent.dds` |
| `GFX_report_event_equipment_from_heavens_aircraft_field` | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_aircraft_field.dds` |
| `GFX_report_event_equipment_from_heavens_overwhelmed_depot` | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_overwhelmed_depot.dds` |
| `GFX_report_event_equipment_from_heavens_atomic_cache` | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_atomic_cache.dds` |
| `GFX_report_event_equipment_from_heavens_chaos_cargo` | `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_chaos_cargo.dds` |
| `GFX_achievement_042_equipment_from_heavens_<id>` plus `_grey` and `_not_eligible` | `gfx/achievements/042_equipment_from_heavens_<id>.dds` and variants |

The landing-zone modifier reuses the vanilla `GFX_modifiers_generic_construction` icon. All sprites are declared in `interface/042_equipment_from_heavens.gfx`.

## CXT registration

Carrier `chaosx_cxt_extension_event042_equipment_from_heavens` registers `chaosx_cxt_extension_event042_equipment_from_heavens_apply`, which grants the seven fielding receipts and neutral templates to the test country without firing Event 42 or granting a package.

## Limitations

- The HOI4 MCP event inspector traces the Event 42 events on this workspace in focused mode only. Helper projections are deferred, so the dispatcher path through scripted effects is proven by source review and not by MCP helper expansion.
- Whether `create_equipment_variant` with `allow_without_tech` accepts modules the recipient has not researched is not documented. The stockpile-delta verification and reroll keep the package full if the engine rejects a variant, and the in-game check belongs to live testing.
- Tier-4 airframes, jets, and rocket interceptors are outside the registry because their engine and module validity across DLC configurations is unproven.
- Borrowed Nightmare uses the director-approved commander-army battle victory criterion. Native callback execution remains a live acceptance check.
- Required post-change MCP event, probability comparison and shared-detail visual acceptance remain open while the connected routes time out.
- The 5 October live screenshots show the legacy news event, not this package; live acceptance of the rework is pending.

## Future plans

- A mission offering to lend or sell part of an unusable consignment to a faction partner could make the awkward families an active diplomatic choice.
- Additional special families can join the allowlist once their owners expose a fielding split or captured-payload consumer, following the registry contract.
- A compact manifest ledger in Event Details could list the anchor family and tier for each historical delivery.

## Release-review evidence

The owner decisions and exact remaining acceptance gates are in `docs/plans/042_equipment_from_heavens_plans/agent_decisions_2026-10-05.md` and `release_review_2026-10-05.md`.
Catalog wording awaits the catalog owner in `catalog_changes_pending.md`; this task does not edit the workbook or its CSV exports.

A replacement recipient inherits the pending delivery's manual status. A direct entry without prepared context is manual even when rerouted, so retargeting cannot make a forced delivery qualify for an achievement.
