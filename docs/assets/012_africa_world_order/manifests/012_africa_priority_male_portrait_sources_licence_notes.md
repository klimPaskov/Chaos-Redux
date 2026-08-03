# Event 012 Africa historical male portrait source notes

This note accompanies `012_africa_priority_male_portrait_sources_manifest.json`. It records the source and rights decisions for the male-only sovereign audit. The package contains archival masters, exact source crops, 156x210 source-evidence PNGs, and converter-produced evidence DDS files. Those DDS files are not runtime replacements. Parent-owned `.gfx`, characters, localisation, and gameplay remain untouched.

## Safe identity candidates requiring the normal repaint gate

- Kanem-Bornu: Shehu Sanda Kura is named in the 1936 Nigeria Handbook image. Commons records the work as public domain, but the selected local byte is a vendor scan. Keep the Commons page and vendor URL together. Current runtime promotion remains the separately reviewed source-locked repaint, not this raw-source evidence.
- Kongo: Pedro VII Afonso is named in the 1934 Sociedade de Geografia de Lisboa photograph. Commons records the image as public domain. The crop includes only the king's source-visible hat, cape, robe, baton, moustache, and spectacles.
- Harar: Emir Abdullahi is the named subject of Philipp Paulitschke's 1885 Gallica/BnF image. The Commons derivative is CC BY-SA 4.0, so attribution and share-alike obligations must remain attached to any future derivative.
- Buganda: Daudi Cwa II is named in Jules Leclercq's 1913 plate. The Commons record carries Public Domain Mark 1.0. The exact crop rectangle is `(650,860,1700,2260)` in the 2385x3203 master and is independently pixel-equal to the master region.
- Merina: Radama II is the exact male subject of the circa 1862 USC Libraries portrait. The source is public domain in the United States, but the photographer and non-US status are not established; keep this as `needs_user_review`, not a runtime grant. This row replaces the earlier female Ranavalona III candidate for the male-only audit.

## Rights or provenance review candidates

- Sokoto: Sir Siddiq Abubakar III is a named 1959 Eliot Elisofon/Smithsonian image. Commons labels it public domain under Nigerian law, while the Smithsonian metadata requests permission for reproducing the archive image. No runtime use until permission is cleared.
- Luba: Albert Kalonji's official portrait is hosted on Commons with a Democratic Republic of the Congo public-domain claim, but the modern uploader and AP News Library provenance are not independently cleared. Treat the crop as evidence only.
- Lunda: Daniel P. Biebuyck's archive names Mwaantayaav Mbaku Citend and dates the pictured ruler to 1957. The page does not grant a reusable license. Photographer/archive permission is required before repaint or distribution.
- Zulu: Dinuzulu kaCetshwayo's March 1908 James Stuart photograph is CC0. The source and identity are strong, but actor eligibility remains blocked; the image must never be labelled Solomon kaDinuzulu.

## Explicit blocks

- Asante: Prempeh II is already owned by Event 006. The available Prempeh I image is a named group photograph, but the exact individual position is not independently confirmed. Do not clone Event 006's portrait or silently select a face from the group.
- Oyo: the National Archives UK image is OGL v1.0 and captioned `Alaafin Oyo c. 1910`, but the mounted figure's face is obscured and no named Alaafin is supplied. It is not safe to relabel the image as Lawani Agogoija, Siyanbola Ladigbolu, or another person.
- Manden, Aksum, Kilwa, Nubia, and Great Zimbabwe: the requested historical identities are pre-photography or lack a defensible named male portrait. Modern generic or reconstructed faces would be identity substitutions.

## Processing and evidence boundary

The exact crop JSON files record crop rectangles, SHA-256 values, and decoded pixel equality against the source masters. The processed PNGs are deterministic direct resizes to 156x210 and are labelled `source_evidence`; they are not source-locked repaints and should not be wired as final portraits. The DDS files are converter-produced evidence derivatives in `docs/assets/012_africa_world_order/final_dds/portraits/`, not files under the runtime `gfx/leaders/` tree.
