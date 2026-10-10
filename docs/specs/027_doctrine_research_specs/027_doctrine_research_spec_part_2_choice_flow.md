# Event 027: Doctrine Research

## Part 2: Choice flow

## Presentation model

The event uses chained country events because the player makes a short sequence of discrete selections.
A custom window would duplicate the native doctrine screen and break whenever vanilla or custom doctrine graphs change.

At every step the player must be able to see which country owns the curriculum, how many choices remain, which domain is being considered, and whether the next click establishes a Grand Doctrine or advances a mastery level.
Pages never show adapter IDs, variables, track indexes, DLC checks, mastery points, or AI scores.

## Implemented page flow

| Page | Purpose |
| --- | --- |
| `.2` | Opening report with the curriculum size and one continue option. |
| `.3` | Domain menu: Army, Navy, Air, Special Forces, Chaos Warfare in that order, showing only domains with a valid action. |
| `.4` | Grand Doctrine menu for a domain whose folder is empty. |
| `.5` | Track menu for a domain with an active Grand Doctrine, showing only tracks that can advance. |
| `.6` | Hidden router to the track's subdoctrine page. |
| `.60` to `.77` | One page per track listing the held subdoctrine, or every eligible subdoctrine for an empty track in native graph order, with two-page navigation for the longest lists. |
| `.7` | Confirmation with its own text for adoption, an assigned-track step, and an empty-track assignment. |
| `.8` | Result of the action. |
| `.9` | Continue to the next choice. |
| `.10` | Curriculum summary. |
| `.11` | No valid action remains, or the target became invalid. |
| `.12` | An interrupted transaction was recovered. |
| `.13` | Stored mastery completed the branch as it was assigned, so no choice was spent. |

Every page shows the remaining choices.
Back, previous, and next options are worded as navigation and never spend a choice.
The domain menu, the selected-domain check, and the confirmation all re-read validity, so a page left open while the country's state changed cannot confirm an invalid action.

### Click cost of the implemented flow

One mastery step on a track that already holds a subdoctrine takes six clicks: domain, track, the one-option subdoctrine page, confirmation, result, and continue.
A five-choice Evolution IV curriculum therefore needs about thirty clicks, and a country with a queued second curriculum doubles that.
The subdoctrine page and the confirmation repeat information the track option already shows, and the result and continue pages carry no decision.
Revisions R1 to R5 below remove those clicks without removing any decision.

## Proposed flow revisions (2026-10-10 audit, pending)

These revisions are proposals from the 2026-10-10 audit.
They change accepted implemented behaviour, so they stay unresolved until the user accepts them (README open questions).
None of them changes what a choice can do, the validity rules, or the transaction receipts.

### R1. The opening report becomes the first domain menu

The `.2` page carries the curriculum premise and size and lists the domain options directly, so the first choice starts on the page that announces the curriculum.
Later choices use the plain domain menu.

### R2. An assigned track advances from the track menu

A track whose subdoctrine is already selected advances when the player clicks it in the track menu.
The option's own trigger and the transaction revalidate the target, and a failed step returns to the rebuilt track menu without spending the choice.
The one-option subdoctrine page and the confirmation are skipped for this case.
The combined Special Forces entry that covers two held subdoctrines keeps its subdoctrine page, because the player still has to pick one.
Adoption and empty-track assignment keep their confirmation, because both are permanent commitments the event cannot undo.

### R3. The result page continues the curriculum

The result page offers the next action directly instead of a separate continue page:

- advance the same branch again, when it can still advance, labelled with its next level
- choose another domain
- let the general staff assign the remaining choices (R5)

After the last choice, the result page shows the summary (part 4, R6) and closes the curriculum, so `.9` and `.10` merge into it.
Stacking one branch through a five-choice curriculum then costs one click per choice after the first.

### R4. Chaos Warfare adoption states its cost

The confirmation for establishing Chaos Warfare adds one sentence that civilian deaths rise in every war the country fights while it follows Chaos Warfare, and that chemical release still needs the CBRN programme's policy, payloads, and prepared operations.
This is the doctrine's real downstream cost through the Chaos Meter combat collateral model and the Deaths ledger, and the free adoption should not hide it.
The native Grand Doctrine description already covers the programme gates, so the confirmation can reuse it.

### R5. The general staff can take the remaining choices

The domain menu and the result page offer "let the general staff assign the remaining choices" as their first option.
It runs the AI resolver for the remaining choices of the current curriculum only, using the same validity pool and scoring as an AI country, then shows the summary.
Queued curricula still open normally afterwards.

Placing it first also fixes unattended pages.
The engine resolves an unanswered event after `EVENT_TIMEOUT_DEFAULT` (13 days in vanilla `00_defines.lua`) by picking an option, which for a human is expected to be the first one (live check).
In the implemented flow that cascades through the first listed domain, track, and confirmation and spends choices on whatever happens to be listed first, normally Army Infantry.
With R5 first, an unanswered curriculum is spent the way an AI country would spend it.
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
  -> human: domain menu (opening text on the first choice, R1) | AI: silent resolution
      -> general staff option (R5) -> AI resolver for the remaining choices -> summary
      -> domain without a Grand Doctrine -> Grand Doctrine page -> confirm -> adopt, spend one choice
      -> domain with a Grand Doctrine -> track page
          -> assigned track -> advance one level, spend one choice (R2)
          -> empty track -> subdoctrine page -> confirm -> assign and advance, spend one choice
              -> bank completes the branch -> assignment stands, no choice spent
      -> result page (R3)
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
