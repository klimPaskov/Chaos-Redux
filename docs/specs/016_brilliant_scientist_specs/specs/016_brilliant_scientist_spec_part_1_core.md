# Event 16 Brilliant Scientist, core specification

All route names, event names, option tones, achievement names, and super-event labels in this file are working labels, not final localisation.

## Event identity

Event ID 16 begins as a minor fire-once event. A random eligible country receives Doctor Warren Kruger, a brilliant scientist whose work accelerates research at an impossible rate. The simple surface is the promised research advantage. The real event is about a government deciding how much sovereignty to give one mind before that mind becomes a power center.

The event should not create a generic science minigame for every country. It should create one living relationship between one host country and Warren Kruger. The host receives extraordinary research output, project access, special-project scientist access, and national attention. The price is that Kruger collects facilities, personnel, secrecy, legal exceptions, and military assets that can later become the foundation of his own state.

## Core fantasy

The player finds a scientist who can compress years of research into months. At first, the country gets better laboratories, new advisors, research breakthroughs, and a powerful special-project scientist. Later, the player realizes that every granted privilege has created a chain of custody that no ordinary ministry controls.

The strongest version of the event makes the player ask four questions:

- Do we keep Kruger inside public institutions or hide him in a military laboratory.
- Do we spend ordinary resources to keep the work safe or approve strange projects for faster breakthroughs.
- Do we protect him from foreign pressure or let the world court him.
- Do we stop him before he can leave, knowing that an attempted arrest can become the trigger for rebellion.

## Baseline event flow

The baseline event fires for one country that can reasonably use research speed. The country should normally exist, have a capital, have at least one research slot, and not be a special nonhuman chaos country. The exact implementation can choose eligible countries dynamically.

The opening creates Doctor Warren Kruger as:

- A country advisor using a copied and renamed base portrait derived from `portrait_generic_biowarfare_europe_male_01`.
- A special project scientist available in every special project field under the same public name.
- A hidden actor target for event logs, evolutions, decisions, project approvals, foreign reactions, and possible rebellion.
- A national research acceleration package that can satisfy the user request for a 100 percent research speed advantage.

The player-facing opening should present Kruger as unusually gifted, unnervingly precise, and hard for ordinary academics to explain. The alien possibility should be hinted through impossible habits, wrong memories, and calculations that arrive before instruments finish measuring. It should not be confirmed at baseline.

## Opening choices

The player should receive several paths, with AI always accepting Kruger.

### Recruit Kruger openly

The host makes him a national figure and attaches him to universities, ministries, and public laboratories. This gives strong research output, raises public fame, lowers early paranoia, and makes foreign states notice sooner.

### Recruit Kruger secretly

The host places him under military security. This gives stronger military, nuclear, electronics, rocket, and special-project output. It raises laboratory autonomy and security burden, and it accelerates the path toward strange projects.

### Send him away

The player refuses the offer and pushes Kruger toward another country. This should not delete the event. It should pick a new eligible host, record that the original country declined him, and create a later foreign reaction if Kruger becomes famous. AI should not choose this.

### Detain for screening

This option should exist only for suspicious or authoritarian routes after a short delay or if the host already has strong intelligence capability. Early detention gives lower output, better information, and a chance to discover anomalies. If used too harshly, it can produce an early escape or assassination attempt.

## The Kruger profile

Doctor Warren Kruger is fictional. He should not be tied to a real historical scientist portrait or biography. His visible identity should sound plausible for a 1930s or 1940s European male scientist, with enough ambiguity that many countries can plausibly recruit him.

Kruger should appear in three roles:

| Role | Gameplay purpose | Visual state |
| --- | --- | --- |
| Advisor | Delivers the baseline research acceleration | Static portrait stage 0 |
| Special project scientist | Makes him usable in every special project field | Same identity with field-agnostic icon treatment |
| Possible country leader | Leads his own breakaway state if rebellion happens | Later portrait stages, with animation for severe stages |

## Main values

The mechanic should use a small set of visible values and a larger set of hidden memory flags.

| Value | Visible to player | Purpose |
| --- | --- | --- |
| Research Momentum | Yes | Shows how much the host is benefiting from Kruger |
| Laboratory Autonomy | Yes | Measures how independent Kruger has become |
| Security Integrity | Yes | Measures protection from spies, sabotage, and internal escape |
| Public Fame | Yes | Measures national and international attention |
| Strangeness | Partly | Signals anomalies without exposing alien truth too early |
| Project Arsenal | Summary only | Records approved project families that later shape rebellion strength |
| Government Leverage | Yes | Measures whether the host can still impose limits |

The player should see the first five clearly in a decision category or mechanic panel. Project Arsenal should be summarized as broad facility types rather than a spoiler list of future rebel armies.

## Baseline rewards and pressure

The baseline should be powerful enough that keeping Kruger is tempting even when the risks appear. A host that accepts him should receive:

- A major research-speed advantage.
- Special-project scientist access across every special project field.
- Faster special-project progress and breakthrough selection.
- A choice of initial research focus that can lean public science, engineering, military research, biology, electronics, rockets, or theoretical work.
- A national spirit or advisor package that can later upgrade, corrupt, or be removed.

The baseline should also start pressure values:

- Laboratory Autonomy begins low for public recruitment and medium for secret recruitment.
- Public Fame begins higher if the public route is selected.
- Security Integrity begins higher if the secret route is selected.
- Strangeness begins hidden or low.
- Government Leverage begins high but falls when the player grants exemptions, private facilities, armed guards, cloned personnel, machine forces, or independent supply chains.

## Event details direction

The Event Details entry should describe a gifted scientist entering one country’s research establishment and changing the pace of modernization. It should mention universities, laboratories, military offices, and rumours of impossible calculations. It must not list the 100 percent research bonus, the hidden rebellion thresholds, the alien branch, or the world-end path.

## Event log and actor direction

The Event Log should show Event 16 as a fire-once event with the host country as actor. Evolutions should be logged with the host country as actor while Kruger remains inside the host. If Kruger rebels, later evolution logs should use the Kruger country as actor when the milestone belongs to him.

## Connections to existing Chaos Redux systems

This event should connect naturally to:

| Existing or cataloged system | Connection direction |
| --- | --- |
| Time Traveler | Time mechanics can make Kruger recognize temporal anomalies or steal methods from the Time Traveler route |
| Alien Spacecraft | Xenotechnology projects can accelerate if alien wreckage or aircraft exist |
| Tomorrow's Girls and alien routes | Alien paranoia and detection decisions can cross-reference Kruger’s biological disguise |
| Mass Panic | Public fame and anomalies can trigger panic if Kruger’s work becomes visible |
| Gift from Scientists | Kruger can cause this event to give stronger or stranger tech to the host |
| Research Failure | Rival labs and sabotage can turn this event into a hostile reaction against the Kruger host |
| Research Investment | Kruger can overperform or hijack investment categories |
| Special Tech | Kruger projects can unlock special technologies earlier |
| Super Soldiers and Crazy Scientist | Biowarfare, cloning, and human enhancement projects can cross-pollinate with those event concepts |
| Chemical and Biological Warfare | Kruger’s dangerous biology projects can produce weapons, countermeasures, or contamination scandals |
| Nuclear and fallout systems | The final device should feed the existing fallout world-end logic after it pushes chaos past the terminal threshold |

## Design boundary

Kruger is a single exceptional actor, not a generic country science reform. Other countries may create rival institutes, theft attempts, and countermeasures, but they should not each get their own full Kruger system unless he defects or is transferred.
