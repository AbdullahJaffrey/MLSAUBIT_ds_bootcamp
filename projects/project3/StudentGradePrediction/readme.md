# Student Grade Prediction Model

## Overview
This Jupyter Notebook (`StudentGradePrediction.ipynb`) implements a predictive model for student grades using Decision Tree and Logistic Regression algorithms. The model is trained on a cleaned dataset (`Cleaned_student_data.csv`). The training data used for the model is stored in the file `Train_student_data.csv`.

## Dataset
The cleaned dataset (`Cleaned_student_data.csv`) includes various features related to students' personal and academic information. The training data used for the model is stored in the file `Train_student_data.csv`.

### Features in Cleaned_student_data.csv
- **School**: Student's school (binary: 'GP' for Gabriel Pereira or 'MS' for Mousinho da Silveira)
- **Sex**: Student's gender (binary: 'F' for female or 'M' for male)
- **Age**: Student's age (numeric: from 15 to 22)
- **Studytime**: Weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
- **Paid**: Extra paid classes within the course subject (Math or Portuguese) (binary: 'yes' or 'no')
- **Activities**: Extra-curricular activities (binary: 'yes' or 'no')
- **Nursery**: Attended nursery school (binary: 'yes' or 'no')
- **Higher**: Wants to take higher education (binary: 'yes' or 'no')
- **Internet**: Internet access at home (binary: 'yes' or 'no')
- **Freetime**: Free time after school (numeric: from 1 - very low to 5 - very high)
- **Health**: Current health status (numeric: from 1 - very bad to 5 - very good)
- **Absences**: Number of school absences (numeric: from 0 to 93)
- **G1**: First period grade (numeric: from 0 to 20)
- **G2**: Second period grade (numeric: from 0 to 20)
- **G3**: Final grade (numeric: from 0 to 20)
- **Attendanceinpercentage**: Attendance percentage based on absences
- **Total**: Total of G1, G2, and G3
- **Percentage**: Percentage calculated from Total
- **Grade**: Final grade category (e.g., 'A+', 'B', 'C', 'Fail', etc.)

## Files
- `StudentGradePrediction.ipynb`: Jupyter Notebook containing the implementation of the Decision Tree and Logistic Regression models.
- `Cleaned_student_data.csv`: Cleaned dataset used for training and testing the models.
- `Train_student_data.csv`: Training data used for model training.

## GitHub Folder
The project files are available in the following GitHub folder:
[MLSAUBIT_ds_bootcamp - Project 3](https://github.com/AbdullahJaffrey/MLSAUBIT_ds_bootcamp/tree/main/projects/project3/StudentGradePrediction)

## Instructions
1. Clone the repository: `git clone https://github.com/AbdullahJaffrey/MLSAUBIT_ds_bootcamp.git`
2. Navigate to the project folder: `cd MLSAUBIT_ds_bootcamp/projects/project3/StudentGradePrediction`
3. Open and run the Jupyter Notebook `StudentGradePrediction.ipynb` to explore the models and predictions.

Feel free to modify the code or dataset as needed. If you have any questions or encounter issues, please open an [issue](https://github.com/AbdullahJaffrey/MLSAUBIT_ds_bootcamp/issues).

Happy exploring!
