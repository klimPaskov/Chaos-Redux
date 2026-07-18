# Event 19 Achievement Matrix

Titles below are working labels, not final player-facing localisation. Final titles and descriptions must be written during implementation from the direction supplied here.

## Achievement set

| Working ID | Eligibility | Unlock condition direction | Disqualifiers | Visibility | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| `019_infantry_spawn_every_rifle_accounted_for` | any country | close a very large generation with high control, low congestion, no revolt, and no unresolved debt | claimant takeover, derivative revolt, debug or forced completion | visible | hard | complete roster, stacked rifles, sealed ledger |
| `019_infantry_spawn_one_battalion_wonder` | any country | an exact one-combat-battalion event division wins its controlled one-formation trial and survives | template expanded before trial | hidden | hard | lone battalion marker against a large front |
| `019_infantry_spawn_the_army_has_voted` | any country under Evolution III | accept or suffer a claimant takeover, then win a major war or survive a long specified period | claimant removed before proof | visible | hard | ballot box crossed with command baton, no readable text |
| `019_infantry_spawn_order_from_noise` | any country | at Evolution III, integrate many distinct random lots while ending at very high control and low congestion | use of forced scenario setup | visible | very hard | chaotic unit symbols arranged into a precise formation |
| `019_infantry_spawn_combined_arms_accident` | any country | an exact Evolution III random division with at least eight distinct combat-component types wins its controlled one-formation trial | deliberate template edit removes generated identity | hidden | very hard | mismatched cavalry, armor, bicycle, and artillery silhouette |
| `019_infantry_spawn_no_room_on_the_train` | any country with a large generation | keep the main supply network functional while integrating a specified high division count | rail mission failure or emergency exploit | visible | hard | train surrounded by unit markers without derailment |
| `019_infantry_spawn_borrowed_future` | any country | an exact advanced event formation wins its controlled one-formation trial while one recorded technology gate remains locked | obtaining the recorded technology first, cloning template equipment | hidden | hard | advanced vehicle emerging from an old depot |
| `019_infantry_spawn_three_false_apocalypses` | any ordinary country | defeat zombie, ghost, and golem derivative countries in one campaign while parent event identities remain distinct | playing a derivative, forced parent-event merge | visible | extreme | three contained silhouettes behind separate seals |
| `019_infantry_spawn_barracks_of_babel` | any country | an exact Evolution III random division containing camelry, bicycle infantry, amphibious armor, a flame element, artillery, and engineers wins its controlled one-formation trial | manual template construction | hidden | extreme | impossible mixed column, readable at 64 by 64 |
| `019_infantry_spawn_quiet_demobilisation` | any country | supervised demobilization of a very large generation with no revolt, no equipment exploit, and stable control | emergency instant removal, claimant seizure | visible | hard | orderly stacks, departing columns, intact seal |
| `019_infantry_spawn_every_barracks_a_front` | triggerable scenario | survive or win under Maximum General Mutiny or Anomalous Rising with the starting country and no terminal world-end state | lowering intensity after launch, tag switching | visible | extreme | country outline filled with many hostile formation markers |

## Tracking notes

### Generated-identity preservation

Achievements involving a random division need a persistent division or lot identity. Manual template editing, deleting, or converting the division must not satisfy a generated-composition achievement unless the achievement explicitly allows standardized follow-up.

### Controlled combat trials

The four exact-formation combat achievements use state-targeted controlled
border trials. The selected attacker state must contain exactly one qualifying
Event 19 division and no other formation. An empty adjacent state owned by a
peaceful independent AI country receives exactly one locked temporary defender.
The engine enforces a fourteen-day minimum engagement and leaves state ownership
unchanged. The shared mission times out after forty-five days, and every started
trial applies the same ninety-day cooldown.

Each trial revalidates immutable unit, generation, lot, template, composition,
material-quality, coherence, readiness, and technology evidence before launch
and before an attacker victory is recorded. The transaction pays its own Army
Experience and Command Power cost, applies a shared cooldown after a started
trial, and cleans up through a country-local nonce on victory, loss,
cancellation, invalidation, or timeout. No casualty, enemy-strength ratio, or
ordinary country-combat proxy is part of the contract.

Scenario host preflight rejects the active trial attacker, the temporary
opponent, an opponent held by failed-cleanup quarantine, and any country whose
same-tag scenario setup or rollback transaction is not idle. Successful cleanup
releases the opponent lock only after proving that no nonce-marked defender and
no temporary trial template remain.

### Parent-isolation achievement

`three_false_apocalypses` must verify derivative origin flags rather than infer from unit appearance alone. It should also verify that the player did not simply defeat the parent Zombie or Death actor and count it as a derivative.

### Scenario achievement

The scenario achievement reads stored launch type and intensity. The temporary bypass flag is not the achievement source.

## Achievement text direction

- Titles can use military, bureaucratic, and darkly absurd language.
- Descriptions should state the visible challenge without revealing hidden random thresholds.
- No achievement text should be advertised in ordinary event, focus, or decision descriptions.
- Historical coercive mobilization should not be treated as slapstick.
