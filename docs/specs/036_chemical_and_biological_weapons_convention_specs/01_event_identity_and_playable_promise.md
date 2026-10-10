# Event identity and playable promise

## Catalog identity

Event 036 replaces the Alien Spacecraft event in slot 36.

The entry event keeps the canonical id `chaosx.nr36.1`.

The design registers the event as Minor Fire-Once with Chaos level 1 (Calm World).

The authoritative workbook already lists Event 036 as a High-severity member of cluster 3, Diplomacy, the cluster formerly named Diplomatic Panic ([event clusters](../../systems/event_system/event_clusters.md)).
The runtime cluster registry still uses the `diplomatic_panic` constant names for cluster 3 and has no Event 036 member row yet, so the member row is implementation work, not a new cluster.

The workbook event row still describes Alien Spacecraft as Minor Repeatable, and [the spreadsheet prompt](prompts/spreadsheet_alignment_prompt.md) owns its replacement.

Recurring conference and program events remain Event 036 follow-ups and never become selectable random events.

## Legacy Alien Spacecraft relocation

The current `events/036_alien_spacecraft.txt` is a small Alien Spacecraft stub, but other events consume its output.

| Consumer | Dependency |
| --- | --- |
| Event 025 shared alien recovery ledger | `chaosx_alien_recovery_ledger_resolve_event036`, the `chaosx_alien_recovery_event036_*` receipts, and `global.chaosx_alien_recovery_event036_recoverers` read by `chaosx_nr25_enroll_event036_recoverers` |
| Event 016 Brilliant Scientist | `brilliant_scientist_alien_spacecraft_recovered` and `brilliant_scientist_try_schedule_alien_spacecraft_contact` |
| News | `chaosx.news.41` |
| Assets | `gfx/event_pictures/036_alien_spacecraft/` and `localisation/english/036_alien_spacecraft_l_english.yml` |

The alien jet recovery is not retired: it moves into Event 025 Alien Technology in Antarctica as that event's entry path (orchestrator decision, 2026-10-10, see README Acceptance basis).
Implementation removes the Alien Spacecraft producer from slot 36 and rehomes the recovery content under Event 025's ownership, keeping the existing receipt names (`chaosx_alien_recovery_event036_*`, `global.chaosx_alien_recovery_event036_recoverers`, `brilliant_scientist_alien_spacecraft_recovered`) so the Event 025 ledger and the Event 016 contact keep reading the same receipts in new and existing saves.
The news event, art, and localisation move with the recovery content; Event 036 keeps none of them.

## Player experience

Governments openly treat battlefield gas, biological laboratories, protective equipment, delivery systems, first-use reservations, and nuclear doctrine as normal treaty subjects.

The player chooses what their country will publicly defend and what it will prepare in private.

Five coherent strategies must remain viable:

- embrace the convention and use its military and research network
- accept chemical warfare while refusing biological normalization
- join for protection and retaliation while keeping a no-first-use line
- reject the convention and lead an opposing bloc
- reject it publicly while running a covert program

Each route changes treaty access, Condemnation treatment, AI behaviour, inspection exposure, and later program access.

## Global setup sequence

The entry effect runs once:

1. Prove Event 036 has not fired and set the active global flag.
2. Select the convention coordinator.
3. Build the eligible country list once in a bounded event-time pass.
4. Send the opening response event to every eligible human country.
5. Resolve AI postures through the posture weights in [10](10_ai_behavior_and_probability_contract.md#opening-posture).
6. Register members and opponents, then calculate Convention Standing and select the Opposition Leader.
7. Apply the one-time Condemnation normalization from [03](03_condemnation_normalization_and_cbrn_integration.md#one-time-normalization-on-entry) after each country's posture is recorded.
8. Apply the opening Chaos outcome from [12](12_chaos_impact_and_cross_event_connections.md#event-owned-chaos).
9. Queue the first agenda.
10. Record Event 036 in History once and publish the opening news.

Human responses that arrive after the AI pass register through the same atomic posture effect and trigger a Standing recalculation.

The coordinator is an internal administrative scope for scheduled Event 036 events.
It does not lead the convention and gains nothing.
It is the strongest Full Ratification member by Standing weight, falls back to any member, and finally to the triggering country.
It is replaced through one bounded effect when it becomes invalid.

## Country eligibility

A country is eligible when it exists, has a capital, passes `uses_normal_civilian_systems`, and is not already registered.

Capitulation alone does not remove a valid government-in-exile.

A special Chaos actor that fails `uses_normal_civilian_systems` is excluded unless its owner adds an Event 036 compatibility trigger proving it can use national research, production, diplomacy, Condemnation, and decisions.

A country that becomes eligible later, such as a released or newly formed country, can join only through Seek Accession after the cooling period in [02](02_national_postures_and_membership.md#accession-after-the-opening), and it starts as Public Rejection with no covert program.

## Multiplayer behaviour

Every eligible human country chooses its own posture, and one player never chooses for another.

The convention, Standing, agendas, evolutions, and the program are global state.
Posture, covert program, treaty ratifications, contribution receipts, and achievement tracking are country state.

One global setup flag prevents duplicate initialization when several players receive the opening on the same day.

A human who does not answer within the event timeout receives Retaliation Reservation, the posture that participates without authorizing first use.

## Convention Standing

Standing is one of the three public values and changes conference cadence, quorum pressure on holdouts, and sanction behaviour.

It is recalculated only inside membership-changing transactions: opening resolution, accession, withdrawal, suspension, expulsion, and invalid-country cleanup.

Calculation, with every value in script constants:

- Standing weight is 3 for a major and 1 otherwise, and a Chemical Accession member counts half.
- Support share is total member weight divided by total member and public opponent weight.

| Standing | Rule | Gameplay effect |
| --- | --- | --- |
| Provisional | Fewer than 3 members or support share below 0.40 | Conferences pause except reconstruction |
| Divided | Support share 0.40 to below 0.60 | Slow cadence and frequent close votes |
| Established | Support share 0.60 to below 0.80 | Normal cadence and full treaty cooperation |
| Dominant | Support share 0.80 or more and at least two major members | Fast cadence and AI holdouts lean toward accession |

## Early pacing

The first agenda opens 90 to 180 days after the opening.
War among members, Established or Dominant Standing, and members with CBRN technology shorten the interval, while Provisional Standing and a peaceful world lengthen it.

The first agenda is always a Baseline family.

## Failure and continuation

A weak opening produces Provisional Standing, not an ended event.
Opponents can keep it weak, members can recruit through lobbying and accession, and later rounds can rebuild it.

## Tone direction

The opening describes what governments and armies are doing because of the convention: chemical works hiring again, gas-mask drills in schools, laboratories under military guard, generals asking for stockpile figures, and diplomats defending all of it in public.

The player sees the convention's public purpose, the five responses, and their broad diplomatic consequences.

The text never reveals multipliers, voting arithmetic, future project candidates, or later evolution content.

Avoid conference-room paperwork as the emotional center, generic crisis correspondence, abstract map descriptions, and statements that the world has become more chaotic.
Follow the writing rules in [the events skill](../../../.claude/skills/chaos-redux-events/SKILL.md#event-writing-and-player-facing-text).
