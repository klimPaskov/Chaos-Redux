# Event 16 Brilliant Scientist, focus tree architecture

All focus names and route labels are working labels and not final localisation.

## Host country overlay branch

The host does not need a full replacement tree. It needs an event overlay branch or additive focus family if the existing repository supports event-added content. If implementation cannot add focus overlays cleanly, the same content can be decision-led. The design should preserve the mechanics either way.

### Host branch map

| Lane | Purpose | Unlock | Payoff |
| --- | --- | --- | --- |
| Public science lane | Keep Kruger inside universities and national science | Accept public recruitment or Evolution I | Safer research, medicine, industry, better Government Leverage |
| Military science lane | Use Kruger for weapons and secret projects | Accept secret recruitment or war pressure | Stronger rockets, electronics, nuclear, and special projects, higher Autonomy |
| Security lane | Protect, audit, screen, and contain the laboratory | Evolution II or early suspicion | Better Security Integrity and containment options |
| Ethical restraint lane | Peer review and public limits | Public route or scandal | Lowers Strangeness and rebellion risk, reduces extreme rewards |
| Sealed projects lane | Approve dangerous secret projects | Evolution III | Unlocks strongest technologies and rebel-asset memories |
| Final confrontation lane | Arrest, bargain, surrender authority, or prepare evacuation | Evolution III or IV | Determines containment, secession, or host subordination |

### Host branch interaction

The public science lane should strengthen ethical restraint and diplomatic openness. The military science lane should strengthen sealed projects and security. The player should be able to mix some support branches, but public restraint and full sealed-project autonomy should become incompatible at key route locks.

Host focuses should change the same values as decisions. A focus tree that gives only research bonuses would fail the event. Host focuses should alter Government Leverage, Autonomy, Security, Public Fame, Strangeness growth, project unlocks, foreign access, and final confrontation odds.

## Kruger country focus tree

The Kruger State needs a major country tree if it can become playable and pursue world conquest.

### Opening survival lane

| Focus group | Role | Gameplay direction |
| --- | --- | --- |
| Seize the complex | Establish country state | Cores or claims on seized lab states, stabilizes capital, starts war plan against host |
| Consolidate the staff | Prevent immediate collapse | Converts host staff, raises compliance-like control, reduces supply penalties |
| Rebuild the power grid | Solves energy and logistics | Factories, infrastructure, railways, supply hub work in seized area |
| Secure the perimeter | Defensive line | Forts, AA, radar, local guard divisions, anti-partisan tools |
| The first theorem of rule | Political identity | Locks Kruger as sovereign leader and opens project doctrine lanes |

### Internal control lane

Kruger should choose how his state functions.

| Route | Meaning | Tradeoff |
| --- | --- | --- |
| Human bureaucracy | Keeps human staff and normal industry | Lower Strangeness growth, weaker absurd units, better diplomacy |
| Clone administration | Solves manpower and obedience | Strong manpower, higher ethical collapse and unrest |
| Machine administration | Uses AI command and robotic logistics | Strong industry and robot units, supply and control vulnerabilities |
| Alien inner circle | Reveals more of Kruger’s true nature | Strong xenotechnology, severe diplomatic isolation |
| Temporal calculus office | Uses time projects to cheat development | Powerful prediction and unit tricks, reality instability |

### Project army lanes

Each lane should be a real branch with several focus groups. Branches can coexist partly, but deep specialization should matter.

| Lane | Military identity | Focus rewards |
| --- | --- | --- |
| Clone legions | Mass obedient infantry | Clone templates, manpower, recovery, cheap divisions, rebellion risk if control fails |
| Robot cohorts | Heavy industrial army | Robot templates, production lines, reliability, armor or mechanized variants |
| Specimen war parks | Monsters and dinosaurs | Shock units, fear effects, terrain bonuses, supply penalties, escape incidents |
| Xenoweapon detachments | Elite alien-equipped forces | Piercing, breakthrough, special weapons, aircraft and jet hooks |
| Temporal detachments | Time-displaced soldiers | Veteran units, planning, redeployment, event weirdness |
| Nuclear guard and final device | Strategic weapons | Reactors, missile sites, final device progress, world-end timer |

### Industry and logistics lane

The Kruger state should not run on ordinary economy alone. It should turn laboratories into factories and factories into laboratories.

Focus groups:

- Convert laboratories into production cells.
- Build automated rail sorting.
- Create specimen feeding and containment chains.
- Expand synthetic materials.
- Mine or synthesize rare materials.
- Capture foreign research centers.
- Move capital functions into sealed underground facilities.

Rewards should include factories, infrastructure, railways, supply hubs, resources, production lines, and decision unlocks. Avoid repeated small production modifiers.

### Expansion and conquest lane

Kruger’s expansion should be direct after Evolution IV.

Focus groups:

| Focus group | Role |
| --- | --- |
| Subdue the former host | First strategic target and revenge war |
| Absorb national laboratories | Gain bonuses from defeated host research |
| Demand research submission | Ultimatums to neighbors with universities or reactors |
| Seize reactor states | Claims or war goals on nuclear infrastructure |
| Harvest great capitals | Major-power war planning and special rewards |
| International laboratory zones | Occupation and collaboration decisions |
| World as experiment | Late conquest doctrine and world-threat escalation |

Expansion should create diplomatic reactions, resistance risks, and foreign coalitions. War goals should not be spammed without route locks and staged targets.

### Final device lane

This branch unlocks only after Evolution IV and meaningful project prerequisites.

Stages:

1. Theoretical unification of nuclear, temporal, and xenotechnology projects.
2. Construction of a sealed reactor or impossible test range.
3. Collection of components from conquered capitals, reactor states, alien sites, or special-project centers.
4. A long research mission that enemies can interrupt.
5. Final arming stage that becomes more likely if Kruger is close to capitulation or already committed to world conquest.

The final device should not be an instant focus reward. It should be a visible campaign race.

## Kruger focus tree AI

AI Kruger should prioritize survival, host defeat, and project specialization based on the assets he already has. A clone-heavy Kruger should use clone lane first. A robot-heavy Kruger should use machine administration and robot cohorts first. A low-asset Kruger should stabilize before attacking majors.

High-chaos Kruger can rush dangerous branches. Ordinary AI should still understand that it must defend its capital and supply first.

## Route coverage acceptance

Implementation should provide a route coverage table with these rows:

| Required route | Implemented branch | Required status |
| --- | --- | --- |
| Host public science | Additive host branch or decision equivalent | Required |
| Host military science | Additive host branch or decision equivalent | Required |
| Host security and containment | Branch or decision equivalent | Required |
| Host sealed projects | Branch or decision equivalent | Required |
| Kruger opening survival | Focus branch | Required if KRG can spawn |
| Kruger internal control | Focus branch | Required if KRG can spawn |
| Clone army | Conditional focus branch | Required if clone project exists |
| Robot army | Conditional focus branch | Required if robot project exists |
| Specimen army | Conditional focus branch | Required if monster or dinosaur project exists |
| Xenotechnology army | Conditional focus branch | Required if alien project exists |
| Temporal army | Conditional focus branch | Required if time project exists |
| Expansion and world conquest | Focus branch | Required for Evolution IV |
| Final device | Focus branch and mission race | Required for world-end path |
