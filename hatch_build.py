from pathlib import Path
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        assert self.target_name == "wheel", self.target_name
        build_data["pure_python"] = False
        build_data["infer_tag"] = True

        # copy lib tree
        src_dir = Path("rtree")
        if (src_lib := src_dir / "lib").is_dir():
            build_data["artifacts"].extend(str(pth) for pth in src_lib.rglob("*"))

        # copy include tree
        if (src_include := src_dir / "include").is_dir():
            build_data["artifacts"].extend(str(pth) for pth in src_include.rglob("*"))
