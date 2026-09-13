# International Chaos Weapons Program

## Program promise

The International Chaos Weapons Program is the late Event 036 system that allows convention participants to reproduce weapon prerequisites normally tied to separate Chaos Redux events.

It is a shared international research and investment program.

It is not an event-selection bypass, a free-weapon button, or a substitute source event.

The program opens only after Evolution III and successful ratification of the program charter.

## Repository-derived project registry

The implementation must inspect the live repository and enumerate every real weapon project that meets the provider contract.

The specification recognizes Zombie Weapon and Black Plague Weapon as examples supplied by the event concept.

Their exact project IDs, source events, prerequisite tokens, availability proofs, and grant effects must come from repository source.

Do not infer additional projects from names, localisation, unused assets, comments, or planned documents.

A project enters the pool only through an explicit provider registration owned by the source event or weapon system.

## Provider registration contract

Each registered row must provide:

| Field | Contract |
| --- | --- |
| Stable project ID | Unique Event 036 registry identity that remains stable across saves |
| Display token | Player-facing project name resolved through owner-approved localisation |
| Source owner | Exact source event or system that normally controls the weapon prerequisite |
| Weapon prerequisite | Exact prerequisite or research gate that Event 036 may open |
| Eligibility trigger | Read-only proof that the project is supported and currently unavailable through its normal route |
| Normal-availability trigger | Read-only proof that the legitimate source route has made the weapon available |
| Participant eligibility trigger | Country-scope proof that a ratifier can receive the research route |
| Grant adapter | Idempotent effect that opens only the registered prerequisite or research route |
| Contribution profile | Allowed contribution families and project-specific resource substitutions |
| Progress target factor | Project complexity factor applied to the shared normalized target |
| Cancellation callback | Owner effect that immediately cancels the active Event 036 project when normal availability occurs |
| Isolation proof | Owner assertions that the grant does not set source-event fired, crisis, evolution, threat, country, narrative, super-event, or terminal state |
| Cleanup adapter | Bounded cleanup for provider-specific temporary targets or pending contribution requests |

The registry can live in a neutral shared provider file if several source events register projects.

Event 036 owns selection, progress, participants, completion, cancellation, and program lifecycle.

The shared registry must not own Event 036 stage or evolution state.

## Project eligibility

A registered project is eligible only when all of these conditions are true:

- Evolution III is active and enabled
- the program charter is active
- the provider row is complete
- the prerequisite is still unavailable through the legitimate normal route
- the project has not already been completed by Event 036
- the project is not currently selected
- the provider supports at least one valid active signatory recipient
- the grant adapter and cancellation callback are available
- the source-isolation contract passes static inspection

A project whose owner cannot distinguish normal availability from Event 036 availability is blocked from registration.

A project whose grant effect fires or advances its source event is blocked from registration.

A project whose only implementation is a completed weapon grant is blocked unless the user later changes the accepted design.

## Equal project selection

The candidate pool is rebuilt from every currently eligible registered project.

Each candidate has exactly one entry and exactly equal probability.

No project receives additional weight from:

- AI strategy
- country ideology
- member technology
- war state
- contribution capacity
- source event popularity
- project power
- project age
- previous failed selection

If one candidate exists, it is selected.

If several candidates exist, selection uses a uniform random pick across the complete deduplicated candidate array.

If no candidate exists, the program becomes Dormant.

The selection effect records:

- membership generation
- candidate count
- selected project ID
- selection date
- provider source owner
- progress target
- project sequence number

The exact candidate pool must be inspectable in debug evidence, but it must not appear in player-facing text.

## Program lifecycle

The program uses these states:

1. Charter Inactive
2. Awaiting Eligible Project
3. Project Active
4. Project Paused for Quorum
5. Completing
6. Cancelled by Normal Availability
7. Completed
8. Dormant

Only one project can be Active, Paused, or Completing at a time.

A completed or cancelled project leaves a permanent project history receipt.

The system then rebuilds the pool and selects another eligible project after a 7 to 30 day administrative interval.

## Shared progress

The project uses one global progress value and one project-specific target.

The default normalized target is `1000` internal progress units.

A provider may apply a complexity factor between `0.75` and `1.50` through a registered script constant.

The player sees only a percentage and broad stage label:

- Organization
- Experimental Work
- Prototype Access
- Final Validation

Internal progress, contribution formulas, and country shares remain hidden except where an achievement or tooltip needs a concise contribution summary.

Progress cannot fall below zero or exceed the current target.

Every contribution transaction records its applied amount before the global total changes.

## Participants

A country becomes a project participant when it:

- is an active compatible program-charter ratifier
- passes the provider participant trigger
- completes at least one valid contribution
- has a current membership-generation receipt

A contribution made before withdrawal remains in the historical ledger.

The country receives the completion unlock only when it is again a valid active participant at completion.

Chemical Accession members cannot participate in a biological project unless the provider explicitly classifies the prerequisite as chemical or general.

Reservation members can participate in research and protection projects when their public policy permits the route.

Public opponents cannot contribute.

## Contribution families

The program exposes four primary contribution families.

Project providers may replace one resource with a more appropriate supported resource, but they may not create a fifth visible cost on one action.

### Dedicate Industrial Capacity

Public action: commit civilian construction and industrial administration for 90 days.

Default cost profile:

- one to three civilian factories according to economy size
- optional fuel or convoy requirement when the provider proves transport-intensive work

Default applied progress:

- small economy: `25` to `30`
- medium economy: `30` to `40`
- large economy: `40` to `55`

The contribution uses a 60-day country cooldown after the commitment ends.

### Assign Research Teams

Public action: divert scientists, laboratories, and research administration for 90 days.

Default cost profile:

- a temporary research-speed burden
- political power or a project-appropriate experience cost
- optional scientist or manpower commitment when a current owner system supports it

Default applied progress:

- weak research base: `20` to `30`
- capable research base: `30` to `45`
- advanced research base: `40` to `55`

The action does not consume or disable a research slot unless the live engine and existing project precedent support that behavior safely.

### Provide Specialist Equipment

Public action: transfer equipment required by the current provider profile.

Supported default resources include:

- support equipment
- motorized equipment
- trains
- convoys
- infantry equipment
- fuel
- provider-owned special equipment when a documented stockpile debit helper exists

The action uses one or two equipment types and never more than four total spendable costs.

Default applied progress is `20` to `50` according to cost and project relevance.

The transaction must use supported stockpile debit helpers and fail closed when the country cannot pay.

### Host a Research or Testing Facility

Public action: provide a valid facility, site, security perimeter, and technical staff for 120 days.

Default cost profile:

- one to three civilian factories or an owner-supported facility commitment
- manpower
- optional support equipment
- optional stability or public-trust risk as a consequence

Default applied progress is `35` to `60`.

The action requires a valid facility or state when the project owner needs one.

It cannot create a fake facility marker that the owner system never uses.

## Small-country participation

Small ratifiers must be able to make meaningful contributions.

Every valid paid contribution applies at least `20` internal progress units before the project reaches its final `5%`.

Large powers receive higher efficiency, but one contribution cannot apply more than `60` units before provider-specific bonuses.

No country can apply more than `12%` of the full project target inside one 90-day period.

This prevents a major power from completing the program alone in one action while preserving its ability to lead repeated investment.

## Contribution receipts

Each contribution records:

- project sequence
- project ID
- country
- contribution family
- exact costs paid
- start date
- completion date
- requested progress
- applied progress
- membership generation
- provider profile

The country receives a cumulative share variable for the active project and a lifetime contribution history for achievements.

A receipt cannot be applied twice after save and reload.

Cancelling a decision before its owner-defined commitment point applies no progress.

Once the contribution completes, its spent resources are not refunded by later project cancellation.

## Progress milestones

The program may issue follow-up reports at `25%`, `50%`, `75%`, and `100%`.

These are Event 036 subevents and do not enter the random event pool.

Milestones can unlock stronger contribution options or project-specific complication events only when the provider supplies them.

A milestone cannot grant the final prerequisite early.

Milestones add zero Chaos.

## Atomic completion transaction

When progress reaches the target:

1. Set the project state to Completing and hide new contribution decisions.
2. Rebuild the selected project’s normal-availability proof.
3. If normal availability is true, run cancellation instead of completion.
4. Revalidate the provider grant adapter and isolation proof.
5. Build the active participant recipient list from current membership and contribution receipts.
6. Call the provider grant adapter once for each valid recipient.
7. Verify that only the weapon prerequisite or research route was opened.
8. Mark the project completed through Event 036.
9. Record the completion history and one-time Chaos change.
10. Clear active progress, participant arrays, temporary targets, and contribution decisions.
11. Rebuild the eligible project pool after the administrative interval.

A recipient that already has the prerequisite receives no duplicate grant.

A recipient that became invalid is skipped with a recorded reason.

## Source-event isolation

Completion must not:

- mark the source event fired
- increase the source event fired count
- change the source event random weight or cap
- activate a source evolution
- create a source crisis state
- create a source country
- set a source world-threat flag
- call a source super-event
- begin a source terminal branch
- advance source narrative stages
- create source decisions that require the source incident
- make the source event appear in History

The provider grant adapter must be narrower than the source event’s normal reward effect.

If the repository has no narrow adapter, implementation must add an owner-owned prerequisite grant API before registering the project.

## Immediate cancellation on normal availability

Every provider owner must call the registered Event 036 cancellation callback in the same normal transaction that makes its weapon prerequisite available.

The callback checks whether the provider’s project is currently selected.

When it matches, cancellation happens immediately:

1. Freeze contributions.
2. Record the normal-availability proof and source owner.
3. Discard all shared progress.
4. Remove active project decisions and missions.
5. Preserve spent resources and historical contribution receipts.
6. Mark the project cancelled by normal availability.
7. Clear the active project state.
8. Rebuild the candidate pool.
9. Select another eligible project after the administrative interval.

No duplicate unlock is granted.

A 30-day bounded coordinator heartbeat rechecks normal availability as a fail-safe.

The heartbeat is not the primary cancellation route and does not scan every country.

## Dormancy and wake-up

The program becomes Dormant when the eligible pool is empty.

Dormancy preserves the charter, membership, completed-project history, and cancelled-project history.

The category explains that no registered unavailable project currently qualifies.

The program wakes when:

- a provider registers a new eligible project and calls the wake-up effect
- a previously unsupported provider becomes valid
- a membership or capability change creates a valid recipient set
- the bounded coordinator recheck finds a new candidate

The recheck interval while Dormant is 90 days.

## Quorum pause

If the program loses its charter capability quorum during an active project, progress pauses.

Contribution decisions disappear and a reconstruction mission can begin.

Progress is preserved during the pause.

If quorum returns, the project resumes.

If normal availability occurs during the pause, the project cancels immediately through the provider callback.

If the charter is repealed completely, the project is cancelled and progress is discarded.

## AI contribution behavior

AI evaluates contribution families from:

- project relevance
- industry
- research capacity
- stockpiles
- manpower
- current war pressure
- expected completion time
- current contribution share
- progress stage
- provider participant eligibility
- competing national needs

AI should avoid an industrial contribution when factory commitment would critically damage survival.

It should avoid an equipment contribution when the stockpile is below its own safety reserve.

It should contribute more near completion when it remains eligible for the unlock.

It should not contribute when it plans to withdraw before completion.

## Player-facing text direction

The project text should identify the selected weapon route only after selection.

It should describe scientific, industrial, and military collaboration without claiming that the source event occurred.

The cancellation report should state that the weapon became available through another route and the international program was abandoned.

The completion report should state that participants can begin the registered research or project route.

It must not say that the weapon itself was delivered or completed unless the provider prerequisite truly represents that result.
