# Scientist portrait identity and source review

This package installs the user-supplied HOI4-style finals from `C:\Users\klimp\Downloads\scientists` as `user_provided_styled_final` candidates. The agent did not operate RunPod, invoke ImageGen, repaint, genericize, or substitute any real-person portrait. The identity links below are attribution/reference sources only; they are not claimed as the source of the supplied styled-final pixels. Rights for redistribution of those supplied bytes remain unresolved beyond the user's explicit internal-installation authorization.

## Required-input inventory

The request specified 70 DDS files; the directory contained 71 DDS files and no other input file type. All 71 were audited. The selected, alternate, and explicit not-needed dispositions are recorded in `input_mapping.json` and `manifest.md`.

## Duplicate identity decisions

- Edwin Broun Fred: `source_01` selected for the stronger frontal fedora/coat framing; `source_02` retained under `alternates/USA_edwin_broun_fred/`.
- Karl Friedrich Meyer: canonical file without `(1)` selected; the `(1)` file is byte-identical by SHA-256 and retained under `alternates/USA_karl_friedrich_meyer/`.
- Masaji Kitano: `source_02` selected because the cap/uniform and pose match the Commons reference; `source_01` retained under `alternates/JAP_masaji_kitano/`.
- Rudolf Weigl: `source_01` selected because the side-profile/goatee framing best matches the archived Weigl reference; `source_02` retained under `alternates/POL_rudolf_weigl/`.

Exactly one runtime portrait and one stable sprite were created per identity; no duplicate scientist identity was added.

## Corrected anonymous-input decisions

- `6925d2612b927.image_00001.dds`: the user authoritatively identified this supplied styled final as Erich Traub. It is installed byte-for-byte for the existing `GER_erich_traub` runtime consumer and retains the established `GFX_portrait_GER_erich_traub` sprite.
- `Sigmund_Rascher_child_00001.dds`: resolved to `GER_sigmund_rascher`; the source-caption evidence describes Sigmund Rascher posing with a child kidnapped by his wife, and the repository already has the stable runtime ID/sprite.
- `s-l1200_00001.dds`: explicitly ignored by the user after the Traub correction. It remains in the durable archive as `not_needed` evidence and receives no identity, sprite, runtime texture, or gameplay assignment.
- `Gutzeit-15_00001.dds`: resolved to `GER_kurt_gutzeit`; the repository already has the stable runtime ID/sprite, and Federal Archive/Commons Kurt Gutzeit imagery provides the defensible broad facial/framing comparison.

## Identity references

The per-input identity-reference URL, source mode, rights status, hash, QA, runtime basename, and sprite are in `input_mapping.json`. The principal external references used for the ambiguous/duplicate review were:

- [Frank Macfarlane Burnet — Australian Dictionary of Biography](https://adb.anu.edu.au/biography/burnet-sir-frank-macfarlane-mac-12267)
- [Shiro Ishii — PBS American Experience](https://cgi.pbs.org/wgbh/amex/weapon/peopleevents/p_ishii.html)
- [Masaji Kitano — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Masaji_kitano.jpg)
- [Edwin Broun Fred — Wikipedia](https://en.wikipedia.org/wiki/Edwin_Broun_Fred)
- [Karl Friedrich Meyer — Wikipedia](https://en.wikipedia.org/wiki/Karl_Friedrich_Meyer)
- [Rudolf Weigl — Wikipedia](https://en.wikipedia.org/wiki/Rudolf_Weigl)
- [Sigmund Rascher — Wikipedia](https://en.wikipedia.org/wiki/Sigmund_Rascher)
- [Kurt Gutzeit — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Kurt_Gutzeit.jpg)
- [Sergey/Sergei Muromtsev — Wikipedia](https://en.wikipedia.org/wiki/Sergey_Muromtsev)

## Review standard

The source crop is the full supplied 156x210 canvas `[0, 0, 156, 210]`; the exact crop PNG is decoded-pixel-equal to the supplied DDS. Native and 4x installed-runtime contact sheets in `contact_sheets/` provide human framing review for all 66 installed portraits. The older `ambiguous_vs_existing` sheets remain historical review evidence and are superseded for these two anonymous inputs by the user's Traub identification and explicit ignore instruction. Every selected candidate received identity, framing, provenance, and strict DDS format checks; the not-needed input is not wired.
