# Frequently Asked Questions (FAQ)

## General Questions

### What is this repository?

This repository contains a comprehensive database of 1,000 parametrically generated tall buildings with outer diagrid structures. Each building has been analyzed under 7 different seismic ground motions, resulting in 7,000 data records with geometric, structural, economic, and environmental variables.

### Who is this dataset for?

This dataset is designed for:
- **Researchers** in structural engineering, architecture, and AI/ML
- **Architects** seeking quantitative structural feedback in early design stages
- **Structural Engineers** exploring performance-based design
- **Data Scientists** working on building design optimization
- **Graduate Students** in civil engineering and architecture programs

### Is this dataset free to use?

Yes, the dataset is freely available under the MIT License (see [LICENSE](../LICENSE)). However, we ask that you cite our work in any publications or projects that use this data.

## Data Questions

### How many buildings are in the database?

There are **1,000 unique building models**, each analyzed under **7 ground motions**, resulting in **7,000 total records**.

### What makes each building unique?

Each building varies in:
- Plan geometry (3-12 sided polygons for top and bottom)
- Height (number of stories)
- Vertical transformations (tapering, twisting, curvilinear forms)
- Floor height
- Plan orientation
- Geometric proportions

### What structural responses are included?

The database includes:
- Maximum acceleration (overall and directional)
- Maximum displacement (overall and directional)
- Inter-storey drift ratios
- Stresses (tension, compression, shear, Von Mises)
- Base reactions and moments
- Torsional response
- Total structural mass

### What are the ground motions used?

7 ground motion records from the **NGA-West2 database**, with characteristics documented in the dataset.

### Are material properties included?

The current dataset focuses on structural response with linear elastic behavior. Material properties are implicit in the analysis but not explicitly varied as input parameters. Future extensions may include material variations.

## Technical Questions

### What software was used to generate this data?

The database was created using parametric modeling and finite element analysis, with automated generation, computer cluster processing, and data management procedures as described in the research paper.

### Why linear elastic analysis?

Linear elastic analysis was chosen to:
- Enable efficient computation of 7,000 analyses
- Provide a baseline performance assessment
- Support future extensions with nonlinear behavior
- Focus on early-stage design decision-making

Future work will explore material nonlinearity and more complex behavior.

### What loading conditions are considered?

Currently, **seismic loading** (7 ground motions from NGA-West2 database). Future extensions may incorporate:
- Wind loading
- Combined load scenarios
- Additional seismic scenarios

### How were the design parameters chosen?

Parameters were selected to:
- Cover a practical and diverse design space
- Include contemporary tall building forms
- Enable meaningful architectural variations
- Support parametric exploration with AI/ML

## Usage Questions

### What programming languages can I use?

The CSV format is universally compatible. Popular choices:
- **Python**: pandas, scikit-learn, TensorFlow/PyTorch
- **R**: tidyverse, caret, ggplot2
- **MATLAB**: Statistics and Machine Learning Toolbox
- **Julia**: DataFrames.jl, MLJ.jl

See [GETTING_STARTED.md](GETTING_STARTED.md) for examples.

### Can I use this for machine learning?

**Absolutely!** The data is organized specifically for AI/ML applications:
- **Input (X)**: 10 design variables (X1-X10)
- **Output (Y)**: Multiple structural responses
- **Tasks**: Regression, classification, clustering, generative design

### What's a good first analysis to try?

Start with:
1. **Visualization**: Plot drift vs height, color-coded by ground motion
2. **Correlation**: Analyze which geometric parameters most affect drift
3. **Simple ML**: Train a random forest to predict maximum drift
4. **Comparison**: Compare building performance across ground motions

See [GETTING_STARTED.md](GETTING_STARTED.md) for code examples.

### How do I handle multiple ground motions?

Options include:
- **Single GM**: Analyze each ground motion separately
- **Aggregate**: Use mean, max, or envelope across all GMs
- **Multi-output**: Predict responses for all GMs simultaneously
- **Robustness**: Evaluate variability/consistency across GMs

### Can I add my own analyses to the repository?

Yes! We welcome contributions. Please:
1. Read [CONTRIBUTING.md](../CONTRIBUTING.md)
2. Fork the repository
3. Add your analysis with clear documentation
4. Submit a pull request

Or simply share your findings by opening an issue.

## Research Questions

### Has this data been peer-reviewed?

The database and methodology are described in a peer-reviewed research paper (citation details in [CITATION.cff](../CITATION.cff)). The paper is currently under review/published [update as appropriate].

### Where is the paper published?

Publication details:
- **Title**: Tall buildings with outer diagrids design exploration: influence of architectural forms on the structural behaviour in the early-stage design
- **DOI**: 10.XXXX/journal.XXXX *(update when available)*
- **Authors**: Kazemi, P., Entezami, A., Turrin, M., Andriotis, C., Mariani, S., Ghisi, A.

### How should I cite this work?

See [CITATION.cff](../CITATION.cff) for the complete citation. In brief:

```bibtex
@article{kazemi2025tall,
  title={Tall buildings with outer diagrids design exploration...},
  author={Kazemi, Pooyan and others},
  year={2025},
  doi={10.XXXX/journal.XXXX}
}
```

### Are there companion papers?

Yes, a companion paper explores AI applications of this database. Check the main paper references for details.

### Can I collaborate on future extensions?

We welcome academic collaborations! Contact:
- **Pooyan Kazemi** (Corresponding Author)
- Email: seyedpooyan.kazemi@polimi.it
- Department of Civil and Environmental Engineering, Politecnico di Milano

## Limitations and Future Work

### What are the current limitations?

- **Linear elastic behavior**: No material nonlinearity
- **Seismic loading only**: Wind loads not yet included
- **Maximum values**: Time-series features not fully explored
- **Fixed structural system**: Outer diagrids only

### What future extensions are planned?

- **Wind loading** analysis
- **Material nonlinearity**
- **Expanded geometric parameters**
- **More ground motion records**
- **Time-series feature extraction**
- **AI-powered design interfaces**

### Can I request specific analyses?

Yes! Please:
1. Open a GitHub issue with your request
2. Describe the analysis and its value
3. We'll consider it for future updates

### Why isn't [feature X] included?

The current dataset represents Phase 1 of this research. We're continuously working on extensions. If you need specific features:
- Check if they can be derived from existing data
- Request them via GitHub issue
- Consider contributing the analysis yourself

## Data Quality and Validation

### How accurate is the data?

All analyses were performed using validated finite element methods with:
- Quality control checks
- Physical consistency verification
- Comparison with design standards
- Peer-review validation

### Are there known errors?

No known errors at this time. If you discover issues:
1. Verify it's not a data interpretation issue
2. Open a GitHub issue with details
3. We'll investigate and issue corrections if needed

### How often is the data updated?

The current version (v1.0.0) represents the complete Phase 1 dataset. Updates will be versioned and documented in the CHANGELOG.

## Visualization Questions

### What format are the visualizations?

Interactive HTML files that can be opened in any web browser (Chrome, Firefox, Safari, Edge).

### Can I modify the visualizations?

Yes! The HTML files can be:
- Viewed as-is in a browser
- Modified if you have the source plotting code
- Recreated using the CSV data

See [visualizations/README.md](../visualizations/README.md) for details.

### Can I create my own visualizations?

Absolutely! Load the CSV data and create any visualizations you need. Consider sharing interesting ones with the community.

## Contact and Support

### Who do I contact for questions?

- **Technical questions**: Open a GitHub issue
- **Research collaboration**: Email Pooyan Kazemi (seyedpooyan.kazemi@polimi.it)
- **Bug reports**: Open a GitHub issue
- **Citation questions**: See [CITATION.cff](../CITATION.cff)

### How quickly will I get a response?

We aim to respond to GitHub issues within 1-2 weeks. For urgent matters, email the corresponding author directly.

### Is there a user community?

We encourage users to:
- Use GitHub Discussions for community interaction
- Share findings via GitHub issues
- Contribute analyses and improvements
- Cite and reference each other's work

### Can I use this data for commercial purposes?

The MIT License permits commercial use. However:
- Citation is still required
- Consider the ethical implications
- Contact the authors for major commercial applications

---

**Didn't find your answer?**

- Check other documentation: [README](../README.md), [DATASET](DATASET.md), [METHODOLOGY](METHODOLOGY.md), [GETTING_STARTED](GETTING_STARTED.md)
- Open a GitHub issue
- Email: seyedpooyan.kazemi@polimi.it
