# Event 014 Cannibalism final weighted-logic audit

Date: 2026-08-25

Mode: read-only audit; no gameplay, AI, event, focus, decision, mission, technology, localisation, GUI, or runtime source was changed.

## Executive result

The current MCP inspection confirms that Event 014 contains several real proportional pools, many score races, and several stateful selectors that the installed analyzer cannot represent.

The exact conditional results carried forward from the completed MCP scenario analyses are the hidden capture cooperation pool at 85/15, each regional Warlord-name pool at 1/4, the six-way Warlord-personality pool at 1/6, Event `.30` at 100/0 for remaining in place versus the AI-ineligible player switch, and Event `.81` at 12/29, 6/29, 5/29, 6/29 for a fascist/unified state and 15/22, 3/22, 1/22, 3/22 for a democratic state.

These are conditional values after the named event, route, target, and option gates have resolved. They are not campaign-wide event frequencies, host-selection probabilities, focus click probabilities, mission frequencies, or terminal-route probabilities.

No P0-P3 balance defect is proven by the available evidence. The principal unresolved risks are analyzer coverage of deterministic host/state/origin selectors, incomplete scripted gates in event options and focus/decision scores, the absent mission adapter, and the absence of a complete lifecycle manifest for spread and terminal state transitions.

## Instructions and references read

The required `AGENTS.md` and these repo skills were read before the audit: `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, `.agents/skills/chaos-redux-event-planning/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-focus-trees/SKILL.md`.

The offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, AI focuses, and national focus modding were consulted.

The vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` was consulted for script concepts, triggers, effects, modifiers, dynamic variables, localisation objects, and MTTH behavior.

## Audited source surfaces and current attestation

The scoped sources are `events/014_cannibalism.txt`, `common/scripted_effects/014_cannibalism_effects.txt`, `common/scripted_triggers/014_cannibalism_triggers.txt`, `common/mtth/014_cannibalism_mtth.txt`, `common/decisions/014_cannibalism_decisions.txt`, `common/decisions/categories/014_cannibalism_categories.txt`, `common/national_focus/014_cannibalism_focus.txt`, `common/ai_strategy/014_cannibalism_warlords.txt`, `common/script_constants/014_cannibalism_constants.txt`, and `common/on_actions/014_cannibalism_on_actions.txt`.

The current Windows SHA-256 file hashes are:

| Source | SHA-256 |
| --- | --- |
| `events/014_cannibalism.txt` | `7efdc94bf09fa50070a1753350cfa2b54cfd624ea132c127e2aaeeade14ea694` |
| `common/scripted_effects/014_cannibalism_effects.txt` | `7fdaac7984c1dbf92df53867fbcf397d14cabf333e942909075d7141f680d5a0` |
| `common/scripted_triggers/014_cannibalism_triggers.txt` | `e1dde14900b46a021d50c16a7ec23862f8bddde67dd2e99f2078c2c2cfbd3231` |
| `common/mtth/014_cannibalism_mtth.txt` | `701323ab8384ae283f33cf4b3b7f8629de2c6d02e097a183152ec057b3b6798d` |
| `common/decisions/014_cannibalism_decisions.txt` | `e44f41ffecfad36556acd61f40c9cc30e86682cc1b1a292a55ead1cf83c7c0b3` |
| `common/decisions/categories/014_cannibalism_categories.txt` | `df60127b1fca9c5d7d30a2d74007cb07aee9db79e91137b6cf11dc8eb7989f25` |
| `common/national_focus/014_cannibalism_focus.txt` | `c32361b7db650ca699f3b54de0cae981200c9b8fd2195c32776ff7d666114b8d` |
| `common/ai_strategy/014_cannibalism_warlords.txt` | `44113b630915d1ea6ff6783ae0627503be4c6a5952371b8f94c9e315c5c9fed3` |
| `common/script_constants/014_cannibalism_constants.txt` | `86eb7a721baf9e139f838843f1472653ee968064bd980ff3e5ef26602d2f8778` |
| `common/on_actions/014_cannibalism_on_actions.txt` | `3c107d32a9aea742e2818cd314a4da40fcbc14122d1bd8ec47b4b32720bc972b` |

The MCP canonical source hashes and revisions are retained separately because the service normalizes source before hashing. The current event option inspect reports source revision `b3ea9cdcca2962342e1ae398bdf50ba130b251190ef714873d1e9b2812ad983d` and source hash `e965dd5d8ff4aee1966343cc6d271ec59c5691569bda80822a2c7c517c7f66e0`.

## MCP evidence

The workspace was `mod_chaos_redux_ea3b2d67c2c0`, targeting Operation Postern `1.19.2.0` revision `d245` where reported by the cached probability artifacts.

Every weighted surface began with `hoi4.probability_inspect` as required.

| Surface and adapter | Current inspect result | Artifact |
| --- | --- | --- |
| `events/014_cannibalism.txt`, `event_option_ai_chance` | `PROBABILITY_SOURCE_INSPECTED`; 40 candidates, `poolComplete=false`, 15 required inputs, 1 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cdc2545a88c2833a491fd52b5dad542bdbc8cf5a80d5ae7095ee8a6100515af2/df819e3a08e300d98ead583af0a2b068cb65d7c5ae912ece4a5ec211f7e683d1/probability-inspect-e965dd5d8ff4.json` |
| `events/014_cannibalism.txt`, `random_list` | `PROBABILITY_SOURCE_INSPECTED`; the `.80.d` pool has 2 candidates, complete source pool, 0 required inputs, 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28ba3084dc9ab3fa4bfd9f9d5716b63a06db42e8761a22ca0da2972e3a3c344c/f1ed4b11245c3e1bb1b82e9584b9a413b1db0ec38ad07b9f36ad0ddf606bb31d/probability-inspect-e965dd5d8ff4.json` |
| `common/scripted_effects/014_cannibalism_effects.txt`, `random_list` | `PROBABILITY_SOURCE_INSPECTED`; 42 candidates across multiple pools, `poolComplete=false`, 5 required inputs, 1 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ea1882cf7f488b6b232e7304d9d698c8843e506ee743ee51ced08ea21f0b649/806c58cc05bde9b7a9c1f988af01cbb3333c4c3f5a65546062f04f2e70b2d41f/probability-inspect-ad0c80af1547.json` |
| deterministic host/state/origin/merge/anchor selectors, `custom_weighted_pool` | `PROBABILITY_SOURCE_INSPECTED`; zero candidates and no usable normalized pool | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c8229978830026e20397a1d89ef72f5e21cc80492c184af52fb159e6530203d/109734634ca6fa48edb52e4082753ce9a0453ab307cff16e53dc3c3112ad4fdc/probability-inspect-ad0c80af1547.json` |
| `common/decisions/014_cannibalism_decisions.txt`, `decision_ai_will_do` | `PROBABILITY_SOURCE_INSPECTED`; 95 candidates, `poolComplete=false`, 32 required inputs, 0 inspect-unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9af8e5a608a5afce65e779d19dc650649ee0966c39242da6563e1123fecb9dca/a877bf5e1820a69d0b9fd1c3b854c9fb99b572e294310cfb2be9d646554d9c93/probability-inspect-eabd8038505f.json` |
| `common/decisions/014_cannibalism_decisions.txt`, `mission_ai_will_do` | `PROBABILITY_SOURCE_DISCOVERED`; requested mission adapter empty, suggested `decision_ai_will_do`, 0 mission candidates, 95 decision candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5707c7cf8ef4b5e8486b437e7b1aeaa78cc130f3c907b35ee046a09fb884feed/f57071c2732b30f0f3f85183600a376d69d5b7b68f098fb57ba8c5518e463853/probability-inspect-eabd8038505f.json` |
| `common/national_focus/014_cannibalism_focus.txt`, `national_focus_ai_will_do` | `PROBABILITY_SOURCE_INSPECTED`; 204 candidates, `poolComplete=false`, 15 required inputs, 0 inspect-unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a75610de172994f3ddddee9ca2892013366164dd454ffee14c9d2576a6a6358/a491f3ed5397561c16e30f351ca4d2ade92afcb64de9d3c32cd79c55181a11e1/probability-inspect-8daaa5f13c9c.json` |
| `common/mtth/014_cannibalism_mtth.txt`, `event_mean_time_to_happen` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason=no_weighted_surfaces`, zero candidates and zero unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63dbd32d5d9089d68a93ff164a678e6805fda64c16f64911edd57ae6eabfde1f/a5e5df455efdaa2730b4bb574c53aedcc8b57eb7c92100ed1390af53ed900e7b/probability-inspect-d7a550b09a98.json` |
| `common/ai_strategy/014_cannibalism_warlords.txt`, `ai_strategy_factor` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason=no_weighted_surfaces`, zero candidates and zero unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22b603e88f68ddd22564d285d12b49dfe528fe7d462bb550eb8d1655fd2013f9/c975ee1b9ee8962d2f5629f9becfdd43c0b3764dd14e3bc35d111c9221dee3ff/probability-inspect-02bd4b54a3b6.json` |

The matching structural event trace returned `EVENT_INSPECTED_PARTIAL`, revision `59143acd4a234aef98ca0b6cfbb7b07211d4aa80f99536718b30e126b1deb6f9`, graph hash `e403ad99017a9482e4ca09f8ce0bde4146fd96bd0576d31f6bd9951d13d55660`, 9,513 events, 14,705 options, 8,301 unresolved nodes, and the informational diagnostic `MCP_INLINE_FILES_TRUNCATED`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a88102024fd850fd73a2afec7f7bc67bc78af8f921f9cdb32eefd11baf22b2dc/5cbc0229144cfce178a18c3aafea5304f2c5fadf3a8ff00fac80b87e34301c3a/event-trace-59143acd4a23.json`.

The matching structural event overview render returned `EVENT_RENDERED_PARTIAL` with manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7815a58a99f1bf92514859bea1550ece49b81802a4879c7edf2cda847d64012a/ea77025c87c8f38d6c1cf925265641cc48a1973b504bf82133c585ebfec458c4/event-overview-59143acd4a23-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/607db9a88afb294578d5e4e37292de287c216138c49556d62d90e529868e76c4/707b62590cc5a6a7e64fb331e27e0005670884c38b7aee565917d2fff3b0b0e6/event-overview-59143acd4a23.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d504bc3252ad5f9d7b097173db6b875eb29141a17be93604824c3984f5a9e25/30cad84617ef807ca5a3326fbe628cce9b597cd80f7436b4c163065bc154bc9d/event-overview-59143acd4a23.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/789f39b7fdb80792c8f95b5ce4179fe97547cb12d3931203af7e7b8005daf128/97d94c895be000d6b1b710a63762cdf49c8052b1ca40eb0dff8870e251454338/event-overview-59143acd4a23.png`.

The focus structural inspectors returned `FOCUS_INSPECTED` with no Event 014 blocking diagnostics for `cannibalism_unified_focus_tree` (108 focuses, 103 connectors, layout hash `29064367ddef9fc917547f65c9cfe4dcf48cda240902f03eb18e51086e8cd364`), `cannibalism_warlord_focus_tree` (68 focuses, 79 connectors, layout hash `f704cbaaf49c7b954a5e3cb44a3b416fcace774f60d249c4ec9557a609438ef1`), and `cannibalism_wendigo_focus_tree` (28 focuses, 28 connectors, layout hash `5685038128dbcfa8f7eadf68f3d359e8d1206578b3b06cae2239ed940aff0e89`). The only diagnostic was the unrelated vanilla `continuous_restrict_freedom_desc` localisation warning.

The structural focus artifacts are unified `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00b2fd0b2a3d1cceb8a27a6c5f899d6e4cf2f0c3f9c0c89b6aa63765d9038110/af6ee803ad82254b66f6269a6b264864a5b067bff8c0ad2080c23cb70bce148d/focus-inspect.88e30923b299428a.json`, Warlord `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce257c6a5061895f10fe469d5edafe46d0d1aba1c0594bc0b2c06a7aa6d4c3ec/de4252e0dbc3c01b651ddbb4721ef874afed8211f1e667dfd972b7cada1c8f7c/focus-inspect.4f4450e8ecd993eb.json`, and Wendigo `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b697bd83e58d386d909c9a33cf7bf400eb25ae1a371ce293de3237d27781aa9/0c9b1903fa15975cca5944a6c7ae0c4ec52a1442230de0e01ee54d59d277e23d/focus-inspect.4f4450e8ecd993eb.json`.

The matching focus renders completed with no Event 014 blocking diagnostics. Rendered HTML/SVG evidence is unified `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d947816318be61abb3d5e8da948f40fbdd2aef1be8736e66ee60b41aecfbcc8/3176fc174d96c23a83e66afac8cbcd08aebc7f656bce0069d1d0f66e50bcafa5/cannibalism_unified_focus_tree.focus.html` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2171b48941e8dcc68b7e9b6b38c925d6eca4c4b3d8f6f4189e1d9c92bfa46884/bac55cb8214e066519758b50b7646d1259941d9d58869c964500c856c4b00fd9/cannibalism_unified_focus_tree.focus.svg`, Warlord `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1db6333ed7a266d4590c6db14a1c486ff194cb5ac940b07dc75577c5598ddc60/26c352ec02580a23b4e05c094ebae6dc87fd04aa0a71c37d73a1f1ca8bd0f51d/cannibalism_warlord_focus_tree.focus.html` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5791167975f262b44ac05dacf7889e5132b14aa0f2ea9fadd1cd9da71db377fe/c566f93bea90e3e1b2dd54cd952711fdccb5019b70579270a2ffa9c11b48a15b/cannibalism_warlord_focus_tree.focus.svg`, and Wendigo `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dddf8ba3818d70fde76db33100341fb4aba5770f66a57b05b0f31339e510a01c/4209fa0965a12573980f520d4089cd53c76e44a04a2bab722e6562e5c90b36ac/cannibalism_wendigo_focus_tree.focus.html` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/232389eb0676368c65dd7d366ccaac11558a757021802f9dd4c4c0119274643d/714f903f0517f91a1deaae1438e42edec4709ec66a070f7135e79166dd455c1d/cannibalism_wendigo_focus_tree.focus.svg`.

## Required scenario matrix

The scenario IDs below are the final audit names. They map to the package's prior scenario contracts and are deliberately explicit about hidden state rather than assuming a campaign frequency.

| Scenario ID | Declared state | Candidate pool and external-factor completeness | Result classification |
| --- | --- | --- | --- |
| `E014_WEAK_ISOLATED_WAR_LOSER` | Wartime country with long war, casualties, low manpower/stability, damaged supply, isolation, convoy pressure, and occupation. | Host and state selectors use complete source loops but the analyzer cannot expose the loop-built candidates or typed scripted predicates. Event `.20/.21` route factors remain unresolved. | Host/state score-only; event option bounded/partial; no probability claim. |
| `E014_WELL_SUPPLIED_STABLE_WAR_PARTICIPANT` | Stable, well-supplied wartime participant with intact manpower and no severe isolation. | Same deterministic selector limitation; stable/high-integrity and clean-route gates are not fully typed in event options. | Score-only/bounded; no normalized route probability. |
| `E014_PLAYER_CONTROLLED_HOST` | Human host or human-selected Warlord at Event `.30`. | `.30` two-option pool complete in the retained scenario evaluation; `.30.b` human-only trigger supplied. Host scorer itself is deterministic. | Exact for `.30`; host selection score-only. |
| `E014_AI_ISLAND_WARLORD` | AI Warlord with island origin, convoy route, and island focus branch. | Origin selector is a strict score race; focus pool is structurally 68 candidates but route/origin inputs remain incomplete. | Score-only/partial. |
| `E014_AI_SIEGE_WARLORD` | AI Warlord with siege-commune origin, relief pressure, and siege focus branch. | Same incomplete origin and focus helper inputs. | Score-only/partial. |
| `E014_AI_MARCH_WARLORD` | AI Warlord with march origin, moving-front and rail pressure. | Same incomplete origin and focus helper inputs. | Score-only/partial. |
| `E014_HIGH_ALIGNMENT` | Warlord/unifier with high network alignment and prepared submission route. | `.71` event-target and submission eligibility predicates are not typed; decision target pool is incomplete. | Bounded/partial; no submission probability. |
| `E014_LOW_ALIGNMENT` | Defiant Warlord with low alignment, strong divisions, and resistance route. | `.71` resistance/challenge gates and division/route inputs are incomplete. | Bounded/partial; no resistance probability. |
| `E014_REVEALED_UNIFIED_CBL` | Revealed unified CBL with valid captured Hannibal target and no terminal lock. | `.81` four-option pool complete in the retained scenario evaluation; route reach and event-target validity are external. | Exact conditional `.81`; route-wide result unresolved. |
| `E014_WENDIGO_ZZZ_PRELOCK` | Revealed ZZZ Wendigo before transformation lock with valid inherited/cold-front targets. | `.81` pool is complete after the event target is valid; Wendigo focus and target scores retain unresolved route/helper inputs. | Exact conditional `.81`; target/focus timing score-only/partial. |
| `E014_WENDIGO_ZZZ_LOCKED` | ZZZ after transformation lock with terminal hunt state. | Terminal target, lock, world-end, and target validity are external; no complete mission pool exists. | Score-only/unresolved; no terminal frequency or timing. |
| `E014_CHAOS_LE_1000` | Unified route with Chaos at or below 1000. | Focus pool supplied, but terminal and route gates are not fully bound by the adapter. `.81` event gate is external. | Focus score-only/partial; no terminal probability. |
| `E014_CHAOS_GT_1000` | Unified or Wendigo route with Chaos above 1000 and terminal prerequisites otherwise declared. | Focus/decision candidates include unresolved terminal flags and target predicates. | Score-only/partial; no terminal probability. |
| `E014_WORLD_OPPOSITION_WEAK` | Low world opposition and open route to expansion or convergence. | Host, target, decision, and focus candidates are not complete under typed external factors. | Unresolved campaign timing/frequency. |
| `E014_WORLD_OPPOSITION_STRONG` | Strong world opposition, major war, and active counterwar pressure. | Same incomplete target/counterwar pool and dynamic state gates. | Unresolved campaign timing/frequency. |

## Exact proportional pools

### Hidden capture cooperation

`events/014_cannibalism.txt:680-681` declares `CANNIBALISM_CAPTURE_COOPERATION_WEIGHT = 85` and `CANNIBALISM_CAPTURE_ESCAPE_WEIGHT = 15`; the nested `random_list` is at `:768-778` under `chaosx.nr14.80.d`.

The completed evaluation `probability-66c8d75f2f1936727a2f0895` used scenario hash `631fa3859f4a9725b74e84d3c322205a11093cc5858560365209c9a6caebe3ae` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1794b3a229866f6541ba76e20a785f37a8f09c55a619c9127ab8eb283bba925/51f094aa6a3d33c6c233f2b2b460ffaa5d54d0456227d3b946d7fb648b1878b3/probability-66c8d75f2f1936727a2f0895.json`.

Conditional on `.80.d` being eligible and selected, cooperation is exactly `85/100 = 0.85` and escape is exactly `15/100 = 0.15`.

The pool has no internal dominance or starvation defect. Its 15% escape branch is intentionally nonzero.

### Warlord regional names

The seven regional helper pools at `common/scripted_effects/014_cannibalism_effects.txt:4648-4705` each contain four entries of weight one for Europe, Asia, Africa, Middle East, North America, South America, and Oceania.

The completed region evaluations were `probability-fc81d6deb5429c53d3176f3f`, `probability-2e8b6fff8f0cefad5f56a0dd`, `probability-d6ad6aa7b83d990bbfa0d78d`, `probability-6138be13c12bfce4ec4ec175`, `probability-1f26cb5b29386dbbedc8401b`, `probability-3eeabf88d532ac51ed7b45c1`, and `probability-a7bd9ad03ac6f4415447c128`.

Each entry is exactly `1/4` conditional on its region helper being selected. The region branch itself is deterministic precedence, not a seven-way random pool.

### Warlord personality

The pool at `common/scripted_effects/014_cannibalism_effects.txt:4711-4717` contains six equal entries: `hoarder`, `feast_captain`, `charismatic_initiator`, `suspicious_tyrant`, `network_disciple`, and `defiant_mouth`.

The completed evaluation `probability-139bd3d79b8c3148b17916c2` used scenario hash `b460ea46f698da1fed0023358123dab9e652c691b2576004ebf79823141f619b` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b5e534e1a274029ae69e4d35cd643d610a04d32bf4a4da084c520650d02a52f/b8aabec558afe333dbbd970fe22978a7072bc1d54b96fc28f96d401278c67de6/probability-139bd3d79b8c3148b17916c2.json`.

Each personality is exactly `1/6`; the rendered ranking artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78d81fc0306e7af0b709bdf38c1595dbbc72f18306273d58597b90183c2d28dd/10b96ace229678fd979e25e939ed7010d51024f3f7bb737c2b47e22b1e5c03a9/probability-139bd3d79b8c3148b17916c2-ranking.svg`.

### Player-host safety `.30`

`chaosx.nr14.30.a` has base 100 and `.30.b` has base 0; `.30.b` is additionally gated by `is_ai = no` at `events/014_cannibalism.txt:225-237`.

The completed evaluation `probability-2df314e43b00d261998c992a` used the player-safety scenario and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3497244d5e893f90c1751bf0df87d8f2ba713b2414bf8c9027aeec344f958c7/72a5b4ae8afdb7fbb07b0da936c80f3badf4b2fa71afbdcbe581a7ee6a49762f/probability-2df314e43b00d261998c992a.json`.

The AI result is exactly `.30.a = 100`, `.30.b = 0`, and the human-triggered option remains available to a player. This is intentional route protection, not an AI balance defect.

### Captured Hannibal `.81`

`chaosx.nr14.81` has a complete four-option pool after the reveal, target, no-world-end, and no-terminal-lock gates resolve.

For fascist/unified state, the retained evaluation `probability-0c4c89f992a9709b4b69d2ab` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69b323d0b99652a5b45bf695645d4d4ff8b375d17a8815e136c9b87e1ddb6043/b31c2750b141a1d0223803439629876c77d48d5b3940746a73549a74fc08ae01/probability-0c4c89f992a9709b4b69d2ab.json` prove weights `[60,30,25,30]` and normalized values `[12/29,6/29,5/29,6/29]` for `.81.a` through `.81.d`.

For democratic state, the retained evaluation `probability-e018952d4ea96793487da5eb` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1afc1ba0396122ff1f2bf84bc58db9ee157dcdd23f60035577aa63e8a6143774/78a295708cf13c935c244f84a2d65de8055709b70c30d2429515399868a8ea9d/probability-e018952d4ea96793487da5eb.json` prove weights `[150,30,10,30]` and normalized values `[15/22,3/22,1/22,3/22]`.

The combined four-scenario analysis `probability-621c764abee3b7442440c14a` used Wendigo, democratic, Chaos below 1000, and Chaos at or above 1000 with zero unresolved option rows and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ffd49f6d9537e808284579adbb0b2dc81a64a39bbb785bb5fca32b158d3fd27/7c2ee2a08212b8ce43824c63943c7c0ff96ed8ed8e7976292bcc10a8fafe330b/probability-621c764abee3b7442440c14a.json`.

The democratic `.81.a` rank shift is large but bounded and source-intended through `ai_urgent_factor = 2.50`; it is not an unbounded dominance claim because it is conditional on the complete `.81` pool.

## Score races and deterministic selectors

### Entry host and state selection

`cannibalism_score_current_host` at `common/scripted_effects/014_cannibalism_effects.txt:1112-1323` starts at base 2, adds player, war-duration, stability, war-support, casualty, manpower, isolation, supply, remote-army, convoy, hunger, occupation, army-size, and Chaos-tier terms, then clamps the score to 1 through 32.

The declared weights are centralized in `common/script_constants/014_cannibalism_constants.txt:491-529`, including war duration 1/3/5, casualties 2/4/6, isolation 3, damaged supply 3, remote army 4, convoy loss 2, occupation 2, and Chaos 1 through 5.

`cannibalism_select_first_host` at `common/scripted_effects/014_cannibalism_effects.txt:1328-1364` loops over every eligible country, calls `find_highest_in_array`, and then preserves the first array candidate at the winning index. This is a deterministic highest-score race with source-array tie behavior, not weight divided by a pool sum.

`cannibalism_score_current_state` at `:1367-1450` and `cannibalism_select_highest_risk_state` use the same deterministic score pattern for controlled states, including army presence, island/remote position, infrastructure, damaged port, port, supply node, occupation, prison/camp, hunger, population density, and capital penalty.

The MCP custom-pool adapter returns zero candidates because `every_country`, `for_each_scope_loop`, `find_highest_in_array`, event-target persistence, and scripted helper side effects are unsupported. No exact selection probability, seeded frequency, dominance, starvation, or rank-reversal result is valid for these selectors.

### Warlord origin and regional dispatch

`cannibalism_select_warlord_candidate_state` at `common/scripted_effects/014_cannibalism_effects.txt:4520` is a deterministic maximum over valid global state candidates using node strength, population, and origin bonuses.

The origin branch has deterministic precedence island, then siege, then march, and the region branch has deterministic precedence Middle East, Europe, Asia, Africa, North America, South America, then Oceania. The regional name pool after that branch is the exact 1/4 pool described above.

### Unification and Wendigo hosts

`cannibalism_select_unification_host` at `common/scripted_effects/014_cannibalism_effects.txt:12011` prefers human candidates, then scores controlled states, divisions, population, larder, alignment, network centrality, ports, capital supply, rail, leverage, manipulation, and isolation before a stable country-id tie break.

`cannibalism_select_wendigo_merge_host` at `:18446` prefers human candidates, scores divisions, controlled states, and population, clamps the score, and uses a stable lowest-id tie break.

Wendigo anchor selection scores capital, population, coast, naval base, supply node, and rail using `cannibalism_wendigo_anchor` constants, with initial target 3, maximum live anchors 6, and 500K minimum creation population.

These are score-only deterministic selectors. The owner must not randomize them solely to satisfy an incomplete analyzer.

### Focus AI

The three focus trees are `cannibalism_unified_focus_tree` with 108 focuses, `cannibalism_warlord_focus_tree` with 68, and `cannibalism_wendigo_focus_tree` with 28.

The completed focus evaluations used 540 unified rows across five named scenarios, 204 Warlord rows across island/siege/march scenarios, and 84 Wendigo rows across unified/Wendigo/high-Chaos scenarios. They were `PROBABILITY_ANALYZED_PARTIAL` because 209 unified rows, 141 Warlord rows, and 79 Wendigo rows retained unresolved route, origin, terminal, or helper inputs.

The focus sweep `probability-99042c8a8d406dc94d858c46` varied `cannibalism_larder`, `cannibalism_world_hostility`, and `cannibalism_frenzy`, requesting pairwise ranking, sensitivity, threshold, and rank-reversal views. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cabd2111fcedd2ee558ec8be398f8d577fd92a8d3d8b76d191b3e7438d7d5cad/36a8baaffb61a3bdeb3cc9a85220b21eea5a412a7ac64b80514aa2e981c82e8a/probability-99042c8a8d406dc94d858c46.json`.

The sweep produced useful score, sensitivity, threshold, and unresolved views, but unresolved rows prevent complete rank-reversal certification. Focus `ai_will_do` values are willingness scores in an independent highest-score race, not focus click probabilities.

### Decision and mission AI

The current decision source contains 95 `ai_will_do` blocks spanning containment, international response, Warlord command, unified Larder/War Machine/global campaign, terminal mobilization, and Wendigo command/counterwar families.

The decision adapter sees 95 candidates and 32 required inputs but no complete available pool, so no decision score ranking, activation frequency, dominance, starvation, or timing conclusion is certified.

The mission adapter is not implemented in the installed MCP route. It returns zero mission candidates and suggests the decision adapter. Mission rows may be structurally mapped to decisions by the package matrix, but that mapping is not engine probability evidence.

Recent commit `cb6a6667f` changed Event 014 decision visibility/availability and raised two decision timing floors from 21/14 to 90 days; its Event 014 diff contains no `ai_chance`, `ai_will_do`, target-score, MTTH, or random-weight edits. Recent commit `b8304e0f6` adds phase and mission-slot scripted triggers and contains no direct weighted values. These changes affect validity and cadence context, not a weighted before/after pair, so no compare is claimed.

### MTTH and Evolution III

`common/mtth/014_cannibalism_mtth.txt` currently retains Evolution I, Evolution II, `cannibalism_unified_target_decision_weight`, and `cannibalism_wendigo_target_decision_weight` declarations.

Evolution I and II use base 90 days with source clamp 21 through 240 days and factors for exploitation, hunger, cells, spread, clean response, integrity, containment due date, and Chaos.

Evolution III is scheduled by `cannibalism_try_schedule_evolution_iii` and deterministic readiness/cooldown logic in `common/scripted_effects/014_cannibalism_effects.txt:3093`; it has no MTTH entry.

Commit `c25b49b64` removed the unused Evolution III MTTH declaration without changing readiness thresholds, event routes, AI scores, decision weights, focus weights, or localisation. The current MTTH inspect reports `no_weighted_surfaces`, so no exact MTTH timing, cumulative chance, or timing distribution is claimed.

The two target-decision MTTH entries add population, supply, cell, prison, port, stability, rail/naval, coalition, enemy, adjacency, cold-front, post-lock population/capital, and overextension factors, but their targeted `FROM` scope and scripted gates are not bound by the adapter. They are score-only/unresolved, not certified normalized target probabilities.

### AI strategies

`common/ai_strategy/014_cannibalism_warlords.txt` defines common, island, siege, and march intensity profiles for army, equipment, templates, convoy/screen ratios, naval bases, artillery, bunkers, arms factories, motorized production, infrastructure, and spare units.

The current `ai_strategy_factor` inspect finds no weighted surfaces. These values are strategy intensities and deterministic enable flags, not a candidate selection probability. No strategy dominance, starvation, or rank-reversal claim is certified.

## Warlord submission, reveal, unification, Wendigo, and terminal routes

Event `.71` has five options for retain command, surrender, autonomy, resistance, and challenge with base values 40, 15, 25, 20, and 5 in `cannibalism_unification_ai`.

The completed `.71` evaluations left 17 scripted gate/factor rows unresolved, including player displacement safety, alignment, route preparation, division strength, resistance, and challenge eligibility. No Warlord-origin-specific submission, resistance, autonomy, or challenge probability is certified.

Event `.80` has a six-option captured-Warlord root pool, but the captured-Warlord event target and no-fallback condition prevent a complete root normalization. Its nested `.80.d` cooperation/escape pool is exact only after `.80.d` itself is reached.

Event `.81` is exact only after reveal completion, valid captured-Hannibal target, no world-end, no terminal host, and no Wendigo transformation lock. Those route gates remain external to the exact four-option calculation.

The ordinary terminal route requires unified host state, terminal route flag, operational packages, Chaos above 1000, Network Reach at least 92, more than 35 controlled states, at least 25,000K consumed population, and Larder at least 750.

The Wendigo terminal route requires transformed ZZZ, locked transformation, no existing world-end, and Chaos above 1000.

The source contains no complete normalized probability pool for reveal, unification host, Wendigo merge host, anchor creation, terminal target, or world-end reach. These are deterministic or stateful route selectors and remain unresolved for campaign frequency and timing.

## Spread, reinfection, cadence, and custom pools

Spread and reinfection are wired through `common/on_actions/014_cannibalism_on_actions.txt`, queue helpers in `common/scripted_effects/014_cannibalism_effects.txt`, and Events `.60`, `.61`, and `.62`.

The source declares route-specific delays and a generation-aware queue, but the analyzer does not execute Clausewitz loops, scripted effects, event-target persistence, target invalidation, recovery, or route replacement. The cached `.60` analysis `probability-53f3063dd71386156cf469fc` retained 20 unresolved rows, and the cached `.61` analysis `probability-925ebf20da754347e06b7d7c` retained 3 unresolved rows.

The prior synthetic sequence parser probe used one candidate, a one-day horizon, 100 samples, and seed 14014; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86df5076a6cb23b9ae20e9c945fcd230f1d0492c51bd69e3d14060b86f151f2a/3bcf87893dde2bad849c7eebcd9717bfeb0dc693443014eee7d9e215b3a0ce36/probability-959793529f480f0842ef5cd5.json`. It is a parser probe, not source cadence evidence.

No seeded simulation or source-linked sequence result is claimed. A complete manifest must declare cadence, cooldown, recovery, caps, removals, invalidation, generation resets, timer changes, and terminal transitions before those tools can prove repetition or snowball behavior.

## Risk findings

| Risk type | Finding | Classification |
| --- | --- | --- |
| Dominance | `.30.a` dominates the AI pool by design because `.30.b` is human-only and weight zero. Democratic `.81.a` rises to 15/22 conditionally because the urgent factor is 2.50. | Exact conditional; not a defect. |
| Starvation | `.80.d` escape remains 15%; all flat name/personality pools are equal. `.30.b` AI starvation is intentional player protection. | Exact conditional; not a defect. |
| Rank reversal | Focus sweep requested rank reversals but unresolved route rows prevent complete certification. Deterministic selectors cannot be swept by the current adapter. | Partial/unresolved. |
| Repetition | Flat random pools have no internal repetition bias beyond declared weights. Queue recurrence, cooldown, recovery, and target replacement are not executable by the adapter. | Exact for flat pools; unresolved for lifecycle. |
| Snowball | Host, merge, target, and terminal scores can accumulate state advantages in source design, but no MCP probability or sequence evidence proves an unsafe snowball. | Design hypothesis only. |
| Invalid/dead candidates | Focus and event analyses expose `NEVER_ELIGIBLE` or unresolved rows for route, target, terminal, origin, and event-target gates, but the adapter cannot prove whether each is excluded at runtime. | Unresolved; do not patch from this alone. |

## Recommended owner changes, without applying them

No balance weight patch is recommended from this audit.

If quantitative closure is required, the owner should expose a read-only typed analyzer manifest for `cannibalism_select_first_host`, `cannibalism_select_highest_risk_state`, `cannibalism_select_warlord_candidate_state`, `cannibalism_select_unification_host`, `cannibalism_select_wendigo_merge_host`, and Wendigo anchor selection containing the complete candidate set, computed score, eligibility reason, and deterministic tie break.

The owner should type the scripted route predicates and event-target/generation gates used by Events `.20`, `.21`, `.60`, `.61`, `.71`, `.80`, `.81`, the focus trees, and the two targeted-decision MTTH entries.

The owner should provide a mission-specific adapter or an explicit decision-compatible mission candidate map with availability, target validity, cost, cooldown, cap, and route-state inputs.

The owner should provide typed focus route/origin/terminal inputs before using the existing focus sweep as rank-reversal evidence.

The owner should publish a complete spread/reinfection/convergence sequence manifest before requesting simulation or sequence analysis.

After any owner-applied weighted, prerequisite, gate, candidate-pool, cadence, or tuning change, rerun `hoi4.probability_inspect` and the same named scenario evaluations, then run `hoi4.probability_compare` with identical candidate pools, external factors, source revision pair, and diagnostic thresholds. Keep score traces separate from normalized probabilities.

## Skipped analyses and exact blockers

`hoi4.probability_compare` was not run because this read-only pass has no owner-applied before/after source patch.

`hoi4.probability_simulate` was not run because no uncertain input distributions, correlations, or approved seeds were declared.

`hoi4.probability_sequence` was not run against source because the custom-pool lifecycle manifest is incomplete; the retained one-candidate parser probe is not campaign evidence.

No exact MTTH timing was run because the current MTTH adapter reports `no_weighted_surfaces`, and the target-decision entries are not bound to typed target scopes.

No exact decision or mission score ranking was run because the decision pool is incomplete and the mission adapter has zero candidates with `requested_adapter_empty`.

No exact AI-strategy probability was run because the strategy adapter reports `no_weighted_surfaces` with zero candidates.

No exact host, state, origin, convergence, Wendigo merge, or anchor probability was run because `custom_weighted_pool` reports zero candidates for deterministic array selectors.

The first parallel batch of current inspect requests returned `INTERNAL_ERROR` for several large sources. Individual retries succeeded for event options, random lists, decisions, focus, MTTH, AI strategy, and custom-pool discovery; the failed parallel responses are recorded as MCP operational noise, not as content conclusions.

The structural Event Chain Viewer remains partial because the MCP workspace inventory is capped at 64 inline paths and reports 8,301 unresolved nodes and 14 blocking diagnostics in the global game graph. The selected Event 014 trace/render artifacts are preserved, but they do not prove complete Event 014 reachability.

## Handoff conclusion

The exact conditional `.30`, `.81`, capture cooperation, regional-name, and Warlord-personality results may be carried forward with their scenario hashes and source-gate conditions.

The current source contains no proven weighted dominance, starvation, rank reversal, repetition, or snowball defect beyond the intentional `.30` player-safety zero and the bounded democratic `.81.a` shift.

Focus, decision, mission, MTTH target, AI strategy, deterministic host/state/origin/merge/anchor, spread, reinfection, reveal, unification, Wendigo, and terminal campaign frequencies remain score-only, bounded, partial, or unresolved as stated above.

No gameplay patch was applied. This document is the only intended change from this subtask.
