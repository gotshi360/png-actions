import anchorpoint as ap

ctx = ap.get_context()
ui = ap.UI()
path = ctx.path

# Defines and shows the pages dialog
def show_dialog():
    dialog = ap.Dialog()
    dialog.title = "Maintenance Notice"
    dialog.icon = ctx.icon
    dialog.add_text("GITEA is currently unavailable due to ongoing maintenance, which temporarily disables file access via Anchorpoint.")
    dialog.add_text("Please refrain from syncing in Anchorpoint until the maintenance is complete.")
    dialog.add_info("You may continue working on your local files, but avoid pushing any changes to the server during this period.")
    dialog.add_text(" ")
    dialog.add_text("Thank you for your patience.")
    dialog.add_info("Play'n GO Anchorpoint Support")
    dialog.show()


show_dialog()

