# Event 028 sourced text consumer evidence

Disposition: accepted source wording implemented; shared-window visual acceptance is open and must not be inferred from the text research or render-success code.
Acceptance basis: the user's full super-event contract and parent acceptance of the verified Bacon excerpt and FitzGerald remark.
The [text research](../../super_events/028_asteroid_incoming_text_research.md) supplies eight main-quote and six remark candidates, exact selected wording, edition attribution and primary links.

The selected quote is the exact excerpt `Nature to be commanded must be obeyed`, followed by a newline and `Francis Bacon`, without added ending punctuation.
The selected remark is `The Moving Finger writes`, attributed in research to FitzGerald's 1859 first-edition English rendering, not directly to historical Khayyám.
The authored title, description, news acknowledgement, image, audio selection and source wiring remain unchanged in this text-only tranche.

## Existing consumer and source rules

There is no new or dedicated Event 028 window.
The existing parent-owned `chaosx_super_events` window in `interface/chaosx_super_events.gui` uses `player_context` through `common/scripted_guis/chaosx_scripted_gui_super_events.txt`.
Its actual quote textbox is at GUI lines 185–195, with `hoi_18mbs`, width 370, height 79 and centered fixed-size text; the close remark uses the existing button at lines 197–206.
`common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:950` and 1219 select the exact `.116.q` and `.116.a` keys when the existing global slot flag has value 116.

Physical GUI SHA-256: `c3c681d008c96832a1b5b543f8d84dd19d04b8bb737ff55edb40555d82e7e8cc`.
Physical scripted-GUI SHA-256: `1b0bf25e6226d906e35caa9010e8a24547b38ffb9b57a9dbccbf38235f29bc2b`.
Neither source is edited by this tranche.

Fresh GUI reference context at limit twelve returned no missing/omitted sources; headings were not treated as detailed rules.
Fresh revision-bound reads covered installed `common/scripted_guis/_documentation.md:8–87`, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, and offline `Interface modding:196–226`, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`.
Offline scripted-GUI properties at lines 391–440 were also read for dynamic image binding, and the installed `interface/eventwindow.gui:473–528` supplies a native picture/text consumer precedent.
The installed launcher points to package `hoi4-agent-tools` version 3.6.0; this installed identity is not a connected-server version handshake.
No exposed health/version probe or client task negotiation was established, so no helper-expansion, job or native-task claim is made.

## Actual connected inspection and declared preview

The corrected explicit fixture is `AST028_SUPER_TEXT_116_1080P_RESOLVED`, 1920×1080, UI scale 1, normal/hover states, generated scenarios disabled.
It declares window-visible and no-Fallout flags, the exact source quote/remark/title strings, and the registered slot-116 sprite through `scenario.values` keyed by the unbracketed getter names.
Those are declared preview inputs, not observed campaign state or proof of runtime helper selection.
The impact description remains unresolved because no incident target/world fixture was invented for this text review.

An initial fixture put UI scale inside `resolution` and was schema-rejected, then corrected to the supported top-level `uiScale` field.
Another initial fixture used bracketed getter keys, leaving the text unresolved; the scalar keys were corrected after reading the installed resolver and the live inspection reduced unresolved values from five to one.
The corrected inspection returned `GUI_INSPECTED`, eight elements, 88 modelled/one unresolved fidelity entries, source revision `7e3eb6cd4abc24bc805b21d6739f81cee4aadb1c6d23f3e33fe3ee32dad5f1f8`, validation false.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d848d9408e9c1587c32e3f6b9241a5e52cff1c6449ad21385cd2a551a9052384/05c91cc73aaa87d16d742063ab8f70de447f1bd9ae8b2105ca7033dd0a61c02f/gui-inspect.7e3eb6cd4abc24bc.json`.

The matching corrected render returned `GUI_RENDERED`, source revision `1c134bea50d9721f743c216250be79291a2fe0c4d347156191074150dbb64831`, one resolution, two states, five views, and the same 88/one fidelity split.
Its `comparisonScenario` substitutes the exact previous quote/remark strings under the same declared visibility, title, image, resolution and scale.
This is a declared-value comparison, not an older `.gui` source snapshot or observed old/new campaign.
The returned difference is 6,672 pixels, ratio `0.0032175925925925926`; a nonzero difference is not a visual pass.

| Returned view | Artifact URI |
| --- | --- |
| Full current PNG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00155e066f161d80fa33c15f68873cb7e4589aae61adc5ca4a50fe642e9565dd/981113c6f26a55463a77ab82e605fcc7435b14c6709f5efa27c6b48a3290dece/chaosx_super_events-full.png` |
| Cropped current PNG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6d8bebf275b81bbd3755821f2d3ff22ac5ce0b4a0e33c44f23997c4f44ff3af/b45cb46c19786884fca2f357e28f170aa6e7f8ed0e4dd596ad9ea07e8aec32d1/chaosx_super_events-cropped.png` |
| Fidelity JSON | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67a015f2cb91e7e6e7f17dd3825e09ebe3e41d216c4d2d6894ab0d95baa6fc13/0be505df29bb5568ec29e8ba66d669e79ce6e5e02c9ebb3a47936f1eb895eef2/chaosx_super_events-fidelity.json` |
| Declared-text comparison PNG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de6acb26c2bab3853263bd76e93cfbb872e10cc975a1e33052d39c32e92733d6/82ccf8ddc4410847f1b11d07b08558352cea9298e08d45099e2d13355f233484/chaosx_super_events-comparison.png` |

## Open visual gate and exact delivery limits

Current inspection/render diagnostics include missing `Quote of the Day` localisation, background clipping from 899×592 to 899×585, a child outside the clipped parent, quote-header/quote rectangle overlap, other background overlaps and missing close-button trigger evidence.
They are not waived, dismissed as renderer discrepancies or represented as resolved.
The remaining description and full incident/controller/long-name/state matrix are unmodelled.
The source text change does not authorize a speculative shared-layout repair without the required reference and production-image review.

After the fresh render, the connected resource list still returned `resources: []`; the artifact template is advertised but no returned image URI was enumerated for the exposed resource reader.
Independent event/map/probability resource reads and the parent's actual artifact-backed event comparison also reproduce `Artifact provenance manifest is unavailable`.
No full current render image, full fidelity body or retrieved-byte hash was available for visual inspection in this session, and no alternative access-control bypass was attempted.
The scripted-GUI skill therefore keeps the visual gate open.
No complete GUI, final in-game playback, target snapshot, clean error log or full Event 028 acceptance is claimed.
