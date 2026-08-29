# Event 012 Africa portrait replacement handoff

Status: installed user-provided final candidates; technical validation complete.

Changed asset files are the 15 priority runtime portrait pairs under `gfx/leaders/012_africa/priority_members/` and `gfx/leaders/012_africa/rsa/portrait_012_africa_rsa_mgolombane_sandile.dds`. Each supplied replacement is 156×210 and normalized to the required 131,168-byte, one-level, uncompressed BGRA DDS format through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

Mapping is Asante, Luba, Kilwa, Kongo, Merina, Nubia, Oyo, Aksum, Lunda, Great Zimbabwe, Manden, Harar, Kanem-Bornu, Zulu, Sokoto, and RSA Mgolombane Sandile to their existing stable sprite IDs and runtime basenames. Priority normal and `_source_locked` variants were both replaced in place; RSA keeps its existing normal path. No `.gfx` file needed editing, and both existing Africa portrait GFX files resolve with zero missing texture paths.

Evidence, source copies, processed PNGs, converted DDS files, native-size review contact sheet, and the complete source/runtime hash table are in [the portrait manifest](../../../assets/portraits/012_africa/user_provided_replacements_2026-08-21/manifest.md).

Buganda was intentionally preserved as its existing 131-byte Git-LFS pointer because no replacement was supplied. The Radama I input was archived as evidence only; repository inspection found no matching consumer, so it was not converted, installed, or wired into Merina. Provider/job metadata and independent historical likeness certification were not supplied, so the replacement state remains pending independent review even though the runtime binaries are installed.

No gameplay, character definitions, localisation, events, focuses, decisions, or unrelated assets were changed. RunPod was not operated.
