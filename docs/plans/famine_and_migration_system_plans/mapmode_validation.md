# Famine and Migration Mapmode Validation

Status: current two-mapmode source and tool evidence after mechanic separation.

## Accepted boundary

The implementation adds exactly two dedicated scripted state mapmodes:

- `famine_state_map_mode`
- `migration_state_map_mode`

Both buttons are intentionally visible and understandable from campaign start. This does not reveal either decision category. Famine and migration decisions remain independently hidden until their own problem evidence is present.

No combined mapmode, third route/reception mapmode, full shared scripted GUI, map rewrite, event ID, event-pool row, or event-pacing pulse exists.

## Famine mapmode

The bottom state fill is the primary Food Security classification:

1. stable supply;
2. supply strain;
3. acute shortage;
4. famine;
5. catastrophic famine.

The complementary top border is famine-owned. It distinguishes proven blockade exposure, exact relief route/delivery state where the famine contract owns that receipt, and pressure severity without replacing the stage fill. Catastrophic famine remains visually unmistakable.

The authorized tooltip explains current stage and, for the owner/controller, the exact score, reserves, capacity/need/logistics, pressure components, exposure, blockade clauses, relief status, and recorded famine deaths. Public viewers receive qualitative state rather than private ledgers.

## Migration mapmode

The bottom state fill uses deterministic migration lifecycle priority:

1. trapped population;
2. overcrowded reception;
3. organized evacuation;
4. active exodus;
5. preparing to leave;
6. return readiness;
7. return transfer/outcome;
8. resettlement transfer/outcome;
9. transit;
10. reception.

The complementary top border is migration-owned. It shows trapped or overcrowded obligation, restrictive border policy on an active migration state, exact evacuation-corridor status, normalized reception-load share, or normalized flight-pressure share.

It does not show famine relief, food reserves, food stages, or credited relief delivery. A neutral humanitarian corridor is displayed here only when its operation is migration evacuation, while the famine mapmode consumes famine-relief corridor receipts.

The owner/controller tooltip explains Displacement Load as the primary value, Reception Capacity and Border Policy as supporting values, exact state load, cohort/endpoint role, latest driver, route/corridor proof, integration, resettlement, and return facts. It fails closed on missing or ambiguous identity.

## Runtime producers and cleanup

Famine colors consume only `famine_*` state variables, flags, and triggers plus the famine side of the neutral corridor contract. Migration colors consume only `migration_*` state/country ledgers plus the evacuation side of that neutral corridor contract.

Every colored migration role has a bounded producer and terminal cleanup in migration core, decision, presentation, capacity, corridor, or transfer completion paths. Every famine stage/blockade/relief value is produced and retired through the famine state registry. Neither mapmode performs population movement, death accounting, route selection, or simulation.

Both modes use `update_daily = yes` for visual refresh. That engine mapmode refresh is not a gameplay state scan or event pacing pulse.

## Static assets

The two button families provide selected and deselected 20×18 DDS textures under `gfx/interface/mapmode/custom/`:

- `famine_state_map_mode_selected.dds`
- `famine_state_map_mode_deselected.dds`
- `migration_state_map_mode_selected.dds`
- `migration_state_map_mode_deselected.dds`

They are registered in `interface/mapmodes_interface.gfx`. Production sources, processed images, round-trip evidence, prompts, and contact sheets are recorded under `docs/assets/famine_and_migration_system/mapmode/`. No third button family exists.

## Mandatory HOI4 MCP evidence

### Map route

The current bounded `hoi4.map_inspect` call returned `MAP_INSPECTED` for representative states 1, 64, 282, 290, and 452 at shared revision `24d421bcc68e84bfc6455b892b1ac5855b0ef47d0a746d0ce4a5a91e7851640`. Definitions, geometry, state membership, adjacency, supply, and railway substrate checks passed. The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a75193c5b26cd1180f60405e66b535e35ff3e96ad25d03aeeded209441129c2f/60deb73e299b4ab6ff6bc342e905d5758b8a18037e0444c2bdc859a58a4dfec6/map-inspect.24d421bcc68e84bf.json`; the overview is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06862ee46ae6ff2778002719a3bbd5bcd567fefa7fd3c1da0f612bd363b84d11/b04a6c5d1ff423af5c952585d61d898aebacec114217214d4839c21d5974539b/map-overview.24d421bcc68e84bf.png`. The route cannot execute custom scripted-mapmode color or tooltip branches. Its workspace-wide validation also surfaced unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics after truncation. Those diagnostics are outside this map-neutral feature and are not treated as mapmode evidence.

Earlier successful state-layer map renders prove the underlying state, coastline, port, supply-node, railway, and adjacency representation. The installed map renderer does not render dynamic scripted mapmode states, so those artifacts are not presented as color/tooltip proof.

### GUI route

The current `hoi4.gui_inspect` requests resolved `MapmodesInterface_Ingame` separately under scenarios `famine_mapmode_button_start` and `migration_mapmode_button_start`. Both returned `GUI_INSPECTED`, inspected 101 elements, and recorded shared revision `336679d372c52421672486b9d9669ee1c6a13611e875173b5069539fa9946f3a`. The famine artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c66a568ef6355fef49c8e79834fb3e17af6bfd205bef15f60613b3c31efeace7/7e69181397c82dcff3fcbca3a29f6c7b87eccfbc3e5f3f415eabfae76575ec2d/gui-inspect.336679d372c52421.json`; the migration artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c8cb70c105f50b00654cd023815ebe79190059132311638fce0119c13d8999f/dd31f736876714c8cbd95ece7e41f19e52f7bf5048e6a73076182c9201541ff8/gui-inspect.336679d372c52421.json`.

The matching `hoi4.gui_render` requests covered 1920x1080 and 2560x1440 plus normal, hover, selected, and missing-localisation states for each separate scenario. Both returned `GUI_RENDERED`. The famine artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b917c62bdfce4541d5f58ddc41eaf6ed5884f630a57a3ea88effd5f0cd3cf003/f1478e2488eafb2c91003afba1245a7753ba63e4e171a66f1c7bc9a9f5de4cc3/MapmodesInterface_Ingame-full.svg`; the migration artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b917c62bdfce4541d5f58ddc41eaf6ed5884f630a57a3ea88effd5f0cd3cf003/d72f3f29f41bf35e26d0edd302e2b243d58e9f54e55ff4c273b87cf9c959bae7/MapmodesInterface_Ingame-full.svg`. The GUI route therefore provides current source-graph and static layout evidence for the two separately named mapmode-button scenarios. It still cannot inject a selected custom mapmode—the attempted `selectedMapMode` scenario field was rejected—and it does not execute state-scoped scripted color or tooltip branches. This is not dynamic mapmode or live click proof.

## Remaining presentation blocker

There is no installed MCP route that executes the scripted state-color branches for these custom mapmodes. The current GUI route resolves and renders the button-window layout but cannot inject the active custom mapmode or evaluate state-scoped color and tooltip logic. Final dynamic color, tooltip expansion, selected-button behavior, and live click-region evidence therefore remain unavailable to the agent. No fallback or third UI surface was added.

A final capability inventory on 2026-08-26 confirmed that the installed HOI4 server exposes only `hoi4.map_inspect`, `hoi4.map_render`, and `hoi4.map_rewrite` for map data, plus `hoi4.gui_inspect`, `hoi4.gui_render`, and `hoi4.gui_rewrite` for interfaces. A fresh map query for scripted-mapmode execution again returned `MAP_INSPECTED`; no execution, active-mapmode injection, scripted-color evaluation, or state-tooltip evaluation route was exposed. The blocker is therefore an absent tool capability, not an untried supported route.
