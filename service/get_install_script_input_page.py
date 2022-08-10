import uuid

from data.InstallScriptInputData import ScriptInputData


class InstallScriptService:
    uuid = []

    def get_install_script_input(self):
        return {"1"}

    def generate_install_script(self, data: ScriptInputData):
        return {"2"}

    def generate_uuid(self):
        self.uuid.append(uuid.uuid4())
        return {self.uuid[-1]}
