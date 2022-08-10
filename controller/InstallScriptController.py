from fastapi import Depends, FastAPI, Query, Path
import consts
from fastapi_utils.inferring_router import InferringRouter
from typing import Optional

from data import InstallScriptInputData
from data.InstallScriptInputData import ScriptInputData
from fasad.InstallScriptFasade import InstallScriptFasade
from fasadImpl.InstallScriptFasadeImpl import InstallScriptFasadeImpl


class InstallScriptController:
    uri = "/RestService/InstallScript"
    endpoint = ""
    app = consts.app
    install_script_fasade = InstallScriptFasadeImpl()


    def __init__(self, url: str):
        self.url = url
        self.endpoint = self.url + self.uri

    @app.get(endpoint)
    def get_script_page(self):
        return {"Data": "get_script_page"}

    @app.get(endpoint + "/{itemId}")
    def get_by_id(self, item_id: int = Path(None, description="The Id we would like to have", gt=0, lt=2)):
        return {"Data": "get_by_id"}

    @app.get(endpoint + "/getByName")
    def get_by_name(self, name: str = Query(None, title="Name", description="The Id we would like to have")):
        return {"Data": "get_by_name"}

    @app.post(endpoint + "/generateScript")
    def get_script_page(self, script_data: ScriptInputData):
        return self.install_script_fasade.generate_install_scripts_input_page(script_data)
