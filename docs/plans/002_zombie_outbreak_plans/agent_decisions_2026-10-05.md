# Event 002 release QA decisions, 2026-10-05

## Authority and disposition

This record follows the parent task dated 2026-10-05, which explicitly authorized a release QA pass for Event 002 and directed the named wording, single-report/count, Settings invalid-host, and once-only defeat-notification checks. It does not claim approval from a missing Event 002 source specification. No Event 002 spec directory was found under `docs/specs/002_zombie_outbreak_specs/`.

## Accepted within the assigned QA scope

- **Initial outbreak super-event wording, implemented.** The parent task identified the “Undead?” heading, Matthew 6:9 quote, and yo-yo button as unsuitable and directed a grounded, attributed replacement. The selected Shakespeare excerpt and film button were researched by `chaosx_super_event_text_researcher`; implementation is in the owned Event 002 English file. This is a bounded presentation correction, not a new event branch.
- **One campaign outbreak news report with a visible successful-site count, source-wired and awaiting shared Settings integration.** The parent task required aggregated target reporting, no repeated `chaosx.news.3` popup for a player during one outbreak campaign, and a count. Event 002 now counts selected sites only after the target state is controlled by the zombie horde and queues the world report once. The out-of-scope special-project caller was changed by the parent to use the same helper. No numeric balance target was chosen.
- **Settings-forced initial outbreak target repair, source helper implemented and shared dispatcher wiring queued.** The parent task required retargeting a valid populated state or giving a readable rejection when Settings requests Event 002 from an invalid host, when the horde is already active, or when no qualifying state exists. The owned selector returns a suitable host/state and reason values. The shared Settings dispatcher still needs the exact parent-owned branch described in the release QA handoff before this is wired end to end.
- **Idempotent defeat and postwar memorial flow, implemented.** The parent task asked whether country callbacks could repeatedly schedule the same postwar popup and required a one-first-anniversary report per country. `on_zombie_threat_defeated` and `activate_zombie_postwar_order` now process a campaign once. The `.12` compact is queued once per former combatant. Acknowledging it schedules one `.13` memorial 365 days later; its 10 PP remembrance reward can be claimed only once and it does not requeue.
- **Outbreak-protection revocation gate, implemented without changing numeric AI weights.** The decision audit found five revocation gates only blocked at war with `ZZZ`, leaving dynamic and weaponized outbreak wars untreated. Their availability now uses a specific trigger covering the main, standard dynamic, and weaponized hordes and shows a readable tooltip. The pre-existing AI weight numbers remain unchanged. The analysis server did not provide a baseline scenario, so numerical AI balance remains unresolved.
- **Concise visible prose corrections, implemented.** The parent task's G3 standard and the localisation audit identified unclear weaponized-outbreak summaries and bookkeeping language in the memorial text. Only keys owned by this task were changed. Shared Event Details and achievement prose remain parent follow-up requests.

## Proposals and unresolved acceptance

- A target-selection interface, new decision category, or new event branch was not designed. Those would exceed the accepted release QA scope.
- Restructuring the weaponized countermeasure category to reduce its possible 16 visible actions requires a separate accepted design decision. The current inventory can exceed the six-action category budget if all eight types are active.
- The weaponized cure category action budget, League cure-duration prose, martial-law scope text, and weighted AI ranking still need separate review. Timed cure, counterstrain, prevention, and League cancellation/refund defects have been patched in the owned decision file; see the implementation handoff for exact IDs and evidence limits.
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
