# Event003 Mandala State-Matrix Render Budget Receipt

Disposition: the single authorized adjusted matrix render was blocked before producing artifacts; no repeat or split request was made.

## Request identity

The read-only route was `hoi4.gui_render` for workspace `mod_chaos_redux_ea3b2d67c2c0` and the exact Event003 window `holy_realm_mandala_category_container`.

The request used the source-backed TIB 1936.1.1 `l_english` fixture, `values.is_ai = false`, `generatedScenarios = { enabled = false }`, one `normal` render state, and one 1280×720 resolution at UI scale 1.

No `refresh`, `sourceBaseline`, or `comparisonScenario` was supplied.

The base scenario was `evt003_tib_refuge_default_no_other_tabs_matrix_20261006`, with only `holy_realm_active` set and no tab flags, preserving the accepted default Refuge selection.

The 14 related scenarios were `evt003_tib_arhats_selected_20261006`, `evt003_tib_diplomacy_selected_20261006`, `evt003_tib_doctrine_selected_max_values_20261006`, `evt003_tib_warnings_selected_empty_risk_20261006`, `evt003_tib_warnings_chaos_999_20261006`, `evt003_tib_warnings_chaos_1000_20261006`, `evt003_tib_warnings_chaos_1001_20261006`, `evt003_tib_refuge_selected_arhats_hover_20261006`, `evt003_tib_mandala_teaching_20261006`, `evt003_tib_mandala_meditation_20261006`, `evt003_tib_mandala_awakened_20261006`, `evt003_tib_mandala_wrathful_20261006`, `evt003_tib_mandala_final_silence_20261006`, and `evt003_tib_mandala_empty_20261006`.

The tab fixtures set only their matching tab country flag and supplied explicit per-control states; the max Doctrine fixture used Bodhi 108/108, Dhyana 4/4, and teaching successes 12/12 with the Buddha Mandate stage; the warning fixtures supplied Chaos 999, 1000, and 1001; the sprite fixtures supplied source-selected stage or variable facts and the corresponding getter values.

The scenario getter strings were supplied through their bare `scenario.values` names and matched the current scripted-localisation branches and English keys, including the default Refuge body, each selected cue, nonempty Doctrine risk line, the strict Warnings gate, and each promoted Mandala sprite id.

## Budget result

The previous 1920×1080 matrix request was rejected with `requested aggregate 68,452,789` pixels over the fixed `67,108,864` limit.

Before the authorized retry, scaling that same aggregate by `(1280×720)/(1920×1080) = 4/9` estimated approximately `30,423,462` viewport pixels, below the limit.

The adjusted request nevertheless returned `RENDER_AGGREGATE_BLOCKED`, status `blocked`, with zero artifacts and no validation checks.

The exact blocker was the native Sharp texture plane for `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_final_silence_animated.dds`: requested aggregate `68,276,183`, reserved `65,453,783`, texture plane `2,822,400` pixels at 6720×420, limit `67,108,864`.

The fixed 16-frame sheet's native pixel-plane reservation remained in the aggregate at the smaller viewport, so the 1280×720 adjustment did not produce a reviewable matrix.

No further render request was made after this blocked result.

## Coverage status

This result proves no visual properties for the unrendered related scenarios and supplies no full-window, crop, state, click-region, hierarchy, or comparison artifacts for them.

The default Refuge/dormant image remains evidenced only by the separate successful 1920×1080/UI1 minimal render receipt in this folder.

Selected Arhats, Diplomacy, Doctrine and Warnings cues; nonempty Doctrine and Warnings risk strings; Chaos boundaries 999/1000/1001; hover; and teaching, meditation, awakened, wrathful, final-silence, and empty-seat sheets remain unresolved by production image review.
