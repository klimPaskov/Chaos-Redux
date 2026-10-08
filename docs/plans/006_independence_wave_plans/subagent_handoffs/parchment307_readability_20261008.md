# Event 006 compromise-report readability

Disposition: implemented and parent reviewed at source; native parchment presentation remains unverified.
The full Event 006 goal remains active and incomplete.

The human-authorized live QA direction from October 3 requires plain text in parchment event descriptions while retaining the dynamic values.
The six specifically reported description keys were repaired in `f3f67275754d79e65cea5dad3a14bb1386d3ed9e`, with their plain nested selectors in `1857b35ab7dcba1707b2dee6fe1276b00ad4a64b`.
The parent found the same defect in the Event 006 compromise report during the continued authorized implementation.

## Source change and consumer proof

Only four keys in `localisation/english/006_independence_wave_form03_l_english.yml` change: `chaosx.nr6.307.d`, `chaosx.nr6.307.charter_without_works.d`, `chaosx.nr6.307.industrial_directorate.d` and `chaosx.nr6.307.dual_compromise.d`.
The first key loses its literal cyan/orange markup, and all four use the already defined `GetIndependenceWaveForm03AccommodationBandPlain` and `GetIndependenceWaveForm03IntegrationBandPlain` selectors.
The three conditional descriptions are selected by `events/006_independence_wave.txt:620` for their exact charter outcome.
The base description key is retained; it is not presented as a new native fallback branch.
The event definition, outcomes, option, tooltip, costs and AI are unchanged.

The plain selectors in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt:2072` and `:2257` each have eleven text branches.
Their branch predicates match the existing coloured selectors exactly after normalising only the selector name and plain return-key suffix.
All twenty-two plain return values retain the numeric display and band wording after removing colour markup from their corresponding coloured values.
The captured [source projection](../evidence_20261008/parchment307/source_projection.json) records the four original lines, before/after file hashes and this equivalence boundary.
This is a source comparison, not execution of the dynamic values in the game.

## References and MCP limits

The offline wiki `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, Colouring characters, lines 124–165, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, describes the section-sign colour codes and resets.
Installed vanilla documentation comments in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/00_scripted_localisation.txt`, lines 1–34, describe `defined_text`, ordered `text` entries, trigger scope and `localization_key` lookup.
That installed file has SHA-256 `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587`.
Vanilla `localisation/english/dod_events_l_english.yml:731`, `DOD_yugoslavia.181.d`, is a plain event description with dynamic country-name expressions.
The context route also identified installed localisation formatter/object documentation; the unrelated formatter examples do not establish a colour or native parchment rule.
The live readability direction and the pertinent offline colouring section establish this presentation choice.

The [MCP metadata](../evidence_20261008/parchment307/mcp_metadata.json) retains the corrected two-node/depth-one inspect request and its partial result at revision `e59ab758e239e5ea62d20e5c085f4aa12ec8c39fae3ec9dac0d5ddca379ebd2d`.
The inspect request started before the localisation edit, but its result was consumed afterward; it is not a frozen localisation baseline.
The first request's depth-zero argument was rejected by live schema validation, then corrected to depth one.
The post-edit neighborhood render at revision `01552eecfb0cf3c61c5f5f86c0ca3771a2678552e40155113944bc93a038c3d9` selects the event, its option and terminal, with three nodes shown, 46,288 omitted and no expanded helpers.
Its [manifest](../evidence_20261008/parchment307/event-neighborhood-01552eecfb0c-manifest.json), [JSON](../evidence_20261008/parchment307/event-neighborhood-01552eecfb0c.json), [SVG](../evidence_20261008/parchment307/event-neighborhood-01552eecfb0c.svg) and [PNG](../evidence_20261008/parchment307/event-neighborhood-01552eecfb0c.png) were retained with matching returned hashes.
The parent viewed the PNG; it is a source event-chain diagram and does not render parchment text.
Helper/lifecycle projections remain deferred by the domain result.
The comparison request returned `JOB_WORKER_EXIT` without publishing a terminal comparison, and the narrower three-node retry returned `EVENT_REVISION_NOT_CACHED` for the retained before revision, with zero artifacts.
The [comparison record](../evidence_20261008/parchment307/comparison.json) preserves both outcomes.
No native rendering or successful comparison is inferred from the source-equivalence check.

## Remaining gates and scope

No asset, gameplay, focus, decision, AI, workbook or admission change belongs to this repair.
No simplification is introduced in this bounded source change.
Native presentation and the wider imported-focus, GUI, AI/balance, portrait and whole-event gates remain open.
Skills used: `chaos-redux-events` and `chaos-redux-shared-git-commit`.
