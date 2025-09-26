"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(rx.text("Welcome to ", rx.code(f"{config.app_name}")), size="9"),
            spacing="5",
            justify="start",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
