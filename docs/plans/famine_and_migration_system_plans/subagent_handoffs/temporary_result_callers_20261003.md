# Temporary result caller contract

Date: 2026-10-03.
Disposition: implemented source correction with source review complete and native execution unresolved.
Acceptance basis: the user's complete valid responses and exact custody receipts require callers to reliably consume their helper results.

The offline Data structures reference at lines 436-442 warns that a temporary first created inside a scripted helper may not remain available outside that helper.
It guarantees that a temporary declared before the call carries into the helper and receives its modifications.
Installed `effects_documentation.md:7820-7839` documents assignment syntax and scope but does not establish deterministic loss on every helper return.
This repair therefore closes an unsafe lifetime assumption rather than claiming an observed universal engine failure.

`migration_open_reception` now declares shelter and medical result outputs before their setters.
`migration_controlled_medical_reception` declares its medical result before the setter and subsequent observation-mission check.
`camp_rework_commit_exact_cohort_custody` declares the current-state result, duplicate-result marker, and resolved living amount before its wrapper and acknowledgment check.
The declarations use existing zero/invalid constants and unprefixed temporary names.
Helper payment, validity, population, service, custody, and outcome logic is otherwise unchanged.

Changed paths are `common/decisions/migration_decisions.txt`, the three-line caller hunk in the mixed-owner `common/scripted_effects/camp_repression_rework_effects.txt`, and the result contract in `common/scripted_effects/migration_capacity_effects.md`.
The Camp file contains extensive concurrent administration work; only this caller hunk belongs to the parent commit.
The repaired migration decision-file SHA-256 is `5000DD59578763690E391A22C8F09E7BCC0FC16E8AA063CE068B2D6104BAA0D7`.
No `ai_will_do`, weight, affordability, cost, duration, visibility, target selection, localisation, asset or event identifier changed.

Independent review in `normal_food_observation_completion_audit_20261003.md` verifies the four call sites and the preserved helper consumers.
The relevant source cases are positive setter result reaching observation, rejected setter result remaining invalid, valid/duplicate custody acknowledgment, and rejected custody with zero output defaults.
Source traces are not native execution or a clean error-log claim.
No game was launched and no logs were read.
No fallback, simplification, new player value, free resource, population, or death effect was introduced.
