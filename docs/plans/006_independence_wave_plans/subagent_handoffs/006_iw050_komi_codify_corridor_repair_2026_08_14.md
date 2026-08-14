# IW-050 Komi codify and corridor repair

Date: 2026-08-14

## Disposition

Implemented one package-local decision/effect repair and kept IW-050 fail-closed for central admission.

## Source change

`common/scripted_effects/006_independence_wave_komi_package_effects.txt` now gives `independence_wave_komi_focus_codify_durable_sovereignty` an idempotent Komi package guard, sets `independence_wave_komi_durable_sovereignty`, and applies `independence_wave_komi_apply_major_settlement`. The previous alias incorrectly opened the Pechora corridor, so codification never produced its named sovereignty state and hid the separate corridor project.

`common/decisions/006_independence_wave_komi_decisions.txt` now gates codification on a chosen Komi route, a resolved compact crisis, a stable compact, capital control, and the existing generation-safe project readiness. Its cancellation path mirrors those lifecycle gates. The Northern Ural corridor project now requires a resolved and stable compact, network membership, the League route, capital control, the Komi strategic cost, and the existing generation-safe readiness; its cancellation path removes the same prerequisites.

The repair does not modify central dispatch, content attestation, normal or SCN-008 preflight, deterministic Join, flags, portraits, map bindings, or formable consumers. IW-050 remains package-local and unadmitted because its exact portrait, neutral/route flag policy, and central admission gates remain unresolved.

## Evidence

Both touched source files have balanced braces and no unsupported comparison operators. The Komi decision file contains one founding mission plus ten project blocks, all player-facing decision keys resolve in `localisation/english/006_independence_wave_komi_l_english.yml`, and the repaired codification helper sets the sovereignty flag rather than the corridor flag.

Required probability inspection was run first on `common/decisions/006_independence_wave_komi_decisions.txt` with adapter `mission_ai_will_do`. It returned `PROBABILITY_SOURCE_INSPECTED`, source revision `d863b818b3caabad74526c14c0f85ca622c5d690024e3c266d505fd4e1f5a9b2`, source hash `9583721e8b4a125ac3a6ffb64f30c549d26c8a85e89953b2d4794df3b5860765`, eleven candidates, zero available candidates, fourteen required inputs, and zero inspect-unresolved items. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf99e95cea0461f83eb41ab84345ffcab4195b57da30e08c9d2b48fbcbbfe701/73f74b3281eb786868376248f01530f7b128af04bf5a187e194152a62ed11540/probability-inspect-9583721e8b4a.json`.

Six named empty-fixture scenarios were evaluated as `KOM_EMPTY_FIXTURES_2026_08_14`. The result was `PROBABILITY_ANALYZED_PARTIAL` with 66 rows, 131 unresolved inputs, and eleven never-eligible diagnostics because the adapter cannot materialize the required campaign scopes. No normalized probability, timing, dominance, starvation, or balance claim is made. The evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf1dc652d66b039e02aca19d13549c5468b8f398c8cf1d2d83acf3d712f82589/9ee18790081a0ac676d684a8c895cf82ade5dc111d65ba776a2c05ed21df79c5/probability-25f6c503e8ea3d6d3fd8e7e3.json`.

A same-source comparison using the identical six scenarios and eleven-candidate pool returned `PROBABILITY_ANALYZED_PARTIAL`, `comparisonChanges=0`, 66 rows, and 131 unresolved inputs. This is a capability/current-current receipt, not a before/after balance proof. The comparison artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d74bdc011ed32a259c221ee71b50568095a46f14a3349df2a7028eb99a91ca22/1c7098593e4590cd89ea443eff46e7511605637b817e60de075861637452c70c/probability-fccf22c5ca145c9f009d38b6.json`.

A focused `hoi4.event_inspect` scan for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics; the workspace-wide helper/lifecycle projection remains deferred. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a91a4dd15e6698e15073681c168a726657c5718db6a09950c8c0b9c5e38bd0f/4441996b145e2c44c8e5346e296b3c253713083f34776384f84138f9d4cf9bff/event-scan-741883f50501.json`.

## Remaining boundary

The package remains outside the central 40-adapter / 32-attestation / 29-group authority. Portrait and flag provenance, typed probability fixtures, and the central adapter/attestation/preflight/Join decision remain unchanged and must be resolved before any promotion.
