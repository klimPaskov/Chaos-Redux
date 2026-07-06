# Secret Alliance values and tuning plan

The numbers below are tuning bands, not final constants. Implementation should centralize thresholds and scaling in script constants or documented tuning helpers where supported.

## Visible value bands

| Value | Low | Medium | High | Critical |
| --- | --- | --- | --- | --- |
| Evidence | rumours only | named suspect possible | confirmed member possible | public dossier credible |
| Preparedness | exposed country | partial defenses | hardened internal lines | reveal-war shock mostly neutralized |
| Diplomatic isolation | neutral world | suspicion around player | third parties doubt player | pact propaganda dominates |
| Pact cohesion | members distrust each other | functional network | disciplined network | war bloc nearly inevitable |
| Pact readiness | meetings only | operations underway | war planning | reveal or war soon |
| War Clock | public pressure | ultimatums | mobilization | war imminent |

## Dynamic factors

Evidence gain should scale with:

- investigation choice difficulty
- member stability
- player agency or equivalent
- decryption and intelligence advantage
- pact incident severity
- member role
- prior successful missions

Preparedness gain should scale with:

- actual resource spending
- unit placement in required states
- supply state
- industry size
- player war state
- focus or idea hooks that support defense

Sabotage severity should scale with:

- evolution stage
- pact readiness
- pact role source
- major patron presence
- player Preparedness mitigation
- target state value
- chaos tier

Invitation chance should scale with:

- pact cohesion
- player isolation
- candidate motive score
- candidate faction state
- geography and diplomatic access
- major patron presence
- chaos tier

War Clock should scale with:

- public pact size
- major count
- border member count
- player Preparedness
- player Evidence
- current wars
- member confidence
- global chaos tier

## Suggested duration bands

| Mission class | Duration direction |
| --- | --- |
| easy investigation | 90 to 110 days |
| medium investigation | 120 to 160 days |
| hard inquiry or network turn | 150 to 210 days |
| border watch | 90 to 180 days depending on border size |
| public war countdown | enough time for final decisions, usually not less than 60 days unless hard reveal fired |

## Balance principles

- A player who ignores the hidden phase should still be able to fight the public pact, but should suffer surprise and stronger pact cohesion.
- A player who investigates well should not always prevent the pact, but should reduce membership, lower enemy coordination, and prepare the first war months.
- A player who overreacts with weak evidence should make the pact easier to justify.
- A very peaceful player should face a slower, more defensive pact.
- A very aggressive player should face more willing members and worse diplomatic isolation.
- Major patron involvement should be frightening but not automatic every campaign.
