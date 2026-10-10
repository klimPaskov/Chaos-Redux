# Zombie Outbreak

## 1. Core goal

Add two zombie-related special projects to the biowarfare facility.

The first project is a short anti-zombie support project that helps contain existing zombie outbreaks.

The second project is a long and complex offensive project called **Weaponize the Zombies**. It creates a custom zombie strain that can be deployed as a strike weapon. The final strain depends on many earlier choices, so the research path should matter and produce clearly different outbreak outcomes.

This whole system should feel dynamic, dangerous, and replayable. It should not be a linear research path with one fixed result.

## 1.1 Current implementation anchor

Both projects exist in source, so this document is a design contract to maintain rather than an unbuilt plan.
Read it against these owners before changing anything.

| Surface | Owner |
| --- | --- |
| Containment project and payload | `zombie_cure_bomb` in `common/special_projects/projects/biowarfare_main_projects.txt`, `zombie_cure_bomb_1` in `common/units/equipment/zombie_special_bombs.txt` |
| Containment raid | `common/raids/biological_zombie_cure_raid.txt` |
| Offensive project and its prototype choices | `weaponize_the_zombies` in `common/special_projects/projects/zombie_weaponized_projects.txt` |
| Offensive raids | `common/raids/zombie_weaponized_raids.txt`, `common/raids/zombie_weaponized_friendly_raids.txt` |
| Profile, archetype, cure and accident logic | `common/scripted_effects/zombie_special_project_effects.txt`, documented in the matching `.md` |
| Raid consequences and bridge events | `common/scripted_effects/zombie_native_raid_effects.txt`, `events/zombie_weaponized_special_projects.txt`, `events/zombie_native_raid_bridge_events.txt` |
| Tuning | the `anti_zombie_bomb`, `weaponized_zombies` and `weaponized_zombie_cxt_fixture` groups in `common/script_constants/zombie_special_project_constants.txt` |

Every number in this document is a description of those constant groups.
Tune the constants; do not reintroduce literals into script.

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

### 2.4 Deployment and state effect

The bombs are deployed through the containment raid, which reserves one produced cure payload per prepared raid and requires command power, preparation days and a bomber formation as recorded in the payload correction.

A successful strike applies the `zombie_decontaminated_state` dynamic modifier to the target state.
The modifier is deliberately controller-facing rather than a generic debuff: it strips most local manpower, cuts the controller's local supplies and movement speed, raises attrition against the controller, raises the enemy's local supplies, and blocks strategic redeployment for the controller.
Because it enables only while the state is zombie-controlled, it punishes the horde holding the state and goes dormant the moment a human government takes it back.

The manpower reduction is the point of the weapon: a decontaminated state is a poor source of zombie manpower.

### 2.5 Duration logic

The modifier uses no timer.
Its `remove_trigger` drops it as soon as the state no longer has an active zombie cure, so every decontaminated state loses the effect together when the cure lapses.

### 2.6 Stacking rules

The bombs do not stack.
A state that already carries the modifier fails `is_anti_zombie_bomb_target_state`, so it cannot be selected for another containment raid, and the apply effect is also guarded against a second copy.

### 2.7 AI and balance intention

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

Each prototype choice is gated on the previous one, so the chain is fixed even though the outcome is not.
The implemented order is: acquisition, nature of the disease, state of the infected, live testing, resource allocation, then the six tuning choices in the order strength, infectiousness, speed, durability, cure resistance and obedience, then field testing, then refinement or the forbidden branch, then deployment.
The stage headings below follow that order; a choice that is still locked shows only the step that has to come first.

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

### 4.4 Stage 4: Are the infected truly dead

The second hypothesis choice follows the nature of the disease:

1. They are biologically dead and only the infection is animating the body.
2. They are alive, but mentally overridden.
3. Their minds remain active in fragments.
4. They are transformed into something else entirely.

This should matter a lot.

If minds remain active in fragments, that should make intelligent or selectively loyal strains more plausible.

If they are fully mindless, then friendly and selective-control outcomes should become much less likely.

If they are undead in a true sense, that should support the demonic or catastrophic paths.

### 4.5 Stage 5: Live testing

The next step requires live testing and consumes the manpower sacrifice held in the `weaponized_zombies` constants.

This represents staffing, disposable test groups, or condemned subjects, and it marks the project moving from theory into human experimentation.

### 4.6 Stage 6: Resource allocation choice

The player then decides how much extra capacity to commit, which directly changes project progress and the hidden accident risk.

1. Minimal allocation: the project loses a little progress and adds the smallest risk
2. Expanded funding: moderate progress and moderate risk
3. Maximum priority: the largest progress gain and the largest risk

The tradeoff must stay legible: a rushed project is measurably more likely to fail containment later.

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

After the tuning choices the player decides whether to test the weapon outside the lab.

A test against an enemy country is preferred when one exists; otherwise the project allows a domestic test under supposedly safe conditions.

Both carry a real outbreak chance, scaled by the test site's population band, and the domestic variant is the more dangerous of the two.
Conducting a test advances the project because the researchers gain practical data, while skipping it costs progress and leaves the strain less understood.

### 4.9 Stage 9: Refinement, the forbidden branch, and deployment

After field testing the chain offers routine refinement or the forbidden branch, and the forbidden option becomes far more attractive to the AI when the profile is already extreme.

Deployment is the last prototype step and requires refinement to have resolved first, so the player always sees one deliberate finalisation before the weapon exists.

### 4.10 Final conclusions event

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

The Purifier path retains enough cognition to distinguish human communities from the non-human forces it hunts.
It requires the existing mix of selective cognition, moderate friendliness and research directions that avoid pure mindless frenzy.
Its strike may target a state controlled by an actual zombie outbreak or another explicitly supported non-human threat.
The target identity comes from that threat's own living country/profile contract, not from the general special-Chaos-country classification.
The Holy Realm is a human sanctuary even when its supernatural leadership makes it a special Chaos actor, so that classification cannot make Holy Realm territory a Purifier target.
A hostile zombie horde occupying a Holy Realm or ordinary human state is a valid non-human controller, while the same state under the sanctuary's or ordinary government's control is not.

Target permission must be checked at preparation, launch and outcome against the current controller and the payload's retained behavior profile.
If the controller becomes human before resolution, the action grants no outbreak or Purifier success reward there.
The native raid retains ownership of its payload reservation and cancellation outcome, following the accepted cure-payload correction where applicable.
Do not add a scripted refund or debit to resolve that targeting change.

Purifier use on a valid non-human target retains the intended exemption from human-target condemnation.
Hostile human-targeting strains retain their existing condemnation consequences through the owning system.
The same target gate applies to human and AI launch paths without changing their existing willingness weights.
Required cases are a peaceful Holy Realm controller, a hostile horde controlling its former sanctuary, and restoration of human control between preparation and outcome.

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

The risk is an MTTH whose base is a long interval and whose factors shorten it, so a cautious project effectively never fails and a reckless one eventually does.

Factors that shorten the interval:

1. More test subjects
2. Higher resource allocation
3. Field testing, and more strongly a domestic test
4. Stronger mutation choices and a high accumulated risk score
5. Demonic or unstable branches
6. High infectiousness

Factors that lengthen it, so biosecurity research is a real answer to the risk:

1. Fail-safe containment facilities
2. Sealed containment laboratories

The accumulated risk score is hidden, and the factors live in the `weaponized_zombies` constants as the base interval plus one multiplier per cause.
The result must stay meaningful without making the accident routine: recklessness is a bet, not a scheduled event.

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

Project completion grants the prototype stockpile held in the `weaponized_zombies` constants, which covers roughly two prepared strikes at the current per-raid payload.

That proves the project produced usable prototypes and nothing more: sustained use requires production.

## 10.3 Production cost

The bomb is deliberately expensive even in its weakest viable form, and its cost is built from the profile rather than a fixed price.

The base price comes from the profile cost tier, and each extreme choice in strength, infectiousness, speed, durability or cure resistance adds a further bonus, with the highest tier reserved for the most exotic outcomes.
Selective-control and rare friendly strains stay costly because they are harder to engineer.
All of those values live in the `weaponized_zombies` constants, so the price curve is tuned in one place.

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

Normal hostile strains can be used against eligible enemy human-controlled states.
Purifier and anti-zombie-friendly strains use the controller-and-profile contract in Section 6.4.
Selective or semi-friendly targeting must remain consistent with the retained cognition and social-behavior result.
A special-country marker, a change of country name or a supernatural leader does not by itself turn a civilian target into a non-human target.
The declared payload profile must govern both permission and the resulting outbreak, so an allowed Purifier strike cannot silently resolve as a human-hunting strain.

The implemented gate (`is_weaponized_zombie_raid_target_state`) is narrower than Section 6.4: a friendly strain may only strike a zombie-controlled state, so the broader non-human-threat permission is not available.
That narrower gate is the safe current behaviour and must not be widened without the other threat's own live-actor contract, because a general "non-human" test would let the classification alone authorise a strike.
A canonical-convergence strain is excluded from that friendly route entirely.

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

The creator already understands the strain, so it starts with a working cure that expires.
The window shortens as the strain gets worse, through the four steps held in the `weaponized_zombies` constants, and the harshest profiles get the shortest grace before the creator must develop a cure like everyone else.

Other countries need the new cure path immediately.
The creator may choose to share its cure, which makes it available to everyone and lets the strain adapt to it sooner.

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

Seven achievements carry this system's identity, each awarded by its own country flag so the condition is the actual play, not the project's existence:

1. **Weaponize the End**, `002_zombie_outbreak_21_weaponize_the_end`: complete Weaponize the Zombies.
2. **Fight Fire With Fire**, `002_zombie_outbreak_22_fight_fire_with_fire`: use a zombie disease bomb against a zombie-held state.
3. **We Made a Cure, Then Made It Worse**, `002_zombie_outbreak_23_we_made_a_cure_then_made_it_worse`: deploy both the containment bomb and a custom strain in one campaign.
4. **Containment Was Temporary**, `002_zombie_outbreak_24_containment_was_temporary`: suffer the laboratory accident outbreak.
5. **Only Obeys Us**, `002_zombie_outbreak_25_only_obeys_us`: create a creator-loyal strain.
6. **A Friend to Mankind**, `002_zombie_outbreak_26_a_friend_to_mankind`: create the branch that hunts only non-human enemies.
7. **The Wendigo Rises**, `002_zombie_outbreak_27_the_wendigo_rises`: trigger the catastrophic branch.


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

Installed coverage is eight weaponized portraits registered in `interface/chaosx_characters.gfx` as `GFX_portrait_ZZZ_weaponized_infected`, `_rabid`, `_parasitic`, `_mutant`, `_undead`, `_necrotic`, `_demonic` and `_wendigo`, with matching creator-category pictures cropped from the same sources.
Keep that mapping when an archetype is added or renamed: a new creature category needs its own portrait, while a new behaviour inside an existing category reuses the category's portrait.

---

## 16. Final design intent

Anti-Zombie Bombs are a containment and denial tool.

Weaponize the Zombies is a risky long-form project that builds a custom outbreak through layered decisions.

The player should feel that they are shaping a biological horror step by step, not just unlocking a generic bomb.

The rare branches should matter.

The safe branches should still be dangerous.

The strongest branches should be expensive, unstable, and difficult to cure.

The demonic branch should feel like the point where the research stopped being science and became a disaster.

---

## 17. Shared Chaos Redux system connections

Already connected in current source:

- A hostile strike's political and diplomatic consequences are applied by `apply_weaponized_zombie_strike_consequences`, which uses the CBRN doctrine multiplier and the condemnation system, preserves the Purifier exemption for a valid zombie-controlled target, and keeps treaty and Kruger consequences.
  Condemnation is not re-implemented here.
- Zombie-held states lose civilians monthly through the shared deaths ledger with the zombie-outbreak cause, so the Chaos Meter receives those losses without an event-specific accumulator.
- The Anti-Zombie League formation and the event's world-end branches are the event's deliberate Chaos Meter contributions, through `add_chaos_meter_value` with a history reason.
- Front movement around any resulting war feeds displacement and a food assessment through the shared hostile-capture adapter, so no strike effect should add its own refugee call.
- The containment payload's production, raid reservation and cancellation behaviour are owned by the native raid system as recorded in the payload correction.

Proposed (spec audit 2026-10-10):

- A zombie-outbreak famine adapter.
  The famine system defines an outbreak pressure source and adapters already exist for camps, chemical aftermath, Black Plague, natural disasters, acid rain and air winter, but not for the zombie outbreak, even though zombie-held states already apply an exact proven civilian loss each month.
  Add `famine_adapt_zombie_outbreak_state` following the Black Plague adapter's contract: state scope, the exact applied loss as the request amount, one food-context open on acceptance, and no second request for fighting the capture adapter already covered.
  This gives a large outbreak the food consequence it currently lacks without a new meter.
- Cure sharing as a visible choice with a cost.
  Sharing the creator's cure already helps everyone and shortens the strain's adaptation; the decision should also read in the condemnation and League surfaces, so a creator that releases a weapon and then shares the cure is treated differently from one that hoards it.

## 18. Open questions

These are proposals from the 2026-10-10 spec audit, not accepted design.

- The zombie-outbreak famine adapter and the cure-sharing consequence above.
- Whether the friendly-strain target gate should ever widen past zombie-controlled states; it stays narrow until another threat supplies a live-actor contract of its own.