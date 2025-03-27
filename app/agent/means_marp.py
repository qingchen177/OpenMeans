import time

from pydantic import Field

from app.agent.browser import BrowserAgent
from app.config import config
from app.prompt.browser import NEXT_STEP_PROMPT as BROWSER_NEXT_STEP_PROMPT
from app.prompt.means_marp import NEXT_STEP_PROMPT, SYSTEM_PROMPT, MARP_MARKDOWN_EXAMPLE
from app.tool import Terminate, ToolCollection
from app.tool.browser_use_tool import BrowserUseTool
from app.tool.marp_cli import MarpCLI
from app.tool.python_execute import PythonExecute
from app.tool.str_replace_editor import StrReplaceEditor


class MeansMarp(BrowserAgent):
    """
    在多功能通用代理基础上，加入了[Marp](https://marp.app/)一个Markdown演示生态系统
    在生成制作PPT、Markdown、PDF相关演示文稿的能力上有所增强
    """

    name: str = "MeansMarp"
    description: str = "一个精通Marp开源框架生态的专家代理。"

    system_prompt: str = SYSTEM_PROMPT.format(directory=config.workspace_root, example=MARP_MARKDOWN_EXAMPLE)
    next_step_prompt: str = NEXT_STEP_PROMPT

    max_observe: int = 10000
    max_steps: int = 20

    # Add general-purpose tools to the tool collection
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            PythonExecute(), BrowserUseTool(), StrReplaceEditor(), MarpCLI(), Terminate()
        )
    )

    async def think(self) -> bool:
        """Process current state and decide next actions with appropriate context."""
        # Store original prompt
        original_prompt = self.next_step_prompt

        # Only check recent messages (last 3) for browser activity
        recent_messages = self.memory.messages[-3:] if self.memory.messages else []
        browser_in_use = any(
            "browser_use" in msg.content.lower()
            for msg in recent_messages
            if hasattr(msg, "content") and isinstance(msg.content, str)
        )

        if browser_in_use:
            # Override with browser-specific prompt temporarily to get browser context
            self.next_step_prompt = BROWSER_NEXT_STEP_PROMPT

        # Call parent's think method
        result = await super().think()

        # Restore original prompt
        self.next_step_prompt = original_prompt

        return result
