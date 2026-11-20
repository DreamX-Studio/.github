# Profile design notes

The organization overview introduces the studio and its public-facing projects.
Members enter the private workspace through a single team-labelled link.

## Community references

- [Catppuccin](https://github.com/catppuccin/.github/blob/main/profile/README.md):
  consistent identity and theme-aware imagery. We adopted the consistency and
  light/dark treatment, without a wall of badges or social icons.
- [Evil Martians](https://github.com/evilmartians): a short introduction followed
  by a concrete product catalogue. Each project here gets a distinct purpose.
- [BeamNG](https://github.com/BeamNG/.github/blob/main/profile/README.md): a game
  studio's tools and integrations presented with explicit status. We keep the
  catalogue compact and use one column so it reads on mobile.
- [Tauri](https://github.com/tauri-apps/.github): a strong header with very few
  navigation choices. The DreamX composition uses its own existing artwork.
- [GitHub documentation](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile):
  public/member visibility and the profile/README.md entry point.

## Presentation decisions

- One brand header; real text for the project descriptions and status.
- A single-column catalogue rather than tiny three-column cards.
- Existing DreamX symbol and lettering; no invented game logo or screenshot.
- Two light/dark images that scale cleanly; no animation or flashing. GitHub's
  themed-picture element rewrites color media conditions, so viewport conditions
  are not combined with them. Smaller displays use the same readable composition.
- No visitor counters, contribution snakes, trophy walls, fake metrics,
  decorative technology stacks, empty social links or claims of production readiness.
- The Godot project is described generically until its title is announced.
- DX MOP is described as a Linux pilot. Project-specific source links live in the team directory.
- DX Relay is named only as an internal studio project. Its purpose, technology,
  architecture and implementation status are intentionally omitted.
- Public summaries contain no private source, account information, raw logs,
  benchmark details or internal acceptance documents.

Project owners confirm changes to public descriptions. Keep dates for dated
announcements. Internal repository additions only require an update to the
private directory unless the studio also announces a public project.
