# Create a Python development environment

To get started working on your package you will want to create a
shiny new Python environment. While this is not required, we strongly
encourage you to create an environment that is dedicated to your Python
package.

Below you learn how to create an environment using both:

- venv - which is the environment manager that comes with Python
- conda - an environment manager that is tailored to the scientific ecosystem.

There is no right or wrong environment option. Chose the option that you prefer.

:::{tip}
If you are a scientist and you work with spatial data or are creating a package that is not pure python, you may prefer conda. But in general pick
the environment tool that works best for you.
:::

## Create a package development environment Using venv

venv comes with any Python installation. Thus, you may find it easy to
use it for your package development needs. Instructions on how to create a
new development environment using venv are below.

1. **Open Terminal or Command Prompt:**

   - Open your terminal or command prompt.

2. **Navigate to the Project Directory:**

   ```bash
   cd path/to/your/project-directory
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv pyos-dev
   ```

4. **Activate the Virtual Environment:**

   - **On Windows:**

   ```bash
   pyos-dev\Scripts\activate
   ```

   - **On macOS/Linux:**

   ```bash
   source pyos-dev/bin/activate
   ```

5. **Install/Manage Dependencies:**

   ```bash
   pip install package_name
   ```

6. **Work on Your Project:**

7. **Deactivate the Virtual Environment:**
   ```bash
   deactivate
   ```

### Additional Notes:

- Remember to reactivate the environment each time you want to work on your project.
- To delete the virtual environment, delete the `pyos-dev` folder.

## Creating a PyOS-Dev Environment Using Conda

Some scientists prefer to use a conda environment for their package development. If that is your preference, follow the steps below.

1. **Create an Environment File (`env.yml`):**

   - Use a text editor to create a file named `env.yml` and specify the required packages in the YAML format. For instance:

   ```yaml
   name: pyos-dev
   channels:
     - defaults
   dependencies:
     - python=3.8
     - package_name1
     - package_name2
     # Add other necessary packages
   ```

2. **Create the Conda Environment from the Environment File:**

   - Open your terminal or command prompt.

   ```bash
   conda env create -f env.yml
   ```

   This command will read the `env.yml` file and create a Conda environment named `pyos-dev` with the specified packages.

3. **Activate the Conda Environment:**

   - Once the environment is created, activate it.
   - **On Windows:**

   ```bash
   conda activate pyos-dev
   ```

   - **On macOS/Linux:**

   ```bash
   source activate pyos-dev
   ```

4. **Work on Your Project:**
   - You're now working in the `pyos-dev` Conda environment.

### Additional Notes:

- Remember to activate the environment each time you want to work on your project.
- To deactivate the environment, use `conda deactivate`.
- To delete the environment, you can use `conda env remove -n pyos-dev`.
