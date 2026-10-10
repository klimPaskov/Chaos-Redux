# Acceptance and completion contract

The general completion, simplification-reporting, audit-routing, and validation rules are in `CLAUDE.md` and [the subagent skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md).
This file lists only what is specific to Event 036.

## Required surfaces

- Alien Spacecraft removed from slot 36 and its recovery relocated into Event 025 with unchanged receipt names ([01](01_event_identity_and_playable_promise.md#legacy-alien-spacecraft-relocation))
- Canonical entry, Minor Fire-Once registration, Chaos level 1, and the cluster 3 member row at High severity
- Opening responses for humans and AI, registries, Standing, coordinator, and Opposition Leader
- Four postures, the covert program, accession, revision, withdrawal, suspension, and expulsion
- Condemnation relief at the correct pipeline point, context limits, combined floors, retaliation through Retaliation Authority, reservation breach, the participant-score term, and opening normalization
- Conference scheduler, three-option responses, quorums, and all ten treaty families
- Evolutions I to III with enable handling and accelerated ordered activation
- Integrated doctrine
- Program providers, equal selection, contributions, completion, cancellation calls, dormancy, pause, and Charter lapse
- Decision category, header, missions, and the reuse of existing CBRN actions
- AI for every decision and response, with probability evidence for every weighted surface
- Event-owned Chaos rows, History, evolution rows, Event Details, news, localisation, assets, and achievements
- Workbook update and CSV export

## Discovery before implementation

The implementation names exact live identifiers for:

- the chemical doctrine mitigation point (`cbrn_prepare_chemical_action_record` and the exposure calculation) and every other Condemnation caller that needs the convention hook
- the Retaliation Authority classification and the CBRN ledger first-use field
- the pledge-breach consequence inside `condemnation_add_source`
- the participant scoring inside `condemnation_recalculate_participants`
- the eligibility triggers of `cbrn_demand_inspections` and `cbrn_sponsor_decontamination_mission`
- every event-gated weapon special project and its access trigger
- the cluster 3 runtime registry and the evolution registration

These specifications supply no guessed substitutes.

## Performance

No whole-world daily or monthly country scan.
The opening uses one bounded event-time pass, and later work iterates the registries, the active agenda, project participants, and the coordinator's timed events.
Program cancellation is called by the provider, and the 30-day recheck is only a fail-safe.

## Save contract

Save and reload preserve the fired state, postures, covert flags, Standing, the active agenda with its responses and deadline, ratifications, evolution state, integrated doctrine, the selected project, progress, receipts, program state, Chaos and normalization flags, and achievement tracking.
Reloading never duplicates responses, normalization, resolution, progress, or grants.

## Forbidden substitutes

- a national spirit in place of recurring treaties
- free technologies or projects in place of access
- a guessed provider list or weighted project selection
- source-event firing in place of the access flag
- a research-sharing group that cannot be removed
- a custom GUI in place of ordinary decisions
- direct CSV edits

## Completion report additions

Besides the `CLAUDE.md` report, list the registered providers with their access flags and cancellation calls, the selection proof for one, two, and three candidates, and the Condemnation checks from [03](03_condemnation_normalization_and_cbrn_integration.md#required-checks).
