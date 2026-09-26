# Event 020 player-facing ledger language handoff

## Scope and result

I reviewed `020_black_plague_reports_l_english.yml` and `020_black_plague_rat_decisions_l_english.yml` for internal ledger language and nearby player-facing implementation terms.
I changed eight report descriptions and two rat decision descriptions without changing gameplay, costs, keys, event targets, or route outcomes.
The Council's charter ledger in `chaosx.nr20.58.t` and `.d`, its opened ledgers in `chaosx.nr20.79.d.council_audit`, and the inspectors' ledgers in `chaosx.nr20.92.a` remain because they are records inside the story.
The Brood Pulse language remains where it names the rat mechanic or describes the brood's growth rhythm.

## Changed keys and wording

- `chaosx.nr20.11.d`: An active ledger and registered disease phase became the last infected state and the absence of an active basin.
- `chaosx.nr20.12.d`: A status transition and the ledger's classification became failing hospitals, local authorities losing control, and flight.
- `chaosx.nr20.14.d`: A public ledger lag became cases that have not yet been found and the remaining chance to contain them.
- `chaosx.nr20.21.d`: A board threshold became countermeasure teams coordinating treatments, stores, cordons, and transport controls.
- `chaosx.nr20.76.d`: Reopening the Black Plague ledger became the Rat King's strike bringing plague pressure to `[black_plague_royal_strike_state.GetName]`.
- `chaosx.nr20.77.d`: A royal meter and next pulse became the decree's command of the warrens and its cost.
- `chaosx.nr20.78.d.migration_lanes`: The last pulse became paths the warrens could not use before.
- `chaosx.nr20.84.d`: Supply ledgers stopped answering became orders failing to reach hospitals and supply depots in `[black_plague_terminal_campaign_state.GetName]`.
- `black_plague_rat_king_close_the_harbors_desc`: The shared plague ledger became a sealed port that remains a plague pressure point and raises Terminal Preparation.
- `black_plague_rat_king_silence_the_capitals_desc`: The shared disease state became an assault that spreads the plague and advances Terminal Preparation.

## Audit findings

No keys are missing from these two files relative to their previous versions, and no duplicate keys were found within either file.
No scripted-localisation definition was changed, and the existing dynamic bindings in every changed key were preserved.
The existing state and continent bindings already give the strike, capital, harbor, and target-continent text current names, so I did not add another dynamic text call.
These two files still contain some exposed system labels, including `Terminal Preparation`, `Dominion`, `Brood Mass`, `Coherence`, and `Brood Pulse`, which are visible player mechanics rather than internal ledger records.
No changed description contains an attributed or sourced quotation, and no quotation was altered.
No event catalog or Event Details source was edited. A subsequent read-only workbook audit found no old wording from these ten keys in Event 20's detail fields (`Events!C21:I21`), the Diseases cluster detail (`Clusters!C14`), or the Black Plague Unbound scenario fields (`Scenarios!C12,E12`). `Events!H21` summarizes capitals falling silent and remains consistent with the revised `.84.d`. No workbook save or CSV export is warranted for this text-only change; the workbook and two CSV exports already had unrelated uncommitted edits and were left untouched.
No broader wording pass was made on other reports, decisions, or scripted localisation.

## Prose changes

Vagueness: `chaosx.nr20.21.d` names the teams and the measures they coordinate, and `chaosx.nr20.84.d` names the facilities cut off from orders.
Bloat and repetition: `chaosx.nr20.11.d`, `.12.d`, and `.14.d` remove explanations of ledger or status bookkeeping that repeated the event title or visible state.
Obvious explanation: The harbor and capital decision descriptions state the visible plague consequence rather than describing a shared data record.
Overcomplication: `chaosx.nr20.77.d` and `.78.d.migration_lanes` replace meter and pulse references with direct court and warren actions.
Style-rule repair: The changed prose uses complete sentences without em dashes, semicolons, or implementation history.

## Source and validation evidence

The offline wiki `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` at lines 73-104, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, confirms the file and line format and UTF-8 BOM requirement.
The same wiki at lines 184-215 and the installed `documentation/script_concept_documentation.md` at lines 12-22, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, cover dynamic localisation syntax.
The offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` at lines 49-75, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`, describes event title and description keys.
The offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` at lines 284-318, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, describes custom decision cost localisation.
`hoi4.source_lookup` located `chaosx.nr20.76` in `events/020_black_death.txt` at lines 927-934, source revision `da0062669ae144b3d3fbb89e6e5fda86e0bd23efebd905069698a4591fbde7d0`.
`hoi4.event_inspect` returned Event 020 graph revision `5cfd608b1d0673f7046c5eccdee8afee71788e3fb9de77e3571fac4a9226b6c9` with no blocking diagnostics for the bounded query.
`hoi4.event_render` returned a source-linked `chaosx.nr20.76` neighborhood at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54769caf6b3aa4c08e5677c3f8b31ae74dcbbf89ba17ecde0acb91cf7a812274/489febe62b2afd3b74b003935f41d23b78b3a8addc4e6dbd07d53f1e7bcb670e/event-neighborhood-5cfd608b1d06.json`.
The render selected three nodes and omitted 42,867 workspace nodes, so it is bounded chain evidence rather than exhaustive Event 020 coverage.
A key-level comparison against `HEAD` found the ten intended text changes, no added or removed keys, no duplicate keys, and identical dynamic-token multisets in every changed key.
Both edited files retain the `EF BB BF` prefix and have no encoding concern.

## Limits and parent follow-up

The standalone Technology Tree Viewer was not exposed in the connected tool list, while the technology inspect, render, and compare routes were exposed; this is a package gap and technology is outside this text-only scope.
The event comparison route rejected a call without a baseline as `EVENT_COMPARISON_BASELINE_REQUIRED`, rejected the returned graph revision as `EVENT_REVISION_NOT_CACHED`, and rejected the returned graph artifact URI as `ARTIFACT_NOT_FOUND` because its provenance manifest was unavailable.
This leaves event comparison blocked despite successful inspect and render routes, and the text-only patch has no MCP before-and-after comparison claim.
I did not render any scripted GUI because no GUI text or layout file was assigned, and I did not run the game because live consumer validation belongs to the user.
Event Details and workbook wording were checked at the fields above; no text mirror requires an update. Other Event 020 spreadsheet rows and live presentation remain outside this bounded language pass.
