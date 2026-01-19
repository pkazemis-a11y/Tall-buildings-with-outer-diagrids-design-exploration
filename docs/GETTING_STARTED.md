# Getting Started

This guide will help you begin working with the Tall Buildings with Outer Diagrids dataset.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/pkazemis-a11y/Tall-buildings-with-outer-diagrids-design-exploration.git
cd Tall-buildings-with-outer-diagrids-design-exploration
```

### 2. Explore the Data

The main dataset is located at:
```
data/database.csv
```

### 3. View Visualizations

Open any HTML file in the `visualizations/` directory with your web browser:
- Navigate to the `visualizations/` folder
- Double-click any `.html` file to open in your default browser
- Interact with the plots (zoom, pan, hover for details)

## Working with the Data

### Using Python

#### Basic Data Loading

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('data/database.csv')

# View first few rows
print(df.head())

# Check dataset shape
print(f"Dataset shape: {df.shape}")

# View column names
print(df.columns.tolist())
```

#### Example: Filter by Ground Motion

```python
# Get data for ground motion 1
gm1_data = df[df['GM'] == 1]

# Get data for a specific building across all ground motions
building_1 = df[df['Model_ID'] == 1]  # Assuming Model_ID column exists
```

#### Example: Analyze Structural Responses

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Plot drift vs height
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Number of stories (Height)', y='Overall_Max_Drift', hue='GM')
plt.xlabel('Number of Stories')
plt.ylabel('Maximum Drift')
plt.title('Inter-storey Drift vs Building Height')
plt.show()
```

#### Example: Machine Learning Preparation

```python
# Define input features (design variables)
X_columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10']
X = df[X_columns]

# Define target variable (e.g., maximum drift)
y = df['Overall_Max_Drift']

# Split data for training
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### Using R

```r
# Load the dataset
library(readr)
df <- read_csv('data/database.csv')

# View structure
str(df)

# Summary statistics
summary(df)

# Filter by ground motion
library(dplyr)
gm1_data <- df %>% filter(GM == 1)

# Visualization
library(ggplot2)
ggplot(df, aes(x = `Number of stories (Height)`, y = Overall_Max_Drift, color = factor(GM))) +
  geom_point(alpha = 0.5) +
  labs(title = "Drift vs Height by Ground Motion",
       x = "Number of Stories",
       y = "Maximum Drift",
       color = "Ground Motion")
```

### Using Excel

1. Open `data/database.csv` in Microsoft Excel
2. Use filters to explore specific subsets
3. Create pivot tables for summary statistics
4. Generate charts for visualization

**Note**: Excel may have limitations with 7,000+ rows. Consider using Python/R for large-scale analysis.

## Common Use Cases

### 1. Parametric Study

**Goal**: Understand how twisting affects drift

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Filter for a single ground motion
gm1 = df[df['GM'] == 1]

# Create visualization
plt.figure(figsize=(12, 6))
sns.scatterplot(data=gm1, x='X8', y='Overall_Max_Drift', 
                hue='Number of stories (Height)', size='TotalMass',
                sizes=(20, 200), alpha=0.6)
plt.xlabel('Twisting Angle (degrees)')
plt.ylabel('Maximum Inter-storey Drift')
plt.title('Effect of Twisting on Structural Drift')
plt.show()
```

### 2. Machine Learning: Regression

**Goal**: Predict maximum drift from design parameters

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# Prepare data
X = df[['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10']]
y = df['Overall_Max_Drift']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R² Score: {r2:.3f}")
print(f"RMSE: {rmse:.4f}")

# Feature importance
importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)
print("\nFeature Importance:")
print(importance)
```

### 3. Classification Task

**Goal**: Classify buildings by drift performance level

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Create performance categories
df['Drift_Category'] = pd.cut(df['Overall_Max_Drift'], 
                               bins=[0, 0.01, 0.02, float('inf')],
                               labels=['Low', 'Medium', 'High'])

# Prepare data
X = df[['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10']]
y = df['Drift_Category']

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
```

### 4. Multi-Ground Motion Analysis

**Goal**: Compare building performance across different seismic scenarios

```python
# Aggregate across ground motions
building_performance = df.groupby('Model_ID').agg({
    'Overall_Max_Drift': ['mean', 'max', 'std'],
    'Max_Displacement': ['mean', 'max'],
    'Overall_Max_Acc': ['mean', 'max']
}).reset_index()

# Identify robust designs (low variability across GMs)
building_performance['Drift_CV'] = (
    building_performance['Overall_Max_Drift']['std'] / 
    building_performance['Overall_Max_Drift']['mean']
)
robust_designs = building_performance.nsmallest(10, 'Drift_CV')
```

## Data Dictionary

For detailed information about all variables, see:
- [docs/DATASET.md](docs/DATASET.md) - Complete variable descriptions
- [docs/METHODOLOGY.md](docs/METHODOLOGY.md) - Research methodology

## Recommended Tools

### For Data Analysis
- **Python**: pandas, numpy, scikit-learn, matplotlib, seaborn, plotly
- **R**: tidyverse, ggplot2, caret, randomForest
- **MATLAB**: Statistics and Machine Learning Toolbox

### For Visualization
- **Interactive**: Plotly, Bokeh, Altair
- **Static**: Matplotlib, ggplot2, Seaborn
- **3D**: Mayavi, PyVista

### For Machine Learning
- **Traditional ML**: scikit-learn, caret (R)
- **Deep Learning**: TensorFlow, PyTorch, Keras
- **AutoML**: Auto-sklearn, H2O.ai

## Next Steps

1. **Read the Paper**: Understand the research context and methodology
2. **Explore Visualizations**: Get familiar with data patterns
3. **Run Examples**: Try the code examples above
4. **Develop Your Analysis**: Apply to your specific research questions

## Getting Help

- **Issues**: Open a GitHub issue for bugs or questions
- **Documentation**: Check [docs/](docs/) folder
- **Contact**: Email the corresponding author (see README)
- **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## Citation

Remember to cite this work in your research:

```bibtex
@article{kazemi2025tall,
  title={Tall buildings with outer diagrids design exploration: influence of architectural forms on the structural behaviour in the early-stage design},
  author={Kazemi, Pooyan and Entezami, Alireza and Turrin, Michela and Andriotis, Charalampos and Mariani, Stefano and Ghisi, Aldo},
  year={2025},
  doi={10.XXXX/journal.XXXX}
}
```

## Additional Resources

- [README.md](README.md) - Repository overview
- [DATASET.md](docs/DATASET.md) - Dataset documentation
- [METHODOLOGY.md](docs/METHODOLOGY.md) - Research methodology
- [Visualizations README](visualizations/README.md) - Visualization guide
