# Review of inherited famine round-3 drafts

Disposition: unresolved source-publication ownership.
Acceptance basis: the last takeover audit's three implementation items, matching spec Parts 2, 5, 7, and 8 and the achievement prompt, under the user's repair authority.
Implementation evidence: the five pre-existing dirty gameplay files dated 2026-10-05, together with this pass's separately owned output and timer corrections.
This review does not authorize committing another agent's uncommitted hunks.

## Food context contracts

`famine_collect_surface_context` resolves occupation and local-war evidence for its exact registered STATE.
The local-war output is declared before the helper call.
The war adds 8 transport pressure and 4 need pressure only when local-war evidence holds and both owner and controller are at war.
No new scan or on_action is introduced.

`famine_open_outbreak_food_context` runs in the accepted outbreak request's STATE.
It converts `famine_surface_context.outbreak_context_days` (30) through the shared day/date helper and writes `famine_outbreak_context_until_date`.
While that date is later than `global.date`, the collector adds production 20, transport 20, vulnerability 20, and environment 10.
`famine_adapt_black_plague_state` calls it only after the food-pressure request returns one.
The existing owner retains outbreak deaths and outbreak source identity.

`famine_open_disaster_food_context` similarly writes `famine_disaster_context_until_date` for 60 days.
The collector adds production 30, transport 15, and need 20 while that window is open.
Natural Disaster and Acid Rain adapters call it only after an accepted request.
Repeated accepted requests extend the date without stacking a second copy of the component contribution.
Expiry removes the contribution during the next assessment, and retirement clears both dates.
Both groups have an unrelieved component score of 28.4 before the shock, reserve relief, or other current causes are applied.
Food stored in advance can absorb the interruption, and poor stores permit strain as stock runs down.
These figures are source arithmetic, not a live outcome or a substitute for the evaluator tests.

Permanent documentation still requiring publication with these drafts: the local-war collector row in `famine_core_effects.md`, the two context-helper rows and adapter behavior in `famine_adapter_effects.md`, and the corresponding causal description in `docs/systems/famine_system.md`.

## Historical cause gates

The selector and mapper share `famine_china_policy_profile_cause_proven`, `famine_ceara_profile_cause_proven`, and `famine_congo_profile_cause_proven`.
Every gate requires positive live food pressure and the specified regional owner/controller.
Their state anchors, profile-component tables, and stage thresholds remain unchanged.

China accepts CHI or PRC in Henan with extraction, concealment, forced-labor quota, restricted departure, or occupation conduct.
Ceara accepts Brazilian ownership/control with a disaster/resource-shortage source, an open disaster context, restricted departure, or an active camp.
Congo accepts Belgian/French ownership/control with occupation, non-core colonial ownership, local-war evidence, forced labor, or an active camp.
The changed gates cannot turn peaceful zero-pressure 1936 anchors into active famines.

Permanent documentation still requiring publication with these drafts: the cause-gate API notes and the historical-profile discussion in `famine_core_effects.md` and `docs/systems/famine_system.md`.

## Achievement attribution

The six blockade/extraction recorders compare the calling state's identity and generation to the country being credited through nested `PREV`, rather than ambient chain `ROOT`.
`humanitarian_achievement_record_blockade_concealed_mortality` sets the flag read by the actual achievement trigger, only for its tracked state and generation.
The mortality owner calls it after a positive applied famine loss in a concealed tracked blockade state, for the state owner and a different controller.
A new blockade generation clears that disqualifier with its other tracked-attempt flags.
The older similarly named famine condemnation flag is a separate output and cannot replace this achievement flag.

Permanent documentation still requiring publication with these drafts: the concealed-mortality recorder and credited-country contract in `humanitarian_achievement_effects.md`.

## Limits

The independent completion auditor confirms matching selector/mapper gates and exact achievement ID/generation attribution in the current working source.
Source tests and live acceptance remain distinct.
No draft is promoted to committed implementation by this review, an old status label, or the existence of an uncommitted file.
