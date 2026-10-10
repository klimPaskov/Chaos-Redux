# Holy Realm Buddhahood Planning Package

This package is the current design reference for the Holy Realm Buddhahood and Final Silence route of Event 003.
The route is implemented; [the event overview](../../../events/003_holy_realm/overview.md) describes current behaviour and [the release reconciliation](../../../plans/003_holy_realm_plans/release_qa_completion_20261006.md) records acceptance for the bounded repairs and the remaining release gates.
Broad acceptance of every nested design claim remains unresolved; claims carry their own disposition where it is known.
The top-level [legacy specification](../003_holy_realm_spec.md) is historical provenance.

Workflow ownership is defined by [chaos-redux-subagents](../../../../.claude/skills/chaos-redux-subagents/SKILL.md), [chaos-redux-event-assets](../../../../.claude/skills/chaos-redux-event-assets/SKILL.md), and [chaos-redux-scripted-gui](../../../../.claude/skills/chaos-redux-scripted-gui/SKILL.md).
Every character portrait belongs to `chaosx_portrait_creator`.
The dedicated mandala window belongs to `chaosx_event_ui_worker` when its accepted bounded brief supplies the required reference and MCP evidence contract.

The event id is `003`; implementation uses the existing `chaosx.nr3.*` Holy Realm namespace.

## Files

| File | Role |
| --- | --- |
| `specs/holy_realm_buddhahood_spec_part_1.md` | Core promise, values, stages, evolutions, shared-system links, event map, balance target |
| `specs/holy_realm_buddhahood_mechanics_and_gui.md` | Mandala panel, concentration ritual, teaching missions, powers, Final Silence ritual |
| `specs/holy_realm_buddhahood_focus_tree.md` | Route design for the focus tree |
| `specs/holy_realm_buddhahood_decisions_missions.md` | Decision categories, missions, compact, cleanup and exploit checks |
| `specs/holy_realm_buddhahood_country_package_ai.md` | Host handling, identity, portraits, ideas, forces, formables, AI actors |
| `specs/holy_realm_buddhahood_asset_animation_spec.md` | Asset families, animation states and delivered packages |
| `specs/holy_realm_buddhahood_super_events.md` | Super-event roles, writing and audio direction |
| `specs/holy_realm_buddhahood_achievements.md` | Achievement conditions and tracking |
| `matrices/holy_realm_buddhahood_route_coverage_matrix.md` | Completion checklist and open gates |
| `matrices/holy_realm_buddhahood_ai_matrix.md` | AI priorities, power use and foreign reactions |
| `research/holy_realm_buddhahood_research_notes.md` | Source anchors, tone notes and research status |
| `prompts/holy_realm_buddhahood_coding_prompt.md` | The single resume brief for further work |

## Open questions

Each item below is proposed (spec audit 2026-10-10) unless stated otherwise.
None is a current implementation requirement until the user or parent accepts it; record the acceptance here before editing source.

### 1. Fewer values that drive decisions

Disposition: partly implemented on 2026-10-11 under the user's authority to remove needless values, relayed by the orchestrator.
The two values nothing read are gone: `compassion` (never shown in any UI) is folded into Compassion Drift and `world_suffering` is retired.
The Detachment fold, the single visible balance meter and the per-tab value filter stay proposed, and the 2026-10-08 conflict below applies only to them.

Before that change, source tracked Spiritual Legitimacy, Compassion Drift, Mandala Reach, Final Silence Pressure, Bodhi Progress, Dhyana Depth, Compassion, Detachment, Defilements, Meditation Charge, World Suffering and Sangha Cohesion, plus teaching counts, the bhumi ladder and the Vow and Final Silence balance of power.
That is more than a player can weigh, and several values change nothing:

- `compassion` is written by about sixteen effects but read nowhere; fold its gains into Compassion Drift, which already carries mercy versus coercion.
- `world_suffering` is set once from the Chaos Meter at formation and never updated or read; retire it and read the Chaos Meter tier and active world-threat sources directly, as Part 1 already requires.
- Detachment is read only by two `> 20` gates; fold it into Defilements so restraint lowers Defilements and those gates read a Defilements ceiling.
- Every `THR_bop_*` decision moves the balance of power and Final Silence Pressure in the same direction; make the native balance the one visible doctrine meter and express the 45/55/65/75 pressure thresholds as balance ranges.
- Each Mandala tab shows only the values that gate its own actions, for example Meditation Charge after the first Dhyana and Sangha Cohesion after the Mandala of Nations forms.

The result is about seven tracked values plus the balance instead of twelve.
This conflicts with the parent's 2026-10-08 decision to preserve the accepted Event 003 public values (`docs/plans/repo_cleanup/specification_improvements_2026-10-08/handoffs/001_006.md`), so it needs an explicit decision before any source change.

### 2. Doctrine actions with consequences

Disposition: implemented on 2026-10-11 under the user's authority to remove repetitive decisions, relayed by the orchestrator.
The doctrine category held twenty-one Political Power actions that mostly bought a small balance shift plus counter changes.
Six remain, three for each side, and the Bodhisattva council mission keeps its unique bhumi advance.
Each merged action applies the strongest balance shift its unlocked tiers allow and adds the side effects of every tier whose original gate holds when it is taken, so no distinct effect was dropped.

| Action | Replaces |
| --- | --- |
| `THR_bop_mercy_council` | Public Vow of Non-Annihilation, Mercy Council, Lamp Processions |
| `THR_bop_send_bodhisattva_to_council` | unchanged |
| `THR_bop_open_lotus_audit` | Lotus Audit, Reconcile Outer Monasteries, Release Sealed Names, White Mandala Oath, Last-Pass Watch |
| `THR_bop_last_resort_clause` | Guarded Silence Clause, Last-Resort Clause, Arhat Inquiries, Border Silence Offices, Forceful Mercy Precedent |
| `THR_bop_final_command_drills` | Final Command Drills, Silent Transit Codes, Nuclear Sutra Committee, Expand Silence Cells |
| `THR_bop_seal_the_ledger` | Argue for the Last Weapon, Authorize the Launch Crews, Empty Mandala Session |

The summed shift of the old twenty actions per cycle fell from about 1.3 to about 0.5, because one purchase now stands for a whole tier ladder.

### 3. Date gates become conditions

Disposition: implemented on 2026-10-11 under the user's 2026-10-10 decision that dates influence and gameplay conditions decide; the late Vow crusade reads `holy_realm_chaos_at_least_totalen_chaos`, and the Empty Mandala session and All Roads End in Silence weights no longer read a date.

- `holy_realm_late_vow_against_annihilation_crusade` in `common/scripted_effects/003_holy_realm_effects.txt` grants the large Vow against Annihilation crusade idea on renunciation when `date > 1944.12.31`, even if the doctrine was never armed and pressure stayed low.
  Replace the date with a real crisis condition, such as `holy_realm_chaos_at_least_totalen_chaos` or an active world-threat source other than the Realm.
- `THR_bop_empty_mandala_session` gives the AI its only positive weight only after 1944; keep the Chaos above 900 and pressure above 75 conditions and let the date at most scale the weight.
- `THR_all_roads_end_silence` couples its Totalen Chaos AI multiplier to `date > 1943.12.31`; drop the date or give it a separate small multiplier.

### 4. Refugees through the migration owner

Disposition: implemented on 2026-10-11 under the user's authority to connect systems, relayed by the orchestrator.
The formation event's three refuge choices, `THR_open_refuge_roads` and `THR_close_refuge_roads` set the Realm's reception policy through `migration_decision_set_policy`, and both decisions read `migration_reception_policy_is_humanitarian_open`.
The daily doctrine pulse pays the refuge credit from the migration owner's `migration_integrated_population`, one block of people at a time, instead of through a hook in the migration owner.
`humanitarian_country_is_valid` now admits the Holy Realm, which the special-country registry had excluded from the famine, migration and transfer systems.
Sangha Cohesion for compact-member refugees and per-cohort manpower stay proposed: the integration settlement exposes no cohort origin to a consumer.

The five flat manpower grants were removed because they created recruits from nothing.
Instead, `THR_open_refuge_roads` and `THR_close_refuge_roads` should set the Realm's reception policy through the migration owner (`migration_open_reception`, `migration_close_border`), and Holy Realm checks should read `migration_reception_policy_is_humanitarian_open` rather than private refuge flags.
Refuge credit (Compassion Drift toward mercy, Sangha Cohesion when the people come from a compact member, and any manpower) is paid once for each cohort that actually integrates in a Realm state through `migration_local_integration`.
Holy Realm never writes migration ledgers, and no new meter is added.

### 5. Relief through the famine owner

Disposition: blocked on the famine owner.
The famine package has no external-donor relief entry: donors are the sparse registry its own recovered-state path fills, and recipients pull from it through their own decisions.
Admitting the Holy Realm to the humanitarian systems lets its states register through that path like any other donor, and the Realm's open reception counts in the donor weighting.
The push entry below belongs to the famine package and is not written here.

`THR_mandala_open_granaries` and `THR_white_scarf_relief_caravans` should help a compact member or neighbour that has a state at acute shortage or worse, delivering through a famine-owned relief adapter.
The kindness-act credit then depends on relief that actually arrives.
If the famine owner has no external-donor relief entry yet, that entry belongs to the famine package; Holy Realm must not write famine variables.

### 6. Condemnation for coercion

Disposition: implemented on 2026-10-11 under the user's authority to connect systems, relayed by the orchestrator, for the two coercion decisions.
`THR_prepare_forced_integration` (victim named) and `THR_mandate_kneeling_province` submit an atrocity-bucket public source through `holy_realm_condemn_coercion`.
A harmful power on a special actor without a hostile front cannot happen, because a harmful power already needs a defensive hostile front.

Wars from `THR_prepare_forced_integration`, `THR_mandate_kneeling_province` and harmful powers used on a special actor without a hostile front should submit `condemnation_add_source` with the victim country, so the world answers through the shared sanctions system.
The clean-route disqualifier stays Holy Realm-owned, and the condemnation owner supplies the source and context constants.

### 7. A peaceful compact that excludes atrocity

Disposition: implemented on 2026-10-11 for entry and eviction.
`holy_realm_sangha_compact_candidate_valid` and `holy_realm_sangha_compact_member_hard_valid` fail for a country with discovered camp sites, so the joining rule refuses it and the anti-puppet clauses remove it through the existing exit path.
A member whose camps are discovered later leaves at the next enforcement, not at the moment of discovery.

The Mandala of Nations should reject an entrant for which `genocide_country_has_discovered_sites` is true, and a member whose camps are discovered should leave through the existing `chaosx.nr3.130` exit path with its Cohesion loss.
This reuses the existing refusal and exit notices and adds no value.

### 8. Wrathful Protection from world events

Evolution D is currently recorded only by `THR_renew_vow_under_fire` and the Touching the Sun and Moon crisis proof.
Record it when a special chaos actor captures a Realm state or a valid compact member's capital, through the existing state-capture on-action with a cheap Holy Realm guard first, so the evolution answers the world rather than a purchase.
This adds no polling.

### 9. Two endings with their own gates

Disposition: implemented on 2026-10-11 under the user's authority to connect systems, relayed by the orchestrator.
`holy_realm_final_rite_ready` holds the shared Buddhahood rite: a Buddha power shown against chaos, the Extinction of Defilements, a secured capital sanctuary and no Schism.
`holy_realm_can_begin_final_silence_ritual` adds the doctrinal gates of the terminal branch, and `holy_realm_can_enter_empty_seat` needs only the rite and Defilements below the Final Silence gate.
`THR_enter_empty_seat` completes the non-terminal ending without the armed doctrine, so the Vow route reaches it, and the Final Silence focus is bypassed once the Empty Seat is taken.
The old ritual gate also required the Final Silence stage flag to be both set (through `holy_realm_final_path_unlocked`) and absent, so it could never hold; the new gate drops that contradiction.
The Buddha powers fall silent once the Empty Seat is taken, as the mechanics specification describes.

Before the change, the gate read as follows.
Current `holy_realm_can_begin_final_silence_ritual` makes both endings require the armed final doctrine, Final Silence dominance of the doctrine balance, the Ministry of Silence memory and a nuclear strike capability, and renouncing the doctrine blocks Final Silence altogether.
A clean Buddha who keeps the Vow against Annihilation therefore cannot reach the non-terminal Empty Seat ending that Part 1 and the mechanics spec describe as spiritual victory.
Split the gates: the Empty Seat ending needs only the Buddhahood ritual (Extinction of Defilements, the Last Wheel, a controlled capital, no Schism) and stays open after renunciation, while the armed doctrine, balance dominance, Ministry and nuclear capability gate only the terminal branch above Chaos 1000.
This gives the peaceful and the doctrinal routes distinct endings instead of one shared nuclear gate.

### Retained unresolved items

- Concentration sequence as the replacement for the literal three-minute hold: implemented, acceptance unresolved.
- Hostile-conduct target permission for harmful powers: accepted on 2026-10-08 and queued (Part 1).
- Compact-member support from Storehouses for the World: unresolved future proposal (focus tree spec).
- The 75 to 95 focus scope guide versus the implemented 111 focuses: unresolved, and it does not authorize deleting routes.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency: Part 1, mechanics, decisions, super-event and achievement specs now describe the accepted Fallout handoff for terminal Final Silence instead of the superseded `world_end_final_silence` launch.
The planning event map was replaced with the implemented event layout, implemented categories, identities, traits, filters and assets were recorded, stale `.agents/skills` links and the deleted `docs/assets/003_holy_realm_buddhahood/animations/` and `audio_research/` paths were corrected, and the research status reflects the verified quotes.
The goal, decision, achievement, super-event and asset prompts were removed because they restated the specs and would send an agent to rebuild installed work; the coding prompt is now the single resume brief.

Pass 2, design: dead and duplicate values, the doctrine-action shop, date gates, the shared nuclear gate that blocks the peaceful Empty Seat ending, and missing migration, famine, condemnation, camp and world-event links were recorded as Open questions with real identifiers.
The compact keeps Sangha Cohesion as its only value (proposed), and refuge actions may grant manpower only from people who actually arrive.
