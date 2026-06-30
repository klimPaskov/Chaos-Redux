# Event 011 Secret Alliance progression map

This is a route sketch for implementation planning. It is not a focus tree layout.

```text
Root event
  selects target country
  selects three valid minor founders
  stores hidden compact state
  opens baseline reports after a short delay

Baseline hidden compact
  diplomatic chill
  press campaign
  courier circuit
  industrial survey
  suspicion rises slowly

Suspicion threshold or Evolution II
  decision category opens
  Dossier Board can open from category
  investigation actions
  defensive actions
  diplomacy actions
  war preparation actions

Evolution I
  minor invitations
  more visible coordinated pressure
  covert support to target rivals
  suspicion rises faster

Evolution II
  major patron can join or found evolved opening
  sabotage attempts
  provocations
  assassination and abduction attempts
  neighboring member border operations
  target can weaken pact before reveal

Reveal gates
  member enters war with target
  evidence reveal
  leak reveal
  ultimatum reveal
  major patron public leadership

Evolution III public compact
  faction named Anti-[target country] Pact
  member cards fully public
  war option available
  all valid members join war if war caused reveal
  public crisis decisions replace hidden actions

After public crisis
  demand disbandment
  isolate patron
  call friendly governments
  prepare or start war
  settle if enough members are wavering
  cleanup when pact no longer has valid members
```

## Main state transitions

| From | To | Transition cause | Player agency |
| --- | --- | --- | --- |
| Root event | Baseline hidden compact | Three valid founders selected | None yet, player receives subtle report later |
| Baseline | Suspicion layer | Repeated patterns or suspicion threshold | Indirect, through existing country setup and reactions |
| Suspicion layer | Counter-play layer | Evolution II, serious incident, or evidence threshold | Player chooses investigation, defense, diplomacy, and preparation |
| Counter-play layer | Public reveal | War, evidence, leak, pressure, or patron reveal | Player can reveal early, delay, split members, or prepare |
| Public reveal | Public crisis | Faction appears and member cards are public | Player chooses war, diplomacy, isolation, or emergency defense |
| Public crisis | Aftermath state | Pact defeated, disbanded, or reduced below valid member count | Player outcome depends on preparation and war result |

## Evolution entry paths

| Evolution | Active-event path | Pre-fire path |
| --- | --- | --- |
| Evolution I | Existing pact unlocks minor invitations and stronger pattern reports | Root event weights prefer better-connected hostile minors |
| Evolution II | Existing pact can add a major patron and opens counter-play | Root event can start with a major founder plus two minors when a valid major exists |
| Evolution III | Existing pact prepares public reveal after counter-play window | Root event starts from Evolution II and reaches public reveal after a compressed delay |
