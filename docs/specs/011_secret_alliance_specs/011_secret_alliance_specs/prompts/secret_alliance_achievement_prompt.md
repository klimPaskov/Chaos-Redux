# Achievement prompt for 011 Secret Alliance

Implement achievements only after the main mechanic exists. Follow existing Chaos Redux achievement patterns, asset rules, localisation rules, and documentation alignment. Achievement titles and descriptions below are direction only. Write final localisation during implementation.

## Planned achievements

### chaosx_secret_alliance_read_the_room

- visibility: visible
- difficulty: medium
- route: hidden phase investigation
- eligible country: player country targeted by Secret Alliance
- unlock: identify at least two original full signatories before public reveal
- disqualifier: trigger public reveal before the second member is confirmed
- why interesting: rewards noticing the hidden pattern before the faction appears
- icon direction: magnifier with three faint seals

### chaosx_secret_alliance_every_door_locked

- visibility: visible
- difficulty: hard
- route: defensive preparation
- unlock: reach public reveal with high Preparedness and no severe sabotage success after the dossier opens
- disqualifier: severe industrial, rail, port, or officer incident succeeds after the dossier phase begins
- icon direction: locked factory, rail, and port motif

### chaosx_secret_alliance_the_empty_chair

- visibility: hidden
- difficulty: hard
- route: diplomacy and evidence
- unlock: force the Convener or major Patron to withdraw before public reveal through evidence, inquiry, or negotiation
- disqualifier: withdrawal caused only by unrelated capitulation or annexation
- icon direction: abandoned chair at meeting table

### chaosx_secret_alliance_pact_against_me

- visibility: visible
- difficulty: medium
- route: revealed war survival
- unlock: survive the reveal war until one full signatory capitulates, exits, or signs a separate exit
- disqualifier: none beyond normal achievement validity
- icon direction: central country silhouette surrounded by seals

### chaosx_secret_alliance_no_shadow_left

- visibility: visible
- difficulty: very hard
- route: decisive counter-network victory
- unlock: collapse the public pact while maintaining high Evidence and preventing outer-ring members from joining the war
- disqualifier: use of a forced debug or manual scenario bypass if such tools exist
- icon direction: exposed lamp cutting network threads

### chaosx_secret_alliance_bad_guess

- visibility: hidden
- difficulty: challenge
- route: recovery from diplomatic mistake
- unlock: accuse an innocent country, repair credibility through inquiry or proof, and expose the real pact before war
- disqualifier: the innocent country becomes a full member before proof is found
- icon direction: cracked false stamp and cleared file

### chaosx_secret_alliance_three_knives_one_table

- visibility: hidden
- difficulty: hard
- route: baseline mastery
- unlock: identify all original three full signatories before Evolution II major patron entry
- disqualifier: major patron joins before all three are identified
- icon direction: three daggers beside a sealed document, no gore

### chaosx_secret_alliance_public_enemy_number_one

- visibility: hidden
- difficulty: very hard
- route: dangerous public war
- unlock: face a public pact with two major members and defeat or force exit from the full faction
- disqualifier: second major joined through debug or invalid forced state
- icon direction: spotlighted central file with two major seals in shadow

### chaosx_secret_alliance_quietly_undone

- visibility: hidden
- difficulty: very hard
- route: hidden diplomatic victory
- unlock: dissolve the hidden pact before public faction formation through evidence, exits, and cohesion collapse
- disqualifier: public faction forms first
- icon direction: closed file with cut red strings

## Tracking notes

The implementation likely needs achievement flags for:

- original three member identification count
- severe sabotage success after dossier opened
- Convener or Patron withdrawal source
- innocent accusation recovery path
- outer-ring conversion count at reveal
- two-major public pact state
- hidden pact dissolved before public faction state

Achievement UI should not reveal hidden member identities before the player discovers them.
