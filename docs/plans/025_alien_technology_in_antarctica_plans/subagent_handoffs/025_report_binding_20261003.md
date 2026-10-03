# Event 025 failure-report asset binding

Disposition: implemented at source level; event render and complete asset acceptance remain unresolved.
Acceptance basis: the user's explicit request to audit and repair every Event 025 visual consumer, plus the report-image and visible-key acceptance gates.

`chaosx.nr25.86` referenced `GFX_report_event_025_antarctic_sabotage` without a sprite definition.
The existing Event 025 DDS is registered under that exact alias in `interface/025_alien_technology_in_antarctica.gfx`.
No new image, resize, icon reuse, or pixel fallback was introduced.
The processed image and decoded DDS were opened individually: damaged equipment and severed camp wiring depict a setback without attributing a culprit.
The DDS has native 210x176 dimensions and SHA-256 `f81491db9cbea41ec481b31bc2be9976b1e7b33188e394d9595c839a10b21914`.

Three source tests in `.tools/test_event025_report_assets.py` prove that every Event 025 event picture alias is registered in the dedicated GFX, every registered texture path exists, and the failure report selects the expected native-size DDS.
These tests do not prove visual rendering, menu delivery, or live-game consumer appearance.
The mandatory event/GUI MCP evidence remains incomplete after the previously recorded narrow timeouts.

The asset audit is promoted as one explicitly named Markdown metadata file despite the existing `docs/assets/` ignore rule.
No ignored image tree is added through that promotion.
Its earlier blanket wiring claim is withdrawn: 131 texture declarations are not 136 unique live DDS consumers, and the five ideas plus two decision-family assets are inside that declaration count.
Crossing/rescue report consumers, eight standalone sector-state consumers, provisional PNG paths, four static evolution-loop substitutions, full Board render/privacy/click-region review, and independent final asset acceptance remain unresolved.
The small binding repair does not accept any of these omissions or fallbacks.
