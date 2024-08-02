# [FiQuS/Pancake3D](https://doi.org/10.1088/1361-6668/ad3f83) Example

This is a transient magneto-thermal quench simulation of a no-insulation HTS pancake coil with FiQuS/Pancake3D, developed at CERN.

The simulation setup is described in the [`HTSPancakeCoil_FiQuS.yaml`](https://github.com/sinaatalay/fiqus-pancake3d-example/blob/main/HTSPancakeCoil_FiQuS.yaml) file. Make sure to use VS Code and download the [YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) for schema support (auto-completion, validation, hover information, etc.).

There are two ways of running the simulation: locally or with GitHub Codespaces.

## Run Locally

1. Install Python 3.11.
2. Clone the repository.
    ```
    git clone --recursive https://github.com/sinaatalay/fiqus-pancake3d-example.git
    ```
3. Install the requirements (consider using a virtual environment).
    ```
    pip install -r requirements.txt
    ```
4. Run the `run_fiqus.py` file to run the simulation.
    ```
    python run_fiqus.py
    ```

## Run with GitHub Codespaces

You don't have to install anything to run it with GitHub Codespaces.

1.  [Fork](https://github.com/sinaatalay/fiqus-pancake3d-example/fork) the repository.
2.  Navigate to the forked repository.
3.  Click the <> **Code** button, then click the **Codespaces** tab, and then click **Create codespace on main**.

    [Visual Studio Code for the Web](https://code.visualstudio.com/docs/editor/vscode-web) will be opened with a ready-to-use development environment.

4.  Press **F5** to run the simulation.

This is done with [Development containers](https://containers.dev/), and the environment is defined in the [`.devcontainer/devcontainer.json`](https://github.com/sinaatalay/fiqus-pancake3d-example/blob/main/.devcontainer/devcontainer.json) file. Dev containers can also be run locally using various [supporting tools and editors](https://containers.dev/supporting).
