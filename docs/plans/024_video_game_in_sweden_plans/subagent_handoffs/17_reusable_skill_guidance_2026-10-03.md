# Reusable decision guidance handoff

Disposition: `implemented` for the bounded skill-maintenance assignment, including the parent-requested AI-hint exception, with final parent review pending.
Acceptance basis: the parent explicitly requested checking the three hazards and adding only missing reusable guidance to the decisions-missions skill.
The parent approved the bounded rule and requested an explicit exception for variable-fee emergency AI hints within the same owned paragraph.
This disposition makes no gameplay completion or design-approval claim.

## Owned changes

- Updated `.agents\skills\chaos-redux-decisions-missions\SKILL.md` with one paragraph under `Custom-cost affordability and payment`, immediately after the existing fractional-quote paragraph.
- Created this handoff at the exact parent-supplied path.
- Created no skills and changed no gameplay identifiers, localisation, assets, workbook, other skills, generated definitions, or Git index entries.
- Used `skill-creator`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-events`.
The events and subagents skills were read fully and left unchanged by this worker.
No routing change or AGENTS.md update is needed.
No commit was made because the parent explicitly retained shared-tree commit ownership.

## Existing coverage and missing guidance

Line citations below refer to the pre-edit working files, rather than HEAD.

| Hazard | Existing guidance | Missing guidance captured |
| --- | --- | --- |
| Emergency resolution under depleted reserves | Decisions-missions lines 193–234 already require matching texticons, aligned display/affordability/debit, sufficient fractional precision, and fresh calculations. | Accepted emergency availability must survive nominal reserve shortfalls, with bounded actual fees, an explicit actual quote, one freshly recomputed coherent payment, and no hidden partial-payment or threshold-waiver cliff. |
| Exact numeric engine reader | Required reading at decisions-missions lines 14–25 requires checking documented syntax, but neither reviewed implementation skill identifies this reader-token hazard. | Use exact documented numeric tokens, including `has_war_support`, while preserving the validity of an intentionally defined normal variable named `war_support`. |
| Final cleanup and late callbacks | Decisions-missions lines 331–338 already guard timeout resolution against duplicate failure, and lines 886–906 cover generic cleanup and setup receipts. Events lines 320–335 cover defeat aftermath and lines 481–492 cover receipt closure for asynchronous local projects. | Closed-state guards and active-context checks must prevent late cleanup from erasing earned finite aftermath or achievement receipts. |

The added rule supplements those existing contracts without repeating generic event wiring, localisation formatting, or lifecycle inventories.

## Exact added paragraph

> When accepted design requires emergency resolution to remain available while every other recovery is unaffordable, do not gate it on full nominal reserves. Bound each actual fee by its nominal fee and the nonnegative current reserve, show the actual quote with matching texticons, and recompute all fees together before any debit, then charge that coherent quote once. Avoid hidden partial payments and threshold fee-waiver cliffs. For variable-fee emergency actions, use an `ai_hint_pp_cost` matching the actual quote only if that input form is verified as supported, otherwise omit the fixed nominal hint so a zero quote remains available to AI at zero political power. Never assume `ai_hint_pp_cost` accepts dynamic values. Verify exact numeric reader tokens in installed dynamic-variable documentation rather than assuming a display or stat name: `has_political_power`, `has_stability`, and `has_war_support` are documented readers, while raw `war_support` is not a documented built-in reader. This does not forbid a custom normal variable named `war_support`. Make final resolution and cleanup idempotent with a closed-state guard, and require queued work and late timed callbacks to match the active context before invoking cleanup. Preserve earned finite aftermath until its intended expiry and retain achievement receipts when removing active-crisis state.

## Direct source evidence

- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md`, lines 431–442, explicitly documents `has_political_power`, `has_stability`, and `has_war_support`.
The latter two readers are documented on the 0–1 scale.
A full-file exact heading search found zero `### war_support` entries, so the wording deliberately says raw `war_support` is not a documented built-in reader rather than banning the token as a custom variable.
Installed-reference SHA-256: `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, lines 1496–1499, lists political-power and stability readers and `has_war_support` on the 0–1 scale.
It also recognizes `political_power` and `stability`, so the rule does not forbid documented alternate tokens.
Offline-wiki SHA-256: `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
- The emergency-fee and receipt-preservation requirements come from the parent's explicit reusable hazard brief, supported by the existing skill contracts cited above.
They are project implementation invariants, not claims that installed documentation establishes a particular balance policy or runtime outcome.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md`, line 335, says `ai_hint_pp_cost` makes the AI save the hinted political-power amount regardless of actual payment and requires a constant rather than a variable.
Offline decision-reference SHA-256: `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.
The installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md` was read fully and contains no `ai_hint_pp_cost` entry or dynamic-input support statement.
Installed decision-reference SHA-256: `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`.
These references do not verify dynamic hint support, so the paragraph permits an actual-quote hint only with separate support evidence and otherwise explicitly permits omitting the fixed nominal hint for variable-fee emergency actions.

Connected-tool route gap: `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` were absent from the exposed tool inventory.
The installed reference and offline wiki were therefore read directly, and no MCP retrieval or engine validation is claimed.

## Review evidence and risks

The target skill already contained another agent's fractional-quote and paid finite-registry-release additions before this worker edited it.
Removing only the owned paragraph and its separating blank line reproduces the exact pre-edit file SHA-256 `2B2805E38E89271C41D19259E34B236A32C8838D9A4F51E88BC126A289115130`, proving those additions and all other pre-edit bytes were preserved.
Post-patch skill SHA-256 after the parent-requested AI-hint exception: `283033F95CBBB822A66242574EDDE98E425165715CDC5EF035B80F9A5267A745`.
The official skill validator passed with `python -X utf8 C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-decisions-missions`.
Its initial default-encoding invocation failed on existing UTF-8 text under Windows cp1252, and the UTF-8 invocation resolved that validation issue without changing the validator.

Parent review should select only this worker's paragraph and handoff, since the HEAD diff also contains the other agent's existing skill additions.
The emergency rule is conditional on accepted design and does not authorize changing ordinary decision fees or introducing a new fallback.
The exception overrides the preceding fixed nominal AI-hint requirement only for variable-fee emergency actions.
It requires verified support for an actual-quote hint or omission of the fixed nominal hint, and never assumes dynamic `ai_hint_pp_cost` syntax is supported.
Actual fee bounds must include zero for depleted or negative reserves, and all fee calculations must precede payment to avoid sequentially changing quote inputs.
Closed-state protection must preserve earned receipts while still allowing the aftermath's designed finite expiry.
Source and skill review do not prove runtime behavior, and no gameplay audit, probability comparison, game launch, service restart, or live validation was performed or required for this documentation-only scope.

The bounded skill task is complete with no simplifications, omissions, or unresolved content blockers.
Parent review and commit remain parent-owned.
