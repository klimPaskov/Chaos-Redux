# Condemnation normalization and CBRN integration

## Governing rule

Event 036 changes how much Condemnation a new public weapon use creates and how other governments react to it.

It owns no attack, outbreak, strike, casualty, contamination, evidence, attribution, or protection transaction.
Every chemical, biological, nuclear, and thermonuclear action continues through its existing owner, the CBRN action ledger ([action records](../../systems/cbrn_warfare/cbrn_action_records.md)), and the shared `condemnation_add_source` helper ([Condemnation and Sanctions](../../systems/cbrn_warfare/condemnation/condemnation_sanctions.md)).

Event 036 never changes deaths, military casualties, outbreaks, contamination, evidence, attribution, first-use status, retaliation status, or action history.

## Where relief applies

The Condemnation pipeline already has these stages: the caller's weapon base, the Integrated Chemical Operations doctrine mitigation on that base, the existing public-harm floors for confirmed strategic and mass-casualty chemical actions, then inside `condemnation_add_source` the civilian-death and contamination terms, the visibility split, and the severity multiplier.

The convention multiplier applies only to the weapon base, at the same point as doctrine mitigation and before the public-harm floors.
Where a context has no doctrine hook, it applies inside `condemnation_add_source` to the base before the death and contamination terms.

This placement gives three results without extra machinery:

- Civilian deaths and contamination always add their full Condemnation, so civilian harm needs no separate convention floor.
- The existing public-harm floors still apply after relief.
- The repeat-use bucket, which takes a share of the new public gain, follows the relieved gain automatically, so it needs no separate multiplier.

Relief is calculated once from the attacker's posture and ratifications on the day of the action.
A later posture change never rewrites an earlier action, and hidden evidence disclosed later carries the value already calculated.

The chemical doctrine mitigation and the convention multiplier multiply.
Their product never falls below the combined floor for the family: `0.10` for chemical, `0.20` for biological strikes, and `0.50` for nuclear strikes.

## Eligible contexts

| Condemnation context | Convention relief |
| --- | --- |
| `chemical_combat`, `chemical_air_strike` | Chemical multiplier |
| `biological_strike` | Biological multiplier |
| `biological_outbreak` | Biological multiplier, never below `0.70` |
| `nuclear_strike` | Nuclear multiplier, never below `0.80` against a capital or a state above the largest population band |
| `chemical_doomsday`, `biological_doomsday`, `thermonuclear_strike`, `final_silence` | None |
| `weaponized_zombies` and other Chaos weapon contexts | None unless the weapon owner maps the context to a family in [08](08_international_chaos_weapons_program.md#provider-contract) |
| Camp, experiment-site, restricted-site, concealment, destroyed-records, blocked-inspection, black-market, inspection-disclosure, and observer contexts | None |
| Pledge-breach add-ons | None |

## Source multipliers

A value of `1.00` is normal Condemnation.
Every value lives in one Event 036 script-constant table.

The stage is the highest step the country holds: Baseline (member), I (the First-Use Revision clause for that family), II (integrated doctrine earned under the Strategic WMD Doctrine Charter for the chemical and biological columns, and the Nuclear Materials and Targeting Accord for the nuclear column), III (the Arsenal Without Limits Articles).
An evolution alone never moves a country to a new stage, and losing integrated doctrine or a ratification drops the country to the highest step it still holds.

| Posture and stage | Chemical | Biological | Nuclear |
| --- | ---: | ---: | ---: |
| Full Ratification, Baseline | `0.55` | `0.75` | `0.90` |
| Full Ratification, I | `0.35` | `0.60` | `0.82` |
| Full Ratification, II | `0.18` | `0.40` | `0.65` |
| Full Ratification, III | `0.08` | `0.22` | `0.50` |
| Chemical Accession, Baseline | `0.60` | `1.00` | `0.95` |
| Chemical Accession, I | `0.40` | `1.00` | `0.90` |
| Chemical Accession, II | `0.22` | `1.00` | `0.75` |
| Chemical Accession, III | `0.12` | `1.00` | `0.60` |
| Retaliation Reservation, Baseline | `0.70` | `0.85` | `0.95` |
| Retaliation Reservation, II | `0.30` | `0.50` | `0.78` |
| Retaliation Reservation, III | `0.18` | `0.35` | `0.65` |
| Public Rejection, with or without a covert program | `1.00` | `1.00` | `1.00` |

Retaliation Reservation members never ratify a first-use clause, so they have no stage I, and their values apply only to retaliation.

For Full Ratification and Chemical Accession members, Baseline relief covers every eligible use of their families.
First use of a family still needs that family's ratified First-Use Revision clause to count as policy-compatible for sanction reactions below.

## Retaliation

Retaliation is proved only by the existing bilateral Retaliation Authority ledger: an exact earlier confirmed use by the target against the actor, while the two countries remain at war, within 365 days.

Event 036 reads that classification and never builds its own.
The existing `0.75` participant-pressure multiplier for verified battlefield retaliation stays separate and unchanged.

## Reservation breach

A Retaliation Reservation member that uses a weapon without Retaliation Authority against that target, or selects a CBRN use policy broader than Retaliation Only, breaks its reservation.

The breach applies:

- `1.00` to that action's source
- the existing pledge-breach consequence (`35` cover-up, `25` repeat-use, and 365 days of broken-pledge memory with zero decay), reused through a neutral helper rather than duplicated
- a suspension under [02](02_national_postures_and_membership.md#suspension-and-expulsion)
- increased sanction willingness among the other reservation members

Using the pledge-breach consequence without the existing `condemnation_non_use_pledge` flag needs an owner-approved adapter in the Condemnation effects (README, Proposals).

## Sanction reactions

The public Condemnation total stays one value per country.

Event 036 supplies one participant-score term to `condemnation_recalculate_participants`:

- a member scoring a member's policy-compatible use is less willing to join sanctions
- a reservation member scoring a first use is more willing
- a public opponent scoring any member use is more willing

Policy-compatible use is retaliation, or use of a family covered by a ratified First-Use Revision clause, or any use by an Arsenal Without Limits ratifier.

## One-time normalization on entry

After each country's opening posture is recorded, its existing public chemical and biological buckets fall once:

| Opening posture | Chemical bucket | Biological bucket |
| --- | ---: | ---: |
| Full Ratification | `-35%` | `-25%` |
| Chemical Accession Only | `-30%` | `0%` |
| Retaliation Reservation | `-15%` | `-10%` |
| Public Rejection | `0%` | `0%` |

Nuclear, atrocity, cover-up, and repeat-use buckets and every hidden bucket stay unchanged.

The effect sets a once-only flag, recalculates the total and tier, and calls the normal participant refresh.
It never cancels a native embargo directly, because the existing embargo owner releases relations only when no owner remains.

This is the one immediate reason for a condemned country to ratify, and it must be visible in the opening option tooltip as the tier the country would move to.

## Evidence and inspections

Inspections use the existing CBRN inspection path (`cbrn_demand_inspections` and the Accept or Refuse responses).
Accepted inspections disclose hidden buckets at the existing rate, including hidden atrocity evidence from camps and restricted sites, which is the real cost of accepting them.

Event 036 never creates an action record, an attacker, or evidence.

Environmental harm alone does not prove weapon use.
[Acid Rain's separate Air source](../033_acid_rain_specs/specs/033_acid_rain_spec_part_11_integrations_migration_and_save_safety.md#air-cleanliness-integration), natural aerosol, and an unattributed outbreak never qualify for relief or retaliation proof, and an inspection may stay unresolved.

If a real chemical or biological action occurs in a state already under Acid Rain, the CBRN owner proves and attributes that action, Event 036 relieves only that action's eligible base, and the rain mortality, environmental burden, and Air receipt keep their owner.

## Protection

Masks, decontamination, detection, and medical preparedness reduce physical harm through their existing systems before Condemnation is calculated.
Protection never reduces responsibility or Condemnation by itself.

## Required checks

These checks are run against the constant table and the actual adapters:

| Check | Expected result |
| --- | --- |
| Base chemical source from low to mass-casualty | Member relief falls as tabled and the public-harm floor still dominates mass-casualty use |
| Doctrine mastery 5 with Full Ratification stage III | The combined product stops at `0.10` of base |
| Biological outbreak at every stage | Never below `0.70` of base |
| Nuclear capital target | Never below `0.80` of base |
| Thermonuclear, Final Silence, doomsday | Exactly `1.00` at every stage |
| Large civilian deaths | The death term is identical with and without the convention |
| Repeat use within 180 days | The repeat bucket gains the share of the relieved gain, with no second reduction |
| Posture change after an action | The earlier action's recorded Condemnation is unchanged |
| Opening normalization | Only public chemical and biological buckets fall, once |
