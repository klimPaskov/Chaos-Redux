# Event 131 Immigrations: achievement integration prompt

## Assignment and ownership

Integrate genuine Event 131 outcomes with the five existing migration achievements. Event 131 is a repeatable starter that submits a proven additional flow to shared migration. Migration and its humanitarian achievement recorders retain cohort, route, reception, settlement, return, and qualification ownership.

Read the Event 131 specification, any explicitly accepted implementation plan, AGENTS.md, the events and subagents skills, `docs/systems/migration_system.md`, `docs/systems/civilian_transfer_system.md`, and the current humanitarian validation contract. Inspect `common/achievements/chaos_redux_achievements.txt`, `common/scripted_triggers/humanitarian_achievement_triggers.txt`, `common/scripted_effects/humanitarian_achievement_effects.md`, their actual recorder implementation, owning constants, and affected migration callers.

The original pass inspected repository snapshot `41bc4e5045a7b5c131be69dda2f08079d478634c`. The IDs, trigger names, and file paths named here were re-verified at `2eabe59360`, and current source must still be rechecked before implementation. Preserve existing IDs, rewards, thresholds, durations, icons, and localisation. This assignment adds provenance continuity and fixes only demonstrated integration gaps. Player-facing copy remains direction-only for the researched localisation pass.

## Existing achievement contracts

Each registered ID below uses the corresponding `humanitarian_achievement_<suffix>_is_complete` trigger. The table summarizes its current evidence requirements. Read the complete predicates and recorder contracts before changing a caller.

| Existing registered ID | Evidence that must remain binding |
| --- | --- |
| `migration_no_one_left_at_the_gate` | Completed terminal generation, all qualifying cohorts protected and resolved, durable outcome, safe reception, valid origin/front/counterpart identity, protected people equal qualifying people, and aligned qualifying/protected/resolved cohort sets. Violent pushback, forced return, internment, and forced labor disqualify the protected outcome. |
| `migration_roads_home` | A major cohort displaced for the existing qualifying duration, ended departure cause, safe origin food and housing, safe route and protection, and a returned large majority. Exact cohort and generation must match, and the credited country must be the tracked origin or host. Forced return and failed return accounting disqualify it. |
| `migration_hungry_not_contagious` | A genuinely outbreak-exposed cohort received through controlled medical reception, with no resulting outbreak or overload and a durable outcome. Cohort, generation, origin, and host evidence remain valid. Protected internment, forced labor, and forced return remain disqualifiers. |
| `migration_a_place_at_the_table` | Existing distinct-origin and integrated-population targets, stability strictly above the existing threshold, all tracked receiving states food-safe, and aligned integration state/cohort evidence. Transfer cycling and integration disqualification prevent completion. |
| `migration_the_country_did_not_empty` | Existing severe-core-state and threatened-population requirements, proven war and displacement, every tracked core state recovered, all famine states recovered, and all major cohorts resolved. The country remains independent and existent, with no core-floor breach, disqualifying tag switch, or annexation. |

All five retain `humanitarian_achievement_possible_campaign_is_valid`. Completion also requires `humanitarian_achievement_natural_campaign_is_valid`, including initialized tracking and positive initial core population. Preserve human-country eligibility, ordinary civilian-system eligibility, and every debug, forced-trigger, and scenario disqualification.

The achievement predicates exclude special Chaos countries. The Holy Realm's humanitarian movement exception does not waive that separate achievement rule or its own policy-surface exception.

An Event 131 cohort may contribute genuine evidence without completing any achievement. A calm opportunity-driven movement cannot supply nonexistent war, outbreak exposure, severe threat, or recovery proof.

## Trace the real outcome path

Follow the accepted Event 131 request into the migration owner. Preserve the real origin, host, people amount, cohort identity, generation, cause, and route context required by that contract. Keep Event 131 provenance separate from ownership of physical movement. Existing migrants are not a newly qualifying cohort merely because another starter fires.

The exact civilian-transfer owner applies one measured origin debit, records route deaths as part of that debit, and credits survivors. Valid movement satisfies `actual origin debit = route deaths + actual survivor credit`. Rolled-back or unfinalized requests cannot produce achievement credit.

For corridor protection, the current receiver contract runs in the actual receiving country. It requires conserved zero-death transfer of the full qualifying cohort with exact destination owner and route identity. Consent alone records no protection. Repeated cohort receipts are rejected. Preserve the generation-bound archive of qualifying, protected, and resolved sets at terminal cleanup.

For local integration, `migration_settle_integrated_cohort` proves the hosted cohort and both reception ledgers, debits reception load once, completes the row, and then credits national integration and achievement history. A rejected settlement changes nothing. Preserve durable history when Event 131's starter lifecycle ends, including unresolved people still owned by migration.

Use existing recorders at their established successful transaction points. A demonstrated missing call or provenance field may receive a narrow documented repair. Qualification must continue to arise from actual owner outcomes rather than event firing, report acknowledgement, offered capacity, accepted negotiations, or requested movement.

## Focused validation

Trace a natural qualifying path and the failure cases relevant to each changed seam. Check partial transfer, nonzero route deaths for a zero-death requirement, rolled-back payment or movement, stale cohort generation, changed destination ownership, duplicate receipts, rejected settlement, return of the wrong cohort, and event closure with survivors unresolved.

Confirm that forced/debug execution remains ineligible. Confirm that legitimate repeat firings can contribute distinct real cohorts without recounting previous people or recycling origin credits. Verify existing threshold operators and constants remain unchanged, particularly the strict stability comparison and exact cohort/generation equality checks.

Preserve the four public values: Displacement, Reception Capacity, Reception Law, and Departure Law. Achievement evidence remains internal or within existing achievement presentation.

## Worker, tool, and delivery map

Use `chaosx_scripted_system_architect` for a bounded caller or receipt repair and `chaosx_event_completion_auditor` for an independent read-only comparison against accepted requirements. The parent owns final integration. Each worker receives an isolated prompt with exact inspected files and the proposed patch boundary.

Use targeted repository reads and `hoi4.source_lookup` for caller and precedent tracing. Use `hoi4.reference_search` and `hoi4.reference_read` for uncertain scope contracts. Apply `hoi4.script_validate` to changed effect or trigger bodies under their actual scope when available. Report unavailable verification as an evidence limit and retain source-based findings. These are planned tool uses.

Deliver a matrix mapping all five IDs to unchanged eligibility, completion predicates, actual Event 131 contribution paths, recorder scopes, generation guards, and meaningful checks. Include changed files, exact integration gaps fixed, preserved difficulty, remaining owner work, and the distinction between source validation and user-run campaign evidence. Existing art and reward presentation require no new production package.
