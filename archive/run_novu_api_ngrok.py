import iterm2

async def main(connection):
    app = await iterm2.async_get_app(connection)

    # Create a new tab
    window = app.current_terminal_window
    if window is None:
        print("No current terminal window found. Creating a new one.")
        window = await app.async_create_window()
    tab = await window.async_create_tab()

    # Get the session
    session = tab.current_session

    # Run ngrok command
    await session.async_send_text("ngrok http http://localhost:3000\n")

iterm2.run_until_complete(main) 