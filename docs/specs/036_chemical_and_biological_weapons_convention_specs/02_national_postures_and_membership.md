# National postures and membership

Per-posture rights, relief, access, and transitions are tabulated in [the posture matrix](matrices/national_posture_matrix.md).
This file owns posture behaviour and the membership transactions.

## Posture model

Every eligible country holds one public posture in one country variable:

1. Full Ratification
2. Chemical Accession Only
3. Retaliation Reservation
4. Public Rejection

The opening offers a fifth response, "Reject publicly, prepare in secret", which records Public Rejection and starts the covert program described below.
The covert program is a country flag, not a fifth posture, so every public system reads the same four values.

Changing posture runs one atomic owner effect that updates the registry, the posture idea, AI strategy, decision visibility, Standing, and the Opposition Leader.

The posture never grants a technology, payload, stockpile, delivery system, special project, or nuclear weapon.
Every ordinary research, production, readiness, delivery, target, and payload gate still applies.

## Posture idea

Each member posture uses one visible event-owned idea whose tooltip states the posture and the derived permission line from [00](00_master_spec.md#public-information-budget).

The idea carries small research-speed and production modifiers for the families the posture accepts and no combat statistics.
Public Rejection uses no idea, so opponents carry no hidden bonus.

The idea is replaced atomically on every posture change and removed on withdrawal, expulsion, or invalidity.

## Full Ratification

The country accepts chemical and biological normalization.
It can ratify every treaty family, receives chemical, biological, and nuclear relief from [03](03_condemnation_normalization_and_cbrn_integration.md#source-multipliers), and can join every project its provider permits.

## Chemical Accession Only

The country accepts chemical articles and keeps the biological prohibition.

It never receives biological cooperation, biological relief, biological clauses, or biological projects through Event 036.
It counts as a member for chemical and general votes, as a non-member for biological clauses, and as half weight for Standing.

## Retaliation Reservation

The country joins the protective, inspection, and retaliation infrastructure and publicly refuses first use.

Its relief applies only to retaliation proved by the existing bilateral Retaliation Authority ledger ([CBRN diplomacy actions](../../systems/cbrn_warfare/cbrn_diplomacy_actions.md#retaliation-authority)).

Offensive first use breaks the reservation through the breach consequence in [03](03_condemnation_normalization_and_cbrn_integration.md#reservation-breach).

After Evolution I, the country may repeal the reservation through Revise Posture and become Full Ratification or Chemical Accession Only.

## Public Rejection

The country keeps normal Condemnation treatment and receives no convention benefits.

It can use Organize Opposition, the existing CBRN diplomacy actions, and Seek Accession after its cooling period.

Opponents coordinate through AI sanction scoring and the Opposition Leader, never through a new faction.

The Opposition Leader is the public opponent with the highest Standing weight, with total factories breaking ties.
It is reselected inside membership-changing transactions.
Its only special role is that its Organize Opposition counts double against the current agenda, which makes the opposition route a real contest for the opposition achievement.

## Covert program

A Public Rejection country can run a covert program from the opening response or later through Begin Covert Program.

The program raises AI research and production priority for one chosen family, chemical or biological, and opens hidden program decisions in [09](09_decisions_missions_costs_and_visibility.md#posture-actions).
It grants nothing directly.

While it runs, each covert action records hidden cover-up evidence through `condemnation_add_source` with Hidden visibility and the `concealment_operation` context, so the existing inspection and observer disclosures can reveal it.

Exposure happens when a disclosure path makes any of that evidence public or when an Inspection and Verification Protocol inspection targets the country.
Exposure fires a public report, clears the covert flag, sets an exposed memory flag, closes covert decisions, and lets foreign AI react through the normal Condemnation refresh.

End Covert Program closes it without exposure, and completed research and recorded evidence remain.

## Registries

The owner keeps bounded country arrays:

- members, with the posture read from each country's variable
- public opponents
- treaty ratifiers, one array per active treaty
- active project participants

A country appears once per array.
Arrays can be rebuilt from country variables, so no versioned membership generation is needed.

## Accession after the opening

A public opponent may begin a 90-day Accession Review mission after 180 days without a posture change.

The country chooses Full Ratification, Chemical Accession Only, or Retaliation Reservation at completion.
A covert country must end or be exposed in its program first.

A new member joins only treaties that are still open for ratification and must ratify later agendas normally.

## Posture revision

Members can revise their posture once 365 days have passed since their last public change.

Allowed revisions:

- between Full Ratification and Chemical Accession Only, both ways
- from either to Retaliation Reservation
- from Retaliation Reservation to Full Ratification or Chemical Accession Only, only after Evolution I
- from any member posture to Public Rejection through withdrawal

Revision costs political power and a temporary stability penalty, and starts the 365-day lock again.
A revision applies only to future actions, because relief is applied once when each action happens.

## Withdrawal

Withdrawal is a 90-day Withdrawal Notice mission.
During the notice the country keeps its obligations and cannot start another posture change.

Completion removes future benefits, voting rights, treaty ratifications, and project access.
It never erases action records, earlier Condemnation, contribution costs, or breach memory.

A country that withdraws during a project keeps its contribution receipt but receives no grant unless it is an active participant at completion.

## Suspension and expulsion

A member is suspended for refusing an inspection demanded under the Inspection and Verification Protocol, failing a Declaration Deadline, or abandoning an Assistance Guarantee while ratified to the Protection and Assistance Compact.

Suspension removes voting and new contributions for 180 days while keeping the posture.
A second suspension inside two years expels the country to Public Rejection with an expelled memory flag.

## Subjects and factions

A subject chooses its own posture when it passes eligibility, and AI overlords influence AI subjects only through weights.
Faction membership never forces convention membership, and one member's posture never grants permissions to its faction.
