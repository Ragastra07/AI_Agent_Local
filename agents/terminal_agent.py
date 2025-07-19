class TerminalAgent:
    def __init__(self):
        pass

    def run_command(self, command: str):
        import subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
