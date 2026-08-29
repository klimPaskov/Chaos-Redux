# Event 027: Doctrine Research

## Part 2: Choice flow and country resolution

## Presentation model

The event uses a chained country-event flow. Each page has one clear purpose and shows only the options relevant to the current step.

The flow keeps the normal event interface because the player is making a small sequence of discrete selections. A custom mechanic window would repeat the doctrine screen, create a second doctrine interface, and make the event harder to maintain when vanilla or custom doctrine graphs change.

The player should always understand four facts:

- which country owns the batch
- how many choices remain
- which doctrine domain is being considered
- whether the next successful selection adopts a Grand Doctrine or advances one mastery level

The event must not expose raw adapter IDs, variables, track indexes, DLC checks, mastery-point totals, or hidden AI values.

## Opening report

A human country with at least one valid option receives an opening report for the current batch.

The report communicates:

- a worldwide military-learning wave has reached the country's staff system
- the total number of choices in this batch
- the number of choices still unused
- Grand Doctrine adoption consumes one choice without an event mastery step
- a mastery choice can be concentrated in one branch or distributed

The report's main continuation opens the doctrine-domain page. It does not consume a choice.

When the country has no valid option, the opening becomes a concise closure report. It explains that every available curriculum is complete, unavailable, or unsupported. The batch closes from that report without compensation.

An AI country does not receive the opening report. It begins silent resolution from the same valid-domain pool.

## Doctrine-domain page

The domain page lists every registered doctrine domain that can currently produce at least one successful action.

A domain appears when either condition is true:

- the domain has no Grand Doctrine and at least one Grand Doctrine can be adopted
- the domain has an active Grand Doctrine and at least one track can receive an event mastery step

The domain option displays a compact dynamic summary:

- domain name and icon
- active Grand Doctrine name, or a clear unselected state
- count of tracks that can still progress when a Grand Doctrine is active
- the result type for the next page, adoption or mastery development

Domains that are unavailable due to DLC, country rules, missing custom prerequisites, invalid adapters, or fully completed content are omitted. They are not shown as tempting disabled choices unless the player can take a clear action to satisfy the requirement from the current event. Event 027 itself provides no such preparatory action, so hidden invalid domains create the cleanest flow.

The domain page also provides a return route to the opening summary when useful. Returning does not consume a choice.

## Grand Doctrine selection page

This page opens only when the selected domain has no active Grand Doctrine.

It lists every Grand Doctrine that the country can currently adopt in that domain. Each option shows:

- Grand Doctrine name
- Grand Doctrine icon
- a short native or scripted summary of its intended military direction
- the selected doctrine domain
- a clear notice that this action consumes one Event 027 choice and grants no event mastery step

The page must not reveal every future subdoctrine reward. The normal doctrine interface remains the detailed reference.

The country can return to the domain page without consuming a choice.

When a Grand Doctrine becomes invalid before confirmation, the selection fails safely and returns to the rebuilt doctrine list. A choice is consumed only when adoption succeeds.

After adoption succeeds:

1. the event records one adoption action in the current batch ledger
2. the remaining choice count falls by one
3. the native Grand Doctrine effects resolve
4. achievement tracking updates
5. the batch either closes or begins the next choice

When another choice remains, the next choice rebuilds the domain page. The newly adopted domain can now offer its tracks.

## Track selection page

This page opens when the selected domain has an active Grand Doctrine.

It lists each track that can still produce a successful event mastery step. Each track option shows:

- track name and track icon when available
- current subdoctrine name, or an unselected state
- current mastery level
- next mastery level
- whether the track is one step from completion
- whether completion would unlock or restore a native Grand Doctrine Milestone

The Milestone note must remain factual and concise. It should use the native doctrine information when possible and avoid duplicating long effect lists.

A fully mastered track is omitted. An empty track with no eligible subdoctrine is omitted.

The country can return to the domain page without consuming a choice.

## Active-subdoctrine resolution

When the selected track already has an active subdoctrine, the next page confirms the branch that will receive the event mastery step.

The confirmation shows:

- domain
- Grand Doctrine
- track
- subdoctrine
- current mastery level
- next mastery level
- remaining choices before confirmation

The branch is revalidated when the country confirms.

A successful confirmation advances one event mastery step and consumes one choice.

A branch that became complete before confirmation returns the country to the rebuilt track page without consuming a choice. This can happen through combat mastery, faction sharing, a focus, a decision, a scripted effect, or another queued event.

## Empty-track subdoctrine page

When the selected track has no active subdoctrine, the event lists every subdoctrine that can currently be selected in that track.

Each option shows:

- subdoctrine name and icon
- the track it occupies
- a concise native or scripted role summary
- a clear notice that the event will select the branch and grant one event mastery step

The normal subdoctrine purchase cost is waived by the event. Other eligibility rules remain active.

The country can return to the track page without consuming a choice.

A successful selection performs the following transaction:

1. select the subdoctrine through the native or custom doctrine route
2. allow native banked mastery to resolve without interference
3. read the resulting current mastery level
4. apply one event mastery step when another level remains
5. record the branch as the target of the current Event 027 choice
6. consume one choice

If native banked mastery completes the branch during selection, the event records the branch adoption but must not consume the Event 027 choice as a mastery result. The flow returns to the valid-track page. The implementation must verify whether the engine treats subdoctrine adoption and banked mastery as one atomic operation. If a clean one-choice transaction cannot be proven, the exact behavior remains blocked until the local doctrine graph and effects provide a safe route.

## Choice completion page

After each successful choice, the event briefly confirms the visible result.

For Grand Doctrine adoption, the confirmation names the adopted doctrine and states that the current choice established the doctrine without an event mastery step.

For mastery development, the confirmation names the subdoctrine and the mastery level reached through the event.

The confirmation also shows the number of choices remaining.

When choices remain, the continuation begins a fresh domain selection. When no choices remain, it opens the batch summary.

The confirmation should be compact. It should not restate the full event premise after every choice.

## Batch summary

The final summary closes one batch for one human country.

It reports:

- total choices granted
- successful Grand Doctrine adoptions
- successful event mastery steps
- number of distinct domains developed
- number of distinct tracks developed
- whether all choices were concentrated in one branch
- whether a native Grand Doctrine Milestone was reached during the batch

The summary does not list hidden achievement conditions. It may use concise dynamic text to recognize concentration, broad development, or a doctrine newly established through the event.

After the summary closes, the next queued batch begins if one exists.

An AI country does not receive a summary popup. Its batch ledger remains available for achievement safety, debugging, and audit until cleanup.

## Flow map

```text
Event 027 global firing
  -> Snapshot valid countries
  -> Create one country batch for each participant
  -> Human opening report or silent AI start
      -> Rebuild valid doctrine domains
          -> No valid domain
              -> Close batch
          -> Select domain
              -> Domain lacks Grand Doctrine
                  -> Select eligible Grand Doctrine
                  -> Adopt doctrine
                  -> Consume one choice
              -> Domain has Grand Doctrine
                  -> Select eligible track
                      -> Track has active subdoctrine
                          -> Advance one mastery level
                          -> Consume one choice
                      -> Track is empty
                          -> Select eligible subdoctrine
                          -> Resolve banked mastery
                          -> Advance one event mastery step
                          -> Consume one choice
      -> Choices remain
          -> Rebuild valid doctrine domains
      -> No choices remain
          -> Human summary or silent AI cleanup
          -> Start next queued batch when present
```

## Rebuilding the option pool

The event rebuilds the valid option pool at every major step. It never trusts a domain, doctrine, track, or subdoctrine list created earlier in the chain.

The rebuild responds to:

- a Grand Doctrine selected by the previous Event 027 choice
- a mastery level reached by the previous choice
- a branch completed through combat or training
- faction doctrine sharing
- a focus or decision completed while the batch is open
- a DLC or ruleset difference loaded with the save
- a custom doctrine system changing its eligibility
- a country changing status or disappearing
- a track becoming fully mastered
- a doctrine adapter being removed or invalidated by cleanup

A rebuilt list that becomes empty closes the batch and discards only the choices that can no longer be spent.

## Ordering and pagination

The domain page uses a stable order:

1. Army
2. Navy
3. Air
4. supported Special Forces doctrine content
5. Chaos Warfare
6. other registered custom domains in registry order

A domain-specific page follows the order defined by its verified doctrine graph. The event should not alphabetize track rows when that would differ from the doctrine interface.

When one event page cannot present every valid Grand Doctrine or subdoctrine clearly, the flow uses pagination. Pagination preserves the doctrine graph order and adds previous and next navigation without consuming a choice.

The event must not shorten a valid pool by displaying only a random subset. The player should be able to reach every valid option.

## Human input integrity

Every human action must be scoped to the country that owns the batch.

The event must prevent these failures:

- one player's option changes another country
- a stale event target points to a prior country's doctrine
- a tag switch applies the choice to the newly selected tag
- two open pages consume the same remaining choice
- back navigation repeats a successful doctrine effect
- a confirmation page can be accepted twice
- a queued batch overwrites the active batch ledger

One successful transaction needs a one-time receipt. The receipt is cleared only after the remaining choice count and batch ledger have updated.

## AI resolution model

AI countries use the same stages as human countries without opening player-facing pages.

For each remaining choice, the AI:

1. rebuilds the valid domain pool
2. scores each domain
3. selects one valid domain from the bounded top pool
4. adopts a Grand Doctrine or selects a track according to the domain state
5. revalidates the final target
6. performs one successful transaction
7. reduces the remaining choice count
8. recalculates all scores before the next choice

The AI never receives a different reward table. It does not gain extra mastery because it resolves silently.

When the AI has no valid option, it closes the batch without compensation.

## Country with no selected doctrine anywhere

A country with no active Grand Doctrine in any valid domain can use its baseline choice to adopt one Grand Doctrine in one chosen domain.

At Evolution I or higher, later choices in the same batch can develop the newly established doctrine.

The AI should usually prioritize Army doctrine for a landlocked country with a field army, Navy doctrine for an island or maritime country whose strategic plan depends on naval control, and Air doctrine for a country whose force structure and production make air power central. This is an AI tendency, not a hard rule.

## Country with mixed domain state

A country may have an active Army Grand Doctrine, no Navy Grand Doctrine, and a partially mastered Air branch.

Its domain page can offer:

- Army mastery development
- Navy Grand Doctrine adoption
- Air mastery development

The player decides among them. The existence of one active doctrine does not block adoption in another domain.

## Country with a complete domain

A domain whose active Grand Doctrine has no track able to receive an event mastery step is omitted from the domain page.

Completion in Army does not block Navy, Air, Special Forces, Chaos Warfare, or another valid domain.

A country with every registered domain complete closes its batch without a substitute reward.

## Country without a navy or air force

The event does not require a current fleet or air wing for a human country to choose Navy or Air doctrine when the native doctrine system allows that choice.

AI scoring treats an absent fleet, absent coastline, absent air production, or absent air force as strong evidence against that domain. It may still adopt the domain when the country's strategic plan, future focus route, island geography, faction role, or custom AI strategy makes the investment coherent.

The event should not create a new hard availability gate that the native doctrine system does not use.

## DLC and ruleset handling

The event builds its pool from content available in the current game setup.

A doctrine, track, or subdoctrine requiring an unavailable DLC is absent from the pool. The event does not expose a broken option, imitate the DLC content, or substitute another reward.

A DLC that changes doctrine topology must be inspected in the local graph. The adapter should identify the exact Grand Doctrines, tracks, subdoctrines, mastery levels, icons, and AI hooks available with that DLC combination.

Special Forces doctrine content remains registry-conditional. It participates only when the installed graph proves that it uses a compatible mastery-based selection and advancement model.

## Custom doctrine handling

Every custom doctrine family needs an explicit adapter. Event 027 never discovers a custom doctrine from a text name alone.

The adapter must establish:

- country eligibility
- domain display name and icon
- active Grand Doctrine test
- eligible Grand Doctrine pool
- active doctrine identity
- track order
- selected subdoctrine per track
- eligible subdoctrine pool for empty tracks
- current mastery level
- maximum mastery level
- safe one-level advancement
- completion and Milestone behavior
- AI domain and branch factors
- DLC or feature ownership gates
- cleanup and invalidation behavior

A missing field blocks that custom domain from Event 027. Other valid domains remain available.

## Chaos Warfare choice behavior

Chaos Warfare appears only for a country that can validly use the Chaos Warfare doctrine system.

When the Grand Doctrine is not active, the domain may offer Chaos Warfare establishment only when every establishment prerequisite required by the owning system is satisfied.

When active, the event can offer its four tracks in their established order. It advances the owning mastery state. It does not directly grant downstream units, policies, operations, ideas, or modifiers.

A track whose next mastery reward still requires a separate technology, formation, equipment, readiness, or policy gate can receive the mastery level. The downstream content remains blocked until its separate gate is satisfied. Event 027 should make this relationship clear through the native or custom doctrine tooltip, without listing hidden implementation variables.

## Native banked mastery sequence cases

| Starting state | Event action | Required result |
| --- | --- | --- |
| Active subdoctrine below the next threshold | Advance current branch | One event mastery step, one choice consumed. |
| Active subdoctrine completes from combat before confirmation | Rebuild track pool | No choice consumed. |
| Empty track with no banked mastery | Select branch | Branch selected, Mastery I granted, one choice consumed. |
| Empty track with partial banked mastery below Mastery I | Select branch | Native bank remains, one event mastery step is added, one choice consumed. |
| Empty track with enough banked mastery for one or more levels | Select branch and resolve native bank | Preserve native levels, then add one event mastery step if another level remains. |
| Empty track whose native bank completes the branch | Select branch | Preserve native completion, return to valid targets, do not consume the Event 027 mastery choice unless the engine exposes a safe combined transaction approved during implementation. |
| Fully mastered branch | None | Branch absent from pool. |

## Queue edge cases

| Situation | Required behavior |
| --- | --- |
| Event fires again during an active human batch | Append a separate batch with its own size and stage. |
| Evolution unlocks during an active batch | Current batch size stays fixed. Later firing uses the evolved size. |
| Country is annexed with two queued batches | Discard active and queued batches. Do not transfer them. |
| Country becomes a subject | Preserve its batches. |
| Country becomes independent | Preserve its batches. |
| Country changes cosmetic tag | Preserve its batches and dynamic country name. |
| Civil war creates a new tag | Original scope keeps its batch when valid. New tag gets no retroactive batch. |
| Human leaves a country through tag switch | Preserve the country batch. Route later resolution to its current controller. |
| AI country becomes human-controlled | Open the next unresolved choice for the human. |
| Human country becomes AI-controlled | AI resolves the remaining batch through the bounded continuation path. |
| Save occurs between doctrine effect and choice decrement | One-time transaction receipt prevents a duplicate effect after reload. |
| Queued batch starts after all doctrines become complete | Close it without compensation. |

## Invalid adapter cases

| Adapter problem | Event behavior |
| --- | --- |
| Domain reports an active Grand Doctrine but cannot identify it | Hide the domain and record a debug or audit failure. |
| Track count and track identities disagree | Hide the affected domain. |
| Selected subdoctrine cannot be resolved | Hide the affected track. |
| Maximum mastery level is unknown | Hide the affected branch. |
| One-level advancement cannot be proven | Block the affected domain from normal release. |
| Icon is missing but gameplay identity is valid | Use the verified domain or doctrine fallback icon only when the owning doctrine interface already uses that fallback. Record the missing asset as an implementation finding. |
| Custom domain cleanup leaves stale state | Hide the domain until the owning system reestablishes a valid adapter state. |

## Player-facing clarity requirements

Every option needs a clear result type.

Grand Doctrine options must say that they establish the doctrine and use one choice without an event mastery step.

Mastery options must name the track, subdoctrine, current level, and next level.

Back and pagination options must read as navigation. They must not look like doctrine choices.

A blocked result must explain the visible reason when the reason is useful to the player. Internal adapter failures belong in debug and audit evidence, not in normal player text.

The player should never have to infer whether a click will consume a choice.
