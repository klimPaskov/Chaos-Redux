# Event 131: Validation matrix

These are future implementation acceptance cases. They are not tests run during this planning pass. Use the existing owner's fixtures and bounded source or tool checks where they can answer the question. Record the evidence type and actual result. Live HOI4 execution remains outside this task unless the user explicitly requests it.

Working case labels are not localisation.

## 1. Selection, identity, and requests

| Case | Setup and action | Required result |
| --- | --- | --- |
| V01: Calm prepared pair | Valid human origin and plausible foreign host, free uncommitted people, viable services and route | A natural episode can start from Chaos 0+. The request, actual departure, and arrival remain separate. Prepared handling creates no automatic unrest |
| V02: Local crisis overlap | A famine or war-capture owner already claims the same state's affected people | Only demonstrably additional uncommitted people can enter Event 131. Zero additional availability declines the new request |
| V03: Missing foreign prospect | The origin has no plausible supported foreign endpoint | No successful firing, new pressure, cost, cohort, history claim, or pacing credit |
| V04: Replay | Replay the same source, origin, generation, and request after acceptance and after save/reload | Exactly one accepted obligation and one event firing. Retries return the existing outcome or fail closed |
| V05: Queue collision | Normal and Domestic Unrest scheduling attempt the same episode | One accepted source identity and one pacing/history record. Cluster selection supplies no extra people |
| V06: Population ceiling | One million origin civilians, proposed acute ceiling of 20,000, only 8,000 genuinely available above floor and unique obligations | At most 8,000 accepted. No rounding up to a shared minimum if that would exceed availability |
| V07: Small origin | Valid minor or subject, but the selected state's permitted request falls below the shared material minimum | That state is ineligible for a new firing. Country class itself is not disqualified, and another valid state may be considered |
| V08: Valid special-country boundary | Test ordinary countries, an annexed country, a disallowed special actor, and the current Holy Realm exception | The actual humanitarian predicate governs movement eligibility. Achievement eligibility remains separately governed by its stricter owner predicate |

## 2. Foreign intent and reception

| Case | Setup and action | Required result |
| --- | --- | --- |
| V09: Competing internal route | Both an internal safe route and a plausible foreign destination exist | Event 131's accepted foreign intention survives. Untagged spontaneous migration retains its ordinary internal-first behavior |
| V10: Every plausible border closed | Valid new intention, all relevant admission routes blocked | People remain at their actual location. No destination population or reception credit, no arbitrary deaths, and no replacement cohort per retry |
| V11: Preparation before consent | Exact incoming request, insufficient real services, affordable valid preparation | Only a real service improvement consumes the matching cost. Preparation and consent each revalidate. Population moves only on finalized passage |
| V12: Refusal and expiry | Host refuses or request expires, then a later prospective route is considered | Only exact request mirrors expire. The owner preserves the retained obligation and identity, with normal retry handling |
| V13: Capacity race | Two valid requests compete for the same host headroom | The owner cannot overcommit capacity or admit a contract that lacks current full headroom. One acceptance does not authorize the other |
| V14: Unchanged paid service | Re-run a service action against an already equal or better provision level | No repeat successful improvement charge or false capacity grant |
| V15: Authority change | State occupation, civil war, annexation, or host loss occurs between quote, payment, consent, and transfer | Revalidate at the actual mutation. Apply matching owner cleanup and refund rules. Preserve living obligations and historical origin |
| V16: Aid promise versus delivery | A donor offers help, then delivery succeeds or fails | Only delivered owner-validated resources or services improve capacity. No free supply from a promise, cancelled mission, or stale target |

## 3. Movement and lifecycle

| Case | Setup and action | Required result |
| --- | --- | --- |
| V17: Safe physical transfer | Execute a valid safe spontaneous leg | Measured debit equals surviving credit. The safe owner requests zero route deaths. Recruitable manpower corrections remain intact |
| V18: Reduced primitive credit | The neutral primitive credits fewer survivors than requested | Restore the exact uncredited residual to origin. Finalized debit equals deaths plus actual credit with zero residual. Publish only the finalized result |
| V19: Full prospective contract | A retained prospective row loses some required headroom | Refuse passage without quietly resizing the row. V18 does not waive this contract's full-headroom rule |
| V20: Route deaths | Use an existing supported unsafe consequence on a genuine moving cohort | Deaths are a bounded slice of measured debit, recorded once by the shared owner. A rejected movement attempt has no invented casualties |
| V21: Integration | A hosted cohort completes the existing integration action, then the callback repeats | Resident population is not credited again. State and country reception obligations clear once. Achievement history is also once-only |
| V22: Distribution and onward transfer | Move a hosted cohort internally, then to another accepted country | Every leg starts from its current host. Original origin, episode, cause, and lineage remain. No new Event 131 firing for these legs |
| V23: Return | Compare safe voluntary return, forced return, and a request cancelled before any departure | Only real return transfers people. Coercive consequences and disqualifiers remain. Cancelled intent creates no fictitious return or integration |
| V24: Mixed outcome | Part of an episode is settled while another part remains stranded or in temporary reception | Local completion can be reported. Overall successful resolution remains unavailable while living obligations are unresolved |
| V25: Loss outcome | All or some members die through actual shared hazards | Preserve deaths and surviving obligations. A closed administrative record does not describe successful relief or award safe-outcome credit |
| V26: Origin recovery | The origin becomes safe while people are waiting there and while another cohort is abroad | Exact unmoved intent may resolve in place. The abroad cohort remains and can consider a valid return. Origin recovery alone never erases it |

## 4. Balance, interface, and evidence

| Case | Setup and action | Required result |
| --- | --- | --- |
| V27: Overloaded host | Real reception demand exceeds current service support | Further admission follows headroom rules. Valid distribution, transit, integration, relief, and return actions remain usable |
| V28: AI parity | Run matched human and AI scenarios for prepared admission, resource shortage, refusal, aid, and safe resolution | Identical validity and cost gates. AI chooses among actual usable actions and can finish without player clicks |
| V29: Chaos overlap and recovery | Orderly wave, new material disruption, later regional severity, shared deaths, and eventual relief | Orderly handling adds 0 direct Chaos. Any event-owned contribution follows the cumulative +5 cap and incremental receipts. Shared harm is not counted twice. Recovery cannot exceed the event's unrecovered contribution |
| V30: Repeat farming | Toggle laws, cancel requests, reroute, reopen reports, and wait out the proposed origin interval | These actions cannot mint new people, new event firings, free aid, repeated refunds, or net negative Chaos |
| V31: Quiet panel | Open Migration during calm conditions and during an active episode | Preserve four canonical values, quiet access, and existing controls. Opening or refreshing creates no pressure or event |
| V32: Information and art | Inspect report, Event Details, state view, map mode, native report art, and both relevant actor roles | Intention differs from arrival, exact data obeys visibility, actors are correct, text fits, and any report DDS matches its actual consumer |
| V33: Shared achievements | Exercise a qualifying receipt, replay it, and test a forced/debug episode | Only the existing full predicates can award. Natural Event 131 is not automatically disqualified. Shortcuts keep their established disqualifiers |
| V34: Identity and documentation | Reconcile event dispatch, history, settings, cluster proposal, workbook, generated exports, and system documentation | Event 131 and retired Event 149 have explicit coherent roles. Widespread Mutiny, already migrated to catalog 120, is not silently destroyed or renumbered. Implementation status matches actual files |
| V35: Final request remainder | Successive first-departure batches leave a positive remainder below the ordinary minimum | No batch exceeds the accepted unfulfilled budget. A supported exact final batch or real terminal disposition resolves the remainder. The minimum neither recruits unclaimed people nor leaves a permanent artificial tail |
| V36: Fulfilled intent and policy exception | One portion has arrived abroad while another waits, and an eligible Holy Realm participant is present | Arrived people can use ordinary domestic distribution while the remainder retains foreign intent. The Holy Realm retains its Event 003 policy adapter and separate panel and achievement eligibility |

## 5. Probability review scenarios

The probability review should cover the complete eligible origin pool, foreign destination pool, and changed response pool. Use these named cases: calm prepared pair, acute local crisis with overlap, poor minor host, closed borders, all routes invalid, internal route available alongside foreign intent, subject origin, changed control, overloaded current host, safe return, and repeat cooldown.

First establish candidate validity and raw scores. Normalize only when the full pool and total are known. Compare the same scenarios before and after a deliberate weighting change. The acceptance goal is sensible selection and usable recovery, not a fabricated percentage target. State-dependent diplomacy, pathing, and native timing remain uncertain where the available tool cannot execute them.

## 6. Completion evidence

The parent maintains one concise route-coverage table linking each spec requirement to actual implementation, exercised case, result, and remaining limitation. A passed source review is source evidence. A partial MCP render is partial evidence. A prior owner's validation artifact is historical evidence until matched to the current source.

Stop optional testing when the concrete risks and required gates are sufficiently covered. Report remaining runtime uncertainty accurately without asking the user to perform a live campaign as a condition of delivering completed authorized work.
