# IW-039 Cossack Don portrait source-placeholder handoff — 2026-08-12

## Disposition

`SOURCE_PLACEHOLDER_READY_PENDING_PARENT_CONSUMER_AND_INDEPENDENT_REVIEW`; IW-039 remains fail-closed. This handoff owns portrait evidence only. No gameplay, attestation, Join, history, focus, decision, AI, country, flag, or localisation file was edited.

## Identity and ownership gate

The accepted candidate is Vladimir Ilyich Sidorin (1882–1943), the existing vanilla `DON_vladimir_sidorin` identity. Vanilla `common/characters/DON.txt` defines him as a despotism/fascism country leader and field marshal, and vanilla DON history recruits him. The subject was a Don Army commander from February 1919 through April 1920, a White movement general, and a Don Cossack. The package defines no duplicate character and no alternate institutional face.

Any future Event 006 consumer must reuse `DON_vladimir_sidorin` under an explicit origin/ownership guard. The IW-039 preflight still reports no Event 006 DON character, setup adapter, content attestation, or safe DON-versus-DHC state/capital policy. Those are runtime blockers, not reasons to invent a replacement face.

## Source and rights evidence

The source page is [Wikimedia Commons File:Vladimir Ilyich Sidorin.jpg](https://commons.wikimedia.org/wiki/File:Vladimir_Ilyich_Sidorin.jpg). The immutable binary was archived from the Commons-credited RIA 1914 item [Сидорин Владимир Ильич](https://ria1914.info/index.php/%D0%A4%D0%B0%D0%B9%D0%BB:%D0%A1%D0%B8%D0%B4%D0%BE%D1%80%D0%B8%D0%BD_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%98%D0%BB%D1%8C%D0%B8%D1%87_-.jpg). Commons metadata identifies the subject as Russian general Vladimir Sidorin, dates the image 1914–1918, credits an unknown author, and marks it Public domain / `PD-RusEmpire`. Rights are `PASS`: the Commons record explicitly states the United States public-domain basis for publication before 1 January 1931. Source-page snapshots are co-located under the portrait package.

## Package and hashes

Package root: `docs/assets/portraits/006_independence_wave/iw039_don_vladimir_sidorin_source_placeholder_2026_08_12/`.

| File | Dimensions | SHA-256 |
|---|---:|---|
| `portrait_DON_independence_wave_vladimir_sidorin_original.jpg` | 540×800 RGB JPEG, 77,376 bytes | `9e5595351e93b0f20f6cf7bbe64042c766caffe3fc782471530fdfdcaef06088` |
| `portrait_DON_independence_wave_vladimir_sidorin_source_crop.png` | 380×512 RGB PNG, 285,591 bytes | `7ff2a38ffa1425745013d6bee38c535f675869a7e7fd0a3f80f2977d87da434a` |
| `portrait_DON_independence_wave_vladimir_sidorin_156x210.png` | 156×210 RGB PNG, 60,327 bytes | `abb407aa262cb9ef54a1fd8d79f274c2e7f6b7d22ed9e8aafecd66e03465756e` |
| `portrait_DON_independence_wave_vladimir_sidorin_4x_nearest.png` | 624×840 RGB PNG, 90,238 bytes | `d0ee226f0d290066ff62b98238693bd4b4f55ba9fb17641f1eab5fcd6b5b1dc0` |

The crop was made by `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` with manual half-open coordinates `[80,0,460,512]`; the paired JSON records exact decoded-pixel equality, dimensions, hashes, and the normalized command. The candidate is a deterministic RGB `156x210` Pillow LANCZOS resize. The source is unchanged; no ImageGen, ComfyUI, repaint, face reconstruction, recolouring, enhancement, or RunPod operation was used.

## Proposed runtime handoff (not installed)

Proposed sprite: `GFX_portrait_DON_independence_wave_vladimir_sidorin`.

Proposed texture: `gfx/leaders/006_independence_wave/portrait_DON_independence_wave_vladimir_sidorin.dds`.

Proposed target `.gfx`: `interface/006_independence_wave_iw039_don_portraits.gfx`.

```text
spriteTypes = {
	SpriteType = {
		name = "GFX_portrait_DON_independence_wave_vladimir_sidorin"
		texturefile = "gfx/leaders/006_independence_wave/portrait_DON_independence_wave_vladimir_sidorin.dds"
	}
}
```

No DDS or `.gfx` entry is installed yet. Independent parent review of identity, framing, and provenance plus a live origin-gated consumer is required before running the standard DDS converter and wiring this sprite. Runtime must never reference `docs/assets/portraits/`.

## Review, skipped checks, and blockers

- Producer review: identity `PASS`; framing `PASS_WITH_CAVEAT` (readable head-and-shoulders composition with period uniform, medals, and archival halftone retained); provenance `PASS` (Commons PD-RusEmpire plus explicit US pre-1931 public-domain basis).
- Parent independent review: pending.
- DDS conversion/header/pixel-round-trip: skipped pending independent approval and runtime consumer.
- `.gfx` registration and character wiring: intentionally skipped; no Event 006 DON consumer or safe origin branch exists.
- Localisation: no new key; vanilla `DON_vladimir_sidorin` remains the only identity key.
- Advisors, high command, dossier, army-small, operative, female, fictional, or alternate Sidorin portraits: explicitly not authorized.

The complete package manifest, provenance contract, crop JSON, source snapshots, review enlargement, and GFX handoff are in the package root. The durable evidence remains available while IW-039 is blocked.
