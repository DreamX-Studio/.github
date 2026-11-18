# Artwork

The DreamX symbol and custom vector lettering are reused from the studio's
existing brand assets. Original files in [brand/](brand/) are copied unchanged;
[provenance.json](brand/provenance.json) records their source paths and hashes.

The header is a new SVG composition of that artwork, not a replacement logo.
It uses a restrained surface, outlined wordmark and an original geometric
illustration. Light/dark versions scale within the same responsive layout.
The three small project-category illustrations are original SVG line art.

Build with [scripts/build_assets.py](../scripts/build_assets.py), using only
Python's standard library. SVGs embed the existing PNG symbol; remaining shapes
are vector paths. Labels use a system sans-serif stack with no font downloads.
No graphics or brand assets were copied from the reference organizations.
