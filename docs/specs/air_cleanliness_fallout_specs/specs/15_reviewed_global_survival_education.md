# Reviewed global-survival education contract

## Ownership

The School in the Vent Room is a Fallout-owned country-level generation-change
chain. It opens only after First Safe Birth has left a durable memory and after
the country has crossed the first recovery window. The chain remains dormant
until the accepted numerical contract authorizes the human and hidden-AI review
lanes.

| Surface | Contract |
| --- | --- |
| Candidate | 289 |
| Transaction | 710015 |
| Route | 7115 |
| Event blocks | 289 through 295 |
| Event Log | History 9120 with fifteen payloads |
| Target | Country only, target type none and target value zero |
| Human envelope | Opening, one delayed result, and one delayed cohort callback |
| Hidden AI envelope | Opening, one delayed result, and one delayed cohort callback |
| Human visible budget | Opening cost three, result cost one, callback cost one |
| Hidden AI visible budget | Zero for every hidden row |
| Timing | Result after 28 days, callback after 210 days |
| Asset | `GFX_report_event_fallout_school_vent_room` |

## Eligibility and grading

The candidate requires the current Fallout country registry, durable survival
identity and resource rows, the First Safe Birth memory, at least one recorded
generation change, campaign day 360 through 899, Cohesion at least 35, Food at
least 25, Shelter at least 35, and one affordable curriculum. Candidate severity
is the generation count multiplied by ten and clamped to the scheduler score
range. Mechanic pressure is zero. Food supplies the state value and the
survival-resource pressure source. Air Winter phase is explicitly phase zero for
the survival-resource contract.

The delayed result freezes Cohesion, Food, Shelter, Recognition, generation
count, education, and exposure. Viability weights Cohesion 35, Food 25,
Shelter 25, and generation count 15. Each curriculum has its own success and
partial threshold. Failure is deterministic and has no random or MTTH branch.

## Branches and consequences

The human and hidden-AI lanes use the same four branches:

1. Technical curriculum spends Food, Power, and Scrap, then raises education
   and research capacity when the grid course succeeds.
2. Old-world history spends Food, Scrap, and Recognition, then raises memory
   and education while exposing unresolved borders when it fails.
3. Civic survival spends Food, Medicine, and Recognition, then raises Cohesion,
   manpower, and public duties when the roster succeeds.
4. Faith classroom spends Food, Medicine, and Recognition, then raises Cohesion
   and keeps a shared family calendar without replacing the country government.

Every branch has success, partial, and failure results. Results update Food,
Medicine, Power, Recognition, Cohesion, stability, war support, manpower,
education, exposure, curriculum memory, timed modifiers, and the Event Log.
Failure routes population loss through the shared Deaths contract at 0.12
percent of each owned state's population. The callback uses 0.06 percent on
failure and records a maintained or failed cohort memory.

## Cleanup and boundaries

The result and callback use the exact issued ticket wrappers. Callback cleanup
prepares the result cleanup only after its own ticket is released. Cleanup
retains durable curriculum and cohort memories while clearing registry, frozen
ledgers, branch, result, callback, and transient flags. It does not activate the
Fallout scheduler, host authority, save recovery, or multiplayer behavior.
