# Chaos impact and cross-event connections

## Event-owned Chaos

Event 036 changes Chaos only when the international order concretely changes, through `add_chaos_meter_value` with an Event 036 history reason.
Evolutions, postures, votes, research bonuses, stage reports, contributions, and cancellations add nothing.
Actual warfare, deaths, contamination, nuclear use, and annexation keep their own generic sources.

| Outcome | Chaos | Gate |
| --- | ---: | --- |
| Convention enters force with Provisional or Divided Standing | `+3` | Once, instead of the next row |
| Convention enters force with Established or Dominant Standing | `+5` | Once, instead of the previous row |
| First chemical First-Use Revision clause in force | `+5` | Once |
| First biological First-Use Revision clause in force | `+5` | Once |
| First Strategic WMD Doctrine Charter in force | `+7` | Once |
| First Nuclear Materials and Targeting Accord in force with a nuclear-capable ratifier | `+5` | Once |
| First Arsenal Without Limits Articles in force | `+10` | Once |
| Program Charter in force | `+5` | Once |
| Program project completed | `+10` | Once per project id |
| Standing falls from Established or Dominant to Provisional through withdrawals | `-5` | Once per campaign |

Each row uses a once-only global flag or a per-project history entry, so repeal and re-ratification, threshold oscillation, and repeated selection cannot farm Chaos.

## Shared systems

| System | Event 036 reads or changes | Event 036 never |
| --- | --- | --- |
| CBRN use policy and delivery ([doctrine](../../systems/cbrn_warfare/chaos_warfare_doctrine.md#use-policy)) | Diplomatic cost of each policy and AI weights | Adds a parallel first-use state or a new delivery route |
| CBRN action ledger and Retaliation Authority | First-use and retaliation classification for relief | Writes or edits a ledger row |
| Condemnation ([03](03_condemnation_normalization_and_cbrn_integration.md)) | Base relief, one participant-score term, opening normalization | Creates a second Condemnation total or touches atrocity and cover-up |
| CBRN diplomacy actions | Extra eligibility for inspections and decontamination aid | Duplicates the actions |
| Protection equipment | Treaty research and production modifiers | Creates a protection value |
| Deaths | Nothing, because Event 036 kills no one | Adds a Deaths reason |
| Air Cleanliness and fallout | Nothing | Changes contamination or fallout |
| Native special projects | Access flags through provider rows | Grants a completed project |
| Event log, evolutions, clusters | One History row, three evolutions, one cluster member row | Advances pacing through follow-ups |

## Air Cleanliness Treaty

Membership in Event 036 never overrides the [Air Cleanliness Treaty](../../systems/air_cleanliness/air_cleanliness_treaty.md).
An Air Cleanliness member that uses an unconventional weapon still triggers `air_cleanliness_treaty_on_unconventional_use`, even when Event 036 relieved the Condemnation.
The two memberships, their sanctions, and their betrayal memories stay separate, which gives a country in both treaties a real conflict.

## Camps

Ratifying the Inspection and Verification Protocol exposes a country to inspections that disclose hidden camp and restricted-site atrocity evidence through the existing disclosure path.
That is the only camp connection, and it is a deliberate cost of ratifying.
Event 036 creates and activates no camp, site, or atrocity source.

## Famine and migration

Event 036 adds no famine or migration link.
CBRN attacks already reach famine and migration through their own owners, and a treaty changes no food, shelter, or movement fact, so a separate link would only restate the same consequence.

## World threat and super-events

Event 036 sets no world-threat flag and owns no super-event or world-end scenario.

## Other events

| Event | Connection |
| --- | --- |
| Event 020 Black Plague | Program provider for `black_plague_weaponization_program` ([08](08_international_chaos_weapons_program.md#known-candidates)) |
| Zombie outbreak and weaponized zombies | Program provider for `weaponize_the_zombies` |
| Event 016 Brilliant Scientist and the Mengele directorate | Their per-country project access is the precedent for the grant flag and never cancels the program |
| Event 016 and Event 025 alien recovery | Consumers of the Alien Spacecraft receipts, which keep their names when the recovery moves into Event 025 ([01](01_event_identity_and_playable_promise.md#legacy-alien-spacecraft-relocation)) |
| Event 033 Acid Rain | Environmental harm never proves weapon use ([03](03_condemnation_normalization_and_cbrn_integration.md#evidence-and-inspections)) |
| Event 050 The Great Embargo | Never fired by Event 036, and its embargo ownership stays separate |
| Event 076 USA Tests Weapons | Proposed: an unconventional test by the United States reads its Event 036 posture (README, Proposals) |

## Cluster

Event 036 is a High-severity member of cluster 3, Diplomacy, in the workbook.
Implementation adds its runtime member row to the cluster 3 registry (still under the `diplomatic_panic` constant names) and keeps one canonical fire-once transaction when launched through the cluster.

## Special countries and shared helpers

Countries failing `uses_normal_civilian_systems` are excluded unless their owner supplies the compatibility trigger in [01](01_event_identity_and_playable_promise.md#country-eligibility).
Event 036 orchestration stays in Event 036 files, and a helper moves to the shared dynamic registry only if it is neutral and documented there.
