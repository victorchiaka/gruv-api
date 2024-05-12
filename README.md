# gruv api
The api for the music streaming app `Gruv` More like `Groov`

### Basic project structure

<strong>src/</strong> This folder holds the actual source code for the api and it's splitted into the following layers
- `routes/` : This is where all the api requests are served, we're using the REST.
- `services/` : Files in this folder serves as the bridge between the routes and the database layer, probably in the `models/` folder
- `models/` : The files here contains the database models and Entities
- `utils/` : This folder holds utitlity files and modules
- `configs/` : Any configuration will go here (Can be taken down anytime depending on how the project is later structured in the future)


<hr />
<strong>test/</strong> This folder contains the tests, integration tests for now using pytest as the test framework (We can change this later)

<hr>
This is the base settings of the project, modifications will be made as the project grows larger

<hr>

<strong>To kick off and contribute to the project</strong>


Run the following commands:
- `python -m venv .venv`
- `pip install -r requirements.txt`

<strong>Make sure you have python 3.x installed</strong>

After working locally and you're sure the tests pass and nothing breaks, run the command  `pip freeze > requirements.txt`to freeze whatever package you installed to while working locally so other developers can use it.

