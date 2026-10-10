# Event 027: Doctrine-domain registry matrix

## Purpose

The registry lets Event 027 serve vanilla domains, DLC domains, Chaos Warfare, and future custom doctrine families without hardcoding choices into the firing.
This file owns the adapter contract.
The implemented adapters live in `common/scripted_triggers/027_doctrine_research_triggers.txt` and `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`, and the overview's Domains section describes them.

## Principles

- A domain enters the pool only when its adapter can answer every question a safe choice needs.
- Adapters fail closed: a broken custom domain hides itself and never removes a valid ordinary domain.
- The registry keeps native order and identity, and never renames, merges, or flattens tracks.
- Queries run at country scope during a firing or a choice, never as a recurring world scan.
- No unknown subdoctrine identity ever reaches a mastery trigger or effect, because a bad identity in `has_mastery_level` has crashed the game before (official 1.17.1 patch notes).

## Adapter contract

| Field | Required answer |
| --- | --- |
| Domain identity | A stable ID distinct from display text, and its native folder. |
| Display | Localised domain name and a verified doctrine-owned icon. |
| Eligibility | DLC, origin, route, and owner-system conditions for the current country. |
| Grand Doctrine state | Whether the folder has an active Grand Doctrine and which one. |
| Adoption pool and action | Every adoptable Grand Doctrine and a native or owner action that adopts exactly one without replacing anything. |
| Tracks | Every track identity and index in native order, with name and icon. |
| Selected subdoctrine | The held branch per track, or empty. |
| Empty-track pool and action | Every assignable subdoctrine and an action that assigns one without replacing a branch. |
| Levels | Current level after banked mastery resolves, and the exact maximum per branch. |
| One-step advancement | An action that grants exactly one event-attributed level. |
| Completion | Branch completion and the track's native Milestone state. |
| Banked mastery | How the bank resolves on assignment and completion. |
| AI factors | Domain, Grand Doctrine, track, and subdoctrine factors drawn from visible force structure, identity, route, threats, or owner-system state. |
| Cleanup | How stale owner-system state is removed and how invalid state is reported. |
| Documentation owner | The document that explains the doctrine family. |

## Domain matrix

| Domain | Native folder | Tracks | Status |
| --- | --- | --- | --- |
| Army | `land` | Infantry, Combat Support, Armor, Operations | Implemented; available while the folder holds no Chaos Warfare. |
| Navy | `naval` | Submarines, Screens, Carriers, Capital Ships | Implemented. |
| Air | `air` | Fighter, Strike, Medium, Heavy Aircraft | Implemented. |
| Special Forces | `special_forces` | First and Second Special Forces | Implemented behind the installed DLC and technology gates; see below. |
| Chaos Warfare | `land` | The four Army tracks, one Chaos Warfare subdoctrine each | Implemented behind the CBRN establishment gate; see below. |
| Future custom | owner-defined | owner-defined | Disabled until a complete adapter is registered. |

Army and Chaos Warfare share the `land` folder, so folder-owned emptiness checks name each domain's own subdoctrine identities and keep an Army Infantry row and a Chaos Warfare Infantry row apart.

### Mastery step mechanism

Every supported branch advances through the native `add_mastery` route, one point at a time, re-reading the level until it reaches exactly the next level.
The guard stops at the level's reward cost, scaled for negative mastery gain factors, and an unresolved readback ends the step as ambiguous without spending a choice.
The 125 `<doctrine>_mastery_gain_factor` names read through `modifier@` are pre-registered in `common/synchronized_dynamic_tokens/027_doctrine_research_tokens.txt`; a new `modifier@` read adds its name there.
Same-effect readback after `add_mastery` and the gain-factor behaviour are live checks.

### Special Forces

Each of the eight Special Forces subdoctrines can occupy either native track and is mutually exclusive with its sibling, while native mastery is read per subdoctrine.
The adapter therefore grants and reads Special Forces mastery by folder and subdoctrine, keeps the selected track label on the receipt, and excludes an empty-track candidate whose sibling already holds a track.
While both tracks are occupied, the first entry covers both held subdoctrines and the second entry stays hidden, so the domain stays available instead of disappearing.
A Special Forces entry reports the Milestone of the subdoctrine it shows, because completing a subdoctrine completes whichever track holds it.

### Chaos Warfare

Chaos Warfare is the `chaos_warfare` Grand Doctrine in the `land` folder, adoptable only while the folder is empty and `cbrn_chaos_warfare_adoption_capable` holds.
Its tracks keep their compatibility identities:

| Track | Subdoctrine | Compatibility ID |
| --- | --- | --- |
| Infantry | Hazard Assault Formations | `extermination_columns` |
| Armor | Toxic Armored Warfare | `chemical_suppression` |
| Combat Support | Contaminant Fire Support | `contaminant_firebases` |
| Operations | Integrated CBRN Command | `integrated_chemical_operations` |

Native mastery runs the reward effects in `common/doctrines/subdoctrines/land/chaos_warfare_*_subdoctrines.txt`, so the CBRN institutional flags, technology grants, operation gates, and officer-corps state update through the owner's own route.
Event 027 waives only the doctrine cost, never the establishment package, and never converts a level into a direct unit, operation, policy, or equipment unlock.
The CBRN system documentation is `docs/systems/cbrn_warfare/chaos_warfare_doctrine.md`.

## Registering a future custom domain

A system that adds a doctrine family registers it in this order:

1. Name the owner system, the stable domain ID, and the native folder.
2. Document the hierarchy and its player-facing purpose.
3. Provide every contract field above.
4. Prove the one-step action against the doctrine graph, including banked mastery.
5. Provide AI factors drawn from real state, never a bonus for the adapter merely existing.
6. Verify icons on the event pages.
7. Add DLC, route, and special-country gates, and an exception in `doctrine_research_country_has_doctrine_system` if the owner is a country the nonhuman classifier excludes.
8. Add cleanup and invalidation behaviour.
9. Add scenarios to the probability file and update this matrix and the overview.

A family that only adds branches to an existing folder extends that domain's adapter.
A new domain is justified only by a distinct high-level selection, track registry, mastery state, AI identity, and player-facing role.

## Valid actions

| Action | Valid when |
| --- | --- |
| Adoption | The domain is eligible, its folder has no active Grand Doctrine, the doctrine exists and passes DLC, country, and owner gates, and adoption replaces nothing. |
| Assigned-track step | The domain and Grand Doctrine are valid, the track holds a known subdoctrine below its maximum, and the step action is available. |
| Empty-track step | The domain and Grand Doctrine are valid, the track is empty, at least one subdoctrine can be assigned, and assignment plus one step is safe. |

## Outputs

Human pages need the localised name, icon, selected state, current, next, and maximum level, and completion and Milestone state, all read from the adapter rather than from English names or branch-number assumptions.
The AI needs domain, Grand Doctrine, track, and subdoctrine factors, completion and continuity values, and hard invalidation.
Achievements need stable identities for curriculum, domain, Grand Doctrine, track, subdoctrine, the step's pre- and post-level, and branch completion, so renamed text or icons never break records.
