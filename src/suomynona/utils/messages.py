import hikari

from suomynona import config


def build_response(
    content: str,
    title: str | None = None,
    footer: str | None = None,
    accent_colour: hikari.Colour = config.DEFAULT_COLOUR,
) -> list[hikari.api.ComponentBuilder]:
    """Creates a nicely formatted message using Discord's Components V2"""

    container = hikari.impl.ContainerComponentBuilder(accent_color=accent_colour)

    if title is not None:
        container.add_text_display(f"### {title}")
        container.add_separator(divider=True)

    container.add_text_display(content)

    if footer is not None:
        container.add_separator(divider=True)
        container.add_text_display(f"-# {footer}")

    return [container]
