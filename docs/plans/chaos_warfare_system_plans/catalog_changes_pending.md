# CBRN catalog wording review pending

Disposition: accepted and queued for the catalog owner, under the user's October 6 instruction to keep workbook edits outside this workstream.
No workbook or export CSV was edited.
No catalog row or field has been assumed from a stale CSV.

Thirty-one CBRN system localisation strings receive prose/title or constant-display repairs, without changing their localisation identifiers or gameplay values.
The exact before/after wording is in `subagent_handoffs/2026-10-06_prose_changes.json`.
The catalog owner should check whether the workbook quotes any of those system descriptions and copy the corresponding current in-game wording if it does.
This is wording alignment rather than a request for a new numbered event, evolution or cluster row.

The changed standalone facility report uses `cbrn_bio_facility.5.desc`:

> Biological material from our former stockpile site in [bio_facility_notice_state.GetName] has escaped while under foreign control. Surviving orders and agent signatures can still establish our responsibility and raise Condemnation without proving deliberate use.

Shortened public actions are Authorize Coercive Security, Authorize Protected Occupation, Destroy Attack Evidence, Admit an Accidental Release and Permit Inspection.
The state remains available through the native target and descriptions rather than being appended to the three shortened state-action titles.
The existing export action remains Audit Mask Shipment.
After an eventual workbook update, the catalog owner must run `python .tools/export_event_catalog_csv.py` from the mod root, without editing the generated CSV files directly.
