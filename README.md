# DreamX Studio profile

GitHub displays [profile/README.md](profile/README.md) on the [studio overview](https://github.com/DreamX-Studio). This repository holds the public introduction and brand artwork.

- [Profile design notes](docs/design-notes.md)
- [Artwork and provenance](assets/README.md)
- [Studio workspace and project directory (team access)](https://github.com/DreamX-Studio/dx-studio)

## Maintaining the profile

Update the public catalogue when the studio announces a title, a release or a change in project status. Confirm wording with the project owner. The team maintains setup instructions and the repository directory in the private workspace. The public profile links to that workspace once and labels the access requirement.

Use the generic title for the Godot game until its public name is announced. Describe DX Relay only as an internal studio project. Keep private repository metadata, source, technical details and internal handoffs out of public summaries.

After changing the banner composition, run `python3 scripts/build_assets.py`. Check the rendered profile in light and dark themes, at desktop and phone widths. Verify that the banner and project icons load and that the team link points to the studio workspace.
