# IW-039/DON flag reuse and affordability review (2026-09-26)

**Disposition:** accepted and queued for implementation under the user's broad implementation approval and specific instruction to complete an affordability review.

The user accepted the Millerovo host/district council, three government settlements, Event 006-only vanilla OOB suppression, one p39 force application after valid muster, separate later-gated FORM-11 scope, and conditional portrait boundary.

This review resolves the package's costs and timing from the installed state data and shared Event 006 tuning, records a no-new-flag disposition, and does not attest package implementation or runtime admission.

## Parent-selected cost contract

The charter mission lasts 420 days, matching the existing Event 006 founding-crisis benchmark used by source-complete regional packages.

The railhead survey spends 25 political power and takes the shared 75-day short project duration.

The district-petition hearing spends 20 political power and takes the shared 45-day rapid project duration.

Only one paid timed project may run at once, and the government settlement is an immediate 30-political-power choice after both success receipts and the issue-focus prerequisites exist.

The constitutional district compact additionally spends the shared light 10 command power.

The emergency host staff grants its proposed immediate 5-point war-support gain and 5-point stability loss, then opens a 90-day civilian-review window that costs 10 political power and must resolve before the charter capstone.

The elected host assembly grants 5 stability, while the constitutional district compact grants 10 stability after its command-power payment.

No paid project consumes or commits a civilian factory because neither state 245 nor optional state 238 has one.

The proposed repeatable guard purchase of 500 infantry equipment, 100 support equipment, and 5,000 manpower per cycle is excluded from this implementation because the p39 anchor-only stockpile cannot guarantee 100 support equipment.

The 10-support-equipment-per-division stockpile contract reaches 100 only at the p39 high-chaos maximum of ten divisions, while p39 allows smaller force counts and the accepted baseline requires 245-only playability.

The package continues to use the once-per-generation p39 mounted-mobile opening force and the existing reinforcement pathways without a second starting-force application.

## Conservative completion-order calculation

The model starts with zero political power, uses the vanilla base income of 2 political power per week, assumes no other Event 006 political-power spending, and serializes the two paid projects.

The common capital-administration focus takes 35 days, followed by the 5-unit authorities focus and 5-unit rail-survey focus, so the rail project can start around day 105 with the base 30 political power accrued.

After spending 25 political power on day 105, the country has about 26.4 by day 180, enough to start the 20-political-power hearing when the 75-day rail project ends.

The 45-day hearing finishes around day 225, when both receipts exist and political power has recovered to about 19.3.

The two issue focuses complete by day 140; the 7-unit service-quota focus then runs after both project receipts and completes around day 274.

Political power reaches the 30-point government cost by day 262.5, and the government choice is available when the service-quota focus completes at about day 274.

The emergency review's additional 10 political power is available around day 297.5, about 24 days after selection and well inside its 90-day window.

The 7-unit charter capstone takes 49 days, completing the normal route around day 323 and the most expensive emergency-review route around day 347.

The emergency route therefore retains about 73 days inside the 420-day charter deadline, before any political-power spending outside this package.

This is a source-based timing model, not a simulation of a live campaign; completion ordering and AI behavior still require scenario review.

## Installed state and force evidence

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/245-Donetsk.txt:2-32` records state 245 as Millerovo, population 761,769, infrastructure 3, victory point province 11476, no factory buildings, and local supply 8.0; SHA-256 `0C3FBC95B82B9AC89AB4ACFF2F000A4D9E7A822F644306E8ED1C96823E3B4FEB`.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/238-volgodonsk.txt:1-29` records state 238 with population 556,677, infrastructure 2, no factory buildings, and local supply 0.0; SHA-256 `AD5BABFFA4BFA6AD15C596ABB7D2EA26EAA88064D163F971EC10E3EDF0496080`.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/units/DON_cossack_host.txt:1-185` defines fifteen opening divisions with template `Kavaleriyskaya Diviziya`, including a unit located in state 218; SHA-256 `9C53DD97D9270E5B9C1EE3198B1D30B00C3A0207D72569573BB9E25182E2D18F`.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/DON - Don Republic.txt:1-90` is the vanilla DON history source for capital 218, vanilla starting politics, two research slots, and `DON_vladimir_sidorin`; SHA-256 `1E6F0806D11567B458A4E3B7CEA09B6561328B9DD86E4EA20D988C6A2371E4CC`.

`common/script_constants/006_independence_wave_constants_registry.txt:992-1007` defines the shared 45/75/120/180-day decision-duration ladder; the review selects its 45-day rapid and 75-day short entries.

`common/script_constants/006_independence_wave_constants_registry.txt:1799-1934` defines the force-budget and p39-relevant opening-stockpile inputs, including 10 support equipment per division and the high-chaos force-count ceiling of ten.

`common/script_constants/006_independence_wave_constants_registry.txt:2066,2280,2494,2708` maps p39 to mounted-mobile profile 6, tradition 82, reinforcement mask 654, and inheritance mask 0.

`common/scripted_effects/006_independence_wave_force_effects.txt:871-891` is the current-generation-gated public entry point for dynamic starting-force creation.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/defines/00_defines.lua:441,443,725` sets initial command power to 0, base command-power gain to 0.4 per day, and base political-power gain to 2 per week; SHA-256 `405A24CE579815443CAFE052CFF1361E20C712CA8182E3F10CCBF45330DD4BE4`.

## Engine-reference route and source evidence

Live tool discovery found no `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, or `hoi4.source_lookup` route, so the pertinent local offline wiki and installed-game sections were read directly.

The offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:294-335,455-520` documents custom-cost payment, the required political-power AI hint, decision timers, and mission activation/completion/timeout behavior; SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.

The offline `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:820-824` documents root-level shared-focus definitions and imports; SHA-256 `BD989A13237C464F140A0AA671CC42C30A48E84A27DAE791B8914654FB9C6203`.

The offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:2047-2049,2212-2218` documents exact-template `delete_units` use; SHA-256 `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C`.

Installed `documentation/effects_documentation.md:3278-3295,3506-3517` confirms the `create_unit` and `delete_units` effect scopes and syntax; SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.

Installed `documentation/script_concept_documentation.md:216-245` and `common/script_constants/documentation.md:15-31` document shared script-constant support and schema; SHA-256s `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` and `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C`.

The current focus MCP can inspect and render the direct Event 006 tree, but imported `shared_focus` nodes remain omitted as previously reported in the addendum.

The current Event MCP global roots scan exceeded the two-minute wait without returning a result, and the prior narrow Event 005/006 traces remain partial at the recorded revision.

The current map inspection reports selected-state data alongside 2,654 unrelated `mod:map/buildings.txt` errors, so this review does not claim a clean map-wide validation.

## DON flag ladder disposition

The read-only asset audit verified the installed vanilla base, communist, fascist, and neutrality DON TGA flags in normal, medium, and small sizes, with no DON democratic variant.

The twelve installed vanilla TGA files match the archived copies byte-for-byte, and the base `DON.tga` SHA-256 is `e9f476fd2ab9167655aacb662a79df5b6374402e94684857dde74cb71d63fd32`.

Vanilla selects the ladder from the existing DON tag and ideology filenames, so this package adds no flag sprite, `.gfx` wiring, cosmetic tag, or image asset.

The existing flag source and asset records are `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw039_flag_asset_handoff_2026_08_12.md`, `docs/assets/006_independence_wave/iw039_don_flag_reuse_2026_08_12/manifest.md`, and `docs/assets/006_independence_wave/iw039_don_flag_reuse_2026_08_12/gfx_handoff.md`.

## Remaining limits

This review does not prove live campaign resource accrual, state-control transitions, emergency-review AI timing, force spawn placement, or cleanup behavior.

The Sidorin portrait remains blocked, the imported-focus layout evidence remains blocked, and FORM-11 has no accepted carrier.

IW-039 stays **HOLD / PARTIAL** until source implementation, post-change package/focus/decision/localisation/event/probability audits, and scenario evidence are complete.
