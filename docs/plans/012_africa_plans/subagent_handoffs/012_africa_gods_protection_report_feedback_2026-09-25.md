# Event 012 Gods of Africa protection-report feedback

Disposition: implemented in source; structural validation is partial, while engine behavior remains unverified.

Acceptance basis: the active Event 012 implementation goal requires complete player-facing effects and descriptions. The completion audit identified that the protection report did not show which conditional services succeeded. This bounded source change adds result reporting without changing Event 012 costs, Event 013 costs, cooldowns, or service eligibility.

The user's accepted boundary remains in force: Event 012 protection has three base cost types and at most one conditional convoy/train cost; the common-defence reserve is a ledger check and decrement for the same infantry shipment, not an additional material payment. Event 013 retains its full existing price in its own Foreign Disaster Relief choice.

## Implementation

`events/012_africa_gods_of_africa.txt` expands the host-side `chaosx.nr12.610` option with conditional tooltips for active guarantee and access relations, successful intelligence sharing, convoy or train delivery, eligible-capital reconstruction, installed Migration reception capacity, and the participant's stability or war-support reward. If mutual market access is absent, the report names missing Arms Against Tyranny, a locked Sanctuary capability, or an unconfirmed outcome. If intelligence sharing is absent, ordered checks name the first failed gate: La Résistance, Security, the host agency, the participant agency, an African war, or an eligible enemy the participant is not already fighting. Other omitted services retain grouped condition guidance.

`common/scripted_effects/012_africa_gods_effects.txt` writes four transient participant flags only after intelligence, convoy, train, or capital-work effects occur. A shared cleanup effect clears these per-action flags before a new protection transaction, when the compact is withdrawn, and after the `.610` report is acknowledged. Existing relation and Migration receipts remain intact for their later owner cleanup.

`localisation/english/012_africa_gods_l_english.yml` explains that conditional services appear in the report details, reports each active or completed service, names the first failed market-access or intelligence gate, and describes grouped gate classes for other services not listed. The separate Event 013 relief choice remains explicitly separate.

`docs/events/012_africa/gods_of_africa.md` records the report behavior. The authoritative event workbook and its CSV exports were not changed because catalog-facing event and evolution text did not change.

## Validation evidence

The source audit found all 11 referenced `gods_of_africa_protection_service_*` tooltip keys in the Event 012 English localisation file. Each of the four transient flags has one writer, one cleanup declaration, and one reader in the `.610` report. The localisation file retains UTF-8 BOM encoding.

The pre-edit focused Event 012 event lint/render revision was `f38750d657aae964fc445b75e7bd6dc5ca78a5f72ff6779d08ba080a8eaded7e` with graph hash `0bc7b2ecdd292bf90391ac6caec342ef3b21516bfee286bb5fd82f5cfa352cc4`.

Post-edit `hoi4.event_inspect` on `{kind: "event", eventId: "chaosx.nr12.610"}` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, revision `811e61df0f66e2986e5ba3d637f8f755945d0c067de0b312c964852355901694`, graph hash `4d1c6fc2b78e2871312bd7c3170c33e645624c4434b6a148075f9cce323839a3`, and zero blocking diagnostics.

Post-edit `hoi4.event_render` for the same selector and `view: "options"` returned `EVENT_RENDERED_PARTIAL`, status `ok`, layout hash `b8ffa7f8f00ff1d13c0dce300c29e8201a47a8be1d2eecccc632c8a2d939d152`, three selected nodes, 42,850 omitted nodes, and zero blocking diagnostics. Both calls deferred workspace-wide helper and lifecycle projections and reported the inline inventory limited to 64 of 384 source paths.

`hoi4.event_compare` was attempted between the pre-edit and post-edit revisions of the earlier success-feedback edit but returned `EVENT_REVISION_NOT_CACHED`; no event-graph diff is claimed. The previous revision was no longer available to the compare route after the source changed.

For the ordered market-access and intelligence blocker refinement, the parent reran `hoi4.event_inspect` in lint mode on `{kind: "event", eventId: "chaosx.nr12.610"}` and received `EVENT_INSPECTED_PARTIAL`, status `ok`, revision `f737d8d5eb3e07985d0b73c706f872a0ccada3c8856c1f2fc0b0984806ade4e9`, graph hash `469de8cac41e98cb61cbf33478fcb289e2ee86b787796178ee08fbe11934a130`, and zero blocking diagnostics. The linked lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/379b7e9a7271fa36dc43087fc780c312a5786fb616e27f7b453d57304b8f155a/733001572183d633cd332ef803f3498e81198a9ce7c1fc121bea8340fc99f06a/event-lint-f737d8d5eb3e.json`.

The matching `hoi4.event_render` options view returned `EVENT_RENDERED_PARTIAL` at the same revision and graph hash, with layout hash `b8ffa7f8f00ff1d13c0dce300c29e8201a47a8be1d2eecccc632c8a2d939d152`, three selected nodes, 42,850 omitted nodes, zero rendered branches, and zero blocking diagnostics. Its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30cb33af1f575e9edfd41a4e15487bf8158c49f3fae63d057c205794025e96a7/60cbdc640362656505c6f9670f635709481d5d09813c533766c141756119ff70/event-options-f737d8d5eb3e-manifest.json`. Both latest results defer workspace-wide helper and lifecycle projections and list only 64 of 384 inline source paths. A fresh `hoi4.event_compare` from the previously accepted report revision `811e61df0f66e2986e5ba3d637f8f755945d0c067de0b312c964852355901694` to `f737d8d5eb3e07985d0b73c706f872a0ccada3c8856c1f2fc0b0984806ade4e9` returned `EVENT_REVISION_NOT_CACHED` with “Requested event graph revision is not cached.” No graph diff is claimed.

## Remaining limits

The report now identifies the first failed market-access and intelligence gates, but omitted guarantees, military access, transport, reconstruction, and Migration reception still have only grouped reason guidance. The event graph output is partial, so helper coverage, lifecycle projections, runtime tooltip substitution, and conditional outcomes remain unverified; no live campaign or owner-system execution was run, and the user retains live-game validation. A successful before/after event comparison remains unavailable. No weighted logic changed, so no probability target or probability comparison was introduced by this tranche.

This handoff closes the source-level success-feedback finding only. It does not complete the overall Event 012 goal or resolve the wider focus-route, scenario-acceptance, image-content, game-scale, or live-game questions. The accepted report-art mapping is recorded in the Event 012 Gods implementation docs.
