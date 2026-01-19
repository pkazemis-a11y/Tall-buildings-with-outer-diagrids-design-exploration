# Tall Buildings with Outer Diagrids: Design Exploration

Parametric database of 1,000 artificial tall buildings with outer diagrids, analyzed under 7 NGA-West2 ground motions. Includes geometric, structural, and environmental variables, organized for AI/ML studies and early-stage design decision support.

## 📁 Repository Structure

```
├── data/                      # Raw datasets
│   └── database.csv          # Main parametric database (7000+ rows)
├── visualizations/           # Interactive analysis plots
│   ├── Ground motion 1/      # Ground motion 1 analyses
│   └── All ground motions/   # Cross-motion comparative analyses
├── docs/                     # Documentation and resources
├── LICENSE                   # Repository license
└── README.md                 # This file
```

## 📊 Dataset Overview

### Main Database: `database.csv`
- **Records**: 1,000 building models × 7 ground motions = 7,000+ rows
- **Design Variables (X1-X10)**:
  - X1: Top plan geometry side count
  - X2: Bottom plan geometry side count
  - X3: Top/Bottom plan orientation
  - X4: Number of stories
  - X5: Floor height
  - X6: Vertical transformation method
  - X7: Tapering ratio
  - X8: Twisting angle
  - X9: Curvilinear; location of control floor
  - X10: Curvilinear; scale of control floor

- **Structural Outputs**: Mass, displacements, stresses, drift ratios, torsion
- **Seismic Inputs**: 7 NGA-West2 ground motions with characteristics
- **Economic Data**: Construction costs (structure, floor, land), sellable price

## 📈 Visualizations

Interactive HTML visualizations are organized into two categories:

### Ground Motion 1 (Single GM Analysis)
- Height vs Tapering Ratio
- Height vs Twisting Angle
- Maximum inter-storey drift vs height
- Plan side ratio vs twisting angle

### All Ground Motions (Comparative Analysis)
- Maximum acceleration vs height
- Maximum building displacement vs height
- Maximum inter-storey drift vs height
- Von Mises stress vs height (by drift and earthquake)

## 🔍 Key Variables

| Category | Variables |
|----------|-----------|
| **Geometric** | Plan geometry, orientation, height, tapering, twisting, curvilinearity |
| **Structural** | Mass, diagrid angles, stresses (tension, compression, shear), von Mises |
| **Seismic Response** | Acceleration, displacement, inter-storey drift, torsion, reactions |
| **Economic** | Material costs, structural costs, land costs, total costs/area |
| **Ground Motion** | Magnitude, mechanism, distance metrics, site conditions, duration |

## 💻 Usage

This dataset is suitable for:
- Machine learning model development (design optimization, response prediction)
- Parametric sensitivity analysis
- Early-stage design decision support
- Structural performance evaluation under seismic loads
- Cost-benefit analysis of tall building design

## 📚 Ground Motion Data
- **Source**: NGA-West2 database
- **Count**: 7 distinct ground motion records
- **Mechanisms**: Strike-slip, reverse, normal oblique faults
- **Magnitude Range**: ~6.2-6.6
- **Distances**: Rjb, Rrup metrics documented
- **Site Conditions**: Vs30 values provided

## ⚖️ License
See [LICENSE](LICENSE) for details.

## 📝 Citation
If you use this dataset in your research, please cite this repository.

---
**Note**: For questions or issues, please open a GitHub issue or contact the repository maintainer.
