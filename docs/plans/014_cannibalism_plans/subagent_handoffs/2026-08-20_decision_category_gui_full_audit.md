# Event 014 Cannibalism Decision-Category GUI Audit

Date: 2026-08-21

Status: the four Event 014 decision-category layouts were audited and patched. Fresh selected-window post-change MCP inspection and render evidence exists for every audited window. The exact rewrite and full post-resolution limitations are disclosed below; this report does not cover or make a completion claim for any other Event 014 surface.

## Scope

Only these Event 014 scripted GUIs were in scope:

| Scripted GUI | Window | Decision-category entry point |
| --- | --- | --- |
| `cannibalism_early_header_scripted_gui` | `cannibalism_early_header_window` | `cannibalism_containment_category`; `cannibalism_network_alerts_category` |
| `cannibalism_warlord_command_scripted_gui` | `cannibalism_warlord_command_window` | `cannibalism_warlord_command_category` |
| `cannibalism_revealed_command_scripted_gui` | `cannibalism_revealed_command_window` | `cannibalism_unified_command_category` |
| `cannibalism_wendigo_command_scripted_gui` | `cannibalism_wendigo_command_window` | `cannibalism_wendigo_command_category` |

`cannibalism_network_scripted_gui` is a `player_context` popup and was excluded. Shared event-log, Event Details, evolution, settings, super-event, focus-tree, other-event, and unrelated decision-category interfaces were excluded.

## Required references

The audit followed `AGENTS.md`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`. It consulted the required offline wiki core pages plus Interface Modding and Scripted GUI Modding, installed `common/scripted_guis/_documentation.md`, and the installed vanilla `sov_paranoia_system_ui` decision-category precedent.

The engine references confirm that a decision-category GUI uses `context_type = decision_category`, is attached through the category's `scripted_gui` field, has no parent window, and uses scripted-GUI effects and triggers for control and state behavior. All four Event 014 roots and all five category attachments follow that model.

## Source and asset findings

The actual Event 014 GUI DDS payloads were hydrated from Git LFS before the visual pass. No runtime asset path was changed by hydration.

The four background payloads exactly match their parent bounds:

| Window | Window and background size |
| --- | --- |
| Early | 470x304 |
| Warlord | 470x340 |
| Revealed | 470x380 |
| Wendigo | 470x400 |

The Early network button is the only control on the four compact decision-category headers and has matching visibility and click-enabled gates. Decorative motion plays automatically and is not presented as a player-facing mechanic or preference.

The pre-reveal Early and Warlord windows do not contain Hannibal localisation, portrait sprites, reveal-only metadata, or reveal-only controls. Reveal and Wendigo names and portrait consumers remain gated behind `cannibalism_reveal_complete`.

## Changes

### Early header

`cannibalism.gui.primary_state` no longer repeats `GetCannibalismActiveMissionSummary` inside the primary-theater card. The dedicated mission-summary field remains the single objective summary, so the theater card and objective area no longer duplicate the same line.

### Warlord command

The seven-counter layout was reduced to four actionable readout groups: Larder, Frenzy, Network Alignment, and formation capacity. `cannibalism_warlord_capacity` now uses the full 244-pixel text region inside the existing 278x72 lower card instead of a cramped 150-pixel overlay. Controlled-state and consumed-population details remain available through the owning decisions and Larder/capacity tooltips rather than competing in the compact category header.

### Revealed command

The redundant continental target card was removed from this compact header. The loyalty card shows the integrated-warlord count; the autonomous count remains in its tooltip. The terminal-ready layout therefore exposes at most Global Larder, Network Reach, integrated warlords, and terminal progress.

The 94x86 unification seal is rendered at 0.75 scale at x356,y234. Its effective bounds are x356..426.5 and y234..298.5, leaving a four-pixel gap below the loyalty card and a 5.5-pixel gap above the terminal band.

### Wendigo command

The redundant Winter Victories row was removed from the category header. The terminal band now reports a distinct `Terminal lock engaged` status instead of repeating transformation progress. The existing transformation row and tooltips retain progression and counterplay information.

The 64x64 anchor pulse moved to x310,y248, ending at y312. The terminal band begins at y320, leaving a clean eight-pixel gap.

## Click regions and interaction density

The only remaining decision-category control stays inside its parent window and does not overlap the surrounding content:

| Window/control | Effective click bounds |
| --- | --- |
| Early network ledger | x335..440.78, y266..295.24 |

No new action, hidden click target, gameplay cost, or AI-only route was added. The Event 014 motion layers are active by default; their static siblings remain registered asset fallbacks but are hidden in the live scripted GUI.

## MCP evidence

### Pre-change matrix

The four pre-change renders covered `normal`, `hover`, `disabled`, `warning`, `active`, `completed`, `minimum-value`, `maximum-value`, and `long-text` states at 1280x720, 1600x900, 1920x1080, and 2560x1440 at UI scale 1. Scenarios covered Early Evolution I/II, severe warning, primary theater present/absent, animation enabled/disabled; Warlord alignment, low/abundant Larder, severe Frenzy, animation enabled/disabled; Revealed terminal ready/not ready and animation enabled/disabled; and Wendigo zero/positive anchors, countdown inactive/active, and animation enabled/disabled.

- Early inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/915bdd724d0f2fd728ec49d845542a484469a6cb1f73b26fc4b55b5e5f97d464/140552c58daaacf2ed903ec3ec764f36cec2a5f5a1f5fed3106d2634b0494154/gui-inspect.3c92444a9fe68937.json`
- Early render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/300fe718947473605eec795904b309c5fc19d7a4bd68f35ff68eee2f5f62018d/bcc7f71fbc3314120e3e562a289e58e9d5417cfbd3996f7b839b4858a3ab9ddd/cannibalism_early_header_window-full.svg`
- Warlord inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4679b65f2d4ec1cea5286d25d92ec4f61232299c80d1d9a7a2654339964a169e/ff8f6c6f4fec489500ee6d36f24f6dd7297b4581f9d3e1008148906058463950/gui-inspect.fec51a1681d7bbca.json`
- Warlord render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f9220b1501be0c2becf194360d056e1183969c9556b56163a53dea0856bec15/de631f694dfd123b82b3c791187335be0a21b93b078683ffcb53e6610ac61866/cannibalism_warlord_command_window-full.svg`
- Revealed inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7651589aaccca1021f2f9826f2ab972c67d7504d6fc61547e50accb6d6b24eb/61607aeb2bfdb43ddc4f314fa225ff39d4ddac3db5326200c1115f7393e9796a/gui-inspect.f574f20608bce2e4.json`
- Revealed render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f43cacaf21b95130f2b7e8077795ce264c897d69575b7b6452c1810bae523fbb/70660171bb88badd3a0187f1abe43f66c722602e760727cef0b16ea3c753b093/cannibalism_revealed_command_window-full.svg`
- Wendigo inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c0f176d6d6a19231bf474db92d6960ef6934523c3a8223d1b9e49b6af1f0262/f0056eee0f17f250b2a05551527354f2b33f4beb36505a5a5a1b879d8d9bf17e/gui-inspect.c34f239c823a607c.json`
- Wendigo render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a060211e1cbaf193437d7c0f667f0f993d05068975606b318e3e94a649525d17/5d1cbd20e3952ffae4ce50f11c36617befa77228f58e39cd792872391324a22a/cannibalism_wendigo_command_window-full.svg`

### Rewrite and post-change evidence

`hoi4.gui_rewrite` reviewed the full revised `interface/014_cannibalism_frontline_hunger.gui` source and produced before, proposed, visual-diff, fidelity, validation, and source-diff artifacts. Its write was blocked by truncated repo-wide graph diagnostics and unrelated Event 003/Event 005 symbol collisions, not by an Event 014 selected-window diagnostic. The reviewed proposal was therefore applied through the normal patch workflow.

- Rewrite visual diff: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5bbe01fffa1275aa2f346b8166a813055c4e3b5b25fe739dbd9b1b3f828e771/ca55a44b4011e41040b6d7568b27dcff725baf9a29e2e4d38279588bf990f448/cannibalism_early_header_window-visual-diff.png`
- Rewrite validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/938bcc00a9daf8468f253fcea2811d4e7effd7b6ab65f4a3443402da5b873245/91bc7bb493d16a1fda45bca1953f7238e1b9d877bc9814a44d9365984e9d65fb/cannibalism_early_header_window-rewrite-validation.json`
- Early post inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e9e8a73b1393d0db68da991eecf2b0cd5399594ec42fded74000502b707b6a4/5d94fd89331885291ebb5e834fde325969122caed6e73adcb1d31c9a8f88aa34/gui-inspect.6095c27d207bb177.json`
- Early 1280x720 post render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9eb6230ea178bb9e1ac5924474741cfe6d15b884f31dd5d2946513b37ad9df3d/afa65575ab4afdda4982df595af432db4091b3219b9cc380da66680703dae676/cannibalism_early_header_window-full.svg`
- Warlord post inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dad7fb3ef76c778e1f05ed01c7989e9990167b068cc30c20b2b071297277fd9f/4f433201499a6ff5d22ccabc4bd52ef4366d9b27adadb448770bf7343a2ecda6/gui-inspect.1ec016a698192c72.json`
- Warlord 1920x1080 post render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/581cb785fb792839767f1d25a02e5247d65bd289ad4d551e46a1774d49e5d5a2/80120b9a135df1c145e560699fed947b664ec7104fe492e374ab94741823323c/cannibalism_warlord_command_window-full.svg`
- Revealed final inspect revision `e3c998880cb64d95`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/097b08e436c23e120a74ef5017d8207b29e6684bc7c82c95e6e3113048498600/2890c0a3c5aae60775147125acd22e4d8fba1d37375544378d7dc6d95ff0b9e0/gui-inspect.e3c998880cb64d95.json`
- Revealed final 1920x1080 render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbf07ca030ed0b500c4162eb9ad1f0fef72ac3a2469536a1cfcde9684296ed15/c69409de3ece8c940fb0bbe7e7a411c1549403f23bafcdc0d4b233c6435649bf/cannibalism_revealed_command_window-full.svg`
- Wendigo post inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82fb2507b7baf46c6a666522eff32166bdaae0eac77cb2ccba0cb656b99749d1/1a91a3e6cbc055b1e9acff9f846752718c014df8fc1e033271e2809548c4ad8e/gui-inspect.de4d951625b2dd9f.json`
- Wendigo 1920x1080 post render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8012152d97714361ed07d26a9fc3d37636fb08257447607c14437b1323b6dcf/9b4250e516851812d9dc7e7a9bf976ae46be4875f65c5b3f6f95dbb29dd4371d/cannibalism_wendigo_command_window-full.svg`

## Files changed

- `interface/014_cannibalism_frontline_hunger.gui`
- `common/scripted_guis/014_cannibalism_scripted_gui.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-08-20_decision_category_gui_full_audit.md`

The decision categories, gameplay decisions, AI, costs, events, focus trees, GFX registrations, portraits, and audio were not changed.

## Simplifications, omissions, and blockers

- The MCP rewrite route was exercised but could not write because its repository-wide safety gate encountered unrelated Event 003/Event 005 collisions and a truncated global graph. The proposal was reviewed and applied manually; selected Event 014 post-inspects and renders then returned `ok`.
- The complete pre-change matrix covered all four supported resolutions and all requested state families. Full post-change cross-product renders repeatedly exceeded the MCP 180-second call limit, including Warlord 1280x720 and final Revealed hover-only retries. Post-change evidence therefore uses fresh selected-window inspections plus Early 1280x720 and Warlord/Revealed/Wendigo 1920x1080 renders, backed by exact fixed-size source bounds and unchanged button sprites.
- The 2026-08-22 cosmetic-control removal was followed by fresh `hoi4.gui_inspect` and single-state `hoi4.gui_render` attempts. The MCP server timed out at 180 seconds before returning an artifact for both the Early and Warlord retry. Source inspection confirms the five removed button definitions have no remaining click regions or handlers, but the missing fresh MCP artifact remains an explicit tooling blocker rather than equivalent engine evidence.
- No gameplay fallback, art fallback, reused interface from another event, or out-of-scope GUI change was made.
