# Event 036 achievements

Titles are working titles and the ids are stable.
Each achievement needs tracking flags, an unlock trigger, disqualifiers that survive save and reload, localisation, and the three image states from [14](14_asset_requirements.md#achievement-assets), following [the custom achievements system](../../systems/custom_achievements.md).

Proof comes from posture history flags, treaty ratification receipts, the CBRN action ledger, and program contribution receipts.
A current idea or posture alone never proves a route, and a disqualified route never becomes valid again.

## `chaosx_036_the_reservation_holds`

The Reservation Holds: stay inside the convention to the end without ever starting a war of gas or plague.

Requirements:

- hold Retaliation Reservation from the opening or from before Evolution I
- still hold it when Evolution III is recorded
- have ratified the Protection and Assistance Compact and the Inspection and Verification Protocol
- never appear as attacker on a CBRN ledger row marked first use

Valid retaliation does not disqualify.
Repeal, withdrawal, expulsion, a reservation breach, or a covert program disqualifies.

Icon direction: a sealed treaty under a gas mask and shield, with an unbroken red line across offensive weapon silhouettes.

## `chaosx_036_a_convention_against_the_convention`

A Convention Against the Convention: lead the opposition and break the permissive order through diplomacy.

Requirements:

- hold Public Rejection from the opening without ever running a covert program
- be the Opposition Leader when the decisive outcome happens
- after Evolution II is recorded, either see an Arsenal Without Limits agenda fail or see Standing fall from Established or Dominant to Provisional
- have public Condemnation below Formal Censure at that moment

Joining the convention, starting a covert program, or appearing as attacker on a first-use ledger row disqualifies.

Icon direction: a treaty split by a clean black prohibition bar, surrounded by withdrawing national seals.

## `chaosx_036_small_state_large_ledger`

Small State, Large Ledger: make a minor country indispensable to a shared weapons program.

Requirements:

- when the project is selected, the country is not a major and has at most 15 civilian and military factories, recorded as a snapshot
- complete contributions in at least three different families for that project
- apply at least `8%` of its final progress
- receive the grant at completion

Withdrawal before completion or receiving the project through another route first disqualifies for that project.

Icon direction: a small national ledger beside a large shared apparatus, with three contribution symbols entering one seal.

## `chaosx_036_without_the_incident`

Without the Incident: receive a Chaos weapon project through the program before the world ever sees its source event.

Requirements:

- receive a program grant at completion
- the grant's provider still had a false global normal-route proof at completion, which the completion transaction already guarantees

Icon direction: an unopened dossier beside a completed research key, with its seal intact.

## `chaosx_036_the_secret_article`

The Secret Article: keep a covert program hidden while the world believes your rejection.

Requirements:

- run a covert program
- research one chemical or biological technology of the program's family while the program runs
- hold at least one unit of a chemical or biological payload of that family in stock
- stay unexposed for 365 days after both conditions are met

Joining the convention, ending the program, or exposure before the timer ends disqualifies.

Icon direction: a folded treaty page hiding a laboratory sketch and a sealed cylinder, with a narrow eye motif.

## `chaosx_036_masks_before_missiles`

Masks Before Missiles: take a gas or plague attack and come through it without ever striking first.

Requirements:

- have ratified the Protection and Assistance Compact
- be the affected country of a confirmed hostile CBRN ledger row while ratified
- receive at least one Assistance Guarantee delivery or decontamination mission from another ratifier for that attack
- end that war without capitulating
- never appear as attacker on a first-use ledger row

Icon direction: rows of gas masks and filters in the foreground, with a distant missile stopped by a shield.

## `chaosx_036_all_articles_invoked`

All Articles Invoked: use the whole permissive doctrine in one war.

Requirements:

- hold Full Ratification with both First-Use Revision clauses, the Strategic WMD Doctrine Charter, and the Arsenal Without Limits Articles ratified
- during one continuous war, appear as attacker on a chemical first-use ledger row and a biological first-use ledger row
- during the same war, carry out a non-thermonuclear nuclear strike

Thermonuclear strikes, Final Silence, and doomsday releases do not count, and losing a required ratification before the last action disqualifies.

Icon direction: chemical, biological, and nuclear symbols arranged as clauses around one signed doctrine seal.

## Asset rule

Each achievement has its own master art and its normal, grey, and not-eligible states, never resized from a decision or idea icon.
