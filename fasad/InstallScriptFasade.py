from abc import ABC, abstractmethod

from data.InstallScriptInputData import ScriptInputData


class InstallScriptFasade(ABC):
    @abstractmethod
    def get_install_scripts_input_page(self):
        pass

    def generate_install_scripts_input_page(self, data: ScriptInputData):
        pass
