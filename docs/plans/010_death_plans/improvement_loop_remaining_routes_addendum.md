# Event 010 Death Remaining Routes Addendum

Status: implemented and closed by the parent Event 010 Death implementation.

Closure note: this plan is retained as design and audit history. The named route packages were implemented and promoted into `docs/events/010_death.md`, `docs/specs/010_death_specs/specs/010_death_decisions_ui_ai.md`, `docs/specs/010_death_specs/specs/010_death_country_package_and_focus_tree.md`, and `docs/specs/010_death_specs/specs/010_death_assets_super_events_achievements.md`.

Scope: Dark Methods, Black Oath, Herald of Zol, Black Apostolate, Black Atlas UI, route achievements, asset and animation handoffs, and route connections that deepen the existing Death package without turning it into a second event.

Do not treat this as a request for another broad Death focus-tree pass. The current fixed-purpose DTH focus tree is deep enough for Death itself. The remaining depth belongs on the living-country response layer and the forbidden-route layer.

## Implementation Disposition

| Item | Final disposition | Evidence |
| --- | --- | --- |
| Focus tree depth follow-up | Implemented and promoted | The active 26-node tree covers Shroud, Hunger, Census, Public Death, Coastal, Wasteland, Host, Last Shores, and World Consumed. |
| Dark Methods | Implemented and promoted | Decisions, helpers, AI gating, localisation, achievement hooks, cleanup, and Black Atlas values are active. |
| Black Oath | Implemented and promoted | The route is a hard alternate response path with Zol contact, oath-taking, Herald state, compact lockout, debt/favor, betrayal pressure, and cleanup. |
| Herald of Zol | Implemented as the Black Oath route state | Cosmetic identity, flags, ideas, diplomacy posture, decision unlocks, and Death targeting exceptions are active. |
| Black Apostolate | Implemented as hidden Herald culmination | The proclamation route, cosmetic identity, achievement state, route consequences, and no-restoration boundary are active. |
| Black Atlas UI | Implemented | The scripted GUI summarizes Death and forbidden-route values while decisions remain the authoritative action surface. |
| Route achievements | Implemented | `death_friend_of_zol`, `death_book_burner`, and `death_black_apostolate` are defined, localised, wired, and backed by DDS triplets. |
| Optional animated Zol and Atlas animation | Implemented with static fallbacks | Animated packages use frame sheets, source frames, contact sheets, previews, manifest entries, and `.gfx`/`.gui` wiring. |
| Optional Herald/Black Oath super-event | Implemented for Black Oath after research | Researched title/option/quote/audio/image documentation is recorded; the Apostolate remains a hidden route culmination without a separate final super-event requirement. |

## Design Boundary

Keep the remaining scope focused on two living-country forbidden paths:

1. Dark Methods: a living state fights Death by using records, bound names, dead-zone rites, and state secrecy. It gives emergency tools against Death but risks exposure, mourning debt, and political collapse.
2. Black Oath: a living state bargains with Zol and becomes a Herald. It is not Death's friend in a normal diplomatic sense. It buys limited reprieve and forbidden favors by sacrificing moral standing, population safety, and future sovereignty.

Black Apostolate is the hidden end of the Black Oath path. It should feel like a government becoming the administrative church of the end, not like forming a new great-power tag.

Do not add:

- A new DTH focus branch.
- A normal Death faction or permanent alliance.
- Population restoration in wastelands.
- Free cores over living states.
- A generic necromancer fantasy army loop.
- A world-scan daily/on-weekly system.
- A second scripted GUI that duplicates every decision action.
- More route achievements beyond the Black Book, Herald, and Apostolate coverage.

## Research And Theme Basis

Use these as historical and cultural inspiration, not as claims that Death is adapting a specific real institution:

- Wartime graves registration, casualty rolls, and missing-person offices give Dark Methods a bureaucratic tone. The horror is the state treating names, remains, roads, and ports as usable strategic inventory.
- Emergency censorship and quarantine administration justify the route's public-disgust and exposure costs. The player is not merely "casting spells"; they are building a hidden state office that can be discovered.
- Funerary books, rolls of the dead, and oath traditions can inspire Black Book and Last Name wording, but avoid direct religious quotation unless the super-event text researcher separately approves it.
- "Apostolate" should mean a mission-bearing office of the end. It can borrow the structure of a ministry, order, or mission without presenting a real faith as Death worship.
- Zol should remain sparse and administrative: debt, names, ports, ledgers, silence. Avoid comic villain language, gore spectacle, and direct exposition of what Zol "really is."

## Implementation Surfaces

Likely files to touch if this addendum is accepted:

- `common/script_constants/010_death_constants.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/scripted_triggers/010_death_triggers.txt`
- `common/decisions/010_death_decisions.txt`
- `common/decisions/categories/010_death_categories.txt`
- `common/scripted_guis/010_death_black_atlas_scripted_gui.txt`
- `interface/010_death.gfx`
- `interface/010_death_black_atlas.gui`
- `common/ideas/010_death_ideas.txt` or the existing Death section in `common/ideas/chaosx_ideas.txt`
- `common/achievements/` or the existing Chaos Redux achievement file used by Event 010
- `common/country_tags/`, `common/cosmetic_tags/`, or existing cosmetic-tag surfaces only if the project already uses them for route identity
- `common/characters/DTH.txt` only if Zol/Herald trait references need display support
- `localisation/english/010_death_l_english.yml`
- `localisation/english/*achievement*` files used by Chaos Redux
- `docs/assets/010_death/generated_art_manifest.md`
- `docs/events/010_death.md`
- `docs/specs/010_death_specs/010_death_decisions_ui_ai.md`
- `docs/specs/010_death_specs/010_death_country_package_and_focus_tree.md`
- `docs/specs/010_death_specs/010_death_assets_super_events_achievements.md`

No spreadsheet edits should be made until implementation facts and final localisation wording exist.

## Shared Helper Plan

Add constants before tuning gameplay values. Suggested categories:

- `death_dark_methods_cost`
- `death_dark_methods_tuning`
- `death_dark_methods_ai`
- `death_black_oath_cost`
- `death_black_oath_tuning`
- `death_black_oath_ai`
- `death_black_apostolate_tuning`
- `death_black_atlas_ui`

Add trigger helpers:

- `death_can_see_forbidden_methods`
- `death_can_open_black_book`
- `death_can_use_dark_method`
- `death_can_burn_black_book`
- `death_can_contact_zol`
- `death_can_take_black_oath`
- `death_is_herald_of_zol`
- `death_can_offer_prison_census`
- `death_can_open_dead_port`
- `death_can_feed_border`
- `death_can_break_black_oath`
- `death_can_progress_last_name`
- `death_can_proclaim_black_apostolate`
- `death_state_can_be_sealed_in_iron`
- `death_state_can_be_dead_port`
- `death_state_can_be_fed_to_border`

Add effect helpers:

- `death_mark_black_atlas_dirty`
- `death_open_black_book_effect`
- `death_add_dark_method_exposure`
- `death_add_bound_names`
- `death_add_mourning_debt`
- `death_bind_unburied_effect`
- `death_interrogate_empty_road_effect`
- `death_seal_names_in_iron_effect`
- `death_burn_black_book_effect`
- `death_whisper_to_zol_effect`
- `death_take_black_oath_effect`
- `death_add_name_debt`
- `death_add_black_favor`
- `death_add_living_disgust`
- `death_offer_prison_census_effect`
- `death_open_dead_port_effect`
- `death_feed_border_effect`
- `death_break_black_oath_effect`
- `death_progress_last_name_effect`
- `death_proclaim_black_apostolate_effect`
- `death_cleanup_forbidden_route_state`

Use flags for true/false route state. Use variables for route meters. All tuning values should be constants or helper-scoped values. Do not introduce direct magic numbers in decisions.

Suggested country variables:

- `death_black_method_exposure`
- `death_bound_names`
- `death_mourning_debt`
- `death_name_debt`
- `death_black_favor`
- `death_living_disgust`
- `death_last_name_progress`
- `death_dead_ports_opened`
- `death_forbidden_route_dirty`

Suggested country flags:

- `death_black_book_opened`
- `death_black_book_burned`
- `death_used_bound_names`
- `death_black_methods_exposed`
- `death_black_oath_contacted`
- `death_black_oath_taken`
- `death_herald_of_zol`
- `death_oath_publicly_revealed`
- `death_oath_broken`
- `death_last_name_started`
- `death_last_name_completed`
- `death_black_apostolate_proclaimed`

Suggested state flags:

- `death_names_sealed_in_iron`
- `death_dead_port_open`
- `death_border_fed`
- `death_herald_mandate_state`

## Dark Methods Route

Dark Methods should unlock after the world knows Death is real, or earlier for a desperate country that directly controls a Death wasteland or has suffered Death border pressure. It should compete with the Black Oath route. A country that takes the Black Oath cannot continue building the Black Book office.

### Decisions

`death_open_black_book`

- Category: living-country containment category or the new forbidden-methods category.
- Visible if Death has been revealed, the country is not DTH, is not a Herald, has not burned the book, and has enough contact with Death to justify the breach.
- Available if the country has political power, stability margin, and either an owned/controlled wasteland, active Death neighbor threat, or high world-end pressure.
- Effects: set `death_black_book_opened`, add initial exposure and mourning debt, unlock Dark Methods category, add a small national idea such as `death_black_book_office`, mark Atlas dirty.
- AI: very low baseline; higher for authoritarian, extremist, collapsing, directly threatened, or already high chaos countries; blocked for stable democracies unless world-end pressure is severe.

`death_bind_unburied`

- Visible after `death_black_book_opened`.
- Available if `death_bound_names` or eligible wasteland/contact states exist and bound-unit cap is not reached.
- Effects: spend bound names, army XP, infantry/support equipment, and stability; create a small, capped irregular unit package or apply a timed combat modifier in wasteland states. Set `death_used_bound_names`, add exposure and mourning debt.
- Implementation preference: use a capped decision effect and a dedicated template/OOB if existing patterns make unit creation safe. If creating units would require a broad new template package, use timed modifiers instead and record the simplification before implementation.
- Failure pressure: if exposure reaches the high threshold, fire a domestic scandal event or apply a timed legitimacy penalty. Do not use random scandal events without player-facing warning.

`death_interrogate_empty_road`

- Visible after `death_black_book_opened`.
- Available if the country has an adjacent Death front, a recaptured wasteland, or a coastal-risk state.
- Effects: spend command power/intel-like cost, add exposure, reveal one practical Death pressure indicator in the Atlas, and apply a cooldown. It can reduce the next wither/coastal risk against that country or improve quarantine-line readiness.
- Do not make this a generic map-reveal exploit. It should only inform Death-adjacent or Death-exposed countries.

`death_seal_names_in_iron`

- Target: controlled Death wasteland, recaptured wasteland, or quarantine-line state.
- Available if the state is not already sealed and the country has equipment/trains/army XP as required.
- Effects: set `death_names_sealed_in_iron`, apply a state modifier reducing ghost pressure, wither pressure, or spread contribution, add exposure and mourning debt.
- Edge case: if Death consumes the state later, add a backlash effect to the former controller if still alive.

`death_burn_black_book`

- Visible after `death_black_book_opened` and before Black Oath.
- Available if no bound decision is currently on a critical cooldown or if the player accepts the penalty for abandoning it.
- Effects: set `death_black_book_burned`, remove/disable Black Book office benefits, reduce exposure over time or remove some active penalties, disband/remove bound units or expire timed modifiers, lock further Dark Methods.
- Achievement hook: eligible for `death_book_burner` only if the player opened the book, used at least one Dark Method, burned the book before taking Black Oath and before exposure passed the scandal threshold, and later helped defeat Death.

### Dark Methods AI

AI should use Dark Methods as a desperation tool:

- High weight: authoritarian or extremist country, Death border, local wastelands, high casualties, compact failing, world-end active.
- Low weight: stable democracies, compact leader with good cohesion, countries far from Death.
- Hard block: DTH, Herald, countries with `death_black_oath_taken`, countries that burned the book, and countries designated by active event logic as non-participants.
- AI should prefer `seal_names_in_iron` and `interrogate_empty_road` over `bind_unburied` unless under direct threat.
- AI should burn the book if Death is defeated, exposure is high, or it is attempting to rejoin living diplomatic systems.

## Black Oath And Herald Route

The Black Oath is a hostile bargain, not peace. A Herald is spared only while the bargain is useful and the debt remains under control. This route should be rare for AI and morally expensive for players.

### Decisions And Events

`death_whisper_to_zol`

- Visible if Death has been revealed and the country is threatened, desperate, or already compromised by Dark Methods.
- Available if not DTH, not in the Living Compact leadership lock, not a Herald, not post-Death-defeat, and not blocked by a route-specific flag.
- Effects: set `death_black_oath_contacted`, add a warning event or confirmation chain, add living disgust, mark Atlas dirty.
- Super-event role: this may prepare a Black Oath super-event role if the country is a major or player-led, but the final title/button/quote/audio must be produced by the super-event workflow later.

`death_take_black_oath`

- Should be a confirmation event or decision with severe visible consequences.
- Effects: set `death_black_oath_taken` and `death_herald_of_zol`, remove/lock Dark Methods, leave the Living Compact, apply opinion and diplomatic penalties with living countries, add a Herald national idea, add black favor and name debt, mark Atlas dirty.
- War handling: if currently at war with Death, use a narrow scripted peace or truce-like handling only for the oath-taker. Do not create a normal alliance or faction with DTH.
- Death target handling: Death should avoid consuming Herald states while the oath is honored and debt is below the betrayal threshold. If debt is too high, oath broken, or Death reaches final world-consumed logic, the Herald can be consumed.

`death_offer_prison_census`

- Visible for Herald only.
- Effects: increase black favor and name debt, add living disgust, possibly reduce local resistance/chaos, and set an achievement-disqualifying cruelty flag for living-route achievements.
- Keep it abstract. Do not require prisoner-population systems unless they already exist.

`death_open_dead_port`

- Target: owned or controlled coastal state, not capital, not already open, not already fully consumed.
- Effects: set `death_dead_port_open`, increase black favor and name debt, reduce Death hostility toward the Herald, and increase coastal danger for neighbors or future betrayal.
- It should create a clear Atlas warning. A dead port is both a favor source and a future vulnerability.

`death_feed_border`

- Target: low-value border or coastal state under Herald control, never capital, never blocked by active scenario/event protections.
- Effects: transfer/consume the state through existing Death consumption helpers or a dedicated Herald sacrifice helper, add black favor, add heavy name debt and living disgust, and update Death global counters.
- Acceptance boundary: this must not be a free exploit for deleting bad states. It should carry diplomatic, stability, manpower, and achievement consequences.

`death_break_black_oath`

- Visible for Herald after oath.
- Available if the Herald has compact support, Death is weakened, name debt is untenable, or living disgust is destabilizing the country.
- Effects: set `death_oath_broken`, remove Herald protection and most favor benefits, reopen living containment decisions where appropriate, trigger Death retaliation pressure, and lock `death_friend_of_zol` and Apostolate achievements.
- This route should exist because a player may regret the oath, but it does not need a separate achievement.

### Herald State

Herald identity should be implemented as flags, ideas, cosmetic identity, and diplomatic posture:

- Flag: `death_herald_of_zol`
- Idea: `death_herald_of_zol` or route-appropriate existing idea file entry.
- Cosmetic identity: use a cosmetic tag or flag variant only if the project already has a stable route for cosmetic tags. Do not create a new playable tag.
- Diplomacy: cannot join or lead Living Compact; receives severe living opinion penalties; has blocked access to normal containment leadership decisions; can still fight non-Death wars unless blocked by route effects.
- Death behavior: receives conditional reprieve from Death spread and wither targeting. Reprieve is lost if debt exceeds the configured threshold, oath breaks, or final world-consumed logic requires cleanup.

### Black Oath AI

AI should almost never take the oath. It is acceptable for the route to be effectively player-first.

- Hard block: DTH, current compact leader, stable major holding the line, countries with route-specific event protection, countries not threatened by Death.
- Very low chance: authoritarian/extremist, direct Death border, severe instability, capital threatened, compact collapsed, world-end active.
- Use `ai_will_do` helper triggers and constants. If weights become cluttered, centralize with MTTH guidance instead of duplicating complex logic across decisions.

## Black Apostolate

The Black Apostolate is a hidden culmination for a Herald that survives long enough to formalize the bargain. It should be implemented as a route proclamation, not a new country package with a full independent mechanic loop.

### Unlock Conditions

Suggested required conditions:

- Country has `death_herald_of_zol`.
- Death is alive.
- Death world-end or Last Shores phase has begun.
- Country capital is not consumed.
- Country is not in the Living Compact and has not broken the oath.
- `death_last_name_completed` is set.
- Country controls a configured number of dead-zone outposts, sealed wastelands, dead ports, or Herald mandate states.
- `death_name_debt` is below the immediate betrayal threshold or has been ritually converted through the Last Name chain.
- Stability is low enough, living disgust high enough, or route idea present long enough to justify irreversible transformation.

### Last Name Chain

Implement this as two or three decisions, not a focus branch:

`death_compile_last_name`

- Visible for Herald in world-end/Last Shores pressure.
- Effects: start `death_last_name_started`, spend black favor, add name debt, require a dead port or outpost network.

`death_seal_apostolate_ledger`

- Visible after the Last Name has started.
- Available if the Herald controls enough eligible states and has survived a configured delay.
- Effects: set `death_last_name_completed`, convert some black favor/name debt into a permanent route modifier, mark Atlas dirty.

`death_proclaim_black_apostolate`

- Visible only if all hidden culmination conditions are met.
- Effects: set `death_black_apostolate_proclaimed`, apply cosmetic identity if supported, apply permanent isolation and Apostolate idea, lock normal living-route systems, update achievement state, mark Atlas dirty.

### Apostolate Rules

- No population restoration.
- No free cores over living states.
- No annexation of Death.
- No normal Death faction.
- No broad conquest bonuses.
- Claims, cores, or modifiers may apply only to states the Herald sacrificed, dead-zone mandate states, or states already changed by Death systems.
- If the Apostolate is later consumed by Death, the route should end cleanly and remove UI/achievement progress where necessary.

### Apostolate AI

AI should not pursue this from neutral state. AI can proclaim only if it is already a Herald, already deep in the route, Death world-end is active, and the normal living response has collapsed. A player-only route is acceptable if the AI conditions would otherwise be contrived.

## Black Atlas UI

The Black Atlas should be implemented because the forbidden routes add enough state that decision tooltips alone will become crowded. It should be a compact decision-adjacent dashboard, not a second game mode.

### UI Shape

Preferred implementation:

- Add a decision-category entry point from `death_country_containment_category`.
- Use a scripted GUI window for player display and tabs.
- Keep decisions as the authoritative action surface. Atlas buttons should handle only open, close, tab selection, and maybe pinning a tracked panel. Do not hide major gameplay effects only in GUI buttons unless every effect has an AI-safe decision equivalent.

Suggested tabs:

- `Map`: consumed-state count, consumed-population band, known origin/reveal state if known, current phase.
- `Census`: Black Census status, ghost tier, public Death status.
- `Coasts`: coastal risk, lit ports, patrol status, dead ports if Herald.
- `Line`: quarantine line status, wither pressure, sealed names, outposts.
- `Compact`: Living Compact leader, member count, available compact calls.
- `Forbidden`: Dark Methods and Black Oath values. Hidden until the player has opened the Black Book, contacted Zol, or become a Herald.

Suggested displayed values:

- Global consumed states and population band.
- Global or country-known ghost tier.
- Local quarantine-line readiness.
- Local coastal warning and port-lighting status.
- Compact membership and player compact role.
- `death_black_method_exposure`
- `death_bound_names`
- `death_mourning_debt`
- `death_name_debt`
- `death_black_favor`
- `death_living_disgust`
- Last Name progress.

### UI Technical Notes

- Use `context_type = player_context` for a full window, or `context_type = decision_category` if embedded category UI is sufficient after checking existing Chaos Redux GUI patterns.
- Track tab state through country flags or variables such as `death_black_atlas_tab`.
- Add `death_mark_black_atlas_dirty` and call it from every helper that changes displayed values.
- Do not create daily update loops. Update from existing decision effects, Death pulse effects, state-control hooks, and route helper effects.
- Every Atlas-visible route action should still have normal decision/localisation support for AI and accessibility.

## Asset And Animation Handoff

Final sprites were registered with stable names and backed by generated final assets or static fallbacks, so the game has no missing sprite dependencies for the implemented route package.

Suggested paths and sprite names:

| Asset | Path | Sprite |
| --- | --- | --- |
| Black Atlas background | `gfx/interface/death/black_atlas/death_black_atlas_background.dds` | `GFX_death_black_atlas_background` |
| Black Atlas header static fallback | `gfx/interface/death/black_atlas/death_black_atlas_header.dds` | `GFX_death_black_atlas_header` |
| Black Atlas header animated sheet | `gfx/interface/death/black_atlas/death_black_atlas_header_animated.dds` | `GFX_death_black_atlas_header_animated` |
| Coastal risk pulse animated sheet | `gfx/interface/death/black_atlas/death_coastal_risk_pulse.dds` | `GFX_death_coastal_risk_pulse` |
| Wither target animated frame | `gfx/interface/death/black_atlas/death_wither_target_frame.dds` | `GFX_death_wither_target_frame` |
| Compact warning pulse | `gfx/interface/death/black_atlas/death_compact_warning_pulse.dds` | `GFX_death_compact_warning_pulse` |
| Herald of Zol flag variant | `gfx/flags/cosmetic/herald_of_zol/` or project-standard cosmetic flag folder | project-standard cosmetic flag keys |
| Black Apostolate flag variant | `gfx/flags/cosmetic/black_apostolate/` or project-standard cosmetic flag folder | project-standard cosmetic flag keys |
| Zol animated portrait overlay | `gfx/leaders/DTH/zol_world_end_animated.dds` | `GFX_leader_zol_world_end_animated` |
| Black Oath super-event image | `gfx/super_events/super_event_death_black_oath.dds` | `GFX_chaosx_super_event_66` |
| Route achievement icon, Black Book | project-standard achievement icon folder | existing `death_book_burner` achievement sprite |
| Route achievement icon, Herald | project-standard achievement icon folder | existing `death_friend_of_zol` achievement sprite |
| Route achievement icon, Apostolate | project-standard achievement icon folder | `death_black_apostolate` achievement sprite if achievement is accepted |

Suggested animation dimensions:

- Atlas background: 640x460 static.
- Atlas header: 640x72 per frame, 8 frames, 6 fps loop, static fallback required.
- Coastal risk pulse: 48x48 per frame, 8 frames, 8 fps loop.
- Wither target frame: 280x64 per frame, 8 frames, 8 fps loop.
- Compact warning pulse: 40x40 per frame, 6 frames, 6 fps loop.
- Zol portrait overlay: 156x210 per frame, 10 frames, 6 fps loop, static fallback required.

Animation must be a true frame sequence. Do not approve a package that only moves, scales, rotates, warps, blurs, recolors, or filters one still image. Each animated package needs source frames, contact sheet, preview, DDS sheet, static fallback, manifest entry, and `.gfx` handoff.

## Route Achievements

Implement only the achievements that map directly to the remaining route work.

`death_book_burner`

- Condition: player opened the Black Book, used at least one Dark Method, burned the Black Book before taking Black Oath and before exposure crossed the scandal threshold, and participated in Death's defeat.
- Disqualifiers: `death_black_oath_taken`, `death_black_methods_exposed`, country consumed by Death, route cleanup failure.

`death_friend_of_zol`

- Condition: player took the Black Oath, became Herald of Zol, kept the capital unconsumed through the configured survival window or Last Shores phase, and did not break the oath.
- Disqualifiers: `death_oath_broken`, country consumed before survival condition, no public reveal/world-end phase.

`death_black_apostolate`

- Implemented because Black Apostolate is implemented.
- Condition: player became Herald, completed the Last Name chain, proclaimed the Black Apostolate during Death world-end or Last Shores phase, controlled the configured dead-zone mandate count, kept the capital unconsumed, and survived the configured delay.
- Disqualifiers: oath broken, Death defeated before proclamation, capital consumed, route cosmetic/idea cleanup missing.

Do not add a separate oathbreaker achievement in this pass. Breaking the oath is a route escape valve, not a third route.

## Super-Event Boundary

This addendum supported these role labels:

- Black Oath public reveal by a major or player-led country.
- Black Apostolate proclamation during Last Shores/world-end pressure.

Do not invent final title, button, quote, audio, or final super-event text in implementation. The accepted Black Oath package was passed through the super-event text/audio workflow and the relevant super-event docs were updated after research.

## Validation Acceptance

The implementation should not be considered complete until these are true:

- Dark Methods decisions exist, are localised, have effect descriptions, use centralized constants, and cleanly lock out Black Oath where needed.
- Black Oath decisions exist, are localised, have visible consequences, lock out normal compact leadership, and do not create a normal Death faction.
- Herald of Zol has route flags, idea/cosmetic support where appropriate, Death targeting exceptions, diplomatic consequences, and cleanup.
- Black Apostolate has hidden unlock conditions, Last Name progression, proclamation consequences, achievement state, and no free living-state cores or population restoration.
- Black Atlas displays all route meters and core Death status without adding gameplay-only GUI actions that AI cannot use.
- Route achievements are wired to real flags/effects and do not trigger from placeholder or partial route state.
- Asset placeholders are registered before art requests, final asset manifest lists exact paths, and animated assets include frame sheets plus static fallbacks.
- No new broad daily/world iteration is introduced.
- Existing Death defeat and world-consumed cleanup removes or freezes forbidden-route state correctly.
- AI has explicit weights or hard blocks for every AI-visible route decision.
- Docs under `docs/events/010_death.md` and `docs/specs/010_death_specs/` are updated after implementation.

## Promotion Closure

The parent accepted and implemented each route package. The design has been promoted into:

- `docs/specs/010_death_specs/specs/010_death_decisions_ui_ai.md` for Dark Methods, Black Oath, Herald, Black Atlas, and AI details.
- `docs/specs/010_death_specs/specs/010_death_country_package_and_focus_tree.md` for Black Apostolate identity and route boundaries.
- `docs/specs/010_death_specs/specs/010_death_assets_super_events_achievements.md` for assets, animation, achievements, and the Black Oath super-event role.
- `docs/events/010_death.md` for the final player-facing systems.

No named route item was rejected as bloat. A further improvement-loop pass is not needed for this addendum.
