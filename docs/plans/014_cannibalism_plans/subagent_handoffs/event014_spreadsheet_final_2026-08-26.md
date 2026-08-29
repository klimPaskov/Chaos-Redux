# Event 014 catalog spreadsheet final audit

Date: 2026-08-26.

Scope: workbook-only audit and correction for Event 014 and manual scenario SCN-010; no gameplay, localisation, scripted localisation, 3D, or asset files were edited.

## Workbook change

Authoritative workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Changed sheet and cell: `Events!C15` for Event ID `14` (`Cannibalism`).

The cell had a replacement-character corruption and stale prose that no longer matched the current event-detail localisation. It now concatenates the current `chaosx.events_log.window.event_details.cannibalism.pre_reveal` and `chaosx.events_log.window.event_details.cannibalism.revealed` strings exactly, separated by one blank line between state variants.

The pre-write workbook SHA-256 was `fdd74f4f2b7ee56d8f104d4587d77f7b1c5102a5e9be529469f047388fc1c36e`.

The post-write workbook SHA-256 is `17a6156440220829a493a584804bbbb20e04cf378835982521c7ff9e164cf08c`.

The Events row 15 SHA-256 changed from `6a8d3281301b1872b963acf574df6860560f25f826ebfa860fd6913f131b8de6` to `820293801c9325ad24c97437ba5a5b865ddf31e7c95ce0e4d4643cb2aa9a8cf5`.

The final `Events!C15` UTF-8 value SHA-256 is `04a94a961a9bcd4a302e94349d42d5266be78eeb0e1cd3ba59fdb84a838e9901` and its length is 777 characters.

The XLSX package comparison made before the in-place write found `xl/sharedStrings.xml` as the only changed package part; sheet XML, tables, styles, workbook metadata, and validation payloads were preserved.

## Event 014 evidence

`Events!A15:N15` is Event ID `14`, name `Cannibalism`, three populated evolution fields in `D15:F15`, two terminal branches in `I15`, type `Minor Fire-Once`, Chaos level `1`, blank Cluster ID and Member Severity, and status `Needs Testing`.

`Events!D15:F15` exactly matches `cannibalism.evolution.stage_1`, `cannibalism.evolution.stage_2`, and `cannibalism.evolution.stage_3` title and description localisation.

`Events!I15` exactly matches the `chaosx_super_event.50` (`The World Is the Larder`) and `chaosx_super_event.53` (`No Thaw Will Come`) title and description localisation, with two terminal branches and no fourth or fifth evolution.

The final Event 014 cell hashes are `D15=a776f9b8dc825bddc0ca5f3ef3a6227df225b905957b53d8a12b83437309c551`, `E15=f361c8b0a396355e0cb244a4c48f2ecf7c59ef742d1d52db2ce91fa6ca6939da`, `F15=43116fad7338cc65b0302d767428a063e9c123f982d5e5a6c74d8c5fb72252d9`, `I15=3884cbc5e474596862b79748845c0524c9b2d372c1dd89a1de41ff9d57b43625`, `J15=07623ecfb458a2075245ab599d180142c88c5b801a5a9021efe35661f1b2dd3a`, `K15=6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b`, `L15=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, `M15=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, and `N15=268f0eee904e51ea6e8378b80c6be8a301f6c056f7aba3d773c8bc8097705d2e`.

The approved scope supplied for the wider package is nine gameplay consumers with seven bespoke models plus vanilla Bone Riders and Network Cadre; this spreadsheet-only pass made no 3D or gameplay claims and did not touch those files.

## SCN-010 evidence

`Scenarios!A10:F10` is `SCN-010`, `The Hunger Lines`, the exact five current scenario types `Discipline Collapse`, `Ritual Cells`, `Silent Islands`, `Warlord States`, and `Convergence`, current intensity wording for Low, Medium, High, and Maximum, and status `Needs Testing`.

The SCN-010 row SHA-256 is `acf9bc46d9a96c94a4ecf415f9c4e2ec00e0e9751d5494df9039572824cf80ec`; it was unchanged by this pass.

The final SCN-010 cell hashes are `A10=e78e01540a83ffc374f8717c1eb10231dab2efd339445089bbfb11897c30b398`, `B10=29743e93e2fa249045dbc6c8248ac36ecfcac946459958ca2f8a0d515ace2c6f`, `C10=5787afe6c64e755a6eeaf4252a2939fd3a2c81a894bbd3e881b60b21f752051b`, `D10=41368461704190d44d1d8d409669921384a4df07d7ea7804976b7602af4d6d1a`, `E10=2114adc0fb9172f917943f587de98c8c17697af7927935632b771b2427fae3d6`, and `F10=268f0eee904e51ea6e8378b80c6be8a301f6c056f7aba3d773c8bc8097705d2e`.

## Export evidence

Ran `python .tools/export_event_catalog_csv.py` from the mod root after the workbook write.

Exporter result was `status: success`.

`docs/spreadsheets/chaos_redux_events_catalog.csv` was refreshed from Events with 167 rows and 14 columns; SHA-256 `8d4d105dbda65bc2f792b5f2d3ccc7423e00d8caee98f5c053f55bc861aa194e`.

`docs/spreadsheets/chaos_redux_clusters_catalog.csv` was refreshed from Clusters with 14 rows and 7 columns; SHA-256 `647c9206de61a70d7a0d7adf0740dc97c81c8e63d01fefac6549b430b666425b` and no content diff.

`docs/spreadsheets/chaos_redux_scenarios_catalog.csv` was refreshed from Scenarios with 12 rows and 6 columns; SHA-256 `c6231be89377eb4e5fdf35966b8493d8400b22fc8e082ac97e6ef9639e653e44`.

The refreshed Events CSV row for ID 14 and Scenarios CSV row for SCN-010 match the final workbook rows exactly. The exporter also reconciled pre-existing snapshot drift outside this task, including the old `Fully Functional` status in the two snapshots and trailing export-only blank records; the CSV files were not edited directly.

## Workbook integrity and render checks

The XLSX zip integrity check returned `None` from `ZipFile.testzip()`.

The workbook has sheets `Events`, `Clusters`, `Scenarios`, and `Legend` with dimensions `1015x14`, `15x7`, `12x6`, and `24x4`; freeze panes and sheet auto-filters remain unset as in the source workbook.

Data validation counts remain `Events=3`, `Clusters=2`, `Scenarios=1`, and `Legend=0`; the raw sheet XML retains one `dataValidations` marker on each data sheet and two `x14:dataValidations` markers on Clusters.

The workbook contains zero formulas and zero formula error values.

LibreOffice `26.2.3.2` converted the workbook to a 36-page PDF successfully; PDF SHA-256 is `d3b5ae29426ee71f612267442dc99d469967ed3d2070da6cbbd325e6488a1222`.

Targeted visual renders were generated and inspected for Events details page 8, Events evolution page 15, Events metadata page 22, Scenarios details page 31, and Scenarios options/status page 33.

The targeted render hashes are page 8 `98ed7a983e4cfc74b3556ed8b4a56e19b761ade36d1d0ba2db60926226d16653`, page 15 `ae78ebe34688100eef4453c5e78c685ec06eb3e27ce6fe067de95ea48802eece`, page 22 `e2ff70d371e65ed2138059fac0800d3bdc9d2ccd130fe354e71358387ef9f845`, page 31 `69fb7d47a812a8a34531577bd0cb8baae50b3151b04b73d586811b14479d950f`, and page 33 `81159073f8a73648e615e2d3b126e7a147427ec2d4be01a44bcd0aebf3668deb`.

## Open evidence gates

`Events!N15` and `Scenarios!F10` intentionally remain `Needs Testing`; no cell was promoted to `Playable` while live evidence gates remain open.

No cell currently contains `Blocked` or `needs_user_review`; no further workbook change is recommended without new player-facing wording or evidence.
