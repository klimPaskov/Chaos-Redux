# Event 011 Secret Alliance AI matrix

## Pact member AI

| Actor | Ordinary behavior | High pressure behavior | Avoids |
| --- | --- | --- | --- |
| Founding minor | Diplomatic chill, courier circuit, press campaign | Sabotage support and public reveal support | Solo war against strong target |
| Wavering minor | Low-risk support, accepts patron backing | Leaves if target evidence and diplomacy are strong | Fanatical war unless trapped |
| Bordering minor | Courier routes and border provocation | Border operation resistance and war readiness | Deep sabotage if own border is weak |
| Distant minor | Press campaign and diplomacy pressure | Public faction support after reveal | Expensive military action |
| Major patron | Cohesion, sabotage, guarantees, war council | Ultimatum and public leadership | Joining if same faction as target or already unstable |
| Rare second major | Joins only if target failed counter-play and pact cohesion high | Public faction backing | Joining when evidence is high or patron weak |

## Target AI action weights

| Target condition | Priority actions |
| --- | --- |
| Has intelligence agency | Trace pouches, break radio net, turn courier |
| No agency | Audit missions, secure ministries, guard rail nodes |
| Low stability | Secure capital ministries, quiet diplomacy, avoid risky leaks |
| Strong army | Contingency plans, border readiness, public war case |
| Weak army | Face-saving exits, pressure neutrals, industrial defense |
| Neighboring member known | Sweep safehouses, seal courier pass, hold border |
| Major patron suspected | Expose patron hand, rally friendly governments |
| Evidence high | Build public dossier, controlled leak, prepare war case |
| Pact pressure high | Fuel reserve security, local defense committees, emergency defense |

## Foreign AI reaction

| Actor type | Reaction to hidden pact | Reaction to public evidence | Reaction to open pact |
| --- | --- | --- | --- |
| Target ally | Suspicion only if relations are high | Diplomatic support and possible guarantee | Aid, volunteers, or faction support |
| Neutral neighbor | May be recruited or pressured | Can warn target if relations high | Chooses neutrality, target support, or pact sympathy |
| Rival of target | Receives covert support | May validate pact claims | May cooperate with public pact if not already in war |
| Existing faction leader | Discourages members from joining hidden pact | Condemns or exploits evidence | May oppose pact if it threatens faction balance |
| Special chaos country | Excluded from pact logic | No normal diplomatic behavior | No normal diplomatic behavior |

## AI safety checks

- Do not evaluate a decision if the selected member is gone.
- Do not target the same member with duplicate active missions.
- Do not join hidden pact if already at war with target.
- Do not invite a country inside target faction.
- Do not let AI fire border operations against non-neighbor members.
- Do not let a major patron force reveal when it cannot lead, join, or support the faction.
- Do not let public pact war logic call invalid members repeatedly.
- Do not let AI choose settlement or exit paths after direct war has begun unless the war state allows it.

## AI personality tuning direction

| AI personality or situation | Pact willingness | Target response |
| --- | --- | --- |
| Expansionist authoritarian | High if target is rival | Strong war preparation |
| Defensive democracy | Low unless target is aggressive | Evidence and diplomacy first |
| Isolated minor | Medium if patron exists | Defensive security first |
| Faction leader | Medium to high if target is rival | Rally allies and expose patron |
| Trade-dependent minor | Medium if members can protect trade | Quiet talks and concessions |
| High chaos actor | Higher risk tolerance | Faster preparation and public reveal |
