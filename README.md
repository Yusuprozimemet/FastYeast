
# The smallest bar plot indicates the fastest yeast.
## How to Use FastYeast?
### Setting Up Environment for Yeast Growth Rate Analysis

1. **Create a Project Directory**:
   - Create a dedicated folder for your yeast growth rate analysis project. Let's call it `fastyeast`.

2. **Navigate to Project Directory**:
   - Open a terminal or command prompt.
   - Change directory (`cd`) to your project folder:
     ```bash
     cd path/to/fastyeast
     ```

3. **Create a Virtual Environment** (Optional but Recommended):
   - It's a good practice to use virtual environments to isolate dependencies for different projects. Create a virtual environment named `venv` (you can choose a different name if you prefer):
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Required Packages**:
   - With the virtual environment activated, install the necessary packages using `pip`:
     ```bash
     pip install pandas matplotlib scikit-learn
     ```

   - This command will install `pandas` (for data manipulation), `matplotlib` (for plotting), and `scikit-learn` (for machine learning tools) within the virtual environment.

5. **Download and Save Your Data**:
   - Place your `file.csv` containing the yeast growth rate data into the `fastyeast` folder or any subfolder you prefer.

6. **Modify the Script**:
   - Open your Python script (`growth_analysis.py`) in a text editor.
   - Update the file path to point to your `file.csv` within your project directory:
     ```python
     file_path = 'path/to/your/file.csv'
     ```
   - Replace `'path/to/your/file.csv'` with the actual path to your CSV file relative to the `fastyeast` folder. For example:
     ```python
     file_path = 'data/file.csv'
     ```

7. **Run the Script**:
   - Ensure your virtual environment is activated.
   - Run the script using Python:
     ```bash
     python growth_analysis.py
     ```

8. **View and Interpret Results**:
   - The script will generate plots showing yeast growth curves and SVR analysis results based on your data. the smallest  
   - Use the plots and printed coefficients to interpret growth rates and analyze your data.

By following these steps, you create a well-organized environment for analyzing yeast growth rates with FastYeast, ensuring that dependencies are managed within the project folder. This approach enhances reproducibility and makes it easier to collaborate or share your project with others.
