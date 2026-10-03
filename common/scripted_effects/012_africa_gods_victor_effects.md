# Gods capitulation victor and recognition contract

The participant named by the engine as Africa's capitulation winner receives a permanent hidden victory record and an exemption from ordinary Gods demands and punishment.
No faction-wide credit, annexation-winner inference, automatic successor renewal, reparations waiver, or resource grant is part of victory recognition.
An explicit request by the victor and acceptance by the current African host constitute the separate Event 012 re-legitimation milestone.
Independent permanent defiance remains subject to its existing paid reconciliation.

## Native transaction capture

Installed `common/on_actions/00_on_actions.txt:931–945` identifies ROOT as the capitulated country and FROM as the winner.
Both existing Event 012 `on_capitulation` owners mark ROOT with transient `gods_of_africa_capitulation_callback`, call `gods_of_africa_capture_capitulation_victor = yes`, and clear the authorization before continuing their original cleanup.
Capture precedes any roster/pointer cleanup in both files, so merged callback ordering cannot discard the proof first.
No recurring on-action or world iteration is added.

The capture effect runs in the native defeated ROOT country, requires actual capitulation, the current host pointer, live Gods/consolidation ownership, and authorization, then saves regular `gods_of_africa_victory_defeated_host`.
It enters native FROM and calls `gods_of_africa_record_participant_victory = yes`.
The record trigger requires the authorized native ROOT, an existing capitulated captured host matching both ROOT and the global host, its generation/origin, actual live participant-array membership of the winner, and the same generation.
Unregistered victors receive no participant result; they never acquired this Gods contract.

The record effect increments normal `gods_of_africa_victory_count`, captures the defeated host ID, generation, original Event 012 origin, and day, and appends aligned victory host/generation/day arrays.
It appends history kind `victory = 13` through the existing history writer before setting exemption, while proven live history authority still exists.
It clears a previous renewal request, sets permanent `gods_of_africa_victor_recorded`, current `gods_of_africa_victor_exempt`, and latest presentation sequence/pending fields, and queues `.615`.
It supplies the actual winner as secondary actor for the existing unifier-loss milestone.
There is no payment, stock transfer, Wrath change, punishment, or automatic pardon.
Exemption closes current-generation authority immediately; the second callback's record attempt cannot pass live membership/exemption proof again.
The existing complete host-loss transaction then removes ordinary contracts and protection but leaves victory facts and its distinct report intact.

## Exemption and receipt

The current-generation participant predicate and registration predicate reject `gods_of_africa_victor_exempt`.
Ordinary dispatch, active response/payment, expiry, voluntary aid, reconciliation, and punishment consumers use that authority predicate.
Raw punishment intent/application also require an active non-capitulated host, so pending intent cannot act after the host loses authority.
Re-entry, government change, a new host generation, an ordinary pardon, and receipt acknowledgement never clear exemption.

`.615` uses `gods_of_africa_victor_report_is_current = yes`, which validates the existing recipient, permanent victory result, pending presentation, required latest defeat fields, and report sequence equal to the victory count.
It does not require the defeated host to survive or the victor to remain registered.
Acknowledgement consumes presentation and its report sequence only.
Victory count, host/generation/day arrays, latest defeat, history, and exemption remain permanent.
The report is a latest-episode receipt, consistent with other Gods response receipts; the aligned hidden arrays retain every recorded victory episode.

## Explicit bilateral renewal

The relationship predicate requires a living ordinary victor, permanent result/exemption, a genuine history ledger and optional matching owner stamp, and an already active committed Gods host with the same Event 012 origin.
The victor may request recognition only outside war with Africa and while holding no current African host core territory.
An existing current request blocks resubmission; a stale request for another host/generation/episode can be replaced explicitly.
The request records normal accepting-host ID, generation, origin, and current victory sequence and sets `gods_of_africa_victor_renewal_requested`.
No clock, mission, fee, authority restoration, or defiance pardon is created by requesting.

Host acceptance requires the exact current request and ROOT to be the active current host.
Calling the commit helper from the victor's own country event therefore cannot self-approve it.
The commit records the accepted victory sequence, host, generation, and day; appends history kind `victor_relegitimation = 14` under that explicit transaction proof; clears exemption and request permission; and invokes normal enrollment when currently eligible.
Older-generation or temporarily non-major victors retain the historical milestone even when ordinary enrollment waits for normal eligibility.
Eligible entrants receive the standard first-demand delay and preserve their previous conduct ledger.
Permanent defiance, prior victory facts, and completed material transfers remain unchanged.
Once the request is consumed and exemption cleared, a repeated acceptance fails before changing history or authority.
Later genuine victory creates a new sequence and invalidates old renewal consent.

Accepted renewal emits `africa_event_log.gods_victor_relegitimation` (12208) through the existing Event 012 history gateway, with the accepting host as actor and the victor as secondary actor.
Both list-title and selected-detail consumers resolve this payload, with English wording in `012_africa_event_log_l_english.yml`.
The request is consumed before emission, so repeated acceptance cannot duplicate its history entry.

The existing participant seek/return and host accept/reject rows carry request, withdrawal, acceptance, and decline without additional primary actions.
Their existing AI scores remain unchanged.
The ordinary defiance branch still transfers ten political power to Africa and requires host acceptance within its existing review window.
The victor-recognition branch displays its own no-reparations offer and never debits that price.
The direct defiance completion helper also validates accepting ROOT ownership.

Withdrawal clears request fields only, including stale requests.
Decline requires the current request and the current host's ROOT consent, records its host/generation/day/sequence and history kind `victor_renewal_rejected = 15`, clears the request, and opens the existing `.612` report with its recognition-specific title/body.
It imposes no ordinary refusal penalty and preserves exemption.
New victory, a new request, or accepted renewal clears stale decline presentation; report acknowledgement clears only its own pending/sequence fields.

## Helper inputs, outputs, and usage

All helpers run in COUNTRY scope and accept no named parameter blocks.
Native capture is callback-only; recording is internal to its explicit authorization and saved host.
Renewal effects read country-owned normal victory/request fields and the current host pointer, with no inferred host or default origin.
Receipt helpers read their own country-owned latest snapshots.
Missing proof fails closed; cleanup takes no inputs and clears exactly the five request fields/flag.

```text
# In native on_capitulation ROOT scope, before loss cleanup:
set_country_flag = gods_of_africa_capitulation_callback
gods_of_africa_capture_capitulation_victor = yes
clr_country_flag = gods_of_africa_capitulation_callback
```

```text
# Victor COUNTRY action:
gods_of_africa_request_victor_relegitimation = yes

# Current host's targeted action, with native FROM as victor:
FROM = { gods_of_africa_commit_victor_relegitimation = yes }
```

## Assets, evidence, and remaining work

`.615` reuses registered `GFX_report_event_012_africa_gods_defiance`; `.612` retains its registered response picture.
The four controls retain their existing Event 012 decision icons and category panel in `interface/012_africa_event_pictures.gfx` and the existing Gods interface definitions.
No image, DDS, portrait, model, scripted GUI, extra public counter, or new country package is introduced.
The control handoff records exact English leaves, dynamic cost/title/body resolution, and native ROOT/FROM references.
The authority handoff records source snapshots and winner, non-winner, ordering, duplicate, stale offer, self-approval, permanent-defiance, withdrawal/decline, and receipt cases.
Both are under `docs/plans/012_africa_plans/subagent_handoffs/` with the implementation report.

This milestone restores authority over the consenting victor only; it does not automatically reopen a defeated old host's cancelled global Gods lifecycle.
Recovered-original-host/government-in-exile reopening remains a separate accepted owner-lifecycle requirement until its exact callback/epoch route is implemented.
Full hidden-history grading, capability/contribution reward scaling, mandatory weighted-scenario evidence, live art/text acceptance, and a clean native error.log remain separate completion requirements.
No source traversal, score-only AI review, or cached MCP definition is presented as native engine acceptance.
