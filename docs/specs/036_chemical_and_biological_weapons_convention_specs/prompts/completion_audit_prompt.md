# Completion audit prompt

Run `chaosx_event_completion_auditor` read-only against `docs/specs/036_chemical_and_biological_weapons_convention_specs/` with a self-contained prompt.

Use [15](../15_acceptance_and_completion_contract.md) as the surface list and [the acceptance matrix](../matrices/acceptance_scenarios.md) as the audit index.

Event-specific checks:

- no Alien Spacecraft producer remains in slot 36, the recovery lives in Event 025 with unchanged receipt names, and the Event 016 and Event 025 consumers still read it
- every registered provider has an access flag, a global normal-route proof, and a cancellation call in its owner's transaction
- project selection is uniform over unique ids
- the convention multiplier sits at the doctrine mitigation point and never touches death, contamination, atrocity, or cover-up terms
- no Event 036 action duplicates an existing CBRN action
- the workbook no longer describes Alien Spacecraft and cluster 3 carries the Event 036 member row

Return complete, incomplete, or blocked with file and identifier evidence.
