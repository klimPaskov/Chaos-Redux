# Mengele final audit prompt

Use this after implementation, super-event research, asset work, localisation, documentation, spreadsheet updates, and improvement-loop resolution.

Required audit routing:

1. `chaosx_localisation_auditor` for missing keys, duplicate keys, scripted localisation, tooltip clarity, super-event wording, and sensitivity.
2. `chaosx_decision_mission_auditor` if decisions or missions were touched.
3. `chaosx_focus_tree_auditor` if `mengele_clone_army_focus_tree` was touched.
4. `chaosx_country_package_auditor` if Directorate tags, client regimes, flags, leaders, starting units, or history setup were touched.
5. `chaosx_documentation_curator` if specs, plans, docs, manifests, or handoffs need reconciliation.
6. `chaosx_spreadsheet_doc_worker` after final in-game wording exists.
7. `chaosx_event_completion_auditor` as the final read-only completion audit.

The final completion audit must compare the implemented repo against this package, all accepted specs, and all plan addenda. It must list finished work, partial work, missing work, placeholders, simplifications, blocked validation, unresolved docs, and recommended next actions.

Do not claim completion if default super-event art remains, audio is undocumented, route tests are missing, the improvement addendum is unresolved, or any live event in the `germany_mengele.*` namespace is unreachable or placeholder without a documented reason.
