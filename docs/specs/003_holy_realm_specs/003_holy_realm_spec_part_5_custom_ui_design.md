# 003 Holy Realm Spec part 5

Part of the legacy specification indexed in [003_holy_realm_spec.md](003_holy_realm_spec.md). Text below is verbatim from that file.

## Part 5: Holy Realm Custom UI Design

### 85. Purpose of the Custom UI

The Holy Realm path needs custom UI because its main tension is not only territory, factories, or war score. The player is managing a state mythology that changes over time. Ordinary events and national spirits can carry part of that, but they cannot make the player feel the slow pressure of spiritual legitimacy, compassion turning into coercion, the expansion of sacred responsibility, and the final doctrine forming in the background.

The UI should give the player a place where the Holy Realm feels like its own system.

The UI should do five things.

1. Show the current spiritual stage of the Realm.
2. Track the main pressures that shape future events.
3. Explain why certain event options, focuses, and decisions are available.
4. Make the Final Silence path feel visible before it becomes irreversible.
5. Connect major Holy Realm moments to the Chaos Redux event log, world threat system, and late-game crisis systems.

The UI should be atmospheric, but it must remain practical. The player should be able to open the panel and understand what is happening without reading a long doctrine essay each time.

The panel should answer simple questions:

1. How accepted is the Holy Realm inside its own society?
2. How far has compassion drifted toward force?
3. How much of the world does the Realm consider part of its duty?
4. How close is the Realm to the Final Silence doctrine?
5. Which stage is the state in right now?
6. What recent events pushed the state in this direction?
7. What can the player still do to change course?

The UI should not replace events. It should make the events feel connected.

### 86. UI Architecture

The Holy Realm should have two connected UI elements.

1. **The Holy Mandala Panel**
2. **The Final Silence Ledger**

The Holy Mandala Panel is the main interface for most of the path. It exists from the early Holy Realm stage through Buddha Mandate and Divine Sovereignty. It shows the state of the Realm, the doctrinal counters, the Arhat system, foreign reach, and recent event memory.

The Final Silence Ledger is a late-game crisis interface. It appears only when Final Silence Pressure is high enough or when the relevant warning events have started. It tracks target status, world destruction phases, interruption paths, protected Holy Realm territory, and global reaction status.

The two interfaces should feel visually related, but not identical.

The Holy Mandala Panel should feel like a sacred state bureau.

The Final Silence Ledger should feel like the same bureau after it stopped caring about persuasion.

### 87. Access Points

The player should be able to access the UI from several places.

Recommended access points:

1. A decision category button named **Open the Holy Mandala**.
2. A special top-level country mechanic button if the mod has a place for country-specific panels.
3. Event options after major Holy Realm events, such as **Review the Mandala** or **Open the Ledger**.
4. A warning icon when Final Silence Pressure reaches dangerous levels.
5. A world threat panel link during the Final Silence scenario.

The UI should not require the player to remember where one old decision is located. If the Holy Realm is a major path, the interface should be easy to find.

When the Holy Realm is controlled by AI, other major countries should not get full access to the Holy Mandala Panel. They may receive a simplified foreign intelligence view during warning events. That foreign view should show only risk level, known stage, observed doctrine, and estimated nuclear threat.

### 88. Main Visual Style

The visual style should be calm, thin, and controlled. It should not use loud cult imagery. It should feel official, old, and bureaucratic.

Core visual elements:

1. Dark parchment or faded lacquer background.
2. Thin gold or muted saffron linework.
3. A central mandala layout with geometric rings.
4. Small ink seals for locked, active, and corrupted states.
5. Subtle mountain silhouette at the bottom edge.
6. Thin red marks only for danger states.
7. Low contrast divine stage effects, not bright fantasy glow.
8. Small ledger stamps for state records.
9. Minimal smoke, ash, or static effects on late screens.

The Holy Mandala should feel like a state document that became sacred through repeated use. The Final Silence Ledger should feel like the same document after human language has been reduced to target categories.

Avoid these visuals:

1. Neon religious symbols.
2. Overly modern sci-fi computer panels.
3. Horror game blood effects.
4. Cartoon halos.
5. Generic apocalypse flames.
6. Large screaming faces.
7. Random skull decorations.

The UI should use fear through order.

### 89. Holy Mandala Panel Overview

The Holy Mandala Panel should be the main interface for the Holy Realm path.

Suggested title:

**The Holy Mandala**

Subtitle changes by stage:

1. Refuge stage: **Records of Refuge and Vow**
2. Bodhisattva stage: **The Seal of the Living Mandate**
3. Arhat Administration stage: **Registers of Attainment and Service**
4. Buddha Mandate stage: **The State beneath the Awakened Seal**
5. Divine Sovereignty stage: **Witness Ledger of the Sovereign Path**
6. Final Silence stage: **The World Awaiting Quiet**

The panel should have a central circular stage display and several surrounding information areas.

Main layout:

1. Central stage ring.
2. Four main counters around the ring.
3. Recent doctrine memory strip.
4. Active stage effects list.
5. Tabs for Arhats, Refuge, Diplomacy, Doctrine, and Warnings.
6. Event log button.
7. Final Silence warning button if unlocked.

The layout should communicate that all systems orbit the spiritual stage. The state is organized around the Mandate.

### 90. Central Stage Ring

The central stage ring is the heart of the Holy Mandala Panel. It should show the current state stage and the possible future stages.

Stages shown on the ring:

1. Refuge
2. Bodhisattva
3. Arhat Administration
4. Buddha Mandate
5. Divine Sovereignty
6. Final Silence

Each stage should have one icon.

Suggested icons:

1. Refuge: mountain gate with small lamp.
2. Bodhisattva: seated figure holding a sealed scroll.
3. Arhat Administration: calm face or mask beside a ledger.
4. Buddha Mandate: lamp circle or empty throne under a wheel.
5. Divine Sovereignty: throne without a body, surrounded by witness marks.
6. Final Silence: empty mandala with a black center.

The current stage should be highlighted with a soft ring. Completed stages should be stamped. Locked stages should be visible but dim. Dangerous future stages should show a thin red crack or warning mark once their conditions become possible.

Hovering over a stage should show:

1. Stage name.
2. How it was reached or how it can be reached.
3. Current active effects.
4. Main risks.
5. Recent events that pushed the state toward or away from that stage.

The player should not have to guess why Divine Sovereignty is unavailable or why Final Silence Pressure is rising. The stage ring should explain it clearly.

### 91. Stage Ring Progression States

The central ring should have visual states.

#### 91.1 Locked State

The stage is visible but unlit. The icon is gray or faded. The tooltip says what broad conditions are missing.

Example tooltip direction:

**The Buddha Mandate cannot be proclaimed while the Bodhisattva state lacks spiritual legitimacy and the Arhats have not taken office.**

#### 91.2 Available State

The stage is softly lit. A small seal appears beside it. The tooltip says which focus, event, or decision can move the Realm into this stage.

Example tooltip direction:

**The lamps are lit. The proclamation can begin when the player completes The Buddha Mandate focus or accepts the proclamation event.**

#### 91.3 Active State

The icon is bright but not loud. The central subtitle changes. The stage effects list updates.

Example tooltip direction:

**The Realm is governed under the Buddha Mandate. Ministers record decisions as transmissions of awakened authority. Foreign powers treat the state as a spiritual dictatorship.**

#### 91.4 Corrupted State

This appears when the stage is active with high Compassion Drift. It should use a thin red line through the seal, not heavy horror visuals.

Example tooltip direction:

**The Mandate is being interpreted through coercive compassion. Several future events will treat restraint as weakness unless the player lowers Compassion Drift.**

#### 91.5 Rejected State

This appears if the player takes the Renunciation and Mercy branch to block final doctrine. Divine Sovereignty and Final Silence can remain visible but crossed by a pale vow mark.

Example tooltip direction:

**The Realm has sworn against annihilation. Final Silence content is blocked unless a later crisis breaks the vow through a special event or setting.**

#### 91.6 Crisis State

This appears when Final Silence warning events have begun. The outer ring should slowly darken or accumulate ash marks.

Example tooltip direction:

**Final Silence Pressure is no longer theoretical. The Mandala Bureau has begun preparing ledgers of foreign states.**

### 92. Main Counter Design

The panel should track four main counters.

1. Spiritual Legitimacy
2. Compassion Drift
3. Mandala Reach
4. Final Silence Pressure

Each counter should appear as a small vertical or curved gauge around the central ring. The gauges should be readable at a glance and should also have detailed tooltips.

The counters should not all use the same emotional language. Each represents a different kind of pressure.

Spiritual Legitimacy should feel like acceptance.

Compassion Drift should feel like interpretation.

Mandala Reach should feel like scope.

Final Silence Pressure should feel like danger.

The UI should avoid implying that every higher value is always good. Spiritual Legitimacy is usually helpful. Mandala Reach is useful but risky. Compassion Drift can unlock power but changes the state. Final Silence Pressure is late-game danger.

### 93. Spiritual Legitimacy Gauge

Spiritual Legitimacy measures how much the population, army, monastic network, and administration accept the sacred state project.

Suggested visual:

A vertical lamp gauge. At low values the lamp is weak. At high values the lamp becomes steady. It should not become flashy.

Possible levels:

1. **Doubted**
2. **Accepted**
3. **Vowed**
4. **Unquestioned**
5. **Recorded as Truth**

Tooltip should show:

1. Current level.
2. Main sources of gain.
3. Main sources of loss.
4. Current effect on stability, schism risk, Arhat performance, and proclamation options.
5. Recent changes.

Example tooltip direction:

**Spiritual Legitimacy is Accepted. The Realm is trusted as a refuge, but the Bodhisattva is not yet beyond political challenge. Recent gains came from sheltered refugees and a successful defense of the high passes. Recent losses came from food pressure in border camps.**

Gameplay meaning:

Low Spiritual Legitimacy should increase the chance of schism, scandal, failed proclamation, and resistance to Arhat power.

High Spiritual Legitimacy should improve stability, reduce schism risk, strengthen Arhat assignments, and unlock major stage transitions.

It should not fully prevent foreign fear. A Holy Realm with high legitimacy can be more frightening to outsiders because it looks internally unified.

### 94. Compassion Drift Gauge

Compassion Drift measures how far the Realm has moved from sheltering people to forcing peace upon them.

Suggested visual:

A prayer bead line that gradually becomes a chain. At low values it looks like beads or knots. At high values metal links appear. At extreme values, one red legal stamp appears at the bottom.

Possible levels:

1. **Sheltering**
2. **Disciplining**
3. **Pacifying**
4. **Finalist**
5. **Mercy without Witnesses**

Tooltip should show:

1. Current level.
2. Recent choices that raised or lowered it.
3. Which event texts are affected.
4. Which focus branches are enabled.
5. How foreign states interpret the Realm.
6. Whether Renunciation choices are still possible.

Example tooltip direction:

**Compassion Drift is Pacifying. The Realm still speaks of relief, but its ministries increasingly treat foreign sovereignty as an obstacle to peace. Peacekeeping options may become occupation options. Final doctrine events are closer.**

Gameplay meaning:

Low Compassion Drift should support defensive, humanitarian, and diplomatic paths.

Medium Compassion Drift should support peacekeeping and supervised occupation.

High Compassion Drift should unlock coercive pacification, Divine Sovereignty, and Final Silence Pressure.

Extreme Compassion Drift should make reversal harder and may allow final doctrine loyalists to challenge attempts at restraint.

### 95. Mandala Reach Gauge

Mandala Reach measures how much of the world the Realm considers part of its responsibility.

Suggested visual:

A map-ring around the central mandala. At low values it shows only the home mountains. At higher values, roads extend outward. At extreme values, the roads become a full circle around the world.

Possible levels:

1. **The Passes**
2. **The Border Valleys**
3. **The War-Tired Nations**
4. **The Mandala of States**
5. **No Outside**

Tooltip should show:

1. Current level.
2. Regions currently affected by pilgrimage, mediation, propaganda, or intervention.
3. Whether faction, guarantee, or peacekeeping options are unlocked.
4. Whether global refusal events can occur.
5. How it interacts with Compassion Drift.

Example tooltip direction:

**Mandala Reach is The War-Tired Nations. The Realm now receives letters, refugees, and envoys from countries beyond the Himalayas. Foreign protests are more likely when the Bodhisattva speaks about peace.**

Gameplay meaning:

Low Mandala Reach keeps the Holy Realm local and defensive.

Medium Mandala Reach enables diplomacy, refugees, mediation, and volunteer-related content.

High Mandala Reach enables faction formation, peacekeeping, ultimatum logic, foreign ideological pressure, and world-stage reactions.

Extreme Mandala Reach makes the Final Silence doctrine more dangerous because the Realm has started to treat all countries as inside its moral jurisdiction.

### 96. Final Silence Pressure Gauge

Final Silence Pressure measures how close the Holy Realm is to treating world destruction as a path to peace.

This counter should be hidden or represented only as a vague warning before the Buddha Mandate. It should become visible after late warning events, the Buddha Mandate, Divine Sovereignty, or specific nuclear doctrine choices.

Suggested visual:

A sealed black ledger with a thin progress line. Each threshold adds a new page mark. At dangerous levels, ash gathers at the corner of the panel.

Possible levels:

1. **Unspoken**
2. **Filed as Theory**
3. **Under Review**
4. **Prepared**
5. **Armed**
6. **Irreversible**

Tooltip should show:

1. Current level.
2. Whether the pressure is hidden, visible, or active.
3. Main causes.
4. Whether the world-end scenario can trigger.
5. Missing prerequisites.
6. Available off-ramps.
7. Whether 1945 nuclear or 1947 thermonuclear logic applies.

Example tooltip direction:

**Final Silence Pressure is Prepared. The Mandala Bureau has joined nuclear planning to doctrine. The scenario cannot begin yet because the Realm is not the strongest industrial power and the year condition has not been met. Renunciation is still possible.**

The gauge should be honest. The player should know when the path is dangerous. Surprise world endings are bad design.

### 97. Counter Change Feedback

Whenever a major event, focus, or decision changes a counter, the player should receive clear feedback.

Good feedback:

1. Small floating text in the panel.
2. Counter pulse or seal stamp.
3. Event option tooltip showing the expected direction.
4. Recent changes list.
5. Event log entry for major threshold crossings.

Example event option tooltip direction:

**This will raise Compassion Drift and may unlock coercive interpretations of future peacekeeping events.**

Example recent changes list:

1. Sheltered refugees at the passes: Spiritual Legitimacy increased.
2. Registered every refugee by vow: Compassion Drift increased.
3. Foreign mediation accepted: Mandala Reach increased.
4. Nuclear doctrine reviewed: Final Silence Pressure increased.

The player should never need to dig through old event text to know why the Realm changed.

### 98. Holy Mandala Tabs

The Holy Mandala Panel should have several tabs. The exact number can depend on UI feasibility, but the design works best with five.

Recommended tabs:

1. **Mandate**
2. **Arhats**
3. **Refuge**
4. **Foreign Roads**
5. **Doctrine**
6. **Warnings**

If six tabs are too many, Refuge and Foreign Roads can be combined into **Pilgrimage**, and Warnings can appear only when relevant.

The tabs should avoid clutter. Each should have one clear purpose.

### 99. Mandate Tab

The Mandate tab is the default tab. It shows the central stage ring, four counters, current leader stage, and active state effects.

Displayed elements:

1. Current stage title.
2. Central stage ring.
3. Current leader title.
4. Active national spirit summary.
5. Four main counters.
6. Recent stage-related events.
7. Button to open the event log filtered to Holy Realm events.
8. Button to open the Final Silence Ledger if unlocked.

The Mandate tab should be the screen the player opens to understand the current state of the Holy Realm.

Possible current stage summaries:

Refuge:

**The Realm shelters those who reach the passes. Its authority is still political, but the language of the state has changed.**

Bodhisattva:

**The Bodhisattva carries the Seal as a burden. Ministries obey, but some still remember when orders had ordinary signatures.**

Arhat Administration:

**The Arhats now hold offices, commands, and records. Their discipline strengthens the state and narrows the space for dissent.**

Buddha Mandate:

**The ruler is no longer treated as a political leader alone. The government has become an instrument of awakened authority.**

Divine Sovereignty:

**The state no longer asks where power begins. It records only where obedience has not yet arrived.**

Final Silence:

**The Mandala Bureau has opened the last ledger. Foreign borders are now filing categories.**

These are UI text directions, not required final localization.

### 100. Arhats Tab

The Arhats tab should make the Arhat system feel like a living bureaucracy and elite cadre layer. It should not be only a list of bonuses.

Displayed elements:

1. Number of Arhat candidates.
2. Number of confirmed Arhats.
3. Arhat distribution by role.
4. Current Arhat doctrine.
5. Scandal or false attainment risk.
6. Assignment slots.
7. Recent Arhat events.

Possible Arhat roles:

1. Administrative Arhats
2. Military Arhats
3. Diplomatic Arhats
4. Scientific Arhats
5. Internal Silence Arhats

The UI does not need all roles if implementation would become too complex. The design goal is to show that Arhats are not only monks. They are the sacred elite of the state.

Possible assignment slots:

1. Assign Arhat Overseer to a core region.
2. Assign Arhat Custodian to an occupied region.
3. Assign Arhat Commander to an army category.
4. Assign Arhat Witness to the Mandala Bureau.
5. Assign Arhat Envoy to foreign pilgrimage work.

Each assignment should have a benefit and a risk.

Example:

Assigning an Arhat Custodian to occupied territory could improve compliance growth, but if Compassion Drift is high, it may also increase resistance events, foreign reports, or condemnation risk.

False attainment should be visible as a risk if the Arhat system grows too quickly or Spiritual Legitimacy is low.

Possible risk levels:

1. **Trusted**
2. **Whispered**
3. **Questioned**
4. **Accused**
5. **Broken Vows**

The Arhats tab should support replay value. A player can build sincere service cadres, cold bureaucratic overseers, military vow-keepers, or final doctrine witnesses.

### 101. Refuge Tab

The Refuge tab should track the humanitarian and population side of the Holy Realm.

Displayed elements:

1. Refugee flow level.
2. Border pass status.
3. Food and shelter strain.
4. Public trust impact.
5. Black market or infiltration risk.
6. Current refugee policy.
7. Recent refugee events.

Possible refugee policies:

1. Open Refuge
2. Registered Refuge
3. Vowed Refuge
4. Militarized Passes
5. Closed Passes

Each policy should shape later events.

Open Refuge:

1. More Spiritual Legitimacy.
2. Better foreign sympathy.
3. More population pressure.
4. Higher infiltration risk.

Registered Refuge:

1. Better security.
2. Better workforce conversion.
3. Moderate Compassion Drift.
4. Moderate foreign suspicion.

Vowed Refuge:

1. More disciplined manpower.
2. Stronger Arhat recruitment.
3. Higher Compassion Drift.
4. Risk of accusations that the Realm is converting refugees under pressure.

Militarized Passes:

1. Strong defense.
2. Lower infiltration.
3. Lower foreign sympathy.
4. Risk of border tragedy events.

Closed Passes:

1. Higher short-term stability.
2. Lower strain.
3. Lower Spiritual Legitimacy if nearby disasters are severe.
4. Later guilt events or burial markers on the border.

This tab should help the player understand that the Holy Realm’s moral authority has material costs.

### 102. Foreign Roads Tab

The Foreign Roads tab should track Mandala Reach, pilgrims, mediation, foreign suspicion, peacekeeping, and diplomatic pressure.

Displayed elements:

1. Current Mandala Reach level.
2. Active foreign pilgrimage networks.
3. Countries under mediation.
4. Countries suspicious of the Realm.
5. Peacekeeping commitments.
6. Holy Realm faction or protected sphere status.
7. Foreign protest and intelligence warning log.

This tab should show the difference between soft reach and coercive reach.

Soft reach examples:

1. Pilgrims arriving.
2. Letters to war-tired societies.
3. Exiles sheltered.
4. Mediation offers.
5. Relief corridors.

Coercive reach examples:

1. Ultimatums.
2. Pacification mandates.
3. Arhat observers in foreign governments.
4. Supervised peace administrations.
5. Forced disarmament demands.

The UI should make it clear when the Realm’s foreign activity is starting to scare other countries.

Possible foreign suspicion levels:

1. **Curious**
2. **Uneasy**
3. **Protesting**
4. **Containing**
5. **Preparing War**

This can be a general global status rather than a per-country list if UI space is limited.

### 103. Doctrine Tab

The Doctrine tab should show the player which interpretation of Holy Realm doctrine is active.

Displayed elements:

1. First Doctrine of Suffering interpretation.
2. Question of Compassionate Force interpretation.
3. Compassion of Non-Return interpretation.
4. Renunciation or final doctrine status.
5. Active doctrine effects.
6. Contradictions or schism risks.

The Doctrine tab is important because the Holy Realm path should remember player choices. This tab becomes the memory of those choices.

Possible doctrine records:

First Doctrine of Suffering:

1. Suffering must be relieved.
2. Suffering must be governed.
3. Suffering must be ended.

Question of Compassionate Force:

1. Guard only those who come to us.
2. Stand between armies.
3. End the war at its source.
4. All sovereign violence is one crime.

Compassion of Non-Return:

1. Non-return means restraint.
2. Non-return means responsibility.
3. Non-return means finality.

Renunciation status:

1. No vow taken.
2. Vow against annihilation active.
3. Vow contested by final doctrine loyalists.
4. Vow broken by catastrophe.
5. Final doctrine armed.

The Doctrine tab should not be too text-heavy. It can use short phrases with detailed tooltips.

Example tooltip direction:

**Non-return means finality. The Realm believes irreversible action can end cycles of revenge. This raises Final Silence Pressure and makes Divine Sovereignty events more likely.**

### 104. Warnings Tab

The Warnings tab should appear when a serious threshold has been crossed.

Possible warning categories:

1. Arhat scandal risk.
2. Compassion Schism risk.
3. Foreign containment risk.
4. Nuclear doctrine risk.
5. Final Silence Pressure risk.
6. World threat escalation.

The Warnings tab should prioritize clarity. It should not list every small modifier. It should tell the player which large risks are active.

Possible warning card format:

1. Title.
2. Short cause.
3. Current severity.
4. Likely consequence.
5. Available response.
6. Event log link if relevant.

Example warning card:

**The Compassion Schism**

**Cause:** Compassion Drift has reached Pacifying while several senior monks still support the refuge doctrine.

**Likely consequence:** A schism event can fire if the player proclaims the Buddha Mandate without resolving the dispute.

**Available response:** Lower Compassion Drift through relief choices, investigate Arhat abuses, or accept the schism risk.

Warnings should feel like state records, not pop-up alarms.

### 105. Final Silence Ledger Overview

The Final Silence Ledger is a late-game interface used when the Holy Realm approaches or begins the world-end scenario.

It should not be available from the start. It should appear in one of these conditions:

1. Final Silence Pressure reaches **Under Review**.
2. The player takes a late nuclear doctrine focus.
3. The player enters Divine Sovereignty.
4. The first Final Silence warning event fires.
5. The world-end scenario begins.

Suggested title before activation:

**The Closed Ledger**

Suggested title during warning phase:

**The Final Silence Ledger**

Suggested title during active scenario:

**The Ledger of Quiet States**

The Ledger should feel much colder than the Holy Mandala Panel. The Mandala Panel is still about doctrine and governance. The Ledger is about filing the world into stages of erasure.

### 106. Final Silence Ledger Layout

The Ledger should be organized as a large rectangular document panel rather than a circular mandala.

Main elements:

1. Header with scenario status.
2. Date condition indicator.
3. Chaos Meter condition indicator.
4. Industry condition indicator.
5. Nuclear or thermonuclear capability indicator.
6. Doctrine lock indicator.
7. World target status summary.
8. Wasteland progression summary.
9. Interruption and reversal options if still available.
10. Event log and world threat links.

During the warning phase, the Ledger should show missing prerequisites and off-ramps.

During the active scenario, it should show destruction phases and which parts of the world remain outside Holy Realm territory.

The Ledger should never encourage the player to click a simple victory button without understanding consequences. It should feel like an irreversible state apparatus.

### 107. Final Silence Prerequisite Indicators

The Ledger should show the main world-end conditions clearly.

Required indicators:

1. **Year Condition**
2. **Chaos Condition**
3. **Industrial Supremacy**
4. **Nuclear Readiness**
5. **Final Doctrine Armed**

Each indicator should have three states.

1. Missing
2. Near
3. Fulfilled

Year Condition:

Missing before 1945.

Fulfilled in 1945 or later.

Thermonuclear variant indicator active in 1947 or later if the required tech or scenario condition is present.

Chaos Condition:

Missing below the late threshold.

Near when Chaos Meter is approaching 1000.

Fulfilled when Chaos Meter is above 1000.

Industrial Supremacy:

Missing if the Holy Realm is not the strongest country by factories.

Near if it is in the top few industrial powers.

Fulfilled if it has the most factories in the world.

Nuclear Readiness:

Missing if the Realm cannot launch the final scenario.

Near if nuclear research or reactors are ready but delivery or stockpile logic is incomplete.

Fulfilled when the scenario can script continuous nuclear strikes.

Final Doctrine Armed:

Missing if the player has not taken the final doctrine path.

Near if Divine Sovereignty is active but the final focus or flag is missing.

Fulfilled if the world-end trigger flag is active.

This section must be very clear for player trust.

### 108. Final Silence Scenario Status

The Ledger should show the current scenario status.

Possible statuses:

1. **Unopened**
2. **Filed as Theory**
3. **Warning Phase**
4. **Launch Network Prepared**
5. **First Silence Ordered**
6. **Continuous Silence Active**
7. **Thermonuclear Silence Active**
8. **Interrupted**
9. **Completed**
10. **Vow Reasserted**

Each status should have a short state description.

Filed as Theory:

**The doctrine exists in memoranda. It has not yet become state policy.**

Warning Phase:

**Foreign intelligence reports, internal memoranda, and Mandala Bureau orders suggest that the Realm is preparing a final solution to war itself.**

Launch Network Prepared:

**Target ledgers, air routes, reactor schedules, and command seals have been linked. The scenario can begin if the final condition is fulfilled.**

First Silence Ordered:

**The first strikes have been authorized. Foreign governments still believe they are facing a war plan. The Realm no longer uses that term.**

Continuous Silence Active:

**The world outside the Realm is being struck in waves. States progress toward wasteland status unless the network is interrupted.**

Thermonuclear Silence Active:

**The 1947 variant is active. Strike waves are larger, wasteland progression is harsher, and global recovery is nearly impossible.**

Interrupted:

**The launch network has been broken or the doctrine has been halted. The damage remains.**

Completed:

**The world outside the Realm has been reduced to silence. There are no ordinary foreign governments left to answer.**

Vow Reasserted:

**The Realm has stepped back from annihilation. Final doctrine loyalists may still exist, but the state has publicly rejected the Ledger.**

### 109. World Target Status Summary

The Ledger should summarize target progress without listing every province one by one.

Suggested categories:

1. Marked
2. Struck
3. Burning
4. Wasteland
5. Silent
6. Protected
7. Interrupted

Protected should apply to Holy Realm core and controlled protected territory that the scenario excludes.

Interrupted should apply to areas where the launch network was broken before full destruction.

The UI should show counts by state or region rather than every province.

Possible summary text:

1. **Marked States:** target ledgers prepared, no strike yet.
2. **Struck States:** initial nuclear strike completed.
3. **Burning States:** repeated strike and fallout effects active.
4. **Wasteland States:** state has crossed destruction threshold.
5. **Silent States:** no further strategic value remains.
6. **Protected States:** excluded by Holy Realm control or scenario rule.
7. **Interrupted States:** spared full progression because the network was disrupted.

The player should see global destruction progressing as a system, not as hundreds of separate popups.

### 110. Wasteland Progression Display

The Ledger should show how destruction progresses.

Recommended progression:

1. **Marked**
2. **First Strike**
3. **Fire Season**
4. **Broken Administration**
5. **Wasteland**
6. **Silent**

Marked:

Target entered into the ledger.

First Strike:

Initial nuclear or thermonuclear strike applied.

Fire Season:

Repeated strikes, fallout, air cleanliness damage, civilian death spikes, and infrastructure collapse.

Broken Administration:

State government, logistics, and organized recovery fail.

Wasteland:

The state is functionally destroyed.

Silent:

The state no longer produces meaningful strategic resistance or recovery events.

The UI should show these as icons, not long text blocks. Tooltips can provide detail.

### 111. Map Overlay Design

The Holy Realm needs a map overlay during late warning and Final Silence phases.

The overlay should be optional. The player should be able to toggle it from the Ledger.

Overlay modes:

1. **Doctrine Reach**
2. **Target Ledger**
3. **Wasteland Progression**
4. **Protected Realm**
5. **Interruption Network**

Doctrine Reach:

Shows where Mandala Reach and foreign influence are active.

Target Ledger:

Shows states marked for future strikes once the Final Silence warning phase begins.

Wasteland Progression:

Shows Marked, Struck, Burning, Wasteland, and Silent states during active scenario.

Protected Realm:

Shows Holy Realm territory excluded from the strikes.

Interruption Network:

Shows airbases, command centers, reactors, or scripted nodes that enemies can target to stop the scenario if that mechanic is implemented.

Suggested overlay colors should be subdued. The final prompt for Photoshop can define exact palette later, but the direction should be muted saffron, ash gray, dim red, black ink, and pale gold.

The map overlay should not cover the whole map with bright colors. It should look like a strategic state ledger projected onto the map.

### 112. Map Marker Icons

The map overlay needs small marker icons.

Recommended marker set:

1. Marked state: small ledger corner or ink dot.
2. First Strike: broken circle.
3. Burning: thin red smoke mark.
4. Wasteland: cracked ground stamp.
5. Silent: blank seal.
6. Protected Realm: mountain gate seal.
7. Launch Node: sealed command mark.
8. Broken Launch Node: cracked command mark.
9. Retaliated Realm State: cracked mandala.
10. Refuge Corridor: small lamp road.

These icons should be simple because HOI4 map markers are small. The shape language matters more than detail.

### 113. Event Log Integration

The Holy Mandala Panel and Final Silence Ledger should connect to the Chaos Redux event log system.

The UI should have a small button named **Open Records** or **Open Event Log**.

The event log filter should show Holy Realm entries.

Important log entries:

1. The first opening of the refuge.
2. The Bodhisattva accepts the Seal.
3. The Arhats take office.
4. First Arhat scandal or false attainment event.
5. First foreign pilgrimage wave.
6. First peacekeeping intervention.
7. First coercive pacification.
8. Buddha Mandate proclamation.
9. Renunciation vow or refusal of final doctrine.
10. Divine Sovereignty.
11. Final Silence warning phase.
12. Final Silence activation.
13. Thermonuclear variant activation.
14. Interruption or completion.

The UI should show a small recent records strip even before opening the full log.

Possible recent record format:

1. Date.
2. Short title.
3. One-line consequence.
4. Counter changed.

Example:

**12 March 1944: A Village without Petitions**

**Arhat oversight improved compliance. Compassion Drift increased.**

This makes the Holy Realm feel like it remembers the campaign.

### 114. Super Event Integration

The UI should support Holy Realm super events without replacing them.

Likely super events:

1. The Buddha Mandate.
2. Divine Sovereignty if reached under high global crisis.
3. The Final Silence.
4. Thermonuclear Final Silence variant.
5. Possible Renunciation capstone if the player rejects annihilation after reaching the edge.

After a super event, the Holy Mandala Panel should update visibly.

For Buddha Mandate:

1. Stage ring advances.
2. Subtitle changes.
3. Buddha Mandate spirit appears.
4. Foreign Roads tab gains new reaction entries.

For Divine Sovereignty:

1. Stage ring darkens.
2. Final Silence Pressure becomes more visible.
3. Warnings tab opens automatically after the event.
4. Diplomacy entries become colder.

For Final Silence:

1. Ledger opens or becomes accessible.
2. Map overlay prompt appears.
3. World threat status updates.
4. Event log records activation.

For Renunciation:

1. Final Silence stages are sealed with vow marks.
2. Warnings tab shows extremist backlash risk.
3. Foreign Roads tab shows improved trust or cautious relief.

### 115. Foreign Intelligence View

Other countries should not see the Holy Mandala Panel in full. That would make no sense. However, if the Holy Realm becomes a world threat, foreign players and AI countries should receive limited information through events, decisions, or intelligence reports.

Suggested foreign view title:

**Foreign Report: The Holy Realm**

Displayed elements:

1. Known stage.
2. Estimated doctrinal risk.
3. Observed nuclear readiness.
4. Foreign suspicion level.
5. Recommended response options.
6. Known event log excerpts.

Possible risk categories:

1. Local spiritual government.
2. Regional peace movement.
3. Interventionist holy state.
4. Sacred dictatorship.
5. Nuclear doctrinal threat.
6. Final Silence imminent.

The foreign view should be less precise than the Holy Realm’s own panel. A country with better intelligence could receive more accurate reports.

This helps multiplayer and AI reaction design. Other players should not be blindsided by a world-ending path with no signal.

### 116. Settings Integration

The UI should respect Chaos Redux settings.

Potential setting interactions:

1. If world-end scenarios are disabled, Final Silence Ledger should show the doctrine as blocked by settings.
2. If super events are disabled, the UI should still update after the stage transition.
3. If custom UI is disabled or unavailable, critical information should still appear through decisions, events, and national spirits.
4. If multiplayer safety is enabled, the Ledger should show warning phase length and interruption rules more clearly.
5. If rare paths are disabled, the most extreme Divine Sovereignty and Final Silence branches should not appear or should remain sealed.

The player should not see broken UI states because a setting removed a system.

Example settings tooltip direction:

**World-end scenarios are disabled. The Final Silence doctrine can still affect internal politics, but the destruction scenario will not trigger.**

### 117. Multiplayer UI Behavior

In multiplayer, the Holy Realm UI should avoid unfair surprise and excessive interruption.

Recommended multiplayer rules:

1. Other players receive foreign intelligence warnings before Final Silence can activate.
2. The Ledger shows a visible warning phase timer if the scenario is active.
3. Interruption options are clear.
4. The active scenario uses grouped updates rather than frequent popups.
5. The Holy Realm player sees detailed doctrine counters, but foreign players see risk estimates.

The UI should make the path tense. It should not make the lobby feel cheated.

Possible foreign player alert:

**Foreign intelligence reports that the Holy Realm has opened a final target ledger. The doctrine is no longer theoretical.**

Possible Holy Realm player alert:

**The Ledger has been opened. The world can still force delay, but the doctrine now has a schedule.**

### 118. AI Use of the UI Systems

The AI does not need to see UI, but the same counters should guide AI behavior.

Holy Realm AI should use:

1. Spiritual Legitimacy to decide whether to centralize.
2. Compassion Drift to decide between refuge, peacekeeping, and pacification.
3. Mandala Reach to decide whether foreign actions are justified.
4. Final Silence Pressure to decide whether late nuclear doctrine is available.
5. World chaos and factory ranking to decide whether world-end behavior is allowed.

Foreign AI should use observed risk levels.

Foreign AI reactions:

1. Ignore a local refuge state.
2. Monitor a Bodhisattva state with rising foreign reach.
3. Protest peacekeeping influence.
4. Contain a coercive Holy Realm.
5. Strike launch nodes or form coalitions if Final Silence is imminent.
6. Prioritize survival and retaliation if Final Silence activates.

The UI design should expose enough system state that debugging AI behavior is easier later.

### 119. Tooltip Writing Style

Tooltips should be clear, sober, and specific.

Good tooltip qualities:

1. Explain the current state.
2. Explain why it changed.
3. Explain what it unlocks.
4. Explain risks.
5. Avoid vague moral text.

Bad tooltip qualities:

1. Pure flavor with no gameplay meaning.
2. Too many numbers without context.
3. Generic apocalypse wording.
4. Religious mockery.
5. Long lore paragraphs.

Example tooltip for Compassion Drift:

**Compassion Drift measures how far the Realm has moved from sheltering people to forcing peace upon them. High values unlock pacification and final doctrine events, but increase foreign fear and internal schism risk.**

Example tooltip for Mandala Reach:

**Mandala Reach measures how much of the world the Realm treats as its responsibility. High values unlock mediation, peacekeeping, and foreign pressure. Combined with high Compassion Drift, it can make the Realm see all sovereignty as a source of suffering.**

Example tooltip for Final Silence Pressure:

**Final Silence Pressure measures whether the Realm is turning nuclear doctrine into a plan to end war by ending the world outside itself. The scenario requires 1945 or later, Chaos above 1000, industrial supremacy, and final doctrine activation.**

### 120. Button Design

The UI should use restrained buttons with state seals, not bright gamey buttons.

Recommended buttons:

1. **Open Records**
2. **Review Doctrine**
3. **Assign Arhat**
4. **Change Refuge Policy**
5. **Send Envoy**
6. **Open Ledger**
7. **Show Map Overlay**
8. **Seal the Vow**
9. **Prepare Interruption**
10. **Close the Ledger**

Button states:

1. Available
2. Locked
3. Dangerous
4. Irreversible
5. Disabled by settings

Dangerous buttons should use a thin red corner mark. Irreversible buttons should require event confirmation rather than being clicked casually in the UI.

The UI should not let the player accidentally trigger Final Silence with one button.

### 121. Progression State Exports Needed Later

The future Photoshop-extension prompt should request exported variants for all major UI states. This spec should identify the needed states, but the actual prompt should remain outside the spec until the full Holy Realm specification is complete.

Holy Mandala Panel state exports:

1. Refuge stage default.
2. Bodhisattva stage default.
3. Arhat Administration stage default.
4. Buddha Mandate stage default.
5. Divine Sovereignty stage default.
6. Final Silence stage default.
7. Renunciation stage with vow marks.
8. Corrupted high-drift variant.
9. Warning phase variant.
10. Disabled-by-settings variant.

Final Silence Ledger state exports:

1. Closed Ledger.
2. Filed as Theory.
3. Warning Phase.
4. Launch Network Prepared.
5. First Silence Ordered.
6. Continuous Silence Active.
7. Thermonuclear Silence Active.
8. Interrupted.
9. Completed.
10. Vow Reasserted.

Map overlay marker exports:

1. Marked.
2. First Strike.
3. Burning.
4. Wasteland.
5. Silent.
6. Protected Realm.
7. Launch Node.
8. Broken Launch Node.
9. Retaliated Realm State.
10. Refuge Corridor.

These exports should be designed in a consistent style so they look like one system.

### 122. Required UI Asset List

Likely required assets:

1. Holy Mandala Panel background.
2. Holy Mandala Panel frame.
3. Central stage ring.
4. Six stage icons.
5. Four counter gauges.
6. Counter icon set.
7. Tab button set.
8. Event record strip.
9. Warning card frame.
10. Arhat assignment slot frame.
11. Refuge policy icon set.
12. Foreign Roads icon set.
13. Doctrine record stamp set.
14. Final Silence Ledger background.
15. Final Silence Ledger frame.
16. Scenario status indicator set.
17. Prerequisite indicator set.
18. Target status icons.
19. Map overlay markers.
20. Super-event compatible decorative frame elements.
21. Foreign intelligence report panel.
22. Disabled or setting-blocked overlay.

Optional assets:

1. Buddha Mandate portrait frame.
2. Divine Sovereignty portrait frame.
3. God-stage leader seal.
4. Arhat leader or advisor frame.
5. Mandala Bureau institutional seal.
6. Animated ash overlay if the UI supports it.
7. Static radio strip for foreign intelligence reports.

The design should work without optional assets, but optional assets would make the path feel much stronger.

### 123. Icon Style Guide

Holy Realm UI icons should follow a shared style.

Icon rules:

1. Thin linework.
2. Limited color range.
3. Clear silhouette at small size.
4. No heavy detail.
5. No modern digital glow.
6. No generic fantasy symbols.
7. No disrespectful religious caricature.
8. Use state, document, mountain, lamp, road, seal, ledger, and circle motifs.

Suggested motifs:

1. Mountain gate.
2. Oil lamp.
3. Sealed scroll.
4. Empty throne.
5. Ledger page.
6. Prayer bead chain.
7. Broken mandala.
8. Silent radio tower.
9. Refuge road.
10. Cracked state seal.

The icon set should make the Holy Realm feel official and dangerous through restraint.

### 124. UI Sound Direction

If the mod uses audio for UI or super events, the Holy Realm interface could use a small set of restrained sounds.

Suggested sounds:

1. Soft paper stamp when a record is added.
2. Low bell when a stage changes.
3. Dry ledger page turn when the Final Silence Ledger opens.
4. Distant radio static during foreign warning reports.
5. Low, short tone when Final Silence Pressure crosses a threshold.
6. Heavier low-frequency hit for thermonuclear variant.

Avoid:

1. Loud horror stingers.
2. Chant loops that become annoying.
3. Overly dramatic orchestral hits.
4. Comic villain sounds.

Sound should reinforce calm state terror, not spectacle.

### 125. Performance and Readability Considerations

The UI must not become too heavy.

Practical safeguards:

1. Use grouped region summaries instead of listing every state.
2. Use tooltips for detail rather than large text blocks.
3. Avoid frequent animated updates during continuous strikes.
4. Batch Final Silence notifications.
5. Keep map overlay icons simple.
6. Allow overlay toggles.
7. Keep foreign player warnings concise.
8. Do not require the custom UI for basic functionality.

The UI should support the scenario rather than slow it down.

If engine limitations prevent the full UI, the fallback should still preserve the design through decisions, event logs, state modifiers, and national spirits. However, the final coding-agent implementation should not choose a fallback unless the intended UI is genuinely impossible in the modding framework.

### 126. UI Failure and Degraded Mode

The design should define what happens if custom UI support is unavailable or disabled.

Degraded mode should include:

1. Decision category showing the four counters.
2. Event log entries for every major threshold.
3. National spirit tooltips describing the current stage.
4. Warning events for Final Silence thresholds.
5. Map markers or state modifiers if overlays are not possible.
6. Super-event updates for major stage transitions.

Degraded mode should still preserve player understanding. The player should still know why the path is moving toward or away from Final Silence.

However, the intended design remains the Holy Mandala Panel and Final Silence Ledger.

### 127. UI Replay Value

The UI should make repeated Holy Realm campaigns feel different.

Replay differences should appear through:

1. Different stage subtitle text.
2. Different doctrine records.
3. Different Arhat role distribution.
4. Different refugee policy history.
5. Different foreign suspicion levels.
6. Different Final Silence Pressure visibility.
7. Renunciation vow marks if the player rejects annihilation.
8. Corrupted seal marks if the player embraces coercion.
9. Different event records based on scandals, interventions, and crises.
10. Different Ledger state if the scenario is interrupted, completed, or never opened.

A player should be able to look at the UI and understand what kind of Holy Realm they built.

### 128. UI Connection to Earlier Parts

This UI design supports the earlier specification sections.

Connections to Part 1:

1. Shows the spiritual hierarchy from Refuge to Final Silence.
2. Tracks Spiritual Legitimacy, Compassion Drift, Mandala Reach, and Final Silence Pressure.
3. Makes the state’s moral descent visible.

Connections to Part 2:

1. Focus tree branches update counters and stage state.
2. Renunciation and Mercy branch can seal final stages.
3. Divine Sovereignty and Final Silence branches open the Ledger.
4. Focus choices can alter doctrine records.

Connections to Part 3:

1. Event choices update the panel.
2. Proclamation events change stage ring status.
3. Arhat scandals appear in the Arhats tab.
4. Refuge and diplomacy choices appear in their tabs.
5. Player choice memory appears in Doctrine records.

Connections to Part 4:

1. Final Silence warning chain appears in the Warnings tab.
2. World-end prerequisites appear in the Ledger.
3. Continuous nuclear progression appears through target status summaries.
4. Wasteland progression appears in the map overlay.
5. Interruption paths appear in the Ledger.

This keeps the Holy Realm system coherent from early events to world-end scenario.

### 129. UI Boundaries

The UI should not do everything.

It should not replace:

1. Focus tree descriptions.
2. Event text.
3. Super events.
4. Map gameplay.
5. Event logs.
6. AI decision logic.
7. Settings screens.

It should support them.

The Holy Mandala Panel is the player’s state memory. The Final Silence Ledger is the player’s crisis interface.

That is enough.

### 130. Part 5 Completion Note

Part 5 defines the Holy Realm custom UI design. It covers the Holy Mandala Panel, the Final Silence Ledger, player-facing counters, tabs, stage ring, Arhat assignments, refugee policy display, foreign reach display, doctrine memory, warnings, map overlays, event log integration, super-event integration, settings behavior, multiplayer behavior, foreign intelligence view, AI use, tooltip style, button states, asset requirements, and degraded mode.

Part 6 should continue with **Holy Realm AI Behavior, Balance Rules, and Campaign Integration**.

Part 6 should cover:

1. AI Holy Realm path selection.
2. AI restraint and escalation rules.
3. AI use of Bodhisattva, Buddha, Divine Sovereignty, and Final Silence stages.
4. Foreign AI containment and response behavior.
5. Balance guardrails for non-final paths.
6. Difficulty and player-facing pacing.
7. Multiplayer balance.
8. Interaction with Chaos Redux settings.
9. Conditions that prevent absurd or too-frequent outcomes.
10. How the Holy Realm should fit into the wider campaign without overwhelming every run.
