# Event 006-owned Event 021 carrier and native footprint queries

These are read-only COUNTRY-scoped helpers on the exact proposed donor.
They publish temporary query data and regular event targets, not actor births or territory/resource changes.
The donor can differ from the event ROOT.
No Event 006 fired state, cap, weight, evolution, release history, league enrollment, public actor alias or setup flag is changed.
No focus, character, units, technology, graphics or GUI is introduced.

## Blueprint

`independence_wave_query_event021_carrier_blueprint` reads the caller's normal `independence_wave_event021_adapter_package_id` and the already initialized complete-package allowlist.
It resolves the same thirty-two static carriers as the current Event 006-owned release crosswalk, without requiring the blueprint to be a living map country.
The caller must directly initialize `event021_release_query_status`, `event021_release_carrier_id` and `event021_release_queried_package_id` before calling if it consumes those outputs after return.
The matched result publishes regular `event021_release_carrier_blueprint` and its native country ID.
Unavailable registry/input, an invalid donor or unknown package leaves any earlier target unusable through the fresh status/ID receipt.
The helper does not initialize the allowlist itself or infer content completeness outside it.

## Native footprint

`independence_wave_collect_event021_native_footprint` requires the same donor/package and a fresh matched blueprint receipt, including country-ID equality.
For a dormant static carrier it records every currently source-owned carrier core, regardless of controller, using the current world core predicates rather than a static state list or compact package CSV.
For an already living static carrier native release is a no-op, so its native debit is empty.
Explicit living-recipient territorial increments and original-tag reuse remain separate parent admission and planning responsibilities.

The caller directly initializes `event021_release_native_status` and `event021_release_native_count`, and clears the following temporary arrays before entry:

- `event021_release_native_states`: the complete native ownership debit.
- `event021_release_prior_controllers`: country pointers aligned one-for-one with that debit.
- `event021_release_source_core_states`: sparse exact subset on which native release can remove the source's cores.

The helper clears its output arrays at each invocation and requires controller-array cardinality to match the state count before publishing a matched snapshot.
It does not turn uncontrolled ownership into held supply, population, factories or forces, authorize third-party occupation, trim islands, or restore cores.
Regular `event021_release_footprint_source` refers to the actual donor, not ROOT.

## Living identity lookup

`independence_wave_resolve_event021_live_carrier` consumes the fresh queried package and the caller's normal package input.
It uses the native original-tag subset iterator for the selected registered identity, on demand, without adding a periodic hook or unrestricted country scan.
The caller directly initializes `event021_release_live_status` and `event021_release_live_count`, and clears `event021_release_live_matches` and `event021_release_live_identity_statuses` before calling.
The nested recorder uses that caller-owned storage and records every occupied identity once, including a nonhuman or unattested living one, so it cannot look like a free dormant carrier.
Zero living identities yields dormant birth; multiple distinct living identities yields collision.
One living identity with the matching package ID and human classification publishes regular `event021_release_live_carrier` with the living-reuse lookup status.
An unmatched/unattested/nonhuman living identity yields recipient-unavailable, not dormant birth.
This lookup is not content, origin, territory, diplomacy, existing-tree, capital or resource admission; those must be proved by the consuming transaction.
Consumers must require the fresh living-reuse status and exact single-match receipt before using the regular target.

`independence_wave_record_event021_live_carrier_match` is an internal COUNTRY callback in that original-tag subset and must not be called without the resolver's initialized arrays and fresh queried package.

## Defaults, lifetime and use

All status values are centralized enums in `006_independence_wave_event021_footprint_constants.txt`, not resource tuning or a state/package-size limit.
Source ID/count outputs start at zero, and arrays start empty in each direct caller.
Regular targets expire with the effect chain and are invalidated logically by fresh status/ID proof when no replacement is published.
There are no global query targets requiring asynchronous cleanup.

Example: the donor sets the existing normal adapter package input, directly creates the output scalar/array storage above, calls the blueprint query, then calls native footprint collection and living identity lookup only on its fresh matched receipt.
The input variable is caller-owned; a wrapper borrowing another subsystem's input must preserve its old presence/value and restore it itself.
The parent's complete release transaction combines the native set with explicit authorized transfers, reserves the whole set, validates it again before mutation and journals all ownership/controller/core/resource deltas.

## Evidence and incomplete integration

`tests/test_event021_native_footprint_query.py` in this folder executes these production bodies with separate saved country/global state and conservative temporary scalar/array cleanup at each helper return.
Its declared fixtures cover all thirty-two dormant static mappings, full Scotland membership, an uncontrolled core and prior controller, source-core subset, fresh core additions, living static no-op, stale query/input invalidation, all six dynamic original-tag carrier families, static/dynamic collision and occupied-but-unattested identity.
Those fixtures do not create countries or prove native resource, release, controller or rollback behavior.
The typed MCP country/state collection excerpt returned partial syntax/kind/scope evidence with nine commands and three native argument blocks unchecked.
Installed effects 5724–5732, 2312–2326, 4076–4095 and 3878–3896; installed triggers 5390–5398; offline Effects 1232/103, Triggers 1846 and Country creation 829–833 are the consulted contracts.
The native installed release wording and offline free-country wording differ; native diplomacy/callback outcome remains acceptance evidence rather than a lookup assumption.
The helpers are not yet wired into all opening/active/frozen consumers, and their query results alone do not close the complete Event 006 native-footprint requirement.
No anchor-only materialization or blanket exclusion of multi-state packages is implemented here.
