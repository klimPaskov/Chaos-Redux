# Formable category attachment audit

Use this companion record for every manifest-driven state-puzzle consumer. The consumer manifest is the source of truth for the finite state set, projection, helper policy, and generated runtime names. This audit proves that every decision category in the formable family actually embeds the generated state-puzzle GUI.

## Strict attachment policy

Set `attachment_scope` to `all_formable_categories` when the event or system requires every category in a formable family to show the state puzzle. A static category picture, category description, or separate status window does not satisfy the policy when exact state control is the formation proof.

Categories outside the formable family may be listed as `out_of_scope` with a concrete reason. Never omit a category silently. If the owner cannot prove the category boundary, treat the audit as blocked.

## Manifest-to-category crosswalk

Keep this table beside the completed `manifest.json` or in the owner plan. `manifest.category_id` (or the compatibility manifest's `decision_category_id`) is the attachment key. The generated runtime output is authoritative for the scripted-GUI identifier and window name. Copy those values from the generated files instead of guessing a naming formula.

| Category ID | Category source | Formable decision IDs | Manifest path | Manifest category ID | Generated scripted GUI ID | Generated window | GUI context | Attachment status | Evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<category_id>` | `common/decisions/categories/<owner>.txt` | `<decision_id>` | `docs/formables/state_puzzles/<consumer>/manifest.json` | `<category_id>` | `<generated_gui_id>` | `<generated_window_name>` | `decision_category` | `attached` / `missing` / `blocked` / `out_of_scope` | `<artifact URI or exact reason>` |

For a category that contains several formation, integration, or post-formation decisions, list every relevant decision ID in the same row. If several categories belong to one formable family, each category needs its own row and an explicit manifest/runtime relationship. Do not assume that one attached category covers another category with a similar name.

## Audit procedure

1. Enumerate the category metadata files and the decision containers owned by the formable family. Include shared and phase-specific category files, not only the first formation category. Record the source paths in the crosswalk.
2. Confirm that every row's manifest is `status: "complete"`, names the same category ID, and contains the exact installed-map state geometry, live qualification helpers, required state policy, and formation territory helper.
3. Inspect `common/scripted_guis/chaosx_formable_state_puzzles.txt` or the owner-generated equivalent and copy the exact scripted-GUI block and window name into the row. The block must use `context_type = decision_category` and expose the manifest's generated state pieces.
4. Inspect each category metadata block and verify `scripted_gui = <generated_gui_id>` points to the row's generated block. The category must not rely on a picture-only or text-only presentation under the strict policy.
5. Use the installed read-only routes `mcp__hoi4_agent_tools__hoi4_gui_inspect` and `mcp__hoi4_agent_tools__hoi4_gui_render` for the linked window. Inspect the category context, hierarchy, generated state-piece sprites, tooltip regions, and click regions. Render every supported resolution and the unresolved, qualifying, optional-hidden, long-text, and missing-localisation states relevant to the consumer. Record artifact URIs and diagnostics in the row.
6. Compare the category's formation decision `available` trigger and AI path against the same territory helper named by the manifest. The GUI is informational and must never be the only formation gate.
7. Fail the audit on a missing category row, duplicate category ID, manifest/category mismatch, missing `scripted_gui` line, wrong `context_type`, unresolved generated reference, stale `status`, absent DDS evidence, or a GUI that presents a different state set than the formation helper. Carry the exact failure to the owner handoff.

## Completion rule

The formable package is not ready for parent review until every in-scope category is `attached`, every generated state piece and hover resolves, and the same named scenarios show agreement between piece status, summary status, decision availability, and AI decision validity. A missing MCP route is a blocker for the affected evidence, not permission to substitute source-only review.
