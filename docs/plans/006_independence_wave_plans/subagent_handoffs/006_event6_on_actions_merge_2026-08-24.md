# Event 006 on-action registry consolidation

## Scope

The seven Event 006 on-action files with unique callback keys were merged into `common/on_actions/006_independence_wave_on_actions_registry.txt`. The registry preserves the original callback names, effect bodies, source order, and source-file markers. The three remaining Event 006 on-action files remain separate because they share engine callback keys and need their own callback-composition boundaries: achievement, evolution, and Join.

## Preservation evidence

The merged set contains 72 callback definitions from the seven former files, with 72 unique identifiers before and after the merge. A static comparison found no missing callback, no duplicate callback in the merged set, and seven source markers. The registry keeps one `on_actions` container, so the unique callbacks are composed without changing their engine names.

## File result

Seven former files were removed and one registry was added, reducing the Event 006 on-action file count by six. No country-wide iteration, callback key, effect, or runtime reference was introduced or removed. The registry is a source-layout change only; no live game loading or callback execution claim is made.

## Validation boundary

The Event 006 event MCP trace was unavailable after its recorded timeout, so runtime callback acceptance remains unclaimed. The three duplicate-key/ownership-sensitive on-action files must remain separate unless a future callback-composition audit proves a safe merge.
