# {{cookiecutter.name}}


## Requirements

* Python {{cookiecutter.python_version}}


## Environment variables


## Releasing a new version to GitLab PyPi

Publishing a new version to GitLab PyPi registry is done manually according to [this instruction](https://docs.gitlab.com/ee/user/packages/pypi_repository/#authenticate-with-a-personal-access-token)

Steps for manual publishing:
1. Update the version in [{{cookiecutter.name}}.__version__.py][{{cookiecutter.name}}.__version__.py] before publishing.

2. Build the package:
   ```bash
   python setup.py sdist bdist_wheel
   ```

3. In order to publish the package, the [Twine](https://pypi.or/project/twine/) tool is used. It uploads packages on PyPi or other repositories. Install Twine:
   ```bash
   pip install twine
   ```

4. [Authenticate with the Package Registry](https://docs.gitlab.com/ee/user/packages/pypi_repository/#authenticate-with-the-package-registry). Create a file `~/.pypirc`. This file is used to add more repositories to Twine. By default Twine upload packages on PyPi, but in this case the package have to be uploaded on Gitlab PyPi. To achieve the file `~/.pypirc` with the following have to be created:
   ```
   [distutils]
   index-servers =
       {{cookiecutter.name}}-index

   [{{cookiecutter.name}}-index]
       repository = https://gitlab.com/api/v4/projects/<project_id>/packages/pypi
       username = __token__
       password = <your personal access token>
   ```
   Where <project_id> can be found on the home page of the project, or in *Settings > General*. To create a personal access token follow [this guide](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html). The personal access token needs the `api` access.

4. [Publish a PyPI package by using twine](https://docs.gitlab.com/ee/user/packages/pypi_repository/#publish-a-pypi-package-by-using-twine):
   ```bash
   python -m twine upload --repository {{cookiecutter.name}}-index dist/{{cookiecutter.name}}-<version>*
   ```
   To view the published package, go to project’s *Packages & Registries* page.


## Usage

1. Generate a [GitLab Personal Access Token][https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html] with `read_api` access.

2. Install the package using `pip`:
   ```bash
   pip install {{cookiecutter.name}} --extra-index-url https://__token__:<your_personal_token>@gitlab.com/api/v4/projects/<project_id>/packages/pypi/simple
   ```

   or in `Pipfile`:
   ```
   [[source]]
   url = "https://__token__:<your_personal_token>@gitlab.com/api/v4/projects/<project_id>/packages/pypi/simple"
   verify_ssl = true
   name = "{{cookiecutter.name}}-gitlab-pypi"

   [packages]
   {{cookiecutter.name}} = {version = "*", index = "{{cookiecutter.name}}-gitlab-pypi"}
   ```


## Development

1. Clone the code with `git clone project/repository/on/git-lab` and `cd` to the directory of the cloned project.

2. Do changes.

3. Run tests (to build and test the package, [tox](https://tox.readthedocs.io/en/latest/) was used, as recommended in the [pytest documentation](https://docs.pytest.org/en/stable/goodpractices.html#tox)):
   ```bash
   tox
   ```

   In case if dependency packages were modified, the virtual environment used by tox has to be rebuild. To do so, run:
   ```bash
   tox -r
   ```

   To run only [specific tox environment](https://tox.readthedocs.io/en/latest/example/general.html#selecting-one-or-more-environments-to-run-tests-against), use:
   ```bash
   tox -e env_name
   ```

   the list of environments definition can be found in [tox.ini](tox.ini) file. For example to tun black formatting, use:
   ```bash
   tox -e format
   ```

4. If all tests are successfully passed, create a MR.


## How to run

1. Clone the code with `git clone project/repository/on/git-lab` and `cd` to the directory of the cloned project.

2. It's strongly recommended to [create a virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) for installing the package and it's dependencies, and activate it before going to next step.

3. Install the package:
   ```bash
   pip install -e .
   ```
   which will install the package in the [development mode](https://packaging.python.org/guides/distributing-packages-using-setuptools/#working-in-development-mode) along with all required dependencies (specified in [setup.py](setup.py)) to run the code. 

   
4. Call `python run.py 1`, where `1` is an argument for the ``run.py`` script. To see what options can be passed to `run.py`, use `python run.py --help`.


## Links

* [Packaging and distributing projects](https://packaging.python.org/guides/distributing-packages-using-setuptools)
* [tox configuration specification](https://tox.readthedocs.io/en/latest/config.html)
