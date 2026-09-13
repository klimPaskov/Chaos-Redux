# Chaos weapon registry contract

## Provider row checklist

| Row field | Required proof | Failure disposition |
| --- | --- | --- |
| Stable project ID | Unique constant and save-safe identity | Block registration |
| Display token | Existing or new owner-approved localisation | Block player-facing selection until present |
| Source owner | Exact event or system file and identifier | Block registration |
| Prerequisite token | Exact research, project, or weapon gate | Block registration |
| Eligibility trigger | Read-only and fail-closed | Block registration |
| Normal availability trigger | Exact legitimate source proof | Block registration |
| Participant trigger | Country-scope and fail-closed | Skip invalid recipients, block if none exist |
| Grant adapter | Idempotent narrow prerequisite grant | Block registration |
| Contribution profile | At least one valid contribution family | Block registration |
| Progress factor | Script constant from `0.75` to `1.50` | Use default `1.00` only when owner approves |
| Cancellation callback | Called in normal unlock transaction | Block registration |
| Isolation proof | No source event or consequence state | Block registration |
| Cleanup adapter | Clears provider temporary state | Block registration if temporary state would leak |

## Candidate build proof

For each selection, record:

- registry generation
- membership generation
- complete unique provider ID list
- rejected provider IDs and reasons
- eligible unique candidate IDs
- candidate count
- selected ID
- random selection result
- selection date

## Uniform selection proof

| Unique candidate count | Required exact probability per candidate |
| ---: | ---: |
| `1` | `100%` |
| `2` | `50%` |
| `3` | `33.333...%` |
| `4` | `25%` |
| `5` | `20%` |

The implementation can use an equal-weight random list or a uniform random array index.

Duplicate provider registration attempts must not add weight.

## Contribution profile schema

| Profile field | Purpose |
| --- | --- |
| Industrial cost band | Civilian factory and optional transport commitment |
| Research cost band | Research burden, experience, political power, scientists, or manpower |
| Equipment token set | Supported stockpile debit helpers and substitution order |
| Facility requirement | Valid facility, state, or owner capability proof |
| Progress ranges | Minimum, normal, and maximum applied progress by family |
| Country cooldown | Time before the same family can be used again |
| Project stage modifiers | Any provider-approved changes by 25%, 50%, or 75% stage |
| Recipient compatibility | Country trigger used again at completion |

## Completion isolation checklist

The completion transaction must prove all rows false before and after the grant:

| Forbidden side effect | Before | After |
| --- | --- | --- |
| Source event fired flag | False | False |
| Source event fired count increased | False | False |
| Source event history row created | False | False |
| Source event random weight changed by grant | False | False |
| Source evolution activated | False | False |
| Source crisis state activated | False | False |
| Source country created | False | False |
| Source world-threat flag set | False | False |
| Source super-event shown | False | False |
| Source terminal state activated | False | False |
| Source narrative stage advanced | False | False |

The only intended after-state is that the valid recipient can access the registered prerequisite or research route.

## Cancellation callback checklist

| Step | Required result |
| --- | --- |
| Source normal unlock begins | Provider proves legitimate normal availability |
| Callback checks active Event 036 project | Exact project ID match required |
| Contribution visibility | Hidden immediately |
| Project state | Cancelled by Normal Availability |
| Shared progress | Set to zero and recorded as discarded |
| Participant receipts | Preserved as historical, no unlock eligibility |
| Spent resources | Not refunded |
| Duplicate unlock | Not granted |
| Candidate pool | Rebuilt after administrative interval |
| New selection | Uniform across remaining unique candidates |
