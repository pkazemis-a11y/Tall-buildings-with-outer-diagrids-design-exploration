# Dataset Documentation

## Overview
This dataset contains parametric information for 1,000 tall building designs with outer diagrid structures, each analyzed under 7 different ground motions from the NGA-West2 database. The buildings feature diverse architectural forms including curvilinear profiles, tapered geometries, and twisting configurations, with plan geometries ranging from 3- to 12-sided polygons.

**Total Records**: 7,000 rows (1,000 models × 7 ground motions)

**Analysis Type**: Transient time-domain analysis with linear elastic behavior

## File Location
- `data/database.csv`

## Key Features

The database enables:
- **AI/ML Applications**: Classification, regression, neural network training, GANs
- **Early-stage Design Support**: Quantitative structural feedback for architects
- **Performance-based Design**: Evaluation under multiple seismic scenarios
- **Cost-benefit Analysis**: Integration of structural, economic, and environmental variables

## Design Variables (X1-X10)

| Variable | Column Name | Type | Description |
|----------|------------|------|-------------|
| X1 | Top plan geometry side count | Integer | Number of sides of the top plan polygon (e.g., 12 for dodecagon) |
| X2 | Bottom plan geometry side count | Integer | Number of sides of the bottom plan polygon |
| X3 | Top and Bottom plan orientation | Float | Rotational offset between top and bottom plans (degrees) |
| X4 | Number of stories (Height) | Integer | Total building height in stories (ranges: 30-100) |
| X5 | Floor height | Float | Height of each floor (m) |
| X6 | Vertical transformation method | Categorical | Type of vertical variation applied |
| X7 | Tapering | Float | Ratio describing plan size reduction from bottom to top |
| X8 | Twisting Angle | Float | Rotational twist of the building profile (degrees) |
| X9 | Curvilinear; location of control floor | Float | Height parameter for curvilinear transformation |
| X10 | Curvilinear; scale of control floor | Float | Scale parameter for curvilinear transformation |

## Structural Properties

| Column | Description | Unit |
|--------|-------------|------|
| TotalGrossArea | Building floor area | m² |
| AspectRatio | Height to width ratio | - |
| TotalFacadeArea | External surface area | m² |
| DiagridAngleBottom | Diagrid angle at base | degrees |
| DiagridAngleTop | Diagrid angle at top | degrees |
| DiagridAngleAvg | Average diagrid angle | degrees |
| TotalMass | Total structural mass | kg |

## Seismic Response Outputs

### Acceleration
- `Overall_Max_Acc`: Maximum acceleration magnitude
- `Acc_X`, `Acc_Y`: Directional components
- `Acc_Time`: Time of peak acceleration
- `Acc_Floor`: Floor experiencing peak acceleration

### Displacement
- `Max_Displacement`: Maximum absolute displacement
- `Displacement_X`, `Displacement_Y`: Directional components
- `Disp_Time`: Time of peak displacement
- `Disp_Story`: Story with peak displacement

### Inter-storey Drift
- `Overall_Max_Drift`: Maximum inter-storey drift ratio
- `Drift_X`, `Drift_Y`: Directional drift components
- `Drift_Time`: Time of occurrence
- `Drift_Floor`: Location of maximum drift

### Stresses (Diagrid System)
- `Max_Stress_Tension_diagrid`: Peak tensile stress in diagrid
- `Max_Stress_Compression_diagrid`: Peak compressive stress in diagrid
- `Max_Shear_diagrid`: Maximum shear stress in diagrid
- `Max_Von_Mises_diagrid`: Von Mises equivalent stress in diagrid
- Time and story locations for each stress component

### Stresses (Total Building)
- Similar metrics for complete structure (prefixed with `Total_`)

### Reactions & Moments
- `Diagrid_Max_Magnitude_R`: Maximum reaction magnitude in diagrid
- `Diagrid_Max_Magnitude_M`: Maximum moment magnitude in diagrid
- Core and total structure equivalents provided

### Torsion
- `Overall_Max_Torsion`: Maximum torsional response

## Ground Motion Properties

| Column | Description |
|--------|-------------|
| GM | Ground motion ID (1-7) |
| Mean Squared Error | Model accuracy metric |
| Scale Factor | Intensity scaling applied |
| 5-75% Duration | Bracketed duration (sec) |
| 5-95% Duration | Standard duration measure (sec) |
| Arias Intensity | Energy content measure (m/sec) |
| Magnitude | Earthquake magnitude (Mw) |
| Mechanism | Fault mechanism (strike-slip, reverse, normal oblique) |
| Rjb | Joyner-Boore distance (km) |
| Rrup | Rupture distance (km) |
| Vs30 | Average shear wave velocity (m/sec) |
| Lowest Useable Frequency | Frequency cutoff (Hz) |

## Economic Data

| Column | Description | Unit |
|--------|-------------|------|
| Cost of structure | Structural materials cost | $ |
| Cost of floor | Floor system cost | $ |
| Cost of Land | Land acquisition cost | $ |
| Total costs | Sum of all costs | $ |
| Cost to TGA | Total cost per gross area | $/m² |
| Sellable price | Potential market value | $ |

## Data Applications

### Machine Learning Tasks
1. **Regression**: Predict structural responses from geometric parameters
2. **Classification**: Categorize buildings by performance levels
3. **Clustering**: Identify design patterns and archetypes
4. **Dimensionality Reduction**: Explore design space structure

### Design Optimization
- Multi-objective optimization (structural, cost, environmental)
- Constraint satisfaction (drift limits, stress limits)
- Generative design workflows
- Design space exploration

### Structural Analysis
- Parametric sensitivity studies
- Performance-based seismic design
- Comparative analysis across ground motions
- Influence of architectural forms on structural behavior

## Data Quality Notes

- All structural analyses performed with linear elastic assumptions
- Maximum values extracted from time-history responses
- Ground motions scaled according to standard procedures
- Geometric parameters cover a wide but practical design space

## Related Documentation

- [METHODOLOGY.md](METHODOLOGY.md) - Detailed methodology
- [README.md](../README.md) - Repository overview
- Main paper - Complete research context and findings

## Citation

When using this dataset, please cite the associated research paper. See [CITATION.cff](../CITATION.cff) for citation details.
| Total costs/TGA | Cost normalized by area | $/m² |
| Sellable price | Market value estimate | $ |

### Environmental Credits (EC)
Various `EC` columns track environmental impact metrics across different steel grades and floor configurations, along with gross internal area (GIA) calculations.

## Data Quality Notes

- Missing values represented as empty cells for design variables (X7, X9, X10) when not applicable
- All numerical values are continuous where applicable
- Categorical variable X6 contains transformation method codes
- Time values are relative to ground motion start

## Analysis Opportunities

1. **Machine Learning**: Predict seismic response given design parameters
2. **Sensitivity Analysis**: Assess influence of each design variable on response
3. **Optimization**: Find designs minimizing drift/cost while meeting performance criteria
4. **Comparative Studies**: Analyze differences across ground motions
5. **Cost-Benefit Analysis**: Explore trade-offs between economic and structural performance

## File Format
- **Format**: CSV (comma-separated values)
- **Encoding**: UTF-8
- **Delimiter**: Comma (,)
- **Header**: Present in row 1
- **Size**: ~7MB (compressed well in git)

## Citation
Please cite this dataset if used in your research or derived work.
