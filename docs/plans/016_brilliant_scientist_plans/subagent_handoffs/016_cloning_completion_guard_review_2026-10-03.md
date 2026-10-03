# Event 016 cloning completion guard: bounded source review

Date: 2026-10-03

Status: The local completion guard prevents duplicate replay of the helper’s initial payload. The limits below remain explicit.

## Scope

Reviewed only `common/scripted_effects/germany_mengele_effects.txt:104-121`, `common/special_projects/projects/mengele_cloning_projects.txt:67-75`, and `common/scripted_effects/016_mengele_project_bridge_effects.txt:90-97`, as requested. No gameplay, model, localisation, or skill files were edited; no MCP call, game launch, broad call-site scan, or commit was made.

## Finding

`germany_mengele_complete_cloning_project` now wraps its existing payload in `if = { limit = { NOT = { has_country_flag = germany_mengele_cloning_project_completed } } ... }`. The helper sets that existing completion flag before setting the directorate completion flag, selecting the refinement, producing clone equipment, checking revolt readiness, or scheduling `germany_mengele.24`. A repeated call therefore fails the guard and cannot repeat the initial equipment production or schedule the revolt event again. The existing payload clauses remain in their original relative order inside the guard.

The native project output caller invokes this helper. The bridge caller additionally requires an applied clone operational grant and absence of the completion flag before invoking it. Both call paths therefore meet at the same guarded helper, with the helper providing the duplicate protection even if a caller invokes it again.

The guard is local to `germany_mengele_complete_cloning_project`; it does not add a guard around independent replenishment actions, so a direct call that bypasses this completion helper remains available. The supplied excerpts do not include any separate replenishment call site, so I cannot inventory or independently certify those callers within the read boundary.

One adjacent call remains outside the helper guard: the native `project_output` block invokes `chaosx_grant_custom_operational_technology` after the completion helper. A duplicate invocation of that outer output block can still reach that separate grant. Its idempotence was not assessed because its implementation is outside the permitted source ranges; this does not alter the finding about initial clone equipment production or revolt scheduling.

## Handoff and validation

The reviewed gameplay identifiers are `germany_mengele_complete_cloning_project`, `germany_mengele_cloning_project_completed`, `germany_mengele_produce_clone_equipment`, `germany_mengele_cloning_project_revolt_ready`, and `germany_mengele.24`. Before the guard, repeated helper calls could replay the enclosed payload. After the guard, the first call latches completion before the grants and revolt scheduling, and later helper calls skip that payload.

Validation was a direct read of the three requested source ranges. No runtime behavior or external replenishment call-site inventory is claimed. Parent owns MCP review, final wiring, and commit.