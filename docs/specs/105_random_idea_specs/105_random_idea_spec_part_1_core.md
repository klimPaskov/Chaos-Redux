# 105 Random Idea

## The event

Every existing country receives an independently drawn national idea from the content loaded into the campaign.
An idea can strengthen the country, damage it, do both, or have almost no practical effect there.
A foreign political movement, a highly specific institutional spirit, an obscure penalty, and an empty hidden spirit all remain possible when they are technically addable national ideas.
The event creates surprise through the breadth of that pool and the combinations countries retain.

| Catalog field | Design value |
| --- | --- |
| Event ID | 105 |
| Name | Random Idea |
| Type | Minor Repeatable |
| Requested status | To Be Reworked |
| Required Chaos level | 1, the player-facing starting level |
| Cluster | Randomizations |
| Cluster member severity | Medium |

These values preserve the current user brief.
The supplied catalog and inspected repository contain older identities, so the technical handoff records the exact reconciliation needed before implementation.
Medium describes this member's severity within the cluster.
It must not be mistaken for the framework's separate required, optional, or randomized participation-role field.

## What the player experiences

The firing resolves automatically for the world.
The player sees their own country's draw and then finds surviving visible ideas in the usual national-spirit display.
The report gives public selected ideas' native identities, preserves hidden presentation, and distinguishes a completed assignment from the ideas still present after their own immediate behavior.
It does not claim that every draw adds a lasting visible icon.

The report's acknowledgement closes the report.
All countries have already received their draws, including countries controlled by AI and human countries whose reports have not been acknowledged.
A country's ideology, faction, size, strength, research, national focus path, and relation to the country that scheduled the event do not change its share in the draw.

The world does not receive one common result.
Two countries may independently draw the same idea, but this is a coincidence produced by separate draws.
No country reserves an idea against use by another country.
An idea remains available internationally after another recipient draws it.

There is no balancing pass that gives weak countries better spirits or compensates a country for receiving a penalty.
The player responds through ordinary campaign decisions such as production, research, diplomacy, political appointments, and war.
Event 105 does not supply a reroll, trade, selection menu, removal service, or separate resource.

## Countries included

A recipient is an existing engine-valid country with a usable national-idea container when the firing's recipient roster is captured.
Include human and AI countries, subjects, countries at peace or war, ordinary and unusual playable tags, and existing capitulated or exile countries when that engine scope remains valid.
The event does not require a minimum population, factory count, army, territory count, or conventional human-country classification.

An uncreated tag, a destroyed country that is no longer an existing country scope, a missing target, and an internal data scope that cannot receive national ideas are outside the recipient roster.
An unusual tag is not excluded merely because a shared classifier describes it as special or nonhuman.
Even an internal test country belongs to the technical recipient set if it actually exists as a valid country with that container in the running test environment.
Test execution is distinguished from achievement-eligible play through the existing debug context, rather than an invented country blacklist.

Capture the roster before the first grant.
Recheck that each recipient still exists immediately before its first dispatch and after a callback that may destroy or replace its country scope.
If a selected idea creates a new country during resolution, that new country waits for a later firing because it was absent from the captured roster.
If a country disappears before its turn, leave a skipped-country result for that firing and continue with the surviving roster.

## The complete loaded pool

The universe is the set of distinct idea definitions actually loaded by the engine that it can apply as national ideas.
The pool includes all qualifying definitions from vanilla, enabled game content, Chaos Redux, and other active mods.
It also includes ideas that are normally obtained only through a particular country, ideology, focus branch, event chain, DLC interface, or specialist mechanic.

The implementation must establish the effective loaded definition before classifying an identity.
An overwritten definition contributes only its effective loaded version.
Multiple source-file mentions of one effective identity give it one share in the draw.
Different identifiers with identical names, artwork, modifiers, or flavour remain different ideas and each receives one share.

| Definition or condition | Treatment |
| --- | --- |
| An ordinary national spirit under the effective national-idea category | Include |
| A hidden national spirit | Include when technically addable |
| An empty national spirit or hidden carrier | Include when technically addable |
| A foreign-country, ideology, event, institution, or specialist-system spirit | Include |
| An idea whose ordinary selection interface says unavailable or whose usual country conditions are false | Keep eligible when direct native addition still accepts it |
| An idea whose modifiers depend on a mechanic the recipient lacks | Include |
| An idea with no useful modifiers, no meaningful local effect, missing artwork, or an untranslated name | Include when technically addable |
| A national idea that removes or replaces itself through its own normal behavior | Include |
| A custom category introduced by another mod | Include every member proven to function as a national idea |
| A law, designer appointment, officer-corps slot, character advisor, or character-slot dummy that is not a national idea | Exclude because of actual engine type |
| A dynamic modifier, trait, technology, or other non-idea object | Exclude because it is a different engine object |
| A definition that is absent, replaced away, malformed, or demonstrably not addable as a national idea | Exclude with specific technical evidence |
| A confirmed reserved engine database object that cannot be added | Exclude only after the reserved-object rule is verified |

Names and prefixes never establish type.
An advisor-looking identifier can still be a national spirit if its effective loaded definition places it in that category.
Likewise, the word dummy does not establish technical invalidity.
No category of merely inconvenient, dangerous, negative, useless, unfamiliar, or mechanically dependent national ideas is permitted.

The pool is not assembled from ideas currently held by countries.
That method would omit never-used ideas, inactive event ideas, later-path content, and content from countries absent from the map.
The event also must not use a short Chaos Redux list, a list of well-behaved spirits, source-balanced themed buckets, or an opt-in registration bus as if any of those represented the whole loaded game.

## Discovery commitment

The preferred route is a supported engine mechanism that discovers the complete loaded national-idea set at runtime.
The technical research found no documented all-ideas array in the inspected offline reference, and current installed-engine documentation was unavailable.
Runtime enumeration therefore remains an implementation question to verify, rather than a capability this package claims already exists.

If the current engine does not expose complete discovery, use a generated registry representing the entire effective active loadout.
That registry must resolve game files, DLC mounts, enabled mods, overrides, custom idea categories, and duplicate identities before generating the selectable set.
A preparatory generator is an external compatibility step and must be described honestly as such.
Ordinary in-game startup cannot be assumed to scan arbitrary files or execute that generator.

The generated route is accepted as the next implementation route within the user's requested investigation order.
It preserves the same indiscriminate membership rules.
A smaller maintained list remains an unresolved fallback requiring an explicit later decision, and it is not an authorized substitute in this package.
The detailed evidence, remaining engine questions, loadout contract, and publication gate are in the technical research and handoff file.

## What one draw means

A draw selects one fresh exact identity and dispatches the native addition once.
Fresh means the country does not already hold that exact identity and it has not already been directly selected during the same firing.
The event does not reapply an already-held identity to refresh a timer, retrigger a callback, or inflate a result count.

Every eligible exact identity has the same probability at the moment of selection.
There are no rarity weights, source quotas, ideology weights, country preferences, family preferences, or modifier-strength weights.
Selecting a source file uniformly and then selecting an idea within that file would violate this rule when files contain different numbers of ideas.

Within a country's bundle, identities are drawn without replacement.
Across countries, each recipient draws from its own eligible set with independent random selections.
Across later firings, a previously drawn identity becomes eligible again if the country no longer holds it.
This permits the native lifecycle to matter while preventing ordinary duplicate accumulation.

An existing idea from the same upgrade family does not exclude a different identifier.
If the native engine replaces one family member with another, the replacement is an intended consequence of drawing that definition.
The event does not attempt to preserve mutually incompatible family members by cloning their modifiers or rewriting their definitions.

## Resolution of one firing

1. Establish that the complete pool and its identity bindings are ready, then create one firing identity through the event framework.
2. Capture current Chaos, the valid recipient roster, every recipient's existing Event 105 burden, and the effective stage selected from the current evolution settings before any idea grants from this firing.
3. Determine each recipient's requested count from that captured state and the enabled evolution stage.
4. For each recipient, form its fresh candidate set from the complete loaded universe and current ownership, then choose a fresh identity uniformly.
5. Immediately before native dispatch, recheck the selected identity's technical binding and current ownership, record its direct-dispatch receipt, and consume that draw exactly once.
6. Allow the selected idea's ordinary native addition, replacement, cancellation, and callbacks to resolve.
7. Continue with distinct unattempted identities until the requested number has been dispatched or the genuine remaining set is exhausted.
8. Settle the firing's retained results, Event 105 Chaos contribution, player report, and bounded history references once.

The whole loaded universe stays fixed during one firing.
Current ownership is rechecked between draws because an earlier idea's callbacks can add another idea that would otherwise be drawn next.
An identity that becomes owned before dispatch is skipped without consuming a draw because Event 105 has not acted on it.
An identity already dispatched by Event 105 remains unavailable for the rest of that bundle even if its own callback immediately removes it.

A proven technical failure before native dispatch can continue the search through the remaining complete set.
Once dispatch begins, immediate absence or an uncertain return must not cause a retry, replacement prize, or rollback.
The idea may already have run an effect, replaced itself, or changed another country.
Removing newly observed ideas as compensation would interfere with the selected definition's normal behavior.

The requested count describes direct draws, not guaranteed net growth in visible spirit icons.
At baseline, a country is assigned one random national idea.
If that idea normally disappears immediately, the event has still made its one intended native assignment, subject to the implementation proving that the assignment route is technically valid.
Diagnostics must distinguish dispatched identities, immediate retained identities, and uncertain execution.
They must not call an unverified dispatch engine-proven delivery.

## Exhaustion and small pools

If a recipient has fewer fresh ideas than its requested count, dispatch each available fresh identity at most once and stop.
The result reports that the available fresh set was exhausted.
It does not repeat existing spirits, clone ideas, clear the country's current ideas, or fill the missing slots with a different reward.

A one-idea pool gives that idea to every recipient that lacks it.
The equality of these results reflects the available content and does not violate independent selection.
A country that already holds every eligible identity receives zero fresh ideas until its ownership changes or the loaded content expands.

A ready, genuinely empty pool is distinct from a failed or incomplete discovery process.
An empty result is a valid technical outcome that can be reported.
An unknown, stale, partially parsed, or truncated pool must never be presented as complete.
Normal automatic selection should treat unresolved discovery as unavailable through the shared framework, and a forced diagnostic firing should return a precise technical reason without spending a false successful outcome.

## Persistence and country changes

Event 105 applies no duration of its own.
Closing the report, ending resolution, changing Chaos, disabling future Event 105 firings, or leaving the Randomizations cluster does not remove already granted ideas.
An idea retains its own modifiers, visibility, cancellation rules, callbacks, replacement behavior, and native inheritance rules.

The event never copies a selected idea into a permanent Chaos-specific clone.
It does not suppress the idea's own removal or rewrite a specialist system to keep the idea effective.
It also does not import the idea's original country setup, focus tree, characters, resources, or unlocks to make the result useful.

Annexation, release, civil war, tag changes, and national transformations follow normal engine ownership behavior.
Event 105 adds no automatic extra inheritance and no compensating grant to a successor.
Its private history follows only a proven country-continuity mapping, as specified in the technical handoff.
Ownership inherited through a native civil-war or release rule can exist without being counted as a direct Event 105 draw by the new country.

## Intended campaign variety

The same country can gradually assemble unrelated bonuses, weaknesses, political identities, and institutional effects.
Some combinations reinforce one another, some cancel each other's practical value, and others matter only when later campaign events activate a related system.
All of these are legitimate outcomes.

The event's visual and written presentation should make the unfamiliar combination intelligible without explaining it away.
Its design does not manufacture a story that every government selected a sensible reform.
The surprise is that the new national condition is real even when it has no reasonable connection to that country.

Continue with part 2 for evolutions, burden, Chaos feedback, and the connection to Rule.
