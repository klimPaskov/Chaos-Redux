# Secret Alliance AI matrix

| Actor group | Ordinary behavior | High chaos behavior | Avoid |
| --- | --- | --- | --- |
| Convener minor | maintain secrecy, host meetings, invite compatible minors slowly | invite faster, pressure outer ring to sign | declaring war before pact readiness unless revealed by external war |
| Saboteur minor | low-damage industrial and rail sabotage | serious sabotage and assassinations in Evolution II | repeated severe sabotage when player Preparedness is high and evidence is low |
| Agitator minor | propaganda and diplomatic isolation | public threats, ideological calls, faster War Clock | joining if ideology is friendly to player without strong motive |
| Border Hand minor | patrol incidents and border watch counterplay | controlled border provocations and war pressure | border incident when it has no border or valid route |
| Banker minor | fund others and hide traces | arms shipments and bribes | direct war leadership |
| Major Patron | fund, protect, and conceal pact | seize leadership, invite more members, prepare war | joining when already collapsing in another war |
| Second major | rare late escalation | join if player isolation and pact cohesion are high | nonsensical enemy-patron pairing without chaos justification |
| Defensive-fear member | cautious signatory, accepts face-saving exit | stays if player is frightening and patron strong | extreme sabotage as default |
| Ideological-hostility member | propaganda and hard commitment | sabotage, war planning, refuses exit | backing down unless defeated or exposed |
| Opportunist member | joins when pact looks safe | rushes to full membership if player weak | staying after pact cohesion collapses |
| Neutral observer | judge evidence and relations | more likely to fear player or patron pressure | certifying weak evidence automatically |
| Player ally | support investigations if evidence is shared | send stronger diplomatic or military help | knowing hidden members without exposure path |
| Innocent suspect | resent accusation, seek inquiry | drift toward pact if humiliated | becoming confirmed member without a join path |

## AI weights by condition

AI should increase pact willingness when:

- player has high world tension contribution
- player borders the country and is much stronger
- player recently annexed, puppeted, or attacked minors
- ideological hostility is high
- player is fighting elsewhere
- pact has a major patron
- pact cohesion is high

AI should decrease pact willingness when:

- country is a player subject or dependent
- country is at war with player at selection time
- country is in a faction with incompatible obligations
- country has very low stability and fears collapse
- player evidence is high and public
- pact cohesion is low
- major patron has been exposed or defeated
- country is an outer-ring member offered a face-saving exit

## War entry behavior

Full signatories join revealed war by default when hard reveal fires. Armed associates evaluate confidence, ideology, patron pressure, and player isolation. Liaisons normally withdraw unless chaos is high and pact cohesion is strong.

## Defection behavior

Members can withdraw or seek separate exit when:

- Evidence against the network is high
- Pact cohesion is low
- Convener or Patron is defeated
- player offered a safe exit before reveal
- member motive is defensive or opportunist
- member is losing badly and major patron cannot protect it
