# Repository evidence record

## Method and limit

The connected GitHub tool was used read-only. A root listing, a project wiki listing, a search for the Event 073 namespace, the full existing event script, and the full unit-modding snapshot were inspected. Truncated directory listings were used as navigation only. They are not a full repository inventory.

## Pinned evidence

Repository: `klimPaskov/Chaos-Redux`.
Default branch reported by the connector: `master`.
Pinned source commit used for the target script and wiki snapshot: `879b3007d3b6bf75c726c11635473fccda45c569`.

### Existing event script

Path: `events/073_mongols_rise.txt`.
Blob SHA reported: `57346d4f4a87561c8e9f1faa755a04fedd34825d`.
Read status: full text.

Source URL: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/events/073_mongols_rise.txt`

Findings are recorded in the event-engine handoff. The current implementation provides namespace and legacy behavior evidence. It does not validate the expanded design.

### Unit-modding project snapshot

Path: `paradox_wiki/Unit modding - Hearts of Iron 4 Wiki.md`.
Blob SHA reported: `d285be8198639cbb2d3b8f24bdc4b78f4f8becce`.
Snapshot's stated capture date: 19 September 2026.
Read status: full text across the initial response and a follow-up range covering the truncated remainder.

Source URL: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/paradox_wiki/Unit%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md`

The snapshot describes custom subunits, cavalry categorization, groups, equipment requirements, terrain modifiers, separate offensive and defensive statistics, entity selection, and icon consumers. It supports the direction of a custom mounted category. It does not verify the exact current installed vanilla values or a universal country-specific division-designer prohibition.

### Search-only localisation evidence

Search returned `localisation/english/073_mongols_rise_l_english.yml` and the shared news file as namespace consumers. The localisation file was not fully read in this session. Do not claim that all legacy localisation or shared news consumers have been audited.

## Not inspected in full

The entire working repository, current local vanilla files, full wiki collection, installed Workshop mods, all country and character definitions, authoritative catalog workbook, current runtime GUI, and local skill reference libraries were not fully inspected. The supplied archive's own text files were fully read, as listed separately in the source ledger.

The connector reported repository files whose sizes differ from the uploaded snapshot. No complete cross-version comparison was performed. The uploaded brief and supplied planning sources remain the design basis, with pinned repository evidence used only for the facts actually inspected.
