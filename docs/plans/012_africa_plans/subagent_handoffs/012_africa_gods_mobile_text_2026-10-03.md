# Event 012 typed truck and artillery localisation handoff

Disposition: implemented bounded localisation patch, with MCP visual validation unresolved.
Acceptance basis: the parent explicitly assigned typed family-2 display, the seven normal type fields, native texticons, reserve requirements, and these three writable paths.
Design reference: `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_mobile_artillery_design_2026-10-03.md`.
No Git/index operation or HOI4 launch occurred.
No parent-owned receipt, report helper, core gameplay, equipment helper, constants, spreadsheet, or other documentation file was written.

## Changed files and identifiers

- `common\scripted_localisation\012_africa_gods_scripted_localisation.txt`: changed only the mobile family branches of the 11 resolvers below.
- `localisation\english\012_africa_gods_l_english.yml`: added the seven keys below without changing existing keys.
- This new handoff.

| Resolver | Own field stem |
| --- | --- |
| GetGodsOfAfricaDemandFamilyName, GetGodsOfAfricaDemandIcon | gods_of_africa_demand |
| GetGodsOfAfricaPaymentIcon | gods_of_africa_payment |
| GetGodsOfAfricaSubstituteIcon | gods_of_africa_substitute |
| GetGodsOfAfricaSubstituteSlot1Name, GetGodsOfAfricaSubstituteSlot1Icon | gods_of_africa_substitute_slot_1 |
| GetGodsOfAfricaSubstituteSlot2Name, GetGodsOfAfricaSubstituteSlot2Icon | gods_of_africa_substitute_slot_2 |
| GetGodsOfAfricaSubstituteSlot3Name, GetGodsOfAfricaSubstituteSlot3Icon | gods_of_africa_substitute_slot_3 |
| GetGodsOfAfricaResponseFamilyName | gods_of_africa_last_response |

Each typed branch requires its own `_family = constant:gods_of_africa_demand_family.mobile_artillery` and its own `_mobile_type = constant:gods_of_africa_mobile_type.trucks` or `.artillery`.
An immediately following family-2 fallback selects `gods_of_africa_mobile_unavailable`, so missing, zero, and invalid subtype values cannot reach the truck or political-power icon.
The response resolver uses receipt family/type only and never active demand type.
All other family branches and resolver defaults remain intact.
The umbrella `gods_of_africa_family_mobile_artillery` key remains unchanged for general explanations and priority text.

| New key | Exact wording |
| --- | --- |
| gods_of_africa_family_trucks | trucks |
| gods_of_africa_family_artillery | artillery |
| gods_of_africa_icon_artillery | ?artillery_texticon |
| gods_of_africa_mobile_unavailable | shipment unavailable |
| gods_of_africa_mobile_truck_capacity_tt | Can ship the required trucks to Africa while keeping enough for army reinforcements and an operating reserve. |
| gods_of_africa_mobile_artillery_capacity_tt | Can ship the required artillery to Africa while keeping enough for army reinforcements and an operating reserve. |
| gods_of_africa_mobile_type_invalid_tt | The shipment specifies either trucks or artillery. |

The truck branches reuse `gods_of_africa_icon_motorized` with `?motorized_texticon`.
Only the two requested capacity tooltip keys were added.
The validity tooltip describes the shipment's concrete equipment choice rather than a numeric enum or script validity check.
No formatting characters were added to scripted localisation, and no helper parameter syntax was introduced.

## Audit and prose review

Missing localisation keys: none among all leaf references in this scripted localisation file after the patch.
Duplicate localisation keys: none in the assigned English file.
Scripted localisation issues fixed: generic family-2 names, truck-only icons, and invalid-subtype fallthrough.
Dynamic text repair: each name/icon now follows its own frozen contract, transaction, offer, slot, or response identity.
Existing amount tokens, scopes, colours, and all existing YML values were preserved.
Encoding concerns: none in the assigned English file, which retains UTF-8 BOM.

Vagueness: generic mobile/artillery labels became concrete trucks or artillery on typed shipments.
Bloat, obvious explanation, repetition, and overcomplication: no existing prose passages were rewritten beyond the bounded branch leaves because their remaining surrounding wording is outside this task's requested change.
The new capacity requirements state the shipment and protected army/reinforcement reserve in one sentence without disclosing private counters or quote calculations.
Style repair: the new validity requirement avoids the technical phrase 'valid fixed equipment type'.
No sourced quotations were touched and the changed leaves contain no attributed quotations.
No dynamic tokens or formatting codes were removed.
Cross-surface alignment: demand, cost icons, substitute slots, and receipt family names all use matching type ownership.
No workbook comparison was performed, and no catalog mismatch is established by this audit.
If the spreadsheet owner mirrors these leaves, use the exact key-level wording above.

## Meaningful validation and limits

A temporary in-memory source check evaluated 770 combinations across all 11 targeted resolvers: 14 families times missing, zero, truck, artillery, and invalid subtype values.
It verified exact subtype leaves, explicit unavailable fallback for family 2, exclusion of the new branches for unrelated families, and response isolation from active demand type.
A complete leaf-reference check found no undefined YML leaves, and a key count found no duplicate keys in the assigned English file.
These are source checks, not engine execution or production-render evidence.

The parent still owns enum constants, field binding/lifetime, receipt capture, and integration of the two capacity tooltips and invalid-type tooltip into helper requirements.
Those concurrent owner changes were not validated as complete by this subagent.
No balance, AI, mechanics, route, quote arithmetic, or reserve policy was changed.
No design-depth gap or additional mechanic was proposed, so no extra expansion plan was written.
No simplification was made to the requested localisation logic.
The patch is reviewable, but full Event 012 completion and native display claims remain with the parent.

## References and MCP blockers

The following relevant local sections were read directly while the exposed reference routes remained pending.
Hashes are SHA-256 revisions of the complete source files, not a claim that the full files were read.

| Source | Read spans | Revision |
| --- | --- | --- |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 65-80 encoding guidance, 223-231 texticons, 657-690 scripted localisation and first matching branch | 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064 |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 125-160 contextual localisation and event scopes | 884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7 |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\DOD_yugo_infiltration_localisation.txt` | 1-32 installed scripted-localisation documentation comments and vanilla precedent | 25b47a353785a25113bbfcea81e27a5c489be430e955bc2449dbf75f8ea6d278 |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\texticons.gfx` | 2131-2135 artillery, motorized definition located at 2150 | e0349b22f05affe550e755fc2e1f3a2ad3749fb016b5c9031b3672d9656304b5 |

Native artillery sprite is `GFX_artillery_texticon`, using `gfx/interface/equipmentdesigner/tanks/role_icons/role_icon_2.dds`.
Native truck sprite is `GFX_motorized_texticon`.
No replacement asset or invented texticon was added.

Exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` schemas were checked.
Localisation context limit 4 and search 'scripted localisation defined_text' limit 4 returned no result before bounded cancellation.
The narrow retry 'localization_key', game_doc-only limit 1, and source lookup `GetGodsOfAfricaDemandFamilyName` likewise returned no result before cancellation.
Without reference ids/revisions, reference_read could not be called correctly.
This is a no-result cancellation boundary, not a diagnosed service timeout or proof of health.

The initial event selector attempts were rejected by schema validation.
Server errors established the required selector object as `{ kind: "event", eventId: "chaosx.nr12.604" }`.
Corrected read-only event lint and options render requests, each bounded to maxNodes 1, returned no result before cancellation.
No artifact URI, source-linked event result, or production render was obtained.
Coverage, overflow, alignment, and native event/decision presentation remain unobserved.
No linked scripted GUI consumer was located by the bounded Event012 source search, so no GUI rendering capability or layout defect is claimed.
Source checks are not a substitute for mandatory MCP or native visual evidence.
Standalone Technology Tree Viewer availability was checked separately against the exposed tools: no standalone viewer tool was present, recorded as a package gap.
No technology, focus, or map surface was assigned in this bounded patch.

Skills used: chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents, and chaos-redux-event-assets.
No skill was created or updated.

## Source validation correction from parent review

The parent's byte-level review found that the delivered `gods_of_africa_icon_artillery` value was the literal `?artillery_texticon`, rather than the required U+00A3 texticon marker.
This was an actual source error, not console display encoding.
The existing motorized leaf already contained the correct U+00A3 marker.
The parent repaired the artillery leaf using `chr(163)` and preserved the English file's UTF-8 BOM.
The correct exact mapping is `gods_of_africa_icon_artillery: "£artillery_texticon"`.

The 770 source scenarios validated selector routing and leaf key existence, but did not verify the icon control character inside the selected YML value.
They therefore did not establish correct native icon-token content.
The earlier exact-wording table states the intended mapping and must not be treated as proof that the initially delivered bytes matched it.
A subsequent read-only check confirmed that the current artillery value starts with U+00A3 and equals `chr(163) + "artillery_texticon"`, with UTF-8 BOM present.
The parent repair resolves this source defect, while native visual validation remains unobserved.
Only this handoff was appended for the correction, with no further YML edits, Git/index operations, or skill maintenance.
