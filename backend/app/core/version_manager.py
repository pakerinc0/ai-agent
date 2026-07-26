import os
import shutil
from datetime import datetime



class VersionManager:


    def __init__(
            self,
            base_path="projects"
    ):

        self.base_path = base_path


        os.makedirs(
            self.base_path,
            exist_ok=True
        )





    def create_project(
            self,
            project_name
    ):


        path = os.path.join(
            self.base_path,
            project_name
        )


        os.makedirs(
            path,
            exist_ok=True
        )


        versions = os.path.join(
            path,
            "versions"
        )


        os.makedirs(
            versions,
            exist_ok=True
        )


        return path





    def save_version(
            self,
            project_name,
            filename,
            content
    ):


        project_path = self.create_project(
            project_name
        )


        versions_path = os.path.join(
            project_path,
            "versions"
        )


        existing = os.listdir(
            versions_path
        )


        version_number = len(existing) + 1


        version_dir = os.path.join(
            versions_path,
            f"v{version_number}"
        )


        os.makedirs(
            version_dir,
            exist_ok=True
        )


        file_path = os.path.join(
            version_dir,
            filename
        )


        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                content
            )


        return {

            "version":
                f"v{version_number}",

            "path":
                file_path

        }





    def set_best(
            self,
            project_name,
            version
    ):


        project_path = os.path.join(
            self.base_path,
            project_name
        )


        source = os.path.join(
            project_path,
            "versions",
            version
        )


        best = os.path.join(
            project_path,
            "best"
        )


        if os.path.exists(best):

            shutil.rmtree(
                best
            )


        shutil.copytree(
            source,
            best
        )


        return {

            "status":
                "best version updated",

            "version":
                version

        }





    def list_versions(
            self,
            project_name
    ):


        path = os.path.join(
            self.base_path,
            project_name,
            "versions"
        )


        if not os.path.exists(path):

            return []


        return sorted(
            os.listdir(path)
        )
