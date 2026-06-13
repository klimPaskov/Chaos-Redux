# Event 008: AI and System Behavior Matrix

Event 008 should influence AI through temporary posture pressure and diplomatic state, not through forced wars.

## AI principle

AI behavior from this event should feel like governments reacting to an atmosphere. The event may raise willingness for already-valid systems, but it must not bypass target validity, route validity, alliance rules, or existing war logic.

## Actor groups

| Actor group | Baseline | Stage I | Stage II | Stage III | Stage IV |
| --- | --- | --- | --- | --- | --- |
| Major powers | normal WT reaction | slight defensive posture | stronger guarantees/rearmament | heavy hostile preparation weights | permanent-alert pressure, still target-checked |
| Faction leaders | normal | watch rivals | invite/guarantee more | pressure members and rivals | hostile bloc discipline, possible intra-faction distrust only if supported |
| Border rivals | normal | small hostility | relation hit likely | near-miss candidates | repeated alarm possible with cooldown |
| Naval powers | normal | no special change | insurance/shipping report possible | radio-silence follow-up possible | naval scare more likely |
| Neutral countries | normal | cautious | shipping and press anxiety | seek guarantees or rearm | panic without automatic faction entry |
| Minor countries | normal | mostly flavour | defensive alignment interest | higher guarantee request logic if supported | high fear, but no suicidal war |
| Special chaos/nonhuman tags | excluded unless allowed by shared triggers | excluded | excluded | excluded or custom only | excluded or custom only |

## AI strategy hooks

Potential temporary AI strategy names:

- `tensions_rising_cautious_alignment`
- `tensions_rising_alarmist_rearmament`
- `tensions_rising_general_staff_fever`
- `tensions_rising_permanent_alert`

The final implementation can use existing AI strategy files or direct decision weights if that is the established pattern.

## AI action families

| Action family | Stage I | Stage II | Stage III | Stage IV | Hard limits |
| --- | --- | --- | --- | --- | --- |
| Guarantees | small positive | medium positive | high positive | high positive | target must matter, no nonsensical guarantees |
| Faction invitations | no direct change | small positive | medium positive | high positive | ideology/geography/faction rules respected |
| Existing hostile decisions | no direct change | small positive | high positive | very high positive | valid targets only |
| War declaration | no direct change | no direct forced war | no forced war | no forced war | war goals and normal AI checks still required |
| Rearmament / mobilization | no direct change | medium | high | very high | no free units from Event 8 |
| Secret alliance systems | no direct change | medium if Event 11 exists | high if valid | high if valid | must respect Event 11 requirements |
| Random War / war cluster pressure | no direct change | low indirect | medium indirect | high indirect | Event 4 remains owned by its own system |

## AI weights by world condition

- If the country is already in a major war, Event 8 should mostly increase defensive and production posture rather than open new fronts.
- If the country is at peace but bordered by rivals, relation damage and border follow-ups should carry more weight.
- If the country is naval/trade-heavy, shipping panic follow-ups make more sense than border panic.
- If the country is a subject, avoid independent global postures unless the parent/overlord relationship is part of a valid panic story.
- If world-end is active, Event 8 should not add new non-terminal AI pressure unless the terminal scenario explicitly allows normal events.

## AI exploit prevention

- Do not let AI use a hidden Stage IV pressure to declare impossible or suicidal wars.
- Do not let temporary relation damage lock allies into permanent hostility after the timed modifier expires.
- Do not create hidden permanent AI strategy flags without cleanup.

## Human-player visibility

The player should not see a raw AI modifier list. They should infer the AI shift from delayed reports, relation changes, guarantees, alliances, and event logs.
