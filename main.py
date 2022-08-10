import uvicorn

from fastapi import FastAPI

app = FastAPI()
from fastapi import  Query, Path


from data.InstallScriptInputData import ScriptInputData

from fasadImpl.InstallScriptFasadeImpl import InstallScriptFasadeImpl

uri = "/RestService/InstallScript"
install_script_fasade = InstallScriptFasadeImpl()


@app.get(uri)
def get_script_page():
    return {"Data": "get_script_page"}


@app.get(uri + "/{itemId}")
def get_by_id(item_id: int = Path(None, description="The Id we would like to have", gt=0, lt=2)):
    return {"Data": "get_by_id"}


@app.get(uri + "/getByName")
def get_by_name( name: str = Query(None, title="Name", description="The Id we would like to have")):
    return {"Data": "get_by_name"}


@app.post(uri + "/generateScript")
def get_script_page( script_data: ScriptInputData):
    return install_script_fasade.generate_install_scripts_input_page(script_data)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host="localhost",
        port=8088,
        timeout_keep_alive=3600
    )


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

