import reflex as rx

config = rx.Config(
    app_name="Visual Direct Acyclic Graph Editor",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)