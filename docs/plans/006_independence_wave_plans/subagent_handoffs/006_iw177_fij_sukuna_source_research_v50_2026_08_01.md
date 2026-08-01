# IW177 FIJ / Ratu Sir Lala Sukuna source-research handoff

Date: 2026-08-01

Scope: sourced male FIJ leader portrait for the 1936 Independence Wave start. No gameplay, GFX, localisation, attestation, or runtime files were edited.

## Result

**Blocked.** I did not find an attributed, rights-cleared archival male photograph that can be defended as no later than 1936. The strongest identity source remains the National Archives of Fiji portrait on Wikimedia Commons, but its source metadata explicitly says “circa 1940s,” so it does not replace the existing source-date blocker for the 1936 leader state.

The grounded-identity gate applies: Ratu Sir Lala Sukuna is a real Fijian chief, scholar, soldier, and statesman. A generated one-person portrait or invented substitute is not allowed. The exact head-and-shoulders crop, source-locked repaint, 156x210 candidate, independent audit, DDS, and sprite handoff were intentionally not created because the source gate did not pass.

## Evidence package

- Manifest with source links, provenance, hashes, rights, date fit, role fit, and blockers: [fij_sukuna_source_manifest.md](../../../assets/006_independence_wave/fij_sukuna_source_manifest.md).
- Candidate comparison sheet: `docs/assets/006_independence_wave/sources/fij_sukuna/contact_sheet_fij_sukuna_candidates.png`.
- Retained source workspace: `docs/assets/006_independence_wave/sources/fij_sukuna/`.
- Strongest archival identity source: `docs/assets/006_independence_wave/sources/fij_sukuna/commons_ratu_sir_lala_sukuna.jpg` (960x1192; SHA-256 `d5bb8e7ec6c2464cbc8affa5c8b314f25a5a8126bd17fd4ef7c63d83ecef2424`). Commons metadata credits National Archives of Fiji, identifies the subject, and records `PD-Fiji` / public domain, but records the source date as “circa 1940s.”
- Fiji Museum library candidate: `fijitimes_library_1.jpg` (720x579; SHA-256 `45257e77b9649ae916ba4ac02ff97e31ba96eb13e79cdb1229ae4bbcdb3fb1c9`); the Fiji Times caption credits Fiji Museum but gives no capture date or reusable license.
- iTaukei Affairs ceremony candidate: `fijitimes_library_2.jpg` (591x442; SHA-256 `b10e00f9213cfb9b7bb89a50e40685b4c40e75a09b33ababab6f1874dc2afa94`); EXIF names the subject and iTaukei Affairs but gives no capture date or reuse permission.

## Source links reviewed

- [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Ratu_Sir_Lala_Sukuna.jpg) and [National Archives credited image](https://upload.wikimedia.org/wikipedia/commons/7/73/Ratu_Sir_Lala_Sukuna.jpg): strongest identity and rights evidence, but “circa 1940s.”
- [Fiji Times biography/photo article](https://www.fijitimes.com.fj/the-life-and-legacy-of-ratu-sir-lala-sukuna/) and [Fiji Museum library image](https://www.fijitimes.com.fj/wp-content/uploads/2022/10/Ratu-Sir-Lala-Sukuna-in-the-library-area.jpg): named subject, no date/license.
- [University of the South Pacific historical-significance page](https://www.usp.ac.fj/news/the-historical-significance-of-ratu-sir-lala-sukuna/), [USP poster](https://www.usp.ac.fj/wp-content/uploads/2024/05/Sukuna.jpg), [Fiji Ministry of Foreign Affairs commemorative page](https://www.foreignaffairs.gov.fj/happy-ratu-sukuna-day-fiji/), and [modern graphic](https://www.foreignaffairs.gov.fj/wp-content/uploads/2025/06/New-post-4-sukuna-480x360.jpg): modern composites, not archival identity sources.
- [Find a Grave memorial photo](https://www.findagrave.com/memorial/228374153/lala-sukuna/photo): modern monument photograph, not a portrait and no reusable license.

## Unblock request

Obtain a high-resolution National Archives of Fiji, Fiji Museum, or iTaukei Affairs scan with photographer/archive attribution, a capture date no later than 1936 (or an explicitly acceptable 1936-era range), and a reusable license/public-domain statement. After receipt, run `extract_portrait_source_crop.py` with exact decoded-pixel equality evidence before any repaint or conversion. Do not use the circa-1940s Commons image as a silent fallback.
