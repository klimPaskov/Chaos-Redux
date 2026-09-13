# Event 033 Acid Rain Audio Revalidation

The accepted super-event excerpt remains Carl Maria von Weber's *Der Freischutz* Overture performed by the Skidmore College Orchestra, with source, rights, attribution, and audition evidence retained in `docs/assets/033_acid_rain/`.

On 2026-09-01, the repository audit found that the manifest-listed OGG companion was absent while the accepted runtime WAV remained present and matched its recorded checksum. The OGG was rebuilt directly from that accepted WAV with libvorbis quality 5 and an explicit composer tag.

## Installed files

- WAV SHA-256: `C0BD481F23AECD058BBCC49F54570353CA2974FF5EED9E497B6980721AABB033`
- OGG SHA-256: `7951F486E425CB059C34C093190EBBE040DB10F3570FE3BC4309E89F6C1A4951`
- OGG size: 1,382,059 bytes
- OGG probe: 80.000 seconds, stereo, 44,100 Hz Vorbis

## Revalidation

- The OGG decoded end to end through FFmpeg without an error.
- EBU R128 measurement was -19.9 LUFS integrated, 9.0 LU LRA, and -5.8 dBFS true peak.
- A `silencedetect=noise=-60dB:d=0.50` scan reported no silence events.
- The installed sound inventory contained no other file with the accepted OGG checksum.
- Runtime playback remains wired to the accepted WAV; rebuilding the companion did not change the in-game sound identifier or excerpt.
