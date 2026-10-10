# 2. Divine Wrath and Government Choices

## The public value

Divine Wrath runs from 0 to 100 for each participating country.
It is an event index of the government's conduct, not a measure of religious belief or a judgment on a population's ethnicity or faith.
The ordinary opening value is 25; scenario profiles (Part 12) can start higher.

The display shows the number with four bands: restrained below 25, mounting from 25, severe from 50 and extreme from 75.
The bands are for reading only; severity responds continuously, so one point never doubles casualties.

Every change names its cause in the tooltip or report, such as a completed water route, an abandoned shelter commitment or relief delivered to a neighbor.
Wrath never changes on its own: it has no decay, no daily drift and no automatic rise from war, poverty, disaster or receiving refugees.

## Harden Our Hearts

Harden Our Hearts is available once per plague phase.
It should tempt a government fighting for survival, not be a trap.

| Effect | Value |
| --- | --- |
| War Support | +10 percentage points for the phase |
| Stability | +5 percentage points, expiring at the next phase |
| Event 085 production interruption | Halved for the phase (never positive output, never repairs destroyed buildings, never touches Famine penalties) |
| Divine Wrath | +15 |

The policy spirit lasts until the next phase opens; to keep its benefit the government must choose again.
Hardening does not block local relief elsewhere, but the same trucks, fuel or state output cannot count toward both the hardening benefit and a relief action; the conflict is shown before selection.
During Darkness, hardening keeps emergency war production and political calm but cannot restore daylight or remove the air and detection penalties, and the tooltip warns about the tenth plague.

## Heed the Warning

Heeding means completing the current phase's protective action (Part 14), not paying a Political Power fee.
Wrath falls for completed work: water delivered, a district cleared, people sheltered, reserves protected, households reached.

| Result | Wrath change | Limit |
| --- | ---: | --- |
| Full completion of a substantial protective objective | −10 | One full credit per country per phase |
| Meaningful partial completion | −5 | Later full completion grants only the remaining −5 |
| Verified foreign relief delivery (Part 10) | −5 | Two distinct deliveries per phase |

Announcing relief, dispatching a convoy or paying for an action earns nothing until the objective completes.
Work interrupted by capture keeps what was actually done but earns no full credit.

## Conduct that raises Wrath

| Conduct | Change | Limit |
| --- | ---: | --- |
| Harden Our Hearts | +15 | Once per phase |
| Abandon a started relief objective while it was still achievable, or divert its committed equipment to a war action | +10 | Once per objective |
| A Condemnation incident recorded against the country for violence against civilians during the episode (camp abuse, chemical or biological use on civilians, genocide, violent border enforcement) | +15 | Once per phase |

Failure caused by a destroyed route, a lost state or genuine lack of capacity raises no Wrath, though the people remain exposed.
The Condemnation link reads the incident record the Condemnation owner already writes; Event 085 does not judge ideology or emergency laws by itself.

## How Wrath changes harm

For every pre-tenth plague, the Wrath multiplier is:

`0.50 + 1.50 × (Divine Wrath / 100)²`

It gives 0.50 at Wrath 0, 0.875 at 50 and 2.00 at 100.
Evolution and recurrence intensity multiply it (Part 9); completed protection reduces the exposure it applies to.
The tenth plague uses its own hazard formula in [Part 8](085_ten_plagues_of_egypt_spec_part_08_the_tenth_plague_and_population.md).

The multiplier is applied in each consequence's own unit: food pressure as a Famine component, deaths as a population transaction, building damage bounded by what exists, and production penalties within the crisis spirit's ceilings (Part 15).

## Recovery of conduct

A country is never trapped at high Wrath.
Every protective phase has a local route that needs no trucks and no factory minimum (Part 14), and foreign relief can supply missing material.
A government can change course midway: earlier deaths remain and late repentance cannot backdate Passover, but relief before the later plagues lowers Wrath, protects survivors and helps end recurrence.

When territory changes hands, completed local protection stays with the state.
Wrath does not transfer with refugees, and a government cannot shed its record by releasing a puppet or changing its name; succession rules are in [Part 9](085_ten_plagues_of_egypt_spec_part_09_evolutions_and_the_plagues_without_end.md).
