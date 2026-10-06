# Event 002 release QA decisions, 2026-10-05

## Authority and disposition

This record follows the parent task dated 2026-10-05, which explicitly authorized a release QA pass for Event 002 and directed the named wording, single-report/count, Settings invalid-host, and once-only defeat-notification checks. It does not claim approval from a missing Event 002 source specification. No Event 002 spec directory was found under `docs/specs/002_zombie_outbreak_specs/`.

## Accepted within the assigned QA scope

- **Initial outbreak super-event wording, implemented.** The parent task identified the “Undead?” heading, Matthew 6:9 quote, and yo-yo button as unsuitable and directed a grounded, attributed replacement. The selected Shakespeare excerpt and film button were researched by `chaosx_super_event_text_researcher`; implementation is in the owned Event 002 English file. This is a bounded presentation correction, not a new event branch.
- **One campaign outbreak news report with a visible successful-site count, implemented in source; runtime counting unverified.** The parent task required aggregated target reporting, no repeated `chaosx.news.3` popup for a player during one outbreak campaign, and a count. Event 002 now counts selected sites only after the target state is controlled by the zombie horde and queues the world report once. The out-of-scope special-project caller was changed by the parent to use the same helper. No numeric balance target was chosen.
- **Settings-forced initial outbreak target repair, implemented in source; runtime dispatch unverified.** The parent task required retargeting a valid populated state or giving a readable rejection when Settings requests Event 002 from an invalid host, when the horde is already active, or when no qualifying state exists. The owned selector returns a suitable host/state and reason values. The dispatcher includes parent-owned preparation and selected-host branches recorded in the integration handoff.
- **Idempotent defeat and postwar memorial flow, implemented.** The parent task asked whether country callbacks could repeatedly schedule the same postwar popup and required a one-first-anniversary report per country. `on_zombie_threat_defeated` and `activate_zombie_postwar_order` now process a campaign once. The `.12` compact is queued once per former combatant. Acknowledging it schedules one `.13` memorial 365 days later; its 10 PP remembrance reward can be claimed only once and it does not requeue.
- **Outbreak-protection revocation gate, implemented without changing numeric AI weights.** The decision audit found five revocation gates only blocked at war with `ZZZ`, leaving dynamic and weaponized outbreak wars untreated. Their availability now uses a specific trigger covering the main, standard dynamic, and weaponized hordes and shows a readable tooltip. The pre-existing AI weight numbers remain unchanged. The analysis server did not provide a baseline scenario, so numerical AI balance remains unresolved.
- **Concise visible prose corrections, implemented.** The parent task's G3 standard and the localisation audit identified unclear weaponized-outbreak summaries and bookkeeping language in the memorial text. Only keys owned by this task were changed. Shared Event Details and achievement prose remain parent follow-up requests.

## Proposals and unresolved acceptance

- A target-selection interface, new decision category, or new event branch was not designed. Those would exceed the accepted release QA scope.
- The historical sixteen-action inventory is superseded by the parent-accepted two-action capital-state consolidation described below.
- The historical weaponized cure action budget is superseded by the parent-accepted consolidation, and the six League-duration/martial-law descriptions are corrected in commit `978c7b5d5745cc00058e136a88b8c068ebe00b94`.
Weighted AI ranking, mechanical scenarios and current GUI evidence remain unresolved; the wording repair does not establish their results.
- Model, portrait, and counter production remain outside this QA patch. Their existing provenance and acceptance gaps are listed in the handoff.

## Implementation evidence and limits

Implementation evidence proves only the source changes listed in `subagent_handoffs/release_qa_20261005.md`. It does not establish approval beyond the parent task, live-game correctness, probability balance, or shared GUI fit. `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.decision_inspect`, `hoi4.gui_inspect`, `hoi4.gui_render`, and `hoi4.probability_inspect` did not return source/scenario artifacts within their recorded timeout windows. No before/after scenario comparison is claimed.
# Parent integration

Explicit Settings requests prepare and revalidate a populated mainland state on a normal civilian host, then dispatch `chaosx.nr2.1` to that host.
The requester target remains available to the shared failure reporter, which displays the owner-provided no-state, already-active, or unavailable reason once.
Automatic firing retains the prior host selection contract.
The laboratory accident in `events/zombie_weaponized_special_projects.txt` uses `queue_zombie_outbreak_world_news`, matching the event-owned overseas outbreak call.
Five shared prevention-revocation descriptions describe ending the measures rather than imposing them.
League investment tests remaining capacity against the authoritative maximum and contribution constants, avoiding duplicate derived totals.
The shared receipt API records whether a PP purchase actually earned sale credit and its sequence, so cancelled orders cannot withdraw an unrelated later-sale credit.
Five actual-source financial scenario groups passed, with native engine primitives explicitly mocked and engine confirmation still open.

The parent inspected the full `evt002_pop01.png` and the contact sheet.
The before and after `hoi4.gui_render` attempts used `windowName = chaosx_super_events`, scenario `{id: usa_1936, date: 1936.1.1}`, 1920x1080 at UI scale 1, normal and long-text states, and disabled generated scenarios.
The linked-window `gui_inspect` and both render attempts timed out at 600 seconds, producing no images or validation artifact for current text fit.

## Current parent reconciliation, 2026-10-06

Acceptance basis is the user's 2026-10-05 release-QA/G6 direction and parent approval of the bounded consolidation.
Two capital-state map-only action types replace the eight research plus eight review definitions, covering all eight profiles through shared helpers.
Constants retain 45 PP, 55 days, 34 progress and 240 days; one-type validation, ready-progress/Wendigo-lock gates and receipt-aware refunds remain enforced.
Two definition types do not imply two world-map markers.
First-defeat totals are preserved in `zombie_postwar_zombie_dead`, `zombie_postwar_civilian_dead` and `zombie_postwar_total_dead` for `.12`/`.13`.
`casualties_k` is converted to people with `constant:zombie_postwar.people_per_thousand`, currently 1000, and eligibility is initialized in the caller.
The approved fictional scene replaces the unverified runtime film still; subagent_handoffs/super_scene_20261006.md records installed hash and archived prior bytes.
Audio IDs 1/5 are verified; IDs 2/3/6 remain unresolved after HTTP 429 and missing runtime matches.
The cure baseline contains unresolved dynamic text; the shared after-layout image uses the previous texture and cannot prove post-scene acceptance.
Current `find_cure_tier_0_desc` through `find_cure_tier_3_desc` say League membership and investment can shorten research, without stale fixed durations.
Current `extreme_martial_law_desc` and `disease_extreme_martial_law_desc` restrict zombie prevention to new rear-area outbreaks and exclude established fronts.
Those six shared source strings are implemented in the committed tranche above; native timing, prevention and GUI fit remain unverified.
Current slot2/3/5 quote strings contain the Liberty Song with Dickinson and Lee attribution, Yeats and Binyon; this is source wording evidence rather than visual acceptance.
See `release_qa_completion_20261006.md` for current dispositions, source evidence and review gates.
