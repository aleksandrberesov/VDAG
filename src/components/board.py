import reflex as rx

class boardState(rx.State):
    Title: str = "Board"

def board() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading(rx.text(boardState.Title), size="1"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )