# Visualizations

This directory contains interactive HTML visualizations exploring the relationships between geometric design parameters, structural responses, and seismic performance of 1,000 tall buildings with outer diagrids.

## Available Visualizations

### Multi-Ground Motion Analyses

These visualizations compare responses across all 7 ground motions:

1. **[acceleration_vs_height__vs_gm_id.html](acceleration_vs_height__vs_gm_id.html)**
   - Maximum acceleration vs building height
   - Color-coded by ground motion ID
   - Shows variation in acceleration response across different seismic scenarios

2. **[drift_vs_height_vs_gm_id.html](drift_vs_height_vs_gm_id.html)**
   - Maximum inter-storey drift vs building height
   - Grouped by ground motion
   - Critical for serviceability assessment

3. **[drift_vs_von_mises_vs_height.html](drift_vs_von_mises_vs_height.html)**
   - Drift vs Von Mises stress relationship
   - Color-coded by building height
   - Reveals stress-displacement correlations

4. **[cost_to_tga_vs_displacement_vs_height.html](cost_to_tga_vs_displacement_vs_height.html)**
   - Cost per unit area vs maximum displacement
   - Color-coded by height
   - Economic-performance trade-offs

### Ground Motion 1 Specific Analyses

Detailed parametric studies for a single representative ground motion:

5. **[drift_vs_height_vs_taper_gm1.html](drift_vs_height_vs_taper_gm1.html)**
   - Effect of tapering on drift response
   - Shows how tapered forms influence lateral displacement

6. **[drift_vs_height_vs_twist_gm1.html](drift_vs_height_vs_twist_gm1.html)**
   - Influence of twisting angle on structural response
   - Demonstrates torsional effects in twisted geometries

7. **[drift_vs_top_to_bottom_vs_twist_gm1.html](drift_vs_top_to_bottom_vs_twist_gm1.html)**
   - Plan ratio (top-to-bottom) vs drift
   - Includes twisting angle effects

8. **[drift_vs_total_mass_vs_height_gm1.html](drift_vs_total_mass_vs_height_gm1.html)**
   - Mass-drift relationship
   - Color-coded by building height
   - Explores inertial effects

9. **[total_mass_vs_height_vs_taper_gm1.html](total_mass_vs_height_vs_taper_gm1.html)**
   - Structural mass vs height
   - Shows impact of tapering on material usage

10. **[total_mass_vs_height_vs_twist_gm1.html](total_mass_vs_height_vs_twist_gm1.html)**
    - Mass-height relationship with twisting effects
    - Environmental/sustainability implications

### Geometric Parameter Exploration

11. **[height_vs_drift_vs_curvilinear_location.html](height_vs_drift_vs_curvilinear_location.html)**
    - Curvilinear transformation effects
    - Shows how curved profiles affect performance

## How to Use

1. **Open in Browser**: Each HTML file can be opened directly in any modern web browser
2. **Interactive Features**: 
   - Hover over points for detailed information
   - Zoom and pan to explore specific regions
   - Toggle legend items to filter data
3. **Export**: Most visualizations support image export for publications

## Visualization Technologies

These plots are generated using interactive plotting libraries (likely Plotly or similar), enabling:
- Dynamic filtering and selection
- Multi-dimensional data exploration
- High-quality rendering for presentations

## Key Insights

The visualizations reveal relationships between:
- Building height and structural responses
- Geometric parameters (tapering, twisting, curvilinearity) and structural behavior
- Ground motion variability and response patterns
- Economic, structural, and environmental factors

## Creating New Visualizations

To create additional visualizations from the dataset:

1. Load `data/database.csv`
2. Select relevant variables
3. Use plotting libraries (Plotly, Matplotlib, Seaborn, etc.)
4. Export as interactive HTML or static images

Example variables for exploration:
- Input: X1-X10 (geometric parameters)
- Output: Drift, acceleration, stress, displacement
- Context: Ground motion ID, cost, mass

## Citation

If you use these visualizations in presentations or publications, please cite the associated research paper (see [CITATION.cff](../CITATION.cff)).

## Contact

For questions about specific visualizations or requests for additional plots:
- Open a GitHub issue
- Contact: Pooyan Kazemi (seyedpooyan.kazemi@polimi.it)
