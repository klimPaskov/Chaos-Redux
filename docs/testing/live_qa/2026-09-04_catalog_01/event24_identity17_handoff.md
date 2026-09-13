# Event 024 host identity parser repair

Disposition: implemented as a single parser keyword correction authorized by the parent within the user-approved safe QA repair scope.
Live acceptance remains pending the parent run.
No source writes follow this handoff, and no launch or commit was performed.

## Source change

`common/scripted_triggers/024_video_game_in_sweden_triggers.txt:48` changes only `is_same_country = ROOT` to `tag = ROOT` inside `video_game_in_sweden_is_current_host`.
The entire helper was read before patching.
The flags `video_game_in_sweden_host_selected` and `video_game_in_sweden_program_active`, the `has_event_target = video_game_in_sweden_host` guard, the event-target scope, the `ROOT` target, and the final `video_game_in_sweden_is_valid_host` call are byte-for-byte preserved.
The valid-host helper still checks existence, Swedish origin, capitulation, and the existing territory conditions.
No call site, original-tag condition, target persistence, cleanup, tuning value, weight, or player text changed.

## Syntax and identity proof

Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:7649` documents `tag` in COUNTRY scope and explicitly lists ROOT among its supported targets.
Offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:282` defines the `tag` trigger as checking whether the current scope is the specified country.
The next entry distinguishes `original_tag`, which tests origin and includes other countries sharing that origin.
Thus `tag = ROOT` compares the actual country selected by `event_target:video_game_in_sweden_host` with the country designated by the enclosing ROOT context.
It does not substitute the static Swedish tag or accept another country merely because it originated from Sweden.

Vanilla `common/scripted_triggers/00_scripted_triggers.txt:278` uses `tag = ROOT` within a CONTROLLER country scope in `is_controlled_by_ROOT_or_subject`.
This is the same country-scope-to-ROOT comparison structure.
Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:245` explains that ROOT remains the inherent root of the enclosing context when entering nested scopes.

The preserved identity relation has these consequences, assuming the other helper guards pass:

| Saved host | ROOT country | Identity predicate |
| --- | --- | --- |
| Same country object | Same country object | True |
| Different country | Different country | False |
| Swedish-origin country A | Distinct Swedish-origin country B | False |
| Dynamic host country A | That same dynamic country A through ROOT | Actual identity comparison, with no origin-group substitution |
| Missing saved host | Any | Existing `has_event_target` guard fails |

These are documentation-backed semantic checks, not live runtime observations.

## Caller inventory and preserved scope concern

The complete direct caller inventory with context is `pre_patch_event24_identity17/caller_inventory.txt`.
Calls occur in Event 024 decisions and mission checks, owner-side effects such as maintenance, evolutions, validation and foreign dispatch, other Event 024 eligibility triggers, and Event `.40` and `.41` triggers.
No focus or GUI source directly calls this helper in the inventory.
The country-root decision and maintenance callers compare their ROOT country against the saved host while evaluating the existing host flags and validity checks.

`events/024_hearts_of_iron.txt:484` calls this helper from an explicit host scope inside Event `.40`, whose event recipient is the foreign partner.
Entering the host scope does not automatically rebind ROOT to the host.
This correction deliberately preserves the requested ROOT comparison, so it does not resolve a possible mismatch between that caller context and the helper's intended use.
This is a recorded caller-scope concern requiring separate parent review, not grounds for replacing ROOT with THIS, PREV, an original tag, or a new event target in this parser-only patch.

## Evidence and validation limits

Fresh launch 16 `logs/launch_16/logs/error.log:393` and line 394 report invalid and unknown `is_same_country` in the owning trigger file at line 48.
The exact pre-patch file is backed up under `pre_patch_event24_identity17/common/scripted_triggers/024_video_game_in_sweden_triggers.txt`.
A source hash guard verified that the file had not changed between reading and writing.
Reversing only this exact replacement reconstructs the original bytes, preserving concurrent and earlier work in this file.

- Before SHA256: `59f0e97d7a2aa41db9ca584ce3bb19845f9bbc3512d27da30c545d9743b7de3a`
- After SHA256: `dfebdb19d1ed7e513d3d230fc1c02c9420d562fbef58ff078620b6cc97342394`
- Exact patch proof: `pre_patch_event24_identity17/patch_evidence.json`

Required read-only event MCP routes were attempted and their full responses and artifact URIs are preserved in `pre_patch_event24_identity17/mcp_evidence.json`.
`hoi4.event_inspect` traced the maintenance event `chaosx.nr24.90` with helper expansion, depth 1, 12 nodes, and 20 edges.
It returned `EVENT_INSPECTED_PARTIAL` at revision `1e7516fb00135d5559a8dfcc786dbeaeac9e3850d4f17dad626bbe811df96bc0`.
`hoi4.event_render` rendered the scope view for the direct nested caller `chaosx.nr24.40` and returned `EVENT_RENDERED_PARTIAL`.
Both responses explicitly deferred workspace-wide helper projections and lifecycle analysis, so neither proves helper scope correctness.
Post-patch `hoi4.event_compare` against the captured revision returned `EVENT_REVISION_NOT_CACHED` with blocker `Requested event graph revision is not cached`.
There is no successful MCP comparison or live acceptance claim.

## Completion boundaries

The authorized single-line parser correction is implemented.
No fallback or gameplay simplification was introduced.
The caller-scope concern and MCP comparison limitation remain explicit.
The other Event 024 malformed constant-token errors visible in launch 16 are outside this one-keyword assignment and were not changed.

No helper was added, no helper input or output contract was redesigned, and no constants, cleanup hooks, assets, localisation, or catalog rows changed.
This handoff documents the existing helper's preserved identity contract.
Previously read skills used for the bounded work are `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and the relevant QA repair discipline from `chaos-redux-debug-playtest`.
No skill was created or updated.
