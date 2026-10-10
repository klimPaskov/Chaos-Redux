# Event 027: Doctrine Research

## Part 2: Choice flow

## Presentation model

The event uses chained country events because the player makes a short sequence of discrete selections.
A custom window would duplicate the native doctrine screen and break whenever vanilla or custom doctrine graphs change.

At every step the player must be able to see which country owns the curriculum, how many choices remain, which domain is being considered, and whether the next click establishes a Grand Doctrine or advances a mastery level.
Pages never show adapter IDs, variables, track indexes, DLC checks, mastery points, or AI scores.

## Page flow

| Page | Purpose |
| --- | --- |
| `.3` | Domain menu: the general staff option first, then Army, Navy, Air, Special Forces, Chaos Warfare in that order, showing only domains with a valid action. The first choice of a curriculum opens here with the premise and size. |
| `.4` | Grand Doctrine menu for a domain whose folder is empty. |
| `.5` | Track menu for a domain with an active Grand Doctrine, showing only tracks that can advance. |
| `.6` | Hidden router: advances an assigned track directly, otherwise opens the track's subdoctrine page. |
| `.60` to `.77` | One page per track listing the held subdoctrine, or every eligible subdoctrine for an empty track in native graph order, with two-page navigation for the longest lists. |
| `.7` | Confirmation for adoption and empty-track assignment. |
| `.8` | Result of the action with the next step: general staff, the same branch again, another track of the domain, another domain, or the closing outcome after the last choice. |
| `.10` | Curriculum summary after the general staff finished a curriculum. |
| `.11` | No valid action remains, or the target became invalid. |
| `.12` | An interrupted transaction was recovered. |
| `.13` | Stored mastery completed the branch as it was assigned, so no choice was spent. |

Every page shows the remaining choices.
Back, previous, and next options are worded as navigation and never spend a choice.
The domain menu, the selected-domain check, and the confirmation all re-read validity, so a page left open while the country's state changed cannot confirm an invalid action.

### Click cost

One mastery step on an assigned track takes two clicks: domain and track.
Stacking the same branch costs one click per further choice through the result page, and the general staff option spends every remaining choice with one click.
Adoption and empty-track assignment keep their confirmation because both are permanent commitments the event cannot undo.

### Direct advance and result page

A track whose subdoctrine is already selected advances when the player clicks it in the track menu.
The transaction revalidates the target, and a failed step goes to the no-action page without spending the choice.
Special Forces entries keep their subdoctrine page, because one entry can show a token from either native track.

The result page offers the next action directly and closes the curriculum after the last choice with its outcome (Grand Doctrines established, mastery levels advanced, any Milestone reached).

### Chaos Warfare adoption

The confirmation for establishing Chaos Warfare states that civilian deaths rise in every war the country fights while it follows Chaos Warfare, and that chemical release still needs the CBRN programme's policy, payloads, and prepared operations.
This is the doctrine's real downstream cost through the Chaos Meter combat collateral model and the Deaths ledger.

### General staff

The domain menu and the result page offer "let the general staff assign the remaining choices" as their first option.
It runs the AI resolver for the remaining choices of the current curriculum only, using the same validity pool and scoring as an AI country, then shows the summary.
Queued curricula open normally afterwards.
Delegated steps are the country's own receipts and count for achievements like any other step.

## Grand Doctrine page

Lists every Grand Doctrine the country can adopt in the selected domain, with its native icon and name.
Each option states that it establishes the doctrine, spends one choice, and grants no mastery step.
The page never previews future subdoctrine rewards, because the native doctrine screen is the reference for that.
If the doctrine became invalid before confirmation, the flow returns to the rebuilt list without spending a choice.

## Track page

Lists each track that can still advance, in native graph order.
A track shows its held subdoctrine and level change, or that it is empty and will be assigned and advanced.
Fully mastered tracks and empty tracks without an eligible subdoctrine are omitted.

## Empty-track assignment

The track's page lists every subdoctrine that can be selected, with its native icon, and states that the event selects the branch and grants its first mastery step.
A successful assignment runs one transaction:

1. select the subdoctrine through the native route (`set_sub_doctrine` with folder and track index)
2. let banked mastery resolve without interference
3. read the resulting level and record it as the step's starting level
4. add one mastery step when a level remains
5. spend one choice

If banked mastery completes the branch on assignment, the assignment stands, no choice is spent, and `.13` explains it.
The assignment and the readback after it are a live check.

## Special Forces

Each Special Forces subdoctrine can occupy either of the two native tracks and is mutually exclusive with its sibling, while native mastery is read per subdoctrine.
Special Forces steps are therefore granted and read by folder and subdoctrine.
While both tracks are occupied, the first Special Forces entry covers the held subdoctrines of both tracks and the second entry stays hidden.
Empty-track candidates exclude a subdoctrine whose sibling already holds a track.
All of this is implemented; two tracks never holding the same subdoctrine is a live check.

## Rebuilding the option pool

The pool is rebuilt at every major step and never trusts a list built earlier in the chain.
It responds to the previous Event 027 choice, combat or training mastery, faction sharing, focuses and decisions completed while the page was open, DLC state, owner-system eligibility, branch completion, and the country becoming nonhuman.
An empty rebuilt pool closes the curriculum and discards only the choices that can no longer be spent, without compensation.

## Pagination

Pages follow native graph order and never alphabetise or randomise.
A list too long for one page uses previous and next options, and every valid option stays reachable.

## Human input integrity

Every action is scoped to the country that owns the curriculum.
The receipt design prevents one player's option from changing another country, a stale target from pointing at another country's doctrine, a tag switch from redirecting a choice, two open pages from spending the same choice, back navigation from repeating an effect, a confirmation from applying twice, and a queued curriculum from overwriting the active one.

## AI resolution

AI countries use the same validity triggers without opening pages.
For each remaining choice the AI rebuilds the domain pool, scores the domains, picks one through a weighted random list, adopts a Grand Doctrine or picks a track and subdoctrine the same way, revalidates, runs one transaction, and rescores before the next choice.
The AI never receives a different reward and closes its curriculum without compensation when nothing is valid.
Part 3 owns the scoring model.

## Flow map

```text
Event 027 firing
  -> one curriculum appended for every participant
  -> human: domain menu (opening text on the first choice) | AI: silent resolution
      -> general staff option -> AI resolver for the remaining choices -> summary
      -> domain without a Grand Doctrine -> Grand Doctrine page -> confirm -> adopt, spend one choice
      -> domain with a Grand Doctrine -> track page
          -> assigned track -> advance one level, spend one choice
          -> empty track -> subdoctrine page -> confirm -> assign and advance, spend one choice
              -> bank completes the branch -> assignment stands, no choice spent
      -> result page
          -> choices remain -> same branch again | another domain | general staff
          -> no choices remain -> summary, next queued curriculum starts
```

## Edge cases

| Situation | Required behaviour |
| --- | --- |
| Target completed by combat or sharing before the click | Rebuild the page, spend nothing. |
| Empty track with partial bank below level 1 | Bank stays, one step added, one choice spent. |
| Empty track whose bank reaches one or more levels | Native levels stay, one further step added if a level remains. |
| Empty track whose bank completes the branch | Assignment stands, no choice spent, `.13` shown. |
| Event fires again during an active curriculum | Append a separate curriculum with its own size and stage. |
| Evolution unlocks mid-curriculum | Current size stays, later firings use the new stage. |
| Country annexed with queued curricula | Discard all of them, transfer nothing. |
| Country becomes a subject, becomes independent, or changes cosmetic tag | Keep its curricula. |
| Civil war creates a new tag | Original country keeps its curriculum, the new tag waits. |
| Human becomes AI | AI resolves the remaining choices. |
| AI becomes human | Next unresolved choice opens for the human once. |
| Save between the doctrine effect and the choice decrement | Receipt recovery prevents a duplicate effect. |
| Country becomes nonhuman while holding a curriculum | Close it through the no-action path, no compensation. |
| Queued curriculum starts after everything is complete | Close it without compensation. |
