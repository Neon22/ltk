# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import ltk

def create():
    def handler(item):
        ltk.LI(
            ltk.Italic(f"Selected menu item: {item.label}")
                .css("margin", 10)
        ).appendTo(ltk.find("#app-feedback"))

    left_css = {
        "border-right": "2px solid lightgray",
        "padding": "50px 20px",
        "background-color": "lightyellow",
        "width": "20%",
    }

    right_css = {
        "padding": 0,
        "background-color": "lightgreen",
        "width": "80%",
    }

    return (
        ltk.VBox(
            ltk.MenuBar(
                ltk.Menu("File",
                    ltk.MenuItem("➕", "New", "", handler),
                    ltk.MenuItem("📂", "Open", "Cmd+O", handler)),
                ltk.Menu("Edit",
                    ltk.MenuItem("✂️", "Copy", "Cmd+C", handler),
                    ltk.MenuItem("📋", "Paste", "Cmd+V", handler)),
            ).css("background-color", "lightblue"),
            ltk.HBox(
                ltk.VBox(
                    ltk.Text("Left Panel"),
                    left_css),
                ltk.VBox(
                    ltk.Text("Right Panel")
                        .css("margin-bottom", 20),
                    ltk.H3("Select a menu item from the blue bar shown above, or press it's shortcut on your keyboard"),
                    ltk.UL().attr("id", "app-feedback"),
                    right_css)
            ).css("height", "100%")
        )
        .css("height", "100%")
        .attr("name", "Application"))