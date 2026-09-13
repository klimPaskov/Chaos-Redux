# Event 006 Statehood Ledger visual evidence, 2026-09-13

Disposition: unresolved, no runtime source edit.

## Outcome and ownership

Event 006, Independence Wave, owns ASSET-039 and the 700x500 `independence_wave_status_window`.
The exact entry is `independence_wave_founding_category` in `common/decisions/categories/006_independence_wave_categories.txt`, which attaches `independence_wave_status_scripted_gui`.
Current category visibility is `is_independence_wave_event6_local_content_active = yes`.
The controller in `common/scripted_guis/006_independence_wave_scripted_gui.txt` uses `context_type = decision_category` and `is_independence_wave_active_country = yes`.
This differs from the older handoff's category-trigger description.

The parent explicitly authorized inspection and concrete presentation repairs only, retained the five founding rows, and prohibited gameplay or shared-interface changes.
Acceptance sources supplied by the parent were ASSET-039 in `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv`, `006_iw006_statehood_ledger_gui_worker_2026_08_06.md`, `006_event6_asset_audit_completion_update_2026-09-12.md`, and `docs/specs/006_independence_wave_specs/quality/package_manifest.md`.
The five-value preservation direction is recorded as parent acceptance within this assignment, not inferred from document existence.

No GUI, scripted GUI, GFX, localisation, gameplay, shared interface, asset, or animation source was changed.
Only this handoff was added.
No staging or commit was performed.

## Diagnosis

The empty-input baseline visibly contains unresolved dynamic tokens and all five tab descriptions overprinted at the bottom right.
Explicit native render fixtures, using the existing source and one visible tab at a time, remove both symptoms.
The government crop and five-tab matrix were visually reviewed, as were the explicit click-region image, active-value crop, and active/long-text/animation matrix.
This is evidence that the layout can display supplied coherent presentation states.
It does not prove that the game evaluates the runtime conditions correctly.

No unambiguous source defect was established for the two reported symptoms.
The controller already defines mutually exclusive tab click effects and panel visibility rules, including a default Government panel when no tab flag is selected.
The old file `common/scripted_localisation/006_independence_wave_gui_scripted_localisation.txt` no longer exists.
Its functions are present in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`, beginning around line 1460.
Their absence from the old path is not missing runtime localisation.

The readout has ten numerical mechanic values, comprising five founding values plus claim intensity, hostility, obligations, patron influence, and network standing.
This exceeds the worker's four-visible-value completion ceiling.
The parent directed preservation, so no values were removed or relocated.
This is an unresolved design-contract conflict, not an MCP capability limitation.

## References and native mapping

The supplied processed reference `docs/assets/006_independence_wave/processed_png/gui/independence_wave_status_panel.png` was visually inspected.
Its named source is `docs/assets/006_independence_wave/source_png/gui/independence_wave_status_panel_source.png`.
The processed artwork is a decorative frame with an open dark central field, without baked controls.
No new reference or raster artwork was made because no source repair was selected.

| Region | Native elements and bounds | Review |
| --- | --- | --- |
| Full panel | `independence_wave_status_panel_background`, 0,0 to 700,500 | Frame covers the intended window and preserves edge illustrations. |
| Header | Title at 26,16, subtitle at 28,48, Animate and Refresh at upper right | Native text and buttons remain separate from art. Utility labels are visibly small and not granted a full typography pass. |
| Founding column | Five metric icons at x24, y92/142/192/242/292, text at x74 | Existing five-value direction preserved. Active-value crop is readable. |
| Relationship/status column | Host, patron, network, phase and mission at x366 | Active crop has readable wrapping. Long-name fixture exists but was reviewed only in the matrix. |
| Navigation | Five tab buttons at x24/142, y380/412/444 | Explicit states isolate the associated detail panel. Seven total controls comprise five navigation and two utility controls. |
| Detail panel | Five native text boxes share x280,y444, 386x42 | One visible panel in explicit fixtures eliminates overprint without source changes. |
| State art | Recognition/dependency at top right, charter/formable at lower right, instability warning at 318,384 | Static and animated siblings are explicitly exclusive in fixtures. Warning is clear of instability text in active crop. |

Current linked sprites are `GFX_independence_wave_status_panel`, four `*_states` strips and four `*_animated` siblings for recognition seal, dependency warning, league charter activation and formable eligibility seal, with `*_static` fallback definitions.
They are registered in `interface/006_independence_wave.gfx` and consume `gfx/interface/006_independence_wave/` and its `animations/` child.
Player text is `localisation/english/006_independence_wave_gui_l_english.yml`.
No identifiers were changed.

Installed `common/scripted_guis/_documentation.md` confirms decision-category attachment, individual `<element>_visible` triggers, click effects and frame properties.
The offline Interface modding and Scripted GUI modding pages were consulted alongside core wiki pages.
The vanilla `interface/sov_paranoia_system_scripted_gui.gui` precedent was inspected for separate background, value text and state art.
This limited no-edit review does not claim the full implementation-reading or visual-acceptance checklist.
The developer-named `references/visual-review.md` is absent from the scripted-GUI skill directory, whose current complete SKILL.md contains the integrated visual checklist.

## Exact MCP calls and revisions

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
All successful calls returned source revision `cddd27b9b2c3db9d16752e6b1678cbebf51f780dd9cd5fb3c6eee0eb4c2283fb`.
All calls targeted only `independence_wave_status_window`.
Requested resolution was 1920x1080 with scenario-level `uiScale: 1` and `generatedScenarios: { enabled: false }`.
The initial schema probe incorrectly put uiScale inside resolution and returned `-32602: Unrecognized key: "uiScale" at scenario.resolution`.
The corrected call succeeded.

Baseline inspect returned 48 event-owned elements, 12 unresolved items and 4 unsupported items.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f009ba0b0900a795f20a240863ca81cb754a90d68f3ef80e2f5e46cfbbc53f3/c5b3ba1c6a408c4d77e5c63e2e0a1d29f7eb69854fb41b9c999fc8634c518dde/gui-inspect.cddd27b9b2c3db9d.json`.

The baseline render used `event006_ledger_baseline_20260913`, no supplied runtime values, and normal state.
Its visually reviewed crop is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e9f30eb962758ee93d79dbcb9aca2e75eacdce13392f2540cfd9f4f8319365c/704aad5d85c20390f82278acca41cafda2f956179328c9247a2c1f54c8588eb5/independence_wave_status_window-cropped.png`.
Its full image is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53aefdbe7e4a7e0980126db1cc6ff63b986ad146c1463fa752e8d0935c76e404/44c4f763eb6d0b09cab9205cfcd1441904d3a938761c18fe592c4f876e32d8d6/independence_wave_status_window-full.png`.

The explicit five-tab render uses `event006_ledger_explicit_government`, `event006_ledger_explicit_recognition`, `event006_ledger_explicit_security`, `event006_ledger_explicit_league`, and `event006_ledger_explicit_ambitions`.
It supplies all ten numbers as zero, the corresponding low/empty descriptive strings, one selected tab and its panel, static status siblings visible, animated siblings hidden, and instability warning hidden.
The supplied country-state strings and visibility are fixture inputs, not observed engine state.
Fidelity is 535 modelled, 1 approximated, 15 ignored, 0 missing, 0 unsupported, and 1 unresolved.
The unresolved item is `independence_wave_status_scripted_gui.visible requires an explicit scenario mock`.
The next fixture can supply `scriptedGui: { "independence_wave_status_scripted_gui.visible": true }` to cover presentation visibility, but that still would not execute the gameplay predicate.
Ignored fields include all seven tooltips, their click sounds and moveable behavior.

The stress render uses `event006_ledger_active_values_warning`, `event006_ledger_long_text_stress` and `event006_ledger_animation_on`, with normal, hover, disabled and warning states requested.
All ten numeric inputs are 100 in this explicitly synthetic stress set, not claimed campaign maxima.
The long patron string is "United Kingdom of Great Britain and Northern Ireland".
Animation time is 0.4 seconds with animated siblings visible and static siblings hidden.
The base active crop and three-scenario matrix were reviewed.
Animation playback is not proved by the static matrix.

No before/after source comparison is claimed because source was unchanged.
Returned self-comparisons of zero changed pixels only show identical comparison inputs and are not repair evidence.
The reduced unresolved count across different fixtures must not be represented as a source improvement.

### Explicit five-tab artifacts

- independence_wave_status_window-full.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f6f6e5eec59f09bbbd52244b9660184ee7b3f6541e8352708a54a4adb1d7138/18ba6e1fb5d2c219dbe518d3147424b685aa931143c127f0385176072cb4dcec/independence_wave_status_window-full.svg`
- independence_wave_status_window-full.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3918764d0cb9165d0bb6743d7e48110bebacfc6d75350354ef4a6834fd5194e4/319c327e688c10fb3461709c8a8a570d8a34ac3bd8b9266f2e63eb14d78fd91a/independence_wave_status_window-full.png`
- independence_wave_status_window-cropped.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af6a685c644a8ec7213785d5091ef7854132f1179633a70601009c6490656086/76b762837892e3949e3ebc0ccd8120aa527b7e128103c222d52f0ffd4ebc5771/independence_wave_status_window-cropped.svg`
- independence_wave_status_window-cropped.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d8f7b226e34ef4c5b86a6867a57b3a5f933febdbfdd50c68fde3db4ab71294f/9815fa6996ce58fc32ec8feafa461dbd447245174ef1cff5f1fd01a2ce5c58ab/independence_wave_status_window-cropped.png`
- independence_wave_status_window-annotated.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4df8e37b428301516878bdff44cda207194f4a193e1f5677745d72e283c8deb/d5a05a70a956796973d489becf7e349a00aadecc0121ccb6882bcada63d47e98/independence_wave_status_window-annotated.svg`
- independence_wave_status_window-annotated.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf76ce82054a72784be5161c49247b2781abce247ba6a76fff6f8ae74a3906df/60167eed195c9902766d1d7cd1b2217919110e7f5cb91b371ea1e9f2a6dad13b/independence_wave_status_window-annotated.png`
- independence_wave_status_window-click-regions.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d0ddec25aa1f335a7dd4ec85fd077527b68b19aa51b7a8a08847547ed3a8074/69e6932b68f3d043318d1ac9ca9f7fdcd60a3f8eb582e0d3a9d66911c1c3f7de/independence_wave_status_window-click-regions.svg`
- independence_wave_status_window-click-regions.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39e9e24aebdfa4290806ab690e37022dab6efc07a7c13f9acde25348608e4465/f4b3024c6ffd778bbd0d8abdaa408f19c3a2401b43982fd09fbf53af57f6fe57/independence_wave_status_window-click-regions.png`
- independence_wave_status_window-source-map.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4307bfe1d08bb4a46f5e2e395ad99fdd2a0692379bb1b9ee2b1f53f760aa09c/e2abbe64852640a57e644fe691cade589d71db63e3e90079ada2e85c4a6a65c8/independence_wave_status_window-source-map.svg`
- independence_wave_status_window-source-map.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15959d602dbf3c321880623b158c32ef0e48a50f6142e4fc461a4b94383c56e0/2a6beb17efe994d54313a8e3a23d54af2831d238ce0eb3367d7d8d5680fc7a93/independence_wave_status_window-source-map.png`
- independence_wave_status_window-hierarchy.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/edb05b09888b81d3a066c7af6a4d759f94cf71130481b07be1239fa41996256e/b78a953afe22aa5477a3400626f84ef4d849de88af794b3acb153749b65ce949/independence_wave_status_window-hierarchy.svg`
- independence_wave_status_window-layout.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d2595e2c6121ac3f4f814479308071ef0ae9e91712e51454388a4461e83b353/c1826bd3578f43f35ec9cb02899be7b9b211fe62e84fd20b338d1cac9e31180e/independence_wave_status_window-layout.json`
- independence_wave_status_window-scenario.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a36a5b3d76e0e41d10e3f6ae50dbb47deefd6b50f2b2ba200bac2bf02216f2c/55537a358b641a910c5f14a3ea7af49636fc2e3d79ad68eeb9e063cdb44f4c94/independence_wave_status_window-scenario.json`
- independence_wave_status_window-fidelity.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5748d2b7d8215f98efca0a532651826244aad8c95dfcb5cd1e2e144c9cad9bea/7e4a4d3c74f423aea7930eab8ebf02d2d2b148c0ddc33040035d89079f627470/independence_wave_status_window-fidelity.json`
- independence_wave_status_window-source-graph.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea0765ce6d17a206c0fc3256bd333c843ba405799c536a76a693d606691b7c56/2a18fde234eb68832dc350f2482714b0a1f299e6f8fe9c015d6e65df9b204c03/independence_wave_status_window-source-graph.json`
- independence_wave_status_window-validation.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7db5f609cc564c56547d60662e75c5e158c45786bc04d9163842a2cb9a9cda03/6f082153b9e557ef528da5f37a91400f50ac262d70e744a8330c6e4b7986e1c0/independence_wave_status_window-validation.json`
- independence_wave_status_window-scenario-matrix.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d2551bd611aecabf8bc0e47c31662177fd33663b8345c6a5a2df9be2dc9744e/67216d9f29fe4f9f27b1bf1aee3877b7f8b6a3c2657f9ffcbc284d1083d4bd10/independence_wave_status_window-scenario-matrix.svg`
- independence_wave_status_window-scenario-matrix.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d03cc9fe52715055d3268062baf5533a476a5aa7e1ccc047739586ef690b42b0/68f49a25f885dab5b91aa909d3b0a6ea7b9078e5662ad523313757ff34e1b7ed/independence_wave_status_window-scenario-matrix.png`
- independence_wave_status_window-scenario-matrix.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/138776b383e433d82c2591d0a1ffee508d5c047113c6880c8cf328140ca5d70a/661a35c4ba4e16d9744277aaaee353905f6f4c25eb365e2d6e36811391975982/independence_wave_status_window-scenario-matrix.json`
- independence_wave_status_window-state-matrix.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1bcb25fad51042cd71e1886513f7e3743259b0a64f0488bbe2240b1dbb0cead/1be10ee96d1b981ac40c85f457873db1a309372798972fa21584adf1b4c673f4/independence_wave_status_window-state-matrix.svg`
- independence_wave_status_window-state-matrix.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e54a58f69c6da53fde6ddbe8d8b55e90aa547c9af0e1ac928495362205c1633/5de8ac5c4bac215a358e53fec389f19eb0fe93314ba7bbbf77a3b49eb8fdebbb/independence_wave_status_window-state-matrix.png`
- independence_wave_status_window-state-matrix.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1da297efa032da4f31b5e23b9a40c0f36ec05531b677777f67839af56d6e395/11dc4da1492e80ba67924117cfad216ea71bdd8d47d622ddd79bbef91b125bea/independence_wave_status_window-state-matrix.json`
- independence_wave_status_window-resolution-scale.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d8422a3a3c0cbeeda1d7c90d8105f7ebd15d5246545e30a9402b326354481dd/cf292cce9d285795843c9789c95de1640530db94d62a6ae98636e3ce3451e5df/independence_wave_status_window-resolution-scale.svg`
- independence_wave_status_window-resolution-scale.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/edd5ddb82b85720fbca247d64a710d35a4b4e4724bf01dec751a22bd538cf678/e79365f901d3129962004a42cbfda6248dd82b2a2509fbf0a3b088dc347bd121/independence_wave_status_window-resolution-scale.png`
- independence_wave_status_window-resolution-scale.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3930e2460b237eaafdc3c9fe202ee776e8ba4c98d7107d69b8ff57cb23d87b7e/c28772f95413a796e10ea9ddc34ab2e8f774090c87022946bfaae80c0721dc67/independence_wave_status_window-resolution-scale.json`
- independence_wave_status_window-comparison.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61d886ac24415882d467119c34444ee3cabcbe77d534eeec8e1d3e9760f0af7f/1909252f6b7e7e31eced17780c176f8eff257dc8824ed797ecaca32d02ed0cf3/independence_wave_status_window-comparison.png`
- independence_wave_status_window-comparison.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/3dcd8b892b458f98acd62811b38ca3b98ecfaf9ad1e00ea51eb8711ee1e4f21c/independence_wave_status_window-comparison.json`

### Active, long-text and animation artifacts

- independence_wave_status_window-full.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfd8fe112312031a7ce859b302a668298f0e4e792f464bd57a631896da4ccf4d/9be939c5f587314d379c12a957ea34615708b17bff0bb7227bf3dd50316a84ba/independence_wave_status_window-full.svg`
- independence_wave_status_window-full.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/beb646d0226dcd6c4ed7debb4bad831315c06e0cf466d73a2a4457ca66a46a67/5eb7bbf8791b0836ca61c37a24335171de2ec4479f9ad76d65827e750bc66715/independence_wave_status_window-full.png`
- independence_wave_status_window-cropped.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/981a2505877b952dfe851fc729531c31d8061277c1a169aef76be193560c7026/8fdf7d117651a33d813a99e29ed795864583a7a4f2a1dd63d7c388ed90e819df/independence_wave_status_window-cropped.svg`
- independence_wave_status_window-cropped.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65bcd983c62f0f9195d455080e1c83326fa7104e09cfd25802fc30ac0a3c5811/c1a425e3da4880ebc949a00c3e50c6386aa3b6b198e95bd84d2ed61d94fb5eec/independence_wave_status_window-cropped.png`
- independence_wave_status_window-annotated.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aed6835f6597efacbf1d1bbd3909b7042c3a780343c32691c0da30966a7657f8/dc306a73148020ffbdbb92797fb9c083cc17f96491f249bd14afc6dcb9bf2963/independence_wave_status_window-annotated.svg`
- independence_wave_status_window-annotated.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42c7e16c58d53e244b081e60c2007a83c488dcc3f29a1409364275d31cb0d178/fd337238a5c0334e325ed4e78dfb18540a6b6f1cbab43e15976d804d65d99fa3/independence_wave_status_window-annotated.png`
- independence_wave_status_window-click-regions.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69f89ff5469061e1599bca3dcb4d9eac71798ae6b2887dc29756246700f0c526/8d0012ab1d0b25f9ef4044e7b043e58faf675a687cae0007a72e9b3da420a854/independence_wave_status_window-click-regions.svg`
- independence_wave_status_window-click-regions.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/672d8f44e29f092ab1df79c1320b2c5983569af2cde0f73c313cbffeca00d664/caa67093163cc42bfb4fbb20c619918a0b6254577ef69d8001bd5535f80f226e/independence_wave_status_window-click-regions.png`
- independence_wave_status_window-source-map.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82bb0a01983e1e9e25f266a7e30219e7dfd08df5a81028554e01e3f53f2948c2/a726bec40e7256c34dc2de8182365406ef513d537d1b183dcd604fcff836232b/independence_wave_status_window-source-map.svg`
- independence_wave_status_window-source-map.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/281fae30522270a80b4cfa722e7d87fc0a22670db74fbeb8442582fff80d03e8/4828db8175fc6f4f3ff324373f25a52e4a6604073e6d8b81aa8498837116c0ff/independence_wave_status_window-source-map.png`
- independence_wave_status_window-hierarchy.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acde4d55b0d1b160309265afe1cc67ab8e581484438397d007e23a15b86dac4c/53c50e2bb0ddeea00109755ed42043fcb86af2796d610c71e8544d52f6b8b26c/independence_wave_status_window-hierarchy.svg`
- independence_wave_status_window-layout.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41af9b35f194078eec72b06fafdb7f1fc66268c80cf7aa3df3c0c8256ac83e01/786754ed5f2862947f5079ff54069bdf5802a9354bff25a0a84b63a183460dc8/independence_wave_status_window-layout.json`
- independence_wave_status_window-scenario.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc1b15366f4f47528f95dda742236407c6b6fdf443a5bbab9b815cc175343bbd/884cbcbb2102e606cbfd9bbda1fb382a2858ba4459d6e328400b7bbdca018025/independence_wave_status_window-scenario.json`
- independence_wave_status_window-fidelity.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/308efa249d5677fd9ba1c210541f2167946215428f4f0513d2e17586d9db9529/f5d1af80a0b286acd18fe4202f1ab8e3d76f6aa2533abc7dd8713ddde6f0fa1d/independence_wave_status_window-fidelity.json`
- independence_wave_status_window-source-graph.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea0765ce6d17a206c0fc3256bd333c843ba405799c536a76a693d606691b7c56/19234f65c6c60dd0570eb147c876bbed667c847090944d42a6f272520082598c/independence_wave_status_window-source-graph.json`
- independence_wave_status_window-validation.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3e539a4085eccd21aeb4bff8a4703ddcff47af7bad903a0e8372529c73a5f95/ecd9edc39519323afb9b9d3253e9abfd415b5851865549a8c0f2f7835004ec8d/independence_wave_status_window-validation.json`
- independence_wave_status_window-scenario-matrix.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dce3d492f1ab07c177e815471b37280c4ed60f2d1aee8f63bcffaa4bbd9e7542/ca287e2ca6406175bda76267d8d85d32b4f1e2bdb898de1d808b0764c3401d0a/independence_wave_status_window-scenario-matrix.svg`
- independence_wave_status_window-scenario-matrix.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0134772bc07c275496ec68780c01567f4187fc3aabd698b2df53a947f64eb4a6/18481e48e7452baebe8917a22caef861c1307e6c9b3d38e7263ce0e3d36b5ec7/independence_wave_status_window-scenario-matrix.png`
- independence_wave_status_window-scenario-matrix.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8763fde8543842d76d2a3c24ccd15df89e57068c4f19cc2f47a6fd9b92856d12/350292937d6d35655e9d26dfa928dcfaf9631e7a7f4b65b20cfa58919bb9e30f/independence_wave_status_window-scenario-matrix.json`
- independence_wave_status_window-state-matrix.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3e14d9c0e6139fe64e948aba4452be98d592bcdf1f786a41695fd15224a14b1/e1dfb7f6e5e76262bcd245b18601c68cd6dccbbb618731a9d7eae09aa9fb022b/independence_wave_status_window-state-matrix.svg`
- independence_wave_status_window-state-matrix.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8aeb7d34ab67aa0026a1101f00fe39e7fea28fe13938964e79bb1277aedf877c/fcaf48ef2b71f43f1da27cb03e9b2f3d466b138600f180193c386f041fc5be3b/independence_wave_status_window-state-matrix.png`
- independence_wave_status_window-state-matrix.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2939869c1ce109a1effce88bf4ac4cee2cfe03764dc63759807825864ef10ead/b79349901096d347698dcd9eeedfa32d74bad4c8033c2a8a9c23cdcd1d2f2898/independence_wave_status_window-state-matrix.json`
- independence_wave_status_window-resolution-scale.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eeaae457cc9fdcbf8fc7c7d7cc180cc862bdd5b72a8b9b099a22b3a088c40054/e563dbe6270d319246b9da5f9c0a0ed6393809fa05c10f59c7f515702e1ef6a4/independence_wave_status_window-resolution-scale.svg`
- independence_wave_status_window-resolution-scale.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acfd9773349d1cdfd9e696d6d44569d86c56f2faeff17b2f775fe404fb5b7390/04f1d7969d58e0e26a4dae35dad54cfbbe13e985c49a8edb5d7fa8829f41c0fa/independence_wave_status_window-resolution-scale.png`
- independence_wave_status_window-resolution-scale.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bed8f580b0b8c5cc5ca56990f86c3215c52794e5e3eebc4a3bea87f9ab09cfe1/003ab57cc4627e6b631d22882f8c64a8bcfbf3d6b1b2694bd6c0ad3f79d075f6/independence_wave_status_window-resolution-scale.json`
- independence_wave_status_window-comparison.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4000e9a0589f4de747ef0e8a82a4477b579c841abcc04c536387bc4e67c73a1/99e82f325e623c9a930d4471da6981f1dcd2c876068ce0e897d7358cedeb9316/independence_wave_status_window-comparison.png`
- independence_wave_status_window-comparison.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/c20e1cb30edd9a8c25842d9954823591422c1d06ff94b6d0e70792debb3708d5/independence_wave_status_window-comparison.json`

## Retrieval and inspection limits

One-shot resource reads truncated binary data and the initial image could not decode.
Recovery used the documented `?offset=<bytes>&length=12000` resource ranges, reconstructing PNG base64 in offset order.
The baseline crop was reconstructed from 53 chunks through the final tail, then successfully displayed at 716x516.
The explicit and stress images were recovered by the same bounded mechanism.
No artifact regeneration, installed-server change or source-only substitute was used to bypass image review.

## Remaining work and omissions

- Overall ASSET-039 status remains unresolved and cannot be promoted to complete.
- Four blendframe shader effects remain unsupported in the empty baseline and animation-on evidence cannot establish playback.
- Baseline diagnostics name missing inferred static fallbacks even though explicitly named static definitions and state-strip siblings exist in source.
  No unsupported fallback field or guessed sprite alias was added.
- Runtime category visibility, state calculations, tab trigger execution and selected-state synchronization remain parent-owned integration questions.
- Click-region image was reviewed for seven separated visible controls, but full painted-bound/glyph-centering assertions and edge interaction testing were not completed.
- Tooltip rendering, moveability and click sound are omitted by the renderer.
- No complete per-control normal/hover/selected/active/disabled/completed matrix or per-tab native-size long-text review was completed.
- Full-window, annotated, hierarchy and comparison artifacts are linked, but not every linked image was independently inspected.
- No post-edit inspect/render cycle exists because no source edit occurred.
- The four-visible-value rule conflicts with the preserved accepted display and remains explicitly unresolved.
- Gameplay payment, AI, balance and Refresh helper behavior were outside this assignment and were not audited.
  Navigation and Animate introduce no displayed spendable costs.
- No asset substitution, value removal, gameplay simplification or shared-interface change was made.
  This is a partial visual diagnostic handoff, not a completed GUI implementation.
- Live-game validation remains user-owned and was not performed.

Skills used for this bounded review: chaos-redux-scripted-gui, chaos-redux-subagents, chaos-redux-event-assets, chaos-redux-frame-animation, chaos-redux-decisions-missions and chaos-redux-events.
No skill was modified.
