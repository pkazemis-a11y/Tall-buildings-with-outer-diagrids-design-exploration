# Methodology

## Overview

This document describes the methodology used to generate and analyze the database of 1,000 tall buildings with outer diagrids. The approach combines parametric modeling, automated structural analysis, and comprehensive data organization for AI/ML applications.

## Database Generation

### 1. Parametric Modeling

The database was created through automated generation of building models with the following characteristics:

#### Geometric Parameters (Design Variables X1-X10)

- **Plan Geometry**: 
  - Top and bottom floor plans defined by 3- to 12-sided polygons
  - Allows for diverse plan shapes from triangular to dodecagonal
  
- **Vertical Transformations**:
  - **Curvilinear forms**: Buildings with smooth curved profiles along height
  - **Tapered forms**: Plan size reduction from bottom to top
  - **Twisting**: Rotational transformation along building height
  
- **Height Variation**:
  - Number of stories varying to represent different building heights
  - Floor height as an independent parameter

### 2. Structural Analysis

#### Analysis Type
- **Time-domain transient analysis** 
- **Linear elastic behavior** assumed (for this phase)
- Enables future developments with material nonlinearity

#### Loading Conditions
- **Seismic Loading**: 7 ground motion records from NGA-West2 database
- Each building model analyzed under all 7 ground motions
- Total: 1,000 models × 7 ground motions = 7,000 analyses

#### Structural System
- **Outer diagrid system** as primary lateral load-resisting structure
- Reduces interior core dimensions
- Frees internal space for alternative uses

### 3. Output Variables

#### Structural Response
- Maximum acceleration (overall and directional components)
- Maximum displacement (absolute and directional)
- Inter-storey drift ratios
- Stresses in diagrid elements:
  - Tensile stress
  - Compressive stress
  - Shear stress
  - Von Mises equivalent stress
- Base reactions and moments
- Torsional response

#### Economic Variables
- Structural material costs
- Floor system costs
- Land acquisition costs
- Total construction costs
- Cost per unit area

#### Environmental Considerations
- Total structural mass (related to embodied carbon)
- Material efficiency metrics

## Data Organization

### Input File Management
The generation process includes:
1. Automated creation of parametric building models
2. Generation of input files for structural analysis software
3. Batch processing capability for computer cluster execution

### Output Definition
Systematic collection of:
- Time-history maximum values
- Location information (story, time of occurrence)
- Directional components for multi-directional responses

### Data Storage
- Organized in CSV format for accessibility
- 7,000+ rows (1,000 models × 7 ground motions)
- Multiple columns covering geometric, structural, economic, and seismic parameters

## AI/ML Preparation

The data organization specifically supports:

### Supervised Learning
- **Input (X)**: Geometric design variables (X1-X10)
- **Output (Y)**: Structural response variables

### Potential Applications
1. **Classification**: Categorizing structural performance levels
2. **Regression**: Predicting continuous structural responses
3. **Neural Networks**: Deep learning for complex pattern recognition
4. **Generative Adversarial Networks (GANs)**: Generating novel designs
5. **Generative Design**: Optimization with structural constraints

## Computational Infrastructure

### Analysis Procedure
- Computer cluster for parallel processing
- Automated workflow from model generation to data collection
- Accurate management of input file generation, output definition, and data storage

## Constraints and Considerations

The database considers:
- Structural behavior constraints
- Cost constraints
- Low embodied carbon footprint considerations

## Future Developments

The methodology is designed for extensibility:

1. **Additional Load Cases**:
   - Wind loading
   - Combined load scenarios
   
2. **Material Nonlinearity**:
   - Plastic behavior modeling
   - Progressive collapse analysis
   
3. **Expanded Database**:
   - More ground motion records
   - Additional geometric parameters
   - Different structural systems
   
4. **Time-Series Analysis**:
   - Features beyond maximum values
   - Frequency-domain characteristics
   - Duration effects
   
5. **AI Integration**:
   - Natural language prompts for design
   - Real-time structural feedback
   - Interactive design exploration

## Quality Assurance

The data has been generated through validated procedures with appropriate checks as described in the research paper.

## References

For detailed technical information, refer to the main paper and companion publications on AI applications of this database.
