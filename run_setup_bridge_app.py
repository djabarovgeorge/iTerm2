import iterm2

async def main(connection):
    app = await iterm2.async_get_app(connection)

    # Create a new tab
    window = app.current_terminal_window
    if window is None:
        print("No current terminal window found. Creating a new one.")
        window = await app.async_create_window()
    tab = await window.async_create_tab()
    session = tab.current_session
    pane1 = session
    pane2 = await pane1.async_split_pane()
    pane3 = await pane2.async_split_pane(vertical=True)


    await pane1.async_send_text("cd ~/projects/main/novu\n")
    await pane1.async_send_text("pnpm start:web\n")
    
    
    await pane2.async_send_text("cd ~/projects/main/bridge-app\n")
    await pane2.async_send_text("npm run dev\n")

    await pane3.async_send_text("npx novu@latest dev --port 4000 -d http://localhost:4200\n")

iterm2.run_until_complete(main) 