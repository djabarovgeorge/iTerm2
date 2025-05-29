import asyncio
import iterm2

async def shutdown_panes(connection):
    try:
        app = await iterm2.async_get_app(connection)
        current_window = app.current_terminal_window

        if not current_window:
            print("No active iTerm2 window found.")
            return

        panes = []
        for tab in current_window.tabs:
            for session in tab.sessions:
                panes.append(session)

        print(f"Found {len(panes)} panes. Attempting graceful shutdown...")

        for pane in panes:
            try:
                await pane.async_send_text("\x03")  # Equivalent to Command + C
                await asyncio.sleep(1)  # Wait for the process to respond
            except Exception as e:
                print(f"Failed to gracefully shut down pane {pane.name}: {e}")

        print("All panes processed. Closing window...")
        await current_window.async_close()

    except Exception as main_e:
        print(f"An error occurred: {main_e}")

if __name__ == "__main__":
    asyncio.run(iterm2.Connection.async_create("", shutdown_panes))
