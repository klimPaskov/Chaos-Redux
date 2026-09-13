# Event 23 affordability parser repair

Four invalid political_power comparisons in common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt use the supported country trigger has_political_power.
Each remains NOT = { balance < cost }, preserving inclusive affordability and all existing constants, scopes, payment paths, and other resource checks.
This is an isolated parser correction within the user-authorized protected-package exception; no redesign, cost adjustment, or weighted AI change was made.
Installed documentation/triggers_documentation.md documents the country trigger; the offline Triggers page states the strict comparison boundary, and vanilla common/decisions/anti_japan_infiltration.txt line 21 provides a less-than precedent.
The immediate original is under pre_patch_event23_pp15/ and full-file transformation hashes are in event23_pp15.json.
Launch 14 records eight diagnostic lines for these four conditions; native retest remains pending.
Live below-cost, exact-cost, and above-cost payment tests remain pending.
MCP trace returned EVENT_INSPECTED_PARTIAL, with workspace-wide helper projections and lifecycle checks deferred.
Trace artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/938ad842e5e24d280bf1db31e31cbcfb1cb20335074921ea7b56ea4f2a738f0d/42d792eb3c9abbb85566b7c0fb566f665778866af568ff75248920e4e83a0796/event-trace-94c858964b40.json

MCP neighborhood rendering returned EVENT_RENDERED_PARTIAL; linked manifest: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6047ade4958970e235d0eb52c8540af93a07e8cfc991070bfe0d9bcb41f5975/2e8bd6719086459fa2b1038fbd8903f712d6b0ab5a84f480ec6a20db40d53b3d/event-neighborhood-94c858964b40-manifest.json
The before-revision comparison returned EVENT_REVISION_NOT_CACHED with no comparison artifact; no helper-level MCP pass is claimed.
