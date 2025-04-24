import iterm2

async def main(connection):
    app = await iterm2.async_get_app(connection)

    # Create a new tab
    window = app.current_terminal_window
    if window is None:
        print("No current terminal window found. Creating a new one.")
        window = await app.async_create_window()
    tab = await window.async_create_tab()
    await tab.async_set_title("Novu App-Gen")

    # Navigate to the project directory
    session = tab.current_session

    await session.async_send_text("cd ~/projects/main/novu\n")
    await session.async_send_text("pnpm --filter @novu/application-generic watch:build\n")

iterm2.run_until_complete(main)
