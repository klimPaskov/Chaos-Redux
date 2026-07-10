# Independence Wave achievement implementation prompt

Implement the complete achievement set for Chaos Redux Event 6.

Read `AGENTS.md`, the Event 6 specification, `matrices/006_achievement_matrix.csv`, the achievement sections of the asset skill, and existing Chaos Redux achievement patterns.

Keep all titles and descriptions as direction until final localisation is written. Do not expose hidden mechanics in ordinary event, focus, or decision text.

## Achievement registry

### `chaosx_006_one_state_to_statehood`

Working label, not final localisation: From One State to Statehood

Eligible actor: any Event 6 country released with anchor package only

Unlock direction: reach Foundational legitimacy, Internationally Entrenched recognition, high capacity and survive ten years

Disqualifiers: voluntary reunion, subject status, console or scenario rule that grants free recognition

Difficulty: very hard

Visibility: visible

Why it is not trivial: requires survival, administration, diplomacy and military restraint

Icon direction: tiny founding seal becoming a complete state emblem

### `chaosx_006_no_master`

Working label, not final localisation: No Master Above Us

Eligible actor: any Event 6 country

Unlock direction: reach mature recognition and security with no patron above the dominance threshold

Disqualifiers: become a subject or take client route

Difficulty: hard

Visibility: visible

Why it is not trivial: rejects the easiest aid path while still requiring survival

Icon direction: severed puppet strings around a sovereign seal

### `chaosx_006_peace_with_host`

Working label, not final localisation: The Signed Border

Eligible actor: any Event 6 country with living former host

Unlock direction: complete recognized separation, property settlement, citizenship settlement and no war with host for five years

Disqualifiers: reconquest war or forced military settlement

Difficulty: hard

Visibility: visible

Why it is not trivial: requires diplomacy and concessions from both sides

Icon direction: two border stones joined by a treaty ribbon without text

### `chaosx_006_break_reconquest`

Working label, not final localisation: The Capital Held

Eligible actor: any Event 6 country attacked by former host

Unlock direction: win or force peace in a reconquest war while retaining the original capital and remaining independent

Disqualifiers: lose capital for the defined failure window or become a client

Difficulty: hard

Visibility: visible

Why it is not trivial: requires military survival without an easy subject shortcut

Icon direction: capital tower behind a broken encirclement ring

### `chaosx_006_found_league`

Working label, not final localisation: Congress of the Newly Free

Eligible actor: founding Event 6 country

Unlock direction: form the league with at least five members and adopt a complete charter

Disqualifiers: league begins through triggerable scenario pre-formation

Difficulty: hard

Visibility: visible

Why it is not trivial: requires several countries to survive and cooperate

Icon direction: multiple small seals around a charter table

### `chaosx_006_cross_regional_league`

Working label, not final localisation: A World of Small Flags

Eligible actor: league leader or member

Unlock direction: maintain ten members from at least four regional overlays with high cohesion for two years

Disqualifiers: radical forced membership or scenario setup that starts complete

Difficulty: very hard

Visibility: visible

Why it is not trivial: requires cross-regional diplomacy and crisis management

Icon direction: globe ringed by distinct small flag shapes without text

### `chaosx_006_rescue_member`

Working label, not final localisation: None Left to the Host

Eligible actor: any league member

Unlock direction: answer a rescue call and prevent annexation of a threatened member capital

Disqualifiers: target later voluntarily rejoins host within the check window

Difficulty: hard

Visibility: visible

Why it is not trivial: requires resource sacrifice and successful intervention

Icon direction: two shields covering a smaller city seal

### `chaosx_006_regional_formable`

Working label, not final localisation: The Second Founding

Eligible actor: any Event 6 country

Unlock direction: form a registered regional formable and complete all first-stage integration missions

Disqualifiers: military proclamation with unresolved required integration

Difficulty: hard

Visibility: visible

Why it is not trivial: formation alone is insufficient

Icon direction: two crowns or seals fused over a rail and river motif

### `chaosx_006_volga_bulgaria`

Working label, not final localisation: The River Remembers

Eligible actor: Volga Bulgaria with Event 6 origin

Unlock direction: complete the signature restoration or federal route, control the required Volga centers, and remain outside Soviet Collapse content

Disqualifiers: country has Event 5 origin or uses wrong origin package

Difficulty: very hard

Visibility: hidden

Why it is not trivial: tests origin separation and a signature route

Icon direction: river, old city silhouette and modern state seal

### `chaosx_006_assyria_survives`

Working label, not final localisation: Between the Rivers

Eligible actor: Assyria with Event 6 origin

Unlock direction: secure broad recognition, protect the anchor population, complete a Mesopotamian settlement route, and survive host conflict

Disqualifiers: forced client capture or loss of anchor

Difficulty: very hard

Visibility: hidden

Why it is not trivial: requires a sensitive signature package and diplomacy

Icon direction: mountain, river and sourced Assyrian symbol direction

### `chaosx_006_small_to_major`

Working label, not final localisation: The Small State Problem

Eligible actor: any country with one-state opening

Unlock direction: become a major, field a professional army, and lead a successful league goal

Disqualifiers: form a huge country before becoming a major through own institutions

Difficulty: very hard

Visibility: visible

Why it is not trivial: requires long-term development from minimal territory

Icon direction: small seal casting a large shadow over factories and ranks

### `chaosx_006_radical_bloc`

Working label, not final localisation: Open Sovereignty

Eligible actor: radical Event 6 country

Unlock direction: trigger the dangerous milestone through a revisionist league, then survive the containment response

Disqualifiers: scenario directly forces the super-event

Difficulty: extreme

Visibility: hidden

Why it is not trivial: requires high chaos, league control and dangerous wars

Icon direction: fractured border stones beneath an activated league emblem

### `chaosx_006_every_flag_survival`

Working label, not final localisation: Every Flag Still Flies

Eligible actor: player in SCN-008

Unlock direction: at a defined late date, keep a high percentage of released candidates alive and independent at Low intensity

Disqualifiers: Common Congress or stronger intensity, subject states count as failures

Difficulty: extreme

Visibility: hidden

Why it is not trivial: the scenario starts all states fragile and requires systemic protection

Icon direction: crowded field of tiny distinct flags around one clock

### `chaosx_006_balanced_patrons`

Working label, not final localisation: The Narrow Bridge

Eligible actor: any Event 6 country

Unlock direction: receive major aid from at least three patrons, never cross dependency threshold, and buy out all concessions

Disqualifiers: choose client route

Difficulty: very hard

Visibility: visible

Why it is not trivial: requires careful multi-patron management

Icon direction: three hands held apart by a balanced bridge

### `chaosx_006_league_arbitrator`

Working label, not final localisation: The Borders Stayed Quiet

Eligible actor: league leader

Unlock direction: resolve five member border disputes through arbitration with no member war during the term

Disqualifiers: military coercion or expulsion used to settle a case

Difficulty: hard

Visibility: visible

Why it is not trivial: rewards league governance rather than conquest

Icon direction: five boundary markers around a judge or council seal

### `chaosx_006_host_remnant`

Working label, not final localisation: The State That Remained

Eligible actor: former host reduced to protected remnant

Unlock direction: survive, negotiate settlements with all Event 6 breakaways, rebuild capacity and remain independent for ten years

Disqualifiers: reconquer a breakaway or become a subject

Difficulty: very hard

Visibility: visible

Why it is not trivial: gives the host a difficult non-revanchist campaign

Icon direction: single capital tower surrounded by signed borders

## Implementation requirements

- Use one root Chaos Redux achievement registry and group Event 6 achievements together.
- Add tracking flags or variables only when the final state cannot prove the route.
- Track Event 6 origin separately from Soviet Collapse origin.
- Track scenario type and intensity disqualifiers where listed.
- Track voluntary reunion, subject status, patron dominance, capital loss, league actions, arbitration, rescue, formable integration, and route history where required.
- Prevent automatic unlocks from simply firing the event or launching a scenario.
- Add complete localisation and icons.
- Create completed, grey, and not-eligible 64x64 asset variants under `gfx/achievements/` with filenames matching the final IDs.
- Update docs and the Event 6 completion report.

## Audit

Verify every achievement against normal waves, cluster firing, manual event firing, all four scenario intensities, voluntary reunion, formable tag changes, annexation, and origin collisions. Report any simplification or unimplemented tracker.
