# Event 036 achievements

## Achievement design rules

These are working titles and stable technical IDs.

Final names and descriptions require the localisation pass.

Each achievement needs:

- exact tracking flags and variables
- unlock trigger
- disqualifiers
- save persistence
- three achievement image states
- documentation
- catalog or achievement surface alignment

Achievements must use CBRN action records, treaty receipts, posture history, project receipts, and source-event isolation proofs.

They must not infer conduct from current ideas alone.

## `chaosx_036_the_reservation_holds`

Working title: The Reservation Holds.

Playable challenge: remain inside the convention without authorizing offensive first use.

Requirements:

- adopt Retaliation Reservation during the opening or before Evolution I
- remain an active reservation member when Evolution III activates
- ratify the Protection and Assistance Compact
- ratify the Inspection and Verification Protocol
- ratify a Retaliation Guarantee
- never create a chemical, biological, or nuclear action record marked as first use

Valid retaliatory use does not disqualify the achievement.

Disqualifiers:

- repeal the reservation
- initiate chemical, biological, nuclear, or thermonuclear use
- leave the convention before Evolution III
- use a covert preparation route

Icon direction: a sealed treaty beneath a gas mask and shield, with an unbroken red line across offensive weapon silhouettes.

## `chaosx_036_a_convention_against_the_convention`

Working title: A Convention Against the Convention.

Playable challenge: lead the public opposition and break the permissive order through diplomacy.

Requirements:

- choose Public Rejection without covert preparation
- become the Opposition Leader
- after Evolution II becomes active, either defeat the Arsenal Without Limits vote or reduce Convention Standing from Established or Dominant to Provisional through public withdrawals
- keep the country’s public Condemnation below Formal Censure at completion

Disqualifiers:

- join the convention
- start covert preparation
- initiate a public unconventional attack
- lose Opposition Leader status before the decisive outcome

Icon direction: a treaty document split by a clean black prohibition bar, surrounded by withdrawing national seals.

## `chaosx_036_small_state_large_ledger`

Working title: Small State, Large Ledger.

Playable challenge: make a minor country indispensable to a shared Chaos weapon project.

Snapshot requirement at project selection:

- country is not a major
- country has no more than 15 total civilian and military factories

Completion requirements:

- complete at least three distinct contribution families
- contribute at least `8%` of the final applied project progress
- remain an active valid participant at completion
- receive the registered prerequisite through the program

Disqualifiers:

- become a major before the first contribution completes
- receive the prerequisite through the normal route before program completion
- withdraw before completion

Icon direction: a small national ledger beside a large shared laboratory apparatus, with three distinct contribution symbols entering one progress seal.

## `chaosx_036_without_the_incident`

Working title: Without the Incident.

Playable challenge: complete a registered Chaos weapon route without triggering its source incident.

Requirements:

- participate in a successful International Chaos Weapons Program project
- receive the registered prerequisite
- prove that the source event was not fired
- prove that the normal source route remained unavailable immediately before the atomic completion transaction
- prove that no source crisis, country, evolution, threat, super-event, or terminal state was activated by the grant

Disqualifiers:

- source event fires before completion
- project is cancelled by normal availability
- prerequisite was already owned before the project

Icon direction: an unopened event dossier beside a completed research key, with the incident seal visibly intact.

## `chaosx_036_the_secret_article`

Working title: The Secret Article.

Playable challenge: maintain a concealed unconventional program behind public rejection.

Requirements:

- choose Public Rejection with Covert Preparation
- complete one valid chemical or biological research milestone through ordinary research
- reach the provider-defined minimum compatible stockpile or readiness threshold
- remain unexposed for 365 days after both conditions are true

Disqualifiers:

- join the convention before the timer completes
- end covert preparation
- become publicly exposed
- receive the capability through a free grant or invalid route

Icon direction: a folded treaty page concealing a laboratory diagram and sealed cylinder, with a narrow intelligence-eye motif.

## `chaosx_036_masks_before_missiles`

Working title: Masks Before Missiles.

Playable challenge: build protection and survive an enemy unconventional attack without initiating one.

Requirements:

- ratify the Protection and Assistance Compact
- ratify the Inspection and Verification Protocol
- ratify a Retaliation Guarantee
- reach the owner-defined high protection state
- become the victim of a valid hostile chemical, biological, or nuclear action
- receive a casualty-mitigation receipt proving that protection reduced harm
- never create a first-use CBRN action record

Disqualifiers:

- initiate unconventional use
- falsify an inspection declaration
- leave every relevant protection treaty before the hostile action

Icon direction: rows of gas masks and medical filters in the foreground, with a distant missile silhouette stopped by a protective shield.

## `chaosx_036_all_articles_invoked`

Working title: All Articles Invoked.

Playable challenge: use the complete permissive doctrine in one war.

Requirements:

- hold Full Ratification
- ratify a chemical and biological first-use article
- ratify the Strategic WMD Doctrine Charter
- ratify the Arsenal Without Limits Articles
- during one continuous war, create one valid attributed chemical first-use action record
- during the same war, create one valid attributed biological first-use action record
- during the same war, create one valid attributed nuclear first-use action record

Disqualifiers:

- use a thermonuclear weapon for the nuclear requirement
- use a doomsday effect
- satisfy two requirements from one duplicated action record
- lose the required ratifications before the third action

Icon direction: three distinct chemical, biological, and nuclear symbols arranged as clauses around one signed military doctrine seal.

## Achievement tracking architecture

Use event-owned stable flags for route history and arrays or variables for project share.

Use the shared CBRN action ledger for first-use, retaliation, victim, attribution, and weapon-family proof.

Use treaty receipts for ratification proof.

Use the project history for source isolation and contribution proof.

Snapshot small-country eligibility when the project is selected so later economic growth does not invalidate legitimate play.

Every achievement must remain disabled in observer, invalid setup, or unsupported test states according to the repository achievement framework.

## Asset requirements

Each achievement needs an original asset family designed for the achievement surface.

Create the normal, grey, and not-eligible states under the root achievement folder using filenames that match the full achievement ID.

Do not derive the achievement art by resizing a decision or idea icon.
