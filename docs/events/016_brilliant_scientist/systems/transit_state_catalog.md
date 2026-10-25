# Transit endpoint geometry catalogue

The private two-site commissioning system uses a lazy state/province membership query as an input to exact endpoint binding.
The catalogue contains all provinces belonging to each current source state, including provinces that have no baseline supply node.
It stores no runtime node, controller, damage, payment or entitlement state.
Current node and control predicates must evaluate candidates independently before an endpoint can be accepted.

## Query and source ownership

`brilliant_scientist_transit_load_state_province_catalog` runs in the selected STATE scope.
The caller owns the temporary numeric state ID, province array and loaded status before its nested invocation.
The query obtains the numeric history-file ID with documented GetID/meta_trigger, then follows a balanced generated dispatcher to one exact membership leaf.
It clears its outputs first and supplies an empty array/false status for an unknown key.
It does not scan all states or initialize a world registry at startup.

The retained source is the verified MCP map catalogue at revision `34b40fa7ff00cf49602d57615f525b0ec820972e86e8c1676f6779eef2a99f6f`.
The input covers 1,081 states and 10,272 unique assigned provinces, with at most 70 provinces in one state.
Source geometry, membership and network checks passed; the overall map result also contains localisation errors and floating-harbor review warnings, so it is not clean-map acceptance.
The dataset and generator retain exact source paths/hashes and do not copy unit/building position or model data.

The public contract and usage example are in `common/scripted_triggers/016_transit_state_province_catalog_triggers.md`.
The existing player-triggered CXT native-ownership probe observes its current capital state's numeric ID, province count and loaded status.
It grants no content and adds no periodic hook or setup package.
No icon, sprite, texture or gameplay window is added; the existing debug action remains the consumer.

## Evidence and future implementation

`python .tools/events/build_event016_transit_state_catalog.py --check` verifies byte-exact generated source against the retained membership input.
`python .tools/tests/test_event016_transit_state_catalog.py` executes the actual generated query/dispatcher and compares every state to the independent MCP membership oracle.
Its 1,114 source cases include all known states, invalid/fractional keys, sequential queries, partial temporary initialization, CXT guard/capital/observation execution and generator refusal boundaries.
Native GetID expansion, scope behavior and runtime performance remain separate engine evidence.

The full private commissioning requirement remains +1 infrastructure in each selected endpoint and a level-two actor-controlled railway between verified supply endpoints, with frozen paid bindings and partial-construction recovery.
The exact current special supply-node reader, selected-node health and whole-edge level/damage predicates are not verified by this geometry query.
The runtime architecture review records those unresolved capabilities; an aggregate building count, static supply_nodes.txt entry or another railway in the state cannot replace them.
Geometry changes require explicit catalogue regeneration from a new checked MCP revision, while runtime construction and control changes do not.
