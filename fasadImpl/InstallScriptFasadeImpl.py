from data.InstallScriptInputData import ScriptInputData
from fasad.InstallScriptFasade import InstallScriptFasade
from service.get_install_script_input_page import InstallScriptService


class InstallScriptFasadeImpl(InstallScriptFasade):
    install_script_service = InstallScriptService();

    def get_install_scripts_input_page(self):
        return s.get_install_script_input()

    def generate_install_scripts_input_page(self, data: ScriptInputData):
        return self.install_script_service.generate_install_script()
