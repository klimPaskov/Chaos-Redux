# Event 006 current completion audit v2 (2026-08-14)

## Disposition

Event 006 remains **HOLD / PARTIAL**.

This audit does not make a whole-event completion claim and does not change the current authority boundary of **40 runtime adapters / 32 content attestations / 29 compatible reservation groups / 161 unattested selectable rows**.

IW-047 MEL and IW-050 KOM remain package-local and absent from central adapter, content-attestation, preflight, dispatcher, and Join admission surfaces.

The eight current adapter-only rows remain fail-closed: IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM.

No gameplay, asset, localisation, GUI, focus, workbook, or catalog source was edited by this audit.

## Highest-impact bounded requirement found and closed

The audit found that IW-050 Komi had no writer for its required command-roster readiness receipt, which prevented its package-local setup from publishing `independence_wave_iw_050_setup_complete`.

The parent applied the bounded repair in commit `109e6e734` while this audit remained open.

| Evidence | Current source fact | Consequence |
| --- | --- | --- |
| Pre-fix `common/scripted_effects/006_independence_wave_komi_package_effects.txt:309-313` | Setup cleared `independence_wave_package_setup_complete`, `independence_wave_iw_050_setup_complete`, `independence_wave_command_roster_ready`, and `independence_wave_komi_roster_checkpoint`. | Setup correctly began fail-closed. |
| Pre-fix `common/scripted_effects/006_independence_wave_komi_package_effects.txt:332-340` | The accepted setup branch called `chaosx.nr6.350`, installed laws and politics, initialized the two pressure variables, and started the compact lifecycle without writing a Komi roster receipt. | The shared readiness flag could not become true. |
| `events/006_independence_wave.txt:186-350` | Hidden roster event `chaosx.nr6.350` contains no KOM branch, no `KOM_pavel_murashev` check, and no Komi roster receipt. | The repair correctly remained package-local rather than widening `.350`. |
| `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:91-93` | `has_independence_wave_komi_command_roster` correctly checks `has_character = KOM_pavel_murashev`. | The installed vanilla character can be the bounded checkpoint input. |
| `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:146-207` | `has_prepared_independence_wave_iw_050_package_setup` requires both the Komi character and `has_country_flag = independence_wave_command_roster_ready`. | The new helper now satisfies the roster-specific half of this gate without bypassing its other requirements. |
| `common/scripted_effects/006_independence_wave_komi_package_effects.txt:312-318` after `109e6e734` | New idempotent helper `independence_wave_komi_checkpoint_vanilla_roster` requires the exact Komi package and `KOM_pavel_murashev`, then writes both the local checkpoint and shared readiness flags. | The missing writer now exists with the accepted vanilla-carrier gate. |
| `common/scripted_effects/006_independence_wave_komi_package_effects.txt:343-346` after `109e6e734` | The setup calls `.350` and then calls the new package-local helper exactly once. | The writer runs before laws, politics, force preparation, and the prepared-setup test. |
| `common/scripted_effects/006_independence_wave_komi_package_effects.txt:381-386` after `109e6e734` | Both setup-complete flags remain written only if `has_prepared_independence_wave_iw_050_package_setup` succeeds. | The repair restores the declared gate without bypassing any other setup requirement. |
| `common/scripted_effects/006_independence_wave_komi_package_effects.txt:423-428` after `109e6e734` | Generation cleanup clears the local checkpoint, shared readiness, and package setup-complete flags. | The repair remains generation-safe and fail-closed on cleanup. |
| `common/scripted_effects/006_independence_wave_mari_package_effects.txt:353-360,389-394` | MEL has the accepted local precedent: an idempotent vanilla-roster checkpoint checks `MEL_zinovy_zhadinov`, writes the package checkpoint and shared readiness flags, and is called during setup. | The Komi repair now mirrors the established package-local pattern without widening shared authority. |

The pre-fix documentation overstated this surface.

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw050_komi_country_core_2026_08_14.md:14` and `006_iw050_komi_package_completion_audit_current_2026_08_14.md:23` claim a vanilla `KOM_pavel_murashev` roster checkpoint, while `docs/events/006_independence_wave/komi_package.md:41` calls the package-local effects source-wired.

The writer now exists, but the documents still need a durable `109e6e734` implementation receipt and the post-fix MCP limitations below.

### Owner patch disposition

Commit `109e6e734` changed only `common/scripted_effects/006_independence_wave_komi_package_effects.txt` for this repair.

It added the idempotent package-local helper described above and called it immediately after the synchronous `.350` call.

Static re-audit found exactly one writer for `independence_wave_komi_roster_checkpoint`, exactly one setup call to the new helper, and retained cleanup clears for both receipt flags.

The patch did not add a KOM branch to `.350`, change central adapter or attestation lists, widen normal/scenario preflight, add a Join branch, or alter MEL.

The repair restores an already-declared package-local contract, uses the installed vanilla carrier, and leaves the 40/32/29/161 authority and fail-closed central MEL/KOM admission unchanged.

Fresh focused event inspection of `.350`, the Komi effects file, and the Komi trigger file returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics.

Fresh `.350` neighborhood rendering returned `EVENT_RENDERED_PARTIAL` with zero selected blocking diagnostics.

## Completion status by accepted specification surface

| Accepted surface | Status | Current evidence and remaining gap |
| --- | --- | --- |
| Part 1: core system | Partial | The active ladder remains 3/4/5/7/10 with World Collapse at 10, the allocator audit reports 40 adapters, 32 attestations, 29 groups, the exact eight adapter-only rows, and a 20-package standalone capacity witness. The accepted 193 selectable candidates plus 13 overlays remain incomplete because 161 selectable rows are unattested. |
| Part 2: event flow and evolutions | Partial | All twelve current Event 006 event source files received fresh inspect and render passes, and the five evolution incident families remain present. Every event result is partial because the server deferred workspace-wide helper projection and lifecycle analysis, and the requested historical compare revision was not cached. Package-local MEL/KOM still cannot be treated as admitted flow; the Komi local roster defect is closed by `109e6e734`. |
| Part 3: mechanics and decisions | Partial | The Statehood Ledger, shared decision families, package decisions, and current project lifecycles are source-present, but the full candidate matrix is not implemented. `109e6e734` restores the roster-specific input to IW-050's setup-complete gate without bypassing the rest of its setup contract. Decision AI and weighted mission evidence remains adapter-limited rather than quantitatively proven. |
| Part 4: focus architecture | Partial / HOLD | Fresh focus evidence resolves 184 focuses and 196 connectors with zero crossings, zero node intersections, and two long connectors. Four authored linear detours and the two long connectors remain accepted layout debt, while aggregate blocking diagnostics include missing vanilla continuous-focus sprites. Five Komi helper calls are source-present but do not make the blocked Komi package reachable. |
| Part 5: country packages and overlays | Partial | Thirty-two packages are centrally content-attested, eight more are adapter-only, and 161 selectable rows remain unattested. MEL and KOM remain package-local and unadmitted. Komi's effects/triggers/ideas/decisions/localisation/focus calls and local roster receipt are source-present after `109e6e734`, while its portrait and flag provenance gates remain open and MEL retains its own portrait/neutral-symbol admission gates. |
| Part 6: formables, League, and SCN-008 | Partial | The 32-cell scenario matrix and eight edge cases pass statically, and FORM-16's exact ARM/GEO/AZR state contract passes its dedicated audit. The grouped formable-state GUI is source-present but lacks family-isolated visual acceptance; many formables remain unavailable because their member packages are unadmitted. Super-event 23 remains blocked on rights-cleared audio, wrappers, and firing; super-event 24 is source-wired but only partially reachable behind factual host, collision, transaction, capacity, and formable gates. |
| Part 7: AI, balance, assets, achievements, and acceptance | Partial | The 102-tag flag audit is complete and the sixteen achievement definitions/localisation/icon triplets pass static parity, but signature achievement reachability inherits package admission blockers. The mandatory current probability audit remains bounded by installed adapter limitations and cannot support campaign balance claims. Character portrait handoffs and durable grounded-source evidence remain incomplete for unresolved carriers; no custom Event 006 3D unit is accepted in current scope. The workbook correctly reports Event 006 and Liberations as Partially Available and SCN-008 as Unavailable. |

## Event MCP evidence

All twelve current Event 006 source files were inspected and rendered at event graph revision `d21fdfa2723e4a624054076fb1104ba638c4fbb1f733358a99b24aac1839ace2` with graph hash `4223118f94e6920016241a8b9cd25da3e9dd5fd0103899eb9fd36238159df415`.

Every scan returned `EVENT_INSPECTED_PARTIAL` and every render returned `EVENT_RENDERED_PARTIAL`.

The selected event sources produced zero blocking diagnostics, but validation remained false because the tool explicitly deferred large-workspace helper projections and lifecycle passes.

| Event source | Selected render nodes | Inspect artifact | Render manifest |
| --- | ---: | --- | --- |
| `events/006_independence_wave.txt` | 73 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d15b55b2584d3c9174ee2451cdb61a9601f50aa8f12486d17b3ae2a241c0587/70446c74c458b1c100f71454e5053931499ef3f58af3f45a75171ba4f00f45ee/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce2c351709b3d79db4aeafd11068f20beb0297c33d9f8cfdff692faf3957c082/9d87f3bcc5d6b9dcf6ccb855ff30c5ad847935ca6ba9479fd64c4afaa573b325/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_join.txt` | 13 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e177b393cd803d68df5db5407cc71ed1a931d103b188c35ebefada83442a230/3af2537a34ed2f0ba82a023fe063ee01c8df954b213eeb2c42b49d7c291db840/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aee5b32c25501cbc01d133654b31c71cd095110d615d01ce5bd6e25be3a76671/a18ec67831d45516bbe659742ef460ade1a2322e69202e01009674945c279b07/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_scenario.txt` | 10 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce628077e44862eddaa4fff8858562b18fc01f159de0e28b612937a71fb453d1/dd492f92a888a6581f9cebc60e1c20503dcd08c5613100dd852f788c0d445bdc/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a36de1fca16c274807acb818e84cdc3e818e9740eedaac3218095d68c71936f9/b3073b7fc8489fe2d37785108032e68b496f1ec322a4752b9d8468801c2bd11b/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_rhineland_bavaria.txt` | 36 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19a8f0f0fb12cc5e07c9ec1377ab8f910571cd1c88203fbb5826a3f9d8651aaa/1507e869ff63ba4cb79bec33cc58c473a723a0b9aca191dfabcb4310c2ce2ddc/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4c1412b950026a1ec1a28482a4e3234d77b22f2f3e7e7ad1cb84d90e6795bf0/96549e718a145ac9b16bf49df116c9b90537ee9017a0fc0a5f941f5459e5ecd2/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_wallonia_frisia.txt` | 15 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52ab25b1970ff1c92e93b81548ae3643d0c4f9496998a1d9e4b894ed349ad54e/23b3f10df160a23e2709dd61c075bc3b50d8c9b71cca225f7203de71c10e4e3d/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50122fb235c82d54728b129afbb8cc9a0c75f3261ece847439ca8fb3dae4acc3/0b2f9db0536596a005f6fd47036e5a8e5b139cd775a31bf1d10eec712fa7c4c5/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_mediterranean.txt` | 50 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aab859c6561d1d021cf4c94cb2aedebd45e7c3ea03605afa28c634919ef6fd72/8b686cf22b224fdc96b2cfaa8edd2d5a5ad18c5de6dbb213c66d5fda35655fae/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85f1e670c840335284512fc58642c3c39a31cb1b587a3d5b78f454ce9033a2f1/3760569dbba68be2157e13c09738c4013791c3da5f9de589558f7cde98157118/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_form01_02_04.txt` | 39 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/743aa4f57c6e8eefdc1aff34062f857673b1f5a0ea22e88ef14e8167d64ec4fa/f6aa246866fd9d133baecf20c4723567395a3ad5a15c4526e8a456be1f6ece12/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a433ece876aab5470396a5cf49eb2e1fa8a7c05b69f19a39c2d08221fe815db6/b7d0c85bce91a38b52e57d31dd03ac4ab7d04664f7fd45c9451d3debc79e22fd/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_form05.txt` | 27 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc7fa975ab25597dbb1a9c56bdb32a66a6bcd8b253a4968b2ebdded296454964/2c763d70587731b4eb86c80f45bde39a323e479d3aafb1720b551d286f3bb22c/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/34ac3b72101c108c490edb3e7d97f33cdfed23aae987d73adef3faa367ca8b4a/720ca5db5617030934acffe60d066cc9e025fbd17f4bc73b3d07ced1afa28cd4/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_form16_events.txt` | 5 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fdc0e28a58c049e5bffaf01dd15613cdaa241bbc1ab94cd597276e0b95ae52d/743997dcda140add6119a263e68c39b99efffd9ca89804797283770cfd4c1d4d/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21f791e6f84d6f84468b19d4ac5ffaf7279842b919490dfc21ca49846c8c64a2/cf599aa1c903e68200fa517cdabba275be1dc32cdb3025d1037bcfa3c9232436/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_iw043_iw058.txt` | 205 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6aa67fc398dd72febbc4a4beaaf824a6fe3d6dc8a8a4ec9b526653fe1d03d8ad/6d0d07ec5ec3d19482fe7324c60791e6eb3018a851bdb6a138678440ddd43226/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef7a3735f82e151ac0b44226b645bc9a26458caf063f70b00479f4c4803681d9/4664459a02033be9d814e20e1b6db0a35a3cfd773f17d07c66fa2a9ba20d4714/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_iw093_iw098.txt` | 40 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3467d15ce70d50a607958260aa4a7e93b98ea089b693a250d3b4bb663a630539/a881766c483c80a603496ad9e0f179a260a12139e41a2b242a9f5e85204868f1/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e13b0ee333dc32f99258cf3ae48ce8e5113154dcccb1ed723013e478b781e79/d24687ec7937e828d4c3e397c83073a90af0fecc42aba0b1917dcbc1b7176f3d/event-overview-d21fdfa2723e-manifest.json` |
| `events/006_independence_wave_evolution_incidents.txt` | 25 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/918624b4cdd0d7e3bc5525aacb44ec653cf014eafca2b6bb45ce487a13881624/52326f8a7702a33d08220accb230f7fc888a6fde8b9a3acc4b3761e3fc631ccd/event-scan-d21fdfa2723e.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16ea66cc8567576d94fc6bd4b434ac166dcc424394322d635247ebb7b6f3b436/6206a5293cd8c8076eb02df0cc0e15dd61b1b69108e0735010ef553cc0604dc7/event-overview-d21fdfa2723e-manifest.json` |

Focused event scans of the Komi effects and triggers independently returned `EVENT_INSPECTED_PARTIAL` at the same revision.

The post-fix effects artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9459a728b2f76dcf6a37fa0e647af213e340824896b990bfbe2ef224727a289/e57bacee4084ae1d61d1ca9752456a2941c3762863d5f242c6ad6e0abfacf297/event-scan-d21fdfa2723e.json`, and the post-fix trigger artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85f0d72c82e0c9379a013d0bd63c4c95ed71f20e8dbe80fba6533f320d541f6e/6791a218e4d12e52b8fff111f3e68607837c839f794673cf2d83de2384b7e48b/event-scan-d21fdfa2723e.json`.

The post-fix `.350` inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b7ca6b2840db39a70fb90bec3be232e38ac64c76868addb7a507800d4def9f7a/d1a1435025f4b2ad36073b2228f1c7794696dff4e26952046d63a0bf686a37d2/event-scan-d21fdfa2723e.json`.

The post-fix `.350` neighborhood render returned `EVENT_RENDERED_PARTIAL`, selected two nodes, and had zero selected blocking diagnostics; its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7b5a823e3e6691bdac90a2e1ec3ff603172b9ba13667659c333d3ebdd4c5133/5226a20dda834d4d6d7ab491f191fc295717f91c53379bb8e97f43c6df13151f/event-neighborhood-d21fdfa2723e-manifest.json`.

An event comparison against historical revision `10b71c98d51a708a5e4791ff29345586abd212f5a697848f4c9944cb20194de9` was attempted with the current revision as the after state.

The route returned exact blocker `EVENT_REVISION_NOT_CACHED` with message `Requested event graph revision is not cached`, so no baseline/changed event comparison artifact or comparison claim exists.

## Focus, GUI, and map evidence

### Focus tree

Fresh focus inspect and render used revision `e7fbf9dac840d42c12d78945824c4e7db14d36cd8b414bb407990a692c6203ec`.

The layout resolves 184 focuses and 196 connectors, with zero crossings, zero node intersections, two long connectors, and four authored linear detours.

The long connectors are `adopt_military_archetype_program -> preserve_independent_command` at span 13x1 and `define_former_host_policy -> inherit_successor_ledger` at span 9x1.

Validation remains false with fourteen aggregate blocking diagnostics, including installed vanilla continuous-focus sprite gaps, so this is a bounded layout receipt rather than a completion proof.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cfac2989d1486e559bf85eb2e32490214e60b1ab1a8b74ebdc22e19512e8e8e1/eae7b8b2914e2518a9a85d3ef3eaafc3a4cba21f29701b1ddfd2804e1b4fa78a/focus-inspect.e7fbf9dac840d42c.json`.

Current render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02a33b6e26cd319131d46e708aa7260478638f337d0a28a6efe1f823d448af30/c18e895e633d802f4b3f9041ca3ba1823679b3232d689dd690ec8ff83b5c921d/independence_wave_focus_tree.focus.svg`.

### Statehood Ledger GUI

The dedicated Event 006 `independence_wave_status_window` has an existing `chaosx_event_ui_worker` ownership and MCP handoff at `006_iw006_statehood_ledger_gui_worker_2026_08_06.md`.

That handoff records pre/post inspection, states, resolutions, hierarchy, click-region, render, rewrite attempt, and unchanged-source comparison evidence; the rewrite route was blocked by `REWRITE_STRUCTURE_LIMIT` and source remained unchanged.

The fresh current inspect used revision `057fc56363e52f92737efe2d894e76251c05e83cf272f8bb8302783ff0402bd7`, selected 48 elements, and returned `GUI_INSPECTED`, but aggregate validation retained 2,000 blocking diagnostics and 75 visible overlaps with diagnostic truncation.

Current inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/954534e7a8b94d69bd7237aa9e2f090653a43d8644f528541426177177f52633/b469a521dea730c750786d7608704203d0b16e0660d0d4dcd9fe3749ecb0860b/gui-inspect.057fc56363e52f92.json`.

The 14-state render across 1920x1080, 1280x720, and 1024x768 returned `GUI_RENDERED`, but the wire response was truncated by `MCP_RESPONSE_TRUNCATED` because 40,212 bytes exceeded the 32,768-byte limit.

Only the full SVG was returned at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7151f87950fd10f39ae7cf64c5dc04fee0744ed2835a3358531571452bcdae64/e5fce1901a1794d53c872a5e5aa50b0418c3742d6d39c4d66c78939fb7420f55/independence_wave_status_window-full.svg`.

Dynamic animation visibility and focused live interaction therefore remain unproved.

### Grouped formable-state GUI

The shared `chaosx_independence_wave_formable_state_puzzle_window` is not a dedicated GUI introduced and owned by one named event, so the Event-specific UI-worker requirement does not apply to it.

Fresh inspect at revision `57e77f6caf31f9ae8dfa206fb9f6e5beedb84936ba0a958f9b34d77a3da3b018` selected 93 elements and returned `GUI_INSPECTED`, but aggregate validation retained 2,000 blocking diagnostics and 521 visible overlaps with truncation.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21be13ab6870d29fc00700b10914414ca65de1d11e38dc842c097ae239f44646/5f72b31b47986112bf97d8513260af74972da128a998278f0aa8b5db537be42e/gui-inspect.57e77f6caf31f9ae.json`.

The ten-state, two-resolution render returned `GUI_RENDERED`, but the response was truncated at 41,918 bytes and only a full SVG was returned at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9654598f01c40a19da62a51464f8e7698112a52589404fd484b76aaf61e8203f/4e3988a4cdc5e68a2cf92de5b276c4928cfeccac39686470257752c0257f6ad1/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The aggregate scenario co-activates mutually exclusive overlays, so family-isolated layout acceptance remains missing.

### Map

Fresh map inspection covered states 249, 256, 397, 399, 651, and 833 at revision `9ec611428b475849a4d3bbd0bfd49f64460b430e1160a28b9275210512116743`.

Membership, bitmap, and network checks passed, while positions and locators remained false under `MAP_DIAGNOSTICS_TRUNCATED`; 1,999 diagnostics were retained and 2,654 aggregate building-position and port-adjacent-sea errors were omitted.

No selected-state defect was proven by that aggregate result.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a3235e9afb5ff101114887504de0bf7cf6c7491772e136e003778d475912469/fac13effb1ee46da23567bbba19b1d716ecf3d7b79ec42ae33723d16516f673d/map-inspect.9ec611428b475849.json`.

The selected-state coastline, building, supply, and railway render returned `MAP_RENDERED` with validation true.

PNG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/631bc5574ea662cb94f15d0a571dba821ccb18d65d52072fb1628ed9e5df1ca0/57b4d068eab243a52d9b3ead4e7b7c833dfa168a099b9b7ad85cba3b3eb6355e/map-state.png`.

## Task-specific static validation

- `.tools/audit_event6_allocator.py` reported 149 publishers, 126 auto/high-chaos candidates, 138 SCN-ranked candidates, 40 adapters, the exact eight adapter-only rows, 32 attestations, 29 groups, the 20-package standalone witness, and active ladder 3/4/5/7/10.
- `.tools/audit_event6_scenario_matrix.py` passed all 32 matrix cells and eight edge cases.
- `.tools/audit_event6_country_api.py` reported 242 broad references, 191 resolved references, 34 Soviet references, 45 Africa references, zero missing tags, and zero duplicate tags.
- `.tools/audit_event6_flags.py` reported 102/102 tag ladders complete.
- `.tools/audit_event6_gui_matrix.py` confirmed five tabs, the 5/3/4/4 animation-frame families, cleanup coverage, and static/animated sprite pairs; it is not live GUI evidence.
- `.tools/audit_event6_form16.py` passed the exact ARM/GEO/AZR member set, states 230/231/229, consent, mutation, rollback, and readiness contracts.
- Read-only workbook inspection confirmed the Event 006 row is `Partially Available`, SCN-008 is `Unavailable`, and the Liberations cluster is `Partially Available` with members 5 and 6. No workbook or CSV export was changed.

## Accepted-plan disposition

- The IW-045 Bashkiria promotion and latest allocator widening are implemented and reflected by the current 40/32/29/161 authority.
- The focus connector cleanup is implemented to the current 184-focus, 196-connector, zero-crossing, zero-intersection, two-long-connector receipt, but the tree remains partial rather than accepted as globally complete.
- The FORM-12/13 MEL consumer rebind uses state 833; state 256 remains Chuvashia and is not a current MEL binding.
- IW-047 MEL has package-local source and the state-833 formable rebind, but central admission remains deliberately unimplemented and fail-closed behind portrait, neutral-symbol, and acceptance evidence.
- IW-050 Komi has package-local gameplay source, and `109e6e734` closes the missing package-local roster checkpoint with the installed vanilla carrier. Central admission remains deliberately unimplemented and fail-closed behind independent portrait, symbol, probability, and acceptance evidence.
- The KUB/TAT admitted-package AI evidence tranche did not prove a safe AI defect. Mission willingness remains score-only and unresolved under campaign scopes; native `ai_strategy` factors are not exposed by the installed probability adapter.
- Super-event 23 remains blocked on user/rights input for final audio and on its runtime wrappers/firing package. Super-event 24 remains source-wired with partial, not universal, reachability.
- The sixteen achievement rows are static-source complete for definitions, proof triggers, localisation triplets, and 48 DDS states, but live unlock behavior and signature-package reachability remain unproved.

## Asset and documentation gaps

- Every unresolved grounded character carrier still requires its own `chaosx_portrait_creator` handoff with durable attributed source and rights evidence, an explicit placeholder/final state, runtime wiring evidence where authorized, and replacement evidence if a final is pending.
- IW-050 portrait research is now closed fail-closed in `006_iw050_komi_portrait_identity_research_2026_08_14.md`: no attributable period source, identity match, or rights basis was found, and no portrait asset or runtime wiring was promoted.
- IW-050 still lacks accepted neutral and route-symbol provenance. No placeholder or later institutional flag should be treated as approval.
- Super-event 23 audio remains a hard external-rights blocker, not optional polish.
- The Komi core and completion handoffs, Komi package documentation, and any current source-of-truth text depending on their roster-checkpoint claim must record `109e6e734` and the bounded post-fix MCP evidence.
- The source-of-truth map and resume packet retain historical count snapshots below their current override sections. Those dated snapshots must remain visibly historical and must not be read as current authority.
- No custom Event 006 3D unit or building model is accepted in the current specification boundary, so custom unit-audio and bespoke-counter completion rules are not applicable to this audit.

## Probability evidence

The mandatory weighted-logic pass was routed through `chaosx_ai_probability_auditor`.

The attempted whole-event refresh under task `event006_probability_current` did not return a final evidence packet before parent closeout and was interrupted rather than represented as proof.

The latest complete whole-event weighted inventory remains `006_event6_probability_current_2026_08_13.md`.

That inventory is dated to the prior 39-adapter / 31-attestation / 28-group / 162-unattested boundary and must not be relabelled as current quantitative evidence, but its adapter limitations remain directly relevant: the core event-option pool was incomplete, the fourteen allocator region entries did not expose inner runtime package availability, evolution MTTH returned `no_weighted_surfaces`, and later decision, mission, focus, strategy, scenario, and Join calls were transport-blocked.

Fresh current KUB/TAT evidence from `event6_current_ai_evidence_recheck` used MCP revision `7442bcad7bce47b835e38f12e1806232c1d8e65e7aa93103b269dfe8251decdb` at the 40/32/29/161 boundary.

Each mission source exposed eleven candidates, zero available candidates, fifteen required inputs, and `poolComplete=false`.

The six named scenario sets for each package returned 66 rows, 114 unresolved items, eleven fixture-conditioned never-eligible diagnostics, and classification **partial / score-only / unresolved**.

KUB inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd65428ff063ab553aa381490c78a8928c387ae33642b3eb539c6cf2dffd9ccc/ca0da1041639ce5be3eb4b641a35909a36c513ff70979713dfe39f420bc468f6/probability-inspect-de8e919c4eae.json`.

TAT inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ddf13dee3fc4adaad1392a70302728829165af6244aa46b0d5c9a2c8f7c9e854/861a1706e9b68ffe3296cb792e29be9f87142672fd6818759fd3562b52c52522/probability-inspect-fc2e09b238bd.json`.

Both native strategy files returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`; direct evaluations returned `PROBABILITY_SURFACE_EMPTY`, so no strategy-factor ranking or overlap result is proven.

The KUB/TAT sweeps returned exact blocker `PROBABILITY_SWEEP_RANGE_REQUIRED` because every sweep path requires a scenario range, numeric alternatives, or a numeric state value.

Fresh IW-050 Komi probability evidence in `006_iw050_komi_probability_audit_2026_08_14.md` likewise returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces` for `ai_strategy_factor`, followed by exact `PROBABILITY_SURFACE_EMPTY — No weighted blocks matched this request` for scenario `KOM_STRATEGY_EMPTY`.

Komi inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1113eb67f4cbcc233c451213f77f2001c8db81927f0163ad0793c01bb0795c7/3c7f93f637e74b4bccb1edc2c91a1d1deaaa79c2cff19d746376ad85cb1fa972/probability-inspect-78be03b0b074.json`.

The `109e6e734` repair changes a deterministic roster receipt and does not change a weight, probability-bearing modifier, MTTH value, random-selection weight, or AI strategy factor, so it does not authorize a before/after probability claim.

No weighted gameplay source was edited by this audit, and no probability comparison against a real owner-applied patch is claimed.

Final probability disposition is **PARTIAL / SCORE-ONLY / UNRESOLVED**.

No exact normalized option, allocator, mission, focus, strategy, timing, dominance, starvation, rank-reversal, repetition, snowball, or exploit-risk claim is supported.

## Recommended next actions

1. Reconcile the Komi core handoff, current Komi completion handoff, and `docs/events/006_independence_wave/komi_package.md` with commit `109e6e734` and the bounded post-fix inspection/render receipts in this audit.
2. Make no further source patch from this finding.
3. Keep IW-050 absent from central admission, preflight, dispatch, attestation, and Join until its independent portrait, symbol, probability, and package acceptance gates pass.
4. Preserve 40 adapters, 32 attestations, 29 groups, 161 unattested rows, and fail-closed MEL/KOM central admission during documentation reconciliation.

## Audit boundary

This is a source and tooling audit, not live runtime evidence.

The user owns live in-game validation.

Concurrent work was present in the shared worktree, so this handoff records the inspected source state and does not revert, stage, or commit any other agent's changes.
