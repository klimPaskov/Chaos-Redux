# 003 Holy Realm Spec part 7

Part of the legacy specification indexed in [003_holy_realm_spec.md](003_holy_realm_spec.md). Text below is verbatim from that file.

## Part 7: Holy Realm Assets, Localization, Super Events, and Implementation Handoff Preparation

### 177. Purpose of the Final Holy Realm Asset Pass

The Holy Realm needs a clear asset and localization plan because the path depends on tone. If the visuals are too loud, it becomes a parody. If the text is too vague, the player will not understand why the state changes. If the super events are generic, the Buddha Mandate and Final Silence lose their identity.

This part defines the assets, names, localization patterns, event picture needs, focus icon needs, leader portrait needs, super-event treatment, sound direction, documentation needs, and final handoff notes for the coding agent.

The goal is to make the Holy Realm feel consistent across all player-facing surfaces:

1. Focus tree.
2. Country leaders.
3. National spirits.
4. Events.
5. Decisions.
6. Custom UI.
7. Event logs.
8. Super events.
9. World threat entries.
10. Foreign intelligence warnings.
11. Map overlays and state markers.

The Holy Realm should always feel calm, administrative, and severe. The style should come from ledgers, vows, sealed records, high passes, restrained religious symbols, muted gold, dark parchment, and controlled silence. Late content can become frightening, but it should become frightening through order rather than noise.

### 178. Asset Style Rules

All Holy Realm assets should follow the same visual discipline.

Use:

1. Dark parchment.
2. Muted saffron.
3. Faded gold.
4. Ink black.
5. Dull red only for warnings, corruption, or final doctrine.
6. Thin linework.
7. Stamped seals.
8. Mountain silhouettes.
9. Ledger grids.
10. Small lamps.
11. Empty thrones.
12. Mandala geometry.
13. Weathered paper.
14. Quiet rooms.
15. State documents.

Avoid:

1. Bright fantasy halos.
2. Neon religious symbols.
3. Random skulls.
4. Generic fire apocalypse art.
5. Exaggerated cult robes.
6. Cartoon mysticism.
7. Loud demonic visuals.
8. Modern sci-fi control screens.
9. Glowing magical weapons.
10. Shock imagery that does not serve the event.

The Holy Realm should look like a state that turned spiritual language into administration. Even the most extreme assets should feel official.

### 179. Required Event Pictures

The Holy Realm should have a dedicated event picture set. Reusing generic mountain, riot, or nuclear images will make the path feel cheaper. The event pictures do not all need to be fully unique at first, but the most important moments should have distinct art.

#### 179.1 Formation and Refuge Pictures

Required pictures:

1. **High Monastery Gathering**
   - A monastery courtyard in cold mountain light.
   - Pilgrims, soldiers, monks, and officials stand apart from each other.
   - No crowd celebration.
   - Used for The Figure at the High Monastery and The Door in the Mountain Opens.

2. **Roads Climb Toward Silence**
   - Refugees moving through a mountain pass.
   - Small lamps or flags along the road.
   - Soldiers watch without dramatic posture.
   - Used for refugee route events.

3. **The Seal of Refuge**
   - A state seal pressed onto dark parchment.
   - Mountain line at the bottom.
   - Used for the first formal transformation.

4. **Border Camps at Dusk**
   - Tents, prayer flags, supply crates, and registration tables.
   - Used for refugee policy and border pressure events.

5. **Shelters under Stone**
   - Civilians inside carved mountain shelters.
   - Quiet, cramped, and controlled.
   - Used for bombing resilience and civil protection events.

#### 179.2 Bodhisattva and Arhat Pictures

Required pictures:

1. **The Bodhisattva Accepts the Seal**
   - A seated figure partly obscured by officials and lamps.
   - The leader should be present but not theatrical.
   - Used for the Bodhisattva recognition event.

2. **Ministries Bow in Silence**
   - A government chamber with empty chairs and bowed officials.
   - Used for centralization events.

3. **Arhat Examinations**
   - Candidates sitting under supervision with ledgers and lamps.
   - Military and civilian candidates can appear together.
   - Used for Arhat system unlock.

4. **The Silent Offices**
   - Clerks in a dark government office.
   - Ledgers, stamps, straight stacks of papers.
   - Used for bureaucracy events.

5. **A Village without Petitions**
   - A quiet village square with a closed petition box.
   - No visible violence.
   - Used for public trust and control events.

6. **The False Arhat**
   - A sealed dossier and removed nameplate.
   - Used for scandal events.

#### 179.3 Buddha Mandate and Divine Sovereignty Pictures

Required pictures:

1. **The Lamps Remain Lit**
   - A government building or monastery glowing at night.
   - Used for pre-proclamation warning.

2. **The Buddha Mandate**
   - Empty throne or seated leader behind a wheel and lamps.
   - This should support super-event use if needed.
   - Used for proclamation event.

3. **The Last Human Signature**
   - A document with a blank signature line and official witness marks.
   - Used for administrative transformation.

4. **A Sermon without Translation**
   - Foreign diplomats listening to a figure or empty screen.
   - Several translation papers disagree.
   - Used for foreign reaction event.

5. **The Throne without a Body**
   - A throne, seal, or symbolic empty seat.
   - No visible ruler.
   - Used for Divine Sovereignty.

6. **No One Leaves the Mandala**
   - Closed border gate, sealed passes, foreign passports held on a desk.
   - Used for lockdown events.

#### 179.4 Final Silence Pictures

Required pictures:

1. **The Ledgers Are Sealed**
   - Large ledgers closed with red thread or wax.
   - Used for first final warning.

2. **The Sky Is Entered into the Register**
   - Weather charts, flight lines, target maps, and seals.
   - Used for target doctrine.

3. **The Last Debate Is Cancelled**
   - Empty assembly chamber.
   - Lamps still burning.
   - Used for final lock-in.

4. **The World Is Marked as a Wound**
   - Pale world map with thin red target marks.
   - Used for final pre-launch event.

5. **The Final Silence Command Room**
   - Quiet bunker, no shouting, one lamp, target ledger open.
   - Used for launch event.

6. **Ash over the High Passes**
   - Ash or snow falling over mountains.
   - Used for internal Holy Realm reaction during launch.

7. **Empty Radio Room**
   - Radio equipment, static, abandoned headset.
   - Used for foreign response and collapse events.

8. **Wasteland Ledger**
   - State names crossed into silence.
   - Used for late scenario phase.

### 180. Focus Icon Requirements

The focus tree needs a dedicated icon language. The player should recognize Holy Realm focuses before reading the text.

#### 180.1 Central Trunk Icons

Required icons:

1. **The Figure at the High Monastery**
   - Mountain monastery silhouette with one lamp.

2. **Convene the Mountain Assembly**
   - Circle of small seals around a central scroll.

3. **The Seal of Refuge**
   - Wax seal with mountain line.

4. **Shelter the Border Villages**
   - Gate and small group of travelers.

5. **The Bodhisattva Accepts the Seal**
   - Seated figure with scroll.

6. **The First Doctrine of Suffering**
   - Open doctrine page with wheel motif.

#### 180.2 Monastic State Icons

Required icons:

1. **Rewrite the Civil Register**
   - Ledger and ink brush.

2. **The Ministry of Vows**
   - Bound scroll with small knot.

3. **Arhat Examinations**
   - Calm face beside checklist.

4. **The Silent Offices**
   - Government building with closed windows.

5. **A Village without Petitions**
   - Petition box with sealed slot.

6. **The Arhats Take Office**
   - Mask or calm face over a state seal.

7. **The Question of False Attainment**
   - Cracked seal over a name record.

#### 180.3 Mandala Economy Icons

Required icons:

1. **Count the Mountain Roads**
   - Road line through mountain pass.

2. **Monastic Labor Vows**
   - Hammer and prayer bead.

3. **Refuge Foundries**
   - Factory chimney behind camp tents.

4. **Reliquary Workshops**
   - Rifle and reliquary box.

5. **The Mandala Bureau**
   - Geometric mandala over file folders.

6. **Laboratories beneath the Snow Line**
   - Underground laboratory door under snow.

7. **Reactors as Prayer Wheels**
   - Reactor core with prayer wheel geometry.

8. **The Engine of Final Peace**
   - Bomber silhouette or rocket line over a mandala grid.

#### 180.4 Mountain Shield Icons

Required icons:

1. **Guard the High Passes**
   - Mountain gate and rifle.

2. **The Vow-Keeper Regiments**
   - Infantry helmet with vow knot.

3. **Shelters under Stone**
   - Bunker carved into mountain.

4. **The Quiet Mobilization**
   - Notice paper pinned before dawn.

5. **Mountain Artillery Mandalas**
   - Artillery arc drawn as mandala segment.

6. **The Road Must Remain Open**
   - Bridge and supply crate.

7. **No Fear beyond the Pass**
   - Open gate and forward road.

#### 180.5 Diplomacy and Intervention Icons

Required icons:

1. **Permit Foreign Pilgrimage**
   - Passport, lamp, and mountain route.

2. **The Court of Quiet Envoys**
   - Three diplomatic seals around a table.

3. **Letters to the War-Tired**
   - Letter with soldier and civilian marks.

4. **Shelter the Exiles**
   - Open door with foreign documents.

5. **The Mandala of Nations**
   - Several small flags around a wheel.

6. **The Refusal of Empires**
   - Broken diplomatic seal.

7. **The Question of Compassionate Force**
   - White flag and rifle held apart.

8. **White Flags on Foreign Roads**
   - White banner on road marker.

9. **The Pacification Mandate**
   - Sealed occupation order.

10. **No Victory Parades**
   - Empty avenue with military shadow.

11. **Release through Administration**
   - Puppet strings cut beside a state seal.

12. **The Last Border Is a Wound**
   - Map border line drawn as red scar.

#### 180.6 Buddha, Mercy, and Final Silence Icons

Required icons:

1. **The Lamps Remain Lit**
   - Row of lamps at night.

2. **The Buddha Mandate**
   - Empty throne under wheel.

3. **The Last Human Signature**
   - Blank signature line.

4. **A Sermon without Translation**
   - Three conflicting translation pages.

5. **The Compassion of Non-Return**
   - Closed circle with single opening.

6. **The Ministry of Silence**
   - Key, ledger, and seal.

7. **Refuse the Final Debate**
   - Closed debate chamber.

8. **The Vow against Annihilation**
   - Pale vow mark across a black center.

9. **Peace without Ownership**
   - Open hands above map.

10. **The World Still Burns**
   - Distant fire beyond mountain wall.

11. **The Second Refuge**
   - Larger gate with many lamps.

12. **The Throne without a Body**
   - Empty throne with witness marks.

13. **The Doctrine of the Last War**
   - Black doctrine book.

14. **All Roads End in Silence**
   - Road network ending at dark mandala.

15. **No One Leaves the Mandala**
   - Closed border gate.

16. **The Peace That Requires No Witnesses**
   - Empty witness box.

17. **The Final Silence**
   - Empty mandala with black center.

### 181. Decision and Category Icons

The Holy Realm decision interface needs small icons for recurring actions. These can be simpler than focus icons.

Required decision category icons:

1. **Holy Mandala**
   - Main mandala seal.

2. **Arhat Assignments**
   - Calm face and ledger.

3. **Refuge Policy**
   - Mountain gate and traveler.

4. **Foreign Pilgrimage**
   - Road and passport.

5. **Compassionate Force**
   - White flag and rifle.

6. **Final Silence Warnings**
   - Sealed black ledger.

7. **Renunciation and Mercy**
   - Pale vow mark over dark circle.

8. **World-End Response**
   - Broken target seal.

Required decision icons:

1. Assign Arhat to Province.
2. Assign Arhat to Army.
3. Assign Arhat to Bureau.
4. Admit Refugees.
5. Register Refugees.
6. Close the Passes.
7. Send Peace Envoys.
8. Issue Pacification Warning.
9. Mediate Border War.
10. Release Supervised Administration.
11. Investigate Arhat Scandal.
12. Reopen the Ledgers.
13. Seal Final Doctrine.
14. Swear against Annihilation.
15. Arm Final Silence.
16. Disrupt Final Silence Network.
17. Restore the Debate Chamber.
18. Record World Threat.

### 182. Leader Portrait Requirements

The Holy Realm leader progression needs portrait support because the path is about visible state transformation.

#### 182.1 Bodhisattva Portrait

Visual direction:

1. Human, restrained, and serious.
2. Simple robes or state garments.
3. No glowing halo.
4. Mountain or office background.
5. Face should look calm but politically aware.
6. Suitable for a leader who still signs policy through a state.

Needed variants:

1. Normal Bodhisattva.
2. Wartime Bodhisattva with darker background.
3. Wounded or post-catastrophe Bodhisattva if the route formed after a disaster.

Possible leader trait names:

1. The Burdened Bodhisattva.
2. Keeper of the High Refuge.
3. The Living Seal.
4. Guardian of the Vow Roads.

#### 182.2 Buddha Mandate Portrait

Visual direction:

1. Less ordinary human framing.
2. More formal symmetry.
3. Lamps, wheel, or empty throne motifs.
4. Face can be more distant.
5. Still not cartoon divine.

Needed variants:

1. Buddha Mandate calm variant.
2. Coercive Mandate corrupted seal variant.
3. Renunciation variant with pale vow mark.
4. Foreign intelligence silhouette variant for other countries.

Possible leader trait names:

1. The Buddha Mandate.
2. The Awakened Seal.
3. The State beneath the Mandate.
4. The Sermon without Translation.

#### 182.3 Divine Sovereignty Portrait

Visual direction:

1. The leader may be replaced by an icon, empty throne, or sealed state image.
2. Human presence should feel reduced.
3. Witness marks and dark mandala geometry should dominate.
4. Use dull red only as a thin line or stamp.
5. This should look like the state has made the ruler legally inhuman.

Needed variants:

1. Divine Sovereignty portrait.
2. God-stage seal portrait.
3. Final Silence active portrait.
4. Interrupted or cracked sovereignty portrait if the launch network is damaged.

Possible leader trait names:

1. Divine Sovereignty.
2. The Throne without a Body.
3. God of the Final Mandala.
4. Witness of Non-Return.
5. The Peace That Requires No Witnesses.

The God-stage title should be used carefully. It should be framed as state corruption, not as normal Buddhist doctrine.

### 183. Advisor, Commander, and Character Asset Needs

The Holy Realm should have a small cast of reusable character archetypes. These do not all need unique portraits at first, but named advisors improve immersion.

Suggested advisor archetypes:

1. **Quietist Elder**
   - Supports restraint, refuge, and anti-annihilation choices.
   - Bonuses to stability, legitimacy, and refugee handling.
   - Opposes Final Silence.

2. **Mandala Bureau Director**
   - Supports administration, research, intelligence, and special projects.
   - Bonuses to political power, research, and counterintelligence.
   - Can drift toward final doctrine if unchecked.

3. **Arhat Examiner**
   - Supports Arhat assignments and internal discipline.
   - Bonuses to compliance and stability.
   - Raises scandal risk if legitimacy is weak.

4. **Vow-Keeper Marshal**
   - Supports defense, mountain warfare, and mobilization.
   - Bonuses to entrenchment, organization, and mobilization.
   - Can push Military Capture route after trauma.

5. **Refuge Steward**
   - Supports refugee policy, civilian resilience, and humanitarian credibility.
   - Bonuses to population integration and public trust.
   - Opposes harsh registration.

6. **Final Silence Theorist**
   - Supports nuclear doctrine, Divine Sovereignty, and final stage.
   - Bonuses to special projects and war support.
   - Raises Final Silence Pressure and foreign fear.

7. **Foreign Pilgrimage Liaison**
   - Supports diplomacy, soft influence, and Mandala Reach.
   - Bonuses to opinion and foreign decision access.
   - Can trigger spy and infiltration events.

Suggested commander archetypes:

1. Vow-Keeper mountain general.
2. Arhat discipline commander.
3. Peace road marshal.
4. Wounded refuge defender.
5. Silent artillery planner.
6. Final doctrine air command officer.

Commanders should not all be fanatics. Some should be sincere defenders, some bureaucratic soldiers, and some dangerous final-doctrine loyalists.

### 184. Super Event Requirements

The Holy Realm needs several possible super events. Not every playthrough should see all of them.

#### 184.1 The Buddha Mandate

Trigger:

1. The Bodhisattva stage reaches proclamation conditions.
2. Spiritual Legitimacy is high enough.
3. Arhat Administration or equivalent state centralization exists.
4. Chaos is high enough to make the proclamation globally meaningful.

Visual direction:

1. Dark interior.
2. Lamps burning at noon or night.
3. Empty throne or seated figure.
4. Soft gold ring around a state seal.
5. Foreign radio reports shown through text, not visual clutter.

Suggested title:

**The Buddha Mandate**

Suggested subtitle variants:

1. **The government became a witness.**
2. **The lamps remained lit.**
3. **The seal no longer required a hand.**

Tone:

This super event should feel like a constitutional rupture. It should not feel like a coronation party.

#### 184.2 The Vow against Annihilation

Trigger:

1. Buddha Mandate is active.
2. Final Silence Pressure is rising.
3. The player takes the Renunciation and Mercy route.
4. Final doctrine is publicly rejected.

Visual direction:

1. Pale vow mark across a black mandala center.
2. Officials in a debate chamber.
3. A closed target ledger in the background.
4. No bright hopeful imagery.

Suggested title:

**The Vow against Annihilation**

Suggested subtitle variants:

1. **Peace would require witnesses.**
2. **The last debate was allowed to continue.**
3. **The world remained guilty and alive.**

Tone:

This should not feel like a simple good ending. It is a hard restraint decision in a world that still burns.

#### 184.3 Divine Sovereignty

Trigger:

1. Buddha Mandate is active.
2. Compassion Drift and Final Silence Pressure are high.
3. The player or AI accepts the Throne without a Body or equivalent focus.
4. The state crosses into final-stage authority.

Visual direction:

1. Empty throne.
2. Witness marks.
3. Dark mandala ring.
4. Thin red crack through state seal.
5. Human figure absent or barely visible.

Suggested title:

**Divine Sovereignty**

Suggested subtitle variants:

1. **The ruler was no longer a person in the records.**
2. **The state signed as witness.**
3. **The last human office closed.**

Tone:

This should feel like a legal and metaphysical collapse of normal government.

#### 184.4 The Final Silence

Trigger:

1. Final Silence scenario begins.
2. Year is 1945 or later.
3. Chaos is above 1000.
4. Holy Realm is strongest by factories.
5. Final doctrine is armed.
6. World-end settings allow it.

Visual direction:

1. Dark mandala over pale world map.
2. Thin target lines.
3. White mountain sun or high pass glow.
4. Static and empty map grid.
5. No triumphant crowds.
6. No normal nuclear explosion image at the start.

Suggested title:

**The Final Silence**

Suggested subtitle variants:

1. **The world was entered into the register.**
2. **Peace was declared against history.**
3. **No witness was required.**
4. **The last petition was received.**

Tone:

This should be quiet and final.

#### 184.5 Thermonuclear Variant

Trigger:

1. Final Silence begins in 1947 or later.
2. Thermonuclear technology, project, or variant is active.
3. Settings allow the stronger variant.

Visual direction:

1. Same composition as Final Silence.
2. Harsher pale light.
3. More static.
4. Target lines thicker or more numerous.
5. Ledger pages partly burned.
6. Still no conventional victory imagery.

Suggested title:

**The Final Silence: Thermonuclear Mandate**

Suggested subtitle variants:

1. **The second sun was recorded as mercy.**
2. **The sky closed all roads at once.**
3. **The world ended in a higher register.**

This variant should feel worse, not louder.

#### 184.6 The Mandala Breaks

Trigger:

1. Final Silence is interrupted.
2. The Holy Realm loses launch network control.
3. The Realm suffers internal schism, foreign strike, leader loss, or successful sabotage.

Visual direction:

1. Cracked mandala.
2. Broken seal.
3. Radio room with static.
4. Half-burned target ledger.
5. Mountain line still visible.

Suggested title:

**The Mandala Breaks**

Suggested subtitle variants:

1. **The last road did not close.**
2. **The witness returned to the chamber.**
3. **The ledger failed before the world did.**

Tone:

This is not a happy ending. It is a prevented end.

### 185. Event Title Bank

The coding agent should use a consistent title bank. These titles can be used directly, adapted, or assigned to event chains.

Formation and refuge titles:

1. The Figure at the High Monastery.
2. The Door in the Mountain Opens.
3. Roads of Pilgrimage.
4. The Seal of Refuge.
5. The Roads Climb Toward Silence.
6. Refugees at the Mountain Passes.
7. Border Camps at Dusk.
8. The First Winter of Vows.
9. The Monasteries Refuse the Census.
10. Ash Settles on the Prayer Flags.

Bodhisattva and state titles:

1. The Bodhisattva Accepts the Seal.
2. The Ministries Bow in Silence.
3. The First Doctrine of Suffering.
4. The Question of Compassionate Force.
5. Foreign Reporters at the Outer Courtyard.
6. The Living Seal.
7. The Burden Is Accepted.
8. The Assembly Waits for No Speech.

Arhat titles:

1. The First Arhat Candidates.
2. Arhat Examinations.
3. The Silent Offices.
4. The Arhats Take Office.
5. A Village without Petitions.
6. The Question of False Attainment.
7. Empty Chairs in the Revenue Bureau.
8. The Vow-Keeper Who Would Not Sleep.
9. The Second Silence in the Assembly.
10. The Ledger of Attainment.

Diplomacy and intervention titles:

1. Permit Foreign Pilgrimage.
2. Letters to the War-Tired.
3. The Court of Quiet Envoys.
4. Shelter the Exiles.
5. The Mandala of Nations.
6. The Refusal of Empires.
7. White Flags on Foreign Roads.
8. The Pacification Mandate.
9. No Victory Parades.
10. Release through Administration.
11. The Last Border Is a Wound.
12. The First Road beyond the Pass.

Buddha and doctrine titles:

1. The Lamps Remain Lit.
2. The Buddha Mandate.
3. The Last Human Signature.
4. A Sermon without Translation.
5. The Compassion of Non-Return.
6. The Ministry of Silence.
7. The Throne without a Body.
8. Divine Sovereignty.
9. The Doctrine of the Last War.
10. No One Leaves the Mandala.
11. The Peace That Requires No Witnesses.

Final Silence titles:

1. The Ledgers Are Sealed.
2. No More Peace Delegations.
3. The Sky Is Entered into the Register.
4. The Last Debate Is Cancelled.
5. The World Is Marked as a Wound.
6. The Final Silence.
7. The Last Condemnation Is Filed.
8. The Wasteland Is Recorded.
9. The Empty Mandala.
10. The Mandala Breaks.

Renunciation and mercy titles:

1. Refuse the Final Debate.
2. The Vow against Annihilation.
3. Peace without Ownership.
4. The World Still Burns.
5. The Second Refuge.
6. The Witness Must Remain.
7. The Target Ledger Is Closed.
8. The Quietists Return to the Chamber.

### 186. National Spirit Name Bank

The Holy Realm should use national spirits that can upgrade rather than clutter the country with unrelated modifiers.

Core spirits:

1. The Seal of Refuge.
2. The Bodhisattva State.
3. The Living Mandate.
4. The Arhat Administration.
5. The Buddha Mandate.
6. Divine Sovereignty.
7. The Final Silence Doctrine.

Administrative spirits:

1. Monastic Labor Vows.
2. The Ministry of Vows.
3. The Silent Offices.
4. The Civil Register.
5. The Mandala Bureau.
6. The Ministry of Silence.
7. The Ledger State.
8. Recorded as Truth.

Refuge and society spirits:

1. Roads of Refuge.
2. Border Camps at Dusk.
3. The Second Refuge.
4. Open Passes.
5. Registered Refugees.
6. Closed Passes.
7. Public Trust in the Mandate.
8. Food Pressure in the Camps.
9. Exiles under the Seal.
10. The World Still Burns.

Military spirits:

1. Vow-Keeper Regiments.
2. Guard the High Passes.
3. Shelters under Stone.
4. Quiet Mobilization.
5. Mountain Artillery Mandalas.
6. The Road Must Remain Open.
7. No Fear beyond the Pass.
8. Peace Columns.
9. Silent Airfields.
10. The Last War Doctrine.

Diplomatic and intervention spirits:

1. Foreign Pilgrimage.
2. The Court of Quiet Envoys.
3. Letters to the War-Tired.
4. The Mandala of Nations.
5. White Flags on Foreign Roads.
6. The Pacification Mandate.
7. Supervised Peace Administrations.
8. The Refusal of Empires.
9. Foreign Suspicion of the Mandate.
10. Containment of the Holy Realm.

Final doctrine spirits:

1. The Ledgers Are Sealed.
2. No More Peace Delegations.
3. The Sky Register.
4. The Last Debate Is Cancelled.
5. The World as a Wound.
6. The Peace That Requires No Witnesses.
7. Final Silence Armed.
8. Wasteland Ledger.
9. The Empty Mandala.
10. Cracked Divine Sovereignty.

Renunciation spirits:

1. The Vow against Annihilation.
2. The Debate Remains Open.
3. Peace Requires Witnesses.
4. The Closed Target Ledger.
5. Quietist Influence Restored.
6. The Second Refuge.

### 187. Decision Category and Decision Name Bank

Decision category names:

1. The Holy Mandala.
2. Records of Refuge and Vow.
3. Arhat Assignments.
4. The Ministry of Vows.
5. Pilgrims beyond the Passes.
6. The Mandala of Nations.
7. Compassionate Force.
8. The Ministry of Silence.
9. Renunciation and Mercy.
10. Final Silence Ledger.
11. World-End Response.
12. Foreign Intelligence on the Holy Realm.

Decision names for internal play:

1. Review the Holy Mandala.
2. Assign an Arhat Overseer.
3. Recall an Arhat Overseer.
4. Investigate False Attainment.
5. Expand the Civil Register.
6. Open the Refuge Roads.
7. Register the Refuge Roads.
8. Close the Refuge Roads.
9. Shelter the Exiles.
10. Send the Quiet Envoys.
11. Issue Letters to the War-Tired.
12. Offer Mediation to a War-Torn State.
13. Stand between Armies.
14. Demand a Pacification Settlement.
15. Release a Supervised Administration.
16. Restore Local Witness Councils.
17. Convene the Quietists.
18. Reopen the Ledgers.
19. Swear the Vow against Annihilation.
20. Seal the Final Debate.
21. Arm the Final Silence.
22. Mark the First Wound.
23. Record the Wasteland.
24. Repair the Broken Mandala.
25. Preserve the Witness Records.

Decision names for foreign countries:

1. Investigate the Holy Mandala.
2. Smuggle Reports from the Passes.
3. Expose Arhat Abuses.
4. Support Quietist Opposition.
5. Sanction the Mandala Bureau.
6. Strike the Launch Network.
7. Bomb the Reactors.
8. Form an Emergency Containment Pact.
9. Offer Final Negotiations.
10. Prepare Retaliation.
11. Evacuate Marked Cities.
12. Denounce the Final Doctrine.
13. Support a Mandala Break.
14. Demand Nuclear Disarmament.
15. Monitor the Sky Register.

### 188. Localization Tone Rules

Holy Realm localization should be restrained, precise, and bureaucratic. The writing should avoid random mystical speech. The state uses religious vocabulary, but it speaks like a government that has filed its metaphysics.

General rules:

1. Use short sentences for event openings.
2. Let unease come from calm procedure.
3. Avoid shouting.
4. Avoid comic cult language.
5. Avoid vague doom words when a specific state action works better.
6. Use official language for extreme acts.
7. Use witness, seal, register, vow, release, burden, road, silence, and ledger consistently.
8. Keep foreign reactions more practical and fearful.
9. Keep internal Holy Realm reactions quieter and more certain.
10. Make player options morally clear without sounding modern or casual.

Good verbs:

1. record.
2. seal.
3. witness.
4. release.
5. vow.
6. register.
7. shelter.
8. refuse.
9. mark.
10. close.
11. reopen.
12. carry.
13. count.
14. forgive.
15. erase.

Good nouns:

1. vow.
2. ledger.
3. seal.
4. witness.
5. road.
6. silence.
7. refuge.
8. burden.
9. mandate.
10. pass.
11. petition.
12. register.
13. lamp.
14. chamber.
15. wound.

Words to use carefully:

1. God.
2. divine.
3. mercy.
4. purification.
5. final.
6. release.
7. peace.
8. witness.
9. non-return.
10. annihilation.

The word God should appear only in late corrupted state content, leader titles, or foreign reactions. It should not be used for early Buddhist path text.

### 189. Localization Samples

These are tone samples. They should guide final writing rather than replace polished localization.

#### 189.1 Formation Sample

**The Figure at the High Monastery**

Reports describe a teacher leading gatherings that threaten the state. The army counted rifles in the courtyards, and the monks counted names at the gate.

By morning, pilgrims had filled the road below the monastery. No order had sent them there.

Options:

1. **Let the monasteries handle it.**
2. **Invite the figure into government.**
3. **Restrict the gatherings.**
4. **Proclaim the new mandate.**

#### 189.2 Refuge Sample

**The Roads Climb Toward Silence**

Refugees arrived as the snow melted, followed by deserters, widows, monks, wounded soldiers, foreign children, and men who claimed to have forgotten their country.

Border officers counted the people they could admit. The Bodhisattva measured the cost of turning anyone away.

Options:

1. **Open the refuge roads.**
2. **Register every name.**
3. **Close the passes until order returns.**

#### 189.3 Arhat Sample

**A Village without Petitions**

The district office reports no petitions for ninety days. The Arhat overseer records the silence as proof of peace, and the local clerk has asked to be reassigned.

The petition box remains in the square. Its slot has been polished smooth by weather, not by use.

Options:

1. **Praise the overseer.**
2. **Send an inquiry.**
3. **Remove the Arhat quietly.**
4. **Expand the method.**

#### 189.4 Buddha Mandate Sample

**The Buddha Mandate**

The foreign envoys expected a proclamation. They received a sealed copy of the new constitutional order.

The document names a witness and records the throne as an instrument of that witness.

Options:

1. **The lamps remain lit.**
2. **Let the world read what it can.**

#### 189.5 Renunciation Sample

**The Vow against Annihilation**

The target ledger was carried into the chamber and placed before the ministers, who left it closed.

The Buddha spoke once. Peace had to leave witnesses alive.

Options:

1. **Seal the vow.**
2. **The world remains guilty and alive.**

#### 189.6 Divine Sovereignty Sample

**The Throne without a Body**

The clerks removed the ruler's name from the daily orders and replaced it with Witnessed by the Sovereign Path.

Foreign diplomats asked who now governed the Realm. The reply arrived without a signature.

Options:

1. **No hand is required.**
2. **The state has become witness.**

#### 189.7 Final Silence Sample

**The Final Silence**

The last peace delegation remained inside as the roads closed at dawn.

At noon, the Mandala Bureau entered the sky into the register, and by dusk the first foreign capital had disappeared from the ledger of future petitions.

Options:

1. **The last war has ended.**

#### 189.8 Foreign Reaction Sample

**Reports from the High Passes**

The embassy cable is incomplete. It describes sealed airfields, missing ministers, silent radio towers, and a doctrine that no translator will sign.

The final line was added by hand: They no longer believe we are countries.

Options:

1. **Prepare containment.**
2. **Dismiss the reports as mountain theatre.**
3. **Send one final envoy.**

### 190. Event Log Writing Rules

Holy Realm event logs should read like short historical records. They should be useful for later callbacks.

Rules:

1. Keep entries short.
2. Mention the decision outcome.
3. Mention the stage or counter affected if relevant.
4. Avoid raw mechanics in the main sentence.
5. Use a second sentence for gameplay summary if needed.
6. Log major stage changes, major schisms, first intervention, first use of pacification, Buddha Mandate, Divine Sovereignty, Renunciation, Final Silence warning chain, launch, interruption, and completion.

Example log entries:

1. **The Holy Realm opened the refuge roads. Border camps grew along the high passes, and the state began treating flight itself as a petition for protection.**

2. **The Arhats took office. The government became faster, quieter, and harder to question.**

3. **The Compassion Schism ended with the Mandala Bureau empowered. The Quietists remained in the monasteries, but their objections no longer shaped state road policy.**

4. **The Buddha Mandate was proclaimed. Foreign governments could no longer decide whether they faced a religion, a state, or a new kind of command.**

5. **The Vow against Annihilation was sworn. The target ledger was sealed, though the world outside the mountains continued to burn.**

6. **The Final Silence began. The Holy Realm entered the world into the register and started closing it by force.**

7. **The Mandala broke. The launch network failed before the last road could close.**

### 191. World Threat Text Direction

The Holy Realm should use unique world threat names and descriptions.

World threat names:

1. Holy Realm Awakening.
2. Buddha Mandate Proclaimed.
3. Divine Sovereignty Declared.
4. Final Silence Warning.
5. Final Silence Armed.
6. Final Silence Active.
7. Thermonuclear Mandate Active.
8. Mandala Broken.
9. Holy Realm Contained.

World threat descriptions:

1. **Holy Realm Awakening**
   - A mountain state has reorganized itself around a living sacred mandate. For now, it speaks of refuge.

2. **Buddha Mandate Proclaimed**
   - The Holy Realm no longer treats its ruler as an ordinary head of government. Foreign ministries are struggling to define what kind of state they face.

3. **Divine Sovereignty Declared**
   - The Holy Realm has crossed into a doctrine where state authority, spiritual authority, and final judgment are no longer separated.

4. **Final Silence Warning**
   - Intelligence reports suggest the Mandala Bureau is preparing a global target doctrine.

5. **Final Silence Armed**
   - The Holy Realm has the doctrine, industry, and weapons needed to begin a world-end scenario if final conditions remain true.

6. **Final Silence Active**
   - The Holy Realm has begun nuclear or thermonuclear strikes outside its own territory. The world-end scenario is active.

7. **Mandala Broken**
   - The Holy Realm launch network has been interrupted. The danger remains, but the immediate world-end sequence has failed.

### 192. Custom UI Asset List from Part 5

Part 5 defined the Holy Mandala Panel and Final Silence Ledger. The asset list should be explicit so the Photoshop prompt and coding agent can connect.

Required UI assets:

1. Holy Mandala main panel background.
2. Central stage ring.
3. Stage icons for Refuge, Bodhisattva, Arhat Administration, Buddha Mandate, Divine Sovereignty, and Final Silence.
4. Stage ring states for locked, available, active, corrupted, rejected, and crisis.
5. Spiritual Legitimacy gauge.
6. Compassion Drift gauge.
7. Mandala Reach gauge.
8. Final Silence Pressure gauge.
9. Doctrine memory strip.
10. Active effects frame.
11. Arhats tab frame.
12. Refuge tab frame.
13. Diplomacy tab frame.
14. Doctrine tab frame.
15. Warnings tab frame.
16. Event log button.
17. Final Silence warning button.
18. Tooltip frames.
19. Progression seals.
20. Vow mark overlay.
21. Corrupted seal overlay.
22. Crisis ash overlay.
23. Foreign intelligence compact panel.
24. Degraded mode decision icon set.

Required Final Silence Ledger assets:

1. Ledger main panel background.
2. Doctrine status section.
3. Weapon stage section.
4. World ledger section.
5. Holy Realm integrity section.
6. Interruption options section.
7. Target list row frame.
8. Marked state icon.
9. Struck state icon.
10. Burning state icon.
11. Wasteland state icon.
12. Silent state icon.
13. Holy Realm protected marker.
14. Launch network integrity gauge.
15. Retaliation damage marker.
16. Mandala break overlay.
17. Thermonuclear variant overlay.
18. Empty Mandala completion state.
19. Grouped strike notification frame.
20. Multiplayer warning frame.

Required map overlay assets:

1. Marked state map icon.
2. Struck state map icon.
3. Burning state map icon.
4. Wasteland state map icon.
5. Silent state map icon.
6. Protected Holy Realm boundary mark.
7. Cracked Mandala marker.
8. Foreign containment marker.
9. Evacuation marker.
10. Launch network target marker.

### 193. Sound and Music Direction

Sound is optional, but the Holy Realm benefits from restrained audio.

General sound direction:

1. Low bell.
2. Distant wind.
3. Paper stamp.
4. Soft radio static.
5. Wood or stone room tone.
6. Low drum only for military branches.
7. No loud choir by default.
8. No triumphant march for Final Silence.

Recommended stingers:

1. **Holy Realm Formation**
   - Single low bell and wind.

2. **Bodhisattva Recognition**
   - Soft bell with short paper stamp.

3. **Arhat Administration**
   - Stamp, page turn, low room tone.

4. **Buddha Mandate**
   - Bell, long silence, faint radio static.

5. **Renunciation**
   - Bell followed by open air sound.

6. **Divine Sovereignty**
   - Low bell, no reverb tail, abrupt stop.

7. **Final Silence**
   - Static, distant bell, then silence before the first strike notification.

8. **Thermonuclear Mandate**
   - Same as Final Silence with lower, harsher tone.

9. **Mandala Breaks**
   - Cracking seal, radio cut, wind returns.

Music direction:

1. Sparse.
2. Slow.
3. No heroic theme.
4. Use drones, low bells, wind, distant throat-like tones only if they do not become theatrical.
5. Silence should be treated as part of the sound design.

### 194. Documentation Requirements for the Coding Agent

The coding agent should document the Holy Realm system as a connected event ecosystem.

Required documentation topics:

1. How Tibet or a Tibetan successor becomes the Holy Realm.
2. How each stage is reached.
3. How Spiritual Legitimacy works.
4. How Compassion Drift works.
5. How Mandala Reach works.
6. How Final Silence Pressure works.
7. Which focuses change which counters.
8. Which event choices are off-ramps.
9. How Arhat assignments work.
10. How refugee policy affects later events.
11. How diplomacy and peacekeeping decisions work.
12. How the Buddha Mandate is triggered.
13. How Renunciation blocks final doctrine.
14. How Divine Sovereignty is reached.
15. How Final Silence checks hard conditions.
16. How 1945 nuclear and 1947 thermonuclear variants differ.
17. How foreign AI response works.
18. How multiplayer warnings work.
19. How settings can disable or restrict the path.
20. Which assets are required and which are optional.
21. Which later Germany and Malta hooks are reserved but not implemented in this Holy Realm pass.

The documentation should also mention failure states. A maintainer should understand why the Holy Realm did not escalate in a campaign.

### 195. Implementation Boundaries

The coding agent should implement the Holy Realm as deeply as the mod structure allows, but it should not invent unrelated systems when existing Chaos Redux systems already cover them.

Use existing Chaos Redux systems where possible:

1. Chaos Meter.
2. Event evolutions.
3. Event logs.
4. Super events.
5. World-end scenario framework.
6. Condemnation.
7. Deaths.
8. Air cleanliness.
9. World threats.
10. Settings.
11. Multiplayer safety behavior.
12. Any existing nuclear or wasteland logic.
13. Any existing UI conventions.

Avoid creating parallel systems for:

1. Global threat if world threats already exist.
2. Death tracking if deaths already exists.
3. Nuclear devastation if wasteland or world-end logic already exists.
4. Settings if Chaos Redux already has world-end toggles.
5. Event logs if existing logs can be extended.
6. Super-event behavior if existing super-event framework can be reused.

The Holy Realm can add new variables, flags, UI assets, spirits, and decisions, but those should connect to existing architecture.

### 196. Required Minimum Implementation

The Holy Realm should not be reduced to only a country rename and a few events. A minimum implementation should include:

1. A formation route for Tibet or a Tibet-centered state.
2. A focus tree or focus branch with clear Holy Realm identity.
3. Bodhisattva stage.
4. Arhat Administration stage.
5. Buddha Mandate stage.
6. A restrained path that rejects final doctrine.
7. A coercive path that can lead to Divine Sovereignty.
8. Core counters or equivalent tracked flags.
9. Event choices that affect future text and options.
10. Arhat, refuge, diplomacy, and doctrine decisions.
11. At least one super event for Buddha Mandate or Final Silence.
12. Final Silence hard conditions.
13. 1945 nuclear world-end variant.
14. 1947 thermonuclear variant if the mod supports thermonuclear logic.
15. AI restraint rules.
16. Foreign response events.
17. Settings integration.
18. Multiplayer warning behavior.
19. Event log integration.
20. Asset placeholders or proper asset requests for every required visual.

If custom UI cannot be implemented immediately, degraded mode must preserve player clarity through decision categories, tooltips, event logs, and warning events.

### 197. Optional Enhancements

These are useful but not mandatory for the first implementation pass.

Optional additions:

1. Unique Arhat advisor pool with portraits.
2. Foreign intelligence compact UI.
3. Full Holy Mandala panel.
4. Full Final Silence Ledger.
5. Dynamic focus descriptions based on Compassion Drift.
6. Multiple Buddha portrait variants.
7. Unique sound stingers.
8. Holy Realm music cue.
9. Multiple refugee policy event chains.
10. Rare Hidden Buddha path.
11. Arhat Oligarchy path.
12. Military Capture path.
13. Mandala Break post-world-end interruption chain.
14. Reconstruction events after Final Silence interruption.
15. Foreign pilgrimage subchains.
16. Special subject type for supervised peace administrations.
17. Foreign propaganda campaigns against the Realm.
18. Detailed map overlay for target stages.
19. Thermonuclear super-event variant.
20. Late-game world archive of states marked silent.

Optional does not mean disposable. If the coding agent chooses to implement an optional feature, it should implement it cleanly rather than as a placeholder.

### 198. Reserved Connection Layers

The Holy Realm should keep hooks for later content, but this Holy Realm spec should not implement those later chains unless explicitly requested.

Reserved hooks:

1. **Tibetan Expedition Hook**
   - Later Germany content can send an expedition to Tibet or Holy Realm territory.
   - Positive results can create a Master Race myth flag.
   - The Holy Realm should expose a clean flag or event target for this.

2. **Mengele and Auschwitz Experiments Hook**
   - Later Germany content can use biological research and facility systems.
   - The Holy Realm should not depend on this.
   - Any connection should come through later expedition or ideology events.

3. **Malta Crusaders Hook**
   - Later Malta content can form or lead the Teutonic Order faction.
   - The Holy Realm can have a reserved reaction flag if invited under rare conditions.

4. **Teutonic Order Hook**
   - Later content can create a temporary alliance between Malta, Germany, and the Holy Realm under extreme ideology fusion conditions.
   - The Holy Realm should not join this naturally through its own core path.

5. **Final Crusade Hook**
   - Later content can add a super event and global war goal for the combined faction.
   - This should be separate from Final Silence.
   - Final Crusade is religious-imperial conquest.
   - Final Silence is world erasure.

6. **Atlantis Breakaway Hook**
   - Later Germany content can break from the faction and claim Atlantis descent.
   - The Holy Realm can become a target or betrayed ally.
   - This should be a later cross-event chain.

7. **Blessed Hitler and Catholic-Buddhist-Nazi Fusion Hook**
   - This is deliberately outside the Holy Realm core.
   - It should only activate through rare cross-event prerequisites.
   - It should not contaminate the normal Holy Realm path.

The Holy Realm must stand on its own. The later connections should feel like rare campaign collisions, not the main purpose of the state.

### 199. Final Integration Checklist

Before implementation is considered complete, the coding agent should verify:

1. The Holy Realm can form through the intended route.
2. The player can avoid the path.
3. The path has a defensive version.
4. The path has an administrative version.
5. The path has a peacekeeper version.
6. The path has a coercive pacification version.
7. The path has a renunciation version.
8. The path has a final doctrine version.
9. Bodhisattva, Arhat, Buddha, Divine Sovereignty, and Final Silence stages are distinct.
10. Counters or equivalent flags affect future content.
11. Event choices have memory.
12. AI does not rush Final Silence.
13. Foreign AI responds to dangerous stages.
14. Settings are respected.
15. Final Silence cannot trigger before 1945.
16. Final Silence requires Chaos Meter above 1000 in standard settings.
17. Final Silence requires Holy Realm strongest-factory status in standard settings.
18. 1947 thermonuclear variant is handled if relevant.
19. World-end event logs are written.
20. Condemnation, deaths, air cleanliness, and world threats are connected where relevant.
21. Non-final Holy Realm paths remain meaningful.
22. UI or degraded mode makes player-facing state clear.
23. Assets are requested or implemented.
24. Later Germany and Malta hooks are only reserved, not forced into the Holy Realm core.

### 200. Final Spec Completion Note

This completes the Holy Realm portion of the Chaos Redux event specification.

The Holy Realm is designed as a full country transformation and event ecosystem. It begins as a mountain refuge, grows into a Bodhisattva-led state, creates the Arhat Administration, reaches the Buddha Mandate, and can either renounce annihilation, become a coercive pacification power, or cross into Divine Sovereignty and Final Silence.

The Holy Realm path should remain serious, restrained, and internally coherent. It should use Buddhist vocabulary as in-world political mythology and state doctrine. It should avoid treating religion as a joke. Its danger should come from calm certainty, administrative control, and the belief that peace can be forced into existence.

The coding agent must follow AGENTS.md and the chaos-redux-events skill. The agent must keep all Chaos Redux systems aligned, including Chaos Meter, evolutions, event logs, super events, world-end scenarios, condemnation, deaths, air cleanliness, world threats, settings, multiplayer behavior, and existing implementation conventions.

The Germany, Mengele, Tibet expedition, Malta Crusaders, Teutonic Order, Final Crusade, and Atlantis ideas remain reserved for later specifications. They should be developed as separate connection layers after the Holy Realm implementation is complete.
