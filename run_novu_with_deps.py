import iterm2

async def main(connection):
    app = await iterm2.async_get_app(connection)

    # Create a new tab
    window = app.current_terminal_window
    if window is None:
        print("No current terminal window found. Creating a new one.")
        window = await app.async_create_window()
    tab = await window.async_create_tab()
    await tab.async_set_title("Novu Services With Dependencies")

    # Navigate to the project directory
    session = tab.current_session

    paneHorizontal = session

    # todo rename to servicePanel
    servicePanel1 = await paneHorizontal.async_split_pane()


    depPanel1 = paneHorizontal
    await depPanel1.async_send_text("cd ~/projects/main/novu\n")
    await depPanel1.async_send_text("pnpm --filter @novu/application-generic watch:build\n")
    
    depPanel2 = await depPanel1.async_split_pane(vertical=True)
    await depPanel2.async_send_text("cd ~/projects/main/novu\n")
    await depPanel2.async_send_text("pnpm --filter @novu/dal build:watch\n")

    depPanel3 = await depPanel2.async_split_pane(vertical=True)
    await depPanel3.async_send_text("cd ~/projects/main/novu\n")
    await depPanel3.async_send_text("pnpm --filter @novu/shared build:watch\n")

    depPanel4 = await depPanel3.async_split_pane(vertical=True)
    await depPanel4.async_send_text("ngrok http http://localhost:3000\n")




    await servicePanel1.async_send_text("cd ~/projects/main/novu\n")
    await servicePanel1.async_send_text("pnpm --filter @novu/api-service start\n")

    servicePanel2 = await servicePanel1.async_split_pane(vertical=True)
    await servicePanel2.async_send_text("cd ~/projects/main/novu\n")
    await servicePanel2.async_send_text("pnpm --filter @novu/worker start\n")

    servicePanel3 = await servicePanel2.async_split_pane(vertical=True)
    await servicePanel3.async_send_text("cd ~/projects/main/novu\n")
    await servicePanel3.async_send_text("pnpm --filter @novu/dashboard start\n")

iterm2.run_until_complete(main)
