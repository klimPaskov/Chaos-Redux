# Event 006 parchment report readability

Disposition: implemented, source parity checked, post-fix live rendering remains unobserved.
Acceptance basis: the user-authorized orchestrator reported unreadable yellow text on the light parchment report at 1080p on 2026-10-03 and requested plain text for six exact Event 006 description keys.

Removed 20 colour-control tokens from `chaosx.nr6.2.d`, `chaosx.nr6.300.d`, `chaosx.nr6.302.d`, `chaosx.nr6.305.d`, `chaosx.nr6.306.d`, and `chaosx.nr6.308.d`.
All bracketed dynamic expressions and all prose remain identical.
The independent `chaosx_localisation_auditor` confirmed all 13 dynamic bracket expressions and every other line in both files match HEAD `090983ebfc0ab7952d370f1c55539ea0544b43ca`.
The diff changes exactly those six lines in `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/006_independence_wave_form03_l_english.yml`.
Option names, tooltips, decisions, and GUI strings retain their existing colour controls.
No gameplay, event-chain, asset, or catalog wording changes are involved, so this narrow formatting correction does not alter their source contracts.
No simplifications were made within this correction.
The wider Event 006 implementation remains incomplete.

## Reference evidence

Local sections were read directly while decision-reference MCP retrieval was pending.
The wiki defines each colour control as the section sign plus one character and identifies the reset control.
Installed documentation covers contextual object/property expressions and relation to event scopes.
The installed Mexico event descriptions retain dynamic country and leader expressions in plain prose.
These precedents support preserving the dynamic values while removing their surrounding colour controls.

## Dynamic return-value follow-up

The first literal-string correction is committed as `f3f67275754d79e65cea5dad3a14bb1386d3ed9e`.
A subsequent consumer audit found four shared helpers returning coloured values into those descriptions.
That first patch alone did not fully remove colour from the resulting report text.
The source correction adds four plain selectors with the same branch order, triggers, scopes, and numeric expressions, plus 24 plain return strings.
Only `.2.d`, `.300.d`, and `.306.d` need the plain selector names, and the other three named descriptions already have plain dynamic returns or no getter.
The original selectors, their coloured return strings, and dark option, tooltip, decision, and GUI consumers remain unchanged.
The independent localisation auditor confirmed exact parity across selector branch counts of two, two, 11, and 11, plus colour-free authored returns and five nested band substitutions.
The parent's recursive check covers 58 description, return, and nested substitution keys.
An incidental registry line-ending change found by the auditor was removed before commit, preserving the original registry as a byte-identical prefix.
Country-name output from `.305.d` and actual rendered appearance remain runtime evidence limits.
No simplification or substitute was used.

The follow-up reads offline Localisation lines 656-689, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, through the connected reference-search/read routes.
The localization context with limit ten reports no omitted or missing sources.
Installed contextual localization and scope documentation at the revision above remains pertinent to the preserved object expressions.
Vanilla `common/scripted_localisation/WTT_infiltration_localisation.txt:10-36` supplies the inspected ordered selector precedent.
The completed plain-selector source tranche is committed as `1857b35ab7dcba1707b2dee6fe1276b00ad4a64b`.
Generic `hoi4.source_lookup` for `GetIndependenceWavePresentationArmedTextPlain` returned zero definitions at catalog revision `57150c7cc227e5f41be0aafe23f6ad30965aa88ddeb13e6e3eca6a2cf9acc648`, although the definition is present in the inspected source.
That catalog result does not confirm namespace coverage or native rendering.
The parent and independent auditor reviewed the actual paired definitions, and the lookup result is retained in [the plain report reference evidence](../mcp/006_plain_report_reference_20261003.json).

| Source | Lines | SHA-256 revision |
| --- | --- | --- |
| `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` | 122-144 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` | 138-156 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/mtg_events_l_english.yml` | 3-8 | `4c2771e50eead349a84973b2f84f9604c30a9fb201723317d98a3586ead2c762` |
