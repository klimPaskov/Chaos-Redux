# Event 012 voluntary diaspora return

Event 012 treats diaspora return as a voluntary, target-owned programme rather than a manpower transfer. The host opens a registry, selects a receiving country and project, and receives an explicit acceptance, counteroffer, refusal, or later withdrawal from that government. Opinion is never a substitute for consent.

## Runtime sequence

1. `open_voluntary_return_registry` establishes the host policy and the individual-consent rule.
2. Target-owned programmes open a request through `africa_diaspora_open_target_request`. The receiving government may accept, negotiate, refuse, or later withdraw.
3. Passage consumes transport capacity and records a voluntary origin group. Housing additionally requires a locally accepted state target and `africa_diaspora_target_has_jobs_or_education`.
4. The livelihood trigger accepts only existing development or education receipts: a local processing chain, Charter development-fund membership, the continental industrial plan, or a completed or partial technical mission.
5. Full housing records permanent housing with livelihoods. A partial result records temporary housing with limited livelihoods. Failure records the housing failure, livelihood failure, and local-ownership loss.
6. Skills missions, investment, citizenship, representation, veterans, and emergency evacuation keep their own ledgers and capacity lanes. Cleanup clears pending requests, event targets, temporary action state, and unused transport or construction commitments without erasing completed rights or project history.

## Integration surfaces

- Gameplay selection and matrix validation: `common/scripted_effects/012_africa_action_effects.txt`
- Consent, capacity, result, and cleanup ownership: `common/scripted_effects/012_africa_diaspora_effects.txt`
- Jobs-or-education and target-owned protocol checks: `common/scripted_triggers/012_africa_diaspora_triggers.txt`
- Shared tuning: `common/script_constants/012_africa_diaspora_constants.txt`
- Receiving-government events: `events/012_africa_diaspora_protocol.txt`
- Player-facing action text: `localisation/english/012_african_union_l_english.yml`

## Visual assets

The accepted Event 012 asset matrix owns the diaspora decision and focus families. Decision sprites belong in `gfx/interface/decisions/012_africa/` and their registrations belong in the existing Event 012 decision GFX file. Focus sprites belong in `gfx/interface/goals/012_africa/` and their registrations belong in the Event 012 focus GFX file. No additional livelihood icon is inferred by this mechanic; jobs and education are visible requirements and runtime receipts within the existing housing action.

## Validation evidence

The mandatory event-chain trace for `chaosx.nr12.310` completed against Event 012 revision `08357425bddf932a120a6cb3abc5b9d7ed72c68b80cfbbc9add75ddb313d0b64` and produced `event-trace-08357425bddf.json`. The analyzer classified the repository-wide result as partial because the complete merged event graph contains unresolved nodes outside this bounded diaspora chain; this evidence is not represented as live gameplay validation.

## Future depth

Later event content can add disputes over professional accreditation, municipal hiring, school capacity, land compensation, and local-language education. Those extensions should remain target-owned, keep citizenship and political representation separate from economic capacity, and preserve voluntary withdrawal and refusal.
