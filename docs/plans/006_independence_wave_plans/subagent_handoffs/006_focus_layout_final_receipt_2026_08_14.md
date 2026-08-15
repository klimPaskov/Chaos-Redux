# Event 006 focus layout final receipt

Date: 2026-08-14

## Superseding current MCP receipt (post-IW-045 documentation pass)

Fresh `hoi4.focus_inspect` against `common/national_focus/006_independence_wave_focus.txt` and tree `independence_wave_focus_tree` returned `FOCUS_INSPECTED` at source revision `7386b22f2b59cec07d42697d0e8e8a6ca0b16c5991dd81de403d72f17e05e540`. The current graph remains 184 focuses and 196 connectors with zero crossings, zero node intersections, two long connectors, and layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`.

Current inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4676e6a5bcafd35b54e3e5f244abda96f13488669367efc9b410ebb8b42bc114/2cfabfbfba2630aaab97afa32540f166d6076286430258962e8fa7afcae82996/focus-inspect.7386b22f2b59cec0.json`.

Current render artifacts: HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d77d09877e1b590360efa25ab41318842ab937b401e728e6f8b9999a2389bef/4b449646441f3bcf76543cde5dfb4e01891d57eb02c5448369a74df2745eb3aa/independence_wave_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02a33b6e26cd319131d46e708aa7260478638f337d0a28a6efe1f823d448af30/386993a4cbb1ce0b3a157511c221f74ab889327a3dfde4b5dc3040ebb2f62cb8/independence_wave_focus_tree.focus.svg`, and JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/edd19123e7474d4790c8d83a4102a367a9b8620c5929a74f01290857c6f23b52/83c12ffe2b96a6d538e3012155a969e2228d70708021534f9a7a19d517fef127/independence_wave_focus_tree.focus.json`.

The current MCP validation remains bounded: the shared tree still reports fourteen blocking diagnostics overall, consisting of unrelated vanilla continuous-focus icon references plus authored Event 006 linear-detour and long-connector warnings. No Event 006 crossing or node-intersection defect is present, and no gameplay, localisation, asset, central-attestation, Join, workbook, or package source changed in this inspection/render pass.

The current shared focus source was inspected and rendered after the temporary coordinate experiment was reverted.

The final source remains at 184 focuses and 196 connectors with zero crossings, zero node intersections, two long connectors, and layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`.

Final inspect receipt: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2feeb42b4913dda42d417668faad1f916bf1ac2a471a01b36fbf888ac23ba49/664c29befaf7c039f413fb95a068e3f5bd4af1e1e365192ba6756ab444cbf038/focus-inspect.f24f8ae82169d42c.json` at source revision `f24f8ae82169d42cc91210b074d0179463256ac175dab3ba27569169db3981f3`.

Final render receipts: HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d77d09877e1b590360efa25ab41318842ab937b401e728e6f8b9999a2389bef/d941bb1329b10bb2943e4ace5434a230921f075c3961ad39282e04d8a4c5a0fc/independence_wave_focus_tree.focus.html` and SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02a33b6e26cd319131d46e708aa7260478638f337d0a28a6efe1f823d448af30/3d444151c2e5e4605726f390558f4e0a031553473a21b9faad71b53bf1c3d1e4/independence_wave_focus_tree.focus.svg`.

The six authored layout warnings remain bounded and unchanged in kind: three linear detours, two intentional long connectors, and one regional-formable detour. Twelve unrelated continuous-focus icon diagnostics remain in the installed vanilla inventory. No coordinate change is retained because the trial moves only transferred the same warnings to adjacent connectors and did not improve crossings or node intersections.

No gameplay, localisation, asset, central-attestation, Join, workbook, or package files were changed by the layout trial.
