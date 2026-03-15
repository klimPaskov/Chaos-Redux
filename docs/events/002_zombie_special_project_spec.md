# Zombie Outbreak

## 1. Core goal

Add two zombie-related special projects to the biowarfare facility.

The first project is a short anti-zombie support project that helps contain existing zombie outbreaks.

The second project is a long and complex offensive project called **Weaponize the Zombies**. It creates a custom zombie strain that can be deployed as a strike weapon. The final strain depends on many earlier choices, so the research path should matter and produce clearly different outbreak outcomes.

This whole system should feel dynamic, dangerous, and replayable. It should not be a linear research path with one fixed result.

---

## 2. Special project A: Anti-Zombie Bombs

### 2.1 Purpose

This is a fast support project for the biowarfare facility.

Its purpose is not to destroy zombies outright, but to decontaminate states where zombies are active and make those states much less useful for zombie expansion.

### 2.2 Unlock conditions

The project can only be useful when the zombie cure system is already active.

The bombs themselves can only be deployed while the cure is active.

If the cure is inactive, this project should still exist as completed content, but its strike action should be unavailable.

### 2.3 Research profile

This special project should be short and easy to complete.

### 2.4 Deployment

The bombs are deployed through strikes.

A successful strike applies a **state decontamination modifier**.

This modifier should do two things at minimum:

1. Apply strong anti-zombie effects in that state.
2. Reduce recruitable manpower from that state so zombies cannot meaningfully draw manpower from it.

### 2.5 State modifier behavior

The decontamination modifier should be strong, but specific.

It should weaken zombies in that state through a combination of effects such as lower combat effectiveness, lower spread efficiency, lower reinforcement efficiency, or anything else that makes sense for the zombie system.

It should not be a generic anti-human debuff. It should target zombies specifically.

The manpower reduction should be significant enough that the state becomes a poor source of zombie manpower.

### 2.6 Duration logic

These state modifiers do not use a normal fixed timer.

Instead, they remain active for as long as the cure is active.

The moment the cure becomes inactive, all anti-zombie decontamination modifiers created by these bombs must be removed from every state.

### 2.7 Stacking rules

These bombs must not stack.

If a state already has the anti-zombie decontamination modifier, dropping another bomb there should not make the modifier stronger.

So simply make the state where there already is decontamination modifier, unraidable with the anti zombie bomb.

### 2.8 AI and balance intention

This project should be a containment tool.

It should be useful against zombie-held or zombie-threatened states, but it should not replace normal military solutions.

It exists to buy time, weaken infected zones, and deny zombie manpower.

---

## 3. Special project B: Weaponize the Zombies

## 3.1 Purpose

This is a long, dangerous, highly iterative special project.

Its goal is to create a deployable zombie disease weapon that produces different outbreak types based on research decisions made during development.

This project should feel like the player is building a pathogen profile over time.

### 3.2 Research profile

This project should take a very long time to complete.

It should contain many special iterations, choice events, and follow-up tests.

The player should not just click once and wait. The interesting part is the sequence of decisions.

### 3.3 Main design principle

The final zombie strain is not one fixed template.

It should be assembled from hidden and visible variables created during the project.

Important variables should include:

1. Nature of the disease
2. Cause or origin of the outbreak
3. State of consciousness after infection
4. Physical strength
5. Infectiousness
6. Movement speed
7. Durability
8. Cure resistance
9. Friendliness or loyalty behavior
10. Resource allocation intensity
11. Number of test subjects used
12. Whether field trials were performed
13. Whether forbidden branches were pursued

These variables should later determine the final zombie outbreak type, cure difficulty, bomb cost, accident risk, and AI behavior of the resulting horde.

---

## 4. Research flow for Weaponize the Zombies

## 4.1 Stage 1: Initial acquisition

The first step is to study the zombies.

The project begins by extracting infected subjects into the player’s country for controlled study.

This is the first real commitment to the project and should frame the rest of the chain.

### 4.2 Stage 2: Controlled experimentation opens

After extraction, the player can begin experimenting on captured infected subjects.

This should unlock the first major decision event.

### 4.3 Stage 3: Determine the nature of the disease

This event decides what the disease appears to be.

This should have several options, not just two.

Possible options:

1. Neurobiological pathogen  
   The disease primarily attacks the brain and suppresses higher cognition.

2. Rage-inducing degenerative agent  
   The disease produces hatred, aggression, and loss of restraint.

3. Parasitic symbiosis  
   The disease may be a living parasite or linked organism rather than a standard pathogen.

4. Necrotic reanimation phenomenon  
   The infected may be physically dead or partially dead and moving anyway.

5. Extra-scientific or demonic corruption  
   The disease cannot be fully explained through normal science.

This choice should heavily influence later outcome pools.

### 4.4 Stage 4: Basic sacrifice for testing

A later iteration requires live testing and consumes **1000 manpower**.

This represents staffing, disposable test groups, or condemned subjects.

This step is important because it marks the project moving from theory into human experimentation.

### 4.5 Stage 5: Resource allocation choice

Add an iteration where the player decides how many extra resources to commit.

This should directly speed up the project, but also increase hidden accident risk.

Three levels make the most sense:

1. Minimal allocation
2. Expanded funding
3. Maximum priority

Higher levels should speed up progress more, but also increase the chance of a containment failure later.

### 4.6 Stage 6: Are the infected truly dead

Add another major hypothesis event:

1. They are biologically dead and only the infection is animating the body.
2. They are alive, but mentally overridden.
3. Their minds remain active in fragments.
4. They are transformed into something else entirely.

This should matter a lot.

If minds remain active in fragments, that should make intelligent or selectively loyal strains more plausible.

If they are fully mindless, then friendly and selective-control outcomes should become much less likely.

If they are undead in a true sense, that should support the demonic or catastrophic paths.

### 4.7 Stage 7: Strain tuning iterations

This is where the player shapes the final weapon.

Each major property should use the same clear pattern of three options:

1. Mild
2. Medium
3. Strong

This should apply at least to these parameters:

1. Strength
2. Infectiousness
3. Speed
4. Durability
5. Cure resistance
6. Friendliness or obedience tendency

These choices should have clear consequences in cost, risk, and final outbreak type.

So there should be separate iteration events for each of those parameters throughout research.

### 4.8 Stage 8: Field testing

At some point the player should test the weapon outside the lab.

If there is an enemy country, the player should be allowed to test it against that enemy.

If there is no enemy country, the project must allow a domestic test under supposedly safe conditions.

Domestic testing should always carry a real outbreak chance.

Conducting tests should grant a research speed bonus because the researchers now have practical data.

The domestic test is supposed to feel useful but dangerous.


### 4.9 Stage 9: Final conclusions event

When the project is completed, fire a conclusions event that explains what kind of zombie weapon was actually created.

This event should summarize the major branch choices and explicitly name the resulting outbreak type.

This is the moment where the project result becomes legible to the player.

---

## 5. Important research iterations and their gameplay effects

Each choice determines how long the research will take, how costly the bombs will be, and what attributes the zombies will have. The stronger the choice, the more impact on those things.

## 5.1 Strength iteration

This determines how physically dangerous the infected are. Like attack, defense, breakthrough, etc.

Mild strength should keep the project cheaper and safer.

Strong strength should make the disease weapon more devastating, increase cost, and increase cure difficulty indirectly through battlefield pressure.

Strong strength should also push the strain away from subtle or semi-controlled behavior and toward brute-force outcomes.

## 5.2 Infectiousness iteration

This is one of the most important values. So, it should increase strike success chance and improve outbreak growth or spread (how quickly they core occupied territory, how much recruitable manpower they can get, etc)

This is also the main stat that determines how likely a successful strike becomes an actual functioning outbreak.

## 5.3 Speed iteration

This determines how quickly the zombies move and pressure territory.

Fast strains should be more dangerous operationally.

High speed should also strongly support animalistic, rabid, predatory, or Wendigo-style branches.

Slow strains should support tankier siege-style undead.

## 5.4 Durability iteration

This is effectively HP and org. So how much manpower they will deplete in combat.

This should also increase bomb production cost and cure difficulty.

Durable strains fit necrotic, undead, demonic, and armored-beast variants especially well.

## 5.5 Cure resistance iteration

This needs to be a dedicated iteration.

Its purpose is to make the resulting outbreak harder to cure.

This should directly affect how difficult it is for other countries to unlock the correct cure for this specific strain.

## 5.6 Friendliness or obedience iteration

This is not a simple yes or no setting.

The player can choose mild, medium, or strong friendliness intent, but that should only be one input, not a guarantee.

The actual final social behavior of the strain must also depend on earlier choices, especially:

1. Nature of the disease
2. Whether minds remain active
3. Whether the strain is mindless or not
4. Whether the cause was scientific, parasitic, or demonic

This means a player cannot just force friendly zombies out of a completely mindless rage plague.

The system should apply logic here.

---

## 6. Social behavior logic of the resulting zombies

## 6.1 Main rule

Friendliness is an outcome shaped by multiple variables.

The friendliness iteration is only a directional influence.

It should never override logic from earlier research.

## 6.2 Outcomes that support friendly or semi-friendly zombies

Friendly or selectively loyal zombies should only be realistically possible when at least some of the following are true:

1. The disease is not fully mindless
2. Some mental activity remains after infection
3. The cause is scientific, parasitic, or hybrid rather than purely rage-driven
4. Friendliness was intentionally pushed toward medium or strong (the stronger, the higher chance for friendliness)
5. Extreme brute-force mutations were not chosen across every category

These outcomes should create strains that can behave in one of these ways:

1. Friendly toward humans in general, focused on attacking only other zombies or non-human entities
2. Friendly only toward the creator

## 6.3 Outcomes that make friendliness unlikely or impossible

Friendly strains should be unlikely or impossible if most of the following are true:

1. The disease was defined as mindless
2. The infected are treated as biologically dead with no mind left
3. The cause is pure rage corruption
4. Extreme strength, speed, and infectiousness were all pushed hard
5. The project leaned heavily into demonic or undead explanations

In these cases, the strain should become hostile to almost everyone, including the creator.

## 6.4 Special anti-zombie-friendly path

There should be a valid path where the resulting zombies are not friendly to humans in a normal sense, but are highly hostile to other zombie outbreaks and other non-human entities.

This makes the bomb useful as an anti-zombie weapon.

If the final strain belongs to this category, the strike should only be allowed in non-human states.

That means the bomb can only be used where the target state is already controlled by zombies or another non-human threat.

This path should be tied to a mix of selective cognition, moderate friendliness, and research directions that do not produce pure mindless frenzy.

---

## 7. Final outbreak archetypes

The conclusions event should name the final result. The project should not produce one generic outbreak. It should produce one of several archetypes.

These are the main outbreak types the system should support.

## 7.1 Rabid Horde

Cause leans scientific or rage-based. Minds are mostly gone. High infectiousness and speed. Low or medium friendliness.

This is the classic hostile outbreak. It spreads fast, hits hard, and is difficult to contain operationally.

## 7.2 Necrotic Siege Strain

Cause leans necrotic or undead. The infected are effectively dead. High durability. Lower speed. Strong pressure through staying power. So, they are not as aggressive, and will not always be in attack.

This is slower but much harder to eliminate.

## 7.3 Parasitic Directed Strain

Cause leans parasitic. Some cognition remains. Medium or high friendliness. Medium speed. Medium or high infectiousness.

This supports selective hostility and higher obedience. This is one of the best branches for creator-loyal zombies.

## 7.4 Controlled Loyalty Strain

This is the branch where the infected are hostile to everyone except their creator.

It requires preserved or partially preserved cognition and strong friendliness direction, but not full human-level control.

This should be rare and should require logical supporting choices earlier in the chain.

## 7.5 Purifier Strain

This is the anti-zombie branch.

These zombies prioritize attacking other zombies and non-human threats. They are not fully friendly in a civilian sense, but they can function as a weapon against existing outbreaks.

This branch should require enough retained cognition to distinguish targets.

This is the key path that justifies using zombie disease bombs against zombie-held states. Using this weapon shouldn't cause condemnation. Human targeting zombie bombs should cause immense condemnation.

## 7.6 Semi-Sapient Cooperative Strain

This is the most controlled and least monstrous path.

It should only be possible if the disease is not mindless, minds remain at least partly active, and extreme brute-force mutations were avoided, so things are mostly mild.

This branch should be rare and unstable. It should not be easy to get.

## 7.7 Creator-Betrayer Strain

This is the path where the player tried to create obedience but failed.

The strain ends up hostile to everyone except perhaps briefly appearing stable and friendly to humans/creator at first.

This is good for dramatic outcomes and failed experiments. So you think they are friendly and intentionally don't border them, and then suddenly they turn on you.

## 7.8 Demonic Catastrophe

This is the forbidden branch.

If the disease is interpreted as demonic, the infected are treated as truly undead, and the player picked at least four strongest mutation options, then a catastrophic special outbreak can fire.

This becomes the Wendigo event chain. Fire a special super event for that.

## 7.9 Canonical Zombie Convergence

If the final weaponized strain resolves into a mindless, undead, aggressive profile with only weak or medium mutation intensity, it should not remain a distinct custom outbreak type. Instead, it should use the same behavior, rules, and identity as the standard canonical zombie outbreak. This represents the research arriving at nothing more than a weaponized version of the already known zombie condition rather than a truly new strain.

---

## 8. Wendigo catastrophic branch

## 8.1 Trigger logic

Add an easter egg disaster event chain.

This should become possible if all of the following are true:

1. The cause or nature was set to demonic or extra-scientific
2. The infected were judged to be undead or beyond normal life
3. At least four mutation categories were set to their strongest option

Good categories to count are strength, speed, durability, infectiousness, and cure resistance.

This should not be guaranteed every time, but it should be a valid disaster branch tied to reckless choices. the more reckless, the stronger probability. If all evolution choices were chosen to be strongest, then this is guaranteed to happen.

## 8.2 Result

A special outbreak occurs with a super event.

A creature named **Wendigo** becomes the leader of this outbreak.

This outbreak is not made of normal human zombies.

It consists of corrupted animal horrors.

They should be much faster, much more durable, and much more dangerous than normal zombies.

Thematically they should feel like predatory biomechanical undead wildlife rather than shambling human infected.

## 8.3 Special mechanics of Wendigo outbreak

These forces should:

1. Be much stronger than normal zombies
2. Move faster
3. Have more durability
4. Have some armor value
5. Core occupied land
6. Use less manpower than normal zombies
7. Require only manpower and no equipment
8. Gain only about 15 percent extra recruitable population from their hunger-style idea

This should make them terrifying, but distinct from standard zombie factions.

## 8.4 Super event

This absolutely needs a super event.

The event should make clear that the player did not create a controllable disease. They opened something worse.

---

## 9. Accident and containment failure system

## 9.1 General idea

While researching Weaponize the Zombies, there should be a small hidden chance of an accident at the state containing the biowarfare facility.

This accident creates a minor outbreak, not as strong as the dynamic ones from the normal zombies.

The outbreak should be presented externally as a normal zombie outbreak with the normal news event and normal presentation.

The player should not get a separate obvious public label saying it was their fault.

## 9.2 Chance growth logic

At the start of the project, the chance should be very low.

It should rise as the player becomes more reckless.

The hidden accident chance should grow from factors such as:

1. More test subjects
2. Higher resource allocation
3. Field testing
4. Stronger mutation choices
5. Demonic or unstable branches
6. Domestic testing
7. High infectiousness

The increase should be meaningful, but not so high that the accident becomes routine.

## 9.3 One-time rule

If a containment accident outbreak happens, it cannot happen again from this system.

Set a one-time country flag so only one secret lab accident outbreak may occur.

## 9.4 Interaction with normal zombie systems

This accident outbreak must **not** trigger the 365-day break that normally pauses dynamic zombie outbreaks.

It should be treated as separate from the standard timing lockout.

The point is that this accident is a hidden lab failure, not part of the regular world outbreak pacing.

---

## 10. Zombie Disease Bomb equipment

## 10.1 Unlock

When Weaponize the Zombies is completed, unlock a new equipment type:

**Zombie Disease Bomb**

## 10.2 Stockpile reward

Project completion should automatically grant a small initial stockpile of zombie bombs.

This is enough to show that the project produced usable prototypes.

It should not be enough for long sustained bombing without production.

The player must still produce more bombs to use the weapon seriously.

## 10.3 Production cost

These bombs should be extremely expensive by default.

Even the weakest viable zombie bomb should be costly.

The cost should scale upward based on the choices made during research.

High values in strength, infectiousness, speed, durability, and cure resistance should all make the bomb more expensive.

Selective-control strains and rare friendly strains can also justify extra cost because they are harder to engineer.

The strongest and most exotic outcomes should be brutally expensive.

---

## 11. Strike deployment rules for Zombie Disease Bombs

## 11.1 Basic deployment

Zombie Disease Bombs are deployed through strikes.

A successful strike creates a new outbreak type in the target.

## 11.2 Success chance

The strike success rate should be tied mainly to the chosen infectiousness level.

The interface should reflect this clearly.

Mild infectiousness means lower strike success.

Strong infectiousness means much higher strike success.

Other factors can influence final success too, the stronger, the better.

## 11.3 Targeting rules

Normal hostile strains can be used against enemy human-controlled states.

Purifier or anti-zombie strains can be used against non-human states.

If the final strain ended up strongly selective or semi-friendly, targeting restrictions should reflect that logic.

For example, a strain designed to attack only zombies should not be usable on a normal civilian target.

## 11.4 Interaction with existing zombie factions

This custom zombie outbreak should be hostile to other zombie outbreaks.

That matters because it gives the player a reason to use the bomb against zombie-held land, not just against human countries.

This also helps make the project feel like more than a simple offensive weapon.

If a weaponized outbreak has resolved into the standard canonical zombie profile, then when it comes into contact with the main dynamic zombie country or its equivalent zombie outbreak, it should be automatically annexed and integrated by that main zombie entity rather than remaining separate.

---

## 12. Cure system for weaponized zombie outbreaks

## 12.1 New cure category

A successful zombie disease bomb outbreak should not be solved by the default cure automatically.

Countries facing this new strain must discover a **separate cure** for that specific outbreak type.

This should be a new dynamic cure category tied to the bomb-created strain.

## 12.2 Cure identity

The cure should be linked to the actual final outbreak profile.

That means a fast rabid strain and a necrotic siege strain should not be treated as identical for cure purposes.

The system does not need infinite variants, but it should at least key the cure to the final named outbreak archetype or a final strain ID.

## 12.3 Cure difficulty

The stronger the final outbreak, the harder the cure should be to develop.

Cure resistance should have the strongest direct effect on this.

High infectiousness, demonic logic, and extreme durability can also support higher cure difficulty. There is also a chance that the created zombie outbreak is uncurable, and so there will be no special cure category.

## 12.4 Creator advantage

The creator country should effectively already understand the strain because it made it. So, in the beginning the creator should have a cure for a year (time depends on how strong the outbreak is, so not always a year for all types, for some demonic or undead there might not even get a starting cure), until needing to develop a new one after it expires.

Other countries are the ones who need the new cure path right away. But, the player can choose to share the cure if they see fit, but it will reduce the cure to being available to everyone and thus the zombies can adapt to the cure quicker.

---

## 13. AI behavior for Japan

## 13.1 Research trigger

Japan should have strong AI weight to research Weaponize the Zombies when at war with China.

This should not be universal AI behavior for all countries in all situations. Japan should have a specific scripted preference here. Most AI countries should never start this special project, unless i explicitly said it.

## 13.2 Completion behavior

Once Japan completes the project, it should prioritize using Zombie Disease Bombs against China.

Prefer high-value Chinese states such as populous states, strategic corridor states, or heavily contested warfront states.

## 13.3 Branch preference

Japan’s AI should prefer practical offensive branches rather than experimental friendly-zombie paths.

That means the AI weight should lean toward hostile, controllable, or creator-loyal strains that are effective against human states.

It should not regularly drift into the rare semi-friendly branch unless specifically intended.

---

## 14. Achievements

Add achievements where they actually support gameplay identity.

Useful examples:

1. **Weaponize the End**  
   Complete Weaponize the Zombies.

2. **Fight Fire With Fire**  
   Use a zombie disease bomb against a zombie-held state.

3. **We Made a Cure, Then Made It Worse**  
   Deploy Anti-Zombie Bombs and Deploy custom Zombies in the same campaign.

4. **Containment Was Temporary**  
   Trigger the secret lab accident outbreak.

5. **Only Obeys Us**  
   Create a creator-loyal strain.

6. **A Friend to Mankind**  
   Create the rare branch where zombies attack only non-human entities.

7. **The Wendigo Rises**  
   Trigger the demonic catastrophic branch.
   
## 15. GFX requirements

Special GFX portraits should be based primarily on the final **creature type**.

That means the visual identity should reflect what the infected physically and biologically are, such as whether they are undead, parasitic, demonic, living but mindless, partially sapient, or something else of that kind.

If two strains behave differently but belong to the same creature category, they do not automatically need fully separate portrait sets. The main visual split should come from creature biology and condition, not diplomatic behavior.

At minimum, the system should support distinct portrait or equivalent special GFX sets for these creature-type categories:

1. **Living mindless infected**  
   Still biologically alive, but with higher cognition effectively destroyed. This should look like a diseased, frenzied, still-living human form rather than a corpse.

2. **Living partially aware infected**  
   Still alive, with traces of awareness, recognition, or directed behavior. These should look more controlled and less physically ruined than fully mindless infected.

3. **Parasitic infected**  
   The body is being directed or altered by a parasite or symbiotic organism. These should have unique visible mutations that suggest infestation, growths, internal takeover, or non-human biological control.

4. **Undead necrotic infected**  
   Functionally dead bodies that keep moving anyway. These should be visually distinct from living infected and clearly read as reanimated, decayed, or corpse-like.

5. **Demonic or extra-scientific corrupted infected**  
   These should not look like a standard disease victim at all. Their design should suggest supernatural corruption, ritual influence, unnatural anatomy, or something fundamentally beyond science.

6. **Wendigo**  

The **Canonical Zombie Convergence** result does not need its own special portrait set because it is supposed to collapse back into the normal canonical zombie identity already used by the mod.

---

## 16. Final design intent

Anti-Zombie Bombs are a containment and denial tool.

Weaponize the Zombies is a risky long-form project that builds a custom outbreak through layered decisions.

The player should feel that they are shaping a biological horror step by step, not just unlocking a generic bomb.

The rare branches should matter.

The safe branches should still be dangerous.

The strongest branches should be expensive, unstable, and difficult to cure.

The demonic branch should feel like the point where the research stopped being science and became a disaster.