# IW-002 Wales portrait ownership scan - retry 03

This scan covers the two requested grounded male identities for Event 6, IW-002 Wales: a civic or national figure and a military, territorial, or mountain commander. The scan is source-clearance evidence only. It does not edit characters, localisation, interface, GFX, or gameplay files.

## Roots checked

- Installed vanilla: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`
- Approved reference mod `1521695605`: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1521695605`
- Approved reference mod `2265420196`: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2265420196`
- Approved reference mod `1458561226`: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1458561226`
- Current Chaos Redux repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`

The search covered character definitions, country history, leader and advisor portrait consumers, interface/GFX definitions, and localisation text. Binary image data and unrelated build/vendor files were excluded from text matching.

## Terms checked

The exact and variant forms checked were `David Grenfell`, `David Rhys Grenfell`, `James Henry Thomas`, `J. H. Thomas`, `J H Thomas`, `William John Gruffydd`, `W. J. Gruffydd`, `George Cornwallis-West`, `Georgecornwalliswest`, `William Ambrose Bebb`, `Ambrose Bebb`, `W. A. Bebb`, `Hugh Evan-Thomas`, `Hugh Evan Thomas`, and `Ivor Thomas`.

## Results

### Clear in checked roots

- David Grenfell: no owner found in vanilla, the three approved reference mods, or current Chaos Redux.
- George Cornwallis-West: no owner found in vanilla, the three approved reference mods, or current Chaos Redux.
- W. J. Gruffydd: no owner found in vanilla, the three approved reference mods, or current Chaos Redux.
- Ivor Thomas: no owner found in vanilla, the three approved reference mods, or current Chaos Redux. This is only an alternate because his Welsh identity and uploader provenance need review.
- James Henry Thomas: no owner found in vanilla, the three approved reference mods, or current Chaos Redux. The retained Commons source is too small for the requested source-locked portrait workflow.

### Blocked ownership conflicts

- William Ambrose Bebb is actively owned by Kaiserreich `1521695605`. The mod recruits `WLS_ambrose_bebb`, defines its character portrait consumers in `common/characters/WLS characters.txt` and `interface/kaiserreich/portraits/WLS_portraits.gfx`, and supplies `WLS_ambrose_bebb` localisation. The source is retained only as a rejected comparison candidate.
- David Lloyd George is owned by installed vanilla content under `common/characters/ENG.txt` (`ENG_david_lloyd_george`), the `GFX_idea_ENG_david_lloyd_george` consumer in the Man the Guns interface, and English localisation (`ENG_david_lloyd_george`). It cannot be reused for this new WLS role even though the source photograph is clear.

### Existing Chaos Redux consumer note

The current repository already reserves these parent-owned sprite consumers:

- `GFX_portrait_WLS_independence_wave_national_council` -> `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`
- `GFX_portrait_WLS_independence_wave_mountain_commandant` -> `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds`

The existing national-council localisation still names Saunders Lewis. This asset subtask does not alter that consumer or any identity wiring.

## Interpretation

David Grenfell and George Cornwallis-West pass the ownership gate for parent-owned downstream processing. The source package still requires later source-locked ImageGen, independent likeness/style/provenance review, deterministic `156x210` processing, and DDS conversion before either identity can be called runtime-ready. W. J. Gruffydd is a visually strong alternate but is held because the available image is dated 1946, after the requested 1936-era setting. Bebb and David Lloyd George remain blocked and must not be wired.
