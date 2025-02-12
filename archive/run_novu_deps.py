import iterm2

async def main(connection):
    app = await iterm2.async_get_app(connection)

    # Create a new tab
    window = app.current_terminal_window
    if window is None:
        print("No current terminal window found. Creating a new one.")
        window = await app.async_create_window()
    tab = await window.async_create_tab()
    await tab.async_set_title("Novu Dependencies")

    # Navigate to the project directory
    session = tab.current_session

    paneHorizontal = session

    depPanel1 = paneHorizontal
    await depPanel1.async_send_text("cd ~/projects/main/novu/libs/application-generic\n")
    await depPanel1.async_send_text("pnpm watch:build\n")
    
    depPanel2 = await depPanel1.async_split_pane(vertical=True)
    await depPanel2.async_send_text("cd ~/projects/main/novu/libs/dal\n")
    await depPanel2.async_send_text("pnpm build:watch\n")

    depPanel3 = await depPanel2.async_split_pane(vertical=True)
    await depPanel3.async_send_text("cd ~/projects/main/novu/packages/shared\n")
    await depPanel3.async_send_text("pnpm build:watch\n")

    depPanel4 = await depPanel3.async_split_pane(vertical=True)
    await depPanel4.async_send_text("ngrok http http://localhost:3000\n")

iterm2.run_until_complete(main)
