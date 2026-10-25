# Import review: Equipment Choice 123

Date: 2026-10-24 (import), reviewed 2026-10-25.

## Scope and authority

The package is the planning ZIP `123_equipment_choice_specs.zip`, which contains 17 members.
The import brief stated 16, so the count discrepancy is recorded here and all 17 members are placed.
Event 123 is the catalog identity, with former catalog ID 135 kept as provenance.
The shared identifier registry already records `123 | Equipment choice | former 135 | User-confirmed catalog identity, runtime unimplemented`.
Catalog identity adoption does not approve the proposed mechanics, register runtime content, or change availability, as the registry states.
Gameplay design, classification, cluster memberships, the cluster 18 cooldown, and the worldwide per-firing distribution remain unresolved proposals (see Unresolved items).
This pass edited documentation only.
No gameplay, localisation, GFX, asset, workbook, or CSV file was changed, and no HOI4 tool or the game was run.

## Destinations

Active design, README, and prompts are in `docs/specs/123_equipment_choice_specs/`.
Historical evidence is in `docs/plans/123_equipment_choice_plans/imported_review/`: the calculation evidence JSON, the source-reading ledger JSON, and the source evidence file.
The acceptance and validation file stays in specs because it holds the 32 active implementation acceptance cases that the coding and goal prompts name.
The implementation handoff also stays in specs because it is the active integration contract.
The three imported_review members were verified byte-identical to the originals by SHA-256 after copying.
Links from active files into imported_review were rewritten, and every relative link in the specs folder resolves.

## Member disposition table

Original SHA-256 values are the hashes of the members as extracted from the ZIP.

| Member | Original SHA-256 | Bytes | Destination | What changed |
| --- | --- | ---: | --- | --- |
| `README.md` | e99480fbb28417931f2940fccbb7de00ab90d74d492f33dcea9bd42d7105f211 | 4593 | specs | Removed the ZIP extraction instruction; identity text corrected to 123 with former 135; registry migration stated; evidence links repointed to imported_review; design-status note added |
| `123_equipment_choice_spec_part_1_core.md` | 1e9f55154b6dd0206bf3895b5664db67898cabd909f8a801192c16691c5fcd93 | 13033 | specs | Identity sentence corrected (123 is the catalog identity, former 135 provenance) |
| `123_equipment_choice_spec_part_2_manifests_and_value.md` | 84ec4da439ff55feb22471d9aa21e6879d70e8014731f90727151b191d904be1 | 12911 | specs | Unchanged; arithmetic spot-checked (see Unresolved item 5) |
| `123_equipment_choice_spec_part_3_evolutions_and_consequences.md` | e02cc04db558f63f79d1a3b68b288e79182749beab7e522b6700c1582f49ca3c | 20244 | specs | Link to source evidence repointed to imported_review |
| `123_equipment_choice_spec_part_4_ai_and_lifecycle.md` | 727db3f229256e3b51e63f0a61633fafe4a81f8ce32e09c4fabc3458dc1ab6a0 | 16080 | specs | "User-authorized" worldwide pass replaced by a permission requirement under AGENTS section 1 rule 8; "this task's implementation" wording removed |
| `123_equipment_choice_spec_part_5_presentation_and_assets.md` | d9aa7486f825d6bcd2efefed9e674862b0a1a2a4be100967435364ba8795c495 | 12675 | specs | "Supplied" replaced by "existing" (templates) and "delivered" (equipment) |
| `123_equipment_choice_spec_part_6_achievements.md` | fbc0c14a89bb6c235cc8d576389b45621a5f8988dfe50459d356ed53848c120a | 8912 | specs | "Supplied achievement templates" replaced by "existing achievement templates" |
| `123_equipment_choice_acceptance_and_validation.md` | 807afb985e6b80378a0ae98ac67800c3bfbaebfe25d3ffb8a40fc011ad84a40d | 18465 | specs | ID crosswalk line updated to the registry state; review history kept as recorded |
| `123_equipment_choice_implementation_handoff.md` | 24f3a781f3026f253447f36dc51e4b5015350bb8f753fa02314aa4c204af569c | 17686 | specs | Identity-audit start replaced by a registry check; user-draft provenance stated; subagent-map intro stops describing the planning session as the source of routing; "supplied source gate" removed; catalog status note added |
| `123_equipment_choice_coding_prompt.md` | f7154df39e95d639a362f4141609158acbccce64f190b74c0900e6f439d78293 | 7843 | specs | "Current source gate" replaced by the AGENTS source-reading rules; occupied-ID crosswalk replaced by the registry state; worldwide pass gated on AGENTS rule 8; "supplied roles" replaced by project roles; workbook work routed to `chaosx_spreadsheet_doc_worker` and `python .tools/export_event_catalog_csv.py`, with CSVs never edited directly |
| `123_equipment_choice_decision_prompt.md` | 3a778303d0f1dc445f4ee2d0b8af45cd52d61b6867e34568c3b1d12b7e0543ab | 5392 | specs | "User-authorized free shipment" replaced by a reference to Part 1 |
| `123_equipment_choice_asset_prompt.md` | cae3ea67734b6288cf5d4e43abbcf1f11fcd74abef936b23ae466a902d77f6e8 | 7582 | specs | "Unchanged supplied templates" replaced by "existing achievement templates" |
| `123_equipment_choice_achievement_prompt.md` | 4c2a3825605bea25653f81575813bc0f30b813b3991053377e95234f446bc350 | 4597 | specs | "Event identity reconciliation" replaced by the registry identity check |
| `123_equipment_choice_goal_prompt.md` | 46c2980cfb4ea5794eb9f6fbc109245d9771d7d4b5d7cfa2e05b8ab6dd0c8d63 | 3980 | specs | "Complete the current source gate" removed; ID-collision sentence replaced by the registry confirmation; length now 3886 characters, under the 4000 limit |
| `123_equipment_choice_source_evidence.md` | 4dc7774eae39591ad3db35b5f2a354bcaa62de16e64727e26e7d6c93454a5db9 | 18127 | imported_review | Historical; byte-identical copy, no edit |
| `123_equipment_choice_source_reading_ledger.json` | 37319abefcbc589d8bcc15cba01bb398dfddd72d092590b72d5118e92722cd10 | 146031 | imported_review | Historical; byte-identical copy, no edit |
| `123_equipment_choice_calculation_evidence.json` | 2a5c641b9ce4156a61c9afa0cf6ae94ba68253cc4dd4e647ce5288cc468fcc65 | 96575 | imported_review | Historical; byte-identical copy, no edit |

## Fixes made, by category

Identity and catalog:
- Event 123 is stated as the catalog identity with former 135 as provenance, in the README and Part 1.
- The README, the implementation handoff, the coding prompt, and the goal prompt state the registry migration (123 Equipment choice from 135, 113 The Partition from 123, 108 Wrestling Tournament from 113) and require workbook confirmation against it before mutation.
- The acceptance line that called the crosswalk unresolved now says the registry records it.

Stale repo or process assumptions:
- The ZIP extraction instruction is removed from the README.
- The coding and goal prompts no longer ask the agent to complete a "current source gate" that depends on the supplied bundle. They point to the AGENTS source-reading rules and owner skills.
- Workbook changes are routed to `chaosx_spreadsheet_doc_worker`, followed by `python .tools/export_event_catalog_csv.py` from the mod root. The coding prompt no longer says to "regenerate and compare" CSVs without the exporter.
- The subagent map no longer describes the planning session's agents as the routing source. It points to `.claude/agents/`.

AGENTS constraints:
- The worldwide per-firing distribution was described as "user-authorized" in Part 4 and the coding prompt. It now states that explicit user permission is required under AGENTS section 1, rule 8, before implementation. The import brief supplies no record of that permission.
- The decision prompt's "user-authorized" shipment wording now refers to Part 1.

Wording:
- "Supplied" and "this task's implementation" phrases in active prompts and specs were replaced with the existing or delivered equivalents.

Hard wraps and formatting:
- A heuristic scan of all 17 members found no mid-sentence hard wraps. Sentences sit on their own physical lines, and paragraphs, headings, tables, and code blocks are unchanged.
- No em dashes or semicolons were found in the prose, and no `<=` or `>=` operators appear.

Links:
- Active links into imported_review were rewritten: README (source evidence, ledger, calculation evidence) and Part 3 (source evidence anchor).

## Verified against the repository

Verified in the current tree (registry, workbook exports, and source files; grep-scoped, not whole-tree):
- `docs/specs/shared_identifier_registry.md` lists 113 The Partition (former 123), 108 Wrestling Tournament (former 113), and 123 Equipment choice (former 135). Its super-event presentation slot 123 belongs to Event 091, a separate namespace, so it is not a collision.
- `docs/spreadsheets/README.md` lists the five valid status labels. Unimplemented events above Event 20 with no `chaosx.nr<ID>.1` root are not To Be Reworked (see Unresolved item 3).
- Cluster 15 (Sudden Abundance) is Minor Repeatable with members 19, 37, 42, 56, 64 in the CSV export, and member 37 carries Medium severity there. `common/script_constants/event_cluster_constants.txt` has `sudden_abundance = 120` in its cooldown table.
- Cluster 18 (Military Preparation) is Minor Repeatable with members 42, 56, 64 in the CSV export. It has no cooldown entry in the constants file and no matching string in `common/scripted_effects/chaosx_event_cluster_effects.txt`, which confirms the package's statement that its runtime registration is missing.
- All shared files cited by the handoff exist: `chaosx_logic_effects.txt`, `chaosx_settings_effects.txt`, `chaosx_settings_triggers.txt`, `event_cluster_constants.txt`, `chaosx_event_cluster_effects.txt`, `chaosx_events_log_effects.txt`, `chaos_redux_achievements.txt`, `clone_system_effects.txt`, `clone_system_constants.txt`, and the Event 027, 042, and 016 helper files.
- `equipment_from_heavens_apply_special_receipt` is defined at line 121 of `042_equipment_from_heavens_special_effects.txt`.
- The five robot, teleportation, paleogenetic, xenobiological, and temporal equipment tokens and the coal golem token exist in the equipment definition files.
- Asset folder conventions exist: `gfx/event_pictures/<id>_<slug>/`, `gfx/interface/decisions/<id>_<slug>/`, `gfx/interface/ideas/<id>_<slug>/`, root `gfx/achievements/<full id>.dds`, and `common/achievements/chaos_redux_achievements.txt`.
- `process_achievement_icons.py`, `convert_to_dds.py`, the event-assets `gfx_references/CATALOG.md`, and `.tools/export_event_catalog_csv.py` exist. The event-assets skill refers to uncompressed BGRA output.
- `chaos-redux-event-planning` `references/specification-delivery.md` sets the goal prompt ceiling at 4000 characters, so the 3886-character goal prompt complies.
- The HOI4 tools named by the MCP usage map (`hoi4.event_inspect`, `event_render`, `probability_inspect`, `probability_analyze`, `gui_inspect`, `gui_render`, and the reference tools) appear in the connected tool list.

Spot-checked arithmetic (not a full recalculation):
- Part 2 industrial subtotal, allowance, and the five illustrative examples reproduce. The subtotal ceiling of 25,000 holds the 24,700 capped-input maximum.
- Part 2 unusual per-set charges and the 1.5 B minimum allowances reproduce from the stated per-unit costs.
- Part 3 Chaos map totals 25 at most; setback chances match the stated bases and increments.
- Part 4 score scenario totals match the stated factor vectors (for example, a conventional score of 5 and an unusual reserve score of 10).
- Temporal reserve ceiling gives 66, 88, and 22 units, which is 22/90 of a set.

## Unresolved items for the parent

1. Worldwide distribution authorization. The package says the per-firing pass to every captured active identity is user-authorized. The import brief contains no explicit user decision for that pass. AGENTS section 1 rule 8 requires explicit permission before implementing a whole-world iteration, so this needs a user answer before coding. The spec, prompts, and handoff now say so.
2. Design acceptance basis. `123_equipment_choice_acceptance_and_validation.md` cites "the parent's selection within the user's authorization to expand the complete specification" as the acceptance basis for the promoted corrections. Nothing in the import brief confirms that. The gameplay mechanics, the Minor Repeatable and Chaos level 1 classification, the Medium memberships, the cluster 18 120-day cooldown (a package planning value with no runtime registration), and the staged-delivery and setback numbers stay unresolved until the parent accepts them. The same status applies to the registry entry, which only adopts the identity.
3. Catalog status. The package requests To Be Reworked. The workbook rules reserve that status for events with a `chaosx.nr<ID>.1` root, and the 24 October migration kept all 19 unimplemented migrated events Unavailable. The parent decides the status, and no workbook change is made here.
4. Event document path. The handoff targets `docs/events/123_equipment_choice.md`. Event 042 uses the folder form `docs/events/042_equipment_from_heavens/overview.md`, and both forms exist. The parent should choose one before implementation.
5. Part 2 rounding example. The illustrative infantry allocation yields 6,250 rifles at 0.5 value, which is 3,125 against the 3,120 infantry share of the 3,900 allowance. The total of 3,885 stays within the allowance. The rule "spend the residual ... within its value allowance" should be read at total or category level. The example was not changed.
6. Pre-existing workbook issues recorded in the imported source evidence: the Events table declares 14 columns against 13 headers, and cluster 15 has an incomplete keyed slot at membership row 61. These were not verified in this pass because the workbook was not inspected. The catalog owner should check them with the 123 membership delta.
7. Numerical fixtures in the calculation JSON, including the isolated load values 2.054779 and 2.465735 and the 62,826 physical value figure, were not recalculated. They are historical planning records.

## Cross-package and catalog items for the parent

- Workbook: the 123 row status, the Medium memberships of 123 in clusters 15 and 18, and the membership slot pattern all need the spreadsheet worker. Cluster 18 also needs a runtime registration decision before any cooldown row is treated as active.
- Registry: the 123 entry already links to `123_equipment_choice_specs/README.md`, which still resolves. The proposed achievement IDs `123_equipment_choice_*` are not in the registry. Whether they need a reservation record depends on the registry's rules, which were not examined here.
- Repo: no other package was edited.

## Checks run

- SHA-256 of all 17 members recorded; imported_review copies compared with the originals and found identical.
- Every edit was an exact-match replacement asserted to occur once, with a second run that skipped already-applied edits.
- Relative links in the specs folder resolve; GitHub links were not fetched.
- Repository identifier and file existence checks listed above, run by scoped search only.
- `python -B .tools/check.py quick --paths` on the two changed folders returned "no check reads the 2 changed path(s)". No Markdown rule applies, so this proves nothing about the content.

Not run: any HOI4 MCP call, any engine or live-game check, save inspection, and any asset or image check. The package is planning only, and nothing here claims an engine or gameplay result.

## Remaining risks

- The engine contracts in the package remain unverified: non-owner unusual stock creation, the victorious-army equipment query, exact timed modifier keys, the effective cost of finished variants, and the controller-change popup behaviour.
- The inherited model-owner limits for the six unusual families are not repaired by this package, as the package itself states.
- The acceptance matrix (EC-A01 to EC-A32) is not executed, and live validation is user-owned.
