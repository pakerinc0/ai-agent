import platform
import os
import shutil

from app.tools.base import Tool
from app.models.schemas import ToolResult



class SystemTool(Tool):

    name = "system_info"


    async def execute(self, **kwargs):

        disk = shutil.disk_usage("/")


        return ToolResult(

            success=True,

            data={

                "system": platform.system(),

                "hostname": platform.node(),

                "cpu_count": os.cpu_count(),

                "disk_total_gb":
                    round(disk.total / (1024**3),2),

                "disk_free_gb":
                    round(disk.free / (1024**3),2)

            }

        )
