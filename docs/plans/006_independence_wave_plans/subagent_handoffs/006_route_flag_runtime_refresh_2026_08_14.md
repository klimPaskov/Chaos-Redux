# Event 006 route flag runtime refresh

Status: complete for the engine-facing TGA format refresh; this is an asset QA repair, not a country-admission decision.

## Scope

The Bashkiria (`BSK`) and Mari (`MEL`) route flag packages already contained the accepted source artwork and processed TGA ladders, but those processed TGA files were RGB/24-bit with descriptor `0`. Installed vanilla flag files use uncompressed truecolor BGRA/32-bit TGA files with descriptor `8`, so the runtime copies were normalized without changing their visible RGB pixels or bottom-left orientation.

The source packages remain unchanged under `docs/assets/006_independence_wave/iw045_bashkiria_flags_2026_08_14/processed_tga/` and `docs/assets/006_independence_wave/iw047_mari_flags_2026_08_14/processed_tga/`. Runtime files are under the engine-required roots `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

## Runtime files

The refresh covers 24 files: four BSK route marks and four MEL route marks at each of normal (`82x52`, `17074` bytes), medium (`41x26`, `4282` bytes), and small (`10x7`, `298` bytes) sizes.

Every refreshed file has TGA image type `2`, 32 bits per pixel, descriptor `8`, and an opaque alpha byte for every pixel. The runtime payload is byte-derived from the package RGB payload by inserting alpha `255` after each BGR triplet; no colour, ordering, crop, or orientation transform was applied.

## Runtime hash evidence

| Family | Size | File | Runtime SHA-256 |
| --- | --- | --- | --- |
| BSK | medium | `BSK_INDEPENDENCE_WAVE_AGRARIANX.tga` | `a6063f96a196a905579229ca3278f9e229d6cb41e073fcc8d1d0f7b5bde86eee` |
| BSK | medium | `BSK_INDEPENDENCE_WAVE_CIVICX.tga` | `c2028f5357407cbf6afd130deb0445829a39b918f6924638133eb4b362f3f2df` |
| BSK | medium | `BSK_INDEPENDENCE_WAVE_EMERGENCYX.tga` | `01a2b4405351ff37cdaa1a2ae49fa6bf99b8722754f5ba3f572556cc9c4135a9` |
| BSK | medium | `BSK_INDEPENDENCE_WAVE_SOCIALISTX.tga` | `cce1155bd53d22f651d65bd5ead831fd866e922a35de5575fbc8e02850e38f9e` |
| BSK | normal | `BSK_INDEPENDENCE_WAVE_AGRARIANX.tga` | `5b7abc8b5a27940ea72a4ddd25c0c5a0c145f20d573e768e7883a561c10bd569` |
| BSK | normal | `BSK_INDEPENDENCE_WAVE_CIVICX.tga` | `6264f9c198b7250d78d9050772b6bca4ee46f22a4ab919a7a575eda1e02e6117` |
| BSK | normal | `BSK_INDEPENDENCE_WAVE_EMERGENCYX.tga` | `57a1c5fbd889288a6113bca00cd1d5b9216dc4584a5f0854779f60dbc32b75c5` |
| BSK | normal | `BSK_INDEPENDENCE_WAVE_SOCIALISTX.tga` | `5cb78ce6685c36aad147f09d02aaeba54d75e2461a822910ef6d8064e9208466` |
| BSK | small | `BSK_INDEPENDENCE_WAVE_AGRARIANX.tga` | `692fc568c7f0f1979abd41020eb96772f5d5d9673c6979e28feae2e94da5613c` |
| BSK | small | `BSK_INDEPENDENCE_WAVE_CIVICX.tga` | `d85fa9c1db6262e16d61b6ce0386c4b88bcbbf37cd435198c40e1bc19b461089` |
| BSK | small | `BSK_INDEPENDENCE_WAVE_EMERGENCYX.tga` | `fe3da99ffc54006fea2157274bbd0d0905be776d5037cc0919e3dc70cd454195` |
| BSK | small | `BSK_INDEPENDENCE_WAVE_SOCIALISTX.tga` | `034312941e2c1b182055a6d656456c8152030836ef76daf134f82ddb151a67ea` |
| MEL | medium | `MEL_INDEPENDENCE_WAVE_CIVICX.tga` | `ceff24492598d3d8093e0c3eec5a0c072f100b5466b9b5c9c8f6e4727727c1fd` |
| MEL | medium | `MEL_INDEPENDENCE_WAVE_EMERGENCYX.tga` | `a63587bd36286044caa160b7f84be3d2a8eaa2aab535e4cf1d374853e388caab` |
| MEL | medium | `MEL_INDEPENDENCE_WAVE_FORESTX.tga` | `9bc48044dd52d4309255c2095a010f45ebd227c152cc1fa1f03f37c9b2e2eaeb` |
| MEL | medium | `MEL_INDEPENDENCE_WAVE_SOCIALISTX.tga` | `cad406ca134e3c954382bccde75fa30b56a5db1de769b6dd0794ce6cc17d8868` |
| MEL | normal | `MEL_INDEPENDENCE_WAVE_CIVICX.tga` | `7a1dcf14d2bc44c5d5c83dcda75d24b71742aa3d2571cf0dfa8b8103e36b5dcc` |
| MEL | normal | `MEL_INDEPENDENCE_WAVE_EMERGENCYX.tga` | `9f75c548585c948a31f4fae057f3c7a6d4caa6eaec13a8dd04cb12a5f738b30f` |
| MEL | normal | `MEL_INDEPENDENCE_WAVE_FORESTX.tga` | `fc7d5184b5cbab46b72c61935d33242d38ab0a0523aa3ac78a80307fbeb725ca` |
| MEL | normal | `MEL_INDEPENDENCE_WAVE_SOCIALISTX.tga` | `2041a658c6193c1223cccba9feae71d925d79c4679b310d4ed4be1b228e52fb2` |
| MEL | small | `MEL_INDEPENDENCE_WAVE_CIVICX.tga` | `2430f11f52de8c1d144caf98c18da2a1bb70ac1e550c879fee9290a354539371` |
| MEL | small | `MEL_INDEPENDENCE_WAVE_EMERGENCYX.tga` | `6f2a987311a526dd41a2047f589db43d8f02aec6f6c1ba50ab5a993ea26eae4e` |
| MEL | small | `MEL_INDEPENDENCE_WAVE_FORESTX.tga` | `037efae4f38db3694fa4dde2149164e5e6782026948e3345a5ca6127448e8557` |
| MEL | small | `MEL_INDEPENDENCE_WAVE_SOCIALISTX.tga` | `7216c8c155f216f1ac6ded8916b4ac164836c40f297e36dd27cb4cf1593fa0bb` |

## Validation and boundaries

The post-refresh QA compared all 24 runtime files against their package RGB sources and confirmed `24/24` header passes, `24/24` RGB-payload matches, and `24/24` opaque-alpha passes. The installed dimensions and exact lengths match the vanilla flag ladder contract.

No country history, `.gfx`, localisation, adapter, attestation, preflight, scenario, or Join files were changed by this refresh. BSK remains subject to its existing admitted-package evidence, while MEL remains package-local and fail-closed pending its separate anchor, portrait, flag-policy, FORM-12/13, and central-admission gates. Route-specific generated marks are not being presented as a neutral historical 1936 flag.

Future asset audits should compare the runtime TGA header and pixel payload against the package evidence rather than copying a 24-bit processed TGA directly into the engine-facing flag roots.
