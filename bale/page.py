import logging

from nicegui import Client, app, ui  # type: ignore

from bale import elements as el
from bale.content import Content
from bale.drawer import Drawer
from bale.interfaces import cli

logger = logging.getLogger(__name__)


def build():
    @ui.page("/", response_timeout=30)
    async def index(client: Client) -> None:
        app.add_static_files("/static", "static")
        el.load_element_css()
        cli.load_terminal_css()
        ui.colors(
            primary=el.primary,
            secondary=el.primary,
            accent=el.primary,
            dark=el.dark,
            positive="#50FA7B",
            negative="#FF5555",
            info="#8BE9FD",
            warning="#F1FA8C",
        )
        column = ui.column()
        content = Content()
        drawer = Drawer(column, content.host_selected, content.hide)
        drawer.build()
        await content.build()
