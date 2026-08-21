# Event 014 Cannibalism user-supplied warlord portrait replacements

Date: 2026-08-21

The supplied 16 DDS portraits replace the current Event 014 warlord runtime pointer targets. Every input is already a final 156x210 one-level uncompressed BGRA DDS with a 131168-byte file size, so the runtime copy preserves the supplied bytes and removes only the user-output `_00001` suffix from the target name.

The existing `interface/014_cannibalism.gfx` registrations remain unchanged. Regional sprite aliases continue to point at the stable runtime textures, and no character, country, gameplay, or localisation identifiers were added. CBG remains unchanged because its existing sprite aliases intentionally reuse the CBF base portrait and no CBG-specific file was supplied.

| Runtime identity | Archived supplied input | SHA-256 | Runtime target | Wiring status |
| --- | --- | --- | --- | --- |
| CBA warlord Middle East | `leader_CBA_warlord_middle_east_00001.dds` | `62b0deb119fdce844dd7bebdc6ae7961146031cf57bab248e99a7302824b6c15` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_middle_east.dds` | Existing CBA regional sprites consume it. |
| CBA warlord South America | `leader_CBA_warlord_south_america_00001.dds` | `926ddf5613232fc4aee968991fe9a05207cf191f3c5eb6453ba83ff4c7c0640c` | `gfx/leaders/014_cannibalism/leader_CBA_warlord_south_america.dds` | Existing CBA regional sprites consume it. |
| CBB warlord Middle East | `leader_CBB_warlord_middle_east_00001.dds` | `9df28df8e2e02063bd36fa647367e4c37dc695fd292a1ab3e2ff9a84bc42c07e` | `gfx/leaders/014_cannibalism/leader_CBB_warlord_middle_east.dds` | Existing CBB regional aliases consume it. |
| CBC warlord base | `leader_CBC_warlord_00001.dds` | `8fd687463d3a67f3a7fb71ad85cfbaf82f48c994efc3b5db0f4cc1d1de96a465` | `gfx/leaders/014_cannibalism/leader_CBC_warlord.dds` | Existing CBC regional aliases consume it. |
| CBC warlord South America | `leader_CBC_warlord_south_america_00001.dds` | `0e4299327870aab31dfef1eaf1917be4c43deb150034598f1b78cba4bde58cd3` | `gfx/leaders/014_cannibalism/leader_CBC_warlord_south_america.dds` | Existing CBC South America sprite consumes it. |
| CBD warlord North America | `leader_CBD_warlord_north_america_00001.dds` | `1163d1bf30763f950553cde8656a66c3b4b8c33a4438f53bb80083d4bff2c135` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_north_america.dds` | Existing CBD regional aliases consume it. |
| CBD warlord South America | `leader_CBD_warlord_south_america_00001.dds` | `a537cdd1dea9cae071df7e5e63e3532a68ae2db9f880e315a84ae70c8d41c5d5` | `gfx/leaders/014_cannibalism/leader_CBD_warlord_south_america.dds` | Existing CBD South America sprite consumes it. |
| CBE warlord base | `leader_CBE_warlord_00001.dds` | `89ba9635fe1dc28485b023376d3572d9bec56e73d31da89d09e9d75988ed57c0` | `gfx/leaders/014_cannibalism/leader_CBE_warlord.dds` | Existing CBE regional aliases consume it. |
| CBE warlord North America | `leader_CBE_warlord_north_america_00001.dds` | `51e13236ae496307843d5326f73e4877c51db1ed5f822beae0238455468fbbc0` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_north_america.dds` | Existing CBE North America sprite consumes it. |
| CBE warlord South America | `leader_CBE_warlord_south_america_00001.dds` | `4a32f397475172984540b80dea255c2a5320856e325af68f346fb5c33cc3abe1` | `gfx/leaders/014_cannibalism/leader_CBE_warlord_south_america.dds` | Existing CBE South America sprite consumes it. |
| CBF warlord base | `leader_CBF_warlord_00001.dds` | `56b2ed307a6d8be4e7445738f0e2e6eb603abd5c52147b19ce6806219c35961c` | `gfx/leaders/014_cannibalism/leader_CBF_warlord.dds` | Existing CBF and CBG aliases consume it. |
| CBF warlord Africa | `leader_CBF_warlord_africa_00001.dds` | `87845e4d4c6b6b0038d8759cf17281751250d2a0ac52fdbbb6cff7776442a313` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_africa.dds` | Existing CBF Africa sprite consumes it. |
| CBF warlord Oceania | `leader_CBF_warlord_oceania_00001.dds` | `e45e068d09eeaeb42afbaa424b9f108d161df91edad3e6308a552062af8de4b1` | `gfx/leaders/014_cannibalism/leader_CBF_warlord_oceania.dds` | Existing CBF Oceania sprite consumes it. |
| CBH warlord base | `leader_CBH_warlord_00001.dds` | `90abf0d8f5edc261b8c4f4f208feb63cf2a5e14b0d12dedda14c75ce51e1f83a` | `gfx/leaders/014_cannibalism/leader_CBH_warlord.dds` | Existing CBH regional aliases consume it. |
| CBH warlord North America | `leader_CBH_warlord_north_america_00001.dds` | `36f9228fd2112f454439e0e73d301fbb45668e92878fe7aac6095e17574a9bd5` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_north_america.dds` | Existing CBH North America sprite consumes it. |
| CBH warlord South America | `leader_CBH_warlord_south_america_00001.dds` | `2685089dd9148507acd14e2014124bd92db7c21e225c8cf61bf46c98a7fc6e0e` | `gfx/leaders/014_cannibalism/leader_CBH_warlord_south_america.dds` | Existing CBH South America sprite consumes it. |

No new icons or GFX registrations are required for this replacement pass. Future work is limited to supplying a distinct CBG asset if the existing CBF alias is ever meant to become a separate regional identity.
