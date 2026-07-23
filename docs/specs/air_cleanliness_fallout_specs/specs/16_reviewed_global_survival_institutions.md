# Reviewed global-survival institution contract

## Ownership

The Empty Ward is a Fallout-owned country-level Year 2 institution chain. It
follows a completed generation memory and a resolved Fever Dormitory memory.
The chain remains dormant until the accepted scheduler contract authorizes its
human and hidden-AI review lanes.

| Surface | Contract |
| --- | --- |
| Candidate | 296 |
| Transaction | 710016 |
| Route | 7116 |
| Event blocks | 296 through 302 |
| Event Log | History 9121 with fifteen payloads |
| Target | Country only, target type none and target value zero |
| Human envelope | Opening, one delayed result, and one delayed institution callback |
| Hidden AI envelope | Opening, one delayed result, and one delayed institution callback |
| Human visible budget | Opening cost three, result cost one, callback cost one |
| Hidden AI visible budget | Zero for every hidden row |
| Timing | Result after 35 days, callback after 240 days |
| Asset | `GFX_report_event_fallout_empty_ward` |

## Eligibility and grading

The candidate requires the current Fallout country registry, durable survival
identity and resource rows, the closed School in the Vent Room memory, one
Fever Dormitory outcome memory, campaign day 500 through 1199, Cohesion at
least 30, Medicine at least 15, Shelter at least 30, and one affordable ward
policy. Candidate severity is recorded civilian Deaths multiplied by 0.0004
and clamped to the scheduler score range. Mechanic pressure is zero. Medicine
supplies the state value and the survival-resource pressure source.

The delayed result freezes Medicine, Shelter, Cohesion, Recognition, generation
count, ward capacity, research, institutional trust, and the ward's durable
exposure ledger. Viability weights are
Cohesion 25, Medicine 35, Shelter 25, and generation count 15. Each policy has
its own success and partial threshold. Failure is deterministic and has no
random or MTTH branch.

## Policies and consequences

1. Veteran home turns the ward into a staffed recovery institution and raises
   manpower, capacity, and trust when the roster holds.
2. Research clinic preserves fever records beside clean instruments and raises
   research capacity while exposing the institution to scrutiny.
3. Memorial hall gives families a common room for names, grief, and a shared
   Recognition ledger.
4. Reserved empty ward keeps emergency capacity available without pretending
   that an unused room is already a public institution.

Every policy has success, partial, and failure results. Results update Food,
Medicine, Power, Recognition, Cohesion, stability, war support, manpower,
capacity, research, trust, durable exposure, policy memory, timed modifiers, and the
Event Log. Failure routes population loss through the shared Deaths contract at
0.1 percent of each owned state's population. The callback uses 0.05 percent
on failure and records a maintained or failed institution memory.

## Cleanup and boundaries

The result and callback use exact issued ticket wrappers. Callback cleanup
prepares result cleanup only after its own ticket is released. Cleanup retains
ward capacity, research, trust, durable exposure, and policy memory while clearing registry,
frozen ledgers, branch, result, callback, and transient flags. It does not
activate the Fallout scheduler, host authority, save recovery, or multiplayer
behavior.
