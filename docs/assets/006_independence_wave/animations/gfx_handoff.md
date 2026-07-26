# Event 006 animated status-panel GFX handoff

The four ASSET-040 through ASSET-043 families are wired into the Event 006 Statehood Ledger. All frames are 64x64, centered, alpha-transparent at unused corners, and authored as state-specific source art. Use the DDS sheet paths below; GIFs are review-only.

| Asset | Static sprite | Animated sprite | Runtime static DDS | Runtime sheet DDS | noOfFrames | Sheet |
| --- | --- | --- | --- | --- | ---: | --- |
| ASSET-040 recognition seal | `GFX_independence_wave_recognition_seal_static` | `GFX_independence_wave_recognition_seal_animated` | `gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_static.dds` | `gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_sheet.dds` | 5 | 320x64 |
| ASSET-041 dependency warning | `GFX_independence_wave_dependency_warning_static` | `GFX_independence_wave_dependency_warning_animated` | `gfx/interface/006_independence_wave/animations/independence_wave_dependency_warning_static.dds` | `gfx/interface/006_independence_wave/animations/independence_wave_dependency_warning_sheet.dds` | 3 | 192x64 |
| ASSET-042 league charter activation | `GFX_independence_wave_league_charter_activation_static` | `GFX_independence_wave_league_charter_activation_animated` | `gfx/interface/006_independence_wave/animations/independence_wave_league_charter_activation_static.dds` | `gfx/interface/006_independence_wave/animations/independence_wave_league_charter_activation_sheet.dds` | 4 | 256x64 |
| ASSET-043 formable eligibility seal | `GFX_independence_wave_formable_eligibility_seal_static` | `GFX_independence_wave_formable_eligibility_seal_animated` | `gfx/interface/006_independence_wave/animations/independence_wave_formable_eligibility_seal_static.dds` | `gfx/interface/006_independence_wave/animations/independence_wave_formable_eligibility_seal_sheet.dds` | 4 | 256x64 |

The Statehood Ledger uses the live state-strip sprites by default and exposes an `Animate` toggle that swaps each strip for its matching frame-by-frame animated sprite. The static DDS files remain the non-animated fallback and are registered in the same `.gfx` surface.

```text
spriteTypes = {
	spriteType = {
		name = "GFX_independence_wave_<family>_static"
		texturefile = "gfx/interface/006_independence_wave/animations/independence_wave_<family>_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_independence_wave_<family>_animated"
		texturefile = "gfx/interface/006_independence_wave/animations/independence_wave_<family>_sheet.dds"
		noOfFrames = <frame_count>
		animation_rate_fps = 5
		looping = yes
		play_on_show = yes
	}
}
```

The parent implementation now owns the `.gui` placement, scripted-GUI context, visibility predicates, state-to-frame mapping, and toggle behavior. `play_on_show = yes` is intentional for the explicit user-selected animation mode; the live strips remain the deterministic state readout when animation is disabled.

Runtime DDS SHA-256 values are recorded in `animation_build_report.json`: recognition static `c1871b031ccb2c264c6508e6a02482231020ab81c63cabe4efaa2f0e794c41cc`, recognition sheet `b6572f49f85660e64842a9a4b5cc56a16076a0c12c1d00a875ba8708603fe9fd`; dependency static `c52d3a2d17dbd594c9ceac36778cab4eb6dfe525efb26d424211282a53bcd1c4`, dependency sheet `2ed53c2f6ae1a55ebd89f5ede4795885de1b16d5fdd51741d0936fe192162fe6`; league static `08f021545bae25aa875a557e54275058bacaf0156ee6617d297d3724643457af`, league sheet `fe4d108d4a085f719eaacf57352bb3f85b69bba1fec88360c0c41ef28734858b`; formable static `de2f835fb3e60bd6fa906884af572f9a588fc614b1b409d91411c6867ebb6a8a`, formable sheet `db8ca4e24c7ce343a354b9a768dc5b2533666bf5779ddf4a9f5a9282b4f64271`.

No advisor or dossier assets are included in this handoff. Runtime `.gfx`, `.gui`, scripted-GUI, and localisation wiring is present in the parent Event 006 files listed above.
