# 📘 Assignment: Python Data Visualization

## 🎯 Objective

Learn how to create informative charts and graphs in Python using matplotlib or plotly to visually communicate data insights.

## 📝 Tasks

### 🛠️ Create Basic Charts with Matplotlib

#### Description
Use matplotlib to create a bar chart and a line chart from provided or self-generated data.

#### Requirements
Completed program should:

- Import `matplotlib.pyplot` and prepare a dataset (can be hardcoded lists or a CSV file)
- Create a **bar chart** comparing at least 5 categories with labeled axes and a title
- Create a **line chart** showing a trend over time with labeled axes and a title
- Save both charts as `.png` image files using `savefig()`


### 🛠️ Build an Interactive Chart with Plotly

#### Description
Use plotly to recreate one of the charts from Task 1 as an interactive visualization.

#### Requirements
Completed program should:

- Import `plotly.express` or `plotly.graph_objects`
- Create an interactive version of either the bar or line chart from Task 1
- Include hover tooltips that display the exact data values
- Display the chart in the browser using `.show()`


### 🛠️ Combine Multiple Visualizations

#### Description
Create a single figure that displays multiple subplots to tell a complete data story.

#### Requirements
Completed program should:

- Use `matplotlib.pyplot.subplots()` to arrange at least 2 different chart types side by side
- Include a scatter plot as one of the subplots
- Add a shared or individual title for each subplot
- Add a main figure title using `suptitle()`
- Save the combined figure as a `.png` file
