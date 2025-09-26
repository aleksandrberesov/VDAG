import reflex as rx

from rxconfig import config

class State(rx.State):
    welcomeTitle: str = f"Welcome to {config.app_name}"

def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(rx.text(State.welcomeTitle), size="2"),
            spacing="5",
            justify="start",
            min_height="85vh",
        ),
    )

