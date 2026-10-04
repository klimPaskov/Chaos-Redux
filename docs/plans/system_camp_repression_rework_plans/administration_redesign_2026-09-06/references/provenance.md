# Camp administration UI reference provenance

Status: the four original generated reference images and the Locations v3 resource-locked and v4 records-locked images are archived for the accepted implementation in [`../accepted_implementation.md`](../accepted_implementation.md); parent review of the current PNGs is complete.

Acceptance basis: the user accepted the implementation plan and requested clean HOI4-style references for Administration, Locations, Records, and a material-shortage state before native GUI edits.

These PNGs are generated visual targets, not gameplay screenshots or historical evidence. They use synthetic scenario text and values constrained to the current GUI's supported data; each fact that comes from a constructed visual fixture is identified below.

The official ImageGen tool produced the final 1672×941 opaque PNGs. Their generated source files and archived reference files are byte-identical, as shown by matching SHA-256 values. The generated references use a restrained vanilla-style dark steel and document palette, and are for layout, hierarchy, density, and status colour guidance only.

The four reference images were opened and visually inspected at source scale. The parent confirmed the Administration, Records, Locations, and shortage references as visually clean or acceptable after the corrections recorded here.

A later [postqualified four-image set](postqualified_2026-09-27/provenance_handoff.md) uses the now-populated vanilla Decisions and Occupied Territories MCP crops together with route-declared Chaos Redux Administration, Locations, Records and shortage crops. The parent inspected all four 900×540 PNGs at original resolution: the visible labels, values, three tabs, six Locations rows, four contextual actions, cause arithmetic and two shortage actions are legible without clipping or invented controls. This set is a design-reference update and cannot retroactively make the original images precede initial GUI editing; its synthetic-fixture and source-hash limits remain in that handoff.

| View | Archived PNG | Resolution | SHA-256 | Generated source PNG |
|---|---|---:|---|---|
| Administration | `camp_admin_administration_reference.png` | 1672×941 | `CE03C2B104FB396257C3722EFA704932CE3BE1F1C4F7D8379AA5B1D3BE82D8E9` | `C:\Users\klimp\.codex\generated_images\01a0d868-dd8c-7982-b313-550419978650\exec-4ef070c4-ff0c-445a-947a-7a973f1e7eee.png` |
| Locations | `camp_admin_locations_reference.png` | 1672×941 | `994C8EBE12030E34B6B6E6450EC40C248344A0FF99E44623998E3A3D1C173EFB` | `C:\Users\klimp\.codex\generated_images\01a0d868-dd8c-7982-b313-550419978650\exec-a131732b-ee5d-4df8-8266-23e23f7e249c.png` |
| Records | `camp_admin_records_reference_v2.png` | 1672×941 | `D047257ECC1151EB0783EE63D7E562047C1775094B2CE4008BD0DE1086C0644D` | `C:\Users\klimp\.codex\generated_images\01a0e2d4-c0c2-7472-9455-3cc0e7ac6cd3\exec-0c4fe957-d810-4e3b-bf34-ed4fc315e2f7.png` |
| Shortage | `camp_admin_shortage_reference.png` | 1672×941 | `64C87B9253A04047559EC0D4A3126FC5E40C5C5F7549565599E1B8693B8BA5EA` | `C:\Users\klimp\.codex\generated_images\01a0d868-dd8c-7982-b313-550419978650\exec-2dfa62f1-981e-4f83-a210-dd0bda879f9c.png` |

The additional four-control Locations image is [the resource-locked v3 reference](camp_admin_locations_resource_locked_reference_v3.png), 1672×941 RGB, SHA-256 `30173E38A6A445B22EAC5080F8504323CC48EB8368D2A4C0DC104F73F217952C`. Its [ImageGen handoff](camp_admin_locations_resource_locked_reference_v3_handoff.md) records the v2 source and changed button. A post-generation source review corrected its rationale: living custody can be released by an accepted dismantlement start, so v3's neutral face represents insufficient resources for the current quote. The matching [three-scale resource-lock review](../mcp/locations_resource_locked_actions_2026-09-27.md) is the native geometry target; the earlier custody-only locked fixture is rejected. The original four-image table remains the initial design set, while v3 is an additional valid blocked-state reference.
The [records-locked v4 reference](camp_admin_locations_records_locked_reference_v4.png), 1672×941 RGB, SHA-256 `21919D937F04BB6FF30C0E1499ABA80759A3976A298343729D5A17B9957A2BA5`, adds a neutral Release Locked face and a custody-record reconciliation status to the same composition. Its [ImageGen handoff](camp_admin_locations_records_locked_reference_v4_handoff.md) records the exact source and output hashes and edited regions. The selected-release trigger and `GetCampAdminSelectedConditions` now supply those two native states; the image remains a design reference, not an engine screenshot.

## Fixture values and visual provenance

### Administration

The selected view is the pre-authorization state: 0% economic contribution, 200 thousand in custody, 0 assigned workforce, 1.24 thousand deaths this month, no authorized economic project, no authorized institutional program, and the actions `Authorize camp administration` and `Close camps and release survivors`.

The country tag used for the adjacent MCP baseline is GER. The final image is a generated design scenario, not a one-to-one rendering of that baseline; no date is displayed or asserted by the reference.

For consistency, the 200 thousand custody total and 1.24 thousand monthly deaths are illustrative pre-authorization country values. The image does not claim that those values belong to an authorized paid network.

### Locations

The selected synthetic site is Brandenburg, with role `Forced-labor institution`, 14,800 people in custody, 9,620 assigned workers, 100% site support, 1.24 equivalent factories of industrial contribution, 74 deaths this month, and 345 cumulative deaths. The status line reads `Maintenance obligations are covered.` The original image shows the three actions `Pause Work`, `Change Purpose`, and `Release Survivors`; v3 adds a fourth neutral `Closure Locked` face for an insufficient current closure quote, while maintenance already paid remains covered.

The left list shows Brandenburg, Upper Silesia, Saxony, Lower Silesia, Pomerania, and Rhineland. East Prussia is below the visible roster and omitted from the image because the generation output misspelled its name; the native list may still scroll to it.

The site values are synthetic illustration values aligned with available fixture variables; they are not historical counts. The original image omitted capacity because that first fixture did not supply an exact value; the v3 and its current-source MCP fixture show 18 thousand. No map thumbnail is shown because the current GUI has no map consumer.

### Records

The table is country-level and uses one row per supported cause, with synthetic May 1942 monthly and cumulative fixture values. The corrected monthly values are custody 100, forced labor 707, site violence 0, institutional programs 0, and occupation violence 400, for a total of 1,207. The cumulative values are 421, 1,865, 0, 0, and 6,233, for a total of 8,519. An active German May 1942 administration has no Auschwitz-linked institutional deaths under the current historical gate; the 33/33 institutional row in the previous image was an unsupported fixture claim.
The earlier label iterations remain as `camp_admin_records_reference_before_label_fix.png` and `camp_admin_records_reference_before_site_violence_label.png`. `camp_admin_records_reference.png` preserves the previous 33/33 arithmetic and closure-status draft; the [v2 ImageGen handoff](camp_admin_records_reference_v2_handoff.md) records the corrected May 1942 totals and active status. The current v2 image was inspected at full resolution with every total adding to its cause rows.

The monthly cause fixture corresponds to `camp_admin_month_custody_deaths_k`, `camp_admin_month_labor_deaths_k`, `camp_admin_month_violence_deaths_k`, `camp_admin_month_institutional_deaths_k`, and `camp_occ_month_deaths_k`. The cumulative values correspond to the country totals `camp_admin_total_custody_deaths_k`, `camp_admin_total_labor_deaths_k`, `camp_admin_total_violence_deaths_k`, `camp_admin_total_institutional_deaths_k`, and `camp_occ_total_deaths_k`.

The displayed authority/status is `German national administration` and `active administration`. The synthetic history rows are `Institutional authority reviewed — Upper Silesia — May 1942`, `Spending ceiling changed — National administration — April 1942`, and `Economic project completed — Brandenburg — March 1942`; these correspond to the supported `authority`, `budget`, and `economic_project` history kinds. No death-record history kind or per-location loss table is implied.

The route fixture supplies no current-game date override, so May 1942 is the illustrative month in this design image, not a claim about the live game date. The generated table is a country-level layout guide; the exact final labels, values, and row controls must be wired to the current country totals and source variables.

### Shortage

The shortage state is an embedded crisis panel. It shows a 54% country support ratio, new development deferred, and `Maintenance support is below current commitments.` The two actions are `Review Spending` and `Defer New Projects`.

The background synthetic fixture shows 20% industrial output, 200 thousand people in custody, 130 thousand assigned workers, 1.24 thousand deaths this month, and an inherited Brandenburg industrial contract at 62% completion. The reference premise is that these are legacy-network records while `Authorize camp administration` offers a separate new paid authority; this reconciles the displayed values without asserting that the button starts or funds the legacy network.

The crisis copy and controls align with the current `camp_admin_maintenance_shortage` state, support ratio, deferred-development state, and the native `Review Spending` and `Defer New Projects` actions. No steel amount, reserve duration, affected-site count, named machinery works, or separate modal is shown.

## MCP image evidence

The MCP images are separately archived under [`../mcp/`](../mcp/). Both successful captures are offline MCP renderer artifacts from `mod:interface/camp_repression_ledger.gui`, not live-game screenshots. Their images were actually opened and visually inspected.

| Scenario | Result | Route details | Artifact |
|---|---|---|---|
| `camp_admin_preview_administration` | Rendered successfully and visually inspected. | GER; 1920×1080; UI scale 1; normal state; `l_english`; Administration visible; Locations, Records, and crisis panel hidden. The exact scenario fixture is [`../mcp/camp_admin_preview_administration.json`](../mcp/camp_admin_preview_administration.json). The fixture describes a legacy funded network, including 200k custody, 130k workforce, 20% output, and a 62% Brandenburg contract, while the new paid authority action remains available. | SVG artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee9b4ab8477514f9420204c93393553d1dd52401946662056f7fbc040fc5f3bf/afa5044e026a334c1fdf6f0434a4913d65cd75324db9c607f24a156087bb5c2c/repression_ledger_window-full.svg`; archived as `repression_admin_current.svg` and `repression_admin_current.png`. |
| `camp_admin_preview_records` | Rendered with `GUI_RENDERED`, no blockers, and empty diagnostics; `validation.passed` was false with an empty checks array. The resulting PNG was visually inspected. | GER; 1280×720; UI scale 1; normal state; `l_english`; Records visible; Administration, Locations, and crisis hidden; generated scenarios disabled. The original exact tool payload was not saved. Existing [`../mcp/camp_admin_preview_records.json`](../mcp/camp_admin_preview_records.json) is an older 1920×1080 starting fixture and is not the exact 1280×720 render payload. | SVG artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0913c33185eae69aff6f608a1c8c7193bd3eea936776ab5c14c44e95b1f65091/e8c3ba806e4dafb5c3c5ecbf363c7d03e8a00ffdc694bc2f108e41d98a474a80/repression_ledger_window-full.svg`; archived as `repression_records_current.svg` and `repression_records_current.png`. |
| `camp_admin_reference_locations_1280` | Not accepted as render evidence. The call returned diagnostics only, without status, code, or artifact URI. | GER; 1280×720; UI scale 1; Locations and selected panel visible; generated scenarios disabled. The attempted request is [`../mcp/camp_admin_reference_locations_1280.json`](../mcp/camp_admin_reference_locations_1280.json), but its `Authorize work` label was later identified as wrong and does not describe the final reference. | No render artifact. |
| `camp_admin_locations_ger_1942_06_01` | Timed out after 180 seconds; no artifact. | GER; 1920×1080; UI scale 1; generated scenarios disabled. This route failure is not evidence of a successful render. | None. |

The successful MCP SVG metadata identifies the source path as `mod:interface/camp_repression_ledger.gui`, but the render response did not expose a source revision or commit identifier. The artifact hashes and URIs above are the available artifact identities; do not describe them as source revisions.

The earlier connected GUI scenario object accepted `id`, `description`, `country`, `resolution`, `uiScale`, `state`, `language`, `animationTimeSeconds`, `values`, `visibility`, `lists`, `elementStates`, and `expectations`; its attempt to pass `scenario.date` was rejected as unrecognized. The later installed MCP 3.5.1 qualification accepts declared `date` and `controls` fields, as recorded in [the reconciled schema evidence](../mcp/mcp_3_5_1_reconciliation/reconciliation.md) and [the custody-locked Locations review](../mcp/locations_custody_locked_actions_2026-09-27.md). Those are declared fixture facts and do not establish a live campaign state. The original Records render’s May 1942 chronology was provided through the history row month/year values, not as a live game date.

The successful Records render used scenario id `camp_admin_preview_records`, GER, 1280×720, UI scale 1, normal state, `l_english`, zero animation time, the Records panel and Records tab marker visible, Administration, Locations, and crisis panels hidden, and generated scenarios disabled. The original full request payload existed only in the transient MCP call and was not archived. The saved `camp_admin_preview_records.json` is a 1920×1080 starting fixture with different visibility and history rows, so it is not an exact replay copy. The actual successful render remains preserved in `repression_records_current.svg` and `.png`.

The offline renderer reports approximations including 1920×1080 source-coordinate scaling for the 1280×720 Records capture, primary sprite frames only, and substitute font paths because font metrics are not supplied. Its metadata also says scripted-GUI visibility needs an explicit scenario mock and otherwise remains visible. These limitations do not erase the successful artifact or the visual inspection, but the images are not live-engine acceptance evidence.

### Vanilla GUI attempts

The initial qualification obtained no usable populated vanilla `countrydecisionview` or `countryoccupationview` artifact. Initial inspect attempts omitted the required `scenario.id` and failed schema validation; after the corrected scenario shape, an earlier populated `countrydecisionview` render timed out after 180 seconds. A later `countrydecisionview` inspect with `animationTimeSeconds = 1`, GER, 1920×1080, and an explicit two-entry decision-grid mock returned `GUI_INSPECTED`, but diagnosed the 550×1080 window clipped to 0×0 at the vanilla source position `x = -606`. A render with the same opening time returned `GUI_RENDERED` but its full PNG was a blank navy canvas; a direct `decisionview_title` fixture override was interpreted as a sprite and raised `GUI_SPRITE_MISSING`. This is a rejected fixture and not a populated reference. The renderer returned the blank PNG artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/fa25dd48ca14c7075493609bedd2c291bb260ee9d1b4ddf41db2a6e77e22b783/countrydecisionview-full.png` only as failure evidence.
The nested vanilla `decision_grid_container` was then inspected by its exact name and returned `GUI_INSPECTED` with one selected element, but a direct child render inherited the offscreen parent transform and returned another blank navy PNG with SHA-256 `397D44367A8A781890CA2BC55C286A9B4F1F5D87D08BBE82D9D756820`. A child locator is therefore not a populated vanilla reference either.

A corresponding GER, 1920×1080, `animationTimeSeconds = 1` `countryoccupationview` render returned `GUI_RENDERED` but diagnosed that window and its background clipped to 0×0 at the same `x = -606` vanilla starting position. Its blank full PNG has the same hash as the blank decision image; generated fixture text also produced two `GUI_MISSING_LOCALISATION` diagnostics for unsupported values. Neither image is treated as a visible vanilla screen. The connected scenario schema has no position or show-state override, and `animationTimeSeconds = 1` did not apply `show_position = { x = -6 y = 78 }` in these calls.

The canonical vanilla reference root was checked for the relevant family, and the required offline wiki and vanilla GUI documentation were consulted. That initial image family had no usable captured vanilla reference, so the generated images are not claimed as direct vanilla screenshot reproductions; the later populated MCP source renders are separate evidence.

Installed MCP 3.5.1 later produced and archived both populated vanilla windows at their onscreen `show_position` endpoints. The [Decisions and Occupied Territories qualification](../mcp/vanilla_reference_2026-09-27/README.md) retains explicit country/date/control fixtures, original images and click overlays, raw installed-source hashes and the remaining engine limits. The Decisions image contains one source-eligible English action; the Occupied Territories image uses a declared German two-state Polish remnant, vanilla Forced Labor law and dashes for unavailable runtime quantities. These renders inform the final reference family but were captured after the original four design images and native edits, so the requested evidence order was not met retroactively.

## Excluded or corrected claims

The original Locations image omits the unsupported map thumbnail, an unsupported `Authorize work` action, and unprovided capacity. It uses `Pause Work`, `Change Purpose`, and `Release Survivors`.
The later `camp_admin_locations_reference_v2.png` is a separate review-only image derived from that reference and a populated current-source MCP Locations render. It adds a fourth native action, `Dismantle Site`, and shows an 18-thousand selected-site capacity; its prompt, source paths, and button mapping are recorded in `camp_admin_locations_reference_v2_handoff.md`. Active Dismantle Site can be valid with 14.8 thousand living detainees when rows reconcile, authority is valid and the country can pay; the action releases those survivors at the accepted start. The resource-short v3 uses a neutral `Closure Locked` face for a different valid state.

The final Records image uses country-level causes only. It does not imply a per-location loss registry or a routed location-loss array.

The final shortage image is an embedded panel with only current support/development fields and two current actions. It does not imply an inventory of materials, reserve duration, affected-site count, or a separate modal.

The records fixture's values and chronology are synthetic display data. Source-backed variables determine availability of the causes and totals, not the displayed example values themselves.

## Native element mapping

See [`native_element_mapping.md`](native_element_mapping.md) for per-label, per-value, and per-button mapping to existing native elements, with new row controls explicitly marked as proposed where the current source has only an aggregate text element.
The later scoped Locations repairs retain the final Locations image as their layout baseline: [`location_locked_actions_reference_2026-09-26.md`](location_locked_actions_reference_2026-09-26.md) covers unavailable labels, and [`location_locked_tooltips_reference_2026-09-26.md`](location_locked_tooltips_reference_2026-09-26.md) maps the reason-specific native controls and current MCP baselines. Neither document creates a new painted asset or changes the four original ImageGen references.
The [paused shortage action reference](shortage_paused_action_reference_2026-09-26.md) uses the existing shortage image and an archived disabled-state MCP baseline to map the neutral `Projects Deferred` native control. It adds no painted asset or fifth ImageGen reference.
The [national authorization locked-state reference](national_action_locked_reference_2026-09-26.md) uses the existing Administration image and a matched MCP short-support fixture to map the active and neutral native authorization controls. It adds no painted asset or fifth ImageGen reference.

## Handoff boundary

These four images are design references, not game assets. No DDS conversion or GFX registration is required. The parent owns `.gui`, scripted GUI source, GFX, localisation, and gameplay edits, and should use matching MCP scenarios for post-edit inspection while keeping offline-renderer limitations distinct from live-game validation.
