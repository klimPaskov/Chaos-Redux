# Event 052 Repository Context

## Repository snapshot inspected

- Repository: `klimPaskov/Chaos-Redux`
- Default branch: `master`
- Inspected commit: `d549536e869056a49890a08ff795fbc80659984e`
- Commit date: 2026-08-27
- Commit message: `Record current Event 006 probability audit`

The connected GitHub repository was used because the local mod root described in the project files is a Windows path outside this execution environment.

## Current Event 52 source

The repository contains:

- `events/052_intelligence_leak.txt`
- `localisation/english/052_intelligence_leak_l_english.yml`
- `events/_chaosx_news.txt` with `chaosx.news.53`
- `interface/chaosx_pictures.gfx`
- `gfx/event_pictures/052_intelligence_leak/report_event_intel_leak.dds`
- `gfx/event_pictures/052_intelligence_leak/news_intel_leak.dds`

Event 52 is already registered in `global.repeatable_events`.

## Legacy behavior that must be replaced

The current chain contains two events.

`chaosx.nr52.1` is a hidden target selector. Its current candidate condition mixes major, human-control, and war checks in a broad structure.

`chaosx.nr52.2` gives every country `100` civilian, army, navy, and air intelligence against the target.

The current behavior has no event-owned expiry, no reversible intelligence ledger, no Exposure value, no target damage-control category, no operative or network risk, no Poison the Leak route, no evolution handling, and no complete cleanup.

The specification treats this as legacy source to replace. It preserves the event ID and namespace.

## Stable identities to preserve

- Event namespace: `chaosx.nr52`
- Entry event: `chaosx.nr52.1`
- Existing target-facing event slot: `chaosx.nr52.2`, unless the implementation needs to repurpose it while retaining compatible history
- Existing news event identity: `chaosx.news.53`
- Existing report sprite: `GFX_report_event_intel_leak`
- Existing news sprite: `GFX_news_intel_leak`
- Existing runtime asset folder: `gfx/event_pictures/052_intelligence_leak/`

The source-design folder uses the accepted event-name slug `intel_leaked`. The implementation can retain the established `intelligence_leak` source filenames to avoid needless churn.

## Asset preflight finding

The GitHub contents API reported both Event 52 DDS files as 130 bytes. This size is consistent with a Git LFS pointer, but size alone is not proof.

Before visual review, the asset worker should:

1. Inspect the exact file bytes for the Git LFS pointer signature.
2. Check the index OID through `git lfs ls-files -l`.
3. Run scoped `git lfs checkout` for the two Event 52 DDS paths when the objects exist locally.
4. Verify the working-file hashes against the index OIDs.
5. Decode and inspect the hydrated DDS containers.

The files should not be replaced solely because of the API size.

## Existing Event 011 connection

The Event 011 Secret Alliance specification already identifies Event 52 as a future stable hook.

Its accepted direction is:

- a leak involving a pact member can increase Evidence
- a leak involving the pact target can increase Pact Readiness
- the connection should wait for a stable Event 52 public contract

Event 52 implementation should expose the public facts needed for this adapter and should avoid reading Event 011 private state directly.

## Event log and enablement work

Event 52 is currently registered as Repeatable, but the rework must still verify:

- event-name selectors
- debug-name selectors
- default actor mapping
- Event Details row
- event Chaos level display
- evolution preview rows
- default-enabled state for a completed rework
- manual normal firing
- cluster membership
- history actor for Total Compromise

The event should remain disabled by default until the rework is complete and aligned. The implementation pass should add it to the reworked-event default allowlist only with the finished event registration and log wiring.

## Likely owner files

The exact final file map should follow current repository precedent and the installed HOI4 documentation. Likely event-owned surfaces include:

- event chain
- decision category and decisions
- event-owned scripted effects
- event-owned scripted triggers
- event-owned script constants
- event-owned on-actions or delayed event pulses
- dynamic modifiers or ideas for temporary exposure
- AI strategy or decision weights
- event localisation
- decision and tooltip localisation
- scripted localisation for Exposure, domains, targets, and blocked reasons
- Event Log integration
- achievement registry and tracking
- event documentation
- authoritative event catalog workbook
- GFX definitions and runtime assets

A neutral helper belongs in `chaosx_dynamic_effects` only when several unrelated systems need the same contract. Event 52 lifecycle and selectors remain event-owned.

## Mandatory implementation references

Before coding, the implementation agent should read the required offline Paradox wiki pages and installed vanilla documentation for:

- events
- decisions and missions
- intelligence and agency effects
- modifiers
- scopes and event targets
- on-actions
- AI weights
- localisation
- graphical assets

The HOI4 MCP event and probability routes are mandatory for the supported event-chain and weighted surfaces. Source inspection alone is not equivalent evidence when the MCP route is available.
