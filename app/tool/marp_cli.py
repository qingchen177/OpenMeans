# @Author  : qingchen
# @Time    : 2025/3/26 下午5:53
import asyncio
import os

from app.config import WORKSPACE_ROOT
from app.tool.base import BaseTool, CLIResult

from app.tool.terminal import Terminal

# TEMP：marp-cli tool

_MARP_CLI_DESCRIPTION = """A CLI interface for Marp, the Markdown presentation tool.It can convert Marp / Marpit Markdown files into static HTML / CSS, PDF, PowerPoint document, and image(s) easily."""
MARP_TYPE = ["html", "pdf", "pptx"]
TIMEOUT = 60


class MarpCLI(BaseTool):
    name: str = "Marp_CLI"
    description: str = _MARP_CLI_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "md_file_path": {
                "type": "string",
                "description": "The Markdown file path.",
            },
            "type": {
                "type": "string",
                "description": "The type of output file. Can be 'html', 'pdf', 'pptx'.",
                "enum": ["html", "pdf", "pptx"],
            },
        },
        "required": ["md_file_path", "type"],
    }

    async def execute(self, md_file_path: str, type: str) -> CLIResult:
        """execute marp-cli command"""
        final_output = CLIResult(output="", error="")
        # Place the generated file in the workspace directory
        if os.path.isabs(md_file_path):
            file_name = os.path.basename(md_file_path)
            full_path = os.path.join(WORKSPACE_ROOT, file_name)
        else:
            full_path = os.path.join(WORKSPACE_ROOT, md_file_path)

        # Ensure the directory exists
        if not os.path.exists(full_path):
            final_output.error += f"Marp-CLI error：markdown file: {full_path} not exist！"
            return final_output

        # Execute the marp-cli command
        if type in MARP_TYPE:
            # command = ["npx", "marp", "--no-stdin", f"--{type}", full_path]
            command = f'npx marp --no-stdin --{type} {full_path}'
            return await Terminal().execute(command=command)
        else:
            final_output.error += f"Marp-CLI Unsupported type: {type}"

        # Remove trailing newlines
        final_output.output = final_output.output.rstrip()
        final_output.error = final_output.error.rstrip()
        return final_output


if __name__ == "__main__":
    marp = MarpCLI()
    rst = asyncio.run(marp.execute("test.md", "pptx"))
    print(rst)
