## Setup
Clone this project onto a local machine that will act as the server.

From within the parent directory of where this code ended up, run `py -m venv env`. You should end up with a structure like the following:

```
env/
├─ Include/
├─ Lib/
├─ Scripts/
├─ .gitignore
├─ pyvenv.cfg
mc_api/
├─ mc_api/
├─ recipes/
├─ .gitignore
├─ db.sqlite3
├─ manage.py
├─ README.md
├─ requirements.txt
├─ sample-endpoints.postman_collection.json
```

CD into the outer `mc_api/` directory, so you're in the folder with `requirements.txt`, `manage.py`, and this README.

Run the following to activate the virtual environment and install the project dependencies:
```sh
..\env\Scripts\activate
pip install -r requirements.txt
```

## Run
Run the following command to start the API server:
```sh
py manage.py runserver 192.168.91.1:80    # Use host's IP instead. Keep port 80.
```

## Usage notes
### PATCH requests

PATCH requests must end in a trailing slash! E.g.,
"http://127.0.0.1:8000/recipes/4415/".
An error will be thrown if the slash is missing. It may be absent on GET requests, however.

To make a PATCH request in Postman, go to Body -> Raw and type something like this (must use double quotes!):
```json
{
    "img_link": "https://www.minecraft-crafting.net/app/src/Other/craft/craft_flowerpot.png"
}
```