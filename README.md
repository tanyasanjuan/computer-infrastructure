# Computer Infrastructure
This repository contains the assessment solutions for the Computer Infrastructure module. It consists of creating a programme in Python and yFinance package to automatically download and display hourly stock market data for the five FAANG companies: META, AAPL, AMZN, NFLX, and GOOG. The  `get_data()` function downloads hourly price data for the last five days and saves it to the `data/` folder with a timestamp-based filename in the format YYYYMMDD-HHmmss.csv. The function also creates the folder if it doesn't exist.

The `plot_data()` function loads the most recent CSV file into the `data` folder and creates a chart showing the closing prices of the five stocks. The chart includes axis labels, a legend, and the date as the title. The chart is saved in the `plots` folder with the same timestamp format (YYYYMMDD-HHmmss.png), and the folder is created if it doesn't exist.
This repository also includes a separate script, `faang.py`, designed to automatically run both functions from the terminal writing (`./faang.py`). It includes a shebang line to execute.ute.

Finally, a GitHub Actions workflow (.github/workflows/faang.yml) is used to automatically run the script every Saturday morning.

## 📂 Repository Structure
The repository contains: 

◽ A README.

◽ A “gitignore” file.

◽ A “requirements.txt” file.

◽ A Jupyter notebook: “problemas.ipynb”.

◽ A Python file: “faang.py”.

◽ A script called “faang.yml”.

◽ Three folders: “data”, “plots”, ".github/workflows/."


## 📖 Notebook Structure
Each assessment is organized by using markdowns, named according to the task, brief description and then the instruction for each task denominated for this subject "Problem" (e.g., problem01, problem02,...)

Within the markdown - Task number and title, you could find:
◽ Code cells in which the solutions to each task are executed.

◽ All relevant explanations and task details written as comments within the task itself.

This approach aims to help keep the notebook clean and focused on the task.

## 📑 About the Tasks
The tasks are designed to:

◽ Test the knowledge acquired in each lesson.

◽ Encourage independent problem-solving.

◽ Require external research to find and apply appropriate solutions.

◽ To be carried out during the semester.

## 📚 Research & References
◽ Throughout the tasks, research and external resources have been cited.

◽ This information has been added to support learning and demonstrate my understanding.

◽ These references can be found in the code comments or in links from reliable sources, such as:

Python Docs
W3Schools

## 💻 Technologies
◽ Python ◽ Git ◽ Github ◽ Jupyter ◽ Matplotlib ◽ yFinance

## 👨‍🏫 Course Information
◽ Professor: Ian McLoughlin .

◽ Module: Computer Infrastructure

◽ Atlantic Tecnhological University

## 👨‍🎓 Author
◽ Student: Tanya San Juan.
