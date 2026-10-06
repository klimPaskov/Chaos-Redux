# Event 013 report and news localisation handoff

Disposition: `superseded` by [the Event 013 report/news implementation handoff](../2026-10-05_report_news_implementation_handoff.md); the source and localisation changes described here are retained as an earlier audit record.
Acceptance basis: parent delegation dated 2026-10-05 authorizes country aggregate reports, one news event per sequence, short period prose, plain parchment, and removal of report bookkeeping.

Current correction: only supplemental report `.100` is used by normal report dispatch and it calls `GetNaturalDisasterReportBatchSummary`. The family reports `.101–.125` remain isolated, uncalled event definitions with neutral acknowledgement options; they are not the active aggregate delivery path. The current mixed summary chooses two actual families, identifies additional hazards when present, reports civilian deaths without exact totals, names measured damaged systems, and combines all active same-sequence recovery needs in one paragraph. Meteor impact land/ocean copy is selected only when the batch has a uniform recorded origin medium. `.100`'s neutral title does not claim that the recipient itself was struck, because caller and global policies can deliver reports to observers.

## Changed files and coverage

Changed `localisation/english/013_natural_disasters_l_english.yml` and this handoff only.
Reviewed report IDs 101-125, added 100, and reviewed news IDs 201-225 including the meteor getter outputs.
All 25 family report bodies identify affected places through the country batch state-list getter.
Family key suffixes follow `natural_disaster_family` constants, including `extreme_wind`, `dust_and_sandstorm`, `dry_mass_movement`, and `wet_mass_movement`.
No gameplay, GUI, spreadsheet, asset, or source spec edits were made.

## Display and prose changes

Vagueness: replaced abstract disruption categories with roads, railways, factories, ports, quays, airfields, extraction sites, and stores.
Bloat: replaced the report summary ledger with a short family paragraph and conditional damage and recovery sentences.
Obvious explanation: removed active-report severity assessments, casualty totals, preparation outcomes, follow-up schedules, and recovery-phase labels from descriptions.
Repetition: country report titles identify the recipient while the body identifies affected states.
Overcomplication: replaced the meteor ocean description's locked-basin and named-state explanation with the observed offshore flash and blast.
Style repair: report bodies and revised news use complete sentences with concrete subjects, plain parchment text, and family-specific physical details.
News rupture and moving-storm copy no longer asserts that a physical path is still advancing after currently scheduled jobs have resolved.
Report 121's option no longer assumes a land crater when an ocean impact supplied the report.
Existing ledger keys remain defined for source compatibility but are no longer reached by the active report descriptions.

## Dynamic contract and owner handoff

The active report `.100.d` calls `[This.GetNaturalDisasterReportBatchSummary]` in recipient-country scope.
`natural_disaster.report.batch.summary` calls the family-body, civilian-death, measured-damage, and combined-recovery getters.
State list keys one/two/three/four/many use the exact parent-supplied array/index contract.
The many case names the first four states and gives the exact omitted count.
Damage present calls `GetNaturalDisasterReportBatchDamageList`, whose owner must preserve first-item and comma selection.
Damage none and recovery none are empty.
Recovery rescue, stabilization, and reconstruction needs are joined into one concise paragraph without phase labels.
Meteor land and ocean variants are selected from recorded same-sequence origin media; the neutral meteor family key is used for mixed or missing medium.
The owner must verify that serialized active indexes remain frozen for an open report and that damage/recovery sentences describe the same report batch.

## Audit findings

Missing keys: the six agreed batch getters and new mixed report originally had no matching English keys, supplied here.
Duplicate keys: none found in the owned English file.
Scripted localisation issues: new getter wiring belongs to the parent and was pending at this handoff.
Dynamic text opportunities: affected states, hidden-state count, family, damage categories, and active recovery needs are supplied through the agreed batch contract.
Cross-surface mismatch: source specs retain per-impact report and repeated news direction, superseded by the parent's accepted aggregate release repair.
Catalog wording was not edited or checked from an export and requires no report/news mirroring, because this patch does not change event-detail/evolution-detail/cluster text.
Encoding concerns: none found in the owned file.
Sourced quotations: none occur on the assigned report/news surfaces, and no quotations were changed.
Dynamic tokens in retained news strings were preserved.
Legacy report-summary ledger tokens were intentionally removed from the active display path under the parent's accepted decision.

## Evidence and validation limits

The supplied `evt013_pop03_view.png` shows the pre-fix Puerto Rico heat popup with colored date and death ledger text and dense status lines.
It predates commits ff1f29862 and f5b1e494a and is contextual evidence, not proof of the final display.
`python .tools/report_colour_audit.py --event 013` reports zero reachable keys with color.
Task-specific local checks verified all 26 report descriptions use the agreed country getter, all 25 family bodies call the state-list getter, all five state-list templates use the supplied dynamic contract, and all 64 damage-category combinations keep proper first-item and comma grammar.
MCP `reference_context(surface=localisation, limit=5)` and `event_inspect(mode=trace, selector={id:chaosx.nr13.120}, maxDepth=1, maxNodes=5)` remained stalled with no result after several minutes.
The parent directed the agent to stop waiting and use local source references.
No MCP artifact URI or source revision was returned.
MCP render and compare were skipped because inspection returned no usable result, so overflow and final event-render coverage remain unresolved and source review is not equivalent evidence.
No focus, GUI, map, or technology surface was edited.
A separate tool-list search found no standalone Technology Tree Viewer route, recorded as a package gap unrelated to this bounded text patch.
Local offline reference: `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, snapshot 2026-09-19, lines 59-93 for encoding and syntax, 534-536 for scope namespaces, and 564-573 for names.
Installed reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, lines 126-141 for contextual object access.
Vanilla precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/00_scripted_localisation.txt`, lines 1-33 for scoped defined_text and fallback localisation keys.
Reference file SHA-256 revisions are listed below.

- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`: `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`: `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/00_scripted_localisation.txt`: `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587`

## Changed keys

- `natural_disaster.report.summary`
- `natural_disaster.report.origin.land_impact`
- `natural_disaster.report.origin.atmospheric_fragmentation`
- `natural_disaster.report.origin.skyfire`
- `natural_disaster.report.origin.ocean_impact`
- `natural_disaster.report.meteor_title.land`
- `natural_disaster.report.meteor_title.ocean`
- `natural_disaster.news.meteor_desc.ocean`
- `natural_disaster.report.damage.transport`
- `natural_disaster.report.damage.industry`
- `natural_disaster.report.damage.industry.next`
- `natural_disaster.report.damage.ports`
- `natural_disaster.report.damage.ports.next`
- `natural_disaster.report.damage.air`
- `natural_disaster.report.damage.air.next`
- `natural_disaster.report.damage.resources`
- `natural_disaster.report.damage.resources.next`
- `natural_disaster.report.damage.none`
- `chaosx.nr13.101.t`
- `chaosx.nr13.101.d`
- `chaosx.nr13.102.t`
- `chaosx.nr13.102.d`
- `chaosx.nr13.103.t`
- `chaosx.nr13.103.d`
- `chaosx.nr13.203.d`
- `chaosx.nr13.104.t`
- `chaosx.nr13.104.d`
- `chaosx.nr13.105.t`
- `chaosx.nr13.105.d`
- `chaosx.nr13.205.d`
- `chaosx.nr13.106.t`
- `chaosx.nr13.106.d`
- `chaosx.nr13.206.d`
- `chaosx.nr13.107.t`
- `chaosx.nr13.107.d`
- `chaosx.nr13.108.t`
- `chaosx.nr13.108.d`
- `chaosx.nr13.109.t`
- `chaosx.nr13.109.d`
- `chaosx.nr13.209.d`
- `chaosx.nr13.110.t`
- `chaosx.nr13.110.d`
- `chaosx.nr13.110.a`
- `chaosx.nr13.210.d`
- `chaosx.nr13.111.t`
- `chaosx.nr13.111.d`
- `chaosx.nr13.112.t`
- `chaosx.nr13.112.d`
- `chaosx.nr13.113.t`
- `chaosx.nr13.113.d`
- `chaosx.nr13.114.t`
- `chaosx.nr13.114.d`
- `chaosx.nr13.115.t`
- `chaosx.nr13.115.d`
- `chaosx.nr13.116.t`
- `chaosx.nr13.116.d`
- `chaosx.nr13.117.t`
- `chaosx.nr13.117.d`
- `chaosx.nr13.217.d`
- `chaosx.nr13.118.t`
- `chaosx.nr13.118.d`
- `chaosx.nr13.119.t`
- `chaosx.nr13.119.d`
- `chaosx.nr13.120.t`
- `chaosx.nr13.120.d`
- `chaosx.nr13.121.t`
- `chaosx.nr13.121.d`
- `chaosx.nr13.121.a`
- `chaosx.nr13.122.t`
- `chaosx.nr13.122.d`
- `chaosx.nr13.222.d`
- `chaosx.nr13.123.t`
- `chaosx.nr13.123.d`
- `chaosx.nr13.223.d`
- `chaosx.nr13.124.t`
- `chaosx.nr13.124.d`
- `chaosx.nr13.125.t`
- `chaosx.nr13.125.d`
- `chaosx.nr13.225.d`
- `chaosx.nr13.100.t`
- `chaosx.nr13.100.d`
- `chaosx.nr13.100.a`
- `natural_disaster.report.batch.summary`
- `natural_disaster.report.batch.family.mixed`
- `natural_disaster.report.batch.damage.present`
- `natural_disaster.report.batch.damage.none`
- `natural_disaster.report.batch.recovery.rescue`
- `natural_disaster.report.batch.recovery.stabilization`
- `natural_disaster.report.batch.recovery.reconstruction`
- `natural_disaster.report.batch.recovery.none`
- `natural_disaster.report.batch.family.earthquake`
- `natural_disaster.report.batch.family.flood`
- `natural_disaster.report.batch.family.tropical_cyclone`
- `natural_disaster.report.batch.family.extreme_wind`
- `natural_disaster.report.batch.family.tornado_outbreak`
- `natural_disaster.report.batch.family.thunderstorm`
- `natural_disaster.report.batch.family.hailstorm`
- `natural_disaster.report.batch.family.blizzard`
- `natural_disaster.report.batch.family.cold_wave`
- `natural_disaster.report.batch.family.heat_wave`
- `natural_disaster.report.batch.family.drought`
- `natural_disaster.report.batch.family.dust_and_sandstorm`
- `natural_disaster.report.batch.family.wildfire`
- `natural_disaster.report.batch.family.dry_mass_movement`
- `natural_disaster.report.batch.family.wet_mass_movement`
- `natural_disaster.report.batch.family.volcanic_eruption`
- `natural_disaster.report.batch.family.ashfall`
- `natural_disaster.report.batch.family.lahar`
- `natural_disaster.report.batch.family.tsunami`
- `natural_disaster.report.batch.family.storm_surge`
- `natural_disaster.report.batch.family.meteor_impact`
- `natural_disaster.report.batch.family.meteor_shower`
- `natural_disaster.report.batch.family.whole_earth_rupture`
- `natural_disaster.report.batch.family.massive_eruption`
- `natural_disaster.report.batch.family.moving_storm_corridor`
- `natural_disaster.report.batch.states.one`
- `natural_disaster.report.batch.states.two`
- `natural_disaster.report.batch.states.three`
- `natural_disaster.report.batch.states.four`
- `natural_disaster.report.batch.states.many`
- `natural_disaster.report.batch.family.meteor_impact.land`
- `natural_disaster.report.batch.family.meteor_impact.ocean`

## Remaining decisions and risks

No unresolved prose choice remains.
Getter selection, event 100 source addition, queue serialization, aggregate origin selection, and final MCP inspection/render/compare remain parent-owned integration and validation.
No new mechanics or fallback design were invented.
Skills used: chaos-redux-events and chaos-redux-subagents.
